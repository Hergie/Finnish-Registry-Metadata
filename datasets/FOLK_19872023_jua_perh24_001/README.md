# FOLK_PERH

- **Identifier:** `FOLK_19872023_jua_perh24_001.xml`
- **DOI:** `work_2017-08_2017-08-03_ain_0003`
- **Temporal coverage:** 1987-01-01 - 2024-12-31
- **Published:** 2025-12-22
- **Organisation:** Tilastokeskus
- **Variable count:** 15
- **Observation count:** —
- **Population:** Perheväestöön kuuluvat henkilöt sekä ne perhväestöön kuulumattomat henkilöt, joilla on lapsia

## Description

FOLK-henkilöaineiston perhemoduuli sisältää tietoja perheväestöön kuuluvien henkilöiden perheistä, erityisesti perheen lasten lukumäärään liittyen. Laajempia perhetietoja (perheen koko, perhetyyppi, perheasema, perheen lasten lukumäärät) löytyy FOLK perustiedot-valmisaineistomoduulista.

<b> Valmisaineiston tarkentava nimi </b>
Tiedot perheväestöön kuuluvien henkilöiden perheistä ja lasten lukumäärästä sekä perheväestöön kuulumattomien henkilöiden lasten lukumäärästä

<b> Aineiston perusjoukko, koostaminen ja tietolähteet </b> 
Aineiston perusjoukkona toimii perhe. Tarkempi määritelmä perheestä on saatavilla <a href="https://stat.fi/meta/kas/perhe.html">Tilastokeskuksen verkkosivuilla</a>.. Lisäksi mukana ovat lapsilukutiedot niille henkilöille, jotka eivät kuulu perheväestöön, mutta joilla on lapsia (laplubio ja lapluka). Perheväestön lukumäärätiedot ovat esitetty numeroarvoina. Aineisto on muodostettu Tilastokeskuksessa muodostetun perhetilastoaineiston tiedoista, joissa lähteenä Digi- ja väestötietoviraston väestötietojärjestelmän eli VTJ-tietoja. 

<b> Huomioitavaa aineistosta ja sen käytöstä </b>
Moduuli sisältää perhekohtaiset koodit, joiden avulla perheenjäsenet voidaan yhdistää saman tilastovuoden aikana.  

Aineistossa on tiedot vuodesta 1987 alkaen. Mahdolliset poikkeamat tietojen saatavuudessa on merkitty muuttujankuvaukseen vuosiluvuilla. Tiedot ovat linkitettävissä muihin henkilövalmisaineistomoduuleihin suojatun henkilönumeron avulla. Mahdolliset muutokset on kuvattu muuttujakohtaisesti. 

<b> Aineiston päivitysaikataulu </b>
Tutustu valmisaineistojen <a href="https://stat.fi/fi/palvelut/palvelut-tutkijoille/tutkimusaineistot/valmisaineistot/valmisaineistojen-paivitysaikataulu">  päivitysaikatauluun</a>.

<b> Aineiston käyttö ja tilaaminen </b> 
Aineisto on tarkoitettu käytettäväksi FIONA-etäpalvelun kautta, ja se on linkitettävissä muihin henkilövalmisaineistomoduuleihin suojatun  henkilöä yksilöivän tunnisteen avulla. Tietoja voi tilata tutkimuksen kohdejoukolle ja tietylle ajanjaksolle.  Aineiston kokonaisaineiston (kaikki muuttujat koko populaatiolle ja kaikilta saatavissa olevilta vuosilta) käyttöoikeus myönnetään vain, jos tutkimuksellinen tarve sitä erityisesti edellyttää. Aineiston muuttujia voi tilata myös räätälöitynä versiona, jos tutkimustarve kohdistuu vain osaan valmisaineiston muuttujista.
 
Aineisto on FIONA-etäkäyttöjärjestelmässä jaettuina vuosikansioihin tilastovuosittain. 

<b> Lisätietoja </b> 
Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@stat.fi

## Variables (15)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `vuosi` | Vuosi | — | — | — |
| `hid_e` | Suojattu henkilön yksilöivä tunniste | — | — | — |
| `petu` | Perheen tunniste | — | — | — |
| `laplubio` | Henkilön biologisten lasten lukumäärä | — | — | Vaestorakenne |
| `lapluka` | Henkilön kaikkien lasten lukumäärä | — | — | Vaestorakenne |
| `uusper` | Uusperhe | — | — | Perhe |
| `pekoko` | Perheen koko | — | — | Perhe |
| `lkm` | Perheen lasten lukumäärä | — | — | Perhe |
| `a3lkm` | Perheen alle 3-vuotiaiden lasten lkm | — | — | Perhe |
| `a7lkm` | Perheen alle 7-vuotiaiden lasten lkm | — | — | Perhe |
| `a18lkm` | Perheen alle 18-v. lasten lkm | — | — | Perhe |
| `a25lkm` | Perheen alle 25-v. lasten lkm | — | — | Perhe |
| `yhta18` | Perheen vanhempien alle 18-v. yhteisten biologisten tai adoptiolasten | — | — | Perhe |
| `aidina18` | Vain äidin alle 18-v. t lasten lkm | — | — | Perhe |
| `isana18` | Vain isän alle 18-v. lasten lkm | — | — | Perhe |

