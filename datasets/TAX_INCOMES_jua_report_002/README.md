# TAX_INCOMES Tulorekisterin palkkatiedot (Report)

- **Identifier:** `TAX_INCOMES_jua_report_002.xml`
- **DOI:** `work_2020-08_2020-08-18_ain_0001`
- **Temporal coverage:** 2019-01-01 - 
- **Published:** 2026-01-23
- **Organisation:** Tilastokeskus
- **Variable count:** 55
- **Observation count:** —

## Kuvaus / Description

Tulorekisteri on Verohallinnon ylläpitämä kansallinen sähköinen tietokanta, joka sisältää henkilöiden reaaliaikaiset, maksukohtaiset palkka-, eläke- ja etuustiedot. Eläke- ja etuustietoja on ilmoitettu tulorekisteriin vuoden 2021 alusta lähtien. Palkkatietoja on ilmoitettu jo vuoden 2019 alusta lähtien, ja ne on koottu Tilastokeskuksessa TAX_INCOMES-valmisaineistoon. Eläke- ja etuustiedoista on muodostettu tutkimuskäyttöön TAX_BENEFIT-valmisaineisto, joka päivittyy kuukausittain. Tiedot voivat päivittyä myös takautuvasti.

Tutkimuskäyttöön suojattu TAX_INCOMES-valmisaineisto sisältää tarkat tuloilmoitustiedot maksajan ja saajan mukaan maksupäivittäin ja tulolajeittain. Valmisaineisto sisältää tietoja vain voimassa olevista tuloilmoituksista. Aineisto ei sisällä korvattuja ja mitätöityjä ilmoituksia. Tiedot päivittyvät kerran kuussa noin 45 päivän aineistoviiveellä. Tiedot päivittyvät aina 13 kk taaksepäin. Tiedot on pilkottu tiedostoihin kuukausittain maksupäivän mukaan.

Osa tiedoista on pakollisesti ilmoitettavia tietoja ja osa vapaaehtoisesti ilmoitettavia. Vapaaehtoisia tietoja ovat mm. tulolajittaiset palkat (lähes 90% ilmoituksista 2019 lopulla) ja työsuhteen laatuun liittyvät tiedot kuten koko/osa-aikaisuus (n. 40%), kuukausi/tuntipalkka/urakkapalkkaperusteisuus (n. 45%), viikkotyöaika (n. 40%) ja tulokohtaiset tunnit (n. 2%). Ammattitiedoissa on myös puutteita. Tiedot on ilmoitettava tulorekisteriin 5 päivän sisällä maksupäivästä mutta ilmoitusten jättämisessä on käytännössä huomattavia viiveitä, esimerkiksi vuonna 2019 78% palkkatietoilmoituksista annettiin 5 päivän aikana maksupäivästä. 1.1.2020 - 20.3.2020 62,1% palkkatieto-ilmoituksista annettiin ennen maksupäivää ja 21,1% 1-5 päivän aikana maksupäivästä. Työnantajan erillisilmoituksista annettiin 26,8% kohdekauden aikana ja 53,2% 1-5 päivän aikana kohdekaudesta. Jotkut vastaajat ilmoittavat yhdellä ilmoituksella kaikki tiedot ja toiset taas ilmoittavat pelkästään tietyt tulolajit omilla ilmoituksillaan.

Tarkemmat tekniset tiedot muuttujista, sekä tulolajien selitteet: 
https://www.vero.fi/tulorekisteri/ohjelmistokehitt%C3%A4j%C3%A4t/dokumentaatio/#palkkojentietosisalto 

Joitakin muuttujia on Tilastokeskuksessa jaettu omiksi muuttujikseen tyypin mukaan, kuten ammattikoodi. Verohallinnon koodistot:
 https://www.vero.fi/tulorekisteri/ohjelmistokehitt%C3%A4j%C3%A4t/dokumentaatio/#koodistot


Valmisaineiston TAX_INCOMES tiedot jakaantuvat neljään tauluun:

- Delivery-taulu sisältää toimitustason tietoja, poimintahetkellä n. 10 milj. riviä
          Esimerkiksi suojattu yritystunnus, palkanmaksupäivä ja -jakso.
