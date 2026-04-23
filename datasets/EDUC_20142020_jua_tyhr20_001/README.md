# Toisen asteen yhteishaku - moduuli, osa 6 (2014 - 2020)

- **Identifier:** `EDUC_20142020_jua_tyhr20_001.xml`
- **DOI:** `khak_2017-05_2017-05-05_ain_0001`
- **Temporal coverage:** —
- **Published:** 2025-12-18
- **Organisation:** Tilastokeskus
- **Variable count:** 111
- **Observation count:** —
- **Source:** OPH:n Tilastokeskukselle vuosittain toimittama toisen asteen koulutuksen yhteishakurekisteri. Taustatietoja saatu Väestörekisterikeskuksesta.

## Description

Toisen asteen yhteishaku -moduulin 6. osa koostuu henkilöistä, jotka osallistuivat tilastovuodesta 2014 alkaen  toisen asteen koulutuksen yhteishakuun. Vuosilta 2014 - 2016 tiedostot on toimitettu Tilastokeskukseen OPH:sta. Vuodesta 2017 alkaen aineisto on haettu rajapinnalta json-muotoisina tiedostoina, joista Tilastokeskuksessa on koottu varsinainen aineisto. Huomioi, että tiedon täsmäävyyttä OPH:n lopulliseen rekisteriin ei voitu tarkistaa.

- Vuonna alkaneisiin toisen asteen ja valmentaviin ja valmistaviin koulutuksiin hakeneet
- Opetushallitus, Opintopolku, ODW-tietokanta
- Henkilö usealla rivillä haun, hakemuksen ja hakutoiveen mukaan

Toisen asteen yhteishaku -moduulin 7. osa koostuu seuraavista tiedostoista
educ_tyhr_20142016
educ_tyhr_2017
educ_tyhr_2018
educ_tyhr_2019
educ_tyhr_2020

Arvosanamuuttujat on sisällytetty seuraaviin erillisiin tiedostoihin (vuoden 2020 arvosanatiedosto puuttuu toistaiseksi): 
educ_tyhr_arvos_2014
educ_tyhr_arvos_2015
educ_tyhr_arvos_2016
educ_tyhr_arvos_2017
educ_tyhr_arvos_2018
educ_tyhr_arvos_2019

Huomaathan, että arvosanatiedot ovat rakenteeltaan erilaisia: esimerkiksi 2014 jokaisella henkilöllä on yhtä monta riviä kuin kouluaineita, kun taas 2015 yhden henkilön kaikki aineet ovat samalla rivillä. Vuoden 2015 pakollisten aineiden arvosanat sisältävissä muuttujissa on paljon tyhjää, mutta valinnaisten aineiden muuttujissa on paljon havaintoja. Näiden muuttujien käyttö on siis tutkijan oman harkinnan varassa.

Lähtökoulun tiedot täytyy etsiä eri tiedostosta/yhdistää myöhemmin

Tiedostoista on salattu henkilön tunnistetiedot. Lisäksi tiedostoista on suojattu kaikkien oppilaitosten tunnistetiedot.

HUOMIOITA tiedostosta:

2014 - 2016:
Yksilöintitunnuksissa SHAKU_OID, SHAKEMUS_OID, SHLOOID, SHAKUKOHTEEN_ORGANISAATIO_OID, SHAKUKOHTEEN_OID ja SLAHTOKOULUN_ORGANISAATIO_OID on havaittu virheitä. Nämä muuttujat eivät vuosien 2014 - 2016 tiedostoissa yksilöi kuvauksen mukaisia kohteita. Näiden muuttujien tiedot vuosilta 2014 - 2016 eivät ole (toistaiseksi) vertailukelpoisia vuoden 2017 ja myöhempien vuosien tietojen kanssa. Mainittujen yksilöintitunnusten avulla tietoja voidaan yhdistellä yli ajan (toistaiseksi) vuodesta 2017 alkaen.

2014:
Uusimuotoisessa toisen asteen hakuaineistossa on laatupulmia. Ensimmäinen hakutoive on kaikkiaan 94 000 hakijalla, mutta 1 300 hakijalta se puuttuu, vaikka muita hakutoiveita heiltä kyllä löytyy. Tähän todennäköisenä selityksenä on vuoden 2015 puolella poistetut hakukohteet, joiden mukana hakukohteeseen liittyvät tiedot hyväksymisineen ja vastaanottoineen ovat hävinneet, eivätkä siis ole mukana TK:een tulleessa aineistossa. Sama ongelma koskee myös muita hakutoiveita. Esimerkiksi toinen hakutoive puuttuu 740 hakijalta, joilta kuitenkin löytyy kolmas hakutoive.

