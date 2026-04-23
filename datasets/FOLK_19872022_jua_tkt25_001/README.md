# FOLK työssäkäynti

- **Identifier:** `FOLK_19872022_jua_tkt25_001.xml`
- **DOI:** `work_2017-12_2017-12-20_ain_0001`
- **Temporal coverage:** 1987-12-31 - 2022-12-31
- **Published:** 2025-01-24
- **Organisation:** Tilastokeskus
- **Variable count:** 48
- **Observation count:** —
- **Population:** Kunkin vuoden viimeisenä päivänä Suomessa vakituisesti asunut väestö
- **Source:** Tilastokeskuksen henkilötietovarasto, yritysrekisterin toimipaikat

## Description

FOLK-henkilöaineiston työssäkäyntimoduuli sisältää pääasiassa työssäkäyntitilaston tietoja. Työnantajaa koskevia tietoja on moduulissa sekä vuoden viimeisen viikon työsuhteesta (TVM) että vuoden pisimmästä, vähintään puoli vuotta kestäneestä  työsuhteesta (ATV). Moduulin tietoja on saatavilla vuodesta 1987 lähtien, jollei muuttujankuvauksessa toisin mainita.

Työssäkäyntimoduulin kokonaisaineistoon voidaan antaa käyttöoikeus vain jos tutkimuksellisesta syystä kokonaisaineiston käyttöön on erityinen tarve. Aineisto on tarkoitettu vain FIONA-etäpalvelun kautta käytettäväksi. Aineisto voidaan linkittää muihin valmisaineistoihin suojatun henkilönumeron sekä henkilön työnantajan liittyvien suojattujen tunnusten avulla. 

Huomioitavaa: 
Tilastovuodelle 2019 työssäkäyntitilastossa otettiin käyttöön tulorekisteri uutena lähdeaineistona. Tulorekisteri korvasi useita tilastossa aiemmin käytössä olleita työsuhdeaineistoja, mikä vaikuttaa tietojen vertailukelpoisuuteen. Tulorekisteristä poimitut jaksotiedot ovat maksujaksoja, minkä seurauksena ATV-pääteltyjä tietoja ei ole moduulissa tilastovuodesta 2019 alkaen. Muutos vaikuttaa myös tilastovuoden 2019 päivämäärämuuttujiin, sillä tulorekisterin tiedoissa kyseessä on maksujakson alkamis- ja loppumispäivämäärät, jotka eroavat aiemmista työsuhdeaineistojen päivämäärätiedoista.

Yrittäjien (amas2 = 2) ATV-tietoja puuttuu vuosilta 1998 ja 2005-2010. 

Vuoden 2023 päivityksessä korjattiin takautuvasti moduulin vuositaulun 2006 syrtun-muuttujan virheellset arvot. 

FOLK Työssäkäynti -aineistot sijaitsevat FIONAssa FOLK_TKT_C-kansiossa, jossa tiedostot on jaettuna tilastovuosittain. Tiedostonimet ovat muotoa "folk_tkt_vuosi_1". 

Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@tilastokeskus.fi.

## Variables (48)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `vuosi` | Vuosi | — | — | — |
| `shnro` | Suojattu TK:n henkilönumero | — | — | — |
| `ammattikoodi` | Ammattikoodi | — | — | Ammatti |
| `syrtun` | Suojattu yritystunnus (TVM) | — | — | — |
| `sykstun` | Suojattu toimipaikan tunnus (TVM) | — | — | — |
| `stpitunj1` | Suojattu jäsenyhteisö- tai virastotunnus (TVM) | — | — | — |
| `stpitunt1` | Suojattu kunta- ja valtiosektorin toimipistetunnus (TVM) | — | — | — |
| `alkupvm1` | Työsuhteen alkamispäivä (TVM) | — | — | — |
| `loppupvm1` | Loppupäivämäärä (TVM) | — | — | — |
| `oty1` | Omistajatyyppi (TVM) | — | — | työsuhde |
| `oik1` | Oikeudellinen muoto (TVM) | — | — | työsuhde |
| `toimiala` | Toimiala (TVM) | — | — | työsuhde, tyossakaynti |
| `tsekt1` | Sektori (TVM) | — | — | työsuhde |
| `tkun` | Työpaikan kunta (TVM) | — | — | — |
| `tp1_hl` | Toimipaikan henkilöstön suuruusluokka (TVM) | — | — | — |
| `tp1_lvl` | Toimipaikan liikevaihdon suuruusluokka (TVM) | — | — | — |
| `yr1_hl` | Yrityksen henkilöstön suuruusluokka (TVM) | — | — | — |
| `yr1_lvl` | Yrityksen liikevaihdon suuruusluokka (TVM) | — | — | — |
| `syrtun2` | Suojattu yritystunnus (ATV) | — | — | — |
| `sykstun2` | Suojattu toimipaikkatunnus (ATV) | — | — | — |
| `stpitunj2` | Suojattu jäsenyhteisötunnus tai virastotunnus (ATV) | — | — | — |
| `stpitunt2` | Suojattu kunta- ja valtiosektorin toimipistetunnus (ATV) | — | — | — |
| `ptoim2` | Pääasiallinen toiminta (ATV) | — | — | tyossakaynti |
| `amas2` | Ammattiasema (ATV) | — | — | tyossakaynti |
| `alkupvm2` | Työsuhteen alkamispäivä (ATV) | — | — | Työsuhde |
| `loppupvm2` | Loppupäivämäärä (ATV) | — | — | Työsuhde |
| `oty2` | Omistajatyyppi (ATV) | — | — | Työsuhde |
| `oik2` | Oikeudellinen muoto (ATV) | — | — | Työsuhde |
| `toimiala2` | Toimiala (ATV) | — | — | Työsuhde |
| `tsekt2` | Sektori (ATV) | — | — | Työsuhde |
| `tkun2` | Työpaikan kunta (ATV) | — | — | — |
| `tp2_hl` | Toimipaikan henkilöstön suuruusluokka (ATV) | — | — | — |
| `tp2_lvl` | Toimipaikan liikevaihdon suuruusluokka (ATV) | — | — | — |
| `yr2_hl` | Yrityksen henkilöstön suuruusluokka (ATV) | — | — | — |
| `yr2_lvl` | Yrityksen liikevaihdon suuruusluokka (ATV) | — | — | — |
| `tyopv` | Työpäiviä | — | — | tyossakaynti |
| `tyottpv` | Työttömyyspäiviä | — | — | Työnhakijarekisteri |
| `sijpv` | Sijoituspäiviä | — | — | Työnhakijarekisteri |
| `sijti` | Sijoittumistieto | — | — | Työnhakijarekisteri |
| `tpide` | Sijoitetun toimenpidekoodi | — | — | Työnhakijarekisteri |
| `viim_tyott_kesto` | Viimeisen työttömyysjakson kesto päivinä | — | — | Työnhakijarekisteri |
| `tpasy` | Työttömyyden päättymissyy | — | — | Työnhakijarekisteri |
| `thpsyy` | Työnhaun päättymissyy | — | — | Työnhakijarekisteri |
| `aika` | Eläkkeen alkamisaika | — | — | Eläke |
| `tyol` | Työvoimakoulutuksessa vuoden viimeisellä viikolla | — | — | — |
| `tyol2` | Työvoimakoulutuksessa yli 5 kk | — | — | — |
| `tyomatka` | Työmatka | — | — | — |
| `auto` | Henkilö ajoneuvon omistaja/haltija | — | — | — |

