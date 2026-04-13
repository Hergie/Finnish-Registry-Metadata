# FIRM_GROUP Konsernit

- **Identifier:** `FIRM_20082020_jua_GROUP_001.xml`
- **DOI:** `work_2013-04_2013-04-05_ain_0001`
- **Temporal coverage:** 1995-01-01 - 2024-12-31
- **Published:** 2025-03-07
- **Organisation:** Tilastokeskus
- **Variable count:** 23
- **Observation count:** —
- **Population:** Konsernit ja niihin kuuluvat yritykset (emo, tytär, osakkuusyritys tai muu)
- **Source:** Konsernirekisteri, konsernitiedot saadaan Patentti- ja rekisterihallitukselle toimitetuista yritysten tilinpäätöksistä. Tietoja täydennetään lisäksi Eurostatin konsernirekisteristä (EGR) sekä yritysten kotisivuilta.
- **Related:** <a href= "http://www.tilastokeskus.fi/meta/kas/konsernirekist.html">Konsernirekisteri</a> <a href= "http://www.stat.fi/meta/rekisteriselosteet/tutka_rekisteriseloste_konsernit.html">Konsernit</a>
- **Keywords:** konsernit

## Kuvaus / Description

Konsernirekisterin tiedoista on muodostettu tutkimuskäyttöön kaksi yhtenäistä aikasarjaa vuosille 1995, 1997 - 2007 ja 2008 - . Aineisto sisältää konsernitason tietoja konsernin rakenteesta (emo-, tytär-, yhteis- ja osakkuusyritykset), henkilöstön määrästä, liikevaihdosta ja kansallisuudesta. Liikevaihdon osalta tietoja on karkeistettu.
Konsernirekisterin ylläpitäminen on aloitettu vuonna 1995. Kattavuus on rekisterin alkuvuosina heikko. Kattavuus paranee ajan myötä rekisterin tietolähteiden ja päivitysprosessien kehittymisen ansiosta. Nykyinen rekisterin tietojärjestelmä on ollut käytössä vuodesta 2008 alkaen. Vuodesta 2008 eteenpäin rekisterin laatu on aiempia vuosia parempi ja tiedot vuosien välillä ovat vertailukelpoisia. Aineisto päivitetään vuosittain uudestaan kaikille vuosille alkaen vuodesta 2008. Tällöin aiempien vuosien (2008-) tiedot saattavat päivittyä takautuvasti. 
PRH:n tilinpäätöksistä saadaan konserniin kuuluvat tytäryhtiöt (äänivalta>50) ja osakkuusyhtiöt (äänivalta<=50), tytäryhtiöiden nimet ja maat. Lisäksi saadaan konsernin perimmäinen omistaja (ns. GGH) ja suoraan omistava emoyritys (tai väliemo), omistusosuudet ja äänivalta. 
Konsernin rakenne voi muuttua tilastovuoden sisällä. Valitsemalla tilastovuoden viimeisin voimassa oleva Konserni-yrityssuhteen ominaisuuden alkupäivä (alkupvm), saa yksilöivät rivit tilastovuosittain.

Lisätietoja tutkijapalveluista: tutkijapalvelut@tilastokeskus.fi.

## Muuttujat / Variables (23)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `knstun_s` | Suojattu konsernitunnus | — | — | — |
| `yrtun_s` | Suojattu konserniyrityksen tunnus | — | — | — |
| `vuosi` | Vuosi | — | — | — |
| `jasenlaji` | Yrityksen asema pääkonsernissa | — | — | — |
| `tyyppi` | Konsernin tyyppi | — | — | — |
| `maa` | Konsernin kansallisuus | — | — | — |
| `maa_vuositieto` | Konsernin kansallisuus viitevuonna | — | — | — |
| `tol2008` | Konsernin laskennallinen päätoimiala TOL2008 | — | toimiala_1_2008_01_01 | — |
| `knslaji` | Eurostatin määrittelemä konsernilaji | — | — | — |
| `henkilosto` | Konsernihenkilöstön määrä | — | — | — |
| `kotim_henkilosto` | Konsernin kotimainen henkilöstö | — | — | — |
| `liikevaihto_sl` | Konsernin konsolidoitu liikevaihto suuruusluokittain | — | — | — |
| `ulkom_henkilosto` | Konsernin ulkomainen henkilöstö | — | — | — |
| `ulkom_liikevaihto_sl` | Konsernin ulkomainen liikevaihto suuruusluokittain | — | — | — |
| `ulkom_liikevaihto_kasvu` | Konsernin ulkomaisen liikevaihdon kasvuprosentti | % | — | — |
| `alo_muoto` | Konsernin aloitusmuoto | — | — | — |
| `lop_muoto` | Konsernin lopetusmuoto | — | — | — |
| `laji` | Kotimainen rekisteriyritys=1 | — | — | — |
| `alkupvm` | Konserni-yrityssuhteen ominaisuuden alkupäivä | — | — | — |
| `loppupvm` | Konserni-yrityssuhteen ominaisuuden loppupäivä | — | — | — |
| `omistus` | Konsernin omistusosuus tytär-, osakkuus- ja muissa yrityksissä | — | — | — |
| `aanivalta` | Konsernin äänivaltaosuus tytär-, osakkuus- ja muissa yrityksissä | — | — | — |
| `kontrolli` | Konsernin määräysvalta yritykseen | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `knstun_s` — Suojattu konsernitunnus

