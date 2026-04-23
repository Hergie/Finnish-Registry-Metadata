# FLOWN - FIRM yritys- ja henkilötiedot

- **Identifier:** `FLOWN_20062016_jua_firm_002.xml`
- **DOI:** `work_2017-03_2017-03-23_ain_0001`
- **Temporal coverage:** 2006-01-01 - 2016-01-01
- **Published:** 2022-04-06
- **Organisation:** Tilastokeskus
- **Variable count:** 21
- **Observation count:** —
- **Population:** Osakeyhtiöt ja niiden osakkaat
- **Source:** Verohallinnon osakeyhtiöiden osakas- ja osinkotiedot, Tilastokeskuksen rakenne- ja tilinpäätöstilaston tiedot sekä työssäkäynti- ja työsuhdetiedot (FLEED)

## Description

FLOWN - FIRM -data sisältää tutkimusta varten muokatut tiedot yrityksittäin ja henkilöittäin vuosilta 2006-2016. Aineisto on rajattu verottajan osakastietokannan yrityksiin, joille on löytynyt vähintään 1 henkilöomistaja (tarvittaessa ketjutettu 1 tai 2 omistusportaan päästä). Aineistoon on yhdistetty tietoja FLEED-aineistosta. FLOWN-aineistoa on kehitetty yhteistyössä Etlan kanssa: Maliranta, M. and S. Nurmi (2019). Business Owners, Employees and Firm Performance. Small Business Economics 52(1) (ETLA Working Papers No. 42).
https://www.etla.fi/julkaisut/business-owners-employees-and-firm-performance/

FIRM-osiota ei päivitetä. Omistajien ketjuttaminen on mahdollista erillisellä stata-koodilla, joka on saatavissa FLOWN-valmisaineiston yhteydessä. Yrityksen henkilöstön ominaisuudet ja henkilö-yritys-linkit ovat erikseen saatavissa FOLK-valmisaineistomoduuleista. Yritysten ja toimipaikkojen tietoja on saatavissa FIRM-valmisaineistomoduuleista.
 
Muista yksikkötason tiedoista poiketen kynnyssääntönä FLOWN-aineiston tietoja julkaistaessa on vähintään 5 havaintoa/luokka. Erityistä huomiota on kiinnitettävä siihen, että suojaus tehdään henkilö- ja yritystasolla siten, että sekä henkilöitä että yrityksiä on oltava julkaistavissa luokissa tietojen taustalla vähintään kynnysarvon verran.

Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@stat.fi.

## Variables (21)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `syrtun` | Suojattu yritystunnus | — | — | — |
| `vuosi` | Vuosi | — | — | — |
| `somtun_hlo` | Suojattu henkilöomistajan tunnus | — | — | — |
| `omosuus` | Omistusosuus | — | — | — |
| `ketj1` | Ketjutus1 | — | — | — |
| `ketj2` | Ketjutus2 | — | — | — |
| `omryh` | Omistusryhmä | — | — | — |
| `yroik` | Yrityksen oikeudellinen muoto | — | — | — |
| `yrhenk` | Yrityksen henkilöstö | — | — | — |
| `yrlv` | Yrityksen liikevaihto | — | — | — |
| `yrjal` | Yrityksen jalostusarvo | — | — | — |
| `yrtol08` | Yrityksen toimiala | — | — | — |
| `omsyrtun` | Omistajan yritys vuoden lopussa | — | — | — |
| `omstpitun` | Omistajan kunta/valtiotunnus vuoden lopussa | — | — | — |
| `omsykstun` | Omistajan toimipaikka vuoden lopussa | — | — | — |
| `omkoul` | Omistajan koulutus | — | — | — |
| `omsp` | Omistajan sukupuoli | — | — | — |
| `omika` | Omistajan ikä | — | — | — |
| `omamas` | Omistajan ammattiasema | — | — | — |
| `omptoim` | Omistajan pääasiallinen toiminta | — | — | — |
| `omsen` | Omistajan senioriteetti | — | — | — |

