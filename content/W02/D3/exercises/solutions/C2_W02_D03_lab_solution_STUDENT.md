# Which answers hold in the practice lab on a tie, GROUP BY against a window, and Kavya's drill, and why?

Answers: 1c 2b 3d 4a 5b 6c 7a 8d 9b 10c

The practice lab set asked for three habits on numbers the chapters never used: predict what the
ranking functions do to a tie before running them, say whether an ask needs GROUP BY or a window and
how many rows it returns, and run the whole day end to end on Kavya's drill of eight invented members.
Two of the ten items are design items: 5, the build sized for an ask by city, and 10, the second route
to a count. Problem 3's queries are the problem's own design work, and a model build is below.

**Who needs the answer.** You, at the end of the lab, checking ten letters and your queries. The TA
reads your problem 3 file the way Kavya reads a list before it leaves the team: the rule and its count
first, then the flag's months, then the running total's last row.

**The questions on the way.**

- Which idea does this set test?
- Why is each key right, item by item?
- What does a model build of Kavya's drill look like?
- Which wrong answer is worth arguing about?
- Where does this show up at work?

## Which idea does this set test?

Each of the day's tools has a shape that can be known before it runs. A ranking function's numbers
follow from where the ties sit, so its count at any line can be predicted. An ask's answer is either
one row per group or one row per row you started with, which decides GROUP BY or a window. The drill
asks for the whole chain on new numbers: a list under the head's rule with its count, a flag that reads
calendar months, the calls where the two meet, a running total whose rows step one at a time, and a
count reached a second way with no window.

## Why is each key right, item by item?

### Q1. Which RANK column comes back for the seven invented members?

Kind: predict the output, on invented numbers. The key is c, "1, 2, 2, 4, 5, 5, 5". H and J share
second place and the next place skips to 4 for K; L, M and N share fifth, the place after K.

- a, "1, 2, 2, 3, 4, 4, 4": DENSE_RANK's column, which skips nothing.
- b, "1, 2, 3, 4, 5, 6, 7": ROW_NUMBER's column, one number per member.
- d, "1, 2, 2, 4, 5, 6, 7": shares the first tie and forgets the second; L, M and N spent the same and
  share fifth.

### Q2. Which DENSE_RANK column comes back for the seven invented members?

Kind: predict the output, on invented numbers. The key is b, "1, 2, 2, 3, 4, 4, 4". Four different
figures, Rs 6,450, Rs 5,980, Rs 5,120 and Rs 4,870, get the numbers 1 to 4.

- a, "1, 2, 2, 4, 5, 5, 5": RANK's column, carried over.
- c, "1, 2, 2, 3, 4, 5, 6": shares the first tie and numbers L, M and N as if they differed.
- d, "1, 1, 1, 2, 3, 3, 3": shares a number among G, H and J, who did not spend the same.

### Q3. How many members do RANK and DENSE_RANK ship for a top four, and then for a top five?

Kind: predict the number. The key is d, "RANK 4 then 7, and DENSE_RANK 7 both times". At four, RANK ships
G, H, J and K, whose numbers are 1, 2, 2 and 4; at five it ships all seven, since L, M and N share
fifth. DENSE_RANK's largest number is 4, so all seven are inside four and inside five.

- a, "RANK 4 then 5, and DENSE_RANK 4 then 5": what ROW_NUMBER ships, which breaks every tie.
- b, "RANK 4 then 7, and DENSE_RANK 4 then 5": RANK's counts with DENSE_RANK read as ROW_NUMBER.
- c, "RANK 5 then 7, and DENSE_RANK 7 both times": RANK at four ships four, since K's place is 4 and L's
  is 5.

### Q4. Which pattern of GROUP BY (G) and window (W) answers the six asks, in order?

Kind: match the question to the method. The key is a, "W, G, G, W, W, G". Ask 1 keeps members and
numbers them inside each city, a window: 18 rows. Ask 2 is one row per segment, GROUP BY: 4 rows. Ask 3
is a GROUP BY with HAVING on the count: 2 rows, Retail-Core with 96 buyers and Retail-Plus with 76. Ask 4
keeps every member's September row and reads the row before it, LAG in a window. Ask 5 keeps all 227
buyers and adds the segment's total beside each, a window sum: 227 rows. Ask 6 is one row per segment:
4 rows.

