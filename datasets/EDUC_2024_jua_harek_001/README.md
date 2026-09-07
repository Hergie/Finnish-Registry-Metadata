# EDUC_HAREK Korkeakoulujen hakutiedot, 2024

- **Identifier:** `EDUC_2024_jua_harek_001.xml`
- **DOI:** `khak_2017-10_2017-10-05_ain_0001`
- **Temporal coverage:** 2024-01-01 - 2024-12-31
- **Published:** 2026-09-01
- **Organisation:** Tilastokeskus
- **Variable count:** 79
- **Observation count:** —
- **Population:** korkeakouluhakijat, jotka ovat hakeneet aineistovuonna alkavaan koulutukseen
- **Source:** Aineisto opiskelijavalinnoista perustuu Opetushallituksen ylläpitämään opiskelijavalintarekisteriin (sis. yliopistojen hakija- ja opinto-oikeusrekisterin, ammattikorkeakoulujen yhteishakurekisterin, ja korkeakoulujen hakurekisterin tiedot ajankohdan mukaisesti), jonka OPH toimittaa Tilastokeskukselle vuosittain. Aineistovuonna 2024 lähdeaineisto on vaihtunut Ovaraan.
- **Related:** <a href= "https://stat.fi/tilasto/khak#contacts">Tilatotieto: Koulutukseen hakeutuminen</a>
- **Keywords:** koulutus,oppilaitokset

## Description

EDUC_HAREK-valmisaineisto sisältää hakurekisterin tietoja mm. korkeakouluhaun kohteesta, hakemuksesta ja hakijasta sekä taustatiedoista karkealla tasolla.

Aineisto on osa EDUC_HAREK -moduulia korkeakoulujen hakurekisteritiedoista 1992-2024. Tämä aineistokuvaus sisältää korkeakoulujen (sekä yliopistojen että ammattikorkeakoulujen) kalenterivuonna alkaneeseen koulutukseen hakeneiden tietoja vuodesta 2024 alkaen, siltä osin kun tiedot on toimitettu Tilastokeskukseen tilastointia varten. Tiedot pohjautuvat Opetushallituksen ylläpitämään Opiskelijavalinnan raportointipalvelu Ovaraan.


<b>Valmisaineiston tarkentava nimi</b>
Korkeakoulujen hakurekisteritiedot, sisältäen tietoja korkeakouluhaun kohteesta, hakemuksesta ja hakijasta sekä taustatiedoista karkealla tasolla.


<b>Aineiston perusjoukko, koostaminen ja tietolähteet</b>
EDUC_HAREK-valmisaineisto perustuu Opetushallituksen ylläpitämään opiskelijavalintarekisteriin (sis. yliopistojen hakija- ja opinto-oikeusrekisterin, ammattikorkeakoulujen yhteishakurekisterin ja korkeakoulujen hakurekisterin tiedot ajankohdan mukaisesti). Vuoden 2024 aineistolle lähdeaineistoksi on vaihtunut Opetushallituksen ylläpitämä Opiskelijavalinnan raportointipalvelu Ovara. Tilastokeskukselle toimitettujen tietojen kattavuus vaihtelee ajanjaksoittain, ja Tilastokeskus on täydentänyt aineistoa tilastotuotannon yhteydessä. Hakeneilla ja korkeakouluihin hyväksytyillä tarkoitetaan henkilöitä, jotka ovat saaneet hyväksymiskirjeen kyseisenä hakuvuonna 15.9. mennessä.

Aineistovuoden 2024 aineistossa henkilö on usealla rivillä valintatapajonon, haun, hakemuksen ja hakutoiveen mukaan. Valinnan tilaa kuvaavat muuttujat (valinnan_tila ja valinnan_tila_tk) kertovat, mikä hakukohteen valintatapajonoista on se, johon hakija on päässyt, mikäli hän on tullut valituksi hakukohteeseen.
 

<b>Huomioitavaa aineistosta ja sen käytöstä</b>
Aineistosta on salattu henkilön tunnistetiedot, ja lisäksi on suojattu muun muassa kaikkien hakukohteiden ja oppilaitosten tunnistetiedot sekä haun ja hakemuksen yksilöivät oid-tunnisteet. Aineiston tiedot on linkitettävissä muiden henkilövalmisaineistomoduulien kanssa suojatun henkilönumeron (hid_e) avulla. Huomaathan, että hakijoille, joille ei ole suomalaista henkilötunnusta, ei olla voitu muodostaa suojattua henkilönumeroa. Vuoden 2024 aineisto sisältää suojatun henkilö-OID-muuttujan (henkilo_oid_s), jota voidaan hyödyntää muihin OPH:n rekisteriaineistoihin pohjautuviin valmisaineistoihin, kuten KOSKI. Huomaathan, että osalle hakijoista ei olla pystytty muodostamaan hid_e- eikä henkilo_oid_s-muuttujaa, ja näiden hakijoiden määrä vaihtelee huomattavasti eri vuosina.

Muutokset lähdeaineistossa ovat vaikuttaneet aineistovuoden 2024 aineiston rakenteeseen: hakijan haku yksittäiseen hakukohteeseen voi esiintyä usealla rivillä, mikäli hakukohteeseen on useampi valintatapajono, esimerkiksi todistus- tai pääsykoevalinta. Hakijan hakukohteen rivit edustavat siis hakijan hakukohteen erillisiä valintatapajonoja. Muuttujat valinnan_tila ja valinnan_tila_tk edustavat yksittäisen valintatapajonon valinnan tilaa ja valintatieto-muuttuja kokoaa yhteen hakukokohteen valintatuloksen hakijalle. Muuttuja hyvaksytty_ensikertalainen_haki kuvaa valintatapajono-tason tietoa hyväksytystä ensikertalaisesta hakijasta.
 
