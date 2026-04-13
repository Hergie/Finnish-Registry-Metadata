# EDUC_OPISK Opiskelijat 1998

- **Identifier:** `EDUC_1998_jua_opisk_001.xml`
- **DOI:** `he_201304_ain_Opiskelutekeilla`
- **Temporal coverage:** 1998-01-01 - 1998-12-31
- **Published:** 2020-05-14
- **Organisation:** Tilastokeskus
- **Variable count:** 50
- **Observation count:** —
- **Population:** Tutkintoon johtavan koulutuksen opiskelijat Suomessa
- **Source:** TK: Oppilaitostilastot
- **Keywords:** Opiskelija,opiskelu,oppilas

## Kuvaus / Description

EDUC_OPISK Opiskelijat 1998 -vuositiedosto sisältää tutkintoon johtavassa koulutuksessa syksyllä 1998 päivälukioissa, ammatillisissa oppilaitoksissa, vakinaisissa ja väliaikaisissa ammattikorkeakouluissa ja yliopistoissa opiskelleet.
Vuosina 1996-1998 yliopistokoulutuksesta ovat mukana sekä oikean että puutteellisen henkilötunnuksen opiskelijat, mutta muilta koulutussektoreilta vain oikean henkilötunnuksen opiskelijat.

MUUTOKSIA VUOTEEN 1997 VERRATTUNA:	
	
- Lähes kaikkien muuttujien nimilyhenteet on muutettu samanlaisiksi kuin muissa	
  koulutustilastoaineistoissa. Muuttujien sijainti ja sisällöt ovat pysyneet samoina	
  alla olevia poikkeuksia lukuunottamatta.	
- Muuttuja alvv tutkinnon aloittamisvuosi: yliopisto-opiskelijoilla nykyisen tutkinnon 	
  aloittamisvuosi (tiekir), kun se edellisessä opiskelijarekisterissä oli kirjoihintulo yliopistoon (kirtu).	
- Vanhat koulutusluokituksen muuttujat on poistettu ja oppilaitostyyppi (oltyp) on siirretty pääasiallisen toiminnan (ptoim1) perään.	
	
YLEISIMMÄT KÄYTTÖTAVAT:

Tiedostossa ovat sekä läsnä- että poissaoleviksi syksyllä ilmoittautuneet opiskelijat. Syksyn 1998 läsnäolevat saadaan poimittua muuttujalla lasnas=1. Kevään 1998 läsnäolevat saadaan poimittua muuttujalla lasnak=1. Huom! Kevään läsnäolotieto koskee vain niitä opiskelijoita, jotka ovat olleet kirjoilla syksyllä (läsnä- tai poissaolevina).

Opiskelija voi samanaikaisesti opiskella useammassa koulutuksessa. Aineistossa ovat opiskelijan kaikki opiskelutiedot. Mikäli halutaan valita henkilölle vain yksi opiskelutieto, saadaan se muuttujalla oprior=1, joka valitsee viimeksi aloitetun ja koulutusluokituksen koulutusasteen mukaisen korkeimman koulutuksen. Oprior on muodostettu syksyllä läsnäoleville opiskelijoille.

Muuttujalla kryh saadaan valittua erikseen lukiokoulutuksessa, ammatillisessa koulutuksessa, ammattikorkeakoulukoulutuksessa sekä yliopistokoulutuksessa opiskelevat. Huom! Jos halutaan valita ammattikorkeakoulut, ne saa helpoimmin muuttujalla kryh=41 ja 42 tai muuttujalla opaste=4. Oppilaitostyypin "oltyp" arvolla 313 tulevat mukaan vain vakinaiset ammattikorkeakoulut.

Jos tiedot halutaan koulutuksittain, käytetään yleensä TK:n koulutusluokituksen (standardiluokitus) 6-numeroista koulutuskoodia, joka löytyy muuttujasta koulk.

TIETOLÄHTEET:

Tiedot päivälukioiden ja ammatillisten oppilaitosten sekä väliaikaisten ammattikorkeakoulujen opiskelijoista perustuvat pääteltyihin tietoihin. Tiedot ammatillisten oppilaitosten ja väliaikaisten ammattikorkeakoulujen opiskelijoiden osalta	perustuvat vuonna 1995 Tilastokeskuksen oppilaitoksilta keräämiin henkilöpohjaisiin tietoihin. Näihin on lisätty vuosina 1996, 1997 ja 1998 yhteishauissa ja yhteishakujen ulkopuolella aloittaneet sekä poistettu vuosina 1995, 1996, 1997 ja tammi-syysk./1998 tutkinnon suorittaneet. Päivälukioiden opiskelijoita koskevat tiedot perustuvat vuoden 1995 opetushallinnon valtionosuusjärjestelmän henkilöpohjaisiin tietoihin, joihin on lisätty vuosina 1996, 1997 ja 1998 yhteishauissa ja yhteishakujen ulkopuolella aloittaneet sekä poistettu vuosina 1995, 1996, 1997 ja 1998 ylioppilastutkinnon suorittaneet.

