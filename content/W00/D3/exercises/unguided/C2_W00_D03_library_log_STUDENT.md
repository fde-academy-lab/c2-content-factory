# Exercise: the librarian's log

Week 0, Wednesday. About twenty minutes, alone. Every item runs on the class log, the college
library's eight issues, loaded as a list called `log` in which `log[0]` is Algebra borrowed by S01.
Answer each item with one letter, except item 11, which takes four letters in order.

Post one line: 1c 2a 3d 4b 5d 6a 7b 8c 9d 10b 11 dcba 12c

---

### 1

```python
print(len("Poetry"), "Poetry" * 2)
```

What does this line print?

a) 6 PoetryPoetry
b) 12 PoetryPoetry
c) 6 Poetry Poetry
d) 1 PoetryPoetry

### 2

```python
days = 20
print(days / 4, days // 3, days % 3)
```

What does this print?

a) 5 6 2
b) 5.0 6.67 2
c) 5.0 6 0.67
d) 5.0 6 2

### 3

Which expression gives the department of the fifth issue in the log?

a) log[5]["dept"]
b) log["dept"][4]
c) log[4]["dept"]
d) log[4]["issue_id"]["dept"]

### 4

```python
total = 0
for issue in log:
    if issue["dept"] == "Arts":
        total = total + issue["days_kept"]
print(total)
```

What does it print for the class log?

a) 2
b) 9
c) 91
d) 14

### 5

```python
for issue in log:
    count = 0
    if issue["days_kept"] > 14:
        count = count + 1
print(count)
```

Two issues in the class log ran past the 14-day loan, and this prints 0. Which change makes it
print 2?

a) Change `> 14` to `>= 14`.
b) Move `count = 0` above the `for` line.
c) Move `print(count)` inside the loop.
d) Change `count + 1` to `count + issue["days_kept"]`.

### 6

```python
counts = {}
for issue in log:
    student = issue["student"]
    if student not in counts:
        ________
    counts[student] = counts[student] + 1
```

Which line fills the blank?

a) counts[student] = 1
b) counts = {student: 0}
c) counts[student] = 0
d) counts.append(student)

### 7

After the loop in item 6 runs on the class log, what does `counts["S01"]` hold, and how many keys
does `counts` have?

a) 2 and 8
b) 1 and 5
c) 2 and 5
d) 32 and 5

### 8

```python
def days_over(issue):
    print(issue["days_kept"] - 14)

result = days_over(log[6])
print(result)
```

`log[6]` is Chemistry, kept for 21 days. What do the two prints show?

a) 7, and then 7 again
b) 7, and then None
c) None, and then 7
d) 7 alone, and nothing more

### 9

```python
def days_over(issue, loan=14):
    if issue["days_kept"] > loan:
        return issue["days_kept"] - loan
    return 0

print(days_over(log[2]), days_over(log[2], loan=21))
```

`log[2]` is Calculus, kept for 20 days. What does this print?

a) 6 0
b) 6 -1
c) 6 6
d) 20 0

### 10

A traceback from the library's weekly script ends with these three lines:

```
  File "report.py", line 12, in total_late
    late = late + days_over(issue)
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
```

Which reading is right?

a) Line 12 adds two numbers, so the fault lies in the first line of the traceback.
b) `late` holds None, so the loop never set the running total before line 12.
c) The fault is in `report.py` itself, so every function it calls can be ruled out.
d) Line 12 adds None to a number, so `days_over` returned nothing for that issue.

### 11

Put these in the order a running total of days needs them, and post the four letters.

a) print the total, after the loop
b) total = 0
c) for issue in log:
d) total = total + issue["days_kept"], inside the loop

### 12

The librarian wants a number she can add to next week's. Which function gives her one?

a) One that returns the total after the loop
b) One that prints the total inside the loop
c) One that returns the total inside the loop
d) One that prints the total after the loop

---

## Hands-on

Open `notebooks/C2_W00_D03_ex1_hands_on_STUDENT.ipynb`. It runs the same five ideas on the next
week's log, where every number is different, and a check under each step tells you whether your
letter was right. Post its twelve letters as a second line.
