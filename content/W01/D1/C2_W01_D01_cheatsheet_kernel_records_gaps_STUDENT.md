# Cheat sheet, gap variant: the kernel and the records

Week 1, Day 1. The same eight panels with about a quarter of the cells blanked. Every blank is
written as `__________ [n]` and the answer key sits at the bottom of this file, so cover it with a
sheet of paper and fill the panels from memory first. Filling this in twice a week is worth more than
reading the full sheet ten times.

---

## Panel 1: the workbench

The kernel is a workbench that holds whatever you put on it for as long as it is running.

| The move | What it does to the bench | What it does to the file |
|---|---|---|
| You run a cell. | It puts a name and a value on the bench. | It changes nothing on disk. |
| You restart the kernel. | __________ [1] | __________ [2] |
| You restart and run all. | It rebuilds the bench from the top in a few seconds. | It changes nothing on disk. |

The notebook file and the kernel state live in two different places, and only one of them is erased
by a restart.

**Crux:** a restart costs you __________ [3] and never __________ [4], which is why the recovery is
cheap.

---

## Panel 2: cells run in the order you ran them

The kernel sees your run history and has no opinion at all about __________ [5].

```
[2]  records = [ ... ]
[3]  count = 0
[1]  for r in records:
```

The cell at the bottom ran first, and the counter in the square brackets is the only honest record of
what happened.

```
__________ [6]
```

You asked for a name the bench was not holding, and the message names the exact word it went looking
for.

**Crux:** when an output surprises you, read __________ [7] before you read the code.

---

## Panel 3: four types, and the question you ask

| Type | What it holds | From today's file |
|---|---|---|
| `str` | It holds text, including text made only of digits. | The id `"KR4224"` and the amount `"4500"` on KR4200. |
| `int` | __________ [8] | The amount `1460` on KR4224. |
| `float` | It holds a number with a decimal part. | A value such as `1460.5`. |
| `bool` | __________ [9] | The result of `2395 > 2000`. |

```
type("4500")        __________ [10]
type(4500)          <class 'int'>
type(4500 > 2000)   <class 'bool'>
```

**Crux:** ask a value what it is before you change any code, because __________ [11] is the easiest
character on the line to skip.

---

## Panel 4: the comparison Python refuses

```
if r["amount"] > 2000:
```

```
__________ [12]
```

The loop stops on __________ [13], the first card in the file, whose amount is the text `"4500"`.

The fix converts at the point of use, so the record stays as it is and the comparison gets a number.

```
if __________ [14] > 2000:
```

With that one change the cell walks all thirty records and reports __________ [15] orders above
Rs 2,000 totalling Rs __________ [16].

**Crux:** Python refuses rather than guessing, and a spreadsheet would have handed you a number with
no warning attached to it.

---

## Panel 5: the loop, the condition and the accumulator

```
count = 0
total = 0
for r in records:
    if r["status"] == "delivered":
        count = count + 1
        total = total + __________ [17]

print(count, total)
```

```
13 __________ [18]
```

The zeros sit __________ [19] and inside the same cell, so rerunning the cell starts from zero
instead of adding a second copy onto the first run.

Move `total = 0` inside the loop and the cell still runs, printing `1460`, which is the amount of
KR4224 and __________ [20].

**Crux:** a total over a group of orders can never be smaller than __________ [21], so check the
number before you trust the code.

---

## Panel 6: lists, and the second name

```
ids = ["KR4200", "KR4201", "KR4202"]

ids[0]      "KR4200"
ids[1:3]    __________ [22]
```

Counting starts at zero, and a slice stops __________ [23].

```
a = ["KR4200", "KR4201"]
b = a
b.append("KR4202")

len(a)      __________ [24]
```

`b = a` gives one list a second name, so appending through either name changes what both names show.
Write __________ [25] when you want a second list on purpose.

**Crux:** one list with two names is one list, and the bug it causes shows up far from the line that
caused it.

---

## Panel 7: records, the missing key and the default

```
r["status"]             "delivered"
r["amount"]             1460
records[0]["discount"]  __________ [26]
```

Two of the thirty orders carry a `discount` field and twenty-eight carry no such field at all, so
absent is a different thing from __________ [27].

```
r.get("discount", 0)
```

| The default you write | What the thirty records total | What it claims |
|---|---|---|
| `r.get("discount", 0)` | The discounts total Rs __________ [28]. | It claims that a record with no discount field was not discounted. |
| `r.get("discount", 100)` | The discounts total Rs __________ [29]. | __________ [30] |

Both cells run to the end and both print a clean number.

**Crux:** the default is a decision you own, and it leaves no mark on the screen once the cell has
run, so you have to say it out loud.

---

## Panel 8: reading an error in three questions

| The question | Where you find the answer |
|---|---|
| __________ [31] | It is the first word on the last line of the message. |
| Which line is mine? | It is the line the message points at in your own cell. |
| __________ [32] | It is the thing named in quotes or described by type at the end of the message. |

The third question is the one people skip, and it is the one that __________ [33].

| Today's error | What it was holding |
|---|---|
| `NameError: name 'records' is not defined` | It was holding nothing, because the setup cell had not run. |
| `TypeError: '>' not supported between instances of 'str' and 'int'` | __________ [34] |
| `KeyError: 'discount'` | It was holding a record that has no field of that name. |

**Crux:** every one of these names the thing it choked on, so read it before you edit anything.

---

## Answer key

Cover this half of the page while you fill the panels in, and check yourself only once you have
written something in every blank.

1. It sweeps the bench completely clean.
2. It changes nothing on disk.
3. the state
4. the file
5. where a cell sits on screen
6. `NameError: name 'records' is not defined`
7. the execution counters
8. It holds a whole number you can do arithmetic with.
9. It holds `True` or `False`, which every comparison hands back.
10. `<class 'str'>`
11. the quotes
12. `TypeError: '>' not supported between instances of 'str' and 'int'`
13. KR4200
14. `int(r["amount"])`
15. 13
16. 35,020
17. `int(r["amount"])`
18. 25720
19. above the loop
20. a total of nothing at all
21. the largest order in that group
22. `["KR4201", "KR4202"]`
23. before its second number
24. 3
25. `b = list(a)`
26. `KeyError: 'discount'`
27. empty
28. 250
29. 3,050
30. It claims a discount of Rs 100 on twenty-eight orders that never recorded one.
31. What is the exception type?
32. What value was it holding?
33. names the record
34. It was holding the text `"4500"` from KR4200 on one side.
