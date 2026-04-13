# PRH_BOARD Kaupparekisterin vastuuhenkilötiedot

- **Identifier:** `PRH_20162023_jua_board_002.xml`
- **DOI:** `work_2017-11_2017-11-06_ain_0001`
- **Temporal coverage:** 2016-01-01 - 2022-12-31
- **Published:** 2025-03-17
- **Organisation:** Tilastokeskus
- **Variable count:** 12
- **Observation count:** —
- **Population:** Tietyt yhtiömuodot ja tietyt roolit
- **Source:** Patentti- ja rekisterihallituksen ylläpitämä kaupparekisteri
- **Related:** <a href= "https://www.prh.fi/stc/attachments/rekisteri-_ja_tietosuojaselosteet/kaupparekisteri_tietosuojaseloste.pdf">Kaupparekisteri</a>

## Kuvaus / Description

PRH_BOARD-aineisto sisältää tietoja yritysten ja muiden organisaatioiden vastuuhenkilöistä, kuten toimitusjohtajista, hallitusten jäsenistä ja tilintarkastajista vuosilta 2016 - 2023. Aineisto pohjautuu Patentti- ja rekisterihallituksen (PRH) kaupparekisteripoiminnan tauluihin (Companrolesid_base ja Companyrolesid) vuodesta 2025 alkaen. Näitä tauluja ei hyödynnetä varsinaisessa tilastotoiminnassa.

Aiemmat vastuuhenkilöitä koskevat valmisaineistot (prh_011994122015 ja prh_012016072019) on koottu PRH:n Tilastokeskukselle toimittaman erillistoimituksen perusteella. 

Lähtökohta on ollut säilyttää aiempien aineistojen sisältö ja muuttujien nimeämiskäytännöt mahdollisimman yhteneväisinä myös suoraan kaupparekisteri poimintaan pohjautuvassa aineistossa. Kaupparekisteripohja mahdollistaa myös aineiston sisällön laajentamisen, mutta toistaiseksi laajennukset ovat olleet maltillisia.

Aineisto kattaa kaikki lähdeaineiston yhtiömuodot ja juridiset toimielimet. Käyttäjän tulee tehdä tarvittavat rajaukset, esimerkiksi osakeyhtiöiden keskeiset toimielimet ovat hallitus (HAL) ja tilintarkastus (TIL).

Yritystunnukset ja toimielimen roolien henkilökohtaiset tiedot on pseudonymisoitu. Aineistosta on poistettu vapaasti kirjoitetut kentät, kuten toiminnan tai oikaisun kuvaukset, jotka voivat sisältää yksilöiviä tietoja. Myös suurelta osin tyhjät kentät, kuten osakepääomaa koskevat tiedot, on jätetty pois.

Yritysmuotoa ja toiminnan lopettamista koskevia tietoja ei ole sisällytetty kaupparekisteripoimintaan tietojen puutteellisuuden vuoksi. Näitä tietoja on saatavilla Tilastokeskuksen Yritys- ja toimipaikkarekisteriin pohjautuvasta FIRM_BASE-aineistosta, johon PRH_BOARD-aineisto on linkitettävissä Syrtun-muuttujan avulla.

Aineiston poimintaan on vaikuttanut ilmoitusten käsittelyn ja järjestelmien muutokset eri aikaväleillä. Erityisesti uuden kaupparekisterin käsittelyjärjestelmän käyttöönotto toukokuussa 2014 muutti vastuuhenkilöiden eroilmoitusten käsittelyä. Tämän seurauksena hallituksen voimassaolon alkupäivämäärä voi määräytyä eri tavoin järjestelmän muutoksista riippuen. Historiatiedoissa voi esiintyä tietoteknisten ja käsittelyprosessien muutosten vuoksi puutteita tai virheitä.

PRH ei vastaa aineistoon sisältyvien tietojen virheistä, katoamisista tai muuttumisesta eikä näistä mahdollisesti aiheutuvista vahingoista käyttäjälle tai kolmansille osapuolille. PRH ei myöskään vastaa Tilastokeskuksen aineistoon tekemistä muutoksista tai tarjoamista palveluista.



Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@stat.fi.

## Muuttujat / Variables (12)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `syrtun` | Suojattu yritystunnus | — | — | — |
| `shnro` | Suojattu henkilönumero | — | — | — |
| `YRITYKSEN_TILA` | Yrityksen tila | — | — | — |
| `TOIMIELINKOODI` | Toimielimen koodi | — | — | — |
| `ROOLIKOODI` | Vastuuhenkilörooli | — | — | — |
| `JASENMAARA_MAX` | Jasenet enimmäismäärä | — | — | — |
| `JASENMAARA_MIN` | Jasenet vähimmäismäärä | — | — | — |
| `ASUINMAA` | Asuinmaa karkeistettuna | — | — | — |
| `KANSALAISUUS` | Jasenen kansallisuus karkeistettuna | — | — | — |
| `ROOLIN_ALKU_PVM` | Vastuuhenkilön roolin alkamispäivämäärä | — | — | — |
| `ROOLIN_LOPPU_PVM` | Vastuuhenkilön roolin loppumispäivämäärä | — | — | — |
| `ORGANISAATION_REKISTEROINTI_PVM` | Organisaation  perustamispäivämäärä | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `syrtun` — Suojattu yritystunnus

