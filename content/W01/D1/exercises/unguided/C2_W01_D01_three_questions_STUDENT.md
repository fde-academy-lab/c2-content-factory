# Day 1, E4. Unguided: the three questions

Drop point: the close of the second half, after records as dictionaries. About 30 minutes, working alone. No hints from the trainer, the Academic TA, the Support TA or the person next to you.

The same thirty records. Three questions to answer in code, then fifteen items on what your answers mean.

1. How many orders are in the Student segment, and what do they total?
2. How many orders were returned, and what do returned orders total?
3. How many delivered orders are above Rs 2,000, and what do they total?

Two rules that make this the real job rather than an exercise. Each answer is a count and a total, said in a sentence that names the group it came from, because a bare number answers none of these three questions. And you read the record before you trust the condition, since one of these three behaves differently from the other two and the difference is in the data rather than in your code.

Post one line at the end, in this shape, using your own letters:

```
1a 2b 3c 4d 5a 6b 7c 8d 9a 10b 11c 12d 13a 14b 15c
```

---

## Item 1

Which of the three questions walks into the record whose amount arrived as text?

a) Question 1, the Student segment
b) Question 3, delivered orders above Rs 2,000
c) All three, since every loop reads every record
d) Question 2, the returned orders

## Item 2

Questions 1 and 3 give the right answer today even with the `int()` left out. Why?

a) Their conditions convert the amount before comparing it
b) Neither of their conditions happens to select KR4200
c) Python converts text to a number inside a `for` loop
d) They read a different copy of the file

## Item 3

Your three counts are 7, 7 and 6, which come to 20 across thirty orders. Is that allowed?

a) Yes, the three are overlapping views of the same file
b) No, since every order must land in exactly one answer
c) Yes, but only because ten orders were dropped as invalid
d) No, since 7 plus 7 plus 6 should come to 30 minus the returns

## Item 4

Match each order to the answers it lands in. One order is left over.

Orders
1. KR4221, a Student order that was returned
2. KR4214, a Student order delivered at Rs 2,840
3. KR4200, a Retail-Core order that was returned at Rs 4,500

Answers
a) Question 1 and question 3
b) Question 2 only
c) Question 1 and question 2
d) Question 2 and question 3

Which matching is right?

a) 1 to a, 2 to c, 3 to b
b) 1 to b, 2 to a, 3 to c
c) 1 to c, 2 to a, 3 to b
d) 1 to c, 2 to d, 3 to a

## Item 5

Can any order land in all three answers?

a) Yes, a large returned Student order would land in all three
b) No, since no order is both returned and delivered
c) Yes, but only if the amount is text
d) No, since the Student segment holds no large orders

## Item 6

Thirteen orders were delivered and thirteen orders are above Rs 2,000, and only six sit in both. What does that tell you?

a) Six orders were counted twice by mistake
b) The file holds twenty-six orders in total
c) Delivery status and order size move together in this file
d) The two thirteens are different orders

## Item 7

You report "13 orders, Rs 35,020" with no other words. What is the reader most likely to assume?

a) That the number covers whatever group they had in mind
b) That the number covers only delivered orders
c) That the number covers the whole file
d) That the number needs its denominator before it means anything

## Item 8

Which sentence is safe to send to somebody who was not in the room?

a) Revenue is Rs 35,020
b) We collected Rs 35,020 from 13 orders
c) 13 of 30 orders are above Rs 2,000, totalling Rs 35,020
d) The order book comes to Rs 35,020 across 13 separate orders

## Item 9

Here is the raw first row of the file, exactly as it arrives.

```
{"order_id": "KR4200", "segment": "Retail-Core", "amount": "4500",
 "status": "returned", "order_date": "2026-08-03"}
```

Which statement about it is true?

a) It is a Student order, so question 1 counts it
b) Its amount is a number already, so no conversion is needed
c) It was delivered, so question 3 counts it
d) Its amount is text, and it is the largest in the file

## Item 10

The Student segment holds seven of thirty orders. What share is that, to the nearest percent?

a) 7 percent
b) 23 percent
c) 30 percent
d) 43 percent

## Item 11

Student orders total Rs 12,945 across seven orders. What is the average Student order, to the nearest rupee?

a) Rs 1,849
b) Rs 12,945
c) Rs 431
d) Rs 2,589

## Item 12

Pick from this bank the three things every one of your three answers must carry. One is left over.

a) The count
b) The name of the group
c) The total
d) The order ids

Which three?

a) a, b and d
b) b, c and d
c) a, b and c
d) a, c and d

## Item 13

You build all three answers in one loop with three pairs of accumulators. What is the cost of doing it that way rather than three separate cells?

a) The answers come out wrong, since one loop cannot hold six accumulators
b) Rerunning one question means rerunning all three
c) The loop runs ninety times rather than thirty
d) There is no cost, and it is always the better shape

## Item 14

Your delivered total and your delivered-above-Rs-2,000 total are the same number. What is the most likely cause?

a) Every delivered order happens to sit above Rs 2,000 in this file
b) The file was read twice
c) The amounts were converted twice
d) The second condition was dropped from the code

## Item 15

Which check would you run first on all three answers, before showing anybody?

a) Confirm each total beats its own smallest member
b) Confirm the three counts add up to thirty exactly
c) Confirm each total ends in a zero
d) Confirm the three totals add up to Rs 58,210 exactly

---

Post your fifteen letters on one line in the shape shown at the top. The solution is released at the close of the session.

## Hands-on

The running half is `notebooks/C2_W01_D01_ex1_hands_on_STUDENT.ipynb`, which walks the three questions with pick-from-options markers and a check after each step. Post its five letters on the same line as these fifteen.

Keep the notebook you built these three answers in and do not throw the cells away. Tonight's take-home is added to the bottom of that same notebook, and it turns this counter into two buckets either side of a boundary you choose.
