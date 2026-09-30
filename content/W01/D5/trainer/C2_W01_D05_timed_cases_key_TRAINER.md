# The three timed design cases: model answers

**TRAINER ONLY.** Read each model answer only after the two call-outs. Each is written as a strong
0 to 3 year candidate would say it aloud in about two minutes. The prompts are in
`exercises/unguided/C2_W01_D05_timed_cases_STUDENT.md`. The situations are set at Kalpa and every
number marked illustrative there is invented for the case; the real-company facts were checked on 30
September 2026, with their sources below and in the provenance.

## The clock for each case, 13 minutes

| Part | Minutes |
|---|---|
| Read, silently | 1 |
| Think, on paper | 3 |
| Answer aloud in pairs, two minutes each | 4 |
| Two call-outs to the room | 3 |
| The model answer and one line on what separated the call-outs | 2 |

One minute at the start sets up the round, so the three cases fill the 40-minute slot.

## Case 1: Meera's first read, two hours after the export lands

**Tag.** [F] You have two hours and a raw export; what do you do first, and what do you skip?
Descends from the Friday row's interview angle and Tuesday's [S] sales-drop question.

**The best fit.** C, about 90 of the 120 minutes, which leaves 30 for the note and a buffer.

**The sizing.** The lab's pace: profile 20, clean with a log 30, reconcile 15, decompose 25, so C is
90; B adds the shuffle test (15) and the note (15), which fills the two hours only if nothing on the
file breaks. A takes 10 minutes and this morning a pass of that kind reported Q2 up 11.8 percent where
the books said down 28.5. D is right on the numbers and misses the meeting.

**What would switch it.** No control total from the ERP: reconcile rows against distinct ids and
state the first read as unreconciled in the caveat, or move to D for anything Meera will spend on. A
segment gap Meera is going to act on: B, so the note can say whether chance produces it, and the
decomposition is cut to the segment in question. A file of millions of rows: the same method in the
warehouse, which is Week 2.

**The model answer.** "I would run C: profile, clean with a log, reconcile, decompose, about ninety
minutes, and send the note marked provisional with no test. The step I never drop is the
reconciliation, because this morning's lab showed a skipped one can flip the sign of the headline,
and it costs fifteen minutes. I skip the shuffle test unless Meera is about to act on a gap between
segments; then I cut the decomposition to that gap and run the test. If there is no control total to
reconcile to, I say so in the first line. DMart does something similar every quarter: its revenue
goes out days after the quarter ends, marked provisional, before the board signs the results."

**What separates the answers.** The weak answer opens with a chart. The good one profiles first. The
strong one sizes the options against the two hours, names the reconciliation as the step never
dropped with its reason, and names the fact that would switch the plan.

**The real company.** Avenue Supermarts (DMart), Q2 FY26 business update released 3 October 2025:
standalone revenue from operations Rs 16,218.79 crore against Rs 14,050.32 crore a year earlier, 432
stores at 30 September 2025, figures provisional and subject to limited review; results approved by
the board on 11 October 2025. Bajaj Broking, https://www.bajajbroking.in/share-market-news/dmart-q2-fy2025-26-results-revenue-at-rs-16218-79-crore
(verified 30 Sep 2026); IndiaCSR, https://indiacsr.in/dmart-q2-fy26-results-revenue-rises-15-4-to-rs-16218-79-cr-store-count-at-432/
(verified 30 Sep 2026).

## Case 2: zero rejects and a Rs 20 lakh gap, after the migration

**Tag.** [S] Walk me through how you clean and check a dataset you have never seen. Descends from
Wednesday's [S] "Finance and your dashboard disagree; what do you do?" and Saturday's [D] anchor on a
cleaning run that reports zero rejects.

**The best fit.** A, then B, then C; D only for any month C cannot close.

**The sizing.** A and B cost a cell each and seconds of compute on 50,000 rows, and between them they
catch the two commonest reasons a new system's total runs high: a batch posted twice and a value the
code set aside without saying. C costs about 30 minutes and tells you whether A and B explained the
whole Rs 20 lakh, and in which month any remainder sits. D costs most of a day and a ledger request,
so it is spent only where C points.

**What would switch it.** A shows rows equal to distinct ids and B shows every value summed or logged:
go straight to C and read the month. C's gap sits in one month: D for that month only. Finance's
number itself is in doubt (a late journal, a reversal): the bridge is walked with Anand's team, and
the note says which figure is the reference.

**The model answer.** "Zero rejects on a first export from a new system makes me suspicious before it
makes me comfortable. I run the cheap checks first: rows against distinct order ids, because a
repeated batch is the commonest way a dashboard runs high, and what my code did with values it could
not read, because a try that sets them to zero hides them from the reject count. Each is a cell. Then
a rupee bridge by month against Finance, about half an hour, which tells me whether those two
explained the whole Rs 20 lakh. Only the month the bridge cannot close gets matched order by order.
Tonight I tell Anand that his number is the reference, that I have a gap I can size but not yet fully
explain, and when I will come back. TSB is the reminder of what trusting a migrated system's output
costs: 1.9 million customers could not see their accounts."

