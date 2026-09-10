# Day 3 solution, E2. Which dataset would you trust

## The idea being tested

Two profiles of the same fifty orders, and every count that a careless reader looks at moved in the direction that reads as progress. Present rose. Converts rose. Only distinct fell, and distinct is the one count nobody quotes.

The whole exercise turns on that asymmetry. A cleaning pass that never fails produces a file that looks finished and has forgotten what it was sent, and the only trace it leaves is a number going down in a column most people skim past.

## The answers

**Answers: 1a 2b 3c 4d 5a 6b 7c 8d 9a 10b 11c 12d 13a 14b 15c**

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | a | Distinct on amount falls from 46 to 41, because six rows now share a value none of them held. | Present and converts both rise, which is what makes B look better. Distinct on order_id is 49 in both, since nothing in that column was ever replaced. |
| 2 | b | Five different raw values, across six rows, collapsed into a single zero. | Nothing was deleted; the row count is 50 in both. Sorting changes no count at all. No column was dropped, since all seven are still profiled. |
| 3 | c | Present 48 minus converts 44 is four values that look filled in and are not. | Two counts the empty cells, which are absent rather than unusable. Six is the number of rows the pass rejects, which is a different question. 44 is the usable count. |
| 4 | d | Two rows have no amount at all, and they are rejected alongside the four unusable ones, which makes six. | Saying both are four ignores the empties. The pass rejects on the amount rather than the status. Nothing is rejected twice. |
| 5 | a | Thirty-nine orders that never had a discount now hold a zero that nobody can tell from a real one. | Nothing was deleted; distinct on discount rose from 9 to 10 because zero joined the nine real values. The field kept its name and its type. |
| 6 | b | A still holds what the source sent, and everything B added is unattributable. | B's usable amounts include six that were invented. The averages are not nearly the same, since six zeroes pull it down. Re-sending is what you do when the source is wrong, and it is not wrong here. |
| 7 | c | Forty-nine distinct values across fifty rows means one value appears twice. | No row is empty, since order_id is present on all fifty. A category has a handful of values, which is what segment looks like. Sort order changes nothing about distinctness. |
| 8 | d | The coercion only touched values that would not convert, and every order_id was present and unchanged. | Ids being text is true and is not the reason; the pass could have replaced them and did not. The duplicate was never removed. Distinct counts work on any type. |
| 9 | a | It names what was replaced, how many rows, and that the value came from you rather than from Kalpa. | The other three are all things somebody would write and none of them lets a reader reconstruct anything. |
| 10 | b | Once the raw values are gone there is no way to separate the zeroes you invented from the zeroes the file held. | Rows, totals and segments are all still readable, which is exactly what makes B dangerous. |
| 11 | c | 46 against 41 is the whole argument in two numbers, and it is the only pair that moves the wrong way. | The other three either favour B or say nothing. |
| 12 | d | Twelve records is a small enough denominator that one order moves a rate by more than eight points. | Segment being a category is true and decides nothing. Rejections turn on the amount. Write order is irrelevant. |
| 13 | a | A comment lives in the code and the decisions log travels with the data. | The other three are true statements about comments and none of them is the reason this comment fails. |
| 14 | b | Clean plus rejects plus the log is the set that lets somebody rebuild your count and your reasoning. | The clean file alone and the clean file with a count both leave the replaced values unrecoverable. Saying nothing can is defeatist and false, since the rejects file holds the raw values. |
| 15 | c | A count of rows the pass changed turns a silent replacement into a number on the profile. | A faster loop solves nothing. A chart per column is a lot of work for a fact three numbers already carry. A check that all fields convert is the coercion, dressed as a test. |

## The part worth arguing about

Item 6. Somebody always argues for B on the grounds that you cannot compute an average on a column with four unusable values. The reply is that you can, on the 44 that convert, and you say 44 beside the number. B lets you compute on 50 and the number is wrong by six invented zeroes, which nobody downstream can see.

Item 15 is the other. A room usually reaches for a chart. The point of the profiler is that three integers per field beat a chart, because integers fit in a log and a chart does not.

## The hands-on picks

The running half is `notebooks/C2_W01_D03_ex2_hands_on_STUDENT.ipynb`, and its four markers are:

**Answers: 1a 2b 3c 4d**

The executed twin is `C2_W01_D03_ex2_hands_on_solution_STUDENT.ipynb` in this folder.

## Where this pattern lives in production

The HGNC formally renamed about 27 human genes in 2020 because spreadsheets silently coerced names like SEPT1 into dates, after a 2016 audit found gene-name errors in roughly a fifth of genetics papers with spreadsheet supplements. That is item 2 at scale: real values replaced by values that look ordinary, with nothing in the file saying so.

The interview question is item 11's, and it arrives as "how do you know a cleaning pass did not damage the data?" Name the count that can fall, and say why the counts that rise prove nothing.
