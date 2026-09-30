# Week 1 Saturday: provenance

INTERNAL. Where every part of the Week 1 Saturday pack came from, which items are waiting for the
tracker, and the decisions taken while building it. Checked on 29 September 2026; the section dated
30 September 2026 records the paper in parts and what was added to it, and the section headed
"30 September 2026, v3" records the paper raised to interview grade, and the section headed
"30 September 2026, v4" at the end records the paper as it now prints, after a blind sitting; it
supersedes the item numbers, counts and sources of every section before it.

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

## 30 September 2026, the requester's rulings on the open items

Q32 and Q51 print as the tracker wrote them. Each names a value planted in the Week 1 Monday
dataset, and the requester ruled that the week's Saturday recap paper, and no other learner file,
may name a plant the room has already found in class, which it has by Saturday (decision
`plants-once-found` in `data/programme/facts.yaml`). Q12 and Q21
both stay as well: Q21 asks for the five rungs of the investigation ladder in order, so it holds
Q12's answer, the first rung, and the requester chose to leave both tracker items as they are.

## 30 September 2026, v3: the paper raised to interview grade

On 30 September 2026 the requester asked for Saturday papers of interview grade, with rich
scenarios, proper diagrams, word banks or match tables in place of plain blanks, applied Python,
data interpretation and some SQL, and approved the plan that the bank sets the topics and the paper
sets the bar, at about 60 percent hard. Later the same day the requester added real companies and
public case studies, and asked that solving outweigh reading code. This section records the paper as
it now prints. It replaces the 54-item paper in six parts described above, so every Q number, count
and source line in the earlier sections belongs to an earlier paper.

### The paper as it prints

36 timed items in five parts, 119.5 minutes at the blueprint's pace against the 120-minute slot,
with 2 easy, 13 medium and 21 hard items, which is 5.6, 36.1 and 58.3 percent by count. Parts 1 to
3 are Kalpa's week, Part 4 is the week's traps in public cases, and Part 5 is a hypothetical support
agent at a food-delivery company such as Swiggy, with every number illustrative. Every part opens on
a visual: the revenue tree, the two Q1 figures' flow, the 5,000-shuffle chart, the debt table and the
agent's loop; each of the three scenario sets carries a chart or a table.

| Part | Items | Minutes | Easy | Medium | Hard |
|---|---|---|---|---|---|
| 1. Where the revenue went | Q1 to Q8 | 25.5 | 2 | 1 | 5 |
| 2. Which Q1 figure is right | Q9 to Q16 | 27.5 | 0 | 3 | 5 |
| 3. Real, worth it, and caused | Q17 to Q22 | 22.5 | 0 | 1 | 5 |
| 4. The same traps, in public | Q23 to Q28 | 21 | 0 | 2 | 4 |
| 5. The agent's bill and its logs | Q29 to Q36 | 23 | 0 | 6 | 2 |

| Q | Source | Format | Level | Min | Day | The trap it stages |
|---|---|---|---|---|---|---|
| Q1 | bank 47 | Applied maths | Easy | 1.5 | Mon | the mean read as the typical order when one bulk order drives it |
| Q2 | new: sales-net | One correct option | Hard | 4 | Mon | a status test written as == "delivered" or "returned", true for every order, so cancellations count as sales |
| Q3 | new: payback-typical | One correct option | Hard | 4 | Mon | the mean of Rs 18,160 priced as the typical first order |
| Q4 | bank 46 | Applied maths | Hard | 4 | Mon | two percentages added where the tree's factors multiply |
| Q5 | new: quarter-counter | One correct option | Hard | 4 | Tue | a counter reset inside the segment loop, so each quarter keeps Student's count |
| Q6 | bank 20 | One correct option | Easy | 1.5 | Tue | a hypothesis before the drop is confirmed |
| Q7 | new: budget-fact | One correct option | Hard | 4 | Tue | a branch chosen before the cost of moving each branch is known |
| Q8 | bank 51 | Order the steps | Medium | 2.5 | Tue | the like-with-like rung skipped |
| Q9 | new: reader-header | One correct option | Hard | 4 | Wed | an extra next() on a DictReader, which drops the first order |
| Q10 | bank 11 | True or false, plain | Medium | 2.5 | Mon | text compared as text, so '4500' sorts after '30000' without an error |
| Q11 | new: evidence-copy | True or false, with the reason | Hard | 4 | Wed | a shallow copy that shares the dictionaries the pass rewrites |
| Q12 | new: reject-loop | More than one correct | Hard | 4 | Wed | rows removed from the list being walked, so a row is skipped while the counts still close |
| Q13 | bank 24 | One correct option | Medium | 2.5 | Wed | a whole-row check that misses a re-sent order carrying a new date |
| Q14 | new: monday-number | Scenario set | Hard | 4 | Tue | the tile's mismatched windows, and the duplicated Q1 still in the export |
| Q15 | new: plus-clean | Scenario set | Hard | 4 | Wed | a rate on the export with May's 11 copied rows still in Q1 |
| Q16 | bank 52 | Order the steps | Medium | 2.5 | Wed | recomputing before reconciling |
| Q17 | bank 35 | More than one correct | Hard | 4 | Thu | the p-value read as the chance the hypothesis is true |
| Q18 | new: shuffle-sign | One correct option | Hard | 4 | Thu | a count run against the direction of the claim, so a real fall reads as p = 0.981 |
| Q19 | new: student-line | One correct option | Hard | 4 | Thu | a p above 0.05 read as proof that nothing happened |
| Q20 | bank 43 | Scenario set | Hard | 4 | Thu | a blended rise credited to the campaign while each segment fell |
| Q21 | bank 45 | Scenario set | Hard | 4 | Thu | a campaign repeated on a mix effect |
| Q22 | new: diwali-test | Scenario set | Medium | 2.5 | Thu | a comparison of groups that differed before the offer |
| Q23 | new: debt-weights | Scenario set | Hard | 4 | Tue | an average of averages that gives one year the weight of nineteen |
| Q24 | new: debt-rows | Scenario set | Medium | 2.5 | Wed | a formula that covered 15 of 20 rows without an error |
| Q25 | new: orbiter-units | One correct option | Medium | 2.5 | Wed | one of two disagreeing figures averaged or trusted before the gap is explained |
| Q26 | new: flu-fit | More than one correct | Hard | 4 | Thu | a proxy that tracks the season, and a fit found among millions of tries |
| Q27 | new: bing-alert | One correct option | Hard | 4 | Thu | a result too good to be true shipped or discarded before the plumbing is checked |
| Q28 | new: wald-buyers | True or false, with the reason | Hard | 4 | Thu | a per-buyer denominator that drops the members who stopped buying |
| Q29 | new: tool-print | One correct option | Hard | 4 | Tue | a tool that prints instead of returning, so the model reads 'None' |
| Q30 | new: agent-history | One correct option | Medium | 2.5 | Tue | a mutable default argument that carries one customer's history into another's call |
| Q31 | new: agent-cost | One correct option | Hard | 4 | Mon | a mean driven by one looping conversation, or the loop deleted from the bill |
| Q32 | new: sql-where | Word bank | Medium | 2.5 | Wed | a row filter placed after grouping |
| Q33 | new: sql-having | Word bank | Medium | 2.5 | Thu | a test on a count placed before grouping, or a LIMIT read as a floor |
| Q34 | new: sql-count | Match the following | Medium | 2.5 | Wed | COUNT(column) read as a count of rows |
| Q35 | new: sql-avg | Match the following | Medium | 2.5 | Wed | AVG read as counting a NULL as zero |
| Q36 | new: sql-rate | Match the following | Medium | 2.5 | Tue | an integer division that returns 0 |

