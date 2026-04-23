# FOLK_MUUTTO_SUOMI_MUU Karkeat muuttotiedot tasolla Suomi/muu

- **Identifier:** `FOLK_19832024_jua_muuttosuomimuu25_001.xml`
- **DOI:** `he_201100_ain_Muutto`
- **Temporal coverage:** 1983-01-01 - 2024-12-31
- **Published:** 2025-11-28
- **Organisation:** Tilastokeskus
- **Variable count:** 15
- **Observation count:** —
- **Population:** Vuoden aikana muuttaneet.
- **Source:** VTJ

## Description

FOLK karkeat muuttotiedot tasolla Suomi/muu -vuosiaineistossa on tietoja maahan- ja maastamuutoista vuodesta 1983 alkaen. Kuntien välisestä ja sisäisistä muutoista tietoja on vuodesta 1987 lähtien. Aineisto on muodostettu muuttotilaston tiedoista, jotka pohjautuvat väestötietojärjestelmän tietoihin. 

FOLK karkeat muuttotiedot tasolla suomi/muu - moduulissa on karkeistettu seuraavat muuttujat 1=suomi, 2=muu -tasolle: kansalaisuus, 2. kansalaisuus, syntymävaltio, lähtömaa ja tulomaa. Äidinkieli on karkeistettu tasolle 1=suomi, 2=ruotsi, 3=muu. 

EU- ja ETA-kansalaisten muutto Suomeen tulee väestötietojärjestelmään ja sitä kautta Tilastokeskukselle, kun henkilö on hakenut ja saanut vakinaisen kotikunnan. Kolmansien maiden kansalaisten täytyy saada oleskelulupa, jotta voivat hakea kotikuntaa DVV:stä. Maahanmuuttoajankohta on se ajankohta, jolloin oleskeluluvan saanut saa kotikunnan ja hänet merkitään VTJ:ään. Henkilö on siis voinut olla maassa jo pidempään ennen virallista maahanmuuttoa. Väestötietojärjestelmässä henkilöllä voi olla myös tilapäinen asuinpaikka, mutta Tilastokeskuksen muuttoliiketilastossa henkilön siirtyminen muualta Suomeen luetaan maahanmuutoksi vain, jos väestötietojärjestelmään on tehty merkintä, että hän on saanut vakinaisen asuinpaikan Suomesta. 

Aineisto on tarkoitettu FIONA-etäpalvelun kautta käytettäväksi. Tiedot on linkitettävissä muiden henkilövalmisaineistomoduulien kanssa suojatun henkilönumeron avulla. 

Vimeisimmät FOLK_MUUTTO_SUOMI_MUU-aineistot ovat kansiossa FOLK_MUUTTO_SUOMI_MUU, jossa tiedostot ovat jaettuna muuttovuosittain. Tiedostonimet ovat muodossa folk_muuttosm_"vuosi"_1. 

Vanhat FOLK muutto -aineistot ovat FIONAssa seuraavisa kansioissa: 
Totaaliaineisto vuosille 2011-2020: FOLK_muutt_11a 
Totaaliaineisto vuosille 2001-2010: FOLK_muutt_0110a 
Totaaliaineisto vuosille 1983-2000: FOLK_muutt_8300a 

Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@stat.fi.

## Variables (15)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `shnro` | Suojattu henkilönumero | — | — | — |
| `folk_id` | Kuuluu FOLK-aineistoon | — | — | — |
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
| `kieli_sm` | Äidinkieli karkeistettu (suomi, ruotsi, muu) | — | — | — |
| `svaltio_sm` | Syntymävaltio (Suomi, muu) | — | — | — |
| `kansa2_sm` | 2. kansalaisuus muuttohetkellä (Suomi, muu) | — | — | — |

### Variable definitions

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

#### `lahtomaakoodi_sm` — Lähtömaa (Suomi, muu)

Tieto maahanmuuttaneilla vuodesta 1983 lähtien. Maahanmuuttajilla lähtömaakoodi = 900 (ulkomaa) Muilla paitsi maahanmuuttajilla lahtomaakoodi=246 (Suomi).

#### `tulomaakoodi_sm` — Tulomaa (Suomi, muu)

Tieto maastamuuttaneilla vuodesta 1983 lähtien. Maastamuuttjailla tulomaakoodi = 900. Muilla paitsi maastamuuttajilla tulomaakoodi=246 (Suomi).

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

#### `kieli_sm` — Äidinkieli karkeistettu (suomi, ruotsi, muu)

Tieto maasta- ja maahanmuuttaneilla vuodesta 1983 lähtien, kuntien välillä ja kuntien sisällä muuttaneilla tieto alkaen vuodesta 1987. 

1= suomi
2= ruotsi
3= muu

#### `svaltio_sm` — Syntymävaltio (Suomi, muu)

Tieto kunnan sisällä muuttaeilla vuodesta 2006 lähtien. Muilla tieto on alkaen vuodesta 1990. 

246= Suomi
900 = muu

#### `kansa2_sm` — 2. kansalaisuus muuttohetkellä (Suomi, muu)

Muuttavan henkilön toinen kansalaisuus muuttohetkellä mikäli se on tiedossa. Tietoja vuodesta 2006 lähtien.

246= Suomi
900= muu

---

[← Back to catalogue](../../README.md)
