# KEHA_URA-aineisto

- **Identifier:** `KEHA_2022_jua_URA_002.xml`
- **DOI:** `tyonv_2016-10_2016-10-25_ain_0001`
- **Temporal coverage:** 2000-01-01 - 2024-12-31
- **Published:** 2020-08-28
- **Organisation:** Työ- ja elinkeinoministeriö
- **Variable count:** 39
- **Observation count:** 15,293,186
- **Population:** Työnhakijat
- **Source:** KEHA-keskuksen URA-aineistot
- **Keywords:** työmarkkinat,työpaikat,työttömyys,työttömät,työvoimapolitiikka

## Description

KEHA-keskus eli ELY-keskusten sekä TE-toimistojen kehittämis- ja hallintokeskus ylläpitää työhallinnon asiakaspalvelun tietojärjestelmää URAa. 

URA-tietojärjestelmän osa-aineistoja ovat: Työtarjoukset avoimiin työpaikkoihin, Työtarjoukset palkkatukipaikkoihin, Suunnitelmat, Yhteydenottotavat, Palvelulinja, Sanssikortti, Maahanmuuttajien kielitaito, Kaikkien kielitaito) 

Muut kuin työnvälitystilaston tiedot on yhdistetty vuosien 2000 - 2010 ja  2011-2014 osalta, ja tämän jälkeen vuosittaiset aineistot ovat erikseen. Vuosien 2000-2010 tiedot on vain 8., 18. ja 28. päivinä syntyneille.  Vuosien 2000-2010 tiedostot, joista löytyy apvm- ja lpvm-muuttujat, on poimittu ehdolla, että työnhaku oli voimassa 2000-2010 ja se oli alkanut vuonna 1995 tai myöhemmin kun taas vuoden  2011 jälkeen tiedostot, joista löytyy apvm- ja lpvm-muuttujat, on poimittu ehdolla, että työnhaku oli voimassa vuonna 2011 tai myöhemmin, ja se oli alkanut vuonna 2000 tai myöhemmin. 

Tiedot ovat URAssa  pääasiassa jaksoittain siten, että mahdolliset uudet tiedot esimerkiksi asiakkaan työllisyys- ja työttömyysjaksoista sekä asiakkaaseen kohdistetuista työvoimapoliittisista toimenpiteistä lisätään jo olemassa olevien tietojen rinnalle. Luokituksista työnhakijan asiointikieli ja kansalaisuus kirjataan järjestelmään kuitenkin niin, että esimerkiksi asiakkaan kansalaisuuden muuttuessa uusi koodi ei kirjaudu vanhan rinnalle vaan korvaa sen, jolloin vanhentunut tieto poistuu rekisteristä. *** URA-järjestelmästä on poistettu vanhentuneita tietoja ennen tietojen arkistointia. Siksi esimerkiksi vuosina 2000-2006 tehtyjen työtarjousten kaikki taustatiedot puuttuvat (mutta päivämäärät löytyvät)

Tässä kuvauksessa on yhdistetty kaikkien osa-aineistojen muuttujakuvaukset. Valitsemalla muuttujaryhmää pystyy erottelemaan eri osa-aineistojen muuttujat. Tiedot päivittyvät Tilastokeskukseen tallennettuun tutkimusaineistoon kerran vuodessa. 

Aineistojen käsittely tapahtuu FIONA etäkäyttöjärjestelmässä. Käyttölupaa aineistoon haetaan Tilastokeskuksesta.

