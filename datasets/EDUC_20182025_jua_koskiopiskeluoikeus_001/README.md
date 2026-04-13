# EDUC_KOSKI -Opiskeluoikeus

- **Identifier:** `EDUC_20182025_jua_koskiopiskeluoikeus_001.xml`
- **DOI:** `opiskt_2025-10_2025-10-23_ain_0001`
- **Temporal coverage:** —
- **Published:** 2025-11-13
- **Organisation:** Tilastokeskus
- **Variable count:** 25
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


Suppea moduuli EDUC_KOSKI_JAKSOT: opiskeluoikeus perustiedot

Sisältää koski-tietovarannon tietoja opiskeluoikeuksista.

Moduulia voidaan käyttää, kun tutkitaan koulutuksessa läsnäoloa sekä koulutuksen kestoa. Yhdistää tietoja KOSKI-raporttikannan tauluista: r_opiskeluoikeus, r_henkilo, r_paatason_suoritus. Sisältää seuraavat tiedot: Tila (läsnäolo, valmistuminen yms.), suojattu oppilaitostunnus, koulutusmuoto, tutkintonimike, oppimäärä, laajuus.
Rajoitukset: koulutusmuoto (ammatillinenkoulutus, lukiokoulutus, ibtutkinto, luva, tuva, perusopetuksenlisaopetus, perusopetus, vapaansivistystyonkoulutus). Mitätöidyt opiskeluoikeudet rajattu ulos. Arkaluontoiset tiedot jätetty ulkopuolelle.

Monet muun ammatillisen koulutuksen (suorituksen_tyyppi='muuammatillinenkoulutus') opiskeluoikeudet koostuvat vain päätason suorituksesta ja eivät näy ammatillisen koulutuksen suoritustauluissa. Tieto näiden koulutuksien mahdollisesta laajuudesta selviää opiskeluoikeus-taulusta. Nämä koulutukset voivat olla esimerkiksi yhden päivän mittaisia kursseja.

Yhdistää tietoja KOSKI raporttikannan tauluista: r_opiskeluoikeus, r_paatason_suoritus, r_organisaatio, r_henkilo.

## Muuttujat / Variables (25)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `shnro` | Suojattu henkilönumero | — | — | — |
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
| `koulutusmoduuli_koodisto` | Opiskeluoikeuden päätason suorituksen koulutusmoduuli_koodisto | — | — | — |
| `tutkinnon_nimi_perusteessa` | ammatillisen tutkinnon nimi | — | — | — |
| `Suoritustapa_nimi` | Suoritustapa nimi | — | — | — |
| `osaamisala_nimi` | Päätason suoritukseen liittyvän osaamisalan nimi | — | — | — |
| `osaamisala_koodiarvo` | Päätason suoritukseen liittyvän osaamisalan koodiarvo | — | — | — |
| `koulutusmoduuli_koodiarvo` | Opiskeluoikeuden päätason suorituksen koulutusmoduuli koodiarvo | — | — | — |
| `koulutusmoduuli_laajuus_arvo` | Opiskeluoikeuden päätason suorituksen laajuuden arvo | — | — | — |
| `koulutusmoduuli_laajuus_yksikko` | Opiskeluoikeuden päätason suorituksen laajuuden yksikko | — | — | — |
| `oppimaara_koodiarvo` | oppimäärä koodiarvo | — | — | — |
| `tuva_jarjestamislupa` | tuva jarjestamislupa | — | — | — |
| `vahvistus_paiva` | Vahvistus päivä | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `shnro` — Suojattu henkilönumero

Suojattu henkilönumero

#### `oppija_oid_s` — Suojattu oppijatunnus

Suojattu OPH:n oppijatunnus

#### `opiskeluoikeus_oid_s` — Suojattu opiskeluoikeuden tunniste

Suojattu OPH:n opiskeluoikeuden tunniste

#### `oppilaitos_oid_s` — Suojattu Oppilaitoksen tunniste

