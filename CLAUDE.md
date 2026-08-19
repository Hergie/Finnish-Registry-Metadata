# CLAUDE.md

This repository is a local mirror of the **Taika** research-data catalogue operated by Statistics Finland (Tilastokeskus), available at <https://taika.stat.fi/>. Taika documents every unit-level research dataset that Statistics Finland makes available to permit-holding researchers through the FIONA remote-access environment. The purpose of this archive is to give Claude Code (or any LLM coding assistant) working on research code that reads Finnish administrative registers authoritative, offline access to variable definitions, dataset coverage, population descriptions, and data-source documentation — so code using these registers doesn't have to guess variable names or semantics.

## Source and API

Taika exposes a public, unauthenticated REST-XQ API backed by an XML-native database. Endpoints used by the fetcher:

| Purpose | Endpoint |
|---|---|
| List all datasets | `GET /restxq/taika/fi/datasets` |
| One dataset's full metadata | `GET /restxq/taika/fi/datasets/{identifier}` |
| All variables for a dataset | `GET /restxq/taika/fi/variables/{identifier}` |

All responses are content-negotiated JSON (`Accept: application/json`). **Finnish (`fi`) is used because the English endpoint lists only about a third of the datasets** — the English translation is incomplete and English is not the canonical metadata language at Statistics Finland. Do not swap to `en` to avoid Finnish text or mojibake; the Finnish endpoint is the authoritative source.

## Layout

```
Finnish-Registry-Metadata/
├── CLAUDE.md                # This file
├── README.md                # Generated catalogue of all datasets
├── idea.txt                 # Original request that prompted this archive
├── fetch_taika_metadata.py  # Rerunnable fetcher (stdlib only)
├── build_catalogue.py       # Reads raw JSON, writes Markdown READMEs
├── .github/workflows/
│   └── refresh-catalogue.yml # Weekly cloud refresh; commits only on real change
├── .claude/
│   ├── settings.json        # Registers the SessionStart hook
│   └── hooks/
│       └── check-upstream.sh # Reports this checkout's standing vs origin/main
├── raw/
│   └── datasets.json        # Verbatim /restxq/taika/fi/datasets response
├── datasets/                # Everything Taika lists TODAY
│   └── <stripped_identifier>/
│       ├── dataset.json     # Verbatim /restxq/taika/fi/datasets/{id} response
│       ├── variables.json   # Verbatim /restxq/taika/fi/variables/{id} response
│       └── README.md        # Generated: human-readable summary + variable table
└── withdrawn/               # Datasets Taika USED TO list — superseded vintages
    ├── README.md            # Generated index of withdrawn datasets
    └── <stripped_identifier>/
        ├── dataset.json     # Preserved verbatim from the last fetch that saw it
        ├── variables.json   # Preserved verbatim
        ├── withdrawn.json   # { identifier, withdrawn_on }
        └── README.md        # Generated, with a withdrawal banner
```

Dataset directory names are the Taika `identifier` with the trailing `.xml` stripped (e.g. the identifier `FOLK_19872023_jua_tyosu25_001.xml` lives at `datasets/FOLK_19872023_jua_tyosu25_001/`).

The `datasets/` vs `withdrawn/` split is the point: `datasets/` mirrors Taika exactly, `withdrawn/` is everything it has retired. A grep across `datasets/*/variables.json` answers "what can I request today"; a grep that also covers `withdrawn/` answers "what documents the data already sitting in my FIONA project".

## How to answer questions about a register variable

1. **Grep across the variables files** when you know a variable code or family: `grep -l "kturaha" datasets/*/variables.json` — returns all datasets that expose `kturaha`.
2. **Open the dataset's README** — `datasets/<identifier>/README.md` has a variable table plus a per-variable definition section (`conceptdef`) in Finnish.
3. **Fall back to the raw JSON** when the Markdown is insufficient or you need fields the generator omits: `datasets/<identifier>/variables.json`.
4. **Cross-reference the top-level catalogue** (`README.md`) for temporal coverage, population, and source documentation when deciding whether a dataset is appropriate for a given analysis.
5. **Check the vintage before you quote the definition** — see below. This step is not optional.

## Data vintage: this archive tracks Taika, not the user's data

**This mirror documents what Statistics Finland offers *today*. A FIONA research project runs against a delivery frozen when its permit was granted.** These drift apart, and the drift is silent.

Most registers are reissued annually under a new identifier: `FOLK_19872023_jua_perus24_001` and `FOLK_19872025_jua_perus26_001` are the same register two vintages apart. Across vintages, variables are added, dropped, renamed, and occasionally redefined — the documented `shnro` → `hid_e` rename is exactly this. Quoting a definition from the wrong vintage produces code that *runs* and is *wrong*, which is worse than code that fails.

