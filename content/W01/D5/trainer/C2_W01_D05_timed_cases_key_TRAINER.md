# What does a strong answer to each timed design case say?

**TRAINER ONLY.** Read each model answer only after the two call-outs. Each is written as a strong
0 to 3 year candidate would say it aloud in about two minutes. The prompts are in
`exercises/unguided/C2_W01_D05_timed_cases_STUDENT.md`. The situations are set at Kalpa and every
number marked illustrative there is invented for the case; the real-company facts were checked on 30
September 2026, with their sources below and in the provenance.

**Who needs the answer.** The trainer, who shows the rehearsal deck's answer slide with each model
answer, and the TA who is asked where a size comes from.

## How do each case's 13 minutes run?

| Part | Minutes |
|---|---|
| Read, silently | 1 |
| Think, on paper | 3 |
| Answer aloud in pairs, two minutes each | 4 |
| Two call-outs to the room | 3 |
| The model answer and one line on what separated the call-outs | 2 |

One minute at the start sets up the round, so the three cases fill the 40-minute slot.

## Case 1: what do you leave out when Meera wants a first read in two hours?

**Tag.** [F] You have two hours and a raw export; what do you do first, and what do you skip? It
descends from the Friday row's interview angle and Tuesday's [S] sales-drop question.

**The best fit.** B, which profiles, cleans, reconciles and decomposes and sends the note marked
provisional, with no test, in 105 of the 120 minutes.

**The sizing.** At the lab's pace A costs 20 + 30 + 25 + 15 + 15 = 105 minutes, B 20 + 30 + 15 + 25 +
15 = 105, C 20 + 30 + 15 + 15 + 15 = 95 and D 30 + 15 + 25 + 15 + 15 = 100, so every plan fits the
clock and the choice is which step to leave out. A leaves out the reconciliation, the one step that
can flip the sign of the first line: on this morning's lab export (proposed for client zero v2.3) a
pass of that kind reported Q2 up 11.8 percent where the books said down 28.5. C skips the tree and tests one
segment's gap, so it answers one segment where Meera asked for all of them. D cleans a file nobody has profiled, so it cleans only the defects
someone already expected. B leaves out the test, which matters only when Meera is about to act on a
gap between segments, and the provisional label says what was not done.

**What would switch it.** If Meera is going to act on a segment gap, run B with the test on that gap
and trim the tree to find the minutes, or run C if she named the segment herself. If the ERP gives no
control total, B still fits, with the first line saying the read is unreconciled and naming the
ids-against-rows and every-value checks. A file of millions of rows takes the same method into the
warehouse, which is Week 2.

**The model answer.** "Every plan here costs about a hundred minutes, so I choose by the step each
leaves out. I would run B: profile, clean with a log, reconcile, decompose, and send the note marked
provisional with no test. The step I never drop is the reconciliation, because a skipped one can flip
the sign of the headline, and it costs fifteen minutes. I leave out the test because Meera is not yet
acting on a gap between segments; if she were, I would trim the tree and test that gap. If there is
no control total to reconcile to, I say so in the first line. DMart did the same for July to
September 2025: its revenue went out three days after the quarter ended, marked provisional, eight
days before the results were filed."

**What separates the answers.** The weak answer opens with a chart. The good one profiles first. The
strong one sizes all four plans, sees that the clock does not choose between them, names the
reconciliation as the step never dropped with its reason, and names the fact that would switch the
plan.

**The real company.** Avenue Supermarts (DMart) released its Q2 FY26 business update on 3 October
2025, with standalone revenue from operations of Rs 16,218.79 crore against Rs 14,050.32 crore a year
earlier and 432 stores at 30 September 2025, the figures provisional and subject to limited review;
it announced the quarter's results in a regulatory filing on 11 October 2025. Bajaj Broking, https://www.bajajbroking.in/share-market-news/dmart-q2-fy2025-26-results-revenue-at-rs-16218-79-crore (verified 30 Sep 2026); IndiaCSR, https://indiacsr.in/dmart-q2-fy26-results-revenue-rises-15-4-to-rs-16218-79-cr-store-count-at-432/ (verified 30 Sep 2026); the results filing on 11 October 2025, Business Today, 11 October 2025, https://www.businesstoday.in/markets/stocks/story/dmart-q2-results-avenue-supermarts-profit-rises-4-to-rs-685-crore-revenue-up-15-497833-2025-10-11 (verified 30 Sep 2026).

