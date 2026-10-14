# Handoff: build the exam graph (M9)

Written 4 October 2026 for a new session. Status: **not started**. Update this line as the work progresses.

The owner's request: build the newly designed graph **without deleting the current ones**, and put it into the frontend as something they can look at **beside what already exists**.

## 1. Read first

1. `CLAUDE.md` and `frontend/DESIGN.md` (project rules, design guide).
2. `analysis/07_graph_representation.md` is the design and its measurements on the 610 items. `analysis/07_graph_representation.html` is the same report with its diagrams, including the solution flow of 2025 B 8 and the layer diagram; open it in a browser.
3. `analysis/07_graph_research_proposal.md` with `analysis/graph_research/example-exam-graph.json` is a parallel proposal written by another session on the same day. It reaches the same core design, and it contributes:
   - the edge vocabulary;
   - routes with explicit facts;
   - scoring rules: 2025 B 11 and 15 are encoded from the key images;
   - two worked routes for 2025 B 15.2.

   Use them; do not edit them.
4. `analysis/graph_design_spec.md`, sections 4–6 (what a principle is, what a link is, assignment rules) and section 11 (graph view requirements).
5. `analysis/06_graph_review.md`, sections 2, 3 and 7 (solution traces, review status, releases).

The two proposals agree on this model. The layers:

- **Exam layer:** Test → Task → Item.
- **Solution layer:** Item → Route → Step, where a step uses the results of earlier steps, applies exactly one principle, and produces a result.
- **Knowledge layer:** Principle → requires → Principle, the rebuilt tree, unchanged.
- **Error layer:** Misconception → corrupts → Principle, and a wrong option of a closed item reveals it.
- **Student layer:** comes later and is not part of this build.

Derived from these, never authored: each item's principle list, the slot template, the coverage map.

## 2. What must not change

- `analysis/data/m9_topic_tree.json`, `analysis/data/m9_item_skills*.json`, `analysis/data/before_rebuild/`: the old tree.
- `analysis/data/rebuilt/*`: the rebuilt tree. **Read only.**
- `analysis/data/m9_item_solutions.json`, `m9_item_solutions_older.json`: **read only**. If the new step data shows an annotation error, record it in the review list (section 3.1). The owner decides whether the solutions file changes. One known example: 2025 B 8.3 applies "opposite sides of a parallelogram are equal" (`KON.VLAST.rovnobeznik`) but does not list it.
- `backend/data/problems.sqlite` and how it is built; the `/strom` and `/ulohy` pages and their feature folders; `analysis/topic_tree.py`; `analysis/parked_graph_trial/`; the other session's `analysis/07_graph_research_proposal.md` and `analysis/graph_research/`.
- **Git:** the working tree holds much uncommitted work, and other sessions may be working in it at the same time. Never stash, reset, check out or discard files you did not create. Before starting, ask the owner whether to create a branch (`CLAUDE.md` wants one feature per branch; propose `exam-graph`). Commit only when asked.

The only existing files this build should touch:
- `backend/api/main.py`: one `include_router` line;
- `frontend/src/App.tsx`: one route;
- `frontend/src/Sidebar.tsx`: one link;
- `frontend/src/shared/routes.ts`: an address builder;
- `CLAUDE.md` and `frontend/DESIGN.md`: documentation;
- `backend/pyproject.toml` and `uv.lock`, only if SymPy is added (ask first).

## 3. Data: a new folder `analysis/data/exam_graph/`

Keys in Czech, like the solutions file (`reseni`, `principy`).

### 3.1 `m9_solution_graphs.json`: one flow per task

```json
{"2025 B": {"8": {
  "zadani": [
    {"id": "z1", "text": "základny 140 cm a 100 cm, výška 30 cm, pravý úhel"},
    {"id": "z2", "text": "řez je rovnoběžný se šikmým ramenem; obvody obou částí se rovnají"}
  ],
  "postupy": [{"id": "hlavni", "nazev": "Přirozený postup", "kroky": [
    {"id": "k1", "vstupy": ["z1"], "vysledek": "S = (140 + 100) · 30 : 2 = 3 600 cm²", "princip": "GEO.ROV.lichobeznik", "odpoved": "8.1"},
    {"id": "k2", "vstupy": ["z1"], "vysledek": "pravoúhlý trojúhelník s odvěsnami 140 − 100 = 40 a 30", "princip": "GEO.PYT.najit"},
    {"id": "k3", "vstupy": ["k2"], "vysledek": "rameno = 50 cm", "princip": "GEO.PYT.veta"},
    {"id": "k4", "vstupy": ["z1", "k3"], "vysledek": "o = 140 + 100 + 30 + 50 = 320 cm", "princip": "GEO.ROV.obvod", "odpoved": "8.2"},
    {"id": "k5", "vstupy": ["z2", "k3"], "vysledek": "řez = rameno = 50 cm", "princip": "KON.VLAST.rovnobeznik"}
  ]}],
  "bodovani": {"typ": "soucet", "body": {"8.1": 1, "8.2": 2, "8.3": 1}},
  "kontrola": {"odpovedi": "shoda-s-klicem", "kroky": "navrh", "principy": "navrh", "poznamky": []}
}}}
```

