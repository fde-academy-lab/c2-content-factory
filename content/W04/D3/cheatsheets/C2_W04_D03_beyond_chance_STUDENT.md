# Which pairs beat chance, and what is a strip slot worth?

Swiggy Instamart, Pune, Week 4 Wednesday. The cart page's strip fell from 6.1 to 3.8 percent click-through once it showed the items most often found in the same cart. Illustrative case: the company is real, the situation and the data are synthetic, built for this class.

## Panel 1: Which three counts does every pair get?

![The ten dots: chai in 6 orders, biscuit in 4, both in 3, beside the 2 by 2 table of counts](../whiteboards/C2_W04_D03_ten_dots_STUDENT.png)

| Count | The question it answers | Formula | On the ten dots |
|---|---|---|---|
| Support | How often are both in a cart? | both / all | 3 / 10 = 0.30 |
| Confidence | How reliably does A bring B? | both / A | 3 / 6 = 0.50 |
| Lift | How far above chance? | both x all / (A x B) | 3 x 10 / (6 x 4) = 1.25 |

**Crux:** Lift is carts seen holding both over the carts chance gives, the same from either side; it counts and never names a cause.

## Panel 2: What did twelve carts say, and what did 40,000 say?

| Pair | Twelve carts | 40,000 carts |
|---|---|---|
| bread, milk | confidence 1.00, lift 1.50 | confidence 0.74, lift 1.04 |
| chips, cold drink | lift 2.67 on 2 carts | lift 3.39 on 2,000 carts |
| ice cream, chocolate sauce | lift 12 on 1 cart | lift 4.60 on 100 carts |

**Crux:** A few carts can make a pull look strong; milk is in 71 percent of carts, so its pull with anything sits near one.

## Panel 3: Why did the click-through fall?

| Slots showing | Share of impressions after | Click-through after |
|---|---|---|
| milk | 50 percent, from 2 before | 1.2 percent |
| everything else | 50 percent | 6.4 percent, from 6.2 |
| blend | 0.5 x 1.2 + 0.5 x 6.4 | 3.8 percent |

**Crux:** The fall sits in the mix: milk took half the impressions, and 70 percent of slot 1, at 1.2 percent.

## Panel 4: Which pairs fill the strip?

| Region | Rule | Pairs |
|---|---|---|
| Promote | lift 1.5 or more, support at least 1 percent (400 carts) | chips and cold drink 3.39, coriander and green chillies 3.00, bread and butter 2.21 |
| Watch | strong lift below the floor | ice cream and chocolate sauce, 4.60 on 100 carts |
| Trap | lift near one, above the floor: what a count ranks first | milk's pairs, 0.99 to 1.04 |
| Ignore | lift near one, below the floor | most of the 1,221 pairs |

**Crux:** Rank by lift above a support floor; a strong pair on few carts is tried before it takes a slot.

## Panel 5: What is a slot worth in rupees?

`60,000 views a day x 6.4% x 0.5 adds per click x Rs 9 margin = Rs 17,280 a day`

At 1.2 percent the slot earns Rs 3,240, a gap of Rs 14,040 a day or about Rs 4.2 lakh a month. Milk holds 1.5 slots' worth, so re-ranking recovers about Rs 6.3 lakh a month (Rs 3.9 lakh to Rs 9.3 lakh across the assumed ranges).

**Crux:** Value is margin on the adds, less any discount handed back; Rs 80,197 a day of sales is never the gain.

## Panel 6: Which check catches each trap?

| The trap | The check |
|---|---|
| Confidence 1.00, or a count ranking, read as a bundle | Lift: is the partner in most carts anyway? |
| "Shoppers changed" | Split by suggested item: the rest rose to 6.4 |
| Heavy buyers inflate a pair | Count each customer once: 3.39 falls to 2.56 |
| A stock-out lowers a count | Set it aside: curd's share returns, its lift stays 1.01 |
| Lift read as a cause | Only a holdout that changes the strip settles it |

**Crux:** Every count is asked "compared with what?" before it takes a slot.

## Panel 7: What does the interviewer listen for?

"Lift, since it divides by the base rate: bread to milk reads 0.74, but milk is in 71 percent of carts, so lift is 1.04." An LLM shopping assistant's add-ons are scored by lift over a popularity baseline, then a holdout.

**Crux:** Name the base rate, the floor and the cost line, and end on one decision.
