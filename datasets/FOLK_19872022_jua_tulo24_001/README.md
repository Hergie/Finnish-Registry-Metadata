# FOLK tulotieto

- **Identifier:** `FOLK_19872022_jua_tulo24_001.xml`
- **DOI:** `work_2017-08_2017-08-09_ain_0002`
- **Temporal coverage:** 1987-01-01 - 2023-12-31
- **Published:** 2026-01-20
- **Organisation:** Eläketurvakeskus
- **Variable count:** 32
- **Observation count:** —
- **Population:** Kunkin vuoden viimeisenä päivänä Suomessa vakituisesti asunut väestö
- **Source:** Väestörekisterikeskuksen väestötietojärjestelmä, Tilastokeskuksen tulonjakotilasto, Verohallinnon rekisterit, Tilastokeskuksen henkilötietovarasto, Kansaneläkelaitoksen rekisterit, THL:n toimeentulotukirekisteri

## Kuvaus / Description

FOLK-henkilöaineiston tulotietomoduulissa on tietoja henkilöiden tuotannontekijätuloista, saaduista ja maksetuista tulonsiirroista, varallisuudesta ja veloista. Aineistossa on tietoja vuodesta 1987 lähtien. Poikkeamat tietojen saatavuudessa on merkitty muuttujan kuvaukseen vuosiluvuilla.

Tulonjakotilastossa muodostetut tulomuuttujat ovat mahdollisimman tarkasti pyritty muokkaamaan vertailukelpoisiksi eri vuosille. Verottajan aineistosta otetut tiedot eivät ole täysin vertailukelpoisia yli ajan. Vertailukelpoisuutta heikentää verotukseen tehdyt muutokset, joista merkittävin on vuoden 2005 verouudistus, jonka seurauksena esim. ansiotulot ja pääomatulot valtionverotuksessa sekä tulovero ansio- tai pääomatulosta eivät ole täysin vertailukelpoisia tietoja vuosina 1995-2004 ja vuodesta 2005 eteenpäin.

Tulonjakotilaston aggregaattimuuttujien (palkkatulot, yrittäjätulot, omaisuustulot, saadut tulonsiirrot, maksetut tulonsiirrot, käytettävissä oleva rahatulo) kuvauksissa ei ole lueteltu yksittäisiä tuloeriä. Nämä muuttujat muodostuvat vuosittain päivitettävän tulonjakotilaston tulonimikkeistön pohjalta ja tietoja on saatavilla vuodesta 1995 lähtien.



Kelan aineistoihin perustuvat tiedot sisältävät myös negatiivisia arvoja. Negatiiviset etuudet voivat johtua takaisinperinnöistä tai väärinmaksatuksista. Tulonjakotilastossa negatiivisia arvoja ei ole nollattu, vaan ne on otettu huomioon käytettävissä olevien tulojen muodostuksessa sellaisenaan. 

Huomioitavaa: 

2022 päivitys: Tulonjakotilaston muodostamista muuttujista ja tulonjakotilaston aineistoista poimituista verottajan tiedoista, on siirrytty tilastovuodesta 2022 alkaen poimimaan tiedot suoraan verottajan aineistoista. Päivityksellä ei ole vaikutusta datan vertailukelpoisuuteen. 

25.1.2024: "toimtu"-muuttujan arvot 2021 vuositauluun on korjattu ja aineisto on ajantasalla.

2021 päivityksessä aineistoon lisätty tulonjakotilaston tulomuuttujat PALK (palkkatulot), YRTU (yrittäjätulot) ja OMTU (omaisuustulot).

TYOTU-muuttuja sisältää tietoja vuoteen 2018 asti. Verottajan lähtöaineistossa ja tilastossa tapahtuneiden muutosten takia kyseistä muuttujaa ei enää ylläpidetä. Vuoden 2018 jälkeiset tiedot henkilön palkkatuloista ovat saatavilla muuttujasta PALK. 

