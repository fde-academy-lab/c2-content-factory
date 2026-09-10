# Day 1, E2. Mid-session: predict the output

Drop point: the close of the first half, after the accumulators, and it runs before the find-the-mistake drill. About 15 minutes, working alone.

Fifteen items. Every one is answerable as a letter, so the thinking is the work and the writing takes a moment. Decide before you run anything, then run the cells and see which of your letters survive.

Post one line at the end, in this shape, using your own letters:

```
1a 2b 3c 4d 5a 6b 7c 8d 9a 10b 11c 12d 13a 14b 15c
```

---

## Item 1

```
print(type('4500'))
```

What appears?

a) `<class 'int'>`
b) `4500`
c) `TypeError`, raised by the quotes
d) `<class 'str'>`

## Item 2

```
print(type(4500) == type('4500'))
```

What appears?

a) `False`, since one is a number and one is text
b) `True`, since both hold four thousand five hundred
c) `<class 'bool'>`, which is what a comparison returns
d) `TypeError`, since two types cannot be compared

## Item 3

Three orders, and one of them was returned.

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

What appears?

a) 5195
b) 3755
c) 1440
d) 2395

## Item 4

Same three orders, one line changed.

```
total = 0
for r in three:
    total = total + r["amount"]

print(total)
```

What appears?

a) 3755
b) 1440
c) 5195
d) 0

## Item 5

```
print("900" > "2000")
```

What appears?

a) `True`, since nine sorts after two
b) `False`, since nine hundred is the smaller number
c) `TypeError`, since text has no size to compare
d) `None`, since neither side is a number at all

## Item 6

```
print(900 > 2000)
```

What appears?

a) `True`
b) `None`
c) `False`
d) `TypeError`

## Item 7

Items 5 and 6 use the same operator and disagree. Somebody reads both printed lines and never sees the code. Which one should they trust?

a) Item 5, since a text comparison is the stricter one
b) Item 6, since both of its sides are numbers
c) Neither, since Python compared neither pair honestly
d) Both, since the operator is the same in each

## Item 8

What would they have to see before they could tell which line to trust?

a) The value of `total` after the loop finished
b) The number of records the file happens to hold
c) The name of whoever ran the cell that morning
d) The type of both operands in each comparison

## Item 9

```
count = 0
for r in three:
    count = count + 1
    if r["status"] == "returned":
        count = count + 1

print(count)
```

What appears?

a) 4
b) 3
c) 1
d) 6

## Item 10

```
amount = "1460"
print(amount + "0")
```

What appears, and what is it?

a) 1470, as a number
b) 14600, as text
c) 14600, as a number
d) `TypeError`, since text has no addition

## Item 11

```
amount = 1460
print(amount + "0")
```

What appears?

a) `TypeError`, naming both types
b) 14600, as text, exactly as item 10 did
c) 1470, since the zero is read as a number
d) `"14600"`, printed with its quotes around it

## Item 12

Thirteen delivered orders total Rs 25,720. What is the average delivered order, to the nearest rupee?

a) Rs 1,460
b) Rs 2,572
c) Rs 1,940
d) Rs 1,978

## Item 13

The thirty amounts in the file add up to Rs 58,210 and the delivered thirteen come to Rs 25,720. What share of the money sits in orders that were not delivered?

a) About a fifth
b) About a third
c) About half
d) About four fifths

## Item 14

True or false. A cell that prints a number without raising has produced a number you can hand to somebody.

a) True
b) False

## Item 15

```
is_large = 2395 > 2000
print(type(is_large))
```

What appears?

a) `<class 'int'>`, since True counts as one
b) `<class 'str'>`, since it prints as a word
c) `<class 'bool'>`
d) `True`, which is the value rather than the type

---

Post your fifteen letters on one line in the shape shown at the top. The solution is released at the close of the session.

## Hands-on

Items 1 to 8 are the reading half. The running half is `notebooks/C2_W01_D01_ex1_hands_on_STUDENT.ipynb`, which asks you to build the three counting answers with pick-from-options markers and checks that tell you whether each step landed. Post its five letters on the same line as these fifteen.
