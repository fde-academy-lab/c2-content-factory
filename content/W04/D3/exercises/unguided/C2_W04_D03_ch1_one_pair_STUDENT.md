# Can you read one pair's three numbers on paper?

Swiggy Instamart, Pune. The cart page's strip of three suggested items switched on Monday 7 September
2026 from a curated list to the items most often found in the same cart, and its click-through
(clicks over the times a slot was shown) fell from 6.1 percent to 3.8 percent. The analyst is ranking
the pairs the strip should show, from 40,000 carts placed from 1 to 28 September. Illustrative case:
the company is real, the situation and the data are synthetic, built for this class.

This is a fifteen-minute drill at the end of chapter 1, on paper, with no code.

**Who needs the answer.** The growth lead, who will put pairs in front of the category manager on
Friday. A pair read on the wrong count either wastes a slot or loses one that would have paid.

**The questions on the way.**

- What are the pair's three numbers, read from four counts?
- Which second route checks the lift?

Three words, defined once. **Support** is the share of carts holding both items. **Confidence** from
A to B is the share of A's carts that also hold B. **Lift** is the carts seen holding both, divided by
the carts chance alone would give (the total times A's share times B's share).

| Count | Carts |
|---|---|
| All carts | 40,000 |
| Carts holding coriander | 6,000 |
| Carts holding green chillies | 3,200 |
| Carts holding both | 1,440 |

**What you post.** Two letters in item order, with no spaces, in this shape:

```
Post exactly this shape: xx
```

---

## How do you read one pair's numbers by hand?

This comes up at work whenever someone asks "do people buy these together?" and the first honest
answer is three numbers from four counts.

### Q1. Which line gives the pair's support, the confidence from green chillies to coriander, and the lift, in that order?

*Level L1 · asked in every analytics interview.* Work each number from the table before you read the
options.

a) 3.6 percent, 0.24 and 3.00
b) 3.6 percent, 0.45 and 3.00
c) 15.0 percent, 0.45 and 3.00
d) 3.6 percent, 0.45 and 1.88

### Q2. Which second route would confirm the lift of 3.00 from a different pair of numbers?

*Level L2, a design call · asked in global capability centre interviews.* A second route reaches the same number
another way, to check the first.

a) 0.24 / 0.45, the confidence from coriander over the confidence from chillies
b) 3.6 percent / 15 percent, the pair's support over coriander's own share of carts
c) 0.45 / 0.15, chillies' confidence toward coriander over coriander's share
d) 1,440 / 3,200, the carts holding both over the carts holding green chillies
