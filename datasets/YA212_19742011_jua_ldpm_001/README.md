# FIRM_PROD Teollisuuden toimipaikkapaneeli LDPM (YA212)

- **Identifier:** `YA212_19742011_jua_ldpm_001.xml`
- **DOI:** `work_2013-11_2013-11-25_ain_0001`
- **Temporal coverage:** 1974-01-01 - 2011-12-31
- **Published:** 2016-02-17
- **Organisation:** Tilastokeskus
- **Variable count:** 107
- **Observation count:** 241,471
- **Population:** Teollisuuden toimipaikat
- **Source:** Teollisuustilastokyselyt 1974 - 1994 ja rakennetilaston teollisuuden toimipaikkatiedot 1995 -
- **Related:** <a href= "http://www.tilastokeskus.fi/til/alyr/index.html">Alueellinen yritystoimintatilasto</a> <a href= "http://www.stat.fi/meta/rekisteriselosteet/tutka_rekisteriseloste_teollisuuden_tuotantotiedot.html">Teollisuuden tuotantotiedot</a>
- **Keywords:** bruttoarvo,henkilöstö,investoinnit,jalostusarvo,käyttöomaisuus,teollisuus,toimipaikat,tuotanto

## Description

Longitudinal Database on Plants in Finnish Manufacturing (LDPM) -aineisto on vuodet 1974 - 2011 käsittävä paneeli teollisuuden toimipaikoista. Paneeli sisältää toimipaikkatason tietoja tuotantopanoksista ja tuotoksesta sekä lukuisia taustamuuttujia. 

Aineisto on koottu teollisuustilastokyselystä (vuodet 1974 - 94) ja rakennetilaston teollisuustoimipaikkoja koskevista tiedoista (vuodet 1995-). Aineistossa on tästä syystä katkoskohta vuosien 1994 ja 1995 välillä sekä otoskehikon että muuttujasisällön osalta. Vuoteen 1994 kysely kattoi periaatteessa kaikki vähintään 5 hengen toimipaikat. Vuoden 1995 jälkeen mukana ovat kaikki vähintään 20 hengen yritysten toimipaikat (myös sellaiset, joiden koko on alle 5 henkeä). Aineiston otoskehikkoon sisältyy siis jokaisena vuotena vähintään 20 henkeä työllistäneet toimipaikat.

Aineiston rahamääräiset muuttujat on ilmaistu tuhansissa euroissa.

Pääosin tiedot on otettu rekisteristä “sellaisena kuin ne olivat”. Aineistossa ei pitäisi olla katoa (tai puuttuvia tietoja). Toisin sanoen, jos muuttujaa on kysytty kyseisenä vuotena, puuttuvan tiedon pitäisi tarkoittaa nollaa. Kaikissa tilanteissa tästä ei kuitenkaan ole täyttä varmuutta, joten kannattaa tapauskohtaisesti miettiä, tarkoittaako puuttuva tieto nollaa vai onko mahdollista, että oikeaa arvoa ei tiedetä.

Aineiston pääomamuuttuja on laskettu perpetual inventory method (PIM) -menetelmällä. Pääomamuuttujan laskentakaava on muotoa
K(t) = (1-s)K(t-1) + I(t),
jossa K(t) on pääomakanta vuonna t, s poistoaste ja I(t) investointi vuonna t. Pääomakantaa laskettaessa poistoasteen s arvona on käytetty 0,10. Laskettaessa pääomakantaa tällä menetelmällä tarvitaan tiedot toimipaikan investoinneista joka vuodelta toimipaikan perustamisvuodesta lähtien. Tämän kriteerin täyttävät vuonna 1974 ja sen jälkeen aloittaneet toimipaikat, joiden investointiaikasarjassa ei ole aukkoja. Ennen vuotta 1974 aloittaneille toimipaikoille investointiaikasarjan alkupäätä ei ole havaittu ja niiden kohdalla pääoman alkuarvon laskennassa on käytetty käyttöomaisuuden palovakuutusarvoa.

Lähtöaineiston tuotanto- ja kustannustiedot ovat nimellisarvoisia. Joitakin muuttujia (tuotanto, arvonlisä, välipanokset ja investoinnit) on muunnettu reaaliarvoisiksi käyttämällä vastaavia kansantalouden tilinpidon implisiittisiä hintaindeksejä.

Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@tilastokeskus.fi.

