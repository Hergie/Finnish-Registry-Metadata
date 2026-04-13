# TRAFI Moottoriajoneuvokannan aineisto, valmismoduuli1 ajoneuvotiedot

- **Identifier:** `TRAFI_20132025_jua_ajoneuvo_001.xml`
- **DOI:** `mkan_2017-12_2017-12-08_ain_0001`
- **Temporal coverage:** 2013-01-01 - 2025-09-30
- **Published:** 2025-10-27
- **Organisation:** Liikenteen turvallisuusvirasto Trafi 
- **Variable count:** 128
- **Observation count:** —
- **Population:** Manner-Suomen ajoneuvorekisterissä olevat tieliikenteen ajoneuvot
- **Source:** Liikenteen turvallisuusviraston (Trafi) ajoneuvorekisteri (ATJ ajoneuvojen tietojärjestelmä)
- **Related:** <a href= "https://www.stat.fi/til/mkan/index.html">Moottoriajoneuvokanta</a> <a href= "https://www.trafi.fi/filebank/a/1327477425/20a2a2f466b690ed94131f93468d4c69/9021-Rekisteriseloste_Ajoneuvoliikennerekisteri.pdf">Ajoneuvoliikennerekisteri</a>

## Kuvaus / Description

TRAFI-valmisaineistot perustuvat Liikenne- ja viestintävirasto (Traficom) ajoneuvoliikennerekisteriin, joka sisältää tiedot kaikista rekisteröintivelvollisuuden alaisista tieliikenteen ajoneuvoista Manner-Suomessa vuodesta 2013 alkaen. Ajoneuvokannasta on muodostettu kaksi valmisaineistomoduulia tutkimuskäyttöön. 

Moduuli 1 sisältää ajoneuvojen perustiedot. Moduuli 2 sisältää tietoja ajoneuvon omistajasta/haltijasta.

Näihin valmisaineistoihin tulee hakea käyttölupaa Traficomilta. Aineistojen käsittely tapahtuu Tilastokeskuksen ylläpitämässä FIONA-etäkäyttöjärjestelmässä.

22.12.2022: Tietoa päivämäärämuuttujista: Ajankohtien 2021q1-2022q2 tiedostoissa olevat päivämäärämuuttujat ovat sekä date-muodossa (ISO8601-formaatti) että string-muodossa. String-muotoiset muuttujat löytyvät tiedostoista, joiden tiedostonimissä on "_2"-pääte. Ajankohdan 2022q3 ja sen jälkeiset tiedostot sisältävät ainoastaan string-muotoiset päivämäärämuuttujat. 

Lisätietoa: Traficom: tietojenluovutus(at)trafi.fi 
                 Tilastokeskus: tutkijapalvelut(at)stat.fi

