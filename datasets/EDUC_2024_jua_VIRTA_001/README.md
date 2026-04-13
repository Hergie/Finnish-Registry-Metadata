# EDUC_VIRTA-aineisto

- **Identifier:** `EDUC_2024_jua_VIRTA_001.xml`
- **DOI:** `yop_2018-08_2018-08-24_ain_0001`
- **Temporal coverage:**  - 2024-12-31
- **Published:** 2025-06-09
- **Organisation:** Tilastokeskus
- **Variable count:** 61
- **Observation count:** —
- **Population:** Korkeakouluopiskelijat
- **Source:** Korkeakoulujen opiskelijarekisterit
- **Related:** <a href= "https://confluence.csc.fi/display/VIRTA/Tietovarannon+tiedot">Virta-opintopalvelun tietosisältö</a>

## Kuvaus / Description

"VIRTA higher education achievement register”

VIRTA-aineisto on korkeakoulujen opiskelijatietoja sisältävä valtakunnallinen tietovaranto. Virta-aineisto sisältää korkeakoulujen opiskelijarekisterien tietoja. Historiatietojen kattavuus riippuu korkeakoulusta.
Virta-aineistoa voi saada tutkimuskäyttöön Tilastokeskuksen FIONA-tutkimusaineistojen etäkäyttöpalveluun. Tutkimushankekohtainen tutkimuslupa VIRTA-aineiston käyttämiseen haetaan Tilastokeskuksen kautta ja korkeakoulut rekisterinpitäjinä vastaavat luvan myöntämisestä. FIONAssa käytettävissä oleva aineisto sisältää kattavasti VIRTA-aineiston tietosisällön ja tiedot päivitetään kerran vuodessa. Maanpuolustuskorkeakoulun opiskelijarekisteriä ei ole otettu Virta-aineistoon mukaan.

VIRTA-aineisto sisältää tietoja viidestä tietoryhmästä: opiskelijat, lukukausi-ilmoittautuminen, opiskeluoikeudet, opiskeluoikeusjakso, opintosuoritukset. 

Aineisto koostuu seuraavista tiedostoista:
LYHENNE_OPISKELIJAT
LYHENNE_LUKUKAUSI_ILMOITTAUTUMINEN
LYHENNE_OPISKELUOIKEUDET
LYHENNE_OPISKELUOIKEUSJAKSO
LYHENNE_OPINTOSUORITUS_vvvv

Huom: muuttujaluettelossa on mukana kaikki muuttujat (huomioi poimintamahdollisuus muuttujaryhmän mukaan), mutta fyysisesti tiedostot ovat FIONA:ssa erillään. Tiedostot on jaoteltu korkeakoulukohtaisiin kansioihin, jotka voidaan avata tutkimushankkeelle korkeakoulun myöntämän luvan mukaisesti. 

VIRTA-aineisto sisältää seuraavat korkeakoulut ("LYHENNE"-osa yläpuolella olevissa tiedostonimissä)

Tarkempia tietoja aineistosta ja muuttujista VIRTA-opintotietopalvelun sivuilla: https://wiki.eduuni.fi/display/CSCVIRTA/Tietovarannon+tiedot

Aineistossa käytetyt luokitukset löytyvät VIRTA Tietovarannon koodistot-luettelosta:
https://confluence.csc.fi/display/VIRTA/Tietovarannon+koodistot


Tiedoksi tiedostojen- ja aineiston rakenteesta 5.6.2025):
**************************************************************************
1. Opiskelijat -tiedostot
	- Avain on muutettu muotoon opiskelija_avain

2. Opiskeluoikeudet -tiedostot
	- Avain on muutettu muotoon opiskeluoikeus_avain

3. Lukukausi_ilmoittautuminen -tiedostot
	- OpiskelijaAvain on muutettu muotoon opiskelija_avain
	- Opiskeluoikeuden_avain on muutettu muotoon opiskeluoikeus_avain

4. Opiskeluoikeusjakso -tiedostot
	- Avain on muutettu muotoon opiskeluoikeus_avain

5. Opintosuoritus_VVVV -tiedostot
	- Henkilo_avain on muutettu muotoon opiskelija_avain
	- Opiskeluoikeus_Avain on muutettu muotoon opiskeluoikeus_avain
	- Opintosuoritus_avain on poistettu kokonaan toimituksesta.

Muokkauksessa on otettu huomioon korkeakoulujen opiskelijoiden yksilöllinen tunnistaminen.

6. Jatkossa uusi data ajetaan vanhojen tiedostojen päälle.


************************************************************************
LYHENNE / Oppilaitosrekisterin 5-numeroinen koodi / Nimi
************************************************************************
HAMK 02467 Hämeen ammattikorkeakoulu
KARELIA 02469 Karelia-ammattikorkeakoulu
OAMK 02471 Oulun ammattikorkeakoulu
SEAMK 02472 Seinäjoen ammattikorkeakoulu
KAMK 02473 Kajaanin ammattikorkeakoulu
JAMK 02504 Jyväskylän ammattikorkeakoulu
SAMK 02507 Satakunnan ammattikorkeakoulu
TUAMK 02509 Turun ammattikorkeakoulu
ARCADA 02535 Yrkeshögskolan Arcada
CENTRIA 02536 Centria-ammattikorkeakoulu
SAVONIA 02537 Savonia-ammattikorkeakoulu
DIAK 02623 Diakonia-ammattikorkeakoulu
VAMK 02627 Vaasan ammattikorkeakoulu
LAUREA 02629 Laurea-ammattikorkeakoulu
TAMK 02630 Tampereen ammattikorkeakoulu
HUMAK 02631 Humanistinen ammattikorkeakoulu
HAAGAHEL 10056 Haaga-Helia ammattikorkeakoulu
METROPOL 10065 Metropolia ammattikorkeakoulu
NOVIA 10066 Yrkeshögskolan Novia
LAPINAMK 10108 Lapin ammattikorkeakoulu
XAMK 10118 Kaakkois-Suomen ammattikorkeakoulu
LAB 10126 LAB-ammattikorkeakoulu
(SAIMAA 02609 Saimaan ammattikorkeakoulu (vanha))
(LAMK 02470 Lahden ammattikorkeakoulu (vanha))

