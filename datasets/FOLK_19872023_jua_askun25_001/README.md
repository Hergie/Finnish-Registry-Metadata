# FOLK asuntokunta

- **Identifier:** `FOLK_19872023_jua_askun25_001.xml`
- **DOI:** `work_2019-02_2019-02-28_ain_0002`
- **Temporal coverage:** 1987-12-31 - 2023-12-31
- **Published:** 2025-05-23
- **Organisation:** Tilastokeskus
- **Variable count:** 31
- **Observation count:** —
- **Population:** Kunkin vuoden viimeisenä päivänä Suomessa vakituisesti asunut asuntoväestö
- **Source:** Tilastokeskuksen tulonjaon kokonaistilasto, Verohallinnon rekisterit, Tilastokeskuksen henkilötietovarasto

## Description

FOLK-henkilöaineiston asuntokuntamoduulissa on tietoja asuntoväestöön kuuluvien henkilöiden asuinoloista ja asuntokunnittain summattuja tulotietoja, jotka on poimittu Tilastokeskuksen tulonjakotilaston aineistosta ja henkilöveroaineistosta. Aineistossa on tietoja vuodesta 1987 lähtien. Poikkeamat tietojen saatavuudessa on merkitty muuttujan kuvaukseen vuosiluvuilla, esimerkiksi tulonjakotilaston tietoja on vasta vuodesta 1995 lähtien. 

Tulonjakotilaston aggregaattimuuttujien (palkkatulot, yrittäjätulot, omaisuustulot, saadut tulonsiirrot, maksetut tulonsiirrot, käytettävissä oleva rahatulo) kuvauksissa ei ole lueteltu yksittäisiä tuloeriä. Nämä muuttujat muodostuvat vuosittain päivitettävän tulonjakotilaston tulonimikkeistön pohjalta. Yksittäiset tuloerät on kuitenkin mainittu aineistossa olevien saatujen tulonsiirtojen alaerien, ns. ESSPROS -etuuksien kuvauksissa. Toimeentuloturvana maksettujen etuuksien luokittelu perustuu Euroopan yhteisöjen tilastoviraston, Eurostatin ESSPROS-järjestelmän mukaiseen sosiaalimenojen ja sosiaalietuuksien ryhmittelyyn (The European System of integrated Social Protection Statistics, ESSPROS). ESSPROS-etuuksia ovat sairaus ja terveys, toimintarajoitteisuus, vanhuus, leskien ja muut omaiset, lapsiperheet, työttömyys, asuminen, muu toimeentuloturva. Opintoetuudet eivät lukeudu ESSPROS-etuuksiin, mutta tulonjakotilastossa ne ovat osana kotitalouksien saamia toimeentuloturvaetuuksia (SAATUSI-tieto). 

Tulonjakotilastossa muodostetut tulomuuttujat ovat mahdollisimman tarkasti pyritty muokkaamaan vertailukelpoisiksi eri vuosille. Verottajan aineistosta otetut tiedot eivät ole täysin vertailukelpoisia yli ajan. Vertailukelpoisuutta heikentää verotukseen tehdyt muutokset, joista merkittävin on vuoden 2005 verouudistus, jonka seurauksena esim. ansiotulot ja pääomatulot valtionverotuksessa sekä tulovero ansio- tai pääomatulosta eivät ole täysin vertailukelpoisia tietoja vuosina 1995-2004 ja vuodesta 2005 eteenpäin.

Aineisto on tarkoitettu FIONA-etäpalvelun kautta luovutettavaksi. Tiedot on linkitettävissä muiden henkilövalmisaineistomoduulien kanssa suojatun henkilönumeron avulla.

Vimeisimmät FOLK asuntokunta-aineistot ovat kansiossa FOLK_ASKUN_C, jossa tiedostot on jaettuna tilastovuosittain. Tiedostonimet ovat muodossa folk_askun_"vuosi"_1.

Vanhat FOLK asuntokunta -aineistot ovat FIONAssa seuraavissa kansioissa: 
Totaaliaineisto vuosille 2011-2019: FOLK_askun_11a 
Totaaliaineisto vuosille 2001-2010: FOLK_askun_0110a 
Totaaliaineisto vuosille 1987-2000: FOLK_askun_8700a 

Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@tilastokeskus.fi.

