# FOLK_VAEN Väestön ennakkotiedot

- **Identifier:** `vamuu_202400_jua_000_000.xml`
- **DOI:** `vamuu_2015-03_2015-03-23_ain_0001`
- **Temporal coverage:** 2015-01-01 - 
- **Published:** 2026-03-23
- **Organisation:** Tilastokeskus
- **Variable count:** 25
- **Observation count:** —
- **Population:** Suomessa tapahtumahetkellä vakinaisesti asuva väestö
- **Source:** Väestön ennakkotilasto

## Kuvaus / Description

<b>Tiedote (03/2026):</b>

Väestön ennakkotietoihin voi tulla muutoksia vuoden 2026 alussa:
 https://dvv.fi/-/loppuvuodesta-2025-vakinainen-osoite-voi-olla-vain-yhdessa-maassa-12-000-henkilolla-osoite-seka-suomessa-etta-virossa
Tämä tarkoittaa käytännössä sitä, että Suomen ja Viron väestörekisterit keskustelee keskenään, esim. jos henkilö muuttaa Viroon, niin DVV:lle tulee tieto. Henkilö ei voi myöskään jatkossa asua samanaikaisesti Suomessa ja Virossa. Tämän myötä rekistereiden tietoja on korjattu, ja henkilö on voinut ilmoittaa tai hänelle on valittu viimeisin vakinainen osoite maiden väliltä.

Vaikutuksia:
- Etenkin väestön ennakkotietoihin pohjautuviin aineistoihin voi tulla muutoksia alkuvuoden 2026 aikana, kun henkilöiden tietoja on lähdetty korjaamaan helmi-maaliskuun aikana
- Ei ole vielä tarkkaa tietoa korjausten suuruusluokasta tai tietoa siitä, mihin asti korjaukset kestävät, mutta oletuksena on, että korjaus vaikuttaa ainakin ensimmäisen vuosineljänneksen osalta
- Positiivista: laatu paranee ja rekisterit ajantasaistuvat.

*********************************************************************************************
<h3>FOLK_VAEN- ja FOLK_VAEN_KANSA-valmisaineistot </h3>
Väestön ennakkotiedot-valmisaineistomoduuli sisältää kuukausittaisia ennakkotietoja väestön rakenteesta. Valmisaineisto palvelee tutkijoiden tarvetta saada mahdollisimman ajankohtaisia tietoja henkilöiden osalta, joilla on kotipaikka Suomessa. Aineistoa käytettäessä on kuitenkin syytä huomioida, että ennakkotiedot ovat alustavia, korjaamattomia tietoja. Joitain tietoja, esimerkiksi maahanmuuttamiseen liittyen, myöskin päivittyy aineistoon merkittävällä viiveellä. Huomioithan, että vain vuoden lopun väkilukuun perustuvat FOLK-moduulit sisältävät lopullista, korjattua ja tarkastettua väestödataa, eikä ennakkotietoja tulisi käyttää enää lopullisten tietojen valmistuttua.

Valmisaineisto päivitetään kerran kuussa, jolloin päivitetään takautuvasti myös sen hetkisen vuoden aiempien kuukausien tiedot. Tämä tehdään siitä syystä, että tiedot voivat revisoitua saman vuoden sisällä. Ennen revisioita tuotettuja kuukausitietoja ei säilytetä Fionassa uuden päivityskerran jälkeen, joten huomioithan, että halutessasi säilyttää kyseiset tiedot hankkeesi käytössä, tulee sinun kopioida tiedot etäkäyttöjärjestelmässä hankkeesi W-levylle ennen päivitysajankohtaa. Kun joulukuun tilasto tuotetaan seuraavan vuoden tammi-helmikuussa (ja samalla vuoden aiempien kuukausien tiedot päivitetään), kyseisen tilastovuoden ennakkotilasto "jäätyy". Joulukuun osalta revisiota ei tapahdu lainkaan, koska se tuotetaan vain kerran (muiden kuukausien osalta revisiota tapahtuu, koska ne tuotetaan uudelleen).

Kaikki aineiston muuttujat ovat korjaamattomia eli ns. raakadataa. Esimerkiksi maahanmuuttoja sekä maastamuuttoja ja kuolemia jää puuttumaan loppuvuoden kuukausista. Ennakkotilaston tehtävä on kuvata "suuntaa" ja kehitystä, ja koska se tuotetaan nopeasti, loppuvuoden osalta tieto jää vajaaksi ja muutoinkin aineisto voi sisältää myös puuttuvaa tietoa ja virheellisiä arvoja. Väestöstä ei ole mahdollista tuottaa korjattua tilastoa kuukausittain. Lopullisissa tilastoissa tiedot ovat saatavilla (esimerkiksi muuttoliikkeen vuositilasto julkistetaan yleensä toukokuun lopussa). 


