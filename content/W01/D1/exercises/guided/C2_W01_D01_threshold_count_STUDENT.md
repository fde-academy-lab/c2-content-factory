# Day 1, E1. Guided: the threshold count and total

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
