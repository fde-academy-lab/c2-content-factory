# Solution: who goes on the protect list?

Answers: 1b 2d 3a 4c 5b 6d 7c

## The idea being tested

GROUP BY answers how much per group, and a window keeps every row and says where each row stands.
Marketing's ask is a question about each member's position inside a segment, so the list needs a
window partitioned by segment, and the list is only done when it has been counted by segment and
the count matches the question. The numbers below come from the warehouse (v4), checked
29 Sep 2026, with Q2 revenue per member taken as the booked amount of the member's Q2 orders.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | b | The board pack wants one row per segment, and GROUP BY collapses the 227 member rows into four, one per segment, carrying the sum and the count. | a returns the right total repeated 227 times, which is a window doing a GROUP BY's job. c answers who leads each segment, which nobody asked. d accumulates across segments, which has no meaning for a board line. |
| 2 | d | The row needs two levels at once, the member's figure and the segment's, and only a window keeps the member row while adding the segment total to it. | a gives the member's figure with no segment total. b collapses the members away, so no member row survives. c filters groups and never places two levels on one row. |
| 3 | a | Without a partition the ranking runs across the whole table, so one large Business order outranks a year of a retail member, and Retail-Plus, the segment Marketing worries about, gets 11 members instead of 50. | b defends the wrong question, because Marketing asked for fifty per segment. c is false, since the Student segment has 20 Q2 buyers who were simply outranked. d still ranks the whole table, so 200 rows would carry even more Business and Retail-Plus members and still no fair fifty per segment. |
| 4 | c | Retail-Plus and Retail-Core have more than fifty buyers and ship 50 each, while Business ships its 35 and Student its 20, so the list carries 35 plus 50 plus 50 plus 20, which is 155 rows. | a assumes every segment has fifty buyers. b forgets that the filter still removes the Retail rows below fiftieth. d treats the filter as a limit on the whole result, and the position restarts in every segment. |
| 5 | b | A segment with 35 buyers has no fifty to choose from, so its top fifty is everyone who bought, and the list should say so in words to stop a reader hunting for fifteen missing members. | a invents members who never bought in Q2. c changes Marketing's rule without asking Marketing. d removes the most valuable members from a list meant to protect them. |
| 6 | d | On a table of member totals each customer_id is a partition of one row, so every member ranks 1 and the filter at fifty keeps all 227; the partition has to be the group the ranking restarts in, which is the segment. | a misreads the order of work, since the filter runs outside the CTE after the rank. b changes the tie rule and leaves every member still ranked 1. c ranks the smallest spenders first and keeps the same one-row partitions. |
| 7 | c | The member total has to exist before it can be ranked, the rank has to exist before it can be filtered, and the count by segment is the check that proves the list answers the ask. | a ranks single orders, which ranks the biggest order rather than the biggest member. b throws away every small order before the members are totalled, so a frequent small buyer vanishes. d cuts to fifty members across the whole table before ranking, which is the Q3 list again. |

## The part worth arguing about

Item 5. Some pairs will say a list of 35 is a failed list, because the ask said fifty. It is the
right list, and the defect would be a report that ships 35 rows without saying why. The sentence
that goes with it is short: the Business and Student lines are every Q2 buyer in those segments.

## Where the pattern lives in production

Every "top N per something" report in a GCC dashboard is this query: top products per category,
top agents per region, top accounts per manager. The ones that ship wrong almost always rank the
whole table and filter at N, and the check that catches them takes one line, the count of the list
by the group the ask named.
