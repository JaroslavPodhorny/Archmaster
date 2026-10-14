# Graf principů M9: the principles the solutions of the test use, as a tree in learning order

Generated from `analysis/data/rebuilt/m9_topic_tree.json` and `analysis/data/rebuilt/m9_item_skills.json`; change them
with `analysis/topic_tree.py`, not here. The tree has 7 areas, 23 topics and 157 skills.
Every one of the 610 scored items (sub-items such as 15.2, or whole tasks) of the 20 tests of
2022–2026 is assigned to the skills it needs.

What rests on what:

- **The assignment is what the solution of each item applies.** Every task was solved from its image and the
  result compared with the official key (`analysis/graph_design_spec.md`, section 8, names the few exceptions);
  the solutions are in `analysis/data/m9_item_solutions.json`. An item is assigned every principle its natural
  solution applies as a step, the main one first. Which principles those are, the grouping and the
  prerequisite links are one solver's judgement, not CERMAT's.
- **Numbers are computed, not estimated**: points from the catalog, success rates from CERMAT's
  published item results.
- **Skills marked S** are quoted from CERMAT's specification (`References/MASPECIFIKACEPOZADAVKU2022 (1).pdf`,
  parts A1, B1, C1; C1 says a candidate must also know A1 and B1) and are needed by no item of the 20
  tests. The specification's four areas are 1 Číslo a proměnná, 2 Závislosti, vztahy a práce s daty,
  3 Geometrie v rovině a prostoru, 4 Nestandardní aplikační úlohy a problémy.

## How the tree is cut

- **A leaf is one principle**: a rule, fact or method that a solution applies as a step and that a student
  either has or lacks. Fine enough to name a gap, no finer; no bundles of several rules and no bins for
  what fits nowhere else. Areas and topics only group leaves. The rules for leaves, links and the assignment
  are in `analysis/graph_design_spec.md`, sections 4–6.
- **Order is learning order.** Everything a leaf needs comes earlier; the *needs* column names the direct
  prerequisites (the editor refuses an order that breaks this). The links say what must be learned first.
  What a task needs is the list of the task itself, not the links.
- **One principle is one leaf wherever it is used.** Thaletova věta, rovnoramenný trojúhelník, výška and
  osa úhlu serve both constructions and calculations, so the properties of figures (KON) come before the
  calculations (GEO).
- **Computing and reading are separated.** Computing with fractions is in POC, fraction word problems in
  VZT. The phrases „o třetinu více než“, „kolikrát“, „o kolik procent“ recur in fractions, percentages
  and equation word problems, so they are one topic (VZT.NEZ) learned once instead of three times.
- Not in the tree: the rules for how answers must look and the list of what is not printed in the
  booklet ([03_ucivo_M9.md](03_ucivo_M9.md), section 0). They apply to every leaf.

## How to read the columns

- **P, priority**, from how often a skill is needed, directly or through a skill that builds on it. A
  foundation therefore never ranks below what stands on it: „pořadí operací“ is needed by few items by name,
  but nearly every computation rests on it. "Standard tests" are the 16 tests of 2022, 2023, 2025, 2026; the four
  2024 tests follow a different design and do not count here.
  **1** = needed in at least 10 of the 16 standard tests, or in at least 6 of the 8 tests of 2025–2026 (47 skills) ·
  **2** = in at least 4 of 16, or 3 of the last 8 (43) · **3** = rarer, or only in 2024 (41) ·
  **S** = in the specification, needed by no item of 2022–2026 (26); where one occurred in an older
  test, its note says so.
- **Tests** = in how many of the 16 standard tests an item needs the skill itself, and after the dot in how
  many of the 8 tests of 2025–2026. A skill that is 2 · 2 is new; one that is 6 · 0 has not come back.
- **Points** = points per standard test that depend on the skill: the full points of every item that
  needs it. An item needing three skills counts for each, so the column does not add up to 50; the
  figures given for topics and areas count each item once.
- **With what builds on it** = the same three numbers (tests · recent tests · points) counting also the
  items that need a skill resting on this one, following the *needs* links. Empty when nothing builds on
  the skill. This is what the priority is taken from, and it is only as good as those links.
- **Success** = points-weighted average success of those items in the regular terms (A, B) of all five
  years. It is the success of the items, not of the skill alone: an item can fail on another skill it needs.
- **Hardest** = the three least solved items (regular terms) in which the skill is the main one. Being
  able to solve these is what "mastered" means for the skill.
- **Kind** says how the skill is practised: *postup* – a procedure, drilled until fast and error-free ·
  *překlad* – turning the Czech wording into mathematics · *znalost* – a fact or property known by heart ·
  *rozbor* – finding the route through a multi-step task.

## Check against tests from before 2022

The tree was built from the 2022–2026 tests, so they fit it by construction. As a check, 3 older tests
it was not built from (2019 A, 2021 A, 2021 B; booklets in `References/Matematika_starsi/`) were solved the same way from
their page images: 97 items. No official keys of these tests are in the repository, so their results are
not checked against a key. The solutions are in `data/m9_item_solutions_older.json`, the assignment in
`data/rebuilt/m9_item_skills_older.json`; they count in none of the numbers below, because the next tests will resemble
the recent ones more than the old ones.

Every item found a place among the skills seen in 2022–2026.

## The tree at a glance

Points per standard test in brackets (each item counted once per topic).

```
POC  Počítání s čísly  (14,1 b.)
├─ Čísla a číselné výrazy  (8,7 b.)
│    1  Pořadí operací a závorky
│    1  Počítání se zápornými čísly
│    1  Počítání s desetinnými čísly
│    1  Druhá mocnina čísla
│    1  Druhá odmocnina
│    3  Zaokrouhlení na daný řád
│    3  Číselná osa se stejnými dílky
│    2  Výraz zadaný slovy
│    S  Absolutní hodnota a opačné číslo
│    S  Periodické číslo: zápis, porovnání, převod zlomku
│    S  Odhad výsledku s danou přesností
├─ Dělitelnost  (1,2 b.)
│    1  Dělitelé a násobky čísla
│    3  Prvočísla a rozklad na prvočísla
│    2  Dělení se zbytkem
│    1  Společný násobek a dělitel
│    S  Znaky dělitelnosti čísly 2, 3, 4, 5, 6, 8 a 10
├─ Zlomky  (5,6 b.)
│    1  Krácení, rozšiřování, základní tvar
│    1  Sčítání a odčítání: společný jmenovatel
│    1  Násobení a dělení zlomků
│    1  Složený zlomek
│    3  Převod desetinného čísla na zlomek a zpět
│    2  Mocnina a odmocnina zlomku
│    3  Smíšené číslo
│    S  Porovnávání zlomků
└─ Jednotky  (1,9 b.)
     2  Jednotky délky
     3  Jednotky obsahu
     3  Jednotky objemu, litry
     3  Jednotky hmotnosti
     2  Jednotky času
     3  Stupně a minuty

ALG  Výrazy a rovnice  (10,1 b.)
├─ Výrazy  (7,4 b.)
│    3  Dosazení čísla do výrazu
│    1  Sloučení členů, minus před závorkou
│    1  Násobení jednočlenů a mnohočlenů (roznásobení závorek)
│    1  Vzorec (a ± b)²
│    2  Vytýkání
│    2  Rozklad a² − b² na součin
│    3  Rozklad trojčlenu podle (a ± b)², doplnění
└─ Rovnice  (6,0 b.)
     1  Ekvivalentní úpravy rovnice
     1  Odstranění zlomků z rovnice
     3  Rovnice bez řešení a s nekonečně mnoha řešeními
     2  Soustava dvou rovnic

VZT  Vztahy mezi veličinami  (19,5 b.)
├─ Zlomek jako část celku  (4,1 b.)
│    1  Zlomek z čísla
│    2  Jakou částí celku je
│    1  Zbytek celku a část ze zbytku
│    3  Zlomek ze zlomku
│    1  Celek z části
├─ Srovnání  (4,3 b.)
│    1  „o kolik“ je rozdíl, „kolikrát“ je podíl
│    1  „o třetinu více / méně než“ jako násobení
│    2  Obrácení vztahu: neznámá je za „než“
├─ Procenta  (7,1 b.)
│    1  Procentová část
│    1  Počet procent
│    1  Základ z procentové části
│    2  Procento, zlomek a poměr: převody
│    1  „o x % více / méně“ jako násobitel
│    2  Základ po změně
│    2  O kolik procent se liší dvě veličiny
│    3  Dvě změny po sobě
│    3  Úrok a daň z úroku
│    S  Promile
│    S  Jistina, úroková míra, úrokovací období, inflace; půjčky a úvěry
├─ Poměr a úměrnost  (3,3 b.)
│    2  Poměr: zápis, krácení
│    2  Díly poměru: z celku, části nebo rozdílu
│    3  Měřítko mapy a plánu
│    3  Měřítko a obsah: druhá mocnina
│    1  Přímá úměrnost
│    2  Nepřímá úměrnost
│    3  Společná práce: sčítají se výkony
│    3  Pohyb: s = v · t
│    3  Směsi a průměrná cena
│    S  Postupný a převrácený poměr, změna čísla v daném poměru
│    S  Přímá a nepřímá úměrnost tabulkou, rovnicí a grafem
└─ Slovní úlohy  (7,6 b.)
     2  Rozbor textu: řetěz jednoduchých výpočtů
     1  Vyjádření veličiny výrazem s proměnnou
     1  Sestavení rovnice ze zadání
     2  Dvě neznámé: dvě podmínky, součet a rozdíl
     3  Podmínka celého čísla

DAT  Grafy, tabulky, průměr  (3,4 b.)
├─ Grafy a tabulky  (2,9 b.)
│    1  Čtení hodnot z grafu nebo diagramu
│    3  Třídění údajů do tabulky
│    3  Kruhový diagram: části jako procenta a úhly
│    3  Graf bez stupnice: hodnota dílku z podmínky
│    2  Dopočet chybějícího údaje ze vztahu mezi údaji
│    S  Statistický soubor, statistický znak, statistické šetření, četnost
│    S  Volba vhodné tabulky a diagramu, vytvoření diagramu z dat
│    S  Bod v pravoúhlé soustavě souřadnic
└─ Aritmetický průměr  (1,1 b.)
     2  Aritmetický průměr
     3  Průměr z četností
     2  Součet z průměru, chybějící hodnota

KON  Geometrie: útvary a konstrukce  (6,9 b.)
├─ Základní pojmy a konstrukce  (5,1 b.)
│    1  Kolmice daným bodem
│    2  Rovnoběžka daným bodem
│    1  Střed a osa úsečky
│    1  Kružnice: body v dané vzdálenosti, přenesení délky
│    3  Úhel dané velikosti
│    1  Středová souměrnost
│    2  Osová souměrnost, samodružný bod
│    S  Přenesení úhlu
│    S  Kružnice opsaná trojúhelníku
│    S  Tečna kružnice v jejím bodě
│    S  Obraz celého útvaru ve středové souměrnosti
├─ Vlastnosti útvarů  (6,4 b.)
│    1  Rovnoramenný a rovnostranný trojúhelník: shodná ramena, úhly při základně, osa
│    2  Thaletova věta a kružnice
│    1  Výška: kolmice z vrcholu na protější stranu, i vně
│    3  Těžnice
│    3  Trojúhelníková nerovnost
│    1  Rovnoběžník: úhlopříčky se půlí
│    3  Kosočtverec
│    2  Obdélník: shodné úhlopříčky, vrcholy na kružnici
│    3  Čtverec
│    3  Rovnoramenný a pravoúhlý lichoběžník
│    3  Pravidelný mnohoúhelník (pěti-, šesti-, osmiúhelník)
│    3  Osy souměrnosti útvaru
│    S  Shodnost trojúhelníků
│    S  Podobnost trojúhelníků: věty sss, sus, uu, poměr podobnosti
└─ Rozbor konstrukční úlohy  (4,8 b.)
     1  Podmínka jako množina bodů, bod jako průsečík dvou čar
     1  Všechna řešení
     S  Trojúhelník a čtyřúhelník ze zadaných údajů (sss, sus, usu)

GEO  Geometrie: výpočty  (10,0 b.)
├─ Úhly  (2,2 b.)
│    1  Vedlejší a vrcholové úhly
│    2  Souhlasné a střídavé úhly
│    1  Součet úhlů v trojúhelníku
│    2  Osa úhlu
├─ Pythagorova věta  (1,6 b.)
│    1  Pythagorova věta
│    2  Nalezení pravoúhlého trojúhelníku v útvaru nebo tělese
├─ Obvod a obsah  (4,4 b.)
│    1  Obvod mnohoúhelníku
│    1  Obsah čtverce a obdélníku
│    1  Obsah trojúhelníku
│    3  Obsah rovnoběžníku a kosočtverce
│    2  Obsah lichoběžníku
│    2  Rozměr z obsahu nebo obvodu (vzorec obráceně, i u kruhu)
│    2  Skládání a rozklad útvarů
│    3  Rozestupy po obvodu
│    S  Obvod a obsah mnohoúhelníku ve čtvercové síti
├─ Kruh  (0,8 b.)
│    2  Obvod kruhu
│    2  Obsah kruhu
│    3  Půlkruh, čtvrtkruh, výseč
│    S  Vzájemná poloha kružnice a přímky: tečna, sečna, vnější přímka
│    S  Vzájemná poloha dvou kružnic, průsečíky a body dotyku
└─ Tělesa  (3,9 b.)
     2  Hrany a stěny hranolu
     1  Objem krychle a kvádru
     1  Povrch krychle a kvádru
     2  Objem hranolu
     2  Povrch hranolu
     2  Objem válce
     3  Plášť a povrch válce
     2  Hrana nebo výška z objemu či povrchu
     3  Síť tělesa
     2  Slepená a rozříznutá tělesa, řez
     3  Tělesa z krychliček
     S  Pohled na těleso shora, zepředu, zprava, zleva a zdola
     S  Náčrt sítě a obrazu tělesa ve volném rovnoběžném promítání
     S  Jehlan: rozpoznání, síť, pohledy, metrické a polohové vlastnosti
     S  Koule: poloměr a průměr ve slovních úlohách

ZAK  Zákonitosti a úsudek  (3,9 b.)
├─ Rostoucí obrazce a číselné řady  (3,1 b.)
│    1  Pokračování pravidla po krocích
│    2  Obecné pravidlo, n-tý člen
│    2  Obrácení pravidla
│    3  Růst násobením
│    3  Číselná řada daná pravidlem
└─ Úsudek a systematické hledání  (1,1 b.)
     2  Periodické děje
     2  Systematické vypsání možností
```

