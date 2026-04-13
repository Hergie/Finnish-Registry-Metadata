# TAX_SUMINCOMES Tulorekisterin summatut palkkatiedot

- **Identifier:** `TAX_SUMINCOMES_jua_summatut_palkkatiedot.xml`
- **DOI:** `work_2020-08_2020-08-18_ain_0001`
- **Temporal coverage:** 2019-01-01 - 
- **Published:** 2025-06-13
- **Organisation:** Tilastokeskus
- **Variable count:** 53
- **Observation count:** —
- **Population:** Kaikki maksajat ovat aineistossa mukana tunnustyypistä riippumatta, ja tulonsaajista on pyritty rajaamaan oikeudelliset henkilöt pois.
- **Source:** Tulorekisteri

## Kuvaus / Description

Tulorekisteri on Verohallinnon ylläpitämä sähköinen tietokanta, jonne ilmoitetaan tiedot maksetuista palkoista, eläkkeistä ja etuuksista. Lisää tietoa tulorekisteristä: https://www.vero.fi/tulorekisteri/tietoa-meist%C3%A4/ 
Tässä tutkimuskäyttöön suojatussa tulorekisterin valmisaineistomoduulissa TAX_SUMINCOMES ”Tulorekisterin summatut palkkatiedot” palvelussuhteen kuukausittaiset tiedot on muodostettu valmiiksi. Eli yhden rivin muodostaa vuosi, kuukausi, maksaja, tulonsaaja. Aineistossa on 47 muuttujaa ja vuodessa aineistoon muodostuu yhteensä noin 30 miljoonaa riviä. 

Aineiston muuttujat on poimittu enimmäkseen suoraan tulorekisterin palkkojen tiedoista (TAX_INCOMES-valmisaineiston taulut delivery, report ja transactionInfo), mutta muutamia johdettuja muuttujia on muodostettu ennen kuin tiedot summataan kuukausitasolle (apu, kokAik, vajaa, minEmploymentStartDate ja KVV). Kaikkia tulolajeja ei ole poimittu erikseen, vaan osa on summattu yhteen. Summat on muodostettu siten, että yksi tulolaji summautuu vain yhden kerran . 

Tämä valmisaineisto on muodostettu TAX_INCOMES-valmisaineiston rinnalle ”helppokäyttöisemmäksi” palkkatietoaineistoksi. Emme luvita tätä aineistoa käytettäväksi TAX_INCOMES-valmisaineiston kanssa yhdessä ilman hyvin perusteltua syytä. 

Kaikki maksajat ovat aineistossa mukana tunnustyypistä riippumatta, ja tulonsaajista on pyritty rajaamaan oikeudelliset henkilöt pois. Palautukset ja perusteettomat edut rajataan tulolajeista pois. Tällöin siis ilmoitukset menevät oikein, jos ilmoittaja on ilmoittanut tulorekisteriin molemmat. Toinen tapa tehdä tämä olisi käyttää palautuksen yhteydessä annettavaa tietoa alkuperäisestä maksujaksosta, mutta tämä olisi työläs toteuttaa ja siitä saatavat hyödyt ovat vielä selvittämättä. 

Sijaismaksajien lähetykset on rajattu pois. Sijaismaksajien toimiessa ilmoitukset tulisi tehdä kahteen kertaan. Yhden tekee sijaismaksaja ja toisen varsinainen työnantaja. Koska datamartissa ei ole tietoa varsinaisesta työnantajasta sijaismaksajan toimiessa, niin on päädytty käyttämään sijaismaksajien osalta vain tulolajeja 321-325, jotka varsinaisen työnantajan tulisi ilmoittaa. Ikävä kyllä on käynyt ilmi, että varsinaiset työnantajat eivät aina tee ilmoitusta. Tämä aiheuttaa pientä katoa palkkasummissa. 

Aineistoon on muodostettu muuttujat tyoAlku ja tyoLoppu kuvaamaan työjaksojen aloitusta ja lopetusta. Näiden mukaan tiedot jaetaan eri kuukausille. Työnaloitusmuuttuja on maksujakson aloituspäivä, ellei työsuhteen aloitukseksi ole merkitty päivä, joka sijoittuu maksujakson sisään. Vastaavasti työn lopetus on maksujakson loppupäivä, ellei työsuhteen lopetuspäivä ole maksujakson sisällä. 


Tulorekisterin tietoja julkaistaessa on noudatettava henkilötiedoissa kynnyssääntöä (10) ja yrityksissä kynnyssääntöä (5) sekä lisäksi dominanssisääntöä (1,75). Yhdistetyissä työntekijä-työnantaja-aineistoissa on suojattava sekä henkilö- että yritystaso eli kussakin taulukon solussa on oltava työntekijöitä vähintään viidestä eri yrityksestä. Dominanssisääntöä on käytettävä esimerkiksi, jos yhden yrityksen palkkasumma muodostaa yli 75 prosenttia tietyn toimialan (sektorin tms.) yritysten palkkasummasta tai jos esim. tietyn ammattiryhmän palkansaajista yli 75 prosenttia työskentelee jossain tietyssä yrityksessä.

