"""The tree of what the M9 test examines, and which skills each task needs.

Two hand-made files in analysis/data, changed only through analysis/topic_tree.py:

m9_topic_tree.json    areas > topics > skills, in learning order
m9_item_skills.json   for every scored item of every test, the skills it needs, the main one first:
                      {"2022 A": {"4.1": ["ALG.VYR.vytykani"], ...}, ...}

A skill no item needs is in CERMAT's specification but was not seen in the tests. The tree and the
assignment were rebuilt from the solutions of all items (analysis/graph_design_spec.md).

Nothing computed is stored. statistics() works out from the assignment and the task catalog how
often each skill is needed, how many points depend on it and how well its items are solved;
tree_view() gives every node with those numbers and the problems behind them, which is what the
tree page shows.
"""
from __future__ import annotations

import collections
import json
import os
from dataclasses import dataclass
from typing import Dict, Iterator, List, Optional, Sequence, Tuple

from .catalog import CatalogItem, CatalogTask, load_catalog

TREE_FILE = 'm9_topic_tree.json'
ITEM_SKILLS_FILE = 'm9_item_skills.json'
# Tests from before 2022 (References/Matematika_starsi), assigned the same way to check the tree against
# tests it was not built from. They are not in the task catalog and count in no statistic.
OLDER_FILE = 'm9_item_skills_older.json'
STANDARD_YEARS = (2022, 2023, 2025, 2026)   # the 2024 tests follow a different design (baseline, section 3)
RECENT_YEARS = (2025, 2026)
REGULAR_TERMS = ('A', 'B')                  # C and D were sat by a few hundred candidates

ItemSkills = Dict[str, Dict[str, List[str]]]


def _load(analysis_data_dir: str, name: str):
    with open(os.path.join(analysis_data_dir, name), encoding='utf-8') as f:
        return json.load(f)


def load_tree(analysis_data_dir: str) -> dict:
    return _load(analysis_data_dir, TREE_FILE)


def load_item_skills(analysis_data_dir: str) -> ItemSkills:
    return _load(analysis_data_dir, ITEM_SKILLS_FILE)


def load_older(analysis_data_dir: str) -> ItemSkills:
    return _load(analysis_data_dir, OLDER_FILE)


def depth(node: dict) -> int:
    """0 for an area, 1 for a topic, 2 for a skill."""
    return node['id'].count('.')


def walk(tree: dict) -> Iterator[Tuple[dict, Optional[dict]]]:
    """Every node with its parent (None for areas), in learning order."""
    def visit(node, parent):
        yield node, parent
        for child in node.get('children', []):
            yield from visit(child, node)
    for area in tree['areas']:
        yield from visit(area, None)


def skills_under(node: dict) -> List[dict]:
    """The skills of an area or topic; a skill gives itself."""
    if depth(node) == 2:
        return [node]
    return [s for child in node['children'] for s in skills_under(child)]


# ---- the test items: where each skill is needed, how often, how well it is solved
@dataclass
class Use:
    """One scored item that needs a skill."""
    year: int
    term: str
    item: str                       # "4.1", or "6" for a task without sub-items
    task: int
    points: float
    success_pct: Optional[float]
    main: bool                      # the skill is the first one listed for the item
    problem_id: str                 # the task's id in the problem database, e.g. M9-2025-B-15

    @property
    def ref(self) -> str:
        return f'{self.year} {self.term} {self.item}'


def catalog_items(catalog: Sequence[CatalogTask]) -> Dict[Tuple[str, str], Tuple[CatalogTask, CatalogItem]]:
    """(test, item) -> (task, item) for every scored item of the catalogued tests."""
    return {(f'{t.year} {t.term}', i.name): (t, i) for t in catalog for i in t.items}


def uses_by_skill(item_skills: ItemSkills, catalog: Sequence[CatalogTask]) -> Dict[str, List[Use]]:
    out = collections.defaultdict(list)
    for (test, name), (task, item) in catalog_items(catalog).items():
        for n, skill_id in enumerate(item_skills.get(test, {}).get(name, [])):
            out[skill_id].append(Use(task.year, task.term, name, task.task, item.points, item.success_pct,
                                     n == 0, task.problem_id))
    return out


def older_uses(older: ItemSkills) -> Dict[str, List[str]]:
    """skill id -> the items of the older tests that need it, e.g. "2021 B 8.1"."""
    out = collections.defaultdict(list)
    for test, items in older.items():
        for item, ids in items.items():
            for skill_id in ids:
                out[skill_id].append(f'{test} {item}')
    return out


