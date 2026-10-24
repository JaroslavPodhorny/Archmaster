"""Console editor for the tree of what the M9 test examines (m9_topic_tree.json) and for the
skills each test item needs (m9_item_skills.json).

The tree was rebuilt from the solutions of all items (analysis/graph_design_spec.md). Its assignment
is the 'principy' lists of the solved items in data/m9_item_solutions.json (and
m9_item_solutions_older.json for the tests before 2022); the editor keeps the two in step.

This file is the only thing that writes the tree and the assignment. Every edit is validated first
(ids, prerequisites that come earlier in the tree, every item of every catalogued test assigned to
existing skills, the solutions saying the same as the assignment), then saved, then the two views
are rebuilt: 04_strom_M9.md and 04_strom_M9.html.

    uv run --project backend python analysis/topic_tree.py show [ID]
    uv run --project backend python analysis/topic_tree.py assign "2025 B 15.2" SKILL [SKILL ...] [--solution TEXT]
    uv run --project backend python analysis/topic_tree.py set ID FIELD [VALUE ...]
    uv run --project backend python analysis/topic_tree.py add PARENT SLUG NAME [--kind ... --requires ...]
    uv run --project backend python analysis/topic_tree.py move ID [--parent ID] [--before ID | --after ID]
    uv run --project backend python analysis/topic_tree.py rename ID SLUG
    uv run --project backend python analysis/topic_tree.py remove ID
    uv run --project backend python analysis/topic_tree.py from-solutions
    uv run --project backend python analysis/topic_tree.py check | build
"""
import argparse, collections, functools, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from backend.core.catalog import TAGS, load_catalog  # noqa: E402
from backend.core import topic_tree as core  # noqa: E402
from backend.core.topic_tree import (ITEM_SKILLS_FILE, OLDER_FILE, STANDARD_YEARS, TREE_FILE, depth,  # noqa: E402
                                     load_item_skills, load_older, load_tree, older_uses, skills_under, walk)

DATA = os.path.join(HERE, 'data')                   # the task catalog and the solved items
KINDS = {'procedure': 'postup', 'translation': 'překlad', 'fact': 'znalost', 'strategy': 'rozbor'}
LIST_FIELDS = ('tags', 'spec', 'requires')
SKILL_FIELDS = ('name', 'kind', 'requires', 'tags', 'spec', 'note')
GROUP_FIELDS = ('name', 'tags', 'spec', 'note')
SOLUTION_FILES = ('m9_item_solutions.json', 'm9_item_solutions_older.json')   # the 20 catalogued tests, the older ones
SOLUTION_FIELDS = {'reseni', 'principy'}

# Where the tree is kept, what its views are called and what they say about how it was made.
target = dict(
    dir=DATA, path='analysis/data', md='04_strom_M9.md', html='04_strom_M9.html',
    title='Strom učiva M9',
    heading='Strom učiva M9: the principles the solutions of the test use, as a tree in learning order',
    assignment=f"""- **The assignment is what the solution of each item applies.** Every task was solved from its image and the
  result compared with the official key (`analysis/graph_design_spec.md`, section 8, names the few exceptions);
  the solutions are in `analysis/data/{SOLUTION_FILES[0]}`. An item is assigned every principle its natural
  solution applies as a step, the main one first. Which principles those are, the grouping and the
  prerequisite links are one solver's judgement, not CERMAT's.""",
    cut="""- **A leaf is one principle**: a rule, fact or method that a solution applies as a step and that a student
  either has or lacks. Fine enough to name a gap, no finer; no bundles of several rules and no bins for
  what fits nowhere else. Areas and topics only group leaves. The rules for leaves, links and the assignment
  are in `analysis/graph_design_spec.md`, sections 4–6.
- **Order is learning order.** Everything a leaf needs comes earlier; the *needs* column names the direct
  prerequisites (the editor refuses an order that breaks this). The links say what must be learned first.
  What a task needs is the list of the task itself, not the links.
- **One principle is one leaf wherever it is used.** Thaletova věta, rovnoramenný trojúhelník, výška and
  osa úhlu serve both constructions and calculations, so the properties of figures (KON) come before the
  calculations (GEO).
- **Computing and reading are separated.** Computing with fractions is in POC, fraction word problems in
  VZT. The phrases „o třetinu více než“, „kolikrát“, „o kolik procent“ recur in fractions, percentages
  and equation word problems, so they are one topic (VZT.NEZ) learned once instead of three times.""",
    older=f"""The tree was built from the 2022–2026 tests, so they fit it by construction. As a check, {{n_tests}} older tests
it was not built from ({{tests}}; booklets in `References/Matematika_starsi/`) were solved the same way from
their page images: {{n_items}} items. No official keys of these tests are in the repository, so their results are
not checked against a key. The solutions are in `data/{SOLUTION_FILES[1]}`, the assignment in
`data/{OLDER_FILE}`; they count in none of the numbers below, because the next tests will resemble
the recent ones more than the old ones.""")


