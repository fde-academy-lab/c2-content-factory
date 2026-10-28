"""Draw every chart the W05 D4 deck shows, from the same code the notebooks run.

Usage, from the repository root:
    python3 content/W05/D4/4_trainer_only/C2_W05_D04_make_figures_INTERNAL.py

It downloads UCI Bank Marketing once into ~/.cache/c2_datasets (never into the repository), rebuilds
the week's split and Wednesday's honest feature set, and writes the PNGs into
1_in_class_training_content/slides/img/. The invented teaching tables are typed here exactly as the
concept notebooks type them. Runs in about two minutes.
"""
import io
import pathlib
import urllib.request
import warnings
import zipfile

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import Lasso, LogisticRegression, Ridge
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import (KFold, StratifiedKFold, cross_val_score, learning_curve,
                                     train_test_split)
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import OneHotEncoder, PolynomialFeatures, StandardScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree

warnings.filterwarnings("ignore")
OUT = pathlib.Path(__file__).resolve().parent.parent / "1_in_class_training_content" / "slides" / "img"
OUT.mkdir(parents=True, exist_ok=True)
INK, VIOLET, ROSE, GREEN, MUTED, TINT = "#1A0F5C", "#5B3FD6", "#D63A6A", "#1F8A5B", "#6B6690", "#EEEAFB"
plt.rcParams.update({"figure.dpi": 150, "axes.spines.top": False, "axes.spines.right": False,
                     "font.size": 13, "axes.titlesize": 14, "axes.titleweight": "bold",
                     "axes.labelsize": 13, "legend.fontsize": 12, "xtick.labelsize": 12,
                     "ytick.labelsize": 12})


def save(fig, name):
    fig.tight_layout()
    fig.savefig(OUT / name, facecolor="white")
    plt.close(fig)
    print("wrote", name)


# ------------------------------------------------------------------ the week's pipeline
CACHE = pathlib.Path.home() / ".cache" / "c2_datasets"
CACHE.mkdir(parents=True, exist_ok=True)


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
HONEST = PROFILE + HISTORY + ECONOMY + ["never_contacted", "days_since_contact"]

bank = load_bank()
bank["never_contacted"] = (bank["pdays"] == 999).astype(int)
bank["days_since_contact"] = np.where(bank["pdays"] == 999, 0, bank["pdays"])
yall = (bank["y"] == "yes").astype(int)
rest, test_idx = train_test_split(bank.index, test_size=0.20, stratify=yall, random_state=42)
tr_idx, va_idx = train_test_split(rest, test_size=0.25, stratify=yall.loc[rest], random_state=42)
train, val = bank.loc[tr_idx], bank.loc[va_idx]
X_train, X_val = train[HONEST], val[HONEST]
y_train, y_val = yall.loc[tr_idx], yall.loc[va_idx]
NUM = [c for c in HONEST if pd.api.types.is_numeric_dtype(bank[c])]
CAT = [c for c in HONEST if c not in NUM]
BASE_ERR = y_val.mean()


def prep(scale=True):
    return ColumnTransformer([("num", StandardScaler() if scale else "passthrough", NUM),
                              ("cat", OneHotEncoder(handle_unknown="ignore"), CAT)])


def tree(**kw):
    return Pipeline([("prep", prep(False)), ("model", DecisionTreeClassifier(random_state=42, **kw))])


def logit(C=0.1):
    return Pipeline([("prep", prep()), ("model", LogisticRegression(C=C, max_iter=3000))])


folds = StratifiedKFold(5, shuffle=True, random_state=42)

# ------------------------------------------------------------------ the week's timeline, Thursday
fig, axes = plt.subplots(1, 2, figsize=(12, 4.2), gridspec_kw={"width_ratios": [1.5, 1]})
ax = axes[0]
ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 4.6)
ax.annotate("", xy=(9.8, 1.35), xytext=(0.2, 1.35), arrowprops=dict(arrowstyle="->", lw=2.2, color=INK))
ax.add_patch(plt.Rectangle((0.3, 1.55), 4.6, 0.9, color=TINT))
ax.text(2.6, 2.0, "past rows: train and validate", ha="center", va="center", fontsize=12.5, color=INK)
ax.plot([5.1, 5.1], [1.2, 2.8], color=INK, lw=2)
ax.text(5.1, 3.0, "prediction\nmoment", ha="center", fontsize=12.5, color=INK, fontweight="bold")
ax.add_patch(plt.Rectangle((5.3, 1.55), 3.2, 0.9, color="#FCEBF0"))
ax.text(6.9, 2.0, "outcome window", ha="center", va="center", fontsize=12.5, color=INK)
ax.text(6.9, 0.85, "duration lives here (Wed)", ha="center", fontsize=12, color=ROSE)
ax.text(2.6, 0.85, "Mon: split, baseline 88.7%", ha="center", fontsize=12, color=MUTED)
ax.text(2.6, 0.35, "Tue: threshold, the four boxes", ha="center", fontsize=12, color=MUTED)
ax.text(5.1, 4.1, "Thu: how much of the past to trust", ha="center", fontsize=13, color=VIOLET,
        fontweight="bold")
