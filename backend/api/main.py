"""Assembles the API from one router per tool. No logic lives in backend/api;
each router only calls into backend/core.

Run from the repository root:
    uv run --project backend uvicorn backend.api.main:app --reload
"""
from __future__ import annotations

import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from . import problems

_DEFAULT_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')


def create_app(data_dir: str) -> FastAPI:
    """data_dir is where the tools keep their built data (backend/data by default)."""
    app = FastAPI(title='ArchMaster API')
    app.include_router(problems.create_router(data_dir))
    app.mount(problems.SCREENSHOTS_URL,
              StaticFiles(directory=os.path.join(data_dir, 'screenshots'), check_dir=False))
    return app


app = create_app(os.environ.get('ARCHMASTER_DATA_DIR', _DEFAULT_DATA_DIR))
