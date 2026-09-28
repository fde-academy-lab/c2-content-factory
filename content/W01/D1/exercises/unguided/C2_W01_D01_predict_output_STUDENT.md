# Mid-session drill: predict before you run

Fifteen minutes. Items 1 to 3 are the three cells on the screen: write your prediction, compare
with your partner, then run them. Items 4 to 6 set the same traps in new places, for pairs who
finish first.

Post one line, six letters in item order, no spaces:

```
Post exactly this shape: xxxxxx
```

---

### Q1

```python
ORDERS[0]["Amount"]
```

What does it print?

a) 2300, because Python ignores the case of a key
b) An error, because the key is amount in lower case
c) None, because a missing key gives back nothing
d) An empty string, since the field exists and is blank

### Q2

```python
"3500" > 3000
```

What does it print?

a) True, since 3500 is the bigger of the two
b) False, because text always sorts after numbers
c) An error, because text and a number cannot be ordered
d) True, since Python converts the text to a number first

### Q3

```python
round(30 / 23, 2)
```

What does it print?

a) 1.3, since the value 1.30 is the number 1.3
b) 1.30, because round keeps two places
c) 1.31, since round always rounds up
d) 1.30434, since round keeps the digits it was given

### Q4

```python
count = 0
for order in ORDERS[:5]:
    count = 0
    count = count + 1
print(count)
```

What does it print?

a) 5, one for each order
b) 0, because the reset comes last
c) An error, since count is assigned twice in one loop
d) 1, because the start sits inside the loop

### Q5

```python
total = 0
for amount in [1200, 950, "1800"]:
    total += amount
```

What happens when it runs?

a) total ends at 3950, since the text is converted
b) total ends at 2150 and no error appears
c) A TypeError on the third pass, with total left at 2150
d) A ValueError on the third pass, because "1800" has no comma

### Q6

```python
amounts = [940, 1190, 2060, 2110, 2300]
print(amounts[len(amounts) // 2])
```

What does it print?

a) 2060
b) 1190
c) 2110
d) 2085.0
