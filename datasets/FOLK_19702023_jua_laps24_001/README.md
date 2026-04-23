# FOLK lapsi - vanhemmat

- **Identifier:** `FOLK_19702023_jua_laps24_001.xml`
- **DOI:** `work_2020-01_2020-01-17_ain_0001`
- **Temporal coverage:** 1970-01-01 - 2024-12-31
- **Published:** 2025-11-27
- **Organisation:** Tilastokeskus
- **Variable count:** 8
- **Observation count:** —
- **Population:** Kunkin vuoden viimeisenä päivänä Suomessa vakituisesti asunut väestö
- **Source:** VTJ

## Description

Sisältyy FOLK lapsi - vanhemmat -moduuliin. FOLK lapsi - vanhemmat on suhdeaineisto, joka sisältää biologisten vanhempien henkilötiedot niille henkilöille, joilla on tieto vanhemmista. Aineistossa lapsi tai ainakin lapsen toinen vanhemmista kuuluu FOLK väestöön, eli henkilön tiedot löytyvät joko FOLK perustieto tai FOLK Väestölaskennat 1970-1985 -aineistoista.

Aineiston lähteenä on väestötietojärjestelmä (VTJ). Väestörekisterikeskus on perustettu vuonna 1969 ja atk-pohjaiseen väestörekisteriin siirryttiin vuonna 1971. Tietoja vanhemmista on siis kattavammin vain 1950-luvulla tai myöhemmin syntyneille. Näille tieto ainakin toisesta biologisesta vanhemmasta löytyy yli 80 prosentille lapsista.

Aineisto sisältää vanhempien tietoja myös niille lapsille, jotka ovat syntyneet vuoden 1952 jälkeen, mutta joiden tietoja ei ole FOLK lapsi - vanhemmat - vuosiaineistossa. Näitä lapsia ovat ulkomailla koko elämänsä asuneet Suomen kansalaiset tai ennen syntymävuoden viimeistä päivää kuolleet lapset. Tällöin ainakin toisen vanhemmista on kuuluttava FOLK väestöön.

Aineisto on tarkoitettu otosaineistona käytettäväksi FIONA-etäkäyttöjärjestelmän kautta. Kokonaisaineistoon voidaan antaa käyttöoikeus vain, jos tutkimuksellisesta syystä kokonaisaineiston käyttöön on erityinen tarve. Tiedot ovat linkitettävissä muiden henkilövalmisaineistomoduulien kanssa suojatun henkilönumeron avulla.

FOLK lapsi - vanhemmat -aineisto on kansiossa FOLK_LAPS_C. Viimeisimmän aineiston tiedostonimi on folk_laps_19702023_1.

Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@stat.fi.

## Variables (8)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `shnro` | Suojattu TK:n henkilönumero, lapsi | — | — | — |
| `syntyv` | Syntymävuosi | — | — | — |
| `kuolv` | Kuolinvuosi | — | — | — |
| `shnro_m` | Suojattu TK:n henkilönumero, biol. äiti | — | — | — |
| `shnro_f` | Suojattu TK:n henkilönumero, biol. isä | — | — | — |
| `folk_c` | Kuuluu FOLK-aineistoon, lapsi | — | — | — |
| `folk_m` | Kuuluu FOLK-aineistoon, biol. äiti | — | — | — |
| `folk_f` | Kuuluu FOLK-aineistoon, biol. isä | — | — | — |

### Variable definitions

#### `shnro` — Suojattu TK:n henkilönumero, lapsi

Lapsen suojattu TK:n henkilönumero.

#### `syntyv` — Syntymävuosi

Lapsen syntymävuosi.

#### `kuolv` — Kuolinvuosi

Lapsen kuolinvuosi.

#### `shnro_m` — Suojattu TK:n henkilönumero, biol. äiti

Biologisen äidin suojattu TK:n henkilönumero.

#### `shnro_f` — Suojattu TK:n henkilönumero, biol. isä

Biologisen isän suojattu TK:n henkilönumero.

#### `folk_c` — Kuuluu FOLK-aineistoon, lapsi

Lapsi kuuluu FOLK-väestöön (folk_c='1') tai ei kuulu, jolloin ainakin toisen vanhemmista on kuuluttava FOLK-väestöön (folk_c='0' ja folk_m/folk_f='1').

#### `folk_m` — Kuuluu FOLK-aineistoon, biol. äiti

Biologinen äiti  kuuluu FOLK-väestöön (folk_m='1') tai ei kuulu, jolloin joko lapsen tai lapsen biologisen isän on kuuluttava FOLK-väestöön  (folk_m='0'  ja folk_c/folk_f='1'),  Jos tietoa biologisesta äidistä ei ole on arvo tyhjä.

#### `folk_f` — Kuuluu FOLK-aineistoon, biol. isä

Biologinen isä kuuluu FOLK-väestöön (folk_f='1') tai ei kuulu, jolloin joko lapsen tai lapsen biologisen äidin on kuuluttava FOLK-väestöön  (folk_f='0'  ja folk_c/folk_m='1'),  Jos tietoa biologisesta isästä ei ole on arvo tyhjä.

---

[← Back to catalogue](../../README.md)
