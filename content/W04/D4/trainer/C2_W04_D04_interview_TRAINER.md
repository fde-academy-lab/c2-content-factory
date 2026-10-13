# Interview room: the scorecards, and the fallback's dispute transcript

**TRAINER ONLY.** The [S] transcript is `extras/C2_W04_D04_interview_STUDENT.md`, which learners read
in the evening; in SECTION 9's interview walk (S78 to S81) the pairs work from S79's table only. This page scores the transcript, and carries the [D] transcript the fallback block's last part runs (fallback deck,
S9). [S] marks a staple asked everywhere and [D] a differentiator, where a strong candidate separates.
Written for this programme in the style of product-company and GCC screens. Zomato Gold, Chennai:
illustrative case, the company is real, the situation and the data are synthetic, built for this
class.

## How do the [S] answers score?

The seven criteria, each 0 to 2: 0 not done, 1 done without a number, 2 asked for the right number
and then used it; the cost criterion asks for a range. A line counts only in the main answer, never
in a follow-up. The interviewer's replies in the transcript hand over every number the hire-grade
answer uses, so a 2 rewards asking and using, never reciting.

| Criterion | Weak | Hire-grade | The line in the transcript that earns it |
|---|---|---|---|
| Clarified the scope | 0 | 2 | Six clarifying questions: who is counted, whether a member who stops paying stays in, against what, how members were acquired, what shipped, and what an order is worth |
| Named the denominator and the window | 0 | 2 | "It is every member two or more months in ... Over everyone who joined before each month it reads 40.9, 40.0, 39.5, then 35.9" |
| Checked the count before the cause | 0 | 2 | "Retention comes from the order records, which the rename never touched, and they match the event log, 27,212 member orders in September. Starting checkout held at 80 percent" |
| Split mix from rate | 1 | 2 | Cohorts at the same age; August split 49 against 20; among members who joined before July, the share who ordered barely moved on either platform while orders per ordering member fell only on Android |
| Found the step with its comparators | 1 | 2 | Completion per session 72.5 to 55; on the same step iOS members 71 to 70 and non-members on Android 65 to 64; the member path; 18,273 starts |
| Tied it to a decision and its cost | 0 | 2 | 3.2 of the 3.6 points is August; the checkout costs 1,133 to 1,317 orders a week, Rs 3.4 to 6.6 lakh of order value; the member path first; what would change the order |
| Gave the structure before the number | 0 | 2 | The first sentence names the six moves before any number |
| Total, of 14 | 2 | 14 | |

**Where the weak answer scores its two points.** It names a cohort effect, the sale members, and a
step, checkout conversion, each without the number that would test it.

**What a strong interviewer would still push on.** "Your 1,317 assumes every lost cart would have
become an order at the old rate. Isn't that an upper bound?" The hire-grade reply: "It is. The share
of failed checkouts followed by an order within a day held near 36 percent, but failures nearly
doubled, from 1,921 to 3,386 a week, so more came back: 1,189 a week against 701. Counted in orders
placed, which keeps those, Android members' weekly orders fell 18 percent while iOS members' rose 7
and non-members' on Android 4: about 1,266 a week against iOS members and 1,133 against non-members.
So 1,133 to 1,317."

**A second push.** "Why not just A/B test the old checkout against the new one?" The hire-grade
reply: "I'd propose it as a cheap, reversible test: send half of Android members back to the old
checkout for two days. The decision does not wait for it: the step fell only for members on the new
flow, the comparators held on the same step, and each week costs over 1,100 orders." Causal testing
itself is not taught today; name it and move on.

## What does the [D] transcript say?

Used in the fallback block's last part (20 minutes): read in pairs, then scored. It is the row's
[D] anchor.

**The question as the interviewer says it.** "You told the membership lead the new Android checkout
is losing orders. The app team's lead says the stage you blamed is fine, and that the sale members
are the real problem. They bring a chart: carts that start checkout held at 80 percent on every
platform, before and after the release. What evidence do you bring to the meeting?"

**The clarifying questions, and what the interviewer answers.**

| The candidate asks | The interviewer answers |
|---|---|
| "Is their chart per session or per member, and over which dates?" | "Per session, 1 August to 30 September, with 14 September marked." |
| "Did the release change anything after checkout starts, such as payment or a member price?" | "The whole checkout flow is new on Android, payment included." |
| "Has their team mapped the renamed event, and do the order records agree with the event log?" | "Mapped; both count 27,212 member orders in September." |
| "Can I put up my own tables: completion of a started checkout by membership, platform and week with the starts behind each rate, the same for members who joined before August, and member orders a week by segment?" | "All three. They are yours, and they are on the shared screen." |

