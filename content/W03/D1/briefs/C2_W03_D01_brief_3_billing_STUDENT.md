# Brief 3: Which claims are still unpaid, how many dollars is that, and can finance trust the figure?

- **For:** the group or groups allocated sub-problem 3
- **Client:** Dr Priya Menon, chief operating officer (COO) of Kalpa Health, and the finance head
- **Data:** the ten files in `data/`, exported on Friday 16 October 2026

Kalpa Health and everyone in it are fictional, and every record in the files is synthetic.

> "The claims we billed say one thing and the posting system says another. Which claims are unpaid,
> how much money is that, and can I trust the figure I report?"
> The finance head, Kalpa Health

**Who needs the answer.** The finance head, who reports the collections figure at the quarter's close
and decides which unpaid claims the revenue-cycle team chases first and whether any are written off.
A figure wrong in either direction reaches the board under the finance head's name, and a claim
chased late can pass its payer's filing deadline and never be paid.

**The questions on the way.** What has Dr Menon asked, and where does this question sit in it? What
do a claim, a remittance and a posting mean, and when is a claim unpaid? Which files hold the
answer, and how big is each? Which ways could a group find the unpaid claims, and what does each
cost? What will the panel ask, and what does a finished answer look like? What does your group ship,
and when?

---

## What has Dr Menon asked, and where does this question sit in it?

**Who needs the answer.** Your group, before it picks a way. The finance head's question is one of
five that together answer Dr Menon's, and every other group's dollar figure is only as good as the
money your group can show arrived.

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
| **3** | **The claims and the posting system disagree: which claims are unpaid, and can the figure be trusted? (yours)** | **The finance head** |
| 4 | KH-ATL-03 has the worst no-show rate: is the centre really worse? | The patient service centres' operations head |
| 5 | The free at-home collection offer "lifted bookings 9 percent": did it work? | The marketing head |

The billing system and the posting system give different totals for the same two quarters, and the
finance head cannot say which claims make up the difference.

### Which real company faces the same question?

Quest Diagnostics names "reducing denials and patient concessions" among its areas of focus, and
reports its days sales outstanding, "a measure of billing and collection efficiency", at 48 days at
the end of 2025 (Form 10-K for 2025). In India, firms such as AGS Health, with more than 15,000
revenue-cycle professionals worldwide and centres in Chennai, Hyderabad and Bengaluru among other cities, sell
billing, coding and denial management to US hospitals and health systems (AGS Health, company page).

---

## What do a claim, a remittance and a posting mean, and when is a claim unpaid?

**Who needs the answer.** The finance head, whose figure your definitions decide. A claim the
contract never meant to pay in full is not unpaid, and a group that counts every short claim as
unpaid hands finance a debt that does not exist.

**The questions on the way.** How does a claim become cash at a US lab? What does each posting
record? What does the contract take away before anyone pays? Which claims count as unpaid?

A US lab bills its list price, and almost nobody pays it. Each payer's contract sets an allowed
amount for each test; the difference between the bill and the allowed amount is a contractual
adjustment, which the lab agreed never to collect. The allowed amount then splits into the payer's
share and the patient's. One worked example from the domain dossier: a commercial patient's two tests
billed at $135 had an allowed amount of $70.20, so $64.80 was written off under the contract; the
plan paid $56.16 and the patient owed $14.04.

| Word | What it means at Kalpa Health | Where it lives in the files |
|---|---|---|
| Claim | The bill for one completed booking, sent to its payer at list prices, plus any collection fee for a home draw | `claims` |
| Remittance | The payer's answer to a claim: what it allows, pays and refuses, and what the patient owes; a remittance that arrives as an electronic file is an ERA | `remittances` |
| Posting | One row the posting system records against a claim: money received, a denial, or money taken back | `remittances.posting` |
| Allowed amount | What the payer's contract permits for the claim, its share and the patient's together | `remittances.allowed_amount` |
| Contractual adjustment | The bill less the allowed amount, written off under the contract and never owed | `remittances.adjustment_amount`, with group `CO`, a contractual obligation |
| Patient responsibility | What the patient owes, such as coinsurance, a share of the allowed amount | `remittances.patient_responsibility` |
| Denial | A payer's decision, after processing, not to pay a claim; it carries one of seven reason categories | `remittances.posting`, `claims.denial_category` |
| Reversal | A posting that takes money back from an earlier payment | `remittances.posting` |
| Filing deadline | The time after the service date within which the payer must receive the claim, after which it need not pay | Not in the files |

Which claims count as unpaid, part paid, paid and denied is a definition your group writes down
before it counts, with the dollars each class holds. The domain dossier,
`study-notes/C2_W03_D01_domain_us_healthcare_STUDENT.md`, follows one claim from the bill to the cash
in its sections 3 and 5, for more depth.

