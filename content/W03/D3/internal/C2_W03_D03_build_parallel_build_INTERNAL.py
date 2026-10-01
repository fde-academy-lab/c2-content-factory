"""Write and execute the parallel-build notebook for Build 1 Wednesday, the New York revenue tree.

    python3 content/W03/D3/internal/C2_W03_D03_build_parallel_build_INTERNAL.py

The notebook reads the Kalpa Health files where Monday's pack keeps them, content/W03/D1/data/,
through a relative path from its own folder, so no copy of any file enters this day. It is built
with scripts/nb_make.py and executed cold in content/W03/D3/parallel-build/, the folder a learner's
Codespace runs it from.

The slice is one metro's billed revenue, New York, Q2 against Q3 of 2026, from the old booking
export and the claims, stopped at the leaves a claim carries. The files are the US pack of decision
build1-us-data, so amounts are dollars. The run sheet in parallel-build/ says which plants the slice
runs beside and how the trainer holds each; no cell below names one, and every number in the
markdown is one the cells print, recomputed by internal/C2_W03_D03_numbers_INTERNAL.py.
"""
import pathlib
import sys

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "scripts" / "nb_make.py").exists())
sys.path.insert(0, str(ROOT / "scripts"))
from nb_make import SETUP, build, code, md  # noqa: E402

OUT = ROOT / "content/W03/D3/parallel-build/C2_W03_D03_new_york_revenue_tree_STUDENT.ipynb"

