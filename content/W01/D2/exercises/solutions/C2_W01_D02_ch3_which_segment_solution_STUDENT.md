# Solution: Which of the four customer segments carries the fall in orders per customer, measured the same way for every segment and quarter?

Answers: 1d 2a 3c 4b 5a 6d

The head of Kalpa Retail's paid membership tier asked whether his tier is the one slipping, after a member reported the app's reorder button broken for six weeks. Chapter 3 wrote Monday's tree once as `tree_for(rows)`, ran it on each of the four customer segments in both quarters, and rolled the segments back up to the company's orders per customer, 1.65 in Q1 and 1.25 in Q2, from 114 and 86 orders by the same 69 customers.

Two of the six items are design items: 1 and 2.

### Q1. Which way should compute the same numbers for eight groups and for the asks due later today? (Design)

Copying the loop takes 72 lines and 8 places to edit, a function 21 lines and 1 place, one pass by key 14 lines and 1 place but shaped for these eight groups, and a channel, a month and delivered orders are asked for later today.

The key is d, "A function, tree_for(rows), since each later subset is one more call". The later asks are new subsets of orders, and a function answers any list of orders with one call; one pass by key would need a new loop for each new key.

- a, "Copy the loop per group, since each copy can be checked on its own": eight places to edit when the definition changes, and one gets forgotten.
- b, "One pass by key, since it is the shortest code and reads the rows once": it is the shortest today, and a channel or a month needs a new loop.
- c, "A spreadsheet, since eight groups are few enough to total by hand": a hand total cannot be rerun on delivered orders this afternoon.

### Q2. How many rows does filtering once per group read on 40 lakh orders? (Design)

Suppose next quarter's export holds 40 lakh orders and Anand wants all 40 segment-and-month groups every Monday; the item sets filtering once per group against one pass by key.

The key is a, "16 crore rows against 40 lakh, so one pass by key takes over". Each filter reads the whole export, 40 times over, while one pass reads it once and fills every group. That volume is the fact the chapter named for switching to one pass by key.

- b, "40 lakh either way, since each group's total reads only its own rows": that holds only once something has split the rows by group, which is itself a pass by key.
- c, "16 crore against 40 lakh, and filtering stays, since each group is easy to check": one pass by key checks just as well group by group, and it reads the export once.
- d, "1,600 rows against 200, the same gap as on today's file": that is today's 200-row file, where speed decides nothing.

### Q3. Why does Anand's summary table show a blank where the helper shows 1.65?

Anand's summary table shows a blank for Q1 orders per customer, although the helper called on its own in a cell shows 1.65.

The key is c, "The helper printed its answer and returned nothing, so the table got None". `print` shows the value on screen and hands back None, so a table built from the call holds None, which shows as a blank.

- a, "The table was filled before the helper ran, so it still holds an old blank": rerunning the table would fix that, and the blank stays.
- b, "The helper rounds 1.652 to 1.65, and the table will not take a rounded value": a table holds any number, rounded or not.
- d, "The helper returned from inside its loop, before the last order was counted": an early return hands back a wrong number, never a blank.

### Q4. What does a weighted roll-up of the four segments give?

Averaged over the four segments, orders per customer reads 1.94 then 1.82, minus 6.0 percent, while the four segments hold 69 customers who placed 114 orders in Q1 and 86 in Q2.

The key is b, "1.65 to 1.25, a fall of 24.6 percent, so frequency is the branch after all". Total orders over total customers weights each segment by its customers: 114 over 69 and 86 over 69, minus 24.6 percent, which reproduces chapter 2's figure.

- a, "1.94 to 1.82, since the weights cancel out once all four segments are counted": weights cancel only when every segment is the same size.
- c, "1.65 to 1.25, a fall of 32.0 percent, measured against the Q2 figure": 32.0 percent is the change measured against Q2.
- d, "0.61 to 0.80, total customers over total orders in each quarter": that is the reciprocal, customers per order.

### Q5. What happened to the typical Business order in Q2?

Business revenue fell Rs 22,29,720 on three fewer orders, and `describe` shows the median Business order barely moved while the range rose about 73 percent.

The key is a, "It held: one very large order stretched the range; the fall is three fewer orders". The median is the typical order, and it barely moved. The range is set by the two extreme orders, and one very large order widened it, while the rupee fall is three orders worth lakhs each.

- b, "It grew, since a range up 73 percent means the middle of the orders moved up too": it reads a spread as a level.
- c, "It shrank, since revenue fell by Rs 22 lakh while the count moved by only three": three orders at about Rs 10 lakh each come to about Rs 30 lakh, so the count carries the fall.
- d, "It is the mean here, since a median ignores the lakh-sized orders that matter most": the mean is what one large order pulls, and the median is the typical order.

### Q6. In which order does the roll-up of the four segments run?

Anand asks for the company's orders per customer rolled up from the four segments, from four steps: divide the totals (p), compute each segment's counts (q), check against chapter 2's company figure (r), and add the segments' counts (s).

The key is d, "q, s, p, r". Compute each segment's counts, add them, divide the totals, then check that the roll-up reproduces the company figure.

- a, "q, p, s, r": it divides before there are totals to divide.
- b, "s, q, p, r": it adds counts that have not been computed yet.
- c, "q, s, r, p": it checks a result before the result exists.
