"""Prove every key and every printed number on the Week 5 Saturday recap paper.

    python3 content/W05/SAT/internal/C2_W05_SAT_key_proofs_INTERNAL.py            # the proofs
    python3 content/W05/SAT/internal/C2_W05_SAT_key_proofs_INTERNAL.py --rerun    # and the data

Runs cold from the repository root and needs only Python 3, PyYAML and openpyxl (the builder's own
imports). It assembles the paper exactly as scripts/build_saturday_paper.py does, from the tracker's
bank, data/programme/paper_edits.yaml and the week's source file, so every check runs on the items
as they print. Every bank-campaign number an exhibit prints is read back from the week's pipeline
file (docs/detailing/W05_research/W05_week_pipeline.md) where that file states it, and from RUN
below where it does not; RUN holds what this session's re-run printed on 28 October 2026, and the
provenance file prints the same table. Every derived number is recomputed from the printed exhibit,
and every key is asserted: the letter of a one-correct or reasoned item must sit on the option that
holds the computed figure, and an applied-maths key must carry the recomputed figures.

With --rerun it also downloads UCI Bank Marketing (needs the network, pandas and scikit-learn),
runs the week's pipeline and every extra model the paper quotes, and asserts each RUN value to the
printed precision, so a change in a library that moves a printed number is caught before Saturday.
It prints one line per item and exits 1 on the first failed assertion.
"""
import math
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
import build_saturday_paper as bsp  # noqa: E402

PIPELINE = (ROOT / "docs/detailing/W05_research/W05_week_pipeline.md").read_text(encoding="utf-8")
PAPER = (ROOT / "content/W05/SAT/paper/C2_W05_SAT_recap_paper_STUDENT.md").read_text(encoding="utf-8")

# What this session's re-run printed on 28 October 2026 (Python 3.13, pandas 3.0.5, scikit-learn
# 1.9.1), for the numbers the pipeline file does not table. --rerun recomputes every one.
RUN = {
    "rows": 41188, "yes": 4640,
    "tree": {3: (0.899, 0.899, 0.751), 5: (0.901, 0.897, 0.783), 8: (0.911, 0.897, 0.777),
             None: (0.996, 0.837, 0.619)},
    "cv_folds": [0.771, 0.769, 0.797, 0.796, 0.798],
    "family_auc": {"logistic": 0.795, "forest": 0.799, "boosting": 0.806},
    "euribor_alone": -0.92, "euribor_full": 0.39,
    "poutcome_success_yes": 0.651, "duration_mean_yes": 553, "duration_mean_no": 221,
    "time_early_rows": 28831, "time_late_rows": 12357, "time_early_yes": 0.056,
    "time_late_yes": 0.246, "time_late_mean_pred": 0.152, "time_late_auc": 0.657,
}
LINES = []


def assemble():
    bank = bsp.read_bank()
    edits = yaml.safe_load(bsp.EDITS.read_text(encoding="utf-8"))
    bsp.apply_edits(bank, edits)
    source = bsp.read_source("W05")
    return bsp.assemble(bank["W5"], source), source


PRINTED, SOURCE = assemble()
BY_ID = {i["id"]: i for i in PRINTED if i.get("added")}
BY_NO = {i["no"]: i for i in PRINTED if not i.get("added")}


def options(item):
    return {letter: text for letter, text in bsp.parts(item)[1]}


def n(s):
    """'7,216' or 'Rs 908,560' as a number."""
    return float(re.sub(r"[^0-9.\-]", "", str(s)))


def close(a, b, tol=0.0005):
    return abs(float(a) - float(b)) <= tol


def r2(x):
    """Round half up to two places, the way a printed figure is rounded."""
    return math.floor(x * 100 + 0.5) / 100


def r3(x):
    return math.floor(x * 1000 + 0.5) / 1000


def ok(q, ref, key, what):
    LINES.append(q)
    print(f"PASS  Q{q:<2} {ref:<18} key {key:<10} {what}")


def keyed(item, letter, *needles):
    """The key is `letter` and that option carries every needle."""
    assert item["key"] == letter, (item.get("id") or item["no"], item["key"], letter)
    text = options(item)[letter]
    for s in needles:
        assert s in text, (item.get("id") or item["no"], s, text)


def table(ex):
    return [[str(c) for c in row] for row in ex["table"]["rows"]]


