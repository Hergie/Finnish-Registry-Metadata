# FOLK perustieto

- **Identifier:** `FOLK_19872023_jua_perus24_001.xml`
- **DOI:** `work_2017-11_2017-11-02_ain_0001`
- **Temporal coverage:** 1987-01-01 - 2024-12-31
- **Published:** 2026-01-26
- **Organisation:** Tilastokeskus
- **Variable count:** 61
- **Observation count:** —
- **Population:** Kunkin vuoden viimeisenä päivänä Suomessa vakituisesti asunut väestö

## Description

FOLK-henkilöaineiston perustietomoduuli sisältää väestörakenne-, tulo- ja työssäkäyntitilastojen tietoja sekä muutamia perhetilaston ja väestön koulutusrakennetilaston tietoja. Tiedot ovat kunkin vuoden lopusta ja yleensä vastaavat virallisia (SVT) tietoja julkaisuajankohtana. Niillä moduulin karkeistetuilla tiedoilla, joista on karkeistamaton tieto saatavissa toisesta FOLK-moduulista tai muualta Tilastokeskuksen tietovarannoista, on loppulyhenteenä _k tai _k2. 

Aineistossa on tietoja vuodesta 1987 lähtien vuoteen 2024 saakka. Poikkeamat tietojen saatavuudessa on merkitty muuttujankuvaukseen vuosiluvuilla lukuun ottamatta niitä edelleen päivittyviä tietoja, joiden päivitysaikataulu on muita tietoja myöhäisempi. Tällöin tämän tiedon viimeinen vuosi on merkitty muuttujankuvauksessa: (aineiston viimeinen vuosi - 1) tai (aineiston viimeinen vuosi - 2). 

Aineisto on tarkoitettu FIONA-etäpalvelun kautta käytettäväksi. Tiedot on linkitettävissä muiden henkilövalmisaineistomoduulien kanssa suojatun henkilönumeron avulla. 

Vimeisimmät FOLK perustieto-aineistot ovat kansiossa FOLK_PERUS_C, jossa tiedostot ovat jaettuna tilastovuosittain. Tiedostonimet ovat muodossa folk_perus_"vuosi"_1. Tilastovuoden tiedot päivitetään noin 6 kk alkuperäisen päivityksen jälkeen; mahdolliset muutokset on kuvattu muuttujakohtaisesti.

Vanhat FOLK perustieto -aineistot ovat FIONAssa seuraavissa tiedostoissa:
Totaaliaineisto vuosille 2011-2020: FOLK_perus_11a
Totaaliaineisto vuosille 2001-2010: FOLK_perus_0110a
Totaaliaineisto vuosille 1987-2000: FOLK_perus_8800a 

Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@tilastokeskus.fi.

## Variables (61)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `vuosi` | Vuosi | — | — | — |
| `hid_e` | Suojattu henkilön yksilöivä tunniste | — | — | Vaestorakenne |
| `syntyv` | Syntymävuosi | — | — | Vaestorakenne |
| `kuolv` | Kuolinvuosi | — | — | Vaestonmuutos |
| `sukup` | Sukupuoli | — | — | Vaestorakenne |
| `smkunta` | Syntymämaakunta | — | — | Vaestorakenne |
| `skunta` | Syntymäkunta | — | — | Vaestorakenne |
| `svaltio_k` | Syntymävaltio | — | — | Vaestorakenne |
| `kansa1_k` | Kansalaisuus | — | — | Vaestorakenne |
| `syntyp2` | Syntyperä | — | — | Vaestorakenne |
| `kieli_k` | Kieli | — | — | Vaestorakenne |
| `ika` | Ikä | — | — | Vaestorakenne |
| `mkunta` | Asuinmaakunta | — | — | Vaestorakenne |
| `kunta` | Asuinkunta | — | — | Vaestorakenne |
| `kuntaryhm` | Kuntaryhmä (kunta) | — | — | — |
| `kunta31_12` | Asuinkunta tilastovuonna | — | — | — |
| `kuntaryhm31_12` | Kuntaryhmä (kunta31_12) | — | — | — |
| `maka` | Maaseutu-kaupunki -luokitus | — | — | — |
| `taajama_k2` | Asuinpaikka taajamassa | — | — | — |
| `sivs` | Siviilisääty | — | — | Vaestorakenne |
| `sose` | Sosioekonominen asema | — | — | Ammatti |
| `yotutk` | Ylioppilastutkinto | — | — | Opiskelijat ja tutkinnot |
| `ututku_aste` | Korkeimman tutkinnon koulutusaste | — | — | Opiskelijat ja tutkinnot |
| `ututku_ala` | Korkeimman tutkinnon koulutusala | — | — | Opiskelijat ja tutkinnot |
| `suorv` | Korkeimman tutkinnon suoritusvuosi | — | — | Opiskelijat ja tutkinnot |
| `amas1` | Ammattiasema (TVM) | — | — | Ammatti |
| `klaji_k2` | Koulutuslaji | — | — | Opiskelijat ja tutkinnot |
| `optuki` | Saanut opintotukea | — | — | — |
| `ptoim1` | Pääasialllinen toiminta (TVM) | — | — | Tyossakaynti |
| `ammattikoodi_k` | Ammattikoodi, 3-nrotaso | — | — | Ammatti |
| `tyke` | Työttömyyskuukausia | — | — | Työnhakijarekisteri, Tyossakaynti |
| `tyokk` | Työssäolokuukausia | — | — | Tyossakaynti |
| `akoko_k` | Asuntokunnan koko | — | — | Asuminen |
| `asty` | Asuntokuntarakenne | — | — | Asuminen |
| `hape` | Hallintaperuste | — | — | Asuminen |
| `hulu` | Huoneluku keittiö pl. | — | — | Asuminen |
| `taty` | Talotyyppi | — | — | Rakennus |
| `vata` | Varustetaso | — | — | Asuminen |
| `penulaika` | Perheen nuorimman lapsen ikä | — | — | Perhe |
| `peas` | Perheasema | — | — | Perhe |
| `lkm_k` | Perheen lasten lkm | — | — | Perhe |
| `a18lkm_k` | Perheen alle 18 v. lasten lukumäärä | — | — | Perhe |
| `a7lkm_k` | Perheen alle 7 v. lasten lukumäärä | — | — | Perhe |
| `a3lkm_k` | Perheen alle 3 v. lasten lkm | — | — | Perhe |
| `pekoko_k` | Perheen koko | — | — | Perhe |
| `pety` | Perhetyyppi | — | — | Perhe |
| `vela` | Vanhuuseläke | — | — | Eläke |
| `tkela` | Työkyvyttömyyseläke | — | — | Eläke |
| `tyela` | Työttömyyseläke | — | — | Eläke |
| `mela` | Maatalouden erityiseläke | — | — | Eläke |
| `osela` | Osa-aikaeläke | — | — | Eläke |
| `pela` | Perhe-eläke | — | — | Eläke |
| `yvela` | Yksilöllinen varhaiseläke | — | — | Eläke |
| `kturaha_k` | Käytettävissä olevat rahatulot | — | — | Tulonjakotilasto |
| `velaty_k` | Velat yhteensä | — | — | Henkilöverotusaineisto |
| `lvar_k` | Verotettava varallisuus | — | — | Henkilöverotusaineisto |
| `svatva_k` | Ansiotulot yhteensä valtion verotuksessa | — | — | Henkilöverotusaineisto |
| `palk_k` | Palkkatulot | — | — | Tulonjakotilasto |
| `tyotu_k` | Summatut työtulot (palkkatulot) | — | — | Henkilöverotusaineisto |
| `tyrtuo_k` | Yrittäjätulot | — | — | Henkilöverotusaineisto |
| `auto_k` | Henkilön omistama/hallitsema ajoneuvo | — | — | — |

