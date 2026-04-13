# FIRM_EMPENT Yritysten/toimipaikkojen ammattirakenteet (YA241)

- **Identifier:** `YA241_19902009_jua_occuyritys_001.xml`
- **DOI:** `work_2014-01_2014-01-03_ain_0001`
- **Temporal coverage:** 1990-01-01 - 2009-12-31
- **Published:** 2016-02-17
- **Organisation:** Tilastokeskus
- **Variable count:** 79
- **Observation count:** —
- **Population:** Yritysrekisterissä esiintyvät yritykset/toimipaikat, jotka työllistävät enemmän kuin yhden henkilön
- **Source:** FLEED (mm. työssäkäyntitilasto), yritysrekisteri
- **Related:** <a href= "http://www.tilastokeskus.fi/til/tyokay/">Työssäkäynti</a> <a href= "http://www.stat.fi/meta/rekisteriselosteet/tutka_rekisteriseloste_toimipaikkojen_yritysten_ammattirakenteet.html">Toimipaikkojen/yritysten ammattirakenteet</a>

## Kuvaus / Description

Occu_tt_xxyy-aineistot kuvaavat henkilökunnan ammattirakenteita yritys- (tt=yr) ja toimipaikkatasolla (tt=tp) sekä niiden muutoksia lähtövuoden (xx) ja päätevuoden (yy) välillä. Muutoksien osalta tarkastellaan sitä, millaisten työntekijävirtojen välityksellä ne ovat tapahtuneet. Tässä erotellaan työtekijöiden liikkuvuus yritysten/toimipaikkojen välillä (external) ja yritysten/toimipaikkojen sisällä ammattien välillä (internal).

Lähtökohtana ovat yritysrekisterissä esiintyvät yritykset/toimipaikat, jotka työllistävät enemmän kuin yhden henkilön (yritysrekisterin mukaan). Näiden yritysten/toimipaikkojen henkilöt on poimittu työssäkäyntitilastoaineistosta. Mukaan on otettu sellaiset työntekijät (so. ei ole tulkittu poikkeavaksi havainnoksi), joilla on a) kelvollinen ammattikoodi (isco88-luokitus), b) ovat työskennelleet vähintään 7 kuukautta vuoden aikana ja c) palkka ei ole liian poikkeava kyseissä ammattiluokassa kyseisenä vuonna (ammattiluokat on tässä määritelty 1-numerotasolla 8 ryhmään). Keskimääräinen kuukausipalkka on tulkittu poikkeavaksi, jos se kuuluu kyseisen ammattiryhmän alimpaan tai ylimpään yhteen prosenttiin. Jos henkilö on tulkittu poikkeavaksi havainnoksi joko lähtövuonna (xx) tai päätevuonna (yy) siksi, että ammattikoodi ei ole kelvollinen (vaikka henkilöllä on yritys/toimipaikka-suhde), työskentelykuukausia on vähemmän kuin 7 tai keskimääräinen kuukausipalkka on hyvin alhainen tai korkea (ks. yllä), se ei ole mukana kyseisen vuosiparin tarkastelussa. Näin on vältetty se, että poikkeavat havainnot eivät näyttäydy näennäisenä liikkuvuutena.

Toimipaikkatason aineistot:
occu_tp_9095
occu_tp_9500
occu_tp_0005
occu_tp_0006
occu_tp_0405
occu_tp_0506
occu_tp_0607
occu_tp_0708
occu_tp_0809

Yritystason aineistot:
occu_yr_9095
occu_yr_9500
occu_yr_0005
occu_yr_0006
occu_yr_0405
occu_yr_0506
occu_yr_0607
occu_yr_0708
occu_yr_0809

Ammattiryhmät määritellään ammattiluokituksen 1-numerotason mukaan. Luokitus 2-numerotasolla:
isco88_2	isco88_2_label	
11	Legislators and senior officials	
12	Corporate managers	
13	Managers of small enterprises	
21	Physical, mathematical and engineering science professionals	
22	Life science and health professionals	
23	Teaching professionals	
24	Other professionals	
31	Physical and engineering science associate professionals	
32	Life science and health associate professionals	
33	Traffic instructors and other teaching associate professionals	
34	Other associate professionals	
41	Office clerks	
42	Customer services clerks	
51	Personal and protective services workers	
52	Models, salespersons and demonstrators	
61	Skilled agricultural and fishery workers (not included)	
71	Extraction and building trades workers	
72	Metal, machinery and related trades workers	
73	Precision, handicraft, craft printing and related trades workers	
74	Other craft and related trades workers	
81	Stationary plant and related operators	
82	Machine operators and assemblers	
83	Drivers and related water traffic operators	
91	Sales and services elementary occupations	
92	Agricultural, fishery and related labourers	
93	Labourers in manufacturing and construction	

Lisätietoja aineistosta: 
Maliranta, M. (2013). Globalization, occupational restructuring and firm 
productivity. ETLA, Working Papers  No. 5.
Tehtäväindeksit (ei-rutiini/interaktiivinen):
Nilsson Hakkala, K., Heyman, F., Sjöholm, F. (2009). Multinational firms and job tasks. VATT, Working Papers  No. 8/2009.

Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@tilastokeskus.fi.