**What separates the answers.** The weak answer defends the dashboard. The good one checks for
duplicates. The strong one orders the checks by cost against what each catches, stops where the
bridge closes, and treats Finance's figure as the reference until then.

**The real company.** TSB: the FCA and PRA fined TSB £48,650,000 in total on 20 December 2022 for the
April 2018 migration to a new IT platform, which affected a significant proportion of its 5.2 million
customers. FCA, https://www.fca.org.uk/news/press-releases/tsb-fined-48m-operational-resilience-failings
(verified 30 Sep 2026). The 1.9 million customers unable to view their accounts and the move from
Lloyds Banking Group's platform to Sabadell's Proteo4UK come from the Slaughter and May review as
reported by The Register, 19 November 2019,
https://theregister.com/2019/11/19/tsb_slammed_for_big_bang_it_approach_behind_disastrous_migration
(verified 30 Sep 2026).

## Case 3: 42 percent on twelve visits

**Tag.** [D] A stakeholder attacks your caveat in front of the room; how do you hold it without
overclaiming? Descends from Friday's [D] and Thursday's [F] "42 percent on 12 users against 31
percent on 1,200".

**The best fit.** C, a split test until each checkout has about 300 visits, about half a week.

**The sizing.** To tell 42 percent from 31 percent with the conventional 5 percent false-alarm rate
and an 80 percent chance of seeing a real difference, each checkout needs about 300 visits (the
standard two-proportion sample-size formula gives 299.5). At about 1,200 visits a week, a half split
reaches 300 each in roughly three and a half days. B would take about 25 weeks at 12 visits a week. D
gives the new checkout about 240 visits in a fortnight, short of 300. And A bets on 5 conversions: if
the new checkout were really at 31 percent, 5 or more of 12 would still happen in about 3 weeks of 10.

**What would switch it.** A new checkout that could lose money if it is worse (a payment step
that fails): C with one visit in ten, run for longer. Traffic of a dozen visits a week, as Student's
orders were on Thursday: no test settles it within a quarter, so decide on the cost of being wrong and
how easily it can be reversed. A change that is free to reverse within a day: ship it behind a switch
and measure it as it runs, which is C by another name.

**The model answer.** "Forty-two is higher than thirty-one, and I would like it to be true too. It
rests on five conversions out of twelve visits, and if the new checkout were really no better, five
of twelve would still turn up in about three weeks out of ten. What the data says today is that the
new flow is not obviously worse, and nothing more. I am not asking to stop it. I am asking to send half
of next week's traffic to it until each checkout has about 300 visits, which is about half a week,
and to decide on that number. If it holds above thirty-one, we ship it with evidence. If we ship now
and it is really at thirty, we will have lost conversions without knowing it. Bing's biggest headline
win was checked like this before anyone believed it."

**What separates the answers.** Folding ("fine, ship it") and overclaiming ("it is noise, ignore it")
are the two weak answers. The strong one restates with the count, sizes the test in visits and days,
and names the condition under which it would ship without one, which turns the caveat into a plan.

**The real company.** Microsoft Bing: "an idea about changing the way the search engine displayed ad
headlines... languished for more than six months"; when tested, a "too good to be true" alert fired,
and the analysis "showed that the change had increased revenue by an astonishing 12%, which on an
annual basis would come to more than $100 million in the United States alone". Ron Kohavi and Stefan
Thomke, "The Surprising Power of Online Experiments", Harvard Business Review, September to October
2017, https://hbr.org/2017/09/the-surprising-power-of-online-experiments (verified 30 Sep 2026). The
article says the result tripped an alert and analysis confirmed it; it does not say the test was re-run,
so the model answer says "checked", never "re-run".

**The arithmetic, for a TA asked.** Sample size per arm n = (1.96 x sqrt(2 x 0.365 x 0.635) + 0.8416
x sqrt(0.31 x 0.69 + 0.42 x 0.58))² / 0.11² = 299.5. The chance of 5 or more conversions in 12
visits at a true 31 percent is 0.303.

## The interview questions of the day, in one breath each

| Tag | Question | The answer in one breath |
|---|---|---|
| [S] | Walk me through how you clean and check a dataset you have never seen. | Profile every field, clean with a written reason per decision, reconcile counts and rupees to a source total, and only then analyse. |
| [S] | Tell me about an analysis you did: what did you find, and how sure are you? | Claim with its number and denominator, the evidence and how it was checked, the caveat that would change it, and the action. |
| [F] | You have two hours and a raw export; what do you do first, and what do you skip? | Profile first, never skip the reconciliation, and skip anything that does not change today's answer. |
| [D] | A stakeholder attacks your caveat in front of the room; how do you hold it without overclaiming? | Restate with the denominator, bound what the data says, and offer the test that would settle it, with its size and time. |
| Design | Which approach fits, sized how, and what would make you switch? | Name the options, size each in minutes and in the error it leaves, choose the cheapest that lands on the reference, and name the fact that moves you to the next. |
