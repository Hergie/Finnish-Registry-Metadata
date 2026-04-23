# MIGR_VOPAL Oleskelulupaa hakeneiden vastaanottopalvelutiedot - vastaanottorahat

- **Identifier:** `MIGR_VOPAL_jua_vorahat_000.xml`
- **DOI:** `std_2025-05_2025-05-19_ain_0001`
- **Temporal coverage:** 2011-01-01 - 2025-12-31
- **Published:** 2026-04-07
- **Organisation:** Tilastokeskus
- **Variable count:** 13
- **Observation count:** —
- **Population:** Oleskelulupaa hakeneet

## Description

<h3>MIGR_VOPAL Oleskelulupaa hakeneiden vastaanottopalvelutiedot (vastaanottorahat) </h3>

Maahanmuuttoviraston koostaman oleskelulupatietoja sisältävän aineiston rekisterinpitäjyys on siirtynyt Tilastokeskukselle, mikä tarkoittaa sitä, että aineistoa luvittaa tutkimuskäyttöön sekä tilastollisiin selvityksiin jatkossa Tilastokeskuksen tutkijapalvelut. Kyseisistä tiedoista on muodostettu viisi valmisaineistoa: MIGR_OLESK, MIGR_OPISK, MIGR_PERHE, MIGR_TYO ja MIGR_VOPAL, joiden kuvaukset löytyvät Taika-katalogista.

<b>MIGR_VOPAL -valmisaineisto koostuu tauluista vastaanottopalvelut ja vastaanottorahat. Tällä sivulla on aineistokuvaus taululle vastaanottorahat. </b>

<b>Vastaanottorahat</b>-taulussa osassa riveistä vastaanottorahan maksupäivä on selvästi väärin. Jonain päivämäärinä keskus on virheellisesti merkinnyt takautuvasti maksetuksi satoja päätöksiä. Rahan voi nostaa takautuvasti, mutta on hyvin poikkeuksellista, että sitä nostettaisiin vuosia päätöksen jälkeen. Virheellisiä ja puuttuvia maksutietoja voi paikata merkitsemällä maksupäiväksi päätöksen ajanjakson loppupäivämäärän.  

Alaikäisen perheenjäsenen saama vastaanottoraha tulisi merkitä hänelle, vaikka raha maksetaankin huoltajalle. Osassa keskuksista on merkitty virheellisesti, että perheen alaikäiset lapset saavat 0 euroa. 

Aineistosta on suojattu yksilöivät tunnisteet ja poistettu suoran tunnistamisen mahdollisuus. Taulut linkittyvät toisiinsa pseudonymisoiduilla tunnisteilla. Tietojen laatu on vaihtelevaa, ja pyrimme kuvaamaan esiin nousseet puutteet aineiston käytön helpottamiseksi. Valmisaineiston sisältö on arkaluonteista, ja se luvitetaan tutkimuskäyttöön tai tilastollisiin selvityksiin vain hyvin perustein. Kaikilta MIGR-aineistoja käyttöönsä hakevilta vaaditaan DPIA eli tietosuojan vaikutusten arviointi. 

Aineiston päivämäärämuuttujat on karkeistettu kuukausitasolle, mutta tarpeen vaatiessa tarkemmat päivämäärät on mahdollista saada räätälöitynä. Valmisaineiston päivityssykli pyritään saamaan jopa kuukausitasolle, kunhan tietojen toimitusprosessi vakiintuu. Aineistoissa käytettäville id-muuttujille löytyy suomenkieliset luokitukset Fionan metatiedoista.

Valmisaineistossa on nyt tietoja vuodesta 2011 alkaen, ja tätä vanhempia tietoja on tarkoitus lisätä aineistoon vuonna 2026. Aikasarja katkeaa vuosien 2010 ja 2011 vaihteessa, sillä aiemmat tiedot ovat peräisin eri järjestelmästä kuin UMA:sta, ja mahdollisesti heikkolaatuisempia kuin vuodesta 2011 alkaen. Hankkeille luvitetaan tietoja vain niiltä vuosilta, joille hankkeella on tarvetta. Käytännössä MIGR-valmisaineistoissa vuosijaottelua ei ole mahdollista toteuttaa täydellisesti, vaan tiedot on jaoteltu vuotta 2011 edeltävään ja vuodesta 2011 alkavaan jaksoon. 

