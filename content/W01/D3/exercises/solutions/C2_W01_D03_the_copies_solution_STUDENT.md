# Solution: round 2 set, the copies and the identity rule

Answers: 1a 2d 3b 4c 5d 6a 7b

## The idea being tested

A duplicate only exists under an identity rule. Every item asks what makes two rows one order,
which copy of a pair stays, and what the choice does to rupees, and two of them stage the round's
trap, a key that makes every row unique, in a new place.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | a | A load timestamp differs on every row, so a whole-record key never matches; 300 rows against 284 ids says 16 rows repeat an order. | b: nothing is lost, the rows are all present. c: the id count is the check, not the error. d: a blank id would lower the present count, which nobody reported. |
| 2 | d | The ERP's own key is the identity: one order, one id. | a: two real orders on one day would merge. b: the timestamp makes every row unique. c: finds only exact copies and misses a copy that differs in one field. |
| 3 | b | The copy whose amount converts carries the order's value; keeping the first would keep one that cannot be summed. | a: first is not a reason when the first is broken. c: Finance booked one order, not a choice. d: throwing both away loses Rs 1,900 of booked revenue. |
| 4 | c | Both copies are valid and disagree on one field; no rule inside the file can say which date is true, so keep the first extract and log the question. | a: the order happened and is booked. b: one id is one order. d: "later is a correction" is a guess about the pipeline. |
| 5 | d | Convert first so the rule can see which copy validates, then the rule, then rows, then rupees to the books. | a and b: running the rule before converting keeps the first copy even when it is unreadable. c: reconciling rows before the rule has nothing to reconcile. |
| 6 | a | Two rows carry about 97 percent of the rupees, which is Anand's gap. | b: the Retail-Plus rows matter to Tuesday's finding, a second conversation. c: the auditor wants every row, and rupees first. d: counting rows hides where the money sits. |
| 7 | b | The key merges the two real orders, and one is set aside as a copy, so revenue falls by its amount. | a and d: the key is wrong for this business. c: the key removes rows; it never adds one. |

## The part worth arguing about

Item 4. Some pairs will want to keep the later date. The honest answer is that the file cannot tell
you, and a guess written into the clean file becomes a fact nobody checked. Logging the question for
the ERP team is the professional move, and it costs one line.

## Where the pattern lives in production

Every pipeline that adds a load id, a timestamp or a surrogate key to rows makes whole-record
deduplication blind. The fix everywhere is the same: dedupe on the business key, keep one row by a
stated preference, and count rows against distinct keys after every load.
