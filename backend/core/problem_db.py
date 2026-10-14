"""The problem database: every task of the official M9 tests, searchable.

build_database() fills a SQLite file and a folder of screenshots (each task
and its official solution) from the booklets and answer keys in References/,
the catalog in analysis/data and the tree of skills kept there (topic_tree.py).
search_problems() and filter_options() read it.
"""
from __future__ import annotations

import os
import re
import sqlite3
from dataclasses import dataclass
from typing import Dict, List, Optional, Sequence

from . import answer_key, booklet, topic_tree
from .catalog import FORMATS, TAGS, TERMS, load_catalog

_BOOKLET_NAMES = {'A': '1_termin_A', 'B': '2_termin_B', 'C': 'nahradni_1_C', 'D': 'nahradni_2_D'}

_SCHEMA = """
CREATE TABLE problems (
    id           TEXT PRIMARY KEY,      -- e.g. M9-2025-A-07
    year         INTEGER NOT NULL,
    term         TEXT NOT NULL,         -- A, B (řádné), C, D (náhradní)
    task         INTEGER NOT NULL,
    format       TEXT NOT NULL,
    points       INTEGER NOT NULL,
    description  TEXT NOT NULL,         -- from the catalog
    text         TEXT NOT NULL,         -- wording taken from the PDF; '' if the PDF has none
    answer_key   TEXT NOT NULL,         -- closed tasks only
    success_pct  REAL,
    skipped_pct  REAL,
    screenshot   TEXT NOT NULL,         -- file name inside the screenshots folder
    solution     TEXT NOT NULL,         -- the task's rows of the official key, same folder
    source_pdf   TEXT NOT NULL,
    pages        TEXT NOT NULL          -- e.g. "4" or "11,12"
);
CREATE TABLE problem_tags (
    problem_id TEXT NOT NULL REFERENCES problems(id),
    tag        TEXT NOT NULL,
    PRIMARY KEY (problem_id, tag)
);
-- areas, topics and skills of the tree, in learning order (position)
CREATE TABLE skills (
    id       TEXT PRIMARY KEY,          -- e.g. VZT, VZT.PROC, VZT.PROC.nasobitel
    parent   TEXT,
    name     TEXT NOT NULL,
    position INTEGER NOT NULL
);
-- the prerequisite links of the tree: a skill and one skill it needs directly
CREATE TABLE skill_requires (
    skill_id    TEXT NOT NULL REFERENCES skills(id),
    required_id TEXT NOT NULL REFERENCES skills(id),
    PRIMARY KEY (skill_id, required_id)
);
-- the skills each scored item of a problem needs; position 0 is the item's main skill
CREATE TABLE problem_skills (
    problem_id TEXT NOT NULL REFERENCES problems(id),
    item       TEXT NOT NULL,           -- "15.2", or the task number when the task has no sub-items
    skill_id   TEXT NOT NULL REFERENCES skills(id),
    position   INTEGER NOT NULL,
    PRIMARY KEY (problem_id, item, skill_id)
);
-- unicode61 + remove_diacritics: "obdelnik" finds "obdélník"
CREATE VIRTUAL TABLE problems_fts USING fts5(
    id UNINDEXED, description, text, tokenize = 'unicode61 remove_diacritics 2'
);
"""

_ORDERINGS = {
    'newest': 'p.year DESC, p.term, p.task',
    'oldest': 'p.year, p.term, p.task',
    'hardest': 'p.success_pct IS NULL, p.success_pct, p.year DESC, p.term, p.task',
    'easiest': 'p.success_pct IS NULL, p.success_pct DESC, p.year DESC, p.term, p.task',
}


@dataclass
class ItemSkill:
    item: str                   # "15.2", or the task number when the task has no sub-items
    skill_id: str
    name: str
    main: bool                  # the first skill listed for the item


