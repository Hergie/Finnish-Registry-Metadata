# Yritys-toimiala-aikasarja (YA221)

- **Identifier:** `YA221_19882020_jua_yrekyritystol_001.xml`
- **DOI:** `work_2012-12_2012-12-03_ain_0002`
- **Temporal coverage:** 1988-01-01 - 2020-12-31
- **Published:** 2022-01-12
- **Organisation:** Tilastokeskus
- **Variable count:** 16
- **Observation count:** —
- **Population:** Yritykset
- **Source:** Yritysrekisterin tilastotiedostot, Yritysten rakenne- ja tilinpäätöstilasto 2013-, luokitustietokannan toimialaluokitusavaimet

## Description

Yritystol8820-tauluun on tutkimuskäyttöä varten muodostettu yritysrekisterin tilastotiedostojen yrityksille toimialaluokitusten 2002 ja 2008 mukaiset toimialat vuosille 1988 - 2020 (2013- mukana vain tilastoyksiköt, joilla yritystunnus) sekä empiirisillä että luokituskannan avaimilla. Lisäksi yrityksistä on koottu perustiedot (oikeudellinen muoto, liikevaihto ja henkilöstön lukumäärä) aikasarjaksi. Vuodesta 2013 alkaen aineistossa on mukana uusi yritys-id.

Vuodesta 1999 lähtien tol08-tieto on peräisin yritysrekisteristä, jossa se on täydennetty yrityksille takautuvasti vuosille 1999 - 2006 erilaisten päättelysääntöjen avulla. Toimialaluokitus 2002 (tai luokitus 1995) on ollut käytössä vuosina 1993 - 2008. Muulloin tarkka toimialatieto tol02 ja tol08 on tarvittaessa käännetty luokitustietokannan avaimilla, jolloin lopputulos on lähinnä suuntaa-antava. Avain kääntää kaikki tiedot 5-numerotasolla pääasialliseen luokkaan, vaikka luokka jakautuisi useaan osaan, mikä voi vääristää aineistoa. Joissakin tapauksissa toimiala on karkeammalla kuin 5-numerotasolla.

2-numerotoimialatason tol02_2 ja tol08_2 on muodostettu empiirisellä avaimella, jossa on valittu pääasiallinen luokka sen mukaan mihin karkeaan 2-numeroluokkaan 5-numerotoimialalta suurin osa yritysten henkilöstöstä siirtyy luokitusmuutosvuonna. Avain toimii suhteellisen hyvin toimialajakauman säilyttämisen näkökulmasta.

Muutoksia yritystilastojen tilastoinnissa tilastovuonna 2013

Yritysten rakenne- ja tilinpäätöstilasto ilmestyi ensimmäisen kerran 18.12.2014 yritystilastojen tietojärjestelmästä (YTY) tuotettuna. Yritysten rakenne- ja tilinpäätöstilasto on uusi tilasto, joka yhdistää Yritysrekisterin vuositilaston sekä eri tilinpäätöstilastot. Tiedot eivät ole vertailukelpoisia edeltäviin tilastoihin nähden.

Tietojärjestelmän uudistus on parantunut yritystilastojen yhtenäisyyttä. Merkittävimmät muutokset liittyvät toimialaluokituksen, yritystietojen (mm. liikevaihto- ja henkilöstötieto) ja yritysjärjestelyjen käsittelyn yhtenäistämiseen sekä päättelysääntöihin, jonka perusteella tilastoitava yritys- tai toimipaikkajoukko muodostetaan. Aiemmin yritysrekisterin vuositilastoissa ei ollut tase-ehtoa yrityksen vuositilastoon kuulumisen ratkaisemiseksi, eikä kohdejoukkoon ole kuuluneet kunnalliset liikelaitokset. Alkutuotannon toimialojen osalta tilastossa ovat tilastovuodesta 2013 alkaen mukana alkutuotannosta arvonlisäverovelvolliset, kun myynnit ylittävät tilastointirajan. Muutoksista johtuen tilastovuodesta 2013 alkaen tilastojen tiedot eivät ole vertailukelpoisia aiempiin tilastovuosiin.

