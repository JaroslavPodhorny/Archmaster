"""Endpoints of the problem database (backend/core/problem_db.py)."""
from __future__ import annotations

import os
from dataclasses import asdict
from typing import List, Literal, Optional

from fastapi import APIRouter, HTTPException, Query

from backend.core import problem_db

SCREENSHOTS_URL = '/api/screenshots'


def create_router(data_dir: str) -> APIRouter:
    """data_dir is the folder written by build_database: problems.sqlite + screenshots/."""
    router = APIRouter(prefix='/api/problems', tags=['problems'])
    db_path = os.path.join(data_dir, 'problems.sqlite')

    def require_database() -> None:
        if not os.path.exists(db_path):
            raise HTTPException(503, 'The problem database has not been built yet '
                                     '(run backend/try_problem_db.py build).')

    @router.get('')
    def problems(
        q: str = '',
        years: Optional[List[int]] = Query(None),
        terms: Optional[List[str]] = Query(None),
        formats: Optional[List[str]] = Query(None),
        tags: Optional[List[str]] = Query(None),
        points: Optional[List[int]] = Query(None),
        min_success: Optional[float] = Query(None, ge=0, le=100),
        max_success: Optional[float] = Query(None, ge=0, le=100),
        order_by: Literal['newest', 'oldest', 'hardest', 'easiest'] = 'newest',
        limit: int = Query(20, ge=1, le=100),
        offset: int = Query(0, ge=0),
    ):
        require_database()
        result = problem_db.search_problems(
            db_path, q, years, terms, formats, tags, points, min_success, max_success,
            order_by, limit, offset)
        return {
            'total': result.total,
            'problems': [{**asdict(p),
                          'screenshot_url': f'{SCREENSHOTS_URL}/{p.screenshot}',
                          'solution_url': f'{SCREENSHOTS_URL}/{p.solution}'}
                         for p in result.problems],
        }

    @router.get('/filters')
    def filters():
        require_database()
        return problem_db.filter_options(db_path)

    return router
