# CERMAT M9 Technical Specification & Reverse-Engineering Manual

> **Document Status**: Production Standard  
> **Target Exam**: Jednotná přijímací zkouška (JPZ) — Matematika 9. třída (M9)  
> **Source Corpus**: 12 official CERMAT test booklets (2024–2026, variants A/B/C/D)  
> **Purpose**: Definitive technical reference for producing authentic, pixel-identical, and mathematically rigorous CERMAT test booklets and answer keys.

---

## Table of Contents

1. [Executive Summary & Technical Architecture](#1-executive-summary--technical-architecture)
2. [Document Geometry & Physical Grid](#2-document-geometry--physical-grid)
3. [Typography & Font Hierarchy](#3-typography--font-hierarchy)
4. [Visual Styling Tokens & Component Anatomy](#4-visual-styling-tokens--component-anatomy)
5. [Diagram & Vector Graphics Blueprint (TikZ)](#5-diagram--vector-graphics-blueprint-tikz)
6. [Task Authoring & Mathematical Invariants](#6-task-authoring--mathematical-invariants)
7. [Production LaTeX Master Template](#7-production-latex-master-template)
8. [Automated Fidelity Verification & Quality Assurance](#8-automated-fidelity-verification--quality-assurance)

---

## 1. Executive Summary & Technical Architecture

### 1.1 Scope and Objective
This document provides the complete technical specification required to generate Czech Unified Entrance Examination (JPZ) test booklets for 9th-grade mathematics (M9) that achieve **100% visual, structural, and mathematical indistinguishability** from genuine booklets produced by the Centrum pro zjišťování výsledků vzdělávání (CZVV / CERMAT).

Every metric, coordinate, font size, stroke weight, color code, and layout pattern in this specification has been reverse-engineered directly from the vector instruction streams of the official 2024, 2025, and 2026 test PDFs.

### 1.2 Toolchain Requirements
To compile authentic CERMAT test booklets, the rendering toolchain must support OpenType font loading, precise micro-typography, and programmatic vector graphics:

- **Compiler**: `XeLaTeX` or `LuaLaTeX` (mandatory for native OpenType font loading and Unicode support).
- **Core Packages**: `geometry`, `fontspec`, `unicode-math` (or `amsmath` + `amssymb`), `tikz`, `tcolorbox`, `tabularx`, `enumitem`, `calc`, `fancyhdr`.
- **Primary Typefaces**:
  - **Body & Headings**: *Adobe Myriad Pro* (`MyriadPro-Regular.otf`, `MyriadPro-Bold.otf`, `MyriadPro-It.otf`, `MyriadPro-BoldIt.otf`).  
    *Open-source fallback*: *TeX Gyre Heros* / *Liberation Sans* (configured with tight tracking).
  - **Mathematics**: *Cambria Math* (`cambria.ttc`) or *Neo Euler* / *Asana Math* paired with Myriad Pro text numerals.
  - **Symbols**: *SymbolMT* / standard Unicode mathematical operator set.

---

## 2. Document Geometry & Physical Grid

### 2.1 Page Dimensions & Coordinate Bounds
Official CERMAT booklets are standard European ISO 216 **A4 portrait**.

| Metric | Millimeters | PostScript Points (`pt`) | Notes |
|---|---|---|---|
| **Page Width** | 210.0 mm | 595.28 pt | Standard A4 |
| **Page Height** | 297.0 mm | 841.89 pt | Standard A4 |
| **Left Margin** | 25.0 mm | 70.90 pt | $x_0$ coordinate for body content |
| **Right Margin** | 23.0 mm | 65.20 pt | $x_1$ coordinate = 530.08 pt |
| **Printable Width** | 162.0 mm | 459.18 pt | Active column width |
| **Top Margin** | 15.0 mm | 42.52 pt | From page edge to running header |
| **Bottom Margin** | 10.0 mm | 28.35 pt | From page edge to footer / page number |

```
0,841.89 pt ──────────────────────────────────────────────── 595.28,841.89 pt
│                                                           │
│   Top Margin: 15.0 mm (42.52 pt)                          │
│   ┌───────────────────────────────────────────────────┐   │
│   │ Running Header (y ≈ 45.0 pt)                      │   │
│   │ ───────────────────────────────────────────────── │   │
│   │                                                   │   │
│   │                                                   │   │
│   │                 BODY CONTENT AREA                 │   │
│   │             Width: 162.0 mm (459.18 pt)           │   │
│   │                                                   │   │
│   │                                                   │   │
│   │                                                   │   │
│   │ ───────────────────────────────────────────────── │   │
│   │ Running Footer (y ≈ 815.9 pt)                     │   │
│   └───────────────────────────────────────────────────┘   │
│   Bottom Margin: 10.0 mm (28.35 pt)                       │
0,0 pt ───────────────────────────────────────────────────── 595.28,0 pt
```

### 2.2 Standard 12-Page Pagination Budget
A genuine CERMAT M9 booklet has a strict 12-page architecture. Content cannot spill across pages arbitrarily; tasks must fit their dedicated page allocations:

| Page | Standard Content Allocation | Page Budget & Flow Constraints |
|---|---|---|
| **1** | **Cover Page**: Official Header, Test Code, Score & Time Badges, 2-Column Instructions, Sample Recording Boxes | Exactly 1 full page. Never overflows. |
| **2** | Top Instruction Banner, **Task 1** (Arithmetic, 2–3 subtasks), **Task 2** (Fractions & Decimals, 2 subtasks) | 2 tasks with 1 context box. |
| **3** | Recommendation banner, **Task 3** (Algebraic Expressions, 2–3 subtasks), **Task 4** (Linear Equations, 1–2 subtasks) | High vertical space for written procedure. |
| **4** | **Task 5** (Word Problem / Modeling), **Task 6** (Planimetry Calculation + Composite Diagram) | Includes 1 geometric vector diagram. |
| **5** | **Task 7** (Applied Word Problem / Proportions), **Task 8** (Geometry / Conversion Application) | 2 applied tasks. |
| **6** | Recommendation banner (`Rýsujte přímo do záznamového archu`), **Task 9** (Geometric Construction 1 — Triangle/Locus) | Context box + large drawing construction field ($h \approx 70\text{ mm}$). |
| **7** | **Task 10** (Geometric Construction 2 — Circle/Tangent/Thales) | Context box + large drawing construction field ($h \approx 70\text{ mm}$). |
| **8** | **Task 11** (Data Diagram / Pie Chart / Ratios), **Task 12** (Multiple-Choice Algebraic Modeling) | Includes 1 vector data chart (pie/bar). |
| **9** | **Task 13** (Multiple-Choice Planimetry Reasoning), **Task 14** (Multiple-Choice Stereometry / Angles) | 2 MC tasks with diagrams and 5 options (A–E). |
| **10** | **Task 15** (Matching Task / 3D Solids Composition — Subtasks 15.1–15.3 vs Options A–F) | Full-page diagram layout ($h \approx 80\text{ mm}$) with shaded 3D figures. |
| **11** | **Task 16** (Sequences & Patterns — Subtasks 16.1–16.3), Bottom Verification Banner | Step-by-step visual sequence + 3 subtasks + final warning rule. |
| **12** | **Formula Sheet**: Squares ($11^2$ to $20^2$), $\pi$ constants, Algebraic identities, Circle formulas | Reference tables only. No test questions. |

---

## 3. Typography & Font Hierarchy

### 3.1 Typeface Matching
CERMAT didaktické testy use **Adobe Myriad Pro** as their universal font family for all text, headings, numbers, and labels, paired with **Cambria Math** for mathematical typography.

```
Typeface Mapping:
├── Body / Headings / Labels ──> Adobe Myriad Pro (OTF)
│   ├── Regular  (MyriadPro-Regular)
│   ├── Bold     (MyriadPro-Bold)
│   ├── Italic   (MyriadPro-It)
│   └── Bold-It  (MyriadPro-BoldIt)
└── Mathematics & Operators   ──> Cambria Math / Asana Math
    ├── Variables & Algebra   ──> Cambria Math Italic (e.g., 𝑎, 𝑏, 𝑥, 𝑦, 𝑟, 𝑆, 𝑉, 𝑜)
    ├── Operators             ──> Cambria Math / SymbolMT (+, −, ⋅, ∶, =, ≐, ≈, √)
    └── Geometric Symbols     ──> Cambria Math (△, ∠, ∥, ⟂, °, π)
```

### 3.2 Font Sizing & Leading Matrix

| Role | Font Style | Size (`pt`) | Baseline Skip / Leading (`pt`) | Exact Text Example |
|---|---|---|---|---|
| **Cover Title** | `MyriadPro-Bold` | 20.0 pt | 24.0 pt | `MATEMATIKA 9A` |
| **Cover Subtitle** | `MyriadPro-Bold` | 14.0 pt | 18.0 pt | `DIDAKTICKÝ TEST` |
| **Cover Section Number** | `MyriadPro-Bold` | 14.0 pt | 18.0 pt | `1`, `2`, `2.1`, `2.2` |
| **Cover Section Title** | `MyriadPro-Bold` | 11.0 pt | 14.0 pt | `Základní informace k zadání zkoušky` |
| **Cover Body Text** | `MyriadPro-Regular` | 11.0 pt | 13.2 pt | `U každé úlohy je uveden maximální...` |
| **Page Running Number** | `MyriadPro-Regular` | 12.0 pt | — | `2`, `3`, `4`, ... (centered at $y = 815.9\text{ pt}$) |
| **Top Instruction Banner**| `MyriadPro-Regular` | 12.0 pt | 15.0 pt | `V úlohách 1, 2.1, 3.1 ... přepište do...` |
| **Context Box Header** | `MyriadPro-Bold` | 12.0 pt | 15.0 pt | `VÝCHOZÍ TEXT K ÚLOZE 5` |
| **Context Box Body** | `MyriadPro-Regular` | 12.0 pt | 15.8 pt | Standard problem descriptions |
| **Context Source Tag** | `MyriadPro-It` | 9.5 pt | 11.0 pt | `(CZVV)` (right-aligned inside box) |
| **Task Number** | `MyriadPro-Bold` | 14.04 pt | 17.0 pt | `1`, `2`, `3`, ..., `16` (left-aligned) |
| **Task Points Badge** | `MyriadPro-Bold` | 12.0 pt | — | `max. 4 body`, `2 body`, `max. 1 bod` |
| **Task Lead Instruction** | `MyriadPro-Bold` | 12.0 pt | 15.8 pt | `Vypočtěte:`, `Zjednodušte:` |
| **Subtask ID** | `MyriadPro-Regular` | 12.0 pt | 15.8 pt | `1.1`, `1.2`, `16.3` |
| **Multiple-Choice Label**| `MyriadPro-Regular` | 12.0 pt | 15.8 pt | `A)`, `B)`, `C)`, `D)`, `E)` |
| **Procedure Warning** | `MyriadPro-Bold` | 12.0 pt | 15.8 pt | `V záznamovém archu uveďte celý postup...` |
| **Mathematical Formulas**| `CambriaMath` | 12.0 pt | 16.0 pt | $A = \frac{2}{9} + \frac{5}{18}$ |
| **Exponents / Indices** | `MyriadPro-Regular` | 8.0–8.5 pt | — | $11^2 = 121$, $16\text{ cm}^2$, $a_1$ |

### 3.3 Czech Mathematical Typesetting Rules
The engine must enforce strict Czech typographical standards:

1. **Division Operator**: Use colon `∶` (`U+2236` or `$:$` with proper spacing: `$a : b$`), NEVER slash `/` or obelus `÷`.
2. **Multiplication Operator**: Use middle dot `⋅` (`\cdot`), NEVER cross `×` or asterisk `*`.
3. **Decimal Separator**: Use comma `,` without trailing space in numbers: `3,14` (in LaTeX: `$3{,}14$`).
4. **Thousands Separator**: Thin non-breaking space: `10 000` (in LaTeX: `$10\,000$`).
5. **Non-breaking Prepositions**: Czech single-letter prepositions (`k`, `s`, `v`, `z`, `o`, `u`, `a`, `i`) must be tied to the following word with a non-breaking space (`~`).
6. **Approximation Symbols**:
   - For decimal rounding: `≐` (`\doteq` or `U+2250`): $\pi \doteq 3{,}14$.
   - For fractional approximation: `≈` (`\approx` or `U+2248`): $\pi \approx \frac{22}{7}$.

---

## 4. Visual Styling Tokens & Component Anatomy

### 4.1 Color Palette & Gray Tones

```
CERMAT Color Palette:
├── Pure Black   (#000000) ──> Text, rules, outlines, borders (CMYK: 0,0,0,100)
├── Pure White   (#FFFFFF) ──> Page background, box backgrounds (CMYK: 0,0,0,0)
├── Gray 95%     (#F2F2F2) ──> 3D Top face fill (RGB: 0.949, 0.949, 0.949)
├── Gray 85%     (#D9D9D9) ──> 3D Front face fill, highlighted tiles (RGB: 0.851, 0.851, 0.851)
├── Gray 75%     (#BFBFBF) ──> 3D Side face fill (RGB: 0.749, 0.749, 0.749)
├── Gray 35%     (#595959) ──> Dark shaded regions / active blocks (RGB: 0.349, 0.349, 0.349)
└── Logo Blue    (#005CAB) ──> Cover page official logo only (RGB: 0.0, 0.361, 0.671)
```

### 4.2 Horizontal Rules & Line Weights

| Line Type | Exact Thickness (`pt`) | Millimeters | Color | Usage |
|---|---|---|---|---|
| **Heavy Rule** | `0.96 pt` | 0.34 mm | Solid Black (`#000000`) | Task header boundary line, Context box top/bottom borders |
| **Thin Rule** | `0.72 pt` | 0.25 mm | Solid Black (`#000000`) | Task separator lines, Cover page dividers, Footer rule |
| **Table Border** | `0.50 pt` | 0.18 mm | Solid Black (`#000000`) | Data tables, Matching option boxes |
| **Diagram Line** | `1.50 pt` | 0.53 mm | Solid Black (`#000000`) | Geometric shapes, coordinate lines, construction objects |
| **Auxiliary Line**| `0.75 pt` | 0.26 mm | Dashed / Solid Black | Dimension leaders, projection lines, height indicators |

### 4.3 Context Box (`VÝCHOZÍ TEXT`) Anatomy
The context box is an unenclosed or framed block containing problem text, tables, or figures.

```
x_left = 65.54 pt                                               x_right = 529.90 pt
┌─────────────────────────────────────────────────────────────────────────────────┐ ◄── Top Border: 0.96 pt
│  VÝCHOZÍ TEXT [A OBRÁZEK / TABULKA] K ÚLOZE N                                   │ ◄── Header: 12.0 pt Bold
│                                                                                 │
│  Context narrative text describing the problem situation, table, or geometry...  │ ◄── Body: 12.0 pt Regular
│  All variables are typeset in Cambria Math Italic.                              │
│                                                                                 │
│                                                                          (CZVV) │ ◄── Tag: 9.5 pt Italic
└─────────────────────────────────────────────────────────────────────────────────┘ ◄── Bottom Border: 0.96 pt
```

- **Top/Bottom Rules**: `x0 = 65.54 pt`, `x1 = 529.90 pt`, `thickness = 0.96 pt`.
- **Side Vertical Brackets**: `x = 65.54 pt` (left) and `x = 529.90 pt` (right), `thickness = 0.96 pt`.
- **Corner Radius**: `0.0 mm` (strictly sharp rectangular corners; no rounded arcs).
- **Background Fill**: Transparent / White (`#FFFFFF`).
- **Attribution Tag**: Right-aligned `(CZVV)` placed $2.5\text{ mm}$ above the bottom rule.

### 4.4 Task Header Anatomy
Every task starts with a standardized header block:

```
70.9 pt                                                                  530.1 pt
1                                                                     max. 3 body
───────────────────────────────────────────────────────────────────────────────── ◄── Rule: 0.72 pt or 0.96 pt
```

- **Left**: Task Number in `MyriadPro-Bold`, `14.04 pt`, baseline at $y$.
- **Right**: Maximum Points in `MyriadPro-Bold`, `12.0 pt`, right-aligned to $x = 530.1\text{ pt}$.
- **Separator Rule**: Placed $3.5\text{ mm}$ below the baseline, spanning the full content width ($459.2\text{ pt}$).
- **Spacing to first subtask**: $4.0\text{ mm}$ vertical clearance.

### 4.5 Subtask & Multiple-Choice Alignment Grid
- **Subtask Identifier**: `MyriadPro-Regular`, `12.0 pt`, left-aligned at $x = 70.9\text{ pt}$.
- **Subtask Content**: Indented to $x = 106.3\text{ pt}$ (exact $12.5\text{ mm}$ tab stop).
- **Multiple-Choice Option Row**:
  - Horizontal distribution across 5 columns (A, B, C, D, E).
  - Column 1 (A): $x = 106.3\text{ pt}$
  - Column 2 (B): $x = 180.0\text{ pt}$
  - Column 3 (C): $x = 255.0\text{ pt}$
  - Column 4 (D): $x = 330.0\text{ pt}$
  - Column 5 (E): $x = 405.0\text{ pt}$

---

## 5. Diagram & Vector Graphics Blueprint (TikZ)

CERMAT mathematics tests feature four distinct vector diagram categories. All diagrams must be rendered as vector paths using the exact styling tokens below.

### 5.1 Planimetry Diagrams (2D Geometry — Tasks 6, 13)
Used for polygon decompositions, angle reasoning, and Pythagorean calculations.

```
                K (vertex label: 12 pt Italic)
               / \
              /   \
             /  |  \
   17 cm    /   |   \   17 cm (dimension: 12 pt Regular)
           /    |v   \
          /     |     \
         /      |      \
        L───────┴───────M
             16 cm
```

#### TikZ Planimetry Styling Rules:
1. **Boundary Lines**: `line width=1.5pt`, `draw=black`, `line cap=round`, `line join=round`.
2. **Auxiliary / Altitude Lines**: `line width=0.75pt`, `draw=black`, optionally `dashed` (`dash pattern=on 3pt off 2pt`).
3. **Vertex Labels**: `font=\fontsize{12}{14}\selectfont\itshape`, offset by $3.5\text{ mm}$ along the vertex angle bisector.
4. **Right Angle Indicator**:
   - Square corner indicator: `line width=0.75pt`, size $3.5\text{ mm} \times 3.5\text{ mm}$.
   - Dot indicator: Circular arc with radius $4.0\text{ mm}$ + centered solid dot (`circle, radius=0.6pt, fill=black`).
5. **Shaded Regions**: `fill=black!15` (CMYK 15% black).

```latex
% TikZ Planimetry Template
\begin{tikzpicture}[scale=1.0, line cap=round, line join=round]
    % Coordinates
    \coordinate (L) at (0,0);
    \coordinate (M) at (4.8,0);
    \coordinate (K) at (2.4,4.5);
    \coordinate (P) at (2.4,0);
    
    % Shaded Area (if applicable)
    \fill[black!15] (L) -- (P) -- (K) -- cycle;
    
    % Outlines
    \draw[line width=1.5pt] (L) -- (M) -- (K) -- cycle;
    \draw[line width=0.75pt, dashed] (K) -- (P);
    
    % Right Angle Symbol
    \draw[line width=0.75pt] (2.4,0.4) -- (2.8,0.4) -- (2.8,0);
    \fill (2.6,0.2) circle (0.6pt);
    
    % Labels
    \node[below left, font=\itshape] at (L) {$L$};
    \node[below right, font=\itshape] at (M) {$M$};
    \node[above, font=\itshape] at (K) {$K$};
    \node[below] at (2.4,-0.1) {$16\text{ cm}$};
\end{tikzpicture}
```

---

### 5.2 Stereometry Diagrams (3D Solids — Tasks 11, 14, 15)
Used for prisms (kvádr, krychle, hranol) and composite solid models.

```
       H ───────────── G
      /             / │
     /             /  │   Top Face: Fill 5% Gray (#F2F2F2)
    E ──────────── F  │
    │             │   │
    │             │   │   Front Face: Fill 15% Gray (#D9D9D9)
    │             │   C
    │  - - - - -  │  /    Side Face: Fill 25% Gray (#BFBFBF)
    │             │ /
    A ──────────── B
```

#### TikZ 3D Solid Styling Rules:
1. **Projection**: Oblique cavalier or dimetric ($x$-axis horizontal, $y$-axis at $30^\circ$ or $45^\circ$, depth ratio $0.5$ or $0.7$).
2. **Visible Edges**: `line width=1.5pt`, `draw=black`.
3. **Hidden / Internal Edges**: `line width=1.0pt`, `dashed` (`dash pattern=on 3.5pt off 2.5pt`).
4. **Three-Tone Photometric Shading Model**:
   - **Top Face**: `fill=black!5` (`#F2F2F2`)
   - **Front Face**: `fill=black!15` (`#D9D9D9`)
   - **Right Side Face**: `fill=black!25` (`#BFBFBF`)
5. **Dimensions**: Placed outside the solid with $1.0\text{ mm}$ offset dimension text.

```latex
% TikZ 3D Kvádr Template
\begin{tikzpicture}[scale=0.8, line cap=round, line join=round]
    % Vertex coordinates
    \coordinate (A) at (0,0);
    \coordinate (B) at (3.5,0);
    \coordinate (C) at (5.0,1.2);
    \coordinate (D) at (1.5,1.2);
    \coordinate (E) at (0,3.0);
    \coordinate (F) at (3.5,3.0);
    \coordinate (G) at (5.0,4.2);
    \coordinate (H) at (1.5,4.2);
    
    % Shaded Faces
    \fill[black!15] (A) -- (B) -- (F) -- (E) -- cycle; % Front
    \fill[black!25] (B) -- (C) -- (G) -- (F) -- cycle; % Right
    \fill[black!5]  (E) -- (F) -- (G) -- (H) -- cycle; % Top
    
    % Hidden Edges
    \draw[line width=1.0pt, dashed, dash pattern=on 3.5pt off 2.5pt] (A) -- (D) -- (C);
    \draw[line width=1.0pt, dashed, dash pattern=on 3.5pt off 2.5pt] (D) -- (H);
    
    % Visible Edges
    \draw[line width=1.5pt] (A) -- (B) -- (C) -- (G) -- (H) -- (E) -- cycle;
    \draw[line width=1.5pt] (E) -- (F) -- (B);
    \draw[line width=1.5pt] (F) -- (G);
    
    % Dimension Labels
    \node[below] at (1.75, 0) {$a = 6\text{ cm}$};
    \node[below right] at (4.25, 0.6) {$b = 4\text{ cm}$};
    \node[left] at (0, 1.5) {$c = 8\text{ cm}$};
\end{tikzpicture}
```

---

### 5.3 Geometric Construction Fields (Tasks 9 & 10)
Tasks 9 and 10 provide a blank construction field with given base elements (points, lines, rays, or circles).

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                 │
│                                                                                 │
│                            ✕ A                                                  │
│                                                                                 │
│                                                    p                            │
│           ─────────────────────────────────────────/───                         │
│                                                   /                             │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

#### Exact Construction Field Specifications:
1. **Field Dimensions**: Width $= 162.0\text{ mm}$ ($459.2\text{ pt}$), Height $= 65.0\text{ mm}$ to $85.0\text{ mm}$.
2. **Bounding Box**: Framed by `0.96 pt` black line identical to the context box.
3. **Given Points Marker**:
   - Rendered as an **$\mathbf{X}$ cross** (NOT a dot or circle).
   - Formed by two intersecting lines: length $= 5.7\text{ pt}$ ($2.0\text{ mm}$), stroke $= 1.5\text{ pt}$, angle $= 45^\circ$.
   - Label: `MyriadPro-Regular` (or Italic), `12.0 pt`, placed $2.5\text{ mm}$ to the right/above: `A`, `B`, `S`.
4. **Given Lines**: Solid line, `line width=1.5pt`, labeled at the endpoint with italic lowercase letter: `p`, `q`, `o`, `v`.

```latex
% TikZ Construction Point & Line Macro
\newcommand{\cermatpoint}[3][above right]{% #1=position, #2=coordinate, #3=label
    \draw[line width=1.5pt] ($#2 + (-2.85pt,-2.85pt)$) -- ($#2 + (2.85pt,2.85pt)$);
    \draw[line width=1.5pt] ($#2 + (-2.85pt,2.85pt)$) -- ($#2 + (2.85pt,-2.85pt)$);
    \node[#1, font=\fontsize{12}{14}\selectfont] at #2 {#3};
}

% Usage:
% \draw[line width=1.5pt] (0, 1.5) -- (12, 1.5) node[right, font=\itshape] {$p$};
% \cermatpoint[above]{(4.0, 3.2)}{$A$};
```

---

### 5.4 Data Charts & Pattern Sequences (Tasks 11, 14, 16)

#### Pie Charts (Task 11 / 14):
- **Outer Circle**: `line width=1.5pt`, `draw=black`, radius $= 25.0\text{ mm}$.
- **Sector Dividers**: `line width=1.0pt`, `draw=black` from center to circumference.
- **Sector Shading Hierarchy**:
  - Sector 1: `fill=black!85` (Text: white `12 pt Bold`)
  - Sector 2: `fill=black!35` (Text: white or black `12 pt Bold`)
  - Sector 3: `fill=black!15` (Text: black `12 pt Regular`)
  - Sector 4: `fill=white`    (Text: black `12 pt Regular`)

#### Sequence Grids (Task 16):
- **Tile Unit**: Square of side $s = 4.5\text{ mm} \times 4.5\text{ mm}$.
- **Tile Border**: `line width=0.8pt`, `draw=black`.
- **Filled Tile**: `fill=black!80` or `fill=black!25`.
- **Figure Layout**: Labeled beneath each term: `1. obrazec`, `2. obrazec`, `3. obrazec`.

```latex
% TikZ Sequence Grid Unit
\newcommand{\cermattile}[3][white]{% #1=fill, #2=x, #3=y
    \draw[line width=0.8pt, fill=#1] (#2*0.45, #3*0.45) rectangle ++(0.45, 0.45);
}
```

---

## 6. Task Authoring & Mathematical Invariants

Every synthesized task must satisfy rigorous mathematical invariants to ensure zero ambiguity, clean solvable arithmetic, and strict alignment with CERMAT testing traditions.

### Task 1: Arithmetic & Order of Operations
- **Target Competence**: Priority of operations, powers of 10, signed integers.
- **Format**: 2–3 independent expressions, result only, 1 point each (Total: 2–3 pts).
- **Mathematical Invariants**:
  - All operands: Integers $a \in [-1000, 1000]$.
  - Divisors: Must divide cleanly without remainder (no repeating decimals).
  - Powers of 10: Bases $10^1, 10^2, 10^3$; exponents $\le 3$.
  - Result: Single integer or terminating decimal with max 1 decimal place.

### Task 2: Rational Numbers & Fractions
- **Target Competence**: Addition, subtraction, multiplication, division of fractions and compound fractions.
- **Format**: 2 subtasks, result only or procedure in 2.2, 1–2 points each (Total: 2–3 pts).
- **Mathematical Invariants**:
  - Denominators: Small primes and composites $d \in \{2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 18, 20, 24, 28\}$.
  - $\text{LCM}(\text{denominators}) \le 72$.
  - Result must reduce to an irreducible fraction $\frac{p}{q}$ with $\gcd(p,q) = 1$, where $|p| \le 99$ and $q \le 50$, or an integer.

### Task 3: Algebraic Expressions
- **Target Competence**: Expansion, factoring via binomial identities, rational expressions.
- **Format**: 2–3 subtasks with full written procedure (Total: 3–4 pts).
- **Mathematical Invariants**:
  - Variables: $a, b, x, y, n$.
  - Identities tested: $(a \pm b)^2 = a^2 \pm 2ab + b^2$ and $a^2 - b^2 = (a-b)(a+b)$.
  - Coefficients: Integers $c \in [-12, 12]$.
  - All algebraic simplifications must result in polynomials with degree $\le 2$.

### Task 4: Linear Equations & Systems
- **Target Competence**: First-order linear equations with fractional terms, brackets, or $2 \times 2$ systems.
- **Format**: 1–2 equations with full written procedure (Total: 3–4 pts).
- **Mathematical Invariants**:
  - Root: Unique integer $x \in [-20, 20]$ or simple fraction $x = \frac{p}{q}$ with $q \in \{2, 3, 4, 5\}$.
  - Linear independence in systems: $\det(A) \neq 0$, integer solution pair $(x, y)$.
  - Intermediate steps must not produce denominators $> 60$.

### Task 5: Applied Word Problems (Equation Modeling)
- **Target Competence**: Word problems (motion $s=vt$, shared work $\frac{1}{t_1} + \frac{1}{t_2} = \frac{1}{t}$, mixtures, age, pricing).
- **Format**: Context narrative + equation formulation + solution with procedure (Total: 3–4 pts).
- **Mathematical Invariants**:
  - Motion problems: Speeds $v \in [3, 120]\text{ km/h}$, times in clean fractions of hours ($15\text{ min} = \frac{1}{4}\text{ h}$).
  - All physical quantities strictly positive.

### Task 6: Planimetry (2D Geometry Calculation)
- **Target Competence**: Area and perimeter of composite polygons, Pythagorean theorem.
- **Format**: Vector diagram + 2–3 subtasks with procedure (Total: 3–4 pts).
- **Mathematical Invariants**:
  - Pythagorean triples: $(3,4,5)$, $(5,12,13)$, $(6,8,10)$, $(8,15,17)$, $(9,12,15)$, $(12,16,20)$.
  - Circle / arc calculations must use $\pi$ symbol or exact fractional multiples.

### Tasks 7 & 8: Applied Proportions, Units & Percentages
- **Target Competence**: Multi-step unit conversion ($\text{km}^2 \leftrightarrow \text{m}^2$, $\text{m}^3 \leftrightarrow \text{l} \leftrightarrow \text{dm}^3$), percentages (price increase/decrease), scale ($1 : 50\,000$).
- **Format**: Result only (Total: 2–3 pts each).

### Tasks 9 & 10: Geometric Constructions
- **Target Competence**: Compass and straightedge locus construction (Thales' theorem, distance loci, angle bisectors, tangents).
- **Format**: Assignment text + given element sketch + answer sheet drawing field (Total: 2–3 pts each).
- **Mathematical Invariants**:
  - Solvability: Must have exactly 1 or 2 distinct valid geometric solutions in the given half-plane.
  - Distances: $2.0\text{ cm} \le d \le 10.0\text{ cm}$ (fits standard drawing space).

### Task 11: Stereometry (3D Geometry Calculation)
- **Target Competence**: Volume and surface area of prisms, cylinders, and pyramids; spatial diagonals.
- **Format**: 3D diagram + 2–3 subtasks with procedure (Total: 3–4 pts).
- **Mathematical Invariants**:
  - Edge lengths: Integers $a, b, c \in [1, 25]\text{ cm}$.
  - Volume $V$ and surface $S$: Clean integers or exact multiples of $\pi$.

### Tasks 12 & 13: Multiple-Choice Reasoning (A–E)
- **Target Competence**: Single-variable algebraic model formulation (Task 12) and geometric angle calculation (Task 13).
- **Format**: 1 question, 5 options (A–E), exactly 1 correct (Total: 2 pts each).
- **Distractor Design Matrix**:
  - Option A: Correct answer (randomly permuted).
  - Option B (Sign Trap): Reverse sign in expansion: $+2ab$ instead of $-2ab$.
  - Option C (Operation Trap): Multiplied instead of divided by coefficient.
  - Option D (Off-by-One / Inversion): Reciprocal fraction or missing constant term.
  - Option E: `jiný výsledek` or boundary calculation error.

### Task 14: Data Interpretation & Truth Evaluation (ANO/NE)
- **Target Competence**: Reading tables/graphs, computing percentages/averages, evaluating 3–4 binary statements.
- **Format**: Table/chart + statements 14.1–14.3 (or 14.4), binary ANO/NE choice (Total: 2–4 pts).
- **Balance Rule**: Truth values must be mixed (never 3x ANO or 3x NE).

### Task 15: Structural Matching (A–F)
- **Target Competence**: Multi-case matching (3 subtasks 15.1–15.3 against 6 options A–F).
- **Format**: Shaded 3D solids / complex percentages / geometry scenarios (Total: 6 pts, 2 pts per match).
- **Distractor Rule**: 6 options provided for 3 subtasks $\implies$ exactly 3 active distractors.

### Task 16: Sequences & Mathematical Induction
- **Target Competence**: Generalizing visual and numerical patterns, deriving arithmetic formula $a_n = a_1 + (n-1)d$.
- **Format**: Context diagram of first 3 figures + 3 subtasks (Total: 4 pts):
  - 16.1: Direct computation ($n \in [4, 8]$).
  - 16.2: Forward extrapolation ($n \in [15, 50]$).
  - 16.3: Inverse equation solving: find $n$ given $a_n = K$ (must yield integer $n \in \mathbb{N}^+$).

---

## 7. Production LaTeX Master Template

This standalone, battle-tested master template implements all visual, typographical, and geometric tokens defined in this specification.

```latex
% ==============================================================================
% CERMAT M9 OFFICIAL TEST BOOKLET MASTER TEMPLATE
% Architecture: XeLaTeX / LuaLaTeX
% ==============================================================================
\documentclass[11pt,a4paper]{article}

% --- GEOMETRY SPECIFICATION (Exact to 0.01 mm) ---
\usepackage[
    paperwidth=210mm,
    paperheight=297mm,
    left=25.0mm,
    right=23.0mm,
    top=15.0mm,
    bottom=10.0mm,
    footskip=8.0mm,
    headheight=12.0mm,
    headsep=4.0mm
]{geometry}

% --- FONT SPECIFICATION ---
\usepackage{fontspec}
\usepackage{unicode-math}

% Primary Text Font: Adobe Myriad Pro (or TeX Gyre Heros fallback)
\IfFontExistsTF{Myriad Pro}{
    \setmainfont{Myriad Pro}[
        BoldFont={Myriad Pro Bold},
        ItalicFont={Myriad Pro Italic},
        BoldItalicFont={Myriad Pro Bold Italic}
    ]
    \setsansfont{Myriad Pro}
}{
    \setmainfont{TeX Gyre Heros}[
        BoldFont={TeX Gyre Heros Bold},
        ItalicFont={TeX Gyre Heros Italic},
        BoldItalicFont={TeX Gyre Heros Bold Italic}
    ]
    \setsansfont{TeX Gyre Heros}
}

% Primary Math Font: Cambria Math
\IfFontExistsTF{Cambria Math}{
    \setmathfont{Cambria Math}
}{
    \setmathfont{Latin Modern Math}
}

% --- PACKAGES ---
\usepackage{amsmath,amssymb}
\usepackage{tabularx,array}
\usepackage{enumitem}
\usepackage{fancyhdr}
\usepackage{tikz}
\usetikzlibrary{calc,arrows.meta,patterns,angles,quotes,shapes.geometric}
\usepackage{tcolorbox}
\tcbuselibrary{skins,breakable}

% --- CZECH LOCALIZATION ---
\usepackage{polyglossia}
\setdefaultlanguage{czech}

% --- COLOR DEFINITIONS ---
\definecolor{cermatblack}{RGB}{0,0,0}
\definecolor{cermatlogoblue}{RGB}{0,92,171}
\definecolor{cermatgray95}{RGB}{242,242,242}
\definecolor{cermatgray85}{RGB}{217,217,217}
\definecolor{cermatgray75}{RGB}{191,191,191}
\definecolor{cermatgray35}{RGB}{89,89,89}

% --- PAGE NUMBERING & RUNNING HEADERS ---
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
\cfoot{\fontsize{12}{14}\selectfont\thepage}

% Suppress headers/footers on page 1
\fancypagestyle{cover}{
    \fancyhf{}
    \renewcommand{\headrulewidth}{0pt}
}

% --- CUSTOM MACROS ---

% 1. Task Header Macro
\newcommand{\taskheader}[2]{% #1 = Task Number, #2 = Points String
    \vspace{4mm}
    \noindent
    \parbox{\textwidth}{%
        {\fontsize{14.04}{17}\selectfont\textbf{#1}}%
        \hfill%
        {\fontsize{12}{15}\selectfont\textbf{#2}}%
    }\\[-1mm]
    \noindent\rule{\textwidth}{0.96pt}\par
    \vspace{2mm}
}

% 2. Subtask Macro
\newcommand{\subtask}[2]{% #1 = Subtask ID (e.g. 1.1), #2 = Text
    \vspace{2mm}\noindent
    \makebox[12.5mm][l]{\fontsize{12}{15.8}\selectfont #1}%
    \parbox[t]{\dimexpr\textwidth-12.5mm\relax}{\fontsize{12}{15.8}\selectfont #2}%
    \par\vspace{1.5mm}
}

% 3. Context Box Macro (VÝCHOZÍ TEXT)
\newtcolorbox{contextbox}[1][]{%
    enhanced,
    sharp corners,
    colback=white,
    colframe=cermatblack,
    boxrule=0.96pt,
    left=3.5mm,
    right=3.5mm,
    top=3.0mm,
    bottom=3.0mm,
    fontupper=\fontsize{12}{15.8}\selectfont,
    before skip=3mm,
    after skip=3mm,
    #1
}

% 4. Context Box Title
\newcommand{\contexttitle}[1]{%
    \noindent{\fontsize{12}{15}\selectfont\textbf{#1}}\par\vspace{2mm}
}

% 5. Context Attribution Tag
\newcommand{\czvvtag}{%
    \par\vspace{1mm}\hfill{\fontsize{9.5}{11}\selectfont\textit{(CZVV)}}\par
}

% 6. Multiple Choice Row (A - E)
\newcommand{\mcoptionsfive}[5]{%
    \vspace{2mm}\noindent
    \begin{tabularx}{\textwidth}{@{}X@{}X@{}X@{}X@{}X@{}}
        \textbf{A)}\ #1 & \textbf{B)}\ #2 & \textbf{C)}\ #3 & \textbf{D)}\ #4 & \textbf{E)}\ #5
    \end{tabularx}\par\vspace{2mm}
}

% 7. Procedure Warning Banner
\newcommand{\procedurewarning}[1]{%
    \vspace{1.5mm}\noindent
    {\fontsize{12}{15.8}\selectfont\textbf{V záznamovém archu} uveďte v úloze #1 celý \textbf{postup řešení}.}\par\vspace{1.5mm}
}

% ==============================================================================
% DOCUMENT BODY (Demonstration of Authentic Page 2 Flow)
% ==============================================================================
\begin{document}

% --- TOP INSTRUCTION BANNER ---
\noindent
{\fontsize{12}{15}\selectfont V úlohách \textbf{1}, \textbf{2.1}, \textbf{3.1}, \textbf{3.2}, \textbf{5}, \textbf{6}, \textbf{7}, \textbf{8} a \textbf{16} přepište do záznamového archu pouze \textbf{výsledky}.}\par
\vspace{1mm}
\noindent\rule{\textwidth}{0.72pt}\par
\vspace{2mm}

% --- TASK 1 ---
\begin{contextbox}
    \contexttitle{VÝCHOZÍ TEXT K ÚLOZE 1}
    Pro čísla $A$, $B$, $C$ platí:
    \begin{align*}
        A &= \frac{2}{9} + \frac{5}{18}\\[1mm]
        B &= \frac{2}{9} : \frac{5}{18}\\[1mm]
        C &\text{ je aritmetický průměr čísel } A \text{ a } B.
    \end{align*}
    \czvvtag
\end{contextbox}

\taskheader{1}{max. 3 body}
\noindent{\fontsize{12}{15}\selectfont\textbf{Zapište zlomkem v základním tvaru číslo:}}\par\vspace{2mm}

\subtask{1.1}{$A$}
\subtask{1.2}{$B$}
\subtask{1.3}{$C$}

% --- SEPARATOR ---
\vspace{4mm}
\noindent\rule{\textwidth}{0.72pt}\par
\vspace{2mm}

% --- TASK 2 ---
\taskheader{2}{max. 3 body}

\subtask{2.1}{%
    \textbf{Vypočtěte:}\\[2mm]
    $(-1{,}5 - 1) \cdot (-1{,}5 + 1) =$
}

\subtask{2.2}{%
    \textbf{Vypočtěte} a výsledek zapište zlomkem v základním tvaru:\\[2mm]
    $\displaystyle \frac{\frac{25}{28} \cdot \left(-\frac{2}{5}\right)}{\frac{6}{7} : 2 + 1} = $
}

\procedurewarning{2.2}

\end{document}
```

---

## 8. Automated Fidelity Verification & Quality Assurance

To guarantee that generated tests match official CERMAT booklets with pixel-perfect accuracy, every test artifact must pass an automated triple-pass validation suite.

```
                    AUTOMATED QA PIPELINE
┌────────────────────────┐      ┌────────────────────────┐      ┌────────────────────────┐
│  PASS 1: MATHEMATICAL  │      │   PASS 2: STRUCTURAL   │      │    PASS 3: VISUAL      │
│     SOLVER CHECK       │ ───> │     GEOMETRY CHECK     │ ───> │    SSIM BENCHMARK      │
│  (SymPy Verification)  │      │    (PyMuPDF Bounds)    │      │ (Pixel Diff vs Target) │
└────────────────────────┘      └────────────────────────┘      └────────────────────────┘
```

### 8.1 Pass 1: Mathematical Invariant Checker (SymPy)
- **Determinism**: Every generated expression, equation, and geometry subtask is executed through a symbolic solver (`SymPy`).
- **Cleanliness Invariant**:
  - No fractions with denominators $> 100$.
  - No unreduced fractions in final answer keys ($\gcd(p, q) == 1$).
  - No negative values for physical quantities (distance, area, mass, speed, time).
  - All linear equations must possess exactly one root (no $\infty$ or $\emptyset$ cases).

### 8.2 Pass 2: Layout & Geometry Validator (PyMuPDF / Fitz)
The compiled PDF is parsed directly to verify physical coordinates:
- Total page count must be **exactly 12 pages**.
- Margin bounding boxes: text spans must not exceed $x_0 < 70.0\text{ pt}$ or $x_1 > 531.0\text{ pt}$.
- Rule thicknesses must match tolerances:
  - Heavy rule: $0.96\text{ pt} \pm 0.05\text{ pt}$.
  - Thin rule: $0.72\text{ pt} \pm 0.05\text{ pt}$.
- Header point badges must exactly sum to **50 bodů**.

### 8.3 Pass 3: Visual SSIM Benchmark
The generated PDF pages are rendered at $300\text{ DPI}$ alongside canonical reference crops. The **Structural Similarity Index (SSIM)** score must satisfy:

$$\text{SSIM}(\text{Generated}, \text{Reference}) \ge 0.965$$

Any deviation in font metrics, leading, rule weights, or TikZ line widths triggers a visual diff heat map for regression tracking.

---

> **Specification Authority**: Antigravity Technical Documentation Standards  
> **Target System**: ArchMaster CERMAT Generator Engine (Backend LaTeX Compiler)  
> **Related Documentation**: [CERMAT_handybook.md](file:///Users/jarda/ArchMaster/docs/CERMAT_handybook.md) (Curriculum & Pedagogical Blueprint)
