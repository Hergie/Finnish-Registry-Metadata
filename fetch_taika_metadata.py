"""Mirror Statistics Finland's Taika research-data catalogue metadata.

Hits the public REST-XQ API at https://taika.stat.fi and writes verbatim JSON
responses to `raw/datasets.json` and `datasets/<id>/{dataset,variables}.json`.
Rerunnable and idempotent.

Datasets that disappear from the upstream catalogue are moved to
`withdrawn/<id>/` rather than deleted. Taika documents only the current release
of each register, but FIONA research projects run against a delivery frozen at
permit time, so metadata for superseded vintages has to stay available.

Exit codes: 0 ok, 1 catalogue unreachable, 2 some per-dataset fetches failed,
3 withdrawal safety valve tripped.
"""

import json
import os
import shutil
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

BASE = "https://taika.stat.fi"
LANG = "fi"
UA = "Finnish-Registry-Metadata/1.0 (+https://github.com/Hergie/Finnish-Registry-Metadata)"
ROOT = Path(__file__).resolve().parent
RAW_DIR = ROOT / "raw"
DATASETS_DIR = ROOT / "datasets"
WITHDRAWN_DIR = ROOT / "withdrawn"
SLEEP_BETWEEN_CALLS = 0.2

# Unattended weekly runs must survive a transient 5xx from an undocumented API.
FETCH_ATTEMPTS = 3
RETRY_BACKOFF = (1.0, 2.0)

# A truncated catalogue response must never be able to gut the mirror.
MAX_WITHDRAW_FRACTION = 0.20


def dir_name_for(identifier: str) -> str:
    """Taika identifiers carry a trailing `.xml`; directory names drop it."""
    return identifier[:-4] if identifier.endswith(".xml") else identifier


def fetch_json(path):
    url = BASE + path
    req = urllib.request.Request(
        url,
        headers={"Accept": "application/json", "User-Agent": UA},
    )
    err = None
    for attempt in range(1, FETCH_ATTEMPTS + 1):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                raw = resp.read()
        except urllib.error.HTTPError as e:
            # 4xx other than rate-limiting will not fix itself; fail fast.
            if e.code < 500 and e.code != 429:
                print(f"  ! fetch failed: {url} -> {e}", file=sys.stderr)
                return None
            err = e
        except (urllib.error.URLError, TimeoutError) as e:
            err = e
        else:
            try:
                return json.loads(raw.decode("utf-8"))
            except (UnicodeDecodeError, json.JSONDecodeError) as e:
                print(f"  ! parse failed: {url} -> {e}", file=sys.stderr)
                return None

        if attempt < FETCH_ATTEMPTS:
            delay = RETRY_BACKOFF[attempt - 1]
            print(f"  ~ transient error, retrying in {delay:g}s: {url} -> {err}", file=sys.stderr)
            time.sleep(delay)

    print(f"  ! fetch failed after {FETCH_ATTEMPTS} attempts: {url} -> {err}", file=sys.stderr)
    return None


def atomic_write_json(path: Path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2, sort_keys=False)
        f.write("\n")
    os.replace(tmp, path)


