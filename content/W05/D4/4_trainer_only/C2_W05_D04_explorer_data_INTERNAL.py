"""Export the numbers the Week 5 Thursday explorer draws, from the same code the notebooks run.

Usage:
    python3 content/W05/D4/4_trainer_only/C2_W05_D04_explorer_data_INTERNAL.py

Writes C2_W05_D04_explorer_data_INTERNAL.json beside this file. scripts/build_companion.py then
inlines it into 1_in_class_training_content/demos/C2_W05_D04_depth_and_brake_explorer_STUDENT.html.
The bank's file is cached in ~/.cache/c2_datasets exactly as the notebooks cache it, so nothing else
is written to the repository.

Two kinds of number leave this script. The "bank" block is real: it reruns case01, case02 and
case03 on UCI Bank Marketing and stops with an error unless every number the page quotes equals
what those notebooks print. The "invented" block reruns the small invented tables of notebooks
ch03 and ch04 through the same scikit-learn calls, so the page's folds, forest votes, boosting
rounds and k-means steps are the notebook's own and need no copying by hand.
"""
import io
import json
import pathlib
import urllib.request
import zipfile

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingClassifier, HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import KFold, StratifiedKFold, cross_val_score, learning_curve, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "C2_W05_D04_explorer_data_INTERNAL.json"
CACHE = pathlib.Path.home() / ".cache" / "c2_datasets"
CACHE.mkdir(parents=True, exist_ok=True)


def fetch(url, name):
    path = CACHE / name
    if not path.exists():
        path.write_bytes(urllib.request.urlopen(url, timeout=60).read())
    return path


def load_bank():
    """UCI Bank Marketing, bank-additional-full.csv (CC BY 4.0). The zip holds a second zip."""
    f = CACHE / "bank-additional-full.csv"
    if not f.exists():
        outer = zipfile.ZipFile(fetch("https://archive.ics.uci.edu/static/public/222/bank+marketing.zip",  # verified 28 October 2026
                                      "bank+marketing.zip"))
        inner = zipfile.ZipFile(io.BytesIO(outer.read("bank-additional.zip")))
        f.write_bytes(inner.read("bank-additional/bank-additional-full.csv"))
    return pd.read_csv(f, sep=";")


# The week's pipeline, exactly as case01 to case03 write it.
PROFILE = ["age", "job", "marital", "education", "default", "housing", "loan"]
HISTORY = ["contact", "month", "day_of_week", "campaign", "previous", "poutcome"]
ECONOMY = ["emp.var.rate", "cons.price.idx", "cons.conf.idx", "euribor3m", "nr.employed"]
HONEST = PROFILE + HISTORY + ECONOMY + ["never_contacted", "days_since_contact"]


def engineer(df):
    """Wednesday's fix for pdays: 999 means never contacted, so it becomes a flag plus the real days."""
    df = df.copy()
    df["never_contacted"] = (df["pdays"] == 999).astype(int)
    df["days_since_contact"] = np.where(df["pdays"] == 999, 0, df["pdays"])
    return df


def week_split(df, seed=42):
    """Test is sealed first (20 percent, the envelope); the rest splits 75/25 into train and validation."""
    y = (df["y"] == "yes").astype(int)
    rest, test = train_test_split(df.index, test_size=0.20, stratify=y, random_state=seed)
    train, val = train_test_split(rest, test_size=0.25, stratify=y.loc[rest], random_state=seed)
    return df.loc[train], df.loc[val], df.loc[test]


def r(x, d=4):
    return round(float(x), d)


def bits(values):
    return "".join("1" if v else "0" for v in values)


FAILS = []


def expect(label, got, want, tol=0.0):
    """Stop the export unless the number equals what the notebook prints."""
    ok = abs(got - want) <= tol if isinstance(want, (int, float)) else got == want
    print(("PASS  " if ok else "FAIL  ") + f"{label}: {got} (notebook {want})")
    if not ok:
        FAILS.append(label)


