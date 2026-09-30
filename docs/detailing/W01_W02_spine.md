# Weeks 1 and 2: the approved spine

Approved by the requester on 29 September 2026, together with the campus day of 10:00 to 13:00 and
14:00 to 17:00 and the TA-led practice lab after it. Each day's session builds from this page
without stopping at a spine of its own. Where this page and a curriculum row differ, this page
wins; everything it leaves unchanged, the row still carries, including the scenario, the data
version, the plants, the interview anchors and the references.

## The rule every day follows

Each day is one Kalpa case climbed in five rungs, each rung a harder business question. Python, SQL,
pandas or Excel is the calculator. Every staged failure is a trap: a plausible wrong number with a
business consequence, shown exactly, then the check that catches it and the fix. A syntax or runtime
error is met when it happens and gets two minutes and the last line of its trace, never a chapter.

## The campus day

Clock times live in `data/programme/facts.yaml`; lesson material carries durations only.

| Block | Minutes | What runs |
|---|---|---|
| Morning | 180 | The client's ask and the thinking drawn on the board (20); round 1 (50); round 2 (50); a break (10); round 3 (50) |
| Afternoon | 180 | The escalated case, unguided (60); the debrief of the room's wrong answers (15); a break (10); the second case, in pairs (45); the interview drill aloud (30); the Kahoot and tomorrow's ask (20) |
| After | The lab's length | The TA-led practice lab, which the pack supplies with a practice set and its solutions |

A round is 50 minutes: the question and its picture, the trainer's demonstration on Kalpa data, the
trap and its wrong number, the room running a harder variant, and Kavya's review.

**Week 2's faculty days (Monday to Wednesday, tentative).** The trainer keeps the morning block and
the first 60 minutes of the afternoon, which carry the escalated case (45) and the Kahoot (15); the
IITGN block takes the last 120 minutes, after the day's applied core, as `facts.yaml` places it.

**Week 1 Friday.** The lab day keeps the row's shape in the longer day: the AI-free lab (150), a
break (10), the lab debrief (40), the growth-review rehearsal in two rounds (100), a timed round of
three analyst cases from the week's interview angles, answered aloud (40), and the Kahoot with
Saturday's preview (20). The case round adds no idea; it fills the longer day with practice.

## Volume per teaching day

The targets, and the form each family takes, are in
`.claude/skills/day-pack-builder/references/the-standard.md`.

## Week 1

Traps marked * were added by this spine; the others come from the rows.

| Day | The case and its five rungs | The traps, each a plausible wrong number |
|---|---|---|
| Mon | Is acquisition even the short branch? The rungs climb from four readings of "sales", to the revenue tree as metrics, to the leaves counted on 30 orders, to the typical order, to which branch Meera opens first. | Rows counted as customers, 30 instead of 23, so orders per customer reads 1.00 and "nobody comes back"*; cancelled orders counted as sales*; the mean of Rs 18,160 sold as the typical order when the median is Rs 2,205; two 10 percent lifts called 20 percent*. |
| Tue | Which branch moved from Q1 to Q2? The rungs run from whether the drop is real, to the tree decomposed, to the segment split, to mix against rate, to the hypothesis Marketing will attack. | Quarters of unequal length compared as totals; an average of segment averages*; a missing discount read as zero; a helper that returns nothing, so a segment drops out of the comparison unnoticed. |
| Wed | Which Q1 figure is right, Rs 2.1 crore or 1.9? The rungs run from the profile, to the migration's duplicates, to the identity rule, to missing and malformed values, to the revenue bridge with Tuesday recomputed. | A whole-record dedupe that reports zero duplicates; bad amounts coerced to zero so the file looks clean; the genuine bulk order removed as an outlier*; counts that reconcile while rupees do not*. |
| Thu | Real, noise, or the discount? The rungs run from a shuffle test on the Retail-Plus gap, to real against worth acting on, to 40 percent on twelve orders, to the monsoon discount split by segment, to the one-page note that may say "not yet". | p = 0.03 read as a 3 percent chance of being wrong; significance treated as importance; a headline rate on twelve orders; the aggregate trusted while every segment fell. |
| Fri | Rebuild the week cold, then defend it. The AI-free lab runs the whole pipeline on an unseen export, the debrief replays where the room broke, and pairs defend the note against a partner playing Marketing. | The week's traps in new places, and a reconciliation skipped under time pressure, which is the one most rooms fall into. |

## Week 2

The IITGN faculty blocks on Monday to Wednesday are tentative, and each takes 120 minutes of the day.

| Day | The case and its five rungs | The traps, each a plausible wrong number |
|---|---|---|
| Mon | Anand's Monday numbers, straight from the warehouse. The rungs run from Week 1's leaves re-answered in SQL and checked against Week 1, to per segment and quarter, to two quarters as CTEs, to the suite Anand's analyst audits. | Orders per customer returning 1 because Postgres divides integers*; COUNT(*) counting order rows as customers*; AVG skipping NULLs without saying so*; LIMIT without ORDER BY giving two learners two answers. |
| Tue | Booked against collected, without lying. The rungs run from two tiny tables, to the naive join, to the row-count check and the revenue bridge, to the unpaid and double-paid lists, to the report by channel Anand signs. | A join fan-out that doubles collected revenue while every row looks right; an INNER join that hides unpaid orders*; a WHERE on the payments side that quietly turns the LEFT join into an INNER one*. |
| Wed | Protect the best members before they drift. The rungs run from the top fifty overall, to per segment, to the tie at fifty, to falling spend with LAG, to the running total against plan. | Ranking the whole table when the ask was per segment*; LAG without PARTITION reading another customer's month*; a skipped month counted as a fall*; a tie that ships 49 or 51 rows. |
| Thu | One table per customer, refreshed every Monday. The rungs run from recency, frequency and spend with groupby, to the exposure merge, to the months pivot, to one question in three tools, to the tool-choice note. | A merge that doubles a customer's spend; pivot_table averaging where a total was meant, which is its default*; groupby dropping customers with no segment*; recency measured from today instead of the data's last date*. |
| Fri | The number reaches the leadership deck. The rungs run from a pivot on the clean table, to the same pivot on the raw export, to the member lookup, to the front-page number, to the operating rule. | A pivot double-counting the double-paid orders; an approximate lookup returning a neighbour for a missing id; SUM counting rows a filter hid*; a headline with no denominator or period. |

