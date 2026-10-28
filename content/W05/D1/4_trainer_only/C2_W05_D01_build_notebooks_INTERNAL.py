"""Write and execute every notebook of the W05 D1 pack from the cell lists below.

Usage:
    python3 content/W05/D1/4_trainer_only/C2_W05_D01_build_notebooks_INTERNAL.py

Each notebook is written as JSON and executed in its own folder with
`jupyter nbconvert --to notebook --execute --inplace`, so it ships with its outputs. The public
datasets are cached in ~/.cache/c2_datasets; nothing else is written outside the day folder. The
practice lab's SQL step runs on Postgres when a server answers and on SQLite in memory otherwise.
"""

import json, pathlib, subprocess, sys

def make(path, cells, execute=True):
    nb = {"cells": [], "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
          "language_info": {"name": "python"}}, "nbformat": 4, "nbformat_minor": 5}
    for i, c in enumerate(cells):
        kind = "markdown" if c.startswith("md:") else "code"
        src = c[3:].strip("\n") if kind == "markdown" else c.strip("\n")
        cell = {"cell_type": kind, "id": f"c{i:02d}", "metadata": {}, "source": src.splitlines(keepends=True)}
        if kind == "code":
            cell["outputs"] = []; cell["execution_count"] = None
        nb["cells"].append(cell)
    path = pathlib.Path(path)
    path.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    if execute:
        r = subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--execute", "--inplace", str(path)],
                           capture_output=True, text=True, cwd=str(path.parent))
        if r.returncode:
            print(r.stderr[-3000:]); sys.exit(1)
        out = json.loads(path.read_text())
        for c in out["cells"]:
            for o in c.get("outputs", []):
                t = "".join(o.get("text", [])) if "text" in o else ""
                if t: print(t.rstrip()[:1500])
                if o.get("output_type") == "error": print("ERROR", o.get("ename"), o.get("evalue"))
        print("OK", path.name)

SETUP = '''# Tools for this notebook, and one helper that prints a check as PASS or FAIL.
import io, zipfile, pathlib, urllib.request
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
plt.rcParams.update({"figure.dpi": 110, "font.size": 11, "axes.spines.top": False, "axes.spines.right": False})

def check(label, ok):
    print(("PASS  " if ok else "FAIL  ") + label)

print("ready: pandas", pd.__version__, "and matplotlib", plt.matplotlib.__version__)
'''

BANK = '''# Load the day's public dataset once; later runs read the cached copy.
CACHE = pathlib.Path.home() / ".cache" / "c2_datasets"
CACHE.mkdir(parents=True, exist_ok=True)

def load_bank():
    """UCI Bank Marketing, bank-additional-full.csv (CC BY 4.0), cached after the first download."""
    f = CACHE / "bank-additional-full.csv"
    if not f.exists():
        url = "https://archive.ics.uci.edu/static/public/222/bank+marketing.zip"  # verified 28 October 2026
        outer = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(url, timeout=60).read()))
        inner = zipfile.ZipFile(io.BytesIO(outer.read("bank-additional.zip")))
        f.write_bytes(inner.read("bank-additional/bank-additional-full.csv"))
    return pd.read_csv(f, sep=";")

bank = load_bank()
print(bank.shape)
'''

PIPE = '''# The week's pipeline: the same columns, the same split and the same model every day.
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# The customer table on the morning of the call: who the client is and how earlier campaigns went.
PROFILE = ["age", "job", "marital", "education", "default", "housing", "loan"]
HISTORY = ["contact", "month", "day_of_week", "campaign", "previous", "poutcome"]
COLUMNS = PROFILE + HISTORY

def week_split(df, seed=42):
    """Test is sealed first (20 percent, the envelope); the rest splits 75/25 into train and validation."""
    y = (df["y"] == "yes").astype(int)
    rest, test = train_test_split(df.index, test_size=0.20, stratify=y, random_state=seed)
    train, val = train_test_split(rest, test_size=0.25, stratify=y.loc[rest], random_state=seed)
    return df.loc[train], df.loc[val], df.loc[test]

def logistic(columns, df):
    # pandas 3 reads text as the "str" dtype, so test for numbers rather than for object.
    num = [c for c in columns if pd.api.types.is_numeric_dtype(df[c])]
    cat = [c for c in columns if c not in num]
    prep = ColumnTransformer([("num", StandardScaler(), num),
                              ("cat", OneHotEncoder(handle_unknown="ignore"), cat)])
    return Pipeline([("prep", prep), ("model", LogisticRegression(max_iter=2000))])
'''

DAY = pathlib.Path(__file__).resolve().parent.parent



