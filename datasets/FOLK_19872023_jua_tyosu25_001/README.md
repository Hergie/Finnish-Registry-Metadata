# FOLK jaksotiedot: työsuhde

- **Identifier:** `FOLK_19872023_jua_tyosu25_001.xml`
- **DOI:** `tyokay_2012-03_2012-03-01_ain_0001`
- **Temporal coverage:** 1987-01-01 - 2023-12-31
- **Published:** 2026-01-16
- **Organisation:** Tilastokeskus
- **Variable count:** 18
- **Observation count:** —
- **Population:** Kunkin vuoden viimeisenä päivänä Suomessa vakituisesti asuneet 15 vuotta täyttäneet henkilöt.
- **Source:** Työsuhderekisterit (ETK, Keva ja Valtionkonttori), tulorekisteri sekä Tilastokeskuksen oma tiedonkeruu
- **Related:** <a href= "http://www.stat.fi/til/tyokay/">Työssäkäynti</a>

## Kuvaus / Description

Sisältyy FOLK jaksotiedot -moduuliin. Työsuhdeaineisto sisältää tietoja henkilön vuoden viimeisen viikon työsuhteesta (TVM =1), henkilön vuoden pisimmästä työsuhteesta (ATV =1) ja mahdollisesta henkilön sivutyösuhteesta (SIVU=1). Lisäksi aineistossa on muita työsuhdejaksoja. 

Tiedot pääsääntöisesti vuodesta 1987 lähtien ja poikkeamat tiedon saatavuudessa on kunkin muuttujan kuvauksessa. Aineistossa on 15 vuotta täyttäneiden työsuhdejaksoja vuoteen 2015 saakka. Vuodesta 2016 lähtien nuorimmat ovat 18-vuotiaita. 

Huomioitavaa: 

Tilastovuodelle 2019 työssäkäyntitilastossa otettiin käyttöön tulorekisteri uutena lähdeaineistona. Tulorekisteri korvasi useita tilastossa aiemmin käytössä olleita työsuhdeaineistoja, mikä vaikuttaa tietojen vertailukelpoisuuteen. Tilastossa henkilön vuoden viimeisen viikon työsuhde (TVM =1) on päätelty tilastovuodelle 2019 tulorekisterin perusteella (aineisto=1). Tulorekisteristä poimitut jaksotiedot ovat maksujaksoja. Tilastovuoden 2019 aineisto sisältää myös ETK:n tulorekisteristä (aineisto=2) poimimat jaksotiedot. 

Työsuhdetiedot vuosilta 1987-2004  ovat laadultaan ja kattavuudeltaan heikompia kuin tiedot vuodesta 2005 lähtien. Tietoja puuttuu ennen vuotta 1995 TVM-työsuhteissa noin 23 % ( mm. kaikki yrittäjien tiedot, kunta-alalta noin 20 %  ja vuodelta 1987 valtion työsuhteet). Tiedot voivat olla myös ristiriitaisia FOLK työssäkäynti-aineiston kanssa ennen vuotta 2005, koska tiedot poimitaan eri lähteistä. Esimerkiksi suuressa osassa valtio- tai kunta-alan työsuhdejaksotiedoissa vuosina 1987-2004 yritys- ja toimipaikkatunnukset (yrtun_s ja ykstun_s) eivät ole samat kuin FOLK työssäkäynti -aineistossa, mutta yleensä näiden virastotunnus (tpitunj_s) ja kunta- ja valtiosektorin toimipistetunnus (tpitunt_s) ovat näissä molemmissa aineistoissa samoja. 

Viimeisimmät aineistot ovat kansiossa FOLK_JAKSOT_C, jossa tiedostot ovat jaettuina vuositiedostoihin.  Tiedostonimet ovat muodossa folk_tyosuhde_"vuosi"_1.

Aikaisemmin julkaistut aineistot ovat FIONAssa kansiossa: FOLK_jaksot_a. 

Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@stat.fi

