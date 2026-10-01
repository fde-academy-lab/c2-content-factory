# Which extra should you take tonight, the stretch or the recovery?

Use the stretch if the day's pass felt comfortable, and the recovery if any chapter left you unsure.
Neither is required, and neither is marked. Both work on the day's case: Kalpa Retail's export of Q1
and Q2 orders from the ERP, the enterprise resource planning system Finance books orders in, which the
day's pass cleaned and reconciled to the books, Finance's own record of Q1 at Rs 1,90,00,000.

## Stretch. What would you send Anand if your bridge had not closed?

Used at work whenever a reconciliation leaves a gap and the note still has to go out.

> "If your bridge had not closed to my books, what would you have sent me?"
>
> Anand Iyer, finance controller, Kalpa Retail

A bridge walks one total to another one cause at a time, and it closes when its last step lands on
the books. Invent a Finance figure that is Rs 25,000 below your clean Q1, as if the books had missed an
order. Write the note you would send, under 120 words, that says which figure you believe and what
evidence would change your mind. Then answer in two sentences: which of the day's checks would you run
first to find a Rs 25,000 order, and why that one?

A bridge that does not close is a finding about the data, and the note reports it as one. It says
precisely what you know and what you do not, and which rows you would put in front of Finance's
analyst, without blaming anyone.

## Recovery. Can you rebuild the day's pass on ten rows you type yourself?

Used at work whenever a method has to be checked on a sample small enough to follow by hand.

If a chapter slipped past you, rebuild it slowly on ten invented rows:

1. Write ten rows as dictionaries of text: nine orders, one of them on two rows, with the first of
   those two copies carrying the amount `"n/a"`. Add up the nine orders by hand, counting the repeated
   order once at its readable amount; that total plays the books.
2. Profile them: present, convertible, distinct, for `order_id` and `amount`. Check each count by
   hand before trusting the code.
3. Apply the identity rule, which decides when two rows are one order, keeping the copy whose amount
   converts, then convert the kept amounts with a rejects log.
4. Reconcile: rows in equal kept plus set aside plus rejected, and the rupees as read less the rupees
   set aside equal your hand total.
5. Change one thing, keep the first copy instead, and watch which reconciliation breaks.

When all five run, say why step 5 breaks the rupees and leaves the rows tied.