### Variable definitions

#### `vuosi` — Vuosi

Tilastovuosi.

#### `hid_e` — Suojattu henkilön yksilöivä tunniste

**Group:** Vaestorakenne

Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e -tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä.

#### `syntyv` — Syntymävuosi

**Group:** Vaestorakenne

Syntymävuosi.

#### `kuolv` — Kuolinvuosi

**Group:** Vaestonmuutos

Kuolinvuosi. Henkilön kuolinvuosi päivittyy kuolinvuotta edeltävälle tilastovuodelle. Tilastovuoden toisessa päivityksessä päivittyy tieto niistä kuolemista, jotka ovat tulleet tilastoon viiveellä.

#### `sukup` — Sukupuoli

**Group:** Vaestorakenne

Henkilön viimeisin sukupuolitieto. Tieto on sama joka vuonna, vaikka henkilön sukupuoli olisi muuttunut. Tieto on vuodesta 2021 alkaen tiedostossa folk_perus_sukup_1. 
1 = Mies
2 = Nainen

#### `smkunta` — Syntymämaakunta

**Group:** Vaestorakenne

Maakunta tuoreimman alueluokituksen mukainen.

#### `skunta` — Syntymäkunta

**Group:** Vaestorakenne

Syntymäkotikunta on henkilön syntymävuoden kuntaluokituksen mukainen.

#### `svaltio_k` — Syntymävaltio

**Group:** Vaestorakenne

Henkilön syntymävaltio.
 1=Suomi 
2=Muu 
bl= puuttuva

#### `kansa1_k` — Kansalaisuus

**Group:** Vaestorakenne

Henkilön viimeisin kansalaisuustieto. Tieto on vuoteen 2020 asti sama  joka vuonna, vaikka henkilön kansalaisuus olisi muuttunut. 
1 = suomi 
2 = muu 
bl = puuttuva

#### `syntyp2` — Syntyperä

**Group:** Vaestorakenne

Syntyperä, arvot:
11= Suomalaistaustainen, syntynyt Suomessa 
12 =Suomalaistaustainen, syntynyt ulkomailla 
21= Ulkomaalaistaustainen, syntynyt Suomessa 
22= Ulkomaalaistaustainen, syntynyt ulkomailla

#### `kieli_k` — Kieli

**Group:** Vaestorakenne

Henkilön viimeisin kielitieto. Tieto on vuoteen 2020 asti sama  joka vuonna, vaikka henkilön kieli olisi muuttunut. 
1 = suomi 
2 = ruotsi  
3 = muu

#### `ika` — Ikä

**Group:** Vaestorakenne

Henkilön ikä vuosissa vuoden lopussa.

#### `mkunta` — Asuinmaakunta

**Group:** Vaestorakenne

Maakunta tuoreimman alueluokituksen mukainen.

#### `kunta` — Asuinkunta

**Group:** Vaestorakenne

Henkilön asuinkunta vuoden viimeisenä päivänä. Alueluokitus on 1.1. tilastovuosi + 1 vuodesta 1999 lähtien. Tätä ennen aluejako on ollut 1.1. tilastovuosi. Kuntanumero 3 merkkiä.

#### `kuntaryhm` — Kuntaryhmä (kunta)

