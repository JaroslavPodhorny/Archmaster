"""The exam graph of the M9 test: the tests, their tasks and items, how each task is solved step by step,
which principle each step applies, and which typical errors the wrong options of closed items reveal.

Its layers (analysis/07_graph_representation.md, section 7):

exam        test > task > item, with points and CERMAT's success rates (the task catalog)
solution    task > route > step; a step uses given facts and the results of earlier steps (all of them
            together), applies exactly one principle and produces a result; a second route is an
            alternative way through the whole task
knowledge   principle > requires > principle: the rebuilt tree, unchanged (analysis/data/rebuilt)
errors      misconception > corrupts > principle; a wrong option of a closed item reveals it

Hand-made inputs, all read only here:

analysis/data/rebuilt/m9_topic_tree.json         principles and their prerequisite links
analysis/data/m9_item_solutions.json             per item the solution line and the stored principle list
analysis/data/m9_task_catalog.tsv, m9_item_stats_2022_2026.csv   tasks, items, points, results, answer shares
analysis/data/exam_graph/m9_solution_graphs.json one flow per task (only the tasks worked out so far):
    {"2025 B": {"8": {"zadani": [{"id": "z1", "text": ...}],
                      "postupy": [{"id": "hlavni", "nazev": ..., "kroky": [
                          {"id": "k1", "vstupy": ["z1"], "vysledek": ..., "princip": "GEO.ROV.lichobeznik",
                           "odpoved": "8.1"}, ...]}],
                      "bodovani": {"typ": "soucet", "body": {"8.1": 1, ...}, "dilci": [...]},
                      "kontrola": {"odpovedi": "shoda-s-klicem", "kroky": "navrh", "principy": "navrh",
                                   "poznamky": []}}}}
analysis/data/exam_graph/m9_misconceptions.json  {"chyby": [...], "nevysvetlene": [...]}

Nothing derived is stored. load_release() validates everything and works out, per route, which item each
step belongs to (the first, in item order, whose answer depends on it), which results an item reuses from
an earlier one, and each item's principle list (the principles of its own steps), which is compared with
the stored list. The views below give a task, a principle, a test with the slot template and the coverage,
and the list of open questions for the owner.
"""
from __future__ import annotations

import collections
import csv
import json
import os
import re
from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

from . import topic_tree
from .catalog import CatalogTask, load_catalog

GRAPH_DIR = 'exam_graph'                    # under analysis/data
GRAPHS_FILE = 'm9_solution_graphs.json'
MISCONCEPTIONS_FILE = 'm9_misconceptions.json'
SOLUTIONS_FILE = 'm9_item_solutions.json'
STATS_FILE = 'm9_item_stats_2022_2026.csv'

TEST_POINTS = 50
TASKS_PER_TEST = 16
CLOSED_FORMATS = ('AN', 'MC', 'PR')
ANSWER_STATES = ('shoda-s-klicem', 'prevzato-z-klice', 'bez-klice')
REVIEW_STATES = ('navrh', 'zkontrolovano')
SCORING_KINDS = ('soucet', 'pocet-spravnych')
FIXED_SLOT_SHARE = 0.6                      # a slot is fixed when one topic fills it in this share of the tests

_OPTION = re.compile(r'^[A-FN]$')


class InvalidRelease(ValueError):
    """The hand-made files do not fit together; `errors` lists every problem found."""

    def __init__(self, errors: Sequence[str]):
        super().__init__(f'{len(errors)} problem(s) in the exam graph data:\n' + '\n'.join(errors))
        self.errors = list(errors)


# ---- the parts of a release
@dataclass
class Principle:
    id: str                         # POC.ZLOM.kraceni
    name: str
    note: str
    kind: str
    topic: str                      # POC.ZLOM
    area: str                       # POC
    requires: List[str]             # direct prerequisites
    position: int                   # place in learning order


@dataclass
class Group:
    """An area or a topic of the rebuilt tree."""
    id: str
    name: str
    parent: Optional[str]


@dataclass
class Given:
    id: str                         # z1
    text: str


@dataclass
class Step:
    id: str                         # k1, unique within its route
    inputs: List[str]               # given facts and earlier steps of the route, needed together
    result: str
    principle: str                  # the one principle it applies
    answer: Optional[str]           # the item it answers, if any
    item: str = ''                  # derived: the first item, in item order, whose answer depends on it
    reused_by: List[str] = field(default_factory=list)   # derived: later items whose own steps use it


@dataclass
class Reuse:
    step: str                       # a result an item uses
    item: str                       # the earlier item it was found on the way to


@dataclass
class ItemSteps:
    """What one route says about one item (all derived)."""
    item: str
    steps: List[str]                # its own steps, in route order
    reused: List[Reuse]
    principles: List[str]           # the principles of its own steps, in step order, each once
    behind: List[str] = field(default_factory=list)   # the principles of the reused steps and all they rest on


