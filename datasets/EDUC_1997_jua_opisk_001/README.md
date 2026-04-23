# EDUC_OPISK Opiskelijat 1997

- **Identifier:** `EDUC_1997_jua_opisk_001.xml`
- **DOI:** `he_201304_ain_Opiskelutekeilla`
- **Temporal coverage:** 1997-01-01 - 1997-12-31
- **Published:** 2020-05-14
- **Organisation:** Tilastokeskus
- **Variable count:** 55
- **Observation count:** —
- **Population:** Tutkintoon johtavan koulutuksen opiskelijat Suomessa
- **Source:** TK: Oppilaitostilastot
- **Keywords:** Opiskelija,opiskelu,oppilas

## Description

EDUC_OPISK Opiskelijat 1997-vuositiedosto sisältää tutkintoon johtavassa koulutuksessa syksyllä 1997 päivälukioissa, ammatillisissa oppilaitoksissa, vakinaisissa ja väliaikaisissa ammattikorkeakouluissa ja yliopistoissa opiskelleet.

MUUTOKSIA VUOTEEN 1996 VERRATTUNA:

- Uusia muuttujia mm.: kansa, kieli, lasnak, lasnas, alvv, allk, oprior, koty (1995 nimellä aikoul) 	
- Muuttuja uusi on jätetty pois (tiedon saa muuttujasta alvv)	
- Useiden muuttujien nimiä on muutettu, esim.: 	
   * Opryh-muuttuja on sama kuin kryh 	
   * Tyyppi-muuttuja on sama kuin oltyp	
   * Koulkx-muuttuja on sama kuin koulk5	
- Aluetietojen muuttujanimiä on muutettu ja aluemuuttujia on tullut lisää	
- Oppilaitosmuuttujia on tullut lisää (nimi, omistaja, jarjest, opkieli)

YLEISIMMÄT KÄYTTÖTAVAT:

Tiedostossa ovat sekä läsnä- että poissaoleviksi syksyllä ilmoittautuneet opiskelijat. 
Syksyn läsnäolevat saadaan valittua muuttujalla lasnas=1.

Opiskelija voi samanaikaisesti opiskella useammassa koulutuksessa. Aineistossa ovat opiskelijan kaikki opiskelutiedot. Mikäli halutaan valita henkilölle vain yksi opiskelutieto, se saadaan muuttujalla oprior=1, joka valitsee viimeksi aloitetun ja uuden koulutusluokituksen koulutusasteen mukaisen korkeimman koulutuksen. Oprior on muodostettu syksyllä läsnäoleville opiskelijoille.
Muuttujalla opryh saadaan valittua erikseen lukiokoulutuksessa, ammatillisessa koulutuksessa, ammattikorkeakoulutuksessa tai yliopistokoulutuksessa opiskelevat.  Huom! Jos halutaan valita ammattikorkeakoulut, ne saa helpoimmin  muuttujalla opryh=41 ja 42 tai muuttujalla opaste=4. Oppilaitostyypin "tyyppi" arvolla 313 tulevat mukaan vain vakinaiset ammattikorkeakoulut. Jos tiedot halutaan koulutuksittain, käytetään yleensä TK:n koulutusluokituksen (standardiluokitus) 6-numeroista  koulutuskoodia, joka löytyy muuttujasta koulk.

LUOKITUKSET:

Tiedostossa ovat sekä TK:n vanhan koulutusluokituksen 5-numeroiset koulutuskoodit (ja niihin liittyvät muut luokitusmuuttujat) että vuonna 1997 käyttöön otetun TK:n uuden koulutusluokituksen 6-numeroiset koulutuskoodit (ja niihin liittyvät muut luokitusmuuttujat). Myös 1997 muuttuneesta Unescon ISCED-luokituksesta tiedostossa on sekä uuden että vanhan luokituksen tiedot.

TIETOLÄHTEET:

Vuoden 1997 perusasteen jälkeisessä koulutuksessa opiskelleiden tiedot on muodostettu seuraavasti:

