# FIRM_COMMOD Hyödykkeet: aineet ja tarvikkeet 2004 - 2012 (YA214)

- **Identifier:** `YA214_20042012_jua_hyodaineetjatarvikkeet_001.xml`
- **DOI:** `tti_2009-09_2009-09-15_ain_0001`
- **Temporal coverage:** 2004-01-01 - 2012-12-31
- **Published:** 2016-02-17
- **Organisation:** Tilastokeskus
- **Variable count:** 18
- **Observation count:** 156,398
- **Population:** Tiedustelun piiriin kuuluvat kaikki vähintään 20 hengen (= palkattu henkilöstö + yrittäjät) teollista toimintaa (TOL 2008: Kaivostoiminta ja louhinta = pääluokka B, Teollisuus = pääluokka C) harjoittavat yritykset.
- **Source:** Rakennetilastojen tuotantotietokanta sekä Yritys- ja toimipaikkarekisteri, oikeudellisten yksiköiden ja toimipaikkojen / toimipaikkayhdistelmien hyödyketiedusteluvastaukset, aputietoina lisäksi Tullin ulkomaankauppatiedot (vienti, tuonti) tavarakaupasta CN-nimikkeittäin, muunnettu TK:ssa koneellisesti PRODCOM-nimikkeisiin, lisäksi eri menetelmin arvioidut tiedot, joko ohjelmallisesti tai käsin arvioituina
- **Related:** <a href= "http://www.stat.fi/til/tti/index.html">Teollisuustuotanto</a> <a href= "http://www.stat.fi/meta/rekisteriselosteet/tutka_rekisteriseloste_hyodykkeet_aineet_ja_tarvikkeet.html">Hyödykkeet: aineet ja tarvikkeet</a>
- **Keywords:** hyödykkeet,jalostus,kaivostoiminta,louhinta,PRODCOM-nimikkeistö,tavarat,teollisuus,teollisuustuotanto,toimialat,tuotanto,tuotteet,valmistus

## Description

Teollisuuden Aineet ja tarvikkeet -tilasto sisältää tavaranimikkeittäisiä eli hyödykkeittäisiä arvo- ja määrätietoja ostetuista aineista ja tarvikkeista sekä joistakin nimikkeistä myös kokonaiskäytöstä kalenterivuodelta tiedonantajakohtaisesti. Tutkimuskäyttöön on suojattu tiedot vuodesta 1986 alkaen. Aineistokuvaus koskee vuosia 2004 - 2012, mutta tätä vanhemmat tiedot ovat pääosin samoja. 

Tiedot kerätään vuosittain oikeudellisilta yksiköiltä tai niiden toimipaikoilta / toimipaikkayhdistelmiltä (toimialat: kaivostoiminta ja louhinta B sekä teollisuus C eli toimialaväli 05100 - 33200). Tilaston piiriin kuuluvat myös alihankintayritykset, jotka suorittavat sopimukseen perustuvaa valmistusta toisen yrityksen tilauksesta. Tilasto koskee vain yrityksen (oikeudellisen yksikön) Suomessa tapahtunutta tuotantoa.  

Aine- ja tarviketietojen laatu ja kattavuus on huonompi kuin tuotantotietojen eikä niihin tehdä imputointeja vastaavasti.

Ostetuilla aineilla ja tarvikkeilla tarkoitetaan kalenterivuoden aikana tuotantoa varten yrityksen ulkopuolelta ostettuja aineita ja tarvikkeita eli 
- raaka-aineita,
- puolivalmisteita,
- lisäaineita ja
- tarvikkeita.
Näistä kysytään arvo- ja määrätieto. Aineiden ja tarvikkeiden kokonaiskäyttöön sisältyy kalenterivuonna tuotantoa varten yrityksen ulkopuolelta ostetut tavarat ja omassa yrityksessä jatkojalostettavaksi valmistetut tuotteet. Kokonaiskäytöstä kysytään vain määrätieto. 
  
Hyödyketilaston Aineet ja tarvikkeet -tietokokonaisuus on periaatteessa Suomen koko teollisuuden tutkimus, mutta tiedustelusta jäävät kuitenkin pois pienimmät tuottajat eli pääsääntöisesti alle 20 hengen teollisuusyritykset. Tiedonantajia pyydetään hyödyketiedonkeruun täyttöohjeissa ilmoittamaan ostot ainakin noin 80-prosenttisesti sekä kokonaiskäyttö 100-prosenttisesti niissä nimikkeissä, joissa kokonaiskäyttö kysytään. Näin saadaan tilastoitua ainakin tärkeimmät tuotannossa käytetyt aineet ja tarvikkeet kalenterivuoden aikana.
   
Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@tilastokeskus.fi.

