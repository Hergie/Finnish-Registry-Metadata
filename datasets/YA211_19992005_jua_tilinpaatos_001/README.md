# FIRM_FSS Tilinpäätösaineisto 1999-2005 (YA211)

- **Identifier:** `YA211_19992005_jua_tilinpaatos_001.xml`
- **DOI:** `work_2016-11_2016-11-22_ain_0001`
- **Temporal coverage:** 1999-01-01 - 2005-12-31
- **Published:** 2017-08-10
- **Organisation:** Tilastokeskus
- **Variable count:** 96
- **Observation count:** —
- **Population:** Tilastoyksikkönä on yritys. Aineisto ei sisällä konserneja eikä yritysten toimipaikkoja. Valtion ja kuntien liikelaitokset sisältyvät aineistoon. Kuvausalueen ulkopuolelle jäävät julkisen sektorin viranomaisyksiköt, voittoa tavoittelemattomat yhteisöt, rahoitus ja vakuutustoiminta sekä ne maatilatalouden yksiköt, jotka eivät toimi työnantajina. Yksilöivänä tunnuksena on yrityksen liike- ja yhteisötunnus eli y-tunnus (suojattu).
- **Source:** Tilinpäätöstilaston aineisto perustuu verohallinnon elinkeinoverotusaineistoon ja Tilastokeskuksen yritystiedusteluun. 
Elinkeinoverotusaineisto sisältää kaikkien elinkeinoverotuslain alaisten yritysten ja ammatinharjoittajien tilinpäätöstiedot. 
Yritysten luokitustiedot kerätään pääsääntöisesti Tilastokeskuksen yritys- ja toimipaikkarekisteristä.

## Kuvaus / Description

Tilinpäätöstilasto kuvaa yritystoiminnan tuloksen muodostumista, kannattavuutta sekä taseen rakennetta. Tilastoyksikkönä on yritys. Valtion ja kuntien liikelaitokset sisältyvät aineistoon. Kuvausalueen ulkopuolelle jäävät julkisen sektorin viranomaisyksiköt, voittoa tavoittelemattomat yhteisöt, rahoitus ja vakuutustoiminta sekä ne maatilatalouden yksiköt, jotka eivät toimi työnantajina. Yksilöivänä tunnuksena on yrityksen liike- ja yhteisötunnus eli y-tunnus.

Tilasto sisältää tuloslaskelma- ja tasetiedot pääkohdittain. Lisäksi tilasto sisältää yritysten perus- ja luokittelutietoja, jotka saadaan Tilastokeskuksen yritysrekisteristä. Tilaston tiedot muodostavat yhtenäisen aikasarjan 1999-2005 (til9905). Aineisto sisältää myös liikevaihdon ja kulujen erittelytietoja.  Kulut esitetään negatiivisina erinä.

Vuodesta 1994 alkaen Tilastokeskuksen käytettävissä on ollut Elinkeinoverotusaineisto, joka sisältää kaikkien elinkeinoverotuslain alaisten yritysten ja ammatinharjoittajien tilinpäätöstiedot. Tilastokeskuksen omassa tiedustelussa kerätään investointitietoja ja muita tilinpäätöksen lisätietoja, kuten liikevaihdon ja kulujen erittelytietoja. Vuodesta 1995 (teollisuudessa ja rakentamisessa) ja vuodesta 1996 (muilla toimialoilla) suorassa tiedustelussa olivat mukana kaikki vähintään 20 hengen yritykset. Lisäksi tiedustelun piiriin kuului 10-20 henkilöä työllistäviä yrityksiä, jotka ylittävät vuosittain ja toimialoittain muuttuvat liikevaihtorajat. 

Elinkeinoverotusaineisto on tärkeä tilaston tietolähde. Aineiston laatu tarkistetaan ja korjataan ohjelmallisesti. Aineiston puuttuvat arvot korvataan eli imputoidaan ensisijaisesti yrityksen aikaisempien vuosien tiedoilla ja toiseksi liikevaihdoltaan ja henkilöstömäärältään vastaavanlaisen yrityksen tiedoilla.Tilinpäätöskyselyyn kuulumattomille yrityksille tuotetaan liikevaihdon ja kulujen erittelyjen tiedot imputointimallin mukaisesti. Malli perustuu kyselyyn kuuluvien yritysten tietoihin. Imputointimallissa lasketaan toimialakohtaiset kertoimet. Kertoimia laskettaessa on huomioitu poikkeavat havainnot.

Tilinpäätöstilastot sisältävät tiettyjä toimialoja, joiden käytön suhteen kannattaa noudattaa erityistä varovaisuutta. Näitä toimialoja ei tarkisteta Tilastokeskuksen toimesta ja tieto on huonolaatuista: alkutuotanto (TOL02;01-05), rahoitustoiminta (TOL02; 65-672), julkinen hallinto ja maanpuolustus (TOL02; 75), julkiset koulutusyksiköt (TOL02; 80), järjestötoiminta (TOL02; 91) sekä kansainväliset järjestöt ja ulkomaiset edustustot (TOL02; 98). Näiden toimialojen rajaamista pois aineistosta kannattaa harkita. Tuntemattomat (TOL02; 99) ja tyhjät toimialat kannattaa rajata pois aineistosta, sillä niille ei ole löydetty toimialoja yritysrekisteristä. Myös hallintayhtiöihin (TOL02; 74150) kannattaa suhtautua varauksella näiden erityisen luonteen johdosta.

Luvut ovat euroina.