- Report-tauluun on koottu ilmoitustason tietoja, poimintahetkellä n. 50 milj. riviä
          Ilmoituksessa on tietoja tulonsaajasta, mm. ammatti, työaika- ja työsuhdetietoja.
          Poissaolotietoja on aggregoitu ilmoitustasolle ja tästä syystä nämä tiedot eivät ole aina tarkkoja.
- TransactionCode-tauluun on muodostettu tulolajitiedot niin, että yksi ilmoitus vastaa yhtä riviä, poimintahetkellä n. 50 milj. riviä
          Tietoja on aggregoitu ilmoitustasolle, joten kaikkia muuttujia tässä taulussa ei kannata käyttää suoraan.
          Samat tiedot löytyvät tarkemmin eriteltynä myös taulusta transactionInfo.
          Esimerkiksi ansaintajaksoja tai yksikkötietoja käytettäessä poiminta kannattaa tehdä taulusta transactionInfo.
- TransactionInfo-tauluun tulolajitiedot on muodostettu niin, että yksi rivi vastaa yhtä tulolajia, poimintahetkellä n. 300 milj. riviä
          Tarkat tiedot, mutta suuri rivimäärä tekee käytöstä melko raskasta
          Samoja tietoja kuin transactionCode-taulussa, mutta lisämuuttujia ja tarkemmalla erittelyllä
          Esimerkiksi tarkempiin tulolajeihin kohdistuvat palkkasummat (sosiaaliturvamaksun tai sairausvakuutusmaksun alaiset palkat) vaativat tarkempien erittelyiden käyttöä. Lisäksi tietyt määritteet kuten takaisinperintä,vakuuttamistiedon tyyppi 1 ja 3, ravintoedun verotuskorvaus, kuuden kuukauden sääntö,  edun tyyppi jne. vaativat TransactionInfo-taulun käyttöä eli näitä muuttujia koskevat tiedot ovat vaillinaisia TransactionCode-datassa.

Taulut yhdistyvät id-tunnisteilla. Taulujen yhdistäminen tapahtuu seuraavasti: 

-delivery.delID=report.delID 
-report.repID=transactionCode.repID=transactionInfo.repID

Koska aineiston laajuus ja määrä aiheuttavat haasteita tietojen käsittelyyn, tulorekisteri-valmisaineiston tiedot on tarkoitettu kokeneemmille käyttäjille. 

Tulorekisterin tietoja julkaistaessa on noudatettava henkilötiedoissa kynnyssääntöä (10) ja yrityksissä kynnyssääntöä (5) sekä lisäksi dominanssisääntöä (1,75). Yhdistetyissä työntekijä-työnantaja-aineistoissa on suojattava sekä henkilö- että yritystaso eli kussakin taulukon solussa on oltava työntekijöitä vähintään viidestä eri yrityksestä. Dominanssisääntöä on käytettävä esimerkiksi, jos yhden yrityksen palkkasumma muodostaa yli 75 prosenttia tietyn toimialan (sektorin tms.) yritysten palkkasummasta tai jos esim. tietyn ammattiryhmän palkansaajista yli 75 prosenttia työskentelee jossain tietyssä yrityksessä.

Lisätietoja Tilastokeskuksen Tutkijapalveluista: tutkijapalvelut@stat.fi ja Verohallinnon sivuilta: https://www.vero.fi/tulorekisteri/