Asuinkunnan kuntaryhmä. Alueluokitus on 1.1. tilastovuosi + 1. Tietoja vuodesta 1999 lähtien.

1 kaupunkimaiset kunnat 
2 taajaan asutut 
3 maaseutumaiset.

#### `kunta31_12` — Asuinkunta tilastovuonna

Henkilön asuinkunta vuoden viimeisenä päivänä. Alueluokitus on 31.12. tilastovuosi. Kuntanumero 3 merkkiä. Tietoja vuosilta 1987-1998 ja vuodesta 2005 lähtien vuosittain.

#### `kuntaryhm31_12` — Kuntaryhmä (kunta31_12)

Asuinkunnan kuntaryhmä. Alueluokitus on 31.12. tilastovuosi. Tietoja vuosilta 1987-1998 ja vuodesta 2005 lähtien vuosittain.

1 = kaupunkimaiset kunnat 
2 = taajaan asutut 
3 = maaseutumaiset

#### `maka` — Maaseutu-kaupunki -luokitus

SYKE:n aluetypologian mukainen maaseutu-kaupunki -luokitus. Vuoteen 2018 asti luokitus perustuu vuoden 2013 aineistoihin, ja  vuodesta 2019 lähtien aluetypologia perustuu vuoden 2018 aineistoihin.  

Luokat: 
K1 Sisempi kaupunkialue 
K2 Ulompi kaupunkialue 
K3 Kaupungin kehysalue 
M4 Maaseudun paikalliskeskus 
M5 Kaupungin läheinen maaseutu 
M6 Ydinmaaseutu 
M7 Harvaan asuttu maaseutu. 

Lisätietoja luokituksesta https://www.ymparisto.fi/kaupunkimaaseutuluokitus.

#### `taajama_k2` — Asuinpaikka taajamassa

1 = Asuinpaikka taajamassa, 
0 = Asuinpaikka haja-asutusalueella. Tieto päivittyy tilaston tuoreilla tiedoilla vuoden alussa tehtävässä tilastovuoden toisessa päivityksessä.

#### `sivs` — Siviilisääty

**Group:** Vaestorakenne

Siviilisääty, arvot:
1 = naimaton 
2 = aviossa, rekisteröidyssä parisuhteessa tai asumuserossa 
4 = eronnut tai eronnut rekisteröidystä parisuhteesta 
5 = leski tai leski rekisteröidystä parisuhteesta

#### `sose` — Sosioekonominen asema

**Group:** Ammatti

Sosioekonominen asema -tieto vuosilta 1990, 1993, 1995, 2000 ja vuodesta 2004 tieto vuosittain (aineiston viimeinen vuosi -1) -vuoteen asti. Perustuu tietoihin henkilön pääasiallisesta toiminnasta, ammatista, ammattiasemasta sekä toimialasta. Henkilöt on luokiteltu oman toimintansa perusteella lukuun ottamatta 0-15 -vuotiaita ja ryhmää "muut työvoimaan kuulumattomat" (lähinnä omaa kotitaloutta hoitavat), jotka ovat saaneet asuntokunnan viitehenkilön sosioekonomisen aseman.

Yrittäjät	
10 Maa- ja metsätalousyrittäjät	
20 Yrittäjät (ei maa- ja metsätalous)	
Ylemmät toimihenkilöt	
31 Johtotehtävissä toimivat ylemmät toimihenkilöt	
32 Suunnittelu- ja tutkimustehtävissä toimivat ylemmät toimihenkilöt	
33 Opetustehtävissä toimivat ylemmät toimihenkilöt	
34 Muut ylemmät toimihenkilöt	
Alemmat toimihenkilöt	
41 Työnjohtotehtävissä toimivat alemmat toimihenkilöt	
42 Itsenäistä toimistotyötä tekevät alemmat toimihenkilöt	
43 Epäitsenäistä toimistotyötä tekevät alemmat toimihenkilöt	
44 Muut alemmat toimihenkilöt	
Työntekijät	
51 Maa- ja metsätaloustyöntekijät	
52 Teollisuustyöntekijät	
53 Muut tuotantotyöntekijät	
54 Jakelu- ja palvelutyöntekijät	
59 Muut työntekijät
	
Vuosina 1990 ja 1993:
60 Eläkeläiset	
70 Opiskelijat ja koululaiset (16 v. täyttäneet)	
Muut	
91 Työttömät	
92 Työlliset, joiden ammatti tuntematon	
93 Muut työvoiman ulkopuolella olevat	
94,99 Sosioekonominen asema tuntematon	

Vuodesta 1995-
60 Opiskelijat	
70 Eläkeläiset	
81 Työttömät	
82 Muut (varusmiehet)	
99 Tuntematon

#### `yotutk` — Ylioppilastutkinto

**Group:** Opiskelijat ja tutkinnot

0 = henkilö ei ole suorittanut pohjakoulutuksena yo-tutkintoa tai yo-tutkinnosta ei ole tietoa 
4 = henkilö on suorittanut pohjakoulutuksena yo-tutkinnon 

Tietoja (aineiston viimeinen vuosi -1) -vuoteen asti.

#### `ututku_aste` — Korkeimman tutkinnon koulutusaste

**Group:** Opiskelijat ja tutkinnot

Korkeimman tutkinnon koulutusaste (taso-1) Tilastokeskuksen tuoreimman koulutusluokituksen mukaisesta koulutuskoodista, joka on ajan yli yhtenäinen. Koulutusasteen taso 1 on sama kuin ISCED 2011 -luokituksessa.

Koulutusaste, taso-1

