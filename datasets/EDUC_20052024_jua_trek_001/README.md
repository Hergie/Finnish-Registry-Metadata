# EDUC_TREK Tutkintorekisteri 2005–2024

- **Identifier:** `EDUC_20052024_jua_trek_001.xml`
- **DOI:** `he_201100_ain_Tutkinto`
- **Temporal coverage:** 2005-01-01 - 2024-12-31
- **Published:** 2026-01-07
- **Organisation:** Tilastokeskus
- **Variable count:** 23
- **Observation count:** —
- **Population:** Tutkinnon suorittanut väestö

## Description

Taulu sisältää tutkintorekisterin tutkintotiedot. Mukana kaikki tutkintorekisterin tutkinnot riippumatta siitä onko henkilö masssa asuvassa väestössä ko. vuonna. Tiedoston vuosi kertoo tutkintorekisterin rekisterivuoden, ja näin yli ajan mahdollisesti muuttuvat muuttujat  (tutkintokoodin luokitus, oppilaitostunnus) kuvaavat sen hetkistä tilannetta. Rekisterin tietoja täydennetään/korjataan takautuvasti, ja näin rekisterin viimeisin rekisterivuosi kertoo ajantasaisimman tiedon.

Tutkintorekisteri-moduuli koostuu erillisistä vuositiedostoista educ_trek_VVVV, jossa VVVV = 2005,...->

Muuta:
- Huomaathan, että muuttujissa on eroja siinä, että koska ne ovat ajallisesti saatavilla. Esimerkiksi tutkinnon suoritusaika on puuttuva usealle ennen tutkintorekisterin perustamisvuotta (1971).
- Moduulin historian täydentäminen ennen 2005 rekisterivuotta olisi mahdollista Tilastokeskuksen kokoomatietojen avulla. Tämä vaati kuitenkin resursseja.
- Tutkintorekisteriin on viety vain henkilöt, joille löytyy henkilötunnus. 
- Tutkintorekisteri valmistuu kunkin tilastovuoden osalta seuraavan vuoden syksyllä (loka-marraskuu). Tietojen valmistumisaika on tilastovuosi + 12 kk.

Muutokset v.2023 päivityksessä:

- Aineistoihin lisätty takautuvasti vuodesta 2020 alkaen kaksi uutta muuttujaa:

ammoppsop= tutkinnossa oppisopimusjaksoja
ammkouso= tutkinnossa koulutussopimusjaksoja

## Variables (23)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `vuosi` | Tilastovuosi tutkintorekisterissä | — | — | — |
| `shnro` | Suojattu henkilönumero | — | — | — |
| `jarno` | Tutkinnon järjestysnumero tietokannassa | — | — | — |
| `oprior` | Prioriteetti | — | — | — |
| `oltunn_s` | Suojattu oppilaitostunnus | — | — | — |
| `koulk` | Koulutuskoodi | — | — | — |
| `lisak` | Opettajankelpoisuus tutkinnossa | — | — | — |
| `saika` | Tutkinnon suoritusaika | — | — | — |
| `opkelp` | Opettajankelpoisuus | — | — | — |
| `opkieli` | Opetuskieli | — | — | — |
| `opty` | Oppilaitostyyppi | — | — | — |
| `kouljat` | Koulutusmuoto | — | — | — |
| `yotutk` | Ylioppilastutkinto | — | — | — |
| `ulkom` | Tutkinto suoritettu ulkomailla | — | — | — |
| `oppiso` | Oppisopimuskoulutus | — | — | — |
| `sakk` | Väiaikaisen ammattikorkeakoulun tunnus salattuna | — | — | — |
| `tutklaja` | Koulutuslaji | — | — | — |
| `kirtuv` | Aloittamisvuosi/kirjoihintulovuosi | — | — | — |
| `kirtulk` | Aloittamislukukausi | — | — | — |
| `sijkun` | Koulutuksen sijaintikunta | — | — | — |
| `suormaa` | Tutkinnon suoritusmaa | — | — | — |
| `ammoppsop` | Tutkinnossa oppisopimusjaksoja | — | — | — |
| `ammkouso` | Tutkinnossa koulutussopimusjaksoja | — | — | — |