# ---- the files
def save(tree, item_skills, older, solutions=None):
    os.makedirs(target['dir'], exist_ok=True)
    with open(os.path.join(target['dir'], TREE_FILE), 'w', encoding='utf-8') as f:
        json.dump(tree, f, ensure_ascii=False, indent=2)
        f.write('\n')
    for name, assignment in ((ITEM_SKILLS_FILE, item_skills), (OLDER_FILE, older)):
        tests = []
        for test, items in assignment.items():       # one line per item
            rows = ',\n'.join(f'    {json.dumps(item)}: {json.dumps(ids)}' for item, ids in items.items())
            tests.append(f'  {json.dumps(test)}: {{\n{rows}\n  }}')
        with open(os.path.join(target['dir'], name), 'w', encoding='utf-8') as f:
            f.write('{\n' + ',\n'.join(tests) + '\n}\n')
    for name, solved in zip(SOLUTION_FILES, solutions or ()):     # same layout as solving/consolidate.py writes
        with open(os.path.join(DATA, name), 'w', encoding='utf-8') as f:
            json.dump(solved, f, ensure_ascii=False, indent=1)
            f.write('\n')


def load_solutions():
    """The solved items the rebuilt assignment comes from: [the 20 catalogued tests, the older tests], each
    {"2023 A": {"6.1": {"reseni": "...", "principy": ["GEO.ROV.trojuhelnik", ...]}}}."""
    out = []
    for name in SOLUTION_FILES:
        with open(os.path.join(DATA, name), encoding='utf-8') as f:
            out.append(json.load(f))
    return out


def assignment_of(solved):
    """What a solutions file says each item needs, in the shape of m9_item_skills.json."""
    return {test: {name: list(s['principy']) for name, s in items.items()} for test, items in solved.items()}


def follow(solutions, item_skills, older):
    """Copies the assignment into the 'principy' lists, so an edit of the assignment reaches the solutions."""
    for solved, assignment in zip(solutions, (item_skills, older)):
        for test, items in assignment.items():
            for name, ids in items.items():
                if name in solved.get(test, {}):
                    solved[test][name]['principy'] = list(ids)


def find(tree, node_id):
    for node, parent in walk(tree):
        if node['id'] == node_id:
            return node, parent
    raise ValueError(f'no node {node_id}')


def siblings(tree, parent):
    return parent['children'] if parent else tree['areas']


def set_id(tree, assignments, node, new_id):
    """Gives a node (and everything under it) a new id and follows it wherever it is referred to."""
    renamed = {}

    def visit(n, nid):
        renamed[n['id']] = nid
        for child in n.get('children', []):
            visit(child, nid + '.' + child['id'].rsplit('.', 1)[1])
        n['id'] = nid
    visit(node, new_id)
    for n, _ in walk(tree):
        if 'requires' in n:
            n['requires'] = [renamed.get(q, q) for q in n['requires']]
    for assignment in assignments:
        for items in assignment.values():
            for name, ids in items.items():
                items[name] = [renamed.get(q, q) for q in ids]


# ---- the numbers: computed in backend/core/topic_tree.py, here only tied to the catalog in data/
@functools.cache
def catalog():
    return load_catalog(DATA)


def catalog_items():
    return core.catalog_items(catalog())


