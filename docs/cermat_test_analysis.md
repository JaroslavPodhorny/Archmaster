# CERMAT M9 Mathematics Test — Complete Analysis & Generation Blueprint

> **Purpose**: This document is the single source of truth for understanding
> CERMAT M9 math entrance exams deeply enough to build an engine that produces
> tests indistinguishable from real ones — both visually and content-wise.

---

## 1. What Is CERMAT / JPZ

**CERMAT** (Centrum pro zjišťování výsledků vzdělávání — CZVV) is the Czech
government agency responsible for standardized testing. The **Jednotná přijímací
zkouška (JPZ)** — Unified Entrance Exam — is the mandatory test students take
when applying to secondary schools (gymnázia) offering maturita programs.

The **M9** designation means **Mathematics for 9th-grade applicants** (students
entering 4-year gymnázium). There is also M5 for students entering 8-year
gymnázium from 5th grade.

### Key Facts

| Parameter | Value |
|---|---|
| Time limit | 70 minutes |
| Max score | 50 points |
| Number of tasks | 16 |
| Allowed aids | Pen, pencil, ruler, compass, protractor only |
| Forbidden | Calculator, math tables |
| Answer recording | Answers go onto a separate **záznamový arch** (answer sheet) for scanning |
| Scoring | Whole points only, no negative marks |
| Attempts | Student takes exam at 2 schools, better result counts |

### Official Sources

- Test PDFs: `prijimacky.cermat.cz` → Testová zadání
- Practice app: `tau.cermat.cz`
- Curriculum spec: Specifikace požadavků k JPZ (based on RVP ZV)

---

## 2. Test Document Structure (Visual / Layout)

This section describes the physical layout of the PDF as printed for
students. Based on analysis of reference PDFs from 2024, 2025, and 2026.

### 2.1 Page Layout

| Property | Value |
|---|---|
| Paper size | A4 (210 × 297 mm) |
| Margins | ~20 mm left/right, ~15 mm top/bottom |
| Content area | ~170 mm wide |
| Font family | Sans-serif (appears to be Arial or a close derivative) |
| Body text size | ~10–11 pt |
| Printing | Black and white only (all gray tones, no color) |

### 2.2 Document Sections (Page by Page)

A typical M9 test PDF has **11–12 pages** structured as:

| Page | Content |
|---|---|
| **Page 1** | **Cover page**: Test title banner, test code (e.g., `M9PAD26C0T01`), max points, time limit, instructions, formula reference sheet |
| **Page 2** | Tasks 1–2 (simple computational tasks) |
| **Page 3** | Tasks 3–4 (algebraic/equation tasks) |
| **Page 4** | Tasks 5–6 (word problem + planimetry) |
| **Page 5** | Tasks 7–8 (construction geometry) |
| **Page 6** | Task 9 (stereometry/3D geometry — typically takes full page) |
| **Page 7** | Task 10 (units/conversions or proportional reasoning) |
| **Page 8** | Tasks 11–12 (multiple-choice application tasks) |
| **Page 9** | Tasks 13–14 (data/logic/ANO-NE tasks) |
| **Page 10** | Task 15 (matching task — full page) |
| **Page 11** | Task 16 (sequence/pattern task — full page with diagram) |
| **Page 12** | Blank page or continuation |

### 2.3 Cover Page Elements

The first page contains (in order from top to bottom):

1. **Header bar**: Bold title — `MATEMATIKA` — with subtitle `Didaktický test`
2. **Test code**: Machine-readable code, e.g., `M9PAD26C0T01`
3. **Max score badge**: `Maximální bodové hodnocení: 50 bodů`
4. **Time badge**: `Časový limit: 70 minut`
5. **Instructions block**: Numbered list of instructions to students
   - Use blue or black ballpoint pen
   - Write answers in the answer sheet only
   - Notes in the test booklet are not evaluated
   - For tasks requiring procedure, writing only the result = 0 points
   - For construction tasks, trace pencil lines with pen
6. **Formula reference sheet**: A gray-shaded box containing key formulas:
   - Area formulas (rectangle, triangle, trapezoid, circle)
   - Volume formulas (prism, cylinder)
   - Pythagorean theorem
   - Percentage formula

### 2.4 Task Layout Anatomy

Every task follows a consistent visual pattern:

