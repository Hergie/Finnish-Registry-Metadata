# TAX_INCOMES Tulorekisterin palkkatiedot (Transaction code)

- **Identifier:** `TAX_INCOMES_jua_transactioncode_002.xml`
- **DOI:** `work_2020-08_2020-08-18_ain_0001`
- **Temporal coverage:** 2019-01-01 - 
- **Published:** 2025-11-11
- **Organisation:** Tilastokeskus
- **Variable count:** 142
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

## Muuttujat / Variables (142)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `repId` | Raportin rivinumero | — | — | — |
| `latauspvm` | Aineiston poimintapäivämäärä Tulorekisteristä | — | — | — |
| `recovery` | Takaisinperintä = Kyllä/Ei | — | — | — |
| `sixMonthRuleApplicabe` | Pakollisuus (K/E) = K | — | — | — |
| `insuranceCode1` | Vakuuttamistiedon tyyppi 1 | — | — | — |
| `insuranceCode2` | Vakuuttamistiedon tyyppi 2 | — | — | — |
| `insuranceCode3` | Vakuuttamistiedon tyyppi 3 | — | — | — |
| `insuranceCode5` | Vakuuttamistiedon tyyppi 5 | — | — | — |
| `insuranceCode6` | Vakuuttamistiedon tyyppi 6 | — | — | — |
| `earningsPeriodStart` | Ansaintakauden alku | — | — | — |
| `earningPeriodEnd` | Ansaintakauden loppu | — | — | — |
| `earningPeriodDays` | Ansaintakauden päivien lukumäärä | — | — | — |
| `unitPrice` | Yksikköpalkka – yksikköhinta | — | — | — |
| `unitAmount` | Yksiköiden määrä esim. työtuntien määrä | — | — | — |
| `unitCode` | Yksikköpalkka – yksikkö (tunti, päivä, viikko, jakso) | — | — | — |
| `unitPrice201` | Aikapalkan yksikköhinta | — | — | — |
| `unitAmount201` | Aikapalkan yksiköiden lukumäärä | — | — | — |
| `unitCode201` | Aikapalkan yksikkö  (tunti, päivä, viikko, jakso) | — | — | — |
| `mealBenefitTaxValue` | Ravintoedun verotusarvo | — | — | — |
| `withhold` | Takaisinperittyyn määrään kohdistuva ennakonpidätys | — | — | — |
| `benefitCode` | Edun tyyppi | — | — | — |
| `Sailorincome` | Merityötulo | — | — | — |
| `SailorIncomeCount` | — | — | — | — |
| `carBenefitCode1` | Käyttöetu | — | — | — |
| `carBenefitCode2` | Vapaa autoetu | — | — | — |
| `amount101` | Palkka yhteissumma | — | — | — |
| `amount102` | Palkkasumma, joka on työeläkevakuutusmaksun alainen | — | — | — |
| `amount103` | Palkkasumma, joka on sosiaalivakuutusmaksujen alainen | — | — | — |
| `amount104` | Palkkasumma, joka on sairausvakuutusmaksun alainen | — | — | — |
| `amount105` | Palkkasumma, joka on työttömyysvakuutusmaksun alainen | — | — | — |
| `amount106` | Palkkasumma, joka on työtapaturma- ja ammattitautivakuutusmaksun alainen | — | — | — |
| `amount201` | Aikapalkka | — | — | — |
| `amount202` | Aloitepalkkio | — | — | — |
| `amount203` | Bonuspalkka | — | — | — |
| `amount204` | Etuusajalta maksettu täydennyspalkka | — | — | — |
| `amount205` | Hätätyökorvaus | — | — | — |
| `amount206` | Iltatyökorvaus | — | — | — |
| `amount207` | Iltavuorolisä | — | — | — |
| `amount208` | Irtisanomisajan korvaus | — | — | — |
| `amount209` | Kilometrikorvaus (veronalainen) | — | — | — |
| `amount210` | Kokouspalkkio | — | — | — |
| `amount211` | Lauantaityökorvaus | — | — | — |
| `amount212` | Lisätyökorvaus | — | — | — |
| `amount213` | Lomaraha | — | — | — |
| `amount214` | Luentopalkkio | — | — | — |
| `amount215` | Luottamustoimipalkkio | — | — | — |
| `amount216` | Muu maksettu lisä | — | — | — |
| `amount217` | Odotusajan korvaus | — | — | — |
| `amount218` | Olosuhdelisä | — | — | — |
| `amount219` | Sairausajan osapalkka | — | — | — |
| `amount220` | Provisiopalkka | — | — | — |
| `amount221` | Sunnuntaityökorvaus | — | — | — |
| `amount222` | Synteettinen optio | — | — | — |
| `amount223` | Tulospalkkio | — | — | — |
| `amount224` | Työaikapankin rahakorvaus | — | — | — |
| `amount225` | Työajantasauskorvaus | — | — | — |
| `amount226` | Työsuhteeseen perustuva osakeanti | — | — | — |
| `amount227` | Urakkapalkka | — | — | — |
| `amount229` | Vahingonkorvaus päättämistilanteissa | — | — | — |
| `amount230` | Varallaolokorvaus | — | — | — |
| `amount231` | Vapaaehtoinen korvaus päättämistilanteessa | — | — | — |
| `amount232` | Viikkolepokorvaus | — | — | — |
| `amount233` | Voittopalkkio | — | — | — |
| `amount234` | Vuosilomakorvaus | — | — | — |
| `amount235` | Ylityökorvaus | — | — | — |
| `amount236` | Yötyökorvaus | — | — | — |
| `amount237` | Yövuorolisä | — | — | — |
| `amount301` | Asuntoetu | — | — | — |
| `amount302` | Asuntolainan korkoetu | — | — | — |
| `amount303` | Ateriakorvaus | — | — | — |
| `amount304` | Autoetu | — | — | — |
| `amount308` | Hallintoelimen jäsenyydestä maksettu palkkio | — | — | — |
| `amount309` | Henkilöstörahastosta nostettu rahasto-osuus ja ylijäämä (veronalainen 80%) | — | — | — |
| `amount310` | Henkilöstölle annettu rahalahja | — | — | — |
| `amount311` | Kilometrikorvaus (verovapaa) | — | — | — |
| `amount312` | Kunnaneläinlääkärin toimenpidepalkkio | — | — | — |
| `amount313` | Käyttökorvaus ansiotuloa | — | — | — |
| `amount314` | Käyttökorvaus pääomatuloa | — | — | — |
| `amount315` | Muu henkilöstölle suunnattu veronalainen etu | — | — | — |
| `amount316` | Muu veronalainen ansiotulo | — | — | — |
| `amount317` | Muu luontoisetu | — | — | — |
| `amount319` | Omaishoitajan palkkio | — | — | — |
| `amount320` | Osakepalkkio | — | — | — |
| `amount321` | Sijaismaksajan maksama palkka, josta työnantaja maksaa työnantajan sosiaalivakuutusmaksut | — | — | — |
| `amount322` | Sijaismaksajan maksama palkka, josta työnantaja maksaa työnantajan työeläkevakuutusmaksun | — | — | — |
| `amount323` | Sijaismaksajan maksama palkka, josta työnantaja maksaa työnantajan työttömyysvakuutusmaksun | — | — | — |
| `amount324` | Sijaismaksajan maksama palkka, josta työnantaja maksaa työtapaturmavakuutusmaksun | — | — | — |
| `amount325` | Sijaismaksajan maksama palkka, josta työnantaja maksaa työnantajan sairausvakuutusmaksun | — | — | — |
| `amount326` | Palkkio työsuhdekeksinnöstä | — | — | — |
| `amount328` | Perhehoitajan palkkio | — | — | — |
| `amount329` | Perhepäivähoitajan kustannusten korvaus | — | — | — |
| `amount330` | Puhelinetu | — | — | — |
| `amount331` | Päiväraha | — | — | — |
| `amount332` | Pääomatuloa oleva suoritus | — | — | — |
| `amount334` | Ravintoetu | — | — | — |
| `amount335` | Sovittelijan kulukorvaus | — | — | — |
| `amount336` | Työkorvaus | — | — | — |
| `amount337` | Työnantajakohtaisen sairaskassan maksama täydennyspäiväraha | — | — | — |
| `amount338` | Työnantajan maksama eläke | — | — | — |
| `amount339` | Työpanokseen perustuva osinko tai ylijäämä (palkka) | — | — | — |
| `amount340` | Työpanokseen perustuva osinko tai ylijäämä (työkorvaus) | — | — | — |
| `amount341` | Työsuhdematkalipun verovapaa osuus | — | — | — |
| `amount342` | Työsuhdematkalipun palkaksi katsottu osuus | — | — | — |
| `amount343` | Työsuhdeoptio | — | — | — |
| `amount350` | Urheilijarahastoon siirretty palkka | — | — | — |
| `amount351` | Urheilijarahastosta maksettu palkka | — | — | — |
| `amount352` | Vakuutuspalkka | — | — | — |
| `amount353` | Veronalainen kustannusten korvaus | — | — | — |
| `amount354` | Yksityisen hoidon tuen kuntalisä | — | — | — |
| `amount355` | Yksityisen hoidon tuki (palkka) | — | — | — |
| `amount356` | Yksityisen hoidon tuki (työkorvaus) | — | — | — |
| `amount357` | Yleishyödyllisen yhteisön maksama kilometrikorvaus | — | — | — |
| `amount358` | Yleishyödyllisen yhteisön maksama päiväraha | — | — | — |
| `amount359` | Perusteeton etu | — | — | — |
| `amount361` | Työsuhdeoptio, jonka merkintähinta on luovutusajankohtana alhaisempi kuin markkinahinta | — | — | — |
| `amount401` | Autoedusta peritty korvaus | — | — | — |
| `amount402` | Ennakonpidätys | — | — | — |
| `amount403` | Luottamushenkilömaksu | — | — | — |
| `amount404` | Lähdevero | — | — | — |
| `amount405` | Lähdeverovähennys | — | — | — |
| `amount406` | Maksettava palkka | — | — | — |
| `amount407` | Muista luontoiseduista peritty korvaus | — | — | — |
| `amount408` | Nettopalkasta vähennettävä muu erä | — | — | — |
| `amount409` | Nettopalkka | — | — | — |
| `amount410` | Työnantajan maksaman kollektiivisen lisäeläkevakuutuksen maksu | — | — | — |
| `amount411` | Työnantajan maksaman kollektiivisen lisäeläkevakuutuksen työntekijältä peritty osuus | — | — | — |
| `amount412` | Työntekijän sairausvakuutusmaksu | — | — | — |
| `amount413` | Työntekijän työeläkevakuutusmaksu | — | — | — |
| `amount414` | Työntekijän työttömyysvakuutusmaksu | — | — | — |
| `amount415` | Työsuhdematkalipusta peritty korvaus | — | — | — |
| `amount416` | Ulkomaille maksettu vero | — | — | — |
| `amount417` | Ulosmittaus | — | — | — |
| `amount418` | Vapaaehtoisen yksilöllisen eläkevakuutuksen maksu | — | — | — |
| `amount419` | Vähennys ennen ennakonpidätystä | — | — | — |
| `amount238` | Muu säännöllinen lisä | — | — | — |
| `amount239` | Vastikevapaan korvaus | — | — | — |
| `amount327` | Perhehoitajan kustannusten korvaus | — | — | — |
| `amount362` | Rajoitetusti verovelvolliselle maksettu rojalti | — | — | — |
| `amount363` | Polkupyöräedun verovapaa osuus | — | — | — |
| `amount364` | Polkupyöräedun palkaksi katsottu osuus | — | — | — |
| `amount365` | Ehdollinen osakepalkkio | — | — | — |
| `amount420` | Polkupyöräedusta peritty korvaus | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `repId` — Raportin rivinumero