@dataclass
class Route:
    id: str
    name: str
    steps: List[Step]
    items: List[ItemSteps] = field(default_factory=list)


@dataclass
class Partial:
    """Points the key awards for an intermediate result when the item's answer is missing or wrong."""
    item: str
    step: str
    points: float


@dataclass
class Scoring:
    kind: str                       # soucet: points per item; pocet-spravnych: points by number of correct items
    points: Dict[str, float]        # item -> points, or number of correct items ("2") -> points
    partial: List[Partial]
    note: str = ''                  # the key's other rules in words, e.g. a point for working with one flaw

    @property
    def max_points(self) -> float:
        return sum(self.points.values()) if self.kind == 'soucet' else max(self.points.values(), default=0)


@dataclass
class Review:
    answers: str                    # shoda-s-klicem, prevzato-z-klice, bez-klice
    steps: str                      # navrh until the owner has reviewed them
    principles: str
    notes: List[str]


@dataclass
class Flow:
    test: str                       # "2025 B"
    task: int
    given: List[Given]
    routes: List[Route]
    scoring: Optional[Scoring]
    review: Review

    @property
    def problem_id(self) -> str:
        return problem_id(self.test, self.task)


@dataclass
class Evidence:
    test: str
    item: str
    option: str


@dataclass
class Misconception:
    id: str
    name: str
    principle: str                  # the principle it corrupts
    description: str
    evidence: List[Evidence]
    state: str


@dataclass
class Unexplained:
    """A wrong option chosen more often than the key, for which no nameable error was found."""
    test: str
    item: str
    option: str
    note: str


@dataclass
class Release:
    principles: Dict[str, Principle]                    # in learning order
    groups: Dict[str, Group]                            # areas and topics, in learning order
    dependents: Dict[str, List[str]]                    # principle -> principles requiring it directly
    tasks: Dict[str, CatalogTask]                       # by problem id, in catalog order
    solutions: Dict[str, Dict[str, dict]]               # test -> item -> {"reseni", "principy"}
    distributions: Dict[Tuple[str, str], Dict[str, float]]   # (test, item) -> option -> share chosen
    flows: Dict[str, Flow]                              # by problem id
    misconceptions: List[Misconception]
    unexplained: List[Unexplained]


# ---- names
def problem_id(test: str, task: int) -> str:
    """"2025 B", 8 -> M9-2025-B-08, as the problem database names a task."""
    year, term = test.split()
    return f'M9-{year}-{term}-{task:02d}'


def test_of(task: CatalogTask) -> str:
    return f'{task.year} {task.term}'


def item_order(name: str) -> Tuple[int, ...]:
    return tuple(int(part) for part in name.split('.'))


def _item_names(task: CatalogTask) -> List[str]:
    return [item.name for item in task.items]


def _keys(task: CatalogTask) -> Dict[str, str]:
    """item -> its key option, for closed tasks; A/N statements as A or N."""
    if task.format not in CLOSED_FORMATS or not task.answer_key:
        return {}
    keys = [{'Ano': 'A', 'Ne': 'N'}.get(k, k) for k in task.answer_key.split(',')]
    return dict(zip(_item_names(task), keys))


# ---- loading
def _read_json(path: str):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def _read_distributions(analysis_data_dir: str, tasks: Iterable[CatalogTask]) -> Dict[Tuple[str, str], Dict[str, float]]:
    """The share of students choosing each option of every closed item. A/N statements of 2024 and later are
    labelled A and B in CERMAT's files; here they are A and N like the keys."""
    formats = {(test_of(t), item): t.format for t in tasks for item in _item_names(t)}
    out = {}
    with open(os.path.join(analysis_data_dir, STATS_FILE), encoding='utf-8') as f:
        for row in csv.DictReader(f):
            key = (f"{row['year']} {row['term']}", row['item'])
            if formats.get(key) not in CLOSED_FORMATS:
                continue
            shares = {}
            for part in row['distribution_pct'].split():
                option, _, value = part.partition(':')
                if _OPTION.match(option) and value:
                    shares[option] = float(value)
            if formats[key] == 'AN' and 'B' in shares and 'N' not in shares:
                shares['N'] = shares.pop('B')
            if shares:
                out[key] = shares
    return out


def _principles(tree: dict) -> Tuple[Dict[str, Principle], Dict[str, Group]]:
    principles, groups = {}, {}
    for node, parent in topic_tree.walk(tree):
        level = topic_tree.depth(node)
        if level < 2:
            groups[node['id']] = Group(node['id'], node['name'], parent['id'] if parent else None)
        else:
            topic = parent['id']
            principles[node['id']] = Principle(
                node['id'], node['name'], node.get('note', ''), node.get('kind', ''), topic,
                groups[topic].parent, list(node.get('requires', [])), len(principles))
    return principles, groups


