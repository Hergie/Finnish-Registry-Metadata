# EDUC_OPISK_HIST: Korkeakouluopiskelijoiden historialliset tiedot 1975-1995 2. osamoduuli

- **Identifier:** `EDUC_19751995_jua_000_000.xml`
- **DOI:** `he_2024-08_2024-08-29_ain_0002`
- **Temporal coverage:** 1970-01-01 - 1995-12-31
- **Published:** 2026-03-30
- **Organisation:** Tilastokeskus
- **Variable count:** 33
- **Observation count:** —

## Description

EDUC_OPISK_HIST Korkeakouluopiskelijoiden historialliset tiedot 1975-1995 -moduulin 2. osa perustuu Tilastokeskuksen niin sanottuun kertymätilastoon, jota tuotettiin vuodesta 1975 alkaen. Tämä moduuli sisältää kyseisen kertymätilaston tiedot vuosilta 1975–1995Tämä tiedostomuoto toimi myöhemmin pohjana Tilastokeskuksen laajemmalle opiskelija-taululle (tutkijakäytössä nimeltään Educ_opisk), josta on löydettävissä samantyyppiset tiedot korkeakoulujen opiskelijoista tuoreemmille vuosille.  
  
Moduulin 2.osa sisältää kirjoilla olleet korkeakouluopiskelijat ja heidän korkeakoulutukseensa liittyviä tietoja. Eri luokitukset ovat kyseisen vuoden luokituksia, jollei ole mainittu toisin. Erillinen vuoden 1975 korkeakoulu-tiedekunta-opintosuunta avain löytyy Fionasta.

HUOM 1: Kyseessä on historiatiedosto, jonka kaikkia eri muuttujia ei ole voitu tarkistaa. 
HUOM 2: Kuvaukset  ovat paikoin puutteellisia.

Tiedostosta salataan seuraavat:
Hid, opintokirjan numero (voi olla osalle puuttellinen, koska numeroinissa esiintyy "00000") ja korkeakoulu (korkeakoulusta kaksi eri versiota, 2-numeroinen jokaista vuotta kuvaava vanha TK:n luokitus ja 5-numeroinen oppilaitostunnus 1995 tilanteen mukaan). 

Tiedostosta salataan seuraavat muuttujat:
Henkilön hid-tunniste, opintokirjan numero (voi olla osalle puuttellinen, koska numeroinissa esiintyy "00000") sekä korkeakoulutunnukset.

## Variables (33)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `tun` | Uusi tietueen tunnus | — | — | — |
| `syntymaaika` | Syntymäaika | — | — | — |
| `sukup` | Sukupuoli | — | — | — |
| `kansalaisuus` | Kansalaisuus | — | — | — |
| `kieli` | Äidinkieli | — | — | — |
| `kotikunta` | Kotikunta | — | — | — |
| `klaa` | Kotilääni | — | — | — |
| `yotutk` | Ylioppilastutkinto | — | — | — |
| `pohjav` | Pohjakoulutusväylä | — | — | — |
| `taikavv` | Tilastoaika | — | — | — |
| `taikalk` | Tilastolukukausi | — | — | — |
| `kirtuvv` | Kirjoihintulto kork.kouluun,vuosi | — | — | — |
| `kirtulk` | Kirjoihintulto kork.kouluun, lukukausi | — | — | — |
| `tiekirvv` | Kirjoihintulo tiedekuntaan, vuosi | — | — | — |
| `tiekirlk` | Kirjoihintulo tiedekuntaan, lukukausi | — | — | — |
| `koulk` | Tavoitetutkinnon koulutuskoodi | — | — | — |
| `apuk` | Tavoitetutkinnon koulutuskoodin apukoodi | — | — | — |
| `ilmos` | Ilmoittautumislaji, syksy | — | — | — |
| `ilmok` | Ilmoittautumislaji, kevät | — | — | — |
| `tiedekunta` | Tiedekunta/osasto | — | — | — |
| `opintosuunta` | Opintosuunta/pääaine | — | — | — |
| `optar` | Opintojen tarkoitus/tavoitetutkinto | — | — | — |
| `opkun` | Opiskelupaikkakunta | — | — | — |
| `oplu` | Opiskelun luonne | — | — | — |
| `yleinentiedekunta` | Yleinen tiedekunta | — | — | — |
| `yleinenopintosuunta` | Yleinen opintosuunta | — | — | — |
| `otkkod` | Opiskelu toisessa korkeakolussa, koodi | — | — | — |
| `otkalk` | Opiskelu toisessa korkeakoulussa, aloitusaika | — | — | — |
| `tvuosi` | Tilastovuosi | — | — | — |
| `opkno_s` | Suojattu opintokirjan numero | — | — | — |
| `kkou_s` | Suojattu korkeakoulun 2-numeroinen tunnus | — | — | — |
| `kkou1_s` | Suojattu oppilaitostunnus 5-numeroinen | — | — | — |
| `hid_e` | Suojattu henkilön yksilöivä tunniste | — | — | — |

