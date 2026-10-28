# W05/D3 sources, licences and decisions

INTERNAL. Built 28 October 2026 in one cloud session on branch `w05-d3`. Python 3.13, pandas
3.0.5, scikit-learn 1.9.1, matplotlib 3.11.2. Every number in the pack comes from the executed
notebooks or from `C2_W05_D03_make_figures_INTERNAL.py`, which reuse the week's pipeline in
`docs/detailing/W05_research/W05_week_pipeline.md`.

## Datasets

| Dataset | Where it is used | URL | Licence | Checked |
|---|---|---|---|---|
| UCI Bank Marketing, `bank-additional-full.csv`, 41,188 rows | ch01, ch02, case01 to case03, guided, figures | https://archive.ics.uci.edu/dataset/222/bank+marketing (verified 28 October 2026); download https://archive.ics.uci.edu/static/public/222/bank+marketing.zip (verified 28 October 2026) | CC BY 4.0 (page text), DOI 10.24432/C5K306; citation Moro, Cortez and Rita, Decision Support Systems, 2014 | 28 Oct 2026 |
| German Credit (Statlog), OpenML `credit-g`, 1,000 rows | practice lab and its solutions | https://www.openml.org/api/v1/json/data/31 (verified 28 October 2026) | OpenML "Public"; UCI copy CC BY 4.0 per `W05_datasets.md` | 28 Oct 2026 |
| Invented Kalpa tables (8, 6, 12, 9, 12 and 30 members) | ch01 to ch05, the explorable, practice set problems 1, 2, 3, 7 | typed in cells and pages, labelled invented | ours | 28 Oct 2026 |

## Numbers measured in this session (validation slice 8,238 calls, seed 42)

