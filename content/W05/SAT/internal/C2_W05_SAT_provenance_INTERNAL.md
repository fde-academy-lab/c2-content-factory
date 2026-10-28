# Provenance: Week 5, Saturday

INTERNAL. One session built this pack on 28 October 2026 on the branch `w05-sat`, cut from
`origin/main`, in one long turn with nobody answering questions. Every call the rules left open is in
`C2_W05_SAT_sources_INTERNAL.md` under "Which decisions did the build make, and why?"; this file
records what the pack rests on, what the paper holds, where each bank item went, and the numbers
the session re-ran.

## What decided this pack

| Source | What it settled |
|---|---|
| The orchestrator's brief for the W05 SAT session, 28 October 2026 | The deliverables, the 60-minute paper, the interview grade, the writing rules, no marks or weights for ME1, and the finish line |
| `docs/curriculum/W5_ML_core_ME1.md`, the Saturday row | The agenda (the ME1 window up to half the block, the 60-minute paper, marking 10, discussion 35, the Build 2 preview 15), ME1's four theme areas, the nine interview anchors and their tags, the paper's format list, and the row's two links |
| `docs/curriculum/source.xlsx`, the Saturday papers tab, paper W5 (29 items, 59.5 minutes, slot 60) | Every bank stem and key, unchanged, and what the paper must test |
| `data/programme/facts.yaml` | `saturday_papers` (no W05 entry in `paper_minutes`, so 60), `campus_day.saturday_minutes` 300, `evaluation.exam_day_and_slot` (open: no day or slot stated), decisions `saturday-interview-grade`, `saturday-real-cases`, `plants-once-found` and `w5-artifact-set`, and module M2 for Week 5 |
| `docs/detailing/W05_ml_core_plan.md` | The five day stories and chapter names the parts and the guide point back to, the six seats, the week's picture, the sealed envelope, and section 6: the row's planted Kalpa figures belonged to a dataset never generated |
| `docs/detailing/W05_research/W05_week_pipeline.md` | The split, the column plan and every model and threshold number the paper prints, re-run in this session and matched exactly; the council's notes on the calendar, the split by date, calibration and the near-tie |
| `docs/detailing/W05_research/W05_cases.md` | The verified cases; Instacart and Booking.com were refetched for the paper, and its unverified list is carried in the sources file |
| `docs/07_Client_Zero.md` v2.2 | Kalpa's people, Rohan Desai's twenty-to-one cost, Build 2's five sub-problem seeds and its Tuesday start |
| `content/W04/SAT` | The source file's form, the proofs' form, the guide's form and the folding practice |

## The paper

`scripts/build_saturday_paper.py W05 --docx` renders 24 timed items in five parts at 57 of 60 minutes
by the blueprint's pace, 3 easy, 14 medium and 7 hard (29 percent hard), with an untimed stretch page
of three. Three bank items print, the blanks of banks 1 to 3, each from a word bank; twenty-six fold
into deeper items; none moves to the stretch page; twenty-one additions come from the week's source
file. A blind guesser averages 4.7 of 24, and the key's guessing line sits at 9. The levels are the
ones the fix pass left after the blind sitting, by exercise-builder's bar; the sources file says why
7 hard items is the honest count, short of the decision's about 60 percent.

| Part | Items | Minutes | Easy | Medium | Hard |
|---|---|---|---|---|---|
| 1. Should the bank build a model, and what must it beat? | Q1 to Q5 | 10.5 | 1 | 3 | 1 |
| 2. Which number tells the truth, and where does the line go? | Q6 to Q11 | 15.5 | 1 | 4 | 1 |
| 3. What was the model allowed to know? | Q12 to Q16 | 11 | 1 | 3 | 1 |
| 4. Is the model learning, or memorising? | Q17 to Q20 | 10 | 0 | 2 | 2 |
| 5. Would the committee sign, and what moves to lending? | Q21 to Q24 | 10 | 0 | 2 | 2 |
| Total | 24 | 57 | 3 | 14 | 7 |

The formats: three word-bank blanks, each last in its part, eleven one-correct items, four
statements judged with their reasons (Q2 and Q20 keyed True, Q6 and Q14 False), four more-than-one
items and two worked items. Every part opens on the bank campaign with an exhibit that pairs a
mermaid picture with a table; three items carry an exhibit of their own (2B, 4B and 5B). The
distractor audit passes with key positions a 6, b 8, c 5 and d 5 across the 19 lettered items,
counting the letters of the four more-than-one keys (Q4 a, d; Q13 b, c; Q18 a, b, d; Q22 b, c),
which share no letter across all four. Among the 15 single keys, 4 tie for the longest option, 4 are
the shortest and 7 sit between.

