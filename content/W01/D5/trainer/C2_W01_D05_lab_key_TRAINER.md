# Lab key: every number a correct run reaches, and every trap with its wrong number

**TRAINER ONLY.** The data is `v3-lab`, **proposed for client zero v2.3** (tracker v7, 21 September
2026) and not yet locked. Every number below is printed by
`trainer/C2_W01_D05_lab_reference_TRAINER.ipynb`; if the lock changes the data, rerun that notebook
and this page follows it.

Regenerate the data with:

```
python3 data/generate_client_zero.py --version v3-lab --out content/W01/D5/data --stem C2_W01_D05
```

## What is planted, and what the room should find

No learner file names any of this. The debrief shows each mechanism on invented numbers and reruns
the real one live from the reference notebook.

| Planted | Where it sits | What a correct run does | If nobody finds it by the 65-minute mark |
|---|---|---|---|
| A September batch posted twice: 10 exact repeat rows | Q2 only: 9 Retail-Core orders dated 2 to 10 September (between KR-07169 and KR-07179, Rs 15,410 in all) and the corporate order KR-07143 of Rs 13,20,000, inserted as a block after the originals | Profile shows 207 rows and 197 distinct ids; identity rule on order_id; 10 dropped with a reason | Nothing during the lab; the observation sheet records it and the debrief opens on it |
| One amount stored as text, "9,85,000" | KR-07073, a Q1 corporate order, customer C-7302 | Converted by removing the grouping commas, kept, flagged in the log | Nothing during the lab |
| One empty segment | KR-07146, a Q2 order of Rs 2,930, customer C-7101, whose other orders are all Retail-Plus | Restored to Retail-Plus from the customer's other orders and flagged, or kept as a flagged unknown with the segment sums reconciled | Nothing during the lab |
| Business on six orders then four | 5 corporate customers; Rs 58,50,000 then Rs 41,40,000 | Named with its count, kept in the caveat, never the headline | Nothing during the lab |

The clean data's finding is a branch the week never showed: customers flat, frequency flat, and
Retail-Core's revenue per order down 17.1 percent.

## The numbers a correct run reaches

### Profile

| Field | Present | Convertible | Distinct |
|---|---|---|---|
| order_id | 207 | | 197 |
| customer_id | 207 | | 67 |
| segment | 206 | | 4 |
| channel | 207 | | 3 |
| city | 207 | | 5 |
| order_date | 207 | | 118 |
| quarter | 207 | | 2 |
| amount | 207 | 206 | 145 |

Typical order on the rows that convert, repeats still in: median Rs 2,110 against a mean of
Rs 52,057. On the clean data: median Rs 2,120, mean Rs 52,657.

### Clean and reconcile

| Measure | Value |
|---|---|
| Input rows | 207 |
| Clean orders | 197 (98 in Q1, 99 in Q2) |
| Rejected | 10, every one a field-for-field repeat of an order kept |
| Converted and flagged | 1 (the text amount, Rs 9,85,000) |
| Defaulted and flagged | 1 (the empty segment, to Retail-Plus) |
| Q1 clean against control | Rs 60,48,000 against Rs 60,48,000, 98 orders against 98 |
| Q2 clean against control | Rs 43,25,480 against Rs 43,25,480, 99 orders against 99 |
| The bridge | Rs 1,07,23,890 summed as read, less Rs 13,35,410 of repeats, plus Rs 9,85,000 recovered from text, lands on Rs 1,03,73,480 |

### The tree, Q1 against Q2, clean

| Segment | Customers | Orders per customer | Revenue per order | Revenue | Orders |
|---|---|---|---|---|---|
| Retail-Core | 30 / 30 | 1.47 / 1.47 | Rs 2,050 / Rs 1,700 | Rs 90,200 / Rs 74,800, -17.1% | 44 / 44 |
| Retail-Plus | 20 / 20 | 1.70 / 1.75 | Rs 2,800 / Rs 2,760 | Rs 95,200 / Rs 96,600, +1.5% | 34 / 35 |
| Student | 12 / 12 | 1.17 / 1.33 | Rs 900 / Rs 880 | Rs 12,600 / Rs 14,080, +11.7% | 14 / 16 |
| Business | 5 / 4 | 1.20 / 1.00 | Rs 9,75,000 / Rs 10,35,000 | Rs 58,50,000 / Rs 41,40,000, -29.2% | 6 / 4 |
| All | 67 / 66 | | | Rs 60,48,000 / Rs 43,25,480, -28.5% | 98 / 99 |

The fall is Rs 17,22,520, and Business carries Rs 17,10,000 of it (99.3 percent), on two fewer
orders; the corporate basket rose. Among consumers the one branch that moved is Retail-Core's
revenue per order.