Tiedot vakinaisten ammattikorkeakoulujen sekä yliopistojen opiskelijoista perustuvat Tilastokeskuksen vuonna 1998 keräämiin henkilöpohjaisiin tietoihin. Vakinaisten ammattikorkeakoulujen opiskelijat ovat 20.9.1998 tilanteen mukaisia, yliopisto-opiskelijat 31.12.1998 tilanteen mukaisia. Väestötiedot ovat Tilastokeskuksen väestötiedostoista.

KARKEISTETUT MUUTTUJATIEDOT:

Valmisaineistomoduulista myönnetään lähtökohtaisesti karkeistettu versio EDUC_OPISK_K, jossa on karkeistettu tiedot kansalaisuudesta luokkiin suomi, muu Eurooppa ja muu, ja äidinkielestä luokkiin suomi, ruotsi ja muu.
  
Tästä valmisaineistomoduulista on mahdollista kuitenkin hakea karkeistamatonta versiota. Tämä löytyy lupapalvelusta nimellä EDUC_OPISK, ja maksaa saman verran. EDUC_OPISK sisältää muuten samat muuttujat, mutta kansalaisuus- ja äidinkielitiedot ovat karkeistamattomat. Tietojen käyttöön saaminen edellyttää erityistä tarvettä tutkimuksellisesta syystä sekä vahvoja perusteita.


Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@stat.fi

## Muuttujat / Variables (50)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `OPRIOR` | Opiskelun prioriteetti | — | — | — |
| `ALVV` | Tutkinnon aloittamisvuosi | — | — | — |
| `SP` | Sukupuoli | — | — | — |
| `TILV` | Aineistovuosi | — | — | — |
| `KOULK` | Tilastokeskuksen koulutuskoodi | — | koulutus_1_1998_01_01 | — |
| `LASNAS` | Kirjoilla 20.9. | — | — | — |
| `LASNAK` | Kirjoilla 20.1. | — | — | — |
| `ALLK` | Tutkinnon aloittamislukukausi | — | — | — |
| `KANSA` | Kansalaisuus | — | valtio_11_1970_01_01 | — |
| `AIKIELI2` | Äidinkieli | — | kieli_13_1998_01_01 | — |
| `AIKOUL` | Nuorten/aikuisten koulutus | — | — | — |
| `ASKUN` | Asuinkunta | — | kunta_1_1998_01_01 | — |
| `KKUN` | Opiskelukunta | — | kunta_1_1998_01_01 | — |
| `KRYH` | Koulutusryhmä | — | — | — |
| `JARJ` | Koulutuksen järjestäjä/ylläpitäjä | — | oppilaittostyyp_1_1996_01_01 | — |
| `KLOHKO` | Opetushallinnon koulutusala | — | — | — |
| `OPALA` | Opetushallinnon opintoala | — | opintoala_1_1997_01_01 | — |
| `OPASTE` | Opetushallinnon koulutusaste | — | — | — |
| `ATKLE` | Unescon koulutusaste | — | isced_aste_1_1997_01_01 | — |
| `ATKFI` | Unescon koulutusala | — | isced_ala_1_1997_01_01 | — |
| `ATKDE` | Unescon sijoittumistavoiteluokitus | — | isced_6_1997_01_01 | — |
| `ATKOR` | Unescon suuntautumisluokitus | — | isced_3_1997_01_01 | — |
| `ATKST` | Unescon kansallinen tutkintorakenne | — | isced_4_1997_01_01 | — |
| `ATKDU` | Unescon koulutuksen suunniteltu kesto | — | isced_5_1997_01_01 | — |
| `OLTYP` | Oppilaitostyyppi | — | oppilaittostyyp_1_1996_01_01 | — |
| `OMIST` | Oppilaitoksen omistajatyyppi | — | — | — |
| `OKIELI` | Oppilaitoksen opetuskieli | — | — | — |
| `OKUN` | Oppilaitoksen sijaintikunta | — | kunta_1_1998_01_01 | — |
| `ASLAANI` | Asuinlääni | — | — | — |
| `ASTEKE` | Asuinkunnan TE-keskus | — | tyov_elink_kesk_1_1997_09_01 | — |
| `ASNUTS3` | Asuinmaakunta | — | maakunta_1_1998_03_01 | — |
| `ASNUTS2` | Asuinkunnan suuralue | — | — | — |
| `ASKUNRYH` | Asuinkunnan kuntaryhmitys | — | — | — |
| `ASSEUTU` | Asuinkunnan seutukunta | — | seutukunta_1_1998_01_01 | — |
| `KLAANI` | Opiskelulääni | — | — | — |
| `KTEKE` | Opiskelukunnan työvoima-  ja elinkeinokeskus | — | tyov_elink_kesk_1_1997_09_01 | — |
| `KNUTS3` | Opiskelumaakunta | — | maakunta_1_1998_03_01 | — |
| `KNUTS2` | Opiskelukunnan suuralue | — | — | — |
| `KKUNRYH` | Opiskelukunnan kuntaryhmitys | — | — | — |
| `KSEUTU` | Opiskelukunnan seutukunta | — | seutukunta_1_1998_01_01 | — |
| `OLAANI` | Oppilaitoksen sijaintilääni | — | — | — |
| `OTEKE` | Oppilaitoksen työvoima-  ja elinkeinokeskus | — | tyov_elink_kesk_1_1997_09_01 | — |
| `ONUTS3` | Oppilaitoksen sijaintimaakunta | — | maakunta_1_1998_03_01 | — |
| `ONUTS2` | Oppilaitoksen suuraluekoodi | — | — | — |
| `OKUNRYH` | Oppilaitoksen sijaintikunnan  kuntaryhmitys | — | — | — |
| `OSEUTU` | Oppilaitoksen sijaintiseutukunta | — | seutukunta_1_1998_01_01 | — |
| `IKA` | Ikä vuosina | — | — | — |
| `AIKIELI` | Äidinkieli | — | kieli_21_1999_01_01 | — |
| `shnro` | Tilastokeskuksen suojattu henkilönumero | — | — | — |
| `s_oltunn` | Tilastokeskuksen suojattu oppilaitostunnus | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `OPRIOR` — Opiskelun prioriteetti

