# FOLK  perhe

- **Identifier:** `FOLK_19872023_jua_perh24_001.xml`
- **DOI:** `work_2017-08_2017-08-03_ain_0003`
- **Temporal coverage:** 1987-01-01 - 2024-12-31
- **Published:** 2025-12-22
- **Organisation:** Tilastokeskus
- **Variable count:** 15
- **Observation count:** —
- **Population:** Perheväestöön kuuluvat henkilöt sekä ne perhväestöön kuulumattomat henkilöt, joilla on lapsia

## Kuvaus / Description

FOLK-henkilöaineiston perhemoduulissa on perheväestöön kuuluvien henkilöiden perhettä koskevia, pääasiassa perheen lasten lukumäärään liittyviä tietoja. Tarkempi kuvaus perheen määritelmästä on saatavilla osoitteesta http://www.stat.fi/meta/kas/perhe.html. Moduuli sisältää perheille luodut koodit perheenjäsenten yhdistämiseksi saman tilastovuoden aikana.

Lisäksi moduulissa on niiden perheväestöön kuulumattomien henkilöiden lapsilukutiedot (laplubio ja lapluka), jotka eivät kuulu perheväestöön, mutta joilla on lapsia. Perheväestön lukumäärätiedot ovat numeroarvoina.

Aineistossa on tietoja vuodesta 1987 lähtien. Poikkeamat tietojen saatavuudessa on merkitty muuttujankuvaukseen vuosiluvuilla. Tiedot on linkitettävissä muiden henkilövalmisaineistomoduulien kanssa suojatun henkilönumeron avulla. Mahdolliset muutokset on kuvattu muuttujakohtaisesti.

FOLK Perhe -aineistot ovat kansiossa FOLK_PERH_C, jossa tiedostot ovat jaettuina vuositiedostoihin. Tiedostonimet ovat muodossa folk_perhe_"vuosi"_1.

Aikaisemmin julkaistut FOLK Perhe -aineistotiedostot, jotka sisältävät useita tilastovuosia ovat FIONAssa seuraavissa kansioissa:
Totaaliaineisto vuosille 2011-2020 : FOLK_perh_11a
Totaaliaineisto vuosille 2001-2010 : FOLK_perh_0110a
Totaaliaineisto vuosille 1987-2000 : FOLK_perh_8800a

Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@stat.fi

## Muuttujat / Variables (15)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
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

### Muuttujien määritelmät / Variable definitions

#### `vuosi` — Vuosi

Tilastovuosi

#### `hid_e` — Suojattu henkilön yksilöivä tunniste

Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e -tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä.

#### `petu` — Perheen tunniste

Perheen tunnisteella voidaan liittää yhtenä havaintovuonna saman perheen henkilöt yhteen. Havaintovuosien välillä sama perheen tunniste ei välttämättä tarkoita samaa perhettä eikä muuttuja kerro riippumatonta lapsi-vanhempi suhdetta. Perheen tunniste perustuu TK:n rakennusnumero-huoneistonumero-perhenumero-yhdistelmään, joka voi samalla perheellä vaihdella vuosittain esimerkiksi muuton takia. Muuttujan arvoon vaikuttaa myös poimintavuosi, eli arvo ei ole identtinen vuositiedostojen ja vanhojen, useita vuosia sisältävien tiedostojen välillä.

'00000000' = perheväestöön kuulumaton henkilö, jolla on kuitenkin adpotio/biologinen lapsi.

#### `laplubio` — Henkilön biologisten lasten lukumäärä

**Ryhmä / Group:** Vaestorakenne

Henkilön biologisten lasten lukumäärä, tieto vuodesta 1989 lähtien. Lapsettomille muuttujan arvo on puuttuva vuosina 1987-2004 ja nolla vuodesta 2005 lähtien.

#### `lapluka` — Henkilön kaikkien lasten lukumäärä

**Ryhmä / Group:** Vaestorakenne

Henkilön kaikkien biologisten ja/tai adoptiolasten lukumäärä. Lapsettomille muuttujan arvo on puuttuva vuosina 1987-2004 ja nolla vuodesta 2005 lähtien.

#### `uusper` — Uusperhe

**Ryhmä / Group:** Perhe

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

**Ryhmä / Group:** Perhe

Perheen henkilöiden lukumäärä. Perheväestöön kuuluvilla perheen koko on kaksi tai enemmän, bl = perheväestöön kuulumaton

#### `lkm` — Perheen lasten lukumäärä

**Ryhmä / Group:** Perhe

Perheen lasten lukumäärä, kaikki kotona asuvat biologiset ja ottolapset, ei ikärajaa, bl = perheväestöön kuulumaton

#### `a3lkm` — Perheen alle 3-vuotiaiden lasten lkm

**Ryhmä / Group:** Perhe

Perheen alle 3-vuotiaiden lasten lukumäärä, kotona asuvat kaikki  biologiset ja ottolapset. Tieto vuodesta 2006 lähtien, bl = perheväestöön kuulumaton.

#### `a7lkm` — Perheen alle 7-vuotiaiden lasten lkm

**Ryhmä / Group:** Perhe

Perheen alle 7-vuotiaiden lasten lukumäärä, kotona asuvat kaikki  biologiset ja ottolapset, bl = perheväestöön kuulumaton.

#### `a18lkm` — Perheen alle 18-v. lasten lkm

**Ryhmä / Group:** Perhe

Perheen alle 18-vuotiaiden lasten lukumäärä, kaikki kotona asuvat biologiset ja ottolapset, bl = perheväestöön kuulumaton.

#### `a25lkm` — Perheen alle 25-v. lasten lkm

**Ryhmä / Group:** Perhe

Perheen alle 25-vuotiaiden lasten lukumäärä, kaikki kotona asuvat biologiset ja ottolapset, bl = perheväestöön kuulumaton.

#### `yhta18` — Perheen vanhempien alle 18-v. yhteisten biologisten tai adoptiolasten

**Ryhmä / Group:** Perhe

Uusperheen vanhempien alle 18-vuotiaiden yhteisten biologisten tai adoptiolasten lukumäärä, bl = perheväestöön kuulumaton.

#### `aidina18` — Vain äidin alle 18-v. t lasten lkm

**Ryhmä / Group:** Perhe

Vain äidin alle 18-vuotiaat biologiset tai adoptiolapset. Vuosina 1987-2005 tieto koskee vain uusperheitä, bl = perheväestöön kuulumaton.

#### `isana18` — Vain isän alle 18-v. lasten lkm

**Ryhmä / Group:** Perhe

Vain isän alle 18-vuotiaat biologiset tai adoptiolapset. Vuosina 1987-2005 tieto koskee vain uusperheitä, bl = perheväestöön kuulumaton.

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
