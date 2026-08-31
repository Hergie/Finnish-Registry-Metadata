# FOLK_MUUTTO_SUOMI_MUU Karkeat muuttotiedot tasolla Suomi/muu

- **Identifier:** `FOLK_19832025_jua_muuttosuomimuu26_001.xml`
- **DOI:** `he_201100_ain_Muutto`
- **Temporal coverage:** 1983-01-01 - 2025-12-31
- **Published:** 2026-08-27
- **Organisation:** Tilastokeskus
- **Variable count:** 15
- **Observation count:** —
- **Population:** Vuoden aikana muuttaneet, joilla vakinainen asuinpaikka Suomessa.
- **Source:** DVV:n väestötietojärjestelmä VTJ

## Description

FOLK_MUUTTO_SUOMI_MUU-valmisaineistomoduuli sisältää tietoja maahan- ja maastamuutoista vuodesta 1983 alkaen. Kuntien välisistä ja sisäisistä muutoista on tietoja vuodesta 1987 alkaen. 
Aineiston sisältämät tiedot ovat karkeistettuja. 

<b> Valmisaineiston tarkentava nimi </b>
Tiedot Suomen maahan- ja maastamuutoista ja Suomen kuntien välillä ja sisässä muuttaneista, sisältäen muuttajan taustatiedot karkealla tasolla (karkeat muuttotiedot tasolla Suomi/muu) (FOLK_MUUTTO_SUOMI_MUU).

<b> Aineiston perusjoukko, koostaminen ja tietolähteet </b>
Aineisto sisältää tietoja vuoden aikana Suomen sisällä tai Suomeen/Suomesta muuttaneista, joilla on/on ollut vakinainen asuinpaikka Suomessa.  Tiedot perustuvat muuttotilaston tietoihin, jotka on koottu  Digi- ja väestötietoviraston (DVV) väestötietojärjestelmästä (VTJ).

FOLK_MUUTTO_SUOMI_MUU-aineiston sisältämät tiedot on karkeistettu seuraavasti: 
Tiedot kansalaisuudesta, syntymävaltiosta sekä lähtö- ja tulomaasta: karkeistettu tasolle suomi/muu
Tieto äidinkielestä: karkeistettu tasolle suomi/ruotsi/muu

EU- ja ETA-kansalaisten muutto Suomeen tulee väestötietojärjestelmään ja sitä kautta Tilastokeskukselle, kun henkilö on hakenut ja saanut vakinaisen kotikunnan. Kolmansien maiden kansalaisten täytyy saada oleskelulupa, jotta voivat hakea kotikuntaa DVV:stä. 
Maahanmuuttoajankohta on se ajankohta, jolloin oleskeluluvan saanut saa kotikunnan ja hänet merkitään VTJ:ään. Henkilö on voinut olla maassa jo pidempään ennen virallista rekisteröintiä/maahanmuuttoa. VTJ:ssä henkilöllä voi olla myös tilapäinen asuinpaikka, mutta Tilastokeskuksen muuttoliiketilastossa maahanmuutoksi lasketaan vain ne tapaukset, joissa henkilö on saanut vakinaisen asuinpaikan Suomessa ja siitä on tehty merkintä VTJ:ään.

<b> Aineiston päivitysaikataulu </b> 
Tutustu valmisaineistojen <a href="https://stat.fi/fi/palvelut/palvelut-tutkijoille/tutkimusaineistot/valmisaineistot/valmisaineistojen-paivitysaikataulu">  päivitysaikatauluun</a>.

<b> Aineiston käyttö ja tilaaminen </b>
Aineisto on tarkoitettu käytettäväksi FIONA-etäkäyttöjärjestelmän kautta, ja se on linkitettävissä muihin henkilövalmisaineistoihin suojatun henkilötunnisteen avulla. 

Käyttöoikeus voidaan myöntää kokonaisaineistoon (kaikki muuttujat koko populaatiolle kaikilta saatavissa olevilta vuosilta), kun sille on tutkimuksellinen tarve. Mikäli tarve koskee vain osaa muuttujista, voidaan aineistosta tilasta räätälöity versio.. 
Aineistosta on saatavilla rinnakkaisversiot FOLK_MUUTTO_MAANOSA ja FOLK_MUUTTO_VALTIO. Näistä ensiksi mainittu moduuli sisältää maanosa-tasolle karkeistetut tiedot ja jälkimmäinen moduuli tarkat valtiotasoiset tiedot. FOLK_MUUTTO_SUOMI_MUU soveltuu erityisesti Suomen sisäisen muuttoliikkeen tarkasteluun.