Lisätietoja Tilastokeskuksen Tutkijapalveluista: tutkijapalvelut@stat.fi ja Verohallinnon sivuilta: vero.fi/tulorekisteri

## Muuttujat / Variables (53)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `vuosi` | Vuosi | — | — | — |
| `kuukausi` | Kuukausi | — | — | — |
| `payerIdType` | Maksajan tunnisteen tyyppi | — | — | — |
| `payerIdCode_s` | Maksajan suojattu yritystunnus | — | — | — |
| `payerOtherIdCode_s` | Maksajan suojattu muu tunnus | — | — | — |
| `payerShnro` | Maksajan suojattu henkilönumero | — | — | — |
| `incomeEarnerIdType` | Tulonsaajan tunnisteen tyyppi | — | — | — |
| `incomeEarnerShnro` | Tulonsaajan suojattu henkilönumero | — | — | — |
| `kokoAikaisuus` | Kokoaikaisuus (kokAik) | — | — | — |
| `tyosuhdeKatkennut` | Vajaa (vajaa) | — | — | — |
| `employmentCode` | Palvelussuhteen tyyppi | — | — | — |
| `parttime` | Osa-aikaisuuden prosentti | — | — | — |
| `hoursperWeek` | Säännöllinen sovittu viikkotyöaika | — | — | — |
| `employed` | Palvelussuhteessa | — | — | — |
| `pensionActCode` | Tieto työeläkevakuutuksesta | — | — | — |
| `pensionProvIdCode_s` | Työeläkelaitoksen suojattu yhtiötunnus | — | — | — |
| `incomeEarnerType` | Tulonsaajan tunnisteen tyyppi | — | — | — |
| `termCode` | Palvelussuhteen kesto | — | — | — |
| `CBACode` | Sovellettava työehtosopimus | — | — | — |
| `professionCode1` | Ammattiluokka (TK10) | — | — | — |
| `professionCode2` | Ammattiluokka (Keva) | — | — | — |
| `professionCode3` | Ammattiluokka (Suomen Pankki) | — | — | — |
| `professionCode4` | Ammattiluokka (Trafi) | — | — | — |
| `placeOfBusiness_s` | Suojattu toimipaikan tunnus | — | — | — |
| `nonResident` | Rajoitetusti verovelvollinen | — | — | — |
| `paymentType` | Palkkauksen muoto | — | — | — |
| `minEmploymentStartDate` | Aikaisin palvelussuhteen alkupäivä (minEmploymentStartDate) | — | — | — |
| `minPaymentStartDate` | Aikaisin maksujakson alkupäivä (minPaymentStartDate) | — | — | — |
| `KuunViimeinenViikko` | Kuukauden viimeinen viikko (KVV) | — | — | — |
| `t101` | Palkka yhteissumma | — | — | — |
| `t201` | Aikapalkka | — | — | — |
| `t202` | Aloitepalkkio | — | — | — |
| `t213` | Lomaraha | — | — | — |
| `t216` | Muu maksettu lisä | — | — | — |
| `t218` | Olosuhdelisä | — | — | — |
| `t220` | Provisiopalkka | — | — | — |
| `t221` | Sunnuntaityökorvaus | — | — | — |
| `t225` | Työajantasauskorvaus | — | — | — |
| `t227` | Urakkapalkka | — | — | — |
| `t230` | Varallaolokorvaus | — | — | — |
| `t232` | Viikkolepokorvaus | — | — | — |
| `t234` | Vuosilomakorvaus | — | — | — |
| `t238` | Muu säännöllinen lisä | — | — | — |
| `t312` | Kunnaneläinlääkärin toimenpidepalkkio | — | — | — |
| `t419` | Vähennys ennen ennakonpidätystä | — | — | — |
| `Luontoisedut` | — | — | — | — |
| `YlityoAnsiot` | — | — | — | — |
| `Tyoaikalisat` | — | — | — | — |
| `Tulospalkkiot` | — | — | — | — |
| `muutTulolajit1` | — | — | — | — |
| `muutTulolajit2` | — | — | — | — |
| `muutTulolajit3` | — | — | — | — |
| `sijaismaksajanPalkat` | — | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `vuosi` — Vuosi

#### `kuukausi` — Kuukausi

#### `payerIdType` — Maksajan tunnisteen tyyppi

Maksajan tunnisteen tyyppi

#### `payerIdCode_s` — Maksajan suojattu yritystunnus