## Variables (18)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `vuosi` | Tilastovuosi | — | — | Tunnistetiedot |
| `koodi` | Aineet ja tarvikkeet -nimikekoodi | — | aineet_tarv_1_2011_01_01 | luokitustiedot |
| `kuvaus` | Aineiden ja tarvikkeiden nimiketeksti (suomeksi), joka vastaa koodia | — | aineet_tarv_1_2011_01_01 | Ohjaustiedot |
| `panostyy` | Panostyyppikoodi | — | — | luokitustiedot |
| `yhdtyyp` | Yhdistelmätyyppi (oikeudellisen yksikön toimipaikan / toimipaikkojen) vastauksissa | — | — | Ohjaustiedot, Luokitustiedot |
| `stptunnus` | Suojattu toimipaikkatunnus | — | — | Tunnistetiedot |
| `syrtunnus` | Suojattu oikeudellisen yksikön Y-tunnus | — | — | Tunnistetiedot |
| `yrtol08` | Oikeudellisen yksikön toimiala (TOL 2008 -luokitus) | — | toimiala_1_2008_01_01 | Luokitustiedot |
| `tptol08` | Toimipaikan toimiala (TOL 2008 -luokitus) | — | toimiala_1_2008_01_01 | Luokitustiedot |
| `tvarmuus` | Aine- ja tarvikehavainnon luotettavuus (tiedon varmuus) tai käsittelyn tilanne | — | — | Ohjaustiedot |
| `estlippu` | Estimointi / imputointi, liputusmuuttuja | — | — | Ohjaustiedot |
| `arv1` | Määrätiedon arviointikoodi mittayksikössä (maara110, maara130) | — | — | Ohjaustiedot |
| `mitta1ti` | Määräyksikön mittayksikkö (maara110, maara130), hyödyketiedustelu | — | — | Luokitustiedot |
| `arvo10` | Ostojen arvo, euroa | — | — | Kokotiedot |
| `maara110` | Ostojen määrä mittayksikössä | — | — | Kokotiedot |
| `maara130` | Kokonaiskäytön määrä mittayksikössä | — | — | Kokotiedot |
| `yrtol02` | Oikeudellisen yksikön toimiala (TOL 2002 -luokitus) | — | toimiala_1_2002_01_01 | — |
| `tptol02` | Toimipaikan toimiala (TOL 2002 -luokitus) | — | toimiala_1_2002_01_01 | — |

### Variable definitions

#### `vuosi` — Tilastovuosi

**Group:** Tunnistetiedot

Tilastovuosi 4 numerolla, lyhenne tv

#### `koodi` — Aineet ja tarvikkeet -nimikekoodi

**Classification:** aineet_tarv_1_2011_01_01 · **Group:** luokitustiedot

Aineet ja tarvikkeet -nimikkeistö on laadittu Euroopan yhteisön CPA-tuoteluokituksen pohjalta soveltaen sitä kansallisten tarpeiden täyttämiseksi. Neljä ensimmäistä numeroa kuvaavat valmistavaa toimialaa (TOL 2008, Nace Rev. 2). Teollisuuden hyödyketilastossa  tilastovuodesta (tv) 2009 lähtien sovellettu CPA-luokitus on nimeltään CPA 2008. (CPA = Euroopan yhteisön tilastollinen toimialoittainen tuoteluokitus)

Aine- ja tarvikenimikkeistössä tapahtuu vähäisiä muutoksia vuodesta toiseen, mutta ei kuitenkaan joka vuosi. Tästä syystä useinkaan tarkalla nimikkeistöllä ei voida laatia vertailukelpoisia tilastoja vuosien välillä. Aggregoidummalla nimiketasolla esim. nimikkeen 4-numerotasolla (TOL 2008 -taso) tai 6-numerotasolla (CPA-taso) tilastoja voidaan tehdä vuosien välillä. 
 
Nimikemuutokset vuodesta toiseen jaotellaan 4 eri päätyyppiin. Niistä muutostyyppien 2 ja 4 muutokset (2: nimikkeen jakautumiset sekä 4: nimikkeiden ryhmittely uudella tavalla) ovat hankalimpia käsitellä, kun haluttaisiin tehdä vertailukelpoisia tilastoja uusimmalla nimikkeistöllä vuodesta tv vuoteen tv-1. 
 