## Muuttujat / Variables (18)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `vuosi` | Vuosi | — | — | — |
| `hid_e` | Suojattu henkilön yksilöivä tunniste | — | — | — |
| `aineisto` | Aineistotunnus | — | — | Työsuhderekisterit |
| `rivinro` | Rivinumero | — | — | Työsuhderekisterit |
| `yrtun_s` | Suojattu yritystunnus | — | — | — |
| `ykstun_s` | Suojattu toimipaikan tunnus | — | — | — |
| `tpitunj_s` | Suojattu jäsenyhteisö- tai virastotunnus | — | — | — |
| `tpitunt_s` | Suojattu kunta- ja valtiosektorin toimipistetunnus | — | — | — |
| `alkupvm` | Työsuhteen alkamispäivä | — | — | Työsuhderekisterit |
| `loppupvm` | Loppupäivämäärä | — | — | Työsuhderekisterit |
| `tvm` | Henkilön päätyösuhde | — | — | Työsuhderekisterit |
| `atv` | Henkilön pisin työsuhde | — | — | Työsuhderekisterit |
| `sivu` | Henkilön sivutyösuhde | — | — | Työsuhderekisterit |
| `oyr_omist_tyyppi` | Omistajatyyppi | — | omistajatyyppi_1_1995_01_01 | Työsuhderekisterit |
| `oyr_oik_muoto` | Oikeudellinen muoto | — | oikeudell_muoto_1_1984_01_01 | Työsuhderekisterit |
| `oyr_sektoriluokka` | Sektoriluokka | — | sektoriluokitus_11_2013_01_01 | Työsuhderekisterit |
| `toimiala` | Toimipaikan toimiala | — | toimiala_1_2008_01_01 | Työsuhderekisterit |
| `tp_sijaintikunta` | Toimipaikan sijaintikunta | — | — | Työsuhderekisterit |

### Muuttujien määritelmät / Variable definitions

#### `vuosi` — Vuosi

Tilastovuosi.

#### `hid_e` — Suojattu henkilön yksilöivä tunniste

Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e -tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä.

#### `aineisto` — Aineistotunnus

**Ryhmä / Group:** Työsuhderekisterit

Aineistotunnus, joka ilmaisee lähdeaineiston. 

Tilastovuonna 2020:
1 = TyEL-työsuhteet (Työssäkäyntitilaston poiminta tulorekisteristä)
4 = YEL-yrittäjäsuhteet 
5 = MYEL-yrittäjäsuhteet 
20 = Verottajan vuosi-ilmoitusaineisto 

Tilastovuonna 2019:
1 = TyEL-työsuhteet (Työssäkäyntitilaston poiminta tulorekisteristä)
2 = TyEL-työsuhteet (ETK:n poiminta tulorekisteristä) 
4 = YEL-yrittäjäsuhteet 
5 = MYEL-yrittäjäsuhteet 
13 = Kaupunkien erillisaineistot 
20 = Verottajan vuosi-ilmoitusaineisto 

Ennen tilastovuotta 2019: 
1 = TEL-työsuhteet, vuodesta 2007 lähtien TyEL.
2 = LEL-työsuhteet (ei enää vuodesta 2007 lähtien, sisältyy TyEL:iin). 
3 = TaEL-työsuhteet (ei enää vuodesta 2007 lähtien, sisältyy TyEL:iin)
4 = YEL-yrittäjäsuhteet
5 = MYEL-yrittäjäsuhteet
6 = MEL-työsuhteet
7 = Kirkon työsuhteet
8 = KELA:n  työsuhteet
9 = Suomen Pankin työsuhteet
10 = KEVA:n työsuhteet
11 = Valtion työsuhteet
12 = Ahvenanmaan työsuhteet
13 = Kaupunkien erillisaineistot
14 = Helsingin Energian työsuhteet
15 = Valtionapulaitosten työsuhteet
20 = Verottajan vuosi-ilmoitusaineisto
86 = VEL-opettajat

#### `rivinro` — Rivinumero

**Ryhmä / Group:** Työsuhderekisterit

Työ- tai yrittäjäsuhteet erottava rivinumero. Yhdellä henkilöllä voi olla useampi työ- tai yrittäjäsuhde.