Viimeksi aloitettu ja TK:n koulutusasteen mukaan
korkein tavoitetutkinto. 1=korkein, 2=muu. 
Oprior muodostettu syksyn läsnäoleville opiskelijoille.

#### `ALVV` — Tutkinnon aloittamisvuosi

Päivälukioiden, ammatillisten oppilaitosten ja 
väliaikaisten ammattikorkeakoulujen opiskelijoilla 
0000 tarkoittaa vuotta 1995 tai aiemmin. 
Vakinaisten ammattikorkeakoulujen opiskelijoilla
ja yliopisto-opiskelijoilla tieto on ko. tutkinnon 
aloittamisvuosi.

#### `SP` — Sukupuoli

1=mies, 2=nainen

#### `TILV` — Aineistovuosi

Vuoden 1998 syksyn opiskelijat

#### `KOULK` — Tilastokeskuksen koulutuskoodi

**Luokitus / Classification:** koulutus_1_1998_01_01

Tilastokeskuksen koulutuskoodi 1998

#### `LASNAS` — Kirjoilla 20.9.

1=Läsnä (=opiskeli tai oli pakollisessa 
työharjoittelussa), 
2=Poissa (=opiskelija oli kirjoilla oppilaitoksessa, 
mutta ei opiskellut asepalveluksen, äitiysloman 
tai muun hyväksytyn syyn vuoksi)

#### `LASNAK` — Kirjoilla 20.1.

1=Läsnä (=opiskeli tai oli pakollisessa 
työharjoittelussa)
, 2=Poissa (=opiskelija oli kirjoilla oppilaitoksessa, 
mutta ei opiskellut asepalveluksen, äitiysloman
tai muun hyväksytyn syyn vuoksi), 
9=Ei ilmoittautumistietoa, 
bl=tieto puuttuu (päivälukiot, ammatill., väliaik.amk)
. Huom! Kevään läsnäolotieto koskee vain niitä 
opiskelijoita, jotka ovat olleet kirjoilla 
syksyllä (läsnä- tai poissaolevina).

#### `ALLK` — Tutkinnon aloittamislukukausi

1=kevät ja kesä, 2=syksy, 9=tieto puuttuu
. Vain vakinaisten ammattikorkeakoulujen ja 
yliopistojen opiskelijoilla, muilla blanco

#### `KANSA` — Kansalaisuus

**Luokitus / Classification:** valtio_11_1970_01_01

Väestötilastojen maaluokitus. 
Koodin 1. merkki maanosa. Karkeistettu tasolle suomi=1, muu Eurooppa=2, muu=3.

