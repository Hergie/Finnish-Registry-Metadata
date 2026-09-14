# EDUC_OPISK_KARK Opiskelijat, v. 1999–2024

- **Identifier:** `EDUC_19992024_jua_opiskk_001.xml`
- **DOI:** `aop_2026-09_2026-09-08_ain_0005`
- **Temporal coverage:** —
- **Published:** 2026-09-08
- **Organisation:** Tilastokeskus
- **Variable count:** 86
- **Observation count:** —
- **Population:** Tutkintoon johtavan koulutuksen opiskelijat Suomessa
- **Source:** Tilastokeskuksen ikätilastoa varten keräämät henkilöpohjaiset tiedot, Tilastokeskuksen opiskelijat ja tutkinnot -tilasto.

## Description

EDUC_OPISK_KARK-valmisaineisto sisältää tietoja muun muassa henkilöiden demografisista taustatekijöistä, oppilaitoksista, koulutus- ja opiskelumuodoista, suoritetuista opintoviikoista ja -pisteistä sekä koulutuslajeista.

Tämä aineistokuvaus koskee vuosien 1999–2024 vuositiedostoja. EDUC_OPISK_KARK-aineistosta on erilliset kuvaukset edeltävien vuosien vuositiedostoille 1995, 1996, 1997 ja 1998. 

<b> Valmisaineiston tarkentava nimi </b> 
Opiskelijoiden tiedot lukiokoulutuksessa, ammatillisessa koulutuksessa, oppisopimuskoulutuksessa ja ammattikorkeakoulu- ja yliopistokoulutuksessa kirjoilla olleista, sisältäen kansalaisuus-, kieli- ja opintotietoja.

<b> Aineiston perusjoukko, koostaminen ja tietolähteet </b> 
Aineisto sisältää tiedot opiskelijoista, jotka ovat olleet 20.9. kirjoilla tutkintoon johtavassa koulutuksessa seuraavilla koulutussektoreilla: lukiokoulutus, ammattikorkeakoulukoulutus ja yliopistokoulutus. Lisäksi moduuli kattaa kalenterivuoden aikana ammatillisessa koulutuksessa kirjoilla olleet tai oppisopimuskoulutukseen osallistuneet opiskelijat.

<u>Laajennukset vuodesta 2013 alkaen: </u>
- Mukana ovat myös ammattikorkeakoulujen tutkintoon johtamattoman koulutuksen opiskelijat (muuttuja oplu= 1). Ammattikorkeakouluaineistossa ovat mukana myös alkuvuonna opintonsa aloittaneet, jotka eivät ole ilmoittautuneet 20.9. mennessä (esimerkiksi koulutuksen keskeyttäneet tai tutkinnon suorittaneet, oplu= 1). 
- Vuodesta 2013 alkaen ammatillisen koulutuksen opiskelijatiedot kattavat koko kalenterivuoden, eivät vain syksyn tilanteen.

<u>Laajennukset vuodesta 2015/2016 alkaen: </u>
Mukaan on otettu myös yliopistojen tutkintoon johtamattomassa koulutuksessa opiskelevat, jotka tunnistetaan tarkemmin muuttujan klaji avulla.
 
Aineiston opiskelutiedot ovat melko yhdenmukaisia vuodesta 1999 alkaen. Sen sijaan vuosien 1995–1998 tiedot ovat sisällöltään selvästi suppeampia.

<b> Huomioitavaa aineistosta ja sen käytöstä </b> 
- Kaikki lukio- ja ammatillinen koulutus on tutkintoon johtavaa koulutusta. Ammattikorkeakoulu- ja yliopistokoulutuksessa tutkintoon johtava koulutus saadaan rajaamalla pois tutkintoon johtamaton koulutus (oplu=1).
- Jaottelu lukiokoulutukseen, ammatilliseen koulutukseen, ammattikorkeakoulukoulutukseen ja yliopistokoulutukseen saadaan muuttujien ain tai klaji avulla.
- Mikäli halutaan kukin henkilö mukaan vain kerran ensisijaisen koulutuksen perusteella, käytetään muuttujaa oprior.
          - Koulutuksessa läsnä olevat opiskelijat saadaan poimittua valitsemalla olosyys = 1 (tai olotamm = 1).
          - Lukio-, ammattikorkeakoulu- ja yliopistokoulutuksessa muuttuja olotamm ei sisällä kaikkia keväällä opiskelleita, vaan ainoastaan ne opiskelijat, jotka jatkoivat opintojaan syksyllä 20.9. 
          - Ammatillisessa koulutuksessa olotamm=1 sisältää opiskelijat, jotka ovat olleet kirjoilla oppilaitoksessa 20.1. sekä ne, jotka ovat osallistuneet oppisopimuskoulutukseen kalenterivuoden aikana. Vuonna 2018 tähän määritelmään tehtiin muutos. Aiemmin ammatillisessa koulutuksessa olotamm=1 sisälsi opetussuunnitelmaperusteisen koulutuksen opiskelijat, jotka olivat kirjoilla oppilaitoksessa 20.1. sekä oppilaitosmuotoisessa näyttötutkintoon valmistavassa koulutuksessa ja oppisopimuskoulutuksessa kalenterivuoden aikana opiskelleet.
