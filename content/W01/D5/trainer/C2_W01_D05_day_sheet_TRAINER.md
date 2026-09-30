# Day sheet: Week 1, Friday. The week rebuilt alone, and the note defended aloud

**TRAINER ONLY.** Nothing on this page reaches a learner. The lab data is `v3-lab`, **proposed for
client zero v2.3** and not yet locked.

Posts to <!-- sync:module:W01/D5 -->Module 1: Foundations of AI and Data<!-- /sync:module:W01/D5 -->, on <!-- sync:day-date:W01/D5 -->Fri 09 Oct 2026<!-- /sync:day-date:W01/D5 -->.

| | |
|---|---|
| **Start from** | Monday to Thursday, all of it. Today teaches nothing new. |
| **Go as far as** | Every learner hands in a lab notebook and a note, and defends Thursday's note once. |
| **Stop before** | Any new technique and any SQL; Week 2 opens that on Monday. Pandas stays closed. |
| **Comes later** | Saturday's paper tests the week on paper; Monday moves the same method into the warehouse. |
| **Cut first** | The rehearsal's second round of call-outs. The observed lab and round one always run in full. |

**The domain.** Kalpa Retail is the room's first business. Its story (how it makes money, who
decides what, its metrics as formulas) is the retail and e-commerce dossier,
`content/W01/D1/study-notes/C2_W01_D01_domain_retail_STUDENT.md`; its section 4 is who decides
what (Anand's "Do your numbers match my books?" is its finance row) and section 5 is the metrics as
formulas, the revenue tree among them. Its one-page card is to ship in `content/W01/D1/cheatsheets/`.
Today retells none of it: every chapter names the metric at stake
(booked revenue per quarter and its branches), who at Kalpa asks for it and what a wrong number
costs, and a learner who is unsure of a term is sent to the dossier.

**Kavya's terms, said in the first minute.** "Before anything goes to Meera, rebuild the week from a
raw export with no assistant and no notes. Then say it to me the way you will say it to her, because
I will push the way Marketing will."

---

## Morning, 180 minutes

```mermaid
flowchart LR
    T["<b>Terms</b><br/>10 min"] --> L["<b>The lab</b><br/>120 min"] --> S["<b>Second look</b><br/>20 min"] --> B["<b>Break</b><br/>10 min"] --> D["<b>Debrief</b><br/>chapter 1, 20 min"]
    classDef core fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class L core
```

| Part | Slides | Beside it | What must land | If short of time |
|---|---|---|---|---|
| Terms, 10 | Lab deck S1 to S6 | Everyone opens the lab notebook and runs its first cell | The four rules; observed, never scored; the first cell runs on every screen before the clock | Read S5 and S6 only |
| The lab, 120 | Lab deck S7, left up | `exercises/unguided/C2_W01_D05_lab_brief_STUDENT.md`, `notebooks/C2_W01_D05_lab_STUDENT.ipynb`; the TAs on the observation sheet | Silence. Time called at 60, 90 and 110 minutes, nothing else | Never cut |
| Second look, 20 | Lab deck S8, S9 | Output folders copied at the 120-minute mark first | Each learner compares their totals with the control totals and writes one line | To 10 minutes |
| Break, 10 | | | | |
| Debrief chapter 1, 20 | Debrief deck S1 to S11 (D2 and D10 self-study) | `notebooks/C2_W01_D05_01_reconciliation_skipped_STUDENT.ipynb` on the projector from S5 | The reconciliation skipped: +11.8 as sent, -14.6 on counts alone, -28.5 on counts and rupees; option C with its switch; the walk back; two second-look lines read aloud | S9 to one sentence |

## Afternoon, 180 minutes

```mermaid
flowchart LR
    D["<b>Debrief</b><br/>chapters 2 and 3, 20 min"] --> R1["<b>Rehearsal 1</b><br/>pairs, 50 min"] --> R2["<b>Rehearsal 2</b><br/>call-outs, 50 min"] --> C["<b>Design cases</b><br/>40 min"] --> K["<b>Kahoot, close</b><br/>20 min"]
    classDef core fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class R1 core
```

| Part | Slides | Beside it | What must land | If short of time |
|---|---|---|---|---|
| Debrief chapters 2 and 3, 20 | Chapter 2, S12 to S20; chapter 3, S21 to S28; then S31 (D13, D19, D22, D29, D30 self-study unless the tally calls one) | `notebooks/C2_W01_D05_02_pass_that_looks_clean_STUDENT.ipynb`, then `03_headline_on_few_orders`; the TAs' lunch tally | Ten minutes each: zero rejects and Q1 Rs 9,85,000 short, option C for a value that will not convert; the corporate -29.2 percent said as counts, option C for the lead, p = 0.0195 on customers | S20 and S28 to one sentence each; never a whole chapter |
| Rehearsal round one, 50 | Rehearsal deck S1 to S6 | `exercises/guided/C2_W01_D05_rehearsal_brief_STUDENT.md`, whose sharpest Marketing push (the monsoon sale's Rs 3,395 against Rs 3,200) is modelled once aloud with a TA as Marketing; the feedback cards; a model answer for every push in `trainer/C2_W01_D05_rehearsal_key_TRAINER.md`, for a stuck pair | Every learner defends Thursday's note twice; the TAs tell each learner their marked step, privately | Pair two to one defence each |
| Rehearsal round two, 50 | S7 | A shuffled name list; `trainer/C2_W01_D05_rehearsal_key_TRAINER.md` for the answer to each push, read after Kavya's review | About a dozen notes read to the room, one push each, a minute of Kavya's review | **Cut first**, whole or in part |
| Timed design cases, 40 | S8 to S11 | `exercises/unguided/C2_W01_D05_timed_cases_STUDENT.md`; the model answers, sizing and sources in `trainer/C2_W01_D05_timed_cases_key_TRAINER.md` | Three cases at Kalpa, 13 minutes each: read 1, think 3, pairs 4, two call-outs 3, model 2. Each answer names the option, its size and the fact that would switch it | Case 3 only |
| Kahoot and close, 20 | S12 to S15 | `kahoot/C2_W01_D05_quiz_STUDENT.md` | Eight items, three of them design items; Saturday's format, never an item; the five crux lines; tonight's three tasks | S14 to one line |

---

## The traps, each with its exact wrong number

Every number is printed by a notebook: the chapter notebooks for the debrief's traps, and
`trainer/C2_W01_D05_lab_reference_TRAINER.ipynb` for the full lab key.

**The debrief's three chapters.**

| Chapter | The options, and the best-fit call | The trap: the wrong number | The check that catches it | The second route |
|---|---|---|---|---|
| 1. The reconciliation, skipped | A trust the pass (0 min, +11.8%), B count check (2 min, -14.6%), C counts and rupees with a bridge (15 min, -28.5%), D order-level match (about 120 min, -28.5%). C; D when there is no control total or the bridge will not close | Q2 up 11.8 percent (Q1 Rs 50,63,000, Q2 Rs 56,60,890) | Each quarter's orders and rupees against the control totals | Walk back from Finance's totals: add the rows removed, subtract the value read back, land on the hurried sum |
| 2. The pass that looks clean | A zero in a try (1 min, no log line), B drop with a reason (2 min), C read, convert, keep and flag (3 min), D hold and ask the owner (a wait). C; D when the text cannot be read without a guess, B when the row is not an order | Q1 Rs 50,63,000 on 98 orders, 0 rejects, counts reconciled; Q2 down 14.6 percent | Rupees against the control total: Q1 Rs 9,85,000 short | Value accounting: present 197 = convertible 196 + logged 1, and the logged value equals the gap |
| 3. The headline on too few orders | A biggest rupee move (Business, 10 orders), B the total unsplit, C count before rate (Retail-Core basket, 88 orders, p = 0.0195), D test all four (about 19 percent false-alarm chance). C; the corporate move leads only when the question is about accounts, said as counts | Business revenue -29.2 percent as the headline trend | Count before rate: 6 orders then 4; coin flips split ten orders at least that unevenly 75.4 percent of the time | Customer by customer: 21 of Retail-Core's 30 customers saw their own basket fall |

**The lab's traps, as the reference run prints them.**

| Trap | The wrong number | The right number | The check that catches it |
|---|---|---|---|
| The reconciliation skipped, the one most rooms fall into | Q2 up 11.8 percent (Q1 Rs 50,63,000, Q2 Rs 56,60,890) | Q2 down 28.5 percent (Rs 60,48,000 to Rs 43,25,480) | Input equals clean plus rejected; rupees against the control totals |
| The pass that looks clean | Q1 Rs 50,63,000, 0 rejects, 98 orders that reconcile | Rs 60,48,000 | Rupees per quarter against the control total |
| The wrong branch | Retail-Core orders per customer +20.5 percent, revenue flat | Frequency flat, revenue per order -17.1 percent | Distinct ids per segment, reconcile before the tree |
| The headline on ten orders | Corporate revenue -29.2 percent as the first line | 6 orders then 4, in the caveat | Count before rate |
| The wrong unit | Orders shuffled, p = 0.0755 | Customers shuffled, p = 0.0195 | The label's unit is the customer |
| The typical order | Mean Rs 52,057 on the rows as read (Rs 52,657 clean) | Median Rs 2,110 as read (Rs 2,120 clean) | Sort and read the top ten |
| The empty segment | Retail-Plus Q2 34 orders, Rs 93,670, -1.6 percent, plus a blank group | 35 orders, Rs 96,600, +1.5 percent | Segments add back to the total |

The only runtime error the file forces is `ValueError: invalid literal for int() with base 10:
'9,85,000'`. It gets two minutes and its last line, from the learner alone.

**When the chapter notebooks open.** They run on the lab export and print its totals, gaps and tree,
so they are released with the debrief deck, after the lab clock stops, never before. No cell prints an
order id or a raw value; the your-turn cells leave that to the learner.

## What is planted, and what to do if nobody finds it

The list with order ids is in the lab key. In short: ten rows of a batch posted twice, all
in Q2 (nine Retail-Core orders from September, one corporate order of Rs 13,20,000 dated 7 August); one corporate Q1 amount stored as the
text "9,85,000"; one Q2 Retail-Plus order with an empty segment; Business on six orders then four.
During the lab, nothing is done if nobody finds a plant: the lab measures what each learner does
alone, and the debrief is where each is found. If a learner asks whether the file is rigged, answer
"what would you check?"

## Checkpoints

After chapter 1, one learner, thirty seconds: "What two things must reconcile, and against what?"
After chapter 2: "Your pass reports zero rejects. What do you check?" After chapter 3: "Your rate rests
on how many orders?" After round one: "When did your caveat come,
before the push or after it?"

## The day's numbers

| Measure | Value |
|---|---|
| Rows, distinct orders, rejected | 207, 197, 10 |
| Q1 and Q2 clean, equal to control | Rs 60,48,000 (98 orders) and Rs 43,25,480 (99 orders) |
| Change, Q1 to Q2 | -28.5 percent; Rs 17,10,000 of the Rs 17,22,520 fall is Business, on 6 orders then 4 |
| Retail-Core | 30 customers both quarters, 1.47 orders each, revenue per order Rs 2,050 to Rs 1,700, -17.1 percent |
| Retail-Plus | 20 customers, 1.70 to 1.75 orders each, Rs 2,800 to Rs 2,760 per order |
| Shuffle | Gap -15.6 points; only 39 of 2,000 customer-level shuffles as large; p = 0.0195; other seeds 0.0145 to 0.0270 |
| Typical order | Median Rs 2,110, mean Rs 52,057, rows as read |

---

## The interview questions of the day, answered in one breath

| Tag | Question | The answer in one breath |
|---|---|---|
| [S] | Walk me through how you clean and check a dataset you have never seen. | Profile every field, clean with a written reason per decision, reconcile counts and rupees to a source total, and only then analyse. |
| [S] | Tell me about an analysis you did: what did you find, and how sure are you? | Claim with its number and denominator, the evidence and how it was checked, the caveat that would change it, and the action. |
| [F] | You have two hours and a raw export; what do you do first, and what do you skip? | Profile first, never skip the reconciliation, and skip anything that does not change today's answer. |
| [D] | A stakeholder attacks your caveat in front of the room; how do you hold it without overclaiming? | Restate with the denominator, bound what the data says, and offer the test that would settle it, with its size and time. |
| Design | Which check, which lead, which test: sized how, and what would make you switch? | Name the options, size each in minutes and in the error it leaves on this file, choose the cheapest that lands on the reference, and name the fact that moves you to the next. |

The full answers are in the study notes; the three timed cases carry case-style follow-ups with model
answers.

## The three design cases, in one breath each

| Case | The real company it is like | The best fit, sized | What would switch it |
|---|---|---|---|
| 1. Meera's first read in two hours | DMart, whose provisional quarter goes out days before the board signs the results | C: profile, clean, reconcile, decompose, about 90 of 120 minutes, marked provisional, no test | No control total: say so in the first line; a segment gap Meera will act on: B with the test |
| 2. Zero rejects and a Rs 20 lakh gap | TSB, whose 2018 migration left 1.9 million customers unable to see their accounts | Ids against rows, then the value accounting, a cell each; then the rupee bridge by month, about 30 minutes | A month the bridge cannot close: match that month order by order |
| 3. 42 percent on twelve visits | Bing, whose 12 percent revenue lift was checked before anyone believed it | A half-and-half split until each checkout has about 300 visits, about half a week | A checkout that could lose money: one visit in ten for a fortnight, still about a 91 percent chance of seeing a real difference; a dozen visits a week in all: decide on cost and reversibility |

The full model answers, the arithmetic and the sources are in `trainer/C2_W01_D05_timed_cases_key_TRAINER.md`.

---

## The practice lab: the TA note

The set is `exercises/practice/C2_W01_D05_practice_STUDENT.md` on the practice export, with the
solution in `exercises/solutions/C2_W01_D05_practice_solution_STUDENT.md` and every number in the
reference notebook's last section. Each learner starts at the problem that holds the step the
observation sheet marked.

| Problem | Where learners stall | The one hint to give |
|---|---|---|
| 1, the profile and decisions | The currency-prefixed amount, "Rs 2,260": they try int() and drop the row | "Can you read that value without guessing?" |
| 2, the reconciliation | They stop at the count check, 39 and 36, and call it done | "Your rows are all there. Are your rupees?" |
| 3, the tree and the test | They read Retail-Plus frequency on the uncleaned rows and report -40 percent | "How many distinct orders does Retail-Plus hold in Q1?" |
| 4, the note | They lead with the flat total, or with Student's 50 percent on five orders | "What is the smallest number of orders any rate in your claim rests on?" |

Items 4, 6, 7, 10, 11, 12, 15 and 16 are design items, eight of seventeen; item 16 is the ordering item
and item 17, on problem 4's last page, is the find-the-defect item on a zeroing try. The practice lead's test sits at p = 0.047 with the order that has no customer_id kept as its
own customer and 0.011 with the order left out of the file entirely; item 3's handling (kept as an
order, customer uncounted) moves the gap to about -34 points and leaves the shuffle no customer to
move (reference notebook, practice section). A learner should say which handling they chose, and the
note calls the first borderline; at a p this close to 0.05 the analyst runs 20,000 shuffles before
calling it, since the p-value's own wobble at 2,000 is about 0.005. A learner who stalled at a step answers that problem's design item aloud to the TA before
the rerun, so the choice of approach is said before the code is typed.

The practice numbers: 79 rows, 75 distinct orders, 4 repeated Q1 Retail-Plus rows, one amount "Rs
2,260", one Q2 order with no customer_id, Q1 Rs 23,21,000 and Q2 Rs 23,39,340 on the control totals,
Retail-Plus orders per member 2.00 to 1.50 (-25.0 percent; -40.0 on the uncleaned rows).

---

## Which file for which moment

| Moment | File |
|---|---|
| Terms and the clock | `slides/C2_W01_D05_lab_STUDENT.pptx` |
| The lab | `exercises/unguided/C2_W01_D05_lab_brief_STUDENT.md`, `notebooks/C2_W01_D05_lab_STUDENT.ipynb`, `data/C2_W01_D05_lab_*` |
| Observing | `trainer/C2_W01_D05_observation_sheet_TRAINER.md`, one per TA |
| The debrief | `slides/C2_W01_D05_debrief_STUDENT.pptx`, with the three chapter notebooks in `notebooks/` on the projector, `01_reconciliation_skipped`, `02_pass_that_looks_clean` and `03_headline_on_few_orders`, released as the lab clock stops |
| Every number | `trainer/C2_W01_D05_lab_key_TRAINER.md` |
| The rehearsal and the cases | `slides/C2_W01_D05_rehearsal_STUDENT.pptx`, `exercises/guided/`, `exercises/unguided/C2_W01_D05_timed_cases_STUDENT.md`, `trainer/C2_W01_D05_rehearsal_key_TRAINER.md`, `trainer/C2_W01_D05_timed_cases_key_TRAINER.md` |
| Close | `kahoot/C2_W01_D05_quiz_STUDENT.md` |
| Tonight | `study-notes/`, `preread/` for Saturday, `exercises/practice/` for the practice lab |

**If a Codespace will not start** for a learner, the lab runs in a local clone of the repository with Python 3 and the two
CSV files, and the TA records the minutes lost; the lab is never moved to a pair.
