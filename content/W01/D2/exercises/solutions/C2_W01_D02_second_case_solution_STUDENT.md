# Solution: the second case, the hypothesis Marketing attacks

Answers: 1c 2a 3d 4b 5c 6d

## The idea being tested

A cause handed over by a stakeholder is a hypothesis, and the data in hand can test it before any
new data is asked for: did the fall start after the cause, and did it fall where the cause acts?
When the file cannot settle it, the answer names the data that would, and says which of the two
hypotheses each piece of data tests.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | c | The set of Q2 customer ids sits wholly inside the Q1 set: all 69 bought in both quarters, none lost and none new, so a flat count hides no churn here. | a: a rate cannot show which people bought. b: sign-ups are not buyers, and no new buyer appears in the orders. d: delivered orders are a different definition, and the ids still overlap. |
| 2 | a | Retail-Plus is Rs 65,250 of the Rs 70,280 consumer fall, 93 percent, and 25 of the 28 lost orders; the same 22 members went from 51 orders to 26, and those who ordered three times now order once. | b answers a behaviour question with rupees. c: its revenue per order rose because small orders fell away, and paying more is not what happened. d waits when the evidence is already in the file. |
| 3 | d | Six weeks back from this week reaches late August. The monthly counts fell in July, from 14 in April and 13 in June to 9, before the break the complaint dates. After 24 August, Retail-Plus placed 8 orders, against 18 from 1 July to 24 August; whether the break deepened the fall rests on eight orders, which is Thursday's kind of question. | a reads the lowest month as proof of the cause. b miscounts six weeks. c: monthly counts can say whether the fall started before or after a date, which is the first test. |
| 4 | b | Web fell from 24 to 9, store from 14 to 9 and app from 13 to 8. Every channel fell together, which an app-only cause would not produce. | a: the app fell too, so "no effect" is more than the data says. c credits the whole app fall to the break with no timing. d swaps one unproved cause for another. |
| 5 | c | H1 needs the app's reorder events and failures by week, the release that broke it, and whether members who used reorder in Q1 fell more than those who did not. H2 needs the tier's change log for benefits, prices and delivery terms, renewals and members' support tickets. | a: more of the same file carries none of the fields that separate the two. b: stated reasons are weak evidence and 22 answers settle neither. d tests a third cause nobody has proposed. |
| 6 | d | A season repeats: if last year's Q2 shows the same dip for members and not for Retail-Core, the season is the story; if last year held flat, it is not. Retail-Core kept 95 percent of its Q1 orders this year against Retail-Plus's 51, which already argues against a season that hit everyone. | a: more months of this year cannot separate a season from anything else. b tests the other hypothesis. c: a season is tested by its repetition, which the data can show. |

The comparison segment: Retail-Core ordered 13, 12, 13, 12, 12 and 12 times across the six months,
flat, which is what a segment untouched by either cause looks like.

## The part worth arguing about

Item 3. The complaint is real and the button may well be broken. The point is narrower: the fall
began before the break, so the break cannot be the whole story, and it may have deepened a fall
already under way. The sentence that holds in the room is "the reorder feature is a hypothesis; the
fall began in July, before the break the complaint dates, so we are asking for the app's reorder
logs."

## Where the pattern lives in production

Product analytics teams run this test every time a stakeholder arrives with a cause: check the
timing against the change log, check whether the metric moved only where the cause acts, and name
the event data that would settle it. The interview version is "a stakeholder hands you a cause; how
do you test it with the data you have and name the data you need?"

## Hands-on picks

The executed solution, `exercises/solutions/C2_W01_D02_05_second_case_solution_STUDENT.ipynb`,
carries the set overlap, the monthly and channel counts and the split at 24 August, each with the
check it passes.
