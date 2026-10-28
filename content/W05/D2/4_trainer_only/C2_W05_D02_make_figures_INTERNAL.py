"""Draw every picture the W05 D2 deck places, from the same data and code as the notebooks.

Usage:
    python3 content/W05/D2/4_trainer_only/C2_W05_D02_make_figures_INTERNAL.py

It downloads UCI Bank Marketing and German Credit into ~/.cache/c2_datasets on the first run (the
notebooks' cached loader), rebuilds Monday's model on the week's seeded split, and writes PNGs into
1_in_class_training_content/slides/img/. The invented teaching tables are the ones typed in the
concept notebooks. Nothing else in the repository is written.
"""
import io, zipfile, pathlib, urllib.request
import numpy as np, pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

OUT = pathlib.Path(__file__).resolve().parents[1] / "1_in_class_training_content" / "slides" / "img"
OUT.mkdir(parents=True, exist_ok=True)
CACHE = pathlib.Path.home() / ".cache" / "c2_datasets"
CACHE.mkdir(parents=True, exist_ok=True)
INK, VIOLET, ROSE, GREEN, MUTED, LIGHT = "#1A0F5C", "#5B3FD6", "#D63A6A", "#1F8A5B", "#6B6690", "#EEEAFB"
plt.rcParams.update({"font.size": 15, "axes.titlesize": 16, "axes.spines.top": False, "axes.spines.right": False,
                     "savefig.dpi": 150, "savefig.bbox": "tight", "font.family": "DejaVu Sans"})


def save(fig, name):
    name = f"C2_W05_D02_{name[:-4]}_STUDENT.png"    # the day stem and the audience tag, as every pack file carries
    fig.savefig(OUT / name, facecolor="white")
    plt.close(fig)
    print("wrote", name)


# ---------- the week's pipeline (docs/detailing/W05_research/W05_week_pipeline.md) ----------
def load_bank():
    f = CACHE / "bank-additional-full.csv"
    if not f.exists():
        url = "https://archive.ics.uci.edu/static/public/222/bank+marketing.zip"  # verified 28 October 2026
        outer = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(url, timeout=60).read()))
        inner = zipfile.ZipFile(io.BytesIO(outer.read("bank-additional.zip")))
        f.write_bytes(inner.read("bank-additional/bank-additional-full.csv"))
    return pd.read_csv(f, sep=";")


COLS = ["age", "job", "marital", "education", "default", "housing", "loan",
        "contact", "month", "day_of_week", "campaign", "previous", "poutcome"]


def bank_scores():
    df = load_bank()
    y = (df["y"] == "yes").astype(int)
    rest, test = train_test_split(df.index, test_size=0.20, stratify=y, random_state=42)
    train, val = train_test_split(rest, test_size=0.25, stratify=y.loc[rest], random_state=42)
    num = [c for c in COLS if pd.api.types.is_numeric_dtype(df[c])]
    cat = [c for c in COLS if c not in num]
    prep = ColumnTransformer([("num", StandardScaler(), num), ("cat", OneHotEncoder(handle_unknown="ignore"), cat)])
    m = Pipeline([("prep", prep), ("model", LogisticRegression(max_iter=2000))])
    m.fit(df.loc[train, COLS], y.loc[train])
    return y.loc[val].to_numpy(), m.predict_proba(df.loc[val, COLS])[:, 1]


def cells(y, p, t):
    a = p >= t
    return int((a & (y == 1)).sum()), int((a & (y == 0)).sum()), int((~a & (y == 1)).sum()), int((~a & (y == 0)).sum())


