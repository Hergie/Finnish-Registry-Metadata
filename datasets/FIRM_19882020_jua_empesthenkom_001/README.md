# FIRM_EMPEST Toimipaikkakohtaiset henkilöstöominaisuudet

- **Identifier:** `FIRM_19882020_jua_empesthenkom_001.xml`
- **DOI:** `work_2012-12_2012-12-10_ain_0001`
- **Temporal coverage:** 1988-01-01 - 2022-12-31
- **Published:** 2024-07-25
- **Organisation:** Tilastokeskus
- **Variable count:** 36
- **Observation count:** —
- **Population:** 16-70-vuotiaat henkilöt yritysrekisterin toimipaikoissa, joille löytyy vähintään 1 henkilö FOLK/FLEEDistä
- **Source:** FOLK/FLEED-aineisto (mm. työssäkäyntitilasto) ja yritysrekisteri

## Description

FOLK-aineistosta on muodostettu tutkimuskäyttöön toimipaikkapohjaiset taulut, joihin on laskettu henkilöstön keskimääräisiä ominaisuuksia ja eri henkilöstöryhmien osuuksia vuodesta 2017 alkaen. Ajanjaksolta 1988-2016 päivitys on tehty FLEED (Finnish Longitudinal Employer - Employee Data)-kokonaisaineiston tietojen pohjalta. Kehikkona on käytetty vuodesta 2013 alkaen toimipaikkatietoja yritystietovarastosta (aikaisemmin yritysrekisteristä). Kohdejoukossa on tilastojärjestelmien ja tilastorajojen muutoksista johtuvia vuosittaisia eroja. Vuoteen 2012 asti mukana on myös ei-tilastoyksiköitä. Ennen vuotta 2000 mukana voi olla myös julkisia yksiköitä, joten yritysrekisterin tilastoyksiköt kannattaa rajata käyttämällä TILYKS=1, koska toimipaikkatunnus ei ole välttämättä yksilöivä. Vuodesta 1998 eteenpäin myös henkilöyrittäjille löytyy toimipaikkatunnus. Mukaan on otettu yritykset, joille löytyy vähintään 1 henkilöhavainto FOLK-moduulista (ennen vuotta 2017 FLEED-moduulista). Kyseisen aineiston henkilömäärää on käytetty osuuksia laskettaessa jakajana. Mukana ovat 16 - 70-vuotiaat henkilöt. 


Keskimääräiset kouluvuodet on määritelty seuraavasti (UTUTKU vuoteen 2004 asti, 2005 alkaen pohjana KTUTK): 
Tutkinnot muutetaan kouluvuosiksi seuraavasti
- Jos koulutustaso='3' tai '4', kouluvuodet=12  (Toinen aste ja erikoisammattikoulutusaste)
- Jos koulutustaso='5', kouluvuodet=14 (Alin korkea-aste)
- Jos koulutustaso='6', kouluvuodet=16 (Alempi korkeakouluaste)
- Jos koulutustaso='7', kouluvuodet=18 (Ylempi korkeakouluaste)
- Jos koulutustaso='8', kouluvuodet=21 (Tutkijakoulutusaste)
- Muutoin kouluvuodet=9

Koulutusryhmät on määritelty seuraavasti:
Muodostetaan 10 työntekijäryhmää koulutustason ja -alan mukaan. XY, jossa X viittaa koulutustasoon (2=peruskoulu, 3=toinen aste ja erikoisammattitukinnot, 5=alin korkea-aste, 6=alempi korkeakouluaste, 8=ylempi korkeakouluaste ja tutkijakoulutusaste) ja Y alaan: Y=G yleinen, Y=T, ”tekninen” (luonnontieteellinen ja tekniikan/ICT koulutus) ja Y=N ”ei-tekninen”. Vuodesta 2016 lähtien 4-alkuiset erikoisammattitutkinnot on sisällytetty luokkaan 3. 

Kullekin koulutusryhmälle on lisäksi laskettu keskimääräiset kuukausiansiot työtulojen (palkkatulot) summan ja työssäolokuukausien summan suhteena. Tämä mittari ei ole kuitenkaan täysin luotettava, esim. äitiysvapaakuukaudet lasketaan mukaan työssäolokuukausiin mutta näillä henkilöillä ei ole työtuloja.

Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@tilastokeskus.fi.

