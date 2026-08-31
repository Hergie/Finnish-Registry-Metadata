# FOLK_MUUTTO_VALTIO Tarkat valtiotasoiset muuttotiedot

- **Identifier:** `FOLK_19832025_jua_muutt26_001.xml`
- **DOI:** `he_201100_ain_Muutto`
- **Temporal coverage:** 1983-01-01 - 2025-12-31
- **Published:** 2026-08-27
- **Organisation:** Tilastokeskus
- **Variable count:** 14
- **Observation count:** —
- **Population:** Vuoden aikana muuttaneet, joilla vakinainen asuinpaikka Suomessa
- **Source:** DVV:n väestietojärjestelmä VTJ

## Description

FOLK_MUUTTO_VALTIO-valmisaineistomoduuli sisältää tietoja maahan- ja maastamuutoista vuodesta 1983 alkaen. Kuntien välisestä ja sisäisistä muutoista tietoja on vuodesta 1987 lähtien. Aineistokansion nimi on aiemmin ollut "FOLK_MUUTT".

<b> Valmisaineiston tarkentava nimi </b>
Tiedot Suomen maahan- ja maastamuutoista ja Suomen kuntien välillä ja sisässä muuttaneista, sisältäen muuttajan taustatiedot tarkalla tasolla 

<b> Aineiston perusjoukko, koostaminen ja tietolähteet </b>
Aineisto sisältää tietoja vuoden aikana Suomen sisällä tai Suomeen/Suomesta muuttaneista, joilla on/on ollut vakinainen asuinpaikka Suomessa. Tiedot perustuvat muuttotilaston tietoihin, jotka on koottu Digi- ja väestötietoviraston (DVV) väestötietojärjestelmästä (VTJ).  
EU- ja ETA-kansalaisten muutto Suomeen kirjautuu väestötietojärjestelmään ja tulee sitä kautta Tilastokeskukselle, kun henkilö hakee ja saa vakinaisen kotikunnan. Kolmansien maiden kansalaisten on ensin saatava oleskelulupa, ennen kun he voivat hakea kotikuntaa DVV:ltä. 
 
Maahanmuuttoajankohta on se ajankohta, jolloin oleskeluluvan saanut saa kotikunnan ja hänet merkitään VTJ:ään. Henkilö on voinut oleskella Suomessa jo pidempään ennen tätä virallista rekisteröintiä/maahanmuuttoa. VTJ:ssä henkilöllä voi olla myös tilapäinen asuinpaikka, mutta Tilastokeskuksen muuttoliiketilastossa maahanmuutoksi lasketaan vain ne tapaukset, joissa henkilö on saanut vakinaisen asuinpaikan Suomessa ja siitä on tehty merkintä VTJ:ään. 

Aineisto sisältää tarkat maa- ja kielikoodit muuttujille 1.kansalaisuus, 2. kansalaisuus, syntymävaltio, lähtömaa, tulomaa sekä äidinkieli.

<b> Aineiston päivitysaikataulu </b> 
Tutustu valmisaineistojen <a href="https://stat.fi/fi/palvelut/palvelut-tutkijoille/tutkimusaineistot/valmisaineistot/valmisaineistojen-paivitysaikataulu">  päivitysaikatauluun</a>.

<b> Aineiston käyttö ja tilaaminen </b>
Aineisto on tarkoitettu käytettäväksi FIONA-etäkäyttöjärjestelmän kautta, ja se on linkitettävissä muihin henkilövalmisaineistoihin suojatun henkilötunnisteen avulla. 

Tietoja voi tilata tutkimuksen kohdejoukolle ja tietylle ajanjaksolle. Käyttöoikeus voidaan myöntää kokonaisaineistoon (kaikki muuttujat koko populaatiolle kaikilta saatavissa olevilta vuosilta), kun sille on tutkimuksellinen tarve. Mikäli tarve koskee vain osaa muuttujista, voidaan aineistosta tilasta räätälöity versio.

