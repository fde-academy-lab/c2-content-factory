# Mock R1, the viva half: prompts per sub-problem

**TRAINER ONLY.** This is the assessors' file, so the plants and their numbers are written here. None
of it is said to a learner, hinted at, or confirmed when a learner guesses. A learner who asks
"is there something hidden in the data?" gets the question back: "What would you check?"

The viva runs eight minutes on the learner's own group's Kalpa Health work. It probes the
translation, which is the move the week trains: the Week 1 and 2 method carried into a domain the
room had never seen. A prepared answer holds on the first question and breaks on the second, and it
breaks soonest where the group's challenges log is thin.

## The eight minutes

| Minutes | Probe | Where it comes from | The rubric criterion it evidences |
|---|---|---|---|
| 1.5 | The opener, the same for every learner | The row's interview angle | The translation, with one decision defended by evidence (6) |
| 1.5 | The translation probe for the group's sub-problem | The row's thinking column | The translation, with one decision defended by evidence (6) |
| 2 | One plant probe for the group's sub-problem, chosen by seat | The spine's plant table | The translation, with one decision defended by evidence (6) |
| 2 | The caveat challenge for the group's sub-problem | The group's headline claim from Wednesday | Defending a caveat under challenge (6) |
| 1 | The looking-back probe | The group's challenges log and decisions log | What they would do differently (3) |

The rubric, rendered from `data/programme/facts.yaml`:

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

**Rotate by seat so group-mates meet different probes.** Each sub-problem below carries plant probes
numbered P1 to P4. Seat 1 takes P1, seat 2 takes P2, seat 3 takes P3 and seat 4 takes P4. The opener,
the translation probe, the caveat challenge and the looking-back probe stay the same for everyone,
since a learner's own words are what they test, and group-mates' answers to them should differ.

**Ask the learner to show the work.** The learner has the group's notebook or SQL, the decisions log
and the challenges log open. Ask for the cell or the log line behind a number at least once. A
learner who can find it in under a minute did the work or read it closely; a learner who searches and
cannot find it carried it.

## The three answers each probe is read against

Every probe below gives three things. **Did the work**: what a learner who built the piece says, with
the number, the unit and the check. **Carried it**: what a learner who presents a group-mate's work
says, usually the right headline without the mechanism. **The follow-up**: the one question that
tells them apart, because it moves the case one step past the headline. A carried answer is a
finding to note as it happened, and it is never a reason to argue with the learner in the room.

---

## The opener, every learner

**`[S]` "Walk me through the analysis you did on unfamiliar data and one decision you would
defend."** (The row's interview angle for this day.)

| Did the work | Carried it | The follow-up |
|---|---|---|
| Starts from Dr Menon's question and the group's sub-problem, names the files profiled and what surprised them, gives one decision from the decisions log with its count or rupees and the reason, and says what would change it | Starts from the tool or the chart, gives the group's headline, and names a decision in general words ("we cleaned the data", "we removed duplicates") | "What was the alternative to that decision, and what number would have come out if you had taken it?" |

---

## The headline, which every group met

Every group started from Dr Menon's words: test volumes grew 5 percent against a plan of 18. Use this
probe in place of a plant probe when a learner's sub-problem probe has already been used by the time
you reach them, or as a second plant probe for a learner who is racing through.

**What is planted.** The 5 percent is the dashboard's count: retail tests booked in the old booking
system only, a package counted as its component tests. Computed from the files: 23,213 tests in Q1
against 24,406 in Q2, which is 5.1 percent. Across both booking systems, tests booked grew 7.8
percent (23,213 to 25,022), tests performed on completed bookings grew 8.6 percent (22,468 to 24,399)
and bookings grew 5.6 percent (5,692 to 6,009). All four exclude the one corporate contract, whose
1,200 health checks add 6,000 tests to Q2; with it, tests booked would read about 34 percent growth.
Every honest reading is short of the plan of 18.

**H. "Dr Menon's dashboard says 5 percent. What is your number for growth, and what did you count?"**

