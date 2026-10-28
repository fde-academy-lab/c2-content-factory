"""Draw every chart the W05 D1 deck places, from the same code the notebooks run.

Usage:
    python3 content/W05/D1/4_trainer_only/C2_W05_D01_make_figures_INTERNAL.py

Writes PNGs into ../1_in_class_training_content/slides/img/. The public datasets are cached in
~/.cache/c2_datasets, exactly as the notebooks cache them, so nothing else is written to the
repository. Invented teaching tables are typed here as they are typed in the notebooks.
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
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

OUT = pathlib.Path(__file__).resolve().parent.parent / "1_in_class_training_content" / "slides" / "img"
OUT.mkdir(parents=True, exist_ok=True)
CACHE = pathlib.Path.home() / ".cache" / "c2_datasets"
CACHE.mkdir(parents=True, exist_ok=True)

INK, VIOLET, LILAC, NIGHT, AMBER, RED, GREY = "#1C1B16", "#5B3FD6", "#9C88F0", "#1A0F5C", "#C98A00", "#C0392B", "#9A968C"
plt.rcParams.update({"font.size": 15, "axes.titlesize": 17, "axes.labelsize": 15, "xtick.labelsize": 14,
                     "ytick.labelsize": 14, "legend.fontsize": 13, "axes.spines.top": False,
                     "axes.spines.right": False, "font.family": "DejaVu Sans"})


def save(fig, name):
    name = f"C2_W05_D01_{name[:-4]}_STUDENT.png"
    fig.savefig(OUT / name, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", name)


def load_bank():
    f = CACHE / "bank-additional-full.csv"
    if not f.exists():
        url = "https://archive.ics.uci.edu/static/public/222/bank+marketing.zip"  # verified 28 October 2026
        outer = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(url, timeout=60).read()))
        inner = zipfile.ZipFile(io.BytesIO(outer.read("bank-additional.zip")))
        f.write_bytes(inner.read("bank-additional/bank-additional-full.csv"))
    return pd.read_csv(f, sep=";")


def load_cars():
    f = CACHE / "auto-mpg.data"
    if not f.exists():
        z = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(
            "https://archive.ics.uci.edu/static/public/9/auto+mpg.zip", timeout=60).read()))  # verified 28 October 2026
        f.write_bytes(z.read("auto-mpg.data"))
    names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"]
    return pd.read_csv(f, sep=r"\s+", names=names, na_values="?")


PROFILE = ["age", "job", "marital", "education", "default", "housing", "loan"]
HISTORY = ["contact", "month", "day_of_week", "campaign", "previous", "poutcome"]
COLUMNS = PROFILE + HISTORY


def week_split(df, seed=42):
    y = (df["y"] == "yes").astype(int)
    rest, test = train_test_split(df.index, test_size=0.20, stratify=y, random_state=seed)
    train, val = train_test_split(rest, test_size=0.25, stratify=y.loc[rest], random_state=seed)
    return df.loc[train], df.loc[val], df.loc[test]


def logistic(columns, df):
    num = [c for c in columns if pd.api.types.is_numeric_dtype(df[c])]
    cat = [c for c in columns if c not in num]
    prep = ColumnTransformer([("num", StandardScaler(), num), ("cat", OneHotEncoder(handle_unknown="ignore"), cat)])
    return Pipeline([("prep", prep), ("model", LogisticRegression(max_iter=2000))])


def timeline():
    fig, ax = plt.subplots(figsize=(11, 3.2))
    ax.axhline(0, color=INK, lw=2)
    ax.axvspan(0, 6, color="#EEEAFB")
    ax.axvspan(6, 9, color="#FFF7E6")
    ax.axvline(6, color=VIOLET, lw=4)
    ax.text(3, 0.45, "past rows: what is known\nprofile, earlier campaigns, orders", ha="center")
    ax.text(5.9, -0.85, "the cut = prediction moment", ha="right", color=VIOLET, fontweight="bold")
    ax.text(7.5, 0.45, "outcome window\nthe target lives here", ha="center", color="#8A5A1F")
    ax.set_xlim(0, 9); ax.set_ylim(-1.2, 1.1); ax.axis("off")
    save(fig, "fig_timeline_monday.png")


def sort_questions():
    fig, ax = plt.subplots(figsize=(11, 3.8)); ax.axis("off")
    for x, t in [(0.02, "Answer already\nin the data?"), (0.36, "Decision written\nas a condition?"), (0.70, "Input now, target\nlater, decision moves?")]:
        ax.add_patch(plt.Rectangle((x, 0.55), 0.28, 0.32, fc="#EEEAFB", ec=VIOLET, lw=2))
        ax.text(x + 0.14, 0.71, t, ha="center", va="center")
    for x, t, c in [(0.02, "QUERY", GREY), (0.36, "RULE", AMBER), (0.70, "PREDICTION", VIOLET)]:
        ax.text(x + 0.14, 0.18, t, ha="center", va="center", color="white", fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.5", fc=c, ec=c))
        ax.annotate("", xy=(x + 0.14, 0.30), xytext=(x + 0.14, 0.55), arrowprops=dict(arrowstyle="->", lw=2))
        ax.text(x + 0.17, 0.42, "yes")
    for x in (0.30, 0.64):
        ax.annotate("", xy=(x + 0.06, 0.71), xytext=(x, 0.71), arrowprops=dict(arrowstyle="->", lw=2))
        ax.text(x + 0.03, 0.78, "no", ha="center")
    save(fig, "fig_ch1_three_tests.png")


def member_timeline():
    orders = pd.DataFrame({
        "member": ["M1", "M1", "M2", "M2", "M2", "M3", "M4", "M4"],
        "order_date": pd.to_datetime(["2026-04-10", "2026-07-20", "2026-05-02", "2026-06-15", "2026-06-28",
                                      "2026-06-01", "2026-04-25", "2026-10-15"])})
    cutoff = pd.Timestamp("2026-06-30"); end = cutoff + pd.Timedelta(days=90)
    fig, ax = plt.subplots(figsize=(11, 3.6))
    ax.axvspan(cutoff, end, color="#FFF7E6")
    ax.axvline(cutoff, color=VIOLET, lw=4)
    for i, m in enumerate(["M1", "M2", "M3", "M4"]):
        d = orders[orders["member"] == m]
        cols = [VIOLET if t <= cutoff else (AMBER if t <= end else GREY) for t in d["order_date"]]
        ax.scatter(d["order_date"], [i] * len(d), s=180, c=cols, zorder=3)
    ax.set_yticks(range(4)); ax.set_yticklabels(["M1", "M2", "M3", "M4"])
    ax.text(cutoff, 3.65, " cutoff: 30 June", color=VIOLET, fontweight="bold")
    ax.text(cutoff + pd.Timedelta(days=45), -0.75, "90-day window", ha="center", color="#8A5A1F")
    ax.set_ylim(-1.0, 4.1)
    save(fig, "fig_ch2_four_members.png")


def split_squares():
    members = pd.DataFrame({"member": [f"M{i:02d}" for i in range(1, 21)],
                            "repeat_90d": [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]})
    fig, axes = plt.subplots(2, 1, figsize=(11, 2.8))
    colour = {"train": VIOLET, "validation": LILAC, "test": AMBER}
    for ax, seed in zip(axes, (42, 7)):
        rest, te = train_test_split(members, test_size=4, stratify=members["repeat_90d"], random_state=seed)
        tr, va = train_test_split(rest, test_size=4, stratify=rest["repeat_90d"], random_state=seed)
        where = {m: "train" for m in tr["member"]} | {m: "validation" for m in va["member"]} | {m: "test" for m in te["member"]}
        for i, m in enumerate(members["member"]):
            ax.add_patch(plt.Rectangle((i, 0), 0.9, 0.9, color=colour[where[m]]))
            if members.loc[i, "repeat_90d"]:
                ax.text(i + 0.45, 0.45, "Y", ha="center", va="center", color="white", fontweight="bold")
        ax.set_xlim(0, 20); ax.set_ylim(0, 1); ax.axis("off"); ax.set_title(f"seed {seed}", loc="left")
    plt.subplots_adjust(hspace=0.7)
    save(fig, "fig_ch3_two_seeds.png")


def residual_squares():
    x = pd.Series([1, 2, 3, 4, 5, 6]); y = pd.Series([290, 450, 500, 700, 750, 910])
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.4))
    for ax, (name, a, b, total) in zip(axes, [("the mean line", 600, 0, "257,200"), ("least squares", 180, 120, "5,200")]):
        pred = a + b * x
        ax.scatter(x, y, color=INK, s=70, zorder=3)
        ax.plot([0.5, 6.5], [a + b * 0.5, a + b * 6.5], color=VIOLET, lw=3)
        for xi, yi, pi in zip(x, y, pred):
            ax.add_patch(plt.Rectangle((xi, min(yi, pi)), abs(yi - pi) / 160, abs(yi - pi), color=RED, alpha=0.25))
            ax.plot([xi, xi], [yi, pi], color=RED, lw=2)
        ax.set_title(f"{name}: squares add to {total}")
        ax.set_xlabel("visits last month"); ax.set_ylabel("spend, Rs")
        ax.set_xlim(0, 8.6); ax.set_ylim(0, 1100)
    plt.tight_layout()
    save(fig, "fig_ch4_squares.png")
    fig, ax = plt.subplots(figsize=(8, 4.4))
    ax.scatter(x, y, color=INK, s=80, zorder=3)
    for xi, yi in zip(x, y):
        ax.text(xi + 0.08, yi - 55, f"Rs {yi}", fontsize=13)
    ax.set_xlabel("visits last month"); ax.set_ylabel("spend this month, Rs"); ax.set_ylim(0, 1100); ax.set_xlim(0, 7)
    ax.set_title("Six members of one store (invented)")
    save(fig, "fig_ch4_six_points.png")


def line_vs_s():
    m = pd.DataFrame({"visits": [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 7], "repeat_90d": [0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1]})
    line = LinearRegression().fit(m[["visits"]], m["repeat_90d"])
    logit = LogisticRegression(C=1e6).fit(m[["visits"]], m["repeat_90d"])
    g = pd.DataFrame({"visits": np.linspace(0, 8, 161)})
    p4 = logit.predict_proba(pd.DataFrame({"visits": [4]}))[0, 1]
    for name, show_s in [("fig_ch5_line_only.png", False), ("fig_ch5_line_vs_s.png", True)]:
        fig, ax = plt.subplots(figsize=(10, 4.4))
        ax.scatter(m["visits"], m["repeat_90d"], s=110, color=INK, zorder=3)
        ax.plot(g["visits"], line.predict(g), color=GREY, ls="--", lw=2, label="straight line")
        ax.axhline(1, color=RED, lw=1); ax.axhline(0, color=RED, lw=1)
        ax.text(8.05, line.predict(pd.DataFrame({"visits": [8]}))[0], " 1.28", color=GREY, va="center")
        if show_s:
            ax.plot(g["visits"], logit.predict_proba(g)[:, 1], color=VIOLET, lw=4, label="logistic S-curve")
            ax.scatter([4], [p4], s=200, color=AMBER, zorder=4)
            ax.text(4.2, p4 - 0.12, f"4 visits: {p4:.2f}", color="#8A5A1F", fontweight="bold")
        ax.set_xlabel("visits last quarter"); ax.set_ylabel("bought again (0 or 1)")
        ax.set_xlim(-0.3, 8.8); ax.set_ylim(-0.25, 1.4); ax.legend(loc="upper left")
        save(fig, name)


def mpg_bow():
    cars = load_cars().dropna(subset=["horsepower"]).reset_index(drop=True)
    line = LinearRegression().fit(cars[["horsepower"]], cars["mpg"])
    cars["hp2"] = cars["horsepower"] ** 2
    curve = LinearRegression().fit(cars[["horsepower", "hp2"]], cars["mpg"])
    cars["r1"] = cars["mpg"] - line.predict(cars[["horsepower"]])
    cars["r2"] = cars["mpg"] - curve.predict(cars[["horsepower", "hp2"]])
    bins = pd.qcut(cars["horsepower"], 5)
    g = pd.DataFrame({"horsepower": np.linspace(46, 230, 100)}); g["hp2"] = g["horsepower"] ** 2
    fig, ax = plt.subplots(figsize=(10, 4.4))
    ax.scatter(cars["horsepower"], cars["mpg"], s=14, color=GREY)
    ax.plot(g["horsepower"], line.predict(g[["horsepower"]]), color=RED, lw=3, label="straight line")
    ax.set_xlabel("horsepower"); ax.set_ylabel("miles per gallon"); ax.legend()
    ax.set_title("392 cars (UCI Auto MPG)")
    save(fig, "fig_ch6_scatter_line.png")
    for col, name, title in [("r1", "fig_ch6_resid_line.png", "Residuals of the line: a bow"),
                             ("r2", "fig_ch6_resid_curve.png", "With horsepower squared: flat")]:
        fig, ax = plt.subplots(figsize=(10, 4.2))
        ax.scatter(cars["horsepower"], cars[col], s=14, color=GREY)
        means = cars.groupby(bins, observed=True)[col].mean()
        ax.plot([iv.mid for iv in means.index], means.values, color=RED, lw=4, marker="o", ms=10)
        for iv, v in zip(means.index, means.values):
            ax.text(iv.mid, v + 1.6, f"{v:+.1f}", ha="center", color=RED, fontweight="bold")
        ax.axhline(0, color=INK, lw=1.2); ax.set_ylim(-15, 18)
        ax.set_xlabel("horsepower"); ax.set_ylabel("residual, mpg"); ax.set_title(title)
        save(fig, name)
    fig, ax = plt.subplots(figsize=(10, 4.2))
    g2 = pd.DataFrame({"horsepower": np.linspace(46, 300, 120)}); g2["hp2"] = g2["horsepower"] ** 2
    ax.scatter(cars["horsepower"], cars["mpg"], s=14, color=GREY)
    ax.plot(g2["horsepower"], curve.predict(g2), color=VIOLET, lw=3)
    ax.axvspan(230, 300, color="#FDECEA")
    ax.text(265, 33, "no data here", ha="center", color=RED)
    ax.set_xlabel("horsepower"); ax.set_ylabel("miles per gallon"); ax.set_ylim(0, 48)
    ax.set_title("The curve that fixed the bow turns up past about 190 hp")
    save(fig, "fig_ch6_extrapolate.png")


def bank_figures():
    bank = load_bank()
    train, val, test = week_split(bank)
    y = (bank["y"] == "yes").astype(int)
    y_train, y_val = y.loc[train.index], y.loc[val.index]
    counts = bank["y"].value_counts()
    fig, ax = plt.subplots(figsize=(10, 3.2))
    ax.barh(["no", "yes"], [counts["no"], counts["yes"]], color=[GREY, VIOLET])
    for i, v in enumerate([counts["no"], counts["yes"]]):
        ax.text(v + 300, i, f"{v:,}", va="center", fontweight="bold")
    ax.set_xlim(0, 44000); ax.set_title("41,188 calls, May 2008 to November 2010")
    save(fig, "fig_case1_yes_no.png")

    sizes = [len(train), len(val), len(test)]
    shares = [(p["y"] == "yes").mean() for p in (train, val, test)]
    fig, ax = plt.subplots(figsize=(10, 4.2))
    bars = ax.bar(["train", "validation", "test"], sizes, color=[VIOLET, LILAC, "white"], edgecolor=INK, hatch=["", "", "//"])
    for b, n, s in zip(bars, sizes, shares):
        ax.text(b.get_x() + b.get_width() / 2, n + 500, f"{n:,} rows\n{s:.1%} yes", ha="center")
    ax.text(2, 1200, "SEALED\nuntil Friday", ha="center", fontweight="bold", fontsize=13)
    ax.set_ylim(0, 31000); ax.set_ylabel("rows")
    save(fig, "fig_case1_split.png")

    model = logistic(COLUMNS, bank).fit(train[COLUMNS], y_train)
    p_val = model.predict_proba(val[COLUMNS])[:, 1]
    pred = (p_val >= 0.5).astype(int)
    right_model, right_base = int((pred == y_val).sum()), int((y_val == 0).sum())
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 4.4))
    a1.bar(["call nobody", "model"], [right_base, right_model], color=[GREY, VIOLET])
    for i, v in enumerate([right_base, right_model]):
        a1.text(i, v + 120, f"{v:,}", ha="center", fontweight="bold")
    a1.set_ylim(0, 8800); a1.set_title("Right answers of 8,238")
    a2.bar(["call nobody", "model"], [0, right_model - right_base], color=[GREY, VIOLET])
    a2.text(1, right_model - right_base + 3, f"+{right_model - right_base}", ha="center", fontweight="bold")
    a2.set_ylim(0, 120); a2.set_title("What the model adds")
    plt.tight_layout()
    save(fig, "fig_case2_edge.png")

    fig, ax = plt.subplots(figsize=(10, 4.0))
    ax.hist(p_val, bins=40, color=VIOLET)
    ax.axvline(0.5, color=RED, ls="--", lw=2); ax.text(0.51, ax.get_ylim()[1] * 0.8, "0.5", color=RED)
    ax.set_xlabel("predicted probability of yes"); ax.set_ylabel("clients")
    ax.set_title(f"Mean probability {p_val.mean():.3f}; share of yes {y_val.mean():.3f}")
    save(fig, "fig_case2_probs.png")

    order = {m: i for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])}
    year, prev, years = 2008, -1, []
    for m in bank["month"]:
        if order[m] < prev:
            year += 1
        prev = order[m]; years.append(year)
    by_year = bank.assign(year=years).groupby("year")["y"].agg(rows="size", share=lambda s: (s == "yes").mean())
    fig, ax = plt.subplots(figsize=(9, 4.2))
    ax.bar(by_year.index.astype(str), by_year["share"], color=[LILAC, VIOLET, NIGHT])
    for i, (n, s) in enumerate(zip(by_year["rows"], by_year["share"])):
        ax.text(i, s + 0.02, f"{s:.0%} of {n:,}", ha="center", fontweight="bold")
    ax.set_ylim(0, 0.65); ax.set_ylabel("share of yes")
    save(fig, "fig_case2_years.png")

    peek_idx, fresh_idx = train_test_split(val.index, train_size=2000, stratify=y.loc[val.index], random_state=7)
    rng = np.random.default_rng(42)
    rows = []
    for k in range(60):
        cols = [str(c) for c in rng.choice(COLUMNS, size=int(rng.integers(3, 14)), replace=False)]
        mm = logistic(cols, bank).fit(train[cols], y_train)
        rows.append({"peek": accuracy_score(y.loc[peek_idx], mm.predict(bank.loc[peek_idx, cols])),
                     "fresh": accuracy_score(y.loc[fresh_idx], mm.predict(bank.loc[fresh_idx, cols]))})
    runs = pd.DataFrame(rows).sort_values("peek").reset_index(drop=True)
    base_peek = 1 - y.loc[peek_idx].mean()
    fig, ax = plt.subplots(figsize=(11, 4.6))
    ax.scatter(range(60), runs["peek"], color=LILAC, s=40, label="peeked score")
    ax.scatter(range(60), runs["fresh"], color=INK, s=24, marker="x", label="same version, fresh rows")
    ax.axhline(base_peek, color=GREY, ls="--"); ax.text(1, base_peek + 0.0008, "doing nothing", color="#6B675E")
    i = 59
    ax.annotate("", xy=(i, runs.loc[i, "fresh"]), xytext=(i, runs.loc[i, "peek"]), arrowprops=dict(arrowstyle="->", color=RED, lw=3))
    ax.text(i - 1.5, runs.loc[i, "peek"], f"chosen: {runs.loc[i, 'peek']:.3f}", ha="right", va="center", color=RED, fontweight="bold")
    ax.text(i - 1.5, runs.loc[i, "fresh"] - 0.002, f"fresh rows: {runs.loc[i, 'fresh']:.3f}", ha="right", color=RED, fontweight="bold")
    ax.set_xlabel("60 versions, sorted by peeked score"); ax.set_ylabel("accuracy"); ax.legend(loc="lower right")
    save(fig, "fig_case3_peek.png")


def four_residuals():
    """Four residual plots from the same 392 cars, for the practice set's matching problem."""
    cars = load_cars().dropna(subset=["horsepower"]).reset_index(drop=True)
    cars["hp2"] = cars["horsepower"] ** 2
    line = LinearRegression().fit(cars[["horsepower"]], cars["mpg"])
    curve = LinearRegression().fit(cars[["horsepower", "hp2"]], cars["mpg"])
    cars["r_line"] = cars["mpg"] - line.predict(cars[["horsepower"]])
    cars["fit_curve"] = curve.predict(cars[["horsepower", "hp2"]])
    cars["r_curve"] = cars["mpg"] - cars["fit_curve"]
    panels = [("P", "horsepower", "r_line", "horsepower"), ("Q", "fit_curve", "r_curve", "predicted mpg"),
              ("R", "model_year", "r_curve", "model year (19xx)"), ("S", "horsepower", "r_curve", "horsepower")]
    fig, axes = plt.subplots(2, 2, figsize=(12, 7.6))
    for ax, (tag, x, r, xlabel) in zip(axes.ravel(), panels):
        ax.scatter(cars[x], cars[r], s=10, color=GREY)
        ax.axhline(0, color=INK, lw=1.2)
        ax.set_ylim(-15, 18); ax.set_xlabel(xlabel); ax.set_ylabel("residual, mpg")
        ax.set_title(f"Plot {tag}", loc="left", fontweight="bold")
    plt.tight_layout()
    save(fig, "fig_practice_four_residuals.png")


