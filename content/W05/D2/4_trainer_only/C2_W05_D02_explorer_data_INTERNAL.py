"""Export the real numbers the Week 5 Tuesday explorer draws, from the same code the notebooks run.

Usage:
    python3 content/W05/D2/4_trainer_only/C2_W05_D02_explorer_data_INTERNAL.py

Writes C2_W05_D02_explorer_data_INTERNAL.json beside this file. scripts/build_companion.py then
inlines it into 1_in_class_training_content/demos/C2_W05_D02_threshold_explorer_STUDENT.html.
UCI Bank Marketing is cached in ~/.cache/c2_datasets exactly as the case notebooks cache it, so
nothing else is written to the repository. The script reruns the week's pipeline (the same
thirteen customer-table columns, the same seeded split, the same logistic model), exports the
8,238 validation scores, and stops with an error if any number the case notebooks print comes out
different, so the page can never quietly disagree with case01, case02 or case03. The concept
pages draw invented numbers typed in the page itself.
"""
import io
import json
import pathlib
import urllib.request
import zipfile

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "C2_W05_D02_explorer_data_INTERNAL.json"
CACHE = pathlib.Path.home() / ".cache" / "c2_datasets"
CACHE.mkdir(parents=True, exist_ok=True)
SCALE = 1_000_000          # scores travel as integers out of a million, so every count below survives
COST_FP, COST_FN, BUDGET = 40, 1200, 1000


def load_bank():
    """UCI Bank Marketing, bank-additional-full.csv (CC BY 4.0), cached after the first download."""
    f = CACHE / "bank-additional-full.csv"
    if not f.exists():
        url = "https://archive.ics.uci.edu/static/public/222/bank+marketing.zip"  # verified 28 October 2026
        outer = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(url, timeout=60).read()))
        inner = zipfile.ZipFile(io.BytesIO(outer.read("bank-additional.zip")))
        f.write_bytes(inner.read("bank-additional/bank-additional-full.csv"))
    return pd.read_csv(f, sep=";")


# The week's pipeline: the same columns, the same split and the same model every day.
PROFILE = ["age", "job", "marital", "education", "default", "housing", "loan"]
HISTORY = ["contact", "month", "day_of_week", "campaign", "previous", "poutcome"]
COLUMNS = PROFILE + HISTORY


def week_split(df, seed=42):
    """Test is sealed first (20 percent, the envelope); the rest splits 75/25 into train and validation."""
    y = (df["y"] == "yes").astype(int)
    rest, test = train_test_split(df.index, test_size=0.20, stratify=y, random_state=seed)
    train, val = train_test_split(rest, test_size=0.25, stratify=y.loc[rest], random_state=seed)
    return df.loc[train], df.loc[val], df.loc[test]


def logistic(columns, df):
    num = [c for c in columns if pd.api.types.is_numeric_dtype(df[c])]
    cat = [c for c in columns if c not in num]
    prep = ColumnTransformer([("num", StandardScaler(), num), ("cat", OneHotEncoder(handle_unknown="ignore"), cat)])
    return Pipeline([("prep", prep), ("model", LogisticRegression(max_iter=2000))])


def cells(y, p, t):
    act = p >= t
    return (int((act & (y == 1)).sum()), int((act & (y == 0)).sum()),
            int((~act & (y == 1)).sum()), int((~act & (y == 0)).sum()))


def bill(c, cfp=COST_FP, cfn=COST_FN):
    return c[1] * cfp + c[2] * cfn


def expect(name, got, want):
    """Stop the export when a number differs from what the notebooks print."""
    if got != want:
        raise SystemExit(f"STOP  {name}: the pipeline gives {got}, the notebooks print {want}")
    print(f"PASS  {name}: {got}")


