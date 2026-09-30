# Provenance: Week 2, Saturday

INTERNAL.

## What decided this pack

| Source | What it settled |
|---|---|
| `docs/detailing/W01_W02_spine.md`, "The Saturdays", approved 29 September 2026 | The 300-minute Saturday and its six blocks, the two-hour paper, no timed additions for Week 2, and the four things the week's source file carries. |
| `docs/detailing/W01_W02_spine.md`, the Week 2 table | The traps the stretch page draws on: integer division, the join fan-out, the WHERE that turns a LEFT join into an INNER one, the tie at fifty, the pivot that averages, and the lookup that returns a neighbour. |
| `docs/curriculum/W2_Data_manipulation.md`, the Saturday row and the Monday to Friday rows | The ten interview anchors, the Build 1 bridge, and the rule that the findings are discussed and the data's contents stay unnamed. |
| `docs/curriculum/source.xlsx`, the Saturday papers tab (W2 paper, 58 items) | Every stem and every key, unchanged. |
| `data/programme/paper_edits.yaml` | Eight proposed option edits where the bank's key was the longest option; the key file lists them. |
| `.claude/skills/exercise-builder/SKILL.md` and its references | The blueprint's minutes per type, the distractor rules, and the source file's four parts. |
| `scripts/build_saturday_paper.py`, docstring | The source file's format, in block-style YAML. |

## The paper

The tracker's Week 2 paper, rendered by `scripts/build_saturday_paper.py W02 --docx`: 58 objective
items in a 120-minute slot, at 119.5 minutes by the blueprint's pace, 14 easy, 34 medium and 10 hard.
The STUDENT paper prints the items, the three exhibits and the stretch page; the TRAINER key carries
every other column, the reasons for all 58 items and the stretch answers. The Word paper runs to 16
pages with the answer sheet on the last one; the Word key runs to 15.

## The week's source file

`C2_W02_SAT_paper_source_INTERNAL.yaml` adds no timed items, since the bank fills 119.5 of 120
minutes.

| Set | Exhibit | Drawn from |
|---|---|---|
| 1, the payments | A diagram of the 1,000 orders split into 920 with one payment row, 50 with two and 30 delivered orders with none | The situation's own numbers. It shows the payment rows before any join and states no join result, so Q40 and Q41 stay to be computed. |
| 2, the ranking tie | A table of the six members and their Q2 revenue in Rs thousand, highest first | The situation's own numbers, with no rank column, so Q44 to Q47 stay to be computed. |
| 3, the merge | A diagram of the customer table and the exposure table meeting in a left merge, then a pivot | The situation's own numbers. It states no merged row count, so Q48 stays to be computed. |

The notes give every one of the 58 items why the key holds, one reason per wrong option on the 31
option items (the misconception behind each), and the interview answer in one breath. The fill-in,
true-or-false and applied maths items carry the common wrong answer inside their reason.

The stretch page carries four written follow-ups, untimed and uncounted, each phrased as a
hypothetical on the paper's own numbers so no item describes the loaded data:

| Stretch | The traps it covers |
|---|---|
| 1 | Integer division: 1,000 / 400 printed as 2 |
| 2 | The WHERE that turns a LEFT join into an INNER one, then the fan-out from retried payments |
| 3 | The tie at fifty: RANK against ROW_NUMBER with a named tiebreaker |
| 4 | The pivot_table that averages, and the XLOOKUP match mode that returns a neighbour |

The four prompts were tightened after the first render: at full length the stretch cards filled
page 15 exactly and the builder's trailing gap pushed a blank page ahead of the answer sheet.

## The numbers, checked on 29 September 2026

| Claim | Where it was checked | Result |
|---|---|---|
| Set 1: LEFT JOIN 1,050 rows, INNER JOIN 1,020, 30 unpaid through IS NULL | PostgreSQL 16.13 in the build session | Holds |
| A WHERE on amount_paid after the LEFT JOIN returns 1,020; the same condition in ON returns 1,050 | PostgreSQL 16.13 | Holds |
| 1,000 / 400 returns 2 on integers and 2.5 on numeric | PostgreSQL 16.13 | Holds |
| Set 2: RANK 1, 2, 2, 4, 4, 6; DENSE_RANK 1, 2, 2, 3, 3, 4; five members at dense rank three or less | PostgreSQL 16.13 | Holds |
| AVG over 100, NULL and 200 is 150 while COUNT(*) is 3 | PostgreSQL 16.13 | Holds |
| LAG over 5,000, 4,200 and 3,900 gives NULL, then falls of 800 and 300 | PostgreSQL 16.13 | Holds |
| validate='one_to_one' raises MergeError "Merge keys are not unique in right dataset; not a one-to-one merge"; a left merge with one repeated right key adds one row | pandas 3.0.6 in the build session | Holds |
| pivot_table averages by default; groupby drops a missing key | pandas 3.0.6 | Holds |
| XLOOKUP match_mode 0 is exact and the default, and -1 and 1 return the next smaller or larger item | Microsoft Support, XLOOKUP function, https://support.microsoft.com/en-au/office/xlookup-function-b7fd680e-6d10-43e6-84f9-88eae8bf5929 (verified 29 Sep 2026) | Holds |
| Set 3: 1,060 merged rows; Rs 21 lakh summed against Rs 20 lakh; 51 rows under RANK and 50 under ROW_NUMBER on a tie at fifty; 8 groups; 400 customers at 2.5 | Arithmetic on the situation's numbers | Holds |

