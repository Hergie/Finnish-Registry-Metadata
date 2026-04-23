# TAX_XPER Työnantajan tai suorituksen maksajan vuosi-ilmoitus verohallinnolle (2004-2005)

- **Identifier:** `TAX_20042005_jua_XPER_002.xml`
- **DOI:** `work_2020-03_2020-03-31_ain_0006`
- **Temporal coverage:** 2004-01-01 - 2005-12-31
- **Published:** 2022-01-10
- **Organisation:** Tilastokeskus
- **Variable count:** 43
- **Observation count:** —
- **Population:** Työnantajat
- **Source:** Verohallinnon Tilastokeskukselle tilastotarkoituksiin toimittama vuosi-ilmoitusaineisto

## Description

Työnantajan tai suorituksen maksajan vuosi-ilmoitustiedot ovat saatavissa tutkimuskäyttöön suorituksittain vuosilta 1995 - 2019.

Työnantajan tai suorituksen maksajan on annettava Verohallinnolle vuosi-ilmoitus (lomake 7801) maksamistaan palkoista, työkorvauksista ja muista suorituksista kuten käyttökorvauksista ja palkkioista. Myös luontoiseduista, työsuhdeoptioista ja osakepalkkioista, päivärahoista, kilometrikorvauksista ja vapaaehtoisista eläkemaksuista ilmoitetaan vuosi-ilmoituksella.

XPER-tiedostoihin on yhdistetty vuosi-ilmoitustiedot myös eläkkeistä (7803), puunostajien metsäkaupoista (7807) ja TVL:n mukaisista koroista, voitto- ja rahasto-osuuksista (7805).

Vuosina 1995-1998 tiedot ovat markoissa, 1999-2001 markoissa/euroissa (rahayks) ja vuodesta 2002 lähtien euroissa.

Palkoista ja muista ansiotuloista ei enää ole annettu vuosi-ilmoitusta vuodesta 2019 lähtien, vaan palkat ja muut ansiotulot on ilmoitettu tulorekisteriin.

Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@stat.fi.

## Variables (43)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `vuosi` | Maksuvuosi | — | — | — |
| `SUORLAJI` | Suorituslaji | — | — | — |
| `PALKKAMK` | Palkka | — | — | — |
| `ENNPIDMK` | Ennakonpidätys | — | — | — |
| `LAKISMAK` | Eläke- ja työttömyysvakuutusmaksut | — | — | — |
| `VAHENNPI` | Vähennys ennen ennakonpidätystä | — | — | — |
| `AUTOLISM` | Verotettavan autoedun määrä | — | — | — |
| `AUTOKORV` | Työnantajan perimä korvaus autoedusta | — | — | — |
| `AUTOKAUT` | Auton käyttöetu | — | — | — |
| `AUTOVAPA` | Vapaa autoetu | — | — | — |
| `KORKOETU` | Asuntolainan korkoetu | — | — | — |
| `MUULISMK` | Muut luontoisedut, palkkaan lis. | — | — | — |
| `MUUKORVA` | Muut luontoisedut, työnant. perimä korvaus | — | — | — |
| `ASUNTOET` | Asuntoetu | — | — | — |
| `RAVINTOE` | Ravintoetu | — | — | — |
| `MUUETU` | Muu etu | — | — | — |
| `RAVINTVA` | Ravintoedun korvaus vastaa verotusarvoa | — | — | — |
| `PAIVARAH` | Päivärahat yhteensä | — | — | — |
| `KOKOPVRA` | Kokopäiväraha | — | — | — |
| `OSAPVRAH` | Osapäiväraha | — | — | — |
| `ULKOMPVR` | Ulkomaanpäiväraha | — | — | — |
| `ATERIAKO` | Ateriakorvaus | — | — | — |
| `KILOMETR` | Kilometrikorvaus, km | — | — | — |
| `KILOMEMK` | Kilometrikorvaus | — | — | — |
| `MUUKORVM` | Muut maksetut korvaukset | — | — | — |
| `ETURVAEI` | Vapaaeht.eläkevak.maksu, perusel.turva ei ylity | — | — | — |
| `ETURVAYL` | Vapaaeht.eläkevak.maksu, perusel.turva ylittyy | — | — | — |
| `VAKEISEL` | Vapaaeht.eläkevak.maksu, väh.oik.ei selvitystä | — | — | — |
| `VAK92MK` | Vapaaeht.eläkevak.maksu, otettu ennen 1992 | — | — | — |
| `VAKMAKSU` | Vapaaeht. yksilöllisen eläkevakuutuksen maksut | — | — | — |
| `VERONALS` | Eläkkeen tai etuuden veronalaisen osan määrä | — | — | — |
| `OMISTAJA` | Metsänomistajaryhmä | — | — | — |
| `KAUPPAHI` | Metsän kauppahinta | — | — | — |
| `ALVOSUUS` | Arvonlisäveron osuus myyjälle | — | — | — |
| `SUORMK` | Suorituksen määrä | — | — | — |
| `PUHELINE` | Puhelinetu | — | — | — |
| `OPTIOETU` | Optioetu | — | — | — |
| `smak_yrtun` | Suojattu maksajan tunnus, yritystunnus | — | — | — |
| `smak_hnro` | Suojattu maksajan tunnus, henkilönumero | — | — | — |
| `smak_muutun` | Suojattu maksajan muu tunnus | — | — | — |
| `ssaa_hnro` | Suojattu saajan henkilönumero | — | — | — |
| `ssaa_yrtun` | Suojattu saajan yritystunnus | — | — | — |
| `ssaa_muutun` | Suojattu saajan muu tunnus | — | — | — |