## Muuttujat / Variables (128)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `avainnro` | avainnumero | — | — | — |
| `ajluok` | Ajoneuovoluokka | — | ajot_1_2017_12_07 | — |
| `ajluokt` | Ajoneuvoluokka yhdistelty | — | — | — |
| `eukilpi` | EUkilpi | — | — | — |
| `erpvm` | Ensirekisteröintipäivämäärä | — | — | — |
| `liikpoistolaji` | Liikenteestäpoiston laji | — | ajot_4_2017_12_07 | — |
| `liikpoistoalpv` | Liikenteestäpoiston alkamispäivämäärä | — | — | — |
| `kaytto` | Käyttötieto. | — | kayttotarkoitus_2_2017_11_07 | — |
| `kayttos` | Ajoneuvon käyttötieto selväkielisenä | — | — | — |
| `ajovakhal` | Ajonvakausjärjestelmä | — | — | — |
| `kaypvm` | Käyttöönottopäivämäärä | — | — | — |
| `lisavari` | Lisäväri | — | ajot_6_2017_12_07 | — |
| `ovilkm` | Ovien lukumäärä | — | — | — |
| `ovisij` | Ovien sijainti | — | — | — |
| `rakajon` | Rakennettu ajoneuvo | — | — | — |
| `tuontimaa` | tuontimaa | — | ajot_7_2017_12_07 | — |
| `thyvnro` | Tyyppihyväksyntänumero | — | — | — |
| `vari` | Väri | — | ajot_5_2017_12_07 | — |
| `tyyppi` | Tyyppikoodi | — | — | — |
| `tyyppinimi` | Tyyppinimi | — | — | — |
| `valmnimi` | Valmistajan nimi | — | — | — |
| `variantti` | Variantti | — | — | — |
| `versio` | Versio | — | — | — |
| `yksmaah` | Yksittäin maahantuotu | — | ajot_8_2017_12_07 | — |
| `yksvalm` | Yksittäin Suomessa valmistettu | — | — | — |
| `istumap` | Istumapaikkojen lukumäärä | — | — | — |
| `korityyppi` | Korityyppi | — | ajot_9_2017_12_07 | — |
| `kuormakorityyppi` | Kuormakorityyppi | — | ajot_10_2017_12_07 | — |
| `seisomap` | SeisomapaikkojenLkm | — | — | — |
| `umpikoritil` | UmpikorinTilavuus | — | — | — |
| `ajonsuursallvetopoytamassa` | AjonSuurSallVetopoytamassa | — | — | — |
| `modulinkokmassa` | ModulinKokonaismassa | — | — | — |
| `omamassa` | Omamassa | — | — | — |
| `teknsuursallkokmassa` | TeknSuurSallKokmassa | — | — | — |
| `tieliiksuursallkokmassa` | TieliikSuurSallKokmassa | — | — | — |
| `pituus` | ajonKokPituus | — | — | — |
| `korkeus` | ajonKorkeus | — | — | — |
| `leveys` | ajonLeveys | — | — | — |
| `kvoima` | Käyttövoima | — | ajot_13_2017_12_07 | — |
| `ahdin` | ahdin | — | — | — |
| `ekoinnovaatio` | ekoinnovaatio | — | — | — |
| `ekoCO2Vahentyminen` | ekoCO2Vahentyminen | — | — | — |
| `huippunopeus` | huippunopeus | — | — | — |
| `iskutil` | iskutilavuus | — | — | — |
| `pataso` | paastotaso | — | ajot_14_2017_12_07 | — |
| `polttoainejarjTyyppi` | polttoainejarjTyyppi | — | ajot_32_2018_01_04 | — |
| `sahkoenergianKulutus` | sahkoenergianKulutus | — | — | — |
| `sahkohybridi` | Sähköhybridi | — | — | — |
| `sahkohybridinluokka` | Sähköhybridinluokka | — | ajot_31_2017_12_12 | — |
| `nettoteho` | suurinNettoteho | — | — | — |
| `sylintlkm` | sylintereidenLkm | — | — | — |
| `lasisamelu` | voimakkuusLASisamelu | — | — | — |
| `CO2yhdist` | CO2yhdistetyn kulutusmäärä | — | — | — |
| `akslkm` | AkselienLkm | — | — | — |
| `kaupnimi` | KaupallinenNimi | — | — | — |
| `kilvenmalli` | KilvenMalli | — | ajot_15_2017_12_07 | — |
| `malli` | Mallimerkintä | — | — | — |
| `merkki` | Merkki | — | ajot_16_2017_12_07 | — |
| `merkkis` | MerkkiSelvakielinen | — | — | — |
| `vaihtlkm` | VaihteidenLkm | — | — | — |
| `vaihteisto` | Vaihteisto | — | ajot_17_2017_12_07 | — |
| `jarru` | VoimanvalJaTehostamistapa | — | ajot_18_2017_12_07 | — |
| `lisajarrulaite` | Lisajarrulaite | — | ajot_19_2017_12_07 | — |
| `Jarrulisatieto` | Jarrulisatieto | — | ajot_20_2017_12_07 | — |
| `vakalpv` | VakuutuksenAlkamispvm | — | — | — |
| `vakyhtios` | Vakuutusyhtiö selkokielinen | — | — | — |
| `ajryhm` | Ajoneuvoryhmnä | — | ajot_21_2017_12_07 | — |
| `aksomamassakevylh` | OmaMassaKevYlh | — | — | — |
| `pieninraidevali` | Pieninraidevali | — | — | — |
| `raidevali` | Raidevali | — | — | — |
| `akssij` | Akselinsijainti | — | — | — |
| `suurinraidevali` | Suurinraidevali | — | — | — |
| `aksteknsuursallmassa` | Aksteknsuursallmassa | — | — | — |
| `akstieliiksuursallmassa` | Akstieliiksuursallmassa | — | — | — |
| `aksvetava` | Aksvetava | — | — | — |
| `aksryhmaomamassaaksryhmaalh` | Aksryhmaomamassaaksryhmaalh | — | — | — |
| `aksryhmanro` | Aksryhmanro | — | — | — |
| `aksryhmateknsuursallmassa` | Aksryhmateknsuursallmassa | — | — | — |
| `aksryhmatieliiksuursallmassa` | Aksryhmatieliiksuursallmassa | — | — | — |
| `aksryhmatyyppi` | Aksryhmatyyppi | — | ajot_22_2017_12_07 | — |
| `avpit` | Akseliväli | — | — | — |
| `avsij` | Akselien sijainti | — | — | — |
| `katsajankoht` | Katsastusajankohta | — | — | — |
| `katslaji` | Katsastuslaji | — | ajot_23_2017_12_07 | — |
| `kokmaspvkaytossa` | AutonKokmassaPVKaytossa | — | — | — |
| `pvmassa` | Perävaunumassa | — | — | — |
| `massajarruin` | Massajarruin | — | — | — |
| `massajarruinvalmsall` | Massajarruinvalmsall | — | — | — |
| `massajarruitta` | Massajarruitta | — | — | — |
| `massajarruittavalmsall` | Massajarruittavalmsall | — | — | — |
| `yhdsuursallmassa` | Yhdsuursallmassa | — | — | — |
| `ajankohta` | Ajankohta | — | — | — |
| `eiMatkamittaria` | EiMatkamittaria | — | — | — |
| `matkamittarilukema` | Matkamittarilukema | — | — | — |
| `mittarilukemaMaileina` | MittarilukemaMaileina | — | — | — |
| `ViisinumeroinenMittari` | ViisinumeroinenMittari | — | — | — |
| `kulutuslaji` | Kulutuslaji | — | ajot_24_2017_12_07 | — |
| `kulutusmaara` | Kulutusmaara | — | — | — |
| `kytkajryhm` | Kytkajryhm | — | ajot_21_2017_12_07 | — |
| `moduuli` | Moduuli | — | — | — |
| `ysskmassa` | Ysskmassa | — | — | — |
| `pvveto` | Pvveto | — | — | — |
| `kytkentalaite` | Kytkentalaite | — | ajot_25_2017_12_07 | — |
| `lisalaite` | Lisalaite | — | ajot_26_2017_12_07 | — |
| `pamaara` | Päästömäärä | — | — | — |
| `palaji` | Päästölaji | — | ajot_27_2017_12_07 | — |
| `patyyppi` | Päästötyyppi | — | ajot_28_2017_12_07 | — |
| `ppuhdlaite` | Puhdistuslaite | — | ajot_29_2017_12_07 | — |
| `valmistaja` | Valmistajaperusajoneuvo | — | — | — |
| `hyvaksyntanro` | Hyvaksyntanro | — | — | — |
| `hyvaksyntapvm` | Hyvaksyntapvm | — | — | — |
| `tyyppiperus` | Tyyppiperusajoneuvo | — | — | — |
| `varianttiperus` | Varianttiperus | — | — | — |
| `perusajoneuvonVersio` | PerusajoneuvonVersio | — | — | — |
| `monivaiheinenTyyppihyvaksynta` | MonivaiheinenTyyppihyvaksynta | — | — | — |
| `PerusajoneuvonMassa` | PerusajoneuvonMassa | — | — | — |
| `oletuslisamassa` | Oetuslisamassa | — | — | — |
| `lisasailio` | Lisäsäiliö | — | — | — |
| `psailtil` | Polttoaineisäiliön tilavuus | — | — | — |
| `turvav` | Turvavaruste | — | ajot_30_2017_12_07 | — |
| `ohjtyyppi` | Ohjaamotyyppi | — | ajot_12_2017_12_07 | — |
| `matka` | matkailuauto | — | — | — |
| `museo` | Museoajoneuvo | — | — | — |
| `yksittaiskayttovoima` | Yksittäiskäyttövoima | — | ajot_13_2017_12_07 | — |
| `kierroksillaMeluPaikallaan` | Kierroksilla melu paikallaan | — | — | — |
| `voimakkuusmeluohiajossa` | Voimakkuus melu ohiajossa | — | — | — |
| `voimakkuusmelupaikallaan` | Voimakkuus melu paikallaan. | — | — | — |
| `aineistonajankohta` | Aineiston ajankohta | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `avainnro` — avainnumero