## Variables (111)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `TILV` | Tilastovuosi | — | — | — |
| `HAKUVUOSI` | Hakuvuosi | — | — | — |
| `HAKUKAUSI` | Hakukausi | — | — | — |
| `KOULUTUKSEN_ALKAMISVUOSI` | Koulutuksen alkamisvuosi | — | — | — |
| `KOULUTUKSEN_ALKAMISKAUSI` | Koulutuksen alkamislukukausi | — | — | — |
| `HAUN_KOHDEJOUKKO` | Haun kohdejoukko | — | — | — |
| `HAKUKOHTEIDEN_PRIORISOINTI` | Hakukohteiden priorisointi | — | — | — |
| `SHAKU_OID` | Suojattu haun yksilöintitunnus | — | — | — |
| `HAKU` | Haun nimi | — | — | — |
| `HAKU_SV` | Haun nimi ruotsiksi | — | — | — |
| `HAKU_EN` | Haun nimi englanniksi | — | — | — |
| `HAKUTYYPPI_KOODI` | Hakutyyppi | — | — | — |
| `HAKUTAPA_KOODI` | Hakutapa | — | — | — |
| `SHAKEMUS_OID` | Suojattu hakemuksen yksilöintitunnus | — | — | — |
| `HAKEMUS_TILA` | Hakemuksen tila | — | — | — |
| `HAKEMUS_TILATK` | Hakemuksen tila (koodattu TK:ssa) | — | — | — |
| `SHLOOID` | Suojattu henkilön yksilöintitunnus ODW:ssä | — | — | — |
| `SOPPIJANUMERO` | Suojattu oppijanumero | — | — | — |
| `SHNRO` | Suojattu henkilön yksilöivä tunniste | — | — | — |
| `SUKUPUOLI_KOODI` | Sukupuoli | — | — | — |
| `IKA` | Ikä | — | — | — |
| `KOTIMAA` | Kotimaa | — | — | — |
| `AIKIELI` | Äidinkieli | — | — | — |
| `AIKIELI_LK` | Äidinkieli (luokiteltu) | — | — | — |
| `KIELIKOODI` | Äidinkieli alkuperäisessa aineistossa | — | — | — |
| `KIELITYYPPI` | Äidinkieli pitkä alkuperäisessä aineistossa | — | — | — |
| `KANSAL` | Kansalaisuus | — | — | — |
| `HAKIJAN_KANSALAISUUS` | Hakijan kansalaisuus | — | — | — |
| `HAKIJAN_KANSALAISUUS2` | Hakijan kansalaisuus 2 | — | — | — |
| `HAKIJAN_KANSALAISUUS3` | Hakijan kansalaisuus 3 | — | — | — |
| `ASKUN` | Asuinkunta | — | — | — |
| `TILVASKUN` | Tilastovuoden asuinkunta | — | — | — |
| `HAKIJAN_KOTIKUNTA` | Hakijan kotikunta | — | — | — |
| `POHJAKOULUTUSTK` | Pohjakoulutuskoodi | — | — | — |
| `PAATTOLUOKKA` | Päättöluokka | — | — | — |
| `YKSILOITY` | Yksilöity | — | — | — |
| `ULKOMAILLA_SUORITETUN_TOISEN_AST` | Ulkomailla suoritetun toisen asteen tutkinnon suoritusmaa | — | — | — |
| `PERUSOPETUKSEN_OPETUSKIELI` | Perusopetuksen opetuskieli | — | — | — |
| `HAKIJAN_KOULUSIVISTYSKIELI` | Hakijan koulusivistyskieli | — | — | — |
| `PERUSOPETUKSEN_PAATTOVUOSI` | Perusopetuksen päättövuosi | — | — | — |
| `HAKUTOIVE` | Hakutoive | — | — | — |
| `SHAKUKOHTEEN_ORGANISAATIO_OID` | Suojattu hakukohteen organisaation yksilöintitunnus | — | — | — |
| `SHAKUKOHTEEN_OPPILAITOS_KOODI` | Suojattu hakukohteen oppilaitostunnus | — | — | — |
| `SHAKUKOHTEEN_OPETUSPISTE_KOODI` | Suojattu hakukohteen opetuspistekoodi | — | — | — |
| `SHAKUKOHTEEN_OID` | Suojattu hakukohteen yksilöintitunnus | — | — | — |
| `SHAKUKOHTEEN_KOODI` | Suojattu hakukohteen koodi | — | — | — |
| `HAKUKOHDE_SV` | Hakukohteen nimi ruotsiksi | — | — | — |
| `HAKUKOHTEEN_NIMI` | Hakukohteen nimi | — | — | — |
| `HAKUKOHTEEN_NIMI_SV` | Hakukohteen nimi ruotsiksi | — | — | — |
| `HAKUKOHTEEN_NIMI_EN` | Hakukohteen nimi englanniksi | — | — | — |
| `HAKUKOHTEEN_KOULUTUSKOODI` | Hakukohteen koulutuskoodi | — | — | — |
| `HAKUK_KOULK1` | Hakukohteen koulutuskoodi 1 | — | — | — |
| `HAKUK_KOULK2` | Hakukohteen koulutuskoodi 2 | — | — | — |
| `HAKUK_KOULK3` | Hakukohteen koulutuskoodi 3 | — | — | — |
| `HAKUK_KOULK4` | Hakukohteen koulutuskoodi 4 | — | — | — |
| `HAKUK_KOULK5` | Hakukohteen koulutuskoodi 5 | — | — | — |
| `HAKUK_SIS_KOULK1` | Hakukohteeseen sisältyvät koulutuskoodit | — | — | — |
| `SLNIMI` | Hakukohteen koulutuskoodin suomenkielinen lyhenne | — | — | — |
| `HAKUKOHTEEN_KUNTA_KAYNTIOSOITE` | Hakukohteen käyntiosoitteen kuntakoodi | — | — | — |
| `HAKUKOHTEEN_KUNTA_POSTIOSOITE` | Hakukohteen postiosoitteen kuntakoodi | — | — | — |
| `ORGANISAATION_KUNTAKOODI` | Organisaation kuntakoodi | — | — | — |
| `HAKUKOHTEEN_KIELI` | Hakukohteen opetuskieli | — | — | — |
| `KOULUTUKSEN_OPETUSKIELI1` | Koulutuksen opetuskieli | — | — | — |
| `HAKUKOHTEEN_KOULUTUSTYYPPI` | Hakukohteen koulutustyyppi | — | — | — |
| `HAKUKOHTEEN_KOULUTUSTYYPPITK` | Hakukohteen koulutustyyppi (koodattu TK:ssa) | — | — | — |
| `POHJAKOULUTUSVAATIMUS` | Pohjakoulutusvaatimus | — | — | — |
| `HARKINNANVARAINEN_VALINTA` | Harkinnanvarainen valinta | — | — | — |
| `HARKINNANVARAINEN_VALINTATK` | Harkinnanvarainen valinta (koodattu TK:ssa) | — | — | — |
| `HYVAKSYTTY_HARKINNANVARAISESTI` | Hyväksytty harkinnanvaraisesti | — | — | — |
| `OSALLISTUI_KIELIKOKEESEEN` | Osallistui kielikokeeseen | — | — | — |
| `YHTEISPISTEET` | Yhteispisteet | — | — | — |
| `ALIN_HYVAKSYTTY_PISTEMAARA` | Alin hyväksytty pistemäärä | — | — | — |
| `ALOITUSPAIKAT` | Aloituspaikat | — | — | — |
| `VALINTOJEN_ALOITUSPAIKAT` | Valintojen aloituspaikat | — | — | — |
| `JONOSIJA` | Jonosija | — | — | — |
| `HAKIJAN_LOPULLINEN_JONOSIJA` | Hakijan lopullinen jonosija | — | — | — |
| `HAKIJAN_JONOSIJAN_TARKENNE` | Hakijan jonosijan tarkenne | — | — | — |
| `VALINTATAPAJONO` | Valintatapajono | — | — | — |
| `VALINNAN_TILA` | Valinnan tila | — | — | — |
| `VALINNAN_TILATK` | Valinnan tila (koodattu TK:ssa) | — | — | — |
| `VALINNAN_TILAN_LISATIETO` | Valinnan tilan lisätieto | — | — | — |
| `VASTAANOTON_TILA` | Vastaanoton tila | — | — | — |
| `VASTAANOTON_TILATK` | Vastaanoton tila (koodattu TK:ssa) | — | — | — |
| `ILMOITTAUTUMISEN_TILA` | Ilmoittautumisen tila | — | — | — |
| `ILMOITTAUTUMISEN_TILATK` | Ilmoittautumisen tila (koodattu TK:ssa) | — | — | — |
| `HTOK` | Henkilötunnuksen oikeellisuus | — | — | — |
| `SLAHTOKOULUN_ORGANISAATIO_OID` | Suojattu lähtökoulun organisaation yksilöintitunnus | — | — | — |
| `SLAHTOKOULU` | Suojattu lähtökoulun oppilaitostunnus | — | — | — |
| `LAHTOKOULU_OKUN` | Lähtökoulun sijantikunta | — | — | — |
| `LAHTOKOULU_ONUTS3` | Lähtökoulun sijantimaakunta | — | — | — |
| `LAHTOKOULU_OKIELI` | Lähtökoulun kieli | — | — | — |
| `LAHTOKOULU_OLTYP` | Lähtökoulun oppilaitostyyppi | — | — | — |
| `LAHTOKOULU_OMIST` | Lähtökoulun omistajatyyppi | — | — | — |
| `OPMALA` | Hakukohteen koulutusala, 2002 luokitus | — | — | — |
| `OPMOPA` | Hakukohteen opintoala, 2002 luokitus | — | — | — |
| `OPMAST` | Hakukohteen koulutusaste, 2002 luokitus | — | — | — |
| `OPM95ALA` | Hakukohteen koulutusala, 1995 luokitus | — | — | — |
| `OPM95OPA` | Hakukohteen opintoala, 1995 luokitus | — | — | — |
| `OPM95AST` | Hakukohteen koulutusaste, 1995 luokitus | — | — | — |
| `KASTE_T2` | Ensimmäisen hakutoiveen koulutusaste | — | — | — |
| `ISCLE2011` | Koulutusaste 1-numeroisena (ISCED 2011) | — | — | — |
| `ISCCAT2011` | Koulutusaste 2-numeroisena (ISCED 2011) | — | — | — |
| `ISCSUBCAT2011` | Koulutusaste 3-numeroisena (ISCED 2011) | — | — | — |
| `ISCFIBROAD2013` | Koulutusala 2-numeroisena (ISCED 2013) | — | — | — |
| `ISCFINARROW2013` | Koulutusala 3-numeroisena (ISCED 2013) | — | — | — |
| `ISCFI2013` | Koulutusala 4-numeroisena (ISCED 2013) | — | — | — |
| `OKUN` | Hakukohteen oppilaitoksen sijantikunta | — | — | — |
| `ONUTS3` | Hakukohteen oppilaitoksen sijantimaakunta | — | — | — |
| `OKIELI` | Hakukohteen oppilaitoksen kieli | — | — | — |
| `OLTYP` | Hakukohteen oppilaitostyyppi | — | — | — |
| `OMIST` | Hakukohteen oppilaitoksen omistajatyyppi | — | — | — |

### Variable definitions

#### `TILV` — Tilastovuosi

Tieto vuodesta 2017 alkaen

#### `HAKUVUOSI` — Hakuvuosi

#### `HAKUKAUSI` — Hakukausi

K = kevät 
S = syksy

#### `KOULUTUKSEN_ALKAMISVUOSI` — Koulutuksen alkamisvuosi

#### `KOULUTUKSEN_ALKAMISKAUSI` — Koulutuksen alkamislukukausi

K = kevät 
S = syksy

#### `HAUN_KOHDEJOUKKO` — Haun kohdejoukko

