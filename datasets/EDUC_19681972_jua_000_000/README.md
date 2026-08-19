# EDUC_OPISK_HIST Korkeakouluopiskelijoiden historialliset tiedot 1968-1972 1. osamoduuli

- **Identifier:** `EDUC_19681972_jua_000_000.xml`
- **DOI:** `he_2024-08_2024-08-29_ain_0001`
- **Temporal coverage:** 1968-01-01 - 1972-12-31
- **Published:** 2026-04-21
- **Organisation:** Tilastokeskus
- **Variable count:** 89
- **Observation count:** —

## Description

Tämä EDUC_OPISK_HIST- moduulin 1.osa kokoaa yhteen korkeakoulujen (eli silloisten yliopistojen ja korkeakoulujen) vanhat henkilötason opiskelijarekisterit alkaen vuodesta 1968 aina vuoteen 1972 saakka. Tilastokeskuksen arkistostoon on tallennettu korkeakoulujen opiskelijarekisterit erikseen kevät- ja syyslukukautta koskien, alkaen syksystä 1967 vuoden 1972 kevääseen saakka. 

Syksyn 1967 tiedostoa ei kuitenkaan saatu käännettyä luettavaan muotoon, jonka vuoksi aineisto alkaa vuoden 1968 kevään tiedoista. Tiedonkeruu lopetettiin vuonna 1972, mutta Tilastokeskus alkoi tekemään niin sanottua ns.kertymätilastoa vuodesta 1975 alkaen. Moduulin 2. osa sisältää nämä kertymätilaston tiedot vuosilta 1975-1995. Tämä tiedostomuoto toimi myöhemmin pohjana Tilastokeskuksen laajemmalle opiskelija-taululle (tutkijakäytössä nimeltään Educ_opisk), josta on löydettävissä samantyyppiset tiedot korkeakoulujen opiskelijoista tuoreemmille vuosille.  

EDUC_OPISK_HIST 1968–1972 ‑aineisto sisältää tietoja korkeakouluissa kirjoilla olleista opiskelijoista. Aikanaan korkeakoulut toimittivat opiskelijarekisterinsä Tilastokeskukselle tilastointia varten ja nämä alkuperäiset rekisterit on säilytetty arkistossa erillisinä tiedostoina.Tilastokeskuksen kirjastossa on saatavilla julkaisu" Korkeakoulut 1966/1967" (Suomen virallinen tilasto), jonka alkuosassa kuvataan rekisterin perustaminen ja kokoaminen Tilastokeskukseen. Teoksessa esitetään myös tiedot aineistossa kerätyistä muuttujista sekä käytetyistä luokituksista.
  
Valmisaineiston osamoduulin 1.osa sisältää kirjoilla olleet korkeakouluopiskelijat (ja heihin liittyvät menneet tiedot) riippuen korkeakoulusta ja lukukaudesta (henkilö voi esiintyä useamman kerran per vuosi ja lukukausi). Eri luokitukset ovat kyseisen vuoden luokituksia, jollei ole mainittu toisin. 

Aineistossa ei ollut henkilötunnusta kaikille henkililöille ennen vuotta 1970. Henkilötunnuksia haettiin Tilastokeskuksen tietokannoista käyttämällä erilaisia päättelysääntöjä. Muuttuja hetu_tag kertoo kuinka henkilötunnus löydettiin henkilöille. Mikäli hetu_tag saa arvon 1, niin henkilön henkilötunnus oli merkittynä rekisteriin ja sille löytyi toimiva hnro. Muuten hnro etsittiin henkilön nimien, syntymäajan ja sukupuolen mukaan käyttäen erilaisia kombinaatioita (tuplia ei sallittu tässä).

HUOM 1: Kyseessä on historiatiedosto, jonka kaikkia eri muuttujia ei ole voitu tarkistaa. 
HUOM 2: Kuvaukset  ovat paikoin puutteellisia.
HUOM 3: Osa muuttujista on kerätty osana erityistä vuosikohtaista selvitystä. Mm. tästä syystä kaikkia muuttujia ei ole moduulista saatavilla kaikilta vuosilta kaikkia korkeakouluja koskien.  
 
