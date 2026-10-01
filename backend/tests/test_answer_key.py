import glob
import os

import pytest

from backend.core.answer_key import locate_solutions

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

KEYS = sorted(glob.glob(os.path.join(ROOT, 'References/Matematika/M9_*_klic.pdf')))


def _key(name: str) -> str:
    return os.path.join(ROOT, f'References/Matematika/M9_{name}_klic.pdf')


def test_all_twenty_keys_are_present():
    assert len(KEYS) == 20


@pytest.mark.parametrize('pdf_path', KEYS, ids=os.path.basename)
def test_every_key_yields_sixteen_solutions(pdf_path):
    regions = locate_solutions(pdf_path)
    assert [r.task for r in regions] == list(range(1, 17))
    for r in regions:
        assert r.segments and r.text
        assert 'CELKEM' not in r.text       # the total row is not part of task 16


def test_solution_text_comes_from_the_right_rows():
    regions = locate_solutions(_key('2025_1_termin_A'))
    assert regions[0].text.startswith('2,5krát')
    assert '4𝑛+ 5' in regions[2].text         # task 3.2
    assert regions[11].text.split()[0] == 'A'   # task 12, closed


def test_solutions_split_by_a_page_break_keep_both_parts():
    # the task number is printed again on the next page
    task10 = locate_solutions(_key('2026_2_termin_B'))[9]
    assert [s.page for s in task10.segments] == [2, 3]
    # the rows simply continue on the next page
    task4 = locate_solutions(_key('2026_nahradni_2_D'))[3]
    assert [s.page for s in task4.segments] == [0, 1]