### Variable definitions

#### `vuosi` — Vuosi

Tilastovuosi.

#### `shnro` — Suojattu TK:n henkilönumero

Suojattu TK:n henkilönumero, joka on sama kaikissa henkilövalmisaineistoissa.

#### `ammattikoodi` — Ammattikoodi

**Group:** Ammatti

Tietoja vuosilta 1990, 1993, 1995, 2000 ja vuodesta 2004 lähtien vuosittain. Tieto henkilön ammatista on tuotettu 18-74-vuotiaille työllisille, siis palkansaajille ja yrittäjille. Ammattitiedot perustuvat pääasiassa eri hallinnollisista aineistoista (työsuhdeaineistot) ja Tilastokeskuksen palkkatilastoista saatuihin ammatti-, virka- ja tehtävänimikkeisiin ja -koodeihin. Lisäksi tehdään erillinen ammattitiedonkeruu vuosittain. Henkilön ammattikoodi tuotetaan ensisijaisesti vuoden viimeisen viikon päätyösuhteen mukaisen ammatin perusteella. Ammattinimikkeiden lisäksi tiedon tuottamisessa käytetään hyväksi tietoa henkilön työpaikan toimialasta ja sektorista sekä henkilön koulutuksesta. Ammattitietojen tuottamista ohjaa kansainvälisen työjärjestön ILO:n laatima hierarkkinen luokitusjärjestelmä International Standard Classification of Occupations, lyh. ISCO. 

Luokitusstandardit:
Vuodesta 2010 lähtien Ammattiluokitus 2010 (AML 2010). 
Vuosina 1995, 2000, 2004 - 2009 Ammattiluokitus 2001. 
Vuosina 1990 ja 1993 Ammattiluokitus 1980.  

Eri luokitusstandardeilla tuotetut tiedot eivät ole keskenään vertailukelpoiset. Tilastossa käytetyt luokitukset samoin kun luokitusten väliset avaimet löytyvät Tilastokeskuksen luokitus- ja metatietopalvelujen kotisivuilta osoitteesta: http://tilastokeskus.fi/luokitukset sekä painetuista luokituskäsikirjoista.

#### `syrtun` — Suojattu yritystunnus (TVM)

Suojattu yritystunnus (TVM) yksilöi työsuhteen työnantajan. Yksityisillä yrityksillä, liikkeen- ja ammatinharjoittajilla sekä kunnilla ja kuntayhteisöillä suojaamaton yritystunnus on y-tunnus, joka annetaan yritys- ja yhteisötietojärjestelmässä (YTJ ks. ytj.fi).  Valtion yksiköillä se on valtion virastotunnus, VIRTUN, joka annetaan Valtiokonttorissa. Kuntien liikelaitoksilla suojaamaton yritystunnus on Yritys- ja toimipaikkarekisterissä muodostettu surrogaattitunnus.

HUOM! Vuodesta 2004 vuoteen 2005 tapahtui hallinnollisia muutoksia työnantajatunnuksissa. Virastotunnusten muuttuessa y-tunnus -muotoon henkilölle, jolla on aiemmin ollut yritystunnus-muuttujassa virastotunnus, on voinut tulla muutoksen jälkeen tämän tilalle y-tunnus. Samalla yritystunnus-muuttujassa aiemmin ollut virastotunnus on siirtynyt jäsenyhteisö-tai virastotunnus -muuttujaan. Näillä henkilöillä suojattu yritystunnus (syrtun) on siis siirtynyt stpitunt-tietoon.

