# FLOWN - OWNER osakastiedot

- **Identifier:** `FLOWN_20062022_jua_owner_001.xml`
- **DOI:** `work_2017-03_2017-03-23_ain_0001`
- **Temporal coverage:** 2006-01-01 - 2024-01-01
- **Published:** 2020-03-24
- **Organisation:** Tilastokeskus
- **Variable count:** 11
- **Observation count:** —
- **Population:** Osakeyhtiöt ja niiden osakkaat
- **Source:** Verohallinnon Tilastokeskukselle tilastotarkoituksiin toimittamat tiedot

## Kuvaus / Description

FLOWN (Finnish Longitudinal OWNer-Employer-Employee Data) -valmisaineisto mahdollistaa yritysten ja niiden omistajien tietojen yhdistämisen ja käytön tutkimuksessa. Aineisto perustuu Verohallinnon Tilastokeskukselle tilastotarkoitusta varten toimittamiin osakeyhtiöiden osakastietoihin, yhtiömiestietoihin ja osinkotietoihin. 

FLOWN-aineisto koostuu seuraavista osista:

FLOWN_OWNER-data sisältää osakastiedot vuodesta 2006 lähtien (osakelkm=0 ja tuplatiedot on poistettu).
Osakeyhtiön on ilmoitettava tiedot osakkaistaan, jos osakkaita on enintään 10. Jos osakkaita on enemmän, osakeyhtiö ilmoittaa vähintään 10 % yhtiön osakekannasta omistavien osakkaiden henkilötiedot sekä kaikki osakkaat, joille on annettu osakaslaina. Tiedot kerätään vuosittain Verohallinnon lomakkeella 6B ja lisälomakkeella 72. Aineistoon on yhdistetty verottajan tieto yrityksen osakekannasta ja yrityksen hallussa olevista omista osakkeista. 

FLOWN_PARTNER-data sisältää yhtiömiestiedot vuodesta 2007 lähtien avointen yhtiöiden ja kommandiittiyhtiöiden osalta. Muut yhtiömuodot (verotus- ja elinkeinoyhtymät) on rajattu pois valmisaineistosta. Yhtymät ilmoittavat yhtiömiehiä koskevat perustiedot verohallinnon lomakkeilla 6A ja 72A. Tietosisältöön on vaikuttanut jonkin verran Verohallinnon tietojärjestelmän uudistaminen 2017 - 2018. 

FLOWN_DIVIDEND-data sisältää osinkotiedot maksajan ja saajan mukaan vuodesta 2003 lähtien. Osinkotiedot saadaan verottajan vuosi-ilmoitustiedoista, lomake 7812. Yritys voi maksaa osinkoa useammin kuin kerran vuodessa, jolloin tiedot ovat omilla riveillään.

FLOWN_LISTED-data sisältää tiedot pörssilistatuista yrityksistä vuodesta 2000 lähtien. Tietojen lähteenä on Nasdaq Omx Nordic -internetsivut. Konsernin emon tietojen lisäksi muut konsernin osat voi yhdistää FIRM_GROUP- tai FIRM_ENTER-datasta.

Aineisto voidaan yhdistää myös yritysten työntekijöihin. Yrityksen henkilöstön ominaisuudet ja henkilö-yritys-linkit ovat erikseen saatavissa FOLK-valmisaineistomoduuleista. Yritysten ja niiden toimipaikkojen tietoja on saatavissa FIRM-valmisaineistomoduuleista. Omistajien ketjuttamista varten on käytettävissä FLOWN-valmisaineiston yhteydessä erillinen stata-koodi.

Muista yksikkötason tiedoista poiketen kynnyssääntönä FLOWN-aineiston tietoja julkaistaessa on vähintään 5 havaintoa/luokka. Erityistä huomiota on kiinnitettävä siihen, että suojaus tehdään henkilö- ja yritystasolla siten, että sekä henkilöitä että yrityksiä on oltava julkaistavissa luokissa tietojen taustalla vähintään kynnysarvon verran.

Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@stat.fi.

