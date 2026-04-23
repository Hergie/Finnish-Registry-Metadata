# TAX_BENEFIT Tulorekisterin etuustiedot (Report)

- **Identifier:** `TAX_BENEFIT_jua_report_002.xml`
- **DOI:** `work_2020-08_2020-08-18_ain_0001`
- **Temporal coverage:** 2021-01-01 - 
- **Published:** 2026-01-23
- **Organisation:** Tilastokeskus
- **Variable count:** 18
- **Observation count:** —
- **Population:** Suomessa maksetut etuudet ja eläkkeet
- **Source:** Tulorekisteri
- **Keywords:** maksetut tulonsiirrot,saadut tulonsiirrot,tulonsiirrot

## Description

Tulorekisteri on Verohallinnon ylläpitämä kansallinen sähköinen tietokanta, joka sisältää henkilöiden reaaliaikaiset, maksukohtaiset palkka-, eläke- ja etuustiedot. Eläke- ja etuustietoja on ilmoitettu tulorekisteriin vuoden 2021 alusta lähtien. Palkkatietoja on ilmoitettu jo vuoden 2019 alusta lähtien, ja ne on koottu Tilastokeskuksessa TAX_INCOMES-valmisaineistoon. Eläke- ja etuustiedoista on muodostettu tutkimuskäyttöön TAX_BENEFIT-valmisaineisto, joka päivittyy kuukausittain. Tiedot voivat päivittyä myös takautuvasti.

Valmisaineiston sisällössä, kuvauksissa ja käyttöopastuksessa saattaa olla puutteita. Valmisaineisto on tarkoitettu kokeneemmille käyttäjille.

Tähän valmisaineistoon on poimittu ei-arkaluonteiset tulolajit ja niistä tehdyt vähennykset. Ei-arkaluonteisiksi katsottuja tulolajeja ovat lapsiperheiden etuudet ja kotihoidon tuki, opintoetuudet, työttömyysetuudet, vanhuuseläkkeet, muut eläkkeet, valikoidut muut etuudet ja suoritukset (tarkemmin muuttujakuvauksessa), rintamalisät sekä vähennettävät erät. Nämä tulolajit kattavat yli 90 % kaikista tammi-huhtikuussa maksetuista etuuksista. Tulolajien luokitukset ja tuloista vähennettävät erät on selitetty tulorekisterin ohjeissa (linkki alempana). Tietoja valmisaineiston ulkopuolelle jäävistä tulolajeista on mahdollista saada käyttöönsä räätälöityinä aineistoina.

Valmisaineisto sisältää tarkat etuusilmoitustiedot maksajan ja saajan mukaan maksupäivittäin ja tulolajeittain. Maksajien ja saajien suorat tunnisteet on suojattu. Aineisto sisältää tietoja vain voimassa olevista etuusilmoituksista, eli korvatut ja mitätöidyt ilmoitukset on jätetty pois. Tiedot on pilkottu tiedostoihin kuukausittain maksupäivän mukaan. Tiedot on ilmoitettava tulorekisteriin 5 päivän sisällä maksupäivästä, mutta ilmoittamista voi tapahtua myös viiveellä.

Valmisaineiston TAX_BENEFIT tiedot jakaantuvat neljään tauluun:

- Delivery-taulu sisältää aineistotason tietoja (tammi-huhtikuun aineisto n. 113 000 riviä). ”Aineisto” tarkoittaa tässä kokoelmaa etuusilmoituksia, jotka toimitetaan yhdessä tulorekisteriin. Aineistotason tietoja ovat esim. maksupäivä ja maksajan tunniste.
- Report-tauluun on koottu ilmoitustason tietoja (tammi-huhtikuun aineisto n. 20 milj. riviä). Ilmoituksessa on tietoja etuuden saajasta, kuten hänen asuinvaltiostaan ja verovelvollisuudestaan. Yhdellä ilmoituksella voi olla montaa eri tulolajia (ks. seuraava taulu).
- TransactionInfo-taulussa on tietoja ilmoitetuista tulolajeista (tammi-huhtikuun aineisto n. 34 milj. riviä). Yksi rivi vastaa yhtä tulolajia, joka sisältyy täsmälleen yhteen ilmoitukseen. Tulolajitason tietoja ovat esim. tulolajin koodi, etuuden määrä, veronalaisuus ja ansaintakausi.
- Deduction-taulu sisältää tulolajeista tehtävät vähennykset eli sijaissaajalle suoritettavat osuudet (tammi-huhtikuun aineisto n. 1,2 milj. riviä). Vähennystason tietoja ovat vähennyksen tulolajin koodi, vähennyksen määrä, alkuperäisen suorituksen maksupäivä ja sijaissaajan tiedot.

