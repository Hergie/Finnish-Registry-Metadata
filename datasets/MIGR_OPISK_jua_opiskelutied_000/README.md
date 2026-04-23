# MIGR_OPISK Oleskelulupaa hakeneiden opiskelutiedot

- **Identifier:** `MIGR_OPISK_jua_opiskelutied_000.xml`
- **DOI:** `std_2025-05_2025-05-19_ain_0001`
- **Temporal coverage:** 2011-01-01 - 
- **Published:** 2026-02-10
- **Organisation:** Tilastokeskus
- **Variable count:** 8
- **Observation count:** —
- **Population:** Oleskelulupaa hakeneet

## Description

<h3>MIGR_OPISK Oleskelulupaa hakeneiden opiskelutiedot </h3>

Maahanmuuttoviraston koostaman oleskelulupatietoja sisältävän aineiston rekisterinpitäjyys on siirtynyt Tilastokeskukselle, mikä tarkoittaa sitä, että aineistoa luvittaa tutkimuskäyttöön sekä tilastollisiin selvityksiin jatkossa Tilastokeskuksen tutkijapalvelut. Kyseisistä tiedoista on muodostettu viisi valmisaineistoa: MIGR_OLESK, MIGR_OPISK, MIGR_PERHE, MIGR_TYO ja MIGR_VOPAL, joiden kuvaukset löytyvät Taika-katalogista.

<b>MIGR_OPISK</b>-valmisaineiston tiedot ovat suhteellisen heikkolaatuista. Kyseessä on asiakkaan itse ilmoittama tieto, ja verraten esim. rekisteripohjaiseen tietoon kuten KOSKI-aineistot, tiedot eivät ole yhtä kattavia. 

Tiedot lisätään hakemukselle vain kerran. Siispä jos hakija on esim. vaihtanut koulutusohjelmaa opiskelujen aikana, ja ilmoittanut siitä, tietoa ei enää päivitetä hakemukselle. Opiskelutiedot listataan vasta, kun asiaan on tehty päätös. Opiskelutiedot lisätään vain opiskelijan hakemuksille. Tähän aineistoon on otettu mukaan seuraavat käsittelyperusteet: Ilmoitus opiskelijan liikkumisesta, EU-kansalaisen rekisteröinti, opiskelu. Näihin perusteisiin voidaan lisätä opiskelutiedot, mutta se ei ole pakollista. 

Oppilaitoksen suojattu koodi edu_institute_id_s on Maahanmuuttoviraston oman luokituksen mukainen oppilaitoksen koodi, eikä se linkity mistään muista valmisaineistoista löytyviin oppilaitostunnuksiin. 

Aineistosta on suojattu yksilöivät tunnisteet ja poistettu suoran tunnistamisen mahdollisuus. Taulut linkittyvät toisiinsa pseudonymisoiduilla tunnisteilla. Tietojen laatu on vaihtelevaa, ja pyrimme kuvaamaan esiin nousseet puutteet aineiston käytön helpottamiseksi. Valmisaineiston sisältö on arkaluonteista, ja se luvitetaan tutkimuskäyttöön tai tilastollisiin selvityksiin vain hyvin perustein. Kaikilta MIGR-aineistoja käyttöönsä hakevilta vaaditaan DPIA eli tietosuojan vaikutusten arviointi. 

Aineiston päivämäärämuuttujat on karkeistettu kuukausitasolle, mutta tarpeen vaatiessa tarkemmat päivämäärät on mahdollista saada räätälöitynä. Valmisaineiston päivityssykli pyritään saamaan jopa kuukausitasolle, kunhan tietojen toimitusprosessi vakiintuu. Aineistoissa käytettäville id-muuttujille löytyy suomenkieliset luokitukset Fionan metatiedoista.

