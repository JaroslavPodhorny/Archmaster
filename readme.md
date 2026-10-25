# ArchMaster

Platforma pro přípravu na CERMAT testy

## závislosti

Potřeba: [uv](https://docs.astral.sh/uv/getting-started/installation/) a [Node.js](https://nodejs.org) 22.12 nebo novější.

```sh
uv sync --project backend
npm --prefix frontend ci
uv run --project backend python backend/try_problem_db.py build
```

## backend

```sh
uv run --project backend uvicorn backend.api.main:app --reload
```

## frontend

```sh
npm --prefix frontend run dev
```