Taulut ovat yhdistettävissä id-tunnisteiden avulla. Tunnisteet kytkeytyvät toisiinsa seuraavasti:

- delivery.delId = report.delId
- report.repId = transactionInfo.repId
- transactionInfo.trxId = deduction.trxId

Vähennyksen tulolaji noudattaa samaa luokitusta kuin se tulolaji (’transaktio’), josta vähennys tehdään. Tulolajiltaan arkaluonteisten vähennysten tulolajikoodit ja sijaissaajan tiedot on peitetty. Huomaathan, että koska moduuli kattaa vain ei-arkaluontoisista tulolajeista (transaktioista) tehdyt vähennykset, arkaluontoisten tulolajien ei-arkaluontoiset vähennykset jäävät ulkopuolelle.

Tulorekisterin etuustietoja julkaistaessa on noudatettava henkilöissä/edunsaajissa kynnyssääntöä (10) ja maksajissa kynnyssääntöä (3) sekä lisäksi dominanssisääntöä (1,75). Yhdistetyissä aineistoissa on suojattava sekä henkilö- että maksajataso eli kussakin taulukon solussa on oltava saajia vähintään kolmesta eri yrityksestä tai muusta maksajasta. Dominanssisääntöä on käytettävä esimerkiksi, jos yhden yrityksen tai muun maksajan maksama etuussumma muodostaa yli 75 prosenttia tietyn toimialan (sektorin tms.) etuussummasta.

Ohessa on lyhyesti kuvattu Tilastokeskuksen aineistoon sisällytetyt muuttujat luokituksineen. Tarkemmat tiedot, kuten tietosisältö ja tulolajien selitteet ja koodistot  löytyvät tulorekisterin sivuilta:
https://www.vero.fi/tulorekisteri/ohjelmistokehitt%C3%A4j%C3%A4t/dokumentaatio/

Lisätietoja Tilastokeskuksen valmisaineistosta saa Tutkijapalveluista: tutkijapalvelut@stat.fi

## Variables (18)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `repId` | Ilmoituksen tunniste | — | — | — |
| `delId` | Aineiston tunniste | — | — | — |
| `IncomeEarnerHid_e` | Suojattu tulonsaajan yksilöivä tunniste | — | — | — |
| `incomeEarnerSyrtun` | Tulonsaajan suojattu y-tunnus | — | — | tulonsaajan tunnisteet |
| `incomeEarnerOtherSId` | Tulonsaajan suojattu muu tunniste | — | — | tulonsaajan tunnisteet |
| `IncomeEarnerOtherIdCode_s` | Tulonsaajan suojattu muu tunniste | — | — | — |
| `incomeEarnerIdType` | Tulonsaajan tunnisteen tyyppi | — | — | tulonsaajan tunnisteet |
| `reportVersion` | Ilmoituksen versionumero | — | — | — |
| `latauspvm` | Aineiston poimintapäivämäärä tulorekisteristä | — | — | — |
| `incomeEarnerIdCountryCode` | Maakoodi | — | — | tulonsaajan tunnisteet |
| `incomeEarnerIdCountryName` | Maan nimi | — | — | tulonsaajan tunnisteet |
| `IncomeEarnerHidType` | Tulonsaajan henkilötunnisteen tyyppi | — | — | — |
| `nonResident` | Rajoitetusti verovelvollinen | — | — | kansainväliset tilanteet |
| `nonResidentCountryCode` | Asuinvaltion maakoodi | — | — | kansainväliset tilanteet |
| `nonResidentCountryName` | Asuinvaltion nimi | — | — | kansainväliset tilanteet |
| `subToWithold` | Ennakonpidätyksen alainen tulo | — | — | kansainväliset tilanteet |
| `receivedTimestamp` | receivedTimestamp | — | — | — |
| `createdTimestamp` | createdTimestamp | — | — | — |

### Variable definitions

#### `repId` — Ilmoituksen tunniste

Tunniste on muodostettu Tilastokeskuksessa taulun luomisen yhteydessä. Ilmoitus ja sen sisältämät tulolajit ovat yhdistettävissä toisiinsa ilmoituksen tunnisteen avulla (report.repId = transactionInfo.repId).

Pakollisuus (K/E) = K

#### `delId` — Aineiston tunniste

Yksilöi aineiston, johon ilmoitus sisältyy. Aineisto ja sen sisältämät ilmoitukset ovat yhdistettävissä toisiinsa aineiston tunnisteen avulla (delivery.delId = report.delId).

Pakollisuus (K/E) = K