(The example is cut short. The full flow of 2025 B 8 has 10 steps and is drawn in the report, section 3, P3.)

Rules:

- **One flow per task.** Items of a task share steps. Every item has exactly one answer step (`odpoved`) in every route.
- **Inputs.** `vstupy` name `zadani` ids or earlier steps of the same route, so a route is acyclic. All inputs of a step are needed together (AND). A second route is an alternative (OR); add one only when it changes the principles applied, e.g. 2025 B 15.2, whose two routes are in the other session's export.
- **One principle per step**, from the rebuilt tree, at the granularity of the principles. Routine whole-number arithmetic stays inside a step and is never a step of its own (spec, rule 6).
- **Deriving an item's list.**
  - A step belongs to the first item, in item order, whose answer depends on it. A later item that needs it *reuses* that result: for example, 8.3 reuses k3 from 8.2.
  - The derived principle list of an item is the principles of its own steps. Reused steps appear as a dependency on the earlier item.
  - Compare the derived list with `principy` in the solutions file and put every difference in a computed review list. Never write the result back.
- **`kontrola`** keeps separate statuses for the answers (`shoda-s-klicem`, `prevzato-z-klice`, `bez-klice`), the steps and the principles (`navrh` until the owner reviews them). Nothing is marked reviewed by the session itself.
- **`bodovani`** per task, read from the key image (`backend/data/screenshots/M9-…-reseni.png`). Either additive points per item, or points by number of correct answers for A/N bundles and matching tasks. The other session read 2025 B 11 as `{2: 2, 3: 4}` and 2025 B 15 as `{1: 2, 2: 4, 3: 6}`; verify both. A whole test must total 50 points.

**Computation items with SymPy.**
1. In a throwaway script, first try generating the steps of the computation tasks (2025 B 1–5) from SymPy expression trees.
2. Keep the generator only if its steps come out at the granularity of the principles. Otherwise write those steps by hand and tell the owner why.
3. SymPy is not yet a dependency: ask before `uv add --project backend sympy`.

### 3.2 `m9_misconceptions.json`

```json
[{"id": "chybny-zaklad-srovnani", "nazev": "Chybný základ srovnání", "princip": "VZT.NEZ.obraceni",
  "popis": "Zlomek nebo procento vztáhne k veličině před „než“ místo k veličině za „než“.",
  "doklady": [{"test": "2025 B", "polozka": "15.2", "moznost": "C"}, {"test": "2023 A", "polozka": "15.2", "moznost": "B"}],
  "stav": "navrh"}]
```

- **Candidates:** the 33 closed MC/PR items where a wrong option is chosen more often than the key. Section 10 of `analysis/graph_representation_audit.py` lists them; run it with `uv run --no-project --with numpy --with networkx --with scikit-learn python analysis/graph_representation_audit.py`.
- **Naming an error:** open each booklet image and work out which calculation gives the wrong option. Record a misconception only when the option follows from a nameable error. List the rest as unexplained.
- **Existing notes:** reuse the „Typická chyba“ notes of the rebuilt tree where they match.
- **Shares:** the share of students choosing an option is read from `analysis/data/m9_item_stats_2022_2026.csv` (`distribution_pct`) at load time, never typed into the file.
- Two known cases:
  - 2025 B 15.2: 47.8 % chose 33 %, against 11.5 % for the key, 50 %.
  - 2023 A 15.2: 49.1 % chose 300 km, against 27.8 % for 320 km.

### 3.3 Pilot, in this order (each step end to end before widening)

1. **2025 B 8**, the worked example. Check that the 8.3 → 8.2 dependency and the missing `KON.VLAST.rovnobeznik` come out of the data.
2. **The other 15 tasks of 2025 B**: 32 items, 50 points. One whole test then has steps, scoring and misconceptions for the exam view.
3. **Tasks from other tests:**
   - 2023 A 15 (the same misconception as 2025 B 15.2);
   - 2022 A 12 (angles; its flow is written out in review 06, section 2);
   - 2022 D 7 (4–10 % success);
   - 2026 B 8 (integer boundary);
   - 2026 A 9 (a construction, worked in the other proposal).

