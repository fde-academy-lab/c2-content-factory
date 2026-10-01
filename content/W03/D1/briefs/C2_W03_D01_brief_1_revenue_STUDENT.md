# Brief 1: Which branch of Kalpa Health's billed revenue is short of the plan, and by how much?

- **For:** the group or groups allocated sub-problem 1
- **Client:** Dr Priya Menon, chief operating officer (COO) of Kalpa Health, and the finance head
- **Data:** the ten files in `data/`, exported on Friday 16 October 2026

Kalpa Health and everyone in it are fictional, and every record in the files is synthetic.

> "The board will ask me where the plan's growth went. Where does our lab revenue actually come
> from, and which branch of it is short?"
> The finance head, Kalpa Health

**Who needs the answer.** The finance head, who writes the board's page on where the plan's growth
went, and Dr Menon, who moves the recovery effort for the second half of the year onto the branch
you name. A branch
named wrongly sends staff and money to a part of the business that was never short, while the part
that is short keeps falling.

**The questions on the way.** What has Dr Menon asked, and where does this question sit in it? What
do revenue, a test and a branch mean at Kalpa Health? Which files hold the answer, and how big is
each? Which ways could a group find the short branch, and what does each cost? What will the panel
ask, and what does a finished answer look like? What does your group ship, and when?

---

## What has Dr Menon asked, and where does this question sit in it?

**Who needs the answer.** Your group, before it picks a way. The finance head's question is one of
five that together answer Dr Menon's, and an answer that ignores the other four repeats work or
contradicts it.

**The questions on the way.** What business is Kalpa Health? What does Dr Menon see? Which five
questions did her heads ask, and which one is yours? Which real company faces the same question?

