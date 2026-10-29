"""Export the real numbers the Week 5 Wednesday explorer draws, from the same code the notebooks run.

Usage:
    python3 content/W05/D3/4_trainer_only/C2_W05_D03_explorer_data_INTERNAL.py

Writes C2_W05_D03_explorer_data_INTERNAL.json beside this file. scripts/build_companion.py then
inlines it into 1_in_class_training_content/demos/C2_W05_D03_leakage_timeline_explorer_STUDENT.html.
UCI Bank Marketing is cached in ~/.cache/c2_datasets exactly as the case notebooks cache it, so
nothing else is written to the repository. The script reruns the week's pipeline (the same
columns, the same seeded split, the same logistic model and today's scorer from case01) and stops
with an error if any number the case notebooks print comes out different, so the page can never
quietly disagree with case01, case02 or case03.

It exports:
  - the 8,238 validation outcomes and three score sets (customer table, + economy, + economy +
    call log), as integers out of 1,000, for the story's ranked columns and case chapter 6's curves;
  - every keep-or-drop combination of the bank's twenty columns, grouped into the eight stamp
    cards of case chapter 7 (2 to the 7th times 3 for pdays: left out, raw, or split), each with its
    validation AUC, the bill at 40 / 1,240 and the buyers in the top 1,000;
  - the call-length fifths, the calendar by month, the AUC inside each month, the sign of
    euribor3m in four neighbourhoods and the permutation importance of the honest model.
The concept pages draw invented numbers typed in the page itself.
"""
import io
import itertools
import json
import pathlib
import time
import urllib.request
import zipfile

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.inspection import permutation_importance
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "C2_W05_D03_explorer_data_INTERNAL.json"
CACHE = pathlib.Path.home() / ".cache" / "c2_datasets"
CACHE.mkdir(parents=True, exist_ok=True)
SCALE = 1000                 # story and chapter 6 scores travel as integers out of 1,000
CALL_RS, MISSED_RS = 40, 1200
THRESHOLD = CALL_RS / (CALL_RS + MISSED_RS)


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
CALL_LOG = ["duration"]
ECONOMY = ["emp.var.rate", "cons.price.idx", "cons.conf.idx", "euribor3m", "nr.employed"]
SPLIT_PDAYS = ["never_contacted", "days_since_contact"]
HONEST = PROFILE + HISTORY + SPLIT_PDAYS + ECONOMY
TRIO = ["emp.var.rate", "euribor3m", "nr.employed"]

# The eight stamp cards of case chapter 7: the bank's twenty columns, grouped the way case02 audits them.
CARDS = [
    ("profile", ["age", "job", "marital", "education"]),
    ("credit", ["default", "housing", "loan"]),
    ("dialler", ["contact", "campaign"]),
    ("calendar", ["month", "day_of_week"]),
    ("history", ["previous", "poutcome"]),
    ("economy", ECONOMY),
    ("duration", CALL_LOG),
]
PDAYS_STATES = [[], ["pdays"], SPLIT_PDAYS]       # left out, raw, split into a flag and the days
ORDER = PROFILE + HISTORY + ["pdays"] + SPLIT_PDAYS + ECONOMY + CALL_LOG   # the notebooks' column order


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


def score(columns, train, val):
    """case01's scorer: fit on training rows, score validation rows, return the day's numbers."""
    ytr, yva = (train["y"] == "yes").astype(int), (val["y"] == "yes").astype(int)
    model = logistic(columns, train).fit(train[columns], ytr)
    p = model.predict_proba(val[columns])[:, 1]
    tn, fp, fn, tp = confusion_matrix(yva, (p >= 0.5).astype(int)).ravel()
    _, fp2, fn2, _ = confusion_matrix(yva, (p >= THRESHOLD).astype(int)).ravel()
    top = yva.values[np.argsort(-p)[:1000]].sum()
    return {"auc": round(roc_auc_score(yva, p), 4), "acc": round(accuracy_score(yva, (p >= 0.5).astype(int)), 4),
            "recall": round(tp / (tp + fn), 3), "bill": int(fp2 * CALL_RS + fn2 * MISSED_RS),
            "top": int(top)}, model, p


def expect(name, got, want):
    """Stop the export when a number differs from what the notebooks print."""
    if got != want:
        raise SystemExit(f"STOP  {name}: the pipeline gives {got}, the notebooks print {want}")
    print(f"PASS  {name}: {got}")


