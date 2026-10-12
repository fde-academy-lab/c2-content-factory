# How does a strong candidate present the redesign, and size drivers at the peak, out loud?

Written for this programme in the style of product-company and GCC screens; the facts inside are from
the case file and the day's data. Two transcripts and one AI-company variant, each in the same order:
the question as the interviewer says it, the clarifying questions a strong candidate asks, the
structure, the trap the interviewer is fishing for, a weak and a hire-grade answer side by side, and
three follow-ups with the line a hire-grade answer gives each. No transcript claims to reproduce any
company's real interview.

> Illustrative case: the company is real, the situation and the data are synthetic, built for this class.

**Who needs the answer.** You, rehearsing aloud before a screen that asks you to present a finding or
size a number on the spot.

**The questions on the way.**

- How do you present a recommendation to a non-technical leader in two minutes?
- How do you size drivers at the evening peak, aloud?
- How does the same presentation sound at an AI company?

---

## How do you present a recommendation to a non-technical leader in two minutes?

**The question, as the interviewer says it.** "Here is the Hyderabad peak-hour guarantee case. You
have two minutes with the city head, who is not technical. Present your recommendation."

**The clarifying questions a strong candidate asks.** What decision is the city head making: redesign
the scheme, or extend it to more cities? Who else hears it: the driver-operations lead, the marketing
lead, the finance partner? Is two minutes the whole slot, or the opening before questions?

**The structure.** The claim; one number with its denominator and its window; the caveat; the action
with its cost and who signs; then one line on the number others will quote.

**The trap the interviewer fishes for.** Opening on method and reading out the dashboard, or quoting
the read that flatters the claim without naming its denominator: bookings per driver-week rose, which
sounds like success.

| A weak answer | A hire-grade answer |
|---|---|
| "So I looked at the dashboard. Peak online hours are up 24 percent and trips are up 3 percent. Trips per hour fell from 1.90 to 1.58, acceptance fell from 0.86 to 0.73, and I worked out bookings three ways. Bookings per driver-week is actually up, so the picture is mixed. I think we should probably look at the scheme again, maybe pay per trip, but there is a lot going on, including the monsoon." | "The scheme is paying for online hours that carry no trips. Over the six weeks after the launch on 31 August, against the six weeks before, an hour a driver spends online at peak brought in Rs 260 of fares instead of Rs 314, at the same Rs 165 fare, and Rs 1.16 crore of the Rs 1.9 crore top-up went to driver-weeks that accepted fewer than half their offers. The monsoon ended in the same weeks, so part of the fall may be the season; a test in a few zones settles it. I recommend paying per completed peak trip with an acceptance floor: Rs 58 lakh to Rs 92.7 lakh back over six weeks depending on whether half or a fifth of the idle drivers start accepting. You will hear that bookings per driver-week rose; that is 140 new drivers joining part-way, and it is not what the scheme pays for." |

**Three follow-ups, with the line a hire-grade answer gives.**

1. "What is the one caveat you would say before anyone decides?" "The monsoon ended inside the window and we have no weeks from last year, so I would test before extending."
2. "Which denominator did you choose, and what would make you choose another?" "Per peak online hour, because the scheme pays per online hour. If the scheme paid per trip I would read per trip, which is flat at Rs 165."
3. "The finance partner says it is the monsoon. Answer in under a minute." "You may be right about part of it, and I have no weeks from last year. Requests rose 1.8 percent, so demand did not fall, and the busiest three weeks after the launch still ran at 1.60 trips an hour. If last year's same weeks fell as far, I would change my view."

---

## How do you size drivers at the evening peak, aloud?

**The question, as the interviewer says it.** "Roughly how many drivers must be online at the evening
peak in a city like Hyderabad to keep rider wait under five minutes? Talk me through it."

**The clarifying questions a strong candidate asks.** Online at one moment, or counted across the
window? Which window, and how long is it? One platform or all of them? Is the target a median wait of
five minutes?

**The structure.** Clarify; map drivers online as requests an hour divided by the trips one online
driver completes in an hour, times a buffer; calculate aloud; give a range and its driving factor;
validate against a number counted the same way.

**The trap the interviewer fishes for.** Multiplying without fixing the unit, the window or the idle
share: a day's trips divided by an hour's rate.

| A weak answer | A hire-grade answer |
|---|---|
| "Hyderabad has about 1 crore people. Say 1 percent take a ride, so 1 lakh trips. A driver does about 2.4 trips an hour, so you need about 41,700 drivers." | "I will take drivers online at one moment of the three-hour weekday evening peak, Uber only, median wait under five minutes. About 1 crore people, 1 percent ride on a weekday, a quarter of those trips in the evening window: about 8,300 requests an hour. A busy driver fits 2.4 trips an hour, and about 30 percent of online drivers have no rider at a given moment, so each online driver completes about 1.68. That is about 4,960 drivers, and 15 percent more for the busiest half hour gives about 5,700, between about 2,900 and 8,600; the share of people who ride sets the range. As a check, the case's own zones had 0.47 online driver-hours behind each request before the launch, against my 0.60, so I am on the generous side. The published count for the city is to be found." |

**Three follow-ups, with the line a hire-grade answer gives.**

1. "Your idle share is a guess. Which number in the case data would catch it?" "The share of online hours with no completed trip: 0.22 before the launch and 0.38 after, so my 0.30 sits between them."
2. "The window is three hours. What does a four-hour window do?" "The evening's 25,000 trips spread over four hours, about 6,250 an hour, so about 4,300 drivers, unless the fourth hour brings trips of its own."
3. "Give a range, and say which factor drives it." "About 2,900 to 8,600. The share of people who ride drives it, and it is the first number I would replace with Uber's own peak requests."

---

## How does the same presentation sound at an AI company?

**The question, as the interviewer says it.** "You are the analyst at a coding-assistant company. The
sales deck quotes acceptance rate, the share of suggestions developers accept, at 32 percent (a figure
invented for this question). You want the team to optimise something else. Present the change to the
head of product in two minutes; they will push back."

**The clarifying questions a strong candidate asks.** What does the team get paid or ranked on today?
Is acceptance counted when a suggestion is later deleted? Which customers see the deck?

**The structure.** The claim; the proposed north star with its denominator and window; the guardrails;
the true part of the objection, conceded; the transition plan.

**The trap the interviewer fishes for.** Dropping acceptance rate outright, which ignores that
customers see it, or keeping it as the north star, which rewards accepted-then-deleted text.

| A weak answer | A hire-grade answer |
|---|---|
| "Acceptance rate is a vanity metric, so we should stop reporting it and survey developers about whether they like the tool." | "Acceptance counts a suggestion as a win even when the developer deletes it before committing, so it can rise while the product helps less. I propose the north star be suggested text still present at the next commit, per active developer-week, with build failures and revert rate as guardrails. You are right that customers see acceptance rate in the deck, so it stays there and on our dashboard as a leading input. We report both for a quarter, and the team is paid on the text that survives." |

**Three follow-ups, with the line a hire-grade answer gives.**

1. "What if retained text falls when we ship a faster model?" "Then the guardrails tell us whether it fell because suggestions got worse or because developers write more themselves, and I would look at revert rate first."
2. "Isn't 'present at the next commit' easy to game too?" "It can be padded with long suggestions, which is why revert rate and build failures sit beside it."
3. "Sales wants one number. Which do they get?" "Acceptance, with its definition printed, while the team's target is the retained text."