Tilastokeskuksessa muodostettu raportin  tunniste, joka muodostuu samalla kun kyseinen taulu tehdään. Muodostettu, jotta taulujen yhdistäminen olisi tehokkaampaa. Report.repId=transactionCode.repId

Pakollisuus (K/E) = K

#### `latauspvm` — Aineiston poimintapäivämäärä Tulorekisteristä

Tarkoittaa sitä hetkeä, jolloin Tilastokeskus on poiminut aineiston Tulorekisteristä. Tilastokeskus sai tulorekisterin tiedot käyttöön vuoden 2020 alussa, joten tästä syystä vuoden 2019 tiedot on ladattu vasta vuoden 2020 puolella. Tyypillisesti tulorekisteriin ilmoitetut tiedot ladataan yhden päivän viiveellä Tilastokeskukseen.
 Pakollisuus (K/E) = K

#### `recovery` — Takaisinperintä = Kyllä/Ei

Huom! Tulolajikohtainen tieto, joten tämä tieto kannattaa poimia taulusta transactionInfo

#### `sixMonthRuleApplicabe` — Pakollisuus (K/E) = K

#### `insuranceCode1` — Vakuuttamistiedon tyyppi 1

1 = Sosiaalivakuutusmaksujen alainen (koodit 2-6). Pakollisuus (K/E) = K

