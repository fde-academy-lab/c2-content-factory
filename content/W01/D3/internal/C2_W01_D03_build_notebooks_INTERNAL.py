"""Build Wednesday's notebooks: six chapters, the escalated case and the second case.

Run from the repository root:
    python3 content/W01/D3/internal/C2_W01_D03_build_notebooks_INTERNAL.py            every notebook
    python3 content/W01/D3/internal/C2_W01_D03_build_notebooks_INTERNAL.py c1 c4       named ones only

Each chapter notebook pairs with the deck section of the same number and title, and each starts
from the state the one before it reached, so notebook 04 opens on the identity rule notebook 03
built. Every chapter runs the need, the options with their sizing, the build, the trap, the second
route and Kavya's review. Each is executed cold in its own folder by scripts/nb_make.py. The TODO
twins are written unexecuted and their solution twins executed. No cell prints a planted record:
every discovery of one sits in an empty your-turn cell, and a mechanism that needs a plant to show
runs on invented records labelled invented.
"""
import pathlib
import re
import sys
import textwrap

sys.path.insert(0, "scripts")
from nb_make import SETUP, build, code, empty, md  # noqa: E402

DAY = pathlib.Path("content/W01/D3")
NB = DAY / "notebooks"
SOL = DAY / "exercises" / "solutions"

CHAPTERS = ["what the ERP sent", "the rows that repeat", "the copy that stays",
            "what is missing or malformed", "the bridge to the books", "the log the analyst audits"]

# ----------------------------------------------------------------------------- the carried code
READ = SETUP + '''
import csv, json, math
from collections import Counter
from datetime import date

DATA = kit.data_dir()
ORDERS_CSV = DATA / "C2_W01_D03_orders_STUDENT.csv"
BOOKS_Q1 = 19000000        # Anand's Q1 to the rupee, which his analyst sends on request

def read_orders(path=ORDERS_CSV):
    """Every row of an export as a dictionary of text, with the file line it came from."""
    with open(path, newline="", encoding="utf-8") as f:
        return [dict(row, line=n) for n, row in enumerate(csv.DictReader(f), start=2)]

def convert(value):
    """A whole number of rupees, or None with the reason, so a failure is counted, never hidden."""
    try:
        return int(value), ""
    except (TypeError, ValueError):
        return None, "amount does not convert to a whole number"

def Q(rows, quarter):
    """Rupees in a quarter over the amounts that convert."""
    return sum(convert(r["amount"])[0] or 0 for r in rows if r["quarter"] == quarter)
'''

PROFILE = '''
FIELDS = ["order_id", "customer_id", "segment", "channel", "city", "order_date", "amount",
          "status", "quarter", "discount"]
NUMERIC = {"amount", "discount"}

def profile(rows, fields=FIELDS):
    """Per field: present, convertible where the field is a number, and distinct."""
    out = {}
    for f in fields:
        present = [r.get(f, "") for r in rows if r.get(f, "") not in ("", None)]
        ok = [v for v in present if convert(v)[0] is not None] if f in NUMERIC else present
        out[f] = {"present": len(present), "convertible": len(ok), "distinct": len(set(present))}
    return out
'''

RULE = '''
def identity_rule(rows, key="order_id"):
    """One row per order: the first copy whose amount converts stays, and every other row is logged."""
    groups = {}
    for r in rows:
        groups.setdefault(r[key], []).append(r)
    kept, log = [], []
    for k, rs in groups.items():
        valid = [r for r in rs if convert(r["amount"])[0] is not None]
        keep = (valid or rs)[0]
        kept.append(keep)
        for r in rs:
            if r is keep:
                continue
            differs = [f for f in r if f != "line" and r[f] != keep[f]]
            reason = ("copy whose amount does not convert; its twin carries the value"
                      if convert(r["amount"])[0] is None else "second copy of the order")
            if differs and "amount" not in differs:
                reason += "; differs on " + ", ".join(differs)
            log.append({"line": r["line"], "order_id": k, "quarter": r["quarter"], "segment": r["segment"],
                        "amount": r["amount"], "rule": key, "reason": reason, "kept_line": keep["line"]})
    return kept, log
'''

PASS = '''
def clean_pass(raw):
    """The day's pass: the identity rule, then conversion with a rejects log, then flags."""
    kept, set_aside = identity_rule(raw)
    clean, rejects, flags = [], [], []
    for r in kept:
        value, reason = convert(r["amount"])
        if value is None:
            rejects.append({"line": r["line"], "order_id": r["order_id"], "field": "amount",
                            "value": r["amount"], "reason": reason})
            continue
        if not r["status"]:
            flags.append({"line": r["line"], "order_id": r["order_id"], "field": "status",
                          "decision": "keep and flag", "why": "booked revenue; its fate is unknown"})
        clean.append(dict(r, amount=value))
    return clean, set_aside, rejects, flags

def per_customer(rows, quarter, segment):
    rs = [r for r in rows if r["quarter"] == quarter and r["segment"] == segment]
    return len(rs) / len({r["customer_id"] for r in rs})
'''


def setup_cell(parts, state):
    return code("".join(parts) + "\n" + state)


def mapcell(n, levels, lit=0):
    ladder = ", ".join(f'"{c}"' for c in CHAPTERS)
    steps = ", ".join(f'"{s}"' for s in levels)
    return code(f'''kit.side_by_side(
    kit.ladder([{ladder}], lit={n - 1}, show=False),
    kit.vflow([{steps}], lit={lit}, show=False),
)''')


def opener(n, title, need, prev):
    need = textwrap.indent(textwrap.dedent(need).strip(), "    ")[4:]
    return md(f'''
    # {n}. {title}

    **Week 1, Wednesday. Chapter {n} of 6.** {prev}

    > **The client asks.** "Your dashboard says Q1 was Rs 2.1 crore. Our books say 1.9. Until your
    > numbers match ours, Finance will not act on a drop measured from an ERP export. Send me a
    > reconciliation."
    >
    > Anand Iyer, finance controller, Kalpa Retail

    {need}

    Kalpa Retail's business, its metrics and who decides what are in the retail dossier,
    `content/W01/D1/study-notes/C2_W01_D01_domain_retail_STUDENT.md`; this notebook assumes it.
    ''')


