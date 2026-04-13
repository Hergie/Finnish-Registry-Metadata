# EDUC_KOSKI - Perusopetus

- **Identifier:** `EDUC_20182025_jua_koskiperus_001.xml`
- **DOI:** `opiskt_2025-06_2025-06-16_ain_0001`
- **Temporal coverage:** —
- **Published:** 2025-11-13
- **Organisation:** Tilastokeskus
- **Variable count:** 21
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


Laaja moduuli EDUC_KOSKI_PERUSOPETUS: Perusopetuksen suoritukset

Taulu sisältää tietoa perusopetuksen vuosiluokkien sekä oppimäärän oppiainesuorituksista (arvosana, laajuus, oppiaine yms), sekä perusopetuksen lisäopetuksen (ns. 10. luokan) oppiainesuorituksista.
Yhdistää tietoja KOSKI raporttikannan tauluista: r_opiskeluoikeus, r_paatason_suoritus, r_osasuoritus, r_henkilo.

## Muuttujat / Variables (21)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `shnro` | Suojattu henkilönumero | — | — | — |
| `oppija_oid_s` | Suojattu oppijatunnus | — | — | — |
| `opiskeluoikeus_oid_s` | Suojattu opiskeluoikeuden tunniste | — | — | — |
| `oppilaitos_oid_s` | Suojattu oppilaitoksen tunniste | — | — | — |
| `oppilaitosnumero_s` | Suojattu oppilaitosnumero | — | — | — |
| `oppilaitos_kotipaikka` | Oppilaitoksen kotikunta | — | — | — |
| `toimipiste_oid_s` | Suojattu toimipisteen tunniste | — | — | — |
| `vuosiluokka` | Oppiaine-suorituksen vuosiluokka | — | — | — |
| `oppiaine` | Oppiaineen tunniste | — | — | — |
| `oppiaine_koodisto` | oppiaineen koodisto | — | — | — |
| `arviointi_arvosana_koodiarvo` | oppiaine-suorituksen arvosana | — | — | — |
| `arviointi_arvosana_koodisto` | arvosanan koodisto | — | — | — |
| `vahvistus_paiva` | Vahvistus päivä | — | — | — |
| `koulutusmoduuli_pakollinen` | Koulutusmoduuli pakollinen | — | — | — |
| `koulutusmoduuli_paikallinen` | Koulutusmoduuli paikallinen | — | — | — |
| `koulutusmoduuli_kieliaine_nimi` | Koulutusmoduuli kieliaine nimi | — | — | — |
| `koulutusmoduuli_laajuus_arvo` | Koulutusmoduuli laajuus arvo | — | — | — |
| `koulutusmoduuli_laajuus_yksikko` | Koulutusmoduuli laajuus yksikkö | — | — | — |
| `luokka` | Luokka | — | — | — |
| `paataso_suorituksen_tyyppi` | Päätaso suorituksen tyyppi | — | — | — |
| `suorituksen_tyyppi` | Suorituksen tyyppi | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `shnro` — Suojattu henkilönumero

Suojattu henkilönumero

#### `oppija_oid_s` — Suojattu oppijatunnus

Suojattu OPH:n oppijatunnus

#### `opiskeluoikeus_oid_s` — Suojattu opiskeluoikeuden tunniste

Suojattu OPH:n opiskeluoikeuden tunniste

#### `oppilaitos_oid_s` — Suojattu oppilaitoksen tunniste

Suojattu oppilaitoksen tunniste

#### `oppilaitosnumero_s` — Suojattu oppilaitosnumero

Suojattu oppilaitosnumero

#### `oppilaitos_kotipaikka` — Oppilaitoksen kotikunta

Oppilaitoksen kotikunnan kuntakoodi

#### `toimipiste_oid_s` — Suojattu toimipisteen tunniste

Suojattu toimipisteen tunniste

#### `vuosiluokka` — Oppiaine-suorituksen vuosiluokka

Kertoo kyseisen oppiaine-suorituksen vuosiluokan. HUOM. laskettu muuttuja. Jos päätason suoritus on tyyppiä perusopetuksenvuosiluokka, haetaan arvo suoraan kyseisestä suorituksesta. Jos taas päätason suoritus on tyyppiä perusopetuksenoppimaara, sijoitetaan näille oppiaineille muuttujaan arvo '9'. Jos kyseessä on perusopetuksen lisäopetuksen suoritus, sijoitetaan tähän kenttää arvo '10'.

#### `oppiaine` — Oppiaineen tunniste

#### `oppiaine_koodisto` — oppiaineen koodisto

Koodisto, josta oppiaineen tunniste löytyy. Jos kyseessä paikallinen suoritus (koulutusmoduuli_paikallinen='t'), niin koodisto on tyhjä

#### `arviointi_arvosana_koodiarvo` — oppiaine-suorituksen arvosana

#### `arviointi_arvosana_koodisto` — arvosanan koodisto

Dokumentaatio - Koodistot - Koski - Opintopolku.fi (https://opintopolku.fi/koski/dokumentaatio/koodistot).

#### `vahvistus_paiva` — Vahvistus päivä

Päivä, jolloin vuosiluokka-/oppimäärä-suoritus, johon oppiaine kuuluu on vahvistettu. Oppiaine-suorituksilla ei yleensä omaa arviointi_paivaa, käytetään siksi vastaavan päätason suorituksen vahvistus_paiva-muuttujaa

#### `koulutusmoduuli_pakollinen` — Koulutusmoduuli pakollinen

Tieto siitä, onko oppiaine pakollinen suoritettavassa koulutuksessa.

#### `koulutusmoduuli_paikallinen` — Koulutusmoduuli paikallinen

Tieto siitä, onko oppiaine paikallisen opintosuunnitelman mukainen

#### `koulutusmoduuli_kieliaine_nimi` — Koulutusmoduuli kieliaine nimi

Tieto opiskeltavasta kielestä

#### `koulutusmoduuli_laajuus_arvo` — Koulutusmoduuli laajuus arvo

Oppiaineen laajuuden arvo

#### `koulutusmoduuli_laajuus_yksikko` — Koulutusmoduuli laajuus yksikkö

Oppiaineen laajuuden yksikkö

#### `luokka` — Luokka

Tieto oppijan luokasta. Purettu päätason suorituksen data-kentästä, muuttuja ei ole kattava.

#### `paataso_suorituksen_tyyppi` — Päätaso suorituksen tyyppi

Päätason suorituksen tyyppi siinä päätason suorituksessa johon oppiaine-rivi sisältyy. Päättötodistuksen arvosanat saa eroteltua tämän kentän arvolla 'perusopetuksenoppimaara', perusopetuksen lisäopetuksen taas arvolla 'perusopetuksenlisaopetus'.

#### `suorituksen_tyyppi` — Suorituksen tyyppi

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
