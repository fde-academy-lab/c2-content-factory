# Brief 2: How far did bookings really fall in the two metros, and why, before anyone moves staff?

- **For:** the group or groups allocated sub-problem 2
- **Client:** Dr Priya Menon, chief operating officer (COO) of Kalpa Health, and the patient service centres' operations head
- **Data:** the ten files in `data/`, exported on Friday 16 October 2026

Kalpa Health and everyone in it are fictional, and every record in the files is synthetic.

> "Bookings fell in two of our metros in Q3. Before I send a field team or cut staff there, I need to
> know how far they fell, and why."
> The patient service centres' operations head, Kalpa Health

**Who needs the answer.** The operations head, who decides this month whether to send a field team
to the two metros, cut staff there, or leave them alone. A fall read too large cuts staff that
patients still need; a fall read too small leaves a real decline running for another quarter.

**The questions on the way.** What has Dr Menon asked, and where does this question sit in it? What
do a booking and a fall mean at Kalpa Health? Which files hold the answer, and how big is each?
Which ways could a group size the fall and explain it, and what does each cost? What will the panel
ask, and what does a finished answer look like? What does your group ship, and when?

---

## What has Dr Menon asked, and where does this question sit in it?

**Who needs the answer.** Your group, before it picks a way. The operations head's question is one
of five that together answer Dr Menon's, and a fall in bookings is one of the places her missing
growth could be hiding.

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
| **2** | **Bookings fell in two metros in Q3: how far, and why? (yours)** | **The patient service centres' operations head** |
| 3 | The claims and the posting system disagree: which claims are unpaid, and can the figure be trusted? | The finance head |
| 4 | KH-ATL-03 has the worst no-show rate: is the centre really worse? | The patient service centres' operations head |
| 5 | The free at-home collection offer "lifted bookings 9 percent": did it work? | The marketing head |

The operations head's report shows bookings down in two of the six metros from Q2 to Q3, with the
other four holding or growing, and the operations head wants to act on it this month. Which two
metros they are is the first thing your group finds in the files.

### Which real company faces the same question?

Quest Diagnostics, a US laboratory company with about 2,400 patient service centres, measures its
volume by test requisitions, a doctor's order for tests and close to a Kalpa Health booking, and
reports the change in requisition volume each year beside its revenue (Form 10-K for 2025).

---

## What do a booking and a fall mean at Kalpa Health?

**Who needs the answer.** The operations head, who will move people on your number. "Bookings fell"
can mean fewer patients, fewer visits each, more cancellations or a different count, and each one
calls for a different action.

**The questions on the way.** What is a booking, and when is it completed or cancelled? How does a
patient book? What do a metro and a site mean here? What is a field team for?

| Word | What it means at Kalpa Health | Where it lives in the files |
|---|---|---|
| Booking | One patient's visit to have one or more tests or panels done | `bookings_legacy`, `bookings_newsys` |
| Completed or cancelled | Whether the visit happened or was called off before the draw | `bookings_legacy.status`, `bookings_newsys.state` |
| Channel | How the patient booked: walking in, online, by phone, or for a collection at home, when a phlebotomist visits the patient | `bookings_legacy.channel`, `bookings_newsys.channel` |
| Metro | One of the six US metro areas Kalpa Health works in | `metro` in most files |
| Site | A laboratory, which runs the tests, or a patient service centre, where blood is drawn; each metro has one laboratory and two centres | `sites` |
| Patient | A person in Kalpa Health's patient register, with a metro, an age band and a payer | `patients` |
| Field team | Operations staff sent to a metro to find out on the ground what is happening, at a cost in time and travel | Not in the files |

A fall is a change from Q2 to Q3 in a count your group defines, in writing, before anything is
counted: what one booking is and which bookings count.

---

## Which files hold the answer, and how big is each?

**Who needs the answer.** Your group, to plan its time. A recount of the two booking files takes about two hours, and a
full ladder takes most of Wednesday.

**The questions on the way.** Which files does the bookings question start from? How many rows does
each hold, and what is one row?

