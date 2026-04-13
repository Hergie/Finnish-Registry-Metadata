# TRAFI Moottoriajoneuvokannan aineisto, valmismoduuli 2  omistaja/haltijatiedot

- **Identifier:** `TRAFI_20132025_jua_omistaja_002.xml`
- **DOI:** `mkan_2017-12_2017-12-12_ain_0001`
- **Temporal coverage:** 2013-01-01 - 2025-09-30
- **Published:** 2025-10-27
- **Organisation:** Liikenteen turvallisuusvirasto Trafi 
- **Variable count:** 31
- **Observation count:** —
- **Population:** Manner-Suomen ajoneuvorekisterissä olevat tieliikenteen ajoneuvoihin liittyvät rajatut omistaja/haltija tiedot
- **Source:** Liikenteen turvallisuusviraston (Trafi) ajoneuvorekisteri (ATJ ajoneuvojen tietojärjestelmä)
- **Related:** <a href= "https://www.stat.fi/til/mkan/index.html">ajoneuvokanta</a> <a href= "https://www.trafi.fi/filebank/a/1327477425/20a2a2f466b690ed94131f93468d4c69/9021-Rekisteriseloste_Ajoneuvoliikennerekisteri.pdf">ajoneuvoliikennerekisteri</a>

## Kuvaus / Description

TRAFI-valmisaineistot perustuvat Liikenne- ja viestintävirasto (Traficom) ajoneuvoliikennerekisteriin, joka sisältää tiedot kaikista rekisteröintivelvollisuuden alaisista tieliikenteen ajoneuvoista Manner-Suomessa vuodesta 2013 eteenpäin.

Ajoneuvokannasta on muodostettu kaksi valmisaineistomoduulia tutkimuskäyttöön. Moduuli 2 sisältää rajatut omistaja/haltijatiedot, jotka liittyvät moduulin 1 ajoneuvotietoihin (yhdistely avainnro- ja sjartun -muuttujilla).

Näihin valmisaineistoihin tulee hakea käyttölupaa Traficomilta. Aineistojen käsittely tapahtuu Tilastokeskuksen ylläpitämässä FIONA-etäkäyttöjärjestelmässä.

8.8.2025: Aineistoon on tehty muutoksia siten, että 2025 Q2 eteenpäin omistajatunnuksista (omtunnus_s) on eroteltu henkilötiedot (shnro), yritystiedot (ytun) ja muut tiedot (omtunnus_m ja haltunnus_m) erikseen. Tätä ennen kaikki ovat olleet samassa muuttujassa. Tämän lisäksi muuttuja suojattu vakuutuksenottaja (svakuttajantun) on poistettu aineistosta käytöstä.

22.12.2022: Tietoa päivämäärämuuttujista: Ajankohtien 2021q1-2022q2 tiedostoissa olevat päivämäärämuuttujat ovat sekä date-muodossa (ISO8601-formaatti) että string-muodossa. String-muotoiset muuttujat löytyvät tiedostoista, joiden tiedostonimissä on "_2"-pääte. Ajankohdan 2022q3 ja sen jälkeiset tiedostot sisältävät ainoastaan string-muotoiset päivämäärämuuttujat. 

11.5.2021: Aineistoa täydennetty omistajien, haltijoiden sekä vakuutuksenottajien shnro-tunnisteilla. 

Lisätietoa: Traficom: tietojenluovutus(at)trafi.fi 
                 Tilastokeskus: tutkijapalvelut(at)stat.fi

## Muuttujat / Variables (31)

