# TAX_XPER Työnantajan tai suorituksen maksajan vuosi-ilmoitus verohallinnolle (2006-2017)

- **Identifier:** `TAX_20062017_jua_XPER_002.xml`
- **DOI:** `work_2020-03_2020-03-17_ain_0001`
- **Temporal coverage:** 2006-01-01 - 2017-12-31
- **Published:** 2022-01-10
- **Organisation:** Tilastokeskus
- **Variable count:** 47
- **Observation count:** —
- **Population:** Työnantajat
- **Source:** Verohallinnon Tilastokeskukselle tilastotarkoituksiin toimittama vuosi-ilmoitusaineisto

## Kuvaus / Description

Työnantajan tai suorituksen maksajan vuosi-ilmoitustiedot ovat saatavissa tutkimuskäyttöön suorituksittain vuosilta 1995 - 2019.

Työnantajan tai suorituksen maksajan on annettava Verohallinnolle vuosi-ilmoitus (lomake 7801) maksamistaan palkoista, työkorvauksista ja muista suorituksista kuten käyttökorvauksista ja palkkioista. Myös luontoiseduista, työsuhdeoptioista ja osakepalkkioista, päivärahoista, kilometrikorvauksista ja vapaaehtoisista eläkemaksuista ilmoitetaan vuosi-ilmoituksella.

XPER-tiedostoihin on yhdistetty vuosi-ilmoitustiedot myös eläkkeistä (7803), puunostajien metsäkaupoista (7807) ja TVL:n mukaisista koroista, voitto- ja rahasto-osuuksista (7805).

Vuosina 1995-1998 tiedot ovat markoissa, 1999-2001 markoissa/euroissa (rahayks) ja vuodesta 2002 lähtien euroissa.

Palkoista ja muista ansiotuloista ei enää ole annettu vuosi-ilmoitusta vuodesta 2019 lähtien, vaan palkat ja muut ansiotulot on ilmoitettu tulorekisteriin.

Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@stat.fi.

## Muuttujat / Variables (47)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `suorlaji` | Suorituslaji | — | — | — |
| `palkka` | Palkka | — | — | — |
| `ennpid` | Ennakonpidätys | — | — | — |
| `lakismak` | Eläke- ja työttömyysvakuutusmaksut | — | — | — |
| `vahennpi` | Vähennys ennen ennakonpidätystä | — | — | — |
| `autolis` | Verotettavan autoedun määrä | — | — | — |
| `autokorv` | Työnantajan perimä korvaus autoedusta | — | — | — |
| `autokaut` | Auton käyttöetu | — | — | — |
| `autovapa` | Vapaa autoetu | — | — | — |
| `korkoetu` | Asuntolainan korkoetu | — | — | — |
| `muulis` | Muut luontoisedut, palkkaan lis. | — | — | — |
| `muukorva` | Muut luontoisedut, työnant. perimä korvaus | — | — | — |
| `asuntoet` | Asuntoetu | — | — | — |
| `ravintoe` | Ravintoetu | — | — | — |
| `muuetu` | Muu etu | — | — | — |
| `ravintva` | Ravintoedun korvaus vastaa verotusarvoa | — | — | — |
| `paivarah` | Päivärahat yhteensä | — | — | — |
| `kokopvra` | Kokopäiväraha | — | — | — |
| `osapvrah` | Osapäiväraha | — | — | — |
| `ulkompvr` | Ulkomaanpäiväraha | — | — | — |
| `ateriako` | Ateriakorvaus | — | — | — |
| `kilometr` | Kilometrikorvaus, km | — | — | — |
| `kilomkor` | Kilometrikorvaus | — | — | — |
| `muukorv` | Muut maksetut korvaukset | — | — | — |
| `puheline` | Puhelinetu | — | — | — |
| `optio` | Optioetu | — | — | — |
| `tavakmak` | Kollekt. lisäeläketurvan vakuutusmaksut, työnantajan maksamat | — | — | — |
| `psvakmak` | Kollekt. lisäeläketurvan vakuutusmaksut, palkansaajan maksamat | — | — | — |
| `vayelmak` | Vapaaeht. yksilöllisen eläkevakuutuksen maksut | — | — | — |
| `luhlomak` | Luottamushenkilömaksu | — | — | — |
| `palkeisv` | Palkka, josta ei sairausvakuutusmaksua | — | — | — |
| `tsmlietu` | Työntekijällä on työsuhdematkalippu käytössä 1=on, 0=ei | — | — | — |
| `tsmlivah` | Työsuhdematkalippuetu | — | — | — |
| `everonal` | Eläkkeen tai etuuden veronalaisen osan määrä | — | — | — |
| `suoritus` | Suorituksen määrä | — | — | — |
| `omistaja` | Metsänomistajaryhmä | — | — | — |
| `kauppahi` | Metsän kauppahinta | — | — | — |
| `alvosuus` | Arvonlisäveron osuus myyjälle | — | — | — |
| `smak_yrtun` | Suojattu maksajan tunnus, yritystunnus | — | — | — |
| `smak_hnro` | Suojattu maksajan tunnus, henkilönumero | — | — | — |
| `smak_muutun` | Suojattu maksajan muu tunnus | — | — | — |
| `ssaa_hnro` | Suojattu saajan henkilönumero | — | — | — |
| `ssaa_yrtun` | Suojattu saajan yritystunnus | — | — | — |
| `ssaa_muutun` | Suojattu saajan muu tunnus | — | — | — |
| `srah_yrtun` | Suojattu sijoitusrahaston tunnus, yritystunnus | — | — | — |
| `srah_muutun` | Suojattu sijoitusrahaston tunnus, muu | — | — | — |
| `vuosi` | Maksuvuosi | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `suorlaji` — Suorituslaji