## Variables (107)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `stopc` | Longitudinal corrected code | — | — | — |
| `stop` | Original plant code | — | — | — |
| `stptunn` | Business register code | — | — | — |
| `syrtun` | Firm code | — | — | — |
| `vuosi` | Year | — | — | — |
| `Kunta` | Toimipaikan sijaintikunta | — | — | — |
| `TOL2008` | Nace 2 | — | — | — |
| `tol2008_2` | Nace 2, 2-digit, empiirinen avain | — | — | — |
| `TOL2002` | Nace 1 | — | — | — |
| `tol2002_2` | Nace 1, 2-digit, empiirinen avain | — | — | — |
| `tol95` | ISIC rev 3 | — | — | — |
| `TOL88` | tol88 | — | — | — |
| `TOL79` | ISIC rev 2 | — | — | — |
| `alvuosi` | Ensimmäinen esiintymisvuosi | — | — | — |
| `lopvuosi` | Viimeinen esiintymisvuosi | — | — | — |
| `TOIMYHT` | Deliveries | — | — | — |
| `JALTEOL` | Teollinen jalostusarvo | — | — | — |
| `JALKOK` | Kokonaisjalostusarvo | — | — | — |
| `BRAKOK` | kokonaisbruttoarvo | — | — | — |
| `mater` | Aineet ja tarvikkeet | — | — | — |
| `ener` | Energiapanokset | — | — | — |
| `serv` | Palvelupanokset | — | — | — |
| `RAKOTIM` | Käytetyt raaka-aineet, kotimaiset | — | — | — |
| `RAULKOM` | Käytetyt raaka-aineet, ulkomaiset | — | — | — |
| `tlaji` | Toiminnan laji | — | — | — |
| `BRAEU` | EU:n mukainen tuotannon bruttoarvo | — | — | — |
| `JALEU` | EU:n mukainen tuotannon jalostusarvo | — | — | — |
| `KULPOLT` | Polttoaineiden hankintakulut | — | — | — |
| `KULSAHKO` | Sähkön hankinta omaan käyttöön | — | — | — |
| `KULLAMPO` | Lämmön hankinta omaan käyttöön | — | — | — |
| `toimyhtr` | Kokonaistoimitukset, 2000 hinnoin (KT) | — | — | — |
| `jalteolr` | Teollinen jalostusarvo, 2000 hinnoin (KT) | — | — | — |
| `jalkokr` | Kokonaisjalostusarvo, 2000 hinnoin (KT) | — | — | — |
| `jaleur` | Jalostusarvo (EU), 2000 hinnoin (KT) | — | — | — |
| `brakokr` | Bruttotuotanto, 2000 hinnoin (KT) | — | — | — |
| `braeur` | Bruttotuotanto (EU), 2000 hinnoin (KT) | — | — | — |
| `materr` | Aineet ja tarvikkeet, 2000 hinnoin | — | — | — |
| `servr` | Palvelupanokset, 2000 hinnoin | — | — | — |
| `enerr` | Energiapanokset, 2000 hinnoin | — | — | — |
| `empb` | Työntekijöitä | — | — | — |
| `empw` | Toimihenkilöitä | — | — | — |
| `emp` | Palkansaajat, -2008 | — | — | — |
| `persons` | Henkilöt, -2008 | — | — | — |
| `hourb` | Työntekijöiden työtunnit | — | — | — |
| `hourw` | Toimihenkilöiden työtunnit | — | — | — |
| `houremp` | Palkansaajien tunnit | — | — | — |
| `avhour` | Kesk.työaika, tuhatta | — | — | — |
| `hourtot` | Tehdyt työtunnit | — | — | — |
| `wageb` | Työntekijöiden palkat, -2008 | — | — | — |
| `sospayb` | Työntekijöiden sosiaalikulut, -2008 | — | — | — |
| `wagew` | Toimihenkilöiden palkat, -2008 | — | — | — |
| `sospayw` | Toimihenkilöiden sosiaalikulut, -2008 | — | — | — |
| `wage` | Palkat | — | — | — |
| `sospay` | Sosiaalikulut | — | — | — |
| `PAPALKAT` | Maksetut palkat yhteensä | — | — | — |
| `PASOSKUL` | Palkatun henkilöstön sosiaalikulut yhteensä | — | — | — |
| `HENUPPI` | Henkilömäärä, adj. -2007 | — | — | — |
| `PALKMFTE` | Palkansaajat, full-time eq, -2005 based on hours worked | — | — | — |
| `PANUPPI` | Palkansaaja määrä, adj. -2007 | — | — | — |
| `YRNUPPI` | Yrittäjien määrä | — | — | — |
| `HELKMFTE` | Henkilöt, full-time eq, -2005 based on hours worked | — | — | — |
| `komhank` | Investoinnit, nimellinen | — | — | — |
| `komjha` | Pääomakanta, käyvin hinnoin (-85) | — | — | — |
| `vuokrat` | Vuokrat | — | — | — |
| `komhankr` | Investoinnit, 2000 hinnoin | — | — | — |
| `komjhar` | Pääomakanta, 2000 (-85) | — | — | — |
| `k00pim` | Pääomakanta PIM, 2000 hinnoin | — | — | — |
| `KATOIM` | Saatu korvaus korjauksista ja asennuksista | — | — | — |
| `PTTOIM` | Palkkiotöiden toimitusten arvo | — | — | — |
| `PATOIM` | Saatu bruttokorvaus muista palveluista | — | — | — |
| `export` | teollisuuden oma vienti | — | — | — |
| `KUSTTE` | Teolliset kustannukset | — | — | — |
| `KUSTKOK` | Kokonaiskustannukset | — | — | — |
| `evalue` | Hankitun sähkön arvo | — | — | — |
| `PALVHANK` | Palvelujen hankinta | — | — | — |
| `KAHANK` | Korjaus-, asennus- ja kunnossapitotyö | — | — | — |
| `PTHANK` | Teetetty palkkiotyö | — | — | — |
| `emwh` | Sähköenergian käyttö | — | — | — |
| `FOR50` | Ulk omist 50- (IS) (-94) | % | — | — |
| `FOR20_50` | Ulk omist 20-50 (IS) (-94) | % | — | — |
| `DOMPRIV` | Omistajatyyppi: Kotimainen yksityinen (-94) | — | — | — |
| `DOMGOV` | Omistajatyyppi: Kotimainen ei-yksityinen (-94) | — | — | — |
| `HEADUNIT` | Toimipaikkatyyppi: Pääkonttori | — | — | — |
| `INVUNIT` | Toimipaikkatyyppi: Investointitoimipaikka | — | — | — |
| `inventor` | Toimipaikkatyyppi: Varasto | — | — | — |
| `RDUNIT` | Toimipaikkatyyppi: T&K-yksikkö | — | — | — |
| `produnit` | Tuotantotoimipaikka tyyppi=3 tai 4 | — | — | — |
| `SALESUNI` | Toimipaikkatyyppi: Myyntikonttori | — | — | — |
| `servunit` | Toimipaikkatyyppi: Tehdaspalveluosasto | — | — | — |
| `ULKOPALV` | Ulkopuoliset palvelut (95-) | — | — | — |
| `KULKORAS` | Teetetyt korjaus-, kunnossapito- ja asennustyöt (95-) | — | — | — |
| `KULPATY` | Teetettyjen palkkatöiden kulut (95-) | — | — | — |
| `KULALIUR` | Aliurakointikulut (95-) | — | — | — |
| `KULTYVUO` | Työvoiman vuokrauskulut (95-) | — | — | — |
| `KULTUTKE` | Tutkimus- ja kehittämispalveluiden kulut (95-) | — | — | — |
| `KULKULJE` | Kuljetus- ja varastointikulut (95-) | — | — | — |
| `KULMAINO` | Mainos-, markkinointi- ja myyntipalvelukulut (95-) | — | — | — |
| `KULATK` | Atk-suunnit.- ja ohjelmointipalvelukulut (95-) | — | — | — |
| `KULPATEN` | Patenttien ja lisenssien kulut (95-) | — | — | — |
| `KULUMUUT` | Muut kuin edellä mainitut kulut (95-) | — | — | — |
| `exporteu` | Vienti EU-maihin (95-2007) | — | — | — |
| `MAA` | Omistajayrityksen maa (YREK, 86, 88-) | — | — | — |
| `OIK` | Oikeudellinen muoto (YREK, 86, 88-) | — | — | — |
| `ISL` | Institutionaalinen muoto (YREK, 86, 88-92) | — | — | — |
| `isl95` | Institutionaalinen muoto 95 (YREK, 93-99) | — | — | — |
| `oty95` | Oty95 (YREK, 93-) | — | — | — |
| `ulkomi` | Ulk. omist., % (YREK, 86, 88-) | — | — | — |

