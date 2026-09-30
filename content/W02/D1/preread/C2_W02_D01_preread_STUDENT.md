# What will Anand ask on Tuesday, and what should you settle tonight?

This pre-read takes about fifteen minutes tonight, with one check to run in your Codespace, and it
asks you to learn no new tool before class.

---

## What does Anand ask on Tuesday?

Anand Iyer, Kalpa Retail's finance controller, read today's Monday numbers and replied with a harder
question:

> "Booked revenue is not collected revenue. Some orders are paid in two instalments, some are
> refunded, some were never paid at all. Show me, order by order, what we actually collected against
> what we booked in Q2. If there is a gap, I want to know which orders and which channel."
>
> Anand Iyer, finance controller, Kalpa Retail

Today every number on his sheet was booked revenue; on Tuesday the money that arrived goes beside it.
Q2 is July to September 2026, and Anand wants the answer for each order and for each channel, app, web
and store.

---

## Which words in Anand's message need a plain meaning before class?

Read each plain meaning, then write your own example in the last column tonight, one line each.
Booked revenue and a key come straight from today; collected revenue and a payment row you will use
from the first minutes of Tuesday.

| Word | What it means, in plain words | Where you meet it | Your own example |
|---|---|---|---|
| Booked revenue | Every order at its amount, whatever happened to it afterwards | Today, every chapter | |
| Collected revenue | The money that arrived for those orders | Tuesday's question | |
| A payment row | One record of money received against an order: which order, how much and when | Tuesday | |
| A key | The column whose value names one record, such as `order_id` for an order or `customer_id` for a customer | Today's lookup, and Tuesday | |

---

## What is one thing worth thinking about before class?

Anand asked for the answer order by order, when one total for the quarter would be shorter to read.
Write down, in two lines, what a single Q2 figure for collected revenue could not tell him, and who in
Finance would need the difference. Bring your two lines to class; the room compares them before any
query runs.

---

## Does your Codespace still give today's Q2 booked revenue?

Open `sql/C2_W02_D01_01_book_STUDENT.sql` in VS Code, select the block named `c1_book` and run it
against the `kalpa` database. It should return two rows, and the Q2 row should read 462 orders and
Rs 9,84,00,000, the booked side of Tuesday's comparison. If it does not run, or the numbers differ,
tell the support TA before class, since Tuesday starts from that number.

---

## Which line do you carry into Tuesday?

Know the booked number before you meet the collected one: Rs 9,84,00,000 on 462 orders in Q2, the
side of Anand's comparison that today already settled.