## Variables (16)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `SYRTUN` | Suojattu yritystunnus | — | — | — |
| `SYRITYSID` | Suojattu yritysID | — | — | — |
| `VUOSI` | Vuosi | — | — | — |
| `tilyks` | Tilastoyksikkö | — | — | — |
| `oik` | Oikeudellinen muoto | — | — | — |
| `oik_vero` | Verohallinnon oikeudellinen muoto | — | — | — |
| `hkyr` | Henkilöstön lukumäärä | — | — | — |
| `lvyr` | Liikevaihto | — | — | — |
| `utalayr` | Tol1988 | — | — | — |
| `ntalayr` | Tol1995 | — | — | — |
| `tol02yr` | Tol2002 | — | — | — |
| `tol08yr` | Tol2008 | — | — | — |
| `TOL02` | Tol2002, luokituskannan avain | — | toimiala_1_2002_01_01 | — |
| `TOL08` | Tol2008, luokituskannan avain/yrek | — | toimiala_1_2008_01_01 | — |
| `tol02_2` | Tol2002_2, empiirinen avain | — | — | — |
| `tol08_2` | Tol2008_2, empiirinen avain | — | — | — |

### Variable definitions

#### `SYRTUN` — Suojattu yritystunnus

#### `SYRITYSID` — Suojattu yritysID

Uusi yritysyksikön tunnus, vuodesta 2013 alkaen

#### `VUOSI` — Vuosi

Vuosi

#### `tilyks` — Tilastoyksikkö

Tilastoyksikkö. 
Mahdolliset arvot ovat:
1            = tulee tilastoon
blankko = ei tule tilastoon
Tilastoon tulevat yritykset ja toimipaikat, jotka ovat toimineet yli puoli vuotta tilastovuonna ja jotka ovat työllistäneet enemmän kuin puoli henkilöä tai joiden liikevaihto on ylittänyt vuosittain määritellyn tilastorajan (10 595 euroa vuonna 2012). Vuonna 2013 alettiin soveltaa myös tase- ja investointirajoja.

Vuosina 1989-1993 ja 2006-2007 tilyks = blankko tapauksia erityisen paljon, vuonna 2013 kaikki havainnot tilastoyksiköitä.

#### `oik` — Oikeudellinen muoto

Käytössä vuoteen 2013 asti.

Oikeudellisen yksikön oikeudellinen muoto. 
Oikeudellisia muotoja ovat:
				11= Luonnollinen henkilö
				12= Kuolinpesä, perikunta
				13= Verotusyhtymä
				14= Avoin yhtiö
				15= Konkurssipesä
				21= Kommandiittiyhtiö
				22= Laivanisännistöyhtiö ( ei osakeyhtiö)
				31= Osakeyhtiö
				32= Keskinäinen vakuutusyhtiö
				33= Säästöpankki
				34= Eläkesäätiö tai –kassa, työeläkelaitos, ty
				35= Asunto-osakeyhtiö
				41= Osuuskunta
				51= Säätiö, rahasto
				52= Aatteellinen yhdistys
				53= Keskinäinen vahinkovakuutusyhdistys
				54= Taloudellinen yhdistys
				61= Julkinen viranomainen
				62= Julkinen liikelaitos
				63= Julkisoikeudellinen yhteisö
				71= Valtionkirkko
				72= Muu uskonnollinen yhteisö
				90= Muu oikeudellinen muoto

#### `oik_vero` — Verohallinnon oikeudellinen muoto

Käytössä vuodesta 2013 alkaen.

