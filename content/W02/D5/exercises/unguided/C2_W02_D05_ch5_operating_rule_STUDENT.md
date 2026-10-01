# Which of the week's steps belong in the workbook, which must never be done there, and how do the two stay in step?

Chapter 5 set, six items, after chapter 5: items 1 and 2 run live in the chapter's last three
minutes; the rest are the practice lab's stretch or tonight's work.

> "Everything you built this week has to survive a room that only has Excel. Which parts belong in
> Excel, which parts must never be in Excel, and how do you keep the two from drifting apart?"
>
> Kavya Nair, senior analyst, Kalpa Retail data team

This week the team answered Kalpa Retail's questions in three tools. On Monday and Tuesday it queried
the warehouse, the Postgres database that holds one row per order and one row per payment and is the
source of truth; Tuesday's report set booked revenue, the value of the orders, against collected
revenue, the money received against them, which needs a join, a query that matches each order with
every payment made against it. On Thursday it built one row per customer in pandas, the Python
library for tables, and today it presents in an Excel workbook. SUMIFS adds every row that matches its
conditions. A drift check on the workbook's Checks tab compares the sheet's own totals, live, with the
warehouse's control totals, such as orders and booked revenue per quarter, which travel on a small
tab beside each export, since a workbook with no login cannot query the warehouse. Anand Iyer is Kalpa
Retail's finance controller.

**Who needs the answer.** Kavya signs the team's operating rule, Anand's analyst audits every number
Finance relies on, and the data platform lead owns the warehouse. A step done in the wrong tool ships
a number nobody can rerun, and a join done in a sheet can report money that customers have paid as
money they owe.

**The questions on the way.**

- What happened when a lookup put collected at Rs 11.84 crore against Rs 19.84 crore booked?
- What does a lookup say is outstanding on four invented orders, and what is?
- Which arrangement fits the booked-against-collected report Anand signs every month?
- Which of three standing arrangements break the team's rule?
- What does the drift check do when the workbook's Q2 falls short of the warehouse's?
- Which route can disagree with each of two workbook figures when the figure is wrong?

Items 2 and 5 use invented figures; the other items use Kalpa's own week.

Post one line of six letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxxxx
```

---

### Q1. What happened when a lookup put collected at Rs 11.84 crore against Rs 19.84 crore booked?

To show collected in the workbook without a login, a hurried analyst fills a lookup beside each of
Kalpa's 1,000 orders, `=VLOOKUP(A2, RawExport!A:H, 7, FALSE)`, an exact match on the order id that
fetches paid_amount from the raw export, which holds one row per payment. Added up, collected reads
Rs 11.84 crore against Rs 19.84 crore booked. What happened?

a) The unpaid orders have no payment row, so they pulled the total down
b) It took the first payment of each order and ignored any second one
c) The exact match failed on half the ids, which then returned zero
d) The refunds were netted off the payments before the export was sent

### Q2. What does a lookup say is outstanding on four invented orders, and what is?

Four invented orders: Rs 10,000, paid in two instalments of Rs 5,000; Rs 6,000, paid once; Rs 4,000,
paid in two instalments of Rs 2,000; and Rs 2,000, not yet paid. A lookup on the order id fetches
paid_amount for each order from the payment rows, and IFERROR turns the unpaid order's #N/A into
zero. Outstanding is booked less collected. What does the lookup say is outstanding, and what is?

a) Rs 9,000 by the lookup, and Rs 2,000 in truth
b) Rs 2,000 by the lookup, and Rs 2,000 in truth
c) Rs 13,000 by the lookup, and Rs 20,000 in truth
d) Rs 9,000 by the lookup, and Rs 9,000 in truth

### Q3. Which arrangement fits the booked-against-collected report Anand signs every month?

Anand signs the report every month, and his analyst reruns any number before relying on it. The
payment export arrives each month, and the workbook that carries the figure to the deck has no login
to the warehouse. Which arrangement fits?

a) A SUMIFS per order in the workbook over each month's payment export, refreshed by hand
b) The join in the warehouse, and the workbook shows its total with no check beside it
c) A notebook that runs the join and pastes the figure in as a value
d) The join in the warehouse, with a SUMIFS in the workbook as a check on it

### Q4. Which of three standing arrangements break the team's rule?

The team's rule gives the warehouse every join, dedupe and rank that Finance relies on, gives pandas
the analyst's iteration until Finance relies on it, and gives the workbook the last mile on an export
that ties. Three arrangements the team could keep from next month:

| Arrangement | How often | What it does |
|---|---|---|
| 1 | Every week | The first-row flag in the workbook counts each order once in the payment export, about 145,000 rows next quarter, and the growth review's revenue, which must equal Finance's, is built on it |
| 2 | Once, for this afternoon's meeting | A pivot on the protect list, which already ties, counts its fifty members by city, and nobody keeps it |
| 3 | Every month | A SUMIFS per order in the workbook adds every payment for the collected figure Anand signs |

Which of them break the rule?

a) Only 3, since the flag ties to the warehouse to the rupee every week
b) 1 and 3, since each cleans or joins the rows a Finance number rests on
c) All three, since none of them has a query in the warehouse behind it
d) 2 and 3, since nothing ties the protect list's city count to the warehouse

### Q5. What does the drift check do when the workbook's Q2 falls short of the warehouse's?

On an invented Monday, the workbook's own Q2 total reads Rs 9.79 crore, and the warehouse's control
total on the tab beside the export reads Rs 9.84 crore. Every row in the workbook's export is a real
order. What does the drift check do?

a) Holds the deck until someone knows why, and asks for a fresh export
b) Ships the deck with a footnote that the export may be incomplete
c) Passes, since Rs 5 lakh is about half a percent of Q2, inside rounding
d) Ships the deck, since every row in the export is a real order

### Q6. Which route can disagree with each of two workbook figures when the figure is wrong?

The workbook shows two figures, and a second route for each has to share none of its steps, so that
it can disagree when the figure is wrong.

| Figure | What it is | How the workbook reaches it |
|---|---|---|
| 1 | Collected, Rs 19,66,45,070 | Every payment added once, after the gateway's 50 copies of a payment are dropped |
| 2 | Booked revenue in Q2, Rs 9,84,00,000 | The flagged rows of the payment export, each order once, summed for Q2 |

The warehouse's payments table holds every payment as the gateway posted it, so the 50 double posts
sit there too. Four routes are on offer:

| Route | What it does |
|---|---|
| P | Booked revenue less the orders that have no payment at all, found in the warehouse with NOT EXISTS |
| Q | The warehouse's payments table joined to its orders and summed |
| R | The warehouse's orders table summed by quarter |
| S | The flagged rows pivoted again, with segment in Columns |

Which pairing gives each figure a route that can disagree with it?

a) Figure 1 with Q, and figure 2 with R
b) Figure 1 with P, and figure 2 with S
c) Figure 1 with P, and figure 2 with R
d) Figure 1 with Q, and figure 2 with S
