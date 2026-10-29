# W06 Build 2, project session: sources, measurements and decisions

INTERNAL. Built 29 October 2026 on branch `w06-project`, Python 3.13, pandas 3.0.5, numpy 2.5.3,
scikit-learn 1.9.1, matplotlib 3.11.2, xlrd 2.0.2 (installed in the session with pip, since reading
the `.xls` file needs it). The files of this session:

| File | What it does |
|---|---|
| `1_project/C2_W06_D02_ticket_STUDENT.md` and `.pdf` | Rohan's ask, the decision and the two error costs, the finished-answer sentence, the hand-in days, the AI lanes; on side two the discovery call, the card box and the eight-stage strip. Two printed sides, about 620 words. |
| `1_project/C2_W06_D02_workbook_STUDENT.md` and `.pdf` | A cover with the page map and the roles by stage, one page per stage 0 to 7, the numbers passport, the run sheet, the challenges log and the AI log. Thirteen printed pages. |
| `4_trainer_only/C2_W06_D02_constraint_cards_TRAINER.md` | Eight cards, one page each, top half handed over on Tuesday, the twist and its numbers below a cut line. |
| `4_trainer_only/C2_W06_D02_discovery_call_script_TRAINER.md` | Rohan for the three role-players: voice, the eight minutes, the answer sheet by question kind, what he does not know, what he never volunteers, the restate-back, the hand-over lines, the tally. |
| `4_trainer_only/C2_W06_D02_reference_build_TRAINER.ipynb` | The executed solution and the breadcrumb notebook's solution twin: 72 cells, 10 rendered pictures, 54 checks passing, every card and twist against the research. |
| `4_trainer_only/C2_W06_D02_gate_and_viva_TRAINER.md` | Thursday's fifteen minutes: the three gate questions with pass and not-yet lines, the viva prompts by stage with their follow-ups, the passport draws, the twist hand-over. |

## Dataset

| Dataset | URL | Licence, as the page states it | Checked | Used in |
|---|---|---|---|---|
| UCI Default of Credit Card Clients, `default of credit card clients.xls` inside the zip | page https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients; file https://archive.ics.uci.edu/static/public/350/default+of+credit+card+clients.zip (verified 29 October 2026; HTTP 200, 5,539,494 bytes) | "This dataset is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) license." Citation as the page asks: Yeh, I. (2009). Default of Credit Card Clients [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C55S3H (verified 29 October 2026) | 29 October 2026 | every file |

The variable definitions Rohan reads aloud in the discovery script were read on the UCI page in this
session (verified 29 October 2026): status "-1 = pay duly; 1 = payment delay for one month; 2 =
payment delay for two months; . . .; 9 = payment delay for nine months and above"; education "1 =
graduate school; 2 = university; 3 = high school; 4 = others"; marital status "1 = married; 2 =
single; 3 = others"; X6, X12 and X18 are September 2005 and X11, X17 and X23 are April 2005; the page
lists "Has Missing Values?" as "No".

## Numbers measured in this build

Every research script in `docs/detailing/W06_research/scripts/` was rerun in this session on the
same file, one after another, and every number of `W06_datasets.md` section 3(c) reproduced. The
reference build recomputes all of them and checks each one.

