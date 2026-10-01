# Strom učiva M9: what the test examines, as a tree in learning order

Generated from `analysis/data/m9_topic_tree.json`; change the tree with `analysis/topic_tree.py`, not here.
It reorganizes the findings of [03_ucivo_M9.md](03_ucivo_M9.md) (20 tests, 2022–2026) into a tree of
7 areas, 24 topics and 140 skills. Nothing here was read anew from the booklets: every skill
and every example task comes from that file or the task catalog, and the specification column from
`References/MASPECIFIKACEPOZADAVKU2022 (1).pdf`, part C1 (its four areas are 1 Číslo a proměnná,
2 Závislosti, vztahy a práce s daty, 3 Geometrie v rovině a prostoru, 4 Nestandardní aplikační úlohy a problémy).

## How the tree is cut

The grouping, the priorities and the prerequisite links are my judgement, not CERMAT's.

- **A leaf is one thing a student can practise in one sitting** and recognise in a task: „složený zlomek“,
  „základ po změně“, „Thaletova kružnice“. Areas and topics only group leaves.
- **Order is learning order.** Areas, topics and leaves are listed so that everything a leaf needs comes
  earlier; the *needs* column names the direct prerequisites (the script checks this).
- **Computing and reading are separated.** Computing with fractions scores 58–76 %, a fraction word problem
  21–33 %; they are different skills, so the first is in POC and the second in VZT. The phrases
  „o třetinu více než“, „kolikrát“, „o kolik procent“ recur in fractions, percentages and equation word
  problems, so they are one topic (VZT.NEZ) learned once instead of three times.
- **Constructions are three layers**: the moves, the properties of figures, and the reading of the task.
- **Tools used everywhere stay single leaves** (druhá mocnina, převody jednotek, Pythagorova věta) and are
  pulled in through *needs* rather than repeated under each topic.
- Not in the tree: the rules for how answers must look and the list of what is not printed in the booklet
  (03, section 0). They apply to every leaf.

**Priority** (column P), by how often a skill is needed in the 20 tests:
**1** in every or nearly every test, usually in a fixed slot (45 leaves) ·
**2** recurring (50) · **3** seen once to three times, or decides only the top score (33) ·
**S** in the specification, not seen in these tests (12).

**Kind** says how the skill is practised: *postup* – a procedure, drilled until fast and error-free ·
*překlad* – turning the Czech wording into mathematics · *znalost* – a fact or property known by heart ·
*rozbor* – finding the route through a multi-step task.

Percentages after an example are CERMAT's success rate for that task or sub-item (terms C and D were sat
by a few hundred candidates, so theirs are noisy; 2024 C and D have none). Points per test and success per
topic are in the contents table of 03 under the tag shown with each topic. They cannot be given per leaf
yet, because the catalog tags whole tasks; that needs every sub-item assigned to a leaf.

## The tree at a glance

```
POC  Počítání s čísly
├─ Číselné výrazy, mocniny, odmocniny
│    2  Pořadí operací, závorky, záporná čísla
│    2  Počítání s desetinnými čísly bez kalkulačky
│    1  Druhá mocnina a odmocnina
│    2  Výraz zadaný slovy (součet, rozdíl, součin, podíl)
│    3  Číselná osa se stejnými dílky
│    S  Absolutní hodnota, opačné číslo, periodické číslo, zaokrouhlování, odhady
├─ Počítání se zlomky
│    1  Čtyři operace se zlomky, společný jmenovatel, krácení, základní tvar
│    1  Složený zlomek
│    2  Zlomky spolu s desetinnými čísly
│    2  Zlomky s druhou mocninou a odmocninou
│    3  Smíšené číslo
│    S  Porovnávání zlomků, převrácený zlomek, zlomek jako periodické číslo
├─ Dělitelnost
│    3  Dělitelé a násobky čísla
│    3  Prvočísla a rozklad na prvočísla
│    3  Dělení se zbytkem ve slovní úloze
│    2  Společný násobek
│    S  Znaky dělitelnosti, nejmenší společný násobek a největší společný dělitel podle názvu
└─ Převody jednotek
     2  Délka (mm, cm, dm, m, km)
     2  Obsah (krok × 100)
     2  Objem a litry (krok × 1 000, 1 l = 1 dm³)
     3  Hmotnost (g, kg)
     2  Čas (hodiny, minuty, desetinné hodiny, sčítání časů)
     S  Sekunda a týden jako převáděné jednotky

ALG  Výrazy a rovnice
├─ Úpravy výrazů
│    1  Roznásobení závorek a sloučení členů
│    1  Vytýkání
│    1  Umocnění dvojčlenu (a ± b)²
│    2  Vzorec (a ± b)² zpětně – doplnění chybějících čísel
│    1  Rozklad a² − b² na součin
│    3  Hodnota výrazu pro dané číslo
└─ Lineární rovnice a soustavy
     1  Rovnice se závorkami a desetinnými čísly
     1  Rovnice se zlomky
     2  Rovnice bez řešení
     3  Rovnice s druhými mocninami dvojčlenů, ve které x² vypadne
     2  Soustava dvou rovnic se dvěma neznámými

VZT  Vztahy mezi veličinami: zlomek, procento, poměr
├─ Zlomek jako část celku
│    2  Zlomek z množství a z času
│    2  Část ze zbytku
│    1  Celek z části
├─ Srovnání „o … více než“, „kolikrát“
│    1  „o kolik“ je rozdíl, „kolikrát“ je podíl
│    1  „o třetinu více / méně než“ jako násobení
│    2  „dvakrát méně“, „čtyřikrát menší než“ jako dělení
│    1  Obrácení vztahu: neznámá není veličina za „než“
├─ Procenta
│    1  Procentová část, počet procent, základ
│    1  „o x % více / méně“ jako násobitel
│    1  Základ po změně („což je o 40 % více než loni“)
│    1  „O kolik procent“ se liší dvě veličiny
│    2  Obrácené srovnání („o třetinu méně“ je opačně „o 50 % více“)
│    2  Dvě změny po sobě
│    2  Procento ze zbytku
│    2  Dvě veličiny svázané procentem a známý součet
│    1  Procento, zlomek a poměr: převody mezi nimi
│    3  Změna v procentních bodech
│    3  Úrok za jeden rok a daň z úroku
│    S  Promile; jistina, úroková míra, úrokovací období, inflace, půjčky a úvěry
├─ Poměr a úměrnost
│    2  Poměr v základním tvaru, dělení v poměru
│    3  Poměr na číselné ose a na úsečce
│    2  Měřítko mapy a plánu
│    2  Přímá úměrnost
│    2  Nepřímá úměrnost
│    2  Společná práce
│    2  Pohyb: s = v · t
│    3  Směsi a průměrná cena
│    S  Postupný a převrácený poměr; graf a rovnice přímé a nepřímé úměrnosti; bod v pravoúhlé soustavě souřadnic
└─ Slovní úlohy na rovnici
     1  Vyjádření veličiny výrazem s proměnnou
     1  Sestavení a vyřešení rovnice z další podmínky
     2  Dvě neznámé: počty a součty
     2  Řešení úsudkem bez rovnice
     3  Podmínka, že výsledek je celé číslo

DAT  Grafy, tabulky, průměr
├─ Grafy a tabulky
│    1  Čtení sloupcového grafu (více řad, skládaný)
│    1  Doplnění chybějícího údaje z podmínek v textu
│    2  Kruhový diagram (procenta, středové úhly)
│    3  Čtení tabulky, třídění údajů z textu
│    S  Statistický soubor, statistický znak, četnost; volba vhodného grafu
└─ Aritmetický průměr
     2  Výpočet aritmetického průměru
     3  Průměr z tabulky četností
     3  Chybějící hodnota z daného průměru

GEO  Geometrie: výpočty
├─ Úhly
│    1  Vrcholové, vedlejší, souhlasné a střídavé úhly
│    1  Součet úhlů v trojúhelníku a čtyřúhelníku
│    1  Úhly v rovnoramenném a rovnostranném trojúhelníku
│    2  Úhly zapsané jako α, 2α, 3α nebo poměrem
│    3  Osa úhlu
│    3  Pravidelný mnohoúhelník
│    3  Úhly v kružnici: poloměry a Thaletova věta
├─ Pythagorova věta
│    1  Přepona z odvěsen, odvěsna z přepony
│    1  Nalezení pravoúhlého trojúhelníku v útvaru
│    2  Pythagorova věta v tělesech
├─ Obvod a obsah rovinných útvarů
│    1  Vzorce pro obvod a obsah
│    1  Strana nebo výška z obsahu
│    3  Obsah vypočtený dvěma způsoby
│    2  Lichoběžník rozdělený na obdélník a trojúhelník
│    2  Složené útvary
│    3  Obvod vyjádřený proměnnou
│    3  Trojúhelníková nerovnost
│    3  Rozestupy po obvodu
│    S  Podobnost trojúhelníků (věty sss, sus, uu, poměr podobnosti), shodnost
├─ Kruh a kružnice
│    2  Obvod a obsah kruhu, počítání s π ≐ 3,14, zaokrouhlení
│    2  Poloměr nebo průměr z obsahu
│    2  Půlkruh, čtvrtkruh, výseč: obsah a obvod
│    3  Útvary ohraničené oblouky
│    S  Tečna, sečna, vnější přímka; vzájemná poloha dvou kružnic
└─ Tělesa
     1  Krychle a kvádr: objem, povrch, součet hran, i zpětně
     1  Kolmý hranol: objem a povrch
     1  Válec: objem, plášť, povrch
     3  Síť tělesa
     2  Slepená a rozříznutá tělesa
     3  Tělesa z krychliček, prostorová představivost
     2  Vztah místo čísla: rovnice pro výšku nebo hranu
     2  Objem v litrech, výška hladiny
     S  Jehlan (promítání, síť, pohledy), koule (poloměr a průměr), pohledy na těleso, náčrt sítě

KON  Geometrie: konstrukce
├─ Základní konstrukce
│    1  Kolmice a rovnoběžka daným bodem
│    1  Střed a osa úsečky
│    3  Osa úhlu
│    1  Přenesení délky kružnicí
│    3  Úhel dané velikosti
│    1  Thaletova kružnice nad úsečkou
│    1  Obraz bodu ve středové souměrnosti („S je střed“)
│    2  Obraz v osové souměrnosti, osa z bodu a jeho obrazu
├─ Vlastnosti útvarů, o které se konstrukce opírá
│    1  Rovnoramenný trojúhelník: osa souměrnosti je osou základny
│    2  Rovnostranný trojúhelník
│    1  Pravoúhlý trojúhelník: vrchol pravého úhlu na Thaletově kružnici
│    2  Výška a těžnice
│    2  Čtverec: shodné, kolmé, půlící se úhlopříčky
│    1  Obdélník: shodné půlící se úhlopříčky, vrcholy na kružnici
│    1  Rovnoběžník: úhlopříčky se půlí, střed souměrnosti
│    2  Kosočtverec: kolmé úhlopříčky, osa souměrnosti
│    2  Lichoběžník: rovnoramenný a pravoúhlý
│    3  Pravidelný šestiúhelník: strana = poloměr kružnice opsané
├─ Rozbor zadání
│    1  Náčrt a převod nepřímé podmínky na množinu bodů
│    1  „Najděte všechna řešení“: druhé řešení
│    1  Označení vrcholů a obtažení konstrukce
│    S  Trojúhelník podle sss, sus, usu; kružnice opsaná; tečna kružnice v jejím bodě
└─ Souměrnost útvarů
     3  Osy souměrnosti útvaru ve čtvercové síti a mnohoúhelníků
     S  Samodružný bod a útvar; vzor a obraz

ZAK  Zákonitosti a úsudek
├─ Rostoucí obrazce a číselné řady
│    1  Pokračování pravidla a tabulka počtů po krocích
│    2  Obecný n-tý člen (lineární růst, n², n·(n + 1)/2)
│    2  Obrácení pravidla: který krok má daný počet
│    3  Růst násobením (mocniny tří)
│    3  Číselná řada daná pravidlem
└─ Úsudek a systematické hledání
     2  Periodické děje: cykly a společný násobek
     2  Systematické vypsání všech řešení
     3  Strategické a netradiční geometrické úlohy
```