#### `sykstun` — Suojattu toimipaikan tunnus (TVM)

Suojattu toimipaikan tunnus (TVM) on Yritys- ja toimipaikkarekisterin käyttämä toimipaikkatunnus, joka sisältää sekä yksityisen että julkisen sektorin toimipaikkatunnuksia.

Myös yksityisellä sektorilla voi olla esim. yritysjärjestelyistä johtuen poikkeuksia, joissa toimipaikkatunnus liittyy useampaan kuin yhteen yritystunnukseen samana vuonna. Toimipaikkatunnus on TK:n ylläpitämä pysyvä yksilöivä tunniste, mutta siinä voi tapahtua muutoksia ja siksi se on hyvä yhdistää y-tunnukseen.

#### `stpitunj1` — Suojattu jäsenyhteisö- tai virastotunnus (TVM)

Suojattu kuntien/kuntayhtymien jäsenyhteisötunnus tai valtion virastotunnus (TVM).

HUOM! Vuodesta 2004 vuoteen 2005 tapahtui hallinnollisia muutoksia työnantajatunnuksissa. Virastotunnusten muuttuessa y-tunnus -muotoon henkilölle, jolla on aiemmin ollut yritystunnus-muuttujassa virastotunnus, on voinut tulla muutoksen jälkeen tämän tilalle y-tunnus. Samalla yritystunnus-muuttujassa aiemmin ollut virastotunnus on siirtynyt jäsenyhteisö-tai virastotunnus -muuttujaan. Näillä henkilöillä suojattu yritystunnus (syrtun) on siis  siirtynyt  stpitunj-tietoon.

#### `stpitunt1` — Suojattu kunta- ja valtiosektorin toimipistetunnus (TVM)

Toimipistetunnus kunta- ja valtiosektorin työsuhteilla (TVM). 

HUOM! Toimipistetunnus ei ole yksikäsitteinen, vaan sitä on aina käytettävä yhdessä yritystunnuksen (syrtun1)  tai 
suojatun jäsenyhteisö- tai virastotunnuksen (stptitunj1) kanssa. Julkisen sektorin toimipistetunnus stpitunt1 voi myös vaihdella vuodesta toiseen samalla toimipaikalla.

#### `alkupvm1` — Työsuhteen alkamispäivä (TVM)

Vuoden viimeisen viikon työsuhteen alkamispäivä. 

Huom. Tilastovuonna 2019 tulorekisterin päivämäärätiedoissa kyseessä on maksujakson alkamispäivä. Tilastossa on ketjutettu maksujaksoja yhteen, jos niissä ei ole yli kuukauden katkoa.

#### `loppupvm1` — Loppupäivämäärä (TVM)

Työ- tai yrittäjäsuhteen loppumispäivämäärä (TVM). 

Huom. Tilastovuonna 2019 tulorekisterin päivämäärätiedoissa kyseessä on viimeisen maksujakson päivämäärä. Tilastossa on ketjutettu maksujaksoja yhteen, jos niissä ei ole yli kuukauden katkoa.

#### `oty1` — Omistajatyyppi (TVM)

**Group:** työsuhde

Henkilön vuoden lopun työsuhteen työnantajayrityksen omistajatyyppi 

Vuodesta 1996 alkaen arvoalue: 
1 = Yksityinen kotimainen 
2 = Valtio 
3 = Kunta
4 = Ahvenanmaan maakunta 
5 = Ulkomaalaisomisteinen 
6 = Muu omistajatyyppi, tuntematon
BL = Henkilö ei työllinen 

1987-1995 arvoalue: 
1 = Yksityinen kotimainen 
2 = Valtio 
3 = Kunta 
4 = Kuntainliitto 
6 = Ulkomaalaisten osuus yli 20 %, enintään 50 %
7 = Ulkomaalaisten osuus yli 50 % 
9 = Muu omistajatyyppi, tuntematon

#### `oik1` — Oikeudellinen muoto (TVM)

**Group:** työsuhde

Henkilön vuoden lopun työsuhteen työnantajayrityksen oikeudellinen muoto. 
11 = Luonnollinen henkilö 
12 = Kuolinpesä, perikunta 
13 = Verotusyhtymä 
14 = Avoin yhtiö 
15 = Konkurssipesä 
21 = Kommandiittiyhtiö 
22 = Laivanisännistö (ei osakeyhtiö) 
31 = Osakeyhtiö 
32 = Keskinäinen vakuutusyhtiö 
33 = Säästöpankki 
34 = Eläkesäätiö tai -kassa, työeläkelaitos, työttömyys- tai avustuskassa 
35 = Asunto-osakeyhtiö 
41 = Osuuskunta 
51 = Säätiö, rahasto 
52 = Aatteellinen yhdistys 
53 = Keskinäinen vahinkovakuutusyhtiö 
54 = Taloudellinen yhdistys 
61 = Julkinen viranomainen 
62 = Julkinen liikelaitos 
63 = Julkisoikeudellinen yhteisö
71 = Valtionkirkko 
72 = Muu uskonnollinen yhteisö 
90 = Muu oikeudellinen muoto, tuntematon 
BL = Henkilö ei työllinen

#### `toimiala` — Toimiala (TVM)

**Group:** työsuhde, tyossakaynti

