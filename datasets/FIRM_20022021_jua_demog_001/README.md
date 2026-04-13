# Yritysten demografiatiedot

- **Identifier:** `FIRM_20022021_jua_demog_001.xml`
- **DOI:** `yty_201300_vaa_demografia_001`
- **Temporal coverage:** 2002-01-01 - 2021-12-31
- **Published:** 2023-09-11
- **Organisation:** Tilastokeskus
- **Variable count:** 13
- **Observation count:** —
- **Population:** YTY-tuotantokannan yrityksiä
- **Source:** Tilastokeskuksen YTY-tietokannat
- **Keywords:** Yritykset

## Kuvaus / Description

Yritystietovaraston (YTY) demografia-taulun tiedot on suojattu tutkimuskäyttöön. Aineisto sisältää yritysten demografiatietoja vuosilta 2002-2021. Vanhempien vuosien tiedot on konvertoitu vanhasta yritysrekisterijärjestelmästä (-2012 asti). Laatu paranee tietojärjestelmäuudistuksen myötä vuodesta 2013 lähtien. Tiedot voivat päivittyä myös takautuvasti tietojen vuosipäivityksen yhteydessä. 

Aloitusten ja lopetusten aitouksia tarkistava prosessi käy karkeaa päättelyä soveltaen läpi kaikki yritystietovaraston yksiköt. Myös julkisen sektorin yksiköt ovat mukana. Automaattisen tarkistuksen lisäksi noin 100 aloitusta ja lopetusta yhteensä on tarkistettu vuosittain käsin. Viime vuosina noin yli 20 henkilön aloitukset on tarkistettu käsin. Tarvittaessa tarkistuksessa käytetään hallinnollisia lähteitä apuna, esim. VILMTK-verohallinnon vuosi-ilmoitusaineistoa.

Huom. aloituspäivämäärät vuosilla 2002 ja 2003 voivat olla virheellisiä laskentatavan vuoksi.

Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@stat.fi.

## Muuttujat / Variables (13)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `DemAlpvm` | Demografinen aloituspvm | — | — | — |
| `DemAloitusAito` | Aloituksen aitouskoodi, kyllä/ei | — | vast_vaihtoehdo_69_2012_01_01 | luokitus |
| `DemLopPvm` | Demografinen lopetuspvm | — | — | — |
| `DemLopetusAito` | Lopetuksen aitouskoodi, kyllä/ei | — | vast_vaihtoehdo_69_2012_01_01 | luokitus |
| `tilaDemografia` | Demografiatiedon tila -koodi | — | demogtila_2_2012_01_01 | luokitus |
| `lopEnnakollinen` | Lopetuksen ennakollisuuskoodi (kyllä/ei -ennakko) | — | vast_vaihtoehdo_69_2012_01_01 | luokitus |
| `versioID` | VersioID | — | — | tunnistetiedot, ohjaustiedot |
| `syritysid` | Suojattu yritys-ID, yrityksen tunnus | — | — | tunnus |
| `syrtun` | Suojattu yritystunnus | — | — | — |
| `SDemSeuraaja` | Seuraajayrityksen suojattu yritysID | — | — | tunnus |
| `SDemEdeltaja` | Edeltäjäyrityksen suojattu yritysID | — | — | tunnus |
| `sdemseuyrtun` | Suojattu seuraajan yritystunnus | — | — | — |
| `sdemedyrtun` | Suojattu edeltäjän yritystunnus | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `DemAlpvm` — Demografinen aloituspvm

Demografinen aloituspäivämäärä on se päivämäärä, jolloin yrityksen on aidosti katsottu aloittaneen toimintansa. Liikevaihtoon huomoidaan kaikki lähteet. Yrityksellä ei katsota olleen henkilöstöä, jos se pyöristyy alle arvon 0.1. Aloitusvuotta edeltää vähintään kaksi tilastovuotta, jolloin yrityksellä ei ole ollut liikevaihtoa tai henkilöstöä. Aloituspäivämäärä on sen vuoden ensimmäinen päivä, jolloin yrityksellä on liikevaihtoa ja / tai henkilöstöä ensimmäistä kertaa vähintään kahteen vuoteen.

#### `DemAloitusAito` — Aloituksen aitouskoodi, kyllä/ei

**Luokitus / Classification:** vast_vaihtoehdo_69_2012_01_01 · **Ryhmä / Group:** luokitus

Aloituksen aitouskoodi, kyllä/ei. Luokitus ei täsmällisesti vastaa kuvauksessa esitettyä.

Tyhjä arvo viittaa aloitukseen, joka ei ole yhdistynyt automaattisessa aitouksien tarkistuksissa muihin yrityksiin, joten niitä voi pitää aitoina aloituksina.

Arvo 0 viittaa epäaitoon aloitukseen. Mikäli yritys yhdistyy potentiaaliseen edeltäjään, on muuttujassa SDemEdeltaja tämän yrityksen yritysID. Mikäli SDemEdeltäjä on tyhjä, potentiaalisia edeltäjiä on useita (esim. fuusiotilanne), aloitusmuoto on väärä tai aloittaneella yrityksellä on voimassa konsernisuhde aloitusvuonna.

