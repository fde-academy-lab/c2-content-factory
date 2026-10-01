# Trainer notes, Build 1 week close: what did the room find, and how do you close the week on it in 15 minutes?

**TRAINER ONLY.** This page names what is planted in Build 1's data, with its numbers. The deck it goes
with, `slides/C2_W03_SAT_week_close_STUDENT.md`, names none of it, and neither do its speaker notes.

Posts to <!-- sync:module:W03/SAT -->Module 1: Foundations of AI and Data<!-- /sync:module:W03/SAT -->, on <!-- sync:day-date:W03/SAT -->Sat 24 Oct 2026<!-- /sync:day-date:W03/SAT -->.

The week close is the last 15 minutes of Build 1, after grade closure. All week nine groups answered
the five questions of Dr Priya Menon's heads (Kalpa Health's COO asked why test volumes grew 5
percent from Q2 to Q3 of 2026 against a plan of 18, and which branch of her business is short), on
ten synthetic files, with the Weeks 1 and 2 method; today every group presented to a panel. The close
names what the week trained, collects one improvement per group for Build 2, and hands the room to
Week 4.

**Who needs the answer.** The trainer, who runs the close, and every learner, who leaves with one
change to make in Build 2 and a story to tell in an interview. A close that names a finding no group
reached hands the next cohort's answers to this one and tells a group what its own slot should have
said.

**The questions on the way.** What does the close need in hand? How do you collect what the room
found? What did the data hold, so you can recognise a finding when a chair describes it? What do you
say on each slide? What do you do when the close goes wrong?

## What does the close need in hand before it starts?

**Who needs the answer.** The trainer, in the minutes before grade closure ends.

**The questions on the way.** How long does the close run, and what can be cut? What must be on the
table?

| | |
|---|---|
| **Length** | 15 minutes: 4 on what the week trained (S1, S3, S4, S6), 8 on the nine improvements (S8, S9), 3 on Monday (S11, S12). D2, D5, D7 and D10 are read alone. |
| **If the day is late** | Run it in 10: say S3 in one minute, keep the eight minutes of improvements whole, and say the bridge in one sentence. Never cut the improvements. |
| **In hand** | The findings list the two chairs fill at the end of their rooms (below), and a board or a shared screen for the nine sentences. |

The close needs one list from each chair and a place to write nine sentences.

## How do you collect what the room found?

**Who needs the answer.** The trainer, who says in the close only what groups found, in their own
words.

**The questions on the way.** Who fills the list, when, and with what?

At the end of each room's last slot, ask the chair for one line per group on the list below. It takes
two minutes and lets the close name only what the room found. Keep it on paper; it is never
committed.

| Group | Question | What the group found, in the chair's words | Found it, found part of it, or stopped at the first cut |
|---|---|---|---|
| G1 to G9 | 1 to 5 | One line | One of the three |

The list is the only source the close quotes from.

## What did the data hold, so you can recognise a finding when a chair describes it?

**Who needs the answer.** The trainer, who hears a chair's one line and must know whether it is a
finding, part of one, or the first cut.

**The questions on the way.** What is planted under each question, with its numbers? What does a group
that found it say?

Every number here is recomputed from the ten files by `internal/C2_W03_SAT_witness_INTERNAL.py`, which
checks each against the approved spine and ends `RESULT: PASS`. The question bank,
`trainer/C2_W03_SAT_question_bank_TRAINER.md`, carries the full tables. Percentages are changes from Q2
to Q3 unless the row says otherwise.

