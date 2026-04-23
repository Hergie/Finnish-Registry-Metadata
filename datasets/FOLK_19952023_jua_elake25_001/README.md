# FOLK jaksotiedot: eläke

- **Identifier:** `FOLK_19952023_jua_elake25_001.xml`
- **DOI:** `tyokay_2012-03_2012-03-01_ain_0001`
- **Temporal coverage:** 1995-01-01 - 2023-12-31
- **Published:** 2025-12-22
- **Organisation:** Tilastokeskus
- **Variable count:** 7
- **Observation count:** —
- **Source:** Kansaneläkelaitoksen ja Eläketurvakeskuksen rekisterit eläkkeensaajista
- **Keywords:** eläkeläiset,eläkkeelle siirtyminen,eläkkeet,kansaneläkkeet,työeläkkeet

## Description

Sisältyy FOLK jaksotiedot -moduuliin. Tietoja eläkkeistä vuodesta 1995 alkaen kunkin vuoden lopun tilanteen mukaan (sisältää vain vuoden lopussa voimassa olleet eläkkeet). 

Jos henkilöllä on ollut voimassa useampia saman eläkelajin jaksoja (elakelaji_alkuper) yhden aineistolähteen sisällä, on henkilölle otettu mukaan jakso, jonka alkamisajankohta on varhaisin. Perhe-eläkkeet ovat mukana vuodesta 1996 lähtien. Takautuvasti myönnetyt työeläkkeet puuttuvat vuosilta 1995 ja 1998. 

Eläketietoja on myös saatavilla TAX_BENEFIT Tulorekisterin etuustiedot -moduulista. 

Viimeisimmät FOLK JAKSO: eläke -aineistot ovat kansiossa FOLK_JAKSOT_C/ELAKE, jossa tiedostot on jaettuna tilastovuosittain. Tiedostonimet ovat muodossa folk_elake_"vuosi"_1.

Vanhat eläkejakso-aineistot ovat FIONAssa kansiossa: FOLK_jaksot_a. 

Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@tilastokeskus.fi

Muutoksia vuoden 2023 aineistossa:
- Vuodesta 2023 alkaen aineisto on tulorekisteripohjainen
- Elakelaji_alkuper muuttujaa ei enää päivitetä vuodesta 2022 eteenpäin, johtuen tulorekisterisiirtymästä
- Eläkelajit mukailevat ETK-datan mukaisia eläkelajeja ja uutena eläkelajina eläkelaji = 8 = Muut eläkkeet
- Jatkossa uusille eläkeläisille otetaan vain minimiarvo alkupäivämääristä ja se pysyy muuttumattomana. ETK:n datassa otettiin "aidot katkokset" huomioon, mutta tulorekisterin datassa tätä ei oteta huomioon vuodesta 2023 eteenpäin.

## Variables (7)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `vuosi` | Vuosi | — | — | — |
| `hid_e` | Suojattu henkilön yksilöivä tunniste | — | — | Vaestorakenne |
| `elakelaji_alkuper` | Eläkelaji (alkuperäinen) | — | elakelaji_3_2017_01_01 | Eläke |
| `aineisto` | Aineisto | — | — | Eläke |
| `elakelaji` | Eläkelaji | — | — | Eläke |
| `alkupvm_elakejakso` | Eläkejakson alkamispäivämäärä | — | — | Eläke |
| `alkupvm_elakelaji` | Eläkelajin alkamispäivämäärä | — | — | Eläke |

### Variable definitions

#### `vuosi` — Vuosi

Tilastovuosi.

#### `hid_e` — Suojattu henkilön yksilöivä tunniste

**Group:** Vaestorakenne

Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e -tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä.

#### `elakelaji_alkuper` — Eläkelaji (alkuperäinen)

**Classification:** elakelaji_3_2017_01_01 · **Group:** Eläke

Alkuperäisen aineiston eläkelaji, josta muodostetaan muuttuja 'eläkelaji'. 

Huom. Muuttujaa ei ylläpidetä enää tilastovuodesta 2023 alkaen.

Huom. taannehtivista eläkkeistä puuttuu takuueläke - eli jos takuueläke on myönnetty henkilölle taannehtivasti, tapaus ei ole mukana kyseisen vuoden taannehtivien eläkkeiden aineistossa (henkilö voi kuitenkin olla mukana aineistossa, jos on saanut jotakin muuta eläkettä).