def uses_by_skill(item_skills):
    return core.uses_by_skill(item_skills, catalog())


def statistics(tree, item_skills):
    return core.statistics(tree, item_skills, catalog())


def screenshot(use):
    return f'../backend/data/screenshots/{use.problem_id}.png'


def solution_problems(item_skills, older, solutions):
    """Where the solved items and the assignment do not say the same."""
    found = []
    for file, solved, assignment in zip(SOLUTION_FILES, solutions, (item_skills, older)):
        for test, items in assignment.items():
            for name, ids in items.items():
                s = solved.get(test, {}).get(name)
                if not isinstance(s, dict) or set(s) != SOLUTION_FIELDS or not str(s['reseni']).strip():
                    found.append(f'{test} {name}: {file} must give its solution, as reseni and principy')
                elif s['principy'] != ids:
                    found.append(f'{test} {name}: {file} lists other principles than the assignment')
        found += [f'{test} {name}: solved in {file} but not assigned'
                  for test, items in solved.items() for name in items if name not in assignment.get(test, {})]
    return found


def problems(tree, item_skills, older, solutions=None):
    """Everything wrong with the files, as sentences; empty when they are valid."""
    found, seen = [], {}
    for node, parent in walk(tree):
        nid, d = node['id'], depth(node)
        if nid in seen:
            found.append(f'{nid}: id used twice')
        seen[nid] = node
        if d > 2 or (parent and nid.rsplit('.', 1)[0] != parent['id']) or (not parent and d):
            found.append(f'{nid}: id does not match its place in the tree')
        fields = SKILL_FIELDS if d == 2 else GROUP_FIELDS + ('children',)
        if set(node) != set(fields) | {'id'}:
            found.append(f"{nid}: fields must be exactly id, {', '.join(fields)}")
            continue
        found += [f'{nid}: unknown tag {g}' for g in node['tags'] if g not in TAGS]
        found += [f'{nid}: specification area must be 1–4, not {s}' for s in node['spec'] if s not in (1, 2, 3, 4)]
        if d < 2:
            continue
        if node['kind'] not in KINDS:
            found.append(f"{nid}: kind must be one of {', '.join(KINDS)}")
        for q in node['requires']:
            if q not in seen or depth(seen[q]) != 2 or q == nid:
                found.append(f'{nid}: prerequisite {q} must be a skill that comes earlier in the tree')
    expected = catalog_items()
    for test, items in list(item_skills.items()) + list(older.items()):
        for name, ids in items.items():
            if (test, name) not in expected and test not in older:
                found.append(f'{test} {name}: not an item of the task catalog')
            if not ids or len(set(ids)) != len(ids):
                found.append(f'{test} {name}: needs at least one skill, each listed once')
            found += [f'{test} {name}: {q} is not a skill of the tree' for q in ids
                      if q not in seen or depth(seen[q]) != 2]
    found += [f'{test} {name}: no skill assigned' for test, name in expected
              if name not in item_skills.get(test, {})]
    if solutions:
        found += solution_problems(item_skills, older, solutions)
    return found


# ---- the two views
def number(x, digits=1):
    return f'{x:.{digits}f}'.replace('.', ',')


def percent(x):
    return '–' if x is None else f'{x:.0f} %'


def outline(tree, stat, root=None):
    rows = []
    for node, _ in walk(tree):
        if root and not (node['id'] + '.').startswith(root + '.'):
            continue
        d = depth(node)
        mark = stat[node['id']]['priority'] if d == 2 else ' '
        rows.append(f"{'' if d or not rows else chr(10)}{'  ' * d}{mark} {node['name']}  [{node['id']}]")
    return '\n'.join(rows)