def drill_slide():
    """The four residual plots and the five causes on one wide picture, sized for a slide."""
    cars = load_cars().dropna(subset=["horsepower"]).reset_index(drop=True)
    cars["hp2"] = cars["horsepower"] ** 2
    line = LinearRegression().fit(cars[["horsepower"]], cars["mpg"])
    curve = LinearRegression().fit(cars[["horsepower", "hp2"]], cars["mpg"])
    cars["r_line"] = cars["mpg"] - line.predict(cars[["horsepower"]])
    cars["fit_curve"] = curve.predict(cars[["horsepower", "hp2"]])
    cars["r_curve"] = cars["mpg"] - cars["fit_curve"]
    fig = plt.figure(figsize=(16, 6.4))
    grid = fig.add_gridspec(2, 3, width_ratios=[1, 1, 1.15], wspace=0.3, hspace=0.55)
    panels = [("P", "horsepower", "r_line", "horsepower"), ("Q", "fit_curve", "r_curve", "predicted mpg"),
              ("R", "model_year", "r_curve", "model year"), ("S", "horsepower", "r_curve", "horsepower")]
    for k, (tag, x, r, xlabel) in enumerate(panels):
        ax = fig.add_subplot(grid[k // 2, k % 2])
        ax.scatter(cars[x], cars[r], s=8, color=GREY)
        ax.axhline(0, color=INK, lw=1.2); ax.set_ylim(-15, 18); ax.set_yticks([-10, 0, 10])
        ax.set_xlabel(xlabel, fontsize=17); ax.tick_params(labelsize=15)
        ax.set_title(f"Plot {tag}", loc="left", fontweight="bold", fontsize=19)
    tx = fig.add_subplot(grid[:, 2]); tx.axis("off")
    causes = ["a  an input left out\n    still carries signal", "b  the misses grow\n    with the prediction",
              "c  a straight line\n    missed a curve", "d  the test set was\n    peeked at", "e  centred on zero:\n    no shape left"]
    for i, c in enumerate(causes):
        tx.text(0, 0.95 - i * 0.2, c, fontsize=19, va="top", family="DejaVu Sans")
    tx.set_title("One cause is spare", loc="left", fontsize=19, fontweight="bold")
    save(fig, "fig_drill_residuals.png")


if __name__ == "__main__":
    timeline(); sort_questions(); member_timeline(); split_squares(); residual_squares(); line_vs_s(); mpg_bow(); bank_figures(); four_residuals(); drill_slide()

# Test inputs and expected outcomes
# --------------------------------
# python3 content/W05/D1/4_trainer_only/C2_W05_D01_make_figures_INTERNAL.py
#     Prints "wrote C2_W05_D01_fig_..." twenty times and leaves twenty PNGs in slides/img/.
# Run it twice in a row: the second run reads both datasets from ~/.cache/c2_datasets and draws the
#     same pictures, because every split and every column draw is seeded.