Ennen vuotta 2015 hakurekistertiedot on saatavilla erikseen yliopistoille ja ammattikorkeakouluille. Yliopistojen osalta tiedostot alkavat vuodesta 1992 ja ammattikorkeakoulujen osalta vuodesta 1996. Näiden aineistojen muuttujasisällöt vaihtelevat merkittäväst sekä ajallisesti että keskenään, ja ne poikkeavat huomattavasti nykyisestä tietosisällöstä.

Yhdistettyjen korkeakoulujen hakurekisteritiedot ovat saatavilla vuosilta 2015–2024. Näiltä vuosilta aineisto sisältää pääosin yhtenäisen muuttujasisällön, mutta myös tämän kokonaisuuden sisällä esiintyy eroavaisuuksia: kaikki muuttujat eivät ole saatavilla koko aikaväliltä, ja muuttujien käytössä on huomioitava tietojen rajoittuneisuus ja mahdollset puutteet.

Huom. maanpuolustuskorkeakoulun hakijat on poistettu aineistosta.

EDUC-HAREK -moduuli on ryhmitelty seuraaviin kokonaisuuksiin, joilla jokaisella on oma Taika-kuvauksensa:
* ammattikorkeakoulujen hakurekisteritiedot 1996-1999
* ammattikorkeakoulujen hakurekisteritiedot 2000-2004
* ammattikorkeakoulujen hakurekisteritiedot 2005-2014
* yliopistojen hakurekisteritiedot 1992-1998
* yliopistojen hakurekisteritiedot 1999-2003
* yliopistojen hakurekisteritiedot 2004-2009
* yliopistojen hakurekisteritiedot 2010-2014
* yhdistetyt korkeakoulujen hakurekisteritiedot 2015–2023
* yhdistetyt korkeakoulujen hakurekisteritiedot (Ovara) 2024

Kunkin osakokonaisuuden kuvauksesta löytyy tarkempaa tietoa tietosisällöstä. Kaikkien tietojen oikeellisuutta ei kuitenkaan ole voitu varmistaa. Huomioithan, että muuttujakuvauksissa on voitu dokumentoida muutoksia muuttujien sisällöistä eri aikajaksojen aikana sekä huomioita, jotka liittyvät muuttujien käyttöön.

EDUC-HAREK -moduulin aineisto koostuu erillisistä vuositiedostoista:
- EDUC_HAREK_amkhaku_VVVV, jossa VVVV = 1996, ..., 2014.
- EDUC_HAREK_yohaku_VVVV, jossa VVVV = 1992, ..., 2014.
- EDUC_HAREK_kkhaku_VVVV, jossa VVVV = 2015, ..., 2024.
Tiedostot sisältävät nimiensä mukaisesti ammattikorkeakoulujen, yliopistojen ja yhdistettyjä korkeakoulujen hakurekisteritietoja niiltä vuosilta, joilta aineistoa on saatavilla.

Vuodesta 2022 eteenpäin shetu-muuttujaa ei olla voitu muodostaa, ja muuttuja puuttuu kokonaan aineistosta.
Huomioithan, että vuodesta 2022 alkaen on tapahtunut muutoksia myös hakuoid- ja hakukohdeoid-muuttujien tilastoinnissa:
* Suojatut hakuoid- ja hakukohdeoid-tunnisteet eivät enää yhdisty ennen vuotta 2022 muodostettuihin aineistoihin.
* Vastaava muutos hakemusoid-muuttujassa tapahtui jo vuonna 2019.
* Esimerkiksi hakukohdeoid_s ei yhdisty aiempien vuosien tunnisteisiin. Tällöin voidaan hyödyntää vaihtoehtoisesti hakukohteen koulutuskoodia (hakuk_koulk1), joka kertoo hakutoiveen koulutusalan, yhdistettynä oppilaitostietoihin (oltunn_s, oppilaitosoid_s). Tämä tieto ei kuitenkaan ole yhtä tarkalla tasolla.

Vuodesta 2024 ähtöaineisto on vaihtunut Ovaraan.


<b>Aineiston päivitysaikataulu</b>
Tutustu valmisaineistojen <a href="https://stat.fi/fi/palvelut/palvelut-tutkijoille/tutkimusaineistot/valmisaineistot/valmisaineistojen-paivitysaikataulu">päivitysaikatauluun</a>.


<b>Aineiston käyttö ja tilaaminen</b>
Aineisto on tarkoitettu käytettäväksi FIONA-etäpalvelun kautta, ja se on linkitettävissä muihin henkilövalmisaineistoihin suojatun henkilönumeron avulla.

Valmisaineiston voi tilata tutkimuksen kohdejoukolle ja tarvittavilta ajanjaksoilta. Kokonaisaineiston (kaikki muuttujat koko populaatiosta ja kaikilta saatavilla olevilta vuosilta) käyttöoikeus myönnetään vain, jos tutkimuksellinen tarve sitä erityisesti edellyttää. Lisäksi aineistosta voi tilata räätälöidyn version, joka sisältää vain osan muuttujista.

Aineisto on FIONA-etäkäyttöjärjestelmässä jaettuina vuosikansioihin tilastovuosittain.


<b>Tarkempaa tietoa muuttujista</b>
Hakurekisteristä on saatavilla erikseen arkaluonteisia ja karkeistamattomia muuttujia, joihin myönnetään käyttöoikeus vain erityisestä tutkimuksellisesta syystä. Tällaisia ovat esimerkiksi karkeistamaton äidinkielitieto, karkeistamaton kansalaisuustieto sekä valinnan_tilan_lisatieto (sisältää kirjoitettuja selitteitä liittyen valinnan tilaan). Niillä karkeistetuilla tiedoilla, joista on saatavilla karkeistamaton versio esimerkiksi Tilastokeskuksen tietovarannoista, on muuttujien lopussa tunniste _k.


<b>Lisätietoa</b>
Lisätietoja aineistosta saa Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@stat.fi