10 = Aikuiskoulutus (2018-)
11 = Ammatillinen koulutus ja lukiokoulutus (2017-)
17 = Perusopetuksen jälkeinen valmistava koulutus (2017-)
18 = Vapaan sivistystyön koulutus (2018-)
20 = Erityisopetuksena järjestettävä ammatillinen koulutus (2017-)

Tieto vuodesta 2017 alkaen

#### `HAKUKOHTEIDEN_PRIORISOINTI` — Hakukohteiden priorisointi

1 = haussa hakutoiveiden priorisointi käytössä (=hakutoiveiden järjestys vaikuttaa)

Tieto vuodesta 2017 alkaen

#### `SHAKU_OID` — Suojattu haun yksilöintitunnus

Yksilöi haut vuodesta 2017 alkaen. Tieto aiemmilta vuosilta ei yksilöi hakuja eikä
ole vertailukelpoinen vuoden 2017 ja myöhempien vuosien tietojen kanssa (toistaiseksi).

#### `HAKU` — Haun nimi

Vuodesta 2014 alkaen:
1 = Ammatillisen koulutuksen ja lukiokoulutuksen kevään yhteishaku
2 = Ammatillisen koulutuksen ja lukiokoulutuksen syksyn yhteishaku
3 = Lisähaku kevään yhteishaussa vapaaksi jääneille opiskelupaikoille
4 = Lisähaku syksyn yhteishaussa vapaaksi jääneille opiskelupaikoille
5 = Perusopetuksen jälkeisen valmistavan koulutuksen kevään haku
6 = Perusopetuksen jälkeisen valmistavan koulutuksen kevään lisähaku
7 = Erityisopetuksena järjestettävän ammatillisen koulutuksen kevään haku
8 = Erityisopetuksena järjestettävän ammatillisen koulutuksen kevään lisähaku
Vuodesta 2017 alkaen:
2 = Ammatillisen koulutuksen syksyn yhteishaku 
Vuodesta 2018 alkaen:
9 = Lisähaku lukiokoulutukseen kevään yhteishaussa vapaaksi jääneille opiskelupaikoille
10 = Lisähaku kymppiluokalle ja lukioon valmistavaan koulutukseen
11 = Perusopetuksen jälkeisen valmistavan koulutuksen haku keväällä alkavaan koulutukseen
12 = Haku vaativana erityisenä tukena järjestettävään ammatilliseen koulutukseen, kevät
13 = Erityisopetuksen järjestettävän ammatillisen koulutuksen haku keväällä alkavaan koulutukseen
Vuodesta 2020 alkaen:
14 = Lisähaku kymppiluokalle

Aiempina vuosina esiintynyttä luokkaa 4 ei enää esiinny muuttujassa vuodesta 2017 alkaen. Vuodesta 2018 alkaen tietoa ei ole kaikilla havainnoilla ja muuttujan sisältö vaihtelee vuodesta toiseen. Sisällön tarkistamiseen  ja puuttuvien tietojen täydentämiseen voi käyttää aineiston muita muuttujia.

#### `HAKU_SV` — Haun nimi ruotsiksi

Vuodesta 2014 alkaen:
1 = Gemensam ansökan till yrkes- och gymnasieutbildning, våren
2 = Gemensam ansökan till yrkes- och gymnasieutbildning, hösten
3 = Tilläggsansökan till lediga platser i vårens gemensamma ansökan
4 = Tilläggsansökan till lediga platser i höstens gemensamma ansökan
5 = Ansökan till förberedande utbildningar efter grundskolan, våren
6 = Tilläggsansökan till förberedande utbildningar efter grundskolan, våren
7 = Ansökan till yrkesinriktad utbildning som anordnas som specialundervisning, våren
8 = Tilläggsansökan till yrkesinriktad utbildning som anordnas som specialundervisning, våren
Vuodesta 2017 alkaen:
2 = Gemensam ansökan till yrkesutbildning, hösten
Vuodesta 2018 alkaen:
9 = Tilläggsansökan till lediga gymnasieplatser i gemensam ansökan, våren
10 = Tilläggsansökan till tionde klassen och utbildning son förbereder för gymnasium
11 = Ansökan till förberedande utbildningar efter grundskolan som börjar på våren
12 = Ansökan till yrkesutbildning med krävande särskilt stöd, våren 
13 = Ansökan till yrkesinriktad specialundervisning som börjar på våren
Vuodesta 2020 alkaen:
14 =  Tilläggsansökan till tionde klassen

Aiempina vuosina esiintynyttä luokkaa 4 ei enää esiinny muuttujassa vuodesta 2017 alkaen. Vuodesta 2018 alkaen tietoa ei ole kaikilla havainnoilla ja muuttujan sisältö vaihtelee vuodesta toiseen. Sisällön tarkistamiseen  ja puuttuvien tietojen täydentämiseen on suositeltavaa käyttää aineiston muita muuttujia.

#### `HAKU_EN` — Haun nimi englanniksi

Tieto vuodesta 2017 alkaen

#### `HAKUTYYPPI_KOODI` — Hakutyyppi

01 = varsinainen haku 
03 = lisähaku

#### `HAKUTAPA_KOODI` — Hakutapa

1 = yhteishaku 
2 = erillishaku (2017-) 
3 = jatkuva haku (2017-)

#### `SHAKEMUS_OID` — Suojattu hakemuksen yksilöintitunnus

Vuodesta 2017 alkaen yksilöi hakemuksen tapauksissa, joissa yhdellä hakijalla on useampi hakemus samana hakuvuonna. Tieto aiemmilta vuosilta ei yksilöi hakemuksia (toistaiseksi).

#### `HAKEMUS_TILA` — Hakemuksen tila

ACTIVE = aktiivinen 
INCOMPLETE = keskeneräinen 

Muuttujan pohjalta muodostettu numeerinen muuttuja HAKEMUS_TILATK.

#### `HAKEMUS_TILATK` — Hakemuksen tila (koodattu TK:ssa)

1 = aktiivinen 
2 = keskeneräinen 

Muodostettu muuttujan HAKEMUS_TILA pohjalta.

#### `SHLOOID` — Suojattu henkilön yksilöintitunnus ODW:ssä

Vuodesta 2017 alkaen yksilöi henkilön ODW:ssä. Tieto aiemmilta vuosilta ei yksilöi henkilöitä eikä ole vertailukelpoinen vuoden 2017 ja myöhempien vuosien tietojen kanssa (toistaiseksi).

#### `SOPPIJANUMERO` — Suojattu oppijanumero

Tieto vain vuodelta 2015

#### `SHNRO` — Suojattu henkilön yksilöivä tunniste

Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e -tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä.

#### `SUKUPUOLI_KOODI` — Sukupuoli

1 = mies 
2 = nainen

#### `IKA` — Ikä

Ikä vuoden lopussa 1 vuoden tarkkuudella. Alle 13-vuotiaat on viety puuttuviksi. 
bl = tuntematon

#### `KOTIMAA` — Kotimaa

ISO 3166-N maakoodi 
999 = muu tai tuntematon 

Vuoden 2014 tieto hakuaineistosta

#### `AIKIELI` — Äidinkieli

ISO 639-standardin mukainen 2-merkkinen kielikoodi 
99 = muu tai tuntematon 

Tieto ensisijaisesti väestörekisteristä. Täydennetty hakuaineiston kielikoodi-muuttujasta henkilöille, joille ei löytynyt tietoa väestötietojärjestelmästä. Vuoden 2014 tieto hakuaineistosta.

#### `AIKIELI_LK` — Äidinkieli (luokiteltu)

fs = suomi, saame 
sv = ruotsi 
99 = muu tai tuntematon

Tieto vuoteen 2016 asti

#### `KIELIKOODI` — Äidinkieli alkuperäisessa aineistossa

ISO 639-standardin mukainen 2-merkkinen kielikoodi
99 = muu tai tuntematon

Tieto vuodesta 2017 alkaen

#### `KIELITYYPPI` — Äidinkieli pitkä alkuperäisessä aineistossa

Tieto vuodesta 2017 alkaen

#### `KANSAL` — Kansalaisuus

ISO 3166-N maakoodi, itsenäiset valtiot 
999 = muu tai tuntematon

Tieto ensisijaisesti VRK:sta, toissijaisesti hakuaineiston kansalaisuus-tieto. Vuoden 2014 tieto hakuaineistosta.

