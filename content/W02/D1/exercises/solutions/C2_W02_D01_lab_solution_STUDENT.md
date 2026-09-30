# Which answers hold in the practice lab on row counts, running order and the returns suite, and why?

Answers: 1c 2a 3d 4b 5a 6c 7d 8b 9c 10a

The practice lab set asked for three habits on questions the chapters never ran: predict a query's
row count before running it, say the order the database works through a query and defend one
placement, and build a short suite for a new stakeholder, the head of customer service, that ties out
and draws the same sample twice. One of the ten items is a design item, item 9, the second route; the
suite itself is the problem's design work, and a model suite is below.

**Who needs the answer.** You, at the end of the lab, checking ten letters and your suite. Anand's
analyst will read any suite the team ships the way the TA reads yours tonight: definition first, then
the tie-out, then the sample.

**The questions on the way.**

- Which idea does this set test?
- Why is each key right, item by item?
- What does a model returns suite look like?
- Which wrong answer is worth arguing about?
- Where does this show up at work?

## Which idea does this set test?

Every query has a shape that can be known before it runs: how many groups it forms, which rows reach
them, and which groups survive. The first two problems ask for that shape. The third asks for the whole
day on a new definition, returned orders: the definition stated once, counts that name what they count,
a tie-out on the columns that add, a half-year counted from the orders, and a sample ordered on a
column no two rows share, beside a fingerprint.

## Why is each key right, item by item?

### Q1. How many rows does the Q2 channel and status query return?

Kind: predict the output. The key is c, 9: three channels times three statuses, all present in Q2.

- a, 3: one row per channel, as if the query grouped by channel alone.
- b, 6: three channels times two quarters, the answer for a query grouped by channel and quarter with
  no WHERE line.
- d, 18: channel, status and quarter together, the answer if the WHERE were removed and the quarter
  grouped.

### Q2. How many segment-quarters clear a bar of 90 customers?

Kind: predict the output from the table. The key is a, 3: Retail-Core in Q1 (102) and Q2 (96) and
Retail-Plus in Q1 (91). Retail-Plus in Q2 has 76.

- b, 4: counts Retail-Plus Q2 as well, which sits at 76.
- c, 2: keeps only Retail-Core, missing Retail-Plus Q1's 91.
- d, 8: every segment-quarter, as if the HAVING line were not there.

### Q3. How many segments placed more than 100 orders in Q2?

Kind: predict the output from the table. The key is d, 2: in Q2, Retail-Core placed 193 orders and
Retail-Plus 140, while Business placed 91 and Student 38.

- a, 4: every segment, as if HAVING did nothing.
- b, 3: counts each segment's half-year orders (Business 188, Retail-Core 392, Retail-Plus 355), which
  is the answer with the WHERE line ignored.
- c, 1: keeps only Retail-Core, as if 140 were under the bar.

### Q4. How many customers does the half-year list hold?

Kind: predict the output. The key is b, 301: DISTINCT keeps each customer once across both quarters.

- a, 471: Q1's 244 added to Q2's 227, which counts the 170 customers who bought in both quarters
  twice.
- c, 1,000: one row per order, which is what the query returns without DISTINCT.
- d, 340: every member on the customers table, including the 39 who bought nothing.

### Q5. In which order does the database work through the five clauses after FROM and the lookup?

Kind: order the steps. The key is a, "WHERE, GROUP BY, HAVING, SELECT, ORDER BY": rows are filtered,
grouped, groups are filtered, the result is computed, and the result is sorted.

- b, "SELECT, WHERE, GROUP BY, HAVING, ORDER BY": the SELECT's counts cannot exist before the groups.
- c, "WHERE, GROUP BY, SELECT, HAVING, ORDER BY": HAVING comes before SELECT, which is why HAVING
  repeats `count(DISTINCT o.customer_id)` rather than using the name customers.
- d, "GROUP BY, WHERE, HAVING, SELECT, ORDER BY": grouping first would group the web and store orders
  the WHERE is meant to remove.

### Q6. Why does WHERE run before GROUP BY while HAVING runs after it?

Kind: defend a placement. The key is c, "WHERE judges single rows before groups exist; HAVING judges a
group's count once groups form". The app filter is a fact about each order, so it acts before the
groups; the bar of 30 is a fact about a group, so it waits for them.

- a, "WHERE is written first, and the database runs the clauses in the order they are written": the
  written order starts with SELECT, which runs fifth.
- b, "HAVING needs the names SELECT gives the columns, so it has to wait for SELECT to finish": HAVING
  runs before SELECT, and in Postgres it cannot use SELECT's names; ORDER BY can, because it runs
  after.
- d, "HAVING and WHERE filter in the same way, and HAVING runs later only to save the database work":
  they filter different things, rows against groups, which is why moving one into the other's place
  changes the answer or fails.

### Q7. Which channel's returned orders rose from Q1 to Q2?

Kind: read the output. The key is d, store: 25 returned orders in Q1 and 29 in Q2.

- a, app: 42 then 29, a fall.
- b, web: 30 then 29, a fall.
- c, "none, since every channel's returns fell": the store's rose.

### Q8. Which tie-out holds on the returns suite in Q1?

Kind: choose the check. The key is b, "The channels' orders add to the Q1 row's 97; their customers add
to 90 against its 78". The orders, 42, 25 and 30, and the rupees, Rs 84,11,410, Rs 17,76,150 and
Rs 92,18,920, add to the quarter's 97 and Rs 1,94,06,480. The customers, 39, 24 and 27, add to 90,
because a customer who returned through two channels sits in both rows, so the sheet carries a note
under the customer column.

