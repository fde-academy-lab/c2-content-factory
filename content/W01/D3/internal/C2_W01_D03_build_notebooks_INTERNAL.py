"""Build Wednesday's notebooks: three rounds, the escalated case and the second case.

Run from the repository root:
    python3 content/W01/D3/internal/C2_W01_D03_build_notebooks_INTERNAL.py            every notebook
    python3 content/W01/D3/internal/C2_W01_D03_build_notebooks_INTERNAL.py r1 case     named ones only

Each teaching notebook is executed cold in its own folder by scripts/nb_make.py, so the saved outputs
are the ones a learner sees on GitHub. The TODO twins are written unexecuted and their solution
twins executed. No cell prints a planted record: every discovery of one sits in an empty your-turn
cell, and a mechanism that needs a plant to show runs on invented records labelled invented.
"""
import pathlib
import sys

sys.path.insert(0, "scripts")
from nb_make import SETUP, build, code, empty, md  # noqa: E402

DAY = pathlib.Path("content/W01/D3")
NB = DAY / "notebooks"
SOL = DAY / "exercises" / "solutions"

LOAD = SETUP + '''
import csv, json

DATA = kit.data_dir()
ORDERS_CSV = DATA / "C2_W01_D03_orders_STUDENT.csv"

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
'''

LADDER = '''kit.ladder(["round 1, the profile: what did the ERP send?", "round 2, the copies: where do the extra rupees come from?",
            "round 3, the proof: which figure is right?", "the escalated case: the full pass alone",
            "the second case: the auditor asks why"], lit={lit}, show=False)'''


