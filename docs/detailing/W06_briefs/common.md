# Build 2 sessions: the rules every session follows

INTERNAL. Four cloud sessions build Build 2's pack in parallel, each on its own branch and its own
files. Read, in this order: `CLAUDE.md` (the sections "From Week 5 on" and "Hard rules"),
`docs/12_Build_Week_W06.md` (the contract), `docs/detailing/W06_build2_plan.md` (the approved spine),
this file, then your own brief beside it. The research behind every number and case is in
`docs/detailing/W06_research/`: `W06_datasets.md` (the data, its real traps and every constraint
card's numbers, measured on 29 October 2026), `W06_references.md` (verified cases, the ML system
design walk, openly licensed images with their attribution lines) and `W06_pedagogy.md` (the
techniques and why).

## The room and the failure this pack answers

39 learners averaging 3 out of 10, in 13 groups of three. In Build 1 they did not read about 10,000
words of brief, pasted it into ChatGPT, could not explain their own numbers, showed no business
nuance and spent seven of ten presentation minutes re-explaining the problem. So every file here
reads small and makes the thinking unavoidable: short sentences, one idea a page, a picture before a
paragraph, a number with its unit and its meaning, and nothing a learner must read twice to use.
Teach from first principles, in the blend of `.claude/skills/day-pack-builder/references/teaching-styles.md`:
the misconception and a prediction first, the idea drawn on tiny numbers, then the real data.

## The problem, word for word

Kalpa Financial Services is launching credit cards in India and has no card history of its own.
Rohan Desai, head of risk, has licensed a public card book to prove the method before Kalpa's own
data exists: UCI Default of Credit Card Clients (CC BY 4.0; cite "Yeh, I. (2009). Default of Credit
Card Clients [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C55S3H"), 30,000
Taiwanese cardholders with six monthly statements from April to September 2005, of whom 22.1 percent
defaulted in October 2005. Rohan's ask: "Before October's due date, whom should Kalpa's team call,
when a missed default costs about five times a wasted call, and what is the error bill of the list
we hand over?" The one action is a call before the due date. Costs are in cost units (a wasted call
is 1, a missed default is 5); Kalpa will price the units once its own call centre runs, and the MVP
plan names that as a gap. The proof is a POC: the Taiwan score proves the pipeline and is never
Kalpa's score, and this data allows no out-of-time split, so the MVP plan must add one.

Download in code, cached: `https://archive.ics.uci.edu/static/public/350/default+of+credit+card+clients.zip`
holds `default of credit card clients.xls`; reading it needs `xlrd`. Never name a trap the room is
meant to find (the header row, the undocumented status codes, the accounts owing nothing labelled
default, the duplicates) in a STUDENT file; the TRAINER files may.

## The constraint cards

Eight cards, the rule in Rohan's words on Tuesday and a one-number twist at Thursday's gate. Numbers
are from `W06_datasets.md` section 3(c); the reference build recomputes them.

| Card | Tuesday's rule | Thursday's twist |
|---|---|---|
| 1 | A missed default costs 5 times a wasted call | The CFO says 20 times |
| 2 | The team can make 1,000 calls this month | It can make 2,000 |
| 3 | The team is measured on balance protected | Rank by chance times balance and compare the lists |
| 4 | Every caller must say the main reason the customer is on the list | Compliance wants the reason in writing |
| 5 | Sex, marital status, age and education may not be used | Show the list's flag rate by group |
| 6 | September's statement arrives after the list is built | The list must go out on the 1st, so only April to August exist |
| 7 | October's outcomes arrive in November | Train today on a proxy label and say what it costs |
| 8 | A code not in the data dictionary is a question, never a guess | Rohan rules that an account owing nothing cannot default |

Cards 1, 2, 4, 5 and 6 are each held by two groups; 3, 7 and 8 by one. Both holders of a card present
back to back on Saturday.

## The ladder, with the explorer's routes

| Stage | Name | Workbook page | Breadcrumb notebook section | Explorer route |
|---|---|---|---|---|
| 0 | The business, black box | 1 | none | `#p1` |
| 1 | The frame | 2 | 1 | `#p1` |
| 2 | Requirements (FR, NFR, constraints, security, privacy, governance) | 3 | 2 | `#p2` |
| 3 | Options A and B, one chosen | 4 | 3 | `#p3` |
| 4 | The POC and its error bill | 5 | 4 | `#p4` |
| 5 | The architecture, black box to white box, HLD to LLD | 6 | 5 | `#p5` |
| 6 | The MVP slice, and POC against MVP against production | 7 | 6 | `#p6` |
| 7 | Present and defend | 8 | none | `#p7` |

The explorer also has `#story`, `#map`, `#case` (the worked parallel and the leak exhibit),
`#field`, `#interview` and `#check`.

## The run sheet (twelve minutes, seven slides, every member speaking)

| Minutes | Slide | Who | What |
|---|---|---|---|
| 0:00 to 1:30 | 1 | Drawn by the panel | The recommendation and its error bill in one sentence, then situation, complication, question |
| 1:30 to 3:00 | 2 | Decision owner | What each error costs, as one picture, and the metric that follows |
| 3:00 to 6:00 | 3 | Builder | The live demo: score one customer, show the reason and the cost, change the card's number |
| 6:00 to 8:00 | 4 | Evaluator | A against B on the error bill, and why we chose |
| 8:00 to 9:30 | 5 | Evaluator | How honest the number is: the do-nothing bill, the spread, the trap we caught |
| 9:30 to 11:00 | 6 | Decision owner | What the POC proved and what an MVP still needs (FR, NFR, constraints) |
| 11:00 to 12:00 | 7 | Builder | What would change our call, the top pre-mortem risk, the ask |

Roles rotate by ladder stage so nobody owns all the code; the presenter of slide 1 is drawn on the
day, so all three rehearse it.

## The numbers passport and the AI lanes

- **Passport.** Each learner carries five numbers from the group's own run (the base rate, the
  do-nothing bill, the chosen threshold or list size, the model's bill, the card's number) with what
  each means and where in the repository it is computed, plus two honesty lines: "The Taiwan score
  proves the pipeline and is never Kalpa's score" and "This data allows no out-of-time split, so the
  MVP must add one". Any member may be asked to recompute any slide number live.