- Mikäli tiedot halutaan koulutuksittain, käytetään yleensä koulutusluokituksen (standardiluokitus) 6-numeroista koulutuskoodia koulk, joka toimii avaimena eri koulutusluokituksiin. Tarkennuksia saa tutkinto-, koulutusohjelma- ja suuntautumisvaihtoehtojen nimikkeistä, mutta ne voivat olla epävirallisia.
- Uudet opiskelijat poimitaan muuttujan alvv avulla (alvv=vuosi).
- Lukiokoulutuksen tiedot eivät sisällä aineopiskelijoita. Julkaistuissa lukiotilastoissa aineopiskelijat ovat kuitenkin mukana vuoteen 1998 asti.
- Vuosina 1999–2003 ammatillisen koulutuksen näyttötutkintoon valmistavan koulutuksen ja oppisopimuskoulutuksen tiedot perustuvat poikkileikkausajankohtaan 20.9., mikä tekee tiedoista koulutuksen luonteen huomioon ottaen alipeittäviä. Vuosien 1995–1998 aineisto ei sisällä näiden koulutusmuotojen opiskelijoita lainkaan.
- Ammattikorkeakoulukoulutuksen tiedot sisältävät sekä vakinaisten ja väliaikaisten ammattikorkeakoulujen opiskelijat. Viimeiset väliaikaiset ammattikorkeakoulut olivat toiminnassa vuoteen 2002 asti.
- Yliopistokoulutuksen tiedot ovat vuosina 1995–2001 ajankohdalta 31.12. ja vuodesta 2002 alkaen ne perustuvat 20.9. tilanteeseen.
- Aineisto ei sisällä Maanpuolustuskorkeakoulun koulutuksia ennen vuotta 2010.
- Vuodesta 1999 alkaen mukana ovat opiskelijat, joilla on joko oikea tai puutteellinen henkilötunnus. Vuosina 1996–1998 yliopistokoulutuksen osalta mukana ovat molemmat ryhmät, mutta muilta koulutussektoreilta vain opiskelijat, joilla on oikea henkilötunnus. Vuoden 1995 tiedoissa ovat mukana ainoastaan ne opiskelijat, joilla on oikea henkilötunnus.
- Tilastovuodesta 2020 alkaen tiedosto on muodostettu yhdistämällä lukiokoulutuksen, ammatillisen koulutuksen, ammattikorkeakoulukoulutuksen ja yliopistokoulutuksen henkilöpohjaiset tiedostot. Nämä perustuvat opetuksen ja koulutuksen järjestäjien (oppilaitosten Opetushallituksen KOSKI-tietovarantoon tai Korkeakoulujen valtakunnalliseen tietovarantoon (VIRTA) ilmoittamiin tietoihin. Lisäksi on hyödynnetty näitä tietovarantoja täydentäviä tiedonkeruita.
- Vuoteen 2019 asti tiedosto muodostettiin yhdistämällä lukiokoulutuksen, ammatillisen koulutuksen, ammattikorkeakoulukoulutuksen ja yliopistokoulutuksen henkilöpohjaiset tiedostot, jotka perustuvat Tilastokeskuksen oppilaitoksilta keräämin tietoihin. Päivälukioiden, ammatillisten oppilaitosten ja väliaikaisten ammattikorkeakoulujen opiskelijatiedot vuosilta 1996–1998 perustuivat vuosittain pääteltyihin tietoihin. Vuoden 1995 osalta ammatillisten oppilaitosten ja väliaikaisten ammattikorkeakoulujen tiedot perustuivat Tilastokeskuksen keräämiin henkilöpohjaisiin tietoihin, joihin lisättiin vuosina 1996, 1997 ja 1998 yhteishaussa tai sen ulkopuolella aloittaneet opiskelijat, ja joista poistettiin vuosina 1995, 1996, 1997 sekä tammi–syyskuussa 1998 tutkinnon suorittaneet. Päivälukioiden vuoden 1995 tiedot perustuivat opetushallinnon valtionosuusjärjestelmän henkilöpohjaisiin tietoihin, joita täydennettiin vastaavalla tavalla: lisättiin vuosina 1996–1998 aloittaneet ja poistettiin ylioppilastutkinnon suorittaneet.

Aineistosta on erikseen saatavilla myös arkaluonteisia erityisopetukseen liittyviä muuttujia. Näihin myönnetään käyttöoikeus vain, jos tutkimuksellinen tarve on perusteltu ja erityinen.

<b> Tarkempaa tietoa luokituksista </b> 
- Luokitustiedot perustuvat tilastovuoteen, ellei toisin mainita.
- Tilastovuodesta 2016 alkaen Tilastokeskus on raportoinut koulutustiedot uuden Kansallisen koulutusluokituksen mukaisesti, joka vastaa kansainvälistä ISCED 2011 -luokitusta. 
- Puuttuvat tiedot on yleensä merkitty numerolla yhdeksän (9), ja kuntamuuttujissa koodi 200 viittaa ulkomaihin.

<u>Muutokset: </u>

2012:
- Muuttujien alvv ja allk sisältö muuttuivat yliopistokoulutuksessa siten, että nyt myös yliopistokoulutuksesta saadaan tieto siitä, milloin henkilö on aloittanut ensimmäistä kertaa kyseisen koulutuksen kyseisessä oppilaitoksessa. Aiemmin, vuoteen 2011 saakka yliopistokoulutuksen aloittamistiedot kuvasivat sitä ajankohtaa, jolloin opiskelija aloitti minkä tahansa koulutuksen kyseisessä oppilaitoksessa (ks. muuttuja kirtu). 
- Opinto-oikeuden alkamista kuvannut muuttujja opoik on poistettu.

2013
- Ennen vuotta 2013 opetussuunnitelmaperusteisen ammatillisen koulutuksen opiskelijatiedot olivat 20.9. tilanteesta, kun taas näyttötutkintoon valmistavan ja oppisopimuskoulutuksen opiskelijatiedot kattoivat koko vuoden.

2016:
- Tilastovuodesta 2016 alkaen Tilastokeskus on raportoinut koulutustiedot uuden Kansallisen koulutusluokituksen mukaisesti, joka vastaa Kansainvälistä ISCED 2011 -koulutusluokitusta.

2018:
- Uusi laki ammatillisesta koulutuksesta tuli voimaan 1.1.2018, minkä myötä koulutusta ei enää jaotella nuorille suunnattuun opetussuunnitelmaperusteiseen ja aikuisille suunnattuun näyttötutkintoon valmistavaan koulutukseen. 
	- Uudistuksen myötä aineistosta on poistetu muuttujat tutktav sekä yrit. 
	- Uudistus vaikutti myös muuttujiin kryh, klaji, oplu, tutalv, tutalk, olotamm, olosyys, rahoitus sekä tyov. 
- Lisäksi muuttujien rahlahde, lkmmt sekä avo määritelmät muuttuivat muista kuin ammatillisen koulutuksen uudistuksesta johtuvista syistä.

2019:
- Muuttujien klaji, tutalv, tutalk, purku, rahoitus, opjarj_s, opyrtunn_s sekä suorosat arvoissa, nimikkeissä, tietojen saatavuudessa ja peitossa tapahtui muutoksia.
- Aineistoon lisättiin useita muuttujia, kuten eril, kmuoto,  jarjestamiskoodi, s_henkiloOid, s_opiskeluOid, koulutussopimus_osuus, koulutussopimuspaivat, oppisopimusosuus, oppisopimuspaivat, oppilaitospaivat sekä s_tyan.
- Poistettu muuttujat tutnim(tutkintonimike) ja kounim (koulutusohjelmanimike). 
- Muuttujan tut koodisto on korvannut -tutnim-muuttujan.
- Muuttujan koukoodisto on korvannut kounim-muuttujan.

2020: 
- Poistettu muuttujat oppis (oppisopimuskoulutus), toteuma (kalenterivuoden toteuma), todis (opiskelija on saanut todistuksen koulutuksen suorittamisesta) sekä oppisopimusosuus (oppisopimuksen osuus kalenterivuoden päivistä).

2023:
- Aluemuuttujia askunx ja tilvaskunx ei enää päivitetä.
- Klaji-muuttujassa tapahtuneet muutokset:
	- arvo 52 sisältää eläinlääkäreiden erikoistumiskoulutuksen, mikäli se on aloitettu 31.7.2023 mennessä.
	- arvo 53 sisältää eläinlääkäreiden erikoistumiskoulutuksen, mikäli se on aloitettu 1.8.2023 tai sen jälkeen.
	ammattikorkeakoulujen erikoistumisopintoja ei enää ole. Klajin arvo 43 pidetään kuvauksessa.
	- Muuttujat kirtupv ja kirtu1pv sisältävät vuodesta 2023 alkaen yliopistokoulutuksen, kun aiemmin ne kattoivat vain amk-koulutuksen.
	- Kirtu-muuttuja koskee vain yliopistokoulutusta.
	- Muuttujan kokosa määrittelyssä käytettään nyt kirtuv-muuttujaa, joka kertoo kirjoille tulovuoden ensimmäistä kertaa kyseiseen yliopistoon. Vuoteen 2022 asti käytössä oli alvv-muuttuja, joka kuvasi aloitusvuotta kyseisessä koulutuksessa kyseisessä yliopistossa, ja tieto perustui tuolloin opoik-muuttujaan.

<b> Aineiston päivitysaikataulu </b>  
Tutustu valmisaineistojen <a href="https://stat.fi/fi/palvelut/palvelut-tutkijoille/tutkimusaineistot/valmisaineistot/valmisaineistojen-paivitysaikataulu">  päivitysaikatauluun</a>. 

<b> Aineiston käyttö ja tilaaminen </b> 
EDUC_OPISK_KARK-valmisaineisto on tarkoitettu käytettäväksi FIONA-etäpalvelun kautta, ja se on linkitettävissä muihin henkilövalmisaineistoihin suojatun henkilönumeron avulla. 

Mikäli tutkimushankkeen tarve kohdistuu tarkkoihin kansalaisuus- ja äidinkielitietoihin, voi se hakea käyttöönsä EDUC_OPISK-valmisaineistoa, joka sisältää muuten samat muuttujat, mutta kansalaisuus- ja äidinkielitiedot ovat tarkalla tasolla. EDUC_OPISK-aineiston käyttöön saaminen edellyttää vahvoja tutkimuksellisia perusteita.
Valmisaineiston voi tilata tutkimuksen kohdejoukolle ja tarvittavalta ajanjaksolta. Kokonaisaineiston (kaikki muuttujat koko populaatiosta ja kaikilta saatavilla olevilta vuosilta) käyttöoikeus myönnetään vain, jos tutkimuksellinen tarve sitä erityisesti edellyttää. Lisäksi aineistosta voi tilata räätälöidyn version, joka sisältää vain osan muuttujista. 
Aineisto on FIONA-etäkäyttöjärjestelmässä jaettuina vuosikansioihin tilastovuosittain.

<b> Lisätietoja </b> 
Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@stat.fi

## Variables (86)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `vuosiluokka` | Vuosiluokka | — | — | c koulutusta tai tavoitetutkintoa kuvaavat tiedot |
| `ykunta` | Koulutuksen järjestäjän sijaintikunnan koodi | — | — | c koulutusta tai tavoitetutkintoa kuvaavat tiedot |
| `tyan_s` | Suojattu työnantajan/yrityksen yritystunnus | — | — | — |
| `oppilaitospaivat` | Oppilaitoksessa opiskelu | lkm | — | — |
| `oppisopimuspaivat` | Oppisopimuksen päivät/vuosi | lkm | — | — |
| `oppisopimusosuus` | Oppisopimuksen osuus kalenterivuoden päivistä | lkm | — | — |
| `koulutussopimuspaivat` | Koulutussopimuksen päivät/vuosi | lkm | — | — |
| `koulutussopimus_osuus` | Koulutussopimuksen osuus kalenterivuoden päivistä | lkm | — | — |
| `opiskeluOid_s` | Suojattu opiskeluoikeuden tunnistenumero (KOSKI-tietovaranto) | — | — | — |
| `henkiloOid_s` | Suojattu henkilön tunnistenumero (KOSKI-tietovaranto) | — | — | — |
| `jarjestamiskoodi` | Järjestämismuoto (vanhat perusteet) | — | — | — |
| `kmuoto` | Koulutusmuoto | — | — | — |
| `eril` | Erillisaineistoon (täydennystiedonkeruut) kuuluva havainto | — | — | — |
| `kirtu` | Ensimmäinen kirjoilletulo ko. yliopistoon mihin tahansa koulutukseen | — | — | — |
| `lkmmt` | Lukukausimaksukokeilu ja maksullinen tilauskoulutus (yliopistokoul.) | — | lkmmt_1_2016_01_01 | — |
| `tutas` | Tutkintoasetus (yliopistokoulutus) | — | — | — |
| `om` | Opiskelumuoto (yliopistokoulutus) | — | opiskelu_3_2016_01_01 | — |
| `opkelp` | Opettajankelpoisuus (yliopistokoulutus) | — | opiskelu_4_2016_01_01 | — |
| `avo` | Hyväksytty avoimen yliopiston opintojen perusteella (yliopistokoulutus) | — | opiskelija_2_2016_01_01 | — |
| `tuotanto` | Tuotantopainotteinen koulutus (ammattikorkeakoulukoulutus) | — | — | — |
| `tdk` | Tiedekunta/osasto (yliopistokoulutus) | — | — | — |
| `fuksi` | Uusi yliopisto-opiskelija | — | opiskelija_3_2016_01_01 | E4 Yliopistokoulutus, E Lähdeaineistojen omat muuttujat |
| `ltopo` | Pätevyyteen tähtäävät opinnot | — | opiskelu_5_2016_01_01 | — |
| `tilmaa` | Maksullisen tilauskoulutuksen sijaintimaa (ammattikorkeakoulukoulutus) | — | valtio_1_2012_01_01 | — |
| `rahlahde` | Opiskelijan rahoitustausta (ammattikorkeakoulukoulutus) | — | opiskelija_4_2018_01_01 | — |
| `kirtupv` | Ko. tutkintoon kirjoihintuloajankohta ko. ammattikorkeakoulussa (ammattikorkeakoulukoulutus) | — | — | — |
| `kirtu1pv` | Ensimmäinen kirjoihintuloajankohta ko. tutkintoon (ammattikorkeakoulukoulutus 2005-) | — | — | — |
| `oplaaj` | Suoritettavien opintojen laajuus (ammattikorkeakoulukoulutus) | — | — | — |
| `poissalk` | Poissaololukukaudet (ammattikorkeakoulukoulutus) | — | — | — |
| `lasnalk` | Läsnäololukukaudet (ammattikorkeakoulukoulutus) | — | — | — |
| `opjarj_s` | Suojattu oppisopimuskoulutuksen järjestäjän nro (oppisopimuskoulutus) | — | — | — |
| `opyrtunn_s` | Suojattu työnantajan/yrityksen yritystunnus (oppisopimuskoulutus) | — | — | — |
| `yrit` | Yrittäjän oppisopimuskoulutus (ammatillinen oppisopimuskoulutus) | — | oppisopimus_2_2016_01_01 | — |
| `todis` | Opiskelija on saanut todistuksen koulutuksen suorittamisesta (ammatillinen oppisopimuskoulutus) | — | oppisopimus_3_2016_01_01 | — |
| `purku` | Oppisopimus purkautunut (ammatillinen oppisopimuskoulutus) | — | oppisopimus_4_2016_01_01 | — |
| `toteuma` | Kalenterivuoden toteuma (ammatillinen oppisopimuskoulutus) | — | oppisopimus_5_2016_01_01 | — |
| `rahoitus` | Koulutuksen rahoitus (ammatillinen näyttötutkintoon valmistava oppilaitosmuotoinen koulutus) | — | ammatillinen_2_2018_01_01 | — |
| `aloit` | Aloittanut koulutuksen tai solminut oppisopimuksen kalenterivuonna | — | — | — |
| `suorosat` | Suoritettujen tutkinnon osien lukumäärä | — | — | — |
| `loaika` | Oppisopimuskoulutuksen tai tietyssä oppilaitoksessa tapahtuvan koulutuksen päättymispäivämäärä | — | — | — |
| `alaika` | Koulutuksen aloituspäivämäärä | — | — | — |
| `tavoite` | Opiskelijan tavoite koulutuksessa (ammatillinen koulutus) | — | ammatillinen_4_2004_01_01 | — |
| `ophal` | Opetushallinnon alainen koulutus | — | — | — |
| `tyov` | Työvoimakoulutus | — | ammatillinen_3_2001_01_01 | — |
| `oppis` | Oppisopimuskoulutus (ammatillinen koulutus 1999-) | — | oppisopimus_1_2014_01_01 | — |
| `noste` | Koulutuksen kuuluminen Noste-ohjelmaan | — | — | — |
| `tutktav` | Opetussuunnitelmaperusteinen/näyttötutkintoon valmistava koulutus | — | ammatillinen_1_2000_01_01 | — |
| `tutklaja` | Ammatillisen koulutuksen koulutuslaji | — | koullaji_2_2014_01_01 | — |
| `jarj_s` | Suojattu koulutuksen järjestäjä/ylläpitäjä | — | — | — |
| `oltunn_s` | Suojattu oppilaitostunnus | — | — | — |
| `kkun` | Koulutuksen sijaintikunta | — | kunta_1_2019_01_01 | — |
| `kkieli` | Koulutuksen opetuskieli (1999-) | — | kieli_1_2010_11_15 | — |
| `aikoul` | Nuorten/aikuisten koulutus | — | koulutus_15_2016_01_01 | — |
| `suv` | Suuntautumisvaihtoehtonimikekoodi | — | — | — |
| `kou` | Koulutusohjelma-/pääainenimikekoodi | — | — | — |
| `tut` | Tutkintonimikekoodi/opintojen tarkoitus | — | — | — |
| `koulk` | Tilastokeskuksen koulutuskoodi | — | koulutus_18_2018_01_01 | — |
| `tutalk` | Lukukausi, jolloin opiskelija on aloittanut ko.koulutuksen/tutkinnon missä tahansa oppilaitoksessa | — | opiskelu_7_2011_01_01 | — |
| `tutalv` | Vuosi, jolloin opiskelija on aloittanut ko. koulutuksen/tutkinnon missä tahansa oppilaitoksessa | — | — | — |
| `ovker` | Edeltävän kevätlukukauden loppuun mennessä suoritetut opintoviikot | — | — | — |
| `ovek` | Edeltävällä kevätlukukaudella suoritetut opintoviikot | — | — | — |
| `oves` | Edeltävällä syyslukukaudella suoritetut opintoviikot | — | — | — |
| `opker` | Edeltävän kevätlukukauden loppuun mennessä suoritetut opintopisteet | — | — | — |
| `opek` | Edeltävällä kevätlukukaudella suoritetut opintopisteet | — | — | — |
| `opes` | Edeltävällä syyslukukaudella suoritetut opintopisteet | — | — | — |
| `fte` | Full-time equivalent (FTE) -luku (yliopisto- ja ammattikorkeakoulukoulutus 2006-) | — | — | — |
| `kokosa` | Kokopäivä-/osa-aikaopiskelija (yliopisto- ja ammattikorkeakoulukoulutus 2002-) | — | opiskelija_1_2014_01_01 | — |
| `tilvaskunx` | Kotikunta edellisen vuoden lopussa ko. tilastovuoden luokituksin | — | kunta_1_2018_01_01 | — |
| `tilvaskun` | Kotikunta / vakituinen asuinkunta tilastovuoden luokituksin | — | kunta_1_2018_01_01 | — |
| `askunx` | Kotikunta / vakituinen asuinkunta edellisen vuoden lopussa | — | kunta_1_2018_01_01 | — |
| `askun` | Opiskelijan kotikunta | — | kunta_1_2019_01_01 | — |
| `aiopis` | Aikuisopiskelija | — | opiskelija_5_2013_01_01 | B Opiskelijaa tai opiskelua kuvaavat tiedot |
| `allk` | Tutkinnon aloittamislukukausi/kirjoilletulolukukausi (1997-) | — | opiskelu_6_2013_01_01 | — |
| `alvv` | Tutkinnon aloittamisvuosi/kirjoilletulovuosi (1997-) | — | — | — |
| `olotamm` | Kirjoilla 20.1. (1999-) | — | kirjoilla_4_2016_01_01 | — |
| `olosyys` | Kirjoilla 20.9 (1999-) | — | kirjoilla_3_2018_01_01 | — |
| `aikieli` | Äidinkieli (1999-) | — | kieli_1_2010_11_15 | — |
| `kansal` | Kansalaisuus (1999-) | — | valtio_1_2012_01_01 | — |
| `ika` | Ikä tilastovuoden lopussa | — | — | — |
| `sp` | Sukupuoli | — | sukupuoli_2_1970_01_01 | — |
| `oplu` | Opiskelun luonne | — | oplu_3_2018_01_01 | — |
| `oprior` | Opiskelun prioriteetti (1997-) | — | opiskelu_1_2014_01_01 | — |
| `klaji` | Koulutuslaji (1999-) | — | — | — |
| `ain` | Lähdeaineisto | — | lahdeaineisto_1_2014_01_01 | — |
| `hid_e` | Suojattu henkilön yksilöivä tunniste | — | — | — |
| `vuosi` | Aineistovuosi | — | — | — |

### Variable definitions

#### `vuosiluokka` — Vuosiluokka

**Group:** c koulutusta tai tavoitetutkintoa kuvaavat tiedot

Vuosiluokka

01=1. vuosiluokka	
02=2. vuosiluokka	
…	
09=9. vuosiluokka

#### `ykunta` — Koulutuksen järjestäjän sijaintikunnan koodi

**Group:** c koulutusta tai tavoitetutkintoa kuvaavat tiedot

Koulutuksen järjestäjän sijaintikunnan koodi. Tilastokeskuksen kuntaluokitusrekisteri

Varhaiskasvatuksen esiopetuksen tieto

#### `tyan_s` — Suojattu työnantajan/yrityksen yritystunnus

Muuttujan nimi on muuttunut vuonna 2019 ammatillisen koulutuksen reformin vuoksi. Oli aikaisemmin OPYRTUNN_S, nyt TYAN_S. Tieto KOSKI-tietovarannosta. Aiemmin vain oppisopimuskoulutuksessa. Tieto vuodesta 2019 alkaen.

#### `oppilaitospaivat` — Oppilaitoksessa opiskelu

**Unit:** lkm

Oppilaitoksessa opiskelu, muualla kuin oppisopimuksella tai koulutussopimuksella. Tieto vuodesta 2019 alkaen.

#### `oppisopimuspaivat` — Oppisopimuksen päivät/vuosi

**Unit:** lkm

Oppisopimuksen päivät/vuosi, ajanjaksoissa päällekkäisyyksiä, joten voi saada arvon yli 365. Tieto vuodesta 2019 alkaen.

#### `oppisopimusosuus` — Oppisopimuksen osuus kalenterivuoden päivistä

**Unit:** lkm

Oppisopimuksen osuus kalenterivuoden päivistä. Voi saada yli 100 %, koska jaksoissa päällekkäisyyksiä. Tieto vain vuodelta 2019.

#### `koulutussopimuspaivat` — Koulutussopimuksen päivät/vuosi

**Unit:** lkm

Koulutussopimuksen päivät/vuosi, ajanjaksoissa päällekkäisyyksiä, joten voi saada arvon yli 365. Numeerinen tieto. Tieto vuodesta 2019 alkaen.

#### `koulutussopimus_osuus` — Koulutussopimuksen osuus kalenterivuoden päivistä

**Unit:** lkm

Koulutussopimuksen osuus kalenterivuoden päivistä. Voi saada yli 100 % arvon, koska jaksoissa päällekkäisyyksiä. Numeerinen tieto.
Tieto vuodesta 2019 alkaen.

#### `opiskeluOid_s` — Suojattu opiskeluoikeuden tunnistenumero (KOSKI-tietovaranto)

Suojattu opiskeluoikeuden tunnistenumero KOSKI-tietovarannossa. Tieto vuodesta 2019 alkaen.

#### `henkiloOid_s` — Suojattu henkilön tunnistenumero (KOSKI-tietovaranto)

Suojattu henkilön tunnistenumero KOSKI-tietovarannossa.
Tieto vuodesta 2019 alkaen.

#### `jarjestamiskoodi` — Järjestämismuoto (vanhat perusteet)

Koulutuksen järjestämismuoto.
Ennen ammatillisen koulutuksen vuonna 2018 voimaan astunutta reformia koulutuksen järjestämismuodolla viitattiin koulutuksessa koulutuksen järjestämiseen oppilaitosmuotoisesti tai oppisopimusmuotoisesti.
10 = koulutuksen järjestäminen oppilaitosmuotoisena
20 = koulutuksen järjestäminen oppisopimuskoulutuksena.
Tietoa vuodesta 2019 alkaen.

#### `kmuoto` — Koulutusmuoto

Ammatillinen koulutus voi vuoden 2021 loppuun saakka olla opetussuunnitelmaperusteista koulutusta (ops) tai näyttötutkintoon valmistavaa koulutusta (naytto). Vuodesta 2018 lähtien koulutuksen voi suorittaa oppilaitosmuotoisena, koulutussopimuksena, oppisopimuksena ja/tai näiden yhdistelmänä (reformi).
1 = ops
2 = naytto
3 = reformi
Tieto vuodesta 2019 alkaen.

#### `eril` — Erillisaineistoon (täydennystiedonkeruut) kuuluva havainto

Ammatillisen koulutuksen tilastoinnissa käytetty aputieto, joka kertoo, onko tieto saatu nk. täydennystiedonkeruun kautta eikä KOSKI-tietovarannosta. Arvo 1 = Kyllä. Uusi muuttuja vuoden 2019 aineistossa.

#### `kirtu` — Ensimmäinen kirjoilletulo ko. yliopistoon mihin tahansa koulutukseen

Vuodesta 2023 alkaen Kirtu-muuttujassa on vain yliopistokoulutuksen arvoja.

vvvv = vuosi, lukukausi 1 = kevät ja kesä, 2 = syksy
00000 = ei tietoa
Tämä tieto oli vuoteen 2011 asti muuttujissa ALLV ja ALLK.
Tiedot alkaen vuodesta 2013. Tieto myös vuonna 1995 muuttujassa KIRTU eri muotoilulla.

#### `lkmmt` — Lukukausimaksukokeilu ja maksullinen tilauskoulutus (yliopistokoul.)

**Classification:** lkmmt_1_2016_01_01

Lukukausimaksukokeilu ja maksullinen tilauskoulutus (vain yliopistokoulutuksessa). Tiedot vuosilta 2010-2017. 
0 = Ei lukukausimaksukokeilua eikä maksullista tilauskoulutusta
1 = Lukukausimaksukokeilun mukainen maisteriohjelma
2 = Maksullinen tilauskoulutus
Vuodesta 2018 muuttuja on poistettu ja tiedot ovat muuttujassa RAHLAHDE. Tiedot on yhdenmukaistettu amk-sektorin kanssa.
Vastaavuudet entisen lkmmt-muuttujan ja rahlahde-muuttujan välillä:
lkmmt 1 =  rahlahde 5, lkmmt 2 = rahlahde 4, lkmmt tyhjä/0 = rahlahde 1.

#### `tutas` — Tutkintoasetus (yliopistokoulutus)

Vain yliopistokoulutus. Tieto vuosilta 2006-2009.
1 = Tutkinto suoritetaan uuden tutkintoasetuksen (794/2004) mukaan
2 = Tutkinto suoritetaan vanhojen tutkintoasetusten mukaan

#### `om` — Opiskelumuoto (yliopistokoulutus)

**Classification:** opiskelu_3_2016_01_01

Opiskelumuoto. Vain yliopistokoulutuksessa. 
0 = Tavallinen koulutusohjelma (2005-)
1 = Maisteriohjelma (2005-2009) / Asetuksen mukainen maisteriohjelma (2010-2013)
2 = Muu maisteriohjelma (2010-) 
Vuonna 2014 poistettu arvo 1 = Asetuksen mukainen maisteriohjelma

Tavallinen koulutusohjelma (OM = 0) tarkoittaa maisteriohjelmaa, johon edetään nykyjärjestelmässä kandin kautta (useimmilla aloilla tämä järjestely on ollut käytössä vuodesta 2005 alkaen).
Asetuksen mkainen maisteriohjelma (OM = 1) viittaa Opetus- ja kulttuuriministeriön asetukseen yliopistojen maisteriohjelmista 1048/2012. Näihin maisteriohjelmiin on ollut erillishaku.
Muu koulutusohjelma (OM = 2) viittaa myös koulutusohjelmiin, joihin on erillishaku.

#### `opkelp` — Opettajankelpoisuus (yliopistokoulutus)

**Classification:** opiskelu_4_2016_01_01

Opettajankelpoisuus. Vain yliopistokoulutuksessa.
0 = Ei ole opettajankelpoisuutta
1 = On opettajankelpoisuus. Tietoja vuodesta 2001 alkaen, paitsi 2004-2005.

#### `avo` — Hyväksytty avoimen yliopiston opintojen perusteella (yliopistokoulutus)

**Classification:** opiskelija_2_2016_01_01

Vain yliopistokoulutuksen uudet opiskelijat. Vuodesta 2018 poistettu tieto, että koskee vain uusia opiskelijoita. Arvo 1 voi olla kaikilla opiskelijoilla.
0 = Ei
1 = Kyllä
bl = Muu kuin yliopistokoulutus tai yliopistokoulutuksen muut kuin uudet opiskelijat. 
Tietoja vuodesta 2001 alkaen, puuttuen vuosilta 2004-2005.

#### `tuotanto` — Tuotantopainotteinen koulutus (ammattikorkeakoulukoulutus)

Tieto vain tekniikan alan koulutuksella ammattikorkeakoulukoulutuksessa
1 = Kyllä
2 = Ei
Tieto vuosilta 2005-2009.

#### `tdk` — Tiedekunta/osasto (yliopistokoulutus)

Yliopisto 2 merkkiä + tiedekunta 2 merkkiä 
TK:n yliopistoaineiston koodisto.
Ennen vuotta 2007 yhdistetty alkuperäisaineiston muuttujista kk ja tdk (2+2 merkkiä) . Tietoja vuosilta 2001-2013, muuttuja poistettu käytöstä 2014.
Vastaava tieto vuonna 1995 muuttujassa TIED eri luokituksella.

#### `fuksi` — Uusi yliopisto-opiskelija

**Classification:** opiskelija_3_2016_01_01 · **Group:** E4 Yliopistokoulutus, E Lähdeaineistojen omat muuttujat

Uusi/vanha yliopisto-opiskelija. Tietoja vuodesta 2013 alkaen.
0 = Vanha, ennen tilastovuotta kirjoittautunut opiskelija
1 = Uusi, tilastovuonna kirjoittautunut opiskelija
Tieto saatavilla muuttujissa 1995 UUSIOPIS sekä 1996 UUSI.

#### `ltopo` — Pätevyyteen tähtäävät opinnot

**Classification:** opiskelu_5_2016_01_01

Vuosina 2013-2014 muuttuja ollut nimellä Lastentarhaopettajan pätevyyteen tähtäävät opinnot. Käsitellyt vain sosionomi (amk)-tutkintoa, johon kuulunut lastentarhaopettajan pätevyyteen tähtääviä opintoja.  1 = Kyllä 2 = Ei. 

Vuonna 2015 muuttunut merkitys ja arvot:
1 = Sosionomi (amk) tutkintoon kuuluu opintoja, jotka tähtäävät lastentarhaopettajan pätevyyteen
2 = Sairaanhoitajan pätevyys (tutkintokeruu)
3 = Ammatillinen opettajankoulutus, pedagogiset opinnot
4 = Ammatillinen opettajankoulutus, opinto-ohjaaja
5 = Ammatillinen opettajankoulutus, erityisopettaja

#### `tilmaa` — Maksullisen tilauskoulutuksen sijaintimaa (ammattikorkeakoulukoulutus)

**Classification:** valtio_1_2012_01_01

Maksullisen tilauskoulutuksen sijaintimaa (ammattikorkeakoulukoulutus). Tiedot vuosina 2010, 2013 ja 2014.
Maakoodi. ISO 3166-standardi, itsenäiset maat ja valtiot. Vain jos Rahlahde = 4.
999 = Tuntematon

#### `rahlahde` — Opiskelijan rahoitustausta (ammattikorkeakoulukoulutus)

**Classification:** opiskelija_4_2018_01_01

Opiskelijan rahoitustausta (ammattikorkeakoulukoulutus 2005-)
1 = Perusrahoitus (2005-)
2 = ESR-rahoitus (2005-)
3 = TE-rahoitus (2005-)
4 = Maksullinen tilauskoulutus (2009-)
5 = Lukukausimaksukokeilu (2011-2017)
5 = Lukukausimaksuvelvollinen (2018-)
Vuodesta 2017 arvo voi olla myös tyhjä, mikäli kyse on erikoistumiskoulutuksesta.
Vuodesta 2018 tiedot myös yliopistokoulutuksesta. Sama tieto yliopistosektorista aiemmin muuttujalla LKMMT.

#### `kirtupv` — Ko. tutkintoon kirjoihintuloajankohta ko. ammattikorkeakoulussa (ammattikorkeakoulukoulutus)

Päivämäärä (vvvvkkpp), jolloin opiskelija on ottanut vastaan ko. tutkinnon opiskeluoikeuden ja ilmoittautunut läsnä- tai poissaolevaksi ko. oppilaitoksessa. Tietoja alkaen vuodesta 2010. Muuttuja kirtupv sisältää vuodesta 2023 alkaen yliopistokoulutuksen, aiemmin vain amk-koulutuksen.

#### `kirtu1pv` — Ensimmäinen kirjoihintuloajankohta ko. tutkintoon (ammattikorkeakoulukoulutus 2005-)

Päivämäärä (vvvvkkpp), jolloin opiskelija on ilmoittautunut ensimmäistä kertaa läsnä- tai poissaolevaksi ko. tutkintoon missä tahansa ammattikorkeakoulussa (ns. siirto-opiskelija). Vertaa muuttujat KIRTUPV, ALLV ja ALLK. Tietoja alkaen vuodesta 2010. Muuttuja kirtu1pv sisältää vuodesta 2023 alkaen myös yliopistokoulutuksen, aiemmin vain amk-koulutuksen

#### `oplaaj` — Suoritettavien opintojen laajuus (ammattikorkeakoulukoulutus)

Suoritettavien opintojen laajuus opintopisteinä (= tutkinnon laajuudesta vähennetty aiemmin suoritettujen hyväksilukujen laajuus). Tieto vuodesta 2010 alkaen.

#### `poissalk` — Poissaololukukaudet (ammattikorkeakoulukoulutus)

Poissaololukukausien määrä ko. tutkinnossa tilastovuoden lopuun mennessä. Vain ammattikorkeakoulukoulutuksessa. Tieto vuodesta 2005 alkaen.

#### `lasnalk` — Läsnäololukukaudet (ammattikorkeakoulukoulutus)

Läsnäololukukausien määrä ko. tutkinnossa tilastovuoden loppuun mennessä.
Vain ammattikorkeakoulukoulutuksessa. Tieto vuodesta 2005 alkaen.

#### `opjarj_s` — Suojattu oppisopimuskoulutuksen järjestäjän nro (oppisopimuskoulutus)

Vain oppisopimuskoulutuksessa. Tietoja vuodesta 2004 alkaen.

#### `opyrtunn_s` — Suojattu työnantajan/yrityksen yritystunnus (oppisopimuskoulutus)

Vain oppisopimuskoulutuksessa. Tiedot vuosilta 2004-2018. Muuttujan nimi muuttui vuoden 2019 ammatillisen koulutuksen reformin vuoksi. Vuodesta 2019 alkaen tiedot muuttujassa TYAN_S.

#### `yrit` — Yrittäjän oppisopimuskoulutus (ammatillinen oppisopimuskoulutus)

**Classification:** oppisopimus_2_2016_01_01

Yrittäjän oppisopimuskoulutus (ammatillinen oppisopimuskoulutus). Tiedot vuosilta 2010-2017. Muuttuja poistettu vuonna 2018. 
1 = Kyllä
2 = Ei

#### `todis` — Opiskelija on saanut todistuksen koulutuksen suorittamisesta (ammatillinen oppisopimuskoulutus)

**Classification:** oppisopimus_3_2016_01_01

Tieto vain oppisopimuskoulutuksessa 2004-2018
1 = Kyllä
2 = Ei

#### `purku` — Oppisopimus purkautunut (ammatillinen oppisopimuskoulutus)

**Classification:** oppisopimus_4_2016_01_01

Vain oppisopimuskoulutuksessa 2004 alkaen

Vuosina 2004-2018:
1 = Koeajalla
2 = Koeajan jälkeen
bl = Oppisopimus ei ole purkautunut

Vuonna 2019 muuttunut määritelmä
1 = Kyllä (aikaisempina vuosina purkautunut koejalla tai purkautunut koeajan jälkeen)

#### `toteuma` — Kalenterivuoden toteuma (ammatillinen oppisopimuskoulutus)

**Classification:** oppisopimus_5_2016_01_01

Vain oppisopimuskoulutuksessa 2004-2018
1 = Suorittanut koko tutkinnon
2 = Suorittanut tutkinnon osan tai osia
3 = Osallistunut valmistavaan koulutukseen, ei ole suorittanut tutkintoja

#### `rahoitus` — Koulutuksen rahoitus (ammatillinen näyttötutkintoon valmistava oppilaitosmuotoinen koulutus)

**Classification:** ammatillinen_2_2018_01_01

Vuodesta 2018 alkaen kaikilla ammatillisen koulutuksen opiskelijoilla. Tätä ennen eli vuosina 2004-2017 vain näyttötutkintoon valmistavassa oppilaitosmuotoisessa koulutuksessa (ei oppisopimuskoulutuksessa).
Vuosina 2004-2017 käytössä yksinumeroiset koodit (1,...,9), vuodesta 2018 alkaen kaksinumeroiset koodit (01,...,12):
1 = Valtionosuusrahoitteinen koulutus (2004-)
2 = Työvoimapoliittinen aikuiskoulutus (kansallinen rahoitus) (2004-2017)
2 = Työvoimakoulutus ely-keskukset ja työ- ja elinkeinotoimistot (kansallinen) (2018-)
3 = Työvoimapoliittinen aikuiskoulutus (ESR-rahoitus) (2004-)
4 = Työnantajan kokonaan rahoittama (2004-)
5 = Noste-ohjelmakoulutus (2004-2012) 
6 = Muuta kautta rahoitettu (opiskelijan kokonaan itse maksama) (2004-)
7 = Nuorten aikuisten osaamisohjelma (2013-)
8 = Aikuisten osaamisperustan vahvistaminen (2015-)
9 = Ei tietoa (2004-2013)
9 = Maahanmuuttajien ammatillinen koulutus (valtionavustus) (2017-)
10 = Työvoimakoulutus (OKM-rahoitus) (2018-)
11 = Ammatillisen osaamisen pilotit 2019
12 = Ammatillisen osaamisen pilotit 2019 työvoimakoulutus
bl = ei tietoa (2014-) 
HUOM! Jos haluaa poimia aineistosta vain opetushallinnon alaisen koulutuksen rahoituksen, käytä lisämuuttujana OPHAL-tietoa (rahoitus = 1 ja ophal = 1).

#### `aloit` — Aloittanut koulutuksen tai solminut oppisopimuksen kalenterivuonna

Vuoteen 2018 asti tieto vain ammatillisessa näyttötutkintoon valmistavassa ja oppisopimuskoulutuksessa. Vuodesta 2019 alkaen tieto on kaikesta ammatillisesta koulutuksesta.
1 = On
2 = Ei

Vuodesta 2004 alkaen

#### `suorosat` — Suoritettujen tutkinnon osien lukumäärä

Suoritettujen tutkinnon osien lukumäärä. Koko tutkinnot ja osatutkinnot. Tiedot alkaen 2013.
HUOM! Vuodesta 2019 alkaen tieto on alipeittävä: tieto on vain täydennyskeruun aineistoilla (eril = 1). KOSKI-aineistosta saatavien suoritusten määrää ei ole laskettu valmiiksi. Tarvittaessa voi laskea KOSKI-tiedoista.

#### `loaika` — Oppisopimuskoulutuksen tai tietyssä oppilaitoksessa tapahtuvan koulutuksen päättymispäivämäärä

Osittain epätäydellinen tieto.
(vvvvkkpp)
Kaikki ammatillinen koulutus 2013-
Ammatillinen näyttötutkintoon valmistava ja oppisopimuskoulutus 2004-2012.
Muuttuja LOAIKA löytyy myös vuonna 1995 (ammatilliinen + amk-koulutus).

#### `alaika` — Koulutuksen aloituspäivämäärä

Päivämäärä (vvvvkkpp), jolloin opiskelija on aloittanut koulutuksen tai solminut oppisopimuksen. 

99999999 = tieto puuttuu.

Kaikki ammatillinen koulutus vuodesta 2013 alkaen.
Ammatillinen näyttötutkintoon valmistava ja oppisopimuskoulutus 2004-2012. Tieto myös vuonna 1995 (ammatillinen & amk).

#### `tavoite` — Opiskelijan tavoite koulutuksessa (ammatillinen koulutus)

**Classification:** ammatillinen_4_2004_01_01

1 = Koko tutkinnon suorittaminen
2 = Tutkinnon osan tai osien suorittaminen
9 = Ei tietoa

Vuosina 2012 asti tieto vain näyttötutkintoon valmistavassa ja oppisopimuskoulutuksessa. Vuodesta 2013 eteenpäin tieto kaikesta ammatillisesta koulutuksesta.
Tieto vuodesta 2004 alkaen.

#### `ophal` — Opetushallinnon alainen koulutus

Vain ammatillisessa koulutuksessa. Vuodesta 2004 alkaen. 
1 = Kyllä
2 = Ei
Opetushallinnon alaiseen koulutukseen ei kuulu työvoimakoulutus (v. 2017 nimellä työvoimapoliittinen aikuiskoulutus), oppilaitostyyppi 28 (palo- ja poliisikoulutus), Rikosseuraamusalan koulutuskeskus (aik. nimellä Vankeinhoidon koulutuskeskus)  ja Ahvenanmaa.

#### `tyov` — Työvoimakoulutus

**Classification:** ammatillinen_3_2001_01_01

Nimi muuttunut 2018. Aikaisempi nimi oli Työvoimapoliittinen aikuiskoulutus. Vain ammatillisessa koulutuksessa. 
1 = Kyllä
2 = Ei (mm. oppisopimuskoulutus)

#### `oppis` — Oppisopimuskoulutus (ammatillinen koulutus 1999-)

**Classification:** oppisopimus_1_2014_01_01

Oppisopimuskoulutus vuodesta 2004 alkaen vuoteen 2018 asti koko kalenterivuodelta. Tätä ennen poikkileikkaustilanteesta 20.9. (alipeittävä). Koko kalenterivuoden tiedot erillisissä oppisopimustoimistojen aineistoissa vuosilta 1997 - 2003. 
1 = Kyllä
2 = Ei

#### `noste` — Koulutuksen kuuluminen Noste-ohjelmaan

Koulutuksen kuuluminen Noste-ohjelmaan (ammatillinen koulutus 2003-). Tietoja vuosilta 2003 ja 2010-2012.
1 = Kyllä
2 = Ei

#### `tutktav` — Opetussuunnitelmaperusteinen/näyttötutkintoon valmistava koulutus

**Classification:** ammatillinen_1_2000_01_01

Vain ammatillisessa koulutuksessa. Tiedot vuosilta 1999-2017. Vuoden 2018 uuden lain myötä ammatillista koulutusta ei enää jaeta nuorille ja aikuisille suunnattuihin koulutuksiin, täten muuttuja poistettu.
1 = Opetussuunnitelmaperusteinen koulutus (klajit 31 ja 35) 
2 = Näyttötutkintoon valmistava koulutus (sisältää oppisopimuskoulutuksen; klajit 32-34 ja 36-38)

#### `tutklaja` — Ammatillisen koulutuksen koulutuslaji

**Classification:** koullaji_2_2014_01_01

Ammatillisten koulutuslaji. Tiedot puuttuvat vuosilta 2004-2005 ja 2007-2008.
1 = Ammatillinen peruskoulutus (klajit 31, 32, 35 ja 36)
2 = Ammattitutkinto (klajit 33 ja 37)
3 = Erikoisammattitutkinto (klajit 34 ja 38)
Vain ammatillisessa koulutuksessa

#### `jarj_s` — Suojattu koulutuksen järjestäjä/ylläpitäjä

Suojattu koulutuksen järjestäjä/ylläpitäjä (1999-). 
Oppisopimuskoulutuksesta tietoa ei ole (ks. opjarj vuodesta 2004 alkaen).

#### `oltunn_s` — Suojattu oppilaitostunnus

Suojattu oppilaitostunnus, 
TK:n oppilaitosluokitus 31.12., 
bl = ei tietoa (oppisopimuskoulutus)
Tiedot alkaen vuodesta 1995.

#### `kkun` — Koulutuksen sijaintikunta

**Classification:** kunta_1_2019_01_01

Koulutuksen sijaintikunta 1.1. tilastovuonna 
VRK:n kuntakoodi
200=Ulkomaat
Oppisopimuskoulutuksessa ja varhaiskasvatuksen esiopetuksessa koulutuksen järjestäjän sijaintikunta.
Tiedot vuosilta 1995 alkaen muuttujassa KKUN, paitsi 1997 OKUNTA.

#### `kkieli` — Koulutuksen opetuskieli (1999-)

**Classification:** kieli_1_2010_11_15

Koulutuksen opetuskieli
2-kirjaiminen tunnus (ISO 639)
bl = yliopistokoulutuksessa tietoa ei ole

#### `aikoul` — Nuorten/aikuisten koulutus

**Classification:** koulutus_15_2016_01_01

Tieto kuvaa koulutuksen järjestämistapaa, ei opiskelijan ikää. Tietoja vuodesta 1995 eteenpäin, paitsi 1996 ja 2004-2009. Vuonna 1997 muuttujassa KOTY.
1 = Nuorten koulutus (2001 alkaen kaikki yliopistokoulutus)
2 = Aikuisten koulutus (sis. 2005 alkaen ylemmät amk-tutkinnot sekä 2015 alkaen amk:n monimuotototeutukset)
9 = Ei määritelty (ammattikorkeakoulujen erikoistumisopinnot ja erikoistumiskoulutukset sekä ammatillinen opettajankoulutus) (2005-)
bl = ammatillisessa koulutuksessa tietoa ei ole
Vuonna 2016 lisätty ammattikorkeakoulujen erikoistumiskoulutukset arvolle 9.

#### `suv` — Suuntautumisvaihtoehtonimikekoodi

Koulutuskoodia tarkentava aputieto vuodesta 2001 alkaen, paitsi 2004-2009. TK:n ammatillisen, amk- ja yliopistoaineiston omat työkoodistot. Lukiokoulutuksessa ja ammatillisessa koulutuksessa tietoa ei ole (= bl). Koodin ensimmäinen merkki kertoo lähdeaineiston: 4 = ammattikorkea-, 5 = yliopistoaineisto. Yliopistokoulutuksessa vain koodit 500000 "Ei suuntautumisvaihtoehtoa" ja 500100 "Aineenopettajan pedagogiset opinnot"
Käytä aina nimikkeen kanssa. Ks. erillinen nimikkeistö, jossa on koodin tuorein nimike.
Vuodesta 2014 määritelmä muuttunut, sisältää vain yliopistokoulutuksen aineenopettajan pedagogiset opinnot. 
Yliopisto-opintojen osalta vuoden 2001-2013 määritelmää vastaava tieto vuonna 1995 muuttujassa SUUNTV.

#### `kou` — Koulutusohjelma-/pääainenimikekoodi

Koulutuskoodia tarkentava aputieto. Tietoja alkaen vuodesta 2001, paitsi vuosilta 2004-2009.
TK:n ammatillisen, amk- ja yliopistoaineiston omat työkoodistot. Lukiokoulutuksessa tietoa ei ole, eikä kaikissa ammatillisissa koulutuksissa.
Koodin ensimmäinen merkki kertoo lähdeaineiston:
3 = ammatillinen (2001-)
4 = ammattikorkea- (2001-2014)
5 = yliopistoaineisto (2001-2013)
bl = lukiokoulutuksessa, ammattikorkeakoulutuksessa ja yliopistokoulutuksessa tietoa ei ole, eikä kaikissa ammatillissa koulutuksissa

Käytä aina nimikkeen kanssa. Ks. erillinen nimikkeistö, jossa on koodin tuorein nimike.
Vuodesta 2019 alkaen  tietoon lisätty luokituskoodisto, koska tieto tulee KOSKI-tietovarannosta.
Vastaavaa tietoa yliopistokoulutuksesta vuodelta 1995 muuttujassa OPS kyseisen vuoden luokituksin.

#### `tut` — Tutkintonimikekoodi/opintojen tarkoitus

Koulutuskoodia tarkentava aputieto vuodesta 2001 alkaen, paitsi 2004-2009.
TK:n ammatillisen, amk- ja yliopistoaineiston omat työkoodistot. Lukiokoulutuksessa tietoa ei ole, eikä kaikissa ammatillisissa koulutuksissa.
Koodin ensimmäinen merkki kertoo lähdeaineiston:
3 = ammatillinen
4 = ammattikorkea- 
5 = yliopistoaineisto
bl = lukio- ja ammattikorkeakoulutuksessa tietoa ei ole, eikä kaikissa ammatillisissa koulutuksissa (2001-2018)
bl = lukiokoulutuksessa, ammattikorkeakoulutuksessa ja yliopistokoulutuksessa tietoa ei ole, eikä kaikissa ammatillisissa koulutuksissa (2019-).

Käytä aina nimikkeen kanssa. Ks. erillinen nimikkeistö, jossa on koodin tuorein nimike.
Vuonna 2014 poistettu arvo 4 = ammattikorkea-.
Vuodesta 2019 alkaen tietoon lisätty luokituskoodisto, koska tieto tulee KOSKI-tietovarannosta. Aiemmin sääntönä, että koodin ensimmäinen merkki kertoi lähdeaineiston: 3 = ammatillinen, 5 = yliopistoaineisto. Nykyisin vain ammatillisen koulutuksen koodit. 
Vastaava tieto yliopisto-opintojen osalta vuonna 1995 muuttujassa OPTAR.

#### `koulk` — Tilastokeskuksen koulutuskoodi

**Classification:** koulutus_18_2018_01_01

Tilastokeskuksen koulutusluokitus 1997 (6-numeroinen koulutuskoodi) ja siihen vuosittain tehdyt muutokset.
Koulutuskoodin 1. merkki kertoo koulutusasteen ja 2. merkki  koulutusalan. Tiedot vuodesta 1995 alkaen.

#### `tutalk` — Lukukausi, jolloin opiskelija on aloittanut ko.koulutuksen/tutkinnon missä tahansa oppilaitoksessa

**Classification:** opiskelu_7_2011_01_01

Tieto ammatillisesta OPS-perusteisesta oppilaitosmuotoisesta koulutuksesta 2004 alkaen, lukio- ja ammattikorkeakoulutuksesta 2011 alkaen
1 = kevät (1.1.-31.7.)
2 = syksy (1.8.-31.12.)
9 = tieto puuttuu (2004-2013)
bl = tietoa ei kerätty
bl = ammatillisessa oppisopimuskoulutuksessa ja näyttötutkintoon valmistavassa koulutuksessa sekä yliopistokoulutuksessa (2011-2017)
bl = yliopistokoulutuksessa (2018-)
Vuonna 2014 poistettu arvo 9= ei tietoa.
Vuodesta 2018 alkaen tieto kaikilla oppilaitosmuotoisen ammatillisen koulutuksen opiskelijoilla. Aikaisempina vuosina tieto vain opetussuunnitelmaperusteisen koulutuksen opiskelijoilla.
Vuodesta 2019 alkaen tietoa ei enää saada ammatillisesta koulutuksesta, koska tietoa ei ole KOSKI-tietovarannossa.

#### `tutalv` — Vuosi, jolloin opiskelija on aloittanut ko. koulutuksen/tutkinnon missä tahansa oppilaitoksessa

VVVV. Tieto ammatillisesta OPS-perusteisesta oppilaitosmuotoisesta koulutuksesta 2004 alkaen, lukio- ja ammattikorkeakoulutuksesta 2011 alkaen. Vuodesta 2018 alkaen tieto kaikilla oppilaitosmuotoisen ammatillisen koulutuksen opiskelijoilla. Aikaisempina vuosina tieto vain opetussuunnitelmaperusteisen koulutuksen opiskelijoilla. Vuodesta 2019 alkaen tietoa ei enää saada ammatillisesta koulutuksesta, koska tietoa ei ole KOSKI-tietovarannossa.
bl = ammatillisessa oppisopimuskoulutuksessa ja näyttötutkintoon valmistavassa koulutuksessa sekä yliopistokoulutuksessa (2011-2017)
bl = yliopistokoulutuksessa (2018-)

#### `ovker` — Edeltävän kevätlukukauden loppuun mennessä suoritetut opintoviikot

Tilastovuoden kevätlukukauden loppuun mennessä suoritetut opintoviikot (yliopisto- ja ammattikorkeakoulukoulutus 2002-2004). Tieto vuosilta 2002-2004. Lukiokoulutuksesta ja ammatillisesta koulutuksesta tietoa ei ole. Vuodesta 2005 alkaen opintopisteet muuttujasta OPKER.

#### `ovek` — Edeltävällä kevätlukukaudella suoritetut opintoviikot

Tilastovuoden kevätlukukaudella suoritetut opintoviikot (yliopisto- ja ammattikorkeakoulukoulutus 2002-2004). Tieto vuosilta 2002-2004. Lukiokoulutuksesta ja ammatillisesta koulutuksesta tietoa ei ole. Vuodesta 2005 alkaen opintopisteet muuttujasta OPEK.

#### `oves` — Edeltävällä syyslukukaudella suoritetut opintoviikot

Edeltävällä syyslukukaudella suoritetut opintoviikot (yliopisto- ja ammattikorkeakoulukoulutus 2002-2004)
Tieto vuosilta 2002-2004. Lukiokoulutuksesta ja ammatillisesta koulutuksesta tietoa ei ole. Vuodesta 2005 alkaen opintopisteet muuttujasta OPES.

#### `opker` — Edeltävän kevätlukukauden loppuun mennessä suoritetut opintopisteet

Tilastovuoden kevätlukukauden loppuun mennessä suoritetut opintopisteet (yliopisto- ja ammattikorkeakoulukoulutus 2005-). 
Tieto vuodesta 2005 alkaen. 
bl = Lukiokoulutuksessa ja ammatillisessa koulutuksessa tietoa ei ole.

#### `opek` — Edeltävällä kevätlukukaudella suoritetut opintopisteet

Tilastovuoden kevätlukukaudella suoritetut opintopisteet (yliopisto- ja ammattikorkeakoulukoulutus 2005-)
Tieto vuodesta 2005 alkaen. Lukiokoulutuksesta ja ammatillisesta koulutuksesta tietoa ei ole.

#### `opes` — Edeltävällä syyslukukaudella suoritetut opintopisteet

Edeltävällä syyslukukaudella suoritetut opintopisteet (yliopisto- ja ammattikorkeakoulukoulutus 2005-)

Tieto vuodesta 2005 alkaen. Lukiokoulutuksesta ja ammatillisesta koulutuksesta tietoa ei ole.

#### `fte` — Full-time equivalent (FTE) -luku (yliopisto- ja ammattikorkeakoulukoulutus 2006-)

Yliopisto- ja ammattikorkeakoulukoulutuksessa. Tieto vuodesta 2006 alkaen.
FTE-luvun avulla muunnetaan tutkintoon johtavan koulutuksen osa-aikaiset opiskelijat kokopäiväopiskelijoiksi. Sen avulla saadaan volyymitietoa mm. kustannusten laskentaa varten. Tietoa käytetään kansainvälisessä UOE-kyselyssä.
0,0 = kaikki poissaoleviksi ilmoittautuneet opiskelijat
0,5 = jatkokoulutuksen opiskelijat (klajit 46 ja 52), edellisenä lukuvuonna alle 30 opintopistettä suorittaneet peruskoulutuksen opiskelijat (klajit 41, 42, 51 ja oplu=0)
1,0 = uudet opiskelijat, edellisenä lukuvuonna vähintään 30 opintopistettä suorittaneet peruskoulutuksen opiskelijat   
bl = tutkintoon johtamattoman koulutuksen opiskelijat (oplu=1) sekä lukio- ja ammatillisen koulutuksen opiskelijat

#### `kokosa` — Kokopäivä-/osa-aikaopiskelija (yliopisto- ja ammattikorkeakoulukoulutus 2002-)

**Classification:** opiskelija_1_2014_01_01

Lukio- ja ammatillisessa koulutuksessa opiskelun koko- tai osa-aikaisuutta ei ole määritelty. 
Yliopisto- ja ammattikorkeakoulukoulutuksessa edellisen lukuvuoden aikana vähintään 30 opintopistettä suorittaneet ja ensimmäistä vuotta opiskelevat luokitellaan kokopäiväisiksi opiskelijoiksi, mikäli he ovat tutkintoon johtavassa peruskoulutuksessa (klajit 41, 42, 51 ja oplu=0) ja läsnä 20.9. (olosyys=1). Muut tutkintoon johtavassa koulutuksessa opiskelevat (edellisenä lukuvuonna alle 30 opintopistettä suorittaneet, poissaoleviksi ilmoittautuneet sekä jatkokoulutuksen opiskelijat) luokitellaan osa-aikaisiksi opiskelijoiksi. Tutkintoon johtamattoman koulutuksen (oplu=1) koko- tai osa-aikaisuutta ei ole määritelty. Tietoja alkaen vuodesta 2002.

Muuttuja kokosa:  Määrittelyyn käytettään nyt kirtuv-muuttujaa, joka  tarkoittaa kirjoilletulovuotta ensimmäisen kerran ko. yliopistoon. Vuoteen 2022 asti käytettiin alvv-muuttujaan, joka tarkoittaa kirjoihintuloa (aloitusvuotta) ensimmäisen kerran ko. koulutukseen ko. yliopistoon. Tieto pohjasi tuolloin opoik-muuttujaan.

1 = Kokopäiväopiskelija
2 = Osa-aikaopiskelija
9 = Ei pystytä määrittelemään (lukio- ja ammatillinen koulutus, tutkintoon johtamaton koulutus)
bl = Ammatillinen koulutus

#### `tilvaskunx` — Kotikunta edellisen vuoden lopussa ko. tilastovuoden luokituksin

**Classification:** kunta_1_2018_01_01

- Tätä muuttujaa ei enää päivitetä vuodesta 2023 lähtien.

Opiskelijan kotikunta 31.12.[tilastovuotta edeltävä vuosi], luokitus 1.1.[tilastovuotta edeltävä vuosi]
VRK:n kuntakoodi. Tiedot vuodesta 2013 alkaen. 
200 = Ulkomaa
999 = Ei tietoa

#### `tilvaskun` — Kotikunta / vakituinen asuinkunta tilastovuoden luokituksin

**Classification:** kunta_1_2018_01_01

Opiskelijan kotikunta 31.12.[tilastovuosi], luokitus 1.1.[tilastovuosi]
Tieto ensisijaisesti VRK:n aineistosta. Tiedot vuodesta 2013 alkaen.
200 = Ulkomaa
999 = Ei tietoa

#### `askunx` — Kotikunta / vakituinen asuinkunta edellisen vuoden lopussa

**Classification:** kunta_1_2018_01_01

- Tätä muuttujaa ei enää päivitetä vuodesta 2023 lähtien.

Opiskelijan kotikunta 31.12.[tilastovuotta edeltävä vuosi], luokitus 1.1.[tilastovuosi]
VRK:n kuntakoodi. Tiedot alkaen vuodesta 2013.
200 = Ulkomaa
999 = Ei tietoa

#### `askun` — Opiskelijan kotikunta

**Classification:** kunta_1_2019_01_01

Opiskelijan kotikunta vuoden lopussa (31.12.), luokitus 1.1. tilastovuosi +1
200 = Ulkomaa
999 = Ei tietoa
Tieto ensisijaisesti VRK:n aineistosta.
Puutteellisen henkilötunnuksen omaavilla oppilaitoksen ilmoittama tieto.
Tieto vuosina 1995-1996 KOTIKUN, 1997 ASKUNTA, 1998 ASKUN.

#### `aiopis` — Aikuisopiskelija

**Classification:** opiskelija_5_2013_01_01 · **Group:** B Opiskelijaa tai opiskelua kuvaavat tiedot

Aikuisopiskelija on henkilö, joka on aloittanut opintonsa ko. oppilaitoksessa ko. koulutuksessa tai osallistunut oppisopimuskoulutukseen 25-vuotiaana tai sitä vanhempana. Aikuisopiskelija voi opiskella missä tahansa oppilaitoksessa tai koulutuksessa riippumatta siitä, onko koulutus suunniteltu aikuisille vai ei. Tietoja alkaen vuodesta 2013. 
Vuodesta 2018 muuttujakuvauksen määritelmää täsmennetty, sisältö ja tarkoitus pysynyt samana: Aikuisopiskelija on henkilö, joka on aloittanut opintonsa ko. oppilaitoksessa ko. koulutuksessa tai solminut oppisopimuksen 25-vuotiaana tai sitä vanhempana. Aikuisopiskelija voi opiskella missä tahansa oppilaitoksessa tai koulutuksessa riippumatta siitä, onko koulutus suunniteltu aikuisille vai ei.
1 = Nuori opiskelija
2 = Aikuisopiskelija
9 = Ei määritelty (kaikki yliopistokoulutus) / Tuntematon

Tietoa ei saada perusopetuksesta.

#### `allk` — Tutkinnon aloittamislukukausi/kirjoilletulolukukausi (1997-)

**Classification:** opiskelu_6_2013_01_01

Tutkinnon aloittamislukukausi (1997-)
1 = Kevät (1.1.-31.7.)
2 = Syksy (1.8.-31.12.)
9 = Ei tietoa

Yliopistojen ALKK-tieto tarkentui vuonna 2012, lisätietoja ALVV-muuttujan yhteydessä.
Vuosilta 1997-1998 vain yliopistokoulutuksesta ja vakinaisten ammattikorkeakoulujen koulutuksista.
Ks. alvv

#### `alvv` — Tutkinnon aloittamisvuosi/kirjoilletulovuosi (1997-)

Vuosi (vvvv), jolloin opiskelija on ottanut vastaan ko. tutkinnon opiskeluoikeuden ko. oppilaitoksessa ja ilmoittautunut koulun kirjoihin 20.9. mennessä tai solminut oppisopimuksen. Oppilaitoksen ja koulutuksen kannalta uudet opiskelijat (muut koulutukset) saadaan tämän muuttujan avulla (alvv=tilastovuosi). Uudet opiskelijat ovat tulleet kirjoille oppilaitokseen 1.1. - 20.9. Ainoastaan ammatillisessa koulutuksessa uudet opiskelijat ja oppisopimuskoulutuksen uudet opiskelijat ovat koko kalenterivuodelta.

9999 = ei tietoa.

Muutokset vuosien varrella:

Ammatillinen koulutus:
- Vuodesta 2013 eteenpäin ammatillisen koulutuksen aloittamistieto on koko kalenterivuodelta kaikkien koulutusten osalta.
- Vuodesta 2004 ammatillisessa koulutuksessa näyttötutkintoon valmistavan koulutuksen uudet opiskelijat ja oppisopimuskoulutuksen uudet opiskelijat ovat koko kalenterivuodelta. 

Ammattikorkeakoulutus:
- Ammattikorkeakoulukoulutuksen uusi opiskelija oli vuoteen 2001 asti ensimmäistä kertaa läsnäolleeksi kirjoittautunut opiskelija. 

Yliopistokoulutus:
- Vuoteen 2011 asti yliopistokoulutuksen ALVV- ja ALKK-muuttujat kuvasivat sitä ajankohtaa, jolloin henkilö aloitti opinnot ko. oppilaitoksessa missä tahansa koulutuksessa. Vuodesta 2012 ALVV- ja ALKK-muuttujien tieto on tarkempi: Vuodesta 2012 alkaen saadaan tieto ajankohdasta, jolloin henkilö aloitti ensimmäistä kertaa ko. koulutuksen ko. oppilaitoksessa.
- Yliopistokoulutuksen uusi opiskelija oli vuoteen 2001 asti kalenterivuonna ko. yliopistossa koulutuksen aloittanut.

Vuosina 1997 ja 1998 päivälukioiden, ammatillisten oppilaitosten ja väliaikaisten ammattikorkeakoulujen opiskelijoilla '0000 tarkoittaa vuotta 1995 tai aiemmin.

#### `olotamm` — Kirjoilla 20.1. (1999-)

**Classification:** kirjoilla_4_2016_01_01

Kirjoilla 20.1. tai kirjoilla kevätlukukaudella (yliopistokoulutus) tai kirjoilla jossain vaiheessa kalenterivuotta (näyttötutk. valm. koulutus) tai voimassa oleva oppisopimus jossain vaiheessa kalenterivuotta 
1 = Läsnä (=opiskeli tai oli pakollisessa työharjoittelussa) 20.1. tai keväällä
2 = Poissa (=opiskelija oli kirjoilla oppilaitoksessa, mutta ei opiskellut asepalveluksen, äitiysloman tai muun hyväksytyn syyn vuoksi) 20.1. tai keväällä
9 = Ei ilmoittautumistietoa / ei kirjoilla 20.1. (esim. kaikki tilastovuoden syksyllä opintonsa aloittaneet)

HUOM! Muuttuja OLOTAMM ei sisällä lukio-, amk- ja yliopistokoulutuksen osalta kaikkia kevään opiskelijoita vaan vain ne, jotka jatkoivat opiskeluaan syksyllä 20.9. Oppisopimuskoulutuksesta (ja vuoteen 2017 asti näyttötutkintoon valmistavasta koulutuksesta) ei ole varsinaista läsnäolotietoa. Mukana ovat kaikki jossain vaiheessa kalenterivuotta opiskelleet. Vuodesta 2018 alkaen tieto on kaikilla oppilaitosmuotoisen ammatillisen koulutuksen opiskelijoilla, aiemmin vain opetussuunnitelmaperusteisen koulutuksen opiskelijoilla. Oppisopimuskoulutus tilastoidaan kuten aikaisempinakin vuosina).
Tieto vuosilta 1997-1998 muuttujassa LASNAK.