#### `HAKIJAN_KANSALAISUUS` — Hakijan kansalaisuus

Hakijan kansalaisuus alkuperäisessä aineistossa

Tieto vuodesta 2017 alkaen

#### `HAKIJAN_KANSALAISUUS2` — Hakijan kansalaisuus 2

Hakijan kansalaisuus alkuperäisessä aineistossa

Tieto vuodesta 2018 alkaen

#### `HAKIJAN_KANSALAISUUS3` — Hakijan kansalaisuus 3

Hakijan kansalaisuus alkuperäisessä aineistossa

Tieto vuodesta 2017 alkaen

#### `ASKUN` — Asuinkunta

Asuinkunta kuntaluokituksella tilastovuosi + 1 (muuttuja tilvaskun noudattaa tilastovuoden luokitusta). 
999 = tuntematon 

Tieto ensisijaisesti VRK:sta, toissijaisesti hakuaineiston muokattu kotikunta-tieto tilastovuoden lopussa. 
Tieto vuodesta 2015 alkaen.

#### `TILVASKUN` — Tilastovuoden asuinkunta

Asuinkunta tilastovuoden kuntaluokituksella (muuttuja askun noudattaa kuntaluokitusta tilastovuosi +1). 
999 = tuntematon 

Tieto ensisijaisesti VRK:sta, toissijaisesti hakuaineiston kotikunta-tieto tilastovuoden lopussa. Vuoden 2014 tieto hakuaineistosta.

#### `HAKIJAN_KOTIKUNTA` — Hakijan kotikunta

TK:n tilastovuoden kuntaluokitus

Tieto vuodesta 2017 alkaen

#### `POHJAKOULUTUSTK` — Pohjakoulutuskoodi

00 = Ulkomailla suoritettu koulutus 
01 = Perusopetuksen oppimäärä 
02 = Perusopetuksen osittain yksilöllistetty oppimäärä 
03 = Perusopetuksen yksilöllistetty oppimäärä, opetus järjestetty toiminta-alueittain 
06 = Perusopetuksen pääosin tai kokonaan yksilöllistetty oppimäärä 
07 = Oppivelvollisuuden suorittaminen keskeytynyt (ei päättötodistusta) 
09 = Lukion päättötodistus tai IB-, EB- tai RP-tutkinnon päättötodistus 

Alkuperäisen aineiston muuttujaan POHJAKOULUTUS  (2014-2016) ja POHJAKOULUTUS_2ASTE (2017-) lisätty TK:ssa etunolla, jotta voidaan yhdistää korkeakoulujen hakuaineiston kanssa.

#### `PAATTOLUOKKA` — Päättöluokka

9 = 9. luokka 
10 = 10. luokka 
A = ammattistartti 
AK = ammatillinen peruskoulutus 
L = lukio 
M = maahanmuuttajien ammatilliseen peruskoulutukseen valmistava koulutus 
ML = maahanmuuttujien lukiokoulutukseen valmistava koulutus 
V = vammaisten valmentava ja kuntouttava opetus ja ohjaus 
VALMA = ammatilliseen peruskoulutukseen valmentava koulutus 
TELMA = työhön ja itsenäiseen elämään valmentava koulutus 
99 = tuntematon 

Tieto vuoteen 2016 asti

#### `YKSILOITY` — Yksilöity

Muuttuja saa arvon true

Tieto vuodesta 2017 alkaen

#### `ULKOMAILLA_SUORITETUN_TOISEN_AST` — Ulkomailla suoritetun toisen asteen tutkinnon suoritusmaa

Tieto vain vuodelta 2017

#### `PERUSOPETUKSEN_OPETUSKIELI` — Perusopetuksen opetuskieli

2-merkkinen kielikoodi 
xx = muu kieli 
98 = ei virallinen kieli 
99 = tuntematon

Tieto vuoteen 2016 asti

#### `HAKIJAN_KOULUSIVISTYSKIELI` — Hakijan koulusivistyskieli

Kielikoodi
de = saksa
en = englanti
fi = suomi
se = saame
sv = ruotsi

Sisältää koodeja, joille ei selitettä.
Tieto vuodesta 2017 alkaen.

#### `PERUSOPETUKSEN_PAATTOVUOSI` — Perusopetuksen päättövuosi

Todistuksen saantivuosi 
bl = tuntematon

Tieto vuoteen 2018 asti

#### `HAKUTOIVE` — Hakutoive

Hakukohteiden järjestysnumero 1 - 5

#### `SHAKUKOHTEEN_ORGANISAATIO_OID` — Suojattu hakukohteen organisaation yksilöintitunnus

Yksilöi hakukohteet vuodesta 2017 alkaen. Tieto aiemmilta vuosilta ei yksilöi hakukohteita eikä siten ole vertailukelpoinen vuoden 2017 ja myöhempien vuosien tietojen kanssa (toistaiseksi).

#### `SHAKUKOHTEEN_OPPILAITOS_KOODI` — Suojattu hakukohteen oppilaitostunnus

Suojatun hakukohteen oppilaitostunnuksen avulla oppilaitoksen voi yhdistää muihin Tilastokeskuksen aineistoihin

#### `SHAKUKOHTEEN_OPETUSPISTE_KOODI` — Suojattu hakukohteen opetuspistekoodi

Tieto vuoteen 2016 asti

#### `SHAKUKOHTEEN_OID` — Suojattu hakukohteen yksilöintitunnus

Mahdollistaa tietojen yhdistämisen muihin OID-muuttujiin vuodesta 2017 alkaen. Tieto aiemmilta vuosilta ei ole vertailukelpoinen vuoden 2017 ja myöhempien vuosien OID-muuttujien kanssa (toistaiseksi). Hakukohteen yksilöintiin voi käyttää muuttujaa SHAKUKOHTEEN_KOODI.

#### `SHAKUKOHTEEN_KOODI` — Suojattu hakukohteen koodi

Yksilöi hakukohteen

#### `HAKUKOHDE_SV` — Hakukohteen nimi ruotsiksi

Tieto vuoteen 2016 asti.
Vrt. muuttujaan HAKUKOHTEEN_NIMI_SV vuodesta 2017 alkaen.

#### `HAKUKOHTEEN_NIMI` — Hakukohteen nimi

Tieto vuodesta 2017 alkaen

#### `HAKUKOHTEEN_NIMI_SV` — Hakukohteen nimi ruotsiksi

Tieto vuodesta 2017 alkaen

#### `HAKUKOHTEEN_NIMI_EN` — Hakukohteen nimi englanniksi

Tieto vuodesta 2017 alkaen

#### `HAKUKOHTEEN_KOULUTUSKOODI` — Hakukohteen koulutuskoodi

TK:n tilastovuoden koulutusluokituksen koulutuskoodit 

999999 = tuntematon 
Lisäksi tutkintoon johtamattomat koulutukset, joita ei löydy koulutusluokituksesta: 
020075 = Perusopetuksen lisäopetus 
038411= Kotitalousopetus (talouskoulu) 
039993 = Ammatilliseen peruskoulutukseen valmentava koulutus (VALMA) 
039994 = Ammatilliseen peruskoulutukseen valmentava koulutus (VALMA) erityisopetuksena 
039997 = Maahanmuuttajien ja vieraskielisten lukiokoulutukseen valmistava koulutus 
039999 = Työhön ja itsenäiseen elämään valmentava koulutus (TELMA)

Tieto vuoteen 2016 asti. 
Vuodesta 2017 alkaen ks. muuttuja HAKUK_KOULK1.

#### `HAKUK_KOULK1` — Hakukohteen koulutuskoodi 1

TK:n koulutusluokituksen koulutuskoodit

Muuttujissa HAKUK_KOULK1 - HAKUK_KOULK5 on tietoja, jos samalla hakukohteella on useita koulutuskoodeja. Pääsääntöisesti käytetään koulutuskooditietona HAKUK_KOULK1-muuttujan tietoa.

Lisäksi tutkintoon johtamattomat koulutukset, joita ei löydy koulutusluokituksesta: 
020075 = Perusopetuksen lisäopetus
999901 = Ammatilliseen peruskoulutukseen valmentava koulutus (VALMA)
999902 = Ammatilliseen peruskoulutukseen valmentava koulutus (VALMA), erityisopetuksena
999903 = Työhön ja itsenäiseen elämään valmentava koulutus (TELMA)