# ============================================================================= chapter 1
def ch1():
    return [
        opener(1, "What the ERP actually sent", '''
        **The need.** Revenue for Q1 is booked value in rupees, and two systems disagree on it by about
        Rs 20 lakh. Anand will not let Kalpa act on Tuesday's drop until the gap is explained, and
        Marketing loses a month for every week the argument runs. Before anyone totals anything, the
        question is what the ERP sent: how many records, how many complete, how many readable as
        numbers, how many distinct. A wrong answer here costs the most, because every later number is
        built on it.

        **Who else faces it.** Target Canada launched in March 2013, lost almost a billion dollars in its first
        year and in January 2015 announced it would close all 133 stores (CBC News, 15 January 2015, checked
        30 Sep 2026).
        Salsify's summary of the Canadian Business investigation puts the accuracy of the product data
        in its new system at about 30 percent, against 98 to 99 percent in the US (checked 30 Sep 2026).
        Data loaded in a hurry during a system change is the kind that needs counting before anyone
        trusts it, and Kalpa's export was stitched during a migration.
        ''', "Tuesday's finding, Retail-Plus orders per customer down 49 percent, was measured on the "
             "export exactly as delivered. This chapter profiles what arrived, before any total."),
        md('''
        **Setup.** The cell finds the shared helper `kit` and defines the day's first tools:
        `read_orders()` reads an export into dictionaries and remembers each row's file line, and
        `convert()` turns an amount into rupees or says why it could not. Nothing here prints a record.
        '''),
        setup_cell([READ, PROFILE], 'raw = read_orders()\nprint(len(raw), "rows read from", ORDERS_CSV.name)'),
        mapcell(1, ["the options\\nhow to learn what arrived", "1. everything read is text",
                    "2. the profile\\npresent, convertible, distinct", "3. the trap\\nthe largest order, sorted as text",
                    "4. convert on purpose\\nfailures logged", "5. a second witness\\nthe JSON feed",
                    "a second route\\nthe same counts another way"]),
        md('''
        ## The options

        Four ways a team could find out what the ERP sent, each sized on this file below.

        | Option | What it does | What it can miss |
        |---|---|---|
        | a) Total it and compare | Sum the amounts, set the sum beside Rs 1.9 crore | Why the two differ, and any amount that is not a number |
        | b) Scroll it in a spreadsheet | Read every cell by eye | A repeated order id a hundred rows away from its twin |
        | c) Spot-check a sample | Pick 20 rows and tie each to the books | Anything outside the 20 |
        | d) Profile every field | Count present, convertible and distinct values per field | Which copy of a repeated order is the right one |
        '''),
        code('''
        cells = len(raw) * len(FIELDS)
        # a repeat is recognisable only when both copies of a pair are drawn: 15 pairs among 201 rows
        p_sample_copy = sum((-1) ** (k + 1) * math.comb(15, k) * math.comb(201 - 2 * k, 20 - 2 * k) / math.comb(201, 20)
                            for k in range(1, 11))
        p_sample_bad = 20 / len(raw)                                     # one unreadable amount
        sizing = [
            ("a) total and compare", "201 amounts", "under a second", "stops on the first unreadable amount; says nothing about why"),
            ("b) scroll it", f"{cells:,} cells by eye", "about 17 minutes at half a second a cell", "repeats far apart are missed"),
            ("c) sample 20 rows", "20 rows", "about 10 minutes of tying out", f"{p_sample_copy:.0%} chance to draw both copies of a pair, {p_sample_bad:.0%} to meet the bad amount"),
            ("d) profile every field", f"{cells:,} values by code", "under a second", "finds every count that does not fit; the choice of copy waits"),
        ]
        kit.table(["option", "what it reads", "time", "what it catches"], sizing,
                  caption="Each option sized on this export: 201 rows, 10 fields")
        kit.bars([("a) total", len(raw)), ("b) scroll", cells), ("c) sample 20", 20 * len(FIELDS)), ("d) profile", cells)],
                 lit=(3,), title="Values each option reads: b and d read all 2,010, and only d does it in under a second")
        '''),
        md('''
        **The best-fit call: d, then a sample where the profile points.** A profile reads every value
        in under a second and turns each defect into a count that does not fit, which is what a
        reconciliation needs first. The minutes in b and the 17 minutes of scrolling are an assumption
        of half a second a cell, labelled as illustrative. **The fact that would change it:** a file with
        no field that names an order. Then there is nothing to count distinct, and chapter 2's fuzzy
        match becomes the only way to find repeats.
        '''),

        md('''
        ## 1. Everything read from a file is text

        Opening the wrong name is the first thing that goes wrong on a Wednesday, and it costs two
        minutes: read the last line, check the folder, move on.

        **Predict before you run.** After `csv.DictReader` reads the file, what is the type of an amount?
        a) `int`, since the column holds numbers; b) `float`, since rupees can carry paise; c) `str`,
        since a CSV holds only text; d) it depends on the row.
        '''),
        code('''
        with kit.expect_error() as err:
            open("orders.csv")            # the name a hurried analyst types from memory

        first = raw[0]
        print({k: first[k] for k in ("order_id", "segment", "quarter", "amount")})
        print("the amount is held as", type(first["amount"]).__name__, repr(first["amount"]))
        segments = ["Retail-Core", "Retail-Plus", "Business", "Student"]
        rows_by = {q: [sum(1 for r in raw if r["quarter"] == q and r["segment"] == s) for s in segments]
                   for q in ("Q1", "Q2")}
        kit.columns(segments, [("Q1 rows", rows_by["Q1"]), ("Q2 rows", rows_by["Q2"])],
                    title="Rows in the export by segment and quarter, before anything is checked")
        '''),
        md('''
        **What happened.** The answer is c. The first call stops with `FileNotFoundError`, whose last line
        names the file Python looked for in the notebook's own folder; the exports live in `../data/`,
        which `read_orders()` already knows. The file reads as 201 rows, and the first amount is the
        text `'2200'`. Every value a CSV gives back is text until it is converted on purpose, so every
        sum, comparison and sort on an amount depends on a conversion somebody chose.
        '''),
        code('''
        kit.check("the export holds 201 rows", len(raw) == 201, f"{len(raw)}")
        kit.check("every value arrives as text", all(isinstance(v, str) for r in raw for k, v in r.items() if k != "line"))
        kit.check("the wrong name raised FileNotFoundError", err.name == "FileNotFoundError", err.name)
        '''),

        md('''
        ## 2. The profile: present, convertible, distinct

        **Predict before you run.** Which field shows the biggest gap between present and the 201 rows?
        a) `amount`, because money fields are messy; b) `discount`, which Tuesday met as optional;
        c) `order_id`, because keys have gaps; d) none, because an ERP export is complete.
        '''),
        code('''
        prof = profile(raw)
        kit.table(["field", "present", "convertible", "distinct"],
                  [(f, p["present"], p["convertible"] if f in NUMERIC else "text", p["distinct"])
                   for f, p in prof.items()], caption="The profile of the orders CSV: 201 rows")
        kit.bars([(f, prof[f]["present"]) for f in FIELDS], lit=(0, 6, 7, 9),
                 title="Values present per field, out of 201 rows")
        '''),
        md('''
        **What happened.** The answer is b: `discount` is present on 143 of 201 rows. Three smaller signals
        matter more for Anand. `order_id` is present on 201 rows and distinct on 186, so some orders
        appear more than once. `amount` is present on 201 and converts on 200. `status` is present on
        200. None of those is a total yet; each is a question a later chapter answers.
        '''),
        code('''
        kit.check("order_id repeats: fewer distinct ids than rows", prof["order_id"]["distinct"] < len(raw),
                  f'{prof["order_id"]["distinct"]} distinct of {len(raw)}')
        kit.check("one amount does not convert", prof["amount"]["present"] - prof["amount"]["convertible"] == 1)
        kit.check("status is missing on one row", len(raw) - prof["status"]["present"] == 1)
        '''),

        md('''
        ## 3. The trap: the largest order, sorted as text

        Anand's analyst audits the way auditors do: the largest orders first, since one of them can
        carry more rupees than a hundred small ones. The hurried analyst sorts Q2 by amount and sends the
        top three.

        **The plausible wrong answer.**
        '''),
        code('''
        q2 = [r for r in raw if r["quarter"] == "Q2"]
        hurried_top = sorted(q2, key=lambda r: r["amount"], reverse=True)[:3]
        kit.stats([(kit.rupees(int(hurried_top[0]["amount"])), "the largest Q2 order", "sorted as it was read"),
                   (", ".join(r["amount"] for r in hurried_top), "the top three sent", "for the analyst to tie out"),
                   ("0", "orders above Rs 10 lakh", "so the sample has no large order in it")],
                  caption="The hurried sort, as it would be sent")
        '''),
        md('''
        **Why it is wrong.** Text sorts character by character, so `'970'` beats `'2945460'` because `9`
        comes after `2`. The analyst would tie out three small orders and skip the orders that carry the
        quarter's money, and the audit would pass on the part of the file that matters least. The check
        asks a business question: can the largest Q2 order be smaller than every Business order, when
        Business sells in lakhs?
        '''),
        code('''
        business_min = min(convert(r["amount"])[0] for r in raw if r["segment"] == "Business" and convert(r["amount"])[0])
        kit.check("the text sort's largest order sits below the smallest Business order",
                  int(hurried_top[0]["amount"]) < business_min, f"{hurried_top[0]['amount']} against {kit.rupees(business_min)}")
        numeric_top = sorted((r for r in q2 if convert(r["amount"])[0]), key=lambda r: convert(r["amount"])[0], reverse=True)[:3]
        kit.strip([convert(r["amount"])[0] for r in q2 if convert(r["amount"])[0]], lo=0, hi=3000000,
                  markers=[("text sort says largest", int(hurried_top[0]["amount"]), "bad"),
                           ("largest as a number", convert(numeric_top[0]["amount"])[0], "good")],
                  title="Every Q2 order on one axis: the text sort picks the wrong end")
        kit.check("sorted as numbers, the largest Q2 order is above Rs 25 lakh", convert(numeric_top[0]["amount"])[0] > 2500000,
                  kit.rupees(convert(numeric_top[0]["amount"])[0]))
        '''),
        md('''
        **The fix, and what changed.** Convert before sorting. The largest Q2 order moves from Rs 970 to
        Rs 29,45,460, and the top three now carry Rs 62,11,460 of the quarter's rupees instead of
        Rs 9,53,940. Chapter 5 comes back to that largest order.

        > **Kavya's review.** "Any sort, max or comparison on an amount you have not converted is a sort
        > on spelling. Convert once, at the door, and never again inside the analysis."
        '''),

        md('''
        ## 4. Convert on purpose, with every failure logged

        **Your turn, two minutes.** Type these lines into the empty cell and run them. The loop stops with
        a `ValueError`; read the last line aloud and write down the value it names. That is an error,
        met and read, and the lesson is the next cell.

        ```python
        total = 0
        for r in raw:
            total += int(r["amount"])
        ```
        '''),
        empty(),
        md('''
        **Predict before you run.** `convert()` returns a number or a reason. After it runs on all 201
        amounts, what should Q1 over the amounts that convert be? a) Rs 1,90,00,000, the books;
        b) Rs 2,09,98,210, the dashboard's 2.1 crore; c) zero, since one failure stops the total;
        d) something between the two.
        '''),
        code('''
        accepted, rejects = [], []
        for r in raw:
            value, reason = convert(r["amount"])
            if value is None:
                rejects.append({"line": r["line"], "order_id": r["order_id"], "field": "amount", "reason": reason})
            else:
                accepted.append(dict(r, amount=value))
        kit.stats([(f"{len(accepted)} + {len(rejects)}", "accepted and logged", f"of {len(raw)} rows"),
                   (kit.rupees(Q(accepted, "Q1")), "Q1, amounts that convert", "the dashboard's 2.1 crore"),
                   (kit.rupees(BOOKS_Q1), "Q1, the books", "Anand's 1.9 crore")])
        kit.flow(["read the text\\n201 amounts", "convert on purpose\\nconvert() returns a reason",
                  "accepted\\n200 numbers", "rejects log\\nline, field, reason"],
                 kinds=[None, None, None, "good"], title="A failure is counted and kept, never turned into a number")
        kit.check("accepted plus rejected is every row", len(accepted) + len(rejects) == len(raw), f"{len(accepted)} + {len(rejects)}")
        kit.check("Q1 over the amounts that convert is the dashboard's figure", Q(accepted, "Q1") == 20998210)
        '''),
        md('''
        **What happened.** The answer is b. The dashboard's 2.1 crore is honest arithmetic on this file:
        Rs 2,09,98,210, Rs 19,98,210 above the books. The rejects log holds one line, and the gap is
        a hundred times larger than any one Retail order, so an unreadable amount cannot explain it.
        The repeated order ids can, and chapter 2 weighs them.
        '''),

        md('''
        ## 5. The harder variant: the JSON feed as a second witness

        The ERP also sent the app's JSON feed. `json.load` stops with a `JSONDecodeError`.

        **Your turn, two minutes.** Type `json.load(open(DATA / "C2_W01_D03_orders_STUDENT.json"))` into the
        empty cell, run it, read the line and column in the last line, and open the file there.
        '''),
        empty(),
        md('''
        **Predict before you run.** The code below reads the feed one complete record at a time and stops
        at the first that is not complete. How should the feed be used? a) in place of the CSV; b) as a
        second witness, compared field by field for the orders it holds; c) not at all; d) merged into
        the CSV so nothing is lost.
        '''),
        code('''
        text = (DATA / "C2_W01_D03_orders_STUDENT.json").read_text(encoding="utf-8")
        decoder, feed, at = json.JSONDecoder(), [], text.index("{")
        while True:
            try:
                record, end = decoder.raw_decode(text, at)
            except json.JSONDecodeError:
                break                         # the first record that is not complete ends the read
            feed.append(record)
            at = text.find("{", end)
            if at == -1:
                break
        feed_prof = profile(feed)
        pct = lambda n, d: round(100 * n / d, 1)
        shown = ("order_id", "status", "amount", "discount")
        kit.columns(list(shown), [("CSV, % present", [pct(prof[f]["present"], len(raw)) for f in shown]),
                                  ("JSON feed, % present", [pct(feed_prof[f]["present"], len(feed)) for f in shown])],
                    fmt=lambda v: f"{v:.0f}%", title="Presence per field in the two sources")
        csv_ids = {r["order_id"] for r in raw}
        kit.check("the feed yields 119 complete records", len(feed) == 119, f"{len(feed)}")
        kit.check("every feed record is an order the CSV holds", all(r["order_id"] in csv_ids for r in feed))
        '''),
        md('''
        **What happened.** The answer is b. The feed yields 119 complete records, all orders the CSV holds,
        so it can confirm the CSV field by field for those orders and can never replace it. Missing looks
        different in each format: a CSV writes an absent value as an empty string, while JSON leaves the
        key out, so `record["status"]` can raise `KeyError` where the CSV returned `""`. The profile uses
        `.get(field, "")`, which counts both the same way.
        '''),

        md('''
        ## A second route: the same counts, reached another way

        The profile counted distinct ids with a set and failures with `convert()`. A `Counter` over the
        ids and the length of the rejects log reach the same two numbers by different code; if they
        disagree, one of the two is wrong.
        '''),
        code('''
        id_counts = Counter(r["order_id"] for r in raw)
        repeated = sum(n - 1 for n in id_counts.values())
        kit.table(["count", "the profile", "the second route"],
                  [("distinct order ids", prof["order_id"]["distinct"], len(id_counts)),
                   ("rows beyond one per id", len(raw) - prof["order_id"]["distinct"], repeated),
                   ("amounts that fail", prof["amount"]["present"] - prof["amount"]["convertible"], len(rejects))])
        kit.check("both routes find 186 distinct ids", len(id_counts) == prof["order_id"]["distinct"] == 186)
        kit.check("both routes find one amount that fails", len(rejects) == prof["amount"]["present"] - prof["amount"]["convertible"])
        '''),
        md('''
        **When to switch.** The profile is the route for a first look, since it asks every field the same
        three questions. The `Counter` is the route when one field matters, because it keeps how many
        times each id appears, which is where chapter 2 starts.

        > **Kavya's review.** "Before you total anything, tell me how many records you received, how many
        > are complete, how many convert and how many are distinct. A total from a file you have not
        > profiled is a guess with a comma in it."

        ### In the interview

        **[F] Everything read from a CSV is a string; what breaks and where do you convert?** "Arithmetic,
        comparison and sorting. Adding text to a number raises a TypeError; comparing `'970'` with
        `'2945460'` puts 970 on top; `max` on text returns whatever starts with the highest digit. I
        convert once, at the boundary, in one function that returns the value or the reason it failed,
        and I count and log the failures. I never turn a failure into a default without writing that
        decision down, because a zero is a claim about the business."

        **[S] How do you handle missing data?** "I measure it per field first: present, convertible,
        distinct. Then I ask what the absence means, and chapter 4 makes the decision."

        **Design. A new export has 2 crore rows. Profile everything, or sample?** "Profile everything. A
        profile is three counts per field, a few minutes of machine time, and it finds a defect wherever
        it sits; a sample of 1,000 rows has well under a one percent chance of meeting a single bad row.
        I would sample only to read rows the profile has already pointed at. What would switch me is a
        profile too slow for the deadline, and then I profile the key and the money fields first."

        ### Depth: look before you leap, or ask forgiveness

        Python offers two styles for a conversion. Look before you leap checks first, as `value.isdigit()`
        does, and rejects `"-2400"`, a valid integer. Easier to ask forgiveness tries the conversion and
        handles the exception, as `convert()` does, so the rule for a valid amount lives in one place.
        Real Python compares the two (https://realpython.com/python-lbyl-vs-eafp/, verified 03 Sep 2026).
        '''),
        code('''
        kit.table(["What chapter 1 established", "The number"],
                  [("Rows the ERP sent in the orders CSV", "201"),
                   ("Distinct order ids among them", "186"),
                   ("Amounts that convert, and failures logged", "200 and 1"),
                   ("Q1 over the amounts that convert", kit.rupees(Q(accepted, "Q1"))),
                   ("Complete records in the JSON feed", str(len(feed)))], caption="The profile, before anyone reconciles")
        kit.check_summary()
        print("Next: chapter 2 asks which rows repeat, and what makes two rows the same order.")
        '''),
    ]


# ============================================================================= chapter 2
INVENTED_DUPES = '''
# Invented records, to show the mechanism without touching the ERP file.
invented = [
    {"order_id": "INV-01", "segment": "Retail-Plus", "order_date": "2026-05-03", "amount": "2400"},
    {"order_id": "INV-02", "segment": "Retail-Core", "order_date": "2026-05-09", "amount": "1300"},
    {"order_id": "INV-01", "segment": "Retail-Plus", "order_date": "2026-05-03", "amount": "2400"},
    {"order_id": "INV-03", "segment": "Business", "order_date": "2026-06-11", "amount": "450000"},
    {"order_id": "INV-03", "segment": "Business", "order_date": "2026-06-11", "amount": "450000"},
]
for n, r in enumerate(invented, start=2):
    r["line"] = n
'''


