# FIRM_BASE oikeudellisten yksiköiden perustiedot

- **Identifier:** `FIRM_BASE_jua_legalunits_001.xml`
- **DOI:** `yty_201300_vaa_oikeudellinen_yksikko_001`
- **Temporal coverage:** —
- **Published:** 2025-06-05
- **Organisation:** Tilastokeskus
- **Variable count:** 70
- **Observation count:** —
- **Population:** Oikeudelliset yksiköt (yritykset ja julkisyhteisöt)
- **Source:** Verohallinnon asiakastietokanta (ASITK) + kunkin päivityksen yhteydessä Tilastokeskuksessa johdetut (päätellyt) tiedot.

## Description

FIRM_BASE-aineisto sisältää yritystietovaraston oikeudellisten yksiköiden kuukausittain päivittyvät taustatiedot, jotka pohjautuvat Verohallinnon asiakastietokantaan ja Tilastokeskuksen yritysrekisterin päättelyihin. Luokitus- ym. tiedot sisältävät tietojen muutoshistorian koko voimassaoloajaltaan. Tutkimusaineiston tiedot päivittyvät noin 45 päivän viiveellä.
 
Aineisto sisältää perustietoja mm. yritysten ja julkisyhteisöjen toimialasta, kotikunnasta, oikeudellisesta muodosta, sektoriluokasta, omistajatyypistä ja alv-velvollisuudesta. 

Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@stat.fi.

