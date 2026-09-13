-- The booked-against-collected report. Anand signs off on this, so you sign off on it first.
--
-- Four deliverables and one comment block. Fill in each. Nothing here needs a join you have not
-- already written today.

-- ---------------------------------------------------------------- the reconciliation
-- Fill this in with real numbers before you write a single total below it. If you cannot write
-- the "Therefore" line, you do not yet know what your join did.
--
-- Rows before: ____ orders.
-- Rows after:  ____.
-- Difference:  ____ orders carry more than one payment row, of which ____ are instalment
--              plans and ____ are gateway retries. ____ orders carry none.
-- Therefore:   ____

-- ---------------------------------------------------------------- 1. the report
-- The question: booked against collected for Q2, by channel, with the gap named.
-- Denominator: every Q2 order, paid or not. State that in your comment.
-- __TODO1__


-- ---------------------------------------------------------------- 2. the unpaid list
-- The question: which delivered orders have no payment at all?
-- Anand asked for these by order id, so give him order id, channel, status and amount.
-- __TODO2__


-- ---------------------------------------------------------------- 3. the double-paid list
-- The question: which orders were charged twice by a gateway retry?
-- A retry repeats the same amount. An instalment plan splits an invoice into different amounts.
-- Your query must separate the two, because deleting both would delete 400 legitimate rows.
-- __TODO3__


-- ---------------------------------------------------------------- 4. the orphans
-- The question: are there payments whose order is not in the book at all?
-- This one is not Anand's problem to fix, and it is still yours to report.
-- __TODO4__
