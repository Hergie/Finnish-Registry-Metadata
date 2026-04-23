# FIRM_EMPEST Toimipaikkakohtainen työpaikka- ja työntekijävirta-aineisto

- **Identifier:** `FIRM_19882018_jua_empestjwfl_001.xml`
- **DOI:** `ata_2014-01_2014-01-02_ain_0001`
- **Temporal coverage:** 1988-01-01 - 2022-12-31
- **Published:** 2021-06-18
- **Organisation:** Tilastokeskus
- **Variable count:** 18
- **Observation count:** —
- **Population:** Yrityssektorin toimipaikat, joissa on yli 1 henkilö
- **Source:** FLEED/FOLK-aineisto (työssäkäyntitilasto), yritysrekisteri
- **Related:** <a href= "http://www.stat.fi/meta/rekisteriselosteet/tutka_rekisteriseloste_tyopaikka_ja_tyontekijavirta.html">Työpaikka- ja työntekijävirta</a>

## Description

Työpaikka- ja työntekijävirta-aineistoon on laskettu toimipaikoittain virtatietoja käyttäen 1-vuoden aikavälejä (1988 - 1989, 1990 - 1991,  …, 2017 - 2018). 

Aineisto jwflow_vvvv on koottu yhdistämällä työssäkäyntitilastoaineisto (FLEED) yritysrekisterin toimipaikka-aineiston kanssa. Mukaan on otettu kaikki toimipaikat, joissa on yli 1 henkilöä. Vuodesta 2017 alkaen aineisto pohjautuu FLEEDin sijaan FOLK työssäkäyntimoduulin tietoihin.

Aineistossa jwflow_vvvv_stan_1p toimipaikkatason tiedot on aggregoitu yrityssektorin toimialoille. Jos ryhmässä on alle 3 toimipaikkaa, työpaikkavirtoja koskevia tunnuslukuja ei ole esitetty tietosuojasyistä. Aineisto sisältää seuraavat indikaattorit:
lkm='Number of establishments'
l_x='Number of emplyees in initial year, employment stat'=sum(l_x)
l_y='Number of emplyees in end year, employment stat'=sum(l_y)
lyr_x='Number of emplyees in initial year, business reg.'=sum(lyr_x)
lyr_y='Number of emplyees in end year, business reg.'=sum(lyr_y)
netr='Net rate, linked employees'=sum(jc-jd)/sum(l_xy)
netr_yr='Net rate, BR persons'=sum(jc_yr-jd_yr)/sum(lyr_xy)
jcr ='Job creation rate, linked emp.'=sum(jc)/sum(l_xy)
jcr_yr ='Job creation rate, BR per.'=sum(jc_yr)/sum(lyr_xy)
jcr_yr_x='Job creation rate, new plants, BR per.'
jdr = 'Job destruction rate, linked emp.'=sum(jd)/sum(l_xy)
jdr_yr='Job destruction rate, BR per.'=sum(jd_yr)/sum(lyr_xy)
jdr_yr_x='Job destruction rate, exit plants, BR per.'
ejr= 'Excess job reallocation rate'=sum(jc+jd)/sum(l_xy)-abs(sum(jc-jd)/sum(l_xy))
ejr_yr= 'Excess job reallocation, BR'=sum(jc_yr+jd_yr)/sum(lyr_xy)-abs(sum(jc_yr-jd_yr)/sum(lyr_xy))
wifr= 'Worker inflow rate'=sum(wif)/sum(l_xy)
wofr= 'Worker outflow rate'=sum(wof)/sum(l_xy)
cfr='Churning rate'=sum(wif+wof-jc-jd)/sum(l_xy)

Aineisto on alunperin tuotettu osana OECD:n Multiprod-hanketta. 

Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@tilastokeskus.fi.

## Variables (18)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `sykstun` | suojattu toimipaikkatunnus | — | — | — |
| `l_x` | työlliset lähtövuonna, työssäkäynti | — | — | — |
| `l_y` | työlliset päätevuonna, työssäkäynti | — | — | — |
| `vuosi` | vuosi | — | — | — |
| `jcr` | työpaikkojen syntyminen, työssäkäynti | — | — | — |
| `jdr` | työpaikkojen tuhoutuminen, työssäkäynti | — | — | — |
| `wif` | sisään tulleet työntekijät | — | — | — |
| `wof` | ulos menneet työntekijät | — | — | — |
| `l_xy` | työlliset keskimäärin, työssäkäynti | — | — | — |
| `lyr_x` | työlliset lähtövuonna, yritysrekisteri | — | — | — |
| `lyr_y` | työlliset päätevuonna, yritysrekisteri | — | — | — |
| `jcr_yr` | työpaikkojen syntyminen, yritysrekisteri | — | — | — |
| `jdr_yr` | työpaikkojen tuhoutuminen, yritysrekisteri | — | — | — |
| `lyr_xy` | työlliset keskimäärin, yritysrekisteri | — | — | — |
| `jcr_yr_x` | työpaikkojen syntyminen, uudet toimipaikat, yritysrekisteri | — | — | — |
| `jdr_yr_x` | työpaikkojen tuhoutuminen, lopetetut toimipaikat, yritysrekisteri | — | — | — |
| `stan` | OECD STAN toimialaluokitus | — | — | — |
| `stan_lab` | STAN labelit | — | — | — |

### Variable definitions

#### `sykstun` — suojattu toimipaikkatunnus

#### `l_x` — työlliset lähtövuonna, työssäkäynti

#### `l_y` — työlliset päätevuonna, työssäkäynti

#### `vuosi` — vuosi

#### `jcr` — työpaikkojen syntyminen, työssäkäynti

#### `jdr` — työpaikkojen tuhoutuminen, työssäkäynti

#### `wif` — sisään tulleet työntekijät

#### `wof` — ulos menneet työntekijät

#### `l_xy` — työlliset keskimäärin, työssäkäynti

#### `lyr_x` — työlliset lähtövuonna, yritysrekisteri

#### `lyr_y` — työlliset päätevuonna, yritysrekisteri

#### `jcr_yr` — työpaikkojen syntyminen, yritysrekisteri

#### `jdr_yr` — työpaikkojen tuhoutuminen, yritysrekisteri

#### `lyr_xy` — työlliset keskimäärin, yritysrekisteri

#### `jcr_yr_x` — työpaikkojen syntyminen, uudet toimipaikat, yritysrekisteri

#### `jdr_yr_x` — työpaikkojen tuhoutuminen, lopetetut toimipaikat, yritysrekisteri

#### `stan` — OECD STAN toimialaluokitus

#### `stan_lab` — STAN labelit

---

[← Back to catalogue](../../README.md)
