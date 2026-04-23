# FIRM_CPI Kuluttajahintaindeksin yksikkötason aineisto vuosilta 1997-2018 (YA272)

- **Identifier:** `FIRM_19972018_jua_cpi_001.xml`
- **DOI:** `khi_2017-05_2017-05-17_ain_0001`
- **Temporal coverage:** 1997-01-01 - 2018-12-31
- **Published:** 2017-11-08
- **Organisation:** Tilastokeskus
- **Variable count:** 39
- **Observation count:** —
- **Source:** <a href= "http://www.stat.fi/til/khi/">Kuluttajahintaindeksi</a>
- **Keywords:** hinnat,kuluttajahinnat

## Description

Kuluttajahintaindeksin yksikkötason aineisto sisältää kuluttajahintaindeksin laskentaa varten liikkeistä kuukausittain kerätyt hyödykkeiden hintatiedot alkaen vuodesta 1997.

Tilastossa käytetään yksityisen kulutuksen käyttötarkoituksen mukaista hyödykeluokitusta (European Classificiation Of Individual Consumption by Purpose, eCOICOP). eCOICOP on yksi Yhdistyneiden Kansakuntien kansantalouden tilinpitojärjestelmän mukaisista luokituksista. Kansallista käyttöä varten luokitusta on edelleen jonkin verran tarkennettu.

Tilastokeskuksen haastattelijat keräävät kuluttajahintaindeksiä varten kuukausittain noin 50 000 päivittäistavaroiden, kestokulutushyödykkeiden ja palvelujen hintaa lähes 500 hyödykkeestä noin 2 700 liikkeestä. Nämä hinnat kattavat noin 50 prosenttia kulutuskorin arvosta. Lisäksi hintatietoja kerätään keskitetysti Tilastokeskuksessa. Lähteenä käytetään myös muita tilastoja, mm. Tilastokeskuksen vuokratilastoa, osakeasuntojen hintatilastoa, kiinteistöjen hintaindeksiä ja rakennuskustannusindeksiä. Tietoja tuottavat myös muut viranomaiset, kuten Terveyden ja hyvinvoinnin laitos (THL) ja Kela.

Kulutuskorin rakenne ja siihen liittyvät hyödykeotokset on uusittu viiden vuoden välein vuoteen 2012 asti. Vuodesta 2013 alkaen kulutuskorin rakenne ja siihen liittyvät hyödykkeet päivitetään vuosittain tammikuussa. Muutos joulukuusta tammikuuhun lasketaan siten, että joulukuun indeksi =100. 

Kuukausittaisen hintaseurannan peruslähde on kuluttajahintaindeksin oma tiedonkeruu, joka päivittäistavaroiden osalta perustuu liikevaihdolla painotettuun otokseen vähittäiskaupoista. Kestokulutus- ja puolikestävien tavaroiden keruu perustuu harkinnanvaraiseen liikeotokseen suurimmista kaupungeista. Muista tilastojärjestelmistä tulevat hintatiedot on kuvattu erikseen näiden tilastojen omien kuvausten yhteydessä.

Kausihyödykkeiden, kuten talvi- ja kesävaatteiden osalta hintakeruu tapahtuu niinä kuukausina, kun hyödykkeitä on saatavilla ja ne ovat edustavia. Kauden jälkeen palautetaan indeksin taso alennusmyyntikauden jälkeen normaalitasolle. Samalla kyseisen hyödykkeen painot nollataan ja jaetaan muille saman ryhmän hyödykkeille. 

Markkinoille tulevien uusien liikkeiden ja palveluiden tarjoajien sisällyttäminen kuluttajahintaindeksiin tapahtuu periaatteessa samalla tavalla kuin uusien tuotteiden.

Kuluttajahintaindeksin käyttäjän käsikirjat ja painot ovat saatavissa Tilastokeskuksen nettisivuilta: http://www.stat.fi/til/khi/men.html

Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@stat.fi.

