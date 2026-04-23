# FLOWN - LISTED pörssilistatut yritykset

- **Identifier:** `FLOWN_20002021_jua_listed_001.xml`
- **DOI:** `work_2017-03_2017-03-23_ain_0001`
- **Temporal coverage:** 2000-01-01 - 2024-01-01
- **Published:** 2020-03-24
- **Organisation:** Tilastokeskus
- **Variable count:** 3
- **Observation count:** —
- **Population:** Pörssiyritykset
- **Source:** Tilastokeskuksen julkisista lähteistä kokoamat tiedot

## Description

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

## Variables (3)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `yrtun_s` | Suojattu yritystunnus | — | — | — |
| `vuosi` | Vuosi | — | — | — |
| `oyr_porssi` | Pörssilistattu yritys | — | — | — |

### Variable definitions

#### `yrtun_s` — Suojattu yritystunnus

#### `vuosi` — Vuosi

#### `oyr_porssi` — Pörssilistattu yritys

Saa arvon 1, jos yritys on pörssilistattu Helsingissä (OMXH). Lähde: Kauppalehden nettisivut. Sisältää konsernien emoyrityksiä, jolloin muiden konserniin kuuluvien Y-tunnusten yhdistäminen tulee tehdä FIRM_GROUP- tai FIRM_ENTER-aineistojen avulla. Aineistossa saattaa olla puutteita tai virheitä.

---

[← Back to catalogue](../../README.md)
