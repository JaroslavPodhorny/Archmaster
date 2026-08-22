"""Analyze CERMAT M9 Math test PDFs — extract typography, layout, and content data.

Produces two JSON output files:
- docs/data/layout_metrics.json  — fonts, sizes, margins, drawing specs
- docs/data/cross_reference.json — per-test, per-task content metadata

Run from project root:
    python3 scripts/analyze_cermat_layout.py
"""

from __future__ import annotations

import json
import re
import statistics
from collections import Counter, defaultdict
from pathlib import Path

import fitz  # PyMuPDF


# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

WORKSPACE = Path("/Users/jarda/ArchMaster")
MATH_DIR = WORKSPACE / "References" / "Matematika"
DATA_DIR = WORKSPACE / "docs" / "data"
SCREENSHOT_DIR = WORKSPACE / "docs" / "reference_screenshots"


# ---------------------------------------------------------------------------
# Phase 1a: Typography & Layout Extraction
# ---------------------------------------------------------------------------


def extract_typography(doc: fitz.Document) -> dict:
    """Extract font usage statistics across all pages."""
    font_usage: dict[str, dict] = {}

    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict", flags=fitz.TEXT_PRESERVE_WHITESPACE)

        for block in blocks.get("blocks", []):
            if block.get("type") != 0:
                continue
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    font = span.get("font", "unknown")
                    size = round(span.get("size", 0), 2)
                    flags = span.get("flags", 0)
                    color = span.get("color", 0)
                    text = span.get("text", "").strip()

                    key = f"{font}|{size}"
                    if key not in font_usage:
                        font_usage[key] = {
                            "font": font,
                            "size": size,
                            "bold": bool(flags & (1 << 4)),
                            "italic": bool(flags & (1 << 1)),
                            "color_hex": f"#{color:06x}",
                            "count": 0,
                            "pages": set(),
                            "sample_texts": [],
                        }
                    font_usage[key]["count"] += 1
                    font_usage[key]["pages"].add(page_num + 1)
                    if text and len(font_usage[key]["sample_texts"]) < 5:
                        font_usage[key]["sample_texts"].append(text[:100])

    # Convert sets to lists for JSON serialization
    for v in font_usage.values():
        v["pages"] = sorted(v["pages"])

    return font_usage


def extract_page_geometry(doc: fitz.Document) -> list[dict]:
    """Extract page dimensions and text bounding boxes to derive margins."""
    pages = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        rect = page.rect

        # Get text bounding box to derive margins
        blocks = page.get_text("dict", flags=fitz.TEXT_PRESERVE_WHITESPACE)
        text_blocks = [b for b in blocks.get("blocks", []) if b.get("type") == 0]

        if text_blocks:
            min_x = min(b["bbox"][0] for b in text_blocks)
            min_y = min(b["bbox"][1] for b in text_blocks)
            max_x = max(b["bbox"][2] for b in text_blocks)
            max_y = max(b["bbox"][3] for b in text_blocks)
        else:
            min_x = min_y = max_x = max_y = 0

        pages.append({
            "page": page_num + 1,
            "width_pt": round(rect.width, 2),
            "height_pt": round(rect.height, 2),
            "width_mm": round(rect.width / 72 * 25.4, 1),
            "height_mm": round(rect.height / 72 * 25.4, 1),
            "text_bbox": {
                "left_pt": round(min_x, 2),
                "top_pt": round(min_y, 2),
                "right_pt": round(max_x, 2),
                "bottom_pt": round(max_y, 2),
            },
            "margins_pt": {
                "left": round(min_x, 2),
                "top": round(min_y, 2),
                "right": round(rect.width - max_x, 2),
                "bottom": round(rect.height - max_y, 2),
            },
        })

    return pages