### Variable definitions

#### `vuosi` — Maksuvuosi

Vuosi, jolta ilmoitus on annettu

#### `SUORLAJI` — Suorituslaji

Suorituslajilla tarkoitetaan ilmoitettavan tulon laatua. Suorituslajeja ovat mm. palkka, palkkio, työkorvaus, kulu- ja käyttökorvaus tai eläke. Suorituslajien luokituksessa saattaa olla puutteita vuosittaisten muutosten vuoksi. Joitakin suorituslajeja on yhdistelty luokkiin F, L ja H4. Suorituslajien tunnukset ovat:
1 Palkka sivutoimesta
1Y Yrittäjän palkka sivutoimesta (palkka tehtävästä, josta saaja on YEL- tai MYEL-vakuuutettu)
2 Merityötulo
2B Sijoitusrahaston voitto-osuus
2C Joukkovelkakirjalainan korko
2D Muu korko
2E Vuosi-ilmoituksen antajan maksama jälkimarkkinahyvitys
2F Vuosi-ilmoituksen antajan saama jälkimarkkinahyvitys
2G Sijoitusrahaston rahasto-osuus
2M Merityötulo, joka kuuluu matkustaja-alusten maksuvapautuksen piiriin (2005-2007)
2Y Yrittäjän merityötulo
3J Ulkomaisen yhteissijoitusyrityksen osuudelle maksettu korko
3K Ulkomailta maksettu/välitetty korko
3L Ulkomaisen yhteissijoitusyrityksen osuus
5 Ns. 6 kk:n säännön alainen palkka
5Y Yrittäjän 6 kk:n säännön alainen palkka
6 Sijaismaksajan maksama palkka
61 Sijaismaksajan maksama 6 kk:n säännön alainen palkka
9A Pystykauppa
9B Hankintakauppa
9C Puun myynnin vakuutussuoritus
A Kansaneläke
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
J Takaisin peritty suoritus, jolla ei ole omaa suorituslajia
K Vapaaehtoiseen henkilövakuutukseen perustuvat suoritukset, mm. potilas ja
vastuuvakuutuksen ansionmenetyskorvaus
L Pakoll. tapaturma- ja liikennevak. päiväraha, vastuuvakuutuskorvaus ym.
M Veronalainen lakkoavustus (alkaen 2005)
O Yleinen perhe-eläke
P Palkka päätoimesta
P2 Urheilijan palkka
P3 Kunnallisen perhepäivähoitajan palkka (alkaen 2005)
PY Yrittäjän palkka päätoimesta (palkka tehtävästä, josta saaja on YEL- tai MYEL-vakuuutettu)
Q Vapaaehtoisen henkivakuutuksen suoritukset ym.
R1 Reserviläispalkka
S Sairausvakuutuslain ym. nojalla maksettavat korvaukset
T Työttömyyspäiväraha ym.
U Koulutustuki, toistuva korvaus, aikuiskoulutustuki
V Tuesta tai päivärahasta peritty eläkemaksu
W Maatalousyrittäjän luopumiskorvaus
W1 Opintoraha
X Lapsen kotihoidontuki ja osittainen hoitoraha
Y Starttiraha (yrittäjän työllistämistuki)
Z Eläkevakuutusmaksun palautus

#### `PALKKAMK` — Palkka

