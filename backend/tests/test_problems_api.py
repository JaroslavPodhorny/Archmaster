import pytest
from fastapi.testclient import TestClient

from backend.api.main import create_app


@pytest.fixture(scope='module')
def client(data_dir) -> TestClient:
    return TestClient(create_app(data_dir))


def test_search_passes_filters_through(client):
    r = client.get('/api/problems', params={
        'q': 'obdelnik', 'years': [2025, 2026], 'order_by': 'hardest', 'limit': 5})
    assert r.status_code == 200
    body = r.json()
    assert 0 < body['total']
    assert len(body['problems']) == min(5, body['total'])
    assert all(p['year'] in (2025, 2026) for p in body['problems'])


def test_problem_shape_and_images(client):
    p = client.get('/api/problems', params={'years': 2025, 'terms': 'A', 'limit': 1}).json()['problems'][0]
    assert p['id'] == 'M9-2025-A-01'
    assert isinstance(p['tags'], list) and isinstance(p['pages'], list)
    for url in (p['screenshot_url'], p['solution_url']):
        image = client.get(url)
        assert image.status_code == 200
        assert image.headers['content-type'] == 'image/png'


def test_filters(client):
    body = client.get('/api/problems/filters').json()
    assert set(body) == {'years', 'terms', 'formats', 'tags', 'points'}
    assert body['years'][0] == {'value': 2026, 'label': '2026', 'count': 64}


def test_invalid_parameters_are_rejected(client):
    assert client.get('/api/problems', params={'order_by': 'random'}).status_code == 422
    assert client.get('/api/problems', params={'limit': 1000}).status_code == 422


def test_missing_database_is_reported(tmp_path):
    client = TestClient(create_app(str(tmp_path)))
    assert client.get('/api/problems').status_code == 503
    assert client.get('/api/problems/filters').status_code == 503
