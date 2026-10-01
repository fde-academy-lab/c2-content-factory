# Which extra fits you tonight: rebuilding each chapter's window on a few invented members, or taking the plan line and the tie rule a step past today?

Both are optional and neither is graded. Each stands on its own, so pick the one that matches where
you are after today's six chapters. Kalpa Retail's marketing lead asked for the top fifty customers
by Q2 revenue in each segment and a flag on anyone whose monthly spend fell two months running, the
head of Retail-Plus asked for members who spent the same to be ranked the same, and Meera Raghavan,
the CEO, asked for revenue to accumulate week by week against the plan line. Q2 is July to September
2026, and revenue is booked revenue, every order at its amount whatever its status. Every query
below runs in a new query window connected to your Codespace's `kalpa` database, or in a notebook
cell through `kit.sql`.

---

## Recover: can you rebuild each chapter's window on a few invented members, and predict every number first?

This one is for you if the morning moved fast and the windows blurred into each other.

**Who needs the answer.** Marketing acts on lists your windows build. If you can predict what a
window prints on six invented rows, you can explain any number it prints on Kalpa's 227 members, and
explaining the number is what Kavya Nair, the senior analyst, asks for before anything leaves the
team.

**The questions on the way.**

1. Chapter 1: is one row of the list an order or a member?
2. Chapter 2: where does the numbering restart when a partition is added?
3. Chapter 3: what do the three functions give, and how many rows does each ship at a line?
4. Chapter 4: whose month does LAG read when nothing partitions the window?
5. Chapter 5: which running total does each order of a busy day show?
6. Chapter 6: does a month with no order break the run?

Each step types its invented members into the query with `VALUES`, so nothing in the warehouse is
read. Write your prediction on paper before you run each one.

### Chapter 1: is one row of the list an order or a member?

Three invented members placed five orders: J placed three, of Rs 900, 800 and 400, K one of Rs 1,200
and L one of Rs 300. Predict how many members the list of the three biggest orders names, then run
both queries.

```sql
WITH invented (member, order_id, amount) AS (
    VALUES ('J', 'X-01', 900), ('J', 'X-02', 800), ('K', 'X-03', 1200),
           ('L', 'X-04', 300), ('J', 'X-05', 400)
),
top_orders AS (
    SELECT member, order_id, amount FROM invented ORDER BY amount DESC, order_id LIMIT 3
)
SELECT count(*) AS rows_on_list, count(DISTINCT member) AS members FROM top_orders;

WITH invented (member, order_id, amount) AS (
    VALUES ('J', 'X-01', 900), ('J', 'X-02', 800), ('K', 'X-03', 1200),
           ('L', 'X-04', 300), ('J', 'X-05', 400)
),
per_member AS (
    SELECT member, sum(amount) AS spend FROM invented GROUP BY member
)
SELECT member, spend, row_number() OVER (ORDER BY spend DESC, member) AS place
FROM   per_member
ORDER  BY place;
```

Your run should show an orders list of 3 rows and 2 members, since J appears twice. Summed
first, the members rank J (Rs 2,100) first, K (Rs 1,200) second and L (Rs 300) third. Chapter
1's list of 50 rows and 28 members went wrong the same way, and the same check catches it.

### Chapter 2: where does the numbering restart when a partition is added?

Six invented members in two regions: P (North, Rs 4,800), Q (North, Rs 4,200), R (South, Rs 4,200),
S (North, Rs 3,900), T (South, Rs 3,100) and U (South, Rs 3,100). Predict who is first in South.

```sql
WITH invented (member, region, spend) AS (
    VALUES ('P', 'North', 4800), ('Q', 'North', 4200), ('R', 'South', 4200),
           ('S', 'North', 3900), ('T', 'South', 3100), ('U', 'South', 3100)
)
SELECT region, member, spend,
       row_number() OVER (ORDER BY spend DESC, member)                     AS place_overall,
       row_number() OVER (PARTITION BY region ORDER BY spend DESC, member) AS place_in_region
FROM   invented
ORDER  BY region, place_in_region;
```