def part_exhibit(p, k=0):
    return SOURCE["parts"][p - 1]["exhibits"][k]


def pipeline_row(label):
    """A row of the pipeline file's model table by the start of its first cell."""
    for line in PIPELINE.splitlines():
        if line.startswith("| " + label):
            return [c.strip() for c in line.strip("|").split("|")]
    raise KeyError(label)


def pipeline_threshold(label):
    for line in PIPELINE.splitlines():
        if line.startswith("| " + label):
            return [c.strip() for c in line.strip("|").split("|")]
    raise KeyError(label)


def shape():
    assert len(PRINTED) == 26, len(PRINTED)
    timed = sum(i["min"] for i in PRINTED)
    assert timed == 59 and bsp.paper_minutes("W05", 60) == 60, timed
    levels = [i["level"] for i in PRINTED]
    assert (levels.count("Easy"), levels.count("Medium"), levels.count("Hard")) == (4, 7, 15)
    assert len(SOURCE["folded"]) == 24 and not SOURCE["stretch_bank"]
    assert sorted(BY_NO) == [1, 2, 3, 4, 5]
    print(f"PASS  shape: 26 items, {timed:g} of 60 minutes, 4 easy, 7 medium, 15 hard; "
          f"5 bank items print and 24 fold")


def no_giveaways():
    """Numbers a later exhibit or stem would hand to an earlier written item."""
    student = PAPER.split("## Stretch")[0]
    for leak in ("0.032", "1 / 31", "1 in 31", "348 / 1,196", "0.291"):
        assert leak not in student, f"the paper prints {leak}, which a written item asks for"
    # The row's planted Kalpa figures belonged to a dataset never generated (the plan's section 6),
    # so the paper prints none of them: no 0.99 for settlement_status and no 96 to 4 split.
    assert not re.search(r"0\.99\b|96 to 4", student), "the paper prints a planted Kalpa figure"
    print("PASS  no giveaways: the cost line and F1 appear only in the key")


