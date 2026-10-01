# What to learn for M9: every topic, how deep, and how CERMAT tests it

Subject: the *didaktický test z matematiky* of the JPZ for four-year programs (`M9`). This file answers one
question: **what exactly must a student be able to do to lose no point**, topic by topic, with real tasks
from the problem database as evidence.

Written October 2026. Companions: [01_baseline_M9.md](01_baseline_M9.md) (how the test is built and scored),
[02_katalog_uloh.md](02_katalog_uloh.md) (all 320 tasks in test order).

## How to read this file

- **Every task reference is a link to the task's screenshot**, followed by CERMAT's success rate for it and,
  in the example lists, a link to the official solution (*řešení*) and a one-line description. Example:
  [2025 B 15.2](../backend/data/screenshots/M9-2025-B-15.png) (12 %) means year 2025, term B, task 15, sub-item 2, and the share of candidates who solved it.
- The images live in `backend/data/screenshots/` (not in git). If the links are dead, build them once:
  `uv run --project backend python backend/try_problem_db.py build`. The same tasks can be filtered by
  topic, year, format and success rate in the problem database page.
- Success rates: a task-level number is the average % score on the whole task; a sub-item number
  (2025 B 15.2) is for that sub-item. Terms A and B were sat by 67 000–95 000 candidates; **C and D by a
  few hundred, so their percentages are noisy**. 2024 C and D have no published results.
- "Standard tests" = the 16 tests of 2022, 2023, 2025, 2026. The four 2024 tests follow a different design
  (baseline, section 3) and are counted separately.
- Each topic section has the same four parts: **Must know** (the checklist), **How it is tested**
  (position, format, wording), **Where points are lost**, **Examples** grouped by sub-skill, and at the end
  a line with every task in the database that carries the topic's tag.

Evidence and its limits:

- "Must know" items marked **[seen]** are backed by tasks I read in the 20 booklets: 18 from the extracted
  text in the database, 2024 A and B from the screenshots. Items marked **[spec only]** are required by
  CERMAT's specification (`References/MASPECIFIKACEPOZADAVKU2022 (1).pdf`, part C1, which includes A1 and
  B1) but did not occur in these 20 tests. A perfect score cannot be guaranteed without them, because
  CERMAT may use anything in the specification.
- Topic boundaries and tags are mine, not CERMAT's. Point averages and success rates per topic are taken
  from the baseline (section 5) and are for the standard tests, regular terms.
- Which solving method a task needs is my reading of the task; where the official key names the method
  (for example *Thaletova kružnice*) I say so.
- Not checked: tests before 2022, and whether the specification still applies unchanged in 2026/2027.

## Contents