## Muuttujat / Variables (96)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `VUOSI` | Tilastovuosi | — | — | — |
| `TOL02YR` | Toimiala | — | — | — |
| `TOL02REK` | Toimiala (yrek) | — | — | — |
| `KPM` | Kirjanpitomuoto | — | — | — |
| `OIK` | Oikeudellinen muoto | — | oikeudell_muoto_1_1984_01_01 | — |
| `YRPKSL` | Yrityksen PK-suuruusluokka | — | — | — |
| `TU` | Tuloslaskelma umpeen | — | 28.2.2013 | — |
| `TU2` | Tuloslaskelman korjausmenetelmä | — | — | — |
| `TA` | Tase umpeen | — | — | — |
| `TA2` | Taseen korjausmenetelmä | — | — | — |
| `IMPU` | Tiedot suorasta kyselystä=0 | — | — | — |
| `LVAIHTO` | Liikevaihto | — | — | — |
| `LIIKMUUT` | Liiketoiminnan muut tuotot (oikaistu) | — | — | — |
| `TUOTYH` | LIIKETOIMINNAN TUOTOT YHTEENSÄ | — | — | — |
| `AINETARV` | Aine- ja tarvikekäyttö | — | — | — |
| `ULKOPALV` | Ulkopuoliset palvelut | — | — | — |
| `HEKULYHT` | Palkat ja henkilösivukulut yhteensä | — | — | — |
| `PALKKORJ` | Laskennallinen palkkakorjaus | — | — | — |
| `MUKULUT` | Liiketoiminnan muut kulut | — | — | — |
| `MUKULYH` | Liiketoiminnan muut kulut (oikaistu) | — | — | — |
| `VAVAROKA` | Valmistevarastojen lisäys/vähennys | — | — | — |
| `KAYTKATE` | KÄYTTÖKATE (oikaistu) | — | — | — |
| `POISTOT` | Suunnitelman mukaiset poistot | — | — | — |
| `KOMARVAL` | Arvonalentumiset pysyvien vastaavien hyödykkeistä | — | — | — |
| `VOMARVAL` | Vaihtuvien vastaavien poikkeukselliset arvonalentumiset | — | — | — |
| `POIARALY` | Poistot ja arvonalentumiset yhteensä | — | — | — |
| `LIVOILMY` | LIIKETULOS | — | — | — |
| `RAHTUOT` | Rahoitustuotot | — | — | — |
| `RAHKUL` | Rahoituskulut | — | — | — |
| `VALVERTU` | Tuloverot | — | — | — |
| `VALVERMU` | Muut välittömät verot | — | — | — |
| `NETTOT` | NETTOTULOS | — | — | — |
| `SATTUOT` | Satunnaiset tuotot | — | — | — |
| `SATKULUT` | Satunnaiset kulut | — | — | — |
| `LVKOMYVO` | Käyttöomaisuuden myyntivoitot | — | — | — |
| `KOMYTAPP` | Käyttöomaisuuden myyntitappiot | — | — | — |
| `FUVOITTO` | Fuusiovoitto | — | — | — |
| `FUTAPPIO` | Fuusiotappio | — | — | — |
| `KOKOT` | KOKONAISTULOS | — | — | — |
| `POISEROM` | Poistoeron lisäys/vähennys | — | — | — |
| `VAPEHTVA` | Vapaaehtoisten varausten lisäys/vähennys | — | — | — |
| `PALKKORP` | Laskennallinen palkkakorjaus (palautus) | — | — | — |
| `TILIKTUL` | TILIKAUDEN TULOS | — | — | — |
| `RAHTUL` | Rahoitustulos | — | — | — |
| `TULORAH` | Tulorahoitus | — | — | — |
| `MAKSKONS` | Maksetut konserniavustukset | — | — | — |
| `SAAKONSA` | Saadut konserniavustukset | — | — | — |
| `DKOATONY` | Aineettomat hyödykkeet yhteensä | — | — | — |
| `DKOANENY` | Aineelliset hyödykkeet yhteensä | — | — | — |
| `DKOARYHT` | Sijoitukset yhteensä | — | — | — |
| `DVOYHT` | Vaihto-omaisuus yhteensä | — | — | — |
| `DSAAYHTP` | Pitkäaikaiset saamiset yhteensä | — | — | — |
| `DSAAYHTL` | Lyhytaikaiset saamiset yhteensä | — | — | — |
| `DROARYHT` | Rahoitusarvopaperit yhteensä | — | — | — |
| `DRORAH` | Rahavarat | — | — | — |
| `DYHT` | Vastaavaa yhteensä | — | — | — |
| `KOPYHT` | Oma pääoma yhteensä | — | — | — |
| `KVARVEY` | Tilinpäätössiirtojen kertymä yhteensä | — | — | — |
| `KVARPAKO` | Pakolliset varaukset yhteensä | — | — | — |
| `KPVPYHT` | Pitkäaikainen vieras pääoma yhteensä | — | — | — |
| `KLVPYHT` | Lyhytaikainen vieras pääoma yhteensä | — | — | — |
| `VPOYHT` | Vieras pääoma yhteensä | — | — | — |
| `KYHT` | Vastattavaa yhteensä | — | — | — |
| `KPVPSAEN` | Ennakkomaksut, pitkäaikaiset | — | — | — |
| `KLVPSAEN` | Ennakkomaksut, lyhytaikaiset | — | — | — |
| `OIKTASE` | Oikaistu tase | — | — | — |
| `KPVPOSTO` | Vastattavaa: pitkäaikaiset ostovelat | — | — | — |
| `KLVPOSTO` | Vastattavaa: lyhytaikaiset ostovelat | — | — | — |
| `DSAAMYYP` | Pitkäaikaiset myyntisaamiset | — | — | — |
| `DSAAMYYL` | Lyhyaikaiset myyntisaamiset | — | — | — |
| `KKORVPO` | Korollinen vieras pääoma | — | — | — |
| `EHDOSING` | Tilikaudelta päätetty / ehdotettu osingonjako | — | — | — |
| `LISKONE` | Koneiden ja laitteiden lisäykset | — | — | — |
| `LISRAKEN` | Rakennusten ja rakennelmien lisäykset | — | — | — |
| `DKOKONE` | Koneet ja kalusto tilikauden lopussa | — | — | — |
| `DKORAKEN` | Rakennukset ja rakennelmat tilikauden lopussa | — | — | — |
| `LISANTYH` | Aineeton käyttöomaisuus: lisäykset | — | — | — |
| `VAHAINTY` | Aineeton käyttöomaisuus: vähennykset | — | — | — |
| `LISANLYH` | Aineellinen käyttöomaisuus: lisäykset | — | — | — |
| `VAHANLYH` | Aineellinen käyttöomaisuus: vähennykset | — | — | — |
| `LISOSAKE` | Osakkeet ja osuudet: lisäykset | — | — | — |
| `VAHOSAK` | Osakkeet ja osuudet: vähennykset | — | — | — |
| `HENKLKMYH` | Henkilöstön lukumäärä yhteensä | — | — | — |
| `HENKKESK` | Henkilöstön lkm kokoaikavastaavana | — | — | — |
| `SIJOP` | Sijoitettu pääoma | — | — | — |
| `JALEU` | Jalostusarvo | — | — | — |
| `SIJTULO` | Pääoman tuotto | — | — | — |
| `KORKULKO` | Korko- ja muut rahoituskulut konsernin yrityksille | — | — | — |
| `KORKULMU` | Korko- ja muut rahoituskulut muille | — | — | — |
| `NETTOVAR` | Nettovarallisuus | — | — | — |
| `QUICKOS` | Quick ratio osoittaja | — | — | — |
| `QUICKNIM` | Quick ratio nimittäjä | — | — | — |
| `VIENTIYH` | Vienti yhteensä | — | — | — |
| `OPOSINKO` | Edellisen tilikauden tuloksesta maksettu osinko | — | — | — |
| `VOLOENNA` | Vaihto-omaisuus tilikauden lopussa | — | — | — |
| `SYRTUN` | Suojattu yritystunnus | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `VUOSI` — Tilastovuosi