## Decisions

1. **No timed additions.** The bank fills 119.5 of 120 minutes, as the spine says.
2. **Exhibits show inputs, never results.** An exhibit that printed 1,050 or rank 4 would answer the
   items under it, so every exhibit stops at the situation's own inputs.
3. **The stretch page covers six traps in four items.** The spine asks for three or four follow-ups,
   so the traps are paired where one question leads into the next: the WHERE into the fan-out, and
   the pivot into the lookup, both of which reach the leadership deck.
4. **Stretch items are hypotheticals.** Each names numbers from the paper and never says the
   warehouse holds them, so the STUDENT paper names nothing about the loaded data.
5. **The discussion guide's 90 minutes split 35 and 55.** Five most-missed items at about seven
   minutes each, then ten anchors at five minutes each with the bridge anchor last.
6. **The mock round is 12, 12 and 6.** Each learner asks two anchors and one stretch follow-up, then
   they swap, and the last six minutes send the hardest question back to the room.
7. **The word for what a peer does is "check".** The guide avoids the grading vocabulary, since the
   paper is ungraded and the count on the front is items right.
8. **Set 1 stays as the bank has it.** Its counts match the Week 2 Tuesday data (50 orders with two
   payment rows, 30 delivered orders with none), which the room found on Tuesday. The requester
   decided on 29 September 2026 to keep the set unchanged. The guide keeps the discussion to what
   the room found and leaves the data's other contents unnamed.

## Open points for the orchestrating session

- mermaid-cli 12.0.0 is the version installed in this environment, and `render_mermaid` in
  `scripts/build_cheatsheet.py` passes `-w 2400`, which that version rejects, so every exhibit PNG
  failed without an error. The build here ran with mermaid-cli 11.17.0 installed outside the
  repository and put first on PATH.
- On page 3 of the Word key the table continues with an empty row under the repeated header, which
  comes from the builder's table split.
- The first marking step in both keys uses the third-person form of the verb mark, which is builder
  text in `render_key` and `docx_spec`; swapping it for "checks" keeps the word out of every file.

## 30 September 2026: the paper in parts, three new timed items and two option edits

The sections above are dated 29 September and number items as the bank does, which is how the paper
printed until this re-cut; the statements there that the source file adds no timed items and that
the paper holds 58 items describe that version. This section records what changed on 30 September.

### The re-cut into parts

The requester approved the re-cut on 30 September 2026: the paper prints in six parts named for
what each shows, page one carries the rules and the blueprint, and every item carries its format
and level beside its number (`data/programme/facts.yaml`, `saturday_papers.rule`). Up to six recall
items may move to the untimed stretch page, and six moved: bank 1 (HAVING), 2 (guarantee), 3 (CTE),
4 (left), 7 (PARTITION) and 9 (melt), all fill in the blank at one minute each. They print as
Stretch 5 to 10, and their keys and reasons stay in the key's stretch section. The move takes the
bank's timed items from 119.5 to 113.5 minutes, which leaves 6.5 minutes for new timed items.

| Part | Items | Minutes | Easy | Medium | Hard |
|---|---|---|---|---|---|
| 1. The week's rules, cold | Q1 to Q11 | 11 | 4 | 6 | 1 |
| 2. Asking the warehouse | Q12 to Q16 | 13 | 2 | 3 | 0 |
| 3. Joins that keep their rows | Q17 to Q27 | 27 | 1 | 8 | 2 |
| 4. Windows: rank, lag and running totals | Q28 to Q39 | 31 | 1 | 5 | 6 |
| 5. pandas and the last mile to Excel | Q40 to Q51 | 29.5 | 0 | 11 | 1 |
| 6. Read the code, read the data | Q52 to Q55 | 8.5 | 0 | 1 | 3 |
| Total | 55 | 120 | 8 | 34 | 13 |

