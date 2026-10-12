# INFRA_SIJAINTI Sijaintitiedot

- **Identifier:** `INFRA_19872022_jua_sijainti_001.xml`
- **DOI:** `work_2020-07_2020-07-07_ain_0001`
- **Temporal coverage:** 1987-12-31 - 2025-12-31
- **Published:** 2026-02-27
- **Organisation:** Tilastokeskus
- **Variable count:** 8
- **Observation count:** —
- **Population:** Kunkin vuoden viimeisenä päivänä Suomessa vakituisesti asuva väestö
- **Source:** Digi- ja väestötietoviraston väestötietojärjestelmä. Koostettu henkilötietovaraston henkilö-vuosi- ja rakennus-tauluista.

## Description

INFRA Sijaintimoduuli -aineisto sisältää sijaintitietoja muun muassa kunnan, postinumeroalueen ja neliökilometriruudun mukaan.

<b> Valmisaineiston tarkentava nimi </b> 
Sijaintitiedot henkilötietovarastossa olevista asuinrakennuksista yhdistettynä väestöön kuuluviin asukkaisiin

<b> Aineiston perusjoukko, koostaminen ja tietolähteet </b> 
Aineisto sisältää Tilastokeskuksen henkilötietovarastossa olevien rakennusten sijaintitiedot yhdistettynä asukkaaseen, eli kunkin vuoden viimeisenä päivänä Suomessa vakituisesti asuneeseen väestöön. Tiedot ovat peräisin Digi- ja väestötietoviraston väestötietojärjestelmästä.

<b> Huomioitavaa aineistosta ja sen käytöstä </b> 
Sijaintitietomoduuli on saatavilla tutkimuskäyttöön myös tarkempana versiona, joka sisältää kuvauksessa lueteltujen muuttujien lisäksi 250 m x 250 m ruututunnukset yli kolmen asukkaan ruuduille sekä vähintään kolme vakituisessa asuinkäytössä olevaa huoneistoa sisältävien rivi- ja kerrostalojen koordinaatit. Käyttölupa tarkemman tason versioon edellyttää vahvoja tutkimuksellisia perusteluja.

Rakennusten koordinaattitietoja ei koskaan anneta ulos etäkäyttöjärjestelmästä. Ruututasolle tai muulle aluetasolle aggregoituja tietoja voidaan antaa ulos etäkäyttöjärjestelmästä vain silloin, kun alueella on vähintään 10 henkilöä. Kokonaista ruutuaineistoa ei saa julkaista. Ruutuihin tai muihin maantieteellisiin alueisiin perustuvia tietoja voidaan julkaista silloin, kun yksittäisiä henkilöitä tai asuntokuntia ei voi tunnistaa. Julkaistavien tietojen tulee olla aggregoituja suuremmalle aluetasolle, suhteutettuja, tai muulla tavalla käsiteltyjä siten, että suora ja epäsuora tunnistaminen on estetty.

Tilastovuoden 2025 päivityksen yhteydessä on tehty takautuvia muutoksia päivittämällä suojausta ja lisäämällä pysyvä rakennustunnus -muuttuja (prt).

<b> Aineiston päivitysaikataulu </b>  
Tutustu valmisaineistojen <a href="https://stat.fi/fi/palvelut/palvelut-tutkijoille/tutkimusaineistot/valmisaineistot/valmisaineistojen-paivitysaikataulu">  päivitysaikatauluun</a>. 

<b> Aineiston käyttö ja tilaaminen </b> 
Aineistoa voi käyttää vain FIONA-etäpalvelun kautta. Tiedot ovat linkitettävissä muihin henkilövalmisaineistoihin suojatun henkilönumeron avulla.

Valmisaineiston voi tilata tutkimuksen kohdejoukolle ja tietylle ajanjaksolle.  Kokonaisaineistoon (sisältää kaikki muuttujat koko populaatiolle ja kaikilta saatavissa olevilta vuosilta) myönnetään käyttöoikeus ainoastaan silloin, kun tutkimuksellinen tarve sitä erityisesti edellyttää. Aineiston muuttujia voi tilata myös räätälöitynä tutkimusaineistona, joka sisältää vain osan valmisaineiston muuttujista. 

<b> Lisätietoja </b> 
Lisätietoja Tilastokeskuksen Tutkijapalveluista: tutkijapalvelut@stat.fi

## Variables (8)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `vuosi` | Vuosi | — | — | — |
| `hid_e` | Suojattu henkilön yksiöivä tunniste | — | — | — |
| `kunta` | Kunta | — | — | Vaestorakenne |
| `euref_1000` | 1 km -ruudun tunniste (euref) | — | — | Spatiaalisettiedot |
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