#### `TOL02YR` — Toimiala

Toimialaluokitus 2002 (rakennetilastosta) saatavissa täydellisenä 2008 asti.

#### `TOL02REK` — Toimiala (yrek)

Toimialaluokitus 2002 (yritysrekisteristä) saatavissa täydellisenä 2008 asti.

#### `KPM` — Kirjanpitomuoto

Yritysrekisterin mukainen kirjanpitomuoto. 1 yhdenkertainen kirjanpito, 2 kahdenkertainen kirjanpito

#### `OIK` — Oikeudellinen muoto

**Luokitus / Classification:** oikeudell_muoto_1_1984_01_01

Yrityksen oikeudellinen muoto, yritysrekisteristä.
11	Luonnollinen henkilö
12	Kuolinpesä, perikunta
13	Verotusyhtymä
14	Avoin yhtiö
15	Konkurssipesä
21	Kommandiittiyhtiö
22	Laivanisännistöyhtiö (ei osakeyhtiö)
31	Osakeyhtiö
32	Keskinäinen vakuutusyhtiö
33	Säästöpankki
34	Eläkesäätiö tai -kassa, työeläkelaitos, työttömyys- tai avustuskassa
35	Asunto-osakeyhtiö
41	Osuuskunta
51	Säätiö, rahasto
52	Aatteellinen yhdistys
53	Keskinäinen vahinkovakuutusyhdistys
54	Taloudellinen yhdistys
61	Julkinen viranomainen
62	Julkinen liikelaitos
63	Julkisoikeudellinen yhteisö
71	Valtionkirkko
72	Muu uskonnollinen yhteisö
90	Muu oikeudellinen muoto

#### `YRPKSL` — Yrityksen PK-suuruusluokka

Oikeudellisen yksikön PK-suuruusluokka EU-määritelmä (yritysrekisteristä). 0 = määrittelmätön, 1 = mikroyritys, alle 5 työntekijää,  2 = pienyritys, 5- 49 työntekijää,  3 = keskisuuriyritys, 50 - 249 työntekijää  4 = suuryritys.vähintään 250 työntekijää. Suuruusluokkien määrittelyssä käytetään lisäksi kriteereinä liikevaihtoa, taseen loppusummaa ja riippumattomuutta.  Luokituksessa käytetään EU:n komission suosittelemaa pienten ja keskisuurten yritysten määritelmää (96/280/EY), jonka mukaan tieto päätellään seuraavien ehtojen perusteella: henkilöstön suuruus, liikevaihdon suuruus, taseen loppusumma ja riippumattomuus suuryrityksistä.

Vuonna 2003 komissio muutti Pk-yritysten kokoluokkarajoja, joten vuodesta 2003 lähtien kokoluokat on määritetty uusin kriteerein.  Vuodet 1999-2002 ja 2003–  eivät ole tältä osin aivan vertailukelpoisia.

#### `TU` — Tuloslaskelma umpeen

**Luokitus / Classification:** 28.2.2013

Laatumuuttuja 1999-2005: tuloslaskelma umpeen = 1, muut arvot kuvaavat erilaisia ongelmia tuloslaskelmassa.

#### `TU2` — Tuloslaskelman korjausmenetelmä

Tuloslaskelman korjausmenetelmä 1999-2005: 4 = lähimmän naapurin menetelmä, 2 = tiedot on korjattu
skaalaamalla, jolloin suhteellinen virhe on ollut pieni.

#### `TA` — Tase umpeen

Laatumuuttuja 1999-2005: tase umpeen = 1, muut arvot kuvaavat erilaisia ongelmia taseessa.

#### `TA2` — Taseen korjausmenetelmä

Taseen korjausmenetelmä 1999-2005: 4 = lähimmän naapurin menetelmä, 2 = tiedot on korjattu
skaalaamalla, jolloin suhteellinen virhe on ollut pieni.

#### `IMPU` — Tiedot suorasta kyselystä=0

Laatumuuttuja 1999-: Yrityksen vastaustietojen lähde. Yritys kuuluu Tilastokeskuksen omaan suoraan kyselyyn, IMPU=0, tiedot tarkistettu manuaalisesti. IMPU=blankko, tietoja ei tarkistettu käsin.

#### `LVAIHTO` — Liikevaihto

Kirjanpidon mukainen liikevaihto. Liikevaihto koostuu yrityksen varsinaisen toiminnan myyntituloista, joista on vähennetty myönnetyt alennukset sekä arvonlisävero ja muut välittömästi myynnin määrään perustuvat verot (KPL 4:1 §). Tietoja vuoteen 2012 saakka.

#### `LIIKMUUT` — Liiketoiminnan muut tuotot (oikaistu)

Liiketoiminnan muita tuottoja ovat  yrityksen varsinaiseen toimintaan liittyvät tuotot, jotka ovat luonteeltaan lähellä liikevaihtoa. Tällaisia tuottoja ovat esimerkiksi vuokratuotot, saadut provisiot, muilta yrityksiltä perityt hallinto-, tietojenkäsittely- yms. korvaukset, mikäli yrityksen varsinaisena toimialana ei ole vuokraustoiminta tai muiden edellä mainittujen palvelujen tuottaminen. Liiketoiminnan muihin tuottoihin kirjataan myös yrityksen varsinaiseen toimintaan saadut avustustukset ja tuet. Tuottoja on oikaistu siirtämällä käyttöomaisuuden myyntivoitot ja fuusiovoitot satunnaisten eriin.

#### `TUOTYH` — LIIKETOIMINNAN TUOTOT YHTEENSÄ

Liikevaihdon ja liiketoiminnan muiden tuottojen yhteissumma.

#### `AINETARV` — Aine- ja tarvikekäyttö

Aine- ja tarvikekäyttö lasketaan vähentämällä virallisen tuloskelman aine- ja tavaraostoista näiden varastojen lisäys tai vastaavasti lisäämällä ostoihin kyseisten varastojen vähennys.

#### `ULKOPALV` — Ulkopuoliset palvelut

Ulkopuoliset palvelut ovat välittömästi tuotantoon tai myyntiin liittyvistä työsuorituksista maksettuja korvauksia.  Ulkopuolisia palveluja voivat olla esimerkiksi alihankkijoiden, suunnittelu- ja konsulttitoimistojen sekä huoltoyhtiöiden suorittamat palvelut ja sellaisen työvoiman vuokrauskulut, jotka liittyvät välittömästi suoritetuotantoon.

