# Representing a CERMAT problem, and the whole exam, as a graph (M9)

Written 4 October 2026. This is a proposal: it changes no data and no code. It looks at how graphs solved problems elsewhere, lists the ways a CERMAT item and a CERMAT test can be represented as a graph, measures several of those ways on the 610 solved items of the 20 tests, and recommends a design. It builds on the rebuilt tree (`data/rebuilt/`), the solutions file (`data/m9_item_solutions.json`), the design spec (`graph_design_spec.md`) and the review (`06_graph_review.md`); it does not repeat them.

All numbers come from `graph_representation_audit.py` (read-only; run it with `uv run --no-project --with numpy --with networkx --with scikit-learn python analysis/graph_representation_audit.py`). Success rates are CERMAT's published item results: 556 of the 610 items have one (2024 C and D have none). For closed items of 2022 and 2023 the success is the share choosing the key, as in `build_catalog.py`.

## Summary

1. **There is no single "best graph". The systems that worked keep several kinds of graph apart and link them.** Google Maps keeps the road network (curated, stable) apart from traffic (measured, changing) and from your trip (one route through it). Facebook's TAO stores one graph with a few typed nodes and typed edges. For CERMAT this means: the **principle graph** (what can be known) is one layer, each **item's solution** (how this item is solved) is another, the **exam** (tests, tasks, items, slots) is a third, **typical errors** a fourth, and later the **student** a fifth. Each layer has its own node and edge types, and the layers are joined by edges such as "this step applies this principle".
2. **The best representation of one problem is a small solution-flow graph whose steps point into the principle graph.** Its nodes are the given values and the intermediate results; an edge says "computed from"; each step names the one principle it applies. The item's principle list is then derived from the steps instead of typed by hand. This is what the Andes physics tutor did (each problem a solution graph, turned into a Bayesian network). Of the representations compared below, it (with its automatic special case for computations, P4) is the only one that explains *how* an item is solved. It also turns one item that needs 2.6 principles on average into steps that need one principle each, which is what diagnosis needs (Pelánek's "credit/blame assignment problem").
3. **The whole exam is best represented as three linked structures:** a bipartite graph of items and principles (each item a hyperedge over the principles it needs: the Q-matrix of psychometrics), a **template** of 16 slots (CERMAT reuses slots: task 4 is algebra in 19 of 20 tests, tasks 9 and 10 are always constructions, task 15 is percentages in 16 of 20 and relations between quantities in 19), and a **coverage map** that paints the principle graph with how often and for how many points each principle appears.
4. **The data supports the current principle graph, with limits:**
   - On the links: in 64 % of the 105 links that can be checked, the prerequisite's items are easier than the items of the principle that rests on it. Adding each item's prerequisites improves the prediction of item success (R² 0.36 → 0.39).
   - On the granularity: the 131 principles predict CERMAT difficulty **no better than the 19 coarse catalog tags** once item format is known (R² 0.48 vs. 0.50), and **format alone explains about a third** of the variance. The fine graph is worth having for explaining and diagnosing; it does not by itself explain why an item is hard.
   - On what is missing: about half of the variance in difficulty is left unexplained. What fills it is systematic errors (in 33 of 110 closed items a wrong option is chosen more often than the key), unusual modelling, number types, position in the test (task 16 averages 16 %) and dependence between items of one task. **This argues for adding an error layer and item-level attributes, not for more principle nodes.**
5. **Recommendation:** keep the principle graph as it is, and add three things in this order:
   1. solution-flow graphs per task, piloted on about 30 items, with the computation items generated automatically from their expression trees using SymPy;
   2. a small layer of misconception nodes, evidenced by CERMAT's distractor data;
   3. the exam template and the coverage map, which can be computed from data that already exists.

   The student layer waits until a tool collects answers. No graph database is needed: Facebook keeps TAO in MySQL.

## 1. What the graph has to do

The owner's goal (spec, section 1): every principle a solution uses is a node, linked where one depends on another; each task is a subgraph, and "this really tests if the graph is good, because you can solve the problem and see how good an insight the graph gives you". Longer term, a student's knowledge is a state of the graph. Turned into criteria a representation can be judged by:

| # | Criterion | Question it answers |
|---|---|---|
| C1 | Insight into a solution | Looking at an item's graph, do I see how it is solved and where it breaks? |
| C2 | Diagnosis | From a student's results, can I name the missing principle (not just "the item failed")? |
| C3 | Learning order | What should be learned before what? What is the student ready for next? |
| C4 | Exam value | How many points depend on a principle, and how does a test sample the graph? |
| C5 | Difficulty | Does the representation explain why some items are hard? |
| C6 | Search and related problems | Find all items that use X; suggest items like this one. |
| C7 | Student state | Can mastery live on the graph and be updated from evidence? |
| C8 | Cost | Can one person annotate 610 items consistently, and can it be checked? |
| C9 | Readability | Can it be drawn so a student or teacher understands it? |

## 2. How graphs solved problems before, and what each teaches here

### 2.1 Outside education