Suojattu Oppilaitoksen tunniste

#### `oppilaitosnumero_s` — Suojattu oppilaitosnumero

Suojattu oppilaitosnumero

#### `sis_opiskeluoikeuteen_oid_s` — sisaltyy opiskeluoikeuteen oid

Suojattu OPH:n opiskeluoikeuden tunniste, joissain tapauksissa opiskeluoikeuden toimija ostaa koulutuksen toiselta koulutustoimijalta, näissä tapauksissa linkki opiskeluoikeuksien väliltä löytyy tästä kentästä. ks. tarkemmat lisätiedot OPH:n eduuni-wikistä (https://wiki.eduuni.fi/spaces/OPHPALV/pages/431685903/r_opiskeluoikeus)

#### `oppilaitos_kotipaikka` — Oppilaitoksen kotikunta

Oppilaitoksen kotikunnan kuntakoodi

#### `koulutustoimija_oid_s` — Suojattu koulutustoimijan tunniste

Suojattu koulutustoimijan tunniste

#### `koulutustoimija_y_tunnus` — suojattu koulutustoimijan y-tunnus

suojattu koulutustoimijan y-tunnus

#### `koulutusmuoto` — koulutusmuoto

Huom. ammatilliseen koulutukseen kuuluu monta eri tyyppistä koulutusta (tutkintokoulutuksen lisäksi esim. valma-koulutus), joten niiden tunnistamiseen täytyy lisäksi käyttää suorituksen_tyyppi-kenttää

#### `alkamispaiva` — Opiskeluoikeuden alkamispäivä

Opiskeluoikeuden alkamispäivä

#### `paattymispaiva` — Opiskeluoikeuden päättymispäivä

Opiskeluoikeuden päättymispäivä

#### `viimeisin_tila` — Opiskeluoikeuden viimeisin tila

Opiskeluoikeuden tila aineiston generointiajankohtana

#### `suorituksen_tyyppi` — Opiskeluoikeuden päätason suorituksen suorituksen tyyppi

Suorituksen tyyppi, joka yksilöi millaisesta päätason suorituksessa on kyse (esimerkiksi ammatillisessa koulutuksessa tieto kertoo sen, suoritetaanko kokonaista tutkintoa, tutkinnon osaa/osia, tutkinnon osaa pienemmistä kokonaisuuksista koostuvaa suoritusta, muun ammatillisen koulutuksen suoritusta, VALMA-koulutusta). Opiskeluoikeus-tauluun poimitaan tiedot yhdestä päätason suorituksesta priorisoiden lukiokoulutuksessa lukion oppimäärän suoritusta, ammatillisessa koulutuksessa tutkinnon tai tutkinnon osan/osien suoritusta, perusopetuksessa oppimäärän suoritusta yms.

#### `koulutusmoduuli_koodisto` — Opiskeluoikeuden päätason suorituksen koulutusmoduuli_koodisto

Tutkintokoulutukset (ammatillinen/lukio) saa eroteltua rajoittamalla tämän kentän arvolla 'koulutus'. HUOM. Valma-koulutuksen sekä ammatillisen koulutuksen jossa tavoitteena on suorittaa tutkinnonosa tai osia on tässä kentässä myös arvo 'koulutus', eli ammatillisen koulutuksen tutkintotavoitteisia koulutuksia eroteltaessa tulee nämä suodattaa pois myös suorituksen_tyyppi-muuttujan avulla. HUOM. Ei välttämättä toimi täysin oikein ib-tutkinnon opiskelijoille, mutta näiden voidaan olettaa olevan tutkintokoulutuksessa. HUOM! Ammatilliseen tehtävään valmistavilla koulutuksilla on tässä kentässä arvo 'ammatilliseentehtavaanvalmistavakoulutus'

#### `tutkinnon_nimi_perusteessa` — ammatillisen tutkinnon nimi

Relevantti ammatillisen koulutuksen opiskeluoikeuksille silloin kun päätason suorituksen_tyyppi on 'ammatillinentutkinto' tai 'ammatillinentutkintoosittainen'

#### `Suoritustapa_nimi` — Suoritustapa nimi

Relevantti ammatillisen koulutuksen opiskeluoikeuksille, kertoo suorittaako opiskelija ammatillisen perustutkinnon 1.1.2018 voimaan tulleen lain ammatillisesta koulutuksesta mukaisesti ('reformin mukainen naytto') vai 13.12.2017 asti voimassa olleen lain mukaan. 13.12.2017 voimassa olleiden lakien mukaisessa opetuksessa olleet saavat suoritustapa_nimi arvot ('ammatillinenperustutkinto) opetussuunnitelmaperusteisesta ammatillisesta peruskoulutuksesta ja  ('nayttotutkinto) ammatillisen aikuiskoulutuksen mukainen näyttötutkinto.

#### `osaamisala_nimi` — Päätason suoritukseen liittyvän osaamisalan nimi

Relevantti ammatillisen koulutuksen opiskeluoikeuksille

#### `osaamisala_koodiarvo` — Päätason suoritukseen liittyvän osaamisalan koodiarvo

Relevantti ammatillisen koulutuksen opiskeluoikeuksille

#### `koulutusmoduuli_koodiarvo` — Opiskeluoikeuden päätason suorituksen koulutusmoduuli koodiarvo

Opiskeluoikeuden päätason suorituksen koulutusmoduuli koodiarvo. HUOM! Lukion aineopiskelijoilla joilla päätason suorituksen tyyppi on 'lukionoppiaineenoppimaara' voi opiskeluoikeuteen sisältyä useampi päätason suoritus, opiskeluoikeus-tauluun poimitaan tiedot vain yhdestä päätason suorituksesta, joten muuttuja koulutusmoduuli_koodiarvo ei kattavasti näiden opiskelijoiden tapauksessa kerro koulutuksen sisällöstä. Kurssitason suoritustiedot löytyvät toisen asteen moduulin lukio/ib-suoritustaulusta.

#### `koulutusmoduuli_laajuus_arvo` — Opiskeluoikeuden päätason suorituksen laajuuden arvo

Relevantti joillekin tuva-, luva sekä valma-koulutuksen opiskeluoikeuksille. Lisäksi monet muun ammatillisen koulutuksen (suorituksen_tyyppi='muuammatillinenkoulutus') opiskeluoikeudet koostuvat vain päätason suorituksesta, jolloin niiden laajuus on määritelty vain tässä kentässä.

#### `koulutusmoduuli_laajuus_yksikko` — Opiskeluoikeuden päätason suorituksen laajuuden yksikko

Opiskeluoikeuden päätason suorituksen laajuuden yksikko

#### `oppimaara_koodiarvo` — oppimäärä koodiarvo

Päätason suorituksen oppimäärä lukiokoulutuksen opiskelijoille, kertoo opiskeleeko opiskelija nuorten opintosuunnitelman mukaan ('nuortenops') vai aikuisten opintosuunnitelman mukaan ('aikuistenops')

#### `tuva_jarjestamislupa` — tuva jarjestamislupa

Tieto siitä, minkä koulutuksen järjestämisluvan puitteissa tutkintokoulutukseen valmentavaa koulutusta järjestetään.

#### `vahvistus_paiva` — Vahvistus päivä

Opiskeluoikeuden päätason suorituksen vahvistus päivä. Huom: päättyneiden opiskeluoikeuksien viimeisen_tilan kanssa kannattaa tarkastella onko päätason suoritus vahvistettu. Esim. joihinkin lukion opiskeluoikeuksiin sisältyy lukion oppimäärän suoritus sekä aineopintojen suoritus ja tällaisissa tapauksissa viimeisin_tila saattaa näkyä tilassa 'eronnut', vaikka lukion oppimäärän suoritus on vahvistettu.

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