### Variable definitions

#### `vuosi` — Tilastovuosi tutkintorekisterissä

#### `shnro` — Suojattu henkilönumero

Henkilötunnuksen korvaava suojattu Tilastokeskuksen henkilönumero

#### `jarno` — Tutkinnon järjestysnumero tietokannassa

Koska henkilöllä voi olla useampia tutkintoja samana vuonna, ne erotetaan järjestysnumerolla, joka on osa taulun avainta

#### `oprior` — Prioriteetti

Henkilön tutkintotietueiden prioriteettijärjestys, koodit:
0 = maassa asuvan muut tutkinnot
1 = maassa asuvan korkein ammatillinen tutkinto
2 = maasta muuttaneen muut tutkinnot
3 = maasta muuttaneen korkein ammatillinen tutkinto
HT-virheelliset sisältyvät tähän luokkaan v. 2006 alkaen
4 = kuolleen muut tutkinnot (v. 1987 alkaen) 
5 = kuolleen korkein ammatillinen tutkinto (v.1987 alkaen)
9 = prioriteettia ei voida määritellä
Maasta muuttaneet ja kuolleet saadaan vuosittain Väestörekisterikeskuksen väestötilastojen laadintaa varten toimittamista väestönmuutostiedoista.

#### `oltunn_s` — Suojattu oppilaitostunnus

Oppilaitostunnus tilastovuonna

#### `koulk` — Koulutuskoodi

TK:n koulutusluokituksen 6-numeroinen koulutuskoodi.
Tieto kullakin vuodella ko. vuoden koulutusluokituksen mukainen

#### `lisak` — Opettajankelpoisuus tutkinnossa

Tutkintoon liittyvä opettajankelpoisuus v. 1998 alkaen
1 = opettajankelpoisuus
0 = ei opettajankelpoisuutta

#### `saika` — Tutkinnon suoritusaika

Tutkinnon suoritusvuosi ja -kuukausi v. 1971 alkaen
muodossa VVVVKK

#### `opkelp` — Opettajankelpoisuus

Henkilöön liittyvä opettajankelpoisuus v. 1998 alkaen
Erilliset opettajan pedagogiset opinnot = auskultointi 
1 = erilliset opettajan pedagogiset opinnot (vain yliopisto)
2 = aineenopettaja (vain AMK)
3 = erityisopettaja (vain AMK)
4 = opinto-ohjaaja (vain AMK)
5 = Henkilöön liittyvä muu opettajankelpoisuus
0 = Ei opettajankelpoisuutta

#### `opkieli` — Opetuskieli

Koulutuksen opetuskieli 
2-kirjaiminen tunnus
(ISO 639-standardi)
BB = tieto puuttuu
Tieto on vain yo-tutkinnoilla, ammatillisissa oppilaitoksissa suoritetuilla tutkinnoilla sekä ammattikorkeakoulututkinnoilla. Tieto on v. 1971 alkaen.

#### `opty` — Oppilaitostyyppi

Oppilaitostyyppi vuonna 2014
11 = Peruskoulut
12 = Peruskouluasteen erityiskoulut
15 = Lukiot
19 = Perus- ja lukioasteen koulut
21 = Ammatilliset oppilaitokset
22 = Ammatilliset erityisoppilaitokset
23 = Ammatilliset erikoisoppilaitokset
24 = Ammatilliset aikuiskoulutuskeskukset
28 = Palo-, poliisi- ja vartiointialojen oppilaitokset
29 = Sotilasalan ammatilliset oppilaitokset
41 = Ammattikorkeakoulut
42 = Yliopistot
43 = Sotilaskorkeakoulut
61 = Musiikkioppilaitokset
62 = Liikunnan koulutuskeskukset
63 = Kansanopistot
64 = Kansalaisopistot
65 = Opintokeskukset
66 = Kesäyliopistot
99 = Muut oppilaitokset
XX = muu kuin koululaitoksen oppilaitos (osa oppisopimus-
koulutuksesta ja näyttötutkinnoista)
BB = tuntematon
(osa oppisopimuskoulutuksen tutkinnoista, osa näyttötutkinnoista,
ennen v. 1971 suoritetut tutkinnot, ulkomailla suoritetut tutkinnot)

