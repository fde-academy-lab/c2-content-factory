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
| 3 | c | A payback is a total over a customer's life, so it needs a mean, and the mean must come from the customers the spend targets, with bulk orders set aside: the consumer mean, about Rs 2,235 an order, on contribution. | a lets one bulk order set the value of every new customer. b describes the typical order well and cannot add up to a total over a year. d plans on the exception. |
| 4 | b | The median moved least and needs no rule; a trimmed mean that drops one order each end only works while there is exactly one bulk order, so it matches the median once its rule drops every bulk order. | a reports the exception as the typical order. c throws away a real order by rule, and the bulk order is real revenue. d ignores the Rs 14,623 move the one large order caused. |
| 5 | b | The median holds across definitions within Rs 145, so either is honest once named. | a and c are means that one order drags, and they swing by Rs 6,640 between definitions. d averages two dragged numbers. |

## The part worth arguing about

Item 3. Many will pick b, since the chapter built the median. The median is the typical order;
a payback adds a customer's orders over time, which only a mean can do, and the mean has to be the
segment's, with the bulk order set aside.

**Kavya's review.** "Put the median in the sentence, say the mean is eight times higher, and say one
order does it."

## Where the pattern lives in production

Blinkit reported a net average order value of Rs 518 for the quarter to June 2026. Across millions
of similar small baskets a mean describes them well; across 30 orders with one very large one, it
does not.

## Hands-on

Notebook 04 prints the median Rs 2,205, the mean 8.2 times higher, and Rs 2,060 on delivered orders.