Esimerkiksi huhtikuun 2023 väkiluku: 

4/2023: 5571439 (1. julkistus toukokuussa 2023) 
 4/2023: 5572700 (viimeinen julkistus tammikuussa 2024) 

Ennakko vs lopullinen 2023 (koko vuosi): 

Maahanmuutot ennakko 71 918 --> lopullinen 73 236 
Maastamuutot  ennakko 13 422 --> lopullinen 15 322 

Sama revisioituminen koskettaa myös kuntien välisiä muuttoja eli Suomen sisällä tapahtuvia muuttoja. Etenkin kesällä muuttojen osalta revisioituminen on suurempaa.  

Elokuun maahan- ja kuntienväliset muutot 2023: 

Maahanmuutot 6929 (1. julkistus syyskuussa 2023) 
 Maahanmuutot 10457 (viimeinen julkistus tammikuussa 2024) 

Kuntien väliset muutot 35972 (1. julkistus syyskuussa 2023) 
 Kuntien väliset muutot 41008 (viimeinen julkistus tammikuussa 2024) 

Asuntoväestöön kuuluvat DVV:n väestötietojärjestelmän mukaan vuoden lopussa varsinaisissa asunnoissa vakinaisesti asuvat henkilöt. Jotta henkilö kuuluu asuntoväestöön, hänellä tulee olla vakinainen osoite, joista saadaan rakennusnumero-, rakennustunnus- ja huoneistotunnustiedot. Huomioithan myös, että mikäli henkilö asuu Suomessa alle vuoden, hän ei saa kotikuntaa, eikä tällöin tule osaksi väestöä. Mikäli tilapäisesti Suomessa oleskeleva henkilö on saanut tilapäisen asuinkunnan, on kuntakoodi 198. Mikäli ei ole tietoa siitä, missä kunnassa henkilö asuu, hänestä ei ole myöskään muun muassa rakennusnumero-, rakennustunnus-, huoneistotunnus- tai vastaavia tietoja. Tilapäisen kunnan (198) osalta myös muut tiedot ovat laadultaan erityisen heikkoja. Mikäli henkilö ei ole ilmoittanut tilapäiselle asumiselle päättymispäivää, tilapäinen asuminen näkyy aineistoissa jatkuvana, vaikka asuminen Suomessa olisi todellisuudessa jo päättynyt. 

Muun muassa laitoksissa vakinaisesti kirjoilla olevat, asuntoloissa ja ulkomailla asuvat sekä asunnottomat henkilöt eivät kuulu asuntoväestöön. Olemme säilyttäneet laitoskoodin eli olinpaikka-koodin saaneet (900-ryhmään kuuluvat) tässä aineistossa. Huomaathan, että olinpaikka-ryhmäläiset eivät kuitenkaan sisälly asuntoväestöön. 900-ryhmä sisältää esimerkiksi henkilöitä, jotka asuvat sellaisessa rakennuksessa, jota ei ole hyväksytty vakinaiseksi asunnoksi. Olinpaikka-muuttuja on karkeistettu yhdistämällä sen luokat yhdeksi (vastaten 900 = Asuntoväestön ulkopuoliset), jolloin mistä tahansa syystä asuinväestön ulkopuoliset saavat kaikki arvon 1. Tähän ryhmään kuuluu vailla vakinaista asuntoa, laitoksessa, tietymättömissä, lähetystöissä maailmalla, tilapäisesti ulkomailla, laivanpäällystössä, rangaistuslaitoksissa, hoitolaitoksissa, opiskelun takia poissa, sairaana muualla kuin hoitolaitoksessa, Eduskunnassa, lyhytaikaisen työn takia poissa ja satunnaisesti poissa kotipaikkakunnalta olevat ja asevelvolliset. Näillä laitoskoodin saaneilla ei myöskään ole rakennustunnus-, huoneistotunnus- ja rakennusnumerotietoja, mutta heistä voi olla saatavilla kuntatieto. Mikäli olinpaikka-muuttuja on tyhjä, henkilö ei ole saanut laitoskoodia ja tällöin hän kuuluu asuntoväestöön. Vaikka olinpaikka 900-ryhmäläiset eivät ole asuntoväestöä, osa olinpaikka 900-ryhmäläisistä voi kuulua perheiden perusväestöön, sillä tämä poikkeaa asuntoväestöstä siten, että siihen lasketaan kuuluvaksi myös asuntoloissa asuvat. 

