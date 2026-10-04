# Brief 5: Did the free at-home collection offer lift bookings 9 percent, and should every patient in all six metros get it?

- **For:** the group or groups allocated sub-problem 5
- **Client:** Dr Priya Menon, chief operating officer (COO) of Kalpa Health, and the marketing head
- **Data:** the ten files in `data/`, exported on Friday 16 October 2026

Kalpa Health and everyone in it are fictional, and every record in the files is synthetic.

> "Our free at-home collection offer lifted bookings 9 percent. I want to offer it to every patient
> in all six metros. Can you confirm it worked?"
> The marketing head, Kalpa Health

**Who needs the answer.** The marketing head, who wants to extend the offer to every patient in all
six metros, and Dr Menon, who signs the cost. Every free collection sends a phlebotomist to a
patient's home, so an offer extended on a lift it did not cause spends that money every week for
nothing, and an offer stopped when it works loses the patients it brought in.

**The questions on the way.** What has Dr Menon asked, and where does this question sit in it? What
do the offer, a lift and the 9 percent mean at Kalpa Health? Which files hold the answer, and how big
is each? Which ways could a group test the claim, and what does each cost? What will the panel ask,
and what does a finished answer look like? What does your group ship, and when?

---

## What has Dr Menon asked, and where does this question sit in it?

**Who needs the answer.** Your group, before it picks a way. The marketing head's question is one of
five that together answer Dr Menon's, and an offer that brings in patients who would not otherwise
have booked is one of the levers she could pull to close her gap.

**The questions on the way.** What business is Kalpa Health? What does Dr Menon see? Which five
questions did her heads ask, and which one is yours? Which real company faces the same question?

Kalpa Health runs a laboratory, which runs the tests, and two patient service centres, where a
phlebotomist draws patients' blood, in each of six US metro areas: Dallas, Phoenix, New York,
Chicago, Atlanta and Philadelphia. Patients book at all eighteen sites. It bills its patients' payers in dollars: commercial health plans, Medicare (the
federal programme for people aged 65 and over and some younger people with disabilities), Medicaid (each state's programme for people on low
incomes) and patients who pay for themselves (self-pay). Its revenue-cycle and analytics work runs
from Kalpa's Global Capability Centre (GCC) in Bengaluru, where you work as trainee engineers in the
data and AI team. It reports in calendar quarters: Q2 is April to June 2026 and Q3 is July to
September 2026.

Its COO, Dr Priya Menon, has written to the team. Her dashboard shows test volumes up 5 percent from
Q2 to Q3, against the board's plan of 18 percent growth in test volumes, and she cannot say which
branch of the business is short: which of the parts it splits into, such as a payer, a metro or a
kind of test. Five of her
heads have each asked her a question, and each group takes one.

| # | The question | Who asks |
|---|---|---|
| 1 | Where does our lab revenue come from, and which branch of it is short? | The finance head |
| 2 | Bookings fell in two metros in Q3: how far, and why? | The patient service centres' operations head |
| 3 | The claims and the posting system disagree: which claims are unpaid, and can the figure be trusted? | The finance head |
| 4 | KH-ATL-03 has the worst no-show rate: is the centre really worse? | The patient service centres' operations head |
| **5** | **The free at-home collection offer "lifted bookings 9 percent": did it work? (yours)** | **The marketing head** |

The marketing head's campaign report says the patients offered a free collection at home booked 9
percent more than the patients who were not offered it, over the weeks the offer ran.

### Which real company faces the same question?

Quest Diagnostics provides "mobile phlebotomy services in many parts of the United States so
patients who prefer an in-home blood draw may access our services for a fee" (Form 10-K for 2025).
Kalpa Health charges a fee of its own for a collection at home, and its offer waived it, so every
free collection cost a phlebotomist's visit with nothing billed for the visit.

---

## What do the offer, a lift and the 9 percent mean at Kalpa Health?

**Who needs the answer.** The marketing head, whose budget rides on the word "lifted" and on what
the lift was measured against.

**The questions on the way.** What did the offer give a patient? Who counts as offered, and who took
it up? Which weeks did it run? How does the report work out the 9 percent?

