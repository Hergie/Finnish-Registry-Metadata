# EDUC_KOSKI TOINEN ASTE -  Nivelvaihe

- **Identifier:** `EDUC_20182025_jua_koskitoinennivel_001.xml`
- **DOI:** `opiskt_2025-06_2025-06-16_ain_0001`
- **Temporal coverage:** —
- **Published:** 2025-11-13
- **Organisation:** Tilastokeskus
- **Variable count:** 26
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


Laaja moduuli EDUC_KOSKI TOINEN ASTE:  Nivelvaihe

Sisältää tiedot nivelvaiheen (tuva-koulutus, oppivelvollisille suunnattu vapaan sivistystyön koulutus, sekä loppuneet koulutusmuodot luva sekä valma). 
Nivelvaiheen koulutuksista luva-koulutuksen kurssisuoritukset, valma-koulutuksen osasuoritukset, oppivelvollisille suunnatun vapaan sivistystyön koulutuksen oppimiskokonaisuuksien suoritukset. Tuva-koulutuksesta annetaan kaikki ylemmät osasuoritukset, eli varsinaiset tuva-koulutuksenosat, sekä ’valinnaisia opintoja’ kokonaisuus. joillakin tuva-opiskeluoikeuksilla valinnaisia opintoja on eritelty tarkemmalla tasolla, mutta suurimmalla osalla ei, joten ’valinnaisia opintoja’ -kokonaisuus antaa kattavamman kuvan koulutusten laajuudesta.

Nivelvaiheen suoritustaulu (tutkintoon valmentava koulutus)
Yhdistää tietoja KOSKI raporttikannan tauluista: r_opiskeluoikeus, r_paatason_suoritus, r_osasuoritus, r_henkilo. Taulu yhdistää useita koulutusmuotoja yhden taulun alle. Käytännössä jokainen rivi on oman hierarkiansa alin suoritus. Tasot koulutusmuodoittain seuraavasti: Luva: kurssitaso, Valma: valmakoulutuksenosa/tutkinnonosanosasalue, Tuva: Tuva-koulutuksen osa, Oppivelvollisille suunnatun vapaansivistystyön koulutuksen: oppimiskokonaisuus.

Aineistossa on mukana koulutusmuodot tuva, luva, vapaansivistystyonkoulutus ja ammatillinenkoulutus. Ammatillisista koulutuksista sisällytetty vain valma-koulutus (päätason suorituksen_tyyppi='valma'). Vapaansivistystyön koulutuksesta sisällytetty vain oppivelvolliselle suunnattu vapaansivistystyön koulutus (päätason suorituksen_tyyppi='vstoppivelvollisillesuunnattukoulutus').

## Muuttujat / Variables (26)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `shnro` | Suojattu henkilönumero | — | — | — |
| `oppija_oid_s` | Suojattu oppijatunnus | — | — | — |
| `opiskeluoikeus_oid_s` | Suojattu opiskeluoikeuden tunniste | — | — | — |
| `tuva_jarjestamislupa` | Tuva järjestämislupa | — | — | — |
| `oppilaitos_oid_s` | Suojattu oppilaitos tunniste | — | — | — |
| `oppilaitosnumero_s` | Suojattu oppilaitosnumero | — | — | — |
| `oppilaitos_kotipaikka` | Oppilaitos kotipaikka | — | — | — |
| `toimipiste_oid_s` | Suojattu toimipisteen tunniste | — | — | — |
| `koulutusmoduuli_koodiarvo2_s` | Koulutusmoduuli koodiarvo2 | — | — | — |
| `koulutusmuoto` | Koulutusmuoto | — | — | — |
| `koulutusmoduuli_koodiarvo` | Koulutusmoduuli koodiarvo | — | — | — |
| `koulutusmoduuli_koodisto` | Koulutusmoduuli koodisto | — | — | — |
| `koulutusmoduuli_paikallinen` | Koulutusmoduuli paikallinen | — | — | — |
| `arviointi_arvosana_koodiarvo` | Arviointi arvosana koodiarvo | — | — | — |
| `arviointi_arvosana_koodisto` | Arviointi arvosana koodisto | — | — | — |
| `arviointi_paiva` | Arviointi päivä | — | — | — |
| `ylempi_osasuoritus_koodiarvo` | Ylempi osasuoritus koodiarvo | — | — | — |
| `ylempi_osasuoritus_koodisto` | Ylempi osasuoritus koodisto | — | — | — |
| `ylempi_osasuoritus_paikallinen` | Ylempi osasuoritus paikallinen | — | — | — |
| `koulutusmoduuli_pakollinen` | Koulutusmoduuli pakollinen | — | — | — |
| `koulutusmoduuli_kieliaine_nimi` | Koulutusmoduuli kieliaine nimi | — | — | — |
| `koulutusmoduuli_laajuus_arvo` | Koulutusmoduuli laajuus arvo | — | — | — |
| `koulutusmoduuli_laajuus_yksikko` | Koulutusmoduuli laajuus yksikkö | — | — | — |
| `suorituksen_tyyppi` | Suorituksen tyyppi | — | — | — |
| `paataso_suorituksen_tyyppi` | Päätason suorituksen tyyppi | — | — | — |
| `paataso_vahvistus_paiva` | Päätaso vahvistus päivä | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `shnro` — Suojattu henkilönumero

