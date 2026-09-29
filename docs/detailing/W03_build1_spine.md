# Build 1 (Week 3): the approved spine

Approved by the requester on 29 September 2026, with four decisions: the data is a synthetic Kalpa
Health pack rather than the unnamed public source the row mentions; the mini project, mock and GD
rubrics are drafted for the requester's approval and wait for it; the group-to-problem allocation is
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

Scoring sheets for the mock, the GD and the mini project take their criteria from the rubrics once the
requester approves them; the locked marks per event (mini project 40, mock 30, GD 30) may be stated
now, and no file states a criterion before the approval.

## The data pack, and what is planted

`data/generate_kalpa_health.py` writes ten CSV files into `content/W03/D1/data/`, deterministically,
and `--contract` asserts every plant. All five days read the same files. The plants are TRAINER ONLY;
the numbers below are the generator's witness.

| Sub-problem | What is planted | The numbers |
|---|---|---|
| The headline, for every group | Dr Menon's 5 percent is her dashboard's count: retail tests booked in the old system only, a package counted as its component tests | 5.1 percent on the dashboard's count; 7.8 percent in tests booked across both systems, 8.6 percent in tests performed and 5.6 percent in bookings, all without the corporate contract, whose 1,200 health checks add 6,000 tests to Q2; every reading is short of the plan of 18 |
| 1 Revenue | One corporate health-check contract in Q2, and packages billed as one line | Rs 18,00,000, 16.2 percent of Q2 revenue; the Q2 mean invoice is Rs 1,904 with it and Rs 1,596 without, against a median of Rs 1,499; 48,235 tests performed behind 22,152 invoice lines |
| 2 Bookings | Chennai and Pune moved to the new booking system on 18 September, and the old system's export carries only its own bookings | The two cities fall 23.0 percent in the old export and 12.2 percent in truth; the old export also repeats 180 rows from a mid-quarter re-export |
| 3 Billing | The payment feed keys invoices as bare digits or INV-numbers, gateway retries double-post, and the corporate invoice is unpaid | An exact join matches 2.2 percent of payments; normalised, every payment matches; 229 double posts; 102 refunds; 398 unpaid invoices |
| 4 No-shows | One small clinic runs by appointment while the others' visit counts include walk-ins | 19.2 percent against 8.7 percent on all visits; 20.0 percent (10 of 50) against 15.2 percent on scheduled visits, a gap chance produces with probability 0.22 |
| 5 Campaign | The offer ran in three cities already rising, and within them it reached patients who had begun to drift | Offered patients book 9.0 percent more overall and less in every campaign city (Bengaluru -10.8, Hyderabad -19.9, Mumbai -13.0 percent); the campaign cities rose 6.9 percent in the two months before the offer |

## Sessions and branches

One session per day: `w03-d1`, `w03-d3`, `w03-d4`, `w03-d5` and `w03-sat`. Each writes only in its
own day folder; the data pack and the generator belong to the orchestrating session.
