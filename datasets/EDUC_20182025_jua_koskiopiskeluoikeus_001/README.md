# EDUC_KOSKI_SUPPEA - Opiskeluoikeus

- **Identifier:** `EDUC_20182025_jua_koskiopiskeluoikeus_001.xml`
- **DOI:** `opiskt_2025-10_2025-10-23_ain_0001`
- **Temporal coverage:** —
- **Published:** 2025-11-13
- **Organisation:** Tilastokeskus
- **Variable count:** 29
- **Observation count:** —

## Description

EDUC_KOSKI-valmisaineisto sisältää OPH:n Koski-tietovarannon tietoja perusopetuksen,
nivelvaiheen sekä toisen asteen koulutuksien läsnäolosta, sisällöstä sekä suorituksista. Aineiston
avulla on mahdollista tutkia läsnäoloa koulutuksissa tarkalla tasolla, sillä aineisto sisältää
jaksomuotoisen tilatiedon. Aineisto sisältää myös koulutuksien suoritustietoja, joiden avulla on
mahdollista tutkia koulutuksien etenemistä tarkalla tasolla. Aineisto on kattavaa vuodesta 2020
lähtien. KOSKI-järjestelmä on otettu käyttöön vuonna 2018, mutta vuosien 2018 ja 2019 tiedot
eivät ole kattavia. Aineistosta ei ole rajattu ulos aiempia tietoja.

Valmisaineisto on jaettu kolmeen moduuliin: suppea, perusopetus ja toinen aste.

Suppea moduuli sisältää opiskeluoikeus-taulun, sekä opiskeluoikeus_jakso-taulun.
Opiskeluoikeus-taulu sisältää perustietoa opiskeluoikeuksista (koulutusmuoto, alkamis- ja
paattymispaiva, oppilaitos, ammatillisen tutkinnon tutkintonimike, lukiokoulutuksen oppimäärä
yms.), opiskeluoikeus_jakso-tauluun taas on eritelty opiskeluoikeuksien tilaa jaksomuotoisesti
mahdollistaen opiskeluoikeuksien tilan tutkimisen päivän tarkkuudella. Kaksi laajempaa moduulia
sisältää suppean moduulin tiedot, joten jos ottaa kaksi laajempaa moduulia ei suppeaa moduulia
tarvita.

Perusopetuksen moduuli sisältää suppean moduulin taulut rajattuna nuoten perusopetuksen sekä
aikuisten perusopetuksen opiskeluoikeuksiin. Lisäksi moduuli sisältää suoritustaulun, joka sisältää
nuorten perusopetuksen vuosiluokkien sekä oppimäärän (päättötodistuksen) oppiaine-suoritukset.
Lisäksi suoritustauluun sisältyy perusopetuksen lisäopetuksen (ns. 10. luokka) oppiaine-suoritukset.
Aikuisten perusopetuksesta moduuliin sisältyy sekä oppiaine- että kurssisuoritukset omina
tauluinaan.

Toisen asteen moduuli sisältää suppean moduulin taulut rajattuna toisen asteen ja nivelvaiheen
koulutuksien opiskeluoikeuksiin. Lisäksi moduuli sisältää koulutusmuotokohtaisia tauluja.

Yleisiä huomioita:

- Kaikista moduuleista on rajattu ulos mitätöidyt opiskeluoikeudet sekä arkaluonteiset tiedot kuten
oppimisen tukeen liittyvät tiedot.

- Sisältää myös lukiokoulutuksen aineopiskelijat, sekä ammatillisesta koulutuksesta muut kuin
tutkintokoulutuksen opiskeluoikeudet. Tutkintoon johtavat koulutukset ovat rajattavissa
opiskeluoikeus-taulun muuttujien koulutusmoduuli_koodisto ja suorituksen_tyyppi avulla.

- Perusopetuksen käyttäytymisen arvioinnit eivät sisälly valmisaineistoon, mutta ne ovat tilattavissa
erikseen toimeksiantona.


- HUOM. Aineisto ei sisällä työhön ja itsenäiseen elämään valmentavaa koulutusta (TELMA) ja
vapaan sivistystyön koulutuksia, eikä perusopetuksen aineopiskelijoiden suorituksia. Aineisto
sisältää kuitenkin kansanopistojen vapaana sivistystyönä järjestämän oppivelvollisuuskoulutuksen
(ns. opistovuosi oppivelvollisille).

