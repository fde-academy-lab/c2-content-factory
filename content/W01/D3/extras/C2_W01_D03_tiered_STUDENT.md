# Extras: one to stretch, one to recover

Use the stretch if the day's pass felt comfortable, and the recovery if any round left you unsure.
Neither is required, and neither is marked.

## Stretch: a reconciliation that fails on purpose

> "If your bridge had not closed to my books, what would you have sent me?"
>
> Anand Iyer, finance controller, Kalpa Retail

Invent a Finance figure that is Rs 25,000 below your clean Q1, as if the books had missed an order.
Write the note you would send, under 120 words, that says which figure you believe and what evidence
would change your mind. Then answer in two sentences: which of the day's checks would you run first
to find a Rs 25,000 order, and why that one?

**The hard part, and the point.** A bridge that does not close is not a failure of the pass; it is a
finding. The note has to be precise about what you know, what you do not, and which rows you would
put in front of Finance's analyst, without blaming anyone.

## Recovery: the pass, one step at a time

If a round slipped past you, rebuild it slowly on ten invented rows you type yourself:

1. Write ten orders as dictionaries of text, with two copies of one order and one amount written as
   `"n/a"`.
2. Profile them: present, convertible, distinct, for `order_id` and `amount`. Check each count by
   hand before trusting the code.
3. Convert with a rejects log, then apply the identity rule preferring the copy that validates.
4. Reconcile: rows in equal kept plus set aside, and the rupees as read less the rupees set aside
   equal your clean total.
5. Change one thing, keep the first copy instead, and watch which reconciliation breaks.

When all five run and you can say why step 5 breaks the rupees and not the rows, the day's three
rounds are yours.