## Variables (70)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `yrtun_s` | Suojattu yrityksen (oikeudellisen yksikön) Y-tunnus. | — | — | — |
| `yritysID_s` | Suojattu yritys-ID, yrityksen tunnus | — | — | — |
| `konserniID_s` | Suojattu konsernitunnus | — | — | — |
| `virastotunnus_s` | Suojattu valtion virastotunnus | — | — | — |
| `AlPvm` | Oikeudellisen yksikön aloituspvm | — | — | RE |
| `LopPvm` | Oikeudellisen yksikön hallinnollinen lopetuspvm | — | — | RE |
| `toimAlPvm` | Oikeudellisen yksikön taloudellisen toiminnan aloituspvm | — | — | RE |
| `toimLopPvm` | Oikeudellisen yksikön taloudellisen toiminnan lopetuspvm | — | — | RE |
| `VerohOikMuoto` | Oikeudellinen muoto (Verohallinto) | — | verohoikmuot_2_2012_01_01 | luokitus, RE |
| `VerohOikAlPvm` | Verohallinnon oikeudellisen muodon alkupvm | — | — | RE |
| `Eurooppayhtio` | Tieto siitä, onko oikeudellinen yksikkö eurooppayhtiö | — | vast_vaihtoehdo_69_2012_01_01 | RE, luokitus |
| `Kuntayhtyma` | Tieto siitä, onko oikeudellinen yksikkö kuntayhtymä. | — | vast_vaihtoehdo_69_2012_01_01 | johdettu, luokitus, RE |
| `Ohi` | Julkisyhteisöjen ohitustieto | — | vast_vaihtoehdo_69_2012_01_01 | RE, luokitus, johdettu |
| `JulkisyhtTyyppi` | Julkisyhteisötyyppi oikeudellisella yksiköllä | — | jlkyhttyyp_2_2012_01_01 | RE, luokitus |
| `Kieli` | Oikeudellisen yksikön asiointikieli YTY:ssä, verohallinnon mukaan. | — | kieli_22_2012_01_01 | luokitus, RE |
| `UlkomVuokratyonantaja` | Koodi ulkomaalaisten vuokratyönantajana toimimisesta | — | vast_vaihtoehdo_69_2012_01_01 | RE, luokitus |
| `Kansalaisuus` | Kansalaisuuden maatunnus | — | valtio_2_2012_01_01 | luokitus, RE |
| `YleishYhteiso` | Koodi yleishyödyllisestä yhteisöstä, verotuksessa | — | vast_vaihtoehdo_69_2012_01_01 | RE, luokitus |
| `YleishAlPvm` | Yleishyödyllisenä yhteisönä aloituspvm | — | — | RE |
| `TotaalToimAlPvm` | Oikeudellisen yksikön totaalisen toiminnan alkupvm verohallinnossa | — | — | RE |
| `LisPvm` | Oikeudellisen yksikön lisäyspvm yritysrekisteriin / YTY-tuotantokantaan | — | — | RE |
| `tilaPerus` | Perustietojen tila oikeudellisella yksiköllä | — | perustiettila_2_2012_01_01 | RE, johdettu, aputiedot_tekniset |
| `oikMuoto` | Oikeudellisen yksikön oikeudellinen (juridinen) muoto yritysrekisterissä | — | oikeudell_muoto_1_1984_01_01 | luokitus, RE |
| `omtyyppi` | Omistajatyyppi oikeudellisella yksiköllä | — | omistajatyyppi_1_1995_01_01 | RE, luokitus |
| `sektoriluokka` | Oikeudellisen yksikön sektoriluokka | — | sektoriluokitus_11_2013_01_01 | luokitus, RE |
| `sektoriAlPvm` | Sektoriluokan muutos-/alkupäivämäärä | — | — | RE |
| `toiminnallisuudenTila` | Oikeudellisen yksikön toiminnallisuuden tila | — | toimtila_2_2012_01_01 | luokitus, RE |
| `tol2008` | Toimiala (TOL2008) | — | toimiala_1_2008_01_01 | luokitus, RE |
| `verohTol2008` | Verohallinnon antama toimialakoodi (TOL2008) oikeudelliselle yksikölle | — | toimiala_1_2008_01_01 | luokitus, RE |
| `kotikunta` | Oikeudellisen yksikön virallisen asuin-/kotikunnan kuntakoodi | — | — | RE, luokitus |
| `ALVVelvLiiketoimAlPvm` | ALV-velvollisen liiketoiminnan alkupvm | — | — | RE |
| `ALVVelvLiiketoimLopPvm` | ALV-velvollisen liiketoiminnan loppupvm | — | — | RE |
| `ALVVelvAlkutuotAlPvm` | ALV-velvollinen alkutuottajuudesta ja/tai taide-esineen tekijänä aloituspäivä | — | — | RE |
| `ALVVelvAlkutuotLopPvm` | ALV-velvollinen alkutuottajuudesta ja/tai taide-esineen tekijänä lopetuspäivä | — | — | RE |
| `ALVVelvKiintVuokrAlPvm` | ALV-velvollinen kiinteistön käyttöoikeuden luovuttajana aloituspäivä | — | — | RE |
| `ALVVelvKiintVuokrLopPvm` | ALV-velvollinen kiinteistön käyttöoikeuden luovuttajana lopetuspäivä | — | — | RE |
| `ALVVelvPorotalAlPvm` | ALV-velvollinen porotaloudesta aloituspäivä | — | — | RE |
| `ALVVelvPorotalLopPvm` | ALV-velvollinen porotaloudesta lopetuspäivä | — | — | RE |
| `ALVVelvUlkomAlPvm` | ALV-velvollisen ulkomaisen toiminnan aloituspäivä | — | — | RE |
| `ALVVelvUlkomLopPvm` | ALV-velvollisen ulkomaisen toiminnan lopetuspäivä | — | — | RE |
| `MuokALVVelv` | Muokattu liiketoiminnasta ALV-velvollisuus | — | vast_vaihtoehdo_70_2012_01_01 | luokitus, RE |
| `MuokTyonant` | Muokattu työnantajuus (TA-rooli) | — | vast_vaihtoehdo_70_2012_01_01 | RE, luokitus |
| `MuokEnnakonperYks` | Muokattu ennakkoperintärekisteriin kuuluminen (EPR-rooli) | — | vast_vaihtoehdo_70_2012_01_01 | luokitus, RE |
| `MuokAlkutuott` | Muokattu alkutuottajuudesta / taide-esineen tekijänä ALV-velvollisuus | — | vast_vaihtoehdo_70_2012_01_01 | RE, luokitus |
| `oikMuotoLahde` | Oikeudellisen (juridisen) muodon saantilähde | — | — | luokitus, RE |
| `omtyyppiLahde` | Omistajatyypin saantilähde | — | — | RE, luokitus |
| `sektoriluokkaLahde` | Sektoriluokan saantilähde | — | — | RE, luokitus |
| `ToiminnallisuudenTilaLahde` | Toiminnallisuuden tilan saantilähde | — | — | luokitus, RE |
| `tol2008Lahde` | Toimialatiedon (TOL 2008) saantilähde | — | — | RE, luokitus |
| `verohTol2008Lahde` | Verohallinnon (oman) toimialatiedon (TOL 2008) saantilähde | — | — | luokitus, RE |
| `kotikuntaLahde` | Kotikuntatiedon saantilähde | — | — | RE, luokitus |
| `paaOikYks` | Pää-(asiallinen) oikeudellinen yksikkö ao. yrityksessä (yritysyksikössä) | — | vast_vaihtoehdo_69_2012_01_01 | RE, luokitus |
| `MuokPorotVelv` | Muokattu ALV-velvollisuus porotaloudesta | — | vast_vaihtoehdo_70_2012_01_01 | luokitus, RE |
| `muokKiintVuokrVelv` | Muokattu ALV-velvollisuus kiinteistöjen vuokrauksesta | — | vast_vaihtoehdo_70_2012_01_01 | RE, luokitus |
| `MuokUlkomVelv` | Muokattu ALV-velvollisuus ulkomaisesta toiminnasta | — | vast_vaihtoehdo_70_2012_01_01 | luokitus, RE |
| `TyonantajaRekAlPvm` | Työnantajarekisteröinnin alkupvm | — | — | RE |
| `TyoLopPvm` | Työnantajarekisteröinnin loppupvm | — | — | RE |
| `ToimLopMuoto` | Oikeudellisen yksikön toiminnan lopetusmuoto | — | yrlopmuot_2_2012_01_01 | re, luokitus |
| `ALVVelvOmaAlPvm` | Ostajana tai omasta käytöstä ALV-velvollinen -kauden alkupvm | — | — | re |
| `ALVVelvOmaLopPvm` | Ostajana tai omasta käytöstä ALV-velvollinen -kauden loppupvm | — | — | re |
| `KuntaAlPvm` | Oikeudellisen yksikön kotikunnan alku-/muutospvm | — | — | RE |
| `oikMuotoAlPvm` | Oikeudellisen yksikön oikeudellisen muodon alku-/muutospvm | — | — | RE |
| `tol2008AlPvm` | Oikeudellisen yksikön toimialakoodin (TOL 2008) alku-/muutospvm | — | — | RE |
| `VerohTol2008AlPvm` | Oikeudellisen yksikön verohallinnon käyttämän ja sieltä suoraan saadun toimialakoodin (TOL 2008)  alku-/muutospvm | — | — | RE |
| `omtyyppiAlPvm` | Oikeudellisen yksikön omistajatyyppikoodin alku-/muutospvm | — | — | RE |
| `toimTilaAlPvm` | Oikeudellisen yksikön toiminnallisuuden tila -koodin alku-/muutospvm | — | — | RE |
| `julkisyhtTyyppiAlPvm` | Oikeudellisen yksikön julkisyhteisötyyppi -koodin alku-/muutospvm | — | — | RE |
| `ALVVelvEsiintymispalkkioAlPvm` | ALV-velvollinen esiintymispalkkioista, aloituspäivä | — | — | — |
| `ALVVelvEsiintymispalkkioLopPvm` | ALV-velvollinen esiintymispalkkioista, lopetuspäivä | — | — | — |
| `shnro_toissijtunnus` | Oikeudellisen yksikön toissijainen tunnus | — | — | tunnus, re |

### Variable definitions

#### `yrtun_s` — Suojattu yrityksen (oikeudellisen yksikön) Y-tunnus.

Yrityksen (oikeudellisen yksikön) tunnisteena on yleisesti eri viranomais- ja muissa järjestelmissä käytössä oleva Y-tunnus (yritys- ja yhteisötunnus, ks. www.ytj.fi). Y-tunnus on muotoa nnnnnnn-t, missä t on tarkistenumero.
  
Y-tunnus korvasi kaupparekisterinumeron Yritys- ja yhteisötietojärjestelmän (YTJ) alusta eli hetkestä 1.4.2001 lähtien. Y-tunnus on korvannut myös mm. säätiö- ja yhdistysrekisterinumerot. Y-tunnuksen aikaisempi nimi oli Liike- ja yhteisötunnus eli ly-tunnus.