def read_identifier(dataset_file: Path, fallback: str) -> str:
    if not dataset_file.exists():
        return fallback
    try:
        ds = json.loads(dataset_file.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return fallback
    return (ds.get("dataset", {}).get("docmeta") or {}).get("identifier") or fallback


def reclaim_reappeared(live_dir_names) -> int:
    """Drop withdrawn copies of datasets that have returned to the catalogue.

    The freshly fetched copy in `datasets/` supersedes it; leaving both would
    produce duplicate grep hits for the same identifier.
    """
    if not WITHDRAWN_DIR.is_dir():
        return 0
    reclaimed = 0
    for entry in sorted(WITHDRAWN_DIR.iterdir()):
        if entry.is_dir() and entry.name in live_dir_names:
            print(f"  ^ back in catalogue, dropping withdrawn copy: {entry.name}")
            shutil.rmtree(entry)
            reclaimed += 1
    return reclaimed


def archive_withdrawn(live_dir_names):
    """Move datasets no longer in the catalogue to `withdrawn/`.

    Returns the list of archived directory names, or None if the safety valve
    tripped, in which case nothing was moved.
    """
    if not DATASETS_DIR.is_dir():
        return []
    present = sorted(d.name for d in DATASETS_DIR.iterdir() if d.is_dir())
    gone = [name for name in present if name not in live_dir_names]
    if not gone:
        return []

    limit = max(1, int(len(present) * MAX_WITHDRAW_FRACTION))
    if len(gone) > limit:
        print(
            f"REFUSING to withdraw {len(gone)} of {len(present)} datasets "
            f"(cap {MAX_WITHDRAW_FRACTION:.0%} = {limit}). The catalogue response "
            "looks truncated. Nothing was moved.",
            file=sys.stderr,
        )
        for name in gone:
            print(f"  ? would withdraw: {name}", file=sys.stderr)
        return None

    WITHDRAWN_DIR.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()
    for name in gone:
        src = DATASETS_DIR / name
        dst = WITHDRAWN_DIR / name
        if dst.exists():
            shutil.rmtree(dst)
        shutil.move(str(src), str(dst))
        # The withdrawal date is only knowable at move time. Recording it as
        # JSON keeps the split clean: the fetcher writes JSON, the builder
        # owns every .md.
        atomic_write_json(
            dst / "withdrawn.json",
            {
                "identifier": read_identifier(dst / "dataset.json", name + ".xml"),
                "withdrawn_on": today,
            },
        )
        print(f"  - withdrawn: {name}")
    return gone


def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    DATASETS_DIR.mkdir(parents=True, exist_ok=True)

    print(f"[1/4] Fetching catalogue list from /restxq/taika/{LANG}/datasets")
    catalogue = fetch_json(f"/restxq/taika/{LANG}/datasets")
    if catalogue is None or "dataset" not in catalogue:
        print("FATAL: could not fetch catalogue list", file=sys.stderr)
        sys.exit(1)
    atomic_write_json(RAW_DIR / "datasets.json", catalogue)

    entries = catalogue["dataset"]
    total = len(entries)
    print(f"      Catalogue has {total} datasets")

    print(f"[2/4] Fetching per-dataset metadata (en route to {DATASETS_DIR.name}/)")
    ok = 0
    failures = []
    # Built from the catalogue, not from fetch success: a transient failure
    # must never be mistaken for a withdrawal.
    live_dir_names = set()
    for i, entry in enumerate(entries, start=1):
        identifier = entry.get("docmeta", {}).get("identifier")
        if not identifier:
            print(f"  [{i:>3}/{total}] missing identifier, skipping", file=sys.stderr)
            failures.append(("<unknown>", "missing identifier"))
            continue

        dir_name = dir_name_for(identifier)
        live_dir_names.add(dir_name)
        out_dir = DATASETS_DIR / dir_name
        print(f"  [{i:>3}/{total}] {dir_name}")

        enc_id = urllib.parse.quote(identifier, safe="")

        ds = fetch_json(f"/restxq/taika/{LANG}/datasets/{enc_id}")
        time.sleep(SLEEP_BETWEEN_CALLS)
        if ds is None:
            failures.append((dir_name, "dataset fetch failed"))
            continue
        atomic_write_json(out_dir / "dataset.json", ds)

        vars_ = fetch_json(f"/restxq/taika/{LANG}/variables/{enc_id}")
        time.sleep(SLEEP_BETWEEN_CALLS)
        if vars_ is None:
            failures.append((dir_name, "variables fetch failed"))
            continue
        atomic_write_json(out_dir / "variables.json", vars_)

        ok += 1

    print("[3/4] Reconciling against the catalogue")
    reclaim_reappeared(live_dir_names)
    archived = archive_withdrawn(live_dir_names)

    print(f"[4/4] Done. Fetched {ok}/{total} datasets, {len(failures)} failures.")
    if archived:
        print(f"      Withdrew {len(archived)} dataset(s) to {WITHDRAWN_DIR.name}/")
    if failures:
        print("Failures:")
        for name, reason in failures:
            print(f"  - {name}: {reason}")

    if archived is None:
        sys.exit(3)
    if failures:
        sys.exit(2)


if __name__ == "__main__":
    main()
