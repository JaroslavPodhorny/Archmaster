"""Endpoints of the exam graph (backend/core/exam_graph.py)."""
from __future__ import annotations

from dataclasses import asdict

from fastapi import APIRouter, HTTPException

from backend.core import exam_graph


def create_router(analysis_data_dir: str) -> APIRouter:
    """analysis_data_dir holds the rebuilt tree, the solutions, the task catalog and the exam graph's own
    files (analysis/data/exam_graph). They are read and checked on every request, so an edit shows on
    reload; data that does not fit together is a 500 that lists every problem."""
    router = APIRouter(prefix='/api/exam-graph', tags=['exam graph'])

    def release() -> exam_graph.Release:
        try:
            return exam_graph.load_release(analysis_data_dir)
        except exam_graph.InvalidRelease as e:
            raise HTTPException(500, str(e))

    @router.get('')
    def index():
        """The tests, every task (which of them have steps) and every principle with its topic and area."""
        out = exam_graph.index(release())
        out['tasks'] = [asdict(t) for t in out['tasks']]
        return out

    @router.get('/tasks/{problem_id}')
    def task(problem_id: str):
        r = release()
        if problem_id not in r.tasks:
            raise HTTPException(404, f'No task {problem_id}')
        return exam_graph.task_view(r, problem_id)

    @router.get('/principles/{principle_id}')
    def principle(principle_id: str):
        r = release()
        if principle_id not in r.principles:
            raise HTTPException(404, f'No principle {principle_id}')
        return exam_graph.principle_view(r, principle_id)

    @router.get('/exam/{test}')
    def exam(test: str):
        """test as in the address: 2025-B."""
        try:
            return exam_graph.exam_view(release(), test.replace('-', ' '))
        except KeyError:
            raise HTTPException(404, f'No test {test}')

    @router.get('/review')
    def review():
        return exam_graph.review_list(release())

    return router