Suorituslajilla tarkoitetaan ilmoitettavan tulon laatua. Suorituslajeja ovat mm. palkka, palkkio, työkorvaus, kulu- ja käyttökorvaus tai eläke. Suorituslajien luokituksessa saattaa olla puutteita vuosittaisten muutosten vuoksi. Joitakin suorituslajeja on yhdistelty luokkiin F, L ja H4. Suorituslajien tunnukset ovat:
1 Palkka sivutoimesta	
1Y Yrittäjän palkka sivutoimesta (palkka tehtävästä, josta saaja on YEL- tai MYEL-vakuuutettu)	
2 Merityötulo	
2B Sijoitusrahaston voitto-osuus	
2C Joukkovelkakirjalainan korko	
2D Muu korko tai pääomatulo	
2E Vuosi-ilmoituksen antajan maksama jälkimarkkinahyvitys verovelvolliselle	
2F Vuosi-ilmoituksen antajan perimä (saama) jälkimarkkinahyvitys	
2G Sijoitusrahaston rahasto-osuus	
2M Merityötulo, joka kuuluu matkustaja-alusten maksuvapautuksen piiriin (2005-2007)	
2Y Yrittäjän merityötulo	
3J Ulkomaisen yhteissijoitusyrityksen osuudelle maksettu korko	
3K Ulkomailta maksettu/välitetty korko	
3L Ulkomaisen yhteissijoitusyrityksen osuus	
3M Toisesta EU-jäsenvaltiosta maksettu/välitetty korko (alkaen 2009)	
3N Toisesta EU-jäsenvaltiosta maksettu/välitetty myynnin,	
takaisinoston tai lunastuksen tuoton kokonaismäärä	
5 Ns. 6 kk:n säännön alainen palkka	
5Y Yrittäjän 6 kk:n säännön alainen palkka	
6 Sijaismaksajan maksama palkka	
61 Sijaismaksajan maksama 6 kk:n säännön alainen palkka	
7K Työnantajan (kiinteä toimipaikka Suomessa) maksama palkka	
työntekijälle, joka ei ole Suomessa vakuutettu (alkaen 2009)	
7L Ulkomaisen työnantajan (ei kiinteää toimipaikkaa Suomessa)	
maksama palkka työntekijälle, joka ei ole Suomessa vakuutettu (alkaen 2009)	
7M Ulkomaisen työnantajan (ei kiinteää toimipaikkaa Suomessa)	
maksama palkka Suomessa vakuutetulle työntekijälle (alkaen 2009)	
7N Ulkomaisen työnantajan (ei kiinteää toimipaikkaa Suomessa)	
maksama palkka työntekijälle, kun työnantaja maksaa 	
työntekijän puolesta verot (nettopalkkasopimus) (alkaen 2009)	
7Q Ulkomaisen työnantajan (ei kiinteää toimipaikkaa Suomessa) 	
maksama palkka työntekijälle, joka on oleskellut Suomessa	
enintään 183 päivää verosopimuksessa tarkoitettuna ajanjaksona (alkaen 2009)	
9A Metsänmyyntitulot pystykaupoista (ennen 1.4.2008, 2009-2011)	
9B Metsänmyyntitulot hankinta- tai käteiskaupoista (ennen 1.4.2008, 2009-2011)	
9C Puun myynnin vakuutussuoritus	
9D 1.4.2008-31.12.2009 tehty pystykauppa (2009-2010)	
9E 1.4.2008-31.12.2009 tehty hankinta- tai käteiskauppa (2009-2010)	
9F 1.1.2010-31.12.2010 tehty pystykauppa (2010-2011)	
9G 1.1.2010-31.12.2010 tehty hankinta- tai käteiskauppa (2010-2011)	
A Kansaneläke	
AA Takuueläke (alkaen 2011)	
B Työ-, virka- ja yrittäjäeläke	
B6 Eläke, joka maksettu ulkomailla asuvalle henkilölle ja josta	
peritty vain sairausvakuutusmaksu	
F Muut eläkkeet	
G Ansiotuloa oleva käyttökorvaus	
G1 Pääomatulot (käyttökorvaus, palkkasaatavan korko tms.)	
H Työkorvaus	
H1 Henkilöstörahaston rahasto-osuus ja ylijäämä	
H2 Urheilijan palkkio	
H3 Perhehoitajan tai omaishoitajan palkkio	
H4 Muu ansiotuloa oleva suoritus	
H5 Yleishyöd. yhteisön maksama matkakustannusten korvaus	
H6 Sovittelijan kulukorvaus (alkaen 2007)	
HT Työpanokseen perustuva osinko (työkorvausta) (alkaen 2010)	
J Takaisin peritty suoritus, jolla ei ole omaa suorituslajia	
K Vapaaehtoiseen henkilövakuutukseen perustuvat suoritukset,	
mm. potilas- ja vastuuvakuutuksen ansionmenetyskorvaus	
L Pakollisen tapaturma- ja liikennevakuutuksen päiväraha, vastuuvakuutuskorvaus ym.	
M Veronalainen lakkoavustus	
O Yleinen perhe-eläke	
P Palkka päätoimesta	
P2 Urheilijan palkka (vuoteen 2010 asti)	
P3 Kunnallisen perhepäivähoitajan palkka	
PT Työpanokseen perustuva osinko (palkkaa) (alkaen 2010)	
PU Urheilijarahastosta maksettava palkka (2011 asti)	
PY Yrittäjän palkka päätoimesta (palkka tehtävästä, josta saaja on YEL- tai MYEL-vakuuutettu)	
Q Vapaaehtoisen yksilölliseen eläkevakuutukseen perustuva	
pääomatuloa oleva vuosittain maksettava eläke (2009 asti suorituslajin kuvaus: vapaaehtoisen henkivakuutuksen suoritukset ym.)	
Q1 Pitkäaikaissäästämissopimukseen perustuva pääoamtuloa oleva (alkaen 2011)	
vuosittain maksettava suoritus	
Q2 Muut pääomatulona verotettavat eläkkeet ja etuudet (alkaen 2010)	
Q3 Kapitalisaatiosopimuksen tuotto (alkaen 2013)	
R1 Reserviläispalkka	
S Sairausvakuutuslain ym. nojalla maksettavat korvaukset	
SA Sairauskassan täydennyspäiväraha	
T Työttömyyspäiväraha ym.	
U Koulutustuki, toistuva korvaus, aikuiskoulutustuki	
V Tuesta tai päivärahasta peritty eläkemaksu (2006 asti)	
V1 Pääomatuloa oleva vapaaehtoiseen eläkevakuutukseen perustuva	
eläke, joka luetaan tuloksi 50 prosentilla korotettuna (2007-2009) / 20 prosentilla korotettuna (alkaen 2010)	
V2 Vapaaehtoiseen yksilölliseen eläkevakuutukseen perustuva eläke,	
joka verotetaan pääomatulona 50 prosentilla korotettuna (alkaen 2010)	
V3 Pitkäaikaissäästämissopimukseen perustuva suoritus, joka	
verotetaan pääomatulona 20 prosentilla korotettuna	
V4 Pitkäaikaissäästämissopimukseen perustuva suoritus, joka	
verotetaan pääomatulona 50 prosentilla korotettuna (alkaen 2011)	
W Maatalousyrittäjän luopumiskorvaus	
W1 Opintoraha	
X Lapsen kotihoidontuki ja osittainen hoitoraha	
Y Starttiraha (yrittäjän työllistämistuki) (alkaen 2011)	
YT YEL/MYEL-vakuutetun yrittäjän työpanokseen perustuva osinko	
(palkkaa) (alkaen 2010)	
Z Eläkevakuutusmaksun palautus	
Z Lakisääteisen eläkevakuutusmaksun palautus

