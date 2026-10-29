# W05 D2 sources, measurements and decisions

INTERNAL. Built on 28 October 2026 for Tuesday 3 November 2026 from `docs/detailing/W05_briefs/W05_D2_brief.md`, the approved week plan (`docs/detailing/W05_ml_core_plan.md`), the row in `docs/curriculum/W5_ML_core_ME1.md` and the research in `docs/detailing/W05_research/`. Environment: Python 3.13, pandas 3.0.5, scikit-learn 1.9.1, matplotlib 3.11.2.

## Datasets

| Dataset | Where used | URL | Licence | Checked |
|---|---|---|---|---|
| UCI Bank Marketing, `bank-additional-full.csv` (Moro, Rita and Cortez, Decision Support Systems, 2014, doi:10.1016/j.dss.2014.03.001) | case01 to case03, guided, figures, explorable (nudge mode) | https://archive.ics.uci.edu/dataset/222/bank+marketing (download https://archive.ics.uci.edu/static/public/222/bank+marketing.zip), verified 28 October 2026 | CC BY 4.0 | 28 October 2026 |
| German Credit (Statlog), OpenML `credit-g` id 31 (creator Hans Hofmann) | practice lab, practice set problems 6 and 7, explorable (loan mode) | https://www.openml.org/api/v1/json/data/31 and https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data, both verified 28 October 2026 | OpenML "Public"; UCI CC BY 4.0 | 28 October 2026 |

Every notebook downloads its file in code into `~/.cache/c2_datasets` and writes nothing into the repository.

## Numbers measured on this machine (validation slice, the week's seeded split)

| Quantity | Measured | Week pipeline note |
|---|---|---|
| Rows; train, validation, test | 41,188; 24,712, 8,238, 8,238 | same |
| Base rate (validation) | 928 of 8,238, 11.26 percent | same |
| Call nobody | accuracy 0.8874, TP 0 | same |
| Customer-table logistic at 0.5 | TP 174, FP 94, FN 754, TN 7,216; accuracy 0.8971; precision 0.649; recall 0.188; F1 0.291; AUC 0.7613 | same |
| Cost threshold 40 / 1,240 = 0.032 | calls 7,438; TP 913, FP 6,525, FN 15; bill Rs 279,000 | same counts |
| Call everyone; call nobody | bills Rs 292,400 and Rs 1,113,600 | not in the note |
| Saving of the cost line over calling everyone | Rs 13,400: 4.6 percent of that bill, 1.2 percent of the Rs 1,113,600 buyer margin at stake | the note says "within one percent of calling everyone"; that holds against the margin at stake, and the pack says both |
| F1-maximising threshold | 0.154: calls 1,226, finds 454, bill Rs 599,680 | not in the note |
| Saving over the best free rule by ratio | 30:1 4.6%; 20:1 8.2%; 15:1 14.0%; 10:1 28.1%; 8:1 38.2%; 5:1 31.5%; 3:1 22.1%; 2:1 16.3% | not in the note |
| Precision at k | top 500: 0.540; top 1,000: 0.404 (404 buyers); top 2,000: 0.272 (544); random 1,000: about 112 (mean of 500 seeded draws) | 0.540 and 0.404, same |
| Budget line | the 1,000th score is 0.182; recall there 0.435 | not in the note |
| Budget bills | top 1,000 Rs 652,640; random 1,000 Rs 1,014,264 | not in the note |
| German Credit, 70/30 stratified split, seed 42, 300 test applicants, logistic on all 20 columns | AUC 0.783; at P(good) 0.833: approves 128, 13 bad approved, 95 good rejected, cost 160 (5:1 units); 0.5: cost 266; approve all 450; reject all 210; cheapest grid point 0.82 at 152 | not in the note |
| German Credit at Rohan's 20:1 (Rs 60,000 and Rs 3,000) | at 0.952: approves 43, 3 bad; Rs 690,000 against Rs 630,000 for rejecting everyone; cheapest grid point 0.98 at Rs 585,000 | not in the note |

## References, one written and one video per new topic

