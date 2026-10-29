# W05 Friday sources, decisions and build log

INTERNAL. Built 28 October 2026 on branch `w05-d5` with Python 3.13, pandas 3.0.5, scikit-learn 1.9.1, matplotlib 3.11.2. Every number in the pack comes from the executed notebooks in `1_in_class_training_content/notebooks/` or from `C2_W05_D05_make_figures_INTERNAL.py`, which reruns the same code.

## Datasets

| Dataset | URL | Licence | Checked |
|---|---|---|---|
| UCI Bank Marketing, `bank-additional-full.csv` (Moro, Rita, Cortez; DOI 10.24432/C5K306) | https://archive.ics.uci.edu/dataset/222/bank+marketing (verified 28 October 2026); download https://archive.ics.uci.edu/static/public/222/bank+marketing.zip (verified 28 October 2026) | CC BY 4.0, per the page | 28 Oct 2026, page HTTP 200, file loaded: 41,188 rows |
| German Credit (Statlog), OpenML `credit-g` id 31 (Hans Hofmann) | https://www.openml.org/api/v1/json/data/31 (verified 28 October 2026); UCI page https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data (verified 28 October 2026) | OpenML "Public"; UCI CC BY 4.0 | 28 Oct 2026, 1,000 rows, 700 good, 300 bad |
| The gym, the lender and the six months of calls in chapters 1 to 5 | typed in the notebooks | invented for teaching, labelled invented | not applicable |

## Real-company facts and references

