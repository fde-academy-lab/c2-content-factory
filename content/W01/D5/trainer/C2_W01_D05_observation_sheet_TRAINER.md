# Where is each learner at each mark of the lab, and which step do they not own yet?

**TRAINER ONLY.** Each TA keeps one sheet, with one line per learner in that TA's rows. The data is
`v3-lab`, proposed for client zero v2.3. Nothing on this sheet is a score, and neither the sheet nor
any tally of it is shown to the room, on a wall or on a screen. It sets each learner's first stretch
or remedial task and tells the trainer which reserve slides, if any, the debrief's three chapters
make room for.

**Who needs the answer.** Each learner, whose first stretch or remedial task comes from this sheet,
and the trainer, who lingers in the debrief where the tally says most of the room broke. A step
recorded wrongly sends a learner to the wrong practice problem tonight.

## How does a TA observe the lab without helping with the method?

- Walk your rows at each mark: 20, 50, 65, 90, 105 and 120 minutes. Record the step each learner is
  on, from their screen, without a word.
- Answer no method question. The only sentence you say about the work is "what would you check?"
  Fix environment problems (a Codespace that will not start, a kernel that dies) at once, and note
  the minutes lost in the last column.
- At the 120-minute mark, copy each learner's `notebooks/output/` folder before the second look
  begins. The sheet's last columns are filled from that copy.

## Which step should a learner have reached at each mark, and which stalls do you code?

The expected step assumes the learner keeps the brief's pace.

| Mark | Expected step | Stall codes to watch for |
|---|---|---|
| 20 | Profile read; moving to clean | P1 computed a total before any profile; P2 profile has no distinct count; P3 the mean quoted as the typical order |
| 50 | Cleaning done, log written | C1 no log rows; C2 text amount set to zero or skipped with no log line; C3 repeats not found; C4 empty segment dropped, or left in a blank group, with no log line (a flagged unknown with its log line is correct) |
| 65 | Reconciled | R1 no count check; R2 a count check and no rupee check; R3 checks written and failing, and the learner moved on |
| 90 | Tree built | D1 total only, no segments; D2 a rate without its order count; D3 frequency named as the branch on uncleaned rows |
| 105 | Shuffle run | Code the unit from the shuffle cell and ignore the p on the screen. T1 segment labels shuffled across single orders, splitting each customer's orders; T1b a customer's two quarters pooled: each customer's Q1 and Q2 figures pooled and the quarter labels dealt, or the orders of both quarters pooled and the quarter label dealt across single orders; T2 a test on Business; T3 the p-value sentence says "chance we are wrong"; T4 a one-way p reported for a direction picked after looking |
| 120 | Note written | N1 no caveat; N2 the corporate rate as the headline; N3 no action or no cost; N4 a mean order in the claim as the typical one |

## What goes on the sheet?

Write the step reached at each mark (P, C, R, D, T or N) and any stall code seen, one line per
learner. Learner names are written only in the TA's own copy and never in a shared file.

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

## Which wrong number on a screen means which stall?

A hurried run prints these wrong numbers, and a TA should recognise each one without reading the
code; all of them are in `trainer/C2_W01_D05_lab_key_TRAINER.md`.

| On the screen | What it means |
|---|---|
| Q2 up 11.8 percent | Repeats kept and the text amount lost: the reconciliation skipped |
| Q2 down 6.4 percent | Repeats kept, text amount read |
| Q2 down 14.6 percent | Repeats removed, text amount set to zero |
| Q1 Rs 50,63,000 with 0 rejects | The pass that looks clean |
| Retail-Core orders per customer 1.77 in Q2 | The tree read on the uncleaned rows |
| Any p-value | Read the shuffle cell and code its unit, whatever the number says. Labels moved with whole customers, or each customer's own two quarters flipped, mean a fair route and no stall; labels shuffled across single orders mean T1; and each customer's Q1 and Q2 figures pooled and dealt, or the quarter label dealt across both quarters' single orders, mean T1b. A learner who ran a fair route reaches a number anywhere from 0.0005 to 0.043, and the lab key lists every route with its number |
| Mean order about Rs 52,000 quoted as typical | The typical-order trap |
| Segments that do not add back to the quarter, or a blank group with no log line; Retail-Plus Q2 read as 34 orders and Rs 93,670 with nothing said about the unknown order | The empty segment dropped or bucketed silently, C4. The same 34 orders and Rs 93,670 with the unknown named, flagged and reconciled is a correct run |
| Q2 down 28.5 percent, and a shuffle cell that keeps each customer's orders together | A correct run, whatever its p |

## What does the lunch tally tell the trainer?

The debrief runs all three chapters whatever the tally says: the reconciliation skipped before lunch,
the pass that looks clean and the headline on too few orders after it. The tally decides where the
trainer lingers and which reserve slide, a self-study slide the chapter otherwise leaves to the
notebook, runs live. Count, across your rows,
the learners with each break at the snapshot, and give the counts to the trainer before the afternoon
starts.

| Break | Count from | Debrief slides | If the count is more than a quarter of the room |
|---|---|---|---|
| The reconciliation skipped | R1, R2 or R3 | Chapter 1, S2 to S17 | It is already the longest chapter; read two second-look lines instead of one |
| The pass that looks clean | C2 or R2 | Chapter 2, S18 to S30 | Type S24's options your-turn cell slowly, then two learners name their own log line |
| The wrong branch | D3 | D16 | Run D16 live for two minutes at the end of chapter 1 |
| The empty segment | C4 | D28 | Run D28 live for two minutes in place of S29 |
| The headline on too few orders | D2 or N2 | Chapter 3, S31 to S48 | Type S39's option D your-turn cell slowly |
| The wrong unit | T1 or T1b | D45 | Run D45 for three minutes in place of S44 |
| The typical order | P3 or N4 | D46 | Run D46 for three minutes in place of S44, unless D45 already runs there; then say the median in one sentence at S47 and leave D46 to self-study |

Chapter 2 and chapter 3 hold ten minutes each; a reserve slide that runs takes its minutes from the
chapter's own second-route slide, which stays in the notebook for self-study.

## Which practice task does each learner start from?

| What the sheet shows | The learner's task in the practice lab |
|---|---|
| Stalled at P or C | Practice problem 1, then 2, with the TA beside them for the first ten minutes |
| Reached R and skipped it, or R2 | Practice problem 2, and the rupee check written before anything else |
| Stalled at D or T, or T1 | Practice problem 3 |
| Finished with a correct run | Practice problem 4, then the stretch: rerun the whole method on the practice export in 45 minutes |

Tell each learner their step privately during the rehearsal's round one, one learner at a time and
never aloud or to a group.