def ch2():
    return [
        opener(2, "The rows that repeat", '''
        **The need.** Q1 as exported is Rs 2,09,98,210 and the books say Rs 1,90,00,000. The ERP team's
        note says the CSV was stitched from two extracts during the Q1 migration, and the profile found
        201 rows for 186 order ids. If orders were exported twice, Q1 revenue and Q1 order counts are
        both inflated, and so is every per-customer rate Tuesday computed. Anand's question is which
        rows repeat; answering it wrongly either keeps Rs 20 lakh that was never earned or deletes real
        orders from the books.

        **Who else faces it.** COMPANY_CH2
        ''', "Chapter 1 profiled the export: 201 rows, 186 distinct ids, one amount that does not convert, "
             "and Q1 at Rs 2,09,98,210 over the amounts that do. This chapter decides what makes two rows one order."),
        md('**Setup.** The helper and chapter 1\'s tools, so this notebook starts where chapter 1 ended.'),
        setup_cell([READ, PROFILE], 'raw = read_orders()\nprint(len(raw), "rows;", len({r["order_id"] for r in raw}), "distinct order ids")'),
        mapcell(2, ["the options\\nwhat makes two rows one order", "1. rows against orders\\nper quarter",
                    "2. the trap\\na dedupe that finds nothing", "3. the business key\\norder_id",
                    "4. the fuzzy key\\nsame count, other rows", "a second route\\ncount the copies another way"]),
        md('''
        ## The options

        | Option | Two rows are the same when | Where it comes from |
        |---|---|---|
        | a) The whole record | every field matches, as the rows now stand | Most tools' default dedupe |
        | b) The whole record less the line | every field but the file line matches | The first fix people reach for |
        | c) The business key | `order_id` matches | The ERP issues one id per order |
        | d) A fuzzy match | same customer and same amount, dated within 60 days | Record linkage when no key can be trusted |

        **Predict before you run.** Which options will flag the same number of rows as c? a) none;
        b) only b; c) only d; d) b and d.
        '''),
        code('''
        def flagged_by(rows, keyf):
            """The rows a key calls repeats; within a group the copy whose amount converts stays, as chapter 3 argues."""
            first, out = {}, []
            for r in rows:
                k = keyf(r)
                if k not in first:
                    first[k] = r
                elif convert(first[k]["amount"])[0] is None and convert(r["amount"])[0] is not None:
                    out.append(first[k]); first[k] = r
                else:
                    out.append(r)
            return out

        KEYS = {
            "a) whole record": lambda r: tuple(sorted(r.items())),
            "b) whole record less line": lambda r: tuple(sorted((k, v) for k, v in r.items() if k != "line")),
            "c) order_id": lambda r: r["order_id"],
        }
        by_key = {name: flagged_by(raw, f) for name, f in KEYS.items()}

        def fuzzy_flagged(rows, days=60):
            """A fuzzy match: same customer, same amount, dates within `days`. No key to group on, so every pair is compared."""
            out, comparisons = {}, 0
            for i, a in enumerate(rows):
                for b in rows[i + 1:]:
                    comparisons += 1
                    if (a["customer_id"] == b["customer_id"] and a["amount"] == b["amount"] and
                            abs((date.fromisoformat(a["order_date"]) - date.fromisoformat(b["order_date"])).days) <= days):
                        out[b["line"]] = b
            return list(out.values()), comparisons

        by_key["d) fuzzy match"], comparisons = fuzzy_flagged(raw)
        truth = {r["line"] for r in by_key["c) order_id"]}
        rows_out = []
        for name, flagged in by_key.items():
            lines = {r["line"] for r in flagged}
            kept = [r for r in raw if r["line"] not in lines]
            wrong = [r for r in flagged if r["line"] not in truth]
            rows_out.append((name, len(flagged), kit.rupees(Q(kept, "Q1")), kit.rupees(Q(kept, "Q2")),
                             len(truth - lines), kit.rupees(sum(convert(r["amount"])[0] or 0 for r in wrong)),
                             f"{comparisons:,} pairs" if name.startswith("d") else "201 lookups"))
        kit.table(["key", "rows flagged", "Q1 after", "Q2 after", "copies missed", "real rupees removed", "work"],
                  rows_out, caption="Each key sized on the ERP file; 'copies missed' is measured against the order_id key")
        kit.bars([(n, len(f)) for n, f in by_key.items()], lit=(2,), title="Rows each key flags as a repeat")
        '''),
        md('''
        **What happened.** The answer is c: the fuzzy match flags 15 rows, as many as the order id, and they
        are not the same 15. It removes one real Business order worth Rs 17,71,000, placed by a customer
        who spent the same amount again within 60 days, and it misses a pair whose amounts differ. The
        whole record flags nothing, and the whole record less the line flags 13 and misses two pairs.
        The fuzzy key also costs the most work: without a key to group on, every row is compared with
        every other, 20,100 pairs here and about 200 lakh crore on a file of 2 crore rows.

        **The best-fit call: c, the order id.** The ERP issues one id per order and never reuses it, so
        the id is what the business says an order is. **The fact that would change it:** two systems
        issuing their own ids, the app numbering from one and the stores numbering from one. The id alone
        would then merge different orders, and the key becomes the source system plus the id.
        '''),

        md('''
        ## 1. Rows against orders, quarter by quarter

        **Predict before you run.** Where do rows and distinct ids part company? a) evenly; b) mostly in
        Q1, the quarter of the migration; c) mostly in Q2; d) nowhere.
        '''),
        code('''
        by_q = {}
        for q in ("Q1", "Q2"):
            rows_q = [r for r in raw if r["quarter"] == q]
            by_q[q] = (len(rows_q), len({r["order_id"] for r in rows_q}))
        kit.columns(["Q1", "Q2"], [("rows", [by_q["Q1"][0], by_q["Q2"][0]]),
                                   ("distinct order ids", [by_q["Q1"][1], by_q["Q2"][1]])],
                    lit=(0,), title="Rows against distinct orders in each quarter")
        kit.check("Q1 carries 14 rows beyond one per order", by_q["Q1"][0] - by_q["Q1"][1] == 14)
        kit.check("Q2 carries 1", by_q["Q2"][0] - by_q["Q2"][1] == 1)
        '''),
        md('''
        **What happened.** The answer is b. Q1 holds 114 rows for 100 orders and Q2 holds 87 for 86, so the
        extra rows sit in the quarter the migration touched, which is where the dashboard and the books
        disagree. That is a lead, and the next step is to remove them.
        '''),

        md('''
        ## 2. The trap: a dedupe that reports zero duplicates

        Chapter 1's rejects log cited a file line, so every record carries `line`. The hurried analyst
        runs the default whole-record dedupe on those records.

        **The plausible wrong answer.**
        '''),
        code('''
        def whole_record_dedupe(rows):
            seen, kept = set(), []
            for r in rows:
                key = tuple(sorted(r.items()))
                if key not in seen:
                    seen.add(key)
                    kept.append(r)
            return kept

        kept_whole = whole_record_dedupe(raw)
        kit.stats([(str(len(raw) - len(kept_whole)), "duplicates found", "the whole-record dedupe"),
                   (kit.rupees(Q(kept_whole, "Q1")), "Q1 revenue", "unchanged, so the dashboard looks right"),
                   ("Rs 20 lakh", "left unexplained", "and the note says Finance is short")],
                  caption="The hurried dedupe, as it would be reported")
        '''),
        md('''
        **Why it is wrong.** The file line records where a row sat and says nothing about which order it is. Two copies of one
        order sit on different lines, so every record is unique and the dedupe can never find anything.
        The note would tell Anand his books are Rs 20 lakh short, sending Finance to hunt for revenue that
        was never earned. The check is chapter 1's: 201 rows and 186 ids cannot both be true of a file
        with no repeats. The mechanism, on five invented records in which two orders appear twice:
        '''),
        code(INVENTED_DUPES + '''
found = len(invented) - len(whole_record_dedupe(invented))
without_line = [{k: v for k, v in r.items() if k != "line"} for r in invented]
found_without = len(without_line) - len(whole_record_dedupe(without_line))
kit.table(["the comparison", "repeats found in the invented five"],
          [("every field, including the file line", found),
           ("every field except the file line", found_without),
           ("the order id alone", len(invented) - len({r["order_id"] for r in invented}))],
          caption="Invented records: the file line makes every row unique")
kit.check("the whole-record dedupe reports zero on the ERP file", len(raw) - len(kept_whole) == 0)
kit.check("yet distinct order ids fall 15 short of the rows", len(raw) - len({r["order_id"] for r in raw}) == 15)
kit.check("on invented records, leaving out the line finds both copies", found == 0 and found_without == 2)
'''),

        md('''
        ## 3. The fix: the business key

        **Predict before you run.** Grouped by `order_id`, how many groups hold more than one row? a) 14,
        one per extra Q1 row; b) 15; c) 186; d) 201.
        '''),
        code('''
        groups = {}
        for r in raw:
            groups.setdefault(r["order_id"], []).append(r)
        multi = {k: rs for k, rs in groups.items() if len(rs) > 1}
        sizes = Counter(len(rs) for rs in groups.values())
        kit.bars([(f"orders appearing {n} time{'s' if n > 1 else ''}", c) for n, c in sorted(sizes.items())],
                 lit=(1,), title="Orders by how many rows carry them")
        kit.columns(["Q1", "Q2"], [("groups of two", [sum(1 for rs in multi.values() if rs[0]["quarter"] == q) for q in ("Q1", "Q2")])],
                    title="Where the repeated orders sit")
        kit.check("15 orders appear twice, none three times", len(multi) == 15 and max(sizes) == 2)
        '''),
        md('''
        **What happened.** The answer is b: 15 orders appear exactly twice, 14 in Q1 and one in Q2. Each
        group of two is one order and a copy, and one row of each pair has to stay. Which one is chapter
        3's question.

        **Your turn.** In the empty cell, print the ids of the 15 orders and the file lines of both
        copies, with `[(k, [r["line"] for r in rs]) for k, rs in multi.items()]`. Say what the second
        line numbers have in common, and what that tells you about the migration.
        '''),
        empty(),

        md('''
        ## 4. The harder variant: the same count, other rows

        **Predict before you run.** The fuzzy key flags 15 rows and the order id flags 15. How many rows do
        the two sets share? a) 15; b) 14; c) 13; d) none.
        '''),
        code('''
        fuzzy = {r["line"] for r in by_key["d) fuzzy match"]}
        shared = fuzzy & truth
        kit.columns(["order_id key", "fuzzy key"], [("flagged", [len(truth), len(fuzzy)]), ("shared", [len(shared), len(shared)])],
                    title="Same count, different rows: 15 against 15, 14 in common")
        kit.check("the two keys share 14 of their 15 rows", len(shared) == 14, f"{len(shared)}")
        kit.check("the fuzzy key removes a real order worth Rs 17,71,000",
                  sum(convert(r["amount"])[0] or 0 for r in by_key["d) fuzzy match"] if r["line"] not in truth) == 1771000)
        '''),
        md('''
        **What happened.** The answer is b. A count that matches is not a match: the two keys agree on 14
        rows, and each has one the other does not. A reviewer who compared counts would have signed off
        a pass that removes Rs 17,71,000 of real Q2 revenue.
        '''),

        md('''
        ## A second route: count the copies with arithmetic

        The groups gave 15 repeated orders. Rows less distinct ids per quarter reaches the same number
        without grouping at all.
        '''),
        code('''
        arithmetic = sum(by_q[q][0] - by_q[q][1] for q in ("Q1", "Q2"))
        grouped = sum(len(rs) - 1 for rs in groups.values())
        kit.table(["route", "rows beyond one per order"], [("rows less distinct ids, per quarter", arithmetic),
                                                           ("groups by order_id", grouped)])
        kit.check("both routes find 15 rows beyond one per order", arithmetic == grouped == 15)
        '''),
        md('''
        **When to switch.** The arithmetic answers how many in one line and is the check to run first on
        any file. The groups answer which, and only they can feed a log.

        > **Kavya's review.** "Tell me what makes two rows the same order before you tell me how many
        > duplicates there are. A count of duplicates without an identity rule is a count of nothing."

        ### In the interview

        **[F] How do you find duplicates, and what makes two records the same?** "I start with the
        identity rule, not the tool. For an order that is the id the system issues; for a customer it
        might be a normalised email, for a payment the gateway's reference. Then I count rows against
        distinct keys. A whole-record comparison finds only exact copies, and a migration copy often
        differs somewhere: a timestamp, a load id, a line number. Then I weigh them, since two rows can
        carry more money than a hundred."

        **[F] A dedupe returns zero duplicates. Do you believe it?** "Only after checking it against a
        count of distinct keys. If rows and keys disagree, the dedupe compared on something that makes
        every row unique."

        **Design. Order id, whole record or fuzzy, for a customer table merged from two apps?** "Neither
        app's id identifies a person across both, so the whole record and the id are out. I would
        normalise email and phone and match on those, block by city so each record is compared only within its own city, which keeps the comparisons in the
        thousands, and send every fuzzy match a person has not confirmed to review. What would switch me
        back to a key is a shared customer id issued by one system."

        ### Depth: when the identity rule is more than one field

        Customer id and order date together is a composite key; on this file it finds 14 of the 15,
        because one pair's copies disagree on the date. Record linkage across systems starts the same
        way, by writing down what makes two records one before counting anything. Week 2 meets
        repeated keys again in a join, where they multiply rows instead of adding them.
        '''),
        code('''
        kit.flow(["rows against keys\\n201 rows, 186 ids", "the trap\\nthe line in the key",
                  "the business key\\n15 orders twice", "the fuzzy key\\n15, one of them real"], lit=2,
                 title="Chapter 2, from a count of rows to a rule for what an order is")
        kit.check_summary()
        print("Next: chapter 3 decides which copy of each pair stays, and what that does to Q1 to the rupee.")
        '''),
    ]


