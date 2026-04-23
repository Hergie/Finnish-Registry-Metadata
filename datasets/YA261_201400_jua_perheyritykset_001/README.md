# FIRM_FAMBUS Perheyritykset 2014 (YA261)

- **Identifier:** `YA261_201400_jua_perheyritykset_001.xml`
- **DOI:** `work_2017-02_2017-02-14_ain_0001`
- **Temporal coverage:** 2014-01-01 - 2014-12-31
- **Published:** 2017-06-28
- **Organisation:** Tilastokeskus
- **Variable count:** 37
- **Observation count:** —
- **Population:** Perheyritykset
- **Source:** Yritysten rakenne- ja tilinpäätöstilasto

## Description

Perheyritysten liiton tilaama yksikkötason aineisto tutkimustarkoituksiin sisältää suuret ja keskisuuret perheyritykset sekä otoksen pienistä perheyrityksistä vuodelta 2014 (ei sisällä ammatinharjoittajia). 

Datassa on kaikki kokoluokat ja näihin liittyvät tilinpäätöstiedot. Pienten yritysten osalta aineisto perustuu otokseen. Tämän vuoksi aineistossa on myös muuttuja Paino, joka saa arvon 1 suurilla ja keskisuurilla yrityksillä, mutta pienillä yrityksillä muuttuja saa arvoja sen mukaan, miten ne on ositetun otannan perusteella laskettu. Pienten yritysten osalta aineistoon on myös korotettu jo muut luvut valmiiksi tuolla painolla. Alkuperäisiin arvoihin siis pääsee jakamalla muuttujien arvot tuolla painon arvolla.

Perheyritystutkimuksen otantakehikkona oli Suomen alle 50 henkilöä työllistävät perheyritykset. Kehikon koko oli 74 807 yritystä. Ennen poimintaa kehikko jaettiin ositteisiin toimialaryhmien (8 kpl) ja yritysten kokoluokkien (4 kpl) mukaan. Otos poimittiin ositetulla suhteellisella otannalla. Poimintasuhde ositteista oli 1 600 / 74 807 eli noin 0,0214. Jokaiseen ositteeseen pakotettiin kuitenkin vähintään 40 yritystä. Lopulliseksi otoskooksi saatiin 2 085.

Aineistoon on rajattu konserniyrityksistä mukaan yritykset, joissa konsernin äänivalta on vähintään 50 prosenttia. Sekä konserniyrityksistä että konserniin kuulumattomista yrityksistä aineistossa on mukana vuonna 2014 rakenne- ja tilinpäätöstilaston tilastoyksikköinä olleet yritykset.

Omistus-muuttuja saa arvoja seuraavasti:
0= tietoa ei saatu
1= sukupolvenvaihdoksen tehnyt perheyritys
2= ensimmäisen polven perheyritys
3= kotimainen muulla tavoin omistettu yritys
 
Kokoluokka-muuttuja: 
1=pieni 
2=keskisuuri
3=suuri

Yrityskokoluokittaiseen taulukkoon konserniyritykset jaettiin kokoluokkiin siten, että konserniyrityksille yrityskokoluokka määrättiin konsernin henkilöstömäärän mukaan. Näin ollen esimerkiksi yritys, jossa työskentelee 10 henkilöä, mutta on osa 1000 henkilön konsernia kuuluu kokoluokituksissa suuryrityksiin. Konserniin kuulumattomilla yrityksillä henkilöstökokoluokka määräytyy yrityksen henkilöstömäärän mukaan.

Toimialoista on rajattu mukaan vain ennalta määritellyt toimialaryhmät:

    A Maatalous, metsätalous ja kalatalous
    B+C+D Kaivostoim., Teollisuus, Sähkö-, kaasu- lämpöh. ym.
    F Rakentaminen
    G Kauppa
    H+J Kuljetus ja varastointi, Informaatio ja viestintä
    I Majoitus- ja ravitsemus
    L Kiinteistöalan toiminta
    M+N+P+Q+R+S Amm+tiet, Hallinto+tuki, Koulutus, Terv+sos.palv, Taiteet, viihde, virk., Muu pal

Toimialalta A esitetään ainoastaan yritysten lukumäärät sekä henkilöstömäärät. Toimialalta ei ole tuotettavissa tilinpäätöslukuja. Toimiala K on tiputettu pois aineistosta, sillä myöskään tältä toimialalta ei ole tuotettavissa tilinpäätöstietoja.

Alueellistamisessa NUTS2-luokkiin käytettiin vuoden 2016 kuntaluokitusta. Yritykset alueellistettiin henkilöstömäärältään suurimman toimipaikan perusteella.

Lisätietoja: http://www.perheyritys.fi/wp-content/uploads/2017/02/FamilyBusinessInFinland2014-julkaisu2017-highres-web.pdf

## Variables (37)