## Variables (36)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `sykstun` | Suojattu toimipaikkatunnus | — | — | — |
| `emp_yrek` | Henkilöstön lukumäärä, Yritysrekisteri | — | — | — |
| `mwage3T` | Keskipalkka, 3T | — | — | — |
| `mwage2G` | Keskipalkka, 2G | — | — | — |
| `mwage3N` | Keskipalkka, 3N | — | — | — |
| `mwage5T` | Keskipalkka, 5T | — | — | — |
| `mwage3G` | Keskipalkka, 3G | — | — | — |
| `mwage8N` | Keskipalkka, 8N | — | — | — |
| `mwage5N` | Keskipalkka, 5N | — | — | — |
| `mwage6T` | Keskipalkka, 6T | — | — | — |
| `mwage6N` | Keskipalkka, 6N | — | — | — |
| `mwage8T` | Keskipalkka, 8T | — | — | — |
| `sh2G` | Osuus, 2G | — | — | — |
| `sh3G` | Osuus, 3G | — | — | — |
| `sh3N` | Osuus, 3N | — | — | — |
| `sh3T` | Osuus, 3T | — | — | — |
| `sh5N` | Osuus, 5N | — | — | — |
| `sh5T` | Osuus, 5T | — | — | — |
| `sh6N` | Osuus, 6N | — | — | — |
| `sh6T` | Osuus, 6T | — | — | — |
| `sh8N` | Osuus, 8N | — | — | — |
| `sh8T` | Osuus, 8T | — | — | — |
| `emp_fleed` | Henkilöstön lukumäärä, FLEED | — | — | — |
| `shage16_24` | Osuus, 16-24v. | — | — | — |
| `shage25_34` | Osuus, 25-34v. | — | — | — |
| `shage35_44` | Osuus, 35-44v. | — | — | — |
| `shage45_54` | Osuus, 45-54v. | — | — | — |
| `shage55_70` | Osuus, 55-70v. | — | — | — |
| `age` | Keskimääräinen ikä | — | — | — |
| `senmonths` | Yrityskohtainen työkokemus, kuukausia | — | — | — |
| `educyears` | Keskimääräiset koulutusvuodet | — | — | — |
| `shwomen` | Naisten osuus | — | — | — |
| `year` | Vuosi | — | — | — |
| `stdage` | Iän keskihajonta | — | — | — |
| `stdeduc` | Koulutusvuosien keskihajonta | — | — | — |
| `tilyks` | Tilastoyksikkö yritysrekisterin vuositilastossa | — | — | — |

### Variable definitions

#### `sykstun` — Suojattu toimipaikkatunnus

#### `emp_yrek` — Henkilöstön lukumäärä, Yritysrekisteri

#### `mwage3T` — Keskipalkka, 3T