Henkilön TVM-käsitteen mukaisen työsuhteen toimiala eli vuoden lopussa työllisenä olevien päätyösuhteen toimiala. 
Käytössä seuraavat luokitukset: 
 toimiala_1_08_s (TOL2008) vuodesta 2007 lähtien 
 toimiala_1_02_s (TOL2002) vuodet 2001-2006 
 toimiala_1_00_s (TOL95, toinen tarkistettu painos) vuodet 1998-2000
 toimiala_1_95_s (TOL95) vuodet 1993-1997
 toimiala_1_88_s (TOL88) vuodet 1987-1992 

Luokitusavaimet: http://www.stat.fi/meta/luokitukset/toimiala/001-2008/luokitusavaimet.html ja http://www.stat.fi/meta/luokitukset/toimiala/versio.html

#### `tsekt1` — Sektori (TVM)

**Group:** työsuhde

Vuoden viimeisen viikon työsuhteen työnantajayrityksen sektori (TVM). Tietoja vuodesta 1989 lähtien.

Luokitus vuodesta 2013 lähtien: Sektoriluokitus 2012 http://www.stat.fi/meta/luokitukset/sektoriluokitus/versio.html.

Vuosien 1999-2012 luokituksen  ja vuodesta 2013 alkavan luokituksen ensimmäinen numero: 
1 Koko kansantalous (kotimaiset sektorit)
2 Ulkomaat

Näillä luokituksilla pääsekstorit ovat kahden numeron tasolla:
11	Yritykset
12	Rahoitus- ja vakuutuslaitokset
13	Julkisyhteisöt
14	Kotitaloudet
15	Kotitalouksia palvelevat voittoa tavoittelemattomat yhteisöt
21	Euroopan unionin jäsenvaltiot ja toimielimet
22	Euroopan unionin ulkopuoliset valtiot ja kansainväliset järjestöt

Vuosina 1989-1994 ja vuosina 1995-1998 luokituksissa jo kahden numeron tasolla merkittäviä eroja, mutta luokitukset ovat samat ensimmäisen numeron tasolla:
1	Yritykset
2	Rahoitus- ja vakuutuslaitokset
3	Julkisyhteisöt
4	Voittoa tavoittelemattomat yhteisöt
5	Kotitaloudet
6	Ulkomaat

Muut luokitukset pyydettävä Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@tilastokeskus.fi.

#### `tkun` — Työpaikan kunta (TVM)

Henkilön vuoden viimeisen viikon työpaikan (toimipaikan) kuntakoodi.  Aluejako ollut ennen vuotta 1999 tilastovuoden aluejako ja taas vuodesta 2005 alkaen tilastovuoden aluejako. Vuosina 1999-2004 aluejako on ollut tilastovuosi + 1 vuosi eli esim. 2003 tiedot ilmoitettiin aluejaon 1.1.2004 mukaan. Tieto on vain työllisillä. Tieto vuodesta 1988 lähtien.

#### `tp1_hl` — Toimipaikan henkilöstön suuruusluokka (TVM)

Vuoden viimeisen viikon työsuhteen toimipaikan henkilöstön suuruusluokka. Tietoja vuodesta 1988 lähtien.
Suuruusluokat ovat: 
1 HK < 4,5 
2 4,5 <= HK < 9,5 
3 9,5 <= HK < 19,5 
4 19,5 <= HK < 49,5 
5 49,5 <= HK < 99,5 
6 99,5 <= HK < 199,5 
7 199,5 <= HK < 499,5 
8 499,5 <= HK < 999,5 
9 999,5 <= HK

#### `tp1_lvl` — Toimipaikan liikevaihdon suuruusluokka (TVM)

Vuoden viimeisen viikon työsuhteen toimipaikan liikevaihdon suuruusluokka toimipaikkarekisteristä. Tietoja vuodesta 1988 lähtien.
 
Suuruusluokat ovat : 
1 LV < 1 000 
2 1 000 <= LV < 40 000 
3 40 000 <= LV < 100 000 
4 100 000 <= LV < 400 000 
5 400 000 <= LV < 2 000 000 
6 2 000 000 <= LV < 10 000 000 
7 10 000 000 <= LV < 40 000 000 
8 40 000 000 <= LV < 200 000 000 
9 200 000 000 <= LV

#### `yr1_hl` — Yrityksen henkilöstön suuruusluokka (TVM)

Vuoden viimeisen viikon työsuhteen yrityksen henkilöstön suuruusluokka. Tietoja vuodesta 1988 lähtien.
Suuruusluokat ovat: 
1 HK < 4,5 
2 4,5 <= HK < 9,5 
3 9,5 <= HK < 19,5 
4 19,5 <= HK < 49,5 
5 49,5 <= HK < 99,5 
6 99,5 <= HK < 199,5 
7 199,5 <= HK < 499,5 
8 499,5 <= HK < 999,5 
9 999,5 <= HK

#### `yr1_lvl` — Yrityksen liikevaihdon suuruusluokka (TVM)

Vuoden viimeisen viikon työsuhteen yrityksen liikevaihdon suuruusluokka toimipaikkarekisteristä (euroa). Tietoja vuodesta 1988 lähtien. 
Suuruusluokat ovat : 
1 LV < 1 000 
2 1 000 <= LV < 40 000 
3 40 000 <= LV < 100 000 
4 100 000 <= LV < 400 000 
5 400 000 <= LV < 2 000 000 
6 2 000 000 <= LV < 10 000 000 
7 10 000 000 <= LV < 40 000 000 
8 40 000 000 <= LV < 200 000 000 
9 200 000 000 <= LV