Tyotu-muuttujassa on puutteita (puuttuvia arvoja) tilastovuoden 1989 osalta.

2020 päivityksessä: ennen 31.2.2020 FOLK tulotieto -valmisaineistossa työtuloihin summautui verotiedot TOSINKP (työpanokseen perustuva osinko, palkkaa) ja TOSINKPY (yrittäjän työpanokseen perustuva osinko, palkkaa) vuosina 2010-17 sekä TELPS7 (kunnallisen perhepäivähoitajan palkka) vuosina 2005-2017 kahteen kertaan, koska nämä tiedot sisältyivät jo verotietoon TRPL. TOSINKP ja TOSINKPY -tietoja oli noin 4 000 henkilöllä ja TELPS7-tietoja 25 000 henkilöllä.

Aineisto on tarkoitettu FIONA-etäpalvelun kautta luovutettavaksi. Tiedot on linkitettävissä muiden henkilövalmisaineistomoduulien kanssa suojatun henkilönumeron avulla.

Vimeisimmät FOLK tulotietoaineistot ovat kansiossa FOLK_TULO_C, jossa tiedostot on jaettuna tilastovuosittain. Tiedostonimet ovat muodossa folk_tulo_"vuosi"_1.

Vanhat FOLK tulotieto -aineistot ovat FIONAssa seuraavissa kansioissa:
Totaaliaineisto vuosille 2011-2019: FOLK_tulo_11a
Totaaliaineisto vuosille 2001-2010: FOLK_tulo_0110a
Totaaliaineisto vuosille 1987-2000: FOLK_tulo_8800a

Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@tilastokeskus.fi.

## Muuttujat / Variables (32)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `vuosi` | Vuosi | — | — | — |
| `hid_e` | Suojattu henkilön yksilöivä tunniste | — | — | — |
| `palk` | Palkkatulot | — | — | Tulonjakotilasto, TJKT |
| `yrtu` | Yrittäjätulot | — | — | TJKT, Tulonjakotilasto |
| `omtu` | Omaisuustulot | — | — | TJKT, Tulonjakotilasto |
| `saatusi` | Saadut tulonsiirrot | — | — | Tulonjakotilasto, TJKT |
| `makstu` | Maksetut tulonsiirrot | — | — | TJKT, Tulonjakotilasto |
| `kturaha` | Käytettävissä olevat rahatulot | — | — | Tulonjakotilasto, TJKT |
| `tyotu` | Summatut työtulot (palkkatulot) | — | — | Henkilöverotusaineisto |
| `tyrtuo` | Yrittäjätulot | — | — | Henkilöverotusaineisto |
| `telinko` | Elinkeinotulot | — | — | Henkilöverotusaineisto |
| `tmaat1` | Maatalouden ansiotulot | — | — | Henkilöverotusaineisto |
| `svatv` | Tulot yhteensä valtionverotuksessa | — | — | Henkilöverotusaineisto |
| `svatva` | Ansiotulot yhteensä valtionverotuksessa | — | — | Henkilöverotusaineisto |
| `svatvp` | Pääomatulot yhteensä valtionverotuksessa | — | — | Henkilöverotusaineisto |
| `saiprva` | Sairauspäivärahat | — | — | Kela |
| `elatulo` | Eläketulot | — | — | Henkilöverotusaineisto |
| `tkotihtu` | Lapsen kotihoidon tuki ja osittainen hoitoraha | — | — | Henkilöverotusaineisto |
| `aiprva` | Vanhempainpäiväraha | — | — | Kela |
| `tyotur` | Työttömyysturvaetuudet | — | — | Henkilöverotusaineisto |
| `astuki` | Asumistuet | — | — | Kela |
| `opira` | Opintorahat | — | — | Kela |
| `toimtu` | Toimeentulotuet | — | — | Kela, THL |
| `tpar` | Sairausvakuutuksen päivärahat | — | — | Henkilöverotusaineisto |
| `ltv` | Valtion tulovero | — | — | Henkilöverotusaineisto |
| `ltva` | Valtion tuloveron osuus ansiotulojen verosta | — | — | Henkilöverotusaineisto |
| `ltvp` | Valtion tuloveron osuus pääomatulojen verosta | — | — | Henkilöverotusaineisto |
| `lkuve` | Kunnallisvero | — | — | Henkilöverotusaineisto |
| `lkive` | Kirkollisvero | — | — | Henkilöverotusaineisto |
| `lvv` | Varallisuusvero | — | — | Henkilöverotusaineisto |
| `lvar` | Verotettava varallisuus | — | — | Henkilöverotusaineisto |
| `velaty` | Velat yhteensä | — | — | Henkilöverotusaineisto |

