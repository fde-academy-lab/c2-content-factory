# W05 D1 sources, measurements and decisions

INTERNAL. Built 28 October 2026 on branch w05-d1, Python 3.13, pandas 3.0.5, scikit-learn 1.9.1, matplotlib 3.11.2.

## Datasets

| Dataset | URL | Licence, as the page states it | Checked | Used in |
|---|---|---|---|---|
| UCI Bank Marketing, `bank-additional-full.csv` inside `bank-additional.zip` inside the outer zip | page https://archive.ics.uci.edu/dataset/222/bank+marketing; file https://archive.ics.uci.edu/static/public/222/bank+marketing.zip (verified 28 October 2026) | "This dataset is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) license." DOI 10.24432/C5K306; creators S. Moro, P. Rita, P. Cortez | 28 October 2026 | case01 to case03, guided, lab, figures |
| UCI Auto MPG, `auto-mpg.data` | page https://archive.ics.uci.edu/dataset/9/auto+mpg; file https://archive.ics.uci.edu/static/public/9/auto+mpg.zip (verified 28 October 2026) | "This dataset is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) license." DOI 10.24432/C5859H; creator R. Quinlan | 28 October 2026 | ch06, figures, practice set A6 |
| Kalpa warehouse v4 (Week 2, already in the repository) | `content/W02/D1/data/C2_W02_D01_warehouse_v4_STUDENT.sql`, loaded by `.devcontainer/load_warehouse.sh` | the programme's own teaching data | 28 October 2026 | the lab's SQL integration step |

Note: the UCI page gives 45,211 instances, which describes the older `bank-full.csv`; the 21-column `bank-additional-full.csv` the week uses has 41,188 rows, measured.

## Numbers measured in this build