Your run should number North P 1, Q 2, S 3 and South R 1, T 2, U 3, where the overall
numbering gave S 4, T 5 and U 6. To keep the top two in each region, wrap the query in a named step
and filter `place_in_region <= 2` outside it: P, Q, R and T. Filtering inside WHERE stops with
"window functions are not allowed in WHERE", as chapter 2 showed.

### Chapter 3: what do the three functions give, and how many rows does each ship at a line?

Take the same six members, now all in one list. Write the ROW_NUMBER, RANK and DENSE_RANK columns by hand,
then count what each rule ships for a top three and for a top five.

```sql
WITH invented (member, spend) AS (
    VALUES ('P', 4800), ('Q', 4200), ('R', 4200), ('S', 3900), ('T', 3100), ('U', 3100)
),
r AS (
    SELECT member, spend,
           row_number() OVER (ORDER BY spend DESC, member) AS rn,
           rank()       OVER (ORDER BY spend DESC)         AS rk,
           dense_rank() OVER (ORDER BY spend DESC)         AS dr,
           count(*)     OVER (PARTITION BY spend)          AS tied_with
    FROM   invented
)
SELECT count(*) FILTER (WHERE rn <= 3)                 AS row_number_top3,
       count(*) FILTER (WHERE rk <= 3)                 AS rank_top3,
       count(*) FILTER (WHERE dr <= 3)                 AS dense_rank_top3,
       count(*) FILTER (WHERE rk + tied_with - 1 <= 3) AS whole_ties_top3,
       count(*) FILTER (WHERE rk <= 5)                 AS rank_top5,
       count(*) FILTER (WHERE dr <= 5)                 AS dense_rank_top5,
       count(*) FILTER (WHERE rk + tied_with - 1 <= 5) AS whole_ties_top5
FROM   r;
```

Your run should give ROW_NUMBER 1 to 6, RANK 1, 2, 2, 4, 5, 5 and DENSE_RANK 1,
2, 2, 3, 4, 4. For a top three the rules ship 3, 3, 4 and 3: nobody ties at third, yet DENSE_RANK
ships S as well, because the tie between Q and R left its numbers one behind. Retail-Core's 52
came from the same slip. For a top five, where T and U tie at fifth, RANK ships 6 and whole ties only ships 4.

### Chapter 4: whose month does LAG read when nothing partitions the window?

Two invented members: V bought in July (Rs 400), August (Rs 650) and September (Rs 900), and W in
August (Rs 700) and September (Rs 600). Predict what the version with no partition puts beside W's
August.

```sql
WITH monthly (member, month, spend) AS (
    VALUES ('V', DATE '2026-07-01', 400), ('V', DATE '2026-08-01', 650),
           ('V', DATE '2026-09-01', 900), ('W', DATE '2026-08-01', 700),
           ('W', DATE '2026-09-01', 600)
)
SELECT member, month, spend,
       lag(spend, 1)  OVER (ORDER BY member, month)                    AS back_1_no_partition,
       lag(spend, 2)  OVER (ORDER BY member, month)                    AS back_2_no_partition,
       lag(member, 2) OVER (ORDER BY member, month)                    AS whose_back_2,
       lag(spend, 1)  OVER (PARTITION BY member ORDER BY month)        AS back_1,
       lag(spend, 2)  OVER (PARTITION BY member ORDER BY month)        AS back_2
FROM   monthly
ORDER  BY member, month;
```

With no partition, your run should show 900 beside W's August as its month before, which is V's
September, and W's September reads 700 and then V's 900, so it looks like two falls running: 600
below 700 below 900. With `PARTITION BY member`, W's August shows NULL and W is never flagged. A
value on a member's first month is the tell, as chapter 4 found on Kalpa's 20 flags.

### Chapter 5: which running total does each order of a busy day show?

Four invented orders: A-1 on 1 July (Rs 100), A-2 and A-3 on 2 July (Rs 200 and Rs 300) and A-4 on 3
July (Rs 50). Predict what A-2 shows when the window is ordered by the day alone.

