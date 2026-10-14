# Strom učiva M9: what the test examines, as a tree in learning order

Generated from `analysis/data/m9_topic_tree.json` and `analysis/data/m9_item_skills.json`; change them
with `analysis/topic_tree.py`, not here. The tree has 7 areas, 24 topics and 162 skills.
Every one of the 610 scored items (sub-items such as 15.2, or whole tasks) of the 20 tests of
2022–2026 is assigned to the skills it needs.

What rests on what:

- **The assignment is my reading of each task.** 18 tests were read from the wording extracted from the
  booklets (figures not seen, so geometry and construction items are placed by their text and the
  catalog description), 2024 A and B from the task screenshots. Which skills an item needs, which one
  is its main skill, the grouping and the prerequisite links are judgement, not CERMAT's.
- **Numbers are computed, not estimated**: points from the catalog, success rates from CERMAT's
  published item results.
- **Skills marked S** are quoted from CERMAT's specification (`References/MASPECIFIKACEPOZADAVKU2022 (1).pdf`,
  parts A1, B1, C1; C1 says a candidate must also know A1 and B1) and are needed by no item of the 20
  tests. The specification's four areas are 1 Číslo a proměnná, 2 Závislosti, vztahy a práce s daty,
  3 Geometrie v rovině a prostoru, 4 Nestandardní aplikační úlohy a problémy.

## How the tree is cut

- **A leaf is one thing a student can practise in one sitting** and recognise in a task: „složený zlomek“,
  „základ po změně“, „Thaletova kružnice“. Areas and topics only group leaves.
- **Order is learning order.** Everything a leaf needs comes earlier; the *needs* column names the direct
  prerequisites (the editor refuses an order that breaks this).
- **Computing and reading are separated.** Computing with fractions is in POC, fraction word problems in
  VZT. The phrases „o třetinu více než“, „kolikrát“, „o kolik procent“ recur in fractions, percentages
  and equation word problems, so they are one topic (VZT.NEZ) learned once instead of three times.
- **Constructions are three layers**: the moves, the properties of figures, and the reading of the task.
- **Tools used everywhere stay single leaves** (druhá mocnina, převody jednotek, Pythagorova věta,
  zaokrouhlení) and are pulled in through *needs* rather than repeated under each topic.
- Not in the tree: the rules for how answers must look and the list of what is not printed in the
  booklet ([03_ucivo_M9.md](03_ucivo_M9.md), section 0). They apply to every leaf.

## How to read the columns

- **P, priority**, from how often a skill is needed, directly or through a skill that builds on it. A
  foundation therefore never ranks below what stands on it: „pořadí operací“ is needed by few items by name,
  but nearly every computation rests on it. "Standard tests" are the 16 tests of 2022, 2023, 2025, 2026; the four
  2024 tests follow a different design and do not count here.
  **1** = needed in at least 10 of the 16 standard tests, or in at least 6 of the 8 tests of 2025–2026 (41 skills) ·
  **2** = in at least 4 of 16, or 3 of the last 8 (32) · **3** = rarer, or only in 2024 (57) ·
  **S** = in the specification, needed by no item of 2022–2026 (32); where one occurred in an older
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
it was not built from (2019 A, 2021 A, 2021 B; booklets in `References/Matematika_starsi/`, read from their
extracted wording, figures not seen) were assigned the same way: 96 items. They are in
`data/m9_item_skills_older.json` and count in none of the numbers below, because the next tests will resemble the
recent ones more than the old ones.

Every item found a place in the tree and none needed a new skill. 3 items needed a skill that no 2022–2026 item needs (marked S below): 2019 A 7.2 – Sekunda a týden v převodech času; 2021 B 8.1 – Podobnost trojúhelníků: věty sss, sus, uu, poměr podobnosti; 2021 B 8.3 – Podobnost trojúhelníků: věty sss, sus, uu, poměr podobnosti. So S skills are real exam material, only rarer; they keep the lowest priority but should not be dropped.

## The tree at a glance

Points per standard test in brackets (each item counted once per topic).

```
POC  Počítání s čísly  (8,2 b.)
├─ Číselné výrazy, mocniny, odmocniny  (1,9 b.)
│    1  Pořadí operací, závorky, záporná čísla
│    1  Počítání s desetinnými čísly bez kalkulačky
│    1  Druhá mocnina a odmocnina
│    3  Výraz zadaný slovy (součet, rozdíl, součin, podíl)
│    3  Číselná osa se stejnými dílky
│    2  Zaokrouhlení výsledku na daný řád
│    S  Absolutní hodnota a opačné číslo
│    S  Periodické číslo: zápis, porovnání, převod zlomku
│    S  Odhad výsledku s danou přesností
├─ Počítání se zlomky  (4,0 b.)
│    1  Čtyři operace se zlomky, společný jmenovatel, krácení, základní tvar
│    1  Složený zlomek
│    3  Zlomky spolu s desetinnými čísly
│    2  Zlomky s druhou mocninou a odmocninou
│    3  Smíšené číslo
│    S  Porovnávání zlomků
│    S  Převrácený zlomek podle názvu
├─ Dělitelnost  (0,9 b.)
│    2  Dělitelé a násobky čísla
│    2  Prvočísla a rozklad na prvočísla
│    3  Dělení se zbytkem ve slovní úloze
│    3  Společný násobek
│    S  Znaky dělitelnosti čísly 2, 3, 4, 5, 6, 8 a 10
│    S  Nejmenší společný násobek a největší společný dělitel dvou až tří čísel
└─ Převody jednotek  (1,6 b.)
     2  Délka (mm, cm, dm, m, km)
     3  Obsah (krok × 100)
     3  Objem a litry (krok × 1 000, 1 l = 1 dm³)
     3  Hmotnost (g, kg)
     2  Čas (hodiny, minuty, desetinné hodiny, sčítání časů)
     3  Stupně a minuty (1° = 60′)
     S  Sekunda a týden v převodech času

ALG  Výrazy a rovnice  (8,0 b.)
├─ Úpravy výrazů  (4,0 b.)
│    1  Roznásobení závorek a sloučení členů
│    2  Vytýkání
│    1  Umocnění dvojčlenu (a ± b)²
│    3  Vzorec (a ± b)² zpětně: rozklad trojčlenu, doplnění chybějících čísel
│    2  Rozklad a² − b² na součin
│    3  Hodnota výrazu pro dané číslo
└─ Lineární rovnice a soustavy  (4,0 b.)
     1  Rovnice se závorkami a desetinnými čísly
     1  Rovnice se zlomky
     3  Rovnice bez řešení
     3  Rovnice s druhými mocninami dvojčlenů, ve které x² vypadne
     1  Soustava dvou rovnic se dvěma neznámými
     S  Rovnice s nekonečně mnoha řešeními

VZT  Vztahy mezi veličinami: zlomek, procento, poměr  (16,9 b.)
├─ Zlomek jako část celku  (2,3 b.)
│    1  Zlomek z množství a z času
│    3  Část ze zbytku
│    3  Zlomek ze zlomku
│    2  Celek z části
├─ Srovnání „o … více než“, „kolikrát“  (3,6 b.)
│    1  „o kolik“ je rozdíl, „kolikrát“ je podíl
│    1  „o třetinu více / méně než“ jako násobení
│    2  „dvakrát méně“, „čtyřikrát menší než“ jako dělení
│    1  Obrácení vztahu: neznámá není veličina za „než“
├─ Procenta  (7,1 b.)
│    1  Procentová část, počet procent, základ
│    1  „o x % více / méně“ jako násobitel
│    2  Základ po změně („což je o 40 % více než loni“)
│    2  „O kolik procent“ se liší dvě veličiny
│    3  Obrácené srovnání („o třetinu méně“ je opačně „o 50 % více“)
│    3  Dvě změny po sobě
│    3  Procento ze zbytku
│    2  Dvě veličiny svázané procentem a známý součet
│    2  Procento, zlomek a poměr: převody mezi nimi
│    3  Změna v procentních bodech
│    3  Úrok za jeden rok a daň z úroku
│    S  Promile
│    S  Jistina, úroková míra, úrokovací období, inflace; půjčky a úvěry
├─ Poměr a úměrnost  (3,0 b.)
│    1  Poměr v základním tvaru, dělení v poměru
│    3  Poměr na číselné ose a na úsečce
│    3  Měřítko mapy a plánu
│    1  Přímá úměrnost
│    2  Nepřímá úměrnost
│    3  Společná práce
│    2  Pohyb: s = v · t
│    3  Směsi a průměrná cena
│    S  Postupný a převrácený poměr, změna čísla v daném poměru
│    S  Bod v pravoúhlé soustavě souřadnic
│    S  Přímá a nepřímá úměrnost tabulkou, rovnicí a grafem
└─ Slovní úlohy na rovnici  (4,7 b.)
     1  Vyjádření veličiny výrazem s proměnnou
     1  Sestavení a vyřešení rovnice z další podmínky
     2  Dvě neznámé: počty a součty
     2  Řešení úsudkem bez rovnice
     3  Podmínka, že výsledek je celé číslo

DAT  Grafy, tabulky, průměr  (3,4 b.)
├─ Grafy a tabulky  (2,9 b.)
│    1  Čtení sloupcového grafu (více řad, skládaný)
│    2  Doplnění chybějícího údaje z podmínek v textu
│    3  Kruhový diagram (procenta, středové úhly)
│    3  Čtení tabulky, třídění údajů z textu
│    S  Statistický soubor, statistický znak, statistické šetření, četnost
│    S  Volba vhodné tabulky a diagramu, vytvoření diagramu z dat
└─ Aritmetický průměr  (1,1 b.)
     2  Výpočet aritmetického průměru
     3  Průměr z tabulky četností
     3  Chybějící hodnota z daného průměru

GEO  Geometrie: výpočty  (9,9 b.)
├─ Úhly  (2,1 b.)
│    1  Vrcholové, vedlejší, souhlasné a střídavé úhly
│    1  Součet úhlů v trojúhelníku a čtyřúhelníku
│    2  Úhly v rovnoramenném a rovnostranném trojúhelníku
│    2  Úhly zapsané jako α, 2α, 3α nebo poměrem
│    3  Osa úhlu
│    3  Pravidelný mnohoúhelník
│    3  Úhly v kružnici: poloměry a Thaletova věta
├─ Pythagorova věta  (1,6 b.)
│    1  Přepona z odvěsen, odvěsna z přepony
│    2  Nalezení pravoúhlého trojúhelníku v útvaru
│    2  Pythagorova věta v tělesech
├─ Obvod a obsah rovinných útvarů  (3,7 b.)
│    1  Vzorce pro obvod a obsah
│    1  Strana nebo výška z obsahu
│    3  Obsah vypočtený dvěma způsoby
│    3  Lichoběžník rozdělený na obdélník a trojúhelník
│    2  Složené útvary
│    2  Obvod vyjádřený proměnnou
│    3  Trojúhelníková nerovnost
│    3  Rozestupy po obvodu
│    S  Obvod a obsah mnohoúhelníku ve čtvercové síti
│    S  Shodnost trojúhelníků
│    S  Podobnost trojúhelníků: věty sss, sus, uu, poměr podobnosti
├─ Kruh a kružnice  (0,6 b.)
│    1  Obvod a obsah kruhu, počítání s π ≐ 3,14, zaokrouhlení
│    3  Poloměr nebo průměr z obsahu
│    3  Půlkruh, čtvrtkruh, výseč: obsah a obvod
│    3  Útvary ohraničené oblouky
│    S  Vzájemná poloha kružnice a přímky: tečna, sečna, vnější přímka
│    S  Vzájemná poloha dvou kružnic, průsečíky a body dotyku
└─ Tělesa  (3,9 b.)
     1  Krychle a kvádr: objem, povrch, součet hran, i zpětně
     1  Kolmý hranol: objem a povrch
     2  Válec: objem, plášť, povrch
     3  Síť tělesa
     2  Slepená a rozříznutá tělesa
     3  Tělesa z krychliček, prostorová představivost
     3  Vztah místo čísla: rovnice pro výšku nebo hranu
     3  Objem v litrech, výška hladiny
     S  Pohled na těleso shora, zepředu, zprava, zleva a zdola
     S  Náčrt sítě a obrazu tělesa ve volném rovnoběžném promítání
     S  Jehlan: rozpoznání, síť, pohledy, metrické a polohové vlastnosti
     S  Koule: poloměr a průměr ve slovních úlohách

KON  Geometrie: konstrukce  (5,8 b.)
├─ Základní konstrukce  (5,3 b.)
│    1  Kolmice a rovnoběžka daným bodem
│    1  Střed a osa úsečky
│    3  Osa úhlu
│    1  Přenesení délky kružnicí
│    3  Úhel dané velikosti
│    1  Thaletova kružnice nad úsečkou
│    1  Obraz bodu ve středové souměrnosti („S je střed“)
│    2  Obraz v osové souměrnosti, osa z bodu a jeho obrazu
│    S  Přenesení úhlu
│    S  Kružnice opsaná trojúhelníku
│    S  Tečna kružnice v jejím bodě
├─ Vlastnosti útvarů, o které se konstrukce opírá  (4,9 b.)
│    1  Rovnoramenný trojúhelník: osa souměrnosti je osou základny
│    3  Rovnostranný trojúhelník
│    2  Pravoúhlý trojúhelník: kolmé odvěsny, vrchol pravého úhlu na Thaletově kružnici
│    2  Výška a těžnice
│    3  Čtverec: shodné, kolmé, půlící se úhlopříčky
│    1  Obdélník: pravé úhly, shodné půlící se úhlopříčky, vrcholy na kružnici
│    1  Rovnoběžník: úhlopříčky se půlí, střed souměrnosti
│    3  Kosočtverec: kolmé úhlopříčky, osa souměrnosti
│    3  Lichoběžník: rovnoramenný a pravoúhlý
│    3  Pravidelný šestiúhelník: strana = poloměr kružnice opsané
│    S  Pravidelný osmiúhelník
├─ Rozbor zadání  (3,6 b.)
│    1  Náčrt a převod nepřímé podmínky na množinu bodů
│    1  „Najděte všechna řešení“: druhé řešení
│    S  Trojúhelník a čtyřúhelník ze zadaných údajů (sss, sus, usu)
└─ Souměrnost útvarů  (0,5 b.)
     3  Osy souměrnosti útvaru ve čtvercové síti a mnohoúhelníků
     S  Samodružný bod a útvar; vzor a obraz
     S  Obraz celého útvaru ve středové souměrnosti

ZAK  Zákonitosti a úsudek  (4,2 b.)
├─ Rostoucí obrazce a číselné řady  (3,0 b.)
│    1  Pokračování pravidla a tabulka počtů po krocích
│    1  Obecný n-tý člen (lineární růst, n², n·(n + 1)/2)
│    2  Obrácení pravidla: který krok má daný počet
│    3  Růst násobením (mocniny tří)
│    3  Číselná řada daná pravidlem
└─ Úsudek a systematické hledání  (1,3 b.)
     3  Periodické děje: cykly a společný násobek
     3  Systematické vypsání všech řešení
     3  Strategické a netradiční geometrické úlohy
```