def extract_drawings(doc: fitz.Document) -> dict:
    """Extract vector drawing elements (lines, rects) per page."""
    drawing_summary = {}

    for page_num in range(len(doc)):
        page = doc[page_num]
        drawings = page.get_drawings()

        if not drawings:
            continue

        page_drawings = {
            "total": len(drawings),
            "fills": [],
            "lines": [],
            "horizontal_rules": [],
        }

        for d in drawings:
            items = d.get("items", [])
            fill = d.get("fill")
            color = d.get("color")
            width = d.get("width")

            for item in items:
                item_type = item[0]

                if item_type in ("re", "qu"):
                    rect_data = item[1]
                    if hasattr(rect_data, "x0"):
                        r = rect_data
                        h = round(r.y1 - r.y0, 2)
                        w = round(r.x1 - r.x0, 2)

                        # Detect horizontal rules (wide, thin rects)
                        if w > 100 and h < 3:
                            page_drawings["horizontal_rules"].append({
                                "x0": round(r.x0, 2),
                                "y": round(r.y0, 2),
                                "x1": round(r.x1, 2),
                                "width_pt": w,
                                "thickness_pt": h,
                                "fill": _color_to_hex(fill),
                            })

                        # Detect filled rectangles (context boxes, etc.)
                        if fill and fill != (0, 0, 0) and w > 50 and h > 20:
                            page_drawings["fills"].append({
                                "x0": round(r.x0, 2),
                                "y0": round(r.y0, 2),
                                "x1": round(r.x1, 2),
                                "y1": round(r.y1, 2),
                                "width_pt": w,
                                "height_pt": h,
                                "fill_color": _color_to_hex(fill),
                                "border_color": _color_to_hex(color),
                            })

                elif item_type == "l":
                    if len(item) >= 3:
                        p1, p2 = item[1], item[2]
                        if hasattr(p1, "x"):
                            page_drawings["lines"].append({
                                "x0": round(p1.x, 2),
                                "y0": round(p1.y, 2),
                                "x1": round(p2.x, 2),
                                "y1": round(p2.y, 2),
                                "width": width,
                                "color": _color_to_hex(color),
                            })

        drawing_summary[str(page_num + 1)] = page_drawings

    return drawing_summary


def _color_to_hex(color) -> str | None:
    """Convert a PyMuPDF color tuple to hex string."""
    if color is None:
        return None
    if isinstance(color, (tuple, list)):
        if len(color) == 3:
            r, g, b = [int(c * 255) for c in color]
            return f"#{r:02x}{g:02x}{b:02x}"
        if len(color) == 1:
            v = int(color[0] * 255)
            return f"#{v:02x}{v:02x}{v:02x}"
    return str(color)


def extract_cover_page_text(doc: fitz.Document) -> list[dict]:
    """Extract the full structured text of the cover page (page 1)."""
    page = doc[0]
    blocks = page.get_text("dict", flags=fitz.TEXT_PRESERVE_WHITESPACE)
    result = []

    for block in blocks.get("blocks", []):
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            line_text = ""
            line_fonts = []
            for span in line.get("spans", []):
                text = span.get("text", "")
                line_text += text
                line_fonts.append({
                    "text": text,
                    "font": span.get("font"),
                    "size": round(span.get("size", 0), 2),
                    "bold": bool(span.get("flags", 0) & (1 << 4)),
                    "y_pos": round(span.get("origin", (0, 0))[1], 2),
                })
            if line_text.strip():
                result.append({
                    "text": line_text.strip(),
                    "spans": line_fonts,
                    "bbox": [round(x, 2) for x in line.get("bbox", [0, 0, 0, 0])],
                })

    return result


def extract_last_page_text(doc: fitz.Document) -> list[dict]:
    """Extract the formula sheet from the last page."""
    page = doc[-1]
    blocks = page.get_text("dict", flags=fitz.TEXT_PRESERVE_WHITESPACE)
    result = []

    for block in blocks.get("blocks", []):
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            line_text = ""
            for span in line.get("spans", []):
                line_text += span.get("text", "")
            if line_text.strip():
                result.append({
                    "text": line_text.strip(),
                    "bbox": [round(x, 2) for x in line.get("bbox", [0, 0, 0, 0])],
                })

    return result


# ---------------------------------------------------------------------------
# Phase 1b: Content Extraction from Answer Keys
# ---------------------------------------------------------------------------


