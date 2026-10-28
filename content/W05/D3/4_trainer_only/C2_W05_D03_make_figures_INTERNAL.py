"""Draw every chart the W05/D3 deck places, from the same code and data as the notebooks.

Usage, from the repository root:
    python3 content/W05/D3/4_trainer_only/C2_W05_D03_make_figures_INTERNAL.py

Writes PNGs into content/W05/D3/1_in_class_training_content/slides/img/. The bank's file is read
from the week's cache (~/.cache/c2_datasets), downloaded once if it is missing. Every label is
drawn at 14 points or more on a figure about 11 inches wide, so it prints above 9 points on a slide.
"""
import io
import pathlib
import urllib.request
import warnings
import zipfile

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.inspection import permutation_importance
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

warnings.filterwarnings("ignore")
OUT = pathlib.Path(__file__).resolve().parents[1] / "1_in_class_training_content" / "slides" / "img"
OUT.mkdir(parents=True, exist_ok=True)
INK, VIOLET, ROSE, GREEN, GREY, TINT = "#1A0F5C", "#5B3FD6", "#D63A6A", "#1F8A5B", "#A9A3D2", "#EEEAFB"
plt.rcParams.update({"font.size": 15, "axes.titlesize": 17, "axes.labelsize": 15, "xtick.labelsize": 14,
                     "ytick.labelsize": 14, "axes.spines.top": False, "axes.spines.right": False,
                     "figure.dpi": 100, "savefig.dpi": 150, "savefig.bbox": "tight"})

CACHE = pathlib.Path.home() / ".cache" / "c2_datasets"
CACHE.mkdir(parents=True, exist_ok=True)
PROFILE = ["age", "job", "marital", "education", "default", "housing", "loan"]
HISTORY = ["contact", "month", "day_of_week", "campaign", "previous", "poutcome"]
CALL_LOG = ["duration"]
ECONOMY = ["emp.var.rate", "cons.price.idx", "cons.conf.idx", "euribor3m", "nr.employed"]
CALL_RS, MISSED_RS = 40, 1200


def load_bank():
    f = CACHE / "bank-additional-full.csv"
    if not f.exists():
        url = "https://archive.ics.uci.edu/static/public/222/bank+marketing.zip"  # verified 28 October 2026
        outer = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(url, timeout=60).read()))
        inner = zipfile.ZipFile(io.BytesIO(outer.read("bank-additional.zip")))
        f.write_bytes(inner.read("bank-additional/bank-additional-full.csv"))
    return pd.read_csv(f, sep=";")


def week_split(df, seed=42):
    y = (df["y"] == "yes").astype(int)
    rest, test = train_test_split(df.index, test_size=0.20, stratify=y, random_state=seed)
    train, val = train_test_split(rest, test_size=0.25, stratify=y.loc[rest], random_state=seed)
    return df.loc[train], df.loc[val], df.loc[test]


def logistic(columns, df):
    num = [c for c in columns if pd.api.types.is_numeric_dtype(df[c])]
    cat = [c for c in columns if c not in num]
    prep = ColumnTransformer([("num", StandardScaler(), num),
                              ("cat", OneHotEncoder(handle_unknown="ignore"), cat)])
    return Pipeline([("prep", prep), ("model", LogisticRegression(max_iter=2000))])


def save(fig, name):
    fig.savefig(OUT / name)
    plt.close(fig)
    print("wrote", name)


def card(ax, x, y, w, h, text, face, edge, colour, size=14, weight="normal"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
                                facecolor=face, edgecolor=edge, linewidth=2))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=size, color=colour,
            weight=weight)