Suojattu konsernitunnus. Konsernitunnus voidaan antaa kaikille Suomessa rekisteröidyille pääkonserneille.

#### `yrtun_s` — Suojattu konserniyrityksen tunnus

Suojattu konserniyrityksen tunnus. Emo-, tytär-, osakkuus- ja muiden yhtiöiden y-tunnus.

#### `vuosi` — Vuosi

Vuosi

#### `jasenlaji` — Yrityksen asema pääkonsernissa

Konserniyrityksen jäsenlaji, joka kertoo yrityksen aseman konsernissa.
Jäsenlajeja ovat:
0	Ei tiedossa 
1	Emoyritys; suomalainen viimekäden emo
2	Tytäryritys; viimekäden tytär
3	Yhteisyritys
4	Osakkuusyritys
5	Intressiyritys 
6	Väliemo; tytäryritys, jolla on myös itsellään tyttäriä
Lähde: Yritysten tilinpäätökset

#### `tyyppi` — Konsernin tyyppi

Konsernin tyyppi. Vuosilta 1995-2007 mukana vain yrityskonsernit, mahdolliset arvot ovat:
(0	Ei tiedossa)
1	Yrityskonserni
(2	Kuntakonserni) 
3	Yksittäinen ulkomaalaisen konsernin kotimainen tytäryritys (nk. OTY5-konserni)

Konsernin tyyppi. Vuodesta 2008 lähtien mukana kaikki konsernityypit, mahdolliset arvot ovat:
0                           Ei tiedossa
1                           Yrityskonserni                                                                                      
2                           Kuntakonserni                                                                                       
3                           Yksittäinen ulkomaalaisen konsernin kotimainen tytäryritys (nk. OTY5-konserni)                      
4                           Kuntayhtymä
5                           Valtiokonserni
6                           Kunta-alakonserni

#### `maa` — Konsernin kansallisuus

Konsernin kansallisuus. Jos konsernilla ei ole voimassa olevaa suhdetta ulkomaiseen emoyritykseen, määräytyy kansallisuudeksi 'Suomi'.

#### `maa_vuositieto` — Konsernin kansallisuus viitevuonna

Konsernin kansallisuus viitevuonna. Jos konsernilla ei ole voimassa olevaa suhdetta ulkomaiseen emoyritykseen, määräytyy kansallisuudeksi 'Suomi'.

#### `tol2008` — Konsernin laskennallinen päätoimiala TOL2008

**Luokitus / Classification:** toimiala_1_2008_01_01

Konsernin laskennallinen päätoimiala (TOL2008) tilastovuonna. Saatavilla 2007-.

#### `knslaji` — Eurostatin määrittelemä konsernilaji

Eurostatin määrittelemä konsernilaji (EG TYPE)

0	Ei tiedossa
1	Täysin kotimainen konserni (All resident group)
2	Kotimaisessa kontrollissa oleva monikansallinen konserni (Domestically controlled group) 
3	Ulkomaalaisessa kontrollissa oleva monikansallinen konserni (Foreign controlled group)

#### `henkilosto` — Konsernihenkilöstön määrä

Konsernihenkilöstö. Henkilöstön määrä tilastovuoden tilikautena keskimäärin.

#### `kotim_henkilosto` — Konsernin kotimainen henkilöstö

Konsernin kotimainen henkilöstö. Henkilöstön määrä Suomessa tilastovuoden tilikautena keskimäärin.

#### `liikevaihto_sl` — Konsernin konsolidoitu liikevaihto suuruusluokittain