def bank_numbers():
    bank = engineer(load_bank())
    train, val, test = week_split(bank)
    X_train, X_val = train[HONEST], val[HONEST]
    y_train = (train["y"] == "yes").astype(int)
    y_val = (val["y"] == "yes").astype(int)
    NUM = [c for c in HONEST if pd.api.types.is_numeric_dtype(bank[c])]
    CAT = [c for c in HONEST if c not in NUM]

    def prep(scale=True):
        return ColumnTransformer([("num", StandardScaler() if scale else "passthrough", NUM),
                                  ("cat", OneHotEncoder(handle_unknown="ignore"), CAT)])

    out = {"rows": len(bank), "yes": int((bank["y"] == "yes").sum()),
           "split": {"train": len(train), "val": len(val), "test": len(test),
                     "val_yes": int(y_val.sum()), "val_no": int((y_val == 0).sum())}}
    expect("split", (len(train), len(val), len(test)), (24712, 8238, 8238))
    expect("call nobody right", int((y_val == 0).sum()), 7310)

    # ---- case01, step 3 and step 4: the unlimited tree
    tree_free = Pipeline([("prep", prep(scale=False)), ("model", DecisionTreeClassifier(random_state=42))])
    tree_free.fit(X_train, y_train)
    pred_tr, pred_val = tree_free.predict(X_train), tree_free.predict(X_val)
    leaves = int(tree_free.named_steps["model"].get_n_leaves())
    depth = int(tree_free.named_steps["model"].get_depth())
    leaf_id = tree_free.named_steps["model"].apply(tree_free.named_steps["prep"].transform(X_train))
    sizes = pd.Series(leaf_id).value_counts()
    size_counts = sizes.value_counts().sort_index()
    bands = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 10), (11, 50), (51, 100000)]
    band_counts = [int(size_counts[(size_counts.index >= a) & (size_counts.index <= b)].sum()) for a, b in bands]
    train_right = int((pred_tr == y_train.values).sum())
    val_right = int((pred_val == y_val.values).sum())
    expect("unlimited tree training accuracy", round(train_right / len(train), 3), 0.996)
    expect("unlimited tree validation accuracy", round(val_right / len(val), 3), 0.841)
    expect("depth and leaves", (depth, leaves), (37, 3662))
    expect("leaves holding one customer", band_counts[0], 1709)
    expect("leaves holding one or two", band_counts[0] + band_counts[1], 2323)
    # The story draws 8,238 of the 24,712 training customers beside the 8,238 validation customers,
    # so the two piles are the same size; the third is a seeded draw, said so on the page.
    pick = np.sort(np.random.default_rng(5).choice(len(train), size=len(val), replace=False))
    out["tree"] = {"train_right": train_right, "val_right": val_right, "depth": depth, "leaves": leaves,
                   "per_leaf": r(len(train) / leaves, 1),
                   "bands": ["1", "2", "3", "4", "5", "6 to 10", "11 to 50", "over 50"], "band_counts": band_counts,
                   "story": {"train_ok": bits(pred_tr[pick] == y_train.values[pick]),
                             "val_ok": bits(pred_val == y_val.values), "val_y": bits(y_val.values == 1),
                             "sample_wrong": int((pred_tr[pick] != y_train.values[pick]).sum())}}

    # ---- case01, step 5: the depth curve
    depths = [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 15, 20, 25, 30, None]
    rows = []
    for d in depths:
        m = Pipeline([("prep", prep(scale=False)),
                      ("model", DecisionTreeClassifier(max_depth=d, random_state=42))]).fit(X_train, y_train)
        rows.append([d or 0, 1 - accuracy_score(y_train, m.predict(X_train)), 1 - accuracy_score(y_val, m.predict(X_val)),
                     roc_auc_score(y_val, m.predict_proba(X_val)[:, 1])])
    out["depth"] = {"depth": [x[0] for x in rows], "train_err": [r(x[1]) for x in rows],
                    "val_err": [r(x[2]) for x in rows], "val_auc": [r(x[3]) for x in rows]}
    expect("depth 3 validation error", r(rows[2][2]), 0.1005)
    expect("no limit validation error", r(rows[-1][2]), 0.1594)
    expect("depth 7 validation AUC", r(rows[6][3]), 0.7812)

    # ---- case01, step 6: learning curves of three trees
    folds = StratifiedKFold(5, shuffle=True, random_state=42)
    trees = {"stump": DecisionTreeClassifier(max_depth=1, random_state=42),
             "free": DecisionTreeClassifier(random_state=42),
             "braked": DecisionTreeClassifier(max_depth=6, min_samples_leaf=50, random_state=42)}
    lc = {}
    for name, model in trees.items():
        s, tr, va = learning_curve(Pipeline([("prep", prep(scale=False)), ("model", model)]), X_train, y_train,
                                   cv=folds, scoring="accuracy", train_sizes=[0.05, 0.1, 0.25, 0.5, 0.75, 1.0])
        lc[name] = {"train_err": [r(1 - v) for v in tr.mean(axis=1)], "held_err": [r(1 - v) for v in va.mean(axis=1)]}
        lc["sizes"] = [int(v) for v in s]
    out["learning"] = lc
    expect("learning curve sizes", lc["sizes"][0], 988)
    expect("unlimited tree at 19,769 rows", (round(lc["free"]["train_err"][-1], 3), round(lc["free"]["held_err"][-1], 3)), (0.003, 0.165))
    expect("braked tree at 19,769 rows", (round(lc["braked"]["train_err"][-1], 3), round(lc["braked"]["held_err"][-1], 3)), (0.098, 0.101))
    expect("stump at 19,769 rows", (round(lc["stump"]["train_err"][-1], 3), round(lc["stump"]["held_err"][-1], 3)), (0.113, 0.113))

    # ---- case02: five deals, five folds, the scaler, the brake C, L1
    outside = pd.concat([train, val])
    y_out = (outside["y"] == "yes").astype(int)

    def logit(C=1.0):
        return Pipeline([("prep", prep()), ("model", LogisticRegression(C=C, max_iter=3000))])

    seed_auc = []
    for seed in [1, 2, 3, 4, 5]:
        a, b = train_test_split(outside.index, test_size=0.25, stratify=y_out, random_state=seed)
        m = logit().fit(outside.loc[a, HONEST], y_out.loc[a])
        seed_auc.append(roc_auc_score(y_out.loc[b], m.predict_proba(outside.loc[b, HONEST])[:, 1]))
    right_way = cross_val_score(logit(), X_train, y_train, cv=folds, scoring="roc_auc")
    X_leaky = X_train.copy()
    X_leaky[NUM] = StandardScaler().fit_transform(X_leaky[NUM])
    no_scaler = ColumnTransformer([("num", "passthrough", NUM), ("cat", OneHotEncoder(handle_unknown="ignore"), CAT)])
    wrong_way = cross_val_score(Pipeline([("prep", no_scaler), ("model", LogisticRegression(max_iter=3000))]),
                                X_leaky, y_train, cv=folds, scoring="roc_auc")
    sweep = []
    for C_ in [0.0001, 0.001, 0.01, 0.1, 1, 10, 100]:
        cv = cross_val_score(logit(C_), X_train, y_train, cv=folds, scoring="roc_auc")
        fit = logit(C_).fit(X_train, y_train)
        sweep.append([C_, roc_auc_score(y_train, fit.predict_proba(X_train)[:, 1]), cv.mean(), cv.std()])
    l1 = []
    for C_ in [0.001, 0.003, 0.01, 0.03, 0.1, 1]:
        m = Pipeline([("prep", prep()), ("model", LogisticRegression(C=C_, l1_ratio=1, solver="liblinear"))]).fit(X_train, y_train)
        coef = m.named_steps["model"].coef_.ravel()
        l1.append([C_, int((abs(coef) > 1e-8).sum()), int(coef.size), roc_auc_score(y_val, m.predict_proba(X_val)[:, 1])])
    out["cv"] = {"deal_size": len(val), "fold_size": len(X_train) // 5,
                 "deals": [r(v) for v in seed_auc], "folds": [r(v) for v in right_way],
                 "mean": r(right_way.mean()), "spread": r(right_way.std()),
                 "inside": r(right_way.mean(), 5), "before": r(wrong_way.mean(), 5),
                 "sweep": {"C": [x[0] for x in sweep], "train": [r(x[1]) for x in sweep], "cv": [r(x[2]) for x in sweep],
                           "spread": [r(x[3]) for x in sweep]},
                 "l1": {"C": [x[0] for x in l1], "kept": [x[1] for x in l1], "of": l1[0][2], "val_auc": [r(x[3]) for x in l1]}}
    expect("five deals", [round(v, 3) for v in seed_auc], [0.79, 0.79, 0.789, 0.786, 0.788])
    expect("fold AUCs", [round(v, 4) for v in right_way], [0.7709, 0.7687, 0.7975, 0.7969, 0.7983])
    expect("scaler inside and before", (round(right_way.mean(), 5), round(wrong_way.mean(), 5)), (0.78648, 0.78645))
    expect("C sweep at 0.0001", round(sweep[0][2], 4), 0.7616)
    expect("L1 at C = 0.03", (l1[3][1], round(l1[3][3], 4)), (20, 0.794))

    # ---- case03: the race on the same five folds
    grid = []
    for d in [4, 5, 6, 7, 8]:
        for leaf in [1, 50, 200]:
            m = Pipeline([("prep", prep(scale=False)),
                          ("model", DecisionTreeClassifier(max_depth=d, min_samples_leaf=leaf, random_state=42))])
            grid.append((cross_val_score(m, X_train, y_train, cv=folds, scoring="roc_auc").mean(), d, leaf))
    grid.sort(reverse=True)
    best_d, best_leaf = grid[0][1], grid[0][2]
    expect("tuned tree", (best_d, best_leaf, round(grid[0][0], 4)), (6, 50, 0.7821))
    models = {
        "logistic": Pipeline([("prep", prep()), ("model", LogisticRegression(C=0.1, max_iter=3000))]),
        "tree": Pipeline([("prep", prep(scale=False)), ("model",
                          DecisionTreeClassifier(max_depth=best_d, min_samples_leaf=best_leaf, random_state=42))]),
        "forest": Pipeline([("prep", prep(scale=False)), ("model",
                            RandomForestClassifier(n_estimators=300, min_samples_leaf=20, n_jobs=-1, random_state=42))]),
        "boosting": Pipeline([("prep", prep(scale=False)), ("model", HistGradientBoostingClassifier(random_state=42))]),
    }
    race, scores = {}, {}
    for name, m in models.items():
        cv = cross_val_score(m, X_train, y_train, cv=folds, scoring="roc_auc")
        m.fit(X_train, y_train)
        scores[name] = m.predict_proba(X_val)[:, 1]
        race[name] = {"folds": [r(v) for v in cv], "mean": r(cv.mean()), "spread": r(cv.std()),
                      "val_auc": r(roc_auc_score(y_val, scores[name]))}
    expect("race means", [round(race[k]["mean"], 3) for k in models], [0.786, 0.782, 0.791, 0.793])
    paired = np.array(race["boosting"]["folds"]) - np.array(race["logistic"]["folds"])
    printed = np.round(np.array([round(v, 3) for v in race["boosting"]["folds"]]) - np.array([round(v, 3) for v in race["logistic"]["folds"]]), 3)
    expect("boosting minus logistic, fold by fold", list(printed), [0.007, 0.007, 0.003, 0.014, 0.003])
    NUDGE, MARGIN = 40, 1200
    threshold = NUDGE / (NUDGE + MARGIN)
    y = y_val.values
    bills, top = {}, {}
    k = round(len(y) * 5000 / 41188)
    for name, p in scores.items():
        act = p >= threshold
        bills[name] = int((act & (y == 0)).sum()) * NUDGE + int((~act & (y == 1)).sum()) * MARGIN
        top[name] = int(y[np.argsort(-p)[:k]].sum())
    bills["everyone"] = int((y == 0).sum()) * NUDGE
    expect("bills", [bills[n] for n in ["logistic", "tree", "forest", "boosting", "everyone"]],
           [278560, 284200, 284360, 281960, 292400])
    expect("buyers in the top 1,000", [top[n] for n in ["logistic", "tree", "forest", "boosting"]], [465, 469, 476, 472])
    lg, gb = models["logistic"], models["boosting"]
    gaps = []
    for a, b in folds.split(X_train, y_train):
        yb = y_train.iloc[b].values
        kk = round(len(b) * 5000 / 41188)
        found = []
        for m in (lg, gb):
            m.fit(X_train.iloc[a], y_train.iloc[a])
            p = m.predict_proba(X_train.iloc[b])[:, 1]
            found.append(yb[np.argsort(-p)[:kk]].sum() * 5000 / kk)
        gaps.append(found[1] - found[0])
    gaps = np.array(gaps)
    low = gaps.mean() - gaps.std()
    expect("extra buyers per 5,000 nudges", [int(round(v)) for v in gaps], [0, 133, 100, 92, 125])
    expect("low end in rupees", round(low * MARGIN), 50939)
    out["race"] = {"order": list(models), "models": race, "paired": [r(v, 4) for v in paired], "printed": [r(v, 3) for v in printed],
                   "threshold": r(threshold), "bills": bills, "k": k, "top": top, "random_top": r(y.mean() * k, 1),
                   "gaps": [r(v, 2) for v in gaps], "gap_mean": r(gaps.mean(), 2), "gap_spread": r(gaps.std(), 2),
                   "low": r(low, 2), "low_rs": int(round(low * MARGIN)), "margin": MARGIN, "nudge": NUDGE,
                   "extra_cost_invented": 75000}
    return out