HY 01901 Helsingin yliopisto        
AA 01903 Åbo Akademi                 
OY 01904 Oulun yliopisto            
TAU 10122 Tamperen yliopisto
JY 01906 Jyväskylän yliopisto        
SHH 01910 Svenska handelshögskolan
VY 01913 Vaasan yliopisto  
LTY 01914 Lappeenrannan-Lahden teknillinen yliopisto LUT
LAY 01918 Lapin yliopisto     
AYO 10076 Aalto yliopisto
ISY 10088 Itä-Suomen yliopisto  
TY 10089 Turun yliopisto
TAIY 10103 Taideyliopisto
(TAY 01905 Tampereen yliopisto (vanha))
(TTY 01915 Tampereen tekn. yliopisto (vanha))

## Muuttujat / Variables (61)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `shnro` | Suojattu henkilönumero | — | — | — |
| `savain` | Suojattu avain | — | — | — |
| `Kirjoihintulopaivamaara` | Kirjoihintulopäivämäärä | — | — | opiskelijat |
| `kunta_koodi` | Asuinkunta | — | — | opiskelijat, opiskeluoikeusjakso |
| `kieli_koodi` | Äidinkieli | — | — | opiskeluoikeusjakso, opiskelijat, opintosuoritus |
| `maan_koodi` | Kansalaisuus | — | — | opiskelijat |
| `patevyys_koodi` | Pätevyys | — | — | opiskelijat |
| `patev_alkpvm` | Pätevyyden alkupäivämäärä | — | — | opiskelijat |
| `koulutusala` | Koulutusala | — | — | opiskeluoikeudet, opintosuoritus |
| `opiskeluoikeuden_tyyppi` | Opiskeluoikeuden tyyppi | — | — | opiskeluoikeudet |
| `Aikuiskoulutus` | Aikuiskoulutus | — | — | opiskeluoikeudet |
| `Siirtopaivamaara` | Siirtopäivämäärä | — | — | opiskeluoikeudet |
| `Lahdejarj_op_oik_tunnus` | Lähdejärjestelmän opiskeluoikeustunnus | — | — | opiskeluoikeudet |
| `Opintojen_aloituspaivamaara` | Opintojen aloituspäivämäärä | — | — | opiskeluoikeudet |
| `Alkamispaivamaara` | Opiontojen alkamispäivämäärä - | — | — | lukukausi_ilmoit, opiskeluoikeudet, opiskeluoikeusjakso |
| `Paattymispaivamaara` | Opintojen päättymispäivämäärä | — | — | opiskeluoikeusjakso, opiskeluoikeudet, lukukausi_ilmoit |
| `Avoimen_vayla` | Avoimen väylä | — | — | opiskeluoikeudet |
| `Maisteriohjelma` | Maisteriohjelma | — | — | opiskeluoikeudet |
| `Laajuus` | Laajuus | — | — | opintosuoritus, opiskeluoikeudet |
| `ens_alkpvm` | Ensisijaisuuden alkamispäivämäärä | — | — | opiskeluoikeudet |
| `ens_paatpvm` | Ensisijaisuuden päättymispäivämäärä | — | — | opiskeluoikeudet |
| `organisaatio` | Organisaatio | — | — | opiskeluoikeudet |
| `org_rooli` | Organisaation rooli | — | — | opiskeluoikeudet |
| `org_osuus` | organisaatio osuus | — | — | opiskeluoikeudet |
| `koulutuskoodi` | Koulutusluokitus | — | — | opiskeluoikeusjakso |
| `rahoituslahde_koodi` | Rahoituslähde | — | — | opiskeluoikeusjakso |
| `Koulutusmoduulitunniste` | Koulutusmoduulin nimi | — | — | opiskeluoikeusjakso, opintosuoritus |
| `Valtakunn_koul_mod_tunniste` | Valtakunnallinen koulutusmoduulitunniste | — | — | opintosuoritus, opiskeluoikeusjakso |
| `opiskelija_avain_s` | suojattu opiskelija avain | — | — | opiskelijat, opintosuoritus, lukukausi_ilmoit |
| `Ilmoittautumispaivamaara` | Ilmoittautumispäivämäärä | — | — | lukukausi_ilmoit |
| `Ylioppilaskunnan_jasen` | Ylioppilaskunnan jäsen | — | — | lukukausi_ilmoit |
| `YTHS_maksu` | YTHS-maksu | — | — | lukukausi_ilmoit |
| `ilmoittautumisen_tila_koodi` | Lukukausi-ilmoittautumisen tila | — | — | lukukausi_ilmoit |
| `ilmoittutumisen_tila_selite` | Lukukausi-ilmoittautumisen tilan selite | — | — | lukukausi_ilmoit |
| `opiskeluoikeus_avain_s` | Opiskeluoikeuden avain | — | — | lukukausi_ilmoit, opintosuoritus, opiskeluoikeudet, opiskeluoikeusjakso |
| `Opiskeluoikeus_Tyyppi` | Opiskeluoikeuden tyyppi | — | — | opintosuoritus |
| `Opiskeluoikeus_Siirtopvm` | Opiskeluoikeuden siirtopäivämäärä | — | — | opintosuoritus |
| `Arvosana` | Arvosana | — | — | opintosuoritus |
| `Arvosana_Asteikko` | Arvosana-asteikko | — | — | opintosuoritus |
| `Tutkinto_Koodi` | Tutkinnon koodi | — | — | opintosuoritus |
| `Opetusharjoittelun_Koodi` | Opetusharjoittelun koodi | — | — | opintosuoritus |
| `Opintosuorituksen_laji` | Opintosuorituksen laji | — | — | opintosuoritus |
| `Koulutusaste` | Koulutusaste | — | — | opintosuoritus |
| `Luokittelu` | Opintosuorituksen luokittelu | — | — | opintosuoritus |
| `Organisaatio_Koodi` | Organisaatiokoodi | — | — | opintosuoritus |
| `Organisaatio_Rooli` | organisaation rooli | — | — | opintosuoritus |
| `Hyvaksilukupaivamaara` | Suorituksen hyväksilukemisen päivämäärä | — | — | opintosuoritus |
| `Opinnaytetyo` | Suoritus opinnäytetyönä | — | — | opintosuoritus |
| `Hankkeistettu` | Suoritus hankkeistettuna | — | — | opintosuoritus |
| `Nimi` | Suorituksen nimi | — | — | opintosuoritus |
| `Opintoviikkolaajuus` | Suorituksen opintoviikkolaajuus | — | — | opintosuoritus |
| `Tki_toiminnan_laajuus` | Tutkimus- ja kehittämistoiminnan laajuus opinnäytetyössä | — | — | opintosuoritus |
| `Tki_harjoittelun_laajuus` | Tutkimus- ja kehittämistoiminnan harjoittelun laajuus | — | — | opintosuoritus |
| `Tki_muut_laajuus` | Tutkimus- ja kehittämistoiminnan muu laajuus | — | — | opintosuoritus |
| `Lisatiedot` | Lisätiedot | — | — | opintosuoritus |
| `Lehtitaso` | Lehtitaso | — | — | opintosuoritus |
| `perustutkinto` | Perustutkinto | — | — | opintosuoritus |
| `patevyys` | Pätevyys | — | — | opiskeluoikeusjakso |
| `patevyys_alkpvm` | Pätevyyden alkamispäivämäärä | — | — | opiskeluoikeusjakso |
| `patevyys_paatpvm` | pätevyyden päättymispäivämäärä | — | — | opiskeluoikeusjakso |
| `suorituspaivamaara` | Suorituksen päivämäärä | — | — | opintosuoritus |