- b, "W, G, G, G, W, G": pictures ask 4 as a table with August and September as columns; the ask keeps
  each member's own row and sets the month before beside it, which is LAG's job.
- c, "G, G, G, W, W, G": answers ask 1 with GROUP BY, which can return each city's top figure and never
  the three members who booked it.
- d, "W, G, W, W, G, G": reads "which segments" in ask 3 as a ranking, and answers ask 5 with GROUP BY,
  which would collapse the 227 buyers into four rows.

### Q5. Which build fits ask 1, and how many rows does it return?

Kind: a design item, the best-fit build with its size. The key is b, "One query ranking members in a
window partitioned by city, places 1 to 3 kept outside: 18 rows, 462 read". Six cities times three
places is 18 rows, since no city has two members tied at third, and the Q2 orders are read once.

- a, "Six sorted queries, one per city, each with LIMIT 3, glued with UNION ALL: 18 rows, 2,772 order
  rows read": the right rows at six times the reading, and six queries to edit when a city opens.
- c, "`GROUP BY city` with `max(q2_revenue)`: 6 rows, each city's top figure, 462 order rows read":
  returns one figure per city and no members.
- d, "`GROUP BY city, customer_id` sorted by Q2 revenue with `LIMIT 18`: 18 rows from across the whole
  book": LIMIT counts across the book, so the cities with the biggest spenders take every row.

### Q6. How many members does the top five ship under the head of Retail-Plus's rule, and why?

Kind: predict the number, on invented numbers. The key is c, "Six, since V-05 and V-08 tie at fifth on
Rs 5,400 and both of them ship". The Q2 totals are V-03 Rs 9,600, V-01 and V-06 Rs 7,800 each, V-02
Rs 6,900, V-05 and V-08 Rs 5,400 each, V-04 Rs 4,700 and V-07 Rs 3,900. RANK gives 1, 2, 2, 4, 5, 5, so
six members are at or inside fifth, and the list says so.

- a, "Five: V-03, V-01, V-06, V-02 and V-05, with V-08 left off by his id": ROW_NUMBER's list, which
  drops a member who spent exactly what the fifth did.
- b, "Four, since the tie at fifth straddles the line and both of its members drop": whole ties only,
  the list short of five that the head refused.
- d, "Seven, since the ties at second and at fifth each save the list a number": DENSE_RANK's count,
  which adds V-04, who ties with nobody.

### Q7. Which member on the hurried flag would a call wrongly accuse, and why?

Kind: spot the plausible wrong output, on invented numbers. The key is a, "V-02, since LAG compared his
September with July and his July with May". V-02 bought in May, July and September, so LAG read July
as his last month and May as the one before; Rs 3,000 below Rs 3,900 below Rs 4,500 looks like two
falls running, across two months with no order.

- b, "V-04, since he stands off the top five and Marketing does not ring him": his fall is real,
  Rs 2,050, Rs 1,550 and Rs 1,100 in three calendar months; being off the list decides whether he is
  rung, and says nothing about whether the flag is right.
- c, "V-05, since his September fell by less than his August did": a fall is a fall, whatever its
  size; Rs 2,300, Rs 1,750 and Rs 1,350 fall twice running in calendar months.
- d, "V-03, since his fall began in July, before the two months Marketing asked about": two months
  running means September below August and August below July, which is exactly V-03's quarter.

### Q8. Who does Marketing ring first: listed under the head's rule and flagged on calendar months?

Kind: choose the decision. The key is d, "V-03 and V-05". The checked flag holds for V-03, V-04 and
V-05; the list under the head's rule holds V-03, V-01, V-06, V-02, V-05 and V-08, so the calls are the
two members on both.

- a, "V-02, V-03 and V-05": takes the hurried flag, which accuses V-02 of a fall across two empty
  months.
- b, "V-03, V-04 and V-05": takes DENSE_RANK's list of seven, which carries V-04.
- c, "V-03 alone": takes whole ties only's list of four, which drops V-05.

### Q9. What do V-05's and V-08's rows of the running total show, and what makes each row its own step?