### Variable definitions

#### `stopc` — Longitudinal corrected code

Suojattu pitkittäiskorjattu STOP. Yksityiskohtaisissa tarkasteluissa on käynyt ilmi, että 1970-luvulla ja 1980-luvun alussa alkuperäisissä toimipaikkatunnuksissa on esiintynyt jonkin verran katkoksia. Aineiston pitkittäisominaisuuden parantamiseksi näitä katkoksia on pyritty korjaamaan. Apuna on käytetty toimipaikan sijaintia, omistajuutta ja toimialaa koskevia tietoja. Identifioinnissa ja korjauksissa on pyritty noudattamaan konservatiivista linjaa siten, ettei kahta eri toimipaikkaa tulkittaisi erheellisesti samaksi.
Erityisen paljon katkoksia esiintyy vuonna 1979; tuona vuonna kaikkiaan 660 tapausta kyettiin identifioimaan taustatietojen perusteella. Näyttää siltä, että kaikkia katkoksia ei kuitenkaan pystytty tunnistamaan. Tähän viittaa se, että aineiston mukaan tuona vuonna oli selvästi normaalia enemmän uusia sekä poistuvia toimipaikkoja. Tämä on syytä ottaa huomioon, kun tutkitaan esimerkiksi toimipaikkojen vaihtuvuutta tai työpaikkojen syntymis- ja tuhoutumisasteita. Vuodesta 1980 lähtien toimipaikkatunnukset näyttäisivät olevan pääasiassa kunnossa.

#### `stop` — Original plant code

Suojattu alkuperäinen toimipaikkatunnus

#### `stptunn` — Business register code

Suojattu toimipaikan tunnus yritysrekisterissä
Tämän tunnuksen avulla toimipaikalle voi liittää yritysrekisterin toimipaikkatason tietoja.

#### `syrtun` — Firm code

Suojattu yritystunnus

#### `vuosi` — Year

Tilastovuosi

#### `Kunta` — Toimipaikan sijaintikunta

#### `TOL2008` — Nace 2

Toimialakoodi, 2008 luokitus (Nace rev. 2), vuodesta 1995 alkaen

#### `tol2008_2` — Nace 2, 2-digit, empiirinen avain

Henkilöstömäärän mukaan luotu empiirinen toimiala-avain tol2008 2-numerotasolla (suositeltava)

#### `TOL2002` — Nace 1

Toimialakoodi, 2002 luokitus (Nace rev. 1), täydennetty luokituskannan avaimella

#### `tol2002_2` — Nace 1, 2-digit, empiirinen avain

Henkilöstömäärän mukaan luotu empiirinen toimiala-avain tol2002 2-numerotasolla (suositeltava)

#### `tol95` — ISIC rev 3

Toimialakoodi, 1995 luokitus (ISIC rev 3), täydennetty luokituskannan avaimella

#### `TOL88` — tol88

Toimialakoodi, 1988 luokitus, vuoteen 1994 asti

#### `TOL79` — ISIC rev 2

Toimialakoodi, 1979 luokitus (ISIC rev 2), vuoteen 1994 asti

#### `alvuosi` — Ensimmäinen esiintymisvuosi

Toimipaikan ensimmäinen esiitymisvuosi aineistossa

#### `lopvuosi` — Viimeinen esiintymisvuosi

Toimipaikan viimeinen esiintymisvuosi aineistossa

#### `TOIMYHT` — Deliveries

Kokonaistoimitukset

#### `JALTEOL` — Teollinen jalostusarvo

Poikkeaa kokonaisjalostusarvosta siinä, että tuotannon puolella eikä välipanoksista ole otettu huomioon ei-teollisia palveluja, vuodesta 2009- ei ole vertailukelpoinen aiempiin vuosiin.

#### `JALKOK` — Kokonaisjalostusarvo

