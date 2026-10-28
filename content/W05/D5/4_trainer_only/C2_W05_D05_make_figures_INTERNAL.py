"""Draw every PNG the W05 D5 deck places, from the same data and code as the day's notebooks.

The concept figures use the invented gym and lender tables typed in notebooks ch01 to ch05; the case
figures rerun the week's pipeline on UCI Bank Marketing and German Credit, downloaded once and cached
under ~/.cache/c2_datasets, exactly as case notebooks 01 to 03 do. Nothing is written into the
repository except the PNGs in ../1_in_class_training_content/slides/img/.

Usage:
    python3 content/W05/D5/4_trainer_only/C2_W05_D05_make_figures_INTERNAL.py
"""
import io
import pathlib
import urllib.request
import zipfile

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
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

OUT = pathlib.Path(__file__).resolve().parent.parent / "1_in_class_training_content" / "slides" / "img"
OUT.mkdir(parents=True, exist_ok=True)
CACHE = pathlib.Path.home() / ".cache" / "c2_datasets"
CACHE.mkdir(parents=True, exist_ok=True)

INK, VIOLET, ROSE, GREEN, MUTED, LILAC = "#1A0F5C", "#5B3FD6", "#D63A6A", "#1F8A5B", "#6B6690", "#CFC9EE"
plt.rcParams.update({"font.size": 15, "axes.titlesize": 16, "axes.titleweight": "bold", "axes.labelsize": 14,
                     "xtick.labelsize": 13, "ytick.labelsize": 13, "legend.fontsize": 13,
                     "axes.spines.top": False, "axes.spines.right": False, "axes.edgecolor": MUTED,
                     "text.color": INK, "axes.labelcolor": INK})


def save(fig, name):
    fig.tight_layout()
    fig.savefig(OUT / name, dpi=170, facecolor="white")
    plt.close(fig)
    print("wrote", name)


