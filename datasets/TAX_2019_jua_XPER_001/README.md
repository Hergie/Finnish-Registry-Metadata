# TAX_XPER Työnantajan maksamat palkat tai muun suorituksen maksajan vuosi-ilmoitus verohallinnolle (2019)

- **Identifier:** `TAX_2019_jua_XPER_001.xml`
- **DOI:** `work_2020-03_2020-03-31_ain_0007`
- **Temporal coverage:** 2019-01-01 - 2019-12-31
- **Published:** 2021-12-21
- **Organisation:** Tilastokeskus
- **Variable count:** 25
- **Observation count:** —
- **Population:** Työnantajat
- **Source:** Verohallinnon Tilastokeskukselle toimittama tulorekisteristä muodostettu palkka-aineisto sekä vuosi-ilmoitukset eläkkeistä, metsäkaupoista ja koroista.

## Kuvaus / Description

Työnantajan tai suorituksen maksajan vuosi-ilmoitustiedot ovat saatavissa tutkimuskäyttöön suorituksittain vuosilta 1995 - 2019.

Vuoden 2019 tiedot pohjautuvat palkkojen osalta tulorekisterin pohjalta tehtyyn Verohallinnon erillistoimitukseen Tilastokeskukselle.

Työnantajan tai suorituksen maksajan on annettava Verohallinnolle vuosi-ilmoitus (lomake 7801) maksamistaan palkoista, työkorvauksista ja muista suorituksista kuten käyttökorvauksista ja palkkioista. Myös luontoiseduista, työsuhdeoptioista ja osakepalkkioista, päivärahoista, kilometrikorvauksista ja vapaaehtoisista eläkemaksuista ilmoitetaan vuosi-ilmoituksella.

XPER-tiedostoihin on yhdistetty vuosi-ilmoitustiedot myös eläkkeistä (7803), puunostajien metsäkaupoista (7807) ja TVL:n mukaisista koroista, voitto- ja rahasto-osuuksista (7805).

Vuosina 1995-1998 tiedot ovat markoissa, 1999-2001 markoissa/euroissa (rahayks) ja vuodesta 2002 lähtien euroissa.

Palkoista ja muista ansiotuloista ei enää ole annettu vuosi-ilmoitusta vuodesta 2019 lähtien, vaan palkat ja muut ansiotulot on ilmoitettu tulorekisteriin.

Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@stat.fi.

## Muuttujat / Variables (25)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `smak_yrtun` | Suojattu maksajan tunnus, yritystunnus | — | — | — |
| `smak_hnro` | Suojattu maksajan tunnus, henkilönumero | — | — | — |
| `smak_muutun` | Suojattu maksajan muu tunnus | — | — | — |
| `ssaa_hnro` | Suojattu saajan henkilönumero | — | — | — |
| `ssaa_yrtun` | Suojattu saajan yritystunnus | — | — | — |
| `ssaa_muutun` | Suojattu saajan muu tunnus | — | — | — |
| `vuosi` | Maksuvuosi | — | — | — |
| `suorlaji` | Suorituslaji (ei koske palkkoja 2019) | — | — | — |
| `ennpid` | Ennakonpidätys (ei koske palkkoja 2019) | — | — | — |
| `eivaltuve` | Ei välitetä tuloverotukseen (eläkkeet ja etuudet) | — | — | — |
| `everonal` | Eläkkeen tai etuuden veronalaisen osan määrä | — | — | — |
| `takperet` | Takaisin peritty etuus | — | — | — |
| `srah_yrtun` | Suojattu sijoitusrahaston tunnus, yritystunnus | — | — | — |
| `srah_muutun` | Suojattu sijoitusrahaston tunnus, muu | — | — | — |
| `suoritus` | Suorituksen määrä (korot ja osuudet) | — | — | — |
| `osuuslkm` | Rahasto-osuuksien lukumäärä | — | — | — |
| `ulkomvero` | Ulkomaille peritty vero (korot ja osuudet) | — | — | — |
| `maatunnus` | Maatunnus (korot ja osuudet) | — | — | — |
| `omistaja` | Metsänomistajaryhmä | — | — | — |
| `kauppahi` | Metsän kauppahinta | — | — | — |
| `alvosuus` | Arvonlisäveron osuus puun myyjälle | — | — | — |
| `Tulotyypit` | Tulotyypit (palkat) | — | — | — |
| `SuorituksenMaara` | Suorituksen määrä (palkat) | — | — | — |
| `SaajaRajoitetustiVerovelvol` | Saaja rajoitetusti verovelvollinen (palkat) | — | — | — |
| `ilmlaji` | Ilmoituslaji eläkkeet ja etuudet | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `smak_yrtun` — Suojattu maksajan tunnus, yritystunnus