#### `HEKULYHT` — Palkat ja henkilösivukulut yhteensä

Henkilöstökulut sisältävät ennakonpidätyksen alaiset palkat ja niihin verrattavat kulut sekä välittömästi palkan perusteella määräytyvät kulut, kuten sosiaaliturvamaksut, pakolliset ja vapaaehtoiset henkilövakuutusmaksut sekä eläkekulut.

#### `PALKKORJ` — Laskennallinen palkkakorjaus

Laskennallinen palkkakorjaus = yrittäjätyöpanos * keskipalkka. Palkkakorjaus esitetään omana eränä ja liitetään henkilöstökuluihin. Palkkakorjaus palautetaan oikaistuun tuloslaskelmaan ennen tilikauden tulosta.

Palkkakorjaus on laskennallinen erä, jolla ei ole vaikutusta yrityksen vakavaraisuuteen eikä kassavirtaan. Palkkakorjaus on tehty vastaamaan yrittäjien itsensä tekemän palkattoman työpanoksen arvoa yrityksessä.Tämän palkan yrittäjä joutuisi maksamaan palkansaajalle, jos hän palkkaisi palkansaajan tekemään omat työt. 

Lähtötietoina käytetään yrityksen yrittäjätyöpanosta ja yrityskohtaista palkatun henkilöstön keskipalkkaa. Arvo perustuu YTR:stä saatavien yrittäjien lukumääriin, ja yrittäjien palkka on arvioitu toimialakohtaisten keskipalkkojen mukaan.

Yhtiömuodosta riippuen omistajan palkkaa käsitellään verotuksessa eri tavoin. Yksityisen elinkeinonharjoittajan palkka ei koskaan sisälly tuloslaskelmaan ja henkilöyhtiöissä omistajan palkka voi vain poikkeustapauksissa olla kuluna. Tämä epäyhtenäinen käytäntö vaikeuttaa erityisesti pienten yritysten keskinäistä vertailua. Palkkakorjaus  tehdään  mikroyrityksille eli alle 10 henkilöä työllistäville. 

Vuodesta 1999-

#### `MUKULUT` — Liiketoiminnan muut kulut

Liiketoiminnan muita kuluja ovat kaikki tuotantoon liittyvät tavanomaiset ja säännöllisesti syntyvät kulut. Ne ovat yrityksen varsinaiseen toimintaan kuuluvia eriä, joita ei ole tuloslaskelmassa erikseen mainittu mm. vuokrat, energia, puhtaanapito, leasingmaksut, mainos- ja markkinointikulut, hallintopalvelujen kulut, tietoliikenne- ja pankkipalvelumaksut sekä käyttöomaisuuden myyntitappiot. Liiketoiminnan muita kuluja ovat myös myyntiprovisiot, tekijäpalkkiot, rahtikulut ja syntyneet luottotappiot.

#### `MUKULYH` — Liiketoiminnan muut kulut (oikaistu)

Liiketoiminnan muut kulut oikaistuna = käyttöomaisuuden myyntitappiot ja fuusiotappiot esitetään satunnaisten erien ryhmässä.
Liiketoiminnan muita kuluja ovat kaikki ne yrityksen varsinaiseen toimintaan kuuluvat erät, joita ei ole tuloslaskelmassa erikseen mainittu mm. vuokrat, leasingmaksut, mainos- ja markkinointikulut, hallintopalvelujen kulut, tietoliikenne- ja pankkipalvelumaksut sekä käyttöomaisuuden myyntitappiot. Tähän erään kuuluvat myös maksetut myyntiprovisiot, tekijäpalkkiot, rahtikulut ja syntyneet luottotappiot.

#### `VAVAROKA` — Valmistevarastojen lisäys/vähennys

Valmiiden ja keskeneräisten tuotteiden varaston muutos (lisäys + vähennys -). Valmiiden ja keskeneräisten tuotteiden varastojen muutos koostuu vaihto-omaisuuden keskeneräisten tuotteiden ja valmiiden tuotteiden tai tavaroiden yhteisestä varaston muutoksesta. Vaihto-omaisuudessa olevien ennakkomaksujen muutos ei sisälly tuloslaskelman varaston muutokseen. Erä sisältää myös valmistuksen omaan käyttöön.

#### `KAYTKATE` — KÄYTTÖKATE (oikaistu)

Käyttökate kertoo yrityksen liiketoiminnan tuloksen ennen poistoja ja rahoituseriä. Käyttökatetta ei esitetä virallisen tuloslaskelman välituloksena. Käyttökate on laskettu oikaistusta tuloslaskelmasta.

#### `POISTOT` — Suunnitelman mukaiset poistot

Virallisen tuloslaskelman suunnitelman mukaiset poistot. Suunnitelman mukaiset poistot perustuvat käyttöomaisuuden hankintamenoon ja omaisuuden taloudelliseen käyttöikään. Poistot tehdään investointiavustuksella vähennetystä hankintamenosta. Investointiin käytettyä varausta ei vähennetä hankintahinnasta, vaan varauksen käyttö käsitellään poistoeron lisäyksenä.

#### `KOMARVAL` — Arvonalentumiset pysyvien vastaavien hyödykkeistä

Todennäköisen luovutushinnan alentumisen perusteella tehtävä kertaluontoinen arvonalennuspoisto. Vaihto-omaisuusvaraston poikkeukselliset arvonalennukset, esim. tulipalosta tai vesivahingosta johtuva arvonlasku.

#### `VOMARVAL` — Vaihtuvien vastaavien poikkeukselliset arvonalentumiset

Vaihtuvien vastaavien poikkeukselliset arvonalentumiset. Vaihto-omaisuusvaraston poikkeukselliset arvonalennukset, esimerkiksi tulipalosta tai vesivahingosta johtuva arvonlasku.  Erässä ei esitetä tavanomaisesta pilaantumisesta johtuvaa arvonalennusta vaan se sisällytetään tuloslaskelman varaston muutoksiin.

#### `POIARALY` — Poistot ja arvonalentumiset yhteensä

Tuloslaskelmassa esitetään poistosuunnitelman mukaiset tilikauden poistot. Suunnitelman mukaiset poistot perustuvat pysyvien vastaavien hankintamenoon ja näiden taloudelliseen käyttöikään. Arvonalentumiset perustuvat todennäköisen luovutushinnan pysyvään alenemiseen.

#### `LIVOILMY` — LIIKETULOS

Liiketulos eli liikevoitto/-tappio (EBIT=earnings before interest and taxes) kertoo, kuinka paljon varsinaisen liiketoiminnan tuotoista on jäljellä ennen rahoituseriä ja veroja.