## Variables (39)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `hid_e` | Suojattu henkilön yksilöivä tunniste | — | — | Kaikkien_kielitaito, Maahanmuuttajien_kielitaito, Palkkatukipaikat, Palvelulinja, Sanssikortti, Suunnitelmat, Tyotarjoukset, Yhteydenottotavat |
| `yrtun_s` | Työnantajan suojattu tunnus | — | — | Palkkatukipaikat, Tyotarjoukset |
| `syntyv` | Syntymävuosi | — | — | Vaestorakenne |
| `sukup` | Sukupuoli | — | sukupuoli_2_1970_01_01 | Vaestorakenne |
| `aidinkielikoodi` | Äidinkieli | — | — | Maahanmuuttajien_kielitaito |
| `allekpvm` | Allekirjoituspäivämäärä | — | — | Suunnitelmat |
| `ammattikoodi` | Työn ammatti | — | — | Palkkatukipaikat, Tyotarjoukset |
| `apvm` | Työnhaun alkamispäivä | — | — | Palvelulinja, Sanssikortti |
| `hakijanaidinkieli` | Hakijan äidinkieli | — | — | Maahanmuuttajien_kielitaito |
| `ilmoitusnumero` | ilmoitusnumero | — | — | Tyotarjoukset |
| `kansalaisuus` | Kansalaisuus muu kuin suomi | — | — | Maahanmuuttajien_kielitaito |
| `kesatyo` | Työtarjous on kesätyöpaikkaan | — | — | Tyotarjoukset |
| `kielikirjtaso` | Kirjallinen taito | — | — | Kaikkien_kielitaito |
| `kielisuulltaso` | Suullinen taito | — | — | Kaikkien_kielitaito |
| `kielitaito` | Kielitaito | — | — | Maahanmuuttajien_kielitaito |
| `kieliyleinentaso` | Kielitaidon yleinen taso | — | — | Maahanmuuttajien_kielitaito |
| `kuntakoodi` | Työtarjouksen työpaikan sijaintikunta | — | — | Tyotarjoukset, Palkkatukipaikat |
| `lpvm` | Työnhaun päättymispäivä | — | — | Sanssikortti, Palvelulinja |
| `oppisopimus` | Työtarjous on oppisopimuspaikkaan | — | — | Tyotarjoukset |
| `osoitettupvm` | Työtarjouksen päivämäärä | — | — | Tyotarjoukset, Palkkatukipaikat |
| `segmenttikoodi` | Segmentti | — | — | Palvelulinja |
| `segmenttipvm` | Segmenttipäivämäärä | — | — | Palvelulinja |
| `sijmahdnumero` | Sijoitusmahdollisuus | — | — | Palkkatukipaikat |
| `sijtyoaikakoodi` | Sijoitustyöpaikan työn työaika | — | — | Palkkatukipaikat |
| `toimiala` | Työnantajan toimiala | — | — | Tyotarjoukset, Palkkatukipaikat |
| `toimikoodi` | Suunnitelmassa sovitetut tehtävä | — | — | Suunnitelmat |
| `toimipvm` | Päivämäärä, mihin mennässä tehtävä on suoritettava | — | — | Suunnitelmat |
| `toimkasitelty` | Onko tehtävä toteutunut vai ei | — | — | Suunnitelmat |
| `toimsuunlaji` | Suunnitelman laji | — | — | Suunnitelmat |
| `toimviimpvm` | Tarkistuspäivämäärä | — | — | Suunnitelmat |
| `tuloskoodi` | Työtarjouksen tulos | — | — | Tyotarjoukset, Palkkatukipaikat |
| `tyoaikakoodi` | Työn työaika | — | — | Tyotarjoukset |
| `tyok_apvm` | Työllisyyskoodin alkamispvm | — | — | Tyotarjoukset, Palkkatukipaikat |
| `tyok_lpvm` | Työllisyyskoodin loppumispvm | — | — | Palkkatukipaikat, Tyotarjoukset |
| `tyollkoodi` | Työllisyyskoodi | — | — | Palkkatukipaikat, Tyotarjoukset |
| `tyonkestokoodi` | Työn kesto | — | — | Tyotarjoukset |
| `tyosuhttyyppi` | Työsuhteen tyyppi | — | — | Tyotarjoukset |
| `yhtottopvm` | Yhteydenottopäivämäärä | — | — | Yhteydenottotavat, Sanssikortti |
| `yhtottotapa` | Yhteydenottotapa (uuden koodit käytössä 5.12.2010 alkaen) | — | — | Yhteydenottotavat |

