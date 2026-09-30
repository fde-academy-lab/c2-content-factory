# Solution: the second case

Answers: 1d 2b 3c 4a

The executed notebook is `solutions/C2_W01_D02_ex2_second_case_solution_STUDENT.ipynb`, and its
lettered TODOs run a c b d. Item 4 is a design item.

## The idea being tested

Find what a number is made of before agreeing or disagreeing with it. Marketing's 40 percent is two
people; its website claim fails on a segment that uses the same website; the tier's call list comes
from orders per member, Q1 against Q2.

## Item by item

| Item | Kind | Key | Why it holds | Why the others fail |
|---|---|---|---|---|
| 1 | scenario | d | The Student ids are the same two in both quarters, and orders went from 5 to 7. | a: no Student id is new in Q2. b: nothing in the file links the orders to a campaign, and on two customers one more order moves the rate 20 percent. c: the 40 percent is orders per customer, not revenue per order. |
| 2 | design | b | A broken website hurts everyone who uses it, so the comparison segment on the same website is the test; Retail-Core held. | a: the app is a different channel and fell too. c: one order to three is too few to read. d: the total mixes the members' fall into everyone else's. |
| 3 | scenario | c | Seven members fell from three orders a quarter to one, the largest drop per member; eleven more fell by one. | a: every member ordered in Q2. b: they had least to lose. d: a list of everyone sets no order of calls. |
| 4 | design | a | The fall began in July, before the break, and chapter 6 capped the button at about 4 orders, so the tier's July change log tests the cause behind the larger part. | b: tests the smaller, after-break part, and is the second request. c: measures acquisition, which the overlap ruled out. d: the export raised the question and cannot test a cause, whatever the month it starts from. |
