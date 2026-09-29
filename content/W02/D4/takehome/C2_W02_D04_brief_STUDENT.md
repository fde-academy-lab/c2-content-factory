# Take-home: the refresh, run on the staging snapshot

About two hours tonight. Friday opens by walking one learner's answer to Part 3.

> **The client's ask.** The data platform lead: "Before your refresh runs against the live
> warehouse on Monday, run it on my staging snapshot. It is a different draw of the same
> business, so your answers from class will not carry over. Tell me what your guards did, what
> the table says, and which win-back threshold you would give Marketing."

## The files

Three CSVs in `content/W02/D4/data/`, written by the programme's data generator:

| File | What it holds |
|---|---|
| `C2_W02_D04_takehome_orders_STUDENT.csv` | Orders, one row each, two quarters |
| `C2_W02_D04_takehome_customers_STUDENT.csv` | The customer list, one row per customer |
| `C2_W02_D04_takehome_exposure_STUDENT.csv` | The monsoon sale's exposure feed |

Read them with `pd.read_csv(..., parse_dates=[...])`; the snapshot has no Postgres of its own.

## Part 1. Run your refresh, and keep what it said (35 minutes)

Adapt `build_customer_table` from the escalated case to read the three CSVs, and run it on the
snapshot with every guard in place. **Paste the output of your first run exactly as it came
out**, whether it was a table or an error, then what you changed and why, then the output of
the run that passed. A first run that passed is fine; say so and say which guard would have
stopped a bad feed.

## Part 2. The table's numbers (20 minutes)

Report the row count, the spend total, the as-of date, the number of customers the sale reached
and how many of them bought, and the 60-day win-back list. Then check them against the
self-check file.

## Part 3. The threshold, defended (25 minutes)

Marketing will send a win-back discount to every customer past the threshold you choose: 45, 60
or 90 days. Give the count at each threshold from the snapshot, choose one, and defend it in
three sentences: what the discount costs if it reaches customers who were coming back anyway,
what it costs if it misses customers who were leaving, and why your threshold is the trade you
would sign. A choice with no number beside it does not count.

## Part 4. Two tools, actually run (20 minutes)

Compute Retail-Plus orders per member for Q1 and Q2 on the snapshot twice: once in pandas and
once in plain Python with a loop and a set. **Paste both outputs.** They must agree to three
places; if they did not at first, say what was wrong.

## Part 5. The months view and one line from the source (20 minutes)

Build the Retail-Plus and Retail-Core months views with `aggfunc="sum"`, check each grand total
against its orders, and report each segment's change from Q1 to Q2. Then open the pandas
reference for `DataFrame.merge` (verified 29 September 2026):
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html
Quote the line that says what `"one_to_one"` checks, and say in one sentence why your function
uses it rather than `"many_to_one"`.

## What you hand in

One notebook, run top to bottom from a fresh kernel, with Parts 1 to 5 in order, the pasted
outputs in Parts 1 and 4, and the three sentences of Part 3 in a markdown cell.