Each part now opens on a stakeholder's words, from the week's rows or the stakeholder table in
`docs/07_Client_Zero.md`: Anand's standing question for Part 1, the data platform lead's warning for Part 2, Anand's Tuesday ask for Part 3, Marketing's
Wednesday ask for Part 4, Kavya Nair's Thursday challenge for Part 5 and her review for Part 6.
Part 6's "shows" line now says a query or a few lines of pandas, since the part prints no small
result and its pandas item runs to ten lines.

### Three new timed items in Part 6

Each exhibit is ten lines or fewer, written with invented, self-contained data in a CTE over VALUES
or a DataFrame built in the snippet, so no key depends on the warehouse's contents and no value
echoes a plant. Each query follows a query the week ran: Monday's `r3_member_spend_hurried`, the
LEFT JOIN with a `paid_date` filter in WHERE from Tuesday's round 3, and the right merge grouped by
segment from Thursday's round 2. The exhibit text was saved from the source file as it stands and
run on PostgreSQL 16.13 and pandas 3.0.5 (Python 3.11.15) on 30 September 2026. The three print
before bank 19, which now closes the part as Q55, so that in the Word paper each exhibit shares a
page with its question.

| Q | Id | Type, level, minutes | Key | Anchor |
|---|---|---|---|---|
| 52 | avg-per-member | One correct option, hard, 2 | c | [D] A stakeholder's analyst must audit your query |
| 53 | where-on-payments | Scenario set, hard, 2.5 | b | [S] INNER against LEFT join |
| 54 | reach-by-segment | One correct option, hard, 2 | d | [S] groupby in the split-apply-combine sentence |

Q52, `psql -X -h localhost -U postgres -d kalpa -f avg-per-member.sql`:

```text
 avg_q1 | avg_q2
--------+--------
   1500 |   1500
(1 row)
```

Q53, `psql -X -h localhost -U postgres -d kalpa -f where-on-payments.sql`:

```text
 rows_out | booked
----------+--------
        2 |   2400
(1 row)
```

Q54, `python3 reach-by-segment.py`:

```text
5 2 2
```

Every wrong option that stands for another computation was run as that computation, and each gave
its option's numbers exactly. For Q52, the query with COALESCE(..., 0) gives 1500 and 750, and the
average of the Q2 order rows gives 1000; option d stands for the belief that a NULL makes AVG NULL,
and AVG over 1,800, 1,200 and two NULLs returned 1500. For Q53, the date condition moved into ON gives 4 rows and 3700, the WHERE
widened to keep a NULL date gives 3 rows and 2900, and payments brought to one row per order give
1 row and 1200. For Q54, `dropna=False` gives 5 5 2, an inner merge gives 2 2 2 and a left merge
gives 4 4 4. Each wrong option's reason in the key names the trap and the day the week staged it.
The Q54 interview answer says that SQL's GROUP BY keeps NULL keys as one group; a GROUP BY over
two segments and three NULLs returned three groups on PostgreSQL 16.13 the same day.

### Option edits and reasons

Two option edits join the eight in `data/programme/paper_edits.yaml`, both proposed. Bank 34 (Q21)
and bank 39 (Q45) are more-than-one-correct items keyed a, b and c, and each offered a nonsense
fourth option, the font of the report and the cell colour, so striking the nonsense left the whole
key. Q21's option d is now "the number of channels before and after the join", a check that reads
like the other three and cannot catch a fan-out; Q45's option d is now "its exact figure", the
precision a room reaches for when a number is misread. Both keys' reasons for option d were
rewritten to match. `scripts/distractor_audit.py` passes with the keys at a 9, b 9, c 8 and d 8.
It reads 27 of the 30 option items: Q21, Q33 and Q45 open on a statement before their question, so
the audit does not take them for a stem, and the two edited options were checked by hand.

The reasons now cover all 55 printed items: why the key holds, a reason for every wrong option on
the 30 option items, and the interview answer in one breath. The three new items carry their own,
and the two ordering items, Q16 and Q51, now name the wrong order a paper is likely to hold.

### The discussion guide, renumbered

The guide's item numbers came from the paper at commit 5c57eea, which numbered items as the bank
does. Each item was matched on its text to the final paper; the six moved items are cited as
Stretch 5 to 10.