Tiedot päivälukioiden ja ammatillisten oppilaitosten sekä väliaikaisten ammattikorkeakoulujen opiskelijoista perustuvat pääteltyihin tietoihin. Tiedot ammatillisten oppilaitosten ja väliaikaisten ammattikorkeakoulujen opiskelijoiden osalta perustuvat vuonna 1995 Tilastokeskuksen oppilaitoksilta keräämiin henkilöpohjaisiin tietoihin. Näihin on lisätty vuosina 1996 ja 1997 yhteishauissa ja yhteishakujen ulkopuolella aloittaneet sekä poistettu vuosina 1995, 1996 ja 1997 tutkinnon suorittaneet. Ammattikorkeakoulujen yhteishakujen ulkopuolella aloittaneiden tietoja ei ole kerätty. Päivälukioiden opiskelijoita koskevat tiedot perustuvat vuoden 1995 opetushallinnon valtionosuusjärjestelmän henkilöpohjaisiin tietoihin, joihin on lisätty vuosina 1996 ja 1997 yhteishauissa ja yhteishakujen ulkopuolella aloittaneet sekä poistettu vuosina 1996 ja 1997 ylioppilastutkinnon suorittaneet.	
	
Tiedot vakinaisten ammattikorkeakoulujen sekä yliopistojen opiskelijoista perustuvat Tilastokeskuksen vuonna 1997 keräämiin henkilöpohjaisiin tietoihin. Vakinaisten ammattikorkeakoulujen opiskelijat ovat 20.9.1997 tilanteen mukaisia, yliopisto-opiskelijat 31.12.1997 tilanteen mukaisia. Väestötiedot ovat Tilastokeskuksen väestötiedostoista.


KARKEISTETUT MUUTTUJATIEDOT:

Valmisaineistomoduulista myönnetään lähtökohtaisesti karkeistettu versio EDUC_OPISK_K, jossa on karkeistettu tiedot kansalaisuudesta luokkiin suomi, muu Eurooppa ja muu, ja äidinkielestä luokkiin suomi, ruotsi ja muu.
  
Tästä valmisaineistomoduulista on mahdollista kuitenkin hakea karkeistamatonta versiota. Tämä löytyy lupapalvelusta nimellä EDUC_OPISK, ja maksaa saman verran. EDUC_OPISK sisältää muuten samat muuttujat, mutta kansalaisuus- ja äidinkielitiedot ovat karkeistamattomat. Tietojen käyttöön saaminen edellyttää erityistä tarvettä tutkimuksellisesta syystä sekä vahvoja perusteita.


Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@stat.fi

