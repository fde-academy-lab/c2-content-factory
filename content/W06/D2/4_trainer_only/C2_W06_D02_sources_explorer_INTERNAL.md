# Week 6 explorer: sources, numbers and decisions

INTERNAL. The explorer is `3_explorer/C2_W06_D02_explorer_STUDENT.html`, built on the Week 5 kit and
inlined by `python3 scripts/build_companion.py`. Its real numbers come from
`4_trainer_only/C2_W06_D02_explorer_data_INTERNAL.py`, which writes the JSON beside it and stops on
any number that differs from its source. Built 29 October 2026.

## What each route draws, and from where

| Route | What the learner does | Numbers and their source |
|---|---|---|
| `#story` | Plays Rohan's ask in six scenes on a storyline rail (no card history, the public book, the one action, the two costs, the question, POC first) and predicts how many in 100 defaulted before 22 appears | 30,000 cardholders and 6,636 October defaults (22.1 percent), counted by the data script from the UCI file; the six months and the 1 to 5 cost units from `docs/detailing/W06_briefs/common.md` |
| `#map` | Plays the eight ladder stages as a path, linked back to Week 3 and Week 5 Monday to Friday and forward to Week 9, Week 14 Friday and Week 16 | Week titles from `docs/curriculum/W5_ML_core_ME1.md`, `W9_Build_3.md`, `W14_Agents_in_production.md`, `W16_ME3_FDE_design_to_deploy.md` |
| `#p1` | Opens a black box into the money flow and the frame, then slides the day the list is built across a month's timeline | Invented phone operator, typed in the page |
| `#p2` | Lights the pipeline boxes each kind of requirement changes, sorts twelve requirements into six kinds, reads the Apple Card callout | Invented requirements; Apple Card facts from `W06_references.md` 3.1 |
| `#p3` | Compares a complaints rule with a model score at a capacity slider, and fills the A against B sheet row by row | Forty invented customers typed in the page; Google's Rules of ML rule 1 from `W06_references.md` section 2 |
| `#p4` | Prices the two free lists, drags the threshold, watches the four boxes and the bill, caps the list at six calls, and switches to customers the model learned from | The same forty invented customers, plus forty invented training customers; at 4 to 1 the cheapest cut is 0.21 with a bill of 15 against 30 and 40 |
| `#p5` | Opens the black box into seven boxes on two paths, lights the training and serving paths apart, zooms one box into its LLD | Invented; function names follow the starter brief (`make_features`, `fit`, `error_bill`, `score`) |
| `#p6` | Switches POC, MVP and production on the iceberg, sorts six promises, reads what changes when Kalpa's data arrives | Ketan Doshi's "up to 90 percent" as his own estimate, and Google Cloud's MLOps levels, from `W06_references.md` sections 1 and 2 |
| `#p7` | Plays the twelve-minute run sheet, builds the answer-first sentence part by part, reads an invented passport | Run sheet from `common.md`; sentence and passport on the invented operator (20 calls, bill 15) |
| `#case` | Walks stages 0 to 7 on Week 5's bank and then the HMDA leak exhibit, five chapters, each with a trap and "Would you ship it?" | Week 5's pipeline rerun: 8,238 validation clients, 928 buyers, AUC 0.795, Rs 2,81,680 at the cost line, Rs 2,92,400 and Rs 11,13,600 for the free lists, Rs 8,61,480 at 0.5, 462 buyers in the top 1,000, the rule's 284 calls finding 189 against the model's 193, duration's 0.9327 and 574, the sealed test's 482 against 113, the late-month promise 15.9 against 24.6 in 100; HMDA's 29,929 applications, 8,040 denials, 0.982, 0.892 and 0.9998 |
| `#field` | Six scenes with one control each, then the six seats on Kalpa's call list | `W06_references.md` 3.1, 3.2, 3.3, 3.6, 3.7, 3.8, 3.12, 3.13 and 3.14 |
| `#interview` | The ten-step ML system design walk for a collections list, then four follow-ups: label delay, reasons for a decline, who a better AUC hurts, the stop switch | Steps from `W06_references.md` section 4; follow-up questions from its list; Regulation B, RBI 2007, the RBI 2026 draft and FREE-AI from section 3 |
| `#check` | Eight checks, the ladder lit, the week's rhythm, and the Week 7 question | Week 7's question from `docs/curriculum/W7_Deep_learning.md` Monday |

## Links on the page, each checked on the day it entered