| Question | What a group that found it said | The numbers |
|---|---|---|
| The headline, every group | Her 5 percent counts retail tests booked in the old booking system only; every honest reading of test volumes grows a little faster, and every one is short of 18 once the one employer contract is set aside. | 5.1 percent on the dashboard's count; 7.8 percent in tests booked across both systems, 8.6 in tests performed, 5.6 in bookings; the contract adds 6,000 tests to Q3. |
| 1 Revenue | One employer claim moves every total and every average, and a panel is one claim line with several tests behind it. | $180,000 is 14.6 percent of Q3's $1,231,001 billed; billed charges grow 26.9 percent with it and 8.3 without; the Q3 mean claim is $210.50 with it and $179.75 without, the median $150; 22,152 claim lines bill 46,867 tests on completed bookings. |
| 2 Bookings | Chicago and Philadelphia moved to a new booking system on 18 September, so the old export shows about twice the real fall, and the old export also repeats rows. | Down 23.0 percent in the old export (1,415 to 1,090) and 12.2 percent across both systems (to 1,243); 180 repeated booking ids. |
| 3 Billing | The posting system keys claims three ways, duplicate remittance loads double-post, the employer claim has no posting, and a denial posts with nothing paid. | An exact join matches 1.9 percent of postings and normalised every one matches; 280 double posts worth $19,204.63; 398 claims with no posting, $253,165, the $180,000 employer claim among them; $801,314 collected net on $2,201,099 billed. |
| 4 No-shows | KH-ATL-03 runs by appointment while the other centres' visits include walk-ins, who cannot miss a slot; on its 79 scheduled slots the remaining gap is within chance. | 18.8 against 7.9 percent on all visits; 19.0 percent (15 of 79) against 15.1 on scheduled slots; chance gives the gap with probability 0.21. |
| 5 The offer | The offer went to half the patients in three metros that were already rising, and inside each of those metros offered patients booked less; New York's gain is chance. | 9.0 percent more overall; 10.8, 19.9 and 13.0 percent less inside Dallas, Atlanta and Phoenix; those metros rose 6.9 percent before the offer; New York's 23.5 percent more has p of about 0.03 among six metros tested. |

A chair's line that names the number in the right-hand column with what it counts is a finding; a line
that repeats the head's own number (5 percent, two metros down, 9 percent, the worst centre) is the
first cut.

## What do you say on each slide?

**Who needs the answer.** The trainer, slide by slide, in 15 minutes.

**The questions on the way.** What is said, asked and written on each live slide?

**Cover and S1, 30 seconds.** "Dr Menon asked which branch of her business is short and what to tell
her board. Every group in this room gave her an answer today, before a panel that had never seen the
work. Three questions close the week, and the middle one is yours."

**S3, 90 seconds.** Read the diagram once, left to right. Then hand each move to the groups that used
it: from the chairs' list, ask one group that reached a finding to state it in one sentence of its own
("Group 4, what did you find on bookings, and which move found it?"), and let the sentence stand as the
group said it. Add no finding, name no problem in the data, and correct no wording; where no group
reached a finding, move to the next move and say nothing about it.

**S4, 1 minute.** "The words changed, the cost of being wrong rose, and the moves stayed: that is the
week." Ask one group for its answer to the [F] question: what did it check twice because a wrong
number here can mean a missed diagnosis?

**S6, 1 minute.** "Seven questions, and a panel asked one of them of someone here today. Tonight, write
your own one-breath answer to each from your group's work; each one is now a true story with a number
in it."

**S8 and S9, 8 minutes.** Two minutes in groups, then each group reads its one sentence and you write it
up exactly as said. Push back on any sentence that names a virtue ("communicate better") with one
question: "What would I see you doing differently on day one of Build 2?" Take the rewrite and move
on. The nine sentences go to the Programme Head for Build 2's first-day sheet; Build 2 opens on
Tuesday 10 November.

**S11, 2 minutes.** Read Meera's words from the slide. "This week you asked which branch is short. On
Monday she asks which one number the whole company should chase, and what stops people gaming it.
Marketing wants orders per month, operations wants app sessions, and the head of Retail-Plus wants
reorders per member." Stop there; Monday opens on it.

**S12, 1 minute.** Read the three lines and Kavya's review. "Rest tonight."

Every live slide asks the room one thing, and the only findings said aloud are the ones a group said
first.

## What do you do when the close goes wrong?

**Who needs the answer.** The trainer, in the minute it happens.

**The questions on the way.** What do you say when a group asks for the answers, its scores, or blames
a teammate?

| What happens | What you do |
|---|---|
| A group asks what it missed | "The panel's questions were the pointers, and your notebook and the files are still there." Name no plant. |
| A group wants its scores | "Scores are with the Programme Head, who tells you how and when you see them." |
| A group's improvement blames a teammate | Ask for the behaviour the group will change, and write that instead. |
| The room is flat after a long day | Keep S8 and S9 whole and cut S3 to its diagram; the improvements are what Build 2 uses. |
| A group asks which group was right | "Two groups can both be honest when each says what it counted; your one-slide answer is yours to defend." |

The close protects two things whatever happens: the nine sentences, and every plant no group named.
