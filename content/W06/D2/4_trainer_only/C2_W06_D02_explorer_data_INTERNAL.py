"""Export the real numbers the Week 6 explorer draws, from public data downloaded in code.

Usage:
    python3 content/W06/D2/4_trainer_only/C2_W06_D02_explorer_data_INTERNAL.py

Writes C2_W06_D02_explorer_data_INTERNAL.json beside this file. scripts/build_companion.py then
inlines it into 3_explorer/C2_W06_D02_explorer_STUDENT.html. Three public files are cached in
~/.cache/c2_datasets, so nothing else is written to the repository:

- UCI Default of Credit Card Clients (Yeh 2009, CC BY 4.0): only the book's size and its October
  default count reach the page, for the story. No card answer (a threshold, a bill, an AUC, a
  trap) is exported, because the groups compute those themselves.
- UCI Bank Marketing (CC BY 4.0): Week 5's pipeline on Wednesday's honest columns, rerun exactly as
  content/W05/D5/4_trainer_only/C2_W05_D05_explorer_data_INTERNAL.py runs it, for the case page's
  worked parallel. Every number the Week 5 pack prints is asserted, so the two weeks cannot disagree.
- HMDA 2023, Delaware, originated or denied (CFPB, public domain): the leak exhibit, the interest
  rate written after the decision, measured as docs/detailing/W06_research/W06_datasets.md
  section 2.6 measured it.

The script stops with an error when any number differs from the source it is checked against, and
then writes nothing.
"""
import io
import json
import pathlib
import urllib.request
import zipfile

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "C2_W06_D02_explorer_data_INTERNAL.json"
CACHE = pathlib.Path.home() / ".cache" / "c2_datasets"
CACHE.mkdir(parents=True, exist_ok=True)
CALL, MISS, K = 40, 1200, 1000          # Week 5's prices: a wasted call and a missed buyer, in rupees
COST_T = CALL / (CALL + MISS)

CARDS_URL = "https://archive.ics.uci.edu/static/public/350/default+of+credit+card+clients.zip"  # checked 29 October 2026
BANK_URL = "https://archive.ics.uci.edu/static/public/222/bank+marketing.zip"  # checked 29 October 2026
HMDA_URL = ("https://ffiec.cfpb.gov/v2/data-browser-api/view/csv?states=DE&years=2023&actions_taken=1,3")  # checked 29 October 2026


def fetch(url):
    return urllib.request.urlopen(url, timeout=120).read()


def expect(name, got, want):
    """Stop the export when a number differs from the source it is checked against."""
    if got != want:
        raise SystemExit(f"STOP  {name}: the data gives {got}, the source says {want}")
    print(f"PASS  {name}: {got}")


# ---------------------------------------------------------------- the three loaders
def load_cards():
    f = CACHE / "default of credit card clients.xls"
    if not f.exists():
        with zipfile.ZipFile(io.BytesIO(fetch(CARDS_URL))) as z:
            f.write_bytes(z.read("default of credit card clients.xls"))
    return pd.read_excel(f, header=1)          # needs xlrd


def load_bank():
    f = CACHE / "bank-additional-full.csv"
    if not f.exists():
        outer = zipfile.ZipFile(io.BytesIO(fetch(BANK_URL)))
        inner = zipfile.ZipFile(io.BytesIO(outer.read("bank-additional.zip")))
        f.write_bytes(inner.read("bank-additional/bank-additional-full.csv"))
    return pd.read_csv(f, sep=";")


def load_hmda():
    f = CACHE / "hmda_de_2023_originated_denied.csv"
    if not f.exists():
        f.write_bytes(fetch(HMDA_URL))
    return pd.read_csv(f, low_memory=False, dtype=str)


# ---------------------------------------------------------------- the story: the card book's size only
def cards_numbers():
    cards = load_cards()
    target = "default payment next month"
    n, d = len(cards), int(cards[target].sum())
    expect("cardholders and October defaults", (n, d), (30000, 6636))
    expect("default rate", round(d / n, 4), 0.2212)
    return {"n": n, "defaults": d, "rate": round(d / n, 4), "per100": round(100 * d / n),
            "months": ["April", "May", "June", "July", "August", "September"], "year": 2005,
            "outcome": "October 2005"}