Kalpa Health runs a laboratory, which runs the tests, and two patient service centres, where a
phlebotomist draws patients' blood, in each of six US metro areas: Dallas, Phoenix, New York,
Chicago, Atlanta and Philadelphia. Patients book at all eighteen sites. It bills its patients' payers in dollars: commercial health plans, Medicare (the
federal programme for people aged 65 and over), Medicaid (each state's programme for people on low
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
| **1** | **Where does our lab revenue come from, and which branch of it is short? (yours)** | **The finance head** |
| 2 | Bookings fell in two metros in Q3: how far, and why? | The patient service centres' operations head |
| 3 | The claims and the posting system disagree: which claims are unpaid, and can the figure be trusted? | The finance head |
| 4 | KH-ATL-03 has the worst no-show rate: is the centre really worse? | The patient service centres' operations head |
| 5 | The free at-home collection offer "lifted bookings 9 percent": did it work? | The marketing head |

Yours is the question nearest to Dr Menon's own: the other four each look at one part of the
business, and yours asks which part is short.

### Which real company faces the same question?

Quest Diagnostics, a US laboratory company with $11,035 million of net revenues in 2025, judges its
testing business on "volume (measured by test requisitions) and revenue per requisition", and its
management uses the two to understand "trends affecting number of requisitions, pricing and test
mix" (Form 10-K for 2025). A requisition is a doctor's order for tests, close to a Kalpa Health
booking.

---

## What do revenue, a test and a branch mean at Kalpa Health?

**Who needs the answer.** Everyone who reads your slide. The finance head says "revenue", Dr Menon's
dashboard says "test volumes", and a group that silently swaps one for the other answers a question
neither of them asked.

**The questions on the way.** What is billed revenue, and how does it differ from money collected?
What are a booking, a test and a panel? What is a branch of a revenue tree?

| Word | What it means at Kalpa Health | Where it lives in the files |
|---|---|---|
| Booking | One patient's visit to have one or more tests or panels done | `bookings_legacy`, `bookings_newsys` |
| Test | One laboratory test, such as a complete blood count or vitamin D | `test_catalogue`, `booking_tests` |
| Panel | Several tests ordered and priced under one name, such as the diabetes monitoring panel; its price is its own, below the sum of its tests' prices | `test_catalogue`, `booking_tests` |
| Claim | The bill Kalpa Health sends to a payer for a completed booking, at list prices, plus any collection fee for a home draw | `claims` |
| Payer | Whoever pays a claim: a commercial plan, Medicare, Medicaid or the patient (self-pay) | `claims.payer_type`, `claims.payer_id` |
| Billed revenue, or gross charges | The dollars on the claims: list prices, plus any collection fee | `claims.billed_amount` |
| Allowed amount | What a payer's contract permits for a claim, payer's and patient's shares together; it is usually well below the billed amount, and the difference is written off under the contract | `remittances.allowed_amount` |
| Branch | One part of a revenue tree: a count or a ratio whose change from Q2 to Q3 shows how much of revenue's growth it carries | Built by your group |

Billed revenue is what Kalpa Health charges, at list prices, plus any collection fee for a home draw, and the money that arrives is a smaller
figure set by the payers' contracts. Both are honest numbers for different decisions, so your group
says which one each branch is measured in. The board's 18 percent is a plan for test volumes; with
prices and the mix of tests unchanged, billed revenue would grow about as fast as volumes, so the
finance head reads each branch by how much of the shortfall against that plan it explains. The
domain dossier,
`study-notes/C2_W03_D01_domain_us_healthcare_STUDENT.md`, follows one claim from the list price to
the cash in its section 3, for more depth.

---

## Which files hold the answer, and how big is each?

**Who needs the answer.** Your group, to plan its time. A way that touches every row of every file
costs a day; one that touches a single file costs an hour.

**The questions on the way.** Which files does the revenue question start from? How many rows does
each hold, and what is one row?

| File | One row is | Rows | Why it bears on this question |
|---|---|---|---|
| `claims` | One claim | 11,356 | The billed dollars, by payer, metro and service date |
| `booking_tests` | One test, panel, or test inside a panel, on a booking | 51,456 | What was booked on each booking, and at what price |
| `test_catalogue` | One test or panel on the price list | 16 | List prices, and which codes are panels |
| `bookings_legacy` | One booking in the booking system in use since before Q2 | 11,729 | Bookings, patients, sites, channels and dates |
| `bookings_newsys` | One booking in the new booking system | 153 | The same, in the new system's codes |
| `patients` | One registered patient | 6,700 | Who the patients are, and who pays for them |
| `sites` | One laboratory or patient service centre | 18 | Which metro each site is in |

Every group holds all ten files, and you may use any of them; these seven are where this question
starts. The data dictionary, `briefs/C2_W03_D01_data_dictionary_STUDENT.md`, gives every column.

---

## Which ways could a group find the short branch, and what does each cost?

**Who needs the answer.** Your group, on Monday, when it chooses how to spend Wednesday and Thursday.
A way chosen for being familiar can burn the build week on an answer the finance head cannot use.

**The questions on the way.** What are the ways? How many rows does each touch, how many hours does
it take, and what can it get wrong? Which Week 1 or 2 move does each need?

The hours are estimates for a group of four working together, from the first file opened to a
checked number.

| Way | What the group does | Rows it touches | Hours | What it can get wrong | The Week 1 or 2 move it needs |
|---|---|---|---|---|---|
| A. Total the billed dollars | Sums the billed dollars on the claims for Q2 and for Q3 and compares their growth with the plan | 11,356 claims | About 1 | Says whether billed dollars grew and never which branch is short, and dollars are not the volume the plan counts | Week 1 Monday: which total is sales, and what each total counts |
| B. Split the dollars by payer and by single test against panel | Totals billed dollars for each payer type and for single tests against panels, in each quarter | 11,356 claims and 51,456 booking lines | About 3 | Shows where the dollars sit; a change in the mix reads like a change in volume unless both quarters are split on the same definitions | Week 1 Tuesday: which segment moved, and did customers pay more or did the mix change; Week 2 Thursday: grouping in pandas |
| C. Build a revenue tree | Splits billed revenue into a product of counts and ratios the group defines, for Q2 and for Q3, and finds the branch whose change explains most of the shortfall | All seven files, about 81,000 rows | About 6 | Is only as right as each box's definition, and every box must be counted the same way in both quarters | Week 1 Monday: the revenue tree, every branch a count over a denominator; Week 2 Monday: the tree as queries |
| D. Rebuild Dr Menon's 5 percent first, then the tree | Reproduces her dashboard's figure from the files before walking the tree, so the tree starts from the number she quotes | As C | About 7 | Costs an hour more than C, and reproduces the dashboard's own way of counting, right or wrong, until the group writes its own beside it | Week 1 Tuesday: confirm the number before explaining it; Week 1 Monday: which total, and what it counts |

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

1. Which branch of Kalpa Health's billed revenue is short, and how much of the shortfall does it
   explain?
2. How did you define each box of your answer, and why that definition?
3. How do your numbers reconcile to the files you were given?
4. What would change your answer?
5. Say your answer in one sentence Dr Menon can carry to the board, with its denominator and its
   caveat.

### What earns full marks on this question?

| Criterion | Marks | Full marks on this question look like |
|---|---|---|
| The question translated | 8 | "Revenue" and "test volumes" are each defined in a line, saying what is counted and in which quarters, and the decision the answer feeds, where the recovery effort goes, is named |
| The data made trustworthy | 10 | Every file the tree uses is profiled first; every row removed, converted or kept on purpose is in the decisions log with its reason; the tree's numbers reconcile to the files they come from, quarter by quarter |
| The analysis | 10 | The tree runs from billed revenue down to the branch whose change explains most of the shortfall, every box a count over a stated denominator and both quarters counted the same way |
| The claim | 6 | One sentence names the branch, how much of the shortfall it explains, on which denominator, for Q2 to Q3, with its caveat and one action Dr Menon can take |
| Presentation and defence | 6 | The notebook runs cold on the raw files in front of the panel, and every member can defend the group's definitions |

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