## Počítání s čísly (POC)

8,2 points per standard test · success 49 % · The tools every other branch uses. Fast and error-free here is what frees time for tasks 6–16.

### Číselné výrazy, mocniny, odmocniny

`POC.VYR` · 1,9 points per standard test, in 14 of 16 · success 36 % · specification area 1 · One or two 1-point openers; from 2025 also inside the fraction task.

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Pořadí operací, závorky, záporná čísla | postup |  | 3 · 0 | 0,2 | 16 · 8 · 32,2 | 68 % | [2022 B 1](../backend/data/screenshots/M9-2022-B-01.png) 68 % | Sign rules: (−6)² = 36, −3·(−3) = +9. |
| 1 | Počítání s desetinnými čísly bez kalkulačky | postup | Pořadí operací (POC.VYR) | 4 · 2 | 0,2 | 16 · 8 · 16,3 | 52 % | [2026 A 2.1](../backend/data/screenshots/M9-2026-A-02.png) 52 % | Multiplying and dividing by decimals: (0,08 − 1) : 0,2. |
| 1 | Druhá mocnina a odmocnina | znalost |  | 8 · 2 | 0,6 | 16 · 8 · 7,6 | 59 % | [2023 B 1](../backend/data/screenshots/M9-2023-B-01.png) 65 % · [2022 A 1](../backend/data/screenshots/M9-2022-A-01.png) 82 % | Squares 1–20 and their roots, decimals, powers of ten, root of a fraction and of a product. Compute inside the root first. Needed all over geometry. |
| 3 | Výraz zadaný slovy (součet, rozdíl, součin, podíl) | překlad | Pořadí operací (POC.VYR) | 2 · 1 | 0,1 |  | 44 % | [2025 A 1](../backend/data/screenshots/M9-2025-A-01.png) 44 % | The verbal items are the ones that fail, not the computations. |
| 3 | Číselná osa se stejnými dílky | postup |  | 1 · 0 | 0,1 | 2 · 0 · 0,2 | – |  |  |
| 2 | Zaokrouhlení výsledku na daný řád | postup | Počítání s desetinnými čísly bez kalkulačky (POC.VYR) | 7 · 2 | 0,9 |  | 28 % | [2024 A 2](../backend/data/screenshots/M9-2024-A-02.png) 16 % · [2023 B 8.2](../backend/data/screenshots/M9-2023-B-08.png) 18 % · [2026 B 7.2](../backend/data/screenshots/M9-2026-B-07.png) 19 % | The last step of the π tasks: „zaokrouhlete na desítky cm³ / celé cm² / desetiny centimetru“. Round once, at the end. |
| S | Absolutní hodnota a opačné číslo | znalost |  |  |  |  |  |  | B1, 1: „určí číslo kladné, záporné a opačné, znázorní a určí absolutní hodnotu čísla“. |
| S | Periodické číslo: zápis, porovnání, převod zlomku | znalost |  |  |  |  |  |  | B1, 1: „rozumí zápisu … desetinného čísla včetně periodického čísla“, „převádí zlomek na desetinné číslo včetně čísla s periodou“. One appears only as an answer option (2022 A 14). |
| S | Odhad výsledku s danou přesností | postup |  |  |  |  |  |  | B1, 1: „provádí odhady početních operací s racionálními čísly s danou přesností“. |

### Počítání se zlomky

`POC.ZLOM` · 4,0 points per standard test, in 16 of 16 · success 62 % · specification area 1 · The computation task of every test: 3–4 points, among the best solved open tasks. Fraction word problems are in VZT.

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Čtyři operace se zlomky, společný jmenovatel, krácení, základní tvar | postup | Pořadí operací (POC.VYR) | 15 · 7 | 1,9 | 16 · 8 · 18,6 | 60 % | [2026 B 2.2](../backend/data/screenshots/M9-2026-B-02.png) 56 % · [2023 A 3.1](../backend/data/screenshots/M9-2023-A-03.png) 59 % · [2022 A 3.1](../backend/data/screenshots/M9-2022-A-03.png) 60 % | An unreduced result costs 1 of 2 points. Never multiply the expression by the common denominator as if it were an equation. |
| 1 | Složený zlomek | postup | Čtyři operace se zlomky (POC.ZLOM) | 14 · 6 | 1,8 |  | 65 % | [2023 A 3.3](../backend/data/screenshots/M9-2023-A-03.png) 58 % · [2024 B 3.2](../backend/data/screenshots/M9-2024-B-03.png) 58 % · [2026 A 2.2](../backend/data/screenshots/M9-2026-A-02.png) 60 % | The worked 2-point item in almost every test. |
| 3 | Zlomky spolu s desetinnými čísly | postup | Čtyři operace se zlomky (POC.ZLOM), Počítání s desetinnými čísly bez kalkulačky (POC.VYR) | 1 · 1 | 0,1 |  | 64 % | [2024 A 3.2](../backend/data/screenshots/M9-2024-A-03.png) 64 % | Convert the decimal to a fraction first (1,4 = 7/5). |
| 2 | Zlomky s druhou mocninou a odmocninou | postup | Čtyři operace se zlomky (POC.ZLOM), Druhá mocnina a odmocnina (POC.VYR) | 4 · 4 | 0,6 |  | 61 % | [2025 A 2.2](../backend/data/screenshots/M9-2025-A-02.png) 56 % · [2025 B 3.2](../backend/data/screenshots/M9-2025-B-03.png) 66 % | From 2025. |
| 3 | Smíšené číslo | postup | Čtyři operace se zlomky (POC.ZLOM) | 1 · 1 | 0,1 |  | 34 % | [2025 B 2](../backend/data/screenshots/M9-2025-B-02.png) 34 % | Once in 20 tests. |
| S | Porovnávání zlomků | postup |  |  |  |  |  |  | B1, 1: „porovnává zlomky“. Not asked as a task of its own. |
| S | Převrácený zlomek podle názvu | znalost |  |  |  |  |  |  | B1, 1: „zapíše převrácený zlomek“. Used silently whenever a fraction divides. |

