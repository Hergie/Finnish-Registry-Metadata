# EDUC_ESIPERUS_K Esi- ja perusopetus 2020 - 2024

- **Identifier:** `EDUC_20202024_jua_esiperusk_001.xml`
- **DOI:** `work_2026-08_2026-08-13_ain_0001`
- **Temporal coverage:** 2020-01-01 - 2024-12-31
- **Published:** 2026-08-13
- **Organisation:** Tilastokeskus
- **Variable count:** 25
- **Observation count:** —
- **Population:** Esi- ja perusopetuksen oppilaat Suomessa
- **Source:** Tiedot pohjautuvat KOSKI-rekisteriin, Ahvenanmaan tilastoviraston aineistoihin sekä Helsingin eurooppalaisen koulun henkilöpohjaisiin oppilasaineistoihin.

## Description

EDUC_ESIPERUS_K –valmisaineistomoduuli sisältää tietoa henkilöiden demografisista taustatekijöistä, koulutuslajista, tutkinnon aloittamisvuodesta, oppilaitoksesta sekä opiskelujakson tilasta ja opiskeluoikeuden tyypistä. Tämä aineistokuvaus koskee EDUC_ESIPERUS_K-aineistoa, joka sisältää karkeistetut tiedot kansalaisuudesta ja äidinkielestä.

<b>Valmisaineiston tarkentava nimi</b>
Esi- ja perusopetuksessa kirjoilla olevat oppilaat ja heidän koulutus- ja taustatietonsa karkeistettuna (EDUC_ESIPERUS_K)

<b>Aineiston koostaminen, tietolähteet ja perusjoukko</b> 
Esi- ja perusopetusmoduuli kattaa oppilaat, jotka ovat olleet kirjoilla esi- tai perusopetuksessa 20. syyskuuta. Tiedot pohjautuvat KOSKI-rekisteriin, Ahvenanmaan tilastoviraston aineistoihin sekä Helsingin eurooppalaisen koulun henkilöpohjaisiin oppilasaineistoihin. Mukana ovat oppilaat, jotka opiskelevat peruskouluissa esiopetuksessa, peruskoulun vuosiluokilla 1–9 tai lisäopetuksessa (10-luokka tai perusopetukseen valmistava koulutus, eli pv). 

<b>Huomioitavaa aineistosta ja sen käytöstä</b> 
Esi- ja perusopetuksessa kirjoilla olevista oppilaista ja heidän koulutus- ja taustatiedoista on muodostettu kaksi valmisaineistoa: EDUC_ESIPERUS sekä EDUC_ESIPERUS_K. Karkeistamattoman aineiston käyttöön saaminen edellyttää erityistä tutkimuksellista tarvetta sekä vahvoja perusteita. 

Tietosisältö kattaa myös oppilaat, jotka ovat aloittaneet opintonsa ennen oppivelvollisuuden alkua. Esi- ja perusopetuksen oppilaiden tiedot ovat mukana aineistossa vuodesta 2020 alkaen. 

EDUC_ESIPERUS_K moduulin aineisto koostuu seuraavista tiedostoista: 
educ_esiperus_2020_k 
educ_esiperus_2021_k 
educ_esiperus_2022_k 
educ_esiperus_2023_k 
educ_esiperus_2024_k 

Opiskeluun liittyvät arkaluonteiset erityisopetustiedot ovat saatavilla erikseen. Näihin muuttujatietoihin myönnetään käyttöoikeus vain, jos tutkimuksellinen tarve on erityisen perusteltu. 

<b>Aineiston päivitysaikataulu</b>
Tutustu valmisaineistojen <a href="https://stat.fi/tup/tutkijapalvelut/valmisaineistojen-paivitysaikataulu.html" > päivitysaikatauluun</a>. 

<b>Aineiston käyttö ja tilaaminen</b> 
Aineisto on tarkoitettu käytettäväksi FIONA-etäpalvelun kautta, ja se on linkitettävissä muihin henkilövalmisaineistoihin suojatun henkilötunnisteen avulla. 

Valmisaineiston voi tilata tutkimuksen kohdejoukolle ja tarvittavalta ajanjaksolta. Kokonaisaineiston (kaikki muuttujat koko populaatiosta ja kaikilta saatavilla olevilta vuosilta) käyttöoikeus myönnetään vain, jos tutkimuksellinen tarve sitä erityisesti edellyttää. Lisäksi aineistosta voi tilata räätälöidyn version, joka sisältää vain osan muuttujista. 