def summary(uses: Sequence[Use]) -> dict:
    """What the uses of one skill (or of all skills of a topic) add up to."""
    uses = list({u.ref: u for u in uses}.values())       # an item counts once for a topic
    standard = [u for u in uses if u.year in STANDARD_YEARS]
    measured = [u for u in uses if u.term in REGULAR_TERMS and u.success_pct is not None]
    own = [u for u in measured if u.main] or measured
    tests = {(u.year, u.term) for u in standard}
    recent = {t for t in tests if t[0] in RECENT_YEARS}
    priority = 'S' if not uses else '1' if len(tests) >= 10 or len(recent) >= 6 else \
        '2' if len(tests) >= 4 or len(recent) >= 3 else '3'
    weight = sum(u.points for u in measured)
    return {
        'priority': priority,
        'items': len(uses),
        'tests': len(tests),            # of the 16 standard tests
        'recent': len(recent),          # of the 8 tests of 2025 and 2026
        'points': sum(u.points for u in standard) / 16,
        'success': sum(u.success_pct * u.points for u in measured) / weight if weight else None,
        'hardest': sorted(own, key=lambda u: u.success_pct)[:3],
    }


def statistics(tree: dict, item_skills: ItemSkills, catalog: Sequence[CatalogTask]):
    """id -> summary for every node, plus the uses by skill.

    A skill's own numbers count the items that need it. Its priority and its 'reach' numbers also count the
    items needing any skill that builds on it, so a foundation is never ranked below what stands on it."""
    uses = uses_by_skill(item_skills, catalog)
    built_on = collections.defaultdict(set)          # skill -> the skills that require it directly
    for node, _ in walk(tree):
        for q in node.get('requires', []):
            built_on[q].add(node['id'])

    def above(skill_id, found):
        for d in built_on[skill_id] - found:
            found.add(d)
            above(d, found)
        return found

    out = {}
    for node, _ in walk(tree):
        own = [u for s in skills_under(node) for u in uses[s['id']]]
        out[node['id']] = st = summary(own)
        if depth(node) == 2:
            dependents = above(node['id'], set())
            reach = summary(own + [u for d in dependents for u in uses[d]])
            st.update(priority=reach['priority'], dependents=len(dependents), reach_tests=reach['tests'],
                      reach_recent=reach['recent'], reach_points=reach['points'])
    return out, uses


# ---- the tree as the page shows it
@dataclass
class ItemUse:
    ref: str                        # "2025 B 15.2"
    problem_id: str                 # the task it belongs to, as the problem database names it
    success_pct: Optional[float]    # None where CERMAT published no result for the item
    main: bool                      # the skill is the item's main one


@dataclass
class TreeNode:
    id: str                         # POC, POC.VYR, POC.VYR.poradi
    parent: Optional[str]           # None for an area
    name: str
    spec: List[int]                 # areas 1–4 of CERMAT's specification
    note: str
    items: int                      # scored items of the 20 tests needing it (for a group: anything under it)
    problems: int                   # the tasks those items belong to: what the problem database finds for the id
    tests: int                      # of the 16 standard tests
    recent: int                     # of the 8 tests of 2025 and 2026
    points: float                   # per standard test
    success_pct: Optional[float]    # points-weighted, regular terms
    # skills only
    kind: Optional[str] = None      # procedure, translation, fact, strategy
    priority: Optional[str] = None  # 1, 2, 3 or S (specification only), counting what builds on the skill
    requires: Sequence[str] = ()    # direct prerequisites
    dependents: int = 0             # skills resting on it, directly or not
    reach_tests: int = 0            # tests, recent and points again, counting the dependents' items too
    reach_recent: int = 0
    reach_points: float = 0
    hardest: Sequence[str] = ()     # refs of its three least solved items
    older: Sequence[str] = ()       # items of the tests before 2022 needing it; in no number above
    uses: Sequence[ItemUse] = ()    # by year, term and task


def tree_view(analysis_data_dir: str) -> List[TreeNode]:
    """Every area, topic and skill in learning order, with its numbers and the problems behind them."""
    tree = load_tree(analysis_data_dir)
    stat, uses = statistics(tree, load_item_skills(analysis_data_dir), load_catalog(analysis_data_dir))
    before = older_uses(load_older(analysis_data_dir))
    nodes = []
    for n, parent in walk(tree):
        st = stat[n['id']]
        mine = [u for s in skills_under(n) for u in uses[s['id']]]
        node = TreeNode(
            id=n['id'], parent=parent['id'] if parent else None, name=n['name'], spec=n['spec'], note=n['note'],
            items=st['items'], problems=len({u.problem_id for u in mine}), tests=st['tests'],
            recent=st['recent'], points=st['points'], success_pct=st['success'])
        if depth(n) == 2:
            mine.sort(key=lambda u: (u.year, u.term, u.task, u.item))
            node.kind, node.priority, node.requires = n['kind'], st['priority'], n['requires']
            node.dependents, node.reach_tests = st['dependents'], st['reach_tests']
            node.reach_recent, node.reach_points = st['reach_recent'], st['reach_points']
            node.hardest = [u.ref for u in st['hardest']]
            node.older = before[n['id']]
            node.uses = [ItemUse(u.ref, u.problem_id, u.success_pct, u.main) for u in mine]
        nodes.append(node)
    return nodes
