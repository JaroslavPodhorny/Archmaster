"""Finds the solution of each task in an official CERMAT answer key
("klíč správných řešení", PDF) and renders it as an image.

Layout facts this relies on, checked on the 20 M9 keys 2022-2026 in
References/Matematika/:

- The key is one table running over all pages: columns "Úloha",
  "Správné řešení", "Body". Its left border is at x = 56, the first column
  ends at x = 101.
- A task starts with a row that has its number alone in the first column;
  sub-items ("2.1"), solutions, constructions and the scoring notes for open
  tasks follow in the rows below, up to the next task's number.
- The last row of the table is "CELKEM" with the total of 50 points.
- A task whose rows continue on the next page either just continues there
  or has its number printed again (2026 B task 10, 2026 D task 9).
"""
from __future__ import annotations

import re
from typing import List, Tuple

import pymupdf as fitz

from .booklet import TASKS_PER_BOOKLET, Segment, TaskRegion, render_strips

# Table geometry in PDF points (A4, 595 x 842).
TABLE_LEFT = 55.0
TABLE_RIGHT = 539.5
_FIRST_COLUMN_END = 101.5
_BORDER = 1.0       # thickness of the table rules


def _scan_page(page: fitz.Page) -> Tuple[List[float], List[Tuple[float, int]], float, float]:
    """Returns the y of every rule crossing the first column, the (y, task)
    of every task number, and the top and bottom of the table on this page
    (top == bottom if the page has no table). On the page with the "CELKEM"
    row the table is taken to end above that row."""
    rules: List[float] = []
    top, bottom = float('inf'), 0.0
    for d in page.get_drawings():
        r = d['rect']
        if r.height < 1.6 and r.x0 < TABLE_LEFT + 3 and r.x1 > _FIRST_COLUMN_END - 3:
            rules.append(r.y0)
        elif r.width < 1.6 and TABLE_LEFT < r.x0 < TABLE_LEFT + 2:      # the left border
            top, bottom = min(top, r.y0), max(bottom, r.y1)
    numbers: List[Tuple[float, int]] = []
    total_row = None
    for block in page.get_text('dict')['blocks']:
        for line in block.get('lines', []):
            text = ''.join(s['text'] for s in line['spans']).strip()
            x0, y0, x1, _ = line['bbox']
            if text == 'CELKEM' and x0 < _FIRST_COLUMN_END:
                total_row = y0
            if re.fullmatch(r'\d{1,2}', text) and TABLE_LEFT < x0 and x1 < _FIRST_COLUMN_END and top <= y0 <= bottom:
                numbers.append((y0, int(text)))
    if bottom <= top:
        return [], [], 0.0, 0.0
    if total_row is not None:
        bottom = max(r for r in rules if r <= total_row + 1)
    return sorted(rules), sorted(numbers), top, bottom + _BORDER


def locate_solutions(pdf_path: str) -> List[TaskRegion]:
    """Returns the 16 tasks of an answer key with the page strips each occupies.

    Raises ValueError if the key does not yield exactly tasks 1..16, or a
    task number has no table rule right above it, so a layout this code does
    not understand cannot pass silently.
    """
    doc = fitz.open(pdf_path)
    regions: List[TaskRegion] = []
    for pno in range(len(doc)):
        rules, numbers, top, bottom = _scan_page(doc[pno])
        starts: List[Tuple[float, int]] = []
        for y, task in numbers:
            above = [r for r in rules if y - 14 < r <= y + 1]
            if not above:
                raise ValueError(f'{pdf_path}: no table rule above task {task} on page {pno + 1}')
            starts.append((max(above), task))
        if not regions and not starts:
            continue        # nothing of the table yet
        edges = [y for y, _ in starts] + [bottom]
        if regions and bottom > top and (not starts or starts[0][0] - top > 3):
            # rows continuing the last task of the previous page
            regions[-1].segments.append(Segment(pno, top, edges[0] + _BORDER))
        for (y, task), end in zip(starts, edges[1:]):
            if regions and regions[-1].task == task:        # number repeated after a page break
                regions[-1].segments.append(Segment(pno, y, end + _BORDER))
            else:
                regions.append(TaskRegion(task, [Segment(pno, y, min(end + _BORDER, bottom))]))
    found = [r.task for r in regions]
    if found != list(range(1, TASKS_PER_BOOKLET + 1)):
        raise ValueError(f'{pdf_path}: expected tasks 1-16, found {found}')
    for region in regions:
        parts = [doc[s.page].get_text('text', clip=fitz.Rect(_FIRST_COLUMN_END, s.y0, TABLE_RIGHT, s.y1))
                 for s in region.segments]
        region.text = re.sub(r'\s+', ' ', ' '.join(parts)).strip()
    return regions


def render_solution(pdf_path: str, region: TaskRegion, png_path: str, dpi: int = 130) -> None:
    """Writes the key rows of one task as a PNG, stacking its page strips."""
    render_strips(pdf_path, region.segments, png_path, TABLE_LEFT, TABLE_RIGHT, dpi)
