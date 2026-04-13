# FLEED Yhdistetty työntekijä-työnantaja-aineisto, kokonaisiaineisto, työttömyysjaksot

- **Identifier:** `YA244_19912016_jua_totaltyottomat_001.xml`
- **DOI:** `tyokay_2012-03_2012-03-01_ain_0001`
- **Temporal coverage:** 2005-01-01 - 2016-12-31
- **Published:** 2019-01-17
- **Organisation:** Tilastokeskus
- **Variable count:** 6
- **Observation count:** —
- **Population:** Työikäinen väestö
- **Source:** Työ- ja elinkeinoministeriön työnhakijarekisteri
- **Keywords:** työttömyys

## Kuvaus / Description

<b>FLEED-aineiston päivitykset päättyvät</b>

Tilastokeskuksen tutkijapalveluiden FOLK-moduulien käyttöönoton myötä FLEED-aineistokokonaisuuden päivitykset päättyvät. FLEED-aineistoon on päivitetty tilastovuoden 2016 tiedot. FLEED-jaksotiedot (eläke-, työsuhde-, työttömyys-, työnhaku-, työvoimakoulutus- ja toimenpidesijoitusjaksot) muuttuvat vastaaviksi FOLK-moduuleiksi. Hankkeissa, joiden käyttölupa FLEED-aineistoon jatkuu päivitysten päättymisen jälkeen, on mahdollista saada käyttöön vastaavat tiedot FOLK-moduuleista. FOLK-moduulien kuvaukset löytyvät TAIKA-tutkimusaineistokatalogista. Tutkijapalvelut on ollut yhteydessä nykyisiin FLEED-valmisaineiston käyttäjiin mahdollisesta käyttöluvan päivittämisestä ja siirtymisestä FOLK-aineiston käyttöön.

<b>FLEED-työttömyysjaksot</b> 
Tietoja vuodesta 1991 alkaen.

## Muuttujat / Variables (6)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `vuosi` | Tilastovuosi | — | vuosi_1_2011_07_01 | — |
| `alkupvm` | Työttömyyden alkupäivämäärä | — | — | Työnhakijarekisteri |
| `loppupvm` | Työttömyyden loppupäivämäärä | — | — | Työnhakijarekisteri |
| `psyy` | Työttömyyden päättymissyy | — | tyottomy_3_1987_01_01 | Työnhakijarekisteri |
| `tjtyol` | Työttömyysjakson työllisyyskoodi | — | — | Työnhakijarekisteri |
| `shnro` | Suojattu Tilastokeskuksen henkilönumero | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `vuosi` — Tilastovuosi

**Luokitus / Classification:** vuosi_1_2011_07_01

Tilastovuosi on se kalenterivuosi, jota tilasto koskee.

#### `alkupvm` — Työttömyyden alkupäivämäärä

**Ryhmä / Group:** Työnhakijarekisteri

Työttömyysjakson alkupäivämäärä.

#### `loppupvm` — Työttömyyden loppupäivämäärä

**Ryhmä / Group:** Työnhakijarekisteri

Työttömyysjakson loppupäivämäärä.

#### `psyy` — Työttömyyden päättymissyy

**Luokitus / Classification:** tyottomy_3_1987_01_01 · **Ryhmä / Group:** Työnhakijarekisteri

Työllisyyskoodin muutoksen syy.
0 = Sijoitettu työllistämistoimenpitein
1 = Välitetty työhön yleisille työmarkkinoille
2 = Lomautus tai lyh. työviikko päättynyt
3 = Saanut itse työpaikan
4 = Aloittanut työvoimakoulutuksen
5 = Siirtynyt työvoiman ulkopuolelle
6 = Muu syy tai ei tietoa
7 = Siirtynyt työttömyyseläkkeelle
8 = Aloittanut muun koulutuksen
9 = Siirtynyt työnhakuun ETA-valtioon

Uusi luokitus tilastovuodesta 2012 alkaen:

00	Työllistetty (entinen nimi: sijoitettu toimenpitein)
01	Välitetty työhön yleisille työmarkkinoille
02	Lomautus tai lyh. työviikko päättynyt
03	Saanut itse työpaikan
04	Aloittanut työvoimakoulutuksen
05	Siirtynyt työvoiman ulkopuolelle (nykyisin merkitään soveltuvin osin syillä 11, 12 ja 13)
06	Muu syy tai ei tietoa
07	Siirtynyt työttömyyseläkkeelle
08	Aloittanut muun koulutuksen
09	Työhön/työnhakuun EU-/ETA-valtioon
10	Ei ole uusinut työnhakuaan (tuli ennen korvertoituna ’6’:ksi)
11	Aloittanut valmennuksen/kokeilun
12	Aloittanut kuntouttavan työtoiminnan
13	Aloittanut omaehtoisen opiskelun työttömyysetuudella

#### `tjtyol` — Työttömyysjakson työllisyyskoodi

**Ryhmä / Group:** Työnhakijarekisteri

Työttömyysjakson työllisyyskoodi.
2 = työtön
3 = lomautettu

#### `shnro` — Suojattu Tilastokeskuksen henkilönumero

Suojattu Tilastokeskuksen henkilönumero.

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