### Formats and their counts

| Format | Items | Count |
|---|---|---|
| One correct option | Q2, Q3, Q5, Q6, Q7, Q9, Q13, Q18, Q19, Q25, Q27, Q29, Q30, Q31 | 14 |
| Scenario set, in three sets | Set 1: Q14 and Q15; Set 2: Q20 to Q22; Set 3: Q23 and Q24 | 7 |
| More than one correct | Q12, Q17, Q26 | 3 |
| Match the following, one table of six values | Q34 to Q36 | 3 |
| True or false, with the reason | Q11, Q28 | 2 |
| Word bank, one bank of six SQL words | Q32, Q33 | 2 |
| Applied maths | Q1, Q4 | 2 |
| Order the steps | Q8, Q16 | 2 |
| True or false, plain | Q10 | 1 |

The three more-than-one keys are b and d, a, c and d, and b and e, so no letter sits in all three.
Across the 25 option items the keys sit at a 6 times, b 8, c 7, d 7 and e once. Q15 is a set item
answered with a number. The word bank leaves four of its six words unused, and the match table
three of its six values.

### The fate of every bank item

Ten bank items print; the other 42 fold into a printed item that tests the same concept; none moves
to the stretch page. The six recall items the earlier re-cut had moved to the stretch page, bank 1, 2,
3, 4, 5 and 7, fold into timed items, and the stretch page now holds four written follow-ups. Each
fold's reason is in the source file's `folded` block and prints in the key under "Bank items folded
into deeper items".

| Bank | Printed as | What changed on the paper |
|---|---|---|
| 47 | Q1 | Paced at 1.5 minutes, an easy item's pace, where the tracker gives 4 |
| 46 | Q4 | Nothing |
| 20 | Q6 | Paced at 1.5 minutes where the tracker gives 2; it prints before bank 51, as the requester asked |
| 51 | Q8 | Nothing |
| 11 | Q10 | Stem reworded, status proposed; paced at 2.5 minutes where the tracker gives 1 |
| 24 | Q13 | Stem and options a, c and d reworded, status proposed; paced at 2.5 minutes where the tracker gives 2 |
| 52 | Q16 | Nothing |
| 35 | Q17 | The accepted order edit; paced at 4 minutes where the tracker gives 2.5 |
| 43 | Q20 | Situation reworded on the week's own numbers, status proposed; paced at 4 minutes where the tracker gives 2.5 |
| 45 | Q21 | The accepted option edit; paced at 4 minutes where the tracker gives 2.5 |

