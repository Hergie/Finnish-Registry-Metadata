# EDUC_YTL  ylioppilaskirjoitusten tulokset 1967-2025

- **Identifier:** `EDUC_19902025_jua_ytl_001.xml`
- **DOI:** `lop_2016-01_2016-01-15_ain_0001`
- **Temporal coverage:** 1967-01-01 - 2025-12-31
- **Published:** 2021-10-06
- **Organisation:** Tilastokeskus
- **Variable count:** 18
- **Observation count:** —
- **Population:** Ylioppilaskirjoituksiin osallistuneet henkilöt
- **Source:** Ylioppilastutkintolautakunnan aineisto

## Kuvaus / Description

EDUC_YTL-moduuli (FMEB-data = Finnish Matriculation Examination Board data) sisältää Ylioppilastutkintolautakunnan (YTL) tietoja ylioppilaskirjoituksiin osallistuneista vuoden 1990 keväästä alkaen.Tiedostot sisältävät kaikki ylioppilaskirjoituksiin osallistuneet henkilöt tältä periodilla ja heidän ylioppilaskirjoitushistorian tai henkilöt, jotka ovat valmistuneet lukiosta tältä periodilta. 

Aineistomoduulin rakenne ja tietosisältö ovat erilaisia aikaisempiin historiavuositiedostoihin verrattuna (aineisto vuosilta 1967-1989). Huomioithan, että yhden henkilön tulokset voivat löytyä osin 1989 tiedostosta ja osin vuoden 1991 tiedoista. 
Henkilö voi esiintyä myöhemmissä tiedostoissa, mikäli korottaa arvosanaa. Toisaalta jos henkilö esiintyy myöhemmissä tiedostoissa ja henkilön kohdalla on tyhjää, niin tällöin aikaisempi tulos on mitätöity. 

Kunta-muuttujasta ("municipality"): Vuoden 2022 aineistosta on poistettu lakkautettujen kuntien kuntakoodit, jotka on korvattu voimassaolevalla kuntakoodilla. Ennen vuotta 2022 aineistossa on kuntakoodeista johtuvia dublikaatteja, sillä osalla henkilöistä on samat tiedot kahdella rivillä: toisella rivillä kuntakoodina lakkautetun kunnan koodi ja toisella voimassaolevan kunnan koodi.

Pävitys kunta-muuttujasta ("municipality") sekä lukion suojatusta tunnuksesta ("sotunnus"): Vuosina 2023-2025 lukion suojattu tunnus ja siihen liittyvä kuntakoodi on yhdistetty päivityshetkellä ajankohtaisten kuntatietojen ja oppilaitostietojen mukaan. Jos lukioon liittyvä kunta tai lukion tunnus ei löydy ajantasaisesta kunta- ja oppilaitoslistauksesta jää näistä tyhjä havainto aineiston "municip"- ja "sotunnus"-sarakkeisiin. Muuttuja "sotunnus" on korvattu "otunnus_s" muuttujalla.

Moduuli koostuu kolmesta erilaisesta tiedostomuodosta. Suojattu henkilönumero (hid_e) toimii avaimena eri tiedostojen kesken.

1. Degree_details-tiedosto sisältää seuraavat tiedot: 
           - tutkinnon valmistumisajankohta (neljä pakollista tai kompensaatio)
           - ajankohta, jolloin  lukio on suoritettu 
           - tieto siitä, että voidaanko tietoa vielä päivittää (eli onko tutkinto kesken)

2. Results-nimiset tiedostot kokoavat yhteen kirjoituksien koskevat yksityiskohtia ja tuloksia eri aineista. Tiedosto sisältä myös tietoja lukiosta. Lukion oppilatostunnus on aineisotossa salattuna.

3. PointsXXXXk- sekä PointsXXXXs- tiedostot sältävät yksityiskohtaiset pistetiedot aine- ja tehtävä-tasolla kevään (k) ja syksyn (s) osalta. Tiedot vuoden 2016 syksyyn asti.

Tarkemmat muuttujakohtaiset kuvaukset muuttujaluettelossa. Aineiden (exam) ja tehtävien (section) osalta erillinen luettelo käytetyistä koodeista D-aseman metadata-kansiossa (metadata > Finnish metadata > EDUC_YTL). 

