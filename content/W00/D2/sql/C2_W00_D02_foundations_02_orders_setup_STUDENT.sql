-- Kalpa Retail's orders as a practice table, for Chapter 2 of the Week 0 foundations guide and its
-- mini project, "Meera's question in one statement". Twelve orders across three tiers and two
-- quarters of 2026, one of them with no amount and two of them cancelled; five customers, one of
-- whom never ordered; and the item lines on each order, which the guided exercise joins in its
-- fan-out step. Written by hand for practice: Kalpa Retail is the programme's fictional company and
-- these rows are not its data. Orders 7 to 11 are the five rows of the diagnostic's Q13 table,
-- renumbered so that order numbers run in date order.
--
-- Run it once from the terminal, in a database of its own, from the folder that holds this file:
--     createdb foundations
--     psql -d foundations -f C2_W00_D02_foundations_02_orders_setup_STUDENT.sql
-- Running it again rebuilds the three tables from scratch, so a mistake is never permanent. It
-- refuses to run inside the kalpa warehouse, whose own orders and customers tables it would replace.

BEGIN;

DO $$
BEGIN
    IF current_database() = 'kalpa' THEN
        RAISE EXCEPTION 'This practice file belongs in the foundations database, never in kalpa.';
    END IF;
END $$;

DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id text PRIMARY KEY,
    city        text NOT NULL
);

CREATE TABLE orders (
    order_id    integer PRIMARY KEY,
    customer_id text    NOT NULL REFERENCES customers (customer_id),
    tier        text    NOT NULL,
    quarter     text    NOT NULL,
    order_date  date    NOT NULL,
    amount      integer,
    status      text    NOT NULL
);

CREATE TABLE order_items (
    order_id integer NOT NULL REFERENCES orders (order_id),
    line_no  integer NOT NULL,
    PRIMARY KEY (order_id, line_no)
);

INSERT INTO customers (customer_id, city) VALUES
    ('C1', 'Ahmedabad'),
    ('C2', 'Pune'),
    ('C3', 'Jaipur'),
    ('C4', 'Kochi'),
    ('C5', 'Indore');

INSERT INTO orders (order_id, customer_id, tier, quarter, order_date, amount, status) VALUES
    (1,  'C1', 'Plus',    'Q1', '2026-01-14', 1200, 'paid'),
    (2,  'C4', 'Plus',    'Q1', '2026-01-27', 1349, 'paid'),
    (3,  'C2', 'Basic',   'Q1', '2026-02-05',  725, 'paid'),
    (4,  'C1', 'Plus',    'Q1', '2026-02-19', 1200, 'paid'),
    (5,  'C2', 'Basic',   'Q1', '2026-03-04',  650, 'cancelled'),
    (6,  'C3', 'Student', 'Q1', '2026-03-17',  425, 'paid'),
    (7,  'C1', 'Plus',    'Q2', '2026-04-02', 1200, 'paid'),
    (8,  'C2', 'Basic',   'Q2', '2026-04-03', NULL, 'paid'),
    (9,  'C1', 'Plus',    'Q2', '2026-04-05',  800, 'cancelled'),
    (10, 'C3', 'Student', 'Q2', '2026-04-06',  300, 'paid'),
    (11, 'C2', 'Basic',   'Q2', '2026-04-09',  500, 'paid'),
    (12, 'C4', 'Plus',    'Q2', '2026-05-21', 1349, 'paid');

INSERT INTO order_items (order_id, line_no) VALUES
    (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1),
    (7, 1), (7, 2), (8, 1), (9, 1), (9, 2), (10, 1),
    (11, 1), (12, 1), (12, 2), (12, 3);

COMMIT;

-- The check: this line should print 5, 12, 16, 1 and 2.
SELECT (SELECT COUNT(*) FROM customers)                        AS customers,
       (SELECT COUNT(*) FROM orders)                           AS orders,
       (SELECT COUNT(*) FROM order_items)                      AS item_lines,
       (SELECT COUNT(*) FROM orders WHERE amount IS NULL)      AS missing_amounts,
       (SELECT COUNT(*) FROM orders WHERE status = 'cancelled') AS cancelled;
