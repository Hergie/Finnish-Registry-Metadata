# FLOWN - PARTNER yhtiömiestiedot

- **Identifier:** `FLOWN_20072020_jua_partner_001.xml`
- **DOI:** `ys_2011-03_2011-03-02_ain_0001`
- **Temporal coverage:** 2007-01-01 - 2024-12-31
- **Published:** 2022-04-05
- **Organisation:** Tilastokeskus
- **Variable count:** 20
- **Observation count:** —
- **Population:** Avoimet ja kommandiittiyhtiöt ja niiden yhtiömiehet
- **Source:** Verohallinnon Tilastokeskukselle tilastotarkoituksiin toimittamat tiedot

## Kuvaus / Description

FLOWN (Finnish Longitudinal OWNer-Employer-Employee Data) -valmisaineisto mahdollistaa yritysten ja niiden omistajien tietojen yhdistämisen ja käytön tutkimuksessa. Aineisto perustuu Verohallinnon Tilastokeskukselle tilastotarkoitusta varten toimittamiin osakeyhtiöiden osakastietoihin, yhtiömiestietoihin ja osinkotietoihin. 

FLOWN-aineisto koostuu seuraavista osista:

FLOWN_OWNER-data sisältää osakastiedot vuodesta 2006 lähtien (osakelkm=0 ja tuplatiedot on poistettu).
Osakeyhtiön on ilmoitettava tiedot osakkaistaan, jos osakkaita on enintään 10. Jos osakkaita on enemmän, osakeyhtiö ilmoittaa vähintään 10 % yhtiön osakekannasta omistavien osakkaiden henkilötiedot sekä kaikki osakkaat, joille on annettu osakaslaina. Tiedot kerätään vuosittain Verohallinnon lomakkeella 6B ja lisälomakkeella 72. Aineistoon on yhdistetty verottajan tieto yrityksen osakekannasta ja yrityksen hallussa olevista omista osakkeista. Vuosina 2017-2020 tiedoissa on joitakin yritys-omistaja-duplikaatteja.

FLOWN_PARTNER-data sisältää yhtiömiestiedot vuodesta 2007 lähtien avointen yhtiöiden ja kommandiittiyhtiöiden osalta. Muut yhtiömuodot (verotus- ja elinkeinoyhtymät) on rajattu pois valmisaineistosta. Yhtymät ilmoittavat yhtiömiehiä koskevat perustiedot verohallinnon lomakkeilla 6A ja 72A. Tietosisältöön on vaikuttanut jonkin verran Verohallinnon tietojärjestelmän uudistaminen 2017 - 2018. 

FLOWN_DIVIDEND-data sisältää osinkotiedot maksajan ja saajan mukaan vuodesta 2003 lähtien. Osinkotiedot saadaan verottajan vuosi-ilmoitustiedoista, lomake 7812. Yritys voi maksaa osinkoa useammin kuin kerran vuodessa, jolloin tiedot ovat omilla riveillään.

FLOWN_LISTED-data sisältää tiedot pörssilistatuista yrityksistä vuodesta 2000 lähtien. Tietojen lähteenä on Nasdaq Omx Nordic -internetsivut. Konsernin emon tietojen lisäksi muut konsernin osat voi yhdistää FIRM_GROUP- tai FIRM_ENTER-datasta.

Aineisto voidaan yhdistää myös yritysten työntekijöihin. Yrityksen henkilöstön ominaisuudet ja henkilö-yritys-linkit ovat erikseen saatavissa FOLK-valmisaineistomoduuleista. Yritysten ja niiden toimipaikkojen tietoja on saatavissa FIRM-valmisaineistomoduuleista. Omistajien ketjuttamista varten on käytettävissä FLOWN-valmisaineiston yhteydessä erillinen stata-koodi.

Muista yksikkötason tiedoista poiketen kynnyssääntönä FLOWN-aineiston tietoja julkaistaessa on vähintään 5 havaintoa/luokka. Erityistä huomiota on kiinnitettävä siihen, että suojaus tehdään henkilö- ja yritystasolla siten, että sekä henkilöitä että yrityksiä on oltava julkaistavissa luokissa tietojen taustalla vähintään kynnysarvon verran.

Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@stat.fi.