def _flows(raw: dict) -> List[Flow]:
    """The flows as written, tolerating missing fields so that validation can name them."""
    flows = []
    for test, tasks in raw.items():
        for number, g in (tasks or {}).items():
            routes = []
            for r in g.get('postupy') or []:
                steps = [Step(s.get('id', ''), list(s.get('vstupy') or []), s.get('vysledek', ''),
                              s.get('princip', ''), s.get('odpoved')) for s in r.get('kroky') or []]
                routes.append(Route(r.get('id', ''), r.get('nazev', ''), steps))
            b = g.get('bodovani')
            scoring = Scoring(
                b.get('typ', ''), {str(k): v for k, v in (b.get('body') or {}).items()},
                [Partial(p.get('polozka', ''), p.get('krok', ''), p.get('body', 0)) for p in b.get('dilci') or []],
                b.get('poznamka', ''),
            ) if b else None
            k = g.get('kontrola') or {}
            review = Review(k.get('odpovedi', ''), k.get('kroky', ''), k.get('principy', ''), list(k.get('poznamky') or []))
            given = [Given(z.get('id', ''), z.get('text', '')) for z in g.get('zadani') or []]
            flows.append(Flow(test, int(number) if str(number).isdigit() else 0, given, routes, scoring, review))
    return flows


def load_release(analysis_data_dir: str) -> Release:
    """Reads every input, checks that they fit together and derives what the steps imply.
    Raises InvalidRelease listing every problem."""
    tree = topic_tree.load_tree(os.path.join(analysis_data_dir, topic_tree.REBUILT_DIR))
    principles, groups = _principles(tree)
    catalog = load_catalog(analysis_data_dir)
    graph_dir = os.path.join(analysis_data_dir, GRAPH_DIR)
    raw_errors = _read_json(os.path.join(graph_dir, MISCONCEPTIONS_FILE))
    dependents = collections.defaultdict(list)
    for p in principles.values():
        for q in p.requires:
            dependents[q].append(p.id)

    release = Release(
        principles=principles,
        groups=groups,
        dependents=dict(dependents),
        tasks={t.problem_id: t for t in catalog},
        solutions=_read_json(os.path.join(analysis_data_dir, SOLUTIONS_FILE)),
        distributions=_read_distributions(analysis_data_dir, catalog),
        flows={},
        misconceptions=[Misconception(m.get('id', ''), m.get('nazev', ''), m.get('princip', ''), m.get('popis', ''),
                                      [Evidence(d.get('test', ''), d.get('polozka', ''), d.get('moznost', ''))
                                       for d in m.get('doklady') or []], m.get('stav', ''))
                        for m in raw_errors.get('chyby', [])],
        unexplained=[Unexplained(u.get('test', ''), u.get('polozka', ''), u.get('moznost', ''), u.get('poznamka', ''))
                     for u in raw_errors.get('nevysvetlene', [])],
    )
    errors = []
    for flow in _flows(_read_json(os.path.join(graph_dir, GRAPHS_FILE))):
        if flow.task < 1 or len(flow.test.split()) != 2:
            errors.append(f'{flow.test}: a task must be named by its number')
        elif flow.problem_id in release.flows:
            errors.append(f'{flow.test} {flow.task}: written twice')
        else:
            release.flows[flow.problem_id] = flow
    errors += validate(release)
    if errors:
        raise InvalidRelease(errors)
    for flow in release.flows.values():
        task = release.tasks[flow.problem_id]
        for route in flow.routes:
            _derive(route, _item_names(task))
    return release