Kokonaisjalostusarvo vuoteen 2008 asti. Jalostusarvo mittaa eri tuotannontekijöiden yhteenlaskettua jalostusarvoa toimipaikan/yrityksen liiketoiminnasta. Jalostusarvon tarkoituksena on kuvata yksikön arvonlisäystä, joka syntyy tuotantotoiminnasta saatujen tuottojen ja tuotantotoimintaa varten hankittujen tuotantopanoskustannusten erotuksena. Määritelmän mukaan kustannuksiin ei sisällytetä työvoimasta aiheutuvia kustannuksia. Tuotannon bruttoarvon avulla voidaan laskea jalostusarvo seuraavasti: BRUTTOARVO – aine- ja tarvikeostot – ostot yrityksen muilta toimipaikoilta – varastojen muutos – ulkopuoliset palvelut – muut kiinteät ja muuttuvat kulut pl. henkilöstökulut + kaup-patavaroiden hankinta =  JALOSTUSARVO

#### `BRAKOK` — kokonaisbruttoarvo

Kokonaisbruttoarvo vuoteen 2008 asti. Tuotannon bruttoarvo mittaa yrityksen tai toimipaikan oman tuotannon arvoa, sen tosiasiallista tuotantoa. Tuotannon bruttoarvon kaava on seuraava: Liikevaihto + toimitukset yrityksen muiden toimipaikkojen käyttöön + valmistevarastojen muutos + valmistus omaan käyttöön + liiketoiminnan muut tuotot – käyttöomaisuuden luovutusvoitot – kauppatavaroiden hankinta = BRUTTOARVO

#### `mater` — Aineet ja tarvikkeet

Vuodesta 2009- ei ole vertailukelpoinen aiempiin vuosiin.

#### `ener` — Energiapanokset

Vuodesta 2009- ei ole vertailukelpoinen aiempiin vuosiin.

#### `serv` — Palvelupanokset

Vuodesta 2009- ei ole vertailukelpoinen aiempiin vuosiin.

#### `RAKOTIM` — Käytetyt raaka-aineet, kotimaiset

Vuoteen 1984 asti

#### `RAULKOM` — Käytetyt raaka-aineet, ulkomaiset

Vuoteen 1984 asti

#### `tlaji` — Toiminnan laji

Toiminnan laji 
1 =  pääkonttori  tms. 
2 =  rakenteilla oleva toimipaikka  eli  investointitoimipaikka 
3 =  varsinainen  toimipaikka  (rakennetilasto) 
4 =  voimalaitokset 
5 =  hallintayhtiö 
6 =  keskusvarasto 
7 =  tutkimusyksikkö 
8 =  erillinen  myyntikonttori 
9 =  tehdaspalveluosasto 
0/ NULL/ tyhjä  =  haaraliike

#### `BRAEU` — EU:n mukainen tuotannon bruttoarvo

Tuotannon bruttoarvo (EU:n määritelmän mukainen, sisältää tukipalkkiot). Vuoteen 1994 asti braeu=brakok. Tuotannon bruttoarvo mittaa yrityksen tai toimipaikan oman tuotannon arvoa, sen tosiasiallista tuotantoa. Tuotantotoimintaan lasketaan mukaan kaikki tuotantoon liittyvät tuotot ( toimitukset yrityksen ulkopuolelle ja toimitukset yrityksen muille oimipaikoille)  ja niitä oikaistaan käyttöomaisuuden luovutusvoitoilla. Käyttöomaisuuden luovutusvoittoja ei pidetä tuotannollisina erinä vaan satunnaisina tuottoina. Kauppatavaroiden hankinta vähennetään tuotantotoiminnan tuotoista, jotta tuotantotoimintaan saadaan mukaan vain kauppatavaroiden myynnistä yritykselle/toimipaikalle syntyvä marginaali.  Tuotannon bruttoarvo lasketaan toimipaikan/yrityksen ilmoittaman laskennallisen käyttökatteen avulla. Tuotannon bruttoarvon kaava on seuraava: Liikevaihto + toimitukset yrityksen muiden toimipaikkojen käyttöön +valmistevarastojen muutos + valmistus omaan käyttöön + liiketoiminnan muut tuotot – käyttöomaisuuden luovutusvoitot - kauppatavaroiden hankinta = BRUTTOARVO

#### `JALEU` — EU:n mukainen tuotannon jalostusarvo

Tuotannon jalostusarvo (EU:n arvonlisäys perushintaan, sisältää tukipalkkiot). Vuoteen 1994 asti jaleu=jalkok. Jalostusarvo mittaa eri tuotannontekijöiden yhteenlaskettua jalostusarvoa toimipaikan/yrityksen liiketoiminnasta. Jalostusarvon tarkoituksena on kuvata yksikön  arvonlisäystä, joka syntyy tuotantotoiminnasta saatujen tuottojen ja tuotantotoimintaa varten hankittujen tuotantopanoskustannusten erotuksena. Määritelmän mukaan kustannuksiin ei sisällytetä työvoimasta aiheutuvia kustannuksia. Tuotannon bruttoarvon avulla voidaan laskea jalostusarvo seuraavasti: BRUTTOARVO - aine- ja tarvikeostot - ostot yrityksen muilta toimipaikoilta - varastojen muutos - ulkopuoliset palvelut – muut kiinteät ja muuttuvat kulut pl. henkilöstökulut + kauppatavaroiden hankinta =  JALOSTUSARVO

#### `KULPOLT` — Polttoaineiden hankintakulut

Polttoaineiden hankinta. Polttoaineiksi luetaan yrityksen tuotannollisen toiminnan tai sen ajoneuvojen energialähteiksi hankitut aineet. Saatavissa vuodesta 1995 lähtien.