## Variables (31)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `vuosi` | Vuosi | — | — | — |
| `hid_e` | Suojattu henkilön yksilöivä tunniste | — | — | — |
| `ak_koodi` | Asuntokuntanumero | — | — | — |
| `akoko` | Asuntokunnan koko | — | — | — |
| `asty` | Asuntokuntarakenne | — | — | — |
| `asva` | Asumisväljyys | — | — | — |
| `autolkm` | Autojen lkm asuntokunnassa | — | — | — |
| `nika` | Asuntokunnan nuorimman henkilön ikä | — | — | — |
| `palk_ak` | Palkkatulot (asuntokunta) | — | — | — |
| `yrty_ak` | Yrittäjätulot (asuntokunta) | — | — | — |
| `omtu_ak` | Omaisuustulot (asuntokunta) | — | — | — |
| `svatva_ak` | Ansiotulot valtionverotuksessa (asuntokunta) | — | — | — |
| `svatvp_ak` | Pääomatulot valtionverotuksessa (asuntokunta) | — | — | — |
| `saatusi_ak` | Saadut tulonsiirrot (asuntokunta) | — | — | — |
| `saira_ak` | Sairausajan toimeentuloturva (asuntokunta) | — | — | — |
| `vamtyoky_ak` | Toimintarajoitteisuuteen liittyvä tuki (asuntokunta) | — | — | — |
| `vanel_ak` | Vanhuuden turva (asuntokunta) | — | — | — |
| `pelake_ak` | Lesken ja muiden omaisten tuki (asuntokunta) | — | — | — |
| `perav_ak` | Lapsiperheiden etuudet (asuntokunta) | — | — | — |
| `tyoel_ak` | Työttömyysturva (asuntokunta) | — | — | — |
| `asutu_ak` | Asumisen tuet (asuntokunta) | — | — | — |
| `optuki_ak` | Opintoetuudet (asuntokunta) | — | — | — |
| `muutuki_ak` | Muu toimeentuloturva (asuntokunta) | — | — | — |
| `makstu_ak` | Maksetut tulonsiirrot (asuntokunta) | — | — | — |
| `lkuve_ak` | Kunnallisvero (asuntokunta) | — | — | — |
| `ltva_ak` | Tulovero ansiotulosta (asuntokunta) | — | — | — |
| `ltvp_ak` | Tulovero pääomatulosta (asuntokunta) | — | — | — |
| `kturaha_ak` | Käytettävissä oleva rahatulo (asuntokunta) | — | — | — |
| `velaty_ak` | Velat yhteensä (asuntokunta) | — | — | — |
| `modoecd` | Kulutusyksiköt modifioidun OECD-skaalan mukaan | — | — | — |
| `desiili` | Tulodesiilit | — | — | — |

### Variable definitions

#### `vuosi` — Vuosi

Tilastovuosi

#### `hid_e` — Suojattu henkilön yksilöivä tunniste

Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e -tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä.

#### `ak_koodi` — Asuntokuntanumero

Asuntokuntanumero yhdistää asuntokunnan jäsenet tilastovuonna. Sama asuntokuntanumero säilyy henkilöllä eri vuosina vain jos henkilö ei muuta asunnosta pois. Tilastovuodesta 2021 alkaen asuntokuntanumero sisältää myös kirjainarvoja.

#### `akoko` — Asuntokunnan koko

Asunnossa vuoden viimeisenä päivänä vakinaisesti asuvien henkilöiden lukumäärä.

#### `asty` — Asuntokuntarakenne

Asuntokuntarakenne-tieto vuodesta 1990 lähtien. 

