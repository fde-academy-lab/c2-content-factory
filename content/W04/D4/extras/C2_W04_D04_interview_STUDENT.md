# How does a strong candidate answer "retention dropped; walk me through your investigation"?

Written for this programme in the style of product-company and GCC screens; the facts inside are
from the case file. The numbers are Thursday's Zomato Gold case in Chennai. Illustrative case: the
company is real, the situation and the data are synthetic, built for this class.

**Who needs the answer.** You, before any analytics, product or AI-startup screen that asks about
retention, churn or a funnel. The interviewer is deciding whether you check the number before you
explain it.

**The questions on the way.**

- What does the interviewer say?
- Which clarifying questions come first?
- What structure carries the answer?
- Which trap is being fished for?
- How do a weak and a hire-grade answer compare?
- What follows up, and which line answers each?
- How does the same question come up at an AI company?
- Which pain points hide inside the question?
- What does the scorer listen for?

## What does the interviewer say?

> "Our membership's retention dropped this quarter. Walk me through how you'd investigate it."

## Which clarifying questions does a strong candidate ask first?

1. "Which retention: who is counted, from which month after joining, and active means what?" The
   answer decides whether a new cohort is inside the number at all.
2. "Dropped against what: last month, last year, or a target?" The answer decides the comparison and
   the window.
3. "Did anything ship, or change in how events are logged, in that window?" The answer decides
   whether the first check is the count itself.

## What structure carries the answer?

1. **The count.** Rule out a tracking change: a renamed event, a new app version, a broken pipeline.
2. **The definition.** Read what the number counts and over whom; recompute it directly.
3. **The segments.** Split by signup cohort, then platform, then date, so a mix change and a rate
   change come apart.
4. **Users or use.** Separate fewer active members from fewer orders by each active member.
5. **The step.** Read the order flow step over step, in one named unit, and find the step that
   changed, for whom and since when.
6. **The call.** What to fix first, its size with an assumption ranged, and what would change it.

This is the order Aced's analyst guide says interviewers listen for: data checked before behaviour
is blamed, segments before a root cause, fewer users kept apart from less use (Aced's 2026 analyst interview guide,
checked 12 October 2026).

## Which trap is the interviewer fishing for?

The candidate names a cause in the first sentence, "it's probably the new release" or "it's the sale
members", and then looks for data to support it. The other trap is accepting a flat or falling
blend at face value without asking who it counts.

## How do a weak answer and a hire-grade answer compare?

| | Weak answer | Hire-grade answer |
|---|---|---|
| First sentence | "It's probably the sale we ran in August; those members were never going to stay." | "Before a cause, I'd check the count, then what the number counts, then split it." |
| The number | Takes the dashboard's 38 as the members' behaviour | "Month-two retention counts members from their second month, so August's 13,000 are outside September's 38 percent. Counting everyone who joined before September, it reads 35.9." |
| The cohorts | "Newer members are worse." | "Every cohort falls with age, about 0.3 points a month after month two, and each starts lower: 58 percent in January's month one, 49 in July's, 31 in August's. Within August, organic members kept 49 and sale-week members 20." |
| Users or use | Not reached | "Android members who stayed active ordered less: 1.36 orders each in August, 1.20 in September, while iOS rose from 1.34 to 1.40. So it isn't only who stays." |
| The step | "Checkout conversion fell, so the release broke checkout." | "Starting checkout held at 80 percent; completing it once started fell from 72.5 to 55, for members on Android only, from the release week. iOS members, 57 to 56, and non-members on Android, 52 to 51, are the comparators, and the fall holds with the cut moved a week." |
| The close | "Retention dropped because of the sale." | "Two problems: one step on Android since 14 September, about 1,317 orders a week, fixed first; and the sale-week members, judged on their own curve before the next sale." |

## What follows up, and which line answers each?

| Follow-up | The hire-grade line |
|---|---|
| "Blended retention is flat while every cohort declines. How?" | "A blend is a size-weighted average of cohorts at different ages: each month a new cohort enters at about 38.5 percent, just above the older cohorts' slide, so the average holds while every cohort falls. Rebuilt from its cohorts, September's lands on 13,218 of 35,000, the direct count." |
| "The app team says the stage you blamed is fine. What do you bring?" | "The part they're right about first: starting checkout held at 80 on every platform. Then the next step, by membership, platform and week: completion fell from 72.5 to 55 for members on Android from the release week, and nobody else fell." |
| "Before trusting a company's published cohort chart, what do you ask?" | "Its denominator: per acquired user, per retained user, or the cohort total. Swiggy says it weaned away users with low expected value, and on a per-retained chart that lifts every later column with nobody's behaviour changing (Swiggy Q2 FY26 letter, checked 12 October 2026)." |

## How does the same question come up at an AI company?

> "We launched an AI writing assistant three weeks ago. Weekly active users hit a record in launch
> week and are still near it. Is the product sticking?"

The blend trap, restated for an AI product. Launch week brings the biggest cohort the app will ever
see, and many of its users came to try something new. A strong answer splits weekly actives by the
week each user signed up and reads every cohort at the same age. Judged at week four, the launch
cohort keeps 24 percent against 36 for a cohort that found the app on its own (invented numbers),
while the blended weekly count looks like recovery because new cohorts keep arriving and prop it.
The call: judge each cohort at the age where habit shows, week four or later, never the blended
count of active users; then ask what the strong cohort does in its first week that the launch cohort
did not. This variant is written for this programme and names no company's figures.

## Which pain points hide inside the question, each with a real case?

| Pain point | The case | The check |
|---|---|---|
| A blend that cannot tell fewer users from less use | Swiggy's monthly transacting users rose 27.4 percent while orders per user fell from 4.13 to 3.87 (Swiggy Q1 FY27 letter, checked 12 October 2026) | Cohorts, and orders per active user |
| A cohort chart with a moving denominator | Swiggy's Instamart cohorts are indexed to one cohort's first quarter, after weaning weak users away (Swiggy Q2 FY26 letter, checked 12 October 2026) | Ask per acquired, per retained or total |
| Before and after read as cause | Zomato says Gold members' order frequency rose about 60 percent after joining (Zomato letter of 19 May 2023, checked 12 October 2026) | Members choose to join when they expect to order more |
| Two units on one chart | The case: menu view to cart reads 34 percent per session and 61 per member | Name the unit on every chart |
| A universal "good retention" number | Amplitude's 7 percent on day seven is a vendor's top-quarter mark, method unpublished (Amplitude blog, checked 12 October 2026) | Define retention before comparing it |

## What does the scorer listen for?

When you practise in pairs, the asker scores each of these from 0 to 2: clarified the scope; named
the denominator and the window; checked the count before the cause; split mix from rate; found the
step with its comparators; tied it to a decision and its cost; gave the structure before the
number.
