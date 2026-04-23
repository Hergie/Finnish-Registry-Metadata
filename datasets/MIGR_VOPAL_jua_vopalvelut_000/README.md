# MIGR_VOPAL Oleskelulupaa hakeneiden vastaanottopalvelutiedot - vastaanottopalvelut

- **Identifier:** `MIGR_VOPAL_jua_vopalvelut_000.xml`
- **DOI:** `std_2025-05_2025-05-19_ain_0001`
- **Temporal coverage:** 2011-01-01 - 2025-12-31
- **Published:** 2026-04-07
- **Organisation:** Tilastokeskus
- **Variable count:** 8
- **Observation count:** —
- **Population:** Oleskelulupaa hakeneet

## Description

<h3>MIGR_VOPAL Oleskelulupaa hakeneiden vastaanottopalvelut (vastaanottopalvelut) </h3>

Maahanmuuttoviraston koostaman oleskelulupatietoja sisältävän aineiston rekisterinpitäjyys on siirtynyt Tilastokeskukselle, mikä tarkoittaa sitä, että aineistoa luvittaa tutkimuskäyttöön sekä tilastollisiin selvityksiin jatkossa Tilastokeskuksen tutkijapalvelut. Kyseisistä tiedoista on muodostettu viisi valmisaineistoa: MIGR_OLESK, MIGR_OPISK, MIGR_PERHE, MIGR_TYO ja MIGR_VOPAL, joiden kuvaukset löytyvät Taika-katalogista.

<b>MIGR_VOPAL -valmisaineisto koostuu tauluista vastaanottopalvelut ja vastaanottorahat. Tällä sivulla on aineistokuvaus taululle vastaanottopalvelut. </b>

<b>Vastaanottopalvelut</b>-taulun postinumeroista: Jos vastaanottokeskus on hajasijoitusmallin vastaanottokeskus, niin vastaanottokeskuksen osoitetieto on vastaanottokeskuksen asiointitoimiston osoite. Hajasijoitusmalli voi tarkoittaa esimerkiksi, että kaupunki, joka on vastaanottokeskusoperaattorina, ja on vuokrannut asuntoja (esim. omia vuokra-asuntojaan) eri puolilta kaupunkia. Postinumero on vastaanottokeskuksen viimeisin voimassa oleva postinumero, eikä tieto huomioi, jos sama keskus on toiminut eri osoitteissa eri aikoina. Postinumerotieto ei ole täysin luotettava, ja on sisältänyt virheellisesti esimerkiksi yritysten postinumeroita. Tällaiset postinumerot on karkeistettu tutkijapalveluiden toimesta aineistoon niin, että niiden tilalle on laitettu kyseisen alueen postinumero. Postitoimipaikka on johdettu postinumerosta. 

Vastaanottorahan saaminen ei kerro kattavasti, onko henkilö ollut kirjoilla vastaanottokeskuksessa, koska henkilö, joka saa vastaanottopalveluita ja käy töissä, ei ole oikeutettu vastaanottorahaan työstä saamansa palkan lisäksi. 

Valmisaineistosta on poistettu muuttuja accommodation_type, joka kertoo minkä tyyppisessä majoituksessa asiakas on majoittunut (esim perheryhmäkoti, säilö, tukiasunto, yksityismajoitus yms.), siitä syystä, ettei asiakkaan kotiosoitetta voitaisi päätellä valmisaineistosta. 

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
| `CUSTOMER_ID_s` | Suojattu asiakasnumero | — | — | — |
| `LODGING_DAY` | Majoituksen pvm | — | — | — |
| `AUTHORITY_UNIT_ID_s` | Suojattu operaattori_id | — | — | — |
| `AUTHORITY_OFFICE_ID_s` | Suojattu vastaanottokeskus_id | — | — | — |
| `ACCOMMODATION_TYPE` | Majoitustyyppi | — | — | — |
| `POSTAL_ADDRESS_NO` | Vastaanottokeskus_postinumero | — | — | — |
| `POSTAL_ADDRESS_AREA` | Vastaanottokeskus_postitoimipaikka | — | — | — |

### Variable definitions

#### `SHNRO` — Suojattu henkilönumero

#### `CUSTOMER_ID_s` — Suojattu asiakasnumero

Henkilön yksilöivä asiakasnumero Umassa

#### `LODGING_DAY` — Majoituksen pvm

Onko asiakas ollut kirjoilla vastaanottojärjestelmässä kyseisenä päivänä; kuun viimeinen päivä

#### `AUTHORITY_UNIT_ID_s` — Suojattu operaattori_id

Majoitusasiaan kirjauksen tehneen vastaanottokeskuksen operaattori (ylätaso)

#### `AUTHORITY_OFFICE_ID_s` — Suojattu vastaanottokeskus_id

Majoitusasiaan kirjauksen tehnyt vastaanottokeskus (alataso)

#### `ACCOMMODATION_TYPE` — Majoitustyyppi

Majoitustyyppi

#### `POSTAL_ADDRESS_NO` — Vastaanottokeskus_postinumero

Vastaanottokeskuksen (AUTHORITY_OFFICE_ID) viimeisin voimassa oleva postinumero. Ei osaa huomioida jos sama keskus on toiminut eri osoitteissa eri aikoina.

#### `POSTAL_ADDRESS_AREA` — Vastaanottokeskus_postitoimipaikka

Vastaanottokeskuksen (AUTHORITY_OFFICE_ID) viimeisin voimassa oleva postitoimipaikka. Ei osaa huomioida jos sama keskus on toiminut eri osoitteissa eri aikoina.

---

[← Back to catalogue](../../README.md)
