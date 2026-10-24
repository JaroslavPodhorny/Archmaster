import pytest
from fastapi.testclient import TestClient

from backend.api.main import create_app


@pytest.fixture(scope='module')
def client(data_dir) -> TestClient:
    return TestClient(create_app(data_dir))


def test_tree_shape(client):
    r = client.get('/api/topic-tree')
    assert r.status_code == 200
    nodes = r.json()
    assert [n['id'].count('.') for n in nodes].count(2) == 157
    area, skill = nodes[0], next(n for n in nodes if n['id'] == 'VZT.NEZ.obraceni')
    assert area['parent'] is None and area['kind'] is None and area['uses'] == []
    assert set(skill) == {
        'id', 'parent', 'name', 'spec', 'note', 'items', 'problems', 'tests', 'recent', 'points',
        'success_pct', 'kind', 'priority', 'requires', 'dependents', 'reach_tests', 'reach_recent',
        'reach_points', 'hardest', 'older', 'uses'}
    assert skill['uses'][4] == {'ref': '2025 B 15.2', 'problem_id': 'M9-2025-B-15', 'success_pct': 11.5, 'main': True}


def test_every_use_is_a_problem_the_database_serves(client):
    """A use links to /api/problems?skills=<skill>, where the problem must be listed."""
    skill = next(n for n in client.get('/api/topic-tree').json() if n['id'] == 'POC.ZLOM.scitani')
    listed = client.get('/api/problems', params={'skills': skill['id'], 'limit': 100}).json()
    assert listed['total'] == skill['problems']
    assert {u['problem_id'] for u in skill['uses']} == {p['id'] for p in listed['problems']}
