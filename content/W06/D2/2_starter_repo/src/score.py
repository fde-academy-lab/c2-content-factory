"""Step 4 of the pipeline: one customer in, the chance of default and the main reason out.

The demo in app/ and the tests call score(); everything else in src/ exists to make it work.
"""
import pathlib

import joblib

MODEL_PATH = pathlib.Path(__file__).resolve().parent.parent / "models" / "model.joblib"


def save_model(model, path=MODEL_PATH):
    """Save a fitted model to models/model.joblib and return the path. Finished for you."""
    path = pathlib.Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, path)
    return path


def load_model(path=MODEL_PATH):
    """Load the saved model. Finished for you.

    Section 4 of notebooks/breadcrumbs.ipynb saves the model, so run it once in every new Codespace.
    """
    path = pathlib.Path(path)
    if not path.exists():
        raise FileNotFoundError(f"No saved model at {path}: run section 4 of notebooks/breadcrumbs.ipynb first")
    return joblib.load(path)


def score(customer, model=None):
    """Return (probability, reason) for one customer.

    customer     one row of the book from load_cards, as a pandas Series
    model        a fitted model; leave it out and the saved one is loaded
    probability  the chance this customer defaults in October, a number from 0 to 1
    reason       the main reason the customer is on the list, one short sentence a caller can say

    __TODO__ Your group writes the body: turn the customer into inputs with make_features, ask the
    model for the probability, then find the input that pushed the probability up the most and say
    it in words a caller can use.
    """
    raise NotImplementedError("score in src/score.py is still a __TODO__ for your group")