| Number | Value | Where |
|---|---|---|
| Rows, defaults, base rate | 30,000; 6,636; 0.2212 | reference build section 1 |
| Hurried read (default header) | 30,001 rows, text columns | section 1 |
| Codes outside the dictionary | September -2 and 0: 17,496 (58.3 percent); education 0, 5, 6: 345; marital 0: 54 | section 1 |
| Code 1 by month, September to April | 3,688, 28, 4, 2, 0, 0 | section 1 |
| Accounts owing and paying nothing for six months | 795, of which 299 labelled default (37.6 percent) | section 1 |
| Repeats | 35 exact; 108 rows share inputs; 21 groups conflict | section 1 |
| September bills below zero, above the limit | 590; 2,115 | section 1 |
| Split | 21,000 train and 9,000 test, stratified, seed 42; validation 5,250 of the train, seed 42 | section 3 |
| Rule A as a flag | status 1 or worse: precision 0.499, recall 0.503, bill 661; status 2 or worse: 0.690, 0.324 | sections 3 and 4 |
| AUC on seed 42 | logistic with codes as numbers 0.7150; as categories 0.7629; gradient boosting 0.7789 | section 3 |
| Bills per 1,000 at 5 to 1 | nobody 1,106; everyone 779; threshold 0.5 762; theory 1/6 566; tuned 0.160 568 (44.5 percent called) | section 4 |
| Five splits | gradient boosting AUC mean 0.7779, range 0.7749 to 0.7819 | section 4 |
| Accuracy | predict no default 0.7788; model at 0.5 0.8182 | section 4 |
| Card 1 twist | 20 to 1: threshold 0.048, 97.7 percent called, bill 765 against 779 (1.8 percent) | section 7 |
| Card 2 | five-split means: 1,000 calls 687 against 666; 2,000 calls 1,079 against 1,009.8; seed 42 at 1,000: 676 against 674 | section 7 |
| Card 3 | chance alone: 676 defaulters, 42.7M of 100.1M NT dollars (42.7 percent); chance x balance: 469, 62.9M (62.8 percent) | section 7 |
| Card 4 | five-split: logistic with categories 0.7649, boosting 0.7779, logistic with numbers 0.7166 | section 7 |
| Card 5 | five-split AUC 0.7779 to 0.7769; seed-42 top 1,000: men 11.5 to 11.3 percent, women 10.9 to 11.0, defaulters 676 to 675; true rates men 23.9, women 21.0 | section 7 |
| Card 6 | five-split AUC 0.747; top 1,000 model 614 against the August rule 563; seed 42 with two months of lag: AUC 0.7295, 564 | section 7 |
| Card 7 | stand-in status 1 or worse: AUC 0.7472, 539; status 2 or worse: 0.6517, 652; true label 0.7790, 680 | section 7 |
| Card 8 | base rate 0.2212, relabelled 0.2112, removed 0.2170; the 299 are 4.5 percent of defaults; call-nobody bill 1,106 to 1,056 | section 7 |
| Repeats dropped | 29,965 rows, test 8,990, AUC 0.7794 against 0.7789 | section 7 |
| Scoring time | the 9,000-row test book in 0.02 seconds | section 5 |

## References and company facts

Every real fact in the STUDENT and TRAINER files is taken from `docs/detailing/W06_research/W06_references.md`
or `W06_pedagogy.md`, where the research session verified it on 29 October 2026; none was refetched
here except the UCI page above.

| Fact as used | Where it is used | Source |
|---|---|---|
| In a demo the problem is framed already; a real project must find it and agree the goal | workbook stage 0 | Ketan Doshi, https://ketanhdoshi.github.io/Enterprise-ML/ (verified 29 October 2026 by the research session); link and paraphrase only |
| The model is "only the tip of the iceberg"; production can take up to 90 percent of the time and effort, his own estimate | workbook stage 6 | Ketan Doshi, https://ketanhdoshi.github.io/Enterprise-ML-Prod/ (verified 29 October 2026 by the research session) |
| Retention offer: 95.3 percent churn in control and 93.7 percent treated in the highest-risk decile | workbook stage 1 | Ascarza (2018), https://www.hbs.edu/ris/Publication%20Files/ascarza_jmr_18_783d54d4-e548-41ed-b1d7-8a180f1ae85a.pdf (verified 29 October 2026 by the research session) |
| Apple Card: limit 20 times his wife's, an agent could not explain, nearly 400,000 applicants checked, no violation, ordinary factors explained | workbook stage 2; card 5 | NYDFS report, March 2021, https://www.dfs.ny.gov/system/files/documents/2021/03/rpt_202103_apple_card_investigation.pdf (verified 29 October 2026 by the research session) |
| Upstart against a traditional model over 22 months; 27 percent more approved, 16 percent lower APRs, reported by Upstart, not replicated | workbook stage 3 | CFPB, 6 August 2019, https://www.consumerfinance.gov/archive/blog/update-credit-access-and-no-action-letter/ (verified 29 October 2026 by the research session) |
| German credit cost matrix: bad as good 5, good as bad 1 | workbook stage 4; card 1 | UCI Statlog German Credit, https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data (verified 29 October 2026 by the research session) |
| Stripe Radar decides in under 100 milliseconds | workbook stage 5 | https://stripe.dev/blog/how-we-built-it-stripe-radar (verified 29 October 2026 by the research session) |
| SR 26-2 of 17 April 2026 keeps effective challenge | workbook stage 7 | https://www.federalreserve.gov/supervisionreg/srletters/sr2602.htm (verified 29 October 2026 by the research session) |
| RBI circular of 6 March 2007: "convey in writing the main reason / reasons", "including credit card applications" | card 4 | https://www.rbi.org.in/scripts/NotificationUser.aspx?Id=3315 (verified 29 October 2026 by the research session); whether a 2025 master direction for banks restates it is not verified and is not claimed |
| Datasheets for Datasets | card 8 | Gebru and colleagues, https://arxiv.org/abs/1803.09010 (verified 29 October 2026 by the research session) |
| Elicitation interview mistakes: question formulation, omission and order | discovery script | Bano, Zowghi, Ferrari and colleagues (2019), https://par.nsf.gov/biblio/10105611-teaching-requirements-elicitation-interviews-empirical-study-learning-from-mistakes (verified 29 October 2026 by the research session) |
| Rohan priced Week 5's loans at twenty to one | discovery script | `content/W05/` files (Rs 60,000 per false approval against Rs 3,000 per wrongful rejection) |