### Variable definitions

#### `hid_e` — Suojattu henkilön yksilöivä tunniste

**Group:** Kaikkien_kielitaito, Maahanmuuttajien_kielitaito, Palkkatukipaikat, Palvelulinja, Sanssikortti, Suunnitelmat, Tyotarjoukset, Yhteydenottotavat

Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e -tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä.

#### `yrtun_s` — Työnantajan suojattu tunnus

**Group:** Palkkatukipaikat, Tyotarjoukset

#### `syntyv` — Syntymävuosi

**Group:** Vaestorakenne

Henkilön syntymävuosi

#### `sukup` — Sukupuoli

**Classification:** sukupuoli_2_1970_01_01 · **Group:** Vaestorakenne

Henkilön sukupuoli

#### `aidinkielikoodi` — Äidinkieli

**Group:** Maahanmuuttajien_kielitaito

Kieliluokitus. Katso Tilastokeskuksen henkilöluokitukset

#### `allekpvm` — Allekirjoituspäivämäärä

**Group:** Suunnitelmat

Poiminta tehdään tämän mukaan

#### `ammattikoodi` — Työn ammatti

**Group:** Palkkatukipaikat, Tyotarjoukset

Tarjotun työn ammatti : Työnhakijan ammatin luokittelemiseen käytetään Pohjoismaiseen ammattiluokitukseen (Nordisk Yrkesklassificering, NYK) perustuvaa luokitusta, jonka sisältö on pyritty muokkaamaan mahdollisimman hyvin Suomen oloja vastaavaksi. Työ- ja elinkeinoministeriön käyttämä ammattiluokitus poikkeaa jonkin verran Tilastokeskuksen vastaavasta.

#### `apvm` — Työnhaun alkamispäivä

**Group:** Palvelulinja, Sanssikortti

#### `hakijanaidinkieli` — Hakijan äidinkieli

**Group:** Maahanmuuttajien_kielitaito

Kieli selväkielisenä (puutteellinen)

#### `ilmoitusnumero` — ilmoitusnumero

**Group:** Tyotarjoukset

Työpaikan numero

#### `kansalaisuus` — Kansalaisuus muu kuin suomi

**Group:** Maahanmuuttajien_kielitaito

Maakoodit. Katso Tilastokeskus alueluokitukset

#### `kesatyo` — Työtarjous on kesätyöpaikkaan

**Group:** Tyotarjoukset

#### `kielikirjtaso` — Kirjallinen taito

**Group:** Kaikkien_kielitaito

Vuodesta 2020 alkaen nimellä szkielikirjtaso. 
01 = äidinkieli  
02 = erittäin hyvä
03 = hyvä  
04 = tyydyttävä  
05 = heikko  
06 = koodi poistetaan

#### `kielisuulltaso` — Suullinen taito

**Group:** Kaikkien_kielitaito

Vuodesta 2020 alkaen nimellä szkielisuulltaso. 
01 = äidinkieli  
02 = erittäin hyvä
03 = hyvä  
04 = tyydyttävä  
05 = heikko  
06 = koodi poistetaan

#### `kielitaito` — Kielitaito

**Group:** Maahanmuuttajien_kielitaito

Vuodesta 2020 alkaen nimellä szkielitaito.

#### `kieliyleinentaso` — Kielitaidon yleinen taso

**Group:** Maahanmuuttajien_kielitaito

Vuodesta 2020 alkaen nimellä szkieliyleinentaso. 
A1.1 = Kielitaidon alkeiden hallinta
A1.2 = Kehittyvä alkeiskielitaito  
A1.3 = Toimiva alkeiskielitaito  
A2.1 = Peruskielitaidon alkuvaihe  
A2.2 = Kehittyvä peruskielitaito  
B1.1 = Toimiva peruskielitaso  
B1.2 = Sujuva peruskielitaito  
B2.1 = Itsenäisen kielitaidon perustaso  
B2.2 = Toimiva itsenäinen peruskielitaito  
X = Kielitaitoa ei ole testattu

