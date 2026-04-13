# EDUC_KOSKI TOINEN ASTE - Lukio_IB

- **Identifier:** `EDUC_20182025_jua_koskitoinenlukioib_001.xml`
- **DOI:** `opiskt_2025-06_2025-06-16_ain_0001`
- **Temporal coverage:** —
- **Published:** 2025-11-13
- **Organisation:** Tilastokeskus
- **Variable count:** 30
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


Laaja moduuli EDUC_KOSKI TOINEN ASTE:  Lukion ja IB-tutkintokoulutuksen kurssisuoritukset

Sisältää lukio- ja ib-tutkinto-koulutuksien kurssisuoritukset ja niihin liittyvää tietoa kuten arvosana, laajuus, oppiaine ja pakollisuus.
Yhdistää tietoja KOSKI raporttikannan tauluista: r_opiskeluoikeus, r_paatason_suoritus, r_osasuoritus, r_henkilo.

## Muuttujat / Variables (30)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `shnro` | Suojattu henkilonumero | — | — | — |
| `oppija_oid_s` | Suojattu oppijatunnus | — | — | — |
| `opiskeluoikeus_oid_s` | Suojattu opiskeluoikeuden tunniste | — | — | — |
| `oppilaitos_oid_s` | Suojattu Oppilaitoksen tunniste | — | — | — |
| `oppilaitosnumero_s` | Suojattu oppilaitosnumero | — | — | — |
| `oppilaitos_kotipaikka` | Oppilaitoksen kotipaikka | — | — | — |
| `toimipiste_oid_s` | Suojattu toimipisteen yksilöintitunnus | — | — | — |
| `kurssinimi_s` | Salattu kurssinimi | — | — | — |
| `kurssitunnus2_s` | salattu kurssintunnus 2 | — | — | — |
| `oppimaara_koodiarvo` | Oppimäärä koodiarvo | — | — | — |
| `aineopinnot` | Aineopinnot | — | — | — |
| `kurssitunnus` | Kurssitunnus | — | — | — |
| `kurssitunnus_koodisto` | Kurssitunnus koodisto | — | — | — |
| `kurssitunnus_paikallinen` | Kurssitunnus paikallinen | — | — | — |
| `arviointi_arvosana_koodiarvo` | Arviointi arvosana koodiarvo | — | — | — |
| `arviointi_arvosana_koodisto` | Arviointi arvosana koodisto | — | — | — |
| `arviointi_paiva` | Arviointi päivä | — | — | — |
| `oppiaine` | Oppiaine | — | — | — |
| `oppiaine_koodisto` | Oppiaine koodisto | — | — | — |
| `oppiaine_paikallinen` | Oppiaine paikallinen | — | — | — |
| `koulutusmoduuli_pakollinen` | Koulutusmoduuli pakollinen | — | — | — |
| `koulutusmoduuli_kurssin_tyyppi` | Koulutusmoduuli kurssin tyyppi | — | — | — |
| `koulutusmoduuli_kieliaine_nimi` | koulutusmoduuli kieliaine nimi | — | — | — |
| `koulutusmoduuli_laajuus_arvo` | Koulutusmoduuli laajuus arvo | — | — | — |
| `koulutusmoduuli_laajuus_yksikko` | Koulutusmoduuli laajuus yksikkö | — | — | — |
| `suorituksen_tyyppi` | Suorituksen tyyppi | — | — | — |
| `sisaltyy_opiskeluoikeuteen_oid_s` | Suojattu opiskeluoikeus tunniste | — | — | — |
| `paataso_vahvistus_paiva` | Päätaso vahvistus päivä | — | — | — |
| `paataso_suorituksen_tyyppi` | Päätaso suorituksen tyyppi | — | — | — |
| `koulutusmuoto` | Koulutusmuoto | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `shnro` — Suojattu henkilonumero

Suojattu henkilönumero

#### `oppija_oid_s` — Suojattu oppijatunnus

Suojattu OPH:n oppijatunnus

#### `opiskeluoikeus_oid_s` — Suojattu opiskeluoikeuden tunniste

Suojattu OPH:n opiskeluoikeuden tunniste

#### `oppilaitos_oid_s` — Suojattu Oppilaitoksen tunniste

Suojattu Oppilaitoksen tunniste

#### `oppilaitosnumero_s` — Suojattu oppilaitosnumero

Suojattu oppilaitosnumero

#### `oppilaitos_kotipaikka` — Oppilaitoksen kotipaikka

Oppilaitoksen kotikunnan kuntakoodi

#### `toimipiste_oid_s` — Suojattu toimipisteen yksilöintitunnus

Suojattu toimipisteen tunniste

#### `kurssinimi_s` — Salattu kurssinimi

Suojattu kurssin nimi paikallisille soveltaville kusseille. Ilman tätä muuttujaa tulisi paljon tuplia. Alkuperäinen nimi OPH:n aineistossa on koulutusmoduuli_nimi.

#### `kurssitunnus2_s` — salattu kurssintunnus 2

Kurssitunnus suojattu paikallisilta kursseilta sekä uskonnon kursseilta.

#### `oppimaara_koodiarvo` — Oppimäärä koodiarvo

Päätason suorituksen oppimäärä lukiokoulutuksen opiskelijoille, kertoo opiskeleeko opiskelija nuorten opintosuunnitelman mukaan ('nuortenops') vai aikuisten opintosuunnitelman mukaan ('aikuistenops')

#### `aineopinnot` — Aineopinnot

