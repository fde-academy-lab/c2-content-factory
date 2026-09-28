-- The hostel mess register as one Postgres table: four weeks of dinners, one row per night.
-- The same numbers as the weekend project's Python data file. Invented practice data, written by
-- hand; it belongs to no client.
--
-- Run it once from the terminal, in the library database you made on Thursday:
--     psql -d library -f C2_W00_D04_03_mess_setup_STUDENT.sql

DROP TABLE IF EXISTS dinners;

CREATE TABLE dinners (
    day     integer PRIMARY KEY,
    week    integer NOT NULL,
    weekday text    NOT NULL,
    cooked  integer NOT NULL,
    eaten   integer NOT NULL
);

INSERT INTO dinners (day, week, weekday, cooked, eaten) VALUES
    (1,  1, 'Mon', 240, 206),
    (2,  1, 'Tue', 240, 211),
    (3,  1, 'Wed', 240, 207),
    (4,  1, 'Thu', 240, 199),
    (5,  1, 'Fri', 240, 176),
    (6,  1, 'Sat', 240, 149),
    (7,  1, 'Sun', 240, 158),
    (8,  2, 'Mon', 240, 203),
    (9,  2, 'Tue', 240, 209),
    (10, 2, 'Wed', 240, 210),
    (11, 2, 'Thu', 240, 202),
    (12, 2, 'Fri', 240, 172),
    (13, 2, 'Sat', 240, 153),
    (14, 2, 'Sun', 240, 162),
    (15, 3, 'Mon', 240, 208),
    (16, 3, 'Tue', 240, 212),
    (17, 3, 'Wed', 240, 205),
    (18, 3, 'Thu', 240, 198),
    (19, 3, 'Fri', 240, 178),
    (20, 3, 'Sat', 240, 147),
    (21, 3, 'Sun', 240, 157),
    (22, 4, 'Mon', 240, 204),
    (23, 4, 'Tue', 240, 208),
    (24, 4, 'Wed', 240, 209),
    (25, 4, 'Thu', 240, 201),
    (26, 4, 'Fri', 240, 174),
    (27, 4, 'Sat', 240, 151),
    (28, 4, 'Sun', 240, 161);

-- The check: this line should print 28, 6720 and 5230.
SELECT COUNT(*) AS nights, SUM(cooked) AS cooked, SUM(eaten) AS eaten FROM dinners;
