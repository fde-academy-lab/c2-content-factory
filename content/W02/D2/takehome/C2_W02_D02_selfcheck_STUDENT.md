# How do you know your take-home is right before anybody reads it?

Every checkpoint is something you can verify alone. If one fails, the likely cause is named beside
it. Work through the numbers first, then the questions on your writing.

---

## Do your part 1 numbers match?

| # | Checkpoint | What you should see | If it does not match |
|---|---|---|---|
| 1 | The book loaded | 120 orders, 125 payment rows and 2 refund rows | Load the file again with ON_ERROR_STOP set and read the first error it prints |
| 2 | Booked, from orders alone | Rs 16,97,600 in all: app 27 orders and Rs 1,87,210, store 50 and Rs 5,12,740, web 43 and Rs 9,97,650 | A different total means a filter crept in; this book is one quarter, so it needs none |
| 3 | Rows out of your report's join | 120, one per order | 128 means payments were joined row by row; bring them to one row per order first |
| 4 | Booked after the join | Rs 16,97,600, the same as checkpoint 2 | A larger figure is the same fan-out as checkpoint 3, seen in rupees |
| 5 | Collected, by channel | app Rs 1,80,310, store Rs 4,33,930, web Rs 6,11,150, and Rs 12,25,390 in all | A figure equal to what the feed posted against the book's orders means a gateway retry is still inside collected; one equal to the whole feed's total means you also summed a payment no order claims |
| 6 | Refunded | Rs 4,250 in all | A figure of minus Rs 4,250 is the stored sign; decide what your column means and say so |
| 7 | Collected net of refunds, by channel | app Rs 1,80,310, store Rs 4,33,930, web Rs 6,06,900, and Rs 12,21,140 in all | Rs 12,29,640 means the negative refunds were subtracted and so added back |
| 8 | The gap, booked less collected | Rs 4,72,210 | If your list of orders short of payment adds to more than the gap, an order whose money partly arrived sits on it at its full booked value |
| 9 | Every payment row accounted for | Your buckets add to 125 rows and Rs 12,40,030 | A bucket that is missing is usually a payment with no order, or the second posting of a retry |

When all nine match, read your lists again with checkpoint 8 in mind. The gap is one number, and
your classification in step 5 decides how many lists it splits into and what each list asks Anand to
do.

---

## Does your part 1 writing hold up?

Answer each question yes or no. Two noes means rewrite it.

1. Is your reconciliation block written with the words before the numbers, so that someone could
   check it without running anything?
2. Does your classification name what Anand would do differently for each list?
3. Does your comment on the refunds say what the stored sign is and what your column means?
4. Does your sentence to Anand give order ids for the action you want, rather than a channel alone?
5. Would your sentence still be true if another retry turned up tomorrow, because it says how you
   removed retries rather than only how many?

---

## Does your own question in part 2 hold up?

1. Is the question in a stakeholder's words, with no SQL in it?
2. Does the reconciliation block name the difference between rows in and rows out, even when it is
   zero?
3. Could you say in one sentence why the join you chose is the honest one for this question?

---

## Does your part 4 line hold up?

Your line says that an INNER join is honest when the question is about matched rows only, and names
one such question. If your line could be pasted into any SQL course, make it about Kalpa.
