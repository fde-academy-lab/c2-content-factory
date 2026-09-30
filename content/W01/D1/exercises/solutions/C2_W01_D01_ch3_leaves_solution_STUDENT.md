# Solution: chapter 3, the leaves, counted

Answers: 1c 2d 3b 4b 5d

## The idea being tested

A row is an order and a customer is an id. Counted by rows, orders per customer reads 1.00 and
"nobody comes back" makes acquisition look like the only branch; counted by distinct ids it is 30 /
23 = 1.30, and 7 customers came back. The dictionary of counts fills both customer branches in one
pass; a set is enough when only the count is asked; the warehouse's COUNT(DISTINCT) takes over at
scale.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | c | A set counts distinct ids, a dictionary keeps a count per id, the `&` of two sets keeps the ids both hold, and the row count is the order count. | a uses the row count for customers, the chapter's trap. b and d swap the set and the dictionary, which answer different questions. |
| 2 | d | "Nobody comes back" says frequency is dead, so buying customers looks like the only way to grow, which is marketing's Rs 12 crore. | a is chapter 1's cancellations. b is chapter 4's question. c has nothing to do with the count. |
| 3 | b | At 4 crore rows the data stays where it lives and the database counts it; Week 2 teaches it. | a works and is the wrong tool at that size. c is the trap at any size. d is impossible by hand. |
| 4 | b | With nobody keeping three orders, 21 orders less 19 customers is 2 customers with two orders. | a and d are the booked and not-cancelled answers. c counts every customer. |
| 5 | d | A set answers "how many" in one line; the dictionary earns its extra line when the question becomes "how many came back". | a is the trap. b works and is more than the ask. c is error-prone and has nothing to do with size. |

## The part worth arguing about

Item 4. The shortcut, orders less customers, holds only when nobody has three orders. The
dictionary is the count to trust, and the stem says why the shortcut is safe here.

**Kavya's review.** "The division was fine; the denominator was a guess. Count people by their ids."

## Where the pattern lives in production

Reliance Retail reports 396 million registered customers. Registered, active and ordering are three
denominators, and each gives a different rate for the same orders.

## Hands-on

Notebook 03 prints 23 customers, 1.30 orders each, 7 came back, and 2 on delivered orders.
