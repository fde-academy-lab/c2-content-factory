# Can you make the seven concept calls on the canteen and the kirana?

A hostel canteen's twelve lunch orders and Sharma Kirana's month in Pune, both invented for the
concept chapters, carry seven items, one for each concept chapter. Items 1 to 4 are sat on paper
inside chapter 4, before the break, and items 5 to 7 inside chapter 9, after lunch. No code.

**Applies:** Support, confidence and lift, derived by counting (chapters 1 to 3, items 1 to 3); The
confidence trap; lift near one (chapter 4, item 4); Basket analysis on the order items (chapter 5,
item 5); The support floor and the watch list (chapter 6, item 6); Cross-sell and upsell reasoning;
expected value in rupees (chapter 9, item 7).

**Who needs the answer.** The canteen manager, who prints combo cards, and the kirana's owner, who
pays for one. A wrong letter here is a card printed on the wrong count, and each item names the
chapter to reread.

**The questions on the way.**

- Which denominator makes a support?
- Which way does a confidence read?
- What does chance give a pair, and what is its lift?
- What should a combo with the most popular item get?
- How many pairs does one order add?
- Which pairs earn a card once a floor is set?
- Which cost line did the kirana's owner forget?

Three words, defined once. **Support** is the share of all orders holding both items. **Confidence**
from A to B is the share of A's orders that also hold B. **Lift** is the orders seen holding both,
divided by the orders chance alone would give: all orders times A's share times B's share.

The canteen's twelve lunch orders, invented:

| Order | Items | Order | Items | Order | Items |
|---|---|---|---|---|---|
| T01 | dal rice, papad, chaas | T05 | dal rice, chaas | T09 | roti, sabzi, chaas |
| T02 | dal rice, papad, chaas | T06 | dal rice, curd, chaas | T10 | roti, sabzi, chaas |
| T03 | dal rice, papad, chaas | T07 | roti, papad, pickle | T11 | roti, sabzi, chaas |
| T04 | dal rice, sabzi, chaas | T08 | papad, pickle | T12 | gulab jamun, curd |

**What you post.** Seven letters in item order, with no spaces, in this shape:

```
Post exactly this shape: xxxxxxx
```

---

## Which counts answer which question on twelve orders?

This comes up at work whenever a shop asks which items to sell together: the first answer is a hand
count on a few bills, said with its denominator.

### Q1. Roti and sabzi share 3 orders. Which denominator turns that count into the pair's support?

*Level L1, a design call · chapter 1 · asked in every analytics interview.*

a) Roti's 4 orders, since roti is named first in the pair
b) All 12 orders, since support is a share of every basket
c) The 5 orders that hold roti, sabzi or both
d) The 8 orders found by adding roti's 4 orders to sabzi's 4 orders

### Q2. Sabzi is in 4 orders, chaas in 9 and both in 4. Which line gives the confidence from sabzi to chaas, then from chaas to sabzi?

*Level L1 · chapter 2 · asked in every analytics interview.*

a) 1.00, then 0.44: each divides by its own item's orders
b) 0.44, then 1.00: each divides by the other item's orders
c) 0.33, then 0.33: both divide by all twelve orders
d) 1.00, then 1.00: confidence reads the same both ways

### Q3. Papad is in 5 orders, pickle in 2 and both in 2. What does chance alone give the pair, and what is its lift?

*Level L2 · chapter 3 · asked in every analytics interview.*

a) 2 by chance, since both pickle orders hold papad, so lift 1.00
b) 0.83 by chance, so lift 0.42, the two kept apart
c) 0.17 by chance, the pair's support, so lift 12 on two orders
d) 0.83 by chance, so lift 2.40, above chance

### Q4. Every dal rice order holds chaas, and chaas is in 9 of the 12 orders. The manager wants a dal rice and chaas combo card: which call fits?

*Level L3, a design call · chapter 4 · asked in product-company interviews.*

a) Print it, since a confidence of 1.00 is the strongest bundle on the menu
b) Print chaas beside every item, since chaas goes with everything
c) Hold it: the lift is 1.33, since chaas was in most orders anyway
d) Take chaas off the menu, since it sells without any help

## How do order lines, floors and rupees change the call?

This comes up at work whenever a count becomes a decision: the table has to be built right, read
above a floor, and priced in rupees before money is spent.

### Q5. A party order arrives with dal rice, papad, chaas, curd and pickle. Counted once with sorted names, how many pairs does it add to the pairs table?

*Level L2 · chapter 5 · asked in data-engineering interviews.*

a) 10, one pair for each two of its five items
b) 5, one pair for each item on the bill
c) 20, every pair counted in both orders of its names
d) 25, every item paired with every item, itself included

### Q6. In the canteen's invented month of 600 orders, where no item depends on another, the manager sets a floor of 30 orders and a bar of 1.5. Which line sorts gulab jamun and jalebi (lift 8.57 on 2 orders), curd and fruit plate (lift 5.88 on 1 order) and an everyday pair at lift 1.00 on more than 30 orders?

*Level L4, a design call · chapter 6 · asked in product-company interviews.*

a) Promote, promote and ignore: the two strongest lifts take the board first
b) Watch, ignore and promote: one order is noise, and 30 orders earn the board
c) Promote, watch and ignore: two orders clear a floor that one order cannot
d) Watch, watch and trap: thin pairs earn a trial; the thick one is chance

### Q7. Sharma Kirana's owner prices the tea-and-rusk card at 18 new packs x Rs 12 = Rs 216, less Rs 20 of printing, so Rs 196 a month. Which cost line did the owner forget?

*Level L4, a design call · chapter 9 · asked in global capability centre interviews.* The card takes
Rs 1 off every bill holding tea and rusk; 150 bills held both before it, and 18 more hold both
after it.

a) The Rs 18 each rusk pack costs the shop, taken off the margin a second time
b) Rs 1 back on all 168 combo bills, the 150 that held both anyway among them
c) The rusk margin on the 150 bills that already held both before the card
d) The tea margin on the 18 bills that add a rusk pack because of the card
