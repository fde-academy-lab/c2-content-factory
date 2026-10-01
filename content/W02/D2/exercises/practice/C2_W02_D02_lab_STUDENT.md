# Do the day's joins still tell the truth on refunds, and on a quarter the day never touched?

Your TA runs about 60 minutes of this set after the day's teaching blocks.
Today the tentative faculty block takes the afternoon's last 120 minutes, so the lab opens on the
escalated case's parts 3 to 5 (`unguided/C2_W02_D02_escalated_STUDENT.md`), then runs this set's
problems 1 to 3, the second case in pairs (`unguided/C2_W02_D02_second_case_STUDENT.md`) and the
interview drill aloud; problem 4 and whatever is left go home with the take-home. The set has four
problems, and they climb in difficulty. The first three run on small invented tables written for this
lab; the fourth runs on the warehouse, on a quarter the day never touched. Work alone first, then
compare with a neighbour before the TA walks the answers.

The question over the whole lab is the one Anand asked in the morning, turned to a new corner of the
book: what did we book, what happened to it afterwards, and how do you know the number is not
double-counted?

For problems 1 to 3, post one line, eleven letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxxxxxxxxx
```

---

## Which tables does the lab run on?

The returns desk has sent six Q1 web orders and the refund rows raised against order ids in their
range. Every number here is invented for the lab.

`lab_orders` (invented):

| order_id | channel | amount |
|---|---|---|
| W-1 | web | 3,200 |
| W-2 | web | 12,500 |
| W-3 | web | 48,000 |
| W-4 | web | 1,900 |
| W-5 | web | 7,400 |
| W-6 | web | 2,600 |

`lab_refunds` (invented; refunds are stored as negative amounts, as the warehouse stores them):

| refund_id | order_id | refund_date | amount | reason |
|---|---|---|---|---|
| R-1 | W-2 | 2026-04-18 | -1,500 | damaged |
| R-2 | W-3 | 2026-04-22 | -6,000 | wrong item |
| R-3 | W-3 | 2026-05-06 | -4,000 | damaged |
| R-4 | W-5 | 2026-05-10 | -7,400 | returned in full |
| R-5 | W-7 | 2026-04-03 | -900 | damaged |

To load them, paste this into a psql session; they are TEMP tables and vanish when you disconnect.

```sql
CREATE TEMP TABLE lab_orders (order_id text PRIMARY KEY, channel text, amount numeric(12, 2));
CREATE TEMP TABLE lab_refunds (refund_id text PRIMARY KEY, order_id text, refund_date date,
                               amount numeric(12, 2), reason text);
INSERT INTO lab_orders VALUES
    ('W-1', 'web', 3200), ('W-2', 'web', 12500), ('W-3', 'web', 48000),
    ('W-4', 'web', 1900), ('W-5', 'web', 7400), ('W-6', 'web', 2600);
INSERT INTO lab_refunds VALUES
    ('R-1', 'W-2', '2026-04-18', -1500, 'damaged'),
    ('R-2', 'W-3', '2026-04-22', -6000, 'wrong item'),
    ('R-3', 'W-3', '2026-05-06', -4000, 'damaged'),
    ('R-4', 'W-5', '2026-05-10', -7400, 'returned in full'),
    ('R-5', 'W-7', '2026-04-03', -900, 'damaged');