3 Toinen aste
4 Erikoisammattikoulutusaste
5 Alin korkea-aste
6 Alempi korkeakouluaste
7 Ylempi korkeakouluaste
8 Tutkijakoulutusaste
9 Koulutusaste tuntematon

Tiedot pohjautuvat Tilastokeskuksen tutkintorekisteriin.  Tutkintorekisterin perustana on vuoden 1970 väestölaskennassa kerätyt tutkintotiedot. Vuosittain päivitettävät tiedot saadaan suoraan koulutuksen järjestäjiltä tai valtakunnallisista KOSKI- ja VIRTA-tietovarannoista.

Rekisteri on kattava Suomessa suoritetuista tutkinnoista, mutta alipeittoinen ulkomailla suoritetuista tutkinnoista. Suomeen muuttavilta henkilöiltä ei kysytä ulkomailla suoritetusta koulutuksesta maahan saapumisen yhteydessä. Tutkintorekisteriin lisätään Valviran rekisteritietoja ulkomailla suoritetuista ja Suomessa laillistetuista terveydenhuollon tutkinnoista, Pohjoismaiden tilastovirastoilta saatuja tutkintotietoja sekä erilliskyselyillä kerättyjä tutkintotietoja.




Tietoja (aineiston viimeinen vuosi -1) -vuoteen asti.

#### `ututku_ala` — Korkeimman tutkinnon koulutusala

**Group:** Opiskelijat ja tutkinnot

Korkeimman tutkinnon koulutusala (1-taso). Tilastokeskuksen tuoreimman koulutusluokituksen mukaisesta koulutuskoodista, joka on ajan yli yhtenäinen. Koulutusalan taso 1 on sama kuin ISCED 2011 -luokituksessa.

Koulutusala, 1-taso
00 Yleissivistävä koulutus
01 Kasvatusalat
02 Humanistiset ja taidealat
03 Yhteiskunnalliset alat
04 Kauppa, hallinto ja oikeustieteet
05 Luonnontieteet
06 Tietojenkäsittely ja tietoliikenne (ICT)
07 Tekniikan alat
08 Maa- ja metsätalousalat
09 Terveys- ja hyvinvointialat
10 Palvelualat
99 Muut tai tuntemattomat koulutusalat

Tietoja (aineiston viimeinen vuosi -1) -vuoteen asti.

#### `suorv` — Korkeimman tutkinnon suoritusvuosi

**Group:** Opiskelijat ja tutkinnot

Korkeimman tutkinnon suoritusvuosi. Tietoja (aineiston viimeinen vuosi -1) -vuoteen asti.

#### `amas1` — Ammattiasema (TVM)

**Group:** Ammatti

Ammattiasema päätyösuhteen mukaan (tvm-päättely). 
1 = palkansaaja 
2 = yrittäjä

Tieto vuosittain (aineiston viimeinen vuosi - 1) -vuoteen asti.

#### `klaji_k2` — Koulutuslaji

**Group:** Opiskelijat ja tutkinnot

Opiskelijan koulutuslaji, tietoja vuodesta 1999 alkaen vuosittain (aineiston viimeinen vuosi - 1) -vuoteen asti. 

1 = Esi-, perus- tai lisäopetus (10-luokka) (tilastvuosi 2020- ) 
2 = Lukiokoulutus 
3 = Ammatillinen koulutus (tilastovuoteen 2018 asti)
4 = AMK 
5 = Korkeakoulutus
6 = Ammatillinen koulutus (tilastovuosi 2018)
7 = Ammatillinen koulutus (tilastovuosi 2019-)
8 = Ammatillinen koulutus (tilastovuosi 2019-)

#### `optuki` — Saanut opintotukea

K = Saanut opintotukea keväällä 
S = Saanut opintotukea syksyllä 
M = Saanut opintotukea molempina lukukausina 

Tietoja vuodesta 1988 lähtien vuosittain (aineiston viimeinen vuosi - 1) -vuoteen asti.

#### `ptoim1` — Pääasialllinen toiminta (TVM)

**Group:** Tyossakaynti

Pääasiallinen toiminta (Työvoimakäsite = TVM eli vuoden viimeisen viikon työsuhteen mukaan). 
11 = työllinen 
12 = työtön 
21 = 0-14 -vuotias 
22 = opiskelija, koululainen 
24 = eläkeläinen 
25 = varusmies, siviilipalvelusmies 
29 = työttömyyseläkkeellä (vain PTOIM1) 
99 = muu työvoiman ulkopuolella oleva
Tieto vuosittain (aineiston viimeinen vuosi - 1) -vuoteen asti. 

HUOM! Tilastovuodesta 2019 lähtien palkansaajien päättelyn pääasiallinen lähdeaineisto on tulorekisteri. Aineistossa palkansaajat päätellään maksujakson voimassaolon perusteella. 

Lisätietoa pääasiallisen tominnan päättelystä Fionassa: 
\metadata\Finnish metadata\Lyhyt kuvaus pääasiallisen toiminnan päättelystä.docx
\metadata\Finnish metadata\ptoim_paattely_fiona.pptx
Lisätietoa myös muuttujan historiasta (englanniksi):
\metadata\English metadata\ptoim_paattely_fiona_en.pptx

Muuttujassa perhevapailla olevat henkilöt päätyvät työllisiksi (ptoim1=11), mikäli saavat palkkaa työnantajalta, muussa tapauksessa he päätyvät muihin luokkiin pääasiallisen toiminnan päättelyjärjestyksen mukaisesti. Ansiosidonnaisella olevat päätyvät työttömiksi (ptoim1=12) (myös osa-aikatyötä tekevät), sillä työttömät päätellään ennen työllisiä pääasiallisen toiminnan päättelyssä