Kuukausittain tilastovuoden osalta päivittyvän ennakkotietoaineiston lisäksi olemme tuottaneet myös aiempien tilastovuosien ennakkotiedot saataville vuosilta 2015-2023 osana FOLK_VAEN-moduulia. Huomioithan, että vanhoissa vuositauluiksi koostetuissa väestön ennakkotiedoissa vuosilta 2015, 2016, 2017, 2018 ja 2019 ei ole saatavilla seuraavia muuttujia: kansa2, a3lapluka, a7lapluka, a13lapluka, a18lapluka, a3laplubio, a7laplubio, a13laplubio, a18laplubio. 

<b>Karkeistetut muuttujatiedot: </b>
Valmisaineistomoduulissa FOLK_VAEN ei ole lähtökohtaisesti saatavilla arkaluonteisia ja karkeistamattomia muuttujia, sillä näihin annetaan käyttöoikeus vain, jos niihin on tutkimuksellisesta syystä erityinen tarve. Moduulissa on karkeistettu kansalaisuustiedot luokkiin suomi, muu eurooppa ja muu. 
 
Tästä valmisaineistomoduulista on mahdollista kuitenkin hakea karkeistamatonta versiota. Tämä löytyy lupapalvelusta nimellä FOLK_VAEN_KANSA. FOLK_VAEN_KANSA sisältää muuten samat muuttujat kuin FOLK_VAEN, mutta kansalaisuustiedot ovat karkeistamattomat. Tietojen käyttöön saaminen edellyttää vahvoja perusteita. 

Ohessa on lyhyesti kuvattu tähän aineistoon sisällytetyt muuttujat luokituksineen. Lisätietoa tilastosta: https://stat.fi/tilasto/vamuu ja vaesto.tilasto@stat.fi  

Lisätietoja valmisaineistosta Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@tilastokeskus.fi.

## Muuttujat / Variables (25)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `shnro` | Suojattu henkilönumero | — | — | — |
| `tilvv` | Tilastovuosi | — | — | — |
| `tilkk` | Tilastokuukausi | — | — | — |
| `syntykk` | Syntymäkuukausi | — | — | — |
| `syntyv` | Syntymävuosi | — | — | — |
| `sukup` | Sukupuoli | — | sukupuoli_2_1970_01_01 | — |
| `kansa1` | 1. kansalaisuus | — | valtio_12_1999_05_10 | — |
| `askunta` | Asuinkunta | — | — | — |
| `prt_s` | Suojattu pysyvä rakennustunnus | — | — | — |
| `olinpaikka` | Olinpaikka | — | — | — |
| `huontuvtj_s` | Suojattu huoneistotunnus | — | — | — |
| `sivs` | Siviilisääty | — | siviilisaaty_1_2002_01_01 | — |
| `laplubio` | Biologisten lasten lukumäärä | — | — | — |
| `lapluka` | Kaikkien lasten lukumäärä | — | — | — |
| `valkukunta` | valkukunta | — | — | — |
| `rnro_s` | Suojattu rakennusnumero | — | — | — |
| `kansa2` | 2. Kansalaisuus | — | valtio_12_1999_05_10 | — |
| `a3lapluka` | Alle 3-vuotiaiden kaikkien lasten määrä | — | — | — |
| `a7lapluka` | Alle 7-vuotiaiden kaikkien lasten määrä | — | — | — |
| `a13lapluka` | Alle 13-vuotiaiden kaikkien lasten määrä | — | — | — |
| `a18lapluka` | Alle 18-vuotiaiden kaikkien lasten määrä | — | — | — |
| `a3laplubio` | Alle 3-vuotiaiden biologisten lasten määrä | — | — | — |
| `a7laplubio` | Alle 7-vuotiaiden biologisten lasten määrä | — | — | — |
| `a13laplubio` | Alle 13-vuotiaiden biologisten lasten määrä | — | — | — |
| `a18laplubio` | Alle 18-vuotiaiden biologisten lasten määrä | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `shnro` — Suojattu henkilönumero

#### `tilvv` — Tilastovuosi

#### `tilkk` — Tilastokuukausi

