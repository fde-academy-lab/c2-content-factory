# Day 1 solution, E3. The misplaced accumulator

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
        total = total + int(r["amount"])

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