### The shuffle

The gap: Retail-Core's change in revenue per order (-17.1 percent) less Retail-Plus's (-1.4
percent), -15.6 points. Segment labels shuffled across the 50 customers, 2,000 times,
`random.Random(7)`: 39 shuffles as extreme, **p = 0.0195**. Twenty other seeds give p from 0.0145
to 0.0270, so any correct run lands between about 0.013 and 0.027 and the verdict does not move.

A learner who tests a different gap is not wrong to do so: accept Retail-Core against all other
consumers, or Retail-Core Q1 against Q2 on revenue per order with the quarter label shuffled across
orders, if the unit is argued. A learner who tests Business has met the too-few-orders trap; record
it.

### The note, as a correct run writes it

**Claim.** From Q1 to Q2 booked revenue fell 28.5 percent, from Rs 60,48,000 to Rs 43,25,480, and
Rs 17,10,000 of the Rs 17,22,520 fall is two fewer corporate orders; among consumers the one branch
that moved is Retail-Core's revenue per order, down 17.1 percent from Rs 2,050 to Rs 1,700, with its
30 customers and 1.47 orders each unchanged.
**Evidence.** 197 distinct orders reconcile to Finance's control totals in both quarters after
dropping 10 rows posted twice and converting one amount stored as text; the Retail-Core gap against
Retail-Plus beat 39 of 2,000 customer-level shuffles, p = 0.02.
**Caveat.** The corporate fall rests on six orders against four, too few to call a trend, and one
Q2 order's segment was restored from the customer's other orders.
**Action.** Open Retail-Core's basket first, items per order and price per item, before any spend;
treat the corporate fall as noise until a third quarter says otherwise.

## The traps a hurried run falls into, each with its exact wrong number

| # | Trap | The wrong number, exactly | The right number | The decision it would have misled | The check that catches it |
|---|---|---|---|---|---|
| 1 | **The reconciliation skipped**, the one most rooms fall into | Q1 Rs 50,63,000, Q2 Rs 56,60,890: **Q2 up 11.8 percent** | Q2 down 28.5 percent | "Q2 grew, nothing to investigate" goes to Meera | Input 207 against clean plus rejected; each quarter's rupees against the control total |
| 1a | Half of it: repeats kept, text read correctly | Q2 Rs 56,60,890: **down 6.4 percent** | down 28.5 | "A mild dip, the usual wobble" | Distinct ids against rows |
| 1b | The other half: repeats removed, text set to zero | Q1 Rs 50,63,000: **down 14.6 percent** | down 28.5 | The size of the fall halved | Q1 rupees against the control total |
| 2 | **The pass that looks clean**: the text amount coerced to zero | 0 rejects, 98 Q1 orders that reconcile, **Q1 Rs 50,63,000** | Rs 60,48,000 | Counts reconcile, so the run is signed off | Rupees per quarter against the control total |
| 3 | **The wrong branch**: the tree read on the uncleaned rows | Retail-Core **orders per customer 1.47 to 1.77, +20.5 percent**; revenue **Rs 90,200 to Rs 90,210, flat**; per order -17.0% | Frequency flat, basket -17.1 percent, revenue -17.1 percent | "Core is fine, its customers order more often" | Distinct ids per segment; reconcile before decomposing |
| 4 | **The headline on ten orders** | "Corporate revenue fell **29.2 percent**" as the first line | 6 orders then 4, in the caveat | Meera chases two invoices | Count before rate; fewer than about thirty observations |
| 5 | **The wrong unit** in the shuffle | Orders shuffled: 151 of 2,000, **p = 0.0755**, "could be chance" | Customers shuffled: p = 0.0195 | A real basket fall dismissed as noise | The unit that carries the label is the customer |
| 6 | **The typical order** | **Rs 52,057**, the mean, as the typical order | Rs 2,110, the median | A basket story told on an average that ten corporate orders set | Sort and read the top ten |
| 7 | **The empty segment dropped or bucketed** | Retail-Plus Q2 **34 orders, Rs 93,670**, and a fifth segment "" of 1 order, Rs 2,930 | 35 orders, Rs 96,600 | Segment sums short of the total by Rs 2,930 | Segments add back to the total, in orders and rupees |

Traps 1, 2 and 3 have the same root: a total used before it was reconciled. Trap 3 is the most
instructive to show, because the repeated batch did more than inflate a total: it manufactured a
frequency rise that hides the basket fall.

## A syntax or runtime error on the way

`ValueError: invalid literal for int() with base 10: '9,85,000'` is what most learners meet first,
and it is the only error the file forces. It gets its two minutes from the learner, never help from
a TA beyond "what does the last line say?". What the learner does next (convert, zero, skip or drop)
is what the observation sheet records.