#### `syrtun2` — Suojattu yritystunnus (ATV)

Suojattu yritystunnus (ATV) yksilöi työsuhteen työnantajan. Tietoja vuodesta 1989 lähtien vuoteen 2018 asti. 

Yksityisillä yrityksillä, liikkeen- ja ammatinharjoittajilla sekä kunnilla ja kuntayhteisöillä suojaamaton yritystunnus on y-tunnus, joka annetaan yritys- ja yhteisötietojärjestelmässä (YTJ ks. ytj.fi).  Valtion yksiköillä se on valtion virastotunnus, VIRTUN, joka annetaan Valtiokonttorissa. 
Kuntien liikelaitoksilla suojaamaton yritystunnus on Yritys- ja toimipaikkarekisterissä muodostettu surrogaattitunnus. 

HUOM! Vuodesta 2004 vuoteen 2005 tapahtui hallinnollisia muutoksia työnantajatunnuksissa. Virastotunnusten muuttuessa y-tunnus -muotoon henkilölle, jolla on aiemmin ollut yritystunnus-muuttujassa virastotunnus, on voinut tulla muutoksen jälkeen tämän tilalle y-tunnus. Samalla yritystunnus-muuttujassa aiemmin ollut virastotunnus on siirtynyt jäsenyhteisö-tai virastotunnus -muuttujaan. Näillä henkilöillä suojattu yritystunnus (syrtun2) on siis  siirtynyt  stpitunj2-tietoon.

#### `sykstun2` — Suojattu toimipaikkatunnus (ATV)

Suojattu toimipaikan tunnus (ATV) on Yritys- ja toimipaikkarekisterin käyttämä toimipaikkatunnus, joka sisältää sekä yksityisen että julkisen sektorin toimipaikkatunnuksia. Toimipaikkatunnus on TK:n ylläpitämä pysyvä yksilöivä tunniste, mutta siinä voi tapahtua muutoksia ja siksi se on hyvä yhdistää yritystunnukseen. Myös yksityisellä sektorilla voi olla esim. yritysjärjestelyistä johtuen poikkeuksia, joissa toimipaikkatunnus liittyy useampaan kuin yhteen yritystunnukseen samana vuonna. 
Tietoja vuoteen 2018 asti.

#### `stpitunj2` — Suojattu jäsenyhteisötunnus tai virastotunnus (ATV)

Suojattu kuntien/kuntayhtymien jäsenyhteisötunnus tai valtion virastotunnus (ATV). 

HUOM! Vuodesta 2004 vuoteen 2005 tapahtui hallinnollisia muutoksia työnantajatunnuksissa. Virastotunnusten muuttuessa y-tunnus -muotoon henkilölle, jolla on aiemmin ollut yritystunnus-muuttujassa virastotunnus, on voinut tulla muutoksen jälkeen tämän tilalle y-tunnus. Samalla yritystunnus-muuttujassa aiemmin ollut virastotunnus on siirtynyt jäsenyhteisö-tai virastotunnus -muuttujaan. Näillä henkilöillä suojattu yritystunnus (syrtun2) on siis siirtynyt stpitunj2-tietoon. Tietoja vuoteen 2018 asti.

#### `stpitunt2` — Suojattu kunta- ja valtiosektorin toimipistetunnus (ATV)

Toimipistetunnus kunta- ja valtiosektorin työsuhteilla (ATV). 

HUOM! Toimipistetunnus ei ole yksikäsitteinen, vaan sitä on aina käytettävä yhdessä yritystunnuksen (syrtun2)  tai 
suojatun jäsenyhteisö- tai virastotunnuksen (stptitunj2) kanssa. Julkisen sektorin toimipistetunnus stpitunt2 voi myös vaihdella vuodesta toiseen samalla toimipaikalla. Tietoja vuoteen 2018 asti.

#### `ptoim2` — Pääasiallinen toiminta (ATV)

**Group:** tyossakaynti

Pääasiallinen toiminta pisimmän työsuhteen päättelyllä. 
11 = työllinen 
12 = työtön 
21 = 0-14 vuotias 
22 = opiskelija 
24 = eläkeläinen 
25 = varus- tai siviilipalvelusmies 
29 = työttömyyseläkeläinen 
99 = muu työvoiman ulkopuolella oleva
Tietoja vuoteen 2018 asti.

#### `amas2` — Ammattiasema (ATV)

**Group:** tyossakaynti

Ammattiasema vuoden pisimmän työsuhteen mukaan. 
1=palkansaaja 
2=yrittäjä 

Päättely muuttunut v. 2005. Aiemmin vaadittu, että yrittäjä on myös työnantaja. Tietoja vuoteen 2018 asti.

#### `alkupvm2` — Työsuhteen alkamispäivä (ATV)

**Group:** Työsuhde

Vuoden pisimmän työsuhteen alkamispäivä. Tietoja vuoteen 2018 asti.

#### `loppupvm2` — Loppupäivämäärä (ATV)

**Group:** Työsuhde

Vuoden pisimmän työsuhteen päättymispäivä. Tietoja vuoteen 2018 asti.

#### `oty2` — Omistajatyyppi (ATV)

**Group:** Työsuhde

Henkilön vuoden pisimmän työsuhteen yrityksen omistajatyyppi. Tietoja vuoteen 2018 asti.