| Topic | Written | Video |
|---|---|---|
| Confusion matrix | scikit-learn user guide 3.4, metrics and scoring, https://scikit-learn.org/stable/modules/model_evaluation.html (verified 28 October 2026) | StatQuest, "Machine Learning Fundamentals: The Confusion Matrix", https://www.youtube.com/watch?v=Kdsp6soqA7o (verified 28 October 2026) |
| Precision, recall, F1 | Google Machine Learning Crash Course, "Classification: Accuracy, recall, precision, and related metrics", https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall (verified 28 October 2026) | Data Science Dojo, "Introduction to Precision, Recall and F1", https://www.youtube.com/watch?v=jJ7ff7Gcq34 (verified 28 October 2026) |
| Class imbalance against accuracy | the same Google MLCC page, its imbalanced-data passage (verified 28 October 2026) | StatQuest, "Machine Learning Fundamentals: Sensitivity and Specificity", https://www.youtube.com/watch?v=vP06aMoz4v8 (verified 28 October 2026) |
| Metric from cost, threshold | Stripe, Radar technical guide, https://stripe.com/guides/primer-on-machine-learning-for-fraud-protection (verified 28 October 2026); scikit-learn 3.3, "Tuning the decision threshold for class prediction", https://scikit-learn.org/stable/modules/classification_threshold.html (verified 28 October 2026) | Google MLCC, "Thresholds and the confusion matrix" (interactive), https://developers.google.com/machine-learning/crash-course/classification/thresholding (verified 28 October 2026) |
| Threshold explorable model | MLU-Explain, "Precision and Recall", https://mlu-explain.github.io/precision-recall/ (verified 28 October 2026), CC BY-SA 4.0, linked only | |
| Beyond today, trainer only | | StatQuest, "ROC and AUC, Clearly Explained!", https://www.youtube.com/watch?v=4jRBRDbJemM (verified 28 October 2026), for the faculty block |

The row's own links (scikit-learn user guide index, StatQuest video index) answered 200 on 28 October 2026; the pack prints the more specific pages above. Interview Query was not re-fetched.

## Real-company facts, each re-read on 28 October 2026

| Company | Fact used | Where | URL |
|---|---|---|---|
| Stripe | 26 dollar sale, 8 percent margin, a missed fraud costs 38.92 dollars, "18.71 legitimate sales", break-even precision 5.07 percent; "The model controls the shape of the precision-recall curve"; 33 percent of consumers would not shop again after a false decline | ch04, slide 47, notes, cheat sheet, interview bank | https://stripe.com/guides/primer-on-machine-learning-for-fraud-protection (verified 28 October 2026) |
| Razorpay (Vulcan, post of 10 September 2026) | compares detection "at the same alert volume"; more fraud from more reviews "is a threshold change, not proof that the model improved"; labels arrive "weeks later" | case03 trap, slide 52, notes, practice set | https://razorpay.com/blog/vulcan-how-razorpay-built-a-foundation-model-for-payment-decisions (verified 28 October 2026) |
| PhonePe (post of 28 July 2022) | fraud systems "at very high precision"; fraud rate down 40 percent on consumer-to-consumer transactions; daily complaints down 38 percent | notes, practice set, interview bank | https://tech.phonepe.com/building-phonepes-real-time-transaction-model-to-prevent-frauds-a-journey/ (verified 28 October 2026) |
| Flipkart with CMU (BIRDNEST, arXiv 1511.06030) | top 250 flagged users hand-labelled, 211 fraud, over 84 percent; all of the first 50; 1.1 million users, 3.3 million ratings | slide 53, notes, practice set | https://arxiv.org/abs/1511.06030 (abstract and PDF read) (verified 28 October 2026) |

Kalpa's people and prices come from the row and `docs/07_Client_Zero.md`: Anand Iyer (Finance controller), Kavya Nair (senior analyst), Meera Raghavan (CEO), Rohan Desai (head of risk, Kalpa Financial Services); Rs 40, Rs 1,200, Rs 60,000, Rs 3,000.

## Images

Every PNG in `1_in_class_training_content/slides/img/` is our own render from `C2_W05_D02_make_figures_INTERNAL.py` (matplotlib) on the datasets above or on the invented tables typed in the concept notebooks. Icons on the card slides are Lucide line icons (ISC licence) that `scripts/build_deck.py` rasterises. No logo, photograph or third-party picture is used.

## Decisions taken in the build