#### `kouljat` — Koulutusmuoto

Koulutusmuoto v.1971 alkaen
Muuttujan luokittelua muutettu v. 2005 alkaen
1 = koulujärjestelmäkoulutus (=muut kuin arvot 2?9) sisältää myös sotilasalan tutkinnot ja ulkomailla suoritetut tutkinnot
Tutkintotavoitteinen aikuiskoulutus
8 = näyttötutkinnot (ammatillinen aikuiskoulutus); ammatilliset perustutkinnot, ammatti- ja erikoisammattitutkinnot v.1994 alkaen
3 = muut kuin näyttötutkinnot;
      ammatilliset aikuiskoulutukset v. 1999 asti
      lukiokoulutuksen aikuiskoulutukset v. 1985 alkaen  
      ammattikorkeakoulun aikuiskoulutukset v.1994 alkaen
      ylemmät ammattikorkeakoulututkinnot v. 2003 alkaen
Muu koulutus
2 = työllisyyskurssikoulutus v. 1990 asti
9 = aikuiskoulutuksen jatkolinja v. 1990 asti
Tieto on kaikilla tutkinnoilla.

#### `yotutk` — Ylioppilastutkinto

Pohjakoulutuksena ylioppilastutkinto
4 = henkilö on suorittanut pohjakoulutuksena yo-tutkinnon
0 = henkilö ei ole suorittanut pohjakoulutuksena yo-tutkintoa tai yo-tutkinnosta ei ole tietoa

#### `ulkom` — Tutkinto suoritettu ulkomailla

1 = tutkinto on suoritettu ulkomailla
0 = tutkinto on suoritettu Suomessa

#### `oppiso` — Oppisopimuskoulutus

Tieto on ammatillisissa oppilaitoksissa suoritetuilla ja
näyttötutkinnoilla vuodesta 1997 lähtien.
1 = tutkinto on suoritettu oppisopimuskoulutuksena
0 = tutkintoa ei ole suoritettu oppisopimuskoulutuksena

#### `sakk` — Väiaikaisen ammattikorkeakoulun tunnus salattuna

Väliaikaisen ammattikorkeakoulun 2-merkkinen koodi SALATTU
01 = Haaga instituutin väliaikainen amk
02 = Vantaan väliaikainen amk 
03 = Turun väliaikainen amk
04 = Satakunnan väliaikainen amk
05 = Hämeen väliaikainen amk
06 = Lahden väliaikainen amk
07 = Tampereen väliaikainen teknillinen amk
08 = Kymenlaakson väliaikainen amk
09 = Etelä-Karjalan väliaikainen amk
10 = Mikkelin väliaikainen amk
11 = Pohjois-Karjalan väliaikainen amk
12 = Pohjois-Savon väliaikainen amk
13 = Jyväskylän väliaikainen amk
14 = Svenska temporära yhs
15 = Seinäjoen väliaikainen amk
16 = Keski-Pohjanmaan väliaikainen amk
17 = Kajaanin väliaikainen amk
18 = Oulun väliaikainen amk
19 = Kemi-Tornion väliaikainen amk
20 = Espoon-Vantaan väliaikainen teknillinen amk
21 = Helsingin väliaikainen tal. ja hal. amk
22 = Yrittäjien väliaikainen amk
23 = Väliaikainen diakonia-amk
24 = Helsingin väliaikainen amk
25 = Temporära yhs Sydväst
26 = Rovaniemen väliaikainen amk 
(tutkintoja vain vakinaisesta amk:sta)
27 = Vaasan väliaikainen amk
28 = Nylands temporära svenska yhs
29 = Espoon-Vantaan väliaikainen amk
30 = Pirkanmaan väliaikainen amk
31 = Östra Nylands temporära yhs
32 = Väliaikainen humanistinen amk
33 = Varsinais-Suomen väliaikainen amk
(tutkintoja vain vakinaisesta amk:sta)
40 = Ålands yrkeshögskola
BB = ei väliaikainen ammattikorkeakoulu

