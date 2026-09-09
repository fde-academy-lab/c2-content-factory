# Day 1 exercises

Four pieces of work. Two are short prediction exercises you write down before you run anything, one is built with the trainer while you mirror it on your own Codespace, and one you do alone with no hints.

Nothing here rewards typing speed. Every answer is a prediction, a repair, a short computation or a sentence you could say to the person who asked the question.

---

## E1. Guided: the threshold count and total

Drop point: the opening of the second half, the guided build. About 40 minutes, trainer-led with the room mirroring on their own Codespace.

Someone on the Kalpa Retail side wants to know how many of these thirty orders are above Rs 2,000 and what those orders add up to.

The cell grows one line at a time. Add the line the trainer adds, then read the sentence under it and check that your own bench agrees before the next line goes on. Run the cell from its first line every time, which is why the two zeros live inside the same cell as the loop.

Step 1. Add this line.

```
count = 0
```

The bench now holds `count` with 0 on it.

Step 2. Add this line.

```
total = 0
```

The bench now holds `count` and `total`, both sitting at 0.

Step 3. Add this line.

```
for r in records:
```

Nothing on the bench changes, and the cell will not run yet, because a `for` line needs an indented body underneath it before Python will accept it.

Step 4. Add this line, indented once.

```
    if r["amount"] > 2000:
```

Nothing on the bench changes and the cell still will not run, because an `if` needs a body of its own. Wait for the next step before you run anything.

Step 5. Add this line, indented twice, and now run the cell.

```
        count = count + 1
```

The cell stops and prints this:

```
TypeError: '>' not supported between instances of 'str' and 'int'
```

The bench now holds `r` set to KR4200 and `count` still sitting at 0. The loop stopped on the first card in the file before it could count anything. Read both type names in that message, then go and find KR4200 in the setup cell and look hard at its amount.

Step 6. Replace the line you wrote in step 4 with this one, and run the cell again.

```
    if int(r["amount"]) > 2000:
```

The bench now holds `count` at 13 and `total` still at 0. The loop walked all thirty cards this time, because the comparison is being handed a number on every one of them.

Step 7. Add this line under the counter, indented twice, and run the cell again.

```
        total = total + int(r["amount"])
```

The bench now holds `count` at 13 and `total` at 35020. Nothing has appeared on screen yet, because nothing has asked it to.

Step 8. Add this line at the bottom, with no indent, and run the cell.

```
print(count, total)
```

```
13 35020
```

Say the answer out loud as a sentence before you move on: 13 of the thirty orders are above Rs 2,000, and those orders total Rs 35,020.

One thing to write in your own notebook before you close this exercise. The opening demo gave you 13 delivered orders totalling Rs 25,720, and this build gave you 13 orders above Rs 2,000 totalling Rs 35,020. Those are two different groups of orders that happen to have the same count, so name the group every time you report either number.

---

## E2. Mid-session: predict the output

Drop point: the close of the first half, after the accumulators, and it runs before the find-the-mistake drill below it. About 15 minutes. Write every prediction down before you run a single cell.

Three short cells. For each one, write what you think it prints, then run it and write what it actually printed. The gap between your two columns is the exercise.

Cell 1.

```
print(type('4500'))
print(type(4500))
```

Cell 2.

```
three = [
    {"order_id": "KR4201", "amount": 2395, "status": "delivered"},
    {"order_id": "KR4202", "amount": 1360, "status": "delivered"},
    {"order_id": "KR4203", "amount": 1440, "status": "returned"},
]

total = 0
for r in three:
    if r["status"] == "delivered":
        total = total + r["amount"]

print(total)
```

Cell 3.

```
print("900" > "2000")
print(900 > 2000)
```

Fill this in as you go, and fill the middle column in first.

| Cell | What you predicted | What it actually printed |
|---|---|---|
| Cell 1, the two calls to `type()` | | |
| Cell 2, the accumulator over three records | | |
| Cell 3, the two comparisons written with the same operator | | |

Then answer one more question in one line, without running anything. Somebody reads the two lines cell 3 printed and never sees the code that produced them. Say which of those two outputs they should trust, and say what they would have to look at before they could tell.

---

## E3. Mid-session: find the mistake

Drop point: the close of the first half, after the accumulators. About 15 minutes. Read the cell before you run it.

This cell runs all the way to the end and prints a number.

```
for r in records:
    if r["status"] == "delivered":
        total = 0
        total = total + int(r["amount"])

print(total)
```

1. Before you run it, write down the number you expect to see.
2. Run it. It prints `1460`. Say in one sentence which order that number is the amount of, and why this loop ended up holding it.
3. Repair the cell by moving one line. Write the corrected cell out and run it, then write down what it prints.
4. This cell named no error and stopped nothing. Say in one sentence why a wrong number that runs cleanly is harder to catch than the `TypeError` you met earlier in the day.
5. Give one check you could do in your head, on any total over a group of orders, that would have caught this without reading the code at all.

---

## E4. Unguided: the three questions

Drop point: the close of the second half, after records as dictionaries. About 30 minutes, working alone. No hints from the trainer, the Academic TA, the Support TA or the person next to you.

The same thirty records. Three questions. Answer each one with a loop, a condition and the two accumulators you have been building all day.

1. How many orders are in the Student segment, and what do they total?
2. How many orders were returned, and what do returned orders total?
3. How many delivered orders are above Rs 2,000, and what do they total?

Three rules that make this the real job rather than an exercise.

- Each answer is a count and a total, printed on one line, and then written out as a sentence that names the group it came from. A bare number on its own is not an answer to any of these questions.
- Build each one as its own cell, so you can rerun any single question without disturbing the other two.
- Read the record before you trust the condition. One of these three questions behaves differently from the other two, and the difference is in the data rather than in your code.

Before the solution appears, write down one more thing. Your three counts do not add up to thirty. Say whether that is allowed, and name one order that lands inside two of your three answers.

The solution is released at the close of the session. Keep the notebook you built these three answers in and do not throw the cells away. Tonight's take-home is added to the bottom of that same notebook, and it turns this counter into two buckets either side of a boundary you choose.
