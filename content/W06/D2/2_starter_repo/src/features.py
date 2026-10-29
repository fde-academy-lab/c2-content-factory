"""Step 2 of the pipeline: turn the book into the inputs a model reads.

Every input must exist on the day the call list is built, and your group's card may forbid some
columns. Whatever make_features does to 21,000 customers it must also do to one customer, because
score.py calls it for one customer at a time.
"""


def without(cards, columns):
    """Return a copy of the book without the named columns.

    Finished for you. It stops with a KeyError when a name is misspelled, so a typo can never
    quietly keep a column your card forbids.
    """
    missing = [name for name in columns if name not in cards.columns]
    if missing:
        raise KeyError(f"These columns are not in the book: {missing}")
    return cards.drop(columns=list(columns))


def make_features(cards):
    """Return the model's inputs for these customers: one row each, numbers only, never the outcome.

    __TODO__ Your group decides which columns go in and how each one is written. Read each column's
    meaning in the dictionary on the UCI page before you decide how to write it, and write each
    choice and its reason in templates/DECISIONS.md.
    """
    raise NotImplementedError("make_features in src/features.py is still a __TODO__ for your group")