## Počítání s čísly (POC)

14,1 points per standard test · success 45 % · Výpočty s čísly, které používají všechny ostatní oblasti: číselné výrazy, dělitelnost, zlomky, jednotky.

### Čísla a číselné výrazy

`POC.VYR` · 8,7 points per standard test, in 16 of 16 · success 50 % · specification area 1

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Pořadí operací a závorky | postup |  | 14 · 6 | 1,8 | 16 · 8 · 3,6 | 61 % | [2023 A 3.1](../backend/data/screenshots/M9-2023-A-03.png) 59 % | Nejdřív závorky, pak mocniny a odmocniny, potom násobení a dělení, nakonec sčítání a odčítání; operace stejné úrovně zleva doprava. Typická chyba: počítat zleva doprava bez ohledu na přednost, např. 5/9 − 5/9 : 5 jako (5/9 − 5/9) : 5. |
| 1 | Počítání se zápornými čísly | postup |  | 16 · 8 | 4,0 | 16 · 8 · 15,4 | 58 % | [2026 A 2.1](../backend/data/screenshots/M9-2026-A-02.png) 52 % · [2022 B 1](../backend/data/screenshots/M9-2022-B-01.png) 68 % | Minus krát minus je plus, odečíst záporné číslo znamená přičíst, sudá mocnina záporného čísla je kladná. Typická chyba: 36 − (−9) = 27 nebo (−3)² = −9. |
| 1 | Počítání s desetinnými čísly | postup |  | 13 · 5 | 2,1 | 16 · 8 · 12,0 | 50 % | [2025 A 4.2](../backend/data/screenshots/M9-2025-A-04.png) 36 % · [2022 B 4.2](../backend/data/screenshots/M9-2022-B-04.png) 40 % · [2022 A 5.1](../backend/data/screenshots/M9-2022-A-05.png) 46 % | Sčítání, násobení a dělení desetinných čísel bez kalkulačky; před dělením se obě čísla rozšíří tak, aby dělitel byl celý (0,92 : 0,2 = 9,2 : 2). Typická chyba: špatně umístěná desetinná čárka v součinu nebo podílu. |
| 1 | Druhá mocnina čísla | znalost |  | 9 · 3 | 0,9 | 15 · 7 · 5,5 | 51 % | [2023 B 16.2](../backend/data/screenshots/M9-2023-B-16.png) 6 % · [2024 B 8.1](../backend/data/screenshots/M9-2024-B-08.png) 39 % · [2023 B 4.2](../backend/data/screenshots/M9-2023-B-04.png) 46 % | Druhá mocnina je číslo násobené samo sebou; druhé mocniny čísel do 20, násobků deseti a jednoduchých desetinných čísel je třeba znát zpaměti. Typická chyba: záměna s násobením dvěma (7² = 14), nebo chyba v řádu u desetinného čísla (0,3² = 0,9). |
| 1 | Druhá odmocnina | znalost | Druhá mocnina čísla (POC.VYR) | 11 · 5 | 1,8 | 14 · 6 · 3,7 | 40 % | [2023 B 1](../backend/data/screenshots/M9-2023-B-01.png) 65 % · [2025 B 3.2](../backend/data/screenshots/M9-2025-B-03.png) 66 % · [2022 A 1](../backend/data/screenshots/M9-2022-A-01.png) 82 % | Druhá odmocnina je nezáporné číslo, jehož druhá mocnina dá odmocňované číslo; výraz pod odmocninou se nejdřív celý vypočítá. Typická chyba: odmocňovat sčítance zvlášť, √(a² + b²) = a + b. |
| 3 | Zaokrouhlení na daný řád | postup | Počítání s desetinnými čísly (POC.VYR) | 2 · 1 | 0,2 |  | 21 % | [2024 A 8.2](../backend/data/screenshots/M9-2024-A-08.png) 21 % | Rozhoduje číslice za požadovaným řádem: 0–4 dolů, 5–9 nahoru; zaokrouhluje se jednou, až konečný výsledek. Typická chyba: zaokrouhlit mezivýsledek, nebo zaokrouhlit na jiný řád, než zadání žádá. |
| 3 | Číselná osa se stejnými dílky | postup |  | 2 · 0 | 0,2 |  | 24 % | [2022 B 2.1](../backend/data/screenshots/M9-2022-B-02.png) 22 % · [2022 B 2.2](../backend/data/screenshots/M9-2022-B-02.png) 25 % | Dílky číselné osy jsou stejně dlouhé: délka dílku je rozdíl dvou známých čísel dělený počtem dílků mezi nimi. Typická chyba: počítat značky místo mezer, nebo předpokládat, že dílek je 1. |
| 2 | Výraz zadaný slovy | překlad | Pořadí operací a závorky (POC.VYR) | 4 · 3 | 0,2 |  | 43 % | [2025 A 1](../backend/data/screenshots/M9-2025-A-01.png) 44 % | Součet, rozdíl, součin, podíl, druhá mocnina a odmocnina zadané slovy se zapíší výrazem ve správném pořadí a se závorkami: „podíl součtu a součinu“ je (a + b) : (a · b). Typická chyba: obrácené pořadí u rozdílu a podílu, nebo vynechaná závorka. |
| S | Absolutní hodnota a opačné číslo | znalost |  |  |  |  |  |  | Specifikace B1, 1: „určí číslo kladné, záporné a opačné, znázorní a určí absolutní hodnotu čísla“. |
| S | Periodické číslo: zápis, porovnání, převod zlomku | znalost |  |  |  |  |  |  | Specifikace B1, 1: „rozumí zápisu … desetinného čísla včetně periodického čísla“, „převádí zlomek na desetinné číslo včetně čísla s periodou“. |
| S | Odhad výsledku s danou přesností | postup |  |  |  |  |  |  | Specifikace B1, 1: „provádí odhady početních operací s racionálními čísly s danou přesností“. |

### Dělitelnost

`POC.DEL` · 1,2 points per standard test, in 8 of 16 · success 16 % · specification area 1 · Před zlomky, protože krácení a společný jmenovatel stojí na dělitelích a násobcích.

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Dělitelé a násobky čísla | postup |  | 3 · 2 | 0,2 | 16 · 8 · 16,0 | 12 % | [2025 A 8.3](../backend/data/screenshots/M9-2025-A-08.png) 2 % · [2025 B 6.3](../backend/data/screenshots/M9-2025-B-06.png) 23 % | Dělitel čísla je číslo, kterým je dělitelné beze zbytku; dělitelé se hledají po dvojicích (95 = 5 · 19), násobky násobením. Typická chyba: vynechat druhého dělitele z dvojice, nebo zaměnit dělitele s násobkem. |
| 3 | Prvočísla a rozklad na prvočísla | postup | Dělitelé a násobky čísla (POC.DEL) | 2 · 2 | 0,2 |  | 27 % | [2025 B 6.2](../backend/data/screenshots/M9-2025-B-06.png) 27 % · [2025 B 6.1](../backend/data/screenshots/M9-2025-B-06.png) 31 % | Prvočíslo má právě dva dělitele, jedničku a samo sebe; složené číslo se dá jediným způsobem rozložit na součin prvočísel (231 = 3 · 7 · 11). Typická chyba: považovat 1 za prvočíslo, zapomenout na sudé prvočíslo 2, nebo ukončit rozklad u složeného čísla. |
| 2 | Dělení se zbytkem | postup |  | 6 · 4 | 0,8 | 7 · 5 · 1,0 | 15 % | [2026 A 16.3](../backend/data/screenshots/M9-2026-A-16.png) 1 % · [2025 B 16.2](../backend/data/screenshots/M9-2025-B-16.png) 1 % · [2026 B 16.2](../backend/data/screenshots/M9-2026-B-16.png) 7 % | Dělenec = dělitel · podíl + zbytek a zbytek je menší než dělitel; podíl říká, kolikrát se něco vejde celé, zbytek, co zůstane. Typická chyba: podíl zaokrouhlit místo práce se zbytkem, nebo zaměnit podíl a zbytek. |
| 1 | Společný násobek a dělitel | postup | Dělitelé a násobky čísla (POC.DEL) | 2 · 1 | 0,2 | 16 · 8 · 7,2 | 6 % | [2026 A 16.3](../backend/data/screenshots/M9-2026-A-16.png) 1 % · [2022 A 16.3](../backend/data/screenshots/M9-2022-A-16.png) 11 % | Nejmenší společný násobek je nejmenší číslo dělitelné oběma čísly, největší společný dělitel největší číslo, které obě dělí; společný násobek je společným jmenovatelem zlomků i okamžikem, kdy se dva opakující se děje znovu sejdou. Typická chyba: brát vždy součin čísel (u 4 a 6 číslo 24 místo 12), nebo zaměnit násobek s dělitelem. |
| S | Znaky dělitelnosti čísly 2, 3, 4, 5, 6, 8 a 10 | znalost |  |  |  |  |  |  | Specifikace B1, 1: „užívá znaky dělitelnosti čísly 2, 3, 4, 5, 6, 8 a 10“. |

### Zlomky

`POC.ZLOM` · 5,6 points per standard test, in 16 of 16 · success 52 % · specification area 1 · Počítání se zlomky; slovní úlohy se zlomky jsou ve VZT.

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Krácení, rozšiřování, základní tvar | postup | Dělitelé a násobky čísla (POC.DEL) | 16 · 8 | 3,2 | 16 · 8 · 13,0 | 67 % | [2026 B 2.2](../backend/data/screenshots/M9-2026-B-02.png) 56 % · [2023 A 3.3](../backend/data/screenshots/M9-2023-A-03.png) 58 % · [2024 B 3.2](../backend/data/screenshots/M9-2024-B-03.png) 58 % | Hodnota zlomku se nezmění, když se čitatel i jmenovatel vynásobí nebo vydělí stejným nenulovým číslem; výsledek se uvádí v základním tvaru. Typická chyba: krátit sčítance místo činitelů, nebo nechat výsledek nezkrácený. |
| 1 | Sčítání a odčítání: společný jmenovatel | postup | Krácení (POC.ZLOM), Společný násobek a dělitel (POC.DEL) | 16 · 8 | 3,9 | 16 · 8 · 4,0 | 54 % | [2022 A 3.1](../backend/data/screenshots/M9-2022-A-03.png) 60 % · [2026 B 2.1](../backend/data/screenshots/M9-2026-B-02.png) 63 % · [2025 A 2.1](../backend/data/screenshots/M9-2025-A-02.png) 65 % | Zlomky se sčítají a odčítají až po převedení na společného jmenovatele; sečtou se čitatelé, jmenovatel zůstává. Typická chyba: sečíst čitatele i jmenovatele (1/2 + 1/3 = 2/5), nebo rozšířit jen jmenovatel. |
| 1 | Násobení a dělení zlomků | postup | Krácení (POC.ZLOM) | 16 · 8 | 4,4 | 16 · 8 · 11,0 | 61 % | [2026 B 2.2](../backend/data/screenshots/M9-2026-B-02.png) 56 % · [2024 A 3.1](../backend/data/screenshots/M9-2024-A-03.png) 62 % · [2023 A 3.2](../backend/data/screenshots/M9-2023-A-03.png) 67 % | Násobí se čitatel s čitatelem a jmenovatel se jmenovatelem, před násobením se krátí křížem; celé číslo násobí jen čitatel. Dělit zlomkem znamená násobit zlomkem převráceným. Typická chyba: převrátit první zlomek místo dělitele, nebo při násobení hledat společného jmenovatele. |
| 1 | Složený zlomek | postup | Násobení a dělení zlomků (POC.ZLOM), Pořadí operací a závorky (POC.VYR) | 14 · 6 | 1,8 |  | 65 % | [2025 A 2.2](../backend/data/screenshots/M9-2025-A-02.png) 56 % · [2023 A 3.3](../backend/data/screenshots/M9-2023-A-03.png) 58 % · [2024 B 3.2](../backend/data/screenshots/M9-2024-B-03.png) 58 % | Hlavní zlomková čára je dělení: nejdřív se zvlášť vypočítá čitatel a jmenovatel, potom se čitatel dělí jmenovatelem. Typická chyba: krátit přes hlavní zlomkovou čáru dřív, než jsou čitatel a jmenovatel upraveny na jeden zlomek, nebo dělit v opačném pořadí. |
| 3 | Převod desetinného čísla na zlomek a zpět | postup | Krácení (POC.ZLOM), Počítání s desetinnými čísly (POC.VYR) | 1 · 1 | 0,1 |  | 64 % | [2024 A 3.2](../backend/data/screenshots/M9-2024-A-03.png) 64 % | Desetinné číslo je zlomek se jmenovatelem 10, 100, …, který se zkrátí (1,4 = 14/10 = 7/5); zlomek se převádí zpět rozšířením na jmenovatele 10 nebo 100, nebo dělením. Typická chyba: 0,3 = 1/3, nebo počítat s oběma zápisy najednou bez převodu. |
| 2 | Mocnina a odmocnina zlomku | postup | Násobení a dělení zlomků (POC.ZLOM), Druhá odmocnina (POC.VYR) | 6 · 4 | 0,5 |  | 28 % | [2024 A 4.1](../backend/data/screenshots/M9-2024-A-04.png) 9 % · [2023 A 4.2](../backend/data/screenshots/M9-2023-A-04.png) 34 % · [2025 B 2](../backend/data/screenshots/M9-2025-B-02.png) 34 % | Zlomek se umocní tak, že se umocní čitatel i jmenovatel; odmocnina zlomku je odmocnina čitatele lomená odmocninou jmenovatele. Typická chyba: umocnit jen čitatel, (3/2)² = 9/2. |
| 3 | Smíšené číslo | postup | Sčítání a odčítání (POC.ZLOM) | 1 · 1 | 0,1 |  | 34 % | [2025 B 2](../backend/data/screenshots/M9-2025-B-02.png) 34 % | Smíšené číslo je součet celého čísla a zlomku, 6 1/4 = 25/4; před násobením, dělením a odmocňováním se převede na zlomek. Typická chyba: číst je jako součin (6 · 1/4), nebo násobit celé části a zlomky zvlášť. |
| S | Porovnávání zlomků | postup |  |  |  |  |  |  | Specifikace B1, 1: „porovnává zlomky“. |

