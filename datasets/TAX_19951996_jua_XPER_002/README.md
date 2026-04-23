# TAX_XPER Työnantajan tai suorituksen maksajan vuosi-ilmoitus verohallinnolle (1995-1996)

- **Identifier:** `TAX_19951996_jua_XPER_002.xml`
- **DOI:** `work_2020-03_2020-03-31_ain_0004`
- **Temporal coverage:** 2000-01-01 - 2001-12-31
- **Published:** 2021-03-05
- **Organisation:** Tilastokeskus
- **Variable count:** 31
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

## Variables (31)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `smak_yrtun` | Suojattu maksajan tunnus, yritystunnus | — | — | — |
| `smak_hnro` | Suojattu maksajan tunnus, henkilönumero | — | — | — |
| `smak_muutun` | Suojattu maksajan muu tunnus | — | — | — |
| `ssaa_hnro` | Suojattu saajan henkilönumero | — | — | — |
| `ssaa_yrtun` | Suojattu saajan yritystunnus | — | — | — |
| `ssaa_muutun` | Suojattu saajan muu tunnus | — | — | — |
| `LAANI` | Ajoläänin tunnus | — | — | — |
| `SUORLAJI` | Suorituslaji | — | — | — |
| `SUORITUS` | Suorituksen markkamäärä | — | — | — |
| `VITAPLAJ` | Rivin tapahtumalaji | — | — | — |
| `ENNPIDAT` | Suorituksen ennakonpidätyksen määrä | — | — | — |
| `TYLUONET` | Luontoisedun määrä | — | — | — |
| `SUORVVAP` | Eläkkeen tai etuuden verovapaa osa | — | — | — |
| `VILAKMAK` | Eläke- ja työttömyysvakuutusmaksu | — | — | — |
| `ELLISAOS` | Kansaneläkkeen tai perhe-eläkkeen lisäosan ilmaisin | — | — | — |
| `PUUMYYJA` | Puun myyjä | — | — | — |
| `ENNPIDKK` | Ennakonpidätys | — | — | — |
| `VVAKMAK1` | TA:n maks ve evakmaks kun perturva ei ylity | — | — | — |
| `VVAKMAK2` | TA:n maks ve evakmaks kun perturva ylittyy | — | — | — |
| `VVAKMAK3` | TA:n maks ve ennen 1.10.1992 otet evakma | — | — | — |
| `VVAKMAK4` | TA:n maks ve evakmaks, väh.oik.ei selvitystä | — | — | — |
| `ARVONLVE` | — | — | — | — |
| `KORKOETU` | Asuntolainan korkoetu | — | — | — |
| `ELAKTLAJ` | Takautuvasti maksetun eläkkeen laji | — | — | — |
| `VIALKPVM` | Tulon kertym tai pal el vak maks alkupvm | — | — | — |
| `VILOPPVM` | Tulon kertym tai pal el vak maks loppupv | — | — | — |
| `VMAKSUVV` | Maksuvuodelle kohdistuva osa eläkkeestä | — | — | — |
| `VMAKSVV1` | Maksuvuosi-1:lle kohdistuva osa eläkkeestä | — | — | — |
| `VMAKSVV2` | Maksuvuosi-2:lle kohdistuva osa eläkkeestä | — | — | — |
| `ELALKAMI` | — | — | — | — |
| `VUOSI` | — | — | — | — |

### Variable definitions

#### `smak_yrtun` — Suojattu maksajan tunnus, yritystunnus

#### `smak_hnro` — Suojattu maksajan tunnus, henkilönumero

#### `smak_muutun` — Suojattu maksajan muu tunnus

#### `ssaa_hnro` — Suojattu saajan henkilönumero

#### `ssaa_yrtun` — Suojattu saajan yritystunnus

#### `ssaa_muutun` — Suojattu saajan muu tunnus

#### `LAANI` — Ajoläänin tunnus

#### `SUORLAJI` — Suorituslaji

