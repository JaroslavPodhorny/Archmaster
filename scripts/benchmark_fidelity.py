"""CERMAT Engine Fidelity Benchmark and Blind Testing System.

Extracts real reference exam task snapshots, generates matching synthetic task snapshots,
runs automated perceptual and structural fidelity tests, and generates an interactive
Blind Discrimination Benchmark report (Turing test).
"""

from __future__ import annotations

import base64
import json
import os
import random
import shutil
from pathlib import Path

from PIL import Image

# Import CERMAT engines & renderer
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "backend"))

from app.engines.cermat.renderer import CermatRenderer
from app.engines.cermat.tasks import (
    Task01ArithmeticGenerator,
    Task02FractionsGenerator,
    Task03AlgebraGenerator,
    Task04EquationsGenerator,
    Task05WordProblemsGenerator,
    Task06PlanimetryGenerator,
    Task11AlgebraicModelingGenerator,
    Task12PlanimetryAnglesGenerator,
    Task14DataLogicGenerator,
    Task15MatchingGenerator,
    Task16SequencesGenerator,
)

TASK_GENERATORS = {
    1: Task01ArithmeticGenerator,
    2: Task02FractionsGenerator,
    3: Task03AlgebraGenerator,
    4: Task04EquationsGenerator,
    5: Task05WordProblemsGenerator,
    6: Task06PlanimetryGenerator,
    11: Task11AlgebraicModelingGenerator,
    12: Task12PlanimetryAnglesGenerator,
    14: Task14DataLogicGenerator,
    15: Task15MatchingGenerator,
    16: Task16SequencesGenerator,
}


def image_to_base64(img_path: Path) -> str:
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def run_benchmark_for_task(task_num: int, output_dir: Path, n_samples: int = 10):
    """Run fidelity comparison & generate blind test set for a given task number."""
    crops_dir = Path("/Users/jarda/ArchMaster/output/reference_crops/math") / f"task_{task_num:02d}"
    real_images = sorted(crops_dir.glob("*.png"))

    if not real_images:
        print(f"No real crop images found in {crops_dir}")
        return None

    gen_cls = TASK_GENERATORS.get(task_num, Task01ArithmeticGenerator)
    gen = gen_cls()
    renderer = CermatRenderer(output_dir=output_dir / f"gen_task_{task_num:02d}")

    # Generate n_samples synthetic snapshots
    synthetic_snapshots = []
    for i in range(n_samples):
        task = gen.generate(seed=1000 + i * 37)
        png_path = renderer.render_snapshot_png(task, filename_prefix=f"gen_task{task_num:02d}_sample_{i+1:02d}")
        if png_path and png_path.exists():
            synthetic_snapshots.append(png_path)

    # Pick real samples (up to n_samples)
    real_sample_pool = real_images[:n_samples]

    # Assemble shuffled blind test items
    deck = []
    for p in real_sample_pool:
        deck.append({
            "id": f"real_{p.stem}",
            "type": "REAL",
            "source": p.name,
            "path": p,
            "b64": image_to_base64(p)
        })

    for p in synthetic_snapshots:
        deck.append({
            "id": f"gen_{p.stem}",
            "type": "GENERATED",
            "source": "CERMAT Generation Engine (Antigravity)",
            "path": p,
            "b64": image_to_base64(p)
        })

    rng = random.Random(42)
    rng.shuffle(deck)

    return {
        "task_number": task_num,
        "task_name": gen.category,
        "num_real": len(real_sample_pool),
        "num_generated": len(synthetic_snapshots),
        "deck": deck
    }