@dataclass
class GraphSkill:
    skill_id: str
    name: str
    topic: str                  # the name of the topic it belongs to
    requires: List[str]         # direct prerequisites; all of them are in the same graph
    needed: bool                # an item of the problem needs it itself, not only as a prerequisite


@dataclass
class Problem:
    id: str
    year: int
    term: str
    task: int
    format: str
    points: int
    tags: List[str]
    skills: List[ItemSkill]     # by item, the main skill of each item first
    skill_graph: List[GraphSkill]   # those skills and everything they rest on, in learning order
    description: str
    text: str
    answer_key: str
    success_pct: Optional[float]
    skipped_pct: Optional[float]
    screenshot: str
    solution: str
    source_pdf: str
    pages: List[int]


@dataclass
class SearchResult:
    total: int                  # matches before limit/offset
    problems: List[Problem]


def build_database(db_path: str, screenshots_dir: str, booklets_dir: str, analysis_data_dir: str) -> int:
    """Rebuilds the database and all screenshots from scratch.

    booklets_dir is References/Matematika (tests and their keys), analysis_data_dir is analysis/data.
    Returns the number of problems stored.
    """
    catalog = load_catalog(analysis_data_dir)
    tree = topic_tree.load_tree(analysis_data_dir)
    item_skills = topic_tree.load_item_skills(analysis_data_dir)
    os.makedirs(screenshots_dir, exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(db_path)), exist_ok=True)
    if os.path.exists(db_path):
        os.remove(db_path)
    db = sqlite3.connect(db_path)
    db.executescript(_SCHEMA)
    db.executemany('INSERT INTO skills VALUES (?,?,?,?)',
                   [(node['id'], parent['id'] if parent else None, node['name'], position)
                    for position, (node, parent) in enumerate(topic_tree.walk(tree))])
    db.executemany('INSERT INTO skill_requires VALUES (?,?)',
                   [(node['id'], required) for node, _ in topic_tree.walk(tree)
                    for required in node.get('requires', [])])

    regions: Dict[tuple, Dict[int, booklet.TaskRegion]] = {}
    solutions: Dict[tuple, Dict[int, booklet.TaskRegion]] = {}
    for t in catalog:
        pdf_name = f'M9_{t.year}_{_BOOKLET_NAMES[t.term]}_test.pdf'
        pdf_path = os.path.join(booklets_dir, pdf_name)
        key_path = os.path.join(booklets_dir, f'M9_{t.year}_{_BOOKLET_NAMES[t.term]}_klic.pdf')
        if (t.year, t.term) not in regions:
            regions[(t.year, t.term)] = {r.task: r for r in booklet.locate_tasks(pdf_path)}
            solutions[(t.year, t.term)] = {r.task: r for r in answer_key.locate_solutions(key_path)}
        region = regions[(t.year, t.term)][t.task]
        problem_id = t.problem_id
        screenshot = f'{problem_id}.png'
        solution = f'{problem_id}-reseni.png'
        booklet.render_task(pdf_path, region, os.path.join(screenshots_dir, screenshot))
        answer_key.render_solution(key_path, solutions[(t.year, t.term)][t.task],
                                   os.path.join(screenshots_dir, solution))
        db.execute(
            'INSERT INTO problems VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
            (problem_id, t.year, t.term, t.task, t.format, t.points, t.description, region.text,
             t.answer_key, t.success_pct, t.skipped_pct, screenshot, solution, pdf_name,
             ','.join(str(p) for p in region.pages)))
        db.executemany('INSERT INTO problem_tags VALUES (?,?)', [(problem_id, tag) for tag in t.tags])
        db.executemany('INSERT INTO problem_skills VALUES (?,?,?,?)', [
            (problem_id, item.name, skill_id, position)
            for item in t.items
            for position, skill_id in enumerate(item_skills.get(f'{t.year} {t.term}', {}).get(item.name, []))])
        db.execute('INSERT INTO problems_fts VALUES (?,?,?)', (problem_id, t.description, region.text))
    db.commit()
    db.close()
    return len(catalog)