Aineisto on FIONA-etäkäyttöjärjestelmässä jaettuina vuosikansioihin tilastovuosittain. 

<b>Tarkempaa tietoa muuttujista</b> 
* Jaottelu esiopetukseen, perusopetukseen, lisäopetukseen ja aikuisten opetukseen saadaan muuttujan KLAJI avulla. Aineisto on rajattu muuttujalla AIN, josta valitaan arvo ’10’ (esi- ja peruskoulutuksen aineisto). 
* Koulutuksessa läsnä olleet saadaan poimittua valitsemalla OLOSYYS-muuttujan 
arvoksi 1 (läsnä 20.9). 
* Perusopetuksen tiedoissa muuttujan OLOSYYS arvo 1 tarkoittaa, että oppilas on ollut läsnä 20.9. 
* Koulutuskohtainen tarkastelu tehdään yleensä koulutusluokituksen (standardiluokitus) 
6-numeroisen koulutuskoodin avulla, joka löytyy muuttujasta KOULK. Tämä koodi toimii myös avaimena eri 
koulutusluokituksiin. 
* Uudet opiskelijat tunnistetaan muuttujan ALVV avulla (ALVV=vuosi). Se tarkoittaa peruskoulun 1. vuosiluokan oppilaita. Muilla AIN = 10 -ryhmän oppilaiden kohdalla tämä tieto on tyhjä. 
* KKIELI-tieto ei ole saatavilla varhaiskasvatuksen esiopetustiedoissa. 
* Varhaiskasvatuksen esiopetuksessa muuttujan KKUN arvoksi on määritelty opetuksen järjestäjän kunta. 
 
Luokitukset: 
* Luokitustiedot ovat tilastovuodelta, ellei toisin mainita. 
* Tilastovuodesta 2016 alkaen Tilastokeskus on raportoinut koulutustiedot käyttäen uutta Kansallista 
koulutusluokitusta, joka vastaa Kansainvälistä ISCED 2011 -koulutusluokitusta. 
* Puuttuvat tiedot on usein koodattu numerolla yhdeksän (9). Kuntamuuttujissa koodi 200 viittaa 
ulkomaihin. 

<b>Lisätietoja</b> 
Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@stat.fi

## Variables (25)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `hid_e` | Suojattu henkilön yksilöivä tunniste | — | — | — |
| `vuosi` | Aineistovuosi | — | — | — |
| `vuosiluokka` | Vuosiluokka | — | — | — |
| `suoritus_perusteendiaarinumero` | Perusteen diaarinumero (vain KOSKI -tietovaranto) | — | — | — |
| `suoritus_kielikylpykieli` | Suorituksen kielikylpykieli (vain KOSKI -tietovaranto) | — | — | — |
| `perusop_opiskeluoikeus_tyyppi` | Opiskeluoikeuden tyyppi | — | — | — |
| `opiskelujakso_tila` | Opiskelujakson tila | — | — | — |
| `alkuennenoppivelvollisuutta` | Aloittanut ennen oppivelvollisuuden alkua | — | — | — |
| `opiskeluOid_s` | Suojattu opiskeluoikeuden tunnistenumero (KOSKI-tietovaranto) | — | — | — |
| `henkiloOid_s` | Suojattu henkilön tunnistenumero (KOSKI-tietovaranto) | — | — | — |
| `jarj_s` | Suojattu koulutuksen järjestäjä/ylläpitäjä | — | — | — |
| `oltunn_s` | Suojattu oppilaitostunnus | — | — | — |
| `kkun` | Koulutuksen sijaintikunta | — | kunta_1_2019_01_01 | — |
| `kkieli` | Koulutuksen opetuskieli | — | kieli_1_2010_11_15 | — |
| `koulk` | Tilastokeskuksen koulutuskoodi | — | koulutus_18_2018_01_01 | — |
| `ASKUNX` | Kotikunta / vakituinen asuinkunta edellisen vuoden lopussa | — | kunta_1_2018_01_01 | — |
| `askun` | Opiskelijan kotikunta | — | kunta_1_2019_01_01 | — |
| `alvv` | Tutkinnon aloittamisvuosi/kirjoilletulovuosi | — | — | — |
| `olosyys` | Kirjoilla 20.9 | — | kirjoilla_3_2018_01_01 | — |
| `ika` | Ikä tilastovuoden lopussa | — | — | — |
| `sp` | Sukupuoli | — | sukupuoli_2_1970_01_01 | — |
| `ain` | Lähdeaineisto | — | lahdeaineisto_1_2014_01_01 | — |
| `klaji` | Koulutuslaji (2020-) | — | — | — |
| `aikieli_k` | Äidinkieli, karkeistettu (2020-) | — | kieli_1_2010_11_15 | — |
| `kansal_k` | Kansalaisuus, karkeistettu (2020-) | — | valtio_1_2012_01_01 | — |

