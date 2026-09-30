# TA observation sheet: the AI-free lab

**TRAINER ONLY.** One sheet per TA, one line per learner in that TA's rows. The data is `v3-lab`,
proposed for client zero v2.3. Nothing on this sheet is a score, nothing is shown to the room, and
no tally of it goes on a wall or a screen. It sets each learner's first stretch or remedial task and
tells the trainer which reserve slides, if any, the debrief's three chapters make room for.

## How to observe

- Walk your rows at each mark: 20, 50, 65, 90, 105 and 120 minutes. Record the step each learner is
  on, from their screen, without a word.
- Answer no method question. The only sentence you say about the work is "what would you check?"
  Environment problems (a Codespace that will not start, a kernel that dies) you fix at once, and
  you note the minutes lost in the last column.
- At the 120-minute mark, copy each learner's `notebooks/output/` folder before the second look
  begins. The copy is what the sheet's last columns record.

## The marks

The step a learner should have reached by each mark, if they keep the brief's pace.

| Mark | Expected step | Stall codes to watch for |
|---|---|---|
| 20 | Profile read; moving to clean | P1 computed a total before any profile; P2 profile has no distinct count; P3 the mean quoted as the typical order |
| 50 | Cleaning done, log written | C1 no log rows; C2 text amount set to zero or skipped with no log line; C3 repeats not found; C4 empty segment dropped, or left in a blank group, with no log line (a flagged unknown with its log line is correct) |
| 65 | Reconciled | R1 no count check; R2 a count check and no rupee check; R3 checks written and failing, and the learner moved on |
| 90 | Tree built | D1 total only, no segments; D2 a rate without its order count; D3 frequency named as the branch on uncleaned rows |
| 105 | Shuffle run | Code the unit from the shuffle cell, never the p on the screen. T1 segment labels shuffled across single orders, splitting each customer's orders; T1b a customer's two quarters pooled: each customer's Q1 and Q2 figures pooled and the quarter labels dealt, or the orders of both quarters pooled and the quarter label dealt across single orders; T2 a test on Business; T3 the p-value sentence says "chance we are wrong"; T4 a one-way p reported for a direction picked after looking |
| 120 | Note written | N1 no caveat; N2 the corporate rate as the headline; N3 no action or no cost; N4 a mean order in the claim as the typical one |

## The sheet

Write the step reached at each mark (P, C, R, D, T or N) and any stall code seen. Use one line per
learner. Learner names are written in the TA's own copy only, never in a shared file.

| Learner | 20 | 50 | 65 | 90 | 105 | 120 | Reconciled at the snapshot? | Headline at the snapshot | Minutes lost to environment |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | yes / count only / no | | |
| | | | | | | | yes / count only / no | | |
| | | | | | | | yes / count only / no | | |
| | | | | | | | yes / count only / no | | |
| | | | | | | | yes / count only / no | | |
| | | | | | | | yes / count only / no | | |
| | | | | | | | yes / count only / no | | |
| | | | | | | | yes / count only / no | | |
| | | | | | | | yes / count only / no | | |
| | | | | | | | yes / count only / no | | |

## Reading a headline from across the room

The wrong numbers a hurried run prints, so a TA recognises each without reading the code. All are in
`trainer/C2_W01_D05_lab_key_TRAINER.md`.

| On the screen | What it means |
|---|---|
| Q2 up 11.8 percent | Repeats kept and the text amount lost: the reconciliation skipped |
| Q2 down 6.4 percent | Repeats kept, text amount read |
| Q2 down 14.6 percent | Repeats removed, text amount set to zero |
| Q1 Rs 50,63,000 with 0 rejects | The pass that looks clean |
| Retail-Core orders per customer 1.77 in Q2 | The tree read on the uncleaned rows |
| Any p-value | Read the shuffle cell and code its unit, never the number. Labels moved with whole customers, or each customer's own two quarters flipped: a fair route, no stall. Labels shuffled across single orders: T1. Each customer's Q1 and Q2 figures pooled and dealt: T1b. A learner who ran a fair route reaches a number anywhere from 0.0005 to 0.043, and the lab key lists every route with its number |
| Mean order about Rs 52,000 quoted as typical | The typical-order trap |
| Segments that do not add back to the quarter, or a blank group with no log line; Retail-Plus Q2 read as 34 orders and Rs 93,670 with nothing said about the unknown order | The empty segment dropped or bucketed silently, C4. The same 34 orders and Rs 93,670 with the unknown named, flagged and reconciled is a correct run |
| Q2 down 28.5 percent, and a shuffle cell that keeps each customer's orders together | A correct run, whatever its p |

## Over lunch: the tally for the debrief

The debrief runs all three chapters whatever the tally says: the reconciliation skipped before lunch,
the pass that looks clean and the headline on too few orders after it. The tally decides where the
trainer lingers and which reserve slide replaces a chapter's self-study slide. Count, across your rows,
the learners with each break at the snapshot, and give the counts to the trainer before the afternoon
starts.

| Break | Count from | Debrief slides | If the count is more than a quarter of the room |
|---|---|---|---|
| The reconciliation skipped | R1, R2 or R3 | Chapter 1, S1 to S11 | Already the longest chapter; read two second-look lines instead of one |
| The pass that looks clean | C2 or R2 | Chapter 2, S12 to S20 | Run S17's options cell slowly, then two learners name their own log line |
| The wrong branch | D3 | D10 | Run D10 live for two minutes at the end of chapter 1 |
| The empty segment | C4 | D19 | Run D19 live for two minutes in place of S20 |
| The headline on too few orders | D2 or N2 | Chapter 3, S21 to S31 | Run S26's options cell slowly |
| The wrong unit | T1 or T1b | D29 | Run D29 for three minutes in place of S28 |
| The typical order | P3 or N4 | D30 | Run D30 for three minutes in place of S27's call-out |

Chapter 2 and chapter 3 hold ten minutes each; a reserve slide that runs takes its minutes from the
chapter's own second-route slide, which stays in the notebook for self-study.

## After the day: the first stretch and remedial tasks

| What the sheet shows | The learner's task in the practice lab |
|---|---|
| Stalled at P or C | Practice problem 1, then 2, with the TA beside them for the first ten minutes |
| Reached R and skipped it, or R2 | Practice problem 2, and the rupee check written before anything else |
| Stalled at D or T, or T1 | Practice problem 3 |
| Finished with a correct run | Practice problem 4, then the stretch: rerun the whole method on the practice export in 45 minutes |

Tell each learner their step privately during the rehearsal's round one, one at a time. Never aloud,
never to a group.
