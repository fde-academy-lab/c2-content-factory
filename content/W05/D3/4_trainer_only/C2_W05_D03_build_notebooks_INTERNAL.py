"""Build and execute every notebook of W05/D3 (feature engineering and leakage).

Usage, from the repository root:
    python3 content/W05/D3/4_trainer_only/C2_W05_D03_build_notebooks_INTERNAL.py            # all
    python3 content/W05/D3/4_trainer_only/C2_W05_D03_build_notebooks_INTERNAL.py case01 ch03 # some

Each notebook is assembled from the cells below with scripts/nb_make.py and executed in its own
folder, so the saved outputs are the ones a learner sees on GitHub. Every data notebook downloads
its public file into ~/.cache/c2_datasets and writes nothing into the repository.
"""
import pathlib
import sys
import textwrap

ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from nb_make import md, code, build  # noqa: E402

DAY = ROOT / "content" / "W05" / "D3"
NB = DAY / "1_in_class_training_content" / "notebooks"
LAB = DAY / "2_take_home_mandatory"
TRAINER = DAY / "4_trainer_only"

STYLE = '''import warnings
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.rcParams.update({"figure.dpi": 110, "font.size": 11, "axes.spines.top": False,
                     "axes.spines.right": False})
INK, VIOLET, ROSE, GREEN, GREY = "#1A0F5C", "#5B3FD6", "#D63A6A", "#1F8A5B", "#A9A3D2"

def check(label, ok):
    """Print one line that starts PASS or FAIL, and keep the notebook running either way."""
    print(("PASS  " if ok else "FAIL  ") + label)
'''

# STYLE indented to sit inside an indented cell string, so nb_make's dedent keeps working.
STYLE8 = textwrap.indent(STYLE, " " * 8)

# The week's shared pipeline (docs/detailing/W05_research/W05_week_pipeline.md), copied into the
# first cells of every case notebook so the five days quote the same numbers.
PIPELINE = STYLE + '''
# The Week 5 pipeline every case notebook starts from: the same file, columns, split and baseline.
import io, zipfile, pathlib, urllib.request
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, accuracy_score, confusion_matrix

CACHE = pathlib.Path.home() / ".cache" / "c2_datasets"
CACHE.mkdir(parents=True, exist_ok=True)

def load_bank():
    """UCI Bank Marketing, bank-additional-full.csv (CC BY 4.0), cached after the first download."""
    f = CACHE / "bank-additional-full.csv"
    if not f.exists():
        url = "https://archive.ics.uci.edu/static/public/222/bank+marketing.zip"
        outer = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(url, timeout=60).read()))
        inner = zipfile.ZipFile(io.BytesIO(outer.read("bank-additional.zip")))
        f.write_bytes(inner.read("bank-additional/bank-additional-full.csv"))
    return pd.read_csv(f, sep=";")

# The customer table on the morning of the call: who the client is and how earlier campaigns went.
PROFILE = ["age", "job", "marital", "education", "default", "housing", "loan"]
HISTORY = ["contact", "month", "day_of_week", "campaign", "previous", "poutcome"]
# Joined on Wednesday from other feeds: the call log and the economic indicators.
CALL_LOG = ["duration"]
ECONOMY = ["emp.var.rate", "cons.price.idx", "cons.conf.idx", "euribor3m", "nr.employed"]

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

# Today's scorer: AUC, accuracy and the matrix at 0.5, then Tuesday's call bill at 40 / 1,240.
SCORER = '''
CALL_RS, MISSED_RS = 40, 1200            # Tuesday's costs: one call, one missed buyer's margin
THRESHOLD = CALL_RS / (CALL_RS + MISSED_RS)

def score(columns, tr=None, va=None):
    """Fit on training rows, score validation rows, and return the numbers the day quotes."""
    tr = train if tr is None else tr
    va = val if va is None else va
    ytr, yva = (tr["y"] == "yes").astype(int), (va["y"] == "yes").astype(int)
    model = logistic(columns, tr).fit(tr[columns], ytr)
    p = model.predict_proba(va[columns])[:, 1]
    tn, fp, fn, tp = confusion_matrix(yva, (p >= 0.5).astype(int)).ravel()
    tn2, fp2, fn2, tp2 = confusion_matrix(yva, (p >= THRESHOLD).astype(int)).ravel()
    top = yva.values[np.argsort(-p)[:1000]].sum()
    return {"columns": len(columns), "AUC": round(roc_auc_score(yva, p), 4),
            "accuracy": round(accuracy_score(yva, (p >= 0.5).astype(int)), 4),
            "TP": tp, "FP": fp, "FN": fn, "recall": round(tp / (tp + fn), 3),
            "bill_Rs": int(fp2 * CALL_RS + fn2 * MISSED_RS), "buyers_in_top_1000": int(top)}, model, p
'''

LOAD = '''
bank = load_bank()
train, val, test = week_split(bank)
y_train = (train["y"] == "yes").astype(int)
y_val = (val["y"] == "yes").astype(int)
print(f"{len(bank):,} calls: train {len(train):,}, validation {len(val):,}, "
      f"test {len(test):,} (sealed until Friday)")
print(f"Base rate: {y_train.mean():.2%} of training calls ended in a deposit")
'''

ENGINEER = '''
def engineer(df):
    """Wednesday's feature work on the bank's file: the 999 sentinel split into a flag and a number."""
    out = df.copy()
    out["never_contacted"] = (out["pdays"] == 999).astype(int)
    out["days_since_contact"] = out["pdays"].where(out["pdays"] != 999, 0)
    return out