#### `olosyys` — Kirjoilla 20.9 (1999-)

**Classification:** kirjoilla_3_2018_01_01

Muuttujan määritelmä vuoteen 2017 saakka:
Kirjoilla 20.9. tai kirjoilla jossain vaiheessa kalenterivuotta (näyttötutk. valm. koulutus) tai voimassa oleva oppisopimus jossain vaiheessa kalenterivuotta 
1 = Läsnä (=opiskeli tai oli pakollisessa työharjoittelussa) 20.9. tai kirjoilla/oppisopimus jossain vaiheessa kalenterivuotta
2 = Poissa (=opiskelija oli kirjoilla oppilaitoksessa, mutta ei opiskellut asepalveluksen, äitiysloman tai muun hyväksytyn syyn vuoksi) 20.9.
9 = Ei ilmoittautumistietoa / ei kirjoilla 20.9.
Muuttujan määritelmä vuodesta 2018 alkaen: 
Kirjoilla 20.9. tai kirjoilla jossain vaiheessa kalenterivuotta (voimassa oleva oppisopimus)
1 = Läsnä (=opiskeli tai oli pakollisessa työharjoittelussa) 20.9. tai opiskeli jossain vaiheessa kalenterivuotta (oppisopimuskoulutus)
2 = Poissa (=opiskelija oli kirjoilla oppilaitoksessa, mutta ei opiskellut asepalveluksen, äitiysloman tai muun hyväksytyn syyn vuoksi) 20.9.
9 = Ei ilmoittautumistietoa / ei kirjoilla 20.9.
Oppisopimuskoulutuksesta ei ole varsinaista läsnäolotietoa. Mukana ovat kaikki jossain vaiheessa kalenterivuotta opiskelleet.

