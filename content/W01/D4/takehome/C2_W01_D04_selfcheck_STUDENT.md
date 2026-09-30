# Take-home self-check: do discounts grow baskets?

Open this after your notebook runs cold. If a number of yours differs, find the decision that moved
it before you change anything: two careful analysts can make different calls on a row, and the log is
where that shows. The numbers below follow the decisions in the right-hand column.

## Section 1. Clean, from your log

| Measure | Number | The decision behind it |
|---|---|---|
| Lines read from the file, below the header | 97 | Every line, before any decision |
| Distinct orders after cleaning | 90 | Each order counted once, as on Wednesday |
| Delivered orders you can use | 59 | Delivered only, and only amounts that can be a basket |
| Retail-Core and Retail-Plus among those 59 | 50 | Business and Student set aside: Business baskets run to lakhs, and Student carries no discount field |
| Of the 50, discount recorded as missing | 12 | Kept out of both groups, and said so in the log's new line |

## Sections 2 and 3. The comparisons

| Comparison | Discounted | Discount of zero | Gap per order |
|---|---|---|---|
| Both tiers together | Rs 2,311 on 22 orders from 20 customers | Rs 2,336 on 16 orders from 15 customers | about Rs 24 smaller with a discount |
| Retail-Core | Rs 2,052 on 10 orders from 9 customers | Rs 2,059 on 8 orders from 8 customers | about Rs 7 smaller |
| Retail-Plus | Rs 2,528 on 12 orders from 11 customers | Rs 2,612 on 8 orders from 7 customers | about Rs 85 smaller |

The per-order averages are rounded to the rupee, so a gap computed from the rounded figures can differ
by a rupee from the one your notebook prints.

## Section 4. Chance

With seed 2026 and 5,000 shuffles of the discount labels, the share of shuffles that favour discounts
at least as much as the real gap does is about 0.54 for both tiers together, about 0.52 for
Retail-Core and about 0.59 for Retail-Plus. Counting a gap that large in either direction, the shares
are about 0.94, 0.99 and 0.81. Every comparison sits well inside the usual wobble, and every group is
under thirty orders and under thirty customers.

## Section 5. What a strong note does

- It says the file shows no sign that discounted Q1 baskets were bigger, in either tier, and that the
  counts are small.
- It gives the two averages with their counts, and both shares in the form that names the
  chance-only world.
- Its caveat names the orders with a missing discount, and names who got discounts: a discount is
  given to some customers and not others, so even a real gap would need a fair comparison.
- Its action is cheap: measure basket size in a held-back group at the next discount, or wait for a
  quarter with more orders.
- It is under 200 words, and it was read aloud to someone outside the programme.

## Signs you took a shortcut

- Your file has more than 90 orders, or an average includes an amount that cannot be a basket.
- You compared discounted orders with every other order, missing discounts included.
- Your sentence about the share contains "chance we are wrong" or "percent certain".
- You report one share and leave out which direction it counted.
