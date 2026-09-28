# Kahoot, Week 1 Monday

Six items, ungraded, scored on correctness and speed together. There is no return question today,
because there is no earlier day of Week 1 to return to.

Each item names what it tests, so an item dropped for time says what was lost.

---

## Q1. Revenue fell while the number of customers rose. Where do you look first?
*Tests: the tree's multiplication, read backwards from a result.*

- Customers, because that is the branch that visibly moved
- Revenue per customer, which must have fallen by more  <- correct
- Price per item alone, since price is the usual suspect
- Nowhere yet, since revenue can fall for no reason at all

---

## Q2. Orders per customer is what, divided by what?
*Tests: a rate carries its denominator, and both sides share one window.*

- Customers divided by orders, in the same window
- Orders divided by every customer ever on record
- Orders divided by distinct customers, same window  <- correct
- Revenue divided by orders, which is the same rate

---

## Q3. In Python, what does "3500" > 3000 give you?
*Tests: the type decides what an operation means, before the size does.*

- True, since 3500 is the larger of the two
- False, because text sorts after every number
- True, because Python converts the text to a number
- An error: text and a number cannot be ordered  <- correct

---

## Q4. Mean order Rs 9,800, median order Rs 1,400. What does that say?
*Tests: a wide gap between the mean and the median is itself a finding.*

- A few orders sit far above the rest  <- correct
- Most orders sit close to Rs 9,800 each
- The median was computed on the wrong column
- The file must hold fewer than ten orders in all

---

## Q5. A fresh kernel runs the cells in the order 3, 1, 2. Cell 1 loads ORDERS and cell 3 uses it. What happens?
*Tests: the kernel knows what it ran, never what the page shows.*

- It works, because the page shows cell 1 above cell 3
- Cell 3 raises a NameError, since ORDERS is not made yet  <- correct
- Cell 1 raises an error, because it ran second
- Nothing prints, since the kernel skips cells out of order

---

## Q6. Fifteen percent off, and 10 percent more items sold. Did revenue rise or fall?
*Tests: branches multiply, and a discount needs more volume than its cut.*

- Rise, to 1.10 of today, since volume is up 10 percent
- Rise, by 25 percent, since both changes help the shopper
- Fall, to 0.935 of today, since 1.10 times 0.85 is 0.935  <- correct
- Stay level, since the discount and the volume cancel out