## The fate of every bank item

| Bank | Type, the tracker's level | Fate | Where it is tested | Why |
|---|---|---|---|---|
| 1 | Fill in the blank, Easy | Printed | Q5 | Answered from a word bank, with the tracker's stem and key, last in its part |
| 2 | Fill in the blank, Easy | Printed | Q11 | Answered from a word bank, with the tracker's stem and key, last in its part |
| 3 | Fill in the blank, Easy | Printed | Q16 | Answered from a word bank, with the tracker's stem and key, last in its part |
| 4 | Fill in the blank, Easy | Folded | Q17, tree-read | The blind sitting found the bank's 100 and 61 percent read beside Exhibit 4A's 0.996 and 0.619, two metrics, and found the blank cued by the part's title and by the options above it, so the item that reads training at 0.996 against validation at 0.837 as memorising tests bank 4's word on the room's own tree. |
| 5 | Fill in the blank, Medium | Folded | Q19, cv-why | The blind sitting found the blank answered by the folds item's own options, which say what one split could have read, so the folds item, whose key is the luck of one split sized at 0.77 to 0.80, tests bank 5's word. |
| 6 | True or false, Easy | Folded | Q6, acc-trap | The printed statement is bank 6's trap on the week's own rows, where calling nobody already scores 0.887 on an 89 to 11 outcome, and option d keys the reason accuracy says little there. |
| 7 | True or false, Medium | Folded | Q14, importance | The statement reads the top of an importance chart as a cause, and the key refuses it because the yes drives the call's length as much as the reverse, which is bank 7's false statement judged with its reason. |
| 8 | True or false, Easy | Folded | Q18, brakes | Option b is a stronger penalty on the weights, which loosens the fit to the training rows, and option c, fitting the training rows until they score 1.0, is bank 8's false statement offered as a brake. |
| 9 | True or false, Hard | Folded | Q20, near-tie | The key is bank 9's statement on the week's three families, a gap of 0.011 AUC inside the 0.03 one split moves by, so the simpler, explainable model is the recommendation. |
| 10 | One correct option, Easy | Folded | Q4, is-it-ml | The item sorts four of the bank's asks into the two that need a prediction and the two a query answers, which is bank 10's question with two keys where the bank has one. |
| 11 | One correct option, Medium | Folded | Q3, logit-071 | The item asks what a logistic score of 0.71 says about one client, with bank 11's three misreadings as the distractors and the calibration condition added to the key. |
| 12 | One correct option, Medium | Folded | Q8, cost-line | The working puts the line at 1 in 31, about 0.032, far below 0.5, and the answer names the direction and that recall leads, which is bank 12's key derived where the bank only asks for it. |
| 13 | One correct option, Hard | Folded | Q24, lend-flip | The item is bank 13 on Rohan Desai's own costs, set beside the nudge's cost line, and its key draws the approval line at about 0.05 chance of default, which is the bar moving up. |
| 14 | One correct option, Medium | Folded | Q12, duration-call | The item is bank 14's leak on the week's real column, duration, which the dataset's own notes say is known only after the call, and its key removes it and reports the honest 0.795. |
| 15 | One correct option, Hard | Folded | Q15, sign-flip | The item is bank 15's sign flip as the week measured it, euribor3m from -0.92 alone to +0.39 beside the other indicators, with the same four causes as options. |
| 16 | One correct option, Medium | Folded | Q17, tree-read | The exhibit is bank 16's curve on the room's own tree, training rising to 0.996 while validation falls to 0.837, and the key caps the depth at the validation peak, which is bank 16's prescription. |
| 17 | One correct option, Medium | Folded | Q21, stale-rule | The key is bank 17's monitoring rule made concrete on the bank's late rows, the called clients' yes rate against the mean score with a stated gap, and its distractors are bank 17's three. |
| 18 | More than one correct, Medium | Folded | Q6, acc-trap | The statement sets the model against the majority-class baseline on the same validation rows, bank 18's options a and c, and its key says why beating the baseline on accuracy alone does not earn a ship, bank 18's option b. |
| 19 | More than one correct, Medium | Folded | Q13, which-pass | The item is bank 19's prediction-time test on the bank's own columns, with the tempting legitimate column, the previous campaign's result, beside the call's duration. |
| 20 | More than one correct, Medium | Folded | Q18, brakes | The item is bank 20 on the week's two families, a depth cap, a stronger penalty and cross-validation as the brakes, with fitting the training rows harder as the false one. |
| 21 | More than one correct, Hard | Folded | Q22, caveat | The item is bank 21's four-part memo on the bank's numbers, with the weakest segment and the staleness trigger as the caveat and the validation score and the budget as the lines that belong elsewhere. |
| 22 | Scenario set, Easy | Folded | Q7, prf | The working computes precision on the week's real matrix, 174 of the 268 called, which is bank 22's arithmetic on numbers the room ran. |
| 23 | Scenario set, Easy | Folded | Q7, prf | The working computes recall on the same matrix, 174 of the 928 buyers, which is bank 23's arithmetic. |
| 24 | Scenario set, Medium | Folded | Q9, bill | The item prices the week's real matrix at bank 24's costs, Rs 40 a wasted call and Rs 1,200 a missed buyer, which is bank 24's error bill. |
| 25 | Scenario set, Hard | Folded | Q9, bill | The item compares the bill at two thresholds and asks which costs less, which is bank 25's question on the week's own thresholds, and its distractors are the three ways the bill is usually miscounted. |
| 26 | Scenario set, Medium | Folded | Q6, acc-trap | The key reads 0.897 accuracy beside 174 of 928 buyers found, which is bank 26's point that an accuracy figure says little about how many buyers were found. |
| 27 | Applied maths, Hard | Folded | Q7, prf | The item asks for precision, recall and F1 from one matrix, bank 27's three figures, on the week's real counts. |
| 28 | Applied maths, Medium | Folded | Q8, cost-line | The working states that one caught buyer pays for 30 wasted calls, which is bank 28's answer, and turns it into the threshold. |
| 29 | Applied maths, Easy | Folded | Q19, cv-why | The key states five models fitted on about four-fifths of the training rows each, which is bank 29's count on the week's 24,712 rows. |

