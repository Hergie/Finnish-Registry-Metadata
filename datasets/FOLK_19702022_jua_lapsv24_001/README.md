# FOLK_LAPS Lapsi-vanhempi- vuosi

- **Identifier:** `FOLK_19702022_jua_lapsv24_001.xml`
- **DOI:** `work_2020-01_2020-01-17_ain_0001`
- **Temporal coverage:** 1970-01-01 - 2023-12-31
- **Published:** 2026-04-21
- **Organisation:** Tilastokeskus
- **Variable count:** 15
- **Observation count:** —
- **Population:** Kunkin vuoden viimeisenä päivänä Suomessa vakituisesti asunut alle 18-vuotias väestö
- **Source:** VTJ, Väestölaskennat, väestörakenne-, asuntokunta ja perhetilastot.

## Description

FOLK_LAPS-valmisaineisto sisältää tietoja perheväestöön kuuluvista lapsista, biologisista ja adoptio- sekä sosiaalisista vanhemmista, ja heidän asumistiedoistaan. 

Tämä aineistokuvaus koskee ”lapsi-vanhemmat-vuosi” -osiota/taulua, joka sisältää tietoja lapsen syntymävuodesta sekä vanhempien, adoptiovanhempien ja sosiaalisten vanhempien suojatut henkilötunnisteista. Aineistossa on lisäksi tietoja asumisstatuksesta, sekä vuosittaiset perhe- ja asuntokuntatunnukset. 

<b> Valmisaineiston tarkentava nimi </b>
Tiedot perheväestöön kuuluvista lapsista, biologisista ja adoptio- sekä sosiaalisista vanhemmista, ja heidän asumistiedoistaan (FOLK_LAPS).

<b> Aineiston koostaminen, tietolähteet ja perusjoukko</b>
FOLK_LAPS-valmisaineisto pohjautuu Tilastokeskuksen väestölaskenta-, väestörakenne-, asuntokunta- sekä perhetilastojen tietoihin. Tietojen lähteenä on mm. Digi- ja viestintäviraston väestötietojärjestelmä (VTJ). Aineisto sisältää vuosittaiset tiedot lapsista, jotka ovat olleet alle 18-vuotiaita ja asuneet vakituisesti Suomessa kunkin vuoden viimeisenä päivänä. Mukana ovat tiedot lapsen biologisista, adoptiovanhemmista sekä sosiaalisista vanhemmista.

Aineistossa ovat mukana vain perheväestöön kuuluvat lapset, joiden perheasema ei ole puuttuva tai tuntematon tilastovuonna. Sosiaaliseksi vanhemmaksi katsotaan samassa perheessä asuva biologisen vanhemman avo- tai aviopuoliso, kun lapsen perheasema on "lapsi" eikä hän ole ottolapsi. Näitä tietoja on saatavilla lapsi-asemassa oleville, jotka ovat syntyneet vuoden 1952 jälkeen ja joille kyseiset tiedot vanhemmista löytyvät. 

Aineistossa on tieto siitä, asuuko biologinen ja/tai adoptiovanhempi lapsen kanssa saman talouden piirissä vuoden viimeisenä päivänä. Adoptiovanhempien tiedot sisältyvät aineistoon kaikilta vuosilta riippumatta siitä, onko adoptiosuhde kyseisenä vuonna voimassa.

Tietoja on saatavilla väestölaskentavuosilta 1970, 1975, 1980 sekä 1985 sekä vuosittain vuodesta 1987 alkaen
.
<b> Aineiston päivitysaikataulu</b>
Tutustu valmisaineistojen <a href="https://stat.fi/fi/palvelut/palvelut-tutkijoille/tutkimusaineistot/valmisaineistot/valmisaineistojen-paivitysaikataulu">  päivitysaikatauluun</a>.

Aineisto päivittyy vuoden viiveellä verrattuna lapsi-vanhempi-osioon.

<b> Aineiston käyttö ja tilaaminen</b>
Aineisto on tarkoitettu käytettäväksi FIONA-etäkäyttöjärjestelmän kautta, ja se on linkitettävissä muihin henkilövalmisaineistoihin suojatun henkilötunnisteen avulla. 
Käyttöoikeus voidaan myöntää kokonaisaineistoon (kaikki muuttujat koko populaatiolle kaikilta saatavissa olevilta vuosilta), kun sille on tutkimuksellinen tarve. Mikäli tarve koskee vain osaa muuttujista, voidaan aineistosta tilasta räätälöity versio.
Aineisto on FIONA-etäkäyttöjärjestelmässä jaettuina tilastovuosittaisiin vuosikansioihin.

<b> Lisätietoja</b> 
Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@stat.fi.

