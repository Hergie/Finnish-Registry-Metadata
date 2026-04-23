# EDUC_KOSKI TOINEN ASTE - ammatillinen_suoritukset

- **Identifier:** `EDUC_20182025_jua_koskitoinenammatillinensuoritukset_001.xml`
- **DOI:** `opiskt_2025-06_2025-06-16_ain_0001`
- **Temporal coverage:** —
- **Published:** 2025-11-13
- **Organisation:** Tilastokeskus
- **Variable count:** 28
- **Observation count:** —

## Description

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


Laaja moduuli EDUC_KOSKI TOINEN ASTE:  ammatillinen_suoritukset

Suoritukset-taulu sisältää kaikki ammatillisen koulutuksen alemmat osasuoritukset. Sisältää tietoja kuten arvosanat, laajuus ja arviointipäivä. Kaikki tämän taulun rivit ovat osa jotain ammatillinen_tutkinnonosat-taulun suoritusta.
Yhdistää tietoja KOSKI raporttikannan tauluista: r_opiskeluoikeus, r_paatason_suoritus, r_osasuoritus, r_henkilo.

## Variables (28)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `shnro` | Suojattu henkilönumero | — | — | — |
| `oppija_oid_s` | Suojattu oppijatunnus | — | — | — |
| `opiskeluoikeus_oid_s` | Suojattu opiskeluoikeuden tunniste | — | — | — |
| `oppilaitos_oid_s` | Suojattu oppilaitostunnus | — | — | — |
| `oppilaitosnumero_s` | Suojattu oppilaitosnumero | — | — | — |
| `koulutusmoduuli_koodiarvo2_s` | Suojattu koulutusmoduuli koodiarvo | — | — | — |
| `oppilaitos_kotipaikka` | Oppilaitoksen kotipaikka | — | — | — |
| `toimipiste_oid_s` | Suojattu toimipisteen tunniste | — | — | — |
| `paataso_koulutusmoduuli` | Päätaso koulutusmoduuli | — | — | — |
| `paataso_koulutusmoduuli_koodisto` | Päätaso koulutusmoduuli koodisto | — | — | — |
| `paataso_tyyppi` | Päätason suorituksen tyyppi | — | — | — |
| `koulutusmoduuli_koodiarvo` | Koulutusmoduuli koodiarvo | — | — | — |
| `koulutusmoduuli_koodisto` | Koulutusmoduuli koodisto | — | — | — |
| `koulutusmoduuli_paikallinen` | Koulutusmoduuli paikallinen | — | — | — |
| `arviointi_arvosana_koodiarvo` | Arviointi arvosana koodiarvo | — | — | — |
| `arviointi_arvosana_koodisto` | Arviointi arvosana koodisto | — | — | — |
| `arviointi_paiva` | Osasuorituksen arviointi päivä | — | — | — |
| `tunnustettu` | Osasuorituksen tunnustus | — | — | — |
| `koulutusmoduuli_pakollinen` | Koulutusmoduuli pakollinen | — | — | — |
| `koulutusmoduuli_laajuus_arvo` | Koulutusmoduuli laajuus arvo | — | — | — |
| `koulutusmoduuli_laajuus_yksikko` | Koulutusmoduuli laajuus yksikkö | — | — | — |
| `tutkinnon_nimi_perusteessa` | Tutkinnon nimi perusteessa | — | — | — |
| `suorituksen_tyyppi` | Suorituksen tyyppi | — | — | — |
| `toinenOsaamisala` | Toinen osaamisala | — | — | — |
| `sisaltyy_opiskeluoikeuteen_oid_s` | Sisältyy opiskeluoikeuteen oid | — | — | — |
| `paataso_vahvistus_paiva` | Päätaso vahvistus päivä | — | — | — |
| `ylempi_osasuoritus_key` | Ylempi osasuoritus key | — | — | — |
| `koulutusmoduuli_kieliaine_nimi` | koulutusmoduuli kieliaine nimi | — | — | — |

### Variable definitions

#### `shnro` — Suojattu henkilönumero

Suojattu henkilönumero

#### `oppija_oid_s` — Suojattu oppijatunnus

Suojattu OPH:n oppijatunnus

#### `opiskeluoikeus_oid_s` — Suojattu opiskeluoikeuden tunniste

