# FOLK muutto

- **Identifier:** `FOLK_19832022_jua_muutt23_001.xml`
- **DOI:** `he_201100_ain_Muutto`
- **Temporal coverage:** 1983-01-01 - 2024-12-31
- **Published:** 2023-07-07
- **Organisation:** Tilastokeskus
- **Variable count:** 15
- **Observation count:** —
- **Population:** Vuoden aikana muuttaneet.
- **Source:** VTJ

## Kuvaus / Description

FOLK muutto -vuosiaineistossa on tietoja maahan- ja maastamuutoista vuodesta 1983 alkaen. Kuntien välisestä ja sisäisistä muutoista tietoja on vuodesta 1987 lähtien. Aineisto on muodostettu muuttotilaston tiedoista, jotka pohjautuvat väestötietojärjestelmän tietoihin. 

EU- ja ETA-kansalaisten muutto Suomeen tulee väestötietojärjestelmään ja sitä kautta Tilastokeskukselle, kun henkilö on hakenut ja saanut vakinaisen kotikunnan. Kolmansien maiden kansalaisten täytyy saada oleskelulupa, jotta voivat hakea kotikuntaa DVV:stä. Maahanmuuttoajankohta on se ajankohta, jolloin oleskeluluvan saanut saa kotikunnan ja hänet merkitään VTJ:ään. Henkilö on siis voinut olla maassa jo pidempään ennen virallista maahanmuuttoa. Väestötietojärjestelmässä henkilöllä voi olla myös tilapäinen asuinpaikka, mutta Tilastokeskuksen muuttoliiketilastossa henkilön siirtyminen muualta Suomeen luetaan maahanmuutoksi vain, jos väestötietojärjestelmään on tehty merkintä, että hän on saanut vakinaisen asuinpaikan Suomesta. 

Aineisto on tarkoitettu FIONA-etäpalvelun kautta käytettäväksi. Tiedot on linkitettävissä muiden henkilövalmisaineistomoduulien kanssa suojatun henkilönumeron avulla. 

Vimeisimmät FOLK muutto-aineistot ovat kansiossa FOLK_MUUTT_C, jossa tiedostot ovat jaettuna muuttovuosittain. Tiedostonimet ovat muodossa folk_muutto_"vuosi"_1. 

Vanhat FOLK muutto -aineistot ovat FIONAssa seuraavisa kansioissa: 
Totaaliaineisto vuosille 2011-2020: FOLK_muutt_11a 
Totaaliaineisto vuosille 2001-2010: FOLK_muutt_0110a 
Totaaliaineisto vuosille 1983-2000: FOLK_muutt_8300a 

Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@stat.fi.

## Muuttujat / Variables (15)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `shnro` | Suojattu henkilönumero | — | — | — |
| `folk_id` | Kuuluu FOLK-aineistoon | — | — | — |
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
| `kieli_m` | Äidinkieli (muutto) | — | kieli_15_2002_12_31 | — |
| `svaltio_m` | Syntymävaltio (muutto) | — | valtio_12_1999_05_10 | — |
| `kansa2_m` | 2. kansalaisuus muuttohetkellä | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `shnro` — Suojattu henkilönumero

Suojattu TK:n henkilönumero, joka on sama kaikissa henkilövalmisaineistoissa.

#### `folk_id` — Kuuluu FOLK-aineistoon

Henkilö kuuluu FOLK-väestöön kun folk_id=1. 

FOLK-väestöön kuuluviksi määritellään ne henkilöt, joiden tiedot löytyvät FOLK Perustieto tai FOLK Väestölaskennat 1970-1985 -kokonaisaineistosta. Eli henkilö on kuulunut vähintään yhden aikasarjan tilastovuoden viimeisenä päivänä Suomessa vakituisesti asuneeseen väestöön.

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

**Luokitus / Classification:** valtio_12_1999_05_10

Tieto maahanmuuttaneilla vuodesta 1983 lähtien. Muilla paitsi maahanmuuttajilla lahtomaakoodi=246 (Suomi).

#### `tulomaakoodi` — Tulomaa

**Luokitus / Classification:** valtio_12_1999_05_10

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

**Luokitus / Classification:** siviilisaaty_2_2005_01_01

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

**Luokitus / Classification:** valtio_12_1999_05_10

Tieto maasta- ja maahanmuuttaneilla vuodesta 1983 lähtien, kuntien välillä ja kuntien sisällä muuttaneilla tieto alkaen vuodesta 1987.

#### `kieli_m` — Äidinkieli (muutto)

**Luokitus / Classification:** kieli_15_2002_12_31

Tieto maasta- ja maahanmuuttaneilla vuodesta 1983 lähtien, kuntien välillä ja kuntien sisällä muuttaneilla tieto alkaen vuodesta 1987.

#### `svaltio_m` — Syntymävaltio (muutto)

**Luokitus / Classification:** valtio_12_1999_05_10

Tieto kunnan sisällä muuttaeilla vuodesta 2006 lähtien. Muilla tieto on alkaen vuodesta 1990.

#### `kansa2_m` — 2. kansalaisuus muuttohetkellä

Muuttavan henkilön toinen kansalaisuus muuttohetkellä mikäli se on tiedossa. Tietoja vuodesta 2006 lähtien.

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
