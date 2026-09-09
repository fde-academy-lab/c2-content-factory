# Day 1, E2. Mid-session: predict the output

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
