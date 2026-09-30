# Kahoot, Week 1 Tuesday

Eight items, ungraded, scored on correctness and speed together. The last item returns to Monday,
one level up.

Each item names what it tests, so an item dropped for time says what was lost.

---

## Q1. Revenue per customer fell 8 percent. Which two numbers do you compute next?
*Tests: revenue per customer splits into two branches, and both are needed.*

- Customers and revenue, since the rate is built from both
- Revenue per order and discounts given, the price side
- The mean and the median of revenue per customer
- Orders per customer and revenue per order  <- correct

---

## Q2. Q1 has 13 weeks of orders and Q2 has 11. Which comparison is fair?
*Tests: a comparison across periods needs matched windows or a rate.*

- A rate per week, or the same 11 weeks of each quarter  <- correct
- The two totals as they stand, since both are quarters
- Q2's total scaled up by 13 over 11, then the two totals
- Q1's last 11 weeks against Q2, the most recent weeks of each

---

## Q3. After `result = revenue_for(seg)`, result holds None although the total printed. What went wrong?
*Tests: a function that prints hands back None, and the table built on it breaks.*

- The segment had no orders, so the total was zero
- The function was called before it had been defined
- The function prints its total and returns nothing  <- correct
- The variable name result is reserved in Python

---

## Q4. A segment's median order is Rs 1,200 and its range is Rs 80,000. What do you say about it?
*Tests: a typical value and a spread describe a group together.*

- Most orders are small; a few large ones stretch the range  <- correct
- Most orders sit near Rs 80,000, with a few small ones below
- The typical order is about Rs 40,000, halfway up the range
- The segment's figures must be wrong, since the gap is too wide

---

## Q5. Customers held flat, and orders per customer fell in one segment only. Which hypothesis goes in the note?
*Tests: a cause is a hypothesis with the evidence that would settle it.*

- Marketing lost customers, so the acquisition budget is the fix
- Prices rose across the company, so every customer bought less
- The segment's buyers left, and new buyers replaced them
- That segment's buyers changed; timing and its data test why  <- correct

---

## Q6. Of 100 invented orders, 40 record a discount, 20 record Rs 0 and 40 have no field. What share had a discount?
*Tests: missing means unknown until someone chooses a default and writes down why.*

- 40 percent, since the orders with no field had no discount
- 40 of the 60 that record it, with 40 orders reported apart  <- correct
- 80 percent, since the orders with no field were discounted too
- 60 percent, the orders that record the field in any amount

---

## Q7. Moved first, frequency costs Rs 51.6 lakh; moved second, Rs 60.9 lakh. What goes beside the bridge?
*Tests: a bridge's split depends on the order of its steps, so the order is written down.*

- The larger figure, since it is the more cautious reading
- The order of the steps, or the symmetric split  <- correct
- The average of the two, about Rs 56 lakh, to be fair
- Nothing yet, since two figures mean one of them is wrong

---

## Q8. Return to Monday. The mean order doubled and the median did not move. What is your first check?
*Tests: a mean pulled away from the median points at a few extreme values.*

- Recompute the median, since it should have doubled as well
- Report the mean, since it is the figure that uses every order
- Sort the amounts and read the few largest orders  <- correct
- Assume prices doubled and tell Finance to expect it