#### `kuntakoodi` — Työtarjouksen työpaikan sijaintikunta

**Group:** Tyotarjoukset, Palkkatukipaikat

Rekisterissä kuntakoodeina käytetään Tilastoikeskuksen ylläpitämiä 3-numeroisia kuntakoodeja. Jos työnhakijan asuinpaikka on työnhaun alussa Ruotsissa, merkitään kuntakoodiksi 198, tai Norjassa, merkitään 197, tai muualla ulkomailla, merkitään 200. Katso Tilastokeskus alueluokitukset

#### `lpvm` — Työnhaun päättymispäivä

**Group:** Sanssikortti, Palvelulinja

#### `oppisopimus` — Työtarjous on oppisopimuspaikkaan

**Group:** Tyotarjoukset

#### `osoitettupvm` — Työtarjouksen päivämäärä

**Group:** Tyotarjoukset, Palkkatukipaikat

Poiminta tehty tämän mukaan

#### `segmenttikoodi` — Segmentti

**Group:** Palvelulinja

00 = Ei asiantuntijapalvelun tarvetta  
01 = Työnvälitys- ja yrityspalvelut  
02 = Osaamisen kehittämispalvelut  
03 = Tuetun työllistymisen palvelut  
04 = Etuusasiakas  
05 = Monialainen yhteispalvelu

#### `segmenttipvm` — Segmenttipäivämäärä

**Group:** Palvelulinja

#### `sijmahdnumero` — Sijoitusmahdollisuus

**Group:** Palkkatukipaikat

Sijoitusmahdollisuus on työpaikkakoodi, johon mahdollisesti henkilö sijoitetaan.

#### `sijtyoaikakoodi` — Sijoitustyöpaikan työn työaika

**Group:** Palkkatukipaikat

00 = ei lainkaan - 1v  
01 = 1-5 vuotta  
02 = yli 5 vuotta

#### `toimiala` — Työnantajan toimiala

**Group:** Tyotarjoukset, Palkkatukipaikat

työnantajan toimiala eli ei työpaikan toimiala: toimialaluokitus. Katso Tilastokeskus henkilöluokitukset

#### `toimikoodi` — Suunnitelmassa sovitetut tehtävä

**Group:** Suunnitelmat