| Old | New | Old | New | Old | New | Old | New |
|---|---|---|---|---|---|---|---|
| 1 | Stretch 5 | 16 | Q10 | 31 | Q42 | 46 | Q36 |
| 2 | Stretch 6 | 17 | Q11 | 32 | Q43 | 47 | Q37 |
| 3 | Stretch 7 | 18 | Q12 | 33 | Q14 | 48 | Q46 |
| 4 | Stretch 8 | 19 | Q55 | 34 | Q21 | 49 | Q47 |
| 5 | Q1 | 20 | Q13 | 35 | Q22 | 50 | Q48 |
| 6 | Q2 | 21 | Q17 | 36 | Q32 | 51 | Q49 |
| 7 | Stretch 9 | 22 | Q18 | 37 | Q33 | 52 | Q15 |
| 8 | Q3 | 23 | Q19 | 38 | Q44 | 53 | Q27 |
| 9 | Stretch 10 | 24 | Q20 | 39 | Q45 | 54 | Q38 |
| 10 | Q4 | 25 | Q28 | 40 | Q23 | 55 | Q39 |
| 11 | Q5 | 26 | Q29 | 41 | Q24 | 56 | Q50 |
| 12 | Q6 | 27 | Q30 | 42 | Q25 | 57 | Q16 |
| 13 | Q7 | 28 | Q31 | 43 | Q26 | 58 | Q51 |
| 14 | Q8 | 29 | Q40 | 44 | Q34 | | |
| 15 | Q9 | 30 | Q41 | 45 | Q35 | | |

The new items join the guide where they belong: Q52, Q53 and Q54 in the most-missed candidate list,
Q53 under the INNER against LEFT anchor and Q54 under the groupby anchor. The marking gains the
step that enters each paper's ticks by seat in `C2_W02_SAT_item_analysis_TRAINER.xlsx`, whose
Discussion sheet orders the most-missed discussion and whose flags go to the tracker's owner.

## 30 September 2026, later: the Word paper in the diagnostic's format

### The format

The Word paper now takes the layout of the requester's baseline diagnostic,
`content/W00/D2/paper/C2_W00_D02_diagnostic_STUDENT.docx`, which the builder draws from commit
f7dff4f: a first page with what the paper is for and the rules with a Company row, then step one,
where each learner rates the six parts from 1 to 4 before reading any item; the paper at a glance
and a pacing ribbon; open question blocks with each item's label beside its level, never split
across pages, with every exhibit and set case opening the block of its first question; and an
answer sheet on one page. The key ends on a marking grid, and the item-analysis workbook gains a
Ratings sheet. Rendered through LibreOffice on 30 September 2026, the paper runs to 16 pages and the
key to 17. Every exhibit and set case prints on the page of its first question, the answer sheet is
page 16 alone, and the ribbon's narrowest band, Part 6 at 8.5 minutes, prints its label whole.

### The labels

Every printed item carries a label of two to five words, printed beside its level, saying what the
item asks the reader to do with what is in front of them; none states or hints at the key, and no
two neighbouring items share one. The bank items' labels sit in `notes`, and the additions carry
their own.

| Q | Label | Q | Label | Q | Label |
|---|---|---|---|---|---|
| Q1 | Complete the filter | Q20 | The first check | Q39 | Run the falling flag |
| Q2 | Name what LAG returns | Q21 | Build the validation | Q40 | Define groupby |
| Q3 | Name the error | Q22 | Compare two joins | Q41 | Explain the row count |
| Q4 | Check the run order | Q23 | Trace the LEFT join | Q42 | Find the wrong setting |
| Q5 | Test a group filter | Q24 | Trace the INNER join | Q43 | Excel's job |
| Q6 | What INNER keeps | Q25 | Find the unpaid orders | Q44 | Four merge claims |
| Q7 | Read a joined SUM | Q26 | Judge the payments SUM | Q45 | What a number needs |
| Q8 | Two rank functions | Q27 | Reason with numbers | Q46 | Count the merged rows |
| Q9 | A window in WHERE | Q28 | Predict the ranks | Q47 | Predict what validate does |
| Q10 | What groupby returns | Q29 | Same values, DENSE_RANK | Q48 | Compare the totals |
| Q11 | A pivot on raw rows | Q30 | Top three per segment | Q49 | Place the fix |
| Q12 | Which clause | Q31 | Find the cause | Q50 | Size the customer table |
| Q13 | Why the warehouse | Q32 | Window or GROUP BY | Q51 | Order the tools |
| Q14 | Four statements | Q33 | Four claims on ties | Q52 | Predict the result |
| Q15 | Predict the row count | Q34 | Rank member D | Q53 | Run the query by hand |
| Q16 | Order the clauses | Q35 | Dense-rank member F | Q54 | Predict the output |
| Q17 | Name the join | Q36 | Count what the filter keeps | Q55 | Fix the query |
| Q18 | Explain the extra rows | Q37 | Exactly four members |  |  |
| Q19 | Read four queries | Q38 | Count both lists |  |  |

### Option edits for balance

`scripts/distractor_audit.py` now fails a Saturday item whose options run past 30 characters when
the shortest is under 60 percent of the longest, and six items failed it. Each outlier was reworded
in `data/programme/paper_edits.yaml`, status proposed, keeping every stem and key; the lengths are
the audit's, without a closing full stop.

