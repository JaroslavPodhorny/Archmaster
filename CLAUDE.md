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

## Decisions made

- **Backend: Python with FastAPI.** Python was chosen for its libraries (e.g. SymPy for checking that answers are mathematically equivalent, PyMuPDF for working with the test PDFs) and because the analysis code is already Python.
- **Frontend: a React + TypeScript app** that talks to the backend over HTTP. Not Next.js: the owner prefers the clear split where all frontend code runs in the browser and all backend code runs on the server.

- **Tooling: Vite** for the frontend build and **uv** for Python dependencies.

Suggested but **not decided** (confirm with the owner before adopting): SQLite as the long-term database, KaTeX for rendering math, where to host.

## Repository layout

Exists now:

- `References/` holds the official CERMAT test booklets and answer keys (PDFs) plus CERMAT's requirements specification for the math exam. These are the primary evidence for the analysis.
- `analysis/` holds the findings derived from those PDFs and from official CERMAT publications (written October 2026): `01_baseline_M9.md` is the baseline for the 9th-grade math test, `02_katalog_uloh.md` lists every task of the 20 tests with CERMAT's success rates, `03_ucivo_M9.md` says per topic what a student must know, how it is tested and which tasks show it (it links to the screenshots in `backend/data/screenshots/`), `04_strom_M9.md` arranges the same curriculum as a tree in learning order (7 areas, 24 topics, 140 skills with priority, prerequisites and example tasks; generated, like the tree view `04_strom_M9.html`, from `data/m9_topic_tree.json`; that JSON is the only copy of the tree and is changed through `topic_tree.py`, a console editor that validates, saves and rebuilds both views: `uv run --project backend python analysis/topic_tree.py --help`), `data/` has the same as TSV/CSV, and `build_catalog.py` regenerates the catalog and summary numbers. Extend these rather than starting over; the 2024 tests follow a different design from the other years (see the baseline, section 3).

Layout the code follows:

```
backend/
  core/      the tools themselves: plain Python, no web code
  api/       FastAPI endpoints that only call into core/
  tests/     tests for core/
frontend/    React + TypeScript pages that only call the API
```

Problem database (branch `problem-database`, October 2026), working end to end for M9 2022–2026 only:

- `backend/core/booklet.py` finds and crops each task in a booklet PDF, `answer_key.py` does the same for each task's rows (solution and scoring notes) in the official key PDF, `catalog.py` reads `analysis/data`, `problem_db.py` has `build_database`, `search_problems`, `filter_options`.
- `backend/api/problems.py` exposes `GET /api/problems` and `GET /api/problems/filters`; `main.py` mounts it and serves the images under `/api/screenshots/`. `create_app(data_dir)` lets tests point it at a temporary database.
- `backend/tests/` builds the database from the real booklets once per run (about 6 s) and tests core and API against it.
- `frontend/src/features/problem-database/` is the page: a filter bar with one dropdown menu per filter on top, a compact result list on the left and the selected problem with its solution on the right. The window never scrolls as a whole; arrow keys step through the list; below 640 px the list and the detail take turns. In development Vite proxies `/api` to FastAPI on port 8000, so there is no CORS setup.
- SQLite is used locally for now; the owner is considering a hosted database (Supabase) for later.

Commands, all from the repository root (Python dependencies are managed with uv: `backend/pyproject.toml`, `backend/uv.lock`, Python 3.13 in `backend/.venv`):

```
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
                                  api.ts, types.ts, a use<Tool>.ts state hook, components/, <tool>.css
frontend/src/shared/              code used by more than one feature (http.ts so far)
```

- `frontend/src/App.tsx` and `backend/api/main.py` are shells that only mount features. Do not put feature code in them.
- A feature never imports from another feature's folder; code two features need moves to `shared/` (frontend) or its own `core/` module (backend).
- Feature CSS classes carry a short prefix (`pd-` for the problem database); `index.css` holds only global base styles.
- No router yet: there is one page. Add one (not decided which) when the second page arrives.

## Interface design

The owner rejects generic AI-looking interfaces and long scrolling pages. For every page:

- Controls the user needs repeatedly (filters, navigation) stay visible; never make the user scroll to reach them. Prefer a fixed bar plus panes that scroll separately over one long page.
- Plain and dense: system font, neutral greys, one accent colour used only for selection and links, hairline borders. No letter-spaced or uppercase labels, gradients, purple/indigo palettes, decorative cards, icons for decoration, or animations.
- For a new page or a real redesign, show the owner a mockup before building.

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