# ============================================================================= chapter 3
def ch3():
    return [
        opener(3, "The copy that stays", '''
        **The need.** Fifteen orders appear twice. For thirteen the two copies are identical and either may
        stay; for two they disagree, and the choice moves Q1 and a delivery date. Anand's analyst ties out
        to the rupee, so a choice that loses one order's amount turns a reconciliation into a finding
        against the team.

        **Who else faces it.** COMPANY_CH3
        ''', "Chapter 2 fixed the identity rule: an order is its order_id, and 15 orders appear twice. "
             "This chapter chooses which copy of each pair stays, and logs the other."),
        md('**Setup.** The helper, chapter 1\'s tools and the identity rule this chapter builds, defined once so later chapters reuse it.'),
        setup_cell([READ, PROFILE, RULE], 'raw = read_orders()\nprint(len(raw), "rows read")'),
        mapcell(3, ["the options\\nfirst, last, the one that validates", "1. three kinds of pair\\ninvented records",
                    "2. the rule on the ERP file", "3. the trap\\nQ1 ties, rows do not",
                    "4. weigh the rows\\nrows against rupees", "a second route\\na dict keyed by id"]),
        md('''
        ## The options

        | Option | Which copy stays | What it assumes |
        |---|---|---|
        | a) The first in the file | the row from the first extract | the first extract is the original |
        | b) The last in the file | the row from the second extract | the second extract corrected the first |
        | c) The copy that validates, then the first | a copy whose amount converts; the first if both do | a value beats no value; otherwise keep the original |
        | d) Keep both, escalate every pair | none until the ERP team answers | nobody inside Kalpa can decide |

        **Predict before you run.** Which options land Q1 on the books to the rupee? a) a only; b) b and c;
        c) c only; d) all four.
        '''),
        code('''
        def keep(rows, how):
            kept = {}
            for r in rows:
                k = r["order_id"]
                if k not in kept or how == "last":
                    kept[k] = r
                elif how == "validates" and convert(kept[k]["amount"])[0] is None and convert(r["amount"])[0] is not None:
                    kept[k] = r
            return list(kept.values())

        options = {"a) first": keep(raw, "first"), "b) last": keep(raw, "last"), "c) validates": keep(raw, "validates")}
        rows_out = [(name, kit.rupees(Q(k, "Q1")), kit.rupees(Q(k, "Q1") - BOOKS_Q1),
                     sum(1 for r in k if convert(r["amount"])[0] is None), "none") for name, k in options.items()]
        rows_out.append(("d) escalate all", "open", "open", 0, "15 pairs, days of waiting"))
        kit.table(["option", "Q1", "against the books", "unreadable orders kept", "questions to the ERP team"], rows_out,
                  caption="Each option sized on the ERP file")
        kit.bars([(n, abs(Q(k, "Q1") - BOOKS_Q1)) for n, k in options.items()], fmt=kit.rupees,
                 title="Rupees each option misses the books by")
        '''),
        md('''
        **What happened.** The answer is b. The first copy keeps a row whose amount cannot be read and lands
        Rs 1,790 short. The last copy lands on the books, and the copy that validates lands on the books;
        escalating everything leaves Q1 open for as long as the ERP team takes to answer 15 questions,
        13 of which have no question in them.

        **The best-fit call: c, and escalate only a pair whose valid copies disagree.** The last copy is
        right here because of the order the migration appended its rows, which is luck rather than a rule.
        **The fact that would change it:** the ERP team saying the second extract was a corrected re-run.
        Then b is the rule, and it is right for a reason.
        '''),

        md('''
        ## 1. Three kinds of pair, on invented records

        Pair A is an exact copy. In pair B one copy's amount does not convert and the other's does. In
        pair C both convert and the two disagree on the date.

        **Predict before you run.** For pair C, which copy should stay? a) the first, logged, and the date
        asked of the ERP team; b) the later date; c) neither; d) both.
        '''),
        code('''
        pairs = [
            {"order_id": "INV-11", "quarter": "Q1", "segment": "Retail-Core", "order_date": "2026-05-02", "amount": "1800", "line": 12},
            {"order_id": "INV-11", "quarter": "Q1", "segment": "Retail-Core", "order_date": "2026-05-02", "amount": "1800", "line": 90},
            {"order_id": "INV-12", "quarter": "Q1", "segment": "Retail-Plus", "order_date": "2026-05-14", "amount": "n/a", "line": 20},
            {"order_id": "INV-12", "quarter": "Q1", "segment": "Retail-Plus", "order_date": "2026-05-14", "amount": "2600", "line": 95},
            {"order_id": "INV-13", "quarter": "Q2", "segment": "Retail-Plus", "order_date": "2026-08-21", "amount": "3100", "line": 40},
            {"order_id": "INV-13", "quarter": "Q2", "segment": "Retail-Plus", "order_date": "2026-07-30", "amount": "3100", "line": 99},
        ]   # invented
        kept_pairs, log_pairs = identity_rule(pairs)
        kit.tree({"label": "rows sharing an order_id", "kind": "lit", "branches": [
            ("", {"label": "identical\\nkeep the first", "kind": "good"}),
            ("", {"label": "one amount unreadable\\nkeep the copy that validates", "kind": "good"}),
            ("", {"label": "valid, fields disagree\\nkeep the first, log, ask", "kind": "known"})]},
            title="Which copy stays: the rule, before the file")
        kit.table(["order", "kept line", "set aside", "reason"],
                  [(e["order_id"], e["kept_line"], e["line"], e["reason"]) for e in log_pairs],
                  caption="Invented pairs: one row per order, and a reason for every row set aside")
        kit.check("the unreadable copy of INV-12 is the one set aside", [e["line"] for e in log_pairs if e["order_id"] == "INV-12"] == [20])
        '''),
        md('''
        **What happened.** The answer is a. Keeping the first copy of pair B would keep the one that cannot
        be summed, so the rule prefers the copy that validates. In pair C both copies are valid and no rule
        inside the file can say which date is true, so the rule keeps the first extract's row, logs the
        disagreement and turns the date into a written question for the ERP team.
        '''),

        md('''
        ## 2. The rule on the ERP file

        **Predict before you run.** After the identity rule, Q1 is? a) Rs 2,09,98,210; b) Rs 1,89,98,210;
        c) Rs 1,90,00,000; d) Rs 2,00,00,000.
        '''),
        code('''
        kept, set_aside = identity_rule(raw)
        kit.columns(["Q1", "Q2"], [("as exported", [Q(raw, "Q1") / 1e5, Q(raw, "Q2") / 1e5]),
                                   ("one row per order", [Q(kept, "Q1") / 1e5, Q(kept, "Q2") / 1e5])],
                    fmt=lambda v: f"{v:,.2f} L", lit=(0,), title="Quarter revenue in lakh, before and after the identity rule")
        kit.stats([(str(len(kept)), "orders kept", "one row per order_id"),
                   (str(len(set_aside)), "rows set aside", "each with a reason"),
                   (kit.rupees(Q(kept, "Q1")), "Q1", "the books say Rs 1,90,00,000")])
        kit.check("186 orders kept and 15 rows set aside", (len(kept), len(set_aside)) == (186, 15))
        kit.check("Q1 lands on the books", Q(kept, "Q1") == BOOKS_Q1, kit.rupees(Q(kept, "Q1")))
        kit.check("no kept order has an amount that fails", all(convert(r["amount"])[0] is not None for r in kept))
        '''),
        md('''
        **What happened.** The answer is c. Q1 moves from Rs 2,09,98,210 to Rs 1,90,00,000, Finance's 1.9
        crore to the rupee, and Q2 from Rs 1,87,03,710 to Rs 1,87,00,000. The amount chapter 1 could not
        read turned out to be one copy of a pair whose twin carries the value, so no revenue went with it.

        **Your turn.** In the empty cell, print the log rows whose reason is more than "second copy of the
        order": `[(e["line"], e["order_id"], e["reason"]) for e in set_aside if e["reason"] != "second copy of the order"]`.
        For each, write the question you would send the ERP team.
        '''),
        empty(),

        md('''
        ## 3. The trap: Q1 ties to the books, so the pass must be right

        Chapter 2 showed that leaving the line out of the whole record finds copies. The hurried analyst
        does exactly that, sees Q1 land on the books, and stops.

        **The plausible wrong answer.**
        '''),
        code('''
        seen, exact = set(), []
        for r in raw:
            k = tuple(sorted((f, v) for f, v in r.items() if f != "line"))
            if k not in seen:
                seen.add(k)
                exact.append(r)
        kit.stats([(kit.rupees(Q(exact, "Q1")), "Q1", "equal to the books, to the rupee"),
                   (str(len(exact)), "orders in the clean file", "reported as orders"),
                   (kit.rupees(Q(exact, "Q2")), "Q2", "sent on to Marketing")],
                  caption="The whole record less the line, as it would be reported")
        '''),
        md('''
        **Why it is wrong.** Q1 ties because the two pairs this pass misses happen to cost Q1 nothing: one
        copy's amount cannot be read, so it adds nothing to the sum. The file still holds 188 rows for 186
        orders. One Q2 order is counted twice, so Q2 is Rs 3,710 high and the Retail-Plus Q2 order count
        is one too many, and an order with an unreadable amount sits in the clean file as an order. A
        rupee tie on one quarter proves that quarter's rupees; it cannot prove the rows. The check is the
        one chapter 2 taught: rows kept against distinct ids.
        '''),
        code('''
        kit.check("the hurried pass keeps more rows than there are orders", len(exact) > len({r["order_id"] for r in exact}),
                  f"{len(exact)} rows, {len({r['order_id'] for r in exact})} ids")
        kit.check("the hurried Q2 is Rs 3,710 above one row per order", Q(exact, "Q2") - Q(kept, "Q2") == 3710)
        kit.columns(["rows kept", "distinct ids"], [("whole record less line", [len(exact), len({r["order_id"] for r in exact})]),
                                                   ("identity rule", [len(kept), len({r["order_id"] for r in kept})])],
                    title="The hurried pass ties in rupees and fails in rows")
        '''),
        md('''
        **The fix, and what changed.** The identity rule on `order_id`, preferring the copy that validates:
        186 rows for 186 orders, Q2 down Rs 3,710 to Rs 1,87,00,000, the unreadable row set aside with its
        reason, and one date written up as a question for the ERP team.
        '''),

        md('''
        ## 4. The harder variant: count the rows, weigh the rupees

        **Predict before you run.** Of the Rs 19,98,210 the rule removed from Q1, what share sits in
        Business rows? a) about a sixth, since they are 2 of 14; b) about half; c) nearly all; d) none.
        '''),
        code('''
        segs = ["Business", "Retail-Plus", "Retail-Core", "Student"]
        q1_aside = [e for e in set_aside if e["quarter"] == "Q1"]
        rows_removed = [sum(1 for e in q1_aside if e["segment"] == s) for s in segs]
        rupees_removed = [sum(convert(e["amount"])[0] or 0 for e in q1_aside if e["segment"] == s) for s in segs]
        kit.bars(list(zip(segs, rows_removed)), title="Q1 rows set aside, by segment")
        kit.bars(list(zip(segs, rupees_removed)), fmt=kit.rupees, lit=(0,), title="Rupees those rows carried")
        share = rupees_removed[0] / sum(rupees_removed)
        kit.check("Business rows carry over 95 percent of the rupees removed", share > 0.95, f"{share:.1%}")
        kit.check("Retail-Plus carries the most rows removed", rows_removed[1] == max(rows_removed), f"{rows_removed[1]} of {len(q1_aside)}")
        '''),
        md('''
        **What happened.** The answer is c. Two Business rows carry Rs 19,67,560 of Rs 19,98,210, about 98
        percent, and eleven Retail-Plus rows carry Rs 27,760. That split decides two conversations. Anand's
        gap is two corporate orders counted twice. Tuesday's finding is a different matter: most extra rows
        sit in Retail-Plus in Q1, the segment and quarter Tuesday compared, so its fall in orders per
        customer was measured on inflated Q1 counts. Chapter 5 recomputes it.
        '''),

        md('''
        ## A second route: a dict keyed by id

        A dictionary keeps one value per key, so building one from the valid rows is an identity rule in a
        line. It keeps the last valid copy, and it logs nothing.
        '''),
        code('''
        by_id = {r["order_id"]: r for r in raw if convert(r["amount"])[0] is not None}
        same_ids = set(by_id) == {r["order_id"] for r in kept}
        same_amounts = all(convert(by_id[r["order_id"]]["amount"])[0] == convert(r["amount"])[0] for r in kept)
        kit.table(["route", "orders", "Q1", "Q2", "rows logged"],
                  [("identity_rule", len(kept), kit.rupees(Q(kept, "Q1")), kit.rupees(Q(kept, "Q2")), len(set_aside)),
                   ("a dict keyed by id", len(by_id), kit.rupees(Q(by_id.values(), "Q1")), kit.rupees(Q(by_id.values(), "Q2")), 0)])
        kit.check("both routes keep the same 186 orders at the same amounts", same_ids and same_amounts)
        '''),
        md('''
        **When to switch.** The dict is the fast check that the rule's totals are right. It is never the
        pass itself, since it chooses silently and leaves Anand's analyst nothing to audit.

        > **Kavya's review.** "An identity rule, a preference for the copy that validates, and a reason on
        > every row you set aside. And when Q1 ties to the books, check the rows before you celebrate."

        ### In the interview

        **[F] Two copies of an order disagree. Which do you keep?** "The one whose fields validate; if
        both do, the one the business calls the original, and I log the disagreement and ask the owner
        of the source. I size the choice first: here keeping the first copy would have cost Rs 1,790."

        **Design. First copy, last copy or the one that validates?** "The copy that validates, then the
        first, with every set-aside row logged. Last copy happened to land on the books here, by file
        order. If the ERP team told me the second extract was a corrected re-run, I would switch to last
        and write that down as the reason."

        ### Depth: survivorship in a dedupe

        Every "keep one" rule is a choice about which record survives, and each survivor rule carries an
        assumption about the source: first means original, last means corrected, most complete means the
        fields are independent. Master-data tools call this the survivorship rule, and they ask for it to
        be written down per field.
        '''),
        code('''
        kit.check_summary()
        print("Next: chapter 4 decides what to do with values that are missing or cannot be read.")
        '''),
    ]


