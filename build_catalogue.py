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
        lines.append("## Kuvaus / Description")
        lines.append("")
        lines.append(description)
        lines.append("")

    if variables:
        lines.append(f"## Muuttujat / Variables ({len(variables)})")
        lines.append("")
        lines.append("| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |")
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
        lines.append("### Muuttujien määritelmät / Variable definitions")
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
                meta_bits.append(f"**Yksikkö / Unit:** {var['measunit']}")
            if var.get("classification"):
                meta_bits.append(f"**Luokitus / Classification:** {var['classification']}")
            if var.get("variablegroups"):
                meta_bits.append(f"**Ryhmä / Group:** {var['variablegroups']}")
            if meta_bits:
                lines.append(" · ".join(meta_bits))
                lines.append("")
            conceptdef = (var.get("conceptdef") or "").strip()
            if conceptdef:
                lines.append(conceptdef)
                lines.append("")
    else:
        lines.append("## Muuttujat / Variables")
        lines.append("")
        lines.append("_Taika ei listaa tämän aineiston muuttujia. / Taika does not list variables for this dataset._")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("[← Takaisin luetteloon / Back to catalogue](../../README.md)")
    lines.append("")

    (dir_path / "README.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


def write_top_readme(rows: list, fetched_date: str) -> None:
    lines = []
    lines.append("# Finnish Registry Metadata")
    lines.append("")
    lines.append(
        "Paikallinen peilaus Tilastokeskuksen **Taika**-tutkimusaineistokatalogista "
        "([taika.stat.fi](https://taika.stat.fi/)). "
        f"{len(rows)} aineistoa, päivitetty {fetched_date}."
    )
    lines.append("")
    lines.append(
        "Local mirror of Statistics Finland's **Taika** research-data catalogue "
        f"({len(rows)} datasets, refreshed {fetched_date})."
    )
    lines.append("")
    lines.append("## Käyttö / Usage")
    lines.append("")
    lines.append(
        "Claude-agenttien tulee konsultoida tätä arkistoa kirjoittaessaan koodia, "
        "joka lukee Tilastokeskuksen rekisteriaineistoja (FOLK, EDUC, SES, FLEED, YA221, kuolemansyyt, "
        "perintöverot jne.). Muuttujatiedot löytyvät kunkin aineiston "
        "`datasets/<tunnus>/README.md`-tiedostosta tai raakana `variables.json`-tiedostosta."
    )
    lines.append("")
    lines.append("## Päivitys / Refresh")
    lines.append("")
    lines.append("```")
    lines.append("python fetch_taika_metadata.py && python build_catalogue.py")
    lines.append("```")
    lines.append("")
    lines.append("Älä muokkaa `raw/`- tai `datasets/`-hakemistoja käsin — ne generoidaan. "
                 "Do not hand-edit `raw/` or `datasets/` — both trees are regenerated.")
    lines.append("")
    lines.append("## Luettelo / Catalogue")
    lines.append("")
    lines.append("| Tunnus / Identifier | Aihe / Subject | Kattavuus / Coverage | #Var | #Obs | |")
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
    lines.append("## Lähteet ja rajoitukset / Source notes")
    lines.append("")
    lines.append(
        "- Taustalla on Taikan julkinen REST-XQ-rajapinta "
        "(`/restxq/taika/fi/datasets`, `/restxq/taika/fi/datasets/{id}`, `/restxq/taika/fi/variables/{id}`). "
        "Rajapintaa ei ole virallisesti dokumentoitu, mutta se on julkinen eikä vaadi autentikointia."
    )
    lines.append(
        "- Arkisto perustuu suomenkieliseen rajapintaan. Englanninkielinen rajapinta "
        "(`/restxq/taika/en/datasets`) on kattavuudeltaan paljon suppeampi "
        "(noin 84 aineistoa vs. suomen 312), joten sitä ei käytetä."
    )
    lines.append(
        "- `statmeta`-kenttä on Taikassa yleensä placeholder (`\"metaa...\"`) ja tallennetaan sellaisenaan."
    )
    lines.append(
        "- Kahdeksalla SURVEY-aineistolla muuttujaluettelo sisältää Taikan placeholder-sentinel-arvon "
        "(`emptyvariablenameforcossicreatedbycsmetaedit`); se suodatetaan pois READMEsta."
    )
    lines.append(
        "- **Henkilötunnusmuuttuja / Person ID variable:** Taika dokumentoi henkilön yksilöivän tunnisteen nykyään nimellä `hid_e`. "
        "Aiemmissa aineistotoimituksissa sama tunniste kulki nimellä `shnro`, ja Tilastokeskus on vaihtanut muuttujan nimen. "
        "Osa sisarprojekteista (mm. Student-Debt-Project, Inheritance-Project) työskentelee edelleen vanhemmilla `shnro`-toimituksilla — "
        "tarkista kunkin projektin `CLAUDE.md` ennen kuin oletat muuttujan nimen. "
        "_Taika now documents the person identifier as `hid_e`; older deliveries called it `shnro`. Several sibling projects still use the older `shnro` deliveries — check each project's CLAUDE.md before assuming a variable name._"
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
