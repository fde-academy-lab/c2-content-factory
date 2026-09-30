# Can you make seven of Tuesday's calls and one of Monday's at speed?

The quiz has eight items, ungraded and scored on correctness and speed together. Every item comes
from the day's case: Kalpa Retail's booked revenue, every order placed before any cancellation or
return, fell from Q1 to Q2, and the day climbed the investigation one rung at a time, each rung a
question settled before the next. The last item returns to Monday, one level up.

---

## Q1. When sales fall, which rung of the investigation comes first?
*Tests: a drop is confirmed on matched windows before anyone explains it.*

- Split the fall by segment to find where it sits
- Confirm the drop is real on windows that match  <- correct
- Name the likeliest cause and test it against the data
- Decompose revenue into customers, frequency and order value

---

## Q2. Revenue per customer fell 8 percent: which two numbers do you compute next?
*Tests: revenue per customer splits into two branches, and both are needed.*

- Customers and revenue, since the rate is built from both
- Revenue per order and discounts given, the price side
- The mean and the median of revenue per customer
- Orders per customer and revenue per order  <- correct

---

## Q3. With 13 weeks of orders in Q1 and 11 in Q2, which comparison is fair?
*Tests: while a quarter is still open, the fair comparison is the same weeks of both quarters, with a rate per week beside them, since a rate alone fixes the length and leaves the position.*

- The same 11 weeks of each quarter, with a rate per week beside them  <- correct
- The two totals as they stand, since both windows are called quarters
- Q2's total scaled up by 13 over 11, then the two totals
- Q1's last 11 weeks against Q2's first 11, the most recent weeks of Q1

---

## Q4. What do you say about a segment whose median order is Rs 1,200 and whose range is Rs 80,000?
*Tests: a typical value and a spread describe a group together.*

- Most orders are small, and a few large ones stretch the range  <- correct
- Most orders sit near Rs 80,000, with a few small ones below
- The typical order is about Rs 40,000, halfway up the range
- The segment's figures must be wrong, since the gap is too wide

---

## Q5. Why does `result = revenue_for(seg)` hold None when the total printed?
*Tests: a function that prints hands back None, and the table built on it breaks.*

- The segment had no orders, so the total was zero
- The function was called before it had been defined
- The function prints its total and returns nothing  <- correct
- The return sits inside the loop, so it stopped after one order

---

## Q6. Revenue per order rose 18 percent while no segment's own rose that far: what happened?
*Tests: a blended rate can move while no segment moves; split mix from rate.*

- Customers in every segment paid about 18 percent more
- Small orders fell out of the mix, lifting the blend  <- correct
- The segments' figures were rounded, hiding the rise
- Business customers alone paid 18 percent more per order

---

## Q7. Customers held flat and one segment's orders per customer fell: which hypothesis goes in the note?
*Tests: a cause is a hypothesis with the evidence that would settle it.*

- Marketing lost customers, so the acquisition budget is the fix
- Prices rose across the company, so every customer bought less
- The segment's buyers left, and new buyers replaced them
- That segment's buyers slowed, and its timing and data test why  <- correct

---

## Q8. Back to Monday: the mean order doubled and the median held, so what is your first check?
*Tests: a mean pulled away from the median points at a few extreme values.*

- Recompute the median, since it should have doubled as well
- Report the mean, since it is the figure that uses every order
- Sort the amounts and read the few largest orders  <- correct
- Assume prices doubled and tell Finance to expect it
