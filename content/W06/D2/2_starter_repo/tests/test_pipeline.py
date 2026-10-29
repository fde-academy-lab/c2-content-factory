"""Four promises the pipeline keeps. Run them from the repository's top folder:

    python -m pytest

A test whose function is still a __TODO__ is skipped, and the skip names the function, so a new
copy of this repository reads 4 skipped. Each test runs as soon as your group writes the function
it checks. By build freeze on Friday the run must read 4 passed.
"""
import pytest

from src import data, score, train


def run_or_skip(function, *args):
    """Call the function, or skip the test while the function is still a __TODO__."""
    try:
        return function(*args)
    except NotImplementedError as todo:
        pytest.skip(str(todo))


def test_the_book_holds_the_30000_cardholders_rohan_licensed():
    cards = run_or_skip(data.load_cards)
    assert len(cards) == 30_000


def test_calling_nobody_costs_every_defaulter_at_the_miss_cost():
    outcome = [1, 0, 0, 1, 0]  # five invented customers: the first and the fourth defaulted
    called = [0, 0, 0, 0, 0]  # the do-nothing list calls nobody
    # Two defaulters are missed at 5 each, and no call is wasted.
    assert run_or_skip(train.error_bill, outcome, called, 5, 1) == 2 * 5


def test_a_mixed_list_pays_for_each_kind_of_mistake():
    outcome = [1, 0, 0, 1, 0]  # the same five invented customers
    called = [1, 1, 0, 0, 0]  # the list calls the first two
    # Customer 2 paid and was called: one wasted call at 1.
    # Customer 4 defaulted and was left off: one missed default at 5.
    assert run_or_skip(train.error_bill, outcome, called, 5, 1) == 1 + 5


def test_score_gives_a_probability_from_0_to_1_and_a_reason():
    cards = run_or_skip(data.load_cards)
    try:
        model = score.load_model()
    except FileNotFoundError as no_model:
        pytest.skip(str(no_model))
    probability, reason = run_or_skip(score.score, cards.iloc[0], model)
    assert 0 <= probability <= 1
    assert isinstance(reason, str) and reason.strip()