08.05.2025 Aineisto päivitetty syksyn 2024 tiedoilla. Muuttuja "sotunnus" on korvattu "otunnus_s" muuttujalla.

13.01.2025 Aineisto päivitetty kevään 2024 tiedoilla.

3.10.2022: Aineisto päivitetty kevään 2022 tiedoilla.

6.4.2022: Vuoden 2020 tiedot on päivitetty ja korjattu. Tiedot sijaitsevat kevään ja syksyn tutkintokertojen mukaan nimetyissä tiedostoissa, ja tutkintokerta ilmenee tiedostonimessä olevasta kirjaimesta ("s" = kevät, "k"=syksy).

28.3.2022: Aineisto päivitetty vuoden 2021 tiedoilla. Tiedot sijaitsevat kevään ja syksyn tutkintokertojen mukaan nimetyissä tiedostoissa, ja tutkintokerta ilmenee tiedostonimessä olevasta kirjaimesta ("s" = kevät, "k"=syksy).

6.10.2021: Vuoden 2020 tiedot ("educ_ytl_2020_tua_results" sekä "educ_ytl_2020_tua_degreedetails") ovat tarkastamattomat. Mahdollisista puutteista/virheistä voi ilmoittaa Tutkijapalveluihin (tutkijapalvelut@stat.fi). 

18.6.2021: Vuosien 2017-2019 tiedostot ("educ_20172019_tua_ytlresults" sekä "educ_20172019_tua_ytldegreedetails") on korjattu shnro-tunnisteiden osalta. Aiemmissa virheellisissä tiedostoissa suurirmman osan henkilöistä shnro-tunniste oli jäänyt tyhjäksi, mikä saatiin nyt korjatuksi.

Lisätietoja saatavilla Tilastokeskuksen Tutkijapalveluista: tutkijapalvelut@stat.fi.

## Muuttujat / Variables (18)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `hid_e` | Suojattu henkiön yksilöivä tunniste. | — | — | — |
| `exam` | Aine (RESULTSxxxx- ja POINTSxxxx-tauluissa) | — | — | — |
| `section` | Tehtävien tunnukset (only in POINTSxxxx tables) | — | — | — |
| `question` | Kysymysnumero (only in POINTSxxxx - tables) | — | — | — |
| `qs_score` | Pisteet (POINTSxxxx-tauluissa) | — | — | — |
| `examination` | Suorituskerran vuosi ja periodi | — | — | — |
| `grading_exam_id` | Kokeen tunniste (POINTSxxxx-taulussa). | — | — | — |
| `education` | Tutkintokokonaisuuteen liittyvä opiskelumuoto kokeeseen ilmottautuessa (RESULTSxxxx-tauluissa). | — | — | — |
| `participation` | Kokelaan tutkintokokonaisuuden tyyppi (RESULTSxxxx-tauluissa). | — | — | — |
| `score` | Yhteispisteet (RESULTSxxxx-tauluissa) | — | — | — |
| `span` | Span (RESULTSxxxx-tauluissa) | — | — | — |
| `mandatory` | Kokeen pakollisuus (RESULTSxxxx-tauluissa) | — | — | — |
| `grade` | Arvosana (RESULTSxxxx-tauluissa) | — | — | — |
| `aborted` | Koe keskeytetty (RESULTSxxxx-tauluissa) | — | — | — |
| `municip` | Oppilaitoksen kunta (RESULTSxxxx-tauluissa) | — | — | — |
| `otunnus_s` | Suojattu oppilaitoksen tunniste (RESULTSxxxx-tauluissa) | — | — | — |
| `certificate` | Vuosi ja periodi, kun ensimmäinen ylioppilastutkintotodistus on muodostettu ja myönnetty (degree details -tauluissa) | — | — | — |
| `graduation` | Ylioppilastutkinnnon valmistumisvuosi ja -periodi (degree details -tauluissa). | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `hid_e` — Suojattu henkiön yksilöivä tunniste.

Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e-tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä.

#### `exam` — Aine (RESULTSxxxx- ja POINTSxxxx-tauluissa)

Kirjoitetun ylioppilaskokeen aineen tunnus.

#### `section` — Tehtävien tunnukset (only in POINTSxxxx tables)

grading_section_detail_code_ytl_id

#### `question` — Kysymysnumero (only in POINTSxxxx - tables)

Kokeen kysymysnumero (grading_question_display_number).