# ---------------------------------------------------------------- the invented gym (chapters 1 to 5)
gym = pd.DataFrame({
    "member": ["M07", "M12", "M03", "M15", "M01", "M19", "M09", "M05", "M18", "M11",
               "M02", "M14", "M06", "M20", "M08", "M16", "M04", "M13", "M10", "M17"],
    "score_A": [0.81, 0.74, 0.66, 0.58, 0.47, 0.41, 0.35, 0.29, 0.24, 0.20,
                0.17, 0.14, 0.11, 0.09, 0.07, 0.05, 0.04, 0.03, 0.02, 0.01],
    "came_back": [1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
})
CALL_G, MISS_G = 30, 900


def gym_ranking():
    fig, ax = plt.subplots(figsize=(12, 3.0))
    ax.scatter(range(20), [0] * 20, s=520, c=[GREEN if c else LILAC for c in gym.came_back], edgecolors=INK)
    for i, r in gym.iterrows():
        ax.text(i, -0.075, f"{r.score_A:.2f}", ha="center", fontsize=12, color=MUTED)
    ax.axvline(5.5, color=ROSE, lw=3)
    ax.text(5.7, 0.06, "call the top 6: 4 of 5 returners, Rs 180", color=ROSE, fontsize=14)
    ax.set_yticks([]); ax.set_xticks([]); ax.set_ylim(-0.11, 0.1)
    ax.set_title("20 lapsed members ranked by model A (invented); green came back")
    save(fig, "C2_W05_D05_gym_ranking_STUDENT.png")


def gym_bill_sweep():
    cuts = sorted(set(gym.score_A) | {0.0, 1.01})
    rows = []
    for t in cuts:
        called = gym.score_A >= t
        w = int((called & (gym.came_back == 0)).sum()); m = int((~called & (gym.came_back == 1)).sum())
        rows.append((t, CALL_G * w, MISS_G * m))
    fig, ax = plt.subplots(figsize=(12, 4.2))
    xs = np.arange(len(rows))
    ax.bar(xs, [r[1] for r in rows], color=LILAC, label="wasted calls x Rs 30")
    ax.bar(xs, [r[2] for r in rows], bottom=[r[1] for r in rows], color=ROSE, label="missed returners x Rs 900")
    ax.set_xticks(xs[::2]); ax.set_xticklabels([f"{r[0]:.2f}" for r in rows][::2])
    i05 = [r[0] for r in rows].index(0.58)
    ax.annotate("0.5 calls 4:\nRs 1,830", (i05, 1830), (i05 - 4.5, 3400), arrowprops=dict(color=INK), fontsize=13)
    i04 = [r[0] for r in rows].index(0.04)
    ax.annotate("cheapest: Rs 360", (i04, 360), (i04 - 1, 2600), arrowprops=dict(color=GREEN), color=GREEN, fontsize=13)
    ax.set_xlabel("call when model A's score is at least"); ax.set_ylabel("bill (Rs)")
    ax.legend(frameon=False, loc="upper left")
    ax.set_title("The bill at every cut: the default looks cheap and costs five times more")
    save(fig, "C2_W05_D05_gym_bill_sweep_STUDENT.png")


def gym_monitor():
    months = ["Apr", "May", "Jun", "Jul", "Aug", "Sep"]
    promised = np.array([0.12, 0.12, 0.13, 0.12, 0.12, 0.13]); real = np.array([24, 22, 28, 40, 44, 50]) / 200
    fig, ax = plt.subplots(figsize=(11, 4.0))
    x = np.arange(6)
    ax.fill_between(x, promised - 0.05, promised + 0.05, color=LILAC, alpha=0.6, label="promise plus or minus 5 points")
    ax.plot(x, promised, "-o", color=VIOLET, lw=3, ms=9, label="promised")
    ax.plot(x, real, "-o", color=INK, lw=3, ms=9, label="real")
    ax.annotate("alarm: second month\nover the line", (4, real[4]), (1.3, 0.24), color=ROSE, fontsize=14,
                arrowprops=dict(color=ROSE, lw=2))
    ax.set_xticks(x); ax.set_xticklabels(months); ax.set_ylabel("share who came back")
    ax.legend(frameon=False, loc="upper left", fontsize=12)
    ax.set_title("200 calls a month (invented): luck moves the share about 4.6 points")
    save(fig, "C2_W05_D05_gym_monitor_STUDENT.png")


def gym_segments():
    seg = pd.DataFrame({"plan": ["student\n20 calls", "family\n80 calls", "regular\n100 calls"],
                        "calls": [20, 80, 100], "promised": [0.15, 0.12, 0.12], "returned": [6, 26, 18]})
    seg["gap"] = seg.returned / seg.calls - seg.promised
    seg["band"] = 2 * np.sqrt(seg.promised * (1 - seg.promised) / seg.calls)
    fig, ax = plt.subplots(figsize=(10, 3.6))
    ax.barh(seg.plan, seg.gap, xerr=seg.band, color=[LILAC, ROSE, LILAC], ecolor=INK, capsize=10)
    ax.axvline(0, color=INK, lw=1)
    ax.set_xlabel("real minus promised share in September, with its luck band")
    ax.set_title("Only family's gap clears its band; student's group is too small to read")
    save(fig, "C2_W05_D05_gym_segments_STUDENT.png")


def two_cuts():
    fig, ax = plt.subplots(figsize=(12, 2.8))
    ax.axhline(0, color=LILAC, lw=14)
    ax.axvline(0.032, color=VIOLET, lw=4)
    ax.text(0.045, 0.45, "nudge when\nP(buy) > 0.03", color=VIOLET, fontsize=15)
    ax.axvline(0.83, color=GREEN, lw=4)
    ax.text(0.815, 0.45, "German Credit 5 : 1\nP(repay) > 0.83", color=GREEN, fontsize=14, ha="right")
    ax.axvline(0.952, color=ROSE, lw=4)
    ax.text(0.965, -0.85, "Rohan 20 : 1\n> 0.95", color=ROSE, fontsize=14, ha="left")
    ax.set_xlim(0, 1.12); ax.set_ylim(-1, 1); ax.set_yticks([])
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0]); ax.set_xlabel("probability of the good outcome")
    ax.set_title("Same formula: cost of the cheap mistake / (cheap + expensive)")
    save(fig, "C2_W05_D05_two_cuts_STUDENT.png")


def memo_seconds():
    parts = [("claim", 4), ("evidence", 13), ("caveat", 9), ("action", 9), ("my choice", 9)]
    fig, ax = plt.subplots(figsize=(12, 2.4))
    left = 0
    for name, s in parts:
        ax.barh(0, s, left=left, color=GREEN if name == "my choice" else VIOLET, edgecolor="white", height=0.6)
        ax.text(left + s / 2, 0, f"{name}\n{s}s", ha="center", va="center", color="white", fontsize=12)
        left += s
    ax.axvline(90, color=ROSE, lw=3); ax.text(88, 0.42, "90 seconds", color=ROSE, fontsize=14, ha="right")
    ax.set_xlim(0, 92); ax.set_yticks([]); ax.set_xlabel("seconds at 140 words a minute (invented gym memo)")
    ax.set_title("The memo aloud takes 44 seconds: room for the questions")
    save(fig, "C2_W05_D05_memo_seconds_STUDENT.png")


