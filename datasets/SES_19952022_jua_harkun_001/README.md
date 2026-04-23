# Harmonisoitu palkkarakennepaneeli - kuntasektori 1995-2022

- **Identifier:** `SES_19952022_jua_harkun_001.xml`
- **DOI:** `ati_2014-05_2014-05-15_ain_0001`
- **Temporal coverage:** 1995-01-01 - 2022-12-31
- **Published:** 2024-12-31
- **Organisation:** Tilastokeskus
- **Variable count:** 33
- **Observation count:** 12,073,966
- **Population:** Kuntasektorin tuntipalkat, kuntasektorin kuukausipalkat
- **Source:** Kuntasektorin tuntipalkat, kuntasektorin kuukausipalkat, kuntasektorin palkkarakenneaineistot (harmonisoimattomat vuosipoikkileikkaukset)
- **Keywords:** ansiotaso,palkansaajat,palkat,yksityinen sektori

## Description

Kuntasektorin harmonisoitu palkkarakennepaneeli vuosilta 1995-2022 tarjoaa työsuhdetason tietoa palkansaajien
(palkatuista) tunneista, palkoista ja palkanosista + yksilötason tietoa työntekijän iästä, koulutuksesta yms. + tietoa työsuhteesta vastaavan kunnan tai kuntayhteisön paikallisyksikön toimialasta jne (yhteensä 33 muuttujaa). Tilasto on kokonaisaineisto kattaen kaikki kuntien ja kuntayhtymien työ- ja virkasuhteiset palkansaajat (12073966 työsuhdehavaintoa). 

Tiedot on harmonisoitu keskenään vertailukelpoisiksi sekä suhteessa yksityisen ja valtiosektorin vastaaviin palkkatilastokäsitteisiin että yli vuosien. Siinä missä alkuperäinen palkkarakenneaineisto takaa sektorien välisen vertailtavuuden saman tilastovuoden sisällä, takaa harmonisoitu palkkarakenneaineisto lisäksi vielä sen, että käytettävät muuttujat todella mittaavat/kuvaavat samaa asiaa tilastovuodesta riippumatta. Vuosien yli harmonisoinnissa noudattavat harmonisoidut muuttujat vuoden 2022 kuntasektorin palkkarakenneaineiston yhteydessä käytettyjä muuttujien muodostussääntöjä ja luokitusmuuttujien luokitusversioita. HAR_ -etuliite muuttujan nimen alussa viittaa yli ajan harmonisoituun muuttujaan. Loput mukaan otetuista muuttujista olivat yli ajan harmonisoidussa muodossa jo vuosipoikkileikkausaineistoissa.

## Variables (33)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `VUOSI` | Tilastovuosi | — | — | — |
| `AINE` | Aineistotunnus | — | — | — |
| `SHNRO` | Suojattu henkilönumero | — | — | — |
| `SYRTUN_L` | Suojattu yritys-/yhteisötunnus | — | — | — |
| `SYRTUN_P` | Suojattu yritys-/yhteisötunnus | — | — | — |
| `PYKSKUNTA` | Paikallisyksikön sijaintikunta. Aineiston harmonisointivuoden (2022) kuntatunnukset: https://stat.fi/fi/luokitukset/kunta/kunta_1_20220101/. | — | — | — |
| `PMUOTO` | Palkkausmuoto | — | — | — |
| `SUKU` | Palkansaajan sukupuoli | — | — | — |
| `IKA` | Palkansaajan ikä | vv | — | — |
| `HAR_BASIS0` | Mukaanottorajaus työntekijä- ja työsuhdemääriä koskeviin havaintomäärälaskelmiin. | — | — | — |
| `HAR_BASIS1` | Mukaanottamisehto HAR_TUNTIPALKKA-muuttujaa koskeville laskelmille | — | — | — |
| `HAR_BASIS2` | Havainnon mukaanottamisehto HAR_KKPALKKA-muuttujaa koskeville laskelmille. | — | — | — |
| `HAR_AML2010` | Tilastokeskuksen AML2010-ammattiluokitus (kansallinen ISCO) | — | ammatti_1_2010_01_01 | — |
| `HAR_PYKSTOL08` | Paikallisyksikön toimiala TOL08 | — | toimiala_910_2008_01_01 | — |
| `HAR_TUTK1` | Tutkintokoodi | — | koulutus_1_2016_01_01 | — |
| `HAR_TUTK1_VUODET` | Tutkinnon pituus | — | — | — |
| `HAR_OSAIK` | Osa-aikaisuus | — | — | — |
| `HAR_VKTA` | Säännöllinen sovittu viikkotyöaika | — | — | — |
| `HAR_TYOAIKAKK` | Kokonaistyöaika | — | — | — |
| `HAR_YLIT` | Ylityötunnit | — | — | — |
| `HAR_KKSANS` | Säännöllisen työajan kuukausiansio | — | — | — |
| `HAR_TPSANS` | Säännöllisen työajan tuntiansio | — | — | — |
| `HAR_LED` | Luontoisedut | — | — | — |
| `HAR_PROV` | Provisiot | — | — | — |
| `HAR_VTL` | Työaikalisät | — | — | — |
| `HAR_KKSANSLIS` | Säännöllisen työajan palkanlisät | — | — | — |
| `HAR_VKORV` | Varallaolokorvaukset | — | — | — |
| `HAR_YLIP` | Ylityöansiot | — | — | — |
| `HAR_KKPALKKA` | Kokonaiskuukausiansiot | — | — | — |
| `HAR_TUNTIPALKKA` | Tuntiansiot | — | — | — |
| `HAR_TULOSPA` | Tulospalkkiot | € | — | — |
| `HAR_LOMARAHA` | Lomarahat | — | — | — |
| `HAR_SOPALA` | Työ-/virkaehtosopimus | — | — | — |

