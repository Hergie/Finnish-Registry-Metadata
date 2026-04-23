# MIGR_TYO Oleskelulupaa hakeneiden työskentelytiedot - osapäätökset

- **Identifier:** `MIGR_TYO_jua_osapaatokset_000.xml`
- **DOI:** `std_2025-05_2025-05-19_ain_0001`
- **Temporal coverage:** 2011-01-01 - 2024-12-31
- **Published:** 2026-04-07
- **Organisation:** Tilastokeskus
- **Variable count:** 14
- **Observation count:** —
- **Population:** Oleskelulupaa hakeneet

## Description

<h3>MIGR_TYO Oleskelulupaa hakeneiden työskentelytiedot (osapäätökset) </h3>

Maahanmuuttoviraston koostaman oleskelulupatietoja sisältävän aineiston rekisterinpitäjyys on siirtynyt Tilastokeskukselle, mikä tarkoittaa sitä, että aineistoa luvittaa tutkimuskäyttöön sekä tilastollisiin selvityksiin jatkossa Tilastokeskuksen tutkijapalvelut. Kyseisistä tiedoista on muodostettu viisi valmisaineistoa: MIGR_OLESK, MIGR_OPISK, MIGR_PERHE, MIGR_TYO ja MIGR_VOPAL, joiden kuvaukset löytyvät Taika-katalogista.

<b>MIGR_TYO -valmisaineisto koostuu tauluista työehdot ja osapäätökset. Tällä sivulla on aineistokuvaus taululle osapäätökset. </b>

<b>Osapäätökset</b>-taulu sisältää tietoja vain vuosille 2011-2024, <b>eikä tämä taulu tule enää päivittymään</b>. Tämä johtuu siitä, että työperäisissä hakemuksissa ei tehdä enää osapäätöksiä. Prosessi on jatkossa osa Migrin normaalia käsittelyä, eikä sisällä enää erillistä TE-keskuksen tekemää osapäätös-toimenpidettä.

Aineistosta on suojattu yksilöivät tunnisteet ja poistettu suoran tunnistamisen mahdollisuus. Taulut linkittyvät toisiinsa pseudonymisoiduilla tunnisteilla. Tietojen laatu on vaihtelevaa, ja pyrimme kuvaamaan esiin nousseet puutteet aineiston käytön helpottamiseksi. Valmisaineiston sisältö on arkaluonteista, ja se luvitetaan tutkimuskäyttöön tai tilastollisiin selvityksiin vain hyvin perustein. Kaikilta MIGR-aineistoja käyttöönsä hakevilta vaaditaan DPIA eli tietosuojan vaikutusten arviointi. 

Aineiston päivämäärämuuttujat on karkeistettu kuukausitasolle, mutta tarpeen vaatiessa tarkemmat päivämäärät on mahdollista saada räätälöitynä. Valmisaineiston päivityssykli pyritään saamaan jopa kuukausitasolle, kunhan tietojen toimitusprosessi vakiintuu. Aineistoissa käytettäville id-muuttujille löytyy suomenkieliset luokitukset Fionan metatiedoista.

Valmisaineistossa on nyt tietoja vuodesta 2011 alkaen, ja tätä vanhempia tietoja on tarkoitus lisätä aineistoon vuonna 2026. Aikasarja katkeaa vuosien 2010 ja 2011 vaihteessa, sillä aiemmat tiedot ovat peräisin eri järjestelmästä kuin UMA:sta, ja mahdollisesti heikkolaatuisempia kuin vuodesta 2011 alkaen. Hankkeille luvitetaan tietoja vain niiltä vuosilta, joille hankkeella on tarvetta. Käytännössä MIGR-valmisaineistoissa vuosijaottelua ei ole mahdollista toteuttaa täydellisesti, vaan tiedot on jaoteltu vuotta 2011 edeltävään ja vuodesta 2011 alkavaan jaksoon. 

Oleskelulupa-aineisto on uutta Tilastokeskuksella, ja vasta kartutamme substanssiosaamistamme kyseiseen aiheeseen. Tästä syystä valmisaineistoihin voi tulla vielä käytettävyyttä parantavia muutoksia. Otamme mieluusti palautetta vastaan.