#### `ammattikoodi_k` — Ammattikoodi, 3-nrotaso

**Group:** Ammatti

Tietoja vuosilta 1990, 1993, 1995, 2000 ja vuodesta 2004 lähtien vuosittain vuoteen (aineiston viimeinen vuosi -1) asti. Tieto henkilön ammatista on tuotettu 18-74-vuotiaille työllisille, siis palkansaajille ja yrittäjille. Ammattitiedot perustuvat pääasiassa eri hallinnollisista aineistoista (työsuhdeaineistot) ja Tilastokeskuksen palkkatilastoista saatuihin ammatti-, virka- ja tehtävänimikkeisiin ja -koodeihin. Lisäksi tehdään erillinen ammattitiedonkeruu vuosittain. 

Henkilön ammattikoodi tuotetaan ensisijaisesti vuoden viimeisen viikon päätyösuhteen mukaisen ammatin perusteella. Ammattinimikkeiden lisäksi tiedon tuottamisessa käytetään hyväksi tietoa henkilön työpaikan toimialasta ja sektorista sekä henkilön koulutuksesta. Ammattitietojen tuottamista ohjaa kansainvälisen työjärjestön ILO:n laatima hierarkkinen luokitusjärjestelmä International Standard Classification of Occupations, lyh. ISCO. 
Luokitusstandardit:
Vuodesta  2010 lähtien:  Ammattiluokitus 2010 (AML 2010).   
Vuosina 1995, 2000, 2004 - 2009: Ammattiluokitus 2001. 
Vuosina 1990  ja 1993: Ammattiluokitus 1980. 
Eri luokitusstandardeilla tuotetut tiedot eivät ole keskenään vertailukelpoiset. Tilastossa käytetyt luokitukset samoin kun luokitusten väliset avaimet löytyvät Tilastokeskuksen luokitus- ja metatietopalvelujen kotisivuilta osoitteesta: https://www.stat.fi/fi/luokitukset/ sekä painetuista luokituskäsikirjoista.

#### `tyke` — Työttömyyskuukausia

**Group:** Työnhakijarekisteri, Tyossakaynti

Henkilön työttömyyskuukaudet -tieto vuosittain (aineiston viimeinen vuosi - 1) -vuoteen asti. Vuodesta 2005 lähtien tieto laskettu työttömyyspäivien lukumäärästä. 

1-14 päivää = 0 
15-44 päivää = 1 
45-74 päivää  =2 
75-104 päivää = 3 
105-135 päivää = 4 
136-165 päivää = 5 
166-196 päivää = 6 
197-226 päivää = 7 
227-256 päivää = 8 
257-287 päivää = 9 
288-317 päivää = 10 
318-348 päivää = 11 
349-365(366) päivää = 12

Vuosina 1987-2004 kukin kalenterikuukausi laskettu erikseen. Jos kalenterikuukautena vähintään 16 työttömyyspäivää, on koko kuukausi laskettu täydeksi työttömyyskuukaudeksi.

#### `tyokk` — Työssäolokuukausia

**Group:** Tyossakaynti

Henkilön työssäolokuukaudet. Tietoja vuodesta 1997 lähtien vuoteen (aineiston viimeinen vuosi -1) asti. Tilastovuodesta 2019 lähtien työssäkäyntitilastossa siirryttiin käyttämään palkansaajien lähdeaineistona tulorekisteriä, jossa työsuhteden kesto lasketaan maksujakson mukaan. Muuttuja ei ole enää suoraan vertailukelpoinen aiempiin vuosiin lähdeaineiston muutoksen vuoksi. 

Vuodesta 2005 lähtien tieto laskettu työpäivien lukumäärästä: 
1-14 päivää=0 
15-44 päivää=1 
45-74 päivää=2 
75-104 päivää=3 
105-135 päivää=4 
136-165 päivää=5 
166-196 päivää=6 
197-226 päivää=7 
227-256 päivää=8 
257-287 päivää=9 
288-317 päivää=10 
318-348 päivää=11 
349-365(366) päivää=12 

1997-2004: Kukin kalenterikuukausi laskettu erikseen. Jos kalenterikuukautena vähintään 16 työpäivää, on koko kuukausi laskettu täydeksi työkuukaudeksi. 

Vuodet 1997-1998 luokka 0 = 1-15 päivää ml. henkilöt joilla ei työssäolopäiviä. 
Vuodet 1999-2004 null=ei työpäiviä, 0 = 1-15 päivää.

#### `akoko_k` — Asuntokunnan koko

**Group:** Asuminen

Asunnossa vuoden viimeisenä päivänä vakinaisesti asuvien henkilöiden lukumäärä. 
1 = 1 henkilö 
2 = 2 henkilöä 
3 = 3 henkilöä 
4 = 4 henkilöä 
5 = 5 henkilöä 
6 = 6 henkilöä 
7 = 7 henkilöä 
8 = 8 henkilöä 
9 = 9+ henkilöä

#### `asty` — Asuntokuntarakenne

**Group:** Asuminen

