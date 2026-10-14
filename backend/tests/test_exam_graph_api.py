import json
import os
import shutil

import pytest
from fastapi.testclient import TestClient

from backend.api.main import create_app

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA = os.path.join(ROOT, 'analysis/data')


@pytest.fixture(scope='module')
def client(tmp_path_factory) -> TestClient:
    # The exam graph reads only analysis/data; the problem database is not needed.
    return TestClient(create_app(str(tmp_path_factory.mktemp('data')), DATA))


def test_index(client):
    r = client.get('/api/exam-graph')
    assert r.status_code == 200
    body = r.json()
    assert len(body['tests']) == 20 and len(body['tasks']) == 320 and len(body['principles']) == 157
    task = next(t for t in body['tasks'] if t['id'] == 'M9-2025-B-08')
    assert task == {'id': 'M9-2025-B-08', 'test': '2025 B', 'task': 8, 'format': 'OV', 'points': 4,
                    'description': task['description'], 'success_pct': task['success_pct'], 'items': 3, 'stepped': True,
                    'main': 'GEO.ROV.lichobeznik'}
    assert {g['id'] for g in body['groups'] if g['parent'] is None} == {'POC', 'ALG', 'VZT', 'DAT', 'KON', 'GEO', 'ZAK'}


def test_task_with_steps(client):
    body = client.get('/api/exam-graph/tasks/M9-2025-B-08').json()
    assert body['stepped'] and body['screenshot'] == 'M9-2025-B-08.png'
    route = body['routes'][0]
    assert [s['id'] for s in route['steps']][:3] == ['k1', 'k2', 'k3']
    assert route['items'][2]['reused'] == [{'step': 'k3', 'item': '8.2'}]
    assert route['items'][2]['missing'] == ['KON.VLAST.rovnobeznik']
    assert [i['success_pct'] for i in body['items']] == [38.1, 42.0, 5.3]
    assert body['scoring']['partial'] == [{'item': '8.2', 'step': 'k3', 'points': 1}]


def test_task_without_steps_keeps_its_solution_lines(client):
    body = client.get('/api/exam-graph/tasks/M9-2022-A-01').json()
    assert not body['stepped'] and body['routes'] == []
    assert body['items'][0]['solution'] and body['items'][0]['stored']


def test_closed_task_lists_its_option_shares(client):
    body = client.get('/api/exam-graph/tasks/M9-2025-B-15').json()
    item = next(o for o in body['options'] if o['item'] == '15.2')
    assert {o['option']: o['share'] for o in item['options']}['C'] == 47.8
    assert [o['option'] for o in item['options'] if o['key']] == ['F']


def test_principle(client):
    body = client.get('/api/exam-graph/principles/KON.VLAST.rovnobeznik').json()
    assert body['topic']['id'] == 'KON.VLAST'
    assert any(s['problem_id'] == 'M9-2025-B-08' and s['step'] == 'k5' and s['item'] == '8.3' for s in body['steps'])
    item = next(i for i in body['items'] if i['test'] == '2025 B' and i['item'] == '8.3')
    assert item['in_steps'] and not item['in_list']
    assert client.get('/api/exam-graph/principles/POC.NIC').status_code == 404


def test_exam(client):
    body = client.get('/api/exam-graph/exam/2025-B').json()
    assert body['test'] == '2025 B' and len(body['tasks']) == 16 and body['points'] == 50
    assert len(body['template']) == 16 and len(body['coverage']) == 157
    assert {r['item'] for r in body['rows'] if r['task'] == 8} == {'8.1', '8.2', '8.3'}
    assert client.get('/api/exam-graph/exam/2030-A').status_code == 404


def test_review(client):
    body = client.get('/api/exam-graph/review').json()
    assert any(r['kind'] == 'rozdil-principu' and r['ref'] == '2025 B 8.3' for r in body)


def test_data_that_does_not_fit_is_reported(tmp_path):
    for name in ('m9_item_solutions.json', 'm9_item_stats_2022_2026.csv', 'm9_task_catalog.tsv'):
        shutil.copy(os.path.join(DATA, name), tmp_path / name)
    for folder in ('rebuilt', 'exam_graph'):
        shutil.copytree(os.path.join(DATA, folder), tmp_path / folder)
    graphs = tmp_path / 'exam_graph' / 'm9_solution_graphs.json'
    data = json.loads(graphs.read_text(encoding='utf-8'))
    data['2025 B']['8']['postupy'][0]['kroky'][0]['princip'] = 'GEO.NIC'
    graphs.write_text(json.dumps(data, ensure_ascii=False), encoding='utf-8')
    r = TestClient(create_app(str(tmp_path), str(tmp_path))).get('/api/exam-graph')
    assert r.status_code == 500 and 'GEO.NIC' in r.json()['detail']
