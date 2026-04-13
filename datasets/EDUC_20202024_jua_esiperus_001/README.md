# EDUC_ESIPERUS Oppilaat 2020 - 2024

- **Identifier:** `EDUC_20202024_jua_esiperus_001.xml`
- **DOI:** `he_201304_ain_Opiskelutekeilla`
- **Temporal coverage:** 2020-01-01 - 2024-12-31
- **Published:** 2025-12-18
- **Organisation:** Tilastokeskus
- **Variable count:** 25
- **Observation count:** —
- **Population:** Esi -ja perusopetuksen oppilaat Suomessa
- **Source:** TK: Oppilaitostilastot
- **Keywords:** Opiskelija,opiskelu,oppilas

## Kuvaus / Description

Esi- ja perusopetusmoduuli sisältää tiedot oppilaista, jotka ovat olleet 20.9. kirjoilla esi- ja perusopetuksessa.
Tiedot pohjautuvat KOSKI-rekisterin ja Ahvenanmaan tilastoviraston ja Helsingin eurooppalaisen koulun henkilöpohjaisiin oppilasaineistoihin, jotka opiskelevat peruskouluissa esiopetuksessa tai peruskoulun oppimäärää vuosiluokilla 1-9 tai lisäopetuksessa (10 -luokka tai pv eli perusopetukseen valmistava koulutus).
Sisältökuvaus
Tietosisältö kattaa myös ennen oppivelvollisuuden alkua aloittaneet oppilaat.
Esi- ja perusopetuksen oppilaiden tiedot ovat aineistossa vuodesta 2020 alkaen. 
EDUC_ESIPERUS moduulin aineisto koostuu seuraavista tiedostoista:	
educ_esiperus_2020
educ_esiperus_2021
educ_esiperus_2022
educ_esiperus_2023


Opiskelusta on erikseen saatavilla arkaluonteisia erityisopetukseen liittyviä muuttujia, joihin annetaan
käyttöoikeus vain, jos niihin on tutkimuksellisesta syystä erityinen tarve.

YLEISIMMÄT KÄYTTÖTAVAT:
* Jaottelu esiopetukseen, perusopetukseen, lisäopetukseen ja aikuisten opetukseen saadaan muuttujan KLAJI avulla. Aineisto on rajattu AIN -muuttujan avulla, niin että lähdeaineistosta otetaan arvo ’10’ (esi-ja peruskoulutuksen aineisto).
* Koulutuksessa läsnä olleet saadaan poimittua valitsemalla OLOSYYS -muuttujan
arvo 1 (=20.9).
* Muuttujassa OLOSYYS perusopetuksen tiedoille on määritelty arvo 1 = läsnä 20.9.
* Jos tiedot halutaan koulutuksittain, käytetään yleensä koulutusluokituksen (standardiluokitus)
6-numeroista koulutuskoodia, joka löytyy muuttujasta KOULK. Koulutuskoodi on myös avain eri
koulutusluokituksiin.
* Uudet opiskelijat saadaan muuttujan ALVV avulla (ALVV=vuosi). 
* ALVV-muuttuja tarkoittaa peruskoulun 1. vuosiluokan oppilaita. Muilla AIN = 10 -ryhmässä tieto on tyhjä.
* KKIELI tietoa ei ole varhaiskasvatuksen esiopetustiedoilla.
* Varhaiskasvatuksen esiopetuksen KKUN-tiedoksi on määritelty järjestäjän kunta.

LUOKITUKSET:
* Luokitustiedot ovat tilastovuodelta, mikäli muuta mainintaa ei ole.
* Tilastovuodesta 2016 alkaen Tilastokeskus raportoi koulutustiedot käyttäen uutta Kansallista
koulutusluokitusta, joka vastaa Kansainvälistä ISCED 2011 -koulutusluokitusta.
* Puuttuvat tiedot on usein koodattu merkillä yhdeksän (9) ja kuntamuuttujissa koodi 200 viittaa
ulkomaihin.

KARKEISTETUT MUUTTUJATIEDOT:
Valmisaineistomoduulista myönnetään lähtökohtaisesti karkeistettu versio EDUC_ESIPERUS_K, jossa on karkeistettu tiedot kansalaisuudesta luokkiin suomi, muu Eurooppa ja muu, ja äidinkielestä luokkiin suomi, ruotsi ja muu.
  
Tästä valmisaineistomoduulista on mahdollista kuitenkin hakea karkeistamatonta versiota. Tämä löytyy lupapalvelusta nimellä EDUC_ESIPERUS, ja maksaa saman verran. EDUC_ESIPERUS sisältää muuten samat muuttujat, mutta kansalaisuus- ja äidinkielitiedot ovat karkeistamattomat. Tietojen käyttöön saaminen edellyttää erityistä tarvettä tutkimuksellisesta syystä sekä vahvoja perusteita.

Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@stat.fi

