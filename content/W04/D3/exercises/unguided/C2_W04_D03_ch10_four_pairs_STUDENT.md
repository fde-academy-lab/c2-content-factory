# Which of four pairs earn a strip slot when lift and support are read together?

Swiggy Instamart, Pune. Since Monday 7 September 2026 the cart page's three-slot strip has shown the
items most often found in the same cart, and its click-through (clicks over the times a slot was
shown) fell from 6.1 percent to 3.8 percent. The analyst has computed every pair across 40,000
September carts and must now say which pairs fill the strip. Illustrative case: the company is real,
the situation and the data are synthetic, built for this class.

This is a four-minute paper check that opens chapter 10, sat as its first prediction, with no code.

**Applies:** The support floor and the watch list (chapter 6, items 1, 3 and 4), with lift from chapter
3; The confidence trap; lift near one (chapter 4, item 2).

**Who needs the answer.** The growth lead, who will defend three slots at Friday's review against a
category manager who wants milk in every one of them. A slot given to the wrong pair costs margin on
every cart page where it shows.

**The questions on the way.**

- Which pairs earn a slot under a stated rule?
- What goes wrong if the pairs are ranked by how often they appear?
- What should happen to a strong pair on very few carts?
- Why sit the floor at 1 percent of carts?

Two terms, defined once. **Support** is the share of carts holding both items. **Lift** is the carts
seen holding both over the carts chance alone would give; 1 means chance. The **support floor** is
the fewest carts a pair must sit in before it may take a slot: 1 percent of 40,000 carts is 400.

| Pair | Support | Lift |
|---|---|---|
| chips, cold drink | 5.0 percent | 3.39 |
| ice cream, chocolate sauce | 0.25 percent | 4.60 |
| bread, toned milk | 25.2 percent | 1.04 |
| onions, tomatoes | 7.5 percent | 1.70 |

Across all pairs, 1,221 have support of at least 0.1 percent, 40 carts, and 246 have support of at
least 1 percent.

**What you post.** Four letters in item order, with no spaces, in this shape:

```
Post exactly this shape: xxxx
```

---

## Which pairs earn a slot, and what happens to the rest?

This comes up at work whenever a ranked list decides what a customer sees: the rule has to say how
strong and how common a pair must be before it gets the space.

### Q1. Under the rule "support at least 1 percent and lift at least 1.5", which pairs earn a slot?

*Level L3, a design call · asked in product-company interviews.*

a) Chips and cold drink alone, the only pair above a lift of 3
b) Ice cream and chocolate sauce, then chips and cold drink
c) Chips and cold drink, then onions and tomatoes
d) Every pair except bread and milk, ranked by lift

### Q2. A colleague ranks the four pairs by support: which pair tops the list, and why is that the wrong slot?

*Level L3 · asked in every analytics interview.*

a) Bread and milk: support follows milk's popularity, and a lift of 1.04 is chance
b) Onions and tomatoes: a support of 7.5 percent is too thin to earn a slot on its own
c) Chips and cold drink: support rewards whichever pair beats chance by the most
d) Ice cream and chocolate sauce: support leaves every thin pair out of the ranking

### Q3. What should happen to ice cream and chocolate sauce?

*Level L5, a design call · asked in product-company interviews.*

a) A slot today, since a lift of 4.60 leads the four pairs by a clear gap
b) The watch list: a two-zone trial with a pass rule fixed before it starts
c) Nothing at all, since any pair below the floor is noise and nothing more
d) A floor lowered to 0.25 percent, so that the pair qualifies for a slot today

### Q4. Why does the floor sit at 1 percent of carts rather than at 0.1 percent?

*Level L5, a design call · asked in global capability centre interviews.*

a) At 0.1 percent, 1,221 pairs pass, many on about 40 carts, where lift moves by luck
b) At 0.1 percent, chips and cold drink would fall under the line and lose their slot
c) At 1 percent, every pair holding milk drops out of the ranking at once
d) At 1 percent, the strip keeps only the pairs the category manager already knows
