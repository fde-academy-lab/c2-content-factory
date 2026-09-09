# Day 1 solutions

Release rule: E1, E2 and E3 at the close of the session. E4 at the close as well, once everyone has stopped working on it. The take-home solution opens tomorrow's session.

Read the explanation before the answer. The answer on its own is worth very little in an interview.

---

## E1. The threshold count and total

### What the build was teaching

Three pieces answer this question and you already had all three: a loop that walks the records one at a time, a condition that asks one thing of each record, and two accumulators that remember what the condition found.

The reason it was built one line at a time is that the failure sits in the middle of it. A cell handed to you whole would have run, given you a number, and taught you nothing about the record that was going to stop it.

### The break you passed through

```
TypeError: '>' not supported between instances of 'str' and 'int'
```

KR4200 stores its amount as the text `"4500"` rather than the number `4500`, and it is the first record in the file, so the loop stopped on card one. `count` was still 0 when it stopped, because nothing had been counted yet.

Python was asked whether a piece of text is greater than a number, and it refused and named both types it was holding. A spreadsheet would have placed that value somewhere in the sort order and shown you a number with no warning attached. You lost ten seconds and you kept the truth.

### The answer

```
count = 0
total = 0
for r in records:
    if int(r["amount"]) > 2000:
        count = count + 1
        total = total + int(r["amount"])

print(count, total)
```

```
13 35020
```

13 of the thirty orders are above Rs 2,000, and those orders total Rs 35,020.

### Line by line

`count = 0` and `total = 0` sit above the loop and inside the same cell. Rerunning the cell puts them back to zero before the loop starts again, which is what stops a second run from adding a second copy of everything onto the first run's answer.

`for r in records:` deals you one card at a time, and `r` is the card in your hand for that turn through the indented lines.

`int(r["amount"])` converts at the point of use. The record on the bench still holds text, and the comparison still gets a number. Today `int()` is a converter and nothing more. What it does when a value will not convert is tomorrow's business.

The two accumulator lines sit inside the `if`, so a card that fails the condition adds nothing to either name. That is the whole mechanism.

`print(count, total)` sits outside the loop with no indent, so it runs once at the end instead of thirty times.

### The two thirteens

The opening demo gave you 13 delivered orders totalling Rs 25,720. This build gave you 13 orders above Rs 2,000 totalling Rs 35,020. They are two different groups of orders that happen to share a count, and the totals are different because the groups are different. If you report one of those thirteens without naming its group, the person reading it will assume you meant the other one.

### Where this pattern lives in production

Every reporting pipeline has a filter, a count and a total somewhere near its output, and the first question a reviewer asks is which records were excluded and why. A money column arriving as text is the ordinary case in this work, which is why the conversion sits at the point of use rather than in your assumptions about the file.

---

## E2. Predicting the output

### The idea being tested

A value carries its type with it, and the type decides what every operator and every method does next. You cannot read a type off the shape of a number on screen, so you ask.

### The answers

Cell 1 prints:

```
<class 'str'>
<class 'int'>
```

Cell 2 prints:

```
3755
```

Cell 3 prints:

```
0
```

| Cell | Why it printed that |
|---|---|
| Cell 1 | The quotes are the entire difference between the two lines, and each quote is one character wide. `'4500'` is text that happens to be made of digits, and `4500` is a number. |
| Cell 2 | Two of the three records are delivered, so the condition held twice, and 2395 plus 1360 is 3755. The returned record added nothing because the condition refused it. |
| Cell 3 | This record has no `discount` field at all, so `.get()` handed back the default you supplied, which was 0. |

The two follow-on questions. With a default of 100, cell 3 prints `100`, because the default is whatever you wrote and Python has no opinion about whether it is sensible. Asking the same record for `r["discount"]` with square brackets stops the cell:

```
KeyError: 'discount'
```

### The part worth arguing about

The default in `.get()` is a decision you are making about the business, and it leaves no mark on the screen once the cell has run.

Run `r.get("discount", 0)` across the thirty records and the discounts total Rs 250, which is exactly the two discounts the file records. Run `r.get("discount", 100)` across the same thirty records and they total Rs 3,050, and Rs 2,800 of that is a number you invented twenty-eight times.

Both cells run to the end. Both print a clean number. Only one of the two totals is a fact about Kalpa Retail. Whoever reads your answer cannot tell which default you chose, so you have to tell them.

### Where this pattern lives in production

Missing fields are the normal state of data that came from more than one system, and every team ends up with a written rule for each optional field saying what absent means for that field. The teams that skip the writing down are the ones where two dashboards disagree and nobody can say which default each one used.

---

## E3. The misplaced accumulator

### The idea being tested

An accumulator works because it is set up once and added to many times. Move the setup inside the loop and the mechanism is gone, and the code carries on looking almost exactly the same.

### The answer

It prints `1460`.

`total = 0` sits inside the loop body, so it runs again on every delivered card and wipes out whatever the last card left there. The line under it then adds that card's amount to a fresh zero. When the loop finishes, `total` holds the amount of the last delivered card and nothing else. That card is KR4224 at Rs 1,460, and Rs 1,460 is a total of nothing at all.

The repair is to move one line above the `for`, with no indent:

```
total = 0
for r in records:
    if r["status"] == "delivered":
        total = total + r["amount"]

print(total)
```

```
25720
```

That is the number the notebook handed you at the start of the day, and it is 13 delivered orders totalling Rs 25,720.

### Why this one is more dangerous than the TypeError

The `TypeError` stopped the cell, named the operator and named both types. It cost you a minute and it could not be ignored.

This cell stopped nothing. It produced Rs 1,460, which is an entirely plausible order-sized number, on a line that reads like a total. Nothing on screen tells you it is wrong, so the only thing standing between it and a slide is whether somebody looks at it and thinks.

### The check you can do in your head

A total over a group of orders can never be smaller than the largest single order in that group. The largest delivered order here is Rs 2,880, and Rs 1,460 is smaller than that, so the number is impossible before you have read a single line of the code. Get into the habit of sanity-checking a total against one record you can see.

### Where this pattern lives in production

Reset-inside-the-loop is one of the few defects that survives code review, because the code reads almost right and the output is a number of the size everybody expected. Wrong-output failures cost far more than crashes, for the simple reason that a crash gets fixed the same day.

---

## E4. The three questions

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
