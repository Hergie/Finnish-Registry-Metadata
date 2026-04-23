# FOLK tutkinto

- **Identifier:** `FOLK_19872024_jua_tutk26_001.xml`
- **DOI:** `work_2017-08_2017-08-21_ain_0001`
- **Temporal coverage:** 1987-12-31 - 2024-12-31
- **Published:** 2026-02-02
- **Organisation:** Tilastokeskus
- **Variable count:** 22
- **Observation count:** —
- **Population:** Tutkinnon suorittanut väestö
- **Source:** Tutkintorekisteri

## Description

FOLK-henkilöaineiston tutkintomoduuli sisältää 15 vuotta täyttäneen väestön peruskoulun, keskikoulun tai kansakoulun jälkeen suorittamien tutkintojen tietoja. Tietojen lähteenä on tutkintorekisteri. Moduulin tietoja on saatavilla vuodesta 1987 eteenpäin, jollei muuttujankuvauksessa toisin mainita. 

Aineisto on tarkoitettu FIONA-etäpalvelun kautta käytettäväksi. FOLK tutkinto -kokonaisaineistoon voidaan antaa käyttöoikeus vain jos tutkimuksellisesta syystä kokonaisaineiston käyttöön on erityinen tarve. Tiedot on linkitettävissä muiden henkilövalmisaineistomoduulien kanssa suojatun henkilönumeron sekä suojatun oppilaitostunnuksen avulla. 

Tutkintorekisterin tietoja on saatavilla myös EDUC_TREK Tutkintorekisteri -moduulista. 

Viimeisimmät FOLK tutkinto -aineistot ovat kansiossa FOLK_TUTK_C, jossa tiedostot on jaettuna tilastovuosittain. Tiedostonimet ovat muodossa folk_tutk_"vuosi"_1. 

FOLK tutkinto -aineistot ovat FIONAssa seuraavista kansioista: 
Totaaliaineisto vuosille 2011-2019 : FOLK_tutk_11a
Totaaliaineisto vuosille 2001-2010 : FOLK_tutk_0110a
Totaaliaineisto vuosille 1987-2000 : FOLK_tutk_8800a

Lisätietoja Tilastokeskuksen tutkijapalveluista: tutkijapalvelut@tilastokeskus.fi

## Variables (22)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `vuosi` | Tilastovuosi | — | — | — |
| `hid_e` | Suojattu henkilön yksilöivä tunniste | — | — | — |
| `koulk` | Korkeimman tutkinnon koulutuskoodi | — | — | — |
| `kaste` | Korkeimman tutkinnon kansallinen koulutusaste | — | — | — |
| `ISCED_ala3` | Korkeimman tutkinnon ISCED koulutusala, taso III | — | — | — |
| `saika` | Korkeimman tutkinnon suoritusaika | — | — | — |
| `kirtuv` | Aloittamisvuosi/kirjoihintulovuosi | — | — | — |
| `kirtulk` | Aloittamislukukausi | — | — | — |
| `oltunn_s` | Suojattu oppilaitostunnus | — | — | — |
| `sijkun` | Oppilaitoksen sijaintikunta | — | — | — |
| `opty` | Oppilaitostyyppi | — | — | — |
| `opkieli` | Opetuskieli | — | — | — |
| `oppiso` | Oppisopimuskoulutus | — | — | — |
| `ulkom` | Tutkinto suoritettu ulkomailla | — | — | — |
| `ktutk_1` | Tuorein muu tutkinto | — | — | — |
| `suorv_1` | Suoritusvuosi, tuorein muu tutkinto | — | — | — |
| `ktutk_2` | Toiseksi tuorein muu tutkinto | — | — | — |
| `suorv_2` | Suoritusvuosi, toiseksi tuorein muu tutkinto | — | — | — |
| `ktutk_3` | Kolmanneksi tuorein muu tutkinto | — | — | — |
| `suorv_3` | Suoritusvuosi, kolmanneksi tuorein muu tutkinto | — | — | — |
| `ktutk_4` | Neljänneksi tuorein muu tutkinto | — | — | — |
| `suorv_4` | Suoritusvuosi, neljänneksi tuorein muu tutkinto | — | — | — |

### Variable definitions

#### `vuosi` — Tilastovuosi

Tilastovuosi

#### `hid_e` — Suojattu henkilön yksilöivä tunniste

Tilastokeskuksessa muodostettu suojattu henkilön yksilöivä tunniste, joka on sama kaikissa henkilövalmisaineistoissa. Yhtenäisesti suojattu hid_e -tunnus mahdollistaa henkilöä koskevien tietojen yhdistämisen eri vuosien ja aineistojen välillä.