### Muuttujien määritelmät / Variable definitions

#### `vuosi` — Vuosi

Tilastovuosi.

#### `hid_e` — Suojattu henkilön yksilöivä tunniste

Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e -tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä.

#### `palk` — Palkkatulot

**Ryhmä / Group:** Tulonjakotilasto, TJKT

Tulonjakotilaston palkkatulot-muuttuja. Sisältää rahapalkkaeriä, työsuhteeseen perustuvien kustannusten korvauksia ja luontoisedut. Muuttuja muodostuu vuosittain päivitettävän tulonjakotilaston tulonimikkeistön pohjalta. Tietoja vuodesta 1995 lähtien.

#### `yrtu` — Yrittäjätulot

**Ryhmä / Group:** TJKT, Tulonjakotilasto

Tulonjakotilaston yrittäjätulot-muuttuja. Muuttujaan on summattu maa- ja metsätilatalouden yrittäjätulot, elinkeinon harjoittajien yrittäjätulot, yhtymien yrittäjätulot ja tekijänoikeuksista, patenteista yms. tulevat yrittäjätulot. Muuttuja muodostuu vuosittain päivitettävän tulonjakotilaston tulonimikkeistön pohjalta. Tietoja vuodesta 1995 lähtien.

#### `omtu` — Omaisuustulot

**Ryhmä / Group:** TJKT, Tulonjakotilasto

Tulonjakotilaston omaisuustulot-muuttuja. Muuttujaan on summattu henkilöveroaineistosta omaisuustuloiksi tulonjakotilastossa määritetyt rekisteripohjaiset tuloerät. Sisältää osinkotulot, korkotulot, yksityisiin vakuutuksiin perustuvat eläkkeet ja korvaukset, vuokratulo osakehuoneistosta ja kiinteistöstä, veronalainen luovutusuvoitto sekä selvittämätön omaisuuden lisäys ja muut pääomatulot. Muuttuja muodostuu vuosittain päivitettävän tulonjakotilaston tulonimikkeistön pohjalta. Tietoja vuodesta 1995 lähtien.

#### `saatusi` — Saadut tulonsiirrot

**Ryhmä / Group:** Tulonjakotilasto, TJKT

Tulonjakotilaston muodostama saatujen tulonsiirtojen yhteissumma. Muuttuja muodostuu vuosittain päivitettävän tulonjakotilaston tulonimikkeistön pohjalta. Tietoja vuodesta 1995 lähtien.

#### `makstu` — Maksetut tulonsiirrot

**Ryhmä / Group:** TJKT, Tulonjakotilasto

Tulonjakotilaston muodostama maksettujen tuloverojen ja veronluonteisten maksujen yhteissumma. Muuttujaan on summattu palkka-, yrittäjä- ja omaisuustulosta sekä saaduista tulonsiirroista maksetut valtion ja kuntien verot ja veronluonteiset pakolliset maksut. Huom. kirkollisvero katsotaan vapaehtoiseksi veroksi, joten sitä ei huomioida maksetuissa tulonsiirroissa. Muuttuja muodostuu vuosittain päivitettävän tulonjakotilaston tulonimikkeistön pohjalta. Tietoja vuodesta 1995 lähtien.