#### `yrtun_s` — Suojattu yritystunnus

Suojattu yritystunnus. 

HUOM! Vuodesta 2004 vuoteen 2005 tapahtui hallinnollisia muutoksia työnantajatunnuksissa. Virastotunnusten muuttuessa y-tunnus -muotoon henkilölle, jolla on aiemmin ollut yrtun_s-muuttujassa virastotunnus, on voinut tulla yrtun_s-muuttujaan y-tunnus. Samalla virastotunnus, joka aiemmin oli yrtun_s-muuttujassa on siirtynyt tpitunj_s-muuttujaan.

#### `ykstun_s` — Suojattu toimipaikan tunnus

Suojattu toimipaikkatunnus. 

HUOM! Julkisella sektorilla toimipaikkatunnus ei ole yksikäsitteinen, vaan sitä on aina käytettävä yhdessä yritystunnuksen (yrtun_s)  tai kuntien/kuntayhtymien jäsenyhteisötunnuksen tai valtion virastotunnuksen (tptitunj_s) kanssa. Myös yksityisellä sektorilla voi olla esim. virheellisistä toimipaikkatunnuksista ja yritysjärjestelyistä johtuen poikkeuksia, joissa toimipaikkatunnus liittyy useampaan kuin yhteen yritystunnukseen samana vuonna. Tapauksia voi rajata pois käyttämällä yritys/toimipaikkarekisteriä kehikkona.

#### `tpitunj_s` — Suojattu jäsenyhteisö- tai virastotunnus

Suojattu kuntien/kuntayhtymien jäsenyhteisötunnus tai valtion virastotunnus.

HUOM! Vuodesta 2004 vuoteen 2005 tapahtui hallinnollisia muutoksia työnantajatunnuksissa. Virastotunnusten muuttuessa y-tunnus -muotoon henkilölle, jolla on aiemmin ollut yrtun_s-muuttujassa virastotunnus, on voinut tulla yrtun_s-muuttujaan y-tunnus. Samalla virastotunnus, joka aiemmin oli yrtun_s-muuttujassa on siirtynyt tpitunj_s-muuttujaan.

#### `tpitunt_s` — Suojattu kunta- ja valtiosektorin toimipistetunnus

Suojattu toimipistetunnus. Kunta- ja valtiosektorin työsuhteilla. 

HUOM! Julkisella sektorilla toimipistetunnus ei ole yksikäsitteinen, vaan sitä on aina käytettävä yhdessä yritystunnuksen (yrtun_s)  tai kuntien/kuntayhtymien jäsenyhteisötunnuksen tai valtion virastotunnuksen (tptitunj_s) kanssa. Julkisen sektorin toimipistetunnus tpitunt_s voi myös vaihdella vuodesta toiseen samalla toimipaikalla ja se voi kuvata eritasoisia yksiköitä.

#### `alkupvm` — Työsuhteen alkamispäivä

**Ryhmä / Group:** Työsuhderekisterit

Työ- tai yrittäjäsuhteen alkamispäivämäärä. 

Tulorekisterin tiedoissa kyseessä on maksujakson alkamispäivä. Tilastossa on ketjutettu maksujaksoja yhteen, jos niissä ei ole yli kuukauden katkoa.

#### `loppupvm` — Loppupäivämäärä

**Ryhmä / Group:** Työsuhderekisterit

Työ- tai yrittäjäsuhteen loppumispäivämäärä.

#### `tvm` — Henkilön päätyösuhde

**Ryhmä / Group:** Työsuhderekisterit

Henkilön päätyösuhde. Muodostetaan pääasiallisen toiminnan päättelyajossa. Työvoimakäsite (TVM) määrittyy vuoden viimeisen viikon työsuhteen mukaan. Merkitään TVM = 1. 

Henkilön vuoden viimeisen viikon työsuhde on päätelty työssäkäyntitilastossa tilastovuodesta 2019 lähtien tulorekisterin perusteella.

#### `atv` — Henkilön pisin työsuhde

**Ryhmä / Group:** Työsuhderekisterit