Maksajan suojattu Y-tunnus

#### `smak_hnro` — Suojattu maksajan tunnus, henkilönumero

Maksajan suojattu henkilönumero

#### `smak_muutun` — Suojattu maksajan muu tunnus

#### `ssaa_hnro` — Suojattu saajan henkilönumero

Palkan- tai muun suorituksen saajan suojattu henkilönumero

#### `ssaa_yrtun` — Suojattu saajan yritystunnus

Palkan- tai muun suorituksen saajan suojattu Y-tunnus

#### `ssaa_muutun` — Suojattu saajan muu tunnus

Palkan- tai muun suorituksen saajan suojattu muu tunnus, joka voi olla puutteellinen

#### `vuosi` — Maksuvuosi

Vuosi, jolta ilmoitus on annettu

#### `suorlaji` — Suorituslaji (ei koske palkkoja 2019)

Suorituslajilla tarkoitetaan ilmoitettavan tulon laatua. Suorituslajeja ovat mm. palkka, palkkio, työkorvaus, kulu- ja käyttökorvaus tai eläke. Suorituslajien luokituksessa saattaa olla puutteita vuosittaisten muutosten vuoksi. Joitakin suorituslajeja on yhdistelty luokkiin F, L ja H4. Suorituslajien tunnukset ovat:
1 Palkka sivutoimesta
1Y Yrittäjän palkka sivutoimesta  (palkka tehtävästä, josta saaja on YEL- tai MYEL-vakuutettu)  
2 Merityötulo
2B Sijoitusrahaston tuotto
2C Joukkovelkakirjalainan korko
2D Muu korko tai pääomatulo
2E Vuosi-ilmoituksen antajan maksama jälkimarkkinahyvitys verovelvolliselle
2F Vuosi-ilmoituksen antajan perimä (saama) jälkimarkkinahyvitys
2G Sijoitusrahaston rahasto-osuus
2Y Yrittäjän merityötulo
3J Ulkomaisen yhteissijoitusyrityksen osuudelle maksettu korko
3K EU:n ulkopuolelta maksettu/välitetty korko
3L Ulkomaisen yhteissijoitusyrityksen osuus
3M Toisesta EU-jäsenvaltiosta maksettu/välitetty korko
3N Toisesta EU-jäsenvaltiosta maksettu/välitetty myynnin,
takaisinoston tai lunastuksen tuoton kokonaismäärä
5 Ns. 6 kk:n säännön alainen palkka
5Y Yrittäjän 6 kk:n säännön alainen palkka
6 Sijaismaksajan maksama palkka ja palkkaturva
61 Sijaismaksajan maksama 6 kk:n säännön alainen palkka
7K Työnantajan (kiinteä toimipaikka Suomessa) maksama palkka
työntekijälle, joka ei ole Suomessa vakuutettu
7L Ulkomaisen työnantajan (ei kiinteää toimipaikkaa Suomessa)
maksama palkka työntekijälle, joka ei ole Suomessa vakuutettu
7M Ulkomaisen työnantajan (ei kiinteää toimipaikkaa Suomessa)
maksama palkka Suomessa vakuutetulle työntekijälle
7N Ulkomaisen työnantajan (ei kiinteää toimipaikkaa Suomessa)
maksama palkka työntekijälle, kun työnantaja maksaa
työntekijän puolesta verot (nettopalkkasopimus)
7Q Ulkomaisen työnantajan (ei kiinteää toimipaikkaa Suomessa)
maksama palkka työntekijälle, joka on oleskellut Suomessa
enintään 183 päivää verosopimuksessa tarkoitettuna ajanjaksona
9A Metsänmyyntitulot pystykaupoista
9B Metsänmyyntitulot hankinta- tai käteiskaupoista
9C Puun myynnin vakuutussuoritus
A Kansaneläke
AA Takuueläke
AB Eläketuki
B Työ-, virka- ja yrittäjäeläke
B6 Eläke, joka maksettu ulkomailla asuvalle henkilölle ja josta
peritty vain sairausvakuutusmaksu
F Muut eläkkeet
F1 Ansiotulona verotettava EU-virkamiehen vapaaehtoiseen eläke-vakuutukseen
perustuva eläke, joka verotetaan 20 %:lla korotettuna
G Ansiotuloa oleva käyttökorvaus
G1 Pääomatuloa oleva käyttökorvaus, palkkasaatavan korko tms.
H Työkorvaus
H1 Henkilöstörahaston rahasto-osuus
H2 Urheilijan palkkio
H3 Perhehoitajan tai omaishoitajan palkkio
H4 Muu ansiotuloa oleva suoritus
H5 Yleishyödyllisen yhteisön maksama korvaus
H6 Sovittelijan kulukorvaus
HT Työpanokseen perustuva osinko (työkorvausta)
J Takaisin peritty suoritus, jolla ei ole omaa suorituslajia
K Vapaaehtoiseen henkilövakuutukseen perustuvat suoritukset,
mm. potilas- ja vastuuvakuutuksen ansionmenetyskorvaus
L Pakollisen tapaturma- ja liikennevakuutuksen päiväraha, vastuuvakuutuskorvaus ym. 
M Veronalainen lakkoavustus
O Yleinen perhe-eläke
P Palkka päätoimesta
P3 Kunnallisen perhepäivähoitajan palkka
PT Työpanokseen perustuva osinko (palkkaa)
PU Urheilijarahastosta maksettava palkka
PY Yrittäjän palkka päätoimesta  (palkka tehtävästä, josta saaja on YEL- tai MYEL-vakuutettu)  
Q Vapaaehtoisen yksilölliseen eläkevakuutukseen perustuva
pääomatuloa oleva vuosittain maksettava eläke
Q1 Pitkäaikaissäästämissopimukseen perustuva pääoamtuloa oleva
vuosittain maksettava suoritus
Q2 Muut pääomatulona verotettavat eläkkeet ja etuudet
Q3 Kapitalisaatiosopimuksen tuotto
R1 Reserviläispalkka
S Sairausvakuutuslain ym. nojalla maksettavat korvaukset
SA Sairauskassan täydennyspäiväraha
T Työttömyyspäiväraha ym.
U Koulutustuki, toistuva korvaus, aikuiskoulutustuki
V1 Vapaaehtoiseen yksilölliseen eläkevakuutukseen perustuva eläke,
joka verotetaan pääomatulona 20 prosentilla korotettuna
V2 Vapaaehtoiseen yksilölliseen eläkevakuutukseen perustuva eläke,
joka verotetaan pääomatulona 50 prosentilla korotettuna
V3 Pitkäaikaissäästämissopimukseen perustuva suoritus, joka
verotetaan pääomatulona 20 prosentilla korotettuna
V4 Pitkäaikaissäästämissopimukseen perustuva suoritus, joka
verotetaan pääomatulona 50 prosentilla korotettuna
W Maatalousyrittäjän luopumiskorvaus
W1 Opintoraha
X Lapsen kotihoidontuki ja osittainen hoitoraha
Y Starttiraha (yrittäjän työllistämistuki)
YT YEL/MYEL-vakuutetun yrittäjän työpanokseen perustuva osinko
(palkkaa)
Z Lakisääteisen eläkevakuutusmaksun palautus