# ---- validation
def validate(release: Release) -> List[str]:
    """Every problem in how the inputs fit together; empty when the release is sound."""
    errors: List[str] = []
    p = release.principles

    # the rebuilt tree: prerequisites exist and form no cycle
    for principle in p.values():
        for q in principle.requires:
            if q not in p:
                errors.append(f'{principle.id} requires unknown principle {q}')
    state: Dict[str, int] = {}

    def visit(pid: str) -> bool:
        if state.get(pid) == 1:
            return False
        if state.get(pid) == 2:
            return True
        state[pid] = 1
        ok = all(visit(q) for q in p[pid].requires if q in p)
        state[pid] = 2
        return ok

    if not all(visit(pid) for pid in p):
        errors.append('the prerequisite links of the rebuilt tree form a cycle')

    # the solutions file covers the catalogued items
    for task in release.tasks.values():
        stored = release.solutions.get(test_of(task), {})
        for name in _item_names(task):
            record = stored.get(name)
            if record is None:
                errors.append(f'{test_of(task)} {name}: no solution in {SOLUTIONS_FILE}')
                continue
            for pid in record.get('principy', []):
                if pid not in p:
                    errors.append(f'{test_of(task)} {name}: stored principle {pid} is not in the rebuilt tree')

    totals = collections.defaultdict(float)
    for flow in release.flows.values():
        where = f'{flow.test} {flow.task}'
        task = release.tasks.get(flow.problem_id)
        if task is None:
            errors.append(f'{where}: no such task in the catalog')
            continue
        items = _item_names(task)
        errors += _validate_flow(flow, items, p, where)
        if flow.scoring:
            scoring_errors = _validate_scoring(flow, task, where)
            errors += scoring_errors
            if not scoring_errors:
                totals[flow.test] += flow.scoring.max_points
        if flow.review.answers not in ANSWER_STATES:
            errors.append(f'{where}: kontrola.odpovedi must be one of {", ".join(ANSWER_STATES)}')
        for state_name, value in (('kroky', flow.review.steps), ('principy', flow.review.principles)):
            if value not in REVIEW_STATES:
                errors.append(f'{where}: kontrola.{state_name} must be one of {", ".join(REVIEW_STATES)}')

    # a test whose every task is scored must come to 50 points
    scored = collections.Counter(f.test for f in release.flows.values() if f.scoring)
    for test, count in scored.items():
        if count == TASKS_PER_TEST and totals[test] != TEST_POINTS:
            errors.append(f'{test}: the scoring of its 16 tasks totals {totals[test]:g} points, not {TEST_POINTS}')

    # misconceptions and unexplained options point at wrong options of closed items
    ids = [m.id for m in release.misconceptions]
    for dup in {i for i in ids if ids.count(i) > 1}:
        errors.append(f'misconception {dup} is listed twice')
    for m in release.misconceptions:
        if not m.id or not m.name or not m.description:
            errors.append(f'misconception {m.id or "?"}: id, nazev and popis are required')
        if m.principle not in p:
            errors.append(f'misconception {m.id}: unknown principle {m.principle}')
        if m.state not in REVIEW_STATES:
            errors.append(f'misconception {m.id}: stav must be one of {", ".join(REVIEW_STATES)}')
        if not m.evidence:
            errors.append(f'misconception {m.id}: no evidence')
        for e in m.evidence:
            errors += _validate_option(release, e.test, e.item, e.option, f'misconception {m.id}')
    for u in release.unexplained:
        errors += _validate_option(release, u.test, u.item, u.option, 'unexplained option')
    return errors


def _validate_flow(flow: Flow, items: List[str], principles: Dict[str, Principle], where: str) -> List[str]:
    errors = []
    given = [g.id for g in flow.given]
    if not flow.given:
        errors.append(f'{where}: no given facts (zadani)')
    if len(set(given)) != len(given) or not all(given):
        errors.append(f'{where}: the ids of the given facts must be unique and not empty')
    if not flow.routes:
        errors.append(f'{where}: no route')
    route_ids = [r.id for r in flow.routes]
    if len(set(route_ids)) != len(route_ids) or not all(route_ids):
        errors.append(f'{where}: the route ids must be unique and not empty')
    for route in flow.routes:
        at = f'{where}, route {route.id}'
        if not route.name:
            errors.append(f'{at}: no name (nazev)')
        known = set(given)
        answered = collections.Counter()
        for step in route.steps:
            if not step.id or step.id in known:
                errors.append(f'{at}: step id {step.id!r} is empty or used twice')
            if not step.inputs:
                errors.append(f'{at}, {step.id}: no inputs')
            for i in step.inputs:
                if i not in known:
                    errors.append(f'{at}, {step.id}: input {i} is neither a given fact nor an earlier step')
            if not step.result:
                errors.append(f'{at}, {step.id}: no result')
            if step.principle not in principles:
                errors.append(f'{at}, {step.id}: unknown principle {step.principle!r}')
            if step.answer is not None:
                if step.answer not in items:
                    errors.append(f'{at}, {step.id}: answers {step.answer}, which is not an item of the task')
                answered[step.answer] += 1
            known.add(step.id)
        for item in items:
            if answered[item] != 1:
                errors.append(f'{at}: item {item} is answered {answered[item]} times, not once')
        # every step leads to some answer
        needed = set()
        for step in reversed(route.steps):
            if step.answer is not None or step.id in needed:
                needed.add(step.id)
                needed.update(step.inputs)
        for step in route.steps:
            if step.id not in needed:
                errors.append(f'{at}, {step.id}: no answer depends on it')
    return errors


