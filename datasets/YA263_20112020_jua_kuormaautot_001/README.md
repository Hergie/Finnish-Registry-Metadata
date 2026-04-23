# FIRM_TRANSP Tieliikenteen tavarankuljetukset (Perusaineisto), Kuorma-auton tiedot 2011-2020 (YA263)

- **Identifier:** `YA263_20112020_jua_kuormaautot_001.xml`
- **DOI:** `kttav_2017-01_2017-01-20_ain_0001`
- **Temporal coverage:** 2011-01-01 - 2020-12-31
- **Published:** 2021-12-09
- **Organisation:** Tilastokeskus
- **Variable count:** 27
- **Observation count:** —
- **Population:** Suomessa sekä yksityiseen että luvanvaraiseen liikenteeseen rekisteröityjen kuorma-autojen kotimaan kuljetustoiminta. Tilastoyksikkönä on kuorma-auto.
- **Keywords:** kuljetus,kuljetussuoritteet,kuorma-autoliikenne,kuorma-autot,liikenne,liikennesuoritteet,tavaraliikenne,tieliikenne

## Description

Kotimaan tieliikenteen tavarankuljetusaineisto kuvaa Suomeen sekä yksityiseen että luvanvaraiseen liikenteeseen rekisteröityjen kuorma-autojen kuljetustoimintaa kotimaassa. Kyseessä on ainoa säännöllisesti tehtävä selvitys kotimaan tieliikenteen tavarankuljetuksista. Tilaston tiedot ovat vertailukelpoisia muiden EU-maiden vastaaviin tilastoihin.

Tilaston perusjoukon muodostavat Suomessa rekisteröidyt kokonaispainoltaan yli 3,5 tonnin kuorma-autot. Tutkimuksen ulkopuolelle jäävät armeijan ajoneuvot ja sellaiset kuorma-autot, joita ei ole ensisijaisesti tarkoitettu tavarankuljetukseen (esim. museoautot ja erikoisajoneuvot). Ahvenanmaalle rekisteröidyt kuorma-autot eivät ole mukana tilastoinnissa. Tilastoyksikkönä on kuorma-auto.

Aineisto perustuu neljännesvuosittain sähköisenä tutkimuksena tehtävään otostutkimukseen. Otos on jaettu kahdeksaan ositteeseen käyttäen hyväksi rekisteritietoja kuorma-auton käytöstä joko yksityisessä tai luvanvaraisessa liikenteessä sekä tietoa kuorma-autotyypistä. Vuosittain kysely osoitetaan yhteensä 10 000 kuorma-auton haltijalle, joilta pyydetään tietoja kuorma-autosta ja sen käytöstä kolmen tai neljän peräkkäisen tutkimuspäivän aikana. Aineiston tiedot perustuvat kyselyn perusteella saatuihin kuorma-autojen matkatietoihin, jotka voidaan tilastollisin menetelmin ja painokertoimia käyttämällä korottaa vastaamaan koko otoskehikkoa ja vuosineljännestä. Otos on painotettu ammattimaisiin varsinaisiin perävaunuyhdistelmiin, koska näiden kuorma-autojen merkitys on suurin kuljetussuoritteen estimoimisessa.

Tehtävissä analyyseissa on syytä ottaa huomioon, että kyseessä on otospohjaisella kyselytutkimuksella kerätty aineisto, joka ei ole kaiken kattava. Niinpä esimerkiksi vaarallisten aineiden kuljetuksista tavoitetaan vain osa. Aineiston pääasiallinen tarkoitus on erilaisten suoritteiden tason estimointi koko maan tasolla, joten sen käyttö kovin yksityiskohtaisiin tarkasteluihin ei ole suositeltavaa.
 
Tieliikenteen tavarankuljetusten perusaineisto jakautuu kahteen osaan: kuorma-auton tiedot sekä ajettujen matkojen ja tavaroiden tiedot. Aineistot voidaan yhdistää vuosi- ja järjestysnumero (jnro) muuttujilla. Ennen yhdistämistä aineistot on järjestettävä näiden molempien muuttujien mukaan.

Mikäli aineistosta halutaan laskea Tilastokeskuksen tilastoja vastaavat kuljetussuoritteet, on otettava huomioon kaksi muuttujaa: matkatyyppi (matkaty) sekä samanlaisten matkojen lukumäärä (mlkm).

Kuljetussuoritteen laskennan aluksi tavaramäärä-muuttuja täytyy korottaa painokertoimella (tmaara*kerroin). Kuljetussuoritteen laskemisessa huomioidaan siis tavaramassan (tmaara) ja matkan pituuden (mpit) lisäksi myös samanlaisten matkojen lukumäärä sekä matkatyyppi. Jos matkatyyppi = 3, niin kuljetussuorite saa kertoimen 0.5. Samanlaisten matkojen lukumäärä taas lisätään sellaisenaan laskukaavaan:

IF matkaty=3 -> kuljetussuorite (milj. tkm) = kerroin*tmaara*mpit*mlkm*0.5/1 000 000 000
ELSE -> 	   kuljetussuorite = kerroin*tmaara*mpit*mlkm /1 000 000 000

Tilastovuoden 2020 päivityksessä on korvattu suojatut henkilötunnukset suojatuilla Tilastokeskuksen henkilönumeroilla vuosina 2011-2020.

