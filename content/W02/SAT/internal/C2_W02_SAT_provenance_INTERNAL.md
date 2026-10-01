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

## 30 September 2026, version 3 raised: what the blind sitting found and what changed

A fresh sitter, who had not seen the key, sat version 3 the same day and found it short of the
interview bar. This section records the findings as the orchestrating session relayed them, the
decisions it recorded, and what changed on branch `w02-sat-v3`. The tables in the section above
describe the version the sitter read; this section supersedes them where they differ.

### The decisions the orchestrating session recorded

- Folding the bank's Set 1 into the set on the week's own quarter is accepted, and is recorded as
  decision `w2-set1-fold` on the integration branch. `data/programme/facts.yaml` is untouched here.
- Folding bank 19 into Q2 is accepted.
- Bank 28 and bank 23 are accepted as handled on this paper, and each goes to the tracker as an
  issue on the bank item itself:
  - **Tracker issue, bank 28.** The key says a running total changes between two runs because the
    window's ORDER BY has ties. Under Postgres's default frame, RANGE with its peers, tied rows share
    one running figure, so the result does not move between runs; a ROWS frame, or a ROW_NUMBER over
    a tied order, is what can change from one run to the next. The item needs a stem that names the
    frame, or a new key. Q34 tests the default frame on a tie.
  - **Tracker issue, bank 23.** The key, HAVING count(*) > 1 grouped by order, lists every order
    with two payment rows: on the week's book that is 216 orders, the 188 invoices paid in two
    instalments as well as the 28 the gateway posted twice. Grouping by order and instalment lists
    the 28. The stem asks for "the orders that were paid twice", which reads either way, so the stem
    needs the instalment in it or the key needs the second column. Q8's left-out step is bank 23's key
    written as a step, and its reason gives both counts.
- The front matter's "write T or F" is being fixed in the builder on the integration branch, so this
  branch leaves it.

### What the sitting found

| Kind | Finding |
|---|---|
| Difficulty | Twelve items were hard in fact: Q1, Q6, Q7, Q9, Q12, Q15, Q21, Q22, Q30, Q31, Q33, and Q34, which was labelled medium. Q5, Q8, Q10, Q11, Q13, Q16, Q20, Q27, Q28 and Q32 were each one judgement, a recall, or answered by a cue. |
| Give-aways | Q8's pronouns gave the order of its steps; Q35's stem handed over its key; Q16 could be answered without its chart, and two of its options printed the same count; Q1, Q16 and Q28 built the key from halves of distractors; Q23 to Q26 shared words between prompts and techniques; Q14's key was its only option without a "because"; Q3's verb blank fitted two of the bank's five words. |
| Leaks | Q13's key helped Q12; Q20's key confirmed Q19's a; Part 5's intro and Q26 carried Q5's key idea; Q11's b and d answered Q27; stretch items 1 and 2 echoed the keys of Q8 and Q13. |
| Arguable keys | Q11 offered a day-level check under "run on every file"; Q25's exhibit said "each order once" beside a payment-level export; Q31's tiebreaker had no direction; Q20's fix failed only on a column the paper never printed; Q15's key also held for C-0185's June and July. |
| Facts | Q27 said the error left five countries "out of one group", where the paper says it excludes them from the analysis and moves three of the four debt groups; Q22's present tense predated the 2020 renaming, which stretch 3 relied on; Q6 said views where TechCrunch's quotation says people; Q11 paraphrased The Register. |
| Wording | Quarters called Q1 and Q2 on a paper whose items are Q1 to Q35; machine-sounding phrases in the purpose and the Part 6 intro; one option pattern, a claim and a reason after a semicolon, used throughout; "35 Business members"; Q13's phrasing; Q29 was one multiplication. |

Later the same day the orchestrating session added two rules: an invented scenario names no real
company, and an item labelled hard takes at least three dependent steps on an exhibit (compute,
compare, then decide), cannot be answered by elimination or by a cue elsewhere on the paper, and
prints its values as a table beside any bar chart that has to be read to an exact value.

### What changed, item by item

| Q | Before | After |
|---|---|---|
| 1 | One correct option, whose key joined the halves of two distractors | A worked answer: what the query prints, the true figures and the change, on the tree, with each quarter named by its months |
| 3 | A verb blank that only "sort" and "guarantee" fitted | A stem edit, proposed in `data/programme/paper_edits.yaml`, whose blank takes a noun, so all five words fit it |
| 5 | Hard: the fact that makes Excel the home, a what-if the room changes, which Part 5 and Q26 echoed | Medium: where a first look at a question belongs, a notebook that reads the warehouse, set against Anand's rule for the reported number |
| 6 | Views, and a cast in the query | The people who played the video, as TechCrunch quotes Facebook; the seconds are decimals, so the query needs no cast that could cue Q1 |
| 8 | Five steps whose pronouns gave the order | Six steps that each stand alone, one of which spoils the report (dropping every order with two payment rows); key e, f, b, c, a |
| 10 | Three checks already marked as passing or failing | The report's figures by channel: the learner works out each gap, finds that web's alone fails, and decides what goes; the Part 2 intro no longer says Anand refuses an unreconciled figure |
| 11 | Day-level checks under "run on every file"; options that answered Q27 | Three labs' files with four counts each, and five per-file checks worked on Lab B; key b, d; The Register quoted in its own words |
| 13 | Hard, with a key that named the tie at fiftieth Q12 asks about | Medium: four rules by name, judged against the head of Retail-Plus's rule, which the Part 3 intro now states |
| 14 | "35 Business members"; a key alone without "because"; options ending in full stops | Customers throughout, members only for Retail-Plus; four options in one form, proposed as an options edit |
| 15 | Options built from the same two sets of members | The calls Marketing makes and the calls that say something untrue, worked from the months; the reason says "fell in both August and September" |
| 16 | Weekly bars, the close given in the stem, two options with "six of its last seven" | Booked so far against plan so far, charted and tabled; the stem gives nothing; no option carries a count |
| 20 | Where the fix belongs, with "validate still on" in the key | Which step keeps each customer's first exposure, on the feed sent newest first, with its three columns printed |
| 22 | Present tense, no renaming, the key the only option with an action | Past tense, the 2020 renaming stated, every option pairing an output with an action; the code counts left_only |
| 23 to 26 | Prompts and techniques shared words | No word shared between a prompt and a technique; Part 5's exhibit prints two rows of the payment-level export |
| 27 | One correct option naming the check Q11 offered; "out of one group" | A worked answer on an illustrative sheet whose average stops at row 5; the paper's own words and its lines 30 to 44 |
| 28 | One row | Three rows, one a falling rate; each option built on its own misreading |
| 29 | Medium, one multiplication | Hard: three trips, the overcharge and its share of the commission charged |
| 30 | Each option an output and a claim | Outputs alone, with the team's bar of 0.5 in the stem |
| 31 | "newest date then run_id first"; "the same thing every morning" | "finished_on descending, then run_id descending"; one row per model; run ids issued in the order runs start |
| 32 | WHERE, GROUP BY and HAVING on seven rows | A HAVING that counts only the rows WHERE kept, set against the lead's question |
| 33 | Two of the four options without the review's conclusion | Every option gives the count and what the review concludes |
| 34 | Medium | Hard, as the sitting found it |
| 35 | The stem gave 2,100 distinct users | A week's visits log; the learner counts |
| Stretch 1 and 2 | Echoed the keys of Q8 and Q13 | Collected revenue week by week; each member's share of the tier's revenue |
| Part 6 | "a company such as Swiggy or Zomato" | "a food-delivery company", invented, with every number illustrative |
| Purpose and intros | Phrases the sitting found machine-made | Plain sentences in the house voice |

Q31 keeps dates for finished_on, where the orchestrating session suggested a timestamp: CLAUDE.md
allows durations only and never clock times in lesson material. The exhibit states that run ids are
issued in the order runs start, so ordering by finished_on descending, then run_id descending keeps
the later of bot-b's two runs of 9 September.

### The hard items, and the steps each takes