Maksetut ennakonpidätyksen alaiset palkat ilman luontoisetuja, euroa (€). Palkalla tarkoitetaan mitä tahansa palkkaa, palkkiota ja korvausta, joka saadaan työ- tai virkasuhteessa, sekä kokouspalkkiota, henkilökohtaista luento- ja esitelmäpalkkiota, hallintoelimen jäsenyydestä saatua palkkiota, toimitusjohtajan palkkiota, avoimen yhtiön ja kommandiittiyhtiön yhtiömiehen nostamaa palkkaa sekä luottamustoimesta saatua korvausta. Palkkaa ovat myös asunto-, ravinto- ym. luontoisedut sekä veronalaiset henkilökuntaedut ja veronalaiset kustannusten korvaukset.

#### `ENNPIDMK` — Ennakonpidätys

Maksetuista palkoista toimitetun ennakonpidätyksen määrä, euroa (€). Ennakonpidätyksellä tarkoitetaan useimmiten tuloveron ennakonpidätystä, jonka työnantaja tekee työntekijän palkkatulosta ja tulouttaa verottajalle.

#### `LAKISMAK` — Eläke- ja työttömyysvakuutusmaksut

Eläke- ja työttömyysvakuutusmaksut yhteensä, euroa (€). Palkoista maksetut  ja työnantajan eläkeyhtiöille ilmoittamat työttömyysvakuutusmaksut ja työeläkemaksut yhteensä.

#### `VAHENNPI` — Vähennys ennen ennakonpidätystä

Vähennys, joka on tehty palkasta ennen ennakonpidätyksen toimittamista, euroa (€). Työnantaja voi vähentää ennen ennakonpidätyksen toimittamista palkansaajan itsensä maksamat työn tekemisestä aiheutuneet välittömät kustannukset. Tällaisia kustannuksia ovat mm. palkansaajan maksamat kustannukset moottorisahan käytöstä ja muut työvälineistä aiheutuneet kustannukset tai menot työmatkoista, jos työnantaja ei maksa niistä verovapaita korvauksia palkan lisäksi.

#### `AUTOLISM` — Verotettavan autoedun määrä

Auton verotusarvon ja työntekijältä perityn määrän erotus, euroa (€). Autoedun määrää ei ole ilmoitettu jos työnantaja perii työntekijältä autoedusta vähintään edun verotusarvon mukaisen määrän. Verotettava autoetu on ilmoitettu myös silloin kun työntekijällä on pelkkä autoetu eikä rahapalkkaa ole maksettu lainkaan.

#### `AUTOKORV` — Työnantajan perimä korvaus autoedusta

Työnanantajan työntekijältä perimä korvaus autoedusta, euroa (€). Korvaus autoedusta on ilmoiettu vaikka työnantaja perisi autoedusta vähintään autoedun raha-arvoa vastaavan tai suuremman korvauksen.

#### `AUTOKAUT` — Auton käyttöetu

Työntekijällä on auton käyttöetu, 1=kyllä, 0=ei. Auton käyttöedussa työntekijä vastaa itse ainakin auton polttoainekuluista. Käyttöedussa työntekijälle maksetaan korvausta työajoista auton polttoainekuluista laadittua matkalaskua vastaan.

#### `AUTOVAPA` — Vapaa autoetu

Työntekijällä on vapaa autoetu, 1=kyllä, 0=ei. Työnantaja maksaa kaikki autosta aiheutuneet kustannukset myös yksityisajojen osalta.

#### `KORKOETU` — Asuntolainan korkoetu

Asuntolainan korkoedun määrä, euroa (€). Työsuhteen perusteella annetusta asuntolainasta työntekijälle syntyvä korkoetu. Työntekijälle syntyy korkoetu, jos työnantaja perii työntekijälle myöntämästään lainasta vuotuista korkoa, joka on alempi kuin viitekorko, silloin kun lainan korko on sidottu yleisesti markkinoilla käytössä olevaan lainan viitekorkoon. Jos lainan korkoa ei ole sidottu viitekorkoon, työntekijälle syntyy korkoetu, silloin kun lainasta peritty vuotuinen korko on alempi kuin 12 kuukauden euribor-korko vuoden ensimmäisenä päivänä.

#### `MUULISMK` — Muut luontoisedut, palkkaan lis.

Muut luontoisedut, palkkaan lisätty määrä. Luontoisetujen verotusarvojen ja työntekijältä perittyjen korvausten erotus, euroa (€). Luontoisetuja ovat työnantajan muuna kuin rahana antamat edut, mm. asunto-, puhelin- ja ravintoetu. Muita etuja ovat myös mm. autotalli- ja vene-etu, palkaksi katsotut henki- ja eläkevakuutusmaksut, yksilöimättömästä lahjakortista syntyvä etu, merimiespalveluksessa olevan henkilön merimiehenä saama luontoisetu ja henkilöstöannista syntyvät edut.  Jos verotusarvoa ei ole erikseen vahvistettu Verohallinnon antamassa päätöksessä, luontoisedun arvo on sen käypä arvo. Luontoisetujen määrä on ilmoitettu, vaikka työntekijälle ei maksettaisi lainkaan rahapalkkaa tai rahapalkka ei riittäisi ennakonpidätyksen täysimääräiseen toimittamiseen.

