# Solution: the escalated case

Answers: 1c 2b 3d 4a 5b

The notebook's letters are `cbcdabadba`, and its executed solution is
`exercises/solutions/C2_W02_D04_hands_on_solution_STUDENT.ipynb`. The four numbers are 340
customers, Rs 19,84,00,000 of spend, 130 customers reached and 111 on the win-back list.

## The five parts

| Part | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | c | groupby only makes groups for keys in the order rows, and 39 customers have none. The customer list is the spine. | a: the warehouse count is 340 on Monday and today. b: `dropna` is about missing keys, and these customers are absent, not missing. d: a left join from the orders side keeps the same 301. |
| 2 | b | An error of this kind is information about the feed. The rule is the business's: reach is first exposure. Validate stays on for next Monday. | a still multiplies the reached customers' rows. c ships the wrong table this week. d describes the defect instead of fixing it. |
| 3 | d | Without the group, `shift(1)` reads the row above, which belongs to another customer. It is Wednesday's LAG without PARTITION. | a: the flag is real output of the code. b: the filter runs before the flag in the notebook. c would flag rises everywhere, not one odd customer. |
| 4 | a | Rs 2,708 is the average Retail-Plus order in September; the month's spend is Rs 1,24,570. | b: the slide is by segment. c: September is complete to the 28th. d: a count would be under a hundred. |
| 5 | b | The wall clock moves; the data did not. Recency from the data's last date makes two runs agree. | a: the file did not change. c: fillna is the same every run. d: order of groups does not change counts. |

## The three sentences to the growth team

"The customer table holds 340 rows, one per customer, as of 28 September, the data's last date,
and its spend adds to Monday's book of Rs 19,84,00,000. The monsoon sale reached 130 customers,
each counted once at their first exposure, and 111 customers are on the 60-day win-back list.
The refresh stops if the exposure feed repeats a customer or if spend stops adding to the book."