#### `shnro` — Suojattu henkilönumero

Pohja-aineistossa on myös tyhjiä jenttiä, jotka on myös tuotu mukaan. Kyseessä on useimmiten henkilö, jolla ei ole suomalaista henkilötunnusta.

#### `YRITYKSEN_TILA` — Yrityksen tila

R=rekisterissä, L=lakannut

#### `TOIMIELINKOODI` — Toimielimen koodi

Toimielinkoodi: 
ASTO	Asukastoimikunta
EDU	Edustaja
ELI	Elinkeinonharjoittaja
ESR	Tosiasialliset edunsaajat
ETJÄS	Etuyhtymän jäsenet
EVA	Edunvalvojat
HAL	Hallitus
HH	Hallinnon hoitaja
HN	Hallintoneuvosto
IS	Isännöitsijä
ISAN	Isännöitsijät
JO	Johtaja
JOH	Johtokunta
JOHT	Johtajat
OI	Oikeutetut
PER	Perustajat
PR	Prokuristit
SANS	Selvittäjät
SELM	Selvitysmiehet
SO	Oikeutetut selvitystilan aikana
TEDU	Toimipaikan edustajat
TIL	Tilintarkastajat
TJ	Toimitusjohtaja
TJS	Toimitusjohtajan sijainen
TOIM	Toimitusjohtajat
UE	Ulkomaiset edustajat
USM	Uskotut miehet
VAH	Vastuunalainen hoitaja
VED	Varaedustaja
VIS	Varaisännöitsijä
VTJ	Varatoimitusjohtaja
YHM	Yhtiömiehet

#### `ROOLIKOODI` — Vastuuhenkilörooli

Vastuuhenkilörooli saa arvot:
E  Edunvalvoja
EDU	Edustaja
ELI	Elinkeinonharjoittaja
ES	Tosiasiallinen edunsaaja
HH	Hallinnon hoitaja
IS	Isännöitsijä
J	Varsinainen jäsen
JO	Johtaja
LT	Lisätilintarkastaja
OI	Oikeutettu
PIS	Päävastuullinen isännöitsijä
PJ	Puheenjohtaja
PR	Prokuristi
PTI	Päävastuullinen tilintarkastaja
S	Selvitysmies
SANS	Saneerauksen selvittäjä
SO	Oikeutettu selvitystilan aikana
T	Tilintarkastaja
TJ	Toimitusjohtaja
TJS	Toimitusjohtajan sijainen
U	Uskottu mies
UE	Ulkomainen edustaja
VAH	Vastuunalainen hoitaja
VED	Varaedustaja
VIS	Varaisännöitsijä
VJ	Varajäsen
VPJ	Varapuheenjohtaja
VS	Varaselvitysmies
VT	Varatilintarkastaja
VTJ	Varatoimitusjohtaja
VU	Uskotun miehen varamies
YHM	Yhtiömies
YHMÄ	Äänetön yhtiömies

#### `JASENMAARA_MAX` — Jasenet enimmäismäärä

Varsinaisten jäsenten enimmäismäärä toimielimessä

#### `JASENMAARA_MIN` — Jasenet vähimmäismäärä

Varsinaisten jäsenten vähimmäismäärämäärä toimielimessä

#### `ASUINMAA` — Asuinmaa karkeistettuna

Jäsenen asuinmaa karkeistettuna: FI, Muu Eurooppa ja Muu

#### `KANSALAISUUS` — Jasenen kansallisuus karkeistettuna

FI - Suomi, muutoin "-"

#### `ROOLIN_ALKU_PVM` — Vastuuhenkilön roolin alkamispäivämäärä

Perustuu Kaupparekisrein Companyrolesid-taulun muuttujaan body_registrationDate

#### `ROOLIN_LOPPU_PVM` — Vastuuhenkilön roolin loppumispäivämäärä

Jos kaupparekisteri poiminnan Companyrolesid-taulun muuttuja "body_expirationDate" on  tyhjä, niin perustuu muodostamissääntöön.

#### `ORGANISAATION_REKISTEROINTI_PVM` — Organisaation  perustamispäivämäärä

Yrityksen/organisaation perustamispäivämäärä

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