## Variables (39)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `hyod` | Hyödyketunnus -- surrogaatti | — | coicop | — |
| `hitun` | Hintahavaintotunnus | — | — | — |
| `stat` | Status | — | — | — |
| `kt` | Keruutunnus | — | — | — |
| `lamu` | Laadunmuutoskoodi | — | — | — |
| `hinta` | Hinta | — | — | — |
| `hiko` | Hintakoodi | — | — | — |
| `maara` | Määrä | — | — | — |
| `nimi` | Hyödykkeen nimi | — | — | — |
| `sual` | Suuralue | — | nuts2 | — |
| `hyodtunnus` | Hyödyketunnus | — | coicop | — |
| `status` | Status | — | — | — |
| `slitun` | Suojattu liiketunnus | — | — | — |
| `kk` | Kuukausi | — | — | — |
| `nhinta` | Hinta | — | — | — |
| `nhinta_num` | Hinta | — | — | — |
| `maara_num` | Määrä, numeerinen | — | — | — |
| `ltyyppi` | Liiketyyppi | — | — | — |
| `yksikko` | Määräyksikkö | — | — | — |
| `kskoodi1` | Käyttökoodi | — | — | — |
| `kskoodi` | Käyttökoodi2 | — | — | — |
| `vuosi` | Tilastovuosi | — | — | — |
| `kuukausi` | Kuukausi | — | — | — |
| `tilastoaika` | Tilastoaika | — | — | — |
| `havaintokohde_tunnus` | Hyödyketunnus | — | coicop_31_2014_01_01 | — |
| `havaintokohde_nimi` | Hyödykkeen nimi | — | — | — |
| `havaintotapahtuma_tunnus` | Hintahavaintotunnus | — | — | — |
| `stiedonkohde_tunnus` | Suojattu liiketunnus | — | — | — |
| `arvo` | Hinta | — | — | — |
| `hintakasite` | Hintakäsite | — | — | — |
| `tieto` | Hintatieto | — | — | — |
| `valuutta` | Valuutta | — | — | — |
| `rahayksikko` | Rahayksikkö | — | — | — |
| `valid_hintakoodi` | Hintakoodi | — | — | — |
| `valid_laadunmuutoskoodi` | Laadunmuutoskoodi | — | — | — |
| `valid_maara` | Määrä | — | — | — |
| `maarayksikko` | Määräyksikkö | — | — | — |
| `suuralue` | Suuralue | — | nuts2 | — |
| `arvo_num` | Arvo, numeerinen | — | — | — |

### Variable definitions

#### `hyod` — Hyödyketunnus -- surrogaatti

**Classification:** coicop

Hyödykkeen/palvelun surrogaattitunnus. Vuosissa 1997-1999 käytettiin surrogaattitunnusta coicop-koodin sijaan. Vuodesta 2000 lähtien on käytetty coicop-koodia hyödykkeen yksilöimisessä.

#### `hitun` — Hintahavaintotunnus

Nelinumeroineinen hintahavaintotunnus. Yksilöi yhden hintahavaintotapahtuman siten, että se on tasolla hyödyketunnus--tilastoaika--liike. Käytössä vuosina 1997-2012.

#### `stat` — Status

Käytössä vuosina 1997-1999, vastaa mjaa "status" vuosissa 2000-2015. Kuvaa hintahavainnon aktiivisuustilaa. Passiivisia hintahavaintoja ei ole otettu laskentaan mukaan. 0=passive, 1=active.

#### `kt` — Keruutunnus

Kuvaa tiedonkeruun toteutusta ja kohdetta vuosina 1997-2012. Vaihtoehtoiset toteutustavat ovat haastattelijakeruu ja keskitetty keruu. Haastattelijakeruuseen kuuluvat koodit P ja A. In year 1997-1999 accepted values were 3, 4, 6, 7 while between 1.1.2000-31.12.2012 accepted values were  P=daily products collected by interviewer, A=other products collected by interviewer, K=centrally collected data collection.

#### `lamu` — Laadunmuutoskoodi

'=no quality change, 00=minor quality, 10=remarkable quality change. Käytössä vuosina 1997-2012.

#### `hinta` — Hinta

Vähittäismyyntihinta, sis. alv:n ja valmiste- ja muut verot. Ns. kuluttajan maksama hinta. Käytössä vuosina 1997-1999.