# ---------------------------------------------------------------- ch123
NB = str(DAY / "1_in_class_training_content" / "notebooks") + "/"
ch1 = [
r'''md:# Chapter 1. Is this an ML problem at all?

*Prediction, rule or query: when a business question is a modelling problem.*

Marketing walks in with a list of questions and the word "AI" on every one of them. Some need a model; most need a query or a rule, which are cheaper, faster and easier to explain. This chapter sorts six of Kalpa's questions, all invented for teaching, with three tests you can run in your head.

By the end you can say, for any business question, whether it is a query, a rule or a prediction, and for a prediction, whether it asks "how much" (regression) or "will they" (classification).

**Search terms:** when to use machine learning, ML problem framing, rules versus machine learning, regression versus classification.''',
SETUP,
r'''md:## Six questions from Kalpa, invented for teaching

**Predict before you run.** How many of the six need a trained model? (a) all six (b) four (c) two (d) none''',
r'''# Six of Kalpa's questions (invented), with the three facts that decide each one.
qs = pd.DataFrame([
    ("How many members bought in September?",                         True,  False, False),
    ("Which members will buy again in the next 90 days?",              False, False, True),
    ("Remind every member whose cart was abandoned yesterday",         False, True,  False),
    ("What was the average basket in Pune last quarter?",              True,  False, False),
    ("How much will each member spend next quarter?",                  False, False, True),
    ("Hold any order above Rs 50,000 from a member who joined this week", False, True, False),
], columns=["question", "answer_already_in_data", "condition_known", "target_later_and_decision_moves"])
print(qs.to_string(index=False))''',
r'''md:## The three tests, in order

1. **Is the answer already sitting in the data?** Then it is a **query**: count, sum or average what happened.
2. **Can someone write the decision down as a condition?** Then it is a **rule**: an if-then that needs no learning.
3. **Otherwise, are all three present:** an input known now, a target known only later, and a decision that changes with the score? Then it is a **prediction**, and a model earns its place.''',
r'''# Run the three tests in order, then split predictions into "how much" and "will they".
def kind(row):
    if row.answer_already_in_data:
        return "query"
    if row.condition_known:
        return "rule"
    if row.target_later_and_decision_moves:
        return "prediction"
    return "not yet framed"

qs["kind"] = qs.apply(kind, axis=1)
qs["family"] = np.where(qs["kind"] != "prediction", "",
                        np.where(qs["question"].str.startswith("How much"), "regression: how much", "classification: will they"))
print(qs[["question", "kind", "family"]].to_string(index=False))
check("two queries, two rules, two predictions", qs["kind"].value_counts().to_dict() == {"query": 2, "rule": 2, "prediction": 2})
check("every question got a kind", (qs["kind"] != "not yet framed").all())''',
r'''md:**What happened.** The answer is (c): only two of the six need a model. The 90-day repeat question is classification (will they), and next-quarter spend is regression (how much). The two counts are queries, and the reminder and the order hold are rules.''',
r'''# Draw the sorting as a picture: three tests, three answers.
fig, ax = plt.subplots(figsize=(10, 3.6)); ax.axis("off")
boxes = [(0.02, "Answer already\nin the data?"), (0.36, "Decision written\nas a condition?"), (0.70, "Input now, target later,\ndecision moves?")]
for x, t in boxes:
    ax.add_patch(plt.Rectangle((x, 0.55), 0.26, 0.3, fc="#EEEAFB", ec="#5B3FD6", lw=2))
    ax.text(x + 0.13, 0.70, t, ha="center", va="center", fontsize=11)
for x, t, c in [(0.02, "QUERY\n2 of 6", "#9A968C"), (0.36, "RULE\n2 of 6", "#C98A00"), (0.70, "PREDICTION\n2 of 6", "#5B3FD6")]:
    ax.text(x + 0.13, 0.22, t, ha="center", va="center", fontsize=12, color="white", fontweight="bold",
            bbox=dict(boxstyle="round", fc=c, ec=c))
    ax.annotate("", xy=(x + 0.13, 0.33), xytext=(x + 0.13, 0.55), arrowprops=dict(arrowstyle="->"))
for x in (0.28, 0.62):
    ax.annotate("", xy=(x + 0.08, 0.70), xytext=(x, 0.70), arrowprops=dict(arrowstyle="->"))
    ax.text(x + 0.04, 0.76, "no", ha="center", fontsize=10)
ax.set_title("Ask the three tests in order; only the last answer needs a model", fontsize=12)
plt.show()''',
r'''md:## When does a rule stop being enough?

Google's Rules of Machine Learning open with "Don't be afraid to launch a product without machine learning" and estimate that a heuristic gets you about half of the gain a model would (developers.google.com/machine-learning/guides/rules-of-ml, verified 28 October 2026). A rule stays the right answer until the business can name what it leaves on the table: members the rule nudges who were going to buy anyway, or members it misses who would have bought with a nudge.

**The flip.** "Use a rule" holds while the rule's misses are cheap. Once a missed repeat buyer costs Rs 1,200 of margin against a Rs 40 nudge (the row's invented numbers), a score that ranks members starts paying for itself, and the question becomes a prediction.

**Uber, for the interview.** Uber's DeepETA post (uber.com/blog/deepeta-how-uber-predicts-arrival-times, verified 28 October 2026) frames arrival time this way: the routing engine already gives an estimate, a rule built from the map, and the model predicts only the residual, how wrong the routing engine will be. The rule stays; the model corrects it.

## What did this chapter establish?

| Question | Answer |
|---|---|
| What makes a question a query? | the answer already sits in the data |
| What makes it a rule? | someone can write the decision as a condition |
| What makes it a prediction? | input known now, target known later, a decision that moves with the score |
| Regression or classification? | "how much" is regression; "will they" is classification |

**Interview line:** "A business question is a modelling problem when the input is known at decision time, the target is known later, and the decision changes with the prediction; if the answer is already in the data it is a query, and if I can write the decision down it is a rule."''',
]
ch2 = [
r'''md:# Chapter 2. What do we know, and when?

*Input, target, prediction time; the repeat-purchase target.*

Marketing wants a score per member for "will buy again in the next ninety days". Before any model, three things must be pinned down: the moment the score is made (the prediction time), what the model may read at that moment (the input), and what it is scored against afterwards (the target). This chapter builds all three on eight orders from four invented Kalpa members.

By the end you can define the ninety-day repeat flag from an order log with a cutoff date, build features that use only what was known at the cutoff, and spot the version that quietly reads the future.

**Search terms:** features and labels, supervised learning setup, prediction time, label leakage, target definition.''',
SETUP,
r'''# Eight orders from four Kalpa members, invented for teaching.
orders = pd.DataFrame({
    "member": ["M1", "M1", "M2", "M2", "M2", "M3", "M4", "M4"],
    "order_date": pd.to_datetime(["2026-04-10", "2026-07-20", "2026-05-02", "2026-06-15", "2026-06-28",
                                  "2026-06-01", "2026-04-25", "2026-10-15"]),
    "amount_rs": [800, 650, 400, 1200, 300, 950, 500, 700],
})
CUTOFF = pd.Timestamp("2026-06-30")
WINDOW_END = CUTOFF + pd.Timedelta(days=90)
print(orders.to_string(index=False))
print(f"\nprediction time (the cutoff): {CUTOFF.date()}; the outcome window runs to {WINDOW_END.date()}")''',
r'''md:## Where does each order sit against the cutoff?

The prediction is made on 30 June. An order on or before that date is history the model may read. An order in the ninety days after it decides the target. An order after the window counts for neither.

**Predict before you run.** How many of the four members buy again inside the window? (a) none (b) one (c) two (d) four''',
r'''# The week's timeline picture on four members: history, the cutoff, the outcome window.
fig, ax = plt.subplots(figsize=(10, 3.4))
ax.axvspan(CUTOFF, WINDOW_END, color="#FFF7E6", label="outcome window, 90 days")
ax.axvline(CUTOFF, color="#5B3FD6", lw=3)
for i, m in enumerate(["M1", "M2", "M3", "M4"]):
    d = orders[orders["member"] == m]
    colours = ["#5B3FD6" if t <= CUTOFF else ("#C98A00" if t <= WINDOW_END else "#9A968C") for t in d["order_date"]]
    ax.scatter(d["order_date"], [i] * len(d), s=120, c=colours, zorder=3)
ax.set_yticks(range(4)); ax.set_yticklabels(["M1", "M2", "M3", "M4"])
ax.text(CUTOFF, 3.6, "  prediction time: 30 June", color="#5B3FD6", fontsize=11)
ax.set_ylim(-0.6, 4.0); ax.set_title("Purple: history the model may read. Amber: decides the target. Grey: too late to count")
plt.show()''',
r'''# Inputs: only orders on or before the cutoff. Target: any order in the 90 days after it.
history = orders[orders["order_date"] <= CUTOFF]
window = orders[(orders["order_date"] > CUTOFF) & (orders["order_date"] <= WINDOW_END)]
table = pd.DataFrame({"member": ["M1", "M2", "M3", "M4"]}).set_index("member")
table["orders_before"] = history.groupby("member").size()
table["days_since_last"] = (CUTOFF - history.groupby("member")["order_date"].max()).dt.days
table["spend_before_rs"] = history.groupby("member")["amount_rs"].sum()
table["repeat_90d"] = table.index.isin(window["member"]).astype(int)
table = table.fillna(0).astype(int)
print(table.to_string())
check("no input uses an order dated after the cutoff", history["order_date"].max() <= CUTOFF)
check("the target window is exactly 90 days", (WINDOW_END - CUTOFF).days == 90)''',
r'''md:**What happened.** The answer is (b): only M1 buys inside the window (20 July). M4's next order, on 15 October, falls after the window closes, so M4's target is 0 even though M4 did buy again. The target is a definition, and "buy again" means "inside these ninety days" because that is what Marketing's budget covers.

## The trap: features computed on the whole log

A hurried analyst counts each member's orders on the full table, because that is the table they have today.''',
r'''# The leaky version: count orders on the full log, which includes the window itself.
leaky = table.copy()
leaky["orders_all_time"] = orders.groupby("member").size()
print(leaky[["orders_before", "orders_all_time", "repeat_90d"]].to_string())
print("\nM1 shows 2 orders all-time: one of them is the very purchase the model is meant to predict.")
check("the leaky count is larger exactly where the target or a later order sits", (leaky["orders_all_time"] > leaky["orders_before"]).sum() == 2)''',
r'''md:**Why it is wrong in Kalpa's terms.** On the day of the nudge, Marketing does not know about the 20 July order. A feature that counts it hands the model the answer, so the score looks brilliant offline and collapses the first morning it runs on real members. **The check:** for every input column, ask "would I know this value on 30 June?" **The fix:** compute every input from orders dated on or before the cutoff, and the target only from the window.

## What did this chapter establish?

| Question | Answer |
|---|---|
| What is the prediction time? | the cutoff, 30 June: the morning Marketing sends the nudge |
| What is the input? | anything known on or before the cutoff: orders, recency, spend |
| What is the target? | at least one order in the 90 days after the cutoff, 1 for M1 only |
| What breaks if the log is read whole? | inputs count the target's own purchase, and the offline score lies |

**Interview line:** "I fix the prediction time first, build every input from data dated on or before it, and define the target only from the window after it; a frozen reference date is what keeps the label honest."''',
]
ch3 = [
r'''md:# Chapter 3. Don't peek at the exam paper

*Train, validation, test; the seed; the baseline.*

A student who sees the board exam paper in advance scores well and has learned nothing anyone can trust. A model is the same. This chapter splits twenty invented Kalpa members into three slices, shows what the seed does, and scores the baseline every model has to beat.

By the end you can say what each slice is for and which one is spent once, why the seed is written down, and what the dumbest model scores on a table where most members do not come back.

**Search terms:** train validation test split, holdout set, random seed reproducibility, baseline model, majority class.''',
SETUP,
r'''# Twenty Kalpa members, invented for teaching: 5 came back within 90 days, 15 did not.
members = pd.DataFrame({"member": [f"M{i:02d}" for i in range(1, 21)],
                        "repeat_90d": [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]})
print(members.T.to_string(header=False))
print(f"share who came back: {members['repeat_90d'].mean():.2f}")''',
r'''md:## Three slices, three jobs

| Slice | The school version | The model version |
|---|---|---|
| train | the practice papers you study from | the rows the model learns from |
| validation | the mock exams you take as often as you like | the rows you compare models and settings on |
| test | the board exam, sat once | the rows you score the chosen model on, once, at the end |

**Predict before you run.** Split with seed 42 and again with seed 7. Will the test slice hold the same members? (a) yes, always (b) no, the seed decides which rows land where''',
r'''# Split 12 / 4 / 4, stratified so every slice keeps the share who came back, with two different seeds.
from sklearn.model_selection import train_test_split

def three_way(df, seed):
    rest, test = train_test_split(df, test_size=4, stratify=df["repeat_90d"], random_state=seed)
    train, val = train_test_split(rest, test_size=4, stratify=rest["repeat_90d"], random_state=seed)
    return train, val, test

slices = {}
for seed in (42, 7):
    tr, va, te = three_way(members, seed)
    slices[seed] = (tr, va, te)
    print(f"seed {seed:2d}  test: {sorted(te['member'])}   validation: {sorted(va['member'])}")
check("the seed changes which members are in the test slice", set(slices[42][2]["member"]) != set(slices[7][2]["member"]))
check("seed 42 gives the same test slice when run again", set(three_way(members, 42)[2]["member"]) == set(slices[42][2]["member"]))''',
r'''# Picture both splits: one square per member, coloured by slice.
fig, axes = plt.subplots(2, 1, figsize=(10, 2.6))
colour = {"train": "#5B3FD6", "validation": "#9C88F0", "test": "#C98A00"}
for ax, seed in zip(axes, (42, 7)):
    tr, va, te = slices[seed]
    where = {m: "train" for m in tr["member"]} | {m: "validation" for m in va["member"]} | {m: "test" for m in te["member"]}
    for i, m in enumerate(members["member"]):
        ax.add_patch(plt.Rectangle((i, 0), 0.9, 0.9, color=colour[where[m]]))
        ax.text(i + 0.45, 0.45, "Y" if members.loc[i, "repeat_90d"] else "", ha="center", va="center", color="white")
    ax.set_xlim(0, 20); ax.set_ylim(0, 1); ax.axis("off"); ax.set_title(f"seed {seed}: purple train, lilac validation, amber test (Y = came back)", fontsize=10)
plt.tight_layout(); plt.show()''',
r'''md:**What happened.** The answer is (b). The seed is the shuffle; a different seed is a different exam paper. Writing `random_state=42` into the notebook is what lets a teammate get the same slices, the same baseline and the same score.

## What does the dumbest model score?

The baseline for a will-they question is the majority class: say "no" for everyone. For a how-much question it is the mean: predict the average spend for everyone. A model is worth building only if it beats this.

**Predict before you run.** Saying "no" to all 20 members is right how often? (a) 25 percent (b) 50 percent (c) 75 percent (d) 95 percent''',
r'''# The majority-class baseline, by hand and by code.
from sklearn.dummy import DummyClassifier
by_hand = (members["repeat_90d"] == 0).mean()
dummy = DummyClassifier(strategy="most_frequent").fit(members[["member"]], members["repeat_90d"])
by_code = (dummy.predict(members[["member"]]) == members["repeat_90d"]).mean()
print(f"say no to everyone: right {int(by_hand * 20)} of 20, accuracy {by_hand:.2f} (by hand) and {by_code:.2f} (by code)")
check("the hand count and the DummyClassifier agree", by_hand == by_code)''',
r'''md:**What happened.** The answer is (c): 15 of 20, 75 percent, by knowing nothing about any member. A model that scores 75 percent here has learned only the share who came back.

**The flip.** The majority baseline is the right bar while classes are uneven. When a cheap rule exists (for example "nudge members who bought twice last quarter"), that rule is the stronger baseline, and the model has to beat it instead.

## What did this chapter establish?

| Question | Answer |
|---|---|
| What is each slice for? | train learns, validation compares, test is scored once at the end |
| Which slice is spent once? | test: any choice made by its score turns it into a second validation slice |
| What does the seed do? | fixes the shuffle, so everyone gets the same slices and the same baseline |
| What is the baseline? | the majority class for will-they, the mean for how-much; here 75 percent |

**Interview line:** "Train is where the model learns, validation is where I choose, and test is spent once on the model I chose; I state the seed, and I report the model next to its baseline, because a score means nothing without the bar it cleared."''',
]
make(NB + "C2_W05_D01_ch01_ml_problem_or_not_STUDENT.ipynb", ch1)
make(NB + "C2_W05_D01_ch02_input_target_time_STUDENT.ipynb", ch2)
make(NB + "C2_W05_D01_ch03_split_seed_baseline_STUDENT.ipynb", ch3)


