# FOLK asuinliitot

- **Identifier:** `FOLK_19872023_jua_aslii24_001.xml`
- **DOI:** `_2017-03_2017-03-23_ain_0001`
- **Temporal coverage:** 1987-12-31 - 2024-12-31
- **Published:** 2025-12-04
- **Organisation:** Tilastokeskus
- **Variable count:** 17
- **Observation count:** —
- **Population:** Kunkin vuoden viimeisenä päivänä Suomessa vakituisesti asunut, 18 vuotta täyttänyt väestö
- **Source:** VTJ, perhe- ja muuttotilastoaineistot

## Description

FOLK-henkilöaineiston asuinliitot -moduulissa on tietoja vuoden vaihteessa väestöön kuuluvista yhdessä asuvista pareista vuodesta 1987 lähtien. Aineisto on muodostettu perhe- ja muuttotilastoaineistojen sekä VTJ-tietojen pohjalta. Asuinliittoaineiston pareja ovat perhetilaston määritelmien mukaiset eri sukupuolta olevat avo- ja avioparit. Perhetilastoaineistosta poimituille pareille on liitetty tietoja yhteen ja erilleen muuttamisesta henkilötilastojen tietovaraston muuttotilastoaineistosta. Lisäksi pareille on liitetty tietoja mahdollisesta avioliitosta ja kuolinpäivämäärät. Tähän aineistoon on hyväksytty ainoastaan ne parit, joiden yhdessä asuminen on kestänyt vähintään 90 päivää. Avopareista kummankin puolison täytyy olla täysi-ikäinen. Kummankin puolison täytyy kuulua väestöön ainakin kerran aineiston vuosien viimeisenä päivänä.

Kokonaisaineistoon voidaan antaa käyttöoikeus vain jos tutkimuksellisesta syystä kokonaisaineiston käyttöön on erityinen tarve. Tiedot on linkitettävissä muiden henkilövalmisaineistomoduulien kanssa suojatun henkilönumeron avulla.

FOLK asuinliitot -aineistot ovat kansiossa FOLK_ASLII_C, jossa tiedostot ovat jaettuina vuositiedostoihin. Tiedostonimet ovat muodossa folk_aslii_"vuosi"_1.

Aikaisemmin julkaistut FOLK asuinliitot -aineistotiedostot, jotka sisältävät useita tilastovuosia ovat FIONAssa seuraavissa kansioissa:
Totaaliaineisto vuosille 2011-2020 : FOLK_aslii_11a
Totaaliaineisto vuosille 2001-2010 : FOLK_aslii_0110a
Totaaliaineisto vuosille 1987-2000 : FOLK_aslii_8800a

Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@stat.fi

## Variables (17)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `vuosi` | Vuosi | — | — | — |
| `hid_e` | Suojattu henkilön yksilöivä tunnus | — | — | — |
| `spuhnro` | Suojattu henkilön yksilöivä tunniste puolisolle | — | — | — |
| `alku` | Tekninen alkupäivämäärä | — | — | — |
| `loppu` | Tekninen loppupäivämäärä | — | — | — |
| `pnro` | Puolison järjestysnumero | — | — | — |
| `jarnro` | Avioliiton järjestysnumero | — | — | — |
| `ymuuttopv` | Yhteenmuuttopäivä | — | — | — |
| `emuuttopv` | Erilleen muuttopäivä | — | — | — |
| `vihkipvm` | Avioliiton solmimispäivä | — | — | — |
| `asumero` | Asumuseropäivä | — | — | — |
| `aeropvm` | Avioeropäivä | — | — | — |
| `kuolpv` | Henkilön kuolinpäivä | — | — | — |
| `pu_kuolpv` | Puolison kuolinpäivä | — | — | — |
| `pu_pnro` | Puolison järjestysnumero (puoliso) | — | — | — |
| `pu_jarnro` | Avioliiton järjestysnumero (puoliso) | — | — | — |
| `laitos` | Vanhuksen laitosasuminen | — | — | — |

### Variable definitions

#### `vuosi` — Vuosi

Tilastovuosi.

#### `hid_e` — Suojattu henkilön yksilöivä tunnus

Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e -tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä.

#### `spuhnro` — Suojattu henkilön yksilöivä tunniste puolisolle

Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e -tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä.

#### `alku` — Tekninen alkupäivämäärä

Alku on yhteenmuuttopäivä, jos päivämäärä on tiedossa. Niillä pareilla, jotka asuivat yhdessä jo 31.12.1986, on alku tämä ko. päivä. Jos yhteenmuuttopäivä puuttuu, niin alku on asuinliiton ensimmäisen vuoden joulukuun 30. päivä.

#### `loppu` — Tekninen loppupäivämäärä

Jos asuinliitto on päättynyt erilleen muuttoon tai kuolemaan, on loppu tämä päivämäärä, mikäli tieto on saatavilla. Jos päättyneestä asuinliitosta ei ole päivämäärä-tietoa, niin loppu on viimeistä asuinliittovuotta seuraavan tammikuun 1. päivä. Jos asuinliitto ei ole päättynyt aineiston viimeisenä tilastovuonna, niin loppu on tämän vuoden viimeinen päivä.

#### `pnro` — Puolison järjestysnumero

Järjestysnumero laskettu vain asuinliittoaineistossa olevista puolisoista.

#### `jarnro` — Avioliiton järjestysnumero

Avioliiton järjestysnumero -tiedot Väestörekisterikeskuksen väestötietojärjestelmästä.

#### `ymuuttopv` — Yhteenmuuttopäivä

Yhteenmuuttopäivä-tiedon lähteenä henkilötilastojen tietovaraston muuttotilastoaineisto.

#### `emuuttopv` — Erilleen muuttopäivä

Erilleen muuttopäivä-tiedon lähteenä henkilötilastojen tietovaraston muuttotilastoaineisto.

#### `vihkipvm` — Avioliiton solmimispäivä

Vihkipäivä-tiedot Väestörekisterikeskuksen väestötietojärjestelmästä. Jos sama pari avioeron jälkeen avioituu uudestaan, niin parilla on aineistossa vain ensimmäiset tiedot vihkipäivästä ja avioeropäivästä.

#### `asumero` — Asumuseropäivä

Asumuseropäivä-tiedot Väestörekisterikeskuksen väestötietojärjestelmästä.

#### `aeropvm` — Avioeropäivä

Avioeropäivä-tiedot Väestörekisterikeskuksen väestötietojärjestelmästä. Kullakin parilla on vain yksi päivämäärätieto, vaikka pari olisi avioitunut ja eronnut useamman kerran.

#### `kuolpv` — Henkilön kuolinpäivä

Kuolinpäivä-tiedot Väestörekisterikeskuksen väestötietojärjestelmästä.

#### `pu_kuolpv` — Puolison kuolinpäivä

Kuolinpäivä-tiedot Väestörekisterikeskuksen väestötietojärjestelmästä.

#### `pu_pnro` — Puolison järjestysnumero (puoliso)

Järjestysnumero laskettu vain asuinliittoaineistossa olevista puolisoista.

#### `pu_jarnro` — Avioliiton järjestysnumero (puoliso)

Avioliiton järjestysnumero -tiedot Väestörekisterikeskuksen väestötietojärjestelmästä.

#### `laitos` — Vanhuksen laitosasuminen

Jos asuinliittoparista jompikumpi puoliso erilleen muuton jälkeen asuu laitoksessa tai huoltolaitosrakennuksessa tulee Vanhuksen laitosasuminen -tiedon arvoksi ’1’. Tieto koskee vain 70 vuotta täyttäneitä.

---

[← Back to catalogue](../../README.md)