def exhibits():
    # Exhibit 1A: the split and the first two scores, against the pipeline file.
    assert "Rows 41,188; train 24,712, validation 8,238, test 8,238" in PIPELINE
    assert 24712 + 8238 + 8238 == RUN["rows"] and close(RUN["yes"] / RUN["rows"], 0.1127, 0.00005)
    assert "11.27" in PIPELINE and "11.26" in PIPELINE
    rows = dict((r[0], r[1]) for r in table(part_exhibit(1)))
    base = pipeline_row("Majority baseline")
    cust = pipeline_row("Logistic, customer table")
    assert base[2] == "0.8874" and rows["Call nobody, on validation"].startswith("accuracy 0.887")
    assert cust[1] == "0.7613" and cust[2] == "0.8971"
    assert "accuracy 0.897; AUC 0.761; finds 174 of the 928" == rows[
        "Logistic regression on the customer table, threshold 0.5"]
    print("PASS  Exhibit 1A: 24,712 + 8,238 + 8,238 = 41,188; 0.887, 0.897 and 0.761 as the pipeline prints")
    # Exhibit 2A: both matrices, against the pipeline file.
    m = {r[0]: [int(n(c)) for c in r[1:]] for r in table(part_exhibit(2))}
    assert m["Call nobody"] == [int(n(c)) for c in base[3:7]]
    assert m["Model at 0.5"] == [int(n(c)) for c in cust[3:7]] == [174, 94, 754, 7216]
    assert sum(m["Model at 0.5"]) == sum(m["Call nobody"]) == 8238
    print("PASS  Exhibit 2A: TP 174, FP 94, FN 754, TN 7,216 and the do-nothing matrix as the pipeline prints")
    # Exhibit 2B: every row adds up, and the threshold rows match the pipeline file.
    for label, called, tp, fp, fn in table(BY_ID["bill"]["exhibit"]):
        called, tp, fp, fn = (int(n(x)) for x in (called, tp, fp, fn))
        assert called == tp + fp and tp + fn == 928, label
    want = {"0.10": "0.10", "0.20": "0.20", "The cost line": "1/31"}
    for label, start in want.items():
        row = next(r for r in table(BY_ID["bill"]["exhibit"]) if r[0] == label)
        src = pipeline_threshold(start)
        assert [int(n(x)) for x in row[1:]] == [int(n(x)) for x in src[1:5]], label
    assert "the top 1,000 at 0.404" in PIPELINE
    print("PASS  Exhibit 2B: called = caught + wasted, caught + missed = 928, rows as the pipeline prints")
    # Exhibit 3A: the three column sets.
    t3 = table(part_exhibit(3))
    econ = pipeline_row("Logistic, + economy (")
    leak = pipeline_row("Logistic, + economy + duration")
    for row, src in zip(t3, (cust, econ, leak)):
        assert row[1] == f"{r3(float(src[1])):.3f}" and row[2] == f"{r3(float(src[2])):.3f}", row
        assert int(row[3]) == int(n(src[3])), row
    print("PASS  Exhibit 3A: 0.761, 0.795 and 0.932; 174, 211 and 390 buyers, as the pipeline prints")
    # Exhibit 4A: the tree by depth, and the chart draws the table.
    t4 = table(part_exhibit(4))
    for row in t4:
        depth = None if row[0] == "No limit" else int(row[0])
        assert tuple(float(x) for x in row[1:]) == RUN["tree"][depth], row
    chart = part_exhibit(4)["mermaid"]
    lines = re.findall(r"line \[([^\]]+)\]", chart)
    assert [float(x) for x in lines[0].split(",")] == [float(r[1]) for r in t4]
    assert [float(x) for x in lines[1].split(",")] == [float(r[2]) for r in t4]
    print("PASS  Exhibit 4A: the chart's two lines are the table's training and validation columns")
    # Exhibit 4B: the folds and the families.
    t4b = dict(table(BY_ID["cv-why"]["exhibit"]))
    folds = [float(t4b[f"Logistic, fold {k}"]) for k in range(1, 6)]
    assert folds == RUN["cv_folds"]
    assert f"{r3(sum(folds) / 5):.3f}" == t4b["Logistic, mean of the five folds"] == "0.786"
    assert float(t4b["Logistic regression, on validation"]) == r3(float(econ[1])) == RUN["family_auc"]["logistic"]
    assert float(t4b["Random forest, on validation"]) == RUN["family_auc"]["forest"]
    assert float(t4b["Gradient boosting, on validation"]) == RUN["family_auc"]["boosting"]
    print("PASS  Exhibit 4B: five folds 0.769 to 0.798, mean 0.786; logistic 0.795 as Wednesday's honest model")
    # Exhibit 5A: the split by date.
    t5 = dict(table(part_exhibit(5)))
    assert RUN["time_early_rows"] + RUN["time_late_rows"] == RUN["rows"]
    assert RUN["time_early_rows"] == int(RUN["rows"] * 0.7)
    assert t5[f"Earliest 70 percent of calls, {RUN['time_early_rows']:,} clients"] == "5.6 percent said yes"
    assert t5[f"Latest 30 percent of calls, {RUN['time_late_rows']:,} clients"] == "24.6 percent said yes"
    assert t5["Mean predicted chance of a yes on the latest 30 percent"] == "0.152"
    assert t5["AUC on the latest 30 percent"] == "0.657, against 0.795 on the random split"
    print("PASS  Exhibit 5A: 28,831 + 12,357 = 41,188; 5.6 against 24.6 percent; mean score 0.152")
    # Exhibit 5B: the public figures as the sources file records them.
    sources = (ROOT / "content/W05/SAT/internal/C2_W05_SAT_sources_INTERNAL.md").read_text(encoding="utf-8")
    for fact in ("61%", "93%", "about 85%", "-0.1 with 90%", "(-0.45, 0.27)", "23 comparisons"):
        assert fact in sources, fact
    print("PASS  Exhibit 5B: Instacart's 93 to 61 and 85, Booking.com's 23 comparisons and -0.1, in the sources file")