Nimikemuutoksia voidaan myös ketjuttaa vuosien välillä, jolloin voidaan muodostaa esim. nimikemuutokset vuosien tv ja tv-2 välillä.

#### `kuvaus` — Aineiden ja tarvikkeiden nimiketeksti (suomeksi), joka vastaa koodia

**Classification:** aineet_tarv_1_2011_01_01 · **Group:** Ohjaustiedot

Nimiketeksti eli koodin mukainen suomenkielinen teksti, lyhennetty max 80 merkkiin. Tieto on alun perin enintään 160 merkkiä.

#### `panostyy` — Panostyyppikoodi

**Group:** luokitustiedot

Panostyyppikoodi kertoo, onko hyödykkeen panoksen (aineiden ja tarvikkeiden) osalta kysytty tiedustelussa ostot vai ostojen lisäksi kokonaiskäyttö. 
 
S = Tiedustellaan vain ostot 
T = Tiedustellaan ostojen lisäksi kokonaiskäyttö  
   
Ns. kokonaiskäytön määrä (aineissa ja tarvikkeissa) = tilastovuonna tuotantoon käytetty ostettujen raaka-aineiden määrä + samassa yrityksessä jatkojalostettavaksi valmistettujen raaka-aineiden määrä.

#### `yhdtyyp` — Yhdistelmätyyppi (oikeudellisen yksikön toimipaikan / toimipaikkojen) vastauksissa

**Group:** Ohjaustiedot, Luokitustiedot

Yhdistelmätyyppi on koodi siitä, että kyseisen ei-sivuutettavan, hyödyketiedusteluun tilastovuonna sisältyvän teollisen varsinaisen toimipaikan (= yhdistelmätoimipaikan) vastauksiin sisältyy myös sivuutettavien teollisten varsinaisten toimipaikkojen vastauksia (samalta oikeudelliselta yksiköltä). Yhdistelmätoimipaikka on kyseessä, jos toimipaikalla on yhdistelmätyyppi = Y tai K.
 
Mahdolliset koodit:

Y = monitoimipaikkkaisen teollisen yrityksen ainoa teollinen tiedustelutoimipaikka = ainoa yhdistelmätoimipaikka, johon sisältyvät saman oikeudellisen yksikön kaikki muutkin teolliset varsinaiset toimipaikat (Y-koodillisia toimipaikkoja oikeudellisella yksiköllä on vain yksi. Monitoimipaikkaisella ei-teollisella oikeudellisella yksiköllä ei koskaan käytetä Y-koodia, vaan sillä ovat mahdollisia vain X- ja K-koodit, joita esiintyy vähintään yksi kappale.)
Z = (aidosti) yksitoimipaikkainen oikeudellinen yksikkö tai minikokoinen oikeudellinen yksikkö = oikeudellisen yksikön ainoa teollinen tiedustelutoimipaikka, johon ei sisälly saman oikeudellisen yksikön muita teollisia varsinaisia toimipaikkoja, koska tällaisia ei ole olemassa (Z-koodillisia toimipaikkoja on vain yksi oikeudellista yksikköä kohden. Z-koodi on ollut käytössä tilastovuodesta 2007 lähtien. Tilastovuosina 2005-2006 kattoi Y-koodi myös Z:n osuuden yhdistelmätyypeistä.)
K = tiedustelutoimipaikka, joka sisältää muita teollisia varsinaisia toimipaikkoja = vastaukset antava teollinen toimipaikka, johon sisältyy saman oikeudellisen yksikön muitakin teollisia varsinaisia toimipaikkoja (K-koodillisia toimipaikkoja oikeudellisella yksiköllä voi olla 0 tai vähintään 1 kappaletta.)
X = ei yhdistelmätoimipaikka (aito teollinen toimipaikka, yksi- tai monitoimipaikkaisella oikeudellisella yksiköllä, myös sivuutettavalla (eli tiedustelun ulkopuolelle suljetulla) teollisella toimipaikalla esiintyy yhdistelmätyyppikoodi X)
Monitoimipaikkaisena vastaavalla oikeudellisella yksiköllä, teollisella tai ei-teollisella, voi olla vastaajatoimipaikoilla sekaisin yhdistelmätyypin koodeja X ja K. 