Valtion virastoillakin on nykyään päätunnuksina Y-tunnukset, ei enää valtion virastotunnukset.

#### `yritysID_s` — Suojattu yritys-ID, yrityksen tunnus

Yritys-ID, yrityksen tunnus, generoitu / annettu Tilastokeskuksessa; eri kuin oikeudellisen yksikön Y-tunnus.

Yritysyksikkö vastaa pienintä oikeudellisten yksiköiden ryhmää, joka muodostaa päätöksenteossaan itsenäisen tuotantoyksikön. Sillä on kaikki tarvittavat tuotannontekijät, se myy tuotteita markkinoille ja sitä johdetaan kokonaisuutena.

Tilastokeskus muodostaa yritysyksikön samaan konserniin kuuluvista Suomessa sijaitsevista yhtiöistä. Konsernin oikeudellisista yksiköistä (y-tunnus) voidaan muodostaa yksi tai useampia yritysyksiköitä. Konserneihin kuulumattomilla yrityksillä yritysyksikkö vastaa aina oikeudellista yksikköä.

Pääsääntöisesti valmisaineistot ovat oikeudellisen yksikön tasolla eli yhdistävänä tunnuksena on syrtun, ei syritysID.

#### `konserniID_s` — Suojattu konsernitunnus

Konsernitunnus, 1-alkuinen 7-mittainen konsernin yksilöintitunnus, joka on muotoa nnnnnnn. Konsernitunnus voidaan antaa kaikille Suomessa rekisteröidyille pääkonserneille. Saantilähde: Konsernitunnus generoidaan yritysrekisterissä.

#### `virastotunnus_s` — Suojattu valtion virastotunnus

Valtion virastotunnus. Annetaan Valtiokonttorissa. 7-mittainen, muotoa nnnnnnt, missa nnnnnn on juokseva numero ja t tarkistemerkki. Oikeudellisella yksiköllä on virastotunnus vain silloin, jos oikeudellisen yksikön alla on *** yksi *** virasto. (Oikeudellisen yksikön alla voi olla jopa lähes 100 virastoa.)

#### `AlPvm` — Oikeudellisen yksikön aloituspvm

**Group:** RE

Oikeudellisen yksikön aloituspäivä. Pääsääntöisesti tämä on verohallintoon tai kaupparekisteriin merkitsemispäivä tai luonnollisella henkilöllä Y-tunnuksen alkamis-/antopäivä. Tietoa johdetaan myös joidenkin ominaisuustietojen alkupäivien avulla ja lisäksi käytössä on puuttuvia ja virheellisiä tietoja korvaavia keinotekoisia päivämääriä (erityisesti vanhemmilla yksiköillä). 

Tätä tietoa johdetaan seuraavien ominaisuustietojen alkupäivien avulla:
- työnantajarekisteri (säännöllinen työnantajuus)
- laivaisännyystyönantajuus
- ennakkoperintärekisteri
- arvonlisäverovelvollisuus
- vakuutusmaksuverovelvollisuus
- alv-vastuuryhmän jäsenyys
- elinkeinotoiminta (vain luonnollisella henkilöllä)
- sijaintiosoite (ei luonnollisella henkilöllä)
- toimiala (ei luonnollisella henkilöllä)
- virallinen nimi (ei luonnollisella henkilöllä)
- toiminimi (ei luonnollisella henkilöllä)
- postiosoite (ei luonnollisella henkilöllä)
- kotikunta (ei luonnollisella henkilöllä)
- oikeudellinen muoto (ei luonnollisella henkilöllä)
- varhaisin tilikausi.
   
Puutteellisten ja virheellisten tietojen lisäksi sisältää runsaasti - erityisesti vanhemmilla yksiköillä - seuraavia keinotekoisia päivämääriä:
- 1.1.1900
- 1.1.1901
- 15.3.1978.

#### `LopPvm` — Oikeudellisen yksikön hallinnollinen lopetuspvm

**Group:** RE

Oikeudellisen yksikön lopetuspäivä (= lopetusajankohta verohallinnon asiakastietokannassa) tai sen Y-tunnuksen lopetuspvm.

#### `toimAlPvm` — Oikeudellisen yksikön taloudellisen toiminnan aloituspvm

**Group:** RE

Oikeudellisen yksikön taloudellisen toiminnan aloituspäivämäärä. Käytännössä sen tilikauden alkupäivä, jolloin yksikön toiminnallisuus havaitaan. Vanhimmilla yksiköillä toiminnan aloituspäivämäärä on varhaisin pvm seuraavista:
- alv-velvollisuuden alkupäivämäärä
- vakuutusmaksuvelvollisuuden alkupäivämäärä
- alv-vastuuryhmän jäsenyyden alkupäivämäärä
- työnantajana toimimisen alkupäivämäärä (säännöllinen työnantajuus)
- laivaisännyystyönantajana toimimisen alkupäivämäärä
- ennakkoverovelvollisuuden alkupäivämäärä.

Toiminnan aloittamiset kasaantuvat tammikuulle, koska aloittaneilla yrityksillä oma-aloitteisten verojen vuosi-ilmoitusten tiedot jaetaan koko vuodelle. Sitä vastoin, mikäli yritys on lopettanut kesken vuoden, oav:n vuosi-ilmoitustiedot jaetaan kuukausille vain lopetusajankohtaan asti.

#### `toimLopPvm` — Oikeudellisen yksikön taloudellisen toiminnan lopetuspvm

**Group:** RE

Oikeudellisen yksikön taloudellisen toiminnan loppumispäivämäärä. Käytännössä sen tilikauden loppupäivä, jolloin toiminnallisuuden lopetus havaitaan. Lisäksi päivitetään aina, kun saadaan tieto Y-tunnuksen lopettamisesta.

Tietoa päätellään tilastoaineistojen, tiedusteluiden tietojen tai yrityksen yhteydenottojen kautta. Joissakin tapauksissa yritys voi jatkaa parin vuoden päästä uudelleen toimintaa, jolloin yksikkö aktivoidaan, jos tieto toiminnan jatkamisesta saadaan jostakin lähteestä (esim. alv- tai työnantajarekisteri, elinkeinoverorekisiteri, tulorekisteri tai maatalouden tilinpäätösaineisto).