#### `KULSAHKO` — Sähkön hankinta omaan käyttöön

Sähkön hankinta omaan käyttöön (pl.  välityssähkö). Sähköenergian hankinta käsittää tuotantoprosessissa käytetyn sähkön lisäksi myös yrityksen tilojen valaistukseen, tuuletukseen, lämmitykseen ym. käytetyn sähkön, mutta ei myytäväksi hankittua sähköä. Saatavissa vuodesta 1995 lähtien.

#### `KULLAMPO` — Lämmön hankinta omaan käyttöön

Lämmön hankinta omaan käyttöön (pl. välityslämpö). Lämpöenergian hankintaan luetaan yrityksen tuotantoprosessissa käytetyn lämmön lisäksi myös tilojen lämmitykseen käytetty energia, mutta ei myytäväksi hankittua lämpöä. Saatavissa vuodesta 1995 lähtien.

#### `toimyhtr` — Kokonaistoimitukset, 2000 hinnoin (KT)

#### `jalteolr` — Teollinen jalostusarvo, 2000 hinnoin (KT)

Vuodesta 2009- ei ole vertailukelpoinen aiempiin vuosiin.

#### `jalkokr` — Kokonaisjalostusarvo, 2000 hinnoin (KT)

Vuoteen 2008 asti.

#### `jaleur` — Jalostusarvo (EU), 2000 hinnoin (KT)

Saatavissa vuoteen 2008 asti. Vuoteen 1994 asti jaleur=jalkokr.

#### `brakokr` — Bruttotuotanto, 2000 hinnoin (KT)

Vuoteen 2008 asti.

#### `braeur` — Bruttotuotanto (EU), 2000 hinnoin (KT)

Saatavissa vuoteen 2008 asti. Vuoteen 1994 asti braeur=brakokr.

#### `materr` — Aineet ja tarvikkeet, 2000 hinnoin

Vuodesta 2009- ei ole vertailukelpoinen aiempiin vuosiin.

#### `servr` — Palvelupanokset, 2000 hinnoin

Vuodesta 2009- ei ole vertailukelpoinen aiempiin vuosiin.

#### `enerr` — Energiapanokset, 2000 hinnoin

Vuodesta 2009- ei ole vertailukelpoinen aiempiin vuosiin.

#### `empb` — Työntekijöitä

Työntekijöiden lukumäärä (B viittaa sanaan ”blue-collar”) vuoteen 2008 asti
Työntekijöiksi luetaan välittömästi teollisuuden valmistusprosessiin osallistuvat henkilöt, apuosastojen työntekijät kuten pakkaajat, huolto- ja kunnossapitotyöntekijät, rakennusosastojen työntekijät, koneenkäyttäjät, lämmittäjät, siivoojat jne. Myös sellaiset työnjohtajat, jotka osallistuvat myös varsinaiseen valmistustyöhön, luetaan työntekijöiksi. Henkilöiden lukumäärät ilmoitetaan tilikauden keskimääräisinä lukuina. Luvut voidaan laskea esim. jakamalla kuukausikeskimäärien summa tilikauden kuukausimäärällä. Ks. myös henkilöstön lukumäärän määritelmä.

#### `empw` — Toimihenkilöitä

Toimihenkilöiden lukumäärä (W viittaa sanaan ”white-collar”) vuoteen 2008 asti
Toimihenkilöiksi luetaan muut kuin yrittäjät ja työntekijät. Henkilöiden lukumäärät ilmoitetaan tilikauden keskimääräisinä lukuina. Luvut voidaan laskea esim. jakamalla kuukausikeskimäärien summa tilikauden kuukausimäärällä. Ks. myös henkilöstön lukumäärän määritelmä.

#### `emp` — Palkansaajat, -2008

emp=empb+empw, vuoteen 2008 asti.

#### `persons` — Henkilöt, -2008

Vuoteen 2008 asti. Yrityksen työvoimaan luetaan kaikki henkilöt, jotka työskentelevät siinä tai sen lukuun. Työvoima luokitellaan itsenäisiin yrittäjiin (omistajiin), toimihenkilöihin ja työntekijöihin Henkilöiden lukumäärät ilmoitetaan tilikauden keskimääräisinä lukuina. Luvut voidaan laskea esim. jakamalla kuukausikeskimäärien summa tilikauden kuukausimäärällä. Henkilöiden lukumääriin lasketaan 1) kaikki tilastoyksikön palveluksessa olevat, myös harjoittelijat, tilapäiset ja osa-aikaiset (osa-aikaiset ilmoitetaan muuntamatta heitä kokopäiväisiksi), 2) vuosilomalla olevat, 3) sairaslomalla olevat, 4) äitiyslomalla olevat, 5) lakossa tai määräaikaisesti lomautetut, 6) kertausharjoituksissa olevat ja 7) kotityöntekijät.

#### `hourb` — Työntekijöiden työtunnit

Vuoteen 2008 asti.

#### `hourw` — Toimihenkilöiden työtunnit

Vuoteen 2008 asti.

#### `houremp` — Palkansaajien tunnit

Vuoteen 2008 asti.

#### `avhour` — Kesk.työaika, tuhatta

Keskimääräinen työaika per henkilö, tuhatta. Vuoteen 2008 asti.

#### `hourtot` — Tehdyt työtunnit

Suositeltava työpanoksen mittari, jos tarkasteluperiodi päättyy 2008 tai ennen. Työtunnit ovat tilikauden aikana tehtyjen todellisten työtuntien summa. Työtunneista on  vähennettävä poissaoloajat (sairasloma, vuosiloma, pekkaspäivät tms.) sekä ns. ylityökorotukset. (Odotusajan työtunnit lasketaan mukaan, jos niistä on maksettu palkkaa). Huom. Työtuntitiedoissa on laadullisia ongelmia ja noin puolet tiedoista on imputoitu.