Tieto vuodesta 2017 alkaen

#### `HAKUK_KOULK2` — Hakukohteen koulutuskoodi 2

TK:n koulutusluokituksen koulutuskoodit

Muuttujissa HAKUK_KOULK1 - HAKUK_KOULK5 on tietoja, jos samalla hakukohteella on useita koulutuskoodeja. Pääsääntöisesti käytetään koulutuskooditietona HAKUK_KOULK1-muuttujan tietoa.

Lisäksi tutkintoon johtamattomat koulutukset, joita ei löydy koulutusluokituksesta: 
020075 = Perusopetuksen lisäopetus
999901 = Ammatilliseen peruskoulutukseen valmentava koulutus (VALMA)
999902 = Ammatilliseen peruskoulutukseen valmentava koulutus (VALMA), erityisopetuksena
999903 = Työhön ja itsenäiseen elämään valmentava koulutus (TELMA)

Tieto vuodesta 2017 alkaen

#### `HAKUK_KOULK3` — Hakukohteen koulutuskoodi 3

TK:n koulutusluokituksen koulutuskoodit

Muuttujissa HAKUK_KOULK1 - HAKUK_KOULK5 on tietoja, jos samalla hakukohteella on useita koulutuskoodeja. Pääsääntöisesti käytetään koulutuskooditietona HAKUK_KOULK1-muuttujan tietoa.

Lisäksi tutkintoon johtamattomat koulutukset, joita ei löydy koulutusluokituksesta: 
020075 = Perusopetuksen lisäopetus
999901 = Ammatilliseen peruskoulutukseen valmentava koulutus (VALMA)
999902 = Ammatilliseen peruskoulutukseen valmentava koulutus (VALMA), erityisopetuksena
999903 = Työhön ja itsenäiseen elämään valmentava koulutus (TELMA)

Tieto vuodesta 2017 alkaen

#### `HAKUK_KOULK4` — Hakukohteen koulutuskoodi 4

TK:n koulutusluokituksen koulutuskoodit

Muuttujissa HAKUK_KOULK1 - HAKUK_KOULK5 on tietoja, jos samalla hakukohteella on useita koulutuskoodeja. Pääsääntöisesti käytetään koulutuskooditietona HAKUK_KOULK1-muuttujan tietoa.

Lisäksi tutkintoon johtamattomat koulutukset, joita ei löydy koulutusluokituksesta: 
020075 = Perusopetuksen lisäopetus
999901 = Ammatilliseen peruskoulutukseen valmentava koulutus (VALMA)
999902 = Ammatilliseen peruskoulutukseen valmentava koulutus (VALMA), erityisopetuksena
999903 = Työhön ja itsenäiseen elämään valmentava koulutus (TELMA)

Tieto vuodesta 2017 alkaen

#### `HAKUK_KOULK5` — Hakukohteen koulutuskoodi 5

TK:n koulutusluokituksen koulutuskoodit

Muuttujissa HAKUK_KOULK1 - HAKUK_KOULK5 on tietoja, jos samalla hakukohteella on useita koulutuskoodeja. Pääsääntöisesti käytetään koulutuskooditietona HAKUK_KOULK1-muuttujan tietoa.

Lisäksi tutkintoon johtamattomat koulutukset, joita ei löydy koulutusluokituksesta: 
020075 = Perusopetuksen lisäopetus
999901 = Ammatilliseen peruskoulutukseen valmentava koulutus (VALMA)
999902 = Ammatilliseen peruskoulutukseen valmentava koulutus (VALMA), erityisopetuksena
999903 = Työhön ja itsenäiseen elämään valmentava koulutus (TELMA)

Tieto vuodesta 2017 alkaen

#### `HAKUK_SIS_KOULK1` — Hakukohteeseen sisältyvät koulutuskoodit

Hakukohteeseen sisältyvät koulutuskoodit  

Tietoa ei ole kaikilla. Hakukohteen koulutuskoodin saa muuttujasta HAKUK_KOULK1.
Tieto vuodesta 2017 alkaen.

#### `SLNIMI` — Hakukohteen koulutuskoodin suomenkielinen lyhenne

bl = tuntematon (ei tutkintoon johtamattomalla koulutuksella)

Lähde koulutusluokitus, pohjana muuttuja HAKUKOHTEEN_KOULUTUSKOODI. 
Tieto vuodesta 2015 alkaen.

#### `HAKUKOHTEEN_KUNTA_KAYNTIOSOITE` — Hakukohteen käyntiosoitteen kuntakoodi

TK:n tilastovuoden kuntaluokitus
999 = tuntematon

Tieto vuoteen 2016 asti

#### `HAKUKOHTEEN_KUNTA_POSTIOSOITE` — Hakukohteen postiosoitteen kuntakoodi

TK:n tilastovuoden kuntaluokitus
999 = tuntematon

Tieto vuoteen 2015 asti

#### `ORGANISAATION_KUNTAKOODI` — Organisaation kuntakoodi

Tieto vuodesta 2017 alkaen

#### `HAKUKOHTEEN_KIELI` — Hakukohteen opetuskieli

2-merkkinen kielikoodi 
xx = muu kieli 
98 = ei virallinen kieli 
99 = tuntematon

Tieto vuoteen 2016 asti

#### `KOULUTUKSEN_OPETUSKIELI1` — Koulutuksen opetuskieli

FI = suomi
SV = ruotsi
EN = englanti

Tieto vuodesta 2017 alkaen

#### `HAKUKOHTEEN_KOULUTUSTYYPPI` — Hakukohteen koulutustyyppi

AMMATILLINEN_PERUSKOULUTUS
AMM_OHJAAVA_JA_VALMISTAVA_KOUL
LUKIOKOULUTUS
MAAHANM_AMM_VALMISTAVA_KOULUTU
MAAHANM_LUKIO_VALMISTAVA_KOULU
PERUSOPETUKSEN_LISAOPETUS
VALMENTAVA_KUNTOUTTAVA_OPET
TUNTEMATON

Muuttujan pohjalta muodostettu numeerinen muuttuja HAKUKOHTEEN_KOULUTUSTYYPPITK.
Tieto vuoteen 2016 asti. Numeerinen muuttuja HAKUKOHTEEN_KOULUTUSTYYPPITK saatavilla myös vuoden 2016 jälkeen.

#### `HAKUKOHTEEN_KOULUTUSTYYPPITK` — Hakukohteen koulutustyyppi (koodattu TK:ssa)

2014

01 = Ammatillinen peruskoulutus
02 = Lukiokoulutus
03 = Maahanmuuttajien ja vieraskielisten lukiokoulutukseen valmistava koulutus
06 = Maahanmuuttajien ammatilliseen peruskoulutukseen valmistava koulutus
09 = Ammatilliseen peruskoulutukseen ohjaava ja valmistava koulutus
11 = Perusopetuksen lisäopetus

2015

01 = Ammatillinen peruskoulutus
02 = Lukiokoulutus
03 = Maahanmuuttajien ja vieraskielisten lukiokoulutukseen valmistava koulutus
04 = Työhön ja itsenäiseen elämään valmentava koulutus (TELMA) (alkup. aineistossa VALMENTAVA_JA_KUNTOUTTAVA_OPET)
11 = Perusopetuksen lisäopetus
12= Ammatilliseen peruskoulutukseen valmentava koulutus (VALMA) (poimittu hakukohteen koulutuskoodilla, alkup. aineistossa TUNTEMATON)
13= Ammatilliseen peruskoulutukseen valmentava koulutus (VALMA), erityisopetuksena (poimittu hakukohteen koulutuskoodilla, alkup. aineistossa TUNTEMATON)
14 = Kotitalousopetus (talouskoulu, alkup. aineistossa AMMATILLINEN_PERUSKOULUTUS)

2016

01 = Ammatillinen peruskoulutus
02 = Lukiokoulutus
03 = Maahanmuuttajien ja vieraskielisten lukiokoulutukseen valmistava koulutus
04 = Työhön ja itsenäiseen elämään valmentava koulutus (TELMA)
11 = Perusopetuksen lisäopetus
12= Ammatilliseen peruskoulutukseen valmentava koulutus (VALMA) (poimittu hakukohteen koulutuskoodilla, alkup. aineistossa TUNTEMATON)
13= Ammatilliseen peruskoulutukseen valmentava koulutus (VALMA), erityisopetuksena (poimittu hakukohteen koulutuskoodilla, alkup. aineistossa TUNTEMATON)

