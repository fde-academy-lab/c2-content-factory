"""The live demo: pick one customer of the test book, see the chance of default, the main reason and
what each kind of mistake would cost.

Run it from the repository's top folder:

    streamlit run app/app.py

Codespaces then offers to open port 8501 in a browser tab. If the page will not open, run the same
demo with no server: python app/no_server.py
"""
import pathlib
import sys

import streamlit as st

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))  # so this file can import src
from src import data, score, train  # noqa: E402

st.title("Whom should Kalpa call before October's due date?")


@st.cache_data
def test_book():
    """The 9,000 customers the model never learned from, built once and kept between clicks."""
    learn, test = train.split_book(data.load_cards())
    return test


try:
    book = test_book()
    model = score.load_model()
except (NotImplementedError, FileNotFoundError) as not_ready:
    st.warning(f"Not ready yet: {not_ready}")
    st.stop()

row = st.number_input("Customer: a row of the test book", min_value=0, max_value=len(book) - 1, value=0)
customer = book.iloc[int(row)]
st.dataframe(customer.to_frame("value").T)

miss_cost = st.number_input("Cost of a missed default, in cost units", min_value=0.0, value=float(train.MISS_COST))
wasted_cost = st.number_input("Cost of a wasted call, in cost units", min_value=0.0, value=float(train.WASTED_COST))
# __TODO__ (ladder stage 6) Add the one control your card changes, for example an st.slider for the
# number of calls the team can make, and show what that number does to this customer.

try:
    probability, reason = score.score(customer, model)
except NotImplementedError as not_ready:
    st.warning(f"Not ready yet: {not_ready}")
    st.stop()

st.metric("Chance this customer defaults in October", f"{probability:.0%}")
st.write(f"**Main reason:** {reason}")
st.table({
    "If Kalpa": ["calls, and the customer would have paid", "skips, and the customer defaults"],
    "the mistake is": ["a wasted call", "a missed default"],
    "it costs": [wasted_cost, miss_cost],
    "chance times cost": [round((1 - probability) * wasted_cost, 2), round(probability * miss_cost, 2)],
})

# Test inputs and expected outcomes
# ---------------------------------
# A new copy of the repository, load_cards still a __TODO__
#     The page shows "Not ready yet: load_cards in src/data.py is still a __TODO__ for your group".
# load_cards written, but section 4 of the notebook never run
#     The page shows "Not ready yet: No saved model at .../models/model.joblib: run section 4 ...".
# Everything written, row 0, costs 5 and 1
#     The page shows the customer's 25 values, a chance such as 13%, one reason, and a table whose
#     last column reads (1 - chance) x 1 and chance x 5.
# Row 0, the missed-default cost raised from 5 to 20
#     The chance and the reason stay the same; only the missed-default line of the table grows,
#     four times larger.
# Row 9000 typed in the box
#     Streamlit refuses it, since the test book's rows run from 0 to 8,999.