#### `palkka` — Palkka

Maksetut ennakonpidätyksen alaiset palkat ilman luontoisetuja, euroa (€). Palkalla tarkoitetaan mitä tahansa palkkaa, palkkiota ja korvausta, joka saadaan työ- tai virkasuhteessa, sekä kokouspalkkiota, henkilökohtaista luento- ja esitelmäpalkkiota, hallintoelimen jäsenyydestä saatua palkkiota, toimitusjohtajan palkkiota, avoimen yhtiön ja kommandiittiyhtiön yhtiömiehen nostamaa palkkaa sekä luottamustoimesta saatua korvausta. Palkkaa ovat myös asunto-, ravinto- ym. luontoisedut sekä veronalaiset henkilökuntaedut ja veronalaiset kustannusten korvaukset.

#### `ennpid` — Ennakonpidätys

Maksetuista palkoista toimitetun ennakonpidätyksen määrä, euroa (€). Ennakonpidätyksellä tarkoitetaan useimmiten tuloveron ennakonpidätystä, jonka työnantaja tekee työntekijän palkkatulosta ja tulouttaa verottajalle.

#### `lakismak` — Eläke- ja työttömyysvakuutusmaksut

Eläke- ja työttömyysvakuutusmaksut yhteensä, euroa (€). Palkoista maksetut  ja työnantajan eläkeyhtiöille ilmoittamat työttömyysvakuutusmaksut ja työeläkemaksut yhteensä, euroa (€).

