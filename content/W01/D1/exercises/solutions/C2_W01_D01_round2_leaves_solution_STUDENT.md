# Solution: count the leaves

Answers: 1c 2a 3b 4d 5a 6c 7b

## The idea being tested

A row is an order, and a customer is an id. Counting rows as customers gives 30, so orders per
customer reads 30 over 30, which is 1.00, and the sentence "nobody comes back" writes itself. That
sentence makes acquisition look like the only branch and supports the Rs 12 crore. The check is one
line: the number of rows against the number of distinct ids. The file has 23 customers, so orders
per customer is 1.30, and 7 customers bought twice, which is 30 percent of customers. Frequency is a
live branch, and it has to be examined before money goes to acquisition.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | c | The claim rests on 30 customers, and the fastest test of that is rows against distinct ids; if they differ, the 1.00 falls. | a: a count by status is round 1's check, and it cannot turn 30 rows into fewer customers. b: mean and median describe the order value, a different leaf. d: asking marketing assumes the claim it should be testing. |
| 2 | a | A set keeps each id once, so its length is the number of distinct customers: 23. | b is the row count, which a list would give. c counts ids seen once, which needs a dictionary of counts. d counts ids seen twice, which also needs the counts. |
| 3 | b | Orders over distinct customers, both on the same 30 booked orders: 30 over 23 is 1.30. | a divides booked orders by the customers on a different definition, so the numerator and denominator disagree. c is the trap, rows as customers. d is the rate upside down. |
| 4 | d | 7 of the 23 customers bought twice, which is 30 percent. | a divides customers by rows. b divides orders by orders, a share of orders rather than of customers. c is the share who did not come back. |
| 5 | a | A third of customers came back inside one quarter, so frequency is a branch that can move, and it costs retention rather than marketing. | b reads "most bought once" as proof, when 30 percent returning in one quarter is a live branch. c jumps from a shape to a spend with no second window. d treats 1.30 as noise, when it is 30 percent more orders than the trap claimed. |
| 6 | c | "Came back" means two or more orders, and no customer in the file has more than two, so > 2 finds none; >= 2 finds 7. | a counts every customer, 23. b removes orders and can only lower the repeat count. d changes the container and leaves the wrong threshold. |
| 7 | b | Delivered orders are 21, the distinct ids on them are 19, and 21 over 19 is 1.11. | a divides delivered orders by booked customers. c is the booked quarter, a different definition. d counts delivered rows as customers, the trap on a new definition. |

## The part worth arguing about

Item 5. Some will say 1.30 is low and proves marketing's point. Low compared with what? With one
quarter there is no earlier number to compare against, so the only fair reading is that frequency
exists and has not been measured moving. That is a reason to look at it before spending Rs 12 crore
on a different branch, and it is the sentence the afternoon builds on.

**Kavya's review.** "Before you divide by customers, prove you counted customers. The row count is
never the customer count until you have checked."

## Where the pattern lives in production

Every table that records events rather than people carries this trap: orders, sessions, tickets,
transactions. A product analyst checks count of rows against count of distinct users before any
per-user metric, and a SQL reviewer asks for COUNT(DISTINCT customer_id) the moment a denominator
says "customers". Week 2 meets the same trap in Postgres.

## Hands-on

Level 4 of `notebooks/C2_W01_D01_02_counting_leaves_STUDENT.ipynb` prints 23 customers and 1.30
orders per customer on booked orders, and 21 orders, 19 customers and 1.11 on delivered, which
confirm Q2, Q3 and Q7.