| Identifier | Name | Unit | Classification | Group |
|---|---|---|---|---|
| `Vuosi` | Vuosi | — | — | — |
| `omistus` | Omistusmuoto | — | — | — |
| `Kokoluokka` | Kokoluokka | — | — | — |
| `Kunta` | Kunta | — | — | — |
| `Kunta16` | — | — | — | — |
| `Maakunta` | Maakunta | — | — | — |
| `NUTS2` | NUTS-alue | — | — | — |
| `Toimiala` | — | — | — | — |
| `TolK` | Toimiala | — | — | — |
| `verohOikMuoto` | Verohallinnon oikeudellinen muoto | — | — | — |
| `Kirjanpitomuoto` | Kahdenkertainen kirjanpito | — | — | — |
| `Paino` | — | — | — | — |
| `henkmaara` | Henkilöstön lukumäärä htv | — | — | — |
| `Liikevaihto` | Liikevaihto / tuotot ammatista yhteensä | — | — | — |
| `PalksaajHtv` | Palkansaajat henkilötyövuosina | — | — | — |
| `ku_HenkilostoYht` | Henkilöstökulut yhteensä | — | — | — |
| `LiikToimTuotYht` | LIIKETOIMINNAN TUOTOT YHTEENSÄ | — | — | — |
| `EUMukTuotJalostusarvo` | EU:n mukainen tuotannon jalostusarvo | — | — | — |
| `KayttokateOik` | KÄYTTÖKATE (oikaistu) | — | — | — |
| `RahTulos` | Rahoitustulos | — | — | — |
| `Nettotulos` | NETTOTULOS | — | — | — |
| `Kokonaistulos` | KOKONAISTULOS | — | — | — |
| `k_TilPaatSiirtKertYht` | TILINPÄÄTÖSSIIRTOJEN KERTYMÄ YHTEENSÄ | — | — | — |
| `AineellinenKayttoOmLis` | Aineellinen käyttöomaisuus: lisäykset | — | — | — |
| `AineellinenKayttoOmVah` | Aineellinen käyttöomaisuus: vähennykset | — | — | — |
| `PaaomanTuotto` | Pääoman tuotto | — | — | — |
| `ops_OmaPaaomaYht` | Oma pääoma yhteensä | — | — | — |
| `VierasPaaomYht` | Vieras pääoma yhteensä | — | — | — |
| `TaseOik` | Oikaistu tase | — | — | — |
| `VastaavaYht` | Vastaavaa yhteensä | — | — | — |
| `er_SaadEnnLyhytAikVel` | Saadut ennakot taseen lyhytaikaisista veloista | — | — | — |
| `er_SaadEnnPitkaAikVel` | Saadut ennakot taseen pitkäaikaisista veloista | — | — | — |
| `er_Korollinen` | Korollinen vieras pääoma | — | — | — |
| `vas_RahoitOmais` | Rahoitusomaisuus yhteensä | — | — | — |
| `ves_LyhytaikYhteens` | Lyhytaikaiset velat yhteensä | — | — | — |
| `k_PakVarYht` | PAKOLLISET VARAUKSET YHTEENSÄ | — | — | — |
| `syrtun` | Suojattu yritystunnus | — | — | — |

### Variable definitions

#### `Vuosi` — Vuosi

#### `omistus` — Omistusmuoto

#### `Kokoluokka` — Kokoluokka

#### `Kunta` — Kunta

#### `Kunta16`

#### `Maakunta` — Maakunta

#### `NUTS2` — NUTS-alue

#### `Toimiala`

#### `TolK` — Toimiala

#### `verohOikMuoto` — Verohallinnon oikeudellinen muoto

#### `Kirjanpitomuoto` — Kahdenkertainen kirjanpito

#### `Paino`

#### `henkmaara` — Henkilöstön lukumäärä htv

#### `Liikevaihto` — Liikevaihto / tuotot ammatista yhteensä

#### `PalksaajHtv` — Palkansaajat henkilötyövuosina

#### `ku_HenkilostoYht` — Henkilöstökulut yhteensä

#### `LiikToimTuotYht` — LIIKETOIMINNAN TUOTOT YHTEENSÄ

#### `EUMukTuotJalostusarvo` — EU:n mukainen tuotannon jalostusarvo

#### `KayttokateOik` — KÄYTTÖKATE (oikaistu)

#### `RahTulos` — Rahoitustulos

#### `Nettotulos` — NETTOTULOS

#### `Kokonaistulos` — KOKONAISTULOS

#### `k_TilPaatSiirtKertYht` — TILINPÄÄTÖSSIIRTOJEN KERTYMÄ YHTEENSÄ

#### `AineellinenKayttoOmLis` — Aineellinen käyttöomaisuus: lisäykset

#### `AineellinenKayttoOmVah` — Aineellinen käyttöomaisuus: vähennykset

#### `PaaomanTuotto` — Pääoman tuotto

#### `ops_OmaPaaomaYht` — Oma pääoma yhteensä

#### `VierasPaaomYht` — Vieras pääoma yhteensä

#### `TaseOik` — Oikaistu tase

#### `VastaavaYht` — Vastaavaa yhteensä

#### `er_SaadEnnLyhytAikVel` — Saadut ennakot taseen lyhytaikaisista veloista

#### `er_SaadEnnPitkaAikVel` — Saadut ennakot taseen pitkäaikaisista veloista

#### `er_Korollinen` — Korollinen vieras pääoma

#### `vas_RahoitOmais` — Rahoitusomaisuus yhteensä

#### `ves_LyhytaikYhteens` — Lyhytaikaiset velat yhteensä

#### `k_PakVarYht` — PAKOLLISET VARAUKSET YHTEENSÄ

#### `syrtun` — Suojattu yritystunnus

---

[← Back to catalogue](../../README.md)
