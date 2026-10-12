# How does a strong candidate answer "retention dropped; walk me through your investigation"?

Written for this programme in the style of product-company and GCC screens, a GCC being a global
capability centre, a multinational's own technology and analytics centre in India. The numbers are
Thursday's Zomato Gold case in Chennai. Illustrative case: the company is real, the situation and the
data are synthetic, built for this class.

**Who needs the answer.** You, before any analytics, product or AI-startup screen that asks about
retention, churn or a funnel. The interviewer is deciding whether you check the number before you
explain it. A hire-grade answer is one that gets the candidate the job.

**The questions on the way.**

- What does the interviewer say?
- Which clarifying questions come first, and what does the interviewer answer?
- What structure carries the answer?
- Which trap is being fished for?
- How do a weak and a hire-grade answer compare?
- What follows up, and which line answers each?
- How does the same question come up at an AI company?
- Which pain points hide inside the question, and where has each shown up?
- What does the scorer listen for?

## What does the interviewer say?

> "Our membership's retention dropped this quarter. Walk me through how you'd investigate it."

## Which clarifying questions come first, and what does the interviewer answer?

A strong candidate asks before any cause, and the interviewer hands over what each question unlocks.
The candidate uses only what was handed over, and says which numbers are assumptions.

| The candidate asks | The interviewer answers |
|---|---|
| "Which retention: who is counted, from which month after joining, and what does active mean?" | "Month-two retention: of the members two or more months past their signup month, the share who ordered this month. It read 38 percent from June to September." |
| "Does retained mean ordered, or renewed, and does a member who stops paying leave the count?" | "Ordered that month. Every member who joined since January stays in the count; this table records no cancelled memberships." |
| "Dropped against what, and over which window?" | "Here is retention counted over everyone who joined before each month: 40.9, 40.0, 39.5 and 35.9 percent from June to September. And the cohort table." |
| "August's cohort is 13,000, about 2.6 times the usual 5,000. Did anything change in how members were acquired: a campaign, a discount, the price?" | "A sale week, 17 to 23 August, with a discounted first month. Here are members by signup channel." |
| "Did anything ship, or change in how events are logged, in that window?" | "A new Android checkout on 14 September, which renamed one Android event; the app team mapped the old name to the new. Here are the order flow by platform and week, and the order records." |
| "What is an order worth to us?" | "Assume Rs 400 of order value, anywhere from Rs 300 to Rs 500; Zomato keeps its commission and fees from that." |

## What structure carries the answer?

1. **Tracking.** Did the count change? Check the orders a second way, in a record the app's event
   names do not touch.
2. **Definition.** What does the number count, and over whom? Recompute it directly.
3. **Cohorts.** Read each signup month at the same age, so a weak group and a weak month come apart.
4. **Everyone.** Did every cohort move at once? Split by platform, date and zone, and keep fewer
   users apart from fewer orders by each user, with the cohorts held fixed.
5. **A stage.** Read the order flow step over step, in one named unit, and find the step that
   changed, for whom and since when, with comparators on the same step.
6. **The call.** What to fix first, its size with every assumption ranged, and what would change it.

Before narrowing, name what sits outside the app and the split that tells each apart. Delivery
times and restaurant supply move every platform and members and non-members alike; a competitor's
offer or a festival week moves the city; a change to Gold's price or benefits moves members only;
a delivery-fee change mostly moves non-members, since Gold members get free delivery. The member
and platform splits separate them.

Aced's guide to analyst interviews makes the same moves on its own sample, a 10 percent drop in a
social app's daily post views: define the metric, rule out a data issue first, segment before a root
cause, and, in its commentary, keep fewer users apart from fewer views each. The page is undated:
https://www.aced.io/blog/top-data-analyst-interview-questions (checked 12 October 2026)

## Which trap is the interviewer fishing for?

The candidate names a cause in the first sentence, "it's probably the new release" or "it's the sale
members", and then looks for data to support it. The other trap is accepting a flat or falling
blend at face value without asking who it counts.

