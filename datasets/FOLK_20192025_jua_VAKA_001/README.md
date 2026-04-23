# FOLK_VAKA - Vardaan pohjautuvat varhaiskasvatustiedot kuukausitasolla

- **Identifier:** `FOLK_20192025_jua_VAKA_001.xml`
- **DOI:** `vaka_2026-01_2026-01-08_ain_0001`
- **Temporal coverage:** 2019-01-01 - 2024-12-31
- **Published:** 2026-03-31
- **Organisation:** Tilastokeskus
- **Variable count:** 20
- **Observation count:** —
- **Population:** Suomessa varhaiskasvatukseen osallistuneet lapset

## Description

FOLK_VAKA moduuli pohjautuu Varhaiskasvatuksen tietovarannon (Varda) tietoihin. Moduulissa on saatavilla tietoa kuukausitasolla varhaiskasvatukseen osallistuvista lapsista Suomessa.


<h3>Tietolähteet ja perusjoukko</h3>
Aineisto on kokonaisaineisto, joka pohjautuu Varhaiskasvatuksen tietovarannon tietoihin, joita on voitu täydentää väestötietojärjestelmän tiedoilla. Varhaiskasvatuksen tietovaranto on kuvattu seuraavasti <a href="https://wiki.eduuni.fi/spaces/ophPPK/pages/453739928/Varda">Vardan Eduuni-wiki palvelussa</a> (9.1.2026):
<i>Varaiskasvatuksen tietovaranto on kansallinen tietovaranto, joka sisältää tietoja varhaiskasvatustoimijoista, varhaiskasvatuksen toimipaikoista, varhaiskasvatuksessa olevista lapsista, lasten huoltajista, varhaiskasvatuksen henkilöstöstä ja varhaiskasvatuksessa annettavasta tuesta. Varda on otettu käyttöön vaiheittain vuosina 2019-2020.</i>

Aineisto on muodostettu yhdistämällä kuukausikohtaisesti lapsen varhaiskasvatustietoihin tarkasteluhetkellä voimassaolevia tietoja lapsesta, varhaiskasvatusmaksusta, toimijasta ja toimipaikasta. Valmisainestoon on kuukausitasolla kerätty niiden lasten tiedot, joilla on ollut voimassaoleva varhaiskasvatussuhde ja -päätös kyseisenä kuukautena.

FOLK_VAKA moduulin perusjoukko muodostuu Vardasta löytyvistä varhaiskasvatukseen osallistuvista lapsista Suomessa, joilla on ollut voimassaoleva varhaiskasvatuspäätös ja -suhde havaintokuukauden ja -vuoden aikana.


<b>Huomioitavaa</b>
Tämän paneelimuotoisen valmisaineiston avulla voi hakea helposti kuukauden tarkkuudella Vardasta löytyvien lasten varhaiskasvatukseen liittyviä tietoja. Vardaan pohjautuvia varhaiskasvatustietoja löytyy myös moduuleista VAKA_ASIAKKUUS_SUPPEA ja VAKA_ASIAKKUUS.

Varda on otettu vaiheittain käyttöön vuosien 2019-2020 aikana, jonka takia ensimmäisten vuosien tiedot voivat olla puutteellisia. Tämä voi näkyä esimerkiksi varhaiskasvatuksen piirissä olevien lasten lukumäärissä.

Yhdellä lapsella voi olla yksi tai useampi varhaiskasvatussuhde. Tämä voi näkyä siten, että sama lapsi voi esiintyä useammalla rivillä valmisaineistossa saman kuukauden aikana, mikäli hänellä on useampi voimassaoleva varhaiskasvatussuhde tarkastelukuukauden aikana.

Tämä valmisaineisto ei sisällä varhaiskasvatuksen maksutietoja, mutta ne on mahdollista lisätä räätälöitynä toimeksiantona. Vardan tietomallin mukaisesti varhaiskasvatusmaksut eivät linkity suoraan varhaiskasvatuspäätökseen tai -suhteeseen. Tämän takia maksutietojen yhdistäminen varhaiskasvatustietoihin on tehty pohjautuen maksutietojen, varhaiskasvatussuhteen ja varhaiskasvatuspäätöksen päivämääriin.

Lapsen asuinkunta pohjautuu Digi- ja väestötietoviraston (DVV) väestötietojärjestelmän (VTJ) tietoihin, mutta jota on voitu täydentää Vardan kotikuntatiedolla, mikäli henkilöllä ei ole suomalaista henkilötunnusta.


<b>Aineiston päivitysaikataulu</b>
Aineisto päivitetään kerran vuodessa.


<b>Aineiston yleisimmät käyttötavat</b>
Aineistoa voidaan hyödyntää tutkimuksiin tai selvityksiin, joissa tarvitaan kuukausitason tarkkuudella tietoa lasten varhaiskasvatuksesta, joiden tietoja on kerätty Vardaan.