# ---------------------------------------------------------------- the case: Week 5's bank, rerun
PROFILE = ["age", "job", "marital", "education", "default", "housing", "loan"]
HISTORY = ["contact", "month", "day_of_week", "campaign", "previous", "poutcome"]
ECONOMY = ["emp.var.rate", "cons.price.idx", "cons.conf.idx", "euribor3m", "nr.employed"]


def bank_numbers():
    bank = load_bank()
    bank["never_contacted"] = (bank["pdays"] == 999).astype(int)
    bank["days_since"] = bank["pdays"].where(bank["pdays"] != 999, 0)
    cols = PROFILE + HISTORY + ECONOMY + ["never_contacted", "days_since"]
    y = (bank["y"] == "yes").astype(int)
    rest, test = train_test_split(bank.index, test_size=0.20, stratify=y, random_state=42)
    train, val = train_test_split(rest, test_size=0.25, stratify=y.loc[rest], random_state=42)

    def logistic(columns):
        num = [c for c in columns if pd.api.types.is_numeric_dtype(bank[c])]
        cat = [c for c in columns if c not in num]
        prep = ColumnTransformer([("num", StandardScaler(), num), ("cat", OneHotEncoder(handle_unknown="ignore"), cat)])
        return Pipeline([("prep", prep), ("model", LogisticRegression(max_iter=3000))]).fit(bank.loc[train, columns], y[train])

    yv = y[val].to_numpy()
    n, pos = len(yv), int(yv.sum())
    expect("bank rows", len(bank), 41188)
    expect("validation clients and buyers", (n, pos), (8238, 928))
    honest = logistic(cols)
    p = honest.predict_proba(bank.loc[val, cols])[:, 1]
    expect("honest validation AUC (Week 5 Friday)", round(roc_auc_score(yv, p), 3), 0.795)

    def cells(score, t):
        on = np.asarray(score) >= t
        tp, fp = int((on & (yv == 1)).sum()), int((on & (yv == 0)).sum())
        return {"called": tp + fp, "found": tp, "wasted": fp, "missed": pos - tp, "bill": CALL * fp + MISS * (pos - tp)}

    q = np.rint(p * 1_000_000) / 1_000_000          # the scores Week 5's page reads
    cut = cells(q, COST_T)
    expect("logistic at the cost line 0.032 (called, found, bill)", (cut["called"], cut["found"], cut["bill"]), (7412, 910, 281680))
    at50 = cells(q, 0.5)
    expect("logistic at 0.5 (called, found, bill)", (at50["called"], at50["found"], at50["bill"]), (331, 214, 861480))
    everyone, nobody = (n - pos) * CALL, pos * MISS
    expect("calling everyone and calling nobody", (everyone, nobody), (292400, 1113600))
    order = np.argsort(-q, kind="stable")
    found = np.cumsum(yv[order])
    expect("buyers in the top 1,000", int(found[K - 1]), 462)

    # Option A of stage 3: Monday's lab rule, call the clients whose previous campaign succeeded.
    rule = (bank.loc[val, "poutcome"] == "success").to_numpy()
    expect("clients the rule calls", int(rule.sum()), 284)
    r_found = int((rule & (yv == 1)).sum())
    r = {"called": int(rule.sum()), "found": r_found, "wasted": int(rule.sum()) - r_found, "missed": pos - r_found}
    r["bill"] = CALL * r["wasted"] + MISS * r["missed"]
    r["acc"] = round(accuracy_score(yv, rule.astype(int)), 4)
    expect("the rule's accuracy (Monday's lab)", r["acc"], 0.8988)
    k = r["called"]
    m_same = {"called": k, "found": int(found[k - 1]), "wasted": k - int(found[k - 1]), "missed": pos - int(found[k - 1])}
    m_same["bill"] = CALL * m_same["wasted"] + MISS * m_same["missed"]
    acc50 = round(accuracy_score(yv, (q >= 0.5).astype(int)), 4)

    # Stage 1's trap: the call's duration, written after the call ends (Week 5 Wednesday).
    leaky = logistic(cols + ["duration"])
    pl = leaky.predict_proba(bank.loc[val, cols + ["duration"]])[:, 1]
    leak_auc = round(roc_auc_score(yv, pl), 4)
    expect("AUC with the call's duration added (Week 5 Wednesday)", leak_auc, 0.9327)
    leak_top = int(yv[np.argsort(-pl, kind="stable")[:K]].sum())
    expect("buyers in the top 1,000 with duration", leak_top, 574)

    # The bill at every threshold, and buyers found after every 50 calls.
    grid = sorted([round(t, 3) for t in np.arange(0, 1.0001, 0.005)] + [COST_T])   # the cost line itself, unrounded
    bills = [[round(t, 4), cells(q, t)["called"], cells(q, t)["bill"]] for t in grid]
    gains = [int(found[i - 1]) for i in range(50, n + 1, 50)] + [int(found[-1])]

    # Stages 5 to 7: the sealed test and the months the model never saw (Week 5 Friday).
    yt = y[test].to_numpy()
    pt = honest.predict_proba(bank.loc[test, cols])[:, 1]
    env = {"testAuc": round(roc_auc_score(yt, pt), 3), "valTop": int(found[K - 1]),
           "testTop": int(yt[np.argsort(-pt, kind="stable")[:K]].sum()), "random": round(yt.mean() * 1000)}
    expect("the sealed test (Week 5 Friday)", env, {"testAuc": 0.801, "valTop": 462, "testTop": 482, "random": 113})
    months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    m_idx = bank["month"].map({m: i for i, m in enumerate(months)}).to_numpy()
    year = 2008 + np.concatenate([[0], np.cumsum(np.diff(m_idx) < 0)])
    period = [f"{yr}-{mi + 1:02d}" for yr, mi in zip(year, m_idx)]
    cut_at = int(0.7 * len(bank))
    early, late = bank.index[:cut_at], bank.index[cut_at:]
    num = [c for c in cols if pd.api.types.is_numeric_dtype(bank[c])]
    prep = ColumnTransformer([("num", StandardScaler(), num), ("cat", OneHotEncoder(handle_unknown="ignore"), [c for c in cols if c not in num])])
    stale = Pipeline([("prep", prep), ("model", LogisticRegression(max_iter=3000))]).fit(bank.loc[early, cols], y[early])
    p_late = stale.predict_proba(bank.loc[late, cols])[:, 1]
    time_ = {"lastTrain": period[early[-1]], "earlyRate": round(float(y[early].mean()), 3),
             "lateRate": round(float(y[late].mean()), 3), "promise": round(float(p_late.mean()), 3),
             "lateAuc": round(roc_auc_score(y[late], p_late), 3), "late": len(late)}
    expect("train early, score late (Week 5 Friday)", (time_["lastTrain"], time_["earlyRate"], time_["lateRate"], time_["promise"], time_["lateAuc"]),
           ("2009-04", 0.056, 0.246, 0.159, 0.664))

    return {"n": n, "pos": pos, "call": CALL, "miss": MISS, "costT": round(COST_T, 4), "auc": 0.795,
            "cut": cut, "at50": at50, "acc50": acc50, "everyone": everyone, "nobody": nobody, "top": int(found[K - 1]),
            "rule": r, "modelAtRule": m_same, "leak": {"auc": leak_auc, "honestAuc": round(roc_auc_score(yv, p), 4), "top": leak_top},
            "bills": bills, "gains": gains, "envelope": env, "time": time_}


