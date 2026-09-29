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

## Open points for the orchestrating session

- Set 1's situation uses the same counts as the Week 2 Tuesday data (50 orders with two payment rows,
  30 delivered orders with none). The room found both on Tuesday, so the paper restates a finding;
  the guide tells the Academic TA to keep the discussion to what the room found.
- mermaid-cli 12.0.0 is the version installed in this environment, and `render_mermaid` in
  `scripts/build_cheatsheet.py` passes `-w 2400`, which that version rejects, so every exhibit PNG
  failed without an error. The build here ran with mermaid-cli 11.17.0 installed outside the
  repository and put first on PATH.
- On page 3 of the Word key the table continues with an empty row under the repeated header, which
  comes from the builder's table split.
- The first marking step in both keys uses the third-person form of the verb mark, which is builder
  text in `render_key` and `docx_spec`; swapping it for "checks" keeps the word out of every file.