### Muuttujien määritelmät / Variable definitions

#### `shnro` — Suojattu henkilönumero

Suojattu TK:n henkilönumero, joka on sama kaikissa henkilövalmisaineistoissa.

#### `savain` — Suojattu avain

Yksilöivä tunniste eli tunniste, jollaista toista ei ole korkeakoulun omassa rekisterissä. Tyypillisesti rekisteritietojärjestelmän antama yksilöivä tunniste, jonka synonyymeja ovat esimerkiksi "surrogaatti" tai "avain". Suojattu avain yhdistää opintosuoritukset, opiskeluoikeudet ja lukukausi-ilmoittautumiset henkilöön. Suojattua avainta tarvitaan, koska kaikille henkilöillä ei löydy suojattua henkilönumeroa (eli henkilötunnus puuttuu). savain=sHenkiloavain=sopiskelijaavain

Opiskeluoikeudet-tiedosto: sAvain = opiskeluoikeus_avain_s (korkeakoulukohtainen tunniste opiskeluoikeudelle)
Opiskeluoikeusjakso-tiedosto: Savain = opiskeluoikeus_avain_s (korkeakoulukohtainen tunniste opiskeluoikeudelle, tämä siis ei ole opiskelija avain)

#### `Kirjoihintulopaivamaara` — Kirjoihintulopäivämäärä

**Ryhmä / Group:** opiskelijat

Opiskelijan kirjoihintulopäivämäärä korkeakouluun. Yliopistoilla tämä on tyypillisesti ollut se ajanhetki, jolloin opiskelija on saanut ja aloittanut ensimmäisen tutkinnonsuoritusoikeuden ko. yliopistossa. Tieto kerätään erikseen, jotta myös todella vanhojen opiskelijoiden, joilla opiskelu on alkanut esim. ennen sähköisten rekisterien aikaa, kirjoihintulopäivämäärä saadaan paikkansa pitävästi tietoon.

#### `kunta_koodi` — Asuinkunta

**Ryhmä / Group:** opiskelijat, opiskeluoikeusjakso

Henkilön vakituinen asuinkunta Suomessa. Aineistossa käytetty luokitus löytyy Tilastokeskuksen luokituspalvelun kotisivuilta osoitteesta: https://stat.fi/fi/luokitukset. 200=Ulkomaat ja 999=Tuntematon

#### `kieli_koodi` — Äidinkieli

**Ryhmä / Group:** opiskeluoikeusjakso, opiskelijat, opintosuoritus

Henkilön äidinkieli. Aineistossa käytetty luokitus löytyy Tilastokeskuksen luokituspalvelun kotisivuilta osoitteesta: https://stat.fi/fi/luokitukset.

#### `maan_koodi` — Kansalaisuus

**Ryhmä / Group:** opiskelijat

Henkilön viimeisin kansalaisuustieto. Aineistossa käytetty luokitus löytyy Tilastokeskuksen luokituspalvelun kotisivuilta osoitteesta: http://tilastokeskus.fi/luokitukset

#### `patevyys_koodi` — Pätevyys

**Ryhmä / Group:** opiskelijat

Pätevyystiedolla tarkoitetaan sellaista muodollista pätevyyttä, jota korkeakoulun ulkopuolinen viranomainen valvoo tai rekisteröi. 
Luokitus löytyy verkosta sivulla https://confluence.csc.fi/display/VIRTA/Tietovarannon+koodistot#Tietovarannonkoodistot-Pätevyys,Behörighet

#### `patev_alkpvm` — Pätevyyden alkupäivämäärä

**Ryhmä / Group:** opiskelijat

Pätevyyden alkupäivämäärä.

#### `koulutusala` — Koulutusala

**Ryhmä / Group:** opiskeluoikeudet, opintosuoritus

