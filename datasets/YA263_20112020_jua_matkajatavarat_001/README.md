# FIRM_TRANSP Tieliikenteen tavarankuljetukset (Perusaineisto), Matka- ja tavaratiedot 2011–2020 (YA263)

- **Identifier:** `YA263_20112020_jua_matkajatavarat_001.xml`
- **DOI:** `kttav_2017-01_2017-01-20_ain_0002`
- **Temporal coverage:** 2011-01-01 - 2020-12-31
- **Published:** 2021-12-09
- **Organisation:** Tilastokeskus
- **Variable count:** 24
- **Observation count:** —
- **Population:** Suomessa sekä yksityiseen että luvanvaraiseen liikenteeseen rekisteröityjen kuorma-autojen kotimaan kuljetustoiminta. Tilastoyksikkönä on kuorma-auto.
- **Keywords:** kuljetus,kuljetussuoritteet,kuorma-autoliikenne,kuorma-autot,liikenne,liikennesuoritteet,tavaraliikenne,tieliikenne

## Kuvaus / Description

Tieliikenteen tavarankuljetusaineisto kuvaa Suomeen sekä yksityiseen että luvanvaraiseen liikenteeseen rekisteröityjen kuorma-autojen kuljetustoimintaa koti- ja ulkomailla. Ulkomaan liikenteellä tarkoitetaan Suomesta ulkomaille (vienti), ulkomailta Suomeen (tuonti), ulkomaasta toiseen ulkomaahan (crosstrade) sekä ulkomaan sisällä (kabotaasi) ajettavia kuljetuksia. Kyseessä on ainoa säännöllisesti tehtävä selvitys kotimaan tieliikenteen tavarankuljetuksista.

Tilaston perusjoukon muodostavat Suomessa rekisteröidyt kokonaispainoltaan yli 3,5 tonnin kuorma-autot. Tutkimuksen ulkopuolelle jäävät armeijan ajoneuvot ja sellaiset kuorma-autot, joita ei ole ensisijaisesti tarkoitettu tavarankuljetukseen (esim. museoautot ja erikoisajoneuvot). Ahvenanmaalle rekisteröidyt kuorma-autot eivät ole mukana tilastoinnissa. Tilastoyksikkönä on kuorma-auto.

Aineisto perustuu neljännesvuosittain sähköisenä tutkimuksena tehtävään otostutkimukseen. Otos on jaettu kahdeksaan ositteeseen käyttäen hyväksi rekisteritietoja kuorma-auton käytöstä joko yksityisessä tai luvanvaraisessa liikenteessä sekä tietoa kuorma-autotyypistä. Vuosittain kysely osoitetaan yhteensä 10 000 kuorma-auton haltijalle, joilta pyydetään tietoja kuorma-autosta ja sen käytöstä kolmen tai neljän peräkkäisen tutkimuspäivän aikana. Aineiston tiedot perustuvat kyselyn perusteella saatuihin kuorma-autojen matkatietoihin, jotka voidaan tilastollisin menetelmin ja painokertoimia käyttämällä korottaa vastaamaan koko otoskehikkoa ja vuosineljännestä. Otos on painotettu ammattimaisiin varsinaisiin perävaunuyhdistelmiin, koska näiden kuorma-autojen merkitys on suurin kuljetussuoritteen estimoimisessa.

## Muuttujat / Variables (24)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `jnro` | Juokseva numero | — | — | — |
| `vuosi` | Tilastointivuosi | — | — | — |
| `nelj` | Tilastointineljännes | — | — | — |
| `rno` | Matkan numero | — | — | — |
| `pvm` | Matkan alkamispäivämäärä (ppkk) | — | — | — |
| `mlkm` | Samanlaisten matkojen lukumäärä | — | — | — |
| `almaa` | Matkan alkamismaa | — | — | — |
| `kkdi1` | Matkan alkamispaikan kunnan nimi Suomessa tai paikkakunnan nimi ulkomailla | — | — | — |
| `lno1` | Matkan alkamispaikka, jos terminaali | — | kttav_terminaal_1_2017_01_30 | — |
| `paatmaa` | Matkan päättymismaa | — | — | — |
| `kkdi2` | Matkan päättymispaikan kunnan nimi Suomessa tai paikkakunnan nimi ulkomailla | — | — | — |
| `lno2` | Matkan päättymispaikka, jos terminaali | — | kttav_terminaal_1_2017_01_30 | — |
| `Transito` | Ulkomaanmatkan transitomaat, pilkulla eroteltuna | — | — | — |
| `tlaji` | Tavaralaji | — | tavaralaji_2_2008_01_01 | — |
| `mpit` | Matkan pituus (km) | — | — | — |
| `pvaunu` | Perävaunu mukana matkan aikana | — | ktyyppi_1_2017_01_30 | — |
| `pakseli` | Perävaunun akseleiden lukumäärä | — | — | — |
| `matkaty` | Matkatyyppi | — | matka_11_2017_01_19 | — |
| `tmaara` | Kuorman paino suurimmillaan (kg) | — | — | — |
| `taytto` | Kuorman täyttöaste | — | tayttoaste_1_2017_02_01 | — |
| `adr_lk` | Vaarallisten aineiden luokka | — | adr_1_2017_01_30 | — |
| `tpi_lk` | Kuormatyyppi | — | kuormatyyppi_1_1995_01_01 | — |
| `kuntakoodi1` | Matkan alkamiskunnan koodi | — | — | — |
| `kuntakoodi2` | Matkan päättymiskunnan koodi | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `jnro` — Juokseva numero

#### `vuosi` — Tilastointivuosi

#### `nelj` — Tilastointineljännes

#### `rno` — Matkan numero

#### `pvm` — Matkan alkamispäivämäärä (ppkk)

#### `mlkm` — Samanlaisten matkojen lukumäärä

#### `almaa` — Matkan alkamismaa

#### `kkdi1` — Matkan alkamispaikan kunnan nimi Suomessa tai paikkakunnan nimi ulkomailla

#### `lno1` — Matkan alkamispaikka, jos terminaali

**Luokitus / Classification:** kttav_terminaal_1_2017_01_30

#### `paatmaa` — Matkan päättymismaa

#### `kkdi2` — Matkan päättymispaikan kunnan nimi Suomessa tai paikkakunnan nimi ulkomailla

#### `lno2` — Matkan päättymispaikka, jos terminaali

**Luokitus / Classification:** kttav_terminaal_1_2017_01_30

#### `Transito` — Ulkomaanmatkan transitomaat, pilkulla eroteltuna

#### `tlaji` — Tavaralaji

**Luokitus / Classification:** tavaralaji_2_2008_01_01

#### `mpit` — Matkan pituus (km)

#### `pvaunu` — Perävaunu mukana matkan aikana

**Luokitus / Classification:** ktyyppi_1_2017_01_30

#### `pakseli` — Perävaunun akseleiden lukumäärä

#### `matkaty` — Matkatyyppi

**Luokitus / Classification:** matka_11_2017_01_19

#### `tmaara` — Kuorman paino suurimmillaan (kg)

#### `taytto` — Kuorman täyttöaste

**Luokitus / Classification:** tayttoaste_1_2017_02_01

#### `adr_lk` — Vaarallisten aineiden luokka

**Luokitus / Classification:** adr_1_2017_01_30

#### `tpi_lk` — Kuormatyyppi

**Luokitus / Classification:** kuormatyyppi_1_1995_01_01

#### `kuntakoodi1` — Matkan alkamiskunnan koodi

#### `kuntakoodi2` — Matkan päättymiskunnan koodi

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
