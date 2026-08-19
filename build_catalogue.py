"""Generate human-readable Markdown catalogue from the raw Taika JSON mirror.

Reads `raw/datasets.json` and every `datasets/<id>/{dataset,variables}.json`,
writes `README.md` (top-level catalogue) and one `datasets/<id>/README.md` per
dataset. Deterministic — sorted output so re-runs produce clean git diffs.

Also regenerates `withdrawn/<id>/README.md` for datasets the fetcher has moved
out of the live catalogue, each stamped with a withdrawal banner, plus a
`withdrawn/README.md` index.
"""

import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RAW_FILE = ROOT / "raw" / "datasets.json"
DATASETS_DIR = ROOT / "datasets"
WITHDRAWN_DIR = ROOT / "withdrawn"
README_FILE = ROOT / "README.md"
WITHDRAWN_README = WITHDRAWN_DIR / "README.md"

EMPTY_VAR_SENTINEL = "emptyvariablenameforcossicreatedbycsmetaedit"


def md_escape_cell(value) -> str:
    """Escape a value for a Markdown table cell."""
    if value is None:
        return "—"
    s = str(value).strip()
    if not s:
        return "—"
    s = s.replace("|", "\\|").replace("\r", "").replace("\n", " ")
    return s


def format_number(value) -> str:
    if value is None:
        return "—"
    s = str(value).strip()
    if not s:
        return "—"
    try:
        n = int(s)
        return f"{n:,}"
    except ValueError:
        return s


def has_sentinel(variables_json) -> bool:
    """True if Taika returned the placeholder 'no variables' sentinel."""
    v = variables_json.get("variables")
    if isinstance(v, dict):
        v = [v]
    if not isinstance(v, list):
        return False
    return any(
        isinstance(var, dict) and var.get("identifier") == EMPTY_VAR_SENTINEL
        for var in v
    )


def normalize_variables(variables_json):
    """Return a list of variable dicts, filtering out placeholder sentinels."""
    v = variables_json.get("variables")
    if v is None:
        return []
    if isinstance(v, dict):
        v = [v]
    if not isinstance(v, list):
        return []
    result = []
    for var in v:
        if not isinstance(var, dict):
            continue
        if var.get("identifier") == EMPTY_VAR_SENTINEL:
            continue
        result.append(var)
    return result