Tutkintolajisille opintosuorituksille ja tutkintoon johtaville opiskeluoikeuksille koulutusalatieto ilmoitetaan Koulutusluokitus-koodistolla. Koulutuskoodi pitää sisällään tiedon koulutusalasta. Vuoden 2016 tiedoista lähtien on otettu käyttöön Opetus- ja kulttuuriministeriön korkeakoulujen ohjauksen alojen mukainen koodisto (OKM:n ohjauksen ala), joka korvaa molemmilla korkeakoulusektoreilla aiemmin käytössä olleet koulutusala 2002 ja opintoala 1995 koodistojen käytön. 
Luokitus:
1 Kasvatusalat
2 Taiteet ja kulttuurialat
3 Humanistiset alat
4 Yhteiskunnalliset alat
5 Kauppa, hallinto ja oikeustieteet
6 Luonnontieteet
7 Tietojenkäsittely ja tietoliikenne
8 Tekniikan alat
9 Maa- ja metsätalousalat
10 Lääketieteet
11 Terveys- ja hyvinvointialat
12 Palvelualat

#### `opiskeluoikeuden_tyyppi` — Opiskeluoikeuden tyyppi

**Ryhmä / Group:** opiskeluoikeudet

Opiskeluoikeudella voi olla koko olemassaolonsa aikana vain yksi opiskeluoikeuden tyyppi. Korkeakoulujen valtakunnalliseen tietovarantoon on pakollista tuoda ne opiskeluoikeudet, jotka liittyvät tutkintoon johtavaan koulutukseen (1-7, pl. 5), erilliseen opettajankoulutukseen (14-15) ja ammattikorkeakoulujen erikoistumisopintoihin (12). 1 Ammattikorkeakoulututkinto  2 Alempi korkeakoulututkinto  3 Ylempi ammattikorkeakoulututkinto   4 Ylempi korkeakoulututkinto   5 Lääkärien erikoistumiskoulutus    6 Lisensiaatintutkinto   7 Tohtorintutkinto   8 Kotimainen opiskelijaliikkuvuus. Korkeakoulujen välisiin sopimuksiin perustuva kotimainen opiskelijaliikkuvuus. 9 Kansainvälinen vaihto. Liikkuva opiskelija suorittaa kokonaista korkeakoulututkintoa (perus- tai jatkotutkintoa) ulkomailla ja suorittaa osan opinnoistaan niin, että Suomessa suoritetut opinnot luetaan hyväksi tutkintoon. 10 Täydennyskoulutus. Opiskeluoikeuden tyyppi on täydennyskoulutus, kun oppija täydentää aiemmin hankittua osaamistaan opinnoilla, jotka eivät tuota pätevyyttä. 11 Pätevöitymiskoulutus. Poistuva opiskeluoikeuden tyyppi, ei käytetä enää vuoden 2018 tiedoista alkaen. Pätevyystiedot tuodaan VIRTAan pätevyyskoodiston arvoina. 12 Erikoistumisopinnot. Ammatilliset erikoistumisopinnot ovat ammattikorkeakoulututkintoon pohjautuvia täydennyskoulutusohjelmia, joiden laajuus on 30-60 opintopistettä. 13 Avoimen opinnot. Opiskeluoikeuden tyyppi on avoimet opinnot, kun oppija suorittaa tutkintoon johtamatonta koulutusta avoimessa yliopistossa tai ammattikorkeakoulussa. 14 Opettajan pedagogiset opinnot. Opiskeluoikeuden tyyppi on opettajan pedagogiset opinnot, kun oppija suorittaa opettajan pedagogisia opintoja erillisopintoina. 15 Ammatillinen opettajankoulutus. Opiskeluoikeuden tyyppi on ammatillinen opettajankoulutus, kun oppija suorittaa ammatillista opettajankoulutusta erillisinä opintoina. 16 Oppisopimus-tyyppinen koulutus. Opiskeluoikeuden tyyppi on korkeakoulutettujen oppisopimustyyppistä täydennyskoulutusta. 17 Valmentava koulutus. Opiskeluoikeuden tyyppi on valmentava koulutus, kun oppija suorittaa esim. maahanmuuttajien valmentavaa koulutusta. 18 Erillisoikeus. Opiskeluoikeuden tyyppi on erillinen opiskeluoikeus, kun korkeakoulu on myöntänyt oppijalle ajallisesti ja sisällöllisesti rajatun oikeuden suorittaa tietyn koulutuksen (opintojakson tai -kokonaisuuden) ilman tutkinnonsuorittamisoikeutta. Tutkintoon johtamattomat opiskeluoikeudet, jotka eivät kategorisoidu muihin opiskeluoikeuden tyyppeihin, saavat myös erillinen opiskeluoikeus -koodiarvon. 19 Erikoistumiskoulutus. Opiskeluoikeuden tyyppi on erikoistumiskoulutus.

#### `Aikuiskoulutus` — Aikuiskoulutus

**Ryhmä / Group:** opiskeluoikeudet

Tarkentaa Opiskeluoikeuden tyyppi -koodiston arvoa 1 Ammattikorkeakoulututkinto. Jos opiskeluoikeus on tyyppiä ammattikorkeakoulututkinto ja tätä arvoa A Aikuiskoulutus ei ole tuotu, on kyseessä nuorten koulutus.

#### `Siirtopaivamaara` — Siirtopäivämäärä

**Ryhmä / Group:** opiskeluoikeudet

#### `Lahdejarj_op_oik_tunnus` — Lähdejärjestelmän opiskeluoikeustunnus

**Ryhmä / Group:** opiskeluoikeudet

#### `Opintojen_aloituspaivamaara` — Opintojen aloituspäivämäärä

**Ryhmä / Group:** opiskeluoikeudet

#### `Alkamispaivamaara` — Opiontojen alkamispäivämäärä -

