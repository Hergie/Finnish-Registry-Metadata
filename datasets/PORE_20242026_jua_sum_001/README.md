# PORE_SUM Kuluttajaluotot

- **Identifier:** `PORE_20242026_jua_sum_001.xml`
- **DOI:** `alkan_2026-08_2026-08-24_ain_0001`
- **Temporal coverage:** 2024-12-31 - 2026-06-30
- **Published:** 2026-08-27
- **Organisation:** Tilastokeskus
- **Variable count:** 27
- **Observation count:** —

## Description

PORE_SUM-valmisaineistomoduuli sisältää Positiivisen luottotietorekisterin yksityishenkilöiden summatut luotto- ja velkatiedot kuukausitasolla, kuten kuluttajaluotot ja niihin rinnastuvat luotot, jotka on eritelty kertaluontoisiin ja jatkuviin luottoihin.

<b>Valmisaineiston tarkentava nimi</b>
Positiivisen luottotietorekisterin yksityishenkilöiden summatut luotto- ja velkatiedot kuukausitasolla (PORE_SUM)

<b>Aineiston perusjoukko, koostaminen ja tietolähteet</b>
Positiivinen luottotietorekisteri on rekisteri, johon kootaan tiedot yksityishenkilöiden luotoista ja tuloista sekä muille luonnollisille henkilöille kuin kuluttajille myönnetyt luotot. Tällaisia luottoja ovat esimerkiksi toiminimiyrittäjälle tai maatalouden harjoittajalle myönnetyt luotot. 

Luotonantajat ilmoittavat luottotietorekisteriin tiedot myöntämistään luotoista sekä luotoissa tapahtuneista muutoksista. Tällaisia muutoksia ovat esimerkiksi lyhennykset ja luottosopimuksen muutokset.

Tiedot toimittaa Verohallinnon Tulorekisteriyksikkö. Lisätietoja Positiivisen luottotietorekisterin sivuilla: <a href="https://www.vero.fi/positiivinenluottotietorekisteri/tietoa-rekisterista.html">Tietoa rekisteristä</a>.

<b>Huomioitavaa aineistosta ja sen käytöstä</b>
Pohja-aineisto päivittyy päivittäin niin, että päivitetyt ja korjatut tiedot korvaavat vanhat tiedot. Tästä syystä kahtena eri ajankohtana päivitetyt tiedot eivät vastaa toisiaan täysin, vaan voivat sisältää pieniä muutoksia.

<b>Aineiston päivitysaikataulu</b>
Tiedot päivitetään kuukausittain. Tutustu valmisaineistojen <a href="https://stat.fi/fi/palvelut/palvelut-tutkijoille/tutkimusaineistot/valmisaineistot/valmisaineistojen-paivitysaikataulu">päivitysaikatauluun</a>.

<b>Aineiston käyttö ja tilaaminen</b>
Aineisto on tarkoitettu käytettäväksi FIONA-etäpalvelun kautta, ja se on linkitettävissä muihin henkilövalmisaineistoihin suojatun henkilötunnisteen avulla.

Valmisaineiston voi tilata tutkimuksen kohdejoukolle ja tarvittavalta ajanjaksolta. Kokonaisaineiston (kaikki muuttujat koko populaatiosta ja kaikilta saatavilla olevilta vuosilta) käyttöoikeus myönnetään vain, jos tutkimuksellinen tarve sitä erityisesti edellyttää. Lisäksi aineistosta voi tilata räätälöidyn version, joka sisältää vain osan muuttujista.

Aineisto on FIONA-etäkäyttöjärjestelmässä jaettuina vuosikansioihin tilastovuosittain.

<b>Tarkempaa tietoa muuttujista</b>
Toiminimiyrittäjien lainat sisältyvät toisen vaiheen tietoihin, jotka on lisätty rekisteriin kuluttajaluottojen jälkeen.

<b>Lisätietoja</b>
Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@stat.fi