def _fts_query(query: str) -> str:
    """Every typed word must occur; each is matched as a prefix, so
    "trojúhelník" also finds "trojúhelníku"."""
    return ' '.join(f'"{w}"*' for w in re.findall(r'\w+', query))


def _where(query, years, terms, formats, tags, skills, points, min_success, max_success):
    clauses: List[str] = []
    params: List[object] = []

    def any_of(column: str, values: Optional[Sequence]) -> None:
        if values:
            clauses.append(f'{column} IN ({",".join("?" * len(values))})')
            params.extend(values)

    fts = _fts_query(query)
    if fts:
        clauses.append('p.id IN (SELECT id FROM problems_fts WHERE problems_fts MATCH ?)')
        params.append(fts)
    any_of('p.year', years)
    any_of('p.term', terms)
    any_of('p.format', formats)
    any_of('p.points', points)
    if tags:
        clauses.append(f'p.id IN (SELECT problem_id FROM problem_tags WHERE tag IN ({",".join("?" * len(tags))}))')
        params.extend(tags)
    if skills:      # an area or topic id stands for every skill under it
        either = ' OR '.join(['skill_id = ? OR skill_id LIKE ?'] * len(skills))
        clauses.append(f'p.id IN (SELECT problem_id FROM problem_skills WHERE {either})')
        params.extend(x for s in skills for x in (s, s + '.%'))
    if min_success is not None:
        clauses.append('p.success_pct >= ?')
        params.append(min_success)
    if max_success is not None:
        clauses.append('p.success_pct <= ?')
        params.append(max_success)
    return (' WHERE ' + ' AND '.join(clauses) if clauses else ''), params


def search_problems(
    db_path: str,
    query: str = '',
    years: Optional[Sequence[int]] = None,
    terms: Optional[Sequence[str]] = None,
    formats: Optional[Sequence[str]] = None,
    tags: Optional[Sequence[str]] = None,
    skills: Optional[Sequence[str]] = None,
    points: Optional[Sequence[int]] = None,
    min_success: Optional[float] = None,
    max_success: Optional[float] = None,
    order_by: str = 'newest',
    limit: int = 50,
    offset: int = 0,
) -> SearchResult:
    """Finds problems.

    query looks in the task wording and the catalog description, ignoring
    case and diacritics. Each list filter keeps problems matching any of its
    values (for tags and skills: having at least one of them); different
    filters combine with AND. skills takes ids from the tree: a skill, or a
    topic or area for everything under it. A success-rate bound leaves out problems with no
    published results. order_by is one of newest, oldest, hardest, easiest.
    """
    if order_by not in _ORDERINGS:
        raise ValueError(f'order_by must be one of {sorted(_ORDERINGS)}')
    where, params = _where(query, years, terms, formats, tags, skills, points, min_success, max_success)
    db = sqlite3.connect(db_path)
    db.row_factory = sqlite3.Row
    total = db.execute(f'SELECT COUNT(*) FROM problems p{where}', params).fetchone()[0]
    rows = db.execute(
        f'SELECT p.*, (SELECT group_concat(tag) FROM problem_tags WHERE problem_id = p.id) AS tags '
        f'FROM problems p{where} ORDER BY {_ORDERINGS[order_by]} LIMIT ? OFFSET ?',
        params + [limit, offset]).fetchall()
    needed: Dict[str, List[ItemSkill]] = {r['id']: [] for r in rows}
    for r in db.execute(
            f'SELECT ps.problem_id, ps.item, ps.skill_id, s.name, ps.position FROM problem_skills ps '
            f'JOIN skills s ON s.id = ps.skill_id WHERE ps.problem_id IN ({",".join("?" * len(rows))}) '
            f'ORDER BY ps.problem_id, CAST(ps.item AS REAL), ps.position', [r['id'] for r in rows]):
        needed[r['problem_id']].append(ItemSkill(r['item'], r['skill_id'], r['name'], r['position'] == 0))
    graphs = _skill_graphs(db, {id: [s.skill_id for s in found] for id, found in needed.items()})
    db.close()
    problems = [Problem(
        id=r['id'], year=r['year'], term=r['term'], task=r['task'], format=r['format'],
        points=r['points'], tags=sorted(r['tags'].split(',')), skills=needed[r['id']],
        skill_graph=graphs[r['id']], description=r['description'],
        text=r['text'], answer_key=r['answer_key'], success_pct=r['success_pct'],
        skipped_pct=r['skipped_pct'], screenshot=r['screenshot'],
        solution=r['solution'], source_pdf=r['source_pdf'],
        pages=[int(p) for p in r['pages'].split(',')]) for r in rows]
    return SearchResult(total, problems)