# ---------- the roadmap and the week's picture ----------
def roadmap():
    weeks = ["W0\nBaseline", "W1\nData\nanalysis", "W2\nData\nmanip.", "W3\nBuild 1", "W4\nAnalyst\ncraft",
             "W5\nML core\n+ ME1", "W6\nBuild 2\nML mini", "W7\nDeep\nlearning", "W8\nTrans-\nformers", "W9\nBuild 3",
             "W10\nGenAI\n+ ME2", "W11\nRAG", "W12\nBuild 4", "W13\nAgents", "W14\nAgents\nin prod", "W15\nBuild 5",
             "W16\nME3\n+ FDE", "W17-20\nCapstone"]
    fig, ax = plt.subplots(figsize=(16, 3.2))
    for i, w in enumerate(weeks):
        done, now = i < 5, i == 5
        col = INK if now else (LIGHT if done else "white")
        ax.add_patch(plt.Rectangle((i, 0), 0.92, 1, facecolor=col, edgecolor=VIOLET if (done or now) else "#B8B2D6", lw=1.5))
        ax.text(i + 0.46, 0.5, w, ha="center", va="center", fontsize=9.5, color="white" if now else (INK if done else MUTED))
    ax.annotate("today: Tuesday,\nthe metric trap", (5.46, 1.0), (5.46, 1.6), ha="center", color=ROSE, fontsize=13,
                arrowprops={"arrowstyle": "->", "color": ROSE})
    ax.annotate("next week: Build 2 puts\nRohan's costs in the brief", (6.46, 0), (8.8, -0.75), ha="center", color=VIOLET,
                fontsize=12, arrowprops={"arrowstyle": "->", "color": VIOLET})
    ax.set_xlim(-0.1, 18); ax.set_ylim(-1.1, 2.1); ax.axis("off")
    save(fig, "roadmap.png")


def timeline_tuesday(y, p):
    fig = plt.figure(figsize=(12, 6.0))
    top = fig.add_axes([0.03, 0.62, 0.94, 0.33]); top.axis("off"); top.set_xlim(0, 10); top.set_ylim(0, 1)
    top.add_patch(plt.Rectangle((0.2, 0.35), 4.6, 0.3, color=LIGHT)); top.text(2.5, 0.5, "past rows: what we knew (Mon)", ha="center", va="center", color=INK)
    top.plot([4.9, 4.9], [0.15, 0.85], color=INK, lw=3); top.text(4.9, 0.95, "the cut (Mon)", ha="center", color=INK, fontsize=13)
    top.add_patch(plt.Polygon([[5.4, 0.2], [5.7, 0.5], [5.4, 0.8]], color=VIOLET)); top.text(5.75, 0.0, "prediction moment:\nthe morning of the call", ha="center", color=VIOLET, fontsize=12)
    top.add_patch(plt.Rectangle((6.2, 0.35), 3.4, 0.3, color="#FCEBF0")); top.text(7.9, 0.5, "outcome window: did they buy?", ha="center", va="center", color=ROSE)
    hum = fig.add_axes([0.06, 0.08, 0.5, 0.45])
    bins = np.linspace(0, 0.8, 41)
    hum.hist(p[y == 0], bins=bins, color=MUTED, alpha=0.5, density=True, label="did not buy")
    hum.hist(p[y == 1], bins=bins, color=GREEN, alpha=0.7, density=True, label="bought")
    t_line = np.sort(p)[::-1][999]          # the budget line: the 1,000th score
    hum.axvline(t_line, color=ROSE, lw=3); hum.text(t_line + 0.01, hum.get_ylim()[1] * 0.8, f"threshold {t_line:.3f}", color=ROSE)
    hum.set_yticks([]); hum.set_xlabel("score: P(buy)"); hum.legend(frameon=False, fontsize=12); hum.set_title("Tue: two humps and a line", color=INK)
    box = fig.add_axes([0.63, 0.06, 0.32, 0.47]); box.axis("off"); box.set_xlim(0, 2); box.set_ylim(0, 2)
    tp, fp, fn, tn = cells(y, p, t_line)
    for (x, yy, lab, n, c) in ((0, 1, "TP", tp, GREEN), (1, 1, "FN", fn, ROSE), (0, 0, "FP", fp, ROSE), (1, 0, "TN", tn, MUTED)):
        box.add_patch(plt.Rectangle((x, yy), 0.96, 0.96, color=c, alpha=0.18)); box.text(x + 0.48, yy + 0.48, f"{lab}\n{n:,}", ha="center", va="center", fontsize=15, color=INK)
    box.set_title("Tue: the four boxes at that line", color=INK)
    save(fig, "timeline_tuesday.png")


# ---------- concept chapters, on the invented tables typed in the notebooks ----------
KALPA20 = pd.DataFrame({"customer": [f"C{i:02d}" for i in range(1, 21)],
                        "nudge": [0,1,0,0,1,0,1,0,0,0,1,0,0,1,0,1,0,0,0,0],
                        "back":  [0,1,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0]})