# --------------------------------------------------------------------------- round 1
def round1():
    return [
        md('''
        # What did the ERP actually send?

        **Week 1, Wednesday. Round 1 of 3: the profile.** By the end of this notebook you can read a CSV
        and a JSON feed, profile every field for presence, convertibility and distinct values, and
        convert amounts on purpose, with every failure counted and logged rather than hidden.

        > **The client asks.** "Your dashboard says Q1 was Rs 2.1 crore. Our books say 1.9. Until your
        > numbers match ours, Finance will not act on a drop measured from an ERP export. Send me a
        > reconciliation."
        >
        > Anand Iyer, finance controller, Kalpa Retail

        > **Kavya's review.** "Before you total anything, tell me how many records you received, how
        > many are complete, how many convert and how many are distinct. A total from a file you have
        > not profiled is a guess with a comma in it."

        Tuesday found that Retail-Plus orders per customer fell from 2.32 to 1.18, down 49 percent, and
        that finding reached the leadership group. It was measured on the export exactly as the ERP
        delivered it, with nothing checked, and this round starts where every reconciliation starts:
        with what arrived.
        '''),
        md('''
        **Setup.** The cell below finds the shared helper, `kit`, and defines the two functions the whole
        day uses: `read_orders()`, which reads an export into dictionaries and remembers the file line
        each row came from, and `convert()`, which turns an amount into rupees or says why it could not.
        Nothing here prints a record.
        '''),
        code(LOAD + '\nprint("helper loaded; data folder:", DATA.name)'),
        code("kit.side_by_side(\n    " + LADDER.format(lit=0) + ''',
    kit.vflow(["1. everything read is text\\nopen, read, count",
               "2. the profile\\npresent, convertible, distinct",
               "3. the trap\\na conversion that hides its failures",
               "4. the harder variant\\nthe JSON feed and the vendor copy"], lit=1, show=False),
)'''),

        md('''
        ## 1. Everything read from a file is text

        The ERP sent an orders CSV. Before any total, open it and count what arrived, and look at what
        Python holds for one amount. Opening the wrong name is the first thing that goes wrong on a
        Wednesday, and it costs two minutes: read the last line, check the folder, move on.

        **Predict before you run.** After `csv.DictReader` reads the file, what is the type of an
        amount such as the first order's? a) `int`, since the column holds numbers; b) `float`, since
        rupees can carry paise; c) `str`, since a CSV holds only text; d) it depends on the row.
        '''),
        code('''
        with kit.expect_error() as err:
            open("orders.csv")            # the name a hurried analyst types from memory

        raw = read_orders()
        first = raw[0]
        print(len(raw), "rows read")
        print({k: first[k] for k in ("order_id", "segment", "quarter", "amount")})
        print("the amount is held as", type(first["amount"]).__name__, repr(first["amount"]))
        '''),
        md('''
        **What happened.** The answer is c. The first call stops with `FileNotFoundError`, and its last
        line names the file Python looked for in the notebook's own folder; the exports live in
        `../data/`, which `read_orders()` already knows. The file then reads as 201 rows, and the first
        amount is the text `'2200'`, not the number 2200. Every value a CSV gives back is text until
        you convert it on purpose, so every sum, comparison and sort on an amount depends on a
        conversion somebody chose.
        '''),
        code('''
        segments = ["Retail-Core", "Retail-Plus", "Business", "Student"]
        rows_by = {q: [sum(1 for r in raw if r["quarter"] == q and r["segment"] == s) for s in segments]
                   for q in ("Q1", "Q2")}
        kit.columns(segments, [("Q1 rows", rows_by["Q1"]), ("Q2 rows", rows_by["Q2"])],
                    title="Rows in the export by segment and quarter, before anything is checked")
        kit.check("the export holds 201 rows", len(raw) == 201, f"{len(raw)}")
        kit.check("every value arrives as text", all(isinstance(v, str) for r in raw for k, v in r.items() if k != "line"))
        kit.check("the wrong name raised FileNotFoundError", err.name == "FileNotFoundError", err.name)
        '''),

        md('''
        ## 2. The profile: present, convertible, distinct

        A profile asks three questions of every field before any analysis: is a value present, does it
        convert to the type the field needs, and how many distinct values does it hold. The three
        counts say what each field can be trusted for. An `order_id` that is present on every row but
        distinct on fewer rows says something about the export; an amount present everywhere but
        convertible on fewer says something about the total.

        **Predict before you run.** Which field do you expect to show the biggest gap between
        present and the 201 rows? a) `amount`, because money fields are messy; b) `discount`, which
        Tuesday met as an optional field; c) `order_id`, because every export has gaps in its keys;
        d) none, because an ERP export is complete.
        '''),
        code('''
        FIELDS = ["order_id", "customer_id", "segment", "channel", "city", "order_date", "amount",
                  "status", "quarter", "discount"]
        NUMERIC = {"amount", "discount"}

        def profile(rows, fields=FIELDS):
            """Per field: present, convertible where the field is a number, and distinct."""
            out = {}
            for f in fields:
                values = [r.get(f, "") for r in rows]
                present = [v for v in values if v not in ("", None)]
                ok = [v for v in present if convert(v)[0] is not None] if f in NUMERIC else present
                out[f] = {"present": len(present), "convertible": len(ok), "distinct": len(set(present))}
            return out

        prof = profile(raw)
        kit.table(["field", "present", "convertible", "distinct"],
                  [(f, p["present"], p["convertible"] if f in NUMERIC else "text", p["distinct"])
                   for f, p in prof.items()],
                  caption="The profile of the orders CSV: 201 rows")
        kit.bars([(f, prof[f]["present"]) for f in FIELDS], lit=(7, 9),
                 title="Values present per field, out of 201 rows")
        '''),
        md('''
        **What happened.** The answer is b: `discount` is present on 143 of 201 rows, the gap Tuesday
        met as an optional field. Three smaller signals matter more today. `order_id` is present on all
        201 rows and distinct on only 186, so some order appears more than once. `amount` is present
        on 201 rows and converts on 200. `status` is present on 200. None of those is a total yet; each
        is a question the next rounds answer.

        **Your turn.** A hurried analyst sums the amounts with `int()` straight away. Type these lines
        into the empty cell below and run them. The loop stops with a `ValueError`; read the last line
        aloud, write down the value it names, and say in one sentence what kind of value it is. You
        have two minutes, because this is an error, not the lesson.

        ```python
        total = 0
        for r in raw:
            total += int(r["amount"])
        ```
        '''),
        empty(),
        code('''
        kit.check("order_id repeats: fewer distinct ids than rows", prof["order_id"]["distinct"] < len(raw),
                  f'{prof["order_id"]["distinct"]} distinct of {len(raw)}')
        kit.check("one amount does not convert", prof["amount"]["present"] - prof["amount"]["convertible"] == 1)
        kit.check("discount is optional on 58 rows", len(raw) - prof["discount"]["present"] == 58)
        '''),

        md('''
        ## 3. The trap: a conversion that makes the file look clean

        **The plausible wrong answer.** The `ValueError` stops the pass, so the hurried fix is a helper
        that turns anything unreadable into zero. The loop runs, the profile reports every amount
        convertible, and Q1 comes out at the dashboard's figure. It reads like proof that the dashboard
        was right and Finance is behind.
        '''),
        code('''
        def to_int(value):
            try:
                return int(value)
            except ValueError:
                return 0                     # "so the loop does not crash"

        coerced = [dict(r, amount=to_int(r["amount"])) for r in raw]
        q1_coerced = sum(r["amount"] for r in coerced if r["quarter"] == "Q1")
        failures_seen = sum(1 for r in coerced if not isinstance(r["amount"], int))
        kit.stats([(f"{len(raw) - failures_seen} of {len(raw)}", "amounts convert", "the coerced profile"),
                   (kit.rupees(q1_coerced), "Q1 revenue", "reads as the dashboard's 2.1 crore"),
                   ("0", "failures reported", "nothing in any log")],
                  caption="The hurried pass, as it would be reported")
        '''),
        md('''
        **Why it is wrong.** A zero is a claim: it says Kalpa sold that order for nothing. Finance booked
        it at a value, so the coerced file carries an order the books do not have, and the profile has
        destroyed the one piece of evidence that something was wrong with it. The note to Anand would
        say "every amount converts" and "Q1 is Rs 2,09,98,210", and his analyst, who ties out to the
        rupee, would find a Rs 0 order in a file you called clean. The check that catches it asks a
        business question of the result: can a Kalpa order be worth nothing?
        '''),
        code('''
        zero_orders = [r for r in coerced if r["amount"] == 0]
        smallest_real = min(v for v in (convert(r["amount"])[0] for r in raw) if v is not None)
        kit.check("the coerced file holds an order at Rs 0", len(zero_orders) == 1, f"{len(zero_orders)} order")
        kit.check("no convertible order in the export is below Rs 400", smallest_real >= 400,
                  f"the smallest real amount is {kit.rupees(smallest_real)}")
        '''),
        md('''
        **The fix.** Convert on purpose: `convert()` returns the number or the reason it failed, and every
        failure goes to a rejects log with its file line, its field and its reason. The row is not
        deleted and not zeroed; it is set aside where anybody can read why.
        '''),
        code('''
        accepted, rejects = [], []
        for r in raw:
            value, reason = convert(r["amount"])
            if value is None:
                rejects.append({"line": r["line"], "order_id": r["order_id"], "field": "amount",
                                "value": r["amount"], "reason": reason})
            else:
                accepted.append(dict(r, amount=value))

        q1_accepted = sum(r["amount"] for r in accepted if r["quarter"] == "Q1")
        kit.stats([(f"{len(accepted)} + {len(rejects)}", "accepted and logged", f"of {len(raw)} rows"),
                   (kit.rupees(q1_accepted), "Q1, amounts that convert", "the same rupees, honestly labelled"),
                   (str(len(zero_orders) - len([r for r in accepted if r["amount"] == 0])), "zero orders removed",
                    "the Rs 0 order is gone")])
        kit.columns(["convert", "fail, and say so", "turned into Rs 0"],
                    [("the coerced pass", [len(raw), 0, 1]), ("the honest pass", [len(accepted), len(rejects), 0])],
                    title="The same 201 amounts, profiled two ways")
        kit.flow(["read the text\\n201 amounts", "convert on purpose\\nconvert() returns a reason",
                  "accepted\\n200 numbers", "rejects log\\nline, field, value, reason"],
                 lit=None, kinds=[None, None, None, "good"], title="A failure is counted and kept, never turned into a number")
        kit.check("accepted plus rejected is every row", len(accepted) + len(rejects) == len(raw),
                  f"{len(accepted)} + {len(rejects)} = {len(raw)}")
        kit.check("no accepted order is worth Rs 0", all(r["amount"] > 0 for r in accepted))
        '''),
        md('''
        **What changed.** The rupees did not move: Q1 over the amounts that convert is still
        Rs 2,09,98,210. What moved is the claim. One order went from "sold for Rs 0" to "amount
        unreadable, set aside on the line the log names", and the profile now reports one failure instead
        of none. Whether that order is revenue is a question for round 2, because the log alone cannot
        answer it.

        **Your turn.** Print the rejects log in the empty cell below with `print(rejects)`, open the CSV
        at the line it names, and read the whole row. Write one sentence on what a person would have to
        know to give that order its real amount.
        '''),
        empty(),
        md('''
        > **Kavya's review.** "A conversion that never fails is a conversion that lies. Show me the count
        > of failures next to the count of successes, and the log that names each one."
        '''),

        md('''
        ## 4. The harder variant: the JSON feed and the vendor copy

        The ERP sent two more files. The app's JSON feed should carry the same orders in another format,
        and a vendor sent a short copy of the CSV. A second source is worth having only once you know
        what it holds, so both get the same profile. The feed does not load: `json.load` stops with a
        `JSONDecodeError`, and that message is worth two minutes.

        **Your turn.** Type `json.load(open(DATA / "C2_W01_D03_orders_STUDENT.json"))` into the empty
        cell below and run it. Read the last line: it names a line and a column. Open the file in the
        editor at that line and describe what you see in one sentence.
        '''),
        empty(),
        md('''
        **Predict before you run.** The feed cannot be parsed whole. The code below reads it one complete
        record at a time and stops at the first record that is not complete. How should the feed be used
        afterwards? a) in place of the CSV, because JSON is the app's own format; b) as a second witness,
        compared field by field for the orders it holds; c) not at all, since a broken file proves nothing;
        d) merged into the CSV, so nothing is lost.
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
            nxt = text.find("{", end)
            if nxt == -1:
                break
            at = nxt

        feed_prof = profile(feed)
        pct = lambda n, d: round(100 * n / d, 1)
        kit.columns(["order_id", "status", "amount", "discount"],
                    [("CSV, % present", [pct(prof[f]["present"], len(raw)) for f in ("order_id", "status", "amount", "discount")]),
                     ("JSON feed, % present", [pct(feed_prof[f]["present"], len(feed)) for f in ("order_id", "status", "amount", "discount")])],
                    fmt=lambda v: f"{v:.0f}%", title="Presence per field in the two sources")
        print(len(feed), "complete records recovered from the feed")
        '''),
        md('''
        **What happened.** The answer is b. The feed yields 119 complete records, all of them orders the
        CSV also holds, so it covers part of the export and can confirm it field by field, but it can
        never replace it. Missing looks different in each format: a CSV writes an absent value as an
        empty string, while JSON leaves the key out, so `record["status"]` on a feed record can raise a
        `KeyError` where the CSV quietly returned `""`. A profile that uses `.get(field, "")`, as this one
        does, counts both the same way.
        '''),
        code('''
        csv_by_id = {}
        for r in accepted:
            csv_by_id.setdefault(r["order_id"], r)
        in_csv = sum(1 for r in feed if r["order_id"] in csv_by_id)
        same_amount = sum(1 for r in feed if r["order_id"] in csv_by_id
                          and convert(r.get("amount"))[0] == csv_by_id[r["order_id"]]["amount"])
        kit.check("every feed record is an order the CSV holds", in_csv == len(feed), f"{in_csv} of {len(feed)}")
        kit.check("the feed agrees with the CSV on nearly every amount", same_amount >= len(feed) - 1,
                  f"{same_amount} of {len(feed)} agree")
        '''),
        md('''
        The vendor copy is a short CSV, so it gets the same profile. A good profile shows a problem as a
        count that does not fit, before anybody looks at a row.

        **Predict before you run.** The vendor copy should hold 39 orders in two segments. If a text
        line that is not an order had slipped in, which counts would move? a) only the row count;
        b) the row count, and a field's convertible count, and a field's distinct count; c) nothing,
        because DictReader skips it; d) only the distinct count of `order_id`.
        '''),
        code('''
        vendor = read_orders(DATA / "C2_W01_D03_vendor_STUDENT.csv")
        vprof = profile(vendor)
        kit.bars([("rows read", len(vendor)), ("amounts that convert", vprof["amount"]["convertible"]),
                  ("distinct order ids", vprof["order_id"]["distinct"]), ("distinct segments", vprof["segment"]["distinct"])],
                 title="The vendor copy, profiled before it is used", lit=(1,))
        '''),
        md('''
        **What happened.** The answer is b: 40 rows read, 39 amounts convert, and the segment field
        holds three distinct values where two were expected. Something that is not an order is being
        read as one.

        **Your turn.** In the empty cell below, print every vendor row whose amount does not convert, and
        say what the row is and how it got there.
        '''),
        empty(),
        code('''
        kit.check("the vendor copy reads one row more than its orders", len(vendor) == vprof["amount"]["convertible"] + 1)
        kit.check("the vendor copy shows one segment too many", vprof["segment"]["distinct"] == 3)
        '''),

        md('''
        ### In the interview

        **[F] Everything read from a CSV is a string; what breaks and where do you convert?** "Arithmetic,
        comparison and sorting all break or, worse, silently do the wrong thing. Adding text to a number
        raises a TypeError; comparing `'900'` with `'1200'` sorts by character and puts 900 last; `max` on
        text amounts returns the one that starts with the highest digit. I convert once, at the boundary,
        in one function that returns the value or the reason it failed, and I count and log the failures.
        I never convert inside the analysis, and I never turn a failure into a default without writing
        that decision down, because a zero or a blank is a claim about the business."

        **[S] How do you handle missing data?** "First I measure it per field: present, convertible,
        distinct. Then I ask what the absence means, because an optional discount that is absent means
        no discount, while a missing status means we do not know the order's fate. Then one of three
        decisions, each written down with its reason: drop the record, fill a stated default, or keep
        it and flag it. For money I almost never fill, since the books either have a value or they do
        not."

        ### Depth: LBYL against EAFP

        Python offers two styles for a conversion. Look before you leap checks first, as
        `value.isdigit()` does, and misses cases such as `"-2400"`, which is a valid integer that
        `isdigit` rejects. Easier to ask forgiveness tries the conversion and handles the exception, as
        `convert()` does, which is why this pack converts that way: the rule for what counts as a valid
        amount lives in one place, `int()`, and every refusal comes back with a reason. Real Python's
        article on the two styles (verified 03 Sep 2026, https://realpython.com/python-lbyl-vs-eafp/)
        walks both.
        '''),
        code('''
        kit.flow(["read\\nall text", "profile\\npresent, convertible, distinct", "convert\\nfailures logged",
                  "second witness\\nthe feed, 119 records"], lit=2,
                 title="Round 1, what the room can now do before any total")
        kit.table(["What round 1 established", "The number"],
                  [("Rows the ERP sent in the orders CSV", "201"),
                   ("Distinct order ids among them", "186"),
                   ("Amounts that convert, and failures logged", "200 and 1"),
                   ("Q1 over the amounts that convert", kit.rupees(q1_accepted)),
                   ("Complete records in the JSON feed", str(len(feed)))],
                  caption="The profile, before anyone reconciles")
        kit.check_summary()
        print("Next: round 2 asks why 201 rows hold only 186 orders, and what that does to Q1.")
        '''),
    ]


