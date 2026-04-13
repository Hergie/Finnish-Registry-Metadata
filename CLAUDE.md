# CLAUDE.md

This repository is a local mirror of the **Taika** research-data catalogue operated by Statistics Finland (Tilastokeskus), available at <https://taika.stat.fi/>. Taika documents every unit-level research dataset that Statistics Finland makes available to permit-holding researchers through the FIONA remote-access environment. The purpose of this archive is to give Claude sessions running in sibling research projects under `C:/Users/vihriae2/ResearchGit/` authoritative, offline access to variable definitions, dataset coverage, population descriptions, and data-source documentation — so code using these registers doesn't have to guess variable names or semantics.

## Source and API

Taika exposes a public, unauthenticated REST-XQ API backed by an XML-native database. Endpoints used by the fetcher:

| Purpose | Endpoint |
|---|---|
| List all datasets | `GET /restxq/taika/fi/datasets` |
| One dataset's full metadata | `GET /restxq/taika/fi/datasets/{identifier}` |
| All variables for a dataset | `GET /restxq/taika/fi/variables/{identifier}` |

All responses are content-negotiated JSON (`Accept: application/json`). **Finnish (`fi`) is used because the English endpoint lists only ~84 datasets while Finnish lists all 312** — the English translation is incomplete and English is not the canonical metadata language at Statistics Finland.

## Layout

```
Finnish-Registry-Metadata/
├── CLAUDE.md                # This file
├── README.md                # Generated catalogue of all datasets
├── idea.txt                 # Original request that prompted this archive
├── fetch_taika_metadata.py  # Rerunnable fetcher (stdlib only)
├── build_catalogue.py       # Reads raw JSON, writes Markdown READMEs
├── raw/
│   └── datasets.json        # Verbatim /restxq/taika/fi/datasets response
└── datasets/
    └── <stripped_identifier>/
        ├── dataset.json     # Verbatim /restxq/taika/fi/datasets/{id} response
        ├── variables.json   # Verbatim /restxq/taika/fi/variables/{id} response
        └── README.md        # Generated: human-readable summary + variable table
```

Dataset directory names are the Taika `identifier` with the trailing `.xml` stripped (e.g. the identifier `FOLK_19872023_jua_tyosu25_001.xml` lives at `datasets/FOLK_19872023_jua_tyosu25_001/`).

## How to answer questions about a register variable

1. **Grep across the variables files** when you know a variable code or family: `grep -l "kturaha" datasets/*/variables.json` — returns all datasets that expose `kturaha`.
2. **Open the dataset's README** — `datasets/<identifier>/README.md` has a variable table plus a per-variable definition section (`conceptdef`) in Finnish.
3. **Fall back to the raw JSON** when the Markdown is insufficient or you need fields the generator omits: `datasets/<identifier>/variables.json`.
4. **Cross-reference the top-level catalogue** (`README.md`) for temporal coverage, population, and source documentation when deciding whether a dataset is appropriate for a given analysis.

## Refreshing the archive

```
python fetch_taika_metadata.py && python build_catalogue.py
```

The fetcher is idempotent (atomic writes, overwrite existing files). The builder is deterministic (sorted output) so re-running produces clean `git diff` output when Taika publishes new datasets or updates existing metadata.

Both scripts are stdlib-only and run on the repository's existing Python install (`C:/ProgramData/anaconda3/python.exe`). A full refresh fetches the catalogue plus two endpoints per dataset with a 0.2 s pause between calls — roughly 2–3 minutes for all 312 datasets.

## Do not hand-edit

The `raw/` and `datasets/` trees are generated from the Taika API. Any manual change will be silently overwritten on the next refresh. Only the two Python scripts, this `CLAUDE.md`, and `.gitignore` are hand-maintained.

## Known quirks of the upstream data

- **`statmeta` is usually a placeholder** — most datasets return the literal string `"metaa..."` instead of structured statistical metadata. Preserved as-is.
- **`everything_else` is always `"asdf"`** — a Taika placeholder / leftover development field. The builder does not render it.
- **Eight SURVEY datasets list a placeholder "no variables" sentinel** (`emptyvariablenameforcossicreatedbycsmetaedit`) instead of a real variable list. The builder filters these out and renders an explanatory note instead.
- **Some fields are `null`** on some datasets (notably `line_count`, `keywords`, `measunit`, `classification`, `variablegroups`). The builder renders these as `—`.
- **HTML fragments in descriptions**: `contentdescription` and `resourcerelation_*` may contain inline HTML (`<a href=…>`, `<b>`). The builder leaves them intact — Markdown renderers generally pass inline HTML through.

## Sibling projects that consult this archive

The following research projects have a `## Finnish Register Metadata` stanza in their `CLAUDE.md` pointing here:

- `C:/Users/vihriae2/ResearchGit/Student-Debt-Project`
- `C:/Users/vihriae2/ResearchGit/Inheritance-Project`

When adding a new project that uses Statistics Finland register data, add the same stanza to its `CLAUDE.md`. Projects under `C:/Users/vihriae2/ResearchGit/Completed/` are frozen replication packages and must not be modified.