Suorituslajilla tarkoitetaan ilmoitettavan tulon laatua. Suorituslajeja ovat mm. palkka, palkkio, työkorvaus, kulu- ja käyttökorvaus tai eläke. Suorituslajit ovat puutteelliset vuosille 1995-1996 ja muuttuja sisältää myös puuttuvia. Joitakin suorituslajeja on yhdistelty luokkiin F, L ja H4. Suorituslajien tunnuksia perustuen myöhempiin vuosiin:
1	Palkka sivutoimesta	
2	Merityötulo
5	Ns. 6 kk:n säännön alainen palkka	
6	Sijaismaksajan maksama palkka
9A	Pystykauppa	
9B	Hankintakauppa	
9C	Puun myynnin vakuutussuoritus	
A	Kansaneläke	
B	Työ-, virka- ja yrittäjäeläke	
F	Muut eläkkeet	
G	Käyttökorvaus	
G1	Pääomatulot	
H	Työkorvaus
H4	 Muu ansiotuloa oleva suoritus
K	Vapaaehtoiseen henkilövakuutukseen perustuvat suoritukset ym.	
L	Pakoll. tapaturma- ja liikennevak. päiväraha, vastuuvakuutuskorvaus ym.	
M	Veronalainen lakkoavustus	
O	Yleinen perhe-eläke	
P	Palkka päätoimesta	
Q	Vapaaehtoisen henkivakuutuksen suoritukset ym.	
S	Sairausvakuutuslain ym. nojalla maksettavat korvaukset	
T	Työttömyyspäiväraha ym.	
U	Koulutustuki, toistuva korvaus, aikuiskoulutustuki	
V	Tuesta tai päivärahasta peritty eläkemaksu	
W	Maatalousyrittäjän luopumiskorvaus	
X	Lapsen kotihoidontuki ja osittainen hoitoraha
Z	Eläkevakuutusmaksun palautus

#### `SUORITUS` — Suorituksen markkamäärä

#### `VITAPLAJ` — Rivin tapahtumalaji

#### `ENNPIDAT` — Suorituksen ennakonpidätyksen määrä

#### `TYLUONET` — Luontoisedun määrä

#### `SUORVVAP` — Eläkkeen tai etuuden verovapaa osa

#### `VILAKMAK` — Eläke- ja työttömyysvakuutusmaksu

#### `ELLISAOS` — Kansaneläkkeen tai perhe-eläkkeen lisäosan ilmaisin

#### `PUUMYYJA` — Puun myyjä

#### `ENNPIDKK` — Ennakonpidätys

Ei saatavissa 1995

#### `VVAKMAK1` — TA:n maks ve evakmaks kun perturva ei ylity

Työnantajan maksaman vapaaehtoisen eläkevakuutuksen maksut vakuutuksesta, joissa peruseläketurva ei ylity

#### `VVAKMAK2` — TA:n maks ve evakmaks kun perturva ylittyy

Työnantajan maksaman vapaaehtoisen eläkevakuutuksen maksut vakuutuksesta, joissa peruseläketurva ylittyy

#### `VVAKMAK3` — TA:n maks ve ennen 1.10.1992 otet evakma

Työnantajan maksamat vapaaehtoisen eläkevakuutuksen maksut vakuutuksesta, joka otettu ennen 1.10.1992

#### `VVAKMAK4` — TA:n maks ve evakmaks, väh.oik.ei selvitystä

Työnantajan maksaman vapaaehtoisen eläkevakuutuksen maksut vakuutuksesta, jonka vähennysoikeudesta ei ole selvitystä.

#### `ARVONLVE`

Ei saatavissa 1995

#### `KORKOETU` — Asuntolainan korkoetu

Ei saatavissa 1995

#### `ELAKTLAJ` — Takautuvasti maksetun eläkkeen laji

#### `VIALKPVM` — Tulon kertym tai pal el vak maks alkupvm

#### `VILOPPVM` — Tulon kertym tai pal el vak maks loppupv

#### `VMAKSUVV` — Maksuvuodelle kohdistuva osa eläkkeestä

#### `VMAKSVV1` — Maksuvuosi-1:lle kohdistuva osa eläkkeestä

#### `VMAKSVV2` — Maksuvuosi-2:lle kohdistuva osa eläkkeestä

#### `ELALKAMI`

#### `VUOSI`

---

[← Back to catalogue](../../README.md)
