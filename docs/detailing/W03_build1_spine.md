# Build 1 (Week 3): the approved spine

Approved by the requester on 29 September 2026, with four decisions: the data is a synthetic Kalpa
Health pack rather than the unnamed public source the row mentions; the mini project, mock and GD
rubrics are drafted for the requester's approval, which came the same day; the group-to-problem allocation is
decided on Monday by the Programme Head; and each day's session builds from this page without
stopping at a spine of its own. Where this page and the Week 3 row differ, this page wins; everything
it leaves unchanged, the row still carries.

## The week

Kalpa Health runs diagnostic laboratories and walk-in clinics in six Indian cities. Its COO, Dr Priya
Menon, asks why test volumes grew 5 percent against a plan of 18, and which branch of her business is
short. Five sub-problems, each the Week 1 and 2 method in a domain the room has never seen:

1. Where lab revenue comes from, and which branch is short: the revenue tree for a diagnostics
   business.
2. Bookings fell in two cities in Q2: the investigation ladder on booking data.
3. Invoices and collections disagree: reconciliation between the billing export and the payment feed.
4. The no-show rate looks worse in one clinic: real or noise, and what a fair comparison needs.
5. A free home-collection campaign "lifted bookings 9 percent": cause or coincidence.

The campus day runs two 180-minute blocks as `data/programme/facts.yaml` gives them. In a build week
the time after the second block is open build time with the TAs, and the pack carries no practice set.

## Day by day

| Day | What runs, and what the pack carries |
|---|---|
| Mon 19 Oct | The Programme Head's online introduction (60), the allocation (30), each group translating its sub-problem into the Week 1 and 2 method in its own words, and the close (15). The pack: Dr Menon's briefing note, the five sub-problem briefs, the data pack with its data dictionary, the translation worksheet, the challenges log, the introduction deck, and the trainer sheet with both ways to allocate nine groups. |
| Tue 20 Oct | Dussehra, a gazetted holiday; no pack. |
| Wed 21 Oct | The daily checkpoint (30), three questions per sub-problem; the trainer's parallel build on a smaller slice, in the open (60); build time; each group's headline claim with its denominators and caveat (20). The pack: the checkpoint questions, the parallel build, the catch-up plan. |
| Thu 22 Oct | Mock R1 for every learner, about 20 minutes each, a technical half on Weeks 1 and 2 and a viva on the group's work; build completion around the roster. The pack: the mock question bank with model answers, the viva prompts per sub-problem, the roster sheet. |
| Fri 23 Oct | Expert day one: GD rounds at about 30 minutes per group on prompts that climb in complexity, a thread separate from the projects; build freeze; two cold demo runs; the first presentations. The pack: the GD prompts with facilitation notes, the demo rehearsal checklist. |
| Sat 24 Oct | Expert day two with the flown-in leader: the remaining GDs, presentations with live demos at 25 to 30 minutes per group, grade closure, and one improvement per group named for Build 2. The pack: the presentation format, the panel's question bank, the closure run sheet. |

## A demo that fails in the room

The requester left the call to the orchestrating session on 29 September 2026, and one rule runs on
both expert days. A group's demo runs once, cold, on its raw files. If it fails, the group has two
minutes to recover it live, as it would in front of a client. If it still fails, the group presents
from its executed notebook, and the panel scores the live demo in presentation and defence as not
run cold. The other 34 marks of the mini project are scored from the executed run, so a failed demo
costs its own marks and never the analysis.

## The rubrics

The requester approved the three rubrics as drafted on 29 September 2026, and ruled that learners may
see them and that Build 1's learner files may name the day of each graded event. They live in
`data/programme/facts.yaml`, which this block renders; a learner file carries the one it needs as
`sync:rubric:W03/mock`, `sync:rubric:W03/gd` or `sync:rubric:W03/mini-project`, and every scoring
workbook copies its criteria from the same place.

<!-- sync:rubric:W03 -->
**Mini project, 40 marks.** The first four criteria are scored once for the group, and every member receives those 34 marks; presentation and defence is scored for each learner on 6 marks, so a silent teammate cannot ride the group's score.

| Criterion | Marks | What full marks look like |
|---|---|---|
| The question translated | 8 | Dr Menon's words are mapped to the right Weeks 1 and 2 method, with the metric defined and the decision it feeds named. |
| The data made trustworthy | 10 | The data is profiled before it is touched, every cleaning call is in the decisions log with its reason, and counts and rupees reconcile across files. |
| The analysis | 10 | The tree, ladder or fair comparison reaches the branch that explains the symptom, on the right denominator, with a chance test where one is needed. |
| The claim | 6 | One sentence carries its number, denominator, period and caveat, plus an action Dr Menon can take. |
| Presentation and defence | 6 | The live demo runs cold, and every member answers a challenge on the caveat. |