Luokitus 2006 alkaen: 
1 = 1 perhe, ei muita 
2 = 1 perhe ja muita 
3 = 2 perhettä, ei lisäksi muita 
4 = 2 perhettä, lisäksi muita 
5 = vähintään 3 perhettä, ei lisäksi muita 
6 = vähintään 3 perhettä, lisäksi muita 
7 = ei perhettä, asuntokunnan koko = 1 
8 = ei perhettä, asuntokunnan koko = 2 joilla sama sukupuoli 
9 = ei perhettä, asuntokunnan koko = 2 joilla eri sukupuoli 
10 = ei perhettä, asuntokunnan koko > 2; kaikilla sama sukupuoli 
11 = ei perhettä, asuntokunnan koko > 2; joilla eri sukupuoli
 
Luokitus vuoteen 2005: 
1 = 1 perhe ja ei muita 
2 = 1 perhe ja muita 
3 = 2+ perhettä ja ei muita 
4 = 2+ perhettä ja muita, 
5 = ei perhettä 1 henkilö, 
6 = ei perhettä, 2 henkilöä samaa sukupuolta. 
7 = ei perhettä, 2 henkilöä eri sukupuolta, 
8 = ei perhettä, väh. kolme henkilä samaa sukupuolta, 
9 = ei perhettä vähintään 3 henkilöä, kaikki eivät samaa sukupuolta
null = ei asukkaita
 
Vuotta 2006 edeltävän luokituksen muuntaminen nykyiseen, (vanha luokitus = uusi luokitus): 
1 = 1 
2 = 2 
3 = 3, 5 
4 = 4, 6 
5 = 7 
6 = 8 
7 = 9 
8 = 10 
9 = 11

#### `asva` — Asumisväljyys

Asumisväljyysluokitus: 
1 = Tilava. 1-5 henkilön asuntokunta, jonka käytössä on vähintään kolme asuinhuonetta enemmän kuin asuntokunnan henkilömäärä (keittiötä ei lueta huonelukuun) 
2 = Normaali 
3 = Ahdas. Enemmän kuin yksi henkilö huonetta kohti (keittiötä ei lueta huonelukuun) 
4 = Tuntematon 

Keittiötä ei ole luettu mukaan huonelukuun vuodesta 1989 lähtien.

#### `autolkm` — Autojen lkm asuntokunnassa

Tieto vuosilta 1990, 1994-1996, 1998  ja vuodesta 2000 lähtien vuosittain. Asuntokunnille summataan asuntokunnan hallinnassa tai omistuksessa olevat autot (kuorma-auto, erikoisauto, pakettiauto, henkilöauto). Auto on ensisijaisesti haltijan nimissä, mutta jos haltijan henkilötunnusta ei ole ollut niin silloin auto on omistajan nimissä.

#### `nika` — Asuntokunnan nuorimman henkilön ikä

Asuntokunnan nuorimman henkilön ikä.

#### `palk_ak` — Palkkatulot (asuntokunta)

Asuntokunnan jäsenten yhteenlasketut palkkatulot kunkin vuoden tulonjakotilaston tulonimikkeistön mukaan. Negatiiviset arvot nollattu. Tietoja vuodesta 1995 lähtien.

#### `yrty_ak` — Yrittäjätulot (asuntokunta)

Kaikki yrittäjätulot kunkin vuoden tulonjakotilaston tulonimikkeistön mukaan. Muuttuja on summattu maa- ja metsätilatalouden yrittäjätulot, elinkeinon harjoittajien yrittäjätulot, yhtymien yrittäjätulot ja tekijänoikeuksista, patenteista yms. tulevat yrittäjätulot. Tietoja vuodesta 1995 lähtien.

#### `omtu_ak` — Omaisuustulot (asuntokunta)

Asuntokunnan jäsenten yhteenlasketut omaisuustulot kunkin vuoden tulonjakotilaston tulonimikkeistön mukaan. Muuttujaan on summattu henkilöveroaineistosta omaisuustuloiksi tulonjakotilastossa määritetyt rekisteripohjaiset tuloerät. Siten mm. haastatelluin kerättävät lähdeveronalaiset korkotulot jäävät puuttumaan tulonjaon kokonaistilaston omaisuustuloista. Tietoja vuodesta 1995 lähtien.

#### `svatva_ak` — Ansiotulot valtionverotuksessa (asuntokunta)