| Tunnus / Identifier | Nimi / Name | Yksikkö / Unit | Luokitus / Classification | Ryhmä / Group |
|---|---|---|---|---|
| `avainnro` | Avainnumero | — | — | — |
| `omaslaji` | Omistajan asiakaslaji | — | ajot_3_2017_12_07 | — |
| `omalkupvm` | Omistussuhteen alkupäivä | — | — | — |
| `omaskieli` | Omistajan asiointikieli | — | ajot_2_2017_12_07 | — |
| `omkunta` | Omistajan kunta | — | — | — |
| `ompnro` | Omistajan postinumeron alku | — | — | — |
| `omsukupuoli` | Omistajan sukupuoli | — | — | — |
| `halaslaji` | Haltijan asiakaslaji | — | ajot_3_2017_12_07 | — |
| `halaskieli` | Haltijan asiointikieli | — | ajot_2_2017_12_07 | — |
| `halalkupvm` | Hallintasuhteen alkupäivä | — | — | — |
| `halkunta` | Haltijan kunta | — | — | — |
| `halpnro` | Haltijan postinumeron alku | — | — | — |
| `halsukupuoli` | Haltijan sukupuoli | — | — | — |
| `omist` | omistajatunnuksen tyyppi | — | — | — |
| `somtunnus` | Ajoneuvon 1. omistajan suojattu Y-tunnus tai henkilötunnus | — | — | — |
| `om_shnro` | Ajoneuvon 1. omistajan suojattu TK:n henkilönumero | — | — | — |
| `haltija` | haltijatunnuksen tyyppi | — | — | — |
| `shaltunnus` | Ajoneuvon 1. haltijan suojattu Y-tunnus tai henkilötunnus | — | — | — |
| `hal_shnro` | Ajoneuvon 1. haltijan suojattu TK:n henkilönumero | — | — | — |
| `vakut` | Vakutuksenottajan tunnuksen tyyppi | — | — | — |
| `svakuttajantun` | Ajoneuvon vakutuksenottajan suojattu Y-tunnus tai henkilötunnus | — | — | — |
| `vak_shnro` | Ajoneuvon vakuutuksenottajan suojattu TK:n henkilönumero | — | — | — |
| `jartun_s` | Suojattu järjestelmätunnus | — | — | — |
| `om_ytun_s` | Ajoneuvon 1. omistajan suojattu TK:n y-tunnus | — | — | — |
| `hal_ytun_s` | Ajoneuvon 1. haltijan suojattu TK:n y-tunnus | — | — | — |
| `vak_ytun_s` | Ajoneuvon vakuutuksenottajan suojattu TK:n y-tunnus | — | — | — |
| `omyrlaji` | Omistajan yritys laji | — | — | — |
| `halyrlaji` | Haltijan yritys laji | — | — | — |
| `halsuhde` | — | — | — | — |
| `omtunnus_m_s` | omistajatunnus muu suojattu | — | — | — |
| `haltunnus_m_s` | Haltijantunnus muu suojattu | — | — | — |

### Muuttujien määritelmät / Variable definitions

#### `avainnro` — Avainnumero

ajoneuvolle luotu pseudotunnus ajoneuvojen eri teknisten tietojen (dataosiot) sekä rajattujen omistaja/haltijatietojen yhdistelyä varten

#### `omaslaji` — Omistajan asiakaslaji

**Luokitus / Classification:** ajot_3_2017_12_07

1. omistajan asiakaslaji.
1= yksityinen, 2= yritys

#### `omalkupvm` — Omistussuhteen alkupäivä

Tieto kertoo milloin ajoneuvon ja 1. omistajan välinen omistussuhde on alkanut (milloin ajoneuvon edellinen rekisteriin merkitty omistaja on luovuttanut ajoneuvon).

#### `omaskieli` — Omistajan asiointikieli

**Luokitus / Classification:** ajot_2_2017_12_07

1. omistajan asiointikieli
fi = suomi, sv= ruotsi

#### `omkunta` — Omistajan kunta

Ajoneuvon 1. omistajan osoitteeseen liittyvä kunta. Henkilön kotipaikkakunta, jos kyseessä vakituinen osoite. Saadaan VTJ:sta tai päätellään voimassaolevan osoitteen postinumerosta. Manner-Suomen rekisterissä olevat ajoneuvot, mutta mukana pieni määrä Ahvenanmaalle sekä ulkomaille (kuntakoodi=200) rekisteröityjä ajoneuvoja ja tuntemattomia kuntakoodeja (198, 199).

#### `ompnro` — Omistajan postinumeron alku

Ajoneuvon 1. omistajan kotimaisen katuosoitteen postinumeron alku, 3 ensimmäistä numeroa.

#### `omsukupuoli` — Omistajan sukupuoli

Tieto luonnollisen henkilön (1. omistaja) sukupuolesta (Mies/Nainen)

#### `halaslaji` — Haltijan asiakaslaji

**Luokitus / Classification:** ajot_3_2017_12_07

1. haltijan asiakaslaji.
0 = ykistyinen, 2= yritys

#### `halaskieli` — Haltijan asiointikieli

**Luokitus / Classification:** ajot_2_2017_12_07

1. haltijan asiointikieli
fi = suomi, sv = ruotsi