#### `syntykk` — Syntymäkuukausi

Henkilön syntymäkuukausi, muotoa KK

#### `syntyv` — Syntymävuosi

Henkilön syntymävuosi, muotoa VVVV

#### `sukup` — Sukupuoli

**Luokitus / Classification:** sukupuoli_2_1970_01_01

Tieto sukupuolesta on saatu Väestötietojärjestelmästä.

#### `kansa1` — 1. kansalaisuus

**Luokitus / Classification:** valtio_12_1999_05_10

1. Kansalaisuus 
Tieto kansalaisuudesta on karkeistettu kolmeen luokkaan: 

1 = Suomi
2 = Muu Eurooppa
3 = Muu

Kansalaisuudella tarkoitetaan jonkin maan kansalaisena olemista. Yleensä kansalaisuus saadaan syntyessä, mutta se voidaan vaihtaa muutettaessa toiseen maahan asumaan. Henkilöllä voi olla myös useamman maan kansalaisuus (kansalaisuuslaki 2003/359 ja kansalaisuusasetus 1985/699). Jos henkilöllä on kahden maan kansalaisuus, joista toinen on Suomen, hän on tilastoissa Suomen kansalaisena. Jos Suomessa asuvalla ulkomaan kansalaisella on useita ulkomaiden kansalaisuuksia, hän on rekisterissä ja tilastoissa sen maan kansalaisena, jonka passilla hän on maahan tullut.

#### `askunta` — Asuinkunta

Kuntanumero. Avain näille on FIONAN Meta-kansiossa.

#### `prt_s` — Suojattu pysyvä rakennustunnus

#### `olinpaikka` — Olinpaikka

Olinpaikka-muuttuja on karkeistettu sen arkaluontoisuuden vuoksi kahteen ryhmään, 0 ja 1. 


0= Kuuluu asuinväestöön

1= Laitoskoodin saanut (esimerkiksi Vailla vakinaista asuntoa, Laitoksessa, Tietymättömissä olevat, Lähetystöissä maailmalla, tilapäisesti ulkomailla, laivanpäällystö, rangaistuslaitokset, hoitolaitokset, asevelvolliset, opiskelun takia poissa, sairaana muualla (ei hoitolaitoksessa), eduskunnassa, lyhyaikaisen työn takia poissa, satunnaisesti poissa kotipaikkakunnalta)

#### `huontuvtj_s` — Suojattu huoneistotunnus

Huoneistotieto perustuu rappukirjaimeen ja huoneistonumeroon. Näiden tarkka kirjoitusasu on saattanut muuttua tietovuosien välillä, joten arvo saattaa muuttua eri vuosina asunnon pysyessä samana.
Porras (1 merkki) + Huoneistonumero (3 merkkiä) + Huoneistotunnisteen jakokirjainosa (1 merkki) + Osoitenumero (1 merkki)

Katso myös "H:\VE\va_513\vaesto\metatiedot\tietojarjestelmat\vtietojarjestelma\attrirh1.doc"
Huoneistotunniste eli huoneistotunnus sisältää seuraavaa
                  
                  1 Porraskirjain on huoneiston tunnisteen kirjainosa. Se
                  kertoo missä portaassa huoneisto sijaitsee.
                  
                  A - Ö, tyhjä. 
                  
                  2 Huoneiston tunnisteen numero_osa. 000 - 999.
                  
                  3 Huoneiston tunnisteen jakokirjain. Jakokirjainta 
                  käytetään kun huoneisto on jaettu kahdeksi tai 
                  useammaksi huoneistoksi.
                  
                  a - ö, tyhjä

#### `sivs` — Siviilisääty

**Luokitus / Classification:** siviilisaaty_1_2002_01_01

Tieto siviilisäädystä saadaan Väestörekisterikeskuksen väestötietojärjestelmästä. On huomioitava, ettei avoliitto ole siviilisääty. Avoliitossa elää jokaisen siviilisäädyn edustajia, myös virallisesti edelleen naimisissa olevia.

Nykyiset avioerosäännökset eivät enää tunne asumuseron käsitettä. Vanhojen avioerosäännösten nojalla ennen 1.1.1988 asumuseroon tuomitut ja edelleen asumuserossa elävät on tilastoissa luettu naimisissa oleviin. 