| Word | What it means at Kalpa Health | Where it lives in the files |
|---|---|---|
| At-home collection | A phlebotomist visits the patient's home and draws the sample there, which costs Kalpa Health the visit; a patient books it as one of the four ways to book | `bookings_legacy.channel`, `bookings_newsys.channel` |
| The offer | A free at-home collection: the visit's fee waived, sent by marketing to a list of patients | `campaign` |
| Offered | On marketing's list, with the day the offer was sent | `campaign.offered_on` |
| Took up | Accepted the offer | `campaign.took_up` |
| The weeks the offer ran | 15 July to 14 September 2026; offers went out from 15 July to 4 August | `campaign.offered_on`, booking dates |
| Bookings per patient | A group's bookings over a period, divided by the number of patients in the group | Built from `patients` and the booking files |
| Lift, as the report works it out | The offered patients' bookings per patient over the weeks the offer ran, divided by every other registered patient's over the same weeks, minus one; the report's figure is 9 percent | Your group recomputes it |

Whether the 9 percent means the offer worked is the question your group answers.

---

## Which files hold the answer, and how big is each?

**Who needs the answer.** Your group, to plan its time. Recomputing the 9 percent takes about two hours,
and the rest of the week goes on what the number means.

**The questions on the way.** Which files does the campaign question start from? How many rows does
each hold, and what is one row?

| File | One row is | Rows | Why it bears on this question |
|---|---|---|---|
| `campaign` | One patient sent the offer | 2,381 | Who was offered, when, where they are registered, and who took it up |
| `patients` | One registered patient | 6,700 | Everyone, offered or not, with their metro, age band and payer |
| `bookings_legacy` | One booking in the booking system in use since before Q2 | 11,729 | Every booking, its patient, date and channel |
| `bookings_newsys` | One booking in the new booking system | 153 | The same, in the new system's codes |
| `sites` | One laboratory or patient service centre | 18 | Which metro each site is in |

Every group holds all ten files, and you may use any of them; these five are where this question
starts. The data dictionary, `briefs/C2_W03_D01_data_dictionary_STUDENT.md`, gives every column.

---

## Which ways could a group test the claim, and what does each cost?

**Who needs the answer.** Your group, on Monday, when it chooses how to spend Wednesday and Thursday.
A way that confirms the arithmetic of the 9 percent tells the marketing head nothing about whether
to spend more.

**The questions on the way.** What are the ways? How many rows does each touch, how many hours does
it take, and what can it get wrong? Which Week 1 or 2 move does each need?

The hours are estimates for a group of four working together, from the first file opened to a
checked number.

| Way | What the group does | Rows it touches | Hours | What it can get wrong | The Week 1 or 2 move it needs |
|---|---|---|---|---|---|
| A. Recompute the 9 percent | Works out bookings per patient over the weeks the offer ran, offered against everyone else | 2,381 offers, 6,700 patients and 11,882 booking rows | About 2 | Confirms the arithmetic and says nothing about cause | Week 1 Tuesday: confirm the number before explaining it |
| B. Compare before with during | Sets the offered patients' bookings in the weeks before the offer against the weeks it ran | As A | About 2 | Anything else that changed in those weeks, a season or a trend, reads as the offer's effect | Week 1 Thursday: cause or coincidence |
| C. Build a fair comparison | Checks how alike the offered and not-offered patients were before the offer, then compares like with like | As A, with the sites | About 5 | Can balance only what the files record, so anything else that differs between the two groups stays in the gap | Week 1 Thursday: is the split fair, and did the discount work |
| D. Ask whether chance could produce the gap | Shuffles the offered label many times and counts how often a gap this large appears by luck, a permutation test | As A | About 2, on top of A or C | Says whether the gap could be luck, never whether the offer caused it | Week 1 Thursday: real, or the wobble |

Which way leads, and which one checks it, is your group's call. Make it in Part 2 of the translation
worksheet, `briefs/C2_W03_D01_translation_worksheet_STUDENT.md`, before anyone opens a notebook, and
name the fact that would make you switch. Kavya Nair, the senior analyst on your team, will ask for
a second way to the same number, so the call needs two of these ways.

---

## What will the panel ask, and what does a finished answer look like?

**Who needs the answer.** Every member. The panel, the industry expert who hears Friday's
presentations, joined on Saturday by a senior industry leader, may put any question to anyone, and
presentation and defence is scored for each learner, so a member who knows only one slice of the
work loses those marks alone.