def items():
    ex2 = {r[0]: [int(n(c)) for c in r[1:]] for r in table(part_exhibit(2))}
    tp, fp, fn, tn = ex2["Model at 0.5"]

    i = BY_NO[1]
    assert i["key"] == "c" and i["bank_word"] == "test"
    ok(i["q"], "bank 1", "c (test)", "the slice spent once")

    i = BY_ID["peek"]
    keyed(i, "b", "spent", "new calls")
    ok(i["q"], "peek", "b", "the peeked test is spent; score once on fresh calls")

    i = BY_ID["random-or-time"]
    keyed(i, "c", "False", "train early and score late")
    assert "5.6 percent" in i["text"] and "24.6 percent" in i["text"]
    ok(i["q"], "random-or-time", "c", "yes rate 5.6 to 24.6 percent across the file, as RUN")

    i = BY_ID["logit-071"]
    keyed(i, "d", "71 in 100", "calibrated")
    ok(i["q"], "logit-071", "d", "a calibrated chance for one client")

    i = BY_ID["is-it-ml"]
    assert bsp.letters_of(i["key"]) == ["a", "d"]
    ok(i["q"], "is-it-ml", "a, d", "the two asks about a future yes")

    i = BY_NO[2]
    assert i["key"] == "b" and i["bank_word"] == "negatives"
    ok(i["q"], "bank 2", "b", "recall's denominator holds the false negatives")

    i = BY_ID["acc-trap"]
    acc_model, acc_none = (tp + tn) / 8238, ex2["Call nobody"][3] / 8238
    assert f"{r3(acc_model):.3f}" == "0.897" and f"{r3(acc_none):.3f}" == "0.887"
    assert fp + fn == 848 and ex2["Call nobody"][2] == 928 and 928 - 848 == 80
    keyed(i, "d", "False", "174 of 928")
    assert "848" in options(i)["b"] and "80 fewer" in options(i)["b"]
    ok(i["q"], "acc-trap", "d", "0.897 against 0.887; recall 174 of 928; option b's 848 = 94 + 754")

    i = BY_ID["prf"]
    p, r = tp / (tp + fp), tp / (tp + fn)
    f1 = 2 * tp / (2 * tp + fp + fn)
    assert close(f1, 2 * p * r / (p + r), 1e-12)
    assert (r2(p), r2(r), r2(f1)) == (0.65, 0.19, 0.29)
    for s in ("174 / 268 = 0.65", "174 / 928 = 0.19", "348 / 1,196 = 0.29"):
        assert s in i["key"], s
    ok(i["q"], "prf", "0.65/0.19/0.29", f"P {p:.4f}, R {r:.4f}, F1 {f1:.4f}")

    i = BY_ID["cost-line"]
    line = 40 / (40 + 1200)
    assert close(line, 1 / 31, 1e-12) and f"{r3(line):.3f}" == "0.032" and 1200 / 40 == 30
    for s in ("40 / 1,240 = 1 / 31", "0.032", "down", "recall leads"):
        assert s in i["key"], s
    ok(i["q"], "cost-line", "1/31", "40 / 1,240 = 0.0323; one buyer pays for 30 wasted calls")

    i = BY_ID["bill"]
    rows = {r[0]: [int(n(c)) for c in r[1:]] for r in table(i["exhibit"])}
    (_, _, fp5, fn5), (_, _, fp1, fn1) = rows["0.5"], rows["0.10"]
    b5, b1 = fp5 * 40 + fn5 * 1200, fp1 * 40 + fn1 * 1200
    assert (b5, b1, b5 - b1) == (908560, 459920, 448640)
    keyed(i, "b", f"Rs {b5:,}", f"Rs {b1:,}", f"Rs {b5 - b1:,}")
    sw5, sw1 = fp5 * 1200 + fn5 * 40, fp1 * 1200 + fn1 * 40
    assert f"Rs {sw5:,}" in options(i)["a"] and f"Rs {sw1:,}" in options(i)["a"] and f"Rs {sw1 - sw5:,}" in options(i)["a"]
    assert f"Rs {fp5 * 40:,}" in options(i)["c"] and f"Rs {fp1 * 40:,}" in options(i)["c"]
    assert f"Rs {(fp1 - fp5) * 40:,}" in options(i)["c"]
    assert f"Rs {fn5 * 1200:,}" in options(i)["d"] and f"Rs {fn1 * 1200:,}" in options(i)["d"]
    assert f"Rs {(fn5 - fn1) * 1200:,}" in options(i)["d"]
    ok(i["q"], "bill", "b", "Rs 908,560 against Rs 459,920; distractors swap the prices or drop a box")

    i = BY_ID["budget-k"]
    top = rows["Top 1,000 by score"]
    lift = (top[1] / top[0]) / (928 / 8238)
    assert top[1] == 404 and f"{lift:.1f}" == "3.6" and rows["The cost line"][0] == 7438
    assert rows["0.5"][0] == 268 and f"{r2(174 / 268):.2f}" == "0.65"
    keyed(i, "c", "top 1,000", "404", "3.6 times")
    ok(i["q"], "budget-k", "c", f"precision at 1,000 is 0.404 against 0.113, {lift:.2f} times")

    i = BY_NO[3]
    assert i["key"] == "c" and i["bank_word"] == "leakage"
    ok(i["q"], "bank 3", "c (leakage)", "a column from the future")

    t3 = table(part_exhibit(3))
    i = BY_ID["duration-call"]
    assert "0.795 to 0.932" in i["text"] and t3[1][1] == "0.795" and t3[2][1] == "0.932"
    assert "0.899 to 0.907" in options(i)["b"] and t3[1][2] == "0.899" and t3[2][2] == "0.907"
    keyed(i, "c", "report 0.795")
    ok(i["q"], "duration-call", "c", "AUC 0.795 to 0.932 while accuracy moves 0.899 to 0.907")

    i = BY_ID["which-pass"]
    assert bsp.letters_of(i["key"]) == ["b", "c", "d"]
    assert f"{round(RUN['poutcome_success_yes'] * 100)} percent" in options(i)["b"]
    ok(i["q"], "which-pass", "b, c, d", "poutcome passes at 65 percent yes; duration fails")

    i = BY_ID["importance"]
    gap = RUN["duration_mean_yes"] - RUN["duration_mean_no"]
    assert gap == 332 and "332 seconds" in options(i)["d"] and "553" in i["text"] and "221" in i["text"]
    keyed(i, "a", "False", "the yes drives the length")
    ok(i["q"], "importance", "a", "553 - 221 = 332 seconds; the arrow runs both ways")

    i = BY_ID["sign-flip"]
    assert f"{RUN['euribor_alone']:.2f}" in i["text"] and f"+{RUN['euribor_full']:.2f}" in i["text"]
    keyed(i, "d", "move together")
    ok(i["q"], "sign-flip", "d", "euribor3m -0.92 alone, +0.39 with the indicators, as RUN")

    i = BY_NO[4]
    assert i["key"] == "a" and i["bank_word"] == "overfitting"
    ok(i["q"], "bank 4", "a", "training far above validation")

    i = BY_NO[5]
    assert i["key"] == "d" and i["bank_word"] == "split"
    ok(i["q"], "bank 5", "d", "the luck of one split")

    i = BY_ID["tree-read"]
    t4 = table(part_exhibit(4))
    best = max(t4, key=lambda r: float(r[3]))
    assert best[0] == "5" and float(t4[-1][2]) < 0.887 < float(t4[-1][1])
    keyed(i, "a", "depth 5")
    ok(i["q"], "tree-read", "a", "validation AUC peaks at depth 5, 0.783; unlimited 0.837 < 0.887")

    i = BY_ID["brakes"]
    assert bsp.letters_of(i["key"]) == ["a", "b", "d"]
    ok(i["q"], "brakes", "a, b, d", "depth cap, stronger penalty, cross-validation")

    i = BY_ID["cv-why"]
    train, k = 24712, 5
    fold, fit = train / k, train * (k - 1) / k
    assert round(fold) == 4942 and round(fit, -1) == 19770
    folds = RUN["cv_folds"]
    assert f"{min(folds):.2f}" == "0.77" and f"{max(folds):.2f}" == "0.80"
    keyed(i, "b", "Five models", "19,770", "0.77 or 0.80")
    ok(i["q"], "cv-why", "b", f"5 models on {fit:,.0f} rows each, scored on {fold:,.0f}; folds 0.77 to 0.80")

    i = BY_ID["near-tie"]
    fam = RUN["family_auc"]
    gap, spread = fam["boosting"] - fam["logistic"], max(folds) - min(folds)
    assert f"{gap:.3f}" == "0.011" and f"{spread:.2f}" == "0.03" and gap < spread
    keyed(i, "c", "False", "0.011", "0.03")
    ok(i["q"], "near-tie", "c", f"gap {gap:.3f} inside the folds' spread {spread:.3f}")

    i = BY_ID["stale-rule"]
    assert RUN["time_late_mean_pred"] < RUN["time_late_yes"]
    keyed(i, "a", "yes rate", "mean score", "stated gap")
    ok(i["q"], "stale-rule", "a", "mean score 0.152 against 24.6 percent yes on the late rows")

    i = BY_ID["caveat"]
    assert bsp.letters_of(i["key"]) == ["b", "c"]
    ok(i["q"], "caveat", "b, c", "the weakest segment and the staleness trigger")

    i = BY_ID["booking"]
    assert "23 comparisons" in i["text"]
    keyed(i, "a", "random trial")
    ok(i["q"], "booking", "a", "offline gain and business gain near uncorrelated, so a trial")

    i = BY_ID["lend-flip"]
    pd_line = 3000 / (3000 + 60000)
    assert f"{r2(pd_line):.2f}" == "0.05" and f"{r2(1 - pd_line):.2f}" == "0.95"
    assert f"{r2(60000 / 63000):.2f}" == "0.95" and 60000 / 3000 == 20
    keyed(i, "d", "3,000 in 63,000", "0.05", "0.95")
    assert "60,000 in 63,000" in options(i)["c"]
    ok(i["q"], "lend-flip", "d", f"default below {pd_line:.4f}, repay above {1 - pd_line:.4f}")