## Variables (27)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `jnro` | Juokseva numero | — | — | — |
| `vuosi` | Tilastointivuosi | — | — | — |
| `nelj` | Tilastointineljännes | — | — | — |
| `osite` | Osite | — | — | — |
| `kpvm` | Kuorma-auton käyttöönottopäivä | — | — | — |
| `kaytto` | Ajoneuvon käyttö | — | ajon_kaytto_2_1995_01_01 | — |
| `opaino` | Ajoneuvon omamassa (kg) | — | — | — |
| `kantav` | Ajoneuvon kantavuus (kg) | — | — | — |
| `kpaino` | Ajoneuvon kokonaispaino, joka on tieliikenteessä suurin sallittu kokonaismassa (kg) | — | — | — |
| `ykantav` | Ajoneuvon ja perävaunun yhteinen kantavuus (kg) | — | — | — |
| `kokpain` | Ajoneuvon ja perävaunun yhteinen kokonaismassa (kg) | — | — | — |
| `ktyyp` | Kuormakorityyppi | — | kuormatyyppi_1_2017_01_30 | — |
| `lisal` | Lisälaitekoodi | — | lisal_1_2017_01_30 | — |
| `akseli` | Akseleiden lukumäärä | — | — | — |
| `ajo` | Ajoneuvon käyttö tutkimuspäivinä | — | ajon_kaytto_3_2017_02_01 | — |
| `liiken` | Kuorma-auton liikennöinti | — | ajon_kaytto_3_2017_02_02 | — |
| `tyyppi` | Kuorma-auton tyyppi tutkimuspäivinä | — | ktyyppi_1_1995_01_01 | — |
| `km` | Edellisvuonna ajetut kilometrit | — | — | — |
| `km_ulko` | Edellisvuonna ajetut kilometrit ulkomailla | — | — | — |
| `tpvm` | Tutkimuspäivämäärä | — | — | — |
| `jalki_osite` | Jälkiosite | — | kttavosite_1_2017_01_23 | — |
| `jakson_pituus` | Tutkimusjakson pituus vuorokausina | — | — | — |
| `kerroin` | kerroin | — | — | — |
| `shatun` | Ajoneuvon haltijan suojattu Y-tunnus tai henkilönumero | — | — | — |
| `shtun` | Ajoneuvon omistajan suojattu Y-tunnus tai henkilönumero | — | — | — |
| `idtyyp_hatun` | Yritystunnuksen tyyppi | — | — | — |
| `idtyyp_htun` | Yritystunnuksen tyyppi | — | — | — |

### Variable definitions

#### `jnro` — Juokseva numero

#### `vuosi` — Tilastointivuosi

#### `nelj` — Tilastointineljännes

#### `osite` — Osite

#### `kpvm` — Kuorma-auton käyttöönottopäivä

#### `kaytto` — Ajoneuvon käyttö

**Classification:** ajon_kaytto_2_1995_01_01

Ajoneuvon käyttö (yks/amm)

#### `opaino` — Ajoneuvon omamassa (kg)

Ajoneuvon omamassa. Saadaan ATJ:n massa-taulusta muuttujasta omamassa, 
joka on ajoneuvon mitattu koko omamassa kilogrammoina.

#### `kantav` — Ajoneuvon kantavuus (kg)

Ajoneuvon kantavuus. Saadaan kaavalla kantav=kpaino-opaino.

#### `kpaino` — Ajoneuvon kokonaispaino, joka on tieliikenteessä suurin sallittu kokonaismassa (kg)

Ajoneuvon kokonaispaino. Saadaan ATJ:n massa-taulusta muuttujasta 
tieliiksuursallkokmassa, joka on tieliikenteessä suurin sallittu kokonaismassa kiloina.

#### `ykantav` — Ajoneuvon ja perävaunun yhteinen kantavuus (kg)

Ajoneuvon ja perävaunun yhteinen kantavuus.

#### `kokpain` — Ajoneuvon ja perävaunun yhteinen kokonaismassa (kg)

Ajoneuvon ja perävaunun yhteinen kokonaismassa.

#### `ktyyp` — Kuormakorityyppi

**Classification:** kuormatyyppi_1_2017_01_30

#### `lisal` — Lisälaitekoodi

**Classification:** lisal_1_2017_01_30

#### `akseli` — Akseleiden lukumäärä

#### `ajo` — Ajoneuvon käyttö tutkimuspäivinä

**Classification:** ajon_kaytto_3_2017_02_01

#### `liiken` — Kuorma-auton liikennöinti

**Classification:** ajon_kaytto_3_2017_02_02

#### `tyyppi` — Kuorma-auton tyyppi tutkimuspäivinä

**Classification:** ktyyppi_1_1995_01_01

#### `km` — Edellisvuonna ajetut kilometrit

#### `km_ulko` — Edellisvuonna ajetut kilometrit ulkomailla

#### `tpvm` — Tutkimuspäivämäärä

#### `jalki_osite` — Jälkiosite

**Classification:** kttavosite_1_2017_01_23

#### `jakson_pituus` — Tutkimusjakson pituus vuorokausina

#### `kerroin` — kerroin

Tulosten estimoinnissa käytettävä painokerroin

#### `shatun` — Ajoneuvon haltijan suojattu Y-tunnus tai henkilönumero

#### `shtun` — Ajoneuvon omistajan suojattu Y-tunnus tai henkilönumero

#### `idtyyp_hatun` — Yritystunnuksen tyyppi

Yritystunnuksen tyyppi
1 = y-tunnus
2 = henkilönumero
3 = muu (esim. tekstiä tai liian lyhyt)

#### `idtyyp_htun` — Yritystunnuksen tyyppi

Yritystunnuksen tyyppi
1 = y-tunnus
2 = henkilönumero
3 = muu (esim. tekstiä tai liian lyhyt)

---

[← Back to catalogue](../../README.md)
