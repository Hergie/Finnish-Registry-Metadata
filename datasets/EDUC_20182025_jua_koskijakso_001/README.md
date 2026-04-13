# EDUC_KOSKI - Opiskeluoikeus_jakso

- **Identifier:** `EDUC_20182025_jua_koskijakso_001.xml`
- **DOI:** `opiskt_2025-06_2025-06-16_ain_0001`
- **Temporal coverage:** —
- **Published:** 2025-11-13
- **Organisation:** Tilastokeskus
- **Variable count:** 11
- **Observation count:** —

## Kuvaus / Description

EDUC_KOSKI-valmisaineisto sisältää OPH:n Koski-tietovarannon tietoja perusopetuksen, nivelvaiheen sekä toisen asteen koulutuksien läsnäolosta, sisällöstä sekä suorituksista. Aineiston avulla on mahdollista tutkia läsnäoloa koulutuksissa tarkalla tasolla, sillä aineisto sisältää jaksomuotoisen tilatiedon. Aineisto sisältää myös koulutuksien suoritustietoja, joiden avulla on mahdollista tutkia koulutuksien etenemistä tarkalla tasolla. Aineisto on kattavaa vuodesta 2020 lähtien. KOSKI-järjestelmä on otettu käyttöön vuonna 2018, mutta vuosien 2018 ja 2019 tiedot eivät ole kattavia. Aineistosta ei ole rajattu ulos aiempia tietoja. 

Valmisaineisto on jaettu kolmeen moduuliin: suppea, perusopetus ja toinen aste. 

Suppea moduuli sisältää opiskeluoikeus-taulun, sekä opiskeluoikeus_jakso-taulun. Opiskeluoikeus-taulu sisältää perustietoa opiskeluoikeuksista (koulutusmuoto, alkamis- ja paattymispaiva, oppilaitos, ammatillisen tutkinnon tutkintonimike, lukiokoulutuksen oppimäärä yms.), opiskeluoikeus_jakso-tauluun taas on eritelty opiskeluoikeuksien tilaa jaksomuotoisesti mahdollistaen opiskeluoikeuksien tilan tutkimisen päivän tarkkuudella. Kaksi laajempaa moduulia sisältää suppean moduulin tiedot, joten jos ottaa kaksi laajempaa moduulia ei suppeaa moduulia tarvita. 

Perusopetuksen moduuli sisältää suppean moduulin taulut rajattuna perusopetuksen opiskeluoikeuksiin. Lisäksi moduuli sisältää suoritustaulun, joka sisältää perusopetuksen vuosiluokkien sekä oppimäärän (päättötodistuksen) oppiaine-suoritukset. Lisäksi suoritustauluun sisältyy perusopetuksen lisäopetuksen (ns. 10. luokka) oppiaine-suoritukset. 

Toisen asteen moduuli sisältää suppean moduulin taulut rajattuna toisen asteen ja nivelvaiheen koulutuksien opiskeluoikeuksiin. Lisäksi moduuli sisältää koulutusmuotokohtaisia tauluja. 
 
Yleisiä huomioita: 

- Kaikista moduuleista on rajattu ulos mitätöidyt opiskeluoikeudet sekä arkaluonteiset tiedot kuten oppimisen tukeen liittyvät tiedot.

- Sisältää myös lukiokoulutuksen aineopiskelijat, sekä ammatillisesta koulutuksesta muut kuin tutkintokoulutuksen opiskeluoikeudet. Tutkintoon johtavat koulutukset ovat rajattavissa opiskeluoikeus-taulun muuttujien koulutusmoduuli_koodisto ja suorituksen_tyyppi avulla. 

- Perusopetuksen käyttäytymisen arvioinnit eivät sisälly valmisaineistoon, mutta ne ovat tilattavissa erikseen toimeksiantona.

-Aineisto ei sisällä DIA- ja EB-tutkinnon opiskelijoita, eikä Helsingin kansainvälisen koulutuksen, tai Helsingin eurooppalaisen koulun opiskelijoita.

- HUOM. Aineisto ei sisällä aikuisten perusopetusta, työhön ja itsenäiseen elämään valmentavaa koulutusta (TELMA) ja vapaan sivistystyön koulutuksia, eikä perusopetuksen aineopiskelijoiden suorituksia. Aineisto sisältää kuitenkin kansanopistojen vapaana sivistystyönä järjestämän oppivelvollisuuskoulutuksen (ns. opistovuosi oppivelvollisille).


Aineistoon on mahdollista tulla myöhemmin lisäyksiä, mikäli muille koulutusmuodoille tulee tarvetta, tai ilmenee tarve muuttujille, joita ei nykyiseen sisältöön kuulu. 
 
