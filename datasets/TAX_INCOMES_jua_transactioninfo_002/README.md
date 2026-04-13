# TAX_INCOMES Tulorekisterin palkkatiedot (Transaction info)

- **Identifier:** `TAX_INCOMES_jua_transactioninfo_002.xml`
- **DOI:** `work_2020-08_2020-08-18_ain_0001`
- **Temporal coverage:** 2019-01-01 - 
- **Published:** 2025-11-11
- **Organisation:** Tilastokeskus
- **Variable count:** 32
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

## Muuttujat / Variables (32)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `repId` | Raportin rivinumero | — | — | — |
| `latauspvm` | Aineiston poimintapäivämäärä Tulorekisteristä | — | — | — |
| `transactionCode` | Tulolajin koodi | — | — | — |
| `amount` | Tulolajin euromäärä | — | — | — |
| `noMoney` | Maksettu muuna kuin rahana | — | — | — |
| `oneOff` | Kertakorvaus | — | — | — |
| `unjustEnrichment` | Perusteeton etu | — | — | — |
| `recovery` | Takaisinperintä | — | — | — |
| `origPaymentDate` | Takaisinperinnän alkuperäinen maksupäivä | — | — | — |
| `origStartDate` | Takaisinperinnän alkuperäisen maksujakson alku | — | — | — |
| `origEndDate` | Takaisinperinnän alkuperäisen maksujakson loppu | — | — | — |
| `unitPrice1` | Tunnin hinta | — | — | — |
| `unitAmount1` | Tuntien määrä | — | — | — |
| `unitPrice2` | Päivän hinta | — | — | — |
| `unitAmount2` | Päivien määrä | — | — | — |
| `unitPrice3` | Viikon hinta | — | — | — |
| `unitAmount3` | Viikkojen määrä | — | — | — |
| `unitPrice5` | Jakson hinta | — | — | — |
| `unitAmount5` | Jaksojen määrä | — | — | — |
| `earningPeriodStartDate` | Ansaintajakson alku | — | — | — |
| `earningPeriodEndDate` | Ansaintajakson loppu | — | — | — |
| `insuranceCode1` | Sosiaalivakuutusmaksujen alainen (koodit 2-6) | — | — | — |
| `insuranceCode2` | Työeläkevakuutusmaksun alainen | — | — | — |
| `insuranceCode3` | Sairasvakuutusmaksun alainen | — | — | — |
| `insuranceCode5` | Työttömyysvakuutusmaksun alainen | — | — | — |
| `insuranceCode6` | Työtapaturma- ja ammattitautivakuutusmaksun alainen | — | — | — |
| `mealBenefitTaxvalue` | Ravintoedusta peritty korvaus joka vastaa verotusarvoa | — | — | — |
| `benefitCode` | "Muun luontaisetu"- tulolajin lisätieto | — | — | — |
| `sixmonthruleApplicable` | 6 kk sääntö | — | — | — |
| `dailyAllowanceCode` | Päivärahan tyyppi | — | — | — |
| `recoveryDate` | Takaisinperintäpäivä | — | — | — |
| `taxAtSource` | Takaisinperittyyn määrään kohdistuva lähdevero | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `repId` — Raportin rivinumero

Tilastokeskuksessa muodostettu raportin  tunniste, joka muodostuu samalla kun kyseinen taulu tehdään. Muodostettu, jotta taulujen yhdistäminen olisi tehokkaampaa. Report.id=transactioInfo.repId

Pakollisuus (K/E) = K

#### `latauspvm` — Aineiston poimintapäivämäärä Tulorekisteristä

Tarkoittaa sitä hetkeä, jolloin Tilastokeskus on poiminut aineiston Tulorekisteristä. Tilastokeskus sai tulorekisterin tiedot käyttöön vuoden 2020 alussa, joten tästä syystä vuoden 2019 tiedot on ladattu vasta vuoden 2020 puolella. Tyypillisesti tulorekisteriin ilmoitetut tiedot ladataan yhden päivän viiveellä Tilastokeskukseen.
Pakollisuus (K/E) = K

#### `transactionCode` — Tulolajin koodi

