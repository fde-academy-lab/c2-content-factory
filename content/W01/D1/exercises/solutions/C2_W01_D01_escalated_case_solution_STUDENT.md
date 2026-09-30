# Solution: does the answer survive on what stayed delivered?

Answers: 3c 4b 5a 7d 8b 9a

The three numbers: item 1 is 19 customers, item 2 is 1.11 orders per customer, item 6 is 7
customers. The notebook's nine TODO picks are `cbdcaabbc`.

The executed notebook beside this file,
`exercises/solutions/C2_W01_D01_ex1_escalated_case_solution_STUDENT.ipynb`, computes every number
here from the 30 orders.

## The idea being tested

Anand asks whether the answer holds on the orders that stayed sold. On the 21 delivered orders, 19
customers kept 1.11 orders each and only 2 kept two; the typical order is Rs 2,060;
 the plan on the 20 everyday delivered orders needs 3 more from frequency alone; a 15 percent discount with
10 percent more orders still loses 6.5 percent. Of the 17 one-time buyers, 7 bought inside the last
45 days. Orders per customer fell; the typical order, the window's edge and the branch held, and the
delivered view adds the leak: of the 7 customers who came back, 4 lost that second order to a
cancellation or a return.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | 19 | The 21 delivered orders carry 19 distinct ids. | 21 counts orders; 23 is the booked customer count. |
| 2 | 1.11 | 21 / 19. | 1.30 is the booked rate; 21 / 23 = 0.91 mixes two definitions. |
| 3 | c | An odd count has one middle, the 11th value, at index 10. | a is the even-count rule, chapter 4's case, applied to an odd count. b is one place past the middle. d is the mean. |
| 4 | b | The plan is a growth plan, and the order at the top of chapter 4's sort is not something a retention offer repeats; on the 20 everyday delivered orders, Rs 40,790, 20 x 1.15 = 23, so 3 more orders at a typical value. | a values every extra order at the delivered mean of Rs 24,800, which no typical order is. c sizes customers, the acquisition branch. d leaves Anand's definition, which is the point of the case. |
| 5 | a | Rs 40,790 x 0.85 x 1.10 = Rs 38,139, since price and quantity multiply. | b adds the two percentages. c counts the orders and forgets the price. d adds both changes as gains. |
| 6 | 7 | Of 17 delivered one-time buyers, 7 placed their order fewer than 45 days before 26 September. | 9 is the booked count; 17 is every one-time buyer. |
| 7 | d | The customers exist and some return; the delivered view shows 4 of the 7 returning customers losing that second order, which is still the frequency branch. | a reads a leak as a missing customer. b and c rest on fields the file lacks or a mean one order drags. |
| 8 | b | The rate fell from 1.30 to 1.11; the median moved Rs 145 and the branch did not move. | a ignores the fall in the rate. c: the typical order fell slightly. d reads a leak as the wrong branch. |
| 9 | a | The board reads Finance's books, and the bridge shows every rupee between the two definitions. | b picks the figure by its size. c picks the definition by the conclusion. d hides the definitions and brings back the mean. |
| 10 | a sentence | "On the 21 delivered orders from 1 July to 26 September, 19 customers kept 1.11 orders each at a typical Rs 2,060, and 17 kept only one, 7 of them too recent to judge, so frequency is still the branch to open first, with returns and cancellations on repeat orders as the leak to fix; one quarter cannot show which branch moved, so hold the Rs 12 crore until Tuesday's two quarters." | A sentence that says "17 of 19 lost" repeats chapter 6's trap; one without the definition repeats chapter 1's. |

## The part worth arguing about

Item 7. A room may argue that 2 of 19 is so low that frequency is hopeless and acquisition wins.
The 7 who came back on booked orders show the customers do return; 4 of them lost the second order
to a cancellation or a return, and a leak is fixed on the frequency branch, not by buying new customers.

**Kavya's review.** "You rebuilt it on Anand's definition and said what moved and what held. That is
the answer that survives the board."

## Hands-on

Every check in the solution notebook passes, including that the branch picked is frequency.