Aiempien vuosien muutokset, jotka ovat edelleen voimassa:
Vuodesta 2016 arvo 9 sis. myös amk:n erikoistumiskoulutuksia, joissa ei ole läsnä- tai poissaoloilmoitusta.
Vuodesta 2017 arvo 9 sis. myös yliopistojen erikoistumiskoulutuksia, joissa ei ole läsnä- tai poissaoloilmoitusta.
Osa klaji=54 arvoista saa olosyys-muuttujalla arvon 2.
Vuodesta 2018 tieto on kaikilla oppilaitosmuotoisen ammatillisen koulutuksen opiskelijoilla, aiemmin vain opetussuunnitelmaperusteisen koulutuksen opiskelijoilla. Oppisopimuskoulutus tilastoidaan kuten aikaisempinakin vuosina.
Tieto vuosina 1997-1998 muuttujassa LASNAS.

#### `aikieli` — Äidinkieli (1999-)

**Classification:** kieli_1_2010_11_15

Opiskelijan äidinkieli 31.12.
2-kirjaiminen tunnus (ISO 639-standardi). Tieto ensisijaisesti VRK:n aineistosta. Puutteellisen henkilotunnuksen omaavilla oppilaitoksen ilmoittama tieto.
99 = ei tietoa.
Tieto vuosina 1995 ja 1997 KIELI, 1998 AIKIELI eroavilla luokituksilla.