### Variable definitions

#### `VUOSI` — Tilastovuosi

Tilaston tilastointivuosi. Tässä tiedostossa 1995-2022. Tiedot kuvaavat pääasiassa vuoden viimeistä neljännestä. Vuosittainen tilastointiajankohta on lokakuu ja tilastointijakso voi pisimmillään olla yksi kuukausi (jos ilmoitusjakso ei satu täysin lokakuulle, niin ilmoitusajankohdaksi valitaan  syys–lokakuulle osuvat viikot).

#### `AINE` — Aineistotunnus

Aineistotunnuksella erotetaan eri tiedonantajalähteet toisistaan. Kuntasektorilla mahdollisia arvoja vv. 1995-2022 vain yksi, 
K=kuntien ja kuntayhteisöjen palkansaajat.

#### `SHNRO` — Suojattu henkilönumero

Suojattu TK:n henkilönumero.

#### `SYRTUN_L` — Suojattu yritys-/yhteisötunnus

Suojattu yritys-/yhteisötunnus (ilman väliviivaa)

#### `SYRTUN_P` — Suojattu yritys-/yhteisötunnus

Suojattu yritys-/yhteisötunnus (ml. väliviiva)

#### `PYKSKUNTA` — Paikallisyksikön sijaintikunta. Aineiston harmonisointivuoden (2022) kuntatunnukset: https://stat.fi/fi/luokitukset/kunta/kunta_1_20220101/.

Tieto toimipaikan tai paikallisyksikön sijaintikunnasta. Tieto saadaan yritysrekisteristä (YTY) tai suoraan palkka-aineistosta. Aineiston harmonisointivuoden (2022) kuntatunnukset: https://stat.fi/fi/luokitukset/kunta/kunta_1_20220101/.

#### `PMUOTO` — Palkkausmuoto

Työsuhteen palkkausmuoto. Mahdolliset arvot vv 1995-2022: 
1 - Kuukausipalkkainen 
2 - Tuntipalkkainen.

#### `SUKU` — Palkansaajan sukupuoli

Tieto sukupuolesta. Muodostetaan pääasiassa henkilötunnuksen perusteella. 1=mies, 2=nainen.

#### `IKA` — Palkansaajan ikä

**Unit:** vv

Palkansaajan ikä vuosina. Lasketaan henkilön syntymävuoden mukaan henkilötunnuksen perusteella.

#### `HAR_BASIS0` — Mukaanottorajaus työntekijä- ja työsuhdemääriä koskeviin havaintomäärälaskelmiin.

Harmonisoitu rajausehto. Arvo=1 tietueilla, jotka otetaan mukaan palkansaajien lukumääriä laskettaessa. Muuten arvo=0. Huom! Aineisto sisältää myös VUOSI*SHNRO-tuplia. Palkkarakenneaineistossa "hyväksytään" vain yksi kokoaikainen (HAR_OSAIK=1) työsuhdehavainto ja korkeintaan kolme osa-aikaista (HAR_OSAIK=2) työsuhdehavaintoa per henkilö ja vuosi. Valitsemalla datarajaus HAR_BASIS0=1 voi varmistaa, että vain "hyväksytyt" henkilö*vuosi -tupla-/triplahavainnot otetaan ainestoa käytettäessä mukaan.

