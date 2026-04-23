# FLOWN - DIVIDEND osinkotiedot

- **Identifier:** `FLOWN_20032021_jua_dividend_001.xml`
- **DOI:** `work_2017-03_2017-03-23_ain_0001`
- **Temporal coverage:** 2003-01-01 - 2024-01-01
- **Published:** 2020-03-24
- **Organisation:** Tilastokeskus
- **Variable count:** 17
- **Observation count:** —
- **Population:** Osingon maksajat ja saajat
- **Source:** Verohallinnon Tilastokeskukselle tilastotarkoituksiin toimittamat tiedot
- **Related:** <a href= "http://www.stat.fi/meta/tietosuojaselosteet/tutka_tietosuojaseloste_yhdistetty_omistaja_tyontekija_tyonantaja_aineisto_flown.html">FLOWN-aineisto</a>

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

## Variables (17)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `hid_e` | Osingon saajan suojattu henkilön yksilöivä tunniste | — | — | — |
| `saa_yrtun_s` | Osingon saajan suojattu y-tunnus | — | — | — |
| `mak_yrtun_s` | Osingon maksajan suojattu y-tunnus | — | — | — |
| `saalaji` | Saajalaji, henkilo/yritys | — | — | — |
| `vuosi` | Vuosi (aineistotunniste) | — | — | — |
| `VEROVUOS` | Sen tilikauden päättymisvuosi, jolta osinko maksettu | — | — | — |
| `MAKSVUOS` | Osingon maksuvuosi | — | — | — |
| `JAKTYYPP` | Jakavan yhtiön tyyppi | — | — | — |
| `OSINKO` | Osingonsaajalle maksettu määrä sentteinä/euroina | — | — | — |
| `SUORLAJI` | Suorituslaji | — | — | — |
| `ENNPIDAT` | Osingoista toimitettu ennakonpidätys sentteinä/euroina | — | — | — |
| `OSAKELKM` | Osakkeiden lukumäärä osingonjakopäätöspäivänä | — | — | — |
| `YELMYEL` | YEL MYEL-vakuutettu | — | — | — |
| `ASUNTO` | Käytössä asunto, joka kuuluu yhtiön varallisuuteen | — | — | — |
| `RAHALAIN` | Osakkaalla rahalaina | — | — | — |
| `YLIJAAMA` | Osuuskuntien ylijäämä (brutto) | — | — | — |
| `LISMAARA` | Omaan pääomaan merkitty määrä | — | — | — |

### Variable definitions

#### `hid_e` — Osingon saajan suojattu henkilön yksilöivä tunniste

Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e -tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä. Korvaa muuttujan saa_shnro.

#### `saa_yrtun_s` — Osingon saajan suojattu y-tunnus

#### `mak_yrtun_s` — Osingon maksajan suojattu y-tunnus

#### `saalaji` — Saajalaji, henkilo/yritys

Tieto siitä, onko saaja henkilötunnus- (1) vai yritystunnusmuotoinen (2)

#### `vuosi` — Vuosi (aineistotunniste)

#### `VEROVUOS` — Sen tilikauden päättymisvuosi, jolta osinko maksettu

Tilikausi, jolta osinko maksettu

#### `MAKSVUOS` — Osingon maksuvuosi

Vuosi, jolloin osinko maksettu

#### `JAKTYYPP` — Jakavan yhtiön tyyppi

Jakavan yhtiön tyyppi 
J = julkisesti noteerattu yhtiö tai osuuskunta (2006-)
M = muu yhtiö tai muu osuuskunta, jossa on vähintään 500 jäsentä
S = muu osuuskunta, jossa on alle 500 jäsentä (2015-)
P = pörssin päälistalla olevan yhtiö (2004-2005)
N = I-, NM-, Pre-listalla tai ML-markkinalla oleva yhtiö (2004-2005)

#### `OSINKO` — Osingonsaajalle maksettu määrä sentteinä/euroina

Osingonsaajalle maksettu määrä sentteinä vuoteen 2017 asti ja alkaen vuodesta 2018 euroina. Vuodesta 2018 alkaen osuuskuntien ylijäämät erillisessä muuttujassa ylijaama (tätä ennen sisältyvät osinko-muuttujaan).

#### `SUORLAJI` — Suorituslaji

Suorituslaji, saatavissa 2005-
01 = Osinko
02 = Korko (osuuskunta, säästöpankki, keskinäinen vakuutusyhtiö)
03 = Reit-osingot asuntojen vuokraustoiminnasta 
04 = VOPR-osinko (2014 alkaen)
05 = Osuuskunnan ylijäämä (2015 alkaen)
06 = Osuuskunnan VOPR-ylijäämä (2015 alkaen))
98 = Suorituslaji on tyhjä
99 = Virhe suorituslajissa

#### `ENNPIDAT` — Osingoista toimitettu ennakonpidätys sentteinä/euroina

Osingosta toimitettu ennakonpidätys sentteinä (2005-2017) tai euroina (2018-)

#### `OSAKELKM` — Osakkeiden lukumäärä osingonjakopäätöspäivänä

Osakkeiden lukumäärä osingonjakopäätöspäivänä (2005-)

#### `YELMYEL` — YEL MYEL-vakuutettu

Onko YEL/MYEL-vakuutettu (1=on) (2005-)

#### `ASUNTO` — Käytössä asunto, joka kuuluu yhtiön varallisuuteen

Onko osingonsaajalla tai perheellä käytettävissä asunto, joka kuuluu yhtiön varallisuuteen (1=on) (2005-)

#### `RAHALAIN` — Osakkaalla rahalaina

Onko osakkaalla rahalaina (1=on) (2005-)

#### `YLIJAAMA` — Osuuskuntien ylijäämä (brutto)

Vuodesta 2018 alkaen osuuskuntien ylijäämät ovat omana muuttujanaan. Aiemmin sisältyivät osinko-muuttujaan. Ylijäämiä ovat suorituslajit 05 ja 06.

#### `LISMAARA` — Omaan pääomaan merkitty määrä

Alkaen vuodesta 2018.

---

[← Back to catalogue](../../README.md)
