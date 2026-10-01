"""Finds the individual tasks inside an official CERMAT test booklet (PDF)
and renders each one as an image.

Layout facts this relies on, checked on the 20 M9 booklets 2022-2026 in
References/Matematika/:

- Page 1 is the cover. Tasks follow in order, 16 per booklet.
- Tasks are separated by a thin full-width horizontal rule. A task that
  flows over a page break continues at the top of the next page without one.
- Every task has a points label ("1 bod", "max. 3 body") at the right margin
  just above its number; a "VÝCHOZÍ TEXT ... K ÚLOZE n" box may precede it.
- One box can serve several tasks ("K ÚLOHÁM 13–14", 2022 D); it is then
  repeated in front of each of them.
- 18 booklets carry real text. 2024 A and 2024 B store every word as a small
  picture, so they have no extractable text; there the points labels, found
  by position, mark the tasks.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

import pymupdf as fitz

TASKS_PER_BOOKLET = 16

# Page geometry in PDF points (A4, 595 x 842).
CONTENT_TOP = 30.0
CONTENT_BOTTOM = 800.0      # the page number sits below this
CROP_LEFT = 58.0
CROP_RIGHT = 541.0
PADDING = 5.0

_POINTS_LABEL = re.compile(r"(max\. )?\d+ bod(y|ů)?")
_CONTEXT_ONE = re.compile(r"VÝCHOZÍ .*K ÚLOZE (\d+)")
_CONTEXT_RANGE = re.compile(r"VÝCHOZÍ .*K ÚLOHÁM (\d+)\s*[–-]\s*(\d+)")
# Lines that are not part of any task: answer-sheet instructions printed
# between tasks, the closing reminder and the formula box.
_INSTRUCTION = ("V úlohách", "Doporučení")
_CLOSING = ("ZKONTROLUJTE", "Druhé mocniny")


@dataclass
class Segment:
    """A horizontal strip of one page (0-based page index, PDF points)."""
    page: int
    y0: float
    y1: float


@dataclass
class TaskRegion:
    task: int
    segments: List[Segment] = field(default_factory=list)
    text: str = ""          # empty for picture-only booklets

    @property
    def pages(self) -> List[int]:
        """1-based page numbers the task appears on."""
        return sorted({s.page + 1 for s in self.segments})


@dataclass
class _Mark:
    y: float            # where the task (or its context box) starts
    task: int
    is_context: bool


@dataclass
class _Page:
    separators: List[float]
    marks: List[_Mark]
    content: List[Tuple[float, float]]      # (y0, y1) of everything printed
    lines: List[Tuple[float, float, str]]   # (y0, y1, text)


def _text_lines(page: fitz.Page):
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            text = "".join(s["text"] for s in line["spans"]).strip()
            if text:
                yield fitz.Rect(line["bbox"]), text, line["spans"][0]["font"]


def _word_rows(page: fitz.Page) -> List[Tuple[fitz.Rect, int]]:
    """Word pictures grouped into rows, with the picture count of each row
    (picture-only booklets)."""
    rows: List[Tuple[fitz.Rect, int]] = []
    words = [fitz.Rect(i["bbox"]) for i in page.get_image_info()]
    for r in sorted((w for w in words if w.height <= 20), key=lambda w: w.y0):
        if rows and abs(rows[-1][0].y0 - r.y0) < 1.5:
            rows[-1] = (rows[-1][0] | r, rows[-1][1] + 1)
        else:
            rows.append((r, 1))
    return rows


def _is_rule(page: fitz.Page, row: fitz.Rect) -> bool:
    """True if a full-width row of pictures is a thin line rather than text."""
    pix = page.get_pixmap(clip=row, matrix=fitz.Matrix(2, 2), colorspace=fitz.csGRAY, annots=False)
    stride = pix.stride
    inked = sum(1 for y in range(pix.height) if min(pix.samples[y * stride:y * stride + pix.width]) < 128)
    return inked <= 4


def _scan_page(page: fitz.Page, has_text: bool, next_task: int, is_last: bool) -> _Page:
    separators: List[float] = []
    marks: List[_Mark] = []
    content: List[Tuple[float, float]] = []
    lines: List[Tuple[float, float, str]] = []

    for d in page.get_drawings():
        r = d["rect"]
        # separator rules span x 70-526; context box borders are wider or narrower
        if has_text and r.height < 1.6 and 69.5 <= r.x0 <= 71.5 and r.x1 >= 525:
            separators.append(r.y0)
        elif r.y1 > CONTENT_TOP and r.y0 < CONTENT_BOTTOM and r.x0 < CROP_RIGHT:
            content.append((r.y0, r.y1))
    for info in page.get_image_info():
        r = fitz.Rect(info["bbox"])
        if r.y0 < CONTENT_BOTTOM and (has_text or r.height > 20):
            content.append((r.y0, r.y1))

    labels: List[float] = []
    for r, text, font in _text_lines(page):
        if r.y0 >= CONTENT_BOTTOM:
            continue
        if re.fullmatch(r"_{20,}", text):     # 2024 C and D draw the rule with underscores
            separators.append(r.y1 - 1)
            continue
        content.append((r.y0, r.y1))
        if not has_text:                      # stray formula fragments only
            continue
        lines.append((r.y0, r.y1, text))
        if _POINTS_LABEL.fullmatch(text) and r.x0 > 400:
            labels.append(r.y0)
        m = _CONTEXT_RANGE.search(text) or _CONTEXT_ONE.search(text)
        if m:
            marks.append(_Mark(r.y0, int(m.group(1)), True))
        elif re.fullmatch(r"\d{1,2}", text) and "Bold" in font and r.x0 < 80:
            marks.append(_Mark(r.y0, int(text), False))
    for mark in marks:      # a task starts at the points label right above its number
        if not mark.is_context:
            mark.y = min([mark.y] + [l for l in labels if mark.y - 40 < l <= mark.y + 2])

    if not has_text:
        for r, count in _word_rows(page):
            if r.y0 >= CONTENT_BOTTOM:
                continue
            if r.x0 <= 72 and r.x1 >= 527 and _is_rule(page, r):
                separators.append(r.y1 - 1)
                continue
            if is_last and count == 1 and r.width > 455:     # the closing reminder, ruled above
                separators.append(r.y0 - 8)
                continue
            content.append((r.y0, r.y1))
            if r.x0 >= 440 and 530 <= r.x1 <= 532:           # "A N" column heads end at 529
                marks.append(_Mark(r.y0, next_task, False))
                next_task += 1

    return _Page(sorted(separators), sorted(marks, key=lambda m: m.y), content, sorted(lines))


def _trim(seg: Segment, page: _Page) -> Optional[Segment]:
    """Shrinks a strip to what is printed inside it, plus a little padding
    that never reaches past the strip into a neighbouring task."""
    inside = [(a, b) for a, b in page.content if seg.y0 - 1 <= (a + b) / 2 <= seg.y1]
    if not inside:
        return None
    y0 = max(seg.y0, min(a for a, _ in inside) - PADDING)
    y1 = min(seg.y1, max(b for _, b in inside) + PADDING)
    return Segment(seg.page, y0, y1) if y1 - y0 > 4 else None


def locate_tasks(pdf_path: str) -> List[TaskRegion]:
    """Returns the 16 tasks of a booklet with the page strips each occupies.

    Raises ValueError if the booklet does not yield exactly tasks 1..16,
    so a layout this code does not understand cannot pass silently.
    """
    doc = fitz.open(pdf_path)
    has_text = sum(len(doc[i].get_text()) for i in range(1, len(doc))) > 300 * (len(doc) - 1)

    regions: Dict[int, TaskRegion] = {}
    shared_range: Dict[int, int] = {}       # first task of a shared box -> last task
    shared_box: Dict[int, Segment] = {}     # first task of a shared box -> the box
    current: Optional[int] = None
    pending: List[Segment] = []     # context printed at a page end, task on the next page

    for pno in range(1, len(doc)):
        page = _scan_page(doc[pno], has_text, len(regions) + 1, pno == len(doc) - 1)
        for _, _, text in page.lines:
            m = _CONTEXT_RANGE.search(text)
            if m:
                shared_range[int(m.group(1))] = int(m.group(2))
        bounds = [CONTENT_TOP] + page.separators + [CONTENT_BOTTOM]
        chunks = [(a, b) for a, b in zip(bounds, bounds[1:]) if b - a > 2]
        for ci, (top, bottom) in enumerate(chunks):
            texts = [(y1, t) for y0, y1, t in page.lines if top <= y0 < bottom]
            if any(t.startswith(_CLOSING) for _, t in texts):
                continue
            starts: List[_Mark] = []        # first mark of each task in this chunk
            for mark in page.marks:
                if top <= mark.y < bottom and mark.task not in [s.task for s in starts]:
                    starts.append(mark)
            if not starts:
                seg = _trim(Segment(pno, top, bottom), page)
                if seg is None or any(t.startswith(_INSTRUCTION) for _, t in texts):
                    continue
                if ci == 0 and current is not None:
                    regions[current].segments.append(seg)
                elif ci == len(chunks) - 1 and not has_text and current not in (None, TASKS_PER_BOOKLET):
                    pending.append(seg)
                continue
            # skip answer-sheet instructions printed above the first task of the chunk
            top = max([top] + [y1 + 1 for y1, t in texts if t.startswith(_INSTRUCTION) and y1 < starts[0].y + 2])
            for i, mark in enumerate(starts):
                y0 = top if i == 0 else mark.y - 2
                y1 = starts[i + 1].y - 2 if i + 1 < len(starts) else bottom
                region = regions.setdefault(mark.task, TaskRegion(mark.task))
                region.segments += pending
                pending = []
                seg = _trim(Segment(pno, y0, y1), page)
                if seg:
                    region.segments.append(seg)
                if mark.task in shared_range and mark.is_context:
                    number_y = min(m.y for m in page.marks if m.task == mark.task and not m.is_context)
                    box = _trim(Segment(pno, y0, number_y - 2), page)
                    if box:
                        shared_box[mark.task] = box
                current = mark.task

    for first, last in shared_range.items():
        for n in range(first + 1, last + 1):
            if n in regions and first in shared_box:
                regions[n].segments.insert(0, shared_box[first])

    found = sorted(regions)
    if found != list(range(1, TASKS_PER_BOOKLET + 1)):
        raise ValueError(f"{pdf_path}: expected tasks 1-16, found {found}")
    if has_text:
        for region in regions.values():
            parts = [doc[s.page].get_text("text", clip=fitz.Rect(0, s.y0, 595, s.y1)) for s in region.segments]
            region.text = re.sub(r"\s+", " ", " ".join(parts)).strip()
    return [regions[n] for n in found]


def render_task(pdf_path: str, region: TaskRegion, png_path: str, dpi: int = 130) -> None:
    """Writes one task as a PNG, stacking its page strips top to bottom.

    Notes added to the PDF afterwards (annotations) are not drawn.
    """
    src = fitz.open(pdf_path)
    width = CROP_RIGHT - CROP_LEFT
    height = sum(s.y1 - s.y0 for s in region.segments)
    out = fitz.open()
    page = out.new_page(width=width, height=height)
    y = 0.0
    for s in region.segments:
        h = s.y1 - s.y0
        clip = fitz.Rect(CROP_LEFT, s.y0, CROP_RIGHT, s.y1)
        page.show_pdf_page(fitz.Rect(0, y, width, y + h), src, s.page, clip=clip)
        y += h
    page.get_pixmap(dpi=dpi).save(png_path)