```sql
WITH invented (day, order_id, amount) AS (
    VALUES (DATE '2026-07-01', 'A-1', 100), (DATE '2026-07-02', 'A-2', 200),
           (DATE '2026-07-02', 'A-3', 300), (DATE '2026-07-03', 'A-4', 50)
)
SELECT day, order_id, amount,
       sum(amount) OVER (ORDER BY day)           AS by_day_alone,
       sum(amount) OVER (ORDER BY day, order_id) AS by_day_and_id
FROM   invented
ORDER  BY day, order_id;
```

By the day alone, your run should show A-2 and A-3 as peers, both on 600, the close of 2
July; with the order id added they show 300 and 600. Both versions end on 650, the total you can
count without a window, which is the check chapter 5 ran on Monday's Rs 9,84,00,000.

### Chapter 6: does a month with no order break the run?

Two invented members: X bought in May (Rs 900), July (Rs 700) and September (Rs 500), with nothing
in June or August, and Y in July (Rs 800), August (Rs 650) and September (Rs 400). Predict which of
them each flag keeps.

```sql
WITH monthly (member, month, spend) AS (
    VALUES ('X', DATE '2026-05-01', 900), ('X', DATE '2026-07-01', 700),
           ('X', DATE '2026-09-01', 500), ('Y', DATE '2026-07-01', 800),
           ('Y', DATE '2026-08-01', 650), ('Y', DATE '2026-09-01', 400)
),
lagged AS (
    SELECT member, month, spend,
           lag(spend, 1) OVER (PARTITION BY member ORDER BY month) AS spend_1_back,
           lag(spend, 2) OVER (PARTITION BY member ORDER BY month) AS spend_2_back,
           lag(month, 1) OVER (PARTITION BY member ORDER BY month) AS month_1_back,
           lag(month, 2) OVER (PARTITION BY member ORDER BY month) AS month_2_back
    FROM   monthly
)
SELECT member,
       spend < spend_1_back AND spend_1_back < spend_2_back AS lag_flag,
       spend < spend_1_back AND spend_1_back < spend_2_back
         AND month_1_back = DATE '2026-08-01'
         AND month_2_back = DATE '2026-07-01'               AS calendar_flag
FROM   lagged
WHERE  month = DATE '2026-09-01'
ORDER  BY member;
```

Your run should show the LAG flag keeping both and the calendar flag keeping only Y, since X's
"month before" September was July. X stands in for the member on holiday: a month with no order
is no reading.

If all six steps matched your paper, open notebook 03 and count Retail-Core's top fifty under each
rule again without looking at its output first.

---

## Stretch: can you take the plan line and the tie rule a step past today?

This one is for you if the chapters landed and you finished the take-home.

**Who needs the answer.** Meera Raghavan wants to know when Q2's lead over plan stopped growing,
the head of Retail-Plus wants a report that states its own count and the members at its line, and
Marketing wants to know whether a gap in a member's buying is unusual before it reads one as drift.

**The questions on the way.**

1. Chapter 5: in which weeks did Q2's lead over plan shrink, and when did it peak?
2. Chapter 3: can one query hand the head of a tier their list, its count and the members at the line?
3. Chapter 6: how often does a member's next order come after a gap of a month or more?

### Chapter 5: in which weeks did Q2's lead over plan shrink, and when did it peak?

Start from chapter 5's fixed build, which lets the plan's first week carry 1 to 5 July:

```sql
WITH weekly AS (
    SELECT greatest(date_trunc('week', order_date)::date,
                    (SELECT min(week_start) FROM plan_line)) AS week_start,
           sum(amount)                                      AS booked
    FROM   orders
    WHERE  quarter = 'Q2'
    GROUP  BY 1
),
to_date AS (
    SELECT p.week_start, p.plan_revenue, coalesce(w.booked, 0) AS booked,
           sum(p.plan_revenue)        OVER (ORDER BY p.week_start) AS plan_to_date,
           sum(coalesce(w.booked, 0)) OVER (ORDER BY p.week_start) AS booked_to_date
    FROM   plan_line p
    LEFT   JOIN weekly w USING (week_start)
)
SELECT week_start, booked, booked_to_date - plan_to_date AS lead
FROM   to_date
ORDER  BY week_start;
```