#### `hiko` — Hintakoodi

Kuvaa hintatietoa, onko se normaali hinta, alennettu hinta, puuttuva hinta vai uuden hyödykkeen hinta. T=normaalihinta, A=alennettu hinta, P=puuttuva hinta, U 00/U10=korvattu. Käytössä vuosina 1997-2012.

#### `maara` — Määrä

Pakkauksen koko/määrä. Käytössä vuosina 1997-2012.

#### `nimi` — Hyödykkeen nimi

Tuotteen tai palvelun nimi. Käytössä vuosina 1997-2012.

#### `sual` — Suuralue

**Classification:** nuts2

NUTS2 alueluokituksen mukainen koodi. Uudemmissa vuosissa käytetty mjanimeä "suuralue". 1=Uusimaa, 2=Southern Finland, 3=Eastern Finalnd, 4=Western Finland, 5=Northern Finland, 6=Ahvenanmaa, 7= Koko maa. Käytössä vuosina 1997-2012.

#### `hyodtunnus` — Hyödyketunnus

**Classification:** coicop

Hyödyketunnus, joka vastaa COICOP-luokituksen tarkimman tason kansallista  luokka-arvoa. Käytössä vuosina 2000-2012.

#### `status` — Status

Käytössä vuodesta 2000 alkaen, vastaa mjaa "stat" vuosissa 1997-1999. Kuvaa hintahavainnon aktiivisuustilaa. Passiivisia hintahavaintoja ei ole otettu laskentaan mukaan. 0=passiivinen, 1=aktiivinen.

#### `slitun` — Suojattu liiketunnus

Liiketunnus yksilöi liikkeen, josta hintatiedot on kerätty. Käytössä vuosina 2000-2012.

#### `kk` — Kuukausi

Vuosissa 1997-2012 käytetään kuukauden nimenä "kk", 2013-2015 "kuukausi".

#### `nhinta` — Hinta

Hyödykkeen tai palvelun nykyhinta. On sama asia kuin hinta-tieto mjanimella "hinta" tai "valid_hinta". 
Vähittäismyyntihinta, sis alv ja mahdolliset valmiste- ja muut verot. Käytössä vuosina 2000-2012.

#### `nhinta_num` — Hinta

Kuvaa samaa asiaa kuin mja "nhinta" mutta nyt tämä arvo on numeerisena datassa. Käytössä vain vuosissa 2000-2015

#### `maara_num` — Määrä, numeerinen

kuvaa saa kuin mja "maara" mutta tämä on numeerisessa muodossa. Käytössä vain vuosissa 2000-2015

#### `ltyyppi` — Liiketyyppi

Kuvaa liikkeen tyyppiä. 1,2,3,4 …10. Käytössä vuosina 2000-2012.

#### `yksikko` — Määräyksikkö

Käytössä vuosina 2009-2012.

#### `kskoodi1` — Käyttökoodi

ilmoittaa onko kyseinen hintahavainto käytössä KHI:ssä vai ei. x=yes, 0=no. Käytössä vuosina 2009-2012.

#### `kskoodi` — Käyttökoodi2

kuten käyttökoodi1. x=yes, 0=no.Käytössä vuosina 2009-2012.

#### `vuosi` — Tilastovuosi

#### `kuukausi` — Kuukausi

Alkaen vuodesta 2013.

#### `tilastoaika` — Tilastoaika

kuvaa tilastoaikaa selkokielisessä muodossa tilastovuosi+ kuukausi suomenkielellä. Alkaen vuodesta 2013.

#### `havaintokohde_tunnus` — Hyödyketunnus

**Classification:** coicop_31_2014_01_01

9-merkkinen havaintokohdetunnus, josta aiemmin käytettiin nimeä hyod tai hyodtunnus. Hyödyketunnus, joka vastaa COICOP-luokituksen tarkimman tason luokka-arvoa. HUOM! mjaan kytketty luokitus sisältää pisteet eikä sisällä loppunollia, mutta muuten koodisto on oikein vuodelle 2015. Alkaen vuodesta 2013.