#### `wageb` — Työntekijöiden palkat, -2008

Vuoteen 2008 asti.

#### `sospayb` — Työntekijöiden sosiaalikulut, -2008

Vuoteen 2008 asti. Erä sisältää maksettuihin palkkoihin perustuvat lakisääteiset ja vapaaehtoiset sosiaalivakuutusmaksut. Työnantajan lakisääteisiin sosiaalivakuutusmaksuihin luetaan: 1) sosiaaliturvamaksu, 2) työttömyysvakuutusmaksu, 3) LEL- ja TEL-vakuutusmaksu, 4) tapaturmavakuutusmaksu, 5) ryhmähenkivakuutusmaksu. Vapaaehtoisiin sosiaalivakuutusmaksuihin luetaan: 1) LEL- ja TEL-lisäturvamaksut, 2) henki- ja eläkevakuutusyhtiöille maksetut ryhmähenki- ja ryhmäeläkevakuutusmaksut, 3) työpaikkojen avustuskassoihin (eläke-, hautaus-, eroavustus- sekä sairausvakuutuskassoihin) maksetut kannatus-maksut sekä  maksetut eläkkeet.  Erään eivät sisälly henkilöstön koulutus-, virkistys-, harrastustoiminnan tai muut vastaavat kulut.

#### `wagew` — Toimihenkilöiden palkat, -2008

Vuoteen 2008 asti.

#### `sospayw` — Toimihenkilöiden sosiaalikulut, -2008

Vuoteen 2008 asti.

#### `wage` — Palkat

#### `sospay` — Sosiaalikulut

#### `PAPALKAT` — Maksetut palkat yhteensä

Vuodesta 1995 alkaen.

#### `PASOSKUL` — Palkatun henkilöstön sosiaalikulut yhteensä

Vuodesta 1995 alkaen.

#### `HENUPPI` — Henkilömäärä, adj. -2007

Vuoteen 2007 asti henuppi=persons*1,051 (kerroin laskettu vuoden 2008 perusteella).

#### `PALKMFTE` — Palkansaajat, full-time eq, -2005 based on hours worked

Vuoteen 2005 asti palkmfte=(hourb+hourw)*0.607 (kerroin laskettu vuosien 2006-2008 perusteella).

#### `PANUPPI` — Palkansaaja määrä, adj. -2007

Vuoteen 2007 asti panuppi=(empb+empw)*1.051 (kerroin laskettu vuoden 2008 perusteella).

#### `YRNUPPI` — Yrittäjien määrä

2008 lähtien.

#### `HELKMFTE` — Henkilöt, full-time eq, -2005 based on hours worked

Vuoteen 2005 asti helkmfte = hourtot*0.607 (kerroin laskettu vuosien 2006-2008 perusteella). Arvioitu myöhempien tietojen perusteella. Ensisijainen henkilöstömuuttuja, jos käytössä periodi 1995- tai koko ajanjakso 1974 - 2011. Hourtot on suositeltava työpanoksen mittari, jos tarkasteltava ajanjakso päättyy vuoteen 2008 tai ennen.

#### `komhank` — Investoinnit, nimellinen

Käyttöomaisuuden nettoinvestoinnit yhteensä

#### `komjha` — Pääomakanta, käyvin hinnoin (-85)

Käyttöomaisuuden jälleenhankinta-arvo (palovakuutusarvo) käyvin hinnoin (1974-79, 81-1984)

#### `vuokrat` — Vuokrat

Vuokrakulut yhteensä. Puuttuu 1985. Erä sisältää vuokrakulut maa- ja vesialueista, leasingeistä ja muista vuokrista. Maa- ja vesialueita ovat mm. maa- ja metsäalueet, rakennetut ja rakentamattomat tontit, koskitilat, vesijätöt ja vesialueet. Yritys voi hankkia käyttöomaisuutta joko käyttöleasing-sopimuksella tai rahoitusleasing-sopimuksella.  Käyttöleasing-sopimuksessa laitteen vuokraava yritys tekee sopimuksen suoraan laitetta käyttävän yrityksen kanssa.  Rahoitusleasing-sopimuksessa laitteen tarvitsija sopii, että rahoitusyhtiö ostaa laitteen ja vuokraa sen laitetta tarvitsevalle. Leasingkulut kattavat siten yrityksen leasing-sopimuksilla vuokraamien käyttöomaisuushyödykkeiden vuokrakulut. Muita vuokria ovat asuinrakennusten ja huoneistojen sekä liike-, tehdas-, konttori-, varasto- ym. rakennusten  sekä koneiden ja laitteiden vuokrakulut sekä sorakuopista, malmi- ja mineraaliesiintymistä, kivilouhoksista, turvesoista ym. maksetut vuokrat.

#### `komhankr` — Investoinnit, 2000 hinnoin

Deflatoinnissa käytetty kansantalouden tilinpidon implisiittistä investointien hintaindeksiä

#### `komjhar` — Pääomakanta, 2000 (-85)

Käyttöomaisuuden jälleenhankinta-arvo (palovakuutusarvo) vuoden 2000 hinnoin (1974-1979, 1981-1985). Deflatoinnissa käytetty kansantalouden tilinpidon implisiittistä investointien hintaindeksiä.

#### `k00pim` — Pääomakanta PIM, 2000 hinnoin