| Q (bank) | Option | Was | Now | Lengths before, after |
|---|---|---|---|---|
| Q14 (33) | c, in the key | HAVING can use COUNT(*). | HAVING can compare COUNT(*) with a number. | 22 to 39, then 34 to 41 |
| Q14 (33) | d | WHERE can use COUNT(*). | WHERE can compare COUNT(*) with a number. | as above |
| Q19 (23) | b | SELECT DISTINCT order_id FROM payments | SELECT DISTINCT order_id FROM payments ORDER BY order_id | 38 to 73, then 47 to 73 |
| Q25 (42) | d | ORDER BY paid_at | RIGHT JOIN, then WHERE orders.order_id IS NULL | 16 to 51, then 37 to 51 |
| Q32 (36) | b | total revenue per segment | each segment's total revenue for the quarter | 25 to 60, then 37 to 60 |
| Q33 (37) | b, in the key | RANK gives tied members the same rank. | RANK gives members who tie the same rank. | 37 to 63, then 40 to 63 |
| Q44 (38) | a, in the key | It is the pandas form of a SQL join. | It is the pandas form of a SQL join on a key. | 35 to 60, then 40 to 60 |

Each wrong option stays a misconception the week staged: WHERE comparing COUNT(*) is the aggregate
in WHERE, the sorted DISTINCT list hides the duplicates it was meant to find, the RIGHT JOIN with IS
NULL on the orders side is the anti-join from the other side that Tuesday's round 3 ran as step A7,
and a segment's total for the quarter is one row per group, which GROUP BY answers alone. The key's
reasons that quoted a changed option were rewritten: bank 23's option b, bank 33's why and option d,
bank 36's option b and bank 42's option d. The audit now reads all 30 option items and passes with
the keys at a 12, b 12, c 11 and d 8, which supersedes the count of 27 recorded above.

### Purpose and company