#### `havaintokohde_nimi` — Hyödykkeen nimi

Kuvaa hyödykkeen nimen. Ennen käytetty termiä "nimi". Alkaen vuodesta 2013.

#### `havaintotapahtuma_tunnus` — Hintahavaintotunnus

Kuvaa yhden havaintotapahtuman tunnusta. Yksilöi havaintotapahtuman tasolla hyödyke-tilastoaika-liike. Ennen tätä vastaava on hitun. Alkaen vuodesta 2013.

#### `stiedonkohde_tunnus` — Suojattu liiketunnus

Yksilöi keruuliikkeen. Ennen käytetty vastaavasta tiedosta nimeä "slitun". Alkaen vuodesta 2013.

#### `arvo` — Hinta

Kuvaa hyödykkeen tai palvelun hintaa tai pistelukua, joka osoittaa hinnassa tapahtuvaa muutosta. Ennen käytetty mjanimeä "hinta" tai "nhinta". Alkaen vuodesta 2013.

#### `hintakasite` — Hintakäsite

Kuvaa hintatietoa. Käytetään yhdessä "arvo"-tiedon kanssa, jolloin tämä selittää sen onko kyseessä verollinen hinta, indeksipisteluku tmv. Vaihtoehtoiset arvot ovat NULL tai verollinen. NULL arvoa käytettäneen silloin kyse on indeksipisteluvusta arvo kentässä. Alkaen vuodesta 2013.

#### `tieto` — Hintatieto

Kuvaa arvo-kentän tiedon sisältöä. Vaihtoehtoiset arvot ovat NULL, hinta, indeksipisteluku. Alkaen vuodesta 2013.

#### `valuutta` — Valuutta

Valuuttaa kuvaava tieto. Voi saada arvon NULL, ei valuuttaa, euro. Alkaen vuodesta 2013.

#### `rahayksikko` — Rahayksikkö

Kuvaa rahayksikköä. Voi saada arvon NULL, ei rahayksikköä, kerroin, snt. Yleensä kaikki euromääräiset tiedot esitetään kahden desimaalin tarkkuudella. Alkaen vuodesta 2013.

#### `valid_hintakoodi` — Hintakoodi

Sama kuin termi "hiko". T=normal price, A=discount price, P=missing price, U=replacement, N=?. Alkaen vuodesta 2013.

#### `valid_laadunmuutoskoodi` — Laadunmuutoskoodi

Sama kuin "lamu". Käytetään yhdessä mjan valid_hintakoodi kanssa. U-hintakoodit liittyvät arvoihin 00 ja 10 ja P-hintakoodit arvoihin imp, IMP. 0=no quality change, 00=minor quality, 10=remarkable quality change, IMP=imputoitu arvo, NULL=puuttuva tieto, imp=imputoitu arvo. Alkaen vuodesta 2013.

#### `valid_maara` — Määrä

Sama kuin mja "maara". Alkaen vuodesta 2013.

#### `maarayksikko` — Määräyksikkö

Mittayksikkö jossa määrä on ilmoitettu. Sama kuin mja "yksikko". Vaihtoehtoiset arvot ovat: NULL, annos, desilitra, ei määräyksikköä, gigatavu, 
gramma, gramma tai kappale, kerta, kilowattitunti, kuukausi, kuutio, kuutiometri, litra, megawattitunti, metri, millilitra, minuutti, neliö, neliömetri, pakkaus, pari, prosentti, tunti, vuorokausi, vuosi. Alkaen vuodesta 2013.

#### `suuralue` — Suuralue

**Classification:** nuts2

sama kuin mja "sual". 1=Uusimaa, 2=Etelä-Suomi, 3=Itä-Suomi, 4=Länsi-Suomi, 5=Pohjois-Suomi, 6=Ahvenanmaa, 7= Koko maa. Alkaen vuodesta 2013.

#### `arvo_num` — Arvo, numeerinen

Kuvaa saa kuin mja "arvo" mutta tämä on numeerisessa muodossa. Käytössä 2013 alkaen.

---

[← Back to catalogue](../../README.md)
