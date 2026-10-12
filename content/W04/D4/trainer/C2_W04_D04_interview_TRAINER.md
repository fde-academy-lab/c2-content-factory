# Interview room: the scorecards, and the fallback's dispute transcript

**TRAINER ONLY.** The [S] transcript the room reads is `extras/C2_W04_D04_interview_STUDENT.md`; this
page scores it, and carries the [D] transcript the fallback block's last part runs (fallback deck,
S9). [S] marks a staple asked everywhere and [D] a differentiator, where a strong candidate separates.
Written for this programme in the style of product-company and GCC screens. Zomato Gold, Chennai:
illustrative case, the company is real, the situation and the data are synthetic, built for this
class.

## How do the [S] answers score?

The seven criteria, each 0 to 2: 0 not done, 1 done without a number, 2 asked for the right number
and then used it. The interviewer's replies in the transcript hand over every number the hire-grade
answer uses, so a 2 rewards asking and using, never reciting.

| Criterion | Weak | Hire-grade | The line in the transcript that earns it |
|---|---|---|---|
| Clarified the scope | 0 | 2 | The four clarifying questions: who is counted, ordered or renewed, against what, and what shipped |
| Named the denominator and the window | 0 | 2 | "It is every member two or more months in ... Over everyone who joined before each month it reads 40.9, 40.0, 39.5, then 35.9" |
| Checked the count before the cause | 0 | 2 | "A date test can't separate logging from behaviour. The order records match the event log, 27,212 orders in September" |
| Split mix from rate | 1 | 2 | Cohorts at the same age; August split 49 against 20; orders per ordering member with the cohorts held fixed, 1.45 to 1.24 on Android |
| Found the step with its comparators | 0 | 2 | Completion 72.5 to 55; on the same step iOS members 71 to 70 and non-members on Android 65 to 64; 18,273 starts |
| Tied it to a decision and its cost | 1 | 2 | The checkout first, 1,223 to 1,317 orders a week, a quarter of Android members' orders, Rs 3.7 to 6.6 lakh of order value; payback before another sale |
| Gave the structure before the number | 0 | 2 | The first sentence names the six moves before any number |
| Total, of 14 | 2 | 14 | |

**Where the weak answer scores its two points.** It names a real cohort effect (the sale members)
and a decision (stop running sales), each without the count, the definition or a comparator that
would have changed it.

**What a strong interviewer would still push on.** "Your 1,317 assumes every lost cart would have
become an order at the old rate. Isn't that an upper bound?" The hire-grade reply: "It is the top of
the range. Two things bring it down or hold it: the comparators lost a point on their own, which
takes it to about 1,223; and retries did not rise, since after a checkout with no order the member
ordered within a day 36.5 percent of the time before the release and 35.1 after. So 1,223 to 1,317,
and the loss did not come back as later orders."

**A second push.** "Why not just A/B test the old checkout against the new one?" The hire-grade
reply: "I'd propose it as a cheap, reversible test: send half of Android members back to the old
checkout for two days. The decision does not wait for it: the step fell only where the release
shipped, the comparators held on the same step, and each week costs about 1,300 orders." Causal
testing itself is not taught today; name it and move on.

## What does the [D] transcript say?

Used in the fallback block's last part (20 minutes): read in pairs, then scored. It is the row's
[D] anchor.

**The question as the interviewer says it.** "You told the membership lead the new Android checkout
is losing orders. The app team's lead says the stage you blamed is fine, and that the sale members
are the real problem. They bring a chart: carts that start checkout held at 80 percent on every
platform, before and after the release. What evidence do you bring to the meeting?"

**The clarifying questions a strong candidate asks.** "Is their chart per session or per member, and
over which dates?" "Did the release change anything after checkout starts, such as payment or a
member price?" "Has their team mapped the renamed event, and can I see the mapping?"

**The structure.** The four moves from Tuesday: restate, answer from the evidence, concede what is
true, say what would change your mind; then one chart and one next step.

**The trap the interviewer fishes for.** Winning the argument: calling the app team's chart wrong, or
retreating to "conversion fell" without the step inside it.

| | Weak answer | Hire-grade answer |
|---|---|---|
| Restate | "Your chart doesn't show the problem." | "You're saying starting checkout held on every platform, so the new flow works, and the sale members explain the fall." |
| Answer | "Add-to-cart to order fell from 58 to 44 on Android." | "The step after yours fell: per session, completing the order once checkout started went from 72.5 to 55 percent for members on Android from the release week, while on that same step iOS members went 71 to 70 and non-members on Android 65 to 64." |
| Concede | Nothing conceded. | "Your chart is right: starts held at 80 everywhere. And the sale members are weak, which is a separate problem with its own fix." |
| What would change it | Not said. | "If the order records showed orders holding while the event log fell, the fall would be in the counting; if members who failed came back and ordered later, it would be a delay. Neither holds: the records match the log, and retries within a day did not rise." |
| Next step | "Roll back the release." | "Let's check what members see after checkout starts on Android, for example whether the free-delivery line or a membership check is recomputed at payment; I'll bring the weekly chart for members by platform." |

**Three follow-ups and the line a hire-grade answer gives each.**

| Follow-up | The line |
|---|---|
| "How do you know it isn't the sale members ordering less?" | "Hold the cohorts fixed: among members who joined before August, completion fell from 70.3 to 53.6 on Android and held at 68.6 to 69.3 on iOS. The sale cohort is about 70 percent Android, like every cohort, so it cannot explain a fall on one platform." |
| "Could it be a tracking change from the renamed event?" | "A date test can't tell: the rename shipped with the release. The order records can, since the app's event names don't feed them, and they count the same 27,212 orders in September as the event log." |
| "The app team outranks you. Now what?" | "It costs about 1,300 orders a week, so I'd ask for the cheapest reversible test: the old checkout back for half of Android members for two days, with the weekly completion chart beside it." |

**The [D] scorecard.**

| Criterion | Weak | Hire-grade |
|---|---|---|
| Clarified the scope | 0 | 2 |
| Named the denominator and the window | 0 | 2 |
| Checked the count before the cause | 0 | 2 |
| Split mix from rate | 0 | 2 |
| Found the step with its comparators | 1 | 2 |
| Tied it to a decision and its cost | 1 | 1 |
| Gave the structure before the number | 0 | 2 |
| Total, of 14 | 2 | 13 |

The hire-grade [D] answer names its unit (per session) and window (from the release week), checks the
count on the order records, holds the cohorts fixed in its first follow-up, and puts its comparators
on the same step. It earns a 1 on cost because the size, about 1,300 orders a week, appears only in a
follow-up; a 2 would say it in the main answer.

**Two facts for the room if a pair asks.** Sale-week members on iOS fell from 63 to 43 percent on
add-to-cart to order across the cut, because they aged from month zero into month one; that is why
all-iOS comparators mix cohorts and the held-fixed split is the clean test. Every cohort sits at
about 70 percent Android (70 to 71 percent across cohorts).

## How is the AI-company variant run?

After the [S] transcript, five minutes: one pair reads the AI question aloud and answers it cold,
then the room compares the answer with the extras page. Explorer scene Th4 shows the same toy: the
launch cohort at 24 percent and the organic cohort at 36 at week four, with the blended count's
toggle. The premise is two months after launch, so week four exists for several cohorts. The moves
to listen for: active defined on the core action, "read each cohort at the same age" said before any
number, and the cost per retained user.