Aineistosta on saatavilla myös rinnakkaisversiot FOLK_MUUTTO_MAANOSA ja FOLK_MUUTTO_SUOMI_MUU, joissa maa- ja kieliluokitukset on valmiiksi karkeistettu. FOLK_MUUTTO_VALTIO ja FOLK_MUUTTO_MAANOSA soveltuvat esimerkiksi ulkomaan ja ulkomaataustaisten muuttoliikettä tarkasteleviin tutkimuksiin, kun taas FOLK_MUUTTO_SUOMI_MUU soveltuu erityisesti Suomen sisäisen muuttoliikkeen tarkasteluun. Käyttölupa tarkemman tason versioon edellyttää vahvoja tutkimuksellisia perusteluja.

Aineisto on FIONA-etäkäyttöjärjestelmässä jaettu vuosikansioihin muuttovuoden perusteella.
 
<b> Lisätietoja </b>
Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@stat.fi.

## Variables (14)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `folk_id` | Kuuluu FOLK-aineistoon | — | — | — |
| `hid_e` | Suojattu henkilön yksilöivä tunniste. | — | — | — |
| `vuosi` | Muuttovuosi | — | — | — |
| `muuttolaji` | Muuttolaji | — | — | — |
| `muuttopv` | Muuttopäivä | — | — | — |
| `lkunta` | Lähtöasuinkunta | — | — | — |
| `tkunta` | Tuloasuinkunta | — | — | — |
| `lahtomaakoodi` | Lähtömaa | — | valtio_12_1999_05_10 | — |
| `tulomaakoodi` | Tulomaa | — | valtio_12_1999_05_10 | — |
| `kslaitmaimuu` | Kunnan sisäisen muuton laitosmaisuus | — | — | — |
| `sivs_m` | Siviilisääty muuttohetkellä | — | siviilisaaty_2_2005_01_01 | — |
| `kansa1_m` | Kansalaisuus muuttohetkellä | — | valtio_12_1999_05_10 | — |
| `svaltio_m` | Syntymävaltio (muutto) | — | valtio_12_1999_05_10 | — |
| `kansa2_m` | 2. kansalaisuus muuttohetkellä | — | — | — |

### Variable definitions

#### `folk_id` — Kuuluu FOLK-aineistoon

Henkilö kuuluu FOLK-väestöön kun folk_id=1. 

FOLK-väestöön kuuluviksi määritellään ne henkilöt, joiden tiedot löytyvät FOLK Perustieto tai FOLK Väestölaskennat 1970-1985 -kokonaisaineistosta. Eli henkilö on kuulunut vähintään yhden aikasarjan tilastovuoden viimeisenä päivänä Suomessa vakituisesti asuneeseen väestöön.

#### `hid_e` — Suojattu henkilön yksilöivä tunniste.

Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa
henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e-tunnus mahdollistaa henkilöä koskevien
tietojen yhdistämisen eri vuosien ja aineistojen välillä.

#### `vuosi` — Muuttovuosi

Tieto maasta- ja maahanmuuttaneilla vuodesta 1983 lähtien, kuntien välillä ja kuntien sisällä muuttaneilla tieto alkaen vuodesta 1987.

#### `muuttolaji` — Muuttolaji

Tietoja maahan-  ja maastamuutosta vuodesta 1983 alkaen. Kuntien välisestä ja kuntien sisäisestä muutosta tietoja on vuodesta 1987 alkaen. 

41 = maahanmuutto 
42 = maastamuutto 
43 = kuntien välinen muutto 
44 = kunnan sisäinen muutto

#### `muuttopv` — Muuttopäivä

Tieto maasta- ja maahanmuuttaneilla vuosilta vuodesta 1983 lähtien, kuntien välillä ja kuntien sisällä muuttaneilla alkaen vuodesta 1987.

#### `lkunta` — Lähtöasuinkunta