#### `kturaha` — Käytettävissä olevat rahatulot

**Ryhmä / Group:** Tulonjakotilasto, TJKT

Tulonjakotilaston muodostama käytettävissä oleva rahatulo muodostuu bruttotuloista (palkkatulojen, yrittäjätulojen, omaisuustulojen ja saatujen tulonsiirtojen summa), joista on vähennetty maksetut tulonsiirrot (maksetut verot ja veronluonteiset maksut). Tulonjaon kokonaistilaston päätulokäsite. Tietoja vuodesta 1995 lähtien.

#### `tyotu` — Summatut työtulot (palkkatulot)

**Ryhmä / Group:** Henkilöverotusaineisto

Summatut työtulot (palkkatulot) sisältää seuraavia verotietoja vuoteen 2018 asti: 
TRPL = rahapalkka päätoimesta, luontaisedut ja työsuhdeoptiot 
TMPT = muut palkkatulot sivutoimesta
TEPALK = ennakonkannon alaiset palkkatulot veroilmoitukselta (vuodesta 1990 lähtien)
TMERI = veronalainen merityötulo (vuosina 2005-2007)
TMERI1 = matkustaja-alusten maksuvapauden piiriin kuuluva merityötulo (vuoteen 2007 asti) 
TKUST = kustannusten korvaukset työnantajalta
TPALV = lunastukset, palvelurahat yms. ennakonkannon alaiset tulot 
TPJTA = hankintatyön arvo metsätaloudesta 
TYHTHAV = hankintatyön arvo yhtymästä 
TPTURVA = palkkaturva ja sijaismaksajan maksama palkka ansiotulona (vuodesta 1993 lähtien)
TELPS = työkorvaus (vuodesta 1993 lähtien)
TELPS3 = urheilijarahastosta maksettava palkka (vuodesta 1999 lähtien)
TLUE2 = luontaisedut merityötulosta (vuodesta 1993 lähtien)
TLUE3 = luontaisedut merityötulosta (vuosina 2005-2007)
TUTMP2 = ulkomaisen työnantajan maksama palkka työntekijälle, joka ei Suomessa vakuutettu (vuodesta 2009 lähtien)
TUTMP3 = ulkomaisen työnantajan maksama palkka Suomessa vakuutetulle työntekijälle (vuodesta 2009 lähtien) 
TOSINKTK= työpanokseen perustuva osinko, työkorvausta (vuodesta 2010 lähtien)

Vuoden 2018 jälkeiset tiedot henkilön palkkatuloista ovat saatavilla muuttujasta PALK.

#### `tyrtuo` — Yrittäjätulot

**Ryhmä / Group:** Henkilöverotusaineisto

Yrittäjätulot sisältävät maatalouden tulot, elinkeinotoiminnan tulot ja tulot yhtymästä. Elinkeinotoiminnan tulot eivät sisällä puolison elinkeinotuloja.

Yrittäjätulot sisältävät seuraavia verotietoja:
TMAAT1 = maatalouden ansiotulo, oma
TMAAT2 = maatalouden pääomatulo, oma
TLIIK1 = elinkeinotoiminnan ansiotulo-osuus, oma
TPORO1 = ansiotulo porotaloudesta
TLIIK2 = elinkeinotoiminnan pääomatulo-osuus, oma
TPORO2 = pääomatulo porotaloudesta
TYHTAT = ansiotulot ilman osinkoja yhtymästä (vuodesta 1993 lähtien)
TEINOYVA = osingot ansiotulona muista kuin listatuista yhtiöistä, verotettava määrä yhtymistä (vuodesta 2005 lähtien)
TYHAU = ansiotulo-osuus ulkomaisen yhtymän tulosta (vuosina 1996-2011)
TYHTPOT = pääomatulot ilman osinkoja yhtymistä (vuodesta 1993 lähtien)
TEINOYVP = osingot pääomatulona muista kuin listatuista yhtiöistä, veronalainen määrä yhtymistä (vuosina 2005-2013)
TNOSYHV = osingot pääomatulona listatuista yhtiöistä, verotettava määrä yhtymistä (vuodesta 2005 lähtien)
TYHAP = pääomatulo-osuus ulkomaisen yhtymän tulosta (vuosina 1996-2017)
TOPYKOK = osuuspääoman korot yhtymistä, yhteismäärä (vuosina 2005-2014)

