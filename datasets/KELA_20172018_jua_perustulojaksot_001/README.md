# KELA_perustulorekisteri, Perustulojaksot

- **Identifier:** `KELA_20172018_jua_perustulojaksot_001.xml`
- **DOI:** `_2021-01_2021-01-25_ain_0001`
- **Temporal coverage:** 2017-01-01 - 2018-12-31
- **Published:** 2021-02-02
- **Organisation:** Tilastokeskus
- **Variable count:** 8
- **Observation count:** —
- **Population:** Perustulokokeilun kohdejoukko
- **Source:** Kansaneläkelaitoksen perustulokokeilurekisteri

## Description

Kelan perustulokokeilurekisteri on suojattu tutkimuskäyttöön. Tutkija hakee aineistolle käyttölupaa Kelasta.

Aineisto sisältää neljä taulua: 
 
1. Perustulokokeilun kohdejoukko 
2. Perustulojaksot 
3. Perustulomaksut  
4. Poiskuittaukset etuuksista  

Taulut 1 ja 2 muodostavat Perustulokokeilusta annetun lain (1528/2016) 18 §:n mukaisen perustulorekisterin. Taulut 3 ja 4 on muodostettu Kelassa helpottamaan varsinaisen perustulorekisterin käyttöä tutkimuksessa. Taulut muuttujineen on kuvattu tarkemmin erikseen. Taulut voi yhdistää henkilötasolla muuttujaa SHNRO avaimena käyttäen. 

Taulu sisältää perustulon ratkaisuihin liittyvät tiedot. Kukin ratkaisu kohdistuu tiettyyn ajanjaksoon. Alkuperäisen, koko perustulokokeilun ajan kattavan myöntöpäätöksen lisäksi ratkaisu voi olla esimerkiksi perustulon lakkautus tietyltä ajanjaksolta. Lisätietoa Perustulokokeilusta: https://www.finlex.fi/fi/laki/alkup/2016/20161528

## Variables (8)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `shnro` | Suojattu henkilönumero | — | — | — |
| `PERUSTULOJAKSO_ALPV` | Perustulojakson alkamispäivä | — | — | — |
| `PERUSTULOJAKSO_LOPV` | Perustulojakson päättymispäivä | — | — | — |
| `SYYKOODI` | Lakkautuksen tai hylkäyksen syy | — | — | — |
| `RATKAISUTYYPPI` | Ratkaisun tyyppi | — | — | — |
| `RATKAISU_PV` | Ratkaisupäivä | — | — | — |
| `POIKKEUS_SAANNOLLINEN_EUR` | Säännöllisen maksun poikkeuksellinen euromäärä | — | — | — |
| `POIKKEUS_VAJAA_KK_EUR` | Vajaan kuukauden poikkeuksellinen euromäärä | — | — | — |

### Variable definitions

#### `shnro` — Suojattu henkilönumero

#### `PERUSTULOJAKSO_ALPV` — Perustulojakson alkamispäivä

#### `PERUSTULOJAKSO_LOPV` — Perustulojakson päättymispäivä

#### `SYYKOODI` — Lakkautuksen tai hylkäyksen syy

Kertoo millä syyllä perustulokokeiluun kuuluneen henkilön maksu on lakkautettu tai hylätty  
Muuttujan arvot:  

01 = ei ole antanut pyydettyjä tietoja;  

02 = hakija ei ole antanut pyydettyjä selvityksiä;  

03 = etuuden saaja on kuollut;  

04 = estävä sosiaalietuus (lakkautus);  

07 = asevelvollisuus tai siviilipalvelus (lakkautus);  

51 = asevelvollisuus tai siviilipalvelus (hylkäys);  

53 = estävä sosiaalietuus (hylkäys);  

54 = sovelletaan työskentelyn perusteella vieraan valtion sosiaaliturvalakia;  

55 = oleskelu ulkomailla (yli 30 päivää) tai on muuttanut ulkomaille pysyvästi;  

99 = muut syyt

#### `RATKAISUTYYPPI` — Ratkaisun tyyppi

Muuttujan arvot: 
•	MYÖ = myöntö; 
•	TAR = tarkistus; 
•	HYL = hylky; 
•	LAK = lakkautus

#### `RATKAISU_PV` — Ratkaisupäivä

Lopullinen ratkaisupäivä

#### `POIKKEUS_SAANNOLLINEN_EUR` — Säännöllisen maksun poikkeuksellinen euromäärä

#### `POIKKEUS_VAJAA_KK_EUR` — Vajaan kuukauden poikkeuksellinen euromäärä

---

[← Back to catalogue](../../README.md)
