# Day 3 solution, E2. Which dataset would you trust

### The answers

1. **A.** B is A after somebody replaced every failure with a stated default of zero.

2. What the colleague did to move each count:

| Count | How it moved |
|---|---|
| `amount` present, 48 to 50 | The two empty amounts were filled with a value |
| `amount` converts, 44 to 50 | The four unreadable amounts became a number |
| `discount` present, 11 to 50 | Thirty nine orders that had no discount were given one |

3. A cleaning step reduces `distinct` when it maps several different input values onto one output value. Five different broken amounts all became `0`, so five distinct values became one.

4. Something close to: "Nothing fails to convert because you replaced everything that failed, so the count you are quoting is a count of your own edits."

5. `distinct` on its own. It is the only one of the three counts that can fall, so it is the only one that can carry bad news. On B alone you would notice that `amount` holds fewer distinct values than a fifty row order book plausibly should, and that `discount` holds nine distinct values across fifty complete entries.

### The part worth arguing about

B is not the work of a careless person. Every move in B is one a reasonable engineer makes under time pressure, and each one individually is defensible if it is written down. What makes B indefensible is that none of it was.

### Where this lives in production

HGNC, 2020. About 27 human genes were formally renamed because spreadsheets silently coerced names like SEPT1 into dates, after a 2016 audit found gene-name errors in roughly a fifth of genetics papers with spreadsheet supplements. No individual coercion was malicious. The damage was that they were invisible.
