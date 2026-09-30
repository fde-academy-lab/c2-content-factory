-- Kalpa Retail, Week 2, Wednesday. Round 2: when two members tie.
--
-- "Ties matter. If two members spent the same, I want them ranked the same, and I want to know
--  how many made the top fifty, not forty-nine because of a tie." The head of Retail-Plus.
--
-- Three ranking functions, one tie, and a count of rows that each rule ships. The first block runs
-- on six invented members so the mechanism is visible on one screen; the rest runs on Kalpa.

-- ---------------------------------------------------------------- 1. three functions, one tie
-- Invented numbers, for the mechanism only. Two members spent Rs 7,500 each and lead the list.
WITH invented (member, spend) AS (
    VALUES ('A', 7500), ('B', 7500), ('C', 6000), ('D', 5200), ('E', 5200), ('F', 4100)
)
SELECT member, spend,
       row_number() OVER (ORDER BY spend DESC, member) AS row_number,
       rank()       OVER (ORDER BY spend DESC)         AS rank,
       dense_rank() OVER (ORDER BY spend DESC)         AS dense_rank
FROM   invented
ORDER  BY spend DESC, member;

-- ---------------------------------------------------------------- 2. the tie at the line
-- Invented again. Marketing wants a top four, and the fourth and fifth members tied.
-- Count the rows each rule ships.
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
SELECT count(*) FILTER (WHERE rn <= 4)                  AS row_number_ships,
       count(*) FILTER (WHERE rk <= 4)                  AS rank_ships,
       count(*) FILTER (WHERE dr <= 4)                  AS dense_rank_ships,
       count(*) FILTER (WHERE rk + tied_with - 1 <= 4)  AS whole_ties_only_ships
FROM   r;

-- ---------------------------------------------------------------- 3. the same count on Kalpa
-- The question: how many Retail-Core members does each rule put on a top-fifty list?
-- Read the dense_rank column twice. It sounds like "ties rank the same"; count what it ships.
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
       count(*) FILTER (WHERE rn <= 50)                  AS row_number_ships,
       count(*) FILTER (WHERE rk <= 50)                  AS rank_ships,
       count(*) FILTER (WHERE dr <= 50)                  AS dense_rank_ships,
       count(*) FILTER (WHERE rk + tied_with - 1 <= 50)  AS whole_ties_only_ships
FROM   r
WHERE  segment = 'Retail-Core'          -- your turn: run it again for 'Retail-Plus'
GROUP  BY segment;

-- ---------------------------------------------------------------- 4. read the boundary
-- The question: who sits either side of position fifty, and why do the counts differ?
-- Change the segment to 'Retail-Plus' when you run it yourself.
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
           dense_rank() OVER (PARTITION BY segment ORDER BY q2_revenue DESC)              AS dr
    FROM   q2
)
SELECT rn, rk, dr, customer_id, q2_revenue
FROM   r
WHERE  segment = 'Retail-Core' AND rn BETWEEN 44 AND 54
ORDER  BY rn;

-- ---------------------------------------------------------------- 5. the rule, written down
-- The head of Retail-Plus asked for tied members to rank the same and for the count to be said
-- out loud. RANK does both: tied members share a position, and everyone at or above fifty ships.
-- The report states how many shipped and why, in the same line.
WITH q2 AS (
    SELECT c.segment, o.customer_id, sum(o.amount) AS q2_revenue
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY c.segment, o.customer_id
),
ranked AS (
    SELECT segment, customer_id, q2_revenue,
           rank() OVER (PARTITION BY segment ORDER BY q2_revenue DESC) AS position
    FROM   q2
)
SELECT segment,
       count(*)      AS members_on_the_list,
       max(position) AS last_position,
       count(*) - least(50, count(*)) AS extra_rows_from_a_tie_at_the_line
FROM   ranked
WHERE  position <= 50
GROUP  BY segment
ORDER  BY segment;