ax.text(9.2, 2.35, "Fri:\nlater\nmonths", ha="center", fontsize=11.5, color=MUTED)
depth_x = [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 15, 20, 25, 30, 37]
err = []
for d in depth_x[:-1] + [None]:
    m = tree(max_depth=d).fit(X_train, y_train)
    err.append((1 - accuracy_score(y_train, m.predict(X_train)), 1 - accuracy_score(y_val, m.predict(X_val))))
err = np.array(err)
ax = axes[1]
ax.plot(depth_x, err[:, 1] * 100, "o-", color=ROSE, label="validation")
ax.plot(depth_x, err[:, 0] * 100, "o-", color=VIOLET, label="training")
ax.axhline(BASE_ERR * 100, color=MUTED, ls="--", label="call nobody")
ax.set_xlabel("tree depth"); ax.set_ylabel("% customers wrong"); ax.set_title("Thursday adds the U")
ax.legend(frameon=False, fontsize=11)
save(fig, "fig_timeline_thursday.png")

# ------------------------------------------------------------------ concept 1
students = pd.DataFrame({"student": ["Asha\nmemorises", "Bilal\nlearns the method", "Chitra\nskims"],
                         "past": [100, 84, 58], "exam": [61, 81, 56]})
fig, ax = plt.subplots(figsize=(9, 4.2))
x = np.arange(3)
b1 = ax.bar(x - 0.2, students["past"], 0.4, color=VIOLET, label="past papers")
b2 = ax.bar(x + 0.2, students["exam"], 0.4, color=ROSE, label="new exam")
for bars in (b1, b2):
    for b in bars:
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 1.5, f"{b.get_height():.0f}",
                ha="center", fontweight="bold")
ax.set_xticks(x); ax.set_xticklabels(students["student"]); ax.set_ylim(0, 115)
ax.set_ylabel("score (invented)"); ax.legend(frameon=False, ncol=2, loc="upper right")
save(fig, "fig_students.png")

old = pd.DataFrame({"age": [24, 29, 33, 38, 42, 46, 51, 55, 60, 64],
                    "nudges": [1, 4, 2, 5, 1, 6, 3, 2, 5, 1],
                    "bought": [0, 1, 0, 1, 1, 0, 1, 0, 1, 0]})
mem = DecisionTreeClassifier(random_state=0).fit(old[["age", "nudges"]], old["bought"])
stump = DecisionTreeClassifier(max_depth=1, random_state=0).fit(old[["age", "nudges"]], old["bought"])
fig, axes = plt.subplots(1, 2, figsize=(13, 5), gridspec_kw={"width_ratios": [1.6, 1]})
plot_tree(mem, feature_names=["age", "nudges opened"], class_names=["no", "buys"], filled=True,
          impurity=False, fontsize=11, ax=axes[0])
axes[0].set_title("No limit: practice 10 of 10, new customers 3 of 4")
plot_tree(stump, feature_names=["age", "nudges opened"], class_names=["no", "buys"], filled=True,
          impurity=False, fontsize=12, ax=axes[1])
axes[1].set_title("One question: practice 8 of 10, new 4 of 4")
save(fig, "fig_tiny_tree.png")

papers = [1, 2, 3, 4, 5]
curves = {"Asha: variance": ([100] * 5, [48, 53, 56, 59, 61]),
          "Chitra: bias": ([60, 59, 58, 58, 58], [52, 54, 55, 56, 56]),
          "Bilal: about right": ([95, 90, 87, 85, 84], [62, 71, 76, 79, 81])}
fig, axes = plt.subplots(1, 3, figsize=(13, 4.2), sharey=True)
for ax, (name, (p, e)) in zip(axes, curves.items()):
    ax.plot(papers, p, "o-", color=VIOLET, lw=2.4, label="practice")
    ax.plot(papers, e, "o-", color=ROSE, lw=2.4, label="new exam")
    ax.set_title(name); ax.set_xlabel("past papers studied"); ax.set_xticks(papers)
