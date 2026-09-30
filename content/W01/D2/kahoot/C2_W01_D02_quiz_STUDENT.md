# Kahoot, Week 1 Tuesday

Eight items, ungraded, scored on correctness and speed together. The last item returns to Monday,
one level up.

Each item names what it tests, so an item dropped for time says what was lost.

---

## Q1. Sales fell. Which rung of the ladder comes first?
*Tests: a drop is confirmed on matched windows before anyone explains it.*

- Split the fall by segment to find where it sits
- Confirm the drop is real on windows that match  <- correct
- Name the likeliest cause and test it against the data
- Decompose revenue into customers, frequency and order value

---

---

## Q2. Revenue per customer fell 8 percent. Which two numbers do you compute next?
*Tests: revenue per customer splits into two branches, and both are needed.*

- Customers and revenue, since the rate is built from both
- Revenue per order and discounts given, the price side
- The mean and the median of revenue per customer
- Orders per customer and revenue per order  <- correct

---

---

## Q3. Q1 has 13 weeks of orders and Q2 has 11. Which comparison is fair?
*Tests: a comparison across periods needs matched windows or a rate.*

- A rate per week, or the same 11 weeks of each quarter  <- correct
- The two totals as they stand, since both are quarters
- Q2's total scaled by 11 over 13, then the two totals
- Q1's last 11 weeks against Q2, the most recent weeks of each

---

---

## Q4. A segment's median order is Rs 1,200 and its range is Rs 80,000. What do you say about it?
*Tests: a typical value and a spread describe a group together.*

- Most orders are small; a few large ones stretch the range  <- correct
- Most orders sit near Rs 80,000, with a few small ones below
- The typical order is about Rs 40,000, halfway up the range
- The segment's figures must be wrong, since the gap is too wide

---

---

## Q5. After `result = revenue_for(seg)`, result holds None although the total printed. What went wrong?
*Tests: a function that prints hands back None, and the table built on it breaks.*

- The segment had no orders, so the total was zero
- The function was called before it had been defined
- The function prints its total and returns nothing  <- correct
- The variable name result is reserved in Python

---

---

## Q6. Revenue per order rose 18 percent, and no segment's own revenue per order rose that far. What happened?
*Tests: a blended rate can move while no segment moves; split mix from rate.*

- Customers in every segment paid about 18 percent more
- Small orders fell out of the mix, lifting the blend  <- correct
- The segments' figures were rounded, hiding the rise
- Business customers alone paid 18 percent more per order

---

---

## Q7. Customers held flat, and orders per customer fell in one segment only. Which hypothesis goes in the note?
*Tests: a cause is a hypothesis with the evidence that would settle it.*

- Marketing lost customers, so the acquisition budget is the fix
- Prices rose across the company, so every customer bought less
- The segment's buyers left, and new buyers replaced them
- That segment's buyers changed; timing and its data test why  <- correct

---

---

## Q8. Return to Monday. The mean order doubled and the median did not move. What is your first check?
*Tests: a mean pulled away from the median points at a few extreme values.*

- Recompute the median, since it should have doubled as well
- Report the mean, since it is the figure that uses every order
- Sort the amounts and read the few largest orders  <- correct
- Assume prices doubled and tell Finance to expect it