## Variables (27)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `vuosi` | Vuosi | — | — | — |
| `kk` | Kuukausi | — | — | — |
| `hid_e` | Luoton saajan suojattu henkilön yksilöivä tunniste | — | — | — |
| `yrtun_s` | Luoton saajan suojattu Y-tunnus | — | — | — |
| `amountissued_yht` | Kertaluottojen myönnetty määrä | — | — | — |
| `amountpaid_yht` | Kertaluottojen nostettu määrä | — | — | — |
| `amortizationpaid_yht` | Kertaluottojen maksettu lyhennys | — | — | — |
| `interestpaid_yht` | Kertaluottojen maksettu korko | — | — | — |
| `otherexpenses_yht` | Kertaluottojen muut maksetut luottokustannukset | — | — | — |
| `onetimeservicefees_yht` | Kertaluottosopimusten kertakulut | — | — | — |
| `homeloan_yht` | Asuntolaina, velkasaldo | — | — | — |
| `homeloanforfirsthome_yht` | Asuntolaina ensiasuntoon, velkasaldo | — | — | — |
| `homeloanforleisurehouse_yht` | Asuntolaina vapaa-ajanasuntoon, velkasaldo | — | — | — |
| `homeloanforinvestment_yht` | Asuntolaina sijoitusasuntoon, velkasaldo | — | — | — |
| `studentloan_yht` | Opintolaina, velkasaldo | — | — | — |
| `guaranteereceivable_yht` | Opintolainan takaussaatava, velkasaldo | — | — | — |
| `loanforvehicleorcraft_yht` | Liikennevälineen hankkimiseksi myönnetty kuluttajaluotto, velkasaldo | — | — | — |
| `loanforbusinessactivities_yht` | Luotto elinkeinotoimintaan, velkasaldo | — | — | — |
| `otherconsumercredit_yht` | Muu kuluttajaluotto, velkasaldo | — | — | — |
| `otherloan_yht` | Muu luotto, velkasaldo | — | — | — |
| `kayttotarkoituspuuttuu_yht` | Puuttuvat, velkasaldo | — | — | — |
| `kertaluotot_yht` | Kertaluottojen velkasaldo yhteensä | — | — | — |
| `credit_balance_yht` | Luottokorttien käytetty summa | — | — | — |
| `credit_interestpaid_yht` | Luottokorttien maksettu korko | — | — | — |
| `leasing_sopimus` | Leasing sopimuksen olemassaolo | — | — | — |
| `delayed_yht` | Maksuviiveet yhteensä | — | — | — |
| `foreclosed_yht` | Eräännytetyt luotot yhteensä | — | — | — |

### Variable definitions

#### `vuosi` — Vuosi

Maksutapahtuman päivämäärästä johdettu vuosi.

#### `kk` — Kuukausi

Maksutapahtuman päivämäärästä johdettu kuukausi.

#### `hid_e` — Luoton saajan suojattu henkilön yksilöivä tunniste

Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e -tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä.

#### `yrtun_s` — Luoton saajan suojattu Y-tunnus

Tunnuksen täytyy olla suomalaisen Y-tunnuksen muotovaatimuksen mukainen ja liittyä yritys- ja yhteisötietojärjestelmässä luotonsaajan henkilötunnukseen.

#### `amountissued_yht` — Kertaluottojen myönnetty määrä

Velallisen henkilön kaikkien kertaluottojen myönnetty määrä yhteensä. Mikäli jollakin luotolla on useampi osakas, ko. luoton myönnetty määrä on jaettu osakkaiden kesken. Näin ollen esim. kahden osakkaan yhteinen 100 000 euron luotto jakaantuu kahdelle eri velallisille siten, että molemmille tulee lainaa 50 000 euroa.

#### `amountpaid_yht` — Kertaluottojen nostettu määrä

Velallisen henkilön kaikkien kertaluottojen nostettu määrä yhteensä. Mikäli jollakin luotolla on useampi osakas, ko. luoton nostettu määrä on jaettu osakkaiden kesken. Näin ollen esim. kahden osakkaan yhteinen 100 000 euron luotto jakaantuu kahdelle eri velallisille siten, että molemmille tulee lainaa 50 000 euroa.

#### `amortizationpaid_yht` — Kertaluottojen maksettu lyhennys

Velallisen henkilön kaikkien kertaluottojen maksettu lyhennys yhteensä. Mikäli jollakin luotolla on useampi osakas, ko. luoton maksettu lyhennys on jaettu osakkaiden kesken. Näin ollen esim. kahden osakkaan yhteinen 50 000 euron maksettu lyhennys jakaantuu kahdelle eri velallisille siten, että molemmille tulee maksettua lyhennystä 25 000 euroa.