axes[0].set_ylabel("score (invented)"); axes[0].legend(frameon=False)
save(fig, "fig_student_curves.png")

# ------------------------------------------------------------------ concept 2
week = np.arange(1, 13)
foot = np.array([42, 47, 55, 52, 60, 66, 63, 70, 74, 71, 78, 80])
ho = np.isin(week, [4, 7, 10])


def brake(alpha, kind=Ridge):
    est = kind(alpha=alpha, max_iter=100000) if kind is Lasso else kind(alpha=alpha)
    return make_pipeline(PolynomialFeatures(7, include_bias=False), StandardScaler(), est).fit(
        week[~ho, None], foot[~ho])


def rmse(m, mask):
    return float(np.sqrt(np.mean((m.predict(week[mask, None]) - foot[mask]) ** 2)))


grid = np.linspace(1, 12, 200)[:, None]
fig, ax = plt.subplots(figsize=(10, 4.4))
ax.scatter(week[~ho], foot[~ho], color=INK, s=60, zorder=3, label="teaching weeks")
ax.scatter(week[ho], foot[ho], facecolors="white", edgecolors=ROSE, s=110, lw=2.4, zorder=3,
           label="held-out weeks")
ax.plot(grid, brake(1e-6).predict(grid), color=ROSE, lw=2, label="no brake")
ax.plot(grid, brake(10).predict(grid), color=GREEN, lw=3, label="brake on")
ax.set_ylim(30, 95); ax.set_xlabel("week"); ax.set_ylabel("footfall, hundreds (invented)")
ax.legend(frameon=False, ncol=2)
save(fig, "fig_brake_curve.png")

alphas = [1e-6, 1e-3, 1e-2, 0.1, 1, 10, 100]
sw = np.array([(rmse(brake(a), ~ho), rmse(brake(a), ho)) for a in alphas])
fig, ax = plt.subplots(figsize=(9, 4.2))
ax.plot(alphas, sw[:, 0], "o-", color=VIOLET, lw=2.4, label="teaching weeks")
ax.plot(alphas, sw[:, 1], "o-", color=ROSE, lw=2.4, label="held-out weeks")
ax.set_xscale("log"); ax.set_xlabel("brake strength (alpha)"); ax.set_ylabel("error, hundreds")
ax.annotate("variance", (1e-6, sw[0, 1]), xytext=(2e-6, 7.2), color=ROSE, fontweight="bold")
ax.annotate("bias", (100, sw[-1, 1]), xytext=(20, 8.6), color=VIOLET, fontweight="bold")
ax.legend(frameon=False, loc="upper center")
save(fig, "fig_brake_sweep.png")

# ------------------------------------------------------------------ concept 3
crowd = pd.DataFrame({"visits": [0, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 8, 9],
                      "bought": [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1]})
kf = KFold(n_splits=5, shuffle=True, random_state=0)
g = np.zeros((5, 20)); fs = []
for i, (t, e) in enumerate(kf.split(crowd)):
    g[i, e] = 1
    m = LogisticRegression().fit(crowd.iloc[t][["visits"]], crowd.iloc[t]["bought"])
    fs.append(m.score(crowd.iloc[e][["visits"]], crowd.iloc[e]["bought"]))
fig, ax = plt.subplots(figsize=(12, 3.6))
ax.imshow(g, cmap=matplotlib.colors.ListedColormap([TINT, ROSE]), aspect="auto")
for i, s in enumerate(fs):
    ax.text(20.2, i, f"exam {s:.0%}", va="center", fontsize=13)
ax.set_yticks(range(5)); ax.set_yticklabels([f"turn {i + 1}" for i in range(5)])
ax.set_xticks(range(20)); ax.set_xticklabels([chr(65 + i) for i in range(20)], fontsize=11)
ax.set_xlim(-0.5, 23); ax.set_xlabel("20 invented customers; pink = sitting the exam this turn")
save(fig, "fig_folds_grid.png")

# ------------------------------------------------------------------ concept 4
shop = pd.DataFrame({"visits": [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9],
                     "basket_rs": [300, 900, 450, 1200, 350, 800, 1500, 400, 1100, 950, 600, 1300]})
groups = KMeans(n_clusters=3, n_init=10, random_state=0).fit_predict(StandardScaler().fit_transform(shop))
fig, ax = plt.subplots(figsize=(8, 4.2))
for k, c in zip(range(3), [VIOLET, ROSE, GREEN]):
    p = shop[groups == k]
    ax.scatter(p["visits"], p["basket_rs"], s=120, color=c, label=f"group {k + 1}")
