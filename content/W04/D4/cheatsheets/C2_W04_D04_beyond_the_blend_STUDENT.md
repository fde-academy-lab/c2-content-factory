# Who is leaving, and at which step?

Zomato Gold, Chennai, Week 4 Thursday. Month-two retention, members two or more months past joining who ordered in the month, read flat at 38 percent from June to September 2026 while every cohort fell, and members' Android add-to-cart to order fell from 58 to 44 percent after the 14 September release. Illustrative case: the company is real, the situation and the data are synthetic, built for this class.

## Panel 1: What does the triangle say?

![The cohort triangle: each signup month's share who ordered, by months since joining](../whiteboards/C2_W04_D04_cohort_triangle_STUDENT.png)

| Read | What it shows | On the case |
|---|---|---|
| Across a row | How a cohort's members leave | Down to about 38.5 in month two, then 0.3 points a month |
| Down column one | How each cohort starts | 58 for January, 49 for July, 31 for August |
| The grid underneath | One row per member per month, 1 if she ordered (panel data) | 241,492 member-months, grouped by joining month and age |

**Crux:** Fix each member's joining month and count her age from it; compare cohorts at the same age, and read one calendar month across them only to look for a shock that hit everyone.

## Panel 2: What did twelve members say?

| Member | Joined | Jun | Jul | Aug | Sep |
|---|---|---|---|---|---|
| ZG20844 | May | 1 | 1 | 1 | 1 |
| ZG21052 | May | 1 | 1 | 0 | 0 |
| ZG22010 | May | 1 | 0 | 0 | 0 |
| ZG22634 | May | 0 | 0 | 0 | 0 |
| ZG25312 | Jun | joined | 1 | 1 | 1 |
| ZG27475 | Jun | joined | 1 | 0 | 0 |
| ZG28603 | Jun | joined | 0 | 0 | 0 |
| ZG38681 | Aug, sale | | | joined | 1 |
| ZG40539, ZG41000, ZG41529, ZG42328 | Aug, sale | | | joined | 0 each |

By age: May 3, 2, 1, 1 of 4; June 2, 1, 1 of 3; August 1 of 5. The dashboard's way, from month two: 2 of 7 in August and in September; everyone before September: 3 of 12.

**Crux:** Each group falls with age and each later group starts lower, while the dashboard's way stands still.

## Panel 3: What is a retention number made of?

| Number | Who it counts | Who ordered, September |
|---|---|---|
| Month-two retention | Members two or more months past joining | 13,218 of 35,000 |
| Everyone before the month | Members who joined before it | 17,248 of 48,000 |

`blend = sum of (cohort size x cohort rate) / sum of cohort sizes`

**Crux:** Rebuilt from its cohorts, a blend lands on the direct count; a plain mean of rates (36.9 against 35.9) misses.

## Panel 4: How does a funnel step read?

| Step, September, members | Per session | Per member |
|---|---|---|
| Search to menu view | 118 percent | 101 percent |
| Menu view to add-to-cart | 34 percent | 61 percent |
| Add-to-cart to checkout start | 80 percent | 91 percent |

`step rate = reached this step / reached the step before, in one named unit`

**Crux:** A rate above 100 is a step people can skip (the carousel); among sessions that searched, 89 percent opened a menu.

## Panel 5: Which cause is checked first?

```mermaid
flowchart LR
    A["<b>1 Tracking</b>"] --> B["<b>2 Definition</b>"] --> C["<b>3 Cohorts</b>"] --> D["<b>4 Everyone</b>"] --> E["<b>5 A stage</b>"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    class A,B,C,D,E known
```

Did the count change; what does the number count; are newer members weaker; did everyone change at once; which step moved?

**Crux:** Rule out the count and the rule before blaming members, and find the step that moved before blaming the step that is low.

## Panel 6: What is fixed first, and what does the interviewer hear?

| Line | On the case |
|---|---|
| The step | Checkout start to order, 72.5 to 55 percent, Android members, from 14 September |
| The comparators | On the same step: iOS members 71 to 70, non-members on Android 65 to 64 |
| The size | About 1,223 to 1,317 orders a week; Rs 3.7 to 6.6 lakh of order value |

"Before a cause, I check the count and what it counts; then cohorts at one age, platform and date; then the step that changed."

**Crux:** The checkout first, since it loses orders every week; then whether the sale-week members (20 against 49 organic) pay back their discount.
