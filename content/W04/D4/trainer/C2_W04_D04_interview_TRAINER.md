# Interview room: the scorecards, and the fallback's dispute transcript

**TRAINER ONLY.** The [S] transcript the room reads is `extras/C2_W04_D04_interview_STUDENT.md`; this
page scores it, and carries the [D] transcript the fallback block's last part runs (fallback deck,
S9). Written for this programme in the style of product-company and GCC screens; the facts inside are
from the case file. Zomato Gold, Chennai: illustrative case, the company is real, the situation and
the data are synthetic, built for this class.

## How do the [S] answers score?

The seven criteria, each 0 to 2: 0 absent, 1 named, 2 named with the day's number.

| Criterion | Weak | Hire-grade | What earned the hire-grade 2 |
|---|---|---|---|
| Clarified the scope | 0 | 2 | Asked who the retention number counts, against what it dropped, and what shipped in the window |
| Named the denominator and the window | 0 | 2 | Month-two retention counts members from their second month: 13,218 of 35,000 in September, the August cohort outside it |
| Checked the count before the cause | 0 | 2 | The renamed Android event and the cut moved a week, before any member was blamed |
| Split mix from rate | 1 | 2 | Cohorts read at the same age; August split into organic (49) and sale-week (20); orders per active Android member 1.36 to 1.20 |
| Found the step with its comparators | 0 | 2 | Completion after checkout start, 72.5 to 55, members on Android only; iOS members and non-members on Android held |
| Tied it to a decision and its cost | 1 | 2 | The Android checkout first, about 1,317 orders a week, Rs 5.3 lakh at an assumed Rs 400 an order |
| Gave the structure before the number | 0 | 2 | "Count, definition, segments, users or use, step, call" said before any number |
| Total, of 14 | 2 | 14 | |

**Where the weak answer scores its two points.** It names a real cohort effect (the sale members)
and a decision (stop running sales), each without the count, the definition or a comparator that
would have changed it.

**What a strong interviewer would still push on.** "Your 1,317 assumes every lost cart would have
become an order at the old rate. Isn't that an upper bound?" The hire-grade reply: "Yes, if some
lost carts were retried later. Orders per active Android member fell from 1.36 to 1.20 while iOS rose,
so most were not; I'd report 1,317 as the upper end and confirm with retried carts in the next week's
log."

**A second push.** "Why not just A/B test the old checkout against the new one?" The hire-grade
reply: "That's the cleanest proof of cause, and I'd propose it. The decision doesn't wait for it,
though: the step fell only where the release shipped, and the comparators held, which is enough to
roll back or fix while the test is set up." Causal testing itself is not taught today; name it and
move on.

## What does the [D] transcript say?

Used in the fallback block's last part (20 minutes): read in pairs, then scored. It is the row's
[D] anchor.

**The question as the interviewer says it.** "You told the membership lead the new Android checkout
is losing orders. The app team's lead says the stage you blamed is fine, and brings a chart: carts
that start checkout held at 80 percent on every platform, before and after the release. What
evidence do you bring to the meeting?"

**The clarifying questions a strong candidate asks.** "Is their chart per session or per member, and
over which dates?" "Did the release change anything after checkout starts, such as payment or a
member price?" "Has their team mapped the renamed event, and can I see the mapping?"

**The structure.** The four moves from Tuesday: restate, answer from the evidence, concede what is
true, say what would change your mind; then one chart and one next step.

**The trap the interviewer fishes for.** Winning the argument: calling the app team's chart wrong, or
retreating to "conversion fell" without the step inside it.

| | Weak answer | Hire-grade answer |
|---|---|---|
| Restate | "Your chart doesn't show the problem." | "You're saying starting checkout held on every platform, so the new flow works." |
| Answer | "Add-to-cart to order fell from 58 to 44 on Android." | "The step after it fell: completing the order once checkout started went from 72.5 to 55 percent, for members on Android, from the release week." |
| Concede | Nothing conceded. | "Your chart is right: starts held at 80 everywhere. And the sale members are weak, which is a separate problem with its own fix." |
| What would change it | Not said. | "If non-members on Android had fallen too, it would be everyone's step; if the renamed event is mapped differently from what I used, I'll rerun it on your mapping." |
| Next step | "Roll back the release." | "Let's look at what members see after checkout starts on Android, since only members fell; I'll bring the weekly chart for members by platform." |

**Three follow-ups and the line a hire-grade answer gives each.**

| Follow-up | The line |
|---|---|
| "How do you know it isn't the sale members ordering less?" | "Members on iOS joined in the same sale and held at 57 to 56; the fall sits on one platform from one date." |
| "Could it be a tracking change from the renamed event?" | "The fall holds with the cut moved a week either way, 58 to 47 and 56 to 43, and the orders table agrees: orders per active Android member fell from 1.36 to 1.20." |
| "The app team outranks you. Now what?" | "I restate their point, show the one weekly chart of completion for Android members, and ask for one engineer to check the member path after checkout starts." |

**The [D] scorecard.**

| Criterion | Weak | Hire-grade |
|---|---|---|
| Clarified the scope | 0 | 2 |
| Named the denominator and the window | 0 | 2 |
| Checked the count before the cause | 0 | 2 |
| Split mix from rate | 0 | 1 |
| Found the step with its comparators | 1 | 2 |
| Tied it to a decision and its cost | 1 | 1 |
| Gave the structure before the number | 0 | 2 |
| Total, of 14 | 2 | 12 |

The hire-grade [D] answer earns a 1 on mix because the dispute never needs the cohort split, and a 1
on cost because it names the next step and leaves the 1,317 orders a week unsaid, which a 2 would
say aloud.

## How is the AI-company variant run?

After the [S] transcript, five minutes: one pair reads the AI question aloud and answers it cold,
then the room compares the answer with the extras page. Explorer scene Th4 shows the same toy: the
launch cohort at 24 percent and the organic cohort at 36 at week four, with the blended count's
toggle. The move to listen for is "read each cohort at the same age", said before any number.