Kind: fix the logic, on invented numbers. The key is b, "Rs 42,900 on both, since they are peers on
Rs 5,400; add the member id to the ORDER BY". Rows that share the ORDER BY value are peers, and the
running total gives each of them the sum through the last of them: Rs 42,900 on both rows, as V-01 and
V-06 both show Rs 25,200. With `ORDER BY q2_revenue DESC, member` the rows step Rs 37,500 then
Rs 42,900, and the last row, V-07's Rs 51,500, equals a plain sum of the eight, which closes the loop.

- a, "Rs 37,500 and Rs 42,900, since each row adds its own Rs 5,400, so nothing needs changing": those
  are the figures after the fix, and the window as written gives peers one figure.
- c, "Rs 5,400 on both, since a running total restarts at a tie; add `PARTITION BY q2_revenue`": a tie
  does not restart anything, and a partition by revenue would make every figure a total of its own
  tie.
- d, "Rs 42,900 on both, since the total belongs on every row; drop the ORDER BY from the window": with
  no ORDER BY every row shows the grand total, Rs 51,500, and nothing runs.

### Q10. Which route reaches the head's count for a top two with no window, and what does it give?

Kind: a design item, the independent second route. The key is c, "Count the members who booked at
least the second member's Rs 7,800: 3". A sort with `OFFSET 1` finds the second member's figure, and
every member at or above it counts: V-03, V-01 and V-06. The tie at the line is counted whole, as RANK
ships it, by a sort and a comparison that no slip in a window could move.

- a, "Count the different Q2 figures at or above the second member's Rs 7,800: 2": counts figures,
  DENSE_RANK's logic.
- b, "Count the members who booked more than the second member's Rs 7,800: 1": "more than" drops both
  members on the line's own figure.
- d, "Rerun the list with `rank()` in a window and count the rows it ships: 3": the right number
  through a window, which the item rules out, since it shares the code it should check.

## What does a model build of Kavya's drill look like?

One version that answers every part. Each step says on its first line what it is for.