## Počítání s čísly (POC)

The tools every other branch uses. Fast and error-free here is what frees time for tasks 6–16.

### Číselné výrazy, mocniny, odmocniny

`POC.VYR` · catalog tag N-ARIT · specification area 1 · One or two 1-point openers; from 2025 also inside the fraction task.

| P | Skill | Kind | Needs | Examples | Note |
|---|---|---|---|---|---|
| 2 | Pořadí operací, závorky, záporná čísla | postup |  | [2022 B 1](../backend/data/screenshots/M9-2022-B-01.png) 68 % · [2022 D 2](../backend/data/screenshots/M9-2022-D-02.png) 28 % · [2023 C 2](../backend/data/screenshots/M9-2023-C-02.png) 44 % | Sign rules: (−6)² = 36, −3·(−3) = +9. |
| 2 | Počítání s desetinnými čísly bez kalkulačky | postup | Pořadí operací (POC.VYR) | [2026 A 2.1](../backend/data/screenshots/M9-2026-A-02.png) 52 % · [2026 D 2.1](../backend/data/screenshots/M9-2026-D-02.png) 25 % | Multiplying and dividing by decimals: (0,08 − 1) : 0,2. |
| 1 | Druhá mocnina a odmocnina | znalost |  | [2022 A 1](../backend/data/screenshots/M9-2022-A-01.png) 82 % · [2023 B 1](../backend/data/screenshots/M9-2023-B-01.png) 65 % · [2022 C 1](../backend/data/screenshots/M9-2022-C-01.png) 52 % · [2025 B 2](../backend/data/screenshots/M9-2025-B-02.png) 34 % | Squares 1–20 and their roots, decimals, powers of ten, root of a fraction and of a product. Compute inside the root first. Needed all over geometry. |
| 2 | Výraz zadaný slovy (součet, rozdíl, součin, podíl) | překlad | Pořadí operací (POC.VYR) | [2023 C 1](../backend/data/screenshots/M9-2023-C-01.png) 28 % · [2025 A 1](../backend/data/screenshots/M9-2025-A-01.png) 44 % | The verbal items are the ones that fail, not the computations. |
| 3 | Číselná osa se stejnými dílky | postup |  | [2023 D 2](../backend/data/screenshots/M9-2023-D-02.png) 25 % · [2022 B 2](../backend/data/screenshots/M9-2022-B-02.png) 24 % |  |
| S | Absolutní hodnota, opačné číslo, periodické číslo, zaokrouhlování, odhady | znalost |  |  | Rounding occurs only as the last step of π tasks. |

### Počítání se zlomky

`POC.ZLOM` · catalog tag N-ZLOM · specification area 1 · The computation task of every test: 3–4 points, among the best solved open tasks. Fraction word problems are in VZT.

| P | Skill | Kind | Needs | Examples | Note |
|---|---|---|---|---|---|
| 1 | Čtyři operace se zlomky, společný jmenovatel, krácení, základní tvar | postup | Pořadí operací (POC.VYR) | [2022 B 3](../backend/data/screenshots/M9-2022-B-03.png) 76 % · [2023 B 3](../backend/data/screenshots/M9-2023-B-03.png) 72 % | An unreduced result costs 1 of 2 points. Never multiply the expression by the common denominator as if it were an equation. |
| 1 | Složený zlomek | postup | Čtyři operace se zlomky (POC.ZLOM) | [2022 A 3](../backend/data/screenshots/M9-2022-A-03.png) 65 % · [2023 A 3](../backend/data/screenshots/M9-2023-A-03.png) 60 % · [2026 B 2](../backend/data/screenshots/M9-2026-B-02.png) 67 % | The worked 2-point item in almost every test. |
| 2 | Zlomky spolu s desetinnými čísly | postup | Čtyři operace se zlomky (POC.ZLOM), Počítání s desetinnými čísly bez kalkulačky (POC.VYR) | [2024 A 3.2](../backend/data/screenshots/M9-2024-A-03.png) 64 % · [2024 C 3.1](../backend/data/screenshots/M9-2024-C-03.png) · [2024 D 3.1](../backend/data/screenshots/M9-2024-D-03.png) · [2026 C 2.2](../backend/data/screenshots/M9-2026-C-02.png) 29 % | Convert the decimal to a fraction first (1,4 = 7/5). |
| 2 | Zlomky s druhou mocninou a odmocninou | postup | Čtyři operace se zlomky (POC.ZLOM), Druhá mocnina a odmocnina (POC.VYR) | [2025 A 2](../backend/data/screenshots/M9-2025-A-02.png) 59 % · [2025 B 3](../backend/data/screenshots/M9-2025-B-03.png) 66 % · [2025 C 3](../backend/data/screenshots/M9-2025-C-03.png) 40 % · [2025 D 3](../backend/data/screenshots/M9-2025-D-03.png) 35 % | From 2025. |
| 3 | Smíšené číslo | postup | Čtyři operace se zlomky (POC.ZLOM) | [2025 B 2](../backend/data/screenshots/M9-2025-B-02.png) 34 % | Once in 20 tests. |
| S | Porovnávání zlomků, převrácený zlomek, zlomek jako periodické číslo | znalost |  |  |  |

### Dělitelnost

`POC.DEL` · catalog tag N-DEL · specification area 1 · Small and badly solved (19 %); usually hidden in a word problem.

| P | Skill | Kind | Needs | Examples | Note |
|---|---|---|---|---|---|
| 3 | Dělitelé a násobky čísla | postup |  | [2022 D 1](../backend/data/screenshots/M9-2022-D-01.png) 14 % |  |
| 3 | Prvočísla a rozklad na prvočísla | postup | Dělitelé a násobky čísla (POC.DEL) | [2025 B 6](../backend/data/screenshots/M9-2025-B-06.png) 27 % · [2025 C 2](../backend/data/screenshots/M9-2025-C-02.png) 11 % · [2026 B 12](../backend/data/screenshots/M9-2026-B-12.png) 20 % | 2 is the only even prime. |
| 3 | Dělení se zbytkem ve slovní úloze | postup |  | [2026 D 13](../backend/data/screenshots/M9-2026-D-13.png) 27 % |  |
| 2 | Společný násobek | postup | Dělitelé a násobky čísla (POC.DEL) | [2025 A 8.3](../backend/data/screenshots/M9-2025-A-08.png) 2 % | Never asked by name, but it is what common denominators and the periodic tasks of task 16 use. |
| S | Znaky dělitelnosti, nejmenší společný násobek a největší společný dělitel podle názvu | znalost |  |  |  |