### Variable definitions

#### `syrtun` — Suojattu yritystunnus

Yrityskehikko on osakasdatasta, mukana vain yritykset, joille on löytynyt vähintään 1 henkilöomistaja

#### `vuosi` — Vuosi

#### `somtun_hlo` — Suojattu henkilöomistajan tunnus

Suojattu henkilöomistajan tunnus, henkilönumero. Vain tiedetyt henkilöomistajat korkeintaan kahden ketjun päähän.

#### `omosuus` — Omistusosuus

Henkilöomistajan omistusosuus (ketjutuksessa omistusosuudet kerrottu) Jakajana käytetty ilmoitettujen osakkeiden lukumäärää yhteensä, jos se on suurempi kuin osakekanta.

#### `ketj1` — Ketjutus1

Jos omistaja on yhtiömuotoinen, henkilöomistajaa on haettu yhtiön taustalta yhden tai kahden omistusportaan päähän. Ketjutus1 saa arvon =1, jos henkilö löytynyt yhden omistusportaan päästä. Jos ketjutus1 saa arvon >1, sama henkilö on löytynyt useamman kuin yhden yhtiön takaa.

#### `ketj2` — Ketjutus2

Jos omistaja on yhtiömuotoinen, henkilöomistajaa on haettu yhtiön taustalta yhden tai kahden omistusportaan päähän. Ketjutus2 saa arvon =1, jos henkilö löytynyt kahden omistusportaan päästä. Jos ketjutus2 saa arvon >1, sama henkilö on löytynyt useamman kuin yhden yhtiön takaa.

#### `omryh` — Omistusryhmä

Omistusryhmä omistuksen hajautumisen mukaan (huomioitu vain tiedetyt henkilöomistajat)
		1= yksi pääasiallinen henkilöomistaja, joka omistaa yli 50%
		2= yksi henkilöomistaja, joka omistaa 10-50%
		3= kaksi henkilöomistajaa, joista kukin omistaa 10-50%
		4= 3-10 henkilöomistajaa, joista kukin omistaa 10-50%
		5= muut

#### `yroik` — Yrityksen oikeudellinen muoto

#### `yrhenk` — Yrityksen henkilöstö

Yrityksen henkilöstön lukumäärä

#### `yrlv` — Yrityksen liikevaihto

#### `yrjal` — Yrityksen jalostusarvo

#### `yrtol08` — Yrityksen toimiala

Toimialaluokituksen 2008 mukainen toimiala

#### `omsyrtun` — Omistajan yritys vuoden lopussa

Omistajan työnantajayritys (TVM=vuoden viim. viikon työ/yrittäjäsuhde) vuoden lopussa

#### `omstpitun` — Omistajan kunta/valtiotunnus vuoden lopussa

Omistajan kunta/valtiotyönantajan tunnus (TVM) vuoden lopussa

#### `omsykstun` — Omistajan toimipaikka vuoden lopussa

Omistajan toimipaikka (TVM) vuoden lopussa

#### `omkoul` — Omistajan koulutus

Omistajan tutkintokoodi, kyseisen vuoden koulutusluokitus ktutk (koulutuskoodi on tyhjä, jos henkilöllä ei ole peruskoulun jälkeistä tutkintoa). Vuonna 2016 erikoisammattitutkinnot 4-numerolla alkavia.

#### `omsp` — Omistajan sukupuoli

#### `omika` — Omistajan ikä

#### `omamas` — Omistajan ammattiasema

Omistajan ammattiasema (TVM)

#### `omptoim` — Omistajan pääasiallinen toiminta

Omistajan pääasiallinen toiminta (TVM)

#### `omsen` — Omistajan senioriteetti

Omistajan senioriteetti/työkokemus kyseisen vuoden lopun TVM- työ/yrittäjäsuhteessa (kk)

---

[← Back to catalogue](../../README.md)