| File | One row is | Rows | Why it bears on this question |
|---|---|---|---|
| `bookings_legacy` | One booking in the booking system in use since before Q2 | 11,729 | Bookings by metro, site, channel, status and date |
| `bookings_newsys` | One booking in the new booking system | 153 | Bookings in the new system's own codes |
| `sites` | One laboratory or patient service centre | 18 | Each site's metro, and its code in each booking system |
| `patients` | One registered patient | 6,700 | Patients per metro, with their age band and payer |
| `booking_tests` | One test, panel, or test inside a panel, on a booking | 51,456 | What each booking was for |
| `claims` | One claim, the bill for one completed booking | 11,356 | A second count of completed bookings, by metro and service date |

Every group holds all ten files, and you may use any of them; these six are where this question
starts. The data dictionary, `briefs/C2_W03_D01_data_dictionary_STUDENT.md`, gives every column.

---

## Which ways could a group size the fall and explain it, and what does each cost?

**Who needs the answer.** Your group, on Monday, when it chooses how to spend Wednesday and Thursday.
The operations head wants to act this month, and a way that explains a fall before sizing it hands
them a story about a number nobody has checked.

**The questions on the way.** What are the ways? How many rows does each touch, how many hours does
it take, and what can it get wrong? Which Week 1 or 2 move does each need?

The hours are estimates for a group of four working together, from the first file opened to a
checked number.

| Way | What the group does | Rows it touches | Hours | What it can get wrong | The Week 1 or 2 move it needs |
|---|---|---|---|---|---|
| A. Explain the report's fall | Takes the report's fall as given and looks for causes: a competitor, staffing, the season | None | About 2 | Explains a fall nobody has confirmed, so a convincing cause can sit on a number that is wrong | The one Week 1 Tuesday warns against: a reason found before rung 1 |
| B. Recount bookings by metro and quarter | Counts one row per booking, Q2 against Q3, the same way for every metro | 11,882 booking rows and 18 sites | About 2 | Is only as right as its definition of one booking; it sizes the fall and says nothing of why | Week 1 Tuesday: is the drop real?; Week 1 Wednesday: profile before you count |
| C. Walk the investigation ladder | Climbs the Week 1 Tuesday ladder rung by rung on the booking files, from confirming the fall to testing a cause | About 18,600 rows across the booking files, patients and sites | About 6 | Costs the most time, and every rung above the first rests on the count rung 1 confirms | Week 1 Tuesday: the ladder, all five rungs |
| D. Count completed bookings a second way | Counts the completed bookings the claims bill, by metro and quarter, against the booking files' count | 11,356 claims | About 1, on top of B or C | Claims exist only for completed bookings, so cancellations never show; it checks a count and cannot replace one | Week 2 Thursday: the same number reached a second way |

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

1. Which two metros fell, and how far did bookings fall in each, on what count?
2. How many bookings did you count in each quarter, and how does that count reconcile to the rows you
   were given?
3. What did you check before you started explaining the fall?
4. Which step of your investigation changed your answer most, and what did it change it from?
5. What should the operations head do next week, and what would change your advice?

### What earns full marks on this question?

| Criterion | Marks | Full marks on this question look like |
|---|---|---|
| The question translated | 8 | "Bookings" and "fell" are defined in a line each, saying what one booking is and which bookings count, and the decision the answer feeds, a field team, a staff cut or neither, is named |
| The data made trustworthy | 10 | Every booking file is profiled before it is counted; every row removed or kept on purpose is in the decisions log with its reason; the booking count reconciles to the rows of every file it was counted from |
| The analysis | 10 | The fall is confirmed for each metro on the stated definition, like with like, then split down to the sites, channels or patients that carry it, before any cause is offered |
| The claim | 6 | One sentence gives how far each metro fell, on which count, for Q2 to Q3, with its caveat and what the operations head should do |
| Presentation and defence | 6 | The notebook runs cold on the raw files in front of the panel, and every member can say what was checked before the fall was explained |

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