Tilastokeskuksella on saatavilla OPH:n KOSKI-raporttikannan sisältö, joten jos jollekin tiedolle on tarvetta, mitä valmisaineistosta ei löydy, voi näitä tietoja pyytää erikseen toimeksiantona. Kuvaukset KOSKI-raporttikannan tiedoille löytyy OPH:n ylläpitämästä eduuni-wikistä (https://wiki.eduuni.fi/spaces/OPHPALV/pages/431685682/KOSKI-raporttikanta). 


Suppea moduuli EDUC_KOSKI_JAKSOT, opiskeluoikeus_jakso:
Sisältää koski-tietovarannon jaksomuotoisen tiedon opiskeluoikeuksien tilasta ja opintojen rahoituksesta.
Yhdistää tietoja KOSKI raporttikannan tauluista: r_opiskeluoikeus, r_opiskeluoikeus_aikajakso, r_henkilo.

HUOM. Perusopetuksessa on jonkin verran voimassa olevia opiskeluoikeuksia, jotka näkyvät läsnä olevana Koski-datassa, mutta eivät ole suorittaneet varsinaisesti mitään. Tällaisia tapauksia ei ole opiskeluoikeus_jakso-taulusta (tai opiskeluoikeus-taulusta) siivottu pois.

## Muuttujat / Variables (11)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `shnro` | Suojattu henkilönumero | — | — | — |
| `oppija_oid_s` | Suojattu oppijatunnus | — | — | — |
| `opiskeluoikeus_oid_s` | Suojattu opiskeluoikeuden tunniste | — | — | — |
| `sis_opiskeluoikeuteen_oid_s` | sisaltyy_opiskeluoikeuteen_oid_s | — | — | — |
| `koulutusmuoto` | koulutusmuoto | — | — | — |
| `alku` | Tilajakson alkupäivä | — | — | — |
| `loppu` | Tilajakson loppupäivä | — | — | — |
| `tila` | Tila | — | — | — |
| `opintojen_rahoitus` | opintojen rahoitus | — | — | — |
| `tila_alkanut` | tila alkanut | — | — | — |
| `oppisopimus_paatason_suoritukses` | oppisopimus jossain paatason suorituksessa | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `shnro` — Suojattu henkilönumero

Suojattu henkilönumero

#### `oppija_oid_s` — Suojattu oppijatunnus

Suojattu OPH:n oppijatunnus

#### `opiskeluoikeus_oid_s` — Suojattu opiskeluoikeuden tunniste

Suojattu OPH:n opiskeluoikeuden tunniste

#### `sis_opiskeluoikeuteen_oid_s` — sisaltyy_opiskeluoikeuteen_oid_s

Suojattu OPH:n opiskeluoikeuden tunniste, joissain tapauksissa opiskeluoikeuden toimija ostaa koulutuksen toiselta koulutustoimijalta, näissä tapauksissa linkki opiskeluoikeuksien väliltä löytyy tästä kentästä. ks. tarkemmat lisätiedot OPH:n eduuni-wikistä (https://wiki.eduuni.fi/spaces/OPHPALV/pages/431685903/r_opiskeluoikeus)

#### `koulutusmuoto` — koulutusmuoto

Huom. ammatilliseen koulutukseen kuuluu monta eri tyyppistä koulutusta (tutkintokoulutuksen lisäksi esim. valma-koulutus), joten niiden tunnistamiseen täytyy lisäksi käyttää suorituksen_tyyppi-kenttää

#### `alku` — Tilajakson alkupäivä

#### `loppu` — Tilajakson loppupäivä

#### `tila` — Tila

Opiskeluoikeuden tila rivin kuvaaman aikajakson aikana.

#### `opintojen_rahoitus` — opintojen rahoitus

Tieto siitä, mikä rahoitusmuoto opinnoilla on ollut rivin kuvaaman aikajakson aikana. Käytettävä koodisto: https://opintopolku.fi/koski/dokumentaatio/koodisto/opintojenrahoitus/latest. Huomio: opintojen_rahoitus='14' tarkoittaa jotpa-rahoitettuja opintoja

#### `tila_alkanut` — tila alkanut

Huomio: jos opiskelijalla on useita peräkkäisiä saman tilan jaksoja, tässä kentässä näkyy näistä ensimmäisen alkamispäivä

#### `oppisopimus_paatason_suoritukses` — oppisopimus jossain paatason suorituksessa

Tieto siitä, jos oppija on ollut oppisopimusmuotoisessa koulutuksessa rivin kuvaaman aikajakson aikana. Relevantti ammatillisen koulutuksen opiskeluoikeuksissa.

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