# ============================================================================= chapter 4
def ch4():
    return [
        opener(4, "What is missing or malformed", '''
        **The need.** The 186 kept orders still carry two kinds of defect. One order has no status, and
        Operations reads the delivered share of orders every week. Fifty-five orders have no discount,
        which Tuesday met. And the pass needs a policy for any amount that does not convert, because the
        next export will carry one without a twin. Each choice either keeps revenue whole, invents a fact
        or deletes one, and Anand's analyst will read every choice in the log.

        **Who else faces it.** COMPANY_CH4
        ''', "Chapter 3 kept 186 orders by the identity rule and set 15 rows aside; Q1 is Rs 1,90,00,000. "
             "This chapter decides each missing and malformed value, and writes the reason down."),
        md('**Setup.** The tools so far and the identity rule from chapter 3, so this notebook starts from the 186 kept orders.'),
        setup_cell([READ, PROFILE, RULE],
                   'raw = read_orders()\nkept, set_aside = identity_rule(raw)\n'
                   'clean = [dict(r, amount=convert(r["amount"])[0]) for r in kept]\n'
                   'print(len(clean), "orders kept;", len(set_aside), "rows set aside")'),
        mapcell(4, ["the options\\ntwo decisions, sized", "1. a missing status\\ndrop, default or flag",
                    "2. a missing discount\\nzero or unknown", "3. the trap\\ncoerced to zero",
                    "4. repair from a witness\\nonly an independent one", "a second route\\nthe profile against the logs"]),
        md('''
        ## The options

        Two decisions, each with its options.

        | A missing status | What it claims |
        |---|---|
        | a) Drop the order | the order never happened |
        | b) Default it to delivered | the order reached the customer |
        | c) Impute it from the customer's last order | the customer's history decides this order's fate |
        | d) Keep it and flag it unknown | the order happened and its fate is unknown |

        | An amount that does not convert | What it does |
        |---|---|
        | a) Coerce it to zero | the loop runs and the order is worth nothing |
        | b) Reject it to the log | the row leaves revenue, with a line and a reason |
        | c) Repair it by reading the text | a person or a parser turns the text into a number |
        | d) Repair it from an independent copy | a second source that carries the value supplies it |
        '''),
        code('''
        q2 = [r for r in clean if r["quarter"] == "Q2"]
        no_status = [r for r in q2 if not r["status"]]
        delivered = sum(1 for r in q2 if r["status"] == "delivered")
        status_opts = [("a) drop", Q(q2, "Q2") - sum(r["amount"] for r in no_status), len(q2) - 1, delivered),
                       ("b) default delivered", Q(q2, "Q2"), len(q2), delivered + 1),
                       ("c) impute from last order", Q(q2, "Q2"), len(q2), delivered + 1),
                       ("d) keep and flag", Q(q2, "Q2"), len(q2), delivered)]
        kit.table(["missing status", "Q2 revenue", "Q2 orders", "delivered", "delivered share"],
                  [(n, kit.rupees(v), o, d, f"{d / o:.1%}") for n, v, o, d in status_opts],
                  caption="The missing status, each option sized on Q2")
        coerced_kept = []
        seen = {}
        for r in raw:                       # coerce first, then keep the first copy, as a hurried pass would
            r2 = dict(r, amount=convert(r["amount"])[0] or 0)
            seen.setdefault(r2["order_id"], r2)
        coerced_kept = list(seen.values())
        amount_opts = [("a) coerce to zero", kit.rupees(Q(coerced_kept, "Q1") - BOOKS_Q1), "an order at Rs 0 in the clean file"),
                       ("b) reject to the log", "Rs 0 here, the whole order elsewhere", "revenue short until repaired"),
                       ("c) repair by reading", "see the invented case below", "a guess dressed as a value"),
                       ("d) repair from a copy", kit.rupees(Q(clean, "Q1") - BOOKS_Q1), "needs a copy that is independent")]
        kit.table(["unreadable amount", "Q1 against the books", "what it leaves"], amount_opts,
                  caption="The unreadable amount, each option sized on this export")
        kit.columns([n for n, *_ in status_opts], [("delivered orders", [d for *_, d in status_opts])],
                    title="Delivered orders in Q2 under each option: two of them invent a delivery")
        '''),
        md('''
        **The best-fit calls.** For the status, d: revenue is booked value whatever the status, so the order
        stays in revenue, and the flag keeps it out of the delivered count, which stays at 57 of 86. For the
        amount, b by default and d when an independent copy exists, which on this file it does: the
        identity rule already kept the twin that carries the value. **The facts that would change them:**
        for the status, a delivery system that can be asked, which turns the flag into a lookup; for the
        amount, a second export from the same extract, which is a copy of the defect and no witness at all.
        '''),

        md('''
        ## 1. A missing status

        **Predict before you run.** Which decision keeps Q2 revenue and the delivered share both honest?
        a) drop; b) default delivered; c) impute; d) keep and flag.
        '''),
        code('''
        flags = [{"field": "status", "decision": "keep and flag", "why": "booked revenue; its fate is unknown"} for _ in no_status]
        kit.line(["drop", "default", "impute", "flag"], [("delivered share of Q2 orders, %", [100 * d / o for _, _, o, d in status_opts], "good")],
                 fmt=lambda v: f"{v:.1f}%", lo=60, title="The delivered share moves with the choice; the axis starts at 60 percent")
        kit.check("exactly one kept order has no status", len(no_status) == 1)
        kit.check("keep and flag leaves Q2 whole", status_opts[3][1] == 18700000, kit.rupees(status_opts[3][1]))
        kit.check("only a default or an imputation adds a delivery", status_opts[1][3] == status_opts[2][3] == delivered + 1)
        '''),
        md('''
        **What happened.** The answer is d. Dropping removes a booked order that Finance has; defaulting and
        imputing each add a delivery nobody recorded, lifting the delivered share from 66.3 to 67.4 percent.
        Keep and flag leaves Q2 at Rs 1,87,00,000 and writes one line in the flags log.
        '''),

        md('''
        ## 2. A missing discount: zero, or unknown?

        Tuesday's trap read a missing discount as zero. Revenue here is the booked amount, so the discount
        does not move it; it moves any average discount a report quotes.

        **Predict before you run.** The average discount over orders that carry one, against the average
        with the missing ones read as zero: how far apart? a) the same; b) a few rupees; c) about 30
        percent lower with zeros; d) higher with zeros.
        '''),
        code('''
        with_disc = [int(r["discount"]) for r in clean if r["discount"] != ""]
        as_zero = with_disc + [0] * (len(clean) - len(with_disc))
        avg_known, avg_zero = sum(with_disc) / len(with_disc), sum(as_zero) / len(as_zero)
        kit.columns(["missing read as zero", "missing kept as unknown"], [("average discount, Rs", [avg_zero, avg_known])],
                    fmt=lambda v: f"Rs {v:.0f}", title="Average discount per order, two readings of the same file")
        kit.check("55 kept orders carry no discount", len(clean) - len(with_disc) == 55)
        kit.check("zeros pull the average down by over a quarter", avg_zero < 0.75 * avg_known, f"Rs {avg_zero:.0f} against Rs {avg_known:.0f}")
        '''),
        md('''
        **What happened.** The answer is c. Reading 55 absences as zero pulls the average from about Rs 67 to
        about Rs 47. The decision is keep and flag: revenue does not need the field, and any discount
        figure is quoted over the orders that carry one, with the count beside it.
        '''),

        md('''
        ## 3. The trap: coerce every failure to zero, and the file looks clean

        **The plausible wrong answer.** The `ValueError` from chapter 1 stops the loop, so the hurried
        analyst writes a helper that turns anything unreadable into zero, then runs the same first-copy
        dedupe everybody reaches for.
        '''),
        code('''
        def to_int(value):
            try:
                return int(value)
            except ValueError:
                return 0                     # "so the loop does not crash"

        coerced = [dict(r, amount=to_int(r["amount"])) for r in raw]
        failures = sum(1 for r in coerced if not isinstance(r["amount"], int))
        kit.stats([(f"{len(raw) - failures} of {len(raw)}", "amounts convert", "the coerced profile"),
                   ("0", "rows in the rejects log", "nothing to explain"),
                   (kit.rupees(Q(coerced_kept, "Q1")), "Q1 after the dedupe", "rounds to 1.9 crore")],
                  caption="The coerced pass, as it would be reported")
        '''),
        md('''
        **Why it is wrong.** A zero is a claim that Kalpa sold that order for nothing. Once the unreadable
        copy is worth Rs 0 it passes as valid, the identity rule can no longer tell it from its twin, the
        first copy wins, and Q1 lands Rs 1,790 short with an order at Rs 0 in a file the note calls clean.
        The profile's failure count went from one to zero while nothing was fixed. The check asks whether
        a Kalpa order can be worth nothing.
        '''),
        code('''
        smallest_real = min(r["amount"] for r in clean)
        zero_orders = [r for r in coerced_kept if r["amount"] == 0]
        kit.check("the coerced pass keeps an order at Rs 0", len(zero_orders) == 1, f"{len(zero_orders)} order")
        kit.check("no real order in the export is below Rs 600", smallest_real >= 600, f"the smallest is {kit.rupees(smallest_real)}")
        kit.check("the coerced pass misses the books by Rs 1,790", BOOKS_Q1 - Q(coerced_kept, "Q1") == 1790)
        kit.bridge(("the books", BOOKS_Q1), [("the valued copy thrown away", -1790)], end_label="coerced Q1",
                   lo=18990000, title="What the zero cost against the books; the axis starts at Rs 1.899 crore")
        '''),
        md('''
        **The fix, and what changed.** Reject to the log, then let the identity rule prefer the copy that
        validates: the Rs 0 order leaves the clean file, the twin with the value stays, and Q1 is back on
        the books. The profile reports one failure, which is the truth about the export.
        '''),

        md('''
        ## 4. The harder variant: repair only from an independent witness

        Two repairs look tempting. Reading the text as a number, on an invented pair in which the first
        copy says `fourteen` and the second `1400`:
        '''),
        code('''
        WORDS = {"fourteen": 14, "twenty": 20}
        invented_pair = [{"order_id": "INV-21", "amount": "fourteen"}, {"order_id": "INV-21", "amount": "1400"}]   # invented
        read_as_word = WORDS[invented_pair[0]["amount"]]
        kit.table(["repair", "value", "against the twin"], [("read the word", read_as_word, read_as_word - 1400),
                                                            ("take the twin", 1400, 0)], caption="Invented: a word is not an amount")
        kit.check("reading the word misses the invented order by Rs 1,386", 1400 - read_as_word == 1386)
        '''),
        md('''
        The other tempting repair is the JSON feed, which carries the same orders.

        **Predict before you run.** For the orders the feed holds, how many amounts agree with the clean
        file? a) all 119; b) 118, and the one that differs carries unreadable text; c) about half; d) none.
        '''),
        code('''
        text = (DATA / "C2_W01_D03_orders_STUDENT.json").read_text(encoding="utf-8")
        decoder, feed, at = json.JSONDecoder(), [], text.index("{")
        while True:
            try:
                record, end = decoder.raw_decode(text, at)
            except json.JSONDecodeError:
                break
            feed.append(record)
            at = text.find("{", end)
            if at == -1:
                break
        clean_by_id = {r["order_id"]: r["amount"] for r in clean}
        agree = sum(1 for r in feed if convert(r.get("amount"))[0] == clean_by_id.get(r["order_id"]))
        unreadable_in_feed = sum(1 for r in feed if convert(r.get("amount"))[0] is None)
        kit.bars([("feed amounts that agree", agree), ("feed amounts that cannot be read", unreadable_in_feed)],
                 title="The JSON feed against the clean file")
        kit.check("the feed agrees on 118 of 119", agree == 118)
        kit.check("the one it does not confirm is unreadable in the feed too", unreadable_in_feed == 1)
        '''),
        md('''
        **What happened.** The answer is b. The feed repeats the defect, because it was cut from the same
        extract, so it is a copy and no witness. The CSV's second extract carried the value, and the
        identity rule already used it. The rule for the log: repair only from a source that could not have
        copied the error, and name the source.
        '''),

        md('''
        ## A second route: the profile against the logs

        The profile counts defects in aggregate and the logs list them row by row. The two must agree.
        '''),
        code('''
        p = profile(clean)
        kit.table(["defect", "from the profile of the clean file", "from the logs"],
                  [("status missing", len(clean) - p["status"]["present"], len(flags)),
                   ("amount that fails", p["amount"]["present"] - p["amount"]["convertible"], 0),
                   ("discount missing", len(clean) - p["discount"]["present"], len(clean) - len(with_disc))])
        kit.check("the profile and the flags log agree on the status", len(clean) - p["status"]["present"] == len(flags))
        kit.check("no amount in the clean file fails", p["amount"]["convertible"] == len(clean))
        '''),
        md('''
        **When to switch.** The profile is how you find defects; the log is how you show them. Run the
        profile on the clean file at the end of every pass, and a defect that got past the log shows as a
        count that disagrees.

        > **Kavya's review.** "Drop, default, or keep and flag: each is a claim about the business. Write
        > the claim beside the decision. And never fill money."

        ### In the interview

        **[S] How do you handle missing data?** "Measure it per field, then ask what the absence means,
        because an absent discount and an absent status mean different things. Then one of three decisions
        with a written reason: drop, fill a stated default, or keep and flag. I size each on the numbers it
        moves: here dropping costs Rs 1,850 of booked revenue, a default adds a delivery nobody recorded,
        and keep and flag moves nothing and says so. For money I never fill."

        **Design. Coerce, reject or repair a malformed amount?** "Reject to a log by default, since a
        coerced zero is a false value and hides the defect from every later check. Repair only from an
        independent source, and name it. I would switch to repair-by-rule only for a known format issue,
        such as a thousands separator, where the rule is exact and tested."

        ### Depth: missing at random, or not

        Statisticians separate values missing completely at random from values whose absence depends on
        something, such as discounts left blank only by one channel. Only the first can be dropped without
        bending a rate. Imputation, filling a value from other records, belongs to model features with a
        column that marks the filled values; for Finance, the answer stays keep and flag.
        '''),
        code('''
        kit.check_summary()
        print("Next: chapter 5 draws the bridge from 2.1 to 1.9 and recomputes Tuesday on the clean file.")
        '''),
    ]


