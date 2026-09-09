# Day 1 solution, E4. The three questions

### Question 1: the Student segment

```
count = 0
total = 0
for r in records:
    if r["segment"] == "Student":
        count = count + 1
        total = total + int(r["amount"])

print(count, total)
```

```
7 12945
```

Seven of the thirty orders are in the Student segment, and they total Rs 12,945.

### Question 2: the returned orders

```
count = 0
total = 0
for r in records:
    if r["status"] == "returned":
        count = count + 1
        total = total + int(r["amount"])

print(count, total)
```

```
7 13670
```

Seven orders were returned, and those returned orders total Rs 13,670.

This is the question that behaves differently from the other two. KR4200 is a returned order and its amount is the text `"4500"`, so question 2 walks straight into the record you fought with in the guided build. Without `int()` around the amount, this cell stops on the very first record. Questions 1 and 3 happen to miss that record, so they give the right answer today even without the conversion, and they would break the morning a second text amount arrives. Convert at the point of use every time and the question of which records happen to be tidy stops mattering.

### Question 3: delivered orders above Rs 2,000

```
count = 0
total = 0
for r in records:
    if r["status"] == "delivered":
        if int(r["amount"]) > 2000:
            count = count + 1
            total = total + int(r["amount"])

print(count, total)
```

```
6 15520
```

Six delivered orders are above Rs 2,000, and they total Rs 15,520.

Two conditions have to hold for a card to count here, so one `if` sits inside the other and the accumulators sit inside both. You can also join the two conditions on a single line with `and`, and you get the same six orders. The nested version is the one built out of the pieces you were handed today, and it makes the order of the two questions visible on screen.

### The overlap question

Your three counts are 7, 7 and 6, which come to 20, and there are thirty orders in the file. The three answers are three overlapping views of the same thirty records rather than three slices of them, so an order can be counted in more than one of them and plenty of orders are counted in none.

KR4221 is a Student order that was returned, so it lands in question 1 and in question 2. KR4214 is a Student order that was delivered at Rs 2,840, so it lands in question 1 and in question 3. No order lands in all three, because a single order cannot be both returned and delivered.

Notice what question 3 also tells you. There are 13 delivered orders and 13 orders above Rs 2,000, and only 6 orders sit in both groups at once. Those two thirteens were never the same thirteen orders.

### Where this pattern lives in production

Filter, count, total, then a sentence naming the group is the shape of most of the reporting work you will be asked for in your first year. The expensive mistake is not the arithmetic. It is a count that travels without the group it came from, which is how a returned-orders total ends up on a slide with the word revenue above it.