Samaa sukupuolta olevat parit ovat voineet 1.3.2002 lähtien myös  Suomessa rekisteröidä parisuhteensa. Rekisteröidyssä parisuhteessa olevat on tietosuojasyistä kunnittaisissa taulukoissa luokiteltu yhteen naimisissa olevien kanssa, samoin rekisteröidystä parisuhteesta eronneet tai leskeksi jääneet eronneiden ja leskien kanssa.

Siviilisäätyluokitus on seuraava: 
- naimaton
- naimisissa  
- eronnut  
- leski  
- rekisteröidyssä parisuhteessa
- eronnut rekisteröidystä parisuhteesta
- leski rekisteröidyn parisuhteen jälkeen.

#### `laplubio` — Biologisten lasten lukumäärä

Henkilön biologisten lasten määrä. Sisältää myös lapset, jotka ovat kuolleet tilastoajankohtaan mennessä.

#### `lapluka` — Kaikkien lasten lukumäärä

Henkilön biologisten lasten ja adoptiolasten yhteismäärä. Sisältää myös lapset, jotka ovat kuolleet tilastoajankohtaan mennessä.

#### `valkukunta` — valkukunta

Vuoden alun asuinkunta

#### `rnro_s` — Suojattu rakennusnumero

#### `kansa2` — 2. Kansalaisuus

**Luokitus / Classification:** valtio_12_1999_05_10

2. Kansalaisuus 
Tieto toisesta kansalaisuudesta on karkeistettu:

1 = Suomi
2 = Muu Eurooppa
3 = Muu
' ' = ei toista kansalaisuutta

Kansalaisuudella tarkoitetaan jonkin maan kansalaisena olemista. Yleensä kansalaisuus saadaan syntyessä, mutta se voidaan vaihtaa muutettaessa toiseen maahan asumaan. Henkilöllä voi olla myös useamman maan kansalaisuus (kansalaisuuslaki 2003/359 ja kansalaisuusasetus 1985/699). Jos henkilöllä on kahden maan kansalaisuus, joista toinen on Suomen, hän on tilastoissa Suomen kansalaisena. Jos Suomessa asuvalla ulkomaan kansalaisella on useita ulkomaiden kansalaisuuksia, hän on rekisterissä ja tilastoissa sen maan kansalaisena, jonka passilla hän on maahan tullut.

#### `a3lapluka` — Alle 3-vuotiaiden kaikkien lasten määrä

Henkilön 0-2-vuotiaiden biologisten lasten ja adoptiolasten yhteismäärä. Ikäryhmittäisissä lapsiluvuissa mukana vain tilastoajankohtana elossa olevat lapset.

#### `a7lapluka` — Alle 7-vuotiaiden kaikkien lasten määrä

Henkilön 0-6-vuotiaiden biologisten lasten ja adoptiolasten yhteismäärä. Ikäryhmittäisissä lapsiluvuissa mukana vain tilastoajankohtana elossa olevat lapset.

#### `a13lapluka` — Alle 13-vuotiaiden kaikkien lasten määrä

Henkilön 0-12-vuotiaiden biologisten lasten ja adoptiolasten yhteismäärä. Ikäryhmittäisissä lapsiluvuissa mukana vain tilastoajankohtana elossa olevat lapset.

#### `a18lapluka` — Alle 18-vuotiaiden kaikkien lasten määrä

Henkilön 0-17-vuotiaiden biologisten lasten ja adoptiolasten yhteismäärä. Ikäryhmittäisissä lapsiluvuissa vain tilastoajankohtana elossa olevat lapset.

#### `a3laplubio` — Alle 3-vuotiaiden biologisten lasten määrä

Henkilön 0-2-vuotiaiden biologisten lasten määrä. Ikäryhmittäisissä lapsiluvuissa vain tilastoajankohtana elossa olevat lapset.

#### `a7laplubio` — Alle 7-vuotiaiden biologisten lasten määrä

Henkilön 0-6-vuotiaiden biologisten lasten määrä. Ikäryhmittäisissä lapsiluvuissa vain tilastoajankohtana elossa olevat lapset.

#### `a13laplubio` — Alle 13-vuotiaiden biologisten lasten määrä

Henkilön 0-12-vuotiaiden biologisten lasten määrä. Ikäryhmittäisissä lapsiluvuissa vain tilastoajankohtana elossa olevat lapset.

#### `a18laplubio` — Alle 18-vuotiaiden biologisten lasten määrä

Henkilön 0-17-vuotiaiden biologisten lasten määrä. Ikäryhmittäisissä lapsiluvuissa vain tilastoajankohtana elossa olevat lapset.

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
