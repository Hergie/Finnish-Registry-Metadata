# EDUC_KOSKI_2ASTE - Ammatillinen_ylemmat

- **Identifier:** `EDUC_20182025_jua_koskiammatillinenylemmat_001.xml`
- **DOI:** `opiskt_2025-06_2025-06-16_ain_0001`
- **Temporal coverage:** —
- **Published:** 2026-04-27
- **Organisation:** Tilastokeskus
- **Variable count:** 29
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


Laaja moduuli EDUC_KOSKI_2ASTE: ammatillinen_ylemmat
ylemmat-taulu sisältää ammatillisen koulutuksen ylemmät osasuoritukset (esim. tutkinnonosien suoritukset). Sisältää tietoja kuten arviointipäivät, arvioinnit ja laajuus.
Yhdistää tietoja KOSKI raporttikannan tauluista: r_opiskeluoikeus, r_paatason_suoritus, r_osasuoritus, r_henkilo.

HUOM. Taulu sisältää tuplarivejä, joita ei ole poistettu.

## Variables (29)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `hid_e` | Suojattu henkilönumero | — | — | — |
| `oppija_oid_s` | Suojattu oppijatunnus | — | — | — |
| `opiskeluoikeus_oid_s` | Suojattu opiskeluoikeuden tunniste | — | — | — |
| `oppilaitos_oid_s` | Suojattu oppilaitoksen tunniste | — | — | — |
| `oppilaitosnumero_s` | Suojattu oppilaitosnumero | — | — | — |
| `koulutusmoduuli_koodiarvo2_s` | Suojattu koulutusmoduuli koodiarvo | — | — | — |
| `sis_opiskeluoikeuteen_oid_s` | Sisältyy opiskeluoikeuteen oid | — | — | — |
| `oppilaitos_kotipaikka` | Oppilaitoksen kotikunta | — | — | — |
| `toimipiste_oid_s` | Suojattu toimipisteen tunniste | — | — | — |
| `paataso_koulutusmoduuli` | Päätaso koulutusmoduuli | — | — | — |
| `paataso_koulutusmoduuli_koodisto` | Päätaso koulutusmoduuli koodisto | — | — | — |
| `paataso_tyyppi` | Päätason suorituksen tyyppi | — | — | — |
| `paataso_vahvistus_paiva` | Päätaso vahvistus päivä | — | — | — |
| `koulutusmoduuli_koodiarvo` | Koulutusmoduuli koodiarvo | — | — | — |
| `koulutusmoduuli_koodisto` | Koulutusmoduuli koodisto | — | — | — |
| `koulutusmoduuli_kieliaine_nimi` | Koulutusmoduuli kieliaine nimi | — | — | — |
| `koulutusmoduuli_paikallinen` | Koulutusmoduuli paikallinen | — | — | — |
| `arviointi_arvosana_koodiarvo` | Arviointi arvosana koodiarvo | — | — | — |
| `arviointi_arvosana_koodisto` | Arviointi arvosana koodisto | — | — | — |
| `arviointi_hyvaksytty` | Arviointi hyväksytty | — | — | — |
| `arviointi_paiva` | Arviointi päivä | — | — | — |
| `tunnustettu` | Tunnustettu | — | — | — |
| `koulutusmoduuli_pakollinen` | Koulutusmoduuli pakollinen | — | — | — |
| `koulutusmoduuli_laajuus_arvo` | Koulutusmoduuli laajuus arvo | — | — | — |
| `koulutusmoduuli_laajuus_yksikko` | Koulutusmoduuli laajuus yksikkö | — | — | — |
| `tutkinnon_nimi_perusteessa` | Tutkinnon nimi perusteessa | — | — | — |
| `suorituksen_tyyppi` | Suorituksen tyyppi | — | — | — |
| `toinenOsaamisala` | Toinen osaamisala | — | — | — |
| `osasuoritus_id` | Osasuoritus id | — | — | — |

