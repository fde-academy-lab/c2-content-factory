# Kahoot, Week 1 Monday

Eight items, ungraded, scored on correctness and speed together. There is no return question today,
because Monday is the first teaching day of the week and there is no earlier day to return to.

Each item names what it tests, so an item dropped for time says what was lost.

---

## Q1. Kalpa's revenue fell while its number of customers rose. Which branch do you open first?
*Tests: the tree's multiplication, read backwards from a result.*

- Customers, since that is the branch that visibly moved this quarter
- Revenue per customer, since it must have fallen by more than customers rose  <- correct
- Price per item alone, since price is always the first suspect
- None yet, since revenue can fall for no reason in any quarter

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

- True, since 3500 is the larger of the two numbers
- False, since text always sorts below any number
- It depends on whether the text holds only digits
- An error: text and a number cannot be ordered  <- correct

---

## Q4. The mean order is Rs 9,800 and the median order is Rs 1,400. What does that say about the orders?
*Tests: a wide gap between the mean and the median is itself a finding.*

- A few orders sit far above the rest  <- correct
- Most orders sit close to Rs 9,800 each
- The median was computed on the wrong column
- The file must hold fewer than ten orders

---

## Q5. A fresh kernel runs the cells in the order 3, 1, 2. Cell 1 loads ORDERS and cell 3 uses it. What happens?
*Tests: the kernel knows what it ran, never what the page shows.*

- It works, since the page shows cell 1 above cell 3
- Cell 3 raises a NameError, since ORDERS is not made yet  <- correct
- Cell 1 raises an error, since it ran second in the order
- Nothing prints, since the kernel skips cells run out of order

---

## Q6. Fifteen percent off lifts quantity 10 percent. Did revenue rise or fall?
*Tests: branches multiply, and a discount needs more volume than its cut.*

- Rise, to 1.10 of today, since the quantity is up 10 percent
- Rise, by 25 percent, since both changes help the shopper
- Fall, to 0.935 of today, since 0.85 times 1.10 is 0.935  <- correct
- Stay level, since the discount and the quantity cancel out

---

## Q7. A loop counted 30 customers in a file of 30 orders. What is the likeliest mistake?
*Tests: a row is an order, and a customer is counted by a distinct id.*

- It counted rows, so a customer with two orders counts twice  <- correct
- None, since each order in a file comes from its own customer
- It skipped the cancelled orders, which belong to other customers
- It counted the channels, since each order carries one channel

---

## Q8. Customers rise 10 percent and orders per customer rise 10 percent. What happens to revenue?
*Tests: lifts multiply along the tree, so two 10 percent lifts make 21 percent.*

- Up 20 percent, since the two lifts add together
- Up 10 percent, since only one of the lifts counts
- Up 11 percent, one lift and a tenth of the other
- Up 21 percent, since 1.10 times 1.10 is 1.21  <- correct
