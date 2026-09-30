# Day sheet: Week 3 Wednesday, Build 1, build days two and three

**TRAINER ONLY.**

Posts to <!-- sync:module:W03/D3 -->Module 1: Foundations of AI and Data<!-- /sync:module:W03/D3 -->, on <!-- sync:day-date:W03/D3 -->Wed 21 Oct 2026<!-- /sync:day-date:W03/D3 -->.

Tuesday was Dussehra, so today carries build days two and three, and the catch-up reserve is spent
as slack. Nothing new is taught. The week's approved spine is `docs/detailing/W03_build1_spine.md`,
and its plant table is the answer key for everything the groups will find.

---

## The two-minute orientation

| | |
|---|---|
| **Start from** | Monday's scopes and translation worksheets. The files went out on Monday with the data dictionary, so every group has already met the mess. Today opens on it, not on a drop of files. |
| **Go as far as** | Every group past profiling and into analysis, both logs moving, and one testable headline claim stated at the close with its denominators and caveat, or a named blocker. |
| **Stop before** | Any new technique, and any answer to a group's sub-problem. The rubrics are approved and learners may see them; quote them, never a verdict against them. |
| **Comes later** | Mock R1 runs for every learner on Thursday 22 October, each with a viva on the group's own work, and the build completes around the roster. Friday 23 October brings the GD rounds and the first presentations. |
| **Cut first** | Build time, never the checkpoint or the close. Inside the parallel build, the clinic split and then the per-day table (see the run sheet). |

---

## The day in Dr Menon's words

Dr Priya Menon, COO of Kalpa Health, is the room's internal client for the week. The cohort sits in
Kalpa's Global Capability Centre as trainee engineers. Her ask has not changed since Monday: *"Test
volumes grew 5 percent against a plan of 18, and I do not know which branch of my business is
short."* Today she wants one sentence per sub-problem that she can carry into her own board meeting.

Her data team has told the room two things, and a trainer may repeat both: two cities changed
booking systems in Q2, and the payment feed keys invoices in its own format.

**The thinking the day trains** is Week 1 Wednesday at scale, with no setup cell to lean on:
profile before touching, decide with reasons, reconcile input against kept plus set aside, and
record every decision so the finance head can follow it. The claim is stated today, before it is
tested, so tomorrow tests it rather than finishing it.

---

## The running order

Durations only. The campus day is two blocks of 180 minutes with lunch between them, then open build
time with the TAs (`data/programme/facts.yaml`). A build week carries no practice set, no Kahoot and
no test.

| Block | Min | What runs | Who leads | The file |
|---|---|---|---|---|
| Morning | 30 | **The daily checkpoint.** Each group answers its sub-problem's three questions in two minutes. | Trainer | `checkpoints/C2_W03_D03_checkpoint_questions_STUDENT.md` on screen; `checkpoints/C2_W03_D03_checkpoint_guide_TRAINER.md` in hand |
| Morning | 60 | **The parallel build.** Delhi's revenue tree, Q1 against Q2, solved in the open. | Trainer | `parallel-build/C2_W03_D03_new_york_revenue_tree_STUDENT.ipynb`, run from `parallel-build/C2_W03_D03_run_sheet_TRAINER.md` |
| Morning | 90 | **Build time.** Groups profile, clean, reconcile and cut. The trainer circulates, stuck groups from the checkpoint first. | Groups; trainer circulates | The group's own notebook or SQL, the decisions log, the challenges log |
| Afternoon | 160 | **Build time.** Groups keep building. At the halfway mark, each group writes its draft claim on the headline sheet's shape. | Groups; trainer circulates | `checkpoints/C2_W03_D03_headline_claim_STUDENT.md` |
| Afternoon | 20 | **The close.** Each group states its headline claim in one sentence with its denominators and caveat, or names its blocker, and receives the presentation format. | Trainer | The headline sheet, and `content/W03/SAT/slides/C2_W03_SAT_presentation_format_STUDENT.md` handed out |
| After | Open | **Open build time with the TAs.** Stuck groups first, on the catch-up plan. | Academic TA | `checkpoints/C2_W03_D03_catchup_plan_TRAINER.md` |

Take a break of about ten minutes inside each build stretch at a point that suits the room. Build
time absorbs it.

**The groups.** The handover plans 35 learners in nine groups, eight of four and one of three, while the tracker's
build-week anatomy asks for fifteen groups, three per sub-problem. The Programme Head allocated
groups to sub-problems on Monday; run today on whatever Monday settled. Every part of the day works
per group, so the count changes only how long the checkpoint and the close take.

---

## What every group ships, said the same way all week