## Variables (79)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `hid_e` | Suojattu henkilön yksilöivä tunniste | — | — | — |
| `henkilo_oid_s` | Suojattu henkilö-OID | — | — | — |
| `hakukohdeoid_s` | — | — | — | — |
| `oppilaitosoid_s` | — | — | — | — |
| `koulutustoimijan_ytunnus_s` | — | — | — | — |
| `oltunn_s` | — | — | — | — |
| `hakuoid_s` | Haku-OID | — | — | — |
| `hakemusoid_s` | Hakemus-OID | — | — | — |
| `tilv` | tilastovuosi | — | — | — |
| `vvuosi` | — | — | — | — |
| `koulutuksen_alkamisvuosi` | Koulutuksen alkamisvuosi | — | — | — |
| `koulutuksen_alkamiskausi` | Koulutuksen alkamiskausi | — | — | — |
| `hakuvuosi` | Hakuvuosi | — | — | — |
| `hakukausi` | Hakukausi | — | — | — |
| `hakuajat_alkaa` | Hakuajan alku | — | — | — |
| `hakuajat_paattyy` | Hakuajan loppu | — | — | — |
| `haun_kohdejoukko` | Haun kohdejoukko | — | — | — |
| `haun_kohdejoukon_tarkenne` | Haun kohdejoukon tarkenne | — | — | — |
| `hakukohteiden_priorisointi` | Hakukohteiden priorisointi | — | — | — |
| `hakutapa_koodi` | Hakutapa | — | — | — |
| `koulutuksen_koulutustyyppi` | Koulutuksen koulutustyyppi | — | — | — |
| `ensikertalaisten_aloituspaikat` | Ensikertalaisten aloituspaikat | — | — | — |
| `hakukohteen_aloituspaikat` | Ilmoitetut aloituspaikat | — | — | — |
| `koulutuksen_opetuskieli1` | Koulutuksen opetuskieli | — | — | — |
| `koulutuksen_opetuskieli2` | Koulutuksen opetuskieli | — | — | — |
| `koulutuksen_opetuskieli3` | Koulutuksen opetuskieli | — | — | — |
| `hakuk_koulk1` | Hakukohteen koulutuskoodi | — | — | — |
| `hakuk_koulk2` | Hakukohteen koulutuskoodi | — | — | — |
| `hakuk_koulk3` | Hakukohteen koulutuskoodi | — | — | — |
| `hakuk_koulk4` | hakukohteen koulutuskoodi | — | — | — |
| `hakuk_koulk5` | hakukohteen koulutuskoodi | — | — | — |
| `snimi` | Koul.koodin suomenk. nimike | — | — | — |
| `organisaation_kuntakoodi` | kuntakoodi | — | — | — |
| `hakemus_tila` | Hakemuksen tila | — | — | — |
| `sija` | Hakukohteen sija | — | — | — |
| `ensikertalaisuus` | Ensikertalaisuus | — | — | — |
| `sp` | sukupuoli | — | — | — |
| `hakijan_kotikunta` | kotikunta | — | — | — |
| `ika` | Hakijan ikä | — | — | — |
| `askun` | asuinkunta | — | — | — |
| `tilvaskun` | asuinkunta | — | — | — |
| `ulkomailla_suoritetun_toisen_ast` | Ulkomailla suoritetun toisenasteen tutkinnon suoritusmaa | — | — | — |
| `pohjakoulutus_kk1` | Pohjakoulutus hakukohteeseen | — | — | — |
| `pohjakoulutus_kk2` | pohjakoulutus hakukohteeseen | — | — | — |
| `pohjakoulutus_kk3` | pohjakoulutus hakukohteeseen | — | — | — |
| `pohjakoulutus_kk4` | pohjakoulutus hakukohteeseen | — | — | — |
| `pohjakoulutus_kk5` | pohjakoulutus hakukohteeseen | — | — | — |
| `pohjakoulutus_kk6` | pohjakoulutus hakukohteeseen | — | — | — |
| `pohjakoulutus_kk7` | pohjakoulutus hakukohteeseen | — | — | — |
| `valintatapajono_oid_s` | Suojattu valintatapajonon yksilöivä tunniste | — | — | — |
| `valintatapajono_koodi` | Luokiteltu valintatapajonon nimi | — | — | — |
| `yksiloity` | Yksilöintitieto | — | — | — |
| `osallistui_paasykokeeseen` | Pääsykokeeseen osallistuminen | — | — | — |
| `valintajonot_pisteet` | Valintajonon pisteet | — | — | — |
| `pisteet` | Hakijan pisteet | — | — | — |
| `alin_hyvaksytty_pistemaara` | Alin hyväksytty pistemäärä valintatapajonossa | — | — | — |
| `valintajonot_jonosija` | Valintajonon jonosija | — | — | — |
| `valinnan_tila` | Valinnan tila | — | — | — |
| `valinnan_tilatk` | Valinnan tila (Tilastokeskus) | — | — | — |
| `vastaanoton_tila` | Vastaanoton tila | — | — | — |
| `vastaanoton_tila_tk` | Vastaanoton tila (Tilastokeskus) | — | — | — |
| `ilmoittautumisen_tila` | Ilmoittautumisen tila | — | — | — |
| `ilmoittautumisen_tila_tk` | Ilmoittautumisen tila (Tilastokeskus) | — | — | — |
| `valintatieto` | Hakijan hakukohteen valintatieto | — | — | — |
| `hyvaksytty_ensikertalaisten_haki` | Hyväksytty ensikertalainen hakija valintatapajonossa. | — | — | — |
| `kaste_t2` | Hakukohteen koulutusaste, koulutusluokitus 2016 | — | — | — |
| `iscle2011` | iscle2011 | — | — | — |
| `isccat2011` | isccat2011 | — | — | — |
| `iscsubcat2011` | iscsubcat2011 | — | — | — |
| `iscfinarrow2013` | iscfinarrow2013 | — | — | — |
| `iscfibroad2013` | iscfibroad2013 | — | — | — |
| `iscfi2013` | iscfi2013 | — | — | — |
| `okun` | Sijaintikunta | — | — | — |
| `okieli` | Opetuskieli | — | — | — |
| `oltyp` | Oppilaitostyyppi | — | — | — |
| `omist` | Omistajatyyppi | — | — | — |
| `kansal_k` | Hakijan karkeistettu kansalaisuus | — | — | — |
| `hakijan_asuinmaa_k` | Hakijan karkeistettu asuinmaa | — | — | — |
| `aikieli_k` | Hakijan äidinkieli | — | — | — |