#### `RAHTUOT` — Rahoitustuotot

Rahoitustuottoja ovat tuotot osuuksista ja muista pysyvien vastaavien sijoituksista sekä muut korko- ja rahoitustuotot, esimerkiksi kurssivoitot.

#### `RAHKUL` — Rahoituskulut

Rahoituskuluja ovat arvonalentumiset pysyvien vastaavien sijoituksista ja vaihtuvien vastaavien rahoitusarvopapereista sekä muut korko- ja rahoituskulut, esim. lainojen hoitokulut, limiittipalkkiot, takausprovisiot, luottovakuutukset, kiinnityskulut, perimiskulut, kurssitappiot, factoring-kulut ja terminointikulut.

#### `VALVERTU` — Tuloverot

Tilikauden tuloksesta aiheutuneet verot. Tuloverot sisältävät joko yrityksen kaikki tuloverot tai muihin kuin satunnaisiin eriin kohdistuvat tuloverot.

#### `VALVERMU` — Muut välittömät verot

Muut välittömät verot. Erä esiintyy varallisuusveroa maksavien kirjanpitovelvollisten tilinpäätöksessä.  Kiinteistöverot esitetään liiketoiminnan muissa kuluissa.

#### `NETTOT` — NETTOTULOS

Nettotulos saadaan, kun liiketulokseen lisätään tuloslaskelman rahoitustuotot ja vähennetään rahoituskulut ja verot.

#### `SATTUOT` — Satunnaiset tuotot

Satunnaiset tuotot syntyvät muusta kuin yrityksen varsinaisesta toiminnasta ja ovat luonteeltaan kertaluonteisia ja suuruudeltaan olennaisia. Pysyvistä vastaavista syntyneet myyntivoitot ja -tappiot ovat normaalisti liiketoiminnan muita tuottoja ja kuluja. Kokonaisesta toimialasta luopumisen yhteydessä syntynyttä myyntivoittoa tai -tappiota pidetään kuitenkin satunnaisena eränä.  Konserniavustuslain mukaiset saadut konserniavustukset esitetään myös satunnaisissa tuotoissa.

#### `SATKULUT` — Satunnaiset kulut

Satunnaiset kulut syntyvät muusta kuin yrityksen varsinaisesta toiminnasta ja ovat luonteeltaan kertaluonteisia ja suuruudeltaan olennaisia. Pysyvistä vastaavista syntyneet myyntivoitot ja -tappiot ovat normaalisti liiketoiminnan muita tuottoja ja kuluja. Kokonaisesta toimialasta luopumisen yhteydessä syntynyttä myyntivoittoa tai -tappiota pidetään kuitenkin satunnaisena eränä.  Konserniavustuslain mukaiset maksetut konserniavustukset esitetään myös satunnaisissa kuluissa.

#### `LVKOMYVO` — Käyttöomaisuuden myyntivoitot

Tilinpäätöstilastoissa liiketoiminnan muihin tuottoihin sisältyvät käyttöomaisuuden myyntivoitot esitetään omana eränään satunnaisten erien ryhmässä nettotuloksen jälkeen.

#### `KOMYTAPP` — Käyttöomaisuuden myyntitappiot

Tilinpäätöstilastoissa liiketoiminnan muihin tuottoihin sisältyvät käyttöomaisuuden myyntitappiot esitetään omana eränään satunnaisten erien ryhmässä nettotuloksen jälkeen.Käyttöomaisuuden myyntitappiot, vain 2004-

#### `FUVOITTO` — Fuusiovoitto

Tilinpäätöstilastoissa liiketoiminnan muihin tuottoihin sisältyvät fuusiovoitot esitetään omana eränään satunnaisten erien ryhmässä nettotuloksen jälkeen. Fuusiovoitto, vain 2004-

#### `FUTAPPIO` — Fuusiotappio

Tilinpäätöstilastoissa liiketoiminnan muihin tuottoihin sisältyvät fuusiotappiot esitetään omana eränään satunnaisten erien ryhmässä nettotuloksen jälkeen.Fuusiotappio, vain 2004-

#### `KOKOT` — KOKONAISTULOS

Kokonaistulos saadaan, kun nettotulokseen lisätään satunnaiset tuotot sekä myynti- ja fuusiovoitot ja vähennetään satunnaiset kulut sekä myynti- ja fuusiotappiot.

#### `POISEROM` — Poistoeron lisäys/vähennys

Poistoeron muutos (lisäys -, vähennys +). Kirjanpidossa on vähennettävä vähintään yhtä suuret poistot kuin verotuksessa halutaan vähentää. Poistot -kohdassa poistot esitetään ainoastaan suunnitelmapoistot, jolloin ylittävä tai alittava poisto esitetään kohdassa poistoero. Suunnitelmapoistot oikaistuna poistoeron muutoksella ovat tilikauden kokonaispoistot.

#### `VAPEHTVA` — Vapaaehtoisten varausten lisäys/vähennys

Vapaaehtoisten varausten muutos (lisäys -, vähennys +). Vapaaehtoisia varauksia ovat investointi-, luottotappio-, toiminta-, varasto-,  asuintalo- ja muut sellaiset varaukset. Myös EVL:n siirtymävarauksen muutos kuuluu tähän ryhmään. Näiden varausten lisäys tai vähennys esitetään tässä kohdassa.

#### `PALKKORP` — Laskennallinen palkkakorjaus (palautus)

Palkkakorjaus on laskennallinen erä, jossa arvioidaan palkka yrittäjäpanokselle. Sillä ei ole vaikutusta yrityksen vakavaraisuuteen eikä kassavirtaan, ja erä palautetaan ennen tilikauden tulosta.Yhtiömuodosta riippuen omistajan palkkaa käsitellään verotuksessa eri tavoin. Yksityisen elinkeinonharjoittajan palkka ei koskaan sisälly tuloslaskelmaan ja henkilöyhtiöissä omistajan palkka voi vain poikkeustapauksissa olla kuluna. Tämä epäyhtenäinen käytäntö vaikeuttaa erityisesti pienten yritysten keskinäistä vertailua. Palkkakorjaus  tehdään mikroyrityksille eli alle 10 henkilöä työllistäville. Lähtötietoina käytetään yrityksen yrittäjätyöpanosta ja yrityskohtaista palkatun henkilöstön keskipalkkaa. Yrittäjätyöpanoksen määrittelee yritys- ja toimipaikkarekisteri YEL-maksutietojen perusteella, eli laskennallinen palkkakorjaus = yrittäjätyöpanos * keskipalkka.

#### `TILIKTUL` — TILIKAUDEN TULOS

