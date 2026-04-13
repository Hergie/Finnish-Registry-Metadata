# MIGR_OLESK Oleskelulupatiedot - Hakemukset

- **Identifier:** `MIGR_OLESK_jua_hakemukset_000.xml`
- **DOI:** `std_2025-05_2025-05-19_ain_0001`
- **Temporal coverage:** 2011-01-01 - 2024-12-31
- **Published:** 2026-04-13
- **Organisation:** Tilastokeskus
- **Variable count:** 17
- **Observation count:** —
- **Population:** Oleskelulupaa ja kv suojelua hakeneet

## Kuvaus / Description

<h3>MIGR_OLESK Oleskelulupatiedot</h3>
Maahanmuuttoviraston koostaman oleskelulupatietoja sisältävän aineiston rekisterinpitäjyys on siirtynyt Tilastokeskukselle, mikä tarkoittaa sitä, että aineistoa luvittaa tutkimuskäyttöön sekä tilastollisiin selvityksiin jatkossa Tilastokeskuksen tutkijapalvelut. 

Kyseisistä tiedoista on muodostettu valmisaineisto, joka sisältää haetut oleskeluluvat vuodesta 2011 päätöksineen ja peruutuksineen, sekä tiedot myönteisistä kansalaisuuspäätöksistä ja voimassa olevista kansalaisuuksista. Valmisaineisto koostuu tauluista <i>hakemukset</i>, <i>päätökset ja peruutukset</i>, <i>kansalaisuuspäätös</i>, <i>voimassaolevat</i> sekä <i>yhteystiedot</i>. <b>Tällä sivulla on aineistokuvaus taululle Hakemukset.</b>  Oleskelulupaa hakeneille henkilöille valmisaineistosta löytyy syntymävuosi, sukupuoli, kansalaisuus sekä postinumeroalue. 

Aineistosta on suojattu yksilöivät tunnisteet ja poistettu suoran tunnistamisen mahdollisuus. Taulut linkittyvät toisiinsa pseudonymisoiduilla tunnisteilla asianumero, toimenpiteen numero, henkilönumero ja Migrin asiakasnumero. Aineistosta on karkeistettu piiloon arkaluontoisimmat oleskelulupahakemusten käsittelyperusteet. Tietojen laatu on vaihtelevaa, ja pyrimme kuvaamaan esiin nousseet puutteet aineiston käytön helpottamiseksi. Valmisaineiston sisältö on arkaluonteista, ja se luvitetaan tutkimuskäyttöön tai tilastollisiin selvityksiin vain hyvin perustein. Kaikilta aineistoa käyttöönsä hakevilta vaaditaan DPIA eli tietosuojan vaikutusten arviointi. Aineiston päivityssykli pyritään saamaan jopa kuukausitasolle, kunhan tietojen toimitusprosessi vakiintuu. 

Oleskelulupa-aineisto on uutta Tilastokeskuksella, ja vasta kartutamme substanssiosaamistamme kyseiseen aiheeseen. Tästä syystä valmisaineistoon voi tulla vielä käytettävyyttä parantavia muutoksia. 

Viralliset oleskelulupahakemuksien ja -päätöksien tilastot laatii edelleen Maahanmuuttovirasto. Aihepiirin tilastoja voi tarkastella <a href="https://tilastot.migri.fi/" > Migrin tilastointipalvelusta</a>. 
Aiheeseen ja terminologiaan voi tutustua tarkemmin <a href="https://migri.fi/oleskelulupa" > Maahanmuuttoviraston sivuilla</a>.

Kysymykset valmisaineistosta ja koko tietosisällöstä voi osoittaa Tilastokeskuksen tutkijapalveluihin tutkijapalvelut@stat.fi.

