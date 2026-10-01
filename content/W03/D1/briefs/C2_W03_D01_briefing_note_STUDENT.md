# Which branch of Kalpa Health is short of the plan, and what should I tell the board?

**From:** Dr Priya Menon, COO, Kalpa Health
**To:** the data and AI team at Kalpa's Global Capability Centre (GCC), Bengaluru
**Re:** Q3 test volumes, and five questions my heads cannot answer
**With it:** ten data files, exported on Friday 16 October 2026

Kalpa Health, Kalpa Group and everyone in them are fictional. Every record in the files is
synthetic, so no real patient's information is in them.

> "My dashboard says test volumes grew 5 percent from Q2 to Q3. The plan the board approved asks for
> 18. I do not need another dashboard. I need to know where the 13 points went, and what to do next."
> Dr Priya Menon, COO, Kalpa Health

**Who needs the answer.** I do, before I take the second half's plan to the board. If you name the
wrong branch, I move staff and money into a part of the business that was never short, and the part
that was short keeps falling for another quarter.

**The questions on the way.** What business is Kalpa Health, and what does my 5 percent measure?
Which five questions are my heads asking, and what will each answer decide? Which files has my data
team sent, and what is in each? How does your week run, and how is it scored? Who checks your work
before it reaches me?

---

## What business is Kalpa Health, and what does my 5 percent measure?

**Who needs the answer.** Every group, before it takes a question. My heads use words most of you
have never needed, and an answer built on the wrong meaning of "a test" or "revenue" answers a
question I did not ask.

**The questions on the way.** Where do we work, and who pays us? What do I mean by Q2 and Q3? What
does my dashboard show, and against what?

### Where do we work, and who pays us?

We run diagnostic laboratories and patient service centres in six US metro areas: Dallas, Phoenix,
New York, Chicago, Atlanta and Philadelphia. A patient service centre is where a phlebotomist, the
person trained to draw blood, takes a patient's sample; the laboratory runs the tests. Each metro
has one laboratory and two patient service centres, so we have eighteen sites. A patient books one
or more tests, or a panel, which is several tests ordered under one name. They book by walking in,
online, by phone, or for a collection at home, when a phlebotomist visits the patient instead.

We bill in dollars. A claim is the bill we send to whoever pays for a patient's tests: a commercial
health plan, Medicare (the federal programme for people aged 65 and over), Medicaid (each state's
programme for people on low incomes) or the patient, who then pays for themselves (self-pay). A
claim goes out at our list prices. The payer answers with a remittance, which says what its
contract allows, what it pays, what the patient owes and what it refuses to pay, which is a denial.
Our revenue-cycle and analytics work runs from the GCC in Bengaluru, and that is why these questions
come to you.

You will hear more of this vocabulary than this note carries. The domain dossier,
`study-notes/C2_W03_D01_domain_us_healthcare_STUDENT.md`, tells the business in full, and its
one-page card is `cheatsheets/C2_W03_D01_us_healthcare_domain_card_STUDENT.pdf`.

### What do I mean by Q2 and Q3?

We report in calendar quarters, the way a US business does. Q2 is April to June 2026, and Q3 is July
to September 2026. Every figure in this note and every file my team sent uses those two quarters.

### What does my dashboard show, and against what?

My dashboard shows test volumes up 5 percent from Q2 to Q3. The plan the board approved asks for 18
percent, so I am 13 percentage points short. Every head I ask names a different cause and backs it
with a different number, and nobody has yet shown me which cause the numbers support.

So, in one line: Kalpa Health is a US laboratory business in six metros, paid in dollars by four
kinds of payer, and my 5 percent is my dashboard's growth in tests from Q2 to Q3, against a plan of
18.

---

## Which five questions are my heads asking, and what will each answer decide?

**Who needs the answer.** Each group, at the allocation. The question you take is one of these five,
and the decision it feeds is what your answer will be judged against.

**The questions on the way.** Who is asking? What did they ask, in their own words? What will they
decide with your answer? What does a wrong answer cost them?

| # | Who is asking | What they asked me, word for word | What your answer decides | What a wrong answer costs |
|---|---|---|---|---|
| 1 | The finance head | "The board will ask me where the plan's growth went. Where does our lab revenue actually come from, and which branch of it is short?" | Where the second half's recovery effort and money go | Money goes to a branch that was never short, and the short one keeps falling |
| 2 | The patient service centres' operations head | "Bookings fell in two of our metros in Q3. Before I send a field team or cut staff there, I need to know how far they fell, and why." | Whether to send a field team, cut staff, or leave the two metros alone | Staff are cut where patients still need them, or a real decline runs on for another quarter |
| 3 | The finance head | "The claims we billed say one thing and the posting system says another. Which claims are unpaid, how much money is that, and can I trust the figure I report?" | The collections figure reported at the quarter's close, and which claims the revenue-cycle team chases first | A wrong figure reaches the board under the finance head's name, and claims are chased after their payers' filing deadlines have passed |
| 4 | The patient service centres' operations head | "KH-ATL-03, one of our two Atlanta patient service centres, has the worst no-show rate on my Q3 report. I am being asked to add a receptionist there or close it. Is the centre really worse?" | A second receptionist, new reminder calls, or a closure notice for KH-ATL-03 | A neighbourhood loses its centre on a rate read wrongly, or a real problem keeps costing slots every day |
| 5 | The marketing head | "Our free at-home collection offer lifted bookings 9 percent. I want to offer it to every patient in all six metros. Can you confirm it worked?" | Whether the offer goes to every patient in all six metros, stays as it is, or stops | Every free collection costs us a phlebotomist's visit, so an offer extended on a lift it did not cause spends that money for nothing |