## Variables (55)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `KOTY` | Nuorten/aikuisten koulutus | — | — | — |
| `OKUNTA` | Opiskelukunta | — | kunta_1_1997_01_01 | — |
| `ALVV` | Tutkinnon aloittamisvuosi | — | — | — |
| `SP` | Sukupuoli | — | — | — |
| `OPRYH` | Oppilaitosryhmä | — | — | — |
| `KIELI2` | Äidinkieli | — | kieli_13_1996_01_01 | — |
| `IKA` | Ikä vuosina | — | — | — |
| `KIELI` | Äidinkieli | — | kieli_13_1996_01_01 | — |
| `TILV` | Aineistovuosi | — | — | — |
| `ASKUNTA` | Asuinkunta | — | kunta_1_1997_01_01 | — |
| `KANSA` | Kansalaisuus | — | valtio_11_1970_01_01 | — |
| `KOULKX` | Tilastokeskuksen koulutuskoodi | — | koulutus_1_1996_01_01 | — |
| `APUKX` | Koulutuskoodin apukoodit | — | koulutus_1_1996_01_01 | — |
| `KLOHKOX` | Opetushallinnon koulutusala | — | — | — |
| `OPALAX` | Opetushallinnon opintoala | — | — | — |
| `OPASTEX` | Opetushallinnon opintoaste | — | — | — |
| `ISCX` | Unescon koulutusaste ja -ala | — | — | — |
| `KLOHKO` | Opetushallinnon koulutusala | — | — | — |
| `OPALA` | Opetushallinnon opintoala | — | — | — |
| `OPASTE` | Opetushallinnon koulutusaste | — | — | — |
| `ATKLE` | Unescon koulutusaste | — | isced_aste_1_1997_01_01 | — |
| `ATKFI` | Unescon koulutusala | — | isced_ala_1_1997_01_01 | — |
| `ATKDE` | Unescon sijoittumistavoiteluokitus | — | isced_6_1997_01_01 | — |
| `ATKOR` | Unescon suuntautumisluokitus | — | isced_3_1997_01_01 | — |
| `ATKST` | Unescon kansallinen tutkintorakenne | — | isced_4_1997_01_01 | — |
| `ATKDU` | Unescon koulutuksen suunniteltu kesto | — | isced_5_1997_01_01 | — |
| `TYYPPI` | Oppilaitostyyppi | — | oppilaittostyyp_1_1996_01_01 | — |
| `OMISTAJA` | Oppilaitoksen omistaja | — | — | — |
| `OPKIELI` | Oppilaitoksen opetuskieli | — | — | — |
| `SIJKUNTA` | Oppilaitoksen sijaintikunta | — | kunta_1_1997_01_01 | — |
| `ASLAANI` | Asuinlääni | — | — | — |
| `ASTEKESK` | Asuinkunnan TE-keskus | — | tyov_elink_kesk_1_1997_09_01 | — |
| `ASMAAK` | Asuinmaakunta | — | maakunta_1_1997_01_01 | — |
| `ASSUURAL` | Asuinkunnan suuralue | — | — | — |
| `ASKUNRYH` | Asuinkunnan kuntaryhmitys | — | — | — |
| `ASSEUTU` | Asuinkunnan seutukunta | — | seutukunta_1_1997_09_01 | — |
| `OLAANI` | Opiskelulääni | — | — | — |
| `OTEKESK` | Opiskelukunnan työvoima-  ja elinkeinokeskus | — | tyov_elink_kesk_1_1997_09_01 | — |
| `OMAAK` | Opiskelumaakunta | — | maakunta_1_1997_09_01 | — |
| `OSUURAL` | Opiskelukunnan suuralue | — | — | — |
| `OKUNRYH` | Opiskelukunnan kuntaryhmitys | — | — | — |
| `OSEUTU` | Opiskelukunnan seutukunta | — | seutukunta_1_1997_09_01 | — |
| `SIJLAANI` | Oppilaitoksen sijaintilääni | — | — | — |
| `SIJTEKES` | Oppilaitoksen työvoima-  ja elinkeinokeskus | — | tyov_elink_kesk_1_1997_09_01 | — |
| `SIJMAAK` | Oppilaitoksen sijaintimaakunta | — | maakunta_1_1997_09_01 | — |
| `SIJSUURA` | Oppilaitoksen suuraluekoodi | — | — | — |
| `SIJKUNRY` | Oppilaitoksen sijaintikunnan  kuntaryhmitys | — | — | — |
| `SIJSEUTU` | Oppilaitoksen sijaintiseutukunta | — | seutukunta_1_1997_09_01 | — |
| `KOULK` | Tilastokeskuksen koulutuskoodi | — | koulutus_1_1997_01_01 | — |
| `LASNAS` | Kirjoilla 20.9. | — | — | — |
| `LASNAK` | Kirjoilla 20.1. | — | — | — |
| `ALLK` | Tutkinnon aloittamislukukausi | — | — | — |
| `OPRIOR` | Opiskelun prioriteetti | — | — | — |
| `shnro` | Tilastokeskuksen suojattu henkilönumero | — | — | — |
| `s_oltunn` | Tilastokeskuksen suojattu oppilaitostunnus | — | — | — |

### Variable definitions

#### `KOTY` — Nuorten/aikuisten koulutus

1=nuorten koulutus
, 2=aikuisten koulutus

#### `OKUNTA` — Opiskelukunta

**Classification:** kunta_1_1997_01_01

Opiskelukunta 1997. 
VRK:n kuntakoodi

#### `ALVV` — Tutkinnon aloittamisvuosi

Päivälukioiden, ammatillisten oppilaitosten ja 
väliaikaisten ammattikorkeakoulujen opiskelijoilla
 0000 tarkoittaa vuotta 1995 tai aiemmin.