**The structure.** The four moves from Tuesday: restate, answer from the evidence, concede what is
true, say what would change your mind; then one chart and one next step. The hire-grade answer says
those moves in its first two sentences, before any number.

**The trap the interviewer fishes for.** Winning the argument: calling the app team's chart wrong, or
retreating to "conversion fell" without the step inside it.

| | Weak answer | Hire-grade answer |
|---|---|---|
| Restate | "Your chart doesn't show the problem." | "You're saying starting checkout held on every platform, so the new flow works, and the sale members explain the fall. I'll check the count, show the step after yours with its comparators, concede what you're right about, say what would change my mind, and put up one chart." |
| Answer | "Add-to-cart to order fell from 58 to 44 on Android." | "The count first: the order records, which the rename never touched, and the event log both say 27,212 member orders in September. Your chart is per session, and so is mine. The step after yours is part of the new flow, payment included, and it fell: from 1 August to 13 September against 14 to 30 September, completing a started checkout went from 72.5 to 55 percent for members on Android, on 18,273 starts after the release, while on that same step iOS members went 71 to 70 and non-members on Android 65 to 64." |
| The chart | Overall add-to-cart to order by week, every platform on one line. | "Weekly completion of a started checkout for Android members, iOS members and non-members on Android, with 14 September marked: the Android members' line drops from near 72.5 to near 55 in the release week, and the other two hold their level." |
| Concede | Nothing conceded. | "Your chart is right: starts held at 80 everywhere. And you're right about retention: the August cohort, mostly sale-week members, explains 3.2 of the 3.6-point fall. The checkout is about orders, and the sale members don't explain that: among members who joined before August, completion fell from 70.3 to 53.6 on Android and held at 68.6 to 69.3 on iOS." |
| What would change it | Not said. | "If the order records showed orders holding while the log fell, or if most failed checkouts came back as later orders, I'd withdraw it. Counted in orders placed, Android members' weekly orders fell 18 percent while iOS members' rose 7." |
| Next step | "Roll back the release." | "It costs 1,133 to 1,317 orders a week, so put members on Android back on the old checkout today, or half of them for two days if your team wants proof, and look in parallel at what only members see on the new page, such as the free-delivery line or the membership check." |

**Three follow-ups and the line a hire-grade answer gives each.**

| Follow-up | The line |
|---|---|
| "Why only members?" | "Non-members ran the same new checkout and held, so the fault is on the member path; the sale cohort is about 70 percent Android, like every cohort, so it cannot explain a fall on one platform." |
| "Could it be a tracking change from the renamed event?" | "A date test can't tell, since the rename shipped with the release. The order records can, since the app's event names don't feed them, and they count the same 27,212 orders in September as the log." |
| "The app team outranks you. Now what?" | "I'd ask for the cheapest reversible test, the old path for half of Android members for two days, with the weekly completion chart beside it." |

**The [D] scorecard.**

| Criterion | Weak | Hire-grade |
|---|---|---|
| Clarified the scope | 0 | 2 |
| Named the denominator and the window | 0 | 2 |
| Checked the count before the cause | 0 | 2 |
| Split mix from rate | 0 | 2 |
| Found the step with its comparators | 1 | 2 |
| Tied it to a decision and its cost | 1 | 2 |
| Gave the structure before the number | 0 | 2 |
| Total, of 14 | 2 | 14 |

The hire-grade [D] answer asks four questions and uses each reply; says its moves before any number
and leads with the count on the order records; names its unit, per session, and both windows; holds
the cohorts fixed to answer the sale members; puts its comparators on the same step; shows one chart;
gives the app team retention and keeps orders; and ties a reversible next step to the size with its
range, all in the main answer. The fourth question is what earns the 2s on mix, step and cost: the
candidate names the tables that carry those numbers before using them.

**Two facts for the room if a pair asks.** Sale-week members on iOS fell from 63 to 43 percent on
add-to-cart to order across the cut, because they aged from month zero into month one; that is why
all-iOS comparators mix cohorts and the held-fixed split is the clean test. Every cohort sits at
about 70 percent Android (70 to 71 percent across cohorts).

## How is the AI-company variant run?

In SECTION 9's interview walk it runs as S80, read aloud in 3 minutes with no discussion. When the fallback block or
the lab has time, one pair answers the AI question cold and the room compares the answer with the
extras page. Explorer scene Th4 shows the same toy: the
launch cohort at 24 percent and a later cohort at 36 at week four, with the blended count's toggle.
The premise is two months after launch, so week four exists for several cohorts. The moves to listen
for: active defined on the core action, the weekly model and pricing changes checked first, "read
each cohort at the same age" said before any number, a verdict from the curves' shape, and the cost
per retained user.
