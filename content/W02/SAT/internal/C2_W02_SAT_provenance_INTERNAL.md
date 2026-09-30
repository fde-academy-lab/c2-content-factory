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