Jos yhdtyyp on tyhjä, nämä ovat pääsääntöisesti tapauksia, joissa kenttä estlippu = 3 eli ne eivät ole mukana ko. vuoden otoksessa vaan niillä tieto on estimoitu. Niiden yhdtyyp on haettava edellisestä vuodesta, tai joissakin tapauksissa sitä aiemmalta vuodelta.

Yhdistelmätoimipaikalla toimiala on vain ko. yksittäisen (yhdistelmä)toimipaikan oma toimiala eikä se kuvaa sitä laajempaa toimipaikkakokonaisuutta, jonka vastaukset saadaan yhdessä ko. toimipaikkaan kytkettyinä. Jos yhdistelmätyyppi = Y, kuvaa tiedonkeruun kohdetta paremmin koko oikeudellisen yksikön toimiala kuin kytköstoimipaikan oma toimiala.

Erillisessä tiedostossa tptunnus_hy_sis.sas on listattu toimipaikat, joiden tuotantotietoja sisältyy 
yhdistelmätoimipaikkojen tuotantotietoihin. Eli toimipaikka A:n tuotannoksi raportoidaan toimipaikkojen A ja B tuotannon summa, mutta toimipaikkaa B ei aineistossa mainita. ID:nä toimipaikka ja vuosi ja col-muuttujat (76) kertovat niiden "haamutoimipaikkojen" tunnukset, joiden tuotanto on sisällytetty "emotoimipaikkojen" tuotantoon. Sama tiedosto pätee ja voidaan käyttää myös tuotetietoihin.

#### `stptunnus` — Suojattu toimipaikkatunnus

**Group:** Tunnistetiedot

Suojattu toimipaikkatunnus

#### `syrtunnus` — Suojattu oikeudellisen yksikön Y-tunnus

**Group:** Tunnistetiedot

Suojattu oikeudellisen yksikön (yrityksen) tai yhteisön Y-tunnus eli yritys- ja yhteisötunnus taikka luonnollisen henkilön henkilötunnus (vain poikkeustapauksissa henkilötunnus, jos Y-tunnusta ei ole tai sitä ei löydy).

#### `yrtol08` — Oikeudellisen yksikön toimiala (TOL 2008 -luokitus)

**Classification:** toimiala_1_2008_01_01 · **Group:** Luokitustiedot

Oikeudellisen yksikön toimiala, TOL 2008 -luokitus. Saatavissa 2008 alkaen. 
 
PRODCOM-nimikekoodin ensimmäiset 4 merkkiä edustavat nimikkeen 4-numeroista toimialakoodia. Nimikettä tuottavan yrityksen / toimipaikan / toimipaikkayhdistelmän (pää)toimiala voi hyvinkin poiketa nimikkeen omasta toimialasta.

#### `tptol08` — Toimipaikan toimiala (TOL 2008 -luokitus)

**Classification:** toimiala_1_2008_01_01 · **Group:** Luokitustiedot

Toimipaikan toimiala, TOL 2008 -luokitus. Saatavissa 2008 alkaen. 
 
PRODCOM-nimikekoodin ensimmäiset 4 merkkiä edustavat nimikkeen 4-numeroista toimialakoodia. Nimikettä tuottavan yrityksen / toimipaikan / toimipaikkayhdistelmän (pää)toimiala voi hyvinkin poiketa nimikkeen omasta toimialasta.

#### `tvarmuus` — Aine- ja tarvikehavainnon luotettavuus (tiedon varmuus) tai käsittelyn tilanne

**Group:** Ohjaustiedot

Aine- ja tarvikehavainnon tiedon varmuus (TUOTANTOPANOS) tai käsittelyn tilanne. TVARMUUS on havaintokohtainen arvioinnin liputusmuuttuja.

Mahdolliset koodit: 
NULL tai tyhjä = tieto saatu normaalisti (tavanomaisin tilanne)
H = hyväksytty 
A = manuaalisesti arvioitu 
O = ohjelmallisesti arvioitu (yleensä yrityksen / toimipaikan / toimipaikkayhdistelmän koko vastaus; siis kun keruuyksikkö ei ole vastannut miltään osin); O-koodi on käytössä ilmeisesti vasta tv 2012 lähtien   
E = epävarma
M = aine- ja tarvike-määrätieto on arvioitu (tietoa käytetään kansalliseen tilastonlaadintaan)

#### `estlippu` — Estimointi / imputointi, liputusmuuttuja

