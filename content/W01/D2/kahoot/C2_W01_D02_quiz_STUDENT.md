# Kahoot, Week 1 Tuesday

Nine items, ungraded, scored on correctness and speed together. The last item returns to Monday,
one level up.

Each item names what it tests, so an item dropped for time says what was lost.

---

## Q1. A stakeholder says sales dropped last quarter. What is your first move?
*Tests: the first rung of the ladder, confirming the drop before explaining it.*

- Split the fall by segment to find where it sits
- Check both windows match, then confirm the drop  <- correct
- Ask the marketing lead which branch they suspect
- Decompose revenue along the tree into its branches

---

## Q2. Revenue per customer fell 8 percent. Which two numbers do you compute next?
*Tests: revenue per customer splits into two branches, and both are needed.*

- Customers and revenue, since the rate is built from both
- Revenue per order and discounts given, the price side
- The mean and the median of revenue per customer
- Orders per customer and revenue per order  <- correct

---

## Q3. Q1 has 13 weeks of orders and Q2 has 11. Which comparison is fair?
*Tests: a comparison across periods needs matched windows or a rate.*

- A rate per week, or the same 11 weeks of each quarter  <- correct
- The two totals as they stand, since both are quarters
- Q2's total scaled up by 13 over 11, then the two totals
- Q1's last 11 weeks against Q2, the most recent weeks of each

---

## Q4. After `result = revenue_for(seg)`, result holds None although the total printed. What went wrong?
*Tests: a function that prints hands back None, and the table built on it breaks.*

- The segment had no orders, so the total was zero
- The function was called before it had been defined
- The function prints its total and returns nothing  <- correct
- The variable name result is reserved in Python

---

## Q5. A segment's median order is Rs 1,200 and its range is Rs 80,000. What do you say about it?
*Tests: a typical value and a spread describe a group together.*

- Most orders are small; a few large ones stretch the range  <- correct
- Most orders sit near Rs 80,000, with a few small ones below
- The typical order is about Rs 40,000, halfway up the range
- The segment's figures must be wrong, since the gap is too wide

---

## Q6. Customers held flat, and orders per customer fell in one segment only. Which hypothesis goes in the note?
*Tests: a cause is a hypothesis with the evidence that would settle it.*

- Marketing lost customers, so the acquisition budget is the fix
- Prices rose across the company, so every customer bought less
- The segment's buyers left, and new buyers replaced them
- That segment's buyers changed; timing and its data test why  <- correct

---

## Q7. A discount field is absent on some orders. What goes in the discount total?
*Tests: missing means unknown until someone chooses a default and writes down why.*

- The absent orders read as zero, since no discount was recorded
- The recorded discounts, with the absent orders reported apart  <- correct
- The average recorded discount, filled in for every absent order
- Nothing, since the total cannot be given while fields are absent

---

## Q8. Moved first, frequency costs Rs 51.6 lakh; moved second, Rs 60.9 lakh. What goes beside the bridge?
*Tests: a bridge's split depends on the order of its steps, so the order is written down.*

- The larger figure, since it is the more cautious reading
- The order of the steps, or the symmetric split  <- correct
- The average of the two, about Rs 56 lakh, to be fair
- Nothing yet, since two figures mean one of them is wrong

---

## Q9. Return to Monday. The mean order doubled and the median did not move. What is your first check?
*Tests: a mean pulled away from the median points at a few extreme values.*

- Recompute the median, since it should have doubled as well
- Report the mean, since it is the figure that uses every order
- Sort the amounts and read the few largest orders  <- correct
- Assume prices doubled and tell Finance to expect it