### Variable definitions

#### `hid_e` — Suojattu henkilön yksilöivä tunniste

Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e-tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä.

#### `henkilo_oid_s` — Suojattu henkilö-OID

Suojattu OPH:n luoma yksilöivä henkilölle. Lisätietoa aiheesta <a><href="https://wiki.eduuni.fi/spaces/ophPPK/pages/190612188/Mik%C3%A4+on+oppijanumero">OPH:n eduuni-wiki -sivustolla</a> (27.8.2026).

#### `hakukohdeoid_s`

Suojattu hakukohteen yksilöintitunnus. Huom.: muuttujan tilastoinnissa tapahtuneiden muutosten vuoksi tieto ei yhdisty hakukohdeoid:eihin ennen vuotta 2022.

#### `oppilaitosoid_s`

Suojattu hakukohteen organisaation yksilöintitunnus

#### `koulutustoimijan_ytunnus_s`

Suojattu koulutuksen järjestäjän y-tunnus

#### `oltunn_s`

Suojattu hakukohteen oppilaitostunnus (oppilaitoskoodi-muuttujasta).

#### `hakuoid_s` — Haku-OID

Suojattu haun yksilöintitunnus.  Huom.: muuttujan tilastoinnissa tapahtuneiden muutosten vuoksi tieto ei yhdisty hakuoid:eihin ennen vuotta 2022.

#### `hakemusoid_s` — Hakemus-OID

Suojattu hakemuksen yksilöintitunnus

#### `tilv` — tilastovuosi

Tilastovuosi

#### `vvuosi`

Numeerinen vuosimuuttuja vvuosi viittaa aina kyseiseen tilastovuoteen, jolta hakurekisteri on muodostettu. Vastaa numeerisena tilastovuosi (tilv) -muuttujaa  (kun taas hakuvuosi voi olla myös esim. tätä edeltävä vuosi, mikäli edellisvuoden rekisteri on muodostettu ennen kyseistä hakua).

#### `koulutuksen_alkamisvuosi` — Koulutuksen alkamisvuosi

Koulutuksen alkamisvuosi, pohjautuu Ovaran  tietoihin.

#### `koulutuksen_alkamiskausi` — Koulutuksen alkamiskausi

Koulutuksen alkamislukukausi. Pohjautuu Ovaran tietoihin.
K = kevät
S = syksy
Voi olla myös tyhjä.

#### `hakuvuosi` — Hakuvuosi

Hakuvuosi mikäli se on voitu määrittää hakuajan alusta (hakuajat_alkaa) ja hakuajan lopusta (hakuajat_paattyy). Haut, joiden hakuajat ylittävät vuoden vaihteen, hakuvuosi on jätetty tyhjäksi.

#### `hakukausi` — Hakukausi

Hakukausi, mikäli se on voitu määrittää hakuajan alusta (hakuajat_alkaa) ja hakuajan lopusta (hakuajat_paattyy). Haut, joiden hakuajat ylittävät vuoden vaihteen, hakukausi on jätetty tyhjäksi.

K = kevät
S = syksy

#### `hakuajat_alkaa` — Hakuajan alku

#### `hakuajat_paattyy` — Hakuajan loppu

#### `haun_kohdejoukko` — Haun kohdejoukko

Haun kohdejoukko
12=Korkeakoulutus
Saatavilla v. 2017 eteenpäin

#### `haun_kohdejoukon_tarkenne` — Haun kohdejoukon tarkenne

Haun kohdejoukon tarkenne vuodesta 2024 eteenpäin:
1 = Siirtohaku
5 =Ammatillinen opinto-ohjaajankoulutus
8 = Maahanmuuttajien valmentava koulutus
9 = Erikoislääkäri ja erikoishammaslääkärinkoulutus 
3 = Jatkotutkintohaku
2 = Ammatillinen opettajankoulutus
4 = Ammatillinen erityisopettajankoulutus
7 = Opettajan pedagogiset opinnot

#### `hakukohteiden_priorisointi` — Hakukohteiden priorisointi

Hakukohteiden priorisointi
1=haussa hakutoiveiden priorisointi käytössä (=hakutoiveiden järjestys vaikuttaa)
0=haussa ei ole hakutoiveiden priorisointi käytössä

Saatavilla v. 2017 eteenpäin

#### `hakutapa_koodi` — Hakutapa

Muuttuja hakutyyppi sisältyy OVARAssa hakutapakoodiin vuodesta 2024 lähtien:
1 = Yhteishaku
2 = Erillishaku
3 = Jatkuva haku
4 = Joustava haku
5 = Siirtohaku
6 = Lisähaku

#### `koulutuksen_koulutustyyppi` — Koulutuksen koulutustyyppi

Hakukohteen koulutustyyppi
3 = Korkeakoulutus
Saatavilla v. 2017 eteenpäin.

#### `ensikertalaisten_aloituspaikat` — Ensikertalaisten aloituspaikat

Ensikertalaisten aloituspaikat

Saatavilla v. 2017 eteenpäin.

#### `hakukohteen_aloituspaikat` — Ilmoitetut aloituspaikat