Hallinnollisen lopetuksen käyttö (LopPvm) on yleistymässä tilastoissa, koska uudelleenaktivointi tuottaa työtä eikä toiminnan lopetuksia tehdä massana. Toiminnan lopetusten päättelyä tehdään pidemmällä viiveellä kuin aloitusten päättelyä.

#### `VerohOikMuoto` — Oikeudellinen muoto (Verohallinto)

**Classification:** verohoikmuot_2_2012_01_01 · **Group:** luokitus, RE

Oikeudellisen yksikön oikeudellinen muoto eli yksikön oikeudellisen aseman verotuksessa ilmaiseva koodi. 

Luokitus:
	01	Luonnollinen henkilö	
	10	Avoin yhtiö	
	11	Kommandiittiyhtiö	
	12	Osakeyhtiö	
	13	Asunto-osakeyhtiö	
	14	Laivanisännistöyhtiö	
	16	Keskinäinen kiinteistö-oy	
	17	Muu kiinteistö-oy	
	18	Konserni	
	19	Muu yhtiö	
	20	Aatteellinen yhdistys	
	21	Erityislainsäädäntöön perustuva yhdistys	
	22	Keskinäinen vahinkovakuutusyhdistys	
	23	Metsänhoitoyhdistys	
	24	Osuuspankki	
	25	Osuuskunta	
	26	Vakuutuskassa	
	27	Työttömyyskassa	
	28	Muu taloudellinen yhdistys	
	29	Muu yhdistys	
	30	Säätiö (säätiölain mukainen)	
	31	Säästöpankki	
	32	Eläkesäätiö (säädekirjalla perustettu)	
	33	Työeläkekassa	
	35	Hypoteekkiyhdistys	
	39	Muu säätiö	
	40	Valtio ja sen laitokset	
	60	Valtion liikelaitos	
	41	Kunta	
	61	Kunnallinen liikelaitos	
	42	Kuntayhtymä	
	62	Kuntainliiton (kuntayhtymän) liikelaitos	
	43	Ahvenanmaan maakunta ja sen virastot	
	63	Ahvenanmaan liikelaitos	
	44	Evankelis-luterilainen kirkko	
	45	Ortodoksinen kirkko	
	46	Rekisteröity uskonnollinen yhdyskunta	
	47	Ylioppilaskunta tai osakunta	
	48	Erillishallinnollinen valtion laitos	
	49	Muu julkisoikeudellinen oikeushenkilö	
	50	Yhteisetuudet (esim. kalastuskunta)	
	51	Verotusyhtymät	
	52	Yhteisvastuullinen pidätysvelvollinen	
	53	Kuolinpesä	
	54	Konkurssipesä	
	55	Yhteismetsä	
	57	Elinkeinoyhtymä	
	59	Muu verotuksen yksikkö	
	70	Ulkomainen yhteisö	
	71	Ulkomaisen yhteisön sivuliike Suomessa	
	91	Muut	
	92	Muut	
	93	Muut	
	94	Muut	
	95	Muut	
	96	Muut	
	99	Muut	
	ZZ	Tieto puuttuu

#### `VerohOikAlPvm` — Verohallinnon oikeudellisen muodon alkupvm

**Group:** RE

Verohallinnon oikeudellisen muodon alkupvm

#### `Eurooppayhtio` — Tieto siitä, onko oikeudellinen yksikkö eurooppayhtiö

**Classification:** vast_vaihtoehdo_69_2012_01_01 · **Group:** RE, luokitus

Tieto siitä, onko oikeudellinen yksikkö eurooppayhtiö. 
Mahdolliset arvot ovat: 0 = ei, 1 = kyllä

#### `Kuntayhtyma` — Tieto siitä, onko oikeudellinen yksikkö kuntayhtymä.

**Classification:** vast_vaihtoehdo_69_2012_01_01 · **Group:** johdettu, luokitus, RE

Tieto siitä, onko oikeudellinen yksikkö kuntayhtymä. Mahdolliset arvot: 0 = Ei, 1 = Kyllä
 


Päätellään oletusarvona ASITK:n oikeudellisen muodon koodista. Jos oikeudellinen muoto syötteessä on 
42 (kuntayhtymä), 
62 (kuntayhtymän liikelaitos), 
43 (Ahvenanmaan maakunta ja sen virasto) tai 
63 (Ahvenanmaan liikelaitos), 
päivitetään Kuntayhtyma = 1, muutoin Kuntayhtyma = 0.

#### `Ohi` — Julkisyhteisöjen ohitustieto

**Classification:** vast_vaihtoehdo_69_2012_01_01 · **Group:** RE, luokitus, johdettu

Julkisyhteisöjen ohitustieto. Saa arvon 1, mikäli johdettu omistajatyyppi on kunta, valtio tai Ahvenanmaan maakunta. Julkisyhteisöt tunnistaa myös seuraavia tapoja noudattaen (nämä kaikki koskevat oikeudellista yksikköä, yritystä ja toimipaikkaa):
 
- Sektoriluokka = 13 Julkisyhteisöt
- Julkisyhteisötyyppi ei ole 00 tai ZZ Ei julkisyhteisö

#### `JulkisyhtTyyppi` — Julkisyhteisötyyppi oikeudellisella yksiköllä

**Classification:** jlkyhttyyp_2_2012_01_01 · **Group:** RE, luokitus

Julkisyhteisötyyppi oikeudellisella yksiköllä. Julkisyhteisötyypit ovat:

SSS	Yhteensä	
00	Ei julkisyhteisö	
11	Valtion virasto	
12	Valtion liikelaitos	
13	Valtion liikelaitos, y-tunnus	
14	Kunta	
15	Kuntayhtymä	
16	Kunnan tai kuntayhtymän liikelaitos	
17	Yliopisto, y-tunnus	
18	Ahvenanmaan maakuntahallitus	
19	PLM-virasto	
20	Sosiaaliturvarahasto	
99	Muu julkisyhteisö	
X	Tieto puuttuu

Tieto lisätty 25.1.2016.

#### `Kieli` — Oikeudellisen yksikön asiointikieli YTY:ssä, verohallinnon mukaan.

**Classification:** kieli_22_2012_01_01 · **Group:** luokitus, RE

Oikeudellisen yksikön asiointikieli YTY:ssä, verohallinnon mukaan. 0=Suomi, 1=Ruotsi.