Henkilön pisin työsuhde. ATV-työsuhde merkitään ATV = 1. Ammatissatoimivuus käsite = ATV, eli määritellään kyseisen vuoden pisimmän työsuhteen mukaan. 

Henkilön vuoden pisin työsuhde on päätelty tilastovuodesta 2019 lähtien tulorekisterin maksujaksotiedoista, mikä heikentää vertailukelpoisuutta tilastovuosien välillä. ATV-tietoa ei käytetä virallisissa tilastojulkistuksissa.

#### `sivu` — Henkilön sivutyösuhde

**Ryhmä / Group:** Työsuhderekisterit

Henkilön sivutyösuhde. Muodostetaan pääasiallisen toiminnan päättelyajossa. Henkilölle valitaan vain yksi sivutyösuhde, vaikka henkilöllä olisikin useampi (sivu)työsuhde. Merkitään sivu = 1. Tietoa on vuodesta 1992 lähtien.

#### `oyr_omist_tyyppi` — Omistajatyyppi

**Luokitus / Classification:** omistajatyyppi_1_1995_01_01 · **Ryhmä / Group:** Työsuhderekisterit

Oikeudellisen yksikön omistajatyyppi. Yritys- ja toimipaikkarekisterin yritykset ja yhteisöt jaetaan omistajuuden perusteella luokkiin. 

Vuodesta 1996 alkaen arvoalue: 
1 = Yksityinen kotimainen 
2 = Valtio 
3 = Kunta 
4 = Ahvenanmaan maakunta 
5 = Ulkomaalaisomisteinen 
6 = Muu omistajatyyppi, tuntematon 

1987-1995 arvoalue: 
1 = Yksityinen kotimainen 
2 = Valtio 
3 = Kunta 
4 = Kuntainliitto 
6 = Ulkomaalaisten osuus yli 20 %, enintään 50 %
7 = Ulkomaalaisten osuus yli 50 % 
9 = Muu omistajatyyppi, tuntematon

#### `oyr_oik_muoto` — Oikeudellinen muoto

**Luokitus / Classification:** oikeudell_muoto_1_1984_01_01 · **Ryhmä / Group:** Työsuhderekisterit

Oikeudellisen yksikön oikeudellinen muoto eli yritysmuoto. 

11 = Luonnollinen henkilö
12 = Kuolinpesä, perikunta
13 = Verotusyhtymä
14 = Avoin yhtiö
15 = Konkurssipesä
21 = Kommandiittiyhtiö
22 = Laivanisännistöyhtiö (ei osakeyhtiö)
31 = Osakeyhtiö
32 = Keskinäinen vakuutusyhtiö
33 = Säästöpankki
34 = Eläkesäätiö tai -kassa, työeläkelaitos
35 = Asunto-osakeyhtiö
41 = Osuuskunta
51 = Säätiö, rahasto
52 = Aatteellinen yhdistys
53 = Keskinäinen vahinkovakuutusyhdistys
54 = Taloudellinen yhdistys
61 = Julkinen viranomainen
62 = Julkinen liikelaitos
63 = Julkisoikeudellinen yhteisö
71 = Valtionkirkko
72 = Muu uskonnollinen yhteisö
90 = Muu oikeudellinen muoto

#### `oyr_sektoriluokka` — Sektoriluokka

**Luokitus / Classification:** sektoriluokitus_11_2013_01_01 · **Ryhmä / Group:** Työsuhderekisterit

Oikeudellisen yksikön sektoriluokka. Luokitus,  jossa yksiköt jaetaan omistajuuden, toiminnan tarkoituksen ja rahoitustavan perusteella eri sektoreihin. Tietoja vuodesta 1989 lähtien. 

Vuosina 1989-1994 ja vuosina 1995-1998 luokituksissa jo kahden numeron tasolla merkittäviä eroja, mutta luokitukset ovat samat ensimmäisen numeron tasolla: 
1	Yritykset 
2	Rahoitus- ja vakuutuslaitokset 
3	Julkisyhteisöt  
4	Voittoa tavoittelemattomat yhteisöt 
5	Kotitaloudet 
6	Ulkomaat 

