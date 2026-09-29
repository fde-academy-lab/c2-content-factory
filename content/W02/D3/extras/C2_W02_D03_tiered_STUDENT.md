# Extras: one to stretch, one to recover

Both are optional and neither counts towards anything. Pick the one that matches where you actually
are tonight, and leave the other for the weekend if you want it.

---

## Stretch: the tools one step past today

You shipped the protect list, the falling-spend flag and the running total, and the window syntax
now reads naturally. Then this one is for you. Everything below goes beyond what today taught, and
nothing in it is needed for Thursday.

**The situation.** Marketing comes back with a follow-up.

> "Fifty is a number we picked. What we really want is to talk about the top quarter of each
> segment, and to see, for any member, what they did the month after a big month."

**What to build.** Three queries on the warehouse, each with one comment line above it that says
the question it answers and the rows it counts.

1. **NTILE, for the top quarter.** On Retail-Core's Q2 buyers, add
   `ntile(4) OVER (ORDER BY q2_revenue DESC)` beside each member. Retail-Core has 96 Q2 buyers, so
   each of the four groups should hold 24 members; count them to confirm it. Then say in one
   comment how NTILE treats two members with the same spend who fall either side of a group
   boundary, and whether that meets the head of Retail-Plus's rule that ties rank the same.
2. **percent_rank, for a position that reads the same in every segment.** Add
   `percent_rank() OVER (PARTITION BY segment ORDER BY q2_revenue DESC)` to the Q2 table. A value
   of 0 is the top member of a segment. Write one comment on why a percentage position lets
   Marketing compare Business, with 35 buyers, against Retail-Core, with 96, when a raw position
   cannot.
3. **LEAD, for the next month.** On the monthly spend table, add
   `lead(spend) OVER (PARTITION BY customer_id ORDER BY month)` beside each month. For C-0010, the
   July row should show Rs 4,080, the August spend. Then add `lead(month)` beside it and count the
   rows where the next row is not the next calendar month, which is today's LAG check facing the
   other way.

**The hard part, and the point.** Each tool is one line to write, and each one carries a rule about
ties or gaps that the business never stated. Your comments should name that rule for each query,
because that is the sentence Marketing will need before they act on any of them.

**A tell that you have done it well:** your NTILE comment names a case where two members with the
same spend land in different quarters, and says what you would tell Marketing about it.

The PostgreSQL 16 documentation lists all three functions in section 9.22, at
https://www.postgresql.org/docs/16/functions-window.html (verified 29 Sep 2026).

---

## Recovery: six rows, three columns, one restart

The session moved fast, the ranking columns blurred into each other, and you would rather rebuild
them than pretend. Then this one is for you, and it takes about twenty minutes.

**Step 1: predict on paper, then run.** Six invented members spent 4,800, 4,200, 4,200, 3,900,
3,100 and 3,100. Before running anything, write the three columns by hand: ROW_NUMBER, RANK and
DENSE_RANK, highest spend first. Then run this and compare your prediction line by line.

```sql
WITH invented (member, spend) AS (
    VALUES ('P', 4800), ('Q', 4200), ('R', 4200), ('S', 3900), ('T', 3100), ('U', 3100)
)
SELECT member, spend,
       row_number() OVER (ORDER BY spend DESC, member) AS row_number,
       rank()       OVER (ORDER BY spend DESC)         AS rank,
       dense_rank() OVER (ORDER BY spend DESC)         AS dense_rank
FROM   invented
ORDER  BY spend DESC, member;
```

Where your paper and the screen disagree, say out loud which rule you applied and which rule the
function applies. The usual miss is RANK's skip: after two members share 2, the next is 4, because
three members spent more than S.

**Step 2: count what each rule ships.** Marketing wants a top three from the same six. Count by hand
how many rows each function ships with `<= 3`, then check your count by wrapping the query above in
a CTE and filtering it outside, since a window cannot be filtered in WHERE.

**Step 3: add a partition.** Give the six members a group: P, Q and S in "North", and R, T and U in
"South". Add `PARTITION BY region` to all three windows and run it again. Before you run it,
predict which member is 1 in each region, and check that every count restarts at 1 when the region
changes.

```sql
WITH invented (member, region, spend) AS (
    VALUES ('P', 'North', 4800), ('Q', 'North', 4200), ('R', 'South', 4200),
           ('S', 'North', 3900), ('T', 'South', 3100), ('U', 'South', 3100)
)
SELECT region, member, spend,
       rank() OVER (PARTITION BY region ORDER BY spend DESC) AS rank_in_region
FROM   invented
ORDER  BY region, rank_in_region;
```

**What you should end up believing.** A window is two decisions: which rows count as the group,
which is PARTITION BY, and who comes first inside it, which is the ORDER BY in the window. The
ranking function only decides what happens when two rows tie, and that choice belongs to whoever
acts on the list.

**If all three steps ran clean,** open today's Round 2 notebook and redo the Retail-Core count of
rows each rule ships, without looking at the output first.
