# Self-check: know you are right before anybody reads it

Every checkpoint is something you can verify alone. If one does not match, the hint beside it names
the likeliest reason. All the numbers are on `data/C2_W01_D01_takehome_STUDENT.py`.

---

## Part 2, the numbers

| # | Checkpoint | What you should see | If it does not match |
|---|---|---|---|
| 1 | The file loaded | 24 orders | The loader still names today's file; change the file name in the setup cell |
| 2 | Customers, booked | 19 distinct customer ids | 24 means you counted rows; count each id once with a set |
| 3 | Orders per customer, booked | 1.26, which is 24 over 19 | 0.79 is the rate upside down; 1.00 is rows counted as customers |
| 4 | Revenue, booked | Rs 5,69,540 | If the sum stops part way, read the last line of the message, print the record the loop stopped on, and read its type before you change a line |
| 5 | Not cancelled | 20 orders, Rs 5,54,410 | 16 orders means you kept only the delivered ones; check which statuses your condition keeps |
| 6 | Delivered | 16 orders, Rs 5,45,930 | 20 orders means the condition still keeps the returned orders |
| 7 | Customers and orders per customer, delivered | 14 customers, 1.14 orders each | 16 customers means you counted delivered rows; 0.84 divides delivered orders by booked customers |
| 8 | The mean order, booked | Rs 23,731 | A different mean beside the right count means one amount was skipped or misread; compare your total with checkpoint 4 |
| 9 | The median order, booked | Rs 2,765 | Rs 2,730 or Rs 2,800 means you took one middle order of an even count; average the two |
| 10 | The median order, delivered | Rs 2,450 | Rs 2,765 is the booked median; filter to delivered orders first |

When all ten match, count how many orders sit above the booked mean, sort the amounts, and read the
top of the sorted list. Put what you find into your sentence on what surprised you, with its number.

---

## Part 1, the tree you built

Read your page back and answer each question yes or no. Two noes means rewrite it.

- Does every branch carry its denominator and its window, in words?
- Could somebody who has never seen that business tell what it sells from your table?
- Is the cost of moving each branch written in the owner's terms?
- Does your threshold name two numbers, and does it say what you would open if it failed?
- Is the number you would ask for one the owner would actually know?

---

## Part 3, the two lines

Your first line names a heading from the page and one specific thing under it. If the line could
have been written without opening the page, it is not yet a citation. Your second line says what
changes in your Part 1 tree, or says plainly that nothing changes and why.