Konsernin konsolidoitu liikevaihto tilastovuonna suuruusluokittain:
0     liikevaihto=0
1     1<=liikevaihto<200000
2     200000<=liikevaihto<400000 
3     400000<=liikevaihto<1000000 
4     1000000<=liikevaihto<2000000 
5     2000000<=liikevaihto<10000000 
6     10000000<=liikevaihto<20000000 
7     20000000<=liikevaihto<50000000 
8     50000000<=liikevaihto<100000000 
9     100000000<=liikevaihto<250000000 
10    250000000<=liikevaihto<500000000 
11    liikevaihto>=500000000
''       liikevaihto on tyhjä tai negatiivinen

#### `ulkom_henkilosto` — Konsernin ulkomainen henkilöstö

Konsernin ulkomainen henkilöstö. Henkilöstön määrä tilastovuoden tilikautena keskimäärin.

#### `ulkom_liikevaihto_sl` — Konsernin ulkomainen liikevaihto suuruusluokittain

Konsernin ulkomainen liikevaihto tilastovuonna suuruusluokittain:
0     liikevaihto=0
1     1<=liikevaihto<200000
2     200000<=liikevaihto<400000 
3     400000<=liikevaihto<1000000 
4     1000000<=liikevaihto<2000000 
5     2000000<=liikevaihto<10000000 
6     10000000<=liikevaihto<20000000 
7     20000000<=liikevaihto<50000000 
8     50000000<=liikevaihto<100000000 
9     100000000<=liikevaihto<250000000 
10    250000000<=liikevaihto<500000000 
11    liikevaihto>=500000000
''       liikevaihto on tyhjä tai negatiivinen

#### `ulkom_liikevaihto_kasvu` — Konsernin ulkomaisen liikevaihdon kasvuprosentti

**Yksikkö / Unit:** %

Konsernin ulkomaisen liikevaihdon kasvuprosentti verrattuna edelliseen tilastovuoteen.

#### `alo_muoto` — Konsernin aloitusmuoto

Konsernin aloitusmuoto. Aloitusmuotoja ovat:

0	Ei tiedossa
1	Yhtiöittäminen tai tytäryrityksen perustaminen
2	Konsernifuusio
3	Yritysosto
9	Muu

#### `lop_muoto` — Konsernin lopetusmuoto

Konsernin lopetusmuoto. Lopetusmuotoja ovat:

0	Toiminnassa
1	Konsernin lakkaaminen
2	Konsernifuusio
3	Tytäryritysten myynti
4	Tytäryritysten lakkaaminen tai sulautuminen
5	Emoyrityksen osto
6	Siirtynyt pois kohdejoukosta
9	Muu

#### `laji` — Kotimainen rekisteriyritys=1

Aineistossa mukana vain kotimaiset rekisteriyritykset, saa arvon 1 aina.

#### `alkupvm` — Konserni-yrityssuhteen ominaisuuden alkupäivä

Konserni-yrityssuhteen ominaisuuden (omistusosuus, äänivalta, jäsenlaji) alkupäivä. Jos suhteen alkupäivämäärää ei tiedetä, käytetään tilikauden ensimmäistä päivää tai tilikaudella perustetun yrityksen aloituspäivää.

#### `loppupvm` — Konserni-yrityssuhteen ominaisuuden loppupäivä

Konserni-yrityssuhteen ominaisuuden (omistusosuus, äänivalta, jäsenlaji) loppupäivä. Jos suhteen loppupäivämäärää ei tiedetä, käytetään tilikauden viimeistä päivää tai mahdollisesti tilikaudella lopettaneen yrityksen lopetuspäivää, joka saadaan yritysrekisteristä.

#### `omistus` — Konsernin omistusosuus tytär-, osakkuus- ja muissa yrityksissä

Konsernin omistusosuus tytär-, osakkuus- ja muissa yrityksissä tai konsernin ulkomaisen emon (suora tai viimekäden emo) omistusosuus konsernin kotimaisesta emosta. Alkaen vuodesta 2008.

#### `aanivalta` — Konsernin äänivaltaosuus tytär-, osakkuus- ja muissa yrityksissä

Konsernin äänivaltaosuus tytär-, osakkuus- ja muissa yrityksissä tai konsernin ulkomaisen emon (suora tai viimekäden emo) äänivaltaosuus konsernin kotimaisesta emosta. Äänivaltaosuus on useimmiten sama kuin osakkeiden ja osuuksien suora omistusosuus.  Alkaen vuodesta 2008.

#### `kontrolli` — Konsernin määräysvalta yritykseen

Konsernin määräysvalta yritykseen. Alkaen vuodesta 2008. Muuttuja kertoo onko knstun-tiedon määrittelemällä konsernilla määräysvalta yrtun-tiedon määrittelemään tytäryritykseen:
0	Ei
1	Kyllä

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