# ---------------------------------------------------------------- ch456
NB = str(DAY / "1_in_class_training_content" / "notebooks") + "/"
ch4 = [
r'''md:# Chapter 4. Drawing the best line

*Linear regression: fit, coefficients in units, residuals.*

Kalpa's Indiranagar store wants to know how a member's spend moves with how often they visit. Six members, invented for teaching, are enough to see the whole idea: a line through the points, a slope in rupees per visit, and the leftovers (residuals) that say what the line missed.

By the end you can fit a line by hand on six points, get the same line from scikit-learn, read the slope in rupees, and say why "best" means the smallest total of squared residuals.

**Search terms:** linear regression explained, least squares, residuals, slope and intercept, StatQuest linear regression.''',
SETUP,
r'''# Six members of one Kalpa store, invented for teaching: visits last month and spend this month.
store = pd.DataFrame({"visits": [1, 2, 3, 4, 5, 6], "spend_rs": [290, 450, 500, 700, 750, 910]})
print(store.to_string(index=False))''',
r'''md:## Which line is "best"?

Before any code, draw a line by eye. Most people join the first and last points, which gives a slope of (910 minus 290) / 5 = Rs 124 per visit. The line any model must beat is the flat one at the mean spend, Rs 600, which ignores visits entirely.

**Predict before you run.** Which line leaves the smallest total of squared misses? (a) the flat mean line (b) the line through the first and last points (c) neither: a third line beats both''',
r'''# Least squares by hand: slope = sum of (x - mean x)(y - mean y) / sum of (x - mean x) squared.
x, y = store["visits"], store["spend_rs"]
dx, dy = x - x.mean(), y - y.mean()
slope = (dx * dy).sum() / (dx ** 2).sum()
intercept = y.mean() - slope * x.mean()
print(f"mean visits {x.mean()}, mean spend Rs {y.mean():.0f}")
print(f"sum of dx*dy = {(dx * dy).sum():.0f}, sum of dx squared = {(dx ** 2).sum():.1f}")
print(f"slope = Rs {slope:.0f} per visit, intercept = Rs {intercept:.0f}")

def sse(a, b):
    return float(((y - (a + b * x)) ** 2).sum())

lines = {"flat mean line": (y.mean(), 0.0), "first-to-last by eye": (166.0, 124.0), "least squares": (intercept, slope)}
for name, (a, b) in lines.items():
    print(f"{name:22s} spend = {a:5.0f} + {b:5.0f} x visits   sum of squared residuals {sse(a, b):9,.0f}")''',
r'''md:**What happened.** The answer is (c). The least-squares line, spend = Rs 180 + Rs 120 per visit, leaves a total of 5,200 squared rupees, against 5,480 for the eye's line and 257,200 for the flat mean. "Best" has a precise meaning: no other straight line leaves a smaller sum of squared residuals.''',
r'''# The same line from scikit-learn, as a second route.
from sklearn.linear_model import LinearRegression
lin = LinearRegression().fit(store[["visits"]], store["spend_rs"])
print(f"scikit-learn: slope {lin.coef_[0]:.2f}, intercept {lin.intercept_:.2f}")
check("the hand slope and scikit-learn agree", abs(lin.coef_[0] - slope) < 1e-9)
check("least squares beats the eye's line and the mean line", sse(intercept, slope) < min(sse(166, 124), sse(y.mean(), 0)))''',
r'''# Draw the residuals as squares: the fit is the line whose squares add up smallest.
store["predicted"] = lin.predict(store[["visits"]])
store["residual"] = store["spend_rs"] - store["predicted"]
fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4))
for ax, (name, (a, b)) in zip((a1, a2), [("flat mean line", lines["flat mean line"]), ("least squares", lines["least squares"])]):
    pred = a + b * x
    ax.scatter(x, y, color="#1C1B16", zorder=3)
    ax.plot([0.5, 6.5], [a + b * 0.5, a + b * 6.5], color="#5B3FD6", lw=2)
    for xi, yi, pi in zip(x, y, pred):
        side = abs(yi - pi) / 160  # a square of side |residual|, drawn to the x-scale
        ax.add_patch(plt.Rectangle((xi, min(yi, pi)), side, abs(yi - pi), color="#C0392B", alpha=0.25))
        ax.plot([xi, xi], [yi, pi], color="#C0392B")
    ax.set_title(f"{name}: squares add to {sse(a, b):,.0f}"); ax.set_xlabel("visits last month"); ax.set_ylabel("spend this month, Rs")
plt.tight_layout(); plt.show()
print(store.to_string(index=False))
check("residuals of a least-squares line with an intercept sum to zero", abs(store["residual"].sum()) < 1e-6)''',
r'''md:## What does the coefficient say, in rupees?

**Slope, Rs 120 per visit:** among these members, each extra visit last month goes with Rs 120 more spend this month. It is an association across members inside this fit. Whether getting a member to visit once more adds Rs 120 is a causal claim, and only an experiment (Week 1 Thursday) can back it.

**Intercept, Rs 180:** the line's value at zero visits. No member here made zero visits, so this is the line extended beyond its data, a number to quote with care.

**Residuals:** -10, +30, -40, +40, -30, +10. Small, mixed signs, no pattern: the straight line holds on these six points. Chapter 6 shows the residuals of a line that does not hold.

**Search it later as:** ordinary least squares, R squared. Here the line removes 98 percent of the squared error of the mean line (1 minus 5,200 / 257,200).

## What did this chapter establish?

| Question | Answer |
|---|---|
| What is the fitted line? | spend = Rs 180 + Rs 120 x visits |
| What makes it the best line? | the smallest sum of squared residuals, 5,200 against 5,480 by eye and 257,200 for the mean |
| What does the slope say? | Rs 120 more spend per extra visit, as an association, other things not held |
| What do the residuals say? | small and patternless here, so a line is enough |

**Interview line:** "Linear regression picks the line with the smallest sum of squared residuals; I read each coefficient in the target's units, say it is an association unless an experiment backs it, and look at the residuals before I trust the line."''',
]
ch5 = [
r'''md:# Chapter 5. From a line to a probability

*Logistic regression: probability, direction, strength.*

Marketing's question is "will this member buy again", a yes or a no. Twelve Kalpa members, invented for teaching, show why a straight line is the wrong tool for that question and how bending it into an S fixes it. The S gives a probability, its sign gives the direction, and the size of its coefficient gives the strength.

By the end you can say what a logistic output of 0.73 means, read a coefficient as a multiplier on the odds, and explain why the line fails at the ends.

**Search terms:** logistic regression, sigmoid function, odds and log-odds, odds ratio, StatQuest logistic regression.''',
SETUP,
r'''# Twelve Kalpa members, invented for teaching: visits last quarter and whether they bought again in 90 days.
members = pd.DataFrame({"visits": [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 7],
                        "repeat_90d": [0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1]})
print(members.T.to_string(header=False))''',
r'''md:## What goes wrong if we fit a line?

A straight line fitted to 0s and 1s gives a number for every member. Read it as a probability and see what happens at the ends.

**Predict before you run.** For a member with 8 visits, the straight line predicts (a) about 0.9 (b) exactly 1.0 (c) more than 1.0''',
r'''# The straight line on yes/no data, and what it says at 0 and at 8 visits.
from sklearn.linear_model import LinearRegression, LogisticRegression
line = LinearRegression().fit(members[["visits"]], members["repeat_90d"])
at = pd.DataFrame({"visits": [0, 4, 8]})
print(pd.DataFrame({"visits": at["visits"], "line_says": line.predict(at).round(2)}).to_string(index=False))
check("the line leaves the 0 to 1 range at 8 visits", line.predict(pd.DataFrame({"visits": [8]}))[0] > 1)''',
r'''md:**What happened.** The answer is (c): 1.28, a "probability" above 1, which no member can have. The line also dips to -0.01 at zero visits. A line keeps rising forever; a probability has to flatten out near 0 and near 1.

## Bend the line into an S

Logistic regression keeps a straight line underneath, `z = a + b x visits`, and squeezes it through the S-shaped function `p = 1 / (1 + exp(-z))`, which can never leave 0 to 1.''',
r'''# Fit the logistic model without a penalty, so the numbers match the formula exactly.
logit = LogisticRegression(C=1e6).fit(members[["visits"]], members["repeat_90d"])
a, b = logit.intercept_[0], logit.coef_[0][0]
grid = pd.DataFrame({"visits": np.linspace(0, 8, 161)})
print(f"z = {a:.2f} + {b:.2f} x visits")
p4 = logit.predict_proba(pd.DataFrame({"visits": [4]}))[0, 1]
by_formula = 1 / (1 + np.exp(-(a + b * 4)))
print(f"a member with 4 visits: p = {p4:.2f} from the model, {by_formula:.2f} from the formula")
check("the model's probability equals the formula's", abs(p4 - by_formula) < 1e-9)
check("every probability on the grid stays between 0 and 1", logit.predict_proba(grid)[:, 1].min() > 0 and logit.predict_proba(grid)[:, 1].max() < 1)

fig, ax = plt.subplots(figsize=(9, 4))
ax.scatter(members["visits"], members["repeat_90d"], s=90, color="#1C1B16", zorder=3, label="members (0 = no, 1 = bought again)")
ax.plot(grid["visits"], line.predict(grid), color="#9A968C", ls="--", label="straight line")
ax.plot(grid["visits"], logit.predict_proba(grid)[:, 1], color="#5B3FD6", lw=3, label="logistic S-curve")
ax.axhline(1, color="#C0392B", lw=0.8); ax.axhline(0, color="#C0392B", lw=0.8)
ax.scatter([4], [p4], s=140, color="#C98A00", zorder=4); ax.text(4.15, p4 - 0.08, f"4 visits: {p4:.2f}")
ax.set_xlabel("visits last quarter"); ax.set_ylabel("chance of buying again"); ax.legend(loc="upper left", fontsize=9)
ax.set_title("The line runs past 1; the S stays inside 0 to 1")
plt.show()''',
r'''md:**What 0.73 means.** Of 100 members who look like this one (4 visits), about 73 would buy again within 90 days, if the model is calibrated. It is a statement about a group of similar members, never a promise about this one.

## Direction and strength

**Direction** is the sign of `b`. Here `b` is positive, so more visits go with a higher chance of buying again.

**Strength** is the size of `b`, read through `exp(b)`: each extra visit multiplies the odds of buying again by that factor. Odds are p / (1 - p): a probability of 0.75 is odds of 3 to 1.''',
r'''# Read the coefficient as a multiplier on the odds, then confirm it on two neighbouring members.
odds = lambda p: p / (1 - p)
p3 = logit.predict_proba(pd.DataFrame({"visits": [3]}))[0, 1]
print(f"exp(b) = {np.exp(b):.2f}: each extra visit multiplies the odds by about {np.exp(b):.1f}")
print(f"3 visits: p = {p3:.2f}, odds {odds(p3):.2f};  4 visits: p = {p4:.2f}, odds {odds(p4):.2f};  ratio {odds(p4) / odds(p3):.2f}")
check("the odds ratio between 3 and 4 visits equals exp(b)", abs(odds(p4) / odds(p3) - np.exp(b)) < 1e-9)''',
r'''md:**The trap.** "Each extra visit adds 1.05 to the probability" reads the coefficient as if it were a line's slope. It adds 1.05 to the log-odds, which multiplies the odds by 2.85; the change in probability depends on where you start (0.25 to 0.49 from 2 to 3 visits, 0.88 to 0.96 from 5 to 6).

**The flip.** Logistic regression gives one direction per input. If the chance of buying rises at both ends of an input (very new and very old members both come back more), one S cannot hold it; chapter 6 shows that failure.

## What did this chapter establish?

| Question | Answer |
|---|---|
| Why not a line? | it predicts 1.28 at 8 visits and -0.01 at 0, outside 0 to 1 |
| What does logistic regression output? | a probability: 0.73 means about 73 of 100 similar members buy again |
| Direction | the sign of b: positive, more visits, more likely |
| Strength | exp(b) = 2.85: each extra visit multiplies the odds by about 2.85 |

**Interview line:** "A logistic output of 0.71 means that among customers who look like this one, about 71 in 100 do the thing, if the model is calibrated; the coefficient's sign is the direction and exp of it is the multiplier on the odds."''',
]
ch6 = [
r'''md:# Chapter 6. What the leftovers confess

*Where each model fails; the residual tells.*

A fitted line always looks fine on a scatter plot from a distance. The residuals, what each point missed by, are where a wrong shape confesses. This chapter uses real public data: the UCI Auto MPG table of 398 cars from the 1970s and early 1980s, where fuel economy (miles per gallon) falls as horsepower rises, along a curve.

By the end you can draw a residual plot, read a bow in it as "the straight line missed a curve", fix it with horsepower squared, and say where each fix and each model stops working.

**Search terms:** residual plot, regression diagnostics, non-linear relationship, polynomial features, extrapolation.

Dataset: UCI Auto MPG, R. Quinlan, licensed CC BY 4.0, archive.ics.uci.edu/dataset/9/auto+mpg (verified 28 October 2026).''',
SETUP + r'''
# Load the day's public dataset once; later runs read the cached copy.
CACHE = pathlib.Path.home() / ".cache" / "c2_datasets"
CACHE.mkdir(parents=True, exist_ok=True)

def load_cars():
    """UCI Auto MPG (CC BY 4.0): whitespace-separated, no header, '?' where horsepower is missing."""
    f = CACHE / "auto-mpg.data"
    if not f.exists():
        z = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(
            "https://archive.ics.uci.edu/static/public/9/auto+mpg.zip", timeout=60).read()))  # verified 28 October 2026
        f.write_bytes(z.read("auto-mpg.data"))
    names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"]
    return pd.read_csv(f, sep=r"\s+", names=names, na_values="?")

raw = load_cars()
cars = raw.dropna(subset=["horsepower"]).reset_index(drop=True)
print(f"{len(raw)} cars, {raw['horsepower'].isna().sum()} with no horsepower, {len(cars)} kept")
check("six cars have no horsepower and are dropped", raw["horsepower"].isna().sum() == 6 and len(cars) == 392)''',
r'''md:## Fit the straight line first

**Predict before you run.** If the true shape is a curve that flattens at high horsepower, the straight line's residuals will be (a) scattered evenly around zero (b) positive at both ends and negative in the middle (c) negative everywhere''',
r'''# Fit mpg on horsepower with a straight line and look at the residuals against horsepower.
from sklearn.linear_model import LinearRegression
X1 = cars[["horsepower"]]
line = LinearRegression().fit(X1, cars["mpg"])
cars["resid_line"] = cars["mpg"] - line.predict(X1)
print(f"mpg = {line.intercept_:.2f} {line.coef_[0]:+.4f} x horsepower")
bins = pd.qcut(cars["horsepower"], 5)
bow = cars.groupby(bins, observed=True)["resid_line"].mean().round(2)
print("mean residual in five horsepower bands, lowest to highest:"); print(bow.to_string())
check("the bow: both end bands sit above zero and the middle band below", bow.iloc[0] > 1 and bow.iloc[-1] > 0 and bow.iloc[2] < -1)''',
r'''md:**What happened.** The answer is (b). The cheapest-horsepower cars beat the line by 2.7 mpg on average, the middle band falls 2.2 below it, and the most powerful cars sit back above it. A pattern like that is the line confessing that the real relationship bends.''',
r'''# Add horsepower squared, refit, and draw both residual plots side by side.
cars["hp2"] = cars["horsepower"] ** 2
curve = LinearRegression().fit(cars[["horsepower", "hp2"]], cars["mpg"])
cars["resid_curve"] = cars["mpg"] - curve.predict(cars[["horsepower", "hp2"]])
bow2 = cars.groupby(bins, observed=True)["resid_curve"].mean().round(2)

fig, axes = plt.subplots(1, 3, figsize=(13, 3.8))
grid = pd.DataFrame({"horsepower": np.linspace(46, 230, 100)}); grid["hp2"] = grid["horsepower"] ** 2
axes[0].scatter(cars["horsepower"], cars["mpg"], s=8, color="#9A968C")
axes[0].plot(grid["horsepower"], line.predict(grid[["horsepower"]]), color="#C0392B", label="straight line")
axes[0].plot(grid["horsepower"], curve.predict(grid), color="#5B3FD6", lw=2, label="with horsepower squared")
axes[0].set_xlabel("horsepower"); axes[0].set_ylabel("mpg"); axes[0].legend(fontsize=8); axes[0].set_title("The data")
for ax, col, title in [(axes[1], "resid_line", "Residuals of the line: a bow"), (axes[2], "resid_curve", "Residuals with hp squared: flat")]:
    ax.scatter(cars["horsepower"], cars[col], s=8, color="#9A968C")
    means = cars.groupby(bins, observed=True)[col].mean()
    ax.plot([iv.mid for iv in means.index], means.values, color="#C0392B", lw=3, marker="o")
    ax.axhline(0, color="#1C1B16", lw=1); ax.set_ylim(-15, 18); ax.set_title(title); ax.set_xlabel("horsepower")
plt.tight_layout(); plt.show()
print("band means after the fix:", bow2.tolist())
rmse = lambda r: float(np.sqrt((r ** 2).mean()))
print(f"typical miss: line {rmse(cars['resid_line']):.2f} mpg, with hp squared {rmse(cars['resid_curve']):.2f} mpg")
check("the fix shrinks the widest band mean below 1 mpg", bow2.abs().max() < 1.0)
check("the fix lowers the typical miss", rmse(cars["resid_curve"]) < rmse(cars["resid_line"]))''',
r'''md:## Where does each model fail?

| Model | Where it fails | What the residuals or outputs show | The fix, and when it comes |
|---|---|---|---|
| Straight line | the truth curves | a bow: positive at the ends, negative in the middle | a squared term today; Wednesday turns this into feature engineering |
| Line with a squared term | outside the data | it predicts mpg rising again past about 190 horsepower | never quote it beyond the range it was fitted on |
| Logistic regression | the chance rises at both ends of an input | one S can only go one way, so the middle is over- or under-called | the same squared-term idea, or bands of the input |
| Any model | the input is missing or wrong | six cars have `?` for horsepower | decide and record what happens to them before fitting |''',
r'''# The squared term's own failure: ask it about engines beyond the data.
for hp in (150, 200, 230, 300):
    g = pd.DataFrame({"horsepower": [hp], "hp2": [hp * hp]})
    print(f"{hp} hp: line says {line.predict(g[['horsepower']])[0]:5.1f} mpg, curve says {curve.predict(g)[0]:5.1f} mpg")
check("the curve predicts more mpg at 300 hp than at 200 hp, which no engine does", curve.predict(pd.DataFrame({"horsepower": [300], "hp2": [90000]}))[0] > curve.predict(pd.DataFrame({"horsepower": [200], "hp2": [40000]}))[0])''',
r'''md:**The rule.** Read the residuals before you trust the fit. A pattern in them (a bow, a fan, bands) is a shape the model missed; random scatter around zero is what a good fit leaves behind. **The flip:** a flat residual plot is evidence for the shape inside the data's range only; outside it, even the curve that fixed the bow fails.

## What did this chapter establish?

| Question | Answer |
|---|---|
| What did the line's residuals show? | a bow: +2.7 mpg in the lowest horsepower band, -2.2 in the middle, +0.8 at the top |
| What fixed it? | horsepower squared: the band means fall within 1 mpg, the typical miss from 4.89 to 4.36 mpg |
| Where does the fix fail? | beyond about 190 horsepower it predicts mileage rising again |
| Where does logistic regression fail? | where the chance rises at both ends of an input |

**Interview line:** "I plot residuals against the input and against the prediction; a bow means the shape is wrong, a fan means the spread changes, and I never quote a polynomial outside the range it was fitted on."''',
]
make(NB + "C2_W05_D01_ch04_linear_regression_STUDENT.ipynb", ch4)
make(NB + "C2_W05_D01_ch05_logistic_regression_STUDENT.ipynb", ch5)
make(NB + "C2_W05_D01_ch06_residuals_auto_mpg_STUDENT.ipynb", ch6)


