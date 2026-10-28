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

1. **No logo or institute name in the deck.** `scripts/build_deck.py` draws the institute's logo, name and administering line on every slide. The shared builder is used by four other day sessions running in parallel, so it was left alone, and `C2_W05_D02_strip_logo_INTERNAL.py` deletes those shapes from the built pptx (64 pictures and 137 labels). Rebuilding the deck needs both commands; the orchestrating session may prefer a flag in the shared builder.
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

## Review log

- `python3 scripts/verify.py content/W05/D2` run once at the end; its output is in the session report.