### Jednotky

`POC.JED` · 1,9 points per standard test, in 10 of 16 · success 49 % · specification area 1

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 2 | Jednotky délky | znalost | Počítání s desetinnými čísly (POC.VYR) | 6 · 4 | 0,9 | 8 · 5 · 1,1 | 48 % | [2024 B 1](../backend/data/screenshots/M9-2024-B-01.png) 50 % | mm, cm, dm a m se liší desetkrát, 1 km = 1 000 m; při převodu na menší jednotku se násobí, na větší dělí. Typická chyba: počítat s údaji v různých jednotkách bez převodu, nebo posunout desetinnou čárku opačným směrem. |
| 3 | Jednotky obsahu | znalost | Jednotky délky (POC.JED) | 2 · 1 | 0,1 |  | 34 % | [2022 A 2.1](../backend/data/screenshots/M9-2022-A-02.png) 28 % · [2026 B 1](../backend/data/screenshots/M9-2026-B-01.png) 41 % | Sousední jednotky obsahu se liší stokrát: 1 dm² = 100 cm², 1 m² = 100 dm² = 10 000 cm². Typická chyba: převádět jako délku, po deseti (0,1 m² = 10 cm²). |
| 3 | Jednotky objemu, litry | znalost | Jednotky délky (POC.JED) | 3 · 1 | 0,2 |  | 25 % | [2023 A 2.2](../backend/data/screenshots/M9-2023-A-02.png) 24 % · [2022 A 2.2](../backend/data/screenshots/M9-2022-A-02.png) 39 % | Sousední jednotky objemu se liší tisíckrát: 1 dm³ = 1 000 cm³, 1 m³ = 1 000 dm³; 1 l = 1 dm³, 1 ml = 1 cm³. Typická chyba: převádět po deseti nebo po stu, nebo neznat vztah litru a dm³. |
| 3 | Jednotky hmotnosti | znalost | Počítání s desetinnými čísly (POC.VYR) | 2 · 1 | 0,2 |  | – |  | 1 kg = 1 000 g, 1 t = 1 000 kg. Typická chyba: počítat s gramy a kilogramy zároveň bez převodu, nebo posunout desetinnou čárku opačným směrem. |
| 2 | Jednotky času | znalost |  | 5 · 3 | 0,5 |  | 75 % | [2022 A 11.2](../backend/data/screenshots/M9-2022-A-11.png) 64 % · [2022 A 11.1](../backend/data/screenshots/M9-2022-A-11.png) 87 % | 1 h = 60 min, 1 min = 60 s, 1 den = 24 h, 1 týden = 7 dní; čas není v desítkové soustavě: 2,4 h = 2 h 24 min, 36 min = 0,6 h. Typická chyba: 1,5 h = 1 h 50 min, nebo sčítat hodiny a minuty jako desetinné číslo. |
| 3 | Stupně a minuty | znalost |  | 0 · 0 | 0,0 |  | – |  | 1° = 60′; stupně a minuty se sčítají a odčítají zvlášť, při odčítání se jeden stupeň rozmění na 60 minut. Typická chyba: počítat s minutami jako s desetinami stupně (126°30′ = 126,3°). |

## Výrazy a rovnice (ALG)

10,1 points per standard test · success 46 % · Úpravy výrazů s proměnnou a řešení lineárních rovnic a soustav.

### Výrazy

`ALG.VYR` · 7,4 points per standard test, in 16 of 16 · success 47 % · specification area 1

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 3 | Dosazení čísla do výrazu | postup | Pořadí operací a závorky (POC.VYR), Druhá mocnina čísla (POC.VYR) | 1 · 1 | 0,1 |  | 48 % | [2026 A 3.1](../backend/data/screenshots/M9-2026-A-03.png) 48 % | Za proměnnou se dosadí číslo (záporné číslo a zlomek v závorce) a výraz se vypočítá podle pořadí operací. Typická chyba: 9x² pro x = 7 počítat jako (9 · 7)², nebo dosadit záporné číslo bez závorky. |
| 1 | Sloučení členů, minus před závorkou | postup | Počítání se zápornými čísly (POC.VYR) | 16 · 8 | 3,3 | 16 · 8 · 13,5 | 47 % | [2024 A 4.1](../backend/data/screenshots/M9-2024-A-04.png) 9 % | Sčítat lze jen členy se stejnou proměnnou ve stejné mocnině; minus před závorkou mění znaménko každého členu v závorce. Typická chyba: změnit znaménko jen u prvního členu, nebo sloučit x² a x. |
| 1 | Násobení jednočlenů a mnohočlenů (roznásobení závorek) | postup | Sloučení členů (ALG.VYR) | 16 · 8 | 6,2 | 16 · 8 · 8,3 | 48 % | [2024 A 4.3](../backend/data/screenshots/M9-2024-A-04.png) 32 % · [2025 A 3.2](../backend/data/screenshots/M9-2025-A-03.png) 32 % · [2025 B 4.3](../backend/data/screenshots/M9-2025-B-04.png) 48 % | Jednočleny se násobí koeficient s koeficientem a proměnná s proměnnou (x · x = x²); mnohočleny každý člen s každým. Typická chyba: roznásobit jen první člen závorky, nebo ztratit znaménko některého součinu. |
| 1 | Vzorec (a ± b)² | postup | Násobení jednočlenů a mnohočlenů (roznásobení závorek) (ALG.VYR) | 12 · 5 | 0,9 | 14 · 6 · 1,1 | 40 % | [2025 B 4.1](../backend/data/screenshots/M9-2025-B-04.png) 32 % · [2023 A 4.2](../backend/data/screenshots/M9-2023-A-04.png) 34 % · [2022 A 4.2](../backend/data/screenshots/M9-2022-A-04.png) 34 % | (a ± b)² = a² ± 2ab + b²; za a, b mohou stát i zlomky, desetinná čísla a záporné členy. Typická chyba: zapomenout prostřední člen, (a + b)² = a² + b², nebo umocnit jen proměnnou a ne koeficient, (3x)² = 3x². |
| 2 | Vytýkání | postup | Násobení jednočlenů a mnohočlenů (roznásobení závorek) (ALG.VYR) | 8 · 3 | 0,5 |  | 42 % | [2023 A 4.1](../backend/data/screenshots/M9-2023-A-04.png) 38 % · [2022 B 4.1](../backend/data/screenshots/M9-2022-B-04.png) 38 % · [2023 B 4.1](../backend/data/screenshots/M9-2023-B-04.png) 46 % | Společný činitel všech členů se napíše před závorku a každý člen se jím vydělí; zpětné roznásobení je kontrola. Typická chyba: po vytknutí celého členu nenechat v závorce 1, nebo při vytýkání záporného činitele nezměnit znaménka. |
| 2 | Rozklad a² − b² na součin | postup | Násobení jednočlenů a mnohočlenů (roznásobení závorek) (ALG.VYR), Druhá mocnina čísla (POC.VYR) | 7 · 4 | 0,5 |  | 47 % | [2024 B 4.2](../backend/data/screenshots/M9-2024-B-04.png) 23 % · [2026 A 3.2](../backend/data/screenshots/M9-2026-A-03.png) 46 % · [2023 B 4.2](../backend/data/screenshots/M9-2023-B-04.png) 46 % | a² − b² = (a + b) · (a − b); oba členy se nejdřív zapíší jako druhé mocniny, 9a² = (3a)². Typická chyba: rozkládat i součet a² + b², nebo odmocnit jen proměnnou a ne koeficient. |
| 3 | Rozklad trojčlenu podle (a ± b)², doplnění | postup | Vzorec (a ± b)² (ALG.VYR) | 2 · 1 | 0,1 |  | 65 % | [2025 A 3.1](../backend/data/screenshots/M9-2025-A-03.png) 65 % | Trojčlen a² ± 2ab + b² je druhá mocnina dvojčlenu; chybějící číslo se určí z prostředního členu, který je dvojnásobkem součinu obou členů. Typická chyba: brát prostřední člen jako součin bez dvojky, nebo nalezené číslo neumocnit. |

### Rovnice

`ALG.ROV` · 6,0 points per standard test, in 16 of 16 · success 46 % · specification area 1

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Ekvivalentní úpravy rovnice | postup | Sloučení členů (ALG.VYR) | 16 · 8 | 5,6 | 16 · 8 · 9,4 | 46 % | [2024 A 5.1](../backend/data/screenshots/M9-2024-A-05.png) 35 % · [2022 A 5.1](../backend/data/screenshots/M9-2022-A-05.png) 46 % · [2024 B 5.1](../backend/data/screenshots/M9-2024-B-05.png) 48 % | Rovnice se nezmění, když se k oběma stranám přičte stejný výraz nebo se obě strany vynásobí či vydělí stejným nenulovým číslem; cílem je neznámá na jedné straně a čísla na druhé. Typická chyba: při převodu členu na druhou stranu nezměnit znaménko, nebo vydělit jen část strany. |
| 1 | Odstranění zlomků z rovnice | postup | Ekvivalentní úpravy rovnice (ALG.ROV), Společný násobek a dělitel (POC.DEL), Násobení jednočlenů a mnohočlenů (roznásobení závorek) (ALG.VYR) | 14 · 6 | 2,9 |  | 50 % | [2024 A 5.2](../backend/data/screenshots/M9-2024-A-05.png) 27 % · [2025 A 4.1](../backend/data/screenshots/M9-2025-A-04.png) 33 % · [2025 B 5.1](../backend/data/screenshots/M9-2025-B-05.png) 38 % | Obě strany se vynásobí společným jmenovatelem všech zlomků; násobí se každý člen, i ten bez zlomku, a čitatel o více členech zůstává v závorce. Typická chyba: nevynásobit člen bez zlomku, nebo u zlomku s minusem před ním změnit znaménko jen prvnímu členu čitatele. |
| 3 | Rovnice bez řešení a s nekonečně mnoha řešeními | znalost | Ekvivalentní úpravy rovnice (ALG.ROV) | 2 · 1 | 0,2 |  | 45 % | [2025 A 4.2](../backend/data/screenshots/M9-2025-A-04.png) 36 % · [2023 A 5.1](../backend/data/screenshots/M9-2023-A-05.png) 54 % | Když neznámá při úpravách vypadne, rozhoduje zbylá rovnost: nepravdivá (5 = 7,5) znamená, že rovnice nemá řešení, pravdivá (0 = 0), že jich má nekonečně mnoho. Typická chyba: napsat x = 0, nebo nenapsat žádný závěr. |
| 2 | Soustava dvou rovnic | postup | Ekvivalentní úpravy rovnice (ALG.ROV) | 4 · 4 | 0,8 |  | 51 % | [2025 B 5.2](../backend/data/screenshots/M9-2025-B-05.png) 58 % · [2026 A 4.2](../backend/data/screenshots/M9-2026-A-04.png) 60 % | Dosazovací metoda: z jedné rovnice se vyjádří neznámá a dosadí do druhé; sčítací metoda: rovnice se sečtou nebo odečtou tak, aby jedna neznámá vypadla. Typická chyba: dopočítat jen jednu neznámou, nebo při odečítání rovnic nezměnit všechna znaménka. |

## Vztahy mezi veličinami (VZT)

19,5 points per standard test · success 42 % · Tentýž vztah mezi veličinami vyjádřený zlomkem, srovnáním, procentem nebo poměrem, a jeho převod z textu do výpočtu.

### Zlomek jako část celku