# ---------------------------------------------------------------- case01
NB = str(DAY / "1_in_class_training_content" / "notebooks") + "/"
cells = [
r'''md:# Case 1: Whom should the bank call?

**Applies chapters 1, 2 and 3:** prediction, rule or query; input, target, prediction time; train, validation, test, the seed and the baseline.

A Portuguese bank phoned 41,188 clients between May 2008 and November 2010 to sell a term deposit (money locked away for a fixed time at a fixed rate). Every call costs an agent's minutes, and most clients say no. The marketing team wants a list: whom do we call first?

By the end of this notebook you can:

- say why "whom do we call" is a prediction problem and name its input, target and prediction time;
- pick the columns the bank knows on the morning of the call;
- split the rows into train, validation and test with a stated seed, and seal the test slice.

**Search terms:** problem framing in machine learning, features and labels, train validation test split, stratified split, random seed.

| | The bank (real data) | Kalpa Retail (our decision) |
|---|---|---|
| The action | a phone call from an agent | a Rs 40 discount nudge from Marketing |
| The question | will this client open a term deposit? | will this member buy again in the next ninety days? |
| The input | the client table on the morning of the call | the customer table on the day of the nudge |
| The target | `y`: yes or no, known once the call ends | the repeat flag, known ninety days later |
| Who asks | the campaign manager | Marketing, with Kavya Nair (senior analyst) asking for the baseline first |''',
SETUP,
BANK,
r'''md:## How many clients said yes?

The target column is `y`. Before you count it, commit to a guess.

**Predict before you run.** What share of the 41,188 calls ended in a yes? (a) about half (b) about a quarter (c) about one in nine (d) about one in thirty''',
r'''# Count the target: how many yes, how many no, and the share of yes.
counts = bank["y"].value_counts()
rate = (bank["y"] == "yes").mean()
print(counts.to_string())
print(f"Share of yes: {rate:.4f}, which is about 1 in {1/rate:.1f} calls")''',
r'''md:**What happened.** The answer is (c): 4,640 yes against 36,548 no, a share of 0.1127. Nine calls in ten end in a no, and every later number today is read against that fact.

## Which columns does the bank know on the morning of the call?

Chapter 2's test is one question asked of every column: on the morning of the call, before anyone dials, does the bank already hold this value? Today the model uses only the client's profile and how earlier campaigns went. Seven more columns arrive from other feeds, and Wednesday audits each of them with the same question, so they wait.''',
r'''# Sort the 21 columns into the three groups the week works with.
PROFILE = ["age", "job", "marital", "education", "default", "housing", "loan"]
HISTORY = ["contact", "month", "day_of_week", "campaign", "previous", "poutcome"]
TARGET = ["y"]
LATER = [c for c in bank.columns if c not in PROFILE + HISTORY + TARGET]

groups = pd.DataFrame({
    "group": ["profile (used today)", "history (used today)", "other feeds (audited Wednesday)", "target"],
    "columns": [", ".join(PROFILE), ", ".join(HISTORY), ", ".join(LATER), "y"],
    "count": [len(PROFILE), len(HISTORY), len(LATER), 1],
})
print(groups.to_string(index=False))
check("the four groups hold all 21 columns once each", groups["count"].sum() == bank.shape[1])
check("today's input has 13 columns", len(PROFILE + HISTORY) == 13)''',
r'''md:## Where does the prediction sit in time?

The prediction is made on the morning of the call. Everything to the left of that moment can be an input; the answer, `y`, only exists to the right of it. This one picture comes back every day this week, and each day adds to it.''',
r'''# The week's timeline picture, in its Monday state.
fig, ax = plt.subplots(figsize=(10, 2.8))
ax.axhline(0, color="#1C1B16", lw=2)
ax.axvspan(0, 6, color="#EEEAFB")
ax.axvspan(6, 9, color="#FFF7E6")
ax.axvline(6, color="#5B3FD6", lw=3)
ax.text(3, 0.45, "what the bank already knows\nprofile and earlier campaigns", ha="center", fontsize=12)
ax.text(6, -0.75, "prediction moment:\nthe morning of the call", ha="center", fontsize=12, color="#5B3FD6")
ax.text(7.5, 0.45, "the outcome\ny = yes or no", ha="center", fontsize=12, color="#8A5A1F")
ax.set_xlim(0, 9); ax.set_ylim(-1.2, 1.1); ax.axis("off")
ax.set_title("Inputs live left of the line, the target lives right of it", fontsize=13)
plt.show()''',
r'''md:## How do we split the rows so a score means something?

The week uses one split. The test slice is cut first, 20 percent of rows, and sealed: nobody scores a model on it until Friday. The rest splits 75 to 25 into train (the model learns here) and validation (we compare models here). `stratify` keeps the share of yes the same in every slice, and `random_state=42` is the seed that makes the cut the same on every laptop.

**Predict before you run.** How many rows land in validation? (a) 8,238 (b) 10,297 (c) 24,712 (d) 32,950''',
PIPE + r'''
train, val, test = week_split(bank, seed=42)
for name, part in [("train", train), ("validation", val), ("test (sealed)", test)]:
    print(f"{name:14s} {len(part):6,d} rows   share of yes {(part['y'] == 'yes').mean():.4f}")''',
r'''md:**What happened.** The answer is (a): 8,238 rows in validation and 8,238 sealed in test, with 24,712 left to train on. The share of yes is 0.1126 or 0.1127 in every slice because the split was stratified.''',
r'''# Picture the split: three slices, the same share of yes, one of them sealed.
sizes = [len(train), len(val), len(test)]
shares = [(p["y"] == "yes").mean() for p in (train, val, test)]
fig, ax = plt.subplots(figsize=(8, 3.6))
bars = ax.bar(["train", "validation", "test"], sizes, color=["#5B3FD6", "#9C88F0", "#FFFFFF"],
              edgecolor="#1C1B16", hatch=["", "", "//"])
for b, n, s in zip(bars, sizes, shares):
    ax.text(b.get_x() + b.get_width() / 2, n + 400, f"{n:,} rows\n{s:.1%} yes", ha="center", fontsize=11)
ax.text(2, 3000, "SEALED\nuntil Friday", ha="center", fontsize=12, fontweight="bold")
ax.set_ylim(0, 30000); ax.set_ylabel("rows")
ax.set_title("The week's split, seed 42")
plt.show()

check("the three slices add up to every row", sum(sizes) == len(bank))
check("no row sits in two slices", len(set(train.index) & set(val.index)) + len(set(val.index) & set(test.index)) + len(set(train.index) & set(test.index)) == 0)
check("the share of yes matches across slices within 0.1 point", max(shares) - min(shares) < 0.001)''',
r'''md:## The trap: a split with no seed

A hurried analyst writes `train_test_split(bank, test_size=0.2)` with no seed and no stratify. The code runs, so it looks fine. Run it five times and the validation share of yes moves, which means the baseline you have to beat moves too, and two teammates quoting "the validation score" are quoting scores on different rows.''',
r'''# Five unseeded, unstratified splits: the share of yes in the held-out part moves each time.
from sklearn.model_selection import train_test_split
rng_shares = []
for _ in range(5):
    _, held = train_test_split(bank, test_size=0.2)
    rng_shares.append((held["y"] == "yes").mean())
print("held-out share of yes, five runs without a seed:", [round(float(s), 4) for s in rng_shares])

seeded = [(week_split(bank, seed=42)[1]["y"] == "yes").mean() for _ in range(5)]
print("validation share of yes, five runs with seed 42:  ", [round(float(s), 4) for s in seeded])
check("seed 42 gives the identical slice every run", len(set(seeded)) == 1)''',
r'''md:**The fix.** State the seed, stratify on the target, and write both into the notebook's first cells, so anybody who reruns it gets the same rows and the same baseline.

## What did this notebook establish?

| Question | Answer |
|---|---|
| Is "whom do we call" a prediction problem? | Yes: an input known on the morning of the call, a target known after it, and a call list that changes with the score |
| What share said yes? | 4,640 of 41,188, which is 0.1127 |
| What is the input today? | 13 columns: 7 about the client, 6 about this and earlier campaigns |
| How are the rows split? | train 24,712, validation 8,238, test 8,238 sealed until Friday, seed 42, stratified |
| What does the seed buy? | the same rows, so the same baseline, on every laptop |

**Next:** case 2 scores the dumbest possible model on the validation slice and asks the logistic model to beat it.''',
]
make(NB + "C2_W05_D01_case01_whom_to_call_STUDENT.ipynb", cells)