#### `qs_score` — Pisteet (POINTSxxxx-tauluissa)

Sensorin antamat pisteet kysymyksestä.

#### `examination` — Suorituskerran vuosi ja periodi

Kokeen suoritusvuosi ja -periodi (K=kevät, S=syksy).

#### `grading_exam_id` — Kokeen tunniste (POINTSxxxx-taulussa).

Kokeen periodikohtainen tunniste.

#### `education` — Tutkintokokonaisuuteen liittyvä opiskelumuoto kokeeseen ilmottautuessa (RESULTSxxxx-tauluissa).

Kokelaan opintotausta, jonka perusteella hän saa osallistumisoikeuden ylioppilastutkintoon. Koulujen täyttämä tieto.
1=yo (lukion opiskelija), 
2=vocational (ammatillisten opintojen pohjalta tutkintoa suorittava kokelas), 
3=yo-and-vocational (lukion oppimäärää ja ammatillista tutkintoa suorittava kokelas), 
4=ei tietoa (muu opiskelija).

#### `participation` — Kokelaan tutkintokokonaisuuden tyyppi (RESULTSxxxx-tauluissa).

Kokelaan tutkintokokonaisuuden tyyppi säilyy samana suorituskerran aikana (span). 
1=first (tutkinnon suorittaja), 
2=after-graduation (korottaja ja/tai täydentäjä), 
3=separate-exam (erillisen kokeen suorittaja). 

Kategorian 1 kokonaisuuksissa on mukana kokeiden uusimisia (korottaja). Kategoriassa 2 on aina kyse kokeelasta, jonka tutkinto on jo aiemmin valmis.

#### `score` — Yhteispisteet (RESULTSxxxx-tauluissa)

Kokeen yhteispisteet, joiden perusteella muodostuu arvosana. Yhteispisteet puuttuvat aikaisemmilta vuosilta, mutta ne voi laskea POINTS-tauluista.

#### `span` — Span (RESULTSxxxx-tauluissa)

Tutkinnon suorituksen aloitusajankohta, johon kyseinen koe liittyy.

#### `mandatory` — Kokeen pakollisuus (RESULTSxxxx-tauluissa)

Ylioppilastutkintoon vaadittava koe (pakolliset kokeet).
1=pakollinen,
0=ei pakollinen.

#### `grade` — Arvosana (RESULTSxxxx-tauluissa)

Aineen arvosana.

#### `aborted` — Koe keskeytetty (RESULTSxxxx-tauluissa)

Koe keskeytetty: 
1=keskeytetty, 
0=ei keskeytetty.

#### `municip` — Oppilaitoksen kunta (RESULTSxxxx-tauluissa)

Koulun sijaintikunta, perustuu Tilastokeskuksen oppilaitosrekisteriin.

#### `otunnus_s` — Suojattu oppilaitoksen tunniste (RESULTSxxxx-tauluissa)

Suojattu oppilaitoksen tunniste perustuu Tilastokeskuksen oppilaitosrekisteriin.

#### `certificate` — Vuosi ja periodi, kun ensimmäinen ylioppilastutkintotodistus on muodostettu ja myönnetty (degree details -tauluissa)

Vuosi (xxxx) ja periodi (K=kevät, S=syksy). Ennen syksyä 2019 certificate kuvaa ajankohtaa, jolloin kokelas on suorittanut pakolliset ylioppilastutkintoon vaaditut kokeet (tai kokelas on saanut puuttuvia kompensaatioita). Syksystä 2019 lähtien kirjaustapa on muuttunut: certificate kuvaa ajankohtaa, kun kokelas valmistuu ylioppilaaksi (graduation), ja saa ylioppilastutkintotodistuksen.

Vuonna 2022 ylioppilastutkintoon vaadittujen kokeiden määritelmä on muuttunut: vuoteen 2021 asti pakollisten kokeiden lukumäärä oli 4 ja vuodesta 2022 alkaen tutkintoon sisällytettävien aineiden kokeiden minimäärä on 5.

#### `graduation` — Ylioppilastutkinnnon valmistumisvuosi ja -periodi (degree details -tauluissa).

Vuosi (xxxx) and periodi (K=kevät, S=syksy). Kokelas on valmistunut, kun hän on suorittanut ylioppilastutkintoon vaaditut kokeet ja on saattanut loppuun lukio-opinnot.

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