#### `HAR_BASIS1` — Mukaanottamisehto HAR_TUNTIPALKKA-muuttujaa koskeville laskelmille

Harmonisoitu rajausehto. Arvo=1 tietueilla, jotka voidaan ottaa mukaan kokonaistyöajan kokonaistuntiansioita (HAR_TUNTIPALKKA) koskeviin laskelmiin ja tarkasteluihin. Muuten arvo=0.

#### `HAR_BASIS2` — Havainnon mukaanottamisehto HAR_KKPALKKA-muuttujaa koskeville laskelmille.

Harmonisoitu rajausehto. Arvo=1 tietueilla, jotka voidaan ottaa mukaan kokonaistyöajan kuukausiansioita (HAR_KKPALKKA) koskeviin tarkasteluihin. Muuten arvo=0.

#### `HAR_AML2010` — Tilastokeskuksen AML2010-ammattiluokitus (kansallinen ISCO)

**Classification:** ammatti_1_2010_01_01

Harmonisoitu kansainväliseen ISCO-ammattiluokitukseen pohjautuva Tilastokeskuksen virallinen kansallinen ammattiluokitus. Ammattiluokituksen pohjana ovat alakohtaiset työnantajien ja Tilastokeskuksen ylläpitämät ammattinimikeluokitukset, jotka on käännösavaimella muokattu sekä kansallisen että kansainvälisen virallisen ammattiluokituksen mukaiseksi. Käytössä kansallinen ammattiluokitus 2010 (AML2010).

#### `HAR_PYKSTOL08` — Paikallisyksikön toimiala TOL08

**Classification:** toimiala_910_2008_01_01

Kunnan tai kuntayhteisön paikallisyksikön toimiala. Perustuu kansainväliseen TOL2008 toimialaluokitukseen. Toimiala on mahdollista luokitella usealle eri tasolle.

#### `HAR_TUTK1` — Tutkintokoodi

**Classification:** koulutus_1_2016_01_01

Harmonisoitu tutkintokoodi. Palkansaajan viimeisin ja korkein tutkinto tilastovuoden lopussa. Käytössä Unescon kansainväliseen ISCED 2011 -luokitukseen perustuva Tilastokeskuksen ylläpitämä kansallinen Koulutusluokitus 2016 -sovellus. Tutkinnot poimitaan Tilastokeskuksen tutkintorekisteristä prioriteettikentän korkeimman prioriteettiarvon mukaan. Perusasteen tutkintoa (tutkintoaste 0,1, tai 2) omaamattomilla henkilöillä tutkintoarvo on tyhjä. Lisäksi rekisteriin tutkintotiedot on voitu viedä vain niille henkilöille, joilla on suomalainen henkilötunnus. Tästä syystä tutkintorekisteristä puuttuvat henkilötunnusta vailla olevien henkilöiden (esim. monien ulkomaalaisten) tutkintotiedot ja tutkintoarvo on siten tyhjä.

#### `HAR_TUTK1_VUODET` — Tutkinnon pituus

Harmonisoidut tutkintoasteet koulutusvuosina.

#### `HAR_OSAIK` — Osa-aikaisuus

Harmonisoitu työsuhteen koko-  tai osa-aikaisuus -tieto. Muodostetaan palvelussuhteen ehtojen ja säännöllisen viikkotyöajan mukaan. Osa-aikaisuuden määrittelyssä rajana pidetään 90 prosenttia alan yleisestä säännöllisestä työajasta. 
Mahdolliset arvot: 
1 - Kokoaikainen, 
2 - Osa-aikainen.

#### `HAR_VKTA` — Säännöllinen sovittu viikkotyöaika

Harmonisoitu palkansaajan henkilökohtainen sovittu säännöllinen viikkotyöaika. Kattaa sekä koko- että osa-aikaiset työsuhteet ja määritettävä työsopimuslain mukaisesti kirjallisesti joko työsopimuksessa tai työnantajan antamassa työnteon keskeisiä ehtoja koskevassa selvityksessä. Säännöllisen viikkotyöajan on noudatettava työaikalakia ja mahdollista työsuhteessa noudatettavaa työ-/virkaehtosopimusta. Todellisen työssöoloajan ohella myös TES:in/VES:in mukaiselle säännölliselle työssäoloajalle sijoittuvat palkattomat ja palkalliset poissaolot sisältyvät käsitteeseen.