| Fact as printed | Source | Checked |
|---|---|---|
| Zillow recorded a "$304.4 million write-down of inventory associated with Zillow Offers"; the wind-down means about a 25 percent reduction of the workforce | Zillow Group 8-K, 2 November 2021: https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/z-20211102.htm (verified 28 October 2026) | text found on the page this session |
| "unable to accurately forecast future home prices at different times in both directions"; prices forecast "three to six months into the future"; unit economics swung about 1,200 basis points | Exhibit 99.3, the Q3 2021 shareholder letter: https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/exhibit993.htm (verified 28 October 2026) | text found on the page this session |
| Instacart's item-availability metric "dropped to 61% from 93%", which told engineers to retrain | Fortune, 9 June 2020: https://fortune.com/2020/06/09/instacart-coronavirus-artificial-intelligence (verified 28 October 2026) | text found on the page this session |
| Instacart adjusted thresholds on top of the model without retraining; models respond sluggishly to a shock | https://company.instacart.com/tech-innovation/how-instacarts-item-availability-evolved-over-the-pandemic (verified 28 October 2026) | HTTP 200; wording as recorded in `docs/detailing/W05_research/W05_cases.md` |
| Google's Rules of ML, Rule 37, measure training and serving skew | https://developers.google.com/machine-learning/guides/rules-of-ml (verified 28 October 2026) | "Rule #37" found on the page |
| Booking.com, offline gains did not predict business gains across 23 model pairs (KDD 2019) | DOI https://doi.org/10.1145/3292500.3330744 returned HTTP 403 to this session (checked 28 October 2026); the facts are from `W05_cases.md`, read there from a mirror PDF | cited in TRAINER material only |
| German Credit's 5 : 1 cost matrix | UCI and OpenML pages above | wording in `W05_datasets.md` |
| StatQuest video index | https://statquest.org/video_index.html (verified 28 October 2026) | HTTP 200 |
| scikit-learn, probability calibration | https://scikit-learn.org/stable/modules/calibration.html (verified 28 October 2026) | HTTP 200 |
| scikit-learn, metrics and scoring | https://scikit-learn.org/stable/modules/model_evaluation.html (verified 28 October 2026) | HTTP 200 |
| Google MLCC, thresholds and the confusion matrix | https://developers.google.com/machine-learning/crash-course/classification/thresholding (verified 28 October 2026) | HTTP 200 |
| Chip Huyen, Introduction to Machine Learning Interviews | https://huyenchip.com/ml-interviews-book/ (verified 28 October 2026) | HTTP 200 |
| IBM Telco churn (the practice set's transfer problem) | https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv (verified 28 October 2026) | HTTP 200; facts from `W05_datasets.md` |

## Images

All 13 PNGs in `1_in_class_training_content/slides/img/` and every chart in the notebooks are drawn by our own code from the datasets above or the invented tables. No image is taken from elsewhere. Mermaid diagrams are rendered by the repository's own build. No logo appears anywhere: from Week 5 on `scripts/build_deck.py` draws no logo or institute name (pull request 266), so the stripping script this build first used was removed and the deck rebuilt.

## Headline numbers (from the executed notebooks)

| Number | Value | Notebook |
|---|---|---|
| Split | train 24,712, validation 8,238, test 8,238; base rate 11.26 percent on validation | all case notebooks |
| Validation AUC | logistic 0.795, tuned tree (depth 7, leaf 20) 0.787, boosting 0.803 | case01 |
| Bill at 0.032 | logistic Rs 2,81,680, tree Rs 2,82,840, boosting Rs 2,83,200; call everyone Rs 2,92,400; logistic at 0.5 Rs 8,61,480 | case01 |
| Top 1,000 | 462, 469, 475 buyers; 113 at random | case01 |
| Boosting minus logistic | 13 buyers (Rs 16,120); paired bootstrap 95 percent band about -1 to 28 | case01 |
| Time split | early 28,831 rows at 5.6 percent; late 12,357 at 24.6 percent; mean promise 15.9 percent; late AUC 0.664 | case02 |
| Stale bill at 0.032 | Rs 4,61,640 against Rs 3,72,920 calling everyone and Rs 4,22,520 planned; 231 scored below 0.032, 79 bought | case02 |
| The rule | ceiling 10 points, two months running; fires 2009-08 | case02 |
| Segments | entrepreneur 0.655 on 26 buyers; blue-collar 0.707 on 122; telephone 0.721 against mobile 0.779 | case02 |
| German Credit | validation AUC 0.783; cost 266 at 0.5, 160 at 0.833; Rohan's 20 : 1 line at 0.952 | case03 |
| The envelope | test AUC 0.801; 482 buyers in the top 1,000 | case03 |

## Decisions taken in this session

1. **Numbers differ from the pipeline note in the third decimal.** `W05_week_pipeline.md` quotes logistic 0.803, tuned tree 0.804, boosting 0.811 for Thursday; this run on Wednesday's honest columns (with the pdays flag and days) and the 75/25 split gives 0.795, 0.787 and 0.803. The pack quotes this run, per the note's own instruction.
2. **The chosen operating point is the budget.** At Rs 40 against Rs 1,200 the cost cut (0.032) calls about nine in ten and every model's bill sits within 4 percent of calling everyone (correction 3), so the memo's claim is the top 1,000 per list of about 8,000, with the cost cut shown as the bill without a budget.
3. **The simpler model is recommended.** Boosting's 13 extra buyers sit inside a paired-bootstrap band that reaches zero, so the near-tie is a tie; the flip is stated as a fresh month whose band clears zero.
4. **The weakest segment is measured.** The row's "Student" belonged to Kalpa v6 data that was never generated. Measured AUC by job puts entrepreneur lowest on 26 buyers (unreadable band) and blue-collar lowest of the groups with 100 or more buyers; contact type adds telephone against mobile. The sample-size reason from Week 1 carries the chapter, taught on an invented student group in chapter 3.
5. **The staleness ceiling is 10 points on the bank, 5 on the gym.** Each comes from about two standard errors at the month's call count (about 100 calls on the late bank months, 200 on the gym).
6. **The week's picture opens with Friday's panel as a question mark.** The full sag is the case 2 reveal, so the opening slide shows Monday to Thursday and a question for Friday; the complete picture is shown at S35 and named at the close.
7. **Notebooks are self-contained.** Each defines a small `check()` that prints PASS or FAIL lines and uses matplotlib, with no import from `scripts/c2kit.py`, so a learner's Codespace needs nothing beyond the packages.
8. **The guided notebook's TODO cells run.** They hold `None` or empty strings and print `TO DO` until filled; the worked answer and its checks are the last section, so the notebook ships executed with PASS lines.
9. **Concept examples are one invented gym** (20 members, Rs 30 a call, Rs 900 a missed return, ratio 1 : 30 like Kalpa's), plus an invented two-wheeler lender for chapter 4 (Rs 40,000 against Rs 2,000, the same 20 : 1 as Rohan's).
10. **The practice lab is sized at about 90 minutes**, core 60; facts.yaml sets no length.
11. **The browsers in this container needed two local links.** Python playwright 1.64 looks for headless shell build 1248 and the container holds 1243, so `/opt/pw-browsers/chromium_headless_shell-1248` was linked to the 1243 build (container only, nothing in the repository) for `deck_check.py` and `html_sweep.py`.
12. **Mermaid rendering needed `PUPPETEER_EXECUTABLE_PATH=/opt/pw-browsers/chromium`** in this container; `build_cheatsheet._chromium()` found no browser. The deck and the PDFs were built with that variable set.
13. **Rupee formatting**: lakh in slides and study material; notebooks print plain thousands separators from Python.

## Review log

- `python3 scripts/verify.py content/W05/D5` passes: 41 files in the Week 5 layout, 11 notebooks executed with passing checks, the explorable swept (7 controls, 0 inert, 0 console errors), the deck markdown and the built deck checked (60 slides, 0 overflowing boxes).
- `tic_scan.py` (llm-tic-scrubber) ran clean on the README, the deck, the practice set, the three study files and the trainer guide.
- One sequencing fix after the first push: the first explorable showed the bank's real bill and months, so it opened in case chapters 6 and 7, after the room had predicted, never in chapters 2 and 3. The rebuilt explorer below keeps that order: its chapter pages run on invented numbers, and the bank's months and three bills stay on its case page.

## The explorer, rebuilt on the Week 5 kit (29 October 2026)

Built on branch `w05-d5-explorer` to `docs/detailing/W05_briefs/explorers/common.md` and `D5.md`, with `scripts/companion/w5kit.*` from main inlined by `scripts/build_companion.py`. The page is `1_in_class_training_content/demos/C2_W05_D05_error_bill_explorer_STUDENT.html`; its numbers come from `C2_W05_D05_explorer_data_INTERNAL.py`, which reruns case01 to case03 with the week's cached loader and stops on any number that differs from the notebooks, and writes `C2_W05_D05_explorer_data_INTERNAL.json`.

### Company facts on the page

| Scene | Fact as printed | Source | Checked |
|---|---|---|---|
| Zillow Offers | $304.4 million Q3 2021 write-down; $240 million to $265 million more expected in Q4; about 25 percent of the workforce; prices forecast three to six months ahead; unable to forecast "in both directions" | https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/z-20211102.htm (checked 29 October 2026, HTTP 200); the letter's wording as recorded in `W05_cases.md` | 29 Oct 2026 |
| Instacart | 93 percent before, 61 percent in March 2020, about 85 percent by June | https://fortune.com/2020/06/09/instacart-coronavirus-artificial-intelligence (checked 29 October 2026, HTTP 200) | 29 Oct 2026 |
| Instacart | thresholds adjusted without training new models; models respond sluggishly | https://company.instacart.com/tech-innovation/how-instacarts-item-availability-evolved-over-the-pandemic (checked 29 October 2026, HTTP 200) | 29 Oct 2026 |
| Google Flu Trends | the revised model missed high 100 of 108 weeks from August 2011; more than double the CDC's share at its worst | https://dash.harvard.edu/server/api/core/bitstreams/7312037d-0e0d-6bd4-e053-0100007fdf3b/content (checked 29 October 2026, HTTP 200, PDF) | 29 Oct 2026 |
| Booking.com | 23 comparisons of 46 models; Pearson -0.1 with 90 percent interval -0.45 to 0.27; Spearman -0.18 with -0.5 to 0.19 | https://blog.kevinhu.me/2021/04/25/25-Paper-Reading-Booking.com-Experiences/bernardi2019.pdf (checked 29 October 2026, HTTP 200, PDF), the mirror `W05_cases.md` read; the DOI page refuses this container | 29 Oct 2026 |

### Decisions

1. **Every route D5.md lists is built**: `#story`, `#map`, `#p1` to `#p5`, `#case` with chapters 6 to 8, `#field`, `#interview` and `#check`.
2. **The data script exports the tree's and boosting's scores** beside logistic's, so chapter 6 draws all three bills, the gains to 1,000 calls and the paired bootstrap from the notebooks' own numbers.
3. **Rupees print in Indian grouping** (Rs 2,81,680) through one page helper, because the kit's formatter groups in thousands and the deck, the guide and the notes write lakh.
4. **Page 2's bank view carries only Thursday's logistic list on Tuesday's prices**, which the room met on Tuesday; a note reconciles its Rs 2,81,680 with Tuesday's Rs 2,79,000, which came from Monday's columns. The three models and their tie wait for case chapter 6.
5. **Page 3 runs on the invented gym only**; the bank's months wait for case chapter 7, so the sag is never shown before its prediction.
6. **The monitor opens at a 50-point ceiling.** The first page's claim that 45 points never fires was false on this data (it fires in April 2010), so the trainer guide and S35's notes were rewritten for the new clicks.
7. **The weakest segment opens at the notebook's rule of 100 buyers** (blue-collar, 0.707); the slider shows entrepreneur's 0.655 on 26 buyers when the bar is lowered.
8. **Booking.com's 23 points are not drawn**: the paper prints the correlations, not the points, so the page draws the learner's line against the measured slope and its interval.
9. **Each case trap and the two answer buttons on page 4 and chapter 8 stay shut until the chapter's prediction** is committed or revealed; the kit's held rule card does the same for the chapter pages.
10. **The map carries the whole week's picture**, five panels, with Friday's filled when chapter 7's prediction is revealed.
11. **Cut**: the campaign-size control of the first page (20,000 customers), since no notebook prints those numbers; the bank months on page 3; the Instacart scene's second metric, since the post gives no number for it.
12. **Deck**: no slide pictured the old page, so only the notes of S28 and S35 were rewritten and the deck rebuilt with `scripts/build_deck.py`.

### Review

- `python3 scripts/html_sweep.py` on the page: 11 routes walked, 366 controls clicked, 0 inert, 0 console errors.
- `python3 scripts/explorer_shots.py --end --tabs`: 76 pictures at 1366 and 390 wide, 0 console errors; every picture was read before and after its reveal, and the overlaps, clipped labels and early answers they showed were fixed before the push.