Tieto muuton lähtöasuinkunnasta suurimmalle osalle maastamuuttaneista vuosina 1983-2004 ja vuodesta 2005 eteenpäin kaikille maastamuuttaneille. Samoin suurimmalle osalle kuntien välillä ja kuntien sisällä muuttaneista tieto lähtöasuinkunnasta on vuosina 1983-2004 ja vuodesta 2005 eteenpäin kaikille. Maahanmuuttaneilla lähtöasuinkunnan arvo '200'.

#### `tkunta` — Tuloasuinkunta

Tieto muuton kohdekunnasta suurimmalle osalle maahanmuuttaneista vuosina 1983-2004 ja vuodesta 2005 eteenpäin kaikille maahanmuuttaneille. Samoin suurimmalle osalle kuntien välillä ja kuntien sisällä muuttaneista tieto tuloasuinkunnasta on vuosina 1983-2004 ja vuodesta 2005 eteenpäin kaikille. Maastamuuttaneilla tuloasuinkuntana arvo '200'.

#### `lahtomaakoodi` — Lähtömaa

**Classification:** valtio_12_1999_05_10

Tieto maahanmuuttaneilla vuodesta 1983 lähtien. Muilla paitsi maahanmuuttajilla lahtomaakoodi=246 (Suomi).

#### `tulomaakoodi` — Tulomaa

**Classification:** valtio_12_1999_05_10

Tieto maastamuuttaneilla vuodesta 1983 lähtien, arvo '200'=tuntematon. Muilla paitsi maastamuuttajilla tulomaakoodi=246 (Suomi).

#### `kslaitmaimuu` — Kunnan sisäisen muuton laitosmaisuus

Kertoo muuttaako henkilö laitokseen vai yksityisasuntokuntaan. 

Luokitus: 
0 = Ei kuulu esiintyä 
1 = Yksityisasunnosta yksityisasuntoon 
2 = Yksityisasunnosta ilman vakituista asuntoa -asumiseen 
3 = Yksityisasunnosta laitosasuntoon 
4 = Ilman vakituista asuntoa -asumisesta yksityisasuntoon 
5 = Ilman vakituista asuntoa -asumisesta ilman vakituista asuntoa -asumiseen 
6 = Ilman vakituista asuntoa -asumisesta laitosasuntoon 
7 = Laitosasunnosta yksityisasuntoon 
8 = Laitosasunnosta ilman vakituista asuntoa -asumiseen 
9 = Laitosasunnosta ilman laitosasuntoon 

Tieto kunnan sisäisissä muutoissa vuodesta 2005 ja kuntien välisissä muutoissa vuodesta 2007. Kunnan sisäisissä muutoissa luokat 5,6,8,9 eivät ole käytössä.

#### `sivs_m` — Siviilisääty muuttohetkellä

**Classification:** siviilisaaty_2_2005_01_01

Tieto maasta- ja maahanmuuttaneilla vuodesta 1983 lähtien, kuntien välillä ja kuntien sisällä muuttaneilla tieto alkaen vuodesta 1987. 

0 = tuntematon 
1 = naimaton 
2 = naimisissa 
4 = eronnut 
5 = leski 
6 = rekisteröidyssä parisuhteessa 
7 = eronnut rekisteröidystä parisuhteesta 
8 = leski rekisteröidyn parisuhteen jälkeen

#### `kansa1_m` — Kansalaisuus muuttohetkellä

**Classification:** valtio_12_1999_05_10

Tieto maasta- ja maahanmuuttaneilla vuodesta 1983 lähtien, kuntien välillä ja kuntien sisällä muuttaneilla tieto alkaen vuodesta 1987.

#### `svaltio_m` — Syntymävaltio (muutto)

**Classification:** valtio_12_1999_05_10

Tieto kunnan sisällä muuttaeilla vuodesta 2006 lähtien. Muilla tieto on alkaen vuodesta 1990.

#### `kansa2_m` — 2. kansalaisuus muuttohetkellä

Muuttavan henkilön toinen kansalaisuus muuttohetkellä mikäli se on tiedossa. Tietoja vuodesta 2006 lähtien.

---

[← Back to catalogue](../../README.md)