Tiedostosta salataan seuraavat:
Hid, opintokirjan numero (voi olla osalle eli puuttellinen, koska numeroinissa esiintyy "00000") ja korkeakoulu (korkeakoulusta kaksi eri versiota, 2-numeroinen jokaista vuotta kuvaava vanha TK:n luokitus ja 5-numeroinen oppilaitostunnus 1995 tilanteen mukaan). Tämän lisäksi suojataan muu korkeakoulu sekä ylioppilaaksi tulon oppilaitos (4-numeroinen, ei TK:n luokitus).

## Variables (89)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `aps` | Tietueen tunniste | — | — | — |
| `kirtuvv` | Kirjoilletulovuosi | — | — | — |
| `kirtulk` | Kirjoilletulolukukausi | — | — | — |
| `kirtupp` | Kijoihintulopäivä | — | — | — |
| `kirtukk` | Kirjoihintulokuukausi | — | — | — |
| `syntymavuosi` | Syntymävuosi | — | — | — |
| `syntymakunta` | Syntymäkunta | — | — | — |
| `sukup` | Sukupuoli | — | — | — |
| `kieli` | Äidinkieli | — | — | — |
| `kansalaisuus` | Kansalaisuus | — | — | — |
| `siviilisaaty` | Sivilisääty | — | — | — |
| `kotikunta` | Kotikunta | — | — | — |
| `osakunta` | Osakunta | — | — | — |
| `ylioppilas` | Ylioppilas | — | — | — |
| `yotutk_pp` | Ylioppilastutkinnon pv (pp) | — | — | — |
| `yotutk_kk` | Ylioppilastutkinnon kuukausi (kk) | — | — | — |
| `yotutk_vv` | Ylioppilastutkinnon vuosi (vv) | — | — | — |
| `yo_keskiarvo` | Ylioppilastutkinnon keskiarvo | — | — | — |
| `yo_arvosana` | Ylioppilastutkinnon arvosana | — | — | — |
| `matematiikan_pituus` | Matematiikan pituus lukiossa | — | — | — |
| `puoltoaanien_lkm` | Lukioiden myöntämät puoltoäänet opiskelijalle | — | — | — |
| `aineiden_lkm` | Aineiden lukumäärä | — | — | — |
| `tiedekunta` | Tiedekunta | — | — | — |
| `opintosuunta` | Opintosuunta | — | — | — |
| `yleinenopintosuunta` | Yleinen opintosuunta (TK:n lisäämä) | — | — | — |
| `lasna_662` | Läsnäolotieto 2/66 | — | — | — |
| `lasna_671` | Läsnäolotieto 1/67 | — | — | — |
| `lasna_672` | Läsnäolotieto 2/67 | — | — | — |
| `lasna_681` | Läsnäolotieto 1/68 | — | — | — |
| `lasna_682` | Läsnäolotieto 2/68 | — | — | — |
| `lasna_691` | Läsnäolotieto 1/69 | — | — | — |
| `lasna_692` | Läsnäolotieto 2/69 | — | — | — |
| `lasna_701` | Läsnäolotieto 1/70 | — | — | — |
| `lasna_702` | Läsnäolotieto 2/70 | — | — | — |
| `lasna_711` | Läsnäolotieto 1/71 | — | — | — |
| `lasna_712` | Läsnäolotieto 2/71 | — | — | — |
| `lasna_721` | Läsnäolotieto 1/72 | — | — | — |
| `opintojentarkoitus` | Opintojen tarkoitus | — | — | — |
| `poissaolonsyy` | Poissaolonsyy | — | — | — |
| `tiedekunnan_nro` | Tiedekunnan numero | — | — | — |
| `yleinentiedekunta` | Yleinentiedekunta | — | — | — |
| `sivuaine1` | 1. sivuaine | — | — | — |
| `sivuaine2` | 2. sivuaine | — | — | — |
| `sivuaine3` | 3. sivuaine | — | — | — |
| `opiskeluaktiivisuus` | Opiskeluaktiivisuus | — | — | — |
| `opiskeluntarkoitus` | Opiskeluntarkoitus | — | — | — |
| `kokopaivatyo` | Kokopaivatyo | — | — | — |
| `osapaivatyo` | Osapaivatyo | — | — | — |
| `edellinentiedekunta1` | Edellinen tiedekunta | — | — | — |
| `edtm1_vvl` | Edellisen tiedekunnan muutosajankohta | — | — | — |
| `edellinentiedekunta2` | Edellistä edellinen tiedekunta | — | — | — |
| `edtm2_vvl` | Edellistä edellisen tiedekunnan muutosajankohta | — | — | — |
| `m_muuallaopiskelu` | Opiskelu muualla | — | — | — |
| `m_koodi` | Opiskelu muualla, opiskelukoodi | — | — | — |
| `m_tiedekunta` | Opiskelu muualla, tiedekunta | — | — | — |
| `m_kirtuppkkvv` | Muualla opiskelun kirjoilletulopäivämäärä | — | — | — |
| `m_oplklkm` | Muualla opiskelun lukukausien lukumäärä | — | — | — |
| `m_opintosuunta` | Muualla opiskelun opintosuunta | — | — | — |
| `tutkintolaskuri` | Tutkintolaskuri | — | — | — |
| `t1_pp` | Uusin tutkinto, suorituspäivä | — | — | — |
| `t1_kk` | Uusin tutkinto, suorituskuukausi | — | — | — |
| `t1_vv` | Uusin tutkinto, suoritusvuosi | — | — | — |
| `t1_tutkintokoodi` | Uusimman tutkinnon tutkintokoodi | — | — | — |
| `t2_pp` | Edellinen tutkinto, suorituspäivä | — | — | — |
| `t2_kk` | Edellinen tutkinto, suorituskuukausi | — | — | — |
| `t2_vv` | Edellinen tutkinto, suoritusvuosi | — | — | — |
| `t2_tutkintokoodi` | Edelllisen tutkinnon tutkintokoodi | — | — | — |
| `t3_pp` | Vanhimman tutkinnon suorituspäivä | — | — | — |
| `t3_kk` | Vanhin tutkinto, suorituskuukausi | — | — | — |
| `t3_vv` | Vanhin tutkinto, suoritusvuosi | — | — | — |
| `t3_tutkintokoodi` | Vanhimman tutkinnon tutkintokoodi | — | — | — |
| `edpsuunta1` | Edellinen opintosuunta | — | — | — |
| `edopsuunta1_vvl` | Edellisen opintosuunnan muutosajankohta | — | — | — |
| `edopsuunta2` | Edelleistä edellisen opintosuunta | — | — | — |
| `edopsuunta2_vvl` | Edellistä edellisen opintosuunann muutosajankohta | — | — | — |
| `aiottuala` | Aiottu ala | — | — | — |
| `aiottututkinto` | Aiottu tutkinto | — | — | — |
| `aitutkintovv` | Aiottu tutkinto suoritusajankohta (vuosi) | — | — | — |
| `aitutkintolk` | Aiottu tutkinto suoritusajankohta (lukukausi) | — | — | — |
| `yo_tulokoulu` | Suojattu ylioppilaaksitulokoulu | — | — | — |
| `m_korkeakoulu` | Suojattu muu korkeakoulu | — | — | — |
| `kkou` | Suojattu 2-numeroinen korkeakoulutunnus | — | — | — |
| `kkou1` | Suojattu 5-numeroinen korkeakoulutunnus | — | — | — |
| `valmistumisflagi` | Valmistumisflagi | — | — | — |
| `opkno` | Suojattu opintokirjan numero | — | — | — |
| `hid_e` | Suojattu henkilön yksilöivä tunnus | — | — | — |
| `hetu_tag` | Hetu_tag | — | — | — |
| `tvuosi` | Tilastovuosi | — | — | — |
| `tkausi` | Tilastokausi | — | — | — |