def markdown(tree, item_skills, older):
    (stat, uses), before = statistics(tree, item_skills), older_uses(older)
    by_id = {n['id']: n for n, _ in walk(tree)}
    parent_of = {n['id']: p for n, p in walk(tree)}
    all_skills = [n for n in by_id.values() if depth(n) == 2]
    count = collections.Counter(stat[n['id']]['priority'] for n in all_skills)
    n_items = len(catalog_items())
    glance = []
    for area in tree['areas']:
        glance.append(f"{area['id']}  {area['name']}  ({number(stat[area['id']]['points'])} b.)")
        for i, topic in enumerate(area['children']):
            last = i == len(area['children']) - 1
            glance.append(f"{'└─' if last else '├─'} {topic['name']}  ({number(stat[topic['id']]['points'])} b.)")
            glance += [f"{'   ' if last else '│  '}  {stat[s['id']]['priority']}  {s['name']}" for s in topic['children']]
        glance.append('')
    unseen = [(ref, by_id[sid]['name']) for sid, refs in before.items() if stat[sid]['priority'] == 'S' for ref in refs]
    older_note = (
        f"Every item found a place in the tree and none needed a new skill. {len(unseen)} items needed a skill "
        f"that no 2022–2026 item needs (marked S below): "
        + '; '.join(f'{ref} – {name}' for ref, name in sorted(unseen)) + '. '
        "So S skills are real exam material, only rarer; they keep the lowest priority but should not be dropped."
    ) if unseen else 'Every item found a place among the skills seen in 2022–2026.'
    older_check = target['older'].format(n_tests=len(older), tests=', '.join(older),
                                         n_items=sum(len(v) for v in older.values()))
    out = f"""# {target['heading']}

Generated from `{target['path']}/{TREE_FILE}` and `{target['path']}/{ITEM_SKILLS_FILE}`; change them
with `analysis/topic_tree.py`, not here. The tree has {len(tree['areas'])} areas, {sum(depth(n) == 1 for n in by_id.values())} topics and {len(all_skills)} skills.
Every one of the {n_items} scored items (sub-items such as 15.2, or whole tasks) of the 20 tests of
2022–2026 is assigned to the skills it needs.

What rests on what:

{target['assignment']}
- **Numbers are computed, not estimated**: points from the catalog, success rates from CERMAT's
  published item results.
- **Skills marked S** are quoted from CERMAT's specification (`References/MASPECIFIKACEPOZADAVKU2022 (1).pdf`,
  parts A1, B1, C1; C1 says a candidate must also know A1 and B1) and are needed by no item of the 20
  tests. The specification's four areas are 1 Číslo a proměnná, 2 Závislosti, vztahy a práce s daty,
  3 Geometrie v rovině a prostoru, 4 Nestandardní aplikační úlohy a problémy.

## How the tree is cut

{target['cut']}
- Not in the tree: the rules for how answers must look and the list of what is not printed in the
  booklet ([03_ucivo_M9.md](03_ucivo_M9.md), section 0). They apply to every leaf.

## How to read the columns

- **P, priority**, from how often a skill is needed, directly or through a skill that builds on it. A
  foundation therefore never ranks below what stands on it: „pořadí operací“ is needed by few items by name,
  but nearly every computation rests on it. "Standard tests" are the 16 tests of {', '.join(map(str, STANDARD_YEARS))}; the four
  2024 tests follow a different design and do not count here.
  **1** = needed in at least 10 of the 16 standard tests, or in at least 6 of the 8 tests of 2025–2026 ({count['1']} skills) ·
  **2** = in at least 4 of 16, or 3 of the last 8 ({count['2']}) · **3** = rarer, or only in 2024 ({count['3']}) ·
  **S** = in the specification, needed by no item of 2022–2026 ({count['S']}); where one occurred in an older
  test, its note says so.
- **Tests** = in how many of the 16 standard tests an item needs the skill itself, and after the dot in how
  many of the 8 tests of 2025–2026. A skill that is 2 · 2 is new; one that is 6 · 0 has not come back.
- **Points** = points per standard test that depend on the skill: the full points of every item that
  needs it. An item needing three skills counts for each, so the column does not add up to 50; the
  figures given for topics and areas count each item once.
- **With what builds on it** = the same three numbers (tests · recent tests · points) counting also the
  items that need a skill resting on this one, following the *needs* links. Empty when nothing builds on
  the skill. This is what the priority is taken from, and it is only as good as those links.
- **Success** = points-weighted average success of those items in the regular terms (A, B) of all five
  years. It is the success of the items, not of the skill alone: an item can fail on another skill it needs.
- **Hardest** = the three least solved items (regular terms) in which the skill is the main one. Being
  able to solve these is what "mastered" means for the skill.
- **Kind** says how the skill is practised: *postup* – a procedure, drilled until fast and error-free ·
  *překlad* – turning the Czech wording into mathematics · *znalost* – a fact or property known by heart ·
  *rozbor* – finding the route through a multi-step task.

## Check against tests from before 2022

{older_check}

{older_note}

## The tree at a glance

Points per standard test in brackets (each item counted once per topic).

```
{chr(10).join(glance[:-1])}
```
""".split('\n')

    def link(u):
        return f'[{u.ref}]({screenshot(u)}) {u.success_pct:.0f} %'

    for area in tree['areas']:
        st = stat[area['id']]
        out += [f"## {area['name']} ({area['id']})", '',
                f"{number(st['points'])} points per standard test · success {percent(st['success'])} · {area['note']}", '']
        for topic in area['children']:
            st = stat[topic['id']]
            out += [f"### {topic['name']}", '',
                    f"`{topic['id']}` · {number(st['points'])} points per standard test, in {st['tests']} of 16 · "
                    f"success {percent(st['success'])} · specification area {', '.join(map(str, topic['spec']))}"
                    + (f" · {topic['note']}" if topic['note'] else ''), '',
                    '| P | Skill | Kind | Needs | Tests | Points | With what builds on it | Success | Hardest | Note |',
                    '|---|---|---|---|---|---|---|---|---|---|']
            for n in topic['children']:
                st = stat[n['id']]
                needs = ', '.join(f"{by_id[q]['name'].split(':')[0].split(',')[0]} ({parent_of[q]['id']})"
                                  for q in n['requires'])
                seen = st['items'] > 0
                out.append(' | '.join([
                    f"| {st['priority']}", n['name'], KINDS[n['kind']], needs,
                    f"{st['tests']} · {st['recent']}" if seen else '',
                    number(st['points']) if seen else '',
                    f"{st['reach_tests']} · {st['reach_recent']} · {number(st['reach_points'])}" if st['dependents'] else '',
                    percent(st['success']) if seen else '',
                    ' · '.join(link(u) for u in st['hardest']),
                    n['note'] + (f" **Before 2022: {', '.join(before[n['id']])}.**" if before[n['id']] and not seen else '')])
                    + ' |')
            out.append('')
    return '\n'.join(out)