#### `interestpaid_yht` — Kertaluottojen maksettu korko

Velallisen henkilön kaikkien kertaluottojen maksettu korko yhteensä. Mikäli jollakin luotolla on useampi osakas, ko. luoton maksettu korko on jaettu osakkaiden kesken. Näin ollen esim. kahden osakkaan yhteinen 50 000 euron maksettu korko jakaantuu kahdelle eri velallisille siten, että molemmille tulee maksettua korkoa 25 000 euroa.

#### `otherexpenses_yht` — Kertaluottojen muut maksetut luottokustannukset

Velallisen henkilön kaikkien kertaluottojen muut maksetut luottokustannukset yhteensä. Mikäli jollakin luotolla on useampi osakas, ko. luoton muut maksetut luottokustannukset on jaettu osakkaiden kesken. Näin ollen esim. kahden osakkaan yhteinen 50 000 euron summa jakaantuu kahdelle eri velallisille siten, että molemmille tulee muita maksettuja luottokustannuksia 25 000 euroa.

#### `onetimeservicefees_yht` — Kertaluottosopimusten kertakulut

Velallisen henkilön kaikkien kertaluottojen luottosopimuksen kertakulu yhteensä. Mikäli jollakin lainalla on useampi osakas, ko. lainan sopimusten kertakulut on jaettu osakkaiden kesken. Näin ollen esim. kahden osakkaan yhteinen 50 000 euron summa jakaantuu kahdelle eri velallisille siten, että molemmille tulee sopimusten kertakuluja 25 000 euroa.

#### `homeloan_yht` — Asuntolaina, velkasaldo

Luoton käyttötarkoitus on asuntolaina. Jos velallisella on useampi asuntolaina, ne on summattu yhteen. Mikäli samalla lainalla on useampi osakas, velkasumma on jaettu osakkaiden kesken. Näin ollen esim. kahden osakkaan yhteinen 100 000 euron asuntolaina jakaantuu kahdelle eri velallisille siten, että molemmille tulee asuntolainaa 50 000 euroa.

#### `homeloanforfirsthome_yht` — Asuntolaina ensiasuntoon, velkasaldo

Luoton käyttötarkoitus on asuntolaina ensiasuntoon. Jos velallisella on useampi asuntolaina ensiasuntoon, ne on summattu yhteen. Mikäli samalla lainalla on useampi osakas, velkasumma on jaettu osakkaiden kesken. Näin ollen esim. kahden osakkaan yhteinen 100 000 euron laina jakaantuu kahdelle eri velallisille siten, että molemmille tulee lainaa 50 000 euroa.

#### `homeloanforleisurehouse_yht` — Asuntolaina vapaa-ajanasuntoon, velkasaldo

Luoton käyttötarkoitus on asuntolaina vapaa-ajanasuntoon. Jos velallisella on useampi asuntolaina vapaa-ajanasuntoon, ne on summattu yhteen. Mikäli samalla lainalla on useampi osakas, velkasumma on jaettu osakkaiden kesken. Näin ollen esim. kahden osakkaan yhteinen 100 000 euron laina jakaantuu kahdelle eri velallisille siten, että molemmille tulee lainaa 50 000 euroa.

#### `homeloanforinvestment_yht` — Asuntolaina sijoitusasuntoon, velkasaldo

Luoton käyttötarkoitus on asuntolaina sijoitusasuntoon. Jos velallisella on useampi asuntolaina sijoitusasuntoon, ne on summattu yhteen. Mikäli samalla lainalla on useampi osakas, velkasumma on jaettu osakkaiden kesken. Näin ollen esim. kahden osakkaan yhteinen 100 000 euron laina jakaantuu kahdelle eri velallisille siten, että molemmille tulee lainaa 50 000 euroa.

#### `studentloan_yht` — Opintolaina, velkasaldo

Luoton käyttötarkoitus on opintolaina. Jos velallisella on useampi opintolaina, ne on summattu yhteen.

#### `guaranteereceivable_yht` — Opintolainan takaussaatava, velkasaldo

