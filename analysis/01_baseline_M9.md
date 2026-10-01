# Baseline: how the CERMAT math test for 9th graders is built

Subject of this document: the *didaktický test z matematiky* of the *jednotná přijímací zkouška* (JPZ) for
*čtyřleté obory vzdělání a nástavbová studia* – the test coded `M9`, sat by 9th graders.

Status: first full pass, October 2026. Companion files:

- [02_katalog_uloh.md](02_katalog_uloh.md) – every task of all 20 tests, classified, with official success rates.
- [data/m9_task_catalog.tsv](data/m9_task_catalog.tsv) – the same catalog as data.
- [data/m9_item_stats_2022_2026.csv](data/m9_item_stats_2022_2026.csv) – CERMAT's per-item results, normalized.
- [build_catalog.py](build_catalog.py) – regenerates the catalog and the summary numbers quoted below.

## 0. Evidence and how far to trust it

| Source | What it was used for |
|---|---|
| 20 test booklets + 20 keys in `References/Matematika/` (2022–2026, terms A–D) | Everything about structure, formats, content, scoring rules. All 20 were read in full: 18 from extracted text, 2024 A and B (image-only PDFs) page by page as images. Figures were additionally checked visually on 9 tests (2022 A–D, 2023 A, 2024 A, B, 2025 A, 2026 A) and on single pages of 4 more. |
| `References/MASPECIFIKACEPOZADAVKU2022 (1).pdf` | The curriculum. CERMAT's site states that for 2025/2026 this specification applies "ve stejném znění" as for 2022/2023. Whether it is unchanged for 2026/2027 is **not yet confirmed**. |
| CERMAT, *Souhrnná závěrečná zpráva JPZ 2022* (Nov 2022), ch. 5 and 9 | The official test blueprint and how open tasks are marked. |
| CERMAT, *Agregované výsledky úloh JPZ* (data.cermat.cz), math four-year programs 2022–2026 | Success and omission rates per item. Available for 18 of the 20 tests (not for 2024 C, D). |
| CERMAT, *JPZ 2023 signální výsledky*; *PZ 2025 – výsledky* (press presentation) | Year-level averages. |
| prijimacky.cermat.cz (rules, answer sheet 2026 A, validation protocols 2024 A and 2026 A) | Time limit, aids, answer sheet layout, post-exam validation. |

Limits that matter:

