-- Kalpa Retail, Week 2 Wednesday, chapter 3: when two members spent the same at the line, how many
-- does each segment's list ship, and which rule did the head of Retail-Plus ask for?
--
-- "Ties matter. If two members spent the same, I want them ranked the same, and I want to know how
--  many made the top fifty, not forty-nine because of a tie." The head of Retail-Plus, the owner of
--  Kalpa's paid membership tier.
--
-- Four rules can cut a list at fifty: ROW_NUMBER with a stated tiebreaker, RANK, DENSE_RANK, and
-- "whole ties only", which keeps a tie only when all of it fits. The first two blocks run on invented
-- members, labelled invented, so the mechanism shows on one screen. The rest run on Kalpa.
--
-- Q2 is July to September 2026. Q2 revenue is booked revenue, every order at its amount whatever its
-- status.

-- name: c3_invented_three
-- Invented numbers, for the mechanism only: six members, and A and B spent the same.
WITH invented (member, spend) AS (
    VALUES ('A', 7500), ('B', 7500), ('C', 6000), ('D', 5200), ('E', 5200), ('F', 4100)
)
SELECT member, spend,
       row_number() OVER (ORDER BY spend DESC, member) AS row_number,
       rank()       OVER (ORDER BY spend DESC)         AS rank,
       dense_rank() OVER (ORDER BY spend DESC)         AS dense_rank
FROM   invented
ORDER  BY spend DESC, member;

-- name: c3_invented_line
-- Invented again: a top four, where the fourth and fifth members spent the same.
-- tied_with counts the members who share a row's spend, so rank + tied_with - 1 is the last place
-- the tie reaches, and "whole ties only" keeps a tie only when that last place is inside the line.
WITH invented (member, spend) AS (
    VALUES ('A', 9100), ('B', 8800), ('C', 8200), ('D', 7400), ('E', 7400), ('F', 6900)
),
r AS (
    SELECT member, spend,
           row_number() OVER (ORDER BY spend DESC, member) AS rn,
           rank()       OVER (ORDER BY spend DESC)         AS rk,
           dense_rank() OVER (ORDER BY spend DESC)         AS dr,
           count(*)     OVER (PARTITION BY spend)          AS tied_with
    FROM   invented
)
SELECT count(*) FILTER (WHERE rn <= 4)                 AS row_number_ships,
       count(*) FILTER (WHERE rk <= 4)                 AS rank_ships,
       count(*) FILTER (WHERE dr <= 4)                 AS dense_rank_ships,
       count(*) FILTER (WHERE rk + tied_with - 1 <= 4) AS whole_ties_only_ships
FROM   r;

-- name: c3_core_counts
-- The question: how many Retail-Core members does each rule put on a top-fifty list?
WITH q2 AS (
    SELECT c.segment, o.customer_id, sum(o.amount) AS q2_revenue
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY c.segment, o.customer_id
),
r AS (
    SELECT segment, customer_id, q2_revenue,
           row_number() OVER (PARTITION BY segment ORDER BY q2_revenue DESC, customer_id) AS rn,
           rank()       OVER (PARTITION BY segment ORDER BY q2_revenue DESC)              AS rk,
           dense_rank() OVER (PARTITION BY segment ORDER BY q2_revenue DESC)              AS dr,
           count(*)     OVER (PARTITION BY segment, q2_revenue)                           AS tied_with
    FROM   q2
)
SELECT segment,
       count(*) FILTER (WHERE rn <= 50)                 AS row_number_ships,
       count(*) FILTER (WHERE rk <= 50)                 AS rank_ships,
       count(*) FILTER (WHERE dr <= 50)                 AS dense_rank_ships,
       count(*) FILTER (WHERE rk + tied_with - 1 <= 50) AS whole_ties_only_ships
FROM   r
WHERE  segment = 'Retail-Core'
GROUP  BY segment;

-- name: c3_core_line
-- The question: what do the three functions say about Retail-Core's members around fiftieth place?
WITH q2 AS (
    SELECT c.segment, o.customer_id, sum(o.amount) AS q2_revenue
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY c.segment, o.customer_id
),
r AS (
    SELECT segment, customer_id, q2_revenue,
           row_number() OVER (PARTITION BY segment ORDER BY q2_revenue DESC, customer_id) AS row_number,
           rank()       OVER (PARTITION BY segment ORDER BY q2_revenue DESC)              AS rank,
           dense_rank() OVER (PARTITION BY segment ORDER BY q2_revenue DESC)              AS dense_rank
    FROM   q2
)
SELECT row_number, rank, dense_rank, customer_id, q2_revenue
FROM   r
WHERE  segment = 'Retail-Core' AND row_number BETWEEN 46 AND 54
ORDER  BY row_number;