def invented_numbers():
    """Notebooks ch03 and ch04 typed these tables; the same calls run here so the page draws them."""
    # ch03: twenty invented shoppers, five random deals, then five folds.
    crowd = pd.DataFrame({"visits": [0, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 8, 9],
                          "bought": [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1]})
    X, y = crowd[["visits"]], crowd["bought"]
    rng = np.random.default_rng(7)
    deals = []
    for _ in range(5):
        exam = rng.choice(20, size=5, replace=False)
        teach = np.setdiff1d(np.arange(20), exam)
        m = LogisticRegression().fit(X.iloc[teach], y.iloc[teach])
        deals.append({"exam": sorted(int(i) for i in exam), "score": r(m.score(X.iloc[exam], y.iloc[exam]), 2)})
    expect("ch03 deals", [d["score"] for d in deals], [0.6, 0.6, 0.8, 0.4, 0.6])
    kf = KFold(n_splits=5, shuffle=True, random_state=0)
    turns = []
    allmu, allsd = float(X["visits"].mean()), float(X["visits"].std(ddof=0))
    for teach, exam in kf.split(X):
        raw = LogisticRegression().fit(X.iloc[teach], y.iloc[teach]).score(X.iloc[exam], y.iloc[exam])
        inside = Pipeline([("scale", StandardScaler()), ("model", LogisticRegression())]).fit(X.iloc[teach], y.iloc[teach])
        mu = float(X.iloc[teach]["visits"].mean())
        z_all = (X - allmu) / allsd
        leak = LogisticRegression().fit(z_all.iloc[teach], y.iloc[teach]).score(z_all.iloc[exam], y.iloc[exam])
        turns.append({"exam": sorted(int(i) for i in exam), "score": r(raw, 2),
                      "inside": r(inside.score(X.iloc[exam], y.iloc[exam]), 2), "leak": r(leak, 2), "mean": r(mu, 2)})
    scores = [t["score"] for t in turns]
    expect("ch03 fold mean and spread", (round(np.mean(scores), 2), round(np.std(scores), 2)), (0.6, 0.41))
    expect("ch03 teaching mean of turn 1", turns[0]["mean"], 3.81, 0.005)
    ch03 = {"visits": crowd["visits"].tolist(), "bought": crowd["bought"].tolist(), "deals": deals, "turns": turns,
            "all_mean": r(allmu, 2)}

    # ch04: twelve invented shoppers; a tree, a forest of five, a booster of four, k-means with k = 3.
    shop = pd.DataFrame({"visits": [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9],
                         "basket_rs": [300, 900, 450, 1200, 350, 800, 1500, 400, 1100, 950, 600, 1300],
                         "joined": [0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1]})
    F = ["visits", "basket_rs"]

    def rules(t, node=0, regress=False):
        """A fitted tree as nested questions; a booster's leaves carry the step it adds to the log-odds."""
        tr = t.tree_
        if tr.children_left[node] == -1:
            leaf = r(tr.value[node][0][0], 3) if regress else int(np.argmax(tr.value[node][0]))
            return {"leaf": leaf, "n": int(tr.n_node_samples[node])}
        return {"f": F[tr.feature[node]], "t": r(tr.threshold[node], 2),
                "lo": rules(t, tr.children_left[node], regress), "hi": rules(t, tr.children_right[node], regress)}

    tree = DecisionTreeClassifier(max_depth=2, random_state=0).fit(shop[F], shop["joined"])
    forest = RandomForestClassifier(n_estimators=5, max_depth=2, random_state=3).fit(shop[F], shop["joined"])
    newcomer = pd.DataFrame({"visits": [7], "basket_rs": [1000]})
    votes = [int(t.predict(newcomer.values)[0]) for t in forest.estimators_]
    expect("ch04 forest votes", votes, [0, 1, 1, 1, 1])
    boost = GradientBoostingClassifier(n_estimators=4, max_depth=1, learning_rate=1.0, random_state=0).fit(shop[F], shop["joined"])
    staged = [p.astype(int).tolist() for p in boost.staged_predict(shop[F])]
    wrong = [int((np.array(p) != shop["joined"].values).sum()) for p in staged]
    expect("ch04 booster mistakes by round", wrong, [1, 0, 0, 0])
    stumps = [rules(boost.estimators_[i, 0], regress=True) for i in range(4)]
    # Which shoppers each forest tree drew, with repeats: scikit-learn's own bootstrap draw for that
    # tree, checked against the number of distinct shoppers the fitted tree reports at its root.
    from sklearn.ensemble._forest import _generate_sample_indices
    drawn = []
    for t in forest.estimators_:
        counts = np.bincount(_generate_sample_indices(t.random_state, len(shop), len(shop), None), minlength=len(shop))
        expect("ch04 forest draw matches its tree", int((counts > 0).sum()), int(t.tree_.n_node_samples[0]))
        drawn.append(counts.astype(int).tolist())
    leaves100 = sum(t.get_n_leaves() for t in RandomForestClassifier(100, max_depth=2, random_state=0)
                    .fit(shop[F], shop["joined"]).estimators_)
    expect("ch04 leaves to read", (int(tree.get_n_leaves()), int(leaves100), 200), (3, 280, 200))
    scaler = StandardScaler().fit(shop[F])
    Z = scaler.transform(shop[F])
    groups = KMeans(n_clusters=3, n_init=10, random_state=0).fit_predict(Z)
    # Lloyd's steps from three starting shoppers, drawn on the page; the end must be sklearn's grouping.
    history, labels, chosen = None, None, []
    for start in ([2, 6, 8], [5, 6, 9], [3, 5, 11]):
        c = Z[start].copy()
        hist = [c.copy()]
        for _ in range(20):
            lab = np.argmin(((Z[:, None, :] - c[None, :, :]) ** 2).sum(axis=2), axis=1)
            new = np.array([Z[lab == j].mean(axis=0) if (lab == j).any() else c[j] for j in range(3)])
            if np.allclose(new, c):
                break
            c = new
            hist.append(c.copy())
        same = all(len(set(groups[lab == j])) == 1 for j in range(3)) and len(set(lab)) == 3
        if same:
            history, labels, chosen = hist, lab, start
            break
    expect("ch04 k-means steps end on sklearn's three groups", history is not None, True)
    ch04 = {"visits": shop["visits"].tolist(), "basket": shop["basket_rs"].tolist(), "joined": shop["joined"].tolist(),
            "tree": rules(tree), "forest": [rules(t) for t in forest.estimators_], "drawn": drawn, "votes": votes,
            "boost": {"stumps": stumps, "staged": staged, "wrong": wrong},
            "leaves": {"tree": int(tree.get_n_leaves()), "forest100": int(leaves100), "boost100": 200},
            "kmeans": {"start": [int(i) for i in chosen], "labels": [int(v) for v in labels],
                       "centres": [[[r(v, 2) for v in row] for row in scaler.inverse_transform(cc)] for cc in history]}}
    return {"ch03": ch03, "ch04": ch04}