Entinen hakijalle_ilmoitetut_aloituspaik. Aloituspaikat
Hakijoille koulutustiedotuksessa ilmoitetut aloituspaikat
Saatavilla v. 2017 eteenpäin

#### `koulutuksen_opetuskieli1` — Koulutuksen opetuskieli

Koulutuksen opetuskieli
Luokat: FI, SV, EN
Saatavilla v. 2017 eteenpäin

#### `koulutuksen_opetuskieli2` — Koulutuksen opetuskieli

Koulutuksen opetuskieli
Luokat: FI, SV, EN
Saatavilla v. 2017 eteenpäin

#### `koulutuksen_opetuskieli3` — Koulutuksen opetuskieli

Koulutuksen opetuskieli
Luokat: FI, SV, EN
Saatavilla v. 2017 eteenpäin

#### `hakuk_koulk1` — Hakukohteen koulutuskoodi

Hakukohteen koulutuskoodi

Muuttujissa hakuk_koulk1-hakuk_koulk5 on tietoja, jos samalla hakukohteella on useita koulutuskoodeja. Pääsääntöisesti käytetään koulutuskooditietona hakuk_koulk1-muuttujan tietoa.
TK:n koulutusluokituksen koulutuskoodit (kts. metadata-kansion luokitustiedot).
Lisäksi tutkintoon johtamattomat koulutukset, joita ei löydy koulutusluokituksesta:
000001 Ammatillinen opettajankoulutus
000002 Ammatillinen erityisopettajan koulutus
000002 Ammatillinen opinto-ohjaajan koulutus
Saatavilla v. 2017 eteenpäin

#### `hakuk_koulk2` — Hakukohteen koulutuskoodi

Hakukohteen koulutuskoodi

Muuttujissa hakuk_koulk1-hakuk_koulk5 on tietoja, jos samalla hakukohteella on useita koulutuskoodeja. Pääsääntöisesti käytetään koulutuskooditietona hakuk_koulk1-muuttujan tietoa.
TK:n koulutusluokituksen koulutuskoodit.
Lisäksi tutkintoon johtamattomat koulutukset, joita ei löydy koulutusluokituksesta:
000001 Ammatillinen opettajankoulutus
000002 Ammatillinen erityisopettajan koulutus
000002 Ammatillinen opinto-ohjaajan koulutus

#### `hakuk_koulk3` — Hakukohteen koulutuskoodi

Hakukohteen koulutuskoodi

Muuttujissa hakuk_koulk1-hakuk_koulk5 on tietoja, jos samalla hakukohteella on useita koulutuskoodeja. Pääsääntöisesti käytetään koulutuskooditietona hakuk_koulk1-muuttujan tietoa.
TK:n koulutusluokituksen koulutuskoodit.
Lisäksi tutkintoon johtamattomat koulutukset, joita ei löydy koulutusluokituksesta:
000001 Ammatillinen opettajankoulutus
000002 Ammatillinen erityisopettajan koulutus
000002 Ammatillinen opinto-ohjaajan koulutus

#### `hakuk_koulk4` — hakukohteen koulutuskoodi

Hakukohteen koulutuskoodi

Muuttujissa hakuk_koulk1-hakuk_koulk5 on tietoja, jos samalla hakukohteella on useita koulutuskoodeja. Pääsääntöisesti käytetään koulutuskooditietona hakuk_koulk1-muuttujan tietoa.
TK:n koulutusluokituksen koulutuskoodit.
Lisäksi tutkintoon johtamattomat koulutukset, joita ei löydy koulutusluokituksesta:
000001 Ammatillinen opettajankoulutus
000002 Ammatillinen erityisopettajan koulutus
000002 Ammatillinen opinto-ohjaajan koulutus

#### `hakuk_koulk5` — hakukohteen koulutuskoodi

Hakukohteen koulutuskoodi

Muuttujissa hakuk_koulk1-hakuk_koulk5 on tietoja, jos samalla hakukohteella on useita koulutuskoodeja. Pääsääntöisesti käytetään koulutuskooditietona hakuk_koulk1-muuttujan tietoa.
TK:n koulutusluokituksen koulutuskoodit.
Lisäksi tutkintoon johtamattomat koulutukset, joita ei löydy koulutusluokituksesta:
000001 Ammatillinen opettajankoulutus
000002 Ammatillinen erityisopettajan koulutus
000002 Ammatillinen opinto-ohjaajan koulutus

#### `snimi` — Koul.koodin suomenk. nimike

Hakukohteen koulutuskoodin nimi (TK)
Saatavilla v. 2017 eteenpäin

#### `organisaation_kuntakoodi` — kuntakoodi

Kuntakoodi
Saatavilla v. 2017 eteenpäin

#### `hakemus_tila` — Hakemuksen tila

Hakemuksen tila
ACTIVE = aktiivinen
INCOMPLETE = keskeneräinen

#### `sija` — Hakukohteen sija

Hakukohteiden järjestysnumero 1-6. Voi sisältää myös -1 arvon.

#### `ensikertalaisuus` — Ensikertalaisuus

Ensikertalaisuus
1 = Ensikertalainen hakija,
0 = Ei ensikertalainen hakija,
Tyhjä arvo = Ei titeoa.

#### `sp` — sukupuoli

Sukupuolikoodi:
1 = mies
2 = nainen

#### `hakijan_kotikunta` — kotikunta

Kotikunta kuntaluokituksen mukaan v. 2017 alkaen.

#### `ika` — Hakijan ikä

Ikä tilastovuoden (tilv) lopussa vuoden tarkkuudella.

#### `askun` — asuinkunta

Asuinkunta seuraavan vuoden luokituksella, 31.12. kuluvana vuonna
Tieto otettu ensisijaisesti VRK:sta, toissijaisesti täydennetty hakijan_kotikunta -tiedosta.
999 = Tuntematon

#### `tilvaskun` — asuinkunta