#### `AIKIELI2` — Äidinkieli

**Luokitus / Classification:** kieli_13_1998_01_01

Väestötilastojen kieliluokitus. Karkeistettu tasolle suomi=1, ruotsi=2, muu=3.

#### `AIKOUL` — Nuorten/aikuisten koulutus

1=nuorten koulutus, 
2=aikuisten koulutus

#### `ASKUN` — Asuinkunta

**Luokitus / Classification:** kunta_1_1998_01_01

Opiskelijan asuinkunta 31.12.1998. 
VRK:n kuntakoodi

#### `KKUN` — Opiskelukunta

**Luokitus / Classification:** kunta_1_1998_01_01

Opiskelukunta 1998
. VRK:n kuntakoodi

#### `KRYH` — Koulutusryhmä

21=Päivälukiot, 
31=Ammatilliset oppilaitokset, 
41=Ammattikorkeakoulut, vakinaiset, 
42=Ammattikorkeakoulut, väliaikaiset, 
51=Yliopistot

#### `JARJ` — Koulutuksen järjestäjä/ylläpitäjä

**Luokitus / Classification:** oppilaittostyyp_1_1996_01_01

TK:n oppilaitosluokitus 31.12.1998

#### `KLOHKO` — Opetushallinnon koulutusala

Opetushallinnon koulutusala 1998, 
0 = Yleissivistävä koulutus
, 1 = Luonnonvara-ala, 
2 = Tekniikan ja liikenteen ala, 
3 = Kaupan ja hallinnon ala, 
4 = Matkailu-, ravitsemis- ja talousala, 
5 = Sosiaali- ja terveysala, 
6 = Kulttuuriala, 
7 = Humanistinen ja opetusala, 
9 = Muu koulutus

#### `OPALA` — Opetushallinnon opintoala

**Luokitus / Classification:** opintoala_1_1997_01_01

Opetushallinnon opintoala 1998

#### `OPASTE` — Opetushallinnon koulutusaste

Opetushallinnon koulutusaste 1998
, 0 = Aste eriytymättä, 
1 = Toinen aste, 
2 = Opistoaste, 
3 = Ammatillinen korkea-aste, 
4 = Ammattikorkeakoulututkinto, 
5 = Alempi korkeakoulututkinto, 
6 = Ylempi korkeakoulututkinto, 
7 = Lisensiaattitutkinto
, 8 = Tohtorin tutkinto, 
9 = Muu tai tuntematon koulutusaste

#### `ATKLE` — Unescon koulutusaste

**Luokitus / Classification:** isced_aste_1_1997_01_01

ISCED 1997

#### `ATKFI` — Unescon koulutusala

**Luokitus / Classification:** isced_ala_1_1997_01_01

ISCED 1997, Field

#### `ATKDE` — Unescon sijoittumistavoiteluokitus

**Luokitus / Classification:** isced_6_1997_01_01

ISCED 1997, Destination

#### `ATKOR` — Unescon suuntautumisluokitus

**Luokitus / Classification:** isced_3_1997_01_01

ISCED 1997, Orientation

#### `ATKST` — Unescon kansallinen tutkintorakenne

**Luokitus / Classification:** isced_4_1997_01_01

ISCED 1997, National degree structure

#### `ATKDU` — Unescon koulutuksen suunniteltu kesto

**Luokitus / Classification:** isced_5_1997_01_01

ISCED 1997, Duration

#### `OLTYP` — Oppilaitostyyppi

**Luokitus / Classification:** oppilaittostyyp_1_1996_01_01

TK:n oppilaitosluokitus 31.12.1998

#### `OMIST` — Oppilaitoksen omistajatyyppi

TK:n oppilaitosluokitus 31.12.1998, 
1=Yksityinen, 
2=Valtio, 
3=Kunta, 
4=Kuntayhtymä, 
5=Ahvenanmaa, 
9=Muu

#### `OKIELI` — Oppilaitoksen opetuskieli

TK:n oppilaitosluokitus 31.12.1998, 
1=Suomi
, 2=Ruotsi, 
3=Suomi/ruotsi, 
5=Saame, 
9=Muu

#### `OKUN` — Oppilaitoksen sijaintikunta

**Luokitus / Classification:** kunta_1_1998_01_01

TK:n oppilaitosluokitus 31.12.1998
, VRK:n kuntakoodi

#### `ASLAANI` — Asuinlääni

31.12.1998, TK:n alueluokitus.
1=Etelä-Suomen
, 2=Länsi-Suomen, 
3=Itä-Suomen, 
4=Oulun, 
5=Lapin, 
6=Ahvenanmaa

