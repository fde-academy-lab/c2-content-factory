# What does a correct run of the lab reach, and what wrong number does each trap print?

**TRAINER ONLY.** The data is `v3-lab`, **proposed for client zero v2.3** (tracker v7, 21 September
2026) and not yet locked. Every number below is printed by
`trainer/C2_W01_D05_lab_reference_TRAINER.ipynb`; if the lock changes the data, rerun that notebook
and bring this page into line with it.

**Who needs the answer.** The trainer, who says this morning's numbers aloud at the debrief, and the
TAs, who read a learner's screen during the lab and name each stall on the observation sheet. A
number misremembered here becomes a wrong correction to a learner.

Regenerate the data with:

```
python3 data/generate_client_zero.py --version v3-lab --out content/W01/D5/data --stem C2_W01_D05
```

## What is planted, and what should the room find?

No learner file names any of these records or their values or carries a number computed from this
export. The debrief deck, the study notes and the debrief's three chapter notebooks
(`notebooks/C2_W01_D05_01_debrief_quarters_STUDENT.ipynb`, `02_debrief_values`,
`03_debrief_segments`, named so a folder listing names no trap) show every trap on an invented export,
built by `internal/C2_W01_D05_invented_export_INTERNAL.py` into
`data/C2_W01_D05_invented_orders_STUDENT.csv` and labelled invented. The notebooks' empty your-turn
cells run each step on this export once a learner types them after the lab; the values the trainer
says aloud are in the day sheet's said-aloud table.

| Planted | Where it sits | What a correct run does | If nobody finds it by the 65-minute mark |
|---|---|---|---|
| A batch posted twice: 10 exact repeat rows | Q2 only: 9 Retail-Core orders dated 2 to 10 September (between KR-07169 and KR-07179, Rs 15,410 in all) and the corporate order KR-07143 of Rs 13,20,000 dated 7 August, inserted as a block after the originals | The profile shows 207 rows and 197 distinct ids, the identity rule is order_id, and the 10 repeats are dropped with a reason | Nothing during the lab; the observation sheet records it and the debrief opens on it |
| One amount stored as text, "9,85,000" | KR-07073, a Q1 corporate order, customer C-7302 | It is converted by removing the grouping commas, then kept and flagged in the log | Nothing during the lab |
| One empty segment | KR-07146, a Q2 order of Rs 2,930, customer C-7101, whose other orders are all Retail-Plus | Restored to Retail-Plus from the customer's other orders and flagged, or kept as a flagged unknown with the segment sums reconciled; both are correct, and their numbers are below | Nothing during the lab |
| Business on six orders then four | 5 corporate customers; Rs 58,50,000 then Rs 41,40,000; C-7304 ordered once in Q1 and not in Q2, and C-7300 ordered twice in Q1 and once in Q2 | It is named with its count and kept in the caveat, out of the headline | Nothing during the lab |

The clean data's finding is a branch the week never showed: customers flat, frequency flat, and
Retail-Core's revenue per order down 17.1 percent.

## Which numbers does a correct run reach?

### What does the profile show?

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

On the rows that convert, with the repeats still in, the typical order is the median of Rs 2,110,
against a mean of Rs 52,057; on the clean data the median is Rs 2,120 and the mean Rs 52,657.

### What do cleaning and the reconciliation reach?

| Measure | Value |
|---|---|
| Input rows | 207 |
| Clean orders | 197 (98 in Q1, 99 in Q2) |
| Rejected | 10, every one a field-for-field repeat of an order kept |
| Converted and flagged | 1 (the text amount, Rs 9,85,000) |
| Defaulted and flagged | 1 (the empty segment, to Retail-Plus), or kept as a flagged unknown |
| Q1 clean against control | Rs 60,48,000 against Rs 60,48,000, 98 orders against 98 |
| Q2 clean against control | Rs 43,25,480 against Rs 43,25,480, 99 orders against 99 |
| The bridge | Rs 1,07,23,890 summed as read, less Rs 13,35,410 of repeats, plus Rs 9,85,000 recovered from text, lands on Rs 1,03,73,480 |
| The second route | The set-aside rows summed come to Rs 13,35,410 and the log's read-back value to Rs 9,85,000, each equal to its move in the bridge |

### What does the clean tree show, Q1 against Q2?