def ch1_four_boxes():
    boxes = {"TP": [], "FP": [], "FN": [], "TN": []}
    for _, r in KALPA20.iterrows():
        boxes[("T" if r.nudge == r.back else "F") + ("P" if r.nudge else "N")].append(r.customer)
    meaning = {"TP": "nudged, came back", "FN": "left alone, came back", "FP": "nudged, did not", "TN": "left alone, did not"}
    fig, ax = plt.subplots(figsize=(10, 6.4))
    for k, (x, y, col) in {"TP": (0, 1, GREEN), "FN": (1, 1, ROSE), "FP": (0, 0, ROSE), "TN": (1, 0, MUTED)}.items():
        ax.add_patch(plt.Rectangle((x, y), 0.97, 0.97, color=col, alpha=0.16))
        ax.text(x + 0.48, y + 0.8, f"{k}: {len(boxes[k])}", ha="center", fontsize=20, weight="bold", color=INK)
        ax.text(x + 0.48, y + 0.66, meaning[k], ha="center", fontsize=13, color=INK)
        for i, c in enumerate(boxes[k]):
            ax.text(x + 0.1 + (i % 4) * 0.22, y + 0.42 - (i // 4) * 0.14, c, fontsize=13, color=col, weight="bold")
    ax.set_xlim(0, 2); ax.set_ylim(0, 2); ax.set_xticks([0.5, 1.5]); ax.set_xticklabels(["model: nudge", "model: leave"])
    ax.set_yticks([1.5, 0.5]); ax.set_yticklabels(["came back", "did not"]); ax.tick_params(length=0)
    save(fig, "ch1_four_boxes.png")


def ch2_denominators():
    TP, FP, FN, TN = 3, 3, 2, 12
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.2))
    for ax, title, hi in ((axes[0], "Precision = 3 / (3 + 3): the nudge column", "col"), (axes[1], "Recall = 3 / (3 + 2): the came-back row", "row")):
        vals = [[TP, FN], [FP, TN]]; names = [["TP", "FN"], ["FP", "TN"]]
        for i in range(2):
            for j in range(2):
                lit = (hi == "col" and j == 0) or (hi == "row" and i == 0)
                ax.add_patch(plt.Rectangle((j, 1 - i), 0.97, 0.97, color=VIOLET if lit else MUTED, alpha=0.35 if lit else 0.08))
                ax.text(j + 0.48, 1.48 - i, f"{names[i][j]}\n{vals[i][j]}", ha="center", va="center", fontsize=20, color=INK)
        ax.set_xlim(0, 2); ax.set_ylim(0, 2); ax.set_xticks([0.5, 1.5]); ax.set_xticklabels(["nudge", "leave"])
        ax.set_yticks([1.5, 0.5]); ax.set_yticklabels(["came back", "did not"]); ax.tick_params(length=0); ax.set_title(title, color=INK)
    save(fig, "ch2_denominators.png")


def ch2_f1():
    f1 = lambda p, r: 2 * p * r / (p + r)
    r = np.linspace(0.01, 1, 100)
    fig, ax = plt.subplots(figsize=(11, 4.8))
    ax.plot(r, (0.9 + r) / 2, color=MUTED, ls="--", lw=2.5, label="plain mean")
    ax.plot(r, f1(0.9, r), color=VIOLET, lw=3, label="F1, the harmonic mean")
    ax.scatter([0.1], [f1(0.9, 0.1)], color=ROSE, s=80, zorder=5); ax.annotate("recall 0.1: mean 0.50, F1 0.18", (0.1, f1(0.9, 0.1)), (0.22, 0.12), color=ROSE)
    ax.set_xlabel("recall, with precision held at 0.9"); ax.set_ylabel("score"); ax.legend(frameon=False, loc="lower right")
    save(fig, "ch2_f1.png")


