# MIGR_OLESK Oleskelulupatiedot - Kansalaisuuspäätökset

- **Identifier:** `MIGR_OLESK_jua_kanspaatos_000.xml`
- **DOI:** `std_2025-05_2025-05-19_ain_0001`
- **Temporal coverage:** 2011-01-01 - 2025-12-31
- **Published:** 2026-04-14
- **Organisation:** Tilastokeskus
- **Variable count:** 6
- **Observation count:** —
- **Population:** Oleskelulupaa hakeneet
- **Source:** Maahanmuuttoviraston (Migri) koostama oleskelulupatietoja sisältävä aineisto

## Description

MIGR_OLESK-valmisaineisto sisältää tietoja haetuista oleskeluluvista päätöksineen ja peruutuksineen sekä voimassa olevista kansalaisuuksista. 

Tämä aineistokuvaus koskee MIGR_OLESK-aineiston ”kansalaisuuspäätökset”-osiota, joka sisältää tietoja kansalaisuuden myöntämistä koskevista päätöksistä. MIGR_OLESK-aineistosta on erilliset kuvaukset myös osioille ”hakemukset”, ”päätökset ja peruutukset”, ”henkilötiedot”, ”voimassaolevat” sekä ”yhteystiedot”.

<b> Valmisaineiston tarkentava nimi </b> 
Oleskelulupahakemukset, -päätökset ja peruutukset, myönteiset kansalaisuuspäätökset ja voimassa olevat kansalaisuudet, sekä hakijoiden taustatiedot (MIGR_OLESK)

<b> Aineiston perusjoukko, koostaminen ja tietolähteet </b> 
Aineisto kattaa kaikki henkilöt, jotka ovat hakeneet lupaa oleskella Suomessa. Tämä käsittää niin oleskelulupaa, kansainvälistä suojelua kuin muuta oleskeluoikeutta hakeneet henkilöt.

Valmisaineisto perustuu Maahanmuuttoviraston koostamaan oleskelulupatietoja sisältävään aineistoon.

<b> Huomioitavaa aineistosta ja sen käytöstä </b> 
Aineistosta on suojattu yksilöivät tunnisteet ja poistettu suoran tunnistamisen mahdollisuus. Taulut linkittyvät toisiinsa pseudonymisoiduilla tunnisteilla asianumero, toimenpiteen numero, henkilönumero ja Migrin asiakasnumero. Aineistosta on karkeistettu piiloon arkaluontoisimmat oleskelulupahakemusten käsittelyperusteet. Tietojen laatu on vaihtelevaa, ja pyrimme kuvaamaan esiin nousseet puutteet aineiston käytön helpottamiseksi. Valmisaineiston sisältö on arkaluonteista, ja se luvitetaan tutkimuskäyttöön tai tilastollisiin selvityksiin vain hyvin perustein. Aineistoa käyttöönsä hakevien tutkimushankkeiden edellytetään laativan DPIA eli tietosuojan vaikutusten arviointi.

Oleskelulupatietoja sisältävä aineisto on uutta Tilastokeskuksella, ja vasta kartutamme substanssiosaamistamme kyseiseen aiheeseen. Tästä syystä valmisaineistoon voi tulla vielä käytettävyyttä parantavia muutoksia. 

<b> Aineiston päivitysaikataulu </b>  
Tutustu valmisaineistojen <a href="https://stat.fi/fi/palvelut/palvelut-tutkijoille/tutkimusaineistot/valmisaineistot/valmisaineistojen-paivitysaikataulu">  päivitysaikatauluun</a>. 

Aineiston päivityssykli pyritään saamaan kuukausitasolle, kunhan tietojen toimitusprosessi vakiintuu.

<b> Aineiston käyttö ja tilaaminen </b> 
Aineisto on tarkoitettu käytettäväksi FIONA-etäpalvelun kautta, ja se on linkitettävissä muihin henkilövalmisaineistoihin suojatun henkilötunnisteen avulla.

Valmisaineiston voi tilata tutkimuksen kohdejoukolle ja tarvittavalta ajanjaksolta. Kokonaisaineiston (kaikki muuttujat koko populaatiosta ja kaikilta saatavilla olevilta vuosilta) käyttöoikeus myönnetään vain, jos tutkimuksellinen tarve sitä erityisesti edellyttää. Lisäksi aineistosta voi tilata räätälöidyn version, joka sisältää vain osan muuttujista. 

<b> Tarkempaa tietoa muuttujista </b> 
Luokitusten koodistot sijaitsevat FIONAssa metadata-kansiossa (D:\metadata\classifications\migr).

<b> Lisätietoja </b> 
Kysymykset valmisaineistosta voi osoittaa Tilastokeskuksen tutkijapalveluihin tutkijapalvelut@stat.fi.

Viralliset oleskelulupahakemuksien ja -päätöksien tilastot laatii edelleen Maahanmuuttovirasto. Aihepiirin tilastoja voi tarkastella  <a href=" https://tilastot.migri.fi/#decisions ">  Migrin tilastointipalvelusta</a>. 
Aiheeseen ja terminologiaan voi tutustua tarkemmin <a href=" https://migri.fi/oleskelulupa">  Maahanmuuttoviraston sivuilla</a>.

## Variables (6)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `hid_e` | Suojattu henkilön yksilöivä tunniste | — | — | — |
| `CUSTOMER_ID_s` | Suojattu asiakasnumero | — | — | — |
| `TILASTOVUOSI` | — | — | — | — |
| `DCSN_MEASURE_CONFIRMATION_DAY` | Paatoksen pvm | — | — | — |
| `CASE_TYPE_NAME_FIN` | Asiatyyppi | — | — | — |
| `DCSN_TYPE_NAME_FIN` | Paatostyyppi | — | — | — |

### Variable definitions

#### `hid_e` — Suojattu henkilön yksilöivä tunniste

#### `CUSTOMER_ID_s` — Suojattu asiakasnumero

Asiakkaan yksilöivä tunniste, käytetään yhdistämään samalle asiakkaalle tehnyt muut asiat ja toimenpiteet.

#### `TILASTOVUOSI`

#### `DCSN_MEASURE_CONFIRMATION_DAY` — Paatoksen pvm

Päivämäärä jolloin henkilölle myönnetty Suomen kansalaisuus

#### `CASE_TYPE_NAME_FIN` — Asiatyyppi

case_type_name_fin case_type_id
EU oleskeluoikeus 63
Ensimmäistä oleskelulupaa koskeva hakemus 59
Jatkolupahakemus 60
Kiintiöpakolaisvalinta, UNHCR:n esitys, Humanitaarinen maahanmuutto, VN:n päätös 46
Oleskeluasema 532000
Oleskelutodistukset ja -ilmoitukset 83
Pitkäaikainen viisumi 488002
Pysyvää oleskelulupaa koskeva hakemus 61
Tilapäinen suojelu 48
Turvapaikkahakemus 49

#### `DCSN_TYPE_NAME_FIN` — Paatostyyppi

Vain ensimmäiset myönteiset päätökset

---

[← Back to catalogue](../../README.md)
