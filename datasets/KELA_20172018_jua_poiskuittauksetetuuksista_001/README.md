# KELA_perustulorekisteri, Poiskuittaukset etuuksista

- **Identifier:** `KELA_20172018_jua_poiskuittauksetetuuksista_001.xml`
- **DOI:** `eltu_2021-01_2021-01-25_ain_0002`
- **Temporal coverage:** 2017-01-01 - 2018-12-31
- **Published:** 2021-02-01
- **Organisation:** Tilastokeskus
- **Variable count:** 5
- **Observation count:** —
- **Population:** Perustulokokeilun kohdejoukko
- **Source:** Kansaneläkelaitoksen perustulokokeilurekisteri

## Kuvaus / Description

Kelan perustulokokeilurekisteri on suojattu tutkimuskäyttöön. Tutkija hakee aineistolle käyttölupaa Kelasta.

Aineisto sisältää neljä taulua: 
1.	Perustulokokeilun kohdejoukko
2.	Perustulojaksot
3.	Perustulomaksut 
4.	Poiskuittaukset etuuksista 

Taulut 1 ja 2 muodostavat Perustulokokeilusta annetun lain (1528/2016) 18 §:n mukaisen perustulorekisterin. Taulut 3 ja 4 on muodostettu Kelassa helpottamaan varsinaisen perustulorekisterin käyttöä tutkimuksessa. Taulut muuttujineen on kuvattu tarkemmin erikseen. Taulut voi yhdistää henkilötasolla muuttujaa SHNRO avaimena käyttäen.

Perustulokokeilusta annetun lain (1528/2016) 7 §:n nojalla perustulo pienentää joidenkin samanaikaisesti mak-settujen sosiaalietuuksien määrää. Näitä etuuksia ovat työmarkkinatuki, peruspäiväraha, ansiopäiväraha, sairauspäiväraha ja osasairauspäiväraha, vanhempainpäiväraha, erityishoitoraha, kuntoutusraha sekä tartuntatauti-lain (583/1986) 27 §:ssä tarkoitettu päiväraha ja ansionmenetyskorvaus. Taulu sisältää tiedot maksetun perus-tulon vähentämisestä muista etuuksista. 

Osasta työttömyyskassojen maksamista etuuksista tehdyistä poiskuittauksista puuttuu muuttujan HETU tieto. Näitä poiskuittauksia ei siis voi yhdistää perustulon saajaan. Tällaisia tiedoiltaan puutteellisia kuittauksia on 178 kappaletta, mikä vastaa noin 16 prosentin osuutta kaikista työttömyyskassojen maksamista etuuksista tehdyistä poiskuittauksista. Euromääräisesti kohdentumattomia kuittauksia on 503609,45 euron verran, mikä vastaa noin 15 prosentin osuutta kaikista työttömyyskassojen maksamista etuuksista tehdyistä poiskuittauksis-ta.
Lisätietoa Perustulokokeilusta: https://www.finlex.fi/fi/laki/alkup/2016/20161528

## Muuttujat / Variables (5)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `shnro` | Suojattu henkilönumero | — | — | — |
| `TYYPPI` | Kuittauksen tyyppi | — | — | — |
| `KA_MAKSU_PV` | Kuittauksen suorituspäivä | — | — | — |
| `KIRJATTU_EUR` | Kuittauksen euromäärä | — | — | — |
| `PALAUTTAVA_ETUUS_KOODI` | Etuus | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `shnro` — Suojattu henkilönumero

#### `TYYPPI` — Kuittauksen tyyppi

Kuittausta koskevan etuuden maksava taho
Muuttujan arvot: 
•	PU = Perustulon kuit-taus Kelan maksamasta etuudesta; 
•	ULKOINEN = Perustu-lon kuittaus työttö-myyskassan maksamasta etuudesta

#### `KA_MAKSU_PV` — Kuittauksen suorituspäivä

Kuittauksen kohteena olevan etuuden maksupäivä

#### `KIRJATTU_EUR` — Kuittauksen euromäärä

#### `PALAUTTAVA_ETUUS_KOODI` — Etuus

Etuus, josta kuittaus on tehty
Muuttujan arvot: 
•	FM = työmarkkinatuki; 
•	FP = peruspäiväraha; 
•	KR = kuntoutusraha; 
•	PR = sairauspäiväraha; 
•	QE = kansaneläke; 
•	VR = vanhempainpäivä-raha, 
•	KASSA = työttömyys-kassan maksama työt-tömyysetuus

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