def ch3_dots():
    fig, ax = plt.subplots(figsize=(6.4, 6.4))
    for i in range(100):
        ax.scatter(i % 10, 9 - i // 10, s=420, color=GREEN if i < 11 else MUTED, alpha=0.95 if i < 11 else 0.35)
    ax.set_xticks([]); ax.set_yticks([]); ax.set_title("100 invented customers, 11 repeaters", color=INK)
    for s in ax.spines.values(): s.set_visible(False)
    save(fig, "ch3_dots.png")


def ch3_free_accuracy():
    b = np.linspace(0.01, 0.5, 100)
    fig, ax = plt.subplots(figsize=(11, 4.8))
    ax.plot(b * 100, (1 - b) * 100, color=ROSE, lw=3)
    for rate, name in ((0.04, "Kalpa's row: 4%"), (0.113, "the bank: 11.3%"), (0.30, "German Credit bad: 30%"), (0.5, "balanced: 50%")):
        ax.scatter(rate * 100, (1 - rate) * 100, color=INK, zorder=5, s=60)
        ax.annotate(name, (rate * 100, (1 - rate) * 100), (rate * 100 + 1.5, (1 - rate) * 100 + 2.5), fontsize=13)
    ax.set_xlabel("base rate of the outcome, %"); ax.set_ylabel("accuracy for saying no to all, %"); ax.set_ylim(45, 102)
    save(fig, "ch3_free_accuracy.png")


def coins(n, small, big, name, small_label, big_label):
    fig, ax = plt.subplots(figsize=(13, 3.8))
    per_row = 15 if n > 20 else 10
    for i in range(n):
        x, yy = i % per_row * 0.6 + 0.35, 1.0 - (i // per_row) * 0.65
        ax.add_patch(plt.Circle((x, yy), 0.25, color=MUTED, alpha=0.6)); ax.text(x, yy, small, ha="center", va="center", fontsize=10, color="white")
    w = per_row * 0.6
    ax.text(w / 2, -0.45, small_label, ha="center", fontsize=14, color=INK)
    ax.text(w + 0.5, 0.7, "=", fontsize=34, ha="center", va="center", color=INK)
    ax.add_patch(plt.Rectangle((w + 1.1, 0.2), 2.2, 1.0, color=GREEN if "buyer" in big_label else ROSE, alpha=0.85))
    ax.text(w + 2.2, 0.7, big, ha="center", va="center", fontsize=17, color="white", weight="bold")
    ax.text(w + 2.2, -0.45, big_label, ha="center", fontsize=14, color=INK)
    ax.set_xlim(0, w + 3.6); ax.set_ylim(-0.8, 1.5); ax.axis("off"); ax.set_aspect("equal")
    save(fig, name)


def ch5_bill_steps():
    p = np.array([0.92, 0.81, 0.66, 0.55, 0.43, 0.38, 0.30, 0.22, 0.18, 0.14, 0.11, 0.09, 0.07, 0.05, 0.035, 0.025, 0.02, 0.015, 0.01, 0.005])
    y = np.array([1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0])
    grid = np.linspace(0, 1, 401)
    bills = [cells(y, p, t)[1] * 40 + cells(y, p, t)[2] * 1200 for t in grid]
    accs = [(cells(y, p, t)[0] + cells(y, p, t)[3]) / 20 * 100 for t in grid]
    fig, ax1 = plt.subplots(figsize=(12, 5))
    ax1.step(grid, bills, where="post", color=VIOLET, lw=3); ax1.set_ylabel("bill, Rs", color=VIOLET)
    ax1.axvline(1 / 31, color=INK, lw=1.5)
    ax1.annotate("0.032: Rs 360", (1 / 31, 360), (0.12, 3300), color=INK, arrowprops={"arrowstyle": "->", "color": INK})
    ax1.axvline(0.5, color=MUTED, lw=1.2, ls=":")
    ax1.annotate("0.5: Rs 3,640", (0.5, 3640), (0.6, 1800), color=INK, arrowprops={"arrowstyle": "->", "color": INK})
    ax1.set_xlabel("the line: nudge everyone scoring at or above")
    ax2 = ax1.twinx(); ax2.step(grid, accs, where="post", color=ROSE, lw=2, ls="--"); ax2.set_ylabel("accuracy, % (dashed)", color=ROSE)
    ax2.spines["right"].set_visible(True)
    save(fig, "ch5_bill_steps.png")


def ch5_line_curve():
    ratio = np.logspace(-2, 2, 200)
    fig, ax = plt.subplots(figsize=(11, 4.6))
    ax.plot(ratio, ratio / (1 + ratio), color=VIOLET, lw=3); ax.set_xscale("log")
    spots = ((40 / 1200, "SMS nudge: 0.032", (0.012, 0.22)), (400 / 1200, "Rs 400 hamper: 0.25", (0.6, 0.12)),
             (1.0, "equal costs: 0.5", (2.2, 0.42)), (20, "Rohan's loan: 0.952", (2.0, 0.85)))
    for r, name, at in spots:
        ax.scatter(r, r / (1 + r), color=ROSE, zorder=5, s=70)
        ax.annotate(name, (r, r / (1 + r)), at, fontsize=13, arrowprops={"arrowstyle": "->", "color": MUTED})
    ax.set_xlabel("cost of acting wrongly / cost of failing to act"); ax.set_ylabel("the line")
    save(fig, "ch5_line_curve.png")


def ch6_two_lines():
    fig, ax = plt.subplots(figsize=(13, 2.9))
    ax.plot([0, 1], [0, 0], color=MUTED, lw=8, solid_capstyle="round")
    ax.scatter([0.032], [0], s=420, color=GREEN, zorder=5); ax.annotate("Retail nudges when P(buy) > 0.032", (0.032, 0), (0.0, 0.55), color=GREEN, fontsize=15)
    ax.scatter([0.952], [0], s=420, color=ROSE, zorder=5); ax.annotate("Rohan lends when P(repay) > 0.952", (0.952, 0), (0.5, -0.8), color=ROSE, fontsize=15)
    ax.set_xlim(-0.03, 1.03); ax.set_ylim(-1.1, 1.0); ax.set_yticks([]); ax.set_xlabel("the probability of the good outcome")
    save(fig, "ch6_two_lines.png")


# ---------- case chapters, on the bank's real scores ----------
def case1_matrices(y, p):
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.6))
    for ax, (t, title) in zip(axes, ((1.01, "Call nobody: accuracy 0.887"), (0.5, "Monday's model at 0.5: accuracy 0.897"))):
        tp, fp, fn, tn = cells(y, p, t)
        grid = [[tp, fn], [fp, tn]]; names = [["TP", "FN"], ["FP", "TN"]]; cols = [[GREEN, ROSE], [ROSE, MUTED]]
        for i in range(2):
            for j in range(2):
                ax.add_patch(plt.Rectangle((j, 1 - i), 0.97, 0.97, color=cols[i][j], alpha=0.2 if grid[i][j] else 0.04))
                ax.text(j + 0.48, 1.55 - i, f"{grid[i][j]:,}", ha="center", va="center", fontsize=24, weight="bold", color=INK)
                ax.text(j + 0.48, 1.25 - i, names[i][j], ha="center", va="center", fontsize=15, color=INK)
        ax.set_xlim(0, 2); ax.set_ylim(0, 2); ax.set_xticks([0.5, 1.5]); ax.set_xticklabels(["called", "not called"])
        ax.set_yticks([1.5, 0.5]); ax.set_yticklabels(["bought", "did not"]); ax.tick_params(length=0); ax.set_title(title, color=INK)
    save(fig, "case1_matrices.png")