# ============================================================================= chapter 5
def ch5():
    return [
        opener(5, "The bridge to the books", '''
        **The need.** Anand asked which Q1 figure is right and how the team knows. Marketing asks whether
        Tuesday's finding survives, because a rescue campaign for Retail-Plus is waiting on it. The metrics
        are Q1 revenue to the rupee, the Q1 to Q2 change, and Retail-Plus orders per customer. A proof
        Finance cannot follow costs the team Anand's trust; a recompute that nobody runs lets Marketing
        spend on a number that was never true.

        **Who else faces it.** COMPANY_CH5
        ''', "Chapters 1 to 4 built the clean file: 186 orders, 15 rows set aside, one status flagged, Q1 on "
             "the books. This chapter proves it and recomputes Tuesday."),
        md('**Setup.** The whole pass so far, as `clean_pass()`, so this notebook starts from the clean file and its logs.'),
        setup_cell([READ, PROFILE, RULE, PASS],
                   'raw = read_orders()\nclean, set_aside, rejects, flags = clean_pass(raw)\n'
                   'print(len(clean), "orders;", len(set_aside), "set aside;", len(flags), "flagged")'),
        mapcell(5, ["the options\\nhow to prove it", "1. the bridge\\n2.1 to 1.9, move by move",
                    "2. Tuesday recomputed", "3. the trap\\nthe bulk order removed",
                    "4. the note to Finance", "a second route\\nbottom up"]),
        md('''
        ## The options

        | Option | What it offers Anand | What it leaves open |
        |---|---|---|
        | a) Take the books' figure | Finance's number, adopted | why the dashboard differs; Tuesday unchecked |
        | b) The difference of the totals | Rs 19,98,210, one subtraction | what the difference is made of |
        | c) A bridge, one move per cause | every rupee of the gap, each move backed by logged rows | nothing, if it closes |
        | d) Rebuild Q1 from the JSON feed | a second source's total | the feed stops at record 120 |
        '''),
        code('''
        text = (DATA / "C2_W01_D03_orders_STUDENT.json").read_text(encoding="utf-8")
        decoder, feed, at = json.JSONDecoder(), [], text.index("{")
        while True:
            try:
                record, end = decoder.raw_decode(text, at)
            except json.JSONDecodeError:
                break
            feed.append(record)
            at = text.find("{", end)
            if at == -1:
                break
        feed_q1 = sum(convert(r.get("amount"))[0] or 0 for r in feed if r["quarter"] == "Q1")
        sizing = [("a) the books' figure", "0", "no", "no"),
                  ("b) the difference", "2 totals", "yes, as a total", "no"),
                  ("c) a bridge by cause", f"{len(set_aside)} logged rows", "yes, to the rupee", "yes"),
                  ("d) rebuild from the feed", f"{len(feed)} records, Q2 barely covered", kit.rupees(feed_q1 - BOOKS_Q1) + " off", "no")]
        kit.table(["option", "rows behind it", "closes to the books", "says why"], sizing, caption="Each proof sized on this export")
        kit.bars([("feed records in Q1", sum(1 for r in feed if r["quarter"] == "Q1")),
                  ("feed records in Q2", sum(1 for r in feed if r["quarter"] == "Q2")),
                  ("clean orders in Q2", sum(1 for r in clean if r["quarter"] == "Q2"))],
                 title="Why the feed cannot carry the proof: it barely reaches Q2")
        '''),
        md('''
        **The best-fit call: c.** A bridge closes to the rupee and every move is a row in the log, so Anand's
        analyst can test each one. The feed is short by Rs 1,790 in Q1 because it carries the same
        unreadable amount, and it holds 19 of Q2's 86 orders. **The fact that would change it:** a bridge that
        does not close. Then the gap is the finding, and it may be Finance's books that miss a booked order.
        '''),

        md('''
        ## 1. The bridge from 2.1 to 1.9

        **Predict before you run.** How many moves does the bridge need to land on the books? a) one, the
        copies; b) two, the corporate copies and the consumer copies; c) three, adding the unreadable
        amount; d) none, since 2.1 rounds close enough.
        '''),
        code('''
        exported_q1 = Q(raw, "Q1")
        q1_aside = [e for e in set_aside if e["quarter"] == "Q1"]
        corporate = -sum(convert(e["amount"])[0] or 0 for e in q1_aside if e["segment"] == "Business")
        consumer = -sum(convert(e["amount"])[0] or 0 for e in q1_aside if e["segment"] != "Business")
        kit.bridge(("Q1 as exported", exported_q1),
                   [("copies of corporate orders", corporate), ("copies of consumer orders", consumer)],
                   end_label="Q1 clean, the books", lit=(0,), lo=18800000,
                   title="From the dashboard's 2.1 crore to the books' 1.9; the axis starts at Rs 1.88 crore")
        kit.check("the bridge lands on the books", exported_q1 + corporate + consumer == BOOKS_Q1)
        kit.check("the rows reconcile: in equals kept plus set aside", len(raw) == len(clean) + len(set_aside) + len(rejects))
        '''),
        md('''
        **What happened.** The answer is b. Copies of two corporate orders carry Rs 19,67,560 and copies of
        consumer orders Rs 30,650, and the bridge lands on Rs 1,90,00,000. The unreadable amount needs no
        move: it was never in the exported total, and its twin, which was, stayed.
        '''),

        md('''
        ## 2. Tuesday recomputed on the clean file

        Tuesday told the leadership group that revenue fell about 11 percent from Q1 to Q2 and that
        Retail-Plus orders per customer fell 49 percent, 2.32 to 1.18, both measured on the export as
        delivered.

        **Predict before you run.** On clean data, the Retail-Plus finding: a) disappears; b) survives,
        smaller; c) grows; d) moves to Retail-Core.
        '''),
        code('''
        segs = ["Retail-Core", "Retail-Plus", "Business", "Student"]
        tuesday = {"Retail-Core": -5.3, "Retail-Plus": -49.0, "Business": -15.0, "Student": 40.0}
        cleaned = {s: round(100 * (per_customer(clean, "Q2", s) / per_customer(clean, "Q1", s) - 1), 1) for s in segs}
        kit.table(["segment", "as Tuesday reported", "clean Q1", "clean Q2", "clean change"],
                  [(s, f"{tuesday[s]:+.1f}%", round(per_customer(clean, "Q1", s), 2), round(per_customer(clean, "Q2", s), 2),
                    f"{cleaned[s]:+.1f}%") for s in segs], caption="Orders per customer, Q1 to Q2")
        kit.columns(segs[:3], [("fall as Tuesday reported", [-tuesday[s] for s in segs[:3]]), ("fall on clean data", [-cleaned[s] for s in segs[:3]])],
                    fmt=lambda v: f"{v:.0f}%", lit=(1,), title="The fall in orders per customer, percent; Student rose and is left out")
        rev_dirty, rev_clean = 1 - 18700000 / 21000000, 1 - Q(clean, "Q2") / Q(clean, "Q1")
        kit.line(["Q1", "Q2"], [("as Tuesday reported, Rs lakh", [210.0, 187.0], "bad"),
                                ("on clean data, Rs lakh", [Q(clean, "Q1") / 1e5, Q(clean, "Q2") / 1e5], "good")],
                 lo=150, title="Revenue Q1 to Q2: an 11 percent fall becomes 1.6 percent; the axis starts at Rs 150 lakh")
        kit.check("Retail-Plus still falls on clean data", cleaned["Retail-Plus"] < -30, f"{cleaned['Retail-Plus']:+.1f}%")
        kit.check("the Retail-Plus fall is smaller than Tuesday reported", cleaned["Retail-Plus"] > tuesday["Retail-Plus"])
        kit.check("the revenue drop shrinks to under 2 percent", rev_clean < 0.02, f"{rev_clean:.1%} against {rev_dirty:.1%}")
        '''),
        md('''
        **What happened.** The answer is b. Retail-Plus orders per customer fall 35.0 percent on clean data,
        1.82 to 1.18, against the 49 Tuesday reported: the finding stands, smaller, because most copies sat
        in Retail-Plus in Q1. The revenue drop shrinks from 11.0 to 1.6 percent. Both go in the note, the
        smaller numbers first.
        '''),

        md('''
        ## 3. The trap: the real bulk order removed as an outlier

        **The plausible wrong answer.** Sorted as numbers, Q2's largest order sits far above the rest, 1.66
        times the next. The hurried analyst removes it "to be safe" and reports the quarter without it.
        '''),
        code('''
        q2_orders = sorted((r for r in clean if r["quarter"] == "Q2"), key=lambda r: r["amount"], reverse=True)
        top, runner_up = q2_orders[0], q2_orders[1]
        q2_trimmed = Q(clean, "Q2") - top["amount"]
        kit.stats([(kit.rupees(q2_trimmed), "Q2 without it", "the hurried figure"),
                   (f"{1 - q2_trimmed / BOOKS_Q1:.1%}", "the drop", "Q1 1.90 crore to Q2 1.58 crore"),
                   (f"{top['amount'] / runner_up['amount']:.2f}x", "the next largest", "why it looked wrong")])
        kit.strip([r["amount"] for r in q2_orders if r["segment"] == "Business"], lit=[0], lo=0, hi=3000000,
                  markers=[("next largest", runner_up["amount"], "plain")],
                  title="Q2's Business orders on one axis; the dark dot is the one a hurried analyst removes")
        '''),
        md('''
        **Why it is wrong.** Large is not wrong. Kalpa's Business segment sells in bulk to corporate buyers,
        every order in lakhs, so a Business order at Rs 29 lakh is the business doing what it does. Removing
        it turns a 1.6 percent dip into a 17.1 percent collapse: Marketing would fund a rescue for a fall
        that never happened, and Finance, whose books hold that order, would reject the reconciliation on
        sight. A fence is a cut-off above which a hurried analyst calls values outliers; the simplest is a
        multiple of the median, and the check below sizes one at three times the median Q2 order. The real
        check asks whether anything about the record is wrong, never whether it is big.
        '''),
        code('''
        buyer_orders = [r for r in clean if r["customer_id"] == top["customer_id"]]
        amounts_q2 = sorted(r["amount"] for r in q2_orders)
        median_q2 = amounts_q2[len(amounts_q2) // 2]
        fence_all = sum(1 for a in amounts_q2 if a > 3 * median_q2)    # a fence at three times the median
        kit.check("the largest Q2 order is a Business order", top["segment"] == "Business")
        kit.check("its customer ordered in both quarters", {r["quarter"] for r in buyer_orders} == {"Q1", "Q2"}, f"{len(buyer_orders)} orders")
        kit.check("a fence on the whole quarter would flag every Business order", fence_all == sum(1 for r in q2_orders if r["segment"] == "Business"),
                  f"{fence_all} flagged")
        kit.line(["Q1", "Q2"], [("every real order kept", [Q(clean, "Q1") / 1e5, Q(clean, "Q2") / 1e5], "good"),
                                ("the bulk order removed", [Q(clean, "Q1") / 1e5, q2_trimmed / 1e5], "bad")],
                 fmt=lambda v: f"{v:,.0f} L", lo=140, title="Quarter revenue in lakh: a dip, or a collapse invented by a fence")
        '''),
        md('''
        **The fix, and what changed.** Keep it, flag it, and show Q2 both ways. Q2 goes back from
        Rs 1,57,54,540 to Rs 1,87,00,000, and the drop from 17.1 percent to 1.6. A fence at three times the median
        Q2 order flags all 17 Business orders, because the quarter mixes a Rs 2,000 basket with a corporate order; a
        fence means something only inside one segment, and even there it is a question about a record.
        '''),

        md('''
        ## 4. The note to Finance

        **Predict before you run.** Which number leads the note? a) the 49 percent Tuesday reported, since
        leadership has seen it; b) the 1.9 crore and why it is right; c) the Rs 29 lakh order; d) the
        count of rows set aside.

        The answer is b: Anand asked which figure is right, so that goes first, then the proof, then what
        changed. Numbers first, which figure is right and why, both reconciliations, what was kept and flagged, and
        whether Tuesday survives, in under 120 words:

        > "Anand, your 1.9 crore is right. The ERP export counted fifteen orders twice, fourteen of them in
        > Q1; copies of two corporate orders carry Rs 19,67,560 of the Rs 19,98,210 difference. Rows
        > reconcile, 201 received equals 186 kept plus 15 set aside, and rupees reconcile to your books
        > exactly. Every row set aside and every decision is in the attached log. Kept and flagged: one Q2
        > order with no status, and the largest Q2 order, a real Business account. On clean data the Q1 to
        > Q2 drop is 1.6 percent, not 11, and the Retail-Plus frequency fall is 35 percent, not 49. It
        > survives, smaller."
        '''),
        code('''
        note = ("Anand, your 1.9 crore is right. The ERP export counted fifteen orders twice, fourteen of them in Q1; "
                "copies of two corporate orders carry Rs 19,67,560 of the Rs 19,98,210 difference. Rows reconcile, 201 "
                "received equals 186 kept plus 15 set aside, and rupees reconcile to your books exactly. Every row set "
                "aside and every decision is in the attached log. Kept and flagged: one Q2 order with no status, and "
                "the largest Q2 order, a real Business account. On clean data the Q1 to Q2 drop is 1.6 percent, not 11, "
                "and the Retail-Plus frequency fall is 35 percent, not 49. It survives, smaller.")
        kit.check("the note is under 120 words", len(note.split()) < 120, f"{len(note.split())} words")
        '''),

        md('''
        ## A second route: bottom up

        The bridge worked top down, from the export less the moves. Summing the kept orders reaches the same
        Q1 from the bottom, and counting customers per segment with a dictionary reaches the same rate.
        '''),
        code('''
        bottom_up = sum(r["amount"] for r in clean if r["quarter"] == "Q1")
        by_customer = {}
        for r in clean:
            if r["segment"] == "Retail-Plus":
                by_customer.setdefault((r["quarter"], r["customer_id"]), 0)
                by_customer[(r["quarter"], r["customer_id"])] += 1
        mean_q = {q: sum(v for (qq, _), v in by_customer.items() if qq == q) / sum(1 for (qq, _) in by_customer if qq == q) for q in ("Q1", "Q2")}
        kit.table(["number", "top down", "bottom up"],
                  [("Q1", kit.rupees(exported_q1 + corporate + consumer), kit.rupees(bottom_up)),
                   ("Retail-Plus orders per customer, Q1", round(per_customer(clean, "Q1", "Retail-Plus"), 2), round(mean_q["Q1"], 2)),
                   ("Retail-Plus orders per customer, Q2", round(per_customer(clean, "Q2", "Retail-Plus"), 2), round(mean_q["Q2"], 2))])
        kit.check("top down and bottom up agree on Q1", bottom_up == exported_q1 + corporate + consumer == BOOKS_Q1)
        kit.check("both routes agree on the Retail-Plus rate", abs(mean_q["Q1"] - per_customer(clean, "Q1", "Retail-Plus")) < 1e-9)
        '''),
        md('''
        **When to switch.** Bottom up is the check anyone can run; top down is the proof, since only the
        bridge says what each rupee of the gap was.

        > **Kavya's review.** "Two reconciliations, rows and rupees, and the bridge drawn. Then tell me what
        > changed in Tuesday's story, including when it got smaller."

        ### In the interview

        **[S] Finance and your dashboard disagree; what do you do?** "I assume both are correct arithmetic on
        different inputs and find the difference. I get Finance's figure to the rupee and its definition,
        profile my source, and build a bridge, one move per cause, each backed by the rows that carry it. I
        reconcile in rows and in rupees. When it closes I say which is right and why, fix the source and
        recompute anything reported from the wrong number."

        **[S] How do you handle outliers?** "I sort, look at the tail, and ask whether the record is wrong
        before asking whether it is big. A valid id, a real account and fields that convert make it
        revenue. I keep it, flag it, and show the result with and without it. For a model trained on the
        data I might cap or transform a long tail, and any fence I use sits inside one segment."

        **[D] Cleaning shrank yesterday's finding. What do you say?** "The smaller number first, what changed
        and why, and whether the decision still holds. Here the fall is 35 percent, not 49, and Thursday
        tests whether 35 is real."

        **Design. Prove the figure with a bridge, or rebuild it from a second source?** "A bridge, when a log
        backs each move, because it says why as well as how much. I would switch to a rebuild when the two
        sources are independent and complete, which this JSON feed is not."

        ### Depth: a bridge with more than one kind of move

        Today's bridge had one cause, copies, split by segment. A month-end bridge between a sales system and
        the ledger usually carries several kinds of move: timing (an order booked on the last day of one
        month and invoiced on the first of the next), definition (returns netted in one system and not the
        other), and error (copies, typos). Each kind gets its own column, and a bridge that closes only
        after an "other" column has not closed. Tesco's GBP 263 million was bridged by period for the same
        reason: a reader needs to see which kind of move each rupee is.
        '''),
        code('''
        kit.check_summary()
        print("Next: chapter 6 hands the logs to Anand's analyst and asks whether a stranger can replay them.")
        '''),
    ]