#### `koulk` — Korkeimman tutkinnon koulutuskoodi

TK:n uusimman koulutusluokituksen mukainen 6-numeroinen koulutuskoodi.

Tiedot pohjautuvat Tilastokeskuksen tutkintorekisteriin.  Tutkintorekisterin perustana on vuoden 1970 väestölaskennassa kerätyt tutkintotiedot. Vuosittain päivitettävät tiedot saadaan suoraan koulutuksen järjestäjiltä tai valtakunnallisista KOSKI- ja VIRTA-tietovarannoista.

Rekisteri on kattava Suomessa suoritetuista tutkinnoista, mutta alipeittoinen ulkomailla suoritetuista tutkinnoista. Suomeen muuttavilta henkilöiltä ei kysytä ulkomailla suoritetusta koulutuksesta maahan saapumisen yhteydessä. Tutkintorekisteriin lisätään Valviran rekisteritietoja ulkomailla suoritetuista ja Suomessa laillistetuista terveydenhuollon tutkinnoista, Pohjoismaiden tilastovirastoilta saatuja tutkintotietoja sekä erilliskyselyillä kerättyjä tutkintotietoja.

#### `kaste` — Korkeimman tutkinnon kansallinen koulutusaste

Korkein tutkinto luokituksena kansallinen koulutusaste 2016, taso 2.  
Kansallisen koulutusasteen taso 1 on sama kuin ISCED 2011 -luokituksessa. Tämän aste-koodin saa KOULK-tiedon ensimmäisestä merkistä.
3 Toinen aste 
31 Lukiokoulutus 
32 Ammatillinen peruskoulutus 
33 Ammattitutkinto 
4 Erikoisammattikoulutusaste 
41 Erikoisammattitutkinto 
5 Alin korkea-aste 
51 Opistoaste 
52 Alimman korkea-asteen koulutus 
6 Alempi korkeakouluaste 
61 Ammatillinen korkea-aste 
62 Ammattikorkeakoulututkinto 
63 Alempi korkeakoulututkinto
69 Muu tai tuntematon alemman korkeakouluasteen koulutus
7 Ylempi korkeakouluaste 
71 Ylempi ammattikorkeakoulututkinto 
72 Ylempi korkeakoulututkinto 
73 Lääkärien erikoistumiskoulutus 
79 Muu tai tuntematon ylemmän korkeakouluasteen koulutus
8 Tutkijakoulutusaste 
81 Lisensiaatintutkinto 
82 Tohtorintutkinto 
9 Koulutusaste tuntematon 
91 Koulutusaste tuntematon

#### `ISCED_ala3` — Korkeimman tutkinnon ISCED koulutusala, taso III

Korkein tutkinto ISCED 2011- koulutusalaluokituksella, neljä merkkiä.
ISCED 2011 koulutusalaluokituksen (Unesco ISCED Fields of Education and Training 2013) kolmas ja tarkin taso (detailed ISCED field). Koulutusalan taso 1 (broad field) on 2-numeroinen, taso 2 (narrow field) 3-numeroinen ja taso 3 (detailed fied) 4-numeroinen. Kansallisen koulutusluokituksen kaikki tasot 1-3 ovat samat kuin ISCED 2011 -luokituksessa.

ISCED 2011 koulutusalaluokituksen pääluokat:
00	Yleissivistävä koulutus
01	Kasvatusalat
02	Humanistiset ja taidealat
03	Yhteiskunnalliset alat
04	Kauppa, hallinto ja oikeustieteet
05	Luonnontieteet
06	Tietojenkäsittely ja tietoliikenne (ICT)
07	Tekniikan alat
08	Maa- ja metsätalousalat
09	Terveys- ja hyvinvointialat
10	Palvelualat
99	Muut tai tuntemattomat koulutusalat

#### `saika` — Korkeimman tutkinnon suoritusaika

Korkeimman tutkinnon suoritusvuosi ja -kuukausi, merkkimuotoinen (VVVVKK).
BBBBBB = puuttuva tieto.

#### `kirtuv` — Aloittamisvuosi/kirjoihintulovuosi

Vuosi, jolloin opiskelija on ottanut vastaan opiskelu- oikeuden ja ilmoittautunut koulun kirjoihin tai solminut oppisopimuksen. Merkkimuotoinen vuositieto (VVVV) on vuoden 1999 jälkeen suoritetuista tutkinnoista, muutoin BBBB = ei tietoa.