| Bank | Tracker type and level | Folded into |
|---|---|---|
| 1 | Fill in the blank, Easy | Q4 (bank 46) |
| 2 | Fill in the blank, Easy | Q15 (new: plus-clean) |
| 3 | Fill in the blank, Easy | Q29 (new: tool-print) |
| 4 | Fill in the blank, Easy | Q10 (bank 11) |
| 5 | Fill in the blank, Easy | Q12 (new: reject-loop) |
| 6 | Fill in the blank, Medium | Q18 (new: shuffle-sign) |
| 7 | Fill in the blank, Easy | Q19 (new: student-line) |
| 8 | Fill in the blank, Medium | Q26 (new: flu-fit) |
| 9 | True or false, Medium | Q17 (bank 35) |
| 10 | True or false, Easy | Q3 (new: payback-typical) |
| 12 | True or false, Easy | Q17 (bank 35) |
| 13 | True or false, Easy | Q14 (new: monday-number) |
| 14 | True or false, Easy | Q19 (new: student-line) |
| 15 | True or false, Easy | Q22 (new: diwali-test) |
| 16 | True or false, Hard | Q20 (bank 43) |
| 17 | One correct option, Easy | Q7 (new: budget-fact) |
| 18 | One correct option, Easy | Q7 (new: budget-fact) |
| 19 | One correct option, Easy | Q3 (new: payback-typical) |
| 21 | One correct option, Medium | Q14 (new: monday-number) |
| 22 | One correct option, Easy | Q29 (new: tool-print) |
| 23 | One correct option, Medium | Q12 (new: reject-loop) |
| 25 | One correct option, Medium | Q12 (new: reject-loop) |
| 26 | One correct option, Hard | Q19 (new: student-line) |
| 27 | One correct option, Easy | Q19 (new: student-line) |
| 28 | One correct option, Medium | Q25 (new: orbiter-units) |
| 29 | One correct option, Hard | Q7 (new: budget-fact) |
| 30 | More than one correct, Easy | Q15 (new: plus-clean) |
| 31 | More than one correct, Medium | Q14 (new: monday-number) |
| 32 | More than one correct, Easy | Q16 (bank 52) |
| 33 | More than one correct, Easy | Q34 (new: sql-count) |
| 34 | More than one correct, Medium | Q22 (new: diwali-test) |
| 36 | Scenario set, Easy | Q15 (new: plus-clean) |
| 37 | Scenario set, Medium | Q7 (new: budget-fact) |
| 38 | Scenario set, Medium | Q7 (new: budget-fact) |
| 39 | Scenario set, Hard | Q7 (new: budget-fact) |
| 40 | Scenario set, Easy | Q12 (new: reject-loop) |
| 41 | Scenario set, Medium | Q12 (new: reject-loop) |
| 42 | Scenario set, Hard | Q14 (new: monday-number) |
| 44 | Scenario set, Medium | Q20 (bank 43) |
| 48 | Applied maths, Easy | Q14 (new: monday-number) |
| 49 | Applied maths, Medium | Q18 (new: shuffle-sign) |
| 50 | Applied maths, Medium | Q4 (bank 46) |

The three new ledger entries sit under W1 in `data/programme/paper_edits.yaml`, each with its
reason; every entry already there is kept as it was.

### Public cases and their sources

Every fact Part 4 states was read in its source on 30 September 2026. The paper names each source
by author, publication and year beside the case, without a link; the key's reasons name the same
source where they cite it. Part 5 names Swiggy only as an example of a food-delivery company and
states nothing about its agents, logs or costs.

| Items | Case | Source | Link | Read |
|---|---|---|---|---|
| Q23, Q24 | The above-90 average and its spreadsheet | Herndon, Ash and Pollin, "Does High Public Debt Consistently Stifle Economic Growth? A Critique of Reinhart and Rogoff", PERI Working Paper 322, April 2013: Table 2 (the seven countries, their years and growth), Table 3 (0.0, 1.7 and -0.1) and note 5 (lines 30 to 44 in place of 30 to 49) | https://peri.umass.edu/wp-content/uploads/joomla/images/WP322.pdf | checked 30 Sep 2026 |
| Q23, Q24 | Reinhart and Rogoff's reply | The Harvard Crimson, "After Error is Revealed, Professor Pair Defends Core Conclusions", 24 April 2013: the error acknowledged, equal weighting by country defended | https://www.thecrimson.com/article/2013/4/24/rogoff-error-defense/ | checked 30 Sep 2026 |
| Q25 | Mars Climate Orbiter | NASA, Mars Climate Orbiter Mishap Investigation Board Phase I Report, 10 November 1999: the root cause, the factor of 4.45, the discrepancies reported informally and not resolved, the planned 226 km and the estimated 57 km | https://llis.nasa.gov/llis_lib/pdf/1009464main1_0641-mr.pdf | checked 30 Sep 2026 |
| Q26 | Google Flu Trends | Lazer, Kennedy, King and Vespignani, "The Parable of Google Flu: Traps in Big Data Analysis", Science 343, 14 March 2014: 50 million terms against 1,152 data points, high school basketball, "part flu detector, part winter detector", the 2009 pandemic missed, and 100 of 108 weeks too high from August 2011 | https://gking.harvard.edu/files/gking/files/0314policyforumff.pdf | checked 30 Sep 2026 |
| Q27 | Bing's ad headlines | Kohavi and Thomke, "The Surprising Power of Online Experiments", Harvard Business Review, September to October 2017: the idea's six-month wait, the "too good to be true" alert, revenue up 12 percent and more than 100 million US dollars a year in the United States | https://hbr.org/2017/09/the-surprising-power-of-online-experiments | checked 30 Sep 2026 |
| Q28 | Wald's returning aircraft | Mangel and Samaniego, "Abraham Wald's Work on Aircraft Survivability", Journal of the American Statistical Association 79 (386), June 1984: Wald's vulnerability estimates from the damage on surviving aircraft, at the Statistical Research Group at Columbia University | https://jhanley.biostat.mcgill.ca/bios601/CandH-ch0102/WaldAircraft.pdf | checked 30 Sep 2026 |
| Part 5 | Swiggy as a food-delivery company | Swiggy, About Us: the company's food delivery business, launched in 2014 | https://www.swiggy.com/corporate/ | checked 30 Sep 2026 |

### The proof run

`content/W01/SAT/internal/C2_W01_SAT_key_proofs_INTERNAL.py` settles every timed key. It executes
each code exhibit as the source file stores it, on the week's own data files where the item names
them, runs the five SQL items in a scratch schema it creates and drops on the local Postgres, and
recomputes every arithmetic key. The run of 30 September 2026, on Python 3.11.15, psycopg2 2.9.13 and
PostgreSQL 16.13, printed:

```
Week 1 Saturday paper: 36 timed items. Each line gives the printed Q, the item, its key and what proves it.
  Q1  bank 47            key 1,400; 97,080 median of five sorted values is the third; 4,85,400 over 5 is 97,080
  Q2  sales-net          key c            prints '30 orders, Rs 544810'; net of cancellations is 26 orders, Rs 5,35,760
  Q3  payback-typical    key b            mean 18,160, median 2,205, bulk order 88 percent, other 29 average 2,235, delivered mean 24,800
  Q4  bank 46            key -6.5 percent 1.10 x 0.85 = 0.935; break-even volume at 15 percent off is 17.6 percent
  Q5  quarter-counter    key d            prints '{'Q1': 5, 'Q2': 7} +40.0%': the counter holds Student's count; the file says 114 and 86
  Q6  bank 20            key a            tracker key: the first rung is confirming the drop is real
  Q7  budget-fact        key d            same 69 customers; orders per customer 1.65 to 1.25; revenue per order +18.0 percent
  Q8  bank 51            key b, d, e, a, c tracker key: real, like with like, decompose, isolate, hypothesise
  Q9  reader-header      key b            prints '200 KR-02002': next() consumed KR-02001, a Q1 order of Rs 2,200
 Q10  bank 11            key False        '4500' < '30000' is False, silently; the tracker's '4500' > 3000 raises TypeError
 Q11  evidence-copy      key c            as_arrived[0]['amount'] is 0 after the pass; the list is new, the dictionaries shared
 Q12  reject-loop        key b, d         prints '4 + 1 = 5' with KR-09053 kept; only (b) and (d) set aside both bad rows
 Q13  bank 24            key b            KR-02151: two Q2 rows at Rs 3,710 dated 2 August and 25 September; whole rows differ
 Q14  monday-number      key d            tile -25.9, per week -12.4, closed -11.0, reconciled -1.6 (Q1 Rs 1,90,00,000 after 14 rows, Rs 19,98,210)
 Q15  plus-clean         key 35.0 fall    51 less 11 May copies is 40 in Q1, 26 in Q2, 22 members: 1.82 to 1.18
 Q16  bank 52            key b, d, a, c   tracker key: profile, decide, reconcile, recompute
      exhibit 3A                          bars [117, 728, 1620, 1679, 721, 135], 135 of 5,000 at or beyond Rs 1,110
 Q17  bank 35            key a, c, d      tracker a, b, d relabelled a, c, d by the accepted order edit
 Q18  shuffle-sign       key c            prints '-880 0.981'; the class's count at +880 is 21, and at or below -880 is 24
 Q19  student-line       key b            12 orders (5 then 7) from 2 customers; coin-flip share 0.397
 Q20  bank 43            key a            sale Rs 3,395 against Rs 3,200 (+6.1); inside each segment -3.0 percent
 Q21  bank 45            key d            at the other group's 40/60 mix the sale group averages Rs 3,104 against Rs 3,200
 Q22  diwali-test        key c            judgement key: a random hold-out inside each segment; no computation
 Q23  debt-weights       key a            prints '71 -0.03 1.68'; HAP Table 3 gives 0.0 and 1.7, and -0.1 with -7.9
 Q24  debt-rows          key a            rows 30 to 44 hold 15 of the sheet's 20 countries: 5 left out
 Q25  orbiter-units      key c            1 lbf = 4.448 N, the report's factor of 4.45; judgement key
 Q26  flu-fit            key b, e         judgement key from Lazer and colleagues, 2014; no computation
 Q27  bing-alert         key b            judgement key from Kohavi and Thomke, 2017; no computation
 Q28  wald-buyers        key c            per member falls Rs 1,110 (33.9 percent); per buyer Rs 625 (17.3)
 Q29  tool-print         key b            the tool prints 'SW-1042: out for delivery' and the model reads 'None'
 Q30  agent-history      key a            B's call sends A's two messages first; with None as default it sends one
 Q31  agent-cost         key d            mean Rs 7.37, median Rs 1.60; C-07 is 81 percent of Rs 51.60
 Q32  sql-where          key WHERE        the filled query returns [('refund', 35)]; HAVING on status fails
 Q33  sql-having         key HAVING       WHERE COUNT(*) >= 30 fails in Postgres; HAVING applies the floor of 30
 Q34  sql-count          key 6            Postgres returns 6 for: SELECT COUNT(latency_ms) FROM calls;
 Q35  sql-avg            key 800          Postgres returns 800.0000000000000000 for: SELECT AVG(latency_ms) FROM calls;
 Q36  sql-rate           key 0            Postgres returns 0 for: SELECT COUNT(*) FILTER (WHERE status <> 'ok') / COUNT(*) FROM calls;
PROVED: all 36 timed items have a key that code, SQL, arithmetic or the tracker settles.
```

### The checks

`scripts/distractor_audit.py` passes the paper with no failure, the llm-tic-scrubber scanner finds
the paper, the key, the discussion guide and this file clean, `scripts/build_saturday_paper.py W01
--check` finds nothing stale, `scripts/xlsx_recalc.py` passes the item-analysis workbook, and
`scripts/verify.py content/W01/SAT` passes with no failure and no warning. The Word paper renders to 18 pages and the key to 19; every page was read at
60 dpi, every exhibit prints with its item, and the answer sheet fits one page.

### The discussion guide

Rewritten for this paper, with the 300-minute shape and every block's timing unchanged. The
most-missed round predicts the likeliest misses among the new items, each with the wrong answer it
tempts, the question to ask the room and the repair; the anchors round keeps the tracker's ten
anchors, each pointed at the items and stretch follow-ups that descend from it; the mock-interview
table gives every anchor twice and sets each follow-up beside an anchor it extends.

## 30 September 2026, v4: the blind sitting, and the paper raised again

A fresh agent sat the v3 paper cold, with the student file only. Every printed cell and query
reproduced its key, so no key was wrong, and the sitting found the paper short of the requester's
bar on eight counts. This section records what it found and what changed. The paper it describes
replaces the v3 paper above, so every Q number, count and source line in the earlier sections
belongs to an earlier paper.

### What the sitting found