`VZT.CAST` · 4,1 points per standard test, in 13 of 16 · success 40 % · specification area 1

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Zlomek z čísla | překlad | Násobení a dělení zlomků (POC.ZLOM) | 7 · 2 | 1,2 | 16 · 8 · 6,4 | 47 % | [2023 B 6.1](../backend/data/screenshots/M9-2023-B-06.png) 56 % · [2022 A 11.2](../backend/data/screenshots/M9-2022-A-11.png) 64 % · [2022 A 11.3](../backend/data/screenshots/M9-2022-A-11.png) 71 % | Zlomek z čísla: dělit jmenovatelem a násobit čitatelem, 3/5 ze 110 = 110 : 5 · 3. Typická chyba: dělit čitatelem a násobit jmenovatelem, nebo zlomek odečíst jako číslo. |
| 2 | Jakou částí celku je | překlad | Krácení (POC.ZLOM) | 3 · 3 | 0,3 |  | 2 % | [2026 B 16.3](../backend/data/screenshots/M9-2026-B-16.png) 2 % | Jakou částí celku je daná část: část lomeno celkem, zkráceno (36 ze 60 je 3/5). Typická chyba: dát do jmenovatele zbytek místo celku. |
| 1 | Zbytek celku a část ze zbytku | překlad | Zlomek z čísla (VZT.CAST) | 12 · 7 | 2,6 |  | 40 % | [2026 A 6.1](../backend/data/screenshots/M9-2026-A-06.png) 38 % · [2022 B 15.2](../backend/data/screenshots/M9-2022-B-15.png) 40 % | Celek je 1 (nebo 100 %): po odebrání části zbývá 1 minus tato část, a „zlomek zbytku“ se počítá z toho, co zbylo. Typická chyba: počítat část ze zbytku z původního celku. |
| 3 | Zlomek ze zlomku | překlad | Zlomek z čísla (VZT.CAST) | 3 · 2 | 0,3 |  | 30 % | [2026 A 6.2](../backend/data/screenshots/M9-2026-A-06.png) 17 % · [2023 B 15.2](../backend/data/screenshots/M9-2023-B-15.png) 50 % | „Zlomek ze zlomku“ je součin: tři čtvrtiny ze tří pětin jsou 3/4 · 3/5. Typická chyba: zlomky sečíst nebo odečíst. |
| 1 | Celek z části | překlad | Zlomek z čísla (VZT.CAST) | 10 · 6 | 1,4 |  | 30 % | [2025 B 7.3](../backend/data/screenshots/M9-2025-B-07.png) 13 % · [2023 A 2.1](../backend/data/screenshots/M9-2023-A-02.png) 30 % · [2022 B 6](../backend/data/screenshots/M9-2022-B-06.png) 32 % | Je-li známá část a její zlomek, vypočítá se nejdřív jeden díl (dělit čitatelem) a z něj celek (násobit jmenovatelem): 60 l jsou 2/3, celek je 60 : 2 · 3. Typická chyba: počítat zlomek ze známé části, místo aby se hledal celek. |

### Srovnání

`VZT.NEZ` · 4,3 points per standard test, in 15 of 16 · success 35 % · specification area 1 · Obraty „o … více než“ a „kolikrát“, které se vracejí ve zlomcích, procentech i slovních úlohách.

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | „o kolik“ je rozdíl, „kolikrát“ je podíl | překlad |  | 11 · 6 | 1,7 | 15 · 8 · 5,7 | 44 % | [2023 A 2.1](../backend/data/screenshots/M9-2023-A-02.png) 30 % · [2022 A 14](../backend/data/screenshots/M9-2022-A-14.png) 35 % · [2022 A 2.2](../backend/data/screenshots/M9-2022-A-02.png) 39 % | „O kolik“ se ptá na rozdíl, „kolikrát“ na podíl; „třikrát více“ je násobení, „třikrát méně“ dělení. Typická chyba: odpovědět rozdílem na otázku „kolikrát“, nebo „dvakrát méně“ počítat odečtením. |
| 1 | „o třetinu více / méně než“ jako násobení | překlad | Zlomek z čísla (VZT.CAST) | 13 · 7 | 2,5 | 13 · 7 · 2,9 | 29 % | [2025 B 7.2](../backend/data/screenshots/M9-2025-B-07.png) 12 % · [2025 B 7.1](../backend/data/screenshots/M9-2025-B-07.png) 19 % · [2023 B 7.2](../backend/data/screenshots/M9-2023-B-07.png) 39 % | „O třetinu více než x“ je x + x/3 = 4/3 · x, „o třetinu méně“ 2/3 · x; zlomek se bere z veličiny za slovem „než“. Typická chyba: přičíst zlomek jako číslo (x + 1/3), nebo ho vzít z nesprávné veličiny. |
| 2 | Obrácení vztahu: neznámá je za „než“ | překlad | „o kolik“ je rozdíl (VZT.NEZ), „o třetinu více / méně než“ jako násobení (VZT.NEZ) | 8 · 5 | 0,9 |  | 28 % | [2025 B 15.2](../backend/data/screenshots/M9-2025-B-15.png) 12 % · [2023 A 15.2](../backend/data/screenshots/M9-2023-A-15.png) 28 % · [2026 A 5](../backend/data/screenshots/M9-2026-A-05.png) 28 % | Vztah lze číst oběma směry: je-li A o polovinu levnější než B, je B dvakrát dražší než A; je-li A 4/3 veličiny B, je B 3/4 veličiny A. Typická chyba: obrátit „o třetinu méně“ na „o třetinu více“ – opačný vztah má jiný zlomek, protože se počítá z jiného základu. |

### Procenta

`VZT.PROC` · 7,1 points per standard test, in 16 of 16 · success 49 % · specification area 1

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Procentová část | postup | Počítání s desetinnými čísly (POC.VYR) | 6 · 5 | 0,8 | 16 · 8 · 7,5 | 53 % | [2025 A 5.2](../backend/data/screenshots/M9-2025-A-05.png) 34 % | 1 % je setina základu; procentová část = základ : 100 · počet procent (25 % z 24 je 6). Typická chyba: brát procenta z jiného základu, než ke kterému se vztahují. |
| 1 | Počet procent | postup | Procentová část (VZT.PROC) | 5 · 4 | 0,8 | 10 · 6 · 2,3 | 49 % | [2024 B 15.2](../backend/data/screenshots/M9-2024-B-15.png) 65 % · [2025 A 15.1](../backend/data/screenshots/M9-2025-A-15.png) 71 % · [2024 B 16.3](../backend/data/screenshots/M9-2024-B-16.png) 78 % | Počet procent = část : základ · 100 (8 z 50 je 16 %). Typická chyba: dělit základ částí, nebo vzít za základ nesprávné číslo. |
| 1 | Základ z procentové části | postup | Procentová část (VZT.PROC) | 7 · 3 | 1,1 | 10 · 5 · 2,0 | 48 % | [2023 A 15.3](../backend/data/screenshots/M9-2023-A-15.png) 36 % · [2026 B 15.2](../backend/data/screenshots/M9-2026-B-15.png) 62 % · [2026 A 11.3](../backend/data/screenshots/M9-2026-A-11.png) 62 % | Základ = část : počet procent · 100: nejdřív 1 %, pak 100 % (30 je 10 %, základ je 300). Typická chyba: počítat procenta ze známé části, místo aby se hledal základ. |
| 2 | Procento, zlomek a poměr: převody | znalost | Procentová část (VZT.PROC), Krácení (POC.ZLOM) | 7 · 3 | 1,1 |  | 61 % | [2024 B 16.1](../backend/data/screenshots/M9-2024-B-16.png) 67 % · [2025 B 15.1](../backend/data/screenshots/M9-2025-B-15.png) 80 % | Procento je setina: 20 % = 1/5, 25 % = 1/4, 50 % = 1/2, 75 % = 3/4; „každý dvacátý“ je 1/20 = 5 %, poměr 3 : 2 znamená o 50 % více. Typická chyba: 1/20 = 20 %. |
| 1 | „o x % více / méně“ jako násobitel | překlad | Procentová část (VZT.PROC) | 10 · 5 | 2,0 | 11 · 5 · 2,9 | 49 % | [2022 A 15.3](../backend/data/screenshots/M9-2022-A-15.png) 19 % · [2023 A 8.1](../backend/data/screenshots/M9-2023-A-08.png) 28 % · [2025 A 15.3](../backend/data/screenshots/M9-2025-A-15.png) 31 % | Zvýšení o x % je násobení číslem 1 + x/100, snížení číslem 1 − x/100: o 25 % více je · 1,25, o 40 % méně · 0,6, o 150 % více · 2,5. Typická chyba: násobit jen samotnými procenty (· 0,25), nebo brát „o 150 % více“ jako 1,5násobek. |
| 2 | Základ po změně | překlad | „o x % více / méně“ jako násobitel (VZT.PROC), Základ z procentové části (VZT.PROC) | 7 · 3 | 1,0 |  | 35 % | [2022 A 15.2](../backend/data/screenshots/M9-2022-A-15.png) 32 % · [2026 B 15.1](../backend/data/screenshots/M9-2026-B-15.png) 42 % | Je-li známá hodnota po změně, původní hodnota se získá dělením násobitelem: 420 je o 40 % více než původně, tedy 420 : 1,4. Typická chyba: odečíst 40 % ze 420 – procenta se počítají z původní hodnoty, ne z nové. |
| 2 | O kolik procent se liší dvě veličiny | překlad | Počet procent (VZT.PROC), „o kolik“ je rozdíl (VZT.NEZ) | 8 · 4 | 1,4 |  | 44 % | [2023 A 7.1](../backend/data/screenshots/M9-2023-A-07.png) 11 % · [2022 B 15.3](../backend/data/screenshots/M9-2022-B-15.png) 24 % · [2026 B 5.2](../backend/data/screenshots/M9-2026-B-05.png) 32 % | O kolik procent je A větší nebo menší než B: rozdíl dělený veličinou za slovem „než“. Typická chyba: dělit rozdíl nesprávnou veličinou, nebo odpovědět podílem místo rozdílu (trojnásobek je o 200 % více, ne o 300 %). |
| 3 | Dvě změny po sobě | postup | „o x % více / méně“ jako násobitel (VZT.PROC) | 2 · 1 | 0,2 |  | 62 % | [2023 A 15.1](../backend/data/screenshots/M9-2023-A-15.png) 50 % · [2024 A 16.3](../backend/data/screenshots/M9-2024-A-16.png) 64 % · [2024 B 11](../backend/data/screenshots/M9-2024-B-11.png) 73 % | Druhá změna se počítá z hodnoty po první změně, násobitele se násobí: +40 % a pak −40 % je · 1,4 · 0,6 = 0,84. Typická chyba: procenta sečíst nebo odečíst (+20 % a +20 % není +40 %). |
| 3 | Úrok a daň z úroku | postup | Procentová část (VZT.PROC) | 0 · 0 | 0,0 |  | 61 % | [2024 A 16.2](../backend/data/screenshots/M9-2024-A-16.png) 50 % · [2024 A 16.1](../backend/data/screenshots/M9-2024-A-16.png) 73 % | Úrok je procentová část vkladu podle roční úrokové míry; daň z úroku se odečítá z úroku, ne z vkladu. Typická chyba: počítat daň z celé částky. |
| S | Promile | znalost |  |  |  |  |  |  | Specifikace B1, 1: „rozlišuje a využívá pojmy procento, základ, počet procent, procentová část, promile“. |
| S | Jistina, úroková míra, úrokovací období, inflace; půjčky a úvěry | znalost |  |  |  |  |  |  | Specifikace C1, 1: „používá s porozuměním základní pojmy finanční matematiky“, „získá základní informace o půjčkách a úvěrech“. |

### Poměr a úměrnost