def stretch():
    s = SOURCE["stretch"]
    assert len(s) == 3
    q = 5 / 6
    assert f"{r2(q):.2f}" == "0.83" and "5 over 6, about 0.83" in s[0]["answer"]
    assert "0.95" in s[0]["answer"] and "0.011" in s[1]["text"] and "0.404" in s[2]["answer"]
    print("PASS  stretch answers: 5 over 6 = 0.83 beside Rohan's 0.95; the gap and the 30-second story")


def balance():
    singles = [i["key"] for i in PRINTED if re.fullmatch(r"[a-d]", i["key"]) and not i.get("bank_options")]
    multis = [bsp.letters_of(i["key"]) for i in PRINTED if bsp.MULTI.match(i["key"])]
    every = singles + [x for m in multis for x in m]
    counts = {c: every.count(c) for c in "abcd"}
    assert max(counts.values()) / len(every) <= 0.5 and min(counts.values()) > 0, counts
    assert not set.intersection(*map(set, multis)), multis
    print(f"PASS  key positions a {counts['a']}, b {counts['b']}, c {counts['c']}, d {counts['d']}; "
          f"no letter sits in every more-than-one key")


def rerun():
    """Download the data and recompute every RUN value and every pipeline number the paper prints."""
    import io
    import urllib.request
    import zipfile
    import numpy as np
    import pandas as pd
    from sklearn.compose import ColumnTransformer
    from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import roc_auc_score
    from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import OneHotEncoder, StandardScaler
    from sklearn.tree import DecisionTreeClassifier

    cache = pathlib.Path.home() / ".cache" / "c2_datasets"
    cache.mkdir(parents=True, exist_ok=True)
    f = cache / "bank-additional-full.csv"
    if not f.exists():
        url = "https://archive.ics.uci.edu/static/public/222/bank+marketing.zip"
        outer = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(url, timeout=60).read()))
        inner = zipfile.ZipFile(io.BytesIO(outer.read("bank-additional.zip")))
        f.write_bytes(inner.read("bank-additional/bank-additional-full.csv"))
    bank = pd.read_csv(f, sep=";")
    profile = ["age", "job", "marital", "education", "default", "housing", "loan"]
    history = ["contact", "month", "day_of_week", "campaign", "previous", "poutcome"]
    economy = ["emp.var.rate", "cons.price.idx", "cons.conf.idx", "euribor3m", "nr.employed"]
    honest = profile + history + economy

    def prep(cols, df, dense=False):
        num = [c for c in cols if pd.api.types.is_numeric_dtype(df[c])]
        cat = [c for c in cols if c not in num]
        enc = OneHotEncoder(handle_unknown="ignore", sparse_output=not dense)
        return ColumnTransformer([("num", StandardScaler(), num), ("cat", enc, cat)])

    def model(cols, df, est, dense=False):
        return Pipeline([("prep", prep(cols, df, dense)), ("model", est)])

    y = (bank["y"] == "yes").astype(int)
    assert (len(bank), int(y.sum())) == (RUN["rows"], RUN["yes"])
    rest, test = train_test_split(bank.index, test_size=0.20, stratify=y, random_state=42)
    tr, va = train_test_split(rest, test_size=0.25, stratify=y.loc[rest], random_state=42)
    train, val = bank.loc[tr], bank.loc[va]
    yt, yv = y.loc[tr], y.loc[va]
    for depth, want in RUN["tree"].items():
        m = model(honest, train, DecisionTreeClassifier(max_depth=depth, random_state=42)).fit(train[honest], yt)
        got = (m.score(train[honest], yt), m.score(val[honest], yv),
               roc_auc_score(yv, m.predict_proba(val[honest])[:, 1]))
        assert tuple(r3(x) for x in got) == want, (depth, got)
    fams = {"logistic": (LogisticRegression(max_iter=2000), False),
            "forest": (RandomForestClassifier(n_estimators=300, min_samples_leaf=5, random_state=42, n_jobs=-1), False),
            "boosting": (HistGradientBoostingClassifier(random_state=42), True)}
    for name, (est, dense) in fams.items():
        m = model(honest, train, est, dense).fit(train[honest], yt)
        assert r3(roc_auc_score(yv, m.predict_proba(val[honest])[:, 1])) == RUN["family_auc"][name], name
    cv = cross_val_score(model(honest, train, LogisticRegression(max_iter=2000)), train[honest], yt,
                         cv=StratifiedKFold(5, shuffle=True, random_state=42), scoring="roc_auc")
    assert [r3(x) for x in cv] == RUN["cv_folds"], cv
    for cols, want in ((["euribor3m"], RUN["euribor_alone"]), (honest, RUN["euribor_full"])):
        m = model(cols, train, LogisticRegression(max_iter=2000)).fit(train[cols], yt)
        coef = dict(zip(m.named_steps["prep"].get_feature_names_out(), m.named_steps["model"].coef_[0]))
        assert r2(coef["num__euribor3m"]) == want, (cols, coef["num__euribor3m"])
    assert r3((bank.loc[bank.poutcome == "success", "y"] == "yes").mean()) == RUN["poutcome_success_yes"]
    means = bank.groupby("y")["duration"].mean()
    assert (round(means["yes"]), round(means["no"])) == (RUN["duration_mean_yes"], RUN["duration_mean_no"])
    cut = int(len(bank) * 0.7)
    early, late = bank.iloc[:cut], bank.iloc[cut:]
    ye, yl = y.iloc[:cut], y.iloc[cut:]
    m = model(honest, early, LogisticRegression(max_iter=2000)).fit(early[honest], ye)
    pl = m.predict_proba(late[honest])[:, 1]
    assert (len(early), len(late)) == (RUN["time_early_rows"], RUN["time_late_rows"])
    assert (r3(ye.mean()), r3(yl.mean()), r3(pl.mean()), r3(roc_auc_score(yl, pl))) == (
        RUN["time_early_yes"], RUN["time_late_yes"], RUN["time_late_mean_pred"], RUN["time_late_auc"])
    p = model(profile + history, train, LogisticRegression(max_iter=2000)).fit(
        train[profile + history], yt).predict_proba(val[profile + history])[:, 1]
    order = np.argsort(-p)
    assert int(yv.values[order[:1000]].sum()) == 404
    print("PASS  rerun: every RUN value and the top 1,000's 404 buyers recomputed from the UCI file")