### Převody jednotek

`POC.JED` · catalog tag N-JED · specification area 1 · Rarely a task of its own; mostly silent: data in one unit, answer demanded in another.

| P | Skill | Kind | Needs | Examples | Note |
|---|---|---|---|---|---|
| 2 | Délka (mm, cm, dm, m, km) | znalost |  | [2024 B 1](../backend/data/screenshots/M9-2024-B-01.png) 50 % · [2022 C 2](../backend/data/screenshots/M9-2022-C-02.png) 49 % |  |
| 2 | Obsah (krok × 100) | znalost | Délka (mm (POC.JED) | [2026 B 1](../backend/data/screenshots/M9-2026-B-01.png) 41 % · [2022 A 2](../backend/data/screenshots/M9-2022-A-02.png) 34 % |  |
| 2 | Objem a litry (krok × 1 000, 1 l = 1 dm³) | znalost | Délka (mm (POC.JED) | [2022 A 2.2](../backend/data/screenshots/M9-2022-A-02.png) 39 % · [2023 A 2.2](../backend/data/screenshots/M9-2023-A-02.png) 24 % · [2025 A 6](../backend/data/screenshots/M9-2025-A-06.png) 18 % |  |
| 3 | Hmotnost (g, kg) | znalost |  | [2025 C 1](../backend/data/screenshots/M9-2025-C-01.png) 29 % |  |
| 2 | Čas (hodiny, minuty, desetinné hodiny, sčítání časů) | znalost |  | [2026 C 1](../backend/data/screenshots/M9-2026-C-01.png) 40 % · [2022 A 11](../backend/data/screenshots/M9-2022-A-11.png) 74 % · [2022 C 2.2](../backend/data/screenshots/M9-2022-C-02.png) 57 % | Needed for pohyb. |
| S | Sekunda a týden jako převáděné jednotky | znalost |  |  |  |

## Výrazy a rovnice (ALG)

Two fixed tasks, 8 points in every one of the 20 tests, each with a fixed set of item roles. The most predictable points of the test.

### Úpravy výrazů

`ALG.VYR` · catalog tag A-VYR · specification area 1 · Always three items, 1 + 1 + 2 points.

| P | Skill | Kind | Needs | Examples | Note |
|---|---|---|---|---|---|
| 1 | Roznásobení závorek a sloučení členů | postup | Pořadí operací (POC.VYR) | [2022 A 4.3](../backend/data/screenshots/M9-2022-A-04.png) 50 % | The worked 2-point item. The trap is a bracket to simplify before multiplying, e.g. (3n − 2n). |
| 1 | Vytýkání | postup | Roznásobení závorek a sloučení členů (ALG.VYR) | [2022 A 4.1](../backend/data/screenshots/M9-2022-A-04.png) 50 % · [2023 A 4.1](../backend/data/screenshots/M9-2023-A-04.png) 38 % · [2023 B 4.1](../backend/data/screenshots/M9-2023-B-04.png) 46 % · [2026 B 3.2](../backend/data/screenshots/M9-2026-B-03.png) 55 % · [2026 D 3.1](../backend/data/screenshots/M9-2026-D-03.png) 26 % | Usually after simplifying first; also a prescribed factor such as (−x). |
| 1 | Umocnění dvojčlenu (a ± b)² | postup | Roznásobení závorek a sloučení členů (ALG.VYR), Druhá mocnina a odmocnina (POC.VYR) | [2022 B 4.2](../backend/data/screenshots/M9-2022-B-04.png) 40 % · [2023 D 4.1](../backend/data/screenshots/M9-2023-D-04.png) 27 % · [2024 A 4.1](../backend/data/screenshots/M9-2024-A-04.png) 9 % · [2025 C 4.1](../backend/data/screenshots/M9-2025-C-04.png) 14 % · [2026 C 3.2](../backend/data/screenshots/M9-2026-C-03.png) 16 % | Awkward coefficients: fractions, decimals, two minus signs. |
| 2 | Vzorec (a ± b)² zpětně – doplnění chybějících čísel | postup | Umocnění dvojčlenu (a ± b)² (ALG.VYR) | [2022 D 4.2](../backend/data/screenshots/M9-2022-D-04.png) 54 % · [2025 A 3.1](../backend/data/screenshots/M9-2025-A-03.png) 65 % |  |
| 1 | Rozklad a² − b² na součin | postup | Umocnění dvojčlenu (a ± b)² (ALG.VYR) | [2023 C 4.1](../backend/data/screenshots/M9-2023-C-04.png) 43 % · [2024 B 4.2](../backend/data/screenshots/M9-2024-B-04.png) 23 % · [2025 D 4.2](../backend/data/screenshots/M9-2025-D-04.png) 35 % · [2025 A 3.3](../backend/data/screenshots/M9-2025-A-03.png) 48 % · [2023 B 4](../backend/data/screenshots/M9-2023-B-04.png) 52 % | In disguise: 49 − (−4a)², or simplify first and then factor. |
| 3 | Hodnota výrazu pro dané číslo | postup |  | [2026 A 3](../backend/data/screenshots/M9-2026-A-03.png) 48 % |  |

### Lineární rovnice a soustavy

`ALG.ROV` · catalog tag A-ROV, A-SOU · specification area 1 · Two worked items of 2 points; the check is never required.

| P | Skill | Kind | Needs | Examples | Note |
|---|---|---|---|---|---|
| 1 | Rovnice se závorkami a desetinnými čísly | postup | Roznásobení závorek a sloučení členů (ALG.VYR), Počítání s desetinnými čísly bez kalkulačky (POC.VYR) | [2022 B 5](../backend/data/screenshots/M9-2022-B-05.png) 72 % · [2023 B 5](../backend/data/screenshots/M9-2023-B-05.png) 48 % · [2026 D 4](../backend/data/screenshots/M9-2026-D-04.png) 29 % |  |
| 1 | Rovnice se zlomky | postup | Rovnice se závorkami a desetinnými čísly (ALG.ROV), Čtyři operace se zlomky (POC.ZLOM) | [2022 A 5](../backend/data/screenshots/M9-2022-A-05.png) 48 % · [2023 C 5](../backend/data/screenshots/M9-2023-C-05.png) 40 % · [2025 C 5](../backend/data/screenshots/M9-2025-C-05.png) 34 % · [2026 B 4](../backend/data/screenshots/M9-2026-B-04.png) 56 % | Keep each numerator in a bracket; the minus before a fraction is the classic error. |
| 2 | Rovnice bez řešení | znalost | Rovnice se závorkami a desetinnými čísly (ALG.ROV) | [2023 A 5](../backend/data/screenshots/M9-2023-A-05.png) 53 % · [2025 A 4](../backend/data/screenshots/M9-2025-A-04.png) 34 % | The sentence „rovnice nemá řešení“ must be written. „Nekonečně mnoho řešení“ is in the specification only. |
| 3 | Rovnice s druhými mocninami dvojčlenů, ve které x² vypadne | postup | Rovnice se závorkami a desetinnými čísly (ALG.ROV), Umocnění dvojčlenu (a ± b)² (ALG.VYR) | [2024 A 5](../backend/data/screenshots/M9-2024-A-05.png) 31 % · [2024 C 5](../backend/data/screenshots/M9-2024-C-05.png) | Only in the 2024 tests. |
| 2 | Soustava dvou rovnic se dvěma neznámými | postup | Rovnice se závorkami a desetinnými čísly (ALG.ROV) | [2025 B 5](../backend/data/screenshots/M9-2025-B-05.png) 48 % · [2025 D 5](../backend/data/screenshots/M9-2025-D-05.png) 34 % · [2026 A 4](../backend/data/screenshots/M9-2026-A-04.png) 54 % · [2026 C 4](../backend/data/screenshots/M9-2026-C-04.png) 41 % | From 2025, in 4 of 8 tests. Dosazovací or sčítací metoda. |

## Vztahy mezi veličinami: zlomek, procento, poměr (VZT)

The same relation is told as a fraction, a percentage or a ratio. Most points of tasks 6–8 and 15 are lost on reading the relation, not on computing.

### Zlomek jako část celku

`VZT.CAST` · catalog tag N-ZLOM · specification area 1 · Single 1-point word items solved by 21–33 %, while the fraction computation task scores 58–76 %.

| P | Skill | Kind | Needs | Examples | Note |
|---|---|---|---|---|---|
| 2 | Zlomek z množství a z času | překlad | Čtyři operace se zlomky (POC.ZLOM) | [2022 A 11](../backend/data/screenshots/M9-2022-A-11.png) 74 % · [2022 C 2.2](../backend/data/screenshots/M9-2022-C-02.png) 57 % |  |
| 2 | Část ze zbytku | překlad | Zlomek z množství a z času (VZT.CAST) | [2025 D 1](../backend/data/screenshots/M9-2025-D-01.png) 21 % | „dvě pětiny zbytku“ is a part of what is left, not of the whole. |
| 1 | Celek z části | překlad | Zlomek z množství a z času (VZT.CAST) | [2022 B 6](../backend/data/screenshots/M9-2022-B-06.png) 32 % · [2023 B 14](../backend/data/screenshots/M9-2023-B-14.png) 33 % · [2023 C 12](../backend/data/screenshots/M9-2023-C-12.png) 40 % · [2025 B 1](../backend/data/screenshots/M9-2025-B-01.png) 33 % · [2026 B 14](../backend/data/screenshots/M9-2026-B-14.png) 39 % · [2023 A 1](../backend/data/screenshots/M9-2023-A-01.png) 33 % | „pětina a o 180 více“ – find what fraction the known number is. |

### Srovnání „o … více než“, „kolikrát“

`VZT.NEZ` · catalog tag A-SLOV · specification area 1 · The phrases that carry the difficulty across fractions, percentages and word problems (03, section 20). Learn them once, here.

| P | Skill | Kind | Needs | Examples | Note |
|---|---|---|---|---|---|
| 1 | „o kolik“ je rozdíl, „kolikrát“ je podíl | překlad |  | [2022 A 2](../backend/data/screenshots/M9-2022-A-02.png) 34 % · [2022 C 14](../backend/data/screenshots/M9-2022-C-14.png) 24 % · [2026 B 7](../backend/data/screenshots/M9-2026-B-07.png) 31 % · [2022 B 6](../backend/data/screenshots/M9-2022-B-06.png) 32 % · [2025 D 12](../backend/data/screenshots/M9-2025-D-12.png) 29 % |  |
| 1 | „o třetinu více / méně než“ jako násobení | překlad | Čtyři operace se zlomky (POC.ZLOM) | [2022 C 6](../backend/data/screenshots/M9-2022-C-06.png) 24 % · [2023 D 6](../backend/data/screenshots/M9-2023-D-06.png) 21 % · [2023 B 7](../backend/data/screenshots/M9-2023-B-07.png) 36 % · [2024 B 7](../backend/data/screenshots/M9-2024-B-07.png) 41 % · [2025 B 7](../backend/data/screenshots/M9-2025-B-07.png) 14 % | 4/3 · x and 2/3 · x, where x is the quantity after „než“. |
| 2 | „dvakrát méně“, „čtyřikrát menší než“ jako dělení | překlad |  | [2025 D 13](../backend/data/screenshots/M9-2025-D-13.png) 25 % · [2026 D 5](../backend/data/screenshots/M9-2026-D-05.png) 15 % · [2025 C 7](../backend/data/screenshots/M9-2025-C-07.png) 20 % |  |
| 1 | Obrácení vztahu: neznámá není veličina za „než“ | překlad | „o třetinu více / méně než“ jako násobení (VZT.NEZ) | [2025 C 6](../backend/data/screenshots/M9-2025-C-06.png) 8 % · [2026 A 5](../backend/data/screenshots/M9-2026-A-05.png) 28 % · [2023 B 7](../backend/data/screenshots/M9-2023-B-07.png) 36 % | „o polovinu levnější než skříň“ with the table = n means the wardrobe is 2n. Solved by 8–28 %. |

### Procenta

`VZT.PROC` · catalog tag P-PROC · specification area 1 · The largest topic: task 15 in every standard test plus one or two items elsewhere. Points are lost on choosing the base.

| P | Skill | Kind | Needs | Examples | Note |
|---|---|---|---|---|---|
| 1 | Procentová část, počet procent, základ | postup | Počítání s desetinnými čísly bez kalkulačky (POC.VYR) | [2024 B 16](../backend/data/screenshots/M9-2024-B-16.png) 74 % · [2024 D 12](../backend/data/screenshots/M9-2024-D-12.png) · [2025 A 15.1](../backend/data/screenshots/M9-2025-A-15.png) 71 % · [2026 D 15](../backend/data/screenshots/M9-2026-D-15.png) 37 % | Where the base is the obvious number, items score 70–80 %. |
| 1 | „o x % více / méně“ jako násobitel | překlad | Procentová část (VZT.PROC) | [2023 B 2](../backend/data/screenshots/M9-2023-B-02.png) 45 % · [2023 C 15](../backend/data/screenshots/M9-2023-C-15.png) 48 % | +25 % is ·1,25; −40 % is ·0,6; +150 % is ·2,5. |
| 1 | Základ po změně („což je o 40 % více než loni“) | překlad | „o x % více / méně“ jako násobitel (VZT.PROC) | [2022 A 15](../backend/data/screenshots/M9-2022-A-15.png) 43 % · [2023 A 15.2](../backend/data/screenshots/M9-2023-A-15.png) 28 % · [2023 D 15](../backend/data/screenshots/M9-2023-D-15.png) 40 % · [2026 B 15](../backend/data/screenshots/M9-2026-B-15.png) 46 % | Divide by the multiplier: 420 : 1,4. |
| 1 | „O kolik procent“ se liší dvě veličiny | překlad | Procentová část (VZT.PROC) | [2022 B 15](../backend/data/screenshots/M9-2022-B-15.png) 40 % · [2024 B 2](../backend/data/screenshots/M9-2024-B-02.png) 34 % · [2026 B 5](../backend/data/screenshots/M9-2026-B-05.png) 42 % · [2026 C 15](../backend/data/screenshots/M9-2026-C-15.png) 32 % · [2026 A 15](../backend/data/screenshots/M9-2026-A-15.png) 56 % | Difference divided by the quantity after „než“. |
| 2 | Obrácené srovnání („o třetinu méně“ je opačně „o 50 % více“) | překlad | „O kolik procent“ se liší dvě veličiny (VZT.PROC), Obrácení vztahu (VZT.NEZ) | [2025 B 15.2](../backend/data/screenshots/M9-2025-B-15.png) 12 % · [2022 D 15](../backend/data/screenshots/M9-2022-D-15.png) 41 % | In 2025 B 15.2 the naive option 33 % drew 47,8 % of candidates. |
| 2 | Dvě změny po sobě | postup | „o x % více / méně“ jako násobitel (VZT.PROC) | [2023 A 15](../backend/data/screenshots/M9-2023-A-15.png) 38 % · [2024 B 11](../backend/data/screenshots/M9-2024-B-11.png) 73 % · [2024 D 2](../backend/data/screenshots/M9-2024-D-02.png) · [2026 D 1](../backend/data/screenshots/M9-2026-D-01.png) 10 % · [2026 D 12](../backend/data/screenshots/M9-2026-D-12.png) 18 % | Multiply the multipliers: +40 % then −40 % is ·0,84. |
| 2 | Procento ze zbytku | překlad | Procentová část (VZT.PROC), Část ze zbytku (VZT.CAST) | [2022 B 15](../backend/data/screenshots/M9-2022-B-15.png) 40 % · [2022 C 15](../backend/data/screenshots/M9-2022-C-15.png) 31 % · [2026 B 15](../backend/data/screenshots/M9-2026-B-15.png) 46 % |  |
| 2 | Dvě veličiny svázané procentem a známý součet | překlad | „o x % více / méně“ jako násobitel (VZT.PROC), Rovnice se závorkami a desetinnými čísly (ALG.ROV) | [2023 D 15](../backend/data/screenshots/M9-2023-D-15.png) 40 % · [2024 C 12](../backend/data/screenshots/M9-2024-C-12.png) · [2025 C 15](../backend/data/screenshots/M9-2025-C-15.png) 35 % | x + 0,7x = 680. |
| 1 | Procento, zlomek a poměr: převody mezi nimi | znalost | Procentová část (VZT.PROC) | [2026 A 12](../backend/data/screenshots/M9-2026-A-12.png) 50 % · [2025 D 15](../backend/data/screenshots/M9-2025-D-15.png) 37 % · [2022 D 15](../backend/data/screenshots/M9-2022-D-15.png) 41 % · [2026 C 15](../backend/data/screenshots/M9-2026-C-15.png) 32 % | „každý dvacátý“ = 5 %; 3 : 2 is „o 50 % více“. |
| 3 | Změna v procentních bodech | překlad | Procentová část (VZT.PROC) | [2024 C 13](../backend/data/screenshots/M9-2024-C-13.png) | Once in 20 tests. |
| 3 | Úrok za jeden rok a daň z úroku | postup | Procentová část (VZT.PROC) | [2024 A 16](../backend/data/screenshots/M9-2024-A-16.png) 62 % | Once in 20 tests. |
| S | Promile; jistina, úroková míra, úrokovací období, inflace, půjčky a úvěry | znalost |  |  |  |

### Poměr a úměrnost

`VZT.POM` · catalog tag P-POM · specification area 1, 2, 3 · Result-only tasks 6–8 with graduated sub-items, or multiple choice. No formula is asked for; small numbers and reasoning.

| P | Skill | Kind | Needs | Examples | Note |
|---|---|---|---|---|---|
| 2 | Poměr v základním tvaru, dělení v poměru | postup | Čtyři operace se zlomky (POC.ZLOM) | [2023 D 1](../backend/data/screenshots/M9-2023-D-01.png) 41 % · [2025 D 2](../backend/data/screenshots/M9-2025-D-02.png) 17 % · [2026 D 7](../backend/data/screenshots/M9-2026-D-07.png) 13 % | Also the parts from their difference: 3 : 5 and a difference of 600 g. |
| 3 | Poměr na číselné ose a na úsečce | postup | Poměr v základním tvaru (VZT.POM), Číselná osa se stejnými dílky (POC.VYR) | [2022 B 2](../backend/data/screenshots/M9-2022-B-02.png) 24 % |  |
| 2 | Měřítko mapy a plánu | postup | Poměr v základním tvaru (VZT.POM), Délka (mm (POC.JED), Obsah (krok × 100) (POC.JED) | [2023 A 11](../backend/data/screenshots/M9-2023-A-11.png) 58 % · [2024 A 15](../backend/data/screenshots/M9-2024-A-15.png) 59 % | Area scales with the square of the length scale. |
| 2 | Přímá úměrnost | postup | Poměr v základním tvaru (VZT.POM) | [2026 B 5](../backend/data/screenshots/M9-2026-B-05.png) 42 % · [2026 C 13](../backend/data/screenshots/M9-2026-C-13.png) 57 % |  |
| 2 | Nepřímá úměrnost | postup | Přímá úměrnost (VZT.POM) | [2026 C 12](../backend/data/screenshots/M9-2026-C-12.png) 42 % · [2023 B 6](../backend/data/screenshots/M9-2023-B-06.png) 21 % · [2024 C 16](../backend/data/screenshots/M9-2024-C-16.png) · [2024 A 1](../backend/data/screenshots/M9-2024-A-01.png) 18 % |  |
| 2 | Společná práce | postup | Nepřímá úměrnost (VZT.POM), Čtyři operace se zlomky (POC.ZLOM) | [2024 D 13](../backend/data/screenshots/M9-2024-D-13.png) · [2025 D 6](../backend/data/screenshots/M9-2025-D-06.png) 23 % · [2022 A 7](../backend/data/screenshots/M9-2022-A-07.png) 34 % | Add the rates per unit of time, not the times. |
| 2 | Pohyb: s = v · t | postup | Přímá úměrnost (VZT.POM), Čas (hodiny (POC.JED) | [2025 C 7](../backend/data/screenshots/M9-2025-C-07.png) 20 % · [2026 A 7](../backend/data/screenshots/M9-2026-A-07.png) 28 % · [2026 D 8](../backend/data/screenshots/M9-2026-D-08.png) 39 % |  |
| 3 | Směsi a průměrná cena | postup | Poměr v základním tvaru (VZT.POM) | [2023 C 8](../backend/data/screenshots/M9-2023-C-08.png) 11 % |  |
| S | Postupný a převrácený poměr; graf a rovnice přímé a nepřímé úměrnosti; bod v pravoúhlé soustavě souřadnic | znalost |  |  | No coordinate system in any of the 20 tests. |

### Slovní úlohy na rovnici

`VZT.SLOV` · catalog tag A-SLOV · specification area 1 · The fixed three-step task (two expressions, then an equation) in 12 of 16 standard tests; its last step is solved by 10–27 %.

| P | Skill | Kind | Needs | Examples | Note |
|---|---|---|---|---|---|
| 1 | Vyjádření veličiny výrazem s proměnnou | překlad | „o třetinu více / méně než“ jako násobení (VZT.NEZ), Obrácení vztahu (VZT.NEZ) | [2022 A 8.1](../backend/data/screenshots/M9-2022-A-08.png) 39 % · [2022 C 6](../backend/data/screenshots/M9-2022-C-06.png) 24 % · [2026 C 5](../backend/data/screenshots/M9-2026-C-05.png) 19 % · [2022 B 14](../backend/data/screenshots/M9-2022-B-14.png) 37 % | The answer is an expression such as 4x/3, not a number. |
| 1 | Sestavení a vyřešení rovnice z další podmínky | rozbor | Vyjádření veličiny výrazem s proměnnou (VZT.SLOV), Rovnice se zlomky (ALG.ROV) | [2022 A 8](../backend/data/screenshots/M9-2022-A-08.png) 49 % · [2023 B 7](../backend/data/screenshots/M9-2023-B-07.png) 36 % · [2026 A 6](../backend/data/screenshots/M9-2026-A-06.png) 19 % · [2026 D 5](../backend/data/screenshots/M9-2026-D-05.png) 15 % | Answer the quantity that is asked, which may not be x. |
| 2 | Dvě neznámé: počty a součty | rozbor | Sestavení a vyřešení rovnice z další podmínky (VZT.SLOV), Soustava dvou rovnic se dvěma neznámými (ALG.ROV) | [2026 B 6](../backend/data/screenshots/M9-2026-B-06.png) 38 % · [2026 C 14](../backend/data/screenshots/M9-2026-C-14.png) 37 % · [2023 D 7](../backend/data/screenshots/M9-2023-D-07.png) 26 % · [2024 D 6](../backend/data/screenshots/M9-2024-D-06.png) · [2025 D 13](../backend/data/screenshots/M9-2025-D-13.png) 25 % |  |
| 2 | Řešení úsudkem bez rovnice | rozbor |  | [2022 D 6](../backend/data/screenshots/M9-2022-D-06.png) 21 % · [2024 D 7](../backend/data/screenshots/M9-2024-D-07.png) · [2022 C 7](../backend/data/screenshots/M9-2022-C-07.png) 55 % |  |
| 3 | Podmínka, že výsledek je celé číslo | rozbor | Sestavení a vyřešení rovnice z další podmínky (VZT.SLOV), Dělení se zbytkem ve slovní úloze (POC.DEL) | [2023 D 7](../backend/data/screenshots/M9-2023-D-07.png) 26 % · [2024 D 15](../backend/data/screenshots/M9-2024-D-15.png) · [2026 D 13](../backend/data/screenshots/M9-2026-D-13.png) 27 % |  |

## Grafy, tabulky, průměr (DAT)

Task 11 (A/N) in 9 of 16 standard tests. Reading values is easy; the conditions in the text are where points go.

### Grafy a tabulky

`DAT.GRAF` · catalog tag D-GRAF · specification area 2

| P | Skill | Kind | Needs | Examples | Note |
|---|---|---|---|---|---|
| 1 | Čtení sloupcového grafu (více řad, skládaný) | postup |  | [2022 C 11](../backend/data/screenshots/M9-2022-C-11.png) 53 % · [2025 C 11](../backend/data/screenshots/M9-2025-C-11.png) 71 % · [2024 B 15](../backend/data/screenshots/M9-2024-B-15.png) 61 % |  |
| 1 | Doplnění chybějícího údaje z podmínek v textu | rozbor | Čtení sloupcového grafu (více řad (DAT.GRAF) | [2023 A 7](../backend/data/screenshots/M9-2023-A-07.png) 14 % · [2025 D 14](../backend/data/screenshots/M9-2025-D-14.png) 28 % · [2023 D 11](../backend/data/screenshots/M9-2023-D-11.png) 57 % · [2026 B 11](../backend/data/screenshots/M9-2026-B-11.png) 60 % · [2022 B 7](../backend/data/screenshots/M9-2022-B-07.png) 50 % | A missing bar or an axis without numbers. Open versions score 14–50 %. |
| 2 | Kruhový diagram (procenta, středové úhly) | postup | Procentová část (VZT.PROC) | [2025 B 11](../backend/data/screenshots/M9-2025-B-11.png) 68 % · [2026 A 11](../backend/data/screenshots/M9-2026-A-11.png) 66 % · [2022 A 14](../backend/data/screenshots/M9-2022-A-14.png) 35 % · [2024 C 15](../backend/data/screenshots/M9-2024-C-15.png) | 360° is the whole, 60° is one sixth. |
| 3 | Čtení tabulky, třídění údajů z textu | postup |  | [2024 D 7](../backend/data/screenshots/M9-2024-D-07.png) · [2024 A 7](../backend/data/screenshots/M9-2024-A-07.png) 56 % |  |
| S | Statistický soubor, statistický znak, četnost; volba vhodného grafu | znalost |  |  | Medián and modus are neither in the specification nor in the tests. |

### Aritmetický průměr

`DAT.PRUM` · catalog tag D-GRAF · specification area 2

| P | Skill | Kind | Needs | Examples | Note |
|---|---|---|---|---|---|
| 2 | Výpočet aritmetického průměru | postup |  | [2022 B 7](../backend/data/screenshots/M9-2022-B-07.png) 50 % · [2026 D 11](../backend/data/screenshots/M9-2026-D-11.png) 58 % |  |
| 3 | Průměr z tabulky četností | postup | Výpočet aritmetického průměru (DAT.PRUM) | [2025 A 14](../backend/data/screenshots/M9-2025-A-14.png) 36 % | Count × value, divided by the total count. |
| 3 | Chybějící hodnota z daného průměru | postup | Výpočet aritmetického průměru (DAT.PRUM) | [2025 D 7](../backend/data/screenshots/M9-2025-D-07.png) 16 % |  |

## Geometrie: výpočty (GEO)

No formula except the circle's is printed. Tasks are chains: a figure, a hidden right triangle, a unit change.

### Úhly

`GEO.UHLY` · catalog tag G-UHLY · specification area 3 · One multiple-choice item among 12–14 in most tests. Straight chains score 50–67 %, figures needing an auxiliary idea 21–24 %.

| P | Skill | Kind | Needs | Examples | Note |
|---|---|---|---|---|---|
| 1 | Vrcholové, vedlejší, souhlasné a střídavé úhly | znalost |  | [2022 B 13](../backend/data/screenshots/M9-2022-B-13.png) 54 % · [2025 A 7](../backend/data/screenshots/M9-2025-A-07.png) 57 % |  |
| 1 | Součet úhlů v trojúhelníku a čtyřúhelníku | znalost |  | [2024 A 11](../backend/data/screenshots/M9-2024-A-11.png) 67 % · [2024 B 13](../backend/data/screenshots/M9-2024-B-13.png) 66 % · [2023 D 13](../backend/data/screenshots/M9-2023-D-13.png) 26 % |  |
| 1 | Úhly v rovnoramenném a rovnostranném trojúhelníku | znalost | Součet úhlů v trojúhelníku a čtyřúhelníku (GEO.UHLY) | [2023 B 12](../backend/data/screenshots/M9-2023-B-12.png) 40 % · [2025 B 12](../backend/data/screenshots/M9-2025-B-12.png) 51 % · [2022 D 12](../backend/data/screenshots/M9-2022-D-12.png) 32 % |  |
| 2 | Úhly zapsané jako α, 2α, 3α nebo poměrem | rozbor | Vrcholové (GEO.UHLY), Součet úhlů v trojúhelníku a čtyřúhelníku (GEO.UHLY) | [2022 A 12](../backend/data/screenshots/M9-2022-A-12.png) 50 % · [2023 A 14](../backend/data/screenshots/M9-2023-A-14.png) 42 % · [2022 C 12](../backend/data/screenshots/M9-2022-C-12.png) 24 % · [2024 C 8](../backend/data/screenshots/M9-2024-C-08.png) | Set up an equation for α. |
| 3 | Osa úhlu | znalost | Součet úhlů v trojúhelníku a čtyřúhelníku (GEO.UHLY) | [2025 C 14](../backend/data/screenshots/M9-2025-C-14.png) 24 % · [2026 A 8](../backend/data/screenshots/M9-2026-A-08.png) 38 % |  |
| 3 | Pravidelný mnohoúhelník | znalost | Úhly v rovnoramenném a rovnostranném trojúhelníku (GEO.UHLY) | [2026 C 8](../backend/data/screenshots/M9-2026-C-08.png) 29 % | Regular pentagon 108°; hexagon as six equilateral triangles. |
| 3 | Úhly v kružnici: poloměry a Thaletova věta | znalost | Úhly v rovnoramenném a rovnostranném trojúhelníku (GEO.UHLY) | [2025 D 11](../backend/data/screenshots/M9-2025-D-11.png) 55 % · [2026 A 8](../backend/data/screenshots/M9-2026-A-08.png) 38 % |  |

### Pythagorova věta

`GEO.PYT` · catalog tag G-PYT · specification area 3 · Never asked for by name; always a hidden step. Sides are whole numbers in the tasks traced.

| P | Skill | Kind | Needs | Examples | Note |
|---|---|---|---|---|---|
| 1 | Přepona z odvěsen, odvěsna z přepony | postup | Druhá mocnina a odmocnina (POC.VYR) | [2022 C 8](../backend/data/screenshots/M9-2022-C-08.png) 30 % · [2025 C 12](../backend/data/screenshots/M9-2025-C-12.png) 38 % · [2024 B 2](../backend/data/screenshots/M9-2024-B-02.png) 34 % | Know the triples 3–4–5, 5–12–13, 8–15–17 and their multiples. |
| 1 | Nalezení pravoúhlého trojúhelníku v útvaru | rozbor | Přepona z odvěsen (GEO.PYT) | [2024 A 6](../backend/data/screenshots/M9-2024-A-06.png) 27 % · [2024 B 6](../backend/data/screenshots/M9-2024-B-06.png) 41 % · [2025 B 8](../backend/data/screenshots/M9-2025-B-08.png) 32 % · [2026 A 13](../backend/data/screenshots/M9-2026-A-13.png) 34 % · [2025 D 8](../backend/data/screenshots/M9-2025-D-08.png) 31 % | Height of an isosceles triangle or trapezoid, slanted side, diagonal. |
| 2 | Pythagorova věta v tělesech | rozbor | Nalezení pravoúhlého trojúhelníku v útvaru (GEO.PYT) | [2023 A 12](../backend/data/screenshots/M9-2023-A-12.png) 39 % · [2022 A 6](../backend/data/screenshots/M9-2022-A-06.png) 30 % · [2022 D 13](../backend/data/screenshots/M9-2022-D-13.png) 24 % · [2023 C 7](../backend/data/screenshots/M9-2023-C-07.png) 19 % · [2023 D 14](../backend/data/screenshots/M9-2023-D-14.png) 14 % | Stěnová úhlopříčka; hypotenuse of the base as an edge. |

### Obvod a obsah rovinných útvarů

`GEO.ROV` · catalog tag G-ROV · specification area 3 · A result-only task among 6–8; 22 % leave it blank. A direct area from given sides does not occur alone.

| P | Skill | Kind | Needs | Examples | Note |
|---|---|---|---|---|---|
| 1 | Vzorce pro obvod a obsah | znalost |  | [2023 A 6](../backend/data/screenshots/M9-2023-A-06.png) 25 % · [2025 B 8](../backend/data/screenshots/M9-2025-B-08.png) 32 % | Čtverec, obdélník, trojúhelník, rovnoběžník, kosočtverec, lichoběžník. None is printed. |
| 1 | Strana nebo výška z obsahu | postup | Vzorce pro obvod a obsah (GEO.ROV), Druhá mocnina a odmocnina (POC.VYR) | [2022 B 8](../backend/data/screenshots/M9-2022-B-08.png) 37 % · [2022 D 8](../backend/data/screenshots/M9-2022-D-08.png) 16 % · [2025 A 5](../backend/data/screenshots/M9-2025-A-05.png) 41 % · [2024 C 6](../backend/data/screenshots/M9-2024-C-06.png) · [2022 C 8](../backend/data/screenshots/M9-2022-C-08.png) 30 % |  |
| 3 | Obsah vypočtený dvěma způsoby | rozbor | Strana nebo výška z obsahu (GEO.ROV) | [2023 B 11](../backend/data/screenshots/M9-2023-B-11.png) 60 % | Height to the hypotenuse, height of a rhombus. |
| 2 | Lichoběžník rozdělený na obdélník a trojúhelník | rozbor | Vzorce pro obvod a obsah (GEO.ROV), Nalezení pravoúhlého trojúhelníku v útvaru (GEO.PYT) | [2024 A 6](../backend/data/screenshots/M9-2024-A-06.png) 27 % · [2024 B 6](../backend/data/screenshots/M9-2024-B-06.png) 41 % · [2025 B 8](../backend/data/screenshots/M9-2025-B-08.png) 32 % · [2025 D 8](../backend/data/screenshots/M9-2025-D-08.png) 31 % |  |
| 2 | Složené útvary | rozbor | Vzorce pro obvod a obsah (GEO.ROV) | [2022 B 8](../backend/data/screenshots/M9-2022-B-08.png) 37 % · [2023 D 12](../backend/data/screenshots/M9-2023-D-12.png) 20 % · [2024 A 12](../backend/data/screenshots/M9-2024-A-12.png) 43 % · [2026 C 6](../backend/data/screenshots/M9-2026-C-06.png) 14 % · [2026 D 6](../backend/data/screenshots/M9-2026-D-06.png) 30 % |  |
| 3 | Obvod vyjádřený proměnnou | rozbor | Vzorce pro obvod a obsah (GEO.ROV), Sestavení a vyřešení rovnice z další podmínky (VZT.SLOV) | [2023 A 8](../backend/data/screenshots/M9-2023-A-08.png) 25 % · [2024 A 13](../backend/data/screenshots/M9-2024-A-13.png) 31 % |  |
| 3 | Trojúhelníková nerovnost | znalost |  | [2026 B 8](../backend/data/screenshots/M9-2026-B-08.png) 11 % | Once in 20 tests. |
| 3 | Rozestupy po obvodu | rozbor |  | [2025 A 8](../backend/data/screenshots/M9-2025-A-08.png) 13 % | Once in 20 tests. |
| S | Podobnost trojúhelníků (věty sss, sus, uu, poměr podobnosti), shodnost | znalost |  |  |  |

### Kruh a kružnice

`GEO.KRUH` · catalog tag G-KRUH · specification area 3 · o = 2πr and S = πr² are printed. Radii are round (5, 10, 50).

| P | Skill | Kind | Needs | Examples | Note |
|---|---|---|---|---|---|
| 2 | Obvod a obsah kruhu, počítání s π ≐ 3,14, zaokrouhlení | postup | Počítání s desetinnými čísly bez kalkulačky (POC.VYR) | [2025 C 8](../backend/data/screenshots/M9-2025-C-08.png) 20 % · [2024 B 14](../backend/data/screenshots/M9-2024-B-14.png) 56 % | Do not confuse poloměr and průměr; round only the final result. |
| 2 | Poloměr nebo průměr z obsahu | postup | Obvod a obsah kruhu (GEO.KRUH), Druhá mocnina a odmocnina (POC.VYR) | [2023 B 8](../backend/data/screenshots/M9-2023-B-08.png) 24 % · [2024 C 7](../backend/data/screenshots/M9-2024-C-07.png) |  |
| 2 | Půlkruh, čtvrtkruh, výseč: obsah a obvod | postup | Obvod a obsah kruhu (GEO.KRUH) | [2022 A 13](../backend/data/screenshots/M9-2022-A-13.png) 40 % · [2026 B 7](../backend/data/screenshots/M9-2026-B-07.png) 31 % | Perimeter of a part = arc + the straight sides. |
| 3 | Útvary ohraničené oblouky | rozbor | Půlkruh (GEO.KRUH), Složené útvary (GEO.ROV) | [2024 A 8](../backend/data/screenshots/M9-2024-A-08.png) 22 % |  |
| S | Tečna, sečna, vnější přímka; vzájemná poloha dvou kružnic | znalost |  |  |  |

### Tělesa

`GEO.TEL` · catalog tag G-TEL · specification area 3 · In every standard test, mostly multiple choice 12–14. Several multi-step items score at the guessing rate.

| P | Skill | Kind | Needs | Examples | Note |
|---|---|---|---|---|---|
| 1 | Krychle a kvádr: objem, povrch, součet hran, i zpětně | postup | Strana nebo výška z obsahu (GEO.ROV) | [2025 D 12](../backend/data/screenshots/M9-2025-D-12.png) 29 % · [2025 C 13](../backend/data/screenshots/M9-2025-C-13.png) 26 % · [2026 C 7](../backend/data/screenshots/M9-2026-C-07.png) 16 % |  |
| 1 | Kolmý hranol: objem a povrch | postup | Vzorce pro obvod a obsah (GEO.ROV) | [2022 A 6](../backend/data/screenshots/M9-2022-A-06.png) 30 % · [2022 C 13](../backend/data/screenshots/M9-2022-C-13.png) 32 % · [2023 B 13](../backend/data/screenshots/M9-2023-B-13.png) 45 % · [2023 C 14](../backend/data/screenshots/M9-2023-C-14.png) 18 % · [2025 A 12](../backend/data/screenshots/M9-2025-A-12.png) 24 % · [2026 D 14](../backend/data/screenshots/M9-2026-D-14.png) 30 % | V = obsah podstavy × výška, for a triangular, rhombic or trapezoidal base. |
| 1 | Válec: objem, plášť, povrch | postup | Obvod a obsah kruhu (GEO.KRUH) | [2022 B 12](../backend/data/screenshots/M9-2022-B-12.png) 56 % · [2022 C 14](../backend/data/screenshots/M9-2022-C-14.png) 24 % · [2023 A 13](../backend/data/screenshots/M9-2023-A-13.png) 30 % · [2025 B 14](../backend/data/screenshots/M9-2025-B-14.png) 35 % · [2024 A 2](../backend/data/screenshots/M9-2024-A-02.png) 16 % | The plášť unrolled is a rectangle. |
| 3 | Síť tělesa | znalost | Kolmý hranol (GEO.TEL) | [2022 B 11](../backend/data/screenshots/M9-2022-B-11.png) 49 % · [2026 D 14](../backend/data/screenshots/M9-2026-D-14.png) 30 % |  |
| 2 | Slepená a rozříznutá tělesa | rozbor | Krychle a kvádr (GEO.TEL), Kolmý hranol (GEO.TEL) | [2022 D 13](../backend/data/screenshots/M9-2022-D-13.png) 24 % · [2022 D 14](../backend/data/screenshots/M9-2022-D-14.png) 34 % · [2025 A 11](../backend/data/screenshots/M9-2025-A-11.png) 54 % · [2026 B 13](../backend/data/screenshots/M9-2026-B-13.png) 22 % · [2024 C 11](../backend/data/screenshots/M9-2024-C-11.png) · [2023 D 14](../backend/data/screenshots/M9-2023-D-14.png) 14 % | The surface changes by the faces that disappear or appear. |
| 3 | Tělesa z krychliček, prostorová představivost | rozbor |  | [2025 B 13](../backend/data/screenshots/M9-2025-B-13.png) 25 % · [2026 A 15](../backend/data/screenshots/M9-2026-A-15.png) 56 % |  |
| 2 | Vztah místo čísla: rovnice pro výšku nebo hranu | rozbor | Válec (GEO.TEL), Rovnice se závorkami a desetinnými čísly (ALG.ROV) | [2023 A 13](../backend/data/screenshots/M9-2023-A-13.png) 30 % · [2026 A 14](../backend/data/screenshots/M9-2026-A-14.png) 33 % · [2022 C 14](../backend/data/screenshots/M9-2022-C-14.png) 24 % | „obsah pláště je třikrát větší než obsah podstavy“. |
| 2 | Objem v litrech, výška hladiny | postup | Válec (GEO.TEL), Objem a litry (krok × 1 000 (POC.JED) | [2025 A 6](../backend/data/screenshots/M9-2025-A-06.png) 18 % · [2024 C 2](../backend/data/screenshots/M9-2024-C-02.png) |  |
| S | Jehlan (promítání, síť, pohledy), koule (poloměr a průměr), pohledy na těleso, náčrt sítě | znalost |  |  | Volume and surface of a pyramid, cone or sphere are not in the specification. |

## Geometrie: konstrukce (KON)

Tasks 9 and 10 in every test, 5–6 points, 32 % success and 28 % blank. Learned as three layers: the moves, the properties, the reading of the task.

### Základní konstrukce

`KON.ZAKL` · catalog tag G-KON · specification area 3 · The moves with ruler, set square and compass. Each must be automatic.

| P | Skill | Kind | Needs | Examples | Note |
|---|---|---|---|---|---|
| 1 | Kolmice a rovnoběžka daným bodem | postup |  | [2022 B 10](../backend/data/screenshots/M9-2022-B-10.png) 26 % · [2022 C 10](../backend/data/screenshots/M9-2022-C-10.png) 23 % |  |
| 1 | Střed a osa úsečky | postup | Kolmice a rovnoběžka daným bodem (KON.ZAKL) | [2022 C 9](../backend/data/screenshots/M9-2022-C-09.png) 19 % · [2026 B 9](../backend/data/screenshots/M9-2026-B-09.png) 15 % |  |
| 3 | Osa úhlu | postup |  | [2025 A 9](../backend/data/screenshots/M9-2025-A-09.png) 33 % |  |
| 1 | Přenesení délky kružnicí | postup |  | [2022 B 9](../backend/data/screenshots/M9-2022-B-09.png) 72 % · [2022 D 10](../backend/data/screenshots/M9-2022-D-10.png) 14 % · [2026 A 9](../backend/data/screenshots/M9-2026-A-09.png) 42 % · [2023 C 9](../backend/data/screenshots/M9-2023-C-09.png) 21 % |  |
| 3 | Úhel dané velikosti | postup |  | [2022 D 9](../backend/data/screenshots/M9-2022-D-09.png) 21 % · [2023 D 10](../backend/data/screenshots/M9-2023-D-10.png) 22 % | 120° and 40° with a protractor; 60° and 90° without. |
| 1 | Thaletova kružnice nad úsečkou | postup | Střed a osa úsečky (KON.ZAKL) | [2023 B 10](../backend/data/screenshots/M9-2023-B-10.png) 43 % · [2024 C 9](../backend/data/screenshots/M9-2024-C-09.png) · [2024 D 9](../backend/data/screenshots/M9-2024-D-09.png) · [2026 B 10](../backend/data/screenshots/M9-2026-B-10.png) 22 % | Never named in the task; named in the official keys. |
| 1 | Obraz bodu ve středové souměrnosti („S je střed“) | postup | Přenesení délky kružnicí (KON.ZAKL) | [2022 A 9](../backend/data/screenshots/M9-2022-A-09.png) 31 % · [2022 D 9](../backend/data/screenshots/M9-2022-D-09.png) 21 % · [2025 C 10](../backend/data/screenshots/M9-2025-C-10.png) 12 % · [2025 D 10](../backend/data/screenshots/M9-2025-D-10.png) 4 % |  |
| 2 | Obraz v osové souměrnosti, osa z bodu a jeho obrazu | postup | Střed a osa úsečky (KON.ZAKL) | [2025 D 9](../backend/data/screenshots/M9-2025-D-09.png) 15 % · [2024 C 10](../backend/data/screenshots/M9-2024-C-10.png) |  |

### Vlastnosti útvarů, o které se konstrukce opírá

`KON.VLAST` · catalog tag G-KON · specification area 3 · The task never says which property to use; the student must recall it from the name of the figure.

| P | Skill | Kind | Needs | Examples | Note |
|---|---|---|---|---|---|
| 1 | Rovnoramenný trojúhelník: osa souměrnosti je osou základny | znalost | Střed a osa úsečky (KON.ZAKL) | [2022 A 9](../backend/data/screenshots/M9-2022-A-09.png) 31 % · [2022 B 9](../backend/data/screenshots/M9-2022-B-09.png) 72 % · [2023 C 10](../backend/data/screenshots/M9-2023-C-10.png) 17 % · [2025 B 9](../backend/data/screenshots/M9-2025-B-09.png) 19 % |  |
| 2 | Rovnostranný trojúhelník | znalost | Přenesení délky kružnicí (KON.ZAKL) | [2024 A 9](../backend/data/screenshots/M9-2024-A-09.png) 31 % · [2025 D 9](../backend/data/screenshots/M9-2025-D-09.png) 15 % |  |
| 1 | Pravoúhlý trojúhelník: vrchol pravého úhlu na Thaletově kružnici | znalost | Thaletova kružnice nad úsečkou (KON.ZAKL) | [2023 B 10](../backend/data/screenshots/M9-2023-B-10.png) 43 % · [2024 D 10](../backend/data/screenshots/M9-2024-D-10.png) · [2026 B 10](../backend/data/screenshots/M9-2026-B-10.png) 22 % |  |
| 2 | Výška a těžnice | znalost | Kolmice a rovnoběžka daným bodem (KON.ZAKL), Střed a osa úsečky (KON.ZAKL) | [2025 A 10](../backend/data/screenshots/M9-2025-A-10.png) 28 % · [2025 C 9](../backend/data/screenshots/M9-2025-C-09.png) 21 % |  |
| 2 | Čtverec: shodné, kolmé, půlící se úhlopříčky | znalost | Kolmice a rovnoběžka daným bodem (KON.ZAKL) | [2022 A 10](../backend/data/screenshots/M9-2022-A-10.png) 51 % · [2023 D 9](../backend/data/screenshots/M9-2023-D-09.png) 13 % |  |
| 1 | Obdélník: shodné půlící se úhlopříčky, vrcholy na kružnici | znalost | Thaletova kružnice nad úsečkou (KON.ZAKL) | [2023 A 9](../backend/data/screenshots/M9-2023-A-09.png) 32 % · [2026 C 10](../backend/data/screenshots/M9-2026-C-10.png) 25 % · [2026 D 10](../backend/data/screenshots/M9-2026-D-10.png) 16 % · [2024 D 9](../backend/data/screenshots/M9-2024-D-09.png) |  |
| 1 | Rovnoběžník: úhlopříčky se půlí, střed souměrnosti | znalost | Obraz bodu ve středové souměrnosti („S je střed“) (KON.ZAKL) | [2022 B 10](../backend/data/screenshots/M9-2022-B-10.png) 26 % · [2022 D 9](../backend/data/screenshots/M9-2022-D-09.png) 21 % · [2025 B 10](../backend/data/screenshots/M9-2025-B-10.png) 9 % · [2025 D 10](../backend/data/screenshots/M9-2025-D-10.png) 4 % |  |
| 2 | Kosočtverec: kolmé úhlopříčky, osa souměrnosti | znalost | Rovnoběžník (KON.VLAST) | [2024 B 9](../backend/data/screenshots/M9-2024-B-09.png) 32 % · [2026 A 10](../backend/data/screenshots/M9-2026-A-10.png) 23 % | 2026 A 10 never says „kosočtverec“; 53 % left it blank. |
| 2 | Lichoběžník: rovnoramenný a pravoúhlý | znalost | Kolmice a rovnoběžka daným bodem (KON.ZAKL) | [2023 B 9](../backend/data/screenshots/M9-2023-B-09.png) 64 % · [2023 C 9](../backend/data/screenshots/M9-2023-C-09.png) 21 % · [2024 C 10](../backend/data/screenshots/M9-2024-C-10.png) |  |
| 3 | Pravidelný šestiúhelník: strana = poloměr kružnice opsané | znalost | Přenesení délky kružnicí (KON.ZAKL) | [2026 B 9](../backend/data/screenshots/M9-2026-B-09.png) 15 % | Once in 20 tests. |

### Rozbor zadání

`KON.ROZBOR` · catalog tag G-KON · specification area 3 · Where the tasks are actually lost: the second construction is the most skipped regular task.

| P | Skill | Kind | Needs | Examples | Note |
|---|---|---|---|---|---|
| 1 | Náčrt a převod nepřímé podmínky na množinu bodů | rozbor | Rovnoramenný trojúhelník (KON.VLAST), Obdélník (KON.VLAST), Rovnoběžník (KON.VLAST) | [2022 C 9](../backend/data/screenshots/M9-2022-C-09.png) 19 % · [2023 A 9](../backend/data/screenshots/M9-2023-A-09.png) 32 % · [2025 A 10](../backend/data/screenshots/M9-2025-A-10.png) 28 % · [2026 A 10](../backend/data/screenshots/M9-2026-A-10.png) 23 % | „Přímka o je osou některé strany“, „Bod M leží na úhlopříčce BD“. |
| 1 | „Najděte všechna řešení“: druhé řešení | rozbor | Náčrt a převod nepřímé podmínky na množinu bodů (KON.ROZBOR) | [2022 A 9](../backend/data/screenshots/M9-2022-A-09.png) 31 % · [2023 D 9](../backend/data/screenshots/M9-2023-D-09.png) 13 % · [2026 A 9](../backend/data/screenshots/M9-2026-A-09.png) 42 % · [2025 C 10](../backend/data/screenshots/M9-2025-C-10.png) 12 % | 18 of 40 construction tasks; then exactly two figures. One of two costs a point. |
| 1 | Označení vrcholů a obtažení konstrukce | znalost |  |  | Letters on all vertices, the whole construction traced in pen, auxiliary lines left visible. |
| S | Trojúhelník podle sss, sus, usu; kružnice opsaná; tečna kružnice v jejím bodě | znalost |  |  |  |

### Souměrnost útvarů

`KON.SOUM` · catalog tag G-SOUM · specification area 3 · A task of its own in 4 of 16 standard tests; otherwise a tool inside constructions.

| P | Skill | Kind | Needs | Examples | Note |
|---|---|---|---|---|---|
| 3 | Osy souměrnosti útvaru ve čtvercové síti a mnohoúhelníků | znalost |  | [2022 D 11](../backend/data/screenshots/M9-2022-D-11.png) 53 % · [2023 D 8](../backend/data/screenshots/M9-2023-D-08.png) 37 % · [2026 C 8](../backend/data/screenshots/M9-2026-C-08.png) 29 % |  |
| S | Samodružný bod a útvar; vzor a obraz | znalost |  |  |  |

## Zákonitosti a úsudek (ZAK)

Task 16: 4 points, 10 % success, 36 % blank. No curriculum of its own; it is a way of working.

### Rostoucí obrazce a číselné řady

`ZAK.RADA` · catalog tag X-NEST · specification area 4

| P | Skill | Kind | Needs | Examples | Note |
|---|---|---|---|---|---|
| 1 | Pokračování pravidla a tabulka počtů po krocích | rozbor |  | [2022 B 16](../backend/data/screenshots/M9-2022-B-16.png) 10 % · [2025 A 16](../backend/data/screenshots/M9-2025-A-16.png) 5 % · [2023 D 16](../backend/data/screenshots/M9-2023-D-16.png) 9 % | Enough for 16.1, solved by 11–42 %. The cheapest point of task 16. |
| 2 | Obecný n-tý člen (lineární růst, n², n·(n + 1)/2) | rozbor | Pokračování pravidla a tabulka počtů po krocích (ZAK.RADA), Vyjádření veličiny výrazem s proměnnou (VZT.SLOV) | [2022 C 16](../backend/data/screenshots/M9-2022-C-16.png) 4 % · [2023 C 16](../backend/data/screenshots/M9-2023-C-16.png) 2 % · [2025 C 16](../backend/data/screenshots/M9-2025-C-16.png) 6 % · [2026 C 16](../backend/data/screenshots/M9-2026-C-16.png) 2 % | Use the differences between consecutive steps. Needed for 16.3, solved by 1–3 %. |
| 2 | Obrácení pravidla: který krok má daný počet | rozbor | Obecný n-tý člen (lineární růst (ZAK.RADA), Druhá mocnina a odmocnina (POC.VYR) | [2024 B 8](../backend/data/screenshots/M9-2024-B-08.png) 29 % | 361 = 19², so the 20th figure. |
| 3 | Růst násobením (mocniny tří) | rozbor | Pokračování pravidla a tabulka počtů po krocích (ZAK.RADA) | [2023 A 16](../backend/data/screenshots/M9-2023-A-16.png) 5 % | Once in 20 tests. |
| 3 | Číselná řada daná pravidlem | rozbor | Pokračování pravidla a tabulka počtů po krocích (ZAK.RADA) | [2022 D 16](../backend/data/screenshots/M9-2022-D-16.png) 13 % · [2025 B 16](../backend/data/screenshots/M9-2025-B-16.png) 12 % |  |

### Úsudek a systematické hledání

`ZAK.USUDEK` · catalog tag X-NEST · specification area 4

| P | Skill | Kind | Needs | Examples | Note |
|---|---|---|---|---|---|
| 2 | Periodické děje: cykly a společný násobek | rozbor | Společný násobek (POC.DEL) | [2022 A 16](../backend/data/screenshots/M9-2022-A-16.png) 22 % · [2026 A 16](../backend/data/screenshots/M9-2026-A-16.png) 11 % |  |
| 2 | Systematické vypsání všech řešení | rozbor |  | [2023 B 16](../backend/data/screenshots/M9-2023-B-16.png) 6 % · [2026 D 16](../backend/data/screenshots/M9-2026-D-16.png) 10 % · [2025 D 7](../backend/data/screenshots/M9-2025-D-07.png) 16 % · [2023 D 8](../backend/data/screenshots/M9-2023-D-08.png) 37 % |  |
| 3 | Strategické a netradiční geometrické úlohy | rozbor |  | [2025 D 16](../backend/data/screenshots/M9-2025-D-16.png) 7 % · [2026 D 16](../backend/data/screenshots/M9-2026-D-16.png) 10 % |  |