The purpose paragraph walks the week's case in order, from the rows: Anand's Monday numbers
computed in the warehouse, booked revenue against collected, Marketing's protect list, and the
customer table built in pandas and carried to the leadership deck; then what the paper finds out,
and that the room's scores by part beside the step-one ratings tell Monday's session where to
start. The Company row names the people the items and the part openings name, with the titles the
week's files give them: Anand Iyer as finance controller, as Tuesday's and Thursday's files and the
client-zero lock have it (Monday's files call him CFO); Kavya Nair as senior analyst; Meera Raghavan
by her office and the growth review deck from Friday's row, since no Week 2 file gives her title;
and the head of Retail-Plus, the marketing lead and the data platform lead by role alone.

### The discussion guide

The guide adds step one: learners rate the six parts before reading any item, the Academic TA
enters the ratings by seat in the workbook's Ratings sheet with the ticks, and the last 5 minutes
of the 90-minute discussion set each part's mean rating beside its right rate and name the parts
where confidence ran ahead of the work. The anchors round is 50 minutes, ten anchors at five
minutes each, as the guide already paced it.

## 30 September 2026, last: the more-than-one keys relabelled

All seven more-than-one items came from the tracker with a in the key, and four of them keyed
exactly a, b and c, so ticking a on every such item always scored. Three are relabelled with an
`order` edit in `data/programme/paper_edits.yaml`, status proposed: the same options print, the
same ones are correct, and the key's letters and the key file's reasons move with them. Each edit
carries `from_key`, the tracker's key it was written against, so the sync reports it folded once
the tracker prints the new order, rather than laying it twice. Bank 34's reworded option d, "the
number of channels before and after the join", now prints at a.

| Q (bank) | Tracker key | Printed as the tracker's | Printed key | Wrong options now at |
|---|---|---|---|---|
| Q14 (33) | a, b, c | a, d, b, c | a, c, d | b |
| Q21 (34) | a, b, c | d, a, b, c | b, c, d | a |
| Q22 (35) | a, b | c, a, d, b | b, d | a and c |

Q32, Q33, Q44 and Q45 keep the tracker's order, so the eight wrong options sit at each letter
twice and each letter sits in five of the seven keys. Q14's order also puts its two WHERE
statements side by side, then its two HAVING statements. `scripts/distractor_audit.py` now fails a
Saturday paper where one letter sits in every more-than-one key across four or more such items;
the paper as it stood before this change fails it, and the relabelled paper passes, with the keys
of all 30 option items at a 10, b 11, c 11 and d 11.

## 30 September 2026, after the merge: Anand's title left off the paper

The tracker's Week 1 and Week 2 rows and the Weeks 1 and 2 spine call Anand Iyer the CFO, while
client zero v2.2 calls him the finance controller, and the tracker ranks higher. The paper now
names him by his work, "Anand Iyer answers for Finance's books", which is true under either
title, and the conflict is recorded as `anand-title` in `data/programme/facts.yaml` for the
Programme Head to settle.

## 30 September 2026, the requester's two decisions

The requester accepted every option edit and relabelling in `data/programme/paper_edits.yaml`, so
each now carries status accepted and applies until the tracker's Saturday papers tab carries it;
the decision is `saturday-edits-w1-w2` in `data/programme/facts.yaml`. The requester also settled
Anand Iyer's title as finance controller (decision `anand-finance-controller`), so the paper names
him by that title again, where the entry above had left the title off.

## 30 September 2026, version 3: the paper raised to interview grade

The sections above describe the 55-item paper. This section records its replacement, built on
branch `w02-sat-v3` from main after the Saturday builder gained folds, stem and situation edits,
word banks and match tables (commit 2ee47f7 on `claude/vigilant-cannon-ukpbs2`).

### What decided it

| Source | What it settled |
|---|---|
| The requester's plan, 30 September 2026 | The bank sets the topics and the paper sets the bar: every bank concept stays tested, and a bank item may be reworded, folded into a deeper item or moved to the stretch page, with a reason; about 35 timed items in 112 to 120 minutes; about 5 percent easy, 35 medium and 60 hard; word banks and match tables in place of plain blanks. |
| The requester's direction on real cases, relayed the same day | Kalpa where an item continues the week's class cases; real companies and public cases for a third to a half of the items, every fact checked against a source, hypotheticals marked as illustrative. |
| The requester's direction on solution design, relayed the same day | Code-reading items at about a third; solution design (best fit, sizing, ordering, matching, the fact that changes a choice) at a third or more; every scenario opening on how the business works, with each domain term explained at first use. |
| `docs/curriculum/W2_Data_manipulation.md`, `docs/detailing/W01_W02_spine.md` and the five Week 2 day sheets | The cases, the quotations, the traps and every Kalpa number the paper continues. |
| `data/programme/facts.yaml`, decisions `plants-once-found`, `anand-finance-controller` and `reporting-day-line` | The paper may name what the room found in class; Anand Iyer is the finance controller; the Tuesday [D] line reads "fails at the end of reporting day". |

### The paper

35 timed items in six parts, paced at 117 of the 120 minutes (21 hard at 4 minutes, 12 medium at 2.5
and 2 easy at 1.5): 60 percent hard, 34 percent medium and 6 percent easy.

| Part | Items | Minutes | Easy | Medium | Hard | Setting |
|---|---|---|---|---|---|---|
| 1. Anand's Monday numbers | Q1 to Q6 | 17.5 | 2 | 1 | 3 | Kalpa, with Facebook's 2016 metric (Q6) |
| 2. Booked against collected | Q7 to Q11 | 20 | 0 | 0 | 5 | Kalpa, with Public Health England, 2020 (Q11) |
| 3. The protect list and the plan line | Q12 to Q16 | 18.5 | 0 | 1 | 4 | Kalpa |
| 4. One row per customer | Q17 to Q22 | 19.5 | 0 | 3 | 3 | Kalpa, with the gene-name case (Q22) |
| 5. The last mile, and spreadsheets in public | Q23 to Q29 | 20.5 | 0 | 5 | 2 | Kalpa's workbook, with Reinhart and Rogoff (Q27), JPMorgan (Q28) and Uber (Q29) |
| 6. Read the code, read the data: an AI team's tables | Q30 to Q35 | 21 | 0 | 2 | 4 | A food-delivery company such as Swiggy or Zomato, illustrative |

Formats: 18 one correct option; 7 scenario-set items in three sets (Set 1, Q7 and Q8; Set 2, Q12 and
Q13; Set 3, Q17 to Q20), answered as one letter (Q7, Q12, Q13 and Q20), a number (Q17), a true or
false with its reason as four options (Q18) and every correct letter (Q19); 2 more-than-one-correct
items in all (Q11 and Q19), whose keys share no letter; 2 ordering items (Q2 and Q8, the second
inside Set 1); 2 word-bank items (Q3 and Q4, Word bank 1, five words for two blanks); 4 match rows
(Q23 to Q26, Match table 1, six techniques for four jobs); 1 applied maths item (Q29). No plain
blank and no bare true or false prints.

By what each item asks: 11 read code or a query (Q1, Q6, Q9, Q15, Q21, Q22, Q30 to Q34); 18 are
solution design, choosing the best fit, sizing, ordering the steps, matching jobs to techniques or
naming the fact that changes a choice (Q5, Q7, Q8, Q10 to Q14, Q17, Q19, Q20, Q23 to Q29); the other 6
read a chart or a claim or recall a rule (Q2 to Q4, Q16, Q18, Q35). 12 items are set in public cases or
at a named company (Q6, Q11, Q22, Q27 to Q35).

`scripts/distractor_audit.py content/W02/SAT` passes with 25 option items read and keys at a 7, b 6,
c 6, d 7 and e 1. The llm-tic-scrubber scanner reports the paper, the key and this guide clean.

### The fate of every bank item

Printed, 4: bank 2 and bank 3 from Word bank 1 (Q3 and Q4, paced at 1.5 minutes where the tracker
says 1), bank 27 with the stem proposed in `data/programme/paper_edits.yaml` (Q14, paced at 2.5
where the tracker says 2), and bank 57 as the tracker has it (Q2). Moved to the stretch page: none.
Folded into a deeper printed item, 54, each with its reason in the source file's `folded` block and
in the key:

| Printed item | Bank items folded into it |
|---|---|
| Q1 int-div | 56 |
| Q2 (bank 57) | 10, 18, 19 |
| Q5 monday-fact | 20, 32, 58 |
| Q7 join-counts | 4, 13, 21, 22, 24, 35, 40, 41 |
| Q8 report-steps | 23, 43, 53 |
| Q9 where-on-payments | 12 |
| Q10 reporting-day | 34 |
| Q12 rows-shipped | 14, 25, 26, 44, 45, 46, 54 |
| Q13 tie-rule | 37, 47 |
| Q14 (bank 27) | 7, 15, 36 |
| Q15 lag-gap | 6, 55 |
| Q16 run-rate | 39 |
| Q17 merge-rows | 30, 48 |
| Q18 pivot-total | 17, 50 |
| Q19 stop-line | 8, 38, 49 |
| Q20 first-touch | 51 |
| Q21 months-view | 9, 16, 29 |
| Q23 fix-lookup | 31 |
| Q32 low-ratings | 1, 11, 33, 52 |
| Q33 not-in | 5, 42 |
| Q34 token-peers | 28 |

Bank 58 first moved to the stretch page; the Word paper then printed it alone on a page of its own,
so it was folded into Q5, whose reason gives the order a number travels.

### The Kalpa numbers

Every Kalpa number on the paper was recomputed on 30 September 2026 from the room's own files: the
warehouse (`content/W02/D1/data/C2_W02_D01_warehouse_v4_STUDENT.sql`) loaded into a scratch schema on
PostgreSQL 16.13, Thursday's exposure feed (`content/W02/D4/data/C2_W02_D04_exposure_STUDENT.csv`)
and Friday's two exports (`content/W02/D5/data/`), on pandas 3.0.5. They match the day sheets: the
Retail-Plus leaf (215 and 140 orders, 91 and 76 members); the LIMIT sample (Rs 3,900, then Rs 4,590
after the reload); Q2's payment rows (216, 188, 28 and 30, with 8 orphans) and the join's 678, 462 and
648; collected Rs 9,66,45,070 and the gap of Rs 17,54,930; the Retail-Plus boundary (ties at Rs 3,480
and Rs 3,350; 51, 52 and 50 shipped); the four members' months and the falling flag; the weekly booked
revenue against the plan line; the merge's 346 rows and Rs 45,800; the lookup's C-0194 for C-0195;
Mumbai's Rs 1,56,790 against Rs 7,14,890; and the raw export's 1,450 rows. The paper names only what
the room found in class (decision `plants-once-found`).

### The public cases, checked on 30 September 2026

| Item | What the paper states | Source |
|---|---|---|
| Q6 | Facebook's average duration of video viewed divided total time by views of 3 seconds or more; an overstatement of 60 to 80 percent over two years; billing not affected | TechCrunch, 22 September 2016, citing The Wall Street Journal |
| Q11 | 15,841 cases between 25 September and 2 October 2020 left out because files exceeded the maximum size; lab CSV files converted to .xls, 65,536 rows a sheet, records past the cut-off left off | GOV.UK, PHE statement, 4 October 2020, updated 5 October; The Register, 5 October 2020 |
| Q22 | Excel turns SEPT2 into 2-Sep and MARCH1 into 1-Mar; about a fifth of papers with Excel gene lists carried such errors (704 of 3,597) | Ziemann, Eren and El-Osta, Genome Biology 17:177, 2016 |
| Q22 | HGNC changed every symbol Excel converts to a date: SEPT1 is now SEPTIN1 and MARCH1 is now MARCHF1 | Bruford and colleagues, Nature Genetics 52(8), 2020, Box 3 |
| Q27 | An average in the spreadsheet stopped short of the data and left out Australia, Austria, Belgium, Canada and Denmark; 2.2 percent against the published -0.1 for the over-90-percent group, a figure that also corrects two other choices | Herndon, Ash and Pollin, PERI working paper 322, April 2013; Retraction Watch, 18 April 2013; The Conversation, 22 April 2013 |
| Q28 | The model ran through Excel spreadsheets filled by copying and pasting (page 123); a step divided by the sum of the old and new rates where the modeller meant their average, "muting volatility by a factor of two" (page 128) | Report of JPMorgan Chase and Co. Management Task Force Regarding 2012 CIO Losses, 16 January 2013 |
| Q29 | Uber took its New York commission on the gross fare, before taxes and fees, and repaid about 900 dollars a driver on average | CBS News, 24 May 2017 |

The pages read, each checked on 30 September 2026:

- TechCrunch: https://techcrunch.com/2016/09/22/facebook-miscalculation-significantly-inflated-average-video-view-times-for-years/ (checked 30 September 2026)
- GOV.UK: https://www.gov.uk/government/news/phe-statement-on-delayed-reporting-of-covid-19-cases (checked 30 September 2026)
- The Register: https://www.theregister.com/2020/10/05/excel_england_coronavirus_contact_error/ (checked 30 September 2026)
- Genome Biology, via PubMed Central: https://pmc.ncbi.nlm.nih.gov/articles/PMC4994289/ (checked 30 September 2026)
- Nature Genetics, via PubMed Central: https://pmc.ncbi.nlm.nih.gov/articles/PMC7494048/ (checked 30 September 2026)
- PERI, the working paper's page: https://peri.umass.edu/publication/does-high-public-debt-consistently-stifle-economic-growth-a-critique-of-reinhart-and-rogoff/ (checked 30 September 2026)
- RePEc, the working paper's abstract: https://ideas.repec.org/p/uma/periwp/wp322.html (checked 30 September 2026)
- Retraction Watch: https://retractionwatch.com/2013/04/18/influential-reinhart-rogoff-economics-paper-suffers-database-error/ (checked 30 September 2026)
- The Conversation: https://theconversation.com/the-reinhart-rogoff-error-or-how-not-to-excel-at-economics-13646 (checked 30 September 2026)
- The JPMorgan report, in Yale's YPFS library: https://ypfsresourcelibrary.blob.core.windows.net/fcic/YPFS/JPMorgan%20Management%20Task%20Force%20Regarding%202012%20CIO%20Losses%201-16-13.pdf (checked 30 September 2026)
- CBS News: https://www.cbsnews.com/news/uber-drivers-underpaid-in-new-york-city-for-years/ (checked 30 September 2026)

What could not be verified in the session, and so does not print: the spreadsheet rows of the
Reinhart and Rogoff average (secondary sources give rows 30 to 44 against 30 to 49; the PERI PDF
returned 410 Gone), the BBC's account of the PHE templates (the BBC and The Guardian refused the
session's fetcher, so The Register carries that detail), and a commission rate for Uber (Q29's 25
percent, fare and tax are marked illustrative). Every number in Part 6 and in the Facebook, JPMorgan
and Uber exhibits is illustrative and says so on the page.

