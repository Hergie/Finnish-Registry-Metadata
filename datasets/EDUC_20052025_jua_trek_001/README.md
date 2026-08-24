# EDUC_TREK Tutkintorekisteri

- **Identifier:** `EDUC_20052025_jua_trek_001.xml`
- **DOI:** `he_201100_ain_Tutkinto`
- **Temporal coverage:**  - 2025-12-31
- **Published:** 2026-08-21
- **Organisation:** Tilastokeskus
- **Variable count:** 23
- **Observation count:** —
- **Population:** Tutkinnon suorittanut väestö
- **Source:** Tutkintorekisteri

## Description

EDUC_TREK-valmisaineisto Tutkintorekisteri 1995–2023-vuositiedosto sisältää tutkintorekisterin tietoja muun muassa tutkinnoista, koulutuksesta, oppilaitostyypistä sekä koulutusmuodosta ja -lajista myös ajalta ennen tutkimusrekisterin perustamisvuotta (1971).

<b>Valmisaineiston tarkentava nimi</b>
Tiedot kaikista tutkintorekisterissä saatavilla olevista tutkinnoista riippumatta siitä, kuuluuko henkilö väestöön kyseisenä vuonna (EDUC_TREK)

<b>Aineiston koostaminen, tietolähteet ja perusjoukko</b> 
Aineisto sisältää Tilastokeskuksen tutkintorekisterin tutkintotietoja. Tutkintorekisteriin on viety vain henkilöt, joille löytyy henkilötunnus. Mukana ovat kaikki tutkintorekisterin tutkinnot riippumatta siitä, kuuluuko henkilö kyseisenä vuonna maassa asuvassa väestöön.  
Yksittäisen vuositiedoston <b>vuosi</b>-muuttuja viittaa tutkintorekisterin rekisterivuoteen. Tämän vuoksi ajan myötä mahdollisesti muuttuvat muuttujat, kuten tutkintokoodien luokitukset tai oppilaitostunnukset, kuvaavat sen hetkistä tilannetta. Rekisterin tietoja täydennetään ja korjataan takautuvasti, joten viimeisin rekisterivuosi tarjoaa ajantasaisimman tiedon.

<b>Huomioitavaa aineistosta ja sen käytöstä</b> 
EDUC_TREK-valmisaineisto kattaa tiedot suoritetuista tutkinnoista aina 1900-luvun alkupuolelta lähtien. Yksittäinen vuositiedosto sisältää kaikki tutkintorekisteriin rekisterivuoden (<b>vuosi</b>-muuttuja) loppuun mennessä tallentuneet tutkinnot myös aiemmin suoritettujen tutkintojen (<b>saika</b><<b>vuosi</b>) osalta.  
Kaikille ennen tutkintorekisterin perustamisvuotta (1971) suoritetuille tutkinnoille ei ole tiedossa tutkinnon suoritusaikaa (<b>saika</b>).

<b>Aineiston päivitysaikataulu</b>
Tutustu valmisaineistojen <a href="https://stat.fi/tup/tutkijapalvelut/valmisaineistojen-paivitysaikataulu.html" > päivitysaikatauluun</a>. 
Tutkintorekisteri valmistuu kunkin tilastovuoden osalta seuraavan vuoden syksyllä (loka-marraskuu). Tietojen valmistumisaika on tilastovuosi + 12 kk. 

<b>Aineiston käyttö ja tilaaminen</b> 
Aineisto on tarkoitettu käytettäväksi FIONA-etäpalvelun kautta, ja se on linkitettävissä muihin henkilövalmisaineistoihin suojatun henkilönumeron avulla.  

Valmisaineiston voi tilata tutkimuksen kohdejoukolle ja tarvittavalta ajanjaksolta. Kokonaisaineiston (kaikki muuttujat koko populaatiosta ja kaikilta saatavilla olevilta vuosilta) käyttöoikeus myönnetään vain, jos tutkimuksellinen tarve sitä erityisesti edellyttää. Lisäksi aineistosta voi tilata räätälöidyn version, joka sisältää vain osan muuttujista.  
Aineisto on FIONA-etäkäyttöjärjestelmässä jaettuina vuosikansioihin tilastovuosittain (=tutkintorekisterin rekisterivuosi). 

<b>Muutokset</b> 
Vuoden 2023 päivitys: 
- Aineistoon lisätty takautuvasti kaksi uutta muuttujaa alkaen vuodesta 2020: <b>ammoppsop</b> (tutkinnossa oppisopimusjaksoja) sekä <b>ammkouso</b> (tutkinnossa koulutussopimusjaksoja). 

<b>Lisätietoja</b> 
Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@stat.fi

## Variables (23)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `vuosi` | Tilastovuosi tutkintorekisterissä | — | — | — |
| `jarno` | Tutkinnon järjestysnumero tietokannassa | — | — | — |
| `hid_e` | Suojattu henkilön yksilöivä tunniste. | — | — | — |
| `oltunn_s` | Suojattu oppilaitostunnus | — | — | — |
| `akk_s` | Väliaikaisen ammattikorkeakoulun tunnus salattuna | — | — | — |
| `oprior` | Prioriteetti | — | — | — |
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
| `tutklaja` | Koulutuslaji | — | — | — |
| `kirtuv` | Aloittamisvuosi/kirjoihintulovuosi | — | — | — |
| `kirtulk` | Aloittamislukukausi | — | — | — |
| `sijkun` | Koulutuksen sijaintikunta | — | — | — |
| `suormaa` | Tutkinnon suoritusmaa | — | — | — |
| `ammoppsop` | Tutkinnossa oppisopimusjaksoja | — | — | — |
| `ammkouso` | Tutkinnossa koulutussopimusjaksoja | — | — | — |

### Variable definitions

#### `vuosi` — Tilastovuosi tutkintorekisterissä

#### `jarno` — Tutkinnon järjestysnumero tietokannassa

Koska henkilöllä voi olla useampia tutkintoja samana vuonna, ne erotetaan järjestysnumerolla, joka on osa taulun avainta

#### `hid_e` — Suojattu henkilön yksilöivä tunniste.

Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa
henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e-tunnus mahdollistaa henkilöä koskevien
tietojen yhdistämisen eri vuosien ja aineistojen välillä.

#### `oltunn_s` — Suojattu oppilaitostunnus

Oppilaitostunnus tilastovuonna

#### `akk_s` — Väliaikaisen ammattikorkeakoulun tunnus salattuna

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