bank = engineer(bank)
train, val, test = week_split(bank)
CUSTOMER = PROFILE + HISTORY
HONEST = CUSTOMER + ["never_contacted", "days_since_contact"] + ECONOMY
'''


def case01():
    cells = [
        md("""
        # Case 1: The junior's join: why did the score jump?
        *Applies: Feature engineering from the customer table: ratios, recency, counts, cohort age,
        basket signals · Encoding categoricals; scaling numerics; which models care*

        A Portuguese bank rang 41,188 clients between May 2008 and November 2010 to sell a term
        deposit, and the week's model ranks whom to ring. On Monday and Tuesday it read the customer
        table alone and scored a validation AUC of 0.76. Overnight a junior on the team joins two more
        feeds to that table: the economic indicators the bank's research desk keeps, and the call log.
        The score jumps. Before anyone celebrates, you measure what each join added and read the jump
        through recall and the call bill, because accuracy will barely move.

        **Who needs the answer.** The campaign head, who decides whom the call centre rings next
        month, and Kavya Nair, Kalpa's senior analyst, who signs off the same method for Kalpa's nudge.

        **The questions on the way.** What does the week's pipeline give us before the join? What
        does each join add? Why does accuracy hide the jump? What does the jump promise in rupees?
        Where do the encoder and the scaler learn their numbers?

        **You will be able to** score three feature sets on one split, read a jump through AUC,
        recall and the bill, and show that the pipeline's encoder and scaler learn from training rows only.

        **Search terms:** feature engineering for machine learning, sklearn ColumnTransformer,
        one-hot encoding, StandardScaler pipeline.
        """),
        md("""
        ## What does the week's pipeline give us before the join?
        The cell below is the week's shared code. It downloads the bank's file once into a cache in
        your home folder, seals 20 percent of the rows as the test set (the envelope on the wall),
        and splits the rest 75 to 25 into training and validation rows with seed 42. The customer
        table is the 13 columns known about a client on the morning of a call. The scorer at the end
        is today's addition: it reports AUC, accuracy, recall, Tuesday's call bill at the threshold
        40 / 1,240 = 0.032, and how many buyers sit in the top 1,000 scores.
        """),
        code(PIPELINE + SCORER + LOAD),
        code('''
        check("41,188 calls loaded from the public file", len(bank) == 41188)
        check("train, validation and test are 24,712, 8,238 and 8,238 rows",
              (len(train), len(val), len(test)) == (24712, 8238, 8238))
        check("the base rate sits between 11 and 12 percent", 0.11 < y_train.mean() < 0.12)
        '''),
        md("""
        ## What does each join add?
        Three feature sets go in, one after another: the customer table (13 columns), the customer
        table plus the five economic columns, and both plus the one call-log column, `duration`.

        **Predict before you run.** The customer table scores 0.76. What do the two joins add?
        (A) about 0.01 each; (B) the economy about 0.03 and the call log about 0.14; (C) the economy
        about 0.14 and the call log about 0.03; (D) nothing, since the model already knows the client.
        """),
        code('''
        SETS = {"customer table": PROFILE + HISTORY,
                "+ economy": PROFILE + HISTORY + ECONOMY,
                "+ economy + call log": PROFILE + HISTORY + ECONOMY + CALL_LOG}
        results = {}
        for name, cols in SETS.items():
            results[name], _, _ = score(cols)
        table = pd.DataFrame(results).T[["columns", "AUC", "accuracy", "recall", "bill_Rs", "buyers_in_top_1000"]]
        table
        '''),
        md("""
        **What happened.** B. AUC climbs from 0.761 to 0.795 with the economy and to 0.932 with the
        call log, a jump of 0.14 from one column. Accuracy at 0.5 moves from 0.897 to 0.907, one
        point, because 88.7 percent of calls end in no and calling nobody already scores 0.887. A
        jump this size from a single column is the first thing a senior doubts; case 2 asks whether
        that column could ever exist when the call list is made.
        """),
        code('''
        fig, axes = plt.subplots(1, 2, figsize=(10, 3.6))
        names = list(table.index)
        colours = [GREY, VIOLET, ROSE]
        axes[0].bar(names, table["AUC"].astype(float), color=colours)
        axes[0].set_ylim(0.5, 1.0); axes[0].set_title("Validation AUC: the ranking jumps")
        axes[1].bar(names, table["accuracy"].astype(float), color=colours)
        axes[1].axhline(0.8874, color=INK, ls="--", lw=1); axes[1].text(-0.4, 0.889, "call nobody: 0.887", fontsize=9)
        axes[1].set_ylim(0.5, 1.0); axes[1].set_title("Accuracy at 0.5: one point")
        for ax, col in zip(axes, ["AUC", "accuracy"]):
            for i, v in enumerate(table[col].astype(float)):
                ax.text(i, v + 0.01, f"{v:.3f}", ha="center", fontsize=10)
            ax.tick_params(axis="x", labelsize=9)
        plt.tight_layout(); plt.show()
        '''),
        md("""
        ## Why does accuracy hide the jump, and what does the jump promise in rupees?
        Accuracy counts right answers at one cut, and nine in ten answers are an easy no. The
        decision lives elsewhere: whom to ring. Read the jump through three numbers the campaign head
        uses: recall at 0.5 (of the buyers, how many the list finds), the call bill at Tuesday's
        threshold (every call Rs 40, every missed buyer Rs 1,200 of lost margin), and the buyers
        found if the centre can ring only 1,000 people.

        **Predict before you run.** On these 8,238 validation calls, the third feature set's bill is
        (A) about the same as the customer table's; (B) about Rs 1.6 lakh lower; (C) higher, because
        it calls more people.
        """),
        code('''
        bill = table[["recall", "bill_Rs", "buyers_in_top_1000"]].copy()
        bill["bill_lakh"] = (bill["bill_Rs"].astype(float) / 1e5).round(2)
        saved = int(bill.loc["+ economy", "bill_Rs"] - bill.loc["+ economy + call log", "bill_Rs"])
        print(f"The call-log join promises Rs {saved/1e5:.2f} lakh less on 8,238 calls, "
              f"and {int(bill.loc['+ economy + call log', 'buyers_in_top_1000']) - int(bill.loc['+ economy', 'buyers_in_top_1000'])} "
              f"more buyers in the top 1,000.")
        bill
        '''),
        md("""
        **What happened.** B. Recall at 0.5 nearly doubles, from 0.23 to 0.42, and the bill falls
        from about Rs 2.80 lakh to about Rs 1.19 lakh, a promise of Rs 1.61 lakh saved on 8,238
        calls. That promise is what a junior would take to the campaign head. Whether the bank can
        collect it depends on one fact about one column, which case 2 checks.
        """),
        md("""
        ## Where do the encoder and the scaler learn their numbers?
        This is the implementation engineer's question. The pipeline's scaler learns each numeric
        column's mean and spread, and the one-hot encoder learns each column's list of categories,
        when `fit` is called on training rows. Validation and test rows are transformed with those
        training numbers. A hurried analyst scales the whole file first and splits afterwards, so
        the sealed test rows quietly shape every feature: a small leak through the split, and the
        habit that later lets bigger ones through.

        **Predict before you run.** How many rows did the fitted scaler see? (A) 41,188; (B) 32,950;
        (C) 24,712.
        """),
        code('''
        _, model, _ = score(SETS["+ economy"])
        scaler = model.named_steps["prep"].named_transformers_["num"]
        encoder = model.named_steps["prep"].named_transformers_["cat"]
        num_cols = model.named_steps["prep"].transformers_[0][2]
        print("rows the scaler saw:", int(scaler.n_samples_seen_))
        print("job categories the encoder learned:", len(encoder.categories_[0]), list(encoder.categories_[0])[:5], "...")
        hurried = StandardScaler().fit(bank[num_cols])          # the trap: all rows, test included
        compare = pd.DataFrame({"mean from training rows": scaler.mean_.round(3),
                                "mean from all rows": hurried.mean_.round(3)}, index=num_cols)
        compare.head(5)
        '''),
        md("""
        **What happened.** C. The scaler saw the 24,712 training rows and nothing else, and the
        encoder learned 12 job categories, `unknown` among them, from the same rows. The means from
        all rows differ only in the second or third decimal on this file, which is why the habit
        looks harmless; on a file where the future differs from the past, the same habit carries the
        future into training. The rule: every encoder and scaler sits inside the pipeline and is fitted
        on training rows only.
        """),
        code('''
        check("adding the economy lifts AUC", results["+ economy"]["AUC"] > results["customer table"]["AUC"])
        check("the call-log join lifts AUC by more than 0.10",
              results["+ economy + call log"]["AUC"] - results["+ economy"]["AUC"] > 0.10)
        check("accuracy moves by less than 0.02 across all three sets",
              table["accuracy"].astype(float).max() - table["accuracy"].astype(float).min() < 0.02)
        check("the scaler was fitted on training rows only", int(scaler.n_samples_seen_) == len(train))
        '''),
        md("""
        ## What does case 1 hand to case 2?
        | Feature set | Columns | Validation AUC | Recall at 0.5 | Bill at 0.032 |
        |---|---|---|---|---|
        | Customer table | 13 | 0.761 | 0.19 | about Rs 2.79 lakh |
        | + economy | 18 | 0.795 | 0.23 | about Rs 2.80 lakh |
        | + economy + call log | 19 | 0.932 | 0.42 | about Rs 1.19 lakh |

        Every join lifted the score and the last one lifted it most. Case 2 asks the prediction-time
        question of every column: on the morning the call list is made, is this value known?
        """),
    ]
    build(NB / "C2_W05_D03_case01_the_junior_join_STUDENT.ipynb", cells, timeout=600)


def case02():
    cells = [
        md("""
        # Case 2: Every column on the timeline: known before the call?
        *Applies: Leakage and the prediction-time question · The column audit · Feature engineering
        from the customer table (the 999 sentinel)*

        Case 1 ended on a promise: the call-log join cuts the bill on 8,238 validation calls from
        about Rs 2.80 lakh to about Rs 1.19 lakh. This notebook asks one question of every column
        before that promise reaches the campaign head: on the morning the call list is made, do we
        know this value for this client?

        **Who needs the answer.** The campaign head, who would plan next month's calls on the
        promise; the solution architect, who decides which feeds the scoring service may read; and
        Kavya, who will ask the same question of Kalpa's payments feed.

        **The questions on the way.** What does the call log know, and when is it written? Which
        columns pass the prediction-time question? Do the economic columns carry the economy or the
        calendar? How well does the model rank clients inside one month? What do `poutcome` and
        `pdays` need? What is the honest score, and what did the leak promise in rupees? Where does
        Kalpa hide the same leak?

        **You will be able to** run the prediction-time question on every column, write the audit
        table with a verdict and a reason per column, split a sentinel into a flag and a number, and
        ship the honest score with its bill.

        **Search terms:** data leakage in machine learning, target leakage, feature audit, leakage
        checklist, train test contamination.
        """),
        md("""
        ## What does the pipeline give us again?
        The week's shared code, reloaded, plus today's scorer from case 1.
        """),
        code(PIPELINE + SCORER + LOAD),
        md("""
        ## What does the call log know, and when is it written?
        `duration` is the length of the last call in seconds. Split the calls into five equal groups
        by length and look at how many in each group said yes.

        **Predict before you run.** The shortest fifth of calls ends in a deposit (A) about 11
        percent of the time, like everyone; (B) about 0.5 percent of the time; (C) about 33 percent
        of the time.
        """),
        code('''
        fifths = pd.qcut(bank["duration"], 5)
        by_length = bank.groupby(fifths, observed=True)["y"].apply(lambda s: (s == "yes").mean()).round(3)
        print("yes-rate by call length, shortest fifth first:")
        print(by_length.to_string())
        zero = bank.loc[bank["duration"] == 0, "y"].value_counts()
        print("\\ncalls of 0 seconds and how they ended:", zero.to_dict())
        '''),
        md("""
        **What happened.** B. The shortest fifth converts at 0.5 percent and the longest at 33
        percent, and every one of the four calls of zero seconds ended in no. A long call is often
        the sale itself being made. The dataset's own documentation says the same about this
        column: the length of a call strongly shapes the outcome, a call of zero seconds always
        ends in no, nobody knows a call's length before dialling, and so the column belongs in
        benchmarks and out of any model meant to make real predictions (UCI Bank Marketing page,
        `duration` row of the variables table, verified 28 October 2026). The column is written
        when the call ends, after the moment the list is made.
        """),
        code('''
        fig, ax = plt.subplots(figsize=(10, 2.6))
        ax.axvline(0, color=INK, lw=2)
        ax.text(0.05, 1.18, "the call list is made", color=INK, fontsize=10)
        known = {"age, job, marital": -400, "previous, poutcome": -120, "economy (published)": -30,
                 "contact, month": -1}
        later = {"duration (call ends)": 3}
        for i, (name, t) in enumerate(known.items()):
            ax.plot(np.sign(t) * np.log10(abs(t) + 1), 0.4 + 0.25 * (i % 3), "o", color=GREEN, ms=9)
            ax.text(np.sign(t) * np.log10(abs(t) + 1), 0.52 + 0.25 * (i % 3), name, ha="center", fontsize=9)
        for name, t in later.items():
            ax.plot(np.log10(t + 1), 0.6, "o", color=ROSE, ms=11)
            ax.text(np.log10(t + 1), 0.72, name, ha="center", fontsize=10, color=ROSE)
        ax.axvspan(0, 3.2, color=ROSE, alpha=0.06)
        ax.text(1.6, 0.12, "after the prediction moment: the model may not read it", ha="center", color=ROSE, fontsize=9)
        ax.set_xlim(-3.2, 3.2); ax.set_ylim(0, 1.3); ax.set_yticks([])
        ax.set_xticks([-2.6, -1.5, 0, 1.5, 2.6]); ax.set_xticklabels(["a year before", "weeks before", "now", "minutes after", "months after"])
        ax.set_title("When each column is written, against the moment the call list is made")
        plt.tight_layout(); plt.show()
        '''),
        md("""
        ## Which columns pass the prediction-time question?
        The audit asks four things of every column: which system writes it, when it is written
        against the moment the call list is made, whether it is known that morning, and the verdict
        with its reason. The table below is the audit of all 20 input columns of the bank's file.
        """),
        code('''
        A = [  # column, written by, when it is written, known before the call, verdict, reason
         ("age, job, marital, education", "client file", "at account opening", "yes", "keep", "who the client is"),
         ("default, housing, loan", "credit file", "before the campaign", "yes", "keep", "the client's other products"),
         ("contact", "dialler", "when the call is planned", "yes", "keep", "the channel chosen for the call"),
         ("month, day_of_week", "dialler", "the day of the call", "yes", "keep, flag", "a calendar stamp; see the next section"),
         ("campaign", "dialler", "counts calls up to this one", "yes", "keep", "how often we have rung this campaign"),
         ("previous, poutcome", "campaign history", "when the last campaign closed", "yes", "keep", "how earlier campaigns went"),
         ("pdays", "campaign history", "when the last campaign closed", "yes", "engineer", "999 means never contacted"),
         ("duration", "call log", "when the call ends", "no", "drop", "written after the moment of prediction"),
         ("emp.var.rate, nr.employed", "research desk", "quarterly", "ask the owner", "keep, flag", "publication date not verified"),
         ("cons.price.idx, cons.conf.idx", "research desk", "monthly", "ask the owner", "keep, flag", "publication date not verified"),
         ("euribor3m", "research desk", "daily", "yes", "keep, flag", "moves with the other rates"),
        ]
        audit = pd.DataFrame(A, columns=["columns", "written by", "written when", "known before the call",
                                         "verdict", "reason"])
        audit
        '''),
        md("""
        **What happened.** One column fails outright: `duration`, written by the call log when the
        call ends. Three sets carry a flag. The quarterly and monthly indicators pass only if each
        figure was published before the call it sits beside, which is a question for the data owner
        and is marked not verified here. The calendar columns pass the question and still need the
        next section, because a column can be known that morning and still let the score borrow
        from the split.
        """),
        md("""
        ## Do the economic columns carry the economy, or the calendar?
        The file runs in date order from May 2008 to November 2010, so the year can be rebuilt from
        the order of the months. The economic columns take very few values, which is the first clue.

        **Predict before you run.** A model given only the year and month of each call, and nothing
        about the client, scores a validation AUC of (A) about 0.50, a coin; (B) about 0.65;
        (C) about 0.79, close to the full honest model.
        """),
        code('''
        print("distinct values:", bank[ECONOMY].nunique().to_dict())
        order = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
        m = bank["month"].map({x: i + 1 for i, x in enumerate(order)})
        bank["year"] = 2008 + (m.diff().fillna(0) < 0).cumsum()
        bank["year_month"] = bank["year"].astype(str) + "-" + m.astype(str).str.zfill(2)
        train, val, test = week_split(bank)
        print("yes-rate by year:", bank.groupby("year")["y"].apply(lambda s: round((s == "yes").mean(), 3)).to_dict())
        calendar, _, _ = score(["year_month"])
        print("AUC from year and month alone:", calendar["AUC"])
        '''),
        code('''
        rate = bank.groupby("year_month")["y"].apply(lambda s: (s == "yes").mean())
        eur = bank.groupby("year_month")["euribor3m"].mean()
        fig, ax = plt.subplots(figsize=(10, 3.4))
        ax.bar(range(len(rate)), rate.values, color=VIOLET, alpha=0.75, label="share of calls that said yes")
        ax2 = ax.twinx(); ax2.plot(range(len(eur)), eur.values, color=ROSE, lw=2, label="euribor3m (right axis)")
        ax.set_xticks(range(0, len(rate), 3)); ax.set_xticklabels(rate.index[::3], rotation=45, fontsize=8)
        ax.set_ylabel("yes-rate"); ax2.set_ylabel("euribor3m")
        ax.set_title("The yes-rate moves with the month, and the rate column marks the month")
        ax.set_ylim(0, 0.85); ax2.set_ylim(0, 6.5)
        fig.legend(loc="upper center", bbox_to_anchor=(0.5, 0.86), ncol=2, fontsize=9)
        plt.tight_layout(); plt.show()
        '''),
        md("""
        **What happened.** C. The year and month alone score about 0.79, against 0.795 for the
        customer table plus the economy. The yes-rate runs from about 5 percent of calls in 2008 to
        about 52 percent in 2010, and `emp.var.rate` and `nr.employed` take only 10 and 11 distinct
        values, so they act as a stamp for the quarter. On a random split every month sits in both
        training and validation, so the model is scored partly on months it has already seen. Next
        month's call list is a month it has never seen.
        """),
        md("""
        ## How well does the model rank clients inside one month?
        The call centre ranks one month's list at a time, so the ranking that matters is the one
        inside a month, where the calendar cannot help.

        **Predict before you run.** Inside a single month the honest model's AUC is (A) about 0.80
        as before; (B) about 0.57; (C) below 0.5.
        """),
        code('''
        bank = bank.assign(never_contacted=(bank["pdays"] == 999).astype(int),
                           days_since_contact=bank["pdays"].where(bank["pdays"] != 999, 0))
        train, val, test = week_split(bank)
        HONEST = PROFILE + HISTORY + ["never_contacted", "days_since_contact"] + ECONOMY
        honest, honest_model, p_honest = score(HONEST)
        v = val.assign(p=p_honest, yes=(val["y"] == "yes").astype(int))
        rows = [(k, len(g), roc_auc_score(g["yes"], g["p"])) for k, g in v.groupby("year_month")
                if len(g) >= 100 and g["yes"].nunique() == 2]
        inside = pd.DataFrame(rows, columns=["month", "validation calls", "AUC inside the month"]).round(3)
        within = float(np.average(inside["AUC inside the month"], weights=inside["validation calls"]))
        print(f"overall validation AUC {honest['AUC']}, weighted AUC inside one month {within:.3f}")
        inside
        '''),
        md("""
        **What happened.** B. Inside one month the honest model ranks clients at about 0.57; most
        of the gap up to 0.80 is the model knowing which month a call was made in. The calendar
        columns are a second leak that looks legal: each value is known on the morning of the call,
        and the random split still lets the score borrow each month's yes-rate from training rows of
        the same month. The verdict is keep and flag: they stay in Wednesday's feature set with this
        caveat written beside the score, and Friday's split by time puts a price on it.
        """),
        md("""
        ## What do poutcome and pdays need?
        Two columns look suspicious for opposite reasons. `poutcome = success` sounds too good, and
        `pdays` sounds like a plain number of days.

        **Predict before you run.** Clients whose previous campaign ended in success say yes this
        time (A) about 11 percent of the time; (B) about 65 percent of the time, which makes the
        column a leak; (C) about 65 percent of the time, and the column stays.
        """),
        code('''
        print(bank.groupby("poutcome")["y"].apply(lambda s: round((s == "yes").mean(), 3)).to_dict())
        never = (bank["pdays"] == 999).mean()
        print(f"pdays == 999 in {never:.2%} of rows; mean of raw pdays: {bank['pdays'].mean():.0f} days")
        print("contacted before, days since contact:", bank.loc[bank["pdays"] != 999, "pdays"].describe()[["min", "50%", "max"]].to_dict())
        raw, _, _ = score(PROFILE + HISTORY + ["pdays"] + ECONOMY)
        print("AUC with raw pdays:", raw["AUC"], "| with the flag and the days:", honest["AUC"])
        '''),
        md("""
        **What happened.** C. A previous success converts at 65 percent, and the column stays,
        because the previous campaign closed months before this call: it passes the prediction-time
        question. "Too good" is a reason to ask the question and never the verdict. `pdays` holds
        999 for 96.3 percent of rows, which means never contacted, so its raw mean of about 962 days
        describes nobody. The fix is two columns: `never_contacted` (1 when pdays is 999) and
        `days_since_contact` (the days for the 3.7 percent who were contacted, 0 otherwise). The
        AUC barely moves on this file; the model now reads a sentence a person can say aloud.
        """),
        md("""
        ## What is the honest score, and what did the leak promise in rupees?
        The audited set is the customer table, the two engineered `pdays` columns and the economy,
        with `duration` dropped. Score it beside the leaked set.

        **Predict before you run.** The honest bill on 8,238 validation calls is (A) about the leaked
        Rs 1.19 lakh; (B) about Rs 2.8 lakh; (C) higher than calling everyone.
        """),
        code('''
        leaked, _, _ = score(PROFILE + HISTORY + ["never_contacted", "days_since_contact"] + ECONOMY + CALL_LOG)
        everyone = int(len(val) - y_val.sum()) * CALL_RS
        final = pd.DataFrame({"leaked (with duration)": leaked, "honest (audited)": honest}).T[
            ["columns", "AUC", "accuracy", "recall", "bill_Rs", "buyers_in_top_1000"]]
        print(f"calling all 8,238 validation clients costs Rs {everyone/1e5:.2f} lakh in calls and misses nobody")
        final
        '''),
        code('''
        fig, ax = plt.subplots(figsize=(8, 3.2))
        labels = ["the leak promised", "the honest model delivers", "calling everyone"]
        values = [leaked["bill_Rs"] / 1e5, honest["bill_Rs"] / 1e5, everyone / 1e5]
        ax.barh(labels, values, color=[ROSE, GREEN, GREY])
        for i, x in enumerate(values):
            ax.text(x + 0.03, i, f"Rs {x:.2f} lakh", va="center", fontsize=10)
        ax.invert_yaxis(); ax.set_xlim(0, 3.6)
        ax.set_title("The call bill on 8,238 validation calls at Rs 40 a call and Rs 1,200 a missed buyer")
        plt.tight_layout(); plt.show()
        '''),
        md("""
        **What happened.** B. The honest model scores AUC 0.796 with recall 0.23 at 0.5, and its
        bill is about Rs 2.82 lakh against the Rs 1.19 lakh the leak promised. The leaked model could
        never deliver its promise, because on the morning of the call the column it leans on does
        not exist yet. The score fell and the model got better: the honest one can run. At these
        costs the honest bill sits close to calling everyone (about Rs 2.92 lakh), which is
        Tuesday's lesson: a cheap call makes the threshold call almost everyone, and the model earns
        its keep under a budget, where its top 1,000 hold 462 buyers against 113 for a random 1,000.
        """),
        md("""
        ## Where does Kalpa hide the same leak?
        Kalpa's junior found `settlement_status` in the payments feed and lifted validation to 0.99.
        The data platform lead, reading the schema, said the field is written after delivery, when
        the payment clears. The nudge goes out on a morning before any order exists, so a settled
        payment can only appear for a member who has already bought: the column is the target,
        written by another system in another vocabulary. It fails the prediction-time question the
        way `duration` does, and the audit row says so.
        """),
        code('''
        kalpa = pd.DataFrame([
            ("orders_90d", "orders table", "nightly, before the nudge", "yes", "keep"),
            ("days_since_last_order", "orders table", "nightly, before the nudge", "yes", "keep"),
            ("settlement_status", "payments feed", "after delivery, when the payment clears", "no", "drop"),
        ], columns=["column", "written by", "written when", "known on the nudge morning", "verdict"])
        kalpa
        '''),
        code('''
        check("the four calls of 0 seconds all ended in no", zero.to_dict() == {"no": 4})
        check("duration is the only column dropped by the audit", list(audit.loc[audit["verdict"] == "drop", "columns"]) == ["duration"])
        check("the calendar alone scores above 0.75", calendar["AUC"] > 0.75)
        check("inside one month the honest model ranks below 0.65", within < 0.65)
        check("the honest model scores more than 0.12 AUC below the leaked one", leaked["AUC"] - honest["AUC"] > 0.12)
        check("the leak promised a bill at least Rs 1 lakh lower", honest["bill_Rs"] - leaked["bill_Rs"] > 100000)
        '''),
        md("""
        ## What does case 2 hand to case 3?
        | Question | Answer from this notebook |
        |---|---|
        | When is `duration` written? | When the call ends, after the list is made, so it is dropped |
        | Do the economic columns pass? | They pass the question and act as a calendar on a random split: keep, flag, Friday prices it |
        | What does `poutcome = success` get? | Kept: 65 percent yes, and known months before the call |
        | What does `pdays` need? | A never-contacted flag plus the days, since 999 is a sentinel |
        | The honest score | AUC 0.796, about 0.57 inside one month, bill about Rs 2.82 lakh |
        | What the leak promised | AUC 0.93 and a bill about Rs 1.6 lakh lower, which no live list could deliver |

        Case 3 reads the honest model's coefficients and its importance chart and asks what they can
        and cannot prove.
        """),
    ]
    build(NB / "C2_W05_D03_case02_prediction_time_audit_STUDENT.ipynb", cells, timeout=900)


def case03():
    cells = [
        md("""
        # Case 3: The sign that flipped: what does it prove?
        *Applies: Feature importance and its limits · Encoding categoricals; scaling numerics;
        which models care (coefficients are compared only on scaled columns)*

        The honest model from case 2 goes to the campaign review. The campaign head reads two
        exhibits: the model's coefficients and an importance chart. Someone will point at the top
        bar and say "so this is what drives deposits". This notebook finds out what each exhibit
        can carry, starting from one column whose coefficient changes sign depending on who sits
        beside it.

        **Who needs the answer.** The campaign head, who will be tempted to act on the top bar, and
        the senior ML engineer, who has to say what the chart proves before anyone acts on it.

        **The questions on the way.** How closely do the rate columns move together? What happens to
        `euribor3m`'s sign when its partners join? What does permutation importance rank? Why can a
        single column's importance exceed the model's whole lift? Does a top rank prove a cause?
        What is the audited feature set we hand to Thursday?

        **You will be able to** show a coefficient's sign flip on real columns, compute permutation
        importance column by column and by group, and say in one sentence what an importance chart
        proves and what it does not.

        **Search terms:** feature importance, permutation importance, multicollinearity, coefficient
        sign flip, correlation is not causation.
        """),
        md("""
        ## What does the pipeline give us again?
        The week's shared code, the scorer and case 2's engineered `pdays` columns, so the honest
        feature set is rebuilt exactly.
        """),
        code(PIPELINE + SCORER + LOAD + ENGINEER + '''
        honest, honest_model, p_honest = score(HONEST)
        print("honest validation AUC:", honest["AUC"])
        '''.replace("\n        ", "\n")),
        md("""
        ## How closely do the rate columns move together?
        Three of the five economic columns describe the same thing from different desks: the
        employment variation rate, the three-month interbank rate and the number employed.

        **Predict before you run.** The correlation between `euribor3m` and `emp.var.rate` is
        (A) about 0.3; (B) about 0.6; (C) above 0.95.
        """),
        code('''
        TRIO = ["emp.var.rate", "euribor3m", "nr.employed"]
        corr = train[TRIO].corr().round(3)
        fig, ax = plt.subplots(figsize=(4.6, 3.6))
        ax.imshow(corr.values, cmap="Purples", vmin=0, vmax=1)
        ax.set_xticks(range(3)); ax.set_xticklabels(TRIO, rotation=20, fontsize=9)
        ax.set_yticks(range(3)); ax.set_yticklabels(TRIO, fontsize=9)
        for i in range(3):
            for j in range(3):
                ax.text(j, i, f"{corr.values[i, j]:.2f}", ha="center", va="center",
                        color="white" if corr.values[i, j] > 0.6 else INK, fontsize=11)
        ax.set_title("Correlation on training rows"); ax.spines[:].set_visible(False)
        plt.tight_layout(); plt.show()
        '''),
        md("""
        **What happened.** C. `euribor3m` and `emp.var.rate` correlate at 0.97, and `nr.employed`
        sits at 0.91 and 0.94 with them. When three columns move together this closely, the data
        holds almost no row where one is high and another low, which is what a coefficient needs in
        order to tell them apart.
        """),
        md("""
        ## What happens to euribor3m's sign when its partners join?
        Fit a logistic model on standardised columns, so each coefficient is the change in log-odds
        for one standard deviation, with a penalty so weak it does not matter (C = 1,000,000).
        First `euribor3m` alone, then with `nr.employed`, then with both partners, then inside the
        full honest model.

        **Predict before you run.** Alone, `euribor3m` has a negative coefficient: higher rates,
        fewer deposits. With both partners beside it, its coefficient (A) stays negative and
        shrinks; (B) turns positive; (C) goes to exactly zero.
        """),
        code('''
        Z = pd.DataFrame(StandardScaler().fit_transform(train[TRIO]), columns=TRIO, index=train.index)
        def coefs(cols):
            fit = LogisticRegression(C=1e6, max_iter=5000).fit(Z[cols], y_train)
            return dict(zip(cols, fit.coef_[0].round(3)))
        names = honest_model.named_steps["prep"].get_feature_names_out()
        full = dict(zip(names, honest_model.named_steps["model"].coef_[0].round(3)))
        flip = pd.DataFrame({
            "alone": coefs(["euribor3m"]),
            "with nr.employed": coefs(["euribor3m", "nr.employed"]),
            "with both partners": coefs(TRIO),
            "honest model (20 columns)": {c: full["num__" + c] for c in TRIO},
        }).reindex(TRIO)
        flip
        '''),
        code('''
        steps = ["alone", "with nr.employed", "with both partners", "honest model (20 columns)"]
        vals = [flip.loc["euribor3m", s] for s in steps]
        fig, ax = plt.subplots(figsize=(8, 3.2))
        ax.bar(range(4), vals, color=[ROSE if v < 0 else GREEN for v in vals])
        ax.axhline(0, color=INK, lw=1)
        for i, v in enumerate(vals):
            ax.text(i, v + (0.05 if v >= 0 else -0.12), f"{v:+.2f}", ha="center", fontsize=11)
        ax.set_xticks(range(4)); ax.set_xticklabels(steps, fontsize=9)
        ax.set_ylabel("coefficient of euribor3m"); ax.set_title("The same column, four neighbourhoods, two signs")
        plt.tight_layout(); plt.show()
        '''),
        md("""
        **What happened.** B. Alone, `euribor3m` carries about -0.92. Beside `nr.employed` it turns
        to about +0.14, beside both partners about +0.77, and inside the honest model it is about
        +0.36. Nothing about interest rates changed between these fits. A coefficient answers "what
        changes when this column moves and the others stay fixed", and in this data the partners
        never stay fixed, so the credit is split between them almost arbitrarily. The rule: read a
        single coefficient's sign only when its column has no close partner; when it has one, read
        the group, or ask Thursday's penalty to share the credit. Coefficients are compared only
        because every numeric column was standardised first, which is why chapter 2's scaling matters
        to a logistic model.
        """),
        md("""
        ## What does permutation importance rank?
        Permutation importance shuffles one column's values across the validation rows, so the
        column keeps its spread and loses its link to each client, and measures how far the AUC
        falls. A big fall means the fitted model leans on that column.

        **Predict before you run.** The top column will be (A) `poutcome`, the strongest single
        signal; (B) one of the economic columns; (C) `age`.
        """),
        code('''
        from sklearn.inspection import permutation_importance
        perm = permutation_importance(honest_model, val[HONEST], y_val, scoring="roc_auc",
                                      n_repeats=5, random_state=42)
        imp = pd.Series(perm.importances_mean, index=HONEST).sort_values(ascending=False).round(4)
        top = imp.head(10)[::-1]
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.barh(top.index, top.values, color=[VIOLET if c in ECONOMY else GREY for c in top.index])
        for i, x in enumerate(top.values):
            ax.text(x + 0.003, i, f"{x:.3f}", va="center", fontsize=9)
        ax.set_xlabel("fall in validation AUC when the column is shuffled")
        ax.set_title("Permutation importance, honest model (economic columns in violet)")
        plt.tight_layout(); plt.show()
        print(imp.head(6).to_string())
        '''),
        md("""
        **What happened.** B. `emp.var.rate` tops the chart with a fall of about 0.34 in AUC, and
        `cons.price.idx` comes second. The client's own history (`poutcome`, `never_contacted`)
        sits far below. The ranking says the fitted model leans hardest on the rate columns, which
        case 2 showed act as a stamp for the month.
        """),
        md("""
        ## Why can one column's importance exceed the model's whole lift?
        The honest model scores 0.80, so its whole lift above a coin is about 0.30. A single column
        whose shuffle costs 0.34 is costing more than the model ever earned. Shuffling
        `emp.var.rate` alone builds clients who never existed: a 2010 employment rate beside a 2008
        interbank rate. The model's large opposing coefficients on the twins then send those clients
        to absurd scores. Shuffling the whole economic group together keeps each row's quarter
        consistent and measures what the group carries.

        **Predict before you run.** Shuffling all five economic columns together costs (A) more
        than 0.34; (B) less than 0.34.
        """),
        code('''
        rng = np.random.default_rng(42)
        base = roc_auc_score(y_val, honest_model.predict_proba(val[HONEST])[:, 1])
        falls = []
        for _ in range(5):
            shuffled = val[HONEST].copy()
            idx = rng.permutation(len(shuffled))
            shuffled[ECONOMY] = shuffled[ECONOMY].values[idx]       # one shuffle for the whole group
            falls.append(base - roc_auc_score(y_val, honest_model.predict_proba(shuffled)[:, 1]))
        group = float(np.mean(falls))
        print(f"model AUC {base:.3f}; lift above a coin {base - 0.5:.3f}")
        print(f"emp.var.rate shuffled alone: {imp['emp.var.rate']:.3f}; the five economic columns shuffled together: {group:.3f}")
        '''),
        md("""
        **What happened.** B. Shuffled together, the five columns cost far less than
        `emp.var.rate` alone, because each shuffled row is still a real quarter. The rule: when
        columns have close partners, permute them as a group; a single-column importance larger
        than the model's own lift is the sign that the shuffle built impossible rows.
        """),
        md("""
        ## Does a top rank prove a cause?
        No. The chart ranks how much this fitted model leans on a column when it predicts. It does
        not say that moving the column moves the outcome. `nr.employed` ranks high, and hiring more
        people in Portugal would not make a client open a deposit: the column marks the quarter.
        `contact` (mobile against landline) ranks in the top ten, and switching every client to a
        mobile would not move the yes-rate by the gap the chart suggests, because the clients who
        were rung on mobiles differ in other ways. The claim "this lever moves the outcome" needs
        Week 1's fair comparison: change the lever for a random group and compare. Kalpa's version:
        if `app_visits_7d` topped Kalpa's chart, pushing notifications to raise visits would test the
        lever; the chart alone would not.
        """),
        code('''
        verdicts = pd.DataFrame([
            ("profile: age, job, marital, education, default, housing, loan", "keep", "known before the call; one-hot and scaled in the pipeline"),
            ("history: contact, month, day_of_week, campaign, previous, poutcome", "keep", "known before the call; poutcome = success converts at 65 percent and passes"),
            ("never_contacted, days_since_contact", "keep (engineered)", "pdays split, since 999 is a sentinel"),
            ("economy: five columns", "keep, flag", "known if published in time; a calendar stamp on a random split; read as a group"),
            ("duration", "drop", "written when the call ends"),
        ], columns=["feature group", "verdict", "reason"])
        print(f"The audited feature set: {len(HONEST)} columns, validation AUC {honest['AUC']}")
        verdicts
        '''),
        code('''
        check("euribor3m is negative alone", flip.loc["euribor3m", "alone"] < 0)
        check("euribor3m turns positive beside both partners", flip.loc["euribor3m", "with both partners"] > 0)
        check("the top single-column importance exceeds the model's lift above a coin", imp.iloc[0] > base - 0.5)
        check("shuffling the economic group together costs less than the top single column", group < imp.iloc[0])
        check("the audited set has 20 columns and no duration", len(HONEST) == 20 and "duration" not in HONEST)
        '''),
        md("""
        ## What do the three cases hand to Thursday?
        | Exhibit | What it proves | What it does not |
        |---|---|---|
        | Validation AUC 0.796 | the honest model ranks calls better than a coin on this split | how it ranks next month; inside a month it is about 0.57 |
        | A coefficient's sign | the direction with every other column held fixed | anything, when the column has close partners |
        | Permutation importance | how much the fitted model leans on a column | that moving the column moves deposits |

        Thursday starts from this audited set of 20 columns and asks whether a more complex model
        earns more than it costs.
        """),
    ]
    build(NB / "C2_W05_D03_case03_sign_flip_importance_STUDENT.ipynb", cells, timeout=900)


def ch01():
    cells = [
        md("""
        # Chapter 1: Turning raw columns into signals: what does a row know?
        *Feature engineering from the customer table: ratios, recency, counts, cohort age, basket
        signals · also searched as: feature engineering for machine learning, RFM features*

        Kalpa's customer table holds raw facts: when a member first ordered, when they last
        ordered, how many orders, how much they spent, how many items. Marketing wants to know who
        will buy again in the next ninety days. A raw total answers a different question from the
        one Marketing asked, and this chapter turns the raw facts into five kinds of signal, each
        with the business reason a marketing lead would repeat.

        **Who needs the answer.** Kalpa's marketing lead, who spends Rs 40 per nudge, and Kavya
        Nair, the senior analyst, who wants a reason beside every feature.

        **The questions on the way.** Which member does a raw total rank first? What do recency,
        counts, ratios, cohort age and basket signals each add? Where are the same five ideas in the
        bank's file?

        **You will be able to** compute recency, counts, ratios, cohort age and basket signals from
        dates and totals, state each one's business reason, and spot them in a new table.
        """),
        md("""
        ## Which member does a raw total rank first?
        The table below is invented: eight Kalpa members as they stood on the nudge morning,
        1 November 2026 (also invented). Every feature is measured from that morning, because
        that is the moment the model will be used.

        **Predict before you run.** Ranked by total spend, the top member is (A) Asha, who ordered
        three days ago; (B) Hari, who spent the most over four years and last ordered ten months
        ago; (C) Dev, the newest member.
        """),
        code(STYLE8 + '''
        NUDGE = pd.Timestamp("2026-11-01")          # the nudge morning (invented)
        members = pd.DataFrame({                     # invented teaching table, eight Kalpa members
            "member":      ["Asha", "Bilal", "Chitra", "Dev", "Esha", "Farid", "Gauri", "Hari"],
            "first_order": pd.to_datetime(["2024-11-02", "2026-08-20", "2023-05-10", "2026-10-05",
                                           "2025-01-15", "2024-06-01", "2025-12-01", "2022-02-11"]),
            "last_order":  pd.to_datetime(["2026-10-29", "2026-10-25", "2026-03-14", "2026-10-30",
                                           "2026-07-01", "2026-10-20", "2026-09-30", "2025-12-24"]),
            "orders":      [24, 6, 30, 3, 8, 12, 10, 40],
            "spend_rs":    [16800, 4200, 19500, 2400, 12000, 3600, 7000, 26000],
            "items":       [96, 30, 60, 15, 16, 48, 40, 80],
        })
        members.sort_values("spend_rs", ascending=False)
        '''),
        md("""
        **What happened.** B. Hari tops total spend with Rs 26,000, and Hari has not ordered for
        more than ten months. A total grows with time, so it ranks the oldest members first, and
        Marketing's question is about the next ninety days. The fix is to measure each member
        against the nudge morning and against their own time with Kalpa.
        """),
        md("""
        ## What do the five signals add?
        Each feature below is one line of pandas and one business reason. Asha's average basket by
        hand: Rs 16,800 over 24 orders is Rs 700.
        """),
        code('''
        f = members[["member"]].copy()
        f["recency_days"] = (NUDGE - members["last_order"]).dt.days            # recency
        f["orders"] = members["orders"]                                          # count
        f["cohort_age_days"] = (NUDGE - members["first_order"]).dt.days          # cohort age
        f["orders_per_month"] = (members["orders"] / (f["cohort_age_days"] / 30.4)).round(2)  # ratio
        f["avg_basket_rs"] = (members["spend_rs"] / members["orders"]).round(0)  # ratio
        f["items_per_order"] = (members["items"] / members["orders"]).round(1)   # basket signal
        f
        '''),
        md("""
        | Signal | Formula | The business reason Marketing would repeat |
        |---|---|---|
        | Recency | `nudge morning - last order`, in days | a member who ordered last week is warm; ten months is lapsed |
        | Count | `orders` (or orders in a fixed window) | habit: more orders, more likely to order again |
        | Cohort age | `nudge morning - first order`, in days | a new member is still deciding; an old one has settled |
        | Ratio | `orders / months as a member`, `spend / orders` | puts old and new members on one scale |
        | Basket signal | `items / orders` | a big basket is a weekly shop; a small one is a top-up |
        """),
        code('''
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.scatter(f["recency_days"], f["orders_per_month"], s=members["spend_rs"] / 60,
                   color=[ROSE if r > 120 else VIOLET for r in f["recency_days"]], alpha=0.75)
        for _, r in f.iterrows():
            ax.annotate(r["member"], (r["recency_days"], r["orders_per_month"]), xytext=(6, 4),
                        textcoords="offset points", fontsize=10)
        ax.set_xlabel("recency: days since last order (lower is warmer)")
        ax.set_ylabel("orders per month as a member")
        ax.set_title("Warm members sit top left; bubble size is total spend")
        plt.tight_layout(); plt.show()
        '''),
        md("""
        **The trap.** Hari's bubble is the biggest on the chart and sits far right: the largest
        total, the coldest member. A model fed only `spend_rs` would rank Hari for a nudge, and
        Kalpa would pay Rs 40 to reach the member least likely to answer it. Recency and
        orders per month put Asha, Bilal and Dev ahead, which is what Marketing meant.
        """),
        md("""
        ## Where are the same five ideas in the bank's file?
        The bank's table already holds counts and a recency: `campaign` counts calls in this
        campaign, `previous` counts calls in earlier campaigns, `pdays` is days since the last
        contact (with 999 for never), and `poutcome` is how the last campaign ended.

        **Predict before you run.** As `campaign` (calls so far this campaign) rises from 1 to 4 or
        more, the yes-rate (A) rises, since persistence pays; (B) falls.
        """),
        code('''
        import io, zipfile, pathlib, urllib.request
        CACHE = pathlib.Path.home() / ".cache" / "c2_datasets"
        CACHE.mkdir(parents=True, exist_ok=True)
        f_bank = CACHE / "bank-additional-full.csv"
        if not f_bank.exists():   # the week's cached loader: UCI Bank Marketing, CC BY 4.0
            url = "https://archive.ics.uci.edu/static/public/222/bank+marketing.zip"
            outer = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(url, timeout=60).read()))
            inner = zipfile.ZipFile(io.BytesIO(outer.read("bank-additional.zip")))
            f_bank.write_bytes(inner.read("bank-additional/bank-additional-full.csv"))
        bank = pd.read_csv(f_bank, sep=";")
        yes = (bank["y"] == "yes")
        calls = pd.cut(bank["campaign"], [0, 1, 2, 3, 100], labels=["1", "2", "3", "4 or more"])
        earlier = pd.cut(bank["previous"], [-1, 0, 1, 100], labels=["0", "1", "2 or more"])
        print("yes-rate by calls this campaign:", yes.groupby(calls, observed=True).mean().round(3).to_dict())
        print("yes-rate by calls in earlier campaigns:", yes.groupby(earlier, observed=True).mean().round(3).to_dict())
        print(f"pdays is 999 (never contacted) in {(bank['pdays'] == 999).mean():.1%} of rows")
        '''),
        md("""
        **What happened.** B. One call this campaign converts at about 13 percent and four or more
        at about 7 percent: a count can carry signal in the direction nobody expected, which is why
        each feature gets a reason and a check. Earlier contact helps sharply. `pdays` holds 999 for
        96.3 percent of rows, a sentinel the case chapters split into a flag and a number.
        """),
        code('''
        check("Asha's average basket matches the hand count of Rs 700", f.loc[f["member"] == "Asha", "avg_basket_rs"].item() == 700)
        check("Dev's recency is 2 days from the nudge morning", f.loc[f["member"] == "Dev", "recency_days"].item() == 2)
        check("total spend ranks Hari first, recency ranks Hari last",
              members.sort_values("spend_rs").iloc[-1]["member"] == "Hari"
              and f.sort_values("recency_days").iloc[-1]["member"] == "Hari")
        check("the bank's file loads with 41,188 rows", len(bank) == 41188)
        '''),
        md("""
        ## What are the rules, and what flips each one?
        1. Measure every feature from the prediction moment. Computed from today's date, recency
           quietly uses days that had not happened when the nudge went out.
        2. Prefer a ratio when members have different tenure; when everyone joined in the same
           window, the total and the ratio rank alike.
        3. Count over a fixed window (orders in the last 90 days) when the decision is about the
           next 90 days; a lifetime count suits a loyalty tier.
        4. A feature ships with its business reason; a feature nobody can explain is dropped, unless
           a fair test shows it carries signal the reasons missed.

        Chapter 2 asks how a model reads the columns that are words, such as city and job.
        """),
    ]
    build(NB / "C2_W05_D03_ch01_feature_engineering_STUDENT.ipynb", cells, timeout=600)


def ch02():
    cells = [
        md("""
        # Chapter 2: Teaching a model to read categories: is Surat twice Pune?
        *Encoding categoricals; scaling numerics; which models care · also searched as: one-hot
        encoding, label encoding, standard scaling, feature scaling*

        A model reads numbers. Kalpa's table has words (city, job, tier) and numbers on very
        different scales (spend in rupees, visits in single digits). How a word becomes a number,
        and whether a number is rescaled, decides what the model can learn, and the right choice
        depends on the model family.

        **Who needs the answer.** The implementation engineer, who writes the pipeline the scoring
        service runs every night, and Kavya, who reads the model's coefficients.

        **The questions on the way.** What goes wrong when cities become 1, 2 and 3? What does
        one-hot encoding do instead? Why does spend in rupees drown visits in a distance? Which
        models care about encoding and scaling, and which shrug? What does the bank's file need?

        **You will be able to** one-hot encode a category, standardise a number by hand and in
        code, and say which model family needs each step.
        """),
        md("""
        ## What goes wrong when cities become 1, 2 and 3?
        Six invented Kalpa members, with city, spend in the last 90 days and app visits in the
        last 30 days.

        **Predict before you run.** Label-encode Pune = 1, Surat = 2, Indore = 3. A logistic model
        that multiplies this code by one weight assumes (A) nothing about the cities; (B) that
        Indore is as far from Surat as Surat is from Pune, and three times Pune.
        """),
        code(STYLE8 + '''
        m = pd.DataFrame({                      # invented teaching table, six Kalpa members
            "member":     ["A", "B", "C", "D", "E", "F"],
            "city":       ["Pune", "Surat", "Indore", "Pune", "Indore", "Surat"],
            "spend_90d":  [9000, 9200, 7000, 2500, 4500, 3000],
            "visits_30d": [2, 9, 2, 8, 6, 3],
        })
        m["city_code"] = m["city"].map({"Pune": 1, "Surat": 2, "Indore": 3})   # the label encoding
        onehot = pd.get_dummies(m["city"], prefix="city", dtype=int)            # the one-hot encoding
        pd.concat([m, onehot], axis=1)
        '''),
        md("""
        **What happened.** B. One weight on `city_code` forces a straight line through the cities:
        whatever Surat adds over Pune, Indore adds again, in an order nobody chose. One-hot gives
        each city its own 0 or 1 column and so its own weight, and every row has exactly one 1.
        A tree is different: it splits on `city_code <= 1.5` and `city_code <= 2.5`, so the made-up
        order costs it little.
        """),
        md("""
        ## Why does spend in rupees drown visits in a distance?
        A distance-based model (nearest neighbours, clustering) adds up differences across columns.
        By hand, member A against member B: spend differs by Rs 200 and visits by 7, so the distance
        is the square root of 200 squared plus 7 squared, about 200.1. Visits barely register.

        **Predict before you run.** A's nearest neighbour before scaling is B (similar spend, very
        different visits). After standardising both columns, A's nearest neighbour is (A) still B;
        (B) someone with similar visits.
        """),
        code('''
        X = m[["spend_90d", "visits_30d"]].astype(float)
        Z = (X - X.mean()) / X.std(ddof=0)                     # standardise: (value - mean) / spread
        def nearest(T, who="A"):
            d = ((T - T.loc[m["member"] == who].values) ** 2).sum(axis=1) ** 0.5
            d[m["member"] == who] = np.inf
            return m.loc[d.idxmin(), "member"], round(float(d.min()), 2)
        print("A to B, unscaled:", round(float(((X.iloc[0] - X.iloc[1]) ** 2).sum() ** 0.5), 1))
        print("nearest to A before scaling:", nearest(X))
        print("nearest to A after scaling: ", nearest(Z))
        Z.round(2).assign(member=m["member"])
        '''),
        code('''
        fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))
        for ax, T, title in [(axes[0], X, "Raw: rupees dominate"), (axes[1], Z, "Standardised: both columns count")]:
            ax.scatter(T["spend_90d"], T["visits_30d"], s=120, color=VIOLET)
            for i, r in T.iterrows():
                ax.annotate(m.loc[i, "member"], (r["spend_90d"], r["visits_30d"]), xytext=(6, 4),
                            textcoords="offset points", fontsize=11)
            ax.set_title(title); ax.set_xlabel("spend_90d"); ax.set_ylabel("visits_30d")
        axes[0].set_xlim(0, 10500); axes[0].set_ylim(0, 10500)   # same scale on both axes, as distance sees it
        plt.tight_layout(); plt.show()
        '''),
        md("""
        **What happened.** B. Drawn on equal axes, the raw table is a flat line: every member's
        visits sit near zero beside thousands of rupees, so distance is spend alone. After
        standardising, each column is measured in its own spreads, and A's nearest neighbour becomes
        C, the member who also visits twice a month. The formula is `z = (value - mean) / standard
        deviation`, with the mean and spread learned from training rows only.
        """),
        md("""
        ## Which models care, and which shrug?
        | Model family | Encoding a category | Scaling a number | Why |
        |---|---|---|---|
        | Logistic or linear regression | one-hot | yes, for the penalty and to compare coefficients | one weight per column, read in the column's units |
        | Nearest neighbours, clustering | one-hot | yes, decisive | distance adds raw differences |
        | Tree, forest, boosting | one-hot or an ordinal code | no | splits on thresholds, which ignore units |

        A forty-value category (a city list) is still one-hot for a logistic model; forty columns
        are cheap. Grouping rare values into "other" keeps it readable. Methods that replace a city
        with its average outcome come later, because they can carry the target into the feature.
        """),
        md("""
        ## What does the bank's file need?
        **Predict before you run.** How many one-hot columns does `job` become? (A) 1; (B) 11;
        (C) 12, with `unknown` as its own category.
        """),
        code('''
        import io, zipfile, pathlib, urllib.request
        CACHE = pathlib.Path.home() / ".cache" / "c2_datasets"
        CACHE.mkdir(parents=True, exist_ok=True)
        f_bank = CACHE / "bank-additional-full.csv"
        if not f_bank.exists():   # the week's cached loader: UCI Bank Marketing, CC BY 4.0
            url = "https://archive.ics.uci.edu/static/public/222/bank+marketing.zip"
            outer = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(url, timeout=60).read()))
            inner = zipfile.ZipFile(io.BytesIO(outer.read("bank-additional.zip")))
            f_bank.write_bytes(inner.read("bank-additional/bank-additional-full.csv"))
        bank = pd.read_csv(f_bank, sep=";")
        text_cols = [c for c in bank.columns if not pd.api.types.is_numeric_dtype(bank[c]) and c != "y"]
        print("text columns:", text_cols)
        print("job levels:", bank["job"].nunique(), "| unknown rows in job:", int((bank["job"] == "unknown").sum()))
        print("numeric spreads (std):", bank[["age", "campaign", "euribor3m", "nr.employed"]].std().round(2).to_dict())
        '''),
        md("""
        **What happened.** C. `job` has 12 levels, `unknown` among them, and stays a category of its
        own because "did not say" can carry signal. The numbers range from a spread of about 2.8 for
        `campaign` to about 72 for `nr.employed`, so a logistic model's coefficients only compare
        after standardising. Case 1 puts both steps inside one pipeline fitted on training rows.
        """),
        code('''
        check("every one-hot row holds exactly one 1", (onehot.sum(axis=1) == 1).all())
        check("standardised columns have mean 0", bool((Z.mean().abs() < 1e-9).all()))
        check("scaling changes A's nearest neighbour from B to C", nearest(X)[0] == "B" and nearest(Z)[0] == "C")
        check("job one-hot gives 12 columns", bank["job"].nunique() == 12)
        '''),
        md("""
        ## What are the rules, and what flips each one?
        1. One-hot a category for linear and distance models; a tree can take an ordinal code
           because it splits on thresholds.
        2. Standardise numbers for linear and distance models; a tree ignores scale, so scaling it
           changes nothing.
        3. Fit every encoder and scaler on training rows only, inside the pipeline; fitted on all
           rows, the test set shapes the features.
        4. Keep `unknown` as a category when "did not say" may carry signal; drop or impute only
           when the business confirms it is noise.

        Chapter 3 asks a harder question of every column: was it even known when the model runs?
        """),
    ]
    build(NB / "C2_W05_D03_ch02_encoding_scaling_STUDENT.ipynb", cells, timeout=600)


def ch03():
    cells = [
        md("""
        # Chapter 3: Answers from the future: known that morning?
        *Leakage and the prediction-time question · also searched as: data leakage in machine
        learning, target leakage, train test contamination*

        Kalpa's junior joined `settlement_status` from the payments feed and validation jumped to
        0.99. The data platform lead, reading the schema, said the field is written after delivery,
        when the payment clears. This chapter shows on twelve invented members why that column
        scores perfectly in training and cannot score at all on the morning the nudge goes out.

        **Who needs the answer.** Kalpa's marketing lead, who wants the 0.99 shipped tonight, and the
        data platform lead, who knows when each field is written.

        **The questions on the way.** Why does one column score twelve out of twelve? What does the
        same column hold on the nudge morning? What is the one question that catches it? What does
        the honest score look like?

        **You will be able to** place every column on a timeline against the prediction moment, ask
        the prediction-time question, and explain why the score fell and the model got better.
        """),
        md("""
        ## Why does one column score twelve out of twelve?
        Twelve invented members as the training table holds them, ninety days after the nudge, when
        the outcome is known. A rule on one column predicts "bought" when the column says so.

        **Predict before you run.** The rule "bought if settlement_status is settled" gets (A) about
        half right; (B) 10 of 12; (C) 12 of 12.
        """),
        code(STYLE8 + '''
        k = pd.DataFrame({                     # invented teaching table, twelve Kalpa members
            "member": [f"M{i:02d}" for i in range(1, 13)],
            "days_since_last_order": [3, 40, 6, 12, 75, 2, 30, 9, 55, 4, 20, 90],
            "orders_90d":            [6, 1, 4, 3, 0, 7, 2, 4, 1, 5, 2, 0],
            "settlement_status": ["settled", "none", "settled", "none", "none", "settled",
                                  "settled", "none", "none", "settled", "settled", "none"],
            "bought_90d":            [1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0],
        })
        def right(rule):
            return int((rule.astype(int) == k["bought_90d"]).sum())
        print("settled -> bought:", right(k["settlement_status"] == "settled"), "of 12")
        print("orders_90d >= 2 -> bought:", right(k["orders_90d"] >= 2), "of 12")
        print("days_since_last_order <= 6 -> bought:", right(k["days_since_last_order"] <= 6), "of 12")
        k
        '''),
        md("""
        **What happened.** C. The settlement rule is perfect, and the best honest rule, two or more
        orders in 90 days, gets 10 of 12. A payment can only settle for a member who bought, so the
        column is the answer written in the payments team's words.
        """),
        md("""
        ## What does the same column hold on the nudge morning?
        The model runs on the nudge morning, before anyone has bought. On that morning no payment
        from the coming 90 days exists, so `settlement_status` reads `none` for every member.

        **Predict before you run.** On the nudge morning the settlement rule gets (A) 12 of 12;
        (B) 6 of 12, the score of predicting that nobody buys.
        """),
        code('''
        morning = k.assign(settlement_status="none")       # what the scoring service sees that morning
        print("settlement rule on the nudge morning:", right(morning["settlement_status"] == "settled"), "of 12")
        print("predict nobody buys:", int((k["bought_90d"] == 0).sum()), "of 12")
        '''),
        md("""
        **What happened.** B. The perfect rule collapses to "nobody buys", 6 of 12. The 0.99 was
        measured on a table built after the outcome, and the model would meet a table built before
        it. That gap is leakage: an input the model sees in training that would not be known at the
        moment it is used.
        """),
        code('''
        # days from the nudge morning, drawn at even spacing so the labels never collide
        events = [("first order\\n(day -400)", -400, GREEN), ("last order\\n(day -9)", -9, GREEN),
                  ("orders_90d written\\n(day -1)", -1, GREEN), ("nudge morning", 0, INK),
                  ("order placed\\n(day +5)", 5, GREY), ("delivered\\n(day +8)", 8, GREY),
                  ("payment clears:\\nsettlement_status (day +12)", 12, ROSE), ("outcome window\\ncloses (day +90)", 90, GREY)]
        spot = {-400: -2.5, -9: -1.5, -1: -0.6, 0: 0, 5: 0.45, 8: 0.95, 12: 1.45, 90: 1.95}
        pos = lambda t: spot[t]
        fig, ax = plt.subplots(figsize=(10, 2.8))
        ax.axhline(0, color=GREY, lw=1)
        ax.axvline(0, color=INK, lw=2.5)
        ax.axvspan(0, 2.45, color=ROSE, alpha=0.06)
        for i, (name, t, c) in enumerate(events):
            if t == 0:
                continue
            y = 0.35 if i % 2 else -0.45
            ax.plot(pos(t), 0, "o", color=c, ms=10)
            ax.text(pos(t), y, name, ha="center", fontsize=9, color=c if c != GREY else INK)
        ax.text(0.03, 0.75, "prediction moment: the nudge morning", color=INK, fontsize=10)
        ax.text(1.05, -0.9, "written after the moment: the model may not read it", color=ROSE, ha="center", fontsize=9)
        ax.set_xlim(-2.9, 2.45); ax.set_ylim(-1.05, 1.0); ax.set_yticks([]); ax.set_xticks([])
        ax.spines[:].set_visible(False)
        ax.set_title("One member's timeline: green is known on the nudge morning, red is written after it")
        plt.tight_layout(); plt.show()
        '''),
        md("""
        ## What is the one question that catches it?
        **The prediction-time question: on the morning the model is used, do we know this value
        for this customer?** It is asked of every column, with the system that writes it and the
        moment it is written. `orders_90d` is written nightly before the nudge: known. The
        settlement status is written days after the order: not known, so it is dropped, however
        well it scores. Two more routes carry the future in: a scaler or encoder fitted on all rows
        before the split, and rows from after the prediction moment sitting in the training set.
        """),
        code('''
        honest = right(k["orders_90d"] >= 2)
        check("the settlement rule is perfect on the training table", right(k["settlement_status"] == "settled") == 12)
        check("on the nudge morning it falls to the do-nothing score", right(morning["settlement_status"] == "settled") == int((k["bought_90d"] == 0).sum()))
        check("the best honest rule scores between the two", 6 < honest < 12)
        '''),
        md("""
        ## What are the rules, and what flips each one?
        1. A column is allowed only if it is known at the prediction moment; a column written later
           is dropped, whatever it scores.
        2. A score that jumps on one new column is a suspect until its write time is checked; a
           jump with a known business cause, such as a new and legitimate data source, survives.
        3. "Too good" is a reason to ask the question and never the verdict: a strong column that
           was known in time stays.
        4. The honest score is the one to ship, and it is lower: the score fell and the model got
           better, because the leaked model cannot run on the morning it is needed.

        Chapter 4 turns the question into an audit of every column, with a verdict and a reason.
        """),
    ]
    build(NB / "C2_W05_D03_ch03_leakage_prediction_time_STUDENT.ipynb", cells, timeout=600)


def ch04():
    cells = [
        md("""
        # Chapter 4: Interrogating every column: keep, drop or fix?
        *The column audit · also searched as: feature audit, leakage checklist, point in time
        correct features*

        A leak hides in the column nobody asked about. The audit asks the same five things of every
        column before any model sees it, and writes a verdict and a reason beside each, so a
        reviewer can disagree with a line instead of with a feeling.

        **Who needs the answer.** The solution architect, who decides which feeds the scoring
        service may read, and Kavya, who signs the feature list.

        **The questions on the way.** What does the audit ask of each column? Which of Kalpa's nine
        candidate columns pass? What is the as-of trap? What does the audit hand to the model?

        **You will be able to** write the audit table for a new dataset, catch a column that is
        rewritten after the fact, and defend each verdict in one line.
        """),
        md("""
        ## What does the audit ask of each column?
        | Ask | Why |
        |---|---|
        | Which system writes it? | the owner knows when and how it changes |
        | When is it written, in days from the prediction moment? | negative means known in time |
        | Is it rewritten later? | a value overwritten after the outcome must be read as it stood that morning |
        | What is its business reason? | a column nobody can explain is dropped or tested |
        | Verdict | keep, drop, or fix (engineer, snapshot, flag) |

        Nine invented candidate columns for Kalpa's nudge model follow.

        **Predict before you run.** How many of the nine are dropped? (A) 1; (B) 3; (C) 5.
        """),
        code(STYLE8 + '''
        cols = pd.DataFrame([   # invented candidate columns for Kalpa's nudge model
            ("days_since_last_order", "orders table", -1, "no", "warm members buy again"),
            ("orders_90d", "orders table", -1, "no", "habit"),
            ("avg_basket_rs", "orders table", -1, "no", "weekly shop against top-up"),
            ("city", "signup form", -400, "no", "stores and delivery differ by city"),
            ("app_visits_7d", "app events", -1, "no", "intent shows before an order"),
            ("loyalty_tier", "loyalty service", -1, "yes", "perks change behaviour"),
            ("member_id", "signup form", -400, "no", ""),
            ("coupon_redeemed", "checkout", 3, "no", "uses the nudge coupon"),
            ("settlement_status", "payments feed", 12, "no", "payment cleared"),
        ], columns=["column", "written by", "written_day", "rewritten later", "business reason"])

        def verdict(r):
            if r["written_day"] > 0:
                return "drop: written after the nudge"
            if not r["business reason"]:
                return "drop: no reason"
            if r["rewritten later"] == "yes":
                return "fix: read the snapshot as of the nudge morning"
            return "keep"
        cols["verdict"] = cols.apply(verdict, axis=1)
        cols
        '''),
        md("""
        **What happened.** B. Three are dropped. `coupon_redeemed` and `settlement_status` are
        written after the nudge, the first on the day the coupon is used, which is the outcome
        itself. `member_id` has no reason: an identifier is a key, and it would only carry signal
        by accident (for example, if ids are issued in signup order, it becomes cohort age in
        disguise, and cohort age should then be engineered openly). `loyalty_tier` is kept with a
        fix, explained next.
        """),
        md("""
        ## What is the as-of trap?
        `loyalty_tier` is written every night and overwritten in place. A member who bought three
        times after the nudge was upgraded to Gold in December. The warehouse today says Gold; on
        the nudge morning it said Silver.

        **Predict before you run.** If training reads today's tier, the Gold members in training are
        (A) a fair mix; (B) mostly members who bought after the nudge, so the tier leaks the outcome.
        """),
        code('''
        tiers = pd.DataFrame({   # invented: two members' tier today and as of the nudge morning
            "member": ["M04", "M07"], "bought_90d": [0, 1],
            "tier_today": ["Silver", "Gold"], "tier_as_of_nudge_morning": ["Silver", "Silver"]})
        tiers
        '''),
        md("""
        **What happened.** B. M07 bought, was upgraded, and today's table says Gold; a model trained
        on today's tier learns "Gold buys", which was written by the purchase. The fix is a snapshot
        (an as-of join): read each value as it stood on the prediction morning. The question to the
        owner is "is this field ever overwritten?", and a yes means the audit asks for history.
        """),
        code('''
        colour = {"keep": GREEN, "fix": VIOLET, "drop": ROSE}
        fig, ax = plt.subplots(figsize=(10, 3.4))
        ax.axvline(0, color=INK, lw=2.5); ax.text(0.05, 8.6, "nudge morning", color=INK, fontsize=10)
        for i, r in cols.iterrows():
            x = np.sign(r["written_day"]) * np.log10(abs(r["written_day"]) + 1)
            c = colour[r["verdict"].split(":")[0]]
            ax.plot(x, i, "o", color=c, ms=10)
            ax.text(x + (0.08 if x < 2 else -0.08), i, f"{r['column']}  ({r['verdict'].split(':')[0]})",
                    va="center", fontsize=9, color=c, ha="left" if x < 2 else "right")
        ax.set_yticks([]); ax.set_xlim(-3, 3); ax.set_ylim(-0.8, 9.2)
        ax.set_xticks([-2.6, -0.3, 0, 0.6, 1.1]); ax.set_xticklabels(["signup", "last night", "", "+3 days", "+12 days"])
        ax.set_title("The audit on a timeline: green keep, violet fix, red drop")
        plt.tight_layout(); plt.show()
        '''),
        code('''
        check("three columns are dropped", int(cols["verdict"].str.startswith("drop").sum()) == 3)
        check("every column written after the nudge is dropped",
              cols.loc[cols["written_day"] > 0, "verdict"].str.startswith("drop").all())
        check("every kept column has a business reason",
              (cols.loc[cols["verdict"] == "keep", "business reason"].str.len() > 0).all())
        '''),
        md("""
        ## What are the rules, and what flips each one?
        1. Audit every column before any model sees it, the boring ones first; an identifier or a
           timestamp is where leaks hide.
        2. Ask the owner whether a field is overwritten; a yes means the model reads the snapshot
           as of the prediction moment, never today's value.
        3. Drop a column with no business reason; keep it only if a fair test shows signal that
           survives the audit.
        4. Write the verdict and the reason on one line per column, so a reviewer argues with a line.

        Chapter 5 asks what the model's importance chart can say about the columns that survive.
        """),
    ]
    build(NB / "C2_W05_D03_ch04_column_audit_STUDENT.ipynb", cells, timeout=600)


def ch05():
    cells = [
        md("""
        # Chapter 5: What the importance chart can't tell you: is it rank or cause?
        *Feature importance and its limits · also searched as: feature importance, permutation
        importance, correlation is not causation*

        Every model review ends on a bar chart of feature importance, and someone points at the top
        bar and calls it the driver. This chapter computes importance by hand on twelve invented
        members, so you can see exactly what it measures, and then the two things it cannot carry.

        **Who needs the answer.** Kalpa's marketing lead, who will want to act on the top bar, and
        the senior ML engineer, who says what the chart proves.

        **The questions on the way.** What does permutation importance measure, by hand? What
        happens when two columns are near twins? Does the top bar name a lever?

        **You will be able to** compute permutation importance by shuffling a column and recounting,
        explain why twins share credit, and say what a chart proves in one sentence.
        """),
        md("""
        ## What does permutation importance measure, by hand?
        Twelve invented members, their app visits and searches in the last week, and whether they
        bought. The model is a rule: predict "buys" when visits plus searches is 8 or more.
        Permutation importance shuffles one column (here, a fixed shuffle that moves every value six
        rows down) and counts how many answers the same rule now gets right.

        **Predict before you run.** The rule gets 11 of 12. With `searches` shuffled it gets
        (A) about 11; (B) about 7; (C) 0.
        """),
        code(STYLE8 + '''
        t = pd.DataFrame({                       # invented teaching table, twelve Kalpa members
            "visits":   [9, 7, 6, 5, 8, 2, 3, 1, 4, 2, 5, 4],
            "searches": [8, 7, 5, 6, 9, 1, 3, 2, 3, 2, 4, 5],
            "bought":   [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0],
        })
        SHUFFLE = [6, 7, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5]   # move every value six rows down
        def right(v, s):
            return int((((v + s) >= 8).astype(int) == t["bought"].values).sum())
        base = right(t["visits"].values, t["searches"].values)
        rows = {"nothing shuffled": base,
                "visits shuffled": right(t["visits"].values[SHUFFLE], t["searches"].values),
                "searches shuffled": right(t["visits"].values, t["searches"].values[SHUFFLE]),
                "both shuffled": right(t["visits"].values[SHUFFLE], t["searches"].values[SHUFFLE])}
        imp = pd.DataFrame({"right of 12": rows, "importance (answers lost)": {k: base - v for k, v in rows.items()}})
        imp
        '''),
        md("""
        **What happened.** B. Shuffling `searches` costs 4 answers and shuffling `visits` costs 2,
        so the rule leans more on searches. Shuffling both costs 8. That is all permutation
        importance measures: how much this fitted model's score falls when one column stops
        lining up with its rows. In code it is `sklearn.inspection.permutation_importance`, scored
        on validation rows, which case 3 runs on the bank.
        """),
        code('''
        fig, ax = plt.subplots(figsize=(7.5, 3))
        lost = imp["importance (answers lost)"].drop("nothing shuffled")
        ax.barh(lost.index, lost.values, color=[VIOLET, VIOLET, INK])
        for i, x in enumerate(lost.values):
            ax.text(x + 0.1, i, f"{x} answers lost", va="center", fontsize=10)
        ax.set_xlim(0, 10); ax.invert_yaxis()
        ax.set_title("The twins one at a time cost 2 and 4; together they cost 8")
        plt.tight_layout(); plt.show()
        print("correlation of visits and searches:", round(float(t["visits"].corr(t["searches"])), 2))
        '''),
        md("""
        ## What happens when two columns are near twins?
        `visits` and `searches` correlate at 0.94: they are near twins. Each one alone costs little
        when shuffled, because its twin still carries most of the signal, and together they cost
        more than the two single costs added up. A chart that lists them one at a time understates
        both, and the split of credit between them depends on accidents of the sample. When columns
        have close partners, shuffle them as a group and read the group.
        """),
        md("""
        ## Does the top bar name a lever?
        **Predict before you run.** Marketing sees `searches` at the top and proposes push
        notifications that drive members to search more. The chart says that pushing searches up
        will (A) raise purchases; (B) nothing about what happens if searches are pushed up.

        **What happened.** B. A member searches because they already mean to buy; the search is a
        symptom of intent. The chart ranks what this model leans on; it does not say that changing
        the column changes the outcome. The way to test the lever is the fair comparison from
        Week 1: push a random half of members, leave the other half, and compare purchases.
        """),
        code('''
        check("the rule gets 11 of 12 before any shuffle", base == 11)
        check("shuffling both twins costs more than the two single costs added", rows["both shuffled"] < rows["visits shuffled"] + rows["searches shuffled"] - base)
        check("the twins correlate above 0.9", t["visits"].corr(t["searches"]) > 0.9)
        '''),
        md("""
        ## What are the rules, and what flips each one?
        1. Importance ranks how much a fitted model leans on a column; it names a lever only when
           the column was changed in a fair test.
        2. Shuffle close partners as a group; a single-column importance is readable only when the
           column has no twin.
        3. Compute importance on validation rows; on training rows it rewards what the model
           memorised.
        4. Run the column audit before the chart: a leaked column tops every importance chart, so
           the chart can never be the audit.

        The case chapters now take all five ideas to the bank's 41,188 calls.
        """),
    ]
    build(NB / "C2_W05_D03_ch05_feature_importance_STUDENT.ipynb", cells, timeout=600)


def guided():
    cells = [
        md("""
        # Guided: two features and three columns: engineer and audit them together
        *Feature engineering from the customer table · Leakage and the prediction-time question ·
        The column audit*

        The trainer leads; the room fills the three TODO cells together, says each reason aloud,
        and runs the check cell. The worked answer sits in the last section, below a clear line, so
        the room tries first. Nothing here needs more than one line of pandas per answer.

        **Who needs the answer.** The campaign head, who will ask "why that feature?", and the
        solution architect, who will ask "is that column there when we score?".

        **The questions on the way.** Which line turns the 999 sentinel into a never-contacted flag?
        Which line marks a previous success? Which of three columns pass the prediction-time
        question? What do the two features add?

        **Search terms:** feature engineering pandas, data leakage checklist.
        """),
        code(PIPELINE + LOAD),
        md("""
        ## Which line turns the 999 sentinel into a never-contacted flag?
        `pdays` is days since the client was last contacted in an earlier campaign, and 999 means
        never. Pick the line, type it in place of `None`, and write the reason a marketing lead
        would repeat.
        """),
        code('''
        # TODO 1: replace None with the line that is 1 when the client was never contacted before.
        #   (A) (bank["pdays"] == 0).astype(int)
        #   (B) (bank["pdays"] == 999).astype(int)
        #   (C) bank["pdays"] / 999
        never_contacted = None
        reason_1 = "TODO: one sentence a marketing lead would repeat"
        print("TODO 1 is open" if never_contacted is None else f"never_contacted is 1 in {never_contacted.mean():.1%} of rows")
        '''),
        md("""
        ## Which line marks a previous success?
        `poutcome` says how the client's previous campaign ended: `success`, `failure` or
        `nonexistent`. Build a 0 or 1 flag for a previous success and give its reason.
        """),
        code('''
        # TODO 2: replace None with the line that is 1 when the previous campaign ended in success.
        #   (A) (bank["poutcome"] == "success").astype(int)
        #   (B) (bank["poutcome"] != "failure").astype(int)
        #   (C) (bank["y"] == "yes").astype(int)
        prior_success = None
        reason_2 = "TODO: one sentence a marketing lead would repeat"
        print("TODO 2 is open" if prior_success is None else f"prior_success is 1 in {prior_success.mean():.1%} of rows")
        '''),
        md("""
        ## Which of three columns pass the prediction-time question?
        On the morning the call list is made, do we know this value for this client? Write
        `"known"` or `"not known"` for each column, and the system that writes it.
        """),
        code('''
        # TODO 3: fill each pair as ("known" or "not known", "the system that writes it and when").
        audit = {"duration": None, "euribor3m": None, "poutcome": None}
        open_items = [c for c, v in audit.items() if v is None]
        print("TODO 3 is open for:", open_items if open_items else "nothing; run the check cell")
        '''),
        md("""
        ## Did the room's answers hold?
        Run this once the three TODO cells are filled. It reports each answer and, when all three
        are in, scores the honest feature set with the two new flags.
        """),
        code('''
        if never_contacted is None or prior_success is None or None in audit.values():
            print("Waiting: fill TODO 1, 2 and 3 above, then run this cell again.")
        else:
            check("never_contacted is 1 for about 96 percent of rows", 0.95 < never_contacted.mean() < 0.97)
            check("prior_success is 1 for about 3 percent of rows", 0.03 < prior_success.mean() < 0.04)
            check("duration is the column that is not known", audit["duration"][0] == "not known"
                  and audit["poutcome"][0] == "known")
        '''),
        md("""
        ---
        ## What is the worked answer?
        **TODO 1 is B.** Reason: "most clients have never heard from us, and the ones who have
        convert far more often." Option A marks clients contacted zero days ago; option C turns a
        sentinel into a fake number of days.

        **TODO 2 is A.** Reason: "a client who said yes last time is the warmest call we have."
        Option B also marks the 35,563 clients with no previous campaign; option C copies the
        target into a feature, which is the leak in its purest form.

        **TODO 3.** `duration` is not known (the call log writes it when the call ends);
        `euribor3m` is known (the research desk publishes it daily, before the call), with the
        calendar caveat of case 2; `poutcome` is known (the previous campaign closed months before).
        """),
        code('''
        never_contacted = (bank["pdays"] == 999).astype(int)
        prior_success = (bank["poutcome"] == "success").astype(int)
        audit = {"duration": ("not known", "call log, when the call ends"),
                 "euribor3m": ("known", "research desk, published daily"),
                 "poutcome": ("known", "campaign history, when the last campaign closed")}
        bank = bank.assign(never_contacted=never_contacted, prior_success=prior_success)
        train, val, test = week_split(bank)
        y_train, y_val = (train["y"] == "yes").astype(int), (val["y"] == "yes").astype(int)
        def auc(cols):
            model = logistic(cols, train).fit(train[cols], y_train)
            return round(roc_auc_score(y_val, model.predict_proba(val[cols])[:, 1]), 4)
        before = auc(PROFILE + HISTORY + ECONOMY)
        after = auc(PROFILE + HISTORY + ECONOMY + ["never_contacted", "prior_success"])
        print(f"customer table + economy: {before}; with the two flags: {after}")
        check("never_contacted is 1 for about 96 percent of rows", 0.95 < never_contacted.mean() < 0.97)
        check("prior_success is 1 for about 3 percent of rows", 0.03 < prior_success.mean() < 0.04)
        check("duration is the column that is not known", audit["duration"][0] == "not known" and audit["poutcome"][0] == "known")
        '''),
        code('''
        rates = pd.DataFrame({
            "never contacted": [bank.loc[never_contacted == 1, "y"].eq("yes").mean(), bank.loc[never_contacted == 0, "y"].eq("yes").mean()],
            "previous success": [bank.loc[prior_success == 0, "y"].eq("yes").mean(), bank.loc[prior_success == 1, "y"].eq("yes").mean()],
        }, index=["flag = 1 / 0", "flag = 0 / 1"])
        fig, axes = plt.subplots(1, 2, figsize=(9, 3.2))
        for ax, (name, a, b, la, lb) in zip(axes, [
                ("never_contacted", rates.iloc[0, 0], rates.iloc[1, 0], "never (1)", "contacted (0)"),
                ("prior_success", rates.iloc[0, 1], rates.iloc[1, 1], "no success (0)", "success (1)")]):
            ax.bar([la, lb], [a, b], color=[GREY, VIOLET])
            for i, v in enumerate([a, b]):
                ax.text(i, v + 0.01, f"{v:.0%}", ha="center", fontsize=11)
            ax.set_ylim(0, 0.8); ax.set_title(f"yes-rate by {name}")
        plt.tight_layout(); plt.show()
        '''),
        md("""
        **What the room should say aloud.** Both flags pass the prediction-time question and carry
        a reason; the AUC barely moves because `poutcome` and `pdays` already held the signal, and
        the flags make it readable. The flip: if a flag's reason cannot be said in one sentence to
        the campaign head, it does not ship, whatever it adds.
        """),
    ]
    build(NB / "C2_W05_D03_guided_two_features_three_columns_STUDENT.ipynb", cells, timeout=600)


BUILDERS = {"guided": guided, "case01": case01, "case02": case02, "case03": case03,
            "ch01": ch01, "ch02": ch02, "ch03": ch03, "ch04": ch04, "ch05": ch05}

if __name__ == "__main__":
    wanted = sys.argv[1:] or list(BUILDERS)
    for name in wanted:
        BUILDERS[name]()
        print("built", name)
