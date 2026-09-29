# Round 3 set: the unpaid list and the double-paid list

About 15 minutes, alone first, then compare with your neighbour. Eight items. Every item has one
right answer.

Anand asked for the gap by order and by channel: "If there is a gap, I want to know which orders and
which channel." Kavya's rule for this round: "Two payment rows are not a double payment. Show me what
makes a retry a retry before you call anyone about a refund."

Post one line, eight letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxxxxxx
```

Items 1, 2, 5, 6 and 7 run on the invented tiny tables from round 1. Items 3, 4 and 8 run on Kalpa's
Q2.

---

## Part A. The filter that turned a LEFT join into an INNER one

A teammate wants "every order, with what was collected inside the quarter" and writes:

```sql
SELECT o.order_id, o.amount AS booked, p.payment_id, p.paid_date
FROM tiny_orders o
LEFT JOIN tiny_payments p ON p.order_id = o.order_id
WHERE p.paid_date BETWEEN '2026-07-01' AND '2026-09-30';
```

### Q1. How many rows does it return, and what has gone?

a) 7, every order kept, since the join is written as a LEFT one
b) 6, and T-4 is gone, because its NULL paid_date fails the WHERE
c) 5, one row per order, since the date filter removes the repeats
d) 6, and P-7 is gone, because its order is not in tiny_orders

### Q2. Anand wants every order kept, with only the payments made inside the quarter attached. Which rewrite gives him that?

a) Keep the WHERE and add OR p.paid_date IS NULL beside it
b) Swap the LEFT JOIN for a FULL JOIN so unmatched rows return
c) Move the date condition into the ON clause beside order_id
d) Move the date condition into a HAVING after GROUP BY order_id

---

## Part B. The unpaid list

### Q3. Which query lists the Q2 orders that have no payment at all, the list Anand asked for?

a) INNER JOIN payments, then keep the rows WHERE p.payment_id IS NULL
b) LEFT JOIN payments, then keep the rows WHERE p.amount = 0
c) LEFT JOIN, GROUP BY o.order_id, and keep HAVING COUNT(*) = 0
d) LEFT JOIN payments, then keep the rows WHERE p.payment_id IS NULL

---

## Part C. The double-paid list

### Q4. `GROUP BY order_id HAVING COUNT(*) > 1` on Q2 payments returns 216 orders worth Rs 9,62,59,340 booked. A teammate drafts a note asking the payments team to reverse the second payment on every one of them. What do you do?

a) Send it, since two payments on one order is a double payment
b) Stop it, and split the 216 by instalment_no before anyone is called
c) Send it for the ten largest orders only, where the money at stake is
d) Stop it, because reversing payments is Finance's call and not ours

### Q5. On the tiny tables, the same HAVING COUNT(*) > 1 lists T-2 and T-3. Which of them is a gateway retry?

a) Both, since each order carries two payment rows in the feed
b) T-2 only, since its two rows fall a month apart on two dates
c) T-3 only, one instalment posted twice on the same day
d) Neither, since both orders were fully paid in the end

### Q6. Grouped by order_id and instalment_no, the retry shows as T-3's instalment 1 posted twice at 1,500. How much was posted that should not have been?

a) 1,500, the one posting too many for that instalment
b) 3,000, everything the feed posted against order T-3
c) 750, half of the instalment, split across both rows
d) 0, since T-3 received at least the amount it booked

### Q7. The reverse anti-join, payments LEFT JOIN orders WHERE the order side IS NULL, returns P-7: Rs 600 against order T-9, which is not in the book. What happens to it in Anand's report?

a) Add it to collected, since the money did arrive in the account
b) Attach it to T-5, the paid order closest to it in the feed
c) Drop it without a note, since no order in the book claims it
d) Keep it out of collected, and send its id to the platform lead

---

## Part D. The invariant

### Q8. Your Q2 unpaid list is ready. Before you trust it, its booked total must equal what?

a) Booked less collected, with retries removed at order grain
b) Booked less everything the feed posted against Q2 orders
c) The count of unpaid orders times the average Q2 order value
d) Zero, since a quarter's payments must cover its bookings

---

## Check it yourself

After you post, run part A of `sql/C2_W02_D02_04_lists_STUDENT.sql`, then part B on the warehouse.
Read the count of each list before you read its rows, and hold both lists for the escalated case.
