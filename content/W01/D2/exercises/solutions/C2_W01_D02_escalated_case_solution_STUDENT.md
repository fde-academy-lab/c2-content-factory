# Solution: the escalated case, mix against rate

Answers: 1c 2a 3d 4b 5c 6d

## The idea being tested

A fall can sit in one place in behaviour and another place in rupees, and both are true at once.
An overall rate is a weighted blend of the segments' rates, so it moves when the mix of orders
moves even if no segment's rate changes. And a helper that returns nothing on some inputs drops
those inputs from every table built on it, which is why the groups in and the groups out are
counted every time.

## The numbers, by segment (Q1 then Q2)

| Segment | Customers | Orders | Orders per customer | Revenue | Revenue per order |
|---|---|---|---|---|---|
| Retail-Core | 34, 34 | 38, 36 | 1.12, 1.06 (down 5.3 percent) | Rs 80,460, Rs 72,510 | Rs 2,117, Rs 2,014 |
| Retail-Plus | 22, 22 | 51, 26 | 2.32, 1.18 (down 49.0 percent) | Rs 1,43,550, Rs 78,300 | Rs 2,815, Rs 3,012 |
| Business | 11, 11 | 20, 17 | 1.82, 1.55 (down 15.0 percent) | Rs 2,07,71,180, Rs 1,85,41,460 | Rs 10,38,559, Rs 10,90,674 |
| Student | 2, 2 | 5, 7 | 2.50, 3.50 (up 40.0 percent) | Rs 4,810, Rs 7,730 | Rs 962, Rs 1,104 |

The orders bridge from 114 to 86: Retail-Core less 2, Retail-Plus less 25, Business less 3, Student
plus 2. The rupee bridge from Rs 2,10,00,000 to Rs 1,87,00,000: Business less Rs 22,29,720, Retail-Plus
less Rs 65,250, Retail-Core less Rs 7,950, Student plus Rs 2,920. The three consumer segments fell from
Rs 2,28,820 to Rs 1,58,540, a fall of 30.7 percent, and Retail-Plus is Rs 65,250 of that Rs 70,280.

Mix against rate: at Q2's order mix and Q1's revenue per order in each segment, revenue per order
would have been Rs 2,07,112. The mix explains Rs 22,902 of the Rs 33,231 rise, about 69 percent, and
the change within segments explains Rs 10,330. Order shares moved from Retail-Core 33.3, Retail-Plus
44.7, Business 17.5 and Student 4.4 percent to 41.9, 30.2, 19.8 and 8.1 percent.

In Retail-Plus, 3 members ordered once in Q1, 9 twice and 10 three times; in Q2, 18 ordered once, 4
twice and none three times. Every member still bought, and the members who ordered three times now
order once.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | c | The orders bridge puts 25 of the 28 lost orders in Retail-Plus, and its 22 members are the same in both quarters. | a reads rupee size as the answer to a question about orders. b: the loss is concentrated in one segment. d: Retail-Core lost two orders, and customer count does not set the company's frequency. |
| 2 | a | Business is Rs 22,29,720 of the Rs 23,00,000 fall, about 97 percent, from 20 orders to 17; in behaviour, Retail-Plus halved. Both hold, and three orders are too few to call a trend today. | b drops the behavioural finding. c: Retail-Plus orders are small, so halving them is Rs 65,250. d: the bridges answer different questions and agree with each other. |
| 3 | d | Q2's order mix at Q1's values gives Rs 2,07,112, so mix is Rs 22,902 of the Rs 33,231 rise, about 69 percent. Revenue per order rose mainly because small Retail-Plus orders disappeared, with no one paying more. | a: Retail-Core's revenue per order fell. b has the split backwards. c: holding one factor at Q1's value is exactly how the two are separated. |
| 4 | b | The helper prints and returns None when a change exceeds 30 percent, so Retail-Plus (down 49.0) and Student (up 40.0) returned None and the filter dropped them. Four segments went in and two rows came out. The fix returns the change every time and flags a large one in a separate column. | a: rounding to one decimal hides nothing here. c: the printed lines are the two largest moves, with no segment name beside them. d: moving the threshold moves the bug to other data. |
| 5 | c | It carries the fall, the flat customer count, the segment with its numbers and the rupee story, and it claims no cause. | a turns three orders into a trend and a cause. b is the marketing lead's reading, which Part 3 overturns. d: the fall is concentrated, which is the finding. |
| 6 | d | Mix explains 68.9 percent moved first and 72.3 percent moved second. The part where mix and rate moved together goes to whichever moves second, so the split shifts by three points and the answer does not: revenue per order rose mainly because small orders disappeared. Say which order you used. | a and b make a convention into a rule. c: both figures are exact; they differ only in who is charged for the overlap. |

## The part worth arguing about

Item 2. Some of the room will want one answer to "where is the fall". The honest answer has two
parts and says which comes first: in behaviour it is Retail-Plus, where the same members buy half as
often, which is a pattern across 22 people; in rupees it is three Business orders, each worth lakhs,
which Wednesday's reconciliation and Thursday's test check before anyone acts on it.

## Where the pattern lives in production

Mix against rate is how finance teams explain a margin that moved while no product's margin did,
and how product teams explain an average order value that rose while sales fell. A helper that
returns None on some inputs is one of the most common silent failures in analytics code: the table
looks complete, and the rows it lost were the interesting ones.

## Hands-on picks

The executed solution, `exercises/solutions/C2_W01_D02_04_escalated_case_solution_STUDENT.ipynb`,
carries the picks for every `TODO` in the notebook, each with the check it passes.