# --------------------------------------------------------------------------- round 2
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


def round2():
    return [
        md('''
        # Where do the extra rupees in Q1 come from?

        **Week 1, Wednesday. Round 2 of 3: the migration's copies and the identity rule.** By the end of
        this notebook you can say what makes two records the same order, count the rows that break that
        rule, choose which copy to keep, and say what the choice does to Q1 in rupees.

        > **The client asks.** "Which Q1 figure is right, and how do you know? My analyst will want to
        > see every row you removed."
        >
        > Anand Iyer, finance controller, Kalpa Retail

        > **Kavya's review.** "Tell me what makes two rows the same order before you tell me how many
        > duplicates there are. A count of duplicates without an identity rule is a count of nothing."

        Round 1 established that the CSV holds 201 rows but only 186 distinct order ids, that one amount
        does not convert and sits in the rejects log, and that Q1 over the amounts that convert is
        Rs 2,09,98,210. The ERP team's note said the CSV was stitched from two extracts during the Q1
        migration. This round finds out what that stitching did.
        '''),
        md('''
        **Setup.** The same helper and the same two functions as round 1, then round 1's honest pass,
        so this notebook starts from 200 accepted rows and a rejects log of one.
        '''),
        code(LOAD + '''
raw = read_orders()
accepted, rejects = [], []
for r in raw:
    value, reason = convert(r["amount"])
    (accepted if value is not None else rejects).append(dict(r, amount=value, reason=reason))
print(len(accepted), "accepted and", len(rejects), "in the rejects log, from", len(raw), "rows")
'''),
        code("kit.side_by_side(\n    " + LADDER.format(lit=1) + ''',
    kit.vflow(["1. rows against orders\\nper quarter",
               "2. the trap\\na dedupe that finds nothing",
               "3. the identity rule\\nwhich copy stays",
               "4. the harder variant\\ncount the rows, weigh the rupees"], lit=1, show=False),
)'''),

        md('''
        ## 1. Rows against orders, quarter by quarter

        Anand's gap is Rs 20 lakh in Q1. If some orders were exported twice, the rows and the distinct
        orders will disagree, and the quarter where they disagree is where the extra rupees sit.

        **Predict before you run.** Where do you expect the rows and the distinct order ids to part
        company? a) evenly across both quarters; b) mostly in Q1, the quarter of the migration;
        c) mostly in Q2, the newer data; d) nowhere, since the difference is one amount.
        '''),
        code('''
        by_q = {}
        for q in ("Q1", "Q2"):
            rows_q = [r for r in raw if r["quarter"] == q]
            by_q[q] = (len(rows_q), len({r["order_id"] for r in rows_q}))
        kit.columns(["Q1", "Q2"], [("rows", [by_q["Q1"][0], by_q["Q2"][0]]),
                                   ("distinct order ids", [by_q["Q1"][1], by_q["Q2"][1]])],
                    lit=(0,), title="Rows against distinct orders in each quarter")
        kit.table(["quarter", "rows", "distinct order ids", "rows beyond one per order"],
                  [(q, a, b, a - b) for q, (a, b) in by_q.items()])
        '''),
        md('''
        **What happened.** The answer is b. Q1 holds 114 rows for 100 distinct orders, and Q2 holds 87
        rows for 86. Almost all the extra rows sit in Q1, the quarter the migration touched, which is
        the quarter where the dashboard and the books disagree. That is a lead, not yet a proof: the
        next step is to remove them, and there is a tempting way to do it that removes nothing.
        '''),
        code('''
        kit.check("Q1 carries 14 rows beyond one per order", by_q["Q1"][0] - by_q["Q1"][1] == 14)
        kit.check("Q2 carries 1", by_q["Q2"][0] - by_q["Q2"][1] == 1)
        '''),

        md('''
        ## 2. The trap: a dedupe that reports zero duplicates

        **The plausible wrong answer.** Round 1 taught the rejects log to cite a file line, so every
        record now carries `line`. The hurried analyst deduplicates on the whole record, the way most
        tools do by default, and gets a clean answer.
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

        kept_whole = whole_record_dedupe(accepted)
        q1_whole = sum(r["amount"] for r in kept_whole if r["quarter"] == "Q1")
        kit.stats([(str(len(accepted) - len(kept_whole)), "duplicates found", "the whole-record dedupe"),
                   (kit.rupees(q1_whole), "Q1 revenue", "unchanged, so the dashboard looks right"),
                   ("Rs 20 lakh", "left unexplained", "and the note says Finance is wrong")],
                  caption="The hurried dedupe, as it would be reported")
        '''),
        md('''
        **Why it is wrong.** The file line is where a row sat in the export, not what the order is. Two
        copies of one order sit on different lines, so every record is unique by construction and the
        dedupe can never find anything. The note would tell Anand there are no duplicates and his books
        are Rs 20 lakh short, which sends Finance hunting for revenue that was never earned. The check
        that catches it is the one round 1 already printed: 201 rows and 186 distinct order ids cannot
        both be true of a file with zero duplicates.

        The mechanism, on five invented records: two orders appear twice.
        '''),
        code(INVENTED_DUPES + '''
found = len(invented) - len(whole_record_dedupe(invented))
without_line = [{k: v for k, v in r.items() if k != "line"} for r in invented]
found_without = len(without_line) - len(whole_record_dedupe(without_line))
kit.table(["the comparison", "duplicates found in the invented five"],
          [("every field, including the file line", found),
           ("every field except the file line", found_without),
           ("the order id alone", len(invented) - len({r["order_id"] for r in invented}))],
          caption="Invented records: the file line makes every row unique")
'''),
        code('''
        ids = [r["order_id"] for r in raw]
        kit.check("the whole-record dedupe reports zero on the ERP file", len(accepted) - len(kept_whole) == 0)
        kit.check("yet distinct order ids fall 15 short of the rows", len(ids) - len(set(ids)) == 15,
                  f"{len(ids)} rows, {len(set(ids))} ids")
        kit.check("on invented records, dropping the line field finds both copies", found == 0 and found_without == 2)
        kit.bars([("whole record, line included", len(accepted) - len(kept_whole)),
                  ("rows beyond one per order_id", len(ids) - len(set(ids)))], lit=(1,),
                 title="The ERP file: what each comparison says is duplicated")
        '''),

        md('''
        ## 3. The identity rule, and which copy stays

        **The fix.** Say what makes two records the same order before counting anything: here it is
        `order_id`, because the ERP issues one id per order and never reuses it. Group the rows by that
        key. A group of one is an order; a group of two is one order exported twice, and one row of the
        pair has to be chosen.

        The choice is not always free. On invented records again: pair A is an exact copy; in pair B,
        one copy's amount does not convert and the other's does; in pair C, the two copies disagree on
        the date and agree on everything else.

        **Predict before you run.** For pair B, which copy should stay? a) the first, since the first
        extract is the original; b) the one whose amount converts, since the other cannot be summed;
        c) both, until Finance decides; d) neither, since a pair that disagrees cannot be trusted.
        '''),
        code('''
        pairs = [
            {"order_id": "INV-11", "order_date": "2026-05-02", "amount": "1800", "line": 12},
            {"order_id": "INV-11", "order_date": "2026-05-02", "amount": "1800", "line": 90},
            {"order_id": "INV-12", "order_date": "2026-05-14", "amount": "n/a", "line": 20},
            {"order_id": "INV-12", "order_date": "2026-05-14", "amount": "2600", "line": 95},
            {"order_id": "INV-13", "order_date": "2026-08-21", "amount": "3100", "line": 40},
            {"order_id": "INV-13", "order_date": "2026-07-30", "amount": "3100", "line": 99},
        ]

        def identity_rule(rows):
            """Keep one row per order_id: the first copy whose amount converts; log the rest with a reason."""
            kept, log = {}, []
            for r in rows:
                value, _ = convert(r["amount"])
                k = r["order_id"]
                if k not in kept:
                    kept[k] = r
                    continue
                first_ok = convert(kept[k]["amount"])[0] is not None
                if not first_ok and value is not None:
                    log.append((kept[k], "copy whose amount does not convert; its twin carries the value"))
                    kept[k] = r
                else:
                    differs = [f for f in r if f != "line" and r[f] != kept[k].get(f)]
                    log.append((r, "second copy of the order" + (f", differs on {', '.join(differs)}" if differs else "")))
            return list(kept.values()), log

        kept_pairs, log_pairs = identity_rule(pairs)
        kit.tree({"label": "rows sharing an order_id", "kind": "lit", "branches": [
            ("", {"label": "identical\\nkeep the first", "kind": "good"}),
            ("", {"label": "one amount unreadable\\nkeep the copy that validates", "kind": "good"}),
            ("", {"label": "valid, fields disagree\\nkeep the first, log, ask the ERP team", "kind": "known"})]},
            title="Which copy stays: the rule, before the file")
        kit.table(["order", "kept line", "kept amount", "set aside", "reason"],
                  [(k["order_id"], k["line"], k["amount"], r["line"], why)
                   for k in kept_pairs for r, why in log_pairs if r["order_id"] == k["order_id"]],
                  caption="Invented pairs: one row per order, and a reason for every row set aside")
        '''),
        md('''
        **What happened.** The answer is b. Keeping the first copy of pair B would keep the one that
        cannot be summed and throw away the one that carries the order's value, so the rule prefers the
        copy whose fields validate. Pair C is subtler: both copies are valid, they disagree on the date,
        and no rule inside the file can say which date is true. The rule keeps the first extract's row,
        logs the disagreement, and the date becomes a question for the ERP team, written down rather
        than guessed.

        Now the same rule on the ERP file, starting again from the raw rows so the rejected amount can
        find its twin.
        '''),
        code('''
        clean, dup_log = identity_rule(raw)
        clean = [dict(r, amount=convert(r["amount"])[0]) for r in clean]
        q = {x: sum(r["amount"] for r in clean if r["quarter"] == x) for x in ("Q1", "Q2")}
        q_raw = {x: sum(r["amount"] for r in accepted if r["quarter"] == x) for x in ("Q1", "Q2")}
        kit.columns(["Q1", "Q2"], [("as exported, amounts that convert", [q_raw["Q1"] / 1e5, q_raw["Q2"] / 1e5]),
                                   ("one row per order", [q["Q1"] / 1e5, q["Q2"] / 1e5])],
                    fmt=lambda v: f"{v:,.2f} L", lit=(0,), title="Quarter revenue in lakh, before and after the identity rule")
        kit.stats([(str(len(clean)), "orders kept", "one row per order_id"),
                   (str(len(dup_log)), "rows set aside", "each with a reason in the log"),
                   (kit.rupees(q["Q1"]), "Q1", "Anand's books say 1.9 crore"),
                   (kit.rupees(q["Q2"]), "Q2", "one row per order")])
        '''),
        md('''
        **Your turn.** The log holds a reason for every row set aside. In the empty cell below, print the
        rows whose reason says the copies differ, with `[(r["line"], r["order_id"], why) for r, why in
        dup_log if "differs" in why or "twin" in why]`. For each, write which field disagreed and what you
        would ask the ERP team.
        '''),
        empty(),
        code('''
        kit.check("186 orders kept and 15 rows set aside", (len(clean), len(dup_log)) == (186, 15))
        kit.check("every kept order has an amount that converts", all(isinstance(r["amount"], int) for r in clean))
        kit.check("Q1 lands on Rs 1,90,00,000", q["Q1"] == 19000000, kit.rupees(q["Q1"]))
        kit.check("kept plus set aside is every row", len(clean) + len(dup_log) == len(raw))
        '''),
        md('''
        **What changed.** Q1 moved from Rs 2,09,98,210 as exported to Rs 1,90,00,000 with one row per
        order, which is Finance's 1.9 crore. Fifteen rows were set aside, fourteen of them in Q1, and the
        one amount round 1 could not read turned out to be a copy whose twin carries the order's value,
        so no revenue was lost with it.

        > **Kavya's review.** "Good: an identity rule, a preference for the copy that validates, and a
        > reason on every row you set aside. Now show me the rupees each group of rows carried, because
        > fifteen rows is not one kind of problem."
        '''),

        md('''
        ## 4. The harder variant: count the rows, weigh the rupees

        Fifteen rows sounds like one problem. The rupees say otherwise, and the note to Anand has to
        say which rows carried his Rs 20 lakh, since that is what his analyst will check first.

        **Predict before you run.** Of the Rs 19,98,210 the identity rule removed from Q1, what share did
        the Business rows carry? a) about a sixth, since they are 2 of 14 rows; b) about half;
        c) nearly all of it, since a Business order runs to lakhs; d) none, since Business orders
        are never duplicated.
        '''),
        code('''
        removed = [r for r, why in dup_log]
        segs = ["Business", "Retail-Plus", "Retail-Core", "Student"]
        rows_removed = [sum(1 for r in removed if r["segment"] == s) for s in segs]
        rupees_removed = [sum(convert(r["amount"])[0] or 0 for r in removed if r["segment"] == s) for s in segs]
        kit.bars(list(zip(segs, rows_removed)), title="Rows set aside by segment")
        kit.bars(list(zip(segs, rupees_removed)), fmt=kit.rupees, lit=(0,), title="Rupees those rows carried")
        '''),
        md('''
        **What happened.** The answer is c. Two Business rows carry Rs 19,67,560 of the Rs 19,98,210,
        about 98 percent, while the membership tier carries most of the rows and a sliver of the rupees.
        That split decides two different conversations. Anand's gap is explained by two corporate orders
        counted twice. Tuesday's finding is a different matter: the extra rows sit mostly in Retail-Plus
        in Q1, which is the segment and the quarter Tuesday compared, so its orders-per-customer fall
        was measured on inflated Q1 counts. Round 3 recomputes it.
        '''),
        code('''
        share = rupees_removed[0] / sum(rupees_removed)
        kit.check("the Business rows carry over 95 percent of the rupees removed", share > 0.95, f"{share:.1%}")
        kit.check("Retail-Plus carries the most rows set aside", rows_removed[1] == max(rows_removed),
                  f"{rows_removed[1]} of {len(removed)}")
        '''),
        md('''
        ### In the interview

        **[F] How do you find duplicates, and what makes two records the same?** "I start with the
        identity rule, not the tool. I ask what the business says makes two records one thing: for an
        order that is the order id the system issues; for a customer it might be a normalised email or a
        phone number, and for a payment the gateway's reference. Then I count rows against distinct keys.
        A whole-record comparison only finds exact copies, and a copy made in a migration often differs
        somewhere, a timestamp, a load id, a line number. For each group I keep one row by a stated
        preference, usually the copy whose fields validate, and I log every row I set aside with its
        reason. Then I weigh them: two rows can carry more money than a hundred."

        **[F] A dedupe returns zero duplicates. Do you believe it?** "Only after I check it against a
        count of distinct keys. If rows and distinct keys disagree, the dedupe compared on something
        that makes every row unique, such as a load timestamp, a surrogate key or a line number."

        ### Depth: when the identity rule is not one field

        Kalpa's order id is issued by one system, so one field is the identity. A customer arriving from
        two systems is harder: the same person as `anand.iyer@kalpa` and `Anand.Iyer@Kalpa ` differ as text.
        That is record linkage, and it starts the same way, by writing down what makes two records one
        before counting anything. Week 2 meets duplicate keys again, in a join, where they multiply rows
        instead of adding them.
        '''),
        code('''
        kit.flow(["rows against keys\\n201 rows, 186 ids", "the identity rule\\norder_id",
                  "which copy stays\\nthe one that validates", "the log\\n15 rows, 15 reasons",
                  "the weight\\n98% in two rows"], lit=1,
                 title="Round 2, from a count of rows to a reason for each")
        kit.table(["What round 2 established", "The number"],
                  [("Orders kept, one row per order_id", "186"),
                   ("Rows set aside, each with a reason", "15, of which 14 in Q1"),
                   ("Q1 with one row per order", kit.rupees(q["Q1"])),
                   ("Q2 with one row per order", kit.rupees(q["Q2"])),
                   ("Share of removed Q1 rupees in Business rows", f"{share:.0%}")])
        '''),
        code('''
        kit.check_summary()
        print("Next: round 3 decides what else stays, proves the reconciliation to the rupee, and recomputes Tuesday.")
        '''),
    ]


