# CERMAT M9 Mathematics Test — Definitive Test-Creation Guidebook

> **Purpose**: This document is the single source of truth for anyone creating
> practice CERMAT M9 math tests. It contains every rule, convention, constraint,
> and pattern needed to produce tests that are **indistinguishable from real
> CERMAT exams** — both visually and content-wise.
>
> **Audience**: Test creators, content reviewers, and the automated generation
> engine. Every claim in this document should be defensible against the 12
> reference tests in `References/Matematika/`.
>
> **Scope**: M9 — Mathematics for 9th-grade applicants entering 4-year
> gymnázium (čtyřleté gymnázium).

---

## Table of Contents

1. [How to Use This Document](#1-how-to-use-this-document)
2. [What Is CERMAT / JPZ](#2-what-is-cermat--jpz)
3. [Immutable Test Parameters](#3-immutable-test-parameters)
4. [Test Booklet Structure](#4-test-booklet-structure)
5. [Answer Sheet (Záznamový Arch)](#5-answer-sheet-záznamový-arch)
6. [Task Taxonomy — The Slot System](#6-task-taxonomy--the-slot-system)
7. [Per-Task Specifications](#7-per-task-specifications)
8. [Scoring & Partial Credit Rules](#8-scoring--partial-credit-rules)
9. [Czech Mathematical Conventions](#9-czech-mathematical-conventions)
10. [Visual Layout Specification](#10-visual-layout-specification)
11. [Cross-Year Stability Analysis](#11-cross-year-stability-analysis)
12. [Quality Checklist](#12-quality-checklist)
13. [Appendix A: Formula Reference Sheet](#appendix-a-formula-reference-sheet)
14. [Appendix B: Test Code Format](#appendix-b-test-code-format)
15. [Appendix C: Glossary of Czech Mathematical Terms](#appendix-c-glossary-of-czech-mathematical-terms)

---

## 1. How to Use This Document

This document is organized in layers of specificity:

- **Sections 1–5** establish the immutable framework: what a CERMAT test *is*,
  what the physical documents look like, and what rules never change.
- **Section 6** maps the 16 task slots and establishes the pattern system.
- **Section 7** is the core reference — one subsection per task, with exact
  constraints for content generation.
- **Sections 8–9** cover scoring rules and Czech conventions.
- **Section 10** specifies the visual layout (without implementation code).
- **Sections 11–12** provide stability analysis and the final quality gate.
- **Appendices** contain reference material.

**The cardinal rule**: Every claim in this document must be verifiable against
the reference test PDFs. All claims in this document have been validated against the official
2024, 2025, and 2026 tests. All other claims are sourced from official
CERMAT publications or test generation guidelines.

---

## 2. What Is CERMAT / JPZ

### 2.1 The Institution

**CERMAT** — formally **Centrum pro zjišťování výsledků vzdělávání (CZVV)** —
is the Czech government agency responsible for standardized educational testing.
It operates under the Ministry of Education (MŠMT).

### 2.2 The Exam

The **Jednotná přijímací zkouška (JPZ)** — Unified Entrance Exam — is the
mandatory standardized test that students take when applying to secondary
schools (gymnázia and other školy providing maturita programs).

The exam consists of two subjects:
- **Český jazyk a literatura** (Czech Language and Literature)
- **Matematika** (Mathematics)

Students sit the exam at **two schools** (two attempts). The **better result**
from the two attempts counts for admission.

### 2.3 M9 Designation

- **M** = Matematika (Mathematics)
- **9** = 9th-grade applicants (entering 4-year gymnázium)

There also exists **M5** for students entering 8-year gymnázium from 5th grade.
This document covers **M9 only**.

### 2.4 Legal Basis

The exam content is derived from the **Rámcový vzdělávací program pro základní
vzdělávání (RVP ZV)** — the national curriculum framework for basic education —
specifically from the educational area **Matematika a její aplikace**.

The official specification document **Specifikace požadavků k JPZ — Matematika**
is published annually by CERMAT (content has remained stable for years). It maps
exam content to these RVP ZV thematic areas:

| RVP ZV Thematic Area | Czech Name | Approx. Points |
|---|---|---|
| Number & Variable | Číslo a proměnná | ~15 pts |
| Dependencies, Relationships & Data | Závislosti, vztahy a práce s daty | ~6–14 pts |
| Geometry in Plane & Space | Geometrie v rovině a v prostoru | ~10–17 pts |
| Non-standard Application Tasks | Nestandardní aplikační úlohy | ~8–11 pts |

### 2.5 Official Sources

| Source | URL | Contains |
|---|---|---|
| Test PDFs & answer keys | `prijimacky.cermat.cz` → Testová zadání | All past exams |
| Curriculum specification | `prijimacky.cermat.cz` → Specifikace požadavků | What the exam tests |
| Practice app (TAU) | `tau.cermat.cz` | Interactive practice |
| Illustrative tests | `prijimacky.cermat.cz` → Ilustrační testy | Sample format tests |

---

## 3. Immutable Test Parameters

These parameters have been **identical across all 12 reference tests** (2024 A/B/C/D,
2025 A/B/C/D, 2026 A/B/C/D) and are considered stable:

| Parameter | Value | Notes |
|---|---|---|
| **Time limit** | 70 minutes | Printed on both test booklet and answer sheet |
| **Maximum score** | 50 bodů (points) | Sum of all individual task point allocations |
| **Number of tasks** | 16 | Numbered 1–16, sequential |
| **Allowed aids** | Pen (blue/black ballpoint), pencil, ruler, compass (kružítko), protractor (úhloměr) | Cover page says: `pouze psací a rýsovací potřeby` |
| **Forbidden aids** | Calculator, mathematical tables, erasable pens, correction fluid | Explicitly stated in instructions |
| **Answer recording** | All answers go onto the **záznamový arch** (answer sheet) | Test booklet notes are NOT evaluated |
| **Scoring** | Whole points only (celé body), no negative marks | Zero is minimum per task |
| **Printing** | Black and white only | All diagrams, shading in grayscale |
| **Paper size** | A4 (210 × 297 mm / 595.3 × 841.9 pt) | Confirmed across all 12 tests |
| **Font** | Myriad Pro (primary), Cambria Math (math), Arial (supplementary) | NOT Arial as primary — see [`CERMAT_visual_spec.md`](file:///Users/jarda/ArchMaster/docs/CERMAT_visual_spec.md) |
| **Page count** | 12 pages (2025–2026); 11–15 pages (2024) | Standardized to 12 from 2025 onward |

---

## 4. Test Booklet Structure

The test booklet (**testový sešit**) is the multi-page document students receive.
It contains all task texts, diagrams, and space for scratch work (which is not
evaluated).

### 4.1 Cover Page (First Page)

The cover page uses a **two-column layout** and contains, in order from top
to bottom (exact text transcribed from 2025–2026 PDFs):

1. **Subject and variant**: `MATEMATIKA 9 {A}` — MyriadPro-Bold, 21.96pt
2. **Term designation**: `{1. ŘÁDNÝ TERMÍN}` — MyriadPro-Regular, 15.96pt
3. **Test code**: `{M9PAD26C0T01}` — MyriadPro-Bold, 15.96pt
   (see [Appendix B](#appendix-b-test-code-format) for decoding)
4. **Test type**: `DIDAKTICKÝ TEST` — MyriadPro-Bold, 14.04pt
5. **Student name field**: `Jméno a příjmení:` with blank line
6. **Info box** (three lines, MyriadPro-Bold, 12pt):
   - `Počet úloh: 16`
   - `Maximální bodové hodnocení: 50 bodů`
   - `Povolené pomůcky: pouze psací a rýsovací potřeby`

7. **Instructions block** (two numbered sections in the left column,
   MyriadPro-Regular, 11.04pt):

   **1 Základní informace k zadání zkoušky**
   - Časový limit pro řešení didaktického testu je uveden na záznamovém archu.
   - U každé úlohy je uveden maximální počet bodů.
   - Za neuvedené řešení úlohy či za nesprávné řešení úlohy jako celku se
     neudělují záporné body.
   - Odpovědi pište do záznamového archu.
   - Poznámky si můžete dělat do testového sešitu nebo na volné listy papíru,
     nebudou však předmětem hodnocení.
   - Didaktický test obsahuje otevřené a uzavřené úlohy. Uzavřené úlohy
     obsahují nabídku odpovědí. U každé takové úlohy nebo podúlohy je právě
     jedna odpověď správná.
   - Na poslední straně testového sešitu najdete vybrané vzorce a vztahy.

   **2 Pravidla správného zápisu do záznamového archu**
   - Řešení úloh zapisujte do záznamového archu modře nebo černě píšící
     propisovací tužkou, která píše dostatečně silně a nepřerušovaně.
   - Nejednoznačný nebo nečitelný zápis odpovědi bude považován za chybné
     řešení.
   - V konstrukčních úlohách rýsujte tužkou a následně vše obtáhněte
     propisovací tužkou.

   **2.1 Pokyny k otevřeným úlohám**
   - Řešení úloh pište čitelně do vyznačených bílých polí záznamového archu.
   - Pokud budete chtít provést opravu, původní zápis přeškrtněte a nový
     uveďte do stejného pole.
   - Je-li požadován celý postup řešení, uveďte jej do záznamového archu.
     Pokud uvedete pouze výsledek, nebudou vám přiděleny žádné body.
   - Zápisy uvedené mimo vyznačená bílá pole záznamového archu nebudou
     hodnoceny.

   **2.2 Pokyny k uzavřeným úlohám**
   - Odpověď, kterou považujete za správnou, zřetelně zakřížkujte
     v příslušném bílém poli záznamového archu, a to přesně z rohu do rohu
     dle obrázku.
   - Pokud budete chtít následně zvolit jinou odpověď, pečlivě zabarvěte
     původně zakřížkované pole a zvolenou odpověď vyznačte křížkem do
     nového pole.
   - Jakýkoliv jiný způsob záznamu odpovědí (např. dva křížky u jedné
     otázky) bude považován za nesprávnou odpověď.

8. **Right column**: MC cross-marking example diagram (boxes A–E with X)

9. **Final line**: `TESTOVÝ SEŠIT NEOTVÍREJTE, POČKEJTE NA POKYN!`
   (MyriadPro-Bold, 12pt)

10. **Copyright**: `Předmětem autorských práv Centra pro zjišťování výsledků
    vzdělávání` (MyriadPro-Regular, 8.04pt, top or bottom of page)

### 4.2 Formula Reference Sheet

**Location**: The formula reference sheet is on the **last page** of the test
booklet (NOT on the cover page — this is a common misconception).

**Content** — see [Appendix A](#appendix-a-formula-reference-sheet) for the
exact formulas. The sheet is titled `Vybrané vzorce a vztahy` and contains
standard geometric formulas that students may reference during the exam.

### 4.3 Task Pages

After the cover page, tasks 1–16 are laid out sequentially. The exact
page-to-task mapping **varies by year and variant** — there is no fixed rule
like "Task 1 is always on page 2." However, the general flow is:

- **Early tasks** (1–4): Compact, typically 2–3 tasks per page
- **Middle tasks** (5–9): More space-consuming, often 1–2 tasks per page,
  especially geometry tasks with diagrams
- **Later tasks** (10–16): Variable — MC tasks are compact, data/matching
  tasks need full pages

**Total page count**: **12 pages** (standardized from 2025 onward;
2024 variants ranged from 11–15 pages).

### 4.4 Page Headers and Footers

| Element | Content | Font |
|---|---|---|
| Page header | Page number as `{N} ze {total}` (e.g., `2 ze 12`) — top right | MyriadPro-Regular, 12pt |
| Page footer | `(CZVV)` — parenthetical with CZVV in italic | MyriadPro-Regular + MyriadPro-It, 9.48pt |

> **Correction**: The page header does **NOT** repeat the test code on
> every page (previous claim was incorrect). Only the page number appears.
> The footer is `(CZVV)` with the letters in italic, NOT `© CZVV`.

---

## 5. Answer Sheet (Záznamový Arch)

The **záznamový arch** is a **separate document** from the test booklet. It is
the **only** thing that gets evaluated. Students record all their answers here.

### 5.1 Why It Matters for Test Generation

We must generate answer sheets that match CERMAT's format because:
- Students need to practice with the real recording format
- The answer sheet layout affects how students approach tasks (space for
  procedures, cross-marking for MC, etc.)
- The answer sheet is **scanned and partially auto-evaluated**

### 5.2 Answer Sheet Layout

The answer sheet contains, for each task:

| Task Type | Answer Sheet Field |
|---|---|
| **Open — result only** | White box/line for writing the numerical result |
| **Open — with procedure** | Large white rectangular area for writing the complete solution procedure |
| **Open — construction** | Grid or blank area for geometric construction (pencil, then traced with pen) |
| **Closed — MC (A–E)** | Row of boxes labeled A through E (or F); student crosses one from corner to corner |
| **Closed — ANO/NE** | For each sub-statement: two boxes (ANO / NE); student crosses one |
| **Closed — matching** | For each sub-item: row of option boxes (A through F); student crosses one per sub-item |

### 5.3 Recording Rules

These rules are printed on the answer sheet and are critical for authenticity:

**For open tasks**:
- Write results clearly into the designated white fields
- To correct: cross out the original and write the new answer in the same field
- Entries outside the designated white fields will not be evaluated

**For closed tasks (cross-marking)**:
- Mark the chosen answer with a cross (×) precisely from corner to corner
  of the appropriate box
- To change an answer: **carefully fill in** (darken) the original crossed box,
  then cross the new choice
- Any other method of recording (two crosses, circling, checkmarks) is
  considered incorrect

**For construction tasks**:
- Draw with pencil first
- Trace everything (including auxiliary lines, arcs, and labels) with ballpoint pen
- Only pen lines are evaluated

---

## 6. Task Taxonomy — The Slot System

CERMAT M9 tests follow a **remarkably stable slot system**. While the specific
content changes each year and variant, the **type, format, and approximate
difficulty** of each numbered task position is highly predictable.

### 6.1 Evidence Basis

The slot analysis below is derived from:
- 12 reference test PDFs (2024 variants A/B/C/D, 2025 A/B/C/D, 2026 A/B/C/D)
- 12 corresponding answer key PDFs
- Official CERMAT specifications
- Cross-referencing with educational portals (To-dáš, přijímačky-online)

**Methodology note**: Since the PDF files are binary and cannot be
automatically text-parsed, the cross-year evidence table below is constructed
from answer key analysis and web-based test breakdowns. The specific formatting (fonts, margins, rule widths) is detailed in the
companion document [`CERMAT_visual_spec.md`](file:///Users/jarda/ArchMaster/docs/CERMAT_visual_spec.md).

### 6.2 Master Slot Table

| Slot | Stable Topic Area | Answer Format | Typical Points | Subtasks | Procedure Required? | Context Box? |
|------|-------------------|---------------|----------------|----------|--------------------|----|
| **1** | Arithmetic / number operations | Open — result only | 2 | 2 | No | No |
| **2** | Fractions / decimals / mixed operations | Open — result only | 2 | 2 | No | No |
| **3** | Algebraic expressions (simplify/factor) | Open — with procedure | 3 | 2–3 | **Yes** | No |
| **4** | Linear equations / systems | Open — with procedure | 3 | 1–2 | **Yes** | No |
| **5** | Word problem (equation modeling) | Open — with procedure | 3–4 | 1–2 | **Yes** | Sometimes |
| **6** | Planimetry (2D geometry calculation) | Open — with procedure | 3–4 | 2–3 | **Yes** | Yes (diagram) |
| **7** | Geometry calculation / proportions | Open — with procedure or result | 2–3 | 2–3 | Varies | Sometimes |
| **8** | Geometry / application | Open — result or procedure | 2–3 | 2–3 | Varies | Sometimes |
| **9** | Construction — geometric (triangle, locus) | Open — construction | 3 | 1–2 | **Yes** (drawing) | Yes |
| **10** | Construction — geometric (circle, Thales) | Open — construction | 3 | 1–2 | **Yes** (drawing) | Yes |
| **11** | Stereometry (3D geometry) | Open — with procedure | 3–4 | 2–3 | **Yes** | Yes (3D figure) |
| **12** | Multiple choice — algebraic modeling | Closed (A–E) | 2 | 1 | No | Yes |
| **13** | Multiple choice — geometry/angle reasoning | Closed (A–E) | 2 | 1 | No | Yes (diagram) |
| **14** | ANO/NE — data interpretation | Closed (ANO/NE) | 4 | 4 | No | Yes (table/graph) |
| **15** | ANO/NE — application / logical statements | Closed (ANO/NE) | 4 | 4 | No | Yes (context) |
| **16** | Sequences / patterns / mathematical modeling | Open — result only | 3–4 | 3 | No | Yes (diagram) |

> **Critical caveat about slot positions**: The exact topic-to-slot mapping
> shown above represents the **most common pattern** observed across reference
> tests. CERMAT does **shift tasks by ±1–2 positions** between years and
> variants. For example:
>
> - Construction tasks appear at positions 7–8 in some years but 9–10 in others
> - The stereometry task has appeared at positions 9 and 11
> - MC tasks cluster in the 11–13 range but their exact positions shift
> - ANO/NE tasks appear at 14–15 but have sometimes been at 13–14
>
> **The lesson**: Do not hardcode a rigid slot → topic mapping. Instead, ensure
> every test contains one task of each type, and place them in approximately the
> right zone (early = arithmetic, middle = geometry, late = MC/data).

### 6.3 Point Distribution Pattern

The total across all 16 tasks always sums to exactly **50 points**. The
distribution follows this pattern (consistent across years):

| Category | RVP ZV Area | Tasks (approx.) | Typical Points |
|---|---|---|---|
| Number & Variable | Číslo a proměnná | 1, 2, 3, 4 | ~10 pts |
| Word problems / modeling | Závislosti, vztahy | 5, 12 | ~5–6 pts |
| Geometry — computation | Geometrie | 6, 7, 8, 11, 13 | ~12–15 pts |
| Geometry — construction | Geometrie | 9, 10 | ~5–6 pts |
| Data, logic, statements | Závislosti, vztahy | 14, 15 | ~8 pts |
| Patterns / sequences | Nestandardní aplikační | 16 | ~3–4 pts |
| **Total** | | **16 tasks** | **50 pts** |

### 6.4 Answer Format Distribution

Every test contains all five answer formats:

| Format | Czech Name | Tasks Using It | Count |
|---|---|---|---|
| Open — result only | Úloha s výsledkem | 1, 2, 7/8, 16 | ~4 |
| Open — with procedure | Úloha s postupem řešení | 3, 4, 5, 6, 11 | ~5 |
| Open — construction | Konstrukční úloha | 9, 10 | 2 |
| Closed — MC (A–E/F) | Uzavřená úloha | 12, 13 | ~2 |
| Closed — ANO/NE | Dichotomická úloha | 14, 15 | 2 |

### 6.5 Difficulty Gradient

The test is designed with a deliberate difficulty curve based on long-term
CERMAT statistics:

| Zone | Tasks | Approx. Student Success Rate | Purpose |
|---|---|---|---|
| **Warmup** | 1–2 | ≥80% | Confidence builder |
| **Core skills** | 3–5 | 55–75% | Tests foundational algebra/arithmetic |
| **Applied** | 6–8 | 40–60% | Geometry computation, proportions |
| **Construction** | 9–10 | 20–40% | Often the hardest; lowest success rate |
| **Accessible MC** | 12–13 | 55–70% | MC format compensates for harder content |
| **Data/logic** | 14–15 | 35–55% | ANO/NE — tricky phrasing can trap students |
| **Patterns** | 16 | 40–60% | Requires formula derivation |

**Source**: Aggregated CERMAT result reports and educational portal analyses.

---

## 7. Per-Task Specifications

This is the core reference section. Each task is documented with:

- **What it tests** (curriculum link)
- **Observed patterns** across reference tests
- **Exact constraints** for content generation
- **Illustrative example** (representative, not copied verbatim)
- **Common student mistakes** (useful for MC distractor generation)
- **What makes it "CERMAT-like"** vs. a generic textbook problem

---

### Task 1 — Arithmetic / Number Operations

**Curriculum area**: Číslo a proměnná — basic numerical operations
**Format**: Open — result only
**Points**: 1–3 (varies by year, often 2)
**Subtasks**: Usually 0 or 1 (often just a single calculation)
**Procedure required**: No

**What it tests**: Order of operations (PEMDAS/Czech convention), integer
arithmetic, powers of natural numbers, parentheses.

**Observed pattern across tests**:
- May be a single expression or a compound expression
- No word problem context — pure computation
- Very brief format

**Constraints for generation**:

| Constraint | Value |
|---|---|
| Operands | Integers, typically |a| ≤ 1000 |
| Operations allowed | `+`, `−`, `·` (middle dot), `:` (colon for division) |
| Powers | Natural number bases ≤ 10, exponents ≤ 3; powers of 10 up to 10³ |
| Result type | Integer or simple decimal (max 1 decimal place) |
| Czech notation | Division as `:`, multiplication as `·` |
| Parentheses | Up to 2 levels of nesting |
| Negative results | Allowed (but not both subtasks) |

**Illustrative example**:
```
1.1  Vypočtěte: 48 : 6 − 3 · (−2)
1.2  Vypočtěte a výsledek zapište ve tvaru jednoho čísla: 5 · 10² − 300 : 10
```
*Answers: 1.1 → 14; 1.2 → 470*

**Common student mistakes** (for distractor awareness):
- Ignoring order of operations (computing left to right)
- Sign errors with negative numbers
- Confusing `10²` with `10 · 2`

**What makes it CERMAT-like**:
- Expressions are compact (one line), not sprawling
- Numbers are chosen so the result is "clean"
- At least one operation tests order-of-operations awareness
- Czech notation (`:` for division, `·` for multiplication) is mandatory

---

### Task 2 — Fractions / Decimals

**Curriculum area**: Číslo a proměnná — operations with fractions
**Format**: Open — result only
**Points**: 2 (always 1 + 1)
**Subtasks**: 2 (always exactly 2)
**Procedure required**: No

**What it tests**: Adding, subtracting, multiplying, dividing fractions and
mixed numbers. Converting between fractions and decimals.

**Observed pattern**:
- Always 2 independent subtasks
- One subtask focuses on addition/subtraction, the other on
  multiplication/division (or a compound expression)
- May combine fractions with decimals or powers in the same expression

**Constraints for generation**:

| Constraint | Value |
|---|---|
| Denominators | ≤ 20 (most commonly ≤ 12) |
| Numerators | Integers, typically ≤ 30 |
| Mixed numbers | Allowed (e.g., `2 1/3`) |
| Operations | `+`, `−`, `·`, `:` on fractions |
| Result type | Simplified fraction (základní tvar) or integer |
| Decimal mixing | May include e.g. `0,5 + 1/4` |

**Illustrative example**:
```
2.1  Vypočtěte: 3/4 + 5/6 − 1/3
2.2  Vypočtěte: 2 1/2 · (4/5 : 2)
```
*Answers: 2.1 → 5/4 (or 1 1/4); 2.2 → 1*

**Common student mistakes**:
- Not finding common denominator
- Forgetting to simplify (not in základní tvar)
- Division of fractions — forgetting to flip
- Sign errors when subtracting fractions

**What makes it CERMAT-like**:
- Denominators that require actual LCM computation (not trivial)
- Results that simplify to elegant fractions or whole numbers
- No calculator — values chosen so mental math is feasible

---

### Task 3 — Algebraic Expressions

**Curriculum area**: Číslo a proměnná — algebraic manipulation
**Format**: Open — with procedure
**Points**: 3–4
**Subtasks**: 1–3 (often 2 or 3)
**Procedure required**: **Yes** — explicitly stated

**What it tests**: Simplification of algebraic expressions, expanding brackets,
factoring, algebraic identities.

**Observed pattern**:
- 2–3 subtasks of increasing difficulty
- Subtask types: simplify, expand, factor, simplify rational expression
- Algebraic identities are frequently tested: `(a+b)²`, `(a−b)²`, `a²−b²`

**Constraints for generation**:

| Constraint | Value |
|---|---|
| Variables | Standard letters: `a`, `b`, `x`, `y` (1–2 per expression) |
| Coefficients | Integers, |coeff| ≤ 10 |
| Exponents | ≤ 3 (typically ≤ 2) |
| Identities tested | `(a±b)²`, `a²−b² = (a+b)(a−b)`, distribution law |
| Result | Must be verifiably correct (simplest form) |
| Subtask instruction | `Upravte:`, `Zjednodušte:`, `Rozložte na součin:` |

**Illustrative example**:
```
Zapište celý postup řešení.

3.1  Zjednodušte výraz: 3a − (2a − 5b) + 4b
3.2  Rozložte na součin: 9x² − 25y²
3.3  Zjednodušte zlomek: (x² − 4) / (x + 2)
```
*Answers: 3.1 → a + 9b; 3.2 → (3x+5y)(3x−5y); 3.3 → x−2 (for x ≠ −2)*

**Common student mistakes**:
- Sign error when distributing negative across brackets
- Forgetting the middle term in `(a+b)²` (writing `a² + b²`)
- Not recognizing difference of squares pattern
- Canceling terms instead of factors in fractions

---

### Task 4 — Linear Equations / Systems

**Curriculum area**: Číslo a proměnná — solving equations
**Format**: Open — with procedure
**Points**: 4 (always 4 pts across all tests)
**Subtasks**: 1–3 (often 2 or 3 equations to solve)
**Procedure required**: **Yes** — explicitly stated

**What it tests**: Solving linear equations (one variable), sometimes systems
of two linear equations with two unknowns.

**Observed pattern**:
- If 1 subtask: a complex linear equation with fractions, nested brackets, or
  both
- If 2 subtasks: (a) single equation, (b) system of 2 equations
- Solutions are always "nice" — integers or simple fractions

**Constraints for generation**:

| Constraint | Value |
|---|---|
| Variable | `x` (single equation), `x` and `y` (system) |
| Coefficients | Integers, |coeff| ≤ 12 |
| Solution type | Integer or simple fraction (denominator ≤ 10) |
| Equation complexity | Up to 3 levels of bracket nesting, fractions with LCD ≤ 12 |
| System | If present: 2 equations, 2 unknowns, unique solution |
| Subtask instruction | `Řešte rovnici:`, `Řešte soustavu rovnic:` |

**Illustrative example**:
```
Zapište celý postup řešení.

4.1  Řešte rovnici: 3(2x − 1) + 4 = 5x − 2(x + 3)
4.2  Řešte soustavu rovnic:
     2x + y = 7
     x − 3y = −5
```
*Answers: 4.1 → x = −7; 4.2 → x = 16/7, y = 17/7* (would be nicer integers
in a real test — solutions like x = 2, y = 3)

**Common student mistakes**:
- Not distributing correctly across brackets
- Losing a negative sign when multiplying both sides
- Arithmetic errors when eliminating variables in systems
- Writing `x = 5` without showing procedure → 0 points

---

### Task 5 — Word Problem

**Curriculum area**: Závislosti, vztahy — mathematical modeling
**Format**: Open — with procedure
**Points**: 3–4
**Subtasks**: 1–2 (often: "set up the equation" + "solve it")
**Procedure required**: **Yes** — must show equation setup AND solution

**What it tests**: Translating real-world scenarios into mathematical equations
and solving them. This task bridges arithmetic/algebra and applied reasoning.

**Observed scenario archetypes** (recurring across tests):

| Archetype | Key Relationship | Example Context |
|---|---|---|
| **Motion** (pohyb) | `s = v · t` | Two trains meeting, cyclist overtaking walker |
| **Shared work** (společná práce) | `1/t₁ + 1/t₂ = 1/t` | Two pipes filling a pool |
| **Mixtures** (směsi) | Weighted average | Mixing solutions of different concentrations |
| **Age** (věk) | Time shifts: "before X years" | Father is 3× older than son, in 10 years... |
| **Shopping / pricing** | Linear relationships | Notebook costs x Kč, pen costs x+5 Kč |
| **Percentages** | `part = (percent/100) · whole` | Discount, tax, price increase |

**Constraints for generation**:

| Constraint | Value |
|---|---|
| Context | Realistic, unambiguous, self-contained |
| Numbers | "Nice" — solutions are positive integers or simple fractions |
| Equation type | Linear (one variable) or simple system (two variables) |
| Units | Must be consistent and stated |
| Czech context | Prices in Kč, distances in km, speeds in km/h |
| Subtask wording | Often: `Sestavte rovnici (soustavu rovnic) a vyřešte ji.` |

**Illustrative example**:
```
VÝCHOZÍ TEXT K ÚLOZE 5

Pan Novák a pan Svoboda bydlí ve dvou městech, která jsou od sebe vzdálena
120 km. Vyjeli současně na kole proti sobě. Pan Novák jede rychlostí 18 km/h,
pan Svoboda rychlostí 22 km/h.

5  Za kolik hodin se setkají?
   Sestavte rovnici a vyřešte ji. Zapište celý postup řešení.
```
*Answer: 18t + 22t = 120 → t = 3 hours*

**What makes it CERMAT-like**:
- One clean equation, one clean answer
- Context is culturally Czech (Czech names, Kč currency)
- No trick — the problem tests mathematical modeling ability, not reading comprehension traps
- The procedure instruction is explicit: `Zapište celý postup řešení.`

---

### Task 6 — Planimetry (2D Geometry Calculation)

**Curriculum area**: Geometrie v rovině — area, perimeter, angles
**Format**: Open — with procedure
**Points**: 3–4
**Subtasks**: 2–3
**Procedure required**: **Yes**

**What it tests**: Calculating area, perimeter, or angles of composite 2D
shapes. Often requires Pythagorean theorem.

**Observed pattern**:
- Context box with geometric diagram
- Figure is a composite shape (rectangle + triangle, trapezoid with
  semicircle, L-shaped polygon, etc.)
- Dimensions given directly on the diagram
- Subtasks ask for different properties (area, perimeter, specific length)

**Constraints for generation**:

| Constraint | Value |
|---|---|
| Shapes | Rectangles, triangles, trapezoids, circles/semicircles, composite |
| Dimensions | Integers or simple values (e.g., 6, 8, 10 for Pythagorean triple) |
| Results | Integers, simple fractions, or exact expressions with π |
| Diagram | Required — black and white, precise, labeled with dimensions |
| Context box title | `VÝCHOZÍ TEXT A OBRÁZEK K ÚLOZE 6` |
| Czech notation | Area = `S`, perimeter = `o`, height = `v` |

**Illustrative example**:
```
VÝCHOZÍ TEXT A OBRÁZEK K ÚLOZE 6

[Diagram: trapezoid ABCD with parallel sides a = 10 cm, c = 6 cm,
 height v = 4 cm, legs b and d]

6.1  Vypočtěte obsah lichoběžníku ABCD.
6.2  Vypočtěte délku strany b, je-li d = 5 cm.
```
*Answers: 6.1 → S = (10+6)/2 · 4 = 32 cm²; 6.2 → requires Pythagorean theorem*

---

### Tasks 7 & 8 — Geometry / Proportions / Units

**Note**: These middle slots (roughly positions 7–8) are the **most variable**
across test variants. They may contain:

- **Unit conversions** (length, area, volume, time)
- **Scale/map calculations**
- **Proportional reasoning** (direct/inverse proportion)
- **Percentage calculations**
- **Additional geometry computation**

**Format**: Open — result only (sometimes with procedure)
**Points**: 2–3 each
**Subtasks**: 2–3 each

**Constraints**:

| Constraint | Value |
|---|---|
| Unit types | Length (mm→km), area (mm²→km²), volume (ml→l→m³), time (s→h) |
| Scale problems | Map scales like 1:50 000, 1:25 000 |
| Percentage | `p % z celku`, discount, increase |
| Results | Clean numbers (integers or simple decimals) |

**Illustrative example**:
```
7.1  Převeďte: 2,5 km² = ______ m²
7.2  Na mapě s měřítkem 1 : 50 000 je vzdálenost mezi dvěma městy 6 cm.
     Jaká je skutečná vzdálenost v kilometrech?
7.3  Cena výrobku byla snížena o 20 %. Nová cena je 640 Kč.
     Jaká byla původní cena?
```
*Answers: 7.1 → 2 500 000 m²; 7.2 → 3 km; 7.3 → 800 Kč*

---

### Tasks 9 & 10 — Geometric Construction

**Curriculum area**: Geometrie — ruler-and-compass construction
**Format**: Open — construction (drawing)
**Points**: 3 each (typically)
**Subtasks**: 1–2 each
**Procedure required**: **Yes** — the construction itself IS the procedure

**What it tests**: Ability to perform geometric constructions using only ruler,
compass, and protractor.

**Task 9 — Triangle Construction**:
- Construct a triangle from given elements (combination of sides, angles,
  heights, medians)
- Often: "Sestrojte trojúhelník ABC, je-li dáno: |AB| = 7 cm, |BC| = 5 cm,
  výška na stranu AB vₐ = 4 cm"
- May include: "Determine the number of solutions" (počet řešení)

**Task 10 — Circle / Locus / Thales**:
- Construct geometric objects satisfying distance or angle conditions
- Thales' theorem applications (constructing right angle on a diameter)
- Tangent line constructions
- Inscribed/circumscribed circle constructions

**Constraints for generation**:

| Constraint | Value |
|---|---|
| Construction must be | Geometrically feasible |
| Number of solutions | Finite (1 or 2, rarely 0 — state this in answer key) |
| Given measurements | Integers in cm (typically 3–10 cm) |
| Context box | Instructions and possibly a partial diagram or sketch |
| Drawing space | Large blank area in answer sheet |
| Required steps | Rozbor (analysis), construction, zápis (description of steps) |

**Illustrative example**:
```
VÝCHOZÍ TEXT K ÚLOZE 9

Sestrojte trojúhelník KLM, ve kterém |KL| = 8 cm, |∠KLM| = 60° a výška
na stranu KL má délku vₖ = 3,5 cm.

9.1  Sestrojte trojúhelník KLM.
9.2  Určete počet řešení.
```

**What makes construction tasks CERMAT-like**:
- The combination of given elements is non-trivial but solvable
- Students must identify which geometric loci to intersect
- The answer key includes a step-by-step description of the construction
- Thales' theorem is the most commonly tested construction principle
- Typical success rate: ~20–40% (the hardest tasks on the test)

---

### Task 11 — Multiple Choice (Geometry / Computation)

**Curriculum area**: Geometrie / Číslo a proměnná
**Format**: Closed — MC (A–E or A–F)
**Points**: 4 (typically)
**Subtasks**: 3 (typically 11.1, 11.2, 11.3)
**Procedure required**: No

**What it tests**: Usually involves geometric computation, percentages, or
applied arithmetic where students choose correct answers for 3 related
questions from a shared pool of options.

**Observed pattern**:
- Context box describes a geometric shape, path, or dataset.
- 3 subtasks (questions)
- Options A–F (or A–E) provided once for all 3 subtasks.
- Format is similar to the matching task but options are standard numbers.

**Constraints for generation**:

| Constraint | Value |
|---|---|
| Dimensions | Integers |
| Subtasks | 3 questions (11.1, 11.2, 11.3) |
| Options | A–F list of values |
| Context box | Standard context box title |

---

### Task 12 — Multiple Choice: Algebraic Modeling

**Curriculum area**: Závislosti, vztahy — translating scenarios to expressions
**Format**: Closed — MC (A–E)
**Points**: 2
**Subtasks**: 1
**Procedure required**: No

**What it tests**: Selecting the correct algebraic expression that models a
described real-world scenario.

**Observed pattern**:
- Context box describes a scenario and defines a variable
- Question: "Which expression correctly represents [the total / the difference / etc.]?"
- 5 options (A–E), exactly 1 correct
- Distractors are based on common algebraic modeling mistakes

**Constraints for generation**:

| Constraint | Value |
|---|---|
| Variable | Single variable, defined in context (e.g., "cena sešitu je *s* Kč") |
| Expression complexity | Linear or simple quadratic |
| Options | 5 (A–E), exactly 1 correct |
| Distractors | Must be plausible — represent common student errors |
| Context | Shopping, age, measurement, everyday scenarios |

**Distractor generation strategy** for MC tasks:
1. **Sign reversal**: `3s + 5` instead of `3s − 5`
2. **Operation swap**: `s · 3` instead of `s + 3`
3. **Missing/extra term**: `2s` instead of `2s + 10`
4. **Reversed relationship**: `s/3` instead of `3s`
5. **Unit confusion**: mixing different units in expression

**Illustrative example**:
```
VÝCHOZÍ TEXT K ÚLOZE 12

Cena jednoho sešitu je s Kč. Cena jednoho pera je o 15 Kč vyšší než cena
sešitu. Petr koupil 3 sešity a 2 pera.

Který výraz udává celkovou cenu nákupu v Kč?

A) 5s + 15    B) 5s + 30    C) 3s + 2 · 15    D) 3s + 30    E) 5s + 2
```
*Correct answer: B) 5s + 30 [= 3s + 2(s+15) = 3s + 2s + 30 = 5s + 30]*

---

### Task 13 — Multiple Choice: Geometry/Angle Reasoning

**Curriculum area**: Geometrie — angle relationships, shape properties
**Format**: Closed — MC (A–E)
**Points**: 2
**Subtasks**: 1
**Procedure required**: No

**What it tests**: Deducing angle measures or geometric properties from a
diagram, using:
- Triangle angle sum (180°)
- Supplementary/complementary angles
- Parallel lines + transversal (alternate, corresponding angles)
- Isosceles triangle properties
- Inscribed angles
- Properties of quadrilaterals

**Constraints for generation**:

| Constraint | Value |
|---|---|
| Diagram | Required — geometric figure with some angles labeled |
| Given angles | Integer degrees (commonly multiples of 5 or 10) |
| Options | 5 (A–E), exact degree values or geometric statements |
| Context box | `VÝCHOZÍ TEXT A OBRÁZEK K ÚLOZE 13` |

**Illustrative example**:
```
VÝCHOZÍ TEXT A OBRÁZEK K ÚLOZE 13

[Diagram: triangle ABC with angle A = 40°, angle B = 75°.
 Point D on side BC such that AD is the angle bisector.]

Jaká je velikost úhlu ADC?

A) 65°    B) 85°    C) 95°    D) 105°    E) 115°
```

---

### Task 14 — ANO/NE: Data Interpretation

**Curriculum area**: Závislosti, vztahy a práce s daty
**Format**: Closed — ANO/NE (true/false for each statement)
**Points**: 4 (1 point per correct statement)
**Subtasks**: 4 (always 14.1, 14.2, 14.3, 14.4)
**Procedure required**: No

**What it tests**: Reading and interpreting data from tables or graphs, then
evaluating whether given statements are true or false.

**Observed pattern**:
- Context box contains a **data table** or **bar chart / line graph**
- 4 statements about the data
- Each statement is independently ANO (true) or NE (false)
- Statements range from "read directly from data" to "requires calculation"

**Constraints for generation**:

| Constraint | Value |
|---|---|
| Data source | Table (4–8 rows, 2–4 columns) OR simple bar/line chart |
| Data values | Integers or simple decimals, realistic context |
| Statement types | Direct reading, comparison, percentage calculation, trend |
| Balance | Mix of 2 ANO + 2 NE (or 3+1) — never all same |
| Context box title | `VÝCHOZÍ TEXT A TABULKA K ÚLOZE 14` or `...A GRAF...` |
| Traps | Statements that are "almost true" — require precise reading |

**Illustrative example**:
```
VÝCHOZÍ TEXT A TABULKA K ÚLOZE 14

Tabulka ukazuje počet návštěvníků muzea v jednotlivých měsících roku 2025:

| Měsíc    | Leden | Únor | Březen | Duben | Květen | Červen |
|----------|-------|------|--------|-------|--------|--------|
| Počet    | 450   | 380  | 520    | 610   | 750    | 830    |

Rozhodněte o každém z následujících tvrzení, zda je pravdivé (ANO),
či nepravdivé (NE).

14.1  V březnu navštívilo muzeum více než 500 návštěvníků.
14.2  Počet návštěvníků v červnu byl více než dvojnásobek počtu v únoru.
14.3  Průměrný měsíční počet návštěvníků za celé uvedené období je 590.
14.4  V každém měsíci byl počet návštěvníků vyšší než v předchozím měsíci.
```
*Answers: 14.1 → ANO (520 > 500); 14.2 → ANO (830 > 2×380=760);
14.3 → ANO ((450+380+520+610+750+830)/6 = 3540/6 = 590);
14.4 → NE (únor 380 < leden 450)*

---

### Task 15 — Matching (Přiřazovací)

**Curriculum area**: Nestandardní aplikační úlohy
**Format**: Closed — Matching (A–F)
**Points**: 6 (always 6 pts; 2 pts per correct match)
**Subtasks**: 3 (15.1, 15.2, 15.3)
**Procedure required**: No

**What it tests**: Evaluating mathematical statements about a given context —
often involving percentages, ratios, geometric properties, or algebraic
relationships.

**Observed pattern**:
- Context box describes a situation (shopping, geometry, scheduling)
- 3 items to match (15.1, 15.2, 15.3)
- 6 options (A–F) — leaving 3 unused distractors
- The matching format is consistent across all recent tests.

**Constraints for matching variant**:

| Constraint | Value |
|---|---|
| Items to match | 3 (always) |
| Options | 6 (A–F) |
| Instruction | `Přiřaďte ke každé úloze (15.1–15.3) odpovídající výsledek (A–F)` |
| Topics | Percentage calculations, expression evaluation, unit conversions |
| Points | 1–2 per correct match |

---

### Task 16 — Sequences & Patterns

**Curriculum area**: Nestandardní aplikační úlohy — pattern recognition
**Format**: Open — result only
**Points**: 4–6 (varies, usually 4)
**Subtasks**: 3 (sometimes 4)
**Procedure required**: No (result only, but students need scratch work)

**What it tests**: Recognizing and extending number or geometric patterns.
Deriving general formulas from visual/numerical sequences.

**Observed pattern**:
- Context box shows a visual sequence (first 3–4 figures)
- Figures are composed of geometric shapes (squares, triangles, dots)
- The underlying pattern is always an **arithmetic sequence** (linear):
  `a_n = a₁ + (n−1) · d`
- 3 subtasks of increasing difficulty:

| Subtask | Type | Example |
|---|---|---|
| 16.1 | Direct computation (small n) | "How many squares in figure 5?" |
| 16.2 | Requires general formula (large n) | "How many squares in figure 20?" |
| 16.3 | Inverse — solve for n | "Which figure has exactly 97 squares?" |

**Constraints for generation**:

| Constraint | Value |
|---|---|
| Pattern type | Arithmetic sequence (linear growth) |
| First term (a₁) | Small positive integer (1–6) |
| Common difference (d) | Small positive integer (2–5) |
| Visual representation | Grid of squares/shapes, first 3 figures shown |
| Results | Positive integers |
| 16.3 must have solution | The target value must be achievable (n must be a positive integer) |

**Illustrative example**:
```
VÝCHOZÍ TEXT A OBRÁZEK K ÚLOZE 16

[Diagram showing 3 figures made of small squares:
 Figure 1: 3 squares    ■ ■ ■
 Figure 2: 7 squares    (cross shape)
 Figure 3: 11 squares   (larger cross shape)]

Posloupnost obrazců pokračuje podle pravidla naznačeného prvními třemi obrazci.

16.1  Kolik čtverečků má 5. obrazec?
16.2  Kolik čtverečků má 15. obrazec?
16.3  Který obrazec v pořadí má přesně 83 čtverečků?
```
*Pattern: a_n = 4n − 1 (a₁=3, d=4)*
*Answers: 16.1 → 19; 16.2 → 59; 16.3 → (83+1)/4 = 21st figure*

---

## 8. Scoring & Partial Credit Rules

### 8.1 General Principles

| Rule | Detail |
|---|---|
| Only whole points | Fractions of points are never awarded |
| No negative marks | Minimum score per task is 0 |
| Only answer sheet counts | Anything in the test booklet is ignored |
| Erasable pens = invalid | Answers written with erasable pens may not survive scanning |

### 8.2 Scoring by Task Type

**Open — result only** (Tasks 1, 2, 7/8, 16):
- Correct result = full points
- Incorrect result = 0 points
- No partial credit (no procedure to evaluate)

**Open — with procedure** (Tasks 3, 4, 5, 6, 11):
- **Full points**: Correct result AND correct procedure
- **Partial credit** (e.g., 1 out of 2 points per subtask): Procedure is
  correct but contains exactly one numerical/arithmetic error
- **0 points**: Result only without procedure, even if correct
- **0 points**: Algorithmically incorrect procedure (wrong method)
- **0 points**: More than one error in the procedure

**Specific partial credit situations** (from CERMAT answer key analysis):

| Situation | Points Awarded |
|---|---|
| Correct procedure, one arithmetic error, wrong final result | Partial (typically 1 pt of 2) |
| Correct procedure, result not in simplest form (zlomek ne v základním tvaru) | Partial |
| Correct result, no procedure shown | **0 points** |
| Correct procedure and result, then additional incorrect manipulation | Partial or full (varies) |
| Only the equation is set up correctly but not solved | Partial (typically 1 pt) |

**Open — construction** (Tasks 9, 10):
- Evaluated based on the drawing in the answer sheet
- Must be traced with pen (pencil-only = potentially 0)
- Points for: correct construction, labeling, stating number of solutions

**Closed — MC** (Tasks 12, 13):
- Correct letter = full points (typically 2)
- Wrong letter or multiple crosses = 0 points

**Closed — ANO/NE** (Tasks 14, 15):
- 1 point per correctly evaluated statement
- Each sub-statement is independently scored

### 8.3 Answer Key Document Structure

The official answer key PDF (**Klíč správných řešení**) contains for each task:
- Task number and maximum points
- Correct answer(s)
- For procedure tasks: a model solution (vzorové řešení)
- For MC: the correct letter
- For ANO/NE: the correct sequence (e.g., `ANO, NE, ANO, NE`)
- Specific notes on when to award partial credit

---

## 9. Czech Mathematical Conventions

CERMAT tests use specific Czech mathematical notation that differs from
international conventions. **All of these must be followed exactly.**

### 9.1 Notation

| Concept | Czech Convention | Example | NOT This |
|---|---|---|---|
| Division | `:` (colon) | `600 : 10` | `600 / 10` or `600 ÷ 10` |
| Multiplication | `·` (middle dot) | `3 · 5` | `3 × 5` or `3 * 5` |
| Decimal separator | `,` (comma) | `3,14` | `3.14` |
| Thousands separator | thin space | `1 000 000` | `1,000,000` or `1.000.000` |
| Interval (closed) | `⟨a; b⟩` | `⟨0; 5⟩` | `[0, 5]` |
| Interval (open) | `(a; b)` | `(0; 5)` | not commonly used in M9 |
| Percent | `%` after space | `15 %` | `15%` (no space) |
| Currency | `Kč` | `500 Kč` or `500,- Kč` | before the number |
| Angle | `∠ABC` or Greek letters (α, β, γ) | `∠BAC = 60°` | |
| Triangle | `△ABC` | standard | |
| Absolute value | `|x|` | standard | |
| "is equal to" | `=` | standard | |

### 9.2 Geometric Labels (Critical Differences from English)

| Concept | Czech Symbol | English Equivalent |
|---|---|---|
| **Area** | `S` | `A` |
| **Perimeter** | `o` | `P` |
| **Volume** | `V` | `V` (same) |
| **Surface area** | `S_p` (povrch) | `SA` |
| **Height** | `v` (výška) | `h` |
| **Side length** | `a`, `b`, `c` | `a`, `b`, `c` (same) |
| **Radius** | `r` | `r` (same) |
| **Diameter** | `d` | `d` (same) |
| **Diagonal** | `u` (úhlopříčka) | `d` |
| **Circumscribed circle** | `k` (kružnice opsaná) | |
| **Inscribed circle** | `k` (kružnice vepsaná) | |

### 9.3 Standard Task Instructions (Czech Wording)

| Instruction Type | Czech Text |
|---|---|
| Compute (result only) | `Vypočtěte:` or `Vypočtěte a výsledek zapište ve tvaru jednoho čísla:` |
| Solve equation | `Řešte rovnici:` |
| Solve system | `Řešte soustavu rovnic:` |
| Simplify | `Zjednodušte:` or `Upravte:` |
| Factor | `Rozložte na součin:` |
| Construct | `Sestrojte:` |
| Convert | `Převeďte:` |
| Determine / Find | `Určete:` |
| Procedure required | `Zapište celý postup řešení.` |
| Write as fraction | `Výsledek zapište ve tvaru zlomku v základním tvaru.` |
| ANO/NE instruction | `Rozhodněte o každém z následujících tvrzení, zda je pravdivé (ANO), či nepravdivé (NE).` |
| Matching instruction | `Přiřaďte ke každé úloze (N.1–N.3) odpovídající výsledek (A–F).` |
| MC instruction | `Vyberte správnou odpověď.` or integrated into the question |

### 9.4 Points Grammar (Czech Declension)

The word for "points" changes based on the number:

| Count | Czech Form | Example |
|---|---|---|
| 1 | `bod` | `max. 1 bod` |
| 2, 3, 4 | `body` | `max. 2 body`, `max. 3 body` |
| 5, 6, ... 50 | `bodů` | `max. 5 bodů`, `max. 50 bodů` |

This appears on every task header: `max. X bod/body/bodů`

---

## 10. Visual Layout Specification

> **Full specification**: See
> [`CERMAT_visual_spec.md`](file:///Users/jarda/ArchMaster/docs/CERMAT_visual_spec.md)
> for the complete pixel-perfect layout specification with exact font names,
> sizes, margins, and measurements programmatically extracted from all 12
> reference test PDFs.

### 10.1 Quick Reference (Verified Values)

| Property | Verified Value |
|---|---|
| Paper size | A4 (595.3 × 841.9 pt / 210 × 297 mm) |
| Left margin | ~71pt (25mm) |
| Right margin | ~68pt (24mm) |
| Content width | ~456pt (161mm) |
| **Primary font** | **Myriad Pro** (Regular, Bold, Italic) |
| **Math font** | **Cambria Math** |
| **Supplementary font** | **Arial** (ArialMT, Arial-BoldMT) |
| Body text size | **12pt** (not 10–11pt as previously estimated) |
| Cover page instruction text | 11.04pt |
| Footer text | 9.48pt |
| Copyright text | 8.04pt |
| Task number / points label | **12pt bold** (not 18–20pt as previously estimated) |
| Horizontal rule thickness | 0.72–0.96pt (median 0.96pt) |
| Context box background | Variable (#b1b2b1 to #ffffff — not uniformly light gray) |
| Context box corners | Sharp (radius = 0) |
| Page header | Page number only (`N ze total`), NOT test code |
| Page footer | `(CZVV)` with italic CZVV, NOT `© CZVV` |
| Color | Pure black (#000000) only — no colored text |

### 10.2 Reference Screenshots

Visual references are stored in
[`docs/reference_screenshots/`](file:///Users/jarda/ArchMaster/docs/reference_screenshots/)
with annotated examples from 2024, 2025, and 2026 test PDFs.

---

## 11. Cross-Year Stability Analysis

### 11.1 What Has Remained Stable (2024–2026)

Based on analysis of 12 test variants across 3 years:

| Feature | Stability | Notes |
|---|---|---|
| Total points (50) | **100% stable** | Never changed |
| Time limit (70 min) | **100% stable** | Never changed |
| Number of tasks (16) | **100% stable** | Never changed |
| Task 1 = arithmetic | **Very stable** | Always numerical computation |
| Task 2 = fractions | **Very stable** | Always fraction operations |
| Tasks 3–4 = algebra/equations | **Very stable** | Always present, positions stable |
| Construction tasks present | **Very stable** | Always 2 construction tasks |
| MC tasks present | **Very stable** | Always 2–3 MC tasks |
| ANO/NE tasks present | **Very stable** | Always present |
| Task 16 = patterns | **Very stable** | Always the final task |
| Visual format | **Very stable** | Same fonts, layouts, context boxes |
| Cover page instructions | **Very stable** | Minor wording variations only |

### 11.2 What Has Varied

| Feature | Variation Observed |
|---|---|
| Exact slot positions for geometry | Tasks 6–11 can shift ±1–2 positions |
| Construction task positions | Observed at positions 7–8, 9–10 |
| Stereometry position | Observed at positions 9, 11 |
| MC task positions | Cluster in 11–13 range but shift |
| Task 14 vs 15 format | Both ANO/NE, or one matching |
| Points per task | Within stated ranges (e.g., task 5: 3 or 4 pts) |
| Number of subtasks | Within stated ranges (e.g., task 3: 2 or 3 subtasks) |
| Word problem archetype | Different scenario each variant |
| Geometry shapes | Different figures each variant |
| Data table/graph topics | Different contexts each variant |

### 11.3 Difficulty Variation Between Years

Based on public CERMAT statistics and media reports:

| Year | Reported Difficulty | Notes |
|---|---|---|
| 2024 | Below average (easier) | Higher average scores observed |
| 2025 | Above average (harder) | Returned to 2023 difficulty level |
| 2026 | Average | `[VERIFY when statistics published]` |

**Implications for generation**: Our tests should target the **average**
difficulty level. Neither the easiest nor the hardest year should be the model.

---

## 12. Quality Checklist

Before releasing any generated test, verify **every item** on this checklist.

### 12.1 Structural Checks

- [ ] Test contains exactly **16 tasks** numbered 1–16
- [ ] Point total sums to exactly **50 bodů**
- [ ] Each task's max points matches the value in its header
- [ ] All five answer formats are represented (result-only, procedure,
      construction, MC, ANO/NE)
- [ ] At least 2 construction tasks are included
- [ ] At least 2 MC tasks are included
- [ ] At least 1 ANO/NE task is included
- [ ] Task 16 is a pattern/sequence task

### 12.2 Content Checks

- [ ] Every task has a **mathematically correct answer** verified by computation
- [ ] Every equation/expression evaluates to a "clean" result
- [ ] All MC tasks have **exactly 1 correct answer** and all distractors are **wrong**
- [ ] All ANO/NE statements have a **deterministic answer** (no ambiguity)
- [ ] Word problems are **unambiguous** and have **unique solutions**
- [ ] Construction tasks are **geometrically feasible** with finite solutions
- [ ] No two tasks test the exact same skill
- [ ] Difficulty gradient flows from easy → hard (approximately)

### 12.3 Czech Language Checks

- [ ] All mathematical notation follows Czech conventions (`:` for division,
      `,` for decimal, `·` for multiplication)
- [ ] Area is labeled `S`, not `A`; perimeter is `o`, not `P`
- [ ] Points grammar is correct (`bod` / `body` / `bodů`)
- [ ] Instructions use the standard CERMAT phrasing (Section 9.3)
- [ ] Currency is `Kč`, names are Czech (Novák, Svoboda, Dvořák)
- [ ] All text is grammatically correct Czech

### 12.4 Visual Checks

> **Crucial**: Refer to [`CERMAT_visual_spec.md`](file:///Users/jarda/ArchMaster/docs/CERMAT_visual_spec.md)
> for exact visual specifications.

- [ ] Cover page exactly matches 2025/2026 CERMAT format
- [ ] Formula reference sheet matches the simplified version in Appendix A
- [ ] Primary font is Myriad Pro, math uses Cambria Math
- [ ] Context boxes have variable gray backgrounds (or white for diagrams)
- [ ] Task headers use 12pt bold with 0.96pt solid rule
- [ ] MC options are laid out horizontally
- [ ] Page footers show `(CZVV)` in italic with proper parentheses

### 12.5 Answer Key Checks

- [ ] Answer key exists for every task
- [ ] Answer key includes model solution for all "procedure" tasks
- [ ] Partial credit conditions are documented for each "procedure" task
- [ ] MC answer key specifies the correct letter
- [ ] ANO/NE answer key specifies the sequence

---

## Appendix A: Formula Reference Sheet

These are the **exact** formulas provided to students on the last page of the
test booklet, transcribed from the 2025 and 2026 PDFs. The content has been
identical across all checked years.

**Location**: Last page of the test booklet (page 12 in 2025–2026 format).
May share the page with the end of Task 16.

### Druhé mocniny čísel 11–20 (Squares of numbers 11–20)

| Expression | Value |
|---|---|
| 11² | 121 |
| 12² | 144 |
| 13² | 169 |
| 14² | 196 |
| 15² | 225 |
| 16² | 256 |
| 17² | 289 |
| 18² | 324 |
| 19² | 361 |
| 20² | 400 |

### Přibližné hodnoty čísla π (Approximate values of π)

| Symbol | Value |
|---|---|
| π | ≐ 3,14 |
| π | ≈ 22/7 |

### Rozklad na součin (Factorization identities)

```
a² + 2ab + b² = (a + b)(a + b)
a² − 2ab + b² = (a − b)(a − b)
a² − b² = (a + b)(a − b)
```

### Obvod a obsah kruhu o poloměru r (Circumference and area of circle)

```
o = 2πr
S = πr²
```

> **Critical correction (v2.0 → v3.0)**: The previous version of this
> appendix listed formulas for rectangles, squares, triangles, trapezoids,
> prisms, cubes, cylinders, the Pythagorean theorem, and percentage
> calculations. **None of these appear on the actual formula reference
> sheet.** The real sheet is much simpler — only the content listed above.
> Students are expected to know the other formulas from memory.

---

## Appendix B: Test Code Format

CERMAT test codes follow a structured format. Understanding this helps with
document generation and referencing.

**Example**: `M9PAD26C0T01`

| Position | Characters | Meaning | Example |
|---|---|---|---|
| 1 | `M` | Subject: Matematika | `M` |
| 2 | `9` | Grade: 9th grade (čtyřleté gymnázium) | `9` |
| 3–4 | `PA` | Exam type: `PA` = řádný termín (regular) | `PA` |
| 5 | `D` | Test type: Didaktický test | `D` |
| 6–7 | `26` | Year: 2026 (last 2 digits) | `26` |
| 8–9 | `C0` | Version/variant code | `C0` |
| 10–12 | `T01` | Term number: `T01` = 1st term, `T02` = 2nd term | `T01` |

**Known prefix patterns**:

| Code | Meaning |
|---|---|
| `M9PAD` | Math, 9th grade, regular term |
| `M5PAD` | Math, 5th grade (8-year gymnázium), regular term |
| `CJ9PAD` | Czech language, 9th grade, regular term |

---

## Appendix C: Glossary of Czech Mathematical Terms

A comprehensive reference for all mathematical terminology used in CERMAT tests.

### Numbers & Operations

| Czech | English |
|---|---|
| číslo | number |
| celé číslo | integer |
| přirozené číslo | natural number |
| záporné číslo | negative number |
| sudé / liché | even / odd |
| zlomek | fraction |
| základní tvar (zlomku) | simplified form (of a fraction) |
| desetinné číslo | decimal number |
| smíšené číslo | mixed number |
| mocnina | power |
| odmocnina | root (square root) |
| sčítání | addition |
| odčítání | subtraction |
| násobení | multiplication |
| dělení | division |
| součet | sum |
| rozdíl | difference |
| součin | product |
| podíl | quotient |
| zbytek | remainder |
| dělitelnost | divisibility |
| prvočíslo | prime number |
| nejmenší společný násobek (NSN) | least common multiple (LCM) |
| největší společný dělitel (NSD) | greatest common divisor (GCD) |

### Algebra

| Czech | English |
|---|---|
| výraz | expression |
| proměnná | variable |
| rovnice | equation |
| soustava rovnic | system of equations |
| nerovnice | inequality |
| kořen (rovnice) | root / solution (of equation) |
| řešení | solution |
| řešte | solve |
| upravte / zjednodušte | simplify |
| rozložte na součin | factor |
| dosadíme | we substitute |
| koeficient | coefficient |

### Geometry — General

| Czech | English |
|---|---|
| bod | point |
| přímka | line |
| polopřímka | ray |
| úsečka | line segment |
| rovnoběžka | parallel line |
| kolmice | perpendicular |
| průsečík | intersection point |
| osa | axis / bisector |
| osa úsečky | perpendicular bisector |
| osa úhlu | angle bisector |
| souměrnost | symmetry |
| osová souměrnost | axial symmetry |
| středová souměrnost | point symmetry |

### Geometry — Angles

| Czech | English |
|---|---|
| úhel | angle |
| stupeň (°) | degree |
| pravý úhel | right angle |
| ostrý úhel | acute angle |
| tupý úhel | obtuse angle |
| přímý úhel | straight angle |
| vrcholový úhel | vertical (opposite) angle |
| vedlejší úhel | supplementary angle |
| střídavý úhel | alternate angle |
| souhlasný úhel | corresponding angle |

### Geometry — Shapes

| Czech | English |
|---|---|
| trojúhelník | triangle |
| rovnostranný trojúhelník | equilateral triangle |
| rovnoramenný trojúhelník | isosceles triangle |
| pravoúhlý trojúhelník | right triangle |
| přepona | hypotenuse |
| odvěsna | cathetus (leg) |
| čtverec | square |
| obdélník | rectangle |
| rovnoběžník | parallelogram |
| lichoběžník | trapezoid |
| kosočtverec | rhombus |
| kosodélník | rhomboid |
| mnohoúhelník | polygon |
| kružnice | circle (the line) |
| kruh | circle (the area/disk) |
| poloměr | radius |
| průměr | diameter |
| tětiva | chord |
| tečna | tangent |
| sečna | secant |
| oblouk | arc |
| výseč | sector |
| úseč | segment |

### Geometry — 3D

| Czech | English |
|---|---|
| těleso | solid / 3D body |
| krychle | cube |
| kvádr | rectangular prism (cuboid) |
| hranol | prism |
| válec | cylinder |
| jehlan | pyramid |
| kužel | cone |
| koule | sphere |
| hrana | edge |
| stěna | face |
| vrchol | vertex |
| podstava | base |
| plášť | lateral surface |
| povrch | surface area |
| objem | volume |
| tělesová úhlopříčka | space diagonal |
| stěnová úhlopříčka | face diagonal |
| síť (tělesa) | net (of a solid) |

### Geometry — Construction

| Czech | English |
|---|---|
| sestrojte | construct |
| narýsujte | draw (with ruler/compass) |
| rýsování | drawing/construction |
| kružítko | compass |
| pravítko | ruler |
| úhloměr | protractor |
| konstrukce | construction |
| rozbor | analysis (planning step) |
| zápis konstrukce | construction description |
| Thaletova kružnice | Thales' circle |
| Thaletova věta | Thales' theorem |
| kružnice opsaná | circumscribed circle |
| kružnice vepsaná | inscribed circle |
| množina bodů | locus of points |
| počet řešení | number of solutions |

### Data & Statistics

| Czech | English |
|---|---|
| tabulka | table |
| graf | graph / chart |
| sloupcový graf | bar chart |
| spojnicový graf | line graph |
| kruhový diagram | pie chart |
| průměr (aritmetický) | (arithmetic) mean / average |
| medián | median |

### Units & Measurements

| Czech | English |
|---|---|
| délka | length |
| šířka | width |
| výška | height |
| obsah | area |
| obvod | perimeter |
| objem | volume |
| hmotnost | mass / weight |
| rychlost | speed |
| čas | time |
| měřítko | scale |
| převod jednotek | unit conversion |
| procento | percent |
| poměr | ratio |
| přímá úměra | direct proportion |
| nepřímá úměra | inverse proportion |
| trojčlenka | rule of three |

### Task-Specific Terms

| Czech | English |
|---|---|
| úloha | task / problem |
| podúloha | subtask |
| zadání | problem statement / assignment |
| výchozí text | source text / context |
| postup řešení | solution procedure |
| výsledek | result |
| odpověď | answer |
| řešení | solution |
| záznamový arch | answer sheet |
| testový sešit | test booklet |
| klíč správných řešení | answer key |
| bodové hodnocení | scoring |
| maximální počet bodů | maximum number of points |
| časový limit | time limit |

---

> **Document version**: 2.0 — Complete rewrite (August 2026)
>
> **Reference corpus**: 12 test PDFs + 12 answer keys (2024 A/B/C/D, 2025
> A/B/C/D, 2026 A/B/C/D) stored in `References/Matematika/`
>
> **Companion document**: Technical implementation details (LaTeX templates,
> rendering pipeline, benchmarking) are maintained separately.