### Dělitelnost

`POC.DEL` · 0,9 points per standard test, in 8 of 16 · success 15 % · specification area 1 · Small and badly solved (19 %); usually hidden in a word problem.

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 2 | Dělitelé a násobky čísla | postup |  | 3 · 2 | 0,2 | 7 · 5 · 1,0 | 12 % | [2025 A 8.3](../backend/data/screenshots/M9-2025-A-08.png) 2 % |  |
| 2 | Prvočísla a rozklad na prvočísla | postup | Dělitelé a násobky čísla (POC.DEL) | 3 · 3 | 0,4 |  | 24 % | [2026 B 12](../backend/data/screenshots/M9-2026-B-12.png) 20 % · [2025 B 6.3](../backend/data/screenshots/M9-2025-B-06.png) 23 % · [2025 B 6.2](../backend/data/screenshots/M9-2025-B-06.png) 27 % | 2 is the only even prime. |
| 3 | Dělení se zbytkem ve slovní úloze | postup |  | 1 · 1 | 0,1 | 2 · 1 · 0,2 | – |  |  |
| 3 | Společný násobek | postup | Dělitelé a násobky čísla (POC.DEL) | 2 · 1 | 0,2 | 2 · 1 · 0,5 | 6 % | [2026 A 16.3](../backend/data/screenshots/M9-2026-A-16.png) 1 % · [2022 A 16.3](../backend/data/screenshots/M9-2022-A-16.png) 11 % | Never asked by name, but it is what common denominators and the periodic tasks of task 16 use. |
| S | Znaky dělitelnosti čísly 2, 3, 4, 5, 6, 8 a 10 | znalost |  |  |  |  |  |  | B1, 1. |
| S | Nejmenší společný násobek a největší společný dělitel dvou až tří čísel | postup |  |  |  |  |  |  | B1, 1. The words do not occur in the 20 tests. |

### Převody jednotek