## Muuttujat / Variables (11)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `yrtun_s` | Suojattu yritystunnus | — | — | — |
| `hid_e` | Suojattu henkilön yksilöivä tunniste (omistajatunnus, henkilö) | — | — | — |
| `omtun_yrtun_s` | Suojattu omistajatunnus, yritys | — | — | — |
| `vuosi` | Vuosi | — | — | — |
| `omlaji` | Omistajalaji, henkilo/yritys | — | — | — |
| `ulkhenkom` | Ulkomainen henkilöomistaja | — | — | — |
| `ulkyrom` | Ulkomainen yritysomistaja | — | — | — |
| `osakelkm` | Osakkeiden lukumäärä | — | — | — |
| `osakek` | Osakekanta | — | — | — |
| `yhtionomat` | Yhtiön hallussa olevat omat osakkeet | — | — | — |
| `omistusmuutos` | Omistusmuutoksen vuosi | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `yrtun_s` — Suojattu yritystunnus

Suojattu yritystunnus yhdistyy muihin yritysvalmisaineistoihin niiltä osin kuin yritykset (osakeyhtiöt) ovat ko. tilaston kohdejoukossa mukana.

#### `hid_e` — Suojattu henkilön yksilöivä tunniste (omistajatunnus, henkilö)

Suojattu henkilöomistajan tunnus (Tilastokeskuksen henkilönumero), ks. OMLAJI. Jos henkilönumeroa ei ole löytynyt ko. hetulle (tilapäinen, virheellinen tms.), tunnus on tyhjä, mutta OMLAJI saa arvon 1. Korvaa muuttujan omtun_shnro.

Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e -tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä.

#### `omtun_yrtun_s` — Suojattu omistajatunnus, yritys

Suojattu yritysomistajan tunnus (Y-tunnus), ks. OMLAJI. Jos omistaja on ulkomainen yritys, tunnus on tyhjä, mutta ULKYROM saa arvon 1 ja OMLAJI arvon 2. Tunnus voi olla myös tuntematon, jolloin OMLAJI saa arvon 2 (osa henkilöitä).

#### `vuosi` — Vuosi

#### `omlaji` — Omistajalaji, henkilo/yritys

Tieto siitä, onko omistaja henkilötunnus- (1) vai yritystunnusmuotoinen (2)

#### `ulkhenkom` — Ulkomainen henkilöomistaja

Tieto siitä, onko omistaja ulkomainen yritys, jolla ei henkilötunnusta (laatu huono, ei kattava), vuodesta 2017 alkaen

#### `ulkyrom` — Ulkomainen yritysomistaja

Tieto siitä, onko omistaja ulkomainen yritys, jolla ei ly-tunnusta (ei kattava)

#### `osakelkm` — Osakkeiden lukumäärä

Osakkeenomistajan osakkeiden lukumäärä (ilmoitetut yhteensä voi joissakin tapauksissa olla suurempi kuin osakekanta)

#### `osakek` — Osakekanta

Yhtiön osakkeiden lukumäärä yhteensä

#### `yhtionomat` — Yhtiön hallussa olevat omat osakkeet

Yhtiön hallussa olevat omat osakkeet

#### `omistusmuutos` — Omistusmuutoksen vuosi

Saatavissa vuodesta 2018 lähtien. 

"Merkitse verovuosi, jolloin vaihto on tapahtunut, jos yli puolet osakkeista tai osuuksista on vaihtanut omistajaa verovuoden aikana tai vaiheittain usean vuoden aikana. Jos vaihtuminen on tapahtunut vaiheittain usean vuoden aikana, merkitse se verovuosi, jota ennen tai jonka aikana syntyneet tappiot eivät omistajanvaihdosten vuoksi ole vähennyskelpoisia."

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
