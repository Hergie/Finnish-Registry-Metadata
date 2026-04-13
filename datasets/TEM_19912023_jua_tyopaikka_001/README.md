# KEHA_Työpaikka: KEHA-keskuksen työnvälitystilaston aineisto

- **Identifier:** `TEM_19912023_jua_tyopaikka_001.xml`
- **DOI:** `work_2016-10_2016-10-16_ain_0004`
- **Temporal coverage:** 1991-01-01 - 2024-12-31
- **Published:** 2025-04-15
- **Organisation:** Työ- ja elinkeinoministeriö
- **Variable count:** 25
- **Observation count:** 4,285,687
- **Population:** TE-toimistoihin ilmoitetut avoimet työpaikat 1991-2024

## Kuvaus / Description

Työllisyys, kehittämis- ja hallintokeskus (KEHA-keskus) on ylläpitänyt työhallinnon asiakaspalvelun tietojärjestelmää URAa. Ennen KEHA-keskusta tietojärjestelmää on ylläpitänyt Työ- ja elinkeinoministeriö yhdessä työ- ja elinkeinotoimistojen kanssa. Tutkijapalveluissa on käytössä kaksi KEHA:n aineistokokonaisuutta: 

1) Työnvälitystilaston aineistoja (osa-aineistot Työnhaku, Työnhakija, Työkunto, Työpaikka) 
2) muita URA-tietojärjestelmän aineistoja. (osa-aineistot Työtarjoukset avoimiin työpaikkoihin, Työtarjoukset palkkatukipaikkoihin, Suunnitelmat, Yhteydenottotavat, Palvelulinja, Sanssikortti, Maahanmuuttajien kielitaito, Kaikkien kielitaito) 

Työpaikka-aineisto sisältää työpaikkailmoitusten perustietoja sekä tietoa työpaikkojen avoinnaolon kestoista seuraavissa  työnvälitystilaston tauluissa:

YPAIKKA: Työpaikkailmoituksen perustiedot
YPKEST: Työpaikkojen avoinnaolon kestot

URA-tietojärjestelmä koostuu kolmesta rekisteristä: henkilöasiakasrekisteristä, työnantajarekisteristä sekä työvoimakoulutuksen järjestäjärekisteristä. URA-järjestelmän käyttöön siirryttiin työvoimatoimistoissa vuonna 1998. Tätä ennen vuodesta 1990 lähtien käytössä oli TYÖTIE-tietojärjestelmä.

Vuoteen 2022 asti tietoja päivitettäessä edeltävien vuosien tiedot on yhdistetty uusimpaan aineistoon. Samalla aineistosta on poistettu duplikaatit, jotka ovat syntyneet kun aineistossa jo olleelle keskeneräiselle jaksolle on saatu uutena havaintona tieto päättymisajankohdasta. Vuodesta 2023 alkaen aineisto käsittää vain KEHA:n tilastovuodelta toimittaman aineiston. Aineistoa yhdistettäessä on siis huomattava, että vuoden lopussa kesken olleet jaksot ovat mukana aineistossa merkinnällä 11.11.2222, sekä mahdollisesti myöhemmin todellisella päättymispäivätiedolla. Todellisten jaksojen lukumäärä on täten havaintojen määrää pienempi.

Aineistojen käsittely tapahtuu FIONA etäkäyttöjärjestelmässä. Tiedot päivittyvät Tilastokeskukseen tallennettuun tutkimusaineistoon kerran vuodessa.