Suojattu OPH:n opiskeluoikeuden tunniste, joissain tapauksissa opiskeluoikeuden toimija ostaa koulutuksen toiselta koulutustoimijalta, näissä tapauksissa linkki opiskeluoikeuksien väliltä löytyy tästä kentästä. ks. tarkemmat lisätiedot OPH:n eduuni-wikistä (https://wiki.eduuni.fi/spaces/OPHPALV/pages/431685903/r_opiskeluoikeus).

#### `oppilaitos_oid_s` — Suojattu oppilaitostunnus

Suojattu Oppilaitoksen tunniste.

#### `oppilaitosnumero_s` — Suojattu oppilaitosnumero

Suojattu oppilaitosnumero

#### `koulutusmoduuli_koodiarvo2_s` — Suojattu koulutusmoduuli koodiarvo

koulutusmoduuli_koodiarvo suojattu paikallisilta kursseilta

#### `oppilaitos_kotipaikka` — Oppilaitoksen kotipaikka

Oppilaitoksen kotikunnan kuntakoodi

#### `toimipiste_oid_s` — Suojattu toimipisteen tunniste

toimipistetietoa ei välttämättä ole viety suoritukseen, tällaisissa tapauksissa toimipiste-kentästä löytyy vastaavan oppilaitoksen tieto.

#### `paataso_koulutusmoduuli` — Päätaso koulutusmoduuli

sen päätason suorituksen koodiarvo, johon tutkinnonosan suoritus kuuluu. Alkuperäinen nimi OPH:n aineistossa on koulutusmoduuli_koodiarvo.

#### `paataso_koulutusmoduuli_koodisto` — Päätaso koulutusmoduuli koodisto

https://opintopolku.fi/koski/dokumentaatio/koodistot, ammatillisen tutkintokoulutuksen suorituksilla on tässä kentässä arvo 'koulutus'. Alkuperäinen nimi OPH:n aineistossa on koulutusmoduuli_koodisto.

#### `paataso_tyyppi` — Päätason suorituksen tyyppi

Päätason suorituksen tyyppi

#### `koulutusmoduuli_koodiarvo` — Koulutusmoduuli koodiarvo

osasuorituksen tunniste. Tyhjätty jos kyseessä paikallinen suoritus (koulutusmoduuli_paikallinen='t'). Näille löytyy suojattu tunnus koulutusmoduuli_koodiarvo2_s.

#### `koulutusmoduuli_koodisto` — Koulutusmoduuli koodisto

Koodisto, josta osasuorituksen koodiarvo löytyy. Jos kyseessä paikallinen suoritus (koulutusmoduuli_paikallinen='t'), niin koodisto on tyhjä https://opintopolku.fi/koski/dokumentaatio/koodistot.

#### `koulutusmoduuli_paikallinen` — Koulutusmoduuli paikallinen

Kertoo onko kyseessä paikallisen opintosuunnitelman mukainen osasuoritus.

#### `arviointi_arvosana_koodiarvo` — Arviointi arvosana koodiarvo

osasuorituksen arvosana.

#### `arviointi_arvosana_koodisto` — Arviointi arvosana koodisto

Koodisto, johon arvosana kuuluu. https://opintopolku.fi/koski/dokumentaatio/koodistot

#### `arviointi_paiva` — Osasuorituksen arviointi päivä

Päivä, jolloin osasuoritus on arvioitu. suorituksen tyypille 'nayttotutkintoonvalmistavankoulutuksenosa' ei rekisteröidä arviointipäivää (tai arvosanaa), näille suorituksille yleensä löytyy vastaava suoritus toisella tyypillä samalla koodiarvolla

#### `tunnustettu` — Osasuorituksen tunnustus

Tieto siitä, onko osasuoritus tunnustettu (eli ns. luettu hyväksi aikaisempien opintojen perusteella).

#### `koulutusmoduuli_pakollinen` — Koulutusmoduuli pakollinen

Tieto siitä, onko osasuoritus pakollinen suoritettavassa koulutuksessa.

#### `koulutusmoduuli_laajuus_arvo` — Koulutusmoduuli laajuus arvo

osasuorituksen laajuuden arvo.

#### `koulutusmoduuli_laajuus_yksikko` — Koulutusmoduuli laajuus yksikkö

Osasuorituksen laajuuden yksikkö.

#### `tutkinnon_nimi_perusteessa` — Tutkinnon nimi perusteessa

ammatillisen tutkinnon nimi.

#### `suorituksen_tyyppi` — Suorituksen tyyppi

Suorituksen tyyppi

#### `toinenOsaamisala` — Toinen osaamisala

Purettu data-kentästä

#### `sisaltyy_opiskeluoikeuteen_oid_s` — Sisältyy opiskeluoikeuteen oid

Suojattu OPH:n opiskeluoikeuden tunniste, joissain tapauksissa opiskeluoikeuden toimija ostaa koulutuksen toiselta koulutustoimijalta, näissä tapauksissa linkki opiskeluoikeuksien väliltä löytyy tästä kentästä. ks. tarkemmat lisätiedot OPH:n eduuni-wikistä (https://wiki.eduuni.fi/spaces/OPHPALV/pages/431685903/r_opiskeluoikeus)

#### `paataso_vahvistus_paiva` — Päätaso vahvistus päivä

Päivä jolloin osasuorituksen sisältävä päätason suoritus on vahvistettu. Alkuperäinen nimi OPH:n aineistossa vahvistus_paiva.

#### `ylempi_osasuoritus_key` — Ylempi osasuoritus key

Yksilöi tutkinnonosan johon suoritus sisältyy, tutkinnonosa johon suoritus sisältyy löytyy vastaavalla avaimella ammatillinen_tutkinnonosat -taulusta.

#### `koulutusmoduuli_kieliaine_nimi` — koulutusmoduuli kieliaine nimi

suorituksen kieliaineen nimi. Huomio: Kieliopintojen koodiarvo ei erittele opiskeltavaa kieltä. Tästä muuttujasta löytyy opiskeltava kieli.

---

[← Back to catalogue](../../README.md)
