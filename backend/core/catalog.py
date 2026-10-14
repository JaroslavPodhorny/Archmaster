"""Reads the hand-made task catalog and CERMAT's item results from analysis/data.

The success-rate rules are the same as in analysis/build_catalog.py
(see the notes at the top of analysis/02_katalog_uloh.md).
"""
from __future__ import annotations

import csv
import os
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

TAGS = {
    'N-ARIT': 'Číselné výrazy, mocniny, odmocniny',
    'N-ZLOM': 'Zlomky',
    'N-DEL': 'Dělitelnost, prvočísla',
    'N-JED': 'Převody jednotek, čas',
    'A-VYR': 'Úpravy výrazů, vzorce, vytýkání',
    'A-ROV': 'Lineární rovnice',
    'A-SOU': 'Soustava dvou rovnic',
    'A-SLOV': 'Výraz s proměnnou a slovní úloha na rovnici',
    'P-PROC': 'Procenta',
    'P-POM': 'Poměr, úměrnost, měřítko, práce, pohyb',
    'D-GRAF': 'Grafy, tabulky, aritmetický průměr',
    'G-UHLY': 'Úhly',
    'G-ROV': 'Obvod a obsah rovinných útvarů',
    'G-PYT': 'Pythagorova věta',
    'G-KRUH': 'Kruh, kružnice, π',
    'G-TEL': 'Tělesa – objem, povrch, sítě',
    'G-KON': 'Konstrukční úlohy',
    'G-SOUM': 'Souměrnost',
    'X-NEST': 'Nestandardní úlohy, zákonitosti',
}
FORMATS = {
    'OV': 'otevřená, jen výsledek',
    'OP': 'otevřená s postupem',
    'OV+OP': 'otevřená, část s postupem',
    'K': 'konstrukční',
    'AN': 'svazek dichotomických (A/N)',
    'MC': 'výběr z 5 (A–E)',
    'PR': 'přiřazovací (A–F)',
}
TERMS = {'A': '1. řádný', 'B': '2. řádný', 'C': '1. náhradní', 'D': '2. náhradní'}

# CERMAT reports 2023 B task 9 under a sub-item number
_ITEM_ALIAS = {('2023', 'B', '9'): '9.3'}


@dataclass
class CatalogItem:
    """One scored part of a task: a sub-item ("4.1"), or the whole task ("6") when it has none."""
    name: str
    points: float                   # statements of an A/N bundle share the bundle's points equally
    success_pct: Optional[float]


@dataclass
class CatalogTask:
    year: int
    term: str
    task: int
    format: str
    tags: List[str]
    points: int
    description: str
    answer_key: str                 # closed tasks only, e.g. "A,N,N" or "C"
    success_pct: Optional[float]    # None where CERMAT published no results
    skipped_pct: Optional[float]
    items: List[CatalogItem]

    @property
    def problem_id(self) -> str:
        """What the task is called everywhere else, e.g. M9-2025-A-07."""
        return f'M9-{self.year}-{self.term}-{self.task:02d}'


def _sub_items(task: str, subpoints: str) -> Tuple[List[Tuple[str, Optional[int]]], int]:
    if subpoints.startswith('b'):       # bundle of three items scored together
        return [(f'{task}.{i}', None) for i in (1, 2, 3)], int(subpoints[1:])
    if ':' not in subpoints:
        return [(task, int(subpoints))], int(subpoints)
    items = [(a, int(b)) for a, b in (x.split(':') for x in subpoints.split(','))]
    return items, sum(p for _, p in items)


def _share_choosing_key(row: Dict[str, str], key: str) -> Optional[float]:
    shares = dict(x.split(':') for x in row['distribution_pct'].split() if ':' in x)
    key = {'Ano': 'A', 'Ne': 'N'}.get(key, key)
    if key in shares:
        return float(shares[key])
    if key == 'N' and 'B' in shares:    # 2024+ files label A/N as columns A, B
        return float(shares['B'])
    return None


def load_catalog(analysis_data_dir: str) -> List[CatalogTask]:
    """All catalogued tasks with their success and omission rates."""
    stats: Dict[Tuple[str, str, str], Dict[str, str]] = {}
    with open(os.path.join(analysis_data_dir, 'm9_item_stats_2022_2026.csv'), encoding='utf-8') as f:
        for r in csv.DictReader(f):
            stats[(r['year'], r['term'], r['item'])] = r

    tasks: List[CatalogTask] = []
    with open(os.path.join(analysis_data_dir, 'm9_task_catalog.tsv'), encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            items, points = _sub_items(r['task'], r['subpoints'])
            keys = r['keys'].split(',') if r['keys'] else []
            closed = r['fmt'] in ('AN', 'MC', 'PR')
            values, weights, skips, parts = [], [], [], []
            for i, (name, item_points) in enumerate(items):
                parts.append(CatalogItem(name, item_points or points / len(items), None))
                item = _ITEM_ALIAS.get((r['year'], r['term'], name), name)
                s = stats.get((r['year'], r['term'], item))
                if not s and not closed:
                    s = stats.get((r['year'], r['term'], r['task']))
                if not s:
                    continue
                if closed:
                    v = _share_choosing_key(s, keys[i]) if keys else None
                else:
                    v = float(s['mean_pct_score']) if s['mean_pct_score'] != '' else None
                if v is not None:
                    values.append(v)
                    weights.append(item_points or 1)
                    if s['item'] != r['task'] or len(items) == 1:   # not the task's result standing in for a part
                        parts[-1].success_pct = v
                if s['skipped_pct'] != '':
                    skips.append(float(s['skipped_pct']))
            tasks.append(CatalogTask(
                year=int(r['year']), term=r['term'], task=int(r['task']), format=r['fmt'],
                tags=r['tags'].split(';'), points=points, description=r['desc'], answer_key=r['keys'],
                success_pct=sum(v * w for v, w in zip(values, weights)) / sum(weights) if values else None,
                skipped_pct=sum(skips) / len(skips) if skips else None,
                items=parts,
            ))
    return tasks
