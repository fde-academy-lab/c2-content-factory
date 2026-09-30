# Which answers show whether Meera's answer survives on the delivered orders?

Answers: 3c 4b 5a 7d 8b 9a

The three numbers: item 1 is 19 customers, item 2 is 1.11 orders per customer, and item 6 is 7
customers. The notebook's nine TODO picks are `cbdcaabbc`.

The executed notebook beside this file,
`exercises/solutions/C2_W01_D01_ex1_escalated_case_solution_STUDENT.ipynb`, computes every number
here from the 30 orders.

## What does the case test?

Anand asks whether the answer holds on the orders that stayed sold. On the 21 delivered orders, 19
customers kept 1.11 orders each and only 2 kept two. The typical delivered order is Rs 2,060, the
11th of the 21 sorted amounts, since an odd count has one middle. Sized on the consumer view's
delivered revenue, Rs 40,790, the plan asks about Rs 6,119 more, to about Rs 46,909, and marketing's
15 percent discount with 10 percent more orders would take the same Rs 40,790 to Rs 38,139, a fall
of 6.5 percent. Of the 17 delivered one-time buyers, 7 ordered fewer than 45 days before 26
September. Orders per customer fell; the typical order, the window's edge and the branch held, and
the delivered view adds a leak: of the 7 customers who came back on booked orders, 4 lost that
second order to a cancellation or a return.

## Why is each answer right, and why does each other option fail?

| Item | Key | The question in one line | Why the key holds | Why each other option fails |
|---|---|---|---|---|
| 1 | 19 | How many distinct customers stand behind the 21 delivered orders? | The 21 delivered orders carry 19 distinct customer ids. | 21 counts orders as customers; 23 is the booked customer count. |
| 2 | 1.11 | What is orders per customer on the delivered reading? | 21 / 19 = 1.11. | 1.30 is the booked rate; 21 / 23 = 0.91 divides delivered orders by booked customers, two readings in one fraction. |
| 3 | c | Which expression is the median of 21 sorted delivered amounts? | An odd count has one middle, the 11th value, which sits at index 10 in a list counted from zero: Rs 2,060. | a: halfway between two middles is the even-count rule, chapter 4's case, applied to an odd count. b: index 11 is the 12th value, one past the middle. d: the total over the count is the mean. |
| 4 | b | Which base should the 15 percent plan use on Anand's delivered reading, and what does it ask? | The plan concerns the three consumer segments and Anand counts what stayed delivered, so the base is the consumer view's delivered revenue: Rs 40,790 x 1.15 is about Rs 46,909, Rs 6,119 more. | a: all delivered revenue includes the segments the plan does not concern, and would ask the consumer segments for Rs 78,119 on top of Rs 40,790. c: the booked consumer view is chapter 5's base, and Anand asked for delivered. d: booked revenue leaves Anand's definition and the plan's segments at once. |
| 5 | a | Where would 15 percent off with 10 percent more orders leave revenue on the Q4 base? | Price and quantity multiply: Rs 40,790 x 0.85 x 1.10 = Rs 40,790 x 0.935 = Rs 38,139, a fall of 6.5 percent. | b: Rs 61,570 applies the added-up 5 percent fall to the booked consumer view. c: Rs 38,751 is the right base with the percentages added, 10 less 15. d: Rs 60,597 multiplies correctly on the booked consumer view, the wrong base for Anand. |
| 6 | 7 | How many delivered one-time buyers ordered fewer than 45 days before the end? | Of the 17 delivered customers who kept one order, 7 ordered fewer than 45 days before 26 September. | 9 is the booked count; 17 is every delivered one-time buyer. |
| 7 | d | Which branch should Meera open first on delivered orders? | The customers exist and some return: on booked orders 7 came back, and 4 of those lost the second order to a cancellation or a return, a leak on the frequency branch that the delivered view makes visible. | a: a lost second order is a leak on customers Kalpa already has, and buying new customers does not mend it. b: the rate fell from 1.30 to 1.11, so the branch holds for a different reason. c: Rs 24,800 is the delivered mean, twelve times the delivered median of Rs 2,060, so it describes almost no delivered order, as chapter 4 found for the booked mean. |
| 8 | b | Which line says what moved and what held between booked and delivered? | Orders per customer fell from 1.30 to 1.11, the median moved Rs 145, from Rs 2,205 to Rs 2,060, and the branch did not move. | a: the rate fell, so something moved. c: the typical order fell slightly. d: a leak on repeat orders is still the frequency branch. |
| 9 | a | Which reading goes in the headline of the note Anand reads at the board, and what goes beside it? | The board reads Finance's books, which count what stayed sold, and the walk beside it shows every rupee of the Rs 24,020 between the readings. | b: the board's books count delivered, so a booked headline starts an argument the note cannot win. c: a reading chosen because it sits in the middle answers no one's question. d: without booked and the walk, nobody can see where the Rs 24,020 went. |
| 10 | a sentence | What one sentence goes to Meera on delivered orders? | "On the 21 delivered orders from 1 July to 26 September, 19 customers kept 1.11 orders each at a typical Rs 2,060, and 17 kept one, 7 too recent to judge, so frequency is still the branch to open first, with returns and cancellations on repeat orders as its leak; one quarter cannot show which branch moved, so hold the Rs 12 crore until Tuesday's two quarters." | A sentence that says "17 of 19 lost" repeats chapter 6's wrong number, and one without its reading of sales repeats chapter 1's. |

## Which item is worth arguing about?

Item 7. A room may argue that 2 of 19 is so low that frequency is hopeless and acquisition wins.
The 7 who came back on booked orders show the customers do return, and 4 of them lost that second
order to a cancellation or a return. A leak on customers Kalpa already has is mended on the frequency
branch, by fixing what went wrong with the second order, and buying new customers leaves it open.

**Kavya's review.** "You rebuilt it on Anand's definition and said what moved and what held. That is
the answer that survives the board."

## What does the solution notebook confirm?

Every check in the solution notebook passes, including that the branch picked is frequency and that
frequency alone reaches the plan on the consumer view's delivered revenue.