# ---------------------------------------------------------------- the bank (case chapters 6 to 8)
def load_bank():
    f = CACHE / "bank-additional-full.csv"
    if not f.exists():
        url = "https://archive.ics.uci.edu/static/public/222/bank+marketing.zip"
        outer = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(url, timeout=60).read()))
        inner = zipfile.ZipFile(io.BytesIO(outer.read("bank-additional.zip")))
        f.write_bytes(inner.read("bank-additional/bank-additional-full.csv"))
    return pd.read_csv(f, sep=";")


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
yv = y[val].to_numpy()


def logistic():
    prep = ColumnTransformer([("num", StandardScaler(), NUM), ("cat", OneHotEncoder(handle_unknown="ignore"), CAT)])
    return Pipeline([("prep", prep), ("model", LogisticRegression(max_iter=3000))])


ordinal = ColumnTransformer([("num", "passthrough", NUM),
                             ("cat", OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1), CAT)])
models = {
    "logistic": logistic(),
    "tuned tree": GridSearchCV(Pipeline([("prep", ordinal), ("model", DecisionTreeClassifier(random_state=42))]),
                               {"model__max_depth": [5, 6, 7, 8], "model__min_samples_leaf": [20, 50, 100]},
                               scoring="roc_auc", cv=StratifiedKFold(5, shuffle=True, random_state=42)),
    "boosting": Pipeline([("prep", ordinal), ("model", HistGradientBoostingClassifier(random_state=42))]),
}
P = {}
for name, m in models.items():
    m.fit(X.loc[train], y[train])
    P[name] = m.predict_proba(X.loc[val])[:, 1]
COST_T = 40 / 1240


def bill_at(yt, p, t):
    called = np.asarray(p) >= t
    fp = int((called & (yt == 0)).sum()); fn = int((~called & (yt == 1)).sum())
    return 40 * fp + 1200 * fn


def found_top(yt, p, k=1000):
    return int(yt[np.argsort(-np.asarray(p), kind="stable")[:k]].sum())


def bank_bills():
    names = ["logistic at 0.5", "call nobody", "call everyone", "logistic", "tuned tree", "boosting"]
    vals = [bill_at(yv, P["logistic"], 0.5), bill_at(yv, np.zeros(len(yv)), 0.5), bill_at(yv, np.ones(len(yv)), 0.5),
            bill_at(yv, P["logistic"], COST_T), bill_at(yv, P["tuned tree"], COST_T), bill_at(yv, P["boosting"], COST_T)]
    fig, ax = plt.subplots(figsize=(12, 4.4))
    ax.barh(names, [v / 1e5 for v in vals], color=[ROSE, ROSE, MUTED, VIOLET, VIOLET, VIOLET])
    for i, v in enumerate(vals):
        ax.text(v / 1e5 + 0.12, i, f"Rs {v / 1e5:.2f} lakh", va="center", fontsize=13)
    ax.set_xlim(0, 13.5); ax.invert_yaxis()
    ax.set_xlabel("error bill on 8,238 validation customers (Rs lakh); the three models at 0.032")
    ax.set_title("At Rs 40 against Rs 1,200, the three models tie with calling everyone")
    save(fig, "C2_W05_D05_bank_bills_STUDENT.png")


def bank_topk():
    names = ["at random", "logistic", "tuned tree", "boosting"]
    vals = [round(yv.mean() * 1000)] + [found_top(yv, P[n]) for n in names[1:]]
    fig, ax = plt.subplots(figsize=(10, 4.0))
    ax.bar(names, vals, color=[MUTED, VIOLET, VIOLET, VIOLET])
    for i, v in enumerate(vals):
        ax.text(i, v + 8, str(v), ha="center", fontsize=15)
    ax.set_ylabel("buyers in 1,000 calls"); ax.set_ylim(0, 560)
    ax.set_title("Under the 1,000-call budget the model earns its keep")
    save(fig, "C2_W05_D05_bank_topk_STUDENT.png")