## Muuttujat / Variables (25)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `hid_e` | Suojattu henkilön yksilöivä tunniste | — | — | YPAIKKA |
| `htun_s` | Suojattu henkilötunnus | — | — | — |
| `yrtun_s` | Suojattu työnantajan liike- ja yhteisötunnus | — | — | — |
| `ammnop` | Vaadittava ammatti | — | — | YPAIKKA |
| `hlokd` | Henkilökunnan kokoluokka | — | — | YPAIKKA |
| `illkm` | Työpaikkojen alkuperäinen lukumäärä | — | — | YPAIKKA |
| `ilmno` | Työpaikan ilmoitusnumero | — | — | YPKEST, YPAIKKA |
| `keskd` | Työn kesto | — | — | YPAIKKA |
| `kouk1` | Vaadittava koulutus | — | — | YPAIKKA |
| `kunnop` | Työpaikan sijaintikunta | — | — | YPAIKKA |
| `paikd` | Työaika | — | — | YPAIKKA |
| `rajpv` | Viimeinen hakemuspäivä | — | — | YPAIKKA |
| `talpvm` | Työn alkamispäivä | — | — | YPAIKKA |
| `tapp1` | Työpaikan ilmoittamispäivä | — | — | YPAIKKA |
| `taskd` | Sektori | — | — | YPAIKKA |
| `tkokd` | Vaadittava työkokemus | — | — | YPAIKKA |
| `toanop` | Työnantajan toimiala | — | — | YPAIKKA |
| `tptyyp` | Työpaikan tyyppi | — | — | YPAIKKA |
| `vppvmp` | Viimeinen päivityspäivä | — | — | YPAIKKA |
| `ely` | Hoitava ELY-keskus | — | — | YPAIKKA |
| `apvm` | Avoinnaolon alkamispäivä | — | — | YPKEST |
| `lpvm` | Avoinnaolon päättymispäivä | — | — | YPKEST |
| `pmukd` | Muutoskoodi | — | — | YPKEST |
| `pmuma` | Työpaikkojen muutosmäärä | — | — | YPKEST |
| `tolkm` | Työpaikkailmoitusta kohden tehtyjen työhönosoitusten lukumäärä | — | — | YPKEST |

### Muuttujien määritelmät / Variable definitions

#### `hid_e` — Suojattu henkilön yksilöivä tunniste

**Ryhmä / Group:** YPAIKKA

Vuorottelukorvausta saavan suojattu henkilön yksilöivä tunniste. Vuorotteluvapaalle jääneistä tarvitaan tietoa myös YTVPOLL-taulusta TYOHAKU-aineistosta,
Vuorottelupaikkaan työllistetystä tarvitaan myös tietoa myös YTVALIT-taulusta TYOHAKU-aineistosta. Aiemmin tiedot muuttujassa vvshtun, nykyinen htun_s.

#### `htun_s` — Suojattu henkilötunnus

Vuorottelukorvausta saavan suojattu henkilötunnus niille, joille ei pystytä yhdistämään TK:n henkilön yksilöivää tunnistetta. Vuorotteluvapaalle jääneistä tarvitaan tietoa myös YTVPOLL-taulusta TYOHAKU-aineistosta, Vuorottelupaikkaan työllistetystä tarvitaan myös tietoa myös YTVALIT-taulusta TYOHAKU-aineistosta. Aiemmin nimellä vvshtun.

#### `yrtun_s` — Suojattu työnantajan liike- ja yhteisötunnus

#### `ammnop` — Vaadittava ammatti

**Ryhmä / Group:** YPAIKKA

Ammattiluokitus: https://www2.tilastokeskus.fi/fi/luokitukset/ammatti/

#### `hlokd` — Henkilökunnan kokoluokka

**Ryhmä / Group:** YPAIKKA

1=0-4 henkilöä, 2=5-9 henkilöä, 3=10-19 henkilöä, 4=20-49 henkilöä, 5=50-99 henkilöä, 6=100-199 henkilöä, 7=200-499 henkilöä, 8=500-999 henkilöä, 9=Yli 1000 henkilöä

#### `illkm` — Työpaikkojen alkuperäinen lukumäärä

**Ryhmä / Group:** YPAIKKA

#### `ilmno` — Työpaikan ilmoitusnumero

**Ryhmä / Group:** YPKEST, YPAIKKA

#### `keskd` — Työn kesto

**Ryhmä / Group:** YPAIKKA

