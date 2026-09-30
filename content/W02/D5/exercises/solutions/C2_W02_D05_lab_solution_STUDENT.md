# Solution: the practice lab

Answers: 1a 2c 3a 4b 5c 6a 7b 8c 9b 10d 11c 12d 13a 14c 15b 16a 17d 18b

## The idea being tested

Problem 1 is the operating rule applied to asks the team really receives: Finance's numbers and every
cleaning step belong to the warehouse, exploration belongs to pandas, and the room belongs to Excel.
Problem 2 is three draft cards a director misreads: one with no period or comparison, one with no
base, and one whose comparison points the wrong way. Problem 3 is round 1's trap on numbers small
enough to hold in your head. Problem 4 is the day's four checks on a sheet somebody else built, which
is how the traps arrive in real work.

## Problem 3, worked

Rows: seven single payments, four instalment rows and two gateway rows, 13 in all, for 10 orders.

| Version | Rows | Sum of order_amount |
|---|---|---|
| As exported | 13 | 20,000 + 2 x 40,000 + 2 x 60,000 + 2 x 2,000 = Rs 2,24,000 |
| After Remove Duplicates | 12 | The gateway's copy goes: Rs 2,22,000 |
| Each order once | 10 | 20,000 + 40,000 + 60,000 + 2,000 = Rs 1,22,000 |

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | a | An audited number is computed where it can be reviewed and rerun. | b is exploration. c lets a sheet own an audited number. |
| 2 | c | Slicing a reconciled table in a room is the last mile. | a and b cannot be sliced by a director on a laptop. |
| 3 | a | Removing rows is cleaning, and cleaning in a sheet leaves no record. | b is acceptable for a one-off look, never for the number the deck uses. c is the step the day says never to do in Excel. |
| 4 | b | Five definitions in an afternoon is the analyst's iteration. | a fixes a definition before anyone knows which one works. c cannot rebuild a table five ways reproducibly. |
| 5 | c | A lookup on a finished table, on a laptop, without a login. | a and b need a login and a tool the chief of staff does not use. |
| 6 | a | Finance signs it, so the warehouse owns it. | b and c hold a signed number in a place nobody audits. |
| 7 | b | An unfunded one-off hypothesis is exploration. | a builds a warehouse job for a question that may die tomorrow. c has no way to join returns to cities reproducibly. |
| 8 | c | A what-if is an input on the sheet, beside the actual. | a and b put an assumption into the source of truth. |
| 9 | b | "Up 12 percent" with no period and no comparison is read against whatever the director remembers. | a is the misread itself. c and d name details a period would not fix. |
| 10 | d | A count of people needs its base: 15 of 91 members is 16.5 percent. | a, b and c are real questions that the missing base makes secondary. |
| 11 | c | 462 is below 538, so "up" is wrong: the fall is 14.1 percent. | a asks for a base the count does not need. b is a smaller gap. d misses the wrong word. |
| 12 | d | Every repeated row adds its order's amount again: Rs 2,24,000. | a is the right total. b and c are partial repeats. |
| 13 | a | Only the gateway's identical copy goes, leaving 12 rows and Rs 2,22,000. | b is counting each order once. c removes instalment rows, which are not identical. d removes nothing. |
| 14 | c | Ten orders: Rs 20,000 plus Rs 40,000, Rs 60,000 and Rs 2,000. | a drops the Rs 2,000 order. b drops a digit. d is the Remove Duplicates total. |
| 15 | b | Rows outnumber orders and the total is double the warehouse: the grain. | a and c are real defects that would not double the total so cleanly. d confuses the export's total with the business's. |
| 16 | a | A departed member is missing from the table, and an approximate match returns a neighbour. | b sorting is what makes an approximate match look plausible. c and d accept a number for a member who is not there. |
| 17 | d | A foot that ignores a filter is SUM. | a would empty the list, which the question does not describe. b and c describe filters that fail visibly. |
| 18 | b | Rs 80,000 on Rs 4.00 lakh is 20 percent; 25 percent divides by Rs 3.20 lakh. | a measures on the later quarter. c and d do not touch the wrong base. |