## The afternoon and the lab, day by day

Each is drawn from the day's own row; the day's session writes the detail.

| Day | The escalated case | The second case, in pairs | The practice lab set |
|---|---|---|---|
| W1 Mon | Meera's question answered with evidence: the leaves, the typical order, the branch to open first and what one window cannot show | Where revenue comes from by customer type and channel, on the same file, and whether one channel changes the recommendation | The five initiatives placed and priced, a tree for a business the learner knows, and predict-the-number items on the leaves |
| W1 Tue | The decomposition for all four segments, the branch and segment that moved, and two hypotheses with the evidence that settles each | The Retail-Plus head's question and Marketing's pushback, argued from the same numbers | Order the rungs, spot the mismatched window in three comparisons, and the one-page investigation memo |
| W1 Wed | The full pass: cleaned data, decisions log, reconciled counts, the revenue bridge, the recomputed tree and the note to Finance | The auditor's question, why 14 rows were dropped, answered from the decisions log | Two profile printouts to judge, and a second export with new defects |
| W1 Thu | The 5,000-shuffle test, the Student and discount answers, and the one-page note | Marketing defends the monsoon sale; the pair reads it by segment and holds the caveat | Four p-value sentences to judge, the confounder in three vignettes, and the shuffle rerun on Monday's take-home data |
| W1 Fri | The lab itself | The rehearsal | Rerun the step where the learner stalled |
| W2 Mon | The Monday suite, six queries reproducing Week 1's tree by segment and quarter | None on a faculty day | Predict the row counts of four queries, and order five clauses by execution |
| W2 Tue | Booked against collected by channel, with the count reconciliation, the unpaid list and the double-paid list | None on a faculty day | Predict four join row counts, and match five business questions to the join that answers each |
| W2 Wed | The protect list with the chosen tie rule, the falling-spend flag and the running total against plan | None on a faculty day | Predict three rankings on a tie, and GROUP BY or window for six asks |
| W2 Thu | The customer table with a validated merge and one reshaped view | The three-tool re-expression and the tool-choice note | Predict the shape of four groupby and pivot calls, and pick the tool for five asks |
| W2 Fri | The three deliverables for Monday's deck, refreshable from the exported customer table | The operating rule defended against a director who wants to edit the source | Warehouse, pandas or Excel for eight asks, and the misread in three front-page numbers |

## The Saturdays

The requester set the Saturday at 300 minutes on 29 September 2026, and the papers at two hours.

| Part | Minutes | What runs |
|---|---|---|
| The recap paper | 120 | Pen and paper, AI-free, from the Word file |
| Break | 20 | |
| Marking | 20 | Papers swapped and marked against the key, read out by the Academic TA |
| The solution discussion | 90 | The most-missed items first, then the week's anchors answered aloud as interview answers, with random call-outs |
| The mock-interview round | 30 | In pairs, each learner asks the other two of the week's anchors and one follow-up from the stretch page, then they swap |
| Doubts and the bridge | 20 | Week 1: the CFO wants the numbers from the warehouse every Monday. Week 2: Build 1 opens in Kalpa Health |

**The papers.** The tracker's bank is the floor. Week 1's bank fills 107 of the 120 minutes, so the
week's source file adds about 13 minutes of new timed items: one or two new scenario sets built on
the week's traps in this spine, at the blueprint's pace. Week 2's bank fills 119.5 minutes and needs
no timed additions. On 30 September 2026 the requester re-cut both papers into parts, each with a
"Read the code, read the data" part, and moved six recall items from each to the stretch page, so
both source files now carry new timed items on short exhibits of the week's own code. Both source
files add an exhibit for every scenario set, drawn only from the
set's own numbers; the reasons for every item, which are why the key holds, why each wrong option
fails and the interview answer in one breath; and an untimed stretch page of three or four written,
interview-grade follow-ups. The builder and the source file's format are in
`scripts/build_saturday_paper.py`.

## Checked on 29 September 2026

On PostgreSQL 16.13, `count(*) / count(distinct customer)` over 3 orders and 2 customers returns 1;
`avg` over 100, NULL and 200 returns 150 while `count(*)` returns 3; a `WHERE` on the payments
table drops the unpaid order from a `LEFT JOIN`; a double-posted payment doubles the naive sum. On
pandas 3.0.5, `pivot_table` averages by default and `groupby` drops a missing key. The Excel `SUM`
behaviour under a filter is checked in Excel during the Week 2 Friday build.

## What stays as the rows have it

SQL stays in Week 2. The data versions, the plants and what the room is meant to find, the interview
anchors, the references and the Kahoot plans are the rows'. Each day's interview drill adds case-style
follow-ups to the row's anchors, and every answer is written in the day pack, never in the row.
