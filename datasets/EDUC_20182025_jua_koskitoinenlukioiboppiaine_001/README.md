# EDUC_KOSKI_2ASTE - IB_lukio_oppiaine

- **Identifier:** `EDUC_20182025_jua_koskitoinenlukioiboppiaine_001.xml`
- **DOI:** `opiskt_2025-06_2025-06-16_ain_0001`
- **Temporal coverage:** —
- **Published:** 2026-04-27
- **Organisation:** Tilastokeskus
- **Variable count:** 27
- **Observation count:** —

## Description

EDUC_KOSKI-valmisaineisto sisältää OPH:n Koski-tietovarannon tietoja perusopetuksen, nivelvaiheen sekä toisen asteen koulutuksien läsnäolosta, sisällöstä sekä suorituksista. Aineiston avulla on mahdollista tutkia läsnäoloa koulutuksissa tarkalla tasolla, sillä aineisto sisältää jaksomuotoisen tilatiedon. Aineisto sisältää myös koulutuksien suoritustietoja, joiden avulla on mahdollista tutkia koulutuksien etenemistä tarkalla tasolla. Aineisto on kattavaa vuodesta 2020 lähtien. KOSKI-järjestelmä on otettu käyttöön vuonna 2018, mutta vuosien 2018 ja 2019 tiedot eivät ole kattavia. Aineistosta ei ole rajattu ulos aiempia tietoja. 

Valmisaineisto on jaettu kolmeen moduuliin: suppea, perusopetus ja toinen aste. 

Suppea moduuli sisältää opiskeluoikeus-taulun, sekä opiskeluoikeus_jakso-taulun. Opiskeluoikeus-taulu sisältää perustietoa opiskeluoikeuksista (koulutusmuoto, alkamis- ja paattymispaiva, oppilaitos, ammatillisen tutkinnon tutkintonimike, lukiokoulutuksen oppimäärä yms.), opiskeluoikeus_jakso-tauluun taas on eritelty opiskeluoikeuksien tilaa jaksomuotoisesti mahdollistaen opiskeluoikeuksien tilan tutkimisen päivän tarkkuudella. Kaksi laajempaa moduulia sisältää suppean moduulin tiedot, joten jos ottaa kaksi laajempaa moduulia ei suppeaa moduulia tarvita. 

Perusopetuksen moduuli sisältää suppean moduulin taulut rajattuna nuorten perusopetuksen sekä aikuisten perusopetuksen opiskeluoikeuksiin. Lisäksi moduuli sisältää suoritustaulun, joka sisältää nuorten perusopetuksen vuosiluokkien sekä oppimäärän (päättötodistuksen) oppiaine-suoritukset. Lisäksi suoritustauluun sisältyy perusopetuksen lisäopetuksen (ns. 10. luokka) oppiaine-suoritukset. Aikuisten perusopetuksesta moduuliin sisältyy sekä oppiaine- että kurssisuoritukset omina tauluinaan.

Toisen asteen moduuli sisältää suppean moduulin taulut rajattuna toisen asteen ja nivelvaiheen koulutuksien opiskeluoikeuksiin. Lisäksi moduuli sisältää koulutusmuotokohtaisia tauluja. 
 
Yleisiä huomioita: 

- Kaikista moduuleista on rajattu ulos mitätöidyt opiskeluoikeudet sekä arkaluonteiset tiedot kuten oppimisen tukeen liittyvät tiedot.

- Sisältää myös lukiokoulutuksen aineopiskelijat, sekä ammatillisesta koulutuksesta muut kuin tutkintokoulutuksen opiskeluoikeudet. Tutkintoon johtavat koulutukset ovat rajattavissa opiskeluoikeus-taulun muuttujien koulutusmoduuli_koodisto ja suorituksen_tyyppi avulla. 

- Perusopetuksen käyttäytymisen arvioinnit eivät sisälly valmisaineistoon, mutta ne ovat tilattavissa erikseen toimeksiantona. 

