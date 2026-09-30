# Solution: chapter 2 set: the rows that repeat

Answers: 1a 2c 3b 4d

2 of 4 items are design items.

## Item by item

| Item | Key | Kind | Why it holds | Why the others fail |
|---|---|---|---|---|
| 1 | a | read | A load stamp differs on every row, so a whole-record key never matches; 300 rows against 284 ids says 16 rows repeat an order. | b: all 300 rows are present, so nothing was lost. c: the id count is the check, and it disagrees with the dedupe. d: blank ids would show in the profile as order_id present on fewer than 300 rows, and the dedupe would still match nothing. |
| 2 | c | design | Neither id names one person across both systems, so the match rests on contact fields cleaned the same way. Every record against every other is 60,000 x 59,999 / 2, about 180 crore pairs, 360 minutes at 50 lakh a minute; within 6 cities of 10,000 it is about 30 crore pairs, 60 minutes, inside the window, with doubtful pairs sent to a person. | a: C-1 in the app and C-1 in a store are different people. b: the right fields, and 6 hours, three times the window. d: two systems rarely write one person's record identically, so real matches are missed. |
| 3 | b | read | Two keys can flag the same number of rows and share fewer than all of them; only the rows themselves show which real orders one key removed and which copies it missed. | a: counts by quarter can match while the rows differ. c: a narrower window changes the count and never tests whether the rows are the same. d: says nothing about which rows either key flagged. |
| 4 | d | design | The fuzzy match removes 4 real orders, Rs 10,00,000, and keeps 2 copies the id key removes, Rs 6,000, so its revenue sits Rs 10,00,000 less Rs 6,000 below: Rs 9,94,000. | a: counts the kept copies as a second loss, when they add rupees. b: counts only the copies and forgets the four real orders. c: forgets the two copies it keeps. |
