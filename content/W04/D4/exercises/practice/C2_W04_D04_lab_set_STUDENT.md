# Can you run the cohort and funnel method on a business you have never seen?

The practice set for the TA-led lab, after the Kalpa lab notebook. It moves the day's method to Dabba
Club, an invented tiffin subscription in Pune, so the counts are small enough to do by hand. Every
number on this page is invented for practice. The items climb from a hand count to the call a
product lead would pay for.

**Who needs the answer.** You, before tomorrow: the cohort row, the skippable step and the split that
settles a dispute return on Saturday's paper and in every retention question an interviewer asks.

**The questions on the way.**

- What does the January cohort keep at each month since joining?
- Which cohort is strongest, read at the same age?
- Which step of a funnel only looks like a win?
- In what order do the lines of the cohort table run?
- Which two charts settle a product lead's objection?
- What is the honest headline when a blend holds?

Three terms, defined once. A **cohort** is the subscribers who joined in the same calendar month.
**Month one** is the first full calendar month after joining; the joining month is month zero and is
never counted. A subscriber is **active** in a month when she took at least one tiffin in it.

Dabba Club's twenty subscribers, January to April. A 1 means she took at least one tiffin that month.

| Subscriber | Joined | Feb | Mar | Apr |
|---|---|---|---|---|
| D01 | Jan | 1 | 1 | 1 |
| D02 | Jan | 1 | 1 | 1 |
| D03 | Jan | 1 | 1 | 1 |
| D04 | Jan | 1 | 1 | 0 |
| D05 | Jan | 1 | 0 | 0 |
| D06 | Jan | 1 | 0 | 0 |
| D07 | Jan | 0 | 0 | 0 |
| D08 | Jan | 0 | 0 | 0 |
| D09 | Feb | joined | 1 | 1 |
| D10 | Feb | joined | 1 | 1 |
| D11 | Feb | joined | 1 | 1 |
| D12 | Feb | joined | 1 | 0 |
| D13 | Feb | joined | 0 | 0 |
| D14 | Feb | joined | 0 | 0 |
| D15 | Mar | | joined | 1 |
| D16 | Mar | | joined | 1 |
| D17 | Mar | | joined | 1 |
| D18 | Mar | | joined | 0 |
| D19 | Mar | | joined | 0 |
| D20 | Mar | | joined | 0 |

**What you post.** Six letters in item order, with no spaces, in this shape:

```
Post exactly this shape: xxxxxx
```

---

## What do the cohorts keep, read by age?

This comes up at work in every first pass over a subscription business: one row per joining month,
counted by hand before any code.

### Q1. Which line gives the January cohort's share at months one, two and three?

*Level L1 · asked in every analytics screen.*

a) 75, 67 and 75 percent
b) 100, 67 and 50 percent
c) 75, 50 and 37.5 percent
d) 25, 50 and 62.5 percent

### Q2. Which ranking of the three cohorts, strongest first, is fair?

*Level L2, a design call · asked in product-company screens.*

a) January, February, March: 75, 67 and 50 percent in each one's month one
b) February and March tie first at 50 percent in April, and January is last at 37.5
c) January first, since its eight subscribers make it the largest of the three
d) None yet, since the three cannot be ranked until March reaches its month two

---

## Which step only looks like a win, and in what order does the code run?

This comes up at work when a funnel and a cohort table are rebuilt in code: the reading has to
survive a step people can skip, and the lines have to run in an order that keeps month zero out.

Dabba Club's app, one week, counted in sessions: 2,000 opened the menu, 2,400 viewed this week's
specials, 600 added a plan and 480 paid. A push notification opens the specials page without the menu.

### Q3. Which step is the artefact, and why?

*Level L3 · asked in every analytics screen.*

a) Specials to plan, 25 percent, since the lowest step is where the loss sits
b) Menu to specials, 120 percent: the notification skips the menu
c) Plan to payment, 80 percent, since some payments fail the first time
d) Menu to specials, 120 percent, since a session views several specials

### Q4. In what order do these four lines build the cohort table from month one on?

*Level L2, a design call · asked in coding rounds for analyst roles.* The table `subs` holds one row
per subscriber per month from her joining month to April, with `cohort`, `month` and `tiffins`, and
`to_n` turns a year-and-month string into a count of months.

```text
1  tri = subs.pivot_table(index="cohort", columns="age", values="active", aggfunc="mean")
2  subs = subs[subs["age"] >= 1]
3  subs["age"] = to_n(subs["month"]) - to_n(subs["cohort"])
4  subs["active"] = subs["tiffins"] > 0
```

Which order runs, and keeps month zero out of the table?

a) 3, 4, 2, 1
b) 3, 4, 1, 2
c) 2, 3, 4, 1
d) 4, 1, 3, 2

---

## What settles a dispute, and what does a flat blend hide?

This comes up at work in the meeting after the table: the owning team says its step is fine, or the
headline number has not moved.

### Q5. Dabba Club's product lead writes: "Payment works. Of plans added, 80 percent were paid in March and 80 percent in April, so your fall is somewhere else." The room found renewals falling since an app update on 6 April. Which two charts settle it?

*Level L5, a design call · asked in GCC analytics screens.*

a) The overall payment rate by month, drawn larger, with a trend line added
b) A competitor's payment completion rate, to show what a good one looks like
c) App sessions in March and April, to show that the traffic held steady
d) Payment split by renewal and platform, then by week with the update marked

### Q6. Cohort A, 400 subscribers, kept 60 percent in May and 55 in June; cohort B, 600, kept 45 and then 40; cohort C, 1,000 new in June, kept 56. Blended retention read 51 percent in both months. What is the honest headline?

*Level L5, a design call · asked in product-company screens.*

a) Retention held at 51 percent, so the plan needs no change this quarter
b) Both older cohorts fell five points, and a big new cohort held the blend at 51
c) Retention improved, since the newest cohort retains the best of all three cohorts
d) The data is wrong, since a blend cannot hold while every cohort falls