#### `HAR_TYOAIKAKK` — Kokonaistyöaika

Harmonisoitu kokonaistyöaika kuukaudessa. Säännöllisen kuukausityöajan ja lisä- ja ylityötuntien yhteissumma kuukaudessa. Lisä- ja ylityötunnit (HAR_YLIT) kuvaavat yksinomaan todellisia palkattuja työssäolotunteja. Sen sijaan säännöllisen kuukausityöajan tunnit (=HAR_TYOAIKAKK-HAR_YLIT) kattavat todellisen työssöoloajan ohella myös TES:in/VES:in määrittämälle työssäoloajalle sijoittuvat palkattomat ja palkalliset poissaolotunnit.

#### `HAR_YLIT` — Ylityötunnit

Palkatut lisä- ja ylityötunnit kuukaudessa. Lisätyötunteja ovat työtunnit,  jotka ylittävät työntekijään sovellettavassa työ- ja työehtosopimuksessa sovitun säännöllisen työajan työtuntimäärän, mutta eivät työaikalain määrittämää säännöllisen työajan enimmäismäärää. Työaikalain mukaisen säännöllisen työajan enimmäismäärän ylittäviä työtunteja kutsutaan ylityötunneiksi.

#### `HAR_KKSANS` — Säännöllisen työajan kuukausiansio

Harmonisoitu säännöllisen (TES/VES) työajan kuukausiansio. Säännölliseltä työajalta maksetun ansion määrä euroina kuukaudessa. Harmonisoituun säännöllisen työajan kuukausiansioon luetaan kultakin palkanmaksujaksolta peruspalkka + tehtävän, ammattitaidon, palvelusvuosien yms. perusteella maksettavat lisät + työpaikan sijainnin ja olosuhteiden perusteella maksettavat lisät + työaikalisät + määrältään vaihtelevat mutta säännöllisesti palkanmaksujaksoittain maksettavat provisiot (myyntiprovisiot, toimihenkilöiden yksilötason työsuoritukseen pohjaavat tulos- ja suoritusperusteiset palkanosat ja työntekijöiden yksilötason työsuoritukseen perustuvat suoritusperusteiset ansiot) + luontoisetujen verotusarvo. Säännöllisen työajan ansio ei sisällä varallaolokorvauksia eikä kertaluonteisia tai epäsäännöllisesti maksettavia palkkaeriä, kuten lomarahaa ja usean työntekijän tai koko yrityksen kollektiivisen työsuoritukseen tai tulokseen pohjautuvia (lähinnä kerran vuodessa maksettavia) tulospalkkioita.

#### `HAR_TPSANS` — Säännöllisen työajan tuntiansio

Harmonisoitu säännöllisen työajan tuntiansio. Säännölliseltä työajalta maksetun ansion määrä euroina tunnissa. Muodostettu säännöllisen työajan kuukausiansiosta (HAR_KKSANS) jakamalla se säännöllisen työajan tuntien (=HAR_TYOAIKAKK-HAR_YLIT) määrällä kuukaudessa. Harmonisoituun säännöllisen työajan tuntiansioon luetaan kultakin palkanmaksujaksolta peruspalkka + tehtävän, ammattitaidon, palvelusvuosien yms. perusteella maksettavat lisät+ työpaikan sijainnin ja olosuhteiden perusteella maksettavat lisät + työaikalisät + provisiot + luontoisetujen verotusarvo. Säännöllisen työajan ansio ei sisällä varallaolokorvauksia eikä kertaluonteisia tai epäsäännöllisesti maksettavia palkkaeriä, kuten lomarahaa ja usean työntekijän tai koko organisaation kollektiivisen työsuoritukseen tai tulokseen pohjautuvia tulospalkkioita.

#### `HAR_LED` — Luontoisedut

Harmonisoitujen veronalaisten luontoisetujen arvo euroina kuukaudessa. Esimerkiksi auto- tai puhelinetu.

#### `HAR_PROV` — Provisiot