## Muuttujat / Variables (55)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `repId` | Raportin tunniste | — | — | — |
| `delId` | Toimituksen tunniste | — | — | — |
| `incomeEarnerHid_e` | Suojattu tulonsaajan yksilöivä tunniste | — | — | — |
| `incomeEarnerIdCode_s` | Tulonsaajan suojattu muu tunnus | — | — | — |
| `incomeEarnerIdType` | Tulonsaajan tunnisteen tyyppi | — | — | — |
| `reportVersion` | Ilmoitusversio | — | — | — |
| `latauspvm` | Aineiston poimintapäivämäärä Tulorekisteristä | — | — | — |
| `pensionActCode` | Tieto työeläkevakuutuksesta | — | — | — |
| `pensionProvIdCode_s` | Suojattu työeläkelaitoksen yhtiötunnus | — | — | — |
| `incomeEarnerType` | Tulonsaajan lisätiedon tyyppi | — | — | — |
| `unpaidAbsStartDate` | Palkattoman poissaolojakson alkupäivä | — | — | — |
| `unpaidAbsEndDate` | Palkattoman poissaolojakson loppupäivä | — | — | — |
| `unpaidAbsAbsenceDays` | Palkattomien poissaolopäivien lukumäärä | — | — | — |
| `unpaidAbsCauseCode` | Palkattoman poissaolon syy | — | — | — |
| `paidAbsStartDate` | Palkallinen poissaolojakso – alkupäivä | — | — | — |
| `paidAbsEndDate` | Palkallinen poissaolojakso – loppupäivä | — | — | — |
| `paidAbsAbsenceDays` | Palkallisten poissaolopäivien lukumäärä | — | — | — |
| `paidAbsAmount` | Palkan määrä palkalliselta poissaololta | — | — | — |
| `paidAbsCauseCode` | Palkallisen poissaolon syy = sairaus/äitiys-, isyys-, ja vanhempainvapaa, vuosiloma yms. | — | — | — |
| `nonResident` | Rajoitetusti verovelvollinen | — | — | — |
| `placeOfBusiness_s` | Suojattu toimipaikan koodi | — | — | — |
| `insuranceExceptionCode1` | Ei vakuuttamisvelvollisuutta, tyyppi=1 | — | — | — |
| `insuranceExceptionCode2` | Ei vakuuttamisvelvollisuutta, koodi 2 | — | — | — |
| `insuranceExceptionCode3` | Ei vakuuttamisvelvollisuutta, koodi 3 | — | — | — |
| `insuranceExceptionCode4` | Ei vakuuttamisvelvollisuutta, koodi 4 | — | — | — |
| `insuranceExceptionCode5` | Ei vakuuttamisvelvollisuutta, koodi 5 | — | — | — |
| `insuranceExceptionCode6` | Ei vakuuttamisvelvollisuutta, koodi 6 | — | — | — |
| `insuranceExceptionCode7` | Ei vakuuttamisvelvollisuutta, koodi 7 | — | — | — |
| `insuranceExceptionCode8` | Ei vakuuttamisvelvollisuutta, koodi 8 | — | — | — |
| `insuranceExceptionCode9` | Ei vakuuttamisvelvollisuutta, koodi 9 | — | — | — |
| `insuranceExceptionCode10` | Ei vakuuttamisvelvollisuutta, koodi 10 | — | — | — |
| `insuranceExceptionCode11` | Ei vakuuttamisvelvollisuutta, koodi 11 | — | — | — |
| `employed` | Palvelussuhteessa | — | — | — |
| `employmentCode` | Palvelussuhteen tyyppi | — | — | — |
| `termCode` | Palvelussuhteen kesto | — | — | — |
| `parttime` | Osa-aikaisuuden prosentti | — | — | — |
| `hoursPerWeek` | Säännöllinen sovittu viikkotyöaika | — | — | — |
| `paymentType` | Palkkauksen muoto | — | — | — |
| `employmentStartDate` | Palvelussuhteen voimassolo: alkupäivä | — | — | — |
| `employmentEndDate` | Palvelussuhteen voimassolo: loppupäivä | — | — | — |
| `employmentDays` | Palvelussuhteen työpäivät | — | — | — |
| `professionType1` | Ammattikoodiston tyyppi | — | — | — |
| `professionCode1` | TK10 Ammattikoodi | — | — | — |
| `professionType2` | Ammattikoodiston tyyppi | — | — | — |
| `professionCode2` | Kevan nimikkeistön koodi | — | — | — |
| `professionType3` | Ammattikoodiston tyyppi | — | — | — |
| `professionCode3` | Suomen Pankin nimikkeistön koodi | — | — | — |
| `professionType4` | Ammattikoodiston tyyppi | — | — | — |
| `professionCode4` | Trafin nimikkeistön koodi | — | — | — |
| `CBACode_s` | Suojattu sovellettava työehtosopimus | — | — | — |
| `PlaceOfBusinessCountryCode` | Tulonsaajan toimipaikan maakoodi | — | — | — |
| `PlaceOfBusinessCountryName` | Tulonsaajan toimipaikan maan nimi | — | — | — |
| `reportReceivedTimstamp` | — | — | — | — |
| `reportVersionCreatedTimestamp` | — | — | — | — |
| `reportVersionReceivedTimestamp` | — | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `repId` — Raportin tunniste