| System | Nodes and edges | What made it work | Lesson for CERMAT |
|---|---|---|---|
| Euler, bridges of Königsberg (1736) | land masses; bridges | throwing away everything except what matters for the question | a node is only what the questions need: principles, not textbook chapters |
| Euclid's *Elements*, drawn as a graph ([Euclid21, MAA](https://old.maa.org/node/590371); [Bridges 2016](https://archive.bridgesmathart.org/2016/bridges2016-503.html)) | propositions; "is used in the proof of" | the graph comes from the proofs themselves | the same method as ours: principles and links taken from the 610 written solutions |
| PERT and CPM (US Navy Polaris, DuPont, 1956–58) ([ENR](https://www.enr.com/articles/29910-network-logic-was-aided-by-mainframe-power?v=preview); [PERT](https://wikipedia.com/wiki/PERT)) | tasks; "must finish before", with durations | the critical path: the longest chain decides the finish date | a study plan before the exam date is a critical-path problem on the prerequisite graph; our longest chain has 6 principles (section 5.9) |
| PageRank (Page, Brin et al., 1998) ([Stanford](https://cs54n.stanford.edu/handouts/24-GooglePageRankAlgorithm.pdf)) | web pages; links | importance flows along links ("a link is a vote") | let the demand of items flow down to prerequisites to rank principles (section 5.9), instead of hand-set thresholds |
| Google Maps ([contraction hierarchies](https://www.mjt.me.uk/posts/contraction-hierarchies/); [DeepMind, 2020](https://deepmind.google/discover/blog/traffic-prediction-with-advanced-graph-neural-networks/)) | junctions or road segments; roads | three separate things: a curated road graph, live traffic as edge weights learned from data, and a hierarchy of important roads for speed and for zoom levels | keep the curated structure (principles, links) apart from measured weights (difficulty, mastery); show the graph at zoom levels (area → topic → principle → step) |
| Facebook TAO ([USENIX 2013](https://usenix.org/system/files/conference/atc13/atc13-bronson.pdf); [engineering blog](https://engineering.fb.com/2013/06/25/core-data/tao-the-power-of-the-graph/)) | typed objects (user, check-in, comment); typed associations (friend, liked by, tagged at) with a time field | one "labeled directed multigraph" with few types and fixed queries; persistent storage is MySQL | one graph with a handful of node types (test, task, item, step, principle, misconception, student) and edge types; SQLite is enough |
| Facebook "People You May Know" ([Cornell INFO 2040](https://blogs.cornell.edu/info2040/2016/09/18/facebook-helps-prove-triadic-closure-property)) | people; friendships | triadic closure: friends of friends become friends | "items like this one" and candidate links from shared neighbours; but co-occurrence is not a prerequisite (section 5.8) |
| Google Knowledge Graph (2012) ([Google blog](https://blog.google/products-and-platforms/products/search/introducing-knowledge-graph-things-not/)) | entities (people, places, works); typed facts | "things, not strings": search by the thing meant, not the words | search tasks by mathematical object (lichoběžník, výška, poměr) rather than by word; a later layer |
| Pinterest PinSage ([arXiv 1806.01973](https://ar5iv.labs.arxiv.org/html/1806.01973)) | pins and boards, a bipartite graph of 3 billion nodes | items are similar when they share boards; random walks on the bipartite graph | the item–principle graph is bipartite too; item similarity for "practise similar problems" comes from it |
| QMR-DT medical diagnosis ([Jaakkola & Jordan](https://arxiv.org/pdf/1105.5462)) | diseases → findings, a two-level bipartite Bayesian network with noisy-OR | hidden causes explain observed symptoms, each with its own probability | the closest analogue of diagnosing a student: principles are hidden causes, item results are symptoms; an item that needs all its principles is a noisy-AND |
| AND/OR graphs (Nilsson; AO*) ([arXiv cs/0305001](https://arxiv.org/pdf/cs/0305001)) | goals; "all of" (AND) and "one of" (OR) decompositions | a solution is a tree of AND steps; alternatives are OR branches | an item's solution is an AND of steps; a materially different route is an OR branch |
| Concept prerequisites from Wikipedia links ([Liang et al., EMNLP 2015](https://www.cs.cmu.edu/~ark/EMNLP-2015/proceedings/EMNLP/pdf/EMNLP193.pdf)) | concepts; asymmetric references | prerequisite direction can be estimated from data | candidate links can be mined (from co-occurrence, later from student data), then reviewed by hand |
| Metro maps of information ([Shahaf et al.](https://brown.stanford.edu/information-cartography/)) | clusters of documents; coherent lines | a few lines with stations are readable where a full graph is not | a way to draw the overview: one line per area or per typical chain |

### 2.2 In education and assessment

| Idea | What it is | Lesson for CERMAT |
|---|---|---|
| Learning hierarchies (Gagné, 1962) ([FERA](https://feraonline.org/article/10-on-validating-learning-hierarchies/)) | a goal broken into subordinate skills; a prerequisite claim must be validated by positive transfer | a link is a hypothesis to test with data, not a fact; section 5.7 is a first, weak test |
| Knowledge space theory, ALEKS ([Falmagne et al.](https://arxiv.org/pdf/1511.06757); [McGraw Hill](https://www.mheducation.com/content/dam/mhe/research/prek-12/essa-tier-4/aleks-assessing-learning-space.pdf)) | a knowledge state is the set of problem types a student can solve; a surmise relation orders them; the **outer fringe** is what the student is ready to learn | the student's state is a set of principles closed under prerequisites; "ready to learn" = principles whose prerequisites are all mastered |
| Q-matrix and cognitive diagnosis models (Tatsuoka; DINA; attribute hierarchy method) ([review, PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6512166); [Psicothema](https://www.psicothema.com/pi?pii=4584)) | an items × attributes 0/1 matrix plus a hierarchy among attributes; a latent-class model per student | our `principy` lists are a Q-matrix; whether gaps can be told apart depends on its design (section 5.6) |
| Linear logistic test model (Fischer, 1973) ([Frontiers](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2017.00897/pdf)) | item difficulty = weighted sum of the difficulties of the operations it needs | a direct test of a representation: does it explain difficulty? (section 5.3) |
| BUGGY (Brown & Burton, 1978) ([summary](https://tecfaetu.unige.ch/staf/staf-d/krige/staf11/buggy.html)) | errors are systematic "bugs", small edits of a correct procedure, and can be diagnosed | misconceptions deserve nodes of their own; CERMAT's distractor data shows them (section 5.5) |
| Experts sort problems by principle (Chi, Feltovich & Glaser, 1981) ([ASU](https://education.asu.edu/lcl/publications/chi-m-t-h-feltovich-p-glaser-r-1981-categorization-and-representation-physics)) | novices sort by surface features, experts by the principle that solves the problem | principles are the right primary node; a search by surface topic is what novices do |
| Schema-based instruction (Jitendra) ([IRIS](https://iris.peabody.vanderbilt.edu/module/math/cresource/q2/p06)) | word problems taught by their structure (change, group, compare) with a schema diagram | a possible "problem type" layer for word problems: srovnání („o třetinu méně než“), část a celek, změna |
| Knowledge components, KLI framework, additive factor model (Koedinger) ([LearnLab](https://learnlab.org/datashop/ResearchGoals)) | a knowledge component (KC) model maps steps to KCs and is judged by learning curves | a principle set is a KC model; it can be compared and refined with data |
| Bayesian knowledge tracing (Corbett & Anderson, 1995) ([JEDM](https://jedm.educationaldatamining.org/index.php/JEDM/article/view/35)) | mastery of one skill as a hidden binary state with learn, guess and slip | the minimal student model per principle |
| Deep and graph-based knowledge tracing ([Khajah et al., 2016](https://arxiv.org/pdf/1604.02416); [GKT survey](https://arxiv.org/pdf/2105.15106)) | neural networks over attempt sequences; GKT puts them on a concept graph | extended simple models matched deep ones; a known graph helps; no need for neural models before there is student data |
| Andes physics tutor (Conati, VanLehn et al.) ([AAAI 1998](https://mlanthology.org/aaai/1998/gertner1998aaai-procedural); [review](https://arxiv.org/pdf/1302.7081)) | each problem's **solution graph** of steps, turned into a Bayesian network for step-level assessment and hints | the model for the per-item layer recommended here |
| Graph2Tree; Inter-GPS ([ACL 2020](https://virtual.acl2020.org/paper_main.362.html); [arXiv 2105.04165](https://arxiv.org/pdf/2105.04165)) | word problems as graphs of quantities decoded into expression trees; geometry problems parsed into formal relations and solved by a sequence of theorems | computation items can be turned into expression trees automatically; a geometry figure can be a graph of objects and relations (a later layer) |
| Math Academy ([summary](https://frankhecker.com/2025/02/14/math-academy-part-7/); [Skycak](https://www.justinmath.com/)) | prerequisite edges plus fractional **encompassing** edges (a topic practises part of a simpler one); "credit travels downwards … penalties travel upwards" | practising an item reviews the principles its steps apply; the weight can be fractional |
| Squirrel AI ([Wikipedia](https://en.wikipedia.org/wiki/Squirrel_AI)) | middle-school mathematics split into over 10,000 knowledge points | the opposite end of granularity; a graph that fine needs a very large volume of student data before its nodes can be estimated |
| Dynamic Learning Maps ([KU, 2012](https://today.ku.edu/2012/05/02/ku-educational-center-unveils-worlds-largest-learning-map)) | more than 3,000 skills and 5,000 connections; items delivered as **testlets** sharing one context | a CERMAT task with several items is a testlet; its items are not independent (section 5.10) |
| Achieve the Core coherence map ([site](https://achievethecore.org/peersandpedagogy/creating-a-coherent-math-curriculum)) | standards linked within and across grades, used to trace a gap back | the teacher's use of a prerequisite graph: trace back from a failed task |
| Khan Academy knowledge map, removed ([support forum](https://support.khanacademy.org/hc/de/community/posts/360058025692/comments/360012904612)); Duolingo tree → path, 2022 ([Duolingo blog](https://blog.duolingo.com/new-duolingo-home-screen-design)) | a huge visible map was dropped; Duolingo replaced a branching tree with one path "to simplify" and reported better outcomes | the system keeps the graph; the student mostly needs a short path and a focused view, not the whole map |
| Domain modelling in practice (Pelánek, Masaryk University, systems Umíme to) ([paper](https://www.fi.muni.cz/~xpelanek/publications/domain-modeling.pdf)) | hundreds of KCs over thousands of items; a tree is often enough in practice; prerequisites matter mainly for rules; several KCs per item bring the "credit/blame assignment problem"; three difficulty levels were sufficient | the strongest practical caution: keep the structure simple, and solve the multi-principle problem by observing steps, not by guessing |

What runs through all of these: **the structures that lasted are curated by people and small in type count; the numbers on them come from data; and the view shown to a user is a small, focused part.**

## 3. Ways to represent one problem

Example used throughout: **2025 B 8** (one figure, three items). A right trapezoid with bases 140 cm and 100 cm and height 30 cm is cut by one segment into a smaller trapezoid and a parallelogram with equal perimeters. 8.1: area of the trapezoid; 8.2: its perimeter; 8.3: perimeter of the parallelogram. CERMAT success: 8.1 38.1 %, 8.2 42.0 %, **8.3 5.3 %**; 24 % skipped the task.

### P1. Bag of principles (what exists now)

The item is a set of principles, main one first. For 8.3: `VZT.SLOV.rovnice`, `VZT.SLOV.vyraz`, `GEO.ROV.obvod`, `ALG.ROV.upravy`. In graph terms the item is a hyperedge over principles, and all items together form a bipartite graph (the Q-matrix).

- Good for: search (C6), coverage counts (C4), the basis of every diagnosis model (C2).
- Weak at: insight (C1). It says *what* is used, not how or in which order, and not that 8.3 needs the 50 cm found in 8.2.

### P2. Induced prerequisite subgraph (spec, rule 8)

P1 plus the prerequisite links among the listed principles, with unlisted prerequisites greyed. For 8.3 the four principles are joined only by `VZT.SLOV.rovnice ← ALG.ROV.upravy` and `← VZT.SLOV.vyraz`; `GEO.ROV.obvod` stands alone.

- Good for: learning order (C3), "what else to revise".
- Weak at: insight. In 224 of the 519 multi-principle items the listed principles have no link among themselves (review 06), so the picture is mostly separate boxes. It shows the curriculum, not the solution.

### P3. Solution-flow graph (recommended)

Nodes are the values given in the task and every intermediate result; a directed edge means "computed from"; each computing step carries exactly one principle. The answers of the items are marked sinks. One graph per task, so items that reuse a result are visibly linked. A materially different route is an OR branch.

```
zadání: a = 140, c = 100, v = 30, řez ∥ rameno, obvody se rovnají

 a, c, v ──[GEO.ROV.lichobeznik]──▶ S = (140 + 100) · 30 : 2 = 3 600 cm²          ◀ 8.1
 a, c, v ──[GEO.PYT.najit]────────▶ pravoúhlý trojúhelník s odvěsnami 40 a 30
           ──[GEO.PYT.veta]───────▶ rameno = 50 cm
 a, c, v, rameno ──[GEO.ROV.obvod]▶ o = 140 + 100 + 30 + 50 = 320 cm               ◀ 8.2
 rameno ──[KON.VLAST.rovnobeznik]─▶ řez = 50 (protější strany rovnoběžníku jsou shodné)   ← not in the item's list
 x, řez ──[VZT.SLOV.vyraz]────────▶ o_R = 2x + 100
 x, a, c, v, řez ──[VZT.SLOV.vyraz]▶ o_L = (140 − x) + (100 − x) + 30 + 50 = 320 − 2x
 o_R, o_L ──[VZT.SLOV.rovnice]────▶ 2x + 100 = 320 − 2x
           ──[ALG.ROV.upravy]─────▶ x = 55
           ──[GEO.ROV.obvod]──────▶ o_R = 210 cm                                     ◀ 8.3
```

What this shows that P1 and P2 cannot:

- **Why 8.3 collapses to 5.3 %.** It is the only item whose path needs a variable, and it rests on the slant side computed in 8.2. A student who failed 8.2 has no 50 cm; the flat lists treat 8.2 and 8.3 as independent.
- **A step the annotation missed.** Drawing the flow exposes the step "the cut equals the slant side because opposite sides of a parallelogram are equal". `KON.VLAST.rovnobeznik` covers that fact in its note, but 8.3 does not list it. This is the owner's test working as intended: solving the task in graph form checks the graph.
- **Where the hint goes.** A tutor can ask for the 50 cm first, then for 2x + 100. Each answer is evidence about one principle, which removes the credit/blame problem for that item.

Cost: 2025 B 8 needs 10 steps for 3 items. The existing `reseni` lines hold about 1,700 computation segments (2.8 per item), but they compress steps (the parallelogram step above is not written out), so a full flow is more likely 3–5 steps per item: 2,000–3,000 steps for the 610 items, of which P4 can generate the computation items. Rule: routine whole-number arithmetic stays inside a step and is not a node of its own (spec, rule 6).

### P4. Expression tree (computation items, automatic)

For pure computations (tasks 1–5 in most tests) the solution flow is the expression's syntax tree: the operators are the steps. SymPy can parse `(66/30 − 55/30) · (−3)` into a tree and map node types to principles (a sum of fractions with unlike denominators → `POC.ZLOM.scitani`, a negative factor → `POC.VYR.zaporna`). This generates P3 for a large share of POC and ALG items without hand work. It also lets the app check a student's intermediate result for mathematical equivalence, one of the reasons Python was chosen.

### P5. Relational graph of a figure (geometry, later)

The figure as objects and relations, as Inter-GPS does: points A, B, C, D; `AB ∥ CD`, `AD ⊥ AB`, `|AB| = 140`; the cut `EF ∥ BC`. Theorems are rules that add new facts. This supports generating variants and drawing figures from structured content (the problem database's long-term plan), and could check geometry solutions mechanically. It is costly, covers only geometry, and does not diagnose by itself. Worth doing only when the database starts storing structured figures.

### P6. Problem type (schema) node

A node for the structure of a word problem, as in schema-based instruction: „srovnání: o zlomek více / méně než, neznámá za ‚než‘“, „část a celek se zbytkem“, „dvě veličiny, součet a rozdíl“. The spec deliberately has no node for a type that is only a combination. A schema node is something else: it groups items by the situation a student must recognise, which is exactly what fails in the two items of section 5.5. It could be a tag on the task rather than a node of the principle graph.

### Comparison of the problem representations

| | C1 insight | C2 diagnosis | C3 order | C5 difficulty | C8 cost | C9 readability |
|---|---|---|---|---|---|---|
| P1 bag of principles | low | medium | none | medium (R² 0.36) | done | high |
| P2 induced subgraph | low–medium | medium | high | slightly better (0.39) | done | medium (scattered boxes) |
| **P3 solution flow** | **high** | **high with step answers** | through its principles | not measured yet | 2,000–3,000 steps; P4 generates the computation items (29 % of items have a POC or ALG main principle) | high (left to right, like a route) |
| P4 expression tree | high for computations | high | through its principles | — | automatic | high |
| P5 figure relations | medium | low | none | — | high | medium |
| P6 problem type | medium | medium (finds misreadings) | none | — | low (one tag per task) | high |

## 4. Ways to represent the whole exam

### E1. Coverage map over the principle graph

Paint each principle with how many of the 20 tests use it and how many points depend on it, and draw the map at zoom levels (area → topic → principle). A single past test touches about 50 principles (41–58), 62 with their prerequisites. The map answers "what does a typical test look like on the graph?" and "what have I not practised?".

### E2. Bipartite item–principle graph with tasks as testlets

Items on one side, principles on the other, an edge per use (main one marked). Tasks group items that share a stem and a figure. This is the structure every diagnosis model needs (Q-matrix, DINA, knowledge tracing), the structure "related problems" come from (PinSage, friends of friends), and the input to the difficulty models of section 5.3.

### E3. Slot template

CERMAT builds tests from slots (section 5.2). The template is a small graph: slot → topics, weighted by how often each fills it, with format and points. It is useful for mock tests ("generate a test that looks like CERMAT's"), for setting expectations ("task 15 is percentages"), and as a structural fact about the exam, measured rather than assumed.

### E4. Error layer from distractors

Misconception nodes attached to the principle they corrupt, each with its evidence: an item, the wrong option, and the share of students choosing it. Closed items (MC, PR, A/N) give this for free: CERMAT publishes the distribution of answers.

### E5. Plan graph

The prerequisite DAG with durations and point values: a critical-path problem (PERT). Given a date and a current state, pick the principles with the most expected points per hour whose prerequisites are in place. This is the "outer fringe" of knowledge space theory with a value attached.

### E6. Derived graphs

Co-occurrence of principles (two principles linked when one item uses both), item–item similarity, communities. These graphs are computed, never authored. They are good for recommendations and for auditing the authored graph, and they are not a substitute for it (section 5.8).

## 5. What the data says (610 items, 20 tests)

### 5.1 Coverage and the long tail

| Principles used in … | count |
|---|---|
| all 20 tests | 8 |
| ≥ 15 tests | 21 |
| ≥ 10 tests | 42 |
| ≥ 5 tests | 81 |
| ≥ 1 test | 131 |

The 8 used in every test: `POC.ZLOM.scitani`, `POC.ZLOM.nasobeni`, `POC.ZLOM.kraceni`, `POC.VYR.zaporna`, `ALG.VYR.nasobeni`, `ALG.VYR.scitani`, `ALG.ROV.upravy`, `KON.ROZBOR.mnoziny`. Two tests share on average 39 % of their principles (Jaccard, range 26–60 %).

Working through k random past tests reaches:

| k tests | share of the 131 principles | share of all principle uses |
|---|---|---|
| 1 | 38 % | 63 % |
| 2 | 55 % | 79 % |
| 3 | 65 % | 86 % |
| 5 | 78 % | 93 % |
| 10 | 91 % | 98 % |

Past tests reach the common principles quickly; the last fifth of the graph needs targeted practice, and the graph says which part that is. This is an argument for E1 as a student-facing view.

### 5.2 Slots

Per task number, the share of the 20 tests whose main principle falls in the most common topic and area:

| Task | Most common topic | Area | Stable? |
|---|---|---|---|
| 3 | POC.ZLOM 65 % | POC 75 % | yes |
| 4 | ALG.VYR 70 % | ALG 95 % | yes |
| 5 | ALG.ROV 75 % | ALG 75 % | yes |
| 9 | KON.VLAST 85 % | KON 100 % | yes |
| 10 | KON.VLAST 90 % | KON 100 % | yes |
| 15 | VZT.PROC 80 % | VZT 95 % | yes |
| 16 | ZAK.RADA 60 % | ZAK 70 % | mostly |
| 1, 2 | POC.VYR 25–30 % | POC 60–65 % | area only |
| 8, 13, 14 | GEO.ROV or GEO.TEL 35–40 % | GEO 50–65 % | area only |
| 6, 7, 11, 12 | ≤ 30 % | 35–60 % | no: free slots |

ALG fills 5.0 items per test with a standard deviation of 0.2; VZT fills 10.6 ± 2.7. The table includes the 2024 tests, which follow a different design (baseline, section 3). Without them, tasks 9, 10 and 15 are even more fixed (15: percentages in 15 of 16 tests, VZT in all 16; 16: ZAK in 14 of 16), while task 3 is less so (fractions in 9 of 16).

### 5.3 Which representation explains difficulty?

CERMAT's item success predicted by ridge regression, trained on 19 tests and tested on the 20th, for each test in turn (no item is predicted by a model that saw its own test). R² is the share of variance explained on the held-out test; MAE is the mean error in percentage points.

| Representation of an item | features | R² | MAE | R², A/B tests only |
|---|---|---|---|---|
| mean only | 0 | −0.01 | 16.8 | −0.01 |
| item format (OV, OP, MC, PR, A/N, K) | 7 | 0.32 | 13.4 | 0.30 |
| catalog tags (19 topics) | 19 | 0.30 | 13.6 | 0.27 |
| topic of the main principle (23) | 23 | 0.31 | 13.6 | 0.34 |
| main principle only | 131 | 0.31 | 13.6 | 0.33 |
| principle set (Q-matrix, P1) | 131 | 0.36 | 13.0 | 0.33 |
| principle set + prerequisites (P2) | 157 | 0.39 | 12.7 | 0.36 |
| principle + topic + area (hierarchical) | 160 | 0.37 | 12.8 | 0.35 |
| counts (number of principles, prerequisites, depth, areas, steps) | 5 | 0.06 | 16.1 | 0.05 |
| format + tags | 26 | 0.42 | 12.2 | 0.41 |
| format + principle set | 138 | 0.45 | 12.0 | 0.44 |
| format + principle set + counts | 143 | 0.48 | 11.5 | 0.47 |
| format + principles with prerequisites + counts | 169 | 0.49 | 11.4 | 0.46 |
| format + tags + counts | 31 | 0.50 | 11.3 | 0.48 |

What it means:

- **Format matters as much as content.** Average success by format: A/N 60 %, OP 48 %, OV+OP 45 %, PR 44 %, MC 36 %, OV 26 %, constructions 25 %. Any model of an item needs its format as an attribute.
- **The prerequisite links carry real information.** Adding each item's prerequisites to its list improves prediction (0.36 → 0.39), so items that share prerequisites behave alike. The links are not arbitrary.
- **Finer is not more predictive.** With format and counts, 131 principles do no better than 19 tags (0.48 vs. 0.50). For explaining difficulty, the detail of the graph is not what is missing. Its value lies in C1, C2 and C3.
- **The number of principles hardly matters.** Correlation with success −0.11: items with one principle average 43 %, with six 30 %, and two to five lie between 33 and 37 %. A task is not hard because it is long.
- **About half the variance is unexplained.** The items most below the model's prediction show what it misses. These are open items, so which error students made is not published; the reading below is mine:
  - 2022 D 7.1–7.2: proportion with two kinds of stairs, 4–10 % success. The proportion itself is simple; the likely obstacle is setting up the situation.
  - 2026 B 8.1–8.2: triangle inequality asking for the smallest and largest whole number, 11–12 %. The likely trap is the strict inequality at an integer boundary.
  - 2022 D 2.2 and 2026 D 2.1: decimals with negative numbers, 13–25 %.
  - 2023 A 7.1 and 2026 C 15.2: „o kolik procent více“, 11–18 %, where the base is easy to take wrong (the error measured directly in 5.5).
  - 2025 D 16.2–16.4: the last task, 3–6 %. Position matters: task 16 averages 16 %.

  None of these is solved by another principle node. They call for misconception nodes, problem-type tags and item-level attributes (format, position, number type).

### 5.4 Item attributes the graph should carry

From 5.3: format, points, position in the test, whether the item reuses another item's result, number types (negative decimals, fractions), and the share skipped. They belong on the item node, not in the principle graph.

### 5.5 Distractors: errors are systematic

Of the 110 closed MC and PR items with a published answer distribution, **41 have a wrong option chosen by at least 25 %** and **33 have a wrong option chosen more often than the key**. The clearest cases:

| Item | Key | Most chosen wrong option | Principles |
|---|---|---|---|
| 2025 B 15.2: mladších o třetinu méně než starších; o kolik % více starších? | F 50 %: 11.5 % | C 33 %: **47.8 %** | VZT.NEZ.obraceni, VZT.NEZ.o-zlomek, VZT.PROC.o-kolik-procent |
| 2023 A 15.2: Roman ujel 400 km, o čtvrtinu více než Jana | C 320: 27.8 % | B 300: **49.1 %** | VZT.NEZ.obraceni, VZT.NEZ.o-zlomek |
| 2025 B 13 (cube of small cubes) | C: 25.0 % | E: 48.1 % | GEO.TEL.krychlicky |
| 2023 D 12 | B: 20.2 % | D: 45.1 % | GEO.ROV.obvod, VZT.SLOV.vyraz, VZT.SLOV.rovnice |
| 2022 C 15.3 | C: 15.3 % | A: 36.3 % | VZT.PROC.zaklad-po-zmene |

The first two are one error in two different tests: the fraction is applied to the wrong base (to the quantity before „než“ instead of the one after it). Nearly half of all students make it. A node „chybný základ srovnání“ attached to `VZT.NEZ.obraceni`, with these two items as evidence, carries more diagnostic value than any split of a principle. The tree's notes already describe typical errors in words („Typická chyba: …“); the error layer turns the most common of them into nodes with evidence. For open items the same evidence will come from students' wrong answers once the app collects them.

### 5.6 Can the item bank tell gaps apart?

A gap in principle k can be isolated from item results when some item needs k alone, or two items differ by exactly k (a contrast pair: solving one and failing the other points at k).

- 36 of the 131 principles appear alone in some item.
- 100 of the 131 are isolable by a contrast pair when items are represented by their explicit lists (P1).
- Only 79 are isolable when items are represented by their lists plus all prerequisites. **Keep the explicit lists; do not replace them with the prerequisite closure.** The rule "list what the solution applies, not what it rests on" (spec, rule 3) is the more diagnostic choice.
- No two principles have the same set of items, so none is indistinguishable from another by item membership alone.

The 31 principles without a contrast pair are where an app needs short diagnostic items of its own, or step answers (P3).

### 5.7 Are prerequisites easier than what rests on them?

Knowledge space theory implies that if B requires A, anyone who solves B's items can solve A's, so A's items should not be harder. Of the 105 links where both ends have at least three items with a success rate, **the prerequisite's items are easier in 67 (64 %)**, by 2.6 percentage points on average. Counting only main principles: 30 of 46 (65 %). This is weak, item-level support. Item contexts differ, so a third of reversals is expected and is not a list of wrong links. The real test (Gagné's transfer) needs student data.

### 5.8 Co-occurrence is not prerequisite

Linking two principles whenever one item uses both gives 568 pairs. Only 81 of them are prerequisite links, and 50 of the 131 prerequisite links never occur together in an item. 39 % of co-occurrence pairs cross areas, against 18 % (24 of 131) of prerequisite links. Tasks combine distant principles; prerequisites stay local. This confirms the spec's decision (section 7) not to add links for pairs that only occur together.

Communities found in the co-occurrence graph (Louvain, 11 groups) agree moderately with the 7 areas (adjusted mutual information 0.56). KON forms a group of its own, GEO joins some POC, VZT joins DAT, ALG joins the word-problem principles of VZT.SLOV, and ZAK joins divisibility. The principles that bridge groups most are `VZT.SLOV.rovnice`, `GEO.ROV.zpetne`, `POC.VYR.odmocnina` and `KON.VLAST.vyska`, the places where tasks connect areas. The taxonomy is reasonable; a data-driven grouping would move VZT.SLOV next to ALG.

### 5.9 Centrality

PageRank on the reversed prerequisite graph, seeded by how often items use each principle (demand flowing down to prerequisites): `POC.VYR.zaporna`, `ALG.VYR.scitani`, `POC.DEL.delitele`, `POC.ZLOM.kraceni`, `POC.ZLOM.nasobeni`, `POC.VYR.desetinna`, `ALG.VYR.nasobeni`, `ALG.ROV.upravy`. The most principles rest on `POC.VYR.desetinna` and `POC.DEL.delitele` (23 each). The longest chain has 6 principles: `POC.DEL.delitele → POC.ZLOM.kraceni → POC.ZLOM.nasobeni → VZT.CAST.cast → VZT.NEZ.o-zlomek → VZT.NEZ.obraceni`, and it ends at the principle of the 47.8 % error. As the review warned, reach is not a causal return; PageRank is a better-founded ranking for C4, not a promise of points.

### 5.10 Items of one task are a unit

185 of the 320 tasks have several items (475 items). In 112 of them all items share at least one principle; success inside one task differs by 19 percentage points on average and by up to 68. 2025 B 8 shows why: one item can depend on another's result. The exam graph needs the task as a node, and P3 should be drawn per task.

### Limits of these measurements

These are aggregated success rates of items, not students. Every principle list is one solver's judgement. The C and D tests have a few hundred takers, so their rates are noisy (the A/B-only column shows the conclusions hold without them). The step count in 5.3 is a rough proxy read from the `reseni` text. And 2024 differs in design. None of this measures learning; it measures whether a representation agrees with how CERMAT items behave.

## 6. The approaches side by side

| Approach | Industry analogue | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 cost | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| A. Topic tree only (catalog tags) | a library catalogue | – | – | – | ✓ | ✓ (as good as principles) | ✓ | – | done | keep for browsing |
| B. Principle DAG + item lists (now) | Euclid; KST; Q-matrix | low | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | done | **keep as the core** |
| C. Solution-flow graphs (P3, P4) | Andes; AND/OR graphs; spreadsheet dependencies | ✓✓ | ✓✓ (steps) | via B | – | ? | ✓ | ✓✓ (step evidence) | medium | **add; pilot first** |
| D. Error layer (misconceptions) | BUGGY; QMR-DT findings | ✓ | ✓✓ | – | ✓ | ✓ (fills residuals) | ✓ | ✓ | low | **add, small** |
| E. Exam template + coverage map | Maps zoom levels; PERT | – | – | ✓ | ✓✓ | ✓ (position) | – | ✓ | computed | **add (derived)** |
| F. Semantic object graph (figures, objects) | Google Knowledge Graph; Inter-GPS | medium | – | – | – | – | ✓✓ | – | high | later, with structured figures |
| G. Data-driven graphs (co-occurrence, learned links, GNN) | PYMK; PinSage; GKT; RefD | – | – | candidate links | – | – | ✓✓ | later | computed | derived views and audits only |
| H. Very fine nodes (thousands) | Squirrel AI | ✓ | only with massive step data | ✓ | – | – | – | ✓ | very high | no |

## 7. Recommended design: one typed graph in layers

```
EXAM LAYER          Test ──contains──▶ Task ──contains──▶ Item
                    (year, term)       (slot, stem,       (format, points, success, skipped,
                                        figure)            distractor shares, position)
                                                            │ answered by
SOLUTION LAYER      Step ──uses result of──▶ Step           ▼
                    (value, text)            (AND; OR for an alternative route)
                      │ applies (exactly one)
KNOWLEDGE LAYER     Principle ──requires──▶ Principle      (the rebuilt tree: 157 nodes, 131 links)
                      │ in
                    Topic ──in──▶ Area                     (taxonomy, for browsing and zoom)
ERROR LAYER         Misconception ──corrupts──▶ Principle
                    Item option ──reveals──▶ Misconception (share of students)
STUDENT LAYER       Student ──attempted──▶ Item / Step     (later: time, answer, result)
(later)             Student ──mastery──▶ Principle         (estimate + model version)
DERIVED             Item ──needs──▶ Principle (from steps, main marked) · Principle ~co-occurs~ Principle
                    Item ~similar~ Item · Slot ──typically──▶ Topic · coverage and PageRank on principles
```

| Part | Authored, derived or learned | Where it lives |
|---|---|---|
| Principles, prerequisites, taxonomy | authored (exists) | `data/rebuilt/m9_topic_tree.json` |
| Steps of each task, step → principle | authored, or generated from expression trees for computations | a `kroky` list per item in the solutions file |
| Item → principle lists | **derived from steps** (today typed by hand) | the existing `principy`, generated |
| Misconceptions | authored from the „Typická chyba“ notes + distractor evidence | a small file next to the tree |
| Item attributes | from the catalog and CERMAT statistics (exists) | catalog, stats, problem database |
| Template, coverage, co-occurrence, PageRank | derived on build | `core/` functions |
| Student state | learned, later | database |

How each part serves the criteria:

- **C1 insight:** the task page shows the step flow left to right, like a route, with each step's principle; clicking a principle opens it in the principle graph.
- **C2 diagnosis:**
  - item results go into a QMR-like model (principles as hidden causes, a noisy-AND per item);
  - step answers, when the app asks for them, give evidence about one principle each;
  - a wrong option that reveals a misconception names the error directly.
- **C3 order:** the prerequisite DAG; the outer fringe of a student's state is "ready to learn".
- **C4 value:** the coverage map plus PageRank; the template for mock tests.
- **C5 difficulty:** item attributes plus principles plus misconceptions, refit when student data arrives.
- **C6 search and related:** the bipartite graph (shared principles), the problem-type tag, later the object layer.
- **C7 student state:** mastery per principle (knowledge tracing), kept apart from evidence as the review asked.

Storage stays as it is: JSON for authoring, SQLite tables of nodes and edges for the app. TAO shows a relational database serving a typed graph at Facebook's scale; at 157 principles and a few thousand steps the whole graph fits in memory.

Drawing (for the redesign in spec section 11), taken from the same sources:

- **Zoom levels, like a map:** the overview shows areas and topics as groups; the principles appear on zooming in; the steps appear inside a task.
- **Focus first:** one principle with its direct prerequisites and dependents (the review's "principle focus"). A whole-graph poster was what Khan Academy dropped.
- **A route for a task:** P3 drawn left to right, the answer at the right end.
- **Lines for the overview (metro map):** the longest chains as lines through stations, as an alternative overview to try.

## 8. Considered and not recommended first

- **More, finer principle nodes.** The data shows finer content features do not explain difficulty better (5.3), and diagnosis gains more from steps and errors than from splitting nodes. Split only where the review's rule holds: parts fail independently and the teaching response differs.
- **A graph database (Neo4j or similar).** It solves none of the open problems: those are semantics, provenance and evidence, not queries.
- **Neural models (deep or graph-based knowledge tracing) now.** They need attempt sequences; simple models matched them even then (Khajah et al.).
- **Letting data define the links.** Co-occurrence finds how tasks are built, not what depends on what (5.8). Use it to propose candidates for review.
- **A full ontology of objects and relations (P5) for all items.** High cost, little diagnostic value now; revisit when the database stores structured figures.

## 9. Decisions for the owner, and a pilot

Questions whose answers change what happens next:

1. **Steps.** Should each task get a solution-flow graph (P3), with item principle lists derived from it? If yes, pilot about 30 items first: 2025 B 8, 2025 B 15, 2023 A 15, 2022 A 12, 2022 D 7, 2026 B 8, two constructions, three computation items generated by P4, and the seven items whose answers were taken from the key (spec, section 8). Judge the pilot by C1: does seeing the flow give real insight, and does it expose annotation errors like the one in 2025 B 8.3?
2. **Errors.** Should misconceptions become nodes, starting with the closed items where a wrong option beats the key (33) and the „Typická chyba“ notes they match?
3. **Problem types.** Should word-problem tasks carry a schema tag (srovnání, část a celek, změna, dvě veličiny)?
4. **Exam views.** Should the template (slots) and the coverage map be computed in `core/` for the graph page and later for mock tests?

Nothing here is needed before the owner's review of the rebuilt tree; all four additions keep the principle graph and its ids as they are.

## Sources

Outside education: [Facebook TAO paper (USENIX ATC 2013)](https://usenix.org/system/files/conference/atc13/atc13-bronson.pdf) · [TAO: the power of the graph](https://engineering.fb.com/2013/06/25/core-data/tao-the-power-of-the-graph/) · [Contraction hierarchies explained](https://www.mjt.me.uk/posts/contraction-hierarchies/) · [DeepMind: traffic prediction with graph neural networks](https://deepmind.google/discover/blog/traffic-prediction-with-advanced-graph-neural-networks/) · [PageRank (Stanford CS54N)](https://cs54n.stanford.edu/handouts/24-GooglePageRankAlgorithm.pdf) · [Introducing the Knowledge Graph](https://blog.google/products-and-platforms/products/search/introducing-knowledge-graph-things-not/) · [PinSage](https://ar5iv.labs.arxiv.org/html/1806.01973) · [Triadic closure and Facebook](https://blogs.cornell.edu/info2040/2016/09/18/facebook-helps-prove-triadic-closure-property) · [QMR-DT variational inference](https://arxiv.org/pdf/1105.5462) · [AND/OR graphs with cycles](https://arxiv.org/pdf/cs/0305001) · [Prerequisite relations from Wikipedia (RefD)](https://www.cs.cmu.edu/~ark/EMNLP-2015/proceedings/EMNLP/pdf/EMNLP193.pdf) · [Euclid21 (MAA)](https://old.maa.org/node/590371) · [Pythagorean theorem as a dependency graph](https://archive.bridgesmathart.org/2016/bridges2016-503.html) · [PERT](https://wikipedia.com/wiki/PERT) · [CPM history (ENR)](https://www.enr.com/articles/29910-network-logic-was-aided-by-mainframe-power?v=preview) · [Information cartography](https://brown.stanford.edu/information-cartography/)

Education: [Knowledge Spaces and Learning Spaces](https://arxiv.org/pdf/1511.06757) · [ALEKS: assessing in a learning space](https://www.mheducation.com/content/dam/mhe/research/prek-12/essa-tier-4/aleks-assessing-learning-space.pdf) · [Attribute hierarchies in cognitive diagnosis](https://pmc.ncbi.nlm.nih.gov/articles/PMC6512166) · [Estimation with hierarchical attributes (Psicothema)](https://www.psicothema.com/pi?pii=4584) · [LLTM (Frontiers)](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2017.00897/pdf) · [BUGGY](https://tecfaetu.unige.ch/staf/staf-d/krige/staf11/buggy.html) · [Chi, Feltovich & Glaser 1981](https://education.asu.edu/lcl/publications/chi-m-t-h-feltovich-p-glaser-r-1981-categorization-and-representation-physics) · [Schema instruction (IRIS)](https://iris.peabody.vanderbilt.edu/module/math/cresource/q2/p06) · [DataShop and knowledge components](https://learnlab.org/datashop/ResearchGoals) · [Properties of BKT](https://jedm.educationaldatamining.org/index.php/JEDM/article/view/35) · [How deep is knowledge tracing?](https://arxiv.org/pdf/1604.02416) · [Survey of knowledge tracing](https://arxiv.org/pdf/2105.15106) · [Andes procedural help](https://mlanthology.org/aaai/1998/gertner1998aaai-procedural) · [Bayesian ITS review](https://arxiv.org/pdf/1302.7081) · [Graph2Tree](https://virtual.acl2020.org/paper_main.362.html) · [Inter-GPS](https://arxiv.org/pdf/2105.04165) · [Math Academy (Frank Hecker)](https://frankhecker.com/2025/02/14/math-academy-part-7/) · [Justin Skycak](https://www.justinmath.com/) · [Squirrel AI](https://en.wikipedia.org/wiki/Squirrel_AI) · [Dynamic Learning Maps](https://today.ku.edu/2012/05/02/ku-educational-center-unveils-worlds-largest-learning-map) · [Coherence Map](https://achievethecore.org/peersandpedagogy/creating-a-coherent-math-curriculum) · [Khan Academy knowledge map thread](https://support.khanacademy.org/hc/de/community/posts/360058025692/comments/360012904612) · [Duolingo path](https://blog.duolingo.com/new-duolingo-home-screen-design) · [Pelánek: Managing items and knowledge components](https://www.fi.muni.cz/~xpelanek/publications/domain-modeling.pdf) · [Validating learning hierarchies](https://feraonline.org/article/10-on-validating-learning-hierarchies/)