# ============================================================================= chapter 6
def ch6():
    return [
        opener(6, "The log the analyst audits", '''
        **The need.** Anand's analyst checks the reconciliation tonight, and an auditor may ask next quarter
        why any row was dropped. The metric is a pair of control totals, a count and a sum computed at each end and compared, rows and rupees, that tie from the
        export to the clean file to the books, and every row that left traceable to a rule. A log the analyst
        cannot follow costs a week of questions; a log that ties in rows and misses in rupees costs the team
        the analyst's trust in everything else it sends.

        **Who else faces it.** COMPANY_CH6
        ''', "Chapter 5 proved Q1 with the bridge and recomputed Tuesday. This chapter turns the pass into logs "
             "a stranger can audit and replay."),
        md('**Setup.** The whole pass as `clean_pass()`, so this notebook starts from the clean file and its logs.'),
        setup_cell([READ, PROFILE, RULE, PASS],
                   'import tempfile, pathlib\nraw = read_orders()\nclean, set_aside, rejects, flags = clean_pass(raw)\n'
                   'print(len(clean), "orders;", len(set_aside), "set aside;", len(rejects), "rejected;", len(flags), "flagged")'),
        mapcell(6, ["the options\\nwhat the analyst receives", "1. the decisions log\\nrupees per decision",
                    "2. the logs written\\nand read back", "3. the trap\\nrows tie, rupees do not",
                    "4. the auditor's 14", "a second route\\nreplay the log"]),
        md('''
        ## The options

        | Option | What the analyst receives | What the analyst can do with it |
        |---|---|---|
        | a) The clean file alone | 186 rows, read against the 201 raw | diff them by hand, with no reasons |
        | b) The clean file and a count | 186 rows and "15 set aside" | tie the rows, and nothing else |
        | c) Row logs, a decisions log and control totals | 15 set-aside rows with reasons, the flags, five decisions, rows and rupees | tie both totals and replay the pass |
        | d) A full diff of the two files | 201 lines marked kept or gone | see what went, and never why |
        '''),
        code('''
        per_line = 30    # seconds an analyst spends on one line of a log or a diff: an illustrative assumption
        sizing = [("a) clean file read against raw", 201 + 186, "no", "no", "no"),
                  ("b) file and a count", 1, "yes", "no", "no"),
                  ("c) logs and control totals", len(set_aside) + len(rejects) + len(flags) + 5 + 2, "yes", "yes", "yes"),
                  ("d) a full diff", 201, "yes", "by hand", "no")]
        kit.table(["option", "lines to read", "ties rows", "ties rupees", "can be replayed"],
                  [(n, l, a, b, c) for n, l, a, b, c in sizing], caption="Each hand-over sized for the analyst")
        kit.bars([(n, l * per_line / 60) for n, l, *_ in sizing], fmt=lambda v: f"{v:.0f} min",
                 lit=(2,), title="Minutes of reading, at an illustrative 30 seconds a line")
        '''),
        md('''
        **The best-fit call: c.** Twenty-three lines, both totals tied, and a pass the analyst can re-run.
        Option b is the fastest read and proves the least; a and d cost over an hour and still say nothing
        about why. **The fact that would change it:** an analyst who must re-derive every row independently,
        as an external auditor sometimes must; then d goes alongside c, never in place of it.
        '''),

        md('''
        ## 1. The decisions log: one line per rule, with what it moved

        **Predict before you run.** Which decision moves the most rupees in Q1? a) the identity rule;
        b) the missing status; c) the bulk order; d) the missing discount.
        '''),
        code('''
        q1_aside = sum(convert(e["amount"])[0] or 0 for e in set_aside if e["quarter"] == "Q1")
        decisions = [
            {"decision": "one row per order_id, the copy that validates stays", "rows": len(set_aside), "q1_rupees": -q1_aside},
            {"decision": "an amount that does not convert is rejected, never zeroed", "rows": len(rejects), "q1_rupees": 0},
            {"decision": "a missing status is kept and flagged", "rows": len(flags), "q1_rupees": 0},
            {"decision": "a missing discount stays unknown, never zero", "rows": sum(1 for r in clean if r["discount"] == ""), "q1_rupees": 0},
            {"decision": "the largest Q2 order is kept and flagged", "rows": 1, "q1_rupees": 0},
        ]
        kit.table(["decision", "rows it touched", "Q1 rupees it moved"],
                  [(d["decision"], d["rows"], kit.rupees(d["q1_rupees"])) for d in decisions], caption="The decisions log")
        kit.bars([(f"decision {i + 1}", abs(d["q1_rupees"])) for i, d in enumerate(decisions)], fmt=kit.rupees, lit=(0,),
                 title="Q1 rupees each decision moved")
        kit.check("the decisions' rupees add to the whole gap", Q(raw, "Q1") + sum(d["q1_rupees"] for d in decisions) == BOOKS_Q1)
        '''),
        md('''
        **What happened.** The answer is a. The identity rule moves all Rs 19,98,210; the other four decisions
        move no Q1 rupees and each still gets a line, because an analyst who finds an unlogged decision
        stops trusting the logged ones.
        '''),

        md('''
        ## 2. The logs written, and read back

        A log that lives only in the notebook reaches nobody. `csv.DictWriter` writes the row logs and
        `json.dump` the decisions; reading them back proves the files hold what the notebook holds.

        **Predict before you run.** Read back from the CSV, what type is each amount in the log? a) `int`,
        since it was written from numbers; b) `str`, since a CSV holds only text; c) `None` for the
        unreadable one and `int` for the rest; d) it depends on the row.
        '''),
        code('''
        out = pathlib.Path(tempfile.mkdtemp())
        with open(out / "set_aside_log.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(set_aside[0]))
            w.writeheader()
            w.writerows(set_aside)
        with open(out / "decisions_log.json", "w", encoding="utf-8") as f:
            json.dump(decisions, f, indent=1)
        with open(out / "set_aside_log.csv", newline="", encoding="utf-8") as f:
            back = list(csv.DictReader(f))       # read_orders() would overwrite the log's own line column
        back_decisions = json.load(open(out / "decisions_log.json", encoding="utf-8"))
        kit.flow(["the pass\\nclean_pass()", "the logs\\nwritten to disk", "read back\\nDictReader, json.load",
                  "compared\\nrow for row"], lit=3, title="A log is proved by reading it back")
        kit.check("the set-aside log reads back 15 rows", len(back) == len(set_aside) == 15)
        kit.check("the decisions log reads back five decisions", len(back_decisions) == 5)
        kit.check("the rupees in the file equal the rupees in the notebook",
                  sum(convert(r["amount"])[0] or 0 for r in back if r["quarter"] == "Q1") == q1_aside)
        '''),
        md('''
        **What happened.** The answer is b. The log went out as text and comes back as text, which is why
        the rupee check converts it again; chapter 1's rule holds for your own files too.

        **Your turn.** In the empty cell, print the set-aside log as the analyst will read it, with
        `print(open(out / "set_aside_log.csv").read())`. Pick one row and follow its `kept_line` to the
        row that stayed.
        '''),
        empty(),

        md('''
        ## 3. The trap: rows tie, rupees do not

        **The plausible wrong answer.** A colleague built the pass in the order that feels natural: remove
        repeated ids first, keeping the first copy, then convert and reject what fails. The log looks
        perfect.
        '''),
        code('''
        seen, first_copy, col_aside = set(), [], []
        for r in raw:
            if r["order_id"] in seen:
                col_aside.append(r)
                continue
            seen.add(r["order_id"])
            first_copy.append(r)
        col_clean = [dict(r, amount=convert(r["amount"])[0]) for r in first_copy if convert(r["amount"])[0] is not None]
        col_rejects = [r for r in first_copy if convert(r["amount"])[0] is None]
        col_aside_q1 = sum(convert(r["amount"])[0] or 0 for r in col_aside if r["quarter"] == "Q1")
        kit.stats([(f"{len(raw)} = {len(col_clean)} + {len(col_aside) + len(col_rejects)}", "rows reconcile", "in equals kept plus logged"),
                   (kit.rupees(col_aside_q1), "Q1 set aside", "Anand's gap, to the lakh"),
                   (kit.rupees(Q(col_clean, "Q1")), "Q1 clean", "1.90 crore when rounded")],
                  caption="The colleague's log, as it would be sent")
        '''),
        md('''
        **Why it is wrong.** Rs 20,00,000 set aside looks like Anand's gap, and the rows tie, and Q1 rounds to
        1.9. To the rupee, Q1 is Rs 1,89,98,210, Rs 1,790 short of the books: keeping the first copy kept one
        whose amount could not be read, rejected it, and set aside the twin that carried the value. A row
        reconciliation proves no row vanished; it cannot prove the right rows stayed. The analyst ties to
        the rupee, finds a booked order missing from a file called reconciled, and questions every other
        line. Two checks catch it: the books against the clean Q1, and a rejected order whose twin sits in
        the set-aside log.
        '''),
        code('''
        rejected_ids = {r["order_id"] for r in col_rejects}
        orphaned = [r for r in col_aside if r["order_id"] in rejected_ids and convert(r["amount"])[0] is not None]
        kit.check("the colleague's rows reconcile", len(raw) == len(col_clean) + len(col_aside) + len(col_rejects))
        kit.check("the colleague's Q1 misses the books by Rs 1,790", BOOKS_Q1 - Q(col_clean, "Q1") == 1790)
        kit.check("a rejected order has a twin with a value in the set-aside log", len(orphaned) == 1)
        kit.bridge(("Q1 as exported", Q(raw, "Q1")), [("the colleague's set-aside rows", -col_aside_q1)],
                   end_label="the colleague's Q1", lo=18800000,
                   title="The colleague's bridge closes on its own file and misses the books; axis from Rs 1.88 crore")
        '''),
        md('''
        **The fix, and what changed.** Convert inside the identity rule, preferring the copy that validates,
        as `clean_pass()` does. The Rs 1,790 order comes back, the rejects log empties because the unreadable
        copy is set aside with its twin named, and both totals tie: rows 201 = 186 + 15, rupees to the books.
        '''),

        md('''
        ## 4. The harder variant: the auditor's 14

        The auditor writes: "Your log says 14 Q1 rows were dropped. Why those 14, and how do I know nothing
        else went with them?"

        **Predict before you run.** Which evidence answers "nothing else went"? a) the count 14; b) every one
        of the 14 has a kept twin, and Q1 rows and rupees both tie; c) the log is sorted; d) the file is smaller.
        '''),
        code('''
        kept_ids = {r["order_id"] for r in clean}
        q1_rows = [e for e in set_aside if e["quarter"] == "Q1"]
        twins = sum(1 for e in q1_rows if e["order_id"] in kept_ids)
        q1_in = sum(1 for r in raw if r["quarter"] == "Q1")
        q1_kept = sum(1 for r in clean if r["quarter"] == "Q1")
        kit.columns(["Q1 rows in", "Q1 orders kept", "Q1 rows set aside"], [("rows", [q1_in, q1_kept, len(q1_rows)])],
                    title="The auditor's first question in three bars")
        kit.check("14 Q1 rows set aside", len(q1_rows) == 14)
        kit.check("every one has a kept twin", twins == 14)
        kit.check("Q1 rows tie: in equals kept plus set aside", q1_in == q1_kept + len(q1_rows))
        '''),
        md('''
        **What happened.** The answer is b. "Set aside with a reason", never "dropped": 14 Q1 rows share an
        id with a kept row, each has its twin named on its line, and Q1 ties in rows (114 = 100 + 14) and in
        rupees (the bridge). The second case this afternoon walks the auditor through it in pairs.
        '''),

        md('''
        ## A second route: replay the log

        The strongest test of a log is that a stranger can rebuild the clean file from the raw export and the
        log alone, without the notebook's code.
        '''),
        code('''
        gone = {int(r["line"]) for r in back} | {r["line"] for r in rejects}
        replayed = [dict(r, amount=int(r["amount"])) for r in raw if r["line"] not in gone]
        same = sorted((r["order_id"], r["amount"]) for r in replayed) == sorted((r["order_id"], r["amount"]) for r in clean)
        kit.table(["route", "orders", "Q1", "Q2"],
                  [("clean_pass()", len(clean), kit.rupees(Q(clean, "Q1")), kit.rupees(Q(clean, "Q2"))),
                   ("raw export less the logged lines", len(replayed), kit.rupees(Q(replayed, "Q1")), kit.rupees(Q(replayed, "Q2")))])
        kit.check("replaying the log reproduces the clean file exactly", same)
        '''),
        md('''
        **When to switch.** The control totals are the quick test the analyst runs first; the replay is the
        test for an auditor who trusts nothing, and it is the one to run before any log leaves the team.

        > **Kavya's review.** "A log is finished when a stranger can replay it. Rows and rupees both tie, a
        > reason on every line, and the twin named for every copy."

        ### In the interview

        **[D] An auditor asks why you dropped 14 rows; walk them through it.** "They were set aside, not
        dropped, and each is in the log. Fourteen Q1 rows share an order id with another row; the identity
        rule is the order id, because the ERP issues one per order. For each pair I kept the copy whose
        fields validate, and the log names the kept line. Two corporate copies carry Rs 19,67,560 and the
        rest Rs 30,650. Q1 rows tie, 114 in and 100 kept, the rupees bridge to your books exactly, and
        replaying the log on the raw export rebuilds my clean file."

        **[F] The row counts reconcile. Are you done?** "No. Rows prove nothing vanished; rupees prove the
        right rows stayed. A colleague's pass here tied in rows and was Rs 1,790 short."

        **Design. What goes in a log so a stranger can replay it?** "The source line, the key, the rule, the
        reason, the value, and the line of the row that stayed; plus a decisions log with each rule's rows
        and rupees, and the control totals. I would add a full diff only for an external auditor who has to
        re-derive every row."

        ### Depth: control totals, and why a log is versioned

        A control total is a count or a sum computed at both ends of a transfer and compared: rows sent
        against rows received, rupees exported against rupees loaded. Finance teams keep them per batch, so
        a load that drops or doubles rows is caught before anyone reads a report. A log is also only
        replayable against the export it was written for, so it carries the export's name, row count and
        date, and a new export gets a new log. Week 2 keeps these totals in the warehouse.
        '''),
        code('''
        kit.flow(["decide\\nfive decisions", "log\\nrows and rules", "reconcile\\nrows and rupees",
                  "replay\\nthe stranger's test"], lit=3, title="Chapter 6, from a clean file to one a stranger can audit")
        kit.check_summary()
        print("Next: the escalated case runs the whole pass alone; Thursday asks whether the smaller Retail-Plus fall is real.")
        '''),
    ]


# ============================================================================= the escalated case
LADDER_PM = '''kit.ladder(["chapters 1 to 6, the pass built", "the escalated case: the full pass alone",
            "the second case: the auditor asks why"], lit={lit}, show=False)'''

CASE_STEPS = [
    ("Step 1. Read and profile", '''
# TODO 1. Which call reads the export so every value can be profiled as the file holds it?
#   a) [dict(r) for r in csv.reader(open(ORDERS_CSV))]
#   b) read_orders()
#   c) json.load(open(ORDERS_CSV))
#   d) open(ORDERS_CSV).read().split(",")
raw = __TODO1__
ids = {r["order_id"] for r in raw}
''', '''
kit.check("201 rows read", len(raw) == 201, f"{len(raw)}")
kit.check("186 distinct order ids", len(ids) == 186, f"{len(ids)}")
kit.bars([("rows", len(raw)), ("distinct order ids", len(ids))], title="Rows against orders in the export")
'''),
    ("Step 2. Convert with a rejects log", '''
# TODO 2. What should happen to an amount that int() refuses?
#   a) it becomes 0, so the total runs
#   b) the row is deleted before anyone sees it
#   c) it goes to the rejects log with its line and reason
#   d) it becomes the median amount of its segment
failed = [r for r in raw if convert(r["amount"])[0] is None]
rejects_log = __TODO2__
''', '''
kit.check("one amount is logged, not zeroed", len(rejects_log) == 1 and all("line" in x for x in rejects_log))
'''),
    ("Step 3. The identity rule", '''
# TODO 3. Which key says two rows are the same order?
#   a) the whole record, file line included
#   b) customer_id and amount together
#   c) the whole record, file line excluded
#   d) order_id alone
KEY = __TODO3__

# TODO 4. Inside a group of rows sharing that key, which copy stays?
#   a) the first copy in the file
#   b) the copy whose amount converts
#   c) the copy with the larger amount
#   d) the last copy in the file
PREFER = __TODO4__
clean, set_aside = apply_rule(raw, KEY, PREFER)
''', '''
kit.check("186 orders kept", len(clean) == 186, f"{len(clean)}")
kit.check("15 rows set aside", len(set_aside) == 15, f"{len(set_aside)}")
kit.check("Q1 is Rs 1,90,00,000", Q(clean, "Q1") == 19000000, kit.rupees(Q(clean, "Q1")))
'''),
    ("Step 4. The two open decisions", '''
# TODO 5. One order has no status. Which decision keeps revenue and the delivered count honest?
#   a) keep and flag
#   b) drop the order
#   c) default it to delivered
#   d) default it to cancelled
STATUS_DECISION = __TODO5__

# TODO 6. The largest Q2 order is 1.66 times the next. What happens to it?
#   a) remove it as an outlier
#   b) cap it at the next largest order
#   c) keep it and flag it, shown with and without
#   d) move it to Q1
BULK_DECISION = __TODO6__
decisions = [("status missing on one Q2 order", STATUS_DECISION), ("largest Q2 order", BULK_DECISION)]
''', '''
kit.check("Q2 stays at Rs 1,87,00,000", Q(clean, "Q2") == 18700000 and "keep" in STATUS_DECISION and "keep" in BULK_DECISION)
kit.columns(["Q1", "Q2"], [("clean, Rs lakh", [Q(clean, "Q1") / 1e5, Q(clean, "Q2") / 1e5])],
            fmt=lambda v: f"{v:,.0f}", title="Clean revenue by quarter")
'''),
    ("Step 5. Reconcile twice and draw the bridge", '''
# TODO 7. Which pair of checks proves the reconciliation to Anand's analyst?
#   a) rows in equal rows kept, and Q1 rounds to 1.9 crore
#   b) rows in equal kept plus set aside, and exported Q1 less set-aside rupees equals the books
#   c) rows kept equal distinct ids, and Q2 is unchanged
#   d) the rejects log is empty, and Q1 is below the dashboard
exported_q1 = Q(raw, "Q1")
removed_q1 = sum(convert(r["amount"])[0] or 0 for r in set_aside if r["quarter"] == "Q1")
proof = __TODO7__
''', '''
kit.check("rows reconcile", len(raw) == len(clean) + len(set_aside))
kit.check("rupees reconcile to the books", exported_q1 - removed_q1 == 19000000)
kit.bridge(("Q1 as exported", exported_q1), [("rows set aside", -removed_q1)], end_label="Q1 clean, the books",
           lo=18800000, title="Q1 from the export to the books; the axis starts at Rs 1.88 crore")
'''),
    ("Step 6. Tuesday recomputed, and the note", '''
# TODO 8. Retail-Plus orders per customer fell 49.0 percent as Tuesday reported. On clean data?
#   a) it vanishes
#   b) it grows past 49 percent
#   c) it moves to Retail-Core
#   d) it falls 35.0 percent, smaller
TUESDAY_VERDICT = __TODO8__
rp = [per_customer(clean, q, "Retail-Plus") for q in ("Q1", "Q2")]
''', '''
kit.check("Retail-Plus falls about 35 percent on clean data", round(100 * (rp[1] - rp[0]) / rp[0], 1) == -35.0)
kit.line(["Q1", "Q2"], [("Retail-Plus orders per customer, clean", [round(x, 2) for x in rp], "good"),
                        ("as Tuesday reported", [2.32, 1.18], "bad")], fmt=lambda v: f"{v:.2f}",
         title="Retail-Plus frequency: the finding stands, smaller")
kit.check_summary()
'''),
]

CASE_ANSWERS = {1: "read_orders()", 2: '[{"line": r["line"], "order_id": r["order_id"], "reason": "amount does not convert"} for r in failed]',
                3: '"order_id"', 4: '"validates"', 5: '"keep and flag"', 6: '"keep and flag, shown with and without"',
                7: '(len(raw) == len(clean) + len(set_aside), exported_q1 - removed_q1 == 19000000)',
                8: '"falls 35.0 percent, smaller"'}