## Decisions taken in this session, and why

1. **The main line keeps all 30,000 rows.** The 35 exact repeats stay in so the test book is the
   9,000 that card 2 names and every number matches the research; the reference build measures the
   other choice (AUC 0.7794 against 0.7789).
2. **The do-nothing bill is calling nobody,** as the passport field says, and stage 4 asks the group
   to beat both simple lists, since at 5 to 1 calling everyone (779) already beats calling nobody
   (1,106) and a group that compares only with calling nobody overstates its gain.
3. **One invented gym runs through every workbook page** (1,000 members, 15 in 100 lapse, 1 unit
   against 4), on a different ratio from Kalpa's 5 and from Week 5's gym (1 against 30), so the
   method shows and the group's answer does not. Its numbers reconcile: 300 test members, 45 lapses,
   80 calls, 30 caught, 50 wasted, 15 missed, 110 units, 367 per 1,000 against 600 and 850.
4. **The workbook's audit questions are generic** (different rows, values in the dictionary, a
   group's rate far from the rest, inputs known in time, test opened once), answered for the gym with
   a trap of its own (booked classes counted as visits). No STUDENT file names the header row, the
   undocumented codes, the accounts owing nothing or the repeats.
5. **Card 6's twist goes one month further** for a group that already dropped September on Tuesday
   (seed 42: AUC 0.7295, 564), since the twist in `common.md` restates Tuesday's rule for such a group.
6. **Rohan's answer on capacity for groups without card 2** is "tell me how many calls your list
   needs", so the list size is an output of the threshold for eleven groups.
7. **Rohan does not know** any value outside the UCI page, and says so to every group; only card 8
   gets the data team's ruling, as its twist.
8. **The reference build is self-contained** (matplotlib and a local `check()`, no `scripts/c2kit.py`),
   so a trainer can copy it into a group's repository and run it. Its `score()` gives the main reason
   by setting one input at a time to the training median and keeping the input whose change lowers
   the chance most, which works for any model and answers card 4 for a boosted model.
9. **No builder script and no cards PDF are committed,** since the brief assigns only the seven files.
   The notebook rebuilds with `jupyter nbconvert --to notebook --execute --inplace` on itself (about
   25 seconds); the cards print with the `build_doc.py` line at the top of the cards file.
10. **The ticket's title is "Whom do we call before the due date?"** so that side one fits one page;
    the day's full question stays in Rohan's quote.
11. **Card 3's balances are written in words** ("42.7 million of 100.1 million NT dollars"), since
    pandoc read the `$` signs as mathematics and dropped the spaces in the PDF.
12. **mermaid-cli needed the browser path** in this session: `PUPPETEER_EXECUTABLE_PATH=/opt/pw-browsers/chromium`,
    because `scripts/build_cheatsheet.py` looks for `chrome-linux/` and this machine has
    `chrome-linux64/`. The shared script was left unchanged.

## Skills used

| Skill | What was taken |
|---|---|
| exercise-builder | Sizing the gate's fifteen minutes to three questions and two prompts per member; a "not yet" with the one thing to fix; the plausible wrong answer as each card's trap |
| scaffold-exercises | The same five-part anatomy on every stage page, so the ladder reads as one structure |
| study-notes-builder | The reading budget and one running thread (the gym) carried through every stage page |
| notebook-builder | MAP, DO, SEE, CHECK, SUM in the reference build: a ladder map per section, predict-then-run cells, a trap per stage (the hurried read, codes as numbers, threshold 0.5, accuracy), checks on shape, a closing summary |
| humanizer and llm-tic-scrubber | A read of every prose file and the notebook's markdown; `tic_scan.py` reports all six clean |

## What another session must match

- The split: stratified 70/30 on all 30,000 rows with `random_state=42` (9,000 test), validation 25
  percent of the train with `random_state=42`; gradient boosting is
  `HistGradientBoostingClassifier(random_state=0, max_iter=300, learning_rate=0.05)`.
- Cost units: a wasted call 1, a missed default 5; card 1's twist 20.
- The two honesty lines, word for word: "The Taiwan score proves the pipeline and is never Kalpa's
  score." and "This data allows no out-of-time split, so the MVP must add one."
- The workbook's page numbers: stage n is page n + 1, and the run sheet and passport follow page 8.
- The score function's contract on the run sheet and in the workbook: one cardholder in; chance, call
  or not, main reason and cost out.
- The gym's numbers if the explorer or the starter repository shows a gym: 1,000 members, 15 in 100,
  1 unit against 4, threshold 0.2.
