import os

import pytest

from backend.core.problem_db import search_problems
from backend.core.topic_tree import tree_view

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture(scope='module')
def nodes():
    return tree_view(os.path.join(ROOT, 'analysis/data'))


@pytest.fixture(scope='module')
def by_id(nodes):
    return {n.id: n for n in nodes}


def test_every_node_once_parents_first(nodes, by_id):
    assert len(by_id) == len(nodes)
    assert [n.id.count('.') for n in nodes].count(0) == 7
    seen = set()
    for n in nodes:
        assert n.parent is None if '.' not in n.id else n.parent == n.id.rsplit('.', 1)[0]
        assert n.parent is None or n.parent in seen
        seen.add(n.id)


def test_prerequisites_are_skills_that_come_earlier(nodes):
    position = {n.id: i for i, n in enumerate(nodes)}
    for n in nodes:
        assert all(q.count('.') == 2 and position[q] < position[n.id] for q in n.requires)


def test_skill_numbers(by_id):
    n = by_id['VZT.NEZ.obraceni']
    assert (n.kind, n.priority, n.parent) == ('translation', '2', 'VZT.NEZ')
    assert n.requires == ['VZT.NEZ.okolik-kolikrat', 'VZT.NEZ.o-zlomek']
    assert (n.items, n.problems, n.tests, n.recent) == (11, 10, 8, 5)
    assert n.points == pytest.approx(0.9375)
    assert n.success_pct == pytest.approx(27.75)        # regular terms (A, B) of the standard years only
    assert [(u.ref, u.problem_id, u.main) for u in n.uses][:2] == [
        ('2022 D 15.3', 'M9-2022-D-15', True), ('2023 A 15.2', 'M9-2023-A-15', True)]
    assert n.hardest == ['2025 B 15.2', '2023 A 15.2', '2026 A 5']


def test_only_skills_carry_skill_fields(nodes):
    for n in nodes:
        if n.id.count('.') == 2:
            assert n.kind and n.priority in ('1', '2', '3', 'S')
            assert n.priority != 'S' or n.items == 0    # specification only: no item needs it
            assert n.items == len(n.uses)
            assert set(n.hardest) <= {u.ref for u in n.uses}
        else:
            assert n.kind is None and n.priority is None and not n.uses and not n.requires


def test_a_foundation_ranks_with_what_builds_on_it(by_id):
    n = by_id['POC.VYR.poradi']
    assert n.dependents > 0
    assert n.reach_tests >= n.tests and n.reach_points >= n.points
    assert n.priority == '1'


def test_a_group_counts_each_item_once(by_id):
    topic = by_id['VZT.PROC']
    skills = [n for n in by_id.values() if n.parent == 'VZT.PROC']
    assert topic.items == len({u.ref for s in skills for u in s.uses})
    assert topic.items < sum(s.items for s in skills)   # some items need two skills of the topic


def test_problem_counts_are_what_the_problem_database_finds(nodes, db_path):
    """The tree page links every node to the database filtered by its id."""
    for n in nodes:
        found = search_problems(db_path, skills=[n.id], limit=1000)
        assert found.total == n.problems, n.id
        assert {p.id for p in found.problems} >= {u.problem_id for u in n.uses}, n.id


def test_the_tree_is_the_one_rebuilt_from_the_solutions(nodes):
    by_id = {n.id: n for n in nodes}
    assert len(by_id) == len(nodes)
    assert [n.id.count('.') for n in nodes].count(0) == 7
    assert [n.id.count('.') for n in nodes].count(2) == 157
    position = {n.id: i for i, n in enumerate(nodes)}
    for n in nodes:
        assert n.parent is None if '.' not in n.id else position[n.parent] < position[n.id]
        assert all(q.count('.') == 2 and position[q] < position[n.id] for q in n.requires)
        if n.id.count('.') == 2:
            assert n.kind and n.priority in ('1', '2', '3', 'S') and n.items == len(n.uses)
    assert len({u.ref for n in nodes for u in n.uses}) == 610
    n = by_id['VZT.NEZ.obraceni']
    assert n.requires == ['VZT.NEZ.okolik-kolikrat', 'VZT.NEZ.o-zlomek']
    assert ('2025 B 15.2', 'M9-2025-B-15', True) in [(u.ref, u.problem_id, u.main) for u in n.uses]
