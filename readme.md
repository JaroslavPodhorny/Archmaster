# ArchMaster

archmaster is a CERMAT preparation platform that is designed to prepare the student as effectively as posisble making most of his time.

## Vision

The main idea is that expensive platforms where the test sheets mimic CERMAT testing are too expensive and can be replaced by AI workflow and a platforms that comes with it that can track the students progress and things like his desired high-school or target points.

I want this project aspire to be a platform that can be deployed to several thousand of active users and to be a product that is worth purchasing not AI-slop exam preparation that already exists in some form somewhere.

The platform is meant to prepare the student by familiarizing him with CERMAT type question through repeated tesing and reinforcement. It is meant to replace the [Todáš](https://www.to-das.cz) - a platform that provides students with practice CERMAT test in pdf form and live streams where the write and correct them.

## Tech Stack

- **Backend**: Python + FastAPI
- **Frontend**: TypeScript + React + Vite

## Run locally

Prerequisites: Python 3.11+, `uv`, and Node.js 22.12+ with npm. Run all commands below from the repository root.

### First-time setup

Install dependencies and build the local problem database:

```sh
uv sync --project backend
npm --prefix frontend ci
uv run --project backend python backend/try_problem_db.py build
```

The build needs the test booklets and answer-key PDFs in `References/Matematika/` and the catalog and curriculum files in `analysis/data/`. It creates `backend/data/problems.sqlite` and the problem and solution images in `backend/data/screenshots/`. These generated files are not tracked in Git. Rerun the build after changing the source data; it replaces the generated database and images.

### Start the app

In one terminal, start the backend:

```sh
uv run --project backend uvicorn backend.api.main:app --reload
```

In a second terminal, start the frontend:

```sh
npm --prefix frontend run dev
```

Open http://localhost:5173 (or the URL printed by Vite). The frontend forwards `/api` requests to the backend on port 8000. Interactive API documentation is available at http://127.0.0.1:8000/docs. Both servers reload when their source files change; press `Ctrl+C` in each terminal to stop them.

If the problem API returns “The problem database has not been built yet”, run the database build command above.

### Development checks

```sh
uv run --project backend pytest backend/tests
npm --prefix frontend run build
npm --prefix frontend run lint
```

## Important Product Principles

### AI does not design the UI/UX

### Do not let AI-generated UI patterns determine the product's design.

The UI and UX should be deliberately designed and kept consistent. Avoid generic "AI slop" interfaces, unnecessary dashboards, excessive cards, gradients, animations, or arbitrary components simply because they are common in AI-generated websites.

### Do not over-engineer or assume the final product

This project is currently in the idea and experimentation stage.

Do not assume that features, architecture, database structure, AI models, or workflows are already decided.

## Current Focus

The project is currently in an **experimentation and discovery phase**.

The main goal right now is to discover what actually makes students improve their
CERMAT results as effectively as possible between tests. I want to experiment
with different features, learning methods, feedback systems, and approaches to
find what genuinely helps students progress.

Most things built during this phase are expected to be temporary. Features
should be treated as experiments rather than commitments to the final product. and made to be easily tested in development enviroment.

The goal is not to keep adding features and optimizing an increasingly complex
system. Instead, the final product should be the result of **aggressive
simplification**: keep what demonstrably works, remove what does not, and
continuously question whether each part of the product is actually necessary.

> **Build → test → learn → delete → simplify → repeat.**

During this phase, prioritize **learning what the product should be** over
building a polished or permanent architecture.