Vakinaisten ammattikorkeakoulujen opiskelijoilla
tieto on ko. tutkinnon aloittamisvuosi 
ko. ammattikorkeakoulussa.
Yliopisto-opiskelijoilla tieto on kirjoihintulovuosi 
ko. yliopistoon.

#### `SP` — Sukupuoli

1=mies, 2=nainen

#### `OPRYH` — Oppilaitosryhmä

21=Päivälukiot
, 31=Ammatilliset oppilaitokset, 
41=Ammattikorkeakoulut, vakinaiset, 
42=Ammattikorkeakoulut, väliaikaiset, 
51=Yliopistot

#### `KIELI2` — Äidinkieli

**Classification:** kieli_13_1996_01_01

Väestötilastojen kieliluokitus. Karkeistettu tasolle suomi=1, ruotsi=2, muu=3.

#### `IKA` — Ikä vuosina

Ikä vuosina 31.12.1997

#### `KIELI` — Äidinkieli

**Classification:** kieli_13_1996_01_01

Väestötilastojen kieliluokitus. Karkeistettu tasolle suomi=1, ruotsi=2, muu=3.

#### `TILV` — Aineistovuosi

Vuoden 1997 syksyn opiskelijat

#### `ASKUNTA` — Asuinkunta

**Classification:** kunta_1_1997_01_01

Opiskelijan asuinkunta 31.12.1997
. VRK:n kuntakoodi

#### `KANSA` — Kansalaisuus

**Classification:** valtio_11_1970_01_01

Väestötilastojen maaluokitus. 
Koodin 1. merkki maanosa. Karkeistettu tasolle suomi=1, muu Eurooppa=2, muu=3.

#### `KOULKX` — Tilastokeskuksen koulutuskoodi

**Classification:** koulutus_1_1996_01_01

Tilastokeskuksen koulutuskoodi 31.12.1997, vanha

#### `APUKX` — Koulutuskoodin apukoodit

**Classification:** koulutus_1_1996_01_01

Tarvitaan, jos käytetään karkeampaa luokitusta. Vanha luokitus.

#### `KLOHKOX` — Opetushallinnon koulutusala

31.12.1997, käännetty vanhan TK:n
koulutuskoodin kautta
. 0 = Yleissivistävä koulutus
, 1 = Luonnonvara-ala, 
2 = Tekniikka ja liikenne
, 3 = Hallinto ja kauppa, 
4 = Matkailu-, ravitsemis- ja talousala
, 5 = Sosiaali- ja terveysala, 
6 = Kulttuuriala, 
7 = Humanistinen ja opetusala, 
8 = Suojeluala, 
9 = Muu koulutus

#### `OPALAX` — Opetushallinnon opintoala

31.12.1997, käännetty vanhan TK:n 
koulutuskoodin kautta

#### `OPASTEX` — Opetushallinnon opintoaste

31.12.1997, käännetty vanhan TK:n 
koulutuskoodin kautta. 
0 = Aste eriytymättä, 
1 = Kouluaste; toinen aste, 
2 = Opistoaste, 
3 = Ammatillinen korkea-aste, 
4 = Ammattikorkeakoulututkinto, 
5 = Alempi korkeakoulututkinto, 
6 = Ylempi korkeakoulututkinto, 
7 = Lisensiaattitutkinto, 
8 = Tohtorin tutkinto, 9 = Muu tai tuntematon opintoaste

#### `ISCX` — Unescon koulutusaste ja -ala

Käännetty vanhan TK:n koulutuskoodin kautta
. 1. merkki level (aste), 2.-3. merkki field (ala)
Vanha luokitus

#### `KLOHKO` — Opetushallinnon koulutusala

1998 
käännetty uuden TK:n koulutuskoodin kautta. 
0 = Yleissivistävä koulutus, 
1 = Luonnonvara-ala
, 2 = Tekniikan ja liikenteen ala, 
3 = Kaupan ja hallinnon ala, 
4 = Matkailu-, ravitsemis- ja talousala, 
5 = Sosiaali- ja terveysala, 
6 = Kulttuuriala, 
7 = Humanistinen ja opetusala
, 9 = Muu koulutus

#### `OPALA` — Opetushallinnon opintoala

1998 
käännetty uuden TK:n koulutuskoodin kautta