def case1_humps(y, p, lines=((0.5, "0.5", ROSE),), name="case1_humps.png"):
    fig, ax = plt.subplots(figsize=(13, 5.2))
    bins = np.linspace(0, 1, 51)
    ax.hist(p[y == 0], bins=bins, color=MUTED, alpha=0.55, label="did not buy: 7,310")
    ax.hist(p[y == 1], bins=bins, color=GREEN, alpha=0.85, label="bought: 928")
    for k, (t, lab, c) in enumerate(lines):
        ax.axvline(t, color=c, lw=3); ax.text(t + 0.01, (1500, 300, 1500)[k % 3], lab, color=c, fontsize=15, backgroundcolor="white")
    ax.set_yscale("log"); ax.set_xlabel("the model's P(buy)"); ax.set_ylabel("clients, log scale"); ax.legend(frameon=False)
    save(fig, name)


def case2_bill_curve(y, p):
    grid = np.round(np.arange(0.001, 0.7, 0.001), 3)
    bills = np.array([cells(y, p, t)[1] * 40 + cells(y, p, t)[2] * 1200 for t in grid])
    fig, ax = plt.subplots(figsize=(13, 5.2))
    ax.plot(grid, bills / 1e5, color=VIOLET, lw=3, label="the model's bill")
    ax.axhline(y.sum() * 1200 / 1e5, color=ROSE, ls="--", lw=2, label="call nobody: Rs 11.14 lakh")
    ax.axhline((len(y) - y.sum()) * 40 / 1e5, color=GREEN, ls="--", lw=2, label="call everyone: Rs 2.92 lakh")
    ax.axvline(1 / 31, color=INK, lw=1.5); ax.text(0.04, 9.6, "0.032: Rs 2.79 lakh", color=INK)
    ax.axvline(0.5, color=MUTED, ls=":", lw=1.5); ax.text(0.51, 7.2, "0.5: Rs 9.09 lakh", color=MUTED)
    ax.set_xlabel("threshold on P(buy)"); ax.set_ylabel("bill of mistakes, Rs lakh"); ax.set_xlim(0, 0.7)
    ax.legend(frameon=False, loc=(0.5, 0.25))
    save(fig, "case2_bill_curve.png")