**Ryhmä / Group:** lukukausi_ilmoit, opiskeluoikeudet, opiskeluoikeusjakso

#### `Paattymispaivamaara` — Opintojen päättymispäivämäärä

**Ryhmä / Group:** opiskeluoikeusjakso, opiskeluoikeudet, lukukausi_ilmoit

#### `Avoimen_vayla` — Avoimen väylä

**Ryhmä / Group:** opiskeluoikeudet

Opiskeluoikeus myönnetty avoimen opintojen perusteella.

#### `Maisteriohjelma` — Maisteriohjelma

**Ryhmä / Group:** opiskeluoikeudet

#### `Laajuus` — Laajuus

**Ryhmä / Group:** opintosuoritus, opiskeluoikeudet

#### `ens_alkpvm` — Ensisijaisuuden alkamispäivämäärä

**Ryhmä / Group:** opiskeluoikeudet

Päivämäärä, josta alkaen opinto-oikeuden ensisijaisuus on voimassa.

#### `ens_paatpvm` — Ensisijaisuuden päättymispäivämäärä

**Ryhmä / Group:** opiskeluoikeudet

Päivämäärä, jolloin opinto-oikeuden ensisijaisuus päättyy.

#### `organisaatio` — Organisaatio

**Ryhmä / Group:** opiskeluoikeudet

Organisaation koodistona toimii Tilastokeskuksen Oppilaitosrekisteri laajennettuna eräillä muilla arvoilla. Laajennusarvot koostuvat pääasiassa Tilastokeskuksen oppilaitostyyppiluokituksen arvoista.Laajennusarvoja on tarkoitus käyttää vain, mikäli varsinaista oppilaitosrekisterin oppilaitostietoa ei ole mahdollista antaa. Tilastokeskuksen Oppilaitosrekisteriä on laajennettu vain alla näkyvillä arvoilla. 42 Yliopistot, 
41 Ammattikorkeakoulut, 
64 Kansalaisopistot Kansalais- ja työväenopistot. Avoin yliopisto-opetus -tiedonkeruu, 
63 Kansanopistot Avoin yliopisto-opetus -tiedonkeruu.  
66 Kesäyliopistot Avoin yliopisto-opetus -tiedonkeruu.
99 Muut oppilaitokset . 
UK Ulkomainen korkeakoulu Hyväksilukemisen lähteenä. 
UM Ulkomainen muu oppilaitos . 
XX Muodollisen koulutuksen ulkopuolella . 

Tilastokeskuksen Oppilaitosrekisteri löytyy Tilastokeskuksen sivustolta osoitteesta: http://www.stat.fi/tup/oppilaitosrekisteri/index.html. Tilastossa käytetyt luokitukset löytyvät Tilastokeskuksen luokitus- ja metatietopalvelujen kotisivuilta osoitteesta: https://stat.fi/fi/luokitukset.

#### `org_rooli` — Organisaation rooli

**Ryhmä / Group:** opiskeluoikeudet

Organisaation rooli liittyy tilanteeseen, jossa varsinainen organisaatiotieto liittyy johonkin toiseen tietoon ja liitokseen liittyen on jokin rooli. 1 = Myöntävä. Ilmaisee sitä organisaatiota, jonka omistamasta tiedosta on kyse. 2 = Järjestävä. Ilmaisee sitä organisaatiota, joka on osallistunut kyseenomaisen tiedon syntymisen järjestämiseen tai toteuttamiseen. 3 = Lähde. Ilmaisee sitä organisaatiota, joka on kyseenomaisen tiedon syntymisen alkuperäinen lähde. 4 = Kohde. Ilmaisee sitä organisaatiota, jonka kyseenomaiseen tietoon liittyen on olemassa liikkuvuutta/siirtyvyyttä ja tässä ilmoitettava organisaatio on siirtymisen kohde. 9 = Tuntematon.

#### `org_osuus` — organisaatio osuus

**Ryhmä / Group:** opiskeluoikeudet

#### `koulutuskoodi` — Koulutusluokitus

**Ryhmä / Group:** opiskeluoikeusjakso

Koulutusluokitus on tutkintoon johtavan koulutuksen yhteismitallisuuden tärkein luokitteleva tekijä korkeakoulujen valtakunnallisen tietovarannon käyttöönoton myötä. Koulutusluokitusta ylläpitää Tilastokeskus. Korkeakoulujen vastuulla on Tilastokeskuksen ohjeiden mukaisesti luokitella koulutusluokituksen koodiarvoilla tutkintoon johtavan koulutuksen opiskeluoikeudet ja tutkintolajiset opintosuoritukset. Mahdollisesti tarpeellisia uusia koodiarvoja koulutusluokitukseen määritellään Tilastokeskuksen johdolla yhteistyössä korkeakoulujen sekä opetus- ja kulttuuriministeriön kesken osana korkeakoulujen tietomallin ja korkeakoulujen valtakunnallisen tietovarannon ylläpitoa.  Luokitus on käytettävissä tutkintolajisille opintosuorituksille ja tutkintoon johtavan koulutuksen opiskeluoikeuksille. Muille opintosuorituksille ja opiskeluoikeuksille käytetään Koulutusala-koodistoa tai Opintoala-koodistoa.

 Koulutusluokitus: <http://www.stat.fi/meta/luokitukset/koulutus/>

#### `rahoituslahde_koodi` — Rahoituslähde

**Ryhmä / Group:** opiskeluoikeusjakso