**Mock interview R1, 30 marks.** Each learner is scored alone, 15 marks on the technical half and 15 on the project viva.

| Half | Criterion | Marks |
|---|---|---|
| Technical | Correctness | 8 |
| Technical | Reasoning aloud with numbers | 4 |
| Technical | Handling a follow-up | 3 |
| Project viva | The translation, with one decision defended by evidence | 6 |
| Project viva | Defending a caveat under challenge | 6 |
| Project viva | What they would do differently | 3 |

**Group discussion, 30 marks.** Each learner is scored alone.

| Criterion | Marks | What full marks look like |
|---|---|---|
| Structures the problem | 8 | The learner frames the decision and the metric before arguing. |
| Uses evidence | 8 | The learner takes a position and defends it with a number from the exhibit. |
| Engages | 8 | The learner builds on or challenges another member's point and brings a quiet member in. |
| Lands a conclusion | 6 | The discussion ends on a recommendation and its main risk. |

Mock R1 runs for every learner on Thursday 22 October. The GD rounds run on Friday 23 October and close on the morning of Saturday 24 October. The presentations run on Friday 23 October where the roster allows and on Saturday 24 October, when every Build 1 grade closes.

Build 1's rubrics are locked, settled by the requester, in session, on 29 September 2026, approving the drafts as written.
<!-- /sync:rubric:W03 -->

## The data pack, and what is planted

`data/generate_kalpa_health.py` writes ten CSV files into `content/W03/D1/data/`, deterministically,
and `--contract` asserts every plant. All five days read the same files. The plants are TRAINER ONLY;
the numbers below are the generator's witness.

| Sub-problem | What is planted | The numbers |
|---|---|---|
| The headline, for every group | Dr Menon's 5 percent is her dashboard's count: retail tests booked in the old system only, a package counted as its component tests | 5.1 percent on the dashboard's count; 7.8 percent in tests booked across both systems, 8.6 percent in tests performed and 5.6 percent in bookings, all without the corporate contract, whose 1,200 health checks add 6,000 tests to Q2; every reading is short of the plan of 18 |
| 1 Revenue | One corporate health-check contract in Q2, and packages billed as one line | Rs 18,00,000, 16.2 percent of Q2 revenue; the Q2 mean invoice is Rs 1,904 with it and Rs 1,596 without, against a median of Rs 1,499; 22,152 invoice lines bill 46,867 tests on the completed bookings behind them (48,235 counting cancelled bookings, which the booking-tests file also lists) |
| 2 Bookings | Chennai and Pune moved to the new booking system on 18 September, and the old system's export carries only its own bookings | The two cities fall 23.0 percent in the old export and 12.2 percent in truth; the old export also repeats 180 rows from a mid-quarter re-export |
| 3 Billing | The payment feed keys invoices as bare digits or INV-numbers, gateway retries double-post, and the corporate invoice is unpaid | An exact join matches 2.2 percent of payments; normalised, every payment matches; 229 double posts; 102 refunds; 398 unpaid invoices |
| 4 No-shows | One small clinic runs by appointment while the others' visit counts include walk-ins | 19.2 percent against 8.7 percent on all visits; 20.0 percent (10 of 50) against 15.2 percent on scheduled visits, a gap chance produces with probability 0.22 |
| 5 Campaign | The offer went at random to half the patients in three cities already rising and to a fifth of the patients elsewhere, and inside the three cities an offered patient booked less while the offer ran than one who was not offered | Offered patients book 9.0 percent more overall and less in every campaign city (Bengaluru -10.8, Hyderabad -19.9, Mumbai -13.0 percent); before the offer the two groups booked within about 6 percent of each other (Bengaluru +1.4, Hyderabad -5.2, Mumbai -6.1 percent), so the files cannot show who was targeted; the campaign cities rose 6.9 percent in the two months before the offer. Outside them the gaps are chance: Chennai -4.8 and Pune +0.6 percent, and Delhi +23.5 percent, a random draw that a permutation test puts at p of about 0.03, so a group that finds it has met a false positive rather than a lift |

## Sessions and branches

One session per day: `w03-d1`, `w03-d3`, `w03-d4`, `w03-d5` and `w03-sat`. Each writes only in its
own day folder; the data pack and the generator belong to the orchestrating session.