Asuinkunta kuluvan vuoden luokituksella, 31.12. kuluvana vuonna
Tieto otettu ensisijaisesti VRK:sta, toissijaisesti täydennetty hakijan_kotikunta -tiedosta
999 = tuntematon

#### `ulkomailla_suoritetun_toisen_ast` — Ulkomailla suoritetun toisenasteen tutkinnon suoritusmaa

Ulkomailla suoritetun toisenasteen tutkinnon suoritusmaa, 999= muu tai tuntematon. Voi sisältää tyhjiä arvoja.
Saatavilla v. 2017 eteenpäin

#### `pohjakoulutus_kk1` — Pohjakoulutus hakukohteeseen

Hakijan ilmoittama pohjakoulutus hakukohteeseen
Voi olla useita (kk1-kk5/kk7):
pohjakoulutus_am (ammatillinen)
pohjakoulutus_amp
pohjakoulutus_amt (ammattitutkinto)
pohjakoulutus_amv
pohjakoulutus_avoin (avoin yliopisto)
pohjakoulutus_kk (korkeakoulututkinto)
pohjakoulutus_kk_ulk (korkeakoulututkinto ulkomailla)
pohjakoulutus_lk
pohjakoulutus_muu
pohjakoulutus_ulk (ulkomailla suoritettu)
pohjakoulutus_yo (ylioppilastutkinto)
pohjakoulutus_yo_ammatillinen (ylioppilastutkinto ja ammatillinen)
pohjakoulutus_yo_kansainvalinen_suomessa (Suomessa suoritettu kansainvälinen ylioppilastutkinto)
pohjakoulutus_yo_ulkomainen (ulkomailla suoritettu ylioppilastutkinto)

Saatavilla v. 2017 eteenpäin

#### `pohjakoulutus_kk2` — pohjakoulutus hakukohteeseen

Hakijan ilmoittama pohjakoulutus hakukohteeseen
Voi olla useita (kk1-kk5/kk7):
pohjakoulutus_am (ammatillinen)
pohjakoulutus_amp
pohjakoulutus_amt (ammattitutkinto)
pohjakoulutus_amv
pohjakoulutus_avoin (avoin yliopisto)
pohjakoulutus_kk (korkeakoulututkinto)
pohjakoulutus_kk_ulk (korkeakoulututkinto ulkomailla)
pohjakoulutus_lk
pohjakoulutus_muu
pohjakoulutus_ulk (ulkomailla suoritettu)
pohjakoulutus_yo (ylioppilastutkinto)
pohjakoulutus_yo_ammatillinen (ylioppilastutkinto ja ammatillinen)
pohjakoulutus_yo_kansainvalinen_suomessa (Suomessa suoritettu kansainvälinen ylioppilastutkinto)
pohjakoulutus_yo_ulkomainen (ulkomailla suoritettu ylioppilastutkinto)
Saatavilla v. 2017 eteenpäin

#### `pohjakoulutus_kk3` — pohjakoulutus hakukohteeseen

Hakijan ilmoittama pohjakoulutus hakukohteeseen
Voi olla useita (kk1-kk5/kk7):
pohjakoulutus_am (ammatillinen)
pohjakoulutus_amp
pohjakoulutus_amt (ammattitutkinto)
pohjakoulutus_amv
pohjakoulutus_avoin (avoin yliopisto)
pohjakoulutus_kk (korkeakoulututkinto)
pohjakoulutus_kk_ulk (korkeakoulututkinto ulkomailla)
pohjakoulutus_lk
pohjakoulutus_muu
pohjakoulutus_ulk (ulkomailla suoritettu)
pohjakoulutus_yo (ylioppilastutkinto)
pohjakoulutus_yo_ammatillinen (ylioppilastutkinto ja ammatillinen)
pohjakoulutus_yo_kansainvalinen_suomessa (Suomessa suoritettu kansainvälinen ylioppilastutkinto)
pohjakoulutus_yo_ulkomainen (ulkomailla suoritettu ylioppilastutkinto)
Saatavilla v. 2017 eteenpäin

#### `pohjakoulutus_kk4` — pohjakoulutus hakukohteeseen

Hakijan ilmoittama pohjakoulutus hakukohteeseen
Voi olla useita (kk1-kk5/kk7):
pohjakoulutus_am (ammatillinen)
pohjakoulutus_amp
pohjakoulutus_amt (ammattitutkinto)
pohjakoulutus_amv
pohjakoulutus_avoin (avoin yliopisto)
pohjakoulutus_kk (korkeakoulututkinto)
pohjakoulutus_kk_ulk (korkeakoulututkinto ulkomailla)
pohjakoulutus_lk
pohjakoulutus_muu
pohjakoulutus_ulk (ulkomailla suoritettu)
pohjakoulutus_yo (ylioppilastutkinto)
pohjakoulutus_yo_ammatillinen (ylioppilastutkinto ja ammatillinen)
pohjakoulutus_yo_kansainvalinen_suomessa (Suomessa suoritettu kansainvälinen ylioppilastutkinto)
pohjakoulutus_yo_ulkomainen (ulkomailla suoritettu ylioppilastutkinto)
Saatavilla v. 2017 eteenpäin

#### `pohjakoulutus_kk5` — pohjakoulutus hakukohteeseen

Hakijan ilmoittama pohjakoulutus hakukohteeseen
Voi olla useita (kk1-kk5/kk7):
pohjakoulutus_am (ammatillinen)
pohjakoulutus_amp
pohjakoulutus_amt (ammattitutkinto)
pohjakoulutus_amv
pohjakoulutus_avoin (avoin yliopisto)
pohjakoulutus_kk (korkeakoulututkinto)
pohjakoulutus_kk_ulk (korkeakoulututkinto ulkomailla)
pohjakoulutus_lk
pohjakoulutus_muu
pohjakoulutus_ulk (ulkomailla suoritettu)
pohjakoulutus_yo (ylioppilastutkinto)
pohjakoulutus_yo_ammatillinen (ylioppilastutkinto ja ammatillinen)
pohjakoulutus_yo_kansainvalinen_suomessa (Suomessa suoritettu kansainvälinen ylioppilastutkinto)
pohjakoulutus_yo_ulkomainen (ulkomailla suoritettu ylioppilastutkinto)
Saatavilla v. 2017 eteenpäin

