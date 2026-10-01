# Does your take-home reach the numbers a careful pass on Wednesday's export reaches?

Open this after your notebook runs cold. If a number of yours differs, find the decision that moved
it before you change anything: two careful analysts can make different calls on a row, and the log is
where that shows. The numbers below follow the decisions in the right-hand column.

The take-home asks whether the marketing lead is right that Q1's discounted orders were bigger
baskets, on `data/C2_W01_D04_takehome_STUDENT.csv`, Wednesday's take-home export. A basket is one
order's amount. The label shuffle deals the discount labels at random across the orders, 5,000 times
with seed 2026, and the share is how often those deals favour discounts at least as much as the real
gap does, or make a gap that large either way. Retail-Core and Retail-Plus are Kalpa Retail's two
consumer tiers, and the day's rule of thumb distrusts a comparison with fewer than thirty customers
behind it.

**Who needs the answer.** You, before you post. Meera Raghavan, Kalpa Retail's CEO, reads your note
as the reason to give more discounts or not, and a count that went wrong in cleaning moves every
average and share after it.

**The questions on the way.**

- How many orders should your cleaning keep?
- What should the blended and per-segment comparisons show?
- How often should chance make each gap?
- What does a strong note to Meera do?
- Which signs say you took a shortcut?

## How many orders should your cleaning keep?

| Measure | Number | The decision behind it |
|---|---|---|
| Lines read from the file, below the header | 97 | Every line, before any decision |
| Distinct orders after cleaning | 90 | Each order counted once, as on Wednesday |
| Delivered orders you can use | 59 | Delivered only, and only amounts that can be a basket |
| Retail-Core and Retail-Plus among those 59 | 50 | Business and Student set aside: Business baskets run to lakhs, and Student carries no discount field |
| Of the 50, discount recorded as missing | 12 | Kept out of both groups, and said so in the log's new line |

## What should the blended and per-segment comparisons show?

| Comparison | Discounted | Discount of zero | Gap per order |
|---|---|---|---|
| Both tiers together | Rs 2,311 on 22 orders from 20 customers | Rs 2,336 on 16 orders from 15 customers | about Rs 24 smaller with a discount |
| Retail-Core | Rs 2,052 on 10 orders from 9 customers | Rs 2,059 on 8 orders from 8 customers | about Rs 7 smaller |
| Retail-Plus | Rs 2,528 on 12 orders from 11 customers | Rs 2,612 on 8 orders from 7 customers | about Rs 85 smaller |

The per-order averages are rounded to the rupee, so a gap computed from the rounded figures can differ
by a rupee from the one your notebook prints.

## How often should chance make each gap?

With seed 2026 and 5,000 shuffles of the discount labels, the share of shuffles that favour discounts
at least as much as the real gap does is about 0.54 for both tiers together, about 0.52 for
Retail-Core and about 0.59 for Retail-Plus. Counting a gap that large in either direction, the shares
are about 0.94, 0.99 and 0.81. Every comparison sits well inside the usual wobble, and every group is
under thirty orders and under thirty customers.

## What does a strong note to Meera do?

- It says the file shows no sign that discounted Q1 baskets were bigger, in either tier, and that the
  counts are small.
- It gives the two averages with their counts, and both shares in the form that names the
  chance-only world.
- Its caveat names the orders with a missing discount, and names who got discounts: a discount is
  given to some customers and not others, so even a real gap would need a fair comparison.
- Its action is cheap: measure basket size in a held-back group at the next discount, or wait for a
  quarter with more orders.
- It is under 200 words, and it was read aloud to someone outside the programme.

## Which signs say you took a shortcut?

- Your file has more than 90 orders, or an average includes an amount that cannot be a basket.
- You compared discounted orders with every other order, missing discounts included.
- Your sentence about the share contains "chance we are wrong" or "percent certain".
- You report one share and leave out which direction it counted.