| Q | The exhibit | The dependent steps |
|---|---|---|
| 1 | The Retail-Plus tree | Predict the integer division for each quarter (2 and 1); compute the true ratios (2.36 and 1.84); compute the change (a fall of about 22 percent) |
| 6 | The two-average query | Evaluate the CASE for five viewers (3 counted); compute both averages (10.0 and 6.0); measure the overstatement on the defined base (about 67 percent) |
| 7 | The join-count query and the payment rows | Size the LEFT JOIN from four kinds of order (678); count the distinct orders (462); take the unpaid orders' NULLs out of count(p.payment_id) (648) |
| 8 | The payment rows | Tell the 188 instalments from the 28 repeats and leave step d out; put the de-duplication before the sum and the sum before the join; check, then send |
| 9 | The date-filtered LEFT JOIN | Join the three orders' rows (O-1 twice); apply the WHERE, NULL dates included; count and sum what remains (2 rows, Rs 2,400) |
| 10 | The report by channel | Work out three gaps; compare each with its unpaid list; decide what goes and what waits |
| 11 | Three labs' counts | Work each of five checks on Lab B's counts; see which counts were taken after the cut; mark every check that fires |
| 12 | Rows 46 to 53 | Rank through two ties under RANK, DENSE_RANK and ROW_NUMBER; count each list at 50 (51, 52 and 50) |
| 15 | Four members' months | Find the rows LAG reads for each September; apply the flag (four members); check the months against the calendar and count the untrue calls (two) |
| 16 | Booked and plan so far | Take booked less plan at seven points; follow the lead's rise and fall; choose the line that states the close and the trend |
| 20 | The feed sent newest first | Read each repeated customer's two sends and their order; apply each of four steps; keep the one that leaves every first exposure |
| 21 | The pivot and melt code | Average M1's two June orders; melt to four rows with a NaN; sum without the NaN |
| 22 | The gene merge | Keep the lab's four rows; mark the two unmatched rows left_only; choose the action that fixes the source |
| 27 | The sheet whose average stops at row 5 | Average rows 2 to 5 (-0.5); average all six (1.0); state the gap and its sign |
| 28 | Three rows of rates | Compute the sheet's three changes; compute the three the modeller meant; compare, and say what half-size moves do to risk |
| 29 | Three trips | Take each fare after tax and fees; compute the commission due; sum the overcharge (2.00 dollars) and set it against the 23.50 charged |
| 30 | The scoring code | Fan the merge out to 7 rows; mark each row right or wrong; take the mean (0.43) |
| 31 | Five evaluation runs | Find each model's latest run through the tie on 9 September; run each of four queries on the rows; keep the one that returns one repeatable row per model |
| 32 | The replies query | Keep the low ratings in WHERE; count them per model and apply HAVING (bot-a 3); set the result against the lead's question |
| 33 | The NOT IN query | Expand NOT IN against a list that holds a NULL; evaluate the unknown for each conversation; count (0) and read what the review concludes |
| 34 | The running total | Find the peers on 22 September; take the frame's running sum for each call; read it call by call |

### The paper now

35 timed items in six parts, paced at 117 of the 120 minutes: 21 hard at 4 minutes, 12 medium at 2.5
and 2 easy at 1.5, which is 60, 34 and 6 percent.

| Part | Items | Minutes | Easy | Medium | Hard |
|---|---|---|---|---|---|
| 1. Anand's Monday numbers | Q1 to Q6 | 16 | 2 | 2 | 2 |
| 2. Booked against collected | Q7 to Q11 | 20 | 0 | 0 | 5 |
| 3. The protect list and the plan line | Q12 to Q16 | 17 | 0 | 2 | 3 |
| 4. One row per customer | Q17 to Q22 | 19.5 | 0 | 3 | 3 |
| 5. The last mile, and spreadsheets in public | Q23 to Q29 | 22 | 0 | 4 | 3 |
| 6. Read the code, read the data: an AI team's tables | Q30 to Q35 | 22.5 | 0 | 1 | 5 |

Formats: 16 one correct option; 7 scenario-set items in three sets, answered as one letter (Q7,
Q12, Q13 and Q20), a number (Q17), a true or false with its reason as four options (Q18) and every
correct letter (Q19); 1 more-than-one-correct item outside a set (Q11), whose key shares no letter
with Q19's; 2 ordering items (Q2, and Q8 with one step to leave out); 2 word-bank items (Q3 and Q4);
4 match rows (Q23 to Q26); 3 worked answers (Q1, Q27 and Q29).

By what each item asks: 10 read code or a query (Q1, Q6, Q7, Q9, Q21, Q22, Q30, Q32, Q33 and Q34);
15 are solution design, choosing the best fit, sizing, ordering the steps, matching jobs to
techniques or deciding what goes (Q5, Q8, Q10 to Q14, Q17, Q19, Q20, Q23 to Q26 and Q31); the other
10 read a table, a chart or a claim, work a spreadsheet, or recall a rule (Q2 to Q4, Q15, Q16, Q18,
Q27 to Q29 and Q35). Twelve items are set outside Kalpa: six in public cases (Q6, Q11, Q22 and Q27 to
Q29) and six at the invented food-delivery company (Q30 to Q35).

`scripts/distractor_audit.py content/W02/SAT` passes with 23 option items read and keys at a 6, b 7,
c 5, d 6 and e 1. The llm-tic-scrubber scanner reports the paper, the key and the discussion guide
clean.

### The facts checked again on 30 September 2026

| Item | What the paper states now | Source |
|---|---|---|
| Q6 | Facebook defined the average duration of video viewed as total time spent watching divided by "the total number of people who have played the video", and calculated it over "only the number of people who have viewed a video for three or more seconds"; inflation of 60 to 80 percent over two years; billing not affected | TechCrunch, Devin Coldewey, 22 September 2016 |
| Q11 | 15,841 cases between 25 September and 2 October 2020 not included; "some files containing positive test results exceeded the maximum file size" | GOV.UK, PHE statement, 4 October 2020 |
| Q11 | Lab CSV files stored in the older .xls format, 65,536 rows a sheet; "records were simply left off and not counted when imported" | The Register, 5 October 2020 |
| Q22 | In 2020 the HGNC renamed the genes whose symbols Excel turns into dates: MARCH1 became MARCHF1 and SEPT1 became SEPTIN1 | Bruford and colleagues, Nature Genetics, 2020, as before; a summary of the renaming read the same day |
| Q27 | A coding error "entirely excludes five countries, Australia, Austria, Belgium, Canada, and Denmark, from the analysis"; footnote 5, "RR averaged cells in lines 30 to 44 instead of lines 30 to 49"; with other errors it took 0.3 points off the highest debt group, overstated the lowest by 0.1 and understated the second by 0.2 | Herndon, Ash and Pollin, PERI working paper 322, 15 April 2013, page 7, read from the PDF itself |

The pages read for this pass, each checked on 30 September 2026:

- TechCrunch: https://techcrunch.com/2016/09/22/facebook-miscalculation-significantly-inflated-average-video-view-times-for-years/ (checked 30 September 2026)
- GOV.UK: https://www.gov.uk/government/news/phe-statement-on-delayed-reporting-of-covid-19-cases (checked 30 September 2026)
- The Register: https://www.theregister.com/2020/10/05/excel_england_coronavirus_contact_error/ (checked 30 September 2026)
- The PERI working paper, PDF: https://peri.umass.edu/wp-content/uploads/joomla/images/WP322.pdf (checked 30 September 2026)
- Progress Educational Trust, on the renaming: https://www.progress.org.uk/human-genes-renamed-as-microsoft-excel-reads-them-as-dates/ (checked 30 September 2026)

The section above lists the Reinhart and Rogoff lines as not verified, because the PERI PDF it tried
returned 410 Gone; the PDF at the address above opened, and the lines are now quoted from footnote 5.

### The Kalpa numbers added

Recomputed on 30 September 2026 on PostgreSQL 16.13 and pandas 3.0.5 from the room's own files:

- The quarters: 'Q1' holds orders from 1 April to 28 June 2026 and 'Q2' from 1 July to 28 September.
- The report by channel for July to September: app booked Rs 4,25,90,270 and collected Rs 4,25,82,150
  against an unpaid list of Rs 8,120; store Rs 3,21,48,730 and Rs 3,11,90,920 against Rs 9,57,810; web
  Rs 2,36,61,000 and Rs 2,28,72,000 against Rs 7,89,000. Q10 prints web's collected Rs 21,750 lower,
  marked illustrative, so that web's bridge alone fails.
- Joining the de-duplicated payment rows before summing them returns 650 rows, the 462 orders plus
  188 second instalments (Q8).