## The numbers the session re-ran

The week's pipeline code, copied from `W05_week_pipeline.md`, was run on 28 October 2026 on the UCI
file downloaded the same day (Python 3.13, pandas 3.0.5, scikit-learn 1.9.1; the pipeline file used
pandas 3.0.6). Every number in its model and threshold tables came out the same. The extra models
below use the honest columns (the customer table and the five economic indicators), the same split
and seed 42; `C2_W05_SAT_key_proofs_INTERNAL.py --rerun` recomputes each one and passed on 28 October
2026.

| What | Setting | Result |
|---|---|---|
| Yes count | the whole file | 4,640 of 41,188 |
| Decision tree, training and validation accuracy, validation AUC | depth 3; 5; 8; no limit | 0.899, 0.899, 0.751; 0.901, 0.897, 0.783; 0.911, 0.897, 0.777; 0.996, 0.837, 0.619 |
| Five-fold cross-validation of the logistic model, AUC | the 24,712 training rows, stratified, shuffled with seed 42, scaling inside the pipeline | 0.771, 0.769, 0.797, 0.796, 0.798; mean 0.786 |
| Three families on validation, AUC | logistic regression; random forest of 300 trees with at least 5 rows a leaf; histogram gradient boosting at its defaults | 0.795; 0.799; 0.806 |
| euribor3m's standardised coefficient | alone; with the honest columns | -0.92; +0.39 |
| euribor3m's correlation with three indicators | the whole file | employment variation rate 0.97; number employed 0.95; consumer confidence 0.28 |
| poutcome success | the whole file | 1,373 rows, 65.1 percent yes |
| Mean call duration | yes; no | 553 seconds; 221 seconds |
| Split by date | earliest 70 percent of rows to train, latest 30 percent to score | 28,831 and 12,357 rows; yes rates 5.6 and 24.6 percent; mean predicted 0.152; AUC 0.657 |
| The error bill at Kalpa's costs | the cost line; calling every validation client | Rs 279,000; Rs 292,400 |

## How the pack was checked

| Check | Result on 28 October 2026 |
|---|---|
| `python3 content/W05/SAT/internal/C2_W05_SAT_key_proofs_INTERNAL.py --rerun` | 24 items proved, every exhibit number matched to the pipeline file or the re-run, and the re-run recomputed from the UCI file |
| `python3 scripts/distractor_audit.py content/W05/SAT` | PASS, positions a 6, b 8, c 5, d 5 |
| `python3 scripts/build_saturday_paper.py W05 --check` | 2 files, 0 stale |
| `python3 scripts/verify.py content/W05/SAT` | PASS; its output is in the session's report |
| The blind sitting, one fresh agent on the student paper alone | All 26 keys of the draft matched; its findings and the fix pass are in the sources file |
| The Word paper converted to PDF and read page by page | 14 pages; every exhibit renders, and Exhibit 4A's title names its two lines because mermaid's xychart draws no legend |

Skills used: exercise-builder for the objective blueprint, distractor discipline and the key's
wrong-option reasons; humanizer for the guide, the sources and this file, read in file mode so that
code, numbers and paths stay as they are.