```
┌─────────────────────────────────────────────┐
│  VÝCHOZÍ TEXT / OBRÁZEK K ÚLOZE N           │  ← Gray shaded context box
│  (optional — not all tasks have this)        │     (only tasks 7–16 typically)
│  Context text, tables, diagrams go here      │
└─────────────────────────────────────────────┘

  N                               max. X body   ← Task number (large bold)
  ─────────────────────────────────────────────  ← Thick horizontal rule
  
  Main instruction text (what to do)
  
  N.1  Subtask instruction / question
       [math expression if needed]
  
  N.2  Another subtask instruction
       [math expression if needed]
  
  N.3  Yet another subtask
       [math expression if needed]
  
  A) option  B) option  C) option  D) option  E) option   ← MC options (if applicable)
```

### 2.5 Visual Design Tokens

| Element | Style |
|---|---|
| Task number | ~18–20 pt, bold, left-aligned |
| Points label | ~10 pt, bold, right-aligned on same line: `max. X body/bodů` |
| Horizontal rule | 1–1.5 pt solid black line, full width |
| Context box | Light gray background (#F0F0F0), thin gray border, 0 border-radius |
| Context box title | Bold, uppercase: `VÝCHOZÍ TEXT K ÚLOZE N` or `VÝCHOZÍ TEXT A OBRÁZEK K ÚLOZE N` |
| Subtask ID | Bold: `N.1`, `N.2`, etc. |
| MC options | Horizontal row: `A)` through `E)` or `F)`, evenly spaced |
| Math expressions | Inline or display, standard mathematical notation |
| Tables | Simple bordered tables with header row |
| Diagrams | Black-and-white geometric diagrams, TikZ-style precision |
| Page headers | Minimal — test code repeated, page number `X / Y` |
| Page footers | Copyright: `© CZVV` |

---

## 3. Task Taxonomy — The 16-Slot System

CERMAT tests follow a remarkably stable slot system. While the specific
content changes each year, the **position and type** of each task is
predictable. This is the core pattern we exploit for generation.

### 3.1 Complete Task Map

| Slot | Topic | Type | Points | Subtasks | Requires Procedure | Context Box |
|------|-------|------|--------|----------|-------------------|-------------|
| **1** | Arithmetic / number operations | Open (result only) | 2 | 2 | No | No |
| **2** | Fractions / decimals / powers | Open (result only) | 2 | 2 | No | No |
| **3** | Algebraic expressions | Open (with procedure) | 3 | 2–3 | **Yes** | No |
| **4** | Linear equations | Open (with procedure) | 3 | 1–2 | **Yes** | No |
| **5** | Word problem (equation modeling) | Open (with procedure) | 3–4 | 1–2 | **Yes** | Sometimes |
| **6** | Planimetry (2D geometry calculation) | Open (with procedure) | 3–4 | 2–3 | **Yes** | Yes (diagram) |
| **7** | Construction — triangle | Open (construction) | 3 | 1–2 | **Yes** (drawing) | Yes (instructions) |
| **8** | Construction — circle/locus | Open (construction) | 3 | 1–2 | **Yes** (drawing) | Yes (instructions) |
| **9** | Stereometry (3D geometry) | Open (with procedure) | 3–4 | 2–3 | **Yes** | Yes (3D figure) |
| **10** | Units / conversions / proportions | Open (result only) | 2–3 | 2–3 | No | Sometimes |
| **11** | Algebraic modeling (MC) | Closed (A–E) | 2 | 1 | No | Yes (word context) |
| **12** | Angle/geometry reasoning (MC) | Closed (A–E) | 2 | 1 | No | Yes (diagram) |
| **13** | Application / percent / ratio (MC) | Closed (A–E) | 2 | 1 | No | Yes (context) |
| **14** | Data / logic (ANO/NE) | Closed (true/false) | 2–3 | 3–4 | No | Yes (table/graph) |
| **15** | Matching / assignment | Closed (match to A–F) | 4–6 | 3–4 | No | Yes (context) |
| **16** | Sequences / patterns | Open (result only) | 3–4 | 3 | No | Yes (diagram) |

### 3.2 Point Distribution Pattern

Consistent across years:

| Category | Tasks | Typical Points |
|---|---|---|
| Number & variable (Číslo a proměnná) | 1, 2, 3, 4 | ~10 pts |
| Word problems / modeling | 5, 11 | ~5–6 pts |
| Geometry — computation | 6, 9, 12 | ~8–10 pts |
| Geometry — construction | 7, 8 | ~6 pts |
| Units / proportions | 10 | ~2–3 pts |
| Data, logic, matching | 13, 14, 15 | ~7–11 pts |
| Patterns / sequences | 16 | ~3–4 pts |
| **Total** | **16 tasks** | **50 pts** |

### 3.3 Difficulty Gradient

The test is designed with a deliberate difficulty curve:

- **Tasks 1–2**: Easy warmup (≥80% students solve correctly)
- **Tasks 3–5**: Medium (60–75% success rate)
- **Tasks 6–10**: Medium-hard (40–60% success rate)
- **Tasks 11–13**: Medium — MC format makes them accessible (55–70%)
- **Tasks 14–16**: Varies — ANO/NE and matching can be tricky (35–55%)
- **Construction tasks (7, 8)**: Often the hardest for students (~30–50%)

---

## 4. Detailed Task Specifications (For Content Generation)

### Task 1 — Arithmetic

**What it tests**: Order of operations, powers of 10, integer arithmetic

**Pattern**: Two independent calculation subtasks, each worth 1 point.

**Typical template**:
```
1.1  Compute: [expression with ×, ÷, +, -, powers of 10]
1.2  Compute and write as a single number: [expression]
```

**Number ranges**: Results are integers or simple decimals. Expressions
use numbers ≤10000, powers of 10 up to 10³.

**Common traps**: Order of operations, negative results, division as `:`

**Generation rules**:
- Always 2 subtasks, each 1 point
- Result must be a "clean" number (integer or one decimal place)
- Use `:` for division (Czech convention), `·` for multiplication
- Difficulty: one subtask easy, one slightly harder

---

### Task 2 — Fractions

**What it tests**: Operations with fractions, mixed numbers, decimal-fraction conversion

**Pattern**: Two calculation subtasks with fractions.

**Typical template**:
```
2.1  Compute: [fraction expression — addition/subtraction]
2.2  Compute: [fraction expression — multiplication/division or compound]
```

**Generation rules**:
- Results are simplified fractions or integers
- Denominators ≤ 20 (rarely > 12)
- May combine fractions with decimals or powers
- One subtask should test different operations than the other

---

### Task 3 — Algebraic Expressions

**What it tests**: Simplification, factoring, expanding brackets, algebraic identities

**Pattern**: 2–3 subtasks requiring full written procedure.

**Typical template**:
```
3.1  Simplify: [algebraic expression]
3.2  Factor: [expression using (a±b)² or a²-b²]
3.3  (optional) Simplify the rational expression: [fraction with variables]
```

**Generation rules**:
- **Procedure required** — this is explicitly stated
- Uses variables: a, b, x, y (standard letters)
- Identities tested: (a+b)², (a-b)², a²-b² = (a+b)(a-b), (a+b)(a-b)
- Coefficients ≤ 10, exponents ≤ 3
- Result must be verifiably correct

---

### Task 4 — Linear Equations

**What it tests**: Solving linear equations, sometimes systems of 2 equations

**Pattern**: 1–2 equations to solve with full procedure.

**Typical template**:
```
4.1  Solve: [linear equation with fractions or nested brackets]
4.2  (optional) Solve the system: { eq1, eq2 }
```

**Generation rules**:
- **Procedure required**
- Solutions are integers or simple fractions
- Equations may have fractions, nested brackets
- If system: 2 equations, 2 unknowns, unique solution
- Common format: `3(2x - 1) + 4 = 5x - 2(x + 3)`

---

### Task 5 — Word Problem

**What it tests**: Translating real-world scenarios into equations

**Pattern**: One word problem requiring equation setup and solution.

**Typical themes**:
- Motion (meeting, overtaking): `d = v · t`
- Shared work: `1/t₁ + 1/t₂ = 1/t`
- Mixtures / concentrations
- Age problems
- Shopping / pricing with percentages

**Generation rules**:
- **Procedure required** (equation setup + solution)
- Context must be realistic and unambiguous
- Numbers should be "nice" — solutions are integers or simple fractions
- Usually 3–4 points, may have subtasks like "set up the equation" + "solve"

---

### Task 6 — Planimetry (2D Geometry)

**What it tests**: Area, perimeter, angles of composite 2D shapes

**Pattern**: Diagram given in context box, 2–3 calculation subtasks.

**Typical shapes**: Compound figures made from rectangles, triangles,
trapezoids, circles/semicircles. Often involves Pythagorean theorem.

**Generation rules**:
- **Procedure required**
- Context box with "VÝCHOZÍ TEXT A OBRÁZEK K ÚLOZE 6"
- TikZ diagram showing the geometric figure with labeled dimensions
- Dimensions are integers or simple values that lead to clean results
- Subtasks: "Calculate perimeter", "Calculate area", "Find angle"

---

### Tasks 7 & 8 — Geometric Construction

**What it tests**: Ruler-and-compass construction, locus of points

**Task 7 — Triangle construction**:
- Given: combination of sides, angles, heights, medians
- "Construct triangle ABC where..."
- Often includes: "Calculate the area of the triangle"

**Task 8 — Circle/locus construction**:
- Find points satisfying distance conditions
- Construct tangent lines, inscribed/circumscribed circles
- Thales' theorem applications

**Generation rules**:
- Context box with construction instructions
- A blank space (or grid) is provided for drawing
- The construction must be geometrically feasible and unique (or finite solutions)
- Solution includes description of construction steps

---

### Task 9 — Stereometry (3D Geometry)

**What it tests**: Volume, surface area of 3D solids

**Typical solids**: Cube, rectangular prism (kvádr), cylinder, prism,
pyramid, combinations

**Pattern**: Full-page task with 3D figure in context box, 2–3 subtasks.

**Generation rules**:
- **Procedure required**
- Context box with "VÝCHOZÍ TEXT A OBRÁZEK K ÚLOZE 9"
- 3D diagram (isometric or perspective sketch)
- Subtasks: "Calculate volume", "Calculate surface area", "Find diagonal"
- Dimensions chosen so results are integers or contain π

---

### Task 10 — Units / Proportions

**What it tests**: Unit conversion, proportional reasoning, percentages

**Pattern**: 2–3 independent subtasks.

**Typical templates**:
```
10.1  Convert 2.5 km² to m²
10.2  A map has scale 1:50000. A distance of 3 cm on the map represents ? km
10.3  What is 15% of 240?
```

**Generation rules**:
- Result-only (no procedure)
- Units: length, area, volume, time, speed
- Scale/map problems are common
- Percentage calculations
- 2–3 points total

---

### Task 11 — Algebraic Modeling (Multiple Choice)

**What it tests**: Translating a word scenario into an algebraic expression

**Pattern**: Context box describes a real-world scenario with a variable.
Student selects which expression (A–E) correctly models the situation.

**Generation rules**:
- Context box with "VÝCHOZÍ TEXT K ÚLOZE 11"
- Defines a variable (e.g., "the price of a notebook is *s* Kč")
- Question: "Which expression represents [total/difference/etc.]?"
- **5 options (A–E)**, exactly 1 correct
- Distractors should be plausible (common algebraic mistakes)
- 2 points

---

### Task 12 — Geometry/Angle Reasoning (Multiple Choice)

**What it tests**: Angle relationships, properties of shapes

**Pattern**: Context box with geometric diagram. Student selects correct
angle measure or geometric relationship from options.

**Generation rules**:
- Context box with diagram
- Tests: supplementary/complementary angles, triangle angle sum,
  parallel lines + transversal, inscribed angles, isosceles properties
- 5 options (A–E)
- 2 points

---

### Task 13 — Application MC

**What it tests**: Practical math application (percentages, ratios, etc.)

**Pattern**: Real-world context, single MC question.

**Typical themes**: Discount calculation, interest, mixture, speed comparison

---

### Task 14 — Data & Logic (ANO/NE)

**What it tests**: Interpreting data from tables/graphs, logical reasoning

**Pattern**: Context box contains a data table or graph. 3–4 statements
to evaluate as true (ANO) or false (NE).

**Generation rules**:
- Context box: "VÝCHOZÍ TEXT A TABULKA/GRAF K ÚLOZE 14"
- Table with 4–6 data points or a bar/line graph
- 3–4 statements (14.1, 14.2, 14.3, 14.4)
- Each statement: ANO or NE
- Mix: some obviously true, some require calculation, some are traps
- 1 point per correct statement

---

### Task 15 — Matching

**What it tests**: Matching expressions/values to correct results

**Pattern**: Context box, 3–4 items to match with 5–6 answer options.

**Generation rules**:
- "Přiřaďte ke každé úloze (15.1–15.3) odpovídající výsledek (A–F)"
- 3–4 matching items, 5–6 options (more options than items = distractors)
- Topics: percentage calculations, expression evaluation, unit conversions
- Each correct match: 2 points (total: 4–6)

---

### Task 16 — Sequences & Patterns

**What it tests**: Recognizing and extending number/geometric patterns

**Pattern**: Context box describes a visual pattern (often with
small squares/tiles), shows first 3–4 terms. Student must find n-th term
and/or figure out which term has a given value.

**Typical subtasks**:
```
16.1  How many squares in the 5th figure?     (direct computation)
16.2  How many squares in the 15th figure?    (general formula needed)
16.3  Which figure has exactly 82 squares?    (inverse — solve for n)
```

**Generation rules**:
- Context box with "VÝCHOZÍ TEXT A OBRÁZEK K ÚLOZE 16"
- TikZ diagram showing 3 figures in the sequence
- Pattern is always linear (arithmetic sequence): `a_n = a₁ + (n-1)·d`
- Start value and common difference are small positive integers
- 3 subtasks, 3–4 points total

---

## 5. Answer Format Types

The test uses 4 distinct answer formats. Our generator must produce
tasks that match these exactly:

### 5.1 Open — Result Only (Úloha s výsledkem)

- Student writes just the final number/expression
- No partial credit for procedure
- Used in: Tasks 1, 2, 10, 16

### 5.2 Open — With Procedure (Úloha s postupem)

- Student must write the complete solution procedure
- Writing **only the result = 0 points** even if correct
- Partial credit possible (e.g., correct setup but arithmetic error)
- Used in: Tasks 3, 4, 5, 6, 7, 8, 9

### 5.3 Closed — Multiple Choice (Uzavřená úloha)

- 5 options labeled A–E (sometimes A–F)
- Exactly 1 correct answer
- Used in: Tasks 11, 12, 13

### 5.4 Closed — True/False (ANO/NE)

- Series of statements to evaluate
- Binary: ANO (true) or NE (false)
- Used in: Task 14

### 5.5 Closed — Matching (Přiřazovací)

- Match items (N.1, N.2, ...) to options (A, B, C, ...)
- More options than items (distractors)
- Used in: Task 15

---

## 6. Content Generation Strategy

### 6.1 Architecture Overview

```
┌──────────────────────────────────────────────────────┐
│                  Test Orchestrator                     │
│  (assembles 16 tasks, validates point totals,         │
│   ensures topic coverage and difficulty balance)      │
└────────────────────────┬─────────────────────────────┘
                         │
          ┌──────────────┼──────────────────┐
          ▼              ▼                  ▼
   ┌──────────┐   ┌──────────┐      ┌──────────┐
   │ Task Gen │   │ Task Gen │ ...  │ Task Gen │
   │  Slot 1  │   │  Slot 2  │      │  Slot 16 │
   └────┬─────┘   └────┬─────┘      └────┬─────┘
        │               │                 │
        ▼               ▼                 ▼
   ┌──────────────────────────────────────────┐
   │         LaTeX Renderer (PDF output)       │
   │  - Applies CERMAT visual template         │
   │  - Generates cover page                   │
   │  - Assembles multi-page document          │
   │  - Produces per-task answer key PDF       │
   └──────────────────────────────────────────┘
```

### 6.2 Per-Task Generator Design

Each task slot has a dedicated generator that:

1. **Accepts a seed** for deterministic reproducibility
2. **Generates random parameters** within validated ranges
3. **Computes the correct answer** symbolically (no hallucination risk)
4. **Validates** that the answer is "clean" (integer, simple fraction, etc.)
5. **Produces structured output**: task text, math expressions, diagram code, answer key
6. **Retries** if generated parameters lead to degenerate cases

### 6.3 Mathematical Correctness — The #1 Priority

> **Every generated task must be mathematically verifiable.**

This means:
- Arithmetic tasks: compute answer with Python/SymPy, verify
- Equation tasks: substitute solution back into equation
- Geometry tasks: compute with exact formulas, cross-check
- MC distractors: verify they are **wrong** (common student mistakes)
- ANO/NE statements: verify each one independently

**No LLM should generate mathematical content directly.** LLMs generate
the *textual wrapper* (word problem scenarios, context descriptions), but
all numbers, equations, and answers are computed deterministically.

### 6.4 AI Workflow for Word Problem Generation

For tasks that need natural-language context (tasks 5, 11, 14, 15):

```
Step 1: Template Selection
  - Pick a scenario archetype (motion, shopping, age, mixture, etc.)
  - Select from a curated pool of ~50 templates per task type

Step 2: Parameter Injection
  - Fill template with random but validated numbers
  - Compute correct answer
  - Verify answer is "student-friendly" (clean numbers)

Step 3: (Optional) LLM Polish
  - Send template-filled text to LLM for Czech language polishing
  - Constrain: "Do not change any numbers or mathematical relationships"
  - Validate: extract numbers from polished text, compare to originals

Step 4: Distractor Generation (for MC)
  - Generate 4 wrong answers based on common mistakes:
    - Sign error, operation swap, forgotten conversion, off-by-one
  - Verify none of the distractors accidentally equal the correct answer
```

### 6.5 Ensuring 15-Test Coverage

If a student takes 15 practice tests, we need **240 unique tasks** (15 × 16).
For each slot, this means ~15 distinct variants. Strategy:

| Slot | Variant Strategy | Pool Size Needed |
|------|-----------------|-----------------|
| 1 (arithmetic) | Random parameter generation — infinite variants | ∞ |
| 2 (fractions) | Random parameter generation — infinite variants | ∞ |
| 3 (algebra) | Template pool × random coefficients | ~30 templates |
| 4 (equations) | Template pool × random coefficients | ~20 templates |
| 5 (word problems) | Scenario pool × parameter randomization | ~50 scenarios |
| 6 (planimetry) | Shape pool × dimension randomization | ~20 shapes |
| 7 (construction) | Construction type pool | ~15 types |
| 8 (construction) | Construction type pool | ~15 types |
| 9 (stereometry) | Solid pool × dimension randomization | ~15 solids |
| 10 (units) | Conversion type pool × random values | ~30 templates |
| 11 (MC modeling) | Scenario pool × variable randomization | ~30 scenarios |
| 12 (MC angles) | Diagram pool × angle randomization | ~20 diagrams |
| 13 (MC application) | Scenario pool | ~25 scenarios |
| 14 (ANO/NE data) | Table/graph generation + statement pool | ~40 datasets |
| 15 (matching) | Topic pool × value randomization | ~25 topics |
| 16 (sequences) | Pattern type × parameter randomization | ~20 patterns |

---

## 7. Visual Fidelity — Pixel-Perfect PDF Generation

### 7.1 Rendering Technology

**Recommended approach: LaTeX to PDF**

Why LaTeX:
- Precise typographic control matching CERMAT's professional typesetting
- Native mathematical formula rendering
- TikZ for geometric diagrams (same technology CERMAT likely uses)
- Reproducible output across platforms
- Full control over every spacing, font size, and layout detail

Alternative considered: **Typst** — newer, faster, but less proven for
this exact use case. Could be explored later.

### 7.2 CERMAT LaTeX Template Specification

```latex
% === DOCUMENT CLASS & GEOMETRY ===
\documentclass[11pt,a4paper]{article}
\usepackage[
    top=15mm,
    bottom=20mm,
    left=20mm,
    right=20mm
]{geometry}

% === FONTS ===
% CERMAT uses a sans-serif font similar to Arial
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[czech]{babel}

% === MATH ===
\usepackage{amsmath,amssymb}

% === GRAPHICS ===
\usepackage{tikz}
\usetikzlibrary{calc,patterns,angles,quotes,arrows.meta}
\usepackage{pgfplots}

% === TABLES ===
\usepackage{array,tabularx,booktabs}

% === BOXES ===
\usepackage{tcolorbox}

% === CERMAT DESIGN TOKENS ===
\definecolor{cermatgray}{RGB}{240,240,240}    % Context box background
\definecolor{cermatborder}{RGB}{180,180,180}   % Context box border
\definecolor{cermatblack}{RGB}{0,0,0}          % Text and rules

% === CONTEXT BOX ===
\newtcolorbox{contextbox}{
    colback=cermatgray,
    colframe=cermatborder,
    arc=0mm,           % Sharp corners (CERMAT uses no rounding)
    boxrule=0.6pt,
    left=4mm,
    right=4mm,
    top=3mm,
    bottom=3mm,
    fontupper=\small\sffamily
}

% === TASK HEADER MACRO ===
\newcommand{\taskheader}[2]{%  #1=number, #2=points
    \noindent{\Large\bfseries #1}\hfill{\bfseries max. #2}\\[1mm]
    \noindent\rule{\textwidth}{1.2pt}\\[3mm]
}

% === SUBTASK MACRO ===
\newcommand{\subtask}[2]{%  #1=id (e.g., 1.1), #2=instruction
    \noindent\textbf{#1}\quad #2\\[2mm]
}
```

### 7.3 Fidelity Benchmarking Pipeline

To achieve pixel-perfect output, we need an automated comparison pipeline:

```
1. REFERENCE EXTRACTION
   ┌─────────────────┐
   │ Reference PDF    │──> PyMuPDF crop per-task regions ──> reference_crops/
   │ (2024/2025/2026) │    at 200–300 DPI                     task_01/*.png
   └─────────────────┘                                        task_02/*.png
                                                               ...

2. SYNTHETIC GENERATION
   ┌─────────────────┐
   │ Engine generates │──> LaTeX → pdflatex → PDF ──> crop same regions ──> gen_crops/
   │ task N           │                                                       task_N/*.png
   └─────────────────┘

3. COMPARISON
   ┌──────────────┐     ┌──────────────┐
   │ reference    │     │ generated    │
   │ task_01.png  │────>│ task_01.png  │──> SSIM score, pixel diff map
   └──────────────┘     └──────────────┘

4. HUMAN BLIND TEST
   Shuffle real + generated crops, display side by side.
   If humans can't tell them apart → PASS.
```

The existing `scripts/benchmark_fidelity.py` already implements parts of
this pipeline. It needs to be extended with:
- SSIM (structural similarity) automated scoring
- Per-element comparison (task header, subtask formatting, math rendering)
- Regression tracking across engine iterations

### 7.4 Key Visual Details to Get Right

Based on analysis of reference PDFs, these details matter most:

1. **Task number size**: Must be significantly larger than body text (~18–20pt vs 11pt)
2. **Horizontal rule**: Exactly the right thickness (1–1.2pt) and spacing
3. **Context box**: Light gray, square corners, specific padding
4. **Subtask indentation**: Consistent left margin after the ID
5. **Math formula spacing**: Display vs inline, proper centering
6. **MC option layout**: Evenly distributed across the page width
7. **Table borders**: Thin, consistent, with header row distinction
8. **Diagram precision**: Clean lines, proper labels, correct scale
9. **Spacing between tasks**: Consistent vertical gaps
10. **Font**: Sans-serif matching Arial/Helvetica closely

---

## 8. Answer Key (Klíč) Generation

Every real CERMAT test comes with a separate **klíč správných řešení** (answer key PDF).

### 8.1 Answer Key Structure

The answer key PDF contains:
- Test identification code
- For each task:
  - Task number
  - Correct answer(s)
  - Point allocation per subtask
  - For "procedure" tasks: model solution steps
  - For MC: the correct letter
  - For ANO/NE: the correct sequence (e.g., ANO, NE, ANO)
  - For matching: the correct mapping (e.g., 15.1→C, 15.2→E, 15.3→A)

### 8.2 Our Answer Key Must Include

For training purposes, our answer keys should be **richer** than CERMAT's:
- Correct answer
- Full step-by-step solution
- Common mistakes to avoid
- Points breakdown
- Difficulty rating (optional, for student analytics)

---

## 9. Czech Language Conventions

CERMAT tests use specific Czech mathematical conventions:

| Concept | Czech Convention | Example |
|---|---|---|
| Division | `:` (colon) | `600 : 10` not `600 / 10` |
| Multiplication | `·` (middle dot) | `3 · 5` not `3 × 5` |
| Decimal separator | `,` (comma) | `3,14` not `3.14` |
| Thousands separator | space | `1 000 000` not `1,000,000` |
| Interval | `⟨a; b⟩` | `⟨0; 5⟩` not `[0, 5]` |
| Percent | `%` after space | `15 %` |
| Currency | `Kč` | `500 Kč` or `500,- Kč` |
| Angle | `∠ABC` or `α` | standard |
| Triangle | `△ABC` | standard |
| Area | `S` | not `A` |
| Perimeter | `o` | not `P` |
| Volume | `V` | standard |
| Surface area | `S_p` (povrch) | |
| Task instruction | `Vypočtěte:` | "Calculate:" |
| With procedure | `Zapište celý postup řešení.` | "Write the complete procedure." |
| Points | `body` / `bodů` | grammatical case matters |

### Points Grammar

| Count | Czech |
|---|---|
| 1 | `1 bod` |
| 2–4 | `2 body`, `3 body`, `4 body` |
| 5+ | `5 bodů`, `6 bodů`, ... `50 bodů` |

---

## 10. Implementation Phases

### Phase 1 — Visual Template (Current Priority)

**Goal**: Produce a single PDF that is visually indistinguishable from a real
CERMAT test, using hardcoded content from a real exam.

1. Install LaTeX toolchain (`pdflatex` or `xelatex`)
2. Create the master CERMAT LaTeX template with all design tokens
3. Manually transcribe one real exam into the template
4. Run fidelity benchmark against the reference PDF
5. Iterate on spacing, fonts, sizing until SSIM > 0.95

### Phase 2 — Task Generators (Slots 1–4, 10–12, 16)

**Goal**: Implement deterministic generators for "computational" tasks
that don't need natural language.

These are the easiest to generate because they're pure math:
- Task 1: Arithmetic expressions
- Task 2: Fraction expressions
- Task 3: Algebraic simplification
- Task 4: Equation solving
- Task 10: Unit conversion
- Task 11: MC algebraic modeling
- Task 12: MC angle reasoning
- Task 16: Sequence patterns

### Phase 3 — Geometry Diagrams (Slots 6, 7, 8, 9, 12)

**Goal**: Automated TikZ diagram generation for geometry tasks.

- Planimetry diagrams (composite shapes)
- Construction diagrams (compass-and-ruler style)
- 3D diagrams (isometric views)
- Angle diagrams

### Phase 4 — Natural Language Tasks (Slots 5, 13, 14, 15)

**Goal**: AI-assisted content generation for word problems and data tasks.

- Template-based word problem generation
- Table/graph data generation
- Statement generation for ANO/NE tasks
- LLM polishing pipeline for Czech language quality

### Phase 5 — Full Test Assembly & Quality Assurance

**Goal**: Complete test orchestrator that assembles 16 tasks into a
print-ready PDF with answer key.

- Point total validation (must = 50)
- Difficulty balancing
- Topic coverage verification
- Final fidelity benchmark
- Human blind testing

---

## 11. What We Have vs. What We Need

### Already Built (from codebase analysis)

| Component | Status | Location |
|---|---|---|
| Task data model | Exists | Backend schemas (Pydantic models) |
| Per-task generators (slots 1–6, 10–12, 14–16) | Exists | `backend/app/engines/cermat/tasks/` |
| LaTeX renderer (per-task snapshots) | Exists | `CermatRenderer` class |
| HTML preview renderer | Exists | `CermatRenderer.export_html_preview()` |
| CLI interface | Exists | `scripts/cermat_cli.py` |
| Reference crop extractor | Exists | `scripts/extract_reference_tasks.py` |
| Blind fidelity benchmark | Exists | `scripts/benchmark_fidelity.py` |
| Unit tests | Exists | `backend/tests/test_cermat_engine.py` |

### Still Needed

| Component | Priority | Notes |
|---|---|---|
| Full-test LaTeX template (cover page + multi-page) | HIGH | Current renderer only does per-task snippets |
| PDF compilation pipeline (LaTeX to PDF) | HIGH | Need `pdflatex` or alternative |
| LaTeX toolchain installation | HIGH | Not currently installed on machine |
| Automated SSIM comparison | MEDIUM | Extend benchmark script |
| Answer key PDF generation | MEDIUM | Separate PDF with solutions |
| Task generators for slots 7, 8, 9, 13 | MEDIUM | Construction & stereometry |
| Word problem template pool expansion | LATER | More variety in scenarios |
| LLM polishing pipeline | LATER | Czech text quality improvement |
| Student-facing test delivery system | LATER | Frontend integration |

---

## 12. Risk Assessment

| Risk | Impact | Mitigation |
|---|---|---|
| Mathematical errors in generated tasks | CRITICAL | Symbolic verification with SymPy, automated answer checking |
| Visual mismatch detected by students | MEDIUM | Iterative fidelity benchmarking, human blind tests |
| Czech language errors | MEDIUM | Template-based generation, Czech-native review |
| Difficulty calibration off | MEDIUM | Statistical comparison with real exam pass rates |
| CERMAT changes format significantly | LOW | Format has been stable for 8+ years |
| Copyright concerns | MEDIUM | We generate new content, not copy existing; visual style is functional layout not creative work |

---

## 13. References

| Source | URL | Used For |
|---|---|---|
| CERMAT official | `prijimacky.cermat.cz` | Test PDFs, specifications |
| Reference PDFs (local) | `References/Matematika/` | Visual analysis, task structure |
| To-dáš | `to-das.cz` | Test analysis, task breakdowns |
| Specifikace požadavků | via CERMAT website | Curriculum coverage requirements |
| TAU app | `tau.cermat.cz` | Understanding practice test format |
| Existing engine code | `backend/app/engines/cermat/` | Current implementation state |
| Benchmark scripts | `scripts/` | Fidelity testing infrastructure |