01	Luonnollinen henkilö
10	Avoin yhtiö
11	Kommandiittiyhtiö
12	Osakeyhtiö
13	Asunto-osakeyhtiö
14	Laivanisännistöyhtiö
16	Keskinäinen kiinteistö-oy
17	Muu kiinteistö-oy
18	Konserni
19	Muu yhtiö
20	Aatteellinen yhdistys
21	Erityislainsäädäntöön perustuva yhdistys
22	Keskinäinen vahinkovakuutusyhdistys
23	Metsänhoitoyhdistys
24	Osuuspankki
25	Osuuskunta
26	Vakuutuskassa
27	Työttömyyskassa
28	Muu taloudellinen yhdistys
29	Muu yhdistys
30	Säätiö (säätiölain mukainen)
31	Säästöpankki
32	Eläkesäätiö (säädekirjalla perustettu)
33	Työeläkekassa
35	Hypoteekkiyhdistys
39	Muu säätiö
40	Valtio ja sen laitokset
60	Valtion liikelaitos
41	Kunta
61	Kunnallinen liikelaitos
42	Kuntayhtymä
62	Kuntainliiton (kuntayhtymän) liikelaitos
43	Ahvenanmaan maakunta ja sen virastot
63	Ahvenanmaan liikelaitos
44	Evankelis-luterilainen kirkko
45	Ortodoksinen kirkko
46	Rekisteröity uskonnollinen yhdyskunta
47	Ylioppilaskunta tai osakunta
48	Erillishallinnollinen valtion laitos
49	Muu julkisoikeudellinen oikeushenkilö
50	Yhteisetuudet (esim. kalastuskunta)
51	Verotusyhtymät
52	Yhteisvastuullinen pidätysvelvollinen
53	Kuolinpesä
54	Konkurssipesä
55	Yhteismetsä
57	Elinkeinoyhtymä
59	Muu verotuksen yksikkö
70	Ulkomainen yhteisö
71	Ulkomaisen yhteisön sivuliike Suomessa
91	Muut
92	Muut
93	Muut
94	Muut
95	Muut
96	Muut
99	Muut
ZZ	Tieto puuttuu

#### `hkyr` — Henkilöstön lukumäärä

Oikeudellisen yksikön henkilöstö. Henkilöstö käsittää palkansaajat ja yrittäjät. Henkilöstö on muunnettu kokovuosityöllisiksi siten, että esimerkiksi puolipäiväinen työntekijä vastaa puolta henkilöä ja kaksi puolivuotista työntekijää vastaa yhtä kokovuosityöllistä.

#### `lvyr` — Liikevaihto

OIkeudellisen yksikön liikevaihto

#### `utalayr` — Tol1988

Toimialaluokitus 1988, saatavissa vuosille 1988-1993.

#### `ntalayr` — Tol1995

Toimialaluokitus 1995, saatavissa vuosille 1993-2001.

#### `tol02yr` — Tol2002

Toimialaluokitus 2002, saatavissa vuosille 2001-2008.

#### `tol08yr` — Tol2008

Toimialaluokitus 2008, saatavissa vuosille 2007-2012.

#### `TOL02` — Tol2002, luokituskannan avain

**Classification:** toimiala_1_2002_01_01

Toimialaluokitus 2002 (tai luokitus 1995) on ollut käytössä vuosina 1993-2008. Muulloin tarkka toimialatieto tol02 on tarvittaessa käännetty luokitustietokannan avaimilla, jolloin lopputulos on lähinnä suuntaa-antava. Avain kääntää kaikki tiedot 5-numerotasolla pääasialliseen luokkaan, vaikka luokka jakautuisi useaan osaan, mikä voi vääristää aineistoa. Joissakin tapauksissa toimiala on karkeammalla kuin 5-numerotasolla.

#### `TOL08` — Tol2008, luokituskannan avain/yrek

**Classification:** toimiala_1_2008_01_01

Vuodesta 1999 lähtien tol08-tieto on peräisin yritysrekisteristä, jossa se on täydennetty yrityksille takautuvasti vuosille1999-2006 erilaisten päättelysääntöjen avulla. Ennen 1999 tarkka tol08 on tarvittaessa käännetty luokitustietokannan avaimilla, jolloin lopputulos on lähinnä suuntaa-antava. Avain kääntää kaikki tiedot 5-numerotasolla pääasialliseen luokkaan, vaikka luokka jakautuisi useaan osaan, mikä voi vääristää aineistoa. Joissakin tapauksissa toimiala on karkeammalla kuin 5-numerotasolla.

#### `tol02_2` — Tol2002_2, empiirinen avain

2-numerotoimialatason tol02_2 on muodostettu empiirisellä avaimella, jossa on valittu pääasiallinen luokka sen mukaan mihin karkeaan 2-numeroluokkaan 5-numerotoimialalta suurin osa yritysten henkilöstöstä siirtyy luokitusmuutosvuonna.

#### `tol08_2` — Tol2008_2, empiirinen avain

2-numerotoimialatason tol08_2 on muodostettu empiirisellä avaimella, jossa on valittu pääasiallinen luokka sen mukaan mihin karkeaan 2-numeroluokkaan 5-numerotoimialalta suurin osa yritysten henkilöstöstä siirtyy luokitusmuutosvuonna.

---

[← Back to catalogue](../../README.md)