### Variable definitions

#### `hid_e` — Suojattu henkilönumero

Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e -tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä.

#### `oppija_oid_s` — Suojattu oppijatunnus

Suojattu OPH:n oppijatunnus

#### `opiskeluoikeus_oid_s` — Suojattu opiskeluoikeuden tunniste

Suojattu OPH:n opiskeluoikeuden tunniste

#### `oppilaitos_oid_s` — Suojattu oppilaitoksen tunniste

Suojattu oppilaitoksen tunniste

#### `oppilaitosnumero_s` — Suojattu oppilaitosnumero

Suojattu oppilaitosnumero

#### `koulutusmoduuli_koodiarvo2_s` — Suojattu koulutusmoduuli koodiarvo

Koulutusmoduuli_koodiarvo suojattu paikallisilta kursseilta

#### `sis_opiskeluoikeuteen_oid_s` — Sisältyy opiskeluoikeuteen oid

Suojattu OPH:n opiskeluoikeuden tunniste, joissain tapauksissa opiskeluoikeuden toimija ostaa koulutuksen toiselta koulutustoimijalta, näissä tapauksissa linkki opiskeluoikeuksien väliltä löytyy tästä kentästä. ks. tarkemmat lisätiedot OPH:n eduuni-wikistä (https://wiki.eduuni.fi/spaces/OPHPALV/pages/431685903/r_opiskeluoikeus)

#### `oppilaitos_kotipaikka` — Oppilaitoksen kotikunta

Oppilaitoksen kotikunnan kuntakoodi

#### `toimipiste_oid_s` — Suojattu toimipisteen tunniste

Suojattu toimipisteen tunniste.

Toimipistetietoa ei välttämättä ole viety suoritukseen, tällaisissa tapauksissa toimipiste-kentästä löytyy vastaavan oppilaitoksen tieto.

#### `paataso_koulutusmoduuli` — Päätaso koulutusmoduuli

Sen päätason suorituksen koodiarvo, johon osasuorituksen suoritus kuuluu.

#### `paataso_koulutusmoduuli_koodisto` — Päätaso koulutusmoduuli koodisto

Lisätietoa https://opintopolku.fi/koski/dokumentaatio/koodistot, ammatillisen tutkintokoulutuksen suorituksilla, sekä VALMA-koulutuksen suorituksilla on tässä kentässä arvo 'koulutus'.

#### `paataso_tyyppi` — Päätason suorituksen tyyppi

Päätason suorituksen tyyppi

#### `paataso_vahvistus_paiva` — Päätaso vahvistus päivä

Päivä, jolloin osasuorituksen sisältävä päätason suoritus on vahvistettu.

#### `koulutusmoduuli_koodiarvo` — Koulutusmoduuli koodiarvo

Osasuorituksen tunniste.
Tyhjätty, jos kyseessä paikallinen suoritus (koulutusmoduuli_paikallinen='t'). Näille löytyy suojattu tunnus koulutusmoduuli_koodiarvo2_s

#### `koulutusmoduuli_koodisto` — Koulutusmoduuli koodisto

Kooodisto, josta osasuorituksen koodiarvo löytyy.
Jos kyseessä paikallinen suoritus (koulutusmoduuli_paikallinen='t'), niin koodisto on tyhjä: https://opintopolku.fi/koski/dokumentaatio/koodistot

#### `koulutusmoduuli_kieliaine_nimi` — Koulutusmoduuli kieliaine nimi

Suorituksen kieliaineen nimi.
Kieliopintojen koodiarvo ei erittele opiskeltavaa kieltä. Tästä muuttujasta löytyy opiskeltava kieli.

#### `koulutusmoduuli_paikallinen` — Koulutusmoduuli paikallinen

Kertoo, onko kyseessä paikallisen opintosuunnitelman mukainen tutkinnonosan suoritus

#### `arviointi_arvosana_koodiarvo` — Arviointi arvosana koodiarvo

Osasuorituksen arvosana.

#### `arviointi_arvosana_koodisto` — Arviointi arvosana koodisto

Koodisto, johon arvosana kuuluu. Lisätietoa: Dokumentaatio - Koodistot - Koski - Opintopolku.fi ( https://opintopolku.fi/koski/dokumentaatio/koodistot )

#### `arviointi_hyvaksytty` — Arviointi hyväksytty

Tieto siitä, onko arvioitu osasuoritus hyväksytysti suoritettu vai onko osasuoritus arvosanan perusteella hylätty.

#### `arviointi_paiva` — Arviointi päivä

Päivä, jolloin osasuoritus on arvioitu.

Suorituksen tyypille 'nayttotutkintoonvalmistavankoulutuksenosa' ei rekisteröidä arviointipäivää (tai arvosanaa), näille suorituksille yleensä löytyy vastaava suoritus toisella tyypillä samalla koodiarvolla. Myöskään keskeneräisille tutkinnonosille ei löydy arviointipäivää.

#### `tunnustettu` — Tunnustettu

Tieto siitä, onko osasuoritus tunnustettu (eli ns. luettu hyväksi aikaisempien opintojen perusteella).

#### `koulutusmoduuli_pakollinen` — Koulutusmoduuli pakollinen

Tieto siitä, onko osasuoritus pakollinen suoritettavassa koulutuksessa
.

#### `koulutusmoduuli_laajuus_arvo` — Koulutusmoduuli laajuus arvo

Osasuorituksen laajuuden arvo. HUOM! Kaikissa osasuorituksissa laajuus ei ole relevantti tieto, sillä osasuorituksilla ei välttämättä ole nimettyä laajuutta (esimerkiksi ammatillisen koulutuksen reformia edeltävät ammattitutkinnot ja erikoisammattitutkinnot, joiden valtakunnallisille ammatillisille tutkinnon osillekaan ei ollut opetussuunnitelman perusteessa määritettyä laajuutta). Myöskään keskeneräisille osasuorituksille (esimerkiksi ammatillisessa tutkintokoulutuksessa keskeneräinen yhteinen tutkinnon osa, jossa kaikkia yhteisen tutkinnon osan osa-alueita ole vielä suoritettu) ei usein ole tallennettu suorituksen laajuutta, vaikka sellainen arvioidulta (= valmiilta) osasuoritukselta lopulta löytyisikin. Näissä tapauksissa kenttä on aina tyhjä.
.

#### `koulutusmoduuli_laajuus_yksikko` — Koulutusmoduuli laajuus yksikkö

Osasuorituksen laajuuden yksikkö
1: opintoviikko
2: opintopistettä
3: vuosiviikkotuntia
4: kurssia
5: tuntia
6: osaamispistettä
7: vuotta
8: viikkoa (TUVA-laajuusyksikkö)
.

#### `tutkinnon_nimi_perusteessa` — Tutkinnon nimi perusteessa

Ammatillisen tutkinnon nimi.

#### `suorituksen_tyyppi` — Suorituksen tyyppi

Suorituksen tyyppi.
Tutkintokoulutuksissa mahdolliset tyypit ovat 'ammatillisentutkinnonosa' tai 'nayttotutkintoonvalmistavankoulutuksenosa', lisäksi muun ammatillisen koulutuksen ylemmät osasuoritukset tässä taulussa saavat arvon 'muunammatillisenkoulutuksenosasuoritus'.

#### `toinenOsaamisala` — Toinen osaamisala

Purettu data-kentästä.

#### `osasuoritus_id` — Osasuoritus id

Käytetään vain linkatessa ammatillinen_alemmat -taulun suorituksia ammatillinen_ylemmat-taulun osasuorituksiin, joihin ne sisältyvät.
 Ei pysyvä tunniste.

---

[← Back to catalogue](../../README.md)