Asuntokunnan jäsenten yhteenlasketut ansiotulot yhteensä valtionverotuksessa. Tietoja vuodesta 1993 lähtien.

#### `svatvp_ak` — Pääomatulot valtionverotuksessa (asuntokunta)

Asuntokunnan jäsenten yhteenlasketut pääomatulot yhteensä valtionverotuksessa. Tietoja vuodesta 1993 lähtien.

#### `saatusi_ak` — Saadut tulonsiirrot (asuntokunta)

Asuntokunnan jäsenten yhteenlasketut saatujen tulonsiirtojen yhteissummat. Muuttuja muodostuu vuosittain päivitettävän tulonjakotilaston tulonimikkeistön pohjalta. Tietoja vuodesta 1995 lähtien.

#### `saira_ak` — Sairausajan toimeentuloturva (asuntokunta)

Asuntokunnan jäsenten yhteenlasketut ESSPROS -luokituksen mukaiset sairauteen liittyvät etuudet. Muuttujaan on summattu Kelan maksamat sairasvakuutuksen suoraan vakuutetulle maksetut sairauspäivärahat (SAIPRVA) ja ruokavaliokorvaus (RVVM vuosina 2002-2016). Lisäksi muuttujaan on summattu tapaturmapäiväraha (TTAPPR) ja sairauskassojen maksamat lisä- ja täydennyspäivärahat, jotka ovat verottajan tiedoissa (TPAR), mutta eivät sisälly Kelan em. etuuksiin (LISAPR). Tietoja vuodesta 1995 lähtien.

#### `vamtyoky_ak` — Toimintarajoitteisuuteen liittyvä tuki (asuntokunta)

Asuntokunnan jäsenten yhteenlasketut ESSPROS -luokituksen mukaiset työkyvyttömyys ja vammaisetuudet. Muuttujaan on summattu Kelan maksama työkyvyttömyyseläke (KELATK), ETK:n työeläkejärjestelmien työkyvyttömyyseläkkeet lain ja lajin mukaan (TYELTK, TELTK, LELTK, YELTK, MYELTK, MELTK, VELTK, KVTELTK, KIELTK, SPYMTK ja KUNTOUTU) sekä Valtionkonttorin sotilasvammalain mukaiset etuudet (SOTTK, SOTAVLIS, SOTTAYDE, SOTLISEL). Lisäksi muuttujaan on summattu henkilöveroaineistosta lakisääteisten tapaturma- ja potilasvakuutusten eläkkeet (TTAPEL ja TPOTEL) sekä takuueläkkeen (TAKUUEL) ja ulkomaan eläkkeiden (TULKEL) työkyvyttömmyyseläkkeiksi määritellyt osuudet (TAKUUELTK ja TULKELTK). Tietoja vuodesta 1995 lähtien.

#### `vanel_ak` — Vanhuuden turva (asuntokunta)

Asuntokunnan jäsenten yhteenlasketut ESSPROS -luokituksen mukaiset vanhuuden turvaan luettavat etuudet. Muuttujaan on summattu Kelan maksama vanhuuseläke (KELAVE) ja rintamalisät (RILI ja RIYLLI), ETK:n työeläkejärjetelmien vanhuuseläkkeet lain ja lajin mukaan (TYELVE, TELVE, LELVE, YELVE, MYELVE, MELVE, VELVE, KVTELVE, KIELVE, SPYMVE ja MAATEREL). Lisäksi muuttujaan on summattu henkilöveroaineistosta ulkomaanedustuston virkamiehen puolison erityiskorvaus (TSUURPU) sekä takuueläkkeen (TAKUUEL) ja ulkomaan eläkkeiden (TULKEL) vanhuusseläkkeiksi määritellyt osuudet (TAKUUELVE ja TULKELVE). Tietoja vuodesta 1995 lähtien.

#### `pelake_ak` — Lesken ja muiden omaisten tuki (asuntokunta)