- HUOM. Aineisto ei sisällä työhön ja itsenäiseen elämään valmentavaa koulutusta (TELMA) ja vapaan sivistystyön koulutuksia, eikä perusopetuksen aineopiskelijoiden suorituksia. Aineisto sisältää kuitenkin kansanopistojen vapaana sivistystyönä järjestämän oppivelvollisuuskoulutuksen (ns. opistovuosi oppivelvollisille).


Aineistoon on mahdollista tulla myöhemmin lisäyksiä, mikäli muille koulutusmuodoille tulee tarvetta, tai ilmenee tarve muuttujille, joita ei nykyiseen sisältöön kuulu. 
 
Tilastokeskuksella on saatavilla OPH:n KOSKI-raporttikannan sisältö, joten jos jollekin tiedolle on tarvetta, mitä valmisaineistosta ei löydy, voi näitä tietoja pyytää erikseen toimeksiantona. Kuvaukset KOSKI-raporttikannan tiedoille löytyy OPH:n ylläpitämästä eduuni-wikistä (https://wiki.eduuni.fi/spaces/OPHPALV/pages/431685682/KOSKI-raporttikanta). 


Laaja moduuli EDUC_KOSKI_2ASTE:  IB_lukio_oppiaine

Sisältää lukio- ja IB-tutkintokoulutuksen oppiainesuoritukset ja niihin liittyvää tietoa kuten arvosana, laajuus, oppiaine ja pakollisuus.
Yhdistää tietoja KOSKI raporttikannan tauluista: r_opiskeluoikeus, r_paatason_suoritus, r_osasuoritus, r_henkilo.

## Variables (27)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `hid_e` | Suojattu henkilonumero | — | — | — |
| `oppija_oid_s` | Suojattu oppijatunnus | — | — | — |
| `opiskeluoikeus_oid_s` | Suojattu opiskeluoikeuden tunniste | — | — | — |
| `sis_opiskeluoikeuteen_oid` | sisaltyy_opiskeluoikeuteen_oid_s | — | — | — |
| `oppilaitos_oid_s` | Suojattu Oppilaitoksen tunniste | — | — | — |
| `oppilaitosnumero_s` | Suojattu oppilaitosnumero | — | — | — |
| `oppilaitos_kotipaikka` | Oppilaitoksen kotipaikka | — | — | — |
| `toimipiste_oid_s` | Suojattu toimipisteen yksilöintitunnus | — | — | — |
| `paataso_vahvistus_paiva` | Päätaso vahvistus päivä | — | — | — |
| `paataso_suorituksen_tyyppi` | Päätaso suorituksen tyyppi | — | — | — |
| `koulutusmuoto` | Koulutusmuoto | — | — | — |
| `oppimaara_koodiarvo` | Oppimäärä koodiarvo | — | — | — |
| `aineopinnot` | Aineopinnot | — | — | — |
| `oppiaine` | Oppiaine | — | — | — |
| `oppiaine_koodisto` | Oppiaine koodisto | — | — | — |
| `oppiaine_paikallinen` | Oppiaine paikallinen | — | — | — |
| `oppiaine_pakollinen` | Oppiaine pakollinen | — | — | — |
| `arviointi_arvosana_koodiarvo` | Arviointi arvosana koodiarvo | — | — | — |
| `arviointi_arvosana_koodisto` | Arviointi arvosana koodisto | — | — | — |
| `arviointi_hyvaksytty` | Arviointi hyväksytty | — | — | — |
| `arviointi_paiva` | Arviointi päivä | — | — | — |
| `vahvistus_paiva` | Vaihvistus päivä | — | — | — |
| `koulutusmoduuli_kieliaine_nimi` | koulutusmoduuli kieliaine nimi | — | — | — |
| `koulutusmoduuli_laajuus_arvo` | Koulutusmoduuli laajuus arvo | — | — | — |
| `koulutusmoduuli_laajuus_yksikko` | Koulutusmoduuli laajuus yksikkö | — | — | — |
| `suorituksen_tyyppi` | Suorituksen tyyppi | — | — | — |
| `oppiaine_id` | Oppiaine id | — | — | — |

### Variable definitions

#### `hid_e` — Suojattu henkilonumero

Suojattu henkilönumero.
Tilastokeskuksessa yhtenäisesti suojattu henkilö-id mahdollistaa henkilöä koskevien tietojen yhdistämisen eri aineistojen ja vuosien välillä.

#### `oppija_oid_s` — Suojattu oppijatunnus

Suojattu OPH:n oppijatunnus
.

#### `opiskeluoikeus_oid_s` — Suojattu opiskeluoikeuden tunniste

Suojattu OPH:n opiskeluoikeuden tunniste.

#### `sis_opiskeluoikeuteen_oid` — sisaltyy_opiskeluoikeuteen_oid_s

Suojattu OPH:n opiskeluoikeuden tunniste, joissain tapauksissa opiskeluoikeuden toimija ostaa koulutuksen toiselta koulutustoimijalta, näissä tapauksissa linkki opiskeluoikeuksien väliltä löytyy tästä kentästä. ks. tarkemmat lisätiedot OPH:n eduuni-wikistä (https://wiki.eduuni.fi/spaces/OPHPALV/pages/431685903/r_opiskeluoikeus)

#### `oppilaitos_oid_s` — Suojattu Oppilaitoksen tunniste

Suojattu Oppilaitoksen tunniste

#### `oppilaitosnumero_s` — Suojattu oppilaitosnumero

Suojattu oppilaitosnumero

#### `oppilaitos_kotipaikka` — Oppilaitoksen kotipaikka

Oppilaitoksen kotikunnan kuntakoodi.

#### `toimipiste_oid_s` — Suojattu toimipisteen yksilöintitunnus

Suojattu toimipisteen tunniste. Toimipistetietoa ei välttämättä ole viety suoritukseen, tällaisissa tapauksissa toimipiste-kentästä löytyy vastaavan oppilaitoksen tieto.

#### `paataso_vahvistus_paiva` — Päätaso vahvistus päivä

Oppiaine-rivin sisältävän päätason suorituksen vahvistus_paiva.

#### `paataso_suorituksen_tyyppi` — Päätaso suorituksen tyyppi

Oppiaine-rivin sisältävän päätason suorituksen tyyppi. Päätason suorituksen tyyppi voi olla lukiokoulutuksen opiskeluoikeuksissa 'lukionoppimaara',  'lukionaineopinnot' tai 'lukionoppiaineenoppimaara'. ib-tutkinnon opiskeluoikeuksille, kertoo liittyykö kurssisuoritus pre-ib-vaiheen-suoritukseen, vai varsinaiseen ib-tutkintoon johtavaan suoritukseen

#### `koulutusmuoto` — Koulutusmuoto

Koulutusmuoto

#### `oppimaara_koodiarvo` — Oppimäärä koodiarvo

Päätason suorituksen oppimäärä lukiokoulutuksen opiskelijoille, kertoo opiskeleeko opiskelija nuorten opintosuunnitelman mukaan ('nuortenops') vai aikuisten opintosuunnitelman mukaan ('aikuistenops').

#### `aineopinnot` — Aineopinnot

Tieto siitä opiskeleeko opiskelija lukion aineopintoja tai lukion oppiaineen oppimäärää lukion oppimäärän sijaan (päätason suorituksen_tyyppi in ('lukionaineopinnot', 'lukionoppiaineenoppimaara')). HUOM. Joillakin opiskelijoilla on saman opiskeluoikeuden sisällä sekä lukion oppimäärän suoritus, että yksi tai useampia lukion oppiaineen oppimäärän suorituksia. Muuttuja on suorituskohtainen, eli kertoo onko kyseinen oppiaine osa koko lukion oppimäärän suoritusta, vai aineopintoja.

#### `oppiaine` — Oppiaine

Oppiaineen koodiarvo, oppiaineen tunniste. Eri uskontojen oppiaineiksi muutettu KT.

#### `oppiaine_koodisto` — Oppiaine koodisto

Oppiaineen koodisto. Jos kyseessä paikallinen oppiaine (oppiaine_paikallinen='t'), niin koodisto on tyhjä https://opintopolku.fi/koski/dokumentaatio/koodistot

#### `oppiaine_paikallinen` — Oppiaine paikallinen

Kertoo, jos oppiaine on paikallisen opetussuunnitelman mukainen.

#### `oppiaine_pakollinen` — Oppiaine pakollinen

Kertoo, onko oppiaine pakollinen suoritettavassa koulutuksessa.

#### `arviointi_arvosana_koodiarvo` — Arviointi arvosana koodiarvo

Kurssisuorituksen arviointi vastaavan koodiston mukaisesti.

#### `arviointi_arvosana_koodisto` — Arviointi arvosana koodisto

Arvosanan koodisto, lisätietoa: https://opintopolku.fi/koski/dokumentaatio/koodistot

#### `arviointi_hyvaksytty` — Arviointi hyväksytty

Tieto siitä, onko arvioitu osasuoritus hyväksytysti suoritettu vai onko osasuoritus arvosanan perusteella hylätty.

#### `arviointi_paiva` — Arviointi päivä

Päivä, jolloin oppiaine on arvioitu. 
Huom. Suurimalta osalta opiskeluoikeuksia oppiaineilla ei ole arviointipäiviä Lähtökohtaisesti kannattaa käyttää muuttujaa paataso_vahvistus_paiva.

#### `vahvistus_paiva` — Vaihvistus päivä

Päivä, jolloin oppiaine on arvioitu. Huom. muuttujaa käytettävä vain 'lukionoppiaineenoppimaara'-tyyppisten suoritusten kanssa, muille suorituksille käytettävä arviointi_paiva-muuttujaa

#### `koulutusmoduuli_kieliaine_nimi` — koulutusmoduuli kieliaine nimi

Oppiaineen kieliaineen nimi. Kieliaineiden oppiaine-muuttuja kertoo, onko kyseessä esim. äidinkieli ('AI'), a1-kieli ('A1') yms. Tämä muuttuja kertoo opiskeltavan kielen.

#### `koulutusmoduuli_laajuus_arvo` — Koulutusmoduuli laajuus arvo

Oppiaineen laajuuden arvo. HUOM! Kaikissa osasuorituksissa laajuus ei ole relevantti tieto, sillä osasuorituksilla ei välttämättä ole nimettyä laajuutta (esimerkiksi ammatillisen koulutuksen reformia edeltävät ammattitutkinnot ja erikoisammattitutkinnot, joiden valtakunnallisille ammatillisille tutkinnon osillekaan ei ollut opetussuunnitelman perusteessa määritettyä laajuutta). Myöskään keskeneräisille osasuorituksille (esimerkiksi ammatillisessa tutkintokoulutuksessa keskeneräinen yhteinen tutkinnon osa, jossa kaikkia yhteisen tutkinnon osan osa-alueita ole vielä suoritettu) ei usein ole tallennettu suorituksen laajuutta, vaikka sellainen arvioidulta (= valmiilta) osasuoritukselta lopulta löytyisikin. Näissä tapauksissa kenttä on aina tyhjä.

#### `koulutusmoduuli_laajuus_yksikko` — Koulutusmoduuli laajuus yksikkö

Oppiaineen laajuuden koodisto.

1: opintoviikko
2: opintopistettä
3: vuosiviikkotuntia
4: kurssia
5: tuntia
6: osaamispistettä
7: vuotta
8: viikkoa (TUVA-laajuusyksikkö)

#### `suorituksen_tyyppi` — Suorituksen tyyppi

Suorituksen tyyppi.

#### `oppiaine_id` — Oppiaine id

Oppiaine-rivin tunniste, käytetään vain linkattaessa oppiaineeseen siihen kuuluvia kurssisuorituksia.
 Ei pysyvä tunniste.

---

[← Back to catalogue](../../README.md)
