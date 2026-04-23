# TAX_BENEFIT Tulorekisterin etuustiedot (Deduction)

- **Identifier:** `TAX_BENEFIT_jua_deduction_002.xml`
- **DOI:** `work_2020-08_2020-08-18_ain_0001`
- **Temporal coverage:** 2021-01-01 - 
- **Published:** 2026-01-23
- **Organisation:** Tilastokeskus
- **Variable count:** 19
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

## Variables (19)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `dedId` | Vähennyksen tunniste | — | — | — |
| `trxId` | Tulolajin tunniste | — | — | — |
| `txno` | Tulolajin numero | — | — | — |
| `rivino` | Rivinumero | — | — | — |
| `deductionTransactionCode` | Vähennyksen tulolajin koodi | — | — | vähennyksen tiedot |
| `deductionType` | Vähennyksen tyyppi | — | — | vähennyksen tiedot |
| `amount` | Vähennyksen määrä | € | — | vähennyksen tiedot |
| `origPaymentDate` | Suorituksen maksupäivä tai muu ilmoituspäivä | — | — | alkuperäisen etuuden ansaintakausi |
| `origStartDate` | Alkupäivä | — | — | alkuperäisen etuuden ansaintakausi |
| `origEndDate` | Loppupäivä | — | — | alkuperäisen etuuden ansaintakausi |
| `incomeBeneficiaryIdType` | Sijaissaajan tunnisteen tyyppi | — | — | sijaissaajan tunnisteet |
| `incomeBeneficiaryIdCountryCode` | Maakoodi | — | — | sijaissaajan tunnisteet |
| `incomeBeneficiaryIdCountryName` | Maan nimi | — | — | sijaissaajan tunnisteet |
| `incomeBeneficiaryHidType` | Sijaissaajan henkilötunnisteen tyyppi | — | — | — |
| `remittanceStartDate` | Alkupäivä | — | — | tilitysjakso |
| `remittanceEndDate` | Loppupäivä | — | — | tilitysjakso |
| `incomeBeneficiaryHid_e` | Suojattu sijaissaajan yksilöivä tunniste | — | — | — |
| `IncomeBeneficiaryIdCode_s` | Sijaissaajan suojattu y-tunnus | — | — | — |
| `IncomeBeneficiaryOtherIdCode_s` | Sijaissaajan suojattu muu tunniste | — | — | — |

### Variable definitions

#### `dedId` — Vähennyksen tunniste

Tunniste on muodostettu Tilastokeskuksessa taulun luomisen yhteydessä.

Pakollisuus (K/E) = K

#### `trxId` — Tulolajin tunniste

Yksilöi tulolajin, josta vähennys tehdään. Tulolaji ja siitä tehdyt vähennykset ovat yhdistettävissä toisiinsa tulolajin tunnisteen avulla (transactionInfo.trxId = deduction.trxId).

Pakollisuus (K/E) = K

#### `txno` — Tulolajin numero

Samalla ilmoituksella olevien tulolajien juokseva järjestysnumero

#### `rivino` — Rivinumero

Samasta tulolajista tehtyjen vähennysten juokseva järjestysnumero

#### `deductionTransactionCode` — Vähennyksen tulolajin koodi

**Group:** vähennyksen tiedot

Vähennyksen tulolajin koodilla ilmoitetaan tieto alkuperäisestä tulolajista, jota vähennys koskee. Koodisto on sama kuin transactionInfo-taulussa (ks. transactionCode-muuttujan kuvaus). Vähennyksissä, joiden tulolajin koodi on arkaluonteinen (= ei sisälly transactionCode-muuttujan kuvauksessa määriteltyihin luokkiin), tulolajin koodi ja sijaissaajan tiedot on peitetty (= tyhjennetty).

#### `deductionType` — Vähennyksen tyyppi

**Group:** vähennyksen tiedot

1 = Elatusapuvelan perintä
2 = Maksun oikaisu nettotulosta
3 = Maksun oikaisu veronalaisesta tulosta
4 = Maksuvaatimus (ei regressitilanne)
5 = MATA- ja MYEL-perintä
6 = Muu vähennys nettotulosta
7 = Muu vähennys veronalaisesta tulosta
8 = Palkansaajamaksujen vähennys
9 = Panttioikeuteen perustuva vähennys
10 = Regressi veronalaiseen tuloon
11 = Regressi verottomaan tuloon
12 = Opintolainan takaussaatavan perintä
13 = YEL-perintä

#### `amount` — Vähennyksen määrä

**Unit:** € · **Group:** vähennyksen tiedot

#### `origPaymentDate` — Suorituksen maksupäivä tai muu ilmoituspäivä

**Group:** alkuperäisen etuuden ansaintakausi

Alkuperäisen suorituksen maksupäivä.

#### `origStartDate` — Alkupäivä

**Group:** alkuperäisen etuuden ansaintakausi

Alkuperäisen ansaintakauden alkupäivä.

#### `origEndDate` — Loppupäivä

**Group:** alkuperäisen etuuden ansaintakausi

Alkuperäisen ansaintakauden loppupäivä.

#### `incomeBeneficiaryIdType` — Sijaissaajan tunnisteen tyyppi

**Group:** sijaissaajan tunnisteet

1 = Y-tunnus (suomalainen)
2 = Henkilötunnus (suomalainen)
3 = Alv-tunniste (VAT)
4 = GIIN-tunniste
5 = Verotunniste (TIN)
6 = Kaupparekisteritunnus
7 = Ulkomainen yritystunnus
9 = Ulkomainen henkilötunnus
99 = Muu tunnus

#### `incomeBeneficiaryIdCountryCode` — Maakoodi

**Group:** sijaissaajan tunnisteet

Jos tunnisteen tyyppinä on muu kuin Y-tunnus tai suomalainen henkilötunnus, merkitään tunnisteen myöntäneen maan koodi. Maakoodi valitaan koodistosta:

https://www.vero.fi/globalassets/tulorekisteri/dokumentaatio-2021/koodistot-20212.pdf

#### `incomeBeneficiaryIdCountryName` — Maan nimi

**Group:** sijaissaajan tunnisteet

Merkitään tunnisteen myöntäneen maan nimi, jos maakoodiksi on annettu arvo ”tuntematon” (99).

#### `incomeBeneficiaryHidType` — Sijaissaajan henkilötunnisteen tyyppi

1 = Y-tunnus (suomalainen)
2 = Henkilötunnus (suomalainen)
3 = Alv-tunniste (VAT)
4 = GIIN-tunniste
5 = Verotunniste (TIN)
6 = Kaupparekisteritunnus
7 = Ulkomainen yritystunnus
9 = Ulkomainen henkilötunnus
99 = Muu tunnus
Joissakin tapauksissa saajalla voi olla kaksi erityyppistä tunnistetta.

#### `remittanceStartDate` — Alkupäivä

**Group:** tilitysjakso

Sijaissaajalle tilitettävän jakson alkupäivä.

#### `remittanceEndDate` — Loppupäivä

**Group:** tilitysjakso

Sijaissaajalle tilitettävän jakson loppupäivä.

#### `incomeBeneficiaryHid_e` — Suojattu sijaissaajan yksilöivä tunniste

Suojattu sijaissaajan yksilöivä tunniste

#### `IncomeBeneficiaryIdCode_s` — Sijaissaajan suojattu y-tunnus

#### `IncomeBeneficiaryOtherIdCode_s` — Sijaissaajan suojattu muu tunniste

---

[← Back to catalogue](../../README.md)