| Segment | Customers | Orders per customer | Revenue per order | Revenue | Orders |
|---|---|---|---|---|---|
| Retail-Core | 30 / 30 | 1.47 / 1.47 | Rs 2,050 / Rs 1,700 | Rs 90,200 / Rs 74,800, -17.1% | 44 / 44 |
| Retail-Plus | 20 / 20 | 1.70 / 1.75 | Rs 2,800 / Rs 2,760 | Rs 95,200 / Rs 96,600, +1.5% | 34 / 35 |
| Student | 12 / 12 | 1.17 / 1.33 | Rs 900 / Rs 880 | Rs 12,600 / Rs 14,080, +11.7% | 14 / 16 |
| Business | 5 / 4 | 1.20 / 1.00 | Rs 9,75,000 / Rs 10,35,000 | Rs 58,50,000 / Rs 41,40,000, -29.2% | 6 / 4 |
| All | 67 / 66 | | | Rs 60,48,000 / Rs 43,25,480, -28.5% | 98 / 99 |

With the empty-segment order kept as a flagged unknown instead of restored, Retail-Plus reads Q2 34
orders and Rs 93,670, -1.6 percent, and a fifth group, segment unknown, holds 1 order of Rs 2,930;
the five groups add back to the quarter. That run is correct as well, because the unknown is named,
flagged and reconciled. Every Retail-Core number is the same under either handling.

The fall is Rs 17,22,520, and Business carries Rs 17,10,000 of it (99.3 percent), on two fewer
orders; the corporate basket rose. Among consumers the one branch that moved is Retail-Core's
revenue per order.

### Which routes can a correct run take to the test, and what does each give?

The note's claim is about the same 30 Retail-Core customers in two quarters, so the fair test for it
keeps each customer's own two quarters together and flips them at random: the paired test, with
Retail-Core's revenue per order recomputed in every world. The direction was chosen after the data
was seen, so the note reports both directions; the one-way share is listed only so a TA recognises it
on a screen. Every route is 2,000 runs on `random.Random(7)` unless the row says otherwise.

| Route | The question it answers | Fair? | p, both ways | p, one way |
|---|---|---|---|---|
| Each Retail-Core customer's two quarters flipped, revenue per order | Did Retail-Core's basket fall? | Yes: the note's test | **0.006** (12 of 2,000); 0.0042 at 20,000; 0.0035 exact over all 2^30 flips | 0.001 |
| The same flips, revenue per customer | Did Retail-Core's customers spend less? | Yes | 0.0015 | |
| Sign test, 21 fell and 9 rose | Did most customers' baskets fall? | Yes: the second route | 0.043, exact | |
| Segment label shuffled across the 50 Retail-Core and Retail-Plus customers, each carrying all their orders | Did Retail-Core's basket move differently from Retail-Plus's? | Yes: the key's between-segment design | 0.0195 (39 of 2,000; gap -15.6 points) | 0.012 |
| The same, with the empty-segment order kept as a flagged unknown | The same | Yes | 0.0230 (gap -15.5 points) | 0.014 |
| Segment label shuffled across Retail-Core and every other consumer customer | Did Retail-Core move differently from the rest? | Yes | 0.0345 (gap -13.7 points) | 0.018 |
| Each customer's Q1 and Q2 revenue pooled, quarter labels dealt at random | Did Retail-Core's customers spend less? | No: it pools paired data, trap 5b | 0.0765 | 0.0325 |
| Retail-Core's 88 orders from both quarters pooled, the quarter label dealt across single orders | Did Retail-Core's basket fall? | No: it pools paired data order by order, trap 5b | 0.0035 | 0.001 |
| Segment label shuffled across single orders | Did Retail-Core move differently from Retail-Plus? | No: it splits customers' orders, trap 5 | 0.0755 | 0.033 |

For the same members across two quarters, the fair test flips each member's own two quarters, a
paired sign-flip; where the groups are different customers, the fair test shuffles the labels across
whole customers. Pooling paired data is the hurried mistake. Every fair route puts the finding under
0.05, so the verdict does not depend on which fair route a learner took, and a learner who reports
the between-segment 0.0195 has answered a different question fairly: accept it with that question
named. Seeds 1 to 20 at 2,000 flips put the note's test between 0.0005 and 0.006, and the
between-segment design between 0.0145 and 0.0270.

A learner who tests Business has met the too-few-orders trap; record it.

### What does the note say when a correct run writes it?

**Claim.** From Q1 to Q2 booked revenue fell 28.5 percent, from Rs 60,48,000 to Rs 43,25,480, and
Rs 17,10,000 of the Rs 17,22,520 fall is two fewer corporate orders; among consumers the one branch
that moved is Retail-Core's revenue per order, down 17.1 percent from Rs 2,050 to Rs 1,700, with its
30 customers and 1.47 orders each unchanged.
**Evidence.** 197 distinct orders reconcile to Finance's control totals in both quarters after
dropping 10 rows posted twice and converting one amount stored as text; with each Retail-Core
customer's two quarters flipped at random, a change this large in either direction came up in 12 of
2,000 worlds, p = 0.006.
**Caveat.** The corporate fall rests on six orders against four, too few to call a trend, and one
Q2 order's segment was restored from the customer's other orders.
**Action.** Open Retail-Core's basket first, items per order and price per item, before any spend;
ask the corporate account owner why C-7304 did not reorder and why C-7300 ordered once where it had
ordered twice.

