# W05 SAT sources: every fact the Saturday pack uses, with its check, and every decision the build made

INTERNAL. One page for the reviewer. One session built this pack on 28 October 2026 on the branch
`w05-sat`, in one long turn with nobody to answer questions, so every call the rules left open is
recorded below with its reason. Every link was fetched in this session on 28 October 2026. Every
bank-campaign number on the paper is either in the week's pipeline file
(`docs/detailing/W05_research/W05_week_pipeline.md`) or in the re-run table of
`C2_W05_SAT_provenance_INTERNAL.md`, and `C2_W05_SAT_key_proofs_INTERNAL.py` checks each one
(`--rerun` recomputes them from the UCI file).

## Which decisions did the build make, and why?

| Decision | What the pack does | Why |
|---|---|---|
| The paper's length | 60 minutes; 24 timed items at 57 minutes by the blueprint's pace | `saturday_papers.paper_minutes` in `data/programme/facts.yaml` names W01, W02 and W04 only, so the builder takes the tracker's slot of 60, which is also the Saturday row's (`docs/curriculum/W5_ML_core_ME1.md`) and the orchestrator's brief |
| The Saturday's length | 300 minutes in the discussion guide, with the row's blocks at the row's minutes | `campus_day.saturday_minutes` is 300 and locked, and facts.yaml ranks above the row's "Four hours"; the 60 extra minutes go to the break, the paired mock-interview round that `campus_day.saturday` names, and the ME1 window's ceiling of half the block |
| ME1 | The guide names ME1's four theme areas and reserves up to half the block; it states no marks, no weight, no day and no slot, and the paper does not mention ME1 | The row says "reserved without stating marks or slot"; `evaluation.exam_day_and_slot` is open and its rule forbids stating a day or a slot; the brief forbids marks or weights anywhere |
| What prints | Three bank items, the blanks of banks 1 to 3, each from a word bank; 26 bank items fold into 21 additions; none moves to the stretch page | At the bank's own pace the 29 items fill 59.5 of the 60 minutes, which leaves no time for the reasoned formats decision `saturday-interview-grade` asks for, and nine of the bank's thirteen option sets fail `scripts/distractor_audit.py` as the tracker prints them: in items 10, 11, 13, 14, 15 and 17 the key is the longest option, and in items 19, 20 and 21 the shortest option is under 60 percent of the longest. Folding keeps every bank concept inside the timed paper, so the stretch page carries three new written follow-ups instead |
| No edits to `data/programme/paper_edits.yaml` | The failing option sets are folded into additions written to pass, never reworded in the shared edits file | Every change stays inside `content/W05/SAT`, so the pack cannot collide with another session's edits to a file every Saturday reads |
| The data on the paper | Every part opens on UCI Bank Marketing (41,188 calls, CC BY 4.0) as the week's pipeline split and scored it; the rupee costs are Kalpa's from the rows (Rs 40, Rs 1,200, Rs 60,000, Rs 3,000) | The orchestrator's brief and the plan's thread two: the paper must match what the room ran. The row's planted Kalpa figures (the 96 to 4 split, the thresholds 0.12 and 0.85, settlement_status at 0.99) belonged to a Kalpa dataset that was never generated (the plan's section 6), so none prints; the proofs fail if one does. settlement_status is named once, as the leak Wednesday told as Kalpa's, with no number |
| Levels | 3 easy, 14 medium, 7 hard: 29 percent hard | Decision `saturday-interview-grade` asks about 60 percent, and exercise-builder's bar says a hard item combines at least two ideas on an exhibit or takes several dependent steps, while a single judgement or arithmetic the stem sets up is medium whatever it is labelled. The first draft labelled 15 hard; the blind sitting graded 4 hard; the fix pass deepened Q13 (a published indicator whose quarter has not closed) and Q24 (two applicants against a line the learner must compute), took the budget's answer off Exhibit 2B for Q10, and the honest count by the bar is 7: Q2, Q10, Q13, Q19, Q20, Q21 and Q24. Reaching 60 percent would mean replacing medium items with new multi-step ones, which the 60 minutes do not hold at the bar's pace; it is flagged for the orchestrating session |
| Formats | Three word-bank blanks, each placed last in its part, eleven one-correct items, four statements judged with their reasons (two keyed True, two False), four more-than-one items and two worked items | Decision `saturday-interview-grade`; the row's format list. Each bank blank defines the term a later item asks the learner to apply, so it prints after them. The bank's scenario set (items 22 to 26) folds because its item 25 prints the answers to its items 22 and 24 in its options |
| What the paper never prints | No student-facing line prints 0.032 (Exhibit 2B labels the row "The cost line"), the dataset's discard note, a timeline placing duration after the call, the word leaky, or the split by date's AUC | Each would answer a later or earlier item: Q8 derives the cost line, Q12 and Q13 test duration's timing, and Q2 judges the random split. The note and the timeline were the week's teaching, so they sit in the key and the guide; the proofs fail if 0.032, 1 in 31, F1's working or 0.657 appears on the paper |
| Real cases | Instacart (Fortune and Instacart's engineering blog) and Booking.com (KDD 2019), each refetched today | Decision `saturday-real-cases`: each figure on the paper is in a fetched source below. The week's other verified cases stay in the discussion guide or unused |
| The fraud anchor | "Precision or recall for fraud, and why?" is answered in the discussion guide only | The bank holds no fraud item, so the paper tests what the bank sets; the guide answers it from the cost rule and Build 2's seed, fraud at half a percent positives (`docs/07_Client_Zero.md`), with no outside figure |
| Student files | The paper is the one STUDENT file | The brief lists the paper, the key, the workbook, the proofs, the guide, the sources and the provenance; Build 2's briefs "ship when they lock" (the row), so the preview runs from the guide |
| "Monday" in the builder's fixed lines | Left as the builder prints it ("Monday's revision", "Monday's remediation read") | Monday 9 November is off after Diwali and Build 2 opens on Tuesday 10 November; the guide says the read feeds Tuesday. Changing the shared builder would re-render every built Saturday, so it is flagged for the orchestrating session instead |
| Rendering the exhibits | `PUPPETEER_EXECUTABLE_PATH=/opt/pw-browsers/chromium-1243/chrome-linux64/chrome` set for the `--docx` run | `_chromium()` in `scripts/build_cheatsheet.py` looks for `chrome-linux/chrome`, and this session's browser sits in `chrome-linux64`; without the variable mermaid-cli wrote no picture. No script was changed; flagged for the orchestrating session |
| The chart's key | Exhibit 4A's title names the upper line training and the lower line validation | Mermaid's xychart draws no legend |

## What did the blind sitting find, and what changed?

One fresh agent sat the student paper alone on 28 October 2026, as exercise-builder's review asks,
and matched all 26 keys of that draft. One fix pass followed; every change below is in the source
file, and the proofs and the audit passed after it.

| Finding | What changed |
|---|---|
| All four true-or-false items were keyed False | Q2 and Q20 now state the claim the key holds, so two read True and two False |
| Exhibit 5A's memo boxes said "where it is weak, when it goes stale" beside Q22, which asks what goes in the caveat | The boxes print the four names only |
| Q10's option b printed precision 0.65, Q7's first answer, and Exhibit 2B's top 1,000 row printed Q10's answer | Option b names no figure, and the row is gone; the 404 lives in the option and the proofs read it from the pipeline file |
| Bank 4's "100 percent on training and 61 percent on validation" sat beside Exhibit 4A's 0.996 and 0.619, two metrics, and bank 4 and bank 5 were cued by Part 4's title and by Q19's and Q20's options | Both fold into the items that test them, Q17 and Q19, and Part 4 prints no blank |
| Stretch 2 named boosting as the model to justify, which tells Q20 its key | Stretch 2 asks about two unnamed models within a hair |
| Q4's option d could be read as a historical rate; Q22's option b as the segment scored lowest; Q18's option d as choosing rather than braking; Q17's key as committing to depth 5 inside the noise | Each option was reworded to the reading the key holds |
| Q8 should accept 1 in 30, from one buyer paying for 30 calls | The key accepts 0.033 beside 0.032 |
| Q20's reasoning compared a paired gap with the folds' spread | The key now says another split could reorder the models and names the paired test on the same five folds |
| Exhibit 5B's Instacart line read as garbled | It follows Fortune's words: a metric used to evaluate the model that predicts whether an item is in stock |
| Q24's options print the cost-over-costs form that Q8 asks for | Kept: Q24 sits after Q8, and its options now print the line only as "near a 5 percent chance" |
| Difficulty: 4 hard | Relabelled to 7 by the bar after the fix pass, as the Levels row says |

## Which data does the paper print, and where does each number come from?

| Number on the paper | Where | Source |
|---|---|---|
| 41,188 calls, 4,640 yes, 11.27 percent; May 2008 to November 2010; date order | Part 1's intro, Exhibit 1A | The UCI download's `bank-additional-names.txt`, "Number of Instances: 41188 for bank-additional-full.csv" and "ordered by date (from May 2008 to November 2010)", read 28 October 2026; the count of yes from the CSV in this session's re-run |
| The split 24,712, 8,238 and 8,238; 928 validation buyers; the do-nothing 0.887; the customer-table model's AUC 0.761, accuracy 0.897, TP 174, FP 94, FN 754, TN 7,216 | Exhibits 1A and 2A, Q6, Q7 | The pipeline file's model table, matched exactly by this session's re-run |
| The thresholds 0.20, 0.10 and the cost line (864, 2,754 and 7,438 called); the top 1,000's 404 buyers | Exhibit 2B, Q9, Q10's option c | The pipeline file's threshold table and budget line, matched exactly by the re-run |
| AUC 0.795 and 0.932, accuracy 0.899 and 0.907, 211 and 390 buyers | Exhibit 3A, Q12 | The pipeline file's model table, matched by the re-run |
| poutcome success, 65 percent yes; durations 553 and 221 seconds on average; euribor3m at -0.92 alone and +0.39 with the indicators, and its correlations of 0.97, 0.95 and 0.28 | Q13, Q14, Q15 and Q15's key | This session's re-run (provenance, re-run table); the pipeline file states the 65 percent and the sign flip in words |
| The tree by depth, the five folds, the three families, the split by date | Exhibits 4A, 4B and 5A, Q17, Q19, Q20, Q21 | This session's re-run (provenance, re-run table) |

## Which public facts does the pack use, and what did the fetch confirm?

| Fact as the pack states it | Where | Source, checked 28 October 2026 | What the fetch confirmed |
|---|---|---|---|
| The dataset's notes say duration "is not known before a call is performed" and "should be discarded if the intention is to have a realistic predictive model" | Q12's key; the guide | `bank-additional-names.txt` inside https://archive.ics.uci.edu/static/public/222/bank+marketing.zip (checked 28 October 2026) | Attribute 11: "Yet, the duration is not known before a call is performed. Also, after the end of the call y is obviously known." and "this input should only be included for benchmark purposes and should be discarded if the intention is to have a realistic predictive model." The note's link word between the two sentences is on the repository's banned list, so the pack quotes the two clauses only |
| The dataset is CC BY 4.0, cited as Moro, Rita and Cortez (2014) | Part 1's intro, the Rules table | https://archive.ics.uci.edu/dataset/222/bank+marketing (checked 28 October 2026) | "licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) license"; "Moro, S., Rita, P., & Cortez, P. (2014). Bank Marketing [Dataset]. UCI Machine Learning Repository." The web page's own variable table carries no discard note, so the pack cites the names file |
| A metric used to evaluate Instacart's in-stock model fell from 93 percent to 61 percent and told the engineers to retrain; about 85 percent by June | Exhibit 5B, Q21's key, the guide | https://fortune.com/2020/06/09/instacart-coronavirus-artificial-intelligence (checked 28 October 2026) | Jonathan Vanian, 9 June 2020: "The accuracy of a metric used to evaluate how many items are found at a store dropped to 61% from 93%," "tipping off the Instacart engineers that they needed to re-train their machine learning model"; "is now correct about 85% of the time," "according to an Instacart graph" |
| Models respond slowly because they need enough new observations; thresholds were changed without training new models | Exhibit 5B, Q21's key | https://company.instacart.com/tech-innovation/how-instacarts-item-availability-evolved-over-the-pandemic (checked 28 October 2026) | Dated 10 July 2023: "ML models exhibit a sluggish response as they require ample observations to adapt"; "by changing these thresholds, we can trade off between these metrics without having to train new ML models" |
| Booking.com: offline performance is a health check; 23 comparisons (46 models); Pearson -0.1, 90 percent interval -0.45 to 0.27 | Exhibit 5B, Q23 and its key, the guide | Mirror copy of the KDD 2019 paper, https://blog.kevinhu.me/2021/04/25/25-Paper-Reading-Booking.com-Experiences/bernardi2019.pdf (checked 28 October 2026); canonical DOI 10.1145/3292500.3330744 | Section heading "MODELING: OFFLINE MODEL PERFORMANCE IS JUST A HEALTH CHECK"; "We include a total of 23 comparisons (46 models)"; "the Pearson correlation is -0.1 with 90% confidence interval (-0.45, 0.27), and Spearman correlation is -0.18 with 90% confidence interval (-0.5, 0.19)"; "increasing the performance of a model, does not necessarily translates to a gain in value". The ACM page returned 403 to the research session that verified the case, so the mirror stands, as `W05_cases.md` records |
| German Credit's cost matrix: a bad borrower classed good costs 5, a good borrower classed bad costs 1 | Stretch 1 and its answer | https://www.openml.org/api/v1/json/data/31 (checked 28 October 2026) | The description of credit-g: "This dataset comes with a cost matrix", rows Good 0 1 and Bad 5 0, "It is worse to class a customer as good when they are bad (5), than it is to class a customer as bad when they are good (1)." The OpenML search page itself rendered empty to the fetch, so the API's copy of the description stands |
| StatQuest's video index lists cross-validation, the confusion matrix, ROC and AUC, regularisation, trees, random forests and logistic regression | The guide's after-session line | https://statquest.org/video_index.html (checked 28 October 2026) | HTTP 200; entries such as "Machine Learning Fundamentals: Cross Validation", "Machine Learning Fundamentals: The Confusion Matrix", "ROC and AUC", "Regularization Part 1: L2, Ridge Regression" and "Random Forests Part 1: Building, using and evaluating" |
| scikit-learn's C is the inverse of regularisation strength, so a smaller C is a stronger penalty | Q18 option b and its key | The docstring of `sklearn.linear_model.LogisticRegression` in scikit-learn 1.9.1, read in this session on 28 October 2026 | "Inverse of regularization strength"; "smaller values specify stronger regularization" |

## Which links were checked and are not used?

| Link | What the check found | Why it is not used |
|---|---|---|
| Interview Query, the row's trainer resource, https://www.interviewquery.com/p/python-data-science-interview-questions (checked 28 October 2026) | HTTP 429 | Unverified today, so no file in the pack carries it; the row's own date, 3 September 2026, stands in the row |
| Stripe's Radar guide, PhonePe, Razorpay, Flipkart's BIRDNEST paper, Uber's DeepETA and Michelangelo posts, Google's Rules of ML, Zech and others, Caruana and others, Google Flu Trends and Zillow's 8-K, as `W05_cases.md` verified them on 28 October 2026 | Not refetched by this session | The paper prints none of them, and the guide names none, so nothing rests on them |

## Which corrections does the pack carry?

| Source of the error | What the pack prints | Why |
|---|---|---|
| The pipeline file's council note 3: at Anand's costs "the bill is within one percent of calling everyone" | Nothing on the paper rests on it; the guide gives the re-run's figures, Rs 279,000 at the cost line against Rs 292,400 for calling everyone, 4.6 percent less | This session's re-run, pricing wasted calls at Rs 40 and missed buyers at Rs 1,200, gives 4.6 percent; pricing every call, the gap is 4.2 percent; neither is within one percent |
| The plan's Tuesday line, "the model at 0.5 (precision 0.69, recall 0.22)" | Precision 0.65 and recall 0.19 on the customer table (Q7) | The pipeline file and the re-run both print 0.649 and 0.188; 0.641 and 0.227 belong to Wednesday's model with the economic indicators |
| The plan's Thursday line, "99.5 percent on training, 84.2 on validation", and the council's "train 0.996, test 0.836" | Training 0.996 and validation 0.837 (Exhibit 4A) | The re-run on the honest columns; the test slice stays sealed until Friday, so the paper prints validation |
| The council's "logistic 0.803, tuned tree 0.804, boosting 0.811" | Logistic 0.795, random forest 0.799, gradient boosting 0.806 on validation (Exhibit 4B) | The council's configuration is not recorded; the re-run is, in the provenance, and the near-tie the item tests holds on both |
| The research brief's citation order "Moro, Cortez, Rita" | Moro, Rita and Cortez | The UCI page's own citation |

## What must no item reach for?

`W05_cases.md` lists cases it could not verify, and no file in this pack uses them: Netflix's
2012 post on not shipping the Prize ensemble; Swiggy's and Zomato's delivery-time posts; Kaufman,
Rosset and Perlich's leakage paper and the KDD Cup 2008 leak; Flipkart's own address-model story;
Razorpay's "8X" figure; Ola and Meesho, which have no Week 5 post; and Uber's Project RADAR, which
publishes no numbers.