# ---------------------------------------------------------------- case02
NB = str(DAY / "1_in_class_training_content" / "notebooks") + "/"
cells = [
r'''md:# Case 2: Beat the dumbest model

**Applies chapters 3 and 5:** the baseline, and logistic regression read as probability, direction and strength. It starts from case 1's state: the same 13 columns, the same seed-42 split, the test slice still sealed.

Kavya Nair, Kalpa's senior analyst, set the condition for the whole week: "Before you show me any model, show me the dumbest possible baseline and what beating it would prove." The bank's campaign manager is owed the same courtesy.

By the end of this notebook you can:

- score the majority-class baseline by hand and by code and get the same number;
- fit the logistic model on the customer table and say how far it sits above the baseline, in rows;
- read one coefficient in words a marketing manager can repeat;
- name the caveat that comes with a random split on this file.

**Search terms:** baseline model, majority class classifier, DummyClassifier, logistic regression coefficients, odds ratio.''',
SETUP,
BANK,
PIPE + r'''
train, val, test = week_split(bank, seed=42)
y_train = (train["y"] == "yes").astype(int)
y_val = (val["y"] == "yes").astype(int)
print(f"train {len(train):,}  validation {len(val):,}  test {len(test):,} (sealed)")''',
r'''md:## What does doing nothing score?

The dumbest model ignores every column and says the majority answer for everyone. Here the majority answer is no, so the model says "do not call" to all 8,238 validation clients and is right whenever the client would have said no anyway.

**Predict before you run.** What accuracy does "call nobody" score on validation? (a) 0.50 (b) 0.75 (c) 0.887 (d) 1.00''',
r'''# The baseline twice: by hand from the share of no, then with scikit-learn's DummyClassifier.
from sklearn.dummy import DummyClassifier
by_hand = (y_val == 0).mean()
dummy = DummyClassifier(strategy="most_frequent").fit(train[COLUMNS], y_train)
by_code = accuracy_score(y_val, dummy.predict(val[COLUMNS]))
print(f"by hand: {(y_val == 0).sum():,} of {len(y_val):,} are no, accuracy {by_hand:.4f}")
print(f"by code: DummyClassifier accuracy {by_code:.4f}")
check("the hand count and DummyClassifier agree", abs(by_hand - by_code) < 1e-12)''',
r'''md:**What happened.** The answer is (c): calling nobody is right 7,310 times in 8,238, an accuracy of 0.8874. Any model that scores 0.88 has learned nothing, however good 88 sounds.

## Does the logistic model beat it?

The logistic model turns the 13 columns into a probability of yes for each client. Reading it as a yes when the probability is 0.5 or more gives a yes-or-no answer we can score with the same accuracy.

**Predict before you run.** How many more validation clients will the model get right than "call nobody" does? (a) about 800 (b) about 80 (c) about 8 (d) none''',
r'''# Fit on train, score on validation. The test slice is not touched.
model = logistic(COLUMNS, bank).fit(train[COLUMNS], y_train)
p_val = model.predict_proba(val[COLUMNS])[:, 1]
pred = (p_val >= 0.5).astype(int)
acc = accuracy_score(y_val, pred)
right_model = int((pred == y_val).sum())
right_base = int((y_val == 0).sum())
print(f"logistic accuracy {acc:.4f}: {right_model:,} right of {len(y_val):,}")
print(f"baseline accuracy {by_hand:.4f}: {right_base:,} right of {len(y_val):,}")
print(f"edge: {right_model - right_base} more right answers, {100 * (acc - by_hand):.2f} points of accuracy")
check("the model beats the baseline on validation", acc > by_hand)
check("the edge is under two points", acc - by_hand < 0.02)''',
r'''# The edge, drawn honestly: the full height first, then the gap that matters.
fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 3.8))
a1.bar(["call nobody", "logistic model"], [right_base, right_model], color=["#9A968C", "#5B3FD6"])
a1.set_ylim(0, len(y_val)); a1.set_ylabel("right answers of 8,238")
a1.set_title("Side by side, they look the same")
a2.bar(["call nobody", "logistic model"], [0, right_model - right_base], color=["#9A968C", "#5B3FD6"])
a2.text(1, right_model - right_base + 2, f"+{right_model - right_base}", ha="center", fontsize=13)
a2.set_ylim(0, 120); a2.set_title("What the model adds over doing nothing")
plt.tight_layout(); plt.show()''',
r'''md:**What happened.** The answer is (b): 80 more right answers in 8,238, under one point of accuracy. The model does carry signal, and it is small. Tuesday asks how many of the 928 clients who said yes this model actually put on the call list, and that count changes how the 0.897 reads.

## What does one coefficient say to the campaign manager?

The logistic model's output for each client is a probability between 0 and 1. Its mean over validation should sit close to the share of yes, since the model is calibrated to this world.''',
r'''# The model's probabilities: spread out, low on average, centred near the base rate.
fig, ax = plt.subplots(figsize=(9, 3.4))
ax.hist(p_val, bins=40, color="#5B3FD6")
ax.axvline(0.5, color="#C0392B", ls="--"); ax.text(0.51, ax.get_ylim()[1] * 0.8, "0.5", color="#C0392B")
ax.set_xlabel("predicted probability of yes"); ax.set_ylabel("validation clients")
ax.set_title("Most clients score low; a few score high")
plt.show()
print(f"mean predicted probability {p_val.mean():.4f}, share of yes {y_val.mean():.4f}")
check("the mean probability is within one point of the share of yes", abs(p_val.mean() - y_val.mean()) < 0.01)''',
r'''md:`campaign` counts the calls already made to this client in the current campaign, including this one. The model stores its coefficient on the standardised scale, so divide by the column's spread to get it per call, then take `exp` to turn log-odds into a multiplier on the odds.

**Predict before you run.** One more call to the same client in this campaign does what to the odds of a yes? (a) doubles them (b) leaves them unchanged (c) lowers them a little (d) halves them''',
r'''# Read the campaign coefficient per call, as a multiplier on the odds.
names = model.named_steps["prep"].get_feature_names_out()
coefs = pd.Series(model.named_steps["model"].coef_[0], index=names)
scale = dict(zip(model.named_steps["prep"].named_transformers_["num"].feature_names_in_,
                 model.named_steps["prep"].named_transformers_["num"].scale_))
per_call = coefs["num__campaign"] / scale["campaign"]
print(f"log-odds per extra call {per_call:.4f}; odds multiplier {np.exp(per_call):.3f}")
print(f"in words: each extra call in this campaign goes with about {100 * (1 - np.exp(per_call)):.0f} percent lower odds of a yes, other columns held")

# A second route: add one call to every validation client and compare the odds directly.
bumped = val[COLUMNS].copy(); bumped["campaign"] += 1
p_bump = model.predict_proba(bumped)[:, 1]
ratio = (p_bump / (1 - p_bump)) / (p_val / (1 - p_val))
print(f"odds ratio measured on 8,238 clients: min {ratio.min():.4f}, max {ratio.max():.4f}")
check("the direction is negative", per_call < 0)
check("the measured odds ratio equals exp(coefficient) for every client", np.allclose(ratio, np.exp(per_call)))''',
r'''md:**What happened.** The answer is (c). Direction: negative, so more calls go with fewer yeses. Strength: each extra call multiplies the odds by 0.93, about 7 percent lower. For the campaign manager: "Calling the same client again and again is associated with a falling chance of a yes, about 7 percent lower odds per call, other things equal." That is an association inside this fit. Whether the extra calls cause the fall needs an experiment, which Week 1 Thursday taught.

## What caveat travels with this score?

The file is sorted by date from May 2008 to November 2010, and our random split mixes those years. If the share of yes changed a lot from year to year, the `month` column helps the model guess the period, and some of the 80 extra right answers are the calendar talking.''',
r'''# Recover the year from row order (the month index drops when a new year starts) and count yes by year.
order = {m: i for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])}
year, prev, years = 2008, -1, []
for m in bank["month"]:
    if order[m] < prev:
        year += 1
    prev = order[m]; years.append(year)
by_year = bank.assign(year=years).groupby("year")["y"].agg(rows="size", yes_share=lambda s: (s == "yes").mean())
print(by_year.round(3).to_string())
fig, ax = plt.subplots(figsize=(7, 3.4))
ax.bar(by_year.index.astype(str), by_year["yes_share"], color=["#9C88F0", "#5B3FD6", "#1A0F5C"])
for x, (n, s) in enumerate(zip(by_year["rows"], by_year["yes_share"])):
    ax.text(x, s + 0.02, f"{s:.0%} of {n:,}", ha="center")
ax.set_ylim(0, 0.65); ax.set_ylabel("share of yes"); ax.set_title("The same campaign, three very different years")
plt.show()
check("the three years cover every row", by_year["rows"].sum() == len(bank))''',
r'''md:**The caveat, in one line for the memo:** on a random split this score is partly about when the call was made, because the share of yes rose from 5 percent in 2008 to 52 percent in 2010. Friday splits by time instead and shows what that does.

## The trap: quoting 0.897 on its own

A hurried status update reads: "Our model is 89.7 percent accurate." The number is right and the sentence misleads, because doing nothing scores 88.7. Written with its baseline, it reads: "The model beats calling nobody by under one point, 80 more right answers in 8,238; Tuesday checks whether those are the clients we want." The first sentence gets a model shipped; the second gets the right question asked.

## What did this notebook establish?

| Question | Answer |
|---|---|
| What does doing nothing score? | 0.8874 on validation, 7,310 right of 8,238 |
| What does the logistic model score? | 0.8971, 7,390 right: 80 more, under one point |
| What does the model output? | a probability per client, mean 0.114 against a share of yes of 0.113 |
| One coefficient for the campaign manager | each extra call goes with about 7 percent lower odds of a yes, other columns held |
| The caveat | the random split mixes 2008 (5 percent yes) with 2010 (52 percent), so part of the score is the calendar |

**Next:** case 3 shows the fastest way to make 0.897 look better than it is, and why the envelope stays on the wall.''',
]
make(NB + "C2_W05_D01_case02_beat_the_baseline_STUDENT.ipynb", cells)