I want one answer per question: a sentence I can carry into the board meeting, the evidence behind
it, what would change it, and what you would have me do.

---

## Which files has my data team sent, and what is in each?

**Who needs the answer.** Every group, before it counts anything. Each file comes from a different
system, and a group that counts the wrong file, or counts the right one the wrong way, answers with
confidence and is wrong.

**The questions on the way.** Which system wrote each file? How many rows came out? Where are the
files, and who else holds them?

My data team exported every file on Friday 16 October 2026, as each system gives it, and has
written up every file and column in the data dictionary,
`briefs/C2_W03_D01_data_dictionary_STUDENT.md`. They have not checked the files against that
description, so what the files hold beyond it is yours to find.

| File | The system it comes from | Rows |
|---|---|---|
| `C2_W03_D01_patients_STUDENT.csv` | The patient register | 6,700 |
| `C2_W03_D01_sites_STUDENT.csv` | The site list, laboratories and patient service centres | 18 |
| `C2_W03_D01_test_catalogue_STUDENT.csv` | The price list of tests and panels | 16 |
| `C2_W03_D01_bookings_legacy_STUDENT.csv` | The booking system we have used since before Q2 | 11,729 |
| `C2_W03_D01_bookings_newsys_STUDENT.csv` | The new booking system | 153 |
| `C2_W03_D01_booking_tests_STUDENT.csv` | The tests and panels on each booking | 51,456 |
| `C2_W03_D01_claims_STUDENT.csv` | The billing system's export of claims | 11,356 |
| `C2_W03_D01_remittances_STUDENT.csv` | The posting system: payers' remittances and the centres' card and cash desks | 11,343 |
| `C2_W03_D01_appointments_STUDENT.csv` | The patient service centres' visit register for Q3 | 7,133 |
| `C2_W03_D01_campaign_STUDENT.csv` | Marketing's list for the free at-home collection offer | 2,381 |

The rows exclude each file's header line. The files are in `data/` beside this note, and every group
holds the same bytes, so one group's count can be checked against another's.

---

## How does your week run, and how is it scored?

**Who needs the answer.** Every learner, today. Each graded event has its own day, and a group that
learns on Thursday what Saturday's panel asks has lost three days.

**The questions on the way.** What happens on each day? When is each event scored, and on what?

### What happens on each day?

You are the analysts I will question. Each group takes one of the five questions on Monday 19
October, when the Programme Head allocates them, and writes it in its own words before anyone opens
a notebook. Tuesday 20 October is Dussehra, a holiday. On Wednesday 21 October each group answers a
short checkpoint and states its headline claim. On Thursday 22 October every learner sits a mock
interview, and the builds are finished around it. On Friday 23 October an industry expert runs group
discussions and the first presentations, and on Saturday 24 October the presentations close with a
live demo on these files, in front of a panel that asks for your opinion, your evidence and what you
would have done differently.

Your group's brief, `briefs/C2_W03_D01_brief_{n}_{name}_STUDENT.md`, says what your question feeds,
the ways a group could answer it and what you ship. The translation worksheet,
`briefs/C2_W03_D01_translation_worksheet_STUDENT.md`, is Monday's work: my question in your words,
mapped onto the method you already own.

### When is each event scored, and on what?

<!-- sync:rubric:W03 -->
**Mini project, 40 marks.** The first four criteria are scored once for the group, and every member receives those 34 marks; presentation and defence is scored for each learner on 6 marks, so a silent teammate cannot ride the group's score.

| Criterion | Marks | What full marks look like |
|---|---|---|
| The question translated | 8 | Dr Menon's words are mapped to the right Weeks 1 and 2 method, with the metric defined and the decision it feeds named. |
| The data made trustworthy | 10 | The data is profiled before it is touched, every cleaning call is in the decisions log with its reason, and counts and dollars reconcile across files. |
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
<!-- /sync:rubric:W03 -->

---

## Who checks your work before it reaches me?

**Who needs the answer.** Every group, before anything leaves the team. I will act on what reaches
me, so whatever is wrong in it becomes my mistake in front of the board.

**The questions on the way.** Who reviews it? Which four things does every review ask for?

Kavya Nair, the senior analyst on your team at the GCC, checks each group's work before it leaves
the team. Every review asks for four things: the baseline your number is compared with, the
denominator every rate is out of, the evidence behind each claim, and a second way to reach the same
number. Work that answers all four reaches me; work that misses one goes back to the group.