Vuosien 1999-2012 luokituksen ensimmäinen numero: 
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

Luokitus vuodesta 2013 lähtien:
1	= Koko kansantalous (kotimaiset sektorit) 
11	= Yritykset ja asuntoyhteisöt 
111	= Yritykset 
1111	= Julkiset yritykset 
11111	= Valtion yritykset 
11112	= Kuntien yritykset 
1112	= Yksityiset yritykset 
11121	= Yksityiset kotimaiset  yritykset 
111211	= Yksityiset suomalaisomisteiset yritykset 
111212	= Yksityiset ulkomaalaisvähemmistöiset yritykset 
11122	= Yksityiset ulkomaalaisenemmistöiset yritykset 
112	= Asuntoyhteisöt 
12	= Rahoitus- ja vakuutuslaitokset
121-2	= Rahalaitokset (S.121, S.122)
121	= Suomen Pankki
122	= Muut rahalaitokset
1221	= Talletuspankit
1222	= Rahamarkkinarahastot
1223	= Muut rahoitusta välittävät rahalaitokset
123	= Muut rahoituslaitokset
124	= Rahoituksen ja vakuutuksen välitystä avustavat laitokset
125	= Vakuutuslaitokset
13	= Julkisyhteisöt
1311	= Valtionhallinto
1312	= Osavaltiohallinto (ei käytössä Suomessa)
1313	= Paikallishallinto
13131	= Kunnat
13132	= Kuntayhtymät
13133	= Ahvenanmaan maakuntahallinto
1314	= Sosiaaliturvarahastot
13141	= Työeläkelaitokset
13149	= Muut sosiaaliturvarahastot
14	= Kotitaloudet
141	= Työnantaja- ja muut elinkeinonharjoittajien kotitaloudet (EKT95: S.141= S.142)
1411	= Maatilataloudenharjoittajien kotitaloudet
1419	= Muut elinkeinonharjoittajien kotitaloudet
143	= Palkansaajakotitaloudet
144	= Omaisuustulojen ja tulonsiirtojen saajakotitaloudet (EKT95: S.1441, S.1442, S.1443)
145	= Laitoskotitaloudet
15	= Kotitalouksia palvelevat voittoa tavoittelemattomat yhteisöt
151	= Valtionkirkot
152	= Muut voittoa tavoittelemattomat yhteisöt
2	= Ulkomaat
21	= Euroopan Unioni
211	= Euroopan unionin jäsenmaat
2111	= EMU:n  jäsenmaat
2112	= EU:n muut jäsenmaat
212	= Euroopan unionin toimielimet
22	= Muut maat ja kansainväliset järjestöt
221	= Muut maat
222	= Kansainväliset järjestöt

Sektoriluokitus 2012 http://www.stat.fi/meta/luokitukset/sektoriluokitus/versio.html. Muut luokitukset pyydettävä Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@tilastokeskus.fi.

#### `toimiala` — Toimipaikan toimiala

**Luokitus / Classification:** toimiala_1_2008_01_01 · **Ryhmä / Group:** Työsuhderekisterit

Työnantajan toimiala. Käytössä seuraavat luokitukset: 
 toimiala_1_08_s (TOL2008) vuodesta 2007 lähtien 
 toimiala_1_02_s (TOL2002) vuodet 2001-2006 
 toimiala_1_00_s (TOL95, toinen tarkistettu painos) vuodet 1998-2000
 toimiala_1_95_s (TOL95) vuodet 1993-1997
 toimiala_1_88_s (TOL88) vuodet 1987-1992 

Luokitusavaimet: http://www.stat.fi/meta/luokitukset/toimiala/001-2008/luokitusavaimet.html ja http://www.stat.fi/meta/luokitukset/toimiala/versio.html

#### `tp_sijaintikunta` — Toimipaikan sijaintikunta

**Ryhmä / Group:** Työsuhderekisterit

Toimipaikan sijaintikunta. Tietoja vuosilta 1987-2000.

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