1. **No logo or institute name in the deck.** `scripts/build_deck.py` draws the institute's logo, name and administering line on every slide. The shared builder is used by four other day sessions running in parallel, so it was left alone, and `C2_W05_D02_strip_logo_INTERNAL.py` deletes those shapes from the built pptx (64 pictures and 137 labels). Rebuilding the deck needs both commands; the orchestrating session may prefer a flag in the shared builder. The orchestrating session then moved this into the shared builder (pull request 266): from Week 5 on `scripts/build_deck.py` draws no logo or institute name, the stripping script was removed and the deck rebuilt.
2. **mermaid-cli in this container** needs `PUPPETEER_EXECUTABLE_PATH=/opt/pw-browsers/chromium-1243/chrome-linux64/chrome`, since `build_cheatsheet._chromium()` looks for `chrome-linux/` and this image ships `chrome-linux64/`.
3. **Concept chapters on invented tables, cases on the bank's file.** The contract allows a tiny teaching table typed in a cell and labelled invented; every invented table is labelled so in its notebook. No dataset is generated.
4. **Kalpa's prices on the bank's calls.** The bank's own costs are unknown; the pack says once that Kalpa's Rs 40 and Rs 1,200 are applied to the bank's calls.
5. **The plan's numbers replaced by measured ones.** The plan's precision 0.69 and recall 0.22 come from the research note's single 80/20 split; the week pipeline's split (and every notebook) gives 0.649 and 0.188, which the brief also quotes. The plan's budget of 5,000 nudges for the whole base becomes the brief's 1,000 calls in the validation slice. The row's 0.12 and 0.85 (Kalpa v6 data, never generated) are not used; the trainer guide says what to answer if a learner quotes them.
6. **Both lines on the same quantity** (correction 4): nudge when P(buy) is above 0.032; lend when P(repay) is above 0.952 (Kalpa's 20:1) or 0.833 (German Credit's documented 5:1). P(default) below 0.048 appears only as the second phrasing in ch06.
7. **No `class_weight="balanced"`** in any notebook, explorable or threshold calculation; the trainer guide carries one note for a learner who asks (mean prediction 0.417 against 0.114 measured, so the formula calls 8,237 of 8,238).
8. **Order of the afternoon.** The contract orders concept chapters before case chapters in the deck, and the brief puts the 15-minute financial services story just before chapter 6, so the afternoon opens on the story, then chapter 6, then the three case chapters. Chapter 6's hand count works on invented applicants; German Credit stays out of the class notebooks.
9. **The explorable's loan mode uses German Credit's 300 held-out scores**, embedded as score bins. The brief keeps German Credit's work in the lab and the take-home; the explorable needs a lending score table for its switch, invented data is ruled out, and the room only flips the switch in class. The nudge mode uses the bank's 8,238 validation scores in bins of 0.01.
10. **Time.** Drill 1 runs 12 minutes against the row's 15; drill 2 (three cost stories) is folded into chapter 4's slide 24 and runs in full only in the faculty-block fallback; the Kahoot and close run 12 minutes against the row's 20, since the afternoon also holds the 15-minute domain story. F1's arithmetic is the first cut, as the row says.
11. **The F1 threshold is shown as a rival option** in case 2 (0.154), so the room sees why a "balanced" metric lands far from the cost line.

12. **Picture names.** The verify gate wants every file, PNGs included, to carry the day stem and an audience tag, so the deck's pictures are named `C2_W05_D02_<name>_STUDENT.png` and the figure script writes those names.
13. **The explorable on the deck.** Slide S24 shows our own screenshot of the explorable's opening state (0.5, 174 of 928 found), saved at 144 dpi so the deck builder measures its labels truthfully.
14. **The random 1,000.** Every file quotes about 112 buyers for a random 1,000 (the mean of 500 seeded draws; the base rate implies 112.6).
15. **The explorable's step.** Its line moves in steps of 0.001, so 0.032 calls 7,452 there against 7,438 at exactly 1 in 31; the page says so beside the slider.
16. **The row's RECAP task** sits in the practice set as a one-line item after A10, with a model line in Part C; the BUILD task is problem A3; the READ task is the pre-read on the practice set's last page.

## Review log

- `python3 scripts/verify.py content/W05/D2`: first run failed on 18 picture names without the day stem and audience tag; fixed by renaming. Second run: `RESULT: PASS (0 failures)`, with 12 notebooks and 59 checks passing, the explorable swept with 0 inert controls and 0 console errors, the deck markdown and the built pptx both passing.
- `llm-tic-scrubber/scripts/tic_scan.py` on the README, the deck, the practice set, the notes, the cheat sheet, the interview bank and the trainer guide: one hit (options run together in one line), fixed; then clean.

## The explorer, rebuilt on 29 October 2026

Rebuilt in place as the day companion of decision `w5-explorer-companion`, on branch `w05-d2-explorer`, with the Week 5 kit (`scripts/companion/w5kit.js` and `w5kit.css`, inlined by `scripts/build_companion.py`) and the briefs `docs/detailing/W05_briefs/explorers/common.md` and `D2.md`. Twelve routes: `#story`, `#map`, `#p1` to `#p6`, `#case`, `#field`, `#interview`, `#check`.

### Data