# ---------------------------------------------------------------- case03
NB = str(DAY / "1_in_class_training_content" / "notebooks") + "/"
cells = [
r'''md:# Case 3: The peek

**Applies chapter 3:** train, validation, test, and why the test slice is spent once. It starts from case 2's state: the same split and the same logistic model, scoring 0.8971 against the baseline's 0.8874.

A junior on the bank's team is short of time. Instead of choosing a model on validation and scoring the test once, they try 60 versions of the model, each with a different list of columns, score every version on the held-out slice, and keep the best. The best number goes in the status update. This notebook stages that peek and catches it.

The real test slice stays sealed in its envelope. A practice envelope of 2,000 validation rows plays its part, and the other 6,238 validation rows are the fresh slice nobody looked at.

By the end of this notebook you can:

- show how choosing by a held-out score inflates that score;
- measure the inflation against a fresh slice;
- say in one sentence why the test slice is spent once.

**Search terms:** test set leakage, selection bias in model evaluation, data snooping, holdout set.''',
SETUP,
BANK,
PIPE + r'''
train, val, test = week_split(bank, seed=42)
y = (bank["y"] == "yes").astype(int)
# Carve the practice envelope out of validation; the real test slice is never used here.
peek_idx, fresh_idx = train_test_split(val.index, train_size=2000, stratify=y.loc[val.index], random_state=7)
print(f"practice envelope {len(peek_idx):,} rows, fresh slice {len(fresh_idx):,} rows, real test {len(test):,} rows sealed")
check("the practice envelope and the fresh slice share no row", len(set(peek_idx) & set(fresh_idx)) == 0)
check("neither touches the sealed test slice", len((set(peek_idx) | set(fresh_idx)) & set(test.index)) == 0)''',
r'''md:## What does the junior's loop report?

Sixty versions, each a random list of 3 to 13 of today's columns, each fitted on train and scored on the practice envelope. The loop keeps whichever scored highest there.

**Predict before you run.** The best of the 60 on the practice envelope will sit how far above doing nothing on that slice? (a) below it (b) about one point (c) close to two points (d) ten points''',
r'''# The junior's loop: 60 column lists, each scored on the practice envelope; keep the best.
rng = np.random.default_rng(42)
rows = []
for k in range(60):
    cols = [str(c) for c in rng.choice(COLUMNS, size=int(rng.integers(3, 14)), replace=False)]
    m = logistic(cols, bank).fit(train[cols], y.loc[train.index])
    rows.append({"version": k, "n_cols": len(cols), "cols": cols,
                 "peek": accuracy_score(y.loc[peek_idx], m.predict(bank.loc[peek_idx, cols])),
                 "fresh": accuracy_score(y.loc[fresh_idx], m.predict(bank.loc[fresh_idx, cols]))})
runs = pd.DataFrame(rows)
best = runs.loc[runs["peek"].idxmax()]
base_peek = 1 - y.loc[peek_idx].mean()
base_fresh = 1 - y.loc[fresh_idx].mean()
print(f"doing nothing on the practice envelope: {base_peek:.4f}")
print(f"best of 60 on the practice envelope:    {best['peek']:.4f}  (version {best['version']}, {best['n_cols']} columns)")
print(f"edge as reported: {100 * (best['peek'] - base_peek):.2f} points")''',
r'''md:**What happened.** The answer is (c): the chosen version reads 0.9055 on the practice envelope, 1.8 points above doing nothing there. That is nearly double the edge case 2 measured honestly. Now score the same chosen version on rows nobody looked at.

**Predict before you run.** On the fresh 6,238 rows, the chosen version scores (a) about 0.906 again (b) about 0.897 (c) about 0.887 (d) about 0.80''',
r'''# Score the chosen version on the fresh slice, which played no part in the choice.
print(f"doing nothing on the fresh slice:   {base_fresh:.4f}")
print(f"the chosen version on the fresh slice: {best['fresh']:.4f}")
print(f"edge on fresh rows: {100 * (best['fresh'] - base_fresh):.2f} points, against {100 * (best['peek'] - base_peek):.2f} reported")
check("the reported score falls on fresh rows", best["fresh"] < best["peek"])
check("the chosen version is the maximum of the peeked scores", best["peek"] == runs["peek"].max())''',
r'''md:**What happened.** The answer is (b): 0.8971 on fresh rows, one point above doing nothing, which is exactly the honest edge from case 2. The extra 0.8 points were luck: among 60 versions scored on the same 2,000 rows, one was bound to be lucky on those rows, and the loop picked the luckiest.''',
r'''# Picture the peek: every version's peeked score, the chosen one, and where it lands on fresh rows.
fig, ax = plt.subplots(figsize=(10, 3.8))
order = runs.sort_values("peek").reset_index(drop=True)
ax.scatter(range(len(order)), order["peek"], color="#9C88F0", s=22, label="score on the practice envelope")
ax.scatter(range(len(order)), order["fresh"], color="#1C1B16", s=10, marker="x", label="same version on fresh rows")
ax.axhline(base_peek, color="#9A968C", ls="--"); ax.text(1, base_peek + 0.0008, "doing nothing", color="#6B675E")
i = len(order) - 1
ax.annotate("", xy=(i, order.loc[i, "fresh"]), xytext=(i, order.loc[i, "peek"]),
            arrowprops=dict(arrowstyle="->", color="#C0392B", lw=2))
ax.text(i - 1, order.loc[i, "peek"], "chosen: 0.906 ", ha="right", va="center", color="#C0392B")
ax.text(i - 1, order.loc[i, "fresh"] - 0.0015, "on fresh rows: 0.897 ", ha="right", color="#C0392B")
ax.set_xlabel("60 versions, sorted by their peeked score"); ax.set_ylabel("accuracy")
ax.legend(loc="lower right", fontsize=9); ax.set_title("Pick the best of 60 on one slice, and the best is partly luck")
plt.show()''',
r'''md:## Why does the peek inflate, and what is the rule?

The peeked scores spread out by chance alone, because 2,000 rows is a small sample. Their spread, next to their spread on the bigger fresh slice, shows how much luck a single slice carries.''',
r'''# How noisy is one slice? Compare the spread of the 60 scores on each slice.
spread_peek = runs["peek"].std()
spread_fresh = runs["fresh"].std()
print(f"spread of the 60 scores on the practice envelope: {spread_peek:.4f}")
print(f"spread of the 60 scores on the fresh slice:       {spread_fresh:.4f}")
print(f"the best peeked score sits {(best['peek'] - runs['peek'].mean()) / spread_peek:.1f} spreads above the average version")
check("the small slice is the noisier one", spread_peek > spread_fresh)''',
r'''md:**The rule.** Choose on validation, as often as you like. Score the test slice once, at the end, and report that one number with its seed. A test score used to choose anything becomes a second validation score, optimistic by however much the choosing bought.

**The envelope.** The trainer's card on the wall reads TEST SET, DO NOT OPEN UNTIL FRIDAY. Every request to peek this week points at it. On Friday it is opened once, the chosen model is scored once, and that number goes in the memo.

## What did this notebook establish?

| Question | Answer |
|---|---|
| What did the peek report? | 0.9055 on the practice envelope, 1.8 points above doing nothing |
| What did fresh rows say? | 0.8971, 1.0 point above doing nothing, the same as case 2 |
| Where did the extra 0.8 points come from? | choosing the luckiest of 60 versions on 2,000 rows |
| What is the rule? | the test slice is spent once; every choice is made on validation |

**Next:** the practice lab builds a second baseline of your own, writes Kalpa's repeat flag in SQL with a cutoff date, and tries to break the result.''',
]
make(NB + "C2_W05_D01_case03_the_peek_STUDENT.ipynb", cells)