Vuodesta 1996 alkaen arvoalue: 
1 = Yksityinen kotimainen 
2 = Valtio 
3 = Kunta
4 = Ahvenanmaan maakunta 
5 = Ulkomaalaisomisteinen 
6 = Muu omistajatyyppi, tuntematon
BL = Henkilö ei työllinen 

1987-1995 arvoalue: 
1 = Yksityinen kotimainen 
2 = Valtio 
3 = Kunta 
4 = Kuntainliitto 
6 = Ulkomaalaisten osuus yli 20 %, enintään 50 %
7 = Ulkomaalaisten osuus yli 50 % 
9 = Muu omistajatyyppi, tuntematon

#### `oik2` — Oikeudellinen muoto (ATV)

**Group:** Työsuhde

Henkilön pisimmän työsuhteen työnantajayrityksen oikeudellinen muoto
11 = Luonnollinen henkilö 
12 = Kuolinpesä, perikunta 
13 = Verotusyhtymä 
14 = Avoin yhtiö 
15 = Konkurssipesä 
21 = Kommandiittiyhtiö 
22 = Laivanisännistö (ei osakeyhtiö) 
31 = Osakeyhtiö 
32 = Keskinäinen vakuutusyhtiö 
33 = Säästöpankki 
34 = Eläkesäätiö tai -kassa, työeläkelaitos, työttömyys- tai avustuskassa 
35 = Asunto-osakeyhtiö 
41 = Osuuskunta 
51 = Säätiö, rahasto 
52 = Aatteellinen yhdistys 
53 = Keskinäinen vahinkovakuutusyhtiö 
54 = Taloudellinen yhdistys 
61 = Julkinen viranomainen 
62 = Julkinen liikelaitos 
63 = Julkisoikeudellinen yhteisö
71 = Valtionkirkko 
72 = Muu uskonnollinen yhteisö 
90 = Muu oikeudellinen muoto, tuntematon 
BL = Henkilö ei työllinen
Tietoja vuoteen 2018 asti.

#### `toimiala2` — Toimiala (ATV)

**Group:** Työsuhde

Vuoden pisimmän työsuhteen toimiala. Tietoja vuoteen 2018 asti.
Käytössä seuraavat luokitukset: 
toimiala_1_08_s (TOL2008) vuodesta 2007 lähtien 
toimiala_1_02_s (TOL2002) vuodet 2001-2006 
toimiala_1_00_s (TOL95, toinen tarkistettu painos) vuodet 1998-2000
toimiala_1_95_s (TOL95) vuodet 1993-1997
toimiala_1_88_s (TOL88) vuodet 1987-1992 

Luokitusavaimet: http://www.stat.fi/meta/luokitukset/toimiala/001-2008/luokitusavaimet.html ja http://www.stat.fi/meta/luokitukset/toimiala/versio.html

#### `tsekt2` — Sektori (ATV)

**Group:** Työsuhde

Vuoden pisimmän työsuhteen työnantajayrityksen sektori (ATV). Tietoja vuodesta 1989 vuoteen 2018.

Luokitus vuodesta 2013 lähtien: Sektoriluokitus 2012 http://www.stat.fi/meta/luokitukset/sektoriluokitus/versio.html.

Vuosien 1999-2012 luokituksen  ja vuodesta 2013 alkavan luokituksen ensimmäinen numero: 
1 Koko kansantalous (kotimaiset sektorit)
2 Ulkomaat

Näillä luokituksilla pääsekstorit ovat kahden numeron tasolla:
11	Yritykset
12	Rahoitus- ja vakuutuslaitokset
13	Julkisyhteisöt
14	Kotitaloudet
15	Kotitalouksia palvelevat voittoa tavoittelemattomat yhteisöt
21	Euroopan unionin jäsenvaltiot ja toimielimet
22	Euroopan unionin ulkopuoliset valtiot ja kansainväliset järjestöt

Vuosina 1989-1994 ja vuosina 1995-1998 luokituksissa jo kahden numeron tasolla merkittäviä eroja, mutta luokitukset ovat samat ensimmäisen numeron tasolla:
1	Yritykset
2	Rahoitus- ja vakuutuslaitokset
3	Julkisyhteisöt
4	Voittoa tavoittelemattomat yhteisöt
5	Kotitaloudet
6	Ulkomaat

Muut luokitukset pyydettävä Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@tilastokeskus.fi.

#### `tkun2` — Työpaikan kunta (ATV)

Henkilön atv-käsitteen mukaisen työpaikan (toimipaikan) kuntakoodi. Aluejako ollut ennen vuotta 1999 tilastovuoden aluejako ja taas vuodesta 2005 alkaen tilastovuoden aluejako. Vuosina 1999-2004 aluejako on ollut tilastovuosi + 1 vuosi eli esim. 2003 tiedot ilmoitettiin aluejaon 1.1.2004 mukaan. Tieto on vain työllisillä. Tieto vuosilta 1989-2004.

#### `tp2_hl` — Toimipaikan henkilöstön suuruusluokka (ATV)

Vuoden pisimmän työsuhteen toimipaikan henkilöstön suuruusluokka. Tietoja vuodesta 1988 vuoteen 2018.
Suuruusluokat ovat: 
1 HK < 4,5 
2 4,5 <= HK < 9,5 
3 9,5 <= HK < 19,5 
4 19,5 <= HK < 49,5 
5 49,5 <= HK < 99,5 
6 99,5 <= HK < 199,5 
7 199,5 <= HK < 499,5 
8 499,5 <= HK < 999,5 
9 999,5 <= HK