1. **Difficulty.** Of the 21 items labelled hard, 5 were firmly hard and 3 hard at a stretch; the
   others were one idiom, one judgement with a cue or weak distractors, arithmetic or recall off any
   exhibit, or a two-way call. The bar is about 60 percent genuinely hard, with the printed level
   true, and a hard item takes at least three dependent steps on an exhibit.
2. **Set 2 contradicted the paper.** Its offer had 70 Retail-Plus customers and 160 customers in
   August at about Rs 4,900 each, where the rest of the paper has 22 Retail-Plus members, 9 of their
   orders in August, Rs 2,169 per member for Q2 and 69 customers in all. The week's own Thursday
   files carry the same gap: the exposure table's 160 customers are not the customers of the order
   file.
3. **Arguable keys.** The Student key printed a rate on 12 orders against Kavya's rule; the two
   ordering items could be argued in another order; the spreadsheet check counted countries where no
   debt band held all 20.
4. **Cues and leaks.** Anand's "no averages" rule gave away two items; the Part 3 intro defined the
   p-value; an advice key named the pattern item's answer; the A/B definition in one case gave away
   the Diwali design; Stretch 1 gave away the budget item; the duplicate item fell to elimination;
   the two word-bank blanks tested one idea twice with the clause defined in each stem; the agent
   history stem explained its own mechanism.
5. **Exhibits.** Three bar charts were read to a precision a bar cannot give; Tuesday's 200 rows and
   Wednesday's 201 were never reconciled on the page; the SQL exhibit had no date filter and counted
   only errors as failures while the match table counted timeouts too.
6. **Facts.** The debt table printed New Zealand at one year and -7.6 where Table 2 of Herndon, Ash
   and Pollin shows five years in its correct columns and -7.9 in Reinhart and Rogoff's; the orbiter
   stem merged two sentences of the board's report; the Bing key had to say how the case ended; the
   flu stem let a reader mark one reason of two.
7. **A real name in a hypothetical.** Part 5 named a real company beside invented, faulty agent logs.
8. **Form and wording.** One bare true or false; a hard label on two multiplications off any exhibit;
   "sales net of cancellations" that counted refunded orders; an ambiguous line on revenue per
   order; no line on why Rs 2.10 crore over 114 rows averages about Rs 1.8 lakh; two digit-grouping
   styles; a tile date that read two ways; an abrupt turn from Wald to Kavya.

### What changed

- **Hard items rebuilt on exhibits.** The payback item became a worked figure on Monday's orders by
  status, the median of the delivered orders; the budget item became Marketing's unit costs, with
  one change of four that flips the call; the reader item added the reconciliation the lost order
  slips past; the evidence item added an append, so the list and its dictionaries part company; the
  duplicate item became a worked Q2 figure on six rows of the export; Monday's number became a
  worked percentage; Part 3 opens on a new item that reads the Retail-Plus shuffle; the Student line
  reads a coin-toss table; the Wald item carries each figure's fall; the agent items count messages,
  trace an unknown order and size a capped bill; the two SQL blanks became one query to run in the
  head on a week's log.
- **Levels made true.** The p-value statements, the flu and Bing cases and the Diwali design print
  at medium; the discount arithmetic of bank 46 folded into the festival advice, where it is a step
  on an exhibit.
- **Set 2 moved out of Kalpa.** The offer set now sits in Part 5 at the illustrative delivery
  company, with its own numbers, and Kalpa's monsoon question is met by the Diwali design alone, so
  no Kalpa population appears twice.
- **Exhibit 3A rebuilt.** Kavya's shuffle keeps each member's two quarters together and swaps them
  on a coin toss, since the same 22 members spent in both quarters; gaps are rounded to the rupee,
  so the six bins are whole-rupee ranges that share no edge. It gives 145 of 5,000 at a fall of
  Rs 1,110 or more, 0.029, and 286 counted both ways, 0.057.
- **Cues removed.** Anand's rule and the p-value definition are gone from the intros; the advice
  options no longer name the pattern; every Diwali design uses chance somewhere; Stretch 1 asks about
  revenue per order instead.
- **Exhibits.** Every chart an item reads exactly carries its values in a table; the Part 2 intro
  gives the 201 rows against Tuesday's 200; the failing-tools query filters the week and counts every
  status but ok, as the match table does; the match instruction says PostgreSQL.
- **Facts.** The debt table now gives the seven countries as the working spreadsheet carried them,
  from Table 2's columns for Reinhart and Rogoff: New Zealand's one counted year, 1951, at -7.9
  where its own sheet said -7.6 (note 6), with its four earlier years left out; the equal-weight
  figure is -0.07, which rounds to the published -0.1. The spreadsheet check now spans the rows each
  formula covers, since only ten countries ever sat above 90 percent (Herndon, Ash and Pollin, page
  8). The orbiter stem keeps the report's two sentences apart. The Bing key and the discussion say
  the lift was real. The flu stem asks for both reasons.
- **No real company in Part 5.** The company is unnamed, and its order numbers carry no prefix.
- **Form.** Bank 11 folds into a true or false with lettered reasons; bank 47's figure prints as
  Rs 4,80,000; Meera's sales are defined in the stem; the tile is an extract taken on 15 September;
  the Part 1 intro says that 20 Business rows carried Rs 2.08 crore of Q1's Rs 2.10 crore; the Wald
  stem turns to Kalpa with "Back at Kalpa".
- **Ledger.** The three v3 entries for bank 11, 24 and 43, all proposed and never accepted, are
  removed because those items now fold. Bank 47 gains a proposed stem edit for the grouping, bank 51
  a proposed stem and option edit that says what each of the first two rungs checks, and bank 52 a
  proposed stem edit that carries Kavya's rule for the pass.

### The paper as it prints

35 timed items in five parts, 117 minutes at the blueprint's pace against the 120-minute slot, with
2 easy, 12 medium and 21 hard items, which is 5.7, 34.3 and 60.0 percent by count.