Pääomakanta saatavissa vuodesta 1975 alkaen. Aineiston pääomamuuttuja on laskettu perpetual inventory method (PIM) -menetelmällä. Pääomamuuttujan laskentakaava on muotoa
K(t) = (1-s)K(t-1) + I(t),
jossa K(t) on pääomakanta vuonna t, s poistoaste ja I(t) investointi vuonna t. Pääomakantaa laskettaessa poistoasteen s arvona on käytetty 0,10. Laskettaessa pääomakantaa tällä menetelmällä tarvitaan tiedot toimipaikan investoinneista joka vuodelta toimipaikan perustamisvuodesta lähtien. Tämän kriteerin täyttävät vuonna 1974 ja sen jälkeen aloittaneet toimipaikat joiden investointiaikasarjassa ei ole aukkoja. Ennen vuotta 1974 aloittaneille toimipaikoille investointiaikasarjan alkupäätä ei ole havaittu ja niiden kohdalla pääoman alkuarvon laskennassa on käytetty käyttöomaisuuden palovakuutusarvoa. Pääomakannan deflatoinnissa on käytetty kansantalouden tilinpidon implisiittistä investointien hintaindeksiä

#### `KATOIM` — Saatu korvaus korjauksista ja asennuksista

Vuoteen 1994 asti.

#### `PTTOIM` — Palkkiotöiden toimitusten arvo

Vuoteen 1994 asti.

#### `PATOIM` — Saatu bruttokorvaus muista palveluista

Vuoteen 1994 asti.

#### `export` — teollisuuden oma vienti

Toimipaikan vienti yhteensä, saatavissa vuoteen 2007 asti. Erään sisältyy vienti EU-maihin ja EU:n ulkopuolisiin maihin. Tavaroiden vientiä on kotimaisten ja ulkomaisten talousyksiköiden välillä tapahtunut muutos tavaroiden omistuksessa. Toimitukset ulkomaiselle tytäryhtiölle tai haaraliikkeelle katsotaan tässä omistajan vaihdokseksi. Vientiin sisällytetään myös palkkatyöjalostuksen jälkeen palautetut tavarat jalostusarvolla lisättynä, vaikkei omistajuus vaihdukaan. Kauttakulkutavarat eivät sisälly vientiin. Tavaraviennin arvona käytetään EU:n sisä- ja ulkokaupassa verotonta myyntihintaa. Arvoon sisällytetään kuljetus- ja vakuutuskustannukset Suomen rajalla olevaan vientipaikkaan asti. Palvelujen vienti koostuu kaikista ulkomaisten talousyksiköiden kotimaisille talousyksiköille suorittamista palveluista.

#### `KUSTTE` — Teolliset kustannukset

Vuoteen 1994 asti.

#### `KUSTKOK` — Kokonaiskustannukset

Vuoteen 1994 asti.

#### `evalue` — Hankitun sähkön arvo

Vuodesta 2009- ei ole vertailukelpoinen aiempiin vuosiin.

#### `PALVHANK` — Palvelujen hankinta

Vuoteen 1994 asti.

#### `KAHANK` — Korjaus-, asennus- ja kunnossapitotyö

Vuoteen 1994 asti.

#### `PTHANK` — Teetetty palkkiotyö

Vuoteen 1994 asti.

#### `emwh` — Sähköenergian käyttö

Vuoteen 1994 asti.

#### `FOR50` — Ulk omist 50- (IS) (-94)

**Unit:** %

Ulkomainen omistus yli 50 prosenttia (IS). Vuoteen 1994 asti.

#### `FOR20_50` — Ulk omist 20-50 (IS) (-94)

**Unit:** %

Ulkomainen omistus 20-50 prosenttia (IS). Vuoteen 1994 asti.

#### `DOMPRIV` — Omistajatyyppi: Kotimainen yksityinen (-94)

Vuoteen 1994 asti.

#### `DOMGOV` — Omistajatyyppi: Kotimainen ei-yksityinen (-94)

Vuoteen 1994 asti.

#### `HEADUNIT` — Toimipaikkatyyppi: Pääkonttori

#### `INVUNIT` — Toimipaikkatyyppi: Investointitoimipaikka

#### `inventor` — Toimipaikkatyyppi: Varasto

#### `RDUNIT` — Toimipaikkatyyppi: T&K-yksikkö

#### `produnit` — Tuotantotoimipaikka tyyppi=3 tai 4

#### `SALESUNI` — Toimipaikkatyyppi: Myyntikonttori

#### `servunit` — Toimipaikkatyyppi: Tehdaspalveluosasto

#### `ULKOPALV` — Ulkopuoliset palvelut (95-)

Vuodesta 1995 lähtien.

#### `KULKORAS` — Teetetyt korjaus-, kunnossapito- ja asennustyöt (95-)

Ulkopuolisilla teetettyjen korjaus-, kunnossapito- ja asennustöiden arvo mukaan luettuna laskutettujen materiaalien arvo. Vuodesta 1995 lähtien.

#### `KULPATY` — Teetettyjen palkkatöiden kulut (95-)

Palkkatyö on tuotteiden valmistuttamista toisella talousyksiköllä. Käytettävät aineet ja tarvikkeet ovat pääosin valmistuttajan omistuksessa tai hallinnassa. Vuodesta 1995 lähtien.

#### `KULALIUR` — Aliurakointikulut (95-)

Vuodesta 1995 lähtien.

#### `KULTYVUO` — Työvoiman vuokrauskulut (95-)

Vuodesta 1995 lähtien.

#### `KULTUTKE` — Tutkimus- ja kehittämispalveluiden kulut (95-)