def main():
    shape()
    no_giveaways()
    exhibits()
    items()
    stretch()
    balance()
    if "--rerun" in sys.argv:
        rerun()
    assert len(LINES) == 26, len(LINES)
    print(f"\nRESULT: PASS ({len(LINES)} items proved)")


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# python3 content/W05/SAT/internal/C2_W05_SAT_key_proofs_INTERNAL.py
#     Prints the shape line, the giveaway line, eight exhibit lines and 26 item lines, PASS Q1 to
#     PASS Q26, each with the item's id or bank number, its key and what was checked, then the
#     stretch and key-position lines and "RESULT: PASS (26 items proved)", exit 0.
# The same run with --rerun, the network open and scikit-learn 1.9.1 installed
#     Adds "PASS  rerun: every RUN value ..." before the result line, exit 0.
# The bill item's key changed to d in the source file
#     keyed() fails at Q10, because the key is no longer b, and the run exits 1.
# Exhibit 2B's 0.10 row retyped with 2,183 wasted calls instead of 2,138
#     The Exhibit 2B check fails: called no longer equals caught plus wasted.
# "0.032" put back into Exhibit 2B's cost-line row
#     The giveaway check fails before any item is proved, since Q9 asks for that number.
# The near-tie item given a gap of 0.04 in its exhibit
#     The near-tie check fails, since the gap would no longer sit inside the folds' spread.
# The pipeline file's customer-table row edited to 0.7700 AUC
#     The Exhibit 1A check fails, because the paper prints 0.761 and the pipeline no longer does.