Tilikauden tuloksessa on huomioitu kaikki yrityksen tuotot ja kulut tilikaudelta sekä etukäteen pakollisina varauksina kirjatut vastaiset menot ja menetykset.

#### `RAHTUL` — Rahoitustulos

Rahoitustulos saadaan lisäämällä nettotulokseen ennen liiketulosta vähennetyt suunnitelman mukaiset poistot ja arvonalentumiset. Rahoitustuloksen pitäisi riittää lainojen lyhennyksiin, investointien omarahoitusosuuksiin, käyttöpääoman lisäyksiin ja voitonjakoon.

#### `TULORAH` — Tulorahoitus

Tulorahoitus = NETTOT = LIVOILMY + RAHTUOTOT + RAHKULUT + VALVERTU + VALMERMU = liiketulos + rahoitustuotot + rahoituskulut + tuloverot + muut välittömät verot.
Nettotulos saadaan, kun liiketulokseen lisätään tuloslaskelman rahoitustuotot ja vähennetään rahoituskulut ja verot.

#### `MAKSKONS` — Maksetut konserniavustukset

Erä sisältää konserniavustuslain mukaan maksetut konserniavustukset. Konserniavustus sisältyy satunnaisiin eriin.

#### `SAAKONSA` — Saadut konserniavustukset

Erä sisältää konserniavustuslain mukaan saadut konserniavustukset. Konserniavustus sisältyy satunnaisiin eriin.

#### `DKOATONY` — Aineettomat hyödykkeet yhteensä

Aineettomat hyödykkeet yhteensä. Aineettomien hyödykkeiden ryhmään kuuluvat menot,  jotka eivät edusta konkreettista omaisuutta.

#### `DKOANENY` — Aineelliset hyödykkeet yhteensä

Aineelliset hyödykkeet yhteensä.  Erä saadaan, kun maa- ja vesialueet, rakennukset ja rakennelmat, koneet ja kalusto, muut aineelliset hyödykkeet sekä ennakkomaksut ja keskeneräiset hankinnat lasketaan yhteen.

#### `DKOARYHT` — Sijoitukset yhteensä

Sijoitukset  yhteensä. Sijoitukset eritellään seuraaviin ryhmiin: Ennakkomaksut ja keskeneräiset hankinnat, saamiset saman konsernin yrityksiltä, osuudet omistusyhteysyrityksissä, saamiset omistusyhteysyrityksiltä, muut osakkeet ja osuudet,  muut saamiset, omat osakkeet/osuudet ja muut sijoitukset.

#### `DVOYHT` — Vaihto-omaisuus yhteensä

Vaihto-omaisuudella tarkoitetaan sellaisinaan tai jalostettuina luovutettaviksi tai kulutettaviksi tarkoitettuja hyödykkeitä. Vaihto-omaisuus yhteensä  on aineiden ja tarvikkeiden, keskeneräisten tuotteiden, valmiiden tuotteiden, tavaroiden (kauppatavarat) sekä muun vaihto-omaisuuden (sis. ennakkomaksut) yhteissumma.

#### `DSAAYHTP` — Pitkäaikaiset saamiset yhteensä

Pitkäaikaiset saamiset yhteensä.  Erä on pitkäaikaisten myyntisaamisten, saman konsernin yrityksiltä saatujen saamisten, omistusyhteysyrityksiltä saatujen saamisten, lainasaamisten, muiden saamisten, maksamattomien osakkeiden tai osuuksien ja siirtosaamisten yhteissumma. Saaminen on pitkäaikainen jos, se erääntyy maksettavaksi yhtä vuotta pidemmän ajan kuluessa.

#### `DSAAYHTL` — Lyhytaikaiset saamiset yhteensä

Lyhytaikaiset saamiset yhteensä. Erä on lyhytaikaisten myyntisaamisten, saman konsernin yrityksiltä saatujen saamisten, omistusyhteysyrityksiltä saatujen saamisten, lainasaamisten, muiden saamisten, maksamattomien osakkeiden tai osuuksien ja siirtosaamisten yhteissumma. Saaminen on lyhytaikainen, jos  se erääntyy makseltavaksi yhtä vuotta lyhyemmän ajan kuluessa.

#### `DROARYHT` — Rahoitusarvopaperit yhteensä

Rahoitusarvopaperit  yhteensä. Erä muodostuu erien osuudet saman konsernin yrityksissä, omat osakkeet ja osuudet sekä muut arvopaperit yhteissummasta.

#### `DRORAH` — Rahavarat

Rahat. Erään sisältyy likvidit varat, varsinainen käteisraha kassassa ja mahdollisissa sivu- tai alakassoissa  olevat varat. On rahat ja pankkisaamiset –erä.

#### `DYHT` — Vastaavaa yhteensä

Taseen vastaavaa yhteensä on pysyvien vastaavien ja vaihtuvien vastaavien yhteissumma.

#### `KOPYHT` — Oma pääoma yhteensä

Erä sisältää kaikki oman pääoman erät yhteensä. Yhteisöillä omassa pääomassa esitetään osake-, osuus-, ja  muu vastaava pääoma, rahastot, edellisten tilikausien voitto/tappio ja tilikauden voitto/tappio. Muut yhtiömuodot ja säätiöt esittävät oman pääomansa erät soveltuvin osin kaavaa noudattaen ottaen huomioon omien erityislakiensa mukaiset oman pääoman muodot.

#### `KVARVEY` — Tilinpäätössiirtojen kertymä yhteensä

Tilinpäätössiirtojen kertymä  on poistoeron ja vapaaehtoisten varausten yhteissumma. Poistoero on  kirjanpidossa tehtyjen kokonaispoistojen ja  suunnitelman mukaisten  poistojen kumulatiivinen erotus. Negatiivista poistoeroa ei taseessa voi olla. Vapaaehtoiset varaukset ovat kirjanpitovelvollisen tekemiä jälleenhankinta-, toiminta-, hinnanlasku-, asuintalo- yms. varauksia.

#### `KVARPAKO` — Pakolliset varaukset yhteensä

Pakolliset varaukset yhteensä on erien eläkevaraukset, verovaraukset ja muut pakolliset varaukset yhteissumma. Pakolliset varaukset ovat  menoja, joiden suorittamiseen on sitouduttu ja ovat todennäköisiä vastaisia menetyksiä.

#### `KPVPYHT` — Pitkäaikainen vieras pääoma yhteensä

Pitkäaikainen vieras pääoma yhteensä. Erä muodostuu joukkokirjalainojen, vaihtovelkakirjalainojen, rahoituslaitoslainojen, eläkelainojen, saatujen ennakoiden, ostovelkojen, veloista saman konsernin yrityksille, veloista omistusyhteysyrityksille, muista veloista sekä siirtoveloista. Velka on pitkäaikainen, jos se  erääntyy maksettavaksi vähintään vuoden kuluessa.

