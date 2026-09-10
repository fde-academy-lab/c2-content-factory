# Day 2, E2. Mid-session: trace the calls

Drop point: the close of the first half, after return against print. About 15 minutes, working alone. Trace on paper before you run anything.

Fifteen items on what a function hands back and what its caller is left holding.

Post one line at the end, in this shape, using your own letters:

```
1c 2a 3d 4b 5c 6d 7a 8b 9c 10d 11a 12b 13c 14d 15a
```

---

## Item 1

```
def show_id(record):
    print(record["order_id"])

result = show_id(orders[0])
```

What is `result` holding?

a) `None`
b) The order id, as text
c) The record it was handed
d) An error, since `print` returns nothing

## Item 2

```
print(result["order_id"])
```

Run straight after item 1, what appears?

a) `KR4200`, since the id was printed a moment ago
b) `TypeError` on the subscript
c) `KeyError: 'order_id'`, since result is empty
d) Nothing at all, since result is nothing

## Item 3

Which line of that traceback do you read first?

a) The first, since it says where the run began
b) The one naming your own file
c) The last
d) Whichever one is longest

## Item 4

```
def get_id(record):
    return record["order_id"]

def get_id_2(record):
    print(record["order_id"])
    return record["order_id"]
```

What is the difference to the caller?

a) None, since both show the id
b) `get_id_2` is slower, and nothing else changes
c) `get_id_2` returns nothing, since printing came first
d) `get_id` returns and `get_id_2` also prints

## Item 5

```
def normalise_amount(raw):
    return int(raw)

print(normalise_amount(orders[0]["amount"]) > 2000)
```

Given that KR4200's amount reads `4500` in the CSV, what appears?

a) `True`
b) `False`
c) `TypeError`
d) `ValueError`

## Item 6

```
print(normalise_amount(orders[0]["amount"]) is orders[0]["amount"])
```

What appears?

a) `True`, since it is the same amount
b) `False`
c) `TypeError`, since a number cannot be compared to text
d) `None`

## Item 7

```
def normalise_amount(raw):
    return int(raw)

print(normalise_amount("twelve"))
```

What appears?

a) `12`
b) `TypeError`, since a word is not a number
c) `ValueError`, quoting the word
d) `None`, since the conversion quietly failed

## Item 8

Where does that exception get decided about?

a) Inside `normalise_amount`, which knows what a bad amount means
b) Inside `int`, which chose to raise
c) In the interpreter's own configuration
d) In the caller, which knows what the run is for

## Item 9

```
def normalise_amount_strict(raw):
    value = int(raw)
    if value < 0:
        raise ValueError(f"amount below zero: {value}")
    return value
```

Why is that message better than letting `int` speak?

a) It names your rule and the value that broke it
b) It is longer, so it carries more of the story
c) It stops the exception reaching the caller at all
d) It converts the value before refusing it

## Item 10

```
total = 0
for r in orders:
    try:
        total += int(r["amount"])
    except:
        pass
print(f"Processed {len(orders)} records. Total: {total}")
```

Given two amounts that will not convert, what does that print?

a) `Processed 28 records. Total: 53745`
b) `Processed 30 records. Total: 53745`
c) `Processed 30 records. Total: 0`
d) It raises on the first bad record

## Item 11

What is wrong with that output?

a) The total is wrong, and the count is right
b) Both numbers are wrong
c) The count says thirty, the total used 28
d) Nothing, since both numbers came from the same loop

## Item 12

Replace the bare `except` with `except ValueError` and keep a `kept` counter. What changes?

a) The total changes, and the claim stays the same
b) Nothing, since the same records still fail
c) The loop now stops on the first bad record
d) The total stays and the claim becomes true

## Item 13

Your pass reports 30 in, 28 clean, 2 rejected. Which is the check worth writing?

a) `assert len(clean) + len(rejects) == len(orders)`
b) `assert len(clean) == 28`, today's known number
c) `assert len(rejects) < len(clean)`, a sanity bound
d) `assert total > 0`

## Item 14

The rejects list holds `{"order_id": "KR4210", "reason": "invalid literal for int() with base 10: 'twelve'"}`. Which part earns its place?

a) The order id alone, since it can be looked up
b) Both, since neither is usable alone
c) The reason alone, since it says what went wrong
d) Neither, since the record was skipped anyway

## Item 15

A colleague says the rejects file is extra work nobody asked for. What is the strongest reply?

a) It is required by the programme's style guide
b) It is quicker than fixing the records
c) It is what makes the clean count defensible
d) It doubles as a backup copy of the input file

---

Post your fifteen letters on one line in the shape shown at the top. The solution is released at the close of the session.

## Hands-on

The running half is `notebooks/C2_W01_D02_ex1_hands_on_STUDENT.ipynb`, which walks the same four functions with pick-from-options markers and a check after each step. Post its four letters on the same line as these fifteen.
