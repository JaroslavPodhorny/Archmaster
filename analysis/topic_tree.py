"""The tree of what the M9 test examines, in learning order: data/m9_topic_tree.json.

This file is the only thing that writes that JSON. Every edit is validated first (ids, prerequisites
that come earlier in the tree, example tasks that exist in data/m9_task_catalog.tsv), then saved, then
04_strom_M9.md and the tree view 04_strom_M9.html are rebuilt.

    uv run --project backend python analysis/topic_tree.py show [ID]
    uv run --project backend python analysis/topic_tree.py set ID FIELD [VALUE ...]
    uv run --project backend python analysis/topic_tree.py add PARENT SLUG NAME [--kind ... --priority ...]
    uv run --project backend python analysis/topic_tree.py move ID [--parent ID] [--before ID | --after ID]
    uv run --project backend python analysis/topic_tree.py rename ID SLUG
    uv run --project backend python analysis/topic_tree.py remove ID
    uv run --project backend python analysis/topic_tree.py check | build
"""
import argparse, collections, csv, functools, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from backend.core.catalog import TAGS, load_catalog  # noqa: E402

DATA = os.path.join(HERE, 'data')
TREE = os.path.join(DATA, 'm9_topic_tree.json')
KINDS = {'procedure': 'postup', 'translation': 'překlad', 'fact': 'znalost', 'strategy': 'rozbor'}
PRIORITIES = ('1', '2', '3', 'S')      # S = in the specification, not seen in the tests
LIST_FIELDS = ('tags', 'spec', 'requires', 'examples')
SKILL_FIELDS = ('name', 'kind', 'priority', 'requires', 'tags', 'spec', 'examples', 'note')
GROUP_FIELDS = ('name', 'tags', 'spec', 'note')
NO_EXAMPLE_NEEDED = {'KON.ROZBOR.zapis'}   # a rule about the answer sheet, not a task type


# ---- the tree
def load():
    with open(TREE, encoding='utf-8') as f:
        return json.load(f)


def save(tree):
    with open(TREE, 'w', encoding='utf-8') as f:
        json.dump(tree, f, ensure_ascii=False, indent=2)
        f.write('\n')


def depth(node):
    return node['id'].count('.')      # 0 area, 1 topic, 2 skill


def walk(tree):
    """Every node with its parent (None for areas), in learning order."""
    def visit(node, parent):
        yield node, parent
        for child in node.get('children', []):
            yield from visit(child, node)
    for area in tree['areas']:
        yield from visit(area, None)


def skills(node):
    return [node] if depth(node) == 2 else [s for c in node['children'] for s in skills(c)]


def find(tree, node_id):
    for node, parent in walk(tree):
        if node['id'] == node_id:
            return node, parent
    raise ValueError(f'no node {node_id}')


def siblings(tree, parent):
    return parent['children'] if parent else tree['areas']


def set_id(tree, node, new_id):
    """Gives a node (and everything under it) a new id and follows it in every prerequisite list."""
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