#### `kansal` — Kansalaisuus (1999-)

**Classification:** valtio_1_2012_01_01

Opiskelijan kansalaisuus vuoden lopussa.
Tieto ensisijaisesti VRK:n aineistosta (ISO 3166-standardi). Puutteellisen henkilötunnuksen omaavilla oppilaitoksen ilmoittama tieto.
999=Ei tietoa.
Tieto saatavilla muuttujissa 1995 KANS ja 1997-1998 KANSA.

#### `ika` — Ikä tilastovuoden lopussa

Ikä vuosina 31.12. Ikätieto on puutteellisen henkilötunnuksen omaavilla oppilaitoksen ilmoittama tieto. Tiedot vuodesta 1995 alkaen.

#### `sp` — Sukupuoli

**Classification:** sukupuoli_2_1970_01_01

Sukupuoli
1 = Mies
2 = Nainen
9 = Määrittelemättä (2020-)
Sukupuolitieto puutteellisen henkilötunnuksen omaavilla oppilaitoksen ilmoittama tieto. Tiedot alkaen vuodesta 1995.

#### `oplu` — Opiskelun luonne

**Classification:** oplu_3_2018_01_01

Vuonna 2013 vain ammattikorkeakoulukoulutuksesta, vuodesta 2014 alkaen arvot koskevat kaikkia koulutussektoreita.
0 = Koulutus johtaa tutkintoon ja opiskelija on kirjoilla 20.9. (2013-)
1 = Koulutus ei johda tutkintoon (näiden henkilöiden tiedot voivat olla puutteellisia) tai opiskelija ei ole kirjoilla 20.9. (2013-)
9 = Opetussuunnitelmaperusteisen koulutuksen opiskelijat, jotka eivät olleet kirjoilla 20.9. (2014-2017)
9 = Ammatillisen koulutuksen opiskelijat, jotka eivät olleet kirjoilla 20.9. (2018-)
Vuodesta 2018 arvo 9 muuttunut lakimuutoksen myötä. Tieto kaikilla oppilaitosmuotoisen ammatillisen koulutuksen opiskelijoilla. Oppisopimuskoulutus tilastoidaan kuten aikaisempinakin vuosina.

