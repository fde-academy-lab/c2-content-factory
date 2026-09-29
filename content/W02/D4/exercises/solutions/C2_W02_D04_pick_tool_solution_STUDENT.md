# Solution: pick the tool for five asks

Answers: 1b 2c 3a 4c 5b

## The idea being tested

All three tools give the same number, so the choice is about who has to trust it: Finance and
auditors rerun and audit, so the number lives where the data lives; an analyst iterates, so the
work sits on the bench; a reader who must follow every step gets the loop.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | b | A view in the warehouse is rerun at the source by anyone, and gives Anand's analyst the same number every time. | a and c run off a copy on one laptop. d: a workbook can present the number on Friday, and must never be where it is computed. |
| 2 | c | Five cuts in an afternoon is iteration, and pandas on the customer table makes each cut one line and a chart. | a is slow to change for each cut. b turns a question into five warehouse objects. d works from last week's export, which is already out of date. |
| 3 | a | The new joiner wants to check by hand, and a loop over ten orders with the totals printed is exactly that. | b and c are correct and compress every step into one statement, which is what the joiner cannot yet read. d hides the arithmetic inside a pivot. |
| 4 | c | A one-off file, today, matched to the table with the fan-out guarded: that is the analyst's bench. | a rebuilds a merge by hand. b is right if the feed becomes a weekly source, and too slow for lunch today. d looks up into a stale copy and returns silently on a missing id. |
| 5 | b | An auditor reruns a statement against the same source and expects the same count. | a and c run off copies. d is a pasted number with no trail back to the source. |

## The part worth arguing about

Item 4, option b. If the platform will send this file every week, the right long-term home is a
warehouse table the platform lead owns, and the note should say so. For today's question, the
bench wins, and the note says which one you chose and why.