#### `tp2_lvl` — Toimipaikan liikevaihdon suuruusluokka (ATV)

Vuoden pisimmän työsuhteen toimipaikan liikevaihdon suuruusluokka toimipaikkarekisteristä (euroa). Tietoja vuodesta 1988 vuoteen 2018.
Suuruusluokat ovat : 
1 LV < 1 000 
2 1 000 <= LV < 40 000 
3 40 000 <= LV < 100 000 
4 100 000 <= LV < 400 000 
5 400 000 <= LV < 2 000 000 
6 2 000 000 <= LV < 10 000 000 
7 10 000 000 <= LV < 40 000 000 
8 40 000 000 <= LV < 200 000 000 
9 200 000 000 <= LV

#### `yr2_hl` — Yrityksen henkilöstön suuruusluokka (ATV)

Vuoden pisimmän työsuhteen yrityksen henkilöstön suuruusluokka. Tietoja vuodesta 1988 vuoteen 2018.
Suuruusluokat ovat: 
1 HK < 4,5 
2 4,5 <= HK < 9,5 
3 9,5 <= HK < 19,5 
4 19,5 <= HK < 49,5 
5 49,5 <= HK < 99,5 
6 99,5 <= HK < 199,5 
7 199,5 <= HK < 499,5 
8 499,5 <= HK < 999,5 
9 999,5 <= HK

#### `yr2_lvl` — Yrityksen liikevaihdon suuruusluokka (ATV)

Vuoden pisimmän työsuhteen yrityksen liikevaihdon suuruusluokka toimipaikkarekisteristä (euroa). Tietoja vuodesta 1988 vuoteen 2018. 
Suuruusluokat ovat : 
1 LV < 1 000 
2 1 000 <= LV < 40 000 
3 40 000 <= LV < 100 000 
4 100 000 <= LV < 400 000 
5 400 000 <= LV < 2 000 000 
6 2 000 000 <= LV < 10 000 000 
7 10 000 000 <= LV < 40 000 000 
8 40 000 000 <= LV < 200 000 000 
9 200 000 000 <= LV

#### `tyopv` — Työpäiviä

**Group:** tyossakaynti

Henkilön työpäivien yhteenlaskettu lukumäärä tilastovuonna. Tietoja vuodesta 2005 lähtien. Työpäivät lasketaan työsuhteen alku- ja loppupäivämäärä -tiedoista.

HUOM! Tilastovuonna 2019 työssäkäyntitilastossa siirryttiin käyttämään palkansaajien lähdeaineistona tulorekisteriä, jossa työsuhteden kesto lasketaan maksujakson mukaan. Muuttuja ei ole enää suoraan vertailukelpoinen aiempiin vuosiin lähdeaineiston muutoksen vuoksi.

#### `tyottpv` — Työttömyyspäiviä

**Group:** Työnhakijarekisteri

Henkilön työttömyyspäivien yhteenlaskettu lukumäärä tilastovuonna. Tietoja vuodesta 2005 lähtien.

#### `sijpv` — Sijoituspäiviä

**Group:** Työnhakijarekisteri

Henkilön työvoimapoliittisten sijoituspäivien yhteenlaskettu lukumäärä tilastovuonna. Eri sijoitusjaksot laskettu yhteen, mahdolliset päällekkäiset jaksot poistettu. Tietoja vuodesta 2004 lähtien.

#### `sijti` — Sijoittumistieto

**Group:** Työnhakijarekisteri

sijti=1 : Henkilö ollut työvoimapoliittisin toimenpitein sijoitettuna vuoden viimeisellä viikolla (25.12-31.12.tilastovuosi, vuodesta 2005 lähtien) tai vuoden viimeisenä päivänä (vuosina 1993-2004). Tietoja vuodesta 1993 lähtien.

#### `tpide` — Sijoitetun toimenpidekoodi

**Group:** Työnhakijarekisteri

Työvoimapoliittisen toimenpiteen sijottumiskoodi. Tieto työministeriön työnhakijarekisteristä vuoden viimeisellä viikolla sijoitettuna olevilla. Tietoja vuosilta 1998-2004. 
40 = valtion työtehtävät 
41 = työllistämispalvelu 
42 = työviraston työohjeen mukainen sijoitus 
50 = kunnallinen työllistämistuki 
51 = oppisopimussijoitus, kunta 
53 = yhdistelmätuki, kunta 
60 = työllistämistuki, yksityinen työnantaja 
62 = yrittäjäraha 
64 = harjaantuminen 
68 = oppisopimussijoiutus, yksityinen 
69 = yhdistelmätuki, yksityinen työnantaja 
70 = työharjoittelu työmarkkinatuella 
73 = työllistäminen osa-aikatyöhön (paikkaan välitetty, tilastoidaan) 
74 = 500 pv yksityinen työmarkkinatuki 
75 = 500 pv kunta työmarkkinatuki 
Muut koodit virheellisiä, epävalideja

#### `viim_tyott_kesto` — Viimeisen työttömyysjakson kesto päivinä

**Group:** Työnhakijarekisteri

Viimeisimmän tilastovuoden lopussa voimassaolevan tai tilastovuoden aikana loppuneen työttömyysjakson kesto päivinä. Lasketaan henkilön viimeisimmän työttömyysjakson alkupäivästä loppupäivään tai jos työttömyys voimassa vuoden loppuun (31.12.) Tietoja vuodesta 2001 lähtien.