Raportin  tunniste, joka muodostuu samalla kun kyseinen taulu tehdään. Muodostettu, jotta taulujen yhdistäminen olisi tehokkaampaa. Report.repId=transactioInfo.repId

Pakollisuus (K/E) = K

#### `delId` — Toimituksen tunniste

Toimituksen tunniste, joka muodostuu samalla, kun kyseinen taulu tehdään. Muodostettu, jotta taulujen yhdistäminen olisi tehokkaampaa. report.delId=delivery.delId

Pakollisuus (K/E) = K

#### `incomeEarnerHid_e` — Suojattu tulonsaajan yksilöivä tunniste

Suojattu tulonsaajan yksilöivä tunniste

#### `incomeEarnerIdCode_s` — Tulonsaajan suojattu muu tunnus

Suojattu muu tunnus on vain niillä tulonsaajilla, joille ei löydy suojattua henkilönumeroa Tilastokeskuksen henkilötietovarastosta. Henkilötunnus on tilapäinen tai puutteellinen tai kyse on muusta tunnuksesta. Yritystunnuksesta on poistettu viiva ennen suojausta. Tätä muuttujaa ei suositella vielä käytettävän linkkauksissa, koska muuttujan suojaus on sikäli puutteellinen, etteivät kaikki alkuperäiset tunnukset ole saaneet oikein yksilöityvää suojattua tunnusta. 

pakollisuus (K/E) = K

#### `incomeEarnerIdType` — Tulonsaajan tunnisteen tyyppi

1 Y-tunnus
2 Henkilötunnus (suomalainen)
3 Alv-tunniste (VAT)
4 GIIN-tunniste
5 Verotunniste (TIN)
6 Kaupparekisteritunnus
7 Ulkomainen yritystunnus
9 Ulkomainen henkilötunnus
99 Muu tunnus

Kentän sisältö ei aina vastaa oletusmuotoa.

https://www.vero.fi/globalassets/tulorekisteri/dokumentaatio-2020/koodistot-2020.pdf

Pakollisuus (K/E) = K

#### `reportVersion` — Ilmoitusversio

Vastaaja voi korvata aikaisemman ilmoituksensa, jolloin syntyy uusi versio ilmoituksesta.

Pakollisuus (K/E) = K

#### `latauspvm` — Aineiston poimintapäivämäärä Tulorekisteristä

Tarkoittaa sitä hetkeä, jolloin Tilastokeskus on poiminut aineiston Tulorekisteristä. Tilastokeskus sai tulorekisterin tiedot käyttöön vuoden 2020 alussa, joten tästä syystä vuoden 2019 tiedot on ladattu vasta vuoden 2020 puolella. Tyypillisesti tulorekisteriin ilmoitetut tiedot ladataan yhden päivän viiveellä Tilastokeskukseen.

Pakollisuus (K/E) = K

#### `pensionActCode` — Tieto työeläkevakuutuksesta

1 = Työntekijän työeläkevakuutus, 
2 = Maatalousyrittäjän eläkevakuutus (MYEL)
, 3 = Yrittäjän eläkevakuutus (YEL). Pakollisuus (K/E) = K

#### `pensionProvIdCode_s` — Suojattu työeläkelaitoksen yhtiötunnus

#### `incomeEarnerType` — Tulonsaajan lisätiedon tyyppi

Pakollisuus (K/E) = K

#### `unpaidAbsStartDate` — Palkattoman poissaolojakson alkupäivä

Huom! Poissaolojaksoja voidaan ilmoittaa useita per ilmoitus, joten useiden poissaolojaksojen osalta tiedot eivät kirjaudu tähän tauluun tarkasti.
Pakollisuus (K/E) = E

#### `unpaidAbsEndDate` — Palkattoman poissaolojakson loppupäivä

Huom! Poissaolojaksoja voidaan ilmoittaa useita per ilmoitus, joten useiden poissaolojaksojen osalta tiedot eivät kirjaudu tähän tauluun tarkasti.
Pakollisuus (K/E) = E

#### `unpaidAbsAbsenceDays` — Palkattomien poissaolopäivien lukumäärä