<b>Rajoitukset</b>
Aineisto voidaan yhdistää toisiin henkilötason valmisaineistoihin niiden henkilöiden osalta, joilla on suomalainen henkilötunniste. Aineiston toimipaikka- tai toimijatiedot voidaan yhdistää suojatun organisaatio-OID muuttujan avulla niihin aineistoihin, joissa on myös organisaatio-OID tunniste käytössä (kuten KOSKI). Tällä hetkellä aineiston toimipaikka- tai toimijatiedot eivät ole yhdistettävissä sellaisiin valmisaineistoihin, joiden toimipaikan tai toimijan tunnisteet pohjautuvat Tilastokeskuksen yritysrekisterin tunnisteisiin.


<b>Lisätietoa</b>
Vardan tietosisältö on dokumentoitu <p><a href="https://wiki.eduuni.fi/spaces/ophPPK/pages/488747922/Vardan+tietoluettelo">Vardan Eduuni-wiki palvelussa (9.1.2026)</a>, josta voi hakea lisätietoa aineiston tietosisällöstä.

<a href="https://vipunen.fi/fi-fi/varhaiskasvatus/Sivut/default.aspx">Opetushallituksen tilastopalvelu</a> (9.1.2026)

<a href="https://stat.fi/tilasto/vaka">Varhaiskasvatustilasto</a> ja tilaston <a href="https://stat.fi/tilasto/dokumentaatio/vaka">dokumentaatio</a> (9.1.2026).


Lisätietoa aineistosta saa Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@tilastokeskus.fi.

## Variables (20)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `vuosi` | Vuosi | — | — | — |
| `kuukausi` | Kuukausi | — | — | — |
| `henkilo_OID_s` | Suojattu henkilö-OID | — | — | — |
| `hid_e` | Suojattu henkiön yksilöivä tunniste. | — | — | — |
| `syntymavuosi` | Henkilön syntymävuosi | — | — | — |
| `syntymakuukausi` | Henkilön syntymäkuukausi | — | — | — |
| `sukupuoli` | Henkilön sukupuoli | — | — | — |
| `aidinkieli_k` | Henkilön äidinkieli, karkeistettu tasolle suomi, ruotsi, muu | — | — | — |
| `kotikunta` | Lapsen asuinkunta | — | — | — |
| `vuorohoito_kytkin` | Vuorohoito | — | — | — |
| `paivittainen_vaka_kytkin` | Päivittäinen varhaiskasvatus (mikäli lapsi ei ole vuorohoidossa) | — | — | — |
| `kokopaivainen_vaka_kytkin` | Kokopäiväinen varhaiskasvatus (mikäli lapsi ei ole vuorohoidossa) | — | — | — |
| `tilapainen_vaka_kytkin` | Tilapäinen varhaiskasvatus (mikäli lapsi on kunnallisessa varhaiskasvatuksessa, jonka järjestämismuoto on jm01, jm02 tai jm03) | — | — | — |
| `tuntimaara_viikossa` | Tuntimäärä viikossa | — | — | — |
| `jarjestamismuoto` | Luokitusmuuttuja varhaiskasvatuksen järjestämismuodosta. | — | — | — |
| `toimipaikan_kuntakoodi` | Varhaiskasvatustoimipaikan kuntakoodi | — | — | — |
| `toimipaikka_OID_s` | Suojattu toimipaikan organisaatio-OID | — | — | — |
| `toimija_OID_s` | Suojattu toimijan organisaatio-OID | — | — | — |
| `toimintamuoto` | Toimipaikan toimintamuoto | — | — | — |
| `oma_organisaatio_OID_s` | Suojattu organisaatio-OID. | — | — | — |

### Variable definitions

#### `vuosi` — Vuosi

#### `kuukausi` — Kuukausi

#### `henkilo_OID_s` — Suojattu henkilö-OID

Henkilön yksilöivä tunniste.

#### `hid_e` — Suojattu henkiön yksilöivä tunniste.

Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e-tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä.

#### `syntymavuosi` — Henkilön syntymävuosi

#### `syntymakuukausi` — Henkilön syntymäkuukausi

#### `sukupuoli` — Henkilön sukupuoli

1=Mies,
2=Nainen.

#### `aidinkieli_k` — Henkilön äidinkieli, karkeistettu tasolle suomi, ruotsi, muu

1=suomi,
2=ruotsi,
MUU=muu,
Tyhjä arvo=ei tietoa.

#### `kotikunta` — Lapsen asuinkunta

Perustuu Tilastokeskuksen kolminumeroiseen kuntanumeroon.

#### `vuorohoito_kytkin` — Vuorohoito