000 = Määrittelemätön; 
001 = Hankin tietoa, jota tarvitsen; 
002 = Haen työpaikkoja; 
003 = Työnhakukeskuksen palvelut; 
004 = Julkaisen CV:ni CV-netissä; 
005 = Otan käyttöön Paikkavahdin; 
006 = Henkilökohtainen työnvälitys (esittelyt, tarjoukset); 
007 = Osallistun työnhakuvalmennukseen; 
008 = Osallistun uudelleensijoittumisvalmennukseen; 
009 = Selvitän, miten voin hakea töitä Euroopasta (Eures); 
010 = Selvitän, mitkä ovat valmiuteni ryhtyä yrittäjäksi; 
011 = Selvitän verkkopalveluiden avulla ammatillisia vaihtoehtojani; 
012 = Henkilökohtainen urasuunnittelu; 
013 = Kartoitan osaamistani ja ammattitaitoani ohjatusti; 
014 = Henkilökohtainen koulutusneuvonta; 
015 = Henkilökohtainen kuntoutussuunnittelu; 
016 = Osallistun työkykyni selvittämiseen; 
017 = Tapaan työhönvalmentajan sovitusti; 
018 = Osallistun työkokeiluun työpaikalla; 
019 = Työelämävalmennus; 
020 = Työharjoittelu; 
021 = Haen opiskelemaan työttömyysetuudella tuetusti; 
022 = Haen työvoimakoulutuksena järjestettävään koulutukseen; 
023 = Valmentava työvoimakoulutus; 
024 = Haen oppisopimuskoulutukseen; 
025 = Kotoutujan rinnasteinen koulutus; 
026 = Palkkatuettu työ; 
027 = Asioin sovitusti työvoiman palvelukeskuksessa; 
028 = Työvoimapalveluja täydentävät palvelut; 
029 = Osallistun kuntouttavaan työtoimintaan; 
030 = Tarvitsen muita viranomaispalveluja; 
031 = Selvitän mahdollisuuksiani saada eläkettä; 
032 = Tarvitsen muita palveluja; 
033 = Ei soveltuvia palveluja tarjolla; 
034 = Menen terveystarkastukseen; 
035 = Osallistun maahanmuuttajien alkukartoitukseen; 
036 = Haen opiskelemaan työttömyysetuudella tuettuun kotoutumiskoulutukseen; 
037 = Haen kotoutumiskoulutukseen, jota järjestetään työvoimakoulutuksena; 
038 = Haen työvoimakoulutuksena järjestettävään perusopetukseen; 
039 = Selvitän mahdollisen yritykseni toimintaa ja kannattavuutta; 
040 = Haen starttirahaa; 
041 = Keskustelen ammatillisista mahdollisuuksistani asiantuntijan kanssa; 
042 = Osallistun uravalmennukseen; 
043 = Osallistun koulutuskokeiluun oppilaitoksessa; 
044 = Tarvitsen muun asiantuntijan arviointiapua tilanteestani; 
045 = Ilmoitan, että opintoni ovat edenneet suunnitellusti;
046 = Luen verkkosivulta työnhakijan oikeuksista ja velvollisuuksista;
047 = Julkaisen CV:n CV-netissä tai muissa osaamisprofiileissa ja pidän sen voimassa;
048 = Tilaan itselleni Avoimet työpaikat -hakupalvelun Työpaikkavahdin ja pidän tilaukseni voimassa;
049 = Haen aktiivisesti työpaikkoja eri työnhakukanavia apuna käyttäen sekä osallistun TE-palvelujen järjestämiin soveltuviin rekrytointitilaisuuksiin;
050 = Julkaisen CV:ni Eures-verkkosivuilla ja haen aktiivisesti työpaikkoja Euroopasta eri työnhakukanavia käyttäen;
051 = Hakeudun työnhakuvalmennukseen työnhakutaitojeni parantamiseksi;
052 = Tutustun verkossa yrityksen perustamiseen tai osallistun tilaisuuteen, jossa aihetta käsitellään;
053 = Laadin toteuttamiskelpoisen liiketoimintasuunnitelman päätoimista yrittäjyyttä varten;
054 = Selvitän yritystoiminnan rahoittamisen mahdollisuudet ja haen tarvittaessa starttirahaa turvatakseni toimeentuloni;
055 = Arvioin työllistymiseni edellytyksiä verkkotyökalun avulla;
056 = Selvitän ammatillisia vaihtoehtojani ammatinvalinnan verkkotyökalun tai verkkosivuston avulla;
057 = Hankin tietoa koulutusmahdollisuuksista Suomesta tai muualta Euroopasta;
058 = Hakeudun osaamiseni ja ammattitaitoni kartoitukseen;
059 = Arvioin ja selvitän ammatillisia mahdollisuuksiani sekä soveltuvaa koulutus- tai työuraa asiantuntijan kanssa;
060 = Suunnittelen soveltuvaa koulutus- ja työuraa ammatinvalinta- ja uraohjauksen psykologin kanssa;
061 = Hakeudun uravalmennukseen;
062 = Hakeudun  koulutuskokeiluun oppilaitoksessa;
063 = Hakeudun työkokeiluun työpaikalla;
064 = Haen työvoimakoulutukseen ja tilaan tarvittaessa sähköpostiini Koulutusvahdilla viestejä alkavista koulutuksista;
065 = Hakeudun oppisopimuskoulutukseen;
066 = Haen omaehtoisiin opintoihin;
067 = Ilmoitan, että työttömyysetuudella tuetut opintoni ovat edenneet suunnitellusti;
068 = Osallistun työtoiveiden suunnitteluun sekä koulutukseen tai uuteen ammattiin liittyvään työkykyni selvittämiseen;
069 = Tarvitsen TE-toimiston palvelujen lisäksi esim. terveydentilan, kuntoutuksen tai eläkemahdollisuuksien selvittämistä;
070 = Tapaan työhönvalmentajani sovitusti saadakseni tukea työllistymiseeni;
071 = Asioin sovitusti työllistymistäni edistävässä monialaisessa yhteispalvelussa;
072 = Hakeudun  kuntouttavaan työtoimintaan;
073 = Hakeudun työnantajan irtisanomistilanteissa järjestämään uudelleensijoittumisvalmennukseen;
074 = Monialaisen yhteispalvelun asiakas;
075 = Julkaisen CV:n osaamisprofiileissa ja pidän sen voimassa työnhakijana oloajan;
076 = Muu kotoutumistani edistävä toiminta;
077 = Haen aktiivisesti palkkatuettuja työpaikkoja;
078 = Osallistun työllistymistäni tukevaan palveluun;
079 = Työnhakuvelvollisuus;
080 = Selvitän mahdollisuuksiani yrittäjyyteen esim. yrityksen perustaminen, liiketoimintasuunnitelman laatiminen, yritystoiminnan rahoitus jne.;
081 = Osallistun osaamiseni ja ammattitaitoni kartoitukseen;
082 = Osallistun koulutuskokeiluun oppilaitoksessa ammatinvalinta- ja uravaihtoehtojen selvittämiseksi;
083 = Haen koulutukseen parantaakseni ammattitaitoani, mahdollisuuttani saada työtä tai säilyttääkseni työpaikkani;
084 = Osallistun TE-toimiston palvelujen lisäksi esim. terveydentilan tai kuntoutuksen selvittämiseen;
085 = Selvitän eläkemahdollisuuksiani;
086 = Osallistun kuntouttavaan työtoimintaan elämänhallintani ja työllistymiseni parantamiseksi;
087 = Osallistun työnantajan irtisanomistilanteissa järjestämään uudelleensijoittumisvalmennukseen;
088 = Muu henkilökohtainen työnhakua tai työllistymistä edistävä palvelu;
089 = Muu täydentävä työnhakua tai työllistymisen yleisiä edellytyksiä parantava palvelu;
090 = Osallistun minulle hankittavaan muutosturvakoulutukseen;