Valmisaineistossa on nyt tietoja vuodesta 2011 alkaen, ja tätä vanhempia tietoja on tarkoitus lisätä aineistoon vuonna 2026. Aikasarja katkeaa vuosien 2010 ja 2011 vaihteessa, sillä aiemmat tiedot ovat peräisin eri järjestelmästä kuin UMA:sta, ja mahdollisesti heikkolaatuisempia kuin vuodesta 2011 alkaen. Hankkeille luvitetaan tietoja vain niiltä vuosilta, joille hankkeella on tarvetta. Käytännössä MIGR-valmisaineistoissa vuosijaottelua ei ole mahdollista toteuttaa täydellisesti, vaan tiedot on jaoteltu vuotta 2011 edeltävään ja vuodesta 2011 alkavaan jaksoon. 

Oleskelulupa-aineisto on uutta Tilastokeskuksella, ja vasta kartutamme substanssiosaamistamme kyseiseen aiheeseen. Tästä syystä valmisaineistoihin voi tulla vielä käytettävyyttä parantavia muutoksia. Otamme mieluusti palautetta vastaan.

Viralliset oleskelulupahakemuksien ja -päätöksien tilastot laatii edelleen Maahanmuuttovirasto. Aihepiirin tilastoja voi tarkastella <a href="https://tilastot.migri.fi/" > Migrin tilastointipalvelusta</a>. 
Aiheeseen ja terminologiaan voi tutustua tarkemmin <a href="https://migri.fi/oleskelulupa" > Maahanmuuttoviraston sivuilla</a>.

Kysymykset valmisaineistosta ja koko tietosisällöstä voi osoittaa Tilastokeskuksen tutkijapalveluihin tutkijapalvelut@stat.fi.

## Variables (8)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `SHNRO` | Suojattu henkilönumero | — | — | — |
| `CASE_ID_s` | Suojattu asianumero | — | — | — |
| `CUSTOMER_ID_s` | Suojattu asiakasnumero | — | — | — |
| `ACADEM_DEGREE_ID` | Tavoitetutkinnon koodi | — | — | — |
| `EDU_INSTITUTE_ID_s` | Suojattu oppilaitos koodi | — | — | — |
| `MUNICIPALITY_ID` | Paikkakunnan koodi | — | — | — |
| `STUDY_NATURE_ID` | Opiskelun luonne koodi | — | — | — |
| `STUDY_LANG_ID` | Opiskelukieli koodi | — | — | — |

### Variable definitions

#### `SHNRO` — Suojattu henkilönumero

#### `CASE_ID_s` — Suojattu asianumero

#### `CUSTOMER_ID_s` — Suojattu asiakasnumero

#### `ACADEM_DEGREE_ID` — Tavoitetutkinnon koodi

Koodi
25000	Ylempi korkeakoulututkinto
25001	Alempi korkeakoulututkinto
25002	Muu
25003	Keskiasteen tutkinto
25004	Ylioppilastutkinto
25005	Ammattitutkinto

#### `EDU_INSTITUTE_ID_s` — Suojattu oppilaitos koodi

Koodi

#### `MUNICIPALITY_ID` — Paikkakunnan koodi

Opiskelupaikkakunnan koodi. Koodien luokitukset löytyvät metatiedoista taulusta municipality_id_to_name. Kyseinen luokitus on Maahanmuuttoviraston oma luokitus, eikä täten linkity muista valmisaineistoista löytyviin paikkakuntien luokituksiin.

#### `STUDY_NATURE_ID` — Opiskelun luonne koodi

Koodi
	
27805	Muu ei tutkintoon johtava opiskelu
27806	Suomesta saatava erityiskoulutus
27807	Täydennysopiskelu
27808	Tutkinto-opiskelu
27809	Vaihto-opiskelu

#### `STUDY_LANG_ID` — Opiskelukieli koodi

Koodi
27681	Venäjä
27682	Englanti
27683	Ruotsi
27684	Suomi
27685	Muu

---

[← Back to catalogue](../../README.md)