| Number on the page | Where it comes from |
|---|---|
| The 8,238 validation scores and outcomes | `C2_W05_D02_explorer_data_INTERNAL.py`, which reruns the week's pipeline (the thirteen customer-table columns, seed 42, the logistic model) and writes `C2_W05_D02_explorer_data_INTERNAL.json`, 60 KB |
| 174, 94, 754, 7,216 at 0.5; 0.8971 and 0.8874; 7,438 calls and Rs 279,000 at 1 in 31; Rs 292,400 and Rs 1,113,600; F1's 0.154, 1,226 calls and Rs 599,680; the eight savings by ratio; 270, 404 and 544 in the top 500, 1,000 and 2,000; 112 at random; 123 in the first 1,000 rows; the 1,000th score 0.182; Rs 652,640 | the same script, which stops with an error unless each equals what case01, case02 and case03 print; all 23 checks passed on this machine |
| The cheapest grid line 0.033 at Rs 279,320, and accuracy's peak at 0.57 (89.85 percent, a bill of Rs 9.32 lakh) | the same script; 0.033 and Rs 279,320 also print in case02 |
| The twenty customers of `#p1` and `#p2`, the hundred of `#p3`, the twenty scores of `#p5` and the twenty applicants of `#p6` | typed in the page exactly as notebooks ch01, ch02, ch03, ch05 and ch06 type them |
| Rohan's Rs 100 (16, 8, 1, 4, 2, 3) | the dossier's illustrative table, section 3 |
| Stripe, Flipkart with CMU, PhonePe, Razorpay | `docs/detailing/W05_research/W05_cases.md`, each verified 28 October 2026, with the link and date on the page |

### Decisions

1. **Scores travel as integers out of a million.** At thousandths, 0.032 calls 7,452 against 7,438 at exactly 1 in 31, which the old page had to explain beside its slider; at millionths every notebook count reproduces and the price button sets the line to exactly 40 / 1,240.
2. **German Credit leaves the explorer.** Decision 9 above gave the old page a lending switch on German Credit's 300 held-out scores. The brief draws `#p6` on one axis with twenty applicants, so `#p6` uses chapter 6's invented applicants, as the notebook does, and German Credit stays in the lab and the practice set.
3. **`#p1` and `#p5` carry both kinds of numbers.** The brief asks for real scores on both pages, and the page rule asks for a mechanism on tiny invented numbers, so each stage has a toggle between the notebook's invented table and the bank's 8,238; the stage's badge and title switch with it.
4. **The line scene is one function, `lineScene(api, cfg)`, for Friday.** It takes any kit stage, a list of score sets (a strip of dots up to 60, two humps above that), two prices and an optional budget, and draws the draggable line, the bill traced at every line tried, the full curve after the reveal, the free rules and the readout. Its interface is documented at the top of the function in the page.
5. **The story reveals 174.** The brief puts the reveal in the story; 174 is already on slide 20's drill and in the deck's notes for the explorable, so the case page still has the do-nothing accuracy to reveal.
6. **The map adds Week 4's expected value.** The brief names Monday's baseline and probability as earlier ideas; the trainer guide's "taught before" also lists Week 4's expected value in rupees, which `#p4` rests on.
7. **Rohan's business sits on `#p6` and in the six seats.** The dossier's illustrative Rs 100 opens `#p6`, lighting the two lines his two prices land on, and the seats on `#field` are framed on his line at 0.952. The dossier's company facts (Tata Capital, Bajaj Finance) stay off the page, since `W05_cases.md` does not carry them.
8. **Invented arithmetic in two real scenes is labelled.** PhonePe publishes no block volume or precision, so the hundred blocks and the 10,000 a day are invented and the stage says so; Razorpay publishes the rule and no curves, so its two models are invented. Stripe's 8 percent case is Stripe's; other margins follow its arithmetic, and the page says which is which.
9. **Answers stay hidden until the reveal.** Every readout, legend or chart that states a prediction's answer shows a question mark, hollow marks or no curve until the learner commits or reveals; the bill curve on `#p5` and `#case` chapter 8 is drawn only as the trace of lines tried until then.
10. **Option lengths are balanced** so no key is the longest option, as the distractor audit asks of exercises, though it does not run on pages.
11. **Cut from the old page:** the typed guess box (the kit's prediction card replaces it), the lending switch on German Credit (decision 2), and the square-root bar heights, replaced by honest shares of each group.
12. **The deck pictured the old page.** Slide 30 (S24) showed a screenshot of the earlier page; the orchestrating session replaced it with page 5 of this explorer and rewrote its notes for the new clicks.

### Proof

- `python3 scripts/build_companion.py` inlines the kit and the data; `--check` passes.
- `python3 scripts/html_sweep.py` walks all twelve routes: 328 controls clicked, none inert, no console errors.
- `python3 scripts/explorer_shots.py` at 1366 and 390 wide, with `--end`, plus a session script that opened every tab and every alternate mode; every picture was looked at, and the overlaps, clipped labels and small type it found were fixed.
- This container's Chromium sits at `/opt/pw-browsers/chromium-1243/chrome-linux64/chrome`, which `find_chromium()` in `scripts/html_sweep.py` does not search, so the sweep and the screenshots ran with `PLAYWRIGHT_BROWSERS_PATH` pointing at a scratch folder that links the binary under `chrome-linux/`. Without that, the sweep falls back to a static scan and still prints PASS.