ajoneuvolle luotu yksilöivä pseudotunnus teknisten tietojen yhdistelyä varten

#### `ajluok` — Ajoneuovoluokka

**Luokitus / Classification:** ajot_1_2017_12_07

Ajoneuvon direktiivin mukainen ajoneuvoluokka  luokittelu.

#### `ajluokt` — Ajoneuvoluokka yhdistelty

Täydennetty ja direktiivin alaluokat yhdistävä selväkielinen ajoneuovoluokka

#### `eukilpi` — EUkilpi

Tieto EU-kilvestä.

#### `erpvm` — Ensirekisteröintipäivämäärä

Ajoneuvon ensirekisteröintipäivä Suomessa.

#### `liikpoistolaji` — Liikenteestäpoiston laji

**Luokitus / Classification:** ajot_4_2017_12_07

Ajoneuvon liikennekäytöstä poiston syy. Rajoitustiedon alalaji. Rajoituslajin täydentävä tieto

01	Tavallinen poisto
02	Käyttämättömyyspoisto
03	Viranomaispoisto
04	Vaurioituneena poisto
05	Kunnan poisto
06	Ahvenanmaalle poisto
07	Ulkomaille poisto
08	Tuhoutuneena poisto
09	Romutuspoisto
10	Itse purettu / tuhottu

#### `liikpoistoalpv` — Liikenteestäpoiston alkamispäivämäärä

Liikenteestäpoiston alkamispäivämäärä. Rajoitustiedon voimassaolon alkamisaika.

#### `kaytto` — Käyttötieto.

**Luokitus / Classification:** kayttotarkoitus_2_2017_11_07

Ajoneuvon käyttötieto (tarkoitus) liikenteessä

YH	Yhteensä
01	Yksityinen käyttö
02	Luvanvarainen
03	Kouluajoneuvo
04	Vuokraus ilman kuljettajaa
05	Myyntivarasto
06            Luvanvarainen tavaraliikenne
TT	Tuntematon

#### `kayttos` — Ajoneuvon käyttötieto selväkielisenä

Ajoneuvon käyttötieto selväkielisenä

#### `ajovakhal` — Ajonvakausjärjestelmä

Kyllä/ei tieto siitä, onko ajoneuvolla ajonvakausjärjestelmä.

#### `kaypvm` — Käyttöönottopäivämäärä

Ajoneuvon käyttöönottopäivä, jonka katsastaja tallentaa tai ajoneuvo saa ensirekisteröinnin yhteydessä uusien ajoneuvojen osalta järjestelmän toimesta.

#### `lisavari` — Lisäväri

**Luokitus / Classification:** ajot_6_2017_12_07

Ajoneuvon lisäväri.

0	Musta
1	Ruskea (beige)
2	Punainen
3	Oranssi
4	Keltainen
5	Vihreä
6	Sininen
7	Violetti
8	Harmaa
9	Valkoinen
a	Vaalea
b	Tumma
c	Metallinhohto

#### `ovilkm` — Ovien lukumäärä

Ajoneuvon ovien lukumäärä.

#### `ovisij` — Ovien sijainti

Ovien sijainti.

#### `rakajon` — Rakennettu ajoneuvo

Tieto (K/E) siitä onko ajoneuvo rakennettu.

#### `tuontimaa` — tuontimaa

**Luokitus / Classification:** ajot_7_2017_12_07

Yksittäin maahantuodun ajoneuvon tuontimaa.
Maaluokitus https://www.stat.fi/meta/luokitukset/valtio/001-2012/index.html

#### `thyvnro` — Tyyppihyväksyntänumero

Ajoneuvon tyypin yksilöivä tunniste.

#### `vari` — Väri

**Luokitus / Classification:** ajot_5_2017_12_07

Ajoneuvon väri
0	Musta
1	Ruskea (beige)
2	Punainen
3	Oranssi
4	Keltainen
5	Vihreä
6	Sininen
7	Violetti
8	Harmaa
9	Valkoinen
X	Monivär.
Y	Hopea
Z	Turkoosi

