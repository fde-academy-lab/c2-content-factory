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
8. **The logo and the institute name are stripped after the build** by `C2_W05_D01_strip_logo_INTERNAL.py`, since `scripts/deck_layout.py` stamps both on every slide and five day sessions run in parallel; editing the shared layout would collide with them. The programme line and the day line stay. The orchestrating session then moved this into the shared builder (pull request 266): from Week 5 on `scripts/build_deck.py` draws no logo or institute name, the stripping script was removed and the deck rebuilt.
9. **The deck has no cover slide, and the row's residual-match drill is slide S34a.** `build_deck.py` produced none from the title lines; the first slide carries the day's three layers. The drill's four plots are real Auto MPG residuals drawn as one slide-sized picture, so its labels print at slide size; the practice set's A6 repeats it with a second, written part.
10. **Mermaid rendering** needed `PUPPETEER_EXECUTABLE_PATH=/opt/pw-browsers/chromium`, because `scripts/build_cheatsheet.py` looks for `chrome-linux/chrome` and this container ships `chrome-linux64/chrome`. No shared script was edited.
11. **Run table minutes:** block one 180 trainer minutes (opening 8, chapters 15, 22, 20, 22, a 10-minute break, 22, 18, case 1 with the guided notebook 43); block two 60 trainer minutes (case 2 25, case 3 15, interview and seat 7, quiz and close 13) before the tentative 120-minute faculty block. The concept block is 119 minutes, inside the 60 to 120 rule.
12. **The guided notebook ships executed** with its TODO cells holding `None` and printing TODO, and an answer cell that prints PASS; its column check compares a fingerprint, so the source never prints the 13 names before the answer cell.
13. **The explorable's right panel asks about any member from 0 to 200 days** instead of the research note's fixed "1.3 against 0.71" pair, which a line fitted to this data cannot produce honestly; the line leaves 0 to 1 past about 120 days.
14. **The practice set's Kahoot-style numbers from the row** (96 to 4, Rs 240 per day of recency) appear only as invented hand items, as the plan's section 6 allows.

## Build log

- Notebooks: `python3 content/W05/D1/4_trainer_only/C2_W05_D01_build_notebooks_INTERNAL.py` writes all twelve and executes each with `jupyter nbconvert --to notebook --execute --inplace`.
- Figures: `python3 content/W05/D1/4_trainer_only/C2_W05_D01_make_figures_INTERNAL.py`.
- Deck: `PUPPETEER_EXECUTABLE_PATH=/opt/pw-browsers/chromium python3 scripts/build_deck.py <deck.md> --footer "Week 5 Monday: regression and classification"`, then the strip script; 63 slides rendered through LibreOffice and inspected on contact sheets.
- PDFs: `python3 scripts/build_doc.py` per STUDENT markdown in folders 2 and 3.
- Explorable: `python3 scripts/html_sweep.py`, 7 controls, 0 inert, 0 console errors.
- MCQs: `scripts/distractor_audit.py` does not parse the Week 5 practice-set layout (its items are `**B1.**` with keys in Part C), so the key rules were checked by a script in this session: no key is the strictly longest option on any single-key item, and keys spread a 4, b 3, c 4, d 4 across the fifteen single-key items.

## The explorer, rebuilt on the Week 5 kit (29 October 2026)

Built on branch `w05-d1-explorer` with `scripts/companion/w5kit.js` 1.0.0, by `python3 scripts/build_companion.py`, from `docs/detailing/W05_briefs/explorers/D1.md` and `common.md`. The page keeps its file name, `1_in_class_training_content/demos/C2_W05_D01_drag_the_line_explorer_STUDENT.html`.

### Routes