#### `telinko` — Elinkeinotulot

**Ryhmä / Group:** Henkilöverotusaineisto

Elinkeinotulot sisältävät elinkeinotoiminnan ansiotulot ja pääomatulot. Ne eivät sisällä puolison elinkeinotuloja. Elinkeinotulot sisältävät seuraavia verotietoja:
TLIIK1 = elinkeinotoiminnan ansiotulo-osuus, oma
TPORO1 = ansiotulo porotaloudesta
TLIIK2 = elinkeinotoiminnan pääomatulo-osuus, oma
TPORO2 = pääomatulo porotaloudesta

#### `tmaat1` — Maatalouden ansiotulot

**Ryhmä / Group:** Henkilöverotusaineisto

Maatalouden ansiotulot, ei sisällä puolison tuloja.

#### `svatv` — Tulot yhteensä valtionverotuksessa

**Ryhmä / Group:** Henkilöverotusaineisto

Valtionveronalaiset tulot = ansiotulot yhteensä + pääomatulot yhteensä. Tietoja vuoteen 1992 asti.

#### `svatva` — Ansiotulot yhteensä valtionverotuksessa

**Ryhmä / Group:** Henkilöverotusaineisto

Ansiotulot yhteensä valtionverotuksessa. Tietoja vuodesta 1993 lähtien.

#### `svatvp` — Pääomatulot yhteensä valtionverotuksessa

**Ryhmä / Group:** Henkilöverotusaineisto

Pääomatulot yhteensä valtionverotuksessa. Tietoja vuodesta 1993 lähtien.

#### `saiprva` — Sairauspäivärahat

**Ryhmä / Group:** Kela

Suoraan vakuutetulle Kelan maksamat sairauspäivärahat. Tietoja vuodesta 1995 lähtien.

#### `elatulo` — Eläketulot

**Ryhmä / Group:** Henkilöverotusaineisto

Eläketulot koostuvat seuraavista verotiedoista:
TKANSEL = Kansaneläke ansiotulona
TANSEL = Työ-, virka- ja yrittäjäeläkkeet
TTAPEL = Pakolliseen tapaturmavakuutukseen perustuva eläke
TLAPEL = Pakolliseen liikennevahinkoturvaan perustuva eläke (vuodesta 2012 alkaen)
TMUUEL1, TMUUEL = Muut eläkkeet
TPOTEL = Potilasvakuutuksen eläke
TEANSTU = Ansiotulona verotettava muu eläke (vuodesta 1993 alkaen)
TPERHEL = Kansaneläkkeen perhe-eläke  (vuodesta 1992 alkaen)
TTYOEL = Työnantajan maksama eläke (vuosina 1998-2017)
TELULKO = Ulkomaille maksettu eläke, josta peritty vain sairaanhoitomaksu  (vuodesta 2006 alkaen)
TPTELAK = Vapaaehtoiseen yksilölliseen eläkevakuutukseen perustuva eläke, 20 % korotus  (vuodesta 2007 alkaen)
TSUURPU = Ulkomaanedustuston virkamiehen puolison erityiskorvaus  (vuodesta 1999 alkaen)
TAKUUEL = Takuueläke  (vuodesta 2011 alkaen)
TELEUVE = EU-virkamiehen vapaaehtoiseen eläkevakuutukseen perustuva eläke  (vuodesta 2014 alkaen).

#### `tkotihtu` — Lapsen kotihoidon tuki ja osittainen hoitoraha

**Ryhmä / Group:** Henkilöverotusaineisto