Huom! Poissaolojaksoja voidaan ilmoittaa useita per ilmoitus, joten useiden poissaolojaksojen osalta tiedot eivät kirjaudu tähän tauluun tarkasti.
Pakollisuus (K/E) = E

#### `unpaidAbsCauseCode` — Palkattoman poissaolon syy

Huom! Poissaolojaksoja voidaan ilmoittaa useita per ilmoitus, joten useiden poissaolojaksojen osalta tiedot eivät kirjaudu tähän tauluun tarkasti.
Pakollisuus (K/E) = E

#### `paidAbsStartDate` — Palkallinen poissaolojakso – alkupäivä

Huom! Poissaolojaksoja voidaan ilmoittaa useita per ilmoitus, joten useiden poissaolojaksojen osalta tiedot eivät kirjaudu tähän tauluun tarkasti.
Pakollisuus (K/E) = K

#### `paidAbsEndDate` — Palkallinen poissaolojakso – loppupäivä

Huom! Poissaolojaksoja voidaan ilmoittaa useita per ilmoitus, joten useiden poissaolojaksojen osalta tiedot eivät kirjaudu tähän tauluun tarkasti.
Pakollisuus (K/E) = E

#### `paidAbsAbsenceDays` — Palkallisten poissaolopäivien lukumäärä

Huom! Poissaolojaksoja voidaan ilmoittaa useita per ilmoitus, joten useiden poissaolojaksojen osalta tiedot eivät kirjaudu tähän tauluun tarkasti.
Pakollisuus (K/E) = E

#### `paidAbsAmount` — Palkan määrä palkalliselta poissaololta

Huom! Poissaolojaksoja voidaan ilmoittaa useita per ilmoitus, joten useiden poissaolojaksojen osalta tiedot eivät kirjaudu tähän tauluun tarkasti.
Pakollisuus (K/E) = K

#### `paidAbsCauseCode` — Palkallisen poissaolon syy = sairaus/äitiys-, isyys-, ja vanhempainvapaa, vuosiloma yms.

Huom! Poissaolojaksoja voidaan ilmoittaa useita per ilmoitus, joten useiden poissaolojaksojen osalta tiedot eivät kirjaudu tähän tauluun tarkasti.
Pakollisuus (K/E) = K.  https://www.vero.fi/globalassets/tulorekisteri/dokumentaatio-2020/koodistot-2020.pdf

#### `nonResident` — Rajoitetusti verovelvollinen

kyllä / ei. Pakollisuus (K/E) = E

#### `placeOfBusiness_s` — Suojattu toimipaikan koodi

Pakollisuus (K/E) = E

#### `insuranceExceptionCode1` — Ei vakuuttamisvelvollisuutta, tyyppi=1

Ei vakuuttamisvelvollisuutta (työeläke-, sairaus-, työttömyys- sekä työtapaturma- ja ammattitautivakuutus). Pakollisuus (K/E) = K

#### `insuranceExceptionCode2` — Ei vakuuttamisvelvollisuutta, koodi 2

Ei vakuuttamisvelvollisuutta (sairausvakuutus). Pakollisuus (K/E) = K

#### `insuranceExceptionCode3` — Ei vakuuttamisvelvollisuutta, koodi 3

Ei vakuuttamisvelvollisuutta (työeläkevakuutus). Pakollisuus (K/E) = K

#### `insuranceExceptionCode4` — Ei vakuuttamisvelvollisuutta, koodi 4

Ei vakuuttamisvelvollisuutta (työtapaturma- ja ammattitautivakuutus). Pakollisuus (K/E) = K

#### `insuranceExceptionCode5` — Ei vakuuttamisvelvollisuutta, koodi 5

Ei vakuuttamisvelvollisuutta (työttömyysvakuutus). Pakollisuus (K/E) = K

#### `insuranceExceptionCode6` — Ei vakuuttamisvelvollisuutta, koodi 6

Ei kuulu Suomen sosiaaliturvan soveltamispiiriin (työeläke-, sairaus-, työttömyys- sekä työtapaturma- ja ammattitautivakuutus). Pakollisuus (K/E) = K

#### `insuranceExceptionCode7` — Ei vakuuttamisvelvollisuutta, koodi 7