#### `tyyppi` — Tyyppikoodi

Tyyppikoodi, joka yksilöi tyypin. Koska tieto otetaan huomautuskentästä voi merkkijono sisältää muitakin merkkejä kuin tyyppikoodin. Huomautustekstin max pituus 1500 merkkiä.

#### `tyyppinimi` — Tyyppinimi

Tyypin nimi

#### `valmnimi` — Valmistajan nimi

Ajoneuvon valmistajan nimi.

#### `variantti` — Variantti

Ajoneuvon variantin yksilöivä tunniste.

#### `versio` — Versio

Ajoneuvon version yksilöivä tunniste.

#### `yksmaah` — Yksittäin maahantuotu

**Luokitus / Classification:** ajot_8_2017_12_07

Tieto siitä onko ajoneuvo yksittäin maahantuotu uutena/käytettynä.
1	Tuotu käytettynä
2	Tuotu uutena

#### `yksvalm` — Yksittäin Suomessa valmistettu

Tieto (K/E) siitä onko ajoneuvo yksittäin Suomessa valmistettu.

#### `istumap` — Istumapaikkojen lukumäärä

Istumapaikkojen lukumäärä.

#### `korityyppi` — Korityyppi

**Luokitus / Classification:** ajot_9_2017_12_07

Ajoneuvon korityyppi. Vapaasti ajoneuvorekisteriin merkittävä tieto, joten ei täysin noudata todellista korimallia kaikilla ajoneuvoilla.
CO	Nivelöity matalalattiainen yksikerroksinen (CO)
BA	Avolavakuorma-auto (BA)
BB	Umpikorinen (BB)
AA	Sedan (AA)
AB	Viistoperä (AB)
AC	Farmari (AC)
AD	Coupé (AD)
AE	Avoauto (AE)
AF	Monikäyttöajoneuvo (AF)
BC	Puoliperävaunun vetoauto (BC)
BD	Perävaunun vetoajoneuvo (BD)
CA	Yksikerroksinen (CA)
CB	Kaksikerroksinen (CB)
CC	Nivelöity yksikerroksinen (CC)
CD	Nivelöity kaksikerroksinen (CD)
CE	Matalalattiainen yksikerroksinen (CE)
CF	Matalalattiainen kaksikerroksinen (CF)
CG	Nivelöity matalalattiainen yksikerroksinen (CG)
CH	Nivelöity matalalattiainen kaksikerroksinen (CH)
CI	Yksikerroksinen (CI)
CJ	Kaksikerroksinen (CJ)
CK	Nivelöity yksikerroksinen (CK)
CL	Nivelöity kaksikerroksinen (CL)
CM	Matalalattiainen yksikerroksinen (CM)
CN	Matalalattiainen kaksikerroksinen (CN)
CP	Nivelöity matalalattiainen kaksikerroksinen (CP)
CQ	Yksikerroksinen (CQ)
CR	Kaksikerroksinen (CR)
CS	Nivelöity yksikerroksinen (CS)
CT	Nivelöity kaksikerroksinen (CT)
CU	Yksikerroksinen (CU)
CV	Matalalattiainen yksikerroksinen (CV)
CW	Yksikerroksinen (CW)
DA	Puoliperävaunu (DA)
DB	Varsinainen perävaunu (DB)
DC	Keskiakseliperävaunu (DC)
SA	Matkailuauto (SA)
SB	Panssariajoneuvo (SB)
SC	Ambulanssi (SC)
SD	Ruumisauto (SD)
SE	Matkailuperävaunu (SE)
SF	Ajoneuvonosturi (SF)
SG	Muut erikoiskäyttöön tarkoitetut ajoneuvot (SG)
SH	Pyörätuolin käyttäjälle tarkoitettu ajoneuvo (SH)
U/A	Umpi/avo
1.7	AG Tavarafarmari
2.11	CX Linja-auton alusta
3.5	BE Avopakettiauto
3.6	BX Alusta-ohjaamo
4.4	DE Nivelöimättömällä vetoaisalla varustettu perävaunu
5.9	SJ Apuvaunu
5.10	SK Erikoiskuljetusperävaunu
2.9	CI Avokattoinen yksikerroksinen ajoneuvo
3.1	BA Tavara-auto
2.10	CJ Avokattoinen kaksikerroksinen ajoneuvo
SK	Erikoiskuljetusperävaunu
SL	Erikoiskuljetusauto
SM	Monilaiteajoneuvo

#### `kuormakorityyppi` — Kuormakorityyppi

**Luokitus / Classification:** ajot_10_2017_12_07

Kuormakorin tyyppi
01	Kappaletavaralava
02	Maansiirtolava
03	Kappaletavaral+irtokate
04	Puutavarapankot
05	Umpikori+säiliö
06	Umpikori eristetty
07	Umpikori eristämätön
08	Painesäiliö
09	Vak-säiliö
10	Muu säiliö
11	Konttivaruste
12	Jätepuristinkori
13	Ajoneuvon kulj.telineet
14	Muu korirakenne
15	Vaihtokorilaitteet
16	Tukikaaret ja telttakatos
17	Telttakatos (ee)
18	Lämmitettävä lava (ee)

#### `seisomap` — SeisomapaikkojenLkm

Seisomapaikkojen lukumäärä.

#### `umpikoritil` — UmpikorinTilavuus

Ajoneuvon umpikorin tilavuus kuutiometreinä (m3). Arvossa on max 1 desimaali..

#### `ajonsuursallvetopoytamassa` — AjonSuurSallVetopoytamassa