#### `OPASTE` — Opetushallinnon koulutusaste

1998 
käännetty uuden TK:n koulutuskoodin kautta. 
0 = Aste eriytymättä, 
1 = Toinen aste, 
2 = Opistoaste, 
3 = Ammatillinen korkea-aste, 
4 = Ammattikorkeakoulututkinto, 
5 = Alempi korkeakoulututkinto, 
6 = Ylempi korkeakoulututkinto, 
7 = Lisensiaattitutkinto, 
8 = Tohtorin tutkinto, 
9 = Muu tai tuntematon koulutusaste

#### `ATKLE` — Unescon koulutusaste

**Classification:** isced_aste_1_1997_01_01

ISCED 1997, Level

#### `ATKFI` — Unescon koulutusala

**Classification:** isced_ala_1_1997_01_01

ISCED 1997, Field

#### `ATKDE` — Unescon sijoittumistavoiteluokitus

**Classification:** isced_6_1997_01_01

ISCED 1997, Destination

#### `ATKOR` — Unescon suuntautumisluokitus

**Classification:** isced_3_1997_01_01

ISCED 1997, Orientation

#### `ATKST` — Unescon kansallinen tutkintorakenne

**Classification:** isced_4_1997_01_01

ISCED 1997, National degree structure

#### `ATKDU` — Unescon koulutuksen suunniteltu kesto

**Classification:** isced_5_1997_01_01

ISCED 1997, Duration

#### `TYYPPI` — Oppilaitostyyppi

**Classification:** oppilaittostyyp_1_1996_01_01

TK:n oppilaitosluokitus 31.12.1997

#### `OMISTAJA` — Oppilaitoksen omistaja

TK:n oppilaitosluokitus 31.12.1997. 
1=Yksityinen, 
2=Valtio
, 3=Kunta
, 4=Kuntayhtymä
, 5=Ahvenanmaa
, 9=Muu

#### `OPKIELI` — Oppilaitoksen opetuskieli

TK:n oppilaitosluokitus 31.12.1997. 
1=Suomi
, 2=Ruotsi, 
3=Suomi/ruotsi, 
5=Saame
, 9=Muu

#### `SIJKUNTA` — Oppilaitoksen sijaintikunta

**Classification:** kunta_1_1997_01_01

TK:n oppilaitosluokitus 31.12.1997. 
VRK:n kuntakoodi

#### `ASLAANI` — Asuinlääni

31.12.1997, TK:n alueluokitus, v. 1997. 
1=Etelä-Suomen
, 2=Länsi-Suomen, 
3=Itä-Suomen, 
4=Oulun, 
5=Lapin, 
6=Ahvenanmaa

#### `ASTEKESK` — Asuinkunnan TE-keskus

**Classification:** tyov_elink_kesk_1_1997_09_01

31.12.1997, TK:n alueluokitus, v. 1997

#### `ASMAAK` — Asuinmaakunta

**Classification:** maakunta_1_1997_01_01

31.12.1997, TK:n alueluokitus, v. 1997

#### `ASSUURAL` — Asuinkunnan suuralue

31.12.1997, TK:n alueluokitus, v. 1997. 
1=Uusimaa
, 2=Etelä-Suomi, 
3=Itä-Suomi, 
4=Väli-Suomi, 
5=Pohjois-Suomi, 
6=Ahvenanmaa

#### `ASKUNRYH` — Asuinkunnan kuntaryhmitys

31.12.1997, TK:n alueluokitus, v. 1997. 
1=Kaupunkimaiset kunnat
, 2=Taajaan asutut kunnat, 
3=Maaseutumaiset kunnat

#### `ASSEUTU` — Asuinkunnan seutukunta

**Classification:** seutukunta_1_1997_09_01

31.12.1997, TK:n alueluokitus, v. 1997

#### `OLAANI` — Opiskelulääni

TK:n alueluokitus, v. 1997. 
1=Etelä-Suomen, 
2=Länsi-Suomen, 
3=Itä-Suomen, 
4=Oulun, 
5=Lapin, 
6=Ahvenanmaa

#### `OTEKESK` — Opiskelukunnan työvoima- 
ja elinkeinokeskus

