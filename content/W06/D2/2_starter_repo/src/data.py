"""Step 1 of the pipeline: get Rohan's card book and turn it into one row per cardholder.

The book is UCI's Default of Credit Card Clients, licensed CC BY 4.0, and every copy of your work
cites it as: Yeh, I. (2009). Default of Credit Card Clients [Dataset]. UCI Machine Learning
Repository. https://doi.org/10.24432/C55S3H (checked 29 October 2026)
What each column means: https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients (checked 29 October 2026)
"""
import pathlib
import urllib.request
import zipfile

import pandas as pd

URL = "https://archive.ics.uci.edu/static/public/350/default+of+credit+card+clients.zip"  # checked 29 October 2026
SHEET = "default of credit card clients.xls"
DATA_DIR = pathlib.Path(__file__).resolve().parent.parent / "data"

# The name of the outcome column load_cards returns: 1 if the cardholder defaulted in October 2005,
# 0 if they paid. Every other file reads the outcome through this one name.
TARGET = "default"


def download(data_dir=DATA_DIR):
    """Download the book the first time, reuse it after that, and return the path of the sheet.

    Finished for you. The zip is about 5.5 MB and lands in data/, which .gitignore keeps out of
    your repository.
    """
    data_dir = pathlib.Path(data_dir)
    sheet = data_dir / SHEET
    if not sheet.exists():
        data_dir.mkdir(parents=True, exist_ok=True)
        zip_path = data_dir / "card_book.zip"
        urllib.request.urlretrieve(URL, zip_path)
        with zipfile.ZipFile(zip_path) as z:
            z.extract(SHEET, data_dir)
    return sheet


def read_raw(sheet=None):
    """Return the sheet the way pandas reads any sheet, before your group makes a single choice.

    Finished for you. Look hard at what it gives you before you write load_cards.
    """
    return pd.read_excel(sheet or download())


def load_cards():
    """Return Rohan's book: one row per cardholder, named columns, numbers only.

    __TODO__ Your group writes this. Start from read_raw() and compare what it gives you with the
    ticket and with the column table on the UCI page. When the function is done:
      - it returns one row for each of the 30,000 cardholders Rohan licensed;
      - every column has a name Rohan could read aloud, and the outcome column is named TARGET;
      - every value is a number.
    tests/test_pipeline.py checks the row count. Write every choice you make here, with its reason,
    in templates/DECISIONS.md.
    """
    raise NotImplementedError("load_cards in src/data.py is still a __TODO__ for your group")