def extract_answer_key(doc: fitz.Document) -> dict:
    """Extract structured answer key data."""
    full_text = ""
    for page_num in range(len(doc)):
        page = doc[page_num]
        full_text += page.get_text("text") + "\n"

    lines = full_text.split("\n")
    result = {
        "header_text": [],
        "total_points": None,
        "task_count": None,
        "closed_count": None,
        "open_count": None,
        "tasks": [],
    }

    # Extract header info
    for line in lines[:10]:
        line = line.strip()
        if line:
            result["header_text"].append(line)

    # Try to find task/point counts
    for i, line in enumerate(lines):
        stripped = line.strip()
        if "Počet úloh" in stripped or stripped == "16":
            for j in range(max(0, i - 2), min(len(lines), i + 5)):
                if lines[j].strip() == "16":
                    result["task_count"] = 16
                    break

        if stripped == "CELKEM":
            for j in range(i + 1, min(len(lines), i + 3)):
                m = re.search(r"(\d+)\s*bod", lines[j])
                if m:
                    result["total_points"] = int(m.group(1))
                    break

    # Extract per-task data
    current_task = None
    tasks = {}

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Task number detection: standalone number at start of scoring section
        task_match = re.match(r"^(\d{1,2})\s*$", stripped)
        if task_match:
            num = int(task_match.group(1))
            if 1 <= num <= 16:
                current_task = num
                if num not in tasks:
                    tasks[num] = {
                        "number": num,
                        "max_points": None,
                        "subtasks": [],
                        "answers": [],
                        "has_partial_credit": False,
                    }

        # Max points
        max_match = re.search(r"max\.\s*(\d+)\s*b\.", stripped)
        if max_match and current_task and current_task in tasks:
            tasks[current_task]["max_points"] = int(max_match.group(1))

        # Subtask detection
        if current_task:
            sub_match = re.match(r"^(\d{1,2})\.(\d{1,2})\s*$", stripped)
            if sub_match:
                task_num = int(sub_match.group(1))
                sub_num = int(sub_match.group(2))
                if task_num == current_task:
                    subtask_id = f"{task_num}.{sub_num}"
                    if subtask_id not in tasks[current_task]["subtasks"]:
                        tasks[current_task]["subtasks"].append(subtask_id)

                    # The answer is typically on the next line
                    for j in range(i + 1, min(len(lines), i + 3)):
                        answer_line = lines[j].strip()
                        if answer_line and not answer_line.startswith("max."):
                            tasks[current_task]["answers"].append({
                                "subtask": subtask_id,
                                "answer": answer_line,
                            })
                            break

        # Standalone answer (for MC tasks or single-answer tasks)
        if current_task and current_task in tasks:
            if re.match(r"^[A-F]\s*$", stripped):
                if not tasks[current_task]["subtasks"]:
                    tasks[current_task]["answers"].append({
                        "subtask": str(current_task),
                        "answer": stripped,
                    })

        # Partial credit detection
        if current_task and current_task in tasks:
            if "Postup řešení obsahuje" in stripped or "nedostatek" in stripped:
                tasks[current_task]["has_partial_credit"] = True

        # Points for individual items
        pts_match = re.match(r"^(\d+)\s*b\.\s*$", stripped)
        if pts_match and current_task and current_task in tasks:
            pts = int(pts_match.group(1))
            if tasks[current_task]["max_points"] is None and not tasks[current_task]["subtasks"]:
                tasks[current_task]["max_points"] = pts

    result["tasks"] = [tasks[k] for k in sorted(tasks.keys())]
    return result


# ---------------------------------------------------------------------------
# Phase 1c: Test Booklet Content Extraction
# ---------------------------------------------------------------------------


def extract_test_content(doc: fitz.Document) -> dict:
    """Extract task structure from test booklet pages."""
    full_text = ""
    page_texts = {}

    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text("text")
        full_text += text + "\n"
        page_texts[page_num + 1] = text

    result = {
        "page_count": len(doc),
        "test_code": None,
        "tasks_detected": [],
    }

    # Find test code
    code_match = re.search(r"(M9\w+T\d+)", full_text)
    if code_match:
        result["test_code"] = code_match.group(1)

    # Detect task positions
    for page_num, text in page_texts.items():
        lines = text.split("\n")
        for i, line in enumerate(lines):
            task_header = re.search(r"^\s*(\d{1,2})\s*$", line.strip())
            if task_header:
                num = int(task_header.group(1))
                if 1 <= num <= 16:
                    context = "\n".join(lines[max(0, i - 1):min(len(lines), i + 3)])
                    if "max." in context or "b." in context:
                        result["tasks_detected"].append({
                            "number": num,
                            "page": page_num,
                        })

    # Detect context boxes
    for page_num, text in page_texts.items():
        if "VÝCHOZÍ TEXT" in text:
            matches = re.findall(r"VÝCHOZÍ TEXT\s+(?:A\s+(?:OBRÁZEK|TABULKA|GRAF)\s+)?K ÚLOZE\s+(\d+)", text)
            for m in matches:
                task_num = int(m)
                for td in result["tasks_detected"]:
                    if td["number"] == task_num:
                        td["has_context_box"] = True
                        break

    return result


