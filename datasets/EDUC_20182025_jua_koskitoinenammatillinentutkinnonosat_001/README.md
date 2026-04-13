# EDUC_KOSKI TOINEN ASTE - ammatillinen_tutkinnonosat

- **Identifier:** `EDUC_20182025_jua_koskitoinenammatillinentutkinnonosat_001.xml`
- **DOI:** `opiskt_2025-06_2025-06-16_ain_0001`
- **Temporal coverage:** —
- **Published:** 2025-11-13
- **Organisation:** Tilastokeskus
- **Variable count:** 28
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


Laaja moduuli EDUC_KOSKI TOINEN ASTE:  ammatillinen_tutkinnonosat

Tutkinnonosa-taulu sisältää ammatillisen koulutuksen ylemmät osasuoritukset (esim. tutkinnonosien suoritukset). Sisältää tietoja kuten arviointipäivät, arvioinnit ja laajuus.
Yhdistää tietoja KOSKI raporttikannan tauluista: r_opiskeluoikeus, r_paatason_suoritus, r_osasuoritus, r_henkilo.

## Muuttujat / Variables (28)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `shnro` | Suojattu henkilönumero | — | — | — |
| `oppija_oid_s` | Suojattu oppijatunnus | — | — | — |
| `opiskeluoikeus_oid_s` | Suojattu opiskeluoikeuden tunniste | — | — | — |
| `oppilaitos_oid_s` | Suojattu oppilaitos tunniste | — | — | — |
| `oppilaitosnumero_s` | Suojattu oppilaitosnumero | — | — | — |
| `koulutusmoduuli_koodiarvo2_s` | Koulutusmoduuli koodiarvo | — | — | — |
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
| `arviointi_paiva` | Arviointi päivä | — | — | — |
| `tunnustettu` | Tunnustettu | — | — | — |
| `koulutusmoduuli_pakollinen` | Koulutusmoduuli pakollinen | — | — | — |
| `koulutusmoduuli_laajuus_arvo` | Koulutusmoduuli laajuus arvo | — | — | — |
| `koulutusmoduuli_laajuus_yksikko` | Koulutusmoduuli laajuus yksikkö | — | — | — |
| `tutkinnon_nimi_perusteessa` | Tutkinnon nimi perusteessa | — | — | — |
| `suorituksen_tyyppi` | Suorituksen tyyppi | — | — | — |
| `toinenOsaamisala` | Toinen osaamisala | — | — | — |
| `sisaltyy_opiskeluoikeuteen_oid_s` | Suojattu opiskeluoikeuden tunniste | — | — | — |
| `paataso_vahvistus_paiva` | Päätaso vahvistus päivä | — | — | — |
| `osasuoritus_key` | Osasuoritus key | — | — | — |
| `koulutusmoduuli_kieliaine_nimi` | koulutusmoduuli kieliaine nimi | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `shnro` — Suojattu henkilönumero

Suojattu henkilönumero

#### `oppija_oid_s` — Suojattu oppijatunnus

Suojattu OPH:n oppijatunnus

#### `opiskeluoikeus_oid_s` — Suojattu opiskeluoikeuden tunniste

Suojattu OPH:n opiskeluoikeuden tunniste

#### `oppilaitos_oid_s` — Suojattu oppilaitos tunniste

Suojattu Oppilaitoksen tunniste

#### `oppilaitosnumero_s` — Suojattu oppilaitosnumero

Suojattu oppilaitosnumero.

#### `koulutusmoduuli_koodiarvo2_s` — Koulutusmoduuli koodiarvo

koulutusmoduuli_koodiarvo suojattu paikallisilta kursseilta

#### `oppilaitos_kotipaikka` — Oppilaitoksen kotipaikka

Oppilaitoksen kotikunnan kuntakoodi

#### `toimipiste_oid_s` — Suojattu toimipisteen tunniste

toimipistetietoa ei välttämättä ole viety suoritukseen, tällaisissa tapauksissa toimipiste-kentästä löytyy vastaavan oppilaitoksen tieto.

#### `paataso_koulutusmoduuli` — Päätaso koulutusmoduuli

sen päätason suorituksen koodiarvo, johon tutkinnonosan suoritus kuuluu. Alkuperäinen nimi OPH:n aineistossa koulutusmoduuli_koodiarvo.

#### `paataso_koulutusmoduuli_koodisto` — Päätaso koulutusmoduuli koodisto

Ammatillisen tutkintokoulutuksen suorituksilla on tässä kentässä arvo 'koulutus'. https://opintopolku.fi/koski/dokumentaatio/koodistot. Alkuperäinen nimi OPH:n aineistossa koulutusmoduuli_koodisto.