`VZT.POM` · 3,3 points per standard test, in 15 of 16 · success 39 % · specification area 1, 2, 3

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 2 | Poměr: zápis, krácení | postup | Krácení (POC.ZLOM) | 5 · 3 | 0,5 | 8 · 4 · 1,3 | 37 % | [2022 B 2.1](../backend/data/screenshots/M9-2022-B-02.png) 22 % · [2026 A 11.2](../backend/data/screenshots/M9-2026-A-11.png) 65 % | Poměr a : b porovnává dvě veličiny podílem; krátí a rozšiřuje se jako zlomek, obě veličiny musí být ve stejných jednotkách a záleží na pořadí. Typická chyba: obrácené pořadí členů, nebo nezkrácený poměr. |
| 2 | Díly poměru: z celku, části nebo rozdílu | postup | Poměr (VZT.POM) | 6 · 2 | 0,6 |  | 26 % | [2023 A 7.3](../backend/data/screenshots/M9-2023-A-07.png) 13 % · [2022 B 2.2](../backend/data/screenshots/M9-2022-B-02.png) 25 % · [2025 A 15.2](../backend/data/screenshots/M9-2025-A-15.png) 30 % | Poměr 3 : 5 znamená 3 a 5 stejných dílů; velikost dílu se určí z toho, co je známo: z celku (8 dílů), z jedné části, nebo z rozdílu (2 díly). Typická chyba: dělit známé číslo nesprávným počtem dílů, např. rozdíl dělit součtem dílů. |
| 3 | Měřítko mapy a plánu | postup | Poměr (VZT.POM), Jednotky délky (POC.JED) | 1 · 0 | 0,2 | 1 · 0 · 0,2 | 59 % | [2023 A 11.2](../backend/data/screenshots/M9-2023-A-11.png) 51 % · [2023 A 11.3](../backend/data/screenshots/M9-2023-A-11.png) 61 % · [2024 A 15.1](../backend/data/screenshots/M9-2024-A-15.png) 64 % | Měřítko 1 : 20 000 znamená, že 1 cm na mapě je 20 000 cm = 200 m ve skutečnosti; obě délky se před výpočtem převedou na stejnou jednotku. Typická chyba: chyba v převodu centimetrů na metry a kilometry, nebo násobení místo dělení. |
| 3 | Měřítko a obsah: druhá mocnina | znalost | Měřítko mapy a plánu (VZT.POM), Druhá mocnina čísla (POC.VYR) | 0 · 0 | 0,0 |  | 42 % | [2024 A 15.3](../backend/data/screenshots/M9-2024-A-15.png) 42 % | Obsahy se mění s druhou mocninou měřítka: při měřítku 1 : 100 je obsah na plánu 10 000krát menší než ve skutečnosti. Typická chyba: použít pro obsah stejný poměr jako pro délky. |
| 1 | Přímá úměrnost | postup | „o kolik“ je rozdíl (VZT.NEZ) | 8 · 6 | 1,3 | 13 · 7 · 2,3 | 48 % | [2026 A 7.2](../backend/data/screenshots/M9-2026-A-07.png) 25 % · [2022 A 7.1](../backend/data/screenshots/M9-2022-A-07.png) 54 % · [2026 B 5.1](../backend/data/screenshots/M9-2026-B-05.png) 64 % | Kolikrát se zvětší jedna veličina, tolikrát se zvětší druhá; počítá se přes jednotku (1 km za 6 minut) nebo trojčlenkou. Typická chyba: použít přímou úměrnost tam, kde jde o nepřímou. |
| 2 | Nepřímá úměrnost | postup | Přímá úměrnost (VZT.POM) | 4 · 1 | 0,6 |  | 17 % | [2024 A 1](../backend/data/screenshots/M9-2024-A-01.png) 18 % · [2023 B 6.2](../backend/data/screenshots/M9-2023-B-06.png) 23 % · [2022 A 7.2](../backend/data/screenshots/M9-2022-A-07.png) 39 % | Kolikrát se zvětší jedna veličina, tolikrát se zmenší druhá; jejich součin zůstává stejný (dělníci · dny = práce). Typická chyba: počítat jako přímou úměrnost – více dělníků, více dní. |
| 3 | Společná práce: sčítají se výkony | postup | Přímá úměrnost (VZT.POM) | 2 · 1 | 0,2 |  | 9 % | [2022 A 7.3](../backend/data/screenshots/M9-2022-A-07.png) 9 % | Při společné práci se sčítají výkony, tedy práce za jednotku času, ne časy: 1/24 + 1/40 = 1/15 za minutu, společně 15 minut. Typická chyba: sečíst nebo zprůměrovat časy. |
| 3 | Pohyb: s = v · t | postup | Přímá úměrnost (VZT.POM) | 2 · 2 | 0,2 |  | 28 % | [2026 A 7.1](../backend/data/screenshots/M9-2026-A-07.png) 34 % | s = v · t, v = s : t, t = s : v; čas a rychlost musí být ve stejných jednotkách (km/h a hodiny). Za stejný čas jsou dráhy ve stejném poměru jako rychlosti. Typická chyba: dosadit minuty k rychlosti v km/h, nebo dělit v opačném pořadí. |
| 3 | Směsi a průměrná cena | postup | Přímá úměrnost (VZT.POM) | 1 · 0 | 0,2 |  | – |  | Cena směsi je součet cen složek; cena za kilogram je celková cena dělená celkovou hmotností, tedy průměr vážený množstvím. Typická chyba: zprůměrovat ceny za kilogram bez ohledu na množství. |
| S | Postupný a převrácený poměr, změna čísla v daném poměru | postup |  |  |  |  |  |  | Specifikace B1, 1: „změní číslo v daném poměru“, „zapíše a upraví postupný a převrácený poměr“. |
| S | Přímá a nepřímá úměrnost tabulkou, rovnicí a grafem | postup |  |  |  |  |  |  | Specifikace C1, 2: „vyjádří přímou a nepřímou úměrnost tabulkou, rovnicí a grafem“. |

### Slovní úlohy

`VZT.SLOV` · 7,6 points per standard test, in 16 of 16 · success 31 % · specification area 1

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 2 | Rozbor textu: řetěz jednoduchých výpočtů | rozbor |  | 5 · 3 | 0,6 |  | – |  | Text se rozloží na řetěz jednoduchých výpočtů bez rovnice: co je známo, co z toho plyne, co se má zjistit. Uvádí se jen tam, kde úlohu nevystihuje žádný jiný princip. Typická chyba: vynechat krok, nebo odpovědět mezivýsledkem. |
| 1 | Vyjádření veličiny výrazem s proměnnou | překlad |  | 14 · 7 | 2,0 | 16 · 8 · 8,7 | 38 % | [2022 A 8.2](../backend/data/screenshots/M9-2022-A-08.png) 28 % · [2022 B 14](../backend/data/screenshots/M9-2022-B-14.png) 37 % · [2022 A 8.1](../backend/data/screenshots/M9-2022-A-08.png) 39 % | Veličina se zapíše výrazem s danou proměnnou podle vztahu v textu (čtvrtina x je x/4, o 12 více je x + 12); výsledkem je výraz, ne číslo. Typická chyba: zapsat vztah obráceně, nebo dosadit za proměnnou konkrétní číslo. |
| 1 | Sestavení rovnice ze zadání | rozbor | Vyjádření veličiny výrazem s proměnnou (VZT.SLOV), Ekvivalentní úpravy rovnice (ALG.ROV) | 14 · 8 | 4,7 | 15 · 8 · 5,4 | 28 % | [2023 B 6.3](../backend/data/screenshots/M9-2023-B-06.png) 2 % · [2025 B 8.3](../backend/data/screenshots/M9-2025-B-08.png) 5 % · [2026 A 6.3](../backend/data/screenshots/M9-2026-A-06.png) 10 % | Neznámá se označí, ostatní veličiny se jí vyjádří a podmínka ze zadání se zapíše jako rovnost; odpovídá se na veličinu, na kterou se zadání ptá. Typická chyba: sestavit rovnici z nesprávné podmínky, nebo odpovědět hodnotou x, když se zadání ptá na jinou veličinu. |
| 2 | Dvě neznámé: dvě podmínky, součet a rozdíl | rozbor | Sestavení rovnice ze zadání (VZT.SLOV) | 6 · 5 | 1,1 |  | 18 % | [2026 B 12](../backend/data/screenshots/M9-2026-B-12.png) 20 % · [2025 B 15.3](../backend/data/screenshots/M9-2025-B-15.png) 34 % | Dvě neznámé vyžadují dvě podmínky; ze součtu a rozdílu se neznámé určí sečtením a odečtením podmínek, jinak dosazením jedné do druhé. Typická chyba: použít jen jednu podmínku, nebo zaměnit, která neznámá je větší. |
| 3 | Podmínka celého čísla | rozbor | Dělitelé a násobky čísla (POC.DEL) | 2 · 2 | 0,4 |  | – |  | Počet kusů nebo osob musí být celé nezáporné číslo; tato podmínka vybírá jen ty možnosti, kde dělení vyjde beze zbytku. Typická chyba: přijmout necelý výsledek, nebo najít jen jednu z více možností. |

## Grafy, tabulky, průměr (DAT)

3,4 points per standard test · success 52 % · Čtení grafů, diagramů a tabulek a aritmetický průměr.

### Grafy a tabulky

`DAT.GRAF` · 2,9 points per standard test, in 13 of 16 · success 53 % · specification area 2

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Čtení hodnot z grafu nebo diagramu | postup |  | 10 · 5 | 2,3 | 13 · 7 · 2,9 | 47 % | [2024 B 15.1](../backend/data/screenshots/M9-2024-B-15.png) 77 % | Hodnota se čte podle stupnice osy a legendy; u grafu s více řadami a u skládaného sloupce se nejdřív určí, která řada a který úsek se čte. Typická chyba: číst jinou řadu, nebo u skládaného sloupce číst horní okraj místo výšky úseku. |
| 3 | Třídění údajů do tabulky | postup |  | 0 · 0 | 0,0 |  | 56 % | [2024 A 7.1](../backend/data/screenshots/M9-2024-A-07.png) 56 % · [2024 A 7.2](../backend/data/screenshots/M9-2024-A-07.png) 56 % | Údaje z textu se roztřídí do tabulky podle dvou hledisek (např. jazyk a chlapci/dívky); součty řádků a sloupců doplní chybějící pole. Typická chyba: zapsat údaj do nesprávného pole, nebo některou skupinu započítat dvakrát. |
| 3 | Kruhový diagram: části jako procenta a úhly | postup | Čtení hodnot z grafu nebo diagramu (DAT.GRAF), Procentová část (VZT.PROC) | 3 · 2 | 0,6 |  | 61 % | [2025 B 11.2](../backend/data/screenshots/M9-2025-B-11.png) 59 % · [2025 B 11.1](../backend/data/screenshots/M9-2025-B-11.png) 70 % · [2026 A 11.1](../backend/data/screenshots/M9-2026-A-11.png) 71 % | Celý kruh je 100 % a 360°: výseči 90° odpovídá čtvrtina, 1 % je 3,6°; části se mezi sebou přepočítávají úměrou. Typická chyba: brát stupně jako procenta, nebo nedopočítat chybějící výseč do celku. |
| 3 | Graf bez stupnice: hodnota dílku z podmínky | rozbor | Čtení hodnot z grafu nebo diagramu (DAT.GRAF), Přímá úměrnost (VZT.POM) | 2 · 1 | 0,2 |  | 18 % | [2023 A 7.2](../backend/data/screenshots/M9-2023-A-07.png) 18 % | Když osa nemá čísla, hodnoty se vyjádří v dílcích a velikost dílku se určí z podmínky v textu (2 dílky = 6 žáků, dílek jsou 3 žáci). Typická chyba: považovat dílek za 1. |
| 2 | Dopočet chybějícího údaje ze vztahu mezi údaji | rozbor | Čtení hodnot z grafu nebo diagramu (DAT.GRAF) | 5 · 4 | 1,0 |  | 60 % | [2026 B 11.2](../backend/data/screenshots/M9-2026-B-11.png) 50 % · [2026 B 11.3](../backend/data/screenshots/M9-2026-B-11.png) 56 % · [2026 B 11.1](../backend/data/screenshots/M9-2026-B-11.png) 73 % | Chybějící údaj se dopočítá ze vztahu, který dává text: stav = předchozí stav + přírůstek − úbytek, daný součet nebo rovnost. Typická chyba: číst jen graf a vztah z textu nepoužít, nebo ho použít s opačným znaménkem. |
| S | Statistický soubor, statistický znak, statistické šetření, četnost | znalost |  |  |  |  |  |  | Specifikace C1, 2: „používá s porozuměním základní statistické pojmy (statistický soubor, statistický znak, statistické šetření), určí četnost, aritmetický průměr“. |
| S | Volba vhodné tabulky a diagramu, vytvoření diagramu z dat | postup |  |  |  |  |  |  | Specifikace C1, 2: „zvolí vhodnou tabulku a vhodný diagram“; B1, 2: „vytvoří vhodný diagram ze vstupních dat“. |
| S | Bod v pravoúhlé soustavě souřadnic | postup |  |  |  |  |  |  | Specifikace B1, 2: „vyznačí bod v pravoúhlé soustavě souřadnic …, zapíše souřadnice daného bodu“. |

### Aritmetický průměr

`DAT.PRUM` · 1,1 points per standard test, in 7 of 16 · success 42 % · specification area 2

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 2 | Aritmetický průměr | postup |  | 4 · 3 | 0,4 | 7 · 5 · 1,1 | 45 % | [2026 A 1.3](../backend/data/screenshots/M9-2026-A-01.png) 37 % · [2022 B 7.1](../backend/data/screenshots/M9-2022-B-07.png) 49 % | Aritmetický průměr je součet hodnot dělený jejich počtem. Typická chyba: dělit nesprávným počtem, nebo vynechat nulovou hodnotu. |
| 3 | Průměr z četností | postup | Aritmetický průměr (DAT.PRUM) | 3 · 2 | 0,5 |  | 35 % | [2022 A 14](../backend/data/screenshots/M9-2022-A-14.png) 35 % | Opakuje-li se hodnota, násobí se četností: součet součinů hodnota · četnost dělený součtem četností. Typická chyba: zprůměrovat jen různé hodnoty bez četností, nebo dělit počtem různých hodnot. |
| 2 | Součet z průměru, chybějící hodnota | postup | Aritmetický průměr (DAT.PRUM) | 4 · 3 | 0,6 |  | 43 % | [2025 A 14](../backend/data/screenshots/M9-2025-A-14.png) 36 % · [2022 B 7.2](../backend/data/screenshots/M9-2022-B-07.png) 51 % | Součet hodnot = průměr · počet; chybějící hodnota je tento součet minus známé hodnoty. Typická chyba: průměrovat průměr s novou hodnotou, nebo dosadit nesprávný počet hodnot. |

## Geometrie: útvary a konstrukce (KON)

6,9 points per standard test · success 32 % · Základní konstrukce, vlastnosti útvarů, o které se opírají konstrukce i výpočty, a rozbor konstrukční úlohy.

### Základní pojmy a konstrukce

