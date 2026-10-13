# Which pairs beat chance, and what is each one worth?

Week 4 Wednesday. The five topics on a hostel canteen's twelve lunch orders and a Pune corner shop's month, both invented, then on Swiggy Instamart's Pune carts, whose strip fell from 6.1 to 3.8 percent click-through once it showed the items most often found in the same cart. Illustrative case: the company is real, the situation and the data are synthetic, built for this class.

## Panel 1: Support, confidence and lift, derived by counting: what does each answer?

![The canteen's 2 by 2: roti in 4 orders, sabzi in 4, both in 3, beside the table of counts](../whiteboards/C2_W04_D03_canteen_two_by_two_STUDENT.png)

| Count | It answers | Formula | Roti and sabzi |
|---|---|---|---|
| Support | How often together? | both / all | 3 / 12 = 0.25 |
| Confidence | How reliably, from A? | both / A | 3 / 4 = 0.75 |
| Lift | How far above chance? | both x all / (A x B) | 3 x 12 / (4 x 4) = 2.25 |

**Crux:** Lift is the baskets seen holding both over the baskets chance gives, the same from either side; it counts a pull and never names a cause.

## Panel 2: The confidence trap; lift near one: does 1.00 mean a bundle?

| Toward chaas, in 0.75 of orders | Confidence | Lift |
|---|---|---|
| dal rice, sabzi | 1.00 | 1.33 |
| roti | 0.75 | 1.00 |
| papad | 0.60 | 0.80 |

Lift cannot pass one over the share: 1.33 for chaas, 1.41 for milk, in 71 percent of carts.

**Crux:** The item in every basket makes a weak bundle partner: it was going in anyway.

## Panel 3: Basket analysis on the order items: how do lines make pairs?

```python
baskets = lines.groupby("order_id").item.apply(set)
pairs = Counter(p for b in baskets
                for p in combinations(sorted(b), 2))
```

k items make k x (k - 1) / 2 pairs: 33 lines make 30; both name orders count 60.

**Crux:** Sort the names so each pair has one key; the table holds counts, never a ranking.

## Panel 4: The support floor and the watch list: when is a pair too thin?

| Region | Rule | Canteen | Instamart |
|---|---|---|---|
| Promote | floor met, lift 1.5 up | roti and sabzi, 2.25 on 3 | chips and cold drink, 3.39 |
| Watch | lift 1.5 up, below floor | gulab jamun and curd, 6.0 on 1 | ice cream and sauce, 4.60 on 100 |
| Trap | floor met, near one | dal rice and chaas, 1.33 on 6 | milk's pairs, 0.99 to 1.04 |

**Crux:** Set the floor where luck stops passing the bar: 8 orders in the invented month, 400 carts.

## Panel 5: Cross-sell and upsell reasoning; expected value in rupees: what is a combo worth?

`value = margin on purchases it changes - discount on every bill that takes it - fixed cost`

Sharma Kirana: 18 packs x Rs 12 = Rs 216, less Rs 168 handed back, less Rs 20 = Rs 28 a month; at 2 percent, -Rs 71. Rusk sales on every combo bill read Rs 5,040.

**Crux:** Cross-sell adds a second item, upsell a dearer one; each earns only on what it changes.

## Panel 6: The case: what did Instamart's carts say?

Bread to milk read confidence 1.00 and lift 1.50 on twelve carts, and 0.74 and 1.04 on 40,000. The fall: 0.5 x 1.2 + 0.5 x 6.4 = 3.8 percent. A slot earns Rs 17,280 a day against Rs 3,240 showing milk; taking milk out recovers about Rs 6.3 lakh a month, gross, since every suggestion but milk clicked alike.

**Crux:** Say the base rate, the floor and the cost line, and end on one decision.

## Panel 7: How do the five topics join?

Three counts (0.25, 0.75, 2.25), then the trap (1.33 behind a confidence of 1.00), then the pairs table (30 pairs from 33 lines), then the floor (8 orders in the month), then the rupees (Rs 28): each counted on the canteen or the kirana first.

**Crux:** Every topic was counted by hand before Instamart's carts used it.