# ---- the task catalog, for checking examples and showing success rates
@functools.cache
def tasks():
    catalog = {(str(t.year), t.term, str(t.task)): t for t in load_catalog(DATA)}
    stats, subitems = {}, {}
    with open(os.path.join(DATA, 'm9_item_stats_2022_2026.csv'), encoding='utf-8') as f:
        for r in csv.DictReader(f):
            stats[(r['year'], r['term'], r['item'])] = r
    with open(os.path.join(DATA, 'm9_task_catalog.tsv'), encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            sp = r['subpoints']
            subitems[(r['year'], r['term'], r['task'])] = \
                {f"{r['task']}.{i}" for i in (1, 2, 3)} if sp.startswith('b') else \
                {x.split(':')[0] for x in sp.split(',') if ':' in x}
    return catalog, stats, subitems


def success(example):
    """% success of a task ("2022 A 4") or a sub-item ("2022 A 4.1"); None where nothing is published."""
    catalog, stats, _ = tasks()
    year, term, item = example.split()
    task = catalog[(year, term, item.split('.')[0])]
    if '.' not in item:
        return task.success_pct
    s = stats.get((year, term, item))
    if not s:
        return None
    if s['mean_pct_score'] != '':
        return float(s['mean_pct_score'])
    keys = task.answer_key.split(',') if task.answer_key else []
    i = int(item.split('.')[1]) - 1
    shares = dict(x.split(':') for x in s['distribution_pct'].split() if ':' in x)
    return float(shares[keys[i]]) if i < len(keys) and keys[i] in shares else None


def problems(tree):
    """Everything wrong with the tree, as sentences; empty when it is valid."""
    catalog, _, subitems = tasks()
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
        if node['priority'] not in PRIORITIES:
            found.append(f"{nid}: priority must be one of {', '.join(PRIORITIES)}")
        for q in node['requires']:
            if q not in seen or depth(seen[q]) != 2 or q == nid:
                found.append(f'{nid}: prerequisite {q} must be a skill that comes earlier in the tree')
        for e in node['examples']:
            parts = e.split()
            key = (*parts[:2], parts[-1].split('.')[0]) if len(parts) == 3 else None
            if key not in catalog or ('.' in parts[2] and parts[2] not in subitems[key]):
                found.append(f'{nid}: example "{e}" is not a task or sub-item in the catalog')
        if node['priority'] != 'S' and not node['examples'] and nid not in NO_EXAMPLE_NEEDED:
            found.append(f'{nid}: a skill seen in the tests needs at least one example')
    return found


# ---- the two views
def screenshot(example):
    year, term, item = example.split()
    return f"../backend/data/screenshots/M9-{year}-{term}-{int(item.split('.')[0]):02d}.png"


def outline(tree, root=None):
    rows = []
    for node, _ in walk(tree):
        if root and not (node['id'] + '.').startswith(root + '.'):
            continue
        d = depth(node)
        mark = node['priority'] if d == 2 else ' '
        rows.append(f"{'' if d or not rows else chr(10)}{'  ' * d}{mark} {node['name']}  [{node['id']}]")
    return '\n'.join(rows)


def markdown(tree):
    by_id = {n['id']: n for n, _ in walk(tree)}
    parent_of = {n['id']: p for n, p in walk(tree)}
    all_skills = [n for n in by_id.values() if depth(n) == 2]
    count = collections.Counter(n['priority'] for n in all_skills)
    glance = []
    for area in tree['areas']:
        glance.append(f"{area['id']}  {area['name']}")
        for i, topic in enumerate(area['children']):
            last = i == len(area['children']) - 1
            glance.append(f"{'└─' if last else '├─'} {topic['name']}")
            glance += [f"{'   ' if last else '│  '}  {s['priority']}  {s['name']}" for s in topic['children']]
        glance.append('')
    out = f"""# Strom učiva M9: what the test examines, as a tree in learning order

Generated from `analysis/data/m9_topic_tree.json`; change the tree with `analysis/topic_tree.py`, not here.
It reorganizes the findings of [03_ucivo_M9.md](03_ucivo_M9.md) (20 tests, 2022–2026) into a tree of
{len(tree['areas'])} areas, {sum(depth(n) == 1 for n in by_id.values())} topics and {len(all_skills)} skills. Nothing here was read anew from the booklets: every skill
and every example task comes from that file or the task catalog, and the specification column from
`References/MASPECIFIKACEPOZADAVKU2022 (1).pdf`, part C1 (its four areas are 1 Číslo a proměnná,
2 Závislosti, vztahy a práce s daty, 3 Geometrie v rovině a prostoru, 4 Nestandardní aplikační úlohy a problémy).

## How the tree is cut

The grouping, the priorities and the prerequisite links are my judgement, not CERMAT's.

- **A leaf is one thing a student can practise in one sitting** and recognise in a task: „složený zlomek“,
  „základ po změně“, „Thaletova kružnice“. Areas and topics only group leaves.
- **Order is learning order.** Areas, topics and leaves are listed so that everything a leaf needs comes
  earlier; the *needs* column names the direct prerequisites (the script checks this).
- **Computing and reading are separated.** Computing with fractions scores 58–76 %, a fraction word problem
  21–33 %; they are different skills, so the first is in POC and the second in VZT. The phrases
  „o třetinu více než“, „kolikrát“, „o kolik procent“ recur in fractions, percentages and equation word
  problems, so they are one topic (VZT.NEZ) learned once instead of three times.
- **Constructions are three layers**: the moves, the properties of figures, and the reading of the task.
- **Tools used everywhere stay single leaves** (druhá mocnina, převody jednotek, Pythagorova věta) and are
  pulled in through *needs* rather than repeated under each topic.
- Not in the tree: the rules for how answers must look and the list of what is not printed in the booklet
  (03, section 0). They apply to every leaf.

**Priority** (column P), by how often a skill is needed in the 20 tests:
**1** in every or nearly every test, usually in a fixed slot ({count['1']} leaves) ·
**2** recurring ({count['2']}) · **3** seen once to three times, or decides only the top score ({count['3']}) ·
**S** in the specification, not seen in these tests ({count['S']}).

**Kind** says how the skill is practised: *postup* – a procedure, drilled until fast and error-free ·
*překlad* – turning the Czech wording into mathematics · *znalost* – a fact or property known by heart ·
*rozbor* – finding the route through a multi-step task.

Percentages after an example are CERMAT's success rate for that task or sub-item (terms C and D were sat
by a few hundred candidates, so theirs are noisy; 2024 C and D have none). Points per test and success per
topic are in the contents table of 03 under the tag shown with each topic. They cannot be given per leaf
yet, because the catalog tags whole tasks; that needs every sub-item assigned to a leaf.

## The tree at a glance

```
{chr(10).join(glance[:-1])}
```
""".split('\n')

    def example(e):
        pct = success(e)
        return f"[{e}]({screenshot(e)})" + (f" {pct:.0f} %" if pct is not None else '')

    for area in tree['areas']:
        out += [f"## {area['name']} ({area['id']})", '', area['note'], '']
        for topic in area['children']:
            out += [f"### {topic['name']}", '',
                    f"`{topic['id']}` · catalog tag {', '.join(topic['tags'])} · specification area "
                    f"{', '.join(map(str, topic['spec']))}" + (f" · {topic['note']}" if topic['note'] else ''), '',
                    '| P | Skill | Kind | Needs | Examples | Note |', '|---|---|---|---|---|---|']
            for n in topic['children']:
                needs = ', '.join(f"{by_id[q]['name'].split(':')[0].split(',')[0]} ({parent_of[q]['id']})"
                                  for q in n['requires'])
                out.append(f"| {n['priority']} | {n['name']} | {KINDS[n['kind']]} | {needs} | "
                           f"{' · '.join(example(e) for e in n['examples'])} | {n['note']} |")
            out.append('')
    return '\n'.join(out)


def view_page(tree):
    """One self-contained page; the screenshots are linked, not embedded."""
    rows = []
    for n, parent in walk(tree):
        pcts = {e: success(e) for e in n.get('examples', [])}
        rows.append({'id': n['id'], 'parent': parent['id'] if parent else '', 'name': n['name'],
                     'kind': KINDS.get(n.get('kind'), ''), 'priority': n.get('priority', ''),
                     'requires': n.get('requires', []), 'tag': ', '.join(n['tags']),
                     'spec': ', '.join(map(str, n['spec'])), 'note': n['note'],
                     'ex': [{'ref': e, 'pct': None if p is None else round(p), 'png': screenshot(e)}
                            for e, p in pcts.items()]})
    with open(os.path.join(HERE, 'tree_view_template.html'), encoding='utf-8') as f:
        return f.read().replace('/*DATA*/', json.dumps(rows, ensure_ascii=False))


def build(tree):
    for name, text in (('04_strom_M9.md', markdown(tree)), ('04_strom_M9.html', view_page(tree))):
        with open(os.path.join(HERE, name), 'w', encoding='utf-8') as f:
            f.write(text)


# ---- edits (each changes the tree in memory; main() validates, saves and rebuilds)
def parse(field, values):
    if field == 'spec':
        return [int(v) for v in values]
    if field in LIST_FIELDS:
        return list(values)
    return ' '.join(values)


def edit_set(tree, a):
    node, _ = find(tree, a.id)
    if a.field not in (SKILL_FIELDS if depth(node) == 2 else GROUP_FIELDS):
        raise ValueError(f'{a.id} has no field {a.field}')
    node[a.field] = parse(a.field, a.value)


def edit_add(tree, a):
    parent, _ = find(tree, a.parent) if a.parent != '-' else (None, None)
    d = depth(parent) + 1 if parent else 0
    node = {'id': f"{parent['id']}.{a.slug}" if parent else a.slug, 'name': a.name}
    if d == 2:
        node.update(kind=a.kind, priority=a.priority, requires=a.requires)
    node.update(tags=a.tags or (parent['tags'] if parent else []),
                spec=a.spec or (parent['spec'] if parent else []))
    if d == 2:
        node['examples'] = a.examples
    node['note'] = a.note
    if d < 2:
        node['children'] = []
    place(tree, node, parent, a.before, None)


def place(tree, node, parent, before, after):
    target = siblings(tree, parent)
    anchor = before or after
    if anchor:
        at = [n['id'] for n in target].index(anchor) + (1 if after else 0)   # ValueError if not a sibling
        target.insert(at, node)
    else:
        target.append(node)


def edit_move(tree, a):
    node, parent = find(tree, a.id)
    new_parent = find(tree, a.parent)[0] if a.parent else parent
    if (depth(new_parent) if new_parent else -1) != depth(node) - 1:
        raise ValueError('a skill moves under a topic, a topic under an area')
    siblings(tree, parent).remove(node)
    place(tree, node, new_parent, a.before, a.after)
    if new_parent is not parent:
        set_id(tree, node, new_parent['id'] + '.' + node['id'].rsplit('.', 1)[1])


def edit_rename(tree, a):
    node, parent = find(tree, a.id)
    set_id(tree, node, f"{parent['id']}.{a.slug}" if parent else a.slug)


def edit_remove(tree, a):
    node, parent = find(tree, a.id)
    gone = {n['id'] for n in skills(node)} if depth(node) < 2 else {node['id']}
    users = [n['id'] for n, _ in walk(tree) if n['id'] not in gone and gone & set(n.get('requires', []))]
    if users:
        raise ValueError(f"still a prerequisite of {', '.join(users)}")
    siblings(tree, parent).remove(node)


def show(tree, node_id):
    if not node_id:
        return outline(tree)
    node, _ = find(tree, node_id)
    if depth(node) < 2:
        return outline(tree, node_id)
    needed_by = [n['id'] for n, _ in walk(tree) if node_id in n.get('requires', [])]
    return '\n'.join(f'{k:9s} {v}' for k, v in list(node.items()) + [('needed by', needed_by)])


def main():
    p = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    sub = p.add_subparsers(dest='cmd', required=True)
    sub.add_parser('check', help='validate the tree')
    sub.add_parser('build', help='rebuild 04_strom_M9.md and 04_strom_M9.html')
    c = sub.add_parser('show', help='print the tree, one branch, or one skill')
    c.add_argument('id', nargs='?')
    c = sub.add_parser('set', help=f"change a field ({', '.join(SKILL_FIELDS)}); list fields take several values")
    c.add_argument('id'); c.add_argument('field'); c.add_argument('value', nargs='*')
    c = sub.add_parser('add', help='add a skill under a topic, a topic under an area, or an area (PARENT = -)')
    c.add_argument('parent'); c.add_argument('slug'); c.add_argument('name')
    c.add_argument('--kind', choices=KINDS, default='procedure')
    c.add_argument('--priority', choices=PRIORITIES, default='2')
    c.add_argument('--requires', nargs='*', default=[])
    c.add_argument('--tags', nargs='*', default=[])
    c.add_argument('--spec', nargs='*', type=int, default=[])
    c.add_argument('--examples', nargs='*', default=[], help='quoted, e.g. "2022 A 4.1" "2025 B 15"')
    c.add_argument('--note', default='')
    c.add_argument('--before')
    c = sub.add_parser('move', help='reorder, or move under another parent')
    c.add_argument('id'); c.add_argument('--parent')
    where = c.add_mutually_exclusive_group()
    where.add_argument('--before'); where.add_argument('--after')
    c = sub.add_parser('rename', help='change the last part of an id')
    c.add_argument('id'); c.add_argument('slug')
    c = sub.add_parser('remove', help='delete a node that nothing requires')
    c.add_argument('id')
    a = p.parse_args()

    tree = load()
    try:
        if a.cmd == 'show':
            return print(show(tree, a.id))
        if a.cmd in ('set', 'add', 'move', 'rename', 'remove'):
            globals()['edit_' + a.cmd](tree, a)
    except ValueError as e:
        sys.exit(f'error: {e}')
    wrong = problems(tree)
    if wrong:
        sys.exit('\n'.join(['not saved:' if a.cmd not in ('check', 'build') else 'invalid tree:'] + wrong))
    if a.cmd == 'check':
        n = [depth(x) for x, _ in walk(tree)]
        return print(f'valid: {n.count(0)} areas, {n.count(1)} topics, {n.count(2)} skills')
    if a.cmd != 'build':
        save(tree)
    build(tree)
    print('saved and rebuilt' if a.cmd != 'build' else 'rebuilt')


if __name__ == '__main__':
    main()
