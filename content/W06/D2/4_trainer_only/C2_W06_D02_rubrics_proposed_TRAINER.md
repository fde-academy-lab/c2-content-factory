# Rubrics, Build 2, all proposed: how is each group and each learner scored?

**TRAINER ONLY. PROPOSED.** Every criterion, weight and rule on this page is a proposal for the
Programme Head, who closes decision `rubrics-and-calendar` in `data/programme/facts.yaml`. Until it
closes, nothing here reaches a learner, and no STUDENT file states a mark. What is already settled
and may be said: the build carries 100 marks, 40 for the mini project, 30 for the mock interview
and 30 for the group discussion (decision `evaluation-lock`, kept by decision `w6-build-pack`), and
the approved plan puts the Mock R2 viva inside Thursday's gate, the written sheet on Thursday, the
GD rounds on Friday and the talks on Saturday.

| Event | Marks | Scored | When, by the approved plan |
|---|---|---|---|
| Mini project | 40 (proposed split: 32 for the group, 8 per learner) | The group part once per group, every member receiving it; passport and defence per learner | Saturday's talk and questions |
| Mock R2 | 30 (proposed split: 15 viva, 15 written) | Per learner | Thursday: the viva inside the gate, the written sheet in block two |
| Group discussion | 30 | Per learner | Friday's GD rounds |

Scores go into `C2_W06_D02_scoring_TRAINER.xlsx` beside this file, which copies these criteria and
flags any score outside them.

## How is the mini project scored? (proposed)

| Criterion | Marks | Scored | What full marks look like |
|---|---|---|---|
| Frame and requirements | 8 | Once per group | Rohan's ask is framed as a decision (who is called, from what is known when the list is built, about October's default), and workbook pages 2 and 3 hold the functional and non-functional requirements, the constraints, and the security, privacy and governance rules, with the card's rule among them. |
| Data audited | 6 | Once per group | Every column used is checked against the data dictionary and against when it is known; every oddity found is a line in the decisions log with what was done and why; the row count reconciles from the file to the model's input. |
| Honest POC and error bill | 10 | Once per group | A and B are scored on the same customers and the same costs against doing nothing, with the spread across five splits; the error bill is in cost units at the chosen list size or threshold; both honesty lines are said. |
| The card's decision and the MVP plan | 8 | Once per group | The card's rule and Thursday's twist each change a number the group shows live; the MVP plan names what the POC proved, what an MVP adds (an out-of-time split among it) and what production adds; the live demo runs from a fresh start. |
| Passport and defence | 8 | Per learner | The learner recomputes a drawn passport number live from the repository inside two minutes and answers a question put to them by name with the group's own numbers and a reason. |

**The demo rule, proposed as Build 1's approved rule.** The live demo on slide 3 runs once from a
fresh start. If it stops, the group has two minutes to recover it live. If it still stops, the
group presents from its executed notebook, the fourth criterion cannot carry full marks, and the
other 24 group marks stand on the executed run, so a failed demo costs its own marks and never the
analysis. A demo held up by a failed machine runs in the room's reserve before anyone's passport and
defence is scored. Friday's cold run is recorded beside it and decides nothing on its own.

**A score below full on a learner who was never asked.** The chair names each member before a
question, so every learner is asked at least once; a learner the panel could not reach is
questioned in the room's reserve, never scored from the group's answers.

## How is Mock R2 scored? (proposed)

**The viva inside Thursday's gate, 15 marks per learner, on the R1 viva's three criteria.** The
questions come from `C2_W06_D02_gate_and_viva_TRAINER.md`.

| Criterion | Marks | What full marks look like |
|---|---|---|
| The translation, with one decision defended by evidence | 6 | The learner turns Rohan's ask into the group's frame in their own words and defends one decision from workbook pages 1 to 5 with a number from the group's run. |
| Defending a caveat under challenge | 6 | Pushed on the weakest number, the learner names the caveat, says what it would take to remove it and holds the claim at its true size. |
| What they would do differently | 3 | One change, specific enough for the MVP plan to act on. |

**The written technical sheet, 15 marks per learner.** Thirty minutes on paper, no AI; the key is
`C2_W06_D02_mock_r2_written_sheet_key_TRAINER.md`.

| Part | Items | Marks |
|---|---|---|
| A. One correct option | 6 | 1 each, 6 |
| B. More than one correct | 2 | 1.5 each, every correct letter and no other, 3 |
| C. Applied maths | 3 | 2 each: 1 for the number with its unit, 1 for the working, 6 |

**The passport at the gate.** One passport number is drawn in the viva and recomputed live. A
learner who cannot is "not yet" and retakes on Friday with TA1; the result is recorded and moves no
mark on its own, since Saturday's passport and defence scores the same skill a second time.

## How is the group discussion scored? (proposed as Build 1's rubric, unchanged)

Each learner is scored alone, on the four criteria approved for Build 1 on 29 September 2026
(`facts.yaml`, `evaluation.rubrics.W03.events.gd`).

| Criterion | Marks | What full marks look like |
|---|---|---|
| Structures the problem | 8 | The learner frames the decision and the metric before arguing. |
| Uses evidence | 8 | The learner takes a position and defends it with a number from the exhibit. |
| Engages | 8 | The learner builds on or challenges another member's point and brings a quiet member in. |
| Lands a conclusion | 6 | The discussion ends on a recommendation and its main risk. |

## What does the Programme Head decide to close this?

| Question | The proposal on this page | What would change it |
|---|---|---|
| Is the mini project split 32 for the group and 8 per learner? | Yes, as the plan proposes, so a silent member cannot ride the group's score and the passport weighs more than Build 1's 6 | A wish to keep Build 1's 34 and 6 |
| Is the Mock R2 split 15 viva and 15 written? | Yes, as the plan proposes | A written sheet judged too short to carry 15 |
| Does an opened hint cost marks? | No; it is recorded in the challenges log so a TA knows where to coach | Evidence that groups open every hint by reflex |
| Does a "not yet" passport at the gate cost marks? | No; Saturday scores it again | A retake list longer than about a third of the room |
| Do learners see these rubrics before Thursday? | Once the decision closes, the criteria (never the weights of the written items) go into the ticket's next print | Nothing; the gate questions stay with the staff |