### Variable definitions

#### `vuosi` — Vuosi

Tilastovuosi

#### `hid_e` — Suojattu henkilön yksilöivä tunniste

Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e -tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä.

#### `petu` — Perheen tunniste

Perheen tunnisteella voidaan liittää yhtenä havaintovuonna saman perheen henkilöt yhteen. Havaintovuosien välillä sama perheen tunniste ei välttämättä tarkoita samaa perhettä eikä muuttuja kerro riippumatonta lapsi-vanhempi suhdetta. Perheen tunniste perustuu TK:n rakennusnumero-huoneistonumero-perhenumero-yhdistelmään, joka voi samalla perheellä vaihdella vuosittain esimerkiksi muuton takia. Muuttujan arvoon vaikuttaa myös poimintavuosi, eli arvo ei ole identtinen vuositiedostojen ja vanhojen, useita vuosia sisältävien tiedostojen välillä.

'00000000' = perheväestöön kuulumaton henkilö, jolla on kuitenkin adpotio/biologinen lapsi.

#### `laplubio` — Henkilön biologisten lasten lukumäärä

**Group:** Vaestorakenne

Henkilön biologisten lasten lukumäärä, tieto vuodesta 1989 lähtien. Lapsettomille muuttujan arvo on puuttuva vuosina 1987-2004 ja nolla vuodesta 2005 lähtien.

#### `lapluka` — Henkilön kaikkien lasten lukumäärä

**Group:** Vaestorakenne

Henkilön kaikkien biologisten ja/tai adoptiolasten lukumäärä. Lapsettomille muuttujan arvo on puuttuva vuosina 1987-2004 ja nolla vuodesta 2005 lähtien.

#### `uusper` — Uusperhe

**Group:** Perhe

Perheessä ainakin yksi ei-yhteinen lapsi, ei ikärajaa.

Vuodesta 2006 lähtien:
0 = ei uusperhe, 
1 = uusperhe, vanhemmat aviopari, vanhemmat rekisteröity pari, vanhemmat samansukupuolinen aviopari
2 = uusperhe, vanhemmat avopari, 
null = ei kuulu perheväestöön

Seuraavat arvot ovat sisällytetty arvoon 1:
3 = uusperhe, vanhemmat rekisteröity pari,
4 = uusperhe, vanhemmat samansukupuolinen aviopari

Vuoteen 2005 asti: 
1 = on uusperhe
null = ei uusperhe / ei kuulu perheväestöön

#### `pekoko` — Perheen koko

**Group:** Perhe

Perheen henkilöiden lukumäärä. Perheväestöön kuuluvilla perheen koko on kaksi tai enemmän, bl = perheväestöön kuulumaton

#### `lkm` — Perheen lasten lukumäärä

**Group:** Perhe

Perheen lasten lukumäärä, kaikki kotona asuvat biologiset ja ottolapset, ei ikärajaa, bl = perheväestöön kuulumaton

#### `a3lkm` — Perheen alle 3-vuotiaiden lasten lkm

**Group:** Perhe

Perheen alle 3-vuotiaiden lasten lukumäärä, kotona asuvat kaikki  biologiset ja ottolapset. Tieto vuodesta 2006 lähtien, bl = perheväestöön kuulumaton.

#### `a7lkm` — Perheen alle 7-vuotiaiden lasten lkm

**Group:** Perhe

Perheen alle 7-vuotiaiden lasten lukumäärä, kotona asuvat kaikki  biologiset ja ottolapset, bl = perheväestöön kuulumaton.

#### `a18lkm` — Perheen alle 18-v. lasten lkm

**Group:** Perhe

Perheen alle 18-vuotiaiden lasten lukumäärä, kaikki kotona asuvat biologiset ja ottolapset, bl = perheväestöön kuulumaton.

#### `a25lkm` — Perheen alle 25-v. lasten lkm

**Group:** Perhe

Perheen alle 25-vuotiaiden lasten lukumäärä, kaikki kotona asuvat biologiset ja ottolapset, bl = perheväestöön kuulumaton.

#### `yhta18` — Perheen vanhempien alle 18-v. yhteisten biologisten tai adoptiolasten

**Group:** Perhe

Uusperheen vanhempien alle 18-vuotiaiden yhteisten biologisten tai adoptiolasten lukumäärä, bl = perheväestöön kuulumaton.

#### `aidina18` — Vain äidin alle 18-v. t lasten lkm

**Group:** Perhe

Vain äidin alle 18-vuotiaat biologiset tai adoptiolapset. Vuosina 1987-2005 tieto koskee vain uusperheitä, bl = perheväestöön kuulumaton.

#### `isana18` — Vain isän alle 18-v. lasten lkm

**Group:** Perhe

Vain isän alle 18-vuotiaat biologiset tai adoptiolapset. Vuosina 1987-2005 tieto koskee vain uusperheitä, bl = perheväestöön kuulumaton.

---

[← Back to catalogue](../../README.md)