### Variable definitions

#### `aps` — Tietueen tunniste

A=ainoa, P=pää, S=sivukoulun tietue

#### `kirtuvv` — Kirjoilletulovuosi

Kirjoilletulovuosi, 2-numeroa

#### `kirtulk` — Kirjoilletulolukukausi

Kirjoilletulolukukausi, 1=kevät, 2=syksy.

#### `kirtupp` — Kijoihintulopäivä

Kijoihintulopäivä

#### `kirtukk` — Kirjoihintulokuukausi

Kirjoihintulokuukausia

#### `syntymavuosi` — Syntymävuosi

Syntymävuosi, 2-numeroinen

#### `syntymakunta` — Syntymäkunta

200=ulkomailla, sisältää 000 arvoja jotka luulatavasti "ei tietoa"

#### `sukup` — Sukupuoli

1=mies, 2=nainen.

#### `kieli` — Äidinkieli

Äidinkieli, 1=suomi,2=ruotsi,3=muu, 9=tuntematon

#### `kansalaisuus` — Kansalaisuus

Kansalaisuus, 1=Suomi, 2=muu

#### `siviilisaaty` — Sivilisääty

1=naimaton, 2=naimisissa,3=leski, 4=eronnut, lisäksi muutos on voitu merkitä riippuen vuodesta