def _validate_scoring(flow: Flow, task: CatalogTask, where: str) -> List[str]:
    s, items = flow.scoring, _item_names(task)
    errors = []
    if s.kind not in SCORING_KINDS:
        return [f'{where}: bodovani.typ must be one of {", ".join(SCORING_KINDS)}']
    if not isinstance(s.note, str):
        errors.append(f'{where}: bodovani.poznamka must be text')
    if not all(isinstance(v, (int, float)) and v >= 0 for v in s.points.values()):
        return [f'{where}: the points of bodovani must be numbers']
    if s.kind == 'soucet':
        if sorted(s.points, key=item_order) != items:
            errors.append(f'{where}: bodovani.body must give points to exactly the items {", ".join(items)}')
        else:
            for item in task.items:
                if s.points[item.name] != item.points:
                    errors.append(f'{where}: {item.name} has {s.points[item.name]:g} points, the catalog says {item.points:g}')
    else:
        counts = sorted(int(k) for k in s.points if k.isdigit())
        if len(counts) != len(s.points) or not counts or counts[-1] > len(items):
            errors.append(f'{where}: bodovani.body must map numbers of correct items (0–{len(items)}) to points')
        elif [s.points[str(c)] for c in counts] != sorted(s.points[str(c)] for c in counts):
            errors.append(f'{where}: more correct items must not give fewer points')
    if s.max_points != task.points:
        errors.append(f'{where}: the scoring gives at most {s.max_points:g} points, the catalog says {task.points}')
    main = flow.routes[0] if flow.routes else None
    for part in s.partial:
        if part.item not in items:
            errors.append(f'{where}: partial points for {part.item}, which is not an item of the task')
        elif main and part.step not in {st.id for st in main.steps}:
            errors.append(f'{where}: partial points for step {part.step}, which is not in the first route')
        elif s.kind == 'soucet' and not 0 < part.points < s.points.get(part.item, 0):
            errors.append(f'{where}: partial points for {part.item} must be fewer than the item gives')
    return errors


def _validate_option(release: Release, test: str, item: str, option: str, what: str) -> List[str]:
    task = next((t for t in release.tasks.values() if test_of(t) == test and item in _item_names(t)), None)
    if task is None:
        return [f'{what}: {test} {item} is not an item of the catalog']
    if task.format not in CLOSED_FORMATS:
        return [f'{what}: {test} {item} is not a closed item']
    shares = release.distributions.get((test, item))
    if not shares or option not in shares:
        return [f'{what}: {test} {item} has no option {option} in CERMAT\'s results']
    if _keys(task).get(item) == option:
        return [f'{what}: {test} {item} {option} is the correct answer']
    return []


# ---- derivation
def _derive(route: Route, items: List[str]) -> None:
    """Gives every step its item and every item its own steps, reused results and principles."""
    by_id = {s.id: s for s in route.steps}
    order = {s.id: n for n, s in enumerate(route.steps)}
    answer = {s.answer: s.id for s in route.steps if s.answer}

    def behind(step_id: str, found: set) -> set:
        found.add(step_id)
        for i in by_id[step_id].inputs:
            if i in by_id and i not in found:
                behind(i, found)
        return found

    for item in sorted(items, key=item_order):
        for step_id in behind(answer[item], set()):
            if not by_id[step_id].item:
                by_id[step_id].item = item
    route.items = []
    for item in sorted(items, key=item_order):
        own = sorted((s for s in route.steps if s.item == item), key=lambda s: order[s.id])
        reused = sorted({i for s in own for i in s.inputs if i in by_id and by_id[i].item != item}, key=order.get)
        for step_id in reused:
            by_id[step_id].reused_by.append(item)
        earlier = set().union(*(behind(i, set()) for i in reused)) if reused else set()
        route.items.append(ItemSteps(
            item, [s.id for s in own], [Reuse(i, by_id[i].item) for i in reused],
            list(dict.fromkeys(s.principle for s in own)),
            list(dict.fromkeys(by_id[i].principle for i in sorted(earlier, key=order.get)))))


# ---- what the pages read
def stored_principles(release: Release, test: str, item: str) -> List[str]:
    return list(release.solutions.get(test, {}).get(item, {}).get('principy', []))


def item_principles(release: Release, test: str, item: str) -> Tuple[List[str], str]:
    """The principles an item needs: derived from the first route's steps where the task has steps,
    otherwise the stored list. With where they come from: 'kroky' or 'seznam'."""
    flow = release.flows.get(problem_id(test, item_order(item)[0]))
    if flow:
        for derived in flow.routes[0].items:
            if derived.item == item:
                return derived.principles, 'kroky'
    return stored_principles(release, test, item), 'seznam'


def _differences(release: Release, test: str, d: ItemSteps) -> Tuple[List[str], List[str], List[str]]:
    """How an item's derived list differs from its stored one: principles its own steps apply that the
    stored list lacks; stored principles applied by no step it depends on; and stored principles applied
    only by a step it reuses from an earlier item (expected: the reused result is the earlier item's)."""
    stored = stored_principles(release, test, d.item)
    missing = [q for q in d.principles if q not in stored]
    extra = [q for q in stored if q not in d.principles and q not in d.behind]
    extra_reused = [q for q in stored if q not in d.principles and q in d.behind]
    return missing, extra, extra_reused