- Business carries 99 percent of the quarter's revenue (Q14's reworded stem).
- Booked so far and plan so far, in Rs crore, at the end of the weeks starting 6 July, 20 July, 3
  August, 17 August, 31 August, 14 September and 28 September: 0.51, 4.22, 5.95, 6.87, 7.54, 9.12 and
  9.84 against 0.76, 2.27, 3.78, 5.30, 6.81, 8.33 and 9.84 (Q16).
- Friday's raw export carries each order's order_amount on every payment row; order KR-00028's two
  rows read Rs 6,35,000 with Rs 3,81,000 and Rs 2,54,000 paid (Part 5's exhibit).
- The exposure feed sent newest first puts C-0001's and C-0002's 11 August sends before their 3
  August sends (Q20); every other value in Q20's exhibit is the feed's own.

### The proof

`content/W02/SAT/internal/C2_W02_SAT_key_proofs_INTERNAL.py` now also reads every table exhibit
back from the source file and works it: the channel gaps, the five checks on Lab B, the calls and
the untrue calls, the running totals behind the chart, the feed sent newest first under each of the
four steps, the sheet's average, the three rates, the three trips and the visits log. Its run on 30
September 2026 on PostgreSQL 16.13, pandas 3.0.5 and Python 3.11.15 printed 35 PASS lines, Q1 to Q35,
and "RESULT: PASS (35 items proved)", and dropped its scratch schema.

### The Word files

Rebuilt with `python3 scripts/build_saturday_paper.py W02 --docx` and read page by page through
LibreOffice on 30 September 2026: the paper runs to 21 pages and the key to 21. Every exhibit prints
on the page of the item that reads it; the chart in Q16 prints with its table of values beneath it;
the visits log prints across the page, so Q35 shares a page with Q33 and Q34; the stretch page holds
the four written follow-ups; and the answer sheet is page 21 alone. Pages 7, 13 and 16 end a part
between a third and a half full, because each part starts on a new page.

### Open points for the orchestrating session

- `python3 scripts/verify.py content/W02/SAT` passes with no failure. `python3
  scripts/sync_programme.py --check` reports no Week 2 file stale and still reports Week 1's paper
  and key as stale; they belong to the Week 1 session and were not touched here.
- Three edits in `data/programme/paper_edits.yaml` are proposed and await the Programme Head: bank
  2's stem, and bank 27's stem and options.
- Bank 28 and bank 23 go to the tracker as the two issues written above.

## 30 September 2026, version 3 raised again: the second sitting and the calibrated test

A second fresh sitter, who had seen neither the key nor the first sitting's findings, sat the raised
paper the same day. The orchestrating session relayed what held, what it found, and a calibrated test
for the word hard. This section records both and what changed on branch `w02-sat-v3`; it supersedes
the tables above where they differ. The findings name items by the numbers the sitter read, Q1 to
Q35; the tables below give both numbers.

### The calibrated test

A hard item makes a trainee combine at least two ideas on an exhibit, such as an idiom and the
business decision it changes, or take several dependent steps on it, and nothing else on the paper
answers it. A single idiom, a single judgement, or arithmetic the stem sets up is medium. Every
label on the paper was set again against this test, and the count is reported against the bar of
60 percent hard whatever it came to.

### What the second sitting found

| Kind | Finding |
|---|---|
| Held | The keys hold, the public cases are correct, and the option lengths and key positions are clean. |
| Cues in the openings | Part 2 said "decide what leaves when a check fails", Part 3 "rank within a segment", Part 4 "read a pivot that averages" and "a key that changed on its way in", and Part 6 "catch the week's traps". |
| Cues in the stems | Q1 asked for "the true figures"; Q15's caption said a blank month has no row; Q20 said the feed runs newest first; Q22 printed both conversions and the SEPT2 to SEPT1 switch; Q28 described the sum-against-average mechanism; Q30 said two tickets carry their label twice; Q33 said the log gained a NULL row; Q31's caption said how run ids are issued. |
| Shared key parts | The option sets of Q6, Q7, Q15, Q30 and Q32 repeated parts of the key across options, so half of each key came free. |
| Leaks | Q8's step c and Exhibit 2D's "Rows out of the join, 462" answered Q7 and Q8; Q18's option d and Q19's option e gave away Q17's arithmetic; Q12's working and the Part 3 opening answered Q13; Q2 drilled the clause order Q32 tests. |
| Arguable keys | Q8's steps b and c; Q5's heading, and a key whose reason did not hold; Q25 did not say booked or collected; Q31 did not define "latest" within a day, and its run ids, r1 to r5, would sort as text once a tenth run came, with no clock time to be added; Q10's rule for a late failure was not in the stem. |
| Consistency | Q16's last point needed labelling as the close, and its peak sits in the fortnight to 9 August at Rs 2.17 crore; Q14's stem gave Business's 99 percent share as the reason all 35 Business customers made the list. |
| Compound | Q7, Q15, Q16, Q22, Q28, Q30, Q33 and Q34 each turned on one idea or a cue, and their options needed each to carry a whole misreading. |

### What changed, item by item

| Before | Now | What changed |
|---|---|---|
| Q1 | Q1 | "The true figures" is gone; the stem asks what the note to the head of Retail-Plus should say orders per member did, and the key is that note: it prints 2 and 1, and orders per member fell about 22 percent, from 2.36 to 1.84. |
| Q2 | Q30 | Bank 57, the clause-order drill, is folded into the replies item, whose reason gives the whole logical order, so no printed item hands over the order Q30 tests. |
| Q3, Q4 | Q2, Q3 | Unchanged; Q2 keeps its proposed stem edit. |
| None | Q4 | New, medium: the average over a LEFT JOIN on Retail-Plus's 120 members on the books, 76 of whom ordered; avg skips the 44 NULL spends and prints 5439, where the head asked for 3445. |
| Q5 | Q5 | Headed "Choose where it runs"; the key is a notebook that reads the warehouse, because the weekly chart is none of the Monday figures Anand's rule governs, a reason that holds. |
| Q6 | Q6 | The options are overstatements alone, each its own misreading: 40 percent on the wrong base, 50 percent from the long viewers, none, and the key, about 67 percent. |
| Q7 | Q7 | Four pairs that share no number: 678 and 648 (the key), 462 and 432, 650 and 620 (the repeats collapsed first), 686 and 656 (the orphans joined). Exhibit 2D no longer prints the report's row count. |
| Q8 | Q8 | Step b reads "LEFT JOIN the quarter's 462 orders to each order's collected figure" and step c "Check that the result has one row for each of the 462 orders, and that each channel's gap equals its unpaid orders' booked value", as the orchestrating session wrote them. |
| Q9 | Q9 | Unchanged. |
| Q10 | Q10 | Anand's rule, send what reconciles and hold what does not, is in the stem. With the rule stated, the item is arithmetic the stem sets up and one stated judgement, so it is relabelled medium at 3.5 minutes. |
| Q11 | Q11 | The options are reordered and the key is c, e, so key positions stay spread. |
| Q12, Q13 | Q12 | One item: old Q12's counts and the rule in the Part 3 opening together answered old Q13, so the two are merged, the head's rule sits only in the stem, and one letter names the ranking and its count through the two ties (RANK, 51). |
| Q14 | Q13 | Bank 27, with its proposed stem and options; the stem's reason is now that the smallest Business spend, Rs 2,25,000, is ten times the largest retail spend, Rs 21,740, where it said Business carries 99 percent. |
| None | Q14 | New, medium: each member's share of the tier's spend, with the window OVER () against GROUP BY, a running ORDER BY and a partition by member. |
| Q15 | Q15 | The caption no longer says a blank month has no row; member_month is described as it is built, and the options are four whole readings of the calls and the untrue calls. |
| Q16 | Q16 | The last point is labelled "Close, 30 Sep" on the chart and in its table; the stem gives the close, so every option agrees on it and the options differ only on the path; the key is the peak in the fortnight to 9 August, about Rs 2.2 crore, and about Rs 0.8 crore ahead on 20 September. |
| Q17, Q18, Q19 | Q17 | One item: how many rows the merged table holds and what the refresh should carry, four pairs that share nothing (346 and validate, the key; 340 and nothing; 352 and drop_duplicates; 136 and indicator). The true-or-false and the guards item that gave away the count are gone. |
| Q20 | Q18 | "Newest first" is gone from the stem; the exhibit prints the feed in the order the tool sends it and the step the refresh runs on it (see the next section). |
| Q21 | Q19 | Five orders; the options share no printed value with the key (2000.0 4 5600.0). |
| Q22 | Q20 | The conversion pairs and the SEPT2 to SEPT1 switch are gone; TP53 sits on two panels in the reference table, so the merge fans out as well as missing the two dates: 5 rows, 3 panels. |
| Q23 to Q26 | Q21 to Q24 | Q23's job reads "Booked revenue by segment". |
| Q27 | Q25 | Two columns, high-debt years and other years; B8 stops at row 5, so the sheet reports -0.5 against 1.5, and over all six countries both average 1.5. The stem cites the PERI abstract, -0.1 published against 2.2 recalculated. |
| Q28 | Q26 | A worked answer. The stem gives the documentation's definition and no mechanism; the learner finds that column D divides by the sum, halving every change, and that a value at risk moving with the changes should read 140 million dollars, over the 120 million limit. Both figures are labelled illustrative, since none comes from the task force report. |
| Q29 | Q27 | CBS News's wording: a refund of about 900 dollars a driver, interest included; the terms set the commission on the fare after taxes and fees. |
| Q30 | Q28 | The stem no longer says two tickets carry their label twice; each option pairs a printed accuracy with what happens to the model. |
| Q31 | Q29 | The stem defines the latest within a day as the run that started later, run ids are numbers issued in the order runs start, and no clock time appears; each option names a query and the call it gives. |
| Q32 | Q30 | The lead will retrain every model on the list; the options give the rows and the models retrained. |
| Q33 | Q31 | The stem no longer mentions the NULL row; the product lead cuts the budget below 40 percent, so the count decides the budget. |
| Q34 | Q32 | The finance partner routes calls to a cheaper model once tokens_so_far passes 1,000, so the peers decide which call is routed first. |
| Q35 | Q33 | Unchanged. |
| Part openings | Parts 1 to 6 | Each opens on the business situation alone, and each part's line says what it shows about the work, never the trap. |
| Stretch 3 | Stretch 3 | The renaming is stated without naming a gene. |

### Cues found on this pass's own read

Read against the calibrated test after the rebuild, four items still carried a cue, and each was
rewritten before the push:

- **Q18.** Its key restated the rule's own words, "sort by exposed_date from the earliest", so a
  learner could match it to "the first by date" without reading the exhibit. The exhibit now prints
  the step the refresh runs, `drop_duplicates(subset="customer_id")`, and the item asks which
  exposure it keeps for C-0001 and what the sale's report, which credits orders from the exposure on,
  makes of C-0001's orders. The key is the 11 August send, so the orders placed in the eight days
  before it go uncredited; on the week's book that is C-0001's order of 6 August, Rs 1,200. The
  sort is the item's answer line.
- **Q28.** The key read "0.43, so a model right on three of its five tickets is held back", a clause
  that announced the trap, and it was the only option in which the model did not ship. The options
  now share one form, figure and decision, and a fourth misreading, that pandas refuses repeated keys
  with a MergeError, also leaves the model unshipped.
- **Q30.** The key alone carried a consequence. Every option now gives the rows the query returns and
  the models the lead retrains.
- **Q32.** The key began "Call 2, although", a word that flagged it. The options are the four calls
  alone.

### The hard items against the calibrated test

21 of the 33 timed items are hard, 64 percent, against the bar of 60 percent. Each combines two
ideas on its exhibit or takes dependent steps on it:

| Q | The exhibit | What it combines, or the steps it takes |
|---|---|---|
| 1 | The Retail-Plus tree | Integer division (it prints 2 and 1), then the true ratios, then the note to the head of Retail-Plus |
| 6 | The two-average query | A CASE with no ELSE inside count, then both averages, then the overstatement on the defined base |
| 7 | The payment rows and the join-count query | The fan-out, the unpaid orders' NULL rows, count(column) skipping them, and the orphan payments a LEFT JOIN from orders never meets |
| 8 | The payment rows | The step that spoils the report, then the order the other five must run in |
| 9 | The date-filtered LEFT JOIN | The fan-out of O-1's instalments with the WHERE that drops the NULL and out-of-quarter rows |
| 11 | Three labs' counts | Where the truncation happens in the chain, then each of five checks worked on Lab B |
| 12 | Rows 46 to 53 | The head's rule mapped to a ranking, then the ranks through two ties |
| 15 | Four members' months | LAG reads rows, then the calls it makes, then which calls are untrue |
| 16 | Booked and plan so far | The lead at seven points, its peak and its date, the value on 20 September, then the line that holds |
| 17 | Monday's refresh | The fan-out on a repeated right key (346 rows), and the guard that stops it before the pivot |
| 18 | The feed and the refresh's step | drop_duplicates keeps the first row as the file lists it, the file lists the later send first, then what the credit rule does to the orders between the sends |
| 19 | The months view | pivot_table's mean, melt's NaN row, and sum skipping it |
| 20 | The gene merge | A repeated symbol that fans the merge out, and two dates that match nothing |
| 25 | The sheet whose average stops at row 5 | The range audit, the recomputation, then whether the comparison holds |
| 26 | Three rows of rates | The formula against its definition, the half-size change, then the value at risk against the limit |
| 27 | Three trips | The base the commission was charged on, the commission due, the overcharge, then its share of the commission charged |
| 28 | The scoring code | The fan-out on repeated labels, the accuracy it prints, then the ship bar |
| 29 | Five evaluation runs | The business's tiebreak within a day, the query that applies it, then the promotion call |
| 30 | The replies query | WHERE before HAVING, then the lead's list and the model left unretrained |
| 31 | The NOT IN query | NOT IN against a NULL, then the budget rule on the count |
| 32 | The running total | The peers under the default frame, then the first call routed |

Four labels are the ones a third sitting is most likely to argue, and each stays hard for the reason
given: Q17, whose options are whole misreadings, so a learner who sizes the merge at 346 needs the
guard only to confirm it; Q11, whose five judgements are each short, though the key needs every one;
Q16, where the arithmetic is subtraction, though the stem sets none of it up; and Q27, where the
stem states the terms and the learner still has to find the base the commission was charged on. If
all four were read as medium, the paper would hold 17 hard items, 52 percent.

### The paper now

33 timed items in six parts, paced at 113 of the 120 minutes: 21 hard, 10 medium and 2 easy, which is
64, 30 and 6 percent.

| Part | Items | Minutes | Easy | Medium | Hard |
|---|---|---|---|---|---|
| 1. Anand's Monday numbers | Q1 to Q6 | 16 | 2 | 2 | 2 |
| 2. Booked against collected | Q7 to Q11 | 19.5 | 0 | 1 | 4 |
| 3. The protect list and the plan line | Q12 to Q16 | 17 | 0 | 2 | 3 |
| 4. One row per customer | Q17 to Q20 | 16 | 0 | 0 | 4 |
| 5. The last mile, and spreadsheets in public | Q21 to Q27 | 22 | 0 | 4 | 3 |
| 6. Read the code, read the data: an AI team's tables | Q28 to Q33 | 22.5 | 0 | 1 | 5 |

Formats: 18 one correct option; 3 scenario-set items in two sets, each one letter (Q7; Q17 and Q18);
1 more-than-one-correct item (Q11); 1 ordering item with one step to leave out (Q8); 2 word-bank
items (Q2 and Q3); 4 match rows (Q21 to Q24); 4 worked answers (Q1, Q25, Q26 and Q27). Twelve items
are set outside Kalpa: six in public cases (Q6, Q11, Q20 and Q25 to Q27) and six at the invented
food-delivery company (Q28 to Q33).

Three bank items print (2, 3 and 27) and 55 fold into deeper items, each with its reason in the key.
`scripts/distractor_audit.py content/W02/SAT` passes with 22 option items read and keys at a 6, b 6,
c 5, d 5 and e 1. The llm-tic-scrubber scanner reports the paper, the key and the discussion guide
clean.

### The facts checked again on 30 September 2026

| Item | What the paper states now | Source |
|---|---|---|
| Q25 | The paper's average growth for countries with public debt over 90 percent of GDP, published as -0.1 percent, was 2.2 percent when properly calculated | Herndon, Ash and Pollin, PERI working paper 322, April 2013, the abstract and page 7 |
| Q26 | The model ran through Excel spreadsheets filled by copying and pasting; the error "likely had the effect of muting volatility by a factor of two and of lowering the VaR". The quotation is corrected to the report's words; the value at risk and the limit on the paper are illustrative | Report of JPMorgan Chase and Co. Management Task Force Regarding 2012 CIO Losses, 16 January 2013, pages 123 and 128 |
| Q27 | Uber would refund each affected New York City driver about 900 dollars, interest included, having calculated its commission "based on gross fares, before any taxes and fees were deducted" | CBS News, 24 May 2017 |
| Q20 | Excel's default settings turn some gene symbols into dates, and about a fifth of genomics papers with Excel gene lists carried such errors | Ziemann, Eren and El-Osta, Genome Biology, 2016 |

The addresses are the ones listed in the sections above, each checked on 30 September 2026.

### The Kalpa numbers added

Recomputed on 30 September 2026 on PostgreSQL 16.13 and pandas 3.0.5 from the room's own files:

- Retail-Plus has 120 members on the books; 76 ordered from July to September and spent Rs 4,13,380,
  so the average over those who ordered is Rs 5,439 and over the books Rs 3,445 (Q4).
- The 35 Business customers who ordered in the quarter spent at least Rs 2,25,000 each, and the
  largest retail spend was Rs 21,740, a Retail-Plus member's (Q13).
- Joining the orders to the payment rows gives 678 rows and 648 payment rows; collapsing identical
  payment rows first gives 650 and 620 (Q7).
- The lead of booked over plan at the chart's seven points: -0.25, 1.95, 2.17, 1.57, 0.73, 0.79 and
  0.00 crore; the week of 13 July booked Rs 2,66,28,920, and six of the seven weeks from 10 August
  booked below the plan's Rs 75.69 lakh a week (Q16).
- C-0001's two sends in the exposure feed are on 3 and 11 August, and its order of 6 August for Rs
  1,200 falls between them (Q18).

### The proof

The proof script reads every exhibit back from the source file and runs it, and each distractor's
reading beside it. Its run on 30 September 2026 on PostgreSQL 16.13, pandas 3.0.5 and Python 3.11.15
printed 33 PASS lines, Q1 to Q33, and "RESULT: PASS (33 items proved)", and dropped its scratch
schema.

### The Word files

Rebuilt with `python3 scripts/build_saturday_paper.py W02 --docx` and read page by page through
LibreOffice on 30 September 2026: the paper runs to 22 pages and the key to 22. Every exhibit prints
on the page of the item that reads it; Q16's chart and its table of values print together above the
item; Q18's exhibit prints the feed with the refresh's step beneath it; the stretch page holds the
four written follow-ups; and the answer sheet is page 22 alone, with six boxes for Q8's five letters.
Pages 5, 8, 14 and 17 close a part with space left, because each part starts on a new page.

### Open points for the orchestrating session

- The proposed edits in `data/programme/paper_edits.yaml` still await the Programme Head: bank 2's
  stem, and bank 27's stem and options.
- Bank 28 and bank 23 go to the tracker as the two issues written above.
- The Week 1 paper and key are still stale under `python3 scripts/sync_programme.py --check`; they
  belong to the Week 1 session and were not touched here.

## 1 October 2026, standard v3: every part named by its question, the paper in line with the rebuilt week, and one review

This pass raises the paper to standard v3 under decisions `question-ladder`, `self-contained` and
`humanizer` in `data/programme/facts.yaml`, against the Week 2 packs as merged on main on 1 October
2026 (#220, #221, #222, #217 and #219), on branch `w02-sat-ladder` from main at 3ed8bf1. The paper's
items, levels and minutes, set on 30 September 2026 after two blind sittings, stay; this pass changes
wording and part names, brings every repeated number, term and rule in line with the rebuilt week,
and fixes what one fresh review found. The paper's own decisions are `saturday-interview-grade`,
`saturday-real-cases`, `saturday-edits-w1-w2`, `w2-set1-fold` and `plants-once-found`. No key moved.

### The part questions

| Part | The question it asks | Who needs the answer, as the opening says it |
|---|---|---|
| 1 | Can the warehouse give Anand Monday numbers that his analyst can audit line by line? | Anand, who signs the Monday sheet after his analyst audits every query in the Monday suite, and the head of Retail-Plus, whose retention budget follows the tier's line, so a ratio or average that counts the wrong people sends it the wrong way |
| 2 | Can Anand sign what Kalpa collected against what it booked, with nothing lost or counted twice? | Anand, who signs the collected figure for the CEO's Monday page, and his collections team, who ring every customer on the unpaid list, so a dropped order goes unchased and a payment counted twice shows cash never received |
| 3 | Which members should Marketing protect and call, and did July to September keep pace with the plan? | The marketing lead, whose retention budget, a call and a renewal offer, goes to the members the lists name, and Meera, who decides at mid-quarter whether to hold the plan, push a campaign or move budget, where a false gap sends Marketing after it with discounts |
| 4 | What must Monday's customer table check before the growth team acts on it? | The growth team, who send win-back codes and first-order nudges straight from the table with no analyst watching, so a missing customer gets no offer and a customer counted twice inflates every total |
| 5 | Which numbers in Monday's workbook can a director trust, and where did three public cases go wrong? | The directors, who read the front page first and may read nothing else, and the head of Retail-Plus, who sizes each city's retention budget from the protect list in the room, so a wrong total with nothing red beside it becomes a decision or a budget before any analyst sees it |
| 6 | Can a food-delivery company's AI team trust the numbers behind its model and budget decisions? | The team lead, who decides which model ships and which is retrained, the product lead, who sets the assistant's budget, and the finance partner, who pays the bill by the token; Exhibit 6A draws who acts on which table |

Parts 4 and 5 carry the names the review gave them (below): Part 4's first name, "Can the growth
team act on Monday's table of 340 customers without checking it first?", answered itself, and
Part 5's, "Which spreadsheet numbers can a director trust, in Monday's workbook and in three public
cases?", called Uber's commission a spreadsheet.

Read alone and in order, Parts 1 to 4 tell the week, from the Monday numbers in the warehouse, to
collected against booked, to the protect list and the plan, to the growth team's table; Part 5
carries the last mile to a director and to three public cases, and Part 6 carries the same
checks to an invented AI team. Each opening quotes the stakeholder in the words the week's notes
give, and each part's "what it shows" line now says what it shows about the learner.

### The paper against the Week 2 packs on main

Checked on 1 October 2026 against each day's day sheet, plant table and study notes on main at
3ed8bf1, and recomputed on the warehouse (`content/W02/D1/data/C2_W02_D01_warehouse_v4_STUDENT.sql`,
whose rows have not changed since the paper's last build; only its header comment did), Thursday's
exposure feed and Friday's two exports. Every number the paper prints still matches the week; the
changes are terms, quotations, rules and the labels of the plan weeks.

| Q or place | Before | After | Where the week has it |
|---|---|---|---|
| Part 1 opening | Anand: "Compute them from the warehouse itself. No notebooks, no exports, nothing a person can mistype." | Anand's words as Monday gives them: "I want these numbers every Monday, for every segment and channel, computed from the warehouse itself. No notebooks, no exports, nothing a person can mistype."; revenue defined as booked revenue, every order at its amount, whatever its status; the book and the Monday suite named | Monday's notes, opening and glossary |
| Part 2 opening | Booked as "the value of the orders customers placed", collected as "the cash that actually arrived"; Anand's ask reworded to "from July to September" | Anand's Tuesday words in full, the platform lead's "the payments feed sometimes double-posts when the gateway retries", collected as the cash that arrived, each payment counted once, a gateway retry as the same instalment of the same order posted twice, and the bridge from booked to collected | Tuesday's notes, the picture and the glossary; morning deck S2 |
| Part 3 opening | The marketing lead's ask reworded; the plan line as "the revenue the growth plan expects by the end of each week", which is plan to date | The marketing lead's words in full; the plan line as Rs 75,69,230 for each of 13 plan weeks starting on Mondays from 6 July; plan to date and booked to date as accumulations to the end of the week read | Wednesday's notes, opening and "what the asks measure" |
| Part 4 opening | A quotation from the data platform lead that no Week 2 file carries; "Marketing chooses"; recency as "days since the last order"; "monetary value" | The growth team's words, with the data platform lead, as Thursday gives them; recency counted to the data's last date, 28 September 2026; frequency and spend; the growth team decides who gets an offer | Thursday's notes, opening and chapters 1 and 6 |
| Part 5 opening | The chief of staff's words cut and reworded, "by member code" | The chief of staff's words in full, "by id" and "Nothing that needs Python" included | Friday's notes, opening |
| Q4 | "the average spend per member on the books" | "the average spend across all 120 members on the books, whether they ordered or not", since Monday's "spend per member" averages over the 107 who bought in either quarter; 5439 and 3445 unchanged | Monday's notes, chapter 4 and glossary |
| Q7, Exhibit 2A | "28 have two identical rows"; "2 identical rows, the gateway's repeat" | "28 have two rows that differ only in payment_id, because the gateway retried and posted instalment 1 twice"; "instalment 1 posted twice, a retry". The warehouse's payments carry a primary key, payment_id, and all 50 retries differ in it alone | Tuesday's glossary, "Gateway retry"; the warehouse |
| Q10 | The rule "send what reconciles and hold what does not" | Tuesday's chapter 6 rule: booked always leaves, because it ties to the orders table alone; a collected figure that does not reconcile never leaves, and an open line goes with the report naming the failed check, what it means and when it will close; a channel's collected reconciles when its gap equals its unpaid orders' booked value. Key c unchanged | Tuesday's notes, chapter 6; afternoon deck S17 |
| Q11, Exhibit 2E | "Records in the lab's CSV", and option c on records | "Rows in the lab's CSV", and option c on rows, since the week counts rows sent against rows loaded and Tuesday tells the case with the BBC's account that each result took several rows. Key c, e unchanged | Tuesday's notes, chapter 3; Thursday's notes, chapter 6 |
| Q12, Exhibit 3A | The head of Retail-Plus quoted as saying "rank them the same. Keep every member who spent at least as much as the fiftieth, and nobody who spent less"; "Row" and "rows 1 to 50" | The head's words as Wednesday gives them, "Ties matter. If two members spent the same, I want them ranked the same, and I want to know how many made the top fifty, not forty-nine because of a tie", with the cut at the fiftieth member's spend stated outside the quotation; "Place" and "places 1 to 50". Key d, 51, unchanged | Wednesday's notes, opening and chapter 3 |
| Q16, Exhibit 3C | Readings labelled "Up to 12 Jul" to "Close, 30 Sep"; "booked so far" and "plan so far"; options dated 26 July, 9 August, 6 and 20 September; "one line for Monday's front page" | Readings labelled by plan week, "6 Jul" to "28 Sep, the close", as Wednesday's table names them; "booked to date" and "plan to date"; the caption says the first plan week carries the orders of 1 to 5 July; options dated by plan week (20 July, 3 August, 31 August, 14 September); "one sentence", since the week keeps "line" for the cut-off and the plan line. Key c and every value unchanged | Wednesday's notes, chapter 5; day sheet, the running total |
| Q16 reason | The leads -0.25, +1.95, +2.17, +1.57, +0.73, +0.79, 0.00 crore; Rs 75.69 lakh a week | The same leads, read from the table, with the exact Rs 1,57,51,980 in the week of 17 August and Rs 79,70,130 in the week of 14 September beside them; Rs 75,69,230 a week | Wednesday's day sheet, the running total |
| Q18 | "Marketing's rule is one exposure per customer" | "The growth team's rule", with the reason giving Thursday's sequence: sort by date, keep the first, merge with validate | Thursday's notes, chapter 2 |
| Q19 reason | "the orders fell 29" | "fell 29.4", Thursday's chapter 3 | Thursday's notes, chapter 3 |
| Q21 | "Find any member by member code" | "Find any member by id", the chief of staff's word | Friday's notes, opening and chapter 3 |
| Key reasons | Traps cited by rounds: Monday's round 2 and round 3, Tuesday's round 1 and round 3, Wednesday's round 1 and "Wednesday's trap", Thursday's round 3 | The chapters the rebuilt week stages them in: integer division, Monday's chapter 3; the skip in avg, Monday's chapter 4; the fan-out, Tuesday's chapter 2; the WHERE that empties the unpaid list, Tuesday's chapter 4; the whole book numbered once, Wednesday's chapter 2; DENSE_RANK's 52, Wednesday's chapter 3; the averaging pivot, Thursday's chapter 3 | Each day's day sheet, the trap table |
| Q30 reason | "The logical order is FROM ... ORDER BY" | Monday's run order, with LIMIT seventh | Monday's notes, the run order |
| Stretch 1 answer | "an order paid in two instalments adds to collected in two different weeks" | On Kalpa's book every paid order was paid within two days of its order and both instalments land on the same day, yet 169 of the 648 payment rows on July to September orders fall in a week other than their order's | Tuesday's day sheet; the warehouse |
| Stretch 2 answer | No count | 60 of the 107 Retail-Plus members who bought did so in both quarters | Monday's notes, chapter 5 |

The figures the paper repeats and the week confirms, unchanged: the Retail-Plus leaf (215 and 140
orders, 91 and 76 members, Rs 2,725 and Rs 2,953 an order, 2.36 to 1.84, down 22.0 percent); the
LIMIT sample, Rs 3,900 then Rs 4,590; 120 members, Rs 4,13,380, 5439 and 3445; the quarter's 462
orders and Rs 9,84,00,000; 216, 188, 28 and 30 orders by payment rows and 8 orphans; 678 and 648;
Rs 20,750 posted twice and Rs 17,54,930 unpaid; each channel's booked, collected and unpaid list;
the tie at fiftieth (C-0185 and C-0242 on Rs 3,350, C-0189 and C-0206 on Rs 3,480, C-0259 on
Rs 3,200; 50, 51, 52 and 49); 35, 11, 4 and 0 on the whole-book list; Rs 2,25,000 and Rs 21,740; the
four members' months; booked and plan to date at the seven readings; 340 customers, Rs 19,84,00,000,
136 feed rows for 130 customers, 346 rows and Rs 45,800; C-0001's sends of 3 and 11 August and its
order of 6 August, Rs 1,200; C-0194's Rs 16,740 for C-0195; Mumbai's Rs 1,56,790 against
Rs 7,14,890; Rs 39.41 crore, 1,400 rows and Rs 19.84 crore; Rs 5,00,000 typed, down 14.6 against
29.4; 244, 227 and 301 buyers; Rs 19.84 crore, Rs 9.84 crore and down 1.6 percent on the card.

### What the paper needed to stand on its own

- Terms explained where they first appear: booked revenue, the book and the Monday suite (Part 1);
  the tree's three leaves (Exhibit 1A); collected, the gateway and a gateway retry, and the bridge
  (Part 2); the open line and when a channel reconciles (Q10); places (Exhibit 3A); the plan line,
  the plan week, plan to date and booked to date (Part 3 and Exhibit 3C); recency, frequency and
  spend, the data's last date and the monsoon sale (Part 4); gene panels (Q20); GDP (Q25); the
  token (Part 6).
- Q4 states its base in the stem, all 120 members whether they ordered or not, so the item no
  longer leans on what "per member" means in Monday's files.
- No stem sends the reader to a class file. The key's reasons name the day and chapter where the
  room met each trap, for the trainer; the STUDENT paper names none.

### What the humanizer's read changed

- In the paper: the purpose no longer says the paper "finds which of those decisions you can make
  cold" and names the six public cases as such; the company row names every role an item uses;
  Part 6's opening names who acts on each number and which decision it feeds, worded so that it
  names no item's trap; Q33's product manager is the product lead the opening introduces.
- In the key: every wrong-option reason now has a subject, where most had opened on a bare verb
  ("Reads ...", "Assumes ...", "Counts ..."), and the openings vary inside each item; the closers
  "what the database withholds is the promise" (Q2), "raising a limit only moves the cliff" (Q11),
  "so it is read the way it was meant" (Q16), "fails without a sound" (Q25) and the "Yes to ...; no
  to ..." pair (Q24) became plain statements; "quietly" left Q6's and Q18's interview lines; and
  Q31's option (a) reason was reworded where the verify sweep read it as the banned contrast.
- In the guide: the opening no longer claims that SQL carries more interview weight than any other
  skill; the most-missed table names each miss in a sentence, as Week 1's guide does; the schedule
  cells, anchor 6's "A window.", anchor 7's "validate, set to ..." and anchor 8's "Upstream of the
  pivot ..." became sentences; the closer "Three hundred minutes in all ..." became a plain line;
  the board's two-fragment slogan became one sentence.
- Builder lines stay as the builder writes them, since this pass writes only under
  `content/W02/SAT/`: "as a guide, not a limit", "never an obscure fact", "the most useful thing
  this paper produces", the Set headings and the rules on the first page.

### The plant rule

Decision `plants-once-found` lets this paper name a planted value only when the room found it in
class. Every planted value the STUDENT paper names was found in class.

| Plant | Where the paper names it | Found in class |
|---|---|---|
| 30 unpaid Q2 orders and 28 gateway retries (Rs 17,54,930 and Rs 20,750) | Set 1 (216, 188, 28, 30), Q7, Q8's steps, Exhibit 2D's unpaid lists | Tuesday, chapter 4's empty cells, where each learner runs the Kalpa lists |
| 8 payments with no order | Set 1 and Exhibit 2A | Tuesday, chapter 4's your-turn cell |
| The tie at fiftieth in Retail-Plus, C-0185 and C-0242 on Rs 3,350 | Exhibit 3A and Q12 | Wednesday, chapter 3's own-run cell (S46) and the case's part 1 |
| C-0161 and C-0171, whose spend fell in each month | Exhibit 3B and Q15 | Wednesday, chapter 6's last your-turn cell and the case's part 2 |
| C-0216 and C-0185 stepping over an empty August | Exhibit 3B and Q15 | Wednesday, chapter 6 (C-0216 on S10; the seven flags over an empty month on S12) |
| The six re-sent exposures, 136 rows for 130 customers, and C-0001's and C-0002's sends | Set 2, Exhibit 4A, Exhibit 4B, Q17 and Q18 | Thursday, chapter 2's your-turn cell, where the room ran the merge on Kalpa's feed |
| The raw export at the payment grain, KR-00028's two rows | Exhibit 5A and Q23 | Friday, chapter 2 |

The plants the paper does not name: the bulk order KR-00667, Wednesday's third falling member
C-0175, and Friday's missing member C-0170 and its lookup on C-0169. Tuesday's day sheet keeps 188
from 216 and 648 from 678 apart in Tuesday's learner files; the Saturday paper prints them together
because the room computed both in class.

### Option lengths

After the relabelling of Q16 its key was the longest option, 119 characters against 115, and the
audit failed it; option (d) was lengthened, and after the review it reads "The lead grew at every
reading from the week of 20 July to the week of 14 September, and the quarter closed level with the
plan", 127. The review then found four keys that were the lone shortest option, and each now has
company: Q4's key reads "who placed an order", 57 characters against 51 to 60; Q12's options (a)
and (d) both end on 51 members, so its key is 65 against 64 to 83; Q14's option (d) is a query of
the key's own length, 70; and Q30's option (a) reads "each beside its low ratings", 71, so the
key's 74 sits between. Across the 21 single-letter items the key ties for longest in four (Q7, Q9,
Q19 and Q20, whose options are numbers of one length), ties for shortest in four (Q14, Q17, Q32 and
Q33) and sits between in thirteen, and it is never the lone longest or the lone shortest. Key
positions across the 22 lettered items: a 6, b 6, c 5, d 5 and e 1.

### The review

One fresh reviewer, read-only, on 1 October 2026: a blind sitting from the STUDENT paper with every
code exhibit run on pandas 3.0.6 and Postgres 16, a read of the part headings alone, every number,
quotation and chapter reference against the packs on main, and a language read against the
humanizer's patterns. The blind sitting agreed with the key on all 33 items. It found no blocker and
no wrong key, six major findings and the rest minor. Every finding was fixed or answered below, and
no key moved.

| Finding | Weight | What changed, or why it stands |
|---|---|---|
| Q32: "routes every call to a cheaper model once tokens_so_far ... passes 1,000" can be read as a moment after which later calls are routed, which makes (b) right | Major | The stem now routes "every call whose tokens_so_far, read from the query above, is over 1,000" and asks which is the first call routed; key (a) stays, and option (b)'s reason says call 3 is first only if each row takes its own step |
| Q12: each option paired its function with that function's true count, so only (d) said 51, which anyone counts off Exhibit 3A | Major | Option (a) now reads "DENSE_RANK, keeping every member ranked 50 or better: 51 members" and (d) "RANK, keeping every member whose rank is 50 or better: 51 members", so the count narrows the item to two options and the choice turns on what DENSE_RANK does after the tie at 48; key (d) stays; the reasons, the guide's row and a proof assertion (option a claims 51, DENSE_RANK's cut keeps 52) follow |
| Q28 (d): "since two tickets repeat in the labels" handed over half of a Hard item | Major | (d) reads "A MergeError, since the two frames differ in length, so the model waits"; its reason says frames of different lengths merge without complaint, and the proof merges the exhibit's 5 and 7 rows to 7 with no error |
| Part 5's heading and opening called all three public cases spreadsheets, and Uber's is a commission on the wrong base | Major | Heading: "Which numbers in Monday's workbook can a director trust, and where did three public cases go wrong?"; its line: "catch a wrong range, formula or base in a number"; the opening names the cases as numbers people relied on: an economics paper's average, a bank's risk figure and a ride-hailing company's commission |
| Exhibit 2C's caption called its orders "three of the quarter's orders", though its dates and instalments match nothing on Kalpa's book | Major | "three illustrative orders" |
| Q10 stated the reconciliation rule against the unpaid list alone, narrower than Tuesday's bridge, which also takes off anything paid short | Major | Q10's stem: "No order on this report was paid short, so a channel's collected reconciles when ..."; Set 1's situation: "Every order with a payment row was paid in full", which the proof checks on the warehouse (0 of 432 paid orders short), so Q8's step (c) holds as written |
| Q16 (d), "Further ahead at every reading ...", is true if read loosely | Minor | "The lead grew at every reading from the week of 20 July to the week of 14 September, and the quarter closed level with the plan" |
| Q15 leaves the learner to infer that member_month has no row for a month with no order | Minor | The stem stays, since saying it gives the trap away; the guide's repair now says it |
| Exhibit 4B's "in the order it sends them" underlined the mechanism Q18 tests | Minor | The caption reads "its rows for three customers" |
| "annotation vendor" is used without explanation | Minor | Exhibit 6A: "label, set by hand at an outside firm"; Q28: "labels that an outside firm set by hand" |
| "active users" in Q33 is not defined | Minor | Stands: a definition answers the item, and Monday's chapter 5 taught that a period counts each person once |
| Q26's "moves in step with" does not give the proportion the arithmetic needs | Minor | "moves in proportion to" |
| Q25 and Q26 are each answered by one visible cue | Minor | Stands: the cue is the skill each item tests, reading a range against its rows and a formula against its written definition, and this pass keeps items and levels |
| Q1's key did not say whether "fell from 2.36 to 1.84" with no percentage earns the tick | Minor | It does; the reason now says so, and that a note of halving, or of 2 and 1, earns none |
| Part 4's heading was a leading question, and Q19 and Q20 are not about that table | Minor | "What must Monday's customer table check before the growth team acts on it?"; the opening's last sentence says the last two items take the same checks to a months view for the head of Retail-Plus and to a genomics lab's gene list |
| Part 3's opening named Meera's decision and not what a wrong reading costs | Minor | It adds Wednesday's line, a false gap against the plan sends Marketing after it with discounts |
| Part 5's stated cost, "misleads both", was vague | Minor | "a wrong total with nothing red beside it becomes a director's decision or a city's budget before any analyst sees it" |
| Part 6: "Each of them acts on one number" is untrue of the product lead | Minor | The opening names each person's decision and closes "A wrong number in these tables changes one of those decisions." |
| Part 2 could name the Rs 9.84 crore at stake | Optional | Stands: Set 1's situation prints the quarter's Rs 9,84,00,000 a page later, and the opening already says what a dropped order and a double count cost |
| Q26's reason cited Thursday, where Friday's notes carry the JPMorgan quotation itself | Minor | The reason keeps Thursday's chapter 4 for the second way to a number and adds Friday's notes and the report's "divided by their sum instead of their average" |
| Q13's "ten times" is 10.35 | Minor | The key's reason says "more than ten times"; the stem's wording sits in `data/programme/paper_edits.yaml`, outside this pass's files (open points, below) |
| The guide asked about "the 216 orders with two payment rows", where the paper's 216 is the one-row orders | Minor | The guide asks which orders with two payment rows are retries and how they differ from instalments; Q8's reason says the 216 two-row orders are the 188 instalment orders and the 28 retries together |
| The guide's validate='many_to_one' against the key's 'one_to_one' in Q28 | Minor | The guide says 'one_to_one' |
| Exhibit 2D is labelled illustrative though only web's collected departs from Kalpa's book | Minor | Stands: naming the altered cell points at the answer; the key's reason says web's collected is the one altered and that web's gap equals its list on Kalpa's book |
| C-0185's empty August and Tuesday's "never print 188 beside 216" | Minor | No change: C-0185's gap is no plant row and the guide names it; decision `plants-once-found` governs the Saturday paper, as the plant table above records |
| Purpose: "with no notes and no assistant" repeats the rules table | Minor | Cut |
| Company row: the list of public cases | Minor | The cases sit in brackets after "Six items draw on public cases" |
| Part 1's run-on sentence, and three sentence openings in a row on "The" | Minor | Split at "Revenue means booked revenue: every order at its amount, whatever its status." |
| Q22: "adds only the members" | Minor | "adds the spend of only the members" |
| Q27: the source is said to give the refund "on average" | Minor | Stands: CBS News of 24 May 2017 says "each affected driver would get a refund of about $900, which includes interest" (re-read on 1 October 2026), and the stem follows it |
| The key's reasons ended on 18 verbless tails, "Run on PostgreSQL 16.14 ... on 1 October 2026." | Minor | The tails are gone, as Week 1's key carries none; the run is recorded in this file and in the proof script. The source citations' "checked on" fragments became clauses ("read on 30 September 2026") |
| Q2's interview line, "returns some rows, never defined ones" | Minor | "returns whichever rows the database reaches first" |
| Q9's interview line, "turns the LEFT JOIN back into an INNER one" | Minor | "back" is gone |
| Q15's interview line had no main verb | Minor | "I build one row per customer per month, take LAG 1 and LAG 2 ..., check ..., and flag ..." |
| Q5 and Q16 reasons opened on a vague "This" | Minor | "Option b ..." |
| Q21 and Q23: "The spare beside it" | Minor | "The unused technique beside it in the match table", and the same in folded bank 31 |
| Q29: "stored as text, '11' would sort below '9'" answers nobody | Minor | Cut, with the proof's assertion on it |
| Q11: "which only a count of rows sent ... measures" contradicts keyed option (e) | Minor | "only" is gone |
| Q33 (c): "how much the assistant must handle at once" | Minor | "how many users the busiest day brought" |
| Guide: "the first paper whose items leave Kalpa" is false | Minor | "Like Week 1's paper, it also leaves Kalpa: six items come from public cases, and Part 6 imagines the tables an AI team keeps." |
| Guide: "Led by the Academic TA." | Minor | "The Academic TA leads the day." |
| Guide: "the marker decides nothing" | Minor | "the key decides every tick, and reading somebody else's answer against it is the exercise" |
| Guide: "The paper carries no marks and ranks nobody" twice | Minor | Kept once, at the end |
| Guide: "Five minutes an anchor, with the bridge anchor last." | Minor | "Each anchor takes five minutes, and the bridge anchor comes last." |
| Guide, anchor 4: "(A row whose key is missing, which is the dropna default.)" | Minor | "(Rows whose key is missing, since groupby drops them by default.)" |
| Guide, anchor 7: "(indicator=True and a count of the matches, Q20.)" | Minor | "The answer is indicator=True with a count of the matches, as in Q20." |
| Guide: the Do and Do not cells lacked full stops | Minor | Added |
| Guide: "genuinely" | Minor | Cut |
| Guide, anchor 9: "a director explores" | Minor | Friday's words: the workbook owns the last mile, presenting, slicing, looking up and taking labelled what-ifs on an export that ties |
| Q14's key was 19 characters shorter than every distractor | Minor | (d) reads "SELECT customer_id, spend, spend / avg(spend) OVER () FROM member_step", the key's length; its results add to 76, which the proof asserts, and (b)'s GROUP BY still tests the share of 1 |
| Q12's and Q30's keys were each 6 characters short of the next option | Minor | Q12 as above; Q30's (a) reads "each beside its low ratings" |
| Q25 repeats the Reinhart and Rogoff case a week after Week 1's paper spelled out its range | Minor | Stands for this pass, which keeps items; named for the requester below |
| Q25's stem made the range error look like the whole cause | Minor | The stem now gives the three corrections the PERI abstract names, "a coding error in the spreadsheet, the exclusion of some available data and an unusual weighting of the averages" (abstract re-read on 1 October 2026) |
| Part 6 opened on a table alone, with no drawn visual | Minor | Exhibit 6A opens with a drawing of who acts on which tables, two rows of three, above the table of tables; the opening lost a sentence so the part's first page still holds the opening, Exhibits 6A and 6B and Q28 |
| "The protect list" is Wednesday's per-segment list in Part 3 and Friday's two-quarter list in Part 5 | Minor | Part 5's opening: "The protect list in the workbook is Friday's: the fifty Retail-Plus members with the highest revenue across both quarters." |

### The proof run

`internal/C2_W02_SAT_key_proofs_INTERNAL.py` ran on 1 October 2026 on PostgreSQL 16.14, pandas
3.0.6 and Python 3.11.15, printed 33 PASS lines, Q1 to Q33, and the stretch line, ended
"RESULT: PASS (33 items proved)" and dropped its scratch schema. The review added these checks:
every paid order of July to September, each retry's second row dropped, adds up to its booked
amount (0 of 432 short), and Set 1 says so; Q10's stem says no order was paid short; Q12's option
(a) claims 51 for DENSE_RANK, whose cut keeps 52; Q13's ratio is 10.35; Q14's option (d) adds to
76; Q28's frames of 5 and 7 rows merge to 7 rows with no error; and Q32's stem routes every call
whose total is over 1,000, the reading the proof's first-over count takes. The keyed texts of Q4
and Q12 follow their new wording, and the text-sort check left with the claim it tested.

### The checks

- `python3 scripts/verify.py content/W02/SAT` ends "RESULT: PASS (0 failures)": the names and the
  style sweep pass on the folder's 10 files, the distractor audit on 22 items and the workbook's
  recalculation on its 2 verdicts, with 1 decision flipped and re-asserted.
- `python3 scripts/distractor_audit.py content/W02/SAT` passes after every wording change: 22
  lettered items, key positions a 6, b 6, c 5, d 5 and e 1.
- `python3 scripts/build_saturday_paper.py W02 --check` reports nothing stale, and
  `python3 scripts/sync_programme.py --check` reports every output current, so the 30 September
  note on Week 1's stale paper no longer holds.
- The Word paper and key went through LibreOffice 24.2.7.2 to PDF and were read page by page. The
  paper runs to 23 pages and the key to 25. Every exhibit prints on the page of the item that reads
  it; Part 6's first page holds its opening, Exhibit 6A's drawing and table, Exhibit 6B and Q28;
  page 6 holds Part 2's opening alone, because Set 1's situation, its drawing and Q7 travel
  together; the answer sheet is page 23 and the key's marking grid page 25.
- The diagrams were drawn with mermaid-cli 11.17.0, the major version `setup.sh` installs, from the
  session's scratch space. The environment's own `mmdc` is 12.0.0, which draws flowchart nodes
  taller and runs the paper to 24 pages.

### Open points, and the shared files this pass would change

- `data/programme/paper_edits.yaml`, bank 27's stem: "is ten times the largest retail spend"
  should read "is more than ten times", since Rs 2,25,000 against Rs 21,740 is 10.35. The key's
  reason says so already, and the proof's check of the stem's wording changes with it. Settled by
  the orchestrating session on 1 October 2026: the stem reads "more than ten times", the paper,
  the key and the workbook were rebuilt with mermaid-cli 11.17.0 (23 and 25 pages), and the key
  proofs pass on all 33 items against the reloaded warehouse. The edit stays proposed, as before.
- mermaid-cli: the environment holds 12.0.0 where `setup.sh` installs @11. A session that builds
  this paper with 12 gets 24 pages, so either the environment returns to 11 or the Saturday
  builder's diagrams are measured again under 12. Settled the same day: the papers are built with
  11, the major version `setup.sh` pins, and 12 is not used for any committed file.
- Q25 repeats the Reinhart and Rogoff case that the Week 1 paper's Part 4 used, where the stopped
  range was spelled out. Another public case of a range that stops short would test the same skill
  cold; that choice sits with the requester, since this pass keeps the items.
- The proposed edits in `data/programme/paper_edits.yaml` (bank 2's stem, bank 27's stem and
  options) still await the Programme Head.
