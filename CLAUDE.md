# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

A web platform that helps students prepare for the Czech CERMAT standardized exams, using artificial intelligence. It will consist of several tools; which tools, and the overall product shape, are not decided yet. No application code exists yet.

The owner has experience with React + TypeScript frontends and has not built a full platform before. Explain backend and infrastructure choices plainly and keep the setup small.

## Current work, in order

1. **Reverse-engineer how CERMAT tests are made.** Analyze everything that can appear in them: every question type, the exact curriculum (which topics, at what difficulty), and how the tests are put together, so the tool can be built specifically for them.
   - **Mathematics for the 9th-grade entrance exam: first full pass done** (see `analysis/`).
   - The other tests are probably not very different, so expect many findings to carry over, but confirm that rather than assume it.
2. **Find out what helps students prepare most time-efficiently and effectively** (planned for the following month), so the tool is designed around what works in practice.
3. **Build tools one at a time** (see "How to build tools"). The first candidate is a searchable database of CERMAT problems that returns a screenshot of each problem and, later, structured content that can be displayed in a custom way, including diagrams. Its specifics are not decided.

## The M9 tree (rebuilt October 2026)

There is one tree. It was rebuilt from the solutions of all 610 items (design, rules and history: `analysis/graph_design_spec.md`) and on 24 October 2026 the owner retired the tree it replaced (7 areas, 24 topics, 162 skills, assigned from the task wording); that one is only in git history.