#### `UlkomVuokratyonantaja` — Koodi ulkomaalaisten vuokratyönantajana toimimisesta

**Classification:** vast_vaihtoehdo_69_2012_01_01 · **Group:** RE, luokitus

Koodi ulkomaalaisten vuokratyönantajana toimimisesta. Sallitut arvot:
1 = kyllä,
0 = ei

#### `Kansalaisuus` — Kansalaisuuden maatunnus

**Classification:** valtio_2_2012_01_01 · **Group:** luokitus, RE

Kansalaisuuden maatunnus, luokitus: Valtiot ja maat -luokitus, jossa on yhtenä koodivaihtoehtona 2-kirjaimiset koodit.

#### `YleishYhteiso` — Koodi yleishyödyllisestä yhteisöstä, verotuksessa

**Classification:** vast_vaihtoehdo_69_2012_01_01 · **Group:** RE, luokitus

Koodi yleishyödyllisestä yhteisöstä, verotuksessa. Sallitut arvot:
1 = kyllä,
0 = ei

#### `YleishAlPvm` — Yleishyödyllisenä yhteisönä aloituspvm

**Group:** RE

Yleishyödyllisenä yhteisönä aloituspvm

#### `TotaalToimAlPvm` — Oikeudellisen yksikön totaalisen toiminnan alkupvm verohallinnossa

**Group:** RE

Oikeudellisen yksikön totaalisen toiminnan alkupvm verohallinnossa

#### `LisPvm` — Oikeudellisen yksikön lisäyspvm yritysrekisteriin / YTY-tuotantokantaan

**Group:** RE

Päivämäärä, jolloin oikeudellinen yksikkö on lisätty verohallinnon asiakastietokannasta (ASITK) yritysrekisteriin / YTY-tuotantokantaan.  Asiakastietokannan päivityspäivämäärä (kuukausittain, aiemmin 1/4-vuosittain). 
  
Käsittely: Ei päivitetä vanhoille oikeudellisille yksiköille.

#### `tilaPerus` — Perustietojen tila oikeudellisella yksiköllä

**Classification:** perustiettila_2_2012_01_01 · **Group:** RE, johdettu, aputiedot_tekniset

Perustietojen tila oikeudellisella yksiköllä: Järjestelmän käyttämä tieto yksikön perustietojen käsittelyn tilasta. Perustiedot sisältävät mm. yksikön toimialan, toiminnan tilan ja osoitetietoja.

0	Tarkistamaton	
1	Virheetön	
2	Virheellinen	
3	Keskeneräinen	
4	Hyväksytty	
5	Pakkohyväksytty	
6	Massakorjattu	
7	Uusi oikeudellinen yksikkö, tietoja ei ole tarkistettu	
8	Tarkistamattomana autom. hyväksytty

#### `oikMuoto` — Oikeudellisen yksikön oikeudellinen (juridinen) muoto yritysrekisterissä

**Classification:** oikeudell_muoto_1_1984_01_01 · **Group:** luokitus, RE

Oikeudellisen yksikön oikeudellinen (juridinen) muoto yritysrekisterissä. Verohallinnon oikeudellinen muoto muunnettu koneellisesti vastaamaan yritysrekisterissä käytettyä luokitusta.

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
34	Eläkesäätiö, vakuutuskassa, työttömyyskassa	
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

#### `omtyyppi` — Omistajatyyppi oikeudellisella yksiköllä

**Classification:** omistajatyyppi_1_1995_01_01 · **Group:** RE, luokitus

Omistajatyyppi oikeudellisella yksiköllä. Johdetaan / muokataan oikeudellisesta muodosta. 

1	Yksityinen kotimainen	
2	Valtio	
3	Kunta	
4	Ahvenanmaan maakunta	
5	Ulkomaalaisomisteinen	
6	Muu omistajatyyppi

#### `sektoriluokka` — Oikeudellisen yksikön sektoriluokka

**Classification:** sektoriluokitus_11_2013_01_01 · **Group:** luokitus, RE

Oikeudellisen yksikön sektoriluokka. Luokitus, jossa yksiköt jaetaan omistajuuden, toiminnan tarkoituksen ja rahoitustavan perusteella eri sektoreihin.