## Muuttujat / Variables (79)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `vuosi` | Year | — | — | — |
| `syrtun` | Firm code (encrypted) | — | — | — |
| `sykstun` | Plant code (encrypted) | — | — | — |
| `tol_2002` | Industry code, NACE 2002 | — | — | — |
| `syrtun_x` | Firm in initial year | — | — | — |
| `syrtun_y` | Firm in end year | — | — | — |
| `nonrout_x` | Index, non-routine tasks, initial year | — | — | — |
| `nonrout_y` | Index, non-routine tasks, end year | — | — | — |
| `interact_x` | Index, interactive tasks, initial year | — | — | — |
| `interact_y` | Index, interactive tasks, end year | — | — | — |
| `ejr_t` | Excess task reallocation | — | — | — |
| `lx` | Employment in initial year, register | — | — | — |
| `ly` | Emplpoyment in end year, register | — | — | — |
| `jx` | Employment in initial year, employment stat. | — | — | — |
| `jy` | Emplpoyment in end year, employment stat. | — | — | — |
| `jx_1` | Employment, occupation=1, in initial year, employment stat. | — | — | — |
| `jx_2` | Employment, occupation=2, in initial year, employment stat. | — | — | — |
| `jx_3` | Employment, occupation=3, in initial year, employment stat. | — | — | — |
| `jx_4` | Employment, occupation=4, in initial year, employment stat. | — | — | — |
| `jx_5` | Employment, occupation=5, in initial year, employment stat. | — | — | — |
| `jx_7` | Employment, occupation=7, in initial year, employment stat. | — | — | — |
| `jx_8` | Employment, occupation=8, in initial year, employment stat. | — | — | — |
| `jx_9` | Employment, occupation=9, in initial year, employment stat. | — | — | — |
| `jy_1` | Employment, occupation=1, in end year | — | — | — |
| `jy_2` | Employment, occupation=2, in end year | — | — | — |
| `jy_3` | Employment, occupation=3, in end year | — | — | — |
| `jy_4` | Employment, occupation=4, in end year | — | — | — |
| `jy_5` | Employment, occupation=5, in end year | — | — | — |
| `jy_7` | Employment, occupation=7, in end year | — | — | — |
| `jy_8` | Employment, occupation=8, in end year | — | — | — |
| `jy_9` | Employment, occupation=9, in end year | — | — | — |
| `jc_1` | Task creation, occupation=1 | — | — | — |
| `jc_2` | Task creation, occupation=2 | — | — | — |
| `jc_3` | Task creation, occupation=3 | — | — | — |
| `jc_4` | Task creation, occupation=4 | — | — | — |
| `jc_5` | Task creation, occupation=5 | — | — | — |
| `jc_7` | Task creation, occupation=7 | — | — | — |
| `jc_8` | Task creation, occupation=8 | — | — | — |
| `jc_9` | Task creation, occupation=9 | — | — | — |
| `jd_1` | Task destruction, occupation=1 | — | — | — |
| `jd_2` | Task destruction, occupation=2 | — | — | — |
| `jd_3` | Task destruction, occupation=3 | — | — | — |
| `jd_4` | Task destruction, occupation=4 | — | — | — |
| `jd_5` | Task destruction, occupation=5 | — | — | — |
| `jd_7` | Task destruction, occupation=7 | — | — | — |
| `jd_8` | Task destruction, occupation=8 | — | — | — |
| `jd_9` | Task destruction, occupation=9 | — | — | — |
| `he_1` | External hiring, occupation=1 | — | — | — |
| `he_2` | External hiring, occupation=2 | — | — | — |
| `he_3` | External hiring, occupation=3 | — | — | — |
| `he_4` | External hiring, occupation=4 | — | — | — |
| `he_5` | External hiring, occupation=5 | — | — | — |
| `he_7` | External hiring, occupation=7 | — | — | — |
| `he_8` | External hiring, occupation=8 | — | — | — |
| `he_9` | External hiring, occupation=9 | — | — | — |
| `se_1` | External separation, occupation=1 | — | — | — |
| `se_2` | External separation, occupation=2 | — | — | — |
| `se_3` | External separation, occupation=3 | — | — | — |
| `se_4` | External separation, occupation=4 | — | — | — |
| `se_5` | External separation, occupation=5 | — | — | — |
| `se_7` | External separation, occupation=7 | — | — | — |
| `se_8` | External separation, occupation=8 | — | — | — |
| `se_9` | External separation, occupation=9 | — | — | — |
| `hi_1` | Internal hiring, occupation=1 | — | — | — |
| `hi_2` | Internal hiring, occupation=2 | — | — | — |
| `hi_3` | Internal hiring, occupation=3 | — | — | — |
| `hi_4` | Internal hiring, occupation=4 | — | — | — |
| `hi_5` | Internal hiring, occupation=5 | — | — | — |
| `hi_7` | Internal hiring, occupation=7 | — | — | — |
| `hi_8` | Internal hiring, occupation=8 | — | — | — |
| `hi_9` | Internal hiring, occupation=9 | — | — | — |
| `si_1` | Internal separation, occupation=1 | — | — | — |
| `si_2` | Internal separation, occupation=2 | — | — | — |
| `si_3` | Internal separation, occupation=3 | — | — | — |
| `si_4` | Internal separation, occupation=4 | — | — | — |
| `si_5` | Internal separation, occupation=5 | — | — | — |
| `si_7` | Internal separation, occupation=7 | — | — | — |
| `si_8` | Internal separation, occupation=8 | — | — | — |
| `si_9` | Internal separation, occupation=9 | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `vuosi` — Year

