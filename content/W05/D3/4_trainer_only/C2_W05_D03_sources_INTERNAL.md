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

## The explorer, rebuilt on the Week 5 kit (29 October 2026)

Rebuilt in place as the day companion of decision `w5-explorer-companion`, on branch `w05-d3-explorer`, with the Week 5 kit (`scripts/companion/w5kit.js` and `w5kit.css`, inlined by `scripts/build_companion.py`) and the briefs `docs/detailing/W05_briefs/explorers/common.md` and `D3.md`. Eleven routes: `#story`, `#map`, `#p1` to `#p5`, `#case` (five tabs), `#field` (four scenes and the six seats), `#interview` (five situations) and `#check` (eight checks).

### Data

| Number on the page | Where it comes from |
|---|---|
| The 8,238 validation outcomes and the three score sets the story ranks and case chapter 6 draws | `C2_W05_D03_explorer_data_INTERNAL.py`, which reruns the week's pipeline and today's scorer from case01 and writes `C2_W05_D03_explorer_data_INTERNAL.json`, 96 KB; scores travel as integers out of 1,000 |
| 0.7613, 0.7946, 0.9324; 0.8971, 0.8986, 0.9074; 0.188, 0.227, 0.420; Rs 279,000, Rs 280,040, Rs 118,800; 404, 460, 572 | the same script, which stops unless each equals case01's output |
| The AUC, bill and top-1,000 buyers of every keep, fix or drop combination on case chapter 7's eight cards (384 refits on the training rows) | the same script; it stops unless the audited set gives 0.7955, Rs 281,680 and 462, the leaked set 0.9327 and Rs 118,520, and raw pdays 0.7951, as case02 prints |
| Call-length fifths 0.005 to 0.330, the four calls of 0 seconds, poutcome's three rates, pdays at 999 in 96.32 percent, the calendar's 0.7854, the yes-rate by month and year, euribor3m by month, the nine within-month AUCs and their weighted 0.568 | the same script, checked against case02 |
| euribor3m at -0.917, +0.144, +0.766, +0.358; the correlations 0.972, 0.944, 0.905; permutation importance 0.3435 down; the group shuffle 0.140; the lift 0.295 | the same script, checked against case03 |
| The eight members of `#p1`, the six of `#p2`, the twelve of `#p3` and the twelve of `#p5` | typed exactly as notebooks ch01, ch02, ch03 and ch05 type them; `#p3` adds one invented column, coupon_redeemed, written on day +3, labelled on the stage |
| The nine candidate columns of `#p4` | notebook ch04's table, with its owners, write days and reasons |
| The thirty invented members `#p4` votes over | found once by a seeded search (seed 3646) so the audited stamps score 23 of 30 on both tables, the junior's unstamped set 29 on the table and 20 on the nudge morning, today's loyalty tier 25 on the table and 23 on the morning, and a kept member_id 20 on both; embedded as a literal |
| Zech, Kaggle IJCNN 2011, Airbnb, Uber Michelangelo | `docs/detailing/W05_research/W05_cases.md`, each verified 28 October 2026, with the link and date on the page; Airbnb's 400 nightly prices and Uber's nine orders are invented for the picture and labelled invented |

### Decisions

1. **The bank's twenty columns are stamped on case chapter 7, and `#p4` stamps chapter 4's nine invented columns.** D3.md puts the bank's columns on `#p4`, which chapter 4 opens before case 2; stamping `duration` there would name the leak the room finds at S38 and S39. `#p4` keeps chapter 4's table and the as-of trap, and case chapter 7 carries the bank's stamps, with the AUC, the bill and the top 1,000 refitted for every combination.
2. **euribor3m's sign flip sits on case chapter 8, and `#p5` teaches twins on chapter 5's invented members.** The deck's own decision keeps euribor3m unnamed before case 3 (S48 calls it the row's second discovery), so `#p5` shuffles the invented visits and searches, adds random shuffles averaged as scikit-learn averages repeats, and draws the lever question.
3. **Zech's control is the test site.** The paper reports 0.931 on the home systems' test images, 0.815 at Indiana and 0.861 for a ranking by hospital prevalence alone; it reports no model with the hospital signal removed, so the toggle switches the test images between home and Indiana instead of switching a hospital feature off.
4. **The story ranks the bank's calls in columns by score.** Each feature set's ranking piles the 928 buyers further right; Kalpa's 0.99 is told in the caption and the readout, with no rows drawn, since Kalpa's version 6 data was never generated.
5. **An unstamped card on case chapter 7 counts as the junior's join:** kept, with pdays left out as case01 left it out, so the unstamped board reads 0.932 and Rs 1.19 lakh exactly.
6. **Answers stay hidden until the reveal.** Every readout, bar or label that states a prediction's answer shows a question mark or a dashed empty bar until the learner commits or reveals; the importance chart on case chapter 8 also hides its column names and colours.
7. **Every readout ends on its hero number.** The kit spans a lone last card across the row, so each readout lists an even number of small cards before the hero.
8. **Cut from the old page:** the thirty-member combined rule and its "add a green feature" click; adding features now happens on `#p1` and on case chapter 6, where the real jump is measured.
9. **The deck's S21** now pictures `#p3` at the nudge morning, cropped at 192 dpi so its smallest label prints at about 14 points, and its notes walk the new clicks. The deck was rebuilt with this folder's `C2_W05_D03_build_deck_INTERNAL.py`; the shared builder no longer places the logo, so the strip removed nothing.
10. **The README run table and the trainer guide** name the page each chapter opens, and the trainer guide's section 11 lists every page with its clicks and what the room should see.

### Kit gaps, worked around on the page

- A toggle has no setter, so the `#p5` player clicks the toggle's button to move it.
- The readout spans only a lone last card, so an odd count before a full-width hero leaves a hole; every readout here orders its cards to avoid it.
- The concept map's panel joins node labels into sentences ("Feeds The feature store"), so the later nodes are named without a leading "The".
- A chart or drawing built inside a hidden tab is built when the tab first gives it a width (the page's `lazy` helper), so the case tabs log no errors at load.
- `W5.tween` can pass a slightly negative progress on its first frame, when the animation frame's timestamp precedes its start time; a bar drawn from it took a negative height and logged a console error in one sweep of three, so every player render here clamps its progress at zero.
- `explorer_shots.py` shoots only a route's first tab; the case, field and interview tabs were shot with a short Playwright script, before and after every reveal.
- `find_chromium()` in `html_sweep.py` searches `chrome-linux/`, and this container keeps Chromium at `/opt/pw-browsers/chromium-1243/chrome-linux64/chrome`; `deck_check.py` names `chromium-1194`. Both were linked into the expected paths outside the repository for this session.

### Proof

- `python3 content/W05/D3/4_trainer_only/C2_W05_D03_explorer_data_INTERNAL.py`: 25 checks pass against case01 to case03, 384 refits, about 190 seconds.
- `python3 scripts/html_sweep.py` walks all eleven routes with no inert control and no console error.
- `python3 scripts/explorer_shots.py --end` at 1366 and 390 wide, plus every tab of `#case`, `#field` and `#interview` before and after its reveals; every picture was looked at, and the overlaps, clipped labels and small type it found were fixed.