Ajoneuvon suurin sallittu vetopöytämassa kilogrammoina.

#### `modulinkokmassa` — ModulinKokonaismassa

Modulin kokonaismassa kilogrammoina.

#### `omamassa` — Omamassa

Ajoneuvon mitattu koko omamassa kilogrammoina.

#### `teknsuursallkokmassa` — TeknSuurSallKokmassa

Teknisesti suurin sallittu kokonaismassa kilogrammoina (valmistajan sallima).

#### `tieliiksuursallkokmassa` — TieliikSuurSallKokmassa

Tieliikenteessä suurin sallittu kokonaismassa kiloina.

#### `pituus` — ajonKokPituus

Ajoneuvon kokonaispituus millimetreinä.

#### `korkeus` — ajonKorkeus

Ajoneuvon korkeus millimetreinä.

#### `leveys` — ajonLeveys

Ajoneuvon leveys millimetreinä.

#### `kvoima` — Käyttövoima

**Luokitus / Classification:** ajot_13_2017_12_07

Ajoneuvon käyttövoima.
10	Biodiesel
11	LPG
13	CNG
31	Moottoripetroli
54	Vety/Sähkö
32	Diesel/Puu
33	Bensiini/Puu
34	Bensiini + moottoripetroli
37	Etanoli
38	Bensiini/CNG
39	Bensiini/Sähkö
40	Bensiini/Etanoli
41	Bensiini/Metanoli
42	Bensiini/LPG
43	Diesel/CNG
44	Diesel/Sähkö
9	Ks. huom.
01	Bensiini
02	Dieselöljy
03	Polttoöljy
04	Sähkö
05	Vety
06	Kaasu
07	Metanoli
57	L-ryhmän maakaasu
58	HL-ryhmän maakaasu
59	CNG/Biometaani
60	Biometaani
61	Puu
62	Etanoli (ED95)
63	Etanoli (E85)
64	Vety-maakaasuseos
65	LNG
66	LNG20
67	Diesel/LNG
68	Diesel/LNG20
45	Diesel/Etanoli
46	Diesel/Metanoli
47	Diesel/LPG
48	Diesel/Biodiesel
49	Diesel/Biodiesel/Sähkö
50	Diesel/Biodiesel/Etanoli
51	Diesel/Biodiesel/Metanoli
52	Diesel/Biodiesel/LPG
53	Diesel/Biodiesel/CNG
55	Dieselöljy/Muu
56	H-ryhmän maakaasu
X	Ei sovellettavissa
Y	Muu

#### `ahdin` — ahdin

Kyllä/ei  tieto ahtimen olemassaolosta.

#### `ekoinnovaatio` — ekoinnovaatio

Ekoinnovaatio kyllä/ei . Tieto vuodesta 2014 ->

#### `ekoCO2Vahentyminen` — ekoCO2Vahentyminen

Ekoinnovaation avulla saavutettu hiilidioksidipäästöjen vähentyminen yhteensä g/km. Tieto vuodesta 2014 ->

#### `huippunopeus` — huippunopeus

Ajoneuvon huippunopeus kilmetriä tunnissa (km/h).

#### `iskutil` — iskutilavuus

Moottorin iskutilavuus kuutiosenttimetreinä (cm3).

#### `pataso` — paastotaso

**Luokitus / Classification:** ajot_14_2017_12_07

Päästöjen hyväksyntätaso, joka kertoo sen säädöstason, jolla tämän version ajoneuvon päästötasot on hyväksytty.
Päästöluokka luokitus

#### `polttoainejarjTyyppi` — polttoainejarjTyyppi

**Luokitus / Classification:** ajot_32_2018_01_04

Ajoneuvon polttoainejärjestelmän tyyppi (Yhdellä tai kahdella polttoaineella toimiva tai polttoainevaatimuksiltaan joustava). Tieto vuodesta 2014 ->
 Luokitus Trafilta KdTyytiPolttoainejarjTyyppi
01	Mono fuel
02	Bi fuel
03	Flex fuel

#### `sahkoenergianKulutus` — sahkoenergianKulutus

Sahkoenergian kulutus. Tieto vuodesta 2014 ->

#### `sahkohybridi` — Sähköhybridi

Tieto (K/E) siitä, onko ajoneuvo sähkökäyttöinen hybridi. Tieto vuodesta 2014 ->

#### `sahkohybridinluokka` — Sähköhybridinluokka

**Luokitus / Classification:** ajot_31_2017_12_12

Tieto onko ajoneuvo verkosta ladattava (01) vai pelkästään polttomoottorilla ladattava (02). Tieto vuodesta 2014 ->

#### `nettoteho` — suurinNettoteho

Moottorin suurin nettoteho kilowatteina (kW). Arvossa on max 1 desimaali.

#### `sylintlkm` — sylintereidenLkm

Sylintereiden lukumäärä.

#### `lasisamelu` — voimakkuusLASisamelu

Meluarvo.

#### `CO2yhdist` — CO2yhdistetyn kulutusmäärä

yhdistetyn kulutuksen CO2-arvo g/km

#### `akslkm` — AkselienLkm

Ajoneuvon akselien lukumäärä.

#### `kaupnimi` — KaupallinenNimi

Valmistajan ilmoittama kaupallinen nimi

#### `kilvenmalli` — KilvenMalli

**Luokitus / Classification:** ajot_15_2017_12_07

Ajoneuvon rekisterikilven malli.
01	Matala
02	Korkea
03	Valinnainen

#### `malli` — Mallimerkintä

Ajoneuvon mallimerkintä. Tieto kootaan tyyppirekisterin tiedoista kaupallinen nimi + mallin lisätiedot.

#### `merkki` — Merkki