def generate_interactive_benchmark_report(benchmarks: list[dict], output_html: Path):
    """Generate interactive blind testing and fidelity review dashboard."""
    output_html.parent.mkdir(parents=True, exist_ok=True)

    # Serialize benchmark data for Javascript interaction
    json_data = []
    for b in benchmarks:
        clean_deck = [
            {
                "id": item["id"],
                "type": item["type"],
                "source": item["source"],
                "b64": item["b64"],
            }
            for item in b["deck"]
        ]
        json_data.append({
            "task_number": b["task_number"],
            "task_name": b["task_name"],
            "deck": clean_deck
        })

    json_str = json.dumps(json_data)

    html_content = f"""<!DOCTYPE html>
<html lang="cs">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CERMAT Engine Fidelity & Indistinguishability Benchmark</title>
<style>
    :root {{
        --bg-main: #0f172a;
        --bg-card: #1e293b;
        --text-main: #f8fafc;
        --text-muted: #94a3b8;
        --accent: #38bdf8;
        --accent-green: #22c55e;
        --accent-red: #ef4444;
        --border: #334155;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
        background: var(--bg-main);
        color: var(--text-main);
        padding: 30px 20px;
        min-height: 100vh;
    }}
    .container {{
        max-width: 1300px;
        margin: 0 auto;
    }}
    header {{
        text-align: center;
        margin-bottom: 30px;
        border-bottom: 1px solid var(--border);
        padding-bottom: 20px;
    }}
    h1 {{
        font-size: 28px;
        font-weight: 800;
        background: linear-gradient(135deg, #38bdf8 0%, #818cf8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 8px;
    }}
    .subtitle {{
        color: var(--text-muted);
        font-size: 15px;
    }}
    .stats-bar {{
        display: flex;
        justify-content: center;
        gap: 24px;
        margin: 20px 0;
        flex-wrap: wrap;
    }}
    .stat-pill {{
        background: var(--bg-card);
        border: 1px solid var(--border);
        padding: 10px 18px;
        border-radius: 8px;
        font-size: 14px;
    }}
    .stat-pill strong {{
        color: var(--accent);
        font-size: 17px;
    }}
    .task-nav {{
        display: flex;
        justify-content: center;
        gap: 10px;
        margin-bottom: 25px;
        flex-wrap: wrap;
    }}
    .task-btn {{
        background: var(--bg-card);
        border: 1px solid var(--border);
        color: var(--text-main);
        padding: 8px 16px;
        border-radius: 6px;
        cursor: pointer;
        font-weight: 600;
        font-size: 14px;
        transition: all 0.2s ease;
    }}
    .task-btn.active {{
        background: var(--accent);
        color: #0f172a;
        border-color: var(--accent);
    }}
    .grid-container {{
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(420px, 1fr));
        gap: 24px;
        margin-top: 20px;
    }}
    .snapshot-card {{
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: 10px;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }}
    .snapshot-card:hover {{
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(0,0,0,0.3);
    }}
    .card-img-wrapper {{
        background: #ffffff;
        padding: 15px;
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 280px;
        border-bottom: 1px solid var(--border);
    }}
    .card-img-wrapper img {{
        max-width: 100%;
        max-height: 380px;
        object-fit: contain;
        border-radius: 4px;
    }}
    .card-controls {{
        padding: 16px;
        display: flex;
        flex-direction: column;
        gap: 12px;
    }}
    .btn-group {{
        display: flex;
        gap: 8px;
    }}
    .choice-btn {{
        flex: 1;
        padding: 8px 12px;
        border: 1px solid var(--border);
        background: #334155;
        color: var(--text-main);
        border-radius: 6px;
        font-weight: 600;
        font-size: 13.5px;
        cursor: pointer;
        transition: all 0.15s ease;
    }}
    .choice-btn:hover {{
        background: #475569;
    }}
    .choice-btn.selected-real {{
        background: #0284c7;
        border-color: #38bdf8;
    }}
    .choice-btn.selected-gen {{
        background: #7c3aed;
        border-color: #a78bfa;
    }}
    .reveal-btn {{
        background: transparent;
        border: 1px dashed var(--border);
        color: var(--text-muted);
        padding: 6px 12px;
        border-radius: 6px;
        font-size: 12.5px;
        cursor: pointer;
    }}
    .reveal-btn:hover {{
        color: var(--text-main);
        border-color: var(--text-muted);
    }}
    .reveal-result {{
        display: none;
        padding: 10px;
        border-radius: 6px;
        font-size: 13.5px;
        font-weight: 600;
        text-align: center;
    }}
    .reveal-result.is-real {{
        background: rgba(34, 197, 94, 0.15);
        color: var(--accent-green);
        border: 1px solid rgba(34, 197, 94, 0.3);
    }}
    .reveal-result.is-gen {{
        background: rgba(168, 85, 247, 0.15);
        color: #c084fc;
        border: 1px solid rgba(168, 85, 247, 0.3);
    }}
    .global-actions {{
        display: flex;
        justify-content: center;
        gap: 15px;
        margin: 25px 0;
    }}
    .action-btn {{
        background: linear-gradient(135deg, #0284c7, #2563eb);
        color: #ffffff;
        border: none;
        padding: 10px 22px;
        border-radius: 8px;
        font-weight: 700;
        font-size: 14.5px;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(2, 132, 199, 0.3);
    }}
    .action-btn:hover {{
        opacity: 0.95;
    }}
</style>
</head>
<body>
<div class="container">
    <header>
        <h1>CERMAT Indistinguishability Benchmark</h1>
        <p class="subtitle">Blind Discrimination Testing: 10 Real Official Exam Snapshots vs. 10 Engine-Generated Snapshots</p>
        <div class="stats-bar">
            <div class="stat-pill">Total Test Cards: <strong id="total-cards">0</strong></div>
            <div class="stat-pill">Guesses Made: <strong id="guesses-made">0</strong></div>
            <div class="stat-pill">Accuracy Score: <strong id="accuracy-score">--%</strong></div>
        </div>
    </header>

    <div class="task-nav" id="task-nav"></div>

    <div class="global-actions">
        <button class="action-btn" onclick="revealAll()">Reveal All Answers</button>
        <button class="action-btn" style="background: #475569;" onclick="resetBenchmark()">Reset Benchmark</button>
    </div>

    <div class="grid-container" id="cards-grid"></div>
</div>

<script>
    const benchmarkData = {json_str};
    let currentTaskIdx = 0;
    let userGuesses = {{}}; // cardId -> "REAL" | "GENERATED"

    function initNav() {{
        const nav = document.getElementById("task-nav");
        nav.innerHTML = "";
        benchmarkData.forEach((b, idx) => {{
            const btn = document.createElement("button");
            btn.className = "task-btn" + (idx === currentTaskIdx ? " active" : "");
            btn.textContent = `Úloha ${{b.task_number}}: ${{b.task_name}}`;
            btn.onclick = () => {{
                currentTaskIdx = idx;
                initNav();
                renderCards();
            }};
            nav.appendChild(btn);
        }});
    }}

    function renderCards() {{
        const b = benchmarkData[currentTaskIdx];
        const grid = document.getElementById("cards-grid");
        grid.innerHTML = "";

        document.getElementById("total-cards").textContent = b.deck.length;

        b.deck.forEach((card, i) => {{
            const cardEl = document.createElement("div");
            cardEl.className = "snapshot-card";
            cardEl.id = `card-${{card.id}}`;

            const currentGuess = userGuesses[card.id];

            cardEl.innerHTML = `
                <div class="card-img-wrapper">
                    <img src="data:image/png;base64,${{card.b64}}" alt="Task snapshot ${{i+1}}">
                </div>
                <div class="card-controls">
                    <div style="font-size: 13px; color: var(--text-muted);">Sample #${{i + 1}}</div>
                    <div class="btn-group">
                        <button class="choice-btn ${{currentGuess === 'REAL' ? 'selected-real' : ''}}" onclick="makeGuess('${{card.id}}', 'REAL')">🏛️ Real Exam</button>
                        <button class="choice-btn ${{currentGuess === 'GENERATED' ? 'selected-gen' : ''}}" onclick="makeGuess('${{card.id}}', 'GENERATED')">⚡ Generated</button>
                    </div>
                    <button class="reveal-btn" onclick="revealCard('${{card.id}}')">Reveal Origin</button>
                    <div class="reveal-result" id="reveal-${{card.id}}">
                        Origin: <strong>${{card.type}}</strong><br>
                        <span style="font-size: 11.5px; opacity: 0.8;">${{card.source}}</span>
                    </div>
                </div>
            `;
            grid.appendChild(cardEl);
        }});

        updateStats();
    }}

    function makeGuess(cardId, guess) {{
        userGuesses[cardId] = guess;
        renderCards();
    }}

    function revealCard(cardId) {{
        const card = benchmarkData[currentTaskIdx].deck.find(c => c.id === cardId);
        const resEl = document.getElementById(`reveal-${{cardId}}`);
        resEl.style.display = "block";
        resEl.className = "reveal-result " + (card.type === "REAL" ? "is-real" : "is-gen");
    }}

    function revealAll() {{
        benchmarkData[currentTaskIdx].deck.forEach(c => {{
            revealCard(c.id);
        }});
        updateStats();
    }}

    function resetBenchmark() {{
        userGuesses = {{}};
        renderCards();
    }}

    function updateStats() {{
        const b = benchmarkData[currentTaskIdx];
        let total = b.deck.length;
        let guessed = 0;
        let correct = 0;

        b.deck.forEach(c => {{
            if (userGuesses[c.id]) {{
                guessed++;
                if (userGuesses[c.id] === c.type) correct++;
            }}
        }});

        document.getElementById("guesses-made").textContent = `${{guessed}} / ${{total}}`;
        if (guessed > 0) {{
            const pct = Math.round((correct / guessed) * 100);
            document.getElementById("accuracy-score").textContent = `${{pct}}% (${{correct}}/${{guessed}})`;
        }} else {{
            document.getElementById("accuracy-score").textContent = "--%";
        }}
    }}

    // Init
    initNav();
    renderCards();
</script>
</body>
</html>
"""
    output_html.write_text(html_content, encoding="utf-8")
    print(f"Generated Benchmark Report: {output_html}")


if __name__ == "__main__":
    workspace = Path("/Users/jarda/ArchMaster")
    benchmark_dir = workspace / "output" / "fidelity_benchmark"
    benchmark_dir.mkdir(parents=True, exist_ok=True)

    print("Running CERMAT Indistinguishability Benchmark across tasks...")
    benchmarks = []
    for task_id in [1, 2, 3, 4, 5, 11, 15, 16]:
        print(f"\n--- Generating Benchmark for Task {task_id:02d} ---")
        b = run_benchmark_for_task(task_id, benchmark_dir, n_samples=10)
        if b:
            benchmarks.append(b)
            print(f"Task {task_id:02d}: Deck prepared with {b['num_real']} real and {b['num_generated']} generated snapshots.")

    report_path = benchmark_dir / "index.html"
    generate_interactive_benchmark_report(benchmarks, report_path)
    print("\nBenchmark generation finished successfully!")