#### `vahennpi` — Vähennys ennen ennakonpidätystä

Vähennys, joka on tehty palkasta ennen ennakonpidätyksen toimittamista, euroa (€). Työnantaja voi vähentää ennen ennakonpidätyksen toimittamista palkansaajan itsensä maksamat työn tekemisestä aiheutuneet välittömät kustannukset. Tällaisia kustannuksia ovat mm. palkansaajan maksamat kustannukset moottorisahan käytöstä ja muut työvälineistä aiheutuneet kustannukset tai menot työmatkoista, jos työnantaja ei maksa niistä verovapaita korvauksia palkan lisäksi.

#### `autolis` — Verotettavan autoedun määrä

Auton verotusarvon ja työntekijältä perityn määrän erotus, euroa (€). Autoedun määrää ei ole ilmoitettu jos työnantaja perii työntekijältä autoedusta vähintään edun verotusarvon mukaisen määrän. Verotettava autoetu on ilmoitettu myös silloin kun työntekijällä on pelkkä autoetu eikä rahapalkkaa ole maksettu lainkaan.

#### `autokorv` — Työnantajan perimä korvaus autoedusta

Työnanantajan työntekijältä perimä korvaus autoedusta, euroa (€). Korvaus autoedusta on ilmoiettu vaikka työnantaja perisi autoedusta vähintään autoedun raha-arvoa vastaavan tai suuremman korvauksen.

#### `autokaut` — Auton käyttöetu

Työntekijällä on auton käyttöetu, 1=kyllä, 0=ei. Auton käyttöedussa työntekijä vastaa itse ainakin auton polttoainekuluista. Käyttöedussa työntekijälle maksetaan korvausta työajoista auton polttoainekuluista laadittua matkalaskua vastaan.

#### `autovapa` — Vapaa autoetu

Työntekijällä on vapaa autoetu, 1=kyllä, 0=ei. Työnantaja maksaa kaikki autosta aiheutuneet kustannukset myös yksityisajojen osalta.

#### `korkoetu` — Asuntolainan korkoetu