## Muuttujat / Variables (25)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `vuosi` | Aineistovuosi | — | — | — |
| `hid_e` | Suojattu henkilön yksilöivä tunniste | — | — | — |
| `ain` | Lähdeaineisto | — | lahdeaineisto_1_2014_01_01 | — |
| `klaji` | Koulutuslaji (2020-) | — | — | — |
| `sp` | Sukupuoli | — | sukupuoli_2_1970_01_01 | — |
| `ika` | Ikä tilastovuoden lopussa | — | — | — |
| `kansal` | Kansalaisuus (2020-) | — | valtio_1_2012_01_01 | — |
| `aikieli` | Äidinkieli (2020-) | — | kieli_1_2010_11_15 | — |
| `olosyys` | Kirjoilla 20.9 | — | kirjoilla_3_2018_01_01 | — |
| `alvv` | Tutkinnon aloittamisvuosi/kirjoilletulovuosi | — | — | — |
| `askun` | Opiskelijan kotikunta | — | kunta_1_2019_01_01 | — |
| `ASKUNX` | Kotikunta / vakituinen asuinkunta edellisen vuoden lopussa | — | kunta_1_2018_01_01 | — |
| `koulk` | Tilastokeskuksen koulutuskoodi | — | koulutus_18_2018_01_01 | — |
| `kkieli` | Koulutuksen opetuskieli | — | kieli_1_2010_11_15 | — |
| `kkun` | Koulutuksen sijaintikunta | — | kunta_1_2019_01_01 | — |
| `oltunn_s` | Suojattu oppilaitostunnus | — | — | — |
| `jarj_s` | Suojattu koulutuksen järjestäjä/ylläpitäjä | — | — | — |
| `henkiloOid_s` | Suojattu henkilön tunnistenumero (KOSKI-tietovaranto) | — | — | — |
| `opiskeluOid_s` | Suojattu opiskeluoikeuden tunnistenumero (KOSKI-tietovaranto) | — | — | — |
| `alkuennenoppivelvollisuutta` | Aloittanut ennen oppivelvollisuuden alkua | — | — | — |
| `opiskelujakso_tila` | Opiskelujakson tila | — | — | — |
| `perusop_opiskeluoikeus_tyyppi` | Opiskeluoikeuden tyyppi | — | — | — |
| `suoritus_kielikylpykieli` | Suorituksen kielikylpykieli (vain KOSKI -tietovaranto) | — | — | — |
| `suoritus_perusteendiaarinumero` | Perusteen diaarinumero (vain KOSKI -tietovaranto) | — | — | — |
| `vuosiluokka` | Vuosiluokka | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `vuosi` — Aineistovuosi

Viiteajankohdat:
* Perustopetus 2020-
  * 20.9.

#### `hid_e` — Suojattu henkilön yksilöivä tunniste

Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e-tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä.

#### `ain` — Lähdeaineisto

**Luokitus / Classification:** lahdeaineisto_1_2014_01_01

Lähdeaineisto (karkea)
10 = esi ja perusopetusen aineisto (2020-)

#### `klaji` — Koulutuslaji (2020-)

Vuodesta 2020 alkaen:
10 = Esiopetus
11 = Perusopetus
12 = Aikuisten perusopetus
13 = Lisäopetus (10-luokka)

#### `sp` — Sukupuoli

**Luokitus / Classification:** sukupuoli_2_1970_01_01

Sukupuoli
1 = Mies
2 = Nainen
9 = Määrittelemättä (2020-)
Sukupuolitieto puutteellisen henkilötunnuksen omaavilla oppilaitoksen ilmoittama tieto.

#### `ika` — Ikä tilastovuoden lopussa

Ikä vuosina 31.12. Ikätieto on puutteellisen henkilötunnuksen omaavilla oppilaitoksen ilmoittama tieto.

#### `kansal` — Kansalaisuus (2020-)

**Luokitus / Classification:** valtio_1_2012_01_01

Opiskelijan kansalaisuus vuoden lopussa.
Tieto ensisijaisesti VRK:n aineistosta (ISO 3166-standardi). Puutteellisen henkilötunnuksen omaavilla oppilaitoksen ilmoittama tieto.
 999=Ei tietoa.
 Karkeistettu tasolle suomi=1, muu Eurooppa=2, muu=3.

#### `aikieli` — Äidinkieli (2020-)

**Luokitus / Classification:** kieli_1_2010_11_15

Opiskelijan äidinkieli 31.12.
2-kirjaiminen tunnus (ISO 639-standardi). Tieto ensisijaisesti VRK:n aineistosta. Puutteellisen henkilotunnuksen omaavilla oppilaitoksen ilmoittama tieto.
 99 = ei tietoa.
 Karkeistettu tasolle suomi=1, ruotsi=2, muu=3.