#### `kotikunta` — Kotikunta

Kuntakoodi

#### `osakunta` — Osakunta

ei tietoa

#### `ylioppilas` — Ylioppilas

Epävarma, mutta oletettavasti 0= ylioppilas, koska löytyy ylioppilastutkinnon suorittaamisen vuosi

#### `yotutk_pp` — Ylioppilastutkinnon pv (pp)

Kuvaukseen merkitty "YO 0-31; ei yo 110, yo ulkom. 200-231."

#### `yotutk_kk` — Ylioppilastutkinnon kuukausi (kk)

Ylioppilastutkinnon kuukausi (kk)

#### `yotutk_vv` — Ylioppilastutkinnon vuosi (vv)

Ylioppilastutkinnon vuosi (vv)

#### `yo_keskiarvo` — Ylioppilastutkinnon keskiarvo

Kuvaukseen merkitty "9.99 suurin mahdollinen arvo".

#### `yo_arvosana` — Ylioppilastutkinnon arvosana

Käytä varauksella, luokitus eroaa kuvauksesta. Kuvaukseen merkitty  "2,2,4,6".

#### `matematiikan_pituus` — Matematiikan pituus lukiossa

Kuvaukseen merkitty, 0= ei tietoa, 1=pitkä, 2=lyhyt.

#### `puoltoaanien_lkm` — Lukioiden myöntämät puoltoäänet opiskelijalle

Käytä varauksella, luokitus eroaa kuvauksesta. Kuvaukseen merkitty, "0, 4-18"

#### `aineiden_lkm` — Aineiden lukumäärä

Kuvaukseen merkitty, "0, 4-6"

#### `tiedekunta` — Tiedekunta

Tiedekuntakoodi

#### `opintosuunta` — Opintosuunta

Opintosuunta tai pääaine

#### `yleinenopintosuunta` — Yleinen opintosuunta (TK:n lisäämä)

Yleinen opintosuunta (TK:n lisäämä)

#### `lasna_662` — Läsnäolotieto 2/66

Kuvaukseen merkitty "Alkaen v.66 syyslukukaudesta(662); 0,1,2."

#### `lasna_671` — Läsnäolotieto 1/67

Kuvaukseen merkitty "Alkaen v.66 syyslukukaudesta(662); 0,1,2."

#### `lasna_672` — Läsnäolotieto 2/67

Kuvaukseen merkitty "Alkaen v.66 syyslukukaudesta(662); 0,1,2."

#### `lasna_681` — Läsnäolotieto 1/68

Kuvaukseen merkitty "Alkaen v.66 syyslukukaudesta(662); 0,1,2."

#### `lasna_682` — Läsnäolotieto 2/68

Kuvaukseen merkitty "Alkaen v.66 syyslukukaudesta(662); 0,1,2

#### `lasna_691` — Läsnäolotieto 1/69

Kuvaukseen merkitty "Alkaen v.66 syyslukukaudesta(662); 0,1,2."

#### `lasna_692` — Läsnäolotieto 2/69

Kuvaukseen merkitty "Alkaen v.66 syyslukukaudesta(662); 0,1,2."

#### `lasna_701` — Läsnäolotieto 1/70

Kuvaukseen merkitty "Alkaen v.66 syyslukukaudesta(662); 0,1,2."

#### `lasna_702` — Läsnäolotieto 2/70

Kuvaukseen merkitty "Alkaen v.66 syyslukukaudesta(662); 0,1,2."

#### `lasna_711` — Läsnäolotieto 1/71

Kuvaukseen merkitty "Alkaen v.66 syyslukukaudesta(662); 0,1,2."

#### `lasna_712` — Läsnäolotieto 2/71