#### `tpasy` — Työttömyyden päättymissyy

**Group:** Työnhakijarekisteri

Työttömyyden päättymisen syy. Tietoja vuodesta 1995 lähtien.
Luokitus vuodesta 2012 alkaen: 
00 = Työllistetty (entinen nimi: sijoitettu toimenpitein) 
01 = Välitetty työhön yleisille työmarkkinoille 
02 = Lomautus/lyhennetty työviikko päättynyt 
03 = Saanut itse työtä 
04 = Aloittanut työvoimakoulutuksen 
05 = Siirtynyt työvoiman ulkopuolelle (nykyisin merkitään soveltuvin osin syillä 11, 12 ja 13) 
06 = Muu syy tai ei tietoa 
07 = Siirtynyt työttömyyseläkkeelle 
08 = Aloittanut muun koulutuksen 
09 = Työhön/työnhakuun EU/ETA-valtioon 
10 = Ei ole uusinut työnhakuaan 
11 = Aloittanut valmennuksen/kokeilun 
12 = Aloittanut kuntouttavan työtoiminnan 
13 = Aloittanut omaehtoisen opiskelun 

Luokitus vuoteen 2011 asti: 
0 = sijoitettu työllistämistoimenpitein 
1 = välitetty työhön yleisille työmarkkinoille 
2 = lomautus tai lyhennetty työviikko on päättynyt 
3 = saanut itse työpaikan 
4 = aloittanut työllisyyskoulutuksen 
5 = siirtynyt työvoiman ulkopuolelle 
6 = muu syy tai ei tietoa 
7 = siirtynyt työttömyyseläkkeelle 
8 = muu koulutus 
9 = työnhakuun ETA-valtioon 
z = tuntematon

#### `thpsyy` — Työnhaun päättymissyy

**Group:** Työnhakijarekisteri

Henkilön viimeisimmän työnhakujakson päättymisen syy. Osalla henkilöitä, joilla työnhaun päättymispäivä on tyhjä eli työnhaku jatkuu vuodenvaihteen yli, on merkitty päättymisen syy. 

Luokitus vuodesta 2012 alkaen: 
00 = Työllistetty (entinen nimi: sijoitettu toimenpitein) 
01 = Välitetty työhön yleisille työmarkkinoille 
02 = Lomautus/lyhennetty työviikko päättynyt 
03 = Saanut itse työtä 
04 = Aloittanut työvoimakoulutuksen 
05 = Siirtynyt työvoiman ulkopuolelle (nykyisin merkitään soveltuvin osin syillä 11, 12 ja 13) 
06 = Muu syy tai ei tietoa 
07 = Siirtynyt työttömyyseläkkeelle 
08 = Aloittanut muun koulutuksen 
09 = Työhön/työnhakuun EU/ETA-valtioon 
10 = Ei ole uusinut työnhakuaan 
11 = Aloittanut valmennuksen/kokeilun 
12 = Aloittanut kuntouttavan työtoiminnan 
13 = Aloittanut omaehtoisen opiskelun 

Luokitus vuoteen 2011 saakka: 
0 = sijoitettu työllistämistoimenpitein 
1 = välitetty työhön yleisille työmarkkinoille
2 = lomautus tai lyhennetty työviikko päättynyt 
3 = saanut itse työpaikan 
4 = aloittanut työllisyyskoulutuksen 
5 = siirtynyt työvoiman ulkopuolelle 
6 = muu syy tai ei tietoa 
7 = siirtynyt työttömyyseläkkeelle 
8 = muu koulutus 
9 = työnhakuun ETA-valtioon

#### `aika` — Eläkkeen alkamisaika

**Group:** Eläke

Voimassaolevista eläkejaksoista (ei osa-aika-, perhe- eikä takuueläke) varhaisin alkamisaika. Tietoja vuodesta 2005 lähtien.

#### `tyol` — Työvoimakoulutuksessa vuoden viimeisellä viikolla

Henkilö ollut työvoimapoliittisessa koulutuksessa vuoden viimeisellä viikolla (25.12.-31-12.) Tietoja vuodesta 1989 lähtien.

#### `tyol2` — Työvoimakoulutuksessa yli 5 kk

Työvoimakoulutuksessa yli 5 kk 

Arvoalue:
1 = Ollut työvoimakoulutuksessa yli 5 kk 
bl = Ei ole ollut työvoimakoulutuksessa tai ollut siinä alle 6 kk 

Tietoja 1988-2004.

#### `tyomatka` — Työmatka

Lineaarinen etäisyys (ns. linnuntie-etäisyys) työpaikan ja asuinpaikan koordinaattien välillä. Mittayksikkö metri. Jos matka > 300 000 m, tieto ei ole luotettava. Tietoja vuodesta 2005 lähtien.

#### `auto` — Henkilö ajoneuvon omistaja/haltija

Henkilö on auton omistaja/haltija ajoneuvorekisterin tietojen mukaan ajoneuvolajeittain vuodesta 2005-2018: 
1=henkilöauto 
2=pakettiauto 
3=kuorma-auto 
4=erikoisauto 
Jos henkilöllä useampia ajoneuvoja on prioriteettijärjestys 1-2-3-4. (Muita ajoneuvolajeja ei mukana). 

Tieto vuosina 1990-2004: 
1 = on auton omistaja/haltija ajoneuvorekisterin tietojen mukaan. 

Tietoja vuodesta 1990 lähtien.

---

[← Back to catalogue](../../README.md)