`POC.JED` · 1,6 points per standard test, in 9 of 16 · success 51 % · specification area 1 · Rarely a task of its own; mostly silent: data in one unit, answer demanded in another.

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 2 | Délka (mm, cm, dm, m, km) | znalost |  | 5 · 3 | 0,6 | 8 · 5 · 0,9 | 60 % | [2024 B 1](../backend/data/screenshots/M9-2024-B-01.png) 50 % |  |
| 3 | Obsah (krok × 100) | znalost | Délka (mm (POC.JED) | 2 · 1 | 0,1 | 3 · 1 · 0,4 | 37 % | [2026 B 1](../backend/data/screenshots/M9-2026-B-01.png) 41 % |  |
| 3 | Objem a litry (krok × 1 000, 1 l = 1 dm³) | znalost | Délka (mm (POC.JED) | 3 · 1 | 0,2 | 3 · 1 · 0,2 | 25 % | [2023 A 2.2](../backend/data/screenshots/M9-2023-A-02.png) 24 % · [2022 A 2.2](../backend/data/screenshots/M9-2022-A-02.png) 39 % |  |
| 3 | Hmotnost (g, kg) | znalost |  | 1 · 1 | 0,1 |  | – |  |  |
| 2 | Čas (hodiny, minuty, desetinné hodiny, sčítání časů) | znalost |  | 5 · 3 | 0,6 | 7 · 5 · 0,9 | 74 % | [2022 A 11.2](../backend/data/screenshots/M9-2022-A-11.png) 64 % · [2022 A 11.3](../backend/data/screenshots/M9-2022-A-11.png) 71 % · [2022 A 11.1](../backend/data/screenshots/M9-2022-A-11.png) 87 % | Needed for pohyb. |
| 3 | Stupně a minuty (1° = 60′) | znalost |  | 0 · 0 | 0,0 |  | – |  |  |
| S | Sekunda a týden v převodech času | znalost |  |  |  |  |  |  | A1, 2: „časové jednotky (sekunda, minuta, hodina, den, týden)“. **Before 2022: 2019 A 7.2.** |

## Výrazy a rovnice (ALG)

8,0 points per standard test · success 49 % · Two fixed tasks, 8 points in every one of the 20 tests, each with a fixed set of item roles. The most predictable points of the test.

### Úpravy výrazů

`ALG.VYR` · 4,0 points per standard test, in 16 of 16 · success 47 % · specification area 1 · Always three items, 1 + 1 + 2 points.

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Roznásobení závorek a sloučení členů | postup | Pořadí operací (POC.VYR) | 16 · 8 | 2,6 | 16 · 8 · 12,7 | 51 % | [2025 B 4.1](../backend/data/screenshots/M9-2025-B-04.png) 32 % · [2024 A 4.3](../backend/data/screenshots/M9-2024-A-04.png) 32 % · [2025 A 3.2](../backend/data/screenshots/M9-2025-A-03.png) 32 % | The worked 2-point item. The trap is a bracket to simplify before multiplying, e.g. (3n − 2n). |
| 2 | Vytýkání | postup | Roznásobení závorek a sloučení členů (ALG.VYR) | 8 · 3 | 0,5 |  | 42 % | [2023 A 4.1](../backend/data/screenshots/M9-2023-A-04.png) 38 % · [2022 B 4.1](../backend/data/screenshots/M9-2022-B-04.png) 38 % · [2023 B 4.1](../backend/data/screenshots/M9-2023-B-04.png) 46 % | Usually after simplifying first; also a prescribed factor such as (−x). |
| 1 | Umocnění dvojčlenu (a ± b)² | postup | Roznásobení závorek a sloučení členů (ALG.VYR), Druhá mocnina a odmocnina (POC.VYR) | 12 · 5 | 0,9 | 15 · 7 · 1,6 | 38 % | [2024 A 4.1](../backend/data/screenshots/M9-2024-A-04.png) 9 % · [2023 A 4.2](../backend/data/screenshots/M9-2023-A-04.png) 34 % · [2022 A 4.2](../backend/data/screenshots/M9-2022-A-04.png) 34 % | Awkward coefficients: fractions, decimals, two minus signs. |
| 3 | Vzorec (a ± b)² zpětně: rozklad trojčlenu, doplnění chybějících čísel | postup | Umocnění dvojčlenu (a ± b)² (ALG.VYR) | 2 · 1 | 0,1 |  | 65 % | [2025 A 3.1](../backend/data/screenshots/M9-2025-A-03.png) 65 % | In 2022–2026 only as „Do rámečků doplňte chybějící čísla“; factoring a whole trinomial (9a² − 30a + 25) was asked in 2021 A 4.1. |
| 2 | Rozklad a² − b² na součin | postup | Umocnění dvojčlenu (a ± b)² (ALG.VYR) | 7 · 4 | 0,5 |  | 47 % | [2024 B 4.2](../backend/data/screenshots/M9-2024-B-04.png) 23 % · [2026 A 3.2](../backend/data/screenshots/M9-2026-A-03.png) 46 % · [2023 B 4.2](../backend/data/screenshots/M9-2023-B-04.png) 46 % | In disguise: 49 − (−4a)², or simplify first and then factor. |
| 3 | Hodnota výrazu pro dané číslo | postup |  | 1 · 1 | 0,1 |  | 48 % | [2026 A 3.1](../backend/data/screenshots/M9-2026-A-03.png) 48 % |  |

### Lineární rovnice a soustavy

`ALG.ROV` · 4,0 points per standard test, in 16 of 16 · success 50 % · specification area 1 · Two worked items of 2 points; the check is never required.

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Rovnice se závorkami a desetinnými čísly | postup | Roznásobení závorek a sloučení členů (ALG.VYR), Počítání s desetinnými čísly bez kalkulačky (POC.VYR) | 11 · 4 | 1,4 | 16 · 8 · 8,8 | 51 % | [2022 A 5.1](../backend/data/screenshots/M9-2022-A-05.png) 46 % · [2024 B 5.1](../backend/data/screenshots/M9-2024-B-05.png) 48 % · [2026 A 4.1](../backend/data/screenshots/M9-2026-A-04.png) 48 % |  |
| 1 | Rovnice se zlomky | postup | Rovnice se závorkami a desetinnými čísly (ALG.ROV), Čtyři operace se zlomky (POC.ZLOM) | 14 · 6 | 2,1 | 16 · 8 · 5,4 | 50 % | [2024 A 5.2](../backend/data/screenshots/M9-2024-A-05.png) 27 % · [2025 A 4.1](../backend/data/screenshots/M9-2025-A-04.png) 33 % · [2025 B 5.1](../backend/data/screenshots/M9-2025-B-05.png) 38 % | Keep each numerator in a bracket; the minus before a fraction is the classic error. |
| 3 | Rovnice bez řešení | znalost | Rovnice se závorkami a desetinnými čísly (ALG.ROV) | 2 · 1 | 0,2 |  | 45 % | [2025 A 4.2](../backend/data/screenshots/M9-2025-A-04.png) 36 % · [2023 A 5.1](../backend/data/screenshots/M9-2023-A-05.png) 54 % | The sentence „rovnice nemá řešení“ must be written. „Nekonečně mnoho řešení“ is in the specification only. |
| 3 | Rovnice s druhými mocninami dvojčlenů, ve které x² vypadne | postup | Rovnice se závorkami a desetinnými čísly (ALG.ROV), Umocnění dvojčlenu (a ± b)² (ALG.VYR) | 0 · 0 | 0,0 |  | 35 % | [2024 A 5.1](../backend/data/screenshots/M9-2024-A-05.png) 35 % | Only in the 2024 tests. |
| 1 | Soustava dvou rovnic se dvěma neznámými | postup | Rovnice se závorkami a desetinnými čísly (ALG.ROV) | 4 · 4 | 0,5 | 7 · 6 · 1,3 | 59 % | [2025 B 5.2](../backend/data/screenshots/M9-2025-B-05.png) 58 % · [2026 A 4.2](../backend/data/screenshots/M9-2026-A-04.png) 60 % | From 2025, in 4 of 8 tests. Dosazovací or sčítací metoda. |
| S | Rovnice s nekonečně mnoha řešeními | znalost |  |  |  |  |  |  | C1, 1: „rozhodne, má-li rovnice jedno řešení, nekonečně mnoho řešení, nebo nemá řešení“. Only the other two outcomes are keyed in the 20 tests. |

## Vztahy mezi veličinami: zlomek, procento, poměr (VZT)

16,9 points per standard test · success 43 % · The same relation is told as a fraction, a percentage or a ratio. Most points of tasks 6–8 and 15 are lost on reading the relation, not on computing.

### Zlomek jako část celku

`VZT.CAST` · 2,3 points per standard test, in 13 of 16 · success 39 % · specification area 1 · Single 1-point word items solved by 21–33 %, while the fraction computation task scores 58–76 %.

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Zlomek z množství a z času | překlad | Čtyři operace se zlomky (POC.ZLOM) | 8 · 4 | 0,8 | 13 · 7 · 2,4 | 58 % | [2022 A 11.2](../backend/data/screenshots/M9-2022-A-11.png) 64 % · [2022 A 11.3](../backend/data/screenshots/M9-2022-A-11.png) 71 % · [2022 A 11.1](../backend/data/screenshots/M9-2022-A-11.png) 87 % |  |
| 3 | Část ze zbytku | překlad | Zlomek z množství a z času (VZT.CAST) | 1 · 1 | 0,1 | 2 · 1 · 0,2 | – |  | „dvě pětiny zbytku“ is a part of what is left, not of the whole. |
| 3 | Zlomek ze zlomku | překlad | Zlomek z množství a z času (VZT.CAST) | 2 · 1 | 0,2 |  | 39 % | [2023 B 15.2](../backend/data/screenshots/M9-2023-B-15.png) 50 % | „Tři čtvrtiny z této utracené částky“, „čtvrtina vzdálenosti, kterou předtím ujel“: multiply the fractions. |
| 2 | Celek z části | překlad | Zlomek z množství a z času (VZT.CAST) | 8 · 4 | 1,3 |  | 31 % | [2025 B 7.3](../backend/data/screenshots/M9-2025-B-07.png) 13 % · [2022 B 6](../backend/data/screenshots/M9-2022-B-06.png) 32 % · [2023 A 1](../backend/data/screenshots/M9-2023-A-01.png) 33 % | „pětina a o 180 více“ – find what fraction the known number is. |

### Srovnání „o … více než“, „kolikrát“

`VZT.NEZ` · 3,6 points per standard test, in 15 of 16 · success 35 % · specification area 1 · The phrases that carry the difficulty across fractions, percentages and word problems (03, section 20). Learn them once, here.

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | „o kolik“ je rozdíl, „kolikrát“ je podíl | překlad |  | 10 · 4 | 0,9 |  | 41 % | [2023 A 2.1](../backend/data/screenshots/M9-2023-A-02.png) 30 % |  |
| 1 | „o třetinu více / méně než“ jako násobení | překlad | Čtyři operace se zlomky (POC.ZLOM) | 10 · 6 | 1,8 | 16 · 8 · 8,3 | 30 % | [2025 B 7.1](../backend/data/screenshots/M9-2025-B-07.png) 19 % · [2023 B 15.3](../backend/data/screenshots/M9-2023-B-15.png) 40 % | 4/3 · x and 2/3 · x, where x is the quantity after „než“. |
| 2 | „dvakrát méně“, „čtyřikrát menší než“ jako dělení | překlad |  | 4 · 4 | 0,4 |  | 47 % | [2025 A 5.1](../backend/data/screenshots/M9-2025-A-05.png) 47 % |  |
| 1 | Obrácení vztahu: neznámá není veličina za „než“ | překlad | „o třetinu více / méně než“ jako násobení (VZT.NEZ) | 5 · 3 | 0,4 | 16 · 8 · 7,0 | 33 % | [2023 A 15.2](../backend/data/screenshots/M9-2023-A-15.png) 28 % · [2026 A 5](../backend/data/screenshots/M9-2026-A-05.png) 28 % · [2024 B 12](../backend/data/screenshots/M9-2024-B-12.png) 33 % | „o polovinu levnější než skříň“ with the table = n means the wardrobe is 2n. Solved by 8–28 %. |

### Procenta

`VZT.PROC` · 7,1 points per standard test, in 16 of 16 · success 49 % · specification area 1 · The largest topic: task 15 in every standard test plus one or two items elsewhere. Points are lost on choosing the base.

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Procentová část, počet procent, základ | postup | Počítání s desetinnými čísly bez kalkulačky (POC.VYR) | 11 · 7 | 2,3 | 16 · 8 · 7,5 | 52 % | [2025 A 15.2](../backend/data/screenshots/M9-2025-A-15.png) 30 % · [2025 B 15.3](../backend/data/screenshots/M9-2025-B-15.png) 34 % · [2025 A 5.2](../backend/data/screenshots/M9-2025-A-05.png) 34 % | Where the base is the obvious number, items score 70–80 %. |
| 1 | „o x % více / méně“ jako násobitel | překlad | Procentová část (VZT.PROC) | 9 · 4 | 1,1 | 11 · 5 · 2,9 | 50 % | [2025 A 15.3](../backend/data/screenshots/M9-2025-A-15.png) 31 % · [2023 B 2.1](../backend/data/screenshots/M9-2023-B-02.png) 40 % · [2023 B 2.2](../backend/data/screenshots/M9-2023-B-02.png) 50 % | +25 % is ·1,25; −40 % is ·0,6; +150 % is ·2,5. |
| 2 | Základ po změně („což je o 40 % více než loni“) | překlad | „o x % více / méně“ jako násobitel (VZT.PROC) | 7 · 3 | 1,0 |  | 35 % | [2022 A 15.2](../backend/data/screenshots/M9-2022-A-15.png) 32 % · [2026 B 15.1](../backend/data/screenshots/M9-2026-B-15.png) 42 % | Divide by the multiplier: 420 : 1,4. |
| 2 | „O kolik procent“ se liší dvě veličiny | překlad | Procentová část (VZT.PROC) | 7 · 3 | 1,3 | 8 · 4 · 1,6 | 47 % | [2022 B 15.3](../backend/data/screenshots/M9-2022-B-15.png) 24 % · [2026 B 5.2](../backend/data/screenshots/M9-2026-B-05.png) 32 % · [2026 A 15.1](../backend/data/screenshots/M9-2026-A-15.png) 42 % | Difference divided by the quantity after „než“. |
| 3 | Obrácené srovnání („o třetinu méně“ je opačně „o 50 % více“) | překlad | „O kolik procent“ se liší dvě veličiny (VZT.PROC), Obrácení vztahu (VZT.NEZ) | 2 · 1 | 0,2 |  | 12 % | [2025 B 15.2](../backend/data/screenshots/M9-2025-B-15.png) 12 % | In 2025 B 15.2 the naive option 33 % drew 47,8 % of candidates. |
| 3 | Dvě změny po sobě | postup | „o x % více / méně“ jako násobitel (VZT.PROC) | 2 · 1 | 0,3 |  | 56 % | [2023 A 15.3](../backend/data/screenshots/M9-2023-A-15.png) 36 % · [2023 A 15.1](../backend/data/screenshots/M9-2023-A-15.png) 50 % · [2024 A 16.3](../backend/data/screenshots/M9-2024-A-16.png) 64 % | Multiply the multipliers: +40 % then −40 % is ·0,84. |
| 3 | Procento ze zbytku | překlad | Procentová část (VZT.PROC), Část ze zbytku (VZT.CAST) | 1 · 0 | 0,1 |  | 40 % | [2022 B 15.2](../backend/data/screenshots/M9-2022-B-15.png) 40 % |  |
| 2 | Dvě veličiny svázané procentem a známý součet | překlad | „o x % více / méně“ jako násobitel (VZT.PROC), Rovnice se závorkami a desetinnými čísly (ALG.ROV) | 8 · 5 | 1,1 |  | 33 % | [2022 A 15.3](../backend/data/screenshots/M9-2022-A-15.png) 19 % · [2026 B 15.3](../backend/data/screenshots/M9-2026-B-15.png) 35 % · [2025 A 13](../backend/data/screenshots/M9-2025-A-13.png) 44 % | x + 0,7x = 680. |
| 2 | Procento, zlomek a poměr: převody mezi nimi | znalost | Procentová část (VZT.PROC) | 7 · 3 | 1,1 |  | 55 % | [2024 B 16.1](../backend/data/screenshots/M9-2024-B-16.png) 67 % | „každý dvacátý“ = 5 %; 3 : 2 is „o 50 % více“. |
| 3 | Změna v procentních bodech | překlad | Procentová část (VZT.PROC) | 0 · 0 | 0,0 |  | – |  | Once in 20 tests. |
| 3 | Úrok za jeden rok a daň z úroku | postup | Procentová část (VZT.PROC) | 0 · 0 | 0,0 |  | 61 % | [2024 A 16.2](../backend/data/screenshots/M9-2024-A-16.png) 50 % · [2024 A 16.1](../backend/data/screenshots/M9-2024-A-16.png) 73 % | Once in 20 tests. |
| S | Promile | znalost |  |  |  |  |  |  | B1, 1. |
| S | Jistina, úroková míra, úrokovací období, inflace; půjčky a úvěry | znalost |  |  |  |  |  |  | C1, 1: „používá s porozuměním základní pojmy finanční matematiky“, „získá základní informace o půjčkách a úvěrech“. |

### Poměr a úměrnost

`VZT.POM` · 3,0 points per standard test, in 13 of 16 · success 38 % · specification area 1, 2, 3 · Result-only tasks 6–8 with graduated sub-items, or multiple choice. No formula is asked for; small numbers and reasoning.

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Poměr v základním tvaru, dělení v poměru | postup | Čtyři operace se zlomky (POC.ZLOM) | 7 · 3 | 1,0 | 13 · 6 · 3,0 | 43 % | [2023 A 7.3](../backend/data/screenshots/M9-2023-A-07.png) 13 % · [2026 A 11.2](../backend/data/screenshots/M9-2026-A-11.png) 65 % | Also the parts from their difference: 3 : 5 and a difference of 600 g. |
| 3 | Poměr na číselné ose a na úsečce | postup | Poměr v základním tvaru (VZT.POM), Číselná osa se stejnými dílky (POC.VYR) | 1 · 0 | 0,1 |  | 24 % | [2022 B 2.1](../backend/data/screenshots/M9-2022-B-02.png) 22 % · [2022 B 2.2](../backend/data/screenshots/M9-2022-B-02.png) 25 % |  |
| 3 | Měřítko mapy a plánu | postup | Poměr v základním tvaru (VZT.POM), Délka (mm (POC.JED), Obsah (krok × 100) (POC.JED) | 1 · 0 | 0,2 |  | 59 % | [2024 A 15.3](../backend/data/screenshots/M9-2024-A-15.png) 42 % · [2023 A 11.2](../backend/data/screenshots/M9-2023-A-11.png) 51 % · [2023 A 11.3](../backend/data/screenshots/M9-2023-A-11.png) 61 % | Area scales with the square of the length scale. |
| 1 | Přímá úměrnost | postup | Poměr v základním tvaru (VZT.POM) | 6 · 3 | 0,7 | 10 · 6 · 1,7 | 58 % | [2022 A 7.1](../backend/data/screenshots/M9-2022-A-07.png) 54 % · [2023 B 6.1](../backend/data/screenshots/M9-2023-B-06.png) 56 % · [2026 B 5.1](../backend/data/screenshots/M9-2026-B-05.png) 64 % |  |
| 2 | Nepřímá úměrnost | postup | Přímá úměrnost (VZT.POM) | 4 · 1 | 0,5 | 5 · 2 · 0,7 | 19 % | [2023 B 6.3](../backend/data/screenshots/M9-2023-B-06.png) 2 % · [2024 A 1](../backend/data/screenshots/M9-2024-A-01.png) 18 % · [2023 B 6.2](../backend/data/screenshots/M9-2023-B-06.png) 23 % |  |
| 3 | Společná práce | postup | Nepřímá úměrnost (VZT.POM), Čtyři operace se zlomky (POC.ZLOM) | 2 · 1 | 0,2 |  | 13 % | [2022 A 7.3](../backend/data/screenshots/M9-2022-A-07.png) 9 % | Add the rates per unit of time, not the times. |
| 2 | Pohyb: s = v · t | postup | Přímá úměrnost (VZT.POM), Čas (hodiny (POC.JED) | 3 · 3 | 0,4 |  | 28 % | [2026 A 7.2](../backend/data/screenshots/M9-2026-A-07.png) 25 % · [2026 A 7.1](../backend/data/screenshots/M9-2026-A-07.png) 34 % |  |
| 3 | Směsi a průměrná cena | postup | Poměr v základním tvaru (VZT.POM) | 1 · 0 | 0,2 |  | – |  |  |
| S | Postupný a převrácený poměr, změna čísla v daném poměru | postup |  |  |  |  |  |  | B1, 1: „změní číslo v daném poměru“, „zapíše a upraví postupný a převrácený poměr“. |
| S | Bod v pravoúhlé soustavě souřadnic | postup |  |  |  |  |  |  | B1, 2: „vyznačí bod v pravoúhlé soustavě souřadnic …, zapíše souřadnice daného bodu“. No coordinate system in any of the 20 tests. |
| S | Přímá a nepřímá úměrnost tabulkou, rovnicí a grafem | postup |  |  |  |  |  |  | C1, 2: „vyjádří přímou a nepřímou úměrnost tabulkou, rovnicí a grafem“. |

### Slovní úlohy na rovnici

`VZT.SLOV` · 4,7 points per standard test, in 16 of 16 · success 33 % · specification area 1 · The fixed three-step task (two expressions, then an equation) in 12 of 16 standard tests; its last step is solved by 10–27 %.

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Vyjádření veličiny výrazem s proměnnou | překlad | „o třetinu více / méně než“ jako násobení (VZT.NEZ), Obrácení vztahu (VZT.NEZ) | 13 · 6 | 1,3 | 15 · 8 · 6,6 | 36 % | [2025 B 7.2](../backend/data/screenshots/M9-2025-B-07.png) 12 % · [2026 A 6.2](../backend/data/screenshots/M9-2026-A-06.png) 17 % · [2023 A 8.1](../backend/data/screenshots/M9-2023-A-08.png) 28 % | The answer is an expression such as 4x/3, not a number. |
| 1 | Sestavení a vyřešení rovnice z další podmínky | rozbor | Vyjádření veličiny výrazem s proměnnou (VZT.SLOV), Rovnice se zlomky (ALG.ROV) | 12 · 6 | 1,8 | 14 · 8 · 3,2 | 28 % | [2026 A 6.3](../backend/data/screenshots/M9-2026-A-06.png) 10 % · [2023 B 7.3](../backend/data/screenshots/M9-2023-B-07.png) 18 % · [2024 B 7.2](../backend/data/screenshots/M9-2024-B-07.png) 35 % | Answer the quantity that is asked, which may not be x. |
| 2 | Dvě neznámé: počty a součty | rozbor | Sestavení a vyřešení rovnice z další podmínky (VZT.SLOV), Soustava dvou rovnic se dvěma neznámými (ALG.ROV) | 5 · 4 | 0,8 |  | 27 % | [2026 B 6.3](../backend/data/screenshots/M9-2026-B-06.png) 19 % |  |
| 2 | Řešení úsudkem bez rovnice | rozbor |  | 4 · 2 | 0,8 |  | 56 % | [2024 A 7.1](../backend/data/screenshots/M9-2024-A-07.png) 56 % · [2024 A 7.2](../backend/data/screenshots/M9-2024-A-07.png) 56 % |  |
| 3 | Podmínka, že výsledek je celé číslo | rozbor | Sestavení a vyřešení rovnice z další podmínky (VZT.SLOV), Dělení se zbytkem ve slovní úloze (POC.DEL) | 1 · 0 | 0,1 |  | – |  |  |

## Grafy, tabulky, průměr (DAT)

3,4 points per standard test · success 52 % · Task 11 (A/N) in 9 of 16 standard tests. Reading values is easy; the conditions in the text are where points go.

### Grafy a tabulky

`DAT.GRAF` · 2,9 points per standard test, in 13 of 16 · success 53 % · specification area 2

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Čtení sloupcového grafu (více řad, skládaný) | postup |  | 4 · 2 | 1,0 | 10 · 5 · 2,3 | 60 % | [2024 B 15.3](../backend/data/screenshots/M9-2024-B-15.png) 40 % · [2024 B 15.2](../backend/data/screenshots/M9-2024-B-15.png) 65 % · [2024 B 15.1](../backend/data/screenshots/M9-2024-B-15.png) 77 % |  |
| 2 | Doplnění chybějícího údaje z podmínek v textu | rozbor | Čtení sloupcového grafu (více řad (DAT.GRAF) | 8 · 4 | 1,8 |  | 44 % | [2023 A 7.1](../backend/data/screenshots/M9-2023-A-07.png) 11 % · [2023 A 7.3](../backend/data/screenshots/M9-2023-A-07.png) 13 % · [2023 A 7.2](../backend/data/screenshots/M9-2023-A-07.png) 18 % | A missing bar or an axis without numbers. Open versions score 14–50 %. |
| 3 | Kruhový diagram (procenta, středové úhly) | postup | Procentová část (VZT.PROC) | 3 · 2 | 0,6 |  | 61 % | [2022 A 14](../backend/data/screenshots/M9-2022-A-14.png) 35 % · [2025 B 11.2](../backend/data/screenshots/M9-2025-B-11.png) 59 % · [2026 A 11.3](../backend/data/screenshots/M9-2026-A-11.png) 62 % | 360° is the whole, 60° is one sixth. |
| 3 | Čtení tabulky, třídění údajů z textu | postup |  | 0 · 0 | 0,0 |  | 56 % | [2024 A 7.1](../backend/data/screenshots/M9-2024-A-07.png) 56 % · [2024 A 7.2](../backend/data/screenshots/M9-2024-A-07.png) 56 % |  |
| S | Statistický soubor, statistický znak, statistické šetření, četnost | znalost |  |  |  |  |  |  | C1, 2. Medián and modus are neither in the specification nor in the tests. |
| S | Volba vhodné tabulky a diagramu, vytvoření diagramu z dat | postup |  |  |  |  |  |  | C1, 2: „zvolí vhodnou tabulku a vhodný diagram“; B1, 2: „vytvoří vhodný diagram ze vstupních dat“. Charts are always given, never drawn. |

### Aritmetický průměr

`DAT.PRUM` · 1,1 points per standard test, in 7 of 16 · success 42 % · specification area 2

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 2 | Výpočet aritmetického průměru | postup |  | 4 · 3 | 0,5 | 7 · 5 · 1,1 | 45 % | [2026 A 1.3](../backend/data/screenshots/M9-2026-A-01.png) 37 % · [2022 B 7.1](../backend/data/screenshots/M9-2022-B-07.png) 49 % |  |
| 3 | Průměr z tabulky četností | postup | Výpočet aritmetického průměru (DAT.PRUM) | 3 · 2 | 0,3 |  | 35 % | [2025 A 14](../backend/data/screenshots/M9-2025-A-14.png) 36 % | Count × value, divided by the total count. |
| 3 | Chybějící hodnota z daného průměru | postup | Výpočet aritmetického průměru (DAT.PRUM) | 3 · 2 | 0,4 |  | 43 % | [2022 B 7.2](../backend/data/screenshots/M9-2022-B-07.png) 51 % |  |

## Geometrie: výpočty (GEO)

9,9 points per standard test · success 38 % · No formula except the circle's is printed. Tasks are chains: a figure, a hidden right triangle, a unit change.

### Úhly

`GEO.UHLY` · 2,1 points per standard test, in 14 of 16 · success 51 % · specification area 3 · One multiple-choice item among 12–14 in most tests. Straight chains score 50–67 %, figures needing an auxiliary idea 21–24 %.

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Vrcholové, vedlejší, souhlasné a střídavé úhly | znalost |  | 10 · 3 | 1,3 | 10 · 3 · 1,3 | 54 % | [2025 A 7.3](../backend/data/screenshots/M9-2025-A-07.png) 40 % · [2022 B 13](../backend/data/screenshots/M9-2022-B-13.png) 54 % · [2025 A 7.1](../backend/data/screenshots/M9-2025-A-07.png) 65 % |  |
| 1 | Součet úhlů v trojúhelníku a čtyřúhelníku | znalost |  | 9 · 4 | 1,2 | 14 · 6 · 2,0 | 53 % | [2026 A 8.2](../backend/data/screenshots/M9-2026-A-08.png) 31 % · [2025 A 7.3](../backend/data/screenshots/M9-2025-A-07.png) 40 % · [2026 A 8.1](../backend/data/screenshots/M9-2026-A-08.png) 42 % |  |
| 2 | Úhly v rovnoramenném a rovnostranném trojúhelníku | znalost | Součet úhlů v trojúhelníku a čtyřúhelníku (GEO.UHLY) | 5 · 2 | 0,8 | 7 · 4 · 1,1 | 46 % | [2023 B 12](../backend/data/screenshots/M9-2023-B-12.png) 40 % · [2025 B 12](../backend/data/screenshots/M9-2025-B-12.png) 51 % |  |
| 2 | Úhly zapsané jako α, 2α, 3α nebo poměrem | rozbor | Vrcholové (GEO.UHLY), Součet úhlů v trojúhelníku a čtyřúhelníku (GEO.UHLY) | 4 · 0 | 0,5 |  | 46 % | [2023 A 14](../backend/data/screenshots/M9-2023-A-14.png) 42 % · [2022 A 12](../backend/data/screenshots/M9-2022-A-12.png) 50 % | Set up an equation for α. |
| 3 | Osa úhlu | znalost | Součet úhlů v trojúhelníku a čtyřúhelníku (GEO.UHLY) | 2 · 2 | 0,2 |  | 31 % | [2026 A 8.2](../backend/data/screenshots/M9-2026-A-08.png) 31 % |  |
| 3 | Pravidelný mnohoúhelník | znalost | Úhly v rovnoramenném a rovnostranném trojúhelníku (GEO.UHLY) | 1 · 1 | 0,2 |  | – |  | Regular pentagon 108°; hexagon as six equilateral triangles. |
| 3 | Úhly v kružnici: poloměry a Thaletova věta | znalost | Úhly v rovnoramenném a rovnostranném trojúhelníku (GEO.UHLY) | 2 · 2 | 0,4 |  | 42 % | [2026 A 8.1](../backend/data/screenshots/M9-2026-A-08.png) 42 % |  |

### Pythagorova věta

`GEO.PYT` · 1,6 points per standard test, in 11 of 16 · success 37 % · specification area 3 · Never asked for by name; always a hidden step. Sides are whole numbers in the tasks traced.

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Přepona z odvěsen, odvěsna z přepony | postup | Druhá mocnina a odmocnina (POC.VYR) | 3 · 1 | 0,3 | 11 · 4 · 1,6 | 48 % | [2024 B 2](../backend/data/screenshots/M9-2024-B-02.png) 34 % · [2023 B 11.2](../backend/data/screenshots/M9-2023-B-11.png) 69 % | Know the triples 3–4–5, 5–12–13, 8–15–17 and their multiples. |
| 2 | Nalezení pravoúhlého trojúhelníku v útvaru | rozbor | Přepona z odvěsen (GEO.PYT) | 4 · 4 | 0,5 | 9 · 4 · 1,4 | 35 % | [2024 A 6.1](../backend/data/screenshots/M9-2024-A-06.png) 27 % · [2026 A 13](../backend/data/screenshots/M9-2026-A-13.png) 34 % · [2024 B 6.1](../backend/data/screenshots/M9-2024-B-06.png) 40 % | Height of an isosceles triangle or trapezoid, slanted side, diagonal. |
| 2 | Pythagorova věta v tělesech | rozbor | Nalezení pravoúhlého trojúhelníku v útvaru (GEO.PYT) | 5 · 0 | 0,9 |  | 33 % | [2023 A 12](../backend/data/screenshots/M9-2023-A-12.png) 39 % | Stěnová úhlopříčka; hypotenuse of the base as an edge. |

### Obvod a obsah rovinných útvarů

`GEO.ROV` · 3,7 points per standard test, in 15 of 16 · success 31 % · specification area 3 · A result-only task among 6–8; 22 % leave it blank. A direct area from given sides does not occur alone.

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Vzorce pro obvod a obsah | znalost |  | 8 · 6 | 1,1 | 16 · 8 · 5,4 | 30 % | [2023 A 8.3](../backend/data/screenshots/M9-2023-A-08.png) 17 % · [2023 A 6.1](../backend/data/screenshots/M9-2023-A-06.png) 22 % · [2023 A 6.2](../backend/data/screenshots/M9-2023-A-06.png) 29 % | Čtverec, obdélník, trojúhelník, rovnoběžník, kosočtverec, lichoběžník. None is printed. |
| 1 | Strana nebo výška z obsahu | postup | Vzorce pro obvod a obsah (GEO.ROV), Druhá mocnina a odmocnina (POC.VYR) | 7 · 2 | 1,0 | 12 · 6 · 2,6 | 36 % | [2022 A 2.1](../backend/data/screenshots/M9-2022-A-02.png) 28 % · [2025 A 5.1](../backend/data/screenshots/M9-2025-A-05.png) 47 % |  |
| 3 | Obsah vypočtený dvěma způsoby | rozbor | Strana nebo výška z obsahu (GEO.ROV) | 1 · 0 | 0,1 |  | 39 % | [2023 B 11.3](../backend/data/screenshots/M9-2023-B-11.png) 39 % | Height to the hypotenuse, height of a rhombus. |
| 3 | Lichoběžník rozdělený na obdélník a trojúhelník | rozbor | Vzorce pro obvod a obsah (GEO.ROV), Nalezení pravoúhlého trojúhelníku v útvaru (GEO.PYT) | 2 · 2 | 0,2 |  | 37 % | [2024 A 6.2](../backend/data/screenshots/M9-2024-A-06.png) 27 % · [2024 B 6.2](../backend/data/screenshots/M9-2024-B-06.png) 42 % · [2025 B 8.2](../backend/data/screenshots/M9-2025-B-08.png) 42 % |  |
| 2 | Složené útvary | rozbor | Vzorce pro obvod a obsah (GEO.ROV) | 8 · 4 | 0,9 | 8 · 4 · 0,9 | 38 % | [2022 B 8](../backend/data/screenshots/M9-2022-B-08.png) 37 % · [2024 A 12](../backend/data/screenshots/M9-2024-A-12.png) 43 % · [2023 B 11.1](../backend/data/screenshots/M9-2023-B-11.png) 71 % |  |
| 2 | Obvod vyjádřený proměnnou | rozbor | Vzorce pro obvod a obsah (GEO.ROV), Sestavení a vyřešení rovnice z další podmínky (VZT.SLOV) | 6 · 4 | 0,8 |  | 24 % | [2025 B 8.3](../backend/data/screenshots/M9-2025-B-08.png) 5 % · [2023 A 8.2](../backend/data/screenshots/M9-2023-A-08.png) 27 % · [2024 A 13](../backend/data/screenshots/M9-2024-A-13.png) 31 % |  |
| 3 | Trojúhelníková nerovnost | znalost |  | 1 · 1 | 0,1 |  | 11 % | [2026 B 8.1](../backend/data/screenshots/M9-2026-B-08.png) 11 % · [2026 B 8.2](../backend/data/screenshots/M9-2026-B-08.png) 12 % | Once in 20 tests. |
| 3 | Rozestupy po obvodu | rozbor |  | 1 · 1 | 0,2 |  | 13 % | [2025 A 8.2](../backend/data/screenshots/M9-2025-A-08.png) 14 % · [2025 A 8.1](../backend/data/screenshots/M9-2025-A-08.png) 24 % | Once in 20 tests. |
| S | Obvod a obsah mnohoúhelníku ve čtvercové síti | postup |  |  |  |  |  |  | B1, 3: „využívá čtvercovou síť pro výpočet obvodu a obsahu mnohoúhelníků“. |
| S | Shodnost trojúhelníků | znalost |  |  |  |  |  |  | B1, 3: „používá věty o shodnosti trojúhelníků k řešení geometrických úloh“. |
| S | Podobnost trojúhelníků: věty sss, sus, uu, poměr podobnosti | znalost |  |  |  |  |  |  | C1, 3: „pomocí poměru podobnosti určí rozměry trojúhelníků“. **Before 2022: 2021 B 8.1, 2021 B 8.3.** |

### Kruh a kružnice

`GEO.KRUH` · 0,6 points per standard test, in 5 of 16 · success 37 % · specification area 3 · o = 2πr and S = πr² are printed. Radii are round (5, 10, 50).

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Obvod a obsah kruhu, počítání s π ≐ 3,14, zaokrouhlení | postup | Počítání s desetinnými čísly bez kalkulačky (POC.VYR) | 2 · 1 | 0,2 | 11 · 5 · 1,6 | 56 % | [2022 B 12](../backend/data/screenshots/M9-2022-B-12.png) 56 % · [2024 B 14](../backend/data/screenshots/M9-2024-B-14.png) 56 % | Do not confuse poloměr and průměr; round only the final result. |
| 3 | Poloměr nebo průměr z obsahu | postup | Obvod a obsah kruhu (GEO.KRUH), Druhá mocnina a odmocnina (POC.VYR) | 1 · 0 | 0,1 |  | 36 % | [2023 B 8.1](../backend/data/screenshots/M9-2023-B-08.png) 36 % |  |
| 3 | Půlkruh, čtvrtkruh, výseč: obsah a obvod | postup | Obvod a obsah kruhu (GEO.KRUH) | 2 · 1 | 0,3 | 2 · 1 · 0,3 | 36 % | [2026 B 7.2](../backend/data/screenshots/M9-2026-B-07.png) 19 % · [2022 A 13](../backend/data/screenshots/M9-2022-A-13.png) 40 % · [2026 B 7.1](../backend/data/screenshots/M9-2026-B-07.png) 54 % | Perimeter of a part = arc + the straight sides. |
| 3 | Útvary ohraničené oblouky | rozbor | Půlkruh (GEO.KRUH), Složené útvary (GEO.ROV) | 0 · 0 | 0,0 |  | 22 % | [2024 A 8.2](../backend/data/screenshots/M9-2024-A-08.png) 21 % · [2024 A 8.1](../backend/data/screenshots/M9-2024-A-08.png) 24 % |  |
| S | Vzájemná poloha kružnice a přímky: tečna, sečna, vnější přímka | znalost |  |  |  |  |  |  | C1, 3. |
| S | Vzájemná poloha dvou kružnic, průsečíky a body dotyku | znalost |  |  |  |  |  |  | C1, 3. |

### Tělesa

`GEO.TEL` · 3,9 points per standard test, in 16 of 16 · success 38 % · specification area 3 · In every standard test, mostly multiple choice 12–14. Several multi-step items score at the guessing rate.

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Krychle a kvádr: objem, povrch, součet hran, i zpětně | postup | Strana nebo výška z obsahu (GEO.ROV) | 7 · 6 | 0,9 | 10 · 6 · 1,7 | 46 % | [2025 A 11.1](../backend/data/screenshots/M9-2025-A-11.png) 70 % |  |
| 1 | Kolmý hranol: objem a povrch | postup | Vzorce pro obvod a obsah (GEO.ROV) | 9 · 4 | 1,2 | 12 · 5 · 2,0 | 33 % | [2025 A 12](../backend/data/screenshots/M9-2025-A-12.png) 24 % · [2022 A 6](../backend/data/screenshots/M9-2022-A-06.png) 30 % · [2023 B 13](../backend/data/screenshots/M9-2023-B-13.png) 45 % | V = obsah podstavy × výška, for a triangular, rhombic or trapezoidal base. |
| 2 | Válec: objem, plášť, povrch | postup | Obvod a obsah kruhu (GEO.KRUH) | 6 · 1 | 0,8 | 8 · 3 · 1,2 | 31 % | [2024 A 2](../backend/data/screenshots/M9-2024-A-02.png) 16 % · [2023 B 8.2](../backend/data/screenshots/M9-2023-B-08.png) 18 % · [2025 B 14](../backend/data/screenshots/M9-2025-B-14.png) 35 % | The plášť unrolled is a rectangle. |
| 3 | Síť tělesa | znalost | Kolmý hranol (GEO.TEL) | 2 · 1 | 0,4 |  | 49 % | [2022 B 11.1](../backend/data/screenshots/M9-2022-B-11.png) 44 % · [2022 B 11.2](../backend/data/screenshots/M9-2022-B-11.png) 47 % · [2022 B 11.3](../backend/data/screenshots/M9-2022-B-11.png) 57 % |  |
| 2 | Slepená a rozříznutá tělesa | rozbor | Krychle a kvádr (GEO.TEL), Kolmý hranol (GEO.TEL) | 7 · 3 | 1,2 |  | 37 % | [2026 B 13](../backend/data/screenshots/M9-2026-B-13.png) 22 % · [2022 B 11.1](../backend/data/screenshots/M9-2022-B-11.png) 44 % · [2025 A 11.2](../backend/data/screenshots/M9-2025-A-11.png) 44 % | The surface changes by the faces that disappear or appear. |
| 3 | Tělesa z krychliček, prostorová představivost | rozbor |  | 2 · 2 | 0,5 |  | 48 % | [2025 B 13](../backend/data/screenshots/M9-2025-B-13.png) 25 % |  |
| 3 | Vztah místo čísla: rovnice pro výšku nebo hranu | rozbor | Válec (GEO.TEL), Rovnice se závorkami a desetinnými čísly (ALG.ROV) | 3 · 1 | 0,4 |  | 31 % | [2023 A 13](../backend/data/screenshots/M9-2023-A-13.png) 30 % · [2026 A 14](../backend/data/screenshots/M9-2026-A-14.png) 33 % | „obsah pláště je třikrát větší než obsah podstavy“. |
| 3 | Objem v litrech, výška hladiny | postup | Válec (GEO.TEL), Objem a litry (krok × 1 000 (POC.JED) | 1 · 1 | 0,1 |  | 18 % | [2025 A 6.2](../backend/data/screenshots/M9-2025-A-06.png) 17 % · [2025 A 6.1](../backend/data/screenshots/M9-2025-A-06.png) 20 % |  |
| S | Pohled na těleso shora, zepředu, zprava, zleva a zdola | rozbor |  |  |  |  |  |  | B1, 3. |
| S | Náčrt sítě a obrazu tělesa ve volném rovnoběžném promítání | postup |  |  |  |  |  |  | B1, 3: „načrtne a sestrojí síť krychle, kvádru a kolmého hranolu“; C1, 3: „načrtne síť válce“. Nets are always given, never drawn. |
| S | Jehlan: rozpoznání, síť, pohledy, metrické a polohové vlastnosti | znalost |  |  |  |  |  |  | C1, 3. The specification does not ask for the volume or surface of a pyramid. |
| S | Koule: poloměr a průměr ve slovních úlohách | znalost |  |  |  |  |  |  | C1, 3: „řeší aplikační slovní úlohy s využitím znalostí o válci a kouli (poloměr a průměr koule)“. No volume or surface. |

## Geometrie: konstrukce (KON)

5,8 points per standard test · success 32 % · Tasks 9 and 10 in every test, 5–6 points, 32 % success and 28 % blank. Learned as three layers: the moves, the properties, the reading of the task.

### Základní konstrukce

`KON.ZAKL` · 5,3 points per standard test, in 16 of 16 · success 32 % · specification area 3 · The moves with ruler, set square and compass. Each must be automatic.

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Kolmice a rovnoběžka daným bodem | postup |  | 10 · 5 | 2,5 | 16 · 8 · 5,2 | 37 % | [2026 A 9](../backend/data/screenshots/M9-2026-A-09.png) 42 % |  |
| 1 | Střed a osa úsečky | postup | Kolmice a rovnoběžka daným bodem (KON.ZAKL) | 8 · 4 | 1,8 | 16 · 8 · 5,1 | 27 % | [2025 B 10](../backend/data/screenshots/M9-2025-B-10.png) 9 % · [2025 B 9](../backend/data/screenshots/M9-2025-B-09.png) 19 % · [2023 A 10](../backend/data/screenshots/M9-2023-A-10.png) 22 % |  |
| 3 | Osa úhlu | postup |  | 1 · 1 | 0,2 |  | 33 % | [2025 A 9](../backend/data/screenshots/M9-2025-A-09.png) 33 % |  |
| 1 | Přenesení délky kružnicí | postup |  | 11 · 6 | 2,6 | 16 · 8 · 4,9 | 31 % | [2025 B 10](../backend/data/screenshots/M9-2025-B-10.png) 9 % · [2026 B 9](../backend/data/screenshots/M9-2026-B-09.png) 15 % · [2025 B 9](../backend/data/screenshots/M9-2025-B-09.png) 19 % |  |
| 3 | Úhel dané velikosti | postup |  | 2 · 0 | 0,2 |  | 31 % | [2024 A 9](../backend/data/screenshots/M9-2024-A-09.png) 31 % | 120° and 40° with a protractor; 60° and 90° without. |
| 1 | Thaletova kružnice nad úsečkou | postup | Střed a osa úsečky (KON.ZAKL) | 5 · 3 | 0,9 | 15 · 8 · 4,0 | 32 % | [2026 B 10](../backend/data/screenshots/M9-2026-B-10.png) 22 % · [2023 A 9](../backend/data/screenshots/M9-2023-A-09.png) 32 % · [2023 B 10](../backend/data/screenshots/M9-2023-B-10.png) 43 % | Never named in the task; named in the official keys. |
| 1 | Obraz bodu ve středové souměrnosti („S je střed“) | postup | Přenesení délky kružnicí (KON.ZAKL) | 9 · 6 | 1,8 | 16 · 8 · 4,4 | 33 % | [2025 B 10](../backend/data/screenshots/M9-2025-B-10.png) 9 % · [2025 A 10](../backend/data/screenshots/M9-2025-A-10.png) 28 % · [2022 A 9](../backend/data/screenshots/M9-2022-A-09.png) 31 % |  |
| 2 | Obraz v osové souměrnosti, osa z bodu a jeho obrazu | postup | Střed a osa úsečky (KON.ZAKL) | 6 · 3 | 0,9 |  | 34 % | [2026 B 9](../backend/data/screenshots/M9-2026-B-09.png) 15 % · [2026 A 10](../backend/data/screenshots/M9-2026-A-10.png) 23 % · [2023 B 9](../backend/data/screenshots/M9-2023-B-09.png) 64 % |  |
| S | Přenesení úhlu | postup |  |  |  |  |  |  | B1, 3: „přenese úhel, porovná dva úhly“. |
| S | Kružnice opsaná trojúhelníku | postup |  |  |  |  |  |  | C1, 3. Its centre is used in 2026 A 8 and 2026 C 10, but it is never constructed. |
| S | Tečna kružnice v jejím bodě | postup |  |  |  |  |  |  | C1, 3. |

### Vlastnosti útvarů, o které se konstrukce opírá

`KON.VLAST` · 4,9 points per standard test, in 16 of 16 · success 31 % · specification area 3 · The task never says which property to use; the student must recall it from the name of the figure.

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Rovnoramenný trojúhelník: osa souměrnosti je osou základny | znalost | Střed a osa úsečky (KON.ZAKL) | 8 · 3 | 1,4 | 16 · 8 · 3,9 | 34 % | [2025 B 9](../backend/data/screenshots/M9-2025-B-09.png) 19 % · [2023 A 10](../backend/data/screenshots/M9-2023-A-10.png) 22 % · [2022 A 9](../backend/data/screenshots/M9-2022-A-09.png) 31 % |  |
| 3 | Rovnostranný trojúhelník | znalost | Přenesení délky kružnicí (KON.ZAKL) | 1 · 1 | 0,1 |  | 31 % | [2024 A 9](../backend/data/screenshots/M9-2024-A-09.png) 31 % |  |
| 2 | Pravoúhlý trojúhelník: kolmé odvěsny, vrchol pravého úhlu na Thaletově kružnici | znalost | Kolmice a rovnoběžka daným bodem (KON.ZAKL), Thaletova kružnice nad úsečkou (KON.ZAKL) | 4 · 2 | 0,7 |  | 32 % | [2026 B 10](../backend/data/screenshots/M9-2026-B-10.png) 22 % · [2023 B 10](../backend/data/screenshots/M9-2023-B-10.png) 43 % |  |
| 2 | Výška a těžnice | znalost | Kolmice a rovnoběžka daným bodem (KON.ZAKL), Střed a osa úsečky (KON.ZAKL) | 4 · 3 | 0,7 |  | 23 % | [2025 A 10](../backend/data/screenshots/M9-2025-A-10.png) 28 % |  |
| 3 | Čtverec: shodné, kolmé, půlící se úhlopříčky | znalost | Kolmice a rovnoběžka daným bodem (KON.ZAKL) | 2 · 0 | 0,3 |  | 51 % | [2022 A 10](../backend/data/screenshots/M9-2022-A-10.png) 51 % |  |
| 1 | Obdélník: pravé úhly, shodné půlící se úhlopříčky, vrcholy na kružnici | znalost | Thaletova kružnice nad úsečkou (KON.ZAKL) | 6 · 4 | 0,9 | 15 · 8 · 4,0 | 30 % | [2024 A 10](../backend/data/screenshots/M9-2024-A-10.png) 26 % · [2023 A 9](../backend/data/screenshots/M9-2023-A-09.png) 32 % |  |
| 1 | Rovnoběžník: úhlopříčky se půlí, střed souměrnosti | znalost | Obraz bodu ve středové souměrnosti („S je střed“) (KON.ZAKL) | 4 · 2 | 0,7 | 16 · 8 · 3,9 | 18 % | [2025 B 10](../backend/data/screenshots/M9-2025-B-10.png) 9 % · [2022 B 10](../backend/data/screenshots/M9-2022-B-10.png) 26 % |  |
| 3 | Kosočtverec: kolmé úhlopříčky, osa souměrnosti | znalost | Rovnoběžník (KON.VLAST) | 1 · 1 | 0,1 |  | 29 % | [2026 A 10](../backend/data/screenshots/M9-2026-A-10.png) 23 % · [2024 B 9](../backend/data/screenshots/M9-2024-B-09.png) 32 % | 2026 A 10 never says „kosočtverec“; 53 % left it blank. |
| 3 | Lichoběžník: rovnoramenný a pravoúhlý | znalost | Kolmice a rovnoběžka daným bodem (KON.ZAKL) | 3 · 1 | 0,5 |  | 64 % | [2023 B 9](../backend/data/screenshots/M9-2023-B-09.png) 64 % |  |
| 3 | Pravidelný šestiúhelník: strana = poloměr kružnice opsané | znalost | Přenesení délky kružnicí (KON.ZAKL) | 1 · 1 | 0,1 |  | 15 % | [2026 B 9](../backend/data/screenshots/M9-2026-B-09.png) 15 % | Once in 20 tests. |
| S | Pravidelný osmiúhelník | znalost |  |  |  |  |  |  | B1, 3: „sestrojí pravidelný šestiúhelník a osmiúhelník“. |

### Rozbor zadání

`KON.ROZBOR` · 3,6 points per standard test, in 15 of 16 · success 28 % · specification area 3 · Where the tasks are actually lost: the second construction is the most skipped regular task.

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Náčrt a převod nepřímé podmínky na množinu bodů | rozbor | Rovnoramenný trojúhelník (KON.VLAST), Obdélník (KON.VLAST), Rovnoběžník (KON.VLAST) | 13 · 6 | 2,8 | 15 · 8 · 3,6 | 26 % | [2025 B 10](../backend/data/screenshots/M9-2025-B-10.png) 9 % · [2025 B 9](../backend/data/screenshots/M9-2025-B-09.png) 19 % · [2026 B 10](../backend/data/screenshots/M9-2026-B-10.png) 22 % | „Přímka o je osou některé strany“, „Bod M leží na úhlopříčce BD“. |
| 1 | „Najděte všechna řešení“: druhé řešení | rozbor | Náčrt a převod nepřímé podmínky na množinu bodů (KON.ROZBOR) | 13 · 6 | 2,8 |  | 32 % | [2025 B 9](../backend/data/screenshots/M9-2025-B-09.png) 19 % · [2023 A 10](../backend/data/screenshots/M9-2023-A-10.png) 22 % · [2022 A 9](../backend/data/screenshots/M9-2022-A-09.png) 31 % | 18 of 40 construction tasks; then exactly two figures. One of two costs a point. |
| S | Trojúhelník a čtyřúhelník ze zadaných údajů (sss, sus, usu) | postup |  |  |  |  |  |  | B1, 3. Not asked as a plain task. |

### Souměrnost útvarů

`KON.SOUM` · 0,5 points per standard test, in 2 of 16 · success – · specification area 3 · A task of its own in 4 of 16 standard tests; otherwise a tool inside constructions.

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 3 | Osy souměrnosti útvaru ve čtvercové síti a mnohoúhelníků | znalost |  | 2 · 0 | 0,5 |  | – |  |  |
| S | Samodružný bod a útvar; vzor a obraz | znalost |  |  |  |  |  |  | B1, 3. |
| S | Obraz celého útvaru ve středové souměrnosti | postup |  |  |  |  |  |  | B1, 3: „sestrojí obraz rovinného útvaru ve středové souměrnosti“. Only single points are reflected in the tests. |

## Zákonitosti a úsudek (ZAK)

4,2 points per standard test · success 12 % · Task 16: 4 points, 10 % success, 36 % blank. No curriculum of its own; it is a way of working.

### Rostoucí obrazce a číselné řady

`ZAK.RADA` · 3,0 points per standard test, in 12 of 16 · success 10 % · specification area 4

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Pokračování pravidla a tabulka počtů po krocích | rozbor |  | 6 · 4 | 0,4 | 12 · 5 · 3,0 | 23 % | [2023 B 16.1](../backend/data/screenshots/M9-2023-B-16.png) 11 % · [2025 A 16.1](../backend/data/screenshots/M9-2025-A-16.png) 12 % · [2026 B 16.1](../backend/data/screenshots/M9-2026-B-16.png) 14 % | Enough for 16.1, solved by 11–42 %. The cheapest point of task 16. |
| 1 | Obecný n-tý člen (lineární růst, n², n·(n + 1)/2) | rozbor | Pokračování pravidla a tabulka počtů po krocích (ZAK.RADA), Vyjádření veličiny výrazem s proměnnou (VZT.SLOV) | 9 · 4 | 1,4 | 10 · 4 · 2,0 | 5 % | [2025 A 16.3](../backend/data/screenshots/M9-2025-A-16.png) 1 % · [2026 B 16.3](../backend/data/screenshots/M9-2026-B-16.png) 2 % · [2022 B 16.3](../backend/data/screenshots/M9-2022-B-16.png) 3 % | Use the differences between consecutive steps. Needed for 16.3, solved by 1–3 %. |
| 2 | Obrácení pravidla: který krok má daný počet | rozbor | Obecný n-tý člen (lineární růst (ZAK.RADA), Druhá mocnina a odmocnina (POC.VYR) | 9 · 3 | 1,0 |  | 7 % | [2023 B 16.3](../backend/data/screenshots/M9-2023-B-16.png) 2 % · [2026 B 16.2](../backend/data/screenshots/M9-2026-B-16.png) 7 % · [2022 B 16.2](../backend/data/screenshots/M9-2022-B-16.png) 12 % | 361 = 19², so the 20th figure. |
| 3 | Růst násobením (mocniny tří) | rozbor | Pokračování pravidla a tabulka počtů po krocích (ZAK.RADA) | 1 · 0 | 0,2 |  | 5 % | [2023 A 16.3](../backend/data/screenshots/M9-2023-A-16.png) 2 % · [2023 A 16.2](../backend/data/screenshots/M9-2023-A-16.png) 2 % · [2023 A 16.1](../backend/data/screenshots/M9-2023-A-16.png) 15 % | Once in 20 tests. |
| 3 | Číselná řada daná pravidlem | rozbor | Pokračování pravidla a tabulka počtů po krocích (ZAK.RADA) | 2 · 1 | 0,5 |  | 12 % | [2025 B 16.2](../backend/data/screenshots/M9-2025-B-16.png) 1 % · [2025 B 16.3](../backend/data/screenshots/M9-2025-B-16.png) 2 % · [2025 B 16.1](../backend/data/screenshots/M9-2025-B-16.png) 42 % |  |

### Úsudek a systematické hledání

`ZAK.USUDEK` · 1,3 points per standard test, in 5 of 16 · success 14 % · specification area 4

| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |
|---|---|---|---|---|---|---|---|---|---|
| 3 | Periodické děje: cykly a společný násobek | rozbor | Společný násobek (POC.DEL) | 2 · 1 | 0,5 |  | 16 % | [2026 A 16.3](../backend/data/screenshots/M9-2026-A-16.png) 1 % · [2026 A 16.2](../backend/data/screenshots/M9-2026-A-16.png) 10 % · [2022 A 16.3](../backend/data/screenshots/M9-2022-A-16.png) 11 % |  |
| 3 | Systematické vypsání všech řešení | rozbor |  | 3 · 2 | 0,4 |  | 2 % | [2023 B 16.3](../backend/data/screenshots/M9-2023-B-16.png) 2 % |  |
| 3 | Strategické a netradiční geometrické úlohy | rozbor |  | 2 · 2 | 0,5 |  | – |  |  |