# ---------------------------------------------------------------- guided
NB = str(DAY / "1_in_class_training_content" / "notebooks") + "/"
cells = [
r'''md:# Guided exercise: frame the call list, split it, score the baseline

You and the trainer build this together, one step at a time, during case 1. Each step has a TODO cell: replace the `None` with your answer and run the cell; the progress cell tells you which steps are done. The answer sits in the last cell. Try every step before you scroll to it.

What you will have at the end: a framed problem in three lines, the 13 input columns, a 0/1 target, the week's split with the seed stated, and the baseline accuracy every later model must beat.

**Search terms:** problem framing, train validation test split, stratify, random_state, DummyClassifier.''',
SETUP + r'''
import hashlib

def fingerprint(names):
    """A short code for a list of names, so the check can test your list without printing the answer."""
    return hashlib.md5(",".join(sorted(names)).encode()).hexdigest()[:10]

def todo_or(label, ok, value):
    """Print TODO while a step still holds None, then PASS or FAIL once it is filled."""
    if value is None:
        print("TODO  " + label)
    else:
        check(label, ok())
''',
BANK,
r'''# The picture to frame from: how the 41,188 calls ended.
counts = bank["y"].value_counts()
fig, ax = plt.subplots(figsize=(6, 3))
ax.barh(["no", "yes"], [counts["no"], counts["yes"]], color=["#9A968C", "#5B3FD6"])
for i, v in enumerate([counts["no"], counts["yes"]]):
    ax.text(v + 300, i, f"{v:,}", va="center")
ax.set_xlim(0, 42000); ax.set_title("How the bank's calls ended"); plt.show()''',
r'''md:## Step 1. Frame it in three lines

Write the input (what the bank knows), the target (what we score against) and the prediction time (the moment the score is made), each as a short phrase.''',
r'''# TODO: replace each None with a short phrase.
frame = {
    "input": None,            # what the bank knows about the client at the prediction time
    "target": None,           # the column we predict, and when it becomes known
    "prediction_time": None,  # the moment the score is made
}
print(frame)''',
r'''md:## Step 2. Pick the columns known at the prediction time

From the 20 input columns, list the ones the bank holds on the morning of the call: the client's profile and how this and earlier campaigns went. Today's answer has 13 names. Leave the other seven for Wednesday.''',
r'''# TODO: a list of 13 column names from bank.columns.
print(list(bank.columns))
KNOWN = None
print(KNOWN)''',
r'''md:## Step 3. Turn the target into 0 and 1''',
r'''# TODO: y should be 1 where bank["y"] is "yes" and 0 otherwise, as integers.
y = None
print(None if y is None else y.value_counts().to_dict())''',
r'''md:## Step 4. Split with a stated seed

Cut the test slice first, 20 percent, stratified on y, and seal it. Split what is left 75 to 25 into train and validation, stratified again. Use the week's seed, 42.''',
r'''# TODO: set SEED and build train_idx, val_idx, test_idx with train_test_split.
from sklearn.model_selection import train_test_split
SEED = None
train_idx = val_idx = test_idx = None
print(None if train_idx is None else (len(train_idx), len(val_idx), len(test_idx)))''',
r'''md:## Step 5. Score the baseline on validation

The baseline says "no" to every client. Its accuracy is the share of no in the validation slice.''',
r'''# TODO: the baseline's accuracy on the validation rows, as a number between 0 and 1.
baseline = None
print(baseline)''',
r'''# Progress: which steps are done?
todo_or("step 1: all three framing lines written", lambda: all(frame.values()), None if not all(frame.values()) else frame)
todo_or("step 2: the 13 columns known on the morning of the call", lambda: len(KNOWN) == 13 and fingerprint(KNOWN) == "0c9125ea0b", KNOWN)
todo_or("step 3: y has 4,640 ones", lambda: int(y.sum()) == 4640, y)
todo_or("step 4: 24,712 / 8,238 / 8,238 with seed 42", lambda: SEED == 42 and (len(train_idx), len(val_idx), len(test_idx)) == (24712, 8238, 8238), train_idx)
todo_or("step 5: baseline accuracy 0.8874", lambda: round(baseline, 4) == 0.8874, baseline)''',
r'''md:## The answer

Run this only after you have tried every step. It fills each step and runs the same progress checks.''',
r'''# The answer, step by step.
frame = {"input": "the client's profile and campaign history as of the morning of the call",
         "target": "y, yes or no, known once the call ends",
         "prediction_time": "the morning of the call, before anyone dials"}
KNOWN = ["age", "job", "marital", "education", "default", "housing", "loan",
         "contact", "month", "day_of_week", "campaign", "previous", "poutcome"]
y = (bank["y"] == "yes").astype(int)
SEED = 42
rest_idx, test_idx = train_test_split(bank.index, test_size=0.20, stratify=y, random_state=SEED)
train_idx, val_idx = train_test_split(rest_idx, test_size=0.25, stratify=y.loc[rest_idx], random_state=SEED)
baseline = float((y.loc[val_idx] == 0).mean())
print(f"split {len(train_idx):,} / {len(val_idx):,} / {len(test_idx):,}; baseline accuracy on validation {baseline:.4f}")

todo_or("step 1: all three framing lines written", lambda: all(frame.values()), frame)
todo_or("step 2: the 13 columns known on the morning of the call", lambda: len(KNOWN) == 13 and fingerprint(KNOWN) == "0c9125ea0b", KNOWN)
todo_or("step 3: y has 4,640 ones", lambda: int(y.sum()) == 4640, y)
todo_or("step 4: 24,712 / 8,238 / 8,238 with seed 42", lambda: SEED == 42 and (len(train_idx), len(val_idx), len(test_idx)) == (24712, 8238, 8238), train_idx)
todo_or("step 5: baseline accuracy 0.8874", lambda: round(baseline, 4) == 0.8874, baseline)''',
r'''md:**What the baseline proves.** Saying no to every client is right 88.74 percent of the time. A model that scores 0.88 has learned the share of no and nothing else; case 2 asks the logistic model to beat 0.8874 and measures by how much.''',
]
make(NB + "C2_W05_D01_guided_frame_and_split_STUDENT.ipynb", cells)


# ---------------------------------------------------------------- lab
D = str(DAY) + "/"

