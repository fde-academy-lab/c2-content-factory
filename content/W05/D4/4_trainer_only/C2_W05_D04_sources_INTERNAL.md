# W05 D4 sources, numbers and decisions

INTERNAL. Built on 28 October 2026 for Thursday 5 November 2026. Python 3.13.17, pandas 3.0.5, scikit-learn 1.9.1, numpy 2.5.3, matplotlib 3.11.2 in the build session.

## Datasets

| Dataset | Where it is used | URL | Licence | Checked |
|---|---|---|---|---|
| UCI Bank Marketing, `bank-additional-full.csv` (41,188 rows, 11.27 percent yes) | case01 to case03, guided notebook, deck, practice set, notes | https://archive.ics.uci.edu/dataset/222/bank+marketing (download https://archive.ics.uci.edu/static/public/222/bank+marketing.zip) | CC BY 4.0, read on the page, verified 28 October 2026 | verified 28 October 2026 |
| German Credit, OpenML credit-g (1,000 rows, 30 percent bad), the documented 5:1 cost matrix | practice lab and its solutions, practice set problem 10, interview bank Q22 | https://www.openml.org/api/v1/json/data/31 (record: credit-g, version 1, licence "Public", uploaded 2014-04-06) | "Public" on OpenML; the UCI copy is CC BY 4.0 (W05_datasets.md) | verified 28 October 2026 |
| Invented teaching tables (three students, ten Kalpa customers, twelve footfall weeks, twenty shoppers, twelve loyalty shoppers, two invented models' folds, twenty-two invented stores in the explorable, which replaced the earlier page's thirty) | ch01 to ch05, the explorable, practice set problems 1, 2, 3, 5, 7 | typed in the cells and the page, labelled invented | ours | not applicable |

Every notebook downloads its file in code with the contract's cached loader into `~/.cache/c2_datasets`, never into the repository.

## Numbers, as run (the run is the source; the row's 100 and 61 do not appear)

