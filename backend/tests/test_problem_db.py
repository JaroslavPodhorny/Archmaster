import os

import pytest

from backend.core.problem_db import filter_options, search_problems


def test_build_stores_every_task_with_screenshot_and_solution(data_dir, db_path):
    result = search_problems(db_path, limit=1000)
    assert result.total == 320            # 20 booklets x 16 tasks
    assert len(result.problems) == 320
    shots = set(os.listdir(os.path.join(data_dir, 'screenshots')))
    assert shots == {p.screenshot for p in result.problems} | {p.solution for p in result.problems}
    assert len(shots) == 640


def test_problem_fields(db_path):
    p = search_problems(db_path, years=[2025], terms=['A'], order_by='oldest').problems[6]
    assert p.id == 'M9-2025-A-07'
    assert (p.year, p.term, p.task) == (2025, 'A', 7)
    assert p.description == 'Úhly u rovnoběžek, kolmice a tří přímek'
    assert p.success_pct == pytest.approx(57.1)
    assert p.screenshot == 'M9-2025-A-07.png'
    assert p.solution == 'M9-2025-A-07-reseni.png'
    assert p.source_pdf == 'M9_2025_1_termin_A_test.pdf'
    assert p.pages and all(isinstance(n, int) for n in p.pages)
    assert p.tags == sorted(p.tags) and p.tags


def test_query_ignores_diacritics_and_case(db_path):
    plain = search_problems(db_path, 'obdelnik', limit=1000)
    accented = search_problems(db_path, 'OBDÉLNÍK', limit=1000)
    assert plain.total == accented.total > 0
    assert [p.id for p in plain.problems] == [p.id for p in accented.problems]


def test_query_matches_word_prefixes_and_needs_every_word(db_path):
    one = search_problems(db_path, 'trojúhelník').total
    assert one > 0
    both = search_problems(db_path, 'trojúhelník obsah').total
    assert 0 < both < one
    assert search_problems(db_path, 'trojúhelník xyzxyz').total == 0


def test_query_of_only_punctuation_is_no_filter(db_path):
    assert search_problems(db_path, ' "*) ').total == 320


def test_list_filters_are_or_within_and_and_between(db_path):
    assert search_problems(db_path, years=[2025]).total == 64
    assert search_problems(db_path, years=[2025, 2026]).total == 128
    assert search_problems(db_path, years=[2025, 2026], terms=['A']).total == 32
    result = search_problems(db_path, years=[2025], tags=['G-PYT', 'G-UHLY'], limit=1000)
    assert result.total > 0
    for p in result.problems:
        assert p.year == 2025
        assert {'G-PYT', 'G-UHLY'} & set(p.tags)


def test_format_and_points_filters(db_path):
    result = search_problems(db_path, formats=['MC'], points=[2], limit=1000)
    assert result.total > 0
    assert all(p.format == 'MC' and p.points == 2 for p in result.problems)


def test_success_bounds_leave_out_problems_without_results(db_path):
    everything = search_problems(db_path, limit=1000).problems
    without = [p for p in everything if p.success_pct is None]
    assert len(without) == 32             # 2024 C and D: CERMAT published no item results
    bounded = search_problems(db_path, min_success=0, limit=1000)
    assert bounded.total == 320 - 32
    hard = search_problems(db_path, max_success=20, limit=1000)
    assert hard.total > 0
    assert all(p.success_pct <= 20 for p in hard.problems)


def test_ordering(db_path):
    newest = search_problems(db_path, limit=1000).problems
    assert newest[0].id == 'M9-2026-A-01'
    assert [p.year for p in newest] == sorted((p.year for p in newest), reverse=True)
    assert search_problems(db_path, order_by='oldest', limit=1).problems[0].id == 'M9-2022-A-01'

    hardest = [p.success_pct for p in search_problems(db_path, order_by='hardest', limit=1000).problems]
    known = [s for s in hardest if s is not None]
    assert known == sorted(known)
    assert hardest[len(known):] == [None] * 32    # problems without results come last
    easiest = [p.success_pct for p in search_problems(db_path, order_by='easiest', limit=1000).problems]
    assert easiest[:len(known)] == sorted(known, reverse=True)

    with pytest.raises(ValueError):
        search_problems(db_path, order_by='random')


def test_limit_and_offset_page_through_the_same_order(db_path):
    first = search_problems(db_path, years=[2026], limit=10)
    second = search_problems(db_path, years=[2026], limit=10, offset=10)
    whole = search_problems(db_path, years=[2026], limit=20)
    assert first.total == second.total == 64
    assert [p.id for p in first.problems + second.problems] == [p.id for p in whole.problems]


def test_filter_options(db_path):
    options = filter_options(db_path)
    assert set(options) == {'years', 'terms', 'formats', 'tags', 'points'}
    assert [o['value'] for o in options['years']] == [2026, 2025, 2024, 2023, 2022]
    assert all(o['count'] == 64 for o in options['years'])
    assert options['terms'] == [
        {'value': 'A', 'label': '1. řádný termín', 'count': 80},
        {'value': 'B', 'label': '2. řádný termín', 'count': 80},
        {'value': 'C', 'label': '1. náhradní termín', 'count': 80},
        {'value': 'D', 'label': '2. náhradní termín', 'count': 80},
    ]
    assert sum(o['count'] for o in options['formats']) == 320
    assert sum(o['count'] for o in options['points']) == 320
    # every option's count is what searching by it returns
    for o in options['tags']:
        assert search_problems(db_path, tags=[o['value']]).total == o['count']
    for o in options['formats']:
        assert search_problems(db_path, formats=[o['value']]).total == o['count']
