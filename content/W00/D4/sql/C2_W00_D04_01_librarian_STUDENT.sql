-- The librarian's three questions, answered in SQL for week 1, the same eight issues Wednesday's
-- Python answered. Each query's comment gives the Python it replaces and the answer to expect.
--
-- Run the whole file from the terminal:
--     psql -d library -f C2_W00_D04_01_librarian_STUDENT.sql

-- 1. How many issues did we have?
--    Python: a running count, started at 0 and raised by 1 per record.
--    Expect 8.
SELECT COUNT(*) AS issues
FROM issues
WHERE week = 1;

-- 2. Which department borrows most?
--    Python: a dictionary of counts, one key per department, then the largest.
--    Expect Maths 4, then Arts 2 and Science 2.
SELECT dept, COUNT(*) AS issues
FROM issues
WHERE week = 1
GROUP BY dept
ORDER BY issues DESC, dept;

-- 3. How many days late did books come back? The loan is 14 days.
--    Python: a running total of days_kept - 14 over the records kept longer than 14 days.
--    Expect 13.
SELECT SUM(days_kept - 14) AS late_days
FROM issues
WHERE week = 1
  AND days_kept > 14;

-- 4. Whose books spend the most days out? Wednesday changed one line of the counting loop.
--    Expect Maths 42, Science 35, Arts 14.
SELECT dept, SUM(days_kept) AS days_out
FROM issues
WHERE week = 1
GROUP BY dept
ORDER BY days_out DESC;

-- 5. The same numbers every week: GROUP BY week answers all four weeks in one query.
--    Expect 8, 10, 10 and 10 issues.
SELECT week, COUNT(*) AS issues
FROM issues
GROUP BY week
ORDER BY week;

--    Expect 13, 16, 8 and 16 late days.
SELECT week, SUM(days_kept - 14) AS late_days
FROM issues
WHERE days_kept > 14
GROUP BY week
ORDER BY week;