def write_dataset_readme(dir_path: Path, docmeta: dict, variables: list, withdrawn_on=None) -> None:
    identifier = docmeta.get("identifier") or dir_path.name
    subject = (docmeta.get("subject") or identifier).strip()

    lines = []
    lines.append(f"# {subject}")
    lines.append("")
    if withdrawn_on:
        lines.append(
            f"> ⚠️ **Withdrawn from Taika on {withdrawn_on}.** This dataset is no longer in "
            "Statistics Finland's current catalogue — it has typically been superseded by a newer "
            "vintage. It is kept here because FIONA projects run against the delivery frozen at "
            "permit time, so this may still be the metadata that matches your data. Confirm the "
            "vintage against the actual files in your project before relying on it."
        )
        lines.append("")
    lines.append(f"- **Identifier:** `{identifier}`")
    doi = docmeta.get("doi")
    if doi:
        lines.append(f"- **DOI:** `{doi}`")
    lines.append(f"- **Temporal coverage:** {docmeta.get('coveragetemporal') or '—'}")
    lines.append(f"- **Published:** {docmeta.get('published_day') or '—'}")
    lines.append(f"- **Organisation:** {docmeta.get('orgname') or '—'}")
    lines.append(f"- **Variable count:** {format_number(docmeta.get('variable_count'))}")
    lines.append(f"- **Observation count:** {format_number(docmeta.get('line_count'))}")
    population = (docmeta.get("coveragepopulation") or "").strip()
    if population:
        lines.append(f"- **Population:** {population}")
    rr1 = (docmeta.get("resourcerelation_1") or "").strip()
    if rr1:
        lines.append(f"- **Source:** {rr1}")
    rr2 = (docmeta.get("resourcerelation_2") or "").strip()
    if rr2:
        lines.append(f"- **Related:** {rr2}")
    keywords = (docmeta.get("keywords") or "").strip()
    if keywords:
        lines.append(f"- **Keywords:** {keywords}")
    lines.append("")

    description = (docmeta.get("contentdescription") or "").strip()
    if description:
        lines.append("## Description")
        lines.append("")
        lines.append(description)
        lines.append("")

    if variables:
        lines.append(f"## Variables ({len(variables)})")
        lines.append("")
        lines.append("| Identifier | Name | Unit | Classification | Group |")
        lines.append("|---|---|---|---|---|")
        for var in variables:
            lines.append(
                "| `{ident}` | {name} | {unit} | {classif} | {group} |".format(
                    ident=md_escape_cell(var.get("identifier")),
                    name=md_escape_cell(var.get("variablename")),
                    unit=md_escape_cell(var.get("measunit")),
                    classif=md_escape_cell(var.get("classification")),
                    group=md_escape_cell(var.get("variablegroups")),
                )
            )
        lines.append("")
        lines.append("### Variable definitions")
        lines.append("")
        for var in variables:
            ident = var.get("identifier") or "(no identifier)"
            name = (var.get("variablename") or "").strip()
            header = f"#### `{ident}`"
            if name:
                header += f" — {name}"
            lines.append(header)
            lines.append("")
            meta_bits = []
            if var.get("measunit"):
                meta_bits.append(f"**Unit:** {var['measunit']}")
            if var.get("classification"):
                meta_bits.append(f"**Classification:** {var['classification']}")
            if var.get("variablegroups"):
                meta_bits.append(f"**Group:** {var['variablegroups']}")
            if meta_bits:
                lines.append(" · ".join(meta_bits))
                lines.append("")
            conceptdef = (var.get("conceptdef") or "").strip()
            if conceptdef:
                lines.append(conceptdef)
                lines.append("")
    else:
        lines.append("## Variables")
        lines.append("")
        lines.append("_Taika does not list variables for this dataset._")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("[← Back to catalogue](../../README.md)")
    lines.append("")

    (dir_path / "README.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


def write_top_readme(rows: list, fetched_date: str, withdrawn_rows: list, sentinel_count: int) -> None:
    lines = []
    lines.append("# Finnish Registry Metadata")
    lines.append("")
    lines.append(
        "Local mirror of Statistics Finland's **Taika** research-data catalogue "
        f"([taika.stat.fi](https://taika.stat.fi/)) — {len(rows)} datasets, "
        f"last upstream change {fetched_date}."
    )
    lines.append("")
    lines.append(
        "A scheduled GitHub Actions job checks Taika every Monday and commits only when something "
        "actually changed, so an older date here means upstream has been stable, not that the "
        "mirror has been abandoned. The [workflow runs]"
        "(https://github.com/Hergie/Finnish-Registry-Metadata/actions/workflows/refresh-catalogue.yml) "
        "are the record of when checks happened."
    )
    lines.append("")
    lines.append("## What this is")
    lines.append("")
    lines.append(
        "This repository mirrors the responses of Statistics Finland's public Taika REST-XQ "
        "research-data catalogue API into a local, greppable, offline-readable tree. For each "
        "dataset the raw JSON is preserved (`raw/` and `datasets/<id>/dataset.json`, "
        "`variables.json`) alongside a generated Markdown view (`datasets/<id>/README.md`)."
    )
    lines.append("")
    lines.append(
        "The mirrored content itself (dataset subjects, descriptions, variable concept "
        "definitions) is in Finnish — that is the authoritative language of Statistics Finland's "
        "metadata, and the English Taika endpoint covers only a fraction of the datasets. The "
        "scaffolding around that content is in English."
    )
    lines.append("")
    lines.append("## Who this is for")
    lines.append("")
    lines.append(
        "Researchers writing code against Statistics Finland register data (FOLK, EDUC, SES, "
        "FLEED, FIRM_*, cause-of-death, inheritance-tax registers, …) inside the FIONA remote-"
        "access environment. Taika's web UI is not browsable offline, the API is undocumented, "
        "and variable definitions are not greppable — this archive fixes all three. Especially "
        "useful if you write code with an LLM coding assistant and want the variable "
        "definitions available directly in-context."
    )
    lines.append("")
    lines.append("## License")
    lines.append("")
    lines.append(
        "Scripts and generated documentation are dedicated to the public domain under CC0-1.0. "
        "The mirrored JSON files under `raw/` and `datasets/` are verbatim responses from "
        "Statistics Finland's Taika API and are **not** covered by the CC0 dedication; downstream "
        "republishers should credit Tilastokeskus as the source. See `LICENSE`."
    )
    lines.append("")
    lines.append("## Data vintage — read this before using a variable definition")
    lines.append("")
    lines.append(
        "**Taika documents the data Statistics Finland offers today. Your FIONA project uses the "
        "delivery frozen when your permit was granted.** Those are not the same thing, and the "
        "mismatch grows the longer a project runs."
    )
    lines.append("")
    lines.append(
        "Statistics Finland reissues most registers annually under a new identifier. `FOLK_19872023_"
        "jua_perus24_001` and `FOLK_19872025_jua_perus26_001` are the same register, two vintages "
        "apart. Between vintages, variables are added, dropped, renamed, and occasionally "
        "redefined — the `shnro` → `hid_e` person-identifier rename noted below is exactly this. A "
        "definition read from the wrong vintage is *quietly* wrong: the code runs, the variable "
        "exists, the numbers mean something slightly different."
    )
    lines.append("")
    lines.append("So before relying on any definition in this archive:")
    lines.append("")
    lines.append(
        "1. **Compare the vintage.** Check the identifier's version suffix (`perus24` vs `perus26`) "
        "and its year span (`FOLK_19872023_` vs `FOLK_19872025_`) against the file names actually "
        "present in your FIONA project directory."
    )
    lines.append(
        "2. **If they differ, look in [`withdrawn/`](./withdrawn/README.md).** Superseded datasets "
        "are archived there rather than deleted, precisely so pinned projects keep their metadata. "
        "Each carries the date Taika dropped it."
    )
    lines.append(
        "3. **Treat the data file as final authority.** If the metadata and the actual columns "
        "disagree, the file wins — check the real variable list before debugging your code."
    )
    lines.append("")
    if withdrawn_rows:
        lines.append(
            f"_{len(withdrawn_rows)} superseded dataset(s) are currently archived in "
            "[`withdrawn/`](./withdrawn/README.md)._"
        )
        lines.append("")
    lines.append("## Usage")
    lines.append("")
    lines.append(
        "LLM coding assistants should consult this archive when writing code that reads Statistics "
        "Finland register data (FOLK, EDUC, SES, FLEED, YA221, cause-of-death, inheritance-tax, "
        "etc.). Variable-level documentation lives in each dataset's `datasets/<id>/README.md` or "
        "in the raw `variables.json`."
    )
    lines.append("")
    lines.append("### Example")
    lines.append("")
    lines.append(
        "A researcher preparing R code locally for upload to FIONA "
        "could ask their LLM assistant:"
    )
    lines.append("")
    lines.append(
        "> *\"Write R code that loads FOLK tulotieto for 2020 and reports the mean and "
        "median of disposable money income across the full resident population.\"*"
    )
    lines.append("")
    lines.append(
        "With this repository available, the assistant identifies the matching dataset, "
        "grep-searches its per-dataset variable list to find that disposable money income "
        "is stored in `kturaha` (*käytettävissä olevat rahatulot*), confirms the population "
        "scope from the dataset README, and produces code without asking you which "
        "variable to use:"
    )
    lines.append("")
    lines.append("```r")
    lines.append("library(haven)")
    lines.append("library(data.table)")
    lines.append("")
    lines.append("tulo_2020 <- as.data.table(")
    lines.append("  read_sas(\"FOLK_TULO_C/folk_tulo_2020_1.sas7bdat\")")
    lines.append(")")
    lines.append("")
    lines.append("# kturaha = käytettävissä olevat rahatulot (disposable money income).")
    lines.append("# FOLK tulotieto is the full resident population, so no filter is needed.")
    lines.append("summary_stats <- tulo_2020[, .(")
    lines.append("  n      = .N,")
    lines.append("  mean   = mean(kturaha, na.rm = TRUE),")
    lines.append("  median = median(kturaha, na.rm = TRUE)")
    lines.append(")]")
    lines.append("")
    lines.append("print(summary_stats)")
    lines.append("```")
    lines.append("")
    lines.append(
        "The exact folder layout and file-naming convention vary between FIONA releases "
        "and research projects. Give your LLM assistant information on your particular "
        "setup — the directory where the files live, the file names, and whether they "
        "are SAS, Stata, or CSV — so the generated code (ideally) runs on the first try."
    )
    lines.append("")
    lines.append("## Refresh")
    lines.append("")
    lines.append("```")
    lines.append("python fetch_taika_metadata.py && python build_catalogue.py")
    lines.append("```")
    lines.append("")
    lines.append("Do not hand-edit `raw/` or `datasets/` — both trees are regenerated.")
    lines.append("")
    lines.append("## Catalogue")
    lines.append("")
    lines.append("| Identifier | Subject | Coverage | #Var | #Obs | |")
    lines.append("|---|---|---|---|---|---|")
    for row in rows:
        lines.append(
            "| `{ident}` | {subject} | {coverage} | {nvars} | {nobs} | [→](./datasets/{dir_name}/README.md) |".format(
                ident=md_escape_cell(row["identifier"]),
                subject=md_escape_cell(row["subject"]),
                coverage=md_escape_cell(row["coverage"]),
                nvars=format_number(row["variable_count"]),
                nobs=format_number(row["line_count"]),
                dir_name=row["dir_name"],
            )
        )
    lines.append("")
    lines.append("## Source notes")
    lines.append("")
    lines.append(
        "- The archive is built against Taika's public REST-XQ API "
        "(`/restxq/taika/fi/datasets`, `/restxq/taika/fi/datasets/{id}`, `/restxq/taika/fi/variables/{id}`). "
        "The endpoint is undocumented but public and does not require authentication."
    )
    lines.append(
        "- The Finnish endpoint is used because the English one "
        "(`/restxq/taika/en/datasets`) covers only about a third of the datasets, and Finnish is "
        "the canonical metadata language at Statistics Finland."
    )
    lines.append(
        "- The `statmeta` field is usually a Taika placeholder (`\"metaa...\"`) and is stored verbatim."
    )
    lines.append(
        f"- {sentinel_count} datasets (all SURVEY) list a placeholder sentinel variable "
        "(`emptyvariablenameforcossicreatedbycsmetaedit`) instead of a real variable list; it is filtered out."
    )
    lines.append(
        "- **Person ID variable:** Taika currently documents the person-level identifier as `hid_e`. "
        "Older data deliveries used `shnro` — Statistics Finland renamed the variable. Some tables "
        "may still expose the identifier under other names."
    )
    lines.append(
        "- **Withdrawn datasets:** when Taika drops a dataset the fetcher moves it to "
        "`withdrawn/<id>/` instead of deleting it, so metadata for superseded vintages stays "
        "greppable. `datasets/` therefore always mirrors Taika exactly; `withdrawn/` is everything "
        "it used to offer."
    )
    lines.append(
        "- **Generated file:** this `README.md` is produced by `build_catalogue.py` along with the "
        f"{len(rows)} per-dataset `datasets/<id>/README.md` files. Do not edit by hand — changes "
        "will be overwritten on the next refresh."
    )
    lines.append("")
    README_FILE.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def write_withdrawn_readme(withdrawn_rows: list) -> None:
    """Index of datasets Taika no longer lists, kept for pinned FIONA vintages."""
    lines = []
    lines.append("# Withdrawn datasets")
    lines.append("")
    lines.append(
        f"{len(withdrawn_rows)} dataset(s) that Statistics Finland has removed from the Taika "
        "catalogue. They are preserved here rather than deleted because FIONA research projects "
        "run against a data delivery frozen at permit time — if your project predates the "
        "withdrawal, the metadata that matches your files is in here, not in "
        "[`../datasets/`](../README.md)."
    )
    lines.append("")
    lines.append(
        "Most entries were superseded by a newer annual vintage of the same register. Check "
        "[the main catalogue](../README.md) for the current replacement, and see its **Data "
        "vintage** section for how to tell which one your project actually uses."
    )
    lines.append("")
    lines.append("| Identifier | Subject | Coverage | Withdrawn | |")
    lines.append("|---|---|---|---|---|")
    for row in withdrawn_rows:
        lines.append(
            "| `{ident}` | {subject} | {coverage} | {when} | [→](./{dir_name}/README.md) |".format(
                ident=md_escape_cell(row["identifier"]),
                subject=md_escape_cell(row["subject"]),
                coverage=md_escape_cell(row["coverage"]),
                when=md_escape_cell(row["withdrawn_on"]),
                dir_name=row["dir_name"],
            )
        )
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("[← Back to catalogue](../README.md)")
    lines.append("")
    WITHDRAWN_README.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def build_withdrawn(live_dir_names: set) -> list:
    """Regenerate READMEs for archived datasets; return index rows."""
    if not WITHDRAWN_DIR.is_dir():
        return []

    withdrawn_rows = []
    for dir_path in sorted(p for p in WITHDRAWN_DIR.iterdir() if p.is_dir()):
        # A dataset that returned to the catalogue is served from datasets/;
        # the fetcher removes the stale copy, but skip it here too.
        if dir_path.name in live_dir_names:
            continue

        dataset_file = dir_path / "dataset.json"
        variables_file = dir_path / "variables.json"
        if not dataset_file.exists() or not variables_file.exists():
            print(f"WARNING: withdrawn/{dir_path.name} is missing JSON, skipping")
            continue

        marker = {}
        marker_file = dir_path / "withdrawn.json"
        if marker_file.exists():
            marker = json.loads(marker_file.read_text(encoding="utf-8"))
        withdrawn_on = marker.get("withdrawn_on") or "an unrecorded date"

        ds = json.loads(dataset_file.read_text(encoding="utf-8"))
        docmeta = ds.get("dataset", {}).get("docmeta") or {}
        variables = normalize_variables(json.loads(variables_file.read_text(encoding="utf-8")))

        write_dataset_readme(dir_path, docmeta, variables, withdrawn_on=withdrawn_on)

        identifier = docmeta.get("identifier") or marker.get("identifier") or dir_path.name
        withdrawn_rows.append({
            "identifier": identifier,
            "dir_name": dir_path.name,
            "subject": docmeta.get("subject") or identifier,
            "coverage": docmeta.get("coveragetemporal"),
            "withdrawn_on": marker.get("withdrawn_on"),
        })

    withdrawn_rows.sort(key=lambda r: r["identifier"])
    return withdrawn_rows


def main():
    raw = json.loads(RAW_FILE.read_text(encoding="utf-8"))
    catalogue = raw.get("dataset", [])
    if not catalogue:
        raise SystemExit("raw/datasets.json has no 'dataset' key — did you run the fetcher?")

    fetched_date = date.fromtimestamp(RAW_FILE.stat().st_mtime).isoformat()

    rows = []
    skipped = 0
    sentinel_count = 0
    for entry in catalogue:
        docmeta = entry.get("docmeta") or {}
        identifier = docmeta.get("identifier")
        if not identifier:
            skipped += 1
            continue
        dir_name = identifier[:-4] if identifier.endswith(".xml") else identifier
        dir_path = DATASETS_DIR / dir_name
        dataset_file = dir_path / "dataset.json"
        variables_file = dir_path / "variables.json"
        if not dataset_file.exists() or not variables_file.exists():
            print(f"WARNING: missing files for {dir_name}, skipping")
            skipped += 1
            continue

        ds = json.loads(dataset_file.read_text(encoding="utf-8"))
        full_docmeta = ds.get("dataset", {}).get("docmeta") or docmeta
        vars_json = json.loads(variables_file.read_text(encoding="utf-8"))
        variables = normalize_variables(vars_json)
        if has_sentinel(vars_json):
            sentinel_count += 1

        write_dataset_readme(dir_path, full_docmeta, variables)

        rows.append({
            "identifier": identifier,
            "dir_name": dir_name,
            "subject": full_docmeta.get("subject") or identifier,
            "coverage": full_docmeta.get("coveragetemporal"),
            "variable_count": full_docmeta.get("variable_count"),
            "line_count": full_docmeta.get("line_count"),
        })

    rows.sort(key=lambda r: r["identifier"])

    live_dir_names = {r["dir_name"] for r in rows}
    withdrawn_rows = build_withdrawn(live_dir_names)

    write_top_readme(rows, fetched_date, withdrawn_rows, sentinel_count)
    if withdrawn_rows:
        write_withdrawn_readme(withdrawn_rows)
    elif WITHDRAWN_README.exists():
        WITHDRAWN_README.unlink()

    print(f"Wrote {len(rows)} per-dataset READMEs and top-level README.md ({skipped} skipped).")
    if withdrawn_rows:
        print(f"Wrote {len(withdrawn_rows)} withdrawn READMEs and withdrawn/README.md.")


if __name__ == "__main__":
    main()