`KON.ZAKL` · 5,1 points per standard test, in 16 of 16 · success 31 % · specification area 3 · Jednotlivé kroky s pravítkem, trojúhelníkem s ryskou, kružítkem a úhloměrem.

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Kolmice daným bodem | postup |  | 9 · 4 | 2,2 | 16 · 8 · 7,5 | 36 % | [2026 A 9](../backend/data/screenshots/M9-2026-A-09.png) 42 % | Kolmice k přímce daným bodem, ať leží na přímce, nebo mimo ni, se rýsuje trojúhelníkem s ryskou; její pata je bod přímky nejbližší danému bodu. Typická chyba: vést kolmici jiným bodem, nebo ji jen odhadnout. |
| 2 | Rovnoběžka daným bodem | postup |  | 5 · 1 | 0,9 | 6 · 1 · 1,1 | 29 % | [2022 B 10](../backend/data/screenshots/M9-2022-B-10.png) 26 % · [2024 B 9](../backend/data/screenshots/M9-2024-B-09.png) 32 % | Rovnoběžka s přímkou daným bodem se rýsuje posunutím trojúhelníku po pravítku; rovnoběžky mají všude stejnou vzdálenost. Typická chyba: vést rovnoběžku od oka. |
| 1 | Střed a osa úsečky | postup | Kolmice daným bodem (KON.ZAKL) | 10 · 5 | 2,2 | 16 · 8 · 4,9 | 26 % | [2025 B 10](../backend/data/screenshots/M9-2025-B-10.png) 9 % · [2025 B 9](../backend/data/screenshots/M9-2025-B-09.png) 19 % · [2026 B 10](../backend/data/screenshots/M9-2026-B-10.png) 22 % | Osa úsečky prochází jejím středem kolmo k ní a tvoří ji všechny body stejně vzdálené od obou krajních bodů; sestrojí se dvěma kružnicemi se stejným poloměrem. Typická chyba: zaměnit osu úsečky s osou úhlu nebo s těžnicí. |
| 1 | Kružnice: body v dané vzdálenosti, přenesení délky | postup |  | 12 · 6 | 2,7 | 16 · 8 · 5,4 | 31 % | [2025 B 10](../backend/data/screenshots/M9-2025-B-10.png) 9 % · [2026 B 9](../backend/data/screenshots/M9-2026-B-09.png) 15 % · [2025 B 9](../backend/data/screenshots/M9-2025-B-09.png) 19 % | Kružnice (S, r) jsou všechny body ve vzdálenosti r od bodu S; kružítkem se délka přenáší a nanáší na přímku. Typická chyba: vzít do kružítka jinou délku, nebo nevyznačit oba průsečíky. |
| 3 | Úhel dané velikosti | postup |  | 2 · 0 | 0,2 |  | 31 % | [2024 A 9](../backend/data/screenshots/M9-2024-A-09.png) 31 % | Úhel dané velikosti se sestrojí úhloměrem u daného vrcholu k danému rameni, 60° a 90° i kružítkem; lze ho vynést na obě strany ramene. Typická chyba: číst nesprávnou stupnici úhloměru (40° místo 140°), nebo úhel sestrojit u jiného vrcholu. |
| 1 | Středová souměrnost | postup | Kružnice (KON.ZAKL) | 9 · 6 | 1,9 | 14 · 7 · 2,7 | 34 % | [2025 B 10](../backend/data/screenshots/M9-2025-B-10.png) 9 % · [2025 A 10](../backend/data/screenshots/M9-2025-A-10.png) 28 % · [2022 A 9](../backend/data/screenshots/M9-2022-A-09.png) 31 % | Obraz bodu X ve středové souměrnosti se středem S leží na polopřímce XS za bodem S ve stejné vzdálenosti; S je střed úsečky XX′. Typická chyba: nanést vzdálenost na jinou přímku, nebo zaměnit střed souměrnosti s osou. |
| 2 | Osová souměrnost, samodružný bod | postup | Kolmice daným bodem (KON.ZAKL) | 6 · 3 | 0,9 | 7 · 3 · 1,4 | 34 % | [2026 B 9](../backend/data/screenshots/M9-2026-B-09.png) 15 % · [2026 A 10](../backend/data/screenshots/M9-2026-A-10.png) 23 % · [2023 B 9](../backend/data/screenshots/M9-2023-B-09.png) 64 % | Obraz bodu v osové souměrnosti leží na kolmici k ose ve stejné vzdálenosti na opačné straně; osa souměrnosti je osou úsečky bod–obraz a body na ose jsou samodružné. Typická chyba: přenést bod jiným směrem než kolmo k ose. |
| S | Přenesení úhlu | postup |  |  |  |  |  |  | Specifikace B1, 3: „přenese úhel, porovná dva úhly“. |
| S | Kružnice opsaná trojúhelníku | postup |  |  |  |  |  |  | Specifikace C1, 3: „sestrojí osu úhlu, osu úsečky, tečnu kružnice v jejím bodě, kružnici opsanou trojúhelníku a využívá Thaletovu kružnici při konstrukci pravoúhlého trojúhelníku“. |
| S | Tečna kružnice v jejím bodě | postup |  |  |  |  |  |  | Specifikace C1, 3: „sestrojí osu úhlu, osu úsečky, tečnu kružnice v jejím bodě, kružnici opsanou trojúhelníku a využívá Thaletovu kružnici při konstrukci pravoúhlého trojúhelníku“. |
| S | Obraz celého útvaru ve středové souměrnosti | postup |  |  |  |  |  |  | Specifikace B1, 3: „sestrojí obraz rovinného útvaru ve středové souměrnosti“. |

### Vlastnosti útvarů

`KON.VLAST` · 6,4 points per standard test, in 16 of 16 · success 32 % · specification area 3 · Vlastnosti, které zadání neříká a které je třeba vybavit si z názvu útvaru; slouží konstrukcím i výpočtům.

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Rovnoramenný a rovnostranný trojúhelník: shodná ramena, úhly při základně, osa | znalost |  | 11 · 5 | 2,5 | 12 · 6 · 2,7 | 36 % | [2025 B 9](../backend/data/screenshots/M9-2025-B-09.png) 19 % · [2023 A 10](../backend/data/screenshots/M9-2023-A-10.png) 22 % · [2022 A 9](../backend/data/screenshots/M9-2022-A-09.png) 31 % | Rovnoramenný trojúhelník má shodná ramena a shodné úhly při základně; osa základny je jeho osou souměrnosti, výškou i těžnicí a prochází hlavním vrcholem. Rovnostranný má všechny strany shodné a úhly 60°; dva poloměry kružnice jsou ramena. Typická chyba: nepoznat rovnoramenný trojúhelník, když na něj zadání neupozorní, nebo splést základnu s ramenem. |
| 2 | Thaletova věta a kružnice | znalost | Kružnice (KON.ZAKL) | 6 · 5 | 0,9 |  | 32 % | [2026 B 10](../backend/data/screenshots/M9-2026-B-10.png) 22 % · [2026 A 8.2](../backend/data/screenshots/M9-2026-A-08.png) 31 % · [2023 B 10](../backend/data/screenshots/M9-2023-B-10.png) 43 % | Všechny body, ze kterých je úsečka AB vidět pod pravým úhlem, leží na kružnici s průměrem AB; obráceně je každý úhel nad průměrem pravý. Typická chyba: sestrojit kružnici se středem v krajním bodě úsečky místo v jejím středu, nebo větu při počítání úhlů nepoužít. |
| 1 | Výška: kolmice z vrcholu na protější stranu, i vně | znalost | Kolmice daným bodem (KON.ZAKL) | 4 · 2 | 0,6 | 13 · 6 · 2,1 | 26 % | [2025 A 10](../backend/data/screenshots/M9-2025-A-10.png) 28 % | Výška je kolmice z vrcholu na přímku protější strany; v tupoúhlém trojúhelníku leží její pata vně strany. Výška rovnoběžníku a lichoběžníku je vzdálenost rovnoběžných stran. Typická chyba: vést výšku do středu strany (záměna s těžnicí), nebo brát jako výšku šikmou stranu. |
| 3 | Těžnice | znalost | Střed a osa úsečky (KON.ZAKL) | 2 · 2 | 0,3 |  | 23 % | [2025 B 9](../backend/data/screenshots/M9-2025-B-09.png) 19 % · [2025 A 10](../backend/data/screenshots/M9-2025-A-10.png) 28 % | Těžnice spojuje vrchol se středem protější strany. Typická chyba: záměna s výškou nebo s osou strany. |
| 3 | Trojúhelníková nerovnost | znalost |  | 1 · 1 | 0,1 |  | 11 % | [2026 B 8.1](../backend/data/screenshots/M9-2026-B-08.png) 11 % · [2026 B 8.2](../backend/data/screenshots/M9-2026-B-08.png) 12 % | Součet dvou stran trojúhelníku je větší než třetí strana; třetí strana je proto větší než rozdíl a menší než součet zbylých dvou. Typická chyba: připustit rovnost, nebo ověřit jen jednu z nerovností. |
| 1 | Rovnoběžník: úhlopříčky se půlí | znalost | Středová souměrnost (KON.ZAKL) | 4 · 2 | 0,7 | 13 · 7 · 2,1 | 18 % | [2025 B 10](../backend/data/screenshots/M9-2025-B-10.png) 9 % · [2022 B 10](../backend/data/screenshots/M9-2022-B-10.png) 26 % | Protější strany rovnoběžníku jsou rovnoběžné a shodné, protější úhly shodné a sousední dávají 180°; úhlopříčky se navzájem půlí a jejich průsečík je středem souměrnosti. Typická chyba: předpokládat shodné nebo kolmé úhlopříčky. |
| 3 | Kosočtverec | znalost | Rovnoběžník (KON.VLAST) | 1 · 1 | 0,1 | 3 · 1 · 0,4 | 29 % | [2026 A 10](../backend/data/screenshots/M9-2026-A-10.png) 23 % · [2024 B 9](../backend/data/screenshots/M9-2024-B-09.png) 32 % | Kosočtverec je rovnoběžník se všemi stranami shodnými; úhlopříčky jsou kolmé, půlí se a jsou osami souměrnosti. Typická chyba: nepoznat kosočtverec, když je popsán jen vlastností (čtyři shodné strany, rovnoběžník souměrný podle úhlopříčky). |
| 2 | Obdélník: shodné úhlopříčky, vrcholy na kružnici | znalost | Rovnoběžník (KON.VLAST) | 6 · 4 | 0,9 | 8 · 4 · 1,2 | 30 % | [2024 A 10](../backend/data/screenshots/M9-2024-A-10.png) 26 % · [2023 A 9](../backend/data/screenshots/M9-2023-A-09.png) 32 % · [2025 A 9](../backend/data/screenshots/M9-2025-A-09.png) 33 % | Obdélník má pravé úhly a shodné úhlopříčky, které se půlí; všechny vrcholy proto leží na kružnici se středem v průsečíku úhlopříček. Typická chyba: považovat úhlopříčky obdélníku za kolmé nebo za osy jeho úhlů. |
| 3 | Čtverec | znalost | Obdélník (KON.VLAST), Kosočtverec (KON.VLAST) | 2 · 0 | 0,3 |  | 51 % | [2022 A 10](../backend/data/screenshots/M9-2022-A-10.png) 51 % | Čtverec má shodné strany a pravé úhly; úhlopříčky jsou shodné, kolmé a půlí se, střed má od všech stran stejnou vzdálenost rovnou polovině strany. Typická chyba: zaměnit vzdálenost středu od strany se vzdáleností od vrcholu. |
| 3 | Rovnoramenný a pravoúhlý lichoběžník | znalost | Rovnoběžka daným bodem (KON.ZAKL) | 3 · 1 | 0,5 |  | 64 % | [2023 B 9](../backend/data/screenshots/M9-2023-B-09.png) 64 % | Lichoběžník má jednu dvojici rovnoběžných stran, základny. Rovnoramenný je souměrný podle osy základen: má shodná ramena, shodné úhly při základně a shodné úhlopříčky. Pravoúhlý má rameno kolmé k základnám. Typická chyba: neurčit ze zadání, které strany jsou základny. |
| 3 | Pravidelný mnohoúhelník (pěti-, šesti-, osmiúhelník) | znalost | Rovnoramenný a rovnostranný trojúhelník (KON.VLAST) | 2 · 2 | 0,2 |  | 15 % | [2026 B 9](../backend/data/screenshots/M9-2026-B-09.png) 15 % | Pravidelný mnohoúhelník má shodné strany i úhly a vrcholy na kružnici; trojúhelníky se společným vrcholem ve středu jsou rovnoramenné, u šestiúhelníku rovnostranné (strana = poloměr). Vnitřní úhel pětiúhelníku je 108°, šestiúhelníku 120°, osmiúhelníku 135°. Typická chyba: zaměnit středový úhel s vnitřním. |
| 3 | Osy souměrnosti útvaru | znalost | Osová souměrnost (KON.ZAKL) | 2 · 0 | 0,5 |  | – |  | Osa souměrnosti dělí útvar na dvě části, které se po překlopení kryjí; útvar jich může mít několik, i šikmých. Typická chyba: přehlédnout šikmou osu, nebo považovat za osu přímku, která útvar jen půlí (úhlopříčka obdélníku). |
| S | Shodnost trojúhelníků | znalost |  |  |  |  |  |  | Specifikace B1, 3: „rozumí pojmu shodnost trojúhelníků, používá věty o shodnosti trojúhelníků k řešení geometrických úloh“. |
| S | Podobnost trojúhelníků: věty sss, sus, uu, poměr podobnosti | znalost |  |  |  |  |  |  | Specifikace C1, 3: „rozlišuje shodné a podobné trojúhelníky, pomocí poměru podobnosti určí rozměry trojúhelníků, využívá věty o podobnosti trojúhelníků (věta sss, uu, sus)“. |