Rahoituslähde. 
1 = Perusrahoitus on Opetushallinnon (tai ammattikorkeakoulun) rahoittama koulutus
2 = ESR-rahoitus, vain ammattikorkeakoulukoulutus, on kokonaan (ml. kansallinen osuus) ESR-rahoituksella tai muulla rakennerahastorahoituksella järjestettävä tutkintoon johtava koulutus 
3 = TE-rahoitus, vain ammattikorkeakoulukoulutus, on työvoimahallinnon ostama AMK-tutkintoon johtava koulutus 
4 = Maksullinen tilauskoulutus. Yo-tiedonkeruussa "2" Käytetään lain 1600/2015 9 §:n ja lain 1601/2015 13 §:n mukaisista koulutuksista 5 = Lukukausimaksuvelvollinen (1.8.2017 lähtien). Yo-tiedonkeruussa "1". Huom. Tätä koodia käytetään myös lain 1600/2015 10 §:n ja lain 1601/2015 13 a §:n koulutuksista.

#### `Koulutusmoduulitunniste` — Koulutusmoduulin nimi

**Ryhmä / Group:** opiskeluoikeusjakso, opintosuoritus

Korkeakoulun anatama koulutusmoduulitunniste

#### `Valtakunn_koul_mod_tunniste` — Valtakunnallinen koulutusmoduulitunniste

**Ryhmä / Group:** opintosuoritus, opiskeluoikeusjakso

Tuleva valtakunnallinen koulutusmoduulitunniste.

#### `opiskelija_avain_s` — suojattu opiskelija avain

**Ryhmä / Group:** opiskelijat, opintosuoritus, lukukausi_ilmoit

savain=sHenkiloavain=sopiskavain

#### `Ilmoittautumispaivamaara` — Ilmoittautumispäivämäärä

**Ryhmä / Group:** lukukausi_ilmoit

Päivämäärä, jolloin lukukausi-ilmoittautuminen on tehty.

#### `Ylioppilaskunnan_jasen` — Ylioppilaskunnan jäsen

**Ryhmä / Group:** lukukausi_ilmoit

#### `YTHS_maksu` — YTHS-maksu

**Ryhmä / Group:** lukukausi_ilmoit

YTHS-maksutieto kerätään pakollisena kaikista korkeakouluista, joiden opiskelijoilla YTHS-maksu on käytössä.

#### `ilmoittautumisen_tila_koodi` — Lukukausi-ilmoittautumisen tila

**Ryhmä / Group:** lukukausi_ilmoit

Lukukausi-ilmoittautumisen tilatieto tarkentaa opiskeluoikeuden tilakoodia "aktiivinen". Aktiivisten opiskeluoikeusjaksojen koko ajalta tulee olla tallennettuna myös lukukausi-ilmoittautumistieto. Lukukausi-ilmoittautumisen laiminlyöminen voi johtaa opiskeluoikeuden menettämiseen (opiskeluoikeuden tila -koodistossa arvo ”passivoitu”). Lukukausi-ilmoittautumisen tila kohdistuu lukukausi-ilmoittautumiseen, joka liittyy joko opiskelijaan (kyseessä korkeakouluun ja opiskelijaan liitetty tieto) tai yksittäiseen opiskeluoikeuteen (kyseessä korkeakouluun, opiskelijaan ja opiskeluoikeuteen liitetty tieto). Lukukausi-ilmoittautumisen tilatieto voi vaihtua kesken lukukauden. 1 = Läsnä. Lukukausi-ilmoittautumisen tila on läsnä silloin, kun opiskelija on ilmoittautunut korkeakoulun prosessin mukaisesti läsnäolevaksi opiskelijaksi. 2 = Poissa. Lukukausi-ilmoittautumisen tila on poissa silloin, kun opiskelija on ilmoittautunut korkeakoulun prosessin mukaisesti poissaolevaksi opiskelijaksi ja poissaolon syy on muu kuin koodin 3 mukainen lakisääteinen syy. 3 = Poissa, ei kuluta opintoaikaa. Lukukausi-ilmoittautumisen tila ”poissa, ei kuluta opintoaikaa” koskee sekä ammattikorkeakoulujen että yliopistojen opiskeluoikeutta rajaavissa laeissa määriteltyä poissaoloa, jossa poissaolon syynä on asevelvollisuuslain, siviilipalveluslain tai naisten vapaaehtoisesta asepalveluksesta annetun lain mukaisen palvelun suorittaminen tai äitiys-, isyys- tai vanhempainvapaan pitäminen. 4 = Puuttuu. Lukukausi-ilmoittautumisen tila on voitu kirjata koodiarvolle puuttuu silloin kun opiskeluoikeuteen on liitetty lukukausitieto, mutta ilmoittautumistietoa ei ole (null) tai se on merkitty puuttuvaksi.

#### `ilmoittutumisen_tila_selite` — Lukukausi-ilmoittautumisen tilan selite

**Ryhmä / Group:** lukukausi_ilmoit

#### `opiskeluoikeus_avain_s` — Opiskeluoikeuden avain

**Ryhmä / Group:** lukukausi_ilmoit, opintosuoritus, opiskeluoikeudet, opiskeluoikeusjakso

#### `Opiskeluoikeus_Tyyppi` — Opiskeluoikeuden tyyppi

**Ryhmä / Group:** opintosuoritus

Opiskeluoikeudella voi olla koko olemassaolonsa aikana vain yksi opiskeluoikeuden tyyppi. Korkeakoulujen valtakunnalliseen tietovaranto sisältää ne opiskeluoikeudet, jotka liittyvät tutkintoon johtavaan koulutukseen (1-7, pl. 5), erilliseen opettajankoulutukseen (14-15) ja ammattikorkeakoulujen erikoistumisopintoihin (12).