Kuvaukseen merkitty "Alkaen v.66 syyslukukaudesta(662); 0,1,2."

#### `lasna_721` — Läsnäolotieto 1/72

Kuvaukseen merkitty "Alkaen v.66 syyslukukaudesta(662); 0,1,2."

#### `opintojentarkoitus` — Opintojen tarkoitus

Kuvaukseen merkitty  "1-9 opetusminist. 0 ei tietoa, 692 alkaen"

#### `poissaolonsyy` — Poissaolonsyy

Kuvaukseen merkitty  "s.68 lähtien 0-9"

#### `tiedekunnan_nro` — Tiedekunnan numero

Tiedekunnan numero 2-numeroinen

#### `yleinentiedekunta` — Yleinentiedekunta

Yleinen tiedekunta (TK:n lisäämä)

#### `sivuaine1` — 1. sivuaine

Ensimmäinen sivuaine. 3-numeroinen sivuainekoodi, kuvaukseen merkitty  "Tku, Åbo, J-lä"

#### `sivuaine2` — 2. sivuaine

Toinen sivuaine. 3-numeroinen sivuainekoodi

#### `sivuaine3` — 3. sivuaine

Kolmas sivuaine. 3-numeroinen sivuainekoodi.

#### `opiskeluaktiivisuus` — Opiskeluaktiivisuus

Kuvaukseen merkitty  "1=täyspäiväopisk., 2=osapäiväopisk. 0=ei tietoa, 692 alkaen."

#### `opiskeluntarkoitus` — Opiskeluntarkoitus

Kuvaukseen merkitty  "0-4,9. kys 66-68:aion suor. 1=täällä,2=muu kk, 3=en" sekä "1-9 opetusminist. 9 ei tietoa, 692 alk."

#### `kokopaivatyo` — Kokopaivatyo

Kuvaukseen merkitty  "kk:ien määrä ed.lukuk., 0-5. kysytty 68/69"

#### `osapaivatyo` — Osapaivatyo

Kuvaukseen merkitty  "kk:ien määrä ed.lukuk., 0-5. kysytty 68/69"

#### `edellinentiedekunta1` — Edellinen tiedekunta

Edellinen tiedekunta, kuvaukseen merkitty  "s.69 alkaen"

#### `edtm1_vvl` — Edellisen tiedekunnan muutosajankohta

Edellisen tiedekunnan muutosajankohta, vuosi ja lukukausi

#### `edellinentiedekunta2` — Edellistä edellinen tiedekunta

Edellistä edellisen tiedekunta, kuvaukseen merkitty  "s.69 alkaen"

#### `edtm2_vvl` — Edellistä edellisen tiedekunnan muutosajankohta

Edellistä edellisen tiedekunnan muutosajankohta, vuosi ja lukukausi

#### `m_muuallaopiskelu` — Opiskelu muualla

Opiskelu muualla, Kuvaukseen merkittu vain "0,1". Todennäköisimmin 0= ei, 1= kyllä.

#### `m_koodi` — Opiskelu muualla, opiskelukoodi

Kuvaukseen merkittt "o-3 (lom.kohdan 14 alajako)

#### `m_tiedekunta` — Opiskelu muualla, tiedekunta

Muualla opiskelun tiedekunta. Kuvaukseen kirjattu "vain, jos opisk.koodi 2".

#### `m_kirtuppkkvv` — Muualla opiskelun kirjoilletulopäivämäärä

Opiskelu muualla, aloitusajankohta (päivä, kuukausi, vuosi): Kuvaukseen kirjattu "jos opisk.koodi 2 tai 3".

#### `m_oplklkm` — Muualla opiskelun lukukausien lukumäärä

Muualla opiskelun lukukausien lukumäärä. Kuvaukseen merkitty "vain jos opisk.koodi 3".

#### `m_opintosuunta` — Muualla opiskelun opintosuunta

Muualla opiskelun opintosuunta

#### `tutkintolaskuri` — Tutkintolaskuri

Ei lainkaan kuvausta, ei tarkempaa tietoa.

#### `t1_pp` — Uusin tutkinto, suorituspäivä

Uusin tutkinto, suorituspäivä.(pp)

#### `t1_kk` — Uusin tutkinto, suorituskuukausi

Uusin tutkinto, suorituskuukausi (kk)

