# INFRA Sijaintitietomoduuli

- **Identifier:** `INFRA_19872022_jua_sijainti_001.xml`
- **DOI:** `work_2020-07_2020-07-07_ain_0001`
- **Temporal coverage:** 1987-12-31 - 2024-12-31
- **Published:** 2026-02-27
- **Organisation:** Tilastokeskus
- **Variable count:** 7
- **Observation count:** —
- **Source:** Digi- ja väestötietoviraston väestötietojärjestelmä. Koostettu henkilötietovaraston henkilö-vuosi- ja rakennus-tauluista.

## Description

INFRA Sijaintitietomoduuli sisältää Tilastokeskuksen henkilötietovarastossa olevien rakennusten sijaintitiedot yhdistettynä asukkaaseen, eli kunkin vuoden viimeisenä päivänä Suomessa vakituisesti asuneeseen väestöön. 

Sijaintitietomoduuli on saatavilla tutkimuskäyttöön myös tarkempana versiona, joka sisältää kuvauksessa lueteltujen muuttujien lisäksi 250m x 250m ruututunnukset yli kolmen asukkaan ruuduille sekä vähintään kolme vakituisessa asuinkäytössä olevaa huoneistoa sisältävien rivi- ja kerrostalojen koordinaatit. Käyttölupa tarkemman tason versioon edellyttää vahvoja tutkimuksellisia perusteluja. 

Rakennusten koordinaattitietoja ei koskaan anneta ulos etäkäyttöjärjestelmästä. Ruututasolle tai muulle aluetasolle aggregoituja tietoja voidaan antaa ulos etäkäyttöjärjestelmästä vain silloin, kun alueella on vähintään 10 henkilöä. Kokonaista ruutuaineistoa ei saa julkaista. Ruutuihin tai muihin maantieteellisiin alueisiin perustuvia tietoja voidaan julkaista silloin, kun yksittäisiä henkilöitä tai asuntokuntia ei voi tunnistaa. Julkaistavien tietojen tulee olla aggregoituja suuremmalle aluetasolle, suhtautettuja, tai muulla tavalla käsiteltyjä siten, että suora ja epäsuora tunnistaminen on estetty.

Lisätietoja Tilastokeskuksen Tutkijapalveluista: tutkijapalvelut@stat.fi

## Variables (7)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `vuosi` | Vuosi | — | — | — |
| `hid_e` | Suojattu henkilön yksiöivä tunniste | — | — | — |
| `kunta` | Kunta | — | — | Vaestorakenne |
| `euref_1000` | 1 km -ruudun tunniste (euref) | — | — | Spatiaalisettiedot |
| `posti_alue` | Tilastollinen postinumeroalue | — | — | Spatiaalisettiedot |
| `rnro_s` | Suojattu rakennusnumero | — | — | — |
| `rappu_s` | Suojattu rappukäytävän tunnus | — | — | — |

### Variable definitions

#### `vuosi` — Vuosi

Tilastovuosi

#### `hid_e` — Suojattu henkilön yksiöivä tunniste

Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e -tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä.

#### `kunta` — Kunta

**Group:** Vaestorakenne

Henkilön asuinkunta vuoden viimeisenä päivänä. Alueluokitus on 1.1. tilastovuosi + 1 vuodesta 1999 lähtien. Tätä ennen aluejako on ollut 1.1. tilastovuosi. Kuntanumero 3 merkkiä.

#### `euref_1000` — 1 km -ruudun tunniste (euref)

**Group:** Spatiaalisettiedot

1 neliökilometriruudun (hilaruudukko) tunnus EUREF-FIN-koordinaatistossa (ETRS89-TM35FIN). Vastaa avoimen Tilastoruudukko 1 km x 1 km -paikkatietoaineiston muuttujaa 'nro'.

#### `posti_alue` — Tilastollinen postinumeroalue

**Group:** Spatiaalisettiedot

Tilastollinen postinumeroaluetieto on spatiaalisesti määritelty käyttäen Tilastokeskuksessa ylläpidettävää tilastolliset postinumeroalueet kartta-aineistoa.

#### `rnro_s` — Suojattu rakennusnumero

Suojattu rakennusnumero korvaa kullekin rakennukselle tietokantaan lisäyksen yhteydessä annetun yksilöivän numeron.

#### `rappu_s` — Suojattu rappukäytävän tunnus

Rakennuskohtainen suojattu rapputunnus on vain asutuilla kerros- ja rivitalohuoneistoilla vuodesta 2005 alkaen. Tieto puuttuu, jos rakennuksessa on vähemmän kuin kolme asuttua huoneistoa.

---

[← Back to catalogue](../../README.md)
