# PRH_BOARD Kaupparekisterin vastuuhenkilötiedot

- **Identifier:** `PRH_19942019_jua_board_001.xml`
- **DOI:** `work_2017-11_2017-11-06_ain_0001`
- **Temporal coverage:** 1994-01-01 - 2019-07-14
- **Published:** 2019-10-31
- **Organisation:** Tilastokeskus
- **Variable count:** 10
- **Observation count:** —
- **Population:** Tietyt yhtiömuodot ja tietyt roolit
- **Source:** Patentti- ja rekisterihallituksen ylläpitämä kaupparekisteri
- **Related:** <a href= "https://www.prh.fi/stc/attachments/rekisteri-_ja_tietosuojaselosteet/kaupparekisteri_tietosuojaseloste.pdf">Kaupparekisteri</a>

## Kuvaus / Description

Tutkimuskäyttöön on poimittu PRH:n kaupparekisteristä vastuuhenkilöt, hallituksen jäsenet, varajäsenet, puheenjohtajat sekä toimitusjohtajat, jotka on rekisteröity aikavälillä 1.1.1994 - 31.12.2015 ja 1.1.2016 - 14.7.2019 (kaksi erillistä poimintaa). Yhtiömuodoista ovat mukana osakeyhtiöiden lisäksi vakuutusyhtiöt, säästö- ja osuuspankit sekä osuuskunnat. 

Rekisterissä olevat yritykset ja lakanneet yritykset ovat erillisissä tiedostoissa.

Poiminnassa on ollut haasteena aikavälillä tapahtuneet muutokset ilmoitusten käsittelyssä ja järjestelmissä. Erityisesti uuden kaupparekisterin  käsittelyjärjestelmän  käyttöönoton jälkeen toukokuun alusta 2014 lähtien, mm. henkilön itse ilmoittamien tehtävistä erojen käsittely on muuttunut. Aiemmin toimielin jäi voimaan ja vain eroavat roolit vanhennettiin, nykyään koko toimielin rekisteröidään uudelleen. Hallituksen voimassaolon alkamispäivä on siis joko se päivämäärä, kun itse hallitus on rekisteröity, tai jos hallituksesta eroaa joku, niin hallituksen voimassaolon alkupäivämäärä on tällöin hallituksen jäsenen eron rekisteröintipäivä. Omien erojen yhteydessä rekisteröidään näin ollen aina koko hallitus uudelleen. Vanhassa järjestelmässä  (ennen 5/2014) hallituksella pysyi voimassaolon alkupäivänä aina varsinainen rekisteröintipäivä,  vaikka joku olisi sieltä eronnutkin. Tietosisällössä voi olla historiatietojen osalta näiden järjestelmäteknisten ja muiden tietojen käsittelyssä aikanaan tapahtuneiden virheiden vuoksi sisällöllisiä virheitä ja puutteellisuuksia.

PRH ei vastaa aineistoon sisältyvien tietojen virheistä, katoamisista tai muuttumisesta taikka tämän aiheuttamista vahingoista asiakkaalle tai kolmannelle osapuolelle. PRH ei myöskään ole vastuussa Tilastokeskuksen aineistoon tekemistä muutoksista ja tarjoamista palveluista.

Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@stat.fi.

## Muuttujat / Variables (10)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `syrtun` | Suojattu yritystunnus | — | — | — |
| `shnro` | Suojattu henkilönumero | — | — | — |
| `YRITYKSEN_TILA` | Yrityksen tila | — | — | — |
| `YR_REKIST_PVM` | Yrityksen rekisteröintipäivämäärä | — | — | — |
| `YRITYSMUOTO` | Yritysmuoto | — | — | — |
| `ROOLIKOODI` | Vastuuhenkilörooli | — | — | — |
| `ROOLIN_ALKU_PVM` | Roolin alkamispäivämäärä | — | — | — |
| `ROOLIN_LOPPU_PVM` | Roolin loppumispäivämäärä | — | — | — |
| `LAKKAAMIS_PVM` | Yrityksen lakkaamispäivämäärä | — | — | — |
| `LAKKAAMISTYYPPI` | Yrityksen lakkaamistapa | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `syrtun` — Suojattu yritystunnus

#### `shnro` — Suojattu henkilönumero

#### `YRITYKSEN_TILA` — Yrityksen tila

R=rekisterissä, L=lakannut

#### `YR_REKIST_PVM` — Yrityksen rekisteröintipäivämäärä

#### `YRITYSMUOTO` — Yritysmuoto

Yritysmuoto saa arvot:
oy=osakeyhtiö
oyj=julkinen osakeyhtiö
voy=vakuutusosakeyhtiö
voj=julkinen vakuutusosakeyhtiö
kvy=keskinäinen vakuutusyhtiö
kvj=julkinen keskinäinen vakuutusosakeyhtiö
sp=säästöpankki
op=osuuspankki
osk=osuuskunta

#### `ROOLIKOODI` — Vastuuhenkilörooli

Vastuuhenkilörooli saa arvot:
j=hallituksen jäsen
vj=hallituksen varajäsen
pj=hallituksen puheenjohtaja
tj=toimitusjohtaja

#### `ROOLIN_ALKU_PVM` — Roolin alkamispäivämäärä

#### `ROOLIN_LOPPU_PVM` — Roolin loppumispäivämäärä

#### `LAKKAAMIS_PVM` — Yrityksen lakkaamispäivämäärä

#### `LAKKAAMISTYYPPI` — Yrityksen lakkaamistapa

Lakkaamistapa saa arvot:
FU	Fuusio	
JA	Jakautuminen	
JY	Jatkaminen yksityisenä elinkeinonharjoittajana	
KO	Konkurssi	
KOP	Poisto	
LA	Lakannut	
LUP	SPL 90-92 §:n mukainen liiketoiminnan luovutus, muutos säätiöksi	
PA	Poisto (asunto-osakeyhtiölaki)	
PK	Poisto (osuuskuntalaki)	
PO	Poisto (kaupparekisterilaki)	
POIS	Poisto	
POT	Tilinpäätöspoisto	
PP	Poisto (osakeyhtiölaki)	
PT	Poisto (tuomioistuinmääräys)	
SE	Selvitystila	
SEP	Poisto	
SI	Kotipaikan siirto

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