Every other task is shown with its `reseni` line and `principy` list, marked as having no steps yet.

## 4. Backend: feature `exam_graph`

- **`backend/core/exam_graph.py`** (plus helper modules if needed). Plain Python, no web code, no numpy.
  - It loads one release: the rebuilt tree (reuse the loaders of `backend/core/topic_tree.py` without changing what `/strom` gets), the solutions file, the catalog, the item statistics and `analysis/data/exam_graph/`.
  - It validates the release. All references must resolve, routes must be acyclic, every item must be answered once per route, every principle id must exist in the rebuilt tree, misconception evidence must point to existing closed items and options, and every test with scoring must total 50.
  - It offers functions for:
    - **a task:** steps, edges, answers with CERMAT success, reused results, the derived and stored lists with their differences, and the misconceptions its options reveal;
    - **a principle:** direct prerequisites and dependents, its misconceptions, the steps and items that apply it;
    - **the exam:** the slot template over the 20 tests, coverage per principle (tests, items, points), and for one test its principles and item × principle incidence;
    - **the review list:** every open question for the owner.
  - Port logic from `analysis/graph_representation_audit.py` where it helps.
- **`backend/try_exam_graph.py`**: a throwaway script, run on real data before any endpoint, like `try_problem_db.py`.
- **`backend/api/exam_graph.py`**: `create_router(analysis_data_dir)`, `GET /api/exam-graph/...`, reading the JSON on every request like `backend/api/topic_tree.py`, so data edits show on reload. `main.py` only includes it.
- **Tests:** `backend/tests/test_exam_graph.py` and `test_exam_graph_api.py`. At least:
  - the real data validates;
  - 2025 B 8.3 reuses 8.2's step;
  - the review list contains the 8.3 difference;
  - task 9 is KON in all 20 tests;
  - 2025 B totals 50 points;
  - a broken reference fails validation.

## 5. Frontend: feature `exam-graph`

- **Address and navigation:** a new page, proposed at `/graf` with the sidebar label „Graf zkoušky“. Address builder in `shared/routes.ts`, link in `Sidebar.tsx`, route in `App.tsx`. Links to `/strom?tree=novy&node=…` and `/ulohy?problem=…` go only through the existing builders.
- **Three views**, switched in the bar the way „Strom | Graf“ switches on `/strom`. All state lives in the address: `/graf?view=uloha&task=M9-2025-B-08&route=hlavni`, `/graf?view=princip&node=VZT.NEZ.obraceni`, `/graf?view=zkouska&test=2025-B`.
  - **Úloha:** the task list on the left, with the tasks that have steps marked. The detail pane shows:
    - the booklet screenshot (`/api/screenshots/…`);
    - the solution flow: boxes for results, the principle under each, arrows meaning "computed from", answers with CERMAT success, a result reused by another item highlighted, and a route switch;
    - the misconceptions its wrong options reveal;
    - the differences between the derived and the stored principle list.
  - **Princip:** a search that lists matches and jumps to the chosen one. The selected principle has its direct prerequisites on the left and its dependents on the right, expandable on click. Below them: its misconceptions with their evidence, the steps and items that apply it, and a link into the new tree on `/strom`.
  - **Zkouška:** a test selector, the 16-slot template, and the coverage map: principles grouped by area and topic, painted by number of tests or points, with the selected test's principles marked.
- **Graph layout:** reuse `shared/graphLayout.ts`, which already lays out DAGs for the problem database and `/strom`. A component that two features need goes to `shared/`.
- **Mockup first** (`CLAUDE.md`; `DESIGN.md`, section 1): a static HTML page in `frontend/public/`, on real data, shown to the owner. Build the page only after their OK, then delete the mockup. The figures in `analysis/07_graph_representation.html` are a starting point for the look of the flow and the slot strip.

## 6. Finish

- `uv run --project backend pytest backend/tests`, then `npm --prefix frontend run build && npm --prefix frontend run lint`.
- In the browser, check `/graf` (all three views), `/strom` (both trees) and `/ulohy`.
- Update `CLAUDE.md` (repository layout, the new feature, its data folder, commands), `frontend/DESIGN.md` for any new UI pattern, and the status line of this file.

Numbers to check against:
- 20 tests, 320 tasks, 610 items;
- rebuilt tree: 7 areas, 23 topics, 157 principles (131 used), 131 links;
- 556 items have a CERMAT success rate (2024 C and D have none);
- 2025 B: 16 tasks, 32 items, 50 points.
