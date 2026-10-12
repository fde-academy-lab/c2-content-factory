# Scorecards, Week 4 Tuesday: how does each answer in the interview room score, and why?

**TRAINER ONLY.** The scored copies of the two transcripts and the AI-company variant in
`extras/C2_W04_D02_interview_room_STUDENT.md`. Pairs score in class from the criteria on slide S52;
this page is the trainer's key for the comparison that follows. Seven criteria, each 0 to 2, are the
programme's own; Aced's guide to analyst interviews supports two of them, that the interviewer
listens for the estimation framework over a precise number and wants each assumption stated so it can
be challenged (checked 12 October 2026). Only what the main answer says is scored; a line that first
appears in a follow-up earns nothing here.

**Who needs the answer.** The trainer reading the pairs' scores, and the Saturday mock round, which
reuses these questions.

**The questions on the way.** How does each answer score on each criterion? What separates a 1 from a
2? Which follow-up breaks a weak answer, and which ones does a strong interviewer add?

## How do the two answers to "present this to a non-technical leader" score?

| Criterion | Weak | Hire-grade | What earns the 2 |
|---|---|---|---|
| Clarified the scope first | 0 | 2 | Asked which decision, who else hears it and how long the slot is, and opened the answer on the decision |
| Named the denominator and the window | 1 | 2 | "An hour a driver spends online at peak", six weeks after the launch on 31 August against six weeks before |
| Saw the trap | 0 | 2 | Named the per-driver-week rise and checked it: four more online hours a week at 17 percent less per hour, the joiners pulling it down |
| Sized it with a unit | 1 | 2 | Rs per peak online hour; Rs 2,836 of top-up per extra trip; Rs 58 lakh to Rs 92.7 lakh over six weeks with its assumption |
| Said what would change their mind | 0 | 2 | "If it shows completed trips per driver falling, or the wait in any zone rising, I would drop the change" |
| Tied it to a decision and its cost | 1 | 2 | A six-week test on half the drivers, picked at random, the city head signing it, and the saving in rupees |
| Gave the structure before the number | 0 | 2 | The decision and the claim come before any number |
| **Total** | **3 of 14** | **14 of 14** | |

The weak answer earns its three points by naming trips per hour, reading numbers with units and
naming pay per trip; it loses the rest by opening on the dashboard and calling the picture mixed.

## How do the two answers to "how many drivers at the evening peak?" score?

| Criterion | Weak | Hire-grade | What earns the 2 |
|---|---|---|---|
| Clarified the scope first | 0 | 2 | Online at one moment, the three-hour weekday evening window, one product, the city's median wait under five minutes |
| Named the denominator and the window | 1 | 2 | Trips an hour in the evening window; trips per online driver-hour |
| Saw the trap | 0 | 2 | Named it ("an hour's trips over an hour's rate, never the day's") and checked like for like, per completed trip |
| Sized it with a unit | 1 | 2 | Trips per 100 people, carried through to about 5,700 drivers and the checked 5,000 to 5,700 |
| Said what would change their mind | 0 | 2 | The check moved the answer, and Uber's own count of drivers online at peak would replace the guess |
| Tied it to a decision and its cost | 0 | 2 | The number sets the evening incentive: up to Rs 9 lakh an evening for each thousand drivers held online with no trips |
| Gave the structure before the number | 0 | 2 | The formula is said before any multiplying |
| **Total** | **2 of 14** | **14 of 14** | |

## How do the two answers in the AI-company variant score?

| Criterion | Weak | Hire-grade | What earns the 2 |
|---|---|---|---|
| Clarified the scope first | 0 | 2 | Asked what the team is judged on, whether deleted suggestions count, what the business is paid on and whether users can be held out |
| Named the denominator and the window | 0 | 2 | Characters still in the file seven days after acceptance, per developer who saw a suggestion that week |
| Saw the trap | 0 | 2 | Accepting and then deleting inflates acceptance, and dropping acceptance ignores what customers buy on; the holdout checks which number tracks renewals |
| Sized it with a unit | 0 | 2 | Characters retained; 32 percent accepted becomes about 26 percent retained (invented) |
| Said what would change their mind | 0 | 2 | "If acceptance tracks renewals and retained code does not, I would keep acceptance as the north star" |
| Tied it to a decision and its cost | 1 | 1 | A decision (which number the team is judged on) with serving cost named but no rupees; a 2 puts a rupee figure on the renewals or the serving cost at stake |
| Gave the structure before the number | 1 | 2 | The claim, then the proposal, then the concession |
| **Total** | **2 of 14** | **13 of 14** | |