#### `insuranceCode2` — Vakuuttamistiedon tyyppi 2

2 = Työeläkevakuutusmaksun alainen. Pakollisuus (K/E) = K

#### `insuranceCode3` — Vakuuttamistiedon tyyppi 3

3 = Sairausvakuutusmaksun alainen. Pakollisuus (K/E) = K

#### `insuranceCode5` — Vakuuttamistiedon tyyppi 5

5 = Työttömyysvakuutusmaksun alainen. Pakollisuus (K/E) = K

#### `insuranceCode6` — Vakuuttamistiedon tyyppi 6

6 = Työtapaturma- ja ammattitautivakuutusmaksun alainen. Pakollisuus (K/E) = K

#### `earningsPeriodStart` — Ansaintakauden alku

Huom! Tulolajikohtainen tieto, joten tämä tieto kannattaa poimia taulusta transactionInfo. Pakollisuus (K/E) = K

#### `earningPeriodEnd` — Ansaintakauden loppu

Huom! Tulolajikohtainen tieto, joten tämä tieto kannattaa poimia taulusta transactionInfo. Pakollisuus (K/E) = K

#### `earningPeriodDays` — Ansaintakauden päivien lukumäärä

Huom! Tulolajikohtainen tieto, joten tämä tieto kannattaa poimia taulusta transactionInfo. Pakollisuus (K/E) = K