| Did the work | Carried it | The follow-up |
|---|---|---|
| Names the unit (tests booked, tests performed or bookings), says both booking systems are in it, says the corporate contract is out or shown apart, and places the number against the plan of 18 | Quotes the group's percentage without the unit, or says the dashboard is wrong without saying what it counted | "Which of your numbers moves most if the corporate contract goes back in, and why is that a reason to keep it apart?" |

---

## Sub-problem 1, revenue: where lab revenue comes from, and which branch is short

**The translation probe (the row's "why this tree for a lab").** "Why this tree for a lab? Walk me down
your revenue tree for Kalpa Health, and tell me where it differs from Meera's."

| Did the work | Carried it | The follow-up |
|---|---|---|
| Patients, times bookings per patient, times tests per booking, times price per test, with packages as a bundle price, home collection as a fee, and the corporate contract as a separate branch; says the retail tree's "items per order" breaks on a package, which is one invoice line and many tests | Recites Meera's tree with lab words swapped in, and cannot say where a package or the corporate contract sits | "A full body checkup is one invoice line, twelve tests and Rs 2,999. Which leaf is it counted in, and what does that do to your price per test?" (Twelve tests at Rs 2,999 is Rs 250 a test, against a list-price sum of Rs 6,370; counting it as one test inflates price per test and hides volume.) |

**What is planted.** One corporate health-check contract in Q2: invoice KH/26-27/007802, account
CORP-0007, Rs 18,00,000, which is 16.2 percent of Q2's invoiced revenue of Rs 1,11,31,711. The Q2
mean invoice is Rs 1,904 with it and Rs 1,596 without it, against a median of Rs 1,499. Packages bill
as one line: 22,152 invoice lines outside the contract bill 46,867 tests on their completed bookings
(48,235 counting cancelled bookings, which the booking-tests file also lists). Invoiced revenue
outside the contract rose from Rs 85,74,238 in Q1 to Rs 93,31,711 in Q2, 8.8 percent; Chennai fell
5.4 percent and Pune 11.6 percent, while Hyderabad rose 26.2 percent. Thirty-five invoice amounts are
written with a thousands comma ("2,600"), so a numeric read of the column fails or skips them.

**P1. "What is the typical invoice in Q2, and what is behind the average?"**

| Did the work | Carried it | The follow-up |
|---|---|---|
| Median Rs 1,499, mean Rs 1,904; sorted and found one Rs 18 lakh invoice on a corporate account, 16.2 percent of Q2; mean Rs 1,596 without it; kept it and reported it as its own branch | Gives Rs 1,904 as typical, or says "we removed an outlier" | "Would you drop that invoice from the revenue Dr Menon sees?" (No: it is real, booked revenue; it goes on its own line, and the billing group will tell her it is unpaid.) |

**P2. "Dr Menon counts test volume. How many tests stand behind Q2's invoices, and how did you get
there?"**

| Did the work | Carried it | The follow-up |
|---|---|---|
| Counted tests from the booking-tests file, component and single-test lines, and got far more tests than invoice lines (48,235 in the file, 46,867 on completed bookings, against 22,152 invoice lines across both quarters, outside the contract) | Counts invoice lines or line items as tests | "Why do invoice lines and tests disagree, and which one is Dr Menon's volume?" (A package is one line and many tests; volume is tests.) |

**P3. "Which branch of the business is short, in rupees?"**

| Did the work | Carried it | The follow-up |
|---|---|---|
| Outside the contract, revenue grew 8.8 percent; the short branch is geographic, Chennai and Pune falling; separates price per test from volume, and says whether the fall is bookings or basket | Says "revenue grew 30 percent" (the total with the contract) or names a branch without a number | "If you give Dr Menon one number for the branch that is short, what is it and over which window?" |

**P4. "Some invoice amounts would not read as numbers. What did you do with them?"**

| Did the work | Carried it | The follow-up |
|---|---|---|
| Found the comma-formatted amounts (35 of them), stripped the comma, logged the rule, and checked the revenue total before and after | "We cleaned the amount column" | "How much revenue would have gone missing if those rows had been coerced to empty?" (It depends on the rows; a learner who did it can compute it in the notebook.) |

**The caveat challenge.** Ask for the group's headline claim and its caveat, then push as the COO: "Your caveat says the Rs 18 lakh contract distorts the averages. It is revenue. Why should I not count it?"

| Did the work | Carried it | The follow-up |
|---|---|---|
| Keeps it counted in revenue and shows it apart: the contract is real and it is 16 percent of Q2, so any average or growth rate with it inside describes one customer; the caveat is about which number describes the business, never about removing revenue | Removes the contract, or drops the caveat | "Would your recommendation change if the contract renews next quarter?" |

---

## Sub-problem 2, bookings: bookings fell in two cities in Q2

**The translation probe (the row's "why this identity rule for bookings").** "What makes two booking
rows the same booking, and why that rule?"

| Did the work | Carried it | The follow-up |
|---|---|---|
| The booking id within the old system, since the old export repeats rows from a re-export and some repeated rows differ in their update time; the new system's references have their own format, so the two systems are stacked with a system column and never deduplicated against each other | "We used drop_duplicates" | "Did the repeated rows match on every column? What would a whole-row dedupe have reported?" (Of the 180 repeated ids, 30 differ in the update time, so a whole-row dedupe leaves those 30 in.) |

**What is planted.** Chennai and Pune moved to the new booking system on 18 September; the old
system's export carries only its own bookings, with the two cities' last old-system date on
17 September. The new system's export has 153 bookings, with its own references (NB/MAA/..., NB/PNQ/...),
its own centre codes (MAA-01, PNQ-02), dd/mm/yyyy dates and its own status and channel words. The two
cities had 1,415 bookings in Q1; the old export alone shows 1,090 in Q2, a fall of 23.0 percent; with
the new system's 153, the real count is 1,243, a fall of 12.2 percent. The old export also repeats
180 rows from a mid-quarter re-export: 11,729 rows, 11,549 distinct booking ids.

**P1. "How much did bookings fall in Chennai and Pune?"**

| Did the work | Carried it | The follow-up |
|---|---|---|
| About 12 percent, 1,415 to 1,243, once the new system's bookings are added; the old export alone says 23 percent | Says 23 percent, or says 12 without being able to say where the other bookings came from | "How did you find out the new system existed, and on what date did it start?" (The data team told them two cities changed systems in Q2; the new export's first date is 18 September.) |

**P2. "Chennai's centres have different codes in the two systems. How did you line them up?"**

| Did the work | Carried it | The follow-up |
|---|---|---|
| The clinics file carries each site's new-system code (MAA-01 against KH-CHE-01), so the centres map one to one; the channel and status words were mapped too (DONE to completed, CXL to cancelled) | "We merged the two files" | "What would your Q2 cancellations show if CXL had been left unmapped?" (The new system's ten cancellations would vanish from the cancelled count.) |