### The proof

`content/W02/SAT/internal/C2_W02_SAT_key_proofs_INTERNAL.py` runs cold from the repository root: it
creates the schema `w02_sat_proof`, loads the warehouse, runs every code exhibit as the source file
prints it, recomputes every Kalpa number, asserts every key letter against the source file and the
text of every keyed option, reasons the Excel items in comments with their arithmetic asserted on
Friday's exports, and drops the schema. Its run on 30 September 2026 on PostgreSQL 16.13, pandas
3.0.5 and Python 3.11.15 printed 35 PASS lines, Q1 to Q35, and "RESULT: PASS (35 items proved)".

### The Word files

Built with `python3 scripts/build_saturday_paper.py W02 --docx` and rendered through LibreOffice on
30 September 2026: the paper runs to 20 pages and the key to 20. Every exhibit prints on the page of
the item that reads it, the two charts print in bronze and ink with titled axes, the stretch page
holds the four written follow-ups, and the answer sheet is page 20 alone. Pages 7, 9, 10 and 18 end
between 40 and 60 percent full, where the next exhibit and its item are kept together or a part
begins.

### Open points for the orchestrating session

- `python3 scripts/sync_programme.py --check` reports Week 1's paper and key as stale: the merged
  builder renders them differently. They belong to the Week 1 session and were not touched here.
- The requester decided on 29 September 2026 to keep bank set 1 unchanged. Version 3 folds it into
  a set on the week's own Q2 book, which carries the instalment orders the bank's set leaves out; the
  decision predates the plan of 30 September, so it needs the requester's confirmation.
- Bank 28's key, ties in the window's ORDER BY, holds under a ROWS frame; under Postgres's default
  frame tied rows share one running total, so the result itself does not move between runs. Q34
  tests the default frame directly.
- Bank 23's key, HAVING count(*) > 1 by order, lists the 188 invoices paid in two instalments on the
  week's book as well as the 28 repeats; Q8's reason gives both counts.
- The session found the local Postgres stopped and its postgres role without the stated password; it
  started the cluster and set the stated password, which touches the environment and no file.