## Case 2: which check runs first when zero rejects meet a Rs 20 lakh gap?

**Tag.** [S] Walk me through how you clean and check a dataset you have never seen. It descends
from Wednesday's [S] "Finance and your dashboard disagree; what do you do?" and Saturday's [D] anchor
on a cleaning run that reports zero rejects.

**The best fit.** A, then B, then C, with D kept for any month C cannot close.

**The sizing.** A and B cost a cell each and seconds of compute on 50,000 rows, and between them they
catch the two commonest silent errors in a new system's total: a batch posted twice, which pushes the
total up, and a value the code set to zero without saying, which pulls it down and can hide inside a
larger gap. C costs about 30 minutes and tells you whether A and B explained the
whole Rs 20 lakh, and in which month any remainder sits. D costs most of a day and a ledger request,
so it is spent only where C points.

**What would switch it.** If A shows rows equal to distinct ids and B shows every value summed or
logged, go straight to C and read the month. If C's gap sits in one month, run D for that month only.
If Finance's number itself is in doubt (a late journal, a reversal), walk the bridge with Anand's
team, and let the note say which figure is the reference.

**The model answer.** "Zero rejects on a first export from a new system makes me suspicious. I run
the cheap checks first: rows against distinct order ids, because a repeated batch is the commonest
way a dashboard runs high, and what my code did with values it could not read, because a try that
sets them to zero hides them from the reject count. Each is a cell. Then I walk a rupee bridge by
month against Finance, about half an hour, which tells me whether those two explained the whole
Rs 20 lakh. Only the month the bridge cannot close gets matched order by order.
Tonight I tell Anand that his number is the reference, that I have a gap I can size but not yet fully
explain, and when I will come back. TSB is a loose reminder of what trusting a migrated system costs:
by The Register's report of the review, 1.9 million customers could not see their accounts."

**What separates the answers.** The weak answer defends the dashboard. The good one checks for
duplicates. The strong one orders the checks by cost against what each catches, stops where the
bridge closes, and treats Finance's figure as the reference until then.

**The real company, a loose likeness.** TSB's customers were locked out of a new platform, while
case 2 is a total trusted before it was reconciled; what the two share is that a new system's output
is the first thing to check. The FCA and PRA fined TSB £48,650,000 in total on 20 December 2022 for
the April 2018 migration to a new IT platform, which affected a significant proportion of its 5.2
million customers. FCA, https://www.fca.org.uk/news/press-releases/tsb-fined-48m-operational-resilience-failings (verified 30 Sep 2026). The 1.9 million customers unable to view their accounts is The Register's own wording in its report
of the Slaughter and May review, and the move from Lloyds Banking Group's platform to Sabadell's
Proteo4UK is the review's finding as The Register reports it, 19 November 2019,
https://theregister.com/2019/11/19/tsb_slammed_for_big_bang_it_approach_behind_disastrous_migration (verified 30 Sep 2026).

## Case 3: can 5 of 12 visits beat 31 percent of 1,200?

**Tag.** [D] A stakeholder attacks your caveat in front of the room; how do you hold it without
overclaiming? It descends from Friday's [D] and Thursday's [F] "42 percent on 12 users against 31
percent on 1,200".

**The best fit.** C, a half-and-half split until each checkout has about 300 visits, the case's
given size, which takes about half a week. D gathers more evidence than C, by the TA block's
arithmetic below, and takes four times as long, so it is the choice when a worse checkout costs
money.

**The sizing.** About 300 visits per checkout is the case's given size for a fair comparison of the
two rates, and the room takes it as given, beside the case file's second size, about 170 new-checkout visits
beside two thousand or more current ones on an uneven split: where both come from is a later week's
topic, Thursday's row puts it out of scope, and the arithmetic sits in the TA block below. At about 1,200 visits a week
a half split reaches 300 each in roughly three and a half days. D, one visit in ten for a fortnight,
puts about 240 visits on the new checkout beside about 2,160 on the current one, and the TA block
shows that is more evidence than C gathers, in four times the time. B, at about 12 pilot visits a
week beside 1,200 on the current checkout, takes about 14 weeks. And A bets on 5 conversions: if the
new checkout were really at 31 percent, 5 or more of 12 would still happen in about 3 weeks of 10.