#### `MUUKORVA` — Muut luontoisedut, työnant. perimä korvaus

Muut luontoisedut; työnantajan perimä korvaus on summa, joka työntekijältä on peritty muista luontoiseduista kuin autoedusta tai työsuhdematkalippuedusta, euroa (€).

#### `ASUNTOET` — Asuntoetu

Työntekijällä on luontoisetuna asuntoetu, 1=kyllä, 0=ei. Kun työntekijä on saanut asunnon käytettäväksesi työ- tai virkasuhteen perusteella tai asunto kuuluu palkkaan, tämä on verotettavaa asuntoetua. Asunnon arvoon vaikuttavat asunnon ikä, perusparannukset sekä pinta-ala.

#### `RAVINTOE` — Ravintoetu

Työntekijällä on luontoisetuna ravintoetu, 1=kyllä, 0=ei. Ravintoedun arvo määräytyy sen mukaan, onko kyseessä tavanomainen työpaikkaruokailu, laitosruokailu, ruokailun valvonnan yhteydessä saatu etu, hotelli-, ravintola- tai lentohenkilöstön, lounasseteli tai muu vastaava ravintoetu.

#### `MUUETU` — Muu etu

Työntekijällä on luontoisetuna muu etu, 1=kyllä, 0=ei. Tällaisia etuja ovat esimerkiksi kodinhoitoetu, vene-etu ja palkkiomatka. Jos työsuhde-edun arvoa ei ole määritelty Verohallinnon päätöksessä, edun arvona pidetään käypää arvoa.

#### `RAVINTVA` — Ravintoedun korvaus vastaa verotusarvoa

Työntekijältä ravintoedusta peritty korvaus vastaa verohallinnon antaman luontoisetupäätöksen mukaista ravintoedunarvoa, 1=kyllä, 0=ei

#### `PAIVARAH` — Päivärahat yhteensä

Verovapaiden päivärahojen ja ateriakorvausten yhteismäärä euroa (€). Myös seuraavat ulkomaantyöskentelyyn liittyvät verovapaat edut, verovelvollisen ja hänen perheenjäsenensä muutto- ja matkakustannukset työntekovaltioon ja takaisin, työnantajan kustantama lasten perus- ja lukiotason koulutus, työnantajan ulkomailla kustantama tavanomainen yksityinen palveluhenkilöstö.

#### `KOKOPVRA` — Kokopäiväraha

Työnantaja on maksanut kokopäivärahaa tai ateriaedun sisältävää puolitettua kokopäivärahaa, 1=kyllä, 0=ei

#### `OSAPVRAH` — Osapäiväraha

Työnantaja on maksanut puolitettua päivärahaa, 1=kyllä, 0=ei

#### `ULKOMPVR` — Ulkomaanpäiväraha

Työnantaja on maksanut ulkomaanpäivärahaa tai ateriaetua sisältävää puolitettua ulkomaanpäivärahaa, 1=kyllä, 0=ei

#### `ATERIAKO` — Ateriakorvaus

Työnantaja on maksanut ateriakorvausta sisältävää puolitettua osapäivärahaa, 1=kyllä, 0=ei

#### `KILOMETR` — Kilometrikorvaus, km

Kilometrikorvauksen perusteena oleva kilometrimäärä, km (kilometrit)

#### `KILOMEMK` — Kilometrikorvaus

Verovapaiden kilometrikorvausten yhteismäärä, pl. muut matkakorvaukset, yhteensä euroa (€).

#### `MUUKORVM` — Muut maksetut korvaukset

Muut maksetut korvaukset, esim. työpuku, -väline, tms, euroa (€).

#### `ETURVAEI` — Vapaaeht.eläkevak.maksu, perusel.turva ei ylity

Vapaaehtoisen eläkevakuutuken maksut vakuutuksesta, joissa peruseläketurva ei ylity, euroa (€). Aineistossa 2004 asti.

#### `ETURVAYL` — Vapaaeht.eläkevak.maksu, perusel.turva ylittyy

Vapaaehtoisen eläkevakuutuksen maksut vakuutuksesta, joissa peruseläketurva ylittyy, euroa (€). Aineistossa 2004 asti.