### Variable definitions

#### `tun` — Uusi tietueen tunnus

0=vanha, 1=uusi

#### `syntymaaika` — Syntymäaika

ppkkvvvv

#### `sukup` — Sukupuoli

1=mies, 2=nainen.

#### `kansalaisuus` — Kansalaisuus

1=suomi, 2=muu

#### `kieli` — Äidinkieli

1=suomi,2=ruotsi,3=muu, 9=tuntematon.

#### `kotikunta` — Kotikunta

Kyseisen tilastovuoden mukainen kuntaluokitus

#### `klaa` — Kotilääni

Kyseisen tilastovuoden mukainen lääniluokitus

#### `yotutk` — Ylioppilastutkinto

1=olen, 2=en, 0 =ei tietoa

#### `pohjav` — Pohjakoulutusväylä

1=ylioppilastutkinto, 2=ammat.koulu, 3=korkeakoulututkinto, 4=muu.

#### `taikavv` — Tilastoaika

VV (vuosi)

#### `taikalk` — Tilastolukukausi

1=kevät, 2=syksy

#### `kirtuvv` — Kirjoihintulto kork.kouluun,vuosi

VV (vuosi)

#### `kirtulk` — Kirjoihintulto kork.kouluun, lukukausi

1=kevät, 2=syksy

#### `tiekirvv` — Kirjoihintulo tiedekuntaan, vuosi

VV (vuosi)

#### `tiekirlk` — Kirjoihintulo tiedekuntaan, lukukausi

1=kevät, 2=syksy

#### `koulk` — Tavoitetutkinnon koulutuskoodi

Koulutuskoodiluokitus 1971-1997

#### `apuk` — Tavoitetutkinnon koulutuskoodin apukoodi

Tavoitetutkinnon koulutuskoodin apukoodi

#### `ilmos` — Ilmoittautumislaji, syksy

1=läsnä, 2=poissa.

#### `ilmok` — Ilmoittautumislaji, kevät

1=läsnä, 2=poissa.

#### `tiedekunta` — Tiedekunta/osasto

KTO-koodisto

#### `opintosuunta` — Opintosuunta/pääaine

KTO-koodisto

#### `optar` — Opintojen tarkoitus/tavoitetutkinto

Muunnettu virkamiestietue.

#### `opkun` — Opiskelupaikkakunta

Kyseisen tilastovuoden mukainen kuntaluokitus

#### `oplu` — Opiskelun luonne

0=varsinainen, 1=ylim, 2=muu, jatko-opisk., 3=mustak, 4=kuuntelu.

#### `yleinentiedekunta` — Yleinen tiedekunta

Yleinen tiedekuntakoodi (TK:n lisäämä)

#### `yleinenopintosuunta` — Yleinen opintosuunta

Yleinen opintosuuntakoodi (TK:n lisäämä)

#### `otkkod` — Opiskelu toisessa korkeakolussa, koodi

1=kyllä, 2=ei

#### `otkalk` — Opiskelu toisessa korkeakoulussa, aloitusaika

vvl (vv=vuosi, l=lukukausi)

#### `tvuosi` — Tilastovuosi

Tiedoston tallennuksen tilastovuosi, lisätty aineistoon

#### `opkno_s` — Suojattu opintokirjan numero

Opintokirjannumero, vain osalle vuosia, osalle 00000. Muuttuja häviää 1977/78

#### `kkou_s` — Suojattu korkeakoulun 2-numeroinen tunnus

Suojattu 2-numeroinen alkuperäinen korkeakoulutunnus

#### `kkou1_s` — Suojattu oppilaitostunnus 5-numeroinen

Suojattu TK:n 5 numeroinen oppilaitostunnus 1995 mukaan

#### `hid_e` — Suojattu henkilön yksilöivä tunniste

Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e -tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä.

---

[← Back to catalogue](../../README.md)