| Part | Items | Minutes | Easy | Medium | Hard |
|---|---|---|---|---|---|
| 1. Where the revenue went | Q1 to Q7 | 21.5 | 2 | 1 | 4 |
| 2. Which Q1 figure is right | Q8 to Q15 | 29 | 0 | 2 | 6 |
| 3. Real, or the wobble | Q16 to Q20 | 17 | 0 | 2 | 3 |
| 4. The same traps, in public | Q21 to Q26 | 18 | 0 | 4 | 2 |
| 5. An offer, an agent and its logs | Q27 to Q35 | 31.5 | 0 | 3 | 6 |

| Q | Source | Format | Level | Min | Day | The trap it stages |
|---|---|---|---|---|---|---|
| Q1 | bank 47 | Applied maths | Easy | 1.5 | Mon | the mean read as the typical order when one bulk order drives it |
| Q2 | new: sales-net | One correct option | Hard | 4 | Mon | a status test that is true for every order, so cancelled orders count as sales |
| Q3 | new: first-order | Applied maths | Hard | 4 | Mon | the mean, or the median of every order, priced as the typical paid first order |
| Q4 | new: quarter-counter | One correct option | Hard | 4 | Tue | a counter reset inside the segment loop, so each quarter keeps Student's count |
| Q5 | bank 20 | One correct option | Easy | 1.5 | Tue | a hypothesis before the drop is confirmed |
| Q6 | new: budget-flip | One correct option | Hard | 4 | Tue | a branch chosen before the cost of moving each branch is worked out |
| Q7 | bank 51 | Order the steps | Medium | 2.5 | Tue | the like-with-like rung taken before each figure is confirmed |
| Q8 | new: reader-header | One correct option | Hard | 4 | Wed | an extra next() on a DictReader, which drops the first order while the pass still reconciles |
| Q9 | new: text-compare | True or false, with the reason | Medium | 2.5 | Mon | text compared as text, so '4500' sorts after '30000' without an error |
| Q10 | new: evidence-copy | True or false, with the reason | Hard | 4 | Wed | a shallow copy that shares the dictionaries the pass rewrites |
| Q11 | new: reject-loop | More than one correct | Hard | 4 | Wed | rows removed from the list being walked, so a row is skipped while the counts still close |
| Q12 | new: dup-rule | Applied maths | Hard | 4 | Wed | a whole-row check that misses a re-sent order carrying a new date |
| Q13 | new: monday-number | Scenario set | Hard | 4 | Tue | the tile's mismatched windows, and a Q1 still holding its copied rows |
| Q14 | new: plus-clean | Scenario set | Hard | 4 | Wed | a rate on the export with May's 11 copied rows still in Q1 |
| Q15 | bank 52 | Order the steps | Medium | 2.5 | Wed | recomputing before reconciling |
| Q16 | new: plus-real | One correct option | Hard | 4 | Thu | counting both tails where the rule counts one, or a per-member fall written as the tier's |
| Q17 | bank 35 | More than one correct | Medium | 2.5 | Thu | the p-value read as the chance the hypothesis is true |
| Q18 | new: shuffle-sign | One correct option | Hard | 4 | Thu | a count run against the direction of the claim, so a real fall reads as p = 0.981 |
| Q19 | new: student-line | One correct option | Hard | 4 | Thu | the wrong rows of the coin-toss table, or a large share read as proof of no effect |
| Q20 | new: diwali-test | One correct option | Medium | 2.5 | Thu | a comparison of groups that differed before the offer, whatever the random draw |
| Q21 | new: debt-weights | Scenario set | Hard | 4 | Tue | an average of averages that gives one counted year the weight of nineteen |
| Q22 | new: debt-rows | Scenario set | Medium | 2.5 | Wed | a formula that covered 15 of 20 rows without an error |
| Q23 | new: wald-buyers | True or false, with the reason | Hard | 4 | Thu | a per-buyer denominator that drops the members who stopped buying |
| Q24 | new: orbiter-units | One correct option | Medium | 2.5 | Wed | one of two disagreeing figures averaged or trusted before the gap is explained |
| Q25 | new: flu-fit | More than one correct | Medium | 2.5 | Thu | a proxy that tracks the season, and a fit found among millions of tries |
| Q26 | new: bing-alert | One correct option | Medium | 2.5 | Thu | a result too good to be true shipped or discarded before the plumbing is checked |
| Q27 | new: sale-mix | Scenario set | Hard | 4 | Thu | a blended lift credited to the offer while spend fell inside both tiers |
| Q28 | new: sale-advice | Scenario set | Hard | 4 | Thu | a deeper cut on a mix effect, and the break-even added where it multiplies |
| Q29 | new: tool-print | One correct option | Hard | 4 | Tue | a tool that prints instead of returning, so the model reads 'None' |
| Q30 | new: agent-history | One correct option | Hard | 4 | Tue | a mutable default argument that carries one customer's messages into another's call |
| Q31 | new: agent-cost | One correct option | Hard | 4 | Mon | a mean driven by one looping conversation, or a capped run counted as free |
| Q32 | new: sql-failing | One correct option | Hard | 4 | Wed | a failure rule that leaves timeouts out, a missing week filter, or no HAVING |
| Q33 | new: sql-count | Match the following | Medium | 2.5 | Wed | COUNT(column) read as a count of rows |
| Q34 | new: sql-avg | Match the following | Medium | 2.5 | Wed | AVG read as counting a NULL as zero |
| Q35 | new: sql-rate | Match the following | Medium | 2.5 | Tue | an integer division that returns 0 |

### Formats and their counts