def main():
    bank = load_bank()
    y = (bank["y"] == "yes").astype(int)
    train, val, test = week_split(bank)
    model = logistic(COLUMNS, bank).fit(train[COLUMNS], y.loc[train.index])
    y_val = y.loc[val.index].to_numpy()
    p_raw = model.predict_proba(val[COLUMNS])[:, 1]
    ints = np.rint(p_raw * SCALE).astype(int)
    p = ints / SCALE                                    # the scores exactly as the page will read them
    n, pos = len(y_val), int(y_val.sum())
    expect("validation clients", n, 8238)
    expect("buyers in validation", pos, 928)

    # Case 1: the do-nothing matrix and Monday's model at 0.5.
    at50 = cells(y_val, p, 0.5)
    expect("Monday's model at 0.5 (TP, FP, FN, TN)", at50, (174, 94, 754, 7216))
    expect("accuracy at 0.5", round((at50[0] + at50[3]) / n, 4), 0.8971)
    expect("accuracy of calling nobody", round((n - pos) / n, 4), 0.8874)
    expect("bill at 0.5", bill(at50), 908_560)

    # Case 2: four ways to set the line, and the saving over the best free rule by ratio.
    t_cost = COST_FP / (COST_FP + COST_FN)
    at_cost = cells(y_val, p, t_cost)
    expect("cost threshold 1 in 31 (TP, FP, FN, TN)", at_cost, (913, 6525, 15, 785))
    expect("bill at 1 in 31", bill(at_cost), 279_000)
    everyone, nobody = (n - pos) * COST_FP, pos * COST_FN
    expect("bill for calling everyone", everyone, 292_400)
    expect("bill for calling nobody", nobody, 1_113_600)
    grid = np.round(np.arange(0.001, 1.0, 0.001), 3)
    f1s = []
    for t in grid:
        a, b, c, _ = cells(y_val, p, t)
        f1s.append(2 * a / (2 * a + b + c) if a else 0)
    t_f1 = float(grid[int(np.argmax(f1s))])
    at_f1 = cells(y_val, p, t_f1)
    expect("F1 threshold", t_f1, 0.154)
    expect("calls and buyers at the F1 threshold", (at_f1[0] + at_f1[1], at_f1[0]), (1226, 454))
    expect("bill at the F1 threshold", bill(at_f1), 599_680)
    sweep = []
    for r in [30, 20, 15, 10, 8, 5, 3, 2]:
        cfn = COST_FP * r
        c = cells(y_val, p, COST_FP / (COST_FP + cfn))
        free = min(pos * cfn, (n - pos) * COST_FP)
        sweep.append([r, round((free - bill(c, COST_FP, cfn)) / free, 3)])
    expect("saving over the best free rule by ratio", [s[1] for s in sweep],
           [0.046, 0.082, 0.14, 0.281, 0.382, 0.315, 0.221, 0.163])
    bills = np.array([bill(cells(y_val, p, t)) for t in grid])
    accs = np.array([(lambda c: (c[0] + c[3]) / n)(cells(y_val, p, t)) for t in grid])
    t_acc = float(grid[int(np.argmax(accs))])

    # Case 3: the budget, precision at k, and the lists a team could make without a model.
    order = np.argsort(-p_raw, kind="stable")
    top = {k: int(y_val[order[:k]].sum()) for k in (500, 1000, 2000)}
    expect("buyers in the top 500, 1,000 and 2,000", (top[500], top[1000], top[2000]), (270, 404, 544))
    rng = np.random.default_rng(42)
    random_found = float(np.mean([y_val[rng.choice(n, BUDGET, replace=False)].sum() for _ in range(500)]))
    expect("buyers in a random 1,000 (mean of 500 draws, rounded)", round(random_found), 112)
    first_found = int(y_val[:BUDGET].sum())
    expect("buyers in the first 1,000 rows", first_found, 123)
    t_budget = float(p[order[BUDGET - 1]])
    at_budget = cells(y_val, p, t_budget)
    expect("the 1,000th score, to three places", round(t_budget, 3), 0.182)
    expect("calls and buyers at the budget's line", (at_budget[0] + at_budget[1], at_budget[0]), (1000, 404))
    budget_bill = (BUDGET - top[1000]) * COST_FP + (pos - top[1000]) * COST_FN
    expect("bill of the top 1,000", budget_bill, 652_640)
    expect("buyers scoring below 0.5", int(((p < 0.5) & (y_val == 1)).sum()), 754)

    # The week pipeline's threshold table, which the matrix page quotes at 0.10 and 0.20.
    expect("cells at 0.10 (TP, FP)", cells(y_val, p, 0.10)[:2], (616, 2138))
    expect("cells at 0.20 (TP, FP)", cells(y_val, p, 0.20)[:2], (376, 488))

    data = {
        "label": "UCI Bank Marketing (CC BY 4.0), validation slice of the week's seeded split, "
                 "scored by Monday's logistic model on the thirteen customer-table columns.",
        "bank": {"n": n, "pos": pos, "scale": SCALE, "score": ints.tolist(),
                 "y": "".join(str(int(v)) for v in y_val)},
        "facts": {
            "at50": dict(zip(["tp", "fp", "fn", "tn"], at50)),
            "cost": {"t": round(t_cost, 6), **dict(zip(["tp", "fp", "fn", "tn"], at_cost)), "bill": bill(at_cost)},
            "f1": {"t": t_f1, **dict(zip(["tp", "fp", "fn", "tn"], at_f1)), "bill": bill(at_f1)},
            "everyone": everyone, "nobody": nobody,
            "accBest": {"t": t_acc, "acc": round(float(accs.max()), 4), "bill": int(bills[int(np.argmax(accs))])},
            "billBest": {"t": float(grid[int(bills.argmin())]), "bill": int(bills.min())},
            "sweep": sweep,
            "top": {str(k): v for k, v in top.items()},
            "random1000": round(random_found, 1), "first1000": first_found,
            "budget": {"k": BUDGET, "t": round(t_budget, 6), "tp": at_budget[0], "bill": budget_bill,
                       "randomBill": round((BUDGET - random_found) * COST_FP + (pos - random_found) * COST_FN)},
            "maxScore": round(float(p.max()), 4),
        },
    }
    OUT.write_text(json.dumps(data, separators=(",", ":")), encoding="utf-8")
    print(f"wrote {OUT.name}: {n:,} clients, {pos} buyers, {OUT.stat().st_size / 1024:.0f} KB; "
          f"accuracy peaks at {t_acc:.3f}, the bill bottoms at {data['facts']['billBest']['t']:.3f}")


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# python3 content/W05/D2/4_trainer_only/C2_W05_D02_explorer_data_INTERNAL.py
#     Prints one PASS line per notebook number (174, 94, 754, 7,216 at 0.5; 7,438 calls and Rs 279,000
#     at 1 in 31; 0.154 and Rs 599,680 for F1; 404 in the top 1,000 and about 112 at random) and
#     writes C2_W05_D02_explorer_data_INTERNAL.json; a second run reads the cache and writes the same bytes.
# The cached CSV deleted first
#     Downloads the bank's zip once, about 1 MB, then behaves as above.
# A pipeline change that moves any count (another seed, another column)
#     Stops at the first number that differs with "STOP <name>: the pipeline gives ..., the notebooks
#     print ...", and writes nothing, so the page keeps its last good data.