Suojattu henkilönumero

#### `oppija_oid_s` — Suojattu oppijatunnus

Suojattu OPH:n oppijatunnus

#### `opiskeluoikeus_oid_s` — Suojattu opiskeluoikeuden tunniste

Suojattu OPH:n opiskeluoikeuden tunniste

#### `tuva_jarjestamislupa` — Tuva järjestämislupa

Tieto siitä, minkä koulutuksen järjestämisluvan puitteissa tutkintokoulutukseen valmentavaa koulutusta järjestetään.

#### `oppilaitos_oid_s` — Suojattu oppilaitos tunniste

Suojattu Oppilaitoksen tunniste.

#### `oppilaitosnumero_s` — Suojattu oppilaitosnumero

Suojattu oppilaitosnumero.

#### `oppilaitos_kotipaikka` — Oppilaitos kotipaikka

Oppilaitoksen kotikunnan kuntakoodi.

#### `toimipiste_oid_s` — Suojattu toimipisteen tunniste

toimipistetietoa ei välttämättä ole viety suoritukseen, tällaisissa tapauksissa toimipiste-kentästä löytyy vastaavan oppilaitoksen tieto.

#### `koulutusmoduuli_koodiarvo2_s` — Koulutusmoduuli koodiarvo2

koulutusmoduuli_koodiarvo suojattu paikallisilta kursseilta ja uskonnon kursseilta

#### `koulutusmuoto` — Koulutusmuoto

koulutusmuoto 'ammatillinenkoulutus' tuva-taulussa viittaa valma-koulutukseen.

#### `koulutusmoduuli_koodiarvo` — Koulutusmoduuli koodiarvo

Osasuorituksen tunniste. Tyhjätty mikäli koulutusmoduuli on paikallinen

#### `koulutusmoduuli_koodisto` — Koulutusmoduuli koodisto

koodisto, josta osasuorituksen koodiarvo löytyy. Jos kyseessä paikallinen suoritus (koulutusmoduuli_paikallinen='t'), niin koodisto on tyhjä

#### `koulutusmoduuli_paikallinen` — Koulutusmoduuli paikallinen

Kertoo onko kyseessä paikallisen opintosuunnitelman mukainen osasuoritus.

#### `arviointi_arvosana_koodiarvo` — Arviointi arvosana koodiarvo

osasuorituksen arvosana.

#### `arviointi_arvosana_koodisto` — Arviointi arvosana koodisto

Koodisto, johon arvosana kuuluu. Lisätietoa: https://opintopolku.fi/koski/dokumentaatio/koodistot

#### `arviointi_paiva` — Arviointi päivä

Päivä, jolloin osasuoritus on arvioitu.

#### `ylempi_osasuoritus_koodiarvo` — Ylempi osasuoritus koodiarvo

Jos koulutusmuoto='luva' ylempi_osasuoritus-muuttujissa on tietoa kyseisen luva-kurssin oppiaineesta, jos taas koulutusmuoto='vapaansivistystyonkoulutus' muuttujat sisältävät tietoa osaamiskokonaisuudesta johon kyseinen opintokokonaisuus-rivi kuuluu

#### `ylempi_osasuoritus_koodisto` — Ylempi osasuoritus koodisto

Jos kyseessä paikallinen oppiaine (oppiaine_paikallinen='t'), niin koodisto on tyhjä

#### `ylempi_osasuoritus_paikallinen` — Ylempi osasuoritus paikallinen

Kertoo onko ylempi osasuoritus (oppiaine/osaamiskokonaisuus) paikallisen opintosuunnitelman mukainen.

#### `koulutusmoduuli_pakollinen` — Koulutusmoduuli pakollinen

Tieto siitä, onko tutkinnonosa pakollinen suoritettavassa koulutuksessa.

#### `koulutusmoduuli_kieliaine_nimi` — Koulutusmoduuli kieliaine nimi

Opiskeltavan kieliaineen nimi.

#### `koulutusmoduuli_laajuus_arvo` — Koulutusmoduuli laajuus arvo

Kertoo osasuorituksen laajuuden arvon.

#### `koulutusmoduuli_laajuus_yksikko` — Koulutusmoduuli laajuus yksikkö

Osasuorituksen laajuuden yksikko.

#### `suorituksen_tyyppi` — Suorituksen tyyppi

#### `paataso_suorituksen_tyyppi` — Päätason suorituksen tyyppi

Päätason suorituksen tyyppi.

#### `paataso_vahvistus_paiva` — Päätaso vahvistus päivä

Päivä jolloin osasuoritukseen liittyvä päätason suoritus on vahvistettu.

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