#### `unitPrice` — Yksikköpalkka – yksikköhinta

Huom! Tulolajikohtainen tieto, joten tämä tieto kannattaa poimia taulusta transactionInfo.

#### `unitAmount` — Yksiköiden määrä esim. työtuntien määrä

Huom! Tulolajikohtainen tieto, joten tämä tieto kannattaa poimia taulusta transactionInfo.

#### `unitCode` — Yksikköpalkka – yksikkö (tunti, päivä, viikko, jakso)

Huom! Tulolajikohtainen tieto, joten tämä tieto kannattaa poimia taulusta transactionInfo.

#### `unitPrice201` — Aikapalkan yksikköhinta

Huom! Tulolajikohtainen tieto, joten tämä tieto kannattaa poimia taulusta transactionInfo

#### `unitAmount201` — Aikapalkan yksiköiden lukumäärä

Huom! Tulolajikohtainen tieto, joten tämä tieto kannattaa poimia taulusta transactionInfo

#### `unitCode201` — Aikapalkan yksikkö  (tunti, päivä, viikko, jakso)

Huom! Tulolajikohtainen tieto, joten tämä tieto kannattaa poimia taulusta transactionInfo

#### `mealBenefitTaxValue` — Ravintoedun verotusarvo

"True" tai tyhjä. Pakollisuus (K/E) = K

#### `withhold` — Takaisinperittyyn määrään kohdistuva ennakonpidätys

Pakollisuus (K/E) = E. https://www.vero.fi/globalassets/tulorekisteri/palkkatietoilmoituksen-tietosisällön-soveltamisohje.pdf

#### `benefitCode` — Edun tyyppi

1 = Asuntoetu, 2 = Puhelinetu, 3 = Ravintoetu, 4 = Muut edut. Pakollisuus (K/E) = K

#### `Sailorincome` — Merityötulo

"True" tai tyhjä. Pakollisuus (K/E) = K

#### `SailorIncomeCount`