**Group:** Ohjaustiedot

Aineissa ja tarvikkeissa ei ole kattava tieto, ei kannata käyttää!

#### `arv1` — Määrätiedon arviointikoodi mittayksikössä (maara110, maara130)

**Group:** Ohjaustiedot

Määrätiedon arviointikoodi mittayksikössä (maara110, maara130) eli estimoinnin liputusmuuttuja

#### `mitta1ti` — Määräyksikön mittayksikkö (maara110, maara130), hyödyketiedustelu

**Group:** Luokitustiedot

Nimikkeellä hyödyketiedustelussa käytettävä määrätietojen mittayksikkö. Aineissa ja tarvikkeissa on TK:ssa harkittu sopivaksi käyttää vain yhtä määräyksikköä kussakin nimikkeessä.
 
Mittayksiköt voivat kuvata painoa tai bruttovetoisuutta, pituutta, pinta-alaa, tilavuutta, lukumäärää (kappaletta tai paria), tehoa ja energiaa, bruttolämpöarvoa tms.

#### `arvo10` — Ostojen arvo, euroa

**Group:** Kokotiedot

Ostojen arvo yritykseen toimitettuna, euroa, kun panostyy = S. Yrityksen ulkopuolelta kalenterivuoden aikana ostettujen aineiden ja tarvikkeiden arvo ilman arvonlisäveroa (alv). Omilla autoilla tapahtuneiden kuljetusten kustannuksia ei kuitenkaan sisällytetä ostoarvoon.
 
Ostetuilla aineilla ja tarvikkeilla tarkoitetaan kalenterivuoden aikana tuotantoa varten yrityksen ulkopuolelta ostettuja aineita ja tarvikkeita eli 
- raaka-aineita,
- puolivalmisteita,
- lisäaineita ja
- tarvikkeita.

Ostojen arvoon tai määrään ei sisällytetä kauppatavaroiden ostoja, jotka on ostettu ja myyty sellaisenaan ilman omaa jatkojalostusta toisille yrityksille ja jotka eivät jää osaksi yrityksen omaa tuotetta. 
 
Kokonaiskäytöstä ei ilmoiteta arvoa, ainoastaan määrä (= MAARA130).

#### `maara110` — Ostojen määrä mittayksikössä

**Group:** Kokotiedot

Ostojen määrä yhdessä mittayksikössä eli määrä_1, kun panostyy = S, mittayksiköt vaihtelevat paljon, ks. muuttuja MITTA1TI. 
 
Hyödykenimikkeestä kysytään hyödyketiedustelussa yksi määrätieto.

#### `maara130` — Kokonaiskäytön määrä mittayksikössä

**Group:** Kokotiedot

Kokonaiskäytön määrä yhdessä mittayksikössä eli määrä_1, kun panostyy = T, mittayksiköt vaihtelevat paljon, ks. muuttuja MITTA1TI.
 
Kokonaiskäytön määrä = tilastovuonna tuotantoon käytettyjen ostettujen aineiden ja tarvikkeiden määrä + samassa yrityksessä jatkojalostettavaksi valmistettujen aineiden ja tarvikkeiden määrä + yrityksen toisilta toimipaikoilta hankittujen aineiden ja tarvikkeiden määrä.

#### `yrtol02` — Oikeudellisen yksikön toimiala (TOL 2002 -luokitus)

**Classification:** toimiala_1_2002_01_01

Oikeudellisen yksikön toimiala (TOL 2002 -luokitus). Saatavissa 2005-.

PRODCOM-nimikekoodin ensimmäiset 4 merkkiä edustavat nimikkeen 4-numeroista toimialakoodia. Nimikettä tuottavan yrityksen / toimipaikan / toimipaikkayhdistelmän (pää)toimiala voi hyvinkin poiketa nimikkeen omasta toimialasta.

#### `tptol02` — Toimipaikan toimiala (TOL 2002 -luokitus)

**Classification:** toimiala_1_2002_01_01

Toimipaikan toimiala (TOL 2002 -luokitus). 

PRODCOM-nimikekoodin ensimmäiset 4 merkkiä edustavat nimikkeen 4-numeroista toimialakoodia. Nimikettä tuottavan yrityksen / toimipaikan / toimipaikkayhdistelmän (pää)toimiala voi hyvinkin poiketa nimikkeen omasta toimialasta.

---

[← Back to catalogue](../../README.md)