def _principle_ref(release: Release, pid: str) -> dict:
    p = release.principles[pid]
    return {'id': pid, 'name': p.name, 'topic': release.groups[p.topic].name}


@dataclass
class TaskEntry:
    id: str                         # M9-2025-B-08
    test: str                       # "2025 B"
    task: int
    format: str
    points: int
    description: str
    success_pct: Optional[float]
    items: int
    stepped: bool                   # it has a solution flow
    main: Optional[str]             # the main principle of its first item (the first of the stored list)


def index(release: Release) -> dict:
    """Everything the page lists: the tests, every task, every principle with its topic and area."""
    tests = list(dict.fromkeys(test_of(t) for t in release.tasks.values()))
    tasks = [TaskEntry(t.problem_id, test_of(t), t.task, t.format, t.points, t.description, t.success_pct,
                       len(t.items), t.problem_id in release.flows,
                       (stored_principles(release, test_of(t), _item_names(t)[0]) or [None])[0])
             for t in release.tasks.values()]
    used = collections.Counter(pid for t in release.tasks.values() for i in _item_names(t)
                               for pid in item_principles(release, test_of(t), i)[0])
    principles = [{'id': p.id, 'name': p.name, 'topic': p.topic, 'area': p.area, 'requires': p.requires,
                   'items': used[p.id]} for p in release.principles.values()]
    groups = [{'id': g.id, 'name': g.name, 'parent': g.parent} for g in release.groups.values()]
    return {'tests': tests, 'tasks': tasks, 'principles': principles, 'groups': groups}


def _options(release: Release, task: CatalogTask) -> List[dict]:
    """The answer shares of each closed item, with the misconception or the note each wrong option has."""
    revealed = {(e.test, e.item, e.option): m.id for m in release.misconceptions for e in m.evidence}
    unexplained = {(u.test, u.item, u.option): u.note for u in release.unexplained}
    keys, test = _keys(task), test_of(task)
    out = []
    for name in _item_names(task):
        shares = release.distributions.get((test, name))
        if not shares:
            continue
        out.append({'item': name, 'key': keys.get(name), 'options': [
            {'option': o, 'share': v, 'key': o == keys.get(name), 'misconception': revealed.get((test, name, o)),
             'unexplained': unexplained.get((test, name, o))}
            for o, v in sorted(shares.items())]})
    return out


def _misconception_view(release: Release, m: Misconception) -> dict:
    evidence = []
    for e in m.evidence:
        task = next(t for t in release.tasks.values() if test_of(t) == e.test and e.item in _item_names(t))
        shares = release.distributions[(e.test, e.item)]
        key = _keys(task).get(e.item)
        evidence.append({'test': e.test, 'item': e.item, 'option': e.option, 'share': shares[e.option],
                         'key': key, 'key_share': shares.get(key), 'problem_id': task.problem_id})
    return {'id': m.id, 'name': m.name, 'description': m.description, 'state': m.state,
            'principle': _principle_ref(release, m.principle), 'evidence': evidence}


def task_view(release: Release, pid: str) -> dict:
    """One task: its items with their answers and results, the stored solution lines and lists, and where
    it has steps, the flow of every route with what each item reuses and how its derived list differs
    from the stored one; the shares of its options and the misconceptions they reveal."""
    task = release.tasks[pid]
    test = test_of(task)
    keys = _keys(task)
    flow = release.flows.get(pid)
    items = []
    for item in task.items:
        stored = release.solutions[test][item.name]
        items.append({'item': item.name, 'points': item.points, 'success_pct': item.success_pct,
                      'key': keys.get(item.name), 'solution': stored['reseni'],
                      'stored': [_principle_ref(release, q) for q in stored['principy']]})
    view = {
        'id': pid, 'test': test, 'task': task.task, 'format': task.format, 'points': task.points,
        'description': task.description, 'success_pct': task.success_pct, 'skipped_pct': task.skipped_pct,
        'screenshot': f'{pid}.png', 'key_screenshot': f'{pid}-reseni.png',
        'items': items, 'stepped': flow is not None, 'given': [], 'routes': [], 'scoring': None, 'review': None,
        'options': _options(release, task),
    }
    shown = {o['misconception'] for item in view['options'] for o in item['options'] if o['misconception']}
    view['misconceptions'] = [_misconception_view(release, m) for m in release.misconceptions if m.id in shown]
    if not flow:
        return view
    view['given'] = [{'id': g.id, 'text': g.text} for g in flow.given]
    for route in flow.routes:
        derived = []
        for d in route.items:
            missing, extra, extra_reused = _differences(release, test, d)
            derived.append({
                'item': d.item, 'steps': d.steps, 'reused': [{'step': r.step, 'item': r.item} for r in d.reused],
                'principles': [_principle_ref(release, q) for q in d.principles],
                'missing': missing, 'extra': extra, 'extra_reused': extra_reused,
            })
        view['routes'].append({
            'id': route.id, 'name': route.name, 'items': derived,
            'steps': [{'id': s.id, 'inputs': s.inputs, 'result': s.result, 'answer': s.answer, 'item': s.item,
                       'reused_by': s.reused_by, 'principle': _principle_ref(release, s.principle)}
                      for s in route.steps]})
    s = flow.scoring
    view['scoring'] = s and {'kind': s.kind, 'points': s.points, 'max_points': s.max_points, 'note': s.note,
                             'partial': [{'item': x.item, 'step': x.step, 'points': x.points} for x in s.partial]}
    view['review'] = {'answers': flow.review.answers, 'steps': flow.review.steps,
                      'principles': flow.review.principles, 'notes': flow.review.notes}
    return view