#### `pohjakoulutus_kk6` — pohjakoulutus hakukohteeseen

Hakijan ilmoittama pohjakoulutus hakukohteeseen
Voi olla useita (kk1-kk5/kk7):
pohjakoulutus_am (ammatillinen)
pohjakoulutus_amp
pohjakoulutus_amt (ammattitutkinto)
pohjakoulutus_amv
pohjakoulutus_avoin (avoin yliopisto)
pohjakoulutus_kk (korkeakoulututkinto)
pohjakoulutus_kk_ulk (korkeakoulututkinto ulkomailla)
pohjakoulutus_lk
pohjakoulutus_muu
pohjakoulutus_ulk (ulkomailla suoritettu)
pohjakoulutus_yo (ylioppilastutkinto)
pohjakoulutus_yo_ammatillinen (ylioppilastutkinto ja ammatillinen)
pohjakoulutus_yo_kansainvalinen_suomessa (Suomessa suoritettu kansainvälinen ylioppilastutkinto)
pohjakoulutus_yo_ulkomainen (ulkomailla suoritettu ylioppilastutkinto)
Saatavilla v. 2017 eteenpäin

#### `pohjakoulutus_kk7` — pohjakoulutus hakukohteeseen

Hakijan ilmoittama pohjakoulutus hakukohteeseen
Voi olla useita (kk1-kk5/kk7):
pohjakoulutus_am (ammatillinen)
pohjakoulutus_amp
pohjakoulutus_amt (ammattitutkinto)
pohjakoulutus_amv
pohjakoulutus_avoin (avoin yliopisto)
pohjakoulutus_kk (korkeakoulututkinto)
pohjakoulutus_kk_ulk (korkeakoulututkinto ulkomailla)
pohjakoulutus_lk
pohjakoulutus_muu
pohjakoulutus_ulk (ulkomailla suoritettu)
pohjakoulutus_yo (ylioppilastutkinto)
pohjakoulutus_yo_ammatillinen (ylioppilastutkinto ja ammatillinen)
pohjakoulutus_yo_kansainvalinen_suomessa (Suomessa suoritettu kansainvälinen ylioppilastutkinto)
pohjakoulutus_yo_ulkomainen (ulkomailla suoritettu ylioppilastutkinto)
Saatavilla v. 2017 eteenpäin

#### `valintatapajono_oid_s` — Suojattu valintatapajonon yksilöivä tunniste

#### `valintatapajono_koodi` — Luokiteltu valintatapajonon nimi

Seuraavat luokitukset on luotu Tutkijapalveluissa.
av = Avoimen väylä
km = Kilpailumenestys
kp = Koepisteet
m = Muu
tv = Todistusvalinta
yp = Yhteispisteet.

Avoimeen väylään on sisällytetty avoimen väylän lisäksi esimerkiksi lukioväylän ja näyttöreittivalinnan valintajonot.
Koepisteet-kategoriaan on sisällytetty mm. valintatapajonot, jotka sisältävät valintakokeen tai soveltuvuuskokeen.
Todistusvalintaan on sisällytetty todistusvalinnan lisäksi esimerkiksi suoravalintajonot ja ylioppilaskokeen arvosanaan perustuvat valintatapajonot.
Yhteispisteet-kategoriaan on sisälltetty lisäksi esimerkiksi ennakkotehtävän ja/ tai haastattelun sisältävät valintatapajonot.

Tutkijapalvelut kartoittaa onko tarvetta tämän muuttujan sisällön päivittämiselle.

#### `yksiloity` — Yksilöintitieto

Tieto hakijan onnistuneesta yksilöimisestä.
t/true = Yksilöinti onnistunut,
f/false = Yksilöinti epäonnistunut.
Saatavilla v. 2017 eteenpäin

#### `osallistui_paasykokeeseen` — Pääsykokeeseen osallistuminen

Osallistui pääsykokeeseen
0 = Ei, 
1 = Kyllä

Saatavilla v. 2017 eteenpäin. 

Tutkijapalvelut selvittää mahdollisuutta muuttujan täydentämiseen aineistovuodelle 2024, missä muuttuja saa tyhjän arvon. Erillistä valintatapajonoista saa myös tiedon, onko hakija on osallistunut pääsykokeeseen.

#### `valintajonot_pisteet` — Valintajonon pisteet

Hakijan pisteet valintatapajonotyypissä.

#### `pisteet` — Hakijan pisteet

Kts. valintajonot_pisteet.

#### `alin_hyvaksytty_pistemaara` — Alin hyväksytty pistemäärä valintatapajonossa

#### `valintajonot_jonosija` — Valintajonon jonosija

Jonosija valintatapajonossa.

#### `valinnan_tila` — Valinnan tila

Hakijan valinnan tila hakukohteen valintatapajonossa.

#### `valinnan_tilatk` — Valinnan tila (Tilastokeskus)

Valinnan tila, TK:ssa koodattu
1 = hyväksytty
2 = hylätty
3 = perunut
4 = peruuntunut
5 = peruutettu
6 = varalla
7 = varasijalta hyväksytty
9=tuntematon

#### `vastaanoton_tila` — Vastaanoton tila

Vastaanoton tila

#### `vastaanoton_tila_tk` — Vastaanoton tila (Tilastokeskus)