#### `toimipvm` — Päivämäärä, mihin mennässä tehtävä on suoritettava

**Group:** Suunnitelmat

#### `toimkasitelty` — Onko tehtävä toteutunut vai ei

**Group:** Suunnitelmat

#### `toimsuunlaji` — Suunnitelman laji

**Group:** Suunnitelmat

01 = Työllistymissuunnitelma
02 = Työllistymisohjelma  
03 = Aktivointisuunnitelma  
04 = Kotoutumissuunnitelma  
05 = Yksilöity työnhakusuunnitelma  
06 = Uudistettu, yksilöity työnhakusuunnitelma
07 = Monialainen työllistymissuunnitelma

#### `toimviimpvm` — Tarkistuspäivämäärä

**Group:** Suunnitelmat

#### `tuloskoodi` — Työtarjouksen tulos

**Group:** Tyotarjoukset, Palkkatukipaikat

01 = Työnvälitys  
02 = Paikka täytetty  
03 = Paikka peruutettu
04 = TA ei hyväksy hakijaa  
05 = HA ei hyväksy tarj.  
06 = HA ei ottanut yht. TA:aan  
07 = eKirje peruttu  
08 = sopimusta ei syntynyt  
09 = Muu/ei tietoa  
10 = HA ei tavoittanut TA:aa
11 = Muu syy  
12 = Ei tietoa
13 = Tarjous peruttu  
51 = Valinta kesken
52 = Valittu, alkamispvm ei tiedossa

#### `tyoaikakoodi` — Työn työaika

