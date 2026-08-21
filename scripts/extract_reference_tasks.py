"""Extract standardized high-resolution reference task cutouts from CERMAT exam PDFs.

Crops individual tasks (Task 1 to 16) from official downloaded PDFs in References/
and organizes them into output/reference_crops/ for fidelity testing and side-by-side benchmarking.
"""

from __future__ import annotations

import os
import re
from pathlib import Path
import fitz  # PyMuPDF


def extract_math_tasks_from_pdf(pdf_path: Path, output_base_dir: Path, dpi: int = 200) -> dict[int, Path]:
    """Extract tasks 1 to 16 from a Math 9 CERMAT PDF."""
    doc = fitz.open(pdf_path)
    exam_id = pdf_path.stem.replace("_test", "")
    extracted = {}

    # Define standard layout zones per task for standard 12-page M9 exams
    # Page numbers are 1-indexed; coordinates in points [x0, y0, x1, y1] on A4 (595x842)
    # Margins: Left 60, Right 535
    task_layout_map = {
        1: (2, fitz.Rect(55, 75, 540, 420)),
        2: (2, fitz.Rect(55, 430, 540, 770)),
        3: (3, fitz.Rect(55, 40, 540, 380)),
        4: (3, fitz.Rect(55, 385, 540, 770)),
        5: (4, fitz.Rect(55, 40, 540, 250)),
        6: (4, fitz.Rect(55, 250, 540, 780)),
        7: (5, fitz.Rect(55, 40, 540, 450)),
        8: (5, fitz.Rect(55, 455, 540, 800)),
        9: (6, fitz.Rect(55, 40, 540, 780)),
        10: (7, fitz.Rect(55, 40, 540, 780)),
        11: (8, fitz.Rect(55, 40, 540, 440)),
        12: (8, fitz.Rect(55, 440, 540, 780)),
        13: (9, fitz.Rect(55, 40, 540, 405)),
        14: (9, fitz.Rect(55, 405, 540, 780)),
        15: (10, fitz.Rect(55, 40, 540, 780)),
        16: (11, fitz.Rect(55, 40, 540, 780)),
    }

    for task_num, (page_num, rect) in task_layout_map.items():
        if page_num > len(doc):
            continue

        page = doc[page_num - 1]
        task_dir = output_base_dir / "math" / f"task_{task_num:02d}"
        task_dir.mkdir(parents=True, exist_ok=True)

        out_path = task_dir / f"real_{exam_id}_task{task_num:02d}.png"

        zoom = dpi / 72.0
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat, clip=rect)
        pix.save(str(out_path))
        extracted[task_num] = out_path

    return extracted


def extract_all_references(ref_dir: Path, out_dir: Path):
    """Extract tasks from all math reference exams."""
    math_dir = ref_dir / "Matematika"
    if not math_dir.exists():
        print(f"References directory not found: {math_dir}")
        return

    test_pdfs = sorted(math_dir.glob("*_test.pdf"))
    print(f"Found {len(test_pdfs)} Math test PDFs to process.")

    total_extracted = 0
    for pdf_file in test_pdfs:
        res = extract_math_tasks_from_pdf(pdf_file, out_dir)
        total_extracted += len(res)
        print(f"Extracted {len(res)} tasks from {pdf_file.name}")

    print(f"\nCompleted! Total extracted real task snapshots: {total_extracted}")


if __name__ == "__main__":
    workspace = Path("/Users/jarda/ArchMaster")
    extract_all_references(workspace / "References", workspace / "output" / "reference_crops")
