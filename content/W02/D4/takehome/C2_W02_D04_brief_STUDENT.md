# Can you build the Monday table on a staging snapshot you have not seen, and say what its feed did?

Tonight, about two hours, alone. Due before Friday's session opens; Friday starts by walking one
learner's answer to part 3. The self-check beside this brief lists the numbers you should reach;
open it only after your own notebook runs top to bottom.

> **The client asks.** "Before your refresh runs against the live warehouse on Monday, run it on my
> staging snapshot. It is a different draw of the same business: the customer list and the totals
> match what you had in class, but different customers placed the orders, on different dates, and
> the campaign feed is a different send. Tell me what your guards did, what the table says, and which
> win-back line you would give Marketing."
>
> The data platform lead, Kalpa Retail

The data platform lead owns Kalpa Retail's warehouse. A staging snapshot is a copy of the business's
data kept apart from the live warehouse, so a job can be tried on it before it runs for real. Some of
your answers from class carry over and most do not. These come out as they did in class: 340
customers in the same four segments, 1,000 orders worth Rs 19,84,00,000 up to 28 September 2026, a
smallest recency of 0, and the same count of orders in each segment and quarter, so Retail-Plus still
has 215 orders in Q1 and 140 in Q2. Every answer about particular customers comes out differently: who
never ordered, whom the sale reached and how many of them bought, the win-back lists, Retail-Plus
orders per member, and each tier's change in spend from Q1 to Q2, so a table that matches class on the
totals tells you nothing yet about its rows.

This snapshot holds three CSV files in this day's `data/` folder, with no Postgres of their own:

| File | What it holds |
|---|---|
| `C2_W02_D04_takehome_orders_STUDENT.csv` | Orders, one row each, from April to September 2026 |
| `C2_W02_D04_takehome_customers_STUDENT.csv` | The customer list, one row per customer, with each customer's segment |
| `C2_W02_D04_takehome_exposure_STUDENT.csv` | The campaign platform's feed of the customers the monsoon sale reached |

**The table you build.** One row for every customer on the list, with recency (the days from the last
order to the table's as-of date, the last date the data covers), frequency (the count of orders),
spend (the value of the orders at the prices charged), the segment, whether the sale reached the
customer, and the lapsed flag: no order in the 60 days to the as-of date. A customer the feed names
more than once was reached once, on the first date it gives; a customer who never ordered gets a
frequency and spend of 0 and is not lapsed. Q1 is April to June 2026 and Q2 is July to September.
Retail-Core and Retail-Plus are Kalpa Retail's two consumer tiers, and Retail-Plus is the paid
membership.

**The four guards.** Your refresh is one function that builds the table and raises an error, writing
nothing, when any of these fails: one row per customer; as many rows as the customer list; spend
equal to the total of the orders; and a smallest recency of 0, since somebody always bought on the
data's last day.

**Who needs the answer.** The data platform lead, who lets the refresh near the live warehouse only
after it has run cleanly on staging, and the growth team, who send Monday's codes from its output. The
lead asks what each guard did on staging, since a guard nobody has seen stop a run gives no evidence
that it can.

**The questions on the way.**

- Does your refresh pass its guards on the snapshot, and what did its first run say?
- What does the snapshot's table say, in eight numbers?
- Which win-back line would you give Marketing, at 45, 60 or 90 days, and why?
- Do pandas and plain Python agree on Retail-Plus orders per member?
- How far did Retail-Plus and Retail-Core spend move, and what does `"one_to_one"` promise?
- What do you read, watch, redo and recap once the notebook runs?

## Part 1. Does your refresh pass its guards on the snapshot, and what did its first run say?

Used at work every time a job meets a new copy of its data.

Thirty-five minutes. In a new notebook saved in this day's `notebooks/` folder, write the refresh
function to read the three CSVs with `pd.read_csv(..., parse_dates=[...])` and run it with every
guard in place. Paste the output of your first run exactly as it came out, whether a table or an
error. Then say what you changed and why, and paste the output of the run that passed. If your first
run passed, say so, and say which guard would have stopped a feed that broke its promise.

## Part 2. What does the snapshot's table say, in eight numbers?

Used at work whenever a table is handed over and its reader checks it before acting.

Twenty minutes. Report the rows, the spend, the as-of date, the smallest recency, the customers who
never ordered, the customers the sale reached and how many of them bought, and the 60-day win-back
list. Take every customer's segment from the customer list.

## Part 3. Which win-back line would you give Marketing, at 45, 60 or 90 days, and why?

Used at work whenever a threshold turns a number into an action that costs money.

Twenty-five minutes. Marketing will send a win-back discount to every customer past the line you
choose. Give the count at each of the three lines from the snapshot, choose one, and defend it in
three sentences: what the discount costs if it reaches customers who were coming back anyway, what it
costs if it misses customers who were leaving, and why your line is the trade you would sign. Put a
count from the snapshot in each of the three sentences, because Marketing weighs a line by how many
customers it sends the discount to.

## Part 4. Do pandas and plain Python agree on Retail-Plus orders per member?

Used at work whenever a number is checked by a route that shares no code with the first.

Twenty minutes. Orders per member is a quarter's orders over the Retail-Plus members who ordered in
that quarter. Compute it for Q1 and Q2 twice, once in pandas and once in plain Python with a loop and
a set, and paste both outputs. They must agree to three decimal places; if they did not at first, say
what was wrong.

## Part 5. How far did Retail-Plus and Retail-Core spend move, and what does `"one_to_one"` promise?

Used at work on every months view that reaches a review, and on every merge that runs unattended.

Twenty minutes. Build a months view for each of the two tiers, one row per member and one column per
month, with its `aggfunc` written out; check each view's grand total against that tier's orders; and
report each tier's change from Q1 to Q2. Then open the pandas reference for `DataFrame.merge`,
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html (verified 1 Oct 2026),
quote the line that says what `"one_to_one"` checks, and say in one sentence why your refresh uses it
rather than `"many_to_one"`.

## What do you read, watch, redo and recap once the notebook runs?

- Read pandas' own guide to grouping, split-apply-combine, at
  https://pandas.pydata.org/docs/user_guide/groupby.html (verified 1 Oct 2026), and then the merging
  guide's section "Merge key uniqueness", at
  https://pandas.pydata.org/docs/user_guide/merging.html (verified 1 Oct 2026).
- Watch Corey Schafer's "Python Pandas Tutorial (Part 8): Grouping and Aggregating - Analyzing and
  Exploring Your Data", at
  https://www.youtube.com/watch?v=txMdrV1Ut64 (title and channel checked 1 Oct 2026; its content not verified).
  pandas 3.0 came out in January 2026, so where a call in the video differs from today's notebooks,
  the notebooks are current.
- Redo the guided carve from chapter 1 on the snapshot, and compare its three numbers with part 2.
- Recap by writing the four guards from memory on a card, each with the failure it catches. Saturday's
  paper asks about the merge's own check, what `validate="one_to_one"` does when the feed names a
  customer twice.

## What do you hand in?

One notebook, run top to bottom from a fresh kernel, with parts 1 to 5 in order, the pasted outputs
in parts 1 and 4, and part 3's three sentences in a markdown cell. Bring the table your refresh wrote
as a CSV to Friday, beside the one from class.