| # | Topic | Tag | Points per standard test | In how many of 16 | Success | Typical position |
|---|---|---|---|---|---|---|
| 0 | [Before the topics: what is printed, what must be memorized, how answers must look](#t0) | | | | | |
| 1 | [Číselné výrazy, mocniny, odmocniny](#t1) | N-ARIT | 1,4 | 13 | 60 % | tasks 1–2, inside the fraction task |
| 2 | [Zlomky](#t2) | N-ZLOM | 5,2 | 16 | 47 % | task 3 (2022–25), task 2 (2025 A, 2026) + word problems |
| 3 | [Dělitelnost, prvočísla](#t3) | N-DEL | 0,6 | 6 | 19 % | anywhere, usually hidden in a word problem |
| 4 | [Převody jednotek, čas](#t4) | N-JED | 0,6 | 8 | 44 % | task 1–2, and embedded in geometry |
| 5 | [Úpravy výrazů](#t5) | A-VYR | 4,0 | 16 | 50 % | task 4 (task 3 in 2025 A, 2026) |
| 6 | [Lineární rovnice a soustavy](#t6) | A-ROV, A-SOU | 4,0 | 16 | 52 % | task 5 (task 4 in 2025 A, 2026) |
| 7 | [Výraz s proměnnou, slovní úlohy na rovnici](#t7) | A-SLOV | 3,0 | 15 | 32 % | one of tasks 5–8, one multiple choice |
| 8 | [Procenta](#t8) | P-PROC | 6,6 | 16 | 44 % | task 15 always, plus 1–2 other items |
| 9 | [Poměr, úměrnost, měřítko, práce, pohyb](#t9) | P-POM | 3,3 | 14 | 37 % | tasks 6–8, task 11, multiple choice |
| 10 | [Grafy, tabulky, aritmetický průměr](#t10) | D-GRAF | 2,8 | 14 | 52 % | task 11 (A/N) in 9 of 16, tasks 7, 14 |
| 11 | [Úhly](#t11) | G-UHLY | 2,1 | 14 | 48 % | one of tasks 12–14, sometimes 7–8 |
| 12 | [Obvod a obsah rovinných útvarů](#t12) | G-ROV | 2,2 | 14 | 32 % | tasks 6–8, multiple choice |
| 13 | [Pythagorova věta](#t13) | G-PYT | 1,0 | 11 | 40 % | never alone; inside areas and solids |
| 14 | [Kruh, kružnice, π](#t14) | G-KRUH | 0,9 | 9 | 35 % | tasks 7–8, 12–14 |
| 15 | [Tělesa](#t15) | G-TEL | 3,1 | 16 | 39 % | tasks 12–14, 11, 6–7 |
| 16 | [Konstrukční úlohy](#t16) | G-KON | 5,2 | 16 | 32 % | tasks 9 and 10, always |
| 17 | [Souměrnost](#t17) | G-SOUM | 0,7 | 4 | – | inside constructions; twice on a square grid |
| 18 | [Nestandardní úlohy, zákonitosti](#t18) | X-NEST | 3,6 | 16 | 10 % | task 16 |
| 19 | [In the specification, not seen in 2022–2026](#t19) | | | | | |
| 20 | [The language of the tasks: phrase → mathematics](#t20) | | | | | |

Three facts decide where to spend time:

1. **Topics 2, 5, 6, 8, 16 and 18 are in every standard test** and are worth 28–29 of 50 points together.
   Add solids (15), also in every test, and it is about 32.
2. **The last points are in task 16, the second construction and the last sub-item of tasks 6–8.** Those are
   the items solved by 1–20 % of candidates; a perfect score is mostly decided there.
3. **Nothing in the 20 tests needs a calculator-sized computation.** Numbers are built to come out as
   integers, simple fractions or one decimal. A result that is ugly is almost always wrong.

---

<a id="t0"></a>
## 0. Before the topics

### What is printed in the booklet, and what is not

Printed in all 20 booklets (and prescribed by the specification, part C2):

- 11² = 121, 12² = 144, 13² = 169, 14² = 196, 15² = 225, 16² = 256, 17² = 289, 18² = 324, 19² = 361, 20² = 400
- π ≐ 3,14 and π ≈ 22/7
- a² + 2ab + b² = (a + b)(a + b), a² − 2ab + b² = (a − b)(a − b), a² − b² = (a + b)(a − b)
- circle: o = 2πr, S = πr²

Not printed, and needed in the tasks of these 20 tests, so it must be known by heart:

| What | Needed for example in |
|---|---|
| Squares of 1–10 and their roots; roots of the squares in the box read backwards (√144, √225, √289) | [2023 B 1](../backend/data/screenshots/M9-2023-B-01.png) (65 %), [2023 B 8](../backend/data/screenshots/M9-2023-B-08.png) (24 %), [2022 D 13](../backend/data/screenshots/M9-2022-D-13.png) (25 %) |
| Pythagorova věta, c² = a² + b² | [2022 C 8](../backend/data/screenshots/M9-2022-C-08.png) (30 %), [2026 A 13](../backend/data/screenshots/M9-2026-A-13.png) (34 %), [2023 A 12](../backend/data/screenshots/M9-2023-A-12.png) (39 %) |
| Area: rectangle a·b, triangle a·v/2, parallelogram a·v, trapezoid (a + c)·v/2 | [2023 A 6](../backend/data/screenshots/M9-2023-A-06.png) (25 %), [2022 D 8](../backend/data/screenshots/M9-2022-D-08.png) (16 %), [2025 B 8](../backend/data/screenshots/M9-2025-B-08.png) (32 %) |
| Volume of any prism and of a cylinder: V = S_p · v (base area × height); cylinder V = πr²v | [2022 A 6](../backend/data/screenshots/M9-2022-A-06.png) (30 %), [2023 B 13](../backend/data/screenshots/M9-2023-B-13.png) (45 %), [2023 C 7](../backend/data/screenshots/M9-2023-C-07.png) (19 %) |
| Surface: sum of all faces; cylinder plášť = 2πr·v, S = 2πr² + 2πrv | [2022 C 14](../backend/data/screenshots/M9-2022-C-14.png) (24 %), [2023 A 13](../backend/data/screenshots/M9-2023-A-13.png) (30 %), [2026 A 14](../backend/data/screenshots/M9-2026-A-14.png) (33 %) |
| Angle sums: triangle 180°, quadrilateral 360°, straight angle 180°; equilateral triangle 60° | [2022 D 12](../backend/data/screenshots/M9-2022-D-12.png) (32 %), [2023 C 13](../backend/data/screenshots/M9-2023-C-13.png) (21 %) |
| Units: 1 l = 1 dm³ = 1 000 cm³, 1 ml = 1 cm³, 1 m² = 100 dm² = 10 000 cm², 1 dm³ = 1 000 000 mm³ | [2025 A 6](../backend/data/screenshots/M9-2025-A-06.png) (18 %), [2026 B 1](../backend/data/screenshots/M9-2026-B-01.png) (41 %), [2022 A 2](../backend/data/screenshots/M9-2022-A-02.png) (34 %) |
| Percent: 1 % = 1/100; fraction ↔ percent (1/20 = 5 %, 1/4 = 25 %, 1/3 ≐ 33 %, 2/5 = 40 %) | [2022 D 15](../backend/data/screenshots/M9-2022-D-15.png) (41 %), [2026 A 12](../backend/data/screenshots/M9-2026-A-12.png) (50 %) |
| s = v·t, including minutes ↔ hours | [2025 C 7](../backend/data/screenshots/M9-2025-C-07.png) (20 %), [2026 A 7](../backend/data/screenshots/M9-2026-A-07.png) (28 %) |
| Aritmetický průměr = sum / count | [2022 B 7](../backend/data/screenshots/M9-2022-B-07.png) (50 %), [2025 A 14](../backend/data/screenshots/M9-2025-A-14.png) (36 %) |

Aids: "pouze psací a rýsovací potřeby" – pen, pencil, ruler, set square with a perpendicular line
(*trojúhelník s ryskou*), compass, protractor (*úhloměr*; the specification lists it, and
[2023 D 10](../backend/data/screenshots/M9-2023-D-10.png) (22 %) asks for a 40° angle). No calculator, no tables.

### How answers must look (rules that cost points regardless of topic)

Taken from the task wording and the official keys; details and sources in the baseline, section 4.

- **"zlomkem v základním tvaru"** – an unreduced fraction costs 1 of 2 points in the worked items.
- **"výsledný výraz nesmí obsahovat závorky"**, "upravte na co nejjednodušší tvar" – like terms must be collected.
- **Worked items** ("uveďte celý postup řešení"): only the result = 0 points. Exactly one error = 1 of 2 points.
- **Units**: the question names the unit ("Vypočtěte v cm", "kolik litrů", "v minutách"). A correct number in
  the wrong unit gets at most a partial point, and only where the key says so.
- **Rounding**: "Výsledek zaokrouhlete na desítky cm³ / celé cm² / desetiny centimetru" – compute with
  π ≐ 3,14 and round only the final result ([2023 B 8](../backend/data/screenshots/M9-2023-B-08.png) (24 %), [2026 B 7](../backend/data/screenshots/M9-2026-B-07.png) (31 %), [2024 A 8](../backend/data/screenshots/M9-2024-A-08.png) (22 %)).
- **"Najděte všechna řešení" / "Uveďte všechna řešení" / "obě řešení"** – one missing or one extra wrong solution
  costs half. In constructions it means two figures (18 of 40 construction tasks).
- **Constructions**: vertices labelled with letters, the whole construction traced in pen
  ("obtáhněte celou konstrukci propisovací tužkou (čáry i písmena)"), auxiliary lines left visible.
- **Ratios** "zapište v základním tvaru" ([2022 B 2](../backend/data/screenshots/M9-2022-B-02.png) (24 %), [2025 D 6](../backend/data/screenshots/M9-2025-D-06.png) (23 %), [2026 D 7](../backend/data/screenshots/M9-2026-D-07.png) (13 %)); time "ve tvaru hodiny : minuty" ([2026 C 1](../backend/data/screenshots/M9-2026-C-01.png) (40 %)).
- **Closed tasks**: no penalty for a wrong answer, so never leave them blank. "jiný výsledek / jiná velikost"
  was never the keyed answer in these 20 tests; a range option ("větší než 120°") was ([2022 D 12](../backend/data/screenshots/M9-2022-D-12.png) (32 %)).

---

<a id="t1"></a>
## 1. Číselné výrazy, mocniny, odmocniny (N-ARIT)

1,4 points per standard test · in 13 of 16 · success 60 % · not in the 2024 tests as a separate item.

**Must know**

- [seen] Order of operations with brackets, negative numbers and the sign rules: (−6)² = 36, −3·(−3) = +9, 6 : 2 before +.
- [seen] Decimal arithmetic by hand, including multiplying and dividing by decimals: (0,08 − 1) : 0,2; 0,5 · (−0,04); 100 · 0,02.
- [seen] Second power and square root of integers (1–20), of decimals (1,3² = 1,69; √0,25 = 0,5) and of powers of ten.
- [seen] Root and power of a fraction and of a product: √(a·b) = √a·√b, (3/5)² = 9/25, √(25/4) = 5/2 – used with mixed numbers in [2025 B 2](../backend/data/screenshots/M9-2025-B-02.png) (34 %).
- [seen] A root of an expression is computed inside first: √(100 − 64) = √36 = 6, not 10 − 8. √(5² − 4²) = 3.
- [seen] Words to expression: *součet, rozdíl, součin, podíl, druhá mocnina, druhá odmocnina, kolikrát větší, o kolik větší*.
- [seen] Reading a number line with equal divisions, also with a ratio ([2022 B 2](../backend/data/screenshots/M9-2022-B-02.png) (24 %), [2023 D 2](../backend/data/screenshots/M9-2023-D-02.png) (25 %)).
- [seen] Value of an expression for a given number ([2026 A 3](../backend/data/screenshots/M9-2026-A-03.png) (48 %): 9a² − 6a + 1 for a = 7, fastest as (3a − 1)² = 20²).
- [spec only] *Absolutní hodnota*, *opačné číslo*; periodic decimals (*periodické číslo*) and converting a fraction to one; rounding to a given place as a task of its own; estimates.

**How it is tested.** One or two result-only items worth 1 point at the very start ("Vypočtěte:"). From
2025 roots and powers also sit inside the fraction task. Only second powers and second roots occur; no
higher powers, no rules for powers with exponents, no partial root extraction.

**Where points are lost.** The verbal items, not the computations: "kolikrát je součet čísel 0,2 a 0,5
větší než jejich součin" was solved by 28 % ([2023 C 1](../backend/data/screenshots/M9-2023-C-01.png) (28 %)), the plain expressions by 65–82 %.

**Examples**

*Sign rules and order of operations*
- [2022 B 1](../backend/data/screenshots/M9-2022-B-01.png) · 68 % · [řešení](../backend/data/screenshots/M9-2022-B-01-reseni.png) — Číselný výraz se zápornými čísly a mocninou
- [2022 D 2](../backend/data/screenshots/M9-2022-D-02.png) · 28 % · [řešení](../backend/data/screenshots/M9-2022-D-02-reseni.png) — Výraz se zápornými čísly a mocninami; výraz s desetinnými čísly
- [2023 C 2](../backend/data/screenshots/M9-2023-C-02.png) · 44 % · [řešení](../backend/data/screenshots/M9-2023-C-02-reseni.png) — Pořadí operací; odmocnina z rozdílu mocnin desetinných čísel

*Powers, roots, powers of ten*
- [2022 A 1](../backend/data/screenshots/M9-2022-A-01.png) · 82 % · [řešení](../backend/data/screenshots/M9-2022-A-01-reseni.png) — Číselný výraz s druhou mocninou a odmocninou ve zlomku
- [2023 B 1](../backend/data/screenshots/M9-2023-B-01.png) · 65 % · [řešení](../backend/data/screenshots/M9-2023-B-01-reseni.png) — Odmocnina z rozdílu druhých mocnin
- [2022 C 1](../backend/data/screenshots/M9-2022-C-01.png) · 52 % · [řešení](../backend/data/screenshots/M9-2022-C-01-reseni.png) — Číselný výraz s mocninami 10 (zlomek)
- [2025 B 2](../backend/data/screenshots/M9-2025-B-02.png) · 34 % · [řešení](../backend/data/screenshots/M9-2025-B-02-reseni.png) — Odmocnina ze součinu smíšených čísel

*Decimals*
- [2026 A 2](../backend/data/screenshots/M9-2026-A-02.png) · 58 % · [řešení](../backend/data/screenshots/M9-2026-A-02-reseni.png) — 2.1: (−1,5 − 1) · (−1,5 + 1)
- [2026 D 2](../backend/data/screenshots/M9-2026-D-02.png) · 40 % · [řešení](../backend/data/screenshots/M9-2026-D-02-reseni.png) — 2.1: 0,5 · (−0,04) − 100 · 0,02

*Expression given in words; number line*
- [2023 C 1](../backend/data/screenshots/M9-2023-C-01.png) · 28 % · [řešení](../backend/data/screenshots/M9-2023-C-01-reseni.png) — Kolikrát je součet čísel 0,2 a 0,5 větší než jejich součin
- [2025 A 1](../backend/data/screenshots/M9-2025-A-01.png) · 44 % · [řešení](../backend/data/screenshots/M9-2025-A-01-reseni.png) — Slovně zadaný výraz: součet čísel vs. odmocnina ze součinu
- [2023 D 2](../backend/data/screenshots/M9-2023-D-02.png) · 25 % · [řešení](../backend/data/screenshots/M9-2023-D-02-reseni.png) — Číselná osa se stejnými dílky – určení čísel

All 16 tasks tagged `N-ARIT`: **2022** [A 1](../backend/data/screenshots/M9-2022-A-01.png), [B 1](../backend/data/screenshots/M9-2022-B-01.png), [C 1](../backend/data/screenshots/M9-2022-C-01.png), [D 2](../backend/data/screenshots/M9-2022-D-02.png) · **2023** [B 1](../backend/data/screenshots/M9-2023-B-01.png), [C 1](../backend/data/screenshots/M9-2023-C-01.png), [C 2](../backend/data/screenshots/M9-2023-C-02.png), [D 2](../backend/data/screenshots/M9-2023-D-02.png) · **2025** [A 1](../backend/data/screenshots/M9-2025-A-01.png), [A 2](../backend/data/screenshots/M9-2025-A-02.png), [B 2](../backend/data/screenshots/M9-2025-B-02.png), [B 3](../backend/data/screenshots/M9-2025-B-03.png), [C 3](../backend/data/screenshots/M9-2025-C-03.png), [D 3](../backend/data/screenshots/M9-2025-D-03.png) · **2026** [A 2](../backend/data/screenshots/M9-2026-A-02.png), [D 2](../backend/data/screenshots/M9-2026-D-02.png)

---

<a id="t2"></a>
## 2. Zlomky (N-ZLOM)

5,2 points per standard test · in 16 of 16 · success 47 % · 3–4 points in the computation task plus fraction word problems.

**Must know**

- [seen] All four operations with fractions, with whole numbers and with negative fractions; brackets and order of operations.
- [seen] Common denominator by least common multiple; cancelling before multiplying (7/5 · 3/8 · 10/21).
- [seen] Dividing by a fraction and by a whole number (5/9 : 5; 1 : 6/5).
- [seen] *Složený zlomek*: simplify numerator and denominator separately, then divide. It is the worked item in almost every test.
- [seen] Mixing fractions with decimals: convert the decimal (1,4 = 7/5; 0,3 = 3/10; 3,3 = 33/10; −5,5 = −11/2).
- [seen] From 2025: second powers and roots inside the fraction expression ((3/5)², √25, √(100 − 64), √(5² − 4²)).
- [seen] *Smíšené číslo* ↔ improper fraction ([2025 B 2](../backend/data/screenshots/M9-2025-B-02.png) (34 %)).
- [seen] Result as a fraction in *základní tvar*; from 2026 "nebo celým číslem". Negative results are common.
- [seen] Fraction of a quantity, also of time and of a remainder ("dvě pětiny zbytku"); finding the whole from a part ("pětina a o 180 více"); comparing fractions of different wholes.
- [seen] "o třetinu více / méně", "o čtvrtinu kratší" as multiplying by 4/3, 2/3, 3/4 – and backwards: a quantity that is "o třetinu větší" and equals 360 means the original is 360 : 4/3 = 270 ([2026 A 5](../backend/data/screenshots/M9-2026-A-05.png) (28 %)).
- [spec only] Comparing and ordering fractions as a task of its own; *převrácený zlomek* by name; fraction → periodic decimal.

**How it is tested.** "Vypočtěte a výsledek zapište zlomkem v základním tvaru." 2022: two worked items,
2 + 2 points. 2023 and 2026: three items, 1 + 1 result-only and one worked *složený zlomek* for 2 points.
2025: two items, 1 + 2. 2024: two worked items, each mixing fractions and decimals. Three to five
operations per item; denominators are small (mostly up to 28) and chosen so that the fractions cancel.

**Where points are lost.** The computation task is among the best solved open tasks (58–76 % in regular
terms), and the key gives 1 of 2 points for exactly one slip or for an unreduced result. It gives 0 for an
"algoritmicky chybná operace se zlomky" and for multiplying the whole expression by the common
denominator as if it were an equation. The word problems are much harder: [2023 A 1](../backend/data/screenshots/M9-2023-A-01.png) (33 %), [2025 B 1](../backend/data/screenshots/M9-2025-B-01.png) (33 %),
[2026 A 5](../backend/data/screenshots/M9-2026-A-05.png) (28 %) and [2025 D 1](../backend/data/screenshots/M9-2025-D-01.png) (21 %) are single 1-point items solved by 21–33 %.

**Examples**

*The computation task, by year design*
- [2022 A 3](../backend/data/screenshots/M9-2022-A-03.png) · 65 % · [řešení](../backend/data/screenshots/M9-2022-A-03-reseni.png) — Dva výrazy se zlomky (závorka; složený zlomek), výsledek v základním tvaru
- [2022 B 3](../backend/data/screenshots/M9-2022-B-03.png) · 76 % · [řešení](../backend/data/screenshots/M9-2022-B-03-reseni.png) — Dva výrazy se zlomky (součin a součet; složený zlomek)
- [2023 A 3](../backend/data/screenshots/M9-2023-A-03.png) · 60 % · [řešení](../backend/data/screenshots/M9-2023-A-03-reseni.png) — Tři výrazy se zlomky (poslední složený, s postupem)
- [2023 B 3](../backend/data/screenshots/M9-2023-B-03.png) · 72 % · [řešení](../backend/data/screenshots/M9-2023-B-03-reseni.png) — Tři výrazy se zlomky
- [2026 B 2](../backend/data/screenshots/M9-2026-B-02.png) · 67 % · [řešení](../backend/data/screenshots/M9-2026-B-02-reseni.png) — Tři výrazy se zlomky (poslední složený, s postupem)
- [2026 D 2](../backend/data/screenshots/M9-2026-D-02.png) · 40 % · [řešení](../backend/data/screenshots/M9-2026-D-02-reseni.png) — Výraz s desetinnými čísly; dva výrazy se zlomky

*With decimals (all four 2024 tests, 2026 C)*
- [2024 A 3](../backend/data/screenshots/M9-2024-A-03.png) · 63 % · [řešení](../backend/data/screenshots/M9-2024-A-03-reseni.png) — 3.2: (13/10 − 1,4) over (2/15 + 1/6)
- [2024 C 3](../backend/data/screenshots/M9-2024-C-03.png) · [řešení](../backend/data/screenshots/M9-2024-C-03-reseni.png) — 3.1: (7/5 + 3,3 − 1/2) over (1/15 + 1/3)
- [2024 D 3](../backend/data/screenshots/M9-2024-D-03.png) · [řešení](../backend/data/screenshots/M9-2024-D-03-reseni.png) — 3.1: a bracket divided by −5/3, all over 0,3
- [2026 C 2](../backend/data/screenshots/M9-2026-C-02.png) · 47 % · [řešení](../backend/data/screenshots/M9-2026-C-02-reseni.png) — 2.2: 5/44 · (−5,5)

*With powers and roots (2025)*
- [2025 A 2](../backend/data/screenshots/M9-2025-A-02.png) · 59 % · [řešení](../backend/data/screenshots/M9-2025-A-02-reseni.png) — Výraz se zlomky; složený zlomek s odmocninami
- [2025 B 3](../backend/data/screenshots/M9-2025-B-03.png) · 66 % · [řešení](../backend/data/screenshots/M9-2025-B-03-reseni.png) — Výraz se zlomky; výraz s odmocninami a zlomky
- [2025 C 3](../backend/data/screenshots/M9-2025-C-03.png) · 40 % · [řešení](../backend/data/screenshots/M9-2025-C-03-reseni.png) — Výraz s odmocninami; složený zlomek s mocninami
- [2025 D 3](../backend/data/screenshots/M9-2025-D-03.png) · 35 % · [řešení](../backend/data/screenshots/M9-2025-D-03-reseni.png) — Výraz se zlomky; složený zlomek s mocninou a odmocninou

*Fraction of a quantity, of time, of a remainder*
- [2022 A 11](../backend/data/screenshots/M9-2022-A-11.png) · 74 % · [řešení](../backend/data/screenshots/M9-2022-A-11-reseni.png) — Zlomky z časových údajů (minuty, hodiny, dny)
- [2022 C 2](../backend/data/screenshots/M9-2022-C-02.png) · 49 % · [řešení](../backend/data/screenshots/M9-2022-C-02-reseni.png) — 2.2: tři pětiny z 1 hodiny 50 minut
- [2023 A 1](../backend/data/screenshots/M9-2023-A-01.png) · 33 % · [řešení](../backend/data/screenshots/M9-2023-A-01-reseni.png) — Film trvá 1 hodinu, zbývá polovina uplynulé doby
- [2025 D 1](../backend/data/screenshots/M9-2025-D-01.png) · 21 % · [řešení](../backend/data/screenshots/M9-2025-D-01-reseni.png) — Stuha – čtvrtina a dvě pětiny zbytku
- [2026 A 1](../backend/data/screenshots/M9-2026-A-01.png) · 64 % · [řešení](../backend/data/screenshots/M9-2026-A-01-reseni.png) — sum, quotient and arithmetic mean of two fractions

*Finding the whole from parts*
- [2022 B 6](../backend/data/screenshots/M9-2022-B-06.png) · 32 % · [řešení](../backend/data/screenshots/M9-2022-B-06-reseni.png) — Kuličky tří barev: čtvrtina, šestina, „o 20 více“ – celek a rozdíl
- [2023 B 14](../backend/data/screenshots/M9-2023-B-14.png) · 33 % · [řešení](../backend/data/screenshots/M9-2023-B-14-reseni.png) — Pomlázky: pětina a „o 180 více“
- [2023 C 12](../backend/data/screenshots/M9-2023-C-12.png) · 40 % · [řešení](../backend/data/screenshots/M9-2023-C-12-reseni.png) — Lokomotiva a vagony – zlomky délky
- [2025 B 1](../backend/data/screenshots/M9-2025-B-01.png) · 33 % · [řešení](../backend/data/screenshots/M9-2025-B-01-reseni.png) — Vstupenky – dvě pětiny ceny
- [2026 A 5](../backend/data/screenshots/M9-2026-A-05.png) · 28 % · [řešení](../backend/data/screenshots/M9-2026-A-05-reseni.png) — „O třetinu větší objem“ – zpětný výpočet
- [2026 B 14](../backend/data/screenshots/M9-2026-B-14.png) · 39 % · [řešení](../backend/data/screenshots/M9-2026-B-14-reseni.png) — Hrnky a kanystr – sedm osmin objemu

All 43 tasks tagged `N-ZLOM`: **2022** [A 3](../backend/data/screenshots/M9-2022-A-03.png), [A 11](../backend/data/screenshots/M9-2022-A-11.png), [B 3](../backend/data/screenshots/M9-2022-B-03.png), [B 6](../backend/data/screenshots/M9-2022-B-06.png), [C 2](../backend/data/screenshots/M9-2022-C-02.png), [C 3](../backend/data/screenshots/M9-2022-C-03.png), [D 3](../backend/data/screenshots/M9-2022-D-03.png), [D 15](../backend/data/screenshots/M9-2022-D-15.png) · **2023** [A 1](../backend/data/screenshots/M9-2023-A-01.png), [A 3](../backend/data/screenshots/M9-2023-A-03.png), [B 3](../backend/data/screenshots/M9-2023-B-03.png), [B 14](../backend/data/screenshots/M9-2023-B-14.png), [B 15](../backend/data/screenshots/M9-2023-B-15.png), [C 3](../backend/data/screenshots/M9-2023-C-03.png), [C 12](../backend/data/screenshots/M9-2023-C-12.png), [D 3](../backend/data/screenshots/M9-2023-D-03.png) · **2024** [A 3](../backend/data/screenshots/M9-2024-A-03.png), [B 3](../backend/data/screenshots/M9-2024-B-03.png), [C 3](../backend/data/screenshots/M9-2024-C-03.png), [C 14](../backend/data/screenshots/M9-2024-C-14.png), [D 3](../backend/data/screenshots/M9-2024-D-03.png) · **2025** [A 2](../backend/data/screenshots/M9-2025-A-02.png), [A 8](../backend/data/screenshots/M9-2025-A-08.png), [B 1](../backend/data/screenshots/M9-2025-B-01.png), [B 2](../backend/data/screenshots/M9-2025-B-02.png), [B 3](../backend/data/screenshots/M9-2025-B-03.png), [B 7](../backend/data/screenshots/M9-2025-B-07.png), [C 3](../backend/data/screenshots/M9-2025-C-03.png), [D 1](../backend/data/screenshots/M9-2025-D-01.png), [D 3](../backend/data/screenshots/M9-2025-D-03.png), [D 15](../backend/data/screenshots/M9-2025-D-15.png) · **2026** [A 1](../backend/data/screenshots/M9-2026-A-01.png), [A 2](../backend/data/screenshots/M9-2026-A-02.png), [A 5](../backend/data/screenshots/M9-2026-A-05.png), [A 6](../backend/data/screenshots/M9-2026-A-06.png), [A 12](../backend/data/screenshots/M9-2026-A-12.png), [B 2](../backend/data/screenshots/M9-2026-B-02.png), [B 14](../backend/data/screenshots/M9-2026-B-14.png), [B 16](../backend/data/screenshots/M9-2026-B-16.png), [C 2](../backend/data/screenshots/M9-2026-C-02.png), [C 14](../backend/data/screenshots/M9-2026-C-14.png), [D 2](../backend/data/screenshots/M9-2026-D-02.png), [D 7](../backend/data/screenshots/M9-2026-D-07.png)

---

<a id="t3"></a>
## 3. Dělitelnost, prvočísla (N-DEL)

0,6 points per standard test · in 6 of 16 · success 19 % · the worst solved of the small topics.

**Must know**

- [seen] *Dělitel*, *násobek*, *prvočíslo*, *číslo složené*; listing all divisors of a number (95 = 5 · 19).
- [seen] *Rozklad na prvočísla* (231 = 3 · 7 · 11) and building divisors from the prime factors (largest two-digit divisor of 231 is 77).
- [seen] The small primes by heart, and the fact that 2 is the only even prime ([2025 C 2](../backend/data/screenshots/M9-2025-C-02.png) (11 %): p² + 3 is prime only for p = 2).
- [seen] Division with a remainder in a word problem ([2026 D 13](../backend/data/screenshots/M9-2026-D-13.png) (27 %)) and common multiples in periodic processes ("v každém 4. kole", "v každé páté sekundě": [2022 A 16](../backend/data/screenshots/M9-2022-A-16.png) (22 %), [2026 A 16](../backend/data/screenshots/M9-2026-A-16.png) (11 %)).
- [seen] Using factorizations to make products equal ([2026 B 12](../backend/data/screenshots/M9-2026-B-12.png) (20 %)).
- [spec only, by name] *Znaky dělitelnosti* 2, 3, 4, 5, 6, 8, 10; *nejmenší společný násobek* and *největší společný dělitel* of two or three numbers; word problems named as divisibility problems. The words NSN and NSD do not occur in the 20 tests, but the least common multiple is what the fraction task and the periodic tasks use.

**How it is tested.** Never announced as a divisibility topic except for the three direct items below. All
of them are short and result-only.

**Where points are lost.** Everywhere: "Vypište všechny dělitele čísla 95, které jsou větší než 1 a menší
než 95" got 14 % ([2022 D 1](../backend/data/screenshots/M9-2022-D-01.png) (14 %)), the prime puzzle 11 % ([2025 C 2](../backend/data/screenshots/M9-2025-C-02.png) (11 %)), the product diagram 20 % with a 20 %
guessing rate ([2026 B 12](../backend/data/screenshots/M9-2026-B-12.png) (20 %)).

**Examples**

- [2022 D 1](../backend/data/screenshots/M9-2022-D-01.png) · 14 % · [řešení](../backend/data/screenshots/M9-2022-D-01-reseni.png) — Dělitelé čísla 95
- [2025 B 6](../backend/data/screenshots/M9-2025-B-06.png) · 27 % · [řešení](../backend/data/screenshots/M9-2025-B-06-reseni.png) — Rozklad čísla 231 na prvočísla, dělitelé
- [2025 C 2](../backend/data/screenshots/M9-2025-C-02.png) · 11 % · [řešení](../backend/data/screenshots/M9-2025-C-02-reseni.png) — Prvočísla – druhá mocnina o 3 menší než jiné prvočíslo
- [2026 B 12](../backend/data/screenshots/M9-2026-B-12.png) · 20 % · [řešení](../backend/data/screenshots/M9-2026-B-12-reseni.png) — Trojúhelníkový diagram – stejný součin čísel na stranách
- [2026 D 13](../backend/data/screenshots/M9-2026-D-13.png) · 27 % · [řešení](../backend/data/screenshots/M9-2026-D-13-reseni.png) — Dělení do trojic a pětic – zbytek
- [2025 A 8](../backend/data/screenshots/M9-2025-A-08.png) · 13 % · [řešení](../backend/data/screenshots/M9-2025-A-08-reseni.png) — 8.3: smallest possible number of plants in a repeating pattern around a perimeter

All 6 tasks tagged `N-DEL`: **2022** [D 1](../backend/data/screenshots/M9-2022-D-01.png) · **2025** [A 8](../backend/data/screenshots/M9-2025-A-08.png), [B 6](../backend/data/screenshots/M9-2025-B-06.png), [C 2](../backend/data/screenshots/M9-2025-C-02.png) · **2026** [B 12](../backend/data/screenshots/M9-2026-B-12.png), [D 13](../backend/data/screenshots/M9-2026-D-13.png)

---

<a id="t4"></a>
## 4. Převody jednotek, čas (N-JED)

0,6 points per standard test as a topic of its own · in 8 of 16 · success 44 % · and hidden inside many geometry tasks.

**Must know**

- [seen] Length mm – cm – dm – m – km, including "cm on a map ↔ m, km in reality".
- [seen] Area mm² – cm² – dm² – m² (factor 100 per step): 0,1 m² = 1 000 cm² ([2026 B 1](../backend/data/screenshots/M9-2026-B-01.png) (41 %)); 4 dm² = 400 cm² ([2022 A 2](../backend/data/screenshots/M9-2022-A-02.png) (34 %)).
- [seen] Volume mm³ – cm³ – dm³ – m³ (factor 1 000 per step) and litres: 1 l = 1 dm³, 1 ml = 1 cm³. In [2025 A 6](../backend/data/screenshots/M9-2025-A-06.png) (18 %) a base of 1 500 cm² and a rise of 10 mm must give litres – 18 % success, 45 % blank.
- [seen] Mass g – kg ([2025 C 1](../backend/data/screenshots/M9-2025-C-01.png) (29 %): 5 kg : 0,25 g).
- [seen] Time: hours ↔ minutes, decimal hours (2,4 h = 2 h 24 min), adding clock times ([2026 C 1](../backend/data/screenshots/M9-2026-C-01.png) (40 %)), days ↔ hours.
- [seen] Speed in km/h with time in minutes (see topic 9).
- [seen, once] Degrees and minutes of angle, 1° = 60′ ([2024 D 14](../backend/data/screenshots/M9-2024-D-14.png)).
- [spec only] Seconds and weeks as units to convert (the specification lists *sekunda, minuta, hodina, den, týden*).

**How it is tested.** As a 1-point opener ("Vypočtěte, o kolik cm² …", "kolikrát větší je objem 1,2 dm³ než
objem 300 mm³") or silently: the data come in one unit and the answer is demanded in another.

**Where points are lost.** Area and volume conversions (factor 100 and 1 000, not 10), and litres.

**Examples**

- [2022 A 2](../backend/data/screenshots/M9-2022-A-02.png) · 34 % · [řešení](../backend/data/screenshots/M9-2022-A-02-reseni.png) — Obdélník (šířka v cm, obsah v dm²) – rozdíl stran; kolikrát větší je 1,2 dm³ než 300 mm³
- [2026 B 1](../backend/data/screenshots/M9-2026-B-01.png) · 41 % · [řešení](../backend/data/screenshots/M9-2026-B-01-reseni.png) — Rozdíl ploch 0,1 m² a 20 cm² v cm²
- [2025 C 1](../backend/data/screenshots/M9-2025-C-01.png) · 29 % · [řešení](../backend/data/screenshots/M9-2025-C-01-reseni.png) — Kolikrát více je 5 kg než 0,25 g
- [2023 A 2](../backend/data/screenshots/M9-2023-A-02.png) · 28 % · [řešení](../backend/data/screenshots/M9-2023-A-02-reseni.png) — 2.2: 200 cubes of 8 dm³ → how many cubes of 1 cm³
- [2025 A 6](../backend/data/screenshots/M9-2025-A-06.png) · 18 % · [řešení](../backend/data/screenshots/M9-2025-A-06-reseni.png) — Válcový sud – objem v litrech z výšky hladiny v mm a naopak
- [2022 C 2](../backend/data/screenshots/M9-2022-C-02.png) · 49 % · [řešení](../backend/data/screenshots/M9-2022-C-02-reseni.png) — Dělení kabelu (m → cm); tři pětiny z 1 h 50 min
- [2026 C 1](../backend/data/screenshots/M9-2026-C-01.png) · 40 % · [řešení](../backend/data/screenshots/M9-2026-C-01-reseni.png) — Časové údaje – příjezd do cíle
- [2024 B 1](../backend/data/screenshots/M9-2024-B-01.png) · 50 % · [řešení](../backend/data/screenshots/M9-2024-B-01-reseni.png) — Délka kroku × počet kroků, rozdíl v km
- [2024 D 1](../backend/data/screenshots/M9-2024-D-01.png) · [řešení](../backend/data/screenshots/M9-2024-D-01-reseni.png) — Délka kroku, o kolik kroků více

All 11 tasks tagged `N-JED`: **2022** [A 2](../backend/data/screenshots/M9-2022-A-02.png), [A 11](../backend/data/screenshots/M9-2022-A-11.png), [C 2](../backend/data/screenshots/M9-2022-C-02.png) · **2023** [A 2](../backend/data/screenshots/M9-2023-A-02.png) · **2024** [B 1](../backend/data/screenshots/M9-2024-B-01.png), [D 1](../backend/data/screenshots/M9-2024-D-01.png) · **2025** [A 6](../backend/data/screenshots/M9-2025-A-06.png), [C 1](../backend/data/screenshots/M9-2025-C-01.png) · **2026** [B 1](../backend/data/screenshots/M9-2026-B-01.png), [C 1](../backend/data/screenshots/M9-2026-C-01.png), [D 1](../backend/data/screenshots/M9-2026-D-01.png)

---

<a id="t5"></a>
## 5. Úpravy výrazů (A-VYR)

4,0 points in every test of the sample (20 of 20) · success 50 % · always three items, 1 + 1 + 2 points.

**Must know**

- [seen] Adding, subtracting and multiplying polynomials in one variable (a second variable appears only in the factoring items); result of degree at most 2.
- [seen] A minus in front of a bracket; a product of two binomials; a product of a monomial and a binomial; a number times a product ("2 · (1 − 3a) · (a + 5)").
- [seen] **Vytýkání**: take out the common factor, also a prescribed one ("vytkněte 3y", "vytkněte (−x)"), usually after simplifying first ("Upravte a rozložte na součin vytknutím").
- [seen] **(a ± b)²** forwards with awkward coefficients: fractions (2/3·a − 3)², (b/3 − 3b)², decimals (0,3x + 0,5)², (5b − 0,4a)², two minus signs (−3 − 2x)², (−n − 1)², a bracket to simplify first (4 + 8a − 8)², (a − a/4)², a factor in front 4·(n − 1/2)², ½·(2a + 4)².
- [seen] **(a ± b)²** backwards: "Do rámečků doplňte chybějící čísla": (y + □)² = y² + 10y + □.
- [seen] **a² − b²** in disguise: 4a² − 9; 9a² − 16; 49 − (−4a)²; 6·6 − 25a²; 6 400 − (x² − 3 600) = 10 000 − x²; and "simplify, then factor by formula": x·(18 − x) + 9·(16 − 2x) = 144 − x².
- [seen] Reading a formula as a multiplication: "nejjednodušší výraz, kterým je třeba vynásobit výraz 3a − 2², abychom získali výraz 9a² − 16" ([2023 B 4](../backend/data/screenshots/M9-2023-B-04.png) (52 %)).
- [seen] Value of an expression for a given value of the variable ([2026 A 3](../backend/data/screenshots/M9-2026-A-03.png) (48 %)).
- [seen] Choosing the expression that describes a situation ([2022 B 14](../backend/data/screenshots/M9-2022-B-14.png) (37 %)).
- Not in the 20 tests and not in the specification: algebraic fractions with a variable in the denominator, division of polynomials, third powers, conditions of validity.

**How it is tested.** Three items in fixed roles:

1. factor – "Upravte a rozložte na součin vytknutím" or "Rozložte na součin užitím vzorce";
2. square – "Umocněte a zjednodušte (výsledný výraz nesmí obsahovat závorky)", or fill in the boxes, or a short simplification;
3. worked, 2 points – "Upravte na co nejjednodušší tvar bez závorek": two or three products, such as
   (4 + 3n)·(3n − 2n) − (n − 1)·5n.

**Where points are lost.** Item 3 hides a bracket that should be simplified before multiplying: (3n − 2n),
(2 − n + 2n), (−2n − n), (1 − 2n − 4n), (3y + y), (4n − n), (c + c), (−3 + 1). The key gives 1 point for
exactly one wrongly handled term and 0 for more. In item 1, factoring is expected to be complete and to
follow a simplification the task does not spell out. The task averages 44–63 % in regular terms; 2024 A
and B were lower (35–36 %).

**Examples**

*Vytýkání*
- [2022 A 4](../backend/data/screenshots/M9-2022-A-04.png) · 46 % · [řešení](../backend/data/screenshots/M9-2022-A-04-reseni.png) — 4.1: vytkněte 3y z 3y² − 9y + 6xy
- [2023 A 4](../backend/data/screenshots/M9-2023-A-04.png) · 50 % · [řešení](../backend/data/screenshots/M9-2023-A-04-reseni.png) — 4.1: 2·(x² − x) + x
- [2023 B 4](../backend/data/screenshots/M9-2023-B-04.png) · 52 % · [řešení](../backend/data/screenshots/M9-2023-B-04-reseni.png) — 4.1: x·(y − 3) + 3·(x − 2y)
- [2026 B 3](../backend/data/screenshots/M9-2026-B-03.png) · 63 % · [řešení](../backend/data/screenshots/M9-2026-B-03-reseni.png) — 3.2: (a − 2b)·b − b + 2b²
- [2026 D 3](../backend/data/screenshots/M9-2026-D-03.png) · 31 % · [řešení](../backend/data/screenshots/M9-2026-D-03-reseni.png) — 3.1: vytkněte (−x)

*Squaring a binomial*
- [2022 B 4](../backend/data/screenshots/M9-2022-B-04.png) · 52 % · [řešení](../backend/data/screenshots/M9-2022-B-04-reseni.png) — 4.2: (5b − 0,4a)²
- [2023 D 4](../backend/data/screenshots/M9-2023-D-04.png) · 32 % · [řešení](../backend/data/screenshots/M9-2023-D-04-reseni.png) — 4.1: (0,3x + 0,5)²
- [2024 A 4](../backend/data/screenshots/M9-2024-A-04.png) · 36 % · [řešení](../backend/data/screenshots/M9-2024-A-04-reseni.png) — 4.1: (a − a/4)²
- [2024 C 4](../backend/data/screenshots/M9-2024-C-04.png) · [řešení](../backend/data/screenshots/M9-2024-C-04-reseni.png) — 4.1: (b/3 − 3b)²
- [2025 C 4](../backend/data/screenshots/M9-2025-C-04.png) · 30 % · [řešení](../backend/data/screenshots/M9-2025-C-04-reseni.png) — 4.1: (4 + 8a − 8)²
- [2026 C 3](../backend/data/screenshots/M9-2026-C-03.png) · 36 % · [řešení](../backend/data/screenshots/M9-2026-C-03-reseni.png) — 3.2: 4·(n − 1/2)²

*Formula backwards and a² − b²*
- [2022 D 4](../backend/data/screenshots/M9-2022-D-04.png) · 42 % · [řešení](../backend/data/screenshots/M9-2022-D-04-reseni.png) — 4.2: (y + □)² = y² + 10y + □
- [2025 A 3](../backend/data/screenshots/M9-2025-A-03.png) · 48 % · [řešení](../backend/data/screenshots/M9-2025-A-03-reseni.png) — 3.1 boxes; 3.3 simplify, then factor 144 − x²
- [2023 C 4](../backend/data/screenshots/M9-2023-C-04.png) · 33 % · [řešení](../backend/data/screenshots/M9-2023-C-04-reseni.png) — 4.1: 4a² − 9
- [2024 B 4](../backend/data/screenshots/M9-2024-B-04.png) · 35 % · [řešení](../backend/data/screenshots/M9-2024-B-04-reseni.png) — 4.2: 6 400 − (x² − 3 600)
- [2025 D 4](../backend/data/screenshots/M9-2025-D-04.png) · 32 % · [řešení](../backend/data/screenshots/M9-2025-D-04-reseni.png) — 4.2: k·(k − 9) + 9·(k − 16)
- [2026 A 3](../backend/data/screenshots/M9-2026-A-03.png) · 48 % · [řešení](../backend/data/screenshots/M9-2026-A-03-reseni.png) — 3.2: 1 − 2n + 2n·(1 − 8n)

*Choosing or evaluating an expression*
- [2022 B 14](../backend/data/screenshots/M9-2022-B-14.png) · 37 % · [řešení](../backend/data/screenshots/M9-2022-B-14-reseni.png) — Výběr výrazu popisujícího situaci (k polic, o 8 knih více)

All 20 tasks tagged `A-VYR`: **2022** [A 4](../backend/data/screenshots/M9-2022-A-04.png), [B 4](../backend/data/screenshots/M9-2022-B-04.png), [C 4](../backend/data/screenshots/M9-2022-C-04.png), [D 4](../backend/data/screenshots/M9-2022-D-04.png) · **2023** [A 4](../backend/data/screenshots/M9-2023-A-04.png), [B 4](../backend/data/screenshots/M9-2023-B-04.png), [C 4](../backend/data/screenshots/M9-2023-C-04.png), [D 4](../backend/data/screenshots/M9-2023-D-04.png) · **2024** [A 4](../backend/data/screenshots/M9-2024-A-04.png), [B 4](../backend/data/screenshots/M9-2024-B-04.png), [C 4](../backend/data/screenshots/M9-2024-C-04.png), [D 4](../backend/data/screenshots/M9-2024-D-04.png) · **2025** [A 3](../backend/data/screenshots/M9-2025-A-03.png), [B 4](../backend/data/screenshots/M9-2025-B-04.png), [C 4](../backend/data/screenshots/M9-2025-C-04.png), [D 4](../backend/data/screenshots/M9-2025-D-04.png) · **2026** [A 3](../backend/data/screenshots/M9-2026-A-03.png), [B 3](../backend/data/screenshots/M9-2026-B-03.png), [C 3](../backend/data/screenshots/M9-2026-C-03.png), [D 3](../backend/data/screenshots/M9-2026-D-03.png)

---

<a id="t6"></a>
## 6. Lineární rovnice a soustavy (A-ROV, A-SOU)

4,0 points in every test of the sample (20 of 20) · success 52 % · two worked items of 2 points.

**Must know**

- [seen] Solving a linear equation by *ekvivalentní úpravy*, written step by step.
- [seen] Equations with brackets and decimals: 0,5x + 2·(x + 2,5) = 2,5·(x + 3); also with the division sign, "3x : 2", "(8 − 6x) : 2", "x : 5".
- [seen] Equations with fractions whose numerators are binomials: (y − 5)/2 + (3 − y)/6 = (1 − 2y)/3. Multiply the whole equation by the common denominator and keep each numerator in a bracket – the minus before a fraction is the classic error.
- [seen] Mixed: a fraction and a decimal in one equation ([2023 D 5](../backend/data/screenshots/M9-2023-D-05.png) (43 %), [2024 B 5](../backend/data/screenshots/M9-2024-B-05.png) (58 %)); a number multiplying a fraction (7 · (y − 3)/6).
- [seen] **An equation with no solution**: the unknown disappears and a false statement remains; the answer "rovnice nemá řešení" must be written ([2023 A 5](../backend/data/screenshots/M9-2023-A-05.png) (53 %), [2025 A 4](../backend/data/screenshots/M9-2025-A-04.png) (34 %)).
- [seen, 2024 only] An equation with squared binomials in which x² cancels: −2·(x + 4) − 3·(x + 1)² = x·(2 − 3x) ([2024 A 5](../backend/data/screenshots/M9-2024-A-05.png) (31 %), [2024 C 5](../backend/data/screenshots/M9-2024-C-05.png)).
- [seen, from 2025] *Soustava dvou rovnic se dvěma neznámými* by *dosazovací* or *sčítací metoda*; one of the four needs rearranging first (3x − (y + 1) = 10; 2x − 9 = y). In 4 of the 8 tests of 2025–2026.
- [spec only] An equation with *nekonečně mnoho řešení* (0 = 0) – the specification names all three outcomes; only "one solution" and "no solution" are keyed in these 20 tests. *Zkouška* is in the specification, but every test says "zkoušku nezapisujte".

**How it is tested.** "Řešte rovnici:" / "Řešte soustavu rovnic:" with "V záznamovém archu uveďte v obou
částech úlohy celý postup řešení (zkoušku nezapisujte)". Unknowns are x and y.

**Where points are lost.** The key: one wrongly handled term in an equivalent step, stopping at *ax = b*, or
a missing or wrong conclusion for an equation without solution = 1 point. An "algoritmicky chybná" step or
more than one error = 0. For systems, finding only one unknown correctly = 1 point. The tests with an
equation without solution or with squares scored lowest ([2025 A 4](../backend/data/screenshots/M9-2025-A-04.png) (34 %) and [2024 A 5](../backend/data/screenshots/M9-2024-A-05.png) (31 %)), the plain pair in
[2022 B 5](../backend/data/screenshots/M9-2022-B-05.png) (72 %) highest.

**Examples**

*Decimals and brackets*
- [2022 B 5](../backend/data/screenshots/M9-2022-B-05.png) · 72 % · [řešení](../backend/data/screenshots/M9-2022-B-05-reseni.png) — Lineární rovnice se závorkami a desetinnými čísly; se zlomky
- [2023 B 5](../backend/data/screenshots/M9-2023-B-05.png) · 48 % · [řešení](../backend/data/screenshots/M9-2023-B-05-reseni.png) — Lineární rovnice s desetinnými čísly; se zlomky
- [2026 D 4](../backend/data/screenshots/M9-2026-D-04.png) · 29 % · [řešení](../backend/data/screenshots/M9-2026-D-04-reseni.png) — Rovnice s desetinnými čísly; rovnice se zlomky

*Fractions*
- [2022 A 5](../backend/data/screenshots/M9-2022-A-05.png) · 48 % · [řešení](../backend/data/screenshots/M9-2022-A-05-reseni.png) — Lineární rovnice s desetinnými čísly; lineární rovnice se zlomky
- [2023 C 5](../backend/data/screenshots/M9-2023-C-05.png) · 40 % · [řešení](../backend/data/screenshots/M9-2023-C-05-reseni.png) — Lineární rovnice s desetinnými čísly; se zlomky
- [2025 C 5](../backend/data/screenshots/M9-2025-C-05.png) · 34 % · [řešení](../backend/data/screenshots/M9-2025-C-05-reseni.png) — Dvě lineární rovnice se zlomky
- [2026 B 4](../backend/data/screenshots/M9-2026-B-04.png) · 57 % · [řešení](../backend/data/screenshots/M9-2026-B-04-reseni.png) — Dvě lineární rovnice se zlomky

*No solution; squares that cancel*
- [2023 A 5](../backend/data/screenshots/M9-2023-A-05.png) · 53 % · [řešení](../backend/data/screenshots/M9-2023-A-05-reseni.png) — Rovnice bez řešení; rovnice se zlomky
- [2025 A 4](../backend/data/screenshots/M9-2025-A-04.png) · 34 % · [řešení](../backend/data/screenshots/M9-2025-A-04-reseni.png) — Rovnice se zlomky; rovnice bez řešení
- [2024 A 5](../backend/data/screenshots/M9-2024-A-05.png) · 31 % · [řešení](../backend/data/screenshots/M9-2024-A-05-reseni.png) — Rovnice s (x+1)², která vede na lineární; rovnice se zlomkem
- [2024 C 5](../backend/data/screenshots/M9-2024-C-05.png) · [řešení](../backend/data/screenshots/M9-2024-C-05-reseni.png) — Rovnice se zlomky; rovnice s druhými mocninami dvojčlenů vedoucí na lineární

*Soustava rovnic*
- [2025 B 5](../backend/data/screenshots/M9-2025-B-05.png) · 48 % · [řešení](../backend/data/screenshots/M9-2025-B-05-reseni.png) — Rovnice se zlomky; soustava dvou rovnic
- [2025 D 5](../backend/data/screenshots/M9-2025-D-05.png) · 34 % · [řešení](../backend/data/screenshots/M9-2025-D-05-reseni.png) — Rovnice s desetinnými čísly; soustava dvou rovnic
- [2026 A 4](../backend/data/screenshots/M9-2026-A-04.png) · 54 % · [řešení](../backend/data/screenshots/M9-2026-A-04-reseni.png) — Rovnice s desetinnými čísly; soustava dvou rovnic
- [2026 C 4](../backend/data/screenshots/M9-2026-C-04.png) · 41 % · [řešení](../backend/data/screenshots/M9-2026-C-04-reseni.png) — Rovnice se zlomky; soustava dvou rovnic

All 20 tasks tagged `A-ROV`: **2022** [A 5](../backend/data/screenshots/M9-2022-A-05.png), [B 5](../backend/data/screenshots/M9-2022-B-05.png), [C 5](../backend/data/screenshots/M9-2022-C-05.png), [D 5](../backend/data/screenshots/M9-2022-D-05.png) · **2023** [A 5](../backend/data/screenshots/M9-2023-A-05.png), [B 5](../backend/data/screenshots/M9-2023-B-05.png), [C 5](../backend/data/screenshots/M9-2023-C-05.png), [D 5](../backend/data/screenshots/M9-2023-D-05.png) · **2024** [A 5](../backend/data/screenshots/M9-2024-A-05.png), [B 5](../backend/data/screenshots/M9-2024-B-05.png), [C 5](../backend/data/screenshots/M9-2024-C-05.png), [D 5](../backend/data/screenshots/M9-2024-D-05.png) · **2025** [A 4](../backend/data/screenshots/M9-2025-A-04.png), [B 5](../backend/data/screenshots/M9-2025-B-05.png), [C 5](../backend/data/screenshots/M9-2025-C-05.png), [D 5](../backend/data/screenshots/M9-2025-D-05.png) · **2026** [A 4](../backend/data/screenshots/M9-2026-A-04.png), [B 4](../backend/data/screenshots/M9-2026-B-04.png), [C 4](../backend/data/screenshots/M9-2026-C-04.png), [D 4](../backend/data/screenshots/M9-2026-D-04.png)

---

<a id="t7"></a>
## 7. Výraz s proměnnou, slovní úlohy na rovnici (A-SLOV)

3,0 points per standard test · in 15 of 16 · success 32 %, 20 % blank · the last step is solved by 10–27 %.

**Must know**

- [seen] Writing a quantity as an expression in a given variable: "Vyjádřete výrazem s proměnnou x …". The answer is an expression such as 4x/3 or 120x + 600, not a number.
- [seen] Translating the relational phrases exactly (full table in [section 20](#t20)): "o třetinu více", "o čtvrtinu déle", "dvakrát déle než", "o 60 % více", "o polovinu levnější než", "čtyřikrát menší než … dohromady".
- [seen] **Turning a relation round**: the variable is often not the quantity the others are compared to. In [2025 C 6](../backend/data/screenshots/M9-2025-C-06.png) (8 %) the bedside table (n) is "o polovinu levnější než skříň" and "o třetinu dražší než postel", so the wardrobe is 2n and the bed is 3n/4 – 8 % success.
- [seen] Setting up and solving one linear equation from a further condition, and answering the question asked (which may be a different quantity than x: [2026 A 6](../backend/data/screenshots/M9-2026-A-06.png) (19 %) asks for the total distance ridden).
- [seen] Problems with two unknowns solved by one equation or by a system: counts and totals ([2026 B 6](../backend/data/screenshots/M9-2026-B-06.png) (38 %): 510 drinks for 29 700 korun; [2026 C 14](../backend/data/screenshots/M9-2026-C-14.png) (37 %): 21 relay teams, 60 runners), sum and difference ([2024 C 1](../backend/data/screenshots/M9-2024-C-01.png)).
- [seen] Solving by *úsudek* without an equation where the numbers allow ([2022 D 6](../backend/data/screenshots/M9-2022-D-06.png) (21 %), [2024 D 7](../backend/data/screenshots/M9-2024-D-07.png)).
- [seen] Whole-number conditions: the number of buses, apples or children must be an integer ([2023 D 7](../backend/data/screenshots/M9-2023-D-07.png) (26 %), [2024 D 15](../backend/data/screenshots/M9-2024-D-15.png), [2026 D 13](../backend/data/screenshots/M9-2026-D-13.png) (27 %)).

**How it is tested.** The fixed three-step task among tasks 5–8, result only: a *výchozí text* with two
relations; "… označíme x"; two expressions for 1 point each; then a new condition and "Vypočtěte …" for
1–2 points. In 12 of 16 standard tests. In addition one multiple-choice word problem in most tests, and
once a choice of the right expression.

**Where points are lost.** The expressions themselves ([2022 A 8.1](../backend/data/screenshots/M9-2022-A-08.png) (39 %) and [2022 A 8.2](../backend/data/screenshots/M9-2022-A-08.png) (28 %)) and then the equation,
which builds on them. Success of whole tasks in regular terms: 49 % (2022 A), 36 % (2023 B), 25 % (2023 A),
14 % (2025 B), 19 % (2026 A).

**Examples**

*The three-step task*
- [2022 A 8](../backend/data/screenshots/M9-2022-A-08.png) · 49 % · [řešení](../backend/data/screenshots/M9-2022-A-08-reseni.png) — Výraz s proměnnou x (cena dortíku, koláčů) a slovní úloha na rovnici
- [2022 C 6](../backend/data/screenshots/M9-2022-C-06.png) · 24 % · [řešení](../backend/data/screenshots/M9-2022-C-06-reseni.png) — Výrazy s proměnnou x („o třetinu více“, „o 12 více“) a rovnice
- [2023 B 7](../backend/data/screenshots/M9-2023-B-07.png) · 36 % · [řešení](../backend/data/screenshots/M9-2023-B-07-reseni.png) — Doba cesty: výrazy s x („dvakrát déle“, „o čtvrtinu déle“) a rovnice
- [2023 D 6](../backend/data/screenshots/M9-2023-D-06.png) · 21 % · [řešení](../backend/data/screenshots/M9-2023-D-06-reseni.png) — Výrazy s p („o třetinu více“, „o 60 % více“) a rovnice
- [2024 B 7](../backend/data/screenshots/M9-2024-B-07.png) · 41 % · [řešení](../backend/data/screenshots/M9-2024-B-07-reseni.png) — Výraz s x („o polovinu více“) a rovnice
- [2025 B 7](../backend/data/screenshots/M9-2025-B-07.png) · 14 % · [řešení](../backend/data/screenshots/M9-2025-B-07-reseni.png) — Prodej salátů – třetina, „o třetinu méně“, výraz s x
- [2025 C 6](../backend/data/screenshots/M9-2025-C-06.png) · 8 % · [řešení](../backend/data/screenshots/M9-2025-C-06-reseni.png) — Ceny nábytku: výrazy s n („o polovinu levnější“, „o třetinu dražší“) a rovnice
- [2026 A 6](../backend/data/screenshots/M9-2026-A-06.png) · 19 % · [řešení](../backend/data/screenshots/M9-2026-A-06-reseni.png) — Cyklostezka: výrazy s x (dvě třetiny, čtvrtina z ujeté části) a rovnice
- [2026 C 5](../backend/data/screenshots/M9-2026-C-05.png) · 19 % · [řešení](../backend/data/screenshots/M9-2026-C-05-reseni.png) — Fitcentrum – výraz 120x + 600 a rovnice
- [2026 D 5](../backend/data/screenshots/M9-2026-D-05.png) · 15 % · [řešení](../backend/data/screenshots/M9-2026-D-05-reseni.png) — Úseky kanalizace: výrazy s r a rovnice

*Expression plus geometry*
- [2023 A 8](../backend/data/screenshots/M9-2023-A-08.png) · 25 % · [řešení](../backend/data/screenshots/M9-2023-A-08-reseni.png) — Čtvercový a obdélníkový pozemek se stejným obvodem – výraz, rovnice, rozdíl obsahů

*Two unknowns*
- [2026 B 6](../backend/data/screenshots/M9-2026-B-06.png) · 38 % · [řešení](../backend/data/screenshots/M9-2026-B-06-reseni.png) — Čaj a punč – cena o 75 % vyšší, výraz, soustava slovně
- [2026 C 14](../backend/data/screenshots/M9-2026-C-14.png) · 37 % · [řešení](../backend/data/screenshots/M9-2026-C-14-reseni.png) — Štafety – soustava slovně, výsledek zlomkem
- [2023 D 7](../backend/data/screenshots/M9-2023-D-07.png) · 26 % · [řešení](../backend/data/screenshots/M9-2023-D-07-reseni.png) — Parkoviště pro auta a autobusy – rovnice
- [2024 D 6](../backend/data/screenshots/M9-2024-D-06.png) · [řešení](../backend/data/screenshots/M9-2024-D-06-reseni.png) — Vagony 1. a 2. třídy – rovnice
- [2025 D 13](../backend/data/screenshots/M9-2025-D-13.png) · 25 % · [řešení](../backend/data/screenshots/M9-2025-D-13-reseni.png) — Vagony tří vlaků – rovnice

*Multiple choice and short word problems*
- [2022 B 14](../backend/data/screenshots/M9-2022-B-14.png) · 37 % · [řešení](../backend/data/screenshots/M9-2022-B-14-reseni.png) — Výběr výrazu popisujícího situaci (k polic, o 8 knih více)
- [2023 B 14](../backend/data/screenshots/M9-2023-B-14.png) · 33 % · [řešení](../backend/data/screenshots/M9-2023-B-14-reseni.png) — Pomlázky: pětina a „o 180 více“
- [2024 A 14](../backend/data/screenshots/M9-2024-A-14.png) · 47 % · [řešení](../backend/data/screenshots/M9-2024-A-14-reseni.png) — Neznámé číslo – rovnice
- [2024 C 14](../backend/data/screenshots/M9-2024-C-14.png) · [řešení](../backend/data/screenshots/M9-2024-C-14-reseni.png) — Komiksy – „o osminu více“
- [2025 A 13](../backend/data/screenshots/M9-2025-A-13.png) · 44 % · [řešení](../backend/data/screenshots/M9-2025-A-13-reseni.png) — Přihlášky na tábor – „o pětinu“ a „o 30 %“ více
- [2026 D 13](../backend/data/screenshots/M9-2026-D-13.png) · 27 % · [řešení](../backend/data/screenshots/M9-2026-D-13-reseni.png) — Dělení do trojic a pětic – zbytek

All 31 tasks tagged `A-SLOV`: **2022** [A 8](../backend/data/screenshots/M9-2022-A-08.png), [B 6](../backend/data/screenshots/M9-2022-B-06.png), [B 14](../backend/data/screenshots/M9-2022-B-14.png), [C 6](../backend/data/screenshots/M9-2022-C-06.png) · **2023** [A 8](../backend/data/screenshots/M9-2023-A-08.png), [B 7](../backend/data/screenshots/M9-2023-B-07.png), [B 14](../backend/data/screenshots/M9-2023-B-14.png), [C 6](../backend/data/screenshots/M9-2023-C-06.png), [D 6](../backend/data/screenshots/M9-2023-D-06.png), [D 7](../backend/data/screenshots/M9-2023-D-07.png) · **2024** [A 13](../backend/data/screenshots/M9-2024-A-13.png), [A 14](../backend/data/screenshots/M9-2024-A-14.png), [B 7](../backend/data/screenshots/M9-2024-B-07.png), [B 12](../backend/data/screenshots/M9-2024-B-12.png), [C 1](../backend/data/screenshots/M9-2024-C-01.png), [C 12](../backend/data/screenshots/M9-2024-C-12.png), [C 14](../backend/data/screenshots/M9-2024-C-14.png), [D 6](../backend/data/screenshots/M9-2024-D-06.png), [D 15](../backend/data/screenshots/M9-2024-D-15.png) · **2025** [A 13](../backend/data/screenshots/M9-2025-A-13.png), [B 1](../backend/data/screenshots/M9-2025-B-01.png), [B 7](../backend/data/screenshots/M9-2025-B-07.png), [C 6](../backend/data/screenshots/M9-2025-C-06.png), [D 13](../backend/data/screenshots/M9-2025-D-13.png) · **2026** [A 6](../backend/data/screenshots/M9-2026-A-06.png), [B 6](../backend/data/screenshots/M9-2026-B-06.png), [B 14](../backend/data/screenshots/M9-2026-B-14.png), [C 5](../backend/data/screenshots/M9-2026-C-05.png), [C 14](../backend/data/screenshots/M9-2026-C-14.png), [D 5](../backend/data/screenshots/M9-2026-D-05.png), [D 13](../backend/data/screenshots/M9-2026-D-13.png)

---

<a id="t8"></a>
## 8. Procenta (P-PROC)

6,6 points per standard test (8,2 in 2024) · in 20 of 20 · success 44 % · the largest single topic.

**Must know**

- [seen] The three basic computations: *procentová část* (x % of a base), *počet procent* (what percent a part is), *základ* (the whole from a part and its percent).
- [seen] "o x % více / méně" as a multiplier: +25 % → ·1,25, −40 % → ·0,6, +150 % → ·2,5.
- [seen] **Finding the base after a change**: "420 uchazečů, což je o 40 % více, než se jich přihlásilo loni" → 420 : 1,4 = 300. The base is the quantity after "než".
- [seen] **"O kolik procent"** between two quantities – divide the difference by the quantity after "než": price 20 000 → 8 000 is "o 60 % snížena"; 120 nails → 80 nails for the same money is a price rise of 50 %.
- [seen] **Reversing the comparison**: "o jednu třetinu méně" one way is "o 50 % více" the other way ([2025 B 15.2](../backend/data/screenshots/M9-2025-B-15.png) (12 %)). "Zmenšila svůj objem o 2/27" means the warm volume was larger by 2/25 = 8 % ([2022 D 15](../backend/data/screenshots/M9-2022-D-15.png) (41 %)).
- [seen] Two successive changes: +20 % and again +20 % is ·1,44; +40 % then −40 % is ·0,84, not the original; "každý další hod o desetinu delší" ([2026 D 1](../backend/data/screenshots/M9-2026-D-01.png) (10 %)).
- [seen] A percentage of the remainder: a quarter mown, then 60 % of the rest → 30 % left ([2022 B 15](../backend/data/screenshots/M9-2022-B-15.png) (40 %)).
- [seen] Two quantities linked by a percentage with a known total: men 30 % fewer than women, 680 together → x + 0,7x = 680 ([2023 D 15](../backend/data/screenshots/M9-2023-D-15.png) (40 %)).
- [seen] Percent ↔ fraction ↔ ratio: "každý dvacátý" = 5 %; 26/25 → o 4 % více; ratio 3 : 2 → o 50 % více; a fifth and 30 % compared.
- [seen] Percentage points on a base: occupancy rising from 70 % to 75 % with 11 people → capacity 220 ([2024 C 13](../backend/data/screenshots/M9-2024-C-13.png)).
- [seen] Percentages in charts and in geometry (areas, volumes of solids: [2026 A 15](../backend/data/screenshots/M9-2026-A-15.png) (56 %)).
- [seen, 2024 A only] Finance: *úrok* for one year, *daň z úroků* ([2024 A 16](../backend/data/screenshots/M9-2024-A-16.png) (62 %)).
- [spec only] *Promile*; the vocabulary *jistina, úroková míra, úrokovací období, inflace*; loans (*půjčky a úvěry*).

**How it is tested.** Task 15 in all 16 standard tests (task 16 in 2024): "Přiřaďte ke každé úloze
(15.1–15.3) odpovídající výsledek (A–F)" – three independent one- or two-sentence problems, 2 points each,
six shared options. Options are round numbers, with "jiný počet" or a range as the sixth. On top of it
usually one multiple-choice or open item elsewhere.

**Where points are lost.** On the base. Items where the base is the obvious number score 70–80 %
(2025 B 15.1: 79,6 %); items where the base is the other quantity or must be reconstructed score 10–35 %.
In 2025 B 15.2 the option 33 % drew 47,8 % of candidates and the key, 50 %, drew 11,5 %.

**Examples**

*Part of a whole, percent of a whole*
- [2024 B 16](../backend/data/screenshots/M9-2024-B-16.png) · 74 % · [řešení](../backend/data/screenshots/M9-2024-B-16-reseni.png) — Procenta: část z celku, sleva, podíl
- [2024 D 12](../backend/data/screenshots/M9-2024-D-12.png) · [řešení](../backend/data/screenshots/M9-2024-D-12-reseni.png) — Kolik procent zbývá dočíst
- [2025 A 15](../backend/data/screenshots/M9-2025-A-15.png) · 44 % · [řešení](../backend/data/screenshots/M9-2025-A-15-reseni.png) — 15.1 direct; 15.2 and 15.3 need the composition worked out first
- [2026 D 15](../backend/data/screenshots/M9-2026-D-15.png) · 37 % · [řešení](../backend/data/screenshots/M9-2026-D-15-reseni.png) — Procenta s tabulkou účastníků kurzů

*Finding the base ("což je o … více než")*
- [2022 A 15](../backend/data/screenshots/M9-2022-A-15.png) · 43 % · [řešení](../backend/data/screenshots/M9-2022-A-15-reseni.png) — Procenta (o x % více/méně) s tabulkou sběru papíru
- [2023 A 15](../backend/data/screenshots/M9-2023-A-15.png) · 38 % · [řešení](../backend/data/screenshots/M9-2023-A-15-reseni.png) — 15.2 base; 15.1 and 15.3 successive changes
- [2023 D 15](../backend/data/screenshots/M9-2023-D-15.png) · 40 % · [řešení](../backend/data/screenshots/M9-2023-D-15-reseni.png) — Procenta: zpětný výpočet základu („o 40 % více než loni“)
- [2026 B 15](../backend/data/screenshots/M9-2026-B-15.png) · 46 % · [řešení](../backend/data/screenshots/M9-2026-B-15-reseni.png) — Procenta: zpětný výpočet základu, zbytek, „o 60 % lehčí“

*O kolik procent*
- [2022 B 15](../backend/data/screenshots/M9-2022-B-15.png) · 40 % · [řešení](../backend/data/screenshots/M9-2022-B-15-reseni.png) — Procenta: snížení ceny, část ze zbytku, zdražení (méně kusů za stejnou částku)
- [2023 B 15](../backend/data/screenshots/M9-2023-B-15.png) · 47 % · [řešení](../backend/data/screenshots/M9-2023-B-15-reseni.png) — Procenta: růst, zlomek ze zlomku, podíl z celku
- [2024 B 2](../backend/data/screenshots/M9-2024-B-02.png) · 34 % · [řešení](../backend/data/screenshots/M9-2024-B-02-reseni.png) — O kolik procent je cesta po odvěsnách delší než po přeponě
- [2026 B 5](../backend/data/screenshots/M9-2026-B-05.png) · 42 % · [řešení](../backend/data/screenshots/M9-2026-B-05-reseni.png) — Recept – přímá úměrnost; o kolik procent více
- [2026 C 15](../backend/data/screenshots/M9-2026-C-15.png) · 32 % · [řešení](../backend/data/screenshots/M9-2026-C-15-reseni.png) — Procenta: podíl, poměr → procenta, rozdíl cen
- [2026 A 15](../backend/data/screenshots/M9-2026-A-15.png) · 56 % · [řešení](../backend/data/screenshots/M9-2026-A-15-reseni.png) — O kolik procent větší/menší objem těles ze základních kvádrů

*Reversed comparison, percent ↔ fraction*
- [2025 B 15](../backend/data/screenshots/M9-2025-B-15.png) · 42 % · [řešení](../backend/data/screenshots/M9-2025-B-15-reseni.png) — Procenta: část z celku, „o třetinu méně → o kolik % více“, rovnice
- [2022 D 15](../backend/data/screenshots/M9-2022-D-15.png) · 41 % · [řešení](../backend/data/screenshots/M9-2022-D-15-reseni.png) — Převod zlomek ↔ procenta, změna základu
- [2026 A 12](../backend/data/screenshots/M9-2026-A-12.png) · 50 % · [řešení](../backend/data/screenshots/M9-2026-A-12-reseni.png) — Parkoviště – dvacetina vs. 4 %
- [2025 D 15](../backend/data/screenshots/M9-2025-D-15.png) · 37 % · [řešení](../backend/data/screenshots/M9-2025-D-15-reseni.png) — Zlomky, procenta a poměr – věk

*More than 100 %, successive changes*
- [2023 B 2](../backend/data/screenshots/M9-2023-B-02.png) · 45 % · [řešení](../backend/data/screenshots/M9-2023-B-02-reseni.png) — „O 150 % dražší“ – kolikrát více, rozdíl cen
- [2024 B 11](../backend/data/screenshots/M9-2024-B-11.png) · 73 % · [řešení](../backend/data/screenshots/M9-2024-B-11-reseni.png) — Zdražení o 40 % a zlevnění o 40 %
- [2024 D 2](../backend/data/screenshots/M9-2024-D-02.png) · [řešení](../backend/data/screenshots/M9-2024-D-02-reseni.png) — Dvojí zlevnění – o kolik procent je konečná cena nižší
- [2026 D 1](../backend/data/screenshots/M9-2026-D-01.png) · 10 % · [řešení](../backend/data/screenshots/M9-2026-D-01-reseni.png) — Každý hod o desetinu delší než předchozí
- [2026 D 12](../backend/data/screenshots/M9-2026-D-12.png) · 18 % · [řešení](../backend/data/screenshots/M9-2026-D-12-reseni.png) — Ceny dílů románu – řetězení procent

*Two linked quantities with a total*
- [2022 C 15](../backend/data/screenshots/M9-2022-C-15.png) · 31 % · [řešení](../backend/data/screenshots/M9-2022-C-15-reseni.png) — Procenta: zbytek po odvozu, zlomek + procento, „o 50 % více než … a méně než …“
- [2023 C 15](../backend/data/screenshots/M9-2023-C-15.png) · 48 % · [řešení](../backend/data/screenshots/M9-2023-C-15-reseni.png) — Procenta: „o 25 % více“, část a zbytek, procento + zlomek z celku
- [2025 C 15](../backend/data/screenshots/M9-2025-C-15.png) · 35 % · [řešení](../backend/data/screenshots/M9-2025-C-15-reseni.png) — Procenta a zlomky – hrnky
- [2024 C 12](../backend/data/screenshots/M9-2024-C-12.png) · [řešení](../backend/data/screenshots/M9-2024-C-12-reseni.png) — Spoření na dárek – procenta a rovnice
- [2024 C 13](../backend/data/screenshots/M9-2024-C-13.png) · [řešení](../backend/data/screenshots/M9-2024-C-13-reseni.png) — Obsazenost sálu 70 % → 75 %

*Finance*
- [2024 A 16](../backend/data/screenshots/M9-2024-A-16.png) · 62 % · [řešení](../backend/data/screenshots/M9-2024-A-16-reseni.png) — Procenta ve finančním kontextu: úrok, daň z úroku, zlevnění a zdražení

All 44 tasks tagged `P-PROC`: **2022** [A 14](../backend/data/screenshots/M9-2022-A-14.png), [A 15](../backend/data/screenshots/M9-2022-A-15.png), [B 15](../backend/data/screenshots/M9-2022-B-15.png), [C 15](../backend/data/screenshots/M9-2022-C-15.png), [D 15](../backend/data/screenshots/M9-2022-D-15.png) · **2023** [A 7](../backend/data/screenshots/M9-2023-A-07.png), [A 15](../backend/data/screenshots/M9-2023-A-15.png), [B 2](../backend/data/screenshots/M9-2023-B-02.png), [B 15](../backend/data/screenshots/M9-2023-B-15.png), [C 15](../backend/data/screenshots/M9-2023-C-15.png), [D 6](../backend/data/screenshots/M9-2023-D-06.png), [D 15](../backend/data/screenshots/M9-2023-D-15.png) · **2024** [A 16](../backend/data/screenshots/M9-2024-A-16.png), [B 2](../backend/data/screenshots/M9-2024-B-02.png), [B 11](../backend/data/screenshots/M9-2024-B-11.png), [B 12](../backend/data/screenshots/M9-2024-B-12.png), [B 15](../backend/data/screenshots/M9-2024-B-15.png), [B 16](../backend/data/screenshots/M9-2024-B-16.png), [C 12](../backend/data/screenshots/M9-2024-C-12.png), [C 13](../backend/data/screenshots/M9-2024-C-13.png), [C 15](../backend/data/screenshots/M9-2024-C-15.png), [D 2](../backend/data/screenshots/M9-2024-D-02.png), [D 8](../backend/data/screenshots/M9-2024-D-08.png), [D 11](../backend/data/screenshots/M9-2024-D-11.png), [D 12](../backend/data/screenshots/M9-2024-D-12.png), [D 16](../backend/data/screenshots/M9-2024-D-16.png) · **2025** [A 5](../backend/data/screenshots/M9-2025-A-05.png), [A 13](../backend/data/screenshots/M9-2025-A-13.png), [A 15](../backend/data/screenshots/M9-2025-A-15.png), [B 15](../backend/data/screenshots/M9-2025-B-15.png), [C 7](../backend/data/screenshots/M9-2025-C-07.png), [C 11](../backend/data/screenshots/M9-2025-C-11.png), [C 15](../backend/data/screenshots/M9-2025-C-15.png), [D 15](../backend/data/screenshots/M9-2025-D-15.png) · **2026** [A 11](../backend/data/screenshots/M9-2026-A-11.png), [A 12](../backend/data/screenshots/M9-2026-A-12.png), [A 15](../backend/data/screenshots/M9-2026-A-15.png), [B 5](../backend/data/screenshots/M9-2026-B-05.png), [B 6](../backend/data/screenshots/M9-2026-B-06.png), [B 15](../backend/data/screenshots/M9-2026-B-15.png), [C 15](../backend/data/screenshots/M9-2026-C-15.png), [D 1](../backend/data/screenshots/M9-2026-D-01.png), [D 12](../backend/data/screenshots/M9-2026-D-12.png), [D 15](../backend/data/screenshots/M9-2026-D-15.png)

---

<a id="t9"></a>
## 9. Poměr, úměrnost, měřítko, společná práce, pohyb (P-POM)

3,3 points per standard test (4,8 in 2024) · in 14 of 16 · success 37 %.

**Must know**

- [seen] *Poměr*: writing it in *základní tvar*, dividing a quantity in a given ratio, finding the parts from their difference (3 : 5 with a difference of 600 g), ratio ↔ fraction ↔ percent.
- [seen] A ratio on a number line or a segment ("bod B dělí úsečku AC v poměru 7 : 3", [2022 B 2](../backend/data/screenshots/M9-2022-B-02.png) (24 %)).
- [seen] *Měřítko mapy / plánu*: deriving it from data (3,5 cm ≙ 700 m → 1 : 20 000), map ↔ reality in both directions with unit changes, and **area scales with the square** (1 : 100 in length is 1 : 10 000 in area, [2024 A 15](../backend/data/screenshots/M9-2024-A-15.png) (59 %)).
- [seen] *Přímá úměrnost* (*trojčlenka*): recipe quantities, exchange rates of goods, unit price.
- [seen] *Nepřímá úměrnost*: more people → fewer days; faster connection → shorter time; a job larger by a half done by four seamstresses instead of five combines both ([2024 A 1](../backend/data/screenshots/M9-2024-A-01.png) (18 %)).
- [seen] *Společná práce*: add the rates per unit of time, not the times ([2024 D 13](../backend/data/screenshots/M9-2024-D-13.png), [2025 D 6](../backend/data/screenshots/M9-2025-D-06.png) (23 %), [2022 A 7](../backend/data/screenshots/M9-2022-A-07.png) (34 %)).
- [seen] *Pohyb*: s = v·t at constant speed, two runners compared, parts of a route at different speeds, minutes ↔ hours.
- [seen] Mixtures and average price by weight ([2023 C 8](../backend/data/screenshots/M9-2023-C-08.png) (11 %)).
- [seen] Reasoning with "kolikrát více / méně" chains (barrel – bucket – watering can).
- [spec only] *Postupný poměr* (a : b : c) and *převrácený poměr* by name; "změní číslo v daném poměru"; **graphs of přímá and nepřímá úměrnost**, their equations, and points in a *pravoúhlá soustava souřadnic*.

**How it is tested.** As one of the result-only applied tasks 6–8 with graduated sub-items, as the A/N
bundle (map scale), or as a multiple-choice word problem. No formula is asked for; everything can be done
by reasoning on small numbers.

**Where points are lost.** The last sub-item, which combines two dependencies: [2023 B 6](../backend/data/screenshots/M9-2023-B-06.png) (21 %) (21 % for the
task), [2022 D 7](../backend/data/screenshots/M9-2022-D-07.png) (7 %) (7 %), [2025 C 7](../backend/data/screenshots/M9-2025-C-07.png) (20 %) (20 %).

**Examples**

*Poměr*
- [2023 D 1](../backend/data/screenshots/M9-2023-D-01.png) · 41 % · [řešení](../backend/data/screenshots/M9-2023-D-01-reseni.png) — Hmotnosti v poměru 3 : 5 s rozdílem 600 g
- [2025 D 2](../backend/data/screenshots/M9-2025-D-02.png) · 17 % · [řešení](../backend/data/screenshots/M9-2025-D-02-reseni.png) — Dvě čísla v poměru 4 : 5
- [2022 B 2](../backend/data/screenshots/M9-2022-B-02.png) · 24 % · [řešení](../backend/data/screenshots/M9-2022-B-02-reseni.png) — Číselná osa: poměr dělení úsečky, určení čísla v bodě
- [2026 D 7](../backend/data/screenshots/M9-2026-D-07.png) · 13 % · [řešení](../backend/data/screenshots/M9-2026-D-07-reseni.png) — Krychle s lichoběžníky na stěnách – zlomek plochy, poměr ploch

*Měřítko*
- [2023 A 11](../backend/data/screenshots/M9-2023-A-11.png) · 59 % · [řešení](../backend/data/screenshots/M9-2023-A-11-reseni.png) — Měřítko mapy
- [2024 A 15](../backend/data/screenshots/M9-2024-A-15.png) · 59 % · [řešení](../backend/data/screenshots/M9-2024-A-15-reseni.png) — Měřítko plánu (délka, obsah)

*Přímá a nepřímá úměrnost*
- [2026 B 5](../backend/data/screenshots/M9-2026-B-05.png) · 42 % · [řešení](../backend/data/screenshots/M9-2026-B-05-reseni.png) — Recept – přímá úměrnost; o kolik procent více
- [2026 C 13](../backend/data/screenshots/M9-2026-C-13.png) · 57 % · [řešení](../backend/data/screenshots/M9-2026-C-13-reseni.png) — Výměna zboží – poměr
- [2026 C 12](../backend/data/screenshots/M9-2026-C-12.png) · 42 % · [řešení](../backend/data/screenshots/M9-2026-C-12-reseni.png) — Rychlost nahrávání – nepřímá úměrnost
- [2023 B 6](../backend/data/screenshots/M9-2023-B-06.png) · 21 % · [řešení](../backend/data/screenshots/M9-2023-B-06-reseni.png) — Zásoby pro expedici – nepřímá úměrnost
- [2024 A 1](../backend/data/screenshots/M9-2024-A-01.png) · 18 % · [řešení](../backend/data/screenshots/M9-2024-A-01-reseni.png) — Švadleny – společná práce (nepřímá úměrnost)
- [2024 C 16](../backend/data/screenshots/M9-2024-C-16.png) · [řešení](../backend/data/screenshots/M9-2024-C-16-reseni.png) — Zedníci – nepřímá úměrnost
- [2022 A 7](../backend/data/screenshots/M9-2022-A-07.png) · 34 % · [řešení](../backend/data/screenshots/M9-2022-A-07-reseni.png) — Spotřeba balení vitaminů – přímá/nepřímá úměrnost, společná spotřeba

*Společná práce*
- [2024 D 13](../backend/data/screenshots/M9-2024-D-13.png) · [řešení](../backend/data/screenshots/M9-2024-D-13-reseni.png) — Společná práce – škrábání brambor
- [2025 D 6](../backend/data/screenshots/M9-2025-D-06.png) · 23 % · [řešení](../backend/data/screenshots/M9-2025-D-06-reseni.png) — Roboti – poměr výkonů, společná práce

*Pohyb*
- [2025 C 7](../backend/data/screenshots/M9-2025-C-07.png) · 20 % · [řešení](../backend/data/screenshots/M9-2025-C-07-reseni.png) — Cyklista – rychlost, dráha, čas, procenta
- [2026 A 7](../backend/data/screenshots/M9-2026-A-07.png) · 28 % · [řešení](../backend/data/screenshots/M9-2026-A-07-reseni.png) — Dva běžci – rychlost, dráha, čas
- [2026 D 8](../backend/data/screenshots/M9-2026-D-08.png) · 39 % · [řešení](../backend/data/screenshots/M9-2026-D-08-reseni.png) — Dva běžci – rychlost, dráha, čas

*Úsudek, směsi*
- [2022 C 7](../backend/data/screenshots/M9-2022-C-07.png) · 55 % · [řešení](../backend/data/screenshots/M9-2022-C-07-reseni.png) — Křídy v krabičkách dvou velikostí – úsudek
- [2022 D 6](../backend/data/screenshots/M9-2022-D-06.png) · 21 % · [řešení](../backend/data/screenshots/M9-2022-D-06-reseni.png) — Hmotnost krabic s činkami – úsudek (soustava bez rovnic)
- [2022 D 7](../backend/data/screenshots/M9-2022-D-07.png) · 7 % · [řešení](../backend/data/screenshots/M9-2022-D-07-reseni.png) — Dvě schodiště s různým počtem schodů – poměr
- [2023 A 2](../backend/data/screenshots/M9-2023-A-02.png) · 28 % · [řešení](../backend/data/screenshots/M9-2023-A-02-reseni.png) — Objemy sud–kbelík–konvička; kvádr z krychlí 8 dm³ → krychličky 1 cm³
- [2023 C 8](../backend/data/screenshots/M9-2023-C-08.png) · 11 % · [řešení](../backend/data/screenshots/M9-2023-C-08-reseni.png) — Cena směsi oříšků z tabulky cen
- [2024 D 7](../backend/data/screenshots/M9-2024-D-07.png) · [řešení](../backend/data/screenshots/M9-2024-D-07-reseni.png) — Ceny obědů z tabulky – úsudek

All 28 tasks tagged `P-POM`: **2022** [A 7](../backend/data/screenshots/M9-2022-A-07.png), [B 2](../backend/data/screenshots/M9-2022-B-02.png), [C 7](../backend/data/screenshots/M9-2022-C-07.png), [D 6](../backend/data/screenshots/M9-2022-D-06.png), [D 7](../backend/data/screenshots/M9-2022-D-07.png) · **2023** [A 2](../backend/data/screenshots/M9-2023-A-02.png), [A 7](../backend/data/screenshots/M9-2023-A-07.png), [A 11](../backend/data/screenshots/M9-2023-A-11.png), [B 6](../backend/data/screenshots/M9-2023-B-06.png), [C 8](../backend/data/screenshots/M9-2023-C-08.png), [C 11](../backend/data/screenshots/M9-2023-C-11.png), [D 1](../backend/data/screenshots/M9-2023-D-01.png) · **2024** [A 1](../backend/data/screenshots/M9-2024-A-01.png), [A 15](../backend/data/screenshots/M9-2024-A-15.png), [C 16](../backend/data/screenshots/M9-2024-C-16.png), [D 7](../backend/data/screenshots/M9-2024-D-07.png), [D 13](../backend/data/screenshots/M9-2024-D-13.png), [D 16](../backend/data/screenshots/M9-2024-D-16.png) · **2025** [C 7](../backend/data/screenshots/M9-2025-C-07.png), [D 2](../backend/data/screenshots/M9-2025-D-02.png), [D 6](../backend/data/screenshots/M9-2025-D-06.png) · **2026** [A 7](../backend/data/screenshots/M9-2026-A-07.png), [A 11](../backend/data/screenshots/M9-2026-A-11.png), [B 5](../backend/data/screenshots/M9-2026-B-05.png), [C 12](../backend/data/screenshots/M9-2026-C-12.png), [C 13](../backend/data/screenshots/M9-2026-C-13.png), [D 7](../backend/data/screenshots/M9-2026-D-07.png), [D 8](../backend/data/screenshots/M9-2026-D-08.png)

---

<a id="t10"></a>
## 10. Grafy, tabulky, aritmetický průměr (D-GRAF)

2,8 points per standard test · in 14 of 16 · success 52 % · the A/N bundle in 9 of 16 standard tests.

**Must know**

- [seen] Reading a *sloupcový graf* with two or three series, with stacked bars, and with bars going both up and down from zero ([2023 D 11](../backend/data/screenshots/M9-2023-D-11.png) (57 %), [2026 B 11](../backend/data/screenshots/M9-2026-B-11.png) (60 %)).
- [seen] **Reconstructing missing data**: a bar is missing, or the axis has no numbers, and the text gives conditions that determine it ([2023 A 7](../backend/data/screenshots/M9-2023-A-07.png) (14 %); [2025 D 14](../backend/data/screenshots/M9-2025-D-14.png) (28 %)).
- [seen] *Kruhový diagram* given by percentages or by central angles: 360° ≙ the whole, 60° ≙ one sixth ([2025 B 11](../backend/data/screenshots/M9-2025-B-11.png) (68 %)); finding the whole from one sector.
- [seen] *Aritmetický průměr*: computing it; finding a missing value from a given mean; mean from a frequency table (count × value); mean of two fractions; "all solutions" for a mean with integer counts ([2025 D 7](../backend/data/screenshots/M9-2025-D-07.png) (16 %)).
- [seen] Reading a table and combining rows ([2024 D 7](../backend/data/screenshots/M9-2024-D-07.png)); sorting people into groups from a text without a chart ([2024 A 7](../backend/data/screenshots/M9-2024-A-07.png) (56 %)).
- [seen] Combining a chart with percentages, ratios and "o polovinu více".
- [spec only] The words *statistický soubor, statistický znak, statistické šetření, četnost*; choosing a suitable type of chart; drawing a chart. *Medián* and *modus* are not in the specification and not in the tests.

**How it is tested.** Task 11: a chart and three statements "Rozhodněte …, zda je pravdivé (A), či nikoli
(N)", 4 points for three correct, 2 for two, 0 otherwise. Or a result-only task among 6–8, or a
multiple-choice item on a mean.

**Where points are lost.** Not on reading values but on the conditions in the text. The A/N bundles score
53–71 % per statement, the open reconstruction tasks 14–50 %.

**Examples**

*Bar charts with missing data*
- [2022 B 7](../backend/data/screenshots/M9-2022-B-07.png) · 50 % · [řešení](../backend/data/screenshots/M9-2022-B-07-reseni.png) — Sloupcový graf s chybějícími údaji, aritmetický průměr
- [2022 C 11](../backend/data/screenshots/M9-2022-C-11.png) · 53 % · [řešení](../backend/data/screenshots/M9-2022-C-11-reseni.png) — Sloupcový graf se třemi řadami (zakoupené, vzrostlé, prodané)
- [2023 A 7](../backend/data/screenshots/M9-2023-A-07.png) · 14 % · [řešení](../backend/data/screenshots/M9-2023-A-07-reseni.png) — Sloupcový graf bez popisu osy, chybějící údaj; procenta a poměr
- [2023 C 11](../backend/data/screenshots/M9-2023-C-11.png) · 56 % · [řešení](../backend/data/screenshots/M9-2023-C-11-reseni.png) — Diagram počtů s chybějícími údaji a poměr
- [2023 D 11](../backend/data/screenshots/M9-2023-D-11.png) · 57 % · [řešení](../backend/data/screenshots/M9-2023-D-11-reseni.png) — Skládaný sloupcový graf s chybějícími údaji
- [2025 C 11](../backend/data/screenshots/M9-2025-C-11.png) · 71 % · [řešení](../backend/data/screenshots/M9-2025-C-11-reseni.png) — Sloupcový graf návštěvnosti – násobky, průměr, procenta
- [2025 D 14](../backend/data/screenshots/M9-2025-D-14.png) · 28 % · [řešení](../backend/data/screenshots/M9-2025-D-14-reseni.png) — Sloupcový graf bez popisu osy, chybějící údaj
- [2026 B 11](../backend/data/screenshots/M9-2026-B-11.png) · 60 % · [řešení](../backend/data/screenshots/M9-2026-B-11-reseni.png) — Skládaný sloupcový graf s chybějícími údaji (parkoviště)
- [2026 C 11](../backend/data/screenshots/M9-2026-C-11.png) · 65 % · [řešení](../backend/data/screenshots/M9-2026-C-11-reseni.png) — Sloupcový graf služeb – úsudek z podmínek
- [2026 D 11](../backend/data/screenshots/M9-2026-D-11.png) · 59 % · [řešení](../backend/data/screenshots/M9-2026-D-11-reseni.png) — Graf výšky s chybějícími údaji, aritmetický průměr
- [2024 B 15](../backend/data/screenshots/M9-2024-B-15.png) · 61 % · [řešení](../backend/data/screenshots/M9-2024-B-15-reseni.png) — Sloupcový graf (chlapci, dívky) a procenta

*Kruhový diagram*
- [2022 A 14](../backend/data/screenshots/M9-2022-A-14.png) · 35 % · [řešení](../backend/data/screenshots/M9-2022-A-14-reseni.png) — Kruhový diagram, dopočet četností, aritmetický průměr
- [2025 B 11](../backend/data/screenshots/M9-2025-B-11.png) · 68 % · [řešení](../backend/data/screenshots/M9-2025-B-11-reseni.png) — Kruhový diagram zadaný středovými úhly
- [2026 A 11](../backend/data/screenshots/M9-2026-A-11.png) · 66 % · [řešení](../backend/data/screenshots/M9-2026-A-11-reseni.png) — Kruhový diagram – zlomek, poměr, výpočet základu
- [2024 C 15](../backend/data/screenshots/M9-2024-C-15.png) · [řešení](../backend/data/screenshots/M9-2024-C-15-reseni.png) — Dva kruhové diagramy, procenta a počty
- [2024 D 8](../backend/data/screenshots/M9-2024-D-08.png) · [řešení](../backend/data/screenshots/M9-2024-D-08-reseni.png) — Dva kruhové diagramy – procenta z času, zaokrouhlení

*Aritmetický průměr from a table*
- [2025 A 14](../backend/data/screenshots/M9-2025-A-14.png) · 36 % · [řešení](../backend/data/screenshots/M9-2025-A-14-reseni.png) — Aritmetický průměr známek z tabulky četností
- [2025 D 7](../backend/data/screenshots/M9-2025-D-07.png) · 16 % · [řešení](../backend/data/screenshots/M9-2025-D-07-reseni.png) — Aritmetický průměr z tabulky s chybějícími údaji (všechna řešení)

All 20 tasks tagged `D-GRAF`: **2022** [A 14](../backend/data/screenshots/M9-2022-A-14.png), [B 7](../backend/data/screenshots/M9-2022-B-07.png), [C 11](../backend/data/screenshots/M9-2022-C-11.png) · **2023** [A 7](../backend/data/screenshots/M9-2023-A-07.png), [C 11](../backend/data/screenshots/M9-2023-C-11.png), [D 11](../backend/data/screenshots/M9-2023-D-11.png) · **2024** [A 7](../backend/data/screenshots/M9-2024-A-07.png), [B 15](../backend/data/screenshots/M9-2024-B-15.png), [C 15](../backend/data/screenshots/M9-2024-C-15.png), [D 8](../backend/data/screenshots/M9-2024-D-08.png) · **2025** [A 14](../backend/data/screenshots/M9-2025-A-14.png), [B 11](../backend/data/screenshots/M9-2025-B-11.png), [C 11](../backend/data/screenshots/M9-2025-C-11.png), [D 7](../backend/data/screenshots/M9-2025-D-07.png), [D 14](../backend/data/screenshots/M9-2025-D-14.png) · **2026** [A 1](../backend/data/screenshots/M9-2026-A-01.png), [A 11](../backend/data/screenshots/M9-2026-A-11.png), [B 11](../backend/data/screenshots/M9-2026-B-11.png), [C 11](../backend/data/screenshots/M9-2026-C-11.png), [D 11](../backend/data/screenshots/M9-2026-D-11.png)

---

<a id="t11"></a>
## 11. Úhly (G-UHLY)

2,1 points per standard test · in 14 of 16 · success 48 %.

**Must know**

- [seen] Pairs of angles: *vrcholové* (equal), *vedlejší* (sum 180°), *souhlasné* and *střídavé* at parallel lines (equal).
- [seen] Sum of the interior angles of a triangle (180°) and of a quadrilateral (360°); the exterior angle of a triangle.
- [seen] *Rovnoramenný* triangle: equal base angles; *rovnostranný*: 60°; right triangle: the two acute angles sum to 90°.
- [seen] Angles written as α, 2α, 3α, 4α or in a ratio 2 : 3 – set up an equation ([2022 A 12](../backend/data/screenshots/M9-2022-A-12.png) (50 %), [2023 A 14](../backend/data/screenshots/M9-2023-A-14.png) (42 %), [2024 C 8](../backend/data/screenshots/M9-2024-C-08.png)).
- [seen] *Osa úhlu* halves the angle ([2025 C 14](../backend/data/screenshots/M9-2025-C-14.png) (24 %), [2026 A 8](../backend/data/screenshots/M9-2026-A-08.png) (38 %)); perpendicular lines give 90°.
- [seen] Regular polygons: interior angle of a regular pentagon (108°), its axes of symmetry ([2026 C 8](../backend/data/screenshots/M9-2026-C-08.png) (29 %)); the hexagon as six equilateral triangles.
- [seen] Circle: radii make isosceles triangles ([2025 D 11](../backend/data/screenshots/M9-2025-D-11.png) (55 %)); a triangle whose circumcentre lies on a side is right-angled – *Thaletova věta* ([2026 A 8](../backend/data/screenshots/M9-2026-A-08.png) (38 %)).
- [seen, once] Degrees and minutes ([2024 D 14](../backend/data/screenshots/M9-2024-D-14.png)).
- [spec only] Measuring with a protractor as a task; *středový a obvodový úhel* are not in the specification and not in the tests beyond the Thales case.

**How it is tested.** One multiple-choice item among 12–14 in most tests, or a three-part result-only task
(2025 A 7, 2026 A 8, 2026 C 8), once the A/N bundle. A figure with a few angles given and Greek letters;
always "Velikosti úhlů neměřte, ale vypočtěte (obrázek je pouze ilustrativní)". Options include ranges
("menší než 120°", "větší než 150°").

**Where points are lost.** Figures that need two or three steps and an auxiliary idea (a parallel, a hidden
isosceles triangle): [2023 C 13](../backend/data/screenshots/M9-2023-C-13.png) (21 %), [2025 C 14](../backend/data/screenshots/M9-2025-C-14.png) (24 %), [2022 C 12](../backend/data/screenshots/M9-2022-C-12.png) (24 %). Straight chains score 50–67 %.

**Examples**

*Intersecting and parallel lines*
- [2022 A 12](../backend/data/screenshots/M9-2022-A-12.png) · 50 % · [řešení](../backend/data/screenshots/M9-2022-A-12-reseni.png) — Úhly u čtyř různoběžek (α a 3α)
- [2022 B 13](../backend/data/screenshots/M9-2022-B-13.png) · 54 % · [řešení](../backend/data/screenshots/M9-2022-B-13-reseni.png) — Úhly u rovnoběžek a příček
- [2022 C 12](../backend/data/screenshots/M9-2022-C-12.png) · 24 % · [řešení](../backend/data/screenshots/M9-2022-C-12-reseni.png) — Úhly u rovnoběžek a kolmic (2α, 3α)
- [2023 A 14](../backend/data/screenshots/M9-2023-A-14.png) · 42 % · [řešení](../backend/data/screenshots/M9-2023-A-14-reseni.png) — Úhly u rovnoběžek (2α, 4α)
- [2025 A 7](../backend/data/screenshots/M9-2025-A-07.png) · 57 % · [řešení](../backend/data/screenshots/M9-2025-A-07-reseni.png) — Úhly u rovnoběžek, kolmice a tří přímek
- [2024 D 14](../backend/data/screenshots/M9-2024-D-14.png) · [řešení](../backend/data/screenshots/M9-2024-D-14-reseni.png) — Součet úhlů u tří přímek (stupně a minuty)

*Triangles*
- [2023 B 12](../backend/data/screenshots/M9-2023-B-12.png) · 41 % · [řešení](../backend/data/screenshots/M9-2023-B-12-reseni.png) — Úhly v rovnoramenném trojúhelníku s rovnoběžkou
- [2023 D 13](../backend/data/screenshots/M9-2023-D-13.png) · 26 % · [řešení](../backend/data/screenshots/M9-2023-D-13-reseni.png) — Úhly v trojúhelníku a rovnoběžka
- [2024 A 11](../backend/data/screenshots/M9-2024-A-11.png) · 67 % · [řešení](../backend/data/screenshots/M9-2024-A-11-reseni.png) — Úhly v trojúhelníku tvořeném třemi přímkami
- [2024 B 13](../backend/data/screenshots/M9-2024-B-13.png) · 66 % · [řešení](../backend/data/screenshots/M9-2024-B-13-reseni.png) — Úhly u čtyř přímek a trojúhelníku
- [2024 C 8](../backend/data/screenshots/M9-2024-C-08.png) · [řešení](../backend/data/screenshots/M9-2024-C-08-reseni.png) — Úhly v trojúhelníku, poměr úhlů 2 : 3
- [2025 B 12](../backend/data/screenshots/M9-2025-B-12.png) · 51 % · [řešení](../backend/data/screenshots/M9-2025-B-12-reseni.png) — Úhly u shodných rovnoramenných trojúhelníků a rovnoběžek

*Composite figures, polygons, bisectors*
- [2022 D 12](../backend/data/screenshots/M9-2022-D-12.png) · 32 % · [řešení](../backend/data/screenshots/M9-2022-D-12-reseni.png) — Úhly ve složeném útvaru s rovnostrannými trojúhelníky
- [2023 C 13](../backend/data/screenshots/M9-2023-C-13.png) · 21 % · [řešení](../backend/data/screenshots/M9-2023-C-13-reseni.png) — Úhly v pětiúhelníku složeném z trojúhelníků
- [2025 C 14](../backend/data/screenshots/M9-2025-C-14.png) · 24 % · [řešení](../backend/data/screenshots/M9-2025-C-14-reseni.png) — Úhly v obdélníku s osami úhlů
- [2026 C 8](../backend/data/screenshots/M9-2026-C-08.png) · 29 % · [řešení](../backend/data/screenshots/M9-2026-C-08-reseni.png) — Úhly v pravidelném pětiúhelníku s osami souměrnosti

*Circle*
- [2025 D 11](../backend/data/screenshots/M9-2025-D-11.png) · 55 % · [řešení](../backend/data/screenshots/M9-2025-D-11-reseni.png) — Úhly v kružnici s průměry
- [2026 A 8](../backend/data/screenshots/M9-2026-A-08.png) · 38 % · [řešení](../backend/data/screenshots/M9-2026-A-08-reseni.png) — Úhly v trojúhelníku vepsaném do půlkružnice, osa úhlu, výška

All 18 tasks tagged `G-UHLY`: **2022** [A 12](../backend/data/screenshots/M9-2022-A-12.png), [B 13](../backend/data/screenshots/M9-2022-B-13.png), [C 12](../backend/data/screenshots/M9-2022-C-12.png), [D 12](../backend/data/screenshots/M9-2022-D-12.png) · **2023** [A 14](../backend/data/screenshots/M9-2023-A-14.png), [B 12](../backend/data/screenshots/M9-2023-B-12.png), [C 13](../backend/data/screenshots/M9-2023-C-13.png), [D 13](../backend/data/screenshots/M9-2023-D-13.png) · **2024** [A 11](../backend/data/screenshots/M9-2024-A-11.png), [B 13](../backend/data/screenshots/M9-2024-B-13.png), [C 8](../backend/data/screenshots/M9-2024-C-08.png), [D 14](../backend/data/screenshots/M9-2024-D-14.png) · **2025** [A 7](../backend/data/screenshots/M9-2025-A-07.png), [B 12](../backend/data/screenshots/M9-2025-B-12.png), [C 14](../backend/data/screenshots/M9-2025-C-14.png), [D 11](../backend/data/screenshots/M9-2025-D-11.png) · **2026** [A 8](../backend/data/screenshots/M9-2026-A-08.png), [C 8](../backend/data/screenshots/M9-2026-C-08.png)

---

<a id="t12"></a>
## 12. Obvod a obsah rovinných útvarů (G-ROV)

2,2 points per standard test · in 14 of 16 · success 32 %, 22 % blank.

**Must know**

- [seen] Perimeter and area of *čtverec, obdélník, trojúhelník, rovnoběžník, kosočtverec, lichoběžník*; none of the formulas is printed.
- [seen] **Backwards**: side of a square from its area (√), side of a rectangle from area and the other side, height of a triangle or trapezoid from its area ([2022 D 8](../backend/data/screenshots/M9-2022-D-08.png) (16 %)).
- [seen] The right triangle's area from its legs; the height to the hypotenuse or the height of a rhombus from the area computed two ways ([2023 B 11](../backend/data/screenshots/M9-2023-B-11.png) (60 %): 4,8 cm).
- [seen] *Pravoúhlý lichoběžník* split into a rectangle and a right triangle, and *rovnoramenný lichoběžník* split symmetrically – the standard route to a missing side (with topic 13).
- [seen] Composite figures: nested squares, a figure cut into congruent triangles or rectangles, a rectangle made of two squares; perimeters of rearranged pieces ([2026 C 6](../backend/data/screenshots/M9-2026-C-06.png) (14 %)).
- [seen] Perimeter relations expressed with a variable ([2023 A 8](../backend/data/screenshots/M9-2023-A-08.png) (25 %), [2024 A 13](../backend/data/screenshots/M9-2024-A-13.png) (31 %), [2026 D 6](../backend/data/screenshots/M9-2026-D-06.png) (30 %)).
- [seen, once] *Trojúhelníková nerovnost*: with a = 7, b = 30 and an integer perimeter, c is between 24 and 36 ([2026 B 8](../backend/data/screenshots/M9-2026-B-08.png) (11 %)).
- [seen] Objects spaced along a perimeter: number of gaps = number of objects on a closed path ([2025 A 8](../backend/data/screenshots/M9-2025-A-08.png) (13 %)).
- [spec only] **Podobnost trojúhelníků** (věty sss, sus, uu; *poměr podobnosti*) and *shodnost* (sss, sus, usu) as named tools; area and perimeter estimated on a square grid as a task of its own.

**How it is tested.** A result-only task among 6–8 with a figure and two or three sub-items ("Vypočtěte v
cm² obsah …, v cm obvod …"), or a multiple-choice item. Lengths are integers; areas are often perfect
squares (9, 16, 144 cm²).

**Where points are lost.** 22 % of candidates leave these tasks blank. The backward
tasks and the composite figures are the hard ones; a direct area from given sides does not occur alone.

**Examples**

*Squares and rectangles*
- [2022 B 8](../backend/data/screenshots/M9-2022-B-08.png) · 37 % · [řešení](../backend/data/screenshots/M9-2022-B-08-reseni.png) — Vnořené čtverce – strana z obsahu (odmocnina), obvod
- [2025 A 5](../backend/data/screenshots/M9-2025-A-05.png) · 41 % · [řešení](../backend/data/screenshots/M9-2025-A-05-reseni.png) — Plánek pozemku – rozměr z obsahu, procenta z rozlohy
- [2026 D 6](../backend/data/screenshots/M9-2026-D-06.png) · 30 % · [řešení](../backend/data/screenshots/M9-2026-D-06-reseni.png) — Obdélník složený ze dvou obdélníků – obvody, obsah
- [2023 D 12](../backend/data/screenshots/M9-2023-D-12.png) · 20 % · [řešení](../backend/data/screenshots/M9-2023-D-12-reseni.png) — Obvod obdélníku složeného ze dvou čtverců
- [2024 A 13](../backend/data/screenshots/M9-2024-A-13.png) · 31 % · [řešení](../backend/data/screenshots/M9-2024-A-13-reseni.png) — Obvod čtverce děleného na obdélníky

*Triangles and trapezoids*
- [2023 A 6](../backend/data/screenshots/M9-2023-A-06.png) · 25 % · [řešení](../backend/data/screenshots/M9-2023-A-06-reseni.png) — Obsah trojúhelníku a pravoúhlého lichoběžníku
- [2022 D 8](../backend/data/screenshots/M9-2022-D-08.png) · 16 % · [řešení](../backend/data/screenshots/M9-2022-D-08-reseni.png) — Výška trojúhelníku a lichoběžníku z obsahů
- [2024 A 6](../backend/data/screenshots/M9-2024-A-06.png) · 27 % · [řešení](../backend/data/screenshots/M9-2024-A-06-reseni.png) — Pravoúhlý lichoběžník – obsah a rameno (Pythagorova věta)
- [2024 B 6](../backend/data/screenshots/M9-2024-B-06.png) · 41 % · [řešení](../backend/data/screenshots/M9-2024-B-06-reseni.png) — Lichoběžník – obsah a obvod (Pythagorova věta)
- [2024 C 6](../backend/data/screenshots/M9-2024-C-06.png) · [řešení](../backend/data/screenshots/M9-2024-C-06-reseni.png) — Pravoúhlý lichoběžník – výška z obsahu trojúhelníku, obsah
- [2025 B 8](../backend/data/screenshots/M9-2025-B-08.png) · 32 % · [řešení](../backend/data/screenshots/M9-2025-B-08-reseni.png) — Pravoúhlý lichoběžník – obsah, obvod, obvod rovnoběžníku
- [2025 D 8](../backend/data/screenshots/M9-2025-D-08.png) · 31 % · [řešení](../backend/data/screenshots/M9-2025-D-08-reseni.png) — Lichoběžník vystřižený ze čtverce – obsah, obvod
- [2026 A 13](../backend/data/screenshots/M9-2026-A-13.png) · 34 % · [řešení](../backend/data/screenshots/M9-2026-A-13-reseni.png) — Obsah rovnoramenného trojúhelníku z obvodu (Pythagorova věta)

*Kosočtverec, composite figures*
- [2023 B 11](../backend/data/screenshots/M9-2023-B-11.png) · 60 % · [řešení](../backend/data/screenshots/M9-2023-B-11-reseni.png) — Kosočtverec složený ze čtyř trojúhelníků – strana, výška
- [2024 A 12](../backend/data/screenshots/M9-2024-A-12.png) · 43 % · [řešení](../backend/data/screenshots/M9-2024-A-12-reseni.png) — Obvod obrazce ze 7 shodných rovnoramenných trojúhelníků
- [2026 C 6](../backend/data/screenshots/M9-2026-C-06.png) · 14 % · [řešení](../backend/data/screenshots/M9-2026-C-06-reseni.png) — Obvody šestiúhelníků složených z trojúhelníků

*Trojúhelníková nerovnost, spacing*
- [2026 B 8](../backend/data/screenshots/M9-2026-B-08.png) · 11 % · [řešení](../backend/data/screenshots/M9-2026-B-08-reseni.png) — Trojúhelníková nerovnost – nejmenší a největší možný obvod
- [2025 A 8](../backend/data/screenshots/M9-2025-A-08.png) · 13 % · [řešení](../backend/data/screenshots/M9-2025-A-08-reseni.png) — Rostliny po obvodu čtyřúhelníku – rozestupy, zlomky, dělitelnost

All 23 tasks tagged `G-ROV`: **2022** [A 2](../backend/data/screenshots/M9-2022-A-02.png), [B 8](../backend/data/screenshots/M9-2022-B-08.png), [C 8](../backend/data/screenshots/M9-2022-C-08.png), [D 8](../backend/data/screenshots/M9-2022-D-08.png) · **2023** [A 6](../backend/data/screenshots/M9-2023-A-06.png), [A 8](../backend/data/screenshots/M9-2023-A-08.png), [B 11](../backend/data/screenshots/M9-2023-B-11.png), [D 12](../backend/data/screenshots/M9-2023-D-12.png) · **2024** [A 6](../backend/data/screenshots/M9-2024-A-06.png), [A 12](../backend/data/screenshots/M9-2024-A-12.png), [A 13](../backend/data/screenshots/M9-2024-A-13.png), [B 6](../backend/data/screenshots/M9-2024-B-06.png), [C 6](../backend/data/screenshots/M9-2024-C-06.png) · **2025** [A 5](../backend/data/screenshots/M9-2025-A-05.png), [A 8](../backend/data/screenshots/M9-2025-A-08.png), [B 8](../backend/data/screenshots/M9-2025-B-08.png), [D 8](../backend/data/screenshots/M9-2025-D-08.png), [D 16](../backend/data/screenshots/M9-2025-D-16.png) · **2026** [A 13](../backend/data/screenshots/M9-2026-A-13.png), [B 8](../backend/data/screenshots/M9-2026-B-08.png), [C 6](../backend/data/screenshots/M9-2026-C-06.png), [C 16](../backend/data/screenshots/M9-2026-C-16.png), [D 6](../backend/data/screenshots/M9-2026-D-06.png)

---

<a id="t13"></a>
## 13. Pythagorova věta (G-PYT)

1,0 point per standard test as its share of mixed tasks · in 11 of 16 · success 40 % · never asked for by name.

**Must know**

- [seen] The theorem in both directions: hypotenuse from the legs, a leg from the hypotenuse and the other leg; the words *odvěsna* and *přepona* ("nejdelší strana" in [2022 C 8](../backend/data/screenshots/M9-2022-C-08.png) (30 %)).
- [seen] Recognizing the integer triples and their multiples: 3–4–5 (6–8–10, 9–12–15, 30–40–50), 5–12–13, 8–15–17, 9–40–41. With the printed squares (17² = 289, 15² = 225) each takes one subtraction.
- [seen] Finding the right triangle yourself: the height of an isosceles triangle or trapezoid, the slanted side of a right trapezoid, a diagonal of a rectangle, a path across a field.
- [seen] In solids: *stěnová úhlopříčka* of a cuboid ([2023 A 12](../backend/data/screenshots/M9-2023-A-12.png) (39 %)), the hypotenuse of a triangular base as an edge of the prism ([2022 A 6](../backend/data/screenshots/M9-2022-A-06.png) (30 %), [2022 D 13](../backend/data/screenshots/M9-2022-D-13.png) (25 %)), a cuboid inscribed in a cylinder (diagonal of the base = diameter, [2023 C 7](../backend/data/screenshots/M9-2023-C-07.png) (19 %)).
- [spec only] The space diagonal (*tělesová úhlopříčka*) is not in the specification wording ("délky hrany a stěnové úhlopříčky") and not in the tests. Non-integer roots: in every task listed below whose numbers I traced (all except 2025 C 12, where the figure is needed) the three sides are whole numbers.

**How it is tested.** As a hidden step inside an area, perimeter, surface or volume task. The right angle is
stated in the text ("pravoúhlý lichoběžník", "odvěsny délek 6 cm a 8 cm") or follows from the figure.

**Where points are lost.** Not seeing that the theorem is needed. [2023 D 14](../backend/data/screenshots/M9-2023-D-14.png) (14 %) (difference of surfaces after
cutting a cuboid diagonally) got 14 % with a 20 % guessing rate.

**Examples**

*In the plane*
- [2022 C 8](../backend/data/screenshots/M9-2022-C-08.png) · 30 % · [řešení](../backend/data/screenshots/M9-2022-C-08-reseni.png) — Obvod obdélníku z obsahu; obsah pravoúhlého trojúhelníku (Pythagorova věta)
- [2024 A 6](../backend/data/screenshots/M9-2024-A-06.png) · 27 % · [řešení](../backend/data/screenshots/M9-2024-A-06-reseni.png) — Pravoúhlý lichoběžník – obsah a rameno (Pythagorova věta)
- [2024 B 2](../backend/data/screenshots/M9-2024-B-02.png) · 34 % · [řešení](../backend/data/screenshots/M9-2024-B-02-reseni.png) — O kolik procent je cesta po odvěsnách delší než po přeponě
- [2024 B 6](../backend/data/screenshots/M9-2024-B-06.png) · 41 % · [řešení](../backend/data/screenshots/M9-2024-B-06-reseni.png) — Lichoběžník – obsah a obvod (Pythagorova věta)
- [2025 B 8](../backend/data/screenshots/M9-2025-B-08.png) · 32 % · [řešení](../backend/data/screenshots/M9-2025-B-08-reseni.png) — Pravoúhlý lichoběžník – obsah, obvod, obvod rovnoběžníku
- [2025 C 12](../backend/data/screenshots/M9-2025-C-12.png) · 38 % · [řešení](../backend/data/screenshots/M9-2025-C-12-reseni.png) — Uzavřený okruh s kolmými úseky – Pythagorova věta
- [2025 D 8](../backend/data/screenshots/M9-2025-D-08.png) · 31 % · [řešení](../backend/data/screenshots/M9-2025-D-08-reseni.png) — Lichoběžník vystřižený ze čtverce – obsah, obvod
- [2026 A 13](../backend/data/screenshots/M9-2026-A-13.png) · 34 % · [řešení](../backend/data/screenshots/M9-2026-A-13-reseni.png) — Obsah rovnoramenného trojúhelníku z obvodu (Pythagorova věta)
- [2023 B 11](../backend/data/screenshots/M9-2023-B-11.png) · 60 % · [řešení](../backend/data/screenshots/M9-2023-B-11-reseni.png) — Kosočtverec složený ze čtyř trojúhelníků – strana, výška

*In solids*
- [2022 A 6](../backend/data/screenshots/M9-2022-A-06.png) · 30 % · [řešení](../backend/data/screenshots/M9-2022-A-06-reseni.png) — Objem trojbokého hranolu a pravidelného čtyřbokého hranolu (společná stěna, přepona = hrana)
- [2022 D 13](../backend/data/screenshots/M9-2022-D-13.png) · 25 % · [řešení](../backend/data/screenshots/M9-2022-D-13-reseni.png) — Obsah stěn tělesa slepeného z trojbokých hranolů (8–15–17)
- [2023 A 12](../backend/data/screenshots/M9-2023-A-12.png) · 39 % · [řešení](../backend/data/screenshots/M9-2023-A-12-reseni.png) — Lomená čára v kvádru – stěnové úhlopříčky
- [2023 C 7](../backend/data/screenshots/M9-2023-C-07.png) · 19 % · [řešení](../backend/data/screenshots/M9-2023-C-07-reseni.png) — Kvádr vepsaný do válce – poloměr (Pythagorova věta), objem válce
- [2023 D 14](../backend/data/screenshots/M9-2023-D-14.png) · 14 % · [řešení](../backend/data/screenshots/M9-2023-D-14-reseni.png) — Rozdíl povrchů kvádru a pětibokého hranolu

All 14 tasks tagged `G-PYT`: **2022** [A 6](../backend/data/screenshots/M9-2022-A-06.png), [C 8](../backend/data/screenshots/M9-2022-C-08.png), [D 13](../backend/data/screenshots/M9-2022-D-13.png) · **2023** [A 12](../backend/data/screenshots/M9-2023-A-12.png), [B 11](../backend/data/screenshots/M9-2023-B-11.png), [C 7](../backend/data/screenshots/M9-2023-C-07.png), [D 14](../backend/data/screenshots/M9-2023-D-14.png) · **2024** [A 6](../backend/data/screenshots/M9-2024-A-06.png), [B 2](../backend/data/screenshots/M9-2024-B-02.png), [B 6](../backend/data/screenshots/M9-2024-B-06.png) · **2025** [B 8](../backend/data/screenshots/M9-2025-B-08.png), [C 12](../backend/data/screenshots/M9-2025-C-12.png), [D 8](../backend/data/screenshots/M9-2025-D-08.png) · **2026** [A 13](../backend/data/screenshots/M9-2026-A-13.png)

---

<a id="t14"></a>
## 14. Kruh, kružnice, π (G-KRUH)

0,9 points per standard test (3,0 in 2024) · in 9 of 16 · success 35 %.

**Must know**

- [seen] o = 2πr and S = πr² (printed), with *poloměr* and *průměr* not confused.
- [seen] Backwards: radius or diameter from the area (S = π·144 cm² → d = 24 cm; S = 314 dm² → r = 10 dm).
- [seen] Parts of a circle: *půlkruh*, *čtvrtkruh*, a fifth or a sixth as a *výseč* – area is the fraction of πr², and the **perimeter of a part = arc + the straight sides** ([2022 A 13](../backend/data/screenshots/M9-2022-A-13.png) (40 %): 2·10 + 2π·10/5 ≐ 33 cm).
- [seen] Figures bounded by arcs: area as square minus quarter-circles ([2024 A 8](../backend/data/screenshots/M9-2024-A-08.png) (22 %)).
- [seen] Computing with π ≐ 3,14 by hand and rounding as instructed; or leaving π in the result when the options are "500π cm³" ([2025 B 14](../backend/data/screenshots/M9-2025-B-14.png) (35 %)).
- [seen] Circles in a square grid or on tiles: the radius is read from the grid ([2024 B 14](../backend/data/screenshots/M9-2024-B-14.png) (56 %), [2025 C 8](../backend/data/screenshots/M9-2025-C-08.png) (20 %)).
- [seen] The circle in solids: cylinder (topic 15).
- [spec only] *Tečna, sečna, vnější přímka*; *vzájemná poloha dvou kružnic*; *body dotyku*; constructing a tangent at a point of a circle; *kružnice opsaná trojúhelníku* as a construction by name (its centre is used in [2026 A 8](../backend/data/screenshots/M9-2026-A-08.png) (38 %) and [2026 C 10](../backend/data/screenshots/M9-2026-C-10.png) (25 %)).

**How it is tested.** A result-only task with a figure, or multiple choice. Where the result is rounded,
the rounding matches π ≐ 3,14; I found no task that needs 22/7. Radii are mostly round (5, 10, 50), so the
multiplication by 3,14 stays short.

**Where points are lost.** The perimeter of a sector (forgetting the two radii) and unit changes with
rounding ([2024 C 7](../backend/data/screenshots/M9-2024-C-07.png): areas in dm², answers in whole metres).

**Examples**

- [2022 A 13](../backend/data/screenshots/M9-2022-A-13.png) · 40 % · [řešení](../backend/data/screenshots/M9-2022-A-13-reseni.png) — Obvod kruhové výseče (pětina kruhu, r = 10 cm)
- [2023 B 8](../backend/data/screenshots/M9-2023-B-08.png) · 24 % · [řešení](../backend/data/screenshots/M9-2023-B-08-reseni.png) — Průměr kruhu z obsahu; objem válce z obsahu řezu, zaokrouhlení
- [2026 B 7](../backend/data/screenshots/M9-2026-B-07.png) · 31 % · [řešení](../backend/data/screenshots/M9-2026-B-07-reseni.png) — Kruh dělený na části – poměr obsahů, obvod části (zaokrouhlení)
- [2025 C 8](../backend/data/screenshots/M9-2025-C-08.png) · 20 % · [řešení](../backend/data/screenshots/M9-2025-C-08-reseni.png) — Obsah kruhu na dlaždici; počty kruhů na podlaze
- [2024 A 8](../backend/data/screenshots/M9-2024-A-08.png) · 22 % · [řešení](../backend/data/screenshots/M9-2024-A-08-reseni.png) — Obsah a obvod obrazce ohraničeného čtvrtkružnicemi
- [2024 B 14](../backend/data/screenshots/M9-2024-B-14.png) · 56 % · [řešení](../backend/data/screenshots/M9-2024-B-14-reseni.png) — Obsah půlkruhu ve čtvercové síti
- [2024 C 7](../backend/data/screenshots/M9-2024-C-07.png) · [řešení](../backend/data/screenshots/M9-2024-C-07-reseni.png) — Obvod kruhu z obsahu; poloměr čtvrtkruhu z obsahu

All 14 tasks tagged `G-KRUH`: **2022** [A 13](../backend/data/screenshots/M9-2022-A-13.png), [B 12](../backend/data/screenshots/M9-2022-B-12.png), [C 14](../backend/data/screenshots/M9-2022-C-14.png) · **2023** [A 13](../backend/data/screenshots/M9-2023-A-13.png), [B 8](../backend/data/screenshots/M9-2023-B-08.png), [C 7](../backend/data/screenshots/M9-2023-C-07.png) · **2024** [A 2](../backend/data/screenshots/M9-2024-A-02.png), [A 8](../backend/data/screenshots/M9-2024-A-08.png), [B 14](../backend/data/screenshots/M9-2024-B-14.png), [C 2](../backend/data/screenshots/M9-2024-C-02.png), [C 7](../backend/data/screenshots/M9-2024-C-07.png) · **2025** [B 14](../backend/data/screenshots/M9-2025-B-14.png), [C 8](../backend/data/screenshots/M9-2025-C-08.png) · **2026** [B 7](../backend/data/screenshots/M9-2026-B-07.png)

---

<a id="t15"></a>
## 15. Tělesa – objem, povrch, sítě (G-TEL)

3,1 points per standard test (1,0 in 2024) · in 16 of 16 · success 39 %.

**Must know**

- [seen] *Krychle* and *kvádr*: volume, surface, sum of all edges (12a; 4·(a + b + c)), and backwards – edge from the surface (54 cm² → 3 cm) or from the sum of edges.
- [seen] *Kolmý hranol* with any base – triangle, right triangle, rhombus, trapezoid, pentagon: V = base area × height; surface = 2 bases + *plášť*; *pravidelný čtyřboký hranol* (square base).
- [seen] *Rotační válec*: V = πr²v, plášť = 2πr·v, S = 2πr² + 2πrv; the plášť unrolled is a rectangle (a square in [2022 B 12](../backend/data/screenshots/M9-2022-B-12.png) (56 %), so v = 2πr).
- [seen] *Síť*: recognising the net of a cube and a prism and reading dimensions from it ([2022 B 11](../backend/data/screenshots/M9-2022-B-11.png) (49 %), [2026 D 14](../backend/data/screenshots/M9-2026-D-14.png) (31 %)).
- [seen] **Bodies glued together or cut apart**: the surface changes by the faces that disappear or appear ([2024 C 11](../backend/data/screenshots/M9-2024-C-11.png), [2026 B 13](../backend/data/screenshots/M9-2026-B-13.png) (22 %) – cutting small cubes out of corners leaves the surface unchanged: 22 %), the volume adds or subtracts.
- [seen] Spatial imagination with small cubes: counting cubes in a 4×4×4 cube by position ([2025 B 13](../backend/data/screenshots/M9-2025-B-13.png) (25 %)).
- [seen] A real object read as a prism lying on its side (pool with a sloping floor = prism with a trapezoid base, [2025 A 12](../backend/data/screenshots/M9-2025-A-12.png) (25 %)).
- [seen] Relations instead of numbers: "obsah pláště je třikrát větší než obsah podstavy", "povrch o 72 cm² větší" → an equation for the height.
- [seen] Volumes with units: litres ↔ cm³, water poured from one cylinder into another ([2024 C 2](../backend/data/screenshots/M9-2024-C-02.png)).
- [spec only] **Jehlan**: recognising it in *volné rovnoběžné promítání*, its net, its views from above and from the side, "metrické a polohové vlastnosti". **Koule**: radius and diameter in word problems. Views of a body (*pohled shora, zepředu, zprava*) and sketching a body or a net as a task. The specification does **not** ask for the volume or surface of a pyramid, cone or sphere, and no such computation occurs in the 20 tests.

**How it is tested.** One or two multiple-choice items among 12–14 in nearly every standard test, the A/N
bundle twice, and a result-only task among 6–7 in some. Bodies are drawn in oblique projection with hidden
edges dashed.

**Where points are lost.** Multi-step items in multiple choice: several score at or just above the 20 %
guessing rate ([2023 C 14](../backend/data/screenshots/M9-2023-C-14.png) (18 %), [2023 D 14](../backend/data/screenshots/M9-2023-D-14.png) (14 %), [2026 B 13](../backend/data/screenshots/M9-2026-B-13.png) (22 %)).

**Examples**

*Krychle, kvádr*
- [2025 D 12](../backend/data/screenshots/M9-2025-D-12.png) · 29 % · [řešení](../backend/data/screenshots/M9-2025-D-12-reseni.png) — Rozdíl objemů krychlí z povrchu a součtu hran
- [2025 C 13](../backend/data/screenshots/M9-2025-C-13.png) · 26 % · [řešení](../backend/data/screenshots/M9-2025-C-13-reseni.png) — Krychle polepená čtverci – hrana z obsahu
- [2026 C 7](../backend/data/screenshots/M9-2026-C-07.png) · 16 % · [řešení](../backend/data/screenshots/M9-2026-C-07-reseni.png) — Hrana krychle z povrchu; objem hranolu
- [2023 A 2](../backend/data/screenshots/M9-2023-A-02.png) · 28 % · [řešení](../backend/data/screenshots/M9-2023-A-02-reseni.png) — 2.2: a cuboid cut into cubes, dm³ → cm³

*Hranoly*
- [2022 A 6](../backend/data/screenshots/M9-2022-A-06.png) · 30 % · [řešení](../backend/data/screenshots/M9-2022-A-06-reseni.png) — Objem trojbokého hranolu a pravidelného čtyřbokého hranolu (společná stěna, přepona = hrana)
- [2022 C 13](../backend/data/screenshots/M9-2022-C-13.png) · 32 % · [řešení](../backend/data/screenshots/M9-2022-C-13-reseni.png) — Objem trojbokého hranolu vzniklého řezem kvádru
- [2023 B 13](../backend/data/screenshots/M9-2023-B-13.png) · 45 % · [řešení](../backend/data/screenshots/M9-2023-B-13-reseni.png) — Objem trojbokého hranolu
- [2023 C 14](../backend/data/screenshots/M9-2023-C-14.png) · 18 % · [řešení](../backend/data/screenshots/M9-2023-C-14-reseni.png) — Objem pravidelného čtyřbokého hranolu z povrchu
- [2025 A 12](../backend/data/screenshots/M9-2025-A-12.png) · 25 % · [řešení](../backend/data/screenshots/M9-2025-A-12-reseni.png) — Objem bazénu se šikmým dnem
- [2026 A 14](../backend/data/screenshots/M9-2026-A-14.png) · 33 % · [řešení](../backend/data/screenshots/M9-2026-A-14-reseni.png) — Rozdíl výšek hranolů z rozdílu povrchů
- [2026 D 14](../backend/data/screenshots/M9-2026-D-14.png) · 31 % · [řešení](../backend/data/screenshots/M9-2026-D-14-reseni.png) — Objem hranolu s kosočtvercovou podstavou ze sítě

*Válec*
- [2022 B 12](../backend/data/screenshots/M9-2022-B-12.png) · 56 % · [řešení](../backend/data/screenshots/M9-2022-B-12-reseni.png) — Plášť válce je čtverec – výška válce
- [2022 C 14](../backend/data/screenshots/M9-2022-C-14.png) · 24 % · [řešení](../backend/data/screenshots/M9-2022-C-14-reseni.png) — Poměr obsahu pláště a podstavy válce
- [2023 A 13](../backend/data/screenshots/M9-2023-A-13.png) · 30 % · [řešení](../backend/data/screenshots/M9-2023-A-13-reseni.png) — Povrch válce (plášť = trojnásobek podstavy)
- [2023 B 8](../backend/data/screenshots/M9-2023-B-08.png) · 24 % · [řešení](../backend/data/screenshots/M9-2023-B-08-reseni.png) — Průměr kruhu z obsahu; objem válce z obsahu řezu, zaokrouhlení
- [2023 C 7](../backend/data/screenshots/M9-2023-C-07.png) · 19 % · [řešení](../backend/data/screenshots/M9-2023-C-07-reseni.png) — Kvádr vepsaný do válce – poloměr (Pythagorova věta), objem válce
- [2025 A 6](../backend/data/screenshots/M9-2025-A-06.png) · 18 % · [řešení](../backend/data/screenshots/M9-2025-A-06-reseni.png) — Válcový sud – objem v litrech z výšky hladiny v mm a naopak
- [2025 B 14](../backend/data/screenshots/M9-2025-B-14.png) · 35 % · [řešení](../backend/data/screenshots/M9-2025-B-14-reseni.png) — Objem dvou válců jako násobek π
- [2024 A 2](../backend/data/screenshots/M9-2024-A-02.png) · 16 % · [řešení](../backend/data/screenshots/M9-2024-A-02-reseni.png) — Objem dutého válce, zaokrouhlení, π ≐ 3,14
- [2024 C 2](../backend/data/screenshots/M9-2024-C-02.png) · [řešení](../backend/data/screenshots/M9-2024-C-02-reseni.png) — Přelití vody mezi válcovými nádobami – výška hladiny

*Glued and cut bodies, nets, small cubes*
- [2022 B 11](../backend/data/screenshots/M9-2022-B-11.png) · 49 % · [řešení](../backend/data/screenshots/M9-2022-B-11-reseni.png) — Hranol slepený ze tří krychlí, síť, povrch
- [2022 D 13](../backend/data/screenshots/M9-2022-D-13.png) · 25 % · [řešení](../backend/data/screenshots/M9-2022-D-13-reseni.png) — Obsah stěn tělesa slepeného z trojbokých hranolů (8–15–17)
- [2022 D 14](../backend/data/screenshots/M9-2022-D-14.png) · 34 % · [řešení](../backend/data/screenshots/M9-2022-D-14-reseni.png) — Objem téhož tělesa
- [2023 D 14](../backend/data/screenshots/M9-2023-D-14.png) · 14 % · [řešení](../backend/data/screenshots/M9-2023-D-14-reseni.png) — Rozdíl povrchů kvádru a pětibokého hranolu
- [2025 A 11](../backend/data/screenshots/M9-2025-A-11.png) · 54 % · [řešení](../backend/data/screenshots/M9-2025-A-11-reseni.png) — Tělesa slepená ze dvou kvádrů – hrany a povrch
- [2025 B 13](../backend/data/screenshots/M9-2025-B-13.png) · 25 % · [řešení](../backend/data/screenshots/M9-2025-B-13-reseni.png) — Krychle 4×4×4 z krychliček – prostorová představivost
- [2026 B 13](../backend/data/screenshots/M9-2026-B-13.png) · 22 % · [řešení](../backend/data/screenshots/M9-2026-B-13-reseni.png) — Povrch krychle s vyříznutými krychličkami
- [2024 C 11](../backend/data/screenshots/M9-2024-C-11.png) · [řešení](../backend/data/screenshots/M9-2024-C-11-reseni.png) — Změna povrchu po rozříznutí krychle
- [2026 A 15](../backend/data/screenshots/M9-2026-A-15.png) · 56 % · [řešení](../backend/data/screenshots/M9-2026-A-15-reseni.png) — O kolik procent větší/menší objem těles ze základních kvádrů

All 30 tasks tagged `G-TEL`: **2022** [A 6](../backend/data/screenshots/M9-2022-A-06.png), [B 11](../backend/data/screenshots/M9-2022-B-11.png), [B 12](../backend/data/screenshots/M9-2022-B-12.png), [C 13](../backend/data/screenshots/M9-2022-C-13.png), [C 14](../backend/data/screenshots/M9-2022-C-14.png), [D 13](../backend/data/screenshots/M9-2022-D-13.png), [D 14](../backend/data/screenshots/M9-2022-D-14.png) · **2023** [A 12](../backend/data/screenshots/M9-2023-A-12.png), [A 13](../backend/data/screenshots/M9-2023-A-13.png), [B 8](../backend/data/screenshots/M9-2023-B-08.png), [B 13](../backend/data/screenshots/M9-2023-B-13.png), [C 7](../backend/data/screenshots/M9-2023-C-07.png), [C 14](../backend/data/screenshots/M9-2023-C-14.png), [D 14](../backend/data/screenshots/M9-2023-D-14.png) · **2024** [A 2](../backend/data/screenshots/M9-2024-A-02.png), [C 2](../backend/data/screenshots/M9-2024-C-02.png), [C 11](../backend/data/screenshots/M9-2024-C-11.png) · **2025** [A 6](../backend/data/screenshots/M9-2025-A-06.png), [A 11](../backend/data/screenshots/M9-2025-A-11.png), [A 12](../backend/data/screenshots/M9-2025-A-12.png), [B 13](../backend/data/screenshots/M9-2025-B-13.png), [B 14](../backend/data/screenshots/M9-2025-B-14.png), [C 13](../backend/data/screenshots/M9-2025-C-13.png), [D 12](../backend/data/screenshots/M9-2025-D-12.png) · **2026** [A 14](../backend/data/screenshots/M9-2026-A-14.png), [A 15](../backend/data/screenshots/M9-2026-A-15.png), [B 13](../backend/data/screenshots/M9-2026-B-13.png), [C 7](../backend/data/screenshots/M9-2026-C-07.png), [D 7](../backend/data/screenshots/M9-2026-D-07.png), [D 14](../backend/data/screenshots/M9-2026-D-14.png)

---

<a id="t16"></a>
## 16. Konstrukční úlohy (G-KON)

5–6 points in every test of the sample (20 of 20) · success 32 %, 28 % blank · tasks 9 and 10.

**Must know – the properties the tasks rely on**

- [seen] *Rovnoramenný trojúhelník*: equal arms, the axis of symmetry is the perpendicular bisector of the base and passes through the main vertex; the height, median and angle bisector from the main vertex coincide.
- [seen] *Rovnostranný trojúhelník*: all sides equal, angles 60°, the height bisects the side.
- [seen] *Pravoúhlý trojúhelník*: the vertex with the right angle lies on the circle whose diameter is the hypotenuse (*Thaletova kružnice*), and conversely.
- [seen] *Výška* (perpendicular from a vertex to the opposite side's line) and *těžnice* (vertex to the midpoint of the opposite side), with the notation v_c, t_c ([2025 A 10](../backend/data/screenshots/M9-2025-A-10.png) (29 %)).
- [seen] *Čtverec*: equal perpendicular diagonals that bisect each other; centre equidistant from all sides and vertices.
- [seen] *Obdélník*: equal diagonals bisecting each other, so all four vertices lie on a circle around the centre ("bod V má stejnou vzdálenost od všech čtyř vrcholů", [2026 C 10](../backend/data/screenshots/M9-2026-C-10.png) (25 %)).
- [seen] *Rovnoběžník*: diagonals bisect each other; the centre S is the midpoint of both, so a vertex is the image of the opposite one in the point reflection in S.
- [seen] *Kosočtverec*: a parallelogram with an axis of symmetry along a diagonal; perpendicular diagonals ([2026 A 10](../backend/data/screenshots/M9-2026-A-10.png) (23 %) never says "kosočtverec"; 53 % left it blank).
- [seen] *Lichoběžník*: two parallel bases; *rovnoramenný* has an axis of symmetry; *pravoúhlý* has an arm perpendicular to the bases.
- [seen, once] *Pravidelný šestiúhelník*: side = radius of the circumscribed circle ([2026 B 9](../backend/data/screenshots/M9-2026-B-09.png) (15 %)).

**Must know – the elementary constructions**

- [seen] Perpendicular and parallel to a line through a point (set square).
- [seen] Midpoint and *osa úsečky*; a point reflected in a centre (*středová souměrnost*) and in a line (*osová souměrnost*).
- [seen] *Osa úhlu* ([2025 A 9](../backend/data/screenshots/M9-2025-A-09.png) (33 %)).
- [seen] A circle with a given centre and radius used to transfer a length ("Základna AB … má délku 6 cm", "Ramena mají délku 5 cm", "Strana BC je o 2 cm delší než strana AB", "Druhá úhlopříčka … má stejnou délku jako úsečka DM").
- [seen] An angle of given size at a point: 120°, 40° (protractor), 60° and 90° (compass and set square).
- [seen] *Thaletova kružnice* over a segment. The official keys name it in 2024 C, 2024 D and 2026 B; it is also the natural tool in [2023 B 10](../backend/data/screenshots/M9-2023-B-10.png) (43 %).
- [spec only] Triangle from sss, sus, usu as a plain task; *kružnice opsaná* by construction; tangent to a circle at its point; transferring an angle; a regular octagon; writing down the *postup konstrukce* (the specification says "bez zápisu postupu konstrukce", and no test asks for it).

**How it is tested.** The answer sheet has the given points and lines pre-printed. The text says which
vertices of which figure they are and adds one or two conditions; "Sestrojte vrcholy …, označte je
písmeny a … narýsujte." Only the drawing is marked. 18 of 40 tasks say "Najděte všechna řešení" and
then have exactly two. Some are split into two steps (first the centre, the axis or one vertex).

**Where points are lost.** By not starting: the second construction is the most skipped regular task (33 %
blank on average). Then by drawing one solution of two (−1 point), by "mírná
nepřesnost" (−1), missing labels, or a figure that does not satisfy all conditions. Success ranges from
72 % ([2022 B 9](../backend/data/screenshots/M9-2022-B-09.png) (72 %)) to 9 % ([2025 B 10](../backend/data/screenshots/M9-2025-B-10.png) (9 %)).

**The conditions are deliberately indirect.** Phrases that create the difficulty or the second solution:
"na přímce q leží jeden z vrcholů A, B", "Přímka o je osou některé strany", "Bod S je střed jednoho ramene",
"Bod M leží na úhlopříčce BD", "Na přímce p leží jedna ze tří výšek", "Dva ze tří bodů P, Q, R leží uvnitř
dvou různých stran".

**Examples**

*A midpoint or a centre is given*
- [2022 A 9](../backend/data/screenshots/M9-2022-A-09.png) · 31 % · [řešení](../backend/data/screenshots/M9-2022-A-09-reseni.png) — Rovnoramenný trojúhelník: dán vrchol C, střed ramene S, přímka q (2 řešení)
- [2022 A 10](../backend/data/screenshots/M9-2022-A-10.png) · 51 % · [řešení](../backend/data/screenshots/M9-2022-A-10-reseni.png) — Čtverec: dán střed O a přímka p se stranou BC
- [2022 D 9](../backend/data/screenshots/M9-2022-D-09.png) · 21 % · [řešení](../backend/data/screenshots/M9-2022-D-09-reseni.png) — Rovnoběžník: vrchol A, střed S, úhel ASB = 120°
- [2023 B 9](../backend/data/screenshots/M9-2023-B-09.png) · 64 % · [řešení](../backend/data/screenshots/M9-2023-B-09-reseni.png) — Rovnoramenný lichoběžník: základna AB, střed ramene S
- [2024 A 9](../backend/data/screenshots/M9-2024-A-09.png) · 31 % · [řešení](../backend/data/screenshots/M9-2024-A-09-reseni.png) — Rovnostranný trojúhelník: vrchol C a střed S strany AB
- [2024 D 9](../backend/data/screenshots/M9-2024-D-09.png) · [řešení](../backend/data/screenshots/M9-2024-D-09-reseni.png) — Obdélník: vrchol A, střed S, vrchol D na p (Thaletova kružnice, 2 řešení)
- [2024 D 10](../backend/data/screenshots/M9-2024-D-10.png) · [řešení](../backend/data/screenshots/M9-2024-D-10-reseni.png) — Pravoúhlý trojúhelník: vrchol C, střed strany S, strana rovnoběžná s p (2 řešení)
- [2025 C 10](../backend/data/screenshots/M9-2025-C-10.png) · 12 % · [řešení](../backend/data/screenshots/M9-2025-C-10-reseni.png) — Obdélník: vrchol A, střed strany S, vrchol D na p (2 řešení)
- [2026 C 9](../backend/data/screenshots/M9-2026-C-09.png) · 14 % · [řešení](../backend/data/screenshots/M9-2026-C-09-reseni.png) — Rovnoramenný trojúhelník: vrchol A, střed strany S, střed P na p (2 řešení)

*A given length or equal lengths (circle)*
- [2022 B 9](../backend/data/screenshots/M9-2022-B-09.png) · 72 % · [řešení](../backend/data/screenshots/M9-2022-B-09-reseni.png) — Rovnoramenný trojúhelník: vrchol C, základna délky 6 cm na přímce q
- [2022 D 10](../backend/data/screenshots/M9-2022-D-10.png) · 14 % · [řešení](../backend/data/screenshots/M9-2022-D-10-reseni.png) — Rovnoramenný trojúhelník: ramena 5 cm, vrchol na přímce, osa souměrnosti bodem Q (2 řešení)
- [2023 C 9](../backend/data/screenshots/M9-2023-C-09.png) · 21 % · [řešení](../backend/data/screenshots/M9-2023-C-09-reseni.png) — Pravoúhlý lichoběžník: strana AB, vrchol C na p, |AC| = |AB| (2 řešení)
- [2024 A 10](../backend/data/screenshots/M9-2024-A-10.png) · 26 % · [řešení](../backend/data/screenshots/M9-2024-A-10-reseni.png) — Obdélník: vrchol A, přímky, |BD| = |AE|
- [2025 B 10](../backend/data/screenshots/M9-2025-B-10.png) · 9 % · [řešení](../backend/data/screenshots/M9-2025-B-10-reseni.png) — Rovnoběžník: vrcholy A, D, úhlopříčky
- [2025 D 10](../backend/data/screenshots/M9-2025-D-10.png) · 4 % · [řešení](../backend/data/screenshots/M9-2025-D-10-reseni.png) — Rovnoběžník: vrcholy L, M, střed na p, |LM| = |LN| (2 řešení)
- [2026 A 9](../backend/data/screenshots/M9-2026-A-09.png) · 42 % · [řešení](../backend/data/screenshots/M9-2026-A-09-reseni.png) — Trojúhelník: AB kolmá k b, BC o 2 cm delší než AB, C na c (2 řešení)
- [2024 B 9](../backend/data/screenshots/M9-2024-B-09.png) · 32 % · [řešení](../backend/data/screenshots/M9-2024-B-09-reseni.png) — Kosočtverec: vrcholy A, B, vrchol C na přímce OA
- [2024 B 10](../backend/data/screenshots/M9-2024-B-10.png) · 37 % · [řešení](../backend/data/screenshots/M9-2024-B-10-reseni.png) — Rovnoramenný trojúhelník s vrcholem na kružnici (2 řešení)

*An axis of a side or of symmetry*
- [2022 C 9](../backend/data/screenshots/M9-2022-C-09.png) · 19 % · [řešení](../backend/data/screenshots/M9-2022-C-09-reseni.png) — Trojúhelník PQR: přímka o je osou některé strany (2 řešení)
- [2023 C 10](../backend/data/screenshots/M9-2023-C-10.png) · 17 % · [řešení](../backend/data/screenshots/M9-2023-C-10-reseni.png) — Rovnoramenný trojúhelník: základna AC, výška na p; osa souměrnosti
- [2024 C 10](../backend/data/screenshots/M9-2024-C-10.png) · [řešení](../backend/data/screenshots/M9-2024-C-10-reseni.png) — Rovnoramenný lichoběžník – osová souměrnost
- [2025 B 9](../backend/data/screenshots/M9-2025-B-09.png) · 19 % · [řešení](../backend/data/screenshots/M9-2025-B-09-reseni.png) — Rovnoramenný trojúhelník: vrcholy A, B, bod M na těžnici (2 řešení)
- [2025 D 9](../backend/data/screenshots/M9-2025-D-09.png) · 15 % · [řešení](../backend/data/screenshots/M9-2025-D-09-reseni.png) — Osa souměrnosti; rovnostranný trojúhelník a jeho obraz
- [2026 A 10](../backend/data/screenshots/M9-2026-A-10.png) · 23 % · [řešení](../backend/data/screenshots/M9-2026-A-10-reseni.png) — Rovnoběžník s osou souměrnosti (kosočtverec), poměr úhlopříček 2 : 1
- [2026 B 9](../backend/data/screenshots/M9-2026-B-09.png) · 15 % · [řešení](../backend/data/screenshots/M9-2026-B-09-reseni.png) — Pravidelný šestiúhelník: vrchol A, osa strany AB

*A right angle with vertices on a circle (Thales), circumscribed circle*
- [2023 B 10](../backend/data/screenshots/M9-2023-B-10.png) · 43 % · [řešení](../backend/data/screenshots/M9-2023-B-10-reseni.png) — Pravoúhlý trojúhelník vepsaný kružnici (Thaletova kružnice, 2 řešení)
- [2024 C 9](../backend/data/screenshots/M9-2024-C-09.png) · [řešení](../backend/data/screenshots/M9-2024-C-09-reseni.png) — Pravoúhlý lichoběžník s vrcholy na kružnici (Thaletova kružnice)
- [2026 B 10](../backend/data/screenshots/M9-2026-B-10.png) · 22 % · [řešení](../backend/data/screenshots/M9-2026-B-10-reseni.png) — Dva pravoúhlé trojúhelníky se společným vrcholem C (Thaletovy kružnice)
- [2023 A 9](../backend/data/screenshots/M9-2023-A-09.png) · 32 % · [řešení](../backend/data/screenshots/M9-2023-A-09-reseni.png) — Obdélník: vrcholy A, C a bod M na úhlopříčce BD
- [2026 C 10](../backend/data/screenshots/M9-2026-C-10.png) · 25 % · [řešení](../backend/data/screenshots/M9-2026-C-10-reseni.png) — Obdélník: bod U na straně, strana na k, V střed kružnice opsané
- [2026 D 10](../backend/data/screenshots/M9-2026-D-10.png) · 16 % · [řešení](../backend/data/screenshots/M9-2026-D-10-reseni.png) — Obdélník vepsaný kružnici: vrchol D, střed S, úhlopříčka bodem U

*Vertices on given lines, parallels and perpendiculars*
- [2022 B 10](../backend/data/screenshots/M9-2022-B-10.png) · 27 % · [řešení](../backend/data/screenshots/M9-2022-B-10-reseni.png) — Rovnoběžník: vrcholy A, C, strany rovnoběžné s p, úhlopříčka kolmá k p; nejprve střed S
- [2022 C 10](../backend/data/screenshots/M9-2022-C-10.png) · 23 % · [řešení](../backend/data/screenshots/M9-2022-C-10-reseni.png) — Obdélník: vrchol A, bod X na straně AB, vrcholy na rovnoběžkách c, p (2 řešení)
- [2023 D 9](../backend/data/screenshots/M9-2023-D-09.png) · 13 % · [řešení](../backend/data/screenshots/M9-2023-D-09-reseni.png) — Čtverec: strana na přímce a, body P, Q, R (2 řešení)
- [2023 D 10](../backend/data/screenshots/M9-2023-D-10.png) · 22 % · [řešení](../backend/data/screenshots/M9-2023-D-10-reseni.png) — Pravoúhlý trojúhelník: úhel 40°, vrcholy na přímkách (2 řešení)
- [2025 A 9](../backend/data/screenshots/M9-2025-A-09.png) · 33 % · [řešení](../backend/data/screenshots/M9-2025-A-09-reseni.png) — Osa úhlu dvou přímek; obdélník s vrcholy na přímkách
- [2026 D 9](../backend/data/screenshots/M9-2026-D-09.png) · 6 % · [řešení](../backend/data/screenshots/M9-2026-D-09-reseni.png) — Pravoúhlý rovnoramenný trojúhelník BCD; lichoběžník s vrcholem na p (2 řešení)

*Výška, těžnice; vertices on a given circle*
- [2025 A 10](../backend/data/screenshots/M9-2025-A-10.png) · 29 % · [řešení](../backend/data/screenshots/M9-2025-A-10-reseni.png) — Trojúhelník: výška v_c na přímce p, těžnice t_c na přímce q
- [2025 C 9](../backend/data/screenshots/M9-2025-C-09.png) · 21 % · [řešení](../backend/data/screenshots/M9-2025-C-09-reseni.png) — Rovnoramenný trojúhelník: vrchol B, výška BM, vrchol A na q
- [2023 A 10](../backend/data/screenshots/M9-2023-A-10.png) · 22 % · [řešení](../backend/data/screenshots/M9-2023-A-10-reseni.png) — Rovnoramenný trojúhelník s vrcholy na kružnici (2 řešení)

---

<a id="t17"></a>
## 17. Souměrnost (G-SOUM)

0,7 points per standard test as a topic of its own · in 4 of 16 · not in 2024 · mostly a tool inside constructions.

**Must know**

- [seen] *Osová souměrnost*: recognising an axis of symmetry of a figure (vertical, horizontal or diagonal) on a square grid; counting all axes; changing one square so that the figure becomes symmetric ([2022 D 11](../backend/data/screenshots/M9-2022-D-11.png) (53 %), [2023 D 8](../backend/data/screenshots/M9-2023-D-08.png) (37 %)).
- [seen] Constructing the image of a point or a triangle in an axis, and finding the axis from a point and its image – the axis is the perpendicular bisector of AA′ ([2025 D 9](../backend/data/screenshots/M9-2025-D-09.png) (15 %)).
- [seen] Axes of symmetry of the isosceles triangle, rectangle, rhombus, isosceles trapezoid, regular pentagon and hexagon.
- [seen] *Středová souměrnost* as "S is the midpoint", and *střed souměrnosti* of a parallelogram and of a regular hexagon ([2025 D 10](../backend/data/screenshots/M9-2025-D-10.png) (4 %), [2026 B 9](../backend/data/screenshots/M9-2026-B-09.png) (15 %)).
- [spec only] *Samodružný bod*, *samodružný útvar*; *vzor* and *obraz* as vocabulary items; constructing the image of a whole figure in a point reflection as a task of its own.

**Examples**

- [2022 D 11](../backend/data/screenshots/M9-2022-D-11.png) · 53 % · [řešení](../backend/data/screenshots/M9-2022-D-11-reseni.png) — Útvary ve čtvercové síti – počet os souměrnosti po přemístění čtverce
- [2023 D 8](../backend/data/screenshots/M9-2023-D-08.png) · 37 % · [řešení](../backend/data/screenshots/M9-2023-D-08-reseni.png) — Osová souměrnost ve čtvercové síti – odebrání čtverce (obě řešení)
- [2025 D 9](../backend/data/screenshots/M9-2025-D-09.png) · 15 % · [řešení](../backend/data/screenshots/M9-2025-D-09-reseni.png) — Osa souměrnosti; rovnostranný trojúhelník a jeho obraz
- [2026 A 10](../backend/data/screenshots/M9-2026-A-10.png) · 23 % · [řešení](../backend/data/screenshots/M9-2026-A-10-reseni.png) — Rovnoběžník s osou souměrnosti (kosočtverec), poměr úhlopříček 2 : 1
- [2026 C 8](../backend/data/screenshots/M9-2026-C-08.png) · 29 % · [řešení](../backend/data/screenshots/M9-2026-C-08-reseni.png) — axes of symmetry of a regular pentagon used for angles

All 4 tasks tagged `G-SOUM`: **2022** [D 11](../backend/data/screenshots/M9-2022-D-11.png) · **2023** [D 8](../backend/data/screenshots/M9-2023-D-08.png) · **2025** [D 9](../backend/data/screenshots/M9-2025-D-09.png) · **2026** [A 10](../backend/data/screenshots/M9-2026-A-10.png)

---

<a id="t18"></a>
## 18. Nestandardní úlohy, zákonitosti (X-NEST)

3,6 points per standard test · task 16 in all 16 standard tests · success 10 %, 36 % blank · in 2024 only [2024 B 8](../backend/data/screenshots/M9-2024-B-08.png) (29 %).

**Must know**

There is no curriculum content of its own here; the specification asks for *úsudek*, discovering
*zákonitosti*, and "jednoduché strategické a kombinatorické úlohy bez použití kombinatorických vzorců".
What the 20 tests actually require:

- [seen] Continuing a rule from the first 2–4 pictured steps and **tabulating** the counts step by step.
- [seen] Finding the n-th term for the common growth types: linear (add a constant), quadratic (n², n·(n + 1)/2 *trojúhelníková čísla*, (2n − 1)²), exponential (3ⁿ: [2023 A 16](../backend/data/screenshots/M9-2023-A-16.png) (5 %)).
- [seen] **Inverting the rule**: which step has 361 dark circles (361 = 19², so the 20th figure, [2024 B 8](../backend/data/screenshots/M9-2024-B-08.png) (29 %)); which figure has 225 triangles in its last band.
- [seen] Working with differences between consecutive steps ("počty … v posledním a v předposledním obrazci se liší o 96").
- [seen] Periodic processes: several actors acting every k-th round or second – think in cycles of the least common multiple ([2022 A 16](../backend/data/screenshots/M9-2022-A-16.png) (22 %), [2026 A 16](../backend/data/screenshots/M9-2026-A-16.png) (11 %)).
- [seen] Number sequences built by a rule, positions and values ([2022 D 16](../backend/data/screenshots/M9-2022-D-16.png) (13 %), [2025 B 16](../backend/data/screenshots/M9-2025-B-16.png) (12 %)).
- [seen] Systematic listing of cases when the task says "Najděte všechna řešení" ([2023 B 16](../backend/data/screenshots/M9-2023-B-16.png) (6 %), [2026 D 16](../backend/data/screenshots/M9-2026-D-16.png) (11 %)).
- [seen, once each] A geometric reasoning task on a rectangle ([2025 D 16](../backend/data/screenshots/M9-2025-D-16.png) (7 %)) and a token game ([2026 D 16](../backend/data/screenshots/M9-2026-D-16.png) (11 %)).

**How it is tested.** A *výchozí text* describing the rule, usually with a picture of the first figures.
Three result-only sub-items, 1 + 1 + 2 points: 16.1 a nearby term, 16.2 the rule inverted or a second
quantity, 16.3 the general law, a large term or all solutions.

**Where points are lost.** 16.1 is reachable by drawing or counting and was solved by 11–42 % in regular
terms; 16.3 by 1–3 % in seven of eight regular standard tests (11 % in 2022 A). For a perfect score this
task is the main obstacle, and it comes last, when time is short.

**Examples**

*Growing figures (linear and quadratic counts)*
- [2022 B 16](../backend/data/screenshots/M9-2022-B-16.png) · 10 % · [řešení](../backend/data/screenshots/M9-2022-B-16-reseni.png) — Hvězdičky v mřížových bodech obdélníku
- [2022 C 16](../backend/data/screenshots/M9-2022-C-16.png) · 4 % · [řešení](../backend/data/screenshots/M9-2022-C-16-reseni.png) — Obrazec z přímek a puntíků – zákonitost (druhé mocniny)
- [2023 B 16](../backend/data/screenshots/M9-2023-B-16.png) · 6 % · [řešení](../backend/data/screenshots/M9-2023-B-16-reseni.png) — Obrazce ve čtvercové síti, tmavá a světlá pole (všechna řešení)
- [2023 C 16](../backend/data/screenshots/M9-2023-C-16.png) · 2 % · [řešení](../backend/data/screenshots/M9-2023-C-16-reseni.png) — Obrazce z malých a velkých čtverečků
- [2023 D 16](../backend/data/screenshots/M9-2023-D-16.png) · 9 % · [řešení](../backend/data/screenshots/M9-2023-D-16-reseni.png) — Trojúhelníkové obrazce – puntíky a úsečky
- [2024 B 8](../backend/data/screenshots/M9-2024-B-08.png) · 29 % · [řešení](../backend/data/screenshots/M9-2024-B-08-reseni.png) — Obrazce z kruhů – zákonitost (druhé mocniny)
- [2025 A 16](../backend/data/screenshots/M9-2025-A-16.png) · 5 % · [řešení](../backend/data/screenshots/M9-2025-A-16-reseni.png) — Obrazce z obdélníčků kolem čtverce
- [2025 C 16](../backend/data/screenshots/M9-2025-C-16.png) · 6 % · [řešení](../backend/data/screenshots/M9-2025-C-16-reseni.png) — Šestiúhelníkové obrazce z trojúhelníků
- [2026 B 16](../backend/data/screenshots/M9-2026-B-16.png) · 6 % · [řešení](../backend/data/screenshots/M9-2026-B-16-reseni.png) — Vnořené čtverce – počty dílů, zlomek obsahu
- [2026 C 16](../backend/data/screenshots/M9-2026-C-16.png) · 3 % · [řešení](../backend/data/screenshots/M9-2026-C-16-reseni.png) — Obrazce ze čtverců – strana, obsah, obvod

*Exponential growth*
- [2023 A 16](../backend/data/screenshots/M9-2023-A-16.png) · 5 % · [řešení](../backend/data/screenshots/M9-2023-A-16-reseni.png) — Dělení trojúhelníků (mocniny tří)

*Number sequences*
- [2022 D 16](../backend/data/screenshots/M9-2022-D-16.png) · 13 % · [řešení](../backend/data/screenshots/M9-2022-D-16-reseni.png) — Číselná řada tvořená trojicemi
- [2025 B 16](../backend/data/screenshots/M9-2025-B-16.png) · 12 % · [řešení](../backend/data/screenshots/M9-2025-B-16-reseni.png) — Odříkávaná čísla – číselná řada se součty

*Periodic processes*
- [2022 A 16](../backend/data/screenshots/M9-2022-A-16.png) · 22 % · [řešení](../backend/data/screenshots/M9-2022-A-16-reseni.png) — Mince přidávané v pravidelných kolech (periodicita, násobky)
- [2026 A 16](../backend/data/screenshots/M9-2026-A-16.png) · 11 % · [řešení](../backend/data/screenshots/M9-2026-A-16-reseni.png) — Roboti přidávají a odebírají míčky – periodický děj

*Reasoning and strategy*
- [2025 D 16](../backend/data/screenshots/M9-2025-D-16.png) · 7 % · [řešení](../backend/data/screenshots/M9-2025-D-16-reseni.png) — Hřiště – délky úseků po obvodu obdélníku (úsudek)
- [2026 D 16](../backend/data/screenshots/M9-2026-D-16.png) · 11 % · [řešení](../backend/data/screenshots/M9-2026-D-16-reseni.png) — Hra s žetony – strategická/kombinatorická úloha (všechna řešení)

---

<a id="t19"></a>
## 19. In the specification, not seen in 2022–2026

A statement about these 20 tests, not a prediction. Each item is quoted from the specification (part and
section in brackets). For a guaranteed perfect score they belong on the list; for the expected score they
are the lowest priority.

| Area | What the specification says | Status in the 20 tests |
|---|---|---|
| Podobnost | "rozlišuje shodné a podobné trojúhelníky, pomocí poměru podobnosti určí rozměry trojúhelníků, využívá věty o podobnosti trojúhelníků (věta sss, uu, sus)" (C1, 3) | not used |
| Jehlan | "rozpozná jehlan ve volném rovnoběžném promítání, zobrazí jehlan při pohledu shora, zepředu …, rozpozná síť jehlanu, využívá … metrické a polohové vlastnosti jehlanu" (C1, 3) | not used |
| Koule | "řeší aplikační slovní úlohy s využitím znalostí o válci a kouli (poloměr a průměr koule)" (C1, 3) | not used |
| Kružnice a přímka | "určí vzájemnou polohu kružnice a přímky (tečna, sečna, vnější přímka), vzájemnou polohu dvou kružnic, průsečíky a body dotyku"; "sestrojí … tečnu kružnice v jejím bodě, kružnici opsanou trojúhelníku" (C1, 3) | circles are used in constructions, tangents never |
| Grafy úměrností | "vyjádří přímou a nepřímou úměrnost tabulkou, rovnicí a grafem" (C1, 2); "vyznačí bod v pravoúhlé soustavě souřadnic" (B1, 2) | no coordinate system in any test |
| Finanční matematika | "jistina, úroková míra, úrok, úrokovací období, daň, inflace, vypočítá úrok z vkladu za jeden rok a daň z úroku, získá základní informace o půjčkách a úvěrech" (C1, 1) | only [2024 A 16](../backend/data/screenshots/M9-2024-A-16.png) (62 %) (*úrok*, *daň z úroků*) |
| Statistika | "statistický soubor, statistický znak, statistické šetření, určí četnost" (C1, 2) | only the arithmetic mean; the word "statistický průzkum" once ([2024 B 15](../backend/data/screenshots/M9-2024-B-15.png) (61 %)) |
| Čísla | "absolutní hodnota", "periodické číslo", "promile", "největší společný dělitel", "nejmenší společný násobek", "znaky dělitelnosti čísly 2, 3, 4, 5, 6, 8 a 10" (B1, 1) | not by name; a periodic decimal appears once as an answer option ([2022 A 14](../backend/data/screenshots/M9-2022-A-14.png) (35 %)) |
| Rovnice | "rozhodne, má-li rovnice jedno řešení, nekonečně mnoho řešení, nebo nemá řešení" (C1, 1) | "nemá řešení" twice; "nekonečně mnoho" never |
| Poměr | "zapíše a upraví postupný a převrácený poměr" (B1, 1) | not by name |
| Zobrazení těles | "zobrazí tělesa při pohledu shora, zepředu, zprava, zleva a zdola", "načrtne a sestrojí síť" (B1, 3) | nets are given, never drawn; no views |
| Zaokrouhlování, odhady | "ovládá a používá pravidla pro zaokrouhlování racionálních čísel, provádí odhady" (B1, 1) | rounding only as the last step of π tasks |

---

<a id="t20"></a>
## 20. The language of the tasks: phrase → mathematics

The same few relational phrases carry the difficulty in topics 2, 7, 8 and 9. Each row was read in the task
linked.

| Phrase in the task | Meaning (x = the quantity after "než") | Seen in |
|---|---|---|
| "o třetinu více hrušek než první princ" | 4/3 · x | [2022 C 6](../backend/data/screenshots/M9-2022-C-06.png) (24 %), [2023 D 6](../backend/data/screenshots/M9-2023-D-06.png) (21 %) |
| "o čtvrtinu déle než autobusem" | 5/4 · x | [2023 B 7](../backend/data/screenshots/M9-2023-B-07.png) (36 %) |
| "o polovinu více, než …" | 3/2 · x | [2024 B 7](../backend/data/screenshots/M9-2024-B-07.png) (41 %), [2025 C 15](../backend/data/screenshots/M9-2025-C-15.png) (35 %) |
| "o třetinu méně salátů než první den" | 2/3 · x | [2025 B 7](../backend/data/screenshots/M9-2025-B-07.png) (14 %) |
| "o čtvrtinu kratší než jeden vagon" | 3/4 · x | [2023 C 12](../backend/data/screenshots/M9-2023-C-12.png) (40 %), [2025 A 8](../backend/data/screenshots/M9-2025-A-08.png) (13 %) |
| "o 25 % kratší", "o 60 % více", "o 75 % vyšší" | 0,75x; 1,6x; 1,75x | [2023 A 8](../backend/data/screenshots/M9-2023-A-08.png) (25 %), [2023 D 6](../backend/data/screenshots/M9-2023-D-06.png) (21 %), [2026 B 6](../backend/data/screenshots/M9-2026-B-06.png) (38 %) |
| "o 150 % dražší" | 2,5x ("2,5krát více") | [2023 B 2](../backend/data/screenshots/M9-2023-B-02.png) (45 %) |
| "dvakrát déle než rychlíkem" (with the bus = x) | the express train takes x/2 | [2023 B 7](../backend/data/screenshots/M9-2023-B-07.png) (36 %) |
| "dvakrát méně vagonů než …", "čtyřikrát menší délku než …", "pětkrát kratší než …" | x/2, x/4, x/5 | [2025 D 13](../backend/data/screenshots/M9-2025-D-13.png) (25 %), [2026 D 5](../backend/data/screenshots/M9-2026-D-05.png) (15 %), [2025 C 7](../backend/data/screenshots/M9-2025-C-07.png) (20 %) |
| "o polovinu levnější než skříň" (with the table = n) | the wardrobe costs 2n | [2025 C 6](../backend/data/screenshots/M9-2025-C-06.png) (8 %) |
| "o třetinu dražší než postel" (with the table = n) | the bed costs 3n/4 | [2025 C 6](../backend/data/screenshots/M9-2025-C-06.png) (8 %) |
| "Větší sud má o třetinu větší objem než menší sud", the larger one given (360 l) | smaller = 360 : 4/3 | [2026 A 5](../backend/data/screenshots/M9-2026-A-05.png) (28 %) |
| "420 uchazečů, což je o 40 % více, než se jich přihlásilo loni" | last year = 420 : 1,4 | [2023 D 15](../backend/data/screenshots/M9-2023-D-15.png) (40 %) |
| "kolikrát větší / více" | a quotient | [2022 A 2](../backend/data/screenshots/M9-2022-A-02.png) (34 %), [2022 C 14](../backend/data/screenshots/M9-2022-C-14.png) (24 %), [2026 B 7](../backend/data/screenshots/M9-2026-B-07.png) (31 %) |
| "o kolik (se liší)" | a difference | [2022 B 6](../backend/data/screenshots/M9-2022-B-06.png) (32 %), [2025 D 12](../backend/data/screenshots/M9-2025-D-12.png) (29 %) |
| "o kolik procent více / méně … než" | difference : the quantity after "než" | [2022 B 15](../backend/data/screenshots/M9-2022-B-15.png) (40 %), [2024 B 2](../backend/data/screenshots/M9-2024-B-02.png) (34 %), [2026 C 15](../backend/data/screenshots/M9-2026-C-15.png) (32 %) |
| "každý dvacátý", "jedna dvacetina" | 1/20 = 5 % | [2022 D 15](../backend/data/screenshots/M9-2022-D-15.png) (41 %), [2026 A 12](../backend/data/screenshots/M9-2026-A-12.png) (50 %) |
| "dvě pětiny zbytku", "60 % zbývající části" | a part of what is left, not of the whole | [2025 D 1](../backend/data/screenshots/M9-2025-D-01.png) (21 %), [2022 B 15](../backend/data/screenshots/M9-2022-B-15.png) (40 %) |
| "čtvrtina vzdálenosti, kterou předtím ujel" | a fraction of a fraction: 1/4 · 2/3 · x | [2026 A 6](../backend/data/screenshots/M9-2026-A-06.png) (19 %) |
| "v poměru 3 : 5 a liší se o 600 g" | 2 parts = 600 g | [2023 D 1](../backend/data/screenshots/M9-2023-D-01.png) (41 %) |
| "Najděte všechna řešení", "Uveďte všechna řešení", "najděte obě řešení" | more than one answer is expected | [2023 B 16](../backend/data/screenshots/M9-2023-B-16.png) (6 %), [2025 D 7](../backend/data/screenshots/M9-2025-D-07.png) (16 %), [2023 D 8](../backend/data/screenshots/M9-2023-D-08.png) (37 %) |
| "Výsledek zaokrouhlete na …" | compute with π ≐ 3,14, round once at the end | [2023 B 8](../backend/data/screenshots/M9-2023-B-08.png) (24 %), [2026 B 7](../backend/data/screenshots/M9-2026-B-07.png) (31 %) |
| "Velikosti úhlů neměřte, ale vypočtěte" | the figure is not to scale | [2022 A 12](../backend/data/screenshots/M9-2022-A-12.png) (50 %) |

## Sources

- Tasks and keys: `References/Matematika/` (20 booklets, 20 keys), through the problem database (`backend/data/`).
- Curriculum: `References/MASPECIFIKACEPOZADAVKU2022 (1).pdf`, parts A1, B1, C1, C2.
- Success rates: CERMAT, *Agregované výsledky úloh JPZ* (`analysis/data/m9_item_stats_2022_2026.csv`).
- Topic averages, scoring rules and test structure: [01_baseline_M9.md](01_baseline_M9.md), sections 3–5.
