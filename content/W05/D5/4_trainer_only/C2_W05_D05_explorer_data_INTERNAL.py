"""Export the real numbers the Week 5 Friday explorer draws, from the same code the case notebooks run.

Usage:
    python3 content/W05/D5/4_trainer_only/C2_W05_D05_explorer_data_INTERNAL.py

Writes C2_W05_D05_explorer_data_INTERNAL.json beside this file. scripts/build_companion.py then
inlines it into 1_in_class_training_content/demos/C2_W05_D05_error_bill_explorer_STUDENT.html.
UCI Bank Marketing and German Credit are cached in ~/.cache/c2_datasets exactly as case notebooks
01 to 03 cache them, so nothing else is written to the repository. The script reruns the week's
pipeline on Wednesday's honest columns (the same seeded split, the same three models of Thursday,
the same time split and the same German Credit model), and stops with an error if any number the
case notebooks print comes out different, so the page can never quietly disagree with case01,
case02 or case03. The concept pages draw the invented gym and lender typed in the page itself.
"""
import io
import json
import pathlib
import urllib.request
import zipfile

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.datasets import fetch_openml
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GridSearchCV, StratifiedKFold, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "C2_W05_D05_explorer_data_INTERNAL.json"
CACHE = pathlib.Path.home() / ".cache" / "c2_datasets"
CACHE.mkdir(parents=True, exist_ok=True)
SCALE = 1_000_000          # scores travel as integers out of a million, so every count below survives
CALL, MISS, K = 40, 1200, 1000
COST_T = CALL / (CALL + MISS)


def load_bank():
    """UCI Bank Marketing, bank-additional-full.csv (CC BY 4.0), cached after the first download."""
    f = CACHE / "bank-additional-full.csv"
    if not f.exists():
        url = "https://archive.ics.uci.edu/static/public/222/bank+marketing.zip"  # verified 28 October 2026
        outer = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(url, timeout=60).read()))
        inner = zipfile.ZipFile(io.BytesIO(outer.read("bank-additional.zip")))
        f.write_bytes(inner.read("bank-additional/bank-additional-full.csv"))
    return pd.read_csv(f, sep=";")


def expect(name, got, want):
    """Stop the export when a number differs from what the notebooks print."""
    if got != want:
        raise SystemExit(f"STOP  {name}: the pipeline gives {got}, the notebooks print {want}")
    print(f"PASS  {name}: {got}")


def counts(y_true, p, t):
    called = np.asarray(p) >= t
    y_true = np.asarray(y_true)
    tp = int((called & (y_true == 1)).sum()); fp = int((called & (y_true == 0)).sum())
    return {"called": tp + fp, "found": tp, "wasted": fp, "missed": int(y_true.sum()) - tp,
            "bill": CALL * fp + MISS * (int(y_true.sum()) - tp)}


def found_top(yt, p, k=K):
    return int(np.asarray(yt)[np.argsort(-np.asarray(p), kind="stable")[:k]].sum())


def ints(p):
    return np.rint(np.asarray(p) * SCALE).astype(int)


# ---------------------------------------------------------------- the week's pipeline (case notebooks)
PROFILE = ["age", "job", "marital", "education", "default", "housing", "loan"]
HISTORY = ["contact", "month", "day_of_week", "campaign", "previous", "poutcome"]
ECONOMY = ["emp.var.rate", "cons.price.idx", "cons.conf.idx", "euribor3m", "nr.employed"]

bank = load_bank()
bank["never_contacted"] = (bank["pdays"] == 999).astype(int)
bank["days_since"] = bank["pdays"].where(bank["pdays"] != 999, 0)
COLS = PROFILE + HISTORY + ECONOMY + ["never_contacted", "days_since"]
X, y = bank[COLS], (bank["y"] == "yes").astype(int)
rest, test = train_test_split(bank.index, test_size=0.20, stratify=y, random_state=42)
train, val = train_test_split(rest, test_size=0.25, stratify=y.loc[rest], random_state=42)
NUM = [c for c in COLS if pd.api.types.is_numeric_dtype(bank[c])]
CAT = [c for c in COLS if c not in NUM]


def logistic():
    prep = ColumnTransformer([("num", StandardScaler(), NUM), ("cat", OneHotEncoder(handle_unknown="ignore"), CAT)])
    return Pipeline([("prep", prep), ("model", LogisticRegression(max_iter=3000))])