## Muuttujat / Variables (17)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `CASE_ID_s` | Suojattu asianumero | — | — | — |
| `MEASURE_ID_s` | Suojattu toimenpiteen numero | — | — | — |
| `CUSTOMER_ID_s` | Suojattu asiakasnumero | — | — | — |
| `hid_e` | Suojattu henkilön yksilöivä tunniste | — | — | — |
| `TILASTOVUOSI` | — | — | — | — |
| `TILASTOKUUKAUSI` | — | — | — | — |
| `SPONSOR_CASE_ID_s` | Perheenkokoajan suojattu oleskelulupahakemuksen id | — | — | — |
| `SPONSOR_CUSTOMER_ID_s` | Perheenkokoajan suojattu asiakasnumeron | — | — | — |
| `CASE_TYPE_NAME_FIN` | Asiatyyppi | — | — | — |
| `CASE_GROUP_NAME_FIN` | Asiaryhma | — | — | — |
| `PROCESSING_GROUNDS_GROUP` | Kasittelyperustetaso | — | — | — |
| `PROCESSING_GROUNDS_NAME_FIN` | Kasittelyperuste | — | — | — |
| `INIT_AUTHORITY` | Vireyttäjän organisaatio | — | — | — |
| `INIT_AUTHORITY_UNIT` | Vireyttäjän organisaation yksikkö | — | — | — |
| `INIT_AUTHORITY_OFFICE` | Vireyttäjän organisaation tulosalue | — | — | — |
| `measure_conf_month` | Vahvistusajankohta kk-tasolla | — | — | — |
| `initiation_month` | Hakemuksen vireilletuloajankohta kk-tasolla | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `CASE_ID_s` — Suojattu asianumero

Asian yksilöivä tunniste joka syntyy asian vireillepanossa. Vireillepanotoimenpide luo asian, johon myöhemmin kertyy asian käsittelyä varten tehdyt toimenpiteet. Asianumeroa voidaan käyttää yhdistämään samaan asiaan tehdyt muut toimenpiteet, kuten osapäätökset, päätökset tai työehdot toimenpiteet

#### `MEASURE_ID_s` — Suojattu toimenpiteen numero

Vireillepanotoimenpiteen (hakemuksen) yksilöllinen tunnus

#### `CUSTOMER_ID_s` — Suojattu asiakasnumero

Asiakkaan yksilöivä tunniste, käytetään yhdistämään samalle asiakkaalle tehnyt muut asiat ja toimenpiteet.

#### `hid_e` — Suojattu henkilön yksilöivä tunniste

#### `TILASTOVUOSI`

#### `TILASTOKUUKAUSI`

#### `SPONSOR_CASE_ID_s` — Perheenkokoajan suojattu oleskelulupahakemuksen id

Jos kyseessä on esimerkiksi perhesiteen perusteella haettava oleskelulupa, tässä on näkyvillä päähakijan (perheenkokoojan) asianumero.

#### `SPONSOR_CUSTOMER_ID_s` — Perheenkokoajan suojattu asiakasnumeron

Jos kyseessä on esimerkiksi perhesiteen perusteella haettava oleskelulupa, tässä on näkyvillä päähakijan (perheenkokoojan) asiakasnumero. Huomioitava, että kyseessä on hakemushetken perheenkokoaja, joka voi vaihtua myöhemmin. Aineistoon on tarkoitus lisätä perheenkokoaja-taulu, jossa perheenkokoajatiedon historiatiedot.

#### `CASE_TYPE_NAME_FIN` — Asiatyyppi

case_type_name_fin case_type_id
EU oleskeluoikeus 63
Ensimmäistä oleskelulupaa koskeva hakemus 59
Jatkolupahakemus 60
Kiintiöpakolaisvalinta, UNHCR:n esitys, Humanitaarinen maahanmuutto, VN:n päätös 46
Oleskeluasema 532000
Oleskelutodistukset ja -ilmoitukset 83
Pitkäaikainen viisumi 488002
Pysyvää oleskelulupaa koskeva hakemus 61
Tilapäinen suojelu 48
Turvapaikkahakemus 49

#### `CASE_GROUP_NAME_FIN` — Asiaryhma

Lupatyyppi ilmaistaan Migrissä neljällä eri muuttujalla, jotka ovat hierarkkisessa suhteessa toisiinsa. Asiaryhmä on lupatyypin ylin hierarkia taso, joka jakautuu edelleen asiatyyppeihin, käsittelyperustetasoihin ja käsittelyperusteisiin, joista viimeisin lupatyypin tarkin taso. Asiaryhmiä ovat esimerkiksi Oleskeluluvat, Kansalaisuushakemukset, Kansainvälinen suojelu

