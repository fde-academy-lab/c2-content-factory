# How do three counts read for two pairs on twelve Instamart carts?

Swiggy Instamart, Pune. The cart page shows a strip of three suggested items. On Monday 7 September
2026 the strip began showing the items most often found in the same cart, and its click-through
(clicks over the times a slot was shown) fell from 6.1 percent to 3.8 percent. The analyst must rank
the pairs the strip should show. Illustrative case: the company is real, the situation and the data
are synthetic, built for this class.

The trainer builds this set with the room. The first item is fully worked, the second half worked,
and the third is yours.

**Who needs the answer.** The category manager, who picks what the strip may suggest. A pair read on
the wrong count takes one of the three spaces under every cart.

**The questions on the way.**

- How do support, confidence and lift read for bread and milk?
- What does lift say for chips and cold drink, and what does it not say?
- What should anyone do with a lift of 12 on one cart?

Three words, defined once. **Support** is the share of carts holding both items. **Confidence** from
A to B is the share of A's carts that also hold B. **Lift** is the carts seen holding both, divided by
the carts chance alone would give: the total times A's share times B's share. A lift of 1 means the
two items turn up together exactly as often as chance would put them there.

These are twelve of the 40,000 Pune carts.

| Cart | Items held |
|---|---|
| C000098 | toned milk, bread, eggs, bananas, coriander, onions, potatoes |
| C003216 | toned milk, bread, eggs, curd, bananas |
| C006334 | toned milk, bread, curd, paneer, onions |
| C009452 | toned milk, bread, eggs, tomatoes |
| C012570 | toned milk, eggs, chips, cold drink, onions |
| C015688 | toned milk, chips, cold drink, coriander |
| C018806 | toned milk, bananas, onions, potatoes |
| C022633 | toned milk, paneer, coriander, tomatoes |
| C026803 | chips, coriander, onions, potatoes |
| C030743 | cold drink, curd, bananas, tomatoes |
| C033861 | eggs, ice cream, chocolate sauce |
| C036979 | curd, onions |

**What you post.** Three letters in item order, with no spaces, in this shape:

```
Post exactly this shape: xxx
```

---

## How do the three counts read when you count by hand?

This comes up at work whenever a product team asks which items "go together": the first answer is a
hand count on a few rows, before any code.

### Q1. Which line gives bread and milk's support, confidence from bread to milk, and lift, in that order?

*Level L1 · asked in every analytics interview.* Worked: bread is in 4 carts and milk in 8, and all 4
bread carts hold milk. Support is 4 of 12. Confidence from bread to milk is 4 of 4. Chance alone
puts milk in 12 x 4/12 x 8/12 = 2.67 of the bread carts, so lift is 4 / 2.67. Which line matches the
working?

a) 0.33, 0.50 and 1.50
b) 0.67, 1.00 and 1.00
c) 0.33, 1.00 and 1.50
d) 0.33, 1.00 and 0.67

### Q2. What is the lift of chips and cold drink on the twelve carts, and what does it say?

*Level L1 · asked in every analytics interview.* Half worked: chips is in 3 carts, cold drink in 3, both
in 2. Chance alone puts both in 12 x 3/12 x 3/12 = 0.75 carts. Finish the count: which line is right?

a) 0.67: two of the three chips carts hold a cold drink
b) 2.67: the pair turns up 2.67 times as often as chance would put it
c) 2.67: chips make a shopper 2.67 times as likely to buy a cold drink
d) 0.17: two of the twelve carts hold both items

### Q3. Ice cream and chocolate sauce share one cart of the twelve, so lift reads 12: which call fits?

*Level L1, a design call · asked in product-company interviews.* Yours to do: decide what the number
justifies before anyone acts on it.

a) Give the pair a strip slot, since 12 is the highest lift on the cards
b) Drop the pair, since a lift above ten must be a data error
c) Run the pair in the evening only, when ice cream sells most
d) Hold the call until the full data counts the pair on enough carts