# ---------------------------------------------------------------------------
# Phase 2: Reference Screenshots
# ---------------------------------------------------------------------------


def render_screenshots(doc: fitz.Document, pdf_name: str, output_dir: Path, dpi: int = 300):
    """Render specific page regions as reference screenshots."""
    output_dir.mkdir(parents=True, exist_ok=True)
    zoom = dpi / 72.0
    mat = fitz.Matrix(zoom, zoom)

    # Full cover page
    if len(doc) > 0:
        page = doc[0]
        pix = page.get_pixmap(matrix=mat)
        pix.save(str(output_dir / f"cover_page_{pdf_name}.png"))

    # Full last page (formula sheet)
    if len(doc) > 1:
        page = doc[-1]
        pix = page.get_pixmap(matrix=mat)
        pix.save(str(output_dir / f"formula_sheet_{pdf_name}.png"))

    # Page 2 (first task page)
    if len(doc) > 1:
        page = doc[1]
        pix = page.get_pixmap(matrix=mat)
        pix.save(str(output_dir / f"first_task_page_{pdf_name}.png"))

    # Find a page with context box
    for page_num in range(1, len(doc)):
        page = doc[page_num]
        text = page.get_text("text")
        if "VÝCHOZÍ TEXT" in text:
            pix = page.get_pixmap(matrix=mat)
            pix.save(str(output_dir / f"context_box_page_{pdf_name}_p{page_num + 1}.png"))
            break

    # Footer region — crop bottom of page 2
    if len(doc) > 1:
        page = doc[1]
        footer_rect = fitz.Rect(0, page.rect.height - 60, page.rect.width, page.rect.height)
        pix = page.get_pixmap(matrix=mat, clip=footer_rect)
        pix.save(str(output_dir / f"footer_{pdf_name}.png"))

    # Header region — crop top of page 2
    if len(doc) > 1:
        page = doc[1]
        header_rect = fitz.Rect(0, 0, page.rect.width, 80)
        pix = page.get_pixmap(matrix=mat, clip=header_rect)
        pix.save(str(output_dir / f"header_{pdf_name}.png"))


# ---------------------------------------------------------------------------
# Main Pipeline
# ---------------------------------------------------------------------------