**Luokitus / Classification:** ajot_16_2017_12_07

Ajoneuvon merkki.

#### `merkkis` — MerkkiSelvakielinen

Ajoneuvon merkki selväkielisenä.

#### `vaihtlkm` — VaihteidenLkm

Eteenpäin vievien vaihteiden lukumäärä.

#### `vaihteisto` — Vaihteisto

**Luokitus / Classification:** ajot_17_2017_12_07

Vaihteiston tyyppi.
1	Käsivalintainen
2	Automaattinen
3	Portaaton
4	Käsivalintainen/automaattinen
5	Variaattori
6	Muuttuvavälityksinen
7	Jalkavalintainen
X	Ei sovellettavissa
Y	Muu

#### `jarru` — VoimanvalJaTehostamistapa

**Luokitus / Classification:** ajot_18_2017_12_07

Ajoneuvon jarrujen voimanvälitys  ja tehostamistapa.
01	Mekaanisesti käytett.jarrut
02	Nestetoimiset jarrut
03	Mekaan./neste jarrut
04	Neste/mekaan. jarrut
05	Nestetoim. alipaineteh.j
06	Nestetoim. ylipaineteh.j
07	Paineilmajarrut
08	Työntöjarrut
09	Painenestejarrut
10	Neste+painenestejarrut
11	Sähköohjatut paineilmajarrut
12	Sähköohjatut nestetoimiset alipainetehostetut jarrut
13	Paineilmakäytt.nestejarru
14	Nestetoiminen työntöjarru
15	Sähkötoiminen työntöjarru
16	Sähköjarrut
17	Elektronisesti ohjattu nestejarru

#### `lisajarrulaite` — Lisajarrulaite

**Luokitus / Classification:** ajot_19_2017_12_07

Lisäjarrulaite.

1	Hidastin
2	Sähkömagneettinen jarru
3	Moottorijarru
4	Pakokaasujarru
5	Voimansiirtojarru
Y	Muu

#### `Jarrulisatieto` — Jarrulisatieto

**Luokitus / Classification:** ajot_20_2017_12_07

Voimanvälitys ja tehostamistavan lisätieto (esim. lukkiutumattomat jarrut).
1	Lukkiutumisen estojärjestelmä (ABS)
2	Kuormantunteva jarruvoiman säätö (ALB)
3	ABS + ALB
4	Elektronisesti ohjattu jarrujärjestelmä (EBS)
5	Elektronisesti ohjattu jarrujärjestelmä (EBS)

#### `vakalpv` — VakuutuksenAlkamispvm

Vakuutuksen alkamispäivä

#### `vakyhtios` — Vakuutusyhtiö selkokielinen

Tieto vakuutusyhtiöstä. Selkokielinen nimi.

#### `ajryhm` — Ajoneuvoryhmnä

**Luokitus / Classification:** ajot_21_2017_12_07

Ajoneuvoluokan alaluokitus. Voi olla yksi tai useampi eri ajoneuvoryhmä-tieto per ajoneuvo.

#### `aksomamassakevylh` — OmaMassaKevYlh

Akselin omamassa kevennettävät ylhäällä kilogrammoina.

#### `pieninraidevali` — Pieninraidevali

Akselin pienin raideväli mm:nä

#### `raidevali` — Raidevali

Akselin raideväli mm:nä

#### `akssij` — Akselinsijainti

Akselien sijainti laskien ajoneuvon etupäästä lähtien.

#### `suurinraidevali` — Suurinraidevali

Akselin suurin raideväli mm:nä

#### `aksteknsuursallmassa` — Aksteknsuursallmassa

Valmistajan akselille/telille sallima suurin massa kilogrammoina.

#### `akstieliiksuursallmassa` — Akstieliiksuursallmassa

Suurin tieliikenteessä sallittu akselimassa.

#### `aksvetava` — Aksvetava

Vetävien akselien sijainti (true/false)

#### `aksryhmaomamassaaksryhmaalh` — Aksryhmaomamassaaksryhmaalh

Akseliryhmän omamassa akseliryhmä alhaalla kilogrammoina.

#### `aksryhmanro` — Aksryhmanro

Akseliryhmän numero, akseliryhmän sijainti edestäpäin lukien.

#### `aksryhmateknsuursallmassa` — Aksryhmateknsuursallmassa

Valmistajan akselille/telille sallima suurin massa kilogrammoina.

#### `aksryhmatieliiksuursallmassa` — Aksryhmatieliiksuursallmassa

Akseliryhmän tieliikenteessä suurin sallittu massa kilogrammoina.

#### `aksryhmatyyppi` — Aksryhmatyyppi

**Luokitus / Classification:** ajot_22_2017_12_07

Akseliryhmän tyyppi johon akseli kuuluu.
1	Yksiakselinen
2	Kaksoisakselisto
3	Kolmoisakselisto
4	Teliakselisto (2 -akselinen)
5	Teliakselisto (3 -akselinen)
Y	Muu

#### `avpit` — Akseliväli

Akselivälin pituus millimetreinä.

#### `avsij` — Akselien sijainti

Akselin sijainti laskien ajoneuvon etupäästä.

#### `katsajankoht` — Katsastusajankohta

Päivämäärä ja kellonaika, jolloin katsastussuorite on suoritettu loppuun tai keskeytetty.

#### `katslaji` — Katsastuslaji

**Luokitus / Classification:** ajot_23_2017_12_07