1 Ammattikorkeakoulututkinto tutkinto
2 Alempi korkeakoulututkinto tutkinto 
3 Ylempi ammattikorkeakoulututkinto tutkinto 
4 Ylempi korkeakoulututkinto tutkinto 
5 Lääkärien erikoistumiskoulutus 
6 Lisensiaatintutkinto tutkinto 
7 Tohtorintutkinto tutkinto 
8 Korkeakoulujen välisiin sopimuksiin perustuva kotimainen opiskelijaliikkuvuus.
9 Kansainvälinen vaihto Liikkuva opiskelija suorittaa kokonaista korkeakoulututkintoa (perus- tai jatkotutkintoa) ulkomailla ja suorittaa osan opinnoistaan niin, että Suomessa suoritetut opinnot luetaan hyväksi tutkintoon. 
10 Täydennyskoulutus . 
11 Pätevöitymiskoulutus Huom! Tätä opiskeluoikeuden tyyppiä ei käytetä enää vuoden 2018 tiedoista alkaen. Pätevyystiedot tuodaan VIRTAan pätevyyskoodiston arvoina.
12 Erikoistumisopinnot. Ammatilliset erikoistumisopinnot ovat ammattikorkeakoulututkintoon pohjautuvia täydennyskoulutusohjelmia, joiden laajuus on 30-60 opintopistettä. 
13 Avoimen opinnot  
14 Opettajan pedagogiset opinnot. Oppija suorittaa opettajan pedagogisia opintoja erillisopintoina. 
15 Ammatillinen opettajankoulutus. Oppija suorittaa ammatillista opettajankoulutusta erillisinä opintoina. 16 Korkeakoulutettujen oppisopimustyyppistä täydennyskoulutusta 
17 Valmentava koulutus. Esim kun oppija suorittaa maahanmuuttajien valmentavaa koulutusta. 
18 Erillisoikeus. Korkeakoulu on myöntänyt oppijalle ajallisesti ja sisällöllisesti rajatun oikeuden suorittaa tietyn koulutuksen (opintojakson tai -kokonaisuuden) ilman tutkinnonsuorittamisoikeutta.
19 Erikoistumiskoulutus

#### `Opiskeluoikeus_Siirtopvm` — Opiskeluoikeuden siirtopäivämäärä

**Ryhmä / Group:** opintosuoritus

#### `Arvosana` — Arvosana

**Ryhmä / Group:** opintosuoritus

Suorituksen arvosana.
Viisiportainen: HYV hyväksytty, 1,   2,   3,   4,   5,
Hyväksytty: HYV hyväksytty, 
Toinen kotimainen: TT tyydyttävät tiedot,  HT hyvät tiedot, 
Näytetyö HYV hyväksytty,  KH kiittäen hyväksytty 
Tutkielma: A approbatur, B lubenter approbatur, N non sine laude approbatur, C cum laude approbatur, M magna cum laude approbatur, E eximia cum laude approbatur, L laudatur 
EiKaytossa: Arvosana ei kaytossa 

Muu-arvosana-asteikon

#### `Arvosana_Asteikko` — Arvosana-asteikko

**Ryhmä / Group:** opintosuoritus

Käytetty arvosana-asteikko.
Viisiportainen
Hyväksytty
Tutkielma
Ei käytössä
 Muu

#### `Tutkinto_Koodi` — Tutkinnon koodi

**Ryhmä / Group:** opintosuoritus

Tilastokeskuksen koulutusluokituksen mukainen koodi.

#### `Opetusharjoittelun_Koodi` — Opetusharjoittelun koodi

**Ryhmä / Group:** opintosuoritus

tietoa ei kerätä

#### `Opintosuorituksen_laji` — Opintosuorituksen laji

**Ryhmä / Group:** opintosuoritus

Opintosuorituksen laji. 1 = Tutkinto. Opintosuoritus on tutkinnon suoritus. Tiedon perusteella päättyneestä opiskeluoikeudesta tiedetään, että opiskeluoikeus on päättynyt valmistumiseen. 2 = Muu opintosuoritus 3 = Ei huomioitava. Väliaikainen suoritustieto joka on ositettu tiedonkeruujaksolle myöhemmin syntyvästä suorituksesta. "Osasuoritus" vain Kelaa varten. 4 = Oppilaitoksen sisäinen. Väliaikainen suoritustieto, jota voidaan käyttää opintosuorituksen sisäiseen tiedon tallentamiseen lähinnä opettajan tarpeisiin. Ei huomioida suoritusotteella.

#### `Koulutusaste` — Koulutusaste

**Ryhmä / Group:** opintosuoritus

#### `Luokittelu` — Opintosuorituksen luokittelu

**Ryhmä / Group:** opintosuoritus

Opintosuoritus voi saada opintosuorituksen luokittelu -koodistosta nolla, yksi tai monta luokittelevaa arvoa. 1 = Suoritus on avoimessa korkeakouluopetuksessa suoritettu 2 = Suoritus on saapuvan kansainvälisen vaihto-opiskelijan suorittama 3 = Suoritus on korkeakoulujen välisillä yhteistyösopimuksilla opiskelevan suorittama 4 = Suoritus on erillisellä opiskeluoikeudella opiskelevan suorittama 5 = Suoritus on erillisellä opiskeluoikeudella opettajankoulutuksen opintoja suorittavan opiskelijan suorittama 6 = Suoritus on maahanmuuttajien valmentavassa koulutuksessa opiskelevan suorittama 7 = Suoritus on kotimainen harjoittelu 8 = Suoritus on ulkomainen harjoittelu 9 = Suoritus on kansainvälinen yhteistutkinto 10 = Suoritus on kansainvälinen kaksoistutkinto 11 = Suoritus on erikoistumiskoulutuksessa suoritettu 12 = Suoritus on korkeakoulujen välisillä yhteistyösopimuksilla opiskelevan suorittama ja kirjattu varsinaisena suorituksena opiskelijan kotikorkeakoulussa 13 = Opintosuoritus on täydennyskoulutuksessa suoritettu 14 = Suoritus on suomi/ruotsi vieraana kielenä 15 = Suoritus sisältää kotimaista harjoittelua

#### `Organisaatio_Koodi` — Organisaatiokoodi

**Ryhmä / Group:** opintosuoritus