def principle_view(release: Release, pid: str) -> dict:
    """One principle: what it needs and what builds on it directly, its misconceptions, the steps that
    apply it and the items that need it."""
    p = release.principles[pid]
    steps = []
    for flow in release.flows.values():
        for n, route in enumerate(flow.routes):
            for s in route.steps:
                if s.principle == pid:
                    steps.append({'problem_id': flow.problem_id, 'test': flow.test, 'task': flow.task,
                                  'route': route.id, 'route_name': route.name, 'main_route': n == 0,
                                  'step': s.id, 'result': s.result, 'item': s.item})
    items = []
    for task in release.tasks.values():
        test = test_of(task)
        for item in task.items:
            used, source = item_principles(release, test, item.name)
            stored = stored_principles(release, test, item.name)
            if pid in used or pid in stored:
                items.append({'test': test, 'item': item.name, 'problem_id': task.problem_id,
                              'success_pct': item.success_pct, 'points': item.points,
                              'main': bool(stored) and stored[0] == pid, 'source': source,
                              'in_steps': source == 'kroky' and pid in used, 'in_list': pid in stored})
    counted = [i for i in items if i['source'] == 'seznam' or i['in_steps']]
    return {
        'id': pid, 'name': p.name, 'note': p.note, 'kind': p.kind,
        'topic': {'id': p.topic, 'name': release.groups[p.topic].name},
        'area': {'id': p.area, 'name': release.groups[p.area].name},
        'requires': [_principle_ref(release, q) for q in p.requires],
        'required_by': [_principle_ref(release, q) for q in release.dependents.get(pid, [])],
        'misconceptions': [_misconception_view(release, m) for m in release.misconceptions if m.principle == pid],
        'steps': steps, 'items': items,
        'tests': len({i['test'] for i in counted}), 'points': sum(i['points'] for i in counted),
    }


def _main_topic(release: Release, task: CatalogTask) -> Optional[str]:
    """The topic of the main principle of a task's first item: the first one of its stored list."""
    stored = stored_principles(release, test_of(task), _item_names(task)[0])
    return release.principles[stored[0]].topic if stored else None


def slot_template(release: Release) -> List[dict]:
    """For every task number, which topics and areas its main principle comes from across the tests."""
    slots = []
    numbers = sorted({t.task for t in release.tasks.values()})
    for n in numbers:
        topics = collections.Counter(_main_topic(release, t) for t in release.tasks.values() if t.task == n)
        topics.pop(None, None)
        areas = collections.Counter()
        for topic, count in topics.items():
            areas[release.groups[topic].parent] += count
        total = sum(topics.values())
        top, top_count = topics.most_common(1)[0]
        slots.append({
            'task': n, 'tests': total, 'fixed': top_count / total >= FIXED_SLOT_SHARE,
            'topics': [{'id': t, 'name': release.groups[t].name, 'count': c} for t, c in topics.most_common()],
            'areas': [{'id': a, 'name': release.groups[a].name, 'count': c} for a, c in areas.most_common()],
        })
    return slots


def coverage(release: Release) -> List[dict]:
    """For every principle: in how many tests, items and points it is needed (an item's points count in
    full for each of its principles, so the points of two principles must not be added)."""
    tests, items, points = collections.defaultdict(set), collections.Counter(), collections.Counter()
    for task in release.tasks.values():
        test = test_of(task)
        for item in task.items:
            for pid in item_principles(release, test, item.name)[0]:
                tests[pid].add(test)
                items[pid] += 1
                points[pid] += item.points
    return [{'id': pid, 'tests': len(tests[pid]), 'items': items[pid], 'points': points[pid]}
            for pid in release.principles]