Harmonisoidut jokaisen säännöllisen palkanmaksun yhteydessä maksettavat provisiot ja muut vastaavat yksilön työsuoritukseen perustuvat ansiot euroina kuukaudessa (vrt. HAR_TULOSPA vuodessa!). Kuntasektorilla näitä edustavat vain tuntipalkkaisten työsuhteiden kappalemäärä-/suoritusperusteiset urakkapalkat eli kuntasektorilla HAR_PROV=0 aina, kun  PMUOTO=1 (=kuukausipalkkainen työsuhde).

#### `HAR_VTL` — Työaikalisät

Harmonisoitujen vuoro-  ym. työaikalisien euromäärä kuukaudessa. Esimerkiksi vuoro-, yö-, ilta-, viikonloppu- ja arkipyhätyöltä maksetut palkanosat.

#### `HAR_KKSANSLIS` — Säännöllisen työajan palkanlisät

Harmonisoidut säännölliseltä työajalta maksetut palkanlisät euroina kuukaudessa. Säännöllisen työajan palkanlisiin lasketaan työpaikan sijainnin ja olosuhteiden perusteella maksettavat lisät + työaikalisät + provisiot (yksityisen sektorin myyntiprovisiot, toimihenkilöiden yksilötason työsuoritukseen pohjaavat tulos- ja suoritusperusteiset palkanosat ja työntekijöiden yksilötason työsuoritukseen perustuvat suoritusperusteiset ansiot) + luontoisetujen verotusarvo. Näin ollen HAR_KKSANSLIS kattaa mm. muuttujat HAR_OLS, HAR_VTL, HAR_PROV ja HAR_LED ja se sisältyy kokonaisuudessaan HAR_KKPALKKA-muuttujan arvoon.

#### `HAR_VKORV` — Varallaolokorvaukset

Harmonisoidut varallaoloajan palkat ja muut kokonaisansion lisät, kuten toimenpidepalkkiot euromääräisinä tilastokuukaudelta.

#### `HAR_YLIP` — Ylityöansiot

Harmonisoitu yli- ja lisätyöajalta maksettu kokonaispalkka (normaali tuntipalkka + ylityölisä) euromääräisenä tilastokuukaudelta.

#### `HAR_KKPALKKA` — Kokonaiskuukausiansiot

Harmonisoitu kokonaistyöajan kuukausiansio. Säännölliseltä työajalta sekä lisä- ja ylityöltä maksetun ansion määrä euroina kuukaudessa.
Sisältää myös mahdolliset varallaolokorvaukset ja luontoisedut. Ei kuitenkaan sisällä epäsäännöllisiä kertaluontoisesti (yleensä kerran vuodessa) maksettavia kollektiiviseen työsuoritukseen perustuvia tulospalkkoja (HAR_TULOSPA).

#### `HAR_TUNTIPALKKA` — Tuntiansiot

Harmonisoitu kokonaistyöajan tuntiansio. Säännölliseltä työajalta sekä lisä- ja ylityöltä maksetun ansion määrä euroina tunnissa. Muodostettu kuukausiansiosta (HAR_KKPALKKA) jakamalla se kokonaistyöajan tuntien määrällä (HAR_TYOAIKAKK).

#### `HAR_TULOSPA` — Tulospalkkiot

**Unit:** €

Harmonisoidut kertaluontoisesti  ja epäsäännöllisesti (lähinnä kerran vuodessa) maksettavat kollektiiviseen työsuoritukseen perustuvat tulospalkkiot euroina vuodessa (vrt HAR_PROV kuukaudessa!).

#### `HAR_LOMARAHA` — Lomarahat

Harmonisoidut lomarahat ja lomakorvaukset euroina vuodessa.

#### `HAR_SOPALA` — Työ-/virkaehtosopimus

Kuntasektorin työ-/virkaehtosopimus. Mahdolliset arvot:

01 -  Kunnallinen yleinen virka- ja työehtosopimus (KVTES) 
02 - Kunta-alan opetushenkilöstön virka- ja työehtosopimus (OVTES) 
03 - Kunta-alan teknisen henkilöstön virka- ja työehtosopimus (TS) 
04 - Kunnallinen lääkärien virkaehtosopimus (LS) 
05 - Muu (esim. muusikot, näyttelijät, satamajäänmurtajat) 
07 - Sosiaali- ja terveydenhuollon henkilöstön työ- ja virkaehtosopimus (SOTE)
010 - Kunta-alan tuntipalkkaisen henkilöstön työehtosopimus (TTES)

---

[← Back to catalogue](../../README.md)