- **AI, two lanes.** No AI for the frame on paper (Tuesday), the gate, the viva and the defence.
  AI allowed for code: every use goes in the AI log, and the group explains every AI-written line
  before it is committed.
- **The opener.** Each day closes with a drawn member of every group saying slide 1 to the room in
  ninety seconds, timed by another group; no score.

## The week (durations only, never clock times)

Tue online: launch 45; silent read of the ticket 6 and a readiness check 15; question writing 10;
discovery calls 8 per group in three rooms, where the card is handed over; stages 0 to 2 on paper
with no AI 60; the starter repo set up; the opener 20. Wed: checkpoint 30; the "I do" walk on Week 5's
bank model 30; the A against B sheet; the POC and its error bill; the group's own first architecture;
pre-mortem 15; the leak exhibit 15; the opener 20. Thu: the approach gate 15 per group with the Mock
R2 viva inside it; the card's twist; architecture revised; red-team swap 20 per pair; dry run 1; the
Mock R2 written sheet 30; the opener 20. Fri: industry showcase 60; GD rounds; the MVP slice, README
and model card; build freeze; the evaluator runs the POC cold; dry run 2 recorded by the partner
group; passport retakes. Sat: talks of 12, questions 6, changeover 2, in two rooms by card; grade
closure; week close.

## Every file, and who builds it

| Session | Branch | Files |
|---|---|---|
| Project | `w06-project` | `1_project/C2_W06_D02_ticket_STUDENT.md` and `.pdf`; `1_project/C2_W06_D02_workbook_STUDENT.md` and `.pdf`; `4_trainer_only/C2_W06_D02_constraint_cards_TRAINER.md`; `4_trainer_only/C2_W06_D02_discovery_call_script_TRAINER.md`; `4_trainer_only/C2_W06_D02_reference_build_TRAINER.ipynb`; `4_trainer_only/C2_W06_D02_gate_and_viva_TRAINER.md`; `4_trainer_only/C2_W06_D02_sources_project_INTERNAL.md` |
| Starter | `w06-starter` | everything under `2_starter_repo/` except `2_starter_repo/presentation/`; `4_trainer_only/C2_W06_D02_starter_repo_notes_TRAINER.md`; `4_trainer_only/C2_W06_D02_sources_starter_INTERNAL.md` |
| Explorer | `w06-explorer` | `3_explorer/C2_W06_D02_explorer_STUDENT.html`; `4_trainer_only/C2_W06_D02_explorer_data_INTERNAL.py` and `.json`; `4_trainer_only/C2_W06_D02_sources_explorer_INTERNAL.md` |
| Run | `w06-run` | `README.md` at the pack root; `content/W06/README.md`; `2_starter_repo/presentation/`; `4_trainer_only/C2_W06_D02_run_sheets_TRAINER.md`; the rubric, scoring workbook and its recalc manifest; the Mock R2 written sheet and key; GD prompts; the expert's showcase brief; `4_trainer_only/C2_W06_D02_sources_run_INTERNAL.md` |

Every pack path is under `content/W06/D2/`. Touch only your own files; if you need another session's
file to say something, write it in your report.

## How every session works and finishes

- Cut your branch from `origin/main` and push with `git push -u origin <branch>`. Commit in small
  commits that say what changed, and push at least every hour. Never open, merge or close a pull
  request.
- Read the skills your brief names and say in your report what you took from each.
- Every printed STUDENT markdown file in `1_project/` gets its PDF from `python3 scripts/build_doc.py`.
- Real company facts come only from `W06_references.md` with their source and date; anything it
  marks not verified stays out.
- Run `python3 scripts/verify.py content/W06/D2` before you finish. Another session's files may be
  missing while you build, so the gate must pass on your own files; quote its last lines.
- Report in under 400 words: the files, what each does, the numbers and where they come from, what
  you cut, and anything another session must match.