def main():
    t0 = time.time()
    bank = load_bank()
    order = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    m = bank["month"].map({x: i + 1 for i, x in enumerate(order)})
    bank["year"] = 2008 + (m.diff().fillna(0) < 0).cumsum()
    bank["year_month"] = bank["year"].astype(str) + "-" + m.astype(str).str.zfill(2)
    bank["never_contacted"] = (bank["pdays"] == 999).astype(int)
    bank["days_since_contact"] = bank["pdays"].where(bank["pdays"] != 999, 0)
    train, val, test = week_split(bank)
    y_val = (val["y"] == "yes").astype(int).to_numpy()
    n, pos = len(val), int(y_val.sum())
    expect("rows: train, validation, test", (len(train), n, len(test)), (24712, 8238, 8238))
    expect("buyers in validation", pos, 928)

    # Case 1 (chapter 6): the junior's three feature sets.
    SETS = {"customer": PROFILE + HISTORY, "economy": PROFILE + HISTORY + ECONOMY,
            "calllog": PROFILE + HISTORY + ECONOMY + CALL_LOG}
    want = {"customer": (0.7613, 0.8971, 0.188, 279000, 404), "economy": (0.7946, 0.8986, 0.227, 280040, 460),
            "calllog": (0.9324, 0.9074, 0.420, 118800, 572)}
    sets, scores = {}, {}
    for key, cols in SETS.items():
        r, _, p = score(cols, train, val)
        expect(f"case01 {key}: AUC, accuracy, recall, bill, top 1,000",
               (r["auc"], r["acc"], r["recall"], r["bill"], r["top"]), want[key])
        sets[key] = dict(r, columns=len(cols))
        scores[key] = np.rint(p * SCALE).astype(int).tolist()
    nobody = round((n - pos) / n, 4)
    expect("accuracy of calling nobody", nobody, 0.8874)
    everyone = (n - pos) * CALL_RS
    expect("bill for calling everyone", everyone, 292400)

    # Case 2 (chapter 7): the call length, then every keep-or-drop combination of the eight cards.
    fifths = pd.qcut(bank["duration"], 5)
    by_len = bank.groupby(fifths, observed=True)["y"].apply(lambda s: round((s == "yes").mean(), 3))
    expect("yes-rate by call-length fifth", by_len.tolist(), [0.005, 0.032, 0.073, 0.125, 0.33])
    counts = bank.groupby(fifths, observed=True).size().tolist()
    edges = [float(iv.right) for iv in by_len.index]
    zero = bank.loc[bank["duration"] == 0, "y"].value_counts().to_dict()
    expect("calls of 0 seconds and how they ended", zero, {"no": 4})
    poutcome = bank.groupby("poutcome")["y"].apply(lambda s: round((s == "yes").mean(), 3)).to_dict()
    expect("yes-rate by poutcome", poutcome, {"failure": 0.142, "nonexistent": 0.088, "success": 0.651})
    expect("share of pdays at 999", round(float((bank["pdays"] == 999).mean()), 4), 0.9632)

    combos = []
    for pd_state in range(3):
        for bits in range(128):
            cols = set(PDAYS_STATES[pd_state])
            for k, (_, group) in enumerate(CARDS):
                if bits >> k & 1:
                    cols.update(group)
            cols = [c for c in ORDER if c in cols]
            if not cols:
                combos.append([0.5, everyone, round(1000 * pos / n)])
                continue
            r, _, _ = score(cols, train, val)
            combos.append([r["auc"], r["bill"], r["top"]])
        print(f"      pdays state {pd_state}: 128 fits done, {time.time() - t0:.0f} s")

    def combo(drop=(), pdays=2):
        bits = sum(1 << k for k, (name, _) in enumerate(CARDS) if name not in drop)
        return combos[pdays * 128 + bits]
    expect("audited set: AUC, bill, top 1,000", tuple(combo(("duration",))), (0.7955, 281680, 462))
    expect("leaked set with the split pdays", tuple(combo())[:3], (0.9327, 118520, 574))
    expect("audited set with raw pdays: AUC", combo(("duration",), 1)[0], 0.7951)
    expect("customer table + economy, pdays left out", combo(("duration",), 0)[0], 0.7946)
    expect("customer table + economy + call log, pdays left out", combo((), 0)[0], 0.9324)

    # Case 2 (chapter 7): the calendar, and the honest model inside one month.
    expect("distinct values of the economy columns", bank[ECONOMY].nunique().to_dict(),
           {"emp.var.rate": 10, "cons.price.idx": 26, "cons.conf.idx": 26, "euribor3m": 316, "nr.employed": 11})
    by_year = bank.groupby("year")["y"].apply(lambda s: round((s == "yes").mean(), 3)).to_dict()
    expect("yes-rate by year", by_year, {2008: 0.048, 2009: 0.195, 2010: 0.521})
    cal, _, _ = score(["year_month"], train, val)
    expect("AUC from year and month alone", cal["auc"], 0.7854)
    months = []
    for ym, g in bank.groupby("year_month"):
        months.append([ym, int(len(g)), round(float((g["y"] == "yes").mean()), 3), round(float(g["euribor3m"].mean()), 3)])
    honest, honest_model, p_honest = score(HONEST, train, val)
    expect("honest AUC", honest["auc"], 0.7955)
    v = val.assign(p=p_honest, yes=y_val)
    inside = [[k, int(len(g)), round(roc_auc_score(g["yes"], g["p"]), 3)] for k, g in v.groupby("year_month")
              if len(g) >= 100 and g["yes"].nunique() == 2]
    w = float(np.average([r[2] for r in inside], weights=[r[1] for r in inside]))
    expect("AUC inside one month, weighted", round(w, 3), 0.568)
    expect("months with 100 or more validation calls", len(inside), 9)

    # Case 3 (chapter 8): the sign of euribor3m, and what the importance chart ranks.
    y_train = (train["y"] == "yes").astype(int)
    corr = train[TRIO].corr().round(3)
    Z = pd.DataFrame(StandardScaler().fit_transform(train[TRIO]), columns=TRIO, index=train.index)

    def coefs(cols):
        fit = LogisticRegression(C=1e6, max_iter=5000).fit(Z[cols], y_train)
        return dict(zip(cols, fit.coef_[0].round(3).tolist()))
    names = honest_model.named_steps["prep"].get_feature_names_out()
    full = dict(zip(names, honest_model.named_steps["model"].coef_[0].round(3).tolist()))
    flip = [coefs(["euribor3m"]), coefs(["euribor3m", "nr.employed"]), coefs(TRIO), {c: full["num__" + c] for c in TRIO}]
    expect("euribor3m in four neighbourhoods", [f["euribor3m"] for f in flip], [-0.917, 0.144, 0.766, 0.358])
    expect("nr.employed beside euribor3m, then beside both", (flip[1]["nr.employed"], flip[2]["nr.employed"]), (-1.068, -1.193))
    expect("emp.var.rate beside both partners", flip[2]["emp.var.rate"], -0.523)
    perm = permutation_importance(honest_model, val[HONEST], y_val, scoring="roc_auc", n_repeats=5, random_state=42)
    imp = pd.Series(perm.importances_mean, index=HONEST).sort_values(ascending=False).round(4)
    expect("permutation importance, top six", imp.head(6).to_dict(),
           {"emp.var.rate": 0.3435, "cons.price.idx": 0.0585, "contact": 0.0281, "month": 0.027,
            "euribor3m": 0.0104, "nr.employed": 0.0101})
    rng = np.random.default_rng(42)
    base = roc_auc_score(y_val, honest_model.predict_proba(val[HONEST])[:, 1])
    falls = []
    for _ in range(5):
        shuffled = val[HONEST].copy()
        idx = rng.permutation(len(shuffled))
        shuffled[ECONOMY] = shuffled[ECONOMY].values[idx]
        falls.append(base - roc_auc_score(y_val, honest_model.predict_proba(shuffled)[:, 1]))
    group = round(float(np.mean(falls)), 3)
    expect("the economy shuffled as a group", group, 0.14)
    expect("the honest model's lift above a coin", round(base - 0.5, 3), 0.295)

    data = {
        "label": "UCI Bank Marketing (CC BY 4.0), validation slice of the week's seeded split (8,238 calls), "
                 "scored by the week's logistic pipeline on the feature sets of case01 to case03.",
        "n": n, "pos": pos, "scale": SCALE, "y": "".join(str(int(v)) for v in y_val),
        "scores": scores, "sets": sets, "nobody": nobody, "everyone": everyone,
        "fifths": {"rate": by_len.tolist(), "calls": counts, "edges": edges, "zero": zero.get("no", 0)},
        "poutcome": poutcome, "pdays999": round(float((bank["pdays"] == 999).mean()), 4),
        "pdaysMean": int(round(float(bank["pdays"].mean()))),
        "cards": [name for name, _ in CARDS], "combos": combos,
        "calendar": {"auc": cal["auc"], "byYear": {str(k): v for k, v in by_year.items()}, "months": months,
                     "distinct": bank[ECONOMY].nunique().to_dict(), "inside": inside, "insideAuc": round(w, 3)},
        "honest": honest,
        "flip": {"corr": {a: {b: float(corr.loc[a, b]) for b in TRIO} for a in TRIO}, "fits": flip},
        "importance": {"cols": imp.index.tolist(), "fall": imp.tolist(), "group": group,
                       "base": round(float(base), 4), "lift": round(float(base - 0.5), 3)},
    }
    OUT.write_text(json.dumps(data, separators=(",", ":")), encoding="utf-8")
    print(f"wrote {OUT.name}: {OUT.stat().st_size / 1024:.0f} KB, {len(combos)} stamp combinations, "
          f"{time.time() - t0:.0f} s")


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# python3 content/W05/D3/4_trainer_only/C2_W05_D03_explorer_data_INTERNAL.py
#     Prints one PASS line per notebook number (0.7613, 0.7946 and 0.9324 for the three feature sets;
#     0.7955, Rs 281,680 and 462 for the audited set; 0.7854 for the calendar; 0.568 inside a month;
#     -0.917, 0.144, 0.766 and 0.358 for euribor3m; 0.3435 and 0.14 for importance), fits the 384
#     stamp combinations in a few minutes, and writes C2_W05_D03_explorer_data_INTERNAL.json.
# The cached CSV deleted first
#     Downloads the bank's zip once, about 1 MB, then behaves as above.
# A pipeline change that moves any number (another seed, another column)
#     Stops at the first number that differs with "STOP <name>: the pipeline gives ..., the notebooks
#     print ...", and writes nothing, so the page keeps its last good data.