## Muuttujat / Variables (20)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `yrtun_astunnus_s` | Suojattu yhtymän Y-tunnus | — | — | — |
| `hid_e` | Suojattu osakkaan yksilöivä tunniste | — | — | — |
| `yrtun_astunnus2_s` | Suojattu osakkaan Y-tunnus | — | — | — |
| `astunnus2_s` | Suojattu osakkaan muu tunnus | — | — | — |
| `vuosi` | Vuosi | — | — | — |
| `yhtiomies` | Yhtiömieslaji | — | — | — |
| `kansal` | Ulkomaalaisen osakkaan kotivaltio | — | — | — |
| `alkupvm` | Osakkuuden alkupäivä | — | — | — |
| `loppupvm` | Osakkuuden loppupäivä | — | — | — |
| `maatnim` | Osuus maataloustulosta, nimittäjä | — | — | — |
| `maatoso` | Osuus maataloustulosta, osoittaja | — | — | — |
| `muutulonim` | Osuus tulosta, nimittäjä | — | — | — |
| `muutulooso` | Osuus tulosta, osoittaja | — | — | — |
| `varalnim` | Osuus varallisuudesta, nimittäjä | — | — | — |
| `varaloso` | Osuus varallisuudesta, osoittaja | — | — | — |
| `metsanim` | Osuus metsätalouden tulosta, nimittäjä | — | — | — |
| `metsaoso` | Osuus metsätalouden tulosta, osoittaja | — | — | — |
| `muutunim` | Osuus yhtymän muusta tulosta, nimittäjä | — | — | — |
| `muutuoso` | Osuus yhtymän muusta tulosta, osoittaja | — | — | — |
| `verohoik_2021` | Verohallinnon oikeudellinen muoto 2021 | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `yrtun_astunnus_s` — Suojattu yhtymän Y-tunnus

#### `hid_e` — Suojattu osakkaan yksilöivä tunniste

Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e -tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä. Korvaa muuttujan shnro_astunnus2.

#### `yrtun_astunnus2_s` — Suojattu osakkaan Y-tunnus

#### `astunnus2_s` — Suojattu osakkaan muu tunnus

Sis. mm. epävalideja hetuja tai muita ilmoitettuja linkittymättömiä tunnuksia.

#### `vuosi` — Vuosi

#### `yhtiomies` — Yhtiömieslaji

Arvot:
1 = äänetön yhtiömies
2 = vastuunalainen yhtiömies

#### `kansal` — Ulkomaalaisen osakkaan kotivaltio

Ulkomaisen osakkaan kotivaltio (esim. CZ, JP).

#### `alkupvm` — Osakkuuden alkupäivä

Osakkuuden alkupäivä, muotoa PPKKVVVV

#### `loppupvm` — Osakkuuden loppupäivä

Osakkuuden loppupäivä, muotoa PPKKVVVV

#### `maatnim` — Osuus maataloustulosta, nimittäjä

#### `maatoso` — Osuus maataloustulosta, osoittaja

#### `muutulonim` — Osuus tulosta, nimittäjä

Vuodesta 2018 lähtien.

#### `muutulooso` — Osuus tulosta, osoittaja

Vuodesta 2018 lähtien.

#### `varalnim` — Osuus varallisuudesta, nimittäjä

#### `varaloso` — Osuus varallisuudesta, osoittaja

#### `metsanim` — Osuus metsätalouden tulosta, nimittäjä

Vuoteen 2017 asti.

#### `metsaoso` — Osuus metsätalouden tulosta, osoittaja

Vuoteen 2017 asti.

#### `muutunim` — Osuus yhtymän muusta tulosta, nimittäjä

Vuoteen 2017 asti.

#### `muutuoso` — Osuus yhtymän muusta tulosta, osoittaja

Vuoteen 2017 asti.

#### `verohoik_2021` — Verohallinnon oikeudellinen muoto 2021

Verohallinnon oikeudellinen muoto vuoden 2021 lopussa tai viimeisin tiedossa oleva. Mukaan on otettu seuraavat yhtiömuodot:
10 avoin yhtiö
11 kommandiittiyhtiö
12 osakeyhtiö

Yritystunnus ei muutu, jos yritys on vaihtanut yhtiömuotoa ay/ky/oy.

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
