# The three timed cases: model answers

**TRAINER ONLY.** Read each model answer only after the two call-outs. Each is written as a strong
0 to 3 year candidate would say it aloud in about two minutes. The prompts are in
`exercises/unguided/C2_W01_D05_timed_cases_STUDENT.md`.

## The clock for each case, 13 minutes

| Part | Minutes |
|---|---|
| Read, silently | 1 |
| Think, on paper | 3 |
| Answer aloud in pairs, two minutes each | 4 |
| Two call-outs to the room | 3 |
| The model answer and one line on what separated the call-outs | 2 |

One minute at the start sets up the round, so the three cases fill the 40-minute slot.

## Case 1: two hours and a raw export

**Tag.** [F] You have two hours and a raw export; what do you do first, and what do you skip?
Descends from the Friday row's interview angle and Tuesday's [S] sales-drop question.

**The model answer.** "First I agree the question: sales is booked order value, last month against
the month before, same number of days. Then twenty minutes on the file before any number: rows,
distinct order ids, how many amounts convert, the date range, and whether the export has a control
total I can reconcile to. I clean with a written log, and before I compute the drop I check that my
cleaned total matches the finance or source-system total for both months, because a duplicated
batch or a lost amount can make the drop look bigger or smaller than it is. Then the tree: orders,
customers, orders per customer, order value, by city or cuisine, whichever split the business runs
on. I skip anything that does not change the answer today: charts beyond one, a significance test on
every segment, a second data source. I never skip the reconciliation, because a drop measured on an
unreconciled file is not a finding."

**What separates the answers.** The weak answer opens with a chart of the fall. The good one profiles
first. The strong one names the reconciliation as the thing never skipped and says why, and names
what it skips out loud.

## Case 2: zero rejects and a Rs 20 lakh gap

**Tag.** [S] Walk me through how you clean and check a dataset you have never seen. Descends from
Wednesday's [S] "Finance and your dashboard disagree; what do you do?" and Saturday's [D] anchor on a
cleaning run that reports zero rejects.

**The model answer.** "Zero rejects on a new system's export makes me suspicious before it makes me
comfortable, because something in 50,000 rows is almost always odd. I check three things in order.
One: rows against distinct order ids, since a repeated batch is the commonest way a dashboard runs
high. Two: how my code handled values that would not convert; if it set them to zero or skipped them
silently, the rejects count is hiding them. Three: a rupee reconciliation by month or quarter
against Finance's total, not just a row count, and a bridge that walks from my number to theirs step
by step. Until the bridge lands I tell Finance that I have a gap of Rs 20 lakh I cannot yet explain,
that their number is the reference until I can, and when I will come back. I do not tell them their
number is wrong."

**What separates the answers.** The weak answer defends the dashboard. The good one checks for
duplicates. The strong one distrusts the zero, checks the conversion handling, reconciles in rupees
and treats Finance's figure as the reference until the bridge lands.

## Case 3: 42 percent on twelve visits

**Tag.** [D] A stakeholder attacks your caveat in front of the room; how do you hold it without
overclaiming? Descends from Friday's [D] and Thursday's [F] "42 percent on 12 users against 31
percent on 1,200".

**The model answer.** "Forty-two is higher than thirty-one, and I would like it to be true too. It
rests on five conversions out of twelve visits, so a week with two fewer would read as twenty-five
percent. What the data says today is that the new flow is not obviously worse, and nothing more. I
am not asking to stop it; I am asking to send a fixed share of traffic to it for long enough to get
a few hundred visits, which at our volume is about a week, and to decide on that number. If it holds
above thirty-one there, we ship it with evidence. If we ship now and it is really at twenty-five, we
will have lost a week of conversions without knowing it."

**What separates the answers.** Folding ("fine, ship it") and overclaiming ("it is noise, ignore
it") are the two weak answers. The strong one restates with the count, bounds what the data can say,
and offers a test with its size and time, which turns the caveat into a plan.

## The interview questions of the day, in one breath each

| Tag | Question | The answer in one breath |
|---|---|---|
| [S] | Walk me through how you clean and check a dataset you have never seen. | Profile every field, clean with a written reason per decision, reconcile counts and rupees to a source total, and only then analyse. |
| [S] | Tell me about an analysis you did: what did you find, and how sure are you? | Claim with its number and denominator, the evidence and how it was checked, the caveat that would change it, and the action. |
| [F] | You have two hours and a raw export; what do you do first, and what do you skip? | Profile first, never skip the reconciliation, and skip anything that does not change today's answer. |
| [D] | A stakeholder attacks your caveat in front of the room; how do you hold it without overclaiming? | Restate with the denominator, bound what the data says, and offer the test that would settle it. |