Aineistoon on mahdollista tulla myöhemmin lisäyksiä, mikäli muille koulutusmuodoille tulee tarvetta,
tai ilmenee tarve muuttujille, joita ei nykyiseen sisältöön kuulu.

Tilastokeskuksella on saatavilla OPH:n KOSKI-raporttikannan sisältö, joten jos jollekin tiedolle on
tarvetta, mitä valmisaineistosta ei löydy, voi näitä tietoja pyytää erikseen toimeksiantona. Kuvaukset
KOSKI-raporttikannan tiedoille löytyy OPH:n ylläpitämästä <a href="https://wiki.eduuni.fi/spaces/OPHPALV/pages/431685682/KOSKI-raporttikanta" > eduuni-wikistä</a>.

Suppea moduuli EDUC_KOSKI_SUPPEA: opiskeluoikeus

Sisältää KOSKI-tietovarannon tietoja opiskeluoikeuksista.

Moduulia voidaan käyttää, kun tutkitaan koulutuksessa läsnäoloa sekä koulutuksen kestoa. Yhdistää
tietoja KOSKI-raporttikannan tauluista: r_opiskeluoikeus, r_henkilo, r_paatason_suoritus. Sisältää seuraavat tiedot: 
Tila (läsnäolo, valmistuminen yms.), suojattu oppilaitostunnus, koulutusmuoto, tutkintonimike, oppimäärä, laajuus.

Rajoitukset: koulutusmuoto (ammatillinenkoulutus, lukiokoulutus, ibtutkinto, luva, tuva,
perusopetuksenlisaopetus, perusopetus, aikuistenperusopetus, vapaansivistystyonkoulutus).
Mitätöidyt opiskeluoikeudet rajattu ulos. Arkaluontoiset tiedot jätetty ulkopuolelle.

Monet muun ammatillisen koulutuksen (suorituksen_tyyppi='muuammatillinenkoulutus')
opiskeluoikeudet koostuvat vain päätason suorituksesta ja eivät näy ammatillisen koulutuksen
suoritustauluissa. Tieto näiden koulutuksien mahdollisesta laajuudesta selviää
opiskeluoikeus-taulusta. Nämä koulutukset voivat olla esimerkiksi yhden päivän mittaisia kursseja.

Yhdistää tietoja KOSKI raporttikannan tauluista: r_opiskeluoikeus, r_paatason_suoritus,
r_organisaatio, r_henkilo

## Variables (29)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `hid_e` | Suojattu henkilönumero | — | — | — |
| `oppija_oid_s` | Suojattu oppijatunnus | — | — | — |
| `opiskeluoikeus_oid_s` | Suojattu opiskeluoikeuden tunniste | — | — | — |
| `oppilaitos_oid_s` | Suojattu Oppilaitoksen tunniste | — | — | — |
| `oppilaitosnumero_s` | Suojattu oppilaitosnumero | — | — | — |
| `sis_opiskeluoikeuteen_oid_s` | sisaltyy opiskeluoikeuteen oid | — | — | — |
| `oppilaitos_kotipaikka` | Oppilaitoksen kotikunta | — | — | — |
| `koulutustoimija_oid_s` | Suojattu koulutustoimijan tunniste | — | — | — |
| `koulutustoimija_y_tunnus` | suojattu koulutustoimijan y-tunnus | — | — | — |
| `koulutusmuoto` | koulutusmuoto | — | — | — |
| `alkamispaiva` | Opiskeluoikeuden alkamispäivä | — | — | — |
| `paattymispaiva` | Opiskeluoikeuden päättymispäivä | — | — | — |
| `viimeisin_tila` | Opiskeluoikeuden viimeisin tila | — | — | — |
| `suorituksen_tyyppi` | Opiskeluoikeuden päätason suorituksen suorituksen tyyppi | — | — | — |
| `vahvistus_paiva` | Vahvistus päivä | — | — | — |
| `koulutusmoduuli_koulutustyyppi` | Koulutusmoduuli koulutustyyppi | — | — | — |
| `koulutusmoduuli_koodiarvo` | Opiskeluoikeuden päätason suorituksen koulutusmoduuli koodiarvo | — | — | — |
| `koulutusmoduuli_koodisto` | Opiskeluoikeuden päätason suorituksen koulutusmoduuli_koodisto | — | — | — |
| `Suoritustapa_nimi` | Suoritustapa nimi | — | — | — |
| `tutkinnon_nimi_perusteessa` | ammatillisen tutkinnon nimi | — | — | — |
| `tutkintonimike_koodiarvo` | Tutkintonimike koodiarvo | — | — | — |
| `toinenTutkintonimike` | Toinen tutkintonimike | — | — | — |
| `toinenOsaamisala` | Toinen osaamisala | — | — | — |
| `koulutusmoduuli_laajuus_arvo` | Opiskeluoikeuden päätason suorituksen laajuuden arvo | — | — | — |
| `koulutusmoduuli_laajuus_yksikko` | Opiskeluoikeuden päätason suorituksen laajuuden yksikko | — | — | — |
| `osaamisala_nimi` | Päätason suoritukseen liittyvän osaamisalan nimi | — | — | — |
| `osaamisala_koodiarvo` | Päätason suoritukseen liittyvän osaamisalan koodiarvo | — | — | — |
| `oppimaara_koodiarvo` | oppimäärä koodiarvo | — | — | — |
| `tuva_jarjestamislupa` | tuva jarjestamislupa | — | — | — |