# --------------------------------------------------------------------------- round 3
CLEAN_PASS = LOAD + '''
def identity_rule(rows):
    kept, log = {}, []
    for r in rows:
        value, _ = convert(r["amount"])
        k = r["order_id"]
        if k not in kept:
            kept[k] = r
        elif convert(kept[k]["amount"])[0] is None and value is not None:
            log.append((kept[k], "copy whose amount does not convert; its twin carries the value"))
            kept[k] = r
        else:
            log.append((r, "second copy of the order"))
    return list(kept.values()), log

raw = read_orders()
kept, dup_log = identity_rule(raw)
clean = [dict(r, amount=convert(r["amount"])[0]) for r in kept]
Q = lambda rows, q: sum(r["amount"] for r in rows if r["quarter"] == q)
print(len(clean), "orders from", len(raw), "rows; Q1", kit.rupees(Q(clean, "Q1")), "and Q2", kit.rupees(Q(clean, "Q2")))
'''


def round3():
    return [
        md('''
        # Which figure is right, and can you prove it?

        **Week 1, Wednesday. Round 3 of 3: keep, drop or flag, the reconciliation, and Tuesday
        recomputed.** By the end of this notebook you can make the three-way decision for a missing
        value, defend keeping a large order that is real, prove a reconciliation in rows and in rupees,
        draw the revenue bridge from the dashboard's figure to the books, and say what cleaning did to
        Tuesday's finding.

        > **The client asks.** "Which figure is right, how do you know, and can my analyst follow every
        > decision you made? And tell Marketing whether Tuesday's finding survives."
        >
        > Anand Iyer, finance controller, Kalpa Retail

        > **Kavya's review.** "Two reconciliations, not one: the rows and the rupees. Input equals clean
        > plus rejected, in both. Then tell me what changed in Tuesday's story, including if it got
        > smaller."

        Round 2 kept 186 orders by the identity rule, set 15 rows aside with a reason each, and brought
        Q1 to Rs 1,90,00,000. Two decisions are still open, and a third mistake is waiting at the end.
        '''),
        md('''
        **Setup.** The helper, the two functions, and round 2's identity rule, so this notebook starts
        from the 186 orders and the log of 15.
        '''),
        code(CLEAN_PASS),
        code("kit.side_by_side(\n    " + LADDER.format(lit=2) + ''',
    kit.vflow(["1. a missing status\\ndrop, default, or keep and flag",
               "2. the trap\\nthe real bulk order removed",
               "3. the trap\\ncounts that reconcile, rupees that do not",
               "4. the harder variant\\nTuesday recomputed"], lit=2, show=False),
)'''),

        md('''
        ## 1. A missing status: drop, default, or keep and flag

        One order has no status. Every cleaning act is one of three decisions, and each moves a
        different number: dropping moves revenue, a default invents a fact, and keep and flag leaves
        revenue whole and keeps the order out of any count that needs its status.

        **Predict before you run.** Revenue here is booked value, every order whatever its status, as
        both the dashboard and the books count it. Which decision leaves Q2 revenue and the delivered
        count both honest? a) drop the order; b) default the status to delivered; c) keep the order and
        flag the status as unknown; d) default the status to cancelled.
        '''),
        code('''
        no_status = [r for r in clean if not r["status"]]
        q2 = Q(clean, "Q2")
        delivered = sum(1 for r in clean if r["quarter"] == "Q2" and r["status"] == "delivered")
        options = [("drop the order", q2 - sum(r["amount"] for r in no_status), delivered),
                   ("default to delivered", q2, delivered + len(no_status)),
                   ("keep and flag", q2, delivered)]
        kit.table(["decision", "Q2 revenue", "Q2 delivered orders", "what it claims"],
                  [(d, kit.rupees(v), n, c) for (d, v, n), c in zip(options,
                   ["the order never happened", "the order reached the customer", "the order happened; its fate is unknown"])])
        kit.columns([d for d, _, _ in options], [("Q2 delivered orders", [n for _, _, n in options])],
                    title="The same order under three decisions: only a default invents a delivery")
        '''),
        md('''
        **What happened.** The answer is c. Dropping the order takes a booked order out of revenue that
        Finance has in its books; defaulting to delivered adds a delivery nobody recorded. Keep and flag
        leaves Q2 at Rs 1,87,00,000, keeps the delivered count at what the data can support, and writes
        one line in the decisions log: which order, which field, what was decided and why.
        '''),
        code('''
        decisions = [{"what": "status missing on one Q2 order", "decision": "keep and flag",
                      "why": "revenue is booked value; the status is unknown, so the order stays out of status counts"}]
        kit.check("exactly one order has no status", len(no_status) == 1)
        kit.check("keep and flag leaves Q2 whole", options[2][1] == 18700000, kit.rupees(options[2][1]))
        '''),

        md('''
        ## 2. The trap: the real bulk order removed as an outlier

        **The plausible wrong answer.** Sort Q2's orders and one sits far above the rest, 1.66 times the
        next largest. The hurried analyst calls it an outlier, removes it "to be safe", and reports the
        quarter without it.
        '''),
        code('''
        q2_orders = sorted((r for r in clean if r["quarter"] == "Q2"), key=lambda r: r["amount"], reverse=True)
        top, runner_up = q2_orders[0], q2_orders[1]
        q2_trimmed = Q(clean, "Q2") - top["amount"]
        drop_trimmed = 1 - q2_trimmed / Q(clean, "Q1")
        kit.strip([r["amount"] for r in q2_orders if r["segment"] == "Business"], lit=[0], lo=0, hi=3000000,
                  markers=[("next largest", runner_up["amount"], "plain")],
                  title="Q2's Business orders on one axis; the dark dot is the one a hurried fence removes")
        kit.stats([(kit.rupees(q2_trimmed), "Q2 without it", "the hurried figure"),
                   (f"{drop_trimmed:.1%}", "the drop", "Q1 1.90 crore to Q2 1.58 crore"),
                   (f"{top['amount'] / runner_up['amount']:.2f}x", "the next largest", "why it looked wrong")])
        '''),
        md('''
        **Why it is wrong.** Large is not wrong. Kalpa sells in bulk to corporate buyers through the
        Business segment, where every order runs to lakhs, so a Business order at 29 lakh is the
        business doing what it does. Removing it turns a 1.6 percent dip into a 17.1 percent collapse,
        and Marketing would fund a rescue for a fall that never happened, while Finance, whose books hold
        that order, would reject the whole reconciliation on sight. The check asks whether anything about
        the record is wrong, not whether it is big: a valid id, a known Business customer with other
        orders, every field converting.
        '''),
        code('''
        buyer = top["customer_id"]
        buyer_orders = [r for r in clean if r["customer_id"] == buyer]
        business_min = min(r["amount"] for r in clean if r["segment"] == "Business")
        kit.check("the largest Q2 order is a Business order", top["segment"] == "Business")
        kit.check("its customer placed other orders in both quarters",
                  {r["quarter"] for r in buyer_orders} == {"Q1", "Q2"}, f"{len(buyer_orders)} orders")
        kit.check("Business orders never run below Rs 2 lakh", business_min >= 200000, kit.rupees(business_min))
        '''),
        md('''
        **The fix.** Keep it, flag it, and show the quarter both ways, so nobody has to trust a removal
        they cannot see. What changed: Q2 goes back from Rs 1,57,54,540 to Rs 1,87,00,000, and the drop
        goes back from 17.1 percent to 1.6 percent.
        '''),
        code('''
        decisions.append({"what": "the largest Q2 order, a Business account with other orders",
                          "decision": "keep and flag", "why": "real revenue; shown with and without in the note"})
        kit.line(["Q1", "Q2"], [("every real order kept", [Q(clean, "Q1") / 1e5, Q(clean, "Q2") / 1e5], "good"),
                                ("the bulk order removed", [Q(clean, "Q1") / 1e5, q2_trimmed / 1e5], "bad")],
                 fmt=lambda v: f"{v:,.0f} L", lo=140, title="Quarter revenue in lakh: a dip, or a collapse invented by a fence")
        '''),
        md('''
        > **Kavya's review.** "An outlier is a question about a record, never a reason to delete it.
        > Check the record; if it is real, keep it and say so."
        '''),

        md('''
        ## 3. The trap: counts that reconcile while rupees do not

        **The plausible wrong answer.** A second analyst builds the pass in the order that feels
        natural: remove duplicate ids first, keeping the first copy, then convert amounts and reject the
        ones that fail. The row count reconciles perfectly, and Q1 rounds to Finance's figure.
        '''),
        code('''
        seen, first_copy, set_aside = set(), [], 0
        for r in raw:
            if r["order_id"] in seen:
                set_aside += 1
                continue
            seen.add(r["order_id"])
            first_copy.append(r)
        hurried = [dict(r, amount=convert(r["amount"])[0]) for r in first_copy if convert(r["amount"])[0] is not None]
        rejected = set_aside + len(first_copy) - len(hurried)
        q1_hurried = Q(hurried, "Q1")
        kit.stats([(f"{len(raw)} = {len(hurried)} + {rejected}", "rows reconcile", "input equals clean plus rejected"),
                   (kit.rupees(q1_hurried), "Q1", f"{q1_hurried / 1e7:.2f} crore, which reads as Finance's 1.9"),
                   ("done", "the hurried verdict", "reconciled, ship it")])
        '''),
        md('''
        **Why it is wrong.** Rounded to the crore, Rs 1,89,98,210 looks like 1.9. To the rupee it is
        Rs 1,790 short of the books, because keeping the first copy kept the one whose amount could not
        be read and set aside its twin, which carried the value. A count reconciliation proves only that
        no row vanished; it cannot prove that the right rows stayed. Anand's analyst ties out to the rupee,
        finds a booked order missing from a file you called reconciled, and stops trusting every other
        decision in the log. The check is the second reconciliation, in rupees, against the books.
        '''),
        code('''
        BOOKS_Q1 = 19000000   # Anand's Q1, which his analyst sends to the rupee
        kit.check("the hurried rows reconcile", len(raw) == len(hurried) + rejected)
        kit.check("the hurried Q1 misses the books by Rs 1,790", BOOKS_Q1 - q1_hurried == 1790,
                  kit.rupees(BOOKS_Q1 - q1_hurried))
        kit.check("the pass that converts first lands on the books", Q(clean, "Q1") == BOOKS_Q1)
        '''),
        md('''
        **The fix.** Convert first, then apply the identity rule preferring the copy that validates, then
        reconcile twice. Rows: 201 in equals 186 kept plus 15 set aside. Rupees: Q1 as exported minus
        the rupees carried by the rows set aside equals the books. The bridge is that second
        reconciliation drawn, and it is the page Anand's analyst will check.

        **Predict before you run.** The bridge starts at Q1 as exported, Rs 2,09,98,210, and must land on
        the books. How many moves does it need to get there? a) one, the duplicates; b) two, the
        corporate copies and the consumer copies; c) three, adding the unreadable amount; d) none,
        since the start already rounds to 2.1.
        '''),
        code('''
        exported_q1 = sum(convert(r["amount"])[0] or 0 for r in raw if r["quarter"] == "Q1")
        q1_removed = [r for r, _ in dup_log if r["quarter"] == "Q1"]
        corporate = -sum(convert(r["amount"])[0] or 0 for r in q1_removed if r["segment"] == "Business")
        consumer = -sum(convert(r["amount"])[0] or 0 for r in q1_removed if r["segment"] != "Business")
        kit.bridge(("Q1 as exported", exported_q1),
                   [("copies of corporate orders", corporate), ("copies of consumer orders", consumer)],
                   end_label="Q1 clean, the books", lit=(0,), lo=18800000,
                   title="From the dashboard's 2.1 crore to the books' 1.9; the axis starts at Rs 1.88 crore")
        kit.table(["reconciliation", "in", "kept", "set aside", "holds"],
                  [("rows, whole file", len(raw), len(clean), len(dup_log), len(raw) == len(clean) + len(dup_log)),
                   ("rupees, Q1", kit.rupees(exported_q1), kit.rupees(Q(clean, "Q1")), kit.rupees(-(corporate + consumer)),
                    exported_q1 + corporate + consumer == Q(clean, "Q1"))])
        '''),
        md('''
        **What happened.** The answer is b. The copies of two corporate orders carry Rs 19,67,560 and the
        copies of the consumer orders carry Rs 30,650, and the bridge lands on Rs 1,90,00,000, the books,
        to the rupee. The unreadable amount needs no move: it was never in the exported total, and its
        twin, which was, stayed. What changed against the hurried pass: one Retail-Plus order and its
        Rs 1,790 are back, and both reconciliations hold.
        '''),
        code('''
        kit.check("the bridge lands on the books", exported_q1 + corporate + consumer == BOOKS_Q1)
        kit.check("the rows reconcile", len(raw) == len(clean) + len(dup_log))
        decisions.append({"what": "15 rows sharing an order_id with another row", "decision": "set aside",
                          "why": "identity rule on order_id; the copy that validates stays"})
        kit.table(["what", "decision", "why"], [(d["what"], d["decision"], d["why"]) for d in decisions],
                  caption="The decisions log, so every act can be followed")
        '''),

        md('''
        ## 4. The harder variant: Tuesday recomputed on clean data

        Tuesday told the leadership group that revenue fell about 11 percent from Q1 to Q2 and that
        Retail-Plus orders per customer fell 49 percent, from 2.32 to 1.18. Both numbers were measured on
        the export as delivered. The honest analyst recomputes and reports what changed, including if the
        finding got smaller.

        **Predict before you run.** On clean data, what happens to Tuesday's Retail-Plus finding?
        a) it disappears, since the duplicates caused it; b) it survives, smaller; c) it grows, since
        clean data sharpens it; d) it moves to Retail-Core.
        '''),
        code('''
        def per_customer(rows, q, seg):
            rs = [r for r in rows if r["quarter"] == q and r["segment"] == seg]
            return len(rs) / len({r["customer_id"] for r in rs})

        segs = ["Retail-Core", "Retail-Plus", "Business", "Student"]
        tuesday = {"Retail-Core": (1.12, 1.06, -5.3), "Retail-Plus": (2.32, 1.18, -49.0),
                   "Business": (1.82, 1.55, -15.0), "Student": (2.50, 3.50, 40.0)}
        dirty = [tuesday[s][2] for s in segs]
        cleaned = [round(100 * (per_customer(clean, "Q2", s) / per_customer(clean, "Q1", s) - 1), 1) for s in segs]
        kit.table(["segment", "Tuesday Q1", "Tuesday Q2", "Tuesday change", "clean Q1", "clean Q2", "clean change"],
                  [(s, tuesday[s][0], tuesday[s][1], f"{d:+.1f}%", round(per_customer(clean, "Q1", s), 2),
                    round(per_customer(clean, "Q2", s), 2), f"{c:+.1f}%") for s, d, c in zip(segs, dirty, cleaned)],
                  caption="Orders per customer, Q1 to Q2: as Tuesday reported it, and on clean data")
        kit.columns(segs[:3], [("fall as Tuesday reported", [-d for d in dirty[:3]]), ("fall on clean data", [-c for c in cleaned[:3]])],
                    fmt=lambda v: f"{v:.0f}%", lit=(1,), title="The fall in orders per customer, in percent; Student rose and is left out")
        '''),
        code('''
        rev_dirty = 1 - 18700000 / 21000000
        rev_clean = 1 - Q(clean, "Q2") / Q(clean, "Q1")
        kit.line(["Q1", "Q2"], [("as Tuesday reported, Rs lakh", [210.0, 187.0], "bad"),
                                ("on clean data, Rs lakh", [Q(clean, "Q1") / 1e5, Q(clean, "Q2") / 1e5], "good")],
                 fmt=lambda v: f"{v:,.0f}", lo=150, title="Revenue Q1 to Q2: an 11 percent fall becomes 1.6 percent")
        kit.check("Retail-Plus still falls on clean data", cleaned[1] < -30, f"{cleaned[1]:+.1f}%")
        kit.check("the Retail-Plus fall is smaller than Tuesday reported", cleaned[1] > dirty[1])
        kit.check("the revenue drop shrinks to under 2 percent", rev_clean < 0.02, f"{rev_clean:.1%} against {rev_dirty:.1%}")
        '''),
        md('''
        **What happened.** The answer is b. Retail-Plus orders per customer fall 35.0 percent on clean
        data, from 1.82 to 1.18, against the 49 percent Tuesday reported: the finding stands, smaller,
        because most of the migration's copies sat in Retail-Plus in Q1. The revenue drop shrinks from
        11.0 percent to 1.6 percent. Both go in the note, the smaller numbers first, because a finding that
        shrank and was reported honestly is worth more to Marketing than one that was never checked.

        **The note to Finance, in under 120 words.** "Anand, your 1.9 crore is right. The ERP export
        counted fifteen rows twice, fourteen of them in Q1; two copies of corporate orders carry
        Rs 19,67,560 of the Rs 19,98,210 difference. Rows reconcile, 201 received equals 186 kept plus
        15 set aside, and rupees reconcile to your books exactly. Every row set aside and every decision
        is in the attached log. Two things we kept and flagged: one Q2 order with no status, and the
        largest Q2 order, a real Business account. On clean data the Q1 to Q2 drop is 1.6 percent, not 11,
        and the Retail-Plus frequency fall is 35 percent, not 49. It survives, smaller."
        '''),
        md('''
        ### In the interview

        **[S] Finance and your dashboard disagree; what do you do?** "I assume nobody is lying and
        both numbers are computed correctly from different inputs, so I find the difference rather than
        pick a side. I get Finance's figure to the rupee and its definition, profile my source, and build a
        bridge from my number to theirs, one move per cause, each move backed by the rows that carry it.
        I reconcile twice, in rows and in rupees. When the bridge closes, I say which figure is right and
        why, fix the source, and recompute anything that was reported from the wrong number."

        **[D] An auditor asks why you dropped 14 rows; walk them through it.** "They were not dropped;
        they were set aside, and each is in the log. Fourteen Q1 rows share an order id with another row.
        The identity rule is the order id, because the ERP issues one per order. For each pair I kept
        the copy whose fields validate, and I can show the rupees: two corporate copies carry
        Rs 19,67,560 and the rest Rs 30,650. The rows reconcile, 114 Q1 rows in and 100 kept, and the
        rupees bridge to your books exactly."

        **[S] How do you handle outliers?** "I sort and look at the tail, then ask whether the record is
        wrong, not whether it is big. A valid id, a real account and fields that convert make it
        revenue. I keep it, flag it, and show the result with and without it, so the reader sees how much
        one record carries."

        ### Depth: why reconcile in both units

        A count reconciliation proves no row vanished, and a rupee reconciliation proves the right value
        stayed. Each catches what the other cannot: this morning's hurried pass reconciled in rows and
        lost Rs 1,790, and a pass that swapped one kept order for another of the same value would
        reconcile in rupees and hide the swap in the rows. Finance teams reconcile control totals in both
        units for exactly that reason.
        '''),
        code('''
        kit.flow(["decide\\nkeep, drop or flag", "check the tail\\nkeep the real bulk order",
                  "reconcile rows\\n201 = 186 + 15", "reconcile rupees\\nthe bridge to the books",
                  "recompute\\nTuesday, smaller"], lit=3,
                 title="Round 3, from decisions to a reconciliation Finance can audit")
        kit.table(["What round 3 established", "The number"],
                  [("Q1 clean, equal to the books", kit.rupees(Q(clean, "Q1"))),
                   ("Q2 clean, every real order kept", kit.rupees(Q(clean, "Q2"))),
                   ("Revenue change Q1 to Q2", f"-{rev_clean:.1%}, not -{rev_dirty:.1%}"),
                   ("Retail-Plus orders per customer", "1.82 to 1.18, -35.0%, not -49.0%"),
                   ("Decisions in the log", str(len(decisions)))])
        '''),
        code('''
        kit.check_summary()
        print("Next: the escalated case runs the whole pass alone; Thursday asks whether the smaller Retail-Plus fall is real.")
        '''),
    ]


