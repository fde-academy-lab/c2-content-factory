# The Week 5 pipeline: one file, one column plan, one split, shared by every day

INTERNAL. Run on 28 October 2026 (Python 3.11, pandas 3.0.6, scikit-learn 1.9.1). Every case
notebook of the week starts from this code, copied into its first cells, so the five days quote the
same numbers. Re-run it in your notebook and print what it prints; if a number differs, trust your
run and say so in the sources file.

## The column plan, which is also the week's story

| Group | Columns | When it enters the model | Why |
|---|---|---|---|
| Profile | age, job, marital, education, default, housing, loan | Monday | known about the client before any call |
| History | contact, month, day_of_week, campaign, previous, poutcome | Monday | how this and earlier campaigns went so far |
| Economy | emp.var.rate, cons.price.idx, cons.conf.idx, euribor3m, nr.employed | Wednesday, joined from another feed | published indicators; legitimate, collinear, and they mark the calendar quarter, which Friday's staleness story uses |
| Call log | duration | Wednesday, joined by a junior | known only after the call ends: the leak |
| Set aside | pdays | Wednesday engineers it | 999 means never contacted (96 percent of rows), a sentinel, never a number of days |

## The code

```python
# The Week 5 pipeline every case notebook starts from: the same file, columns, split and baseline.
import io, zipfile, pathlib, urllib.request
import numpy as np, pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, accuracy_score, confusion_matrix

CACHE = pathlib.Path.home() / ".cache" / "c2_datasets"
CACHE.mkdir(parents=True, exist_ok=True)

def load_bank():
    """UCI Bank Marketing, bank-additional-full.csv (CC BY 4.0), cached after the first download."""
    f = CACHE / "bank-additional-full.csv"
    if not f.exists():
        url = "https://archive.ics.uci.edu/static/public/222/bank+marketing.zip"
        outer = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(url, timeout=60).read()))
        inner = zipfile.ZipFile(io.BytesIO(outer.read("bank-additional.zip")))
        f.write_bytes(inner.read("bank-additional/bank-additional-full.csv"))
    return pd.read_csv(f, sep=";")

# The customer table on the morning of the call: who the client is and how earlier campaigns went.
PROFILE = ["age", "job", "marital", "education", "default", "housing", "loan"]
HISTORY = ["contact", "month", "day_of_week", "campaign", "previous", "poutcome"]
# Joined on Wednesday from other feeds: the call log and the economic indicators.
CALL_LOG = ["duration"]
ECONOMY = ["emp.var.rate", "cons.price.idx", "cons.conf.idx", "euribor3m", "nr.employed"]

def week_split(df, seed=42):
    """Test is sealed first (20 percent, the envelope); the rest splits 75/25 into train and validation."""
    y = (df["y"] == "yes").astype(int)
    rest, test = train_test_split(df.index, test_size=0.20, stratify=y, random_state=seed)
    train, val = train_test_split(rest, test_size=0.25, stratify=y.loc[rest], random_state=seed)
    return df.loc[train], df.loc[val], df.loc[test]

def logistic(columns, df):
    # pandas 3 reads text as the "str" dtype, so test for numbers rather than for object.
    num = [c for c in columns if pd.api.types.is_numeric_dtype(df[c])]
    cat = [c for c in columns if c not in num]
    prep = ColumnTransformer([("num", StandardScaler(), num),
                              ("cat", OneHotEncoder(handle_unknown="ignore"), cat)])
    return Pipeline([("prep", prep), ("model", LogisticRegression(max_iter=2000))])

if __name__ == "__main__":
    bank = load_bank()
    train, val, test = week_split(bank)
```

## What it prints (validation slice of 8,238 rows; the test slice of 8,238 stays sealed until Friday)

| Model | Validation AUC | Accuracy at 0.5 | TP | FP | FN | TN | Precision | Recall |
|---|---|---|---|---|---|---|---|---|
| Majority baseline (call nobody) | n/a | 0.8874 | 0 | 0 | 928 | 7,310 | n/a | 0.000 |
| Logistic, customer table (Monday, Tuesday) | 0.7613 | 0.8971 | 174 | 94 | 754 | 7,216 | 0.649 | 0.188 |
| Logistic, + economy (Wednesday, honest) | 0.7946 | 0.8986 | 211 | 118 | 717 | 7,192 | 0.641 | 0.227 |
| Logistic, + economy + duration (the leak) | 0.9324 | 0.9074 | 390 | 225 | 538 | 7,085 | 0.634 | 0.420 |