Oleskelulupa-aineisto on uutta Tilastokeskuksella, ja vasta kartutamme substanssiosaamistamme kyseiseen aiheeseen. Tästä syystä valmisaineistoihin voi tulla vielä käytettävyyttä parantavia muutoksia. Otamme mieluusti palautetta vastaan.

Viralliset oleskelulupahakemuksien ja -päätöksien tilastot laatii edelleen Maahanmuuttovirasto. Aihepiirin tilastoja voi tarkastella <a href="https://tilastot.migri.fi/" > Migrin tilastointipalvelusta</a>. 
Aiheeseen ja terminologiaan voi tutustua tarkemmin <a href="https://migri.fi/oleskelulupa" > Maahanmuuttoviraston sivuilla</a>.

Kysymykset valmisaineistosta ja koko tietosisällöstä voi osoittaa Tilastokeskuksen tutkijapalveluihin tutkijapalvelut@stat.fi.

## Variables (13)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `SHNRO` | Suojattu henkilönumero | — | — | — |
| `CUSTOMER_ID_s` | Suojattu asiakasnumero | — | — | — |
| `ALLOWANCE_DCSN_ID_s` | Suojattu vastaanottorahapaatos id | — | — | — |
| `ALLOWANCE_PAYM_DETAIL_ID_s` | Suojattu maksutapahtuman id | — | — | — |
| `AUTHORITY_OFFICE_ID_s` | Suojattu vastaanottokeskus id | — | — | — |
| `AUTHORITY_OFFICE_NAME_s` | Suojattu vastaanottokeskus | — | — | — |
| `PAYMENT_SUM` | Maksusumma | — | — | — |
| `ALLOWANCE_ADDITION` | Lisays/vahennys | — | — | — |
| `IS_ONEOFF` | Kertaluonteinen | — | — | — |
| `dcsn_month` | Paatoksen ajankohta kuukausitasolla | — | — | — |
| `payment_month` | Maksuajankohta kuukausitasolla | — | — | — |
| `payment_start_month` | Maksun ajankohdan alku kuukausitasolla | — | — | — |
| `payment_end_month` | Maksun ajankohdan loppu kuukausitasolla | — | — | — |

### Variable definitions

#### `SHNRO` — Suojattu henkilönumero

#### `CUSTOMER_ID_s` — Suojattu asiakasnumero

#### `ALLOWANCE_DCSN_ID_s` — Suojattu vastaanottorahapaatos id

Perheenjäsenille tehdään yhteinen päätös

#### `ALLOWANCE_PAYM_DETAIL_ID_s` — Suojattu maksutapahtuman id

Jokaiselle päätöksessä olevalla henkilölle oma maksutapahtumarivi

#### `AUTHORITY_OFFICE_ID_s` — Suojattu vastaanottokeskus id

Vastaanottorahapäätöksen tehneen henkilön organisaatio eli vastaanottokeskus; alataso

#### `AUTHORITY_OFFICE_NAME_s` — Suojattu vastaanottokeskus

Vastaanottorahapäätöksen tehneen henkilön organisaatio eli vastaanottokeskus; alataso

#### `PAYMENT_SUM` — Maksusumma

#### `ALLOWANCE_ADDITION` — Lisays/vahennys

Onko maksu vähennys tai lisäys

#### `IS_ONEOFF` — Kertaluonteinen

Onko maksu kertaluonteinen; 0/1

#### `dcsn_month` — Paatoksen ajankohta kuukausitasolla

#### `payment_month` — Maksuajankohta kuukausitasolla

#### `payment_start_month` — Maksun ajankohdan alku kuukausitasolla

Vastaanottorahamaksu koskee tätä ajanjaksoa. Rahan voi nostaa myös takautuvasti

#### `payment_end_month` — Maksun ajankohdan loppu kuukausitasolla

Vastaanottorahamaksu koskee tätä ajanjaksoa. Rahan voi nostaa myös takautuvasti

---

[← Back to catalogue](../../README.md)