Asuntokunnan jäsenten yhteenlasketut ESSPROS -luokituksen mukaiset lesken ja orpojen lasten tuet. Muuttujaan on summattu Kelan lesken ja lasten perhe-eläkkeet (LEPE, LETO, LAKE), ETK:n ansioeläkejärjestelmien perhe-eläkkeet (TYELPE, TELPE, LELPE, YELPE, MYELPE, MELPE, VELPE, KVTELPE, KIELPE, SPYMPE), Valtionkonttorin sotilasvammalain mukaiset perhe-eläkkeet ja -korvaukset (SOTPE ja SOTPEPIT) sekä perhe-eläikkeiksi määritelty jäännöserä verottajan ansioeläketiedon (TANSEL) ja ETK:n ansioeläkesumman positiivisesta erotuksesta. Tietoja vuodesta 1995 lähtien.

#### `perav_ak` — Lapsiperheiden etuudet (asuntokunta)

Asuntokunnan jäsenten yhteenlasketut ESSPROS -luokituksen mukaiset lapsiperheiden tuet. Muuttujaan on summattu Kelan rekistereistä oman kansaneläkkeen lapsikorotus (OMALAPSK), vanhempainpäivärahat (AITPRV), kotihoidon tuet (KTHR, KTHL, KTKU, OSHR), lapsilisät (LLMK), lapsen vammaistuki (LHOTU) ja erityishoitoraha (sairaan lapsen hoito- ja kuntoutusavustus WMKY). Lisäksi muuttujaan on summattu verottajan kotihoidontuen (TKOTIHTU) ja edellä mainittujen Kelan kotihoidontukien positiivinen erotus (TKOTIMUO). Tietoja vuodesta 1995 lähtien.

#### `tyoel_ak` — Työttömyysturva (asuntokunta)

Asuntokunnan jäsenten yhteenlasketut ESSPROS -luokituksen mukaiset työttömyyteen liittyvät etuudet. Muuttujaan on summattu Kelan työttömyyseläkkeet (KELATY), ETKn eri ansioeläkejärjestelmien työttömyyseläkkeet (TYELTY, TELTY, LELTY, YELTY, MYELTY, MELTY, VELTY, KVTELTY, KIELTY, SPYMTY), Kelan työttömyyden peruspäivärahat (YHTE), kotoutumustuki (YHTEZ) ja työmarkkinatuki (TMTUKIMK) , finassivalvonnan ansiosidonnaiset työttömyyspäivärahat (VVVMK1 ja VVVMK5), henkilöveroaineiston yrittäjän työllistämistuki (TTYOLTUK), koulutustuet (TKOULTUK) sekä rekisterivertailuista syntyvät ns. jäännöserät (TYOTKMUU ja TUNTELTY). Tietoja vuodesta 1995 lähtien.

#### `asutu_ak` — Asumisen tuet (asuntokunta)

Asuntokunnan jäsenten yhteenlasketut ESSPROS -luokituksen mukaiset asumisen tuet. Muuttujaan on summattu Kelan yleinen asumistuki (ASTUKI), eläkkeensaajan asumistuki (AEMKM) ja opintorahan asumislisä (ASULI). Tietoja vuodesta 1995 lähtien.

#### `optuki_ak` — Opintoetuudet (asuntokunta)

Asuntokunnan jäsenten yhteenlasketut opintoetuudet. Opintoetuudet eivät kuulu ESSPROS-etuuksiin, mutta sisältyvät kuitenkin asuntokuntien saamiin toimeentuloturvaetuuksiin (SAATUSI).  Muuttujaan on summattu Kelan opintorahat (OPIRAKE ja OPIRAKO), Koulutusrahaston ammattitutkintosipendit (AMSTIPE) ja verottajan veronalainen apuraha (TAPUR). Tietoja vuodesta 1995 lähtien.

#### `muutuki_ak` — Muu toimeentuloturva (asuntokunta)

Asuntokunnan jäsenten yhteenlasketut muut toimeentuloturvaetuudet ESSPROS-luokituksen mukaan. Muuttujaan on summattu THL:n toimeentulotuki, Kelan sotilasavustus, Kelan maahanmuuttajatuki ja Kelan opintolainojen korkoavustus. Tietoja vuodesta 1995 lähtien.

#### `makstu_ak` — Maksetut tulonsiirrot (asuntokunta)