#### `carBenefitCode1` — Käyttöetu

"True" tai tyhjä. Pakollisuus (K/E) = K

#### `carBenefitCode2` — Vapaa autoetu

"True" tai tyhjä. Pakollisuus (K/E) = K

#### `amount101` — Palkka yhteissumma

Pakollisuus (K/E) = K

#### `amount102` — Palkkasumma, joka on työeläkevakuutusmaksun alainen

Pakollisuus (K/E) = K

#### `amount103` — Palkkasumma, joka on sosiaalivakuutusmaksujen alainen

Pakollisuus (K/E) = K

#### `amount104` — Palkkasumma, joka on sairausvakuutusmaksun alainen

Pakollisuus (K/E) = K

#### `amount105` — Palkkasumma, joka on työttömyysvakuutusmaksun alainen

Pakollisuus (K/E) = K

#### `amount106` — Palkkasumma, joka on työtapaturma- ja ammattitautivakuutusmaksun alainen

Pakollisuus (K/E) = K

#### `amount201` — Aikapalkka

Pakollisuus (K/E) = E

#### `amount202` — Aloitepalkkio

Pakollisuus (K/E) = E

#### `amount203` — Bonuspalkka

Pakollisuus (K/E) = E

#### `amount204` — Etuusajalta maksettu täydennyspalkka

Pakollisuus (K/E) = E

#### `amount205` — Hätätyökorvaus

Pakollisuus (K/E) = E

#### `amount206` — Iltatyökorvaus

Pakollisuus (K/E) = E

#### `amount207` — Iltavuorolisä

Pakollisuus (K/E) = E

#### `amount208` — Irtisanomisajan korvaus

Pakollisuus (K/E) = E

#### `amount209` — Kilometrikorvaus (veronalainen)

Pakollisuus (K/E) = E

#### `amount210` — Kokouspalkkio

Pakollisuus (K/E) = E

#### `amount211` — Lauantaityökorvaus

Pakollisuus (K/E) = E

#### `amount212` — Lisätyökorvaus

Pakollisuus (K/E) = E

#### `amount213` — Lomaraha

Pakollisuus (K/E) = E

#### `amount214` — Luentopalkkio

Pakollisuus (K/E) = E

#### `amount215` — Luottamustoimipalkkio

Pakollisuus (K/E) = E

#### `amount216` — Muu maksettu lisä

Pakollisuus (K/E) = E

#### `amount217` — Odotusajan korvaus

Pakollisuus (K/E) = E

#### `amount218` — Olosuhdelisä

Pakollisuus (K/E) = E

#### `amount219` — Sairausajan osapalkka

Pakollisuus (K/E) = E

#### `amount220` — Provisiopalkka

Pakollisuus (K/E) = E

#### `amount221` — Sunnuntaityökorvaus

Pakollisuus (K/E) = E

#### `amount222` — Synteettinen optio

Pakollisuus (K/E) = E

#### `amount223` — Tulospalkkio

Pakollisuus (K/E) = E

#### `amount224` — Työaikapankin rahakorvaus

Pakollisuus (K/E) = E

#### `amount225` — Työajantasauskorvaus

Pakollisuus (K/E) = E

#### `amount226` — Työsuhteeseen perustuva osakeanti

Pakollisuus (K/E) = E

#### `amount227` — Urakkapalkka

Pakollisuus (K/E) = E

#### `amount229` — Vahingonkorvaus päättämistilanteissa

Pakollisuus (K/E) = E

#### `amount230` — Varallaolokorvaus

Pakollisuus (K/E) = E

#### `amount231` — Vapaaehtoinen korvaus päättämistilanteessa

Pakollisuus (K/E) = E

#### `amount232` — Viikkolepokorvaus

Pakollisuus (K/E) = E

#### `amount233` — Voittopalkkio

Pakollisuus (K/E) = E

#### `amount234` — Vuosilomakorvaus

Pakollisuus (K/E) = E

#### `amount235` — Ylityökorvaus

Pakollisuus (K/E) = E

#### `amount236` — Yötyökorvaus

Pakollisuus (K/E) = E

#### `amount237` — Yövuorolisä

Pakollisuus (K/E) = E