Viralliset oleskelulupahakemuksien ja -päätöksien tilastot laatii edelleen Maahanmuuttovirasto. Aihepiirin tilastoja voi tarkastella <a href="https://tilastot.migri.fi/" > Migrin tilastointipalvelusta</a>. 
Aiheeseen ja terminologiaan voi tutustua tarkemmin <a href="https://migri.fi/oleskelulupa" > Maahanmuuttoviraston sivuilla</a>.

Kysymykset valmisaineistosta ja koko tietosisällöstä voi osoittaa Tilastokeskuksen tutkijapalveluihin tutkijapalvelut@stat.fi.

## Variables (14)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `Shnro` | Suojattu hnro | — | — | — |
| `DCSN_DATA_OCCUPATION_ID_s` | Osapaatoksen lisatty ammattialan yksilollinen suojattu tunnus | — | — | — |
| `MEASURE_ID_s` | Suojattu paatosnumero | — | — | — |
| `CASE_ID_s` | Suojattu asianumero | — | — | — |
| `CUSTOMER_ID_s` | Suojattu asiakasnumero | — | — | — |
| `TILASTOVUOSI` | — | — | — | — |
| `TILASTOKUUKAUSI` | — | — | — | — |
| `OCCUPATION_FIELD_ID` | Ammattialan koodi | — | — | — |
| `IS_EMPLOYER_SPECIFIC` | Onko lupa tyonantajakohtainen | — | — | — |
| `TEM_MEASURE_CONF_MONTH` | Osapaatoksen vahvistusajankohdan kuukausi | — | — | — |
| `AUTHORITY_UNIT` | Yksikko | — | — | — |
| `AUTHORITY_OFFICE` | Toimisto | — | — | — |
| `TEM_DCSN_TYPE` | Osaratkaisun tyyppi | — | — | — |
| `TEM_DCSN_GROUNDS` | Osaratkaisun peruste | — | — | — |

### Variable definitions

#### `Shnro` — Suojattu hnro

#### `DCSN_DATA_OCCUPATION_ID_s` — Osapaatoksen lisatty ammattialan yksilollinen suojattu tunnus

Te-toimiston Osapäätöksen yksilöllinen tunnus. Osapäätökseen voi liittyä useampia ammattiala, tällaisia tilanteita ovat jossa henkilön työsopimuksessa on merkitty useampi työtehävä samalla työnantajalla. Tällöin dcsn_data_occupation_id on uniikki id. Measure id:n avulla voidaan tunnistaa samaan osapäätökseen lisätyt ammattiala.

#### `MEASURE_ID_s` — Suojattu paatosnumero

#### `CASE_ID_s` — Suojattu asianumero

#### `CUSTOMER_ID_s` — Suojattu asiakasnumero

#### `TILASTOVUOSI`

#### `TILASTOKUUKAUSI`

#### `OCCUPATION_FIELD_ID` — Ammattialan koodi

Ammattialan koodi. Ammattialan nimi löytyy taulusta OCCUPATION_FIELD_ID_TO_NAME. 
Nämä ammattiluokitukset ovat Migrin toimittaman luokituksen mukaisia, eivätkä täten linkkaannu muihin ammattiluokituksiin.

#### `IS_EMPLOYER_SPECIFIC` — Onko lupa tyonantajakohtainen

Joissain tapauksissa oleskelulupa voidaan myöntää vain yhdellä työnantajalla työskentelemistä varten. Näissä tapauksissa ammattialatieto saattaa puuttua.

#### `TEM_MEASURE_CONF_MONTH` — Osapaatoksen vahvistusajankohdan kuukausi

#### `AUTHORITY_UNIT` — Yksikko

Osapäätöksen vahvistaneen työntekijän organisaatiotieto; ylätaso

#### `AUTHORITY_OFFICE` — Toimisto

Osapäätöksen vahvistaneen työntekijän organisaatiotieto; alataso

#### `TEM_DCSN_TYPE` — Osaratkaisun tyyppi

Esimerkiksi myönteinen tai kielteinen

#### `TEM_DCSN_GROUNDS` — Osaratkaisun peruste

Esimerkiksi Saatavuusharkinta tai Myönt: Yrittäjä

---

[← Back to catalogue](../../README.md)