Rows 41,188; train 24,712, validation 8,238, test 8,238; base rate 11.27 percent (train) and 11.26
percent (validation).

Thresholds on the customer-table model (Tuesday):

| Threshold | Called | TP | FP | FN | Precision | Recall |
|---|---|---|---|---|---|---|
| 1/31, about 0.032 (Rs 40 call against Rs 1,200 margin) | 7,438 | 913 | 6,525 | 15 | 0.123 | 0.984 |
| 0.10 | 2,754 | 616 | 2,138 | 312 | 0.224 | 0.664 |
| 0.20 | 864 | 376 | 488 | 552 | 0.435 | 0.405 |

Budget cut (Tuesday): the top 500 by score convert at 0.540 and the top 1,000 at 0.404, against
the 0.113 base rate. The cost threshold says "call nearly everyone" because a call is cheap; the
binding constraint is the budget, which is why the ranking, precision at k, carries the decision.
That is the flip condition of the cost rule.

## Traps every session meets

- pandas 3 reads text columns as the `str` dtype, so `dtype == object` finds no categoricals; test
  `pd.api.types.is_numeric_dtype` instead.
- The file uses `;` as its separator; the zip is nested.
- `unknown` is a category, not a missing value, unless a chapter decides otherwise and says why.
- The rows run in time order from May 2008 to November 2010; the random split above mixes years.
  Friday's staleness chapter splits by row order instead, and Thursday's cross-validation notes it.

## The senior ML engineer's corrections (council, measured on 28 October 2026)

1. **The random-split score is mostly the calendar.** The yes rate is 4.8 percent in 2008, 19.5 in
   2009 and 52 in 2010, and the economic columns take 10 or 11 distinct values, so they label the
   period. On a random split a model on year-month alone reaches AUC 0.795, while the ranking a call
   list needs, inside one month, is about 0.56. Monday says the random score is mostly "when";
   Wednesday names the calendar columns as a second, legal-looking leak beside `duration`.
2. **One split, used honestly.** The random split above runs Monday to Thursday with that caveat
   said aloud. Friday's reveal is the split by time (train on the earlier 70 percent of rows, score
   the later 30): the base rate jumps from about 6 to about 25 percent, the mean prediction stays
   near 0.16, the bill at the threshold overshoots, and AUC hides it. Calibration is what breaks.
3. **At Anand's costs the model barely matters.** 40 / 1,240 = 0.032 is right, but at an 11 percent
   base rate it calls about nine in ten people, and the bill is within one percent of calling
   everyone. The model earns its keep under a budget (precision at k) or a tighter cost ratio; the
   explorable lets the room move the ratio and watch that happen.
4. **"Opposite thresholds" means the same quantity on both sides.** Say it as: nudge when P(buy) is
   above 0.03; lend when P(repay) is above 0.83 (German Credit's 5:1 matrix) or 0.95 (Kalpa's 20:1).
   The cost formula assumes calibrated probabilities: `class_weight="balanced"` pushes the mean
   prediction to about 0.39 against a true 0.11 and makes the formula call everyone.
5. **Teach the leak through recall and the bill.** With `duration`, AUC goes 0.80 to 0.94 while
   accuracy only goes 0.901 to 0.912. Test the rule "known before the call": `poutcome = success`
   (65 percent yes) is just as predictive and entirely legitimate.
6. **Numbers to get right.** The unlimited tree: train 0.996, test 0.836, below the 0.887 baseline
   (the row's 100 and 61 will not appear; quote what you run). The near-tie holds: logistic 0.803,
   tuned tree 0.804, boosting 0.811, error bills within about 4 percent. euribor3m flips from
   negative alone to positive in the full model. `pdays`: use a never-contacted flag plus the days
   for the contacted ones; the raw coefficient reads the 999 sentinel.
