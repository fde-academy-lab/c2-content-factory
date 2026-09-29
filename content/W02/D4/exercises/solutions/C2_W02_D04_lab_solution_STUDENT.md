# Solution: the practice lab

Answers: 1c 2a 3d 4b 5a 6c 7b 8d 9a

## Problems 1 and 2, item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | c | The customer list has six cities: Bengaluru, Chennai, Delhi, Hyderabad, Mumbai and Pune. | a and d confuse the group with its members. b is the segment split. |
| 2 | a | Two keys give one row per pair that exists: 471 customer-quarter pairs have orders. | b and c assume every customer ordered in both quarters. d counts orders, not pairs. |
| 3 | d | Three channels down the side, two quarters across. | a swaps index and columns. b is the long form. c is `transform`. |
| 4 | b | One row per customer who ordered, two named measures. | a assumes customers with no orders appear. c transposes. d is `transform`. |
| 5 | a | Three teams reading one list from one source is what the warehouse is for. | b and c make three copies. d is a pasted copy nobody can rerun. |
| 6 | c | One question, asked once, answered by changing one line on the customer table. | a builds a warehouse object for a question asked once. b uses a stale export. d rebuilds what pandas does in a line. |
| 7 | b | A reviewer following step by step sees both dates and both subtractions. | a, c and d show the two counts without showing why they differ. |
| 8 | d | Finance reconciles against its books, so the number lives where Finance can rerun it. | a and c are copies. b is a hand-updated copy with no trail. |
| 9 | a | A one-off list, matched this afternoon, with the fan-out guarded. | b is too slow for a one-off. c looks up into a stale export. d rebuilds a merge by hand. |

## Problem 3, the self-check

```python
ch = orders.pivot_table(index="customer_id", columns="channel", values="order_id",
                        aggfunc="count", fill_value=0).reset_index()
t = customers.merge(ch, on="customer_id", how="left", validate="one_to_one")
counts = t[["app", "store", "web"]].fillna(0).astype("int64")   # the merge left NaN for 39
t = t.assign(favourite=counts.idxmax(axis=1).where(counts.sum(axis=1) > 0))
ties = int((counts.eq(counts.max(axis=1), axis=0).sum(axis=1) > 1)[counts.sum(axis=1) > 0].sum())
```

| Check | Value |
|---|---|
| rows | 340, one per customer on the list |
| customers with no orders, favourite left empty | 39 |
| favourite, before any tie rule | app 149, store 92, web 60 |
| customers whose favourite is a tie | 98 |

The `fillna(0)` matters twice: the left merge gives the 39 customers with no orders `NaN` in
every channel column, and on pandas 3 `idxmax` raises `ValueError: Encountered all NA values` on
such a row. That error gets its two minutes; the tie is the real trap.

A tie rule to give the growth team: "Where two channels are tied, the favourite is the channel of
the customer's most recent order." Whatever the rule, it is written down, because `idxmax`
silently picks the first column and would settle 98 ties by the order of the columns rather
than by any rule the growth team chose.

## Problem 4, the self-check

| Check | Value |
|---|---|
| rows | 340 |
| Q2 spend, equal to the Q2 book | Rs 9,84,00,000 |
| Q2's last order date | 28 September 2026 |
| smallest recency | 0 days |
| customers with no Q2 order | 113 |
| 30-day win-back list, from 28 September | 109 customers |
| the same list, from 19 October | 180 customers |

The 113 customers with no Q2 order have no recency in this table and sit on neither list, which
is a decision worth saying aloud: a customer who bought in Q1 and not in Q2 is exactly who a
win-back is for, and the Q2-only table cannot see them. That is the argument for the full
two-quarter table the escalated case built.
