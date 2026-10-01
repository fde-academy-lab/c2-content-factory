# Which answers hold in the chapter 3 set on which copy stays, and why?

Answers: 1a 2c 3d 4b

When an order appears twice in Kalpa Retail's export from the ERP, the enterprise resource planning system Finance books orders in, the team has to choose which copy stays, and Anand Iyer's analyst checks that choice against the books, Finance's own record of Q1 at Rs 1,90,00,000, to the rupee.

Two of the four items are design items: 2 and 3.

### Q1. Which row of order KR-90012 stays, and what does the log say?

On an invented export two rows share order_id KR-90012; the first reads amount `--`, the second `1900`, and every other field matches.

The key is a, "The second, whose amount converts; the first logged unreadable". The copy whose amount converts carries the order's value, and the log names the unreadable copy and the line of the row that stayed.

- b, "The first, as the original, with the second logged as its copy": keeps a row that cannot be summed, so the quarter falls Rs 1,900 short.
- c, "Both, flagged, until Finance says which amount it booked": counts one order twice in the rows, and Finance booked one order.
- d, "The first, with its amount set to 0 so that the sum runs": turns a failure into a sale for nothing.

### Q2 (Design). What does keeping the first copy of every pair cost against the books?

An invented export holds 40 repeated orders: 38 identical pairs, one pair whose first copy is unreadable beside a twin, the other copy of the same order, at Rs 2,600, and one pair that differs only on the date, both copies at Rs 1,450.

The key is c, "Rs 2,600, the twin's value, which the first copy lacks". Only the pair whose first copy is unreadable moves rupees: that copy adds nothing to the sum, so its Rs 2,600 twin is lost. The pair with two dates keeps Rs 1,450 whichever copy stays.

- a, "Rs 0, since every order still keeps one of its rows": misses that the kept copy cannot be summed.
- b, "Rs 4,050, the unreadable pair and the pair with two dates": the pair with two dates costs nothing, since both copies carry Rs 1,450.
- d, "Rs 5,200, since the lost twin's value counts twice in Q1": the twin is lost once, and its value leaves Q1 once.

### Q3 (Design). Which survivor rule goes in the log once the ERP team explains the second extract?

The ERP team says the second extract, the second pull of rows out of the ERP, re-ran May's orders after a pricing fix and copied April's and June's unchanged.

The key is d, "Last copy for May; elsewhere the copy that converts, then first". May's second copies carry the corrected prices, so they win in May. April and June were copied unchanged, so the day's rule still decides there, and it keeps a readable copy wherever one exists.

- a, "Last copy for every pair, since the second extract is the fix": applies May's reason to months it does not cover.
- b, "First copy for every pair, as the first extract is the original": keeps May's prices from before the fix.
- c, "The copy that converts, then the first, everywhere, as it tied Q1 today": a rupee tie on today's file is no reason to keep May's prices from before the fix.

### Q4. Who hears first about the two Business rows set aside?

Twenty rows are set aside as copies: two Business orders, Kalpa's sales to companies, carry Rs 9,00,000 of the Rs 9,30,000, and eighteen are Retail-Plus orders, from Kalpa's paid membership tier.

The key is b, "Anand's, since nearly all of the gap in rupees sits in those two". Two rows carry about 97 percent of the rupees, which is where Anand's gap sits. The eighteen Retail-Plus rows matter to a per-customer rate, which is a second conversation.

- a, "Marketing's, since Retail-Plus carries most of the rows set aside": the Retail-Plus rows are Marketing's, and they carry Rs 30,000.
- c, "The auditor's, since every row set aside needs its reason first": the auditor wants every row, and the money decides which to show first.
- d, "Operations', since Business orders move the count of deliveries": two rows move a count of orders very little.
