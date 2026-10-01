"""The problem database: every task of the official M9 tests, searchable.

build_database() fills a SQLite file and a folder of screenshots (each task
and its official solution) from the booklets and answer keys in References/
and the catalog in analysis/data.
search_problems() and filter_options() read it.
"""
from __future__ import annotations

import os
import re
import sqlite3
from dataclasses import dataclass
from typing import Dict, List, Optional, Sequence

from . import answer_key, booklet
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
class Problem:
    id: str
    year: int
    term: str
    task: int
    format: str
    points: int
    tags: List[str]
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
    os.makedirs(screenshots_dir, exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(db_path)), exist_ok=True)
    if os.path.exists(db_path):
        os.remove(db_path)
    db = sqlite3.connect(db_path)
    db.executescript(_SCHEMA)

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
        problem_id = f'M9-{t.year}-{t.term}-{t.task:02d}'
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
        db.execute('INSERT INTO problems_fts VALUES (?,?,?)', (problem_id, t.description, region.text))
    db.commit()
    db.close()
    return len(catalog)


def _fts_query(query: str) -> str:
    """Every typed word must occur; each is matched as a prefix, so
    "trojúhelník" also finds "trojúhelníku"."""
    return ' '.join(f'"{w}"*' for w in re.findall(r'\w+', query))


def _where(query, years, terms, formats, tags, points, min_success, max_success):
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
    values (for tags: having at least one of them); different filters
    combine with AND. A success-rate bound leaves out problems with no
    published results. order_by is one of newest, oldest, hardest, easiest.
    """
    if order_by not in _ORDERINGS:
        raise ValueError(f'order_by must be one of {sorted(_ORDERINGS)}')
    where, params = _where(query, years, terms, formats, tags, points, min_success, max_success)
    db = sqlite3.connect(db_path)
    db.row_factory = sqlite3.Row
    total = db.execute(f'SELECT COUNT(*) FROM problems p{where}', params).fetchone()[0]
    rows = db.execute(
        f'SELECT p.*, (SELECT group_concat(tag) FROM problem_tags WHERE problem_id = p.id) AS tags '
        f'FROM problems p{where} ORDER BY {_ORDERINGS[order_by]} LIMIT ? OFFSET ?',
        params + [limit, offset]).fetchall()
    db.close()
    problems = [Problem(
        id=r['id'], year=r['year'], term=r['term'], task=r['task'], format=r['format'],
        points=r['points'], tags=sorted(r['tags'].split(',')), description=r['description'],
        text=r['text'], answer_key=r['answer_key'], success_pct=r['success_pct'],
        skipped_pct=r['skipped_pct'], screenshot=r['screenshot'],
        solution=r['solution'], source_pdf=r['source_pdf'],
        pages=[int(p) for p in r['pages'].split(',')]) for r in rows]
    return SearchResult(total, problems)


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
    db.close()
    return {
        'years': [{'value': y, 'label': str(y), 'count': years[y]} for y in sorted(years, reverse=True)],
        'terms': [{'value': t, 'label': f'{TERMS[t]} termín', 'count': terms[t]} for t in TERMS if t in terms],
        'formats': [{'value': f, 'label': FORMATS[f], 'count': formats[f]} for f in FORMATS if f in formats],
        'tags': [{'value': t, 'label': TAGS[t], 'count': tags[t]} for t in TAGS if t in tags],
        'points': [{'value': p, 'label': str(p), 'count': points[p]} for p in sorted(points)],
    }