**What would switch it.** If the new checkout could lose money when it is worse (a payment step
that fails), run D, one visit in ten for a fortnight, which limits the exposure and still gathers
more evidence than C. If the traffic is a dozen visits a week, as Student's orders were on Thursday,
no test settles it within a quarter, so decide on the cost of being wrong and how easily the change
can be reversed. If the change is free to reverse within a day, ship it behind a switch and measure
it as it runs, which gives C's comparison while the change is live.

**The model answer.** "Forty-two is higher than thirty-one, and I would like it to be true too. It
rests on five conversions out of twelve visits, and if the new checkout were really no better, five
of twelve would still turn up in about three weeks out of ten. Today the data says only that the new
flow is not obviously worse. I want to keep it live and send it half of next week's traffic until
each checkout has about 300 visits, which is about half a week, and then decide on that number. If
it holds above thirty-one, we ship it with evidence. If we ship now and it is really at thirty, we
will have lost conversions without knowing it. Bing's biggest headline win was checked like this
before anyone believed it."

**What separates the answers.** Folding ("fine, ship it") and overclaiming ("it is noise, ignore it")
are the two weak answers. The strong one restates with the count, sizes the test in visits and days,
and names the condition under which it would ship without one, which turns the caveat into a plan.

**The real company.** At Microsoft Bing, "an idea about changing the way the search engine displayed
ad headlines... languished for more than six months"; when it was tested, a "too good to be true"
alert fired, and the analysis "showed that the change had increased revenue by an astonishing 12%, which on an
annual basis would come to more than $100 million in the United States alone". Ron Kohavi and Stefan
Thomke, "The Surprising Power of Online Experiments", Harvard Business Review, September to October
2017, https://hbr.org/2017/09/the-surprising-power-of-online-experiments (verified 30 Sep 2026). The
article says the result tripped an alert and analysis confirmed it; it does not say the test was re-run,
so the model answer says "checked" and avoids "re-run".

**The arithmetic, for a TA who is asked; the room hears only the two sizes.** The given size comes from statistical power:
to tell 42 percent from 31 at the conventional 5 percent false-alarm rate with an 80 percent chance of
seeing a real difference, an equal split needs n = (1.96 x sqrt(2 x 0.365 x 0.635) + 0.8416 x
sqrt(0.31 x 0.69 + 0.42 x 0.58))² / 0.11² = 299.5 visits per checkout. For an unequal split the power
is the normal probability of 0.11 / sqrt(0.31 x 0.69 / n1 + 0.42 x 0.58 / n2) less 1.96: about 0.80 at
300 and 300, 0.91 at 2,160 and 240 (D), and 0.82 after 14 weeks at 1,200 and 12 a week (B); about 170
new-checkout visits beside the rest already reach 0.80, because the larger side is measured so
precisely. So D is more evidence than C, 0.91 against 0.80, in a fortnight against half a week. The
chance of 5 or more conversions in 12 visits at a true 31 percent is 0.303.

## How is each interview question answered in one breath?

| Tag | Question | The answer in one breath |
|---|---|---|
| [S] | Walk me through how you clean and check a dataset you have never seen. | Profile every field, clean with a written reason per decision, reconcile counts and rupees to a source total, and only then analyse. |
| [S] | Tell me about an analysis you did: what did you find, and how sure are you? | Give the claim with its number and denominator, the evidence and how it was checked, the caveat that would change it, and the action. |
| [F] | You have two hours and a raw export; what do you do first, and what do you skip? | Profile first, never skip the reconciliation, and skip anything that does not change today's answer. |
| [D] | A stakeholder attacks your caveat in front of the room; how do you hold it without overclaiming? | Restate with the denominator, bound what the data says, and offer the test that would settle it, with its size and time. |
| Design | Which approach fits, sized how, and what would make you switch? | Name the options, size each in minutes and in the error it leaves, choose the cheapest that lands on the reference, and name the fact that moves you to the next. |