Koulutusryhmät on määritelty seuraavasti:
Muodostetaan 10 työntekijäryhmää koulutustason ja -alan mukaan. XY, jossa X viittaa koulutustasoon ja Y alaan: Y=G yleinen, Y=T, ”tekninen” (luonnontieteellinen ja tekniikan koulutus) ja Y=N ”ei-tekninen”
- Jos koulutuskoodi='30', XY='3G'
- Jos koulutuskoodi=('31', '32', '33', '36', '37', '38', '39'), XY='3N'
- Jos koulutuskoodi=('34', '35'), XY='3T'
- Jos koulutuskoodi=('('51', '52', '53', '56', '57', '58', '59'), XY='5N'
- Jos koulutuskoodi=('('54', '55'), XY='5T'
- Jos koulutuskoodi=('('61', '62', '63', '66', '67', '68', '69'), XY='6N'
- Jos koulutuskoodi=('('64', '65'), XY='6T'
- Jos koulutuskoodi=('('71', '72', '73', '76', '77', '78', '79', '81', '82', '83', '86', '87', '88', '89'), XY='8N'
- Jos koulutuskoodi=('('74', '75', '84', '85'), XY='8T'
- Muutoin XY='2G'
Kullekin koulutusryhmälle on laskettu keskimääräiset kuukausiansiot työtulojen (palkkatulot) summan ja työssäolokuukausien summan suhteena. Tämä mittari ei ole kuitenkaan täysin luotettava, esim. äitiysvapaakuukaudet lasketaan mukaan työssäolokuukausiin mutta näillä henkilöillä ei ole työtuloja.

Vuonna 2016 4-alkuiset erikoisammattitutkinnot on sisällytetty luokkaan 3.

#### `mwage2G` — Keskipalkka, 2G

#### `mwage3N` — Keskipalkka, 3N

#### `mwage5T` — Keskipalkka, 5T

#### `mwage3G` — Keskipalkka, 3G

#### `mwage8N` — Keskipalkka, 8N

#### `mwage5N` — Keskipalkka, 5N

#### `mwage6T` — Keskipalkka, 6T

#### `mwage6N` — Keskipalkka, 6N

#### `mwage8T` — Keskipalkka, 8T

#### `sh2G` — Osuus, 2G

Koulutusryhmät on määritelty seuraavasti:
Muodostetaan 10 työntekijäryhmää koulutustason ja -alan mukaan. XY, jossa X viittaa koulutustasoon ja Y alaan: Y=G yleinen, Y=T, ”tekninen” (luonnontieteellinen ja tekniikan koulutus) ja Y=N ”ei-tekninen”
- Jos koulutuskoodi='30', XY='3G'
- Jos koulutuskoodi=('31', '32', '33', '36', '37', '38', '39'), XY='3N'
- Jos koulutuskoodi=('34', '35'), XY='3T'
- Jos koulutuskoodi=('('51', '52', '53', '56', '57', '58', '59'), XY='5N'
- Jos koulutuskoodi=('('54', '55'), XY='5T'
- Jos koulutuskoodi=('('61', '62', '63', '66', '67', '68', '69'), XY='6N'
- Jos koulutuskoodi=('('64', '65'), XY='6T'
- Jos koulutuskoodi=('('71', '72', '73', '76', '77', '78', '79', '81', '82', '83', '86', '87', '88', '89'), XY='8N'
- Jos koulutuskoodi=('('74', '75', '84', '85'), XY='8T'
- Muutoin XY='2G'

Vuonna 2016 4-alkuiset erikoisammattitutkinnot on sisällytetty luokkaan 3.

#### `sh3G` — Osuus, 3G

#### `sh3N` — Osuus, 3N

#### `sh3T` — Osuus, 3T

#### `sh5N` — Osuus, 5N

#### `sh5T` — Osuus, 5T

#### `sh6N` — Osuus, 6N

#### `sh6T` — Osuus, 6T

#### `sh8N` — Osuus, 8N

#### `sh8T` — Osuus, 8T

#### `emp_fleed` — Henkilöstön lukumäärä, FLEED

#### `shage16_24` — Osuus, 16-24v.

#### `shage25_34` — Osuus, 25-34v.

#### `shage35_44` — Osuus, 35-44v.

#### `shage45_54` — Osuus, 45-54v.

#### `shage55_70` — Osuus, 55-70v.

#### `age` — Keskimääräinen ikä

#### `senmonths` — Yrityskohtainen työkokemus, kuukausia

Senioriteetti TVM-käsitteen eli vuoden viimeisen viikon tilanteen mukaan

#### `educyears` — Keskimääräiset koulutusvuodet

- Tutkinnot muutetaan kouluvuosiksi seuraavasti:
 Jos koulutustaso='3', kouluvuodet=12  (Keskiaste)
 Jos koulutustaso='5', kouluvuodet=14 (Alin korkea-aste)
 Jos koulutustaso='6', kouluvuodet=16 (Alempi korkeakouluaste)
 Jos koulutustaso='7', kouluvuodet=18 (Ylempi korkeakouluaste)
 Jos koulutustaso='8', kouluvuodet=21 (Tutkijakoulutusaste)
 Muutoin kouluvuodet=9
- Vuoteen 2004 asti pohjautuu UTUTKU-muuttujaan (vuoden 2004 koulutusluokituksen mukainen), vuodesta 2005 alkaen pohjana KTUTK (kyseisen vuoden koulutusluokituksen mukainen)

Vuonna 2016 4-alkuiset erikoisammattitutkinnot on sisällytetty luokkaan 3.

#### `shwomen` — Naisten osuus

#### `year` — Vuosi

#### `stdage` — Iän keskihajonta

Henkilöstön iän keskihajonta

#### `stdeduc` — Koulutusvuosien keskihajonta

Henkilöstön koulutusvuosien keskihajonta

#### `tilyks` — Tilastoyksikkö yritysrekisterin vuositilastossa

Tilastoyksikkö. 
Mahdolliset arvot ovat:
1 = tulee tilastoon 
blankko = ei tule tilastoon 
Tilastoon tulevat yritykset ja toimipaikat, jotka ovat toimineet yli puoli vuotta tilastovuonna ja jotka ovat työllistäneet enemmän kuin puoli henkilöä tai joiden liikevaihto on ylittänyt vuosittain määritellyn tilastorajan (esim. 10 595 euroa vuonna 2012). Suositellaan käytettävän vain tilastoyksiköiden tietoja, koska mukana voi olla julkisten yhteisöjen yksiköitä, joita toimipaikkatunnus ei aina yksilöi.

---

[← Back to catalogue](../../README.md)