def exam_view(release: Release, test: str) -> dict:
    """One test against all of them: the slot template, the coverage of every principle, and the test's own
    tasks and items with the principles each needs (an item × principle incidence)."""
    tasks = [t for t in release.tasks.values() if test_of(t) == test]
    if not tasks:
        raise KeyError(test)
    rows, used = [], set()
    for task in tasks:
        flow = release.flows.get(task.problem_id)
        for item in task.items:
            principles, source = item_principles(release, test, item.name)
            stored = stored_principles(release, test, item.name)
            used.update(principles)
            rows.append({'task': task.task, 'item': item.name, 'problem_id': task.problem_id, 'points': item.points,
                         'success_pct': item.success_pct, 'source': source, 'principles': principles,
                         'main': stored[0] if stored else None})
    scored = [release.flows[t.problem_id].scoring for t in tasks
              if t.problem_id in release.flows and release.flows[t.problem_id].scoring]
    return {
        'test': test,
        'tasks': [{'task': t.task, 'id': t.problem_id, 'format': t.format, 'points': t.points,
                   'description': t.description, 'success_pct': t.success_pct, 'topic': _main_topic(release, t),
                   'stepped': t.problem_id in release.flows} for t in tasks],
        'points': sum(t.points for t in tasks),
        'scored_tasks': len(scored),
        'rows': rows,
        'principles': [pid for pid in release.principles if pid in used],
        'template': slot_template(release),
        'coverage': coverage(release),
    }


def review_list(release: Release) -> List[dict]:
    """Every open question for the owner, most specific first: principle lists that differ from the steps,
    answers not checked against a key, notes, proposed misconceptions, unexplained and unexamined wrong
    options, and the flows waiting for review."""
    out = []
    for flow in release.flows.values():
        for d in flow.routes[0].items:
            missing, extra, extra_reused = _differences(release, flow.test, d)
            if missing or extra or extra_reused:
                out.append({'kind': 'rozdil-principu', 'problem_id': flow.problem_id,
                            'ref': f'{flow.test} {d.item}', 'missing': missing, 'extra': extra,
                            'extra_reused': extra_reused,
                            'reused': [{'step': r.step, 'item': r.item} for r in d.reused]})
    for flow in release.flows.values():
        if flow.review.answers != 'shoda-s-klicem':
            out.append({'kind': 'odpoved', 'problem_id': flow.problem_id, 'ref': f'{flow.test} {flow.task}',
                        'state': flow.review.answers})
        for note in flow.review.notes:
            out.append({'kind': 'poznamka', 'problem_id': flow.problem_id, 'ref': f'{flow.test} {flow.task}',
                        'text': note})
    for m in release.misconceptions:
        if m.state == 'navrh':
            out.append({'kind': 'chyba', 'id': m.id, 'name': m.name,
                        'refs': [f'{e.test} {e.item} {e.option}' for e in m.evidence]})
    for u in release.unexplained:
        out.append({'kind': 'nevysvetleno', 'ref': f'{u.test} {u.item} {u.option}', 'text': u.note,
                    'problem_id': problem_id(u.test, item_order(u.item)[0])})
    seen = {(e.test, e.item, e.option) for m in release.misconceptions for e in m.evidence}
    seen |= {(u.test, u.item, u.option) for u in release.unexplained}
    for c in distractor_candidates(release):
        if (c['test'], c['item'], c['option']) not in seen:
            out.append({'kind': 'neprozkoumano', 'ref': f"{c['test']} {c['item']} {c['option']}",
                        'problem_id': c['problem_id'], 'share': c['share'], 'key_share': c['key_share']})
    for flow in release.flows.values():
        if 'navrh' in (flow.review.steps, flow.review.principles):
            out.append({'kind': 'kroky', 'problem_id': flow.problem_id, 'ref': f'{flow.test} {flow.task}'})
    return out


def distractor_candidates(release: Release) -> List[dict]:
    """Closed items (MC and PR) where a wrong option is chosen more often than the key, the commonest first
    (analysis/graph_representation_audit.py, section 10)."""
    out = []
    for task in release.tasks.values():
        if task.format not in ('MC', 'PR'):
            continue
        test, keys = test_of(task), _keys(task)
        for name in _item_names(task):
            shares, key = release.distributions.get((test, name)), keys.get(name)
            if not shares or key not in shares:
                continue
            option, share = max(((o, v) for o, v in shares.items() if o != key), key=lambda ov: ov[1])
            if share > shares[key]:
                out.append({'test': test, 'item': name, 'problem_id': task.problem_id, 'option': option,
                            'share': share, 'key': key, 'key_share': shares[key]})
    return sorted(out, key=lambda c: c['key_share'] - c['share'])