### Rozbor konstrukční úlohy

`KON.ROZBOR` · 4,8 points per standard test, in 16 of 16 · success 28 % · specification area 3 · Převod zadání na postup konstrukce.

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Podmínka jako množina bodů, bod jako průsečík dvou čar | rozbor | Kružnice (KON.ZAKL), Střed a osa úsečky (KON.ZAKL) | 16 · 8 | 4,4 | 16 · 8 · 4,8 | 28 % | [2025 B 10](../backend/data/screenshots/M9-2025-B-10.png) 9 % · [2026 B 9](../backend/data/screenshots/M9-2026-B-09.png) 15 % · [2025 B 9](../backend/data/screenshots/M9-2025-B-09.png) 19 % | Každá podmínka ze zadání určuje čáru, na které hledaný bod leží (kružnici, osu úsečky, kolmici, rovnoběžku, Thaletovu kružnici); bod je průsečíkem dvou takových čar. Typická chyba: použít jen jednu podmínku, nebo nepřevést nepřímou podmínku („přímka je osou strany“) na čáru. |
| 1 | Všechna řešení | rozbor | Podmínka jako množina bodů (KON.ROZBOR) | 13 · 6 | 2,8 |  | 32 % | [2025 B 9](../backend/data/screenshots/M9-2025-B-09.png) 19 % · [2023 A 10](../backend/data/screenshots/M9-2023-A-10.png) 22 % · [2022 A 9](../backend/data/screenshots/M9-2022-A-09.png) 31 % | Protínají-li se čáry ve dvou bodech nebo připouští-li zadání dvě polohy útvaru, má úloha dvě řešení a sestrojují se obě. Typická chyba: skončit u prvního řešení. |
| S | Trojúhelník a čtyřúhelník ze zadaných údajů (sss, sus, usu) | postup |  |  |  |  |  |  | Specifikace B1, 3: „sestrojí trojúhelník ze zadaných údajů (sss, sus, usu), sestrojí čtyřúhelník ze zadaných údajů“. |

## Geometrie: výpočty (GEO)

10,0 points per standard test · success 38 % · Výpočty úhlů, délek, obsahů, objemů a povrchů.

### Úhly

`GEO.UHLY` · 2,2 points per standard test, in 14 of 16 · success 49 % · specification area 3

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Vedlejší a vrcholové úhly | znalost |  | 13 · 6 | 1,5 | 14 · 6 · 1,7 | 52 % | [2024 B 13](../backend/data/screenshots/M9-2024-B-13.png) 66 % · [2024 A 11](../backend/data/screenshots/M9-2024-A-11.png) 67 % | Vedlejší úhly dávají dohromady 180°, vrcholové jsou shodné; úhly po jedné straně přímky se společným vrcholem dávají 180°. Typická chyba: považovat vedlejší úhly za shodné. |
| 2 | Souhlasné a střídavé úhly | znalost | Vedlejší a vrcholové úhly (GEO.UHLY) | 8 · 2 | 1,1 |  | 50 % | [2022 B 13](../backend/data/screenshots/M9-2022-B-13.png) 54 % · [2025 A 7.1](../backend/data/screenshots/M9-2025-A-07.png) 65 % · [2025 A 7.2](../backend/data/screenshots/M9-2025-A-07.png) 66 % | Příčka svírá s rovnoběžkami shodné souhlasné a shodné střídavé úhly; úhel se tak přenese od jedné rovnoběžky ke druhé. Typická chyba: přenést místo shodného úhlu jeho doplněk do 180°, nebo použít pravidlo u přímek, které rovnoběžné nejsou. |
| 1 | Součet úhlů v trojúhelníku | znalost |  | 14 · 6 | 1,9 |  | 50 % | [2025 A 7.3](../backend/data/screenshots/M9-2025-A-07.png) 40 % | Součet vnitřních úhlů trojúhelníku je 180°; v pravoúhlém trojúhelníku dávají oba ostré úhly 90°. Typická chyba: sečíst úhly, které neleží v jednom trojúhelníku. |
| 2 | Osa úhlu | znalost |  | 3 · 3 | 0,5 |  | 36 % | [2026 A 8.1](../backend/data/screenshots/M9-2026-A-08.png) 42 % | Osa úhlu dělí úhel na dva shodné úhly a tvoří ji body stejně vzdálené od obou ramen; celý úhel je dvojnásobkem poloviny. Typická chyba: zapomenout úhel zdvojnásobit, nebo zaměnit osu úhlu s osou strany. |

### Pythagorova věta

`GEO.PYT` · 1,6 points per standard test, in 11 of 16 · success 37 % · specification area 3

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Pythagorova věta | postup | Druhá odmocnina (POC.VYR) | 11 · 4 | 1,6 | 11 · 4 · 1,6 | 37 % | [2024 B 6.1](../backend/data/screenshots/M9-2024-B-06.png) 40 % · [2023 B 11.2](../backend/data/screenshots/M9-2023-B-11.png) 69 % | V pravoúhlém trojúhelníku je c² = a² + b², kde c je přepona; odvěsna se počítá odečtením, a² = c² − b². Typická chyba: sečíst druhé mocniny i tehdy, když se hledá odvěsna, nebo zapomenout odmocnit. |
| 2 | Nalezení pravoúhlého trojúhelníku v útvaru nebo tělese | rozbor | Pythagorova věta (GEO.PYT) | 7 · 4 | 0,9 |  | 40 % | [2024 A 6.2](../backend/data/screenshots/M9-2024-A-06.png) 27 % · [2023 A 12](../backend/data/screenshots/M9-2023-A-12.png) 39 % | Pravoúhlý trojúhelník je často třeba nejdřív najít nebo vytvořit: výškou v rovnoramenném trojúhelníku a lichoběžníku, úhlopříčkou obdélníku, stěnovou úhlopříčkou tělesa. Typická chyba: dosadit délky, které netvoří strany jednoho pravoúhlého trojúhelníku (celou základnu místo její poloviny nebo místo rozdílu základen). |

### Obvod a obsah

`GEO.ROV` · 4,4 points per standard test, in 15 of 16 · success 31 % · specification area 3

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Obvod mnohoúhelníku | postup |  | 10 · 6 | 1,6 | 15 · 8 · 3,2 | 32 % | [2024 A 13](../backend/data/screenshots/M9-2024-A-13.png) 31 % · [2024 B 6.2](../backend/data/screenshots/M9-2024-B-06.png) 42 % · [2025 B 8.2](../backend/data/screenshots/M9-2025-B-08.png) 42 % | Obvod je součet délek všech stran po hranici útvaru; u obdélníku 2 · (a + b), u čtverce 4a. Typická chyba: vynechat stranu, nebo započítat úsečku, která leží uvnitř útvaru. |
| 1 | Obsah čtverce a obdélníku | znalost |  | 4 · 3 | 0,3 | 16 · 8 · 5,8 | 37 % | [2023 A 8.3](../backend/data/screenshots/M9-2023-A-08.png) 17 % | Obsah obdélníku je a · b, čtverce a². Typická chyba: záměna s obvodem. |
| 1 | Obsah trojúhelníku | znalost | Obsah čtverce a obdélníku (GEO.ROV), Výška (KON.VLAST) | 9 · 3 | 1,2 | 11 · 5 · 1,6 | 33 % | [2023 A 6.1](../backend/data/screenshots/M9-2023-A-06.png) 22 % · [2026 A 13](../backend/data/screenshots/M9-2026-A-13.png) 34 % | Obsah trojúhelníku je strana krát výška k této straně děleno dvěma; v pravoúhlém trojúhelníku jsou stranou a výškou obě odvěsny. Typická chyba: nevydělit dvěma, nebo násobit stranu výškou k jiné straně. |
| 3 | Obsah rovnoběžníku a kosočtverce | znalost | Obsah čtverce a obdélníku (GEO.ROV), Výška (KON.VLAST) | 1 · 0 | 0,1 |  | 39 % | [2023 B 11.3](../backend/data/screenshots/M9-2023-B-11.png) 39 % | Obsah rovnoběžníku i kosočtverce je strana krát výška k této straně. Typická chyba: násobit dvě sousední strany. |
| 2 | Obsah lichoběžníku | znalost | Obsah trojúhelníku (GEO.ROV) | 4 · 2 | 0,3 |  | 30 % | [2024 A 6.1](../backend/data/screenshots/M9-2024-A-06.png) 27 % · [2023 A 6.2](../backend/data/screenshots/M9-2023-A-06.png) 29 % · [2025 B 8.1](../backend/data/screenshots/M9-2025-B-08.png) 38 % | Obsah lichoběžníku je (a + c) · v : 2, kde a, c jsou základny a v jejich vzdálenost. Typická chyba: nevydělit dvěma, nebo dosadit rameno místo výšky. |
| 2 | Rozměr z obsahu nebo obvodu (vzorec obráceně, i u kruhu) | postup | Obsah čtverce a obdélníku (GEO.ROV), Obvod mnohoúhelníku (GEO.ROV) | 8 · 3 | 1,3 |  | 39 % | [2023 B 8.1](../backend/data/screenshots/M9-2023-B-08.png) 36 % · [2025 A 5.1](../backend/data/screenshots/M9-2025-A-05.png) 47 % · [2022 B 11.3](../backend/data/screenshots/M9-2022-B-11.png) 57 % | Vzorec se použije obráceně: strana čtverce je odmocnina z obsahu, strana obdélníku obsah dělený druhou stranou, výška trojúhelníku 2S : a, poloměr kruhu z r² = S : π. Typická chyba: u trojúhelníku zapomenout na dvojku, u čtverce dělit čtyřmi nebo dvěma místo odmocnění. |
| 2 | Skládání a rozklad útvarů | rozbor | Obsah čtverce a obdélníku (GEO.ROV), Obvod mnohoúhelníku (GEO.ROV) | 7 · 4 | 1,0 |  | 31 % | [2026 B 16.3](../backend/data/screenshots/M9-2026-B-16.png) 2 % · [2024 A 8.1](../backend/data/screenshots/M9-2024-A-08.png) 24 % · [2022 B 8](../backend/data/screenshots/M9-2022-B-08.png) 37 % | Útvar se rozloží na známé části nebo doplní na větší útvar; obsahy částí se sčítají a odčítají a přemístěním dílů se obsah nemění. Typická chyba: započítat překrývající se část dvakrát, nebo sčítat obvody částí – společné úsečky do obvodu nepatří. |
| 3 | Rozestupy po obvodu | rozbor | Obvod mnohoúhelníku (GEO.ROV) | 1 · 1 | 0,2 |  | 17 % | [2025 A 8.2](../backend/data/screenshots/M9-2025-A-08.png) 14 % · [2025 A 8.1](../backend/data/screenshots/M9-2025-A-08.png) 24 % | Po uzavřeném obvodu je stejně rozestupů jako předmětů; na úsečce s předměty na obou koncích je rozestupů o jeden méně. Typická chyba: nerozlišit počet rozestupů a počet předmětů. |
| S | Obvod a obsah mnohoúhelníku ve čtvercové síti | postup |  |  |  |  |  |  | Specifikace B1, 3: „využívá čtvercovou síť pro výpočet obvodu a obsahu mnohoúhelníků“. |

### Kruh

`GEO.KRUH` · 0,8 points per standard test, in 6 of 16 · success 36 % · specification area 3

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 2 | Obvod kruhu | postup | Počítání s desetinnými čísly (POC.VYR) | 3 · 1 | 0,4 | 5 · 1 · 0,7 | 34 % | [2026 B 7.2](../backend/data/screenshots/M9-2026-B-07.png) 19 % · [2024 A 8.2](../backend/data/screenshots/M9-2024-A-08.png) 21 % · [2022 A 13](../backend/data/screenshots/M9-2022-A-13.png) 40 % | o = 2πr = πd, s π ≐ 3,14. Typická chyba: dosadit průměr místo poloměru, nebo záměna se vzorcem pro obsah. |
| 2 | Obsah kruhu | postup | Počítání s desetinnými čísly (POC.VYR), Druhá mocnina čísla (POC.VYR) | 3 · 1 | 0,3 | 9 · 4 · 1,1 | 37 % | [2024 A 8.1](../backend/data/screenshots/M9-2024-A-08.png) 24 % · [2023 A 13](../backend/data/screenshots/M9-2023-A-13.png) 30 % · [2024 B 14](../backend/data/screenshots/M9-2024-B-14.png) 56 % | S = πr², s π ≐ 3,14. Typická chyba: umocnit průměr místo poloměru, nebo počítat 2πr. |
| 3 | Půlkruh, čtvrtkruh, výseč | postup | Obvod kruhu (GEO.KRUH), Obsah kruhu (GEO.KRUH) | 2 · 1 | 0,3 |  | 34 % | [2026 B 7.2](../backend/data/screenshots/M9-2026-B-07.png) 19 % · [2024 A 8.2](../backend/data/screenshots/M9-2024-A-08.png) 21 % · [2022 A 13](../backend/data/screenshots/M9-2022-A-13.png) 40 % | Půlkruh, čtvrtkruh a výseč jsou zlomkem kruhu podle středového úhlu (90° je čtvrtina): tímto zlomkem se násobí obsah i délka oblouku; obvod části tvoří oblouk a rovné úseky. Typická chyba: zapomenout k oblouku přičíst poloměry nebo průměr. |
| S | Vzájemná poloha kružnice a přímky: tečna, sečna, vnější přímka | znalost |  |  |  |  |  |  | Specifikace C1, 3: „určí vzájemnou polohu kružnice a přímky (tečna, sečna, vnější přímka), vzájemnou polohu dvou kružnic, průsečíky a body dotyku“. |
| S | Vzájemná poloha dvou kružnic, průsečíky a body dotyku | znalost |  |  |  |  |  |  | Specifikace C1, 3: „určí vzájemnou polohu kružnice a přímky (tečna, sečna, vnější přímka), vzájemnou polohu dvou kružnic, průsečíky a body dotyku“. |

