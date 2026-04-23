# Finnish Registry Metadata

Paikallinen peilaus Tilastokeskuksen **Taika**-tutkimusaineistokatalogista ([taika.stat.fi](https://taika.stat.fi/)). 312 aineistoa, päivitetty 2026-04-13.

Local mirror of Statistics Finland's **Taika** research-data catalogue (312 datasets, refreshed 2026-04-13).

## Käyttö / Usage

Claude-agenttien tulee konsultoida tätä arkistoa kirjoittaessaan koodia, joka lukee Tilastokeskuksen rekisteriaineistoja (FOLK, EDUC, SES, FLEED, YA221, kuolemansyyt, perintöverot jne.). Muuttujatiedot löytyvät kunkin aineiston `datasets/<tunnus>/README.md`-tiedostosta tai raakana `variables.json`-tiedostosta.

## Päivitys / Refresh

```
python fetch_taika_metadata.py && python build_catalogue.py
```

Älä muokkaa `raw/`- tai `datasets/`-hakemistoja käsin — ne generoidaan. Do not hand-edit `raw/` or `datasets/` — both trees are regenerated.

## Luettelo / Catalogue

| Tunnus / Identifier | Aihe / Subject | Kattavuus / Coverage | #Var | #Obs | |
|---|---|---|---|---|---|
| `EDUC_19751995_jua_000_000.xml` | EDUC_OPISK_HIST: Korkeakouluopiskelijoiden historialliset tiedot 1975-1995 2. osamoduuli | 1970-01-01 - 1995-12-31 | 33 | — | [→](./datasets/EDUC_19751995_jua_000_000/README.md) |
| `EDUC_1985_jua_tyhr19_001.xml` | EDUC_TYHR Toisen asteen yhteishaku -moduuli, osa 1, 1985 | — | 105 | — | [→](./datasets/EDUC_1985_jua_tyhr19_001/README.md) |
| `EDUC_19891995_jua_tyhr19_001.xml` | EDUC_TYHR Toisen asteen yhteishaku -moduuli, osa 2, 1989, 1991-1995 | — | 104 | — | [→](./datasets/EDUC_19891995_jua_tyhr19_001/README.md) |
| `EDUC_19902025_jua_ytl_001.xml` | EDUC_YTL  ylioppilaskirjoitusten tulokset 1967-2025 | 1967-01-01 - 2025-12-31 | 18 | — | [→](./datasets/EDUC_19902025_jua_ytl_001/README.md) |
| `EDUC_19921998_jua_harekyo_001.xml` | EDUC_HAREK Yliopistojen hakurekisteritiedot 1992-1998 | 1992-01-01 - 1998-12-31 | 13 | — | [→](./datasets/EDUC_19921998_jua_harekyo_001/README.md) |
| `EDUC_1995_jua_opisk_001.xml` | EDUC_OPISK Opiskelijat 1995 | 1995-01-01 - 1995-12-31 | 50 | — | [→](./datasets/EDUC_1995_jua_opisk_001/README.md) |
| `EDUC_19961997_jua_tyhr19_001.xml` | EDUC_TYHR Toisen asteen yhteishaku -moduuli, osa 3, 1996-1997 | — | 199 | — | [→](./datasets/EDUC_19961997_jua_tyhr19_001/README.md) |
| `EDUC_19961999_jua_harekamk_001.xml` | EDUC_HAREK Ammattikorkeakoulujen hakurekisteritiedot 1996-1999 | 1996-01-01 - 1999-12-31 | 255 | — | [→](./datasets/EDUC_19961999_jua_harekamk_001/README.md) |
| `EDUC_1996_jua_opisk_001.xml` | EDUC_OPISK Opiskelijat 1996 | 1996-01-01 - 1996-12-31 | 29 | — | [→](./datasets/EDUC_1996_jua_opisk_001/README.md) |
| `EDUC_1997_jua_opisk_001.xml` | EDUC_OPISK Opiskelijat 1997 | 1997-01-01 - 1997-12-31 | 55 | — | [→](./datasets/EDUC_1997_jua_opisk_001/README.md) |
| `EDUC_19982007_jua_tyhr19_001.xml` | EDUC_TYHR Toisen asteen yhteishaku -moduuli, osa 4, 1998-2007 | — | 201 | — | [→](./datasets/EDUC_19982007_jua_tyhr19_001/README.md) |
| `EDUC_1998_jua_opisk_001.xml` | EDUC_OPISK Opiskelijat 1998 | 1998-01-01 - 1998-12-31 | 50 | — | [→](./datasets/EDUC_1998_jua_opisk_001/README.md) |
| `EDUC_19992003_jua_harekyo_001.xml` | EDUC_HAREK Yliopistojen hakurekisteritiedot 1999-2003 | 1999-01-01 - 2003-12-31 | 28 | — | [→](./datasets/EDUC_19992003_jua_harekyo_001/README.md) |
| `EDUC_19992024_jua_opisk_001.xml` | EDUC_OPISK Opiskelijat 1999 - 2024 | 1999-01-01 - 2024-12-31 | 86 | — | [→](./datasets/EDUC_19992024_jua_opisk_001/README.md) |
| `EDUC_20002004_jua_harekamk_001.xml` | EDUC_HAREK Ammattikorkeakoulujen hakurekisteritiedot 2000-2004 | 2000-01-01 - 2004-12-31 | 200 | — | [→](./datasets/EDUC_20002004_jua_harekamk_001/README.md) |
| `EDUC_20042009_jua_harekyo_001.xml` | EDUC_HAREK Yliopistojen hakurekisteritiedot 2004-2009 | 2004-01-01 - 2009-12-31 | 69 | — | [→](./datasets/EDUC_20042009_jua_harekyo_001/README.md) |
| `EDUC_20052014_jua_harekamk_001.xml` | EDUC_HAREK Ammattikorkeakoulujen hakurekisteritiedot 2005-2014 | 2005-01-01 - 2014-12-31 | 351 | — | [→](./datasets/EDUC_20052014_jua_harekamk_001/README.md) |
| `EDUC_20052024_jua_trek_001.xml` | EDUC_TREK Tutkintorekisteri 2005–2024 | 2005-01-01 - 2024-12-31 | 23 | — | [→](./datasets/EDUC_20052024_jua_trek_001/README.md) |
| `EDUC_20082013_jua_tyhr19_001.xml` | EDUC_TYHR Toisen asteen yhteishaku -moduuli, osa 5, 2008-2013 | — | 142 | — | [→](./datasets/EDUC_20082013_jua_tyhr19_001/README.md) |
| `EDUC_20102014_jua_harekyo_001.xml` | EDUC_HAREK Yliopistojen hakurekisteritiedot 2010-2014 | 2010-01-01 - 2014-12-01 | 82 | — | [→](./datasets/EDUC_20102014_jua_harekyo_001/README.md) |
| `EDUC_20142020_jua_tyhr20_001.xml` | Toisen asteen yhteishaku - moduuli, osa 6 (2014 - 2020) | — | 111 | — | [→](./datasets/EDUC_20142020_jua_tyhr20_001/README.md) |
| `EDUC_20142023_jua_tyhr24_001.xml` | EDUC TYHR Toisen asteen yhteishaku - moduuli, osa 6, 2014 - 2024 | 2014-01-01 - 2024-12-31 | 132 | — | [→](./datasets/EDUC_20142023_jua_tyhr24_001/README.md) |
| `EDUC_20152023_jua_harek_001.xml` | EDUC_HAREK Korkeakoulujen hakurekisteritiedot, 2015-2023 | 2015-01-01 - 2023-12-31 | 115 | — | [→](./datasets/EDUC_20152023_jua_harek_001/README.md) |
| `EDUC_20182025_jua_koskijakso_001.xml` | EDUC_KOSKI - Opiskeluoikeus_jakso | — | 11 | — | [→](./datasets/EDUC_20182025_jua_koskijakso_001/README.md) |
| `EDUC_20182025_jua_koskiopiskeluoikeus_001.xml` | EDUC_KOSKI -Opiskeluoikeus | — | 25 | — | [→](./datasets/EDUC_20182025_jua_koskiopiskeluoikeus_001/README.md) |
| `EDUC_20182025_jua_koskiperus_001.xml` | EDUC_KOSKI - Perusopetus | — | 21 | — | [→](./datasets/EDUC_20182025_jua_koskiperus_001/README.md) |
| `EDUC_20182025_jua_koskitoinenammatillinensuoritukset_001.xml` | EDUC_KOSKI TOINEN ASTE - ammatillinen_suoritukset | — | 28 | — | [→](./datasets/EDUC_20182025_jua_koskitoinenammatillinensuoritukset_001/README.md) |
| `EDUC_20182025_jua_koskitoinenammatillinentutkinnonosat_001.xml` | EDUC_KOSKI TOINEN ASTE - ammatillinen_tutkinnonosat | — | 28 | — | [→](./datasets/EDUC_20182025_jua_koskitoinenammatillinentutkinnonosat_001/README.md) |
| `EDUC_20182025_jua_koskitoinenlukioib_001.xml` | EDUC_KOSKI TOINEN ASTE - Lukio_IB | — | 30 | — | [→](./datasets/EDUC_20182025_jua_koskitoinenlukioib_001/README.md) |
| `EDUC_20182025_jua_koskitoinennivel_001.xml` | EDUC_KOSKI TOINEN ASTE -  Nivelvaihe | — | 26 | — | [→](./datasets/EDUC_20182025_jua_koskitoinennivel_001/README.md) |
| `EDUC_20182025_jua_koskitoinenosaamisenhankkimistapa_001.xml` | EDUC_KOSKI TOINEN ASTE -  Osaamisen hankkimistapa | — | 11 | — | [→](./datasets/EDUC_20182025_jua_koskitoinenosaamisenhankkimistapa_001/README.md) |
| `EDUC_20202024_jua_esiperus_001.xml` | EDUC_ESIPERUS Oppilaat 2020 - 2024 | 2020-01-01 - 2024-12-31 | 25 | — | [→](./datasets/EDUC_20202024_jua_esiperus_001/README.md) |
| `EDUC_2024_jua_VIRTA_001.xml` | EDUC_VIRTA-aineisto | - 2024-12-31 | 61 | — | [→](./datasets/EDUC_2024_jua_VIRTA_001/README.md) |
| `FIRMRDINNO_2018_jua_innovaatio_001.xml` | FIRM_RDINNO Innovaatiotutkimus 2018 (YA231) | 2016-01-01 - 2018-12-31 | 285 | 2,267 | [→](./datasets/FIRMRDINNO_2018_jua_innovaatio_001/README.md) |
| `FIRMRDINNO_2020_jua_innovaatio_001.xml` | FIRM_RDINNO Innovaatiotutkimus 2020 | 2018-01-01 - 2020-12-31 | 326 | 2,267 | [→](./datasets/FIRMRDINNO_2020_jua_innovaatio_001/README.md) |
| `FIRMRDINNO_2022_jua_innovaatio_001.xml` | FIRM_RDINNO Innovaatiotutkimus 2022 | 2020-01-01 - 2022-12-31 | 358 | 2,267 | [→](./datasets/FIRMRDINNO_2022_jua_innovaatio_001/README.md) |
| `FIRM_1985062021_jua_BANKRkonkurssit_001.xml` | FIRM_BANKR Konkurssit (YA262) | 1985-01-01 - 2021-06-30 | 45 | — | [→](./datasets/FIRM_1985062021_jua_BANKRkonkurssit_001/README.md) |
| `FIRM_1985072022_jua_BANKRkonkurssit_001.xml` | FIRM_BANKR Konkurssit | 1985-01-01 - 2024-06-30 | 45 | — | [→](./datasets/FIRM_1985072022_jua_BANKRkonkurssit_001/README.md) |
| `FIRM_1985_jua_rd_001.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen 1985 (YA231) | 1985-01-01 - 1985-12-31 | 147 | 962 | [→](./datasets/FIRM_1985_jua_rd_001/README.md) |
| `FIRM_19862021_jua_FSSpaneeli_001.xml` | FIRM_FSS Tilinpäätöspaneeli 1986-2024 | 1986-01-01 - 2024-12-31 | 85 | — | [→](./datasets/FIRM_19862021_jua_FSSpaneeli_001/README.md) |
| `FIRM_1987_jua_rd_001.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen 1987 (YA231) | 1987-01-01 - 1987-12-31 | 175 | 1,081 | [→](./datasets/FIRM_1987_jua_rd_001/README.md) |
| `FIRM_19882017_jua_empenthenkom_001.xml` | FIRM_EMPENT Yrityskohtaiset henkilöstöominaisuudet (YA241) | 1988-01-01 - 2018-12-31 | 36 | — | [→](./datasets/FIRM_19882017_jua_empenthenkom_001/README.md) |
| `FIRM_19882018_jua_empestjwfl_001.xml` | FIRM_EMPEST Toimipaikkakohtainen työpaikka- ja työntekijävirta-aineisto | 1988-01-01 - 2022-12-31 | 18 | — | [→](./datasets/FIRM_19882018_jua_empestjwfl_001/README.md) |
| `FIRM_19882020_jua_empenthenkom_001.xml` | FIRM_EMPENT Yrityskohtaiset henkilöstöominaisuudet | 1988-01-01 - 2022-12-31 | 36 | — | [→](./datasets/FIRM_19882020_jua_empenthenkom_001/README.md) |
| `FIRM_19882020_jua_empesthenkom_001.xml` | FIRM_EMPEST Toimipaikkakohtaiset henkilöstöominaisuudet | 1988-01-01 - 2022-12-31 | 36 | — | [→](./datasets/FIRM_19882020_jua_empesthenkom_001/README.md) |
| `FIRM_19882021_jua_ENTERyritystol_001.xml` | FIRM_ENTER Yritys-toimiala -aikasarja 1988-2024 | 1988-01-01 - 2024-12-31 | 16 | — | [→](./datasets/FIRM_19882021_jua_ENTERyritystol_001/README.md) |
| `FIRM_1989_jua_rd_001.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen 1989 (YA231) | 1989-01-01 - 1989-12-31 | 172 | 1,190 | [→](./datasets/FIRM_1989_jua_rd_001/README.md) |
| `FIRM_1991_jua_rd_001.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen 1991 (YA231) | 1991-01-01 - 1991-12-31 | 178 | 911 | [→](./datasets/FIRM_1991_jua_rd_001/README.md) |
| `FIRM_1992_jua_rd_001.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen 1992 (YA231) | 1992-01-01 - 1992-12-31 | 14 | 394 | [→](./datasets/FIRM_1992_jua_rd_001/README.md) |
| `FIRM_1993062021_jua_BANKRsaneeraukset_001.xml` | FIRM_BANKR Yrityssaneeraukset (YA262) | 1993-01-01 - 2021-06-30 | 41 | — | [→](./datasets/FIRM_1993062021_jua_BANKRsaneeraukset_001/README.md) |
| `FIRM_1993062022_jua_BANKRsaneeraukset_001.xml` | FIRM_BANKR Yrityssaneeraukset | 1993-01-01 - 2024-06-30 | 42 | — | [→](./datasets/FIRM_1993062022_jua_BANKRsaneeraukset_001/README.md) |
| `FIRM_1993_jua_rd_001.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen 1993 (YA231) | 1993-01-01 - 1993-12-31 | 182 | 763 | [→](./datasets/FIRM_1993_jua_rd_001/README.md) |
| `FIRM_1994_jua_rd_001.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen 1994 (YA231) | 1994-01-01 - 1994-12-31 | 80 | 558 | [→](./datasets/FIRM_1994_jua_rd_001/README.md) |
| `FIRM_19952021_jua_IFATS_001.xml` | FIRM_IFATS Ulkomainen omistajuus | 1995-01-01 - 2024-12-31 | 18 | — | [→](./datasets/FIRM_19952021_jua_IFATS_001/README.md) |
| `FIRM_1995_jua_rd_001.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen 1995 (YA231) | 1995-01-01 - 1995-12-31 | 213 | 1,722 | [→](./datasets/FIRM_1995_jua_rd_001/README.md) |
| `FIRM_1996_jua_rd_001.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen 1996 (YA231) | 1996-01-01 - 1996-12-31 | 13 | 2,028 | [→](./datasets/FIRM_1996_jua_rd_001/README.md) |
| `FIRM_19972018_jua_cpi_001.xml` | FIRM_CPI Kuluttajahintaindeksin yksikkötason aineisto vuosilta 1997-2018 (YA272) | 1997-01-01 - 2018-12-31 | 39 | — | [→](./datasets/FIRM_19972018_jua_cpi_001/README.md) |
| `FIRM_1997_jua_rd_001.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen 1997 (YA231) | 1997-01-01 - 1997-12-31 | 193 | 1,672 | [→](./datasets/FIRM_1997_jua_rd_001/README.md) |
| `FIRM_1998_jua_rd_001.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen 1998 (YA231) | 1998-01-01 - 1998-12-31 | 158 | 3,038 | [→](./datasets/FIRM_1998_jua_rd_001/README.md) |
| `FIRM_1999_jua_rd_001.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen 1999 (YA231) | 1999-01-01 - 1999-12-31 | 291 | 3,450 | [→](./datasets/FIRM_1999_jua_rd_001/README.md) |
| `FIRM_2000_jua_rd_001.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen 2000 (YA231) | 2000-01-01 - 2000-12-31 | 284 | 3,590 | [→](./datasets/FIRM_2000_jua_rd_001/README.md) |
| `FIRM_20012006_jua_gvc_001.xml` | FIRM_GVC Toimintojen ulkoistaminen ja siirtäminen ulkomaille -kyselyn aineisto 2001–2006 (International Sourcing -hanke) (ya228) | 2001-01-01 - 2006-12-31 | 279 | 1,653 | [→](./datasets/FIRM_20012006_jua_gvc_001/README.md) |
| `FIRM_2001_jua_rd_001.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen 2001 (YA231) | 2001-01-01 - 2001-12-31 | 285 | 3,847 | [→](./datasets/FIRM_2001_jua_rd_001/README.md) |
| `FIRM_20022021_jua_demog_001.xml` | Yritysten demografiatiedot | 2002-01-01 - 2021-12-31 | 13 | — | [→](./datasets/FIRM_20022021_jua_demog_001/README.md) |
| `FIRM_2003_jua_rd_001.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen 2003 (YA231) | 2003-01-01 - 2004-12-31 | 279 | 4,139 | [→](./datasets/FIRM_2003_jua_rd_001/README.md) |
| `FIRM_2004_jua_rd_001.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen 2004 (YA231) | 2004-01-01 - 2004-12-31 | 291 | 3,737 | [→](./datasets/FIRM_2004_jua_rd_001/README.md) |
| `FIRM_2005_jua_rd_001.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen 2005 (YA231) | 2005-01-01 - 2005-12-31 | 291 | 3,908 | [→](./datasets/FIRM_2005_jua_rd_001/README.md) |
| `FIRM_2006_jua_rd_001.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen 2006 (YA231) | 2006-01-01 - 2006-12-31 | 290 | 3,817 | [→](./datasets/FIRM_2006_jua_rd_001/README.md) |
| `FIRM_2007_jua_rd_001.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen 2007 (YA231) | 2007-01-01 - 2007-12-31 | 292 | 4,301 | [→](./datasets/FIRM_2007_jua_rd_001/README.md) |
| `FIRM_20082020_jua_GROUP_001.xml` | FIRM_GROUP Konsernit | 1995-01-01 - 2024-12-31 | 23 | — | [→](./datasets/FIRM_20082020_jua_GROUP_001/README.md) |
| `FIRM_2008_jua_rd_001.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen 2008 (YA231) | 2008-01-01 - 2008-12-31 | 235 | 4,180 | [→](./datasets/FIRM_2008_jua_rd_001/README.md) |
| `FIRM_2009_jua_rd_001.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen 2009 (YA231) | 2009-01-01 - 2009-12-31 | 235 | 4,332 | [→](./datasets/FIRM_2009_jua_rd_001/README.md) |
| `FIRM_2010_jua_rd_001.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen 2010 (YA231) | 2010-01-01 - 2010-12-31 | 311 | 4,531 | [→](./datasets/FIRM_2010_jua_rd_001/README.md) |
| `FIRM_2011_jua_rd_001.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen 2011 (YA231) | 2011-01-01 - 2011-12-31 | 321 | 4,532 | [→](./datasets/FIRM_2011_jua_rd_001/README.md) |
| `FIRM_2012_jua_rd_001.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen 2012 (YA231) | 2012-01-01 - 2012-12-31 | 317 | 4,684 | [→](./datasets/FIRM_2012_jua_rd_001/README.md) |
| `FIRM_20132019_jua_COMMODraakaaineet_002.xml` | FIRM_COMMOD Hyödykkeet: aineet ja tarvikkeet 2013, 2015, 2017, 2019, 2021, 2023 | 2013-01-01 - 2023-12-31 | 11 | — | [→](./datasets/FIRM_20132019_jua_COMMODraakaaineet_002/README.md) |
| `FIRM_20132020_jua_COMMODtuotteet_001.xml` | FIRM_COMMOD Hyödykkeet: tuotteet 2013 - 2023 | 2013-01-01 - 2023-12-31 | 16 | — | [→](./datasets/FIRM_20132020_jua_COMMODtuotteet_001/README.md) |
| `FIRM_20132020_jua_FSS_001.xml` | FIRM_FSS Tilinpäätösaineisto 2013 -2020 (YA211) | 2013-01-01 - 2020-12-31 | 303 | — | [→](./datasets/FIRM_20132020_jua_FSS_001/README.md) |
| `FIRM_20132021_jua_FSS_001.xml` | FIRM_FSS Tilinpäätösaineisto 2021-2024 | 2021-01-01 - 2024-12-31 | 307 | — | [→](./datasets/FIRM_20132021_jua_FSS_001/README.md) |
| `FIRM_2013_jua_rd_001.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen 2013 (YA231) | 2013-01-01 - 2013-12-31 | 321 | 4,744 | [→](./datasets/FIRM_2013_jua_rd_001/README.md) |
| `FIRM_20142019_jua_ENVPROT_001.xml` | FIRM_ENVPROT Teollisuuden ympäristönsuojelumenot 2014-2019 | 2014-01-01 - 2019-12-31 | 36 | — | [→](./datasets/FIRM_20142019_jua_ENVPROT_001/README.md) |
| `FIRM_2014_jua_rd_001.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen 2014 (YA231) | 2014-01-01 - 2014-12-31 | 318 | 4,406 | [→](./datasets/FIRM_2014_jua_rd_001/README.md) |
| `FIRM_20152017_jua_gvc_001.xml` | FIRM_GVC Global Value Chains 2015-2017 (YA228) | 2015-01-01 - 2017-12-31 | 404 | 1,653 | [→](./datasets/FIRM_20152017_jua_gvc_001/README.md) |
| `FIRM_2015_jua_rd_001.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen 2015 (YA231) | 2015-01-01 - 2015-12-31 | 325 | 4,586 | [→](./datasets/FIRM_2015_jua_rd_001/README.md) |
| `FIRM_2016_jua_rd_001.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen 2016 (YA231) | 2016-01-01 - 2016-12-31 | 322 | 4,447 | [→](./datasets/FIRM_2016_jua_rd_001/README.md) |
| `FIRM_2017_jua_rd_001.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen 2017 (YA231) | 2017-01-01 - 2017-12-31 | 323 | 4,348 | [→](./datasets/FIRM_2017_jua_rd_001/README.md) |
| `FIRM_20182020_jua_gvc_000.xml` | FIRM_GVC Globaalit arvoketjut ja toimintojen ulkoistaminen -kyselyn aineisto 2018-2020 | 2018-01-01 - 2020-12-31 | 374 | — | [→](./datasets/FIRM_20182020_jua_gvc_000/README.md) |
| `FIRM_2018_jua_ENTER_001.xml` | FIRM_ENTER Yritystietovarasto: yritykset 2018 (YA221) | 2018-01-01 - 2018-12-31 | 41 | 361,026 | [→](./datasets/FIRM_2018_jua_ENTER_001/README.md) |
| `FIRM_2018_jua_ofats_001.xml` | FIRM_OFATS Suomalaiset tytäryhtiöt ulkomailla 2018 (YA225) | 2018-01-01 - 2018-12-31 | 12 | 5,434 | [→](./datasets/FIRM_2018_jua_ofats_001/README.md) |
| `FIRM_2018_jua_rd_001.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen 2018 (YA231) | 2018-01-01 - 2018-12-31 | 321 | 4,002 | [→](./datasets/FIRM_2018_jua_rd_001/README.md) |
| `FIRM_2019_jua_ICT_001.xml` | FIRM_ICT Tietotekniikka ja sähköinen kauppa yrityksissä 2019 (YA233) | 2019-01-01 - 2019-12-31 | 182 | 3,020 | [→](./datasets/FIRM_2019_jua_ICT_001/README.md) |
| `FIRM_2019_jua_ofats_001.xml` | FIRM_OFATS Suomalaiset tytäryhtiöt ulkomailla 2019 (YA225) | 2019-01-01 - 2019-12-31 | 12 | 5,398 | [→](./datasets/FIRM_2019_jua_ofats_001/README.md) |
| `FIRM_2019_jua_rd_001.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen 2019 (YA231) | 2019-01-01 - 2019-12-31 | 316 | 3,746 | [→](./datasets/FIRM_2019_jua_rd_001/README.md) |
| `FIRM_2020_jua_ICT_001.xml` | FIRM_ICT Tietotekniikka ja sähköinen kauppa yrityksissä 2020 (YA233) | 2020-01-01 - 2020-12-31 | 176 | — | [→](./datasets/FIRM_2020_jua_ICT_001/README.md) |
| `FIRM_2020_jua_RDINNO_001.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen vuonna 2020 (YA231) | 2020-01-01 - 2020-12-31 | 323 | — | [→](./datasets/FIRM_2020_jua_RDINNO_001/README.md) |
| `FIRM_2020_jua_ofats_001.xml` | FIRM_OFATS Suomalaiset tytäryhtiöt ulkomailla 2020 | 2020-01-01 - 2020-12-31 | 12 | 5,398 | [→](./datasets/FIRM_2020_jua_ofats_001/README.md) |
| `FIRM_20212023_jua_gvc_000.xml` | FIRM_GVC Globaalit arvoketjut ja toimintojen ulkoistaminen -kyselyn aineisto 2021-2023 | 2021-01-01 - 2023-12-31 | 324 | 2,047 | [→](./datasets/FIRM_20212023_jua_gvc_000/README.md) |
| `FIRM_2021_jua_ENTER_001.xml` | FIRM_ENTER Yritystietovarasto: yritykset 2021 | 2020-01-01 - 2021-12-31 | 41 | 370,252 | [→](./datasets/FIRM_2021_jua_ENTER_001/README.md) |
| `FIRM_2021_jua_ESTAB_001.xml` | FIRM_ESTAB Yritystietovarasto: toimipaikat 2021 | 2021-01-01 - 2021-12-31 | 28 | 410,542 | [→](./datasets/FIRM_2021_jua_ESTAB_001/README.md) |
| `FIRM_2021_jua_ICT_001.xml` | FIRM_ICT Tietotekniikka ja sähköinen kauppa yrityksissä 2021 (YA233) | 2021-01-01 - 2021-12-31 | 178 | — | [→](./datasets/FIRM_2021_jua_ICT_001/README.md) |
| `FIRM_2021_jua_RDINNO_rd.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen vuonna 2021 | 2021-01-01 - 2021-12-31 | 323 | 4,697 | [→](./datasets/FIRM_2021_jua_RDINNO_rd/README.md) |
| `FIRM_2021_jua_SUBSID_001.xml` | FIRM_SUBSID Yritystukitietokanta 2021 | 2021-01-01 - 2021-12-31 | 60 | — | [→](./datasets/FIRM_2021_jua_SUBSID_001/README.md) |
| `FIRM_2021_jua_ofats_001.xml` | FIRM_OFATS Suomalaiset tytäryhtiöt ulkomailla 2021 | 2021-01-01 - 2021-12-31 | 12 | 5,398 | [→](./datasets/FIRM_2021_jua_ofats_001/README.md) |
| `FIRM_2022_jua_ENTER_001.xml` | FIRM_ENTER Yritystietovarasto: yritykset 2022 | 2022-01-01 - 2022-12-31 | 40 | 576,152 | [→](./datasets/FIRM_2022_jua_ENTER_001/README.md) |
| `FIRM_2022_jua_ESTAB_001.xml` | FIRM_ESTAB Yritystietovarasto: toimipaikat 2022 | 2022-01-01 - 2022-12-31 | 28 | 399,828 | [→](./datasets/FIRM_2022_jua_ESTAB_001/README.md) |
| `FIRM_2022_jua_ICT_001.xml` | FIRM_ICT Tietotekniikka ja sähköinen kauppa yrityksissä 2022 (YA233) | 2022-01-01 - 2022-12-31 | 150 | — | [→](./datasets/FIRM_2022_jua_ICT_001/README.md) |
| `FIRM_2022_jua_RDINNO_rd.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen vuonna 2022 | 2022-01-01 - 2022-12-31 | 324 | — | [→](./datasets/FIRM_2022_jua_RDINNO_rd/README.md) |
| `FIRM_2022_jua_SUBSID_001.xml` | FIRM_SUBSID Yritystukitietokanta 2022-2024 | 2009-01-01 - 2024-12-31 | 33 | — | [→](./datasets/FIRM_2022_jua_SUBSID_001/README.md) |
| `FIRM_2022_jua_ofats_001.xml` | FIRM_OFATS Suomalaiset tytäryhtiöt ulkomailla 2022 | 2021-01-01 - 2022-12-31 | 12 | 5,398 | [→](./datasets/FIRM_2022_jua_ofats_001/README.md) |
| `FIRM_2023_jua_ENTER_001.xml` | FIRM_ENTER Yritystietovarasto: yritykset 2023-2024 | 2023-01-01 - 2024-12-31 | 42 | 580,397 | [→](./datasets/FIRM_2023_jua_ENTER_001/README.md) |
| `FIRM_2023_jua_ESTAB_001.xml` | FIRM_ESTAB Yritystietovarasto: toimipaikat 2023-2024 | 2023-01-01 - 2024-12-31 | 28 | 399,828 | [→](./datasets/FIRM_2023_jua_ESTAB_001/README.md) |
| `FIRM_2023_jua_RDINNO_rd.xml` | FIRM_RDINNO Yritysten tutkimus ja kehittäminen vuonna 2023 | 2023-01-01 - 2023-12-31 | 324 | — | [→](./datasets/FIRM_2023_jua_RDINNO_rd/README.md) |
| `FIRM_2023_jua_prod_001.xml` | FIRM_PROD Alueellisen yritystoimintatilaston aineisto | 2013-01-01 - 2024-12-31 | 146 | — | [→](./datasets/FIRM_2023_jua_prod_001/README.md) |
| `FIRM_2023_jua_trade_001.xml` | FIRM_TRADE Tavaroiden ja palveluiden ulkomaankauppa MDL-kannasta 2013 - 2023 | 2013-01-01 - 2023-12-31 | 9 | — | [→](./datasets/FIRM_2023_jua_trade_001/README.md) |
| `FIRM_BASE_jua_legalunits_001.xml` | FIRM_BASE oikeudellisten yksiköiden perustiedot | — | 70 | — | [→](./datasets/FIRM_BASE_jua_legalunits_001/README.md) |
| `FIRM_VAT_jua_2004_002.xml` | FIRM_VAT oma-aloitteiset verot ja työnantajasuoritukset 2004 - | 2004-01-01 - 2023-12-31 | 49 | — | [→](./datasets/FIRM_VAT_jua_2004_002/README.md) |
| `FLOWN_20002021_jua_listed_001.xml` | FLOWN - LISTED pörssilistatut yritykset | 2000-01-01 - 2024-01-01 | 3 | — | [→](./datasets/FLOWN_20002021_jua_listed_001/README.md) |
| `FLOWN_20032021_jua_dividend_001.xml` | FLOWN - DIVIDEND osinkotiedot | 2003-01-01 - 2024-01-01 | 17 | — | [→](./datasets/FLOWN_20032021_jua_dividend_001/README.md) |
| `FLOWN_20062016_jua_firm_002.xml` | FLOWN - FIRM yritys- ja henkilötiedot | 2006-01-01 - 2016-01-01 | 21 | — | [→](./datasets/FLOWN_20062016_jua_firm_002/README.md) |
| `FLOWN_20062022_jua_owner_001.xml` | FLOWN - OWNER osakastiedot | 2006-01-01 - 2024-01-01 | 11 | — | [→](./datasets/FLOWN_20062022_jua_owner_001/README.md) |
| `FLOWN_20072020_jua_partner_001.xml` | FLOWN - PARTNER yhtiömiestiedot | 2007-01-01 - 2024-12-31 | 20 | — | [→](./datasets/FLOWN_20072020_jua_partner_001/README.md) |
| `FOLK_1950_jua_vl50_001.xml` | FOLK Väestölaskenta 1950 | 1950-12-31 - | 73 | — | [→](./datasets/FOLK_1950_jua_vl50_001/README.md) |
| `FOLK_19701985_jua_vl7085_004.xml` | FOLK Väestölaskennat 1970-1985 | 1970-12-31 - 1985-12-31 | 39 | 4,601,576 | [→](./datasets/FOLK_19701985_jua_vl7085_004/README.md) |
| `FOLK_19702022_jua_lapsv24_001.xml` | FOLK lapsi - vanhemmat - vuosi | 1970-01-01 - 2023-12-31 | 15 | — | [→](./datasets/FOLK_19702022_jua_lapsv24_001/README.md) |
| `FOLK_19702023_jua_laps24_001.xml` | FOLK lapsi - vanhemmat | 1970-01-01 - 2024-12-31 | 8 | — | [→](./datasets/FOLK_19702023_jua_laps24_001/README.md) |
| `FOLK_19832022_jua_muutt23_001.xml` | FOLK muutto | 1983-01-01 - 2024-12-31 | 15 | — | [→](./datasets/FOLK_19832022_jua_muutt23_001/README.md) |
| `FOLK_19832024_jua_muuttomaanosa25_001.xml` | FOLK_MUUTTO_MAANOSA Maanosatasoiset muuttotiedot | 1983-01-01 - 2024-12-31 | 25 | — | [→](./datasets/FOLK_19832024_jua_muuttomaanosa25_001/README.md) |
| `FOLK_19832024_jua_muuttosuomimuu25_001.xml` | FOLK_MUUTTO_SUOMI_MUU Karkeat muuttotiedot tasolla Suomi/muu | 1983-01-01 - 2024-12-31 | 15 | — | [→](./datasets/FOLK_19832024_jua_muuttosuomimuu25_001/README.md) |
| `FOLK_19872022_jua_tkt25_001.xml` | FOLK työssäkäynti | 1987-12-31 - 2022-12-31 | 48 | — | [→](./datasets/FOLK_19872022_jua_tkt25_001/README.md) |
| `FOLK_19872022_jua_tulo24_001.xml` | FOLK tulotieto | 1987-01-01 - 2023-12-31 | 32 | — | [→](./datasets/FOLK_19872022_jua_tulo24_001/README.md) |
| `FOLK_19872023_jua_askun25_001.xml` | FOLK asuntokunta | 1987-12-31 - 2023-12-31 | 31 | — | [→](./datasets/FOLK_19872023_jua_askun25_001/README.md) |
| `FOLK_19872023_jua_aslii24_001.xml` | FOLK asuinliitot | 1987-12-31 - 2024-12-31 | 17 | — | [→](./datasets/FOLK_19872023_jua_aslii24_001/README.md) |
| `FOLK_19872023_jua_perh24_001.xml` | FOLK  perhe | 1987-01-01 - 2024-12-31 | 15 | — | [→](./datasets/FOLK_19872023_jua_perh24_001/README.md) |
| `FOLK_19872023_jua_perus24_001.xml` | FOLK perustieto | 1987-01-01 - 2024-12-31 | 61 | — | [→](./datasets/FOLK_19872023_jua_perus24_001/README.md) |
| `FOLK_19872023_jua_tyosu25_001.xml` | FOLK jaksotiedot: työsuhde | 1987-01-01 - 2023-12-31 | 18 | — | [→](./datasets/FOLK_19872023_jua_tyosu25_001/README.md) |
| `FOLK_19872024_jua_tutk26_001.xml` | FOLK tutkinto | 1987-12-31 - 2024-12-31 | 22 | — | [→](./datasets/FOLK_19872024_jua_tutk26_001/README.md) |
| `FOLK_19912023_jua_sijoi24_001.xml` | FOLK jaksotiedot: sijoitetut | 1991-01-01 - 2024-12-31 | 7 | — | [→](./datasets/FOLK_19912023_jua_sijoi24_001/README.md) |
| `FOLK_19912023_jua_tyonh24_001.xml` | FOLK jaksotiedot: työnhakijat | 1991-01-01 - 2024-12-31 | 6 | — | [→](./datasets/FOLK_19912023_jua_tyonh24_001/README.md) |
| `FOLK_19912023_jua_tyott24_001.xml` | FOLK jaksotiedot: työttömät | 1991-01-01 - 2024-12-31 | 6 | — | [→](./datasets/FOLK_19912023_jua_tyott24_001/README.md) |
| `FOLK_19952023_jua_elake25_001.xml` | FOLK jaksotiedot: eläke | 1995-01-01 - 2023-12-31 | 7 | — | [→](./datasets/FOLK_19952023_jua_elake25_001/README.md) |
| `FOLK_20052023_jua_tyovk24_001.xml` | FOLK jaksotiedot: työvoimakoulutus | 2005-01-01 - 2024-12-31 | 5 | — | [→](./datasets/FOLK_20052023_jua_tyovk24_001/README.md) |
| `FOLK_20192025_jua_VAKA_001.xml` | FOLK_VAKA - Vardaan pohjautuvat varhaiskasvatustiedot kuukausitasolla | 2019-01-01 - 2024-12-31 | 20 | — | [→](./datasets/FOLK_20192025_jua_VAKA_001/README.md) |
| `INFRA_19872022_jua_sijainti_001.xml` | INFRA Sijaintitietomoduuli | 1987-12-31 - 2024-12-31 | 7 | — | [→](./datasets/INFRA_19872022_jua_sijainti_001/README.md) |
| `KEHA_2022_jua_URA_002.xml` | KEHA_URA-aineisto | 2000-01-01 - 2024-12-31 | 39 | 15,293,186 | [→](./datasets/KEHA_2022_jua_URA_002/README.md) |
| `KELA_20172018_jua_perustulojaksot_001.xml` | KELA_perustulorekisteri, Perustulojaksot | 2017-01-01 - 2018-12-31 | 8 | — | [→](./datasets/KELA_20172018_jua_perustulojaksot_001/README.md) |
| `KELA_20172018_jua_perustulokokeilunkohdejoukko_001.xml` | KELA_perustulorekisteri, Perustulokokeilun kohdejoukko | 2017-01-01 - 2018-12-31 | 4 | — | [→](./datasets/KELA_20172018_jua_perustulokokeilunkohdejoukko_001/README.md) |
| `KELA_20172018_jua_perustulomaksut_001.xml` | KELA_perustulorekisteri, Perustulomaksut | 2017-01-01 - 2018-12-31 | 5 | — | [→](./datasets/KELA_20172018_jua_perustulomaksut_001/README.md) |
| `KELA_20172018_jua_poiskuittauksetetuuksista_001.xml` | KELA_perustulorekisteri, Poiskuittaukset etuuksista | 2017-01-01 - 2018-12-31 | 5 | — | [→](./datasets/KELA_20172018_jua_poiskuittauksetetuuksista_001/README.md) |
| `MIGR_OLESK_jua_hakemukset_000.xml` | MIGR_OLESK Oleskelulupatiedot - Hakemukset | 2011-01-01 - 2024-12-31 | 17 | — | [→](./datasets/MIGR_OLESK_jua_hakemukset_000/README.md) |
| `MIGR_OLESK_jua_henkilotiedot_000.xml` | MIGR_OLESK Oleskelulupatiedot - Henkilötiedot | 2011-01-01 - 2024-12-31 | 7 | — | [→](./datasets/MIGR_OLESK_jua_henkilotiedot_000/README.md) |
| `MIGR_OLESK_jua_kanspaatos_000.xml` | MIGR_OLESK Oleskelulupatiedot - Kansalaisuuspäätökset | 2011-01-01 - 2024-12-31 | 6 | — | [→](./datasets/MIGR_OLESK_jua_kanspaatos_000/README.md) |
| `MIGR_OLESK_jua_paatoksetjaper_000.xml` | MIGR_OLESK Oleskelulupatiedot - Päätökset ja peruutukset | 2011-01-01 - 2024-12-31 | 21 | — | [→](./datasets/MIGR_OLESK_jua_paatoksetjaper_000/README.md) |
| `MIGR_OLESK_jua_voimassaoleva_000.xml` | MIGR_OLESK Oleskelulupatiedot - Voimassaolevat | 2011-01-01 - 2024-12-31 | 18 | — | [→](./datasets/MIGR_OLESK_jua_voimassaoleva_000/README.md) |
| `MIGR_OLESK_jua_yhteystiedot_000.xml` | MIGR_OLESK Oleskelulupatiedot - Yhteystiedot | 2011-01-01 - 2024-12-31 | 8 | — | [→](./datasets/MIGR_OLESK_jua_yhteystiedot_000/README.md) |
| `MIGR_OPISK_jua_opiskelutied_000.xml` | MIGR_OPISK Oleskelulupaa hakeneiden opiskelutiedot | 2011-01-01 - | 8 | — | [→](./datasets/MIGR_OPISK_jua_opiskelutied_000/README.md) |
| `MIGR_PERHE_jua_perheside_000.xml` | MIGR_PERHE Oleskelulupaa hakeneiden perhetiedot - perheside | 2011-01-01 - | 5 | — | [→](./datasets/MIGR_PERHE_jua_perheside_000/README.md) |
| `MIGR_PERHE_jua_siviilisaaty_000.xml` | MIGR_PERHE Oleskelulupaa hakeneiden perhetiedot - siviilisääty | 2011-01-01 - | 7 | — | [→](./datasets/MIGR_PERHE_jua_siviilisaaty_000/README.md) |
| `MIGR_TYO_jua_osapaatokset_000.xml` | MIGR_TYO Oleskelulupaa hakeneiden työskentelytiedot - osapäätökset | 2011-01-01 - 2024-12-31 | 14 | — | [→](./datasets/MIGR_TYO_jua_osapaatokset_000/README.md) |
| `MIGR_TYO_jua_tyoehdot_000.xml` | MIGR_TYO Oleskelulupaa hakeneiden työskentelytiedot - työehdot | 2011-01-01 - | 30 | — | [→](./datasets/MIGR_TYO_jua_tyoehdot_000/README.md) |
| `MIGR_VOPAL_jua_vopalvelut_000.xml` | MIGR_VOPAL Oleskelulupaa hakeneiden vastaanottopalvelutiedot - vastaanottopalvelut | 2011-01-01 - 2025-12-31 | 8 | — | [→](./datasets/MIGR_VOPAL_jua_vopalvelut_000/README.md) |
| `MIGR_VOPAL_jua_vorahat_000.xml` | MIGR_VOPAL Oleskelulupaa hakeneiden vastaanottopalvelutiedot - vastaanottorahat | 2011-01-01 - 2025-12-31 | 13 | — | [→](./datasets/MIGR_VOPAL_jua_vorahat_000/README.md) |
| `PIAAC_202500_jua_survey_001.xml` | PIAAC2 – Aikuisten taitotutkimus II | 2022-09-01 - 2023-06-30 | 175 | 4,061 | [→](./datasets/PIAAC_202500_jua_survey_001/README.md) |
| `PRH_19942019_jua_board_001.xml` | PRH_BOARD Kaupparekisterin vastuuhenkilötiedot | 1994-01-01 - 2019-07-14 | 10 | — | [→](./datasets/PRH_19942019_jua_board_001/README.md) |
| `PRH_20162023_jua_board_002.xml` | PRH_BOARD Kaupparekisterin vastuuhenkilötiedot | 2016-01-01 - 2022-12-31 | 12 | — | [→](./datasets/PRH_20162023_jua_board_002/README.md) |
| `SES_19952019_jua_harkun_001.xml` | SES Harmonisoitu palkkarakennepaneeli - kuntasektori 1995-2019 | 1995-01-01 - 2019-12-31 | 32 | 10,746,092 | [→](./datasets/SES_19952019_jua_harkun_001/README.md) |
| `SES_19952020_jua_base22tot_001.xml` | SES Palkkarakenneaineistopaneeli 1995-2020 | 1995-01-01 - 2020-12-31 | 32 | 34,636,712 | [→](./datasets/SES_19952020_jua_base22tot_001/README.md) |
| `SES_19952020_jua_haryks_001.xml` | SES - harmonisoitu palkkarakennepaneeli - yksityinen sektori 1995-2020 (HSES) | 1995-01-01 - 2020-12-31 | 39 | 20,605,840 | [→](./datasets/SES_19952020_jua_haryks_001/README.md) |
| `SES_19952021_jua_base23tot_001.xml` | SES Palkkarakenneaineistopaneeli 1995-2021 | 1995-01-01 - 2021-12-31 | 34 | 36,060,720 | [→](./datasets/SES_19952021_jua_base23tot_001/README.md) |
| `SES_19952022_jua_base24tot_001.xml` | SES Palkkarakenneaineistopaneeli 1995-2022 | 1995-01-01 - 2022-01-31 | 34 | 37,531,173 | [→](./datasets/SES_19952022_jua_base24tot_001/README.md) |
| `SES_19952022_jua_harkun_001.xml` | Harmonisoitu palkkarakennepaneeli - kuntasektori 1995-2022 | 1995-01-01 - 2022-12-31 | 33 | 12,073,966 | [→](./datasets/SES_19952022_jua_harkun_001/README.md) |
| `SES_19952022_jua_harval_001.xml` | SES Harmonisoitu palkkarakennepaneeli - valtiosektori 1995-2022 (HSES) | 1995-01-01 - 2022-12-31 | 34 | 3,027,061 | [→](./datasets/SES_19952022_jua_harval_001/README.md) |
| `SES_19952023_jua_base25tot_001.xml` | SES Palkkarakenneaineistopaneeli 1995-2023 | 1995-01-01 - 2023-12-31 | 35 | 39,025,932 | [→](./datasets/SES_19952023_jua_base25tot_001/README.md) |
| `SES_19952023_jua_harkun_001.xml` | Harmonisoitu palkkarakennepaneeli - kuntasektori 1995-2023 | 1995-01-01 - 2023-12-31 | 32 | 12,529,686 | [→](./datasets/SES_19952023_jua_harkun_001/README.md) |
| `SES_19952023_jua_harval_001.xml` | SES Harmonisoitu palkkarakennepaneeli - valtiosektori 1995-2023 (HSES) | 1995-01-01 - 2023-12-31 | 33 | 3,121,166 | [→](./datasets/SES_19952023_jua_harval_001/README.md) |
| `SES_19952023_jua_haryks_001.xml` | SES - harmonisoitu palkkarakennepaneeli - yksityinen sektori 1995-2023 (HSES) | 1995-01-01 - 2023-12-31 | 38 | 23,367,991 | [→](./datasets/SES_19952023_jua_haryks_001/README.md) |
| `SURVEY_0000_jua_aikuiskoulutus_001.xml` | SURVEY_Aikuiskoulutus - Haastattelu- ja kyselytutkimus aikuisväestön koulutukseen osallistumisesta ja oppimisesta | — | 1 | — | [→](./datasets/SURVEY_0000_jua_aikuiskoulutus_001/README.md) |
| `SURVEY_0000_jua_kulutusaikasarja_0001.xml` | SURVEY_Kulutus_Aikasarja – haastattelu- ja kyselytutkimus kotitalouksien kulutuksesta Suomessa: aikasarja | — | 1 | — | [→](./datasets/SURVEY_0000_jua_kulutusaikasarja_0001/README.md) |
| `SURVEY_0000_jua_tyoolo_001.xml` | SURVEY_Tyoolo - haastattelu- ja kyselytutkimus palkansaajien työoloista | — | 1 | — | [→](./datasets/SURVEY_0000_jua_tyoolo_001/README.md) |
| `SURVEY_0000_jua_tyovoima_0001.xml` | SURVEY_Tyovoima – haastattelu- ja kyselytutkimus väestön työmarkkinoille osallistumisesta | — | 1 | — | [→](./datasets/SURVEY_0000_jua_tyovoima_0001/README.md) |
| `SURVEY_0000_jua_varallisuusaikasarja8719_001.xml` | SURVEY_Varallisuus_aikasarja_1987_2019 - Haastattelu- ja kyselytutkimus suomalaisten kotitalouksien varallisuudesta. Aikasarja-aineisto. | — | 1 | — | [→](./datasets/SURVEY_0000_jua_varallisuusaikasarja8719_001/README.md) |
| `SURVEY_0000_jua_varallisuusaikasarja8723_001.xml` | SURVEY_Varallisuus_aikasarja_1987_2023 - Haastattelu- ja kyselytutkimus suomalaisten kotitalouksien varallisuudesta. Aikasarja-aineisto. | — | 1 | — | [→](./datasets/SURVEY_0000_jua_varallisuusaikasarja8723_001/README.md) |
| `SURVEY_0000_jua_varallisuushfcs_001.xml` | SURVEY_Varallisuus_HFCS - Euroopan keskuspankin koordinoima haastattelu- ja kyselytutkimus suomalaisten kotitalouksien varallisuudesta. Vuosiaineisto. | — | 1 | — | [→](./datasets/SURVEY_0000_jua_varallisuushfcs_001/README.md) |
| `SURVEY_000_jua_kulutus_0001.xml` | SURVEY_Kulutus – haastattelu- ja kyselytutkimus kotitalouksien kulutuksesta Suomessa | — | 1 | — | [→](./datasets/SURVEY_000_jua_kulutus_0001/README.md) |
| `TAX_19951996_jua_XPER_002.xml` | TAX_XPER Työnantajan tai suorituksen maksajan vuosi-ilmoitus verohallinnolle (1995-1996) | 2000-01-01 - 2001-12-31 | 31 | — | [→](./datasets/TAX_19951996_jua_XPER_002/README.md) |
| `TAX_19971999_jua_XPER_001.xml` | TAX_XPER Työnantajan tai suorituksen maksajan vuosi-ilmoitus verohallinnolle (1997-1999) | 2000-01-01 - 2001-12-31 | 44 | — | [→](./datasets/TAX_19971999_jua_XPER_001/README.md) |
| `TAX_20002003_jua_XPER_002.xml` | TAX_XPER Työnantajan tai suorituksen maksajan vuosi-ilmoitus verohallinnolle (2000-2003) | 2000-01-01 - 2003-12-31 | 46 | — | [→](./datasets/TAX_20002003_jua_XPER_002/README.md) |
| `TAX_20042005_jua_XPER_002.xml` | TAX_XPER Työnantajan tai suorituksen maksajan vuosi-ilmoitus verohallinnolle (2004-2005) | 2004-01-01 - 2005-12-31 | 43 | — | [→](./datasets/TAX_20042005_jua_XPER_002/README.md) |
| `TAX_20062017_jua_XPER_002.xml` | TAX_XPER Työnantajan tai suorituksen maksajan vuosi-ilmoitus verohallinnolle (2006-2017) | 2006-01-01 - 2017-12-31 | 47 | — | [→](./datasets/TAX_20062017_jua_XPER_002/README.md) |
| `TAX_2018_jua_XPER_002.xml` | TAX_XPER Työnantajan tai suorituksen maksajan vuosi-ilmoitus verohallinnolle (2018) | 2018-01-01 - 2018-12-31 | 52 | — | [→](./datasets/TAX_2018_jua_XPER_002/README.md) |
| `TAX_2019_jua_XPER_001.xml` | TAX_XPER Työnantajan maksamat palkat tai muun suorituksen maksajan vuosi-ilmoitus verohallinnolle (2019) | 2019-01-01 - 2019-12-31 | 25 | — | [→](./datasets/TAX_2019_jua_XPER_001/README.md) |
| `TAX_BENEFIT_jua_deduction_002.xml` | TAX_BENEFIT Tulorekisterin etuustiedot (Deduction) | 2021-01-01 - | 19 | — | [→](./datasets/TAX_BENEFIT_jua_deduction_002/README.md) |
| `TAX_BENEFIT_jua_delivery_002.xml` | TAX_BENEFIT Tulorekisterin etuustiedot (Delivery) | 2021-01-01 - | 4 | — | [→](./datasets/TAX_BENEFIT_jua_delivery_002/README.md) |
| `TAX_BENEFIT_jua_report_002.xml` | TAX_BENEFIT Tulorekisterin etuustiedot (Report) | 2021-01-01 - | 18 | — | [→](./datasets/TAX_BENEFIT_jua_report_002/README.md) |
| `TAX_BENEFIT_jua_transactioninfo_002.xml` | TAX_BENEFIT Tulorekisterin etuustiedot (Transaction info) | 2021-01-01 - | 27 | — | [→](./datasets/TAX_BENEFIT_jua_transactioninfo_002/README.md) |
| `TAX_INCOMES_jua_delivery_002.xml` | TAX_INCOMES Tulorekisterin palkkatiedot (Delivery) | 2019-01-01 - | 23 | — | [→](./datasets/TAX_INCOMES_jua_delivery_002/README.md) |
| `TAX_INCOMES_jua_report_002.xml` | TAX_INCOMES Tulorekisterin palkkatiedot (Report) | 2019-01-01 - | 55 | — | [→](./datasets/TAX_INCOMES_jua_report_002/README.md) |
| `TAX_INCOMES_jua_transactioncode_002.xml` | TAX_INCOMES Tulorekisterin palkkatiedot (Transaction code) | 2019-01-01 - | 142 | — | [→](./datasets/TAX_INCOMES_jua_transactioncode_002/README.md) |
| `TAX_INCOMES_jua_transactioninfo_002.xml` | TAX_INCOMES Tulorekisterin palkkatiedot (Transaction info) | 2019-01-01 - | 32 | — | [→](./datasets/TAX_INCOMES_jua_transactioninfo_002/README.md) |
| `TAX_SUMINCOMES_jua_summatut_palkkatiedot.xml` | TAX_SUMINCOMES Tulorekisterin summatut palkkatiedot | 2019-01-01 - | 53 | — | [→](./datasets/TAX_SUMINCOMES_jua_summatut_palkkatiedot/README.md) |
| `TEM_19912023_jua_tyokunto_001.xml` | KEHA_Työkunto: KEHA-keskuksen työnvälitystilaston aineisto | 1991-01-01 - 2024-12-31 | 12 | 344,466 | [→](./datasets/TEM_19912023_jua_tyokunto_001/README.md) |
| `TEM_19912023_jua_tyonhakija_001.xml` | KEHA_Työnhakija: KEHA-keskuksen työnvälitystilaston aineisto | 1991-01-01 - 2024-12-31 | 23 | 5,111,297 | [→](./datasets/TEM_19912023_jua_tyonhakija_001/README.md) |
| `TEM_19912023_jua_tyonhaku_001.xml` | KEHA_Työnhaku: KEHA-keskuksen työnvälitystilaston aineisto | 1991-01-01 - 2024-12-31 | 96 | 7,757,662 | [→](./datasets/TEM_19912023_jua_tyonhaku_001/README.md) |
| `TEM_19912023_jua_tyopaikka_001.xml` | KEHA_Työpaikka: KEHA-keskuksen työnvälitystilaston aineisto | 1991-01-01 - 2024-12-31 | 25 | 4,285,687 | [→](./datasets/TEM_19912023_jua_tyopaikka_001/README.md) |
| `TON_19892024_jua_onnettomuudet_001.xml` | TONN_ONN Tieliikenneonnettomuudet - onnettomuusmoduuli | 1989-01-01 - 2024-12-31 | 51 | — | [→](./datasets/TON_19892024_jua_onnettomuudet_001/README.md) |
| `TON_19892024_jua_onnettomuudetosalliset_001.xml` | TONN_ONN_OSALL Tieliikenneonnettomuudet - onnettomuudet ja osalliset -moduuli | 1989-01-01 - 2024-12-31 | 72 | — | [→](./datasets/TON_19892024_jua_onnettomuudetosalliset_001/README.md) |
| `TRAFI_20132025_jua_ajoneuvo_001.xml` | TRAFI Moottoriajoneuvokannan aineisto, valmismoduuli1 ajoneuvotiedot | 2013-01-01 - 2025-09-30 | 128 | — | [→](./datasets/TRAFI_20132025_jua_ajoneuvo_001/README.md) |
| `TRAFI_20132025_jua_omistaja_002.xml` | TRAFI Moottoriajoneuvokannan aineisto, valmismoduuli 2  omistaja/haltijatiedot | 2013-01-01 - 2025-09-30 | 31 | — | [→](./datasets/TRAFI_20132025_jua_omistaja_002/README.md) |
| `TULLI_19992021_jua_commod_001.xml` | TULLI_COMMOD Tullin ulkomaankauppa hyödykkeittäin | 1999-01-01 - 2024-12-31 | 22 | — | [→](./datasets/TULLI_19992021_jua_commod_001/README.md) |
| `TULLI_19992021_jua_enter_001.xml` | TULLI_ENTER Tullin ulkomaankauppa yrityksittäin | 1999-01-01 - 2024-12-31 | 10 | 418,299 | [→](./datasets/TULLI_19992021_jua_enter_001/README.md) |
| `UTH_2014_jua_ATH17_001.xml` | UTH-aineisto 2014 (ATH-verrokin a-osio) | — | 17 | — | [→](./datasets/UTH_2014_jua_ATH17_001/README.md) |
| `UTH_2014_jua_THL17_001.xml` | UTH-aineisto 2014 (terveys ja hyvinvointi, THL) | — | 191 | 3,262 | [→](./datasets/UTH_2014_jua_THL17_001/README.md) |
| `UTH_2014_jua_TK17_001.xml` | UTH-aineisto 2014 (koulutus ja työmarkkinat, Tilastokeskus) | 2014-01-01 - 2014-12-31 | 223 | 3,262 | [→](./datasets/UTH_2014_jua_TK17_001/README.md) |
| `VAKA_20192024_jua_asiakkuusSuppea_001.xml` | VAKA_ASIAKKUUS_SUPPEA - vuosipäivitteiset varhaiskasvatustiedot | 2019-01-01 - 2024-12-31 | 30 | — | [→](./datasets/VAKA_20192024_jua_asiakkuusSuppea_001/README.md) |
| `VAKA_20192024_jua_asiakkuus_001.xml` | VAKA_ASIAKKUUS - kuukausipäivitteiset Vardaan pohjautuvat varhaiskasvatustiedot | 2019-01-01 - 2026-03-25 | 37 | — | [→](./datasets/VAKA_20192024_jua_asiakkuus_001/README.md) |
| `VAKA_20192026_jua_toimijaToimipaikkaSuppea_001.xml` | VAKA_TOIMIJA_TOIMIPAIKKA_SUPPEA - vuosipäivitteiset Vardaan pohjautuvat varhaiskasvatustoimija- ja -toimipaikkatiedot | 2019-01-01 - 2024-12-31 | 16 | — | [→](./datasets/VAKA_20192026_jua_toimijaToimipaikkaSuppea_001/README.md) |
| `VAKA_20192026_jua_toimijaToimipaikka_001.xml` | VAKA_TOIMIJA_TOIMIPAIKKA - kuukausipäivitteiset Vardaan pohjautuvat varhaiskasvatustoimija- ja -toimipaikkatiedot | 2019-01-01 - 2026-03-31 | 26 | — | [→](./datasets/VAKA_20192026_jua_toimijaToimipaikka_001/README.md) |
| `YA211_19861994_jua_tilinpaatos_001.xml` | FIRM_FSS Tilinpäätösaineisto 1986-1994 (YA211) | 1986-01-01 - 1994-12-31 | 84 | — | [→](./datasets/YA211_19861994_jua_tilinpaatos_001/README.md) |
| `YA211_19941998_jua_tilinpaatos_001.xml` | FIRM_FSS Tilinpäätösaineisto 1994-1998 (YA211) | 1994-01-01 - 1998-12-31 | 107 | — | [→](./datasets/YA211_19941998_jua_tilinpaatos_001/README.md) |
| `YA211_19992005_jua_tilinpaatos_001.xml` | FIRM_FSS Tilinpäätösaineisto 1999-2005 (YA211) | 1999-01-01 - 2005-12-31 | 96 | — | [→](./datasets/YA211_19992005_jua_tilinpaatos_001/README.md) |
| `YA211_20062012_jua_tilinpaatos_001.xml` | FIRM_FSS Tilinpäätösaineisto 2006-2012 (YA211) | 2006-01-01 - 2012-12-31 | 99 | — | [→](./datasets/YA211_20062012_jua_tilinpaatos_001/README.md) |
| `YA212_19741994_jua_teollisuustil_001.xml` | FIRM_PROD Teollisuustilaston aineisto 1974-1994 (YA212) | 1974-01-01 - 1994-12-31 | 165 | 166,060 | [→](./datasets/YA212_19741994_jua_teollisuustil_001/README.md) |
| `YA212_19742011_jua_ldpm_001.xml` | FIRM_PROD Teollisuuden toimipaikkapaneeli LDPM (YA212) | 1974-01-01 - 2011-12-31 | 107 | 241,471 | [→](./datasets/YA212_19742011_jua_ldpm_001/README.md) |
| `YA212_19952012_jua_teollisuustil_001.xml` | FIRM_PROD Teollisuuden rakennetilaston aineisto 1995-2012 (YA212) | 1995-01-01 - 2012-12-31 | 201 | 775,351 | [→](./datasets/YA212_19952012_jua_teollisuustil_001/README.md) |
| `YA214_20042012_jua_hyodaineetjatarvikkeet_001.xml` | FIRM_COMMOD Hyödykkeet: aineet ja tarvikkeet 2004 - 2012 (YA214) | 2004-01-01 - 2012-12-31 | 18 | 156,398 | [→](./datasets/YA214_20042012_jua_hyodaineetjatarvikkeet_001/README.md) |
| `YA214_20042012_jua_hyodtuotteet_001.xml` | FIRM_COMMOD Hyödykkeet: tuotteet 2004 - 2012 (YA214) | 2004-01-01 - 2012-12-31 | 25 | 105,309 | [→](./datasets/YA214_20042012_jua_hyodtuotteet_001/README.md) |
| `YA221_19882020_jua_yrekyritystol_001.xml` | Yritys-toimiala-aikasarja (YA221) | 1988-01-01 - 2020-12-31 | 16 | — | [→](./datasets/YA221_19882020_jua_yrekyritystol_001/README.md) |
| `YA221_2012_jua_yrekyritys_003.xml` | FIRM_ENTER Yritysrekisterin tilastotiedostot: yritykset (1982-) 2012 (YA221) | 2012-01-01 - 2012-12-31 | 68 | 330,410 | [→](./datasets/YA221_2012_jua_yrekyritys_003/README.md) |
| `YA221_2013_jua_yritysyty_002.xml` | FIRM_ENTER Yritystietovarasto: yritykset 2013 (YA221) | 2013-01-01 - 2013-12-31 | 42 | 356,440 | [→](./datasets/YA221_2013_jua_yritysyty_002/README.md) |
| `YA221_2014_jua_yritysyty_002.xml` | FIRM_ENTER Yritystietovarasto: yritykset 2014 (YA221) | 2014-01-01 - 2014-12-31 | 41 | 363,587 | [→](./datasets/YA221_2014_jua_yritysyty_002/README.md) |
| `YA221_2015_jua_yritysyty_004.xml` | FIRM_ENTER Yritystietovarasto: yritykset 2015 (YA221) | 2015-01-01 - 2015-12-31 | 41 | 360,059 | [→](./datasets/YA221_2015_jua_yritysyty_004/README.md) |
| `YA221_2016_jua_yritysyty_001.xml` | FIRM_ENTER Yritystietovarasto: yritykset 2016 (YA221) | 2016-01-01 - 2016-12-31 | 41 | 356,790 | [→](./datasets/YA221_2016_jua_yritysyty_001/README.md) |
| `YA221_2017_jua_yritysyty_002.xml` | FIRM_ENTER Yritystietovarasto: yritykset 2017 (YA221) | 2017-01-01 - 2017-12-31 | 41 | 364,514 | [→](./datasets/YA221_2017_jua_yritysyty_002/README.md) |
| `YA221_2019_jua_yritysyty_001.xml` | FIRM_ENTER Yritystietovarasto: yritykset 2019 (YA221) | 2019-01-01 - 2019-12-31 | 41 | 370,252 | [→](./datasets/YA221_2019_jua_yritysyty_001/README.md) |
| `YA221_2020_jua_yritysyty_001.xml` | FIRM_ENTER Yritystietovarasto: yritykset 2020 (YA221) | 2020-01-01 - 2020-12-31 | 41 | 370,252 | [→](./datasets/YA221_2020_jua_yritysyty_001/README.md) |
| `YA222_19882015_jua_yrektoimiptol_001.xml` | FIRM_ESTAB Toimipaikka-toimiala-aikasarja 1988-2024 | 1988-01-01 - 2024-12-31 | 14 | — | [→](./datasets/YA222_19882015_jua_yrektoimiptol_001/README.md) |
| `YA222_2012_jua_yrektoimipaikka_004.xml` | FIRM_ESTAB Yritysrekisterin tilastotiedostot: toimipaikat (1976-) 2012 (YA222) | 2012-01-01 - 2012-12-31 | 46 | 366,042 | [→](./datasets/YA222_2012_jua_yrektoimipaikka_004/README.md) |
| `YA222_2013_jua_toimipaikkayty_001.xml` | FIRM_ESTAB Yritystietovarasto: toimipaikat 2013 (YA222) | 2013-01-01 - 2013-12-31 | 29 | 389,071 | [→](./datasets/YA222_2013_jua_toimipaikkayty_001/README.md) |
| `YA222_2014_jua_toimipaikkayty_001.xml` | FIRM_ESTAB Yritystietovarasto: toimipaikat 2014 (YA222) | 2014-01-01 - 2014-12-31 | 28 | 394,283 | [→](./datasets/YA222_2014_jua_toimipaikkayty_001/README.md) |
| `YA222_2015_jua_toimipaikkayty_004.xml` | FIRM_ESTAB Yritystietovarasto: toimipaikat 2015 (YA222) | 2015-01-01 - 2015-12-31 | 29 | 390,581 | [→](./datasets/YA222_2015_jua_toimipaikkayty_004/README.md) |
| `YA222_2016_jua_toimipaikkayty_001.xml` | FIRM_ESTAB Yritystietovarasto: toimipaikat 2016 (YA222) | 2016-01-01 - 2016-12-31 | 29 | 387,373 | [→](./datasets/YA222_2016_jua_toimipaikkayty_001/README.md) |
| `YA222_2017_jua_toimipaikkayty_001.xml` | FIRM_ESTAB Yritystietovarasto: toimipaikat 2017 (YA222) | 2017-01-01 - 2017-12-31 | 29 | 396,739 | [→](./datasets/YA222_2017_jua_toimipaikkayty_001/README.md) |
| `YA222_2018_jua_toimipaikkayty_001.xml` | FIRM_ESTAB Yritystietovarasto: toimipaikat 2018 (YA222) | 2018-01-01 - 2018-12-31 | 30 | 394,044 | [→](./datasets/YA222_2018_jua_toimipaikkayty_001/README.md) |
| `YA222_2019_jua_toimipaikkayty_001.xml` | FIRM_ESTAB Yritystietovarasto: toimipaikat 2019 (YA222) | 2019-01-01 - 2019-12-31 | 30 | 399,828 | [→](./datasets/YA222_2019_jua_toimipaikkayty_001/README.md) |
| `YA222_2020_jua_toimipaikkayty_001.xml` | FIRM_ESTAB Yritystietovarasto: toimipaikat 2020 (YA222) | 2020-01-01 - 2020-12-31 | 30 | 399,828 | [→](./datasets/YA222_2020_jua_toimipaikkayty_001/README.md) |
| `YA225_20072012_jua_ofats_000.xml` | FIRM_OFATS Suomalaiset tytäryhtiöt ulkomailla 2007 - 2012 (YA225) | 2007-01-01 - 2012-12-31 | 13 | 28,512 | [→](./datasets/YA225_20072012_jua_ofats_000/README.md) |
| `YA225_2013_jua_ofats_001.xml` | FIRM_OFATS Suomalaiset tytäryhtiöt ulkomailla 2013 (YA225) | 2013-01-01 - 2013-12-31 | 13 | 4,773 | [→](./datasets/YA225_2013_jua_ofats_001/README.md) |
| `YA225_2014_jua_ofats_001.xml` | FIRM_OFATS Suomalaiset tytäryhtiöt ulkomailla 2014 (YA225) | 2014-01-01 - 2014-12-31 | 18 | 4,870 | [→](./datasets/YA225_2014_jua_ofats_001/README.md) |
| `YA225_2015_jua_ofats_001.xml` | FIRM_OFATS Suomalaiset tytäryhtiöt ulkomailla 2015 (YA225) | 2015-01-01 - 2015-12-31 | 12 | 4,870 | [→](./datasets/YA225_2015_jua_ofats_001/README.md) |
| `YA225_2016_jua_ofats_001.xml` | FIRM_OFATS Suomalaiset tytäryhtiöt ulkomailla 2016 (YA225) | 2016-01-01 - 2016-12-31 | 12 | 5,398 | [→](./datasets/YA225_2016_jua_ofats_001/README.md) |
| `YA225_2017_jua_ofats_001.xml` | FIRM_OFATS Suomalaiset tytäryhtiöt ulkomailla 2017 (YA225) | 2017-01-01 - 2017-12-31 | 12 | 5,398 | [→](./datasets/YA225_2017_jua_ofats_001/README.md) |
| `YA227_20022014_jua_pukauppa_001.xml` | FIRM_TRADE Palvelujen ulkomaankauppa 2002 - 2014 (YA227) | 2002-01-01 - 2014-12-31 | 7 | 391,670 | [→](./datasets/YA227_20022014_jua_pukauppa_001/README.md) |
| `YA227_20152016_jua_pukauppa_001.xml` | FIRM_TRADE Tavaroiden ja palveluiden ulkomaankauppa 2015 - 2016 (YA227) | 2015-01-01 - 2016-12-31 | 10 | — | [→](./datasets/YA227_20152016_jua_pukauppa_001/README.md) |
| `YA228_20092011_jua_gvc_001.xml` | FIRM_GVC Global Value Chains 2009-2011 (YA228) | 2009-01-01 - 2011-12-31 | 852 | 1,653 | [→](./datasets/YA228_20092011_jua_gvc_001/README.md) |
| `YA231_19852016_jua_tkpaneeli_002.xml` | FIRM_RDINNO T&K-paneeli (YA231) | 1985-01-01 - 2017-12-31 | 82 | 97,209 | [→](./datasets/YA231_19852016_jua_tkpaneeli_002/README.md) |
| `YA231_1991_jua_innovaatiot_001.xml` | FIRM_RDINNO Innovaatiotutkimus 1991 (YA231) | 1989-01-01 - 1991-12-31 | 244 | 876 | [→](./datasets/YA231_1991_jua_innovaatiot_001/README.md) |
| `YA231_1996_jua_innovaatiot_001.xml` | FIRM_RDINNO Innovaatiotutkimus 1996 (YA231) | 1994-01-01 - 1996-12-31 | 163 | 1,993 | [→](./datasets/YA231_1996_jua_innovaatiot_001/README.md) |
| `YA231_1998_jua_innovaatiot_001.xml` | FIRM_RDINNO Innovaatiotutkimus 1998 (YA231) | 1996-01-01 - 1998-12-31 | 18 | 3,038 | [→](./datasets/YA231_1998_jua_innovaatiot_001/README.md) |
| `YA231_2000_jua_innovaatiot_001.xml` | FIRM_RDINNO Innovaatiotutkimus 2000 (YA231) | 1998-01-01 - 2000-12-31 | 175 | 1,637 | [→](./datasets/YA231_2000_jua_innovaatiot_001/README.md) |
| `YA231_2002_jua_innovaatiot_001.xml` | FIRM_RDINNO Yritysten innovaatiotoiminta 2000 - 2002  ja Yritysten tutkimus- ja kehittäminen 2002 (YA231) | 2000-01-01 - 2002-12-31 | 252 | 3,635 | [→](./datasets/YA231_2002_jua_innovaatiot_001/README.md) |
| `YA231_2004_jua_innovaatiot_001.xml` | FIRM_RDINNO Innovaatiotutkimus 2004 (YA231) | 2002-01-01 - 2004-12-31 | 168 | 2,549 | [→](./datasets/YA231_2004_jua_innovaatiot_001/README.md) |
| `YA231_2006_jua_innovaatiot_001.xml` | FIRM_RDINNO Innovaatiotutkimus 2006 (YA231) | 2004-01-01 - 2006-12-31 | 124 | 2,464 | [→](./datasets/YA231_2006_jua_innovaatiot_001/README.md) |
| `YA231_2008_jua_innovaatiot_001.xml` | FIRM_RDINNO Innovaatiotutkimus 2008 (YA231) | 2006-01-01 - 2008-12-31 | 137 | 2,565 | [→](./datasets/YA231_2008_jua_innovaatiot_001/README.md) |
| `YA231_2010_jua_innovaatiot_002.xml` | FIRM_RDINNO Innovaatiotutkimus 2010 (YA231) | 2008-01-01 - 2010-12-31 | 157 | 2,323 | [→](./datasets/YA231_2010_jua_innovaatiot_002/README.md) |
| `YA231_2012_jua_innovaatiot_002.xml` | FIRM_RDINNO Innovaatiotutkimus 2012 (YA231) | 2010-01-01 - 2012-12-31 | 157 | 2,554 | [→](./datasets/YA231_2012_jua_innovaatiot_002/README.md) |
| `YA231_2014_jua_innovaatiot_002.xml` | FIRM_RDINNO Innovaatiotutkimus 2014 (YA231) | 2012-01-01 - 2014-12-31 | 178 | 2,414 | [→](./datasets/YA231_2014_jua_innovaatiot_002/README.md) |
| `YA231_2016_jua_innovaatiot_002.xml` | FIRM_RDINNO Innovaatiotutkimus 2016 (YA231) | 2014-01-01 - 2016-12-31 | 238 | 2,267 | [→](./datasets/YA231_2016_jua_innovaatiot_002/README.md) |
| `YA232_19852013_jua_patentithaetut_001.xml` | FIRM_PAT Suomessa haetut patentit (YA232) | 1985-01-01 - 2013-12-31 | 6 | 41,059 | [→](./datasets/YA232_19852013_jua_patentithaetut_001/README.md) |
| `YA233_20012010_jua_ictpaneeli_001.xml` | FIRM_ICT ICT-paneeli (YA233) | 2001-01-01 - 2010-12-31 | 31 | 33,111 | [→](./datasets/YA233_20012010_jua_ictpaneeli_001/README.md) |
| `YA233_2002_jua_ict_001.xml` | FIRM_ICT Tietotekniikka ja sähköinen kauppa yrityksissä 2002 (YA233) | 2002-01-01 - 2002-12-31 | 150 | 3,091 | [→](./datasets/YA233_2002_jua_ict_001/README.md) |
| `YA233_2003_jua_ict_001.xml` | FIRM_ICT Tietotekniikka ja sähköinen kauppa yrityksissä 2003 (YA233) | 2003-01-01 - 2003-12-31 | 152 | 3,279 | [→](./datasets/YA233_2003_jua_ict_001/README.md) |
| `YA233_2004_jua_ict_001.xml` | FIRM_ICT Tietotekniikka ja sähköinen kauppa yrityksissä 2004 (YA233) | 2004-01-01 - 2004-12-31 | 133 | 3,176 | [→](./datasets/YA233_2004_jua_ict_001/README.md) |
| `YA233_2005_jua_ict_001.xml` | FIRM_ICT Tietotekniikka ja sähköinen kauppa yrityksissä 2005 (YA233) | 2005-01-01 - 2005-12-31 | 152 | 3,518 | [→](./datasets/YA233_2005_jua_ict_001/README.md) |
| `YA233_2006_jua_ict_001.xml` | FIRM_ICT Tietotekniikka ja sähköinen kauppa yrityksissä 2006 (YA233) | 2006-01-01 - 2006-12-31 | 150 | 3,265 | [→](./datasets/YA233_2006_jua_ict_001/README.md) |
| `YA233_2007_jua_ict_001.xml` | FIRM_ICT Tietotekniikka ja sähköinen kauppa yrityksissä 2007 (YA233) | 2007-01-01 - 2007-12-31 | 152 | 3,452 | [→](./datasets/YA233_2007_jua_ict_001/README.md) |
| `YA233_2008_jua_ict_001.xml` | FIRM_ICT Tietotekniikka ja sähköinen kauppa yrityksissä 2008 (YA233) | 2008-01-01 - 2008-12-31 | 135 | 3,772 | [→](./datasets/YA233_2008_jua_ict_001/README.md) |
| `YA233_2009_jua_ict_001.xml` | FIRM_ICT Tietotekniikka ja sähköinen kauppa yrityksissä 2009 (YA233) | 2009-01-01 - 2009-12-31 | 170 | 3,820 | [→](./datasets/YA233_2009_jua_ict_001/README.md) |
| `YA233_2010_jua_ict_001.xml` | FIRM_ICT Tietotekniikka ja sähköinen kauppa yrityksissä 2010 (YA233) | 2010-01-01 - 2010-12-31 | 160 | 2,951 | [→](./datasets/YA233_2010_jua_ict_001/README.md) |
| `YA233_2011_jua_ict_001.xml` | FIRM_ICT Tietotekniikka ja sähköinen kauppa yrityksissä 2011 (YA233) | 2011-01-01 - 2011-12-31 | 159 | 2,981 | [→](./datasets/YA233_2011_jua_ict_001/README.md) |
| `YA233_2012_jua_ict_001.xml` | FIRM_ICT Tietotekniikka ja sähköinen kauppa yrityksissä 2012 (YA233) | 2012-01-01 - 2012-12-31 | 156 | 3,016 | [→](./datasets/YA233_2012_jua_ict_001/README.md) |
| `YA233_2013_jua_ict_001.xml` | FIRM_ICT Tietotekniikka ja sähköinen kauppa yrityksissä 2013 (YA233) | 2013-01-01 - 2013-12-31 | 139 | 3,067 | [→](./datasets/YA233_2013_jua_ict_001/README.md) |
| `YA233_2014_jua_ict_001.xml` | FIRM_ICT Tietotekniikka ja sähköinen kauppa yrityksissä 2014 (YA233) | 2014-01-01 - 2014-12-31 | 148 | 3,035 | [→](./datasets/YA233_2014_jua_ict_001/README.md) |
| `YA233_2015_jua_ict_001.xml` | FIRM_ICT Tietotekniikka ja sähköinen kauppa yrityksissä 2015 (YA233) | 2015-01-01 - 2015-12-31 | 159 | 3,070 | [→](./datasets/YA233_2015_jua_ict_001/README.md) |
| `YA233_2016_jua_ict_001.xml` | FIRM_ICT Tietotekniikka ja sähköinen kauppa yrityksissä 2016 (YA233) | 2016-01-01 - 2016-12-31 | 164 | 2,981 | [→](./datasets/YA233_2016_jua_ict_001/README.md) |
| `YA233_2017_jua_ict_001.xml` | FIRM_ICT Tietotekniikka ja sähköinen kauppa yrityksissä 2017 (YA233) | 2017-01-01 - 2017-12-31 | 179 | 2,928 | [→](./datasets/YA233_2017_jua_ict_001/README.md) |
| `YA233_2018_jua_ict_001.xml` | FIRM_ICT Tietotekniikka ja sähköinen kauppa yrityksissä 2018 (YA233) | 2018-01-01 - 2018-12-31 | 186 | 3,028 | [→](./datasets/YA233_2018_jua_ict_001/README.md) |
| `YA241_19902009_jua_occuyritys_001.xml` | FIRM_EMPENT Yritysten/toimipaikkojen ammattirakenteet (YA241) | 1990-01-01 - 2009-12-31 | 79 | — | [→](./datasets/YA241_19902009_jua_occuyritys_001/README.md) |
| `YA244_19882016_jua_henkilot_002.xml` | FLEED Yhdistetty työntekijä-työnantaja-aineisto, otos, henkilöt (YA244) | 1988-01-01 - 2016-12-31 | 165 | — | [→](./datasets/YA244_19882016_jua_henkilot_002/README.md) |
| `YA244_19882016_jua_totalhenkilot_002.xml` | FLEED Yhdistetty työntekijä-työnantaja-aineisto, totaali, henkilöt (YA244) | 1988-01-01 - 2016-12-31 | 164 | — | [→](./datasets/YA244_19882016_jua_totalhenkilot_002/README.md) |
| `YA244_19882016_jua_totaltyosuhteet_002.xml` | FLEED Yhdistetty työntekijä-työnantaja-aineisto, kokonaisaineisto, työsuhdejaksot | 1988-01-01 - 2016-12-31 | 18 | — | [→](./datasets/YA244_19882016_jua_totaltyosuhteet_002/README.md) |
| `YA244_19882016_jua_tyosuhteet_002.xml` | FLEED Yhdistetty työntekijä-työnantaja-aineisto, otos, työsuhdejaksot (YA244) | 1988-01-01 - 2016-12-31 | 18 | — | [→](./datasets/YA244_19882016_jua_tyosuhteet_002/README.md) |
| `YA244_19912016_jua_sijoitustoimenpiteet_001.xml` | FLEED Yhdistetty työntekijä-työnantaja-aineisto, otos, sijoitusjaksot (YA244) | 1991-01-01 - 2016-12-31 | 7 | — | [→](./datasets/YA244_19912016_jua_sijoitustoimenpiteet_001/README.md) |
| `YA244_19912016_jua_totalsijoitustoimenpiteet_002.xml` | FLEED Yhdistetty työntekijä-työnantaja-aineisto, sijoitusjaksot (kokonaisaineisto) | 2005-01-01 - 2016-12-31 | 7 | — | [→](./datasets/YA244_19912016_jua_totalsijoitustoimenpiteet_002/README.md) |
| `YA244_19912016_jua_totaltyonhakijat_001.xml` | FLEED Yhdistetty työntekijä-työnantaja-aineisto, kokonaisaineisto, työnhakujaksot | 2005-01-01 - 2016-12-31 | 6 | — | [→](./datasets/YA244_19912016_jua_totaltyonhakijat_001/README.md) |
| `YA244_19912016_jua_totaltyottomat_001.xml` | FLEED Yhdistetty työntekijä-työnantaja-aineisto, kokonaisiaineisto, työttömyysjaksot | 2005-01-01 - 2016-12-31 | 6 | — | [→](./datasets/YA244_19912016_jua_totaltyottomat_001/README.md) |
| `YA244_19912016_jua_tyonhakijat_001.xml` | FLEED Yhdistetty työntekijä-työnantaja-aineisto, otos, työnhakujaksot (YA244) | 1991-01-01 - 2016-12-31 | 6 | — | [→](./datasets/YA244_19912016_jua_tyonhakijat_001/README.md) |
| `YA244_19912016_jua_tyottomat_001.xml` | FLEED Yhdistetty työntekijä-työnantaja-aineisto, otos, työttömyysjaksot (YA244) | 1991-01-01 - 2016-12-31 | 6 | — | [→](./datasets/YA244_19912016_jua_tyottomat_001/README.md) |
| `YA244_19952016_jua_elakkeet_001.xml` | FLEED Yhdistetty työntekijä-työnantaja-aineisto, otos, eläkejaksot (YA244) | 1995-01-01 - 2016-12-31 | 7 | — | [→](./datasets/YA244_19952016_jua_elakkeet_001/README.md) |
| `YA244_19952016_jua_totalelakkeet_001.xml` | FLEED Yhdistetty työntekijä-työnantaja-aineisto, kokonaisaineisto, eläkejaksot | 1995-01-01 - 2016-12-31 | 7 | — | [→](./datasets/YA244_19952016_jua_totalelakkeet_001/README.md) |
| `YA244_20052016_jua_totaltyovoimakoulutukset_001.xml` | FLEED Yhdistetty työntekijä-työnantaja-aineisto, kokonaisaineisto,  työvoimakoulutusjaksot | 2005-01-01 - 2016-12-31 | 5 | — | [→](./datasets/YA244_20052016_jua_totaltyovoimakoulutukset_001/README.md) |
| `YA244_20052016_jua_tyovoimakoulutukset_001.xml` | FLEED Yhdistetty työntekijä-työnantaja-aineisto, otos, työvoimakoulutusjaksot (YA244) | 2005-01-01 - 2016-12-31 | 5 | — | [→](./datasets/YA244_20052016_jua_tyovoimakoulutukset_001/README.md) |
| `YA246_19952014_jua_palkkarakenneotos_001.xml` | SES Palkkarakenneaineisto-otos | 1995-01-01 - 2014-12-31 | 25 | 8,806,828 | [→](./datasets/YA246_19952014_jua_palkkarakenneotos_001/README.md) |
| `YA246a_19952018_jua_harmonpalrakval_002.xml` | SES Harmonisoitu palkkarakennepaneeli - valtiosektori 1995-2018 (YA246A) | 1995-01-01 - 2018-12-31 | 34 | 2,674,189 | [→](./datasets/YA246a_19952018_jua_harmonpalrakval_002/README.md) |
| `YA251_20002016_jua_yritystuet_001.xml` | FIRM_SUBSID Yritystukitietokanta 2000 - 2017 (YA251) | 2000-01-01 - 2017-12-31 | 99 | — | [→](./datasets/YA251_20002016_jua_yritystuet_001/README.md) |
| `YA251_2018_jua_yritystuet_001.xml` | FIRM_SUBSID Yritystukitietokanta 2018 | 2018-01-01 - 2018-12-31 | 53 | — | [→](./datasets/YA251_2018_jua_yritystuet_001/README.md) |
| `YA251_2019_jua_yritystuet_001.xml` | FIRM_SUBSID Yritystukitietokanta 2019 | 2019-01-01 - 2019-12-31 | 45 | — | [→](./datasets/YA251_2019_jua_yritystuet_001/README.md) |
| `YA251_2020_jua_yritystuet_001.xml` | FIRM_SUBSID Yritystukitietokanta 2020 | 2020-01-01 - 2020-12-31 | 58 | — | [→](./datasets/YA251_2020_jua_yritystuet_001/README.md) |
| `YA261_201400_jua_perheyritykset_001.xml` | FIRM_FAMBUS Perheyritykset 2014 (YA261) | 2014-01-01 - 2014-12-31 | 37 | — | [→](./datasets/YA261_201400_jua_perheyritykset_001/README.md) |
| `YA263_20112020_jua_kuormaautot_001.xml` | FIRM_TRANSP Tieliikenteen tavarankuljetukset (Perusaineisto), Kuorma-auton tiedot 2011-2020 (YA263) | 2011-01-01 - 2020-12-31 | 27 | — | [→](./datasets/YA263_20112020_jua_kuormaautot_001/README.md) |
| `YA263_20112020_jua_matkajatavarat_001.xml` | FIRM_TRANSP Tieliikenteen tavarankuljetukset (Perusaineisto), Matka- ja tavaratiedot 2011–2020 (YA263) | 2011-01-01 - 2020-12-31 | 24 | — | [→](./datasets/YA263_20112020_jua_matkajatavarat_001/README.md) |
| `ksyyt_197122_jua_kuolemansyyt_001.xml` | Kuolemansyyaineisto | 1971-01-01 - 2024-12-31 | 69 | 2,738,679 | [→](./datasets/ksyyt_197122_jua_kuolemansyyt_001/README.md) |
| `vamuu_202400_jua_000_000.xml` | FOLK_VAEN Väestön ennakkotiedot | 2015-01-01 - | 25 | — | [→](./datasets/vamuu_202400_jua_000_000/README.md) |
| `vamuu_202500_jua_000_000.xml` | FOLK_ENHEN Ennakkotiedot henkilötunnuksellisista | 2022-01-01 - | 13 | — | [→](./datasets/vamuu_202500_jua_000_000/README.md) |

## Lähteet ja rajoitukset / Source notes

- Taustalla on Taikan julkinen REST-XQ-rajapinta (`/restxq/taika/fi/datasets`, `/restxq/taika/fi/datasets/{id}`, `/restxq/taika/fi/variables/{id}`). Rajapintaa ei ole virallisesti dokumentoitu, mutta se on julkinen eikä vaadi autentikointia.
- Arkisto perustuu suomenkieliseen rajapintaan. Englanninkielinen rajapinta (`/restxq/taika/en/datasets`) on kattavuudeltaan paljon suppeampi (noin 84 aineistoa vs. suomen 312), joten sitä ei käytetä.
- `statmeta`-kenttä on Taikassa yleensä placeholder (`"metaa..."`) ja tallennetaan sellaisenaan.
- Kahdeksalla SURVEY-aineistolla muuttujaluettelo sisältää Taikan placeholder-sentinel-arvon (`emptyvariablenameforcossicreatedbycsmetaedit`); se suodatetaan pois READMEsta.
- **Henkilötunnusmuuttuja / Person ID variable:** Taika dokumentoi henkilön yksilöivän tunnisteen nykyään nimellä `hid_e`. Aiemmissa aineistotoimituksissa sama tunniste kulki nimellä `shnro`, ja Tilastokeskus on vaihtanut muuttujan nimen. Osa sisarprojekteista (mm. Student-Debt-Project, Inheritance-Project) työskentelee edelleen vanhemmilla `shnro`-toimituksilla — tarkista kunkin projektin `CLAUDE.md` ennen kuin oletat muuttujan nimen. _Taika now documents the person identifier as `hid_e`; older deliveries called it `shnro`. Several sibling projects still use the older `shnro` deliveries — check each project's CLAUDE.md before assuming a variable name._
