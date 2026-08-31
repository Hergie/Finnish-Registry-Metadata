# INFRA_SIJAINTI_TARKKA Sijaintitiedot tarkka

- **Identifier:** `INFRA_19872025_jua_sijaintitarkka_001.xml`
- **DOI:** `work_2026-07_2026-07-20_ain_0001`
- **Temporal coverage:** 1987-12-31 - 2025-12-31
- **Published:** 2026-07-20
- **Organisation:** Tilastokeskus
- **Variable count:** 9
- **Observation count:** —
- **Source:** Digi- ja väestöviraston väestötietojärjestelmä. Koostettu henkilötietovaraston henkilö-vuosi- ja rakennus-tauluista.

## Description

INFRA_SIJAINTI-valmisaineisto sisältää Tilastokeskuksen henkilötietovarastossa olevien rakennusten sijaintitiedot yhdistettynä asukkaaseen, eli kunkin vuoden viimeisenä päivänä Suomessa vakituisesti asuneeseen väestöön. Aineistosta on olemassa kaksi versiota, INFRA_SIJAINTI ja INFRA_SIJAINTI_TARKKA, joilla on molemmilla oma aineistokuvauksensa.

Tämä aineistokuvaus koskee aineiston tarkempaa versiota, joka sisältää 250m x 250m ruututunnukset yli kolmen asukkaan ruuduille sekä vähintään kolme huoneistoa sisältävien rakennusten koordinaatit. Käyttölupa tarkemman tason versioon edellyttää vahvoja tutkimuksellisia perusteluja.

Rakennusten koordinaattitietoja ei koskaan anneta ulos etäkäyttöjärjestelmästä. Ruututasolle tai muulle aluetasolle aggregoituja tietoja voidaan antaa ulos etäkäyttöjärjestelmästä vain silloin, kun alueella on vähintään 10 henkilöä. Kokonaista ruutuaineistoa ei saa julkaista. Ruutuihin tai muihin maantieteellisiin alueisiin perustuvia tietoja voidaan julkaista silloin, kun yksittäisiä henkilöitä tai asuntokuntia ei voi tunnistaa. Julkaistavien tietojen tulee olla aggregoituja suuremmalle aluetasolle, suhtautettuja, tai muulla tavalla käsiteltyjä siten, että suora ja epäsuora tunnistaminen on estetty.

Tilastovuoden 2025 päivityksen yhteydessä on tehty takautuvia muutoksia päivittämällä suojausta ja lisäämällä pysyvä rakennustunnus -muuttuja (prt).

Lisätietoja Tilastokeskuksen Tutkijapalveluista: tutkijapalvelut@stat.fi.

## Variables (9)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `vuosi` | Vuosi | — | — | — |
| `hid_e` | Suojattu henkilön yksiöivä tunniste | — | — | — |
| `kunta` | Kunta | — | — | Vaestorakenne |
| `euref_1000` | 1 km -ruudun tunniste (euref) | — | — | Spatiaalisettiedot |
| `euref_250` | 250 m -ruudun tunniste (euref) | — | — | spatiaalisettiedot |
| `posti_alue` | Rakennuksen tilastollinen postinumeroalue | — | — | Spatiaalisettiedot |
| `rnro_s` | Suojattu rakennusnumero | — | — | — |
| `prt_s` | Suojattu pysyvä rakennustunnus | — | — | — |
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

#### `euref_250` — 250 m -ruudun tunniste (euref)

**Group:** spatiaalisettiedot

250 m ruudun (hilaruudukko) tunnus EUREF-FIN-koordinaatistossa (ERTS89-TM35FIN).

#### `posti_alue` — Rakennuksen tilastollinen postinumeroalue

**Group:** Spatiaalisettiedot

Tilastollinen postinumeroaluetieto on spatiaalisesti määritelty käyttäen Tilastokeskuksessa ylläpidettävää tilastolliset postinumeroalueet kartta-aineistoa. Tuntematon arvo on merkitty koodilla 99999.

#### `rnro_s` — Suojattu rakennusnumero

Suojattu rakennusnumero korvaa kullekin rakennukselle tietokantaan lisäyksen yhteydessä annetun yksilöivän numeron.

#### `prt_s` — Suojattu pysyvä rakennustunnus

Pysyvä rakennustunnus yksilöi rakennuksen ja se säilyy rakennuksella koko rakennuksen elinkaaren ajan. Pysyvä rakennustunnus on otettu käyttöön VTJ-tietojärjestelmässä 10.11.2014. Tätä aiemmat tiedot on täydennetty henkilötietovaraston rnro:n mukaisesti.

#### `rappu_s` — Suojattu rappukäytävän tunnus

Rakennuskohtainen suojattu rapputunnus on vain asutuilla kerros- ja rivitalohuoneistoilla vuodesta 2005 alkaen. Tieto puuttuu, jos rakennuksessa on vähemmän kuin kolme asuttua huoneistoa.

---

[← Back to catalogue](../../README.md)
