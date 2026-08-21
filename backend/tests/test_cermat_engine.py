"""Tests for the CERMAT Question Replica Engine."""

from __future__ import annotations

import pytest

from app.engines.cermat import (
    CermatRenderer,
    generate_cermat_task_latex,
    generate_full_cermat_test,
    generate_task,
    list_available_tasks,
)


def test_list_available_tasks():
    tasks = list_available_tasks()
    assert len(tasks) >= 12
    assert 1 in tasks
    assert 2 in tasks
    assert 3 in tasks
    assert 4 in tasks


@pytest.mark.parametrize("task_num", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16])
def test_generate_individual_tasks(task_num: int):
    # Test deterministic seed generation
    task1 = generate_task(task_num, seed=12345)
    task2 = generate_task(task_num, seed=12345)

    assert task1.task_number == task_num
    assert task1.max_points > 0
    assert task1.detailed_solution
    assert task1.scoring_rubric

    # Check reproducibility with identical seed
    assert task1.task_code == task2.task_code
    assert task1.detailed_solution == task2.detailed_solution


def test_latex_generation():
    task = generate_task(2, seed=42)
    latex_code = generate_cermat_task_latex(task, standalone=True)
    assert r"\documentclass" in latex_code
    assert r"\textbf{2}" in latex_code
    assert r"\end{document}" in latex_code


def test_full_cermat_test_generation():
    test_suite = generate_full_cermat_test(seed=999)
    assert len(test_suite) >= 12
    total_points = sum(t.max_points for t in test_suite)
    assert total_points >= 40


def test_renderer_export(tmp_path):
    renderer = CermatRenderer(output_dir=tmp_path)
    task = generate_task(1, seed=10)

    tex_path = renderer.export_latex(task)
    assert tex_path.exists()
    assert tex_path.suffix == ".tex"

    html_path = renderer.export_html_preview(task)
    assert html_path.exists()
    assert html_path.suffix == ".html"
    assert "CERMAT Úloha 1" in html_path.read_text(encoding="utf-8")
