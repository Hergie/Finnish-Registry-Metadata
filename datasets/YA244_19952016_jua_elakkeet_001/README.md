# FLEED Yhdistetty työntekijä-työnantaja-aineisto, otos, eläkejaksot (YA244)

- **Identifier:** `YA244_19952016_jua_elakkeet_001.xml`
- **DOI:** `tyokay_2012-03_2012-03-01_ain_0001`
- **Temporal coverage:** 1995-01-01 - 2016-12-31
- **Published:** 2019-01-17
- **Organisation:** Tilastokeskus
- **Variable count:** 7
- **Observation count:** —
- **Population:** Työikäinen väestö
- **Source:** Kansaneläkelaitoksen ja Eläketurvakeskuksen rekisterit eläkkeensaajista
- **Related:** <a href= "http://www.stat.fi/til/tyokay/">Työssäkäyntitilasto</a> <a href= "http://www.stat.fi/meta/rekisteriselosteet/tutka_rekisteriseloste_yhdistetty_tyontekija_tyonantaja_aineisto_otos_elakejaksot.html">Yhdistetty työntekijä-työnantaja-aineisto (FLEED), otos, eläkejaksot</a>
- **Keywords:** eläkeläiset,eläkkeelle siirtyminen,eläkkeet,kansaneläkkeet,työeläkkeet

## Description

<b>FLEED-aineiston päivitykset päättyvät</b>

Tilastokeskuksen tutkijapalveluiden FOLK-moduulien käyttöönoton myötä FLEED-aineistokokonaisuuden päivitykset päättyvät. FLEED-aineistoon on päivitetty tilastovuoden 2016 tiedot. FLEED-jaksotiedot (eläke-, työsuhde-, työttömyys-, työnhaku-, työvoimakoulutus- ja toimenpidesijoitusjaksot) muuttuvat vastaaviksi FOLK-moduuleiksi. Hankkeissa, joiden käyttölupa FLEED-aineistoon jatkuu päivitysten päättymisen jälkeen, on mahdollista saada käyttöön vastaavat tiedot FOLK-moduuleista. FOLK-moduulien kuvaukset löytyvät TAIKA-tutkimusaineistokatalogista. Tutkijapalvelut on ollut yhteydessä nykyisiin FLEED-valmisaineiston käyttäjiin mahdollisesta käyttöluvan päivittämisestä ja siirtymisestä FOLK-aineiston käyttöön.

<b> FLEED Eläkejaksot </b>
Eläkejaksot yhdistetyn työntekijä-työnantaja-aineiston (Finnish Longitudinal Employer-Employee Data FLEED) otoksen henkilöille.  FLEED kattaa tiedot kaikista 15–70-vuotiaista suomalaisista sekä kaikista Suomen yrityksistä. FLEED-otos on totaaliaineiston henkilöistä poimittu 1/3 satunnaisotos. Tietoja vuodesta 1995 alkaen kunkin vuoden lopun tilanteen mukaan (sisältää vain vuoden lopussa voimassa olleet eläkkeet). 

Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@tilastokeskus.fi

## Variables (7)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `vuosi` | Tilastovuosi | — | vuosi_1_2011_07_01 | — |
| `elakelaji_alkuper` | Eläkelaji (alkuperäinen) | — | — | Eläkerekisterit |
| `aineisto` | Aineisto | — | — | Eläkerekisterit |
| `elakelaji` | Eläkelaji | — | elakelaji_1_99_s | Eläkerekisterit |
| `alkupvm_elakejakso` | Eläkejakson alkamispäivämäärä | — | — | Eläkerekisterit |
| `alkupvm_elakelaji` | Eläkelajin alkamispäivä | — | — | Eläkerekisterit |
| `shnro` | Suojattu Tilastokeskuksen henkilönumero | — | — | — |

### Variable definitions

#### `vuosi` — Tilastovuosi

**Classification:** vuosi_1_2011_07_01

Tilastovuosi on se kalenterivuosi, jota tilasto koskee.

#### `elakelaji_alkuper` — Eläkelaji (alkuperäinen)

**Group:** Eläkerekisterit

Alkuperäisen aineiston eläkelaji, josta muodostetaan muuttuja 'eläkelaji'.

#### `aineisto` — Aineisto

**Group:** Eläkerekisterit

Tieto eläkkeiden lähtöaineistosta.
31 = Kansaneläkkeet 1995-2002
32 = Työeläkkeet 1995-2002
33 = Kansaneläkkeet, taannehtivat 1995-
34 = Työeläkkeet, taannehtivat 1996-
35 = Työ- ja kansaneläkkeet, yhteistilastoaineisto 2003-

#### `elakelaji` — Eläkelaji

**Classification:** elakelaji_1_99_s · **Group:** Eläkerekisterit

Muodostetaan Tilastokeskuksessa alkuperäisen aineiston koodistosta alla olevan luokituksen mukaisiksi:
1 = Vanhuuseläke
2 = Työkyvyttömyyseläke
3 = Yksilöllinen varhaiseläke
4 = Työttömyyseläke
5 = Maatalouden erityiseläke
6 = Osa-aikaeläke
7 = Perhe-eläke
9 = Takuueläke (v.2011 alkaen)

#### `alkupvm_elakejakso` — Eläkejakson alkamispäivämäärä

**Group:** Eläkerekisterit

Koko eläkkeelläolojakson alkamisaika eli se päivä, jolloin henkilö jäi eläkkeelle. Eläkkeelläolojaksolla tarkoitetaan yhtenäistä eläkkeellä oloa. Jos eläkkeessä on välillä aito katkos (esimerkiksi määräaikaisen eläkkeen päättymisen jälkeen), alkuperäinen alkamisaika siirtyy katkoksen jälkeen alkavan eläkkeen alkamispäivään. Esimerkiksi jos henkilö jää työkyvyttömyyseläkkeelle, joka sitten jatkuu vanhuuseläkkeenä ikärajan täyttymisen jälkeen, alkupvm_elakejakso kertoo koko eläkeajan alkamisen ja alkupvm_elakelaji vanhuuseläkkeen alkamisen. Osa-aikaeläke on aina erikseen eli sen jälkeen alkavan eläkkeen alkamispäivä ja alkuperäinen alkamispäivä ovat aina samat.

#### `alkupvm_elakelaji` — Eläkelajin alkamispäivä

**Group:** Eläkerekisterit

Nykyisen eläkelajin alkamispäivä eli se päivä, jolloin nykyisen eläkelajin mukainen eläke alkoi. Tieto on mahdollista saada vain työeläkkeille (ETK). Tietoja ei ole toistaiseksi saatavilla millekään vuodelle.

#### `shnro` — Suojattu Tilastokeskuksen henkilönumero

Suojattu Tilastokeskuksen henkilönumero.

---

[← Back to catalogue](../../README.md)
