# FIRM_BANKR Yrityssaneeraukset

- **Identifier:** `FIRM_1993062022_jua_BANKRsaneeraukset_001.xml`
- **DOI:** `work_2017-03_2017-03-23_ain_0002`
- **Temporal coverage:** 1993-01-01 - 2024-06-30
- **Published:** 2023-07-25
- **Organisation:** Tilastokeskus
- **Variable count:** 42
- **Observation count:** —
- **Population:** Vireille tulleet yrityssaneeraukset ja käräjäoikeuksiin saapuneet yrityssaneerausasiat.
- **Source:** Aineisto perustuu käräjäoikeuden riita- ja hakemusasioiden Tuomas -kirjaamisjärjestelmän tietoihin sekä Tilastokeskuksen yritysrekisterin tietoihin.
- **Related:** <a href= "http://www.stat.fi/til/ysan/index.html">Yrityssaneeraukset</a>

## Kuvaus / Description

Tutkimuskäyttöön on suojattu yrityssaneeraukset-tilaston perusaineisto vuosilta 1993-06/2022.

Tilasto vireille tulleista yrityssaneerauksista ja käräjäoikeuksiin saapuneista yrityssaneerausasioista julkaistaan neljännesvuosittain. Päättyneitä asioita kuvaavat tiedot julkaistaan kerran vuodessa.

Vireille pannuilla yrityssaneerauksilla tarkoitetaan kalenterivuoden aikana yrityssaneeraukseen haettuja yrityksiä ja yhteisöjä.

Samaa yritystä voidaan vuoden aikana hakea yrityssaneeraukseen useiden eri velkojien toimesta. Hakemusten määrä on aina suurempi kuin tilastoissa esitetty vireille pantujen yrityssaneerausten määrä.

Kalenterivuoden ensimmäinen yrityssaneeraushakemus tilastoidaan vireille pantuna yrityssaneerauksena. Kalenterivuonna saapuneet samaa yritystä tai yhteisöä koskevat muut hakemukset näkyvät tilastoissa ainoastaan loppuun käsitellyissä asioissa. Vuoden ensimmäinen samaa yritystä koskeva saneeraushakemus saa aineistossa muuttujan PRIT arvoksi 1 (ja myöhemmät PRIT=0), joten tarkasteluun voidaan tarvittaessa valita vain yksi havainto (hakemus) kullekin aineiston yritykselle.

Loppuun käsitellyillä yrityssaneerausasioilla tarkoitetaan Tilastokeskuksen yrityssaneeraustilastossa käräjäoikeuksissa loppuun käsiteltyjä yrityssaneerausasioita. Yrityssaneeraustilastossa tilastoidaan yrityssaneeraushakemusten lisäksi myös muut käräjäoikeuksissa käsitellyt yrityssaneerausasiat.

Loppuun käsiteltyjä yrityssaneerausasioita koskevat tilastot kuvaavat eri perusjoukkoa kuin vireille pannut yrityssaneeraukset. Loppuun käsitellyt asiat sisältävät jo tilastovuotta aiemmin vireille tulleita asioita ja vastaavasti osa tilastovuonna vireille tulleista asioista käsitellään loppuun vasta tulevina vuosina.

Vuoden 1993 helmikuussa (8.2.1993) tuli voimaan uusi laki yrityksen saneerauksesta. Lailla pyritään korjaamaan taloudellisiin vaikeuksiin joutuneiden yritysten taloudellista asemaa.

Yritysten saneerausmenettely on vaihtoehto yrityksen konkurssille. Menettely tähtää elinkelpoisen yrityksen toiminnan jatkumisen turvaamiseen. Tuomioistuimen harkinnassa on päättää, onko yrityksellä elinmahdollisuuksia saneerattuna.

Sen jälkeen kun laki yrityksen saneerauksesta tuli voimaan, velkojat eivät enää ole voineet ajaa konkurssiin elinkelpoista yritystä. Saneerausmenettely syrjäyttää konkurssin, jos saneeraukselle on tuomioistuimen arvion mukaan olemassa edellytykset.

Konkurssi voidaan torjua tekemällä saneeraushakemus ennen kuin konkurssiinasettamispäätös on tehty. Samoin, jos saneeraushakemus on tehty ja yritystä haetaan konkurssiin, on konkurssihakemuksen käsittelyä lykättävä, kunnes päätös saneerausmenettelyn aloittamisesta on tehty. Konkurssimenettely voidaan jatkossa käynnistää uudelleen, mikäli velallinen laiminlyö maksuohjelman mukaiset velanmaksut tai osoittautuu maksukyvyttömäksi.

Tilastokeskukselle toimitetaan oikeusministeriön kautta kuukausittain tiedot käräjäoikeuksissa vireille tulleista yrityssaneerausasioista ja käräjäoikeuksissa loppuun käsitellyistä yrityssaneerausasioista. Aineisto on kokonaisaineisto. Tiedot saadaan käräjäoikeuksien asiankäsittelyjärjestelmästä, josta käytetään lyhennettä Tuomas. Tuomas-järjestelmä otettiin käyttöön 1.12.1993. Tilastokeskuksessa yrityssaneeraukseen haettuun yritykseen yhdistetään sitä kuvaavat taustatiedot, kuten toimiala ja henkilökunnan määrä.