cells = [
    md("""
    # Did New York's billed revenue grow from Q2 to Q3, and did more claims or bigger claims carry it?

    **Week 3, Build 1, Wednesday: the parallel build on one metro.** Kalpa Health is a US
    diagnostics business, fictional and synthetic in every record. It runs a laboratory and two
    patient service centres, where patients have blood drawn, in each of six US metro areas, and its
    revenue-cycle and analytics work runs from Kalpa's Global Capability Centre (GCC) in Bengaluru,
    where you work as trainee engineers in the data and AI team. A completed booking is billed as one claim, a bill
    at Kalpa Health's list prices sent to whoever pays for the patient's tests: a commercial health
    plan, Medicare, Medicaid or the patient. The quarters are calendar Q2 (April to June 2026) and
    Q3 (July to September 2026), and every file is the export taken on Friday 16 October 2026.

    > **The client asks.** "My dashboard says test volumes grew 5 percent from Q2 to Q3. The plan
    > the board approved asks for 18. Which branch of my business is short, and what do I do next?"
    >
    > Dr Priya Menon, chief operating officer, Kalpa Health

    Each of the five questions Dr Menon's heads have asked needs the same moves before it has a
    claim: say what one row is, convert every amount, reconcile one file against another, and only
    then split the number. This notebook runs those moves once, end to end, on a question smaller
    than any group's: New York's billed revenue, one metro of six. The metric at stake is **billed
    revenue**, the dollars on the claims at list prices, which splits into two leaves: how many
    claims were billed, and the mean claim, the average dollars on one claim. Quest Diagnostics, a
    US laboratory company, states its own growth the way this notebook ends, with the period and
    both bases in one sentence (section 8).

    **Who needs the answer.** The finance head, who writes the board's page on where the plan's
    growth went and reads each metro's billed revenue as claims times the mean claim. A metro read
    wrongly, as slower than it was because rows were counted as bookings, or with its totals swollen
    because one file was joined to another twice, sends the recovery effort to a place that was never
    short.

    **The questions on the way.**
    1. How could a team find what moved New York's billed revenue, and what does each way cost?
    2. How many New York bookings does the export hold, once a row stops counting as a booking?
    3. Does every New York amount convert to dollars, or does the total come out short without a warning?
    4. Do the claims and the completed bookings describe the same visits, one to one?
    5. Did more claims or a bigger mean claim carry the change, and does it hold per day?
    6. Which New York site billed the extra claims, and where does this build stop?
    7. Does SQL, run on the same raw files, reach the same claims and dollars?
    8. What sentence can the finance head carry, with its denominators, its period and its caveat?
    """),
    md("""
    **Setup.** The next cell finds the shared helper `kit` by walking up from this folder, then reads
    two of the ten Kalpa Health files from Monday's data folder, `../../D1/data/`: the old booking
    system's export and the billing system's claims. Every value is read as text, so nothing is
    converted before it has been looked at, and the cell keeps each file's New York rows.
    `quarter()` reads Q2 or Q3 from an ISO date, and `usd()` prints dollars the way a US price list
    does.
    """),
    code(SETUP + '''
import pandas as pd

DATA = pathlib.Path("../../D1/data")
raw_bookings = pd.read_csv(DATA / "C2_W03_D01_bookings_legacy_STUDENT.csv", dtype=str, keep_default_na=False)
raw_claims = pd.read_csv(DATA / "C2_W03_D01_claims_STUDENT.csv", dtype=str, keep_default_na=False)

# The slice: New York only. A group profiles its whole file; this build profiles the rows it uses.
bookings = raw_bookings[raw_bookings["metro"] == "New York"].copy()
claims = raw_claims[raw_claims["metro"] == "New York"].copy()

def quarter(dates):
    """Q2 is April to June and Q3 is July to September, read from the ISO date text."""
    return dates.map(lambda d: "Q2" if d < "2026-07-01" else "Q3")

def usd(value, cents=False):
    """Dollars with a thousands comma and, where asked, the cents."""
    v = float(value)
    text = f"${abs(v):,.2f}" if cents else f"${abs(round(v)):,}"
    return "-" + text if v < 0 else text

bookings["quarter"] = quarter(bookings["booking_date"])
claims["quarter"] = quarter(claims["service_date"])
print(f"New York rows read: {len(bookings):,} from the old booking export, {len(claims):,} from the claims")
'''),
    code('''
kit.side_by_side(
    kit.ladder(["Which way, at what cost?", "How many bookings?", "Does every amount convert?",
                "Do claims match bookings?", "More claims, or bigger?", "Which site, and where to stop?",
                "Does SQL agree?", "What can the finance head carry?"], lit=None, show=False),
    kit.vflow(["one metro, two files\\nthe old booking export and the claims",
               "one rule per decision\\nwritten in the decisions log",
               "one claim\\nwith its denominators, period and caveat"], show=False),
)
'''),

    # ----------------------------------------------------------------- 1: the options
    md("""
    ## 1. How could a team find what moved New York's billed revenue, and what does each way cost?

    Billed revenue is what Kalpa Health asked the payers for, at list prices. At Kalpa Retail an
    order's amount was what the shopper paid at the till; at Kalpa Health the payers pay a contracted
    share of a claim weeks later, so billed revenue is a request, and the money that arrives is a
    smaller number for a different decision. The domain dossier, `content/W03/D1/study-notes/C2_W03_D01_domain_us_healthcare_STUDENT.md`,
    follows one claim from the list price to the cash in its section 3, for more depth. The finance
    head's question is what moved the billed number, and four ways could answer it.

    | Option | What the team does | Rows it reads | What it can say | What it assumes |
    |---|---|---|---|---|
    | A. Compare the totals | Sums each quarter's billed dollars on the claims | The claims | Whether billed revenue grew, and by how many dollars | Every amount is a number |
    | B. The tree on the claims alone | Splits each quarter into claims times the mean claim | The claims | Whether more claims or bigger claims carried the change | Each claim is one completed booking, and each completed booking has one claim |
    | C. The tree after reconciling | Keeps one row per booking, proves the claims match the completed bookings one to one, then splits | The booking export and the claims | The same split, plus a count of visits the finance head's analyst can audit | One booking id is one booking |
    | D. The tree on the booking export | Takes the export's rows as the volume and divides billed dollars by them | The booking export, and the claims' totals | A volume and the billed dollars per booking | Every row is one completed, billed booking |

    **Predict before you run.** Which two options will report different growth in volume on the same
    New York files? a) B and C, which read different files; b) B and D, which count different things;
    c) none of them, since all three read the same quarters; d) all three, since each reads its own
    rows.
    """),
    code('''
import time

start = time.perf_counter()
claims_q = claims.groupby("quarter").size()
rows_q = bookings.groupby("quarter").size()
seconds = time.perf_counter() - start
grow = lambda s: s["Q3"] / s["Q2"] - 1
kit.table(["Option", "Rows read", "Volume growth it reports", "What it would miss", "Hours for a group, estimated"],
          [["A. Compare the totals", f"{len(claims):,}", "none, totals only", "Which leaf moved", "about 0.2"],
           ["B. The tree on the claims alone", f"{len(claims):,}", f"{grow(claims_q):+.1%}, claims",
            "A claim that is not a visit, or a visit never billed", "about 0.3"],
           ["C. The tree after reconciling", f"{len(bookings) + len(claims):,}", "B's figure, once proved or disproved",
            "Nothing these two files can show", "about 1"],
           ["D. The tree on the booking export", f"{len(bookings):,}", f"{grow(rows_q):+.1%}, export rows",
            "Cancelled bookings and repeated rows, counted as visits", "about 0.3"]],
          caption=f"The four options, sized on New York's files as exported; both counts ran in {seconds:.3f} seconds")
kit.columns(["B. claims", "D. export rows"], [("Q2", [claims_q["Q2"], rows_q["Q2"]]), ("Q3", [claims_q["Q3"], rows_q["Q3"]])],
            title="Two cheap ways to count New York's volume, on the same two quarters")
'''),
    md("""
    **What happened.** The answer is b. On the same quarters, the claims grow 8.0 percent and the
    export's rows 4.8 percent, so the two cheap ways disagree by more than three points before
    anyone has asked why. Option A cannot see the split at all. Every option runs in under a second
    on these rows, so what separates them is an analyst's hour.

    **The best-fit call.** C. Only a reconciliation can say which of B's and D's counts is New
    York's volume, and it costs about 2,100 more rows and an hour against a number the finance head
    will put on the board's page. D is out, since it assumes every row is one completed, billed
    booking, which is exactly what C tests. **What would switch it.** A control total from Dr
    Menon's data team, signed, saying the claims file holds one claim per completed booking and
    nothing else, would make B enough and save the hour.
    """),

    # ----------------------------------------------------------------- 2: one row per booking
    md("""
    ## 2. How many New York bookings does the export hold, once a row stops counting as a booking?

    Week 1 Wednesday's first move is the profile: what one row is, how many there are and what each
    column holds, before anything is cleaned. A booking is one patient's visit to have tests done,
    and the data dictionary says one row of this export is one booking. The export holds 2,128 New
    York rows, and a hurried count calls that 2,128 bookings and moves on.

    **Predict before you run.** How many New York bookings does the old export hold? a) exactly
    2,128, one per row; b) fewer than 2,128; c) more than 2,128, since cancelled bookings sit in
    another file; d) no way to tell until the claims file has been read.
    """),
    code('''
def profile(df, columns):
    """Per column: filled, blank, distinct values, and one example, which is the Week 1 profile."""
    rows = []
    for c in columns:
        filled = (df[c] != "").sum()
        rows.append([c, f"{filled:,}", f"{len(df) - filled:,}", f"{df[c].nunique():,}", df[c].iloc[0]])
    return rows

kit.table(["Column", "Filled", "Blank", "Distinct", "Example"],
          profile(bookings, ["booking_id", "patient_id", "site_code", "booking_date", "channel", "status", "updated_at"]),
          caption=f"The old booking export, New York rows: {len(bookings):,}")
kit.table(["Column", "Filled", "Blank", "Distinct", "Example"],
          profile(claims, ["claim_id", "booking_id", "service_date", "billed_amount"]),
          caption=f"The claims, New York rows: {len(claims):,}. The tree reads these four columns.")
distinct_ids = bookings["booking_id"].nunique()
kit.check("the export holds more rows than distinct booking ids", len(bookings) > distinct_ids,
          f"{len(bookings):,} rows, {distinct_ids:,} distinct ids")
kit.check("every claim id appears once", claims["claim_id"].is_unique, f"{len(claims):,} claims")
rows_q = bookings.groupby("quarter").size()
ids_q = bookings.groupby("quarter")["booking_id"].nunique()
wrong, right = rows_q["Q3"] / rows_q["Q2"] - 1, ids_q["Q3"] / ids_q["Q2"] - 1
kit.table(["Count", "Q2", "Q3", "Change"],
          [["Rows in the export (the plausible wrong answer)", f"{rows_q['Q2']:,}", f"{rows_q['Q3']:,}", f"{wrong:+.1%}"],
           ["Distinct booking ids", f"{ids_q['Q2']:,}", f"{ids_q['Q3']:,}", f"{right:+.1%}"],
           ["Extra rows", f"{rows_q['Q2'] - ids_q['Q2']}", f"{rows_q['Q3'] - ids_q['Q3']}", ""]],
          caption="New York, the old booking export, counted two ways")
kit.check("rows and bookings disagree on New York's growth", round(wrong, 3) != round(right, 3),
          f"{wrong:+.1%} on rows, {right:+.1%} on bookings")
'''),
    md("""
    **What happened.** The answer is b. The export holds 2,128 New York rows and 2,095 distinct
    `booking_id` values, so 33 ids appear on two rows each. The claims pass the same test: 2,032
    rows and 2,032 distinct claim ids. `channel`, how the patient booked, is blank on 43 rows; this
    tree splits by site, so the column is logged as not used and left as it is. The billed amounts
    were read as text, which section 3 deals with.

    **The plausible wrong answer.** Count rows per quarter and call them bookings, as the last table
    does. New York then grows from 1,039 to 1,089, a rise of 4.8 percent, the number a hurried
    analyst would send.

    **Why it is wrong.** The repeated ids are not spread evenly: 26 of the 33 extra rows sit in Q2
    and 7 in Q3, so counting rows swells the base quarter and makes New York look slower than it was.
    A metro reported at 4.8 percent when its bookings grew 6.8 percent could be the one Dr Menon
    decides to fix. The check that catches it is the one above, rows against distinct ids, per
    quarter, before any rate is written.

    **The fix: one rule for what makes a booking.** One `booking_id` is one booking, the Week 1
    Wednesday identity rule. Where two rows share an id, keep the row with the later `updated_at`,
    the system's latest word on the booking. Of the 33 pairs, 26 are identical in every field and 7
    differ only in `updated_at`, so the rule loses no fact about any booking. Why a booking was
    exported twice is a question for Dr Menon's data team; it goes into the challenges log as a
    question, and the rule does not wait for the answer.
    """),
    code('''
pairs = bookings[bookings["booking_id"].duplicated(keep=False)].groupby("booking_id")
identical = sum(1 for _, g in pairs if len(g.drop_duplicates()) == 1)
only_updated = sum(1 for _, g in pairs
                   if len(g.drop_duplicates()) == 2 and len(g.drop(columns=["updated_at"]).drop_duplicates()) == 1)
clean = bookings.sort_values(["booking_id", "updated_at"]).drop_duplicates("booking_id", keep="last")
set_aside = len(bookings) - len(clean)
kit.table(["Repeated ids", "Identical in every field", "Differ only in updated_at", "Rows set aside"],
          [[f"{pairs.ngroups}", f"{identical}", f"{only_updated}", f"{set_aside}"]],
          caption="What the identity rule decided")
kit.check("rows read equal rows kept plus rows set aside", len(bookings) == len(clean) + set_aside,
          f"{len(bookings):,} = {len(clean):,} + {set_aside}")
kit.check("every repeated pair differs, if at all, only in updated_at", identical + only_updated == pairs.ngroups,
          f"{identical} + {only_updated}")
kit.check("the kept rows hold one row per booking id", clean["booking_id"].is_unique)
'''),

    # ----------------------------------------------------------------- 3: amounts
    md("""
    ## 3. Does every New York amount convert to dollars, or does the total come out short without a warning?

    Revenue can only be summed once every amount is a number, and a conversion that fails without a
    message costs more than one that stops the run. The `billed_amount` column was read as text. The quick fix is
    `pd.to_numeric(..., errors="coerce")`, which turns anything it cannot read into a blank and lets
    the sum carry on. Week 1 Wednesday's rule for an amount that cannot be read was to reject it and
    repair it only from a source that could not have copied the error, never to let it vanish.

    **Predict before you run.** What does the coerced sum do to New York's billed revenue? a) it
    stops with an error at the first amount it cannot read; b) it matches the true total to the
    dollar, since coerce only changes the type; c) it doubles, since text amounts are joined before
    they are added; d) it comes out short, because a few amounts become blanks.
    """),
    code('''
coerced = pd.to_numeric(claims["billed_amount"], errors="coerce")
dropped = claims[coerced.isna()]
wrong_total = coerced.groupby(claims["quarter"]).sum()
kit.table(["What the coerced sum shows", "Q2", "Q3"],
          [["Billed revenue (the plausible wrong answer)", usd(wrong_total["Q2"]), usd(wrong_total["Q3"])],
           ["Amounts turned into blanks", f"{(dropped['quarter'] == 'Q2').sum()}", f"{(dropped['quarter'] == 'Q3').sum()}"]],
          caption="New York's claims, coerced")
print("The amounts coerce could not read:", ", ".join(dropped["billed_amount"]))
'''),
    md("""
    **What happened.** The answer is d. Six amounts are written as text with a dollar sign and
    cents, the way a spreadsheet prints currency, and coerce turned each into a blank: five in Q2 and
    one in Q3. The Q2 total comes out $668 short and Q3 $235 short.

    **Why it is wrong.** Nothing on the screen says anything was lost, so the finance head's books
    and this notebook would disagree by $903 with no row to point at, and the board's page would
    carry a number nobody can reconcile. The check that catches it counts the amounts that failed
    to convert, which must be zero before any total is read. **The fix.** Remove the dollar sign
    and any comma, then convert strictly, so an amount still unreadable stops the run with its row
    named instead of vanishing.
    """),
    code('''
claims["amount_usd"] = (claims["billed_amount"].str.replace("$", "", regex=False)
                        .str.replace(",", "", regex=False).astype(float))
right_total = claims.groupby("quarter")["amount_usd"].sum()
kit.table(["Billed revenue", "Q2", "Q3"],
          [["Coerced (wrong)", usd(wrong_total["Q2"]), usd(wrong_total["Q3"])],
           ["Every amount converted", usd(right_total["Q2"]), usd(right_total["Q3"])],
           ["What the blanks hid", usd(right_total["Q2"] - wrong_total["Q2"]), usd(right_total["Q3"] - wrong_total["Q3"])]],
          caption="New York's claims, the same rows summed two ways")
kit.check("no amount is left unconverted", claims["amount_usd"].notna().all(), f"{len(claims):,} amounts")
kit.check("the fix recovers exactly what coerce dropped",
          round(right_total.sum() - wrong_total.sum(), 2) == round(claims.loc[dropped.index, "amount_usd"].sum(), 2),
          usd(right_total.sum() - wrong_total.sum()))
'''),

    # ----------------------------------------------------------------- 4: reconcile
    md("""
    ## 4. Do the claims and the completed bookings describe the same visits, one to one?

    A booking ends completed or cancelled, and only a completed one is billed. If the two files
    describe the same visits, every completed booking has exactly one claim and no cancelled booking
    has one. Week 2 Tuesday's rule is that a join is counted before anything is summed, because a
    join can repeat rows it matches twice and the sum moves without a warning. A hurried analyst
    joins the raw export to the claims on `booking_id` and sums the amounts.

    **Predict before you run.** Joined on `booking_id` to the raw export, how many rows come back?
    a) 2,032, one per claim; b) 2,128, one per export row; c) more than 2,032 and fewer than 2,128;
    d) fewer than 2,032, since cancelled rows fall away.
    """),
    code('''
fanned = bookings.merge(claims, on="booking_id", suffixes=("", "_clm"))
fanned_q = fanned.groupby("quarter_clm")["amount_usd"].sum()
kit.table(["Joined on the raw export", "Rows", "Q2 billed", "Q3 billed", "Growth"],
          [["The plausible wrong answer", f"{len(fanned):,}", usd(fanned_q["Q2"]), usd(fanned_q["Q3"]),
            f"{fanned_q['Q3'] / fanned_q['Q2'] - 1:+.1%}"],
           ["The claims themselves", f"{len(claims):,}", usd(right_total["Q2"]), usd(right_total["Q3"]),
            f"{right_total['Q3'] / right_total['Q2'] - 1:+.1%}"]],
          caption="The same claims, joined to the export before the identity rule")
from pandas.errors import MergeError
try:
    bookings.merge(claims, on="booking_id", validate="one_to_one")
    refused = None
except MergeError as error:
    refused = str(error).splitlines()[0]
print("MergeError:", refused)
kit.check("a join that declares its grain refuses the raw export", refused is not None, refused)
'''),
    md("""
    **What happened.** The answer is c: 2,065 rows. Every repeated booking that was completed carries
    its claim twice, so the joined billed revenue reads $364,853 against $359,395 in the claims,
    $5,458 too much, $4,589 of it in Q2. New York's growth then reads 3.3 percent instead of 5.5.

    **Why it is wrong.** The join changed the grain, what one row stands for, from one row per claim
    to one row per export row without saying so, which is the Week 2 fan-out. The check that catches
    it is `validate="one_to_one"`, which refuses the join the moment either side repeats a key, and
    the cell above shows it refusing. **The fix.** Join the kept rows, with the grain declared, and
    keep both sides visible with an outer join, so a booking with no claim and a claim with no
    booking would each show up instead of vanishing. Then write the reconciliation as Week 1
    Wednesday's arithmetic: rows read equal rows kept plus rows set aside, all the way down to the
    claims.
    """),
    code('''
joined = clean.merge(claims, on="booking_id", how="outer", validate="one_to_one",
                     suffixes=("", "_clm"), indicator=True)
side = joined["_merge"].value_counts()
completed = clean[clean["status"] == "completed"]
cancelled = clean[clean["status"] == "cancelled"]
matched = joined[joined["_merge"] == "both"]
kit.table(["Step", "Rows"],
          [["Rows read from the old export", f"{len(bookings):,}"],
           ["Set aside by the identity rule", f"{set_aside}"],
           ["Bookings kept", f"{len(clean):,}"],
           ["of which cancelled, so no claim is expected", f"{len(cancelled)}"],
           ["of which completed", f"{len(completed):,}"],
           ["Completed bookings matched to one claim", f"{(matched['status'] == 'completed').sum():,}"],
           ["Claims with no booking in the export", f"{side.get('right_only', 0)}"],
           ["Cancelled bookings with a claim", f"{(matched['status'] == 'cancelled').sum()}"]],
          caption="New York, Q2 and Q3 together")
kit.bridge(("rows read", len(bookings)), [("set aside", -set_aside), ("cancelled", -len(cancelled))],
           end_label="completed = claims", fmt=lambda v: f"{v:,.0f}", lo=1800)
kit.check("rows read equal kept plus set aside", len(bookings) == len(clean) + set_aside)
kit.check("every completed booking has exactly one claim",
          (matched["status"] == "completed").sum() == len(completed) == len(claims),
          f"{len(completed):,} completed, {len(claims):,} claims")
kit.check("no claim lacks a booking, and no cancelled booking is billed",
          side.get("right_only", 0) == 0 and (matched["status"] == "cancelled").sum() == 0)
'''),

    # ----------------------------------------------------------------- 5: the tree
    md("""
    ## 5. Did more claims or a bigger mean claim carry the change, and does it hold per day?

    Week 1 Monday's revenue tree splits a total into branches that multiply back to it, each a count
    over a denominator. For a lab's billed revenue the first split is claims times the mean claim,
    where the mean claim is billed dollars over claims: a booking stands where an order stood, and a
    claim where a bill stood. Sections 2 to 4 proved that the claims are New York's completed
    bookings, one to one, so the claim count is a count of visits.

    **Predict before you run.** Which leaf moved New York's billed revenue from Q2 to Q3? a) more
    claims, at a lower mean claim; b) fewer claims, at a higher mean claim; c) more claims, at a
    higher mean claim; d) as many claims, at a higher mean claim.
    """),
    code('''
tree = claims.groupby("quarter")["amount_usd"].agg(["count", "sum", "mean", "median"])
q2, q3 = tree.loc["Q2"], tree.loc["Q3"]
kept_q = clean.groupby("quarter").size()
cancel_q = cancelled.groupby("quarter").size()
move = lambda a, b: f"{b / a - 1:+.1%}"
kit.table(["Leaf", "Q2", "Q3", "Change"],
          [["Billed revenue", usd(q2["sum"]), usd(q3["sum"]), move(q2["sum"], q3["sum"])],
           ["Claims (completed bookings)", f"{int(q2['count']):,}", f"{int(q3['count']):,}", move(q2["count"], q3["count"])],
           ["Mean claim", usd(q2["mean"], cents=True), usd(q3["mean"], cents=True), move(q2["mean"], q3["mean"])],
           ["Median claim", usd(q2["median"]), usd(q3["median"]), move(q2["median"], q3["median"])]],
          caption="New York, from the claims, after sections 2 to 4")
kit.driver_tree({"label": "Billed revenue", "note": f"{usd(q2['sum'])} to {usd(q3['sum'])}", "kind": "lit",
                 "children": [
                     {"label": "Claims", "note": f"{int(q2['count']):,} to {int(q3['count']):,}", "kind": "known",
                      "children": [{"label": "Bookings kept", "note": f"{kept_q['Q2']:,} to {kept_q['Q3']:,}", "kind": "known"},
                                   {"label": "less cancelled", "note": f"{cancel_q['Q2']} to {cancel_q['Q3']}", "kind": "known"}]},
                     {"label": "Mean claim", "note": f"{usd(q2['mean'], cents=True)} to {usd(q3['mean'], cents=True)}",
                      "kind": "known",
                      "children": [{"label": "What a claim holds", "note": "not opened in this build", "kind": "unknown"}]}]})
volume = (q3["count"] - q2["count"]) * q2["mean"]
value = q3["count"] * (q3["mean"] - q2["mean"])
kit.bridge(("Q2 billed", q2["sum"]), [("more claims", round(volume)), ("lower mean", round(value))],
           end_label="Q3 billed", lit=[0], lo=160000, fmt=lambda v: f"${v / 1000:,.1f}k")
kit.check("the two leaves add up to the change in billed revenue", round(volume + value) == round(q3["sum"] - q2["sum"]),
          f"{usd(volume)} and {usd(value)}")
kit.check("more claims and a lower mean, as predicted", q3["count"] > q2["count"] and q3["mean"] < q2["mean"])
'''),
    md("""
    **What happened.** The answer is a. Claims rose 8.0 percent, from 977 to 1,055, and the mean
    claim fell 2.3 percent, from $179.03 to $174.87, so billed revenue rose 5.5 percent, from
    $174,910 to $184,485. The bridge splits the $9,575 into its two leaves in tree order: the 78
    extra claims at Q2's mean add $13,964, and Q3's lower mean across all 1,055 claims takes away
    $4,389. The median claim stayed at $150, so the mean moved without a typical claim changing.

    **The plausible wrong answer.** "New York billed 8.0 percent more claims in Q3." It is true of
    the totals and wrong as a pace. Q2 runs 91 days and Q3 runs 92, so one extra day of work sits
    inside the 8.0 percent.

    **Predict before you run.** Per day, how much did New York's claims grow from Q2 to Q3? a) 8.0
    percent, the same as the totals; b) it fell, once Q3's extra day is taken out; c) about 6.8
    percent; d) about 9 percent.
    """),
    code('''
days = {"Q2": 91, "Q3": 92}
per_day = {q: (tree.loc[q, "count"] / days[q], tree.loc[q, "sum"] / days[q]) for q in days}
kit.table(["Per day", "Q2, 91 days", "Q3, 92 days", "Change"],
          [["Claims", f"{per_day['Q2'][0]:.2f}", f"{per_day['Q3'][0]:.2f}", move(per_day["Q2"][0], per_day["Q3"][0])],
           ["Billed revenue", usd(per_day["Q2"][1]), usd(per_day["Q3"][1]), move(per_day["Q2"][1], per_day["Q3"][1])]],
          caption="New York, the same totals over unequal quarters")
kit.check("the two quarters are different lengths, so totals are not a pace", days["Q2"] != days["Q3"], "91 and 92 days")
kit.check("per day, claims grow more slowly than the totals say",
          per_day["Q3"][0] / per_day["Q2"][0] < q3["count"] / q2["count"])
'''),
    md("""
    **What happened.** The answer is c. Per day, claims rose 6.8 percent and billed revenue 4.3
    percent, about 1.2 points below the totals. **Why it is wrong.** A pace compared with a plan set
    per month or per day is overstated by the extra day, and a claim that quotes totals has to say
    the windows differ; Week 1 Tuesday's like-with-like rung asks for the same weeks or a rate per
    day before any change is read. **The fix.** Quote the per-day change beside the totals, or
    quote the totals with the window lengths in the same sentence.
    """),

    # ----------------------------------------------------------------- 6: where, and where to stop
    md("""
    ## 6. Which New York site billed the extra claims, and where does this build stop?

    Every booking carries its `site_code`, and New York has three sites: KH-NYC-01, its laboratory,
    and two patient service centres, KH-NYC-02 and KH-NYC-03. Splitting the claims by site says where
    inside New York the extra claims were billed, which is a question about place; it cannot say why
    the mean claim fell.

    **Predict before you run.** Which New York site billed most of the 78 extra claims? a) KH-NYC-01,
    the laboratory, where samples are tested; b) KH-NYC-02, a patient service centre; c) KH-NYC-03,
    the other patient service centre; d) all three sites about equally.
    """),
    code('''
by_site = (clean.merge(claims, on="booking_id", validate="one_to_one", suffixes=("", "_clm"))
                .groupby(["site_code", "quarter_clm"])["amount_usd"].agg(["count", "sum"]))
sites = sorted(clean["site_code"].unique())
kit.columns(sites, [("Q2 claims", [by_site.loc[(c, "Q2"), "count"] for c in sites]),
                    ("Q3 claims", [by_site.loc[(c, "Q3"), "count"] for c in sites])], lit=[1],
            title="New York's claims by site, Q2 against Q3")
kit.table(["Site", "Q2 claims", "Q3 claims", "Change", "Q2 billed", "Q3 billed"],
          [[c, f"{by_site.loc[(c, 'Q2'), 'count']:,}", f"{by_site.loc[(c, 'Q3'), 'count']:,}",
            f"{by_site.loc[(c, 'Q3'), 'count'] - by_site.loc[(c, 'Q2'), 'count']:+,}",
            usd(by_site.loc[(c, "Q2"), "sum"]), usd(by_site.loc[(c, "Q3"), "sum"])] for c in sites],
          caption="New York by site, from the kept bookings joined to their claims")
kit.check("the sites add back to the metro, in claims and dollars",
          by_site["count"].sum() == len(claims) and round(by_site["sum"].sum(), 2) == round(claims["amount_usd"].sum(), 2),
          f"{by_site['count'].sum():,} claims, {usd(by_site['sum'].sum())}")
'''),
    md("""
    **What happened.** The answer is b. KH-NYC-02 billed 69 more claims, 296 to 365, KH-NYC-03
    billed 18 more, and the laboratory, KH-NYC-01, billed 9 fewer, so one patient service centre
    carried most of New York's growth in volume. **Where this build stops.** Below the mean claim sits what each claim
    holds, and why the mean fell is a question the claims alone cannot answer. It goes into the
    challenges log as an open question for the branch below, which this build does not open.
    """),

    # ----------------------------------------------------------------- 7: a second route
    md("""
    ## 7. Does SQL, run on the same raw files, reach the same claims and dollars?

    A second route earns its place only if it could fail where the first route is wrong. This one
    runs the whole build again in SQL, in SQLite, a database engine that ships inside Python, so the
    query runs with no server: Week 2 Wednesday's `ROW_NUMBER()` keeps one row per booking, Week 2
    Tuesday's join is made on the kept rows, and Week 2 Monday's tree is one `GROUP BY`. It shares
    no code with the pandas cells above. SQLite turns text it cannot read into 0 without a word, the
    same silence as coerce, so the query strips the dollar sign before the cast and a check counts
    any amount still holding something other than digits and a point.
    """),
    code('''
import sqlite3

con = sqlite3.connect(":memory:")
bookings.drop(columns=["quarter"]).to_sql("bookings", con, index=False)
claims[["claim_id", "booking_id", "service_date", "billed_amount"]].to_sql("claims", con, index=False)
query = """
WITH ranked AS (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY booking_id ORDER BY updated_at DESC) AS n FROM bookings),
kept AS (SELECT * FROM ranked WHERE n = 1 AND status = 'completed')
SELECT CASE WHEN c.service_date < '2026-07-01' THEN 'Q2' ELSE 'Q3' END AS quarter,
       COUNT(*) AS claims,
       ROUND(SUM(CAST(REPLACE(REPLACE(c.billed_amount, '$', ''), ',', '') AS REAL)), 2) AS billed
FROM kept JOIN claims c ON c.booking_id = kept.booking_id
GROUP BY quarter ORDER BY quarter"""
sql_tree = pd.read_sql_query(query, con).set_index("quarter")
unreadable = con.execute("""SELECT COUNT(*) FROM claims
    WHERE REPLACE(REPLACE(REPLACE(billed_amount, '$', ''), ',', ''), '.', '') GLOB '*[^0-9]*'""").fetchone()[0]
kit.table(["Route", "Q2 claims", "Q3 claims", "Q2 billed", "Q3 billed"],
          [["pandas, sections 2 to 5", f"{int(q2['count']):,}", f"{int(q3['count']):,}", usd(q2["sum"]), usd(q3["sum"])],
           ["SQL in SQLite", f"{sql_tree.loc['Q2', 'claims']:,}", f"{sql_tree.loc['Q3', 'claims']:,}",
            usd(sql_tree.loc["Q2", "billed"]), usd(sql_tree.loc["Q3", "billed"])]],
          caption="Two routes from the same raw files")
kit.check("no amount reaches the SQL cast still holding text", unreadable == 0, f"{unreadable} unreadable")
kit.check("SQL and pandas agree on the claims in each quarter",
          sql_tree["claims"].tolist() == [int(q2["count"]), int(q3["count"])])
kit.check("SQL and pandas agree on billed revenue to the cent",
          sql_tree["billed"].round(2).tolist() == [round(q2["sum"], 2), round(q3["sum"], 2)])
'''),
    md("""
    **What happened.** Both routes land on 977 and 1,055 claims and on $174,910 and $184,485, to the
    cent. The SQL route chose the kept row with its own rule, converted the amounts with its own
    code and joined with its own engine, so an error in the pandas cells would have shown here as a
    gap. **When to switch.** On the warehouse in Week 2 the SQL route was the first route, since
    Finance's number belongs where Finance can rerun it; on two CSV files and an hour of build time,
    pandas leads and SQL checks.
    """),

    # ----------------------------------------------------------------- 8: the claim
    md("""
    ## 8. What sentence can the finance head carry, with its denominators, its period and its caveat?

    Week 1 Thursday's note runs claim, evidence, caveat, action, claim first, because a reader with
    two minutes reads the first line and stops. The claim carries its number, its denominators (the
    claims in each quarter), its period (Q2 against Q3) and its reason; the caveat goes on its own
    line below and is never folded into the claim.

    | Part | New York, Q2 against Q3 |
    |---|---|
    | **Claim** | New York's billed revenue rose 5.5 percent, from $174,910 on 977 claims in Q2 to $184,485 on 1,055 claims in Q3, because it billed 78 more claims at a mean claim $4.16 lower. |
    | **Evidence** | The old export's 2,128 New York rows are 2,095 bookings under one identity rule; the 2,032 completed bookings match the 2,032 claims one to one; every amount converts; SQL on the raw files reaches the same claims and dollars; the bridge splits the $9,575 into $13,964 from more claims and minus $4,389 from the lower mean. |
    | **Caveat** | Billed revenue is list price, and the payers pay a contracted share of it, so this is not money collected; Q3 has 92 days to Q2's 91, so per day billed revenue rose 4.3 percent. Why the mean claim fell is not yet known. |
    | **Action** | Report New York as growing on claim volume, and open the branch below the mean claim before calling the lower mean a price or a mix change. |

    A listed lab writes growth the same way. Quest Diagnostics' annual report for 2025 gives net
    revenues of $11,035 million against $9,872 million for 2024 and says they "increased by 11.8%
    compared to the prior year", with the period and both bases on the page. Its revenue is an
    estimate that includes "the impact of contractual allowances (including payer denials), and
    patient price concessions", so what a US lab reports as revenue is what it expects to collect,
    below its list-price charges, and that is why New York's claim says billed.

    The decisions log follows the Week 1 Wednesday shape, one row per decision, and it includes a
    row that was kept as it was.
    """),
    code('''
kit.table(["Field", "Issue", "Rows", "Decision", "Reason"],
          [["booking_id", "33 ids appear on two rows", "33", "Keep the row with the later updated_at",
            "One id is one booking; 26 pairs are identical and 7 differ only in updated_at, so no booking fact is lost"],
           ["billed_amount", "6 amounts written as text with a dollar sign", "6", "Remove the dollar sign and any comma, convert strictly",
            "Coerce would blank them and leave billed revenue $903 short with no error"],
           ["channel", "Blank on 43 rows", "43", "Kept as they are",
            "This tree splits by site, so the blanks change no number here; logged for any split by channel"],
           ["status", "63 cancelled bookings carry no claim", "63", "Kept, outside billed revenue",
            "A cancelled booking is a real booking that bills nothing; the reconciliation shows each one"]],
          caption="The decisions log for the New York build")
kit.vflow([f"Billed revenue\\n{usd(q2['sum'])} to {usd(q3['sum'])}, +5.5%",
           f"Claims x mean claim\\n977 to 1,055 claims, {usd(q2['mean'], cents=True)} to {usd(q3['mean'], cents=True)}",
           "What a claim holds\\nthe next branch, not opened here"],
          kinds=["lit", "known", "unknown"])
'''),
    md("""
    > **Kavya's review.** "I want the count you started from, every row you set aside with its
    > reason, and a second way to the same total. You have 2,128 rows read, 33 set aside and 63
    > cancelled, and SQL lands on the same 2,032 claims and $359,395. Now tell me why the mean fell
    > before anyone calls it price."

    ### In the interview: how do you reconcile two systems' ids, and how do you say a finding in one sentence?

    **[F] Two systems export the same entity with different id formats; how do you reconcile them?**
    "I profile both keys before any join: the shapes each system writes and how many rows carry
    each, because a shape I have not counted is a shape my rule will miss. Then I write one rule
    that maps every shape to one canonical key and apply it to both sides, leaving both exports
    untouched. I prove the rule on the rows: the match count before and after, an anti-join in both
    directions, and every leftover classified as a real gap or a defect in the rule. On the way I
    check the grain, so a key repeated on one side cannot double a total, and the rule goes in the
    decisions log so the finance team can rerun it. Sometimes no rule exists: Kalpa Retail's
    campaign platform keyed its August list C-6000 to C-6159 and Finance's order file keyed its
    customers C-2000 to C-5003, so a profile of the two keys shows two populations, and no rule
    can make them match."
    Here the booking system and the billing system happened to write `booking_id` the same way, and
    the proof was the same: one to one, both directions, every leftover named.

    **[D] State your finding in one sentence a COO can carry into a board meeting.** "New York's
    billed revenue rose 5.5 percent, from $174,910 on 977 claims in Q2 to $184,485 on 1,055 in Q3,
    because it billed more claims at a slightly lower mean." Then the caveat, alone on the next
    line: billed is not collected, and per day the rise is 4.3 percent. The number, both bases, the
    period and the reason sit in one sentence, and nothing in it needs a chart to be understood.

    ### Depth: does the bridge's split depend on which leaf moves first?

    It does. In tree order, the volume leaf is priced at Q2's mean and the mean leaf is counted on
    Q3's claims: $13,964 and minus $4,389. Reversed, the extra 78 claims are priced at Q3's lower
    mean, $13,640, and the mean's fall is counted on Q2's 977 claims, minus $4,065. Both orders add
    to $9,575, and the $324 between them is the joint part, the change that exists only because both
    leaves moved at once. The symmetric split gives each leaf half of it: $13,802 and minus $4,227.
    Week 1 Tuesday chose the tree order and stated it, since a report that does not state its order
    leaves $324 of the split unexplained.
    """),
    md("""
    ## So did New York's billed revenue grow from Q2 to Q3, and did more claims or bigger claims carry it?

    1. Option C, the tree after reconciling, because the claims (up 8.0 percent) and the export's
       rows (up 4.8 percent) disagree and only a reconciliation can say which counts New York's
       volume; it reads 4,160 rows against 2,032.
    2. The export holds 2,095 bookings in 2,128 rows: 33 ids appear twice, 26 of the extra rows in
       Q2, so bookings grew 6.8 percent where rows grew 4.8.
    3. Six amounts were dollar text, and coerce left billed revenue $903 short, $668 in Q2 and $235
       in Q3; removing the dollar sign and converting strictly recovers every dollar.
    4. Yes: 2,095 bookings are 2,032 completed and 63 cancelled, and the 2,032 completed match
       2,032 claims one to one; the raw join fans out to 2,065 rows and $5,458 too much.
    5. More claims at a lower mean: claims up 8.0 percent and the mean claim down 2.3 percent, so
       $13,964 more from volume and $4,389 less from the mean; per day, claims rose 6.8 percent and
       billed revenue 4.3.
    6. KH-NYC-02, a patient service centre, billed 69 of the extra claims, and the build stops at
       what a claim holds, with why the mean fell logged as an open question.
    7. Yes: SQL in SQLite reaches 977 and 1,055 claims and $174,910 and $184,485, to the cent.
    8. "New York's billed revenue rose 5.5 percent, from $174,910 on 977 claims in Q2 to $184,485
       on 1,055 claims in Q3, because it billed 78 more claims at a mean claim $4.16 lower", with
       the caveat on its own line: billed is not collected, and per day the rise is 4.3 percent.

    New York's billed revenue grew 5.5 percent, $9,575, and more claims carried it: 78 more claims
    added $13,964 while a mean claim $4.16 lower took $4,389 away.
    """),
    code('''
kit.check_summary()
print("Next: your group's own question, run through the same moves, with its claim ready for the close.")
'''),
]

if __name__ == "__main__":
    build(OUT, cells, timeout=300)
    print(f"wrote and executed {OUT.relative_to(ROOT)}")

# Test inputs and expected outcomes
# --------------------------------
# python3 content/W03/D3/internal/C2_W03_D03_build_parallel_build_INTERNAL.py
#     Writes the notebook in parallel-build/ executed, with every check passing, and prints its path.
# python3 scripts/nb_check.py content/W03/D3
#     PASS: every code cell carries an output, at least three diagrams and five checks, none failing.
# The Kalpa Health files regenerated with a changed seed
#     The narrative numbers in the markdown no longer match the outputs; a check may fail, and the
#     markdown is updated from internal/C2_W03_D03_numbers_INTERNAL.py before the rebuild.