Asuntolainan korkoedun määrä, euroa (€). Työsuhteen perusteella annetusta asuntolainasta työntekijälle syntyvä korkoetu. Työntekijälle syntyy korkoetu, jos työnantaja perii työntekijälle myöntämästään lainasta vuotuista korkoa, joka on alempi kuin viitekorko, silloin kun lainan korko on sidottu yleisesti markkinoilla käytössä olevaan lainan viitekorkoon. Jos lainan korkoa ei ole sidottu viitekorkoon, työntekijälle syntyy korkoetu, silloin kun lainasta peritty vuotuinen korko on alempi kuin 12 kuukauden euribor-korko vuoden ensimmäisenä päivänä.

#### `muulis` — Muut luontoisedut, palkkaan lis.

Muut luontoisedut, palkkaan lisätty määrä, euroa (€). Luontoisetujen verotusarvojen ja työntekijältä perittyjen korvausten erotus. Luontoisetuja ovat työnantajan muuna kuin rahana antamat edut, mm. asunto-, puhelin- ja ravintoetu. Muita etuja ovat myös mm. autotalli- ja vene-etu, palkaksi katsotut henki- ja eläkevakuutusmaksut, yksilöimättömästä lahjakortista syntyvä etu, merimiespalveluksessa olevan henkilön merimiehenä saama luontoisetu ja henkilöstöannista syntyvät edut.  Jos verotusarvoa ei ole erikseen vahvistettu Verohallinnon antamassa päätöksessä, luontoisedun arvo on sen käypä arvo. Luontoisetujen määrä on ilmoitettu, vaikka työntekijälle ei maksettaisi lainkaan rahapalkkaa tai rahapalkka ei riittäisi ennakonpidätyksen täysimääräiseen toimittamiseen.

#### `muukorva` — Muut luontoisedut, työnant. perimä korvaus

Muut luontoisedut; työnantajan perimä korvaus on summa, joka työntekijältä on peritty muista luontoiseduista kuin autoedusta tai työsuhdematkalippuedusta, euroa (€).

#### `asuntoet` — Asuntoetu

Työntekijällä on luontoisetuna asuntoetu, 1=kyllä, 0=ei. Kun työntekijä on saanut asunnon käytettäväksesi työ- tai virkasuhteen perusteella tai asunto kuuluu palkkaan, tämä on verotettavaa asuntoetua. Asunnon arvoon vaikuttavat asunnon ikä, perusparannukset sekä pinta-ala.

#### `ravintoe` — Ravintoetu

Työntekijällä on luontoisetuna ravintoetu, 1=kyllä, 0=ei. Ravintoedun arvo määräytyy sen mukaan, onko kyseessä tavanomainen työpaikkaruokailu, laitosruokailu, ruokailun valvonnan yhteydessä saatu etu, hotelli-, ravintola- tai lentohenkilöstön, lounasseteli tai muu vastaava ravintoetu.

#### `muuetu` — Muu etu

Työntekijällä on luontoisetuna muu etu, 1=kyllä, 0=ei. Tällaisia etuja ovat esimerkiksi kodinhoitoetu, vene-etu ja palkkiomatka. Jos työsuhde-edun arvoa ei ole määritelty Verohallinnon päätöksessä, edun arvona pidetään käypää arvoa.

#### `ravintva` — Ravintoedun korvaus vastaa verotusarvoa

Työntekijältä ravintoedusta peritty korvaus vastaa verohallinnon antaman luontoisetupäätöksen mukaista ravintoedunarvoa, 1=kyllä, 0=ei

#### `paivarah` — Päivärahat yhteensä

Verovapaiden päivärahojen ja ateriakorvausten yhteismäärä euroa (€). Myös seuraavat ulkomaantyöskentelyyn liittyvät verovapaat edut, verovelvollisen ja hänen perheenjäsenensä muutto- ja matkakustannukset työntekovaltioon ja takaisin, työnantajan kustantama lasten perus- ja lukiotason koulutus, työnantajan ulkomailla kustantama tavanomainen yksityinen palveluhenkilöstö.

#### `kokopvra` — Kokopäiväraha

Työnantaja on maksanut kokopäivärahaa tai ateriaedun sisältävää puolitettua kokopäivärahaa, 1=kyllä, 0=ei

#### `osapvrah` — Osapäiväraha

Työnantaja on maksanut puolitettua päivärahaa, 1=kyllä, 0=ei

#### `ulkompvr` — Ulkomaanpäiväraha

