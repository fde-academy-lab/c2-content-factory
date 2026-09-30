# Chapter 4 scenario set: the typical order

> "No averages. One business customer can move an average."
> Anand Iyer, finance controller, Kalpa Retail

Five items on the same 30 orders, alone, in the room's turn of chapter 4. Items marked **Design**
ask for the best-fit approach, a sizing, or the fact that would switch it.

Post one line, five letters in item order, no spaces:

```
Post exactly this shape: xxxxx
```

```mermaid
flowchart LR
    S["<b>sort the amounts</b>"] --> M["<b>take the middle</b><br/>or halfway between two"]
    M --> T["<b>the typical order</b>"]
```

---

### Q1. The mean of 30 orders is Rs 18,160 and 29 of them sit below it. What does that say about the orders?

a) One or a few very large orders pull the mean far above a typical order
b) Most orders sit near Rs 18,160, and a few small ones pull the mean down below them
c) The mean is wrong arithmetic, and it should be recomputed by hand from the amounts
d) The orders are spread evenly, so the mean and the median must sit close together

### Q2. The 30 amounts are sorted; the 15th is Rs 2,110 and the 16th Rs 2,300. What is the median order?

a) Rs 2,110, the 15th amount in size order
b) Rs 2,300, the 16th amount in size order
c) Rs 18,160, the booked total divided by the count of 30
d) Rs 2,205, halfway between the two middle amounts

### Q3. Design. Marketing's payback adds up what a new customer brings over their first year. Which number should it be built on, and what would change it?

a) The booked mean, since every rupee counts in a total; a cleaner extract would change it
b) The median of first orders, the typical order; a skewed segment would change it
c) The targeted segment's mean, one-off orders aside; a new target would change it
d) The largest order, the ceiling a customer can reach; a price cut would change it

### Q4. Design. One invented Rs 90,000 order joins five invented orders of Rs 1,900 to Rs 2,600: the mean moves Rs 14,623, the median Rs 50, the trimmed mean Rs 83. Which should the team report as the typical order, and when would the trimmed mean do as well?

a) The mean, since the order that moved it most is the one the business most needs to see
b) The median; the trimmed mean would do once its rule drops every large order
c) The trimmed mean always, since it throws away the two orders most likely to be errors
d) Any of the three, since on five ordinary orders they all sit within Rs 100 of each other

### Q5. On not-cancelled orders the mean is Rs 20,606 and the median Rs 2,100; on booked orders, Rs 18,160 and Rs 2,205. Which figure should Meera plan the typical order on?

a) Rs 20,606, the not-cancelled mean, since those orders at least stayed sold
b) About Rs 2,100 to Rs 2,205, the median, named with its definition
c) Rs 18,160, because the mean is the figure that multiplies back to revenue
d) Rs 19,383, the average of the two means, so both definitions are represented

---

## Hands-on

`notebooks/C2_W01_D01_04_the_typical_order_STUDENT.ipynb` sizes the four middles on the invented
records and prints the median under each definition. Check Q2, Q4 and Q5 against it.

**In the interview.** [S] Mean or median for order value, and why?