The hire-grade answer is left at 1 on the decision criterion on purpose: ask the room which one
sentence would earn the 2.

## Which follow-ups break a weak answer?

| Transcript | The follow-up | What a weak candidate does | What a hire-grade candidate does |
|---|---|---|---|
| Present it | "Which denominator did you choose?" | Names none, or names per driver-week because it rose | Per peak online hour, the unit the scheme pays in; under a per-trip scheme, completed trips per enrolled driver and top-up per completed trip |
| Present it | "The finance partner says it is the monsoon." | Quotes the six-week rise in requests, or drops the recommendation | The last three weeks: requests back inside the before range, trips per hour still 1.56 |
| Drivers at the peak | "Your idle share is a guess. What in the data would catch it?" | Quotes hours with no trip as if they were idle at a moment | Like for like from trips per hour: about 0.21 before the launch, the window that held the wait at 4.8 minutes, which gives about 5,000 |
| Drivers at the peak | "The window is three hours. What does a four-hour window do?" | About 4,300 drivers, since the average hour fell | Nothing at the busiest moment: the buffer rises to about 1.53 and the answer stays about 5,700 |
| AI variant | "Isn't retained code easy to game too?" | Points at build failures and revert rate, which padding passes | Ratio guardrails: retained characters per accepted character, and edits per accepted suggestion |

## Which follow-ups does a strong interviewer add, and what answers them?

| Transcript | The follow-up | The line that survives it |
|---|---|---|
| Present it | "What is the per-trip rate, and why does a fifth of the money still paid mean anything?" | Monday left the rate open; the saving assumes drivers who start accepting are paid about what the floor paid them. Requests rose only 1.8 percent, so most of the trips that newly accepting drivers complete would otherwise go to drivers already serving: the uncertain number is the per-trip rate more than the uptake, and the test sets it |
| Present it | "What did riders get, and where are the idle hours?" | A median wait of 4.8 to 4.6 minutes; 74 percent of the idle money sat in the three outer zones, which still ran about six minutes, so median wait by zone is the guardrail |
| Present it | "Where do you set the acceptance floor, and what stops accepting and then cancelling?" | At half the offers, in the gap Monday's data shows (no idle-tail week above 46 percent, no other week below 78 percent); driver cancels rose from 4 to 9 percent, so the floor counts accepted trips net of cancels |
| Drivers at the peak | "Is your 1 percent riders or trips?" | Trips per 100 people; a commuter riding both ways counts twice, and doubling the factor doubles the answer, to about 11,400 |
| Drivers at the peak | "Where did five minutes enter your arithmetic?" | Through the idle share: the before window held a 4.8-minute median at an idle share near 0.21, and the outer zones ran 6.6 minutes even then, so the median is read by zone |
| Drivers at the peak | "A driver online on Uber may be on another app's trip." | Then the idle share overstates who is free, so lean it low and the answer up |
| AI variant | "A study of GitHub Copilot's users found acceptance tracks how productive developers feel. Why judge the team on retention?" | Because feeling is not the outcome: METR's 2025 randomised study found experienced developers took 19 percent longer with AI tools while believing they were 20 percent faster (METR now calls those results out of date), so the holdout reads renewals |

## What does the guesstimate rest on, and where is its anchor?

The estimate of drivers at the evening peak has no published anchor: the research ledger holds none, and a search on
12 October 2026 found only undated or decade-old counts of drivers signed up, a different unit. The
slot reads "to be found", and the case data checks one ratio like for like instead: 0.53 online
driver-hours per completed trip before the launch, against the chain's 0.60, which moves the answer to
about 5,000 to 5,700. The paired UPI estimate is anchored to 802 million a day in September 2026 (NPCI
via Outlook Money, 2 October 2026, checked 12 October 2026), with the catch that 24.07 billion over 31
days gives 776 million, and the sharper check that the month's value works out to about Rs 1,220 a
payment. The full worked versions are in `trainer/C2_W04_D02_guesstimate_TRAINER.md`.