def view_page(tree, item_skills, older):
    """One self-contained page; the screenshots are linked, not embedded."""
    (stat, uses), before = statistics(tree, item_skills), older_uses(older)
    rows = []
    for n, parent in walk(tree):
        mine = sorted({u.ref: u for s in skills_under(n) for u in uses[s['id']]}.values(),
                      key=lambda u: (u.year, u.term, u.task, u.item))
        st = stat[n['id']]
        rows.append({
            'id': n['id'], 'parent': parent['id'] if parent else '', 'name': n['name'],
            'kind': KINDS.get(n.get('kind'), ''), 'requires': n.get('requires', []),
            'spec': ', '.join(map(str, n['spec'])), 'note': n['note'],
            'priority': st['priority'], 'items': st['items'], 'tests': st['tests'], 'recent': st['recent'],
            'points': number(st['points']), 'success': None if st['success'] is None else round(st['success']),
            'hardest': [u.ref for u in st['hardest']], 'older': before[n['id']],
            'dependents': st.get('dependents', 0), 'reach': [st.get('reach_tests'), st.get('reach_recent'),
                                                             number(st.get('reach_points', 0))],
            'ex': [{'ref': u.ref, 'pct': None if u.success_pct is None else round(u.success_pct),
                    'png': screenshot(u), 'main': u.main} for u in mine] if depth(n) == 2 else []})
    with open(os.path.join(HERE, 'tree_view_template.html'), encoding='utf-8') as f:
        return f.read().replace('<title>Strom učiva M9</title>', f"<title>{target['title']}</title>") \
            .replace('/*DATA*/', json.dumps(rows, ensure_ascii=False))


