# Brief 4: Is KH-ATL-03 really worse at no-shows than the other centres, before anyone adds staff or closes it?

**For:** the group or groups allocated sub-problem 4
**Client:** Dr Priya Menon, COO, Kalpa Health, and the patient service centres' operations head
**Data:** the ten files in `data/`, exported on Friday 16 October 2026

Kalpa Health and everyone in it are fictional, and every record in the files is synthetic.

> "KH-ATL-03, one of our two Atlanta patient service centres, has the worst no-show rate on my Q3
> report. I am being asked to add a receptionist there or close it. Is the centre really worse?"
> The patient service centres' operations head, Kalpa Health

**Who needs the answer.** The operations head, who decides between a second receptionist, new
reminder calls and a closure notice for KH-ATL-03. A centre closed on a rate read wrongly takes a
neighbourhood's nearest blood draw away from its patients; a real problem left alone keeps costing
slots every day.

**The questions on the way.** What has Dr Menon asked, and where does this question sit in it? What
do a visit, a no-show and a no-show rate mean at Kalpa Health? Which files hold the answer, and how
big is each? Which ways could a group test the centre's rate, and what does each cost? What will the
panel ask, and what does a finished answer look like? What does your group ship, and when?

---

## What has Dr Menon asked, and where does this question sit in it?

**Who needs the answer.** Your group, before it picks a way. The operations head's question is one of
five that together answer Dr Menon's, and a centre losing its booked patients is one of the places
her missing growth could be hiding.

**The questions on the way.** What business is Kalpa Health? What does Dr Menon see? Which five
questions did her heads ask, and which one is yours?

Kalpa Health runs a laboratory and two patient service centres, the places where a phlebotomist
draws a patient's blood, in each of six US metro areas: Dallas, Phoenix, New York, Chicago, Atlanta
and Philadelphia. It bills its patients' payers in dollars: commercial health plans, Medicare (the
federal programme for people aged 65 and over), Medicaid (each state's programme for people on low
incomes) and patients who pay for themselves (self-pay). Its revenue-cycle and analytics work runs
from Kalpa's Global Capability Centre (GCC) in Bengaluru, where you work as trainee engineers in the
data and AI team. It reports in calendar quarters: Q2 is April to June 2026 and Q3 is July to
September 2026.

Its COO, Dr Priya Menon, has written to the team. Her dashboard shows test volumes up 5 percent from
Q2 to Q3 against a plan of 18, and she cannot say which branch of the business is short. Five of her
heads have each asked her a question, and each group takes one.

| # | The question | Who asks |
|---|---|---|
| 1 | Where does our lab revenue come from, and which branch of it is short? | The finance head |
| 2 | Bookings fell in two metros in Q3: how far, and why? | The patient service centres' operations head |
| 3 | The claims and the posting system disagree: which claims are unpaid, and can the figure be trusted? | The finance head |
| **4** | **KH-ATL-03 has the worst no-show rate: is the centre really worse? (yours)** | **The patient service centres' operations head** |
| 5 | The free at-home collection offer "lifted bookings 9 percent": did it work? | The marketing head |

The operations head's monthly report ranks the twelve patient service centres by their no-show rate
for Q3, and KH-ATL-03 sits at the bottom. The centre's manager says its patients are no different
from anyone else's.

---

## What do a visit, a no-show and a no-show rate mean at Kalpa Health?

**Who needs the answer.** The operations head, who will staff or close a centre on the rate you
defend. A rate is a count over a denominator, and both halves are part of its definition.

**The questions on the way.** What is a visit at a patient service centre? What is a no-show? How
does the report work out the rate? What do a receptionist and a reminder call change?

| Word | What it means at Kalpa Health | Where it lives in the files |
|---|---|---|
| Patient service centre | A site where a phlebotomist draws patients' blood; each metro has two, beside its laboratory | `sites` |
| Visit | One entry in a centre's visit register, for one patient on one day | `appointments` |
| No-show | A visit the register marks as not attended | `appointments.attended` |
| No-show rate, as the report works it out | The share of a centre's Q3 visits that the register marks as not attended | Your group recomputes it from `appointments` |
| Receptionist and reminder call | The front desk, and the call or message that reminds a patient of a booked slot the day before; both cost staff time | Not in the files |

Whether the report's rate is the right one for the operations head's decision is part of what your
group decides. A missed blood draw can also mean a missed diagnosis, which is why a wrong answer here
can cost more than a slot.

---

## Which files hold the answer, and how big is each?

**Who needs the answer.** Your group, to plan its time. This question needs few rows, and the time it
saves on counting belongs to the thinking about what a fair comparison needs.

**The questions on the way.** Which files does the no-show question start from? How many rows does
each hold, and what is one row?

| File | One row is | Rows | Why it bears on this question |
|---|---|---|---|
| `appointments` | One visit, or one booked slot, at a patient service centre, Q3 only | 7,133 | Every visit, its centre, its day, its kind and whether the patient was seen |
| `sites` | One laboratory or patient service centre | 18 | Which metro each centre is in, and which sites are centres |

Every group holds all ten files, and you may use any of them; these two are where this question
starts. The data dictionary, `briefs/C2_W03_D01_data_dictionary_STUDENT.md`, gives every column.

---

## Which ways could a group test the centre's rate, and what does each cost?

**Who needs the answer.** Your group, on Monday, when it chooses how to spend Wednesday and Thursday.
A way that ranks the centres and stops hands the operations head the same report back with more
decimals.

**The questions on the way.** What are the ways? How many rows does each touch, how many hours does
it take, and what can it get wrong? Which Week 1 or 2 move does each need?

The hours are our estimate for a group of four working together, from first file opened to a
checked number.

