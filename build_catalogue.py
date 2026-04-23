"""Generate human-readable Markdown catalogue from the raw Taika JSON mirror.

Reads `raw/datasets.json` and every `datasets/<id>/{dataset,variables}.json`,
writes `README.md` (top-level catalogue) and one `datasets/<id>/README.md` per
dataset. Deterministic — sorted output so re-runs produce clean git diffs.
"""

import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RAW_FILE = ROOT / "raw" / "datasets.json"
DATASETS_DIR = ROOT / "datasets"
README_FILE = ROOT / "README.md"

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


def write_dataset_readme(dir_path: Path, docmeta: dict, variables: list) -> None:
    identifier = docmeta.get("identifier") or dir_path.name
    subject = (docmeta.get("subject") or identifier).strip()

    lines = []
    lines.append(f"# {subject}")
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


def write_top_readme(rows: list, fetched_date: str) -> None:
    lines = []
    lines.append("# Finnish Registry Metadata")
    lines.append("")
    lines.append(
        "Local mirror of Statistics Finland's **Taika** research-data catalogue "
        f"([taika.stat.fi](https://taika.stat.fi/)) — {len(rows)} datasets, refreshed {fetched_date}."
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
        "and research projects. Give your LLM assistant a short description of your "
        "particular setup — the directory where the files live and whether they are SAS, "
        "Stata, or CSV — so the generated code runs on the first try."
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
        "(`/restxq/taika/en/datasets`) covers only about 84 of the 312 datasets."
    )
    lines.append(
        "- The `statmeta` field is usually a Taika placeholder (`\"metaa...\"`) and is stored verbatim."
    )
    lines.append(
        "- Eight SURVEY datasets list a placeholder sentinel variable "
        "(`emptyvariablenameforcossicreatedbycsmetaedit`) instead of a real variable list; it is filtered out."
    )
    lines.append(
        "- **Person ID variable:** Taika currently documents the person-level identifier as `hid_e`. "
        "Older data deliveries used `shnro` — Statistics Finland renamed the variable. Some tables "
        "may still expose the identifier under other names."
    )
    lines.append(
        "- **Generated file:** this `README.md` is produced by `build_catalogue.py` along with the "
        "312 per-dataset `datasets/<id>/README.md` files. Do not edit by hand — changes will be "
        "overwritten on the next refresh."
    )
    lines.append("")
    README_FILE.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def main():
    raw = json.loads(RAW_FILE.read_text(encoding="utf-8"))
    catalogue = raw.get("dataset", [])
    if not catalogue:
        raise SystemExit("raw/datasets.json has no 'dataset' key — did you run the fetcher?")

    fetched_date = date.fromtimestamp(RAW_FILE.stat().st_mtime).isoformat()

    rows = []
    skipped = 0
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
    write_top_readme(rows, fetched_date)

    print(f"Wrote {len(rows)} per-dataset READMEs and top-level README.md ({skipped} skipped).")


if __name__ == "__main__":
    main()