| Route | What the learner does there |
|---|---|
| `#story` | Plays six scenes: 41,188 calls land on the week's picture in month columns (one dot for every ten calls), 4,640 light as yes, the bank's ask and Kalpa's Rs 40 against Rs 1,200 twin, then predicts what calling nobody scores before 88.7 percent appears. |
| `#map` | Plays the six subtopics in the row's order with three earlier ideas (Week 1 Thursday, Week 2, Week 4 Friday) and five later ones (Tuesday to Friday, Build 2), and predicts which idea both models rest on. |
| `#p1` | Sorts Kalpa's six asks into query, rule and model bins; each drop plays the mechanism that answers it. |
| `#p2` | Slides the prediction moment and the 60, 90 or 120-day window over four members' eight orders; the table shows the allowed inputs and the whole-log column that leaks. |
| `#p3` | Moves the seed (1 to 60) and stratify on twenty members split 12 / 4 / 4 with the test envelope sealed, then plays the junior's 60-version loop. |
| `#p4` | Drags slope and intercept over 24 customers with every training miss drawn as a square; Mean line, Join first and last, and Least squares buttons. |
| `#p5` | Reads the straight line at 8 visits, switches to the logistic S, moves its weight, and counts 100 members at the asked visit count. |
| `#p6` | Switches the Auto MPG fit between the line and the squared term, reads the residual bow, asks the fit about 300 hp, and sees one S fail on a two-ended pattern. |
| `#case` | Chapter 7 splits with and without a seed; chapter 8 sets the model against calling nobody at full height and as the gap, with the campaign coefficient and the calendar caveat; chapter 9 plays the 60-version peek. Each carries its trap. |
| `#field` | Uber DeepETA (drag the target from minutes to the engine's miss), Google's Rules of ML (rules 1, 4 and 14), Booking.com (regression against stay classes), then the six seats with the senior ML engineer lit. |
| `#interview` | Five situations: is this an ML problem, what 0.71 means, the three slices, linear or logistic, and the one-point edge for Marketing. |
| `#check` | Eight checks, the map with today lit, and Tuesday's question. |

### Numbers the page draws, and where each comes from

| Number on the page | Value | Source |
|---|---|---|
| Calls, yes, share | 41,188; 4,640; 0.1127 | the data script, as case01 prints |
| Calls and yes by month, by year | 26 months; 2008 4.8 percent of 27,690, 2009 19.5 of 11,440, 2010 52.1 of 2,058 | the data script, as case02 recovers the year |
| Split, shares | 24,712 / 8,238 / 8,238; 11.27, 11.26, 11.26 percent | the data script, as case01 prints |
| Sixty splits with no seed and no stratify | held-out share of yes 0.1067 to 0.1197 (shuffles drawn with random_state 1000 to 1059, so the run is repeatable) | the data script; case01's five unseeded runs (0.1096 to 0.1133) sit inside this range |
| Baseline, model, edge | 0.8874 (7,310); 0.8971 (7,390); 80 rows | the data script, as case02 prints |
| Campaign coefficient | odds × 0.9334 per extra call; mean probability 0.1140 | the data script, as case02 prints |
| The peek | 0.9055 (version 45, 7 columns) on 2,000 rows, 0.8971 on 6,238 fresh rows; doing nothing 0.8875 and 0.8873; spreads 0.0072 and 0.0052 | the data script, as case03 prints |
| Auto MPG | 392 of 398 cars; band means +2.73, +0.04, −2.18, −1.74, +0.81 and with hp squared +0.44, +0.05, −0.99, +0.36, +0.10; typical miss 4.89 and 4.36 mpg; 27.8 mpg at 300 hp | the data script, as ch06 prints |
| Concept pages 1 to 5 and the U-shaped S | invented tables typed in the page: the deck's six asks, four members, twenty members and twelve members; 24 invented customers on page 4; 24 invented members on page 6's S | checked in this session with scikit-learn 1.9.1 (least squares slope −28.5 Rs per day, intercept Rs 4,706; logistic a −3.1988, b 1.0472; one S nearly flat at 0.43 to 0.48, 13 of 24 right; the S with age squared 19 of 24 right) |
| Uber, Google, Booking.com quotes | as in `docs/detailing/W05_research/W05_cases.md` | each source refetched in this session: the Uber post and Google's guide on 29 October 2026; the Booking.com abstract page on 29 October 2026 and its section 4 text from the mirror PDF named in `W05_cases.md`, read the same day |

### Decisions taken in this build

1. **AUC and the call list's recall stay off the page.** The brief puts AUC 0.761 and 174 of 928 buyers on the case page; the row's STOP BEFORE forbids any metric beyond accuracy today and both are Tuesday's numbers, so the case page ends on Tuesday's question instead: how many of the 928 who said yes did the model put on the list?
2. **The split by time stays off the page.** The brief's 5.6 against 24.6 percent is Friday's reveal (the pipeline note's correction 2), so a Monday page would spend it. The calendar caveat is told with the deck's yes share by year (S46).
3. **Page 3's sixty-version loop runs on invented numbers.** A concept page uses invented numbers, so the loop scores sixty equally good invented versions (truly right on 78 to 82 in 100) on the same 50 members with a seeded generator in the page; the bank's 0.9055 falling to 0.8971 is case chapter 9.
4. **Page 4 uses new invented customers.** The old page's 24 members followed a curve, so a straight line on page 4 would have taught page 6's lesson early. The new 24 sit on a straight trend with noise; slope in Rs per day of recency, as the brief asks. The rule card cites slide S21's six-member contest.
5. **Page 5 uses the deck's twelve members.** So 1.28 at 8 visits, 0.73 at 4 visits and exp(b) = 2.85 match slides S24 to S28 and notebook ch05. The brief's 71 of 100 near 0.71 moved to interview situation 2; the 100-member grid on page 5 follows the asked visit count instead.
6. **Page 3's seeds are scikit-learn's.** The split of the twenty members for seeds 1 to 60, stratified and not, was computed with `train_test_split` and typed into the page, so seed 42 puts M06, M08, M10 and M18 in the test envelope, as notebook ch03 does.
7. **Page 6 also shows the S failing.** One S on a pattern high at both ends (24 invented members, age against home delivery) lies flat and ties saying no to everyone; a squared term bends it into a U. It sits below the real-data stage with its own invented badge.
8. **No picture or readout states an answer before the prediction.** Page 2 greys the orders after the cut until the reveal; page 4's Least squares button counts as a reveal and says so; page 5 hides the line past 6 visits; page 6 draws the residuals after the reveal; case chapter 8 hides the model's bar; page 3 and case chapter 9 hide the fresh score. The field situations were rewritten so that each quote arrives with its reveal.
9. **No key is the longest option** in any prediction, interview pick or check on the page, counted by hand in this session.
10. **The deck's notes for S20 and S26** pointed at the old page's right panel; both now point at `#p4` and `#p5`, and the deck was rebuilt with `scripts/build_deck.py` and no `--footer`, which reproduces the committed build: a text diff of all 63 slides, their pictures and their notes shows only those two notes changed.

### Kit gaps found

- `html_sweep.py` counts console errors raised while a kit page loads in its total line but does not fail on them; this page logged 16 that way (a chart laid out inside a hidden tab) and passed until it was fixed.
- A cloud label lays out each piece of rich text as its own flex item, so a sentence with bold in it wraps in fragments; the page passes each sentence as one span.
- A chart cannot change its y range after it is built; case chapter 8 sets `chart.o.y` and calls `layout`.
- A toggle has no setter; pages 1 and 5 click its button to switch it from another control.
- The interview whiteboard boxes hold a title, a note and an icon, never a picture, so situation 2's 100 clients cannot be drawn on the board.
- The map's player counts its opening frame as step 1, so step captions that carry their own number print two numbers.
- `explorer_shots.py` shoots only a route's first tab; the case, field and interview tabs were checked with a session script.

### Build log for the explorer

- Data: `python3 content/W05/D1/4_trainer_only/C2_W05_D01_explorer_data_INTERNAL.py` writes `C2_W05_D01_explorer_data_INTERNAL.json` (6,317 bytes).
- Page: `python3 scripts/build_companion.py content/W05/D1/1_in_class_training_content/demos/C2_W05_D01_drag_the_line_explorer_STUDENT.html`.
- Proofs: `python3 scripts/html_sweep.py` on the page; `python3 scripts/explorer_shots.py <page> <scratch> --end` at 1366 and 390 wide, with `--presenter` at 1366, and every tab of the case, field and interview pages shot before and after its reveals; every picture looked at.
