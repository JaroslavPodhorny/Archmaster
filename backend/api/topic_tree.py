"""Endpoint of the curriculum tree (backend/core/topic_tree.py)."""
from __future__ import annotations

from dataclasses import asdict

from fastapi import APIRouter

from backend.core import topic_tree


def create_router(analysis_data_dir: str) -> APIRouter:
    """analysis_data_dir holds the hand-made tree, the item–skill assignment and the task catalog
    (analysis/data). They are read on every request, so an edit made with analysis/topic_tree.py
    shows on reload."""
    router = APIRouter(prefix='/api/topic-tree', tags=['topic tree'])

    @router.get('')
    def tree():
        return [asdict(node) for node in topic_tree.tree_view(analysis_data_dir)]

    return router