#### `amount301` — Asuntoetu

Pakollisuus (K/E) = E

#### `amount302` — Asuntolainan korkoetu

Pakollisuus (K/E) = K

#### `amount303` — Ateriakorvaus

Pakollisuus (K/E) = E

#### `amount304` — Autoetu

Pakollisuus (K/E) = K

#### `amount308` — Hallintoelimen jäsenyydestä maksettu palkkio

Pakollisuus (K/E) = K

#### `amount309` — Henkilöstörahastosta nostettu rahasto-osuus ja ylijäämä (veronalainen 80%)

Pakollisuus (K/E) = K

#### `amount310` — Henkilöstölle annettu rahalahja

Pakollisuus (K/E) = K

#### `amount311` — Kilometrikorvaus (verovapaa)

Pakollisuus (K/E) = K

#### `amount312` — Kunnaneläinlääkärin toimenpidepalkkio

Pakollisuus (K/E) = K

#### `amount313` — Käyttökorvaus ansiotuloa

Pakollisuus (K/E) = K

#### `amount314` — Käyttökorvaus pääomatuloa

Pakollisuus (K/E) = K

#### `amount315` — Muu henkilöstölle suunnattu veronalainen etu

Pakollisuus (K/E) = K

#### `amount316` — Muu veronalainen ansiotulo

Pakollisuus (K/E) = K

#### `amount317` — Muu luontoisetu

Pakollisuus (K/E) = K

#### `amount319` — Omaishoitajan palkkio

Pakollisuus (K/E) = K

#### `amount320` — Osakepalkkio

Pakollisuus (K/E) = K

#### `amount321` — Sijaismaksajan maksama palkka, josta työnantaja maksaa työnantajan sosiaalivakuutusmaksut

Pakollisuus (K/E) = K

#### `amount322` — Sijaismaksajan maksama palkka, josta työnantaja maksaa työnantajan työeläkevakuutusmaksun

Pakollisuus (K/E) = K

#### `amount323` — Sijaismaksajan maksama palkka, josta työnantaja maksaa työnantajan työttömyysvakuutusmaksun

Pakollisuus (K/E) = K

#### `amount324` — Sijaismaksajan maksama palkka, josta työnantaja maksaa työtapaturmavakuutusmaksun

Pakollisuus (K/E) = K

#### `amount325` — Sijaismaksajan maksama palkka, josta työnantaja maksaa työnantajan sairausvakuutusmaksun

Pakollisuus (K/E) = K

#### `amount326` — Palkkio työsuhdekeksinnöstä

Pakollisuus (K/E) = E

#### `amount328` — Perhehoitajan palkkio

Pakollisuus (K/E) = K

#### `amount329` — Perhepäivähoitajan kustannusten korvaus

Pakollisuus (K/E) = K

#### `amount330` — Puhelinetu

Pakollisuus (K/E) = E

#### `amount331` — Päiväraha

Pakollisuus (K/E) = K

#### `amount332` — Pääomatuloa oleva suoritus

Pakollisuus (K/E) = K

#### `amount334` — Ravintoetu

Pakollisuus (K/E) = E

#### `amount335` — Sovittelijan kulukorvaus

Pakollisuus (K/E) = K

#### `amount336` — Työkorvaus

Pakollisuus (K/E) = K

#### `amount337` — Työnantajakohtaisen sairaskassan maksama täydennyspäiväraha

Pakollisuus (K/E) = K

#### `amount338` — Työnantajan maksama eläke

Pakollisuus (K/E) = K

#### `amount339` — Työpanokseen perustuva osinko tai ylijäämä (palkka)

Pakollisuus (K/E) = K

#### `amount340` — Työpanokseen perustuva osinko tai ylijäämä (työkorvaus)

Pakollisuus (K/E) = K

#### `amount341` — Työsuhdematkalipun verovapaa osuus

Pakollisuus (K/E) = K

#### `amount342` — Työsuhdematkalipun palkaksi katsottu osuus

Pakollisuus (K/E) = K

#### `amount343` — Työsuhdeoptio

Pakollisuus (K/E) = K

#### `amount350` — Urheilijarahastoon siirretty palkka