Organisaation koodistona toimii Tilastokeskuksen Oppilaitosrekisteri laajennettuna eräillä muilla arvoilla. Laajennusarvot koostuvat pääasiassa Tilastokeskuksen oppilaitostyyppiluokituksen arvoista.Laajennusarvoja on tarkoitus käyttää vain, mikäli varsinaista oppilaitosrekisterin oppilaitostietoa ei ole mahdollista antaa. Tilastokeskuksen Oppilaitosrekisteriä on laajennettu vain alla näkyvillä arvoilla. 42 Yliopistot, 
41 Ammattikorkeakoulut, 
64 Kansalaisopistot Kansalais- ja työväenopistot. Avoin yliopisto-opetus -tiedonkeruu, 
63 Kansanopistot Avoin yliopisto-opetus -tiedonkeruu.  
66 Kesäyliopistot Avoin yliopisto-opetus -tiedonkeruu.
99 Muut oppilaitokset . 
UK Ulkomainen korkeakoulu Hyväksilukemisen lähteenä. 
UM Ulkomainen muu oppilaitos . 
XX Muodollisen koulutuksen ulkopuolella . 

Tilastokeskuksen Oppilaitosrekisteri löytyy Tilastokeskuksen sivustolta osoitteesta: http://www.stat.fi/tup/oppilaitosrekisteri/index.html. Tilastossa käytetyt luokitukset löytyvät Tilastokeskuksen luokitus- ja metatietopalvelujen kotisivuilta osoitteesta: https://stat.fi/fi/luokitukset.

#### `Organisaatio_Rooli` — organisaation rooli

**Ryhmä / Group:** opintosuoritus

Organisaation rooli liittyy tilanteeseen, jossa varsinainen organisaatiotieto liittyy johonkin toiseen tietoon ja liitokseen liittyen on jokin rooli. 1 = Myöntävä. Ilmaisee sitä organisaatiota, jonka omistamasta tiedosta on kyse. 2 = Järjestävä. Ilmaisee sitä organisaatiota, joka on osallistunut kyseenomaisen tiedon syntymisen järjestämiseen tai toteuttamiseen. 3 = Lähde. Ilmaisee sitä organisaatiota, joka on kyseenomaisen tiedon syntymisen alkuperäinen lähde. 4 = Kohde. Ilmaisee sitä organisaatiota, jonka kyseenomaiseen tietoon liittyen on olemassa liikkuvuutta/siirtyvyyttä ja tässä ilmoitettava organisaatio on siirtymisen kohde. 9 = Tuntematon.

#### `Hyvaksilukupaivamaara` — Suorituksen hyväksilukemisen päivämäärä

**Ryhmä / Group:** opintosuoritus

Suorituksen hyväksilukemisen päivämäärä on tieto siitä, milloin opintosuoritus on hyväksytty tai kirjattu kyseisen korkeakoulun rekisteriin. Hyväksilukemisen päivämäärä on hyväksiluvun tekevän korkeakoulun hallinnollisen päätöksen päivämäärä eli hyväksiluvun tuloksena uuden suorituksen rekisteriinsä myöntävän korkeakoulun toimenpide.

#### `Opinnaytetyo` — Suoritus opinnäytetyönä

**Ryhmä / Group:** opintosuoritus

Opintosuoritus on suoritettu opinnäytetyönä.

#### `Hankkeistettu` — Suoritus hankkeistettuna

**Ryhmä / Group:** opintosuoritus

Opintosuoritus on suoritettu hankkeistettuna.

#### `Nimi` — Suorituksen nimi

**Ryhmä / Group:** opintosuoritus

Opintosuorituksen nimi.

#### `Opintoviikkolaajuus` — Suorituksen opintoviikkolaajuus

**Ryhmä / Group:** opintosuoritus

Opintoviikkolaajuus on lisätiedon omainen erillinen tieto, joka voi olla suorituksella opintopistelaajuuden lisäksi.

#### `Tki_toiminnan_laajuus` — Tutkimus- ja kehittämistoiminnan laajuus opinnäytetyössä

**Ryhmä / Group:** opintosuoritus

Tutkimus- ja kehittämistoiminnan (TKI) laajuus opinnäytetyössä.

#### `Tki_harjoittelun_laajuus` — Tutkimus- ja kehittämistoiminnan harjoittelun laajuus

**Ryhmä / Group:** opintosuoritus

Tutkimus- ja kehittämistoiminnan (TKI) harjoittelun laajuus.

#### `Tki_muut_laajuus` — Tutkimus- ja kehittämistoiminnan muu laajuus

**Ryhmä / Group:** opintosuoritus

Tutkimus- ja kehittämistoiminnassa (TKI) suoritetut opintopisteet, jotka eivät kuulu harjoitteluun tai opinnäytetyöhön.

#### `Lisatiedot` — Lisätiedot

**Ryhmä / Group:** opintosuoritus

Suorituksen mahdolliset, vain julkiset lisätiedot.

#### `Lehtitaso` — Lehtitaso

**Ryhmä / Group:** opintosuoritus

#### `perustutkinto` — Perustutkinto

**Ryhmä / Group:** opintosuoritus

#### `patevyys` — Pätevyys

**Ryhmä / Group:** opiskeluoikeusjakso

Pätevyystiedolla tarkoitetaan sellaista muodollista pätevyyttä, jota korkeakoulun ulkopuolinen viranomainen valvoo tai rekisteröi. 
Luokitus löytyy verkosta sivulla https://confluence.csc.fi/display/VIRTA/Tietovarannon+koodistot#Tietovarannonkoodistot-Pätevyys,Behörighet

#### `patevyys_alkpvm` — Pätevyyden alkamispäivämäärä

**Ryhmä / Group:** opiskeluoikeusjakso

#### `patevyys_paatpvm` — pätevyyden päättymispäivämäärä

**Ryhmä / Group:** opiskeluoikeusjakso

#### `suorituspaivamaara` — Suorituksen päivämäärä

**Ryhmä / Group:** opintosuoritus

Opintosuorituksen päivämäärä

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