#### `t1_vv` — Uusin tutkinto, suoritusvuosi

Uusin tutkinto, suoritusvuosi (vv)

#### `t1_tutkintokoodi` — Uusimman tutkinnon tutkintokoodi

Uusin tutkinto, tutkintokoodi. Ei tietoa luokituksesta.

#### `t2_pp` — Edellinen tutkinto, suorituspäivä

Edellinen tutkinto, suorituspäivä (pp)

#### `t2_kk` — Edellinen tutkinto, suorituskuukausi

Edellinen tutkinto, suorituskuukausi (kk)

#### `t2_vv` — Edellinen tutkinto, suoritusvuosi

Edellinen tutkinto, suoritusvuosi (vv)

#### `t2_tutkintokoodi` — Edelllisen tutkinnon tutkintokoodi

Edellinen tutkinto, tutkintokoodi. Ei tietoa luokituksesta.

#### `t3_pp` — Vanhimman tutkinnon suorituspäivä

Vanhin tutkinto, suorituspäivä (pp)

#### `t3_kk` — Vanhin tutkinto, suorituskuukausi

Vanhin tutkinto, suorituskuukausi (kk)

#### `t3_vv` — Vanhin tutkinto, suoritusvuosi

Vanhin tutkinto, suoritusvuosi (vv)

#### `t3_tutkintokoodi` — Vanhimman tutkinnon tutkintokoodi

Vanhin tutkinto, tutkintokoodi

#### `edpsuunta1` — Edellinen opintosuunta

Edellinen opintosuunta

#### `edopsuunta1_vvl` — Edellisen opintosuunnan muutosajankohta

Edellisen opintosuunnan muutosajankohta (vvl)

#### `edopsuunta2` — Edelleistä edellisen opintosuunta

Edelleistä edellisen opintosuunta

#### `edopsuunta2_vvl` — Edellistä edellisen opintosuunann muutosajankohta

Edellistä edellisen opintosuunann muutosajankohta (vvl)

#### `aiottuala` — Aiottu ala

Kuvaukseen merkitty 1969-1970 lk: "671:n erikoistutkimus" ja 1970:  "1=opett, 2= lehd, 3=liikme, 4=hall, 5=järj, 6=muu"

#### `aiottututkinto` — Aiottu tutkinto

Aiottu tutkinto, 66/67 erikostutkimus

#### `aitutkintovv` — Aiottu tutkinto suoritusajankohta (vuosi)

Aiottu tutkinto suoritusajankohta (vuosi), 66/67 erikostutkimus

#### `aitutkintolk` — Aiottu tutkinto suoritusajankohta (lukukausi)

Aiottu tutkinto suoritusajankohta (lukukausi), 66/67 erikostutkimus

#### `yo_tulokoulu` — Suojattu ylioppilaaksitulokoulu

Suojattu ylioppilaaksitulokoulu, kuvaukseen merkitty "Helsingin yliopiston koululuettelo".

#### `m_korkeakoulu` — Suojattu muu korkeakoulu

Suojattu muu korkeakoulu, liittyy m_ alkuisiin muuttujiin

#### `kkou` — Suojattu 2-numeroinen korkeakoulutunnus

2-numeroinen alkuperäinen korkeakoulutunnus

#### `kkou1` — Suojattu 5-numeroinen korkeakoulutunnus

TK:n 5 numeroinen oppilaitostunnus 1995 mukaan

#### `valmistumisflagi` — Valmistumisflagi

Ei tarkempaa tietoa, lisätty aikanaan luultavasti tutkintoreksiteriä käyttäen.

#### `opkno` — Suojattu opintokirjan numero

Suojattu opintokirjanumero, vain osalle vuosia, osalle 00000

#### `hid_e` — Suojattu henkilön yksilöivä tunnus

Suojattu henkilön yksilöivä tunnus

#### `hetu_tag` — Hetu_tag

Kertoo onko hnro päätelty.1= hetu löytyy rekisteristä. Muut arvot = hetu päätelty

#### `tvuosi` — Tilastovuosi

Tiedoston tallennuksen tilastovuosi, lisätty aineistoon

#### `tkausi` — Tilastokausi

Tiedoston tallennuksen tilastokausi, lisätty aineistoon

---

[← Back to catalogue](../../README.md)