Then add the two columns Meera needs: the lead at the week before, with LAG, and whether this week's
lead is the quarter's peak, with `max(lead) OVER ()`. Writing `lag(...)` around the window that
computes the lead stops with "window function calls cannot be nested", so the lead needs a named
step of its own first.

Your figures should match these: Q2 sits Rs 24,69,050 behind plan after the week of 6 July, and the
lead peaks at Rs 2,16,69,660 at the end of the week of 3 August, stands at Rs 1,57,51,980 at
mid-quarter, the week of 17 August, and closes at Rs 10. It shrinks in 8 of the 12 weeks that have a
week before them, and each of those weeks booked below its plan of Rs 75,69,230, since the lead
moves by exactly the week's booked less its plan. Write the line to Meera: when the lead stopped
growing, and what the run rate has done since.

### Chapter 3: can one query hand the head of a tier their list, its count and the members at the line?

Take eight invented members, with their spend and their Q2 orders, and a top five:

```sql
WITH invented (member, spend, q2_orders) AS (
    VALUES ('N1', 9600, 4), ('N2', 9100, 2), ('N3', 8700, 5), ('N4', 8050, 3),
           ('N5', 7400, 2), ('N6', 7400, 3), ('N7', 6900, 1), ('N8', 6500, 6)
),
ranked AS (
    SELECT member, spend, q2_orders, rank() OVER (ORDER BY spend DESC) AS place
    FROM   invented
)
SELECT member, spend, place
FROM   ranked
WHERE  place <= 5
ORDER  BY place, member;
```

Add two windows to the outer query: `count(*) OVER ()`, the list's count on every row, and
`place = max(place) OVER ()`, which is true for the members at the line. Both run after the outer
WHERE, so they count only the rows it kept. Then write the hard-cap version for five gift boxes
already packed: ROW_NUMBER with more Q2 orders first as the tiebreaker.

Your answer should match this: under RANK the list holds 6, and N5 and N6 stand at the line on
Rs 7,400 each. Under the hard cap, more orders first keeps N6 (3 orders) and leaves N5 (2) off,
where a tiebreak on the member code would keep N5, a reason nobody could defend to N6. The sentence
the head reads names the rule, the count and the two members at the line.

### Chapter 6: how often does a member's next order come after a gap of a month or more?

Chapter 6 found that a member buys in about 2.5 of the six months, so a month with no order is the
usual state. Put a number on it with LEAD, which reads the next row the way LAG reads the one
before. First predict it on the chapter 6 recovery members X and Y: which of their rows have a next
order more than a month later? Then run it on Kalpa's warehouse.

```sql
WITH monthly AS (
    SELECT customer_id, date_trunc('month', order_date)::date AS month, sum(amount) AS spend
    FROM   orders
    GROUP  BY customer_id, date_trunc('month', order_date)
),
ahead AS (
    SELECT customer_id, month,
           lead(month) OVER (PARTITION BY customer_id ORDER BY month) AS next_month
    FROM   monthly
)
SELECT count(*) FILTER (WHERE next_month IS NULL)                              AS last_month_of_member,
       count(*) FILTER (WHERE next_month = (month + INTERVAL '1 month')::date) AS next_calendar_month,
       count(*) FILTER (WHERE next_month > (month + INTERVAL '1 month')::date) AS after_a_gap,
       count(*)                                                               AS member_months
FROM   ahead;
```

Your counts should match these: X's May and July rows each have a next order two months on, and
none of Y's rows do. On the warehouse, the query reads all 752 member-months, the last month of each
of the 301 members who bought has no next row, and your other two counts add to 451. The share of
next orders that come after a gap is yours to find; write one line to Marketing on what it says
about reading a single empty month as drift.
