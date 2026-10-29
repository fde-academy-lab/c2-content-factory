# Week 6 plan: Build 2 at Kalpa Financial, one shared problem from black box to defence

INTERNAL. The requester approved this spine on 29 October 2026, with the Mock R2 viva inside
Thursday's approach gate and the breadcrumb notebook in the starter repo from Tuesday. It wins over
the tracker row `docs/curriculum/W6_Build_2.md` where they differ (decisions `w6-build-pack`,
`w6-open-images` and `w6-poc-mvp` in `data/programme/facts.yaml`). The pack's contract is
`docs/12_Build_Week_W06.md`. Research: `docs/detailing/W06_research/` (datasets measured, references
and cases verified, pedagogy), each checked on 29 October 2026. Planned in BMAD order (brief,
research, design, council, spine) and critiqued by a four-seat council (learning designer, hiring
manager, senior ML engineer, trainer operations).


Changes from v1 (council of 29 October 2026): the card goes to each group in Tuesday's discovery call
and Thursday's gate twists one number on it; one action, a call before the due date; card 3 becomes
"balance protected"; the passport carries the two honesty lines (the Taiwan AUC proves the pipeline
and is never Kalpa's score; this data allows no out-of-time split, so the MVP plan must add one); the
builder role rotates by stage and the evaluator runs the POC cold on Friday; the Mock R2 viva folds
into Thursday's gate with every member questioned, and the technical half becomes a written sheet;
the red-team partner records Friday's cold run; Saturday rooms run by card, both holders back to
back; a daily ninety-second opener; Wednesday's "I do" runs on the Week 5 bank model, and HMDA shrinks
to a 15-minute leak exhibit; learners open four things all week; the Mock R2 prep keeps questions
only. The requester then chose the council's view on the breadcrumb notebook: it is the starter repo's
only notebook from Tuesday, with its hints sealed.

## The problem
Kalpa Financial is launching credit cards in India and has no card history yet. Rohan Desai licenses
a public card book (UCI Default of Credit Card Clients, CC BY 4.0: 30,000 Taiwanese cardholders, six
monthly statements, April to September 2005, 22.1 percent defaulted in October) to prove the method
first. That is the POC; the MVP plan says what changes when Kalpa's own data arrives. The one action:
a call from Kalpa's team before October's due date. The ask: "Whom do we call, when a missed default
costs about five times a wasted call and the team can reach N people, and what is the error bill of
the list?"

## The cards (each changes the answer, measured on the data; five cards held twice)
| Card | The rule | Thursday's twist |
|---|---|---|
| 1 | A missed default costs 5 times a wasted call | The CFO says 20 times: the model beats "call everyone" by 1.8 percent, so the action must change |
| 2 | The team can make 1,000 calls | 2,000 calls: the model's lead over "sort by months late" grows from 21 to 69 defaulters |
| 3 | The team is paid on balance protected | Rank by chance times balance: a different list from the same model |
| 4 | Every caller must say the main reason a customer is on the list | Compliance asks for the reason in writing (RBI, 6 March 2007): logistic 0.765 against boosting 0.778 |
| 5 | Sex, marital status, age and education may not be used | Show the list by group: AUC moves 0.001 and the gap stays |
| 6 | September's statement arrives after the list is built | AUC 0.778 to 0.747; the rule loses its best column |
| 7 | October's outcomes arrive in November | Train on a proxy label: 141 fewer defaulters per 1,000 calls |
| 8 | A code not in the dictionary is a question, never a guess | Rohan rules that an account owing nothing cannot default: the base rate moves |

## The ladder, one page each in the workbook
0 The business, black box · 1 The frame · 2 FR, NFR, constraints, security and governance · 3 Options
A and B, one chosen, the fact that flips it · 4 The POC and its error bill · 5 The architecture,
black box to white box, HLD to LLD · 6 The MVP slice: a scoring function, a live demo, README, model
card · 7 Present and defend.

## The week (durations only)
| Day | Stages | What happens |
|---|---|---|
| Tue, online | 0 to 2 | Launch 45; silent read of the ticket 6 and a readiness check 15; question writing 10; discovery calls of 8 per group in three rooms, where the card is handed over; stages 0 to 2 on paper with no AI 60; starter kit set up; the opener 20 |
| Wed | 3 to 5 | Checkpoint 30; the "I do" walk on Week 5's bank model 30; the A against B sheet; the POC and its error bill; the group's own first architecture; pre-mortem 15; HMDA leak exhibit 15; the opener 20 |
| Thu | 5 | The approach gate, 15 per group, with the Mock R2 viva inside it and every member questioned; the card's twist; architecture revised against the notebook's sealed hints; red-team swap 20 per pair; dry run 1; the Mock R2 written sheet 30; the opener 20 |
| Fri | 6, 7 | Industry showcase 60; GD rounds; the MVP slice, README and model card; build freeze; the evaluator runs the POC cold; dry run 2 recorded by the partner group; passport retakes |
| Sat | 7 | Talks of 12 minutes, questions 6, changeover 2, in two rooms by card; grade closure; week close |

## What a learner opens all week (four things)
1 The ticket (two sides: the ask, the discovery-call guide, the card, the AI rules). 2 The workbook
(eight pages, with the challenges log, AI log, passport and run sheet inside). 3 The starter repo
(the breadcrumb notebook, src, the demo app stub, model card and README templates, the seven-slide
template). 4 The week explorer (the story of an ML project from ask to production,
the concept map, how-it-works pages, the leak exhibit, two field scenes, the interview room solving
the ML system design walk step by step).

## Trainer-only
Run sheets per day; Rohan's discovery-call script; the cards and their twists; gate and checkpoint
questions; the full reference build with every card's numbers; rubrics marked proposed; scoring
workbooks; the Mock R2 written sheet and viva prompts; GD prompts and facilitation; the expert's
showcase brief; sources.

## Proposed for the Programme Head (facts.yaml has them open)
Mini project 40: frame and requirements 8, data audited 6, honest POC and error bill 10, the card's
decision and the MVP plan 8, all for the group; passport and defence 8 per learner. Mock R2 30: viva
inside the gate 15, written technical sheet 15. GD 30: Build 1's rubric. Mock and GD owners.

## Staff arithmetic
Thursday's gate: 13 groups at 15 minutes is 195 minutes, about 65 for each of three staff. Saturday:
13 slots of 20 minutes is 260 minutes, 130 per room. Friday's GDs at about 30 minutes per group are
390 minutes, about 195 per room in two rooms.
