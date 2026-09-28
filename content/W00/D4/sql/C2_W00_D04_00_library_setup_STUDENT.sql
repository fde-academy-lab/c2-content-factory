-- The college library's issue log, four weeks of it, as one Postgres table.
-- Week 1 is Wednesday's class log and week 2 is the following week's log, row for row;
-- weeks 3 and 4 are new. Practice data for the Week 0 SQL brush-up, written by hand.
--
-- Run it once from the terminal, inside the library database:
--     psql -d library -f C2_W00_D04_00_library_setup_STUDENT.sql
-- Running it again rebuilds the table from scratch, so a mistake is never permanent.

DROP TABLE IF EXISTS issues;

CREATE TABLE issues (
    issue_id  integer PRIMARY KEY,
    week      integer NOT NULL,
    student   text    NOT NULL,
    book      text    NOT NULL,
    dept      text    NOT NULL,
    days_kept integer NOT NULL
);

INSERT INTO issues (issue_id, week, student, book, dept, days_kept) VALUES
    (1,  1, 'S01', 'Algebra',   'Maths',    12),
    (2,  1, 'S02', 'Poetry',    'Arts',      5),
    (3,  1, 'S01', 'Calculus',  'Maths',    20),
    (4,  1, 'S03', 'Poetry',    'Arts',      9),
    (5,  1, 'S04', 'Physics',   'Science',  14),
    (6,  1, 'S02', 'Algebra',   'Maths',     3),
    (7,  1, 'S05', 'Chemistry', 'Science',  21),
    (8,  1, 'S03', 'Calculus',  'Maths',     7),
    (9,  2, 'S02', 'Physics',   'Science',  16),
    (10, 2, 'S06', 'Poetry',    'Arts',      4),
    (11, 2, 'S01', 'Algebra',   'Maths',    15),
    (12, 2, 'S07', 'History',   'Arts',     22),
    (13, 2, 'S03', 'Chemistry', 'Science',   9),
    (14, 2, 'S06', 'Algebra',   'Maths',    14),
    (15, 2, 'S04', 'History',   'Arts',     11),
    (16, 2, 'S08', 'Calculus',  'Maths',     6),
    (17, 2, 'S02', 'Chemistry', 'Science',  19),
    (18, 2, 'S07', 'Poetry',    'Arts',      8),
    (19, 3, 'S09', 'Economics', 'Commerce', 10),
    (20, 3, 'S01', 'Calculus',  'Maths',    13),
    (21, 3, 'S05', 'Physics',   'Science',  17),
    (22, 3, 'S10', 'Accounts',  'Commerce',  6),
    (23, 3, 'S03', 'Poetry',    'Arts',     12),
    (24, 3, 'S08', 'Algebra',   'Maths',    18),
    (25, 3, 'S02', 'Chemistry', 'Science',   8),
    (26, 3, 'S06', 'History',   'Arts',     15),
    (27, 3, 'S09', 'Accounts',  'Commerce', 11),
    (28, 3, 'S04', 'Physics',   'Science',   5),
    (29, 4, 'S07', 'Poetry',    'Arts',      7),
    (30, 4, 'S01', 'Algebra',   'Maths',     9),
    (31, 4, 'S10', 'Economics', 'Commerce', 23),
    (32, 4, 'S05', 'Chemistry', 'Science',  12),
    (33, 4, 'S03', 'History',   'Arts',     16),
    (34, 4, 'S02', 'Calculus',  'Maths',     4),
    (35, 4, 'S08', 'Physics',   'Science',  14),
    (36, 4, 'S06', 'Poetry',    'Arts',     10),
    (37, 4, 'S04', 'Algebra',   'Maths',    19),
    (38, 4, 'S09', 'Economics', 'Commerce',  8);

-- The check: this line should print 38.
SELECT COUNT(*) AS rows_loaded FROM issues;