ax.set_xlabel("visits a month"); ax.set_ylabel("average basket, Rs (invented)")
ax.legend(frameon=False)
save(fig, "fig_kmeans.png")

# ------------------------------------------------------------------ concept 5
paper = pd.Series({"logistic regression": 0.8432, "random forests": 0.8460, "LogitBoost": 0.8493,
                   "GAM": 0.8542, "GA2M (readable)": 0.8576})
fig, ax = plt.subplots(figsize=(9, 4))
ax.barh(paper.index, paper.values, color=[GREEN, VIOLET, VIOLET, GREEN, GREEN])
for i, v in enumerate(paper.values):
    ax.text(v + 0.0005, i, f"{v:.3f}", va="center", fontsize=13)
ax.set_xlim(0.83, 0.866); ax.set_xlabel("AUC, pneumonia data, Caruana and others (KDD 2015)")
save(fig, "fig_caruana.png")

simple = np.array([0.78, 0.80, 0.79, 0.81, 0.79]); cplx = np.array([0.79, 0.80, 0.80, 0.82, 0.80])
fig, ax = plt.subplots(figsize=(6.5, 4.2))
for i in range(5):
    ax.plot([0, 1], [simple[i], cplx[i]], "o-", color=VIOLET, lw=2, alpha=0.8)
ax.set_xticks([0, 1]); ax.set_xticklabels(["simple", "complex"]); ax.set_xlim(-0.3, 1.3)
ax.set_ylabel("AUC on the same fold (invented)")
save(fig, "fig_paired_invented.png")

# ------------------------------------------------------------------ case 1
free = tree().fit(X_train, y_train)
tr_acc = accuracy_score(y_train, free.predict(X_train)); va_acc = accuracy_score(y_val, free.predict(X_val))
fig, ax = plt.subplots(figsize=(9, 4.2))
vals = [tr_acc * 100, va_acc * 100, (1 - BASE_ERR) * 100]
bars = ax.bar(["training\n(seen)", "validation\n(unseen)", "call nobody\n(baseline)"], vals,
              color=[VIOLET, ROSE, MUTED], width=0.55)
for b, v in zip(bars, vals):
    ax.text(b.get_x() + b.get_width() / 2, v + 0.4, f"{v:.1f}%", ha="center", fontweight="bold", fontsize=15)
ax.set_ylim(75, 103); ax.set_ylabel("accuracy, %")
save(fig, "fig_unlimited_scores.png")

fig, ax = plt.subplots(figsize=(11, 4.6))
ax.plot(depth_x, err[:, 0] * 100, "o-", color=VIOLET, lw=2.4, label="training error")
ax.plot(depth_x, err[:, 1] * 100, "o-", color=ROSE, lw=2.4, label="validation error")
ax.axhline(BASE_ERR * 100, color=MUTED, ls="--", lw=2, label="call nobody, 11.3%")
best = int(np.argmin(err[:, 1]))
ax.annotate(f"lowest: {err[best, 1] * 100:.1f}% at depth {depth_x[best]}", (depth_x[best], err[best, 1] * 100),
            xytext=(8, 4), arrowprops=dict(arrowstyle="->", color=INK), fontweight="bold")
ax.annotate(f"no limit: {err[-1, 1] * 100:.1f}%", (37, err[-1, 1] * 100), xytext=(26, 13.2),
            arrowprops=dict(arrowstyle="->", color=ROSE), color=ROSE, fontweight="bold")
ax.set_xlabel("max_depth (37 = no limit)"); ax.set_ylabel("% of customers wrong")
ax.legend(frameon=False, loc="lower left")
save(fig, "fig_depth_u.png")

lc = {}
for name, kw in [("Stump (depth 1)", {"max_depth": 1}), ("No limit", {}),
                 ("Depth 6, leaf 50", {"max_depth": 6, "min_samples_leaf": 50})]:
    s, trs, vas = learning_curve(tree(**kw), X_train, y_train, cv=folds, scoring="accuracy",
                                 train_sizes=[0.05, 0.1, 0.25, 0.5, 0.75, 1.0], n_jobs=-1)
    lc[name] = (s, (1 - trs.mean(1)) * 100, (1 - vas.mean(1)) * 100)


