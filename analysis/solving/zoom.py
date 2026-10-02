"""zoom.py YEAR TERM TASK x0 y0 x1 y1 OUT.png: a part of a task (fractions of its width and height), enlarged.

    uv run --project backend python analysis/solving/zoom.py 2024 A 12 0.25 0.22 0.75 0.42 /tmp/zoom.png

For figures too small to read in backend/data/screenshots/. Write OUT outside the repository.
"""
import glob, os, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
import pymupdf as fitz  # noqa: E402
from backend.core.booklet import locate_tasks, render_task  # noqa: E402

year, term, task = sys.argv[1], sys.argv[2], int(sys.argv[3])
x0, y0, x1, y1 = map(float, sys.argv[4:8])
out_path = sys.argv[8]
pdf = glob.glob(os.path.join(ROOT, 'References', 'Matematika', f'M9_{year}_*_{term}_test.pdf'))[0]
region = [r for r in locate_tasks(pdf) if r.task == task][0]
with tempfile.TemporaryDirectory() as tmp:
    big = os.path.join(tmp, 'full.png')
    render_task(pdf, region, big, dpi=390)
    pm = fitz.Pixmap(big)
    clip = fitz.IRect(int(x0 * pm.width), int(y0 * pm.height), int(x1 * pm.width), int(y1 * pm.height))
    part = fitz.Pixmap(pm.colorspace, clip, pm.alpha)
    part.copy(pm, clip)
    part.save(out_path)
print(out_path, part.width, part.height)