1	Koko kansantalous	
11	Yritykset	
111	Yritykset pl. asuntoyhteisöt	
11101	Julkiset yritykset pl. asuntoyhteisöt	
11102	Yksityiset kotimaiset yritykset  pl. asuntoyhteisöt	
11103	Ulkomaisomisteiset yritykset  pl. asuntoyhteisöt	
112	Asuntoyhteisöt	
1121	Asunto-osakeyhtiöt	
11211	Asunto-osakeyhtiöt, julkiset	
11212	Asunto-osakeyhtiöt, yksityiset kotimaiset	
11213	Asunto-osakeyhtiöt, ulkomaisomisteiset	
1122	Muut asuntoyhteisöt	
11221	Muut asuntoyhteisöt, julkiset	
11222	Muut asuntoyhteisöt, yksityiset kotimaiset	
11223	Muut asuntoyhteisöt, ulkomaisomisteiset	
12	Rahoitus- ja vakuutuslaitokset	
121-123	Rahalaitokset	
121	Keskuspankki	
122	Muut rahalaitokset	
1221	Talletuspankit	
12211	Talletuspankit, julkiset	
12212	Talletuspankit, yksityiset kotimaiset	
12213	Talletuspankit, ulkomaisomisteiset	
1222	Muut luottolaitokset	
12221	Muut luottolaitokset, julkiset	
12222	Muut luottolaitokset, yksityiset kotimaiset	
12223	Muut luottolaitokset, ulkomaisomisteiset	
1223	Muut rahalaitokset kuin luottolaitokset	
12231	Muut rahalaitokset kuin luottolaitokset, julkiset	
12232	Muut rahalaitokset kuin luottolaitokset, yksityiset kotimaiset	
12233	Muut rahalaitokset kuin luottolaitokset, ulkomaisomisteiset	
123	Rahamarkkinarahastot	
124-127	Muut rahoituslaitokset	
124	Yhteissijoitusyritykset pl. rahamarkkinarahastot	
1241	Sijoitusrahastot (UCITS)	
1242	Muut yhteissijoitusyritykset	
125	Muut rahoituksen välittäjät	
12501	Muut rahoituksen välittäjät, julkiset	
12502	Muut rahoituksen välittäjät, yksityiset kotimaiset	
12503	Muut rahoituksen välittäjät, ulkomaisomisteiset	
126	Rahoituksen ja vakuutuksen välitystä avustavat laitokset	
12601	Rahoituksen ja vakuutuksen välitystä avustavat laitokset, julkiset	
12602	Rahoituksen ja vakuutuksen välitystä avustavat laitokset, yksityiset kotimaiset	
12603	Rahoituksen ja vakuutuksen välitystä avustavat laitokset, ulkomaisomisteiset	
127	Konserninsisäiset rahoitusyksiköt ja rahanlainaajat	
12701	Konserninsisäiset rahoitusyksiköt ja rahanlainaajat, julkiset	
12702	Konserninsisäiset rahoitusyksiköt ja rahanlainaajat, yksityiset kotimaiset	
12703	Konserninsisäiset rahoitusyksiköt ja rahanlainaajat, ulkomaisomisteiset	
128-129	Vakuutuslaitokset ja eläkerahastot	
128	Vakuutuslaitokset	
12801	Vakuutuslaitokset, julkiset	
12802	Vakuutuslaitokset, yksityiset kotimaiset	
12803	Vakuutuslaitokset, ulkomaisomisteiset	
129	Eläkerahastot	
13	Julkisyhteisöt	
1311	Valtionhallinto	
13111	Valtion budjettitalous	
13119	Muut valtionhallinnon yksiköt	
1312	Osavaltiohallinto (ei käytössä Suomessa)	
1313	Paikallishallinto	
13131	Kunnat	
13132	Kuntayhtymät	
13133	Ahvenanmaan maakunnan hallitus	
13139	Muut paikallishallinnon yksiköt	
1314	Sosiaaliturvarahastot	
13141	Työeläkelaitokset	
13149	Muut sosiaaliturvarahastot	
14	Kotitaloudet	
141	Työnantaja- ja muut elinkeinonharjoittajien kotitaloudet	
143	Palkansaajakotitaloudet	
144	Omaisuustulojen ja tulonsiirtojen saajakotitaloudet	
1441	Omaisuustulojen saajakotitaloudet	
1442	Eläkkeensaajakotitaloudet	
1443	Muiden tulonsiirtojen saajakotitaloudet	
15	Kotitalouksia palvelevat voittoa tavoittelemattomat yhteisöt	
2	Ulkomaat	
21	Euroopan unionin jäsenvaltiot ja toimielimet	
211	Euroopan unionin jäsenvaltiot	
2111	Euroalueen jäsenvaltiot	
2112	Euroalueen ulkopuoliset jäsenvaltiot	
212	Euroopan unionin toimielimet	
2121	Euroopan keskuspankki (EKP)	
2122	Euroopan unionin toimielimet pl. EKP	
22	Euroopan unionin ulkopuoliset valtiot ja kansainväliset järjestöt

#### `sektoriAlPvm` — Sektoriluokan muutos-/alkupäivämäärä

**Group:** RE

Sektoriluokan muutos-/alkupäivämäärä

#### `toiminnallisuudenTila` — Oikeudellisen yksikön toiminnallisuuden tila

**Classification:** toimtila_2_2012_01_01 · **Group:** luokitus, RE

Oikeudellisen yksikön toiminnallisuuden tila

0	Passiivinen	
1	Aktiivinen	
2	Toiminta keskeytynyt	
3	Ehdolla aktivointiin	
4	Ehdolla lopetettavaksi

#### `tol2008` — Toimiala (TOL2008)

**Classification:** toimiala_1_2008_01_01 · **Group:** luokitus, RE

Toimialaluokitus TOL 2008:n mukainen toimialakoodi, joka määräytyy oikeudellisen yksikön toiminnan perusteella. Monitoimipaikkaisella oikeudellisella yksiköllä koodi ilmaisee yksikön päätoimialaa, joka määräytyy ohjelmallisesti toimipaikkojen toimiala- ym. tiedoista.

Verohallinon VerohTol2008-tieto saattaa erota yritysrekisterin tol2008-tiedosta. Esim. monitoimipaikkaisilla tol2008 on laskettu toimipaikoilta henkilötyövuosien ja toimialoitteisen arvonlisäkertoimen perusteella. Ensisijaisesti käytetään tol2008-tietoa.

VerohTol2008-muuttujaan mahdolliset muutokset tulevat kuukausittain Verohallinnon ASITK-päivityksen myötä ja yksitoimipaikkaisilla 
tieto viedään myös tol2008-muuttujaan. Yksitoimipaikkaisilla tiedot ovat yleensä yhteneväiset. Muutoksia voi tulla myös yritysrekisterin omien tiedustelujen kautta.
 
Monitoimipaikkaisilla päätoimiala päätellään useamman kerran vuodessa, mutta muutoksia tulee vain kerran sen mukaan, onko toimipaikan toimiala muuttunut tiedustelun perusteella. Jonkin verran myös käsin muutetaan tietoa jonkin saantilähteen perusteella, esim. nettisivut, muut tilastot.

Toimialamuutosten ajantasaisuus ja laatu riippuu myös siitä ilmoittavatko yritykset toimialamuutoksen Verohallintoon tai PRH:een.

Julkisen sektorin toimijoille toimiala oikeudellisen yksikön tasolla on yleensä kuntataso, joka kuuluu julkiseen yleishallintoon. Toimipaikka/toimipistetietoa tarvitaan toimintojen eriyttämiseen.

#### `verohTol2008` — Verohallinnon antama toimialakoodi (TOL2008) oikeudelliselle yksikölle

**Classification:** toimiala_1_2008_01_01 · **Group:** luokitus, RE

Verohallinnon antama toimialakoodi (TOL2008) oikeudelliselle yksikölle

#### `kotikunta` — Oikeudellisen yksikön virallisen asuin-/kotikunnan kuntakoodi

**Group:** RE, luokitus

Oikeudellisen yksikön virallisen asuin-/kotikunnan kuntakoodi. (Asuinkunta voi olla myös ns. keinokunta, koodi 200.) Kunkin vuoden / hetken tilanne on omana kuntakoodistonaan TK:n luokituseditorissa.

#### `ALVVelvLiiketoimAlPvm` — ALV-velvollisen liiketoiminnan alkupvm