#### `paataso_tyyppi` — Päätason suorituksen tyyppi

päätason suorituksen tyyppi. Alkuperäinen nimi OPH:n aineistossa on suorituksen_tyyppi.

#### `koulutusmoduuli_koodiarvo` — Koulutusmoduuli koodiarvo

Tutkinnonosan tunniste. Tyhjätty jos kyseessä paikallinen suoritus (koulutusmoduuli_paikallinen='t'). Näille löytyy suojattu tunnus koulutusmoduuli_koodiarvo2_s.

#### `koulutusmoduuli_koodisto` — Koulutusmoduuli koodisto

koodisto, josta tutkinnonosan koodiarvo löytyy. Jos kyseessä paikallinen suoritus (koulutusmoduuli_paikallinen='t'), niin koodisto on tyhjä https://opintopolku.fi/koski/dokumentaatio/koodistot

#### `koulutusmoduuli_paikallinen` — Koulutusmoduuli paikallinen

Kertoo onko kyseessä paikallisen opintosuunnitelman mukainen tutkinnonosan suoritus.

#### `arviointi_arvosana_koodiarvo` — Arviointi arvosana koodiarvo

tutkinnonosan arvosana.

#### `arviointi_arvosana_koodisto` — Arviointi arvosana koodisto

Koodisto, johon arvosana kuuluu. https://opintopolku.fi/koski/dokumentaatio/koodistot

#### `arviointi_paiva` — Arviointi päivä

Päivä, jolloin tutkinnonosa on arvioitu. Suorituksen tyypille 'nayttotutkintoonvalmistavankoulutuksenosa' ei rekisteröidä arviointipäivää (tai arvosanaa), näille suorituksille yleensä löytyy vastaava suoritus toisella tyypillä samalla koodiarvolla. Myöskin keskeneräisille tutkinnonosille ei löydy arviointipäivää.

#### `tunnustettu` — Tunnustettu

Tieto siitä, onko tutkinnonosa tunnustettu (eli ns. luettu hyväksi aikaisempien opintojen perusteella).

#### `koulutusmoduuli_pakollinen` — Koulutusmoduuli pakollinen

Tieto siitä, onko tutkinnonosa pakollinen suoritettavassa koulutuksessa.

#### `koulutusmoduuli_laajuus_arvo` — Koulutusmoduuli laajuus arvo

tutkinnonosan laajuuden arvo.

#### `koulutusmoduuli_laajuus_yksikko` — Koulutusmoduuli laajuus yksikkö

Tutkinnonosan laajuuden yksikko.

#### `tutkinnon_nimi_perusteessa` — Tutkinnon nimi perusteessa

Ammatillisen tutkinnon nimi.

#### `suorituksen_tyyppi` — Suorituksen tyyppi

Suorituksen tyyppi. Tutkintokoulutuksissa mahdolliset tyypit ovat 'ammatillisentutkinnonosa' tai 'nayttotutkintoonvalmistavankoulutuksenosa', lisäksi muun ammatillisen koulutuksen ylemmät osasuoritukset tässä taulussa saavat arvon 'muunammatillisenkoulutuksenosasuoritus'.

#### `toinenOsaamisala` — Toinen osaamisala

Purettu data-kentästä

#### `sisaltyy_opiskeluoikeuteen_oid_s` — Suojattu opiskeluoikeuden tunniste

Suojattu OPH:n opiskeluoikeuden tunniste, joissain tapauksissa opiskeluoikeuden toimija ostaa koulutuksen toiselta koulutustoimijalta, näissä tapauksissa linkki opiskeluoikeuksien väliltä löytyy tästä kentästä. ks. tarkemmat lisätiedot OPH:n eduuni-wikistä (https://wiki.eduuni.fi/spaces/OPHPALV/pages/431685903/r_opiskeluoikeus)

#### `paataso_vahvistus_paiva` — Päätaso vahvistus päivä

Päivä jolloin tutkinnonosan sisältävä päätason suoritus on vahvistettu. Alkuperäinen nimi OPH:n aineistossa vahvistus_paiva.

#### `osasuoritus_key` — Osasuoritus key

Käytetään vain linkatessa ammatillinen_suoritukset taulun suorituksia tutkinnonosiin joihin ne sisältyvät.

#### `koulutusmoduuli_kieliaine_nimi` — koulutusmoduuli kieliaine nimi

suorituksen kieliaineen nimi. Huomio: Kieliopintojen koodiarvo ei erittele opiskeltavaa kieltä. Tästä muuttujasta löytyy opiskeltava kieli.

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