#### `VAKEISEL` — Vapaaeht.eläkevak.maksu, väh.oik.ei selvitystä

Vapaaehtoisen eläkevakuutuksen maksut vakuutuksesta, jonka vähennysoikeudesta ei ole selvitystä, euroa (€). Aineistossa 2004 asti.

#### `VAK92MK` — Vapaaeht.eläkevak.maksu, otettu ennen 1992

Vapaaehtoisen eläkevakuutuksen maksut vakuutuksesta, joka on otettu ennen 1.10.1992, euroa (€). Aineistossa 2004 asti.

#### `VAKMAKSU` — Vapaaeht. yksilöllisen eläkevakuutuksen maksut

Vapaaehtoisen yksilöllisen eläkevakuutuksen maksut yhteensä, euroa (€). Tässä on ilmoitettu työnantajan työntekijöille ottaman vapaaehtoisen eläkevakuutuksen maksut kokonaisuudessaan. Sisältää myös sellaisen yksilöllisen eläkevakuutuksen maksut, joka on otettu avoimen yhtiön yhtiömiehelle, kommandiittiyhtiön vastuunalaiselle yhtiömiehelle tai sellaisen osakeyhtiön osakkaalle, joka ei ole TyEL-vakuutettu.Aineistossa 2004 asti.

#### `VERONALS` — Eläkkeen tai etuuden veronalaisen osan määrä

Eläkkeen tai etuuden veronalaisen osan määrä, euroa (€)

#### `OMISTAJA` — Metsänomistajaryhmä

Metsänomistajaryhmä,01 = yksittäinen metsän omistaja tai kuolinpesä, 02 = metsän yhdessä omistavat puolisot, 03 = verotusyhtymä, 04 = avoin yhtiö, kommandiittiyhtiö tai muu elinkeinoyhtymä, 05 = yhteismetsä, tiekunta, kalastuskunta tai jakokunta,09 = osakeyhtiö

#### `KAUPPAHI` — Metsän kauppahinta

Kauppahinta ilman arvonlisäveron osuutta, euroa (€)

#### `ALVOSUUS` — Arvonlisäveron osuus myyjälle

Puun myyjälle maksettu arvonlisäveron osuus, euroa (€),

#### `SUORMK` — Suorituksen määrä

Suoritusten määrä tai sijoitusrahasto-osuuden määrä, euroa (€).

#### `PUHELINE` — Puhelinetu

Työntekijällä on luontoisetuna puhelinetu, 1=kyllä, 0=ei. Jos työntekijä soittaa puhelimella vapaa-aikana yksityispuheluja ja työnantaja maksaa myös ne, saat työnantajalta verotettavaa puhelinetua. Verohallinnon luontoisetupäätöksessä on määritelty, mitä kuluja puhelinetu kattaa. Matkapuhelimen käyttö maksuvälineenä ei sisälly puhelinetuun, vaan se verotetaan erikseen. Sen sijaan tietoliikenneyhteyden yksityiskäyttö on verotonta.

#### `OPTIOETU` — Optioetu

Työsuhdeoptiot ja osakepalkkiot, josta on vähennetty työntekijän osakkeesta tai osuudesta ja työsuhdeoptiosta maksama hinta, euroa (€). Etua käsitellään kuin luontoisetua, ennakkopidätys lasketaan rahapalkan luontoisetujen, optioedun ja muiden veronalaisten etujen yhteismäärästä ja vähennetään rahapalkasta. Työsuhdeoptioita ovat etu työsuhteeseen perustuvasta oikeudesta saada tai hankkia yhteisön osakkeista tai osuuksia käypää hintaa alempaan hintaan vaihtovelkakirjan, optiolainan, optio-oikeuden tai muun näihin verrattavan sopimuksen tai sitoumuksen perusteella. Edun arvo on osakkeen tai osuuden käypä arvo sillä hetkellä kun työsuhdeoptiota käytetään. Edun arvosta on vähennetty hinta, jonka työntekijä yhteensä maksaa osakkeesta tai osuudesta ja työsuhdeoptiosta.

#### `smak_yrtun` — Suojattu maksajan tunnus, yritystunnus

#### `smak_hnro` — Suojattu maksajan tunnus, henkilönumero

#### `smak_muutun` — Suojattu maksajan muu tunnus

#### `ssaa_hnro` — Suojattu saajan henkilönumero

#### `ssaa_yrtun` — Suojattu saajan yritystunnus

#### `ssaa_muutun` — Suojattu saajan muu tunnus

---

[← Back to catalogue](../../README.md)