#### `KLVPYHT` — Lyhytaikainen vieras pääoma yhteensä

Lyhytaikainen vieras pääoma yhteensä. Erä muodostuu joukkokirjalainojen, vaihtovelkakirjalainojen, rahoituslaitoslainojen, eläkelainojen, saatujen ennakoiden, ostovelkojen, rahoitusvekseleiden, veloista saman konsernin yrityksille, veloista omistusyhteysyrityksille, muista veloista sekä siirtoveloista. Velka on lyhytaikainen, jos se  erääntyy maksettavaksi tasan vuoden tai sitä lyhyemmän ajan kuluessa. 

Joukkovelkakirjalainat. Joukkovelkakirjat ovat liikkeelle laskettuja obligaatio-, debentuuri-, yritystodistus- ja sijoitustodistuslainoja sekä haltijalle asetettuja optiolainoja.

#### `VPOYHT` — Vieras pääoma yhteensä

Taseen pitkäaikainen ja lyhytaikainen vieraspääoma yhteensä.

#### `KYHT` — Vastattavaa yhteensä

Vastattavaa yhteensä on taseen neljän pääryhmän, oma pääoma, tilinpäätössiirtojen kertymä, pakolliset varaukset  ja vieras pääoma, summa.

#### `KPVPSAEN` — Ennakkomaksut, pitkäaikaiset

Saadut ennakot taseen pitkäaikaisista veloista. Erä sisältää saadut ennakkomaksut, jotka on ilmoitettu taseen vastattavaa -puolen pitkäaikaisen vieraan pääoman erässä.

#### `KLVPSAEN` — Ennakkomaksut, lyhytaikaiset

Saadut ennakot taseen lyhytaikaisista veloista. Erä sisältää saadut ennakkomaksut, jotka on ilmoitettu taseen vastattavaa -puolen lyhytaikaisen vieraan pääoman erässä.

#### `OIKTASE` — Oikaistu tase

Oikaistu tase = KYHT - KLVPSAEN - KPVPSAEN = Vastattavaa yhteensä - lyhytaikaiset ennakkomaksut - pitkäaikaiset ennakkomaksut

#### `KPVPOSTO` — Vastattavaa: pitkäaikaiset ostovelat

Ostovelat. Ostovelat ovat vaihto-, käyttö-, tai rahoitusomaisuuden hankkimiseen  liittyviä velkoja. Pitkäaikaisessa vieraassa pääomassa esitettävien ostovelkojen takaisinmaksuun on oltava aikaa vähintään vuosi. On pitkäaikaisen vieraan pääoman erä.

#### `KLVPOSTO` — Vastattavaa: lyhytaikaiset ostovelat

Ostovelat ovat vaihto-, käyttö-, tai rahoitusomaisuuden hankkimiseen  liittyviä velkoja. Lyhytaikaisen vieraan pääoman erä. Velka on lyhytaikainen, jos se  erääntyy maksettavaksi tasan vuoden tai sitä lyhyemmän ajan kuluessa.

#### `DSAAMYYP` — Pitkäaikaiset myyntisaamiset

Myyntisaamiset. Myyntisaamiset ovat varsinaisesta toiminnasta eli tavaroiden ja palveluiden myynnistä syntyneitä saamisia. Ne perustuvat yleensä lähetettyyn laskuun ja niitä seurataan myyntireskontrassa.  On pitkäaikaisten saamisten erä. Saaminen on pitkäaikainen, jos se erääntyy maksettavaksi yhtä vuotta pidemmän ajan kuluessa.

#### `DSAAMYYL` — Lyhyaikaiset myyntisaamiset

Lyhytaikaiset myyntisaamiset. Myyntisaamiset ovat varsinaisesta toiminnasta eli tavaroiden ja palveluiden myynnistä syntyneitä saamisia. Ne perustuvat yleensä lähetettyyn laskuun ja niitä seurataan myyntireskontrassa. On lyhytaikaisten saamisten erä. Saaminen on lyhytaikainen, jos se erääntyy maksettavaksi yhtä vuotta lyhyemmän ajan kuluessa.

#### `KKORVPO` — Korollinen vieras pääoma

Korollisten velkojen määrä taseen pitkä- ja lyhytaikaisesta vieraasta pääomasta sekä pääomalainat.

#### `EHDOSING` — Tilikaudelta päätetty / ehdotettu osingonjako

Tilikaudelta päätetty/ehdotettu osingonjako.

#### `LISKONE` — Koneiden ja laitteiden lisäykset

Koneiden ja kaluston lisäykset. Koneet, kalusto ja kuljetusvälineet ilmoitetaan yhdessä. Koneista ja kalustosta ilmoitetaan erikseen niihin sisältyvät tietokoneet ja ICT -laitteet.

#### `LISRAKEN` — Rakennusten ja rakennelmien lisäykset

Rakennusten ja rakennelmien lisäykset. Rakennuksilla tarkoitetaan asuinrakennuksia ja muita talonrakennuksia.

#### `DKOKONE` — Koneet ja kalusto tilikauden lopussa

Koneisiin ja kalustoihin tulee irtain käyttöomaisuus kuten tehdaskoneet, konttorikoneet, autot, trukit, traktorit, alukset, lentokoneet, kuljetuskalustot, televisiot, radiot, viestintäkalustot ja huonekalut. Leasingille otettua kalustoa ei lueta verotuksessa käyttöomaisuuteen, joten sitä ei merkitä tähän.

#### `DKORAKEN` — Rakennukset ja rakennelmat tilikauden lopussa

Rakennukset ja rakennelmat. Rakennuksiin kuuluvat kaikki yritystoiminnan rakennukset ja rakennelmat, sekä prosessia palvelevat että sosiaalisiin tarkoituksiin käytetyt  rakennukset. Rakennuksia ovat kirjanpitovelvollisen toiminnassa käyttämät tehdas-, varasto-, talous-, myymälä-, toimisto-, ja asuinrakennukset, hotellit, sairaalat, hallit, voima-asemat yms. Rakennelmia ovat siilot, polttoneste- ja happosäilöt, kalliosuojat ja -varastot sekä parakit.

#### `LISANTYH` — Aineeton käyttöomaisuus: lisäykset

Aineettomien hyödykkeiden lisäykset. Aineettomia hyödykkeitä ovat kehittämismenot, liikearvo, aineettomat oikeudet, muut pitkävaikutteiset menot sekä aineettomiin hyödykkeisiin kohdistuvat ennakkomaksut ja keskeneräiset hankinnat. Aineettomista oikeuksista ilmoitetaan erikseen siihen sisältyvät ATK -ohjelmistot.

