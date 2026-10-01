# When payments are attached to orders, which rows does each join keep, drop or repeat?

The chapter 1 set has six items, each a question Anand, his analyst or the platform lead would ask.
Items 1 and 2 close the chapter live; the rest open the TA-led practice lab or are worked tonight. The
tables below are invented for this set, so none of its numbers comes from the chapter.

> **The client asks.** "Show me, order by order, what we actually collected against what we booked in
> Q2. If there is a gap, I want to know which orders and which channel."
>
> Anand Iyer, finance controller, Kalpa Retail

## What do you need to know before the items?

**Who needs the answer.** Anand's analyst audits the statement line by line, and you sign the
collected number. A join that drops an unpaid order hides it from the collections team.

**The questions on the way.**

- How many rows does the INNER join return?
- What does the LEFT join, orders first, add?
- Which query answers the platform lead's question?
- What is wrong with a statement that reads 116 percent collected?
- How many rows will a FULL join return, from the key counts alone?
- Which question is an INNER join the honest choice for?

An item marked Design asks for the best-fit approach, a sizing, the fact that would switch it, or the second route.

- **Booked** is every order at its amount. **Collected** is the cash that arrived, each payment counted
  once. **Posted** is every payment row the feed holds, repeats included. A **retry** is one payment
  the gateway posted twice.
- The **grain** of a table is what one row stands for: one order in `orders`, one payment event in
  `payments`.
- **INNER JOIN** keeps only the pairs that match. **LEFT JOIN** keeps every row of the table named
  first, with NULL where nothing matched. **RIGHT JOIN** keeps every row of the table named second.
  **FULL OUTER JOIN** keeps both sides. NULL is SQL's mark for "no value here".

The invented `orders`:

| order_id | channel | amount |
|---|---|---|
| A-1 | app | 1,200 |
| A-2 | web | 900 |
| A-3 | store | 2,400 |
| A-4 | app | 600 |

The invented `payments`:

| payment_id | order_id | amount | instalment_no |
|---|---|---|---|
| Q-1 | A-1 | 1,200 | 1 |
| Q-2 | A-2 | 900 | 1 |
| Q-3 | A-2 | 900 | 1 |
| Q-4 | A-3 | 1,400 | 1 |
| Q-5 | A-3 | 1,000 | 2 |
| Q-6 | A-7 | 500 | 1 |

Post one line, six letters in item order, no spaces:

```
Post exactly this shape: xxxxxx
```

---

### Q1. How many rows does the INNER join return?

`orders o JOIN payments p ON p.order_id = o.order_id`, on the two tables above. How many rows come back?

a) 4, one row for each order, A-1 to A-4
b) 5, as A-2 and A-3 each come out twice
c) 6, one row for each payment, Q-1 to Q-6
d) 3, one row each for A-1, A-2 and A-3

### Q2. What does the LEFT join, orders first, add?

`orders o LEFT JOIN payments p ON p.order_id = o.order_id`. Which order carries NULL payment columns, and how many rows does the join return?

a) A-4, and 6 rows
b) A-7, and 6 rows
c) A-4, and 5 rows
d) no order, and 7 rows

### Q3. Which query answers the platform lead's question? (Design)

The data platform lead owns the payments feed and asks: "How many payment rows in the feed sit on an order id we never booked?" A teammate tries four ways on the two tables above. Which way, with the count it reports, answers him?

a) orders LEFT JOIN payments, rows with no payment: 1
b) payments JOIN orders, rows with no order: 0
c) payments LEFT JOIN orders, rows with no order: 1
d) payment rows less order rows, 6 less 4: 2

### Q4. What is wrong with a statement that reads 116 percent collected?

A teammate starts the statement from `payments` and attaches each payment's order. It shows 6 lines and 5,900 of cash against 5,100 booked, so it reads as 116 percent collected. Which reading of it is right?

a) A-4 is missing, and A-2's retry and A-7's 500 sit in the cash
b) A-3's two instalments are one payment, counted twice here
c) the cash is right, since customers may pay before booking
d) A-7 is an order paid in advance, and it belongs on the statement

### Q5. How many rows will a FULL join return, from the key counts alone? (Design)

Before running any join on a new pair of tables, you count keys. Order X appears once in `orders` and three times in `payments`. Order Y appears once in `orders` and never in `payments`. Key Z never appears in `orders` and twice in `payments`. How many rows does a FULL OUTER JOIN return for these three keys?

a) 4
b) 5
c) 6
d) 7

### Q6. Which question is an INNER join the honest choice for? (Design)

A teammate answers four questions from the rows of `orders o JOIN payments p ON p.order_id = o.order_id` on the tables above, and writes beside each the figure those rows give. For which question is that figure also the true answer?

a) app orders booked: 1
b) share of booked orders paid: 100 percent
c) payment rows with no booked order: 0
d) store cash received: 2,400

---

## Where does this skill come back?

It comes back in chapter 2 on Kalpa's Q2, where the same LEFT JOIN meets a key that repeats, and in
the second case, where the platform lead's question starts from `payments`. The notebook for this
chapter is `notebooks/C2_W02_D02_01_what_a_join_keeps_STUDENT.ipynb`.