CASE_WHY = {
    1: "b. read_orders() keeps every value as the file's text and records the line. a loses the header names, c is the wrong parser for a CSV, and d splits the whole file on commas without rows.",
    2: "c. a failure is kept where anyone can read it. a invents an order worth nothing, b deletes evidence, and d invents an amount.",
    3: "d. the ERP issues one order_id per order. a finds nothing because the line makes every row unique, b removes a real Rs 17,71,000 order and misses a pair, and c misses the two pairs whose copies differ.",
    4: "b. the copy that validates carries the value. a keeps an unreadable amount and loses Rs 1,790, c picks by size, which is no rule, and d lands on the books here only because of file order.",
    5: "a. revenue is booked value and the fate is unknown. b removes a booked order, c and d invent a status.",
    6: "c. it is a real Business order. a turns a 1.6 percent dip into 17.1, b invents a smaller order, and d moves revenue between quarters.",
    7: "b. rows and rupees both reconcile. a is the count-only pass that lost Rs 1,790, c proves nothing about rupees, and d is false, since the rule sets the unreadable copy aside.",
    8: "d. 1.82 to 1.18 is a fall of 35.0 percent. a and b misread the recompute, and c confuses segments.",
}

CASE_HELPERS = READ + '''
def apply_rule(rows, key, prefer):
    """One row per key; prefer is "validates" or "first". Returns (kept, set aside)."""
    kept, aside = {}, []
    for r in rows:
        k = r[key] if isinstance(key, str) and key in r else tuple(sorted(r.items()))
        if k not in kept:
            kept[k] = r
        elif prefer == "validates" and convert(kept[k]["amount"])[0] is None and convert(r["amount"])[0] is not None:
            aside.append(kept[k]); kept[k] = r
        else:
            aside.append(r)
    good = [dict(r, amount=convert(r["amount"])[0]) for r in kept.values() if convert(r["amount"])[0] is not None]
    aside += [r for r in kept.values() if convert(r["amount"])[0] is None]
    return good, aside

def per_customer(rows, q, seg):
    rs = [r for r in rows if r["quarter"] == q and r["segment"] == seg]
    return len(rs) / len({r["customer_id"] for r in rs})
'''


def case_cells(solution):
    cells = [
        md('''
        # The escalated case: the full pass, alone

        **Week 1, Wednesday afternoon, the escalated case.** Anand has replied: "Send the reconciliation
        and the log before the day closes. My analyst checks it tonight." Run the whole pass the six
        chapters built: read and profile, convert with a rejects log, apply the identity rule, make the
        two open decisions, reconcile in rows and in rupees, draw the bridge, and recompute Tuesday.

        Each step has lettered choices above a placeholder such as `__TODO1__`. Replace the placeholder
        with the code of the option you choose, run the step, and read its checks. Run as shipped, the
        notebook stops at the first placeholder with a `NameError`; that is expected. Post your eight
        letters in order when every check passes, then write the note to Finance in under 120 words.
        ''' if not solution else '''
        # The escalated case: the full pass, solution

        **Week 1, Wednesday afternoon, the escalated case, solution twin.** Every placeholder is filled
        with its keyed option and the notebook runs clean. Under each step, one line says why the other
        three letters fail.

        The letters, in order: 1b 2c 3d 4b 5a 6c 7b 8d.
        '''),
        code(CASE_HELPERS + '\nprint("helper and case functions loaded")'),
        code("kit.side_by_side(\n    " + LADDER_PM.format(lit=1) + ''',
    kit.vflow(["read and profile", "convert with a log", "the identity rule", "two decisions",
               "reconcile twice", "Tuesday and the note"], lit=0, show=False),
)'''),
    ]
    for title, body, check in CASE_STEPS:
        cells.append(md(f"## {title}"))
        src = body.strip("\n")
        if solution:
            for k, v in CASE_ANSWERS.items():
                src = src.replace(f"__TODO{k}__", v)
        cells.append(code(src + f'\nprint("{title.split(".")[0]}: done")'))
        if solution:
            nums = [int(x) for x in re.findall(r"TODO (\d+)\.", body)]
            cells.append(md("**Why the other letters fail.** " + " ".join(CASE_WHY[k] for k in nums)))
        cells.append(code(check.strip("\n")))
    cells.append(md('''
    **Post** your eight letters in order, then the note to Finance: numbers first, which figure is right
    and why, the two reconciliations, the two flagged decisions, and whether Tuesday's finding survives.
    '''))
    return cells


# ============================================================================= the second case
AUDIT_HELPERS = CASE_HELPERS + '''
raw = read_orders()
clean, set_aside = apply_rule(raw, "order_id", "validates")
by_id = {}
for r in raw:
    by_id.setdefault(r["order_id"], []).append(r)
q1_aside = [r for r in set_aside if r["quarter"] == "Q1"]
print(len(clean), "orders kept;", len(q1_aside), "Q1 rows set aside")
'''

AUDIT_STEPS = [
    ("Question 1. How many Q1 rows were set aside, and is that the auditor's 14?", '''
# TODO 1. Which count answers the auditor's first question?
#   a) rows in the file less orders kept, both quarters
#   b) Q1 rows in less Q1 orders kept
#   c) distinct order ids in Q1
#   d) rows in the rejects log
q1_in = sum(1 for r in raw if r["quarter"] == "Q1")
q1_kept = sum(1 for r in clean if r["quarter"] == "Q1")
answer_1 = __TODO1__
''', '''
kit.check("the auditor's 14 is Q1 rows in less Q1 orders kept", answer_1 == 14, f"{answer_1}")
kit.columns(["Q1"], [("rows in", [q1_in]), ("orders kept", [q1_kept])], title="Q1 rows in against orders kept")
'''),
    ("Question 2. Is every one of the 14 a second copy of a kept order?", '''
# TODO 2. Which test shows each set-aside row has a twin that stayed?
#   a) its order_id appears among the kept orders
#   b) its amount appears among the kept orders
#   c) its customer_id appears among the kept orders
#   d) its line number is above 186
kept_ids = {r["order_id"] for r in clean}
has_twin = [__TODO2__ for r in q1_aside]
''', '''
kit.check("all 14 have a kept twin", all(has_twin) and len(has_twin) == 14)
'''),
    ("Question 3. Which rows carry the rupees?", '''
# TODO 3. How should the rupees be shown to the auditor?
#   a) one total for all 14 rows
#   b) split by the segment of each row, rows and rupees side by side
#   c) only the largest row, since it dominates
#   d) as a share of Q2 revenue
segs = ["Business", "Retail-Plus", "Retail-Core"]
rows_by = [sum(1 for r in q1_aside if r["segment"] == s) for s in segs]
rupees_by = [sum(convert(r["amount"])[0] or 0 for r in q1_aside if r["segment"] == s) for s in segs]
shown = __TODO3__
''', '''
kit.check("the rupees add to Rs 19,98,210", sum(rupees_by) == 1998210, kit.rupees(sum(rupees_by)))
kit.bars(list(zip(segs, rupees_by)), fmt=kit.rupees, title="Rupees in the 14 Q1 rows, by segment")
kit.bars(list(zip(segs, rows_by)), title="Rows among the 14, by segment")
'''),
    ("Question 4. Why was one copy chosen over its twin?", '''
# TODO 4. For a pair whose copies differ, what does the log have to say?
#   a) nothing, since the pair shares an id
#   b) which copy stayed, which field differed, and why that copy
#   c) the average of the two copies
#   d) that the pair was deleted
pairs_differing = [k for k, rs in by_id.items() if len(rs) > 1
                   and len({tuple((f, v) for f, v in r.items() if f != "line") for r in rs}) > 1]
log_rule = __TODO4__
''', '''
kit.check("two pairs differ between their copies", len(pairs_differing) == 2)
kit.check("the log states the copy, the field and the reason", "field" in log_rule and "why" in log_rule)
'''),
    ("Question 5. What does the auditor sign?", '''
# TODO 5. Which statement is the one the evidence supports?
#   a) 14 Q1 rows were deleted as errors
#   b) the dashboard was right and the books are short
#   c) 14 Q1 rows are copies of kept orders, set aside by the order_id rule; rows and rupees reconcile
#   d) the 14 rows were outliers
statement = __TODO5__
''', '''
kit.check("rows reconcile in Q1", q1_in == q1_kept + len(q1_aside))
kit.check("rupees reconcile in Q1", Q(raw, "Q1") - sum(rupees_by) == 19000000)
kit.flow(["the question\\nwhy 14 rows", "the rule\\norder_id", "the twins\\nall 14 have one",
          "the rupees\\nby segment", "the signature\\nboth reconcile"], lit=4, title="The auditor's walk through the log")
kit.check_summary()
'''),
]
AUDIT_ANSWERS = {1: "q1_in - q1_kept", 2: 'r["order_id"] in kept_ids', 3: "list(zip(segs, rows_by, rupees_by))",
                 4: '{"copy": "kept", "field": "which one differed", "why": "the copy that validates"}',
                 5: '"14 Q1 rows are copies of kept orders, set aside by the order_id rule; rows and rupees reconcile"'}
AUDIT_WHY = {
    1: "b. the auditor asked about Q1. a counts both quarters and gives 15, c counts orders, not rows, and d counts the one unreadable amount.",
    2: "a. a twin is the same order_id. b and c match different orders that happen to share a value or a buyer, and d is where a row sits, not what it is.",
    3: "b. the auditor needs rows and rupees by kind, since two rows carry 98 percent of the money. a hides that, c hides the other rows, and d answers a different quarter.",
    4: "b. a pair that differs needs the kept copy, the field and the reason. a leaves the auditor guessing, c invents a value, and d is false.",
    5: "c. it states the rule and both reconciliations. a calls copies errors and says deleted, b reverses the finding, and d confuses copies with outliers.",
}


def audit_cells(solution):
    cells = [
        md('''
        # The second case: the auditor's question

        **Week 1, Wednesday afternoon, the second case, in pairs.** Anand's auditor writes: "Your log says
        14 Q1 rows were dropped. Why those 14, and how do I know nothing else went with them?" Answer
        from the log and the file, one question at a time. One of the pair drives; the other plays the
        auditor and asks the next question only when the check passes.

        Each question has lettered choices above a placeholder such as `__TODO1__`. Replace it with the
        code of the option you choose. Run as shipped, the notebook stops at the first placeholder with a
        `NameError`, which is expected. Post your five letters when every check passes.
        ''' if not solution else '''
        # The second case: the auditor's question, solution

        **Week 1, Wednesday afternoon, the second case, solution twin.** Every placeholder filled, run
        clean. The letters, in order: 1b 2a 3b 4b 5c.
        '''),
        code(AUDIT_HELPERS),
        code("kit.side_by_side(\n    " + LADDER_PM.format(lit=2) + ''',
    kit.vflow(["which 14", "a twin for each", "the rupees", "the log's reasons", "the signature"], lit=0, show=False),
)'''),
    ]
    for title, body, check in AUDIT_STEPS:
        cells.append(md(f"## {title}"))
        src = body.strip("\n")
        if solution:
            for k, v in AUDIT_ANSWERS.items():
                src = src.replace(f"__TODO{k}__", v)
        cells.append(code(src + f'\nprint("{title.split(".")[0]}: done")'))
        if solution:
            nums = [int(x) for x in re.findall(r"TODO (\d+)\.", body)]
            cells.append(md("**Why the other letters fail.** " + " ".join(AUDIT_WHY[k] for k in nums)))
        cells.append(code(check.strip("\n")))
    return cells


# ============================================================================= companies and build
COMPANY = {
    "COMPANY_CH2": ("On 22 and 23 May 2009 a processing fault at Starbucks billed some card customers twice across "
                    "about 7,800 company-owned stores in the US and Canada, and the company repaid about one million "
                    "customers (NBC News and AP, 10 June 2009, checked 30 Sep 2026). The same purchase recorded twice "
                    "looks like two purchases until someone asks what makes two records one."),
    "COMPANY_CH3": ("India's GST system writes the identity rule into law for every business invoice. The Invoice "
                    "Registration Portal rejects an invoice already reported under the same supplier GSTIN (its GST "
                    "registration number), invoice "
                    "number, document type and financial year, the fields it also hashes into the invoice's reference "
                    "number (GSTN e-invoice FAQ, version 1.4, checked 30 Sep 2026). Since 1 August 2023 that applies "
                    "to every business above Rs 5 crore of turnover (Notification 10/2023-Central Tax, checked "
                    "30 Sep 2026), which includes a seller like Kalpa's Business segment."),
    "COMPANY_CH4": ("On the evening of Friday 12 December 2014 a repricing tool used by Amazon UK sellers set "
                    "hundreds of items to 1p for about an hour; Amazon said most orders were cancelled once the error "
                    "was spotted (BBC News, 15 December 2014, checked 30 Sep 2026). A value that fell to a default "
                    "sold real stock, which is what a coerced zero does to a report."),
    "COMPANY_CH5": ("In September 2014 Tesco said it had overstated its half-year profit guidance by about "
                    "GBP 250 million, mainly by recognising supplier income early. Its own investigation then "
                    "bridged the figure to GBP 263 million, split by period: GBP 118 million in the first half, "
                    "about GBP 70 million in 2013/14 and about GBP 75 million before (BBC News, 22 September 2014; "
                    "Tesco interim results, 23 October 2014; both checked 30 Sep 2026). The question was Anand's: "
                    "which figure is right, and what is the gap made of."),
    "COMPANY_CH6": ("At Patisserie Valerie, a UK cafe chain, the administrators put the accounting hole at "
                    "GBP 94 million in March 2019 (BBC News, 15 March 2019), and in September 2021 the Financial "
                    "Reporting Council fined its former auditor GBP 4 million, reduced to GBP 2.34 million, for "
                    "missing red flags in three years of audits (FRC, 27 September 2021; both checked 30 Sep 2026). "
                    "An auditor who cannot trace a number to its rows is the one who pays for it."),
}


def fill(cells):
    for c in cells:
        if c.cell_type == "markdown":
            for k, v in COMPANY.items():
                c.source = c.source.replace(k, v)
    return cells


BUILDS = {
    "c1": lambda: build(NB / "C2_W01_D03_01_profile_STUDENT.ipynb", fill(ch1())),
    "c2": lambda: build(NB / "C2_W01_D03_02_duplicates_STUDENT.ipynb", fill(ch2())),
    "c3": lambda: build(NB / "C2_W01_D03_03_identity_rule_STUDENT.ipynb", fill(ch3())),
    "c4": lambda: build(NB / "C2_W01_D03_04_missing_malformed_STUDENT.ipynb", fill(ch4())),
    "c5": lambda: build(NB / "C2_W01_D03_05_bridge_STUDENT.ipynb", fill(ch5())),
    "c6": lambda: build(NB / "C2_W01_D03_06_audit_logs_STUDENT.ipynb", fill(ch6())),
    "case": lambda: (build(NB / "C2_W01_D03_ex1_escalated_case_STUDENT.ipynb", case_cells(False), execute=False),
                     build(SOL / "C2_W01_D03_ex1_escalated_case_solution_STUDENT.ipynb", case_cells(True))),
    "audit": lambda: (build(NB / "C2_W01_D03_ex2_auditor_STUDENT.ipynb", audit_cells(False), execute=False),
                      build(SOL / "C2_W01_D03_ex2_auditor_solution_STUDENT.ipynb", audit_cells(True))),
}

if __name__ == "__main__":
    for name in (sys.argv[1:] or list(BUILDS)):
        BUILDS[name]()
        print("built", name)
