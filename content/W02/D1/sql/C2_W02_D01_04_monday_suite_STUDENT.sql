-- The Monday suite: six queries Anand's analyst will run every Monday and audit line by line.
--
-- Anand: "I want these numbers every Monday, for every segment and channel, computed from the
-- warehouse itself. No notebooks, no exports, nothing a person can mistype."
--
-- The analyst reads this file without you beside him, so every block opens on one comment line
-- stating the question, the definition of revenue and the denominator. Write each query under its
-- comment. The brief is exercises/unguided/C2_W02_D01_monday_suite_brief_STUDENT.md.
--
-- The rules the analyst audits against:
--   revenue means booked revenue, every status, and the comment says so;
--   a customer is counted once, however many orders they placed;
--   every ratio is computed in numeric and rounded for the reader;
--   every list has an ORDER BY, so two runs return the same rows in the same order;
--   a step that feeds another step is a named CTE.

-- name: suite_1_book
-- 1. What did each quarter book, in orders and rupees, and what did it change by?


-- name: suite_2_customers
-- 2. How many customers bought in each quarter, against the members on the book?


-- name: suite_3_segment_leaves
-- 3. The leaves per segment per quarter: customers, orders per customer, revenue per order, revenue.


-- name: suite_4_typical_order
-- 4. The typical order per segment per quarter: the median beside the mean.


-- name: suite_5_thin_cells
-- 5. Which segment-quarters hold fewer than 30 orders, so their rates carry a warning?


-- name: suite_6_what_moved
-- 6. Which branch moved in each segment from Q1 to Q2, as percentage changes? Two CTEs, one per quarter.