```

---

## Problem 1. How many rows does each join return on the refund tables?

Allow about 10 minutes. Before you trust any join at work, you predict its row count aloud.

Write your four numbers on paper before you run anything. Then run the four joins and mark each
prediction right or wrong, with the row that surprised you.

### Q1. How many rows does `lab_orders JOIN lab_refunds ON order_id` return?

a) 6, one row for each order the desk sent
b) 4, one row per refund that finds its order
c) 3, one row for each order that was refunded
d) 5, one row for each refund row on the list

### Q2. How many rows does the LEFT join from orders to refunds return?

a) 6, since a LEFT join keeps each order once
b) 5, the same as the refund rows on the list
c) 9, the six orders and three refunded ones
d) 7, four matched rows and three unrefunded

### Q3. How many rows does the RIGHT join from orders to refunds return?

a) 5, every refund row once, as ids are unique
b) 4, since a refund with no order is dropped
c) 7, the matched rows and the unrefunded orders
d) 6, one row for each order the desk sent over

### Q4. How many rows does the FULL join return?

a) 11, the six orders and the five refunds added
b) 7, the same as the LEFT join and no more
c) 8, the LEFT join's rows and the refund for W-7
d) 5, one row per refund, the larger table's count

---

## Problem 2. Which join answers each of five business questions?

Allow about 10 minutes. At work you choose the join from the question, before any SQL is typed.

Items 5 to 9 share the same four options, and an option may answer more than one item.

### Q5. The returns desk asks: "For the orders that were refunded, what was the average refund per order?" Which join answers it?

a) INNER JOIN, matched pairs only
b) LEFT JOIN, every order kept
c) Anti-join, unmatched orders
d) FULL JOIN, both sides' orphans

### Q6. Anand asks: "For every Q1 web order, booked and refunded, whether it was refunded or not?" Which join answers it?

a) INNER JOIN, matched pairs only
b) LEFT JOIN, every order kept
c) Anti-join, unmatched orders
d) FULL JOIN, both sides' orphans

### Q7. Kavya Nair, the team's senior analyst, asks: "Which Q1 web orders have no refund at all, so we can sample them for the satisfaction survey?" Which join answers it?

a) INNER JOIN, matched pairs only
b) LEFT JOIN, every order kept
c) Anti-join, unmatched orders
d) FULL JOIN, both sides' orphans

### Q8. The auditor asks: "Which orders and which refunds fail to find each other, on either side?" Which join answers it?

a) INNER JOIN, matched pairs only
b) LEFT JOIN, every order kept
c) Anti-join, unmatched orders
d) FULL JOIN, both sides' orphans

### Q9. The returns desk asks: "Which refund reasons came up on refunded orders, and how often?" Which join answers it?

a) INNER JOIN, matched pairs only
b) LEFT JOIN, every order kept
c) Anti-join, unmatched orders
d) FULL JOIN, both sides' orphans

---

## Problem 3. Is 16.3 percent the right Q1 refund rate for these six orders?

Allow about 15 minutes. At work, even a plausible rate gets read back to the rows that made it.

Anand wants the Q1 refund rate on these web orders: refunded value over booked value. A teammate
sends this, and reports 16.3 percent:

```sql
SELECT count(*) AS rows_out,
       sum(o.amount) AS booked,
       -sum(r.amount) AS refunded,
       round(100.0 * -sum(r.amount) / sum(o.amount), 1) AS refund_rate
FROM lab_orders o
LEFT JOIN lab_refunds r ON r.order_id = o.order_id
WHERE r.refund_date BETWEEN '2026-04-01' AND '2026-06-28';
```

| rows_out | booked | refunded | refund_rate |
|---|---|---|---|
| 4 | 1,15,900 | 18,900 | 16.3 |

### Q10. Which orders make up the booked figure of 1,15,900 that the rate divides by?

a) all six orders, each of them counted once
b) the three refunded orders, each counted once
c) the refunded orders, with W-3 counted twice
d) all six orders, with W-3 counted twice

### Q11. What Q1 refund rate should Anand be given for these six orders?

a) 15.3 percent, 18,900 over 1,23,600
b) 25.0 percent, 18,900 over 75,600
c) 16.3 percent, 18,900 over 1,15,900
d) 26.2 percent, 19,800 over 75,600

Then write the corrected query yourself and check that it returns the rate you chose. Put the
reconciliation above it as a comment block: orders in, rows out, and the difference.

---

## Problem 4. What did Q1 collect against what it booked, and how do you prove it?

Allow about 25 minutes. At work this is the month-end report, rerun on a period nobody checked for
you.

The day's escalated case ran on Q2. Anand now asks for the same report on Q1, the quarter the day
never touched: "Show me, by channel, what we booked in Q1 and what we collected against it, and
prove the collected number is not double-counted."

On the warehouse, write and run:

1. Q1 orders and booked by channel, from orders alone.
2. Collected by channel at order grain, with a retry counted once, and the count reconciliation
   written above the query before you run it.
3. The Q1 unpaid list and the Q1 double-paid list, each with its count and value by channel.
4. The report by channel with three checks that return true: rows out equals rows in, booked minus
   collected equals the unpaid total plus anything paid short, and collected plus the surplus posted
   twice equals what the feed posted against Q1 orders.
5. One sentence to Anand that gives the Q1 collected number and says how you know it is honest.

Stretch, if you finish early: the refunds table holds refunds raised against Q1 orders. Add refunded
and collected net of refunds by channel, and say in one comment line whether the net figure belongs
in the report Anand signs or beside it.