Katsastuslaji.
1.5.1	Rekisteröintikatsastus
1.5.10	Kytkentäkatsastus
1.5.11	Teknisten tietojen korjaus
1.5.12	Ennakkoilmoitus
1.5.13	Valvontakatsastus
1.5.14	Tienvarsitarkastus, kevyt
1.5.15	Mitätöinti
1.5.18	Yksittäishyväksyntä
1.5.19	Yksittäishyväksynnän korjaus
1.5.2	Muutoskatsastus
1.5.3	Määräaikaiskatsastus
1.5.4	Liikenteeseenottokatsastus
1.5.5	VAK/ADR -katsastus
1.5.6	Vientikatsastus
1.5.7	Kiinnitystarkastus
1.5.8	Yksittäisen ajoneuvon hyväksyntä
1.5.9	Tienvarsitarkastus, raskas
9.5.1	Rajoitustietojen ylläpito

#### `kokmaspvkaytossa` — AutonKokmassaPVKaytossa

Ajoneuvon kokonaismassa kiloina (kevyenkytkentä).

#### `pvmassa` — Perävaunumassa

Perävaunumassa kiloina.

#### `massajarruin` — Massajarruin

Perävaunun kytkentämassa jarruin.

#### `massajarruinvalmsall` — Massajarruinvalmsall

Valmistajan sallima perävaunumassa jarruin.

#### `massajarruitta` — Massajarruitta

Perävaunun kytkentämassa jarruitta.

#### `massajarruittavalmsall` — Massajarruittavalmsall

Valmistajan sallima perävaunumassa jarruitta.

#### `yhdsuursallmassa` — Yhdsuursallmassa

Yhdistelmän suurin sallittu massa kiloina (kevyenkytkentä).

#### `ajankohta` — Ajankohta

Ajankohta jolloin matkamittari on luettu

#### `eiMatkamittaria` — EiMatkamittaria

Tieto jos ajoneuvosta puuttuu matkamittari. Usein merkitty ei-matkamittaria, jos kyseessä on uusintakatsastus eikä mittarilukemaa tallenneta uudestaan.

#### `matkamittarilukema` — Matkamittarilukema

Ajoneuvon todettu matkamittarilukema jos se on kilometreina

#### `mittarilukemaMaileina` — MittarilukemaMaileina

Ajoneuvon todettu matkamittarilukema, jos se on maileina.

#### `ViisinumeroinenMittari` — ViisinumeroinenMittari

Tieto onko ajoneuvossa viisi numeroinen matkamittari.

#### `kulutuslaji` — Kulutuslaji

**Luokitus / Classification:** ajot_24_2017_12_07

Kulutuslaji. Kulutuslaji kertoo mihin kulutustietoon kulutusmäärä-tieto liittyy.
1	Kulutus maantieajossa
2	Kulutus kaupunkiajossa
3	Yhdistetty kulutus
4	CO2 Yhdistetty
5	CO2 Kaupunki
6	CO2 Maantie
7	CO2 Painotettu, yhdistetty
8	Kulutus Painotettu, yhdistetty

#### `kulutusmaara` — Kulutusmaara

Kulutuksen määrä sataa kilometriä kohden. Kulutuslajiin liittyvä kulutus-tieto. Arvossa on max 1 desimaali.

#### `kytkajryhm` — Kytkajryhm

**Luokitus / Classification:** ajot_21_2017_12_07

Kytkennän ajoneuvoryhma.

#### `moduuli` — Moduuli

Moduuli

#### `ysskmassa` — Ysskmassa

Yhdistelmän suurin sallittu kokonaismassa kilogrammoina.

#### `pvveto` — Pvveto

Kyllä/ei  tieto siitä soveltuuko vetokytkin kiinteäaisaisen perävaunun vetoon.

#### `kytkentalaite` — Kytkentalaite

**Luokitus / Classification:** ajot_25_2017_12_07

Kytkentälaitteen laji.

1	Vetokytkin
2	Vetopöytä
3	Vetokoukku
4	SA-vetokoukku
5	Vetoaisa
6	Vetopalkki
7	Vetotappi
8	KAP-vetokytkin
9	Vetopää

#### `lisalaite` — Lisalaite

**Luokitus / Classification:** ajot_26_2017_12_07

Lisalaitteen laji.
01	Nosturi
02	Kippi
03	Takalaitanostin
04	Sivulaitanostin
05	Vaihtokorilaitteet
06	Lämmityslaite
07	Jäähdytyslaite
08	Vinssi
09	Kitkavetolaite
10	Konttilukot
11	Invanostin
12	Kolmikaatokippi
13	Aurausvarustus
14	Aurauspuskuri
15	Lumiaura
16	Sohjonkeräyslevy
17	Hiekoituslaite
18	Maalauslaite
19	Harjakone
20	Jalkalavalaite
21	Aggregaatti
22	Kompressori
23	Tukijalat
24	Ajosillat
25	SA-vetokoukku
Z	Muu, mikä...

#### `pamaara` — Päästömäärä

Käytönaikaisen pakokaasupäästön määrä päästölajin mukaisina yksikköinä. Arvossa on max 5 desimaalia.
Päästölajiin liittyvä päästömäärä. Päästötyyppi huomioitava myös

#### `palaji` — Päästölaji

**Luokitus / Classification:** ajot_27_2017_12_07

Päästölaji, johon päästömäärä-tieto liittyy.
01	CO
02	CO<sub>2</sub>
03	NO<sub>x</sub>
04	Savutus [m<sup>-1</sup>]
05	Lambda-arvo
06	HC/THC
07	NMHC
09	CH<sub>4</sub>
10	Hiukkaset
11	HC/THC+NO<sub>x</sub>
12	Hiukkasten lkm * 10<sup>11</sup>
13	ELR-testin savutus [m<sup>-1</sup>]
14	CO [g/min]
15	HC [g/min]
16	NH3 [ppm]
17	CO [til%]