def bank_gap():
    rng = np.random.default_rng(0)
    gaps = []
    for _ in range(300):
        s = rng.integers(0, len(yv), len(yv))
        gaps.append(found_top(yv[s], P["boosting"][s]) - found_top(yv[s], P["logistic"][s]))
    gaps = np.array(gaps); lo, hi = np.percentile(gaps, [2.5, 97.5])
    fig, ax = plt.subplots(figsize=(11, 4.0))
    ax.hist(gaps, bins=25, color=LILAC, edgecolor=VIOLET)
    ax.axvspan(lo, hi, color=VIOLET, alpha=0.08); ax.axvline(0, color=ROSE, lw=3)
    ax.text(0.5, ax.get_ylim()[1] * 0.85, "zero: no gap", color=ROSE, fontsize=14)
    ax.set_xlabel("extra buyers boosting finds in 1,000 calls, 300 resamples")
    ax.set_title(f"13 more buyers, band {lo:.0f} to {hi:.0f}: inside the luck of the draw")
    save(fig, "C2_W05_D05_bank_gap_STUDENT.png")


def bank_sag():
    months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    m_idx = bank["month"].map({m: i for i, m in enumerate(months)}).to_numpy()
    year = 2008 + np.concatenate([[0], np.cumsum(np.diff(m_idx) < 0)])
    period = pd.Series([f"{yr}-{mi + 1:02d}" for yr, mi in zip(year, m_idx)])
    cut = int(0.7 * len(bank)); early = bank.index[:cut]
    stale = logistic().fit(X.loc[early], y[early])
    df = pd.DataFrame({"period": period, "real": y, "promised": stale.predict_proba(X)[:, 1]})
    per = sorted(df.period.unique())
    g = df.groupby("period").agg(real=("real", "mean"), promised=("promised", "mean")).reindex(per)
    fig, ax = plt.subplots(figsize=(13, 4.6))
    xs = np.arange(len(per))
    last_train = per.index(period[cut - 1])
    ax.axvspan(-0.5, last_train + 0.5, color=LILAC, alpha=0.35)
    ax.plot(xs, g.real, "-o", color=INK, lw=2.5, ms=6, label="real share who subscribed")
    ax.plot(xs, g.promised, "-o", color=ROSE, lw=2.5, ms=6, label="the model's promise")
    ax.fill_between(xs, g.promised, g.real, where=g.real > g.promised, color=ROSE, alpha=0.12)
    ax.text(0.3, 0.86, "trained here: May 2008 to April 2009", color=VIOLET, fontsize=13)
    ax.text(last_train + 1, 0.86, "scored here: the promise sags below reality", color=ROSE, fontsize=13)
    ax.set_xticks(xs[::3]); ax.set_xticklabels(per[::3], rotation=35)
    ax.set_ylim(0, 0.95); ax.set_ylabel("share who subscribe")
    ax.legend(frameon=False, loc="center left", bbox_to_anchor=(0.0, 0.62))
    ax.set_title("UCI Bank Marketing, month by month: the model keeps its 2008 promise")
    save(fig, "C2_W05_D05_bank_sag_STUDENT.png")


def bank_segments():
    chosen = logistic().fit(X.loc[train], y[train])
    v = bank.loc[val, ["job"]].copy()
    v["p"], v["yy"] = chosen.predict_proba(X.loc[val])[:, 1], yv
    rng = np.random.default_rng(1)
    rows = []
    for job, t in v.groupby("job"):
        a = []
        for _ in range(200):
            s = rng.integers(0, len(t), len(t))
            if t.yy.values[s].min() != t.yy.values[s].max():
                a.append(roc_auc_score(t.yy.values[s], t.p.values[s]))
        rows.append((job, int(t.yy.sum()), roc_auc_score(t.yy, t.p), *np.percentile(a, [2.5, 97.5])))
    seg = pd.DataFrame(rows, columns=["job", "buyers", "auc", "lo", "hi"]).sort_values("auc")
    fig, ax = plt.subplots(figsize=(12, 5.2))
    ax.errorbar(seg.auc, seg.job, xerr=[seg.auc - seg.lo, seg.hi - seg.auc], fmt="none", ecolor=LILAC, elinewidth=9)
    ax.scatter(seg.auc, seg.job, color=[ROSE if b < 60 else VIOLET for b in seg.buyers], s=90, zorder=3)
    for _, r in seg.iterrows():
        ax.text(1.0, r.job, f"{r.buyers} buyers", va="center", fontsize=12, color=MUTED)
    ax.axvline(roc_auc_score(v.yy, v.p), color=INK, ls="--", lw=1.5)
    ax.set_xlim(0.45, 1.1); ax.set_xlabel("AUC inside the job group, 95 percent band (rose: under 60 buyers)")
    ax.set_title("A wide band is a small group talking")
    save(fig, "C2_W05_D05_bank_segments_STUDENT.png")