# ---------------------------------------------------------------- the leak exhibit: HMDA
def hmda_numbers():
    df = load_hmda()
    y = (df["action_taken"] == "3").astype(int).to_numpy()
    n, d = len(df), int(y.sum())
    expect("HMDA applications and denials", (n, d), (29929, 8040))
    # W06_datasets.md quotes 98.4 and 0.7 percent, which count the blank rates only, beside an AUC of 0.982,
    # which counts blank or "Exempt". The page uses one flag throughout, no rate recorded (blank or Exempt),
    # so its shares and its AUC describe the same column.
    blank = df["interest_rate"].isna().to_numpy()
    expect("blank rates among denials and originations (W06_datasets.md)",
           (round(float(blank[y == 1].mean()), 3), round(float(blank[y == 0].mean()), 3)), (0.984, 0.007))
    missing = (df["interest_rate"].isna() | df["interest_rate"].isin(["NA", "Exempt"])).to_numpy()
    table = {"deniedMissing": int((missing & (y == 1)).sum()), "deniedHas": int((~missing & (y == 1)).sum()),
             "origMissing": int((missing & (y == 0)).sum()), "origHas": int((~missing & (y == 0)).sum()),
             "deniedExempt": int(((df["interest_rate"] == "Exempt").to_numpy() & (y == 1)).sum())}
    share_d = round(table["deniedMissing"] / d, 3)
    share_o = round(table["origMissing"] / (n - d), 3)
    expect("no rate recorded (blank or Exempt) among denials and originations", (share_d, share_o), (1.0, 0.037))
    flag_auc = round(roc_auc_score(y, missing.astype(int)), 3)
    expect("AUC of the missing-rate flag alone", flag_auc, 0.982)

    def num(s):
        return pd.to_numeric(s, errors="coerce")
    dti_map = {"<20%": 15, "20%-<30%": 25, "30%-<36%": 33, "50%-60%": 55, ">60%": 65}
    dti = num(df["debt_to_income_ratio"].map(lambda v: dti_map.get(v, v)).astype(str).str.rstrip("%"))
    X = pd.DataFrame({"loan_amount": num(df.loan_amount), "income": num(df.income), "ltv": num(df.loan_to_value_ratio),
                      "property_value": num(df.property_value), "dti": dti, "loan_term": num(df.loan_term),
                      "loan_purpose": num(df.loan_purpose), "loan_type": num(df.loan_type), "lien": num(df.lien_status),
                      "occupancy": num(df.occupancy_type), "credit_score_type": num(df.applicant_credit_score_type)})
    X_leak = X.assign(interest_rate=num(df.interest_rate), origination_charges=num(df.origination_charges))
    cv = StratifiedKFold(5, shuffle=True, random_state=0)
    app = round(float(cross_val_score(HistGradientBoostingClassifier(random_state=0), X, y, cv=cv, scoring="roc_auc").mean()), 3)
    leak = round(float(cross_val_score(HistGradientBoostingClassifier(random_state=0), X_leak, y, cv=cv, scoring="roc_auc").mean()), 4)
    expect("boosted model, application fields only", app, 0.892)
    expect("boosted model, plus interest rate and origination charges", leak, 0.9998)
    return {"n": n, "denied": d, "rate": round(d / n, 4), "table": table, "shareDenied": share_d, "shareOrig": share_o,
            "aucFlag": flag_auc, "aucApp": app, "aucLeak": leak}