#### `patyyppi` — Päästötyyppi

**Luokitus / Classification:** ajot_28_2017_12_07

Käytönaikaisen pakokaasupäästön tyyppi.
01	Joutokäynti [%]
02	Korotettu joutokäynti [%]
03	[g/km]
04	ETC [g/kWh]
05	ESC [g/kWh]
06	[mg/km]
07	WHSC [mg/kWh]
08	WHTC [mg/kWh]

#### `ppuhdlaite` — Puhdistuslaite

**Luokitus / Classification:** ajot_29_2017_12_07

Pakokaasun puhdistuslaite.
01	Kolmitoimikatalysaattori
02	OBD-järjestelmä
03	Katalysaattori
04	Happitunnistin
05	Ilman suihkutus tai ilmapumppu
06	Pakokaasun takaisinkierrätys
07	Haihtumispäästöjen valvontajärjestelmä
08	Hiukkasloukku
09	Vähäpäästöinen
10	Urearuiskutus
11	Vääntömomentin rajoitin
Z	Muu, mikä...

#### `valmistaja` — Valmistajaperusajoneuvo

Perusajoneuvon valmistaja (vaihevalmistus).

#### `hyvaksyntanro` — Hyvaksyntanro

Hyväksyntänumero (vaihevalmistus, perusajoneuvo)

#### `hyvaksyntapvm` — Hyvaksyntapvm

Hyväksynnän päivämäärä (perusajoneuvo, vaihevalmistus)

#### `tyyppiperus` — Tyyppiperusajoneuvo

Perusajoneuvon tyyppi.

#### `varianttiperus` — Varianttiperus

Perusajoneuvon variantti (vaihevalmistus).

#### `perusajoneuvonVersio` — PerusajoneuvonVersio

Perusajoneuvon versio (vaihevalmistus).

#### `monivaiheinenTyyppihyvaksynta` — MonivaiheinenTyyppihyvaksynta

Monivaiheinen tyyppihyväksyntä kyllä/ei

#### `PerusajoneuvonMassa` — PerusajoneuvonMassa

Perusajoneuvon massa

#### `oletuslisamassa` — Oetuslisamassa

Oletuslisämassa

#### `lisasailio` — Lisäsäiliö

Kyllä/Ei  tieto siitä onko kyseessä lisäpolttoainesäiliö.

#### `psailtil` — Polttoaineisäiliön tilavuus

Ajoneuvon polttoainesäiliön tilavuus litroina. Arvossa on max 1 desimaali ajoneuvoluokilla L1 2, muilla 0 desimaalia.

#### `turvav` — Turvavaruste

**Luokitus / Classification:** ajot_30_2017_12_07

Turvavarusteen laji
an	Aktiivinen niskatuki
et	Etuturvatyyny
st	Sivuturvatyyny
vk	Turvavyön kiristin

#### `ohjtyyppi` — Ohjaamotyyppi

**Luokitus / Classification:** ajot_12_2017_12_07

Ajoneuvon ohjaamotyyppi.
1	Umpiohjaamo
2	Suojakehys
3	Jatko-ohjaamo
4	Avo-ohjaamo

#### `matka` — matkailuauto

Ajoneuvoryhmätieto 29 eli matkailuauto

#### `museo` — Museoajoneuvo

Ajoneuvoryhmätieto 21 eli rekisteröity museoajoneuvoksi

#### `yksittaiskayttovoima` — Yksittäiskäyttövoima

**Luokitus / Classification:** ajot_13_2017_12_07

Ajoneuvolla voi olla useampi eri käyttövoima, joihin kulutus- ja päästötiedot liittyvät.
10	Biodiesel
11	LPG
13	CNG
31	Moottoripetroli
54	Vety/Sähkö
32	Diesel/Puu
33	Bensiini/Puu
34	Bensiini + moottoripetroli
37	Etanoli
38	Bensiini/CNG
39	Bensiini/Sähkö
40	Bensiini/Etanoli
41	Bensiini/Metanoli
42	Bensiini/LPG
43	Diesel/CNG
44	Diesel/Sähkö
9	Ks. huom.
01	Bensiini
02	Dieselöljy
03	Polttoöljy
04	Sähkö
05	Vety
06	Kaasu
07	Metanoli
57	L-ryhmän maakaasu
58	HL-ryhmän maakaasu
59	CNG/Biometaani
60	Biometaani
61	Puu
62	Etanoli (ED95)
63	Etanoli (E85)
64	Vety-maakaasuseos
65	LNG
66	LNG20
67	Diesel/LNG
68	Diesel/LNG20
45	Diesel/Etanoli
46	Diesel/Metanoli
47	Diesel/LPG
48	Diesel/Biodiesel
49	Diesel/Biodiesel/Sähkö
50	Diesel/Biodiesel/Etanoli
51	Diesel/Biodiesel/Metanoli
52	Diesel/Biodiesel/LPG
53	Diesel/Biodiesel/CNG
55	Dieselöljy/Muu
56	H-ryhmän maakaasu
X	Ei sovellettavissa
Y	Muu

#### `kierroksillaMeluPaikallaan` — Kierroksilla melu paikallaan

Melumittauksen kierrosluku per minuutti.

#### `voimakkuusmeluohiajossa` — Voimakkuus melu ohiajossa

Meluarvo. Voimakkuus melu ohiajossa

#### `voimakkuusmelupaikallaan` — Voimakkuus melu paikallaan.

Meluarvo. Voimakkuus melu paikallaan.

#### `aineistonajankohta` — Aineiston ajankohta

Poikkileikkauksen ajankohdan osoittava päivämäärä

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
