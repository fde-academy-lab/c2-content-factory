-- Kalpa Retail, Week 2 Wednesday, chapter 1: which fifty members spent the most in Q2?
--
-- Marketing wants to protect Kalpa's best members before their buying drifts: "Give us the top
-- fifty customers by Q2 revenue in each segment." This chapter builds the first and simplest form,
-- one list of fifty across the whole book, and counts who is on it.
--
-- A member is one customer on the customers table, and the segment lives on the customer. Q2 is
-- July to September 2026. Q2 revenue is booked revenue, every order at its amount whatever its
-- status, which is how Monday's suite reached Rs 9,84,00,000 for the quarter.
--
-- Run one block at a time: put the cursor inside a block, select it and run it. Each block opens on
-- the question it answers, and the notebook runs the same blocks by the names on their first lines.

-- name: c1_q2_book
-- The question: what did Q2 book, as Monday's suite counted it?
SELECT count(*)                    AS orders,
       count(DISTINCT customer_id) AS members_who_bought,
       sum(amount)                 AS q2_revenue
FROM   orders
WHERE  quarter = 'Q2';

-- name: c1_segments
-- The question: how many members bought in Q2 in each segment, and what did each segment book?
SELECT c.segment,
       count(DISTINCT o.customer_id) AS members_who_bought,
       count(*)                      AS orders,
       sum(o.amount)                 AS q2_revenue
FROM   orders o
JOIN   customers c USING (customer_id)
WHERE  o.quarter = 'Q2'
GROUP  BY c.segment
ORDER  BY q2_revenue DESC;

-- name: c1_top_orders_hurried
-- The quickest list to write: the fifty biggest Q2 orders, largest first.
SELECT o.order_id, o.customer_id, c.segment, o.amount
FROM   orders o
JOIN   customers c USING (customer_id)
WHERE  o.quarter = 'Q2'
ORDER  BY o.amount DESC, o.order_id
LIMIT  50;

-- name: c1_top_orders_check
-- The question: how many rows, how many different members and how many segments does that list hold?
WITH fifty AS (
    SELECT o.order_id, o.customer_id, c.segment, o.amount
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    ORDER  BY o.amount DESC, o.order_id
    LIMIT  50
)
SELECT count(*)                    AS rows_on_the_list,
       count(DISTINCT customer_id) AS different_members,
       count(DISTINCT segment)     AS segments
FROM   fifty;

-- name: c1_top_orders_repeats
-- The question: which members appear more than once on the list of fifty orders, and how often?
WITH fifty AS (
    SELECT o.customer_id
    FROM   orders o
    WHERE  o.quarter = 'Q2'
    ORDER  BY o.amount DESC, o.order_id
    LIMIT  50
)
SELECT customer_id, count(*) AS times_on_the_list
FROM   fifty
GROUP  BY customer_id
HAVING count(*) > 1
ORDER  BY times_on_the_list DESC, customer_id;

-- name: c1_member_spend
-- The question: what did each member book in Q2? One row per member who bought.
SELECT o.customer_id,
       c.segment,
       count(*)      AS q2_orders,
       sum(o.amount) AS q2_revenue
FROM   orders o
JOIN   customers c USING (customer_id)
WHERE  o.quarter = 'Q2'
GROUP  BY o.customer_id, c.segment
ORDER  BY q2_revenue DESC, o.customer_id;

-- name: c1_top_fifty_groupby
-- Option B: group by member, sort, keep fifty. The order of the rows is the only position.
SELECT o.customer_id,
       c.segment,
       sum(o.amount) AS q2_revenue
FROM   orders o
JOIN   customers c USING (customer_id)
WHERE  o.quarter = 'Q2'
GROUP  BY o.customer_id, c.segment
ORDER  BY q2_revenue DESC, o.customer_id
LIMIT  50;

-- name: c1_top_fifty
-- Option C: group by member in a named step, number every member in a window, keep positions 1 to 50.
-- row_number() OVER (ORDER BY ...) keeps every member's row and adds its place in the order, and the
-- customer id breaks any tie in revenue so the numbering is the same on every run.
WITH q2_spend AS (
    SELECT o.customer_id,
           c.segment,
           count(*)      AS q2_orders,
           sum(o.amount) AS q2_revenue
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY o.customer_id, c.segment
),
ranked AS (
    SELECT customer_id, segment, q2_orders, q2_revenue,
           row_number() OVER (ORDER BY q2_revenue DESC, customer_id) AS position
    FROM   q2_spend
)
SELECT position, customer_id, segment, q2_orders, q2_revenue
FROM   ranked
WHERE  position <= 50
ORDER  BY position;

-- name: c1_list_by_segment
-- The question: how many members of each segment are on the one list of fifty?
-- Every segment is listed, including one with nobody on the list, because the count runs over all
-- members who bought and FILTER keeps the ones in the first fifty.
WITH q2_spend AS (
    SELECT o.customer_id, c.segment, sum(o.amount) AS q2_revenue
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY o.customer_id, c.segment
),
ranked AS (
    SELECT segment,
           row_number() OVER (ORDER BY q2_revenue DESC, customer_id) AS position
    FROM   q2_spend
)
SELECT segment,
       count(*) FILTER (WHERE position <= 50) AS on_the_list,
       count(*)                               AS members_who_bought
FROM   ranked
GROUP  BY segment
ORDER  BY on_the_list DESC, segment;

-- name: c1_where_business_ends
-- The question: where on the one list does Business end and the first retail member appear?
WITH q2_spend AS (
    SELECT o.customer_id, c.segment, sum(o.amount) AS q2_revenue
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY o.customer_id, c.segment
),
ranked AS (
    SELECT customer_id, segment, q2_revenue,
           row_number() OVER (ORDER BY q2_revenue DESC, customer_id) AS position
    FROM   q2_spend
)
SELECT position, customer_id, segment, q2_revenue
FROM   ranked
WHERE  position BETWEEN 33 AND 40
ORDER  BY position;

-- name: c1_rows_for_python
-- The second route's input: every Q2 order row with its member and segment, 462 rows.
SELECT o.customer_id, c.segment, o.amount
FROM   orders o
JOIN   customers c USING (customer_id)
WHERE  o.quarter = 'Q2';