if __name__ == "__main__":
    data = {
        "label": "UCI Bank Marketing (CC BY 4.0), the week's seeded split and Wednesday's honest columns, rerun as Thursday's case notebooks run it; the invented block reruns notebooks ch03 and ch04.",
        "bank": bank_numbers(),
        "invented": invented_numbers(),
    }
    if FAILS:
        raise SystemExit(f"{len(FAILS)} numbers differ from the notebooks: {', '.join(FAILS)}")
    OUT.write_text(json.dumps(data, separators=(",", ":")) + "\n")
    b = data["bank"]
    print(f"wrote {OUT.name}, {OUT.stat().st_size:,} bytes")
    print(f"tree {b['tree']['train_right']:,} of {b['split']['train']:,} on training, {b['tree']['val_right']:,} of {b['split']['val']:,} on validation; "
          f"{b['tree']['story']['sample_wrong']} wrong in the drawn third of the training rows")
    print(f"race low end Rs {b['race']['low_rs']:,} against an invented Rs {b['race']['extra_cost_invented']:,}")

# Test inputs and expected outcomes
# --------------------------------
# python3 content/W05/D4/4_trainer_only/C2_W05_D04_explorer_data_INTERNAL.py
#     Prints one PASS line per number it checks against case01, case02, case03, ch03 and ch04 (split
#     24,712 / 8,238 / 8,238; call nobody 7,310; the unlimited tree 0.996 and 0.841, depth 37, 3,662
#     leaves, 1,709 with one customer; depth 3 at 0.1005; the folds 0.7709 to 0.7983; the scaler
#     0.78648 against 0.78645; race means 0.786, 0.782, 0.791, 0.793; bills Rs 278,560 to Rs 292,400;
#     extra buyers 0, 133, 100, 92, 125 and a low end of Rs 50,939), then the file it wrote.
# A notebook number that no longer reproduces prints FAIL and the script exits with an error naming
#     it, before any JSON is written, so a stale page cannot be built from a moved pipeline.
# Run it twice: the second run reads the bank's file from ~/.cache/c2_datasets and writes identical
#     JSON, because every split, draw and model is seeded.