Yrityssaneerausaineistossa saneeraukseen joutumisen saa datasta poimimalla mukaan tapaukset, joilla on lopullisen päätöksen päivämäärä (lppv), asia on ’3010’ (velkajärjestelyhakemus) ja ratkaisun tyyppi on ”saneerausohjelma vahvistettu” (rkod = ’21’).

Tietojen lähteenä olevan käräjäoikeuksien Tuomas -kirjaamisjärjestelmän kirjamaisohjeet ovat lisäksi saatavilla täältä: www.finlex.fi/data/normit/31061/tuomaskirjaamisohje2007.pdf

## Muuttujat / Variables (42)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `TUIS` | Tuomioistuintunnus | — | — | — |
| `SAAPV1` | Hakemuksen saapumisvuosi | — | — | — |
| `SAAPV3` | Hakemuksen saapumiskuukausi | — | — | — |
| `SAAPV4` | Hakemuksen saapumispäivä | — | — | — |
| `ASIA` | Siviiliasiain nimikkeistön koodi | — | — | — |
| `LPPV1` | Lopullisen päätöksen vuosi | — | — | — |
| `LPPV3` | Lopullisen päätöksen kuukausi | — | — | — |
| `LPPV4` | Lopullisen päätöksen päivä | — | — | — |
| `RKOD` | Lopullisen päätöksen ratkaisukoodi | — | — | — |
| `SELITE1` | Lopullisen ratkaisukoodin selitekoodi | — | — | — |
| `SELITE2` | Lopullisen ratkaisukoodin selitekoodi | — | — | — |
| `SELITE3` | Lopullisen ratkaisukoodin selitekoodi | — | — | — |
| `VKELA` | Saneeraukseen haetun kotikunta | — | — | — |
| `HASEMA` | Saneeraukseen hakijan asema | — | — | — |
| `PKOD` | Velallisen päätoimialakoodi | — | — | — |
| `VARAT` | Saneeraukseen haetun varat | — | — | — |
| `VELAT` | Saneeraukseen haetun velat | — | — | — |
| `MAKSE` | Maksettavaksi määrätty, euroja | — | — | — |
| `KONKV` | Konkurssihakemus vireillä | — | — | — |
| `VALI` | Asiasta valitettu hovioikeuteen | — | — | — |
| `KUNMU` | Kuntamuoto | — | — | — |
| `MAAK` | Maakunta | — | — | — |
| `SUURA` | Suuralue | — | — | — |
| `KKUNTA5` | Sijaintikunta | — | — | — |
| `YRTOL02` | Toimiala 2002 | — | — | — |
| `YRTOL08` | Toimiala 2008 | — | — | — |
| `YRTOL88` | Toimiala 1988 | — | — | — |
| `LOPJM` | Lopullinen oikeudellinen muoto | — | — | — |
| `LOPKELA` | Lopullinen kuntatieto | — | — | — |
| `LOPHKPA` | Lopullinen palkatun henkilöstön lukumäärä | — | — | — |
| `LOPHKYR` | Lopullinen yrittäjien määrä | — | — | — |
| `LOPLV` | Lopullinen liikevaihto | — | — | — |
| `LOPVUOPA` | Lopullinen vuosipalkkasumma | — | — | — |
| `LOPTOL08` | Lopullinen toimiala 2008 | — | — | — |
| `ULAANI` | Kunnan uusi läänikoodi | — | — | — |
| `YRTOL95` | Toimiala 1995 | — | — | — |
| `SEUTUK` | Seutukunta | — | — | — |
| `PRIT` | Vuoden 1. saneeraushakemuksen tunniste (=1, muut=0) | — | — | — |
| `idtyyp` | Yritystunnuksen tyyppi | — | — | — |
| `syrtun` | Suojattu saneeraukseen haetun yritystunnus | — | — | — |
| `shnro` | Suojattu saneeraukseen haetun henkilönumero | — | — | — |
| `VARHAINEN_SANEERAUSMENETTELY1` | Varhainen saanerausmenettely | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `TUIS` — Tuomioistuintunnus

#### `SAAPV1` — Hakemuksen saapumisvuosi

#### `SAAPV3` — Hakemuksen saapumiskuukausi

#### `SAAPV4` — Hakemuksen saapumispäivä

#### `ASIA` — Siviiliasiain nimikkeistön koodi

3110	Saneerausmenettelyhakemus
3120	Saneerausohjelman muuttaminen (hyvin vähän havaintoja, syy ei tiedossa)
3130	Saneerausohjelman raukeaminen, yrityssaneerauslaki 65 § ja 66 §, (hyvin vähän havaintoja, syy ei tiedossa)
3140	Velkajärjestelyn raukeaminen
3190	Muu yrityssaneerausasia (hyvin vähän havaintoja, syy ei tiedossa)

