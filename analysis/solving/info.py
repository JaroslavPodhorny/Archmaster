"""info.py YEAR TERM: the catalog rows (item, points, success rate, key) and the trimmed official key of one test.

    uv run --project backend python analysis/solving/info.py 2025 B
"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
import pymupdf as fitz  # noqa: E402
from backend.core.catalog import load_catalog  # noqa: E402

year, term = int(sys.argv[1]), sys.argv[2]
for t in load_catalog(os.path.join(ROOT, 'analysis', 'data')):
    if (t.year, t.term) == (year, term):
        items = ' '.join(f'{i.name}:{i.points:g}b/{i.success_pct}' for i in t.items)
        print(f'{t.task:>2} {t.format:<5} key={t.answer_key or "-":<8} {items}')
pdf = glob.glob(os.path.join(ROOT, 'References', 'Matematika', f'M9_{year}_*_{term}_klic.pdf'))[0]
skip = re.compile(r'^(- |Postup řešení obsahuje|V řešení je více|Předmětem autorských|JEDNOTNÁ|KLÍČ|\d ze \d|MATEMATIKA|KÓD|Celkem'
                  r'|Uzavřených|Otevřených|Počet úloh|Úloha|Správné řešení|Body|CELKEM|50 bodů|Vyjádření ekvivalentní'
                  r'|Kromě správných|v žákovských)')
out, drop = [], False
for page in fitz.open(pdf):
    for line in page.get_text().splitlines():
        s = line.strip()
        if not s or skip.match(s):
            drop = s.startswith('- ') or 'nedostatk' in s
            continue
        if drop and not re.match(r'^(\d|max|[A-F]$|N$)', s) and len(s) > 25:
            continue                      # continuation of a scoring-note bullet
        drop = False
        out.append(s)
# NOTE: a minus sign in front of a fraction is sometimes lost in the text of the 2024 keys; check the key image then.
print(' | '.join(out))