Tieto siitä opiskeleeko opiskelija lukion aineopintoja tai lukion oppiaineen oppimäärää lukion oppimäärän sijaan (päätason suorituksen_tyyppi in ('lukionaineopinnot', 'lukionoppiaineenoppimaara')) HUOM. Joillakin opiskelijoilla on saman opiskeluoikeuden sisällä sekä lukion oppimäärän suoritus, että yksi tai useampia lukion oppiaineen oppimäärän suorituksia. Muuttuja on suorituskohtainen, eli kertoo onko kyseinen kurssisuoritus osa koko lukion oppimäärän suoritusta, vai aineopintoja.

#### `kurssitunnus` — Kurssitunnus

Tyhjätty jos kyseessä paikallinen suoritus (kurssitunnus_paikallinen='t'). Eri uskontojen kurssit tyhjätty. Näille löytyy suojattuna tunnus kurssitunnus2_s

#### `kurssitunnus_koodisto` — Kurssitunnus koodisto

Jos kyseessä paikallinen suoritus (kurssitunnus_paikallinen='t'), niin koodisto on tyhjä. Lisätietoa: https://opintopolku.fi/koski/dokumentaatio/koodistot

#### `kurssitunnus_paikallinen` — Kurssitunnus paikallinen

Kertoo jos kurssi on paikallisen opetussuunnitelman mukainen

#### `arviointi_arvosana_koodiarvo` — Arviointi arvosana koodiarvo

Kurssisuorituksen arviointi vastaavan koodiston mukaisesti.

#### `arviointi_arvosana_koodisto` — Arviointi arvosana koodisto

Arvosanan koodisto, lisätietoa: https://opintopolku.fi/koski/dokumentaatio/koodistot

#### `arviointi_paiva` — Arviointi päivä

Päivä jolloin kurssisuoritus on arvioitu.

#### `oppiaine` — Oppiaine

Kurssisuorituksen oppiaineen koodiarvo. Oppiainetieto poimitaan joko päätason suorituksesta tai ylemmästä osasuorituksesta riippuen vastaavan kurssisuorituksen hierarkiasta. Eri uskontojen oppiaineiksi muutettu KT.

#### `oppiaine_koodisto` — Oppiaine koodisto

Kurssisuorituksen oppiaineen koodisto. Jos kyseessä paikallinen oppiaine (oppiaine_paikallinen='t'), niin koodisto on tyhjä https://opintopolku.fi/koski/dokumentaatio/koodistot

#### `oppiaine_paikallinen` — Oppiaine paikallinen

Kertoo jos oppiaine on paikallisen opetussuunnitelman mukainen.

#### `koulutusmoduuli_pakollinen` — Koulutusmoduuli pakollinen

Kertoo onko kurssi pakollinen suoritettavassa koulutuksessa.

#### `koulutusmoduuli_kurssin_tyyppi` — Koulutusmoduuli kurssin tyyppi

Tieto siitä, mitä kurssityyppiä (pakollinen, valinnainen, soveltava jne.) osasuoritus on silloin, kun kyseessä on vuoden 2015 lukion opetussuunnitelman perusteiden mukainen lukion kurssi

#### `koulutusmoduuli_kieliaine_nimi` — koulutusmoduuli kieliaine nimi

Kurssisuorituksen oppiaineen kieliaineen nimi. Kieliaineiden oppiainen muuttuja kertoo onko kyseessä esim. äidinkieli ('AI'), a1-kieli ('A1') yms. Tämä muuttuja kertoo opiskeltavan kielen

#### `koulutusmoduuli_laajuus_arvo` — Koulutusmoduuli laajuus arvo

Kurssin laajuuden arvo

#### `koulutusmoduuli_laajuus_yksikko` — Koulutusmoduuli laajuus yksikkö

Kurssin laajuuden koodisto.

#### `suorituksen_tyyppi` — Suorituksen tyyppi

Suorituksen tyyppi

#### `sisaltyy_opiskeluoikeuteen_oid_s` — Suojattu opiskeluoikeus tunniste

Suojattu OPH:n opiskeluoikeuden tunniste, joissain tapauksissa opiskeluoikeuden toimija ostaa koulutuksen toiselta koulutustoimijalta, näissä tapauksissa linkki opiskeluoikeuksien väliltä löytyy tästä kentästä. ks. tarkemmat lisätiedot OPH:n eduuni-wikistä (https://wiki.eduuni.fi/spaces/OPHPALV/pages/431685903/r_opiskeluoikeus)

#### `paataso_vahvistus_paiva` — Päätaso vahvistus päivä

Kurssisuorituksen sisältävän päätason suorituksen vahvistus_paiva. Kertoo milloin päätason suoritus johon kurssi liittyy on vahvistettu. Alkuperäinen nimi OPH:n aineistossa on vahvistus_paiva.

#### `paataso_suorituksen_tyyppi` — Päätaso suorituksen tyyppi

Kurssisuorituksen sisältävän päätason suorituksen tyyppi. Päätason suorituksen tyyppi voi olla lukiokoulutuksen opiskeluoikeuksissa 'lukionoppimaara',  'lukionaineopinnot' tai 'lukionoppiaineenoppimaara'. ib-tutkinnon opiskeluoikeuksille, kertoo liittyykö kurssisuoritus pre-ib-vaiheen-suoritukseen, vai varsinaiseen ib-tutkintoon johtavaan suoritukseen

#### `koulutusmuoto` — Koulutusmuoto

Koulutusmuoto

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