#### `PROCESSING_GROUNDS_GROUP` — Kasittelyperustetaso

Hakemuksen perusteen yläkategoria:

processing_grounds_group processing_grounds_group_id
EU-kansalainen 490003
Ensimmäinen hakemus 490001
Kiintiöpakolaisvalinta 460001
Kv-suojelua saaneiden jatkoluvat 50
Muut 4
Oleskeluasema 532001
Oleskelutodistukset ja -ilmoitukset 830001
Opiskelu 3
Perhe 1
Perheenjäsenen oleskelukortti 1005
Pitkäaikainen viisumi 488001
Pitkään oleskelleen kolmannen maan kansalaisen EU -oleskelulupa 2000
Pysyvä oleskelulupa 2001
Sisäinen siirto 490004
Tilapäinen suojelu 480001
Työ 2
Uusintahakemus 490002

#### `PROCESSING_GROUNDS_NAME_FIN` — Kasittelyperuste

Hakemuksen peruste: Esimerkiksi Eritysasiantuntija, Suomen kansalaisen puoliso. 
Valmisaineistossa käsittelyperuste karkeistetaan niin, että arkaluontoisimmat käsittelyperusteet peittyvät.

processing_grounds_name_fin
611-ryhmään liittyvä oleskelulupahakemus
Adoptio
Au pair
D-viisumi
EU-kansalaisen perheenjäsenen pysyvää oleskelukorttia koskeva hakemus
EU-kansalaisen rekisteröinti
EU-kansalaisen rekisteröinti, Elinkeinonharjoittaminen
EU-kansalaisen rekisteröinti, opiskelu
EU-kansalaisen rekisteröinti, perheside
EU-kansalaisen rekisteröinti, riittävä toimeentulo
EU-kansalaisen rekisteröinti, työnteko
Entinen Suomen kansalainen, suomalainen syntyperä
Erityisasiantuntija
Erityisasiantuntija, sininen kortti
Erosopimuksen mukainen oleskeluoikeus
Erosopimuksen mukainen perheenjäsenen oleskeluoikeus
Erosopimuksen mukainen perheenjäsenen pysyvä oleskeluoikeus
Erosopimuksen mukainen pysyvä oleskeluoikeus
Harjoittelija
Ilmoitus lyhytaikaisesta liikkumisesta
Ilmoitus opiskelijan liikkumisesta
Ilmoitus tutkijan liikkumisesta
Ilmoitus tutkijan perheenjäsenen liikkumisesta
Kansallinen tutkija
Kasvuyrittäjä
Kausityö
Kausityötodistus
Kiintiöpakolaisvalintaesitys
Kiintiöpakolaisvalintaesitys, EU
Kv. Suojelua saaneen huoltaja
Kv. Suojelua saaneen lapsi
Kv. Suojelua saaneen muu omainen
Kv. Suojelua saaneen puoliso
Kv. suojelua saaneen huoltaja
Kv. suojelua saaneen lapsi
Kv. suojelua saaneen muu omainen
Kv. suojelua saaneen puoliso
Lapsi
Liikkuva sisäinen siirto
Maastapoistamisen este
Muu harjoittelija
Muu omainen
Muu peruste
Muu työnteko
Muun ulkomaalaisen huoltaja
Muun ulkomaalaisen lapsi
Muun ulkomaalaisen muu omainen
Muun ulkomaalaisen puoliso
Oleskelukortin uusiminen
Oleskelulupa suojelun tarpeen perusteella
Opiskelu
Oleskelulupakortin uusiminen
Oleskeluluvan peruuttaminen
Osaratkaisua edellyttävä kausityö
P-EU -asema toisessa valtiossa
Pakolaisasema
Paluumuuttaja
Perheenjäsenen oleskelukortti, ei EU-kansalainen
Perhesidelupa
Pitkään oleskelleen EU-oleskelulupahakemus
Puoliso
Pysyvä oleskelulupa muulla perusteella
Pysyvä oleskelulupa perhesiteen perusteella
Pysyvä oleskelulupa suojelun perusteella
Pysyvä oleskelulupa työnteon perusteella
Pysyvä oleskelulupa yrittämisen perusteella
Pysyvän statuksen vaihtaminen
Pysyvän statuksen vaihtaminen oleskelukortti
Pysyvää oleskelulupaa koskeva hakemus
Seurustelusuhde
Sisäinen siirto
Suomen kansalaisen huoltaja
Suomen kansalaisen lapsi
Suomen kansalaisen muu omainen
Suomen kansalaisen puoliso
Suomessa tutkinnon tai tutkimuksen suorittanut
Tieteellinen tutkimus
Tilapäinen suojelu
Tilapäistä suojelua koskeva asia
Tilapäistä suojelua koskeva asia, alaikäinen yksin tullut
Toissijaisen suojelun asema
Turvapaikkahakemus, EU-kansalainen
Turvapaikkahakemus, aikuinen
Turvapaikkahakemus, mukana hakeva alaikäinen
Turvapaikkahakemus, sisäinen siirto aikuinen
Turvapaikkahakemus, sisäinen siirto alaikäinen yksin tullut
Turvapaikkahakemus, sisäinen siirto mukana tullut alaikäinen
Turvapaikkahakemus, uusintahakemus
Turvapaikkahakemus, uusintahakemus aikuinen
Turvapaikkahakemus, uusintahakemus mukana hakeva alaikäinen
Turvapaikkahakemus, uusintahakemus yksin tullut alaikäinen
Turvapaikkahakemus, yksin tullut alaikäinen
Työnantajan moitittava menettely
Työnhaku
Työntekijän oleskelulupa
Urheilu ja valmentaminen
VN:n esitys henkilöstä ja lupa
Vapaaehtoistoiminta
Working holiday
Yksilöllinen, inhimillinen syy
Yrittäjä