Normaaliksi varhaiskasvatusajaksi on määritelty arkisin (ma-pe) klo 6.00-18.00 välisenä aikana tapahtuva varhaiskasvatus. Vuorohoidoksi on määritelty normaalin varhaiskasvatusajan ulkopuolella tapahtuva varhaiskasvatus.
Lapsi on vuorohoidossa, jos varhaiskasvatus tapahtuu ns. normaalien varhaiskasvatusaikojen ulkopuolella (vuorohoito = true). Lapsi ei ole vuorohoidossa, jos varhaiskasvatus toteutuu normaalin varhaiskasvatusajan sisällä. (vuorohoito = false).

#### `paivittainen_vaka_kytkin` — Päivittäinen varhaiskasvatus (mikäli lapsi ei ole vuorohoidossa)

Lapsi on päivittäisessä varhaiskasvatuksessa, jos varhaiskasvatus jakautuu viidelle arkipäivälle (ma-pe), (päivittäinen varhaiskasvatus =  true).

Lapsi on osaviikkoisessa varhaiskasvatuksessa, jos varhaiskasvatus toteutuu vain joinain arkipäivinä (ma-pe), ei kaikkina arkipäivinä, (päivittäinen varhaiskasvatus = false).

#### `kokopaivainen_vaka_kytkin` — Kokopäiväinen varhaiskasvatus (mikäli lapsi ei ole vuorohoidossa)

Lapsi on kokopäiväisessä varhaiskasvatuksessa, jos varhaiskasvatusaika on yli viisi tuntia päivässä (5.01 tai yli) ja varhaiskasvatus tapahtuu arkipäivinä (ma-pe), (kokopäiväinen varhaiskasvatus  = true).
Lapsi on osapäiväisessä varhaiskasvatuksessa, jos varhaiskasvatusaika on viisi tuntia tai vähemmän (5.0 tai alle) päivässä ja varhaiskasvatus tapahtuu arkipäivinä (ma-pe), (kokopäiväinen varhaiskasvatus = false).

#### `tilapainen_vaka_kytkin` — Tilapäinen varhaiskasvatus (mikäli lapsi on kunnallisessa varhaiskasvatuksessa, jonka järjestämismuoto on jm01, jm02 tai jm03)

Tilapäisellä varhaiskasvatuksella tarkoitetaan kunnan järjestämää varhaiskasvatusta, johon lapsi osallistuu väliaikaisesti ja satunnaisesti.

#### `tuntimaara_viikossa` — Tuntimäärä viikossa

Lapsen varhaiskasvatuspäätökseen tai sitä vastaavaan sopimukseen merkitty viikoittainen tuntimäärä.

#### `jarjestamismuoto` — Luokitusmuuttuja varhaiskasvatuksen järjestämismuodosta.

Muuttujaan on koottu seuraavat arvot perustuen <a href="https://virkailija.opintopolku.fi/varda/julkinen/koodistot/vardajarjestamismuoto">Vardan järjestysmuotoon</a> (30.03.2026):
0=Kunnan tai kuntayhtymän järjestämä varhaiskasvatus (JM01),
1=Ostopalveluna tai palvelusetelillä toteutettu varhaiskasvatus, kunnan tai kuntayhtymän järjestämä (JM02 ja JM03),
2=Yksityisen hoidon tuella järjestetty varhaiskasvatus tai yksityinen varhaiskasvatus ilman yksityisen hoidon tukea (JM04 ja JM05)

Muuttujassa arvo 0 viittaa kunnallisen varhaiskasvatuksen järjestysmuotoon ja arvot 1 ja 2 yksityisen varhaiskasvatuksen järjestämismuotoon.

#### `toimipaikan_kuntakoodi` — Varhaiskasvatustoimipaikan kuntakoodi

Perustuu Tilastokeskuksen kolminumeroiseen kuntanumeroon.

#### `toimipaikka_OID_s` — Suojattu toimipaikan organisaatio-OID

Yksilöivä tunniste toimipaikalle.

#### `toimija_OID_s` — Suojattu toimijan organisaatio-OID

Yksilöivä tunniste varhaiskasvatusta tuottaville ja järjestäville toimijoille.

#### `toimintamuoto` — Toimipaikan toimintamuoto

Perustuu <a href="https://virkailija.opintopolku.fi/varda/julkinen/koodistot/vardatoimintamuoto">Vardan luokitukseen</a> (30.03.2026):
TM01=Päiväkoti,
TM02=Perhepäivähoito,
TM03=Ryhmäperhepäivähoito.

#### `oma_organisaatio_OID_s` — Suojattu organisaatio-OID.

Varhiaskasvatuksen järjestämisvastuussa oleva kunta tai kuntayhtymä, jos varhaiskasvatus on tuotettu ostopalvelulla tai palvelusetelillä.

---

[← Back to catalogue](../../README.md)
