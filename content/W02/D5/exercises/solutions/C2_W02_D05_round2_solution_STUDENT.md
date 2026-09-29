# Solution: round 2, the protect list and the lookup

Answers: 1b 2c 3a 4c 5d 6a 7b

## The idea being tested

A lookup that cannot find an id must say so. `VLOOKUP` with its fourth argument left out, and
`MATCH` with 1, return the largest id not above the one asked for on a sorted table, so a missing
id comes back as a neighbour's row with no warning (Microsoft Support, VLOOKUP, verified 29 September
2026). The foot of a list a director filters has the same shape of failure: `SUM` keeps adding the
rows the filter hid.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | b | C-0195 is not in the table, so an approximate match returned C-0194's row, Rs 16,740 at rank 15. | a, c and d describe real mistakes that would not produce another member's exact row. |
| 2 | c | An exact `MATCH` returns #N/A for a missing id and `IFERROR` turns that into the words. | a and b are approximate matches that return a neighbour. d wraps an approximate match, so it never errors and never prints the words. |
| 3 | a | XLOOKUP's fourth argument is `if_not_found`, and its match mode is exact by default (Microsoft Support, XLOOKUP, verified 29 September 2026). | b returns #N/A, which says missing but not in words. c returns the next smaller item, the neighbour. d puts the text in the search-mode position, which is not an if-not-found argument. |
| 4 | c | `SUM` adds every row in its range; the filter hid 39 of them from the eye only. The eleven on screen spent Rs 1,56,790. | a is what SUBTOTAL(109) shows. b and d describe filters nobody applied. |
| 5 | d | SUBTOTAL(109) leaves out rows hidden by a filter and by hand (Microsoft Support, SUBTOTAL, verified 29 September 2026). | a adds everything. b leaves out filtered rows and keeps rows hidden by hand. c hard-codes one city, so it stops following the filter the moment somebody changes it. |
| 6 | a | Ties matter only across the boundary; Rs 8,580 and Rs 8,520 differ, so the list ships exactly fifty. | b and d invent a tie that is not there. c treats Wednesday's tie as a rule rather than a property of the data. |
| 7 | b | The lookup's dangerous exit is the missing id; testing a present id proves nothing about it. | a, c and d test cases where an approximate match also returns the right row, so the defect survives the test. |

## Where this appears in production

Every CRM and finance sheet with a lookup by customer id meets missing ids: churned customers,
new ones not yet in the export, typos. Teams that ship lookups test them against a known-missing id
as part of review, and a finance team treats an approximate match on an id column as a defect.