#### `VAHAINTY` — Aineeton käyttöomaisuus: vähennykset

Aineettomien hyödykkeiden vähennykset.
Liiketoiminnasta johtuneet vähennykset tilikauden aikana sen arvon mukaisena, jolla liiketoimet on suoritettu, esimerkiksi luovutushinta tai muu vastike.

#### `LISANLYH` — Aineellinen käyttöomaisuus: lisäykset

Aineellisen käyttöomaisuuden lisäykset. Aineellista käyttöomaisuutta ovat esimerkiksi maa- ja vesialueet, rakennukset ja rakennelmat, koneet ja kalusto.

#### `VAHANLYH` — Aineellinen käyttöomaisuus: vähennykset

Aineellisen käyttöomaisuuden vähennykset. Aineellista käyttöomaisuutta ovat esimerkiksi maa- ja vesialueet, rakennukset ja rakennelmat, koneet ja kalusto.

#### `LISOSAKE` — Osakkeet ja osuudet: lisäykset

Taseen pysyvien vastaavien sijoituksiin kuuluvat osakkeiden ja osuuksien lisäykset.

#### `VAHOSAK` — Osakkeet ja osuudet: vähennykset

Taseen pysyvien vastaavien sijoituksiin kuuluvat osakkeiden ja osuuksien vähennykset.

#### `HENKLKMYH` — Henkilöstön lukumäärä yhteensä

Henkilöstön nuppilukumäärä yhteensä. Henkilöstön lukumäärä yhteensä. Yrityksen  työvoimaan luetaan kaikki henkilöt, jotka työskentelevät siinä tai sen lukuun.

#### `HENKKESK` — Henkilöstön lkm kokoaikavastaavana

Henkilöstön määrä kokoaikaiseksi muunnettuna.

#### `SIJOP` — Sijoitettu pääoma

Sijoitettu pääoma = KVARVEY + KKORVPO = Tilinpäätössiirtojen kertymä yhteensä + korollinen vieras pääoma.

#### `JALEU` — Jalostusarvo

Jalostusarvo. Tuotannon jalostusarvo (EU:n arvonlisäys perushintaan, sisältää tukipalkkiot). Jalostusarvo mittaa eri tuotannontekijöiden yhteenlaskettua jalostusarvoa toimipaikan/yrityksen liiketoiminnasta. Jalostusarvon tarkoituksena on kuvata yksikön  arvonlisäystä, joka syntyy tuotantotoiminnasta saatujen tuottojen ja tuotantotoimintaa varten hankittujen tuotantopanoskustannusten erotuksena. Kustannuksiin ei sisällytetä työvoimasta aiheutuvia kustannuksia. Tuotannon bruttoarvon avulla voidaan laskea jalostusarvo seuraavasti: BRUTTOARVO - aine- ja tarvikeostot - ostot yrityksen muilta toimipaikoilta - varastojen muutos - ulkopuoliset palvelut – muut kiinteät ja muuttuvat kulut pl. henkilöstökulut + kauppatavaroiden hankinta =  JALOSTUSARVO

#### `SIJTULO` — Pääoman tuotto

Pääoman tuotto = NETTOT-KORKULKO-KORKULMU-VALVERTU-VALVERMU = nettotulos - korkokulut - korkokulut muille - tuloverot - muut välittömät verot.

#### `KORKULKO` — Korko- ja muut rahoituskulut konsernin yrityksille

Korkokulut ja muut rahoituskulut saman konsernin yrityksille. Korko- ja muut rahoituskulut ovat  lyhytaikaisista sijoituksista saatavat korko- ja muut tuotot  sekä niistä johtuvat kurssierot.

#### `KORKULMU` — Korko- ja muut rahoituskulut muille

Korkokulut ja muut rahoituskulut  muille. Korko- ja muut rahoituskulut ovat  lyhytaikaisista sijoituksista saatavat korko- ja muut tuotot sekä niistä johtuvat kurssierot.

#### `NETTOVAR` — Nettovarallisuus

Nettovarallisuus, elinkeinoveroaineiston (EVR)  tieto.

#### `QUICKOS` — Quick ratio osoittaja

Quick ratio = rahoitusomaisuus / lyhytaikainen vieras pääoma. Quick ratio osoittaja = DSAAYHTL+DROARYHT+DRORAH = lyhytaikaiset saamiset yhteensä + rahoitusarvopaperit yhteensä + rahat ja pankkisaamiset

#### `QUICKNIM` — Quick ratio nimittäjä

Quick ratio = rahoitusomaisuus / lyhytaikainen vieras pääoma. Quick ratio nimittäjä = KLVPYHT-KLVPSAEN = lyhyaikainen vieras pääoma - lyhytaikaiset ennakkomaksut.

#### `VIENTIYH` — Vienti yhteensä

Vienti yhteensä. Erään sisältyy vienti EU-maihin ja EU:n ulkopuolisiin maihin. Tavaroiden vientiä on kotimaisten ja ulkomaisten talousyksiköiden välillä tapahtunut muutos tavaroiden omistuksessa. Toimitukset ulkomaiselle tytäryhtiölle tai haaraliikkeelle katsotaan tässä omistajan vaihdokseksi. Vientiin sisällytetään myös palkkatyöjalostuksen jälkeen palautetut tavarat jalostusarvolla lisättynä, vaikkei omistajuus vaihdukaan. Kauttakulkutavarat eivät sisälly vientiin. Tavaraviennin arvona käytetään EU:n sisä- ja ulkokaupassa verotonta myyntihintaa. Arvoon sisällytetään kuljetus- ja vakuutuskustannukset Suomen rajalla olevaan vientipaikkaan asti. Palvelujen vienti koostuu kaikista ulkomaisten talousyksiköiden kotimaisille talousyksiköille suorittamista palveluista. Saatavissa vuosilta 2006-2007.

#### `OPOSINKO` — Edellisen tilikauden tuloksesta maksettu osinko

Tilikauden aikana jaettu osinko. Oman pääoman erä.

#### `VOLOENNA` — Vaihto-omaisuus tilikauden lopussa

Ennakkomaksut. Vaihto-omaisuushyödykkeiden ennakkomaksut ovat suorituksia, jotka on maksettu etukäteen tilatusta vaihto-omaisuudesta, jota ei ole vielä vastaanotettu. On vaihto-omaisuuserä. Vaihto-omaisuutta on kirjanpitovelvollisen sellaisenaan tai jalostettuina luovutettavaksi tai kulutettavaksi tarkoitetut hyödykkeet

#### `SYRTUN` — Suojattu yritystunnus

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