def main():
    data = {
        "label": "UCI Default of Credit Card Clients (size and October defaults only); UCI Bank Marketing on Week 5's "
                 "pipeline; HMDA 2023 Delaware, originated or denied.",
        "cards": cards_numbers(),
        "bank": bank_numbers(),
        "hmda": hmda_numbers(),
    }
    OUT.write_text(json.dumps(data, separators=(",", ":")), encoding="utf-8")
    print(f"wrote {OUT.name}: {OUT.stat().st_size / 1024:.1f} KB")


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# python3 content/W06/D2/4_trainer_only/C2_W06_D02_explorer_data_INTERNAL.py
#     Prints one PASS line per checked number (30,000 cardholders and 6,636 defaults; the bank's 8,238 and 928,
#     AUC 0.795, Rs 281,680 at 0.032, 462 in the top 1,000, the rule's 284 calls at accuracy 0.8988, duration's
#     0.9327 and 574, the sealed test's 482 against 113; HMDA's 29,929 and 8,040, 98.4 and 0.7 percent blank,
#     no rate on all 8,040 denials and 3.7 percent of originations, 0.982, 0.892 and 0.9998) and writes C2_W06_D02_explorer_data_INTERNAL.json; a second run reads the cache.
# The cached files deleted first
#     Downloads the card zip (about 5.5 MB), the bank zip (about 1 MB) and the HMDA slice (about 11.5 MB) once.
# A changed source (a re-released HMDA file, a new scikit-learn that moves an AUC)
#     Stops at the first number that differs with "STOP <name>: the data gives ..., the source says ...",
#     and writes nothing, so the page keeps its last good data.