Arvo 1 viittaa aitoon aloitukseen, joka on automaattisessa tai manuaalisessa tarkistuksessa todettu aidoksi. Automaattisessa tarkistuksessa yritys on yhdistynyt toisiin yksiköihin, mutta aloitus on katsottu aidoksi.

#### `DemLopPvm` — Demografinen lopetuspvm

Demografinen lopetuspvm. Liikevaihtoon huomoidaan kaikki lähteet. Yrityksellä ei katsota olleen henkilöstöä, jos se pyöristyy alle arvon 0.1. Lopetuspäivämäärä on sen tilastovuoden viimeinen päivä, jota seuraa vähintään kaksi tilastovuotta, joiden aikana yrityksellä ei ole ollut henkilöstöä tai liikevaihtoa.

#### `DemLopetusAito` — Lopetuksen aitouskoodi, kyllä/ei

**Luokitus / Classification:** vast_vaihtoehdo_69_2012_01_01 · **Ryhmä / Group:** luokitus

Lopetuksen aitouskoodi, kyllä/ei. 

Tyhjä arvo viittaa aitoon lopetukseen, jossa yritys aidosti lopettaa, eikä yhdisty automaattisessa tarkistuksessa muihin yksiköihin.

Arvo 0 viittaa epäaitoon lopetukseen, jossa yritys ei aidosti lopeta toimintaansa tuotannontekijöiden yhdistelmänä, vaan liiketoiminta jatkuu oletettavasti jossakin muussa yrityksessä. Mikäli SDemSeuraaja - muuttuja on tyhjä, potentiaalisia seuraajia on useita eikä seuraajaa voida määrittää. Mikäli SDemSeuraaja - muuttuja ei ole tyhjä, potentiaalinen seuraaja on tunnistettu.

Arvo 1 viittaa aitoon lopetukseen, jossa yritys lopettaa toimintansa. Lopetuksen aitous on tarkistettu automaattisesti tai manuaalisesti, mutta lopetus on todettu aidoksi.

#### `tilaDemografia` — Demografiatiedon tila -koodi

**Luokitus / Classification:** demogtila_2_2012_01_01 · **Ryhmä / Group:** luokitus

Demografiatiedon tila -koodi. Luokitus ei välttämättä ole aina aineistossa tässä kuvatun kaltainen. 

0 Tarkistamaton
1 Automaattisesti hyväksytty
2 Tarkistettava manuaalisesti
3 Manuaalisesti hyväksytty

#### `lopEnnakollinen` — Lopetuksen ennakollisuuskoodi (kyllä/ei -ennakko)

**Luokitus / Classification:** vast_vaihtoehdo_69_2012_01_01 · **Ryhmä / Group:** luokitus

Lopetuksen ennakollisuuskoodi (kyllä 1/ei 0 -ennakko). Luokitus ei välttämättä ole aina aineistossa tässä kuvatun kaltainen.

#### `versioID` — VersioID

**Ryhmä / Group:** tunnistetiedot, ohjaustiedot

YTY-tietovaraston demografia-taulun versioID.

#### `syritysid` — Suojattu yritys-ID, yrityksen tunnus

**Ryhmä / Group:** tunnus

Suojattu yritys-ID, yrityksen tunnus, generoitu / annettu Tilastokeskuksessa, käytössä muissa yritysaineistoissa vuodesta 2013 lähtien.

#### `syrtun` — Suojattu yritystunnus

Yritystunnus puuttuu kunnallisilta liikelaitoksilta.

#### `SDemSeuraaja` — Seuraajayrityksen suojattu yritysID

**Ryhmä / Group:** tunnus

Seuraajayrityksen suojattu yritysID, mikäli lopettaneelle yritykselle on pystytty tunnistamaan yksi yritysID joka on potentiaalinen jatkaja. Potentiaalisia seuraajia ei saa olla useita. Seuraajaksi valitaan ensisijaisesti hallinnollisesta aineistosta löydetty yritys. Mikäli yritys yhdistyy osoitteen ja toimialan perusteella toiseen yritykseen, saa samassa osoitteessa olla korkeintaan kolme yritystä, jotta kyseessä voi olla edeltäjä - jatkaja -pari.

#### `SDemEdeltaja` — Edeltäjäyrityksen suojattu yritysID

**Ryhmä / Group:** tunnus

Edeltäjäyrityksen suojattu yritysID. Potentiaalisia edeltäjiä ei saa olla useita. Edeltäjäksi valitaan ensisijaisesti hallinnollisesta aineistosta löydetty yritys. Mikäli yritys yhdistyy osoitteen ja toimialan perusteella toiseen yritykseen, saa samassa osoitteessa olla korkeintaan kolme yritystä, jotta kyseessä voi olla edeltäjä - jatkaja -pari. Yritykset, joilla on voimassa oleva konsernisuhde aloitusvuonna, merkitään epäaidoiksi aloituksiksi ilman edeltäjää. Vastaavasti toimitaan määrättyjen oikeudellisten yksiköiden hallinnollisten aloitusmuotojen kanssa.

#### `sdemseuyrtun` — Suojattu seuraajan yritystunnus

Ks. sdemseuraaja-muuttujan kuvaus

#### `sdemedyrtun` — Suojattu edeltäjän yritystunnus

ks. sdemedeltaja-muuttujan kuvaus

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
