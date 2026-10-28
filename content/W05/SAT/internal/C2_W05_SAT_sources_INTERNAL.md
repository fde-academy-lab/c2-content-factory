# W05 SAT sources: every fact the Saturday pack uses, with its check, and every decision the build made

INTERNAL. One page for the reviewer. One session built this pack on 28 October 2026 on the branch
`w05-sat`, in one long turn with nobody to answer questions, so every call the rules left open is
recorded below with its reason. A second session raised the paper the same day on the branch
`w05-sat-raise`; the section "What did the raise change, and why?" logs every change it made, and
the rows below state the pack as it now stands. Every link was fetched in this session on 28 October 2026. Every
bank-campaign number on the paper is either in the week's pipeline file
(`docs/detailing/W05_research/W05_week_pipeline.md`) or in the re-run table of
`C2_W05_SAT_provenance_INTERNAL.md`, and `C2_W05_SAT_key_proofs_INTERNAL.py` checks each one
(`--rerun` recomputes them from the UCI file).

## Which decisions did the build make, and why?

| Decision | What the pack does | Why |
|---|---|---|
| The paper's length | 60 minutes; 22 timed items at 58.5 minutes by the blueprint's pace, after the raise (the first build printed 24 at 57) | `saturday_papers.paper_minutes` in `data/programme/facts.yaml` names W01, W02 and W04 only, so the builder takes the tracker's slot of 60, which is also the Saturday row's (`docs/curriculum/W5_ML_core_ME1.md`) and the orchestrator's brief |
| The Saturday's length | 300 minutes in the discussion guide, with the row's blocks at the row's minutes | `campus_day.saturday_minutes` is 300 and locked, and facts.yaml ranks above the row's "Four hours"; the 60 extra minutes go to the break, the paired mock-interview round that `campus_day.saturday` names, and the ME1 window's ceiling of half the block |
| ME1 | The guide names ME1's four theme areas and reserves up to half the block; it states no marks, no weight, no day and no slot, and the paper does not mention ME1 | The row says "reserved without stating marks or slot"; `evaluation.exam_day_and_slot` is open and its rule forbids stating a day or a slot; the brief forbids marks or weights anywhere |
| What prints | No bank item prints as the tracker words it: all 29 fold into 22 additions, and none moves to the stretch page. The first build printed the blanks of banks 1 to 3 from word banks; the raise folded them, since each sat beside an item that tested its word | At the bank's own pace the 29 items fill 59.5 of the 60 minutes, which leaves no time for the reasoned formats decision `saturday-interview-grade` asks for, and nine of the bank's thirteen option sets fail `scripts/distractor_audit.py` as the tracker prints them: in items 10, 11, 13, 14, 15 and 17 the key is the longest option, and in items 19, 20 and 21 the shortest option is under 60 percent of the longest. Folding keeps every bank concept inside the timed paper, so the stretch page carries three new written follow-ups instead |
| No edits to `data/programme/paper_edits.yaml` | The failing option sets are folded into additions written to pass, never reworded in the shared edits file | Every change stays inside `content/W05/SAT`, so the pack cannot collide with another session's edits to a file every Saturday reads |
| The data on the paper | Every part opens on UCI Bank Marketing (41,188 calls, CC BY 4.0) as the week's pipeline split and scored it; the rupee costs are Kalpa's from the rows (Rs 40, Rs 1,200, Rs 60,000, Rs 3,000) | The orchestrator's brief and the plan's thread two: the paper must match what the room ran. The row's planted Kalpa figures (the 96 to 4 split, the thresholds 0.12 and 0.85, settlement_status at 0.99) belonged to a Kalpa dataset that was never generated (the plan's section 6), so none prints; the proofs fail if one does. settlement_status is named once, as the leak Wednesday told as Kalpa's, with no number |
| Levels | After the raise, 0 easy, 9 medium, 13 hard: 59 percent hard by exercise-builder's bar. The raise's blind sitting graded 4 hard and 2 borderline before its fix pass (below). The first build's 3 easy, 14 medium and 7 hard (29 percent) is the history in this row's next cell | Decision `saturday-interview-grade` asks about 60 percent, and exercise-builder's bar says a hard item combines at least two ideas on an exhibit or takes several dependent steps, while a single judgement or arithmetic the stem sets up is medium whatever it is labelled. The first draft labelled 15 hard; the blind sitting graded 4 hard; the fix pass deepened Q13 (a published indicator whose quarter has not closed) and Q24 (two applicants against a line the learner must compute), took the budget's answer off Exhibit 2B for Q10, and the honest count by the bar is 7: Q2, Q10, Q13, Q19, Q20, Q21 and Q24. Reaching 60 percent would mean replacing medium items with new multi-step ones, which the 60 minutes do not hold at the bar's pace; it is flagged for the orchestrating session |
| Formats | After the raise: twelve one-correct items, three statements judged with their reasons (two keyed True, one False), four more-than-one items and three worked items; the word banks went with the blanks they served | Decision `saturday-interview-grade`; the row's format list. Each bank blank defines the term a later item asks the learner to apply, so it prints after them. The bank's scenario set (items 22 to 26) folds because its item 25 prints the answers to its items 22 and 24 in its options |
| What the paper never prints | No student-facing line prints 0.032 (Exhibit 2B labels the row "The cost line"), the dataset's discard note, a timeline placing duration after the call, the word leaky, the split by date's AUC, either F1 or either bill that Q8 asks for, the top 1,000's 404 buyers, or the word calibration outside Q21's stem | Each would answer a later or earlier item: Q8 derives the cost line, Q12 and Q13 test duration's timing, and Q2 judges the random split. The note and the timeline were the week's teaching, so they sit in the key and the guide; the proofs fail if 0.032, 1 in 31, F1's working or 0.657 appears on the paper |
| Real cases | Instacart (Fortune and Instacart's engineering blog) and Booking.com (KDD 2019), refetched by the first build; Zech and others (PLOS Medicine 2018), Stripe's fraud primer and Flipkart's BIRDNEST evaluation (arXiv 1511.06030), refetched by the raise. Each was taught in the week's own decks (Wednesday, Tuesday, Tuesday) | Decision `saturday-real-cases`: each figure on the paper is in a fetched source below. The week's other verified cases stay in the discussion guide or unused |
| The fraud anchor | "Precision or recall for fraud, and why?" is now Q22, the paper's one under-specified item, and the guide still answers it aloud | The raise's brief asked for one item whose best answer opens with a clarifying question; Rohan's question leaves out what a flag does and how many the team can review, which is the anchor's honest answer. The bank holds no fraud item, so Q22 is an addition; it prints no Build 2 figure, since the briefs ship when they lock |
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

## What did the raise change, and why?

The orchestrator's brief of 28 October 2026: at least 13 hard timed items inside the same 60 minutes,
made by turning single-judgement items into items that combine two of the week's ideas on an exhibit
or take several dependent steps, on the week's real numbers and verified cases; every bank concept
kept; easy items cut or folded rather than the paper lengthened; keys spread and never the longest;
one under-specified item whose best answer opens with a clarifying question. Every decision of the
first build stands unless a row below changes it.

| Change | Item now | Reason |
|---|---|---|
| The three word-bank blanks (banks 1 to 3) fold, and the three word banks go | Banks 1, 2 and 3 fold into Q3, Q6 and Q10 | They were the paper's three easy items, and each printed beside an item that used its word: the peek item said the slice was spent, the worked matrix put the false negatives under recall, and the duration item's reason is leakage |
| The peek item predicts the score of the best of 60 versions on fresh rows | Q3, hard | The old item named the misuse in its stem. The new one runs Monday's own loop (0.9055 peeked, 0.8971 fresh, from the D1 notebook): selection on a slice, the baseline as the anchor and the slice's new status, three ideas on Exhibit 1A |
| The score item asks what lets the memo read 0.71 as a chance | Q2, hard | Monday's probability reading joined to Friday's finding that a ranking can hold while the scores drift: the tempting reply cites the AUC, which vouches for the order only |
| The bill item becomes a worked item: F1 against the bill at 0.20 and 0.10 | Q8, hard | Two thresholds, two yardsticks, two disagreeing choices and the reason they disagree; worked, since a lettered version made the key the commonest part of every option. It leaves 0.5 to Q6, so no figure repeats |
| The budget item's options become nested plans | Q9, hard | The old key was the only option carrying a result (404 buyers). Now the 864 above 0.20 and the 268 above 0.5 sit inside the top 1,000, which the learner has to see; 404 prints nowhere |
| The importance and sign-flip items merge into one item on two conclusions | Q13, hard | Two of Wednesday's ideas on one exhibit, with the four options as the four combinations of the two verdicts, so no part marks the key; banks 7 and 15 fold into it |
| A shortcut item on Zech and others' pneumonia model | Q12, hard | Wednesday's verified case: leakage through a proxy against overfitting, read from 0.931, 0.815, 0.861 and the two pneumonia rates |
| The alarm item asks which way the cut on drifting scores moves | Q18, hard | Its two best options share the rule and differ in direction, so the learner has to reason from scores that run low to a cut that moves down |
| The evidence item asks for the trial's design | Q20, hard | Booking.com joined to Exhibit 5A's drift: a before-and-after measures the calendar, and a random trial scored on AUC measures the wrong thing |
| The lending item's options lose the nudge's 3 percent and a self-contradicting option | Q21, hard | The old option c printed Q7's answer as "a 3 percent chance"; option d now flips the direction, the slip a learner carrying the nudge's rule makes |
| A new under-specified fraud item | Q22, hard | The row's fraud anchor had no item. Rohan's question leaves out what a flag does and how many the team can review; two replies open on a question, and only one asks the question that decides it. Stripe and Flipkart were taught on Tuesday |
| Q16, the folds, relabelled medium | Q16 | One count of rows and one reading of the spread, so medium by the bar, whatever the first build labelled it |
| The workbook's demo counts Part 1's own size | `scripts/build_saturday_paper.py`, `demo_overconfident()` | The demo marks cover five items and expected two overconfident seats, which holds only when Part 1 has five items; the raised Part 1 has four. Weeks 1, 2 and 4 still compute seats 4 and 6, so their manifests do not change |
| Exhibit 5A's caption no longer says "instead of at random" | Exhibit 5A | The blind sitting read the caption as Q4's answer |

The minutes: 10 in Part 1, 15.5 in Part 2, 10.5 in Part 3, 10 in Part 4 and 12.5 in Part 5, 58.5 of 60.
The hard items carry 2.5 or 3 minutes, and the worked F1 item 3.5.

## What did the raise's blind sitting find, and what changed?

One fresh agent sat the raised student paper alone on 28 October 2026 and matched all 22 keys. It
graded 4 items hard (Q8, Q13, Q17, Q18) and 2 borderline (Q3, Q20). One fix pass followed; the proofs
and the audit passed after it.

| Finding | What changed |
|---|---|
| Q11's option d, an economic indicator for an unclosed quarter, was keyed a leak while the paper's honest model, its 0.795 and Q10's key all use the five indicators | Option d is now a callback flag an agent sets during this campaign, which fails the timing test without contradicting the honest columns. The first build carried the same conflict |
| Q2's key was the only option with an "if" | Option b now carries one too |
| Q3's 0.897 could not be worked out, and option b was defensible if the columns were noise | The stem says the versions use the customer table's columns, whose model Exhibit 1A puts at 0.897; option d is now 0.902, a halved edge, beside the key |
| Q12's exhibit stated the hospital shortcut outright | The row on a network naming the hospital is gone; the learner reads it from 0.861 and the two pneumonia rates |
| Q19's option c restated Q18's monitoring rule | It now reads "the reading that would retire the model, stated as a number before launch" |
| Q20's key sat where two options overlapped and was the only random design | The options now cross random or not with deposits or AUC |
| Q21's option d contradicted itself (its own 1 in 20 approves P) | It now flips the direction: Q clears the line, P does not |
| Q22's stem asked for the "best first reply", and its key was the only option that was not a metric | The stem asks which reply holds, and option b opens on a question that cannot decide it, how rare fraud is |
| Q4's answer read off Part 5's opener and Exhibit 5A's caption; Q4's key sits beside random-split scores elsewhere | The caption is changed; the random split running Monday to Thursday with its caveat said aloud is the week's design, so the guide's Q4 row says so |
| Q17: a paired gap of 0.011 on the same rows may be real, so option c is arguable | Kept: the key says another split could reorder the models and names the paired test on the same five folds, as the first build's fix pass settled |
| Q7 should accept 0.033 | It already does |
| Difficulty: most hard items solved by eliminating absurd options | The fixes above replace the giveaway options in Q3, Q11, Q20, Q21 and Q22; Q16 is relabelled medium. The count by the bar after the fix pass is 13; the sitting's own count, before the fixes, was 4 |

## Which data does the paper print, and where does each number come from?

| Number on the paper | Where | Source |
|---|---|---|
| 41,188 calls, 4,640 yes, 11.27 percent; May 2008 to November 2010; date order | Part 1's intro, Exhibit 1A | The UCI download's `bank-additional-names.txt`, "Number of Instances: 41188 for bank-additional-full.csv" and "ordered by date (from May 2008 to November 2010)", read 28 October 2026; the count of yes from the CSV in this session's re-run |
| The split 24,712, 8,238 and 8,238; 928 validation buyers; the do-nothing 0.887; the customer-table model's AUC 0.761, accuracy 0.897, TP 174, FP 94, FN 754, TN 7,216 | Exhibits 1A and 2A, Q6, Q7 | The pipeline file's model table, matched exactly by this session's re-run |
| The thresholds 0.20, 0.10 and the cost line (864, 2,754 and 7,438 called); the top 1,000's 404 buyers | Exhibit 2B, Q9, Q10's option c | The pipeline file's threshold table and budget line, matched exactly by the re-run |
| AUC 0.795 and 0.932, accuracy 0.899 and 0.907, 211 and 390 buyers | Exhibit 3A, Q12 | The pipeline file's model table, matched by the re-run |
| poutcome success, 65 percent yes; durations 553 and 221 seconds on average; euribor3m at -0.92 alone and +0.39 with the indicators, and its correlations of 0.97, 0.95 and 0.28 | Q13, Q14, Q15 and Q15's key | This session's re-run (provenance, re-run table); the pipeline file states the 65 percent and the sign flip in words |
| The tree by depth, the five folds, the three families, the split by date | Exhibits 4A, 4B and 5A, Q17, Q19, Q20, Q21 | This session's re-run (provenance, re-run table) |
| The peek loop: 60 versions scored on 2,000 held-out clients, the best at 0.9055 against 0.8875 for calling nobody there; 0.8971 on 6,238 fresh clients against 0.8873 | Q3 and its key | The executed outputs of Monday's notebook `content/W05/D1/1_in_class_training_content/notebooks/C2_W05_D01_case03_the_peek_STUDENT.ipynb`, which the proofs read back |

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
| A pneumonia model scored AUC 0.931 on held-out X-rays from its two hospital systems and 0.815 at a third; sorting by hospital alone scored 0.861; pneumonia ran at 34.2 percent in one system and 1.2 percent in the other; a network identified the hospital of 22,050 of 22,062 X-rays from one system | Exhibit 3B, Q12 and its key, the guide | https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1002683 (checked 28 October 2026) | Zech and others, PLOS Medicine 2018: "The highest internal performance was achieved by combining training and test data from MSH and NIH (AUC 0.931, 95% CI 0.927 to 0.936), but this model demonstrated significantly lower external performance at IU (AUC 0.815, 95% CI 0.745 to 0.885, P = 0.001)"; "The prevalence of pneumonia was high enough at MSH (34.2%) relative to NIH and IU (1.2% and 1.0%) that merely sorting by hospital system achieved an AUC of 0.861"; "CNNs were able to directly detect hospital system of a radiograph for 99.95% NIH (22,050/22,062)". The paper's ranges are written here with the word to |
| Stripe's worked example: profit per sale 2.08 dollars, a fraudulent sale loses 38.92 dollars, one fraud costs the profit of 18.71 good sales, break-even precision 5.07 percent; 33 percent of consumers in a survey Stripe cites would not shop again after a false decline | Exhibit 5C, Q22 and its key | https://stripe.com/guides/primer-on-machine-learning-for-fraud-protection (checked 28 October 2026) | "your profit per sale is $26.00 × 8.00% = $2.08"; "your total loss for a fraudulent sale is $23.92 + $15.00 = $38.92"; "one fraudulent sale costs you the profit of $38.92 / $2.08 = 18.71 legitimate sales, and your break-even precision is 1 / (1 + 18.71) = 5.07%"; "in a recent survey, 33% of consumers said they wouldn't shop again at a business after a false decline" |
| Flipkart investigated the 250 accounts BIRDNEST ranked most suspicious, and 211 were involved in fraud | Exhibit 5C, Q22 and its key | https://arxiv.org/abs/1511.06030, the PDF read (checked 28 October 2026) | Hooi and others: the authors "provided them to Flipkart; these accounts were investigated and hand-labelled by Flipkart, finding that 211 users of the top 250 flagged by BIRDNEST were involved in fraud" |
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

## What did the blind sitting of the raised paper change?

A fresh reader sat the raised paper on 28 October 2026 with no key, guide or trainer file open, and
matched the key on all 22 items. These changes came from what it found.

| Item | What changed | Why |
|---|---|---|
| Q17 | Option b and the key now carry Thursday's two tests: a lead must hold fold by fold and pay its upkeep in rupees | The old reason set a gap between two models against one model's fold spread, while Thursday's case03 showed boosting leading on all five paired folds; the paper now teaches what Thursday taught |
| Q16 | The interview line compares two models fold by fold on the same folds | Same reason as Q17 |
| Q12 | Exhibit 3B no longer prints the 0.861 from sorting by hospital alone; the key and guide still quote it from the paper | The row stated the key, so a hard item was answerable from one line; the pneumonia rates, 34.2 and 1.2 percent, now carry the inference |
| Q20 | Option c is a before-and-after scored on AUC, so the four options cross before-and-after or random with deposits or AUC | The key was the one option sharing a feature with every other, which a test-wise reader finds without the content |
| Q21 | Option d carries the nudge's 3 percent line over to lending, which rejects both applicants | The old d approved the riskier applicant only and named the same 5 percent line as the key, which a test-wise reader rules out unread |
| Q18 | The stem cites Exhibit 5B beside 5A | Instacart's rows back the key, and no item cited them |
| Part 4 intro | Names the honest columns as the ones Wednesday's audit kept, without listing them | The list answered Q11a two parts early |

Kept as they are: Q15 option d, a brake chosen by cross-validation, which the key counts as a brake;
Q7, whose direction Exhibit 2B hints at while the marked number still needs the working; Q19, which
rests on Friday's memo lines as the class drew them. The level counts stay at 9 medium and 13 hard.