def main():
    yv = y[val].to_numpy()
    n, pos = len(yv), int(yv.sum())
    expect("rows in the file", len(bank), 41188)
    expect("validation clients and buyers", (n, pos), (8238, 928))

    # ---------------------------------------------------------- case 1: the bill for the near-tie
    ordinal = ColumnTransformer([("num", "passthrough", NUM),
                                 ("cat", OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1), CAT)])
    tree = GridSearchCV(Pipeline([("prep", ordinal), ("model", DecisionTreeClassifier(random_state=42))]),
                        {"model__max_depth": [5, 6, 7, 8], "model__min_samples_leaf": [20, 50, 100]},
                        scoring="roc_auc", cv=StratifiedKFold(5, shuffle=True, random_state=42))
    boost = Pipeline([("prep", ordinal), ("model", HistGradientBoostingClassifier(random_state=42))])
    models = {"logistic": logistic(), "tree": tree, "boosting": boost}
    P = {}
    for name, m in models.items():
        m.fit(X.loc[train], y[train])
        P[name] = m.predict_proba(X.loc[val])[:, 1]
    expect("tree picked by cross-validation", tree.best_params_, {"model__max_depth": 7, "model__min_samples_leaf": 20})
    auc = {k: round(roc_auc_score(yv, p), 3) for k, p in P.items()}
    expect("validation AUC", auc, {"logistic": 0.795, "tree": 0.787, "boosting": 0.803})
    expect("mean score", {k: round(float(p.mean()), 3) for k, p in P.items()}, {"logistic": 0.114, "tree": 0.114, "boosting": 0.113})

    # The page reads the scores rounded to a millionth; every count below is taken from those.
    Q = {k: ints(p) / SCALE for k, p in P.items()}
    at_cut = {k: counts(yv, Q[k], COST_T) for k in Q}
    expect("bills at 0.032", {k: v["bill"] for k, v in at_cut.items()}, {"logistic": 281680, "tree": 282840, "boosting": 283200})
    expect("calls at 0.032", {k: v["called"] for k, v in at_cut.items()}, {"logistic": 7412, "tree": 6976, "boosting": 7512})
    at50 = counts(yv, Q["logistic"], 0.5)
    expect("logistic at 0.5 (called, found, bill)", (at50["called"], at50["found"], at50["bill"]), (331, 214, 861480))
    everyone, nobody = (n - pos) * CALL, pos * MISS
    expect("calling everyone and calling nobody", (everyone, nobody), (292400, 1113600))
    top = {k: found_top(yv, Q[k]) for k in Q}
    expect("buyers in the top 1,000", top, {"logistic": 462, "tree": 469, "boosting": 475})
    cut_score = {k: round(float(np.sort(Q[k])[::-1][K - 1]), 3) for k in Q}
    expect("the logistic score at the 1,000th call", cut_score["logistic"], 0.245)
    rng = np.random.default_rng(0)
    gaps = []
    for _ in range(300):
        s = rng.integers(0, n, n)
        gaps.append(found_top(yv[s], P["boosting"][s]) - found_top(yv[s], P["logistic"][s]))
    gaps = np.array(gaps)
    lo, hi = np.percentile(gaps, [2.5, 97.5])
    expect("bootstrap gap: mean, band", (round(float(gaps.mean()), 1), round(float(lo)), round(float(hi))), (13.8, -1, 28))
    # Gains curves for the budget slider: buyers found after every 50 calls, in score order.
    gains = {}
    for k in Q:
        order = np.argsort(-Q[k], kind="stable")
        cum = np.cumsum(yv[order])
        gains[k] = [int(cum[i - 1]) for i in range(50, n + 1, 50)] + [int(cum[-1])]

    # ---------------------------------------------------------- case 2: train early, score late
    months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    m_idx = bank["month"].map({m: i for i, m in enumerate(months)}).to_numpy()
    year = 2008 + np.concatenate([[0], np.cumsum(np.diff(m_idx) < 0)])
    bank["period"] = [f"{yr}-{mi + 1:02d}" for yr, mi in zip(year, m_idx)]
    cut = int(0.7 * len(bank))
    early, late = bank.index[:cut], bank.index[cut:]
    stale = logistic().fit(X.loc[early], y[early])
    p_late = stale.predict_proba(X.loc[late])[:, 1]
    y_late = y[late].to_numpy()
    expect("early and late rows", (len(early), len(late)), (28831, 12357))
    expect("months either side of the cut", (bank.loc[early[0], "period"], bank.loc[early[-1], "period"],
                                             bank.loc[late[0], "period"], bank.loc[late[-1], "period"]),
           ("2008-05", "2009-04", "2009-04", "2010-11"))
    rates = (round(float(y[early].mean()), 3), round(float(y_late.mean()), 3), round(float(p_late.mean()), 3))
    expect("early rate, late rate, late promise", rates, (0.056, 0.246, 0.159))
    late_auc = round(roc_auc_score(y_late, p_late), 3)
    expect("AUC on the late rows", late_auc, 0.664)
    actual = counts(y_late, p_late, COST_T)
    planned = round(281680 / 8238 * len(late))
    late_every = counts(y_late, np.ones(len(late)), 0.5)["bill"]
    low = p_late < COST_T
    expect("stale bills: planned, actual, everyone", (planned, actual["bill"], late_every), (422520, 461640, 372920))
    expect("scored below 0.032, and of those who bought", (int(low.sum()), int(y_late[low].sum())), (231, 79))
    periods = sorted(bank["period"].unique())
    p_all = stale.predict_proba(X)[:, 1]
    by_month = pd.DataFrame({"period": bank["period"], "real": y, "promised": p_all}).groupby("period").agg(
        calls=("real", "size"), yes=("real", "sum"), real=("real", "mean"), promised=("promised", "mean")).reindex(periods)
    expect("months in the file", len(periods), 26)
    share = 1000 / 8238
    mon = []
    for per in sorted(bank.loc[late, "period"].unique()):
        month = bank.loc[late][bank.loc[late, "period"] == per].index
        pm, ym = stale.predict_proba(X.loc[month])[:, 1], y[month].to_numpy()
        k = max(1, round(len(month) * share)); topm = np.argsort(-pm, kind="stable")[:k]
        mon.append([per, k, round(float(pm[topm].mean()), 3), round(float(ym[topm].mean()), 3)])
    expect("monitor, first five months", mon[:5], [["2009-04", 194, 0.226, 0.309], ["2009-05", 703, 0.136, 0.142],
                                                    ["2009-06", 87, 0.451, 0.46], ["2009-07", 22, 0.324, 0.545],
                                                    ["2009-08", 93, 0.316, 0.441]])
    over = [abs(r[3] - r[2]) > 0.10 for r in mon]
    first = next(mon[i][0] for i in range(1, len(mon)) if over[i] and over[i - 1])
    expect("first month the rule fires at 10 points", first, "2009-08")

    chosen = logistic().fit(X.loc[train], y[train])
    v = bank.loc[val, ["job", "contact"]].copy()
    v["p"], v["yy"] = chosen.predict_proba(X.loc[val])[:, 1], yv
    rng = np.random.default_rng(1)

    def auc_band(t, nb=200):
        a = [roc_auc_score(t.yy.values[s], t.p.values[s]) for s in (rng.integers(0, len(t), len(t)) for _ in range(nb))
             if t.yy.values[s].min() != t.yy.values[s].max()]
        return np.percentile(a, [2.5, 97.5])
    seg = []
    for job, t in v.groupby("job"):
        blo, bhi = auc_band(t)
        seg.append([job, len(t), int(t.yy.sum()), round(roc_auc_score(t.yy, t.p), 3), round(float(blo), 2), round(float(bhi), 2)])
    seg.sort(key=lambda r: r[3])
    expect("weakest two jobs", seg[:2], [["entrepreneur", 275, 26, 0.655, 0.54, 0.81], ["blue-collar", 1834, 122, 0.707, 0.65, 0.76]])
    contact = {c: [len(t), int(t.yy.sum()), round(roc_auc_score(t.yy, t.p), 3)] for c, t in v.groupby("contact")}
    expect("AUC by contact", (contact["cellular"][2], contact["telephone"][2]), (0.779, 0.721))

    # ---------------------------------------------------------- case 3: lending, and the envelope
    credit = fetch_openml(name="credit-g", version=1, as_frame=True, data_home=str(CACHE / "openml")).frame
    repaid = (credit["class"] == "good").astype(int)
    Xc = credit.drop(columns="class")
    expect("German Credit applicants, good", (len(credit), int(repaid.sum())), (1000, 700))
    num = [c for c in Xc if pd.api.types.is_numeric_dtype(Xc[c])]
    cat = [c for c in Xc if c not in num]
    tr, va = train_test_split(credit.index, test_size=0.3, stratify=repaid, random_state=42)
    lender = Pipeline([("prep", ColumnTransformer([("num", StandardScaler(), num),
                                                   ("cat", OneHotEncoder(handle_unknown="ignore"), cat)])),
                       ("model", LogisticRegression(max_iter=3000))]).fit(Xc.loc[tr], repaid[tr])
    p_repay, yc = lender.predict_proba(Xc.loc[va])[:, 1], repaid[va].to_numpy()
    expect("German Credit validation AUC", round(roc_auc_score(yc, p_repay), 3), 0.783)
    pr = ints(p_repay) / SCALE

    def lend(t, bad, good):
        ok = pr >= t
        fa, wr = int((ok & (yc == 0)).sum()), int((~ok & (yc == 1)).sum())
        return {"approved": int(ok.sum()), "fa": fa, "wr": wr, "cost": bad * fa + good * wr}
    expect("cost at 0.5, at 5/6, approving everyone", (lend(0.5, 5, 1)["cost"], lend(5 / 6, 5, 1)["cost"], lend(0.0, 5, 1)["cost"]),
           (266, 160, 450))
    expect("approved at 0.5 and at 5/6", (lend(0.5, 5, 1)["approved"], lend(5 / 6, 5, 1)["approved"]), (226, 128))
    expect("Rohan's costs at 0.952", lend(60000 / 63000, 60000, 3000)["cost"], 690000)
    wrong_side = lend(1 / 6, 5, 1)
    expect("German Credit duration, months", (int(credit["duration"].min()), int(credit["duration"].max())), (4, 72))

    p_test = chosen.predict_proba(X.loc[test])[:, 1]
    yt = y[test].to_numpy()
    env = {"valAuc": round(roc_auc_score(yv, P["logistic"]), 3), "testAuc": round(roc_auc_score(yt, p_test), 3),
           "valTop": found_top(yv, P["logistic"]), "testTop": found_top(yt, p_test), "random": round(yt.mean() * 1000)}
    expect("the envelope", env, {"valAuc": 0.795, "testAuc": 0.801, "valTop": 462, "testTop": 482, "random": 113})

    data = {
        "label": "UCI Bank Marketing (CC BY 4.0) on Wednesday's honest columns, the week's seeded split, "
                 "Thursday's three models; German Credit (OpenML credit-g) for the lending step.",
        "bank": {"n": n, "pos": pos, "scale": SCALE, "y": "".join(str(int(t)) for t in yv),
                 "logistic": ints(P["logistic"]).tolist(), "tree": ints(P["tree"]).tolist(),
                 "boosting": ints(P["boosting"]).tolist()},
        "models": {k: {"auc": auc[k], "cut": at_cut[k], "top": top[k], "cutScore": cut_score[k], "gains": gains[k]} for k in Q},
        "at50": at50, "everyone": everyone, "nobody": nobody,
        "gap": {"values": gaps.tolist(), "mean": round(float(gaps.mean()), 1), "lo": round(float(lo)), "hi": round(float(hi))},
        "time": {"early": len(early), "late": len(late), "earlyRate": rates[0], "lateRate": rates[1], "promise": rates[2],
                 "lateAuc": late_auc, "planned": planned, "actual": actual, "everyone": late_every,
                 "below": int(low.sum()), "belowBought": int(y_late[low].sum()), "lastTrain": bank.loc[early[-1], "period"],
                 "months": [[per, int(r.calls), int(r.yes), round(float(r.real), 4), round(float(r.promised), 4)]
                            for per, r in by_month.iterrows()],
                 "monitor": mon},
        "segments": {"jobs": seg, "contact": contact, "overall": round(roc_auc_score(v.yy, v.p), 3)},
        "credit": {"n": len(yc), "good": int(yc.sum()), "auc": round(roc_auc_score(yc, p_repay), 3),
                   "p": ints(p_repay).tolist(), "y": "".join(str(int(t)) for t in yc), "wrongSide": wrong_side},
        "envelope": env,
    }
    OUT.write_text(json.dumps(data, separators=(",", ":")), encoding="utf-8")
    print(f"wrote {OUT.name}: {OUT.stat().st_size / 1024:.0f} KB; the rule fires in {first}")


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# python3 content/W05/D5/4_trainer_only/C2_W05_D05_explorer_data_INTERNAL.py
#     Prints one PASS line per notebook number (AUC 0.795, 0.787, 0.803; bills Rs 281,680, 282,840 and 283,200
#     at 0.032; 462, 469 and 475 buyers in the top 1,000; the band -1 to 28; late AUC 0.664 and the alarm in
#     2009-08; entrepreneur 0.655 and blue-collar 0.707; German Credit 266 and 160; the envelope 482 and 0.801)
#     and writes C2_W05_D05_explorer_data_INTERNAL.json; a second run reads the cache and writes the same bytes.
# The cached files deleted first
#     Downloads the bank's zip (about 1 MB) and German Credit (about 36 KB) once, then behaves as above.
# A pipeline change that moves any count (another seed, another column)
#     Stops at the first number that differs with "STOP <name>: the pipeline gives ..., the notebooks
#     print ...", and writes nothing, so the page keeps its last good data.