| Deliverable | What it is |
|---|---|
| The presentation | A slot of 25 to 30 minutes with a live demo run cold on the group's own Kalpa Health files, and the panel's questions |
| The one-slide answer | The slide Dr Menon carries into her board meeting: claim, evidence, caveat, action |
| The reproduction | The notebook or SQL that reproduces every number from the raw files, top to bottom |
| The decisions log | The Week 1 Wednesday shape: Field, Issue, Rows, Decision, Reason, including one row kept (`content/W03/D1/briefs/C2_W03_D01_decisions_log_STUDENT.xlsx`) |
| The challenges log | Every obstacle and open question as it happened (`content/W03/D1/briefs/C2_W03_D01_challenges_log_STUDENT.xlsx`) |

**Marks, if a learner asks.** The per-event marks are locked (mini project 40, mock 30, GD 30), and
the requester approved the three rubrics on 29 September 2026 for learners to see. The mini project's
rubric, rendered from `data/programme/facts.yaml`:

<!-- sync:rubric:W03/mini-project -->
**Mini project, 40 marks.** The first four criteria are scored once for the group, and every member receives those 34 marks; presentation and defence is scored for each learner on 6 marks, so a silent teammate cannot ride the group's score.

| Criterion | Marks | What full marks look like |
|---|---|---|
| The question translated | 8 | Dr Menon's words are mapped to the right Weeks 1 and 2 method, with the metric defined and the decision it feeds named. |
| The data made trustworthy | 10 | The data is profiled before it is touched, every cleaning call is in the decisions log with its reason, and counts and dollars reconcile across files. |
| The analysis | 10 | The tree, ladder or fair comparison reaches the branch that explains the symptom, on the right denominator, with a chance test where one is needed. |
| The claim | 6 | One sentence carries its number, denominator, period and caveat, plus an action Dr Menon can take. |
| Presentation and defence | 6 | The live demo runs cold, and every member answers a challenge on the caveat. |
<!-- /sync:rubric:W03/mini-project -->

Today's close is where "The claim" criterion is first heard, so hear each sentence against its line.

---

## Circulating: what to watch for, per sub-problem

Ask, never tell. Each line gives the move that shows a group is working well, the mistake it is most
likely to make today, and the question that turns it back without handing over the find.

| Sub-problem | A group is working well when it | The likely mistake today | Ask |
|---|---|---|---|
| 1. Revenue | Has converted every amount, matched invoices to completed bookings across both booking files, and sorted the amounts to see the largest ones | Reads a mean invoice as typical, or divides revenue by `line_items` and calls it revenue per test | "What is your largest single invoice, and what is it for?" and "How many tests sit behind one invoice line?" |
| 2. Bookings | Has opened both booking files, applied an identity rule to the old export, and mapped the new system's ids, clinic codes, channels and dates onto the old ones | States the old export's fall as the finding, or parses the new file's dates month first | "Which of your Q2 bookings are in neither file you've counted?" and "Read one new-system date aloud: which is the day?" |
| 3. Billing | Has counted the reference forms, written one normalisation rule, and anti-joined both ways | Tries a fuzzy match, or sums every payment row as money received | "What rule, in one sentence, turns a reference into an invoice number?" and "What does the same reference and amount twice, minutes apart, mean?" |
| 4. No-shows | Has row counts per clinic beside every rate and has read the values of `kind` | Calls one clinic twice as bad from 19.2 against 8.7 percent | "Which visits could never be a no-show?" and "How often would chance give a gap like this on a base of 50?" |
| 5. Campaign | Has split offered against not offered inside each city and fixed a window | Quotes the 9 percent across all cities as the campaign's effect | "Run it inside one city. Does it hold?" and "Were those cities rising before the offer?" |

**For every group, Dr Menon's 5 percent.** A group that tries to explain her 5 percent with its own
number is doing the right thing. Ask, "What does her dashboard count?", and leave it there. The spine
holds the answer (5.1 percent on the dashboard's count, 7.8 in tests booked across both systems, 8.6
in tests performed and 5.6 in bookings, all without the corporate contract, and every reading short
of 18).

**The offer outside the three cities.** The campaign file carries offers in all six cities: half
the patients in Bengaluru, Hyderabad and Mumbai, and a fifth elsewhere at random (Delhi 316). In
Delhi, offered patients out-book the rest by 23.5 percent, and a permutation test puts that at p of
about 0.03. It is a chance draw: the offer there was random, and nothing in the data makes an offered patient
there book differently. A group that
finds it has met a false positive. Ask it what else it would expect to see if the offer caused the
gap, and whether Chennai and Pune show it (minus 4.8 and plus 0.6 percent).

---

## The close: hearing the headline claims