- The tree is in `analysis/data/` (`m9_topic_tree.json`, `m9_item_skills.json`, `m9_item_skills_older.json`): 7 areas, 23 topics, 157 skills (the spec calls them principles), 131 links. Its assignment is the `principy` lists of the solved items in `analysis/data/m9_item_solutions.json` (20 tests) and `m9_item_solutions_older.json` (the three tests before 2022, no keys to check against). Raw notes and helper scripts are in `analysis/solving/`.
- `analysis/topic_tree.py` edits it and keeps the solutions files in step (`check`, `show`, `assign … --solution`, `from-solutions`, `build`).
- **Not built:** the solution lines and per-task subgraphs (spec, section 9, steps 5–7) and the graph redesign (section 11).
- **Removed on 24 October 2026 at the owner's request:** the exam graph page (`/graf`, „Graf zkoušky“) and its research (`analysis/06_graph_review.md`, `07_graph_*`, `exam_graph_handoff.md`, `graph_research/`, `data/exam_graph/`), and the parked graph trial (`analysis/parked_graph_trial/`). All of it is in git history. Do not rebuild any of it unless the owner asks.
- **The problem generator** (whole M9 tests in CERMAT's format) was an experiment and is not part of this branch or `main`. It lives only on the local branch `experiment/problem-generator`, which the owner does not want presented.

## Decisions made

- **Backend: Python with FastAPI.** Python was chosen for its libraries (e.g. SymPy for checking that answers are mathematically equivalent, PyMuPDF for working with the test PDFs) and because the analysis code is already Python.
- **Frontend: a React + TypeScript app** that talks to the backend over HTTP. Not Next.js: the owner prefers the clear split where all frontend code runs in the browser and all backend code runs on the server.

- **Tooling: Vite** for the frontend build and **uv** for Python dependencies.
- **Styling: Tailwind CSS** (v4, through its Vite plugin; no config file). Components carry utility classes; the only stylesheet is `frontend/src/index.css`, which holds the design tokens (`@theme`: the palette, a 4 px spacing step, radii) and the base font.

Suggested but **not decided** (confirm with the owner before adopting): SQLite as the long-term database, KaTeX for rendering math, where to host.

## Repository layout

Exists now:

- `References/` holds the official CERMAT test booklets and answer keys (PDFs) plus CERMAT's requirements specification for the math exam. These are the primary evidence for the analysis.
- `analysis/` holds the findings derived from those PDFs and from official CERMAT publications (written October 2026): `01_baseline_M9.md` is the baseline for the 9th-grade math test, `02_katalog_uloh.md` lists every task of the 20 tests with CERMAT's success rates, `03_ucivo_M9.md` says per topic what a student must know, how it is tested and which tasks show it (it links to the screenshots in `backend/data/screenshots/`), `04_strom_M9.md` (and the tree view `04_strom_M9.html`) arranges the same curriculum as a tree in learning order: 7 areas, 23 topics, 157 skills, each with its prerequisites, how often it is needed, the points that depend on it, the success rate and its hardest items. Both are generated from three JSON files in `data/`: `m9_topic_tree.json` (the tree), `m9_item_skills.json` (for every scored item of the 20 tests, the skills it needs, main one first) and `m9_item_skills_older.json` (the same for 2019 A, 2021 A and 2021 B from `References/Matematika_starsi/`, a check that counts in no statistic). Those files are changed only through `topic_tree.py`, a console editor that validates, saves and rebuilds both views (`uv run --project backend python analysis/topic_tree.py --help`). Priorities are computed from the assignment, not stored; a skill no item needs is specification-only. The assignment comes from solving every item from its page image and checking the result against the official key (`graph_design_spec.md`); which skills an item needs is one solver's judgement. `data/` has the catalog and statistics as TSV/CSV, and `build_catalog.py` regenerates the catalog and summary numbers. Extend these rather than starting over; the 2024 tests follow a different design from the other years (see the baseline, section 3).

Layout the code follows:

```
backend/
  core/      the tools themselves: plain Python, no web code
  api/       FastAPI endpoints that only call into core/
  tests/     tests for core/
frontend/    React + TypeScript pages that only call the API
```

Problem database (branch `problem-database`, October 2026), working end to end for M9 2022–2026 only:

- `backend/core/booklet.py` finds and crops each task in a booklet PDF, `answer_key.py` does the same for each task's rows (solution and scoring notes) in the official key PDF, `catalog.py` reads `analysis/data`, `topic_tree.py` reads the tree and the item–skill assignment kept there (see "Curriculum tree page" below), `problem_db.py` has `build_database`, `search_problems`, `filter_options`.
- The database stores the tree (`skills`), its prerequisite links (`skill_requires`) and the skills of every item (`problem_skills`); `search_problems(skills=[...])` takes a skill, topic or area id, and every problem comes back with its skills per item and with `skill_graph`: those skills plus everything they rest on, directly or not, each with its direct prerequisites.
- `backend/api/problems.py` exposes `GET /api/problems` and `GET /api/problems/filters`; `main.py` mounts it and serves the images under `/api/screenshots/`. `create_app(data_dir)` lets tests point it at a temporary database.
- `backend/tests/` builds the database from the real booklets once per run (about 6 s) and tests core and API against it.
- `frontend/src/features/problem-database/` is the page: a filter bar with one dropdown menu per filter on top, where the „Téma“ menu is the curriculum tree (areas, topics that open to their skills; it replaced the 19 catalog tags in the page, the API still accepts `tags`), a compact result list on the left (the row above it holds the count, the filters in use and the sort order; the next page loads by itself as the end of the list comes near) and the selected problem with its skills, each once with the items that need it (click one to filter by it), under it its screenshot, its solution (opened by a button) and last the graph of those skills with all their prerequisites (`components/ProblemSkillGraph.tsx`; the problem's own skills in the accent colour, a box links to the skill in the tree), on the right. The window never scrolls as a whole; arrow keys step through the list; below 640 px the list and the detail take turns. The search and the shown problem are kept in the address (`/ulohy?skills=VZT.PROC&years=2025&problem=M9-2025-B-15`, same parameter names as the API; `address.ts`). In development Vite proxies `/api` to FastAPI on port 8000, so there is no CORS setup.
- SQLite is used locally for now; the owner is considering a hosted database (Supabase) for later.

Curriculum tree page (October 2026, built in the same working tree as the problem database), cross-referenced with it:

- `backend/core/topic_tree.py` also holds the numbers the tree is read by (`statistics`: priority, tests, points, success, hardest items; moved there from the console editor, which now imports them) and `tree_view(analysis_data_dir)`, which returns every area, topic and skill in learning order with those numbers and, for a skill, the items that need it with the id of their problem.
- `backend/api/topic_tree.py` exposes `GET /api/topic-tree`. It reads `analysis/data` on every request (about 10 ms), so an edit made with the console editor shows on reload. The problem database is a snapshot: **after editing the tree or the assignment, rebuild it** (`try_problem_db.py build`), or the tree's links lead to stale results. `backend/tests/test_topic_tree.py` checks that every node's problem count equals what the database finds for its id.
- `frontend/src/features/topic-tree/` is the page at `/strom`: a filter bar (search, priority and kind of skill as dropdown menus like the problem database's, „Jen související“; the switch between tree and graph at its right end), the tree on the left (arrow keys move, left/right close and open) and the selected node on the right with its numbers and the graph of its prerequisites. The selected node is in the address (`/strom?node=VZT.NEZ.obraceni`). It replaces `analysis/04_strom_M9.html` for browsing; that file is still generated.
- The same page has a second view, switched by „Strom | Graf“ in the bar (`/strom?node=…&view=graf`): the graph of all prerequisite links in place of the tree pane (`components/SkillGraph.tsx`). A skill's column is the length of the longest chain of prerequisites before it; skills no link joins form separate groups, one under another; the skills without any link are listed below by area. Selecting a skill draws its whole chain in the accent colour, the filters grey skills out without moving them, „Jen související“ hides the rest, arrow keys move between boxes, and the detail pane lists „Potřebuje“ and „Navazuje“ instead of the small graph. The layout is our own code (`shared/graphLayout.ts`, also used by the problem database for a problem's graph; no library; dagre was tried and was no clearer), deterministic, worked out once per load.
- The cross-references: in the tree, every node has „Zobrazit N úloh v databázi úloh“ and every item of a skill opens its task in the database filtered by that skill; in the database, every skill of a problem has „ve stromu“. Tasks of the tests before 2022 are not in the database and are plain text in the tree.

Commands, all from the repository root (Python dependencies are managed with uv: `backend/pyproject.toml`, `backend/uv.lock`, Python 3.13 in `backend/.venv`):

```bash
uv run --project backend python backend/try_problem_db.py build   # writes backend/data/ (SQLite + 640 images: each task and its solution, not in git)
uv run --project backend pytest backend/tests
uv run --project backend uvicorn backend.api.main:app --reload    # API on :8000
npm --prefix frontend install                                      # once
npm --prefix frontend run dev                                      # page on :5173
npm --prefix frontend run build && npm --prefix frontend run lint
```

Earlier folders named `scripts/`, `docs/`, `backend/`, `frontend/`, `output/` and the files `readme.md`, `GEMINI.md` were generated by another AI tool, are considered low quality and have been deleted from the working tree. Do not restore them from git history, build on them, or cite their conclusions.

## Code organization

The owner plans a large project and wants every tool kept as an isolated, neatly organized feature. Each tool gets one module or folder per layer, under the same name, and nothing of it leaks into shared files:

```
backend/core/<tool>.py            logic (plus helper modules it needs)
backend/api/<tool>.py             an APIRouter built by create_router(...); main.py only includes it
backend/tests/test_<tool>*.py
frontend/src/features/<tool>/     index.ts (the only file imported from outside), <Tool>Page.tsx,
                                  api.ts, types.ts, a use<Tool>.ts state hook, components/
frontend/src/shared/              code used by more than one feature (http.ts, routes.ts, controls.ts, graphLayout.ts,
                                  Dropdown.tsx, CheckOption.tsx, Section.tsx, Loading.tsx, icons.tsx,
                                  SidebarButton.tsx, sidebar.ts)
```

- `frontend/src/App.tsx` and `backend/api/main.py` are shells that only mount features. Do not put feature code in them. The shell's other pieces are `frontend/src/Sidebar.tsx` (`WithSidebar`: the navigation around every page) and `ThemeSwitch.tsx` (light, dark or the system's theme, in the sidebar).
- A feature never imports from another feature's folder; code two features need moves to `shared/` (frontend) or its own `core/` module (backend).
- Styling is Tailwind utility classes in the component itself. A class list used more than once becomes a constant in that file, or a small component; the ones every page uses (button, input, link, message, focus ring) are in `shared/controls.ts`. Use only the colours defined in `index.css` (Tailwind's default palette is switched off), and do not add feature stylesheets.
- Pages are routed with React Router (`BrowserRouter` and `Routes` in `App.tsx`; the links to the pages are in `Sidebar.tsx`). Each page has a Czech address (`/strom`, `/ulohy`) defined in `shared/routes.ts`; a page links to another only through the address builders there (`treeUrl`, `problemsUrl`). State another page or a reload must be able to restore (the selected node, the search and the shown problem) lives in the address, not only in component state.

## Interface design

**Read `frontend/DESIGN.md` before any UI work.** It is the design guide: what the owner wants and has rejected, the tokens (colours for both themes, the four text sizes, spacing, corners, shadows, layers), the page anatomy (sidebar, bar, panes, detail pane), the shared controls and patterns, the responsive, dark-theme, interaction and wording rules, and a checklist for finishing UI work. Keep it in step with the code, and update it whenever the owner decides something new about the interface.

The rules that matter most:

- The owner rejects generic AI-looking interfaces (gradients, purple, letter-spaced or uppercase labels, decorative cards and icons, animations) and long scrolling pages. The model is the ChatGPT web interface: plain, calm, soft greys, pills, rounded rows.
- Controls the user needs repeatedly stay visible: a fixed bar plus panes that scroll on their own; the window never scrolls.
- Every colour is a token from `index.css` (light and dark themes); shared class names are in `shared/controls.ts`, shared components in `shared/`. No fixed colours, no ad-hoc text sizes.
- Every number has its label beside it, related things sit in a section under a heading, weight shows level and never importance, and nothing moves, overflows or wraps into more than two rows when the window changes.
- For a new page or a real redesign, show the owner a mockup before building; when unsure, offer variants on real data.

## How to build tools

- **Logic first, web last.** Write each tool as plain Python functions in `backend/core/`, with defined inputs and outputs. Try them from a small throwaway script on real data before anything else. The function is the product; the script is not.
- Nothing in `core/` may know it is part of a website (no FastAPI imports, no request objects). This keeps tools testable and lets one tool call another directly.
- Once the behaviour is settled, add tests, then wrap the function in a thin API endpoint, then build the page that calls it.
- One tool at a time, as a thin slice through data → API → page, working end to end on real data before it is polished. One feature per git branch.
- If a tool idea does not work at the script stage, stop there; do not build an endpoint and page for it.
- Do not add accounts, payments, deployment setup or other platform features until a tool needs them.

## How to work here

- Every claim about CERMAT tests must be checked against the official PDFs or official CERMAT publications, and should say which tests it was verified on. Do not fill gaps with plausible-sounding guesses.
- The tests are in Czech; keep Czech terminology and wording exact when describing or reproducing tasks.
- Do not introduce product features, tools or infrastructure the owner has not asked for. Beyond the decisions listed above, the product shape waits for the analysis and the preparation research.
- The test booklets are marked "Předmětem autorských práv Centra pro zjišťování výsledků vzdělávání". Using them privately for analysis and development is fine; whether CERMAT's tasks or screenshots of them can be shown on a public site is unresolved and must be raised before anything is published.