| Way | What the group does | Rows it touches | Hours | What it can get wrong | The Week 1 or 2 move it needs |
|---|---|---|---|---|---|
| A. Rank the twelve centres on the report's rate | Recomputes each centre's rate the way the report does and acts on the worst | 7,133 visits | Under 1 | Takes the report's denominator and its gap as given, and checks neither | Week 2 Thursday: grouping a count by centre |
| B. Recompute every rate on a definition you state and defend | Decides what each rate is out of, then compares KH-ATL-03 with the other eleven centres on that definition | 7,133 visits and 18 sites | About 2 | A rate on a fair definition can still differ by chance at a small centre, and this way says nothing about chance | Week 1 Monday: a metric defined before it is counted; Week 1 Thursday: how many people stand behind a percentage |
| C. Ask whether chance could produce the gap | On the chosen definition, works out how often a centre with KH-ATL-03's number of visits would sit this far from the others by luck alone, with a permutation or binomial check | 7,133 visits | About 3, with B | Answers real or noise on whatever definition is fed into it, so a wrong denominator gets a confident answer | Week 1 Thursday: real, or the wobble, and is it worth acting on |
| D. Check the comparison is fair before running it | Lists what else differs between KH-ATL-03 and the other centres, in every column the register carries, and compares like with like | 7,133 visits and 18 sites | About 2 | Can only rule out what the register records; a patient's own reason for missing a slot is not in the files | Week 1 Thursday: is the split fair, and do the two groups differ only in the thing tested |

Which way leads, and which one checks it, is your group's call. Make it in Part 2 of the translation
worksheet, `briefs/C2_W03_D01_translation_worksheet_STUDENT.md`, before anyone opens a notebook, and
name the fact that would make you switch. Kavya Nair, the senior analyst on your team, will ask for
a second way to the same number, so the call needs two of these ways.

---

## What will the panel ask, and what does a finished answer look like?

**Who needs the answer.** Every member, since the panel may put any question to anyone. A group that
knows only its own slice of the work loses marks one learner at a time.

**The questions on the way.** Which questions will the panel ask? What earns full marks on each
criterion of the mini project, for this question?

### Which questions will the panel ask?

The panel reads your one-slide answer, then asks questions like these. Every member should be able
to answer each one from your own work.

1. What is KH-ATL-03's no-show rate, on what denominator, and against which comparison?
2. Could chance alone produce the gap you see? How did you check, and what did the check say?
3. What would a fair comparison between two centres need, and did yours have it?
4. What should the operations head do about KH-ATL-03, and what evidence would change your advice?
5. If a patient's missed draw meant a missed diagnosis, what would you want checked before acting?

### What earns full marks on this question?

| Criterion | Marks | Full marks on this question look like |
|---|---|---|
| The question translated | 8 | The no-show rate is defined in a line, saying what it counts and what it is out of, and the decision the answer feeds, a receptionist, reminder calls or a closure, is named |
| The data made trustworthy | 10 | The visit register is profiled before any rate is worked out; every row removed or kept on purpose is in the decisions log with its reason; the visits behind every rate reconcile to the register's rows |
| The analysis | 10 | KH-ATL-03 is compared with the other centres on a denominator the group defends, the comparison is shown to be fair, and a chance check says whether the gap could be luck |
| The claim | 6 | One sentence gives KH-ATL-03's rate and the others', on which denominator, for Q3, whether chance could produce the gap, the caveat, and what the operations head should do |
| Presentation and defence | 6 | The notebook runs cold on the raw files in front of the panel, and every member can defend the denominator |

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

**The questions on the way.** What does every group ship? When is each piece seen? What happens if
the live demo fails?

| What | What it holds | When it is seen |
|---|---|---|
| The translation worksheet | Dr Menon's question in your words, the method that leads, your vocabulary map, your first three moves, the cost of an error and your one-sentence scope | Monday's close, when each group reads its scope aloud |
| The challenges log | Every time the group was stuck, what you tried and what you decided, dated as it happened, in `briefs/C2_W03_D01_challenges_log_STUDENT.xlsx` | Entry one by Monday's close; read again in Thursday's viva |
| The decisions log | Every cleaning and matching call in the Week 1 Wednesday shape (field, issue, rows, decision, reason), with each file's rows reconciled, in `briefs/C2_W03_D01_decisions_log_STUDENT.xlsx` | Kept from your first cleaning call; scored in the mini project |
| The headline claim | One sentence with its number, denominator, period and caveat | Wednesday 21 October, at the day's close |
| The notebook or SQL | The code that reproduces every number on your slide from the raw files in `data/`, run top to bottom from a fresh start; a number the code does not produce is not in the answer | The live demo |
| The one-slide answer | The slide Dr Menon carries into her board meeting: the claim, the evidence, the caveat and the action | Your presentation |
| A presentation slot of 25 to 30 minutes | Your answer, a live demo run cold on your own copy of the files, and the panel's questions; every member answers | Friday 23 October where the roster allows, or Saturday 24 October |

**If the live demo fails.** The demo runs once, cold, on the raw files. If it fails, your group has
two minutes to recover it live, as it would in front of a client. If it still fails, you present from
your executed notebook, and the panel scores the live demo, inside presentation and defence, as not
run cold. The other 34 marks are scored from the executed run, so a failed demo costs its own marks
and never the analysis.

The mock interview (30 marks) and the group discussion (30 marks) are scored apart from the project:
Mock R1 runs for every learner on Thursday 22 October, and the group discussion rounds run on Friday
23 October and close on the morning of Saturday 24 October. The briefing note,
`briefs/C2_W03_D01_briefing_note_STUDENT.md`, carries their rubrics. Nothing new is taught this week:
everything the build needs is in your Weeks 1 and 2 notes, and a question about the domain, such as
what a phlebotomist does, is always fair to ask a trainer or a TA.