Pakollisuus (K/E) = K

#### `payerOtherIdCode_s` — Maksajan suojattu muu tunnus

#### `payerShnro` — Maksajan suojattu henkilönumero

Maksajan suojattu henkilönumero, muodostetaan Tilastokeskuksessa.

#### `incomeEarnerIdType` — Tulonsaajan tunnisteen tyyppi

Tulonsaajan tunnisteen tyyppi

#### `incomeEarnerShnro` — Tulonsaajan suojattu henkilönumero

Tulonsaajan suojattu henkilönumero

#### `kokoAikaisuus` — Kokoaikaisuus (kokAik)

Kokoaikaisuus tieto on muodostettu työaikaa käsittelevistä muuttujista palvelussuhteen tyyppi (employmentCode), säännöllinen sovittu viikkotyöaika (hoursPerWeek) ja osa-aikaisuuden prosentti (parttime). Muuttujaa käytetään kokoaikaisuuden estimoinnissa.

#### `tyosuhdeKatkennut` — Vajaa (vajaa)

Tämä on apumuuttuja kokoaikaisuuden estimointia varten. Kuvaa tapauksia joissa työsuhde on alkanut tai loppunut kesken maksujakson.

#### `employmentCode` — Palvelussuhteen tyyppi

Palvelussuhteen tyyppi

#### `parttime` — Osa-aikaisuuden prosentti

Osa-aikaisuuden prosentti

#### `hoursperWeek` — Säännöllinen sovittu viikkotyöaika

Säännöllinen sovittu viikkotyöaika

#### `employed` — Palvelussuhteessa

Palvelussuhteessa

#### `pensionActCode` — Tieto työeläkevakuutuksesta

Tieto työeläkevakuutuksesta

#### `pensionProvIdCode_s` — Työeläkelaitoksen suojattu yhtiötunnus

#### `incomeEarnerType` — Tulonsaajan tunnisteen tyyppi

Tulonsaajan tunnisteen tyyppi

#### `termCode` — Palvelussuhteen kesto

Palvelussuhteen kesto

#### `CBACode` — Sovellettava työehtosopimus

Sovellettava työehtosopimus

#### `professionCode1` — Ammattiluokka (TK10)

Ammattiluokka (TK10)

#### `professionCode2` — Ammattiluokka (Keva)

Ammattiluokka (Keva)

#### `professionCode3` — Ammattiluokka (Suomen Pankki)

Ammattiluokka (Suomen Pankki)

#### `professionCode4` — Ammattiluokka (Trafi)

Ammattiluokka (Trafi)

#### `placeOfBusiness_s` — Suojattu toimipaikan tunnus

#### `nonResident` — Rajoitetusti verovelvollinen

Rajoitetusti verovelvollinen

#### `paymentType` — Palkkauksen muoto

Palkkauksen muoto

#### `minEmploymentStartDate` — Aikaisin palvelussuhteen alkupäivä (minEmploymentStartDate)

Poimitaan palvelussuhteen aikaisin alkupäivä eli pienin arvo muuttujasta employmentStartDate. Kyseinen muuttuja on vapaaehtoinen, joten tietoa ei löydy kaikille. Tietoa käytetään esimerkiksi palkkarakenteessa.

#### `minPaymentStartDate` — Aikaisin maksujakson alkupäivä (minPaymentStartDate)

Poimitaan aikaisin palvelussuhteelle kohdistuva maksujakson aloituspäivä.

#### `KuunViimeinenViikko` — Kuukauden viimeinen viikko (KVV)

Kuukauden viimeinen viikko saa arvon 1, jos palvelussuhteella on kohdistunut palkkailmoitus kuukauden viimeiselle viikolle. Tietoa hyödynnetään työssäkäyntitilastossa.

#### `t101` — Palkka yhteissumma

#### `t201` — Aikapalkka

#### `t202` — Aloitepalkkio

#### `t213` — Lomaraha

#### `t216` — Muu maksettu lisä

#### `t218` — Olosuhdelisä

#### `t220` — Provisiopalkka

#### `t221` — Sunnuntaityökorvaus

#### `t225` — Työajantasauskorvaus

#### `t227` — Urakkapalkka

#### `t230` — Varallaolokorvaus

#### `t232` — Viikkolepokorvaus

#### `t234` — Vuosilomakorvaus

#### `t238` — Muu säännöllinen lisä

#### `t312` — Kunnaneläinlääkärin toimenpidepalkkio

#### `t419` — Vähennys ennen ennakonpidätystä

#### `Luontoisedut`

#### `YlityoAnsiot`

#### `Tyoaikalisat`

#### `Tulospalkkiot`

#### `muutTulolajit1`

#### `muutTulolajit2`

#### `muutTulolajit3`

#### `sijaismaksajanPalkat`

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