#### `olosyys` — Kirjoilla 20.9

**Luokitus / Classification:** kirjoilla_3_2018_01_01

Vuodesta 2020 perusopetuksen tiedoille on määritely arvo 1 = läsnä 20.9.

#### `alvv` — Tutkinnon aloittamisvuosi/kirjoilletulovuosi

Vuosi (vvvv), jolloin oppilas on ilmoittautunut koulun kirjoihin 20.9. mennessä.10 -ryhmässä (esi -ja perusopetus) ALVV-muuttuja tarkoittaa peruskoulun 1. vuosiluokan oppilaita. Muilla AIN = 10 -ryhmässä tieto on tyhjä.


9999 = ei tietoa.

#### `askun` — Opiskelijan kotikunta

**Luokitus / Classification:** kunta_1_2019_01_01

Opiskelijan kotikunta vuoden lopussa (31.12.), luokitus 1.1. tilastovuosi +1
200 = Ulkomaa
999 = Ei tietoa
Tieto ensisijaisesti VRK:n aineistosta.
Puutteellisen henkilötunnuksen omaavilla oppilaitoksen ilmoittama tieto.

#### `ASKUNX` — Kotikunta / vakituinen asuinkunta edellisen vuoden lopussa

**Luokitus / Classification:** kunta_1_2018_01_01

Opiskelijan kotikunta 31.12.[tilastovuotta edeltävä vuosi], luokitus 1.1.[tilastovuosi]
VRK:n kuntakoodi. 
200 = Ulkomaa
999 = Ei tietoa. Aluemuuttujaa ei enää päivitetä 2023 eteenpäin.

#### `koulk` — Tilastokeskuksen koulutuskoodi

**Luokitus / Classification:** koulutus_18_2018_01_01

Tilastokeskuksen koulutusluokitus 1997 (6-numeroinen koulutuskoodi) ja siihen vuosittain tehdyt muutokset.
Koulutuskoodin 1. merkki kertoo koulutusasteen ja 2. merkki  koulutusalan.

#### `kkieli` — Koulutuksen opetuskieli

**Luokitus / Classification:** kieli_1_2010_11_15

Koulutuksen opetuskieli
2-kirjaiminen tunnus (ISO 639)


KKIELI-tietoa ei ole varhaiskasvatuksen esiopetustiedoilla.

#### `kkun` — Koulutuksen sijaintikunta

**Luokitus / Classification:** kunta_1_2019_01_01

Koulutuksen sijaintikunta 1.1. tilastovuonna 
VRK:n kuntakoodi
200=Ulkomaat
Oppisopimuskoulutuksessa ja varhaiskasvatuksen esiopetuksessa koulutuksen järjestäjän sijaintikunta.

#### `oltunn_s` — Suojattu oppilaitostunnus

Suojattu oppilaitostunnus, 
TK:n oppilaitosluokitus 31.12., 
bl = ei tietoa (oppisopimuskoulutus)

#### `jarj_s` — Suojattu koulutuksen järjestäjä/ylläpitäjä

Suojattu koulutuksen järjestäjä/ylläpitäjä.

#### `henkiloOid_s` — Suojattu henkilön tunnistenumero (KOSKI-tietovaranto)

Suojattu henkilön tunnistenumero KOSKI-tietovarannossa.

#### `opiskeluOid_s` — Suojattu opiskeluoikeuden tunnistenumero (KOSKI-tietovaranto)

Suojattu opiskeluoikeuden tunnistenumero KOSKI-tietovarannossa.

#### `alkuennenoppivelvollisuutta` — Aloittanut ennen oppivelvollisuuden alkua

Arvot:
true
false

Tieto vuodesta 2020 alkaen.

#### `opiskelujakso_tila` — Opiskelujakson tila

Tieto esi- ja perusopetuksesta.
Arvot:
lasna
valiaikaisestikeskeytynyt

Tieto vuodesta 2020 alkaen.

#### `perusop_opiskeluoikeus_tyyppi` — Opiskeluoikeuden tyyppi

1 = esiopetus
2 = perusopetus
3 = international school
4 = perusopetuksen lisaopetus
5 = aikuisten perusopetus

Tieto vuodesta 2020 alkaen.

#### `suoritus_kielikylpykieli` — Suorituksen kielikylpykieli (vain KOSKI -tietovaranto)

Tieto vuodesta 2020 alkaen

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

#### `vuosiluokka` — Vuosiluokka

01 = 1. vuosiluokka
02 = 2. vuosiluokka
...
09 = 9. vuosiluokka

Tieto vuodesta 2020 alkaen. Vuodesta 2022 alkaen mukana myös PV muuttuja. PV = perusopetukseen valmistava opetus.

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