def build(tree, item_skills, older):
    for name, text in ((target['md'], markdown(tree, item_skills, older)),
                       (target['html'], view_page(tree, item_skills, older))):
        with open(os.path.join(HERE, name), 'w', encoding='utf-8') as f:
            f.write(text)


# ---- edits (each changes the data in memory; main() validates, saves and rebuilds)
def edit_assign(tree, item_skills, older, a, solutions=None):
    year, term, name = a.item.split()
    test = f'{year} {term}'
    in_older = test in older or (test not in item_skills and (test, name) not in catalog_items())
    (older if in_older else item_skills).setdefault(test, {})[name] = a.skills
    if a.solution:                                   # a new or corrected solution; the principles follow in main()
        solutions[in_older].setdefault(test, {})[name] = {'reseni': ' '.join(a.solution), 'principy': a.skills}


def edit_set(tree, item_skills, older, a):
    node, _ = find(tree, a.id)
    if a.field not in (SKILL_FIELDS if depth(node) == 2 else GROUP_FIELDS):
        raise ValueError(f'{a.id} has no field {a.field}')
    node[a.field] = [int(v) for v in a.value] if a.field == 'spec' else \
        list(a.value) if a.field in LIST_FIELDS else ' '.join(a.value)


def place(tree, node, parent, before, after):
    target = siblings(tree, parent)
    anchor = before or after
    if anchor:
        at = [n['id'] for n in target].index(anchor) + (1 if after else 0)   # ValueError if not a sibling
        target.insert(at, node)
    else:
        target.append(node)


def edit_add(tree, item_skills, older, a):
    parent = find(tree, a.parent)[0] if a.parent != '-' else None
    node = {'id': f"{parent['id']}.{a.slug}" if parent else a.slug, 'name': a.name}
    if parent and depth(parent) == 1:
        node.update(kind=a.kind, requires=a.requires)
    node.update(tags=a.tags or (parent['tags'] if parent else []),
                spec=a.spec or (parent['spec'] if parent else []), note=a.note)
    if not parent or depth(parent) == 0:
        node['children'] = []
    place(tree, node, parent, a.before, None)


def edit_move(tree, item_skills, older, a):
    node, parent = find(tree, a.id)
    new_parent = find(tree, a.parent)[0] if a.parent else parent
    if (depth(new_parent) if new_parent else -1) != depth(node) - 1:
        raise ValueError('a skill moves under a topic, a topic under an area')
    siblings(tree, parent).remove(node)
    place(tree, node, new_parent, a.before, a.after)
    if new_parent is not parent:
        set_id(tree, (item_skills, older), node, new_parent['id'] + '.' + node['id'].rsplit('.', 1)[1])


def edit_rename(tree, item_skills, older, a):
    node, parent = find(tree, a.id)
    set_id(tree, (item_skills, older), node, f"{parent['id']}.{a.slug}" if parent else a.slug)


def edit_remove(tree, item_skills, older, a):
    node, parent = find(tree, a.id)
    gone = {n['id'] for n in skills_under(node)}
    users = [n['id'] for n, _ in walk(tree) if n['id'] not in gone and gone & set(n.get('requires', []))]
    if users:
        raise ValueError(f"still a prerequisite of {', '.join(users)}")
    assigned = [ref for s in gone for ref in [u.ref for u in uses_by_skill(item_skills)[s]] + older_uses(older)[s]]
    if assigned:
        raise ValueError(f"still assigned to {len(assigned)} items, e.g. {', '.join(assigned[:5])}")
    siblings(tree, parent).remove(node)


def show(tree, item_skills, older, node_id):
    stat, uses = statistics(tree, item_skills)
    if not node_id:
        return outline(tree, stat)
    node, _ = find(tree, node_id)
    if depth(node) < 2:
        return outline(tree, stat, node_id)
    st = stat[node_id]
    rows = list(node.items()) + [
        ('needed by', [n['id'] for n, _ in walk(tree) if node_id in n.get('requires', [])]),
        ('priority', st['priority']),
        ('in tests', f"{st['tests']} of 16 standard, {st['recent']} of the last 8"),
        ('points', f"{number(st['points'])} per standard test"),
        ('reach', f"with the {st['dependents']} skills that build on it: {st['reach_tests']} of 16, "
                  f"{st['reach_recent']} of the last 8, {number(st['reach_points'])} points"),
        ('success', percent(st['success'])),
        ('items', ', '.join(u.ref + ('' if u.main else '*') for u in uses[node_id]) + '   (* = not the main skill)'),
        ('pre-2022', ', '.join(older_uses(older)[node_id]) or '–')]
    return '\n'.join(f'{k:9s} {v}' for k, v in rows)