def week_timeline(state):
    """The week's one growing picture: past rows, the cut, the prediction moment, the outcome window."""
    fig, ax = plt.subplots(figsize=(13, 4.6))
    ax.set_xlim(0, 13); ax.set_ylim(0, 4.6); ax.axis("off")
    ax.add_patch(plt.Rectangle((0.3, 2.3), 5.2, 0.7, color=TINT))
    ax.text(2.9, 2.65, "past rows: train and validation", ha="center", va="center", fontsize=15, color=INK)
    ax.plot([5.7, 5.7], [1.25, 3.9], color=GREY, lw=2, ls="--")
    ax.text(5.6, 4.05, "the cut", ha="right", fontsize=14, color=INK)
    ax.plot([7.0, 7.0], [1.25, 3.9], color=INK, lw=4)
    ax.text(7.1, 4.05, "prediction moment", ha="left", fontsize=15, color=INK, weight="bold")
    ax.add_patch(plt.Rectangle((7.2, 2.3), 5.4, 0.7, color="#F6F1FF"))
    ax.text(9.9, 2.65, "outcome window: did they buy?", ha="center", va="center", fontsize=15, color=INK)
    ax.annotate("", xy=(12.8, 1.9), xytext=(0.3, 1.9), arrowprops=dict(arrowstyle="->", color=GREY, lw=1.5))
    ax.text(0.3, 1.45, "Mon: split, baseline.  Tue: threshold.", fontsize=13, color="#6B6690")
    if state == "tuesday":
        card(ax, 3.2, 0.35, 6.6, 0.75, "Wed: which columns sit left of the line?", "#FFF7E6", "#C98A00",
             "#5C3D00", size=15, weight="bold")
    else:
        card(ax, 0.6, 0.35, 2.9, 0.75, "customer table", "#E8F5EE", GREEN, GREEN, size=14, weight="bold")
        card(ax, 3.7, 0.35, 2.9, 0.75, "economy (flag)", "#E8F5EE", GREEN, GREEN, size=14, weight="bold")
        card(ax, 8.0, 0.35, 3.6, 0.75, "duration: call ends", "#FCEBF0", ROSE, ROSE, size=15, weight="bold")
    save(fig, f"C2_W05_D03_week_timeline_{state}_STUDENT.png")