def three_panels(labels, fname, titles):
    fig, axes = plt.subplots(1, 3, figsize=(13, 4.3), sharey=True)
    for ax, key, title in zip(axes, labels, titles):
        s, trs, vas = lc[key]
        ax.plot(s / 1000, trs, "o-", color=VIOLET, lw=2.4, label="training")
        ax.plot(s / 1000, vas, "o-", color=ROSE, lw=2.4, label="held out")
        ax.axhline(BASE_ERR * 100, color=MUTED, ls="--", lw=1.5)
        ax.set_title(title); ax.set_xlabel("training customers, thousands")
    axes[0].set_ylabel("% wrong"); axes[0].legend(frameon=False)
    save(fig, fname)


three_panels(list(lc), "fig_learning_curves_bank.png",
             ["Stump: bias", "No limit: variance", "Depth 6, leaf 50: about right"])
three_panels(["No limit", "Stump (depth 1)", "Depth 6, leaf 50"], "fig_mystery_curves.png",
             ["Model A", "Model B", "Model C"])

# ------------------------------------------------------------------ case 2
outside = pd.concat([train, val]); y_out = yall.loc[outside.index]
seed_auc = []
for seed in [1, 2, 3, 4, 5]:
    a, b = train_test_split(outside.index, test_size=0.25, stratify=y_out, random_state=seed)
    m = Pipeline([("prep", prep()), ("model", LogisticRegression(max_iter=3000))]).fit(outside.loc[a, HONEST], y_out.loc[a])
    seed_auc.append(roc_auc_score(y_out.loc[b], m.predict_proba(outside.loc[b, HONEST])[:, 1]))
cv5 = cross_val_score(Pipeline([("prep", prep()), ("model", LogisticRegression(max_iter=3000))]),
                      X_train, y_train, cv=folds, scoring="roc_auc")
fig, ax = plt.subplots(figsize=(11, 3.6))
ax.scatter(seed_auc, [1] * 5, s=130, color=VIOLET, zorder=3, label="five deals of 8,238 customers")
ax.scatter(cv5, [0] * 5, s=130, color=ROSE, zorder=3, label="five folds of about 4,942")
ax.set_yticks([0, 1]); ax.set_yticklabels(["folds", "deals"]); ax.set_ylim(-0.6, 1.6)
ax.set_xlabel("AUC, the same logistic model")
ax.legend(frameon=False, loc="upper left", ncol=2)
save(fig, "fig_seed_swing.png")

Cs = [0.0001, 0.001, 0.01, 0.1, 1, 10, 100]
rows = []
for C in Cs:
    cv = cross_val_score(logit(C), X_train, y_train, cv=folds, scoring="roc_auc")
    fit = logit(C).fit(X_train, y_train)
    rows.append((roc_auc_score(y_train, fit.predict_proba(X_train)[:, 1]), cv.mean(), cv.std()))
rows = np.array(rows)
fig, ax = plt.subplots(figsize=(10, 4.3))
ax.plot(Cs, rows[:, 0], "o-", color=VIOLET, lw=2.4, label="training AUC")
ax.plot(Cs, rows[:, 1], "o-", color=ROSE, lw=2.4, label="cross-validated AUC")
ax.fill_between(Cs, rows[:, 1] - rows[:, 2], rows[:, 1] + rows[:, 2], color=ROSE, alpha=0.12)
ax.set_xscale("log"); ax.set_xlabel("C   (left: strong brake, right: brake off)"); ax.set_ylabel("AUC")
ax.legend(frameon=False, loc="lower right")
save(fig, "fig_c_sweep.png")

l1 = []
for C in [0.001, 0.003, 0.01, 0.03, 0.1, 1]:
    m = Pipeline([("prep", prep()), ("model", LogisticRegression(C=C, l1_ratio=1, solver="liblinear"))]).fit(X_train, y_train)
    l1.append((C, int((abs(m.named_steps["model"].coef_.ravel()) > 1e-8).sum()),
               roc_auc_score(y_val, m.predict_proba(X_val)[:, 1])))
fig, ax = plt.subplots(figsize=(10, 4.3))
ax.bar(range(len(l1)), [r[1] for r in l1], color=VIOLET)
for i, (C, kept, auc) in enumerate(l1):
    ax.text(i, kept + 1.2, f"{kept} cols\nAUC {auc:.3f}", ha="center", fontsize=12)
ax.set_xticks(range(len(l1))); ax.set_xticklabels([f"C={r[0]}" for r in l1])
ax.set_ylim(0, 62); ax.set_ylabel("columns kept, of 63")
save(fig, "fig_l1_columns.png")