def main():
    p = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    sub = p.add_subparsers(dest='cmd', required=True)
    sub.add_parser('check', help='validate the tree, the assignment and the solutions')
    sub.add_parser('build', help='rebuild the two views (04_strom_M9.md and .html)')
    sub.add_parser('from-solutions', help='take the assignment from the principy lists of the solutions files')
    c = sub.add_parser('show', help='print the tree, one branch, or one skill with its items')
    c.add_argument('id', nargs='?')
    c = sub.add_parser('assign', help='set the skills an item needs, the main one first')
    c.add_argument('item', help='quoted, e.g. "2025 B 15.2" or "2022 A 6"'); c.add_argument('skills', nargs='+')
    c.add_argument('--solution', nargs='+', help='the solution of the item, when it is new or changes')
    c = sub.add_parser('set', help=f"change a field ({', '.join(SKILL_FIELDS)}); list fields take several values")
    c.add_argument('id'); c.add_argument('field'); c.add_argument('value', nargs='*')
    c = sub.add_parser('add', help='add a skill under a topic, a topic under an area, or an area (PARENT = -)')
    c.add_argument('parent'); c.add_argument('slug'); c.add_argument('name')
    c.add_argument('--kind', choices=KINDS, default='procedure')
    c.add_argument('--requires', nargs='*', default=[])
    c.add_argument('--tags', nargs='*', default=[])
    c.add_argument('--spec', nargs='*', type=int, default=[])
    c.add_argument('--note', default='')
    c.add_argument('--before')
    c = sub.add_parser('move', help='reorder, or move under another parent')
    c.add_argument('id'); c.add_argument('--parent')
    where = c.add_mutually_exclusive_group()
    where.add_argument('--before'); where.add_argument('--after')
    c = sub.add_parser('rename', help='change the last part of an id')
    c.add_argument('id'); c.add_argument('slug')
    c = sub.add_parser('remove', help='delete a node that nothing requires and no item needs')
    c.add_argument('id')
    a = p.parse_args()

    solutions = load_solutions()
    edits = ('assign', 'set', 'add', 'move', 'rename', 'remove', 'from-solutions')
    tree = load_tree(target['dir'])
    if a.cmd == 'from-solutions':
        item_skills, older = map(assignment_of, solutions)
    else:
        item_skills, older = load_item_skills(target['dir']), load_older(target['dir'])
    try:
        if a.cmd == 'show':
            return print(show(tree, item_skills, older, a.id))
        if a.cmd == 'assign':
            edit_assign(tree, item_skills, older, a, solutions)
        elif a.cmd in edits and a.cmd != 'from-solutions':
            globals()['edit_' + a.cmd](tree, item_skills, older, a)
    except ValueError as e:
        sys.exit(f'error: {e}')
    if a.cmd in edits:
        follow(solutions, item_skills, older)
    wrong = problems(tree, item_skills, older, solutions)
    if wrong:
        sys.exit('\n'.join(['not saved:' if a.cmd in edits else 'invalid:'] + wrong[:40]))
    if a.cmd == 'check':
        n = [depth(x) for x, _ in walk(tree)]
        return print(f'valid: {n.count(0)} areas, {n.count(1)} topics, {n.count(2)} skills, '
                     f'{sum(len(v) for v in item_skills.values())} items assigned, '
                     f'{sum(len(v) for v in older.values())} items of older tests'
                     + ', every one with its solution')
    if a.cmd in edits:
        save(tree, item_skills, older, solutions)
    build(tree, item_skills, older)
    print('saved and rebuilt' if a.cmd in edits else 'rebuilt')


if __name__ == '__main__':
    main()