Aineisto on jaettu FIONA-etäkäyttöjärjestelmässä vuosikansioihin muuttovuoden perusteella. 

<b> Lisätietoja </b>
Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@tilastokeskus.fi.

## Variables (15)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `folk_id` | Kuuluu FOLK-aineistoon | — | — | — |
| `hid_e` | Suojattu henkilön yksilöivä tunniste. | — | — | — |
| `vuosi` | Muuttovuosi | — | — | — |
| `muuttolaji` | Muuttolaji | — | — | — |
| `muuttopv` | Muuttopäivä | — | — | — |
| `lkunta` | Lähtöasuinkunta | — | — | — |
| `tkunta` | Tuloasuinkunta | — | — | — |
| `lahtomaakoodi_sm` | Lähtömaa (Suomi, muu) | — | — | — |
| `tulomaakoodi_sm` | Tulomaa (Suomi, muu) | — | — | — |
| `kslaitmaimuu` | Kunnan sisäisen muuton laitosmaisuus | — | — | — |
| `sivs_m` | Siviilisääty muuttohetkellä | — | — | — |
| `kansa1_sm` | Kansalaisuus muuttohetkellä (Suomi, muu) | — | — | — |
| `svaltio_sm` | Syntymävaltio (Suomi, muu) | — | — | — |
| `kansa2_sm` | 2. kansalaisuus muuttohetkellä (Suomi, muu) | — | — | — |
| `kieli_sm` | Äidinkieli karkeistettu (suomi, ruotsi, muu) | — | — | — |

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

#### `lahtomaakoodi_sm` — Lähtömaa (Suomi, muu)

Tieto maahanmuuttaneilla vuodesta 1983 lähtien. Maahanmuuttajilla lähtömaakoodi = 900 (ulkomaa) Muilla paitsi maahanmuuttajilla lahtomaakoodi=246 (Suomi).

#### `tulomaakoodi_sm` — Tulomaa (Suomi, muu)

Tieto maastamuuttaneilla vuodesta 1983 lähtien. Maahanmuuttajilla tulomaakoodi = 900. Muilla paitsi maastamuuttajilla tulomaakoodi=246 (Suomi).

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

Tieto maasta- ja maahanmuuttaneilla vuodesta 1983 lähtien, kuntien välillä ja kuntien sisällä muuttaneilla tieto alkaen vuodesta 1987. 

0 = tuntematon 
1 = naimaton 
2 = naimisissa tai rekisteröidyssä parisuhteessa 
4 = eronnut tai eronnut rekisteröidystä parisuhteesta 
5 = leski tai  leski rekisteröidyn parisuhteen jälkeen

#### `kansa1_sm` — Kansalaisuus muuttohetkellä (Suomi, muu)

Tieto maasta- ja maahanmuuttaneilla vuodesta 1983 lähtien, kuntien välillä ja kuntien sisällä muuttaneilla tieto alkaen vuodesta 1987. 

246= Suomi
900= muu

#### `svaltio_sm` — Syntymävaltio (Suomi, muu)

Tieto kunnan sisällä muuttaeilla vuodesta 2006 lähtien. Muilla tieto on alkaen vuodesta 1990. 

246= Suomi
900 = muu

#### `kansa2_sm` — 2. kansalaisuus muuttohetkellä (Suomi, muu)

Muuttavan henkilön toinen kansalaisuus muuttohetkellä mikäli se on tiedossa. Tietoja vuodesta 2006 lähtien.

246= Suomi
900= muu

#### `kieli_sm` — Äidinkieli karkeistettu (suomi, ruotsi, muu)

Tieto maasta- ja maahanmuuttaneilla vuodesta 1983 lähtien, kuntien välillä ja kuntien sisällä muuttaneilla tieto alkaen vuodesta 1987. 

1= suomi
2= ruotsi
3= muu

---

[← Back to catalogue](../../README.md)