#### `halalkupvm` — Hallintasuhteen alkupäivä

Tieto kertoo milloin ajoneuvon ja 1. haltijan välinen hallintasuhde on alkanut (milloin ajoneuvon edellinen rekisteriin merkitty haltija on luovuttanut ajoneuvon).

#### `halkunta` — Haltijan kunta

A.joneuvon 1. haltijan osoitteeseen liittyvä kunta. Henkilön kotipaikkakunta, jos kyseessä vakituinen osoite. Saadaan VTJ:sta tai päätellään voimassaolevan osoitteen postinumerostaManner-Suomen rekisterissä olevat ajoneuvot, mutta mukana pieni määrä Ahvenanmaalle sekä ulkomaille (kuntakoodi=200) 
rekisteröityjä ajoneuvoja ja tuntemattomia kuntakoodeja (198, 199).

#### `halpnro` — Haltijan postinumeron alku

Ajoneuvon 1. haltijan kotimaisen katuosoitteen postinumeron alku, 3 ensimmäistä numeroa

#### `halsukupuoli` — Haltijan sukupuoli

Tieto luonnollisen henkilön (1. haltija) sukupuolesta (Mies/Nainen)

#### `omist` — omistajatunnuksen tyyppi

1= henkilötunnus
2=y-tunnus
3= muu tunnus

#### `somtunnus` — Ajoneuvon 1. omistajan suojattu Y-tunnus tai henkilötunnus

Ajoneuvon 1. omistajan suojattu Y-tunnus tai henkilötunnus (pseudotunnus).

#### `om_shnro` — Ajoneuvon 1. omistajan suojattu TK:n henkilönumero

Ajoneuvon 1. omistajan suojattu TK:n henkilönumero (pseudotunnus).

#### `haltija` — haltijatunnuksen tyyppi

1=henkilötunnus
2=y-tunnus
3=muu tunnus

#### `shaltunnus` — Ajoneuvon 1. haltijan suojattu Y-tunnus tai henkilötunnus

Ajoneuvon 1. haltijan suojattu Y-tunnus tai henkilötunnus (pseudotunnus).

#### `hal_shnro` — Ajoneuvon 1. haltijan suojattu TK:n henkilönumero

Ajoneuvon 1. haltijan suojattu TK:n henkilönumero  (pseudotunnus).

#### `vakut` — Vakutuksenottajan tunnuksen tyyppi

1=henkilötunnus
2=y-tunnus
3=muu tunnus

#### `svakuttajantun` — Ajoneuvon vakutuksenottajan suojattu Y-tunnus tai henkilötunnus

Ajoneuvon vakutuksenottajan suojattu Y-tunnus tai henkilötunnus (pseudotunnus).

#### `vak_shnro` — Ajoneuvon vakuutuksenottajan suojattu TK:n henkilönumero

Ajoneuvon vakutuksenottajan suojattu TK:n henkilönumero (pseudotunnus).

#### `jartun_s` — Suojattu järjestelmätunnus

Tilastokeskuksen Tutkijapalveluissa pseudonymisoitu tunnus yksilöi Traficomin liikenneasioiden rekisterissä olevat ajoneuvot.

#### `om_ytun_s` — Ajoneuvon 1. omistajan suojattu TK:n y-tunnus

Ajoneuvon 1. omistajan suojattu TK:n y-tunnus (pseudotunnus).

#### `hal_ytun_s` — Ajoneuvon 1. haltijan suojattu TK:n y-tunnus

Ajoneuvon 1. haltijan suojattu TK:n y-tunnus (pseudotunnus).

#### `vak_ytun_s` — Ajoneuvon vakuutuksenottajan suojattu TK:n y-tunnus

Ajoneuvon vakutuksenottajan suojattu TK:n y-tunnus (pseudotunnus).

#### `omyrlaji` — Omistajan yritys laji

#### `halyrlaji` — Haltijan yritys laji

#### `halsuhde`

#### `omtunnus_m_s` — omistajatunnus muu suojattu

Suojattu muu omistaja tunnus, joka ei ole perinteinen hetu tai y-tunnus.

#### `haltunnus_m_s` — Haltijantunnus muu suojattu

Suojattu muu haltijantunnus, joka ei ole perinteinen hetu tai y-tunnus.

---

[← Takaisin luetteloon / Back to catalogue](../../README.md)