def _skill_graphs(db: sqlite3.Connection, needed: Dict[str, List[str]]) -> Dict[str, List[GraphSkill]]:
    """For each problem (id -> the skills its items need) those skills with all their prerequisites,
    direct or not, in learning order."""
    requires: Dict[str, List[str]] = {}
    for skill_id, required_id in db.execute(
            'SELECT r.skill_id, r.required_id FROM skill_requires r JOIN skills s ON s.id = r.required_id '
            'ORDER BY s.position'):
        requires.setdefault(skill_id, []).append(required_id)
    skills = {r['id']: r for r in db.execute(
        'SELECT s.id, s.name, s.position, t.name AS topic FROM skills s JOIN skills t ON t.id = s.parent')}

    def graph(own: List[str]) -> List[GraphSkill]:
        found, todo = set(), list(own)
        while todo:
            skill_id = todo.pop()
            if skill_id not in found:
                found.add(skill_id)
                todo.extend(requires.get(skill_id, []))
        return [GraphSkill(i, skills[i]['name'], skills[i]['topic'], requires.get(i, []), i in own)
                for i in sorted(found, key=lambda i: skills[i]['position'])]

    return {problem_id: graph(own) for problem_id, own in needed.items()}


def filter_options(db_path: str) -> Dict[str, List[dict]]:
    """The values each filter can take, with Czech labels and problem counts."""
    db = sqlite3.connect(db_path)

    def counts(sql: str) -> Dict[object, int]:
        return dict(db.execute(sql).fetchall())

    years = counts('SELECT year, COUNT(*) FROM problems GROUP BY year')
    terms = counts('SELECT term, COUNT(*) FROM problems GROUP BY term')
    formats = counts('SELECT format, COUNT(*) FROM problems GROUP BY format')
    tags = counts('SELECT tag, COUNT(*) FROM problem_tags GROUP BY tag')
    points = counts('SELECT points, COUNT(*) FROM problems GROUP BY points')
    # the tree in learning order; an area or topic counts the problems needing anything under it
    skills = db.execute(
        "SELECT s.id, s.name, (SELECT COUNT(DISTINCT problem_id) FROM problem_skills "
        "WHERE skill_id = s.id OR skill_id LIKE s.id || '.%') FROM skills s ORDER BY s.position").fetchall()
    db.close()
    return {
        'years': [{'value': y, 'label': str(y), 'count': years[y]} for y in sorted(years, reverse=True)],
        'terms': [{'value': t, 'label': f'{TERMS[t]} termín', 'count': terms[t]} for t in TERMS if t in terms],
        'formats': [{'value': f, 'label': FORMATS[f], 'count': formats[f]} for f in FORMATS if f in formats],
        'tags': [{'value': t, 'label': TAGS[t], 'count': tags[t]} for t in TAGS if t in tags],
        'points': [{'value': p, 'label': str(p), 'count': points[p]} for p in sorted(points)],
        # skills no task needs (in the specification only) cannot be searched for
        'skills': [{'value': i, 'label': name, 'count': n, 'depth': i.count('.')} for i, name, n in skills if n],
    }