def case2_ratio(y, p):
    ratios = [30, 20, 15, 10, 8, 5, 3, 2]; saving = []
    for r in ratios:
        cfn = 40 * r; t = 40 / (40 + cfn); tp, fp, fn, tn = cells(y, p, t)
        free = min(y.sum() * cfn, (len(y) - y.sum()) * 40); saving.append((free - (fp * 40 + fn * cfn)) / free * 100)
    fig, ax = plt.subplots(figsize=(12, 4.8))
    xs = list(range(len(ratios)))
    ax.plot(xs, saving, "o-", color=VIOLET, lw=3, ms=9)
    for x, s_ in zip(xs, saving):
        ax.text(x, s_ + 2, f"{s_:.1f}%", ha="center", fontsize=13, color=INK)
    ax.set_xticks(xs); ax.set_xticklabels([f"{r}:1" for r in ratios])
    ax.set_xlabel("a missed buyer costs this many wasted nudges"); ax.set_ylabel("saving over the best free rule, %")
    ax.set_ylim(0, 48); ax.annotate("Anand's 30:1", (0, saving[0]), (0.2, 14), color=ROSE, arrowprops={"arrowstyle": "->", "color": ROSE})
    save(fig, "case2_ratio.png")


def case3_prec_at_k(y, p):
    order = np.argsort(-p); ks = np.arange(50, len(y), 25)
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.2))
    axes[0].plot(ks, [y[order[:k]].mean() for k in ks], color=VIOLET, lw=3, label="top k by score")
    axes[0].axhline(y.mean(), color=MUTED, ls="--", lw=2, label="base rate 0.113")
    axes[0].scatter([1000], [y[order[:1000]].mean()], color=ROSE, s=90, zorder=5)
    axes[0].annotate("1,000 calls: 0.404", (1000, 0.404), (2300, 0.52), color=ROSE, arrowprops={"arrowstyle": "->", "color": ROSE})
    axes[0].set_xlabel("calls made, k"); axes[0].set_ylabel("share of calls that buy"); axes[0].legend(frameon=False); axes[0].set_title("Precision at k", color=INK)
    axes[1].plot(np.arange(1, len(y) + 1), np.cumsum(y[order]), color=VIOLET, lw=3, label="model's ranking")
    axes[1].plot([0, len(y)], [0, y.sum()], color=MUTED, ls="--", lw=2, label="random list")
    axes[1].axvline(1000, color=ROSE, lw=2); axes[1].text(2300, 230, "1,000 calls: 404 against 112", color=ROSE)
    axes[1].set_xlabel("calls made"); axes[1].set_ylabel("buyers found"); axes[1].legend(frameon=False, loc="lower right"); axes[1].set_title("Buyers found", color=INK)
    save(fig, "case3_prec_at_k.png")


if __name__ == "__main__":
    roadmap()
    ch1_four_boxes(); ch2_denominators(); ch2_f1(); ch3_dots(); ch3_free_accuracy()
    coins(30, "40", "Rs 1,200", "ch4_coins.png", "30 wasted nudges at Rs 40", "1 buyer's margin")
    ch5_bill_steps(); ch5_line_curve(); ch6_two_lines()
    coins(20, "3k", "Rs 60,000", "ch6_loan_coins.png", "20 good loans' interest at Rs 3,000", "1 default")
    y, p = bank_scores()
    timeline_tuesday(y, p)
    case1_matrices(y, p); case1_humps(y, p)
    case2_bill_curve(y, p); case2_ratio(y, p)
    case1_humps(y, p, ((1 / 31, "cost line 0.032", INK), (0.182, "budget line 0.182", ROSE), (0.5, "0.5", MUTED)), "case_humps_lines.png")
    case3_prec_at_k(y, p)