Työnantaja on maksanut ulkomaanpäivärahaa tai ateriaetua sisältävää puolitettua ulkomaanpäivärahaa, 1=kyllä, 0=ei

#### `ateriako` — Ateriakorvaus

Työnantaja on maksanut ateriakorvausta sisältävää puolitettua osapäivärahaa, 1=kyllä, 0=ei

#### `kilometr` — Kilometrikorvaus, km

Kilometrikorvauksen perusteena oleva kilometrimäärä, km (kilometrit).

#### `kilomkor` — Kilometrikorvaus

Verovapaiden kilometrikorvausten yhteismäärä, pl. muut matkakorvaukset, yhteensä euroa (€)

#### `muukorv` — Muut maksetut korvaukset

Muut maksetut korvaukset, esim. työpuku, -väline, tms, euroa (€).

#### `puheline` — Puhelinetu

Työntekijälle on annettu luontoisetuna puhelinetu, 1=kyllä, 0=ei . Jos työntekijä soittaa puhelimella vapaa-aikana yksityispuheluja ja työnantaja maksaa myös ne, saat työnantajalta verotettavaa puhelinetua. Verohallinnon luontoisetupäätöksessä on määritelty, mitä kuluja puhelinetu kattaa. Matkapuhelimen käyttö maksuvälineenä ei sisälly puhelinetuun, vaan se verotetaan erikseen. Sen sijaan tietoliikenneyhteyden yksityiskäyttö on verotonta.

#### `optio` — Optioetu

Työsuhdeoptiot ja osakepalkkiot, josta on vähennetty työntekijän osakkeesta tai osuudesta ja työsuhdeoptiosta maksama hinta. Etua käsitellään kuin luontoisetua, ennakkopidätys lasketaan rahapalkan luontoisetujen, optioedun ja muiden veronalaisten etujen yhteismäärästä ja vähennetään rahapalkasta. Työsuhdeoptioita ovat etu työsuhteeseen perustuvasta oikeudesta saada tai hankkia yhteisön osakkeista tai osuuksia käypää hintaa alempaan hintaan vaihtovelkakirjan, optiolainan, optio-oikeuden tai muun näihin verrattavan sopimuksen tai sitoumuksen perusteella. Edun arvo on osakkeen tai osuuden käypä arvo sillä hetkellä kun työsuhdeoptiota käytetään. Edun arvosta on vähennetty hinta, jonka työntekijä yhteensä maksaa osakkeesta tai osuudesta ja työsuhdeoptiosta.

#### `tavakmak` — Kollekt. lisäeläketurvan vakuutusmaksut, työnantajan maksamat

Työnantajan maksamat kollektiivisen lisäeläketurvan vakuutusmaksut, euroa (€). Tässä on ilmoitettu työnantajan maksamat 6.5.2004 tai sen jälkeen työntekijöilleen otetun lisäeläketurvan maksut, jos työntekijä on itse maksanut maksuista osan.  Jos työnantaja on maksanut kollektiivisen lisäeläketurvan maksut kokonaan, tietoja ei ole ilmoitettu vuosi-ilmoituksella. Tässä on ilmoitettu maksut  myös silloin, kun uusi työntekijä on tullut 6.5.2004 jälkeen mukaan työnantajan ennen tuota päivää ottamaan, ns. kollektiiviseen vakuutusjärjestelmään.

#### `psvakmak` — Kollekt. lisäeläketurvan vakuutusmaksut, palkansaajan maksamat

Palkansaajan maksamat kollektiivisen lisäeläketurvan vakuutusmaksut, euroa (€). Tässä on ilmoitettu työntekijän maksama osuus 6.5.2004 tai sen jälkeen työnantajan työntekijöilleen ottaman lisäeläketurvan maksuista. Jos työnantaja on maksanut kollektiivisen lisäeläketurvan maksut kokonaan, tietoja ei ole ilmoitettu vuosi-ilmoituksella. Tässä on ilmoitettu maksut  myös silloin, kun uusi työntekijä on tullut 6.5.2004 jälkeen mukaan työnantajan ennen tuota päivää ottamaan, ns. kollektiiviseen vakuutusjärjestelmään.

#### `vayelmak` — Vapaaeht. yksilöllisen eläkevakuutuksen maksut