Ei kuulu Suomen sosiaaliturvan soveltamispiiriin (työeläkevakuutus). Pakollisuus (K/E) = K

#### `insuranceExceptionCode8` — Ei vakuuttamisvelvollisuutta, koodi 8

Ei kuulu Suomen sosiaaliturvan soveltamispiiriin (työtapaturma- ja ammattitautivakuutus). Pakollisuus (K/E) = K

#### `insuranceExceptionCode9` — Ei vakuuttamisvelvollisuutta, koodi 9

Ei kuulu Suomen sosiaaliturvan soveltamispiiriin (työttömyysvakuutus). Pakollisuus (K/E) = K

#### `insuranceExceptionCode10` — Ei vakuuttamisvelvollisuutta, koodi 10

Ei kuulu Suomen sosiaaliturvan soveltamispiiriin (sairausvakuutus). Pakollisuus (K/E) = K

#### `insuranceExceptionCode11` — Ei vakuuttamisvelvollisuutta, koodi 11

Vapaaehtoinen vakuuttaminen Suomessa (työeläkevakuutus). Pakollisuus (K/E) = K

#### `employed` — Palvelussuhteessa

(true/false)

Pakollisuus (K/E) = E

#### `employmentCode` — Palvelussuhteen tyyppi

1 = Kokoaikainen, 2 = Osa-aikainen, 3 = Tietoa ei ole saatavilla. Pakollisuus (K/E) = E

#### `termCode` — Palvelussuhteen kesto

1=Toistaiseksi voimassa oleva, 2=Määräaikainen. 

Pakollisuus (K/E) = E

#### `parttime` — Osa-aikaisuuden prosentti

Pakollisuus (K/E) = E

#### `hoursPerWeek` — Säännöllinen sovittu viikkotyöaika

Pakollisuus (K/E) = E

#### `paymentType` — Palkkauksen muoto

1 = Kuukausipalkka, 2 = Tuntipalkka, 3 = Urakkapalkka. Pakollisuus (K/E) = K

#### `employmentStartDate` — Palvelussuhteen voimassolo: alkupäivä

Pakollisuus (K/E) = K

#### `employmentEndDate` — Palvelussuhteen voimassolo: loppupäivä

Pakollisuus (K/E) = K/E

#### `employmentDays` — Palvelussuhteen työpäivät

#### `professionType1` — Ammattikoodiston tyyppi

Saa arvon yksi, jos ilmoitettu TK10 koodi

#### `professionCode1` — TK10 Ammattikoodi

Sama ammattiluokitus kuin Ammattiluokitus 2010, mutta teknisestä syystä muodostettu jokaisesta ammattikoodista viisinumeroinen lisäämällä nollia Ammattiluokitus 2010 koodin perään riittävästi.
https://www.tilastokeskus.fi/fi/luokitukset/ammatti/ammatti_17_20180515/
Pakollisuus (K/E) = K jos tapaturmavakuutettu

#### `professionType2` — Ammattikoodiston tyyppi

Saa arvon kaksi, jos ilmoitettu Keva-koodi

#### `professionCode2` — Kevan nimikkeistön koodi

Pakollisuus (K/E) = K

#### `professionType3` — Ammattikoodiston tyyppi

Pakollisuus (K/E) = K

#### `professionCode3` — Suomen Pankin nimikkeistön koodi

Pakollisuus (K/E) = K

#### `professionType4` — Ammattikoodiston tyyppi

Pakollisuus (K/E) = K

#### `professionCode4` — Trafin nimikkeistön koodi

Pakollisuus (K/E) = K

#### `CBACode_s` — Suojattu sovellettava työehtosopimus

Pakollisuus (K/E) = E.

#### `PlaceOfBusinessCountryCode` — Tulonsaajan toimipaikan maakoodi

ISO3166-maakoodiston mukainen 2-kirjaiminen koodi. Jos maa on tuntematon, arvo on ”99”. Pakollisuus (K/E) = E

#### `PlaceOfBusinessCountryName` — Tulonsaajan toimipaikan maan nimi

Pakollisuus (K/E) = K, jos maakoodi = 99.

#### `reportReceivedTimstamp`

#### `reportVersionCreatedTimestamp`

#### `reportVersionReceivedTimestamp`

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