**Group:** RE

ALV-velvollisen liiketoiminnan alkupvm

#### `ALVVelvLiiketoimLopPvm` — ALV-velvollisen liiketoiminnan loppupvm

**Group:** RE

ALV-velvollisen liiketoiminnan loppupvm

#### `ALVVelvAlkutuotAlPvm` — ALV-velvollinen alkutuottajuudesta ja/tai taide-esineen tekijänä aloituspäivä

**Group:** RE

ALV-velvollinen alkutuottajuudesta ja/tai taide-esineen tekijänä aloituspäivä

#### `ALVVelvAlkutuotLopPvm` — ALV-velvollinen alkutuottajuudesta ja/tai taide-esineen tekijänä lopetuspäivä

**Group:** RE

ALV-velvollinen alkutuottajuudesta ja/tai taide-esineen tekijänä lopetuspäivä

#### `ALVVelvKiintVuokrAlPvm` — ALV-velvollinen kiinteistön käyttöoikeuden luovuttajana aloituspäivä

**Group:** RE

ALV-velvollinen kiinteistön käyttöoikeuden luovuttajana aloituspäivä

#### `ALVVelvKiintVuokrLopPvm` — ALV-velvollinen kiinteistön käyttöoikeuden luovuttajana lopetuspäivä

**Group:** RE

ALV-velvollinen kiinteistön käyttöoikeuden luovuttajana lopetuspäivä

#### `ALVVelvPorotalAlPvm` — ALV-velvollinen porotaloudesta aloituspäivä

**Group:** RE

ALV-velvollinen porotaloudesta aloituspäivä

#### `ALVVelvPorotalLopPvm` — ALV-velvollinen porotaloudesta lopetuspäivä

**Group:** RE

ALV-velvollinen porotaloudesta lopetuspäivä

#### `ALVVelvUlkomAlPvm` — ALV-velvollisen ulkomaisen toiminnan aloituspäivä

**Group:** RE

ALV-velvollisen ulkomaisen toiminnan aloituspäivä

#### `ALVVelvUlkomLopPvm` — ALV-velvollisen ulkomaisen toiminnan lopetuspäivä

**Group:** RE

ALV-velvollisen ulkomaisen toiminnan lopetuspäivä

#### `MuokALVVelv` — Muokattu liiketoiminnasta ALV-velvollisuus

**Classification:** vast_vaihtoehdo_70_2012_01_01 · **Group:** luokitus, RE

Indikaattorimuuttuja liiketoiminnasta arvonlisäverovelvollisuudelle
1	Kyllä	
2	Ei ole enää	
3	Ei ole koskaan ollut

#### `MuokTyonant` — Muokattu työnantajuus (TA-rooli)

**Classification:** vast_vaihtoehdo_70_2012_01_01 · **Group:** RE, luokitus

Indikaattorimuuttuja (säännölliselle) työnantajuudelle (ei koske satunnaista työnantajuutta)
1	Kyllä	
2	Ei ole enää	
3	Ei ole koskaan ollut

#### `MuokEnnakonperYks` — Muokattu ennakkoperintärekisteriin kuuluminen (EPR-rooli)

**Classification:** vast_vaihtoehdo_70_2012_01_01 · **Group:** luokitus, RE

Indikaattorimuuttuja ennakkoperintärekisteriin (EPR) kuulumiselle
1	Kyllä	
2	Ei ole enää	
3	Ei ole koskaan ollut

#### `MuokAlkutuott` — Muokattu alkutuottajuudesta / taide-esineen tekijänä ALV-velvollisuus

**Classification:** vast_vaihtoehdo_70_2012_01_01 · **Group:** RE, luokitus

Indikaattorimuuttuja alkutuottajuudelle / taide-esineen tekijyydelle (ALT-rooli)
1	Kyllä	
2	Ei ole enää	
3	Ei ole koskaan ollut

#### `oikMuotoLahde` — Oikeudellisen (juridisen) muodon saantilähde

**Group:** luokitus, RE

Oikeudellisen (juridisen) muodon saantilähde
  1 Suorat tiedonkeruut
  2 Tilastot
  3 Hallinnolliset aineistot
  4 Estimoinnit
  5 Muut muokkaukset
  9 Muut lähteet
  Z Tieto puuttuu

#### `omtyyppiLahde` — Omistajatyypin saantilähde

**Group:** RE, luokitus

Omistajatyypin saantilähde
  1 Suorat tiedonkeruut
  2 Tilastot
  3 Hallinnolliset aineistot
  4 Estimoinnit
  5 Muut muokkaukset
  9 Muut lähteet
  Z Tieto puuttuu

#### `sektoriluokkaLahde` — Sektoriluokan saantilähde

**Group:** RE, luokitus

Sektoriluokan saantilähde
  1 Suorat tiedonkeruut
  2 Tilastot
  3 Hallinnolliset aineistot
  4 Estimoinnit
  5 Muut muokkaukset
  9 Muut lähteet
  Z Tieto puuttuu

#### `ToiminnallisuudenTilaLahde` — Toiminnallisuuden tilan saantilähde

**Group:** luokitus, RE

Toiminnallisuuden tilan saantilähde
  1 Suorat tiedonkeruut
  2 Tilastot
  3 Hallinnolliset aineistot
  4 Estimoinnit
  5 Muut muokkaukset
  9 Muut lähteet
  Z Tieto puuttuu

#### `tol2008Lahde` — Toimialatiedon (TOL 2008) saantilähde

**Group:** RE, luokitus

Toimialatiedon (TOL 2008) saantilähde
  1 Suorat tiedonkeruut
  2 Tilastot
  3 Hallinnolliset aineistot
  4 Estimoinnit
  5 Muut muokkaukset
  9 Muut lähteet
  Z Tieto puuttuu

#### `verohTol2008Lahde` — Verohallinnon (oman) toimialatiedon (TOL 2008) saantilähde

**Group:** luokitus, RE

Verohallinnon (oman) toimialatiedon (TOL 2008) saantilähde
  1 Suorat tiedonkeruut
  2 Tilastot
  3 Hallinnolliset aineistot
  4 Estimoinnit
  5 Muut muokkaukset
  9 Muut lähteet
  Z Tieto puuttuu

#### `kotikuntaLahde` — Kotikuntatiedon saantilähde