**Group:** Tyotarjoukset

01 = kokoaikatyö
03 = 2-vuorotyö
04 = 3-vuorotyö  
05 = 4-5 -vuorotyö  
06 = yötyö  
07 = osapäivätyö  
08 = muu osa-aikatyö
09 = iltatyö
10 = viikonlopputyö

#### `tyok_apvm` — Työllisyyskoodin alkamispvm

**Group:** Tyotarjoukset, Palkkatukipaikat

ko. työllisyyskoodin alkamispäivä

#### `tyok_lpvm` — Työllisyyskoodin loppumispvm

**Group:** Palkkatukipaikat, Tyotarjoukset

ko. työllisyyskoodin loppumispäivä

#### `tyollkoodi` — Työllisyyskoodi

**Group:** Palkkatukipaikat, Tyotarjoukset

Hakijan työllisyyskoodi sillä hetkellä kun työtarjous tehty: 
00 = työssä oleva, työllistetty
01 = työssä oleva, yleisillä työmarkkinoilla
02 = työtön
03 = lomautettu
04 = lyhennetyllä työviikolla  
05 = työvoiman ulkopuolella oleva  
06 = Koodi ei käytössä (ent. työttömyyseläke)  
07 = työllistymistä edistävässä palvelussa
08 = koulutuksessa
09 = osa-aikatyössä oleva

#### `tyonkestokoodi` — Työn kesto

**Group:** Tyotarjoukset

Tarjotun työn kesto: 
01 = alle 11 pv  
02 = 11 pv - 1 kk  
03 = 1 - 3 kk  
04 = 3 - 6 kk  
05 = 6 - 12 kk  
06 = yli 12 kuukautta

#### `tyosuhttyyppi` — Työsuhteen tyyppi

**Group:** Tyotarjoukset

Työsuhteen tyyppi eli ei työpaikan tyyppi  
01 = palkkatyö
02 = provisio  
03 = yrittäjä  
04 = vuorottelu

#### `yhtottopvm` — Yhteydenottopäivämäärä

**Group:** Yhteydenottotavat, Sanssikortti

Poiminta tehty tämän mukaan yhteydenottotavat-tiedostossa

#### `yhtottotapa` — Yhteydenottotapa (uuden koodit käytössä 5.12.2010 alkaen)

**Group:** Yhteydenottotavat

01 = Soitto asiakkaalle
02 = Soittoyritys asiakkaalle  
03 = Kirje asiakkaalle  
04 = Tekstiviesti asiakkaalle  
05 = Sähköposti asiakkaalle
20 = Videoneuvottelu
21 = Alkuhaastattelu käynti
22 = Alkuhaastattelu videoneuvottelu
23 = Alkuhaastattelu puhelinsoitto
24 = Täydentävä työnhakukeskustelu käynti
25 = Täydentävä työnhakukeskustelu videoneuvottelu
26 = Täydentävä työnhakukeskustelu puhelinsoitto
27 = Työnhakukeskustelu käynti
28 = Työnhakukeskustelu videoneuvottelu
29 = Työnhakukeskustelu puhelinsoitto
30 = Täydentävä työnhakukeskustelu palveluntuottajalla
31 = Asiakkaan soitto
32 = Asiakkaan kirje
33 = Asiakkaan tekstiviesti
34 = Asiakkaan sähköposti
35 = Asiakkaan käynti aikavarauksella  
36 = Asiakkaan käynti ilman aikavarausta 
70 = Haastattelukäynti
71 = Haastattelu videoneuvotteluna
72 = Haastattelu puhelimitse
80 = Haastattelukäynti palveluntuottajalla
81 = Haastattelu palveluntuottajalla videoneuvotteluna
82 = Haastattelu palveluntuottajalla puhelimitse
95 = Muu yhteydenotto  
96 = Muu tallennus toimistossa  
97 = Asiointi verkossa
98 = Ei tiedossa  
99 = Muu tallennus

---

[← Back to catalogue](../../README.md)
