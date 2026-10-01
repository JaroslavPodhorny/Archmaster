"""Builds the problem database once per test run from the real booklets
in References/Matematika and the catalog in analysis/data (takes a few seconds)."""
import os

import pytest

from backend.core import problem_db

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture(scope='session')
def data_dir(tmp_path_factory) -> str:
    path = str(tmp_path_factory.mktemp('data'))
    problem_db.build_database(
        os.path.join(path, 'problems.sqlite'), os.path.join(path, 'screenshots'),
        os.path.join(ROOT, 'References/Matematika'), os.path.join(ROOT, 'analysis/data'))
    return path


@pytest.fixture(scope='session')
def db_path(data_dir) -> str:
    return os.path.join(data_dir, 'problems.sqlite')
