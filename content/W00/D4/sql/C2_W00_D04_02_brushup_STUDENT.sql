-- The SQL brush-up on all four weeks of the library's log. Run it a block at a time: select the
-- lines of one query in VS Code and paste them into psql, or run the whole file with
--     psql -d library -f C2_W00_D04_02_brushup_STUDENT.sql
-- Each comment says what the query answers and what to expect.

-- A. Rows and columns. Which Science books came back late, longest first?
--    Expect issues 7, 17, 21 and 9, kept 21, 19, 17 and 16 days.
SELECT issue_id, student, book, days_kept
FROM issues
WHERE dept = 'Science'
  AND days_kept > 14
ORDER BY days_kept DESC;

-- B. A list of values. Every Commerce book is Economics or Accounts.
--    Expect 5 rows.
SELECT issue_id, week, book, days_kept
FROM issues
WHERE book IN ('Economics', 'Accounts')
ORDER BY issue_id;

-- C. A range, both ends included. Books kept between 10 and 14 days.
--    Expect 11.
SELECT COUNT(*) AS kept_10_to_14
FROM issues
WHERE days_kept BETWEEN 10 AND 14;

-- D. Sorting on more than one column: department first, then the longest keep inside each, then
--    the issue number, which settles the two Science books kept exactly 14 days.
--    Expect Arts first, with issue 12 at 22 days at the top of Arts.
SELECT dept, issue_id, days_kept
FROM issues
ORDER BY dept, days_kept DESC, issue_id;

-- E. Five aggregates over the whole table, one row back.
--    Expect 38 issues, 452 days, a shortest keep of 3, a longest of 23 and an average of 11.9.
SELECT COUNT(*)                AS issues,
       SUM(days_kept)          AS total_days,
       MIN(days_kept)          AS shortest,
       MAX(days_kept)          AS longest,
       ROUND(AVG(days_kept), 1) AS average_days
FROM issues;

-- F. One row per department.
--    Expect Maths 12, Arts 11, Science 10, Commerce 5.
SELECT dept, COUNT(*) AS issues, ROUND(AVG(days_kept), 1) AS average_days
FROM issues
GROUP BY dept
ORDER BY issues DESC;

-- G. One row per department per week, where Commerce appears only from week 3.
--    Expect 14 rows.
SELECT dept, week, COUNT(*) AS issues
FROM issues
GROUP BY dept, week
ORDER BY dept, week;

-- H. Groups filtered by HAVING: students with at least five issues.
--    Expect S02 6, S01 5, S03 5.
SELECT student, COUNT(*) AS issues
FROM issues
GROUP BY student
HAVING COUNT(*) >= 5
ORDER BY issues DESC, student;

-- I. WHERE on rows, then HAVING on groups: departments with more than 10 late days.
--    Expect Science 17, Maths 16, Arts 11.
SELECT dept, SUM(days_kept - 14) AS late_days
FROM issues
WHERE days_kept > 14
GROUP BY dept
HAVING SUM(days_kept - 14) > 10
ORDER BY late_days DESC;