#### `LPPV1` — Lopullisen päätöksen vuosi

#### `LPPV3` — Lopullisen päätöksen kuukausi

#### `LPPV4` — Lopullisen päätöksen päivä

#### `RKOD` — Lopullisen päätöksen ratkaisukoodi

Harvinaiset arvot (lähinnä 1990-luvun vuosina) saattavat olla vanhan lähdeaineiston virheellisiä kirjauksia. Suuri osa arvoista ei ole käytössä konkurssiaineistossa, vaan ainoastaan muissa samarakenteisissa aineistoissa (esim. yrityssaneerausaineisto).

01	YPT, hyväksytty (hyvin vähän havaintoja, syy ei tiedossa)
03	Hyväksytty kokonaan tai osittain
04	Hylätty
05	Tutkimatta jätetty
07	Sillensä, sovinto (hyvin vähän havaintoja, syy ei tiedossa)
08	Sillensä, muu syy
16	Hakemus rauennut / sillensä
17	Hakemus peruutettu
18	Hakemusasiassa sopimus (hyvin vähän havaintoja, syy ei tiedossa)
19	Asia siirretty
21	Saneerausohjelma vahvistettu
22	Saneerausohjelmaehdotus hylätty
23	Menettely määrätty lakkaamaan
25	Maksuohjelma vahvistettu (hyvin vähän havaintoja, syy ei tiedossa)
91	Kiireell. määrääm. hylätty (hyvin vähän havaintoja, syy ei tiedossa)
99	Erhe (hyvin vähän havaintoja, syy ei tiedossa)

#### `SELITE1` — Lopullisen ratkaisukoodin selitekoodi

Selitekoodi täydentää tapauksen ratkaisukoodia, eikä siten lähtökohtaisesti sovellu käytettäväksi sellaisenaan.

11	Konkurssi
12	Muu syy
13	Kaikkien velkojien suostumus
14	Enemmistön suostumus
15	Ei suostumusta
16	Konkurssiinasettamispäätös
17	YSL 7 §
18	Ei ohjelmaehdotusta

#### `SELITE2` — Lopullisen ratkaisukoodin selitekoodi

#### `SELITE3` — Lopullisen ratkaisukoodin selitekoodi

#### `VKELA` — Saneeraukseen haetun kotikunta

#### `HASEMA` — Saneeraukseen hakijan asema

1	Velallinen itse
2	Velkoja
3	Kuolinpesän osakas

#### `PKOD` — Velallisen päätoimialakoodi

#### `VARAT` — Saneeraukseen haetun varat

#### `VELAT` — Saneeraukseen haetun velat

#### `MAKSE` — Maksettavaksi määrätty, euroja

#### `KONKV` — Konkurssihakemus vireillä

Kertoo onko ko. hakijalla myös konkurssihakemus vireillä

#### `VALI` — Asiasta valitettu hovioikeuteen

#### `KUNMU` — Kuntamuoto

#### `MAAK` — Maakunta

#### `SUURA` — Suuralue

#### `KKUNTA5` — Sijaintikunta

#### `YRTOL02` — Toimiala 2002

#### `YRTOL08` — Toimiala 2008

#### `YRTOL88` — Toimiala 1988

#### `LOPJM` — Lopullinen oikeudellinen muoto

#### `LOPKELA` — Lopullinen kuntatieto

#### `LOPHKPA` — Lopullinen palkatun henkilöstön lukumäärä

#### `LOPHKYR` — Lopullinen yrittäjien määrä

#### `LOPLV` — Lopullinen liikevaihto

#### `LOPVUOPA` — Lopullinen vuosipalkkasumma

#### `LOPTOL08` — Lopullinen toimiala 2008

#### `ULAANI` — Kunnan uusi läänikoodi

#### `YRTOL95` — Toimiala 1995

#### `SEUTUK` — Seutukunta

#### `PRIT` — Vuoden 1. saneeraushakemuksen tunniste (=1, muut=0)

Jos PRIT=0, ei havaintoa kannattane ottaa tarkasteluun.

#### `idtyyp` — Yritystunnuksen tyyppi

1 = y-tunnus
2 = hetu-muotoinen tunnus (vuodesta 1998 alkaen vain harvoin)
3 = muu (esim. tekstiä)

#### `syrtun` — Suojattu saneeraukseen haetun yritystunnus

#### `shnro` — Suojattu saneeraukseen haetun henkilönumero

#### `VARHAINEN_SANEERAUSMENETTELY1` — Varhainen saanerausmenettely

Heinäkuusta 2022 alkaen on ollut mahdollista tehdä varhainen yrityssaneeraus. Varhaiseen yrityssaneeraukseen voidaan hakeutua jo ennen varsinaista maksukyvyttömyyttä. Kesken varhaisen yrityssaneerausmenettelyn voidaan siirtyä normaaliin yrityssaneerausmenettelyyn.

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
