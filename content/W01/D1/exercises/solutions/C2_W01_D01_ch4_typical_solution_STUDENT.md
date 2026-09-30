# Solution: chapter 4, the typical order

Answers: 1a 2d 3c 4b 5b

## The idea being tested

The mean is total over count and takes in every rupee of every order, so one very large order drags
it: Rs 18,160 with 29 of 30 orders below it. The median, Rs 2,205, is the typical order, and it
barely moves when the definition changes (Rs 2,060 delivered). The design items ask which middle a
payback should use, and size how far each middle moves when one large order arrives.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | a | When 29 of 30 sit below the mean, something at the top is pulling it; one order is enough. | b is the reverse of the picture. c: the arithmetic is right; the choice of middle is the problem. d: an even spread would put about half on each side. |
| 2 | d | An even count has two middles, and the median is halfway: (2,110 + 2,300) / 2 = Rs 2,205. | a and b take one of the two middles. c is the mean. |
| 3 | c | The payback buys first orders, so their median prices it; per-type means answer better once each type gets its own plan. | a lets one large order set the price of every new customer. b depends on a trimming rule nobody has set. d plans on the exception. |
| 4 | b | The invented mean goes from Rs 2,260 to Rs 16,883, a move of Rs 14,623. | a moves Rs 50. c moves Rs 83. d: one order moved the mean by more than six times its old value. |
| 5 | b | The median holds across definitions within Rs 145, so either is honest once named. | a and c are means that one order drags, and they swing by Rs 6,640 between definitions. d averages two dragged numbers. |

## The part worth arguing about

Item 3. The mean is right for a revenue forecast, and a payback model does add up rupees. The
payback is priced per new customer, though, and a typical new customer places a typical order.

**Kavya's review.** "Put the median in the sentence, say the mean is eight times higher, and say one
order does it."

## Where the pattern lives in production

Blinkit reported a net average order value of Rs 518 for the quarter to June 2026. Across millions
of similar small baskets a mean describes them well; across 30 orders with one very large one, it
does not.

## Hands-on

Notebook 04 prints the median Rs 2,205, the mean 8.2 times higher, and Rs 2,060 on delivered orders.