def credit_threshold():
    credit = fetch_openml(name="credit-g", version=1, as_frame=True, data_home=str(CACHE / "openml")).frame
    repaid = (credit["class"] == "good").astype(int); Xc = credit.drop(columns="class")
    num = [c for c in Xc if pd.api.types.is_numeric_dtype(Xc[c])]; cat = [c for c in Xc if c not in num]
    tr, va = train_test_split(credit.index, test_size=0.3, stratify=repaid, random_state=42)
    lender = Pipeline([("prep", ColumnTransformer([("num", StandardScaler(), num),
                                                   ("cat", OneHotEncoder(handle_unknown="ignore"), cat)])),
                       ("model", LogisticRegression(max_iter=3000))]).fit(Xc.loc[tr], repaid[tr])
    p, yc = lender.predict_proba(Xc.loc[va])[:, 1], repaid[va].to_numpy()

    def cost(t, bad, good):
        lend = p >= t
        return bad * int((lend & (yc == 0)).sum()) + good * int((~lend & (yc == 1)).sum())
    ts = np.linspace(0.30, 0.99, 70)
    fig, axes = plt.subplots(1, 2, figsize=(13, 4.4))
    for ax, vals, t_star, title, unit in [
            (axes[0], [cost(t, 5, 1) for t in ts], 5 / 6, "German Credit's documented 5 : 1", "cost units"),
            (axes[1], [cost(t, 60000, 3000) / 1e5 for t in ts], 60000 / 63000, "Rohan's Rs 60,000 : Rs 3,000", "Rs lakh")]:
        ax.plot(ts, vals, color=VIOLET, lw=3)
        ax.axvline(0.5, color=MUTED, ls=":", lw=2); ax.axvline(t_star, color=ROSE, lw=3)
        ax.text(t_star - 0.015, max(vals) * 0.88, f"lend above {t_star:.2f}", color=ROSE, ha="right", fontsize=14)
        ax.set_xlabel("approve when P(repay) is above"); ax.set_ylabel(unit); ax.set_title(title)
    save(fig, "C2_W05_D05_credit_threshold_STUDENT.png")


def envelope():
    chosen = logistic().fit(X.loc[train], y[train])
    pv, pt = chosen.predict_proba(X.loc[val])[:, 1], chosen.predict_proba(X.loc[test])[:, 1]
    yt = y[test].to_numpy()
    vals = [round(yt.mean() * 1000), found_top(yv, pv), found_top(yt, pt)]
    aucs = ["", f"AUC {roc_auc_score(yv, pv):.3f}", f"AUC {roc_auc_score(yt, pt):.3f}"]
    fig, ax = plt.subplots(figsize=(10, 4.0))
    ax.bar(["at random", "validation\n(used to choose)", "test\n(opened once)"], vals, color=[MUTED, VIOLET, GREEN])
    for i, v in enumerate(vals):
        ax.text(i, v + 10, f"{v} {aucs[i]}".strip(), ha="center", fontsize=14)
    ax.set_ylabel("buyers in 1,000 calls"); ax.set_ylim(0, 580)
    ax.set_title("The envelope, opened once: the sealed number agrees")
    save(fig, "C2_W05_D05_envelope_STUDENT.png")


if __name__ == "__main__":
    for f in (gym_ranking, gym_bill_sweep, gym_monitor, gym_segments, two_cuts, memo_seconds,
              bank_bills, bank_topk, bank_gap, bank_sag, bank_segments, credit_threshold, envelope):
        f()

# Test inputs and expected outcomes
# --------------------------------
# python3 content/W05/D5/4_trainer_only/C2_W05_D05_make_figures_INTERNAL.py
#     Writes 13 PNGs into ../1_in_class_training_content/slides/img/ and prints one "wrote" line each.
#     The first run downloads UCI Bank Marketing (about 1 MB) and German Credit (about 36 KB) into
#     ~/.cache/c2_datasets; a second run reads the cache and draws the same pictures.
# With no network and an empty cache
#     load_bank() raises a URLError before any PNG of the bank is drawn; the six gym figures are already written.
