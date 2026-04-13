# TAX_INCOMES Tulorekisterin palkkatiedot (Delivery)

- **Identifier:** `TAX_INCOMES_jua_delivery_002.xml`
- **DOI:** `work_2020-08_2020-08-18_ain_0001`
- **Temporal coverage:** 2019-01-01 - 
- **Published:** 2026-01-23
- **Organisation:** Tilastokeskus
- **Variable count:** 23
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

## Muuttujat / Variables (23)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `delId` | Toimituksen tunniste | — | — | — |
| `payerIdType1_s` | Maksajan suojattu yritystunnus | — | — | — |
| `payerhid_e` | Suojattu maksajan yksilöivä tunniste | — | — | — |
| `payerOtherIdCode_s` | Maksajan suojattu muu tunnus | — | — | — |
| `payerOtherIdType` | Muu tunnus, maksajan tunnustyyppi | — | — | — |
| `payerSubOrgType1_s` | Maksajan aliorganisaation suojattu tunnus, kun tyyppi=1 | — | — | — |
| `payerSubOrgType2_s` | Maksajan aliorganisaation suojattu tunnus, kun tyyppi=2 | — | — | — |
| `payerSubOrgType3_s` | Maksajan aliorganisaation suojattu tunnus, kun tyyppi=3 | — | — | — |
| `paymentDate` | Maksupäivä | — | — | — |
| `paymentStartDate` | Maksukauden alku | — | — | — |
| `paymentEndDate` | Maksukauden loppu | — | — | — |
| `substitutePayerActs` | Toimii sijaismaksajana = Kyllä/Ei | — | — | — |
| `substitutePayerWageSec` | Maksettu palkkaturvana = Kyllä/Ei | — | — | — |
| `payerType1` | Maksajan tunnus, kun koodi = 1 | — | — | — |
| `payerType2` | Maksajan tunnus, kun koodi = 2 | — | — | — |
| `payerType3` | Maksajan tunnus, kun koodi = 3 | — | — | — |
| `payerType4` | Maksajan tunnus, kun koodi = 4 | — | — | — |
| `payerType6` | Maksajan tunnus, kun koodi = 6 | — | — | — |
| `payerType7` | Maksajan tunnus, kun koodi = 7 | — | — | — |
| `payerType8` | Maksajan tunnus, kun koodi = 8 | — | — | — |
| `payerType9` | Maksajan tunnus, kun koodi = 9 | — | — | — |
| `payerType10` | Maksajan tunnus, kun koodi = 10 | — | — | — |
| `latauspvm` | Aineiston poimintapäivämäärä Tulorekisteristä | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `delId` — Toimituksen tunniste

Tilastokeskuksessa muodostettu toimituksen tunniste joka muodostuu samalla kun kyseinen taulu tehdään. Muodostettu jotta taulujen yhdistäminen olisi tehokkaampaa. report.delId=delivery.Id, 


Pakollisuus (K/E) = K

#### `payerIdType1_s` — Maksajan suojattu yritystunnus

#### `payerhid_e` — Suojattu maksajan yksilöivä tunniste

Suojattu maksajan yksilöivä tunniste

#### `payerOtherIdCode_s` — Maksajan suojattu muu tunnus

#### `payerOtherIdType` — Muu tunnus, maksajan tunnustyyppi

Maksajan tunnustyyppi, kun se ei ole henkilö- tai yritystunnus. 

3 Alv-tunniste (VAT)
4 GIIN-tunniste
5 Verotunniste (TIN)
6 Kaupparekisteritunnus
7 Ulkomainen yritystunnus
9 Ulkomainen henkilötunnus
99 Muu tunnus

Suorituksen maksajasta annetaan ensisijaisesti suomalainen asiakastunniste (esimerkiksi Y-tunnus tai henkilötunnus). Jos maksajalla ei ole suomalaista asiakastunnistetta, annetaan ulkomainen tunniste. Tällöin pitää antaa myös tarkentavia yksilöinti- ja yhteystietoja, kuten maksajan nimi ja osoitetiedot. Vastaavat tiedot on annettava myös silloin, kun suorituksen maksaja on tilapäinen työnantaja.
https://www.vero.fi/tulorekisteri/yritykset-ja-organisaatiot/yksityiskohtaiset-tulorekisterin-ohjeet/63749/tietojen-ilmoittaminen-tulorekisteriin-palkkatietoilmoituksen-pakolliset-ja-t%C3%A4ydent%C3%A4v%C3%A4t-tiedot3/

 Pakollisuus (K/E) = K

#### `payerSubOrgType1_s` — Maksajan aliorganisaation suojattu tunnus, kun tyyppi=1

1 = Kevan ilmoittajakoodisto. Pakollisuus (K/E) = K. HUOM! Luokituksen sisältö vaihtelee ja voi sisältää myös tekstiä.

#### `payerSubOrgType2_s` — Maksajan aliorganisaation suojattu tunnus, kun tyyppi=2

2 = Maksajan oma koodisto. Pakollisuus (K/E) = K. HUOM! Luokituksen sisältö vaihtelee ja voi sisältää myös tekstiä.

#### `payerSubOrgType3_s` — Maksajan aliorganisaation suojattu tunnus, kun tyyppi=3

3 = Virastotunniste. Pakollisuus (K/E) = K. HUOM! Luokituksen sisältö vaihtelee ja voi sisältää myös tekstiä.

#### `paymentDate` — Maksupäivä

Pakollisuus (K/E) = K

#### `paymentStartDate` — Maksukauden alku

Pakollisuus (K/E) = K

#### `paymentEndDate` — Maksukauden loppu

Pakollisuus (K/E) = K

#### `substitutePayerActs` — Toimii sijaismaksajana = Kyllä/Ei

"True". Pakollisuus (K/E) = K

#### `substitutePayerWageSec` — Maksettu palkkaturvana = Kyllä/Ei

"True". Pakollisuus (K/E) = K

#### `payerType1` — Maksajan tunnus, kun koodi = 1

1 = Julkisyhteisö

#### `payerType2` — Maksajan tunnus, kun koodi = 2

2 = Kotitalous

#### `payerType3` — Maksajan tunnus, kun koodi = 3

3 = Tilapäinen työnantaja

#### `payerType4` — Maksajan tunnus, kun koodi = 4

4 = Ulkomainen työnantaja

#### `payerType6` — Maksajan tunnus, kun koodi = 6

6=Valtio

#### `payerType7` — Maksajan tunnus, kun koodi = 7

7=Valtion liikelaitos tai erillishallinnollinen valtion laitos

#### `payerType8` — Maksajan tunnus, kun koodi = 8

8=Erityisjärjestö

#### `payerType9` — Maksajan tunnus, kun koodi = 9

9=Ulkomainen konserniyhtiö

#### `payerType10` — Maksajan tunnus, kun koodi = 10

10=Kotitalouksien työnantajarinki

#### `latauspvm` — Aineiston poimintapäivämäärä Tulorekisteristä

Tarkoittaa sitä hetkeä, jolloin Tilastokeskus on poiminut aineiston Tulorekisteristä. Tilastokeskus sai tulorekisterin tiedot käyttöön vuoden 2020 alussa, joten tästä syystä vuoden 2019 tiedot on ladattu vasta vuoden 2020 puolella. Tyypillisesti tulorekisteriin ilmoitetut tiedot ladataan yhden päivän viiveellä Tilastokeskukseen.

Pakollisuus (K/E) = K

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