| Format | Items | Count |
|---|---|---|
| One correct option | Q2, Q4, Q5, Q6, Q8, Q16, Q18, Q19, Q20, Q24, Q26, Q29, Q30, Q31, Q32 | 15 |
| Scenario set, in three sets | Set 1: Q13 and Q14; Set 2: Q21 and Q22; Set 3: Q27 and Q28 | 6 |
| True or false, with the reason | Q9, Q10, Q23 | 3 |
| More than one correct | Q11, Q17, Q25 | 3 |
| Applied maths | Q1, Q3, Q12 | 3 |
| Match the following, one table of six values | Q33 to Q35 | 3 |
| Order the steps | Q7, Q15 | 2 |

No plain true or false and no word bank print. The three more-than-one keys are b and d, a, c and
d, and b and e, so no letter sits in all three. Across the 24 option items the audit counts keys at
a 7 times, b 7, c 6, d 7 and e once. Of the 35 items, 6 are public cases and 9 sit at the
illustrative delivery company.

### The fate of every bank item

Five bank items print; the other 47 fold into a printed item that tests the same concept; none moves
to the stretch page. Each fold's reason is in the source file's `folded` block and prints in the key.

| Bank | Printed as | What changed on the paper |
|---|---|---|
| 47 | Q1 | Stem edit, proposed: Rs 4,80,000 in the Indian grouping; paced at 1.5 minutes where the tracker gives 4 |
| 20 | Q5 | Paced at 1.5 minutes where the tracker gives 2 |
| 51 | Q7 | Stem and options b and d reworded, proposed, so the order of the first two rungs follows |
| 52 | Q15 | Stem reworded, proposed, to carry Kavya's rule that fixes the order |
| 35 | Q17 | The accepted order edit; printed at medium and 2.5 minutes where the tracker says hard |

| Bank | Tracker type and level | Folded into |
|---|---|---|
| 1 | Fill in the blank, Easy | Q28 (new: sale-advice) |
| 2 | Fill in the blank, Easy | Q14 (new: plus-clean) |
| 3 | Fill in the blank, Easy | Q29 (new: tool-print) |
| 4 | Fill in the blank, Easy | Q9 (new: text-compare) |
| 5 | Fill in the blank, Easy | Q11 (new: reject-loop) |
| 6 | Fill in the blank, Medium | Q18 (new: shuffle-sign) |
| 7 | Fill in the blank, Easy | Q19 (new: student-line) |
| 8 | Fill in the blank, Medium | Q25 (new: flu-fit) |
| 9 | True or false, Medium | Q17 (bank 35) |
| 10 | True or false, Easy | Q3 (new: first-order) |
| 11 | True or false, Medium | Q9 (new: text-compare) |
| 12 | True or false, Easy | Q17 (bank 35) |
| 13 | True or false, Easy | Q13 (new: monday-number) |
| 14 | True or false, Easy | Q19 (new: student-line) |
| 15 | True or false, Easy | Q20 (new: diwali-test) |
| 16 | True or false, Hard | Q27 (new: sale-mix) |
| 17 | One correct option, Easy | Q6 (new: budget-flip) |
| 18 | One correct option, Easy | Q6 (new: budget-flip) |
| 19 | One correct option, Easy | Q3 (new: first-order) |
| 21 | One correct option, Medium | Q13 (new: monday-number) |
| 22 | One correct option, Easy | Q29 (new: tool-print) |
| 23 | One correct option, Medium | Q11 (new: reject-loop) |
| 24 | One correct option, Medium | Q12 (new: dup-rule) |
| 25 | One correct option, Medium | Q11 (new: reject-loop) |
| 26 | One correct option, Hard | Q19 (new: student-line) |
| 27 | One correct option, Easy | Q19 (new: student-line) |
| 28 | One correct option, Medium | Q24 (new: orbiter-units) |
| 29 | One correct option, Hard | Q6 (new: budget-flip) |
| 30 | More than one correct, Easy | Q14 (new: plus-clean) |
| 31 | More than one correct, Medium | Q13 (new: monday-number) |
| 32 | More than one correct, Easy | Q15 (bank 52) |
| 33 | More than one correct, Easy | Q33 (new: sql-count) |
| 34 | More than one correct, Medium | Q20 (new: diwali-test) |
| 36 | Scenario set, Easy | Q14 (new: plus-clean) |
| 37 | Scenario set, Medium | Q6 (new: budget-flip) |
| 38 | Scenario set, Medium | Q6 (new: budget-flip) |
| 39 | Scenario set, Hard | Q6 (new: budget-flip) |
| 40 | Scenario set, Easy | Q11 (new: reject-loop) |
| 41 | Scenario set, Medium | Q11 (new: reject-loop) |
| 42 | Scenario set, Hard | Q13 (new: monday-number) |
| 43 | Scenario set, Hard | Q27 (new: sale-mix) |
| 44 | Scenario set, Medium | Q27 (new: sale-mix) |
| 45 | Scenario set, Hard | Q28 (new: sale-advice) |
| 46 | Applied maths, Hard | Q28 (new: sale-advice) |
| 48 | Applied maths, Easy | Q13 (new: monday-number) |
| 49 | Applied maths, Medium | Q16 (new: plus-real) |
| 50 | Applied maths, Medium | Q28 (new: sale-advice) |

### Sources read for this pass