### Tělesa

`GEO.TEL` · 3,9 points per standard test, in 16 of 16 · success 38 % · specification area 3

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 2 | Hrany a stěny hranolu | znalost |  | 3 · 3 | 0,3 | 4 · 3 · 0,5 | 70 % | [2025 A 11.1](../backend/data/screenshots/M9-2025-A-11.png) 70 % | Kvádr má 12 hran (čtyři od každého rozměru), 8 vrcholů a 6 stěn; n-boký hranol má 3n hran. Součet délek hran kvádru je 4 · (a + b + c), krychle 12a. Typická chyba: počítat jen viditelné hrany. |
| 1 | Objem krychle a kvádru | znalost | Obsah čtverce a obdélníku (GEO.ROV) | 6 · 4 | 0,9 | 14 · 7 · 3,0 | 37 % | [2025 A 12](../backend/data/screenshots/M9-2025-A-12.png) 24 % · [2022 A 6](../backend/data/screenshots/M9-2022-A-06.png) 30 % · [2026 A 15.1](../backend/data/screenshots/M9-2026-A-15.png) 42 % | V = a · b · c, u krychle a³. Typická chyba: záměna s povrchem, nebo počítat a³ jako 3a. |
| 1 | Povrch krychle a kvádru | znalost | Obsah čtverce a obdélníku (GEO.ROV) | 7 · 6 | 0,8 | 14 · 7 · 2,4 | 39 % | [2022 B 11.2](../backend/data/screenshots/M9-2022-B-11.png) 47 % | S = 2 · (ab + bc + ac), u krychle 6a²: součet obsahů všech šesti stěn. Typická chyba: započítat jen tři stěny, nebo u krychle počítat 4a². |
| 2 | Objem hranolu | postup | Objem krychle a kvádru (GEO.TEL) | 6 · 2 | 0,8 | 8 · 3 · 1,3 | 33 % | [2022 A 6](../backend/data/screenshots/M9-2022-A-06.png) 30 % · [2023 B 13](../backend/data/screenshots/M9-2023-B-13.png) 45 % | V = obsah podstavy · výška hranolu; podstavou je mnohoúhelník, který se v tělese opakuje, ne nutně stěna, na které těleso leží. Typická chyba: vzít za podstavu boční stěnu, nebo u trojúhelníkové podstavy nevydělit dvěma. |
| 2 | Povrch hranolu | postup | Povrch krychle a kvádru (GEO.TEL) | 4 · 1 | 0,5 | 7 · 1 · 0,9 | 33 % | [2026 A 14](../backend/data/screenshots/M9-2026-A-14.png) 33 % | S = 2 · obsah podstavy + plášť; plášť je obdélník o stranách obvod podstavy a výška hranolu. Typická chyba: započítat jen jednu podstavu, nebo vynechat některou boční stěnu. |
| 2 | Objem válce | postup | Objem hranolu (GEO.TEL), Obsah kruhu (GEO.KRUH) | 4 · 2 | 0,5 |  | 22 % | [2024 A 2](../backend/data/screenshots/M9-2024-A-02.png) 16 % · [2023 B 8.2](../backend/data/screenshots/M9-2023-B-08.png) 18 % · [2025 A 6.1](../backend/data/screenshots/M9-2025-A-06.png) 20 % | V = πr² · v. Typická chyba: dosadit průměr místo poloměru. |
| 3 | Plášť a povrch válce | postup | Povrch hranolu (GEO.TEL), Obvod kruhu (GEO.KRUH) | 3 · 0 | 0,4 |  | 43 % | [2023 A 13](../backend/data/screenshots/M9-2023-A-13.png) 30 % · [2022 B 12](../backend/data/screenshots/M9-2022-B-12.png) 56 % | Plášť válce je po rozvinutí obdélník o stranách obvod podstavy 2πr a výška v; povrch je plášť a dvě podstavy, 2πrv + 2πr². Typická chyba: zapomenout podstavy, nebo počítat plášť s obsahem podstavy místo obvodu. |
| 2 | Hrana nebo výška z objemu či povrchu | postup | Objem krychle a kvádru (GEO.TEL), Povrch krychle a kvádru (GEO.TEL) | 5 · 4 | 0,5 |  | 27 % | [2025 A 6.2](../backend/data/screenshots/M9-2025-A-06.png) 17 % | Vzorec pro objem nebo povrch se použije obráceně: výška je objem dělený obsahem podstavy, hrana krychle odmocnina z obsahu stěny (povrch : 6). Typická chyba: u krychle odmocnit celý povrch, nebo dělit nesprávnou veličinou. |
| 3 | Síť tělesa | znalost | Hrany a stěny hranolu (GEO.TEL) | 2 · 1 | 0,3 |  | 46 % | [2022 B 11.1](../backend/data/screenshots/M9-2022-B-11.png) 44 % · [2022 B 11.2](../backend/data/screenshots/M9-2022-B-11.png) 47 % | Síť je povrch tělesa rozložený do roviny: každá stěna je v ní jednou a strany, které se při složení spojí v hranu, jsou stejně dlouhé; obsah sítě je povrch tělesa. Typická chyba: nepoznat, které strany v síti patří k sobě. |
| 2 | Slepená a rozříznutá tělesa, řez | rozbor | Povrch krychle a kvádru (GEO.TEL), Objem krychle a kvádru (GEO.TEL) | 8 · 3 | 1,3 |  | 33 % | [2026 B 13](../backend/data/screenshots/M9-2026-B-13.png) 22 % · [2025 A 12](../backend/data/screenshots/M9-2025-A-12.png) 24 % · [2022 B 11.1](../backend/data/screenshots/M9-2022-B-11.png) 44 % | Objem slepeného tělesa je součet objemů částí. Povrch součtem není: slepením zmizí styčná plocha z obou těles, rozříznutím přibudou dvě plochy řezu. Typická chyba: sečíst povrchy částí, nebo odečíst styčnou plochu jen jednou. |
| 3 | Tělesa z krychliček | rozbor |  | 2 · 2 | 0,5 |  | 48 % | [2025 B 13](../backend/data/screenshots/M9-2025-B-13.png) 25 % | Těleso z krychliček se počítá po vrstvách nebo doplněním na kvádr; krychlička v rohu, na hraně a uprostřed stěny patří ke třem, dvěma a jedné stěně tělesa. Typická chyba: zapomenout na zakryté krychličky, nebo započítat rohovou krychličku vícekrát. |
| S | Pohled na těleso shora, zepředu, zprava, zleva a zdola | rozbor |  |  |  |  |  |  | Specifikace B1, 3: „zobrazí tělesa při pohledu shora, zepředu, zprava, zleva a zdola“. |
| S | Náčrt sítě a obrazu tělesa ve volném rovnoběžném promítání | postup |  |  |  |  |  |  | Specifikace B1, 3: „načrtne a sestrojí síť krychle, kvádru a kolmého hranolu“; C1, 3: „načrtne síť válce“. |
| S | Jehlan: rozpoznání, síť, pohledy, metrické a polohové vlastnosti | znalost |  |  |  |  |  |  | Specifikace C1, 3: „rozpozná jehlan ve volném rovnoběžném promítání, zobrazí jehlan při pohledu shora, zepředu, zdola, zprava atd., rozpozná síť jehlanu, využívá při řešení úloh metrické a polohové vlastnosti jehlanu“. |
| S | Koule: poloměr a průměr ve slovních úlohách | znalost |  |  |  |  |  |  | Specifikace C1, 3: „řeší aplikační slovní úlohy s využitím znalostí o válci a kouli (poloměr a průměr koule)“. |

## Zákonitosti a úsudek (ZAK)

3,9 points per standard test · success 11 % · Hledání pravidla v řadě obrazců nebo čísel a úlohy řešené úsudkem.

### Rostoucí obrazce a číselné řady

`ZAK.RADA` · 3,1 points per standard test, in 13 of 16 · success 10 % · specification area 4

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Pokračování pravidla po krocích | rozbor |  | 7 · 4 | 0,8 | 13 · 6 · 3,1 | 8 % | [2023 A 16.2](../backend/data/screenshots/M9-2023-A-16.png) 2 % · [2023 B 16.1](../backend/data/screenshots/M9-2023-B-16.png) 11 % | Z prvních obrazců nebo členů se zjistí, o kolik se počet mění, a pravidlo se krok za krokem prodlouží, nejlépe v tabulce. Typická chyba: odhadnout pravidlo jen ze dvou obrazců, nebo se splést v počtu kroků. |
| 2 | Obecné pravidlo, n-tý člen | rozbor | Pokračování pravidla po krocích (ZAK.RADA), Vyjádření veličiny výrazem s proměnnou (VZT.SLOV) | 9 · 4 | 1,9 | 9 · 4 · 1,9 | 11 % | [2025 A 16.3](../backend/data/screenshots/M9-2025-A-16.png) 1 % · [2022 B 16.3](../backend/data/screenshots/M9-2022-B-16.png) 3 % · [2025 A 16.2](../backend/data/screenshots/M9-2025-A-16.png) 6 % | Počet v n-tém kroku se zapíše výrazem s n (lineární růst, n², n · (n + 1) : 2), takže vzdálený člen lze vypočítat bez vypisování. Typická chyba: ověřit výraz jen na jednom obrazci, nebo posunout n o jedna. |
| 2 | Obrácení pravidla | rozbor | Obecné pravidlo (ZAK.RADA) | 7 · 2 | 1,1 |  | 10 % | [2023 B 16.3](../backend/data/screenshots/M9-2023-B-16.png) 2 % · [2026 B 16.2](../backend/data/screenshots/M9-2026-B-16.png) 7 % · [2022 B 16.2](../backend/data/screenshots/M9-2022-B-16.png) 12 % | Ze známého počtu se určí pořadí kroku: výraz pro n-tý člen se položí rovný danému číslu a vyřeší (361 = 19²). Typická chyba: odpovědět hodnotou n, když se zadání ptá na jinou veličinu téhož obrazce, nebo posun o jeden krok. |
| 3 | Růst násobením | rozbor | Pokračování pravidla po krocích (ZAK.RADA) | 2 · 1 | 0,4 |  | 4 % | [2023 A 16.3](../backend/data/screenshots/M9-2023-A-16.png) 2 % · [2023 A 16.1](../backend/data/screenshots/M9-2023-A-16.png) 15 % | Počet se v každém kroku násobí stejným číslem (1, 3, 9, 27, …), přírůstky proto nejsou stejné. Typická chyba: pokračovat přičítáním stejného rozdílu. |
| 3 | Číselná řada daná pravidlem | rozbor | Pokračování pravidla po krocích (ZAK.RADA) | 2 · 1 | 0,5 |  | 12 % | [2025 B 16.2](../backend/data/screenshots/M9-2025-B-16.png) 1 % · [2025 B 16.3](../backend/data/screenshots/M9-2025-B-16.png) 2 % · [2025 B 16.1](../backend/data/screenshots/M9-2025-B-16.png) 42 % | Řada čísel daná slovním pravidlem se rozdělí na opakující se skupiny (dvojice, trojice) a určí se, co stojí na daném místě skupiny. Typická chyba: splést pořadí čísla ve skupině s pořadím skupiny. |

### Úsudek a systematické hledání

`ZAK.USUDEK` · 1,1 points per standard test, in 7 of 16 · success 13 % · specification area 4

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 2 | Periodické děje | rozbor | Dělení se zbytkem (POC.DEL) | 4 · 2 | 0,6 |  | 15 % | [2026 A 16.3](../backend/data/screenshots/M9-2026-A-16.png) 1 % · [2026 A 16.2](../backend/data/screenshots/M9-2026-A-16.png) 10 % · [2022 A 16.3](../backend/data/screenshots/M9-2022-A-16.png) 11 % | Děj, který se po pevném počtu kroků opakuje, se počítá po celých periodách; zbytek po dělení délkou periody říká, kde v periodě děj skončí, a dva děje se sejdou ve společném násobku svých period. Typická chyba: zapomenout na neúplnou periodu na konci. |
| 2 | Systematické vypsání možností | rozbor |  | 4 · 3 | 0,6 |  | 2 % | [2025 A 8.3](../backend/data/screenshots/M9-2025-A-08.png) 2 % · [2023 B 16.3](../backend/data/screenshots/M9-2023-B-16.png) 2 % | Možnosti se vypisují v pevném pořadí (od nejmenší hodnoty jedné veličiny), aby žádná nechyběla a žádná nebyla dvakrát. Typická chyba: skončit u prvního nalezeného řešení. |