def analyze_all():
    """Run the full analysis pipeline."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

    # -----------------------------------------------------------------------
    # Layout Metrics (from test booklets)
    # -----------------------------------------------------------------------
    print("=" * 60)
    print("PHASE 1a: Typography & Layout from Test Booklets")
    print("=" * 60)

    layout_metrics = {
        "summary": {
            "font_usage_across_tests": {},
            "page_dimensions": {},
            "margin_ranges": {"left": [], "right": [], "top": [], "bottom": []},
            "horizontal_rules": [],
            "context_box_fills": [],
        },
        "per_test": {},
    }

    test_pdfs = sorted(MATH_DIR.glob("*_test.pdf"))
    print(f"Found {len(test_pdfs)} test PDFs")

    all_font_counters: dict[str, int] = Counter()
    all_font_details: dict[str, dict] = {}

    for pdf_file in test_pdfs:
        print(f"\n  Analyzing: {pdf_file.name}")
        doc = fitz.open(pdf_file)
        name = pdf_file.stem

        # Typography
        typography = extract_typography(doc)
        for key, data in typography.items():
            all_font_counters[key] += data["count"]
            if key not in all_font_details:
                all_font_details[key] = {
                    "font": data["font"],
                    "size": data["size"],
                    "bold": data["bold"],
                    "italic": data["italic"],
                    "color_hex": data["color_hex"],
                    "total_count": 0,
                    "test_count": 0,
                    "sample_texts": data["sample_texts"][:3],
                }
            all_font_details[key]["total_count"] += data["count"]
            all_font_details[key]["test_count"] += 1

        # Page geometry
        geometry = extract_page_geometry(doc)
        for pg in geometry:
            if pg["page"] > 1:  # Skip cover page for margin analysis
                layout_metrics["summary"]["margin_ranges"]["left"].append(pg["margins_pt"]["left"])
                layout_metrics["summary"]["margin_ranges"]["right"].append(pg["margins_pt"]["right"])
                layout_metrics["summary"]["margin_ranges"]["top"].append(pg["margins_pt"]["top"])
                layout_metrics["summary"]["margin_ranges"]["bottom"].append(pg["margins_pt"]["bottom"])

        # Drawings
        drawings = extract_drawings(doc)
        for pg_key, pg_data in drawings.items():
            for rule in pg_data.get("horizontal_rules", []):
                layout_metrics["summary"]["horizontal_rules"].append(rule)
            for fill in pg_data.get("fills", []):
                layout_metrics["summary"]["context_box_fills"].append(fill)

        # Cover page text
        cover_text = extract_cover_page_text(doc)

        # Formula sheet
        formula_text = extract_last_page_text(doc)

        # Test content structure
        test_content = extract_test_content(doc)

        layout_metrics["per_test"][name] = {
            "page_count": len(doc),
            "test_code": test_content.get("test_code"),
            "page_dimensions": {
                "width_pt": geometry[0]["width_pt"] if geometry else None,
                "height_pt": geometry[0]["height_pt"] if geometry else None,
            },
            "tasks_detected": test_content.get("tasks_detected", []),
            "cover_page_lines": [line["text"] for line in cover_text],
            "formula_sheet_lines": [line["text"] for line in formula_text],
        }

        # Screenshots for representative tests
        if "2026_1_termin_A" in name or "2025_1_termin_A" in name or "2024_1_termin_A" in name:
            print("    Rendering reference screenshots...")
            render_screenshots(doc, name.replace("_test", ""), SCREENSHOT_DIR)

        doc.close()

    # Aggregate font data
    layout_metrics["summary"]["font_usage_across_tests"] = {
        k: v for k, v in sorted(
            all_font_details.items(),
            key=lambda x: -x[1]["total_count"]
        )
    }

    # Aggregate margin statistics
    for key in ["left", "right", "top", "bottom"]:
        values = layout_metrics["summary"]["margin_ranges"][key]
        if values:
            layout_metrics["summary"]["margin_ranges"][key] = {
                "min": round(min(values), 2),
                "max": round(max(values), 2),
                "mean": round(statistics.mean(values), 2),
                "median": round(statistics.median(values), 2),
            }

    # Deduplicate and summarize horizontal rules
    rule_widths = [r["width_pt"] for r in layout_metrics["summary"]["horizontal_rules"]]
    rule_thicknesses = [r["thickness_pt"] for r in layout_metrics["summary"]["horizontal_rules"]]
    if rule_widths:
        layout_metrics["summary"]["horizontal_rule_stats"] = {
            "count": len(rule_widths),
            "width_range": [round(min(rule_widths), 2), round(max(rule_widths), 2)],
            "thickness_range": [round(min(rule_thicknesses), 2), round(max(rule_thicknesses), 2)],
            "typical_thickness": round(statistics.median(rule_thicknesses), 2),
        }
    del layout_metrics["summary"]["horizontal_rules"]

    # Summarize context box fills
    fills = layout_metrics["summary"]["context_box_fills"]
    if fills:
        fill_colors = Counter(f["fill_color"] for f in fills if f.get("fill_color"))
        layout_metrics["summary"]["context_box_fill_stats"] = {
            "count": len(fills),
            "fill_colors": dict(fill_colors.most_common(10)),
        }
    del layout_metrics["summary"]["context_box_fills"]

    # Save layout metrics
    with open(DATA_DIR / "layout_metrics.json", "w", encoding="utf-8") as f:
        json.dump(layout_metrics, f, indent=2, ensure_ascii=False)
    print(f"\n  Saved: {DATA_DIR / 'layout_metrics.json'}")

    # -----------------------------------------------------------------------
    # Cross-Reference (from answer keys)
    # -----------------------------------------------------------------------
    print("\n" + "=" * 60)
    print("PHASE 1b: Content Cross-Reference from Answer Keys")
    print("=" * 60)

    cross_reference = {
        "metadata": {
            "description": "CERMAT M9 Math cross-reference data extracted from answer key PDFs",
            "source_count": 0,
            "extraction_tool": "PyMuPDF + analyze_cermat_layout.py",
        },
        "tests": [],
    }

    key_pdfs = sorted(MATH_DIR.glob("*_klic.pdf"))
    print(f"Found {len(key_pdfs)} answer key PDFs")

    for pdf_file in key_pdfs:
        print(f"\n  Analyzing: {pdf_file.name}")
        doc = fitz.open(pdf_file)
        name = pdf_file.stem.replace("_klic", "")

        key_data = extract_answer_key(doc)

        # Parse test identifiers from filename
        parts = name.split("_")
        year = int(parts[1]) if len(parts) > 1 else None
        variant = parts[-1] if len(parts) > 1 else None

        # Determine term
        term = "unknown"
        if "1_termin" in name:
            term = "1_radny"
        elif "2_termin" in name:
            term = "2_radny"
        elif "nahradni_1" in name:
            term = "nahradni_1"
        elif "nahradni_2" in name:
            term = "nahradni_2"

        # Match with test booklet data
        test_booklet_name = name + "_test"
        booklet_data = layout_metrics["per_test"].get(test_booklet_name, {})

        test_entry = {
            "id": name,
            "year": year,
            "term": term,
            "variant": variant,
            "test_code": booklet_data.get("test_code"),
            "total_points": key_data.get("total_points"),
            "page_count": booklet_data.get("page_count"),
            "answer_key_pages": len(doc),
            "tasks": key_data.get("tasks", []),
        }

        cross_reference["tests"].append(test_entry)
        cross_reference["metadata"]["source_count"] += 1

        doc.close()

    # Save cross-reference
    with open(DATA_DIR / "cross_reference.json", "w", encoding="utf-8") as f:
        json.dump(cross_reference, f, indent=2, ensure_ascii=False)
    print(f"\n  Saved: {DATA_DIR / 'cross_reference.json'}")

    # -----------------------------------------------------------------------
    # Summary Report
    # -----------------------------------------------------------------------
    print("\n" + "=" * 60)
    print("SUMMARY REPORT")
    print("=" * 60)

    print("\n--- Font Stack (sorted by frequency) ---")
    for key, data in sorted(all_font_details.items(), key=lambda x: -x[1]["total_count"])[:20]:
        bold_str = "BOLD" if data["bold"] else ""
        italic_str = "ITALIC" if data["italic"] else ""
        print(f"  {data['font']:30s} {data['size']:6.2f}pt {bold_str:5s} {italic_str:6s} "
              f"total={data['total_count']:5d} in {data['test_count']:2d}/12 tests")
        for sample in data["sample_texts"][:2]:
            print(f"    Sample: \"{sample}\"")

    print("\n--- Page Counts ---")
    page_counts = Counter()
    for name, data in layout_metrics["per_test"].items():
        pc = data["page_count"]
        page_counts[pc] += 1
        print(f"  {name}: {pc} pages")
    print(f"\n  Distribution: {dict(page_counts)}")

    print("\n--- Margin Statistics (excluding cover page) ---")
    for key in ["left", "right", "top", "bottom"]:
        stats = layout_metrics["summary"]["margin_ranges"].get(key, {})
        if isinstance(stats, dict):
            print(f"  {key:6s}: min={stats.get('min', 'N/A')}, max={stats.get('max', 'N/A')}, "
                  f"median={stats.get('median', 'N/A')} pt")

    print("\n--- Horizontal Rules ---")
    rule_stats = layout_metrics["summary"].get("horizontal_rule_stats", {})
    if rule_stats:
        print(f"  Count: {rule_stats['count']}")
        print(f"  Width range: {rule_stats['width_range']} pt")
        print(f"  Thickness range: {rule_stats['thickness_range']} pt")
        print(f"  Typical thickness: {rule_stats['typical_thickness']} pt")

    print("\n--- Context Box Fills ---")
    fill_stats = layout_metrics["summary"].get("context_box_fill_stats", {})
    if fill_stats:
        print(f"  Count: {fill_stats['count']}")
        print(f"  Colors: {fill_stats['fill_colors']}")

    print("\n--- Cross-Reference: Points per Test ---")
    for test in cross_reference["tests"]:
        total = test.get("total_points", "?")
        task_count = len(test.get("tasks", []))
        print(f"  {test['id']}: {total} pts, {task_count} tasks extracted")

    print("\nDone!")


if __name__ == "__main__":
    analyze_all()