Tutkimusmenoilla tarkoitetaan ulkopuolisilta yrityksiltä hankittuja tutkimus- ja kehittämispalveluja. Tutkimus- ja kehittämispalvelut ovat uuden tieteellisen tai teknisen tiedon tuottamiseksi tarpeellisesta suunnitelmallisesta tutkimustoiminnasta aiheutuneita menoja. Vuodesta 1995 lähtien.

#### `KULKULJE` — Kuljetus- ja varastointikulut (95-)

Erä sisältää yrityksen ulkopuolelta ostetut kuljetus- ja varastointipalvelut, terminaali- ja lastinkäsittelypalvelut. Varastointipalveluilla tarkoitetaan tässä itsenäisinä palveluina tarjottuja varastointipalveluja. Tähän sisältyvät esim. välivarastointipalvelut kylmävarastoissa ja tullivarastoissa sekä konttien säilytys jne. Jonkin tietyn alueen tai rakennuksen tai sen osan vuokraus varastoksi ei sisälly tähän. Vuodesta 1995 lähtien.

#### `KULMAINO` — Mainos-, markkinointi- ja myyntipalvelukulut (95-)

Erä sisältää yrityksen ulkopuolelta hankitut mainos-, myynti- ja markkinointikulut. Tällaisia eri ovat esimerkiksi: tuotteiden markkinoinnin ja myynnin aiheuttamat kulut, mainonnan sekä myyntinäyttelyiden kulut, mainostoimistojen palvelut, markkinoinnin, viestinnän ja suhdetoiminnan konsultointiin, markkinatutkimuksiin ja mielipideselvityksiin liittyvät kulut,  ulko- ja liikennemainosten pystyttämiseen ja hoitoon liittyvät  kulut ,  näyteikkunoiden somistukseen ja näyttelytilojen suunnitteluun liittyvät kulut, urheilumainontaan, puhelinmainontaan, ilmamainontaan jne. liittyvät kulut sekä  messujen yms. tuote-esittelytilaisuuksien järjestämisestä aiheutuvat kulut. Vuodesta 1995 lähtien.

#### `KULATK` — Atk-suunnit.- ja ohjelmointipalvelukulut (95-)

Erä sisältää yrityksen ulkopuolelta hankitut, asiakkaan laskuun tapahtuvat atk-palvelut. Tällaisia palveluja ovat automaattiseen tietojenkäsittelyyn liittyvä laitteisto- ja ohjelmistokonsultointi, ohjelmistojen suunnittelu ja valmistus, tietokone- ja käsittelypalvelutoiminta, tietokantaisännöinti, konttori- ja tietokoneiden korjaus ja huolto, muu tietojenkäsittelypalvelu, esim. systeemityöpalvelu, atk-ohjelmistojen ylläpitopalvelu sekä atk-ohjelmistokonsultointi. Vuodesta 1995 lähtien.

#### `KULPATEN` — Patenttien ja lisenssien kulut (95-)

Kulut rojalteista, patenteista ja lisensseistä. Erä sisältää muille maksetut korvaukset patenttien ja lisenssien käyttöoikeuksista. Vuodesta 1995 lähtien.

#### `KULUMUUT` — Muut kuin edellä mainitut kulut (95-)

Vuodesta 1995 lähtien.

#### `exporteu` — Vienti EU-maihin (95-2007)

1995-2007.

#### `MAA` — Omistajayrityksen maa (YREK, 86, 88-)

Omistajayrityksen maa (yritysrekisterin tieto, 1986, 1988-).

#### `OIK` — Oikeudellinen muoto (YREK, 86, 88-)

Oikeudellinen muoto (YREK, 1986, 1988-)
11 = luonnollinen henkilö, 12 = kuolinpesä, perikunta, 
13 = verotusyhtymä (esim. rekisteröimätön osakeyhtiö tai rakennustyöyhteenliit-tymä), 
14 = avoin yhtiö, 15 = konkurssipesä, 21 = kommandiittiyhtiö, 
22 = laivanisännistöyhtiö ( ei osakeyhtiö), 
31 = osakeyhtiö, 
32 = keskinäinen vakuutusyhtiö, 33 = säästöpankki, 
34 = eläkesäätiö tai -kassa, työeläkelaitos, työttömyys- tai avustuskassa, 
35 = asunto-osakeyhtiö, 41 = osuuskunta, 
51 = säätiö, rahasto, 52 = aatteellinen yhdistys (ry., rekisteröiyty yhdistys), 
53 = keskinäinen vahinkovakuutusyhdistys (joskus myös keskinäinen vakuutusyh-tiö), 
54 = taloudellinen yhdistys (juridisesti usein aatteellinen yhdistys, jonka liiketoi-minata on yrek:ssä todettu merkittäväksi), 
61 = julkinen viranomainen, 62 = julkinen liikelaitos, 63 = julkisoikeudellinen yhtei-sö, 
71 = valtionkirkko, 72 = muu uskonnollinen yhteisö, 
90 = muu oikeudellinen muoto (esim. ulkomaisen talousyksikön suomessa oleva sivuliike tai sen muu epäitsenäinen osa).

#### `ISL` — Institutionaalinen muoto (YREK, 86, 88-92)

Institutionaalinen muoto (yritysrekisteri, 1986, 1988-1992)

#### `isl95` — Institutionaalinen muoto 95 (YREK, 93-99)

Institutionaalinen muoto 1995 luokituksen mukaan, yritysrekisteri (1993-1999)

#### `oty95` — Oty95 (YREK, 93-)

Omistajatyyppi, yritysrekisteri (1993-)

#### `ulkomi` — Ulk. omist., % (YREK, 86, 88-)

Ulkomainen omistus, prosenttia (yritysrekisterin tieto, vuosille 1986, 1988-2008)

---

[← Back to catalogue](../../README.md)