**The questions on the way.** Which questions will the panel ask? What earns full marks on each
criterion of the mini project, for this question?

### Which questions will the panel ask?

The panel reads your one-slide answer, then asks questions like these. Every member should be able
to answer each one from your own work.

1. Lifted against what? Whom did you compare with whom, and over which weeks?
2. Would the offered patients have booked anyway? What in your analysis answers that?
3. What else changed in the same weeks, and how did you rule it in or out?
4. If marketing ran the offer again, how should it be run so that the answer is clean?
5. Should the offer go to every patient in all six metros, and what is the caveat?

### What earns full marks on this question?

| Criterion | Marks | Full marks on this question look like |
|---|---|---|
| The question translated | 8 | "Lifted" is defined in a line, saying which groups are compared, on what, over which weeks, and the decision the answer feeds, extend, keep or stop the offer, is named |
| The data made trustworthy | 10 | The offer list, the patients and both booking files are profiled before anything is compared; every row removed or kept on purpose is in the decisions log with its reason; every patient in the comparison is counted once |
| The analysis | 10 | The comparison is shown to be fair, or its unfairness is named and dealt with, before the gap is read; a chance check says whether the gap could be luck |
| The claim | 6 | One sentence says whether the offer caused more bookings, by how much on which comparison, over which weeks, with its caveat and what the marketing head should do next |
| Presentation and defence | 6 | The notebook runs cold on the raw files in front of the panel, and every member can say why the two groups are, or are not, alike |

The rubric the panel scores against, as approved:

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

---

## What does your group ship, and when is each piece due?

**Who needs the answer.** Your group, today, so that nothing is built on Friday that should have
started on Monday.

**The questions on the way.** What does every group ship, and when is each piece seen? What happens
if the live demo fails? When are the mock interview and the group discussion, and what is each worth?

| What | What it holds | When it is seen |
|---|---|---|
| The translation worksheet | Dr Menon's question in your words, the method that leads, your vocabulary map, your first three moves, the cost of an error and your one-sentence scope | Monday's close, when each group reads its scope aloud |
| The challenges log | Every time the group was stuck, what you tried and what you decided, dated as it happened, in `briefs/C2_W03_D01_challenges_log_STUDENT.xlsx` | Entry one by Monday's close; read again in Thursday's viva |
| The decisions log | Every cleaning and matching call in the Week 1 Wednesday shape (field, issue, rows, decision, reason), with each file's rows reconciled, in `briefs/C2_W03_D01_decisions_log_STUDENT.xlsx` | Kept from your first cleaning call; scored in the mini project |
| The headline claim | One sentence with its number, denominator, period and caveat | Wednesday 21 October, at the day's close |
| The notebook or SQL | The code that reproduces every number on your slide from the raw files in `data/`, run top to bottom from a fresh start; a number the code does not produce is not in the answer | The live demo |
| The one-slide answer | The slide Dr Menon carries into her board meeting: the claim, the evidence, the caveat and the action | Your presentation |
| A presentation slot of 25 to 30 minutes | Your answer, a live demo run cold on your own copy of the files, and the panel's questions; every member answers | Friday 23 October where the roster allows, or Saturday 24 October |

### What happens if the live demo fails?

The demo runs once, cold, on the raw files. If it fails, your group has
two minutes to recover it live, as it would in front of a client. If it still fails, you present from
your executed notebook, and the panel scores the live demo, inside presentation and defence, as not
run cold. The other 34 marks are scored from the executed run, so a failed demo costs its own marks
and never the analysis.

### When are the mock interview and the group discussion, and what is each worth?

Both are scored for each learner alone, apart from the project. Mock R1, the first round of mock
interviews, is worth 30 marks and runs for every learner on Thursday 22 October: a technical half on
Weeks 1 and 2, and a viva, a spoken defence of your group's work. The group discussion is worth 30
marks; its rounds run on Friday 23 October and close on the morning of Saturday 24 October. The briefing note,
`briefs/C2_W03_D01_briefing_note_STUDENT.md`, carries their rubrics. Nothing new is taught this week:
everything the build needs is in your Weeks 1 and 2 notes, and a question about the domain, such as
what a phlebotomist does, is always fair to ask a trainer or a TA.