## Variables (15)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `vuosi` | Vuosi | — | — | — |
| `hid_e` | Suojattu henkilön yksilöivä tunniste | — | — | — |
| `petu` | Perhetunnus | — | — | — |
| `ak_koodi` | Asuntokuntakoodi | — | — | — |
| `syntyv` | Syntymävuosi | — | — | — |
| `hid_e_m` | Suojattu henkilön yksilöivä tunniste, biol. äiti | — | — | — |
| `hid_e_f` | Suojattu henkilön yksilöivä tunniste, biol. isä | — | — | — |
| `hid_e_am` | Suojattu henkilön yksilöivä tunniste, adoptioäiti | — | — | — |
| `hid_e_af` | Suojattu henkilön yksilöivä tunniste, adoptioisä | — | — | — |
| `hid_e_s1` | Suojattu henkilön yksilöivä tunniste, sosiaalinen vanh.1 | — | — | — |
| `hid_e_s2` | Suojattu henkilön yksilöivä tunniste, sosiaalinen vanh.2 | — | — | — |
| `status_m` | Asumisstatus, biol. äiti | — | — | — |
| `status_f` | Asumisstatus, biol. isä | — | — | — |
| `status_am` | Asumisstatus, adoptioäiti | — | — | — |
| `status_af` | Asumisstatus, adoptioisä | — | — | — |

### Variable definitions

#### `vuosi` — Vuosi

Tilastovuosi.

#### `hid_e` — Suojattu henkilön yksilöivä tunniste

Lapsen suojattu TK:n henkilö yksilöivä tunniste. Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e -tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä.

#### `petu` — Perhetunnus

Lapsen perheen tunniste on sama kuin FOLK perhemoduulissa.

#### `ak_koodi` — Asuntokuntakoodi

Lapsen asuntokuntanumero on sama kuin FOLK asuntokuntamoduulissa.

#### `syntyv` — Syntymävuosi

Lapsen syntymävuosi.

#### `hid_e_m` — Suojattu henkilön yksilöivä tunniste, biol. äiti

Biologisen äidin suojattu henkilön yksilöivä tunniste. Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e -tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä.

#### `hid_e_f` — Suojattu henkilön yksilöivä tunniste, biol. isä

Biologisen isän suojattu henkilön yksilöivä tunniste. Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e -tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä.

#### `hid_e_am` — Suojattu henkilön yksilöivä tunniste, adoptioäiti

Adoptioäidin suojattu henkilön yksilöivä tunniste. Tieto on lapsen jokaiselle vuodelle riippumatta siitä, onko adoptio tuolloin voimassa vai ei. Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e -tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä.

#### `hid_e_af` — Suojattu henkilön yksilöivä tunniste, adoptioisä

Adoptioisän Suojattu henkilön yksilöivä tunniste. Tieto on lapsen jokaiselle vuodelle riippumatta siitä, onko adoptio tuolloin voimassa vai ei. Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e -tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä.

#### `hid_e_s1` — Suojattu henkilön yksilöivä tunniste, sosiaalinen vanh.1

Sosiaalisen vanhemman (1.) suojattu henkilön yksilöivä tunniste. Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e -tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä.



Sosiaalinen vanhempi (1.) on samassa asunnossa asuva isä, adoptioisä, sosiaalinen isä tai naisparista se, joka ei ole biologinen äiti.

#### `hid_e_s2` — Suojattu henkilön yksilöivä tunniste, sosiaalinen vanh.2

Sosiaalisen vanhemman (2.) suojattu henkilön yksilöivä tunniste. Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e -tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä.


Sosiaalinen vanhempi (2.) on samassa asunnossa asuva äiti, adoptioäiti, sosiaalinen äiti tai miesparista se, joka ei ole biologinen isä.

#### `status_m` — Asumisstatus, biol. äiti

Biologinen äiti 
1 = asuu lapsen kanssa, 
2 = asuu muualla, 
3 = kuollut, 
4, 5 = ei tietoa / muu.

#### `status_f` — Asumisstatus, biol. isä

Biologinen isä 
1 = asuu lapsen kanssa, 
2 = asuu muualla, 
3 = kuollut, 
4, 5 = ei tietoa / muu.

#### `status_am` — Asumisstatus, adoptioäiti

Adoptioäiti 1 = asuu lapsen kanssa, 2 = asuu muualla, 3 = kuollut, 4 = ei tietoa / muu. Tieto on lapsen jokaiselle vuodelle riippumatta siitä, onko adoptio tuolloin voimassa vai ei.

#### `status_af` — Asumisstatus, adoptioisä

Adoptioisä 1 = asuu lapsen kanssa, 2 = asuu muualla, 3 = kuollut, 4 = ei tietoa / muu. Tieto on lapsen jokaiselle vuodelle riippumatta siitä, onko adoptio tuolloin voimassa vai ei.

---

[← Back to catalogue](../../README.md)