2017 - 2021

01 = Ammatillinen perustutkinto (2017-2018)
02 = Lukiokoulutus
04 = Ammatillinen perustutkinto erityisopetuksena
05 = Työhön ja itsenäiseen elämään valmentava koulutus (TELMA)
06 = Perusopetuksen lisäopetus
09 = Maahanmuuttajien ja vieraskielisten lukiokoulutukseen valmistava koulutus
10 = Vapaan sivistystyön koulutus (2018-)
11 = Ammattitutkinto (2018-)
12 = Erikoisammattitutkinto (2018-)
13 = Ammatillinen perustutkinto näyttötutintona (2018)
18 = Ammatilliseen peruskoulutukseen valmentava koulutus (VALMA)
19 = Ammatilliseen peruskoulutukseen valmentava koulutus (VALMA) erityisopetuksena
26 = Ammatillinen perustutkinto (reformin mukainen) (2018)

Muodostettu muuttujan HAKUKOHTEEN_KOULUTUSTYYPPI pohjalta

#### `POHJAKOULUTUSVAATIMUS` — Pohjakoulutusvaatimus

PK =  peruskoulun päättötodistus 
YO = ylioppilastutkinto (ei 2019) 
ER = peruskoulu / yksilöllistetty perusopetus

#### `HARKINNANVARAINEN_VALINTA` — Harkinnanvarainen valinta

oppimisvaikudet = oppimisvaikeudet 
sosiaalisetsyyt 
todistustenpuuttuminen 
todistustenvertailuvaikeudet
riittamatonkielitaito (2018-)
99999  = ei tietoa / tuntematon 

Muuttujan pohjalta muodostettu numeerinen muuttuja HARKINNANVARAINEN_VALINTATK

#### `HARKINNANVARAINEN_VALINTATK` — Harkinnanvarainen valinta (koodattu TK:ssa)

1 = oppimisvaikeudet 
2 = sosiaaliset syyt 
3 = todistusten puuttuminen 
4 = todistusten vertailuvaikeudet 
5 = riittämätön kielitaito (2018-)
99999  = ei tietoa / tuntematon

Muodostettu muuttujan HARKINNANVARAINEN_VALINTA pohjalta

#### `HYVAKSYTTY_HARKINNANVARAISESTI` — Hyväksytty harkinnanvaraisesti

0 = ei hyväksytty harkinnanvaraisesti 
1 = hyväksytty harkinnanvaraisesti

#### `OSALLISTUI_KIELIKOKEESEEN` — Osallistui kielikokeeseen

Tieto vuodesta 2017 alkaen

#### `YHTEISPISTEET` — Yhteispisteet

Muuttuja sisältää negatiivisia arvoja 

bl = tuntematon

#### `ALIN_HYVAKSYTTY_PISTEMAARA` — Alin hyväksytty pistemäärä

Tieto vuodesta 2017 alkaen

#### `ALOITUSPAIKAT` — Aloituspaikat

Hakijoille koulutustiedotuksessa ilmoitetut aloituspaikat

Tieto vuodesta 2015 alkaen

#### `VALINTOJEN_ALOITUSPAIKAT` — Valintojen aloituspaikat

Valinnoissa käytetyt "todelliset" aloituspaikat. Voi olla pienempi tai suurempi kuin edellä oleva "aloituspaikat" 

Tieto vuodesta 2015 alkaen

#### `JONOSIJA` — Jonosija

99999 = tuntematon

Tieto vain vuodelta 2015

#### `HAKIJAN_LOPULLINEN_JONOSIJA` — Hakijan lopullinen jonosija

Tieto vuodesta 2017 alkaen

#### `HAKIJAN_JONOSIJAN_TARKENNE` — Hakijan jonosijan tarkenne

Tieto vuodesta 2017 alkaen

#### `VALINTATAPAJONO` — Valintatapajono

Tieto vuodesta 2017 alkaen

#### `VALINNAN_TILA` — Valinnan tila

HYLATTY 
HYVAKSYTTY 
PERUNUT 
PERUUNTUNUT 
PERUUTETTU 
VARALLA 
VARASIJALTA_HYV
99999 = tuntematon

Muuttujan pohjalta muodostettu numeerinen muuttuja VALINNAN_TILATK

#### `VALINNAN_TILATK` — Valinnan tila (koodattu TK:ssa)

1 = hyväksytty 
2 = hylätty 
3 = perunut 
4 = peruuntunut 
5 = peruutettu 
6 = varalla 
7 = varasijalta hyväksytty 
9 = tuntematon

Muodostettu muuttujan VALINNAN_TILA pohjalta

#### `VALINNAN_TILAN_LISATIETO` — Valinnan tilan lisätieto

Kirjoitettuja selitteitä

Tieto vuodesta 2017 alkaen

#### `VASTAANOTON_TILA` — Vastaanoton tila

KESKEN 
PERUNUT 
PERUUTETTU 
EI_VASTAANOTETTU_MAARA_AIKANA 
VASTAANOTTANUT_SITOVASTI
TUNTEMATON (2018-)

Muuttujan pohjalta muodostettu numeerinen muuttuja VASTAANOTON_TILATK

#### `VASTAANOTON_TILATK` — Vastaanoton tila (koodattu TK:ssa)

1 = vastaanottanut sitovasti 
2 = ilmoitettu (arvo esiintyy vain vuonna 2014) 
3 = kesken 
4 = perunut 
5 = peruutettu 
6 = ei vastaanotettu määräaikana 
7 = vastaanottanut läsnäolevana (arvo esiintyy vain vuonna 2014) 
8 = vastaanottanut poissaolevana (arvo esiintyy vain vuonna 2014)
9 = tuntematon 

Muodostettu muuttujan VASTAANOTON_TILA pohjalta

#### `ILMOITTAUTUMISEN_TILA` — Ilmoittautumisen tila

EI_ILMOITTAUTUNUT 
EI_TEHTY 
LASNA 
LASNA_KOKO_LUKUVUOSI 
LASNA_SYKSY 
POISSA 
POISSA_KOKO_LUKUVUOS 
POISSA_SYKSY

Muuttujan pohjalta muodostettu numeerinen muuttuja ILMOITTAUTUMISEN_TILATK. Arvojen LASNA ja POISSA eroa muihin ei ole voitu varmistaa.
Tieto vuodesta 2016 alkaen.

#### `ILMOITTAUTUMISEN_TILATK` — Ilmoittautumisen tila (koodattu TK:ssa)

1 = läsnä koko lukuvuosi 
2 = läsnä syksy 
3 = läsnä 
4 = poissa 
5 = poissa koko lukuvuosi 
6 = poissa syksy 
7 = ei tehty 
8 = ei ilmoittautunut

Muodostettu muuttujan ILMOITTAUTUMISEN_TILA pohjalta. Arvojen 3 ja 4 eroa muihin ei ole voitu varmistaa. 
Tieto vuodesta 2016 alkaen.

#### `HTOK` — Henkilötunnuksen oikeellisuus

1 = oikea 
2 = puutteellinen 

Tieto vuosilta 2015 ja 2017 - 2020

#### `SLAHTOKOULUN_ORGANISAATIO_OID` — Suojattu lähtökoulun organisaation yksilöintitunnus

Vuodesta 2017 alkaen yksilöi lähtökoulun organisaation. Aiemmilta vuosilta ei yksilöi lähtökoulun organisaatiota eikä siten ole vertailukelpoinen vuoden 2017 ja myöhempien vuosien tietojen kanssa (toistaiseksi).

#### `SLAHTOKOULU` — Suojattu lähtökoulun oppilaitostunnus

Tieto korkeintaan vuoteen 2016 asti

#### `LAHTOKOULU_OKUN` — Lähtökoulun sijantikunta

TK:n tilastovuoden kuntaluokitus 
bl = tuntematon

Ensisijainen lähde oppilaitosrekisteri, pohjana muuttuja LAHTOKOULUN_OPPILAITOS_KOODI
Tieto vuoteen 2016 asti

#### `LAHTOKOULU_ONUTS3` — Lähtökoulun sijantimaakunta