# --------------------------------------------------------------------------- the escalated case, TODO twin
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
#   b) customer_id and order_date together
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
exported_q1 = sum(convert(r["amount"])[0] or 0 for r in raw if r["quarter"] == "Q1")
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
    3: "d. the ERP issues one order_id per order. a finds nothing because the line makes every row unique, b merges two real orders placed the same day, and c misses copies that differ on one field.",
    4: "b. the copy that validates carries the value. a keeps an unreadable amount and loses Rs 1,790, c picks by size, which is no rule, and d is a coin toss dressed as one.",
    5: "a. revenue is booked value and the fate is unknown. b removes a booked order, c and d invent a status.",
    6: "c. it is a real Business order. a turns a 1.6 percent dip into 17.1, b invents a smaller order, and d moves revenue between quarters.",
    7: "b. rows and rupees both reconcile. a is the count-only pass that lost Rs 1,790, c proves nothing about rupees, and d is false, since the log holds one reject.",
    8: "d. 1.82 to 1.18 is a fall of 35.0 percent. a and b misread the recompute, and c confuses segments.",
}

CASE_HELPERS = LOAD + '''
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

Q = lambda rows, q: sum(r["amount"] for r in rows if r["quarter"] == q)

def per_customer(rows, q, seg):
    rs = [r for r in rows if r["quarter"] == q and r["segment"] == seg]
    return len(rs) / len({r["customer_id"] for r in rs})
'''