- UCI Default of Credit Card Clients download, https://archive.ics.uci.edu/static/public/350/default+of+credit+card+clients.zip, checked 29 October 2026
- UCI Bank Marketing download, https://archive.ics.uci.edu/static/public/222/bank+marketing.zip, checked 29 October 2026
- CFPB HMDA data browser, Delaware 2023, originated or denied, https://ffiec.cfpb.gov/v2/data-browser-api/view/csv?states=DE&years=2023&actions_taken=1,3, checked 29 October 2026
- NYDFS, Report on Apple Card Investigation, https://www.dfs.ny.gov/system/files/documents/2021/03/rpt_202103_apple_card_investigation.pdf, checked 29 October 2026
- CFPB, Goldman Sachs consent order, https://files.consumerfinance.gov/f/documents/cfpb_goldman-sachs-bank-usa-consent-order_2024-10.pdf, checked 29 October 2026
- CFPB, Director's remarks on the Goldman and Apple orders, https://www.consumerfinance.gov/archive/newsroom/prepared-remarks-of-cfpb-director-rohit-chopra-on-the-goldman-sachs-and-apple-enforcement-press-call/, checked 29 October 2026
- CFPB blog on Upstart's No-Action Letter, https://www.consumerfinance.gov/archive/blog/update-credit-access-and-no-action-letter/, checked 29 October 2026
- Ascarza, post-print on the HBS site, https://www.hbs.edu/ris/Publication%20Files/ascarza_jmr_18_783d54d4-e548-41ed-b1d7-8a180f1ae85a.pdf, checked 29 October 2026
- Stripe engineering blog on Radar, https://stripe.dev/blog/how-we-built-it-stripe-radar, checked 29 October 2026
- Stripe, ML primer for fraud protection, https://stripe.com/guides/primer-on-machine-learning-for-fraud-protection, checked 29 October 2026
- RBI Working Group on digital lending, https://www.rbi.org.in/Scripts/PublicationReportDetails.aspx?ID=1189, checked 29 October 2026
- RBI circular of 6 March 2007, https://www.rbi.org.in/scripts/NotificationUser.aspx?Id=3315, checked 29 October 2026
- RBI Digital Lending Directions, 2025, https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12848, checked 29 October 2026
- RBI policy statement of 6 December 2024, https://www.rbi.org.in/scripts/BS_PressReleaseDisplay.aspx?prid=59245, checked 29 October 2026
- PIB on MuleHunter.AI, https://www.pib.gov.in/PressReleasePage.aspx?PRID=2244478&reg=3&lang=2, checked 29 October 2026
- Google, Rules of Machine Learning (CC BY 4.0), https://developers.google.com/machine-learning/guides/rules-of-ml, checked 29 October 2026
- Ketan Doshi, Enterprise ML in production, https://ketanhdoshi.github.io/Enterprise-ML-Prod/, checked 29 October 2026
- Google Cloud, MLOps levels (CC BY 4.0), https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning, checked 29 October 2026

Every link above was fetched for `W06_references.md` or `W06_datasets.md` on 29 October 2026; the
three data links were fetched again by this session's data script the same day.

## Decisions taken in the build

| Decision | Why |
|---|---|
| The stage pages teach on an invented postpaid phone operator, with forty unseen and forty training customers typed in the page and a cost ratio of 4 to 1 | The brief forbids handing a group its answer on the card data; a phone plan's churn is the project brief's own suggestion for invented examples, and a different ratio keeps 1 / 6 off the page |
| No Taiwan number beyond the book's size and its October default count reaches the page | Thresholds, bills, AUCs and the traps (the header row, the undocumented codes, the zero-balance defaulters, the duplicates) are what the groups compute and find |
| The story keeps 22 in 100 behind its prediction | The brief asks for the prediction before 22 appears; the ticket states 22.1 percent, so the page states it once committed |
| HMDA's "no rate recorded" means blank or Exempt everywhere on the page | `W06_datasets.md` quotes 98.4 and 0.7 percent, which count blanks only, beside an AUC of 0.982, which counts blank or Exempt. One flag throughout gives all 8,040 denials and 3.7 percent of originations, with AUC 0.982; the data script asserts both readings |
| The bank rule of stage 3 is Week 5 Monday's lab rule, previous campaign succeeded | It is the rule the learners already wrote, and it scores 284 calls at accuracy 0.8988 on the same validation slice |
| The bank's bill slider stops at 0.030 and treats it as the cost line 0.0323 | The grid steps by 0.005, and Week 5 printed the bill at 40 / 1,240 exactly |
| No openly licensed image is used | The kit's own drawings carry every idea; decision `w6-open-images` allows images, it does not ask for them |
| Quotations from Google's rule 29 and from paper titles are left out | `W06_references.md` names rule 29 and the Ascarza paper without their exact words, so the page paraphrases |
| Upstart's figures are labelled as provided by Upstart and not replicated | As `W06_references.md` 3.3 records |
| The RBI 2026 model risk guidance is called a draft | Its finalisation was not verified (`W06_references.md` 3.9) |

## Gaps in the kit (not patched)

- `scripts/html_sweep.py` `find_chromium()` looks for `chrome-linux/chrome`, while this container
  installs `chromium-1243/chrome-linux64/chrome`. The sweep and `explorer_shots.py` ran with
  `PLAYWRIGHT_BROWSERS_PATH` pointed at a scratch folder holding a `chrome-linux` link to the
  installed browser. Adding `chromium-*/chrome-linux64/chrome` to the patterns would remove the step.
- The interview room's order list holds ten steps for the system design walk; it works, and a long
  list on a phone needs scrolling while dragging, so the arrow buttons are the easier route there.
- A field scene's stage title is one string for both views of a toggle, so the Stripe scene's title
  names both views.

## Skills used

companion-builder (the rules: every control acts, nothing preloaded, instant scrolling, dated links);
design-taste-frontend (one accent, one radius scale, no three equal cards, reduced motion);
dataviz (one axis per chart, a legend for two series or more, text in ink, status colours only with
a tick or cross); concept-packaging (a misconception and a prediction first, a paired handle in
each rule card); humanizer (the visible text read for contrasts, triads and staged openers).
