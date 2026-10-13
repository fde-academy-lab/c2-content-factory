# Can you run the pairs method on a store you have never seen?

The practice set for the TA-led lab, after the Kalpa lab notebook. It moves the day's method to an
invented store so the counts are small enough to do by hand: a Nagpur hardware shop's 200 bills
from one week, and four pairs and three bundles from an invented quick-commerce strip. Every number on this
page is invented for practice. The items climb from a hand count to a call a merchandiser, the person
who decides which products are bundled and promoted, would pay for. Uplift, used in item 6, is the
extra sales a promotion causes beyond what would have sold anyway.

**Applies:** Support, confidence and lift, derived by counting (chapters 1 to 3, items 1 and 2); The
confidence trap; lift near one (chapter 4, items 2 and 6); Basket analysis on the order items (chapter
5, item 5); The support floor and the watch list (chapter 6, items 3 and 6); Cross-sell and upsell
reasoning; expected value in rupees (chapter 9, items 4 and 6).

**Who needs the answer.** You, before tomorrow: the same three counts and the same rupee line return
on Saturday's paper and in every basket question an interviewer asks.

**The questions on the way.**

- What are a pair's three numbers from four counts?
- What does a lift of exactly one say?
- Which of four pairs earn a slot?
- What does a slot earn once a discount is paid?
- In what order do the counting lines run?
- Which of three bundles runs first, and why?

Three words, defined once. **Support** is the share of bills holding both items. **Confidence** from
A to B is the share of A's bills that also hold B. **Lift** is the bills seen holding both over the
bills chance alone would give, which is the total times A's share times B's share.

| The hardware shop's week, invented | Bills |
|---|---|
| All bills | 200 |
| Bills with paint | 90 |
| Bills with brushes | 50 |
| Bills with paint and brushes | 28 |
| Bills with sandpaper | 80 |
| Bills with sandpaper and paint | 36 |

**What you post.** Six letters in item order, with no spaces, in this shape:

```
Post exactly this shape: xxxxxx
```

---

## What do the counts say about paint, brushes and sandpaper?

This comes up at work in every first pass over a basket table: four counts, three numbers, one
sentence.

### Q1. What is the lift of paint and brushes?

*Level L1 · asked in every analytics interview.*

a) 0.56
b) 0.31
c) 1.24
d) 0.14

### Q2. Sandpaper and paint read a lift of exactly 1.00: what does that say?

*Level L2 · asked in product-company interviews.*

a) Sandpaper and paint turn up together exactly as often as chance would put them
b) Sandpaper brings paint 45 percent of the time, which makes the pair a strong bundle
c) Every bill with sandpaper also holds paint, so the pair cannot be separated
d) The pair turns up less often than chance, so the two items compete

## Which pairs and bundles earn the strip's space?

This comes up at work whenever a list of pairs has to become a decision with a cost attached.

| Invented pair | Support | Lift |
|---|---|---|
| A | 12 percent | 1.05 |
| B | 4 percent | 2.6 |
| C | 0.4 percent | 6.0 |
| D | 2 percent | 1.8 |

### Q3. Under the rule "support at least 1 percent and lift at least 1.5", which reading of the four pairs is right?

*Level L3, a design call · asked in global capability centre interviews.*

a) C, then B, then D take slots, and A is left out as no better than chance
b) B and D take slots; A is a trap near one; C goes on the watch list
c) A and B take slots, since both clear the support floor
d) B, C and D take slots, since each lift clears 1.5

### Q4. A slot is shown 30,000 times a day at 5 percent click-through; half the clicks become adds, an add earns Rs 10 margin and the bundle gives Rs 3 back on each: what does the slot earn a day?

*Level L5 · asked in product-company interviews.* The added item sells for Rs 30.

a) Rs 7,500
b) Rs 5,250
c) Rs 15,000
d) Rs 22,500

### Q5. In what order do these four lines run to count every pair?

*Level L2, a design call · asked in coding rounds for analyst roles.*

```text
1  lift = pair_count[(a, b)] * len(baskets) / (single[a] * single[b])
2  baskets = items.groupby("cart_id").item.apply(set)
3  single = Counter(x for b in baskets for x in b)
4  pair_count = Counter(p for b in baskets for p in combinations(sorted(b), 2))
```

Take `a` and `b` as the two items being checked, already set. Which order runs without an error
and counts every pair?

a) 2, 3, 4, 1
b) 3, 2, 4, 1
c) 2, 1, 3, 4
d) 4, 2, 3, 1

### Q6. A merchandiser offers three bundles: X (lift 1.02, support 30 percent), Y (lift 2.4, support 3 percent, Rs 12 margin an add) and Z (lift 5.0, support 0.2 percent). Which plan runs first?

*Level L5, a design call · asked in product-company interviews.*

a) Z first, since its lift is the highest of the three and repays a discount fastest
b) X first, since it reaches the most bills of the three and needs no trial at all
c) Y first, priced with an uplift assumption and its range; Z watched; X left alone
d) All three at once, so that one week of sales shows which of them really works