## Which traps does a hurried run fall into, and what exact wrong number does each print?

| # | Trap | The wrong number, exactly | The right number | The decision it would have misled | The check that catches it |
|---|---|---|---|---|---|
| 1 | **The reconciliation skipped**, the one most rooms fall into | Q1 Rs 50,63,000, Q2 Rs 56,60,890: **Q2 up 11.8 percent** | Q2 down 28.5 percent | "Q2 grew, nothing to investigate" goes to Meera | Input 207 against clean plus rejected; each quarter's rupees against the control total |
| 1a | Half of it: repeats kept, text read correctly | Q2 Rs 56,60,890: **down 6.4 percent** | down 28.5 | "A mild dip, the usual wobble" | Distinct ids against rows |
| 1b | The other half: repeats removed, text set to zero | Q1 Rs 50,63,000: **down 14.6 percent** | down 28.5 | The fall is reported at half its size | Q1 rupees against the control total |
| 2 | **The pass that looks clean**: the text amount coerced to zero | 0 rejects, 98 Q1 orders that reconcile, **Q1 Rs 50,63,000** | Rs 60,48,000 | Counts reconcile, so the run is signed off | Rupees per quarter against the control total |
| 3 | **The wrong branch**: the tree read on the uncleaned rows | Retail-Core **orders per customer 1.47 to 1.77, +20.5 percent**; revenue **Rs 90,200 to Rs 90,210, flat**; per order -17.0% | Frequency flat, basket -17.1 percent, revenue -17.1 percent | "Core is fine, its customers order more often" | Distinct ids per segment; reconcile before decomposing |
| 4 | **The headline on ten orders** | "Corporate revenue fell **29.2 percent**" as the first line | 6 orders then 4, in the caveat | Meera chases two invoices | Count before rate; fewer than about thirty observations |
| 5 | **The wrong unit: single orders shuffled** between segments | 151 of 2,000, **p = 0.0755**, "could be chance" | p = 0.0195 with the label moving with whole customers, or 0.006 with each customer's quarters flipped | A real basket fall read as chance, because splitting each customer's orders between the groups breaks their Q1 to Q2 pairing; on other data the same mistake more often makes a chance gap look real | Read the code: the label must move with the whole customer |
| 5b | **The wrong unit: paired data pooled**, each customer's Q1 and Q2 figures dealt as strangers, or the quarter label dealt across Retail-Core's single orders from both quarters | Per-customer revenue pooled: **p = 0.0765** both ways, 0.0325 one way. Quarter label across single orders: **p = 0.0035** both ways, 0.001 one way | p = 0.0015 on per-customer revenue and 0.006 on revenue per order, each customer's quarters flipped | The first reads a real fall as chance, or, quoted one way, gives a verdict chosen after looking; the second agrees with the fair verdict on this file for the wrong reason, treating the same 30 customers' orders as unrelated, and on another file it makes a chance gap look real | Read the code: each customer's own two quarters stay together |
| 6 | **The typical order** | **Rs 52,057**, the mean, as the typical order | Rs 2,110, the median | A basket story told on an average that ten corporate orders set | Sort and read the top ten |
| 7 | **The empty segment dropped or bucketed silently** | Segment sums short of the quarter by 1 order and Rs 2,930, or a blank group nobody names; Retail-Plus Q2 read as **34 orders, Rs 93,670, -1.6 percent**, a falling tier, with nothing in the note about the missing order | Restored: 35 orders, Rs 96,600, +1.5 percent; or the same 34 orders and Rs 93,670 with the unknown named, flagged and reconciled | A tier that grew reported as a second falling segment | Segments add back to the total, in orders and rupees |

Traps 1, 2 and 3 have the same root: a total used before it was reconciled. Trap 3 is the most
instructive to show, because the repeated batch inflated a total and also manufactured a frequency
rise that hides the basket fall. Trap 7 is the silence about the unknown order, whichever handling
the learner chose: the same Rs 93,670 is a correct run when the note names the unknown order and the
groups reconcile. A learner who shuffled order amounts between segments has
made trap 5's mistake, whatever file the code came from: name it as the mistake.

## Which runtime error does the file force, and how is it handled?

Most learners meet `ValueError: invalid literal for int() with base 10: '9,85,000'` first, and it is
the only error the file forces. The learner gives it two minutes alone, and a TA says
nothing beyond "what does the last line say?". The observation sheet records what the learner does
next (convert, zero, skip or drop).