### Variable definitions

#### `hid_e` — Suojattu henkilönumero

Tilastokeskuksessa yhtenäisesti suojattu henkilö-id mahdollistaa henkilöä koskevien tietojen yhdistämisen aineistojen ja vuosien välillä.

#### `oppija_oid_s` — Suojattu oppijatunnus

Suojattu OPH:n oppijatunnus

#### `opiskeluoikeus_oid_s` — Suojattu opiskeluoikeuden tunniste

Suojattu OPH:n opiskeluoikeuden tunniste

#### `oppilaitos_oid_s` — Suojattu Oppilaitoksen tunniste

Suojattu Oppilaitoksen tunniste

#### `oppilaitosnumero_s` — Suojattu oppilaitosnumero

Suojattu oppilaitosnumero.

#### `sis_opiskeluoikeuteen_oid_s` — sisaltyy opiskeluoikeuteen oid

Suojattu OPH:n opiskeluoikeuden tunniste, joissain tapauksissa opiskeluoikeuden toimija ostaa
koulutuksen toiselta koulutustoimijalta, näissä tapauksissa linkki opiskeluoikeuksien väliltä löytyy
tästä kentästä. ks. tarkemmat lisätiedot OPH:n eduuni-wikistä (https://wiki.eduuni.fi/spaces/OPHPALV/pages/431685903/r_opiskeluoikeus)

#### `oppilaitos_kotipaikka` — Oppilaitoksen kotikunta

Oppilaitoksen kotikunnan kuntakoodi

#### `koulutustoimija_oid_s` — Suojattu koulutustoimijan tunniste

Suojattu koulutustoimijan tunniste

#### `koulutustoimija_y_tunnus` — suojattu koulutustoimijan y-tunnus

Suojattu koulutustoimijan y-tunnus

#### `koulutusmuoto` — koulutusmuoto

Huom. ammatilliseen koulutukseen kuuluu monta eri tyyppistä koulutusta (tutkintokoulutuksen
lisäksi esim. valma-koulutus), joten niiden tunnistamiseen täytyy lisäksi käyttää
suorituksen_tyyppi-kenttää.

#### `alkamispaiva` — Opiskeluoikeuden alkamispäivä

Opiskeluoikeuden alkamispäivä

#### `paattymispaiva` — Opiskeluoikeuden päättymispäivä

Opiskeluoikeuden päättymispäivä

#### `viimeisin_tila` — Opiskeluoikeuden viimeisin tila

Opiskeluoikeuden tila aineiston generointiajankohtana

#### `suorituksen_tyyppi` — Opiskeluoikeuden päätason suorituksen suorituksen tyyppi

Suorituksen tyyppi, joka yksilöi, millaisesta päätason suorituksessa on kyse (esimerkiksi ammatillisessa koulutuksessa tieto kertoo sen, suoritetaanko kokonaista tutkintoa, tutkinnon osaa/osia, tutkinnon osaa pienemmistä kokonaisuuksista koostuvaa suoritusta, muun ammatillisen koulutuksen suoritusta, VALMA-koulutusta). Opiskeluoikeus-tauluun poimitaan tiedot yhdestä päätason suorituksesta priorisoiden lukiokoulutuksessa lukion oppimäärän suoritusta, ammatillisessa koulutuksessa tutkinnon tai tutkinnon osan/osien suoritusta, perusopetuksessa oppimäärän suoritusta, IB-tutkinnon opiskeluoikeuksissa IB-tutkinnon suoritusta, sekä aikuisten
perusopetuksessa oppimäärän (eli päättövaiheen) suoritusta,

HUOM!Valma-koulutus on koulutusmuodoltaan ammatillista koulutusta, joten sen erottelemiseen täytyy käyttää tätä muuttujaa. Ammatillinen tutkintokoulutus sisältää opiskeluoikeuksia, joissa tavoite on suorittaa koko tutkinto (suorituksen_tyyppi='ammatillinentutkinto') ja opiskeluoikeuksia joissa tavoitteena on suorittaa tutkinnonosa tai osia (suorituksen_tyyppi='ammatillinentutkintoosittainen'), näiden erotteluun tarvitaan tätä muuttujaa muuttujan koulutusmoduuli_koodisto lisäksi.

#### `vahvistus_paiva` — Vahvistus päivä

Opiskeluoikeuden päätason suorituksen vahvistus_paiva, kertoo milloin päätason suoritus (esim. ammatillinen tutkinto tai lukion oppimäärä) on vahvistettu.

#### `koulutusmoduuli_koulutustyyppi` — Koulutusmoduuli koulutustyyppi

Koulutustyyppi ryhmittelee joissain koulutusmuodoissa tutkintokoulutuksen suorituksia erilaisiin tai eritasoisiin suorituksiin. KOSKI-datan kohdalla relevantti vain ammatillisen tutkintokoulutuksen kohdalla, ja kertoo sen, onko ammatillisen tutkintokoulutuksen (koko tutkinnon suoritus tai tutkinnonosan/osien suoritus) suorituksessa kyse ammatillinen perustutkinnosta, ammattitutkinnosta vai erikoisammattitutkinnosta tai niihin liittyvistä opinnoista.
Koodisto: https://opintopolku.fi/koski/dokumentaatio/koodisto/koulutustyyppi/latest  (koulutustyyppi - Koski - Opintopolku.fi)

#### `koulutusmoduuli_koodiarvo` — Opiskeluoikeuden päätason suorituksen koulutusmoduuli koodiarvo

Opiskeluoikeuden päätason suorituksen koulutusmoduuli koodiarvo. HUOM! Lukion aineopiskelijoilla
joilla päätason suorituksen tyyppi on 'lukionoppiaineenoppimaara' sekä aikuisten perusopetuksen
aineopiskelijoilla joilla päätason suorituksen tyyppi on 'perusopetuksenoppiaineenoppimaara' voi
opiskeluoikeuteen sisältyä useampi päätason suoritus, opiskeluoikeus-tauluun poimitaan tiedot
vain yhdestä päätason suorituksesta, joten muuttuja koulutusmoduuli_koodiarvo ei kattavasti
näiden opiskelijoiden tapauksessa kerro koulutuksen sisällöstä. Tiedot opiskeluoikeuden
oppiaineista löytyvät näissä tapauksissa tauluista ib_lukio_oppiaine, tai aik_perusopetus_oppiaine.

#### `koulutusmoduuli_koodisto` — Opiskeluoikeuden päätason suorituksen koulutusmoduuli_koodisto

Opiskeluoikeuden päätason suorituksen koulutusmoduuli_koodisto.
Tutkintokoulutukset (ammatillinen/lukio) saa eroteltua rajoittamalla tämän kentän arvolla 'koulutus'.
HUOM. Valma-koulutuksen sekä ammatillisen koulutuksen jossa tavoitteena on suorittaa
tutkinnonosa tai osia on tässä kentässä myös arvo 'koulutus', eli ammatillisen koulutuksen
tutkintotavoitteisia koulutuksia eroteltaessa tulee nämä suodattaa pois myös
suorituksen_tyyppi-muuttujan avulla. HUOM. Ei välttämättä toimi täysin oikein ib-tutkinnon
opiskelijoille, mutta näiden voidaan olettaa olevan tutkintokoulutuksessa. HUOM! Ammatilliseen
tehtävään valmistavilla koulutuksilla on tässä kentässä arvo
'ammatilliseentehtavaanvalmistavakoulutus'

#### `Suoritustapa_nimi` — Suoritustapa nimi

Relevantti ammatillisen koulutuksen opiskeluoikeuksille, kertoo suorittaako opiskelija ammatillisen
perustutkinnon näyttönä ('nayttotutkinto'), opetussuunnitelmaperusteisesti
('ammatillinenperustutkinto'), vai reformin mukaisesti ('reformin mukainen naytto')

#### `tutkinnon_nimi_perusteessa` — ammatillisen tutkinnon nimi

Ammatillisen tutkinnon nimi. Relevantti ammatillisen koulutuksen opiskeluoikeuksille silloin, kun päätason suorituksen_tyyppi on 'ammatillinentutkinto' tai 'ammatillinentutkintoosittainen'

#### `tutkintonimike_koodiarvo` — Tutkintonimike koodiarvo

Tutkintonimikkeen koodiarvo, koodisto: https://opintopolku.fi/koski/dokumentaatio/koodisto/tutkintonimikkeet/latest

#### `toinenTutkintonimike` — Toinen tutkintonimike

Onko kyse uuden tutkintonimikkeen suorituksesta liittyen aiemmin suoritettuun tutkintoon (t/f).

#### `toinenOsaamisala` — Toinen osaamisala

Onko kyse uuden osaamisalan suorituksesta liittyen aiemmin suoritettuun tutkintoon (t/f)

#### `koulutusmoduuli_laajuus_arvo` — Opiskeluoikeuden päätason suorituksen laajuuden arvo

Opiskeluoikeuden päätason suorituksen laajuuden arvo. 
Relevantti joillekin tuva-, luva sekä valma-koulutuksen opiskeluoikeuksille. Lisäksi monet muun
ammatillisen koulutuksen (suorituksen_tyyppi='muuammatillinenkoulutus') opiskeluoikeudet
koostuvat vain päätason suorituksesta, jolloin niiden laajuus on määritelty vain tässä kentässä.

#### `koulutusmoduuli_laajuus_yksikko` — Opiskeluoikeuden päätason suorituksen laajuuden yksikko

Opiskeluoikeuden päätason suorituksen laajuuden yksikkö:
1: opintoviikko 
2: opintopistettä 
3: vuosiviikkotuntia 
4: kurssia 
5: tuntia 
6: osaamispistettä 
7: vuotta 
8: viikkoa (TUVA-laajuusyksikkö)

#### `osaamisala_nimi` — Päätason suoritukseen liittyvän osaamisalan nimi

Päätason suoritukseen liittyvän osaamisalan nimi. Relevantti ammatillisen koulutuksen opiskeluoikeuksille.

#### `osaamisala_koodiarvo` — Päätason suoritukseen liittyvän osaamisalan koodiarvo

Päätason suoritukseen liittyvän osaamisalan koodiarvo. Relevantti ammatillisen koulutuksen opiskeluoikeuksille.

#### `oppimaara_koodiarvo` — oppimäärä koodiarvo

Päätason suorituksen oppimäärä lukiokoulutuksen opiskelijoille, kertoo opiskeleeko opiskelija nuorten opintosuunnitelman mukaan ('nuortenops') vai aikuisten opintosuunnitelman mukaan ('aikuistenops').

#### `tuva_jarjestamislupa` — tuva jarjestamislupa

Tieto siitä, minkä koulutuksen järjestämisluvan puitteissa tutkintokoulutukseen valmentavaa koulutusta järjestetään. Relevantti vain tuva-koulutuksen opiskeluoikeuksille.

---

[← Back to catalogue](../../README.md)