1=1-11p,2=11p-1kk,3=1-3kk,4=3-6kk,5=6-12kk,6=>12

#### `kouk1` — Vaadittava koulutus

**Ryhmä / Group:** YPAIKKA

#### `kunnop` — Työpaikan sijaintikunta

**Ryhmä / Group:** YPAIKKA

Rekisterissä kuntakoodeina käytetään Väestörekisterikeskuksen ylläpitämiä 3-numeroisia kuntakoodeja.

#### `paikd` — Työaika

**Ryhmä / Group:** YPAIKKA

1=Kokopäivätyö, 2=Liukuva päivätyö, 3=2-vuorotyö, 4=3-vuorotyö, 5=4-5 -vuorotyö, 6=Yötyö, 7=Osapäivätyö, 8=Muu osa-aikatyö, 9=Iltatyö

#### `rajpv` — Viimeinen hakemuspäivä

**Ryhmä / Group:** YPAIKKA

#### `talpvm` — Työn alkamispäivä

**Ryhmä / Group:** YPAIKKA

#### `tapp1` — Työpaikan ilmoittamispäivä

**Ryhmä / Group:** YPAIKKA

#### `taskd` — Sektori

**Ryhmä / Group:** YPAIKKA

1=valtio,2=kunta,3=yks.ta, 4=yritys, 5=kotit., 6=kuntainl

#### `tkokd` — Vaadittava työkokemus

**Ryhmä / Group:** YPAIKKA

0=ei, 1=hieman, 2=täysi (nykyisin tyhjää)

#### `toanop` — Työnantajan toimiala

**Ryhmä / Group:** YPAIKKA

Työnantajan tuotantotoiminnan luokittelemiseen käytetään Tilastokeskuksen laatimaa toimialaluokitusta. Työhallinnon asiakasrekisterissä käytössä on 2-numerotaso, johon kuuluvat luokat merkitään 2-numeroisella koodilla.

#### `tptyyp` — Työpaikan tyyppi

**Ryhmä / Group:** YPAIKKA

1=palkka, 2=provisio, 3=yritys, 4=vuor.vapaa

#### `vppvmp` — Viimeinen päivityspäivä

**Ryhmä / Group:** YPAIKKA

#### `ely` — Hoitava ELY-keskus

**Ryhmä / Group:** YPAIKKA

02 = UUSIMAA, 03 = VARSINAIS-SUOMI, 14 = SATAKUNTA, 15 = HÄME, 04 = PIRKANMAA, 05 = KAAKKOIS-SUOMI, 06 = ETELÄ-SAVO, 09 = POHJOIS-SAVO, 10 = POHJOIS-KARJALA, 08 = KESKI-SUOMI, 16 = ETELÄ-POHJANMAA, 07 = POHJANMAA, 12 = POHJOIS-POHJANMAA, 11 = KAINUU, 13 = LAPPI, 20 = AHVENANMAA, 30 = ULKOMAAT,

#### `apvm` — Avoinnaolon alkamispäivä

**Ryhmä / Group:** YPKEST

#### `lpvm` — Avoinnaolon päättymispäivä

**Ryhmä / Group:** YPKEST

#### `pmukd` — Muutoskoodi

**Ryhmä / Group:** YPKEST

Työpaikan avoimmaolon muutoskoodi  0=täytetty työhönosoituks., 1=täyt.muuten tston hakijalla, 2=täytetty muutoin, 3=peruutettu, 4=ehdokkaita riittävästi, 5=työpaikkoja lisätty, 6=hakuaika päättynyt, 7=täytetty verkon kautta, 8=poistettu/peruutettu verkon kautta, 9=täyttymätön työpaikka (tulossa oleva arvo)

#### `pmuma` — Työpaikkojen muutosmäärä

**Ryhmä / Group:** YPKEST

#### `tolkm` — Työpaikkailmoitusta kohden tehtyjen työhönosoitusten lukumäärä

**Ryhmä / Group:** YPKEST

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