TK:n tilastovuoden maakuntaluokitus 
bl = tuntematon

Ensisijainen lähde oppilaitosrekisteri, pohjana muuttuja LAHTOKOULUN_OPPILAITOS_KOODI.
Tieto vuoteen 2016 asti.

#### `LAHTOKOULU_OKIELI` — Lähtökoulun kieli

1 = suomi 
2 = ruotsi 
3 = suomi/ruotsi 
4 = englanti 
5 = saame 
9 = muu 
bl = tuntematon 

Lähde oppilaitosrekisteri, pohjana muuttuja LAHTOKOULUN_OPPILAITOS_KOODI.
Tieto vuoteen 2016 asti.

#### `LAHTOKOULU_OLTYP` — Lähtökoulun oppilaitostyyppi

Oppilaitostyyppi 1999 

11 = Peruskoulut 
12 = Peruskouluasteen erityiskoulut 
15 = Lukiot 
19 = Perus- ja lukioasteen koulut 
21 = Ammatilliset oppilaitokset 
22 = Ammatilliset erityisoppilaitokset 
23 = Ammatilliset erikoisoppilaitokset 
24 = Ammatilliset aikuiskoulutuskeskukset 
61 = Musiikkioppilaitokset 
62 = Liikunnan koulutuskeskukset 
63 = Kansanopistot 
64 = Kansalaisopistot 
bl = tuntematon 

Lähde oppilaitosrekisteri, pohjana muuttuja LAHTOKOULUN_OPPILAITOS_KOODI.
Tieto vain vuosilta 2015 - 2016.

#### `LAHTOKOULU_OMIST` — Lähtökoulun omistajatyyppi

1 = yksityinen 
2 = valtio 
3 = kunta 
4 = kuntayhtymä 
5 = Ahvenanmaa 
9 = muu 
bl = tuntematon 

Lähde oppilaitosrekisteri, pohjana muuttuja LAHTOKOULUN_OPPILAITOS_KOODI.
Tieto vuoteen 2016 asti.

#### `OPMALA` — Hakukohteen koulutusala, 2002 luokitus

Opetushallinnon koulutusluokitus 2002, koulutusala 

0 = Yleissivistävä koulutus 
1 = Humanistinen ja kasvatusala 
2 = Kulttuuriala 
3 = Yhteiskuntatieteiden, liiketalouden ja hallinnon ala 
4 = Luonnontieteiden ala 
5 = Tekniikan ja liikenteen ala 
6 = Luonnonvara- ja ympäristöala 
7 = Sosiaali-, terveys- ja liikunta-ala 
8 = Matkailu-, ravitsemis- ja talousala 
9 = Muu koulutus 
bl = tuntematon 

Pohjana muuttuja HAKUKOHTEEN_KOULUTUSKOODI.
Tieto vuoteen 2018 asti.

#### `OPMOPA` — Hakukohteen opintoala, 2002 luokitus

Opetushallinnon koulutusluokitus 2002, opintoala 

001 = Esiopetus
002 = Perusopetus
003 = Lukiokoulutus
099 = Muu yleissivistävä koulutus
101 = Vapaa-aika ja nuorisotyö
102 = Kielitieteet
103 = Historia ja arkeologia
104 = Filosofia
105 = Kasvatustieteet ja psykologia
106 = Opetus- ja kasvatustyö
107 = Teologia
199 = Muu humanistisen ja kasvatusalan koulutus
201 = Käsi- ja taideteollisuus
202 = Viestintä ja informaatiotieteet
203 = Kirjallisuus
204 = Teatteri ja tanssi
205 = Musiikki
206 = Kuvataide
207 = Kulttuurin- ja taiteiden tutkimus
299 = Muu kulttuurialan koulutus
301 = Liiketalous ja kauppa
302 = Kansantalous
303 = Hallinto
304 = Tilastotiede
305 = Sosiaalitieteet
306 = Politiikkatieteet
307 = Oikeustiede
399 = Muu yhteiskuntatieteiden, liiketalouden ja hallinnon alan koulutus
401 = Matematiikka
402 = Tietojenkäsittely
403 = Geo-, avaruus- ja tähtitieteet
404 = Fysiikka
405 = Kemia
406 = Biologia
407 = Maantiede
499 = Muu luonnontieteiden alan koulutus
501 = Arkkitehtuuri ja rakentaminen
502 = Kone-, metalli- ja energiatekniikka
503 = Sähkö- ja automaatiotekniikka
504 = Tieto- ja tietoliikennetekniikka
505 = Graafinen ja viestintätekniikka
506 = Elintarvikeala ja biotekniikka
507 = Prosessi-, kemian- ja materiaalitekniikka
508 = Tekstiili- ja vaatetustekniikka
509 = Ajoneuvo- ja kuljetustekniikka
510 = Tuotantotalous
599 = Muu tekniikan ja liikenteen alan koulutus
601 = Maatilatalous
602 = Puutarhatalous
603 = Kalatalous
604 = Metsätalous
605 = Luonto- ja ympäristöala
699 = Muu luonnonvara- ja ympäristöalan koulutus
701 = Sosiaaliala
702 = Terveysala
703 = Sosiaali- ja terveysala (alojen yhteiset ohjelmat)
704 = Hammaslääketiede ja muu hammashuolto
705 = Kuntoutus ja liikunta
706 = Tekniset terveyspalvelut
707 = Farmasia ja muu lääkehuolto
708 = Lääketiede
709 = Eläinlääketiede
710 = Kauneudenhoitoala
799 = Muu sosiaali-, terveys- ja liikunta-alan koulutus
801 = Matkailuala
802 = Majoitus- ja ravitsemisala
804 = Kotitalous- ja kuluttajapalvelut
805 = Puhdistuspalvelut
899 = Muu matkailu-, ravitsemis- ja talousalan koulutus
901 = Sotilas- ja rajavartioala
902 = Palo- ja pelastusala
903 = Poliisiala
904 = Vankeinhoito
969 = Muu opetusministeriön hallinnonalan ulkopuolella järjestettävä koulutus
998 = Muu opetusministeriön hallinnonalalla järjestettävä koulutus
bl = tuntematon 

Pohjana muuttuja HAKUKOHTEEN_KOULUTUSKOODI. 
Tieto vuoteen 2018 asti.

#### `OPMAST` — Hakukohteen koulutusaste, 2002 luokitus

Opetushallinnon koulutusluokitus 2002, koulutusaste 

31 = Lukiokoulutus 
32 = Ammatillinen koulutus 
bl = tuntematon

Pohjana muuttuja HAKUKOHTEEN_KOULUTUSKOODI.
Tieto vuoteen 2018 asti.

#### `OPM95ALA` — Hakukohteen koulutusala, 1995 luokitus

Opetushallinnon koulutusluokitus 1995,  koulutusala 

0 = Yleissivistävä koulutus 
1 = Luonnonvara-ala 
2 = Tekniikka ja liikenne 
3 = Hallinto ja kauppa 
4 = Ravitsemis- ja talousala 
5 = Terveys- ja sosiaaliala 
6 = Kulttuuriala 
7 = Humanistinen ja opetusala 
8 = Suojeluala 
9 = Muu koulutus 
bl = tuntematon 

Pohjana muuttuja HAKUKOHTEEN_KOULUTUSKOODI.
Tieto vuoteen 2016 asti.

#### `OPM95OPA` — Hakukohteen opintoala, 1995 luokitus

Opetushallinnon koulutusluokitus 1995, opintoala 