## How do a weak answer and a hire-grade answer compare?

| | Weak answer | Hire-grade answer |
|---|---|---|
| First sentence | "It's probably the sale we ran in August; those members were never going to stay." | "Before a cause, I'll check the count, then what the number counts, then cohorts, then whether everyone moved, then the step, and then make a call." |
| The count | Not checked | "Retention comes from the order records, which the rename never touched, and they match the event log, 27,212 orders in September. Starting checkout held at 80 percent, so the starts were counted too." |
| The number | Takes the dashboard's 38 as the members' behaviour | "The label misleads: it is every member two or more months in, a blend of seven cohorts, so August's 13,000 are outside it. Over everyone who joined before each month it reads 40.9, 40.0, 39.5, then 35.9: that is the drop, and the dashboard misses it because it starts at month two." |
| The cohorts | "Newer members are worse." | "The members who stay past month one are steady: every cohort lands near 38.5 in month two and slides about 0.3 points a month. What fell is month one, 58 percent for January down to 49 for July, which the dashboard leaves out by design, and August at 31. Within August, organic members kept 49 and sale-week members 20." |
| Users or use | Not reached | "Held to members who joined before August, the share who ordered fell alike on both platforms, 39.5 to 37.6 on Android and 39.8 to 38.0 on iOS, while orders per ordering member fell only on Android, 1.45 to 1.24, with iOS at 1.44 and 1.45." |
| The step | "Checkout conversion fell, so the release broke checkout." | "Completing a started checkout fell from 72.5 to 55 for Android members from the release week, while on that same step iOS members went 71 to 70 and non-members on Android 65 to 64. Non-members ran the same new checkout and held, so the break is in what only members see, such as the free-delivery line or the membership check at payment. Every Android session moved to the new version that day, so date and version are one split. The 55 rests on 18,273 checkout starts, so chance moves it by under a point." |
| The close | "Retention dropped because of the sale." | "Of the 3.6-point fall from August to September, about 3.2 is the August cohort, 13,000 members at 31, mostly sale-week members at 20; a normal August would have cost about 0.4. Retention can't see the checkout, since a member it cost an order still ordered once, but it loses 1,133 to 1,317 orders a week, a quarter of Android members' orders, Rs 3.4 to 6.6 lakh of order value. Fix the member path of the checkout first, because a fix ends a weekly loss; then ask whether the sale paid back. If August loses July's 10.5 points into month two, October's dashboard reads about 33, 32 to 34. What would change the order: if most failed checkouts came back as later orders, the checkout would cost a delay and the sale would go first." |

## What follows up, and which line answers each?

| Follow-up | The hire-grade line |
|---|---|
| "Blended retention is flat while every cohort declines. How?" | "Each month one more cohort reaches month two and enters the count at about 38.5, a little above the older cohorts' slide, so the blend holds; that prop is worth well under a point. The question that matters is what the count leaves out: month one, which fell cohort after cohort, and August's 13,000 at 31. Rebuilt from its cohorts, September's lands on 13,218 of 35,000, which proves the rebuild, not the cause." |
| "The app team says the stage you blamed is fine. What do you bring?" | "The part they're right about first: starting checkout held at 80 on every platform. Then the next step, on the same rate for everyone: completion fell from 72.5 to 55 for Android members while iOS members went 71 to 70 and non-members on Android 65 to 64, from the release week." |
| "Was the sale a mistake?" | "Not yet known. A sale-week member placed 0.23 orders in month one against 0.61 for an organic member. The organic August members, 4,973, and September's 5,089 sit near the usual 5,000, so the 8,027 sale-week members look like extra members rather than members pulled forward. I'd set what each contributes over six months against the discount she was given before anyone runs another sale." |
| "Before trusting a company's published cohort chart, what do you ask?" | "Its denominator and its measure: users, orders or spend; per user who joined or per user who stayed. Swiggy says it weaned away Instamart users with 'low potential Lifetime values', and its cohort spend table states no denominator. If those cells are spend per user who stayed, letting users go lifts that quarter's cells and every later one with nobody's behaviour changing; and Instamart's average order value grew about 40 percent in the same year." |

