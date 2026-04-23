# TAX_BENEFIT Tulorekisterin etuustiedot (Delivery)

- **Identifier:** `TAX_BENEFIT_jua_delivery_002.xml`
- **DOI:** `work_2020-08_2020-08-18_ain_0001`
- **Temporal coverage:** 2021-01-01 - 
- **Published:** 2025-11-11
- **Organisation:** Tilastokeskus
- **Variable count:** 4
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

## Variables (4)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `delId` | Aineiston tunniste | — | — | — |
| `payerIdType1_s` | Etuuden maksajan suojattu y-tunnus | — | — | — |
| `latauspvm` | Aineiston poimintapäivämäärä tulorekisteristä | — | — | — |
| `paymentDate` | Suorituksen maksupäivä tai muu ilmoituspäivä | — | — | — |

### Variable definitions

#### `delId` — Aineiston tunniste

Tunniste on muodostettu Tilastokeskuksessa taulun luomisen yhteydessä. Aineisto ja sen sisältämät ilmoitukset ovat yhdistettävissä toisiinsa aineiston tunnisteen avulla (delivery.delId = report.delId).

Pakollisuus (K/E) = K

#### `payerIdType1_s` — Etuuden maksajan suojattu y-tunnus

#### `latauspvm` — Aineiston poimintapäivämäärä tulorekisteristä

Tarkoittaa sitä hetkeä, jolloin Tilastokeskus on poiminut aineiston tulorekisteristä.

Pakollisuus (K/E) = K

#### `paymentDate` — Suorituksen maksupäivä tai muu ilmoituspäivä

Suorituksen maksupäivä on päivä, jolloin suoritus on tulonsaajan käytettävissä, esimerkiksi merkitty tulonsaajan pankkitilille. Muu ilmoituspäivä voi tulla kyseeseen esimerkiksi takaisinperintätilanteissa. Aineiston poiminta ja ajallinen jaottelu on tehty Tilastokeskuksessa tämän päivämäärän perusteella.

Pakollisuus (K/E) = K

---

[← Back to catalogue](../../README.md)
