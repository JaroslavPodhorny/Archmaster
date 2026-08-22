# CERMAT M9 Mathematics Test — Visual & Layout Specification

> **Purpose**: Pixel-perfect layout specification for producing CERMAT M9 math
> test PDFs (testový sešit) that are visually indistinguishable from official
> exams. Every measurement in this document is **programmatically extracted**
> from the 12 reference test PDFs (2024–2026) using PyMuPDF.
>
> **Companion document**: Content rules, task taxonomy, and Czech conventions
> are in [`CERMAT_handybook.md`](file:///Users/jarda/ArchMaster/docs/CERMAT_handybook.md).
>
> **Data sources**: [`layout_metrics.json`](file:///Users/jarda/ArchMaster/docs/data/layout_metrics.json),
> [`cross_reference.json`](file:///Users/jarda/ArchMaster/docs/data/cross_reference.json)

---

## Table of Contents

1. [Typography System](#1-typography-system)
2. [Page Geometry](#2-page-geometry)
3. [Cover Page Specification](#3-cover-page-specification)
4. [Page Headers & Footers](#4-page-headers--footers)
5. [Task Header Format](#5-task-header-format)
6. [Context Box Format](#6-context-box-format)
7. [Answer Format Layouts](#7-answer-format-layouts)
8. [Mathematical Typesetting](#8-mathematical-typesetting)
9. [Diagrams & Figures](#9-diagrams--figures)
10. [Formula Reference Sheet](#10-formula-reference-sheet)
11. [Answer Sheet Specification](#11-answer-sheet-záznamový-arch)
12. [Reference Screenshots Index](#12-reference-screenshots-index)
13. [Year-Over-Year Layout Changes](#13-year-over-year-layout-changes)

---

## 1. Typography System

### 1.1 Font Stack

The CERMAT M9 test uses **three font families**. This was confirmed across
all 12 test PDFs (2024–2026):

| Font | Role | Variants Used |
|---|---|---|
| **Myriad Pro** | Primary text font — body, instructions, headers, labels | `MyriadPro-Regular`, `MyriadPro-Bold`, `MyriadPro-It` (italic) |
| **Cambria Math** | Mathematical symbols, variables, operators, equations | `CambriaMath`, `Cambria-Italic` |
| **Arial** | Fallback / supplementary text (tasks, options) | `ArialMT`, `Arial-BoldMT` |

> **Critical correction**: The previous handybook claimed "Arial or close
> derivative (Helvetica is acceptable)" — this is **wrong**. The primary
> font is **Myriad Pro**, an Adobe typeface. Arial appears only as a
> supplementary font for certain text elements.

### 1.2 Font Size Roles

Extracted from all 12 tests, sorted by frequency of use:

| Size (pt) | Font | Weight | Role | Usage Count |
|---|---|---|---|---|
| **12.00** | MyriadPro-Regular | Normal | Body text, task instructions, subtask text | 4568× (dominant) |
| **12.00** | MyriadPro-Bold | Bold | Task numbers, point labels, context box titles, key phrases | 1443× |
| **12.00** | CambriaMath | Normal | Mathematical expressions, variables, operators | 559× |
| **12.00** | MyriadPro-It | Italic | Emphasized terms, variable names in text context | 496× |
| **12.00** | ArialMT | Normal | Supplementary body text, option labels | 465× |
| **12.00** | Arial-BoldMT | Bold | Bold supplementary text | 147× |
| **11.04** | MyriadPro-Regular | Normal | Cover page instruction text | 852× |
| **11.04** | MyriadPro-Bold | Bold | Cover page section headings | 384× |
| **11.04** | CambriaMath | Normal | Math in cover page context | 360× |
| **14.04** | MyriadPro-Bold | Bold | `DIDAKTICKÝ TEST` subtitle | 48× |
| **9.48** | MyriadPro-Regular | Normal | Footer parenthetical text | 186× |
| **9.48** | MyriadPro-It | Italic | Footer copyright attribution (`CZVV`) | 93× |
| **8.04** | MyriadPro-Regular | Normal | Copyright notice text | 147× |
| **8.52** | MyriadPro-Regular | Normal | Superscripts (exponents in body) | 76× |
| **21.96** | MyriadPro-Bold | Bold | Title: `MATEMATIKA 9 A` (cover page) | 2× per test |
| **15.96** | MyriadPro-Regular | Normal | Term designation: `1. ŘÁDNÝ TERMÍN` | 1× per test |
| **15.96** | MyriadPro-Bold | Bold | Test code: `M9PAD26C0T01` | 1× per test |

### 1.3 Color

All text across all 12 tests uses **pure black** (`#000000`). No colored
text appears anywhere in the document. The only non-black elements are:
- Gray background fills in context boxes
- Gray shading in geometric diagrams

---

## 2. Page Geometry

### 2.1 Page Dimensions

Consistent across all 12 tests:

| Property | 2024 Tests | 2025–2026 Tests | Unit |
|---|---|---|---|
| Width | 595.28 | 595.32 | pt |
| Height | 841.89 | 841.92 | pt |
| Width | 210.0 | 210.0 | mm |
| Height | 297.0 | 297.0 | mm |

Standard **A4** paper. The 0.04pt difference between years is negligible
(rounding in PDF generation tools).

### 2.2 Page Count

| Year | Variant A | Variant B | Variant C | Variant D |
|---|---|---|---|---|
| 2024 | **13** | **15** | **14** | **11** |
| 2025 | 12 | 12 | 12 | 12 |
| 2026 | 12 | 12 | 12 | 12 |

> **Key finding**: CERMAT standardized to **12 pages** starting in 2025.
> The 2024 tests had variable page counts (11–15). For test generation,
> target **12 pages** as the canonical layout.

### 2.3 Margins (Content Pages, Excluding Cover Page)

Derived from text bounding boxes across all content pages (pages 2+):

| Margin | Median (pt) | Median (mm) | Min (pt) | Max (pt) |
|---|---|---|---|---|
| **Left** | 70.94 | 25.0 | 68.42 | 294.82* |
| **Right** | 68.40 | 24.1 | 66.12 | 521.0* |
| **Top** | 27.96 | 9.9 | 27.96 | 815.57* |
| **Bottom** | 13.12 | 4.6 | 11.30 | 507.55* |

*\*Large maximum values come from pages with very little content (e.g.,
construction task pages with only a header, or pages where text is
concentrated in a small area).*

**Effective content area** (using median margins):
- Left edge: ~71pt from left page edge
- Right edge: ~527pt from left page edge (= 595 − 68)
- **Content width**: ~456pt (~161mm)
- Top edge: ~28pt from top page edge
- Bottom edge: ~829pt from top page edge (= 842 − 13)

### 2.4 Two-Column Cover Page

The cover page uses a **two-column layout** for the instructions:
- Left column: ~55% width — instruction text
- Right column: ~45% width — MC cross-marking example diagram

The exact column boundaries vary slightly by year.

---

## 3. Cover Page Specification

### 3.1 Complete Cover Page Text (2025–2026 Format)

The following is the **exact text** transcribed from the 2025 and 2026
cover page PDFs. Text in `{braces}` varies per test:

```
{JEDNOTNÁ PŘIJÍMACÍ ZKOUŠKA 2026}
{TESTOVÝ SEŠIT}

MATEMATIKA 9 {A}
{1. ŘÁDNÝ TERMÍN}
{M9PAD26C0T01}

DIDAKTICKÝ TEST

Jméno a příjmení{:                    }

Počet úloh: 16
Maximální bodové hodnocení: 50 bodů
Povolené pomůcky: pouze psací a rýsovací potřeby

───────────────────────────────────────────────────

1  Základní informace k zadání zkoušky

•  Časový limit pro řešení didaktického testu
   je uveden na záznamovém archu.
•  U každé úlohy je uveden maximální počet
   bodů.
•  Za neuvedené řešení úlohy či za nesprávné
   řešení úlohy jako celku se neudělují
   záporné body.
•  Odpovědi pište do záznamového archu.
•  Poznámky si můžete dělat do testového
   sešitu nebo na volné listy papíru, nebudou
   však předmětem hodnocení.
•  Didaktický test obsahuje otevřené
   a uzavřené úlohy. Uzavřené úlohy
   obsahují nabídku odpovědí. U každé
   takové úlohy nebo podúlohy je právě
   jedna odpověď správná.
•  Na poslední straně testového sešitu
   najdete vybrané vzorce a vztahy.

2  Pravidla správného zápisu
   do záznamového archu

•  Řešení úloh zapisujte do záznamového
   archu modře nebo černě píšící
   propisovací tužkou, která píše dostatečně
   silně a nepřerušovaně.
•  Nejednoznačný nebo nečitelný zápis
   odpovědi bude považován za chybné
   řešení.
•  V konstrukčních úlohách rýsujte tužkou
   a následně vše obtáhněte propisovací
   tužkou.

2.1  Pokyny k otevřeným úlohám

•  Řešení úloh pište čitelně do vyznačených
   bílých polí záznamového archu.
•  Pokud budete chtít provést opravu,
   původní zápis přeškrtněte a nový uveďte
   do stejného pole.
•  Je-li požadován celý postup řešení,
   uveďte jej do záznamového archu. Pokud
   uvedete pouze výsledek, nebudou vám
   přiděleny žádné body.
•  Zápisy uvedené mimo vyznačená bílá
   pole záznamového archu nebudou
   hodnoceny.

2.2  Pokyny k uzavřeným úlohám

•  Odpověď, kterou považujete za správnou,
   zřetelně zakřížkujte v příslušném bílém
   poli záznamového archu, a to přesně
   z rohu do rohu dle obrázku.
•  Pokud budete chtít následně zvolit jinou
   odpověď, pečlivě zabarvěte původně
   zakřížkované pole a zvolenou odpověď
   vyznačte křížkem do nového pole.
•  Jakýkoliv jiný způsob záznamu odpovědí
   (např. dva křížky u jedné otázky) bude
   považován za nesprávnou odpověď.

TESTOVÝ SEŠIT NEOTVÍREJTE, POČKEJTE NA POKYN!
```

### 3.2 Cover Page Element Typography

| Element | Font | Size | Weight | Position |
|---|---|---|---|---|
| `JEDNOTNÁ PŘIJÍMACÍ ZKOUŠKA {year}` | MyriadPro | ~12pt | Bold | Top area |
| `TESTOVÝ SEŠIT` | MyriadPro | ~12pt | Bold | Below exam title |
| `MATEMATIKA 9 {variant}` | MyriadPro-Bold | **21.96pt** | Bold | Prominent, left |
| `{n}. ŘÁDNÝ TERMÍN` | MyriadPro-Regular | **15.96pt** | Normal | Below subject |
| `{test_code}` | MyriadPro-Bold | **15.96pt** | Bold | Below term |
| `DIDAKTICKÝ TEST` | MyriadPro-Bold | **14.04pt** | Bold | Centered |
| `Jméno a příjmení:` | MyriadPro-Regular | 12pt | Normal | Below test type |
| Info box text | MyriadPro-Bold | 12pt | Bold | `Počet úloh:`, etc. |
| Section headings `1`, `2` | MyriadPro-Bold | 11.04pt | Bold | Left column |
| Instruction bullets | MyriadPro-Regular | 11.04pt | Normal | Left column |
| `TESTOVÝ SEŠIT NEOTVÍREJTE...` | MyriadPro-Bold | 12pt | Bold | Bottom of page |
| Copyright notice | MyriadPro-Regular | 8.04pt | Normal | Very top/bottom |

### 3.3 Cover Page Visual Elements

- **Horizontal rules**: Two black rules separating the header area from
  the info box and the info box from the instructions
  - Position: y ≈ 148pt and y ≈ 245pt (from 2026-A)
  - Width: ~456pt (full content width)
  - Thickness: ~0.72pt (thin black fill)
- **MC cross-marking example**: A small diagram in the right column
  showing how to correctly mark answers (boxes labeled A–E with an X)
- **Bullet character**: `•` (bullet, SymbolMT font at 11.04pt on cover page)

---

## 4. Page Headers & Footers

### 4.1 Page Header (All Content Pages)

Present on every page except the cover page (page 1).

| Element | Content | Font | Size |
|---|---|---|---|
| Page number | `{N} ze {total}` (e.g., `2 ze 12`) | MyriadPro-Regular | 12pt |
| Position | Top-right area, y ≈ 28pt from top | | |

> **Note**: The page header does **NOT** repeat the test code on every
> page (correcting a claim in the handybook). Only the page number
> appears in the header.

### 4.2 Page Footer (All Content Pages)

Present on every page except the cover page.

| Element | Content | Font | Size |
|---|---|---|---|
| Copyright | `(CZVV)` | MyriadPro-Regular 9.48pt + MyriadPro-It 9.48pt | 9.48pt |
| Position | Bottom-center or bottom-right | | |

The footer format is: `(` in Regular + `CZVV` in Italic + `)` in Regular

The **extended copyright notice** appears on page 1 (cover page):
`Předmětem autorských práv Centra pro zjišťování výsledků vzdělávání`
(MyriadPro-Regular, 8.04pt)

---

## 5. Task Header Format

### 5.1 Structure

Every task begins with this header pattern:

```
{TaskNumber}                                    max. {X} bod/body/bodů
─────────────────────────────────────────────────────────────────────
```

### 5.2 Typography

| Element | Font | Size | Weight | Alignment |
|---|---|---|---|---|
| Task number | MyriadPro-Bold / Arial-BoldMT | **12pt** | Bold | Left-aligned |
| Points label (`max. X body`) | MyriadPro-Bold | **12pt** | Bold | Right-aligned, same line |

> **Correction**: The handybook claimed task numbers are "~18–20pt, bold".
> Extraction shows they are **12pt bold** — the same size as body text,
> just bold. The visual prominence comes from the bold weight and the
> horizontal rule below, not from a larger font size.

### 5.3 Horizontal Rule

Below the task number line:

| Property | Value | Source |
|---|---|---|
| Thickness | **0.72–0.96pt** (median 0.96pt across all tests) | Vector drawing extraction |
| Width | Full content width (~456pt) | x0 ≈ 69.5pt to x1 ≈ 526pt |
| Color | Pure black (#000000) fill | Drawing fill color |
| Implementation | Thin filled rectangle (not a stroke) | PyMuPDF drawing type = `re` |

### 5.4 Spacing

- Space above task number: ~6–8mm from end of previous task content
- Space between task number line and horizontal rule: ~0–1mm (rule is
  immediately below)
- Space below horizontal rule to task text: ~3–4mm

---

## 6. Context Box Format

### 6.1 Title

Context boxes appear for tasks that have introductory text, diagrams,
tables, or graphs.

| Title Pattern | Used When |
|---|---|
| `VÝCHOZÍ TEXT K ÚLOZE {N}` | Text-only context |
| `VÝCHOZÍ TEXT A OBRÁZEK K ÚLOZE {N}` | Context with geometric diagram |
| `VÝCHOZÍ TEXT A TABULKA K ÚLOZE {N}` | Context with data table |
| `VÝCHOZÍ TEXT A GRAF K ÚLOZE {N}` | Context with chart/graph |

Title font: **MyriadPro-Bold, 12pt, bold**

### 6.2 Box Visual Properties

Extracted from vector drawing analysis across all 12 tests:

| Property | Value | Notes |
|---|---|---|
| Background fill | Variable — see color table below | Not a single consistent color |
| Border | Constructed from thin rectangles (~0.96pt) | Not a CSS-style border |
| Corner radius | **0** — sharp rectangular corners | Confirmed: no rounding |
| Padding | ~3–4mm on all sides | Content offset from box edges |

### 6.3 Context Box Fill Colors (Extracted)

| Color (Hex) | Occurrences | Description |
|---|---|---|
| `#ffffff` | 7 | White (no visible fill) |
| `#bebfbe` | 2 | Medium gray |
| `#d8d9d8` | 2 | Light-medium gray |
| `#dbddde` | 1 | Light gray |
| `#f1f2f1` | 1 | Very light gray |
| `#b1b2b1` | 1 | Darker gray |

> **Key finding**: The context box background is **NOT consistently
> light gray** as the handybook claimed (`~#F0F0F0`). It varies
> significantly — from white to medium gray. Some boxes use a visually
> distinct gray, others appear white. The construction likely depends
> on whether the box contains a diagram (which needs a white background)
> or pure text.
>
> For test generation, use **#EBEBEB** (~92% white) as a good middle
> ground for text-only context boxes, and **white** for boxes containing
> geometric diagrams.

---

## 7. Answer Format Layouts

### 7.1 Multiple Choice (A–E or A–F)

Options are laid out **horizontally** across the content width:

```
A) {option}    B) {option}    C) {option}    D) {option}    E) {option}
```

| Property | Value |
|---|---|
| Labels | Capital letter + `)` — e.g., `A)`, `B)`, `C)` |
| Font | MyriadPro-Bold for label, MyriadPro-Regular for option text |
| Layout | Evenly distributed across content width |
| Typical count | 5 options (A–E), sometimes 6 (A–F) |

### 7.2 ANO/NE (True/False Statements)

Each sub-statement is presented as a block:

```
{N.1}  {Statement text that may wrap to multiple lines.}
{N.2}  {Another statement.}
{N.3}  {Third statement.}
{N.4}  {Fourth statement.}
```

| Property | Value |
|---|---|
| Subtask ID | Bold: `14.1`, `14.2`, etc. |
| Statement text | Regular, indented after ID |
| Always 4 statements | Confirmed across all tests |
| Instruction | `Rozhodněte o každém z následujících tvrzení, zda je pravdivé (ANO), či nepravdivé (NE).` |

### 7.3 Matching (Přiřazovací)

Items to match (3–4) with options (5–6):

```
Přiřaďte ke každé úloze ({N.1}–{N.3}) odpovídající výsledek (A–F).

{N.1}  {item description}
{N.2}  {item description}
{N.3}  {item description}

A) {option}  B) {option}  C) {option}  D) {option}  E) {option}  F) {option}
```

### 7.4 Open — Result Only

```
{N.1}  Vypočtěte: {expression}
{N.2}  Vypočtěte: {expression}
```

No special visual formatting beyond standard subtask layout.

### 7.5 Open — With Procedure

```
Zapište celý postup řešení.

{N.1}  {instruction}
{N.2}  {instruction}
```

The procedure instruction `Zapište celý postup řešení.` appears in
**bold** before the subtasks.

---

## 8. Mathematical Typesetting

### 8.1 Font Usage

| Math Element | Font | Size | Example |
|---|---|---|---|
| Variables | CambriaMath or MyriadPro-It | 12pt | *x*, *y*, *a*, *b* |
| Operators | CambriaMath | 12pt | +, −, ·, =, <, > |
| Numbers in expressions | ArialMT or MyriadPro-Regular | 12pt | 3, 15, 100 |
| Greek letters | CambriaMath | 12pt | π, α, β, γ |
| Superscripts (exponents) | MyriadPro-Regular or CambriaMath | **8.52pt** | ², ³ |
| Subscripts | Reduced size (~8pt) | | |

### 8.2 Fraction Rendering

- **Inline fractions**: Written as stacked fraction with horizontal bar
  when in display context, or as `a/b` in compact inline text
- **Fraction bar**: Thin horizontal rule, same width as the wider of
  numerator/denominator
- **Vertical spacing**: Extra spacing above and below displayed fractions

### 8.3 Division and Multiplication Notation

- Division: `:` (colon) — uses MyriadPro-Regular
- Multiplication: `·` (middle dot, U+00B7) — uses CambriaMath
- These are **Czech standard** and must never be replaced with `/` or `×`

---

## 9. Diagrams & Figures

### 9.1 General Properties

| Property | Value |
|---|---|
| Color | Black lines on white background (always B&W) |
| Line weight (figure edges) | ~0.5–1.0pt |
| Line weight (dimension/auxiliary) | ~0.3–0.5pt (thinner) |
| Dashing | Used for hidden edges in 3D, auxiliary lines in construction |
| Labels | Capital letters (A, B, C, ...) in MyriadPro or Arial |
| Dimensions | Values with units directly on the diagram |
| Shading | Light gray fill for highlighted areas |

### 9.2 3D Diagrams (Stereometry)

- Isometric or parallel projection
- Hidden edges drawn with dashed lines
- Visible edges solid
- Vertex labels at corners

### 9.3 Construction Diagrams

- May include partial given elements (a line, a point, an arc)
- Blank space left for student construction (in the answer sheet)
- Grid lines are NOT provided — construction is on blank paper

---

## 10. Formula Reference Sheet

### 10.1 Location

The formula sheet is on the **last page** of the test booklet (page 12
in 2025–2026 format). It may share the page with the last task (Task 16)
if space permits — this was observed in the 2025 tests.

### 10.2 Title

`Vybrané vzorce a vztahy` — does NOT appear as a standalone title.
Instead, the formulas are organized under category headings.

### 10.3 Exact Content (Transcribed from 2026-A)

The formula sheet contains three sections:

**Druhé mocniny čísel 11–20** (Squares of numbers 11–20):

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

**Přibližné hodnoty čísla π** (Approximate values of π):

| Symbol | Value |
|---|---|
| π | ≐ 3,14 |
| π | ≈ 22/7 |

**Rozklad na součin** (Factorization identities):

```
a² + 2ab + b² = (a + b)(a + b)
a² − 2ab + b² = (a − b)(a − b)
a² − b² = (a + b)(a − b)
```

**Obvod a obsah kruhu o poloměru r** (Circumference and area of circle):

```
o = 2πr
S = πr²
```

> **Critical correction**: The handybook's Appendix A listed formulas for
> rectangles, squares, triangles, trapezoids, prisms, cubes, cylinders,
> and the Pythagorean theorem. The **actual** formula sheet is much
> simpler — only squares of 11–20, π approximations, algebraic identities,
> and circle formulas. The other formulas are NOT provided on the sheet.

---

## 11. Answer Sheet (Záznamový Arch)

> **Status**: The answer sheet (záznamový arch) is a **separate PDF
> document** that is NOT included in the downloaded test booklet PDFs.
> Answer sheet specimens must be obtained separately from
> [prijimacky.cermat.cz](https://prijimacky.cermat.cz).
>
> The specification below is reconstructed from:
> - Cover page instructions describing the answer sheet
> - Answer key structure analysis
> - Official CERMAT documentation

### 11.1 General Properties

| Property | Value |
|---|---|
| Document type | Separate from test booklet |
| Paper size | A4 |
| Purpose | The ONLY document that is evaluated/scored |
| Scanning | Machine-scanned (must be filled with pen, not pencil) |
| Time limit | Printed on the answer sheet (70 minutes) |

### 11.2 Field Types

Based on the cover page instructions and answer key analysis:

**Open — result only fields**: White rectangular boxes/lines for writing
numerical results. One field per subtask.

**Open — with procedure fields**: Large white rectangular areas for
writing the complete solution procedure. Must be big enough for multi-step
algebraic work.

**Open — construction fields**: Large blank area (no grid) for geometric
construction. Students draw with pencil first, then trace with pen.

**Closed — MC fields**: Row of boxes labeled A through E (or F). Student
crosses one from corner to corner with an X.

**Closed — ANO/NE fields**: For each sub-statement: two boxes (ANO / NE).
Student crosses one per statement.

**Closed — matching fields**: For each sub-item: row of option boxes
(A through F). Student crosses one per sub-item.

### 11.3 Cross-Marking Instructions (From Cover Page)

The cover page includes a diagram showing the correct cross-marking
technique. On the actual answer sheet, small boxes (~8–10mm) are provided
for each option. The student marks with an `×` precisely from corner to
corner.

To change an answer: carefully fill in (darken) the original crossed box
completely, then cross the new choice.

### 11.4 Recording Rules Summary

| Rule | Detail |
|---|---|
| Writing instrument | Blue or black ballpoint pen (propisovací tužka) |
| Construction drawing | Pencil first, then traced with pen |
| Corrections (open) | Cross out original, write new in same field |
| Corrections (closed) | Fill original box solid, cross new choice |
| Entries outside fields | NOT evaluated |
| Erasable pens | NOT allowed (may not survive scanning) |
| Procedure required | If stated and not provided → 0 points even if result correct |

---

## 12. Reference Screenshots Index

All screenshots are stored in
[`docs/reference_screenshots/`](file:///Users/jarda/ArchMaster/docs/reference_screenshots/).

### Cover Pages (Full Page, 300 DPI)

| File | Source |
|---|---|
| `cover_page_M9_2024_1_termin_A.png` | 2024 A — shows older format |
| `cover_page_M9_2025_1_termin_A.png` | 2025 A — current format |
| `cover_page_M9_2026_1_termin_A.png` | 2026 A — current format |

### Task Pages

| File | Source |
|---|---|
| `first_task_page_M9_2024_1_termin_A.png` | Page 2 of 2024-A |
| `first_task_page_M9_2025_1_termin_A.png` | Page 2 of 2025-A |
| `first_task_page_M9_2026_1_termin_A.png` | Page 2 of 2026-A |

### Context Boxes

| File | Source |
|---|---|
| `context_box_page_M9_2025_1_termin_A_p4.png` | Page 4 of 2025-A |
| `context_box_page_M9_2026_1_termin_A_p2.png` | Page 2 of 2026-A |

### Headers & Footers

| File | Source |
|---|---|
| `header_M9_2024_1_termin_A.png` | Top 80pt of page 2 |
| `header_M9_2025_1_termin_A.png` | Top 80pt of page 2 |
| `header_M9_2026_1_termin_A.png` | Top 80pt of page 2 |
| `footer_M9_2024_1_termin_A.png` | Bottom 60pt of page 2 |
| `footer_M9_2025_1_termin_A.png` | Bottom 60pt of page 2 |
| `footer_M9_2026_1_termin_A.png` | Bottom 60pt of page 2 |

### Formula Sheets (Full Last Page)

| File | Source |
|---|---|
| `formula_sheet_M9_2024_1_termin_A.png` | Last page of 2024-A |
| `formula_sheet_M9_2025_1_termin_A.png` | Last page of 2025-A |
| `formula_sheet_M9_2026_1_termin_A.png` | Last page of 2026-A |

---

## 13. Year-Over-Year Layout Changes

### 2024 → 2025 Changes

| Aspect | 2024 | 2025+ |
|---|---|---|
| Page count | Variable (11–15) | Stable at 12 |
| Page dimensions | 595.28 × 841.89 pt | 595.32 × 841.92 pt |
| Cover page format | Slightly different structure* | Standardized two-column layout |
| Font stack | Same (MyriadPro + CambriaMath + Arial) | Same |
| Font sizes | Same hierarchy | Same hierarchy |

*\*The 2024 cover page text extraction was less clean, suggesting possible
structural differences in the PDF generation pipeline.*

### 2025 → 2026 Changes

No significant visual changes detected. The 2025 and 2026 tests appear
to use the same PDF template.

---

> **Document version**: 1.0 — Initial extraction (August 2026)
>
> **Data sources**: 12 test PDFs + 12 answer key PDFs from
> `References/Matematika/`, analyzed with PyMuPDF via
> [`analyze_cermat_layout.py`](file:///Users/jarda/ArchMaster/scripts/analyze_cermat_layout.py)
>
> **Companion documents**:
> - [`CERMAT_handybook.md`](file:///Users/jarda/ArchMaster/docs/CERMAT_handybook.md) — Content rules and task specifications
> - [`layout_metrics.json`](file:///Users/jarda/ArchMaster/docs/data/layout_metrics.json) — Raw extracted typography and layout data
> - [`cross_reference.json`](file:///Users/jarda/ArchMaster/docs/data/cross_reference.json) — Per-test, per-task content metadata
