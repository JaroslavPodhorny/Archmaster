import json
import os
import shutil

import pytest

from backend.core import exam_graph

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA = os.path.join(ROOT, 'analysis/data')


@pytest.fixture(scope='module')
def release():
    return exam_graph.load_release(DATA)


def test_the_real_data_is_valid(release):
    assert len(release.tasks) == 320
    assert sum(len(t.items) for t in release.tasks.values()) == 610
    assert sum(i.success_pct is not None for t in release.tasks.values() for i in t.items) == 556
    assert len(release.principles) == 157
    assert sum(len(p.requires) for p in release.principles.values()) == 131
    assert {exam_graph.test_of(t) for t in release.tasks.values()} == {
        f'{y} {t}' for y in range(2022, 2027) for t in 'ABCD'}


def test_an_item_reuses_the_result_of_an_earlier_one(release):
    route = release.flows['M9-2025-B-08'].routes[0]
    steps = {s.id: s for s in route.steps}
    item = {d.item: d for d in route.items}
    assert [(r.step, r.item) for r in item['8.3'].reused] == [('k3', '8.2')]
    assert steps['k3'].item == '8.2' and steps['k3'].reused_by == ['8.3']
    assert item['8.2'].steps == ['k2', 'k3', 'k4']
    # 8.3 rests on the slant side but does not apply the Pythagorean theorem itself
    assert 'GEO.PYT.veta' not in item['8.3'].principles


def test_the_review_list_has_the_principle_the_stored_list_lacks(release):
    entry = next(r for r in exam_graph.review_list(release) if r['kind'] == 'rozdil-principu' and r['ref'] == '2025 B 8.3')
    assert entry['missing'] == ['KON.VLAST.rovnobeznik'] and entry['extra'] == []
    assert entry['reused'] == [{'step': 'k3', 'item': '8.2'}]
    assert not any(r['kind'] == 'rozdil-principu' and r['ref'] in ('2025 B 8.1', '2025 B 8.2')
                   for r in exam_graph.review_list(release))


def test_2025_B_has_steps_and_scoring_for_all_16_tasks_totalling_50(release):
    flows = [f for f in release.flows.values() if f.test == '2025 B']
    assert len(flows) == 16 and all(f.scoring for f in flows)
    assert sum(f.scoring.max_points for f in flows) == 50
    assert sum(len(f.routes[0].items) for f in flows) == 32
    scoring = release.flows['M9-2025-B-11'].scoring
    assert scoring.kind == 'pocet-spravnych' and scoring.points == {'0': 0, '1': 0, '2': 2, '3': 4}


def test_stored_principles_of_a_reused_step_are_told_apart(release):
    entry = next(r for r in exam_graph.review_list(release) if r['kind'] == 'rozdil-principu' and r['ref'] == '2025 B 6.3')
    assert entry['extra'] == [] and entry['extra_reused'] == ['POC.DEL.prvocisla']


def test_a_stepped_item_counts_with_its_derived_list(release):
    assert exam_graph.item_principles(release, '2025 B', '8.3')[1] == 'kroky'
    assert 'KON.VLAST.rovnobeznik' in exam_graph.item_principles(release, '2025 B', '8.3')[0]
    assert exam_graph.item_principles(release, '2022 A', '1') == (
        exam_graph.stored_principles(release, '2022 A', '1'), 'seznam')


def test_task_9_is_a_construction_in_every_test(release):
    slot = exam_graph.slot_template(release)[8]
    assert slot['task'] == 9 and slot['tests'] == 20 and slot['fixed']
    assert slot['areas'][0]['id'] == 'KON' and slot['areas'][0]['count'] == 20


def test_every_test_has_16_tasks_and_50_points(release):
    for test in {exam_graph.test_of(t) for t in release.tasks.values()}:
        view = exam_graph.exam_view(release, test)
        assert len(view['tasks']) == 16 and view['points'] == 50


def test_wrong_options_chosen_more_often_than_the_key(release):
    found = exam_graph.distractor_candidates(release)
    assert len(found) == 33
    assert (found[0]['test'], found[0]['item'], found[0]['option'], found[0]['share']) == ('2025 B', '15.2', 'C', 47.8)
    assert {'test': '2023 A', 'item': '15.2', 'option': 'B'}.items() <= next(
        c for c in found if c['test'] == '2023 A' and c['item'] == '15.2').items()


def test_every_dominant_wrong_option_is_explained_or_listed(release):
    review = exam_graph.review_list(release)
    assert not any(r['kind'] == 'neprozkoumano' for r in review)
    named = {(e.test, e.item) for m in release.misconceptions for e in m.evidence}
    listed = {(u.test, u.item) for u in release.unexplained}
    assert {(c['test'], c['item']) for c in exam_graph.distractor_candidates(release)} <= named | listed


