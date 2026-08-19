# EDUC_KOSKI_2ASTE -  Osaamisen_hankkimistapa

- **Identifier:** `EDUC_20182025_jua_koskitoinenosaamisenhankkimistapa_001.xml`
- **DOI:** `opiskt_2025-06_2025-06-16_ain_0001`
- **Temporal coverage:** —
- **Published:** 2025-11-13
- **Organisation:** Tilastokeskus
- **Variable count:** 11
- **Observation count:** —

## Description

EDUC_KOSKI-valmisaineisto sisältää OPH:n Koski-tietovarannon tietoja perusopetuksen, nivelvaiheen sekä toisen asteen koulutuksien läsnäolosta, sisällöstä sekä suorituksista. Aineiston avulla on mahdollista tutkia läsnäoloa koulutuksissa tarkalla tasolla, sillä aineisto sisältää jaksomuotoisen tilatiedon. Aineisto sisältää myös koulutuksien suoritustietoja, joiden avulla on mahdollista tutkia koulutuksien etenemistä tarkalla tasolla. Aineisto on kattavaa vuodesta 2020 lähtien. KOSKI-järjestelmä on otettu käyttöön vuonna 2018, mutta vuosien 2018 ja 2019 tiedot eivät ole kattavia. Aineistosta ei ole rajattu ulos aiempia tietoja.

Valmisaineisto on jaettu kolmeen moduuliin: suppea, perusopetus ja toinen aste.

Suppea moduuli sisältää opiskeluoikeus-taulun, sekä opiskeluoikeus_jakso-taulun. Opiskeluoikeus-taulu sisältää perustietoa opiskeluoikeuksista (koulutusmuoto, alkamis- ja paattymispaiva, oppilaitos, ammatillisen tutkinnon tutkintonimike, lukiokoulutuksen oppimäärä yms.), opiskeluoikeus_jakso-tauluun taas on eritelty opiskeluoikeuksien tilaa jaksomuotoisesti mahdollistaen opiskeluoikeuksien tilan tutkimisen päivän tarkkuudella. Kaksi laajempaa moduulia sisältää suppean moduulin tiedot, joten jos ottaa kaksi laajempaa moduulia ei suppeaa moduulia tarvita.

Perusopetuksen moduuli sisältää suppean moduulin taulut rajattuna nuoten perusopetuksen sekä aikuisten perusopetuksen opiskeluoikeuksiin. Lisäksi moduuli sisältää suoritustaulun, joka sisältää nuorten perusopetuksen vuosiluokkien sekä oppimäärän (päättötodistuksen) oppiaine-suoritukset. Lisäksi suoritustauluun sisältyy perusopetuksen lisäopetuksen (ns. 10. luokka) oppiaine-suoritukset. Aikuisten perusopetuksesta moduuliin sisältyy sekä oppiaine- että kurssisuoritukset omina tauluinaan.

Toisen asteen moduuli sisältää suppean moduulin taulut rajattuna toisen asteen ja nivelvaiheen koulutuksien opiskeluoikeuksiin. Lisäksi moduuli sisältää koulutusmuotokohtaisia tauluja.

Yleisiä huomioita:

- Kaikista moduuleista on rajattu ulos mitätöidyt opiskeluoikeudet sekä arkaluonteiset tiedot kuten oppimisen tukeen liittyvät tiedot.

- Sisältää myös lukiokoulutuksen aineopiskelijat, sekä ammatillisesta koulutuksesta muut kuin tutkintokoulutuksen opiskeluoikeudet. Tutkintoon johtavat koulutukset ovat rajattavissa opiskeluoikeus-taulun muuttujien koulutusmoduuli_koodisto ja suorituksen_tyyppi avulla.

- Perusopetuksen käyttäytymisen arvioinnit eivät sisälly valmisaineistoon, mutta ne ovat tilattavissa erikseen toimeksiantona.

- HUOM. Aineisto ei sisällä työhön ja itsenäiseen elämään valmentavaa koulutusta (TELMA) ja vapaan sivistystyön koulutuksia, eikä perusopetuksen aineopiskelijoiden suorituksia. Aineisto sisältää kuitenkin kansanopistojen vapaana sivistystyönä järjestämän oppivelvollisuuskoulutuksen (ns. opistovuosi oppivelvollisille).


Aineistoon on mahdollista tulla myöhemmin lisäyksiä, mikäli muille koulutusmuodoille tulee tarvetta, tai ilmenee tarve muuttujille, joita ei nykyiseen sisältöön kuulu.