#### `oprior` — Opiskelun prioriteetti (1997-)

**Classification:** opiskelu_1_2014_01_01

Ensisijainen koulutus on viimeksi aloitettu koulutus. Jos samana vuonna on aloitettu useita koulutuksia, on poimittu TK:n koulutusasteen mukaan korkein koulutus. Tutkintoon johtava koulutus on priorisoitu ennen tutkintoon johtamatonta koulusta. Tiedot alkaen vuodesta 1997.
1 = Ensisijainen koulutus 
2 = Toissijainen koulutus. 
Muuttuja Oprior on laskettu vuosina 1997-2000 ainoastaan syksyllä läsnä oleviksi ilmoittautuneista opiskelijoista. 
Muuttuja Oprior on laskettu vuosina 2001-2009 kaikesta koulutuksesta (sekä tutkintoon johtavasta että tutkintoon johtamattomasta koulutuksesta). Tästä syystä mukana voi olla henkilöitä, joille löytyy vain oprior=2. Tällöin henkilö on aloittanut viimeiseksi tutkintoon johtamattoman koulutuksen. 
Vuodesta 2010 lähtien oprior lasketaan vain tutkintoon johtavasta koulutuksesta.

#### `klaji` — Koulutuslaji (1999-)

21 = Lukiokoulutus, nuorten OPS (oppilaitoksen määrittelemä tieto)
22 = Lukiokoulutus, aikuisten OPS (oppilaitoksen määrittelemä tieto)
31 = OPS-perusteinen ammatillinen peruskoulutus (ei oppisopimuskoulutus) 
32 = Näyttötutkintoon valmistava koulutus: perustutkinnot (ei oppisop. koul.)
33 = Näyttötutkintoon valmistava koulutus: ammattitutkinnot (ei oppisop.koul.)
34 = Näyttötutkintoon valmistava koulutus: erikoisammattitutkinnot (ei oppisop.k.)
35 = OPS-perusteinen ammatillinen peruskoulutus (oppisopimuskoulutus) 
36 = Näyttötutkintoon valmistava koulutus: perustutkinnot (oppisopimuskoulutus)
37 = Näyttötutkintoon valmistava koulutus: ammattitutkinnot (oppisopimuskoulutus)
38 = Näyttötutkintoon valmistava koulutus: erikoisammattitutkinnot (oppisop.koul.)
41 = Ammattikorkeakoulututkinto, nuorten koulutus 
42 = Ammattikorkeakoulututkinto, aikuisten koulutus
46 = Ylempään AMK-tutkintoon tähtäävä koulutus 
51 = Alempaan ja ylempään korkeakoulututkintoon tähtäävä koulutus
52 = Lisensiaatinkoulutus, tohtorinkoulutus ja lääkärien erik.koul.
Vuodesta 2013 alkaen:
43 = Ammattikorkeakoulujen erikoistumisopinnot (poistuvat, OPLU=1) ( ammattikorkeakoulujen erikoistumisopintoja ei enää ole. Klajin arvo 43 pidetään kuvauksessa.)
45 = Ammattikorkeakoulujen ammatillinen opettajankoulutus (OPLU=1)
Vuodesta 2015 alkaen: 
52 = Lisensiaatinkoulutus, tohtorinkoulutus ja eläinlääkäreiden erik.koul. ( arvo 52 sisältää eläinlääkäreiden erikoistumiskoulutuksen, jos se on aloitettu 31.7.2023 mennessä.)
53 = Lääkärien ja hammaslääkärien erikoistumiskoulutus (OPLU=1 eli tutkintoon johtamaton koulutus) ( arvo 53 sisältää eläinlääkäreiden erikoistumiskoulutuksen, jos se on aloitettu 1.8.2023 tai sen jälkeen.)
Vuodesta 2016 alkaen:
41 = Ammattikorkeakoulututkinto, päivätoteutus
42 = Ammattikorkeakoulututkinto, monimuotototeutus
44 = Ammattikorkeakoulujen erikoitusmiskoulutukset (OPLU=1)
54 = Yliopistojen erikoistumiskoulutukset (OPLU=1) alk. 2016, pl. lääkärit ja hammaslääkärit
Vuodesta 2018 alkaen:
61 = Ammatilliset perustutkinnot, ei oppisopimuskoulutus
62 = Ammattitutkinnot, ei oppisopimuskoulutus
63 = Erikoisammattitutkinnot, ei oppisopimuskoulutus
64 = Ammatilliset perustutkinnot, oppisopimuskoulutus
65 = Ammattitutkinnot, oppisopimuskoulutus
66 = Erikoisammattitutkinnot, oppisopimuskoulutus
Poistettu käytöstä ammatillisen koulutuksen arvot 31, 32, 33, 34, 35, 36, 37 ja 38.
Vuodesta 2019 alkaen:
71 = Ammatilliset perustutkinnot (ei sisällä koulutussopimus- eikä oppisopimusjaksoja)
72 = Ammattitutkinnot (ei sisällä koulutus- eikä oppisopimusjaksoja)
73 = Erikoisammattitutkinnot (ei sisällä koulutus- eikä oppisopimusjaksoja)
74 = Ammatilliset perustutkinnot (sisältää sekä koulutus- että oppisopimusjaksoja)
75 = Ammattitutkinnot (sisältää sekä koulutus- että oppisopimusjaksoja)
76 = Erikoisammattitutkinnot (sisältää sekä koulutus- että oppisopimusjaksoja)
77 = Ammatilliset perustutkinnot (sisältää koulutussopimusjaksoja)
78 = Ammattitutkinnot (sisältää koulutussopimusjaksoja)
79 = Erikoisammattittutkinnot (sisältää koulutussopimusjaksoja)
80 = Ammatilliset perustutkinnot (sisältää oppisopimusjaksoja)
81 = Ammattitutkinnot (sisältää oppisopimusjaksoja)
82 = Erikoisammattitutkinnot (sisältää oppisopimusjaksoja)