Vapaaehtoisen yksilöllisen eläkevakuutuksen maksut yhteensä, euroa (€). Tässä on ilmoitettu työnantajan työntekijöille ottaman vapaaehtoisen eläkevakuutuksen maksut kokonaisuudessaan. Sisältää myös sellaisen yksilöllisen eläkevakuutuksen maksut, joka on otettu avoimen yhtiön yhtiömiehelle, kommandiittiyhtiön vastuunalaiselle yhtiömiehelle tai sellaisen osakeyhtiön osakkaalle, joka ei ole TyEL-vakuutettu. Jos työnantajan työntekijälle ottaman vapaaehtoisen yksilöllisen eläkevakuutuksen maksut ylittävät 8500 euroa, ylittävältä osalta maksut ovat palkkaa ja ne on ilmoitettu kohdassa/muuttujassa Muut luontoisedut.

#### `luhlomak` — Luottamushenkilömaksu

Luottamushenkilömaksu euroa (€). Luottamushenkilömaksun on ilmoittanut vain kunta, kuntayhtymä, puolue tai puolueen paikallisosasto. Kunta tai kuntayhtymä on ilmoittanut luottamushenkilömaksun, joka on peritty kunnalliseen luottamustoimeen valitulle henkilölle maksetuista palkkiosta. Maksua ei ole ilmoitettu, jos se on peritty muusta kuin kunnallisesta luottamustoimesta, esimerkiksi osakeyhtiön tai muun yksityisoikeudellisen yhteisön hallituksen jäsenyydestä.

#### `palkeisv` — Palkka, josta ei sairausvakuutusmaksua

Palkka, josta ei makseta sairausvakuutusmaksua, euroa (€). Sairausvakuutuksen päivärahamaksu määrätään veronalaisen palkkatulon ja työtulon perusteella. Veronalaiseen tuloon voi sisältyä joitakin sellaisia eriä, jotka eivät kuulu päivärahamaksun perusteeseen. Näistä tuloista ei makseta työnantajan sairausvakuutusmaksua.

#### `tsmlietu` — Työntekijällä on työsuhdematkalippu käytössä 1=on, 0=ei

Vuosina 2006-2007.

#### `tsmlivah` — Työsuhdematkalippuetu

Työntekijän työsuhdematkalippuetu, joko kokonaan palkaksi katsottu tai työntekijältä peritty määrä, euroa (€). Jos palkansaaja ostaa matkalipun itse ja työnantaja maksaa työntekijälle matkalipun hinnan tai osan siitä, työnantajan maksama korvaus katsotaan kokonaisuudessaan työntekijän palkaksi. Tässä on ilmoitettu sekä palkkana verotettava summa, että mahdollinen palkansaajan nettopalkasta peritty korvaus.

#### `everonal` — Eläkkeen tai etuuden veronalaisen osan määrä

Eläkkeen tai etuuden veronalaisen osan määrä

#### `suoritus` — Suorituksen määrä

Suoritusten määrä tai sijoitusrahasto-osuuden määrä

#### `omistaja` — Metsänomistajaryhmä

Metsänomistajaryhmä,01 = yksittäinen metsän omistaja tai kuolinpesä, 02 = metsän yhdessä omistavat puolisot, 03 = verotusyhtymä, 04 = avoin yhtiö, kommandiittiyhtiö tai muu elinkeinoyhtymä, 05 = yhteismetsä, tiekunta, kalastuskunta tai jakokunta,09 = osakeyhtiö

#### `kauppahi` — Metsän kauppahinta

Kauppahinta ilman arvonlisäveron osuutta euroa (€)

#### `alvosuus` — Arvonlisäveron osuus myyjälle

Puun myyjälle maksettu arvonlisäveron osuus euroa (€)

#### `smak_yrtun` — Suojattu maksajan tunnus, yritystunnus

#### `smak_hnro` — Suojattu maksajan tunnus, henkilönumero

#### `smak_muutun` — Suojattu maksajan muu tunnus

#### `ssaa_hnro` — Suojattu saajan henkilönumero

#### `ssaa_yrtun` — Suojattu saajan yritystunnus

#### `ssaa_muutun` — Suojattu saajan muu tunnus

#### `srah_yrtun` — Suojattu sijoitusrahaston tunnus, yritystunnus

Vuodesta 2015 lähtien.

#### `srah_muutun` — Suojattu sijoitusrahaston tunnus, muu

Vuodesta 2015 lähtien.

#### `vuosi` — Maksuvuosi

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
