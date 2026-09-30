# Week 1 Saturday: provenance

INTERNAL. Where every part of the Week 1 Saturday pack came from, which items are waiting for the
tracker, and the decisions taken while building it. Checked on 29 September 2026; the section dated
30 September 2026 at the end records the paper in parts and what was added to it.

## Sources

| Source | What it gave the pack | Checked |
|---|---|---|
| `docs/detailing/W01_W02_spine.md`, "The Saturdays" | The 300-minute shape (paper 120, break 20, marking 20, discussion 90, mock-interview round 30, doubts and the bridge 20), the rule that the bank is the floor and that Week 1 adds about 13 minutes of new timed items | 29 Sep 2026 |
| `docs/detailing/W01_W02_spine.md`, the Week 1 table | The week's traps the new items are built on: rows counted as customers, an average of segment averages, a whole-record dedupe, counts that reconcile while rupees do not | 29 Sep 2026 |
| `docs/curriculum/W1_Data_analysis_found.md`, the Saturday row | The ten interview anchors, the paper's format and status (ungraded, AI-free), the bridge into Week 2 | 29 Sep 2026 |
| `docs/curriculum/W1_Data_analysis_found.md`, the Monday to Friday rows | The daily interview angles each new item's anchor is taken from, and the client-zero plants the STUDENT paper must not name | 29 Sep 2026 |
| `docs/curriculum/source.xlsx`, Saturday papers tab, paper W1 | The 52 bank items, their keys, levels, tags, roles, days, minutes and anchors (107 minutes at the blueprint's pace) | 29 Sep 2026 |
| `data/programme/paper_edits.yaml` | The option rewordings already laid on the bank; none added by this pack | 29 Sep 2026 |
| `data/programme/facts.yaml`, `saturday_papers.paper_minutes` | The paper's 120 minutes | 29 Sep 2026 |
| `.claude/skills/exercise-builder/SKILL.md` and `references/distractor-discipline.md` | The blueprint's pace per item type, the level and tag rules, and the distractor discipline | 29 Sep 2026 |
| `scripts/build_saturday_paper.py`, docstring | The source file's four sections and block-style format | 29 Sep 2026 |
| `.claude/skills/day-pack-builder/references/artifact-manifest.md`, the Saturday paragraph | The Saturday folders and what each of the three files carries | 29 Sep 2026 |
| `content/W01/D4/trainer/C2_W01_D04_day_sheet_TRAINER.md` | The Thursday numbers the discussion guide's anchors 8 and 10 cite (the exposure mix, the Retail-Plus fall at 135 of 5,000 shuffles, p = 0.027, and Retail-Core at p = 0.345) | 29 Sep 2026 |

No external link enters this pack. The row's two trainer resources stay in the row and were not
re-verified here.

## The new items, waiting for the tracker

All five sit in the scenario section after the bank's three sets, at 2.5 minutes each, which is
12.5 minutes and takes the paper from 107 to 119.5 minutes by the blueprint's pace.

| Q | Set | Level | Tag | Day | Key | The trap it stages | Anchor |
|---|---|---|---|---|---|---|---|
| Q46 | 4 | Easy | [S] | Mon | 2.00 (or 2) | Rows counted as customers, so orders per customer reads 1.00 | Marketing wants budget for acquisition; what would you check before agreeing it is the right branch? |
| Q47 | 4 | Medium | [S] | Tue | 4,000 (Rs 4,000) | An average of segment averages, Rs 7,000 | Why is a rate without a denominator meaningless? |
| Q48 | 4 | Hard | [D] | Tue | c | Marketing's "nobody comes back" read off the broken slide | Marketing insists the answer is acquisition and your data says frequency; how do you make the case in the room? |
| Q49 | 5 | Medium | [F] | Wed | d | A whole-record dedupe reporting zero duplicates | How do you find duplicates, and what makes two records the same? |
| Q50 | 5 | Hard | [D] | Wed | b | Counts that reconcile while Rs 3.0 lakh does not | Finance and your dashboard disagree; what do you do? |

Accept one by adding it to the tracker's Saturday papers tab, paper W1, and deleting it from the
source file. Until then the key lists them under "New items waiting for the tracker".

## Decisions

1. **Two new scenario sets and five items, 12.5 minutes.** The blueprint prices a scenario item at
   2.5 minutes, so five items land the paper at 119.5 minutes against 120, the same margin Week 2
   carries. A sixth item would run to 122.
2. **The new sets cover the traps the bank does not.** The bank already stages unequal windows (Q21),
   p = 0.03 misread (Q9, Q26, Q35) and the aggregate trusted while every segment fell (Set 3). Set 4
   takes Monday and Tuesday's rows counted as customers and average of averages; Set 5 takes
   Wednesday's whole-record dedupe and counts that reconcile while rupees do not.
3. **The new sets use their own numbers, not client zero's.** Set 4 is an April export of 500 rows
   and Set 5 a store-channel Q1 export of 1,200 rows, so no stem carries a planted figure from v0 to
   v3 and nothing a learner reads names a plant.
4. **Key positions.** The three new option items key on c, d and b, which keeps the paper's
   positions spread across a, b, c and d.
5. **Exhibits.** Sets 1, 2, 3 and 4 carry a small table and Set 5 a Mermaid flow, each drawn only
   from its situation's numbers. Set 2's exhibit was first drawn as a Mermaid flow and rendered a
   full page tall in the Word paper, so it became a table; no exhibit prints a number an item asks
   for.
6. **Notes on every bank item.** The fill-in, true-or-false, applied maths and ordering items carry
   their commonest wrong answers as the keys of `wrong`, so the key file prints each wrong answer in
   brackets beside the misconception behind it.
7. **The stretch page.** Four written follow-ups: acquisition's cost case, p = 0.03 for the board,
   the auditor's walk through removed rows, and the two-hour export. Stretch 2 names no segment, so
   it gives away no Thursday finding.
8. **The discussion guide.** Rewritten for the 300-minute Saturday. The most-missed list gains the
   five new items; the anchors keep their answers and their item lists move to the printed numbers
   (bank items 46 to 52 now print as Q51 to Q57); the mock-interview round assigns anchor pairs by
   counting round the room, so every anchor is asked and no pair picks its favourites.
9. **The Word files were first rendered with a session shim for mermaid-cli, and then rebuilt
   without it.** The installed mermaid-cli 12.0.0 has no `-w` option, which the builders passed for
   every PNG, so every Mermaid exhibit silently dropped from the Word paper. The builders now ask
   mmdc which options it has: on 11 they pass `-w` as before, and on 12 they pass `--size` at the
   diagram's own size, capped at the old page width. The Word paper and key were rebuilt with that
   fix and no shim.

## 30 September 2026: the paper in parts, three code items and three option edits

The requester approved the re-cut into parts on 30 September 2026. The orchestrating session wrote
the builder that prints it and moved six recall items to the stretch page; this section records the
content that completed the paper. The Q numbers in the sections above belong to the paper of 29
September, and the numbers below are the paper as it now prints: 54 items in six parts, 119.5 minutes
at the blueprint's pace against the 120-minute slot, 19 easy, 22 medium and 13 hard.

| Part | Items | Minutes | Easy | Medium | Hard |
|---|---|---|---|---|---|
| 1. The week's rules, cold | Q1 to Q9 | 9 | 5 | 3 | 1 |
| 2. Where did the revenue go | Q10 to Q21 | 27.5 | 5 | 5 | 2 |
| 3. Rows you can trust | Q22 to Q31 | 23 | 3 | 6 | 1 |
| 4. Read the code, read the data | Q32 to Q41 | 21.5 | 2 | 4 | 4 |
| 5. Chance and a fair test | Q42 to Q48 | 16.5 | 1 | 2 | 4 |
| 6. The numbers | Q49 to Q54 | 22 | 3 | 2 | 1 |

### The six recall items on the stretch page

Bank items 1, 2, 3, 4, 5 and 7, all fill in the blank, print untimed and unmarked as Stretch 5 to 10,
in the bank's order, with their keys and reasons in the key's stretch section: price, customers,
None, str (a string), rejected and caveat.

### The part openings

Each part opens on a stakeholder's own words from the week's material. Part 1 quotes Kavya Nair from
`content/W01/D5/slides/C2_W01_D05_rehearsal_STUDENT.md`, Part 2 Meera Raghavan from
`content/W01/D2/slides/C2_W01_D02_half1_STUDENT.md`, Part 3 Anand Iyer from
`content/W01/D3/slides/C2_W01_D03_half1_STUDENT.md`, Part 4 Kavya's review in
`content/W01/D1/slides/C2_W01_D01_half1_STUDENT.md`, Part 5 Meera from
`content/W01/D4/slides/C2_W01_D04_half1_STUDENT.md` and Part 6 Kavya from
`content/W01/D5/slides/C2_W01_D05_lab_STUDENT.md`. Part 3 stops before Anand's "Until your numbers
match ours" and Part 5 leaves out Meera's "or did those customers buy anyway?", since each would
point at an answer on the paper.

### Three code items in part 4, and the proof of each key

Part 4 gains three items of one correct option at 2 minutes each, which takes the timed paper from
113.5 to 119.5 minutes. Each exhibit is invented data, labelled invented in its caption, run through
at most eight lines faithful to the week's notebooks, and carries no client-zero value. Each wrong
option is a trap the week staged, and the key names the trap and its day. Every key was proved on 30
September 2026 by executing the exhibit exactly as the source file stores it, with Python 3.11.15:

```
python3 -c "import yaml; d = yaml.safe_load(open('content/W01/SAT/internal/C2_W01_SAT_paper_source_INTERNAL.yaml')); exec(next(a for a in d['additions'] if a['id'] == 'ID')['exhibit']['code']['text'])"
```

with ID replaced by the item's id.

| Q | id | Level | Tag | Day | The trap it stages | Code it follows | Printed output | Key |
|---|---|---|---|---|---|---|---|---|
| Q38 | blank-discount | Medium | [S] | Tue | A blank discount read as zero | Tuesday notebook 02, section 4, `order.get("discount", 0) > 0` | `2 of 5 orders had a discount` | d |
| Q40 | helper-summary | Hard | [F] | Tue | A helper that prints and hands back None, so the summary loses a city | Tuesday notebook 04, part 1, `pct_change` and the falls filter | `check by hand: -50.0%`, then `{'Delhi': -6.0}` | b |
| Q41 | first-copy | Hard | [F] | Wed | The first copy kept before conversion, so the rows add up and the rupees do not | Wednesday notebook 03, section 3, the first-copy pass, with round 1's `setdefault` | `4 rows: 2 clean, 2 set aside; Rs 5500` | a |

The wrong options were run the same way. On Q41, keeping the copy that validates prints `4 rows: 3
clean, 1 set aside; Rs 7300`, option b, and coercing "n/a" to zero prints `4 rows: 3 clean, 1 set
aside; Rs 5500`, option c. On Q40, a helper that returns on both paths prints `{'Pune': -50.0,
'Delhi': -6.0}`, the summary option a describes. On Q38, the orders that record a discount give 2
of 3, and the share across all five lies between 0.4 and 0.8.

Part 4 prints Q32 (bank 11), the two exports as Sets 3 and 4, and then the four code items: Q38,
Q39 (bank 22), Q40 and Q41. In that order every exhibit and every set's situation shares a page with
its questions in the Word paper as LibreOffice renders it, without relying on keep-with-next, and
the easy print item comes straight before the hard helper item. The five items added on 29 September
now print as Q33 (whole-record-dedupe), Q34 (rows-not-rupees), Q35 (rows-as-customers), Q36
(average-of-averages) and Q37 (broken-slide).

### Three option edits, proposed

Three options were ones no reader would take, so each item tested one fewer idea than it printed.
`data/programme/paper_edits.yaml` proposes a near-miss for each, and the source file's notes explain
the new wording. Stems and keys stay as the bank has them, and the distractor audit passes.

| Q | Bank | Option | Was | Proposed |
|---|---|---|---|---|
| Q13 | 21 | c | Drop Q2 from the analysis. | Compare the quarters month by month, three months against three. |
| Q15 | 30 | c | the colour of its chart | its value in the previous quarter |
| Q27 | 33 | d | the p-value of the field | the value to fill in where one is missing |

### The discussion guide

The guide's item numbers were remapped by script from the paper at 5c57eea, matching each item on
its text, and the quarters named Q1 and Q2 were left as they were. The map, from the paper at
5c57eea to this one:

| Old | New | Old | New | Old | New |
|---|---|---|---|---|---|
| Q1 | Stretch 5 | Q20 | Q12 | Q39 | Q20 |
| Q2 | Stretch 6 | Q21 | Q13 | Q40 | Q28 |
| Q3 | Stretch 7 | Q22 | Q39 | Q41 | Q29 |
| Q4 | Stretch 8 | Q23 | Q22 | Q42 | Q30 |
| Q5 | Stretch 9 | Q24 | Q23 | Q43 | Q46 |
| Q6 | Q1 | Q25 | Q24 | Q44 | Q47 |
| Q7 | Stretch 10 | Q26 | Q42 | Q45 | Q48 |
| Q8 | Q2 | Q27 | Q43 | Q46 | Q35 |
| Q9 | Q3 | Q28 | Q25 | Q47 | Q36 |
| Q10 | Q4 | Q29 | Q14 | Q48 | Q37 |
| Q11 | Q32 | Q30 | Q15 | Q49 | Q33 |
| Q12 | Q5 | Q31 | Q16 | Q50 | Q34 |
| Q13 | Q6 | Q32 | Q26 | Q51 | Q50 |
| Q14 | Q7 | Q33 | Q27 | Q52 | Q51 |
| Q15 | Q8 | Q34 | Q44 | Q53 | Q52 |
| Q16 | Q9 | Q35 | Q45 | Q54 | Q53 |
| Q17 | Q10 | Q36 | Q17 | Q55 | Q54 |
| Q18 | Q11 | Q37 | Q18 | Q56 | Q21 |
| Q19 | Q49 | Q38 | Q19 | Q57 | Q31 |

The marking gains the step where the Academic TA enters each paper by seat in the item-analysis
workbook, the most-missed discussion follows its Discussion sheet, and the candidate table and the
anchors gain Q38, Q40 and Q41.

## 30 September 2026, later: the Word paper in the diagnostic's format

The requester asked for the Saturday paper's Word version to follow the format of the baseline
diagnostic, `content/W00/D2/paper/C2_W00_D02_diagnostic_STUDENT.docx`, with an answer sheet to print
at the end, wording that is never generic, no bias in option length or quality and no surface-level
items. The orchestrating session's builder draws that format from commit f7dff4f: a first page with
the purpose, the rules with a Company row, step one's ratings of each part from 1 to 4 before any
item is read, the paper at a glance and a pacing ribbon; open question blocks labelled beside the
level, each exhibit and set case bound to the first item that reads it; an answer sheet on one page;
and a key that ends on a marking grid. The item-analysis workbook gains a Ratings sheet.

Rendered with LibreOffice on 30 September 2026, the Word paper runs to 17 pages and the key to 17.
Every exhibit and set case prints with its first question, the answer sheet fits page 17, and the
labels, tables, code panels and pacing ribbon read cleanly. Q54 prints alone on page 14: Part 6's
five working boxes need slightly more than pages 12 and 13 hold, so one item spills in any order.

### Labels

Every printed item carries a label of two to five words saying what it asks the reader to do with
what is in front of them, in the manner of the diagnostic's own labels. No label states or leans
toward a key, and no two neighbours share one. Bank items carry theirs in the source file's notes,
and the eight additions in their own entries.

| Q | Label | Q | Label | Q | Label |
|---|---|---|---|---|---|
| Q1 | Complete the definition | Q19 | Test the decomposition | Q37 | Reply in the room |
| Q2 | Name the mechanism | Q20 | Answer Marketing's claim | Q38 | Read the discount count |
| Q3 | Read a p-value claim | Q21 | Order the ladder | Q39 | Predict what result holds |
| Q4 | Test a claim on averages | Q22 | Repair the crash | Q40 | Trace the summary |
| Q5 | Judge a claim on significance | Q23 | Decide what a duplicate is | Q41 | Predict the output |
| Q6 | Check a claim on duplicates | Q24 | Read the run's report | Q42 | Read the shuffles |
| Q7 | Compare two counts | Q25 | Choose the first move | Q43 | Advise Meera |
| Q8 | Test a causal claim | Q26 | Treat a missing value | Q44 | Design a fair test |
| Q9 | Judge an aggregate claim | Q27 | Define the profile | Q45 | Check four p-value statements |
| Q10 | Rule out a branch | Q28 | Count the clean rows | Q46 | Name the pattern |
| Q11 | Place the Rs 12 crore | Q29 | Size the rejects log | Q47 | Judge frequency's role |
| Q12 | Pick the first rung | Q30 | Update the comparison | Q48 | Advise on Diwali |
| Q13 | Repair the comparison | Q31 | Order the cleaning pass | Q49 | Read the two averages |
| Q14 | Compare the levers | Q32 | Predict the comparison | Q50 | Reason with numbers |
| Q15 | Define a rate | Q33 | Choose the count to trust | Q51 | Compute median and mean |
| Q16 | Find what fakes a drop | Q34 | Judge the reconciliation | Q52 | Size the change |
| Q17 | Compute a leaf | Q35 | Count per customer | Q53 | Read p off the shuffles |
| Q18 | Find the branch that moved | Q36 | Price the average order | Q54 | Build revenue from the tree |

### Option lengths

The audit now fails a Saturday item whose options run past 30 characters when the shortest is under
60 percent of the longest, and nine items did. Each fix is proposed in the W1 block of
`data/programme/paper_edits.yaml`, with the lengths before and after in its reason, and the key's
notes answer the new wording. Stems and keys stay as the bank has them. On Q16 both ends of the
range were keyed options, so no distractor could balance the set, and keyed option a was reworded
with its meaning and its letter unchanged. Lengths are the audit's own, in characters.

| Q | Bank | Option | Was | Now | Item's options, before | After |
|---|---|---|---|---|---|---|
| Q10 | 17 | d | discounts (9) | the value of the discounts given (32) | 9 to 33 | 23 to 33 |
| Q13 | 21 | a | Compare the two totals as they stand. (36) | Compare the two totals as they stand, since each is one calendar quarter. (72) | 36 to 70 | 63 to 72 |
| Q15 | 30 | c | its value in the previous quarter (33) | its value last quarter (22) | 13 to 33 | 13 to 25 |
| Q16 | 31 | a (keyed) | quarters of unequal length (26) | quarters holding unequal numbers of weeks (41) | 26 to 54 | 36 to 54 |
| Q26 | 32 | d | Type a value into the source file. (33) | Type a value into the export. (28) | 12 to 33 | 12 to 28 |
| Q30 | 42 | a | It grows. (8) | It grows, because removing rows takes revenue out. (49) | 8 to 48 | 34 to 49 |
| Q43 | 27 | a | Move budget to Student now. (26) | Move budget to Student now, since it grows fastest. (50) | 24 to 48 | 45 to 51 |
| Q43 | 27 | c | Drop the Student segment. (24) | Drop Student from the report as too small to matter. (51) | 24 to 48 | 45 to 51 |
| Q44 | 34 | d | a deeper discount (17) | a deeper discount, so any effect is easier to see (49) | 17 to 51 | 36 to 51 |
| Q49 | 19 | a | Most orders sit near Rs 9,800. (29) | Most orders sit close to the Rs 9,800 mean. (42) | 29 to 59 | 34 to 50 |
| Q49 | 19 | b | The median has been miscalculated from an incomplete export. (59) | The median was miscalculated from a partial export. (50) | 29 to 59 | 34 to 50 |

### Purpose and company

The first page's "What this paper is for" reads: "This week Meera Raghavan asked whether the Rs 12 crore Marketing wants for acquisition goes to the branch of revenue that is actually short, Anand Iyer disputed the Q1 figure the ERP export put on the dashboard, and Meera now has to decide whether the monsoon discount runs again at Diwali. This paper puts those decisions in front of you once more, with no notebook, no notes and no assistant, to find which of them you can make cold. The room's scores in each part, set beside the ratings you give in step one, decide where Monday's revision starts. A wrong answer tells Monday more than a blank one, so answer every item."

The Rules table's Company row reads: "Every item is set inside Kalpa Retail, where you work as a trainee engineer in the data and AI team of its Global Capability Centre. Meera Raghavan is its CEO, Anand Iyer its finance controller and Kavya Nair a senior analyst in its data team; Marketing and Finance appear by function, and every number an item needs is on the page." Every name and role in it is one the week's own files
give: Meera Raghavan, CEO, on the Monday, Tuesday and Thursday deck covers; Anand Iyer, finance
controller, on Wednesday's; Kavya Nair, senior analyst in the Kalpa Retail data team, on Friday's;
and the data and AI team of Kalpa's Global Capability Centre in the address lines of those covers.

## 30 September 2026, last: the more-than-one keys relabelled

All six more-than-one items came from the tracker keyed with a and b, so a learner who ticked a and
b on every such item scored on all six without reading one. Four of them are relabelled with an
`order` edit in `data/programme/paper_edits.yaml`, status proposed: the same options print, the
same ones are correct, and the key's letters and the key file's reasons move with them. Each edit
carries `from_key`, the tracker's key it was written against, so the sync reports it folded once
the tracker prints the new order, rather than laying it twice.

| Q (bank) | Tracker key | Printed as the tracker's | Printed key | Wrong option now at |
|---|---|---|---|---|
| Q16 (31) | a, b, c | d, a, b, c | b, c, d | a |
| Q26 (32) | a, b, c | a, d, b, c | a, c, d | b |
| Q44 (34) | a, b, c | d, a, b, c | b, c, d | a |
| Q45 (35) | a, b, d | a, c, b, d | a, c, d | b |

Q15 and Q27 keep the tracker's order, so the six wrong options sit at a twice, b twice, c once and
d once, and each letter sits in four or five of the six keys. `scripts/distractor_audit.py` now
fails a Saturday paper where one letter sits in every more-than-one key across four or more such
items; the paper as it stood before this change fails it, and the relabelled paper passes, with the
keys of all 31 option items at a 10, b 10, c 11 and d 12.