#### `kirtulk` — Aloittamislukukausi

Tutkintooon johtavan koulutuksen aloittamislukukausi oppilaitoksessa 
1 = kevät (1.1.-31.7.) 
2 = syksy (1.8.-31.12.) 
B = ei tietoa. 
Tieto on vuoden 1999 jälkeen suoritetuista tutkinnoista.

#### `oltunn_s` — Suojattu oppilaitostunnus

Suojattu oppilaitostunnus on suorittamisvuoden luokituksen mukainen.

#### `sijkun` — Oppilaitoksen sijaintikunta

Koulutuksen sijaintikunta tutkinnon suorittamisvuonna Väestörekisterikeskuksen kuntakoodina v.1971 alkaen. 
V. 2006 alkaen ylioppilastutkinnoilla on oppilaitoksen sijaintikunta eikä koulutuksen sijaintikunta. 
200 = ulkomailla 
BBB = tuntematon (999)

#### `opty` — Oppilaitostyyppi

Oppilaitoksen tuorein tieto oppilaitostyypistä
15 = Lukiot 
19 = Perus- ja lukioasteen koulut 
21 = Ammatilliset oppilaitokset 
22 = Ammatilliset erityisoppilaitokset 
23 = Ammatilliset erikoisoppilaitokset 
24 = Ammatilliset aikuiskoulutuskeskukset 
28 = Palo-, poliisi- ja vartiointialojen oppilaitokset 
29 = Sotilasalan ammatilliset oppilaitokset 
41 = Ammattikorkeakoulut 
42 = Yliopistot 
61 = Musiikkioppilaitokset 
62 = Liikunnan koulutuskeskukset 
63 = Kansanopistot 
64 = Kansalaisopistot 
99 = Muut oppilaitokset 
BB = tuntematon

#### `opkieli` — Opetuskieli

Koulutuksen opetuskieli, Koski-rekisterin 2-kirjaiminen tunnus. 
EN /en= englanti
FI /fi = suomi
SV /sv =  ruotsi
de  = saksa
et  = viro
fr  = ranska
ru = venäjä
se  = pohjoissaame
00 / BB   = tieto puuttuu
98 = ei virallinen kieli rekisterissä 

Tietoa on lähinnä vuoden 1970 jälkeen suoritetuista tutkinnoista.

#### `oppiso` — Oppisopimuskoulutus

Tieto on ammatillisissa oppilaitoksissa vuodesta 1997 lähtien suoritetuilla tutkinnoilla ja näyttötutkinnoilla. 
1 = tutkinto on suoritettu oppisopimuskoulutuksena 
0 = tutkintoa ei ole suoritettu oppisopimuskoulutuksena

#### `ulkom` — Tutkinto suoritettu ulkomailla

1 = tutkinto on suoritettu ulkomailla 
0 = tutkinto on suoritettu Suomessa

#### `ktutk_1` — Tuorein muu tutkinto

Muu kuin henkilön korkein tutkinto kyseisenä vuonna. TK:n uusimman koulutusluokituksen 6-numeroinen koulutuskoodi.

#### `suorv_1` — Suoritusvuosi, tuorein muu tutkinto

Merkkimuotoinen suoritusvuosi (VVVV).

#### `ktutk_2` — Toiseksi tuorein muu tutkinto

Muu kuin henkilön korkein tutkinto kyseisenä vuonna. TK:n uusimman koulutusluokituksen 6-numeroinen koulutuskoodi.

#### `suorv_2` — Suoritusvuosi, toiseksi tuorein muu tutkinto

Merkkimuotoinen suoritusvuosi (VVVV).

#### `ktutk_3` — Kolmanneksi tuorein muu tutkinto

Muu kuin henkilön korkein tutkinto kyseisenä vuonna. TK:n uusimman koulutusluokituksen 6-numeroinen koulutuskoodi.

#### `suorv_3` — Suoritusvuosi, kolmanneksi tuorein muu tutkinto

Merkkimuotoinen suoritusvuosi (VVVV).

#### `ktutk_4` — Neljänneksi tuorein muu tutkinto

Muu kuin henkilön korkein tutkinto kyseisenä vuonna.TK:n uusimman koulutusluokituksen 6-numeroinen koulutuskoodi.

#### `suorv_4` — Suoritusvuosi, neljänneksi tuorein muu tutkinto

Merkkimuotoinen suoritusvuosi (VVVV).

---

[← Back to catalogue](../../README.md)