Twenty minutes. Each group gets about a minute. One member says the claim and a different member
says the caveat. Write each claim down word for word; tomorrow's viva and the Saturday panel start
from these sentences.

Say one thing to each group, chosen by the kind of claim it brings. Never give a verdict, never say
whether the number matches the spine, and never compare two groups.

| The claim you hear | What to say |
|---|---|
| Number, denominators, period and caveat, all there | "What single finding would make you withdraw it?" Then: "Pin it." |
| A number with no base ("Bengaluru is short") | "Short against what, and per what?" |
| Dr Menon's own number said back ("growth is 5 percent") | "Whose count is that, and what does it count?" |
| A cause read from a comparison ("the campaign lifted bookings") | "Compared with whom, and are they alike?" |
| A rate on a small base ("the clinic is twice as bad") | "How many visits is that?" |
| A number no one can reproduce ("about 20 percent") | "Which cell prints it?" |
| A caveat folded into the claim until the claim disappears | "Say the claim alone, then the caveat alone." |
| A blocker, named | "Thank you. The TA will be at your table first." Add it to the catch-up list. |

Then hand out the presentation format and say it plainly: tonight's task is the presentation
skeleton on claim, evidence, caveat, action, and closing the evidence gaps today's claim exposed.

---

## The interview angle, with written answers

The questions go to the room exactly as the row tags them. The answers stay here.

**[F] Two systems export the same entity with different id formats; how do you reconcile them?**
I write one rule that turns every format into a canonical key and apply it to both sides, leaving
both exports untouched. At Kalpa Health, for example, the payment feed writes an invoice as bare
digits, as `INV-` and a number, or in full. The rule pads the digits and prefixes the series, so an
exact join that matched 2.2 percent of payments matches all of them. Then I prove the rule: the
match rate before and after, an anti-join in both directions, and every leftover classified as a
real gap or a defect in the rule. On the way I check the grain, so a key repeated on one side cannot
double a total, and the rule goes in the decisions log so finance can rerun it. In one breath:
normalise to one key by a stated rule, prove it both ways, and classify every leftover.

**[D] State your finding in one sentence a COO can carry into a board meeting.** The number, its
denominators, the period and the reason in one sentence, with the caveat on the next line. From
today's parallel build: "Delhi's invoiced revenue rose 5.4 percent, from Rs 15,56,455 on 977
invoices in Q1 to Rs 16,39,775 on 1,055 in Q2, because it raised more invoices at a slightly lower
mean." The caveat follows on its own line: it is invoiced revenue, not collected, and per day the
rise is 4.2 percent. In one breath: claim first with its bases, caveat second, and nothing a chart
would have to explain.

---

## When the day goes wrong

| What happens | What you do |
|---|---|
| A Codespace will not open for a group | That group works from one member's laptop for the checkpoint, and the TA sorts the environment in the first build stretch. The data is in the repository at `content/W03/D1/data/`. |
| Half the room is stuck on the same step | Stop build time for five minutes and ask the checkpoint nudge for that step to the whole room. Never demonstrate the answer. |
| A group finishes its sub-problem early | Ask it for a second way to reach its headline number, then for the claim's weakest assumption, tested. Keep it out of another group's sub-problem. |
| A group asks what the rubric rewards | Point at the rubric on the headline sheet and read the line for the criterion it is asking about. Never say where the group stands against it. |
| Two groups on one sub-problem reach opposite claims | That is the week working. Tell both to keep their caveats; the panel hears alternate viewpoints on purpose. |
| The close runs long | Cut the one-thing-to-say to a single question and keep every group's sentence. A group that does not speak today enters tomorrow's viva with no claim. |

---

## Files for each moment

| Moment | File |
|---|---|
| The checkpoint | `checkpoints/C2_W03_D03_checkpoint_questions_STUDENT.md`, `checkpoints/C2_W03_D03_checkpoint_guide_TRAINER.md` |
| The parallel build | `parallel-build/C2_W03_D03_new_york_revenue_tree_STUDENT.ipynb`, `parallel-build/C2_W03_D03_run_sheet_TRAINER.md` |
| Build time and the close | `checkpoints/C2_W03_D03_headline_claim_STUDENT.md` |
| Open build time | `checkpoints/C2_W03_D03_catchup_plan_TRAINER.md` |
| Monday's pack, referenced | `content/W03/D1/briefs/` (the briefing note, the five briefs, the data dictionary, the translation worksheet, both logs) and `content/W03/D1/slides/C2_W03_D01_introduction_STUDENT.md` |
| Handed out at the close | `content/W03/SAT/slides/C2_W03_SAT_presentation_format_STUDENT.md` |
| Where every number came from | `internal/C2_W03_D03_provenance_INTERNAL.md` |