- a, "The channels' orders and customers both add to the Q1 row, 97 orders and 90 customers": the Q1
  row counts 78 customers, each once.
- c, "The channels' customers add to the Q1 row's 78, and their orders to its 97": 39, 24 and 27 add to
  90.
- d, "Neither adds, since each channel's returns are counted in a group of their own": orders and
  rupees add, since every returned order sits in exactly one channel.

### Q9. Which second route confirms the half-year count of customers who returned an order?

Kind: a design item, the independent second route. The key is c, "Q1's 78 plus Q2's 76 less the 24 in
both, which gives 130". Adding the quarters counts the 24 twice, and taking them off once gives 130,
the same as the count from the orders.

- a, "Q1's 78 plus Q2's 76, which gives 154": counts the 24 customers who returned in both quarters
  twice.
- b, "The 184 returned orders, one customer each, which gives 184": counts orders, and some customers
  returned more than one.
- d, "The larger quarter, 78, since most customers who returned in Q2 also returned in Q1": only 24 of
  Q2's 76 returned in Q1 as well, so 52 are missing.

### Q10. Which ordering and printout make the service team's sample auditable?

Kind: choose the fix and its check. The key is a, "`ORDER BY order_id LIMIT 5`, with the returned
book's rows, rupees and customers printed beside it". No two orders share an id, so the five are fixed:
KR-00540, KR-00548, KR-00556, KR-00565 and KR-00567, Rs 4,110 in all. The fingerprint, 184 rows,
Rs 3,80,55,960 and 130 customers, says whether the returned book moved between two runs.

- b, "`LIMIT 5` alone, with the returned book's rows, rupees and customers printed beside it": the
  fingerprint is right and the sample can still change on a rerun, since nothing fixes which five.
- c, "`ORDER BY order_id LIMIT 5`, with the time the run took printed beside it": the sample repeats,
  and the time says nothing about the book.
- d, "`ORDER BY channel LIMIT 5`, with the returned book's row count printed beside it, and nothing
  else": 29 orders share each channel in Q2, so the order among them is left to the database, and a
  row count misses a corrected amount.

## What does a model returns suite look like?

One version that answers every part, run on the warehouse. Each query states the definition on its
first step and names what each count counts.

```sql
-- The returns suite, part 1: orders, customers who returned and rupees per channel and quarter.
WITH returned AS (
    -- The definition, stated once: an order whose status is returned.
    SELECT order_id, customer_id, quarter, channel, amount
    FROM   orders
    WHERE  status = 'returned'
),
per_channel AS (
    -- One row per channel and quarter; each customer is counted once within a row.
    SELECT channel, quarter,
           count(*)                    AS orders,
           count(DISTINCT customer_id) AS customers,
           sum(amount)                 AS rupees
    FROM   returned
    GROUP  BY channel, quarter
)
SELECT * FROM per_channel ORDER BY quarter, channel;

-- Part 2: the same measures for each quarter across all channels, for the tie-out.
WITH returned AS (
    SELECT order_id, customer_id, quarter, channel, amount
    FROM   orders
    WHERE  status = 'returned'
)
SELECT quarter,
       count(*)                    AS orders,
       count(DISTINCT customer_id) AS customers,
       sum(amount)                 AS rupees
FROM   returned
GROUP  BY quarter
ORDER  BY quarter;

-- Part 3: the half-year, counted from the orders.
SELECT count(DISTINCT customer_id) AS customers_half_year
FROM   orders
WHERE  status = 'returned';

-- Part 4: five returned Q2 orders, ordered on a column no two rows share.
SELECT order_id, channel, amount
FROM   orders
WHERE  status = 'returned' AND quarter = 'Q2'
ORDER  BY order_id
LIMIT  5;

-- Part 5: the returned book's fingerprint, printed beside the sample.
SELECT count(*) AS rows, sum(amount) AS rupees, count(DISTINCT customer_id) AS customers
FROM   orders
WHERE  status = 'returned';
```

| What the suite prints | Q1 | Q2 |
|---|---|---|
| app: orders, customers who returned, rupees | 42, 39, Rs 84,11,410 | 29, 28, Rs 66,02,830 |
| store: orders, customers who returned, rupees | 25, 24, Rs 17,76,150 | 29, 28, Rs 69,23,060 |
| web: orders, customers who returned, rupees | 30, 27, Rs 92,18,920 | 29, 27, Rs 51,23,590 |
| All channels: orders, customers who returned, rupees | 97, 78, Rs 1,94,06,480 | 87, 76, Rs 1,86,49,480 |

The half-year holds 130 customers who returned an order. Chapter 5's `GROUPING SETS` would print the
channel rows and the quarter rows in one pass, which is the better build once the suite settles; two
queries sharing one definition are fine for a first suite.

A TA reading your suite checks four things, in this order: the definition sits in one place, the
customer counts are distinct counts named for what they count, the channel rows tie out on orders and
rupees with a note on customers, and the sample is ordered on the order id beside a fingerprint.

## Which wrong answer is worth arguing about?

Item 6, option b. Many learners have seen `ORDER BY revenue` use a name SELECT gave, and conclude that
every later clause can. HAVING cannot in Postgres, because it runs before SELECT, while ORDER BY runs
after it. The argument is worth having because it is the fastest way to remember the order: whatever
can see SELECT's names ran after SELECT.

## Where does this show up at work?

Analyst interviews at data teams ask for the running order of a query and then hand over a new table
and a new stakeholder, which is problem 3 in miniature: a definition, counts that say what they count,
a tie-out and a sample someone else can draw again.