#### `ennpid` — Ennakonpidätys (ei koske palkkoja 2019)

Maksetuista palkoista ja muista tuloista toimitetun ennakonpidätyksen määrä euroa (€). Ennakonpidätyksellä tarkoitetaan useimmiten tuloveron ennakonpidätystä, jonka työnantaja tekee työntekijän palkkatulosta ja tulouttaa verottajalle.

#### `eivaltuve` — Ei välitetä tuloverotukseen (eläkkeet ja etuudet)

0=ei (välitetään tuloverotukseen), 1= kyllä

#### `everonal` — Eläkkeen tai etuuden veronalaisen osan määrä

Eläkkeen tai etuuden veronalaisen osan määrä

#### `takperet` — Takaisin peritty etuus

Liikaa tai väärin perustein maksettuja etuuksia (esim. työttömyystuet, opintorahat yms.)

#### `srah_yrtun` — Suojattu sijoitusrahaston tunnus, yritystunnus

Suojattu sijoitusrahaston Y-tunnus

#### `srah_muutun` — Suojattu sijoitusrahaston tunnus, muu

Suojattu sijoitusrahaston muu tunnus

#### `suoritus` — Suorituksen määrä (korot ja osuudet)

Suoritusten määrä tai sijoitusrahasto-osuuden määrä