| Number | Value | Where it was produced |
|---|---|---|
| Split | train 24,712, validation 8,238, test 8,238 sealed; call nobody 88.7 percent right on validation (7,310 of 8,238) | case01 |
| Unlimited tree | training accuracy 99.6 percent, validation 84.1 percent, depth 37, 3,662 leaves, 1,709 with one customer, 2,323 (63 percent) with one or two | case01 |
| Depth curve | validation error 11.3 percent at depth 1, 10.05 at depth 3, 10.1 at depth 6, 11.8 at depth 15, 15.9 with no limit; validation AUC peaks at 0.781 at depth 7 | case01 |
| Learning curves at 19,769 rows | stump 11.3 and 11.3; unlimited 0.3 and 16.5; depth 6 leaf 50, 9.8 and 10.1 (percent wrong) | case01, guided |
| Five deals of the same rows | validation AUC 0.786 to 0.790 | case02 |
| Five folds, braked logistic | 0.769 to 0.798, mean 0.786, spread 0.0136 | case02, case03 |
| Scaler before the folds | 0.00003 AUC difference | case02 |
| C sweep | C 0.0001: 0.762; C 0.01 to 100: 0.784 to 0.786 under folds | case02 |
| L1 | C 0.03 keeps 20 of 63 columns, validation AUC 0.794; C 1 keeps 45, 0.795 | case02 |
| Race under five folds | tuned tree (depth 6, leaf 50) 0.782, logistic 0.786, forest 0.791, boosting 0.793 | case03 |
| Race on validation | logistic 0.796, tree 0.790, forest 0.803, boosting 0.804 | case03 |
| Boosting minus logistic, fold by fold | +0.007, +0.007, +0.003, +0.014, +0.003 AUC | case03 |
| Bills at threshold 40 / 1,240 | logistic Rs 2,78,560; tree Rs 2,84,200; forest Rs 2,84,360; boosting Rs 2,81,960; nudge everyone Rs 2,92,400 (8,238 customers) | case03 |
| Top 1,000 of 8,238 (5,000 of 41,188) | buyers 465, 469, 476, 472 against about 113 at random | case03 |
| Boosting's extra buyers per 5,000 nudges, fold by fold | 0, 133, 100, 92, 125; mean 90, spread 48, low end 42 (Rs 50,939) | case03 |
| German Credit | unlimited tree 100 percent training, 67.1 percent under folds against a 70.0 baseline; best depth 5 (0.709); C 0.1 0.784, C 100 0.756; forest 0.791, boosting 0.780; shuffled answers 0.461; bill 429 at 1/6 and 782 at 0.5 | lab solutions; forest and boosting from a build-session run with the lab's folds |
| Time-ordered folds (TRAINER only, Friday's reveal) | five folds cut by row order: 0.515, 0.551, 0.495, 0.716, 0.741 against shuffled 0.79 | build-session run, not shipped in a STUDENT file |

The week pipeline's correction 6 quoted logistic 0.803, tuned tree 0.804 and boosting 0.811; this run on the same seed with the engineered pdays flag gives 0.796, 0.790 and 0.804 on validation. The direction holds and the run's numbers are the ones printed.

## Cases and references

| Fact | Source | Checked |
|---|---|---|
| Airbnb: listing IDs "mostly led to overfitting"; Figure 5's training NDCG toward 1 with flat test NDCG; "at most 365 times in an entire year"; the first network online was a single hidden layer of 32 ReLUs, booking neutral against the GBDT | Haldar, Abdool, Ramanathan, Xu, Yang and others, "Applying Deep Learning To Airbnb Search", https://arxiv.org/abs/1810.09591 (authors read from the arXiv page's citation metadata) | verified 28 October 2026 |
| Pneumonia: neural net AUC 0.86 against logistic 0.77; "HasAsthma(x) => LowerRisk(x)"; 2015 AUCs 0.8432 (logistic), 0.8460 (random forests), 0.8493 (LogitBoost), 0.8542 (GAM), 0.8576 (GA2M) | Caruana and others, KDD 2015, https://www.microsoft.com/en-us/research/wp-content/uploads/2017/06/KDD2015FinalDraftIntelligibleModels4HealthCare_igt143e-caruanaA.pdf | verified 28 October 2026 (quotes as recorded in W05_cases.md the same day; the PDF answered 200) |
| Google Flu Trends: 50 million terms, 1,152 points, high school basketball, "part flu detector, part winter detector", missed 2009 H1N1 | Lazer, Kennedy, King, Vespignani, Science, 14 March 2014, Harvard DASH copy https://dash.harvard.edu/server/api/core/bitstreams/7312037d-0e0d-6bd4-e053-0100007fdf3b/content | verified 28 October 2026 |
| scikit-learn user guide, cross-validation | https://scikit-learn.org/stable/modules/cross_validation.html | verified 28 October 2026 |
| scikit-learn user guide, validation and learning curves | https://scikit-learn.org/stable/modules/learning_curve.html | verified 28 October 2026 |
| StatQuest video index (entries "Machine Learning Fundamentals: Bias and Variance" at https://youtu.be/EuBBz3bI-aA and "Machine Learning Fundamentals: Cross Validation" at https://youtu.be/fSytzGwwBVw, read from the index page) | https://statquest.org/video_index.html | verified 28 October 2026; youtube.com itself answered 429 to the session, so the video links rest on the index page |
| MLU-Explain, Bias Variance Tradeoff and Cross-Validation | https://mlu-explain.github.io/bias-variance/ and https://mlu-explain.github.io/cross-validation/ | verified 28 October 2026 |

**Not verified, not used in any STUDENT file:** the Netflix Prize story (Netflix not deploying the full Prize ensemble, April 2012 tech blog post). netflixtechblog.com returned 403 on 28 October 2026 and a search surfaced no reachable copy of the sentence. The brief asked for it to carry "the simpler model wins"; the verified Caruana pneumonia case carries it instead, and the trainer guide says so.

## Images

Every image in the deck, the practice set, the study notes and the cheat sheet is our own render: matplotlib charts drawn by `C2_W05_D04_make_figures_INTERNAL.py` from the same code as the notebooks, and mermaid diagrams rendered through the shared theme. No third-party image, no logo. The Caruana chart plots the paper's published AUC values, drawn by us.

## Decisions taken in this build

1. **Numbers.** The row's 100 and 61 and its "near-tie within a point" belonged to Kalpa v6 data that was never generated. The deck, notes and practice set quote this run: 99.6 and 84.1 against 88.7. The invented students keep the row's 100 and 61, labelled invented.
2. **"The simpler model wins" on this file.** Boosting's lead is real (it wins every fold), so the case teaches two tests: is the gap real, is it worth its cost. The extra cost of running and explaining boosting is unknown at Kalpa, so it is an invented Rs 75,000 per campaign, labelled invented, and the change that flips the call is printed (63 extra buyers at the low end). This is more honest than calling 0.007 AUC a statistical tie, which a paired reading of the folds contradicts.
3. **Netflix replaced by Caruana**, as above.
4. **The explorable** follows `W05_explorables.md` Thursday (polynomial degree as the curve's version of tree depth, a ridge brake, reshuffle). The brief's "depth and penalty sliders" is met by the degree slider labelled as the curve's version of depth. Its thirty stores are a fixed invented array; the two nearest and two farthest stores always teach so no curve is scored far outside its rows.
5. **Time order.** Shuffled folds are used all day with the caveat said aloud; the time-cut folds (0.50 to 0.74) are Friday's reveal and appear only in TRAINER files.
6. **Run length.** The row's agenda (220 minutes) is fitted into 240 trainer minutes: 180 in block one and 60 in block two before the tentative faculty block. Drill 2 runs at 10 minutes inside case 3; the row's unguided exercise is case03 run by learners plus the "rerun with one column removed" BUILD task, which fills the faculty block's 120 minutes if it does not run.
7. **Quiz item 1** uses this run's numbers (99.6, 84.1, 88.7) in place of the row's 100 and 61.
8. **Branding.** `scripts/deck_layout.py` still draws the institute's logo and name on every slide. The deck is stripped after each build by `C2_W05_D04_strip_branding_INTERNAL.py` (63 logos and 126 text boxes removed). A shared fix in the deck layout would remove the need; it was left to the orchestrating session so five parallel day builds do not edit the same script. The orchestrating session moved this into the shared builder (pull request 266): from Week 5 on `scripts/build_deck.py` draws no logo or institute name, so the stripping script was removed and the deck rebuilt.
9. **mermaid-cli** needs `PUPPETEER_EXECUTABLE_PATH=/opt/pw-browsers/chromium` in this container, because `build_cheatsheet._chromium()` looks for `chrome-linux/` and the installed browser sits in `chrome-linux64/`. No script was changed.
10. **The practice lab** is a TODO twin (unexecuted, measured on its source) and its solutions are executed. German Credit's `duration` (loan length in months) is flagged in the lab as the same name with a different meaning from the bank's leaked `duration`.
11. **Nothing found today is shown before it is found.** The ticket slide shows the 99.6 and hides the validation score until case 1; the opening timeline slide shows Thursday's panel empty (`fig_timeline_open`) and the filled U returns at the close (S54a).
12. **The guided exercise uses three models the room has not seen as curves**: a tree capped at depth 12 (variance whose gap closes with rows, 12.4 points at 1,236 rows to 4.2 at 19,769), logistic at C = 0.0001 (bias from a brake set far too hard) and logistic at C = 0.1 (about right). Case 1 has already shown the stump and the unlimited tree with their names, so reusing them would test memory.
13. **Role labels for invented people.** The three invented students are "the memoriser", "the learner" and "the skimmer", so no STUDENT file names a person outside Kalpa's cast (Anand, Rohan).
14. **Real cases on the deck.** Airbnb sits on S38 (more rows against the brake) and Google Flu Trends on S43 (selection learns from the answers), each as one line with its source; Caruana carries chapter 5 (S30).
15. **Shared tooling.** Both `build_cheatsheet._chromium()` and `html_sweep.ensure_browser()` look for `chrome-linux/` and this container's browser sits in `chrome-linux64/`; mermaid rendering worked with `PUPPETEER_EXECUTABLE_PATH` set, and html_sweep fell back to asking playwright for a browser and then passed.
16. **Cheat sheet length.** The cumulative "everything so far" lines run one per week for Weeks 1 to 4, from the day lines in `docs/programme/calendar.md`, and one per day for Week 5, to keep the printed sheet at two pages.

## Skills read and what was taken

| Skill | What was taken |
|---|---|
| training-deck-builder, pptx | the deck's chapter openers, one idea per slide, the render check of every slide after the build |
| notebook-builder | the rhythm of each notebook (what you will do, the prediction, the run, the check, what you carry forward) and checks that assert on shape |
| exercise-builder | distractors from real misconceptions, keys spread across letters, keys never the longest option (audited by script) |
| study-notes-builder, fde-cheat-sheets | per chapter: the picture, three lines, the worked example, the trap, the interview line; the cumulative sheet |
| companion-builder, design-taste-frontend | one question, two sliders and one button, a wrong default, a prediction before the reveal, linked picture and numbers |
| concept-packaging | the memorising student as the sticky handle for variance |
| humanizer, llm-tic-scrubber | the read of every prose file for staged openers, triads and stock phrasing |

## The explorer, rebuilt on 29 October 2026

Rebuilt in place as the day companion of decision `w5-explorer-companion`, on branch `w05-d4-explorer`, with the Week 5 kit (`scripts/companion/w5kit.js` and `w5kit.css`, inlined by `scripts/build_companion.py`) and the briefs `docs/detailing/W05_briefs/explorers/common.md` and `D4.md`. Eleven routes: `#story`, `#map`, `#p1` to `#p5`, `#case`, `#field`, `#interview`, `#check`. It replaces decision 4 above.

### Data

| Number on the page | Where it comes from |
|---|---|
| The story's 16,476 dots: 8,238 validation customers right or wrong under the unlimited tree, and 8,238 of the 24,712 training customers drawn with seed 5 (34 wrong) | `C2_W05_D04_explorer_data_INTERNAL.py`, which reruns case01's pipeline and writes `C2_W05_D04_explorer_data_INTERNAL.json`, 30 KB |
| 99.6 and 84.1 percent (24,623 of 24,712 and 6,925 of 8,238), 88.7 (7,310), depth 37, 3,662 leaves, 1,709 and 2,323; the fifteen-depth curve; the three trees' learning curves at 988 to 19,769 rows | the same script, against case01 |
| Five deals 0.786 to 0.790; folds 0.7709 to 0.7983, mean 0.786, spread 0.014; 0.78648 against 0.78645; the C sweep; L1's 2 to 45 columns | the same script, against case02 |
| The race's folds and means, the paired leads +0.007, +0.007, +0.003, +0.014, +0.003, the bills Rs 2,78,560 to Rs 2,92,400, 465 to 476 buyers in the top 1,000, the extra buyers 0, 133, 100, 92, 125, the low end 42.45 buyers and Rs 50,939 | the same script, against case03; the extra cost of Rs 75,000 is case03's invented figure |
| The twenty shoppers' deals and folds (60, 60, 80, 40, 60; 100, 0, 75, 25, 100), the teaching means (3.81 in turn 1) and 4.10 | the script's invented block reruns notebook ch03's calls |
| The twelve shoppers' tree, the five forest trees with their bootstrap draws, the booster's four stumps and scores, k-means from shoppers C, G and I, and the 3, 280 and 200 leaves | the script's invented block reruns notebook ch04's calls; each forest tree's draw is scikit-learn's own (`_generate_sample_indices`), checked against the tree's root count |
| The three students and their learning curves | typed in the page exactly as notebook ch01 types them |
| The twenty-two stores of `#p1` and `#p2`, the ridge and lasso fits, and the two-weight picture | typed and computed in the page; the page's 0.50 and 30.17 at twelve bends, 2.73 and 1.52 at four, and 2.42 and 1.52 at alpha 0.01 were checked against numpy on this machine, and the lasso path against a Python coordinate descent |
| Airbnb, Caruana and others, Google Flu Trends | `docs/detailing/W05_research/W05_cases.md`; each PDF answered on 29 October 2026 and the quoted lines were re-read in it, so the page's source lines carry that date |

The script stops with an error before writing any JSON unless all 38 numbers it checks equal what the notebooks print; all 38 passed on this machine.

### Decisions

1. **New invented stores for `#p1` and `#p2`.** The earlier page's thirty stores gave a shallow U at its default split (held-out error 9.0 at twelve bends against 7.0 at four). Twenty-two stores, seven held out, give a U a room can read: twelve bends thread the teaching stores at 0.50 and dive to 30.17 where three held-out stores sit, four bends reach 1.52, and a brake of alpha 0.01 at twelve bends returns to 1.52. The depth and brake sliders of the earlier page are kept as the cores of `#p1` and `#p2`.
2. **The brake is labelled twice.** The curve is a ridge regression whose knob is alpha, and the readout prints the C that LogisticRegression would write for it (C = 1 / alpha), so the C trap of slide S16 is on the page.
3. **The L1 diamond and the L2 circle are drawn as a picture.** D4.md asks for them; the trainer guide's "do not teach today" keeps the derivation for the faculty block, so the page shows where the ring touches each shape and names the zero, and derives nothing. The trainer guide's row now says so. The two-weight bowl is invented and its brake is labelled lambda, apart from the curve's alpha.
4. **Training is violet, held out is amber.** The notebooks draw held-out error in rose; the kit keeps rose for wrong answers beside a cross, so the page uses its second series colour for every held-out, validation or exam score.
5. **The story reveals 84.1.** D4.md puts the reveal on `#story`; the deck holds 84.1 until case 1. The run table opens `#story` at the opening for scenes 1 to 3 with the guesses taken aloud and nothing committed, and commits and plays scene 4 at S34. The deck's notes for S4, S33 and S34 say so.
6. **Equal piles in the story.** The training pile is a seeded third of the 24,712, so both piles hold 8,238 dots and the 34 wrong answers on practice sit beside the 1,313 on the exam at the same density. Wrong dots are drawn larger in the grids to be seen, and true to size once they are piled, so the two piles and the outline of calling nobody's 928 compare by height.
7. **`#p4` names the shoppers A to L** so the captions can say which shopper the booster's second round fixes (B) and which one k-means moves (F).
8. **`#p5` plays Thursday's real race, and the case page's chapter 8 judges four models three ways** (AUC on folds, the bill at the cost line, buyers in the top 1,000), so the two tests are not repeated: the case adds the forest, the tuned tree and the finding that the highest AUC does not buy the smallest bill at the cost line.
9. **The Airbnb and Google Flu Trends charts are drawn with invented numbers in the shape the sources describe**, labelled invented on the stage; neither paper's plotted values are copied.
10. **Answers stay hidden until the reveal**: the exam pile and the exam bars, the students' exam scores, the errors at alpha 0.01, the deal scores, the forest's 280 leaves, the decision at Rs 75,000, the single-customer leaf bar, the lowest validation error, the folds' AUCs, the four bills and the Airbnb test curve show a question mark, a dashed outline or nothing until the learner commits or reveals.
11. **Cut**: the earlier page's reshuffle button and five-split table (the five folds of `#p3` and case 2's deals and folds carry that idea on the notebook's own numbers), its blurred numbers card (the kit's prediction card replaces it), and the time-ordered folds, which stay Friday's reveal.
12. **Slides.** No slide pictured the earlier page; the notes of S4, S5, S11, S15, S20, S22, S30, S33, S34, S38 and S43 were rewritten for the new clicks and the deck was rebuilt with `scripts/build_deck.py` (`PUPPETEER_EXECUTABLE_PATH=/opt/pw-browsers/chromium`, as decision 9 records); only those eleven notes changed.

### Proof

- `python3 scripts/build_companion.py` inlines the kit and the data; `--check` passes.
- `python3 scripts/html_sweep.py` walks all eleven routes with no inert control and no console error.
- `python3 scripts/explorer_shots.py` at 1366 and 390 wide, with `--end`, plus a session script that opened every tab and every picture toggle and set the states that matter (the shapes with the brake on, the deals played out, the booster and k-means at their last frames, a learning curve fully built); every picture was looked at, and the overlaps, clipped labels, an undefined colour and small type it found were fixed.
- This container's Chromium sits at `/opt/pw-browsers/chromium-1243/chrome-linux64/chrome`, which `find_chromium()` in `scripts/html_sweep.py` does not search, so the sweep and the screenshots ran with `PLAYWRIGHT_BROWSERS_PATH` pointing at a scratch folder that links the binary under `chrome-linux/`.
- Skills used: companion-builder's Rules (every control visible, no storage or network, instant scrolling, the checked date on each link's line), design-taste-frontend (one accent locked, no three equal cards, a grid with no empty cell, so the forest's sixth cell is its tally), dataviz (one axis per chart, text in ink, a legend for two or more series, a numbers table behind the charts that carry one).