Pakollisuus (K/E) = K

#### `amount351` — Urheilijarahastosta maksettu palkka

Pakollisuus (K/E) = K

#### `amount352` — Vakuutuspalkka

Pakollisuus (K/E) = K

#### `amount353` — Veronalainen kustannusten korvaus

Pakollisuus (K/E) = K

#### `amount354` — Yksityisen hoidon tuen kuntalisä

Pakollisuus (K/E) = K

#### `amount355` — Yksityisen hoidon tuki (palkka)

Pakollisuus (K/E) = K

#### `amount356` — Yksityisen hoidon tuki (työkorvaus)

Pakollisuus (K/E) = K

#### `amount357` — Yleishyödyllisen yhteisön maksama kilometrikorvaus

Pakollisuus (K/E) = K

#### `amount358` — Yleishyödyllisen yhteisön maksama päiväraha

Pakollisuus (K/E) = K

#### `amount359` — Perusteeton etu

Pakollisuus (K/E) = K

#### `amount361` — Työsuhdeoptio, jonka merkintähinta on luovutusajankohtana alhaisempi kuin markkinahinta

Pakollisuus (K/E) = K

#### `amount401` — Autoedusta peritty korvaus

Pakollisuus (K/E) = K

#### `amount402` — Ennakonpidätys

Pakollisuus (K/E) = K

#### `amount403` — Luottamushenkilömaksu

Pakollisuus (K/E) = K

#### `amount404` — Lähdevero

Pakollisuus (K/E) = K

#### `amount405` — Lähdeverovähennys

Pakollisuus (K/E) = K

#### `amount406` — Maksettava palkka

Pakollisuus (K/E) = E

#### `amount407` — Muista luontoiseduista peritty korvaus

Pakollisuus (K/E) = K

#### `amount408` — Nettopalkasta vähennettävä muu erä

Pakollisuus (K/E) = E

#### `amount409` — Nettopalkka

Pakollisuus (K/E) = E

#### `amount410` — Työnantajan maksaman kollektiivisen lisäeläkevakuutuksen maksu

Pakollisuus (K/E) = K

#### `amount411` — Työnantajan maksaman kollektiivisen lisäeläkevakuutuksen työntekijältä peritty osuus

Pakollisuus (K/E) = K

#### `amount412` — Työntekijän sairausvakuutusmaksu

Pakollisuus (K/E) = K

#### `amount413` — Työntekijän työeläkevakuutusmaksu

Pakollisuus (K/E) = K

#### `amount414` — Työntekijän työttömyysvakuutusmaksu

Pakollisuus (K/E) = K

#### `amount415` — Työsuhdematkalipusta peritty korvaus

Pakollisuus (K/E) = K

#### `amount416` — Ulkomaille maksettu vero

Pakollisuus (K/E) = E

#### `amount417` — Ulosmittaus

Pakollisuus (K/E) = E

#### `amount418` — Vapaaehtoisen yksilöllisen eläkevakuutuksen maksu

Pakollisuus (K/E) = K

#### `amount419` — Vähennys ennen ennakonpidätystä

Pakollisuus (K/E) = K

#### `amount238` — Muu säännöllinen lisä

Pakollisuus (K/E) = K, uusi tulolaji 2021

#### `amount239` — Vastikevapaan korvaus

Pakollisuus (K/E) = K, uusi tulolaji 2021

#### `amount327` — Perhehoitajan kustannusten korvaus

Pakollisuus (K/E) = K, uusi tulolaji 2021

#### `amount362` — Rajoitetusti verovelvolliselle maksettu rojalti

Pakollisuus (K/E) = K, uusi tulolaji 2021

#### `amount363` — Polkupyöräedun verovapaa osuus

Pakollisuus (K/E) = K, uusi tulolaji 2021

#### `amount364` — Polkupyöräedun palkaksi katsottu osuus

Pakollisuus (K/E) = K, uusi tulolaji 2021

#### `amount365` — Ehdollinen osakepalkkio

Pakollisuus (K/E) = K, uusi tulolaji 2021

#### `amount420` — Polkupyöräedusta peritty korvaus

Pakollisuus (K/E) = K, uusi tulolaji 2021

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