def concept_figures():
    nudge = pd.Timestamp("2026-11-01")
    m = pd.DataFrame({
        "member": ["Asha", "Bilal", "Chitra", "Dev", "Esha", "Farid", "Gauri", "Hari"],
        "first": pd.to_datetime(["2024-11-02", "2026-08-20", "2023-05-10", "2026-10-05", "2025-01-15",
                                 "2024-06-01", "2025-12-01", "2022-02-11"]),
        "last": pd.to_datetime(["2026-10-29", "2026-10-25", "2026-03-14", "2026-10-30", "2026-07-01",
                                "2026-10-20", "2026-09-30", "2025-12-24"]),
        "orders": [24, 6, 30, 3, 8, 12, 10, 40],
        "spend": [16800, 4200, 19500, 2400, 12000, 3600, 7000, 26000]})
    rec = (nudge - m["last"]).dt.days
    opm = m["orders"] / ((nudge - m["first"]).dt.days / 30.4)
    fig, ax = plt.subplots(figsize=(11, 5))
    ax.scatter(rec, opm, s=m["spend"] / 30, color=[ROSE if r > 120 else VIOLET for r in rec], alpha=0.7)
    for name, x, y in zip(m["member"], rec, opm):
        ax.annotate(name, (x, y), xytext=(10, 6), textcoords="offset points", fontsize=15)
    ax.set_xlabel("recency: days since last order"); ax.set_ylabel("orders per month")
    ax.set_title("Hari spent the most and is the coldest (invented members)")
    save(fig, "C2_W05_D03_ch1_members_STUDENT.png")

    X = pd.DataFrame({"spend_90d": [9000, 9200, 7000, 2500, 4500, 3000], "visits_30d": [2, 9, 2, 8, 6, 3]},
                     dtype=float)
    Z = (X - X.mean()) / X.std(ddof=0)
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8))
    for ax, T, title in [(axes[0], X, "Raw, equal axes: rupees only"), (axes[1], Z, "Standardised: both count")]:
        ax.scatter(T["spend_90d"], T["visits_30d"], s=180, color=VIOLET)
        for i, r in T.iterrows():
            ax.annotate("ABCDEF"[i], (r["spend_90d"], r["visits_30d"]), xytext=(8, 6),
                        textcoords="offset points", fontsize=16)
        ax.set_title(title); ax.set_xlabel("spend_90d"); ax.set_ylabel("visits_30d")
    axes[0].set_xlim(0, 10500); axes[0].set_ylim(0, 10500)
    axes[0].text(500, 6000, "A's nearest: B\n(Rs 200 apart,\nvisits 2 vs 9)", fontsize=14, color=ROSE)
    axes[1].text(-1.4, 0.4, "A's nearest: C\n(both visit twice)", fontsize=14, color=GREEN)
    save(fig, "C2_W05_D03_ch2_scaling_STUDENT.png")

    events = [("first order\n(day -400)", -400, GREEN), ("last order\n(day -9)", -9, GREEN),
              ("orders_90d\nwritten (day -1)", -1, GREEN), ("order placed\n(day +5)", 5, GREY),
              ("delivered\n(day +8)", 8, GREY), ("payment clears:\nsettlement_status\n(day +12)", 12, ROSE),
              ("outcome window\ncloses (day +90)", 90, GREY)]
    spot = {-400: -2.5, -9: -1.5, -1: -0.6, 5: 0.45, 8: 0.95, 12: 1.45, 90: 1.95}  # even spacing, no collisions
    pos = lambda t: spot[t]
    fig, ax = plt.subplots(figsize=(13, 4))
    ax.axhline(0, color=GREY, lw=1.5); ax.axvline(0, color=INK, lw=4); ax.axvspan(0, 2.45, color=ROSE, alpha=0.07)
    for i, (name, t, c) in enumerate(events):
        y = 0.32 if i % 2 else -0.62
        ax.plot(pos(t), 0, "o", color=c, ms=14)
        ax.text(pos(t), y, name, ha="center", fontsize=14, color=c if c != GREY else INK)
    ax.text(0.04, 0.78, "nudge morning", color=INK, fontsize=16, weight="bold")
    ax.set_xlim(-2.9, 2.45); ax.set_ylim(-1.1, 1.0); ax.axis("off")
    ax.set_title("Green is known on the nudge morning; red is written after it (invented member)")
    save(fig, "C2_W05_D03_ch3_member_timeline_STUDENT.png")

    fig, ax = plt.subplots(figsize=(11, 4.2))
    labels = ["settlement rule,\ntraining table", "settlement rule,\nnudge morning", "orders_90d >= 2,\nhonest", "predict\nnobody buys"]
    vals = [12, 6, 10, 6]
    ax.bar(labels, vals, color=[ROSE, ROSE, GREEN, GREY])
    for i, v in enumerate(vals):
        ax.text(i, v + 0.2, f"{v} of 12", ha="center", fontsize=16)
    ax.set_ylim(0, 13.5); ax.set_ylabel("members right")
    ax.set_title("The perfect rule collapses when it meets the morning (invented)")
    save(fig, "C2_W05_D03_ch3_rule_counts_STUDENT.png")

    cols = [("days_since_last_order", -1, "keep"), ("orders_90d", -1, "keep"), ("avg_basket_rs", -1, "keep"),
            ("city", -400, "keep"), ("app_visits_7d", -1, "keep"), ("loyalty_tier", -1, "fix"),
            ("member_id", -400, "drop"), ("coupon_redeemed", 3, "drop"), ("settlement_status", 12, "drop")]
    colour = {"keep": GREEN, "fix": VIOLET, "drop": ROSE}
    fig, ax = plt.subplots(figsize=(13, 5.4))
    ax.axvline(0, color=INK, lw=4); ax.text(0.06, 8.75, "nudge morning", color=INK, fontsize=15, weight="bold")
    for i, (name, t, v) in enumerate(cols):
        x = np.sign(t) * np.log10(abs(t) + 1)
        ax.plot(x, i, "o", color=colour[v], ms=13)
        left = -1 < x < 0
        ax.text(x + (-0.1 if left else 0.1), i, f"{name}  ({v})", va="center", fontsize=14, color=colour[v],
                ha="right" if left else "left")
    ax.set_yticks([]); ax.set_xlim(-3, 3.9); ax.set_ylim(-0.8, 9.3)
    ax.set_xticks([-2.6, -0.3, 0.6, 1.1]); ax.set_xticklabels(["signup", "last night", "+3 days", "+12 days"])
    ax.set_title("Nine candidate columns on the timeline: keep, fix, drop (invented)")
    save(fig, "C2_W05_D03_ch4_audit_timeline_STUDENT.png")

    fig, ax = plt.subplots(figsize=(11, 4))
    names = ["visits shuffled", "searches shuffled", "both shuffled"]
    lost = [2, 4, 8]
    ax.barh(names, lost, color=[VIOLET, VIOLET, INK])
    for i, x in enumerate(lost):
        ax.text(x + 0.15, i, f"{x} answers lost of 11", va="center", fontsize=15)
    ax.set_xlim(0, 11); ax.invert_yaxis()
    ax.set_title("Twins alone cost 2 and 4; together they cost 8 (invented)")
    save(fig, "C2_W05_D03_ch5_twins_STUDENT.png")