def case_cells(solution):
    import re
    cells = [
        md('''
        # The escalated case: the full pass, alone

        **Week 1, Wednesday afternoon, the escalated case.** Anand has replied: "Send the reconciliation
        and the log by five. My analyst checks it tonight." Run the whole pass on the ERP export: read and
        profile, convert with a rejects log, apply the identity rule, make the two open decisions,
        reconcile in rows and in rupees, draw the bridge, and recompute Tuesday.

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
        code("kit.side_by_side(\n    " + LADDER.format(lit=3) + ''',
    kit.vflow(["read and profile", "convert with a log", "the identity rule", "two decisions",
               "reconcile twice", "Tuesday and the note"], lit=0, show=False),
)'''),
    ]
    for n, (title, body, check) in enumerate(CASE_STEPS, start=1):
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


# --------------------------------------------------------------------------- the second case, TODO twin
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
#   c) 14 Q1 rows are second copies set aside by the order_id rule; rows and rupees reconcile
#   d) the 14 rows were outliers
statement = __TODO5__
''', '''
kit.check("rows reconcile in Q1", q1_in == q1_kept + len(q1_aside))
kit.check("rupees reconcile in Q1", sum(convert(r["amount"])[0] or 0 for r in raw if r["quarter"] == "Q1") - sum(rupees_by) == 19000000)
kit.flow(["the question\\nwhy 14 rows", "the rule\\norder_id", "the twins\\nall 14 have one",
          "the rupees\\nby segment", "the signature\\nboth reconcile"], lit=4, title="The auditor's walk through the log")
kit.check_summary()
'''),
]
AUDIT_ANSWERS = {1: "q1_in - q1_kept", 2: 'r["order_id"] in kept_ids', 3: "list(zip(segs, rows_by, rupees_by))",
                 4: '{"copy": "kept", "field": "which one differed", "why": "the copy that validates"}',
                 5: '"14 Q1 rows are second copies set aside by the order_id rule; rows and rupees reconcile"'}