#### `tutklaja` — Koulutuslaji

Ammatillisen koulutuksen tutkintolaji v. 1994 alkaen 
Muuttujan luokittelua muutettu v. 2005 alkaen
1 = ammatillinen peruskoulutus; 
      toinen aste, opistoaste, ammatillinen korkea-aste,
      (opmast = 32, 50, 61)
      sisältää myös sotilasalan ja ulkomailla suoritetut
      ammatilliset tutkinnot (kouljat=1,3,8) 
2 = ammatillinen lisäkoulutus, ammattitutkinto v. 1994 
      alkaen (kouljat=8) 
3 = ammatillinen lisäkoulutus, erikoisammattitutkinto 
      v. 1994 alkaen (kouljat=8) 
9 = muu kuin ammatillinen koulutus; 
      ylioppilas-, ammattikorkeakoulu- ja yliopistotutkinnot,
      sisältää myös sotilasalan ja ulkomailla suoritetut
      korkeakoulu- ja yliopistotutkinnot (kouljat=1,8)
      työllisyyskurssikoulutukset (kouljat=2) 
      aikuiskoulutuksen jatkolinjat (kouljat=9)
Tieto on kaikilla tutkinnoilla.

#### `kirtuv` — Aloittamisvuosi/kirjoihintulovuosi

Vuosi, jolloin opiskelija on ottanut vastaan opiskelu-
oikeuden  ja ilmoittautunut koulun kirjoihin tai solminut
oppisopimuksen muodossa VVVV.
BBBB = ei tietoa
Tieto on vuodesta 2000 alkaen.

#### `kirtulk` — Aloittamislukukausi

Tutkintooon johtavan koulutuksen aloittamislukukausi oppilaitoksessa
1 = kevät (1.1.-31.7.)
2 = syksy (1.8.-31.12.)
B = ei tietoa
Tieto on vuodesta 2000 alkaen.

#### `sijkun` — Koulutuksen sijaintikunta

Koulutuksen sijaintikunta tutkinnon suorittamisvuonna
Väestörekisterikeskuksen kuntakoodina v.1971 alkaen
V. 2006 alkaen ylioppilastutkinnoilla on oppilaitoksen 
sijaintikunta eikä koulutuksen sijaintikunta.
200 = ulkomailla
BBB = tuntematon (999)

#### `suormaa` — Tutkinnon suoritusmaa

Tutkinnon suoritusmaa
YK:n 3-numeroinen tunnus (ISO 3166-standardi)
200 = ent. Tsekkoslovakia
278 = ent. Itä-Saksa
810 = ent. Neuvostoliitto
890 = ent. Jugoslavia
999 = tuntematon 
Ensimmäisen kerran käytössä vuoden 2005 tutkintorekisterissä.

#### `ammoppsop` — Tutkinnossa oppisopimusjaksoja

Muuttujan avulla saa tiedon onko suoritettuun tutkintoon kuulunut oppisopimusjaksoja. Tieto on vuoden 2020 rekisterissä ja saatavilla koskien suoritusvuosia 2019 ja 2020. 1=tutkintoon kuului em. jaksoja, 2=tutkintoon ei kuulunut em. jaksoja.

#### `ammkouso` — Tutkinnossa koulutussopimusjaksoja

Muuttujien avulla saa tiedon onko suoritettuun tutkintoon kuulunut koulutussopimusjaksoja. Tieto on vuoden 2020 rekisterissä ja saatavilla koskien suoritusvuosia 2019 ja 2020. 1=tutkintoon kuului em. jaksoja, 2=tutkintoon ei kuulunut em. jaksoja.

---

[← Back to catalogue](../../README.md)