### Variable definitions

#### `hid_e` — Suojattu henkilön yksilöivä tunniste

Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e-tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä.

#### `vuosi` — Aineistovuosi

Viiteajankohdat:
* Perustopetus 2020-
  * 20.9.

#### `vuosiluokka` — Vuosiluokka

01 = 1. vuosiluokka
02 = 2. vuosiluokka
...
09 = 9. vuosiluokka

Tieto vuodesta 2020 alkaen. Vuodesta 2022 alkaen mukana myös PV muuttuja. PV = perusopetukseen valmistava opetus.

#### `suoritus_perusteendiaarinumero` — Perusteen diaarinumero (vain KOSKI -tietovaranto)

Tutkinnon perusteen diaarinumero
1/011/2004 = Perusopetuksen opetussuunnitelman perusteet 2004
102/011/2014 = Esiopetuksen opetussuunnitelman perusteet 2014
104/011/2014 = Perusopetuksen opetussuunnitelman perusteet 2014
105/011/2014 = Lisäopetuksen opetussuunnitelman perusteet 2014
19/011/2015 = Aikuisten perusopetuksen opetussuunnitelman perusteet 2015
3/011/2004 = Perusopetuksen lisäopetuksen opetussuunnitelman perusteet 2004
60/011/2015 = Työhön ja itsenäiseen elämään valmentava koulutus
OPH-1280_2017 = Aikuisten perusopetuksen opetussuunnitelman perusteet 2017
OPH-486-2021 = NA (toistaiseksi, lisätietoja ePerusteet-palvelu https://eperusteet.opintopolku.fi/#/fi)

Tieto vuodesta 2020 alkaen.

#### `suoritus_kielikylpykieli` — Suorituksen kielikylpykieli (vain KOSKI -tietovaranto)

Tieto vuodesta 2020 alkaen

#### `perusop_opiskeluoikeus_tyyppi` — Opiskeluoikeuden tyyppi

1 = esiopetus
2 = perusopetus
3 = international school
4 = perusopetuksen lisaopetus
5 = aikuisten perusopetus

Tieto vuodesta 2020 alkaen.

#### `opiskelujakso_tila` — Opiskelujakson tila

Tieto esi- ja perusopetuksesta.
Arvot:
lasna
valiaikaisestikeskeytynyt

Tieto vuodesta 2020 alkaen.

#### `alkuennenoppivelvollisuutta` — Aloittanut ennen oppivelvollisuuden alkua

Arvot:
true
false

Tieto vuodesta 2020 alkaen.

#### `opiskeluOid_s` — Suojattu opiskeluoikeuden tunnistenumero (KOSKI-tietovaranto)

Suojattu opiskeluoikeuden tunnistenumero KOSKI-tietovarannossa.

#### `henkiloOid_s` — Suojattu henkilön tunnistenumero (KOSKI-tietovaranto)

Suojattu henkilön tunnistenumero KOSKI-tietovarannossa.

#### `jarj_s` — Suojattu koulutuksen järjestäjä/ylläpitäjä

Suojattu koulutuksen järjestäjä/ylläpitäjä.

#### `oltunn_s` — Suojattu oppilaitostunnus

Suojattu oppilaitostunnus, 
TK:n oppilaitosluokitus 31.12., 
bl = ei tietoa (oppisopimuskoulutus)

#### `kkun` — Koulutuksen sijaintikunta

**Classification:** kunta_1_2019_01_01

Koulutuksen sijaintikunta 1.1. tilastovuonna 
VRK:n kuntakoodi
200=Ulkomaat
Oppisopimuskoulutuksessa ja varhaiskasvatuksen esiopetuksessa koulutuksen järjestäjän sijaintikunta.

#### `kkieli` — Koulutuksen opetuskieli

**Classification:** kieli_1_2010_11_15

Koulutuksen opetuskieli
2-kirjaiminen tunnus (ISO 639)


KKIELI-tietoa ei ole varhaiskasvatuksen esiopetustiedoilla.

#### `koulk` — Tilastokeskuksen koulutuskoodi

**Classification:** koulutus_18_2018_01_01

Tilastokeskuksen koulutusluokitus 1997 (6-numeroinen koulutuskoodi) ja siihen vuosittain tehdyt muutokset.
Koulutuskoodin 1. merkki kertoo koulutusasteen ja 2. merkki  koulutusalan.

#### `ASKUNX` — Kotikunta / vakituinen asuinkunta edellisen vuoden lopussa

**Classification:** kunta_1_2018_01_01

Opiskelijan kotikunta 31.12.[tilastovuotta edeltävä vuosi], luokitus 1.1.[tilastovuosi]
VRK:n kuntakoodi. 
200 = Ulkomaa
999 = Ei tietoa. Aluemuuttujaa ei enää päivitetä 2023 eteenpäin.

#### `askun` — Opiskelijan kotikunta

**Classification:** kunta_1_2019_01_01

Opiskelijan kotikunta vuoden lopussa (31.12.), luokitus 1.1. tilastovuosi +1
200 = Ulkomaa
999 = Ei tietoa
Tieto ensisijaisesti VRK:n aineistosta.
Puutteellisen henkilötunnuksen omaavilla oppilaitoksen ilmoittama tieto.

#### `alvv` — Tutkinnon aloittamisvuosi/kirjoilletulovuosi

Vuosi (vvvv), jolloin oppilas on ilmoittautunut koulun kirjoihin 20.9. mennessä.10 -ryhmässä (esi -ja perusopetus) ALVV-muuttuja tarkoittaa peruskoulun 1. vuosiluokan oppilaita. Muilla AIN = 10 -ryhmässä tieto on tyhjä.


9999 = ei tietoa.

#### `olosyys` — Kirjoilla 20.9

**Classification:** kirjoilla_3_2018_01_01

Vuodesta 2020 perusopetuksen tiedoille on määritely arvo 1 = läsnä 20.9.

#### `ika` — Ikä tilastovuoden lopussa

Ikä vuosina 31.12. Ikätieto on puutteellisen henkilötunnuksen omaavilla oppilaitoksen ilmoittama tieto.

#### `sp` — Sukupuoli

**Classification:** sukupuoli_2_1970_01_01

Sukupuoli
1 = Mies
2 = Nainen
9 = Määrittelemättä (2020-)
Sukupuolitieto puutteellisen henkilötunnuksen omaavilla oppilaitoksen ilmoittama tieto.

#### `ain` — Lähdeaineisto

**Classification:** lahdeaineisto_1_2014_01_01

Lähdeaineisto (karkea)
10 = esi ja perusopetusen aineisto (2020-)

#### `klaji` — Koulutuslaji (2020-)

Vuodesta 2020 alkaen:
10 = Esiopetus
11 = Perusopetus
12 = Aikuisten perusopetus
13 = Lisäopetus (10-luokka)

#### `aikieli_k` — Äidinkieli, karkeistettu (2020-)

**Classification:** kieli_1_2010_11_15

Opiskelijan äidinkieli 31.12. 
2-kirjaiminen tunnus (ISO 639-standardi). Tieto ensisijaisesti VRK:n aineistosta. Puutteellisen henkilotunnuksen omaavilla oppilaitoksen ilmoittama tieto.
 99 = ei tietoa.
 Karkeistettu tasolle suomi=1, ruotsi=2, muu=3.

#### `kansal_k` — Kansalaisuus, karkeistettu (2020-)

**Classification:** valtio_1_2012_01_01

Opiskelijan kansalaisuus vuoden lopussa.
Tieto ensisijaisesti VRK:n aineistosta (ISO 3166-standardi). Puutteellisen henkilötunnuksen omaavilla oppilaitoksen ilmoittama tieto.
 999=Ei tietoa.
 Karkeistettu tasolle suomi=1, muu Eurooppa=2, muu=3.

---

[← Back to catalogue](../../README.md)