| Number | Value | Where it was run |
|---|---|---|
| Bank rows, yes | 41,188 rows; 4,640 yes, 0.1127 | case01 |
| Week split, seed 42, stratified | 24,712 / 8,238 / 8,238; yes share 0.1127, 0.1126, 0.1126 | case01 |
| Five unseeded splits | held-out yes share between about 0.114 and 0.119 (varies per run) | case01 |
| Majority baseline on validation | 0.8874, 7,310 of 8,238 | case02, guided |
| Logistic on the 13 customer-table columns | accuracy 0.8971, 7,390 of 8,238, edge 80 rows, 0.97 points; mean probability 0.1140 | case02 |
| Validation AUC of the same model (not taught today, Tuesday's number) | 0.7613 | build check, matches `W05_week_pipeline.md` |
| `campaign` coefficient | -0.0690 log-odds per call, odds x 0.933; measured odds ratio 0.9334 on all validation rows | case02 |
| Yes share by year (year recovered from row order) | 2008 0.048 of 27,690; 2009 0.195 of 11,440; 2010 0.521 of 2,058 | case02 |
| The staged peek (2,000-row practice envelope from validation, 6,238 fresh, 60 random column lists, seed 42) | best peeked 0.9055 against 0.8875 doing nothing (edge 1.80); same version fresh 0.8971 against 0.8873 (edge 0.98) | case03 |
| One-line rule `poutcome == "success"` | calls 284, accuracy 0.8988 | lab solutions |
| `contact == "cellular"` rule (a common wrong rule) | calls 5,255, accuracy 0.4386 | build check |
| Shuffled-label model | 0.8874, equal to the baseline | lab solutions |
| Seed 7 | model 0.8977, baseline 0.8874, edge 1.03 points | lab solutions |
| Kalpa warehouse, cutoff 30 June 2026, window to 28 September, delivered orders | 205 members with history, 110 repeat, 0.537; naive whole-log flag 178 of 268, perfectly predicted by its own count | lab solutions |
| Kalpa rule "two or more orders before the cutoff" | accuracy 0.566 | lab solutions |
| Auto MPG | 398 cars, 6 with `?` horsepower, 392 kept; line mpg = 39.94 - 0.1578 x hp; band means +2.73, +0.04, -2.18, -1.74, +0.81; with hp squared +0.44, +0.05, -0.99, +0.36, +0.10; RMSE 4.89 to 4.36; curve vertex about 189 hp; 27.8 mpg predicted at 300 hp | ch06 |
| Auto MPG residual spread | hp-squared residual standard deviation by predicted-mpg quarter 2.53, 3.77, 4.81, 5.80 (the fan in plot Q); mean residual by model year from about -2.9 (1975) to +5.3 (1980) (the trend in plot R) | build check for practice set A6 |

The invented teaching tables (six questions, eight orders, twenty members, six store points, twelve members, the practice set's exhibits, the explorable's 24 members) are typed in cells or in the page and labelled invented where a learner reads them.

## References and company facts

| Fact | Source | Checked |
|---|---|---|
| Uber DeepETA: "We then use machine learning to predict the residual between the routing engine ETA and real-world observed outcomes"; MAE "must improve significantly over the incumbent XGBoost model"; "must return an ETA within a few milliseconds at most"; post dated 10 February 2022 | https://www.uber.com/blog/deepeta-how-uber-predicts-arrival-times/ (verified 28 October 2026) | fetched in this session |
| Google Rules of ML: rule 1 "Don't be afraid to launch a product without machine learning"; "a heuristic will get you 50% of the way there"; rule 4 "Keep the first model simple and get the infrastructure right"; rule 14 "Starting with an interpretable model makes debugging easier"; page last updated 2025-08-25 UTC | https://developers.google.com/machine-learning/guides/rules-of-ml (verified 28 October 2026) | fetched in this session |
| Booking.com, KDD 2019: "a regression predicting the length of a stay, turned in to a multiclass classification problem"; "Setups where simple models can do significantly better than trivial models are preferred" | abstract https://www.kdd.org/kdd2019/accepted-papers/view/150-successful-machine-learning-models-6-lessons-learned-at-booking.com and full text via the mirror listed in `docs/detailing/W05_research/W05_cases.md` (verified 28 October 2026 by the research session) | taken from W05_cases.md, not refetched |
| StatQuest video index lists "The Essence of Linear Regression", "Linear Models Part 1: Linear Regression" and "Logistic Regression"; no entry titled "main ideas" exists, so the row's wording is replaced by the real titles | https://statquest.org/video_index.html (verified 28 October 2026) | fetched in this session |
| scikit-learn 1.9.1, "1.1.1. Ordinary Least Squares" and "1.1.11. Logistic regression" | https://scikit-learn.org/stable/modules/linear_model.html (verified 28 October 2026) | fetched in this session |

## Images

Every PNG in `1_in_class_training_content/slides/img/` is drawn by `4_trainer_only/C2_W05_D01_make_figures_INTERNAL.py` from the two UCI datasets (CC BY 4.0, attributed above) or from the invented tables. No image of unknown licence and no logo is used. Mermaid diagrams are rendered by the shared theme.

## Decisions taken in this build

1. **AUC stays out of every STUDENT file.** The brief quotes validation AUC 0.761 and the row's STOP BEFORE forbids any metric beyond accuracy today; the row wins inside the brief's own list of what it binds. The trainer guide carries 0.7613 as Tuesday's number.
2. **The staged peek keeps the real envelope sealed.** The peek picks the best of 60 random column lists on a 2,000-row practice envelope carved from validation and scores the winner on the other 6,238 validation rows. A peek at the real test slice would have broken the week's device on Monday.
3. **The coefficient read for Marketing is `campaign`.** It is numeric, its unit (one call) is concrete, its direction is a story the campaign manager knows, and the second route (add one call to every client) reproduces it exactly. `poutcome` was kept for the lab's rule so the two do not compete.
4. **The calendar caveat is told with the yes share by year,** in accuracy-free terms, since the measure correction 1 used (AUC 0.795 from year-month alone) is Tuesday's metric.
5. **The rule that beats the model goes to the lab, not the case.** `poutcome == "success"` scores 0.8988 against the model's 0.8971; the row's after-class BUILD asks learners to find a rule baseline themselves, so case 2 does not name it. The trainer guide warns the trainer and the practice set's A9 uses it after class.
6. **The lab's integration step runs the SQL on the Codespace's Postgres,** with a fallback that loads the same warehouse file into in-memory SQLite, so the notebook runs and shows identical numbers on a laptop with no server. Delivered orders only count as purchases; the practice set's A4 makes the learner ask that question.
7. **Kalpa's warehouse is used only for the repeat flag and its baseline.** Its spend column holds a planted bulk order from Week 1, so no regression on Kalpa spend is fitted; the rupee coefficient lives in chapter 4's invented table.
8. **The logo and the institute name are stripped after the build** by `C2_W05_D01_strip_logo_INTERNAL.py`, since `scripts/deck_layout.py` stamps both on every slide and five day sessions run in parallel; editing the shared layout would collide with them. The programme line and the day line stay.
9. **The deck has no cover slide.** `build_deck.py` produced none from the title lines; the first slide carries the day's three layers.
10. **Mermaid rendering** needed `PUPPETEER_EXECUTABLE_PATH=/opt/pw-browsers/chromium`, because `scripts/build_cheatsheet.py` looks for `chrome-linux/chrome` and this container ships `chrome-linux64/chrome`. No shared script was edited.
11. **Run table minutes:** block one 180 trainer minutes (opening 8, chapters 15, 22, 20, 22, a 10-minute break, 22, 18, case 1 with the guided notebook 43); block two 60 trainer minutes (case 2 25, case 3 15, interview and seat 7, quiz and close 13) before the tentative 120-minute faculty block. The concept block is 119 minutes, inside the 60 to 120 rule.
12. **The guided notebook ships executed** with its TODO cells holding `None` and printing TODO, and an answer cell that prints PASS; its column check compares a fingerprint, so the source never prints the 13 names before the answer cell.
13. **The explorable's right panel asks about any member from 0 to 200 days** instead of the research note's fixed "1.3 against 0.71" pair, which a line fitted to this data cannot produce honestly; the line leaves 0 to 1 past about 120 days.
14. **The practice set's Kahoot-style numbers from the row** (96 to 4, Rs 240 per day of recency) appear only as invented hand items, as the plan's section 6 allows.

## Build log

- Notebooks executed with `jupyter nbconvert --to notebook --execute --inplace` from builder scripts kept in the session's scratchpad.
- Figures: `python3 content/W05/D1/4_trainer_only/C2_W05_D01_make_figures_INTERNAL.py`.
- Deck: `PUPPETEER_EXECUTABLE_PATH=/opt/pw-browsers/chromium python3 scripts/build_deck.py <deck.md> --footer "Week 5 Monday: regression and classification"`, then the strip script; 62 slides rendered through LibreOffice and inspected on four contact sheets.
- PDFs: `python3 scripts/build_doc.py` per STUDENT markdown in folders 2 and 3.
- Explorable: `python3 scripts/html_sweep.py`, 7 controls, 0 inert, 0 console errors.