Asuntokuntarakenne. Luokitus 2006 alkaen: 
1 = 1 perhe, ei muita
2 = 1 perhe ja muita 
3 = 2 perhettä, ei lisäksi muita 
4 = 2 perhettä, lisäksi muita 
5 = vähintään 3 perhettä, ei lisäksi muita 
6 = vähintään 3 perhettä, lisäksi muita 
7 = ei perhettä, asuntokunnan koko = 1 
8 = ei perhettä, asuntokunnan koko = 2, joilla sama sukupuoli 
9 = ei perhettä, asuntokunnan koko = 2, joilla eri sukupuoli 
10 = ei perhettä, asuntokunnan koko > 2, kaikilla sama sukupuoli 
11 = ei perhettä, asuntokunnan koko > 2, joilla eri sukupuoli null = ei perheitä 

Luokitus vuoteen 2005: 
1 = 1 perhe ja ei muita 
2 = 1 perhe ja muita 
3 = 2 + perhettä ja ei muita 
4 = 2 + perhettä ja muita 
5 = ei perhettä, 1 henkilö 
6 = ei perhettä, 2 henkilöä samaa sukupuolta 
7 = ei perhettä, 2 henkilöä eri sukupuolta 
8 = ei perhettä, väh. kolme henkilä samaa sukupuolta 
9 = ei perhettä vähintään 3 henkilöä, kaikki eivät samaa sukupuolta 
null = ei perheitä 

Tietoja vuodesta 1990 alkaen. Tieto vuosittain (aineiston viimeinen vuosi - 1) -vuoteen asti.

#### `hape` — Hallintaperuste

**Group:** Asuminen

Asunnon hallintaperuste on pääsääntöisesti päätelty vakinaisesti asutuille asunnoille eli asuntokunnille.
1-2 = Omistusasunnot
3-5 = Vuokra-asunnot
6 = Muut
9 = Tuntematon hallintaperuste. Tässä luokassa koko asuntokannan osalta tyhjät asunnot arava-asuntoja lukuunottamatta.

1998- 
1 = Omistaa talon 
2 = Omistaa asunnon osakkeet 
3 = Aravavuokra-asunto 
4 = Korkotukivuokra-asunto 
5 = Muu vuokra-asunto 
6 = Asumisoikeusasunnot 
7 = Muu hallintaperuste (sukulaisuus ym.) 
9 = Tuntematon 

1987-1997 
1 = Omistaa talon 
2 = Omistaa osakkeet 
5 = Vuokra-asunto 
7 = Muu hallintaperuste 
9 = Hallintaperuste tuntematon 

Tieto vuosittain (aineiston viimeinen vuosi - 1) -vuoteen asti.

#### `hulu` — Huoneluku keittiö pl.

**Group:** Asuminen

Asunnon huoneiden lukumäärä ilman keittiötä.

#### `taty` — Talotyyppi

**Group:** Rakennus

Talotyyppi. 
1 = Erillinen pientalo 
2 = Rivi- tai ketjutalo 
3 = Asuinkerrostalo 
4 = Muu rakennus (liike-, toimisto- ym.)
5 = Rakennus, jonka talotyyppi on tuntematon

#### `vata` — Varustetaso

**Group:** Asuminen

Asunnon varustelutason luokitus: 
1 = hyvin varustettu  
2 = puutteellisesti varustettu
3 = erittäin puutteellisesti varustettu (vuoteen 2015 saakka)
0 = varustetaso tuntematon

Varustetasoluokat 2, 3 sekä tuntematon tieto kannattaa yhdistää, sillä eri vuosina on ollut erilaisia päättelysääntöjä tuntemattomaksi jäävien osalta. Kannattaa myös huomioida, että kaikki varustemuutokset eivät ole luvanvaraisia toimenpiteitä eivätkä näin ollen tule viranomisten tietoon eivätkä rekistereihin ja tilastoihin.

#### `penulaika` — Perheen nuorimman lapsen ikä

**Group:** Perhe

Perheen lapsiksi katsotaan iästä riippumatta vanhempiensa kanssa asuvat omat tai puolison biologiset lapset tai ottolapset, mutta ei kasvattilapsia tai huollettavia lapsia. Tietoja (aineiston viimeinen vuosi -1) -vuoteen asti.

#### `peas` — Perheasema

**Group:** Perhe

Perheasema luokitus:
1 = Päämies 
2 = Puoliso 
3 = Lapsi 
4 = Avoperheen päämies 
5 = Avoperheen puoliso 
9 = Tuntematon 
0 = Perheeseen kuulumaton 

Lapseksi katsotaan iästä riippumatta vanhempiensa kanssa asuvat omat tai puolison biologiset lapset tai ottolapset, mutta ei kasvattilapsia tai huollettavia lapsia. Tietoja (aineiston viimeinen vuosi -1) -vuoteen asti.

#### `lkm_k` — Perheen lasten lkm

**Group:** Perhe

Perheen lasten lukumäärä, kaikki kotona asuvat lapset, biologiset ja ottolapset. 
0 = perheessä ei lapsia 
1 = perheessä 1 lapsi, 
2 = perheessä 2 lasta, jne 
7 = perheessä vähintään 7 lasta 
bl = ei kuulu perheväestöön

Tietoja (aineiston viimeinen vuosi -1) -vuoteen asti.

#### `a18lkm_k` — Perheen alle 18 v. lasten lukumäärä

**Group:** Perhe

Perheen alle 18 v. lasten lukumäärä 
0 = perheessä ei alle 18-vuotiaita lapsia 
1 = perheessä 1 alle 18-vuotias 
2 = perheessä 2 alle 18-vuotiasta,
3 = perheessä 3 alle 18-vuotiasta,
4 = perheessä 4 alle 18-vuotiasta,
5 = perheessä vähintään 5 alle 18-vuotiaita 
bl = ei kuulu perheväestöön