#### `INIT_AUTHORITY` — Vireyttäjän organisaatio

Hakemuksen vireyttäjän organisaatiotieto hakemuksen vireytyshetkeltä. Tämä ei ole sama kuin hakemuksen vireytyspaikka, vaikka tästä voi päätellä missä hakemus todennäköisesti on vireytetty. Esimerkiksi "poliisi", "edustustot", "rajavartiolaitos".

#### `INIT_AUTHORITY_UNIT` — Vireyttäjän organisaation yksikkö

Hakemuksen vireyttäjän organisaatiotieto hakemuksen vireytyshetkeltä. Tämä ei ole sama kuin hakemuksen vireytyspaikka, vaikka tästä voi päätellä missä hakemus todennäköisesti on vireytetty. Esimerkiksi "Hämeenlinnan pa", "Pietari", "Kapkaupunki".

#### `INIT_AUTHORITY_OFFICE` — Vireyttäjän organisaation tulosalue

Hakemuksen vireyttäjän organisaatiotieto hakemuksen vireytyshetkeltä. Tämä ei ole sama kuin hakemuksen vireytyspaikka, vaikka tästä voi päätellä missä hakemus todennäköisesti on vireytetty. Esimerkiksi "Helsinkin pl", "Kanta-Hämeen pl", "Turkki".

#### `measure_conf_month` — Vahvistusajankohta kk-tasolla

Mikäli hakemus on laitettu vireille ns. automaattisen vireillepanon prosessissa hakemuksen päivämäärä ja päivämäärä, jolloin hakemus on tullut vireille Umassa on tyypillisesti sama pvm. Hakemuksissa ja päätöksissä käytetty tilastopäivämäärä. Päivämäärä on karkeistettu kuukausitasolle.

#### `initiation_month` — Hakemuksen vireilletuloajankohta kk-tasolla

Päivämäärä, jolloin hakemus jätetty (Hakemuslomakkeeseen merkitty arvo), voi erota päivämäärästä jolloin hakemus on kirjattu järjestelmään. Päivämäärä on karkeistettu kuukausitasolle.

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
