# FOLK_JAKSOT: työttömät

- **Identifier:** `FOLK_19912023_jua_tyott24_001.xml`
- **DOI:** `tyokay_2012-03_2012-03-01_ain_0001`
- **Temporal coverage:** 1991-01-01 - 2024-12-31
- **Published:** 2025-12-22
- **Organisation:** Tilastokeskus
- **Variable count:** 6
- **Observation count:** —
- **Population:** Suomessa vakituisesti asuvat, vuoden viimeisenä päivänä vähintään 15 vuotta täyttäneet henkilöt
- **Source:** Työ- ja elinkeinoministeriön työnhakijarekisteri
- **Keywords:** työttömyys

## Description

Aineisto on osa laajempaa jaksotietoja sisältävää valmisaineistomoduulia, joka sisältää tiedot työsuhde-, työttömyys-, työvoimakoulutus-, sijoitus-, työnhaku- ja eläkejaksoista sekä taustatiedot yrityksen toimipaikasta. Työttömät–osa-aineisto sisältää tietoja työttömyyden alkamis- ja loppumispäivämääristä sekä työttömyyden laadusta ja päättymissyistä vuodesta 1987 alkaen sekä tietoja työttömyysjaksoista vuodesta 1991 alkaen.

<b> Valmisaineiston tarkentava nimi </b> 
Jaksotiedot työsuhde-, työttömyys-, työvoimakoulutus-, sijoitus-, työnhaku- ja eläkejaksoista, sisältäen taustatietoja yrityksen toimipaikasta.  

<b> Aineiston koostaminen, tietolähteet ja perusjoukko </b> 
Aineisto sisältyy FOLK_JAKSOT –moduuliin, ja sen lähdeaineistona toimii Työ- ja elinkeinoministeriön työnhakijarekisteri. Rekisteri sisältää tietoa Suomessa vakituisesti asuvista, vuoden viimeisenä päivänä vähintään 15 vuotta täyttäneet henkilöt, jotka ovat ilmoittautuneet työhakijoiksi. 

<b> Aineiston päivitysaikataulu </b> 
Tutustu valmisaineistojen <a href="https://stat.fi/fi/palvelut/palvelut-tutkijoille/tutkimusaineistot/valmisaineistot/valmisaineistojen-paivitysaikataulu">  päivitysaikatauluun</a>. 

<b> Aineiston käyttö ja tilaaminen </b> 
Aineisto on tarkoitettu käytettäväksi FIONA-etäpalvelun kautta, ja se on linkitettävissä muihin henkilövalmisaineistomoduuleihin suojatun henkilönumeron avulla. Tietoja voi tilata tutkimuksen kohdejoukolle ja tietylle ajanjaksolle.    

Aineiston kokonaisaineiston (kaikki muuttujat koko populaatiolle ja kaikilta saatavissa olevilta vuosilta) käyttöoikeus myönnetään vain, jos tutkimuksellinen tarve sitä erityisesti edellyttää. Aineistosta voi tilata muuttujia voi tilata myös räätälöidyn version, joka sisältää vain osan valmisaineiston muuttujista. 

<b> Lisätietoja </b> 
Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@stat.fi

## Variables (6)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `vuosi` | Vuosi | — | — | — |
| `hid_e` | Suojattu henkilön yksilöivä tunniste | — | — | — |
| `alkupvm` | Työttömyyden alkupäivämäärä | — | — | Työnhakijarekisteri |
| `loppupvm` | Työttömyyden loppupäivämäärä | — | — | Työnhakijarekisteri |
| `psyy` | Työttömyyden päättymissyy | — | tyottomy_3_2012_01_01 | Työnhakijarekisteri |
| `tjtyol` | Työttömyysjakson työllisyyskoodi | — | tyottomy_11_2012_01_01 | Työnhakijarekisteri |

### Variable definitions

#### `vuosi` — Vuosi

Tilastovuosi on se kalenterivuosi, jota tilasto koskee.

#### `hid_e` — Suojattu henkilön yksilöivä tunniste

Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e -tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä

#### `alkupvm` — Työttömyyden alkupäivämäärä

**Group:** Työnhakijarekisteri

Työttömyysjakson alkupäivämäärä.

#### `loppupvm` — Työttömyyden loppupäivämäärä

**Group:** Työnhakijarekisteri

Työttömyysjakson loppupäivämäärä.

#### `psyy` — Työttömyyden päättymissyy

**Classification:** tyottomy_3_2012_01_01 · **Group:** Työnhakijarekisteri

Uusi luokitus tilastovuodesta 2012 alkaen:

00 = Työllistetty (entinen nimi: sijoitettu toimenpitein)
01 = Välitetty työhön yleisille työmarkkinoille
02 = Lomautus tai lyh. työviikko päättynyt
03 = Saanut itse työpaikan
04 = Aloittanut työvoimakoulutuksen
05 = Siirtynyt työvoiman ulkopuolelle (nykyisin merkitään soveltuvin osin syillä 11, 12 ja 13)
06 = Muu syy tai ei tietoa
07 = Siirtynyt työttömyyseläkkeelle
08 = Aloittanut muun koulutuksen
09 = Työhön/työnhakuun EU-/ETA-valtioon
10 = Ei ole uusinut työnhakuaan (tuli ennen korvertoituna ’6’:ksi)
11 = Aloittanut valmennuksen/kokeilun
12 = Aloittanut kuntouttavan työtoiminnan
13 = Aloittanut omaehtoisen opiskelun työttömyysetuudella

Aiemmin: 

0 = Sijoitettu työllistämistoimenpitein
1 = Välitetty työhön yleisille työmarkkinoille
2 = Lomautus tai lyh. työviikko päättynyt
3 = Saanut itse työpaikan
4 = Aloittanut työvoimakoulutuksen
5 = Siirtynyt työvoiman ulkopuolelle
6 = Muu syy tai ei tietoa
7 = Siirtynyt työttömyyseläkkeelle
8 = Aloittanut muun koulutuksen
9 = Siirtynyt työnhakuun ETA-valtioon

#### `tjtyol` — Työttömyysjakson työllisyyskoodi

**Classification:** tyottomy_11_2012_01_01 · **Group:** Työnhakijarekisteri

Työttömyysjakson työllisyyskoodi, työttömien aineistossa mukana vain luokat 2 ja 3. 

2 = työtön 
3 = lomautettu

---

[← Back to catalogue](../../README.md)