The Swiggy line is from its Q2 FY26 shareholder letter:
https://www.swiggy.com/corporate/wp-content/uploads/2025/10/Q2-FY2026-Shareholder-letter.pdf (checked 12 October 2026)

## How does the same question come up at an AI company?

> "We launched an AI writing assistant two months ago. Weekly active users hit a record in launch week
> and are still near it. Is the product sticking?"

The blend trap, restated for an AI product. Launch week brings the biggest cohort the app will ever
see, and many of its users came to try something new. A strong answer first defines active as the
core action, a draft the user keeps, since a login says little about an AI tool. Then the count:
model, prompt and pricing changes ship weekly and move every cohort in one calendar week, so they are
checked first, as the release was in Chennai. It splits weekly actives by signup week and draws each
cohort's kept-draft curve by weeks since signup. Two months in, the launch cohort and the next few
weekly cohorts have all reached week four: the launch cohort keeps 24 percent against 36 for a later
weekly cohort (invented numbers), while the blended weekly count stays near the record because each
new week's cohort adds to it. The verdict turns on the curves' shape: if the later cohorts flatten
by week six while the launch cohort keeps sliding, the product sticks for the users who came looking
for it, and the launch week's crowd was trying it out. Beside each cohort sit the share of drafts
kept and the cost per retained user, since every active user costs inference. Week four is the
programme's rule of thumb, not a published law; the blended count still sizes load and spend. This
variant is written for this programme and names no company's figures.

## Which pain points hide inside the question, and where has each shown up?

| Pain point | Where it showed up | The check |
|---|---|---|
| More users, less use each: the mix or the habit? | Swiggy's platform-wide users who order in a month rose 27.4 percent year on year while platform frequency, completed orders per user in a month, fell from 4.13 to 3.87 (Q1 FY27 letter, checked 12 October 2026) | Cohorts, and orders per active user with the cohorts held fixed |
| A cohort chart with no stated denominator | Swiggy's Instamart spend by cohort, after weaning users away (Q2 FY26 letter, checked 12 October 2026) | Ask per user who joined, per user who stayed, or total |
| Before and after read as cause | Zomato says Gold members' order frequency rose about 60 percent after joining (letter of 19 May 2023, checked 12 October 2026) | Members choose to join when they expect to order more |
| Two units on one chart | This case, synthetic: menu view to add-to-cart reads 34 percent per session and 61 per member | Name the unit on every chart |
| A universal "good retention" number | Amplitude, a product-analytics vendor, says 7 percent of a cohort back on day seven puts a product in the top 25 percent for activation, from more than 2,600 companies, and its blog gives no method (checked 12 October 2026) | Define retention before comparing it |

The sources, in the order of the table:

- Swiggy, Q1 FY27 shareholder letter:
  https://nsearchives.nseindia.com/corporate/SWIGGY_30072026154100_Covering_Letter_Letter_to_Shareholders_-_signed.pdf (checked 12 October 2026)
- Zomato, shareholder letter of 19 May 2023:
  https://www.bseindia.com/xml-data/corpfiling/AttachHis/42b3bf3b-1edb-4da7-849a-87ca9da27ff8.pdf (checked 12 October 2026)
- Amplitude, the 7 percent retention rule:
  https://www.amplitude.com/blog/7-percent-retention-rule (checked 12 October 2026)

## What does the scorer listen for?

When you practise in pairs, the asker scores each of these from 0 to 2: 0 not done, 1 done without a
number, 2 asked for the right number and then used it. Clarified the scope; named the denominator
and the window; checked the count before the cause; split mix from rate, the mix being each cohort's
share of the count; found the step with its comparators on the same step; tied it to a decision and
its cost, with a range; gave the structure before the number.