Therefore, when answering any variable question:

- **Establish which vintage the user actually has.** If it is not already known from the conversation, ask, or ask them to list their data directory. Do not assume the newest vintage is theirs — long-running projects usually have an older one.
- **Match the identifier's version suffix and year span** (`perus24` vs `perus26`; `FOLK_19872023_` vs `FOLK_19872025_`) against their actual file names.
- **If their vintage is no longer current, read it from `withdrawn/`**, which exists for precisely this case. `grep -l "kturaha" withdrawn/*/variables.json` works the same way.
- **State the vintage alongside the answer** — "in `perus26`, `kturaha` is …" — so a mismatch is visible to the user rather than buried.
- **The data file is the final authority.** If metadata and actual columns disagree, the file wins.

## Refreshing the archive

```
python fetch_taika_metadata.py && python build_catalogue.py
```

The fetcher is idempotent (atomic writes, overwrite existing files). The builder is deterministic (sorted output) so re-running produces clean `git diff` output when Taika publishes new datasets or updates existing metadata.

Both scripts are stdlib-only and run on the repository's existing Python install (`C:/ProgramData/anaconda3/python.exe` — plain `python` is *not* on PATH on this machine). A full refresh fetches the catalogue plus two endpoints per dataset with a 0.2 s pause between calls, plus up to two retries on 5xx/timeout — roughly 5 minutes for the full catalogue.

**Withdrawals.** Datasets that vanish from the catalogue are *moved to* `withdrawn/<id>/`, never deleted, and stamped with a `withdrawn.json` marker. If an identifier later reappears, the stale `withdrawn/` copy is dropped in favour of the fresh one. A safety valve refuses to withdraw more than 20 % of the catalogue in a single run and exits non-zero — a truncated API response must not be able to gut the mirror.

Fetcher exit codes: `0` ok · `1` catalogue unreachable · `2` some per-dataset fetches failed · `3` safety valve tripped.

## Automated refresh

`.github/workflows/refresh-catalogue.yml` runs the same two scripts on GitHub's runners every **Monday 05:00 UTC**, and can be triggered by hand from the Actions tab or with `gh workflow run refresh-catalogue.yml`. It pushes to `main` with the default `GITHUB_TOKEN` (`permissions: contents: write`); no secrets are configured.

It **commits only when `raw/`, `datasets/`, or `withdrawn/` actually changed.** The top-level `README.md` stamps a date and so would otherwise churn on every run; when nothing else moved, that change is discarded. This is why the README says "last upstream change" rather than "refreshed" — an old date means Taika has been stable. The Actions run history is the record of when checks happened.

*Caveat:* GitHub disables scheduled workflows after 60 days with no repository activity and emails the owner. Re-enabling is one click on the Actions tab.

Locally, a `SessionStart` hook (`.claude/hooks/check-upstream.sh`, registered in `.claude/settings.json`) fetches `origin/main` and reports where this checkout stands — because the cloud job moves the remote with nothing happening locally. It prints on *every* session start, including when nothing is wrong: `up to date`, a behind/diverged warning, or `could not reach origin` when the fetch fails or times out. **If it reports behind or diverged, `git pull --ff-only` before grepping `datasets/` or `withdrawn/`; if it could not reach origin, treat the mirror's freshness as unknown rather than current.** Silence means the hook did not run at all. The hook only reports; it never modifies the working tree and always exits 0.

## Do not hand-edit

The `raw/`, `datasets/`, and `withdrawn/` trees are generated from the Taika API. Any manual change will be silently overwritten on the next refresh. Only the two Python scripts, the workflow, the hook, this `CLAUDE.md`, and `.gitignore` are hand-maintained.

## Known quirks of the upstream data

- **`statmeta` is usually a placeholder** — most datasets return the literal string `"metaa..."` instead of structured statistical metadata. Preserved as-is.
- **`everything_else` is always `"asdf"`** — a Taika placeholder / leftover development field. The builder does not render it.
- **Some SURVEY datasets list a placeholder "no variables" sentinel** (`emptyvariablenameforcossicreatedbycsmetaedit`) instead of a real variable list. The builder filters these out, renders an explanatory note, and reports the current count in the top-level README — it grows as Taika adds surveys, so do not trust a remembered number. Count them with `grep -l emptyvariablenameforcossicreatedbycsmetaedit datasets/*/variables.json | wc -l`.
- **Some fields are `null`** on some datasets (notably `line_count`, `keywords`, `measunit`, `classification`, `variablegroups`). The builder renders these as `—`.
- **HTML fragments in descriptions**: `contentdescription` and `resourcerelation_*` may contain inline HTML (`<a href=…>`, `<b>`). The builder leaves them intact — Markdown renderers generally pass inline HTML through.