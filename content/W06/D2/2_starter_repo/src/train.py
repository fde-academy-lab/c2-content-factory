"""Step 3 of the pipeline: split the book, fit a model, and price the mistakes of a call list."""
from sklearn.model_selection import train_test_split

from src.data import TARGET

# Rohan's ask: a missed default costs about five times a wasted call. These are cost units, which
# Kalpa will price in rupees once its own call centre runs. If your card changes a cost, change it here.
MISS_COST = 5
WASTED_COST = 1


def split_book(cards, seed=42):
    """Split the book: 70 percent to learn from, 30 percent to test on. Returns (learn, test).

    Finished for you. On the full book of 30,000 in the sheet's order, the test part holds 9,000
    customers, and with seed 42 every group holds the same 9,000, so two groups' numbers can be
    compared on Saturday. stratify keeps the share of defaulters the same in both parts. Change the
    seed only to see how far your numbers move.
    """
    return train_test_split(cards, test_size=0.3, stratify=cards[TARGET], random_state=seed)


def fit(X, y):
    """Return a fitted model, learned from the inputs X and the outcomes y, that has predict_proba.

    __TODO__ Your group chooses the model: option A or option B from section 3 of the notebook.
    """
    raise NotImplementedError("fit in src/train.py is still a __TODO__ for your group")


def error_bill(outcome, called, miss_cost=MISS_COST, wasted_cost=WASTED_COST):
    """Return what a call list costs, in cost units.

    outcome  1 for each customer who defaulted, 0 for each who paid (a list or a column)
    called   1 for each customer on the list, 0 for each customer left off, in the same order
    A defaulter left off the list is a missed default, and each one costs miss_cost.
    A payer on the list is a wasted call, and each one costs wasted_cost.

    __TODO__ Your group writes the body. tests/test_pipeline.py checks it on five invented customers.
    """
    raise NotImplementedError("error_bill in src/train.py is still a __TODO__ for your group")