-- name: c3_core_ties
-- The question: where inside Retail-Core's first fifty do two members share one Q2 revenue figure?
WITH q2 AS (
    SELECT c.segment, o.customer_id, sum(o.amount) AS q2_revenue
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY c.segment, o.customer_id
),
r AS (
    SELECT segment, customer_id, q2_revenue,
           row_number() OVER (PARTITION BY segment ORDER BY q2_revenue DESC, customer_id) AS row_number,
           count(*)     OVER (PARTITION BY segment, q2_revenue)                           AS tied_with
    FROM   q2
)
SELECT row_number, customer_id, q2_revenue, tied_with
FROM   r
WHERE  segment = 'Retail-Core' AND tied_with > 1 AND row_number <= 50
ORDER  BY row_number;

-- name: c3_all_counts
-- The same four counts for every segment, for the checks. Your own segment's line is yours to read.
WITH q2 AS (
    SELECT c.segment, o.customer_id, sum(o.amount) AS q2_revenue
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY c.segment, o.customer_id
),
r AS (
    SELECT segment, customer_id, q2_revenue,
           row_number() OVER (PARTITION BY segment ORDER BY q2_revenue DESC, customer_id) AS rn,
           rank()       OVER (PARTITION BY segment ORDER BY q2_revenue DESC)              AS rk,
           dense_rank() OVER (PARTITION BY segment ORDER BY q2_revenue DESC)              AS dr,
           count(*)     OVER (PARTITION BY segment, q2_revenue)                           AS tied_with
    FROM   q2
)
SELECT segment,
       count(*) FILTER (WHERE rn <= 50)                 AS row_number_ships,
       count(*) FILTER (WHERE rk <= 50)                 AS rank_ships,
       count(*) FILTER (WHERE dr <= 50)                 AS dense_rank_ships,
       count(*) FILTER (WHERE rk + tied_with - 1 <= 50) AS whole_ties_only_ships
FROM   r
GROUP  BY segment
ORDER  BY segment;

-- name: c3_second_route
-- The second route, with no window: find the fiftieth member's Q2 revenue with a sort and OFFSET,
-- then count every member of the segment who spent at least that much.
WITH q2 AS (
    SELECT c.segment, o.customer_id, sum(o.amount) AS q2_revenue
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY c.segment, o.customer_id
)
SELECT s.segment,
       (SELECT count(*)
        FROM   q2
        WHERE  q2.segment = s.segment
          AND  q2.q2_revenue >= coalesce(
                   (SELECT q.q2_revenue FROM q2 q WHERE q.segment = s.segment
                    ORDER BY q.q2_revenue DESC OFFSET 49 LIMIT 1), 0)) AS at_or_above_fiftieth
FROM   (SELECT DISTINCT segment FROM q2) s
ORDER  BY s.segment;

-- name: c3_your_segment
-- Your turn: the four counts for one segment. Change the segment's name on the last line.
WITH q2 AS (
    SELECT c.segment, o.customer_id, sum(o.amount) AS q2_revenue
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY c.segment, o.customer_id
),
r AS (
    SELECT segment, customer_id, q2_revenue,
           row_number() OVER (PARTITION BY segment ORDER BY q2_revenue DESC, customer_id) AS rn,
           rank()       OVER (PARTITION BY segment ORDER BY q2_revenue DESC)              AS rk,
           dense_rank() OVER (PARTITION BY segment ORDER BY q2_revenue DESC)              AS dr,
           count(*)     OVER (PARTITION BY segment, q2_revenue)                           AS tied_with
    FROM   q2
)
SELECT count(*) FILTER (WHERE rn <= 50)                 AS row_number_ships,
       count(*) FILTER (WHERE rk <= 50)                 AS rank_ships,
       count(*) FILTER (WHERE dr <= 50)                 AS dense_rank_ships,
       count(*) FILTER (WHERE rk + tied_with - 1 <= 50) AS whole_ties_only_ships
FROM   r
WHERE  segment = 'Retail-Plus';