AUDIT_WHY = {
    1: "b. the auditor asked about Q1. a counts both quarters and gives 15, c counts orders not rows, and d counts the one unreadable amount.",
    2: "a. a twin is the same order_id. b and c match different orders that happen to share a value or a buyer, and d is where a row sits, not what it is.",
    3: "b. the auditor needs rows and rupees by kind, since two rows carry 98 percent of the money. a hides that, c hides the other rows, and d answers a different quarter.",
    4: "b. a pair that differs needs the kept copy, the field and the reason. a leaves the auditor guessing, c invents a value, and d is false.",
    5: "c. it states the rule and both reconciliations. a calls copies errors and says deleted, b reverses the finding, and d confuses copies with outliers.",
}


def audit_cells(solution):
    import re
    cells = [
        md('''
        # The second case: the auditor's question

        **Week 1, Wednesday afternoon, the second case, in pairs.** Anand's auditor writes: "Your log says
        14 Q1 rows were dropped. Why those 14, and how do I know nothing else went with them?" Answer
        from the decisions log and the file, one question at a time. One of the pair drives; the other
        plays the auditor and asks the next question only when the check passes.

        Each question has lettered choices above a placeholder such as `__TODO1__`. Replace it with the
        code of the option you choose. Run as shipped, the notebook stops at the first placeholder with a
        `NameError`, which is expected. Post your five letters when every check passes.
        ''' if not solution else '''
        # The second case: the auditor's question, solution

        **Week 1, Wednesday afternoon, the second case, solution twin.** Every placeholder filled, run
        clean. The letters, in order: 1b 2a 3b 4b 5c.
        '''),
        code(AUDIT_HELPERS),
        code("kit.side_by_side(\n    " + LADDER.format(lit=4) + ''',
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


BUILDS = {
    "r1": lambda: build(NB / "C2_W01_D03_01_profile_STUDENT.ipynb", round1()),
    "r2": lambda: build(NB / "C2_W01_D03_02_duplicates_STUDENT.ipynb", round2()),
    "r3": lambda: build(NB / "C2_W01_D03_03_bridge_STUDENT.ipynb", round3()),
    "case": lambda: (build(NB / "C2_W01_D03_hands_on_STUDENT.ipynb", case_cells(False), execute=False),
                     build(SOL / "C2_W01_D03_hands_on_solution_STUDENT.ipynb", case_cells(True))),
    "audit": lambda: (build(NB / "C2_W01_D03_ex2_auditor_STUDENT.ipynb", audit_cells(False), execute=False),
                      build(SOL / "C2_W01_D03_ex2_auditor_solution_STUDENT.ipynb", audit_cells(True))),
}

if __name__ == "__main__":
    for name in (sys.argv[1:] or list(BUILDS)):
        BUILDS[name]()
        print("built", name)