**P3. "The real fall is still about 12 percent. Is that a real fall, or the switch again?"**

| Did the work | Carried it | The follow-up |
|---|---|---|
| Looked month by month: the two cities were falling before the switch, so part of the fall is real, and the switch doubled how it looked | Treats 12 percent as either all real or all artefact without evidence | "What would you ask the clinics' operations head to explain the fall that remains?" |

**P4. "The old export has more rows than bookings. How many, and why?"**

| Did the work | Carried it | The follow-up |
|---|---|---|
| 11,729 rows, 11,549 distinct ids, 180 repeats from a re-export; kept one per id, the latest update, and logged it | "There were some duplicates" | "Would the repeats have changed the two cities' fall?" (The learner who did it checks the repeats by city and quarter rather than guessing.) |

**The caveat challenge.** Ask for the group's headline claim and its caveat, then push as the finance head: "Your caveat says the two cities' numbers depend on stitching two systems together. I do not want caveats; did bookings fall or not?"

| Did the work | Carried it | The follow-up |
|---|---|---|
| Holds both halves: yes, bookings fell about 12 percent, and the 23 percent on the old dashboard is the system switch; the caveat is the size of the fall, never whether it happened, and it names what would shrink it (the new system's export being complete for the second half of September) | Drops the caveat under pressure and gives one number, or retreats to "it depends" | "What would you check tomorrow to make the caveat smaller?" |

---

## Sub-problem 3, billing: invoices and collections disagree

**The translation probe.** "In Week 2 you joined payments to orders on an order id both sides shared.
What was your join key here, and why?"

| Did the work | Carried it | The follow-up |
|---|---|---|
| An exact join on the invoice number matched almost nothing, because the payment feed keys invoices as bare digits (000123) or as INV-123, and only some as the full KH/26-27/000123; the key was normalised to the invoice's trailing number and the amounts were checked after | "We joined on invoice number" and a collected figure, with no word about the key | "INV-123 and 000123: how do you know they are the same invoice?" (Pad to six digits, match, then confirm the amounts agree.) |

**What is planted.** An exact join matches 247 of 11,289 payment rows, 2.2 percent; normalised, every
payment matches an invoice. Gateway retries double-post 229 payments: a second success on the same
reference and amount, about two minutes after the first. There are 102 refunds, as negative amounts.
398 invoices have no payment, worth Rs 24,47,805, of which Rs 18,00,000 is the corporate contract's
invoice. Invoiced across both quarters is Rs 1,97,05,949. The naive sum of successful payments is
Rs 1,76,13,398; without the double posts (Rs 3,55,254) and net of refunds (Rs 1,60,164), collected is
Rs 1,70,97,980, and the gap to invoiced is exactly the unpaid invoices plus the refunds.

**P1. "What share of payments matched on your first join, and what did you do about it?"**

| Did the work | Carried it | The follow-up |
|---|---|---|
| About 2 percent (247 of 11,289); saw the feed's three formats in a profile; normalised; every payment then matched | "The join worked after cleaning" | "How did you prove the normalised match was right, and not a coincidence of digits?" (The amounts agree on the matched pairs.) |

**P2. "Some invoices are paid twice. Did the patients pay twice?"**

| Did the work | Carried it | The follow-up |
|---|---|---|
| No: 229 are gateway retries, the same reference and amount two minutes apart, both marked success; counted once, logged, and listed for finance to confirm with the gateway | "We removed duplicate payments" | "A patient really does pay the same amount twice for two invoices. How does your rule avoid removing that?" (The rule is the same invoice reference, not the same patient and amount.) |

**P3. "What is still unpaid, and what would you tell the finance head first?"**

| Did the work | Carried it | The follow-up |
|---|---|---|
| 398 invoices, about Rs 24.5 lakh, and most of the rupees are one corporate invoice of Rs 18 lakh; the finance head hears about that one first | Gives a count of unpaid invoices with no rupees, or misses the corporate one | "Is the corporate invoice late, or is it a problem? What would you ask?" (Its payment terms; a contract may pay on terms longer than a quarter.) |

**P4. "Walk me from invoiced to collected in rupees."**

| Did the work | Carried it | The follow-up |
|---|---|---|
| Invoiced about Rs 1.97 crore; successful payments sum to about Rs 1.76 crore, which overstates collection by the double posts; net of those and of refunds, collected is about Rs 1.71 crore; the gap is the unpaid invoices plus the refunds | Gives collected as the naive sum, or cannot bridge the two numbers | "Which line of your bridge would you check first if finance's number differed from yours by Rs 3.5 lakh?" (The double posts.) |

**The caveat challenge.** Ask for the group's headline claim and its caveat, then push as the COO: "Your caveat says the double posts are gateway retries. My finance head says patients complain of being charged twice. Is your caveat hiding a problem?"

| Did the work | Carried it | The follow-up |
|---|---|---|
| Keeps the rule and says what evidence would change it: the retries sit about two minutes apart on one reference, which is a gateway pattern, and the list of 229 goes to finance to check against the gateway's own record and any refund requests; if patients were charged twice, the gateway shows two settlements | Concedes that patients may have paid twice, or insists without evidence | "Which single record from the gateway would settle it for one of the 229?" |

---

## Sub-problem 4, no-shows: one clinic's rate, real or noise

**The translation probe (the row's "what a fair comparison needed in a clinic").** "What did a fair
comparison between clinics need here?"

| Did the work | Carried it | The follow-up |
|---|---|---|
| The same denominator: the other clinics' visits include walk-ins, and a walk-in cannot be a no-show, so no-shows are compared on scheduled visits only; then the question is whether the gap on that base is bigger than chance on a small clinic | "We compared the no-show rate of each clinic" | "Can a walk-in be a no-show? So what does counting walk-ins do to a clinic's rate?" (It lowers it: more attended visits in the denominator.) |

**What is planted.** Clinic KH-HYD-03, a small clinic that runs by appointment, shows 19.2 percent
no-shows on all its visits (10 of 52) against 8.7 percent for the other clinics, whose visit counts
are about 42 percent walk-ins. On scheduled visits only, it is 20.0 percent (10 of 50) against 15.2
percent. If its true rate were 15.2 percent, ten or more no-shows in fifty would happen by chance with
probability 0.22.

**P1. "Is the clinic's no-show rate worse? Give me the two numbers you compared."**

| Did the work | Carried it | The follow-up |
|---|---|---|
| On scheduled visits, 20 percent (10 of 50) against about 15 percent; the doubled gap on all visits came from the others' walk-ins | "It is 19 percent against 9, more than double" | "Why did you drop the walk-ins from the others and not from this clinic?" (Dropped from every clinic; this one has almost none.) |

**P2. "Ten no-shows in fifty. Is that a real difference or noise?"**

| Did the work | Carried it | The follow-up |
|---|---|---|
| Ran a chance check, a shuffle or the binomial: at the others' rate, ten or more in fifty happens about one time in five, so the gap is within chance | Says "it is significant" or "it is not significant" with no test named | "Say that to the clinics' operations head in one sentence, without the word probability." |

**P3. "How many fewer no-shows would make this clinic look average?"**

| Did the work | Carried it | The follow-up |
|---|---|---|
| At 15.2 percent of 50, about 7.6, so two or three fewer no-shows; on a base this small, a couple of patients decide the headline | Cannot compute it, or answers in percentages only | "What sample would you need before calling this clinic worse?" (Months more of scheduled visits; the learner who did the work says what they would wait for.) |

**P4. "The operations head wants to retrain this clinic's front desk. What do you advise?"**

| Did the work | Carried it | The follow-up |
|---|---|---|
| Not on this evidence: the fair gap is inside chance; keep reading the rate on scheduled visits monthly and act if it holds; the cost of retraining is small, so a cheap reminder call trial is a fair middle | Agrees, because the rate "is double" | "What would change your advice?" |

**The caveat challenge.** Ask for the group's headline claim and its caveat, then push as the clinics' operations head: "You say the gap could be chance. Twenty percent is twenty percent. Why should I not act?"

| Did the work | Carried it | The follow-up |
|---|---|---|
| Holds it with the number: on fifty scheduled visits, two or three patients decide the gap, and a gap this size appears by chance about one time in five; acting is fine if it is cheap, and the caveat says what to measure next and for how long | Agrees the clinic is worse, or repeats "not significant" with no number | "If you had to give her one action today, what is it and what would it cost?" |

---

## Sub-problem 5, campaign: the free home-collection offer, cause or coincidence

**The translation probe.** "In Week 1 the monsoon discount looked like it worked in total. What was
the equivalent of the segment split here, and what did it show?"

| Did the work | Carried it | The follow-up |
|---|---|---|
| The split is by city, and within the campaign cities; offered patients book more in total and less inside every campaign city, so the 9 percent comes from who was offered it and where | Says "Simpson's paradox" with no city numbers, or confirms the 9 percent | "Where did the offer run, and what were those cities doing before it started?" |

**What is planted.** The offer went at random to half the patients in three cities that were already
rising, Bengaluru, Hyderabad and Mumbai, and to a fifth of patients elsewhere; inside the three cities
an offered patient books less than one who was not offered while the offer runs. Offered patients
(2,381, of whom 948 took it up) book 9.0 percent more than the rest in the offer window overall, and
less than the rest in every campaign city: Bengaluru 10.8 percent less, Hyderabad 19.9 percent less,
Mumbai 13.0 percent less. Before the offer the two groups book alike: from 1 April to 14 July, offered
patients booked within about 6 percent of the rest in each campaign city (Bengaluru 1.4 percent more,
Hyderabad 5.2 and Mumbai 6.1 percent less), so the files show who was offered and never how they were
chosen. The overall 9 percent comes from where the offer went: about half the patients in the
campaign cities were offered it against about a fifth elsewhere, and the campaign cities book more
per patient. The campaign cities rose 6.9 percent in the two months before the offer, and 7.4 percent
into the offer window, against 3.0 percent in Delhi over the same windows.

**P1. "Did the campaign lift bookings 9 percent?"**

| Did the work | Carried it | The follow-up |
|---|---|---|
| The 9 percent is offered against not offered, across all cities; inside each campaign city offered patients booked less, by 11 to 20 percent; so the 9 percent measures where the offer went | "Yes, 9 percent" or "No, it is a paradox" with no numbers | "So did the campaign reduce bookings?" (The files cannot settle it: they show who was offered and never how they were chosen, so the gap inside a city may come from who was chosen. A held-out random share would settle it.) |

**P2. "The campaign cities were growing. By how much, before the offer?"**

| Did the work | Carried it | The follow-up |
|---|---|---|
| About 7 percent in the two months before the offer, against about 3 in the comparison city, so the rise was under way | Does not know, or did not look before the offer | "What comparison would you have needed to credit the campaign with any of the rise?" |

**P3. "Who was offered the free collection? Were they like the patients who were not?"**

| Did the work | Carried it | The follow-up |
|---|---|---|
| Compared offered and not-offered patients in each campaign city before the offer: within about 6 percent of each other, with the sign changing between cities, so nothing before the campaign separates the two groups, the gap opens inside the offer window, and the files cannot say how the offer was assigned | Asserts that the offer went to drifting patients, or that it was random, without comparing the two groups before the offer | "How would you design the next wave so the question can be answered?" (Hold out a random share of eligible patients and compare.) If a group shows offered patients behind in the two months just before the offer: "Could chance give a gap that size between two groups this big?" |

**P4. "The marketing head says 948 people took it up, so it worked. Answer them."**

| Did the work | Carried it | The follow-up |
|---|---|---|
| Uptake says people used a free service, which they would do anyway; the question is whether they booked more than they would have, which uptake cannot answer | Agrees, or quotes the 9 percent | "What would you want to know about the 948 before and after the offer?" |

**The caveat challenge.** Ask for the group's headline claim and its caveat, then push as the marketing head: "You cannot prove the campaign did nothing. Your caveat is just doubt. I need budget for the next wave."

| Did the work | Carried it | The follow-up |
|---|---|---|
| Agrees the data cannot prove harm or help, which is the point of the caveat; offers the next wave as the test, with a random held-out share of eligible patients, so the budget buys an answer | Says the campaign failed, or gives in and agrees it worked | "How large a held-out share would you ask for, and what would you compare?" |

---

## The looking-back probe, every learner

**"From your challenges log: what would you do differently if you started this sub-problem again
tomorrow?"**

| Did the work | Carried it | The follow-up |
|---|---|---|
| Opens the log, finds an entry they wrote, names the step they would move earlier or do another way (profile both systems before any join, ask the data team a question on the first day) and the time or error it would have saved | Gives a general lesson ("manage time better") or reads an entry a group-mate wrote as if for the first time | "Which entry in your log shows the moment you should have changed course, and what told you?" |

If the group's challenges log has fewer than a handful of entries by Thursday, note it; the looking-back
probe then asks about the decisions log instead: "Pick one line in the decisions log and tell me who
decided it and what they looked at."
