# Self-check: know you are right before anybody reads it

Every checkpoint is something you can verify alone. If one fails, the fix is named beside it. Every
revenue figure uses the day's definition: the booked amount of Q2 orders in every status.

Load the sample first, from the repository root:

```
psql -d kalpa -f content/W02/D3/data/C2_W02_D03_takehome_STUDENT.sql
```

---

## Part 1, the numbers

| # | Checkpoint | What you should see | If it does not match |
|---|---|---|---|
| 1 | The base | 454 Q2 orders, a Q2 total of Rs 9,23,60,000 and 98 Retail-Core members with a Q2 order | A total well above Rs 9,23,60,000 means Q1 crept in, so filter on the quarter; a different buyer count means you counted order rows instead of distinct members. |
| 2 | A top twenty under ROW_NUMBER | 20 members | If you get more, the filter sits on the wrong column; ROW_NUMBER can never ship more than twenty. |
| 3 | A top twenty under RANK | 21 members | If you get 20, you ranked the whole book or ranked orders instead of members; rank Retail-Core members by their Q2 total. |
| 4 | A top twenty under DENSE_RANK | 22 members | If you expected it to match RANK, read the dense_rank column either side of twenty and see where it stops leaving gaps. |
| 5 | A top twenty under whole ties only | 18 members | If you get 21, you kept a tie that does not fit inside twenty; a tie is kept only when its last position is twenty or less. |
| 6 | The flag across the whole book, no PARTITION BY | 21 flagged, 8 of them compared with another member's row | If the second count is zero, check that you compared the member of the row two back, lag(customer_id, 2), with the current one. |
| 7 | The flag with PARTITION BY customer_id | 13 flagged, 7 of them reading a skipped month as last month | If the second count is zero, carry lag(month) beside lag(spend) and compare it with the calendar month before. |
| 8 | The flag that requires August and July | 6 flagged across the whole book | If you get 13, the calendar check is missing; if you get more than 13, the September filter is missing. |
| 9 | The flag on your RANK list of 21 | 1 member carries the step 8 flag, and the step 7 flag catches no one else on the list | If you get 6, you flagged the whole book and never joined the flag to your list. |
| 10 | Mid-quarter, the end of the seventh plan week (the week starting 17 August) | Booked to date Rs 5,07,89,120 against plan to date Rs 5,06,80,000, which is Rs 1,09,120 ahead | If the plan side reads Rs 72,40,000, you set a running actual beside one week's plan; accumulate the plan too. |
| 11 | The close, the week starting 28 September | Booked to date Rs 9,23,60,000 against plan to date Rs 9,41,20,000, which is Rs 17,60,000 behind | If your close reads Rs 8,66,29,560, your join dropped every order before the plan line's first week; read the actual at each plan week's last day instead. |
| 12 | The first plan week (the week starting 6 July) | Booked to date Rs 1,35,56,560 against Rs 72,40,000 | If you see Rs 78,26,120, your running total starts at the first plan week instead of the first day of Q2. |

When checkpoints 10 and 11 both match, look at where the lead was largest and ask whether the
quarter was on track by its total, by its weekly run rate or by both. Put the answer in your third
sentence.

---

## Part 2, the recap and your own question

The recap values give ROW_NUMBER 1, 2, 3, 4, 5, RANK 1, 2, 2, 2, 5 and DENSE_RANK 1, 2, 2, 2, 3.
If your RANK line ended on 3, you wrote DENSE_RANK's answer under RANK's name.

Read your own question back and answer each check yes or no. Two noes means rewrite it.

1. Would a Kalpa stakeholder ask your question in those words?
2. Does your window query return a different number of rows from its GROUP BY impostor, and does
   your comment say which rows differ?
3. Does your comment say what question the impostor answers instead?
4. Did you run both queries and paste both results?

---

## Part 3, the three lines

Each line names a window clause you actually wrote. The third line names the function the site's
answer uses, says whether DENSE_RANK keeps the same rows at position one, and says what ROW_NUMBER
would do to a facility that tied for the most slots. If your reason could apply to any query, it is
not yet a reason.