**Group:** RE, luokitus

Kotikuntatiedon saantilähde
  1 Suorat tiedonkeruut
  2 Tilastot
  3 Hallinnolliset aineistot
  4 Estimoinnit
  5 Muut muokkaukset
  9 Muut lähteet
  Z Tieto puuttuu

#### `paaOikYks` — Pää-(asiallinen) oikeudellinen yksikkö ao. yrityksessä (yritysyksikössä)

**Classification:** vast_vaihtoehdo_69_2012_01_01 · **Group:** RE, luokitus

Pää-(asiallinen) oikeudellinen yksikkö ao. yrityksessä (yritysyksikössä), luokitus. Luokitus. Koodit: 1 = Kyllä, on pääasiallinen oikeudellinen yksikkö, 0 = Ei ole.

#### `MuokPorotVelv` — Muokattu ALV-velvollisuus porotaloudesta

**Classification:** vast_vaihtoehdo_70_2012_01_01 · **Group:** luokitus, RE

Indikaattorimuuttuja arvonlisäverovelvollisuudelle porotaloudesta
1	Kyllä	
2	Ei ole enää	
3	Ei ole koskaan ollut

#### `muokKiintVuokrVelv` — Muokattu ALV-velvollisuus kiinteistöjen vuokrauksesta

**Classification:** vast_vaihtoehdo_70_2012_01_01 · **Group:** RE, luokitus

Indikaattorimuuttuja arvonlisäverovelvollisuudelle kiinteistöjen vuokrauksesta 
1	Kyllä	
2	Ei ole enää	
3	Ei ole koskaan ollut

#### `MuokUlkomVelv` — Muokattu ALV-velvollisuus ulkomaisesta toiminnasta

**Classification:** vast_vaihtoehdo_70_2012_01_01 · **Group:** luokitus, RE

Indikaattorimuuttuja arvonlisäverovelvollisuudelle ulkomaisesta toiminnasta  
1	Kyllä	
2	Ei ole enää	
3	Ei ole koskaan ollut

#### `TyonantajaRekAlPvm` — Työnantajarekisteröinnin alkupvm

**Group:** RE

Työnantajarekisterin aloituspäivä (= säännöllisen työnantajuuden aloituspäivä).

#### `TyoLopPvm` — Työnantajarekisteröinnin loppupvm

**Group:** RE

Työnantajarekisterin lopetuspäivä (= säännöllisen työnantajuuden lopetuspäivä)

#### `ToimLopMuoto` — Oikeudellisen yksikön toiminnan lopetusmuoto

**Classification:** yrlopmuot_2_2012_01_01 · **Group:** re, luokitus

Oikeudellisen yksikön toiminnan lopetusmuoto
11	Kuoleminen	
12	Oikeudellisen muodon muutos	
13	Toiminnan siirtyminen	
14	Konkurssi	
15	Fuusio	
18	Jakautuminen	
21	Virheellinen aloitus	

Tieto lisätty 17.3.2014

#### `ALVVelvOmaAlPvm` — Ostajana tai omasta käytöstä ALV-velvollinen -kauden alkupvm

**Group:** re

Ostajana tai omasta käytöstä ALV-velvollinen -kauden alkupvm

Tieto lisätty 17.3.2014

#### `ALVVelvOmaLopPvm` — Ostajana tai omasta käytöstä ALV-velvollinen -kauden loppupvm

**Group:** re

Ostajana tai omasta käytöstä ALV-velvollinen -kauden loppupvm

Tieto lisätty 17.3.2014

#### `KuntaAlPvm` — Oikeudellisen yksikön kotikunnan alku-/muutospvm

**Group:** RE

Oikeudellisen yksikön kotikunnan alku-/muutospvm

#### `oikMuotoAlPvm` — Oikeudellisen yksikön oikeudellisen muodon alku-/muutospvm

**Group:** RE

Oikeudellisen yksikön oikeudellisen muodon alku-/muutospvm

#### `tol2008AlPvm` — Oikeudellisen yksikön toimialakoodin (TOL 2008) alku-/muutospvm

**Group:** RE

Oikeudellisen yksikön toimialakoodin (TOL 2008) alku-/muutospvm

#### `VerohTol2008AlPvm` — Oikeudellisen yksikön verohallinnon käyttämän ja sieltä suoraan saadun toimialakoodin (TOL 2008)  alku-/muutospvm

**Group:** RE

Oikeudellisen yksikön verohallinnon käyttämän ja sieltä suoraan saadun toimialakoodin (TOL 2008)  alku-/muutospvm

#### `omtyyppiAlPvm` — Oikeudellisen yksikön omistajatyyppikoodin alku-/muutospvm

**Group:** RE

Oikeudellisen yksikön omistajatyyppikoodin alku-/muutospvm

#### `toimTilaAlPvm` — Oikeudellisen yksikön toiminnallisuuden tila -koodin alku-/muutospvm

**Group:** RE

Oikeudellisen yksikön toiminnallisuuden tila -koodin alku-/muutospvm

#### `julkisyhtTyyppiAlPvm` — Oikeudellisen yksikön julkisyhteisötyyppi -koodin alku-/muutospvm

**Group:** RE

Oikeudellisen yksikön julkisyhteisötyyppi -koodin alku-/muutospvm

Tieto lisätty 25.1.2016.

#### `ALVVelvEsiintymispalkkioAlPvm` — ALV-velvollinen esiintymispalkkioista, aloituspäivä

ALV-velvollinen esiintymispalkkioista, aloituspäivä

#### `ALVVelvEsiintymispalkkioLopPvm` — ALV-velvollinen esiintymispalkkioista, lopetuspäivä

ALV-velvollinen esiintymispalkkioista, lopetuspäivä

#### `shnro_toissijtunnus` — Oikeudellisen yksikön toissijainen tunnus

**Group:** tunnus, re

Oikeudellisen yksikön toissijainen tunnus: 
Henkilötunnuspohjaiset oikeudellisen yksikön (luonnollisten henkilöiden) tunnukset on viety toissijaisiksi tunnuksiksi. Näitä voidaan joskus hyödyntää toisten aineistojen linkittämisessä erityisesti yrittäjiin liittyen. Tunnus on muutettu Tilastokeskuksen suojatuksi henkilönumeroksi.

---

[← Back to catalogue](../../README.md)
