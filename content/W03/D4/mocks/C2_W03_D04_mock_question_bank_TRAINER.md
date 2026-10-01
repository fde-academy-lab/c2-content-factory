# Which Week 1 and 2 questions does Mock R1's technical half ask, and what does a full-marks answer sound like?

**TRAINER ONLY.** The assessors keep this page. Nothing on it reaches a learner, before or after the
mock.

**Who needs the answer.** The three assessors, the Programme Head and the Academic TA in person and
the Principal Advisor online, who each run about twelve nine-minute technical halves on Thursday 22
October. Each half scores 15 of the mock's 30 marks, and an assessor who improvises a question, or
asks one about a group's own files, scores something the rubric does not ask for and can hand a
learner a finding their group has not reached yet.

**The questions on the way.** How is the half scored, and which criteria does each question feed?
Which three questions does a learner meet, and why those three? Why is every question set in a corner
of Kalpa Health that no group's data covers? How far above a definitional screen does each question
sit? Then, family by family, one question per taught day of Weeks 1 and 2, each at three levels.

Kalpa Health is a US diagnostics business with a laboratory and two patient service centres, where a
phlebotomist draws a patient's blood, in each of six US metro areas. It bills each patient's payer in
dollars: a commercial health plan, Medicare (the federal programme for people aged 65 and over and
some younger people with disabilities), Medicaid (each state's programme for people on low incomes)
or the patient (self-pay). A claim is the bill the lab sends a payer, and a remittance is the payer's
answer, saying what it paid and why. Its analytics and revenue-cycle work runs from Kalpa's Global
Capability Centre (GCC) in Bengaluru, the offshore centre where the learners are trainee engineers.
Its chief operating officer (COO), Dr Priya Menon, has asked why test volumes grew 5 percent from Q2
to Q3 of 2026 against a plan of 18. Each of the nine groups answers one of her heads' five questions,
its sub-problem, from ten data files exported on 16 October 2026: 1 revenue, 2 bookings, 3 billing,
4 no-shows and 5 the free at-home collection offer. The viva half, on the group's own work, is in
`C2_W03_D04_viva_prompts_TRAINER.md`, and the huddle before the first mock and the evidence note, the
assessor's written record of each mock, are in `C2_W03_D04_assessors_guide_TRAINER.md`.

---

## How is the technical half scored, and which criteria does each question feed?

**Who needs the answer.** Each assessor, before the first mock. The three criteria are scored
together at the end of the half, from the evidence note, so an assessor who marks question by question
as the half runs has no room left to weigh one weak answer against two strong ones.

**The questions on the way.** Which criteria does the half carry? Which part of a bank entry sets the
bar for each?

The half carries three of the six criteria of the rubric approved on 29 September 2026 and held in
`data/programme/facts.yaml`:

<!-- sync:rubric:W03/mock -->
**Mock interview R1, 30 marks.** Each learner is scored alone, 15 marks on the technical half and 15 on the project viva.

| Half | Criterion | Marks |
|---|---|---|
| Technical | Correctness | 8 |
| Technical | Reasoning aloud with numbers | 4 |
| Technical | Handling a follow-up | 3 |
| Project viva | The translation, with one decision defended by evidence | 6 |
| Project viva | Defending a caveat under challenge | 6 |
| Project viva | What they would do differently | 3 |
<!-- /sync:rubric:W03/mock -->

| Criterion | The part of each bank entry that sets its bar |
|---|---|
| Correctness, 8 | The model answer: the move named and applied, with the mechanism behind the number |
| Reasoning aloud with numbers, 4 | The numbers inside the model answer, said unprompted, each with its denominator |
| Handling a follow-up, 3 | The follow-up and what it separates: an answer that moves one step past the first one |

Every question feeds all three criteria. The half has three questions, so a learner who gets one
wrong can still earn most of the correctness marks on the other two.

---

## Which three questions does a learner meet, and why those three?

**Who needs the answer.** The assessor at the huddle, who opens only the three questions the roster's
Grid prints for each learner, and the Programme Head, who rebuilds the roster if the groups change.
A question that rehearses a learner's own viva minutes before it spends the half on evidence the viva
gathers anyway.

**The questions on the way.** What does each level ask for? Which taught day does each family come
from? Which set does a learner meet? Which questions are swapped for a learner whose group works close
to them? What are the reserves for?

| Level | What it asks for | What an understood answer shows |
|---|---|---|
| L1, the move | The method named and applied to a business ask | The learner states the move and its first check without prompting |
| L2, the number | A plausible wrong number on the table, and what produced it | The learner names the mechanism that made the number, the check that catches it and the fix |
| L3, the judgement | A stakeholder pushing back, or a design call to make and defend | The learner weighs two or more ways, sizes them, holds a position with a number and names the fact that would change it |

Ten families cover the fortnight, one per taught day, and each carries one question per level, so the
bank holds thirty. Each question keeps the tag its anchor carries on that day's row of the
programme's curriculum tracker, where the anchor is the interview question the row names: `[S]` a
staple asked everywhere, `[F]` frequent in GCC and product screens, and `[D]` a differentiator, the
programme's own calibration for candidates with 0 to 3 years' experience in the Indian market.

| Family | Taught on | The move, as that day's pack names it | Where in Kalpa Health the questions sit |
|---|---|---|---|
| T01 | Week 1 Monday | Which total is sales, the revenue tree, and the typical value one large record cannot move | The board's revenue plan, the lab's turnaround, the practices that order tests |
| T02 | Week 1 Tuesday | Is the drop real, which branch and which segment moved, and did the price change or the mix | Cash posted, patients' share of the bill, the allowed amount per test |
| T03 | Week 1 Wednesday | Profile before you touch, the identity rule, and the bridge that names every dollar | The courier company's invoice, a patient register from a lab Kalpa Health is thinking of buying |
| T04 | Week 1 Thursday | Real or the wobble, how many stand behind a rate, and did the change work | Rejected blood samples, a new billing rule |
| T05 | Week 1 Thursday and Friday | The note in four parts, and holding it when someone pushes | Turnaround for the COO, a seventh metro |
| T06 | Week 2 Monday | The warehouse query: its logical order, counts named for what they count, and a run an auditor can repeat | Analysers, redraws, days in accounts receivable |
| T07 | Week 2 Tuesday | Attach, count, explain the difference, then sum, and the checks before a number leaves | Samples against results, claims against a payer's fee schedule |
| T08 | Week 2 Wednesday | Rank inside each group, ties at the line, and LAG within one member's months | The practices marketing visits |
| T09 | Week 2 Thursday | One row per member in pandas, the merge that must not repeat a row, and the as-of date | Patients' open balances |
| T10 | Week 2 Friday | The tool for each job, the lookup that says "missing", and the number a director reads in two minutes | The COO's planning workbook |

A learner meets one set of three questions. Within a group the seats take consecutive letters, so no
two members of a group meet the same set. Each set draws one question per level from three different
families, and every set mixes Week 1 and Week 2.

| Set | L1, the move | L2, the number | L3, the judgement |
|---|---|---|---|
| A | T01-L1 | T04-L2 | T07-L3 |
| B | T02-L1 | T05-L2 | T08-L3 |
| C | T03-L1 | T06-L2 | T09-L3 |
| D | T09-L1 | T02-L2 | T10-L3 |
| E | T10-L1 | T08-L2 | T05-L3 |
| F | T06-L1 | T09-L2 | T02-L3 |
| G | T05-L1 | T10-L2 | T03-L3 |
| H | T08-L1 | T01-L2 | T04-L3 |

### Which questions are swapped for a learner whose group works close to them?

Eleven questions sit close to one sub-problem's viva, so a learner from that sub-problem is asked
another question at the same level in their place. The replacement is always the question at that
level from the set four letters on, A with E, B with F, C with G and D with H. A group's seats take at
most four consecutive letters, so no group-mate ever meets the replacement, no seat holds two
questions from one family, and nothing in the set four letters on sits close to the same sub-problem.
Once the roster's Groups sheet carries Monday's allocation, its Seats sheet makes every swap and its
Grid prints each learner's three questions, so read the questions from the Grid.

| The group's sub-problem | The question in the set | In set | What it rehearses in that viva | Asked in its place |
|---|---|---|---|---|
| 1 revenue | T01-L1, what a lab's revenue is made of | A | The revenue tree of the translation probe | T10-L1 |
| 1 revenue | T01-L2, a typical turnaround | H | The typical claim of seat 1's probe | T02-L2 |
| 2 bookings | T02-L1, a fall in its first thirty minutes | B | Confirming the fall, seat 1's probe | T06-L1 |
| 2 bookings | T02-L2, what has to match before two months compare | D | Whether the data covers the whole window | T01-L2 |
| 3 billing | T03-L1, the courier's invoice against the log | C | The bridge from billed to paid, seat 4's probe | T05-L1 |
| 3 billing | T09-L2, a merge that repeats a patient | F | What the join kept, dropped and repeated, the translation probe | T05-L2 |
| 3 billing | T07-L3, the checks before a joined number leaves | A | The join and the bridge | T05-L3 |
| 3 billing | T03-L3, the auditor's walk through the rows set aside | G | The bridge from billed to paid | T09-L3 |
| 4 no-shows | T04-L2, a rate on 25 draws | A | A rate read on few slots, seat 2's probe | T08-L2 |
| 5 the offer | T02-L3, the rate and the mix | F | The comparison inside each metro, the translation probe | T08-L3 |
| 5 the offer | T04-L3, did a new rule work | H | Whether the offer worked, seat 1's probe | T10-L3 |

### What are the reserves for?

Six questions sit outside every set as reserves, two at each level: T04-L1 and T07-L1, T03-L2 and
T07-L2, and T01-L3 and T06-L3. Use a reserve at the same level when a learner says they heard a
question from someone mocked earlier, when a learner gives a model answer word for word, or when a
mock restarts after a dropped connection. Take the first reserve the table allows for the learner's
sub-problem, and the second if a group-mate has already been asked the first; where the table leaves
none, keep the set's question and go straight to its follow-up.

| The group's sub-problem | L1 reserve | L2 reserve | L3 reserve |
|---|---|---|---|
| 1 revenue | T04-L1, then T07-L1 | T07-L2, then T03-L2 | T06-L3 |
| 2 bookings | T04-L1, then T07-L1 | T07-L2 | T06-L3, then T01-L3 |
| 3 billing | T04-L1 | T03-L2 | T01-L3 |
| 4 no-shows | T07-L1 | T07-L2, then T03-L2 | T06-L3, then T01-L3 |
| 5 the offer | T07-L1 | T07-L2, then T03-L2 | T06-L3, then T01-L3 |

Mocks run all day and learners talk. Eight sets spread the risk, and the follow-up carries the half,
since a memorised model answer survives the first question and breaks on a follow-up written to move
the case one step.

---

## Why is every question set in a corner of Kalpa Health that no group's data covers?

**Who needs the answer.** Every assessor, before improvising anything. A question about a group's
own files asks the viva's question twice, and a question about another group's files can hand a
learner that group's finding before the presentations score it.

**The questions on the way.** Where are the questions set? What does the assessor say about the
numbers? What does an assessor do when a learner answers from their own files?

Each question is set in a corner of Kalpa Health that no group's files touch: the lab's turnaround,
the courier company, payers' fee schedules, patients' balances, the practices that order tests, a
lab Kalpa Health is thinking of buying in Austin, and the board's plans. Every number in a question
is invented for it and lies outside the ten files, and the assessor reads every number the learner
needs aloud; the opening script tells the learner so once, before the first question. No question
names a plant, which is a pattern placed in the files on purpose for a group to find, reuses a
planted number, or sets up a plant's shape. If a learner answers with their own group's finding, say
"Thank you; keep that for the second half" and move on without confirming it. Never invent a question
about the data on the day; if none of a learner's three works, use the reserve at the same level.

---

## How far above a definitional screen does each question sit?

**Who needs the answer.** The assessor deciding whether an answer is good enough for a GCC screen at
the 0 to 3 year band. A bar set at the definition passes learners whom a real screen stops at its
first case.

**The questions on the way.** What does the curriculum row name for calibration? Where does this bank
sit against it? What do you ask a learner who cannot answer at the case level?

The Week 3 Thursday row of the curriculum tracker names GeeksforGeeks, "Data Analyst Interview
Questions and Answers", to calibrate the technical half:
https://www.geeksforgeeks.org/data-analysis/data-analyst-interview-questions-and-answers/ (verified 1 October 2026)
Its questions are definitional ("what is data cleaning", "how do you handle missing data"). This bank
sits one step above them, because a GCC screen at this band asks for the definition inside a business
case. If a learner cannot answer at the case level, ask the entry's anchor question once, which is
the plain form, note in the evidence that you did, and move on.

---

## T01. What is a lab's revenue made of, which number describes a typical case, and which branch does the money belong on? (Week 1 Monday)

**Who needs the answer.** The assessor, since a learner who counts before saying what the number is
made of will one day hand a board a growth figure built on the wrong total. This family tests the
first move of Week 1 Monday, when Meera Raghavan, Kalpa Retail's CEO, asked whether acquisition was
even the branch that was short.

**The questions on the way.** What is Kalpa Health's revenue made of, and what do you ask first?
Which number describes a typical turnaround? Should money go to new practices when existing ones
order less?

### T01-L1. What is Kalpa Health's revenue made of, and what do you ask the COO before any file opens?

| | |
|---|---|
| The move | Week 1 Monday: which total is sales, and what each total counts; the revenue tree, every branch a count over a denominator. Tag `[F]`. |
| Anchor, on the Week 1 Monday row | "A business says 'grow revenue 15 percent'; how do you turn that into questions data can answer?" |
| Ask | "Dr Menon's board wants Kalpa Health's revenue up 12 percent next year. Before you open any file, what is a lab's revenue made of, and what is the first thing you ask her?" |
| Model answer, under a minute | Three totals could be called revenue at a US lab: gross charges at the lab's list prices, the allowed amount the payers' contracts accept, and net revenue, what the lab expects to collect once denials and unpaid balances are out. So the first question is which one the board means, and over which window. Then the tree: revenue is patients, times visits per patient, times tests per visit, times revenue per test, and revenue per test depends on the payer mix, since each payer allows a different amount for the same test. Quest Diagnostics judges its own testing business on the top of that tree, "volume (measured by test requisitions) and revenue per requisition" (Form 10-K for 2025). The second question is which branch the plan assumed would grow. |
| Follow-up | "Take visits per patient. What exactly is its denominator, and what goes wrong if you divide by the whole patient register?" |
| What the follow-up separates | Understood: distinct patients with at least one visit in the same window; dividing by every registered patient, including those who never came that year, mixes how many patients came with how often they came, and dividing visit rows by visit rows reads 1.0. Memorised: recites the four branches and says "the number of patients" without saying which ones. |
| A weak answer sounds like | "I would open the revenue dashboard and see which tests sell most", or a list of marketing ideas with no tree. |

### T01-L2. Which number describes a typical sample's turnaround, the mean of 31 hours or the median of 16?

| | |
|---|---|
| The move | Week 1 Monday: what a typical value looks like, stated so that one large record cannot move it. Tag `[S]`. |
| Anchor, on the Week 1 Monday row | "Mean or median for order value, and why?" |
| Ask | "The lab director's report says the mean turnaround, from the blood draw to the released result, was 31 hours last month against a promise of 24; the median was 16 hours, and 88 percent of samples met the promise. The director wants to fund a night shift. Which number goes in the director's note, and what do you do before you choose?" |
| Model answer, under a minute | A mean nearly twice the median says a few very slow samples are pulling it. Before choosing, I sort the samples by turnaround and read the slowest. If they cluster, on one courier route, one analyser that was down for a day, or one weekend's batch, then the typical sample is the median, 16 hours, and the late cluster is its own line with its cause. The doctors' number is the share within the promise, 88 percent. A night shift adds capacity for every sample, while a cluster from one route is a courier fix that costs far less, so the slowest samples decide which fix the director funds. Every sample stays in the data; the late cluster stays out of the word "typical" only. |
| Follow-up | "When is the mean the right number to give the director?" |
| What the follow-up separates | Understood: when the decision needs a total, since the mean times the count rebuilds the total; for a courier contract that pays a penalty per hour late, the right mean is of the hours past the promise across all samples, zero for a sample on time, stated with the slow cluster. Memorised: "the median is always better because it ignores outliers". |
| A weak answer sounds like | "Remove the outliers and take the mean again", which deletes real late samples, and their patients, from the lab's record. |

### T01-L3. Should marketing's $400,000 go to signing new practices when the tree says existing practices order less? (reserve)

| | |
|---|---|
| The move | Week 1 Monday: which branch the plan should open first, and why not the others. Tag `[D]`. |
| Anchor, on the Week 1 Monday row | "Marketing wants budget for acquisition; what would you check before agreeing it is the right branch, and how would you say no?" |
| Ask | "Kalpa Health's tests are ordered by doctors' practices. The marketing head wants $400,000 to sign up new practices. Your tree says the number of ordering practices held at 600 over the last two years, and requisitions per practice, the orders each sends, fell from 120 a year to 108. You are in the room with the marketing head. What do you say?" |
| Model answer, under a minute | I put the two branches side by side for the same two years: practices held at 600, and orders per practice fell 10 percent, from 120 to 108, which is 7,200 fewer requisitions. The gap is in how much the existing practices order, so money to sign new ones is aimed at a branch that is not short. There are three ways to spend: the $400,000 on new practices, an outreach programme to the practices whose orders fell, or a small test first, outreach to a random half of the falling practices for one quarter, read against the other half. I would take the test, because it costs a fraction and tells us within a quarter whether orders respond. What would change my call: if last year's newly signed practices already order more per practice than the old ones, acquisition is the cheaper lever after all. |
| Follow-up | "The marketing head says new practices become loyal later, so signing them fixes orders per practice too. What data answers that, and what if it is too early to tell?" |
| What the follow-up separates | Understood: last year's new practices' orders per practice in their first quarters against existing practices over the same months, and if they are too new to read, "not yet" with the date it can be read. Memorised: repeats "the data says frequency" without naming the comparison. |
| A weak answer sounds like | Caving ("it could help, let us try both"), or an assertion with no number. |

---

## T02. Is a fall real, which branch moved, and did the price change or the mix? (Week 1 Tuesday)

**Who needs the answer.** The assessor, since a learner who explains a fall before confirming it
sends a team after a cause that a calendar or a late file made. This family tests Week 1 Tuesday's
investigation ladder, whose first rung asks whether the drop is real at all.

**The questions on the way.** What do you do in the first thirty minutes after a fall? What has to
match before two months are compared? Why can every payer's rate rise 3 percent while the lab's
average barely moves?

### T02-L1. Cash posted fell 16 percent last month: what do you do in the first thirty minutes, in order?

| | |
|---|---|
| The move | Week 1 Tuesday: the investigation ladder, all five rungs, with rung 1, is the drop real, first. Tag `[S]`. |
| Anchor, on the Week 1 Tuesday row | "Sales dropped 15 percent last month; how would you investigate?" |
| Ask | "The revenue-cycle head says the cash posted from payers and patients fell 16 percent last month. What do you do in the first thirty minutes, in order?" |
| Model answer, under a minute | First, is the fall real: the same length of window, the same definition (cash by the day it was posted, or by the month of the service it pays for), and the month complete for every payer. Payers pay in runs, so a month with fewer payment runs looks short with nothing wrong. Second, which branch moved: claims billed, times the share that paid, times the amount paid per paid claim. Third, which segment carries it: a payer, a metro, a kind of test. Fourth, is it a change of mix or a change of rate inside the segments. Fifth, one hypothesis for the business, with the evidence that would settle it. Causes come last, because they are the cheapest thing to guess and the most expensive to guess wrong. |
| Follow-up | "The largest plan, about 70 percent of the cash, pays in one run every Friday. Last month had four Fridays and the month before had five. What does that do to your 16 percent?" |
| What the follow-up separates | Understood: that plan's cash falls by a fifth with nothing changed, which alone takes the total down about 14 points of the 16, so the drop goes back to the calendar, and the fair comparison is cash per payment run or the same weeks. Memorised: repeats the five rungs and never computes the calendar's share. |
| A weak answer sounds like | "Payers are paying slower; probably a policy change", with no check that the fall is real. |

### T02-L2. Patients' share of the bill jumped from 11 to 19 percent between December and January: what has to match before you call it a change?

| | |
|---|---|
| The move | Week 1 Tuesday: what has to match before two windows are compared fairly. Tag `[F]`. |
| Anchor, on the Week 1 Tuesday row | "What has to match before a quarter-on-quarter comparison is fair?" |
| Ask | "Of everything the payers' contracts allow on Kalpa Health's claims, the share the patients owe themselves rose from 11 percent in December to 19 percent in January. The finance head calls it a collections problem on the way. What do you check?" |
| Model answer, under a minute | The two months are not alike. A deductible is the amount a patient pays each plan year before the plan pays, and deductibles reset each plan year, so January's bills lean on patients and later months lean on the plans. The fair comparison is January against last January, the same month of the plan year. Then the rest that has to match: the same payer mix, since more self-pay patients or more plans with high deductibles would raise the share on their own; the same definition, patients' share over the allowed amount; and January's remittances complete, since the latest month's answers are still arriving. Only then is a rise a change. |
| Follow-up | "Last January the share was 18 percent. What do you tell the finance head now?" |
| What the follow-up separates | Understood: most of the jump is the deductible calendar, one point above last January is small enough to need the payer mix checked before anyone acts, and the useful action is planning for January's patient balances, such as telling patients their share before the draw. Memorised: says "seasonality" and stops, with no comparison named. |
| A weak answer sounds like | "Patients are paying less; send the balances to collections." |

### T02-L3. Every payer allowed about 3 percent more per test, and the lab's average per test rose only 0.5 percent: what happened, and how do you make the case in the room?

| | |
|---|---|
| The move | Week 1 Tuesday: did customers pay more, or did the mix change. Tag `[D]`. |
| Anchor, on the Week 1 Tuesday row | "Marketing insists the answer is acquisition and your data says frequency; how do you make the case in the room?" |
| Ask | "From one quarter to the next, the average amount allowed per test rose about 3 percent for each of the four payer types, and the lab's overall average per test rose only 0.5 percent. The head of payer contracting budgeted the 3 percent and says your numbers must be wrong. What happened, and how do you make the case in the room?" |
| Model answer, under a minute | Nothing is wrong; the mix moved. More of the second quarter's tests came from payers that allow less per test, Medicaid for example, so the blend rose less than any payer's own rate. Rerunning the query proves nothing, since the same data gives the same number, while one table settles it in a minute: each payer's share of tests and its allowed amount per test in both quarters, with the change split into a rate effect of about 3 percent and a mix effect that takes about 2.5 points back. Quest Diagnostics reported the same shape for 2025: revenue per requisition up 0.1 percent, and 2.4 percent on an organic basis, because an acquired business "which has a lower revenue per requisition" joined the mix (Form 10-K for 2025). What would change my call: a payer whose own rate fell would make it a story about rates. |
| Follow-up | "Which one number goes on the slide for Dr Menon?" |
| What the follow-up separates | Understood: the mix effect in dollars or points, with the payer whose share grew named, beside the rate effect the head budgeted. Memorised: says "it is the mix" and stops, with no number and no payer named. |
| A weak answer sounds like | "There must be a data error; I would recheck the query." |

---

## T03. Which number is right when two sources disagree, and how do you show every dollar between them? (Week 1 Wednesday)

**Who needs the answer.** The assessor, since a learner who picks one of two disagreeing numbers
instead of reconciling them gets finance to pay or withhold money nobody can audit. This family tests
Week 1 Wednesday's profile-first and bridge moves, which started when Anand Iyer, Kalpa Retail's
finance controller, found the dashboard and his books a crore apart.

**The questions on the way.** Which number do you pay when an invoice and a log disagree? How can a
dedupe find nothing when duplicates exist? How do you walk an auditor through the rows you set aside?

### T03-L1. The courier invoices 4,180 pickups and the lab's log shows 3,960: which number does finance pay?

| | |
|---|---|
| The move | Week 1 Wednesday: profile before you touch, then the bridge that names every unit between two totals. Tag `[S]`. |
| Anchor, on the Week 1 Wednesday row | "Finance and your dashboard disagree; what do you do?" |
| Ask | "Kalpa Health's courier company carries blood samples from the patient service centres to the labs. It invoices 4,180 pickups for last month. The lab's own pickup log shows 3,960. The finance head wants to know which number to pay before anyone pays. What do you do?" |
| Model answer, under a minute | I do not pick one. First I match definitions: is a pickup one stop at a site on one run, or one bag, and does the contract pay for a stop the lab cancelled? Then I profile both files before touching them: rows, distinct stops by route, site, date and run, the dates covered, blanks and the largest values. Then I build the bridge from 4,180 to 3,960 line by line, in pickups and in dollars: invoice lines that repeat one stop, stops billed after the lab cancelled them, stops logged on one side of the month's end and invoiced on the other, and anything else, each counted. Every call goes in a decisions log, and input equals matched plus set aside, so finance can audit every dollar it pays or withholds. |
| Follow-up | "Your pickup counts now reconcile, and the dollars still do not. Where do you look?" |
| What the follow-up separates | Understood: the rates, such as a weekend or after-hours surcharge, a rate change applied to the wrong days, or a stop billed in the wrong distance band. Memorised: "check for duplicates" again, which the counts already ruled out. |
| A weak answer sounds like | "The courier is the vendor, so its invoice is right", or "finance's number is the source of truth". |

### T03-L2. A whole-row dedupe of the Austin lab's patient register finds no duplicates, and its front desk says many patients are registered twice: how can both be true? (reserve)

| | |
|---|---|
| The move | Week 1 Wednesday: which rows repeat, and what makes two records one. Tag `[F]`. |
| Anchor, on the Week 1 Wednesday row | "How do you find duplicates, and what makes two records the same?" |
| Ask | "Kalpa Health is thinking of buying a small lab in Austin. Its patient register has 9,400 rows. A dedupe on the whole row finds no duplicates, and the Austin front desk swears many patients are registered twice. How can both be true, and what do you do?" |
| Model answer, under a minute | Two registrations of one person are rarely identical on every column: a name spelt two ways, a typo in the date of birth, a new phone number or a new plan. A whole-row dedupe compares every column, so it finds nothing. The identity rule has to be what makes two rows one person, and with no shared id that is a combination such as date of birth, last name and ZIP code. I would flag the pairs that match for a person to review rather than merge them blind, because merging two different patients puts one person's results in another's record, which is far worse than a duplicate. Then I count the flagged pairs, check a sample by hand, and log the rule with its count. |
| Follow-up | "Two rows share a date of birth and a last name and have different first names. Do you merge them?" |
| What the follow-up separates | Understood: not automatically; twins share both, while a nickname or a typo in the first name makes one person look like two, so the pair is flagged for the front desk with the ZIP code and phone checked, since a false merge mixes two people's results. Memorised: "keep the first one". |
| A weak answer sounds like | "I would run drop_duplicates." |

### T03-L3. An auditor asks why your clean courier file has 220 fewer pickups than the invoice: how do you walk them through it?

| | |
|---|---|
| The move | Week 1 Wednesday: the decisions log and the bridge, where input equals clean plus set aside. Tag `[D]`. |
| Anchor, on the Week 1 Wednesday row | "An auditor asks why you dropped 14 rows; walk them through it." |
| Ask | "An auditor from the finance team asks why your clean courier file has 220 fewer pickups than the courier's invoice of 4,180. The contract pays $16 a stop. Walk them through it." |
| Model answer, under a minute | I open the decisions log, where each rule has a line: what it caught, how many pickups, how many dollars and why. Say 130 invoice lines repeated a stop already billed, the same route, site, run and time, $2,080, set aside with their line numbers for the courier to explain; 70 were stops the lab cancelled before the run, which the contract does not pay, $1,120; and 20 were stops the log dates on the first of the new month and the invoice puts in this one, $320, moved after checking the run sheets. That is 130, 70 and 20, which is 220, so 3,960 matched plus 220 set aside equals the invoice's 4,180, and the bridge shows the $3,520 between the two totals rule by rule. Nothing was dropped without a line. |
| Follow-up | "Which of the 220 would you defend least, and what would change your mind?" |
| What the follow-up separates | Understood: names a real judgement call, such as the 20 moved across the month's end because they rest on run sheets, and the evidence that would settle them, such as the courier's own pickup scans. Memorised: "all 220 were clearly wrong". |
| A weak answer sounds like | "They were bad records, so I removed them." |

---

## T04. Is a gap real or the wobble chance makes, and did a change work? (Week 1 Thursday)

**Who needs the answer.** The assessor, since a learner who reads a p-value as the chance of being
wrong, or credits a change without asking who got it, sends a lab to retrain a good phlebotomist or
roll out a rule that did nothing. This family tests Week 1 Thursday, where the room asked whether a
fall in Retail-Plus, Kalpa Retail's paid membership tier, was real and whether its monsoon sale
worked.

**The questions on the way.** What does a p of 0.04 mean, and not mean? Should a phlebotomist with 2
rejected samples in 25 be retrained? Did a new billing rule cut denials?

### T04-L1. Your test on two phlebotomy teams gives p = 0.04: what does that tell the lab director, and what does it not? (reserve)

| | |
|---|---|
| The move | Week 1 Thursday: real, or the wobble, read from the share of shuffled worlds. Tag `[S]`. |
| Anchor, on the Week 1 Thursday row | "What does p = 0.03 mean, and not mean?" |
| Ask | "A sample is rejected when the lab cannot test it, for example because the blood broke down in the tube, and the patient has to come back for a second draw. Your permutation test on the gap in rejected samples between the morning and the afternoon phlebotomy teams gives p = 0.04. The lab director asks what that means. What do you say it means, and what does it not mean?" |
| Model answer, under a minute | If there were no real difference between the teams, a gap at least this large would turn up by chance about 4 times in 100. So the gap is hard to put down to luck. It does not mean a 4 percent chance that we are wrong, it does not mean a 96 percent chance that the gap is real, and it says nothing about whether the gap is big enough to act on. That second question is about cost, the patients called back and the draws repeated, and I answer it separately with those numbers. |
| Follow-up | "Explain where the 0.04 came from without using the word probability." |
| What the follow-up separates | Understood: shuffle the team labels across the samples thousands of times, work out the gap each time, and count how often a shuffled gap was as large as the real one: about 4 in every 100 shuffles. Memorised: repeats the definition. |
| A weak answer sounds like | "There is a 96 percent chance the result is right." |

### T04-L2. A new phlebotomist had 2 of 25 samples rejected against the centre's 4 percent on 2,400: retrain them this week?

| | |
|---|---|
| The move | Week 1 Thursday: how many people stand behind a rate, the rule of thumb against thirty, and coin flips on the count. Tag `[F]`. |
| Anchor, on the Week 1 Thursday row | "42 percent on 12 users against 31 percent on 1,200; which do you trust?" |
| Ask | "A new phlebotomist has had 2 of their 25 samples rejected, 8 percent. The centre's rate is 4 percent on 2,400 draws. The lab director wants to send them for retraining this week. What do you tell the director?" |
| Model answer, under a minute | Eight percent stands on 25 draws, so one sample moves it 4 points, and 25 is below thirty, the rule of thumb for how many must stand behind a rate before it is read. The 4 percent stands on 2,400 draws and is solid. If the new phlebotomist were exactly as good as the centre, 2 or more rejections in 25 draws would still happen about a quarter of the time, so this gap is inside the wobble. I would trust the 4 percent, tell the director the new phlebotomist is not yet shown to be worse, and offer something cheap meanwhile, such as a day beside a senior phlebotomist, while the count builds. |
| Follow-up | "What would you have the director watch while the count builds, and how would you read it next month?" |
| What the follow-up separates | Understood: the same coin-flip check on the bigger count each month; 8 or more rejections in 100 draws would happen only about 1 time in 20 for a phlebotomist as good as the centre, so a rate still near 8 percent then is worth acting on, and how many draws it takes to be sure of a gap is power, a later week's topic. Memorised: "a larger sample", with no check and no number. |
| A weak answer sounds like | "Eight is double four, so retrain them." |

### T04-L3. Medicare's necessity denials fell from 6.0 to 3.5 percent after a new billing rule: did the rule work, and should it go everywhere?

| | |
|---|---|
| The move | Week 1 Thursday: did the change work; who got it, what else changed, and the hold-back that would settle it. Tag `[F]`. |
| Anchor, on the Week 1 Thursday row | "Revenue rose after a discount; did the campaign work, and what would you need to know?" |
| Ask | "A medical-necessity denial is a payer refusing a claim because it does not consider the test needed for the patient's condition. In March, Kalpa Health added a rule to its billing system that checks the diagnosis code on Medicare claims before they leave. By June, necessity denials on Medicare claims had fallen from 6.0 to 3.5 percent. The revenue-cycle head wants the rule on every payer's claims. Did it work, and what would you need to know?" |
| Model answer, under a minute | Before and after alone cannot say, since it assumes nothing else changed in those months. The change beside the change sets Medicare against the payers without the rule over the same months: if their necessity denials fell almost as much, say from 5.8 to 3.6 percent, something else moved, such as the doctors' coding. Even a fall near zero there assumes Medicare moves like the others, and nobody has shown that, since a rule chose Medicare for its worst rate and no coin did. The way that settles it is a random hold-back: the rule off for a random fifth of the ordering practices for two months, compared inside Medicare. At 2.5 points on, say, 4,000 Medicare claims a month, the rule prevents 100 denials a month, so the hold-back forgoes about 20 a month. My call is to run the hold-back before the every-payer rollout. |
| Follow-up | "The revenue-cycle head says the rule costs nothing to run, so why not switch it on everywhere today?" |
| What the follow-up separates | Understood: the cost is the claims the rule holds back for a fix, the staff time to fix them and the filing deadlines they drift towards, so switch it on everywhere if the head wants, and keep a random fifth held back so the answer still arrives. Memorised: "correlation is not causation", with no comparison and no design. |
| A weak answer sounds like | "Denials fell after the rule, so it worked." |

---

## T05. What goes in front of the COO, and how do you hold it when someone pushes? (Week 1 Thursday and Friday)

**Who needs the answer.** The assessor, since a finding told in the order it was found never
reaches the decision it was for. This family tests the four-part note Week 1 Thursday wrote and Week 1
Friday defended: claim, evidence, caveat and action.

**The questions on the way.** How do you put one finding in front of Dr Menon in two minutes? What is
missing from a count with no denominator? What do you say when the honest answer is "not yet"?

### T05-L1. Dr Menon has two minutes before her board meeting: how do you put one finding in front of her?

| | |
|---|---|
| The move | Week 1 Thursday and Friday: the note in four parts, claim, evidence, caveat and action. Tag `[S]`. |
| Anchor, on the Week 1 Thursday row | "Explain a finding to a non-technical stakeholder." |
| Ask | "Dr Menon has two minutes before her board meeting. How do you put one finding in front of her? Use any example from the lab." |
| Model answer, under a minute | One sentence for each of four parts. The claim says what is true, with its number. The evidence is the comparison that shows it, with its denominator and window. The caveat is the one thing that could make it wrong, and how big that risk is. The action is what she should do next and what it costs. For example: turnaround within the 24-hour promise fell from 94 to 89 percent of samples between the last two months; 61 percent of the late samples came from two of the eleven courier routes, which carry 18 percent of samples; one month is one reading, so a bad week could be part of it; move those two routes' last pickup an hour earlier for a month and read the share again. |
| Follow-up | "Your caveat: how would Dr Menon know if it came true?" |
| What the follow-up separates | Understood: names the check and when it can be read, such as the two routes' share next month against their own last three months. Memorised: a caveat that fits any finding, such as "the data may have errors". |
| A weak answer sounds like | The analysis told in the order it was done, from loading the files. |

### T05-L2. A line for the COO says 2,300 samples missed the promise last month, up from 1,900: what is missing before it goes to her?

| | |
|---|---|
| The move | Week 1 Tuesday's rate with its denominator, inside the note. Tag `[S]`. |
| Anchor, on the Week 1 Tuesday row | "Why is a rate without a denominator meaningless?" |
| Ask | "A colleague's line for Dr Menon reads: 'Turnaround is slipping: 2,300 samples missed the 24-hour promise last month, up from 1,900 the month before.' The lab received 52,000 samples last month and 42,000 the month before. What is missing before it goes to her?" |
| Model answer, under a minute | The denominator is missing. Late samples rose 21 percent, and samples received rose 24 percent, so the share that missed the promise held: 1,900 of 42,000 is 4.5 percent and 2,300 of 52,000 is 4.4 percent. Turnaround is not slipping; volume grew and the late count grew with it. The line also needs the two windows, matched, and whether the movement is bigger than the usual month to month, and it needs an action. A version for her: the share of samples within the 24-hour promise held at about 95.5 percent while volume grew 24 percent; no action on turnaround this month. |
| Follow-up | "Now say volume was flat, 42,000 both months. Rewrite the line." |
| What the follow-up separates | Understood: the late share rose from 4.5 to 5.5 percent, a real slip of one point, and the action changes: find where the extra 400 late samples sit, by route, analyser and day of the week. Memorised: keeps "slipping" without recomputing. |
| A weak answer sounds like | "Add a chart to make it clearer." |

### T05-L3. Dr Menon asks whether to open a seventh metro next year, and the honest answer is "not yet": what do you say?

| | |
|---|---|
| The move | Week 1 Thursday: "not yet" as an answer, with what would make it yes; Week 1 Friday: holding the note when someone pushes. Tag `[D]`. |
| Anchor, on the Week 1 Thursday row | "The CEO wants a yes or no and the honest answer is 'not yet'; what do you say, and how do you hold the line when marketing pushes?" |
| Ask | "Dr Menon asks: should Kalpa Health open a seventh metro next year, yes or no? You have the candidate metro's population and its mix of payers, and no evidence yet on how many patients would come. The honest answer is not yet. What do you say?" |
| Model answer, under a minute | I say not yet, then what would make it yes and when we would know. What we know is the metro's size and its payer mix, which sets what each test would earn. What we do not know is how many patients would book. The cost of each wrong call is a lab and two centres opened where patients do not come, or a market left to a competitor. The decision she can make today is a cheaper way to find out: open one patient service centre without a lab, courier its samples to the nearest Kalpa lab for two quarters, and set the rule now, such as opening the lab if the centre reaches 40 draws a day by its third month. |
| Follow-up | "The marketing head says analysts never commit to anything. Answer them." |
| What the follow-up separates | Understood: the decision rule is the commitment, written before the result is known, so nobody can move it afterwards. Memorised: "we need more data". |
| A weak answer sounds like | A yes to please the room, or a lecture on statistics with no decision. |

---

## T06. Can the warehouse give the number every week, the same way, to someone who will audit it? (Week 2 Monday)

**Who needs the answer.** The assessor, since a query that runs but filters in the wrong place, or
divides one integer by another, ships a wrong KPI every Monday until someone audits it. This family
tests Week 2 Monday's SQL, asked as business questions, the moves the room used to give Anand Iyer,
Kalpa Retail's finance controller, his Monday numbers from the warehouse itself.

**The questions on the way.** Where does each condition go in a query, and why? Why does a rate come
back as 0 for every centre? How do you write a KPI query an auditor can repeat?

### T06-L1. The lab director wants every analyser that ran more than 2,000 tests last month, counting released results only: where does each condition go, and why there?

| | |
|---|---|
| The move | Week 2 Monday: the logical order of a query, WHERE against HAVING. Tag `[S]`. |
| Anchor, on the Week 2 Monday row | "WHERE against HAVING, one sentence each" and "Explain the logical order in which a SQL query executes." |
| Ask | "An analyser is the machine that runs the tests. The lab director wants every analyser that ran more than 2,000 tests last month, counting only tests whose results were released. Where does each condition go in the query, and why there?" |
| Model answer, under a minute | "Released results only" filters rows, so it goes in WHERE and runs before the grouping. "More than 2,000 tests" filters a group by its count, and the count exists only after GROUP BY, so it goes in HAVING. The database runs FROM, then WHERE, then GROUP BY, then HAVING, then SELECT, then ORDER BY and LIMIT, which is why the conditions sit in the order the business question puts them. |
| Follow-up | "Why can you not use the alias you named in SELECT inside WHERE?" |
| What the follow-up separates | Understood: SELECT runs after WHERE, so the alias does not exist yet when WHERE runs. Memorised: "it is a SQL rule". |
| A weak answer sounds like | "HAVING is like WHERE but for groups", with no reason and no order. |

### T06-L2. Your query returns the redraw rate as exactly 0 for every centre: did nobody redraw anyone?

| | |
|---|---|
| The move | Week 2 Monday: counts named for what they count, and a KPI checked against a known value before it leaves; the trap of integer division. Tag `[F]`. |
| Anchor, on the Week 2 Monday row | "Why would you compute a KPI in the warehouse rather than in a notebook?" |
| Ask | "A redraw is a second blood draw after a rejected sample. Your Monday query divides redraws by draws for each patient service centre and returns exactly 0 for every centre. The lab director reads it as no centre redrawing anyone. What happened?" |
| Model answer, under a minute | Both counts are integers, and Postgres divides an integer by an integer as an integer, so 37 redraws over 2,400 draws, which is 1.5 percent, comes back as 0. Casting one side to numeric gives the real rate. I would also check the denominator counts draws, the thing the rate is out of, and not tubes or rows of another table. Before the number went out, it should have been set against a figure someone already knows, such as last month's redraw count, which is far from zero. |
| Follow-up | "How do you stop this reaching the lab director next Monday?" |
| What the follow-up separates | Understood: a check query that compares the KPI with a known count or a sensible range and fails loudly, run before the report is sent. Memorised: "cast to float", and nothing about the check. |
| A weak answer sounds like | "The centres had no redraws last month." |

### T06-L3. The finance head's analyst will audit your days-in-receivables query line by line: what changes in how you write it, and what would you refuse to compute in a notebook? (reserve)

| | |
|---|---|
| The move | Week 2 Monday: named steps an auditor can run one at a time, and a run that gives the same answer twice. Tag `[D]`. |
| Anchor, on the Week 2 Monday row | "A stakeholder's analyst must audit your query; what changes in how you write it, and what would you refuse to compute in a notebook?" |
| Ask | "Days in accounts receivable says how many days of revenue the lab is still owed: the money owed to it on a date, divided by its average net revenue per day. Quest Diagnostics reports its version, days sales outstanding, as 48 days at the end of 2025. The finance head's analyst will audit your Kalpa Health query line by line. What changes in how you write it, and what would you refuse to compute in a notebook?" |
| Model answer, under a minute | I write it as named steps, one common table expression per business step: what is owed on the as-of date, net of the amounts the contracts never meant to pay, then net revenue per day over the trailing window, then the division. Every filter is explicit, the as-of date is printed on the result, any LIMIT has an ORDER BY with a tie-break, a reconciliation line sets the amount owed against finance's own ledger on the same date, and the run prints its row count and totals, so a rerun gives the same answer. A notebook, an export to Excel or a view in the warehouse could each produce it, and the view wins for a number finance reads every month, since a notebook copy drifts and two versions of one number then exist. What would change that: a one-off question finance will never ask again is fine in a notebook. |
| Follow-up | "Two analysts ran your list of the twenty oldest balances and got different lists. Why?" |
| What the follow-up separates | Understood: LIMIT without ORDER BY, or ties at twentieth place with no tie-break, returns whichever rows come first. Memorised: "the data changed". |
| A weak answer sounds like | "I would add comments to the query." |

---

## T07. When two tables are joined, which rows does the join keep, drop or repeat, and how do you know before the number leaves? (Week 2 Tuesday)

**Who needs the answer.** The assessor, since a join that silently drops or repeats rows changes a
dollar figure without a single row looking wrong. This family tests Week 2 Tuesday, where the room
set what Kalpa Retail collected against what it booked and showed that nothing was counted twice.

**The questions on the way.** Which join keeps the samples still waiting for a result? Why do expected
dollars nearly double after a join? Which checks run before a joined number reaches a payer meeting?

### T07-L1. The lab director wants turnaround for every sample received last week, including those still waiting: INNER or LEFT join, and what does the wrong one hide? (reserve)

| | |
|---|---|
| The move | Week 2 Tuesday: which join keeps, drops or repeats, and the rows with no partner. Tag `[S]`. |
| Anchor, on the Week 2 Tuesday row | "INNER against LEFT join: what does each drop or keep?" and "How do you find orders with no payment?" |
| Ask | "The lab director wants turnaround for every sample received last week, including the ones still waiting for a result. You have a table of samples and a table of results. INNER join or LEFT join from samples to results, and what does the wrong one hide?" |
| Model answer, under a minute | LEFT from samples to results, because it keeps every sample, and the ones still waiting show an empty result. An INNER join drops the waiting samples, which are exactly the slowest, so turnaround looks better than it is. The list of samples still waiting is the anti-join, the samples whose result side is empty, and that list is often what the lab director wanted most. |
| Follow-up | "You add WHERE result status equals 'final'. What happens to your LEFT join?" |
| What the follow-up separates | Understood: the filter removes the rows whose result side is empty, so the LEFT join behaves as an INNER one; the condition moves into the ON clause. Memorised: "LEFT keeps everything". |
| A weak answer sounds like | "LEFT keeps all the rows from both tables." |

### T07-L2. After you join claim lines to the plan's fee schedule, expected dollars nearly double and every row looks right: where do you look? (reserve)

| | |
|---|---|
| The move | Week 2 Tuesday: attach, count, explain the difference, then sum; the join that grew the row count. Tag `[F]`. |
| Anchor, on the Week 2 Tuesday row | "Revenue doubled after a join and every row looks fine; where do you look?" and "Your join grew the row count; name the cause and the check." |
| Ask | "A payer's fee schedule lists what its contract allows for each test. To check what one commercial plan should have paid last quarter, you join 41,200 claim lines to its fee schedule on the test code. Expected dollars come out almost double what payer contracting expects, and every row looks right. Where do you look?" |
| Model answer, under a minute | I would look at the grain. The fee schedule holds more than one row per test code, an old rate and a new rate, each with the dates it applies from and to, so the join repeats each claim line once per rate and the sum counts it twice. I count rows and distinct claim lines before and after the join: if 41,200 lines became about 79,600 rows, the join fanned out. The fix joins on the test code and on the service date falling inside the rate's dates, so each line meets exactly one rate, and then rows after the join equal lines before it. |
| Follow-up | "What single check, run every time, would have caught it?" |
| What the follow-up separates | Understood: the row count after the join equals the claim-line count, or the claim-line id stays unique after the join. Memorised: "remove duplicates after the join", which hides the cause. |
| A weak answer sounds like | "Payer contracting must be missing some claims." |

### T07-L3. Which checks run before an expected-against-paid number reaches the payer contracting head, and what do you do when one fails an hour before the meeting?

| | |
|---|---|
| The move | Week 2 Tuesday: the checks before a number leaves, and what the stakeholder gets when one fails. Tag `[D]`. |
| Anchor, on the Week 2 Tuesday row | "Design the validation you run before a joined number reaches Finance, and say what you do when it fails at the end of reporting day." |
| Ask | "Payer contracting is renegotiating a commercial plan's rates and wants your figure for what the plan paid against what its contract says it should have. Design the checks you run before the number reaches the head of payer contracting. Then it is an hour before the meeting and one check fails. What do you do?" |
| Model answer, under a minute | The checks are row counts before and after each join, the key unique on each side, dollar totals before and after, unmatched claim lines and unmatched rates counted and listed, and a bridge from billed to expected to paid that closes. When one fails near the deadline there are four ways: send the number anyway, send last quarter's reconciled number, send today's with the gap stated in dollars, or ask for the meeting to move. I tell the head at once what failed and how big it is, and send the second or the third, with the gap written on the number itself and the time the fixed number will arrive. What would change my call: a failure that touches a few dollars on another plan's claims can travel as a footnote; one that touches this plan's claims cannot. |
| Follow-up | "The head says send it anyway; the meeting cannot move. What do you send?" |
| What the follow-up separates | Understood: sends it with the caveat in dollars on the number itself, and logs the decision and who made it. Memorised: "fix it quickly". |
| A weak answer sounds like | "I would fix the bug fast and send it." |

---

## T08. Who is first inside each group, what happens at a tie, and whose orders fell two months running? (Week 2 Wednesday)

**Who needs the answer.** The assessor, since a ranking that mishandles ties or reads across members
ships the wrong list to a sales team that visits exactly the practices on it. This family tests Week
2 Wednesday's window functions, which the room used to list the members Kalpa Retail's marketing
team should protect before they drift.

**The questions on the way.** GROUP BY or a window for the top three per metro? Why does a falling
list flag a practice that grew? How many rows does a top twenty-five ship at a tie?

### T08-L1. Marketing wants the three practices that sent the most requisitions in each metro: GROUP BY or a window function, and why?

| | |
|---|---|
| The move | Week 2 Wednesday: rank inside each group with PARTITION BY. Tag `[S]`. |
| Anchor, on the Week 2 Wednesday row | "Top-3 per group: GROUP BY or a window, and why?" |
| Ask | "Marketing wants the three practices that sent Kalpa Health the most requisitions last quarter in each of the six metros. GROUP BY or a window function, and why?" |
| Model answer, under a minute | I would use a window function. GROUP BY collapses each metro to one row, so it can give the largest count but loses the practices behind it. A window ranks practices inside each metro, partitioned by metro and ordered by requisitions, and keeps every row, so I filter to rank three or better in an outer query, since a window function cannot sit inside WHERE. |
| Follow-up | "Two practices tie for third place in Dallas. How many Dallas rows does marketing get?" |
| What the follow-up separates | Understood: it depends on the function; RANK gives four, ROW_NUMBER gives three with an arbitrary pick unless a tie-break is added, and marketing decides the rule. Memorised: "three". |
| A weak answer sounds like | "ORDER BY requisitions DESC and LIMIT 3", which gives three practices for the whole company. |

### T08-L2. Your list of practices whose orders fell two months running flags a practice whose orders rose every month: what went wrong?

| | |
|---|---|
| The move | Week 2 Wednesday: LAG within one member's months, and a month with no order read as no reading. Tag `[F]`. |
| Anchor, on the Week 2 Wednesday row | "How would you find customers whose spend fell two months in a row?" |
| Ask | "You built a list of practices whose monthly requisitions fell two months running, using LAG. It flags a practice whose orders rose every month. What went wrong?" |
| Model answer, under a minute | LAG without PARTITION BY practice reads the previous row of the whole table, and at the start of each practice's months that row belongs to another practice. So the practice's first month is compared with someone else's last. The fix partitions by practice and orders by month. I would also fill the months with no orders first, because a skipped month otherwise vanishes and LAG compares across it. |
| Follow-up | "A practice ordered in one month, nothing the next, and ordered again the month after. Did its orders fall?" |
| What the follow-up separates | Understood: with the empty month filled as zero, yes; without the fill, LAG compares the third month with the first; and if the practice was closed for the month, that month is no reading, so marketing decides the rule. Memorised: "sort by practice". |
| A weak answer sounds like | "The data must have duplicates." |

### T08-L3. Marketing says ties rank the same and wants the top 25 practices in each metro for sales visits, and the team can visit exactly 25: which function, how many rows might ship, and what do you tell them?

| | |
|---|---|
| The move | Week 2 Wednesday: ties at the line, and the rule the business chooses. Tag `[D]`. |
| Anchor, on the Week 2 Wednesday row | "The business says 'ties rank the same'; which function, and how many rows might the top-N report ship?" |
| Ask | "Marketing says practices with the same number of requisitions rank the same, and wants the top 25 in each metro for its sales team to visit. The team can visit exactly 25 a metro. In Dallas, the practices in 25th and 26th place both sent 61 requisitions. Which function, how many rows might you ship, and what do you tell them?" |
| Model answer, under a minute | I see three ways, sized on Dallas. RANK, which marketing asked for, ships 26, because two practices tie at 25th. DENSE_RANK can ship more, since it counts distinct values rather than practices. ROW_NUMBER ships exactly 25 but drops one of the tied pair arbitrarily, so two runs can disagree. The best fit is a tie-break marketing chooses, such as the most recent requisition, written into the ORDER BY: with it, RANK ships exactly 25, the same 25 every run, and the report's first line prints the count shipped. What would change my call: if the team can stretch to 26 visits, RANK alone is fine. |
| Follow-up | "Marketing will not choose a tie-break. What do you do?" |
| What the follow-up separates | Understood: ships RANK's 26 with the tie named in the first line, and asks again with the cost of each choice. Memorised: "use ROW_NUMBER", which drops one tied practice by an arbitrary pick. |
| A weak answer sounds like | "Just take the first 25." |

---

## T09. How do you build one row per patient, merge onto it without repeating anyone, and date it so the count holds? (Week 2 Thursday)

**Who needs the answer.** The assessor, since a table with a patient repeated, or aged by the wrong
date, sends collection letters to patients who do not yet owe them. This family tests Week 2
Thursday's pandas moves, which built Kalpa Retail's growth team a table of one row per customer that
it could act on without checking.

**The questions on the way.** How do you build one row per patient, and check it? Why did a patient's
balance double after a merge? Why must days since the last payment be counted from the extract's date?

### T09-L1. The revenue-cycle team wants one row per patient with their open balance, statements sent and last payment date: how do you build it, and what do you check?

| | |
|---|---|
| The move | Week 2 Thursday: groupby as split, apply, combine, and the check that the result has one row per member. Tag `[S]`. |
| Anchor, on the Week 2 Thursday row | "groupby in the split-apply-combine sentence." |
| Ask | "A patient's open balance is what they still owe the lab after their plan has paid. The revenue-cycle team wants one row per patient with their open balance, the number of statements sent to them and the date of their last payment. Say how you build it in one sentence, then the check you run." |
| Model answer, under a minute | Split the balance records by patient, apply a sum to the balance, a count to the statements and a maximum to the payment date, and combine the results into one row per patient. The check is that the result has exactly as many rows as there are distinct patients in the source, and that the total balance equals the source's total. |
| Follow-up | "Patients with no payer recorded have vanished from your table. Why?" |
| What the follow-up separates | Understood: grouping by payer as well drops rows whose payer is missing, since groupby leaves missing keys out by default, so set dropna to False or fill the payer first. Memorised: restates split, apply, combine. |
| A weak answer sounds like | The definition, with no check. |

### T09-L2. After you merge the coverage table onto the patient table, one patient's balance has doubled: which argument would have stopped it, and what is the fix?

| | |
|---|---|
| The move | Week 2 Thursday: the merge that must not repeat a row, stopped by validate. Tag `[F]`. |
| Anchor, on the Week 2 Thursday row | "Which merge argument raises on duplicate keys, and which error?" |
| Ask | "You merge a table of each patient's insurance coverage onto the patient-balance table, and one patient's open balance has doubled. Which argument would have stopped it, and what is the fix?" |
| Model answer, under a minute | The argument is validate: set to many_to_one or one_to_one, it makes pandas raise a MergeError when the key repeats on the side that should be unique. Here the coverage table lists the patient twice, which is normal in US coverage: a patient with Medicare and an employer's plan has a primary payer, which pays first, and a secondary payer. So the patient's row was repeated and the balance counted twice. The fix decides the rule first, primary coverage only, or one row per patient with both plans side by side, brings coverage to one row per patient, and then merges with validate on. |
| Follow-up | "Why not drop duplicates after the merge?" |
| What the follow-up separates | Understood: it hides which side was duplicated, and here it would keep one of the patient's two plans by chance. Memorised: "that also works". |
| A weak answer sounds like | "I would check the shape of the result." |

### T09-L3. The balance table refreshes every Monday, and a colleague counts days since each patient's last payment from today's date: what goes wrong, and which tool and date do you choose?

| | |
|---|---|
| The move | Week 2 Thursday: the same question in three tools, and the date the data was taken, never today's. Tag `[D]`. |
| Anchor, on the Week 2 Thursday row | "Same question, three tools: how do you choose, and defend one choice?" |
| Ask | "The patient-balance table is rebuilt every Monday from an extract, and balances with no payment for more than 90 days go to an outside collection agency. A colleague counts the days since each patient's last payment from today's date. What goes wrong, and which tool and date do you choose?" |
| Model answer, under a minute | Today's date ages every patient with the calendar, so an extract that arrives late, or a table read later in the week, makes balances look older than the data says, and patients cross 90 days with nothing changed in their account. I pin an as-of date to the extract, the date it was taken, and print it on the table. Three tools could compute it: SQL in the warehouse with the as-of date as a parameter, pandas against the extract's date, or Excel with TODAY(), which drifts every day the file is opened. I choose SQL, because the warehouse already holds the balances and finance audits it there, and pandas on the same as-of date must give the same counts. |
| Follow-up | "The extract is a week old and the colleague used today's date. Which patients get a collection letter they should not?" |
| What the follow-up separates | Understood: everyone whose true count is 84 to 90 days reads as 91 to 97, more than 90, and crosses the line, and the learner counts them by recomputing with the as-of date and comparing. Memorised: "use the latest date". |
| A weak answer sounds like | "Today's date is fine, since the table refreshes every week." |

---

## T10. Which tool owns which number, and what can a director break in the workbook? (Week 2 Friday)

**Who needs the answer.** The assessor, since a workbook that returns a neighbour's numbers for a
missing id puts a wrong figure in a director's plan with no error showing. This family tests Week 2
Friday, where the room built Kalpa Retail's chief of staff a workbook a director could open without
a login, change in the room and still trust.

**The questions on the way.** SQL, pandas or Excel for one of Dr Menon's asks? Why does a missing id
return a neighbour's numbers? What did a sheet get right when two directors get two answers?

### T10-L1. SQL, pandas or Excel: how do you choose, for one of Dr Menon's asks?

| | |
|---|---|
| The move | Week 2 Friday: which tool owns which number, and what a stakeholder may change. Tag `[S]`. |
| Anchor, on the Week 2 Friday row | "SQL, pandas or Excel: how do you choose?" and "A stakeholder wants to poke the numbers themselves; what do you give them and what do you never give them?" |
| Ask | "SQL, pandas or Excel: how do you choose, for one of Dr Menon's asks?" |
| Model answer, under a minute | The warehouse, in SQL, owns a number finance relies on every week, such as days in accounts receivable, because it runs where the data lives and one version exists. pandas owns a several-step analysis or a reshape I must reproduce top to bottom, such as splitting a change in the average per test into price and mix. Excel owns the view for a director who wants to change assumptions and watch the answer move, such as next year's plan, fed from an exported, reconciled table and never used to edit the source. |
| Follow-up | "Dr Menon's chief of staff wants to edit the numbers themselves. What do you give them?" |
| What the follow-up separates | Understood: yellow input cells for the assumptions, formulas protected, the data read-only and a checks tab. Memorised: "Excel, because they know Excel". |
| A weak answer sounds like | "Whichever tool I am most comfortable in." |

### T10-L2. A director types a practice id that has never ordered from Kalpa Health, and the sheet shows another practice's numbers: what happened, and what do you fix?

| | |
|---|---|
| The move | Week 2 Friday: the lookup that must say "missing", and SUBTOTAL under a filter; the trap of an approximate lookup returning a neighbour for a missing id. Tag `[F]`. |
| Anchor, on the Week 2 Friday row | "Your pivot shows a different total from the warehouse; where do you look first?" |
| Ask | "Your planning workbook lets a director type a practice id and see that practice's requisitions. A director types an id for a practice that has never ordered from Kalpa Health, and the sheet shows another practice's numbers instead of an error. What happened, and what do you fix?" |
| Model answer, under a minute | The lookup is approximate. VLOOKUP with its fourth argument TRUE, or left out, searches a sorted column for the nearest key at or below the one typed, so a missing id returns the row of the id just before it. The fix is an exact match, VLOOKUP with FALSE or INDEX and MATCH with 0, wrapped so that a missing id says "not in the table". Then I would test it on an id I know is missing before the workbook goes out. |
| Follow-up | "The director then filters the practice table to Dallas, and the total under it does not change. Why?" |
| What the follow-up separates | Understood: SUM adds the rows a filter hides, while SUBTOTAL leaves filtered rows out with either 9 or 109 as its first argument, 109 also leaving out rows hidden by hand; that is also the first place to look when a sheet's total and the warehouse's disagree. Memorised: "Excel is calculating wrongly". |
| A weak answer sounds like | "The director must have typed it wrong." |

### T10-L3. Two directors change assumptions in the planning meeting and each gets a different answer from your sheet: what did you get right, and what do you fix?

| | |
|---|---|
| The move | Week 2 Friday: assumptions in one place, and the number a director reads in two minutes with its period, comparison and base. Tag `[D]`. |
| Anchor, on the Week 2 Friday row | "Two directors change assumptions in the room and the sheet recalculates differently for each; what did you get right and what do you fix?" and "How do you present one number so it is not misread?" |
| Ask | "Two directors change assumptions in the planning meeting, and each gets a different answer from your sheet. What did you get right, and what do you fix?" |
| Model answer, under a minute | I got half of it right: the sheet recalculates, so the assumptions are live. What needs fixing is that the assumptions are scattered, so the two directors edited different cells. There are two fixes: lock the sheet, which stops the directors using it in the room, or move every assumption into one labelled block of yellow input cells with two scenario columns side by side, so both directors see both answers. The block wins, with the formulas and the source data protected and a checks tab that turns red when a total stops tying to the warehouse. What would change my call: a sheet that goes to the board as a final figure gets locked once the meeting has chosen its scenario. The front page shows one number with its unit, denominator, period and the comparison it is read against. |
| Follow-up | "Show me the front-page number for turnaround in one line." |
| What the follow-up separates | Understood: states the value, the unit, the denominator, the period and the comparison, such as 91.8 percent of 48,300 samples released within 24 hours in the last four weeks, against 94.1 percent in the four weeks before. Memorised: "a big number in bold". |
| A weak answer sounds like | "Lock the sheet so nobody can change anything." |