**Classification:** tyov_elink_kesk_1_1997_09_01

TK:n alueluokitus, v. 1997

#### `OMAAK` — Opiskelumaakunta

**Classification:** maakunta_1_1997_09_01

TK:n alueluokitus, v. 1997

#### `OSUURAL` — Opiskelukunnan suuralue

TK:n alueluokitus, v. 1997. 
1=Uusimaa, 
2=Etelä-Suomi, 
3=Itä-Suomi, 
4=Väli-Suomi, 
5=Pohjois-Suomi, 
6=Ahvenanmaa

#### `OKUNRYH` — Opiskelukunnan kuntaryhmitys

TK:n alueluokitus, v. 1997. 
1=Kaupunkimaiset kunnat, 
2=Taajaan asutut kunnat, 
3=Maaseutumaiset kunnat

#### `OSEUTU` — Opiskelukunnan seutukunta

**Classification:** seutukunta_1_1997_09_01

TK:n alueluokitus, v. 1997

#### `SIJLAANI` — Oppilaitoksen sijaintilääni

TK:n alueluokitus, v. 1997. 
1=Etelä-Suomen, 
2=Länsi-Suomen
, 3=Itä-Suomen, 
4=Oulun, 
5=Lapin, 
6=Ahvenanmaa

#### `SIJTEKES` — Oppilaitoksen työvoima- 
ja elinkeinokeskus

**Classification:** tyov_elink_kesk_1_1997_09_01

TK:n alueluokitus, v. 1997

#### `SIJMAAK` — Oppilaitoksen sijaintimaakunta

**Classification:** maakunta_1_1997_09_01

TK:n alueluokitus, v. 1997

#### `SIJSUURA` — Oppilaitoksen suuraluekoodi

TK:n alueluokitus, v. 1997. 
1=Uusimaa
, 2=Etelä-Suomi, 
3=Itä-Suomi, 
4=Väli-Suomi
, 5=Pohjois-Suomi, 
6=Ahvenanmaa

#### `SIJKUNRY` — Oppilaitoksen sijaintikunnan 
kuntaryhmitys

TK:n alueluokitus, v. 1997. 
1=Kaupunkimaiset kunnat, 
2=Taajaan asutut kunnat, 
3=Maaseutumaiset kunnat

#### `SIJSEUTU` — Oppilaitoksen sijaintiseutukunta

**Classification:** seutukunta_1_1997_09_01

TK:n alueluokitus, v. 1997

#### `KOULK` — Tilastokeskuksen koulutuskoodi

**Classification:** koulutus_1_1997_01_01

Tilastokeskuksen koulutuskoodi 1997

#### `LASNAS` — Kirjoilla 20.9.

1=Läsnä (=opiskeli tai oli pakollisessa 
työharjoittelussa), 
2=Poissa (=opiskelija oli kirjoilla oppilaitoksessa, 
mutta ei opiskellut asepalveluksen, äitiysloman 
tai muun hyväksytyn syyn vuoksi), 
0=Ei ilmoittautumistietoa

#### `LASNAK` — Kirjoilla 20.1.

1=Läsnä (=opiskeli tai oli pakollisessa 
työharjoittelussa), 
2=Poissa (=opiskelija oli kirjoilla oppilaitoksessa, 
mutta ei opiskellut asepalveluksen, äitiysloman 
tai muun hyväksytyn syyn vuoksi), 
0=Ei ilmoittautumistietoa, 
bl=tieto puuttuu (päivälukiot, ammatill., väliaik.amk)

#### `ALLK` — Tutkinnon aloittamislukukausi

1=kevät ja kesä, 2=syksy
. Vain vakinaisten ammattikorkeakoulujen ja 
yliopistojen opiskelijoilla, muilla blanco

#### `OPRIOR` — Opiskelun prioriteetti

Viimeksi aloitettu ja TK:n koulutusasteen mukaan 
korkein tavoitetutkinto. 1=korkein, 2=muu

#### `shnro` — Tilastokeskuksen suojattu henkilönumero

#### `s_oltunn` — Tilastokeskuksen suojattu oppilaitostunnus

---

[← Back to catalogue](../../README.md)
