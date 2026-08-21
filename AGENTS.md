# Repository Guidelines

## Project Structure & Module Organization

ArchMaster is a CERMAT preparation platform.
The product is split by runtime:

- `backend/app/` contains the FastAPI application: HTTP routes in `api/`,
  configuration in `core/`, request/response models in `schemas/`, and proven
  learning rules in `engines/`.
- `backend/tests/` contains API and engine tests.
- `frontend/src/` contains the Vite React application; use `components/`,
  `features/`, `pages/`, `services/`, and `styles/` when needed.
- `docs/` holds product notes. `scripts/` is for repeatable development
  utilities.

## Build, Test, and Development Commands

Run commands from the project directory:

```bash
cd frontend && npm install && npm run dev  # Vite development server
cd frontend && npm run build && npm run lint
cd backend && uv sync --extra dev          # create/update local environment
cd backend && uv run uvicorn app.main:app --reload
cd backend && uv run pytest && uv run ruff check .
```

The frontend proxies `/api` requests to the backend at `localhost:8000` during
development.

## Coding Style & Naming Conventions

Use TypeScript with strict typing and React function components. Follow the
existing ESLint configuration; use PascalCase for components (`QuestionCard.tsx`)
and camelCase for functions and variables. Use four-space indentation in Python,
type annotations for public functions, `snake_case` modules/functions, and
`PascalCase` classes. Ruff is the backend style gate.

Keep engines independent of FastAPI and persistence: API routes validate input
and call engine functions; engines own learning rules. Develop exploratory
features in a focused Git branch, not a separate runtime or module tree.

## Testing Guidelines

Write pytest tests as `backend/tests/test_<area>.py`; test engine behavior
directly and API behavior through FastAPI's test client. Run the backend
suite before submitting changes. Frontend checks currently consist of
`npm run lint` and `npm run build`; add component tests when behavior merits it.

## Commit & Pull Request Guidelines

Git history uses imperative lowercase subjects (for example,
`add readme`). Continue that style: `add retry scheduler` or `fix API CORS`.
Keep commits focused. Create branches such as `feature/mistake-review` or
`experiment/question-selection` for exploratory work. Pull requests should
explain the product change, list verification commands run, link relevant
issues, and include screenshots for visible frontend changes.

## Configuration & Local Data

Copy `.env.example` files to `.env` files when configuration is needed;
never commit secrets. Do not edit `node_modules/`, `dist/`, or `.venv/` content.
