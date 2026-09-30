# Briefing note: Kalpa Health, from Dr Priya Menon

**From:** Dr Priya Menon, COO, Kalpa Health
**To:** the data and AI team, Kalpa's Global Capability Centre, Bengaluru
**Re:** Q2 volumes, and five questions my team cannot answer

Kalpa Health and everyone in it are fictional. Any resemblance to a real company is coincidental.

---

## What I am looking at

My dashboard shows test volumes up 5 percent from Q1 to Q2. The plan the board approved for the year
asks for 18. I present to the board shortly, and I cannot tell them which branch of the business is
short, because every head I ask gives me a different reason and a different number.

We run diagnostic laboratories and walk-in clinics in six cities: Bengaluru, Mumbai, Delhi, Chennai,
Hyderabad and Pune. Each city has one laboratory and two walk-in clinics. Patients book tests or
packages by walking in, on the app, by phone, or for collection at home, and our corporate accounts
book health checks for their staff. Our financial year runs April to March, so Q1 is April to June
and Q2 is July to September 2026.

> "I do not need a dashboard. I need to know where the 13 points went, and what to do next."
> Dr Priya Menon

## What my team is asking

Each of my heads has raised a question with me. I have written each one the way it was put to me.

| # | Who is asking | What they asked me |
|---|---|---|
| 1 | The finance head | "The board will ask me where the plan's growth went. Where does our lab revenue actually come from, and which branch of it is short?" |
| 2 | The clinics' operations head | "Bookings fell in two of our cities in Q2. Before I send a field team or cut staff there, I need to know how far they fell, and why." |
| 3 | The finance head | "The invoices say one thing and the collections say another. Which invoices are unpaid, how much money is that, and can I trust the figure I report?" |
| 4 | The clinics' operations head | "KH-HYD-03, one of our Hyderabad walk-in clinics, has the worst no-show rate on my monthly report. I am being asked to add a receptionist there or close it. Is the clinic really worse?" |
| 5 | The marketing head | "Our free home-collection offer lifted bookings 9 percent. I want to offer it to every patient in all six cities. Can you confirm it worked?" |

I want one answer per question: a sentence I can carry into the board meeting, the evidence behind it,
what would change it, and what you would have me do.

## What my data team has sent you

Ten files, exported as each system gives them. My data team has written up every file and column in
the data dictionary (`C2_W03_D01_data_dictionary_STUDENT.md`). They have told me two things they
already know, and they are in the dictionary too: two cities changed booking systems in Q2, and the
payment feed has a different id format from the invoice export.

| File | The system it comes from |
|---|---|
| `C2_W03_D01_patients_STUDENT.csv` | The patient register |
| `C2_W03_D01_clinics_STUDENT.csv` | The site list, laboratories and walk-in clinics |
| `C2_W03_D01_test_catalogue_STUDENT.csv` | The test and package price list |
| `C2_W03_D01_bookings_legacy_STUDENT.csv` | The booking system we have used since before Q1 |
| `C2_W03_D01_bookings_newsys_STUDENT.csv` | The new booking system |
| `C2_W03_D01_booking_tests_STUDENT.csv` | The tests and packages on each booking |
| `C2_W03_D01_invoices_STUDENT.csv` | The billing export |
| `C2_W03_D01_payments_STUDENT.csv` | The payment feed: the gateway and the clinics' cash desks |
| `C2_W03_D01_appointments_STUDENT.csv` | The walk-in clinics' visit register, Q2 |
| `C2_W03_D01_campaign_STUDENT.csv` | The free home-collection offer: who was offered it, and who took it up |

They are in `data/` beside this pack, and every group holds the same files.

## How this week runs for you

You are the analysts I will question. Each group takes one of the five questions, and the Programme
Head allocates them on Monday 19 October. Each group presents to a panel on Friday 23 October where
the roster allows, or on Saturday 24 October, with a live demo run on these files, and the panel will
ask for your opinion, your evidence and what you would have done differently. Your group's brief
(`C2_W03_D01_brief_{n}_{name}_STUDENT.md`) says what your question feeds and what you ship.

Before anyone opens a notebook, write my question in your own words and say which part of the method
you already know answers it. That is Monday's work, in the translation worksheet
(`C2_W03_D01_translation_worksheet_STUDENT.md`).

## How you are scored

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
<!-- /sync:rubric:W03 -->

## Who checks your work

My team will review everything before it reaches me. Kavya Nair, the senior analyst on your team at the GCC, checks
each group's work before it leaves the team: the baseline, the denominator, the evidence, and a second way
to reach the same number.
