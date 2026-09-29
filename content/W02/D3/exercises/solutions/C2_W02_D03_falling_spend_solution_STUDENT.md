# Solution: whose spend is falling, and is the quarter on plan?

Answers: 1a 2b 3c 4d 5c 6b 7a

## The idea being tested

LAG reads the previous row, so the partition must be the member and the previous row must be the
previous calendar month; a running total is only as true as its order and its start, and it is
read against the plan to date, never against one week's plan. Every figure below comes from the
warehouse (v4), checked 29 Sep 2026: 118 members ordered in September, the flag without a
partition holds 20, with the partition 16, and with the months checked 9.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | a | Without PARTITION BY the previous row is whatever sorts before, so a member's first months are compared with the last months of the member above; 4 of the 20 flags compared a month with another member's month. | b describes the next defect, which exists with or without the partition. c still runs across members, so it compares a month with someone else's. d gets the order of work wrong, since the window is computed before the outer filter. |
| 2 | b | The previous row of his June is his April, because he has no May row, so LAG returns Rs 1,710 and calls a month two back "last month". | a is false, since LAG returns NULL only when there is no earlier row at all. c describes a zero-filled table, which this one is not. d describes LEAD, which reads the next row. |
| 3 | c | His September row's previous row is July and the one before is May, so the flag read two gaps as two falls; requiring the previous rows to be August and July removes him, because a month without an order is no reading. | a treats orders as months, which is the defect itself. b turns every holiday into a fall to zero and flags more members who were away. d throws away real falls for any member who once skipped a month. |
| 4 | d | Sixteen flags less the seven that span a skipped month leaves nine members whose spend fell in consecutive months. | a keeps the members the check exists to remove. b has the direction wrong, since a stricter check can only shrink the list. c counts only the members the fix removed. |
| 5 | c | With only order_date in the order, rows of the same date are peers and the default window includes every peer, so all twelve show the day's closing figure; adding order_id gives each row its own step, from Rs 3,45,16,000 up to Rs 3,76,90,290. | a invents a duplication, and the twelve order ids differ. b restarts the total every day, which destroys the running total Meera asked for. d is false, since Postgres never rounds a sum to a day. |
| 6 | b | Booked to date is cumulative, so it has to sit beside the plan to date, Rs 5,29,84,610 by week seven, which puts Q2 ahead by Rs 1,57,51,980. | a compares a cumulative figure with a single week. c reads the weekly plan as a floor for every week, which the plan line never said. d is false, since a running total that runs ahead of plan is exactly what the numbers show. |
| 7 | a | The monthly table has to exist before LAG can read it, LAG has to run inside each member's months, the months have to be checked before a comparison is trusted, and only then is the fall tested. | b and d run LAG over the whole table, the Q1 defect. c tests the fall before LAG exists to supply the earlier months. |

## The part worth arguing about

Item 3, option b. Filling a missing month with zero looks tidy, because every member then has a
row for every month. It changes the question from "did the member spend less" to "did the member
buy at all", and it flags every member who took a holiday. A month without an order is no reading,
so it breaks the run.

## Where the pattern lives in production

Churn flags, month-on-month growth by account and "two quarters of decline" alerts all use LAG, and
the two defects above are the ones that reach dashboards: the missing partition, which shows up as a
first month with a previous value, and the skipped month, which shows up as a customer on the phone
saying he was away. Running totals on dashboards fail the same way, by an ambiguous order or by
setting a cumulative line beside a weekly target.