```sql
-- Kavya's drill, part 1: the list, the flag and the calls, in one query of named steps.
WITH months (member, month, spend) AS (
    VALUES ('V-01', DATE '2026-07-01', 2700), ('V-01', DATE '2026-08-01', 2950), ('V-01', DATE '2026-09-01', 2150),
           ('V-02', DATE '2026-05-01', 4500), ('V-02', DATE '2026-07-01', 3900), ('V-02', DATE '2026-09-01', 3000),
           ('V-03', DATE '2026-07-01', 4100), ('V-03', DATE '2026-08-01', 3200), ('V-03', DATE '2026-09-01', 2300),
           ('V-04', DATE '2026-07-01', 2050), ('V-04', DATE '2026-08-01', 1550), ('V-04', DATE '2026-09-01', 1100),
           ('V-05', DATE '2026-07-01', 2300), ('V-05', DATE '2026-08-01', 1750), ('V-05', DATE '2026-09-01', 1350),
           ('V-06', DATE '2026-06-01', 4000), ('V-06', DATE '2026-07-01', 3500), ('V-06', DATE '2026-09-01', 4300),
           ('V-07', DATE '2026-07-01', 2100), ('V-07', DATE '2026-08-01', 1800),
           ('V-08', DATE '2026-07-01', 1500), ('V-08', DATE '2026-08-01', 2100), ('V-08', DATE '2026-09-01', 1800)
),
q2 AS (
    -- Q2 revenue per member, July to September only.
    SELECT member, sum(spend) AS q2_revenue
    FROM   months
    WHERE  month >= DATE '2026-07-01'
    GROUP  BY member
),
listed AS (
    -- The head's rule: members who spent the same share a place, and a tie at the line ships whole.
    SELECT member, q2_revenue, rank() OVER (ORDER BY q2_revenue DESC) AS place
    FROM   q2
),
lagged AS (
    -- Each member's own months, with the two rows before and the months they came from.
    SELECT member, month, spend,
           lag(spend, 1) OVER (PARTITION BY member ORDER BY month) AS spend_1_back,
           lag(spend, 2) OVER (PARTITION BY member ORDER BY month) AS spend_2_back,
           lag(month, 1) OVER (PARTITION BY member ORDER BY month) AS month_1_back,
           lag(month, 2) OVER (PARTITION BY member ORDER BY month) AS month_2_back
    FROM   months
),
flagged AS (
    -- Three calendar months, each lower: a skipped month breaks the run.
    SELECT member
    FROM   lagged
    WHERE  month = DATE '2026-09-01'
      AND  spend < spend_1_back AND spend_1_back < spend_2_back
      AND  month_1_back = DATE '2026-08-01' AND month_2_back = DATE '2026-07-01'
)
SELECT l.place, l.member, l.q2_revenue, (f.member IS NOT NULL) AS ring_first
FROM   listed l
LEFT   JOIN flagged f USING (member)
WHERE  l.place <= 5
ORDER  BY l.place, l.member;

-- Part 2: the running total of all eight, by revenue and then by id, beside a plain sum that closes
-- the loop, and the top two's count reached with no window.
WITH months (member, month, spend) AS (
    VALUES ('V-01', DATE '2026-07-01', 2700), ('V-01', DATE '2026-08-01', 2950), ('V-01', DATE '2026-09-01', 2150),
           ('V-02', DATE '2026-05-01', 4500), ('V-02', DATE '2026-07-01', 3900), ('V-02', DATE '2026-09-01', 3000),
           ('V-03', DATE '2026-07-01', 4100), ('V-03', DATE '2026-08-01', 3200), ('V-03', DATE '2026-09-01', 2300),
           ('V-04', DATE '2026-07-01', 2050), ('V-04', DATE '2026-08-01', 1550), ('V-04', DATE '2026-09-01', 1100),
           ('V-05', DATE '2026-07-01', 2300), ('V-05', DATE '2026-08-01', 1750), ('V-05', DATE '2026-09-01', 1350),
           ('V-06', DATE '2026-06-01', 4000), ('V-06', DATE '2026-07-01', 3500), ('V-06', DATE '2026-09-01', 4300),
           ('V-07', DATE '2026-07-01', 2100), ('V-07', DATE '2026-08-01', 1800),
           ('V-08', DATE '2026-07-01', 1500), ('V-08', DATE '2026-08-01', 2100), ('V-08', DATE '2026-09-01', 1800)
),
q2 AS (
    SELECT member, sum(spend) AS q2_revenue
    FROM   months
    WHERE  month >= DATE '2026-07-01'
    GROUP  BY member
)
SELECT member, q2_revenue,
       sum(q2_revenue) OVER (ORDER BY q2_revenue DESC, member) AS running,
       (SELECT sum(q2_revenue) FROM q2)                        AS plain_total,
       (SELECT count(*) FROM q2
        WHERE  q2_revenue >= (SELECT q2_revenue FROM q2 ORDER BY q2_revenue DESC OFFSET 1 LIMIT 1)) AS top_two_count
FROM   q2
ORDER  BY q2_revenue DESC, member;
```

| What the drill prints | Value |
|---|---|
| The list under the head's rule, top five | 6 members: V-03, V-01 and V-06, V-02, V-05 and V-08 |
| The hurried flag, with no calendar check | 4 members: V-02, V-03, V-04 and V-05 |
| The checked flag | 3 members: V-03, V-04 and V-05 |
| The calls, listed and checked | 2 members: V-03 and V-05 |
| The running total by revenue and id | Rs 9,600, 17,400, 25,200, 32,100, 37,500, 42,900, 47,600 and 51,500 |
| The plain sum of the eight | Rs 51,500, equal to the running total's last row |
| The top two under the head's rule, with no window | 3 members |

A TA reading your file checks four things, in this order: the list's count says which rule made it,
the flag carries the months LAG read, the calls are the overlap of the two, and the running total's
last row equals a sum you counted without it.

## Which wrong answer is worth arguing about?

Item 7, option b. V-04 is the member a careful analyst most wants to take off the call list, since he
is not on the top five, and the argument sounds like rigour. His three months are a real fall in
calendar months, so the flag is right about him, and being off the list is a separate decision about
who gets rung this week. The flag and the list answer two different questions, and item 8 is where
the answers meet.

## Where does this show up at work?

Analyst interviews at data teams ask for the three functions on a tie, then hand over an ask and ask
"GROUP BY or a window, and how many rows?", and close on a small end-to-end problem like Kavya's drill,
where the interviewer watches for the count, the months behind a flag and the last row of a running
total.
