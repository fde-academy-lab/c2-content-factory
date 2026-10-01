# Solution: Does the story survive when revenue counts only the orders that reached customers and stayed?

Answers: 1b 2c 3a 4d 5a 6c

The executed notebook is `solutions/C2_W01_D02_ex1_escalated_case_solution_STUDENT.ipynb`, and its
lettered TODOs run b a c d a b d. Two of the six items are design items: 2 and 6.

Meera Raghavan, Kalpa Retail's CEO, asked whether the morning's story survives on delivered orders,
the board pack's definition: only the orders whose status is delivered, the ones that reached the
customer and were not sent back. On booked orders, every order placed before any cancellation or
return, the morning found revenue down 11.0 percent, the same 69 customers in both quarters, orders
per customer down from 1.65 to 1.25 and furthest down in Retail-Plus, the paid membership tier, and
about 69 percent of the rise in revenue per order coming from the mix of segments.

## What does the escalated case test?

It is the morning's ladder, climbed alone on a harder definition. The drop, the branch and the
segment all survive. The one thing that moves is the customers branch, and it turns out to be
cancellations and returns: every customer who dropped out of the delivered count booked again in Q2
and had those orders cancelled or returned, so nobody was lost.

## Part 1. Is the delivered drop real?

### Q1. Which figure answers Meera on delivered revenue?

The notebook keeps the delivered orders and compares the two closed quarters of 13 weeks each.

The key is b, "Down 11.3 percent, since closed delivered quarters differ by Rs 16,40,290". The two
quarters hold 138 delivered orders between them, and Rs 16,40,290 less on two closed quarters of 13
weeks is a fall of 11.3 percent.

- a, "Down 25.9 percent, since the Q2 tile holds 11 weeks of delivered orders against 13": 25.9 is
  the morning's booked window trap, and the closed delivered quarters both hold 13 weeks.
- c, "Down 11.0 percent, since the definition changes no total that matters to Meera": 11.0 is the
  booked figure.
- d, "No fall at all, since returns for Q2 are still arriving and will lift its total": late returns
  can only lower Q2's delivered total, never lift it.

## Part 2. Which branch moves on delivered orders?

### Q2. Which check runs before anyone names the customers branch? (Design)

Customers with a delivered order fell from 54 to 50, and the bridge charges that branch Rs 10,74,442.

The key is c, "The delivered ids against the booked ids; a leaver who never booked in Q2 is churn". A
branch that held on booked orders and moves on delivered ones is made of whatever the new definition
drops, so the check sets the customers who left the delivered count against those who still booked.
Churn would show as a leaver with no Q2 order at all.

- a, "The CRM's sign-ups by month; a Q2 campaign would make it acquisition": sign-ups count new
  customers only, and the question is who left.
- b, "The bridge in the other order; a smaller customers step would make it an artefact": the order
  of the bridge moves the size of a step, never what the step is made of.
- d, "The tree per segment; a fall inside one segment would make it that segment's churn": a tree per
  segment still counts delivered customers, which is the number that needs explaining.

## Part 3. Are those lost customers?

### Q3. What happened to the customers who dropped out of the delivered count in Q2?

Nineteen of Q1's delivered customers have no delivered order in Q2.

The key is a, "Customers who ordered in Q2 and had those orders cancelled or returned". The customers
delivered to in Q1 and not in Q2, set against the customers who booked in Q2, hold all 19, and their
Q2 orders were 10 cancelled and 10 returned.

- b, "Customers Kalpa lost, replaced by fifteen new ones who joined in Q2": the booked overlap is 69
  in both quarters, none only in Q1 and none only in Q2.
- c, "Business accounts whose large orders are still waiting to be delivered": the 19 span segments,
  and their Q2 orders ended cancelled or returned.
- d, "Customers whose Q1 orders were delivered late and counted in Q2 instead": every order sits in
  the quarter of its order date, so no delivery moves an order between quarters.

## Part 4. Which segment moves on delivered orders?

### Q4. How did orders per customer move on delivered orders?

The notebook runs `tree_for` on each segment's delivered orders and rolls the rate up to the company.

The key is d, "Weighted it fell from 1.50 to 1.14, and Retail-Plus fell furthest at 42.6 percent". 81
delivered orders over 54 customers is 1.50 and 57 over 50 is 1.14, and Retail-Plus went from 1.85 to
1.06 orders per member.

- a, "Averaged over the four segments it fell 9.2 percent, so frequency matters less here": it
  averages the segments' averages again, so a two-customer segment counts as much as a large one.
- b, "Business fell furthest, 11.6 percent, since its orders are the largest": Business fell 11.6
  percent, less than Retail-Plus.
- c, "Every segment fell by about the same share, so no segment stands out": Retail-Plus fell nearly
  four times as far as the next segment.

## Part 5. Is the delivered rise mix or rate?

### Q5. What does a mix share of 44 percent mean for the consumer business?

On delivered orders the mix explains 44 percent of the rise in revenue per order, Rs 1,79,074 to
Rs 2,25,696, against 69 percent on booked orders.

The key is a, "Little, since the rate part is Business's larger orders, not consumer prices".
Business's delivered orders grew from Rs 10,24,651 to Rs 11,60,405 each on average, while the
consumer segments moved by about a hundred rupees at most.

- b, "Consumer prices rose, since the rate part now carries most of the rise": the rate part is
  Business.
- c, "The split failed, since mix and rate should not change with the definition used": the split
  depends on the orders it is run on, and delivered orders are a different set.
- d, "Delivered orders are unreliable, so the booked split should be used on its own": both
  definitions are valid, and they answer different questions.

## Stretch. How do you report two definitions next month?

### Q6. What goes in next month's report, and what would change it? (Design)

Meera will see both definitions again next month, booked and delivered.

The key is c, "Both side by side and labelled, moving to delivered alone once returns settle". Two
definitions answer two questions, and the newest quarter's delivered figure still moves as returns
post. Once they settle, delivered alone matches the board.

- a, "Delivered alone, since it is the board's number, whatever the booked figure says": it drops the
  definition the morning's work used, with no bridge between the two.
- b, "Booked alone, since it closes first and never moves after the quarter": it ignores the board's
  definition.
- d, "Delivered alone, with last quarter's booked figures restated as delivered": it reports
  delivered alone while the newest quarter's returns are still posting, and drops the booked view
  Meera has already seen.
