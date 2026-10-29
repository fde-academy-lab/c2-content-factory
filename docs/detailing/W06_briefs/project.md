# Build 2, project session: the ticket, the workbook, the cards, Rohan and the reference build

INTERNAL. Read `common.md` first. Branch `w06-project`. Skills: `exercise-builder` (item sizing and
how a sheet forces a decision), `scaffold-exercises` (the ladder of stages), `study-notes-builder`
(the printed page), `notebook-builder` (the reference build's rhythm and checks), `humanizer`.

## 1. The ticket (`1_project/C2_W06_D02_ticket_STUDENT.md`, two printed sides)

Side one: Rohan's ask in his own words (one short paragraph); the decision and the one action; what
a finished answer looks like (one sentence with the list size, the error bill and its caveat); what
the group hands in and on which day (the workbook pages, the repository, the twelve-minute talk);
the AI lanes in a box. Side two: how to run the discovery call (ten minutes of question writing
first, then eight minutes with Rohan, then the restate-back: the group says the problem back to him
in two sentences), a blank box where the group writes its constraint card, and the ladder as one
strip of eight boxes. No more than about 600 words in all, and a picture or a table wherever one
works.

## 2. The workbook (`1_project/C2_W06_D02_workbook_STUDENT.md`, about twelve printed pages)

One page per ladder stage (0 to 7), then the numbers passport, the run sheet, the challenges log and
the AI log. Each stage page runs: the question the stage answers; why a real team does this step,
in three sentences with one real-world consequence from `W06_references.md` (for example the Apple
Card's explanation failure for stage 2, Upstart's A against B for stage 3, Ketan Doshi's "the model
is the tip of the iceberg" for stage 6); a tiny worked example on invented numbers labelled
invented, on a different product (a gym's lapsed members or a phone plan's churn), so the method is
shown and the group's answer is not; the boxes the group fills; and "you are ready for the next
stage when", a checkable line. Stage 2 is a table of FR, NFR, constraints, security, privacy and
governance with one invented row filled. Stage 3 is the A against B sheet (what it is, error bill,
build time, can Rohan explain a call, how it fails, our call and the fact that would flip it).
Stage 5 has a black box, a white box with five to seven boxes (data, features, train, evaluate,
score, serve, monitor) and one box zoomed into its LLD. Stage 6 is a three-column table: what the POC
proved, what an MVP adds, what production adds. The passport and run sheet follow `common.md`.

## 3. The constraint cards (`4_trainer_only/C2_W06_D02_constraint_cards_TRAINER.md`)

Each card on its own page, ready to print and hand over: the rule in Rohan's words, where such a
rule comes from in the real world (for card 4 the RBI circular of 6 March 2007 as `W06_datasets.md`
quotes it; for card 5 the fairness reasoning; for card 6 a statement cycle), and what the card asks
the group to produce. Below a cut line, trainer-only: the Thursday twist and the numbers the
reference build gives for the card and its twist.

## 4. Rohan's discovery-call script (`4_trainer_only/C2_W06_D02_discovery_call_script_TRAINER.md`)

For the three role-players: who Rohan is and how he talks; the answers he gives only when asked (the
cost ratio, the call capacity when the card has one, what each column means as the UCI page states
it, what the decision changes, when the outcome is known), the answers he does not have ("ask my data
team" for codes the dictionary omits), what he never volunteers, and the restate-back he insists on.
Eight minutes a group.

## 5. The reference build (`4_trainer_only/C2_W06_D02_reference_build_TRAINER.ipynb`, executed)

The trainer's full solution and the breadcrumb notebook's solution twin: load in code, the audit that
finds every real trap, the frame, the split, the rule "sort by months late" as approach A, logistic
regression and gradient boosting as B, the error bill at 5 to 1, and every card's number and twist's
number, each printed as a PASS check against `W06_datasets.md` section 3(c) or a printed difference
with its reason. Charts: the base rate, the threshold sweep and its bill, the top-N list against the
rule. Follow the MAP, DO, SEE, CHECK, SUM rhythm.

## 6. The gate and the viva (`4_trainer_only/C2_W06_D02_gate_and_viva_TRAINER.md`)

Thursday's 15-minute approach gate per group: what the group shows (workbook pages 1 to 5, the POC
run), the three gate questions with what a pass sounds like and what "not yet" sounds like, then the
Mock R2 viva inside it, every member questioned for about three minutes on the group's own work
(prompts by ladder stage, with the follow-up that separates understanding from recital), and the
card's twist handed over at the end.

Print the ticket and workbook with `python3 scripts/build_doc.py content/W06/D2`.