Tietoja (aineiston viimeinen vuosi -1) -vuoteen asti.

#### `a7lkm_k` — Perheen alle 7 v. lasten lukumäärä

**Group:** Perhe

Perheen alle 7 v. lasten lukumäärä 
0 = perheessä ei alle 7-vuotiaita lapsia 
1 = perheessä 1 alle 7-vuotias 
2 = perheessä 2 alle 7-vuotiasta 
3 = perheessä vähintään 3 alle 7-vuotiasta
bl = ei kuulu perheväestöön 

Tietoja (aineiston viimeinen vuosi -1) -vuoteen asti.

#### `a3lkm_k` — Perheen alle 3 v. lasten lkm

**Group:** Perhe

Perheen alle 3 v. lasten lkm 
0 = perheessä ei alle 3-vuotiaita lapsia 
1 = perheessä 1 alle 3-vuotias 
2 = perheessä vähintään 2 alle 3-vuotiasta 
bl = ei kuulu perheväestöön 

Tieto vuodesta 2006 lähtien. Tietoja (aineiston viimeinen vuosi -1) -vuoteen asti.

#### `pekoko_k` — Perheen koko

**Group:** Perhe

Perheen henkilöluku. Arvoalue 2-9 (9 = henkilöitä perheessä 9 tai enemmän). Muuttujan arvo on puuttuva henkilöillä, jotka eivät kuulu perheväestöön (ks. perheen määritelmä: http://www.stat.fi/meta/kas/perhe.html). 

Tietoja (aineiston viimeinen vuosi -1) -vuoteen asti.

#### `pety` — Perhetyyppi

**Group:** Perhe

Perhetyyppi perheväestöön kuuluvalla
1 = aviopari ilman lapsia 
2 = aviopari ja lapsia 
3 = äiti ja lapsia 
4 = isä ja lapsia 
5 = avopari ja yhteisiä lapsia 
6 = avopari ja vain ei-yhteisiä lapsia 
7 = avopari ilman lapsia

Tarkempi kuvaus perheen määritelmästä: http://www.stat.fi/meta/kas/perhe.html. Tietoja (aineiston viimeinen vuosi -1) -vuoteen asti.

#### `vela` — Vanhuuseläke

**Group:** Eläke

Arvo 1 = Henkilö saa vuoden lopussa vanhuuseläkettä. Tietoja vuodesta 1988 lähtien (aineiston viimeinen vuosi -2) -vuoteen asti.

#### `tkela` — Työkyvyttömyyseläke

**Group:** Eläke

Arvo 1 = Henkilö saa vuoden lopussa työkyvyttömyyseläkettä. Tietoja vuodesta 1988 lähtien (aineiston viimeinen vuosi -2) -vuoteen asti.

#### `tyela` — Työttömyyseläke

**Group:** Eläke

Arvo 1 = Henkilö saa vuoden lopussa työttömyyseläkettä. Tietoja vuosilta 1988-2014.

#### `mela` — Maatalouden erityiseläke

**Group:** Eläke

Arvo 1 = Henkilö saa maatalouden erityiseläkettä vuoden lopussa. Tietoja vuodesta 1995 lähtien (aineiston viimeinen vuosi -2) -vuoteen asti.

#### `osela` — Osa-aikaeläke

**Group:** Eläke

Arvo 1 = Henkilö saa vuoden lopussa osa-aikaeläkettä. Tietoja (aineiston viimeinen vuosi -2) -vuoteen asti.

#### `pela` — Perhe-eläke

**Group:** Eläke

Arvo 1 = Henkilö saa vuoden lopussa perhe-eläkettä. Tietoja vuodesta 1996 lähtien (aineiston viimeinen vuosi -2) -vuoteen asti.

#### `yvela` — Yksilöllinen varhaiseläke

**Group:** Eläke

Arvo 1 = Henkilö saa yksilöllistä varhaiseläkettä vuoden lopussa. Tieto vuosilta 1988-2011.

#### `kturaha_k` — Käytettävissä olevat rahatulot

**Group:** Tulonjakotilasto

Tulonjakotilaston muodostama käytettävissä oleva rahatulo muodostuu bruttotuloista (palkkatulojen, yrittäjätulojen, omaisuustulojen ja saatujen tulonsiirtojen summa), joista on vähennetty maksetut tulonsiirrot (maksetut verot ja veronluonteiset maksut). Tulonjaon kokonaistilaston päätulokäsite.

Arvot pyöristetty sadoiksi euroiksi, negatiiviset arvot nollattu, vuosittainen ylin persentiili mediaanina. Tietoja vuodesta 1995 lähtien vuosittain (aineiston viimeinen vuosi - 1) -vuoteen asti.

#### `velaty_k` — Velat yhteensä

**Group:** Henkilöverotusaineisto

Velat yhteensä koostuu seuraavista verotiedoista: 
NLIIKK= Elinkeinotoiminnan velat (vuoteen 1994 saakka)
NLIIKKY= Elinkeinotoiminnan velat yhteensä (vuosina 1995-2006 ja vuodesta 2014 alkaen)
NMAAT= Maatalouteen kohdistuneet velat
NYHT= Velat yhtymistä (vuoteen 2005 saakka)
NMUUT= Asunto- ja muut velat

Arvot pyöristetty sadoiksi euroiksi, vuosittainen ylin persentiili mediaanina. Tieto vuosittain (aineiston viimeinen vuosi - 1) -vuoteen asti.

#### `lvar_k` — Verotettava varallisuus

**Group:** Henkilöverotusaineisto

Verotettavan varallisuuden arvot pyöristetty sadoiksi euroiksi, vuosittainen ylin persentiili mediaanina. Tietoja vuoteen 2005 saakka.

#### `svatva_k` — Ansiotulot yhteensä valtion verotuksessa

**Group:** Henkilöverotusaineisto

Ansiotulot yhteensä valtionverotuksessa. Arvot pyöristetty sadoiksi euroiksi, vuosittainen  ylin persentiili mediaanina. Tietoja vuodesta 1993 lähtien vuosittain (aineiston viimeinen vuosi - 1) -vuoteen asti.

#### `palk_k` — Palkkatulot

**Group:** Tulonjakotilasto

Tulonjakotilaston palkkatulot-muuttuja. Sisältää rahapalkkaeriä, työsuhteeseen perustuvien kustannusten korvauksia ja luontoisedut. Muuttuja muodostuu vuosittain päivitettävän tulonjakotilaston tulonimikkeistön pohjalta.

Arvot pyöristetty sadoiksi euroiksi, negatiiviset arvot nollattu, vuosittainen ylin persentiili mediaanina. Tietoja vuodesta 1995 lähtien vuosittain (aineiston viimeinen vuosi - 1) -vuoteen asti.

#### `tyotu_k` — Summatut työtulot (palkkatulot)

**Group:** Henkilöverotusaineisto

Summatut työtulot (palkkatulot) sisältää seuraavia verotietoja vuoteen 2018 asti:
TRPL = rahapalkka päätoimesta, luontaisedut ja työsuhdeoptiot
TMPT = muut palkkatulot sivutoimesta
TEPALK = ennakonkannon alaiset palkkatulot veroilmoitukselta (vuodesta 1990 lähtien)
TMERI = veronalainen merityötulo (vuosina 2005-2007)
TMERI1 = matkustaja-alusten maksuvapauden piiriin kuuluva merityötulo (vuoteen 2007 asti)
TKUST = kustannusten korvaukset työnantajalta
TPALV = lunastukset, palvelurahat yms. ennakonkannon alaiset tulot
TPJTA = hankintatyön arvo metsätaloudesta
TYHTHAV = hankintatyön arvo yhtymästä
TPTURVA = palkkaturva ja sijaismaksajan maksama palkka ansiotulona (vuodesta 1993 lähtien)
TELPS = työkorvaus (vuodesta 1993 lähtien)
TELPS3 = urheilijarahastosta maksettava palkka (vuodesta 1999 lähtien)
TLUE2 = luontaisedut merityötulosta (vuodesta 1993 lähtien)
TLUE3 = luontaisedut merityötulosta (vuosina 2005-2007)
TUTMP2 = ulkomaisen työnantajan maksama palkka työntekijälle, joka ei Suomessa vakuutettu (vuodesta 2009 lähtien)
TUTMP3 = ulkomaisen työnantajan maksama palkka Suomessa vakuutetulle työntekijälle (vuodesta 2009 lähtien)
TOSINKTK= työpanokseen perustuva osinko, työkorvausta (vuodesta 2010 lähtien)

Arvot on pyöristetty sadoiksi euroiksi, vuosittainen ylin persentiili mediaanina. Vuoden 2018 jälkeiset tiedot henkilön palkkatuloista ovat saatavilla muuttujasta palk_k.

#### `tyrtuo_k` — Yrittäjätulot

**Group:** Henkilöverotusaineisto

Yrittäjätulot sisältävät maatalouden tulot, elinkeinotoiminnan tulot ja tulot yhtymästä. Elinkeinotoiminnan tulot eivät sisällä puolison elinkeinotuloja.

Yrittäjätulot sisältävät seuraavia verotietoja:
TMAAT1 = maatalouden ansiotulo, oma
TMAAT2 = maatalouden pääomatulo, oma
TLIIK1 = elinkeinotoiminnan ansiotulo-osuus, oma
TPORO1 = ansiotulo porotaloudesta
TLIIK2 = elinkeinotoiminnan pääomatulo-osuus, oma
TPORO2 = pääomatulo porotaloudesta
TYHTAT = ansiotulot ilman osinkoja yhtymästä (vuodesta 1993 lähtien)
TEINOYVA = osingot ansiotulona muista kuin listatuista yhtiöistä, verotettava määrä yhtymistä (vuodesta 2005 lähtien)
TYHAU = ansiotulo-osuus ulkomaisen yhtymän tulosta (vuosina 1996-2011)
TYHTPOT = pääomatulot ilman osinkoja yhtymistä (vuodesta 1993 lähtien)
TEINOYVP = osingot pääomatulona muista kuin listatuista yhtiöistä, veronalainen määrä yhtymistä (vuosina 2005-2013)
TNOSYHV = osingot pääomatulona listatuista yhtiöistä, verotettava määrä yhtymistä (vuodesta 2005 lähtien)
TYHAP = pääomatulo-osuus ulkomaisen yhtymän tulosta (vuodesta 1996 lähtien)
TOPYKOK = osuuspääoman korot yhtymistä, yhteismäärä (vuosina 2005-2014)

Arvot pyöristetty sadoiksi euroiksi, vuosittainen ylin persentiili mediaanina. Tieto vuosittain (aineiston viimeinen vuosi - 1) -vuoteen asti.

#### `auto_k` — Henkilön omistama/hallitsema ajoneuvo

1 = on auton omistaja/haltija. Tietoja vuodesta 1990 lähtien vuoteen 2018 asti.

---

[← Back to catalogue](../../README.md)