0 = Yleissivistävä koulutus
00 = Esiopetus
01 = Perusopetus
02 = Lukiokoulutus
04 = Muu yleissivistävä koulutus
1 = Luonnonvara-ala
05 = Maatilatalous
06 = Puutarhatalous
08 = Kalatalous
09 = Muu luonnonvara-ala
10 = Metsätalous
87 = Luonnontieteellinen koulutus
88 = Maatalous-metsätieteellinen koulutus
2 = Tekniikan ja liikenteen ala
17 = Graafinen ala
18 = LVI-ala
19 = Kone- ja metalliala
20 = Auto- ja kuljetusala
21 = Tekstiili- ja vaatetusala
22 = Elintarvikeala
24 = Sähköala
25 = Maanmittausala
26 = Rakennusala
27 = Puuala
28 = Pintakäsittelyala
29 = Paperi- ja kemianteollisuuden ala
37 = Merenkulkuala
38 = Muu tekniikka ja liikenne
56 = Tietoliikenne
57 = Lentoliikenne
89 = Teknillistieteellinen koulutus
3 = Kaupan ja hallinnon ala
40 = Kaupan ja hallinnon ala
82 = Yhteiskuntatieteellinen koulutus
85 = Oikeustieteellinen koulutus
86 = Kauppatieteellinen koulutus
4 = Matkailu-, ravitsemis- ja talousala
31 = Hotelli-, ravintola- ja suurtalousala
32 = Koti-, laitostalous- ja puhdistuspalveluala
5 = Sosiaali- ja terveysala
44 = Sosiaali- ja terveysala
45 = Kauneudenhoitoala
81 = Liikuntatieteellinen koulutus
84 = Terveystieteiden koulutus
90 = Lääketieteellinen koulutus
91 = Hammaslääketieteellinen koulutus
92 = Eläinlääketietieteellinen koulutus
93 = Farmasian koulutus
6 = Kulttuuriala
12 = Käsi- ja taideteollisuusala
13 = Viestintä- ja kuvataideala
64 = Musiikkiala
65 = Teatteri- ja tanssiala
77 = Taideteollinen koulutus
78 = Musiikkialan koulutus (yliopistot)
79 = Teatteri- ja tanssialan koulutus (yliopistot)
94 = Kuvataidealan koulutus (yliopistot)
7 = Humanistinen ja opetusala
63 = Vapaa-ajan toiminta
66 = Liikunta-ala
75 = Teologinen koulutus
76 = Humanistinen koulutus
80 = Kasvatustieteellinen koulutus
83 = Psykologian koulutus
9 = Muu koulutus
48 = Yrittäjyys
55 = Muu suojeluala
58 = Sotilas- ja rajavartiokoulutus
59 = Palokoulutus
60 = Poliisikoulutus
61 = Vankeinhoito
99 = Muu tai tuntematon opintoala
bl = tuntematon

Pohjana muuttuja HAKUKOHTEEN_KOULUTUSKOODI.
Tieto vuoteen 2016 asti.

#### `OPM95AST` — Hakukohteen koulutusaste, 1995 luokitus

Opetushallinnon koulutusluokitus 1995, koulutusaste 

0 = Aste eriytymättä 
1 = Toinen aste 
bl = tuntematon 

Pohjana muuttuja HAKUKOHTEEN_KOULUTUSKOODI.
Tieto vuoteen 2016 asti.

#### `KASTE_T2` — Ensimmäisen hakutoiveen koulutusaste

Koulutusluokitus 2016

Tieto vuodesta 2018 alkaen

#### `ISCLE2011` — Koulutusaste 1-numeroisena (ISCED 2011)

Unescon kansainvälisen koulutusluokituksen (ISCED 2011) 1-numeroinen koulutusaste tilastovuoden mukaisena. 

3 = Upper secondary education 
4 = Post-secondary non-tertiary education (2018-)
bl = tuntematon 

Pohjana muuttuja HAKUKOHTEEN_KOULUTUSKOODI. 
Tieto vuodesta 2015 alkaen.

#### `ISCCAT2011` — Koulutusaste 2-numeroisena (ISCED 2011)

Unescon kansainvälisen koulutusluokituksen (ISCED 2011) 2-numeroinen koulutusaste tilastovuoden mukaisena. 

34 = Upper secondary education, General 
35 = Upper secondary education, Vocational 
45 = Post-secondary non-tertiary education, Vocational  (2018-)
bl = tuntematon 

Pohjana muuttuja HAKUKOHTEEN_KOULUTUSKOODI. 
Tieto vuodesta 2015 alkaen.

#### `ISCSUBCAT2011` — Koulutusaste 3-numeroisena (ISCED 2011)

Unescon kansainvälisen koulutusluokituksen (ISCED 2011) 3-numeroinen koulutusaste tilastovuoden mukaisena. 

344 = Upper secondary education, General, Sufficient for level completion, with direct access to tertiary 
354 = Upper secondary education, Vocational, Sufficient for level completion, with direct access to tertiary
454 = Post-secondary non-tertiary education, Vocational, Sufficient for level completion, with direct access to tertiary education (2018-)
bl = tuntematon 

Pohjana muuttuja HAKUKOHTEEN_KOULUTUSKOODI. 
Tieto vuodesta 2015 alkaen.

#### `ISCFIBROAD2013` — Koulutusala 2-numeroisena (ISCED 2013)

Unescon kansainvälisen koulutusluokituksen (ISCED 2013) 2-numeroinen koulutusala tilastovuoden mukaisena (https://www.stat.fi/meta/luokitukset/isced_ala/001-2011/koko_luokitus.html) 
bl = tuntematon 

Pohjana muuttuja HAKUKOHTEEN_KOULUTUSKOODI. 
Tieto vuodesta 2015 alkaen.

#### `ISCFINARROW2013` — Koulutusala 3-numeroisena (ISCED 2013)

Unescon kansainvälisen koulutusluokituksen (ISCED 2013) 3-numeroinen koulutusala tilastovuoden mukaisena (https://www.stat.fi/meta/luokitukset/isced_ala/001-2011/koko_luokitus.html) 
bl = tuntematon 

Pohjana muuttuja HAKUKOHTEEN_KOULUTUSKOODI. 
Tieto vuodesta 2015 alkaen.

#### `ISCFI2013` — Koulutusala 4-numeroisena (ISCED 2013)

Unescon kansainvälisen koulutusluokituksen (ISCED 2013) 4-numeroinen koulutusala tilastovuoden mukaisena (https://www.stat.fi/meta/luokitukset/isced_ala/001-2011/koko_luokitus.html) 
bl = tuntematon 

Pohjana muuttuja HAKUKOHTEEN_KOULUTUSKOODI. 
Tieto vuodesta 2015 alkaen.

#### `OKUN` — Hakukohteen oppilaitoksen sijantikunta

TK:n tilastovuoden kuntaluokitus 
bl = tuntematon 

Lähde oppilaitosrekisteri, pohjana muuttuja HAKUKOHTEEN_OPPILAITOS_KOODI. 
Tieto vuodesta 2015 alkaen.

#### `ONUTS3` — Hakukohteen oppilaitoksen sijantimaakunta

TK:n tilastovuoden maakuntaluokitus 
bl = tuntematon 

Lähde oppilaitosrekisteri, pohjana muuttuja HAKUKOHTEEN_OPPILAITOS_KOODI. 
Tieto vuodesta 2015 alkaen.

#### `OKIELI` — Hakukohteen oppilaitoksen kieli

1 = suomi 
2 = ruotsi 
3 = suomi/ruotsi 
4 = englanti 
5 = saame 
9 = muu 
bl = tuntematon 

Lähde oppilaitosrekisteri, pohjana muuttuja HAKUKOHTEEN_OPPILAITOS_KOODI. 
Tieto vuodesta 2015 alkaen.

#### `OLTYP` — Hakukohteen oppilaitostyyppi

Oppilaitostyyppi 1999 

11 = Peruskoulut 
12 = Peruskouluasteen erityiskoulut 
15 = Lukiot 
19 = Perus- ja lukioasteen koulut 
21 = Ammatilliset oppilaitokset 
22 = Ammatilliset erityisoppilaitokset 
23 = Ammatilliset erikoisoppilaitokset 
24 = Ammatilliset aikuiskoulutuskeskukset 
61 = Musiikkioppilaitokset 
62 = Liikunnan koulutuskeskukset 
63 = Kansanopistot 
64 = Kansalaisopistot
bl = tuntematon 

Lähde oppilaitosrekisteri, pohjana muuttuja HAKUKOHTEEN_OPPILAITOS_KOODI. 
Tieto vuodesta 2015 alkaen.

#### `OMIST` — Hakukohteen oppilaitoksen omistajatyyppi

1 = yksityinen 
2 = valtio 
3 = kunta 
4 = kuntayhtymä 
5 = Ahvenanmaa 
9 = muu 
bl = tuntematon 

Lähde oppilaitosrekisteri, pohjana muuttuja HAKUKOHTEEN_OPPILAITOS_KOODI. 
Tieto vuodesta 2015 alkaen.

---

[← Back to catalogue](../../README.md)