100- ja 200-sarja vastaavat toisiaan. 100-sarjassa on laskettu kaikki kaksisataa sarjan tiedot yhteen palkkasummaan. Vastaaja voi antaa tiedot ainoastaan toisella sarjoista. Eli jos raportissa on yksikin 200-sarjan erä niin tällä ilmoituksella ei voi ilmoittaa 100-sarjan eriä.
https://www.vero.fi/globalassets/tulorekisteri/tulolajien-ja-tuloista-vahennettavien-erien-selitteet-2020.pdf
Pakollisuus (K/E) = K

#### `amount` — Tulolajin euromäärä

Pakollisuus (K/E) = K

#### `noMoney` — Maksettu muuna kuin rahana

"True" tai tyhjä. Pakollisuus (K/E) = E

#### `oneOff` — Kertakorvaus

"True" tai tyhjä. Pakollisuus (K/E) = E

#### `unjustEnrichment` — Perusteeton etu

"True" tai tyhjä. Pakollisuus (K/E) = E

#### `recovery` — Takaisinperintä

"True" tai tyhjä. Pakollisuus (K/E) = E

#### `origPaymentDate` — Takaisinperinnän alkuperäinen maksupäivä

Jos tulolajille on ilmoitettu useita maksupäiviä, niin otetaan viimeisin.
Pakollisuus (K/E) = E

#### `origStartDate` — Takaisinperinnän alkuperäisen maksujakson alku

Jos tulolajille on ilmoitettu useita maksujakson alkupäiviä, niin otetaan ensimmäinen. Pakollisuus (K/E) = K

#### `origEndDate` — Takaisinperinnän alkuperäisen maksujakson loppu

Jos tulolajille on ilmoitettu useita maksujakson loppupäiviä, niin otetaan viimeisin. Pakollisuus (K/E) = K

#### `unitPrice1` — Tunnin hinta

#### `unitAmount1` — Tuntien määrä

#### `unitPrice2` — Päivän hinta

#### `unitAmount2` — Päivien määrä

#### `unitPrice3` — Viikon hinta

#### `unitAmount3` — Viikkojen määrä

#### `unitPrice5` — Jakson hinta

#### `unitAmount5` — Jaksojen määrä

#### `earningPeriodStartDate` — Ansaintajakson alku

Jos tulolajille on ilmoitettu useita ansaintajaksoja, niin alkupäiväksi ensimmäinen. Pakollisuus (K/E) = K

#### `earningPeriodEndDate` — Ansaintajakson loppu

Jos tulolajille on ilmoitettu useita ansaintajaksoja, niin loppupäiväksi viimeinen. Pakollisuus (K/E) = K

#### `insuranceCode1` — Sosiaalivakuutusmaksujen alainen (koodit 2-6)

Pakollisuus (K/E) = K

#### `insuranceCode2` — Työeläkevakuutusmaksun alainen

Pakollisuus (K/E) = K

#### `insuranceCode3` — Sairasvakuutusmaksun alainen

Pakollisuus (K/E) = K

#### `insuranceCode5` — Työttömyysvakuutusmaksun alainen

Pakollisuus (K/E) = K

#### `insuranceCode6` — Työtapaturma- ja ammattitautivakuutusmaksun alainen

Pakollisuus (K/E) = K

#### `mealBenefitTaxvalue` — Ravintoedusta peritty korvaus joka vastaa verotusarvoa

Pakollisuus (K/E) = K

#### `benefitCode` — "Muun luontaisetu"- tulolajin lisätieto

1 = Asuntoetu, 2 = Puhelinetu, 3 = Ravintoetu, 4 = Muut edut. Jos tulolajille on ilmoitettu useita muun luontoisedun tietoja, niin koodiksi 99. Pakollisuus (K/E) = K

#### `sixmonthruleApplicable` — 6 kk sääntö

Pakollisuus (K/E) = K

#### `dailyAllowanceCode` — Päivärahan tyyppi

Jos tulolajille on ilmoitettu useita päivärahan tyyppejä, niin koodiksi 99. Pakollisuus (K/E) = K

#### `recoveryDate` — Takaisinperintäpäivä

Pakollisuus (K/E) = K

#### `taxAtSource` — Takaisinperittyyn määrään kohdistuva lähdevero

Pakollisuus (K/E) = E

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
