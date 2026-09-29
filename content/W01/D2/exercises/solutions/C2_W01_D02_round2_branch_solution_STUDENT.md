# Solution: round 2, which branch moved?

Answers: 1c 2b 3d 4a 5a 6b 7c 8d

## The idea being tested

A change in revenue decomposes along the tree: customers, times orders per customer, times revenue
per order. On the two closed quarters, customers held at 69, orders per customer fell from 1.65 to
1.25, and revenue per order rose from Rs 1,84,211 to Rs 2,17,442. The product of the three ratios,
1.000 times 0.754 times 1.180, is 0.890, which is Rs 1,87,00,000 over Rs 2,10,00,000, so the tree
accounts for the whole fall. The discount branch is where a missing field tempts a zero, and a zero
there reverses the direction of the finding.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | c | 114 over 69 is 1.65 and 86 over 69 is 1.25; the change against Q1 is 24.6 percent. | a divides customers by orders, which is the rate upside down. b measures the fall against Q2's figure. d counts customers where it should count orders. |
| 2 | b | Customers held, so acquisition is the branch that did not move; the fall sits in frequency, and a rise in order value softened it. | a reads a rising branch as proof about a flat one. c: the export's totals are exact, and the tree explains them. d: the product of the branches says exactly how much each contributed. |
| 3 | d | The branches multiply, and 0.890 equals the revenue ratio, so the decomposition is complete. | a adds ratios that multiply. b: the frequency branch alone is 0.754, and 0.890 is the product of all three. c names one factor as if it were the product. |
| 4 | a | 69 times less 0.4058 is 28 fewer orders, and 28 times Rs 1,84,211 is Rs 51,57,895. | b is the whole fall, which nets two branches. c prices the orders at Q2's value, which double counts the order-value branch. d is the order-value branch, which is a gain of Rs 28,57,895. |
| 5 | a | `.get("discount", 0)` turns "not recorded" into "no discount", so both totals are floors. Over the orders that record the field, discount per order rose from Rs 60.98 to Rs 76.67, the opposite direction to the report. | b repeats the misleading number. c changes the statistic and keeps the zero. d removes real orders from revenue to tidy a discount column. |
| 6 | b | Rs 180 over the three invented orders that record a value is Rs 60, and the fourth is reported as not recorded. | a counts the absence as a zero. c drops a recorded zero, which is a real value. d refuses a number the recorded orders can give. |
| 7 | c | Even if every Q2 order carried the largest recorded discount, 86 times Rs 150 is Rs 12,900, which is under 1 percent of the Rs 23,00,000 fall. | a uses the floor as if it were the value. b quotes a change in a floor as a share of the fall. d: a bound needs only the largest recorded value. |
| 8 | d | 81 over 54 is 1.50 and 57 over 50 is 1.14; frequency still carries the fall on Anand's definition. | a: customers fall a little on delivered orders, far less than frequency. b: revenue per order rises by 26.0 percent, which softens the fall. c: an 11.3 percent fall decomposes like any other. |

## The part worth arguing about

Item 5. The hurried fix makes the KeyError go away, and a notebook that runs feels like a notebook
that is right. The default in `.get()` is a decision about what an absence means, and it belongs in
a written line: absent means not recorded, reported separately, never summed as zero. How many
orders lack the field is the count you made in your own notebook, and it is the first line of that
note.

## Where the pattern lives in production

Revenue decomposition is the first model a finance or growth team builds, and it appears in
interviews as "revenue fell 11 percent, how do you split the change?". Missing fields turn up in
every export that joins two systems: a loyalty table that records a discount only when one was
applied, an app event that logs a field only on newer versions. Teams that fill them with zero
publish floors as facts, and the fix is the same everywhere: count the absences, report them, and
bound what they could change.

## Hands-on picks

Round 2's notebook, `notebooks/C2_W01_D02_02_which_branch_STUDENT.ipynb`, prints every figure in
the table above. Its your-turn cells have no letters to post; the count of orders without a
discount field is yours to make there.