def cells(solution):
    T = lambda student, answer: answer if solution else student
    title = "Practice lab: whom to call, and whom to nudge" + (" (solutions)" if solution else "")
    return [
rf'''md:# {title}

The TA-led practice lab after the second block, and extra practice afterwards. It runs about 75 minutes with a TA and longer alone. Fill each TODO, run the cell, and read the progress line under it: TODO until you fill it, then PASS or FAIL.

| Step | What you do | Minutes |
|---|---|---|
| 1 | Read the situation and the six seats | 5 |
| 2 | Build: split, baseline, model on the bank's calls | 15 |
| 3 | Assignment: a second baseline of your own, a simple rule | 15 |
| 4 | Integration with Week 2: Kalpa's repeat flag in SQL, with a cutoff date | 20 |
| 5 | QA: try to break your own result | 10 |
| 6 | The five-line write-up | 10 |

**Search terms:** baseline model, rule-based baseline, label leakage, SQL window by date, sanity check with shuffled labels.''',
r'''md:## 1. The situation and the six seats

A Portuguese bank's campaign team (UCI Bank Marketing, 41,188 calls, CC BY 4.0) wants to rank clients so agents call the likeliest first. Kalpa Retail's Marketing wants the same shape of answer for its Rs 40 nudge: which members will buy again within ninety days. Kavya Nair, the senior analyst, wants the dumbest baseline before any model.

| Seat | The question this seat asks today |
|---|---|
| Business owner | Does the model change whom we call, and is that worth the build? |
| Product manager | What does the campaign team see, and when do they see it? |
| Solution architect | Where is the target computed, and as of which date? |
| Senior ML engineer (today's spotlight) | What is predicted, from what, known when; what is the bar; which rows score it? |
| Implementation engineer | Does the same split and the same score come out on every laptop? |
| QA and tester | What would break this number, and did we try it? |''',
SETUP + r'''
def todo_or(label, ok, value):
    """Print TODO while a step still holds None, then PASS or FAIL once it is filled."""
    if value is None:
        print("TODO  " + label)
    else:
        check(label, ok())
''',
BANK + r'''check("the bank file has 41,188 rows", len(bank) == 41188)''',
r'''md:## 2. Build: the split, the baseline, the model

The week's pipeline is loaded for you. Use seed 42 exactly as the class did, so your numbers match the room's.''',
PIPE + T(r'''
# TODO 2a: split the bank with week_split and seed 42.
train = val = test = None

# TODO 2b: the majority-class baseline's accuracy on validation (the share of "no").
baseline = None

# TODO 2c: fit logistic(COLUMNS, bank) on train and score its accuracy on validation at 0.5.
model_acc = None

todo_or("2a: validation has 8,238 rows", lambda: len(val) == 8238, val)
todo_or("2b: baseline 0.8874", lambda: round(baseline, 4) == 0.8874, baseline)
todo_or("2c: the model beats the baseline", lambda: model_acc > baseline, model_acc)''', r'''
# 2a: the week's split with seed 42.
train, val, test = week_split(bank, seed=42)
y_train = (train["y"] == "yes").astype(int)
y_val = (val["y"] == "yes").astype(int)

# 2b: the majority-class baseline on validation.
baseline = float((y_val == 0).mean())

# 2c: the logistic model on the 13 columns, scored at 0.5.
model = logistic(COLUMNS, bank).fit(train[COLUMNS], y_train)
model_acc = accuracy_score(y_val, model.predict(val[COLUMNS]))
print(f"baseline {baseline:.4f}, model {model_acc:.4f}")

todo_or("2a: validation has 8,238 rows", lambda: len(val) == 8238, val)
todo_or("2b: baseline 0.8874", lambda: round(baseline, 4) == 0.8874, baseline)
todo_or("2c: the model beats the baseline", lambda: model_acc > baseline, model_acc)'''),
r'''md:## 3. Assignment: a second baseline of your own

A baseline can be smarter than "say no to everyone". Write one rule a campaign manager could apply with no model at all, using one or two of the 13 columns, and score it on validation. Does it beat the majority class? Does it beat the model?

Pick your rule from what you know about the business before you look at any numbers, and write down why you expect it to work.''',
T(r'''# TODO 3: rule is a True/False Series over the validation rows: True means "call".
# Example shape (choose your own column and value): rule = val["some_column"] == "some_value"
rule = None
rule_acc = None if rule is None else accuracy_score((val["y"] == "yes").astype(int), rule.astype(int))
print(rule_acc)
todo_or("3: the rule is scored on all 8,238 validation rows", lambda: len(rule) == 8238, rule)''',
r'''# 3: call only clients whose previous campaign ended in success.
# Why expect it: a client who said yes to the bank before is the warmest lead an agent has.
rule = val["poutcome"] == "success"
rule_acc = accuracy_score(y_val, rule.astype(int))
print(f"rule calls {int(rule.sum())} clients; accuracy {rule_acc:.4f} against baseline {baseline:.4f} and model {model_acc:.4f}")
todo_or("3: the rule is scored on all 8,238 validation rows", lambda: len(rule) == 8238, rule)
check("this rule beats the majority class", rule_acc > baseline)
check("this one-line rule scores at least as well as the model on accuracy", rule_acc >= model_acc)'''),
r'''# Picture the three bars on validation: doing nothing, your rule, the model.
scores = {"call nobody": baseline, "your rule": rule_acc, "logistic model": model_acc}
shown = {k: v for k, v in scores.items() if v is not None}
if len(shown) < 3:
    print("Fill TODO 2 and 3 to draw the comparison; here is the bar every option must clear:", round(0.8874, 4))
    shown = {"call nobody (from class)": 0.8874}
fig, ax = plt.subplots(figsize=(8, 3.4))
ax.barh(list(shown), list(shown.values()), color=["#9A968C", "#C98A00", "#5B3FD6"][:len(shown)])
for i, v in enumerate(shown.values()):
    ax.text(v + 0.0005, i, f"{v:.4f}", va="center")
ax.set_xlim(0.88, 0.905); ax.set_xlabel("accuracy on validation (axis starts at 0.88)")
ax.set_title("Three ways to choose whom to call")
plt.show()''',
r'''md:## 4. Integration with Week 2: Kalpa's repeat flag in SQL, with a cutoff date

The Codespace's Postgres warehouse (loaded by `.devcontainer/load_warehouse.sh`) holds Kalpa Retail's `orders` table from Week 2: one row per order, with `customer_id`, `order_date`, `amount` and `status`. The helper below runs a query there; if no Postgres server answers, it loads the same warehouse file into an in-memory SQLite database and runs the same SQL, so the numbers are identical either way.

The prediction time is 30 June 2026. The target is: at least one delivered order in the ninety days after it, 1 July to 28 September.''',
r'''# Run SQL against the Codespace warehouse, or against the same file in memory if no server answers.
import os, sqlite3, subprocess, shutil

WAREHOUSE = pathlib.Path("../../../W02/D1/data/C2_W02_D01_warehouse_v4_STUDENT.sql")

def from_postgres(sql):
    if not shutil.which("psql"):
        return None
    env = dict(os.environ, PGHOST=os.environ.get("PGHOST", "localhost"), PGUSER=os.environ.get("PGUSER", "postgres"),
               PGPASSWORD=os.environ.get("PGPASSWORD", "postgres"), PGDATABASE=os.environ.get("PGDATABASE", "kalpa"))
    r = subprocess.run(["psql", "-X", "--csv", "-c", sql], capture_output=True, text=True, env=env, timeout=60)
    return pd.read_csv(io.StringIO(r.stdout)) if r.returncode == 0 else None

def sqlite_copy():
    """The warehouse file's orders block, loaded into SQLite in memory; nothing is written to disk."""
    text = WAREHOUSE.read_text(encoding="utf-8")
    block = text.split("COPY orders")[1].split("\\.")[0].splitlines()[1:]
    rows = [line.split("\t") for line in block if line.strip()]
    db = sqlite3.connect(":memory:")
    pd.DataFrame(rows, columns=["order_id", "customer_id", "order_date", "quarter", "channel", "amount", "status"]) \
      .astype({"amount": float}).to_sql("orders", db, index=False)
    return db

def run_sql(sql):
    out = from_postgres(sql)
    if out is not None:
        print("ran on Postgres")
        return out
    print("no Postgres server answered, so the same SQL ran on SQLite in memory")
    return pd.read_sql_query(sql, sqlite_copy())

n = run_sql("select count(*) as orders, min(order_date) as first_day, max(order_date) as last_day from orders")
print(n.to_string(index=False))
check("the warehouse answered with 1,000 orders", int(n.loc[0, "orders"]) == 1000)''',
r'''md:**The naive version, first.** A hurried analyst writes the flag on the whole table: a member "repeats" if they have more than one delivered order, and the feature is their order count. Run it and look at the two columns side by side.''',
r'''# The naive flag: written on the whole log, with no cutoff date.
naive = run_sql("""
    select customer_id,
           count(*) as orders_ever,
           case when count(*) > 1 then 1 else 0 end as repeat_naive
    from orders
    where status = 'delivered'
    group by customer_id
""")
rule_says = (naive["orders_ever"] >= 2).astype(int)
print(f"{len(naive)} members; a 'model' that reads orders_ever is right {(rule_says == naive['repeat_naive']).mean():.0%} of the time")
check("the naive feature predicts the naive flag perfectly", (rule_says == naive["repeat_naive"]).all())''',
r'''md:**The leak, named.** The naive flag and its feature count the same orders, including orders placed after any date Marketing could nudge on, so the feature contains the answer and any model reading it scores 100 percent. It is the chapter 2 trap at warehouse scale. Now write the honest version: inputs from orders on or before 30 June, the target from the window after it.''',
T(r'''# TODO 4: write the honest query. One row per member who had a delivered order on or before 2026-06-30, with
#   orders_before   delivered orders on or before 2026-06-30
#   last_before     the date of the latest of those orders
#   repeat_90d      1 if the member has a delivered order after 2026-06-30 and on or before 2026-09-28, else 0
HONEST_SQL = None
honest = None if HONEST_SQL is None else run_sql(HONEST_SQL)
print(None if honest is None else honest.head())
todo_or("4: one row per member with history, and the window flag", lambda: len(honest) == 205 and int(honest["repeat_90d"].sum()) == 110, honest)''',
r'''# 4: the honest query, with the cutoff and the window written as literal dates.
HONEST_SQL = """
    with hist as (
        select customer_id, count(*) as orders_before, max(order_date) as last_before
        from orders
        where status = 'delivered' and order_date <= '2026-06-30'
        group by customer_id),
    win as (
        select distinct customer_id
        from orders
        where status = 'delivered' and order_date > '2026-06-30' and order_date <= '2026-09-28')
    select h.customer_id, h.orders_before, h.last_before,
           case when w.customer_id is null then 0 else 1 end as repeat_90d
    from hist h left join win w on w.customer_id = h.customer_id
    order by h.customer_id
"""
honest = run_sql(HONEST_SQL)
honest["days_since_last"] = (pd.Timestamp("2026-06-30") - pd.to_datetime(honest["last_before"])).dt.days
print(honest.head().to_string(index=False))
print(f"{len(honest)} members with history; {int(honest['repeat_90d'].sum())} bought again in the window, share {honest['repeat_90d'].mean():.3f}")
todo_or("4: one row per member with history, and the window flag", lambda: len(honest) == 205 and int(honest["repeat_90d"].sum()) == 110, honest)'''),
T(r'''# TODO 4b: Kalpa's majority-class baseline on this flag. Which class is the majority here, and what does it score?
kalpa_baseline = None
todo_or("4b: the majority-class baseline on Kalpa's flag", lambda: round(kalpa_baseline, 3) == 0.537, kalpa_baseline)''',
r'''# 4b: here the majority class is "buys again", so the dumbest model nudges everyone.
share = honest["repeat_90d"].mean()
kalpa_baseline = max(share, 1 - share)
print(f"majority class: {'buys again' if share > 0.5 else 'does not'}; baseline accuracy {kalpa_baseline:.3f}")
rule_kalpa = (honest["orders_before"] >= 2).astype(int)
print(f"a rule, 'nudge members with two or more orders before the cutoff': accuracy {(rule_kalpa == honest['repeat_90d']).mean():.3f}")
todo_or("4b: the majority-class baseline on Kalpa's flag", lambda: round(kalpa_baseline, 3) == 0.537, kalpa_baseline)'''),
r'''md:## 5. QA: try to break your own result

Two attacks a tester would run. First, shuffle the target in the training rows: a model that learns from noise should fall back to the baseline, and if it does not, something leaks. Second, change the seed: the edge over the baseline should stay roughly where it was, and how far it moves tells you how much of the edge is luck.''',
T(r'''# TODO 5: (a) fit the model on train with y_train shuffled (np.random.default_rng(0).permutation) and score it on validation;
#         (b) rebuild the split with seed 7 and score the baseline and the model again.
shuffled_acc = None
seed7_edge = None
todo_or("5a: the shuffled-label model scores no better than the baseline plus 0.002", lambda: shuffled_acc <= baseline + 0.002, shuffled_acc)
todo_or("5b: the seed-7 edge is still positive", lambda: seed7_edge > 0, seed7_edge)''',
r'''# 5a: shuffled labels, so the columns carry no signal about the target.
y_shuffled = pd.Series(np.random.default_rng(0).permutation(y_train.values), index=y_train.index)
shuffled_acc = accuracy_score(y_val, logistic(COLUMNS, bank).fit(train[COLUMNS], y_shuffled).predict(val[COLUMNS]))
# 5b: the same build on a different seed.
tr7, va7, _ = week_split(bank, seed=7)
y_tr7, y_va7 = (tr7["y"] == "yes").astype(int), (va7["y"] == "yes").astype(int)
acc7 = accuracy_score(y_va7, logistic(COLUMNS, bank).fit(tr7[COLUMNS], y_tr7).predict(va7[COLUMNS]))
seed7_edge = acc7 - (y_va7 == 0).mean()
print(f"shuffled labels: {shuffled_acc:.4f} against baseline {baseline:.4f}")
print(f"seed 7: model {acc7:.4f}, baseline {(y_va7 == 0).mean():.4f}, edge {100 * seed7_edge:.2f} points (seed 42: {100 * (model_acc - baseline):.2f})")
todo_or("5a: the shuffled-label model scores no better than the baseline plus 0.002", lambda: shuffled_acc <= baseline + 0.002, shuffled_acc)
todo_or("5b: the seed-7 edge is still positive", lambda: seed7_edge > 0, seed7_edge)'''),
T(r'''md:## 6. The five-line write-up

Write five lines for Kavya in the shape the programme uses. Use your own numbers from this notebook.

1. **Claim:** TODO
2. **Evidence:** TODO
3. **Caveat:** TODO
4. **Action:** TODO
5. **Next check:** TODO''',
r'''md:## 6. The five-line write-up (a model answer)

1. **Claim:** on the bank's validation slice the logistic model beats calling nobody by about one point of accuracy (0.8971 against 0.8874), and a one-line rule, call clients whose last campaign succeeded, does as well (0.8988).
2. **Evidence:** the same seed-42 split as the class; the shuffled-label model falls to the baseline, so nothing leaks; seed 7 keeps a positive edge of similar size.
3. **Caveat:** accuracy on a 89 to 11 split rewards saying no; the random split mixes 2008 with 2010; and Kalpa's own flag (110 of 205 members, 0.537) has the opposite majority.
4. **Action:** ship the rule as the Friday baseline for the campaign team and keep the model in validation until it beats the rule on the measure Tuesday chooses.
5. **Next check:** Tuesday's count of how many of the 928 yes clients each option actually puts on the call list.'''),
    ]

make(D + "2_take_home_mandatory/C2_W05_D01_practice_lab_STUDENT.ipynb", cells(False))
make(D + "4_trainer_only/C2_W05_D01_practice_lab_solutions_TRAINER.ipynb", cells(True))


# Test inputs and expected outcomes
# --------------------------------
# python3 content/W05/D1/4_trainer_only/C2_W05_D01_build_notebooks_INTERNAL.py
#     Prints each notebook's outputs and "OK <name>" twelve times, and every notebook in the pack is
#     rewritten with fresh outputs: 59 PASS lines in all and no FAIL.
# The same run with PGPORT=5999 (no Postgres server)
#     The lab notebooks print "no Postgres server answered, so the same SQL ran on SQLite in memory"
#     and the same 205 members and 110 repeaters.