Vastaanoton tila, TK:ssa koodattu
Huom. luokitus eroaa aikavälillä:
1 = vastaanottanut, vastaanottanut sitovasti
2 = ilmoitettu (ei 2017 aineistoissa, ei saatavilla 2021)
3 = kesken
4 = perunut
5 = peruutettu
6 = ei vastaanotettu määräaikana
7 = vastaanottanut läsnäolevana (2015-2020, ei 2017 aineistoissa), 7 = ottanut vastaan toisen paikan (2021)
8 = vastaanottanut poissaolevana (ei 2017 aineistossa)
9 = tuntematon (vuosina 2015-2016 sekä vuonna 2021 ja 2024), 9=ottanut vastaan toisen paikan (2017-2020).

#### `ilmoittautumisen_tila` — Ilmoittautumisen tila

Ilmoittautumisen tila
Huom. Tyhjä arvo tai 99999 = Tuntematon.

#### `ilmoittautumisen_tila_tk` — Ilmoittautumisen tila (Tilastokeskus)

Ilmoittautumisen tila, TK:ssa koodattu.
Huom. luokitus eroaa aikavälillä.
2015-2016:
1 = läsnä, kevät
2 = läsnä, syksy
3 = läsnä, koko lukuvuosi
4 = poissa, kevät
5 = poissa, syksy
6 = poissa, koko lukuvuosi
7 = ei ilmoittautunut
8 = ei tehty
9 = tuntematon

2017-2021, 2024:
1=Läsnä koko lukuvuosi
2=läsnä syksy
3=läsnä
4=poissa
5=poissa koko lukuvuosi
6=poissa syksy
7=ei tehty
8=ei ilmoittautunut
Lisäksi vuonna 2021 lisätty luokka 9=tuntematon.

#### `valintatieto` — Hakijan hakukohteen valintatieto

Hakijan hakukohteen valintatieto. Eroaa valinnan_tila muuttujasta siten, että tämä muuttuja kuvaa hakukohteen valintatietoa yli valintatapajonojen.

#### `hyvaksytty_ensikertalaisten_haki` — Hyväksytty ensikertalainen hakija valintatapajonossa.

Lisätieto valinnasta ensikertalaisena hakijana. Tieto on valintatapajonokohtainen, ts. mikäli hakija on hyväksytty hakukohteeseen tietyn valintatapajonon kautta, tieto hakijan ensikertalaisuudesta löytyy kyseisen valintatapajonon riviltä.

#### `kaste_t2` — Hakukohteen koulutusaste, koulutusluokitus 2016

Hakukohteen koulutusaste, koulutusluokitus 2016
Saatavilla v. 2018 eteenpäin

#### `iscle2011` — iscle2011

Unescon kansainvälisen koulutusluokituksen (ISCED 2011)
1-numeroinen koulutusaste tilastovuoden mukaisena

#### `isccat2011` — isccat2011

Unescon kansainvälisen koulutusluokituksen (ISCED 2011)
2-numeroinen koulutusaste tilastovuoden mukaisena

#### `iscsubcat2011` — iscsubcat2011

Unescon kansainvälisen koulutusluokituksen (ISCED 2011)
3-numeroinen koulutusaste tilastovuoden mukaisena

#### `iscfinarrow2013` — iscfinarrow2013

Unescon kansainvälisen koulutusluokituksen (ISCED 2013)
3-numeroinen koulutusala tilastovuoden mukaisena

#### `iscfibroad2013` — iscfibroad2013

Unescon kansainvälisen koulutusluokituksen (ISCED 2013)
2-numeroinen koulutusala tilastovuoden mukaisena

#### `iscfi2013` — iscfi2013

Unescon kansainvälisen koulutusluokituksen (ISCED 2013)
4-numeroinen koulutusala tilastovuoden mukaisena

#### `okun` — Sijaintikunta

Hakukohteen oppilaitoksen sijantikunta.
Lähde Ovara
bl = tuntematon

#### `okieli` — Opetuskieli

Hakukohteen oppilaitoksen kieli.
Lähde oppilaitosrekisteri
1 = suomi
2 = ruotsi
3 = suomi/ruotsi
4 = englanti
5 = saame
9 = muu
bl = tuntematon

#### `oltyp` — Oppilaitostyyppi

Hakukohteen oppilaitostyyppi.
Lähde Ovara.
bl = tuntematon

#### `omist` — Omistajatyyppi

Hakukohteen oppilaitoksen omistajatyyppi.
Lähde Ovara
1 = yksityinen
2 = valtio
3 = kunta
4 = kuntayhtymä
5 = Ahvenanmaa
9 = muu
bl = tuntematon

#### `kansal_k` — Hakijan karkeistettu kansalaisuus

Kansalaisuus (karkeistettu tieto).
Tieto otettu ensisijaisesti VTJ:sta 31.12., toissijaisesti täydennetty Ovaran kansalaisuustiedolla (ISO 3166-N maakoodi).
Karkeistetut luokitukset:
1 = Suomi
2 = Eurooppa
3 = muu tai ei tietoa.

#### `hakijan_asuinmaa_k` — Hakijan karkeistettu asuinmaa

Hakijan asuinmaa (karkeistettu tieto).
Karkeistetut luokitukset:
1 = Suomi
2 = Eurooppa
3 = muu tai ei tietoa
(3 sis. kaikki muut luokat, ml. luokan 999 = ei tietoa)
Perustuu alkuperäisen aineiston tietoihin
Saatavilla v. 2017 eteenpäin

#### `aikieli_k` — Hakijan äidinkieli

Äidinkieli (karkeistettu tieto).
Tieto otettu ensisijaisesti VRK:sta, toissijaisesti täydennetty hakuaineiston äidinkieli-tieto (henkilöille, joille ei löytynyt tietoa väestötietojärjestelmästä).
Karkeistetut luokitukset (perustuen 2-merkkiseen kielikoodiin):
1 = suomi
2 = ruotsi
3 = muu tai ei tietoa
(3 sis. kaikki muut luokat, ml. luokan 99 = tuntematon)

---

[← Back to catalogue](../../README.md)
