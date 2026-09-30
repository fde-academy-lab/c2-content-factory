# Solution: practice lab, two more files and two printouts

Answers: 1b 2c 3b 4c 5a 6a 7d 8b 9d 10a 11b

## The idea being tested

The day's pass, run on files nobody demonstrated: a profile read as evidence, a second source read
for what it can witness, and a reconciliation in rows and rupees against a clean file you built
yourself.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | b | B counts its failures and logs them; A turned four failures into Rs 0 orders. | a: a perfect convertible count beside four zeros is the coercion trap. c: agreeing rows and ids say nothing about amounts. d: copies are a reason to reconcile, never a reason to reject a printout. |
| 2 | c | 320 rows less 305 distinct ids is 15. | a: the failed amounts. b: 15 less 4 mixes two counts. d: 15 plus 4 adds them. |
| 3 | b | Adding zeros changes no total, so A looks identical in rupees while hiding four orders. | a: equal totals are the disguise. c: a failed amount can carry any value, and nobody has read these four. d: nothing in either printout places them in a quarter. |
| 4 | c | A line that is not an order is read as one row, and its amount does not convert. | a and d: the profile counts every line after the first. b: one amount is text that is no number. |
| 5 | a | Read the rows that fail before deciding anything; the failed amount and the extra segment value come from the same line. | b: a branch for a value nobody sold to is invented. c: the field is fine on every other row. d: read first, then ask. |
| 6 | a | The rows that convert total Rs 81,890. | b, c and d: digits moved or dropped, the slips a hand copy makes. |
| 7 | d | 119 records are complete, and each carries the same amount text as its CSV row. | a and c: the last record is cut. b: nothing differs among the complete ones. |
| 8 | b | The feed was cut from the same extract, so it witnesses what the extract held, never whether a value is right: a flaw in the extract appears in both files. | a: both files can carry the same wrong value. c: agreement on amounts says nothing about repeated ids. d: the complete records are real evidence of what was exported. |
| 9 | d | 40 rows in, 39 orders kept, 1 line set aside. | a: miscounts the rows read. b and c: the other 39 are distinct orders. |
| 10 | a | Rupees reconcile when the same orders carry the same total. | b: the copy holds only the orders it holds, a slice of the quarter. c and d: a tolerance hides the gap an analyst ties out to. |
| 11 | b | A witness that agrees to the rupee confirms what it holds and nothing more, which is worth one line in the note. | a: a slice of the export cannot replace the whole of it. c: it covers only the rows it holds. d: a small witness still confirms. |

## The part worth arguing about

Problem 3, item 8. Two sources that agree feel like proof. They are proof of a common origin, and a
defect in that origin sits in both, which is why the reconciliation to the books is the test and the
feed only witnesses what the extract held.

## Where the pattern lives in production

Every data team keeps a second source for its most important numbers: a gateway report against the
orders table, a ledger extract against the warehouse. Reading it for what it can witness, and never
as a replacement, is what stops two copies of one mistake from looking like confirmation.