Luoton käyttötarkoitus on opintolainan takaussaatava. Jos velallisella on useampi opintolainan takaussaatava, ne on summattu yhteen.

#### `loanforvehicleorcraft_yht` — Liikennevälineen hankkimiseksi myönnetty kuluttajaluotto, velkasaldo

Luoton käyttötarkoitus on liikennevälineen hankkimiseksi myönnetty kuluttajaluotto. Jos velallisella on useampi liikennevälineen hankkimisluotto, ne on summattu yhteen. Mikäli samalla luotolla on useampi osakas, velkasumma on jaettu osakkaiden kesken. Näin ollen esim. kahden osakkaan yhteinen 50 000 euron luotto jakaantuu kahdelle eri velallisille siten, että molemmille tulee luottoa 25 000 euroa.

#### `loanforbusinessactivities_yht` — Luotto elinkeinotoimintaan, velkasaldo

Luoton käyttötarkoitus on luotto elinkeinotoimintaan. Jos velallisella on useampi luotto elinkeinotoimintaan, ne on summattu yhteen. Mikäli samalla luotolla on useampi osakas, velkasumma on jaettu osakkaiden kesken. Näin ollen esim. kahden osakkaan yhteinen 100 000 euron luotto jakaantuu kahdelle eri velallisille siten, että molemmille tulee luottoa 50 000 euroa. Tieto saatavilla kattavasti 02/2026 alkaen.

#### `otherconsumercredit_yht` — Muu kuluttajaluotto, velkasaldo

Luoton käyttötarkoitus on muu kuluttajaluotto. Jos velallisella on useampi muu kuluttajaluotto, ne on summattu yhteen. Mikäli samalla luotolla on useampi osakas, velkasumma on jaettu osakkaiden kesken. Näin ollen esim. kahden osakkaan yhteinen 50 000 euron luotto jakaantuu kahdelle eri velallisille siten, että molemmille tulee luottoa 25 000 euroa.

#### `otherloan_yht` — Muu luotto, velkasaldo

Luoton käyttötarkoitus on muu luotto. Jos velallisella on useampi muu luotto, ne on summattu yhteen. Mikäli samalla luotolla on useampi osakas, velkasumma on jaettu osakkaiden kesken. Näin ollen esim. kahden osakkaan yhteinen 50 000 euron luotto jakaantuu kahdelle eri velallisille siten, että molemmille tulee luottoa 25 000 euroa. Tieto saatavilla kattavasti 03/2025 alkaen.

#### `kayttotarkoituspuuttuu_yht` — Puuttuvat, velkasaldo

Tässä kentässä ovat ne kertaluotot, joiden käyttötarkoitusta ei tiedetä (esim. velkajärjestelyn takia). Jos velallisella on useampi (käyttötarkoitus puuttuu) luotto, ne on summattu yhteen. Mikäli samalla luotolla on useampi osakas, velkasumma on jaettu osakkaiden kesken. Näin ollen esim. kahden osakkaan yhteinen 50 000 euron luotto jakaantuu kahdelle eri velallisille siten, että molemmille tulee luottoa 25 000 euroa.

#### `kertaluotot_yht` — Kertaluottojen velkasaldo yhteensä

Muuttujaan on summattu taulussa olevien erilaisten kertaluottojen (asuntolaina, autolaina...) kokonaissumma, ts. velkasaldot summattu yhteen.

#### `credit_balance_yht` — Luottokorttien käytetty summa

Luottokorttien käytetty summa, eli paljollako luottokortteja käytetty kuukauden aikana.

#### `credit_interestpaid_yht` — Luottokorttien maksettu korko

Luottokorttien maksettu korko, eli paljonko luottokorteilla korollista velkaa kuukaudessa.

#### `leasing_sopimus` — Leasing sopimuksen olemassaolo

Jos henkilöllä on Leasing sopimus, kenttä saa arvon 1.

#### `delayed_yht` — Maksuviiveet yhteensä

Yhteissumma (eur) kaikista kk aikana viivästyneistä maksuista.

#### `foreclosed_yht` — Eräännytetyt luotot yhteensä

Yhteissumma (eur) kaikista kk aikana eräännytetyistä luotoista.

---

[← Back to catalogue](../../README.md)