Lapsen kotihoidon tuki ja osittainen hoitoraha.

#### `aiprva` — Vanhempainpäiväraha

**Ryhmä / Group:** Kela

Suoraan vakuutetulle Kelan maksamat äitiys-, isyys- ja vanhempainrahat sekä erityisäitiysraha. Tietoja vuodesta 1995 lähtien.

#### `tyotur` — Työttömyysturvaetuudet

**Ryhmä / Group:** Henkilöverotusaineisto

Työttömyysturvaetuudet koostuvat seuraavista verotiedoista:

TTYOTPR=Työttömyyspäiväraha, työmarkkinatuki, vuorottelukorvaus ja osa-aikalisä 
TKOULTUK= koulutustuki, aikuisopintoraha ja toistuvaiskorvaus
TTYOLTUK= yrittäjän työllistämistuki (vuodesta 1992 alkaen)

#### `astuki` — Asumistuet

**Ryhmä / Group:** Kela

Asumistuet sisältää yleisen asumistuen, eläkeläisen asumistuen, opiskelijan asumislisän ja lesken asumistuen. Tieto yleisestä asumistuesta on saatavilla sille kotitalouden henkilölle, joka on hakenut tukea. Maksettua tukea ei ole jaettu kotitalouteen kuuluvien kesken. Tietoja vuodesta 1995 lähtien.

#### `opira` — Opintorahat

**Ryhmä / Group:** Kela

Opintorahat sisältää keskiasteen opintorahan, korkeakoulun opintorahan ja aikuisopintorahan, tietoja vuodesta 1995 lähtien.

#### `toimtu` — Toimeentulotuet

**Ryhmä / Group:** Kela, THL

Toimeentulotuet sisältää varsinaisen toimeentulotuen ja ehkäisevän toimeentulotuen.

#### `tpar` — Sairausvakuutuksen päivärahat

**Ryhmä / Group:** Henkilöverotusaineisto

Sairausvakuutuksen päivärahat = (vanhempainpäivärahat + sairauspäivärahat)

#### `ltv` — Valtion tulovero

**Ryhmä / Group:** Henkilöverotusaineisto

Valtion tulovero, tietoja vuoteen 1992 asti.

#### `ltva` — Valtion tuloveron osuus ansiotulojen verosta

**Ryhmä / Group:** Henkilöverotusaineisto

Valtion tuloveron osuus ansiotulojen verosta, tietoja vuodesta 1993 lähtien.

#### `ltvp` — Valtion tuloveron osuus pääomatulojen verosta

**Ryhmä / Group:** Henkilöverotusaineisto

Valtion tuloveron osuus pääomatulojen verosta, tietoja vuodesta 1993 lähtien.

#### `lkuve` — Kunnallisvero

**Ryhmä / Group:** Henkilöverotusaineisto

Kunnallisvero.

#### `lkive` — Kirkollisvero

**Ryhmä / Group:** Henkilöverotusaineisto

Kirkollisvero.

#### `lvv` — Varallisuusvero

**Ryhmä / Group:** Henkilöverotusaineisto

Varallisuusvero, tietoja vuoteen 2005 asti.

#### `lvar` — Verotettava varallisuus

**Ryhmä / Group:** Henkilöverotusaineisto

Verotettava varallisuus, tietoja vuoteen 2005 asti.

#### `velaty` — Velat yhteensä

**Ryhmä / Group:** Henkilöverotusaineisto

Velat yhteensä koostuu seuraavista verotiedoista: 
NLIIKK = Elinkeinotoiminnan velat (vuoteen 1994 saakka) 
NLIIKKY = Elinkeinotoiminnan velat yhteensä (vuosina 1995-2006 ja vuodesta 2014 alkaen) 
NMAAT = Maatalouteen kohdistuneet velat 
NYHT = Velat yhtymistä (vuoteen 2005 saakka) 
NMUUT = Asunto- ja muut velat.

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