Asuntokunnan jäsenten yhteenlasketut maksettujen tuloverojen ja veronluonteisten maksujen yhteissummat. Muuttuja muodostuu vuosittain päivitettävän tulonjakotilaston tulonimikkeistön pohjalta. Muuttujaan on summattu palkka-, yrittäjä- ja omaisuustulosta sekä saaduista tulonsiirroista maksetut valtion ja kuntien verot ja veronluonteiset pakolliset maksut. Huom. kirkollisvero katsotaan vapaehtoiseksi veroksi, joten sitä ei huomioida maksetuissa tulonsiirroissa. Tietoja vuodesta 1995 lähtien.

#### `lkuve_ak` — Kunnallisvero (asuntokunta)

Asuntokunnille summattu kunnallisvero.

#### `ltva_ak` — Tulovero ansiotulosta (asuntokunta)

Asuntokunnille summattu valtion tuloveron osuus ansiotulojen verosta, tietoja vuodesta 1993 lähtien.

#### `ltvp_ak` — Tulovero pääomatulosta (asuntokunta)

Asuntokunnille summattu valtion tuloveron osuus pääomatulojen verosta, tietoja vuodesta 1993 lähtien.

#### `kturaha_ak` — Käytettävissä oleva rahatulo (asuntokunta)

Asuntokunnan jäsenten yhteenlasketut käytettävissä oleva rahatulot. Käytettävissä oleva rahatulo muodostuu palkka-, yrittäjä- ja omaisuustuloista sekä saaduista tulonsiirroista vähennettynä em. tuloista maksetusta veroista ja veronluonteisista maksuista. Tulonjaon kokonaistilaston päätulokäsite, joka muodostuu vuosittain päivitettävän tulonjaon tulonimikkeistön pohjalta. Tietoja vuodesta 1995 lähtien.

#### `velaty_ak` — Velat yhteensä (asuntokunta)

Asuntokunnan jäsenten yhteenlasketut velat yhteensä koostuu seuraavista verotiedoista:
NLIIKK = Elinkeinotoiminnan velat (vuoteen 1994 saakka) 
NLIIKKY = Elinkeinotoiminnan velat yhteensä (vuosina 1995-2006 ja vuodesta 2014 alkaen) 
NMAAT = Maatalouteen kohdistuneet velat 
NYHT = Velat yhtymistä (vuoteen 2005 saakka) 
NMUUT = Asunto- ja muut velat

#### `modoecd` — Kulutusyksiköt modifioidun OECD-skaalan mukaan

Tulonjakotilastossa ja kulutustutkimuksessa on käytetty vuodesta 2002 lähtien Euroopan unionin tilastoviraston Eurostatin suosittamaa OECD:n ns. muunnettua kulutusyksikköasteikkoa, jossa - kotitalouden ensimmäinen aikuinen saa painon 1 - muut yli 13-vuotiaat saavat painon 0,5 - lapset saavat painon 0,3 (0–13-vuotiaat). Tietoja vuodesta 1995 lähtien.

#### `desiili` — Tulodesiilit

Tulokymmenykset eli tulodesiilit muodostetaan tulonjakotilastossa asuntokunnan ekvivalenttien käytettävissä olevien rahatulojen pohjalta.Desiiliryhmät eli tulokymmenykset on muodostettu jakamalla ensin asuntokunnan tulot talouden kulutusyksiköillä (ns. ekvivalentit tulot). Jokaiselle kotitalouden jäsenelle tulee sama ekvivalentti tulo. Henkilöt järjestetään tämän jälkeen tulojensa mukaiseen järjestykseen ja jaetaan kymmeneen yhtä suureen ryhmään. Jokaisessa tulokymmenyksessä on siten 10 prosenttia väestöstä. Ensimmäiseen tulokymmenykseen kuuluu pienituloisin kymmenes ja viimeiseen suurituloisin. Tulokymmenysten tulo-osuudet osoittavat, kuinka suuren osan kyseessä olevien tulojen kokonaissummasta kukin kymmenys saa. Tietoja vuodesta 1995 lähtien.

---

[← Back to catalogue](../../README.md)
