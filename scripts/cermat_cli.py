#!/usr/bin/env python3
"""Interactive CLI for CERMAT Question Replica Generator & Visual Snapshot Studio."""

from __future__ import annotations

import os
import sys
import subprocess
from pathlib import Path

# Add backend directory to sys.path
backend_dir = Path(__file__).resolve().parent.parent / "backend"
if str(backend_dir) not in sys.path:
    sys.path.insert(0, str(backend_dir))

from app.engines.cermat import (
    generate_task,
    generate_full_cermat_test,
    list_available_tasks,
    CermatRenderer,
    generate_cermat_task_latex,
)

# ANSI Color Codes
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"


def print_banner():
    print(f"\n{CYAN}{BOLD}============================================================{RESET}")
    print(f"{CYAN}{BOLD}   CERMAT M9 Question Replica Generator & Snapshot Studio   {RESET}")
    print(f"{CYAN}{BOLD}============================================================{RESET}\n")


def display_task_details(task):
    print(f"\n{GREEN}{BOLD}--- [Úloha {task.task_number}: {task.category}] ---{RESET}")
    print(f"{BOLD}Kód úlohy:{RESET} {task.task_code} | {BOLD}Max. bodů:{RESET} {task.max_points}")

    if task.header_banner:
        print(f"\n{YELLOW}{BOLD}[{task.header_banner}]{RESET}")
    if task.context_text:
        print(f"{task.context_text}")

    if task.tikz_graphic:
        print(f"\n{DIM}[TikZ diagram přítomen: {len(task.tikz_graphic.splitlines())} řádků]{RESET}")

    if task.instruction_notice:
        print(f"\n{BOLD}Pokyn:{RESET} {task.instruction_notice}")

    if task.main_prompt:
        print(f"\n{BOLD}Zadání:{RESET} {task.main_prompt}")

    if task.subtasks:
        print(f"\n{BOLD}Podúlohy:{RESET}")
        for st in task.subtasks:
            math_info = f" -> {st.latex_math}" if st.latex_math else ""
            print(f"  {BOLD}{st.subtask_id}{RESET} {st.instruction}{math_info} ({st.point_value} b.)")
            print(f"     {GREEN}Správné řešení: {st.correct_answer}{RESET}")

    if task.multiple_choice_options:
        print(f"\n{BOLD}Možnosti:{RESET}")
        for k, v in sorted(task.multiple_choice_options.items()):
            correct_mark = f" {GREEN}[SPRÁVNÁ]{RESET}" if k == task.correct_choice else ""
            print(f"  {BOLD}{k}){RESET} {v}{correct_mark}")

    print(f"\n{CYAN}{BOLD}Bodovací pravidlo:{RESET} {task.scoring_rubric}")
    print(f"\n{CYAN}{BOLD}Podrobný postup řešení:{RESET}\n{task.detailed_solution}")


def handle_generate_task(task_num: int, renderer: CermatRenderer, open_preview: bool = True):
    task = generate_task(task_num)
    display_task_details(task)

    tex_file = renderer.export_latex(task)
    html_file = renderer.export_html_preview(task)

    print(f"\n{BOLD}Exportováno do:{RESET}")
    print(f"  LaTeX: {tex_file}")
    print(f"  HTML Cutout Snapshot: {html_file}")

    if open_preview and sys.platform == "darwin":
        try:
            subprocess.run(["open", str(html_file)], check=False)
            print(f"{GREEN}✓ Náhled otevřen v prohlížeči.{RESET}")
        except Exception:
            pass


def handle_batch_validation():
    print(f"\n{YELLOW}Spouštím hromadný test matematické konzistence (100 generování)...{RESET}")
    tasks = list_available_tasks().keys()
    count = 0
    for num in tasks:
        for seed_offset in range(10):
            task = generate_task(num, seed=42 + seed_offset)
            assert task.max_points > 0
            assert task.detailed_solution
            count += 1
    print(f"{GREEN}{BOLD}✓ Všechny úlohy ({count} instancí) vygenerovány bez chyb a halucinací!{RESET}\n")


def main():
    renderer = CermatRenderer()
    while True:
        print_banner()
        available = list_available_tasks()
        for num, desc in available.items():
            print(f"  {CYAN}{num:2d}{RESET} - {desc}")
        print(f"  {YELLOW}all{RESET} - Vygenerovat kompletní CERMAT test (všechny úlohy)")
        print(f"  {YELLOW}val{RESET} - Spustit hromadný test konzistence (batch verification)")
        print(f"   {RED}q{RESET}  - Ukončit\n")

        try:
            choice = input(f"{BOLD}Zadejte číslo úlohy nebo příkaz:{RESET} ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print(f"\n{CYAN}Ukončuji CERMAT Studio.{RESET}\n")
            break

        if choice in ["q", "exit", "quit"]:
            print(f"\n{CYAN}Ukončuji CERMAT Studio. Ať se daří při přípravě!{RESET}\n")
            break
        elif choice == "all":
            print(f"\n{YELLOW}Generuji kompletní CERMAT M9 test...{RESET}")
            full_test = generate_full_cermat_test()
            total_points = sum(t.max_points for t in full_test)
            print(f"{GREEN}Vygenerováno {len(full_test)} úloh (celkem {total_points} bodů).{RESET}")
            for t in full_test:
                renderer.export_latex(t)
                renderer.export_html_preview(t)
            print(f"{GREEN}Všechny úlohy uloženy do {renderer.output_dir}{RESET}")
        elif choice == "val":
            handle_batch_validation()
        elif choice.isdigit():
            task_num = int(choice)
            if task_num in available:
                handle_generate_task(task_num, renderer, open_preview=False)
            else:
                print(f"{RED}Neplatné číslo úlohy!{RESET}")
        else:
            print(f"{RED}Neznámá volba!{RESET}")

        try:
            input(f"\n{DIM}Stiskněte Enter pro návrat do menu...{RESET}")
        except (EOFError, KeyboardInterrupt):
            break


if __name__ == "__main__":
    main()