def case_figures():
    bank = load_bank()
    yes = bank["y"].eq("yes")
    calls = pd.cut(bank["campaign"], [0, 1, 2, 3, 100], labels=["1", "2", "3", "4+"])
    earlier = pd.cut(bank["previous"], [-1, 0, 1, 100], labels=["0", "1", "2+"])
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.4))
    for ax, grp, title in [(axes[0], calls, "calls this campaign"), (axes[1], earlier, "calls in earlier campaigns")]:
        r = yes.groupby(grp, observed=True).mean()
        ax.bar(r.index.astype(str), r.values, color=VIOLET)
        for i, v in enumerate(r.values):
            ax.text(i, v + 0.01, f"{v:.0%}", ha="center", fontsize=15)
        ax.set_ylim(0, 0.6); ax.set_title(f"yes-rate by {title}")
    save(fig, "C2_W05_D03_ch1_bank_counts_STUDENT.png")

    bank["never_contacted"] = (bank["pdays"] == 999).astype(int)
    bank["days_since_contact"] = bank["pdays"].where(bank["pdays"] != 999, 0)
    order = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    mo = bank["month"].map({x: i + 1 for i, x in enumerate(order)})
    bank["year_month"] = (2008 + (mo.diff().fillna(0) < 0).cumsum()).astype(str) + "-" + mo.astype(str).str.zfill(2)
    train, val, _ = week_split(bank)
    ytr, yva = train["y"].eq("yes").astype(int), val["y"].eq("yes").astype(int)
    thr = CALL_RS / (CALL_RS + MISSED_RS)

    def fit(cols):
        model = logistic(cols, train).fit(train[cols], ytr)
        p = model.predict_proba(val[cols])[:, 1]
        tn, fp, fn, tp = confusion_matrix(yva, (p >= 0.5).astype(int)).ravel()
        _, fp2, fn2, _ = confusion_matrix(yva, (p >= thr).astype(int)).ravel()
        return dict(auc=roc_auc_score(yva, p), acc=((p >= 0.5).astype(int) == yva).mean(), recall=tp / (tp + fn),
                    bill=fp2 * CALL_RS + fn2 * MISSED_RS), model, p

    sets = {"customer\ntable": PROFILE + HISTORY, "+ economy": PROFILE + HISTORY + ECONOMY,
            "+ economy\n+ call log": PROFILE + HISTORY + ECONOMY + CALL_LOG}
    res = {k: fit(v)[0] for k, v in sets.items()}
    fig, axes = plt.subplots(1, 2, figsize=(13, 4.8))
    for ax, key, title in [(axes[0], "auc", "Validation AUC jumps"), (axes[1], "acc", "Accuracy at 0.5 barely moves")]:
        vals = [res[k][key] for k in sets]
        ax.bar(list(sets), vals, color=[GREY, VIOLET, ROSE])
        for i, v in enumerate(vals):
            ax.text(i, v + 0.01, f"{v:.3f}", ha="center", fontsize=16)
        ax.set_ylim(0.5, 1.02); ax.set_title(title)
    axes[1].axhline(0.8874, color=INK, ls="--", lw=1.5)
    axes[1].text(-0.45, 0.855, "call nobody: 0.887", fontsize=14)
    save(fig, "C2_W05_D03_case1_auc_accuracy_STUDENT.png")

    fig, axes = plt.subplots(1, 2, figsize=(13, 4.6))
    rec = [res[k]["recall"] for k in sets]
    bills = [res[k]["bill"] / 1e5 for k in sets]
    axes[0].bar(list(sets), rec, color=[GREY, VIOLET, ROSE]); axes[0].set_ylim(0, 0.55)
    axes[0].set_title("Recall at 0.5 nearly doubles")
    for i, v in enumerate(rec):
        axes[0].text(i, v + 0.01, f"{v:.2f}", ha="center", fontsize=16)
    axes[1].bar(list(sets), bills, color=[GREY, VIOLET, ROSE]); axes[1].set_ylim(0, 3.5)
    axes[1].set_title("Bill on 8,238 calls, Rs lakh")
    for i, v in enumerate(bills):
        axes[1].text(i, v + 0.06, f"Rs {v:.2f} lakh", ha="center", fontsize=15)
    save(fig, "C2_W05_D03_case1_recall_bill_STUDENT.png")

    fifths = pd.qcut(bank["duration"], 5)
    r = yes.groupby(fifths, observed=True).mean()
    fig, ax = plt.subplots(figsize=(11, 4.4))
    labels = ["0 to 89 s", "90 to 146 s", "147 to 222 s", "223 to 368 s", "369 s and up"]
    ax.bar(labels, r.values, color=[ROSE] * 5)
    for i, v in enumerate(r.values):
        ax.text(i, v + 0.008, f"{v:.1%}", ha="center", fontsize=16)
    ax.set_ylim(0, 0.4); ax.set_title("Yes-rate by call length, in five equal groups of calls")
    save(fig, "C2_W05_D03_case2_duration_fifths_STUDENT.png")

    rate = bank.groupby("year_month")["y"].apply(lambda s: s.eq("yes").mean())
    eur = bank.groupby("year_month")["euribor3m"].mean()
    fig, ax = plt.subplots(figsize=(13, 4.8))
    ax.bar(range(len(rate)), rate.values, color=VIOLET, alpha=0.8, label="yes-rate")
    ax2 = ax.twinx(); ax2.plot(range(len(eur)), eur.values, color=ROSE, lw=3, label="euribor3m (right)")
    ax2.spines["right"].set_visible(True)
    ax.set_xticks(range(0, len(rate), 4)); ax.set_xticklabels(rate.index[::4], fontsize=13)
    ax.set_ylim(0, 0.85); ax2.set_ylim(0, 6.5)
    ax.set_title("The yes-rate moves with the month; the rate column stamps the month")
    fig.legend(loc="upper center", bbox_to_anchor=(0.5, 0.86), ncol=2, fontsize=14, frameon=False)
    save(fig, "C2_W05_D03_case2_calendar_STUDENT.png")

    honest_cols = PROFILE + HISTORY + ["never_contacted", "days_since_contact"] + ECONOMY
    honest, hmodel, hp = fit(honest_cols)
    leaked = fit(honest_cols + CALL_LOG)[0]
    calendar = fit(["year_month"])[0]
    v = val.assign(p=hp, yy=yva)
    rows = [(len(g), roc_auc_score(g["yy"], g["p"])) for _, g in v.groupby("year_month")
            if len(g) >= 100 and g["yy"].nunique() == 2]
    within = np.average([a for _, a in rows], weights=[n for n, _ in rows])
    fig, ax = plt.subplots(figsize=(11, 4.4))
    labels = ["year and month\nalone", "honest model,\nrandom split", "honest model,\ninside one month"]
    vals = [calendar["auc"], honest["auc"], within]
    ax.bar(labels, vals, color=[GREY, VIOLET, INK])
    for i, x in enumerate(vals):
        ax.text(i, x + 0.01, f"{x:.2f}", ha="center", fontsize=17)
    ax.axhline(0.5, color=ROSE, ls="--", lw=1.5); ax.text(2.25, 0.51, "a coin", color=ROSE, fontsize=14)
    ax.set_ylim(0.4, 0.9); ax.set_ylabel("validation AUC")
    ax.set_title("Most of 0.80 is knowing the month")
    save(fig, "C2_W05_D03_case2_within_month_STUDENT.png")

    everyone = int((yva == 0).sum()) * CALL_RS
    fig, ax = plt.subplots(figsize=(11, 3.8))
    labels = ["the leak promised", "the honest model delivers", "calling everyone"]
    vals = [leaked["bill"] / 1e5, honest["bill"] / 1e5, everyone / 1e5]
    ax.barh(labels, vals, color=[ROSE, GREEN, GREY])
    for i, x in enumerate(vals):
        ax.text(x + 0.04, i, f"Rs {x:.2f} lakh", va="center", fontsize=16)
    ax.invert_yaxis(); ax.set_xlim(0, 3.8)
    ax.set_title("Call bill on 8,238 validation calls (Rs 40 a call, Rs 1,200 a missed buyer)")
    save(fig, "C2_W05_D03_case2_bill_STUDENT.png")

    trio = ["emp.var.rate", "euribor3m", "nr.employed"]
    corr = train[trio].corr()
    fig, ax = plt.subplots(figsize=(6.4, 5.2))
    ax.imshow(corr.values, cmap="Purples", vmin=0, vmax=1)
    ax.set_xticks(range(3)); ax.set_xticklabels(trio, rotation=15)
    ax.set_yticks(range(3)); ax.set_yticklabels(trio)
    for i in range(3):
        for j in range(3):
            ax.text(j, i, f"{corr.values[i, j]:.2f}", ha="center", va="center", fontsize=18,
                    color="white" if corr.values[i, j] > 0.6 else INK)
    ax.set_title("Three desks, one signal"); ax.spines[:].set_visible(False)
    save(fig, "C2_W05_D03_case3_corr_STUDENT.png")

    Z = pd.DataFrame(StandardScaler().fit_transform(train[trio]), columns=trio, index=train.index)

    def coef(cols):
        return LogisticRegression(C=1e6, max_iter=5000).fit(Z[cols], ytr).coef_[0][cols.index("euribor3m")]
    names = hmodel.named_steps["prep"].get_feature_names_out()
    full = dict(zip(names, hmodel.named_steps["model"].coef_[0]))
    steps = ["alone", "with\nnr.employed", "with both\npartners", "honest model\n(20 columns)"]
    vals = [coef(["euribor3m"]), coef(["euribor3m", "nr.employed"]), coef(trio), full["num__euribor3m"]]
    fig, ax = plt.subplots(figsize=(11, 4.6))
    ax.bar(steps, vals, color=[ROSE if x < 0 else GREEN for x in vals])
    ax.axhline(0, color=INK, lw=1.5)
    for i, x in enumerate(vals):
        ax.text(i, x + (0.06 if x >= 0 else -0.16), f"{x:+.2f}", ha="center", fontsize=17)
    ax.set_ylim(-1.15, 1.0); ax.set_ylabel("euribor3m coefficient")
    ax.set_title("One column, four neighbourhoods, two signs")
    save(fig, "C2_W05_D03_case3_flip_STUDENT.png")

    perm = permutation_importance(hmodel, val[honest_cols], yva, scoring="roc_auc", n_repeats=5, random_state=42)
    imp = pd.Series(perm.importances_mean, index=honest_cols).sort_values(ascending=False)
    top = imp.head(8)[::-1]
    fig, ax = plt.subplots(figsize=(11, 5))
    ax.barh(top.index, top.values, color=[VIOLET if c in ECONOMY else GREY for c in top.index])
    for i, x in enumerate(top.values):
        ax.text(x + 0.004, i, f"{x:.3f}", va="center", fontsize=14)
    ax.set_xlim(0, 0.42); ax.set_xlabel("fall in validation AUC when shuffled")
    ax.set_title("Permutation importance, honest model (economy in violet)")
    save(fig, "C2_W05_D03_case3_permutation_STUDENT.png")

    rng = np.random.default_rng(42)
    base = roc_auc_score(yva, hmodel.predict_proba(val[honest_cols])[:, 1])
    falls = []
    for _ in range(5):
        s = val[honest_cols].copy()
        s[ECONOMY] = s[ECONOMY].values[rng.permutation(len(s))]
        falls.append(base - roc_auc_score(yva, hmodel.predict_proba(s)[:, 1]))
    fig, ax = plt.subplots(figsize=(11, 4.2))
    labels = ["the model's whole lift\nabove a coin", "emp.var.rate\nshuffled alone", "all five economy\ncolumns together"]
    vals = [base - 0.5, imp["emp.var.rate"], float(np.mean(falls))]
    ax.bar(labels, vals, color=[GREEN, ROSE, VIOLET])
    for i, x in enumerate(vals):
        ax.text(i, x + 0.008, f"{x:.2f}", ha="center", fontsize=17)
    ax.set_ylim(0, 0.42); ax.set_ylabel("AUC")
    ax.set_title("One twin shuffled costs more than the model ever earned")
    save(fig, "C2_W05_D03_case3_group_STUDENT.png")
    print(f"honest {honest['auc']:.4f} leaked {leaked['auc']:.4f} calendar {calendar['auc']:.4f} within {within:.3f}")


if __name__ == "__main__":
    week_timeline("tuesday")
    week_timeline("wednesday")
    concept_figures()
    case_figures()