- The topic classification in the catalog is mine (the tags are not CERMAT's). Tasks that mix topics carry several tags and their points are split evenly between them, so topic point shares are approximate to about ±1 point.
- For 2022 and 2023 CERMAT publishes raw counts of candidates per points earned, not percentages. I converted them; a handful of 2022 rows are aggregated irregularly in the source (e.g. 2022 A task 6 and 8.3), so treat single 2022 item values as approximate. 2024–2026 values are CERMAT's own percentages.
- Replacement terms (C, D) are sat by 300–800 candidates versus 67 000–95 000 in regular terms. All difficulty statements below use regular terms (A, B) only.
- Nothing here has been checked against tests older than 2022 or against the tests for six- and eight-year gymnázia or Czech. CERMAT has the M9 tests back to 2015 online.

## 1. The exam in facts

| | | Verified on |
|---|---|---|
| Length | 70 minutes (the booklet only says the limit "je uveden na záznamovém archu") | CERMAT rules page; 2022 report |
| Size | 16 tasks, 50 points | all 20 booklets |
| Aids | "pouze psací a rýsovací potřeby"; no calculator, no tables | all 20 booklets; specification |
| Penalties | none: "se neudělují záporné body" | all 20 booklets |
| Where answers go | only the *záznamový arch* is marked; notes in the booklet are ignored | all 20 booklets |
| Attempts | each candidate may sit the test twice; the better result counts | CERMAT rules page |
| Weight | the JPZ must make up at least 60 % of a school's admission criteria (40 % for gymnázium se sportovní přípravou); there is no central pass mark | CERMAT rules page |
| Marking of open tasks | each scanned answer box is marked independently by two trained raters; a *superrater* decides when they disagree | 2022 report, 9.3 |
| Guessing floor | *náhodný skór* 6,9 % (3,45 points) | 2022 report, 5.2.3 |

The reference box printed in every booklet (last page; on page 2 in 2024) is identical in all 20 tests:
squares of 11–20, π ≐ 3,14 and π ≈ 22/7, the three factoring formulas
a² + 2ab + b² = (a + b)(a + b), a² − 2ab + b² = (a − b)(a − b), a² − b² = (a + b)(a − b),
and o = 2πr, S = πr². Nothing else is given – no Pythagorean theorem, no area or volume formulas.

The answer sheet (2026 A, 4 pages on 2 sheets): small boxes for result-only answers, large boxes labelled
"Uveďte postup řešení." for worked tasks, the construction figures pre-printed full size with
"Obtáhněte vše propisovací tužkou.", and a grid of cross-boxes for tasks 11–15.

How hard it is for the population (average % score, better of the two attempts, all applicants to four-year
programs; CERMAT): 2017 46,1 · 2018 35,8 · 2019 43,1 · 2020 43,8 · 2021 43,2 · 2022 45,3 · 2023 39,8 ·
2024 49,3 · 2025 38,4. In 2023 by school type applied to: gymnázia 57,7 · lycea 48,5 · SOŠ 38,9 · SOU 30,2 ·
nástavby 16,4. Single-test averages: 2024 A 40,3 and B 48,5; 2025 A 35,1 and B 34,4; 2026 A 41,2 and B 38,4.

So the typical candidate earns 17–24 of 50 points, and a gymnázium applicant about 29. The test is
built to spread candidates out, not to be passed.

## 2. CERMAT's own blueprint

From the 2022 final report (5.2 and 5.2.3), in CERMAT's words:

- The test targets knowledge and skills "převážně v základní a standardní úrovni obtížnosti. Okrajově jsou zastoupeny nadstandardní úlohy." It must work for all maturita programs, not only gymnázia, hence "dostatečný počet úloh v základní úrovni obtížnosti (tzv. úlohy pro minimálního žáka)".
- Počet úloh: 16. Počet bodů: 50. Časový limit: 70 minut.
- 11 otevřených úloh (68 % of points), 1 svazek dichotomických úloh (8 %), 3 úlohy multiple-choice s výběrem z 5 alternativ (12 %), 1 svazek přiřazovacích úloh (12 %).
- Among the open tasks are "široce otevřené úlohy, u nichž se hodnotí nejen výsledek řešení, ale i postup řešení", and 2 geometric construction tasks worth 5 points together.
- Content is defined only by the specification (part C1, which also includes everything from parts A1 and B1).

The booklets match this exactly in 2022, 2023, 2025 and 2026: 11 open + 5 closed tasks, 34 + 16 points.
Constructions are worth 5 points in 11 of those 16 tests and 6 points in the other 5.

## 3. The skeleton of the test

In the 16 tests of 2022, 2023, 2025 and 2026 a task's position tells you its format and nearly always its
topic. Average success and omission are from the 8 regular-term tests of those years.

| Úloha | Body | Format | What it is | Success | Left blank |
|---|---|---|---|---|---|
| 1 | 1 (3 in 2026 A) | open, result only | A warm-up: numeric expression, unit conversion, or a one-step word problem | 54 % | 9 % |
| 2 | 1–4 | open, result only (2025 A and 2026: last part with working) | 2022–23: two small numeric or unit items. 2025 B–D: one 1-point item. 2025 A and 2026: the fractions | 43 % | 12 % |
| 3 | 3–4 | 2–3 parts; the last one or two with full working | Fractions (2022, 2023, 2025 B–D); algebraic expressions (2025 A, 2026) | 62 % | 3 % |
| 4 | 4 | 3 parts: 1 + 1 + 2 points, last with working | Algebraic expressions (2022, 2023, 2025 B–D); equations (2025 A, 2026) | 49 % | 6 % |
| 5 | 4 (2 × 2); 1–4 where applied | full working, "zkoušku nezapisujte" | Two equations (2022, 2023, 2025 B–D). In 2025 A and 2026 the opening block is one task shorter and slot 5 is already an applied task | 48 % | 10 % |
| 6–8 | 2–4 each, 9–12 together | open, result only, 2–3 parts each | Three applied tasks, each with a *výchozí text* and often a picture: word problems, an "express with variable x" task, plane or solid geometry, a graph | 26–33 % | 20–29 % |
| 9, 10 | 3 + 2 or 3 + 3 | construction on the answer sheet | Triangle or quadrilateral from given points and lines | 39 %, 28 % | 24 %, 33 % |
| 11 | 4 | 3 statements, A/N | Graph, geometry or ratio context | 61 % per statement | 1 % |
| 12–14 | 2 each | choice of 5 (A–E) | Angles, solids, a word problem, a chart | 36–41 % | 2–3 % |
| 15 | 6 (3 × 2) | match 3 questions to 6 options (A–F) | Percentages | 44 % | 2 % |
| 16 | 4 (1 + 1 + 2) | open, result only | Non-standard task: a growing pattern, number sequence or game | 10 % | 36 % |

The computational core – fractions, expressions, equations – is worth 11–12 points in every one of these
16 tests (4 + 4 + 4 in 2022 and 2023, usually 3 + 4 + 4 or 4 + 4 + 4 since 2025). With the warm-up items in
front of it the opening block comes to 12–16 points.

What changed inside this skeleton:

- **2022** – fractions are two worked items of 2 points each; no system of equations.
- **2023** – fractions become 1 + 1 (result only) + 2 (worked).
- **2025** – fractions drop to 3 points (in test A they move up to task 2 and the whole block ends at task 4); tests B and D replace the second equation with a *soustava rovnic*; square roots appear inside the fraction task.
- **2026** – every test opens tasks 2, 3, 4 as fractions, expressions, equations; A and C have a *soustava rovnic*; the header of each term is printed on the cover.

### 2024 is a different test

All four 2024 booklets share a structure found in no other year in the sample:

- 6 closed and 10 open tasks (the keys say "Uzavřených 6, Otevřených 10") – 17 closed points instead of 16.
- Four multiple-choice tasks (11–14), then the A/N bundle as task 15 for **3** points scored 3 / 1 / 0, then the matching bundle as task 16.
- No pattern task in the last position; only 2024 B has one (task 8). Tasks 6–8 are always 2 + 2 points.
- Both constructions are worth 3 points and the keys list construction steps with tolerances ("s přesností 1 mm", "Tolerance úhlu … 3°") instead of describing typical student errors.
- Reference box on page 2; different house style: "Vypočítejte" instead of "Vypočtěte", "Kč" instead of "korun", "jiný výsledek" as a distractor, no "(CZVV)" source line, percentages placed in financial contexts (*úrok*, *daň z úroků*).
- Different content mix: more circle and percentage work, far less solid geometry, no divisibility or symmetry (section 5).

Press coverage from April 2024 records candidates saying the concept was "úplně jiná" than in earlier
tests. I found no official explanation of why 2024 differs, and 2025 and 2026 returned to the earlier design.
For product purposes the 2022/2023/2025/2026 design is the one to model; 2024 is useful extra
practice material but not a template.

## 4. Formats and how points are won and lost

Verified on all 20 keys unless a year is given.

**Result-only open items** ("přepište do záznamového archu pouze výsledky"). 1 or 2 points, all or nothing,
except where the key names a specific partial answer: a correct number with a wrong unit (2022 A 6, 2023 A 2.1,
2025 A 5), a correct intermediate value (2022 A 8.3, 2023 B 6.3), a correctly computed answer that is unrounded
or wrongly rounded (2023 B 8.2), an answer consistent with an earlier wrong sub-answer (2023 C 7.2, 2025 C 6.3),
or two correct values written in swapped boxes (2026 A 8). When a task says "Najděte všechna řešení", one
missing or one extra wrong solution costs half (2023 B 16.3, 2023 D 8, 2026 D 16.3).

**Worked items** ("V záznamovém archu uveďte celý postup řešení"). Always 2 points, and "Pokud uvedete pouze
výsledek, nebudou vám přiděleny žádné body." The rubric is the same every year:

| Item | 1 point if exactly one of these | 0 points |
|---|---|---|
| Fractions | result not in *základní tvar*; wrong sign; one numerical slip; a superfluous wrong step after the correct result | an "algoritmicky chybná operace se zlomky"; multiplying the expression by the common denominator as if it were an equation; more than one error |
| Expressions | exactly one term handled wrongly; one error when multiplying brackets (from 2025); final collection of like terms missing | more than one error |
| Equations | one term wrong in an equivalent step; stopped one step early (form *ax = b*); wrong or missing conclusion when the equation has no solution | an "algoritmicky chybná" manipulation; more than one error |
| Systems (2025+) | one term wrong; only one unknown found correctly | more than one error in the first unknown |

**Constructions.** Marked on the drawing only – no written procedure, no analysis. Standard instruction:
"Sestrojte vrcholy …, označte je písmeny a … narýsujte." and "V záznamovém archu obtáhněte celou konstrukci
propisovací tužkou (čáry i písmena)." Typical deductions: only one of two required solutions (−1), "mírná
nepřesnost" (−1), missing or wrong vertex labels, an extra figure that does not satisfy the task. 18 of the
40 construction tasks say "Najděte všechna řešení" and then have exactly two.

**A/N bundle** (*svazek dichotomických úloh*, "Rozhodněte o každém z následujících tvrzení …, zda je
pravdivé (A), či nikoli (N)"). Three statements; 3 correct = 4 points, 2 correct = 2 points, 1 or 0 correct = 0.
Guessing alone yields 1,25 points on average.

**Multiple choice.** Five options A–E, exactly one correct, 2 points. The last option is frequently open:
"jiný výsledek / jiná velikost / jiný objem", or the options are ranges ("menší než 120°", "větší než 150°").
In these 20 tests the option "jiný …" is never the keyed answer, in multiple choice or in the matching
bundles; a range option is (2022 D 12 "větší než 120°", 2025 C 15.1, 2026 C 15.1).

**Matching bundle** (*svazek přiřazovacích úloh*, "Přiřaďte ke každé úloze (15.1–15.3) odpovídající výsledek
(A–F)"). Three questions share six options; 2 points per question, scored independently
(3 → 6, 2 → 4, 1 → 2). The sixth option is usually "jiný počet" or a range.

## 5. What is tested

Average points per test by topic. "Std" is the 16 tests of 2022, 2023, 2025, 2026. Success is the
points-weighted average % score in the 8 regular-term tests of those years.

| Topic | Points per test (std) | In how many of 16 | Points per test (2024) | Success | Left blank |
|---|---|---|---|---|---|
| Procenta | 6,6 | 16 | 8,2 | 44 % | 6 % |
| Zlomky | 5,2 | 16 | 4,2 | 47 % | 10 % |
| Konstrukční úlohy | 5,2 | 16 | 6,0 | 32 % | 28 % |
| Úpravy výrazů (vytýkání, vzorce, roznásobení) | 4,0 | 16 | 4,0 | 50 % | 4 % |
| Lineární rovnice (+ soustava 0,5 b, 4 tests) | 4,0 | 16 | 4,0 | 52 % | 8 % |
| Nestandardní úlohy, zákonitosti | 3,6 | 16 | 1,0 | 10 % | 36 % |
| Poměr, úměrnost, měřítko, společná práce, pohyb | 3,3 | 14 | 4,8 | 37 % | 15 % |
| Tělesa – objem, povrch, sítě | 3,1 | 16 | 1,0 | 39 % | 9 % |
| Výraz s proměnnou + slovní úloha na rovnici | 3,0 | 15 | 4,5 | 32 % | 20 % |
| Grafy, tabulky, aritmetický průměr | 2,8 | 14 | 2,2 | 52 % | 8 % |
| Obvod a obsah rovinných útvarů | 2,2 | 14 | 2,8 | 32 % | 22 % |
| Úhly | 2,1 | 14 | 2,5 | 48 % | 6 % |
| Číselné výrazy, mocniny, odmocniny | 1,4 | 13 | 0 | 60 % | 5 % |
| Pythagorova věta | 1,0 | 11 | 1,2 | 40 % | 16 % |
| Kruh, kružnice, π | 0,9 | 9 | 3,0 | 35 % | 13 % |
| Souměrnost | 0,7 | 4 | 0 | – | – |
| Dělitelnost, prvočísla | 0,6 | 6 | 0 | 19 % | 27 % |
| Převody jednotek, čas | 0,6 | 8 | 0,5 | 44 % | 17 % |

Grouped the way the specification is organized, a standard test is roughly: number and algebra 19 points,
percent/ratio/data 13, geometry 15 (5 of them construction), non-standard 4.

### Recurring task types, by topic

Wording is quoted from the booklets.

**Zlomky** (every test). "Vypočtěte a výsledek zapište zlomkem v základním tvaru." Three to five operations,
brackets, negative results, a *složený zlomek* in the worked item. From 2025 mixed with decimals, squares and
square roots (√25, √(100 − 64), (3/5)²), and once *smíšená čísla* (2025 B 2).

**Úpravy výrazů** (every test), always three items:
1. "Upravte a rozložte na součin vytknutím" or "Rozložte na součin užitím vzorce" (a² − b² in disguise: 49 − (−4a)², 6·6 − 25a²).
2. "Umocněte a zjednodušte (výsledný výraz nesmí obsahovat závorky)" – a squared binomial with a fraction or decimal coefficient; or "Do rámečků doplňte chybějící čísla" in (y + □)² = y² + 10y + □.
3. Worked: "Upravte na co nejjednodušší tvar bez závorek" – two or three products of binomials, result at most quadratic. The trap is a bracket to simplify first, e.g. (3n − 2n).

**Rovnice** (every test). One equation with decimals and brackets, one with fractions; twice the answer is
"rovnice nemá řešení" (2023 A, 2025 A). From 2025 a *soustava rovnic* with integer solutions in 4 of 8 tests.
A check is never required ("zkoušku nezapisujte").

**Výraz s proměnnou → rovnice** (the explicit "Vyjádřete výrazem" task is in 12 of the 16 standard tests; a
word problem solved by an equation is in 15). Fixed three-step pattern: "… označíme x. Vyjádřete výrazem s
proměnnou x …" (twice), then a new condition and "Vypočtěte …". The relations are the same few phrases:
"o třetinu více", "o čtvrtinu déle", "dvakrát méně", "o 60 % více", "o 12 více". The last step was solved by
10–27 % of candidates in the regular terms of 2023–2026.

**Procenta** (every test, 6–8 points). Task 15 is a percentage matching bundle in all 16 standard tests.
Recurring sub-types: percentage of a whole; "o kolik procent více/méně" between two quantities; finding the
base after a change ("což je o 40 % více, než loni"); two successive changes; a percentage of the remainder;
percent ↔ fraction ("každý dvacátý", "o 2/27"). The item whose base is not the obvious quantity is the one
that fails: 2025 B 15.2 was answered correctly by 11,5 % while 47,8 % chose the same wrong option.

**Poměr a úměrnost.** Dividing in a ratio, ratio on a number line, map scale (2023 A 11), inverse proportion
(supplies for an expedition, upload speed), joint work, uniform motion (2025 C, 2026 A, 2026 D).

**Grafy a tabulky.** Bar charts with a missing bar or an unlabelled axis, stacked bars, pie charts given by
percentages or by central angles; the question asks for *aritmetický průměr*, a ratio or a percentage. Appears
as the A/N bundle in 9 of 16 standard tests.

**Úhly** (14 of 16). Parallel lines cut by transversals, intersecting lines with angles given as α, 2α, 3α,
angle sums in triangles and regular polygons, angle bisectors, the angle in a semicircle. Always
"Velikosti úhlů neměřte, ale vypočtěte (obrázek je pouze ilustrativní)."

**Rovinné útvary.** Area and perimeter of rectangle, triangle, trapezoid, rhombus and composite figures;
sides from areas; Pythagorean theorem with integer triples (6–8–10, 9–12–15, 5–12–13, 8–15–17, 9–40–41);
circle sectors and quarter-circles with π ≐ 3,14 and "Výsledek zaokrouhlete na …".

**Tělesa** (every standard test). Cube, cuboid, prisms with triangular, rhombic or trapezoidal base, cylinder;
volume, surface, nets, bodies glued together or cut apart, face diagonals. No pyramid, cone or sphere
computation occurs in the 20 tests.

**Konstrukční úlohy** (2 per test). Find missing vertices of a triangle (isosceles, right, equilateral) or a
quadrilateral (square, rectangle, parallelogram, rhombus, trapezoid; once a regular hexagon) from 1–3 given
points and 0–2 lines or a circle. The needed tools recur: perpendicular and parallel through a point, midpoint
and perpendicular bisector, point reflection in a centre, axial symmetry, circle of given radius, Thales'
circle for a right angle (never named in the task, named in the keys). They are the least attempted regular
tasks: task 10 was left blank by 33 % on average and by 53 % in 2026 A.

**Nestandardní úloha** (task 16). A rule generating figures or numbers, with an illustration of the first
2–4 steps; 16.1 asks for a nearby term, 16.2 inverts the rule, 16.3 (2 points) needs the general law or all
solutions. In 2025 D it is a geometric reasoning task and in 2026 D a token game. 16.3 was solved by
1–3 % of candidates in seven of the eight regular standard tests; 2022 A, at 11 %, is the exception.

### In the specification but not seen in these 20 tests

Checked by text search plus my reading; a statement about these 20 tests only, not a prediction.

- *Podobnost trojúhelníků* (věty sss, uu, sus), *jehlan*, *koule*, tangent and relative position of circles.
- Graphs of *přímá a nepřímá úměrnost*, coordinates in *pravoúhlá soustava souřadnic*.
- Financial terminology (*jistina, úroková míra, daň, inflace*) – only in 2024 A task 16 (*úrok*, *daň z úroků*).
- *Největší společný dělitel / nejmenší společný násobek* by name, *absolutní hodnota*, *promile*, periodic decimals (one appears only as an answer option, 2022 A 14).
- Statistical vocabulary (*četnost*, *statistický soubor*); only the arithmetic mean is used.

## 6. Where the points actually are

From the regular-term item data of the standard years (section 3 and 5 tables):

1. **The opening computation block is the most solved open part**: tasks 3, 4 and 5 average 62 %, 49 % and 48 %, with 3–10 % blank. The fractions–expressions–equations core is 11–12 points.
2. **Closed tasks are attempted by nearly everyone** (1–3 % blank) and are worth 16 points, but multiple choice is answered correctly by only 36–41 % against a 20 % guessing rate.
3. **Result-only applied tasks 6–8 are where most points are lost**: 10 points on average, 26–33 % success, 20–29 % blank. Within them the last sub-item is far harder than the first.
4. **Constructions**: 5–6 points, 32 % success, 28 % blank. Results vary enormously between tests – from 72 % (2022 B 9) to 9 % (2025 B 10).
5. **Task 16**: 4 points, 10 % success, 36 % blank; its first sub-item ranges from 11 % to 42 %.
6. **The same topic costs more in open form.** Word problems leading to an equation score 32 % as open tasks, while percentage problems in the matching bundle score 44 %.
7. **Omission grows through the open part**: about 3 % at the fractions, 20–29 % at tasks 6–8, 33 % at the second construction, then drops to 1–3 % for the closed tasks and rises again to 36 % at task 16. The data cannot tell whether candidates ran out of time or skipped on purpose.

## 7. How the tasks are constructed

Patterns observed across the booklets; each is a description of what the tests do, not of CERMAT's intent.

- **No calculator, so the numbers are engineered.** Results are small integers, simple fractions or one-decimal numbers; Pythagorean triples are integer; areas are perfect squares (9, 16, 144 cm²); π tasks use r = 5, 10 or 50.
- **A *výchozí text* box precedes most tasks**, headed "VÝCHOZÍ TEXT (A OBRÁZEK / GRAF / TABULKA) K ÚLOZE n" and signed "(CZVV)". The question below adds a further condition. Sub-questions often each add their own extra fact.
- **Graduated sub-items.** Multi-part tasks go from a direct reading or one-step computation to a step that needs a relation set up; the points and the success rates follow (e.g. 2026 A task 6: 38 % → 17 % → 10 %).
- **Relational language carries the difficulty**: "o třetinu více než", "kolikrát větší", "o kolik procent menší … než", "dvakrát méně". The same quantity is described as a fraction, a percentage and a ratio within one test.
- **Unit changes are embedded, not announced**: cm with dm², litres with cm² and mm, metres with cm.
- **Figures are illustrative.** Angle and construction figures are not to scale for measuring; solids are shown in oblique projection with hidden edges dashed.
- **Constructions are underdetermined on purpose.** Phrases such as "na přímce q leží jeden z vrcholů A, B" or "přímka o je osou některé strany" create the second solution.
- **Distractors include the naive answer.** In 2025 B 15.2 ("o jednu třetinu méně" → "o kolik procent více") the option 33 % drew 47,8 % of candidates; the key, 50 %, drew 11,5 %. The option "jiný …" is present in about half of the multiple-choice tasks.
- **Terms of one year are parallel but not equivalent.** Same skeleton, different contexts, and unequal difficulty: 2024 A averaged 40,3 % and 2024 B 48,5 %. Seznam Zprávy (26 April 2024) quotes CERMAT's then director as saying the tests are not deliberately made comparable in difficulty.

## 8. What carries over to other tests – not yet verified

The 2022 report gives blueprints for the other math tests: six-year gymnázia also 16 tasks / 50 points / 70 minutes
(10 open, 1 A/N bundle, 4 multiple choice, 1 matching bundle, 2 constructions for 6 points); eight-year gymnázia
14 tasks / 50 points / 70 minutes with one construction task for 6 points. So the format family is shared, while the
curriculum (specification parts A1, B1) and the difficulty target differ: those tests aim to pick out above-average
pupils rather than to cover the whole population. None of their booklets has been analysed here. The Czech test
(60 minutes, 50 points, largely four-option multiple choice plus a few open tasks) is a different instrument.

## 9. Open questions

1. Is the specification unchanged for 2026/2027? (CERMAT confirms it only up to 2025/2026.)
2. Why did 2024 differ, and could that design return? No official statement found.
3. Do the 2015–2021 M9 tests fit the same skeleton? They are on CERMAT's site and would triple the sample.
4. Item results for 2024 C and D are not published; per-school-type item results are not public at item level.
5. Time pressure versus deliberate skipping cannot be separated from omission rates; this needs observation of real students.

## Sources

- Test booklets and keys: `References/Matematika/` (also at prijimacky.cermat.cz → Testová zadání k procvičování → čtyřleté obory, matematika).
- Specification: `References/MASPECIFIKACEPOZADAVKU2022 (1).pdf`; validity note at https://prijimacky.cermat.cz/menu/specifikace-pozadavku-k-jpz.html
- Blueprint and marking: https://data.cermat.cz/files/files/2022/JPZ/Souhrnna_zaverecna-zprava_JPZ_2022.pdf
- Item results: https://data.cermat.cz/data-a-analyticke-vystupy-jednotna-prijimaci-zkouska/agregovana-data-jpz/agregovane-vysledky-uloh-jpz.html
- Year averages: https://data.cermat.cz/files/files/JPZ2023_signalni_vysledky.pdf (p. 37); https://data.cermat.cz/files/files/JPZ/PZ2025_prezentace_vysledky_TK.pdf (p. 7)
- Rules: https://prijimacky.cermat.cz/menu/jednotna-prijimaci-zkouska ; https://prijimacky.cermat.cz/menu/jednotna-prijimaci-zkouska/prijimacky-bez-obav/pravidla-a-doporuceni.html
- Answer sheet 2026 A: https://prijimacky.cermat.cz/files/files/dokumenty/M9A_2026_ZA.pdf
- Press on 2024: https://cnn.iprima.cz/test-zvladli-byste-letosni-prijimacky-cermat-sklizi-kritiku-na-detech-se-mel-vyradit-434124 ; https://www.seznamzpravy.cz/clanek/domaci-cermat-prijimaci-zkouska-z-matematiky-pro-ctyrlete-obory-byla-letos-snazsi-250759