#### `IncomeEarnerHid_e` — Suojattu tulonsaajan yksilöivä tunniste

Suojattu tulonsaajan yksilöivä tunniste

#### `incomeEarnerSyrtun` — Tulonsaajan suojattu y-tunnus

**Group:** tulonsaajan tunnisteet

Tulonsaajan suojattu y-tunnus (suojattu ilman väliviivaa)

#### `incomeEarnerOtherSId` — Tulonsaajan suojattu muu tunniste

**Group:** tulonsaajan tunnisteet

Tulonsaajan suojattu muu tunniste, y-tunnuksesta on poistettu viiva ennen suojausta. Tätä muuttujaa ei suositella vielä käytettävän linkkauksissa, koska muuttujan suojaus on ollut sikäli virheellinen, etteivät kaikki alkuperäiset tunnukset ole saaneet oikein yksilöityvää suojattua tunnusta.

#### `IncomeEarnerOtherIdCode_s` — Tulonsaajan suojattu muu tunniste

#### `incomeEarnerIdType` — Tulonsaajan tunnisteen tyyppi

**Group:** tulonsaajan tunnisteet

1 = Y-tunnus (suomalainen)
2 = Henkilötunnus (suomalainen)
5 = Verotunniste (TIN)
9 = Ulkomainen henkilötunnus
99 = Muu tunnus

https://www.vero.fi/globalassets/tulorekisteri/dokumentaatio-2021/koodistot-20212.pdf (§ 1.15)

#### `reportVersion` — Ilmoituksen versionumero

Etuuden maksaja voi korvata tai mitätöidä aikaisemman ilmoituksensa, jolloin syntyy uusi versio ilmoituksesta. Halutessaan hän voi eritellä lähettämänsä korjaukset tai mitätöinnit versionumeron avulla, jolloin varmistetaan, että korjaaminen tai mitätöinti kohdistuu oikeaan ilmoitukseen. Tähän aineistoon on otettu kustakin ilmoituksesta vain viimeisin versio.

#### `latauspvm` — Aineiston poimintapäivämäärä tulorekisteristä

Tarkoittaa sitä hetkeä, jolloin Tilastokeskus on poiminut aineiston tulorekisteristä.

Pakollisuus (K/E) = K

#### `incomeEarnerIdCountryCode` — Maakoodi

**Group:** tulonsaajan tunnisteet

Jos tunnisteen tyyppinä on muu kuin suomalainen henkilötunnus, merkitään tulonsaajan tunnisteen myöntäneen maan koodi. Tunnisteen myöntänyt maa voi olla eri kuin tulonsaajan asuinvaltio. Maakoodi valitaan koodistosta:

https://www.vero.fi/globalassets/tulorekisteri/dokumentaatio-2021/koodistot-20212.pdf (§ 1.59)

#### `incomeEarnerIdCountryName` — Maan nimi

**Group:** tulonsaajan tunnisteet

Merkitään tunnisteen myöntäneen maan nimi, jos maakoodiksi on annettu arvo ”tuntematon” (99).

#### `IncomeEarnerHidType` — Tulonsaajan henkilötunnisteen tyyppi

1 = Y-tunnus (suomalainen)
2 = Henkilötunnus (suomalainen)
5 = Verotunniste (TIN)
9 = Ulkomainen henkilötunnus
99 = Muu tunnus

https://www.vero.fi/globalassets/tulorekisteri/dokumentaatio-2021/koodistot-20212.pdf (§ 1.15)
Joissakin tapauksissa saajalla voi olla kaksi erityyppistä tunnistetta.

#### `nonResident` — Rajoitetusti verovelvollinen

**Group:** kansainväliset tilanteet

”Kyllä” (true) tai tyhjä

#### `nonResidentCountryCode` — Asuinvaltion maakoodi

**Group:** kansainväliset tilanteet

Rajoitetusti verovelvollisesta on ilmoitettava sen valtion maatunnus, jota pidetään tulonsaajan asuinpaikkana. Maakoodi valitaan koodistosta:

https://www.vero.fi/globalassets/tulorekisteri/dokumentaatio-2021/koodistot-20212.pdf (§ 1.59)

#### `nonResidentCountryName` — Asuinvaltion nimi

**Group:** kansainväliset tilanteet

Merkitään asuinvaltion nimi, jos asuinvaltion maakoodin arvoksi on annettu ”tuntematon” (99).

#### `subToWithold` — Ennakonpidätyksen alainen tulo

**Group:** kansainväliset tilanteet

”Kyllä” (true) tai tyhjä

#### `receivedTimestamp` — receivedTimestamp

#### `createdTimestamp` — createdTimestamp

---

[← Back to catalogue](../../README.md)