#### `osuuslkm` — Rahasto-osuuksien lukumäärä

Rahasto-osuuksien lukumäärä

#### `ulkomvero` — Ulkomaille peritty vero (korot ja osuudet)

Ulkomaille peritty vero

#### `maatunnus` — Maatunnus (korot ja osuudet)

Maatunnus, suorituslajien 5 / 5Y / 7Q osalta.  Työskentelyvaltion maatunnus suorituslaji  5 on Kuuden kuukauden säännön alainen vakuutuspalkka  tai 5Y Yrittäjän kuuden kuukauden säännön alainen vakuutuspalkka.  Jos maita on ollut useampia kuin yksi, on ilmoitettu se maa, jossa työntekijä on verovuonna työskennellyt kauimmin. Suorituslaji  7Q on  Ulkomaisen työnantajan (ei kiinteää toimipaikkaa Suomessa) maksama palkka työntekijälle, joka on oleskellut Suomessa enintään 183 päivää verosopimuksessa tarkoitettuna ajanjaksona ja  minkä maan verosopimuksen perusteella Suomella ei ollut verotusoikeutta palkkatuloon. Verosopimusmaan maatunnus on ilmoitettu aina, kun suorituslajia 7Q on käytetty.

#### `omistaja` — Metsänomistajaryhmä

Metsänomistajaryhmä:                                                    
01 = yksittäinen metsän omistaja tai kuolinpesä,
02 = metsän yhdessä omistavat puolisot,                        
03 = verotusyhtymä,
04 = avoin yhtiö, kommandiittiyhtiö tai muu elinkeinoyhtymä,
05 = yhteismetsä, tiekunta, kalastuskunta tai jakokunta,   
09 = osakeyhtiö

#### `kauppahi` — Metsän kauppahinta

Metsän kauppahinta ilman arvonlisäveron osuutta, euroa (€)

#### `alvosuus` — Arvonlisäveron osuus puun myyjälle

Puun myyjälle maksettu arvonlisäveron osuus, euroa (€).

#### `Tulotyypit` — Tulotyypit (palkat)

100 Ennakonpidätyksen alaiset palkat ja luontoisedut	
101 Työsuhdeoptiot ja osakepalkkiot	
102 Työpanokseen perustuvat osingot tai ylijäämät, työkorvaus	
103 Työpanokseen perustuvat osingot tai ylijäämät, palkka	
104 Käyttökorvaukset ansiotuloa ja palkkio työsuhdekeksinnöstä	
105 Perhehoitajan palkkiot ja kustannusten korvaukset	
106 Urheilijan palkkiot	
107 Henkilöstörahastosta nostettu rahasto-osuus ja ylijäämä veronalainen 80%	
108 Perhehoitajan kustannusten korvaukset	
110 Sovittelijan kulukorvaus	
111 Muut veronalaiset kustannuskorvaukset	
112 Muu veronalainen ennakonpidätyksen alainen ansiotulo	
113 Ulkomaisen työnantajan maksama palkka työntekijälle, nettopalkkasopimus	
114 Ulkomaisen työnantajan = jolla ei ole kiinteää toimipaikkaa Suomessa, maksama palkka työntekijälle	
115 Ennakkoperintärekisteröimättömän työkorvaukset, ALV	
116 Ennakkoperintäreisteröimättömän työkorvaukset, ei ALV	
118 Palkat ja luontoisedut merityötuloista	
120 Omaishoitajan palkkiot

#### `SuorituksenMaara` — Suorituksen määrä (palkat)

#### `SaajaRajoitetustiVerovelvol` — Saaja rajoitetusti verovelvollinen (palkat)

#### `ilmlaji` — Ilmoituslaji eläkkeet ja etuudet

Saa arvon PEB, kun vuosi-ilmoitus eläkkeistä/etuuksista

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