#### `syrtun` — Firm code (encrypted)

Only in firm-level data

#### `sykstun` — Plant code (encrypted)

#### `tol_2002` — Industry code, NACE 2002

#### `syrtun_x` — Firm in initial year

Only in plant-level data

#### `syrtun_y` — Firm in end year

Only in plant-level data

#### `nonrout_x` — Index, non-routine tasks, initial year

#### `nonrout_y` — Index, non-routine tasks, end year

#### `interact_x` — Index, interactive tasks, initial year

#### `interact_y` — Index, interactive tasks, end year

#### `ejr_t` — Excess task reallocation

#### `lx` — Employment in initial year, register

#### `ly` — Emplpoyment in end year, register

#### `jx` — Employment in initial year, employment stat.

#### `jy` — Emplpoyment in end year, employment stat.

#### `jx_1` — Employment, occupation=1, in initial year, employment stat.

#### `jx_2` — Employment, occupation=2, in initial year, employment stat.

#### `jx_3` — Employment, occupation=3, in initial year, employment stat.

#### `jx_4` — Employment, occupation=4, in initial year, employment stat.

#### `jx_5` — Employment, occupation=5, in initial year, employment stat.

#### `jx_7` — Employment, occupation=7, in initial year, employment stat.

#### `jx_8` — Employment, occupation=8, in initial year, employment stat.

#### `jx_9` — Employment, occupation=9, in initial year, employment stat.

#### `jy_1` — Employment, occupation=1, in end year

#### `jy_2` — Employment, occupation=2, in end year

#### `jy_3` — Employment, occupation=3, in end year

#### `jy_4` — Employment, occupation=4, in end year

#### `jy_5` — Employment, occupation=5, in end year

#### `jy_7` — Employment, occupation=7, in end year

#### `jy_8` — Employment, occupation=8, in end year

#### `jy_9` — Employment, occupation=9, in end year

#### `jc_1` — Task creation, occupation=1

#### `jc_2` — Task creation, occupation=2

#### `jc_3` — Task creation, occupation=3

#### `jc_4` — Task creation, occupation=4

#### `jc_5` — Task creation, occupation=5

#### `jc_7` — Task creation, occupation=7

#### `jc_8` — Task creation, occupation=8

#### `jc_9` — Task creation, occupation=9

#### `jd_1` — Task destruction, occupation=1

#### `jd_2` — Task destruction, occupation=2

#### `jd_3` — Task destruction, occupation=3

#### `jd_4` — Task destruction, occupation=4

#### `jd_5` — Task destruction, occupation=5

#### `jd_7` — Task destruction, occupation=7

#### `jd_8` — Task destruction, occupation=8

#### `jd_9` — Task destruction, occupation=9

#### `he_1` — External hiring, occupation=1

#### `he_2` — External hiring, occupation=2

#### `he_3` — External hiring, occupation=3

#### `he_4` — External hiring, occupation=4

#### `he_5` — External hiring, occupation=5

#### `he_7` — External hiring, occupation=7

#### `he_8` — External hiring, occupation=8

#### `he_9` — External hiring, occupation=9

#### `se_1` — External separation, occupation=1

#### `se_2` — External separation, occupation=2

#### `se_3` — External separation, occupation=3

#### `se_4` — External separation, occupation=4

#### `se_5` — External separation, occupation=5

#### `se_7` — External separation, occupation=7

#### `se_8` — External separation, occupation=8

#### `se_9` — External separation, occupation=9

#### `hi_1` — Internal hiring, occupation=1

#### `hi_2` — Internal hiring, occupation=2

#### `hi_3` — Internal hiring, occupation=3

#### `hi_4` — Internal hiring, occupation=4

#### `hi_5` — Internal hiring, occupation=5

#### `hi_7` — Internal hiring, occupation=7

#### `hi_8` — Internal hiring, occupation=8

#### `hi_9` — Internal hiring, occupation=9

#### `si_1` — Internal separation, occupation=1

#### `si_2` — Internal separation, occupation=2

#### `si_3` — Internal separation, occupation=3

#### `si_4` — Internal separation, occupation=4

#### `si_5` — Internal separation, occupation=5

#### `si_7` — Internal separation, occupation=7

#### `si_8` — Internal separation, occupation=8

#### `si_9` — Internal separation, occupation=9

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