# ------------------------------------------------------------------ case 3
models = {"Logistic, braked": logit(0.1),
          "Tree, depth 6, leaf 50": tree(max_depth=6, min_samples_leaf=50),
          "Random forest": Pipeline([("prep", prep(False)), ("model", RandomForestClassifier(
              n_estimators=300, min_samples_leaf=20, n_jobs=-1, random_state=42))]),
          "Gradient boosting": Pipeline([("prep", prep(False)),
                                         ("model", HistGradientBoostingClassifier(random_state=42))])}
cvs, scores = {}, {}
for name, m in models.items():
    cvs[name] = cross_val_score(m, X_train, y_train, cv=folds, scoring="roc_auc", n_jobs=-1)
    scores[name] = m.fit(X_train, y_train).predict_proba(X_val)[:, 1]
fig, ax = plt.subplots(figsize=(11, 4.4))
for i, (name, cv) in enumerate(cvs.items()):
    ax.scatter(cv, [i] * 5, color=VIOLET, alpha=0.55, s=70)
    ax.scatter([cv.mean()], [i], color=INK, marker="|", s=900, lw=3)
    ax.text(cv.mean(), i + 0.3, f"{cv.mean():.3f}", ha="center", fontweight="bold")
ax.set_yticks(range(4)); ax.set_yticklabels(list(cvs)); ax.set_ylim(-0.5, 3.7)
ax.set_xlabel("AUC on each of five folds (dots) and the mean (bar)")
save(fig, "fig_race_folds.png")

lgf, gbf = cvs["Logistic, braked"], cvs["Gradient boosting"]
fig, ax = plt.subplots(figsize=(7, 4.4))
for i in range(5):
    ax.plot([0, 1], [lgf[i], gbf[i]], "o-", color=VIOLET, lw=2.2)
    ax.text(1.05, gbf[i], f"+{gbf[i] - lgf[i]:.3f}", va="center", fontsize=12)
ax.set_xticks([0, 1]); ax.set_xticklabels(["logistic", "boosting"]); ax.set_xlim(-0.3, 1.45)
ax.set_ylabel("AUC on the same fold")
save(fig, "fig_paired_gap.png")

y = y_val.values; thr = 40 / 1240
bill = {}
for name, p in scores.items():
    act = p >= thr
    bill[name] = int((act & (y == 0)).sum()) * 40 + int((~act & (y == 1)).sum()) * 1200
bill["Nudge everyone"] = int((y == 0).sum()) * 40
fig, ax = plt.subplots(figsize=(10, 4.2))
names = list(bill); v = [bill[n] / 1e5 for n in names]
ax.barh(names, v, color=[VIOLET] * 4 + [MUTED])
for i, val_ in enumerate(v):
    ax.text(val_ + 0.04, i, f"Rs {val_:.2f} lakh", va="center", fontsize=13)
ax.set_xlim(0, max(v) * 1.3); ax.invert_yaxis()
ax.set_xlabel("error bill at threshold 0.032 on 8,238 customers, Rs lakh")
save(fig, "fig_bills.png")

gaps = []
for a, b in folds.split(X_train, y_train):
    yb = y_train.iloc[b].values; kk = round(len(b) * 5000 / 41188); found = []
    for m in (models["Logistic, braked"], models["Gradient boosting"]):
        m.fit(X_train.iloc[a], y_train.iloc[a])
        found.append(yb[np.argsort(-m.predict_proba(X_train.iloc[b])[:, 1])[:kk]].sum() * 5000 / kk)
    gaps.append(found[1] - found[0])
gaps = np.array(gaps); low = (gaps.mean() - gaps.std()) * 1200
fig, ax = plt.subplots(figsize=(11, 3.8))
ax.scatter(gaps * 1.2, [0] * 5, s=140, color=VIOLET, zorder=3, label="each fold's extra margin")
ax.axvline(75, color=ROSE, ls="--", lw=2.4, label="extra cost, invented: Rs 75k")
ax.axvline(low / 1000, color=INK, lw=3, label=f"low end: Rs {low / 1000:.0f}k")
ax.set_yticks([]); ax.set_xlabel("boosting's extra margin per 5,000-nudge campaign, Rs thousand")
ax.legend(frameon=False, loc="upper left", fontsize=12)
ax.set_xlim(-10, 200)
save(fig, "fig_budget_gap.png")

print("bills", bill)
print("fold gaps", gaps, "low end", round(low))
print("seed auc", np.round(seed_auc, 3), "cv5", np.round(cv5, 3))
