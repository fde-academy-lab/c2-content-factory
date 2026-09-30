# Solution: the escalated case, on delivered orders

Answers: 1b 2c 3a 4d 5a 6c

The executed notebook is `solutions/C2_W01_D02_ex1_escalated_case_solution_STUDENT.ipynb`, and its
lettered TODOs run b a c d a b d. Items 2 and 6 are design items.

## The idea being tested

The morning's ladder, climbed alone on a harder definition. The drop survives, the branch survives,
and the segment survives; the one thing that moves is the customers branch, and it turns out to be
fulfilment rather than churn: every customer who dropped out of the delivered count booked again in
Q2 and had orders cancelled or returned.

## Item by item

| Item | Kind | Key | Why it holds | Why the others fail |
|---|---|---|---|---|
| 1 | scenario | b | 138 delivered orders; Rs 16,40,290 less on two closed quarters of 13 weeks is 11.3 percent. | a: 25.9 is the morning's window trap. c: 11.0 is the booked figure. d: returns can lower the newest quarter further, which never makes the fall disappear. |
| 2 | design | c | The right move when a branch starts moving under a new definition is to decompose it before anyone names it. | a: the overlap in Part 3 shows nobody left. b: the bridge is exact; the definition changed. d: frequency still carries Rs 32,23,327, the largest move. |
| 3 | scenario | a | (delivered Q1 minus delivered Q2) and booked Q2 holds all 19; their Q2 orders were 10 cancelled and 10 returned. | b: the booked overlap is 69, 0 and 0. c: the 19 span segments and their Q2 orders ended cancelled or returned. d: nothing in the file shows split ids. |
| 4 | scenario | d | 81 over 54 and 57 over 50; Retail-Plus 1.85 to 1.06. | a: the average of averages again. b: Business fell 11.6 percent, less than Retail-Plus. c: Retail-Plus fell four times as far as the next segment. |
| 5 | scenario | a | Business's delivered orders grew from Rs 10,24,651 to Rs 11,60,405 each on average; consumer segments moved by about a hundred rupees at most. | b: the rate part is Business. c: the split legitimately depends on the population. d: both definitions are valid and answer different questions. |
| 6 | design | c | Two definitions answer two questions, and the newest quarter's delivered figure still moves as returns post; once they settle, delivered alone matches the board. | a: drops the definition the morning's work used, with no bridge between. b: ignores the board's definition. d: chooses by outcome, which no reader can trust. |
