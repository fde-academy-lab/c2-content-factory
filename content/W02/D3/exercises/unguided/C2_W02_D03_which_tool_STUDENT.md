# Round 1 set: who goes on the protect list?

Marketing wrote on Monday: "Retail-Plus frequency is the problem, so we want to protect our best
members before they drift. Give us the top fifty customers by Q2 revenue in each segment." Before
anyone writes a query, the team has to decide which questions GROUP BY answers and which ones need
a window, and then check that the list answers the question Marketing asked.

Seven items, about fifteen minutes, worked in pairs. Q2 revenue per member is the booked amount of
the member's Q2 orders, all statuses, which is the definition Monday's suite used for the
Rs 9,84,00,000 quarter. The warehouse has 227 Q2 buyers: 35 Business, 76 Retail-Plus, 96
Retail-Core and 20 Student.

Post one line in this shape, your seven letters in item order: `1x 2x 3x 4x 5x 6x 7x`

---

### Q1

Anand's board pack needs one line per segment carrying the segment's Q2 revenue and its number of
buyers. Which tool answers it, and what comes back?

a) A window sum partitioned by segment, which returns 227 rows that repeat their segment's total
b) GROUP BY segment, which returns four rows with the revenue and the buyer count on each
c) RANK over the segment column, filtered to position one, which returns each segment's top member
d) A running total ordered by segment, which returns 227 rows that climb to the quarter's total

### Q2

Marketing wants every Q2 buyer on one sheet with the member's own Q2 revenue and the segment's
total beside it, so a member's share of the segment can be read off the row. Which tool keeps
both figures on the same row?

a) GROUP BY customer_id and segment, which returns one row per member carrying the member's total
b) GROUP BY segment, which returns four rows, each holding the segment total and its members
c) A HAVING clause on the member totals, which keeps the member rows and the segment rows together
d) sum(q2_revenue) OVER (PARTITION BY segment), which keeps all 227 rows and adds the total

### Q3

An analyst sends a protect list built with `row_number() OVER (ORDER BY q2_revenue DESC)` and a
filter at fifty. Counted by segment it holds 35 Business, 11 Retail-Plus, 4 Retail-Core and no
Student members. What should the reviewer conclude before it reaches Marketing?

a) It ranked the whole table, and Marketing asked for fifty members inside each segment
b) It is right, since Business members spend the most and so deserve the most protection
c) The Student segment had no Q2 buyers, which is why no Student member made the list
d) The filter at fifty dropped rows, and raising it to 200 gives each segment its fifty

### Q4

The fix partitions the ranking by segment and keeps `row_number() OVER (PARTITION BY segment
ORDER BY q2_revenue DESC)` at fifty or below. How many rows does the list carry?

a) 200, which is fifty for each of the four segments
b) 227, since a partition keeps every buyer in the table
c) 155, since two segments have fewer than fifty buyers
d) 50, since the filter at fifty still applies to the whole result

### Q5

On the fixed list the Business line holds 35 members, which is every Business member who bought in
Q2. What should the list tell Marketing about that line?

a) That fifteen Business members were cut by the filter and should be added back by hand
b) That the Business fifty is every Business Q2 buyer, so nobody there was ranked out
c) That Business needs a tighter cut-off, such as a top twenty, to keep the list selective
d) That the Business rows should come off the list, since fifty members could not be found

### Q6

A colleague's list uses `rank() OVER (PARTITION BY customer_id ORDER BY q2_revenue DESC)` on the
table of member totals, filtered at fifty, and it comes back with all 227 Q2 buyers. What went
wrong, and what is the fix?

a) The filter ran before the rank, so the fix is to move the filter inside the window itself
b) RANK kept every tie together, so the fix is ROW_NUMBER, which always ships exactly fifty
c) The order should run ascending, so the fix is to reverse it and keep the same partition
d) Each member is a partition of one row and ranks 1, so the fix is to partition by segment

### Q7

Which order of steps builds the per-segment protect list and proves it before Marketing sees it?

a) Rank the order rows within each segment, then sum each member's Q2 orders, filter at fifty and count by segment
b) Keep the fifty largest orders, then sum each member's Q2 orders, rank within each segment and count by segment
c) Sum each member's Q2 orders, rank within each segment in a CTE, filter at fifty outside it, then count by segment
d) Sum each member's Q2 orders, filter the top fifty members first, then rank within each segment and count by segment
