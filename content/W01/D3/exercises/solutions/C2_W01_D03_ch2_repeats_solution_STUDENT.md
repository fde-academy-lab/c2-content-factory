# Solution: chapter 2 set: the rows that repeat

Answers: 1b 2c 3a 4d 5c 6d

4 of 6 items are design items.

## Item by item

| Item | Key | Kind | Why it holds | Why the others fail |
|---|---|---|---|---|
| 1 | b | read | A load timestamp differs on every row, so a whole-record key never matches; 300 rows against 284 ids says 16 rows repeat an order. | a: nothing is lost, the rows are all present. c: the id count is the check. d: a blank id would lower the present count, which nobody reported. |
| 2 | c | design | The ERP's own key is the identity: one order, one id. | a: two real orders on one day would merge. b: the timestamp makes every row unique. d: finds only exact copies and misses a copy that differs in one field. |
| 3 | a | read | The key merges the two real orders, and one is set aside as a copy, so revenue falls by its amount. | b and d: the key is wrong for this business. c: a dedupe removes rows and never adds one. |
| 4 | d | design | Rows less distinct order ids: 150 minus 141 is 9. Convertible amounts are a separate count. | a: 150 less 148 is the failed amounts. b: 9 less 2 mixes the two counts. c: 9 plus 2 adds them. |
| 5 | c | design | Neither id identifies a person across both systems, so the match rests on contact fields cleaned the same way, with a person reviewing the doubtful pairs. | a: C-1 in the app and C-1 in a store are different people. b: two systems never write a person identically. d: names repeat and are spelled many ways. |
| 6 | d | design | 10,000 times 9,999 over 2 is 49,995,000, about 5 crore, which is why fuzzy matching is blocked by a field such as city first. | a: that is one lookup per row, a key's cost. b: far too few pairs. c: 100 crore is ten times every row against every row, not half of it. |