The six public sources are the ones the v3 section lists, each checked on 30 September 2026. This
pass read further in two of them. Herndon, Ash and Pollin's working paper
(https://peri.umass.edu/wp-content/uploads/joomla/images/WP322.pdf, checked 30 Sep 2026) gave Table 2's columns for
Reinhart and Rogoff's calculation, note 6 on the transcription of New Zealand's -7.6 as -7.9, and
page 8's count of ten countries ever above 90 percent. The Mars Climate Orbiter board's Phase I
report (checked 30 Sep 2026, https://llis.nasa.gov/llis_lib/pdf/1009464main1_0641-mr.pdf) gave the
two sentences the orbiter stem now keeps apart: concerns at the working level through spring and
summer, reported informally, and the Doppler-only solutions that, as the craft approached Mars,
consistently placed it closer to the planet. No real company is named in Part 5, so the Swiggy page
listed in the v3 section no longer supports anything on the paper.

### The proof run

The proof script now settles all 35 keys; the run of 30 September 2026, on Python 3.11.15,
psycopg2 2.9.13 and PostgreSQL 16.13, printed:

```
Week 1 Saturday paper: 35 timed items. Each line gives the printed Q, the item, its key and what proves it.
  Q1  bank 47          key 1,400; 97,080 the third of five sorted values; 4,85,400 over 5 is 97,080
  Q2  sales-net        key b            prints '30 orders, Rs 544810'; Meera's delivered and returned are 26 orders, Rs 5,35,760
  Q3  first-order      key Rs 2,060     median of the 21 delivered orders, the 11th; mean 24,800, all-30 median 2,205
  Q4  quarter-counter  key d            prints '{'Q1': 5, 'Q2': 7} +40.0%': the counter holds Student's count; the file says 114 and 86
  Q5  bank 20          key a            tracker key: the first rung is confirming the drop is real
  Q6  budget-flip      key c            Rs 2.00 a rupee against Rs 2.50; only a Rs 800 win-back, Rs 1.88, flips it
  Q7  bank 51          key b, d, e, a, c tracker key: real, like with like, decompose, isolate, hypothesise
  Q8  reader-header    key c            prints '200 KR-02002'; the pass closes 200 = 185 + 15 and KR-02001 is in neither
  Q9  text-compare     key d            '4500' < '30000' is False, silently; every CSV amount is text
 Q10  evidence-copy    key c            as_arrived keeps 2 rows and its first amount is now 0; rows holds 3
 Q11  reject-loop      key b, d         prints '4 + 1 = 5' with KR-09053 kept; only (b) and (d) set aside both bad rows
 Q12  dup-rule         key Rs 10,930    identity rule keeps 3 Q2 orders; the whole-row check leaves Rs 14,640
 Q13  monday-number    key 1.6 fall     tile -25.9, weekly -12.4, closed -11.0; Q1 less Rs 20,00,000 of copies gives -1.6
 Q14  plus-clean       key 35.0 fall    51 less 11 May copies is 40 in Q1, 26 in Q2, 22 members: 1.82 to 1.18
 Q15  bank 52          key b, d, a, c   tracker key: profile, decide, reconcile, recompute
 Q16  plus-real        key a            paired shuffle bars [141, 766, 1526, 1683, 739, 145]; 145 of 5,000 reach the fall, 0.029; both ways 0.057
 Q17  bank 35          key a, c, d      tracker a, b, d relabelled a, c, d by the accepted order edit
 Q18  shuffle-sign     key c            prints '-880 0.981'; the class's count at +880 is 21, and at or below -880 is 24
 Q19  student-line     key b            12 orders (5 then 7) from 2 customers; 7 or more in Q2 in 1,985 of 5,000 worlds
 Q20  diwali-test      key a            judgement key: a random hold-back inside each segment
 Q21  debt-weights     key a            prints '71 -0.07 1.68'; -0.07 rounds to the published -0.1; HAP Table 3 gives 1.7
 Q22  debt-rows        key d            the formula spans rows 30 to 44, 15 of the sheet's 20 country rows
 Q23  wald-buyers      key d            per member falls Rs 1,110 (33.9 percent); per buyer Rs 625 (17.3); 6 stopped
 Q24  orbiter-units    key b            1 lbf = 4.448 N, the report's factor of 4.45; judgement key
 Q25  flu-fit          key b, e         judgement key from Lazer and colleagues, 2014; no computation
 Q26  bing-alert       key b            judgement key from Kohavi and Thomke, 2017; the lift was real
 Q27  sale-mix         key 2.5 fall     blend +6.8; at the no-offer mix 0.4 x 1,470 + 0.6 x 580 = 936, -2.5 against 960
 Q28  sale-advice      key c            at 25 percent off orders must rise by 1 over 0.75, a third; each tier fell
 Q29  tool-print       key b            the model reads 'out for delivery', 'None', 'delivered'; no error is raised
 Q30  agent-history    key a            the three calls send 1, 3 and 5 messages; with None as default each sends 1
 Q31  agent-cost       key d            median Rs 1.60, mean Rs 7.26; capped at 5 calls C-07 costs Rs 2.00, saving Rs 40.00
 Q32  sql-failing      key a            Postgres returns order_status 34 and refund 38; 'error' alone gives refund 35
 Q33  sql-count        key 6            Postgres returns 6 for: SELECT COUNT(latency_ms) FROM calls;
 Q34  sql-avg          key 800          Postgres returns 800.0000000000000000 for: SELECT AVG(latency_ms) FROM calls;
 Q35  sql-rate         key 0            Postgres returns 0 for: SELECT COUNT(*) FILTER (WHERE status <> 'ok') / COUNT(*) FROM calls;
PROVED: all 35 timed items have a key that code, SQL, arithmetic or the tracker settles; 21 are hard.
```

### The checks

`scripts/distractor_audit.py` passes the paper with no failure, the llm-tic-scrubber scanner finds
the paper, the key, the discussion guide and this file clean, and `scripts/build_saturday_paper.py
W01 --check` finds nothing stale. The Word paper renders to 23 pages and the key to 20; every page
was read at 60 dpi, every exhibit prints with its item, the charts' labels are legible, and the
answer sheet fits one page.

### The discussion guide

Rewritten for this paper, with the 300-minute shape and every block's timing unchanged. The
most-missed round predicts the likeliest misses among the rebuilt items, each with the wrong answer
it tempts, the question to ask the room and the repair; it says how the Bing case ended and names
the two customers behind Student's 12 orders. The anchors round keeps the tracker's ten anchors,
each pointed at the items that descend from it.
