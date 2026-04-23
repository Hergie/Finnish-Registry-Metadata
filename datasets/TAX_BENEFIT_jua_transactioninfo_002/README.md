# TAX_BENEFIT Tulorekisterin etuustiedot (Transaction info)

- **Identifier:** `TAX_BENEFIT_jua_transactioninfo_002.xml`
- **DOI:** `work_2020-08_2020-08-18_ain_0001`
- **Temporal coverage:** 2021-01-01 - 
- **Published:** 2025-11-11
- **Organisation:** Tilastokeskus
- **Variable count:** 27
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

## Variables (27)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `trxId` | Tulolajin tunniste | — | — | — |
| `repId` | Ilmoituksen tunniste | — | — | — |
| `txno` | Tulolajin numero | — | — | — |
| `transactionCode` | Tulolajin koodi | — | — | tulolajin yleistiedot |
| `retroactiveTransactionCode` | Tulolaji muuttunut, uusi tulolajin koodi | — | — | tulolajin yleistiedot |
| `amount` | Määrä | € | — | tulolajin yleistiedot |
| `taxTreatment` | Etuuden veronalaisuus | — | — | tulolajin yleistiedot |
| `oneOff` | Kertakorvaus | — | — | tulolajin yleistiedot |
| `unjustEnrichment` | Perusteeton etu | — | — | tulolajin yleistiedot |
| `recovery` | Takaisinperintä | — | — | tulolajin yleistiedot |
| `unpromptedRefund` | Oma-aloitteinen palautus | — | — | tulolajin yleistiedot |
| `delayIncrease` | Viivästyskorotus | — | — | tulolajin yleistiedot |
| `recourse` | Regressi | — | — | tulolajin yleistiedot |
| `paymentReallocation` | Maksun oikaisu | — | — | tulolajin yleistiedot |
| `noTaxEffect` | Ei vaikuta verotukseen | — | — | tulolajin yleistiedot |
| `earningPeriodStartDate` | Alkupäivä | — | — | ansaintakausi |
| `earningPeriodEndDate` | Loppupäivä | — | — | ansaintakausi |
| `benefitUnitCode` | Yksikkö | — | — | etuuden yksikkö |
| `benefitUnitAmount` | Yksiköiden määrä | — | — | etuuden yksikkö |
| `recoveryDate` | Takaisinmaksupäivä | — | — | takaisinmaksun lisätiedot |
| `recoveryWithhold` | Takaisinmaksuun kohdistuva ennakonpidätys | € | — | takaisinmaksun lisätiedot |
| `recoveryTaxAtSource` | Takaisinmaksuun kohdistuva lähdevero | € | — | takaisinmaksun lisätiedot |
| `origPaymentDate` | Suorituksen maksupäivä tai muu ilmoituspäivä | — | — | alkuperäinen ansaintakausi |
| `origStartDate` | Alkupäivä | — | — | alkuperäinen ansaintakausi |
| `origEndDate` | Loppupäivä | — | — | alkuperäinen ansaintakausi |
| `recoursePaymentDate` | Regressi verottomasta tulosta, maksupäivä | — | — | regressin lisätiedot |
| `NonresidentPensionBasis` | Rajoitetusti verovelvolliselle maksetun eläkkeen peruste | — | — | tulolajin lisätiedot |

### Variable definitions

#### `trxId` — Tulolajin tunniste

Tunniste on muodostettu Tilastokeskuksessa taulun luomisen yhteydessä. Tulolaji ja siitä tehdyt vähennykset ovat yhdistettävissä toisiinsa tulolajin tunnisteen avulla (transactionInfo.trxId = deduction.trxId).

Pakollisuus (K/E) = K

#### `repId` — Ilmoituksen tunniste

Yksilöi ilmoituksen, johon tulolaji sisältyy. Ilmoitus ja sen sisältämät tulolajit ovat yhdistettävissä toisiinsa ilmoituksen tunnisteen avulla (report.repId = transactionInfo.repId).

Pakollisuus (K/E) = K

#### `txno` — Tulolajin numero

Samalla ilmoituksella olevien tulolajien juokseva järjestysnumero

#### `transactionCode` — Tulolajin koodi

**Group:** tulolajin yleistiedot

Päämoduuli sisältää seuraaviin luokkiin kuuluvat tulolajit:

Lapsiperheiden etuudet ja kotihoidon tuki
Opintoetuudet
Työttömyysetuudet
Vanhuuseläkkeet
Muut eläkkeet
Muut etuudet ja suoritukset*
Rintamalisät
Vähennettävät erät

*Muut etuudet ja suoritukset seuraavien tulolajien osalta:

Vuorottelukorvaus (Kela)
Vuorottelukorvaus (työttömyyskassat)
Eläkkeensaajan asumistuki
Yleinen asumistuki
Starttiraha (Laki julkisesta työvoima- ja yrityspalvelusta)
Yleinen asumistuki (Ahvenanmaan maakunta)
Päiväraha (Ahvenanmaan maakunta)
Osa-aikaeläke (ryhmäeläkevakuutus)
Eläke (yksityishenkilön ottama vapaaehtoinen yksilöllinen eläkevakuutus)
Eläke (työnantajan ottama vapaaehtoinen yksilöllinen eläkevakuutus)
Eläke (kertamaksullinen vapaaehtoinen eläkevakuutus)
Osa-aikaeläke (vapaaehtoinen työeläkevakuutus)
Työttömyyseläke (yksityishenkilön ottama vapaaehtoinen yksilöllinen eläkevakuutus)
Työttömyyseläke (työnantajan ottama vapaaehtoinen yksilöllinen eläkevakuutus)