#### `ain` — Lähdeaineisto

**Classification:** lahdeaineisto_1_2014_01_01

Lähdeaineisto (karkea)
20 = Lukiokoulutusaineisto
30 = Ammatillisen koulutuksen aineisto
40 = Ammattikorkeakoulukoulutusaineisto
50 = Yliopistokoulutusaineisto

#### `hid_e` — Suojattu henkilön yksilöivä tunniste

Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e -tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä.

#### `vuosi` — Aineistovuosi

Opiskelija-aineistossa TILV 1995-1998.

Viiteajankohdat:

* Lukiokoulutus 1995-
  * 20.9. (ei sisällä aineopiskelijoita)

* Ammatillinen koulutus 2013- 1.1.-31.12. (Kaikki koulutuslajit)
* Ammatillinen koulutus 2004-2012
  * Opetussuunnitelmaperusteinen amm. koulutus 20.9. 
  * Näyttötutkintoon valmistava ja oppisopimuskoulutus
    1.1.-31.12.
* Ammatillinen koulutus 1995-2003
  * 20.9. (1995-1998 ei sisällä oppisopimuskoulutusta)

* Ammattikorkeakoulukoulutus 1995- 
  * 20.9.

* Yliopistokoulutus 2002-
  * 20.9. 
* Yliopistokoulutus 1995-2001 
  * 31.12. sisältäen syksyllä tutkinnon suorittaneet

---

[← Back to catalogue](../../README.md)