---

## Which files hold the answer, and how big is each?

**Who needs the answer.** Your group, to plan its time. Two files of eleven thousand rows each are
small enough to match row by row, and a match that is not checked is wrong in a direction nobody
sees.

**The questions on the way.** Which files does the billing question start from? How many rows does
each hold, and what is one row?

| File | One row is | Rows | Why it bears on this question |
|---|---|---|---|
| `claims` | One claim | 11,356 | What was billed, to which payer, for which service date |
| `remittances` | One posting | 11,343 | What each payer or desk allowed, paid, denied or took back, and when it was recorded |
| `patients` | One registered patient | 6,700 | Each patient's payer |
| `bookings_legacy` | One booking in the booking system in use since before Q2 | 11,729 | The booking behind each claim |
| `bookings_newsys` | One booking in the new booking system | 153 | The same, in the new system's codes |

Every group holds all ten files, and you may use any of them; these five are where this question
starts. The postings run up to the export on Friday 16 October 2026, and a payer usually answers a
claim some weeks after the service, so the newest claims have had the least time for an answer. The
data dictionary,
`briefs/C2_W03_D01_data_dictionary_STUDENT.md`, gives every column.

---

## Which ways could a group find the unpaid claims, and what does each cost?

**Who needs the answer.** Your group, on Monday, when it chooses how to spend Wednesday and Thursday.
Finance needs a list of claims with dollars beside them, and a way that ends on two totals cannot
produce one.

**The questions on the way.** What are the ways? How many rows does each touch, how many hours does
it take, and what can it get wrong? Which Week 1 or 2 move does each need?

The hours are estimates for a group of four working together, from the first file opened to a
checked number.

| Way | What the group does | Rows it touches | Hours | What it can get wrong | The Week 1 or 2 move it needs |
|---|---|---|---|---|---|
| A. Compare the two totals | Sets billed dollars on the claims against paid dollars in the postings, quarter by quarter | 11,356 claims and 11,343 postings | About 1 | The gap mixes dollars the contracts never meant to pay with dollars still owed, and it names no claim | Week 1 Wednesday: the bridge that names every dollar between two totals |
| B. Match every posting to its claim, then classify every claim | Attaches postings to claims, counts what matched before any sum, then labels each claim paid, part paid, denied or with no posting | 11,356 claims and 11,343 postings | About 6 | Is only as right as the match, and a match nobody counted before and after can be wrong in either direction without a warning | Week 2 Tuesday: attach, count, explain the difference, then sum; Week 1 Wednesday: reconcile |
| C. Reconcile payer by payer first | Totals billed, allowed and paid for each payer and quarter, then matches claim by claim only where a payer's figures do not add up | 11,356 claims and 11,343 postings | About 4 | A payer can balance in total while single claims inside it are wrong, so unpaid claims can hide inside a payer that looks clean | Week 2 Thursday: grouping; Week 2 Friday: the pivot, before Week 2 Tuesday's join |
| D. Trace a sample of claims by hand | Picks 50 claims at random and follows each one through the posting system | 50 claims, looked up in 11,343 postings | About 2 | Gives a feel for how the two files relate and an estimate with a margin, never the list of unpaid claims finance needs | Week 1 Wednesday: profile before you touch; Week 1 Thursday: how far a sample can be off |

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

1. How many claims are paid, part paid, denied and unpaid, and how many dollars does each class hold?
2. How did you match a posting to its claim, and how do you know the match is right?
3. Where did every posting row go? Show rows in against rows matched, set aside and unexplained.
4. Which collections figure should the finance head report, and which caveat travels with it?
5. What would you ask the data team to change at the source, so the next close is easier?

### What earns full marks on this question?

| Criterion | Marks | Full marks on this question look like |
|---|---|---|
| The question translated | 8 | Paid, part paid, denied and unpaid are each defined in a line, collections is defined, and the decisions the answer feeds, the figure finance reports and the claims chased first, are named |
| The data made trustworthy | 10 | Both files are profiled before any match; every posting is accounted for, rows in equal rows matched plus rows set aside, none unexplained; every call is in the decisions log with its reason |
| The analysis | 10 | Every claim is classified with its dollars, and the gap between billed and paid is split into what the contracts never meant to pay, what was denied and what is still owed |
| The claim | 6 | One sentence gives the collections figure, the unpaid claims and their dollars, for which quarters, with its caveat and the first action for the revenue-cycle team |
| Presentation and defence | 6 | The notebook runs cold on the raw files in front of the panel, and every member can show how a posting finds its claim |

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