Muut kuin edellä määritellyt tulolajit on katsottu arkaluonteisiksi ja siksi rajattu päämoduulin ulkopuolelle.

Katso tulolajien tarkat koodit ja niiden selitteet tulorekisterin sivuilta:

https://www.vero.fi/globalassets/tulorekisteri/dokumentaatio-2021/koodistot-20212.pdf
https://www.vero.fi/globalassets/tulorekisteri/dokumentaatio-2021/etuudet-tulolajien-ja-tuloista-vahennettavien-erien-selitteet-2021.pdf

#### `retroactiveTransactionCode` — Tulolaji muuttunut, uusi tulolajin koodi

**Group:** tulolajin yleistiedot

Uusi tulolajin koodi noudattaa samaa koodistoa kuin alkuperäinen (transactionCode). Rivit, joilla uusi tulolajin koodi on arkaluonteinen (= ei sisälly transactionCode-muuttujan kuvauksessa määriteltyihin luokkiin), on jätetty aineiston ulkopuolelle.

#### `amount` — Määrä

**Unit:** € · **Group:** tulolajin yleistiedot

#### `taxTreatment` — Etuuden veronalaisuus

**Group:** tulolajin yleistiedot

1 = Ansiotuloa
2 = Ansiotuloa, korotettu 20%
3 = Ansiotuloa, peritään ainoastaan sairaanhoitomaksu
4 = Pääomatuloa
5 = Pääomatuloa, korotettu 20%
6 = Pääomatuloa, korotettu 50%
7 = Verotonta
8 = Verotonta, annetaan perintö- ja lahjaverolain tieto
9 = Pääomatuloa sekä annetaan perintö- ja lahjaverolain tieto

https://www.vero.fi/globalassets/tulorekisteri/dokumentaatio-2021/koodistot-20212.pdf (§ 1.16)

#### `oneOff` — Kertakorvaus

**Group:** tulolajin yleistiedot

”Kyllä” (true) tai tyhjä

#### `unjustEnrichment` — Perusteeton etu

**Group:** tulolajin yleistiedot

”Kyllä” (true) tai tyhjä

#### `recovery` — Takaisinperintä

**Group:** tulolajin yleistiedot

”Kyllä” (true) tai tyhjä

#### `unpromptedRefund` — Oma-aloitteinen palautus

**Group:** tulolajin yleistiedot

”Kyllä” (true) tai tyhjä

#### `delayIncrease` — Viivästyskorotus

**Group:** tulolajin yleistiedot

”Kyllä” (true) tai tyhjä

#### `recourse` — Regressi

**Group:** tulolajin yleistiedot

”Kyllä” (true) tai tyhjä

#### `paymentReallocation` — Maksun oikaisu

**Group:** tulolajin yleistiedot

”Kyllä” (true) tai tyhjä

#### `noTaxEffect` — Ei vaikuta verotukseen

**Group:** tulolajin yleistiedot

”Kyllä” (true) tai tyhjä

#### `earningPeriodStartDate` — Alkupäivä

**Group:** ansaintakausi

Ansaintakauden alkupäivä.

#### `earningPeriodEndDate` — Loppupäivä

**Group:** ansaintakausi

Ansaintakauden loppupäivä.

#### `benefitUnitCode` — Yksikkö

**Group:** etuuden yksikkö

1 = Tunti
2 = Päivä
3 = Viikko
4 = Kuukausi
5 = Neljännesvuosi
6 = Vuosi

https://www.vero.fi/globalassets/tulorekisteri/dokumentaatio-2021/koodistot-20212.pdf (§ 1.17)

#### `benefitUnitAmount` — Yksiköiden määrä

**Group:** etuuden yksikkö

#### `recoveryDate` — Takaisinmaksupäivä

**Group:** takaisinmaksun lisätiedot

#### `recoveryWithhold` — Takaisinmaksuun kohdistuva ennakonpidätys

**Unit:** € · **Group:** takaisinmaksun lisätiedot

#### `recoveryTaxAtSource` — Takaisinmaksuun kohdistuva lähdevero

**Unit:** € · **Group:** takaisinmaksun lisätiedot

#### `origPaymentDate` — Suorituksen maksupäivä tai muu ilmoituspäivä

**Group:** alkuperäinen ansaintakausi

Alkuperäinen suorituksen maksupäivä tai muu ilmoituspäivä.

#### `origStartDate` — Alkupäivä

**Group:** alkuperäinen ansaintakausi

Alkuperäisen ansaintakauden alkupäivä.

#### `origEndDate` — Loppupäivä

**Group:** alkuperäinen ansaintakausi

Alkuperäisen ansaintakauden loppupäivä.

#### `recoursePaymentDate` — Regressi verottomasta tulosta, maksupäivä

**Group:** regressin lisätiedot

#### `NonresidentPensionBasis` — Rajoitetusti verovelvolliselle maksetun eläkkeen peruste

**Group:** tulolajin lisätiedot

1 = Muussa kuin liiketoiminnassa ansaittu julkisyhteisön maksama työeläke
2 = Liiketoiminnassa ansaittu julkisyhteisön maksama työeläke
3 = Kansaneläkelaitoksen tai Valtiokonttorin maksama muu kuin työeläke
4 = Muu sosiaaliturvalainsäädäntöön perustuva suoritus
5 = Muu kuin sosiaaliturvalainsäädäntöön perustuva suoritus

https://www.vero.fi/globalassets/tulorekisteri/dokumentaatio-2021/koodistot-20212.pdf (§ 1.41)

---

[← Back to catalogue](../../README.md)