0 = Täysi työkyvyttömyyseläke (aineisto 35)	
A = Työuraeläke (v.2018 alkaen) (aineisto 35)	
0K = Kuntoutustuki (aineisto 35)	
0R = Kunnallinen erotuseläke (aineisto 35)	
0Y = Yksilöllinen varhaiseläke (aineisto 35)	
1 = Osa-aikaeläke (aineisto 35)	
10 = Muu työkyvyttömyyseläke (aineisto 35)	
11 = Varsinainen vanhuuseläke (aineisto 33) | Varsinainen työkyvyttömyyseläke (aineisto 34)	
12 = Lykätty vanhuuseläke (RAKE-tapauksilla) (aineisto 33) | Määräaikainen työkyvyttömyyseläke (aineisto 34)	
13 = Varhennettu vanhuuseläke (aineisto 33) | Kuntoutustuki (aineisto 34)	
15 = Yksilöllinen varhaiseläke (aineisto 34)	
16 = Osatyökyvyttömyyseläkkeen suuruinen yksilöllinen varhaiseläke (aineisto 34)	
2 = Osatyökyvyttömyyseläke (aineisto 35)	
20 = Toistaiseksi myönnetty työkyvyttömyyseläke (aineisto 33) | Muu osatyökyvyttömyyseläke (aineisto 34)	
21 = Osatyökyvyttömyyseläke (aineisto 34)	
22 = Määräaikainen osatyökyvyttömyyseläke (aineisto 34)	
23 = Toistaiseksi myönnetty työkyvyttömyyseläke (aineisto 33) | Osakuntoutustuki (aineisto 34)	
2K = Osakuntoutustuki (aineisto 35)	
2Y = Osatyökyvyttömyyseläkkeen suuruinen yksilöllinen varhaiseläke (aineisto 35)	
30 = Määräaikainen työkyvyttömyyseläke (aineisto 33)	
33 = Määräaikainen työkyvyttömyyseläke (aineisto 33) | Rintamaveteraanien varhaiseläke (aineisto 34)	
4 = Työttömyyseläke (aineisto 35)	
40 = Työttömyyseläke (aineisto 34)	
45 = Osa-aikaeläke (aineisto 34)	
5 = Vanhuuseläke (aineisto 35)	
50 = Varsinainen vanhuuseläke (aineisto 34)	
51 = Varhennettu vanhuuseläke (aineisto 34)	
52 = Osittainen varhennettu vanhuuseläke, 25 % (aineisto 35)	
55 = Osittainen varhennettu vanhuuseläke, 50 % (aineisto 35)	
5A = Varhennettu vanhuuseläke (aineisto 35)	
6 = Luopumiseläke (aineisto 35)	
60 = Luopumiseläke (aineisto 34)	
61 = Luopumiskorvaus (aineisto 34)	
62 = Luopumislisä (aineisto 34)	
6A = Luopumiskorvaus (aineisto 35)	
6M = Luopumislisä (vanhuuseläkkeen rinnalla) (aineisto 35)	
7 = MYEL-sukupolvevaihdoseläke (aineisto 35)	
70 = Työttömyyseläke (aineisto 33) | MYEL-sukupolvevaihdoseläke tai SpvL:n mukainen sukupolvenvaihdoseläke (aineisto 34)	
73 = Luopumistuki (aineisto 34)	
7A = SpvL:n mukainen sukupolvenvaihdoseläke (aineisto 35)	
7B = Luopumistuki (aineisto 35)	
80 = Yksilöllinen varhaiseläke (aineisto 33) | Muu perhe-eläkkeen edunsaaja (aineisto 34)	
81 = Perhe-eläke / leski (aineisto 35)	
82 = Perhe-eläke / lapsi (aineisto 35)	
83 = Perhe-eläke / muu edunsaaja (aineisto 35) | Leskeneläke, vanha laki (aineisto 34)	
84 = Lapseneläke, vanha laki (aineisto 34)	
85 = Entisen puolison eläke, vanha laki (aineisto 34)	
86 = Leskeneläke, uusi laki (aineisto 34)	
87 = Lapseneläke, uusi laki (aineisto 34)	
88 = Entisen puolison eläke, uusi laki (aineisto 34)	
90 = Takuueläke (v. 2011 alkaen) (aineisto 35)	
95 = Takuueläke (aineisto 33)

#### `aineisto` — Aineisto

**Group:** Eläke

Tieto eläkkeiden lähtöaineistosta: 
31 = Kansaneläkkeet 1995-2002 
32 = Työeläkkeet 1995-2002 
33 = Kansaneläkkeet, taannehtivat 1995-2019 
34 = Työeläkkeet, taannehtivat 1996- 
35 = Työ- ja kansaneläkkeet, yhteistilastoaineisto 2003-

#### `elakelaji` — Eläkelaji

**Group:** Eläke

Muodostetaan Tilastokeskuksessa alkuperäisen aineiston koodistosta alla olevan luokituksen mukaisiksi:
1 = Vanhuuseläke 
2 = Työkyvyttömyyseläke 
3 = Yksilöllinen varhaiseläke 
4 = Työttömyyseläke 
5 = Maatalouden erityiseläke 
6 = Osa-aikaeläke 
7 = Perhe-eläke 8= Muut eläkkeet (v. 2023 alkaen) 
9 = Takuueläke (v. 2011 alkaen)

#### `alkupvm_elakejakso` — Eläkejakson alkamispäivämäärä

**Group:** Eläke

Koko eläkkeelläolojakson alkamisaika eli se päivä, jolloin henkilö jäi eläkkeelle. Eläkkeelläolojaksolla tarkoitetaan yhtenäistä eläkkeellä oloa. Jos eläkkeessä on välillä aito katkos (esimerkiksi määräaikaisen eläkkeen päättymisen jälkeen), alkuperäinen alkamisaika siirtyy katkoksen jälkeen alkavan eläkkeen alkamispäivään. Esimerkiksi jos henkilö jää työkyvyttömyyseläkkeelle, joka sitten jatkuu vanhuuseläkkeenä ikärajan täyttymisen jälkeen, alkupvm_elakejakso kertoo koko eläkeajan alkamisen ja alkupvm_elakelaji vanhuuseläkkeen alkamisen. Osa-aikaeläke on aina erikseen eli sen jälkeen alkavan eläkkeen alkamispäivä ja alkuperäinen alkamispäivä ovat aina samat.

#### `alkupvm_elakelaji` — Eläkelajin alkamispäivämäärä

**Group:** Eläke

Alkuperäisen eläkelajin alkupäivämäärä. Tieto päivitetty ainoastaan aineistokoodille 35. Tietoja vuodesta 2015 lähtien.

---

[← Back to catalogue](../../README.md)
