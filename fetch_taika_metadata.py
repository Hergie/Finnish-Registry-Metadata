"""Mirror Statistics Finland's Taika research-data catalogue metadata.

Hits the public REST-XQ API at https://taika.stat.fi and writes verbatim JSON
responses to `raw/datasets.json` and `datasets/<id>/{dataset,variables}.json`.
Rerunnable and idempotent.
"""

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

BASE = "https://taika.stat.fi"
LANG = "fi"
UA = "Finnish-Registry-Metadata/1.0 (+https://taika.stat.fi)"
ROOT = Path(__file__).resolve().parent
RAW_DIR = ROOT / "raw"
DATASETS_DIR = ROOT / "datasets"
SLEEP_BETWEEN_CALLS = 0.2


def fetch_json(path):
    url = BASE + path
    req = urllib.request.Request(
        url,
        headers={"Accept": "application/json", "User-Agent": UA},
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            raw = resp.read()
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as e:
        print(f"  ! fetch failed: {url} -> {e}", file=sys.stderr)
        return None
    try:
        return json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as e:
        print(f"  ! parse failed: {url} -> {e}", file=sys.stderr)
        return None


def atomic_write_json(path: Path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2, sort_keys=False)
        f.write("\n")
    os.replace(tmp, path)


def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    DATASETS_DIR.mkdir(parents=True, exist_ok=True)

    print(f"[1/3] Fetching catalogue list from /restxq/taika/{LANG}/datasets")
    catalogue = fetch_json(f"/restxq/taika/{LANG}/datasets")
    if catalogue is None or "dataset" not in catalogue:
        print("FATAL: could not fetch catalogue list", file=sys.stderr)
        sys.exit(1)
    atomic_write_json(RAW_DIR / "datasets.json", catalogue)

    entries = catalogue["dataset"]
    total = len(entries)
    print(f"      Catalogue has {total} datasets")

    print(f"[2/3] Fetching per-dataset metadata (en route to {DATASETS_DIR.name}/)")
    ok = 0
    failures = []
    for i, entry in enumerate(entries, start=1):
        identifier = entry.get("docmeta", {}).get("identifier")
        if not identifier:
            print(f"  [{i:>3}/{total}] missing identifier, skipping", file=sys.stderr)
            failures.append(("<unknown>", "missing identifier"))
            continue

        dir_name = identifier[:-4] if identifier.endswith(".xml") else identifier
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

    print(f"[3/3] Done. Fetched {ok}/{total} datasets, {len(failures)} failures.")
    if failures:
        print("Failures:")
        for name, reason in failures:
            print(f"  - {name}: {reason}")
        sys.exit(2)


if __name__ == "__main__":
    main()