#### `ASTEKE` — Asuinkunnan TE-keskus

**Luokitus / Classification:** tyov_elink_kesk_1_1997_09_01

31.12.1998, TK:n alueluokitus

#### `ASNUTS3` — Asuinmaakunta

**Luokitus / Classification:** maakunta_1_1998_03_01

31.12.1998, TK:n alueluokitus

#### `ASNUTS2` — Asuinkunnan suuralue

31.12.1998, TK:n alueluokitus. 
1=Uusimaa
, 2=Etelä-Suomi, 
3=Itä-Suomi
, 4=Väli-Suomi, 
5=Pohjois-Suomi, 
6=Ahvenanmaa

#### `ASKUNRYH` — Asuinkunnan kuntaryhmitys

31.12.1998, TK:n alueluokitus
. 1=Kaupunkimaiset kunnat
, 2=Taajaan asutut kunnat
, 3=Maaseutumaiset kunnat

#### `ASSEUTU` — Asuinkunnan seutukunta

**Luokitus / Classification:** seutukunta_1_1998_01_01

31.12.1998, TK:n alueluokitus

#### `KLAANI` — Opiskelulääni

TK:n alueluokitus, v. 1998. 
1=Etelä-Suomen, 
2=Länsi-Suomen, 
3=Itä-Suomen, 4=Oulun
, 5=Lapin
, 6=Ahvenanmaa

#### `KTEKE` — Opiskelukunnan työvoima- 
ja elinkeinokeskus

**Luokitus / Classification:** tyov_elink_kesk_1_1997_09_01

TK:n alueluokitus, v. 1998

#### `KNUTS3` — Opiskelumaakunta

**Luokitus / Classification:** maakunta_1_1998_03_01

TK:n alueluokitus, v. 1998

#### `KNUTS2` — Opiskelukunnan suuralue

TK:n alueluokitus, v. 1998. 
1=Uusimaa, 
2=Etelä-Suomi, 
3=Itä-Suomi
, 4=Väli-Suomi
, 5=Pohjois-Suomi
, 6=Ahvenanmaa

#### `KKUNRYH` — Opiskelukunnan kuntaryhmitys

TK:n alueluokitus, v. 1998. 
1=Kaupunkimaiset kunnat, 
2=Taajaan asutut kunnat, 
3=Maaseutumaiset kunnat

#### `KSEUTU` — Opiskelukunnan seutukunta

**Luokitus / Classification:** seutukunta_1_1998_01_01

TK:n alueluokitus, v. 1998

#### `OLAANI` — Oppilaitoksen sijaintilääni

TK:n alueluokitus, v. 1998. 
1=Etelä-Suomen, 
2=Länsi-Suomen
, 3=Itä-Suomen, 
4=Oulun, 
5=Lapin
, 6=Ahvenanmaa

#### `OTEKE` — Oppilaitoksen työvoima- 
ja elinkeinokeskus

**Luokitus / Classification:** tyov_elink_kesk_1_1997_09_01

TK:n alueluokitus, v. 1998

#### `ONUTS3` — Oppilaitoksen sijaintimaakunta

**Luokitus / Classification:** maakunta_1_1998_03_01

TK:n alueluokitus, v. 1998

#### `ONUTS2` — Oppilaitoksen suuraluekoodi

TK:n alueluokitus, v. 1998. 
1=Uusimaa, 
2=Etelä-Suomi, 
3=Itä-Suomi
, 4=Väli-Suomi
, 5=Pohjois-Suomi
, 6=Ahvenanmaa

#### `OKUNRYH` — Oppilaitoksen sijaintikunnan 
kuntaryhmitys

TK:n alueluokitus, v. 1998. 
1=Kaupunkimaiset kunnat, 
2=Taajaan asutut kunnat
, 3=Maaseutumaiset kunnat

#### `OSEUTU` — Oppilaitoksen sijaintiseutukunta

**Luokitus / Classification:** seutukunta_1_1998_01_01

TK:n alueluokitus, v. 1998

#### `IKA` — Ikä vuosina

Ikä vuosina 31.12.1998. 
bl = tieto puuttuu

#### `AIKIELI` — Äidinkieli

**Luokitus / Classification:** kieli_21_1999_01_01

Väestötilastojen kieliluokitus. Karkeistettu tasolle suomi=1, ruotsi=2, muu=3.

#### `shnro` — Tilastokeskuksen suojattu henkilönumero

#### `s_oltunn` — Tilastokeskuksen suojattu oppilaitostunnus

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
