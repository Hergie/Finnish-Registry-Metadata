# MIGR_PERHE Oleskelulupaa hakeneiden perhetiedot - perheside

- **Identifier:** `MIGR_PERHE_jua_perheside_000.xml`
- **DOI:** `std_2025-05_2025-05-19_ain_0001`
- **Temporal coverage:** 2011-01-01 - 
- **Published:** 2026-02-10
- **Organisation:** Tilastokeskus
- **Variable count:** 5
- **Observation count:** —
- **Population:** Oleskelulupaa hakeneet

## Description

<h3>MIGR_PERHE Oleskelulupaa hakeneiden perhetiedot (perheside) </h3>

Maahanmuuttoviraston koostaman oleskelulupatietoja sisältävän aineiston rekisterinpitäjyys on siirtynyt Tilastokeskukselle, mikä tarkoittaa sitä, että aineistoa luvittaa tutkimuskäyttöön sekä tilastollisiin selvityksiin jatkossa Tilastokeskuksen tutkijapalvelut. Kyseisistä tiedoista on muodostettu viisi valmisaineistoa: MIGR_OLESK, MIGR_OPISK, MIGR_PERHE, MIGR_TYO ja MIGR_VOPAL, joiden kuvaukset löytyvät Taika-katalogista.

<b>MIGR_PERHE-valmisaineisto koostuu tauluista perheside ja siviilisääty. Tällä sivulla on aineistokuvaus taululle perheside. </b>

<b>Perheside</b>-tauluun haetaan aina viimeisin tieto sukulaisuussuhteesta, ja perusjoukkoon kuuluvien asiakkaiden sukulaisuussuhde päivitetään kuukausittain, mikäli heidän tietojaan on päivitetty edellisen kuukauden aikana. Mukana on myös asiakasnumeroita, jotka eivät kuulu perusjoukkoon. 

Aineistosta on suojattu yksilöivät tunnisteet ja poistettu suoran tunnistamisen mahdollisuus. Taulut linkittyvät toisiinsa pseudonymisoiduilla tunnisteilla. Tietojen laatu on vaihtelevaa, ja pyrimme kuvaamaan esiin nousseet puutteet aineiston käytön helpottamiseksi. Valmisaineiston sisältö on arkaluonteista, ja se luvitetaan tutkimuskäyttöön tai tilastollisiin selvityksiin vain hyvin perustein. Kaikilta MIGR-aineistoja käyttöönsä hakevilta vaaditaan DPIA eli tietosuojan vaikutusten arviointi. 

Aineiston päivämäärämuuttujat on karkeistettu kuukausitasolle, mutta tarpeen vaatiessa tarkemmat päivämäärät on mahdollista saada räätälöitynä. Valmisaineiston päivityssykli pyritään saamaan jopa kuukausitasolle, kunhan tietojen toimitusprosessi vakiintuu. Aineistoissa käytettäville id-muuttujille löytyy suomenkieliset luokitukset Fionan metatiedoista.

Valmisaineistossa on nyt tietoja vuodesta 2011 alkaen, ja tätä vanhempia tietoja on tarkoitus lisätä aineistoon vuonna 2026. Aikasarja katkeaa vuosien 2010 ja 2011 vaihteessa, sillä aiemmat tiedot ovat peräisin eri järjestelmästä kuin UMA:sta, ja mahdollisesti heikkolaatuisempia kuin vuodesta 2011 alkaen. Hankkeille luvitetaan tietoja vain niiltä vuosilta, joille hankkeella on tarvetta. Käytännössä MIGR-valmisaineistoissa vuosijaottelua ei ole mahdollista toteuttaa täydellisesti, vaan tiedot on jaoteltu vuotta 2011 edeltävään ja vuodesta 2011 alkavaan jaksoon. 

Oleskelulupa-aineisto on uutta Tilastokeskuksella, ja vasta kartutamme substanssiosaamistamme kyseiseen aiheeseen. Tästä syystä valmisaineistoihin voi tulla vielä käytettävyyttä parantavia muutoksia. Otamme mieluusti palautetta vastaan.

Viralliset oleskelulupahakemuksien ja -päätöksien tilastot laatii edelleen Maahanmuuttovirasto. Aihepiirin tilastoja voi tarkastella <a href="https://tilastot.migri.fi/" > Migrin tilastointipalvelusta</a>. 
Aiheeseen ja terminologiaan voi tutustua tarkemmin <a href="https://migri.fi/oleskelulupa" > Maahanmuuttoviraston sivuilla</a>.

Kysymykset valmisaineistosta ja koko tietosisällöstä voi osoittaa Tilastokeskuksen tutkijapalveluihin tutkijapalvelut@stat.fi.

## Variables (5)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `SHNRO` | Suojattu henkilönumero | — | — | — |
| `CUSTOMER_ID_s` | Suojattu asiakasnumero | — | — | — |
| `RELATED_CUSTOMER_ID_s` | Suojattu asiakkaan sukulaisen asiakasnumero | — | — | — |
| `PERSON_RELATIONSHIP_CODE` | Asiakkaan ja sukulaisen sukulaisuussuhde koodi | — | — | — |
| `MODIFICATION_DAY` | Sukulaissuhteen kirjaus tai paivityspvm | — | — | — |

### Variable definitions

#### `SHNRO` — Suojattu henkilönumero

Henkilönumero on poimittu niille joille se löytyy.

#### `CUSTOMER_ID_s` — Suojattu asiakasnumero

Asiakkaan yksilöivä tunniste, käytetään yhdistämään samalle asiakkaalle tehnyt muut asiat ja toimenpiteet.

#### `RELATED_CUSTOMER_ID_s` — Suojattu asiakkaan sukulaisen asiakasnumero

#### `PERSON_RELATIONSHIP_CODE` — Asiakkaan ja sukulaisen sukulaisuussuhde koodi

Koodit ovat selitetty auki taulussa relationship_code_to_name, joka löytyy metatiedoista. 
Jos muuttuja saa esim. arvon "Äiti", niin related_customer_id on customer_id:n äiti
.

#### `MODIFICATION_DAY` — Sukulaissuhteen kirjaus tai paivityspvm

---

[← Back to catalogue](../../README.md)
