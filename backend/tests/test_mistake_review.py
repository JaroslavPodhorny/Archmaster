from datetime import date

from app.engines.mistake_review import review_due_date


def test_incorrect_answer_is_reviewed_tomorrow() -> None:
    assert review_due_date(
        is_correct=False, is_retry=False, today=date(2026, 8, 15)
    ) == date(2026, 8, 16)


def test_successful_retry_is_reviewed_in_three_days() -> None:
    assert review_due_date(
        is_correct=True, is_retry=True, today=date(2026, 8, 15)
    ) == date(2026, 8, 18)


def test_first_time_correct_answer_has_no_scheduled_review() -> None:
    assert review_due_date(
        is_correct=True, is_retry=False, today=date(2026, 8, 15)
    ) is None