| Quantity | Value | Where |
|---|---|---|
| AUC: customer table, + economy, + economy + duration | 0.7613, 0.7946, 0.9324 | case01 (matches the week pipeline) |
| Accuracy at 0.5 for the same three | 0.8971, 0.8986, 0.9074 | case01 |
| Recall at 0.5 | 0.188, 0.227, 0.420 | case01 |
| Bill at 40 / 1,240 = 0.032 | Rs 2,79,000; Rs 2,80,040; Rs 1,18,800 | case01 |
| Honest audited set (20 columns) | AUC 0.7955, recall 0.231, bill Rs 2,81,680, 462 buyers in the top 1,000 | case02 |
| Leaked set with engineered pdays | AUC 0.9327, bill Rs 1,18,520 | case02 |
| Year and month alone | AUC 0.7854 (the pipeline note's correction 1 says 0.795 by another method; this pack quotes its own run) | case02 |
| Inside one month, weighted over months with 100 or more validation calls | AUC 0.568 | case02 |
| duration fifths, yes-rate | 0.005, 0.032, 0.073, 0.125, 0.330; four 0-second calls all no | case02 |
| poutcome yes-rate | success 0.651, failure 0.142, nonexistent 0.088 | case02 |
| euribor3m coefficient | alone -0.917; with nr.employed +0.144; with both partners +0.766; honest model +0.358 | case03 |
| Permutation importance | emp.var.rate 0.344, cons.price.idx 0.059, contact 0.028; economy group shuffled together 0.140; model lift 0.295 | case03 |
| German Credit | AUC 0.8043; with monthly_burden 0.8055; scrambled target 0.424; checking_status bad rate 0.493, 0.390, 0.222, 0.117 | practice lab |

## References and case facts

| Fact used | Source | Checked |
|---|---|---|
| The `duration` note (quoted in the trainer guide, paraphrased elsewhere) | https://archive.ics.uci.edu/dataset/222/bank+marketing (verified 28 October 2026) | 28 Oct 2026 |
| Zech and others: internal AUC 0.931, external 0.815, 99.95 percent hospital detection, metal token, 41.1 against 32.8 percent prevalence, prevalence-only AUC 0.861 | https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1002683 (verified 28 October 2026), facts from `W05_cases.md` | 28 Oct 2026 |
| Kaggle IJCNN 2011: test set de-anonymised from a Flickr crawl, AUC 0.981 | https://arxiv.org/abs/1102.4374 (verified 28 October 2026), facts from `W05_cases.md` | 28 Oct 2026 |
| Airbnb: unnormalised features stalled the first network; the two normalisation formulas; the monthly price bug for stays over 28 days | https://arxiv.org/abs/1810.09591 (verified 28 October 2026), facts from `W05_cases.md` | 28 Oct 2026 |
| Uber Michelangelo: "the same expressions are applied at training time and at prediction time" | https://www.uber.com/blog/michelangelo-machine-learning-platform/ (verified 28 October 2026; the phrase was found in the fetched page) | 28 Oct 2026 |
| scikit-learn, Common pitfalls: "Data leakage occurs when information that would not be available at prediction time..." | https://scikit-learn.org/stable/common_pitfalls.html (verified 28 October 2026) | 28 Oct 2026 |
| scikit-learn, Permutation importance, with its note on strongly correlated features | https://scikit-learn.org/stable/modules/permutation_importance.html (verified 28 October 2026) | 28 Oct 2026 |
| scikit-learn, Permutation importance with multicollinear features (example) | https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance_multicollinear.html (verified 28 October 2026) | 28 Oct 2026 |
| scikit-learn, Preprocessing data | https://scikit-learn.org/stable/modules/preprocessing.html (verified 28 October 2026) | 28 Oct 2026 |
| Kaggle Learn, Data Leakage notebook | https://www.kaggle.com/code/alexisbcook/data-leakage (verified 28 October 2026) | 28 Oct 2026 |
| Google MLCC, One-hot encoding | https://developers.google.com/machine-learning/crash-course/categorical-data/one-hot-encoding (verified 28 October 2026) | 28 Oct 2026 |
| Google MLCC, Normalization | https://developers.google.com/machine-learning/crash-course/numerical-data/normalization (verified 28 October 2026) | 28 Oct 2026 |

## Videos (titles and channels confirmed through YouTube's oEmbed endpoint)

| Topic | Video | URL |
|---|---|---|
| Feature engineering | CampusX, What is Feature Engineering, Day 23, 100 Days of Machine Learning | https://www.youtube.com/watch?v=sluoVhT0ehg (verified 28 October 2026) |
| Encoding | StatQuest, One-Hot, Label, Target and K-Fold Target Encoding, Clearly Explained | https://www.youtube.com/watch?v=589nCGeWG1w (verified 28 October 2026) |
| Scaling | Normalized Nerd, Standardization vs Normalization Clearly Explained | https://www.youtube.com/watch?v=sxEqtjLC0aM (verified 28 October 2026) |
| Leakage | Krish Naik, What is Data Leakage In Machine Learning? | https://www.youtube.com/watch?v=n9jz7G68pVg (verified 28 October 2026) |
| Importance | A Data Odyssey, Permutation Feature Importance from Scratch | https://www.youtube.com/watch?v=U-iahfXlSoY (verified 28 October 2026) |

Not verified: whether each quarterly and monthly economic indicator in the bank's file was
published before the calls it sits beside; the pack says so and stamps the columns "ask the owner".

## Images

Every PNG in `1_in_class_training_content/slides/img/` is drawn by `C2_W05_D03_make_figures_INTERNAL.py`
from the public data or the invented tables; every chart in a notebook is drawn by its own code
cell. Mermaid diagrams are rendered by the shared theme. No image from elsewhere and no logo is
used.

## Decisions taken in the session

| Decision | Reason |
|---|---|
| The deck is built with `scripts/build_deck.py` and then stripped of the institute's logo and two name lines by `C2_W05_D03_build_deck_INTERNAL.py` (195 shapes removed) | the shared builder places the logo on every slide; Week 5 forbids logos; changing the shared builder from a day branch would collide with four parallel day builds |
| The `duration` quote sits in the trainer guide with one bracketed capital, `[T]hus` | the brief asks for the verbatim quote in a TRAINER file, and `scripts/verify.py` fails the word in every file |
| The calendar and economy columns are kept and flagged, never dropped | they pass the prediction-time question; Thursday's numbers rest on the 20-column set; Friday's split by time prices the caveat |
| The honest set includes `never_contacted` and `days_since_contact` (20 columns, AUC 0.7955) | correction 6 of the week pipeline |
| Chapter 5 teaches twins on invented data and never names `euribor3m`; the Wednesday state of the week's picture first appears at S47, after case 2; the deck opens on Tuesday's state | nothing the room finds is named before the step where it is found |
| The guided notebook runs between case 1 and case 2 | the room calls `duration` "not known" itself before the full audit |
| The run: block one 180 minutes (concept block 90), block two 60 trainer minutes, then the faculty block (tentative) | the week plan's 240 trainer minutes and the facts file's two 180-minute blocks |
| The two mid-session drills are deck slides (S15 and S16, S27 and S28); the unguided task is a blank-notebook task in S53's notes | the artifact set has no exercise folder |
| The explorable's 30 invented members come from a seeded search (seed 17) run once in the session and embedded as a literal; it lands on 30, 22 and 24 of 30 | the explorable design asks for about 22 of 30 after the marker moves and a rise of one or two points after a feature is added |
| The practice lab uses German Credit, with the two collections columns described and never created | the lending transfer from Tuesday; no synthetic data |
| Practice set and interview bank use invented Kalpa numbers labelled invented, real-company facts only from `W05_cases.md` and pages fetched today | the brief's rule on real-company facts |
| Mermaid-cli needs `PUPPETEER_EXECUTABLE_PATH=/opt/pw-browsers/chromium` in this session | the shared helper searches `chromium-*/chrome-linux/chrome`, and this machine holds `chrome-linux64` |
| The deck carries 64 slides plus the cover | the brief's 45 to 65 |

## Skills read and what was taken

training-deck-builder and pptx (slide order, one exhibit per slide, the render check through
LibreOffice), notebook-builder (predict, run, what happened, checks, the trap, rules with flips),
exercise-builder (keys never the longest, keys spread, distractors from real misconceptions),
study-notes-builder and fde-cheat-sheets (picture first per chapter, the cumulative line list),
companion-builder and design-taste-frontend (one question, two controls, a wrong default, the
prediction lock, no hover-only state), concept-packaging (the cold open on the 0.99, paired rules),
humanizer and llm-tic-scrubber (the style sweep before commit).