def test_a_misconception_carries_cermat_shares(release):
    view = exam_graph.task_view(release, 'M9-2025-B-15')
    m = next(m for m in view['misconceptions'] if m['id'] == 'chybny-zaklad-srovnani')
    assert m['principle']['id'] == 'VZT.NEZ.obraceni'
    here = next(e for e in m['evidence'] if e['test'] == '2025 B')
    assert (here['option'], here['share'], here['key'], here['key_share']) == ('C', 47.8, 'F', 11.5)
    option = next(o for o in view['options'] if o['item'] == '15.2')['options'][2]
    assert option['option'] == 'C' and option['misconception'] == 'chybny-zaklad-srovnani'


def test_coverage_counts_an_item_once_per_principle(release):
    cover = {c['id']: c for c in exam_graph.coverage(release)}
    assert cover['KON.ROZBOR.mnoziny']['tests'] == 20
    assert all(c['tests'] == 0 for c in cover.values() if c['items'] == 0)
    assert sum(c['items'] > 0 for c in cover.values()) >= 131


# ---- data that does not fit together
@pytest.fixture
def copy(tmp_path):
    """A copy of the inputs that a test may break."""
    for name in (exam_graph.SOLUTIONS_FILE, exam_graph.STATS_FILE, 'm9_task_catalog.tsv'):
        shutil.copy(os.path.join(DATA, name), tmp_path / name)
    for folder in ('rebuilt', exam_graph.GRAPH_DIR):
        shutil.copytree(os.path.join(DATA, folder), tmp_path / folder)
    return tmp_path


def _edit(path, name, change):
    file = path / exam_graph.GRAPH_DIR / name
    data = json.loads(file.read_text(encoding='utf-8'))
    change(data)
    file.write_text(json.dumps(data, ensure_ascii=False), encoding='utf-8')


def _steps(graphs):
    return graphs['2025 B']['8']['postupy'][0]['kroky']


BREAKS = {
    'an input that does not exist': (
        lambda g: _steps(g)[3].update(vstupy=['z1', 'k99']), 'k4: input k99 is neither'),
    'an input that comes later (a cycle)': (
        lambda g: _steps(g)[1].update(vstupy=['k3']), 'k2: input k3 is neither'),
    'a principle not in the rebuilt tree': (
        lambda g: _steps(g)[0].update(princip='GEO.ROV.lichobeznik-obsah'), "unknown principle 'GEO.ROV.lichobeznik-obsah'"),
    'an item answered twice': (
        lambda g: _steps(g)[2].update(odpoved='8.2'), 'item 8.2 is answered 2 times'),
    'an item not answered': (
        lambda g: _steps(g)[0].pop('odpoved'), 'item 8.1 is answered 0 times'),
    'a step no answer needs': (
        lambda g: _steps(g).append({'id': 'k11', 'vstupy': ['z1'], 'vysledek': 'x', 'princip': 'GEO.ROV.obvod'}),
        'k11: no answer depends on it'),
    'points that differ from the catalog': (
        lambda g: g['2025 B']['8']['bodovani']['body'].update({'8.2': 3}), 'the catalog says 4'),
    'a task that does not exist': (
        lambda g: g['2025 B'].update({'17': g['2025 B']['8']}), '2025 B 17: no such task'),
    'a review state the session may not set': (
        lambda g: g['2025 B']['8']['kontrola'].update(odpovedi='zkontrolovano'), 'kontrola.odpovedi must be'),
}


@pytest.mark.parametrize('broken', BREAKS)
def test_broken_flows_fail_validation(copy, broken):
    change, message = BREAKS[broken]
    _edit(copy, exam_graph.GRAPHS_FILE, change)
    with pytest.raises(exam_graph.InvalidRelease) as e:
        exam_graph.load_release(str(copy))
    assert any(message in error for error in e.value.errors), e.value.errors


@pytest.mark.parametrize('evidence, message', [
    ({'test': '2025 B', 'polozka': '15.2', 'moznost': 'F'}, 'is the correct answer'),
    ({'test': '2025 B', 'polozka': '15.2', 'moznost': 'G'}, 'has no option G'),
    ({'test': '2025 B', 'polozka': '8.3', 'moznost': 'A'}, 'is not a closed item'),
    ({'test': '2025 B', 'polozka': '17', 'moznost': 'A'}, 'is not an item of the catalog'),
])
def test_misconception_evidence_must_be_a_wrong_option(copy, evidence, message):
    def change(data):
        data['chyby'] = [{'id': 'zkouska', 'nazev': 'Zkouška', 'princip': 'VZT.NEZ.obraceni', 'popis': 'x',
                          'doklady': [evidence], 'stav': 'navrh'}]
    _edit(copy, exam_graph.MISCONCEPTIONS_FILE, change)
    with pytest.raises(exam_graph.InvalidRelease) as e:
        exam_graph.load_release(str(copy))
    assert any(message in error for error in e.value.errors), e.value.errors