Tilastokeskuksella on saatavilla OPH:n KOSKI-raporttikannan sisältö, joten jos jollekin tiedolle on tarvetta, mitä valmisaineistosta ei löydy, voi näitä tietoja pyytää erikseen toimeksiantona. Kuvaukset KOSKI-raporttikannan tiedoille löytyy OPH:n ylläpitämästä eduuni-wikistä (https://wiki.eduuni.fi/spaces/OPHPALV/pages/431685682/KOSKI-raporttikanta).


Laaja moduuli EDUC_KOSKI_2ASTE: osaamisen_hankkimistapa

Taulu sisältää jaksomuotoista tietoa ammatillisen koulutuksen osaamisen hankkimistavasta, sisältäen oppisopimuskoulutusjaksot, koulutussopimusjaksot sekä oppilaitosmuotoisen koulutuksen jaksot. Tauluun sisältyy mm. oppisopimuspaikan suojatun yritystunnus, kunta ja tieto oppisopimuksen purkamisesta koeajalla.
Sisältää tietoja KOSKEN osaamisen_hankkimistapa_ ammatillinen- taulusta.

Huom. Osaamisen_hankkimistapa-taulu ei sisällä tietoja aivan kaikista ennen ammatillisen koulutuksen reformia voimassa olleista opiskeluoikeuksista, opiskeluoikeus_jakso-taulun muuttuja oppisopimus_jossain_paatason_suorituksessa, mahdollistaa oppisopimuskoulutuksen erottelun näillekin koulutuksille.

## Variables (11)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `hid_e` | Suojattu henkilönumero | — | — | — |
| `opiskeluoikeus_oid_s` | suojattu opiskeluoikeuden tunniste | — | — | — |
| `oppisopimus_yrtun_s` | suojattu oppisopimus yritystunnus | — | — | — |
| `koulutussopimus_yrtun_s` | suojattu koulutussopimus yritystunnus | — | — | — |
| `aikajakso_tyyppi` | Aikajakso tyyppi | — | — | — |
| `alku` | Alku | — | — | — |
| `loppu` | Loppu | — | — | — |
| `os_purkamisen_pva` | oppisopimus purku paiva | — | — | — |
| `oppisopimus_purettu_koeajalla` | Oppisopimus purku koeajalla | — | — | — |
| `koulutussopimus_paikkakunta` | Koulutussopimuksen paikkakunta | — | — | — |
| `koulutussopimus_maa` | Koulutussopimus maa | — | — | — |

### Variable definitions

#### `hid_e` — Suojattu henkilönumero

Suojattu henkilönumero. Tilastokeskuksessa yhtenäisesti suojattu henkilö-id mahdollistaa henkilöä koskevien tietojen yhdistämisen eri aineistojen ja vuosien välillä.

#### `opiskeluoikeus_oid_s` — suojattu opiskeluoikeuden tunniste

Suojattu opiskeluoikeuden tunniste.

#### `oppisopimus_yrtun_s` — suojattu oppisopimus yritystunnus

Suojattu oppisopimukseen liittyvän toimijan yritystunnus.

#### `koulutussopimus_yrtun_s` — suojattu koulutussopimus yritystunnus

Suojattu koulutussopimukseen liittyvän toimijan yritystunnus.

#### `aikajakso_tyyppi` — Aikajakso tyyppi

Kertoo, onko kyseessä koulutusopimus- vai oppisopimus-jakso.

#### `alku` — Alku

Jakson alkupäivä.

#### `loppu` — Loppu

Jakson päättymispäivä.

#### `os_purkamisen_pva` — oppisopimus purku paiva

Päivä, jolloin oppisopimus on purettu.

#### `oppisopimus_purettu_koeajalla` — Oppisopimus purku koeajalla

Tieto, onko oppisopimus purettu koeajalla.

#### `koulutussopimus_paikkakunta` — Koulutussopimuksen paikkakunta

Paikkakunta, jossa koulutussopimukseen kuuluva työssäoppiminen on tapahtunut.
Relevantti tieto vain koulutussopimuksissa (= jos aikajakson tyyppi on 'koulutussopimus').

Käytettävä koodisto: https://opintopolku.fi/koski/dokumentaatio/koodisto/kunta/latest.

#### `koulutussopimus_maa` — Koulutussopimus maa

Maa, jossa koulutussopimukseen kuuluva työssäoppiminen on tapahtunut.
Relevantti tieto vain koulutussopimuksissa (= jos aikajakson tyyppi on 'koulutussopimus').

Käytettävä koodisto: https://opintopolku.fi/koski/dokumentaatio/koodisto/maatjavaltiot2/latest.

---

[← Back to catalogue](../../README.md)
