# Chapter 9. The diagnostic, worked: every question in sequence, its answer, and why the other options fail

Week 0 foundations guide, chapter 9 of 9. [Back to the map](C2_W00_D02_foundations_00_map_STUDENT.md).

The forty questions follow here in the order they were set, Q1 to Q40, with the section breaks of the paper. Each carries the question as it was set, the four options with a verdict on each, the answer, and the reasoning step by step. Use the [question map at the front of this guide](C2_W00_D02_foundations_00_map_STUDENT.md) to jump to any item. Reading time for the whole chapter: 44 minutes; about two minutes per item.

## Section A. Python for data and GenAI, Q1 to Q12

Python for data and GenAI, Q1 to Q12. [Chapter 1](C2_W00_D02_foundations_01_python_STUDENT.md) carries the mechanisms.

<a id="q1"></a>

### Q1 of 40. Predict the output: types do not convert on their own

What does this code print?

```python
orders = ["120", "80", "200"]
total = 0
for o in orders:
    total = total + o
print(total)
```

| Option | Text | Verdict |
|---|---|---|
| A | 400, since the strings are converted to numbers first | Strings are never converted on their own; Python raises rather than guess. |
| B | 12080200, since + joins the strings together | + joins two strings, but total is an int, so the first + is int plus str, which has no meaning. |
| C | TypeError, since int and str cannot be added | **Correct.** total starts as the integer 0 and each o is a string, so the first + raises TypeError. Convert with int(o) before adding. |
| D | 0, since the loop body never runs at all | The loop runs three times; the failure happens inside the first iteration. |

**Answer.** C.

**Step by step.**

1. Read the types before the operator: total starts as the integer 0, and every o taken from orders is a string such as "120".
2. On the first pass the expression is 0 + "120", an int plus a str. Python's + has a meaning for two numbers and for two strings and no meaning across the two.
3. Python does not convert on its own, so it raises TypeError: unsupported operand type(s) for +: 'int' and 'str', and print(total) never runs.
4. The repair is one conversion, total = total + int(o), which makes the loop print 400.

<a id="q2"></a>

### Q2 of 40. Spot the bug, if there is one: two names, one list

Kavya expected q1 to stay as [4, 9, 7]. The code prints 4 9. Which statement is right?

```python
q1 = [4, 9, 7]
q2 = q1
q2.append(3)
print(len(q1), sorted(q1)[-1])
```

| Option | Text | Verdict |
|---|---|---|
| A | There is a bug: q2 = q1 should have copied the list and Python failed to, so the change leaked into q1 | Assignment is not a copy and never was; Python did what it always does. |
| B | The code is right: q2 = q1 makes both names refer to one list; q2 = q1.copy() would give a separate one | **Correct.** Assignment never copies a list. q1 and q2 are two names for one object, so an append through either name shows through both. q1.copy() or list(q1) makes a separate list. |
| C | append() cannot affect q1 because it was called on q2, so the printed 4 must come from somewhere else in the program | A method call acts on the object, not the name, so a change through q2 is visible through q1. |
| D | sorted() changed q1 in place, and that in-place sort is what added the fourth element to the list | sorted() returns a new list and leaves q1 untouched; append() added the element. |

**Answer.** B.

**Step by step.**

1. q2 = q1 binds a second name to the same list object; nothing is copied.
2. q2.append(3) changes that one object, so q1 now refers to [4, 9, 7, 3] as well.
3. len(q1) is 4 and sorted(q1)[-1] is the largest value, 9, so the output 4 9 is exactly what the code says.
4. The expectation was wrong, the code was not; q2 = q1.copy() is what a separate list needs.

<a id="q3"></a>

### Q3 of 40. Trace the flow (pseudocode): accumulator and running best, strict comparison on a tie

This is pseudocode, not Python. What does it print?

```text
SET running_total TO 0
SET best_day TO none
FOR EACH (day, revenue) IN [(Mon, 40), (Tue, 25), (Wed, 55), (Thu, 55)]
    running_total <- running_total + revenue
    IF best_day IS none OR revenue > best_revenue THEN
        best_day <- day
        best_revenue <- revenue
    END IF
END FOR
PRINT best_day, running_total
```

| Option | Text | Verdict |
|---|---|---|
| A | Thu 175 | The tie goes to the earlier day because the comparison is strict; a later day would win only with >=. |
| B | Wed 120 | The running total is never stopped; it adds every row, ending at 175. |
| C | Thu 55 | The print shows the running total, not best_revenue. |
| D | Wed 175 | **Correct.** The comparison is strict (>), so Thursday's 55 does not replace Wednesday's 55. The running total is 40 + 25 + 55 + 55 = 175. |

**Answer.** D.

**Step by step.**

1. Set up two columns, running_total and best_day with best_revenue, and walk the four rows in order.
2. Mon 40: total 40, best Mon 40. Tue 25: total 65, best unchanged. Wed 55: total 120, 55 > 40 so best becomes Wed 55.
3. Thu 55: total 175; the test is revenue > best_revenue, 55 > 55, which is false, so best stays Wed.
4. The print shows best_day then running_total: Wed 175.

<a id="q4"></a>

### Q4 of 40. Predict the output: counting labels with dict.get

An LLM has labelled six support tickets. What does the code print?

```python
labels = ["refund", "delivery", "refund", "refund", "delivery", "other"]
count = {}
for lab in labels:
    count[lab] = count.get(lab, 0) + 1
print(count["refund"], len(count))
```

| Option | Text | Verdict |
|---|---|---|
| A | 3 3 | **Correct.** count.get(lab, 0) returns 0 for a key it has not seen, so there is no KeyError. Three tickets are labelled refund and there are three distinct keys. |
| B | 3 6 | len(count) counts keys, and there are three distinct labels, not six. |
| C | 6 3 | The two values are swapped: refund count first, then the number of keys. |
| D | KeyError: 'refund' | .get with a default never raises KeyError; that is its purpose. |

**Answer.** A.

**Step by step.**

1. count.get(lab, 0) returns the current count for lab, or 0 the first time a label is seen, so no KeyError is possible.
2. Walking the six labels gives refund 3, delivery 2, other 1.
3. count["refund"] is 3, and len(count) counts keys, not labels, so it is 3.
4. Output: 3 3.

<a id="q5"></a>

### Q5 of 40. Fix the code: reading a nested JSON response

The last line raises TypeError: list indices must be integers or slices, not str. Which replacement for the last line returns the text 'Refund approved'?

```python
resp = {"choices": [{"message": {"role": "assistant", "content": "Refund approved"}}],
        "usage": {"prompt_tokens": 412, "completion_tokens": 9}}
text = resp["choices"]["message"]["content"]
```

| Option | Text | Verdict |
|---|---|---|
| A | `text = resp["choices"]["message"][0]["content"]` | The integer index belongs on choices, the list; message is a dict inside the first element. |
| B | `text = resp["choices"][0]["message"]["content"]` | **Correct.** resp['choices'] is a list, so it needs an integer index first; the message dict sits inside its first element. |
| C | `text = resp.choices.message.content` | A dict has no attributes named after its keys; dot access fails with AttributeError. |
| D | `text = resp["choices"]["message"]["content"][0]` | The list index is still missing at the choices level, and indexing the string at the end returns one character. |

**Answer.** B.

**Step by step.**

1. Read the brackets: resp is a dict; resp["choices"] is a list (square brackets), and lists need an integer index.
2. The first element of that list is a dict with a "message" key; inside it, "content" holds the text.
3. The path therefore reads resp["choices"][0]["message"]["content"], one index per level, left to right.
4. Option B is that path; the others index the wrong level or treat the dict as an object.

<a id="q6"></a>

### Q6 of 40. Predict the output: truthiness drops zero as well as None

What does this code print?

```python
sales = [1200, 0, 900, None, 300]
clean = [s for s in sales if s]
print(sum(clean) / len(clean), len(sales) - len(clean))
```

| Option | Text | Verdict |
|---|---|---|
| A | 600.0 1 | Only None removed would give 600.0 1; but 0 is also false in an if test and is removed too. |
| B | 800 2 | True division always returns a float, so the first number prints as 800.0, not 800. |
| C | TypeError, because None cannot be summed | The comprehension removes None before sum() ever sees it. |
| D | 800.0 2 | **Correct.** In an if test, 0 and None are both false, so the comprehension drops two values. sum(clean) / len(clean) is 2400 / 3, and / always gives a float: 800.0. |

**Answer.** D.

**Step by step.**

1. The comprehension keeps a value only when "if s" is true; in Python both 0 and None are false.
2. So clean is [1200, 900, 300]: two values were dropped, and len(sales) - len(clean) is 2.
3. sum(clean) / len(clean) is 2400 / 3, and / always returns a float, so the first number prints as 800.0.
4. Output: 800.0 2.

<a id="q7"></a>

### Q7 of 40. Which line: integer division hides the fraction

Kavya's calculator gives 833.33 as the Plus average for the same rows, but the function returns 833. Which line causes the difference?

```python
 1  def average_by_tier(rows):
 2      totals = {}
 3      counts = {}
 4      for tier, amount in rows:
 5          totals[tier] = totals.get(tier, 0) + amount
 6          counts[tier] = counts.get(tier, 0) + 1
 7      result = {}
 8      for tier in totals:
 9          result[tier] = totals[tier] // counts[tier]
10      return result
```

| Option | Text | Verdict |
|---|---|---|
| A | Line 9: the // operator discards the fraction | **Correct.** // is floor division and discards the fraction. totals[tier] / counts[tier] keeps it. |
| B | Line 5: totals should be written with += amount | totals[tier] = totals.get(tier, 0) + amount and += are the same operation; line 5 is correct. |
| C | Line 6: counts should start from 1, not 0 | Starting counts at 1 would double-count the first row; line 6 is correct. |
| D | No line: the calculator is showing extra decimals | The calculator is right; the code discards the fraction with //. |

**Answer.** A.

**Step by step.**

1. Lines 5 and 6 accumulate totals and counts correctly; += and the explicit form are identical.
2. Line 9 divides with //, floor division, which discards the fraction: 2500 // 3 is 833.
3. A calculator does true division and shows 833.33, so the difference comes from the operator, not the data.
4. Change // to / on line 9 and the function returns 833.333...

<a id="q8"></a>

### Q8 of 40. Predict the output: a default argument is created once

What does this code print?

```python
def tag_order(order_id, tags=[]):
    tags.append(order_id)
    return tags

a = tag_order("K-101")
b = tag_order("K-102")
print(a, b)
```

| Option | Text | Verdict |
|---|---|---|
| A | ['K-101'] ['K-102'] | The default list is created once, not on every call, so the second call sees the first call's tag. |
| B | ['K-101'] ['K-101', 'K-102'] | return hands back the object itself, not a snapshot, so a and b are the same list and both show two tags. |
| C | ['K-101', 'K-102'] ['K-101', 'K-102'] | **Correct.** A default argument is created once, when the function is defined. Both calls append to that same list, so a and b are the same object. Use tags=None and create the list inside the function. |
| D | The output depends on the Python version | The behaviour is defined by the language and identical across Python versions. |

**Answer.** C.

**Step by step.**

1. A default value is evaluated once, when def runs, so tags=[] creates one list object at definition time.
2. The first call appends "K-101" to that shared list and returns it; a is that list.
3. The second call, with no tags passed, appends "K-102" to the same list and returns it; b is the same object as a.
4. Both names show ['K-101', 'K-102']. The idiom tags=None with a fresh list inside the function gives one list per call.

<a id="q9"></a>

### Q9 of 40. Fix the code: defensive conversion: skip and count the bad rows

The comprehension crashes with ValueError on 'n/a'. Anand wants every bad value skipped and counted, whatever it looks like. Which rewrite does that?

```python
def to_amount(text):
    return float(text.replace(",", ""))

rows = ["1,200", "950", "n/a", "300"]
amounts = [to_amount(r) for r in rows]
```

| Option | Text | Verdict |
|---|---|---|
| A | `amounts, rejected = [], []; for r in rows:; try:; amounts.append(to_amount(r)); except ValueError:; rejected.append(r)` | **Correct.** Only a try/except inside the loop catches every failing value and keeps a record of it. Skipping named strings misses the next bad value; a try around the whole loop drops every row after the first failure. |
| B | `amounts = []; for r in rows:; if r not in ("n/a", "NA", ""):; amounts.append(to_amount(r))` | It skips three named strings and crashes on the next bad value, and it counts nothing. |
| C | `amounts = []; try:; for r in rows:; amounts.append(to_amount(r)); except ValueError:; print("bad row found")` | One try around the whole loop stops at the first bad value and drops every row after it. |
| D | `amounts = [float(r.replace(",", "")) for r in rows if r.strip()]` | It removes the comma handling that '1,200' needs and still crashes on 'n/a'. |

**Answer.** A.

**Step by step.**

1. The requirement has two parts: skip every bad value, whatever it looks like, and count what was skipped.
2. Only a try/except around the single conversion, inside the loop, meets both: each failure is caught where it happens and appended to rejected.
3. A filter on named strings (option B) handles today's bad values and crashes on tomorrow's; a try around the whole loop (option C) stops at the first failure and loses every later row; option D removes the comma handling and still crashes.
4. Option A is the only rewrite that finishes with amounts and rejected both filled.

<a id="q10"></a>

### Q10 of 40. Spot the bug: sorted() on tuples orders by the first element

The code should print the customer with the highest spend, but it prints ('Zara', 700). Why?

```python
customers = [("Asha", 4200), ("Ravi", 9100), ("Zara", 700)]
top = sorted(customers)[-1]
print(top)
```

| Option | Text | Verdict |
|---|---|---|
| A | sorted() returns ascending order, so [-1] picks the smallest value rather than the largest | sorted() is ascending, so [-1] is the largest, which is correct; the problem is what it sorts by. |
| B | Tuples cannot be compared with each other, so the data must be a list of lists first | Tuples compare and sort fine; that is the mechanism producing the surprise. |
| C | 700 is compared as text, and the string '7' sorts after '4' and '9' | 700 is an integer and is never compared here; the names are compared first. |
| D | sorted() orders tuples by their first element, the name, unless a key is given | **Correct.** Tuples compare element by element from the first, so sorted() orders by name. sorted(customers, key=lambda c: c[1])[-1] gives the highest spend. |

**Answer.** D.

**Step by step.**

1. sorted() compares tuples element by element, starting with the first element, which here is the name.
2. Alphabetically Asha, Ravi, Zara, so sorted(customers)[-1] is ("Zara", 700), the last name, not the highest spend.
3. To sort by spend, pass a key: sorted(customers, key=lambda c: c[1])[-1] returns ("Ravi", 9100).
4. Option D names the actual mechanism; the others describe things that are not happening.

<a id="q11"></a>

### Q11 of 40. Predict the output: braces inside a format template are placeholders

Kavya builds a classification prompt from a template. What happens on the second line?

```python
template = ('Classify the ticket as one of {labels}. '
            'Reply as JSON: {"label": ...}. Ticket: {ticket}')
prompt = template.format(labels="refund, delivery, other", ticket="My parcel never came")
```

| Option | Text | Verdict |
|---|---|---|
| A | The prompt is built with both placeholders filled and the JSON kept as written | format() cannot skip the JSON braces; it treats them as a placeholder and fails. |
| B | KeyError, since the braces around "label" read as a third placeholder | **Correct.** str.format() treats every {...} as a placeholder, so {"label": ...} is read as a field named "label" and raises KeyError. Double the braces ({{ }}) or build the JSON part separately. |
| C | SyntaxError, since double quotes cannot sit inside a single-quoted string | Double quotes inside a single-quoted string are valid Python; the string itself is fine. |
| D | The prompt is built but {ticket} is left unfilled because it comes last | format() is all or nothing; it raises before producing any output. |

**Answer.** B.

**Step by step.**

1. str.format() scans the template for every pair of braces and treats each as a placeholder to fill.
2. The JSON example contains {"label": ...}, so format() looks for a keyword argument named "label": ... and finds none.
3. It raises KeyError: '"label"' on the second line; the prompt is never built, in whole or in part.
4. Escape literal braces by doubling them, {{ and }}, or assemble the JSON example outside the template.

<a id="q12"></a>

### Q12 of 40. Fix the code: a repeated inner list is one object

grid should be two independent rows of three zeros. After grid[0][1] = 7 it prints [[0, 7, 0], [0, 7, 0]]. Which first line gives [[0, 7, 0], [0, 0, 0]]?

```python
grid = [[0] * 3] * 2
grid[0][1] = 7
print(grid)
```

| Option | Text | Verdict |
|---|---|---|
| A | `grid = [[0, 0, 0]] * 2` | [[0, 0, 0]] \* 2 repeats one inner list exactly as the original did. |
| B | `grid = list([[0] * 3] * 2)` | list() copies the outer list; both entries still reference one inner list. |
| C | `grid = [[0] * 3 for _ in range(2)]` | **Correct.** [[0] \* 3] \* 2 repeats one inner list twice, so both rows are the same object; list() and copy() copy only the outer list. A comprehension builds a fresh inner list for each row. |
| D | `grid = [[0] * 3] * 2 and then grid = grid.copy()` | copy() is shallow: the outer list is new, the inner list is shared. |

**Answer.** C.

**Step by step.**

1. [[0] \* 3] \* 2 builds one inner list and repeats the reference to it twice, so both rows are the same object.
2. Writing grid[0][1] = 7 changes that one object, which is why row 1 shows the 7 too.
3. list() and copy() copy only the outer list; the two inner references still point at one object.
4. A comprehension, [[0] \* 3 for _ in range(2)], runs [0] \* 3 twice and builds two independent rows.

## Section B. SQL for data and GenAI, Q13 to Q20

SQL for data and GenAI, Q13 to Q20. The pipeline figure in [Chapter 2](C2_W00_D02_foundations_02_sql_STUDENT.md) decides most of these.

<a id="q13"></a>

### Q13 of 40. Predict the result: COUNT(\*) against COUNT(column) with NULL

The orders table below is used for Q13 to Q16 and Q18. What does this query return?

| order_id | customer_id | tier | order_date | amount | status |
|---|---|---|---|---|---|
| 1 | C1 | Plus | 2026-04-02 | 1200 | paid |
| 2 | C2 | Basic | 2026-04-03 | NULL | paid |
| 3 | C1 | Plus | 2026-04-05 | 800 | cancelled |
| 4 | C3 | Student | 2026-04-06 | 300 | paid |
| 5 | C2 | Basic | 2026-04-09 | 500 | paid |

```sql
SELECT COUNT(*), COUNT(amount), SUM(amount)
FROM orders
WHERE status <> 'cancelled';
```

| Option | Text | Verdict |
|---|---|---|
| A | 4, 4, 2000 | COUNT(amount) skips NULL, so it returns 3, not 4. |
| B | 4, 3, 2000 | **Correct.** COUNT(\*) counts rows, COUNT(amount) counts non-NULL amounts, and SUM ignores NULL. After the WHERE removes the cancelled order, four rows remain, three with an amount, summing to 2000. |
| C | 5, 4, 2800 | The WHERE clause removed the cancelled order; five rows are never counted. |
| D | 4, 3, NULL | SUM ignores NULL rather than becoming NULL; it returns 2000. |

**Answer.** B.

**Step by step.**

1. Apply WHERE first: status <> 'cancelled' removes order 3, leaving four rows.
2. COUNT(\*) counts rows: 4. COUNT(amount) counts non-NULL amounts: order 2 is NULL, so 3.
3. SUM(amount) ignores NULL: 1200 + 300 + 500 = 2000.
4. Result: 4, 3, 2000.

<a id="q14"></a>

### Q14 of 40. Fix the query: integer division in SQL

On Postgres this query returns 0 for the orders table, where one order in five is cancelled. Which version returns 0.2?

```sql
SELECT SUM(CASE WHEN status = 'cancelled' THEN 1 ELSE 0 END) / COUNT(*) AS cancel_rate
FROM orders;
```

| Option | Text | Verdict |
|---|---|---|
| A | `SUM(CASE WHEN status = 'cancelled' THEN 1 ELSE 0 END) * 1.0 / COUNT(*)` | **Correct.** Both operands are integers, so Postgres does integer division and 1 / 5 becomes 0. Multiplying by 1.0 (or casting) makes the division decimal. |
| B | `ROUND(SUM(CASE WHEN status = 'cancelled' THEN 1 ELSE 0 END) / COUNT(*), 2)` | Rounding 0 to two decimals is still 0; the truncation happened before ROUND. |
| C | `COUNT(status = 'cancelled') / COUNT(*)` | COUNT(expression) counts rows where the expression is not NULL, which is every row, giving 5 / 5 = 1. |
| D | `AVG(status = 'cancelled')` | PostgreSQL has no AVG over booleans; the query errors. |

**Answer.** A.

**Step by step.**

1. SUM(CASE ...) returns an integer and COUNT(\*) returns an integer, so PostgreSQL performs integer division: 1 / 5 is 0.
2. Making either operand decimal changes the division: multiplying by 1.0 does it without changing the value.
3. ROUND of 0 is still 0; COUNT(expression) counts non-NULL rows, which is all five; AVG over a boolean is not defined on PostgreSQL.
4. Option A returns 0.2.

<a id="q15"></a>

### Q15 of 40. Predict the result: WHERE before grouping, HAVING after

Against the orders table, what does this query return?

```sql
SELECT tier, COUNT(*) AS n
FROM orders
WHERE status = 'paid'
GROUP BY tier
HAVING COUNT(*) > 1;
```

| Option | Text | Verdict |
|---|---|---|
| A | Plus 2 and Basic 2 | Plus has two orders only if the cancelled one is counted, and WHERE removed it. |
| B | Basic 2, Plus 1 and Student 1 | This is the result without HAVING; HAVING drops the groups with a single row. |
| C | No rows, because HAVING must refer to the alias n | HAVING may repeat the aggregate expression; the alias is not required. |
| D | Basic 2 only | **Correct.** WHERE removes the cancelled order before grouping, so Plus has one paid order. HAVING then keeps only groups with more than one row: Basic with 2. |

**Answer.** D.

**Step by step.**

1. WHERE runs first and keeps paid orders only: Plus has 1 (order 3 was cancelled), Basic has 2, Student has 1.
2. GROUP BY tier forms three groups with those counts.
3. HAVING COUNT(\*) > 1 keeps only groups with more than one row, which is Basic alone.
4. Result: Basic 2. HAVING may repeat the aggregate; it does not need the alias.

<a id="q16"></a>

### Q16 of 40. Spot the bug: NULL in a comparison

Kavya expects 4 (five orders minus the one at 800) but gets 3. Why?

```sql
SELECT COUNT(*) FROM orders WHERE amount <> 800;
```

| Option | Text | Verdict |
|---|---|---|
| A | <> is not valid in Postgres, so != must be used for the comparison to run | <> and != are both valid on PostgreSQL. |
| B | COUNT(\*) skips any row that has a NULL in any of its columns | COUNT(\*) counts every row it receives; the row was removed by WHERE, not by COUNT. |
| C | NULL compared with 800 is neither true nor false, so that row is dropped | **Correct.** A comparison with NULL yields unknown, and WHERE keeps only rows that are true, so the NULL-amount order is dropped along with the 800. Use amount <> 800 OR amount IS NULL if NULL rows should count. |
| D | The cancelled row is left out automatically because its status is not paid | Nothing in the query filters on status. |

**Answer.** C.

**Step by step.**

1. Four orders have an amount, one has NULL. For the NULL row, amount <> 800 is neither true nor false but unknown.
2. WHERE keeps only rows whose condition is true, so the NULL row is dropped along with the row that equals 800.
3. Three rows remain, not the four Kavya expected.
4. To keep NULL rows, say so: WHERE amount <> 800 OR amount IS NULL.

<a id="q17"></a>

### Q17 of 40. Spot the bug and fix it: a WHERE on the right table turns a LEFT JOIN into an inner join

Anand wants one row per customer with the count of orders placed in 2026, including customers with none. The tables and the query are below. The query returns only C1 2 and C3 1. Which one-line change returns C1 2, C2 0, C3 1, C4 0?

*customers*

| customer_id |
|---|
| C1 |
| C2 |
| C3 |
| C4 |

*orders*

| order_id | customer_id | order_date |
|---|---|---|
| 1 | C1 | 2026-01-15 |
| 2 | C2 | 2025-11-03 |
| 3 | C1 | 2026-03-02 |
| 4 | C3 | 2026-02-20 |

```sql
SELECT c.customer_id, COUNT(o.order_id) AS orders_2026
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
WHERE o.order_date >= '2026-01-01'
GROUP BY c.customer_id;
```

| Option | Text | Verdict |
|---|---|---|
| A | Move the date condition from WHERE into the ON clause | **Correct.** The LEFT JOIN keeps C2 and C4 with NULL order columns, but the WHERE on o.order_date then throws those rows away. A condition in ON filters the right side before the join, so every customer survives. |
| B | Change COUNT(o.order_id) to COUNT(\*) so that the empty rows are counted | COUNT(\*) would count the NULL-filled rows as 1, and the rows are already gone by the time COUNT runs. |
| C | Change LEFT JOIN to RIGHT JOIN so that the customers side is kept | RIGHT JOIN keeps every order instead of every customer; C4 would still vanish. |
| D | Add HAVING COUNT(o.order_id) >= 0 after GROUP BY | HAVING cannot restore rows WHERE has already removed. |

**Answer.** A.

**Step by step.**

1. The LEFT JOIN keeps every customer; C2 and C4 get NULL in every order column because C2's only order is from 2025 and C4 has none.
2. WHERE o.order_date >= '2026-01-01' is then evaluated on those NULLs, is unknown, and the rows are dropped; the query behaves like an inner join.
3. Moving the date condition into the ON clause filters the orders side before the join, so every customer survives and C2 and C4 count 0.
4. Option A is that one-line change; the other options alter counting or join direction without addressing the NULL rows.

<a id="q18"></a>

### Q18 of 40. Predict the result: aggregates cannot sit in WHERE

Against the orders table, what happens when this runs on Postgres?

```sql
SELECT customer_id, SUM(amount) AS total
FROM orders
WHERE SUM(amount) > 1000
GROUP BY customer_id;
```

| Option | Text | Verdict |
|---|---|---|
| A | It returns the customers whose total is above 1000, in the order they appear | WHERE cannot evaluate SUM; the query does not run. |
| B | It fails: an aggregate is not allowed in WHERE; the condition belongs in HAVING | **Correct.** WHERE runs row by row before any grouping, so no aggregate exists yet and Postgres refuses the query. HAVING SUM(amount) > 1000 after GROUP BY is the right place. |
| C | It returns every customer, since WHERE runs before SUM exists and is quietly skipped | SQL never silently skips a condition; it raises an error. |
| D | It returns no rows, since SUM is NULL at the moment WHERE is evaluated | There is no NULL evaluation; the query is rejected before any row is read. |

**Answer.** B.

**Step by step.**

1. WHERE runs row by row before any grouping, so at that point no aggregate exists to compare.
2. PostgreSQL rejects the query with the error that aggregate functions are not allowed in WHERE.
3. The condition belongs in HAVING, which runs after GROUP BY: HAVING SUM(amount) > 1000.
4. Option B is what happens; the options that return rows describe behaviour SQL does not have.

<a id="q19"></a>

### Q19 of 40. Predict the result: latest row per group with ROW_NUMBER

Farhan's team logs every LLM call made on a support ticket. The llm_calls table below is used for Q19 and Q20. What does this query return?

| call_id | ticket_id | model | prompt_tokens | completion_tokens | cost |
|---|---|---|---|---|---|
| 1 | T1 | small | 400 | 100 | 0.02 |
| 2 | T1 | large | 1200 | 300 | 0.30 |
| 3 | T2 | small | 800 | 50 | 0.03 |
| 4 | T3 | large | 600 | 200 | 0.30 |
| 5 | T2 | small | 200 | 20 | 0.01 |

```sql
SELECT ticket_id, call_id
FROM (
  SELECT ticket_id, call_id,
         ROW_NUMBER() OVER (PARTITION BY ticket_id ORDER BY call_id DESC) AS rn
  FROM llm_calls
) t
WHERE rn = 1
ORDER BY ticket_id;
```

| Option | Text | Verdict |
|---|---|---|
| A | (T1, 1), (T2, 3), (T3, 4) | ORDER BY call_id DESC numbers the highest call first, so rn 1 is the latest call, not the earliest. |
| B | Five rows, because ROW_NUMBER never removes rows | The outer WHERE rn = 1 removes the other rows; five rows is the inner query's output. |
| C | An error, because a window function cannot be used to filter rows | A window function cannot sit directly in WHERE, and this one does not; it is computed in the inner query and filtered outside. |
| D | (T1, 2), (T2, 5), (T3, 4) | **Correct.** ROW_NUMBER() numbers each ticket's calls from the highest call_id down, and rn = 1 in the outer query keeps the latest call per ticket. The window function sits in a subquery, which is why filtering on it works. |

**Answer.** D.

**Step by step.**

1. The inner query numbers each ticket's calls from the highest call_id downward: T1 gets call 2 as rn 1, T2 gets call 5 as rn 1, T3 gets call 4 as rn 1.
2. ROW_NUMBER never removes rows, so the inner query still has five rows.
3. The outer WHERE rn = 1 keeps one row per ticket; it works because the window value was computed in the inner query.
4. Result: (T1, 2), (T2, 5), (T3, 4).

<a id="q20"></a>

### Q20 of 40. Fix the query: join fan-out inflates a SUM

tickets holds one row per ticket with its category: T1 refund, T2 delivery, T3 refund. ticket_tags holds (T1, urgent), (T1, vip), (T2, urgent), (T3, vip). Anand asks for LLM spend by ticket category. The query returns refund 0.94 and delivery 0.04, which adds to 0.98, while the cost column of llm_calls sums to 0.66. Which change gives the right totals?

```sql
SELECT t.category, SUM(c.cost) AS spend
FROM llm_calls c
JOIN tickets t ON t.ticket_id = c.ticket_id
JOIN ticket_tags g ON g.ticket_id = t.ticket_id
GROUP BY t.category;
```

| Option | Text | Verdict |
|---|---|---|
| A | Change SUM(c.cost) to SUM(DISTINCT c.cost), so each cost value is added only once | SUM(DISTINCT) drops the second of the two genuine 0.30 costs and gives refund 0.32, wrong in a new way. |
| B | Add DISTINCT after SELECT, so repeated rows are removed before summing | SELECT DISTINCT removes duplicate output rows after aggregation; the SUM has already counted the repeats. |
| C | Drop the ticket_tags join; the question never uses tags and it repeats T1's calls | **Correct.** A ticket can carry several tags, so joining ticket_tags repeats every llm_calls row once per tag; T1's two tags double its spend. Drop the join. SUM(DISTINCT) would also merge the two genuine 0.30 costs into one. |
| D | Change JOIN tickets to LEFT JOIN tickets, so no ticket is lost from the totals | No ticket is lost; rows are duplicated, and LEFT JOIN changes nothing about that. |

**Answer.** C.

**Step by step.**

1. The raw cost column sums to 0.66; the query returns 0.98, so 0.32 was added by the query itself.
2. T1 has two tags, so each of T1's two calls appears twice after the ticket_tags join; the extra 0.32 is exactly T1's calls counted once more.
3. The question never uses tags, so the join to ticket_tags is the defect; remove it and the totals are refund 0.62 and delivery 0.04.
4. SUM(DISTINCT) would also merge the two genuine 0.30 costs; SELECT DISTINCT acts after the SUM; LEFT JOIN changes nothing about duplication.

## Section C. Numbers and reasoning, Q21 to Q28

Numbers and reasoning, Q21 to Q28. Every item is a rung on [Chapter 3](C2_W00_D02_foundations_03_numbers_STUDENT.md)'s ladder.

<a id="q21"></a>

### Q21 of 40. Reason with numbers: ratios of percentage changes

Kalpa Retail revenue fell 12 percent from Q1 to Q2 while the order count rose 5 percent. Which statement about the average order value must be true?

| Option | Text | Verdict |
|---|---|---|
| A | It fell by about 7 percent | Percentage changes divide; subtracting 5 from 12 is the common wrong move. |
| B | It fell by about 12 percent | It ignores the 5 percent rise in orders, which spreads the smaller revenue over more orders. |
| C | It cannot be determined without the number of customers | Average order value is revenue over orders; customers do not enter the definition. |
| D | It fell by about 16 percent | **Correct.** Average order value is revenue divided by orders: 0.88 / 1.05 is about 0.84, a fall of roughly 16 percent. Percentage changes divide; they do not subtract. |

**Answer.** D.

**Step by step.**

1. Average order value is revenue divided by orders, so its change is the ratio of the two changes.
2. Revenue index 0.88, orders index 1.05: 0.88 / 1.05 is about 0.84.
3. That is a fall of about 16 percent; subtracting the percentages gives 7, which is wrong.
4. The customer count is not needed, since the definition involves only revenue and orders.

<a id="q22"></a>

### Q22 of 40. Reason with numbers: median against mean under one extreme value

Five Plus customers spent Rs 300, 350, 400, 450 and 9,000 this quarter. Meera wants one number on her slide for 'what a typical Plus customer spends'. Which number, and why?

| Option | Text | Verdict |
|---|---|---|
| A | 400, the median, since one bulk buyer drags the mean above the other four | **Correct.** Four of the five customers spent 300 to 450; the mean of 2,100 describes none of them. The median, 400, is what 'typical' means here. |
| B | 2,100, the mean, since it is the only number that uses every value | The mean is dragged to 2,100 by one buyer and describes none of the five. |
| C | 300 to 9,000, the range, since any single number would mislead the board | A range refuses the choice the slide needs. |
| D | 1,250, the midpoint between the mean and the median, as a compromise | The midpoint of the mean and the median is not a statistic; it has no meaning. |

**Answer.** A.

**Step by step.**

1. Sort the values: 300, 350, 400, 450, 9,000. Four of five sit in a narrow band; one is far away.
2. The mean, 2,100, is pulled toward the outlier and describes nobody.
3. The median, 400, is the middle value and describes the typical customer, which is what the slide asks for.
4. The range avoids the decision; the midpoint of mean and median is not a statistic anyone uses.

<a id="q23"></a>

### Q23 of 40. Reason with numbers: compare rates, not counts

A monsoon discount email went to 20,000 customers and produced 400 orders. A plain email went to 5,000 customers and produced 150 orders. Which group responded better?

| Option | Text | Verdict |
|---|---|---|
| A | The discount group, since 400 orders is more than double 150 | Counts from groups of different sizes cannot be compared; 400 of 20,000 is the lower rate. |
| B | The plain-email group, since 3 percent beats 2 percent | **Correct.** Compare rates, not counts: 150 / 5,000 is 3 percent and 400 / 20,000 is 2 percent. The plain email did better per person reached. |
| C | They are level once the group sizes are allowed for | Allowing for size is exactly what shows they are not level: 2 percent against 3 percent. |
| D | It cannot be judged without the revenue per order | Revenue per order answers a different question from response. |

**Answer.** B.

**Step by step.**

1. Turn counts into rates: discount group 400 / 20,000 = 2 percent; plain group 150 / 5,000 = 3 percent.
2. The plain email produced more orders per person reached, so it responded better.
3. Four hundred beats 150 only as a count, and the groups differ four to one in size.
4. Revenue per order answers a different question; response rate is what was asked.

<a id="q24"></a>

### Q24 of 40. Two statements: percentage changes do not add

Statement I: A number that rises 10 percent and then falls 10 percent is back where it started.

Statement II: A number that falls 50 percent needs a rise of 100 percent to recover.

| Option | Text | Verdict |
|---|---|---|
| A | Only I is true | Statement I is false: 1.10 times 0.90 is 0.99. |
| B | Both are true | Statement I is false, so both cannot be true. |
| C | Only II is true | **Correct.** 1.10 x 0.90 = 0.99, so Statement I is false. Halving needs a doubling to recover, so Statement II is true. |
| D | Neither is true | Statement II is true: halving needs a doubling to recover. |

**Answer.** C.

**Step by step.**

1. Statement I: 1.10 times 0.90 is 0.99, so a 10 percent rise then fall lands 1 percent below the start; false.
2. Statement II: after a 50 percent fall the value is 0.5 of the start; returning needs a factor of 2, which is a 100 percent rise; true.
3. Only II is true.

<a id="q25"></a>

### Q25 of 40. Reason with numbers: small counts move for no reason

A clinic with 50 bookings a week saw its no-show rate go from 10 percent to 14 percent this week. What is the fairest reading?

| Option | Text | Verdict |
|---|---|---|
| A | Two extra no-shows out of 50 sits inside normal week-to-week noise; watch a few more weeks | **Correct.** The rate moved from 5 no-shows to 7 out of 50. A change of two events sits well inside week-to-week noise for a count that small; several more weeks are needed before it means anything. |
| B | A rise from 10 to 14 percent is a 40 percent jump in the rate, which needs action this week | The 40 percent is a relative change on two events out of fifty; it is arithmetic on noise. |
| C | The rate has been miscalculated, since 7 out of 50 is 12 percent and not 14 | 7 out of 50 is 14 percent; the arithmetic in the option is wrong. |
| D | Nothing can be said either way until a proper significance test has been run | The size of the count already says this is within noise; no test is needed to say so. |

**Answer.** A.

**Step by step.**

1. Convert the percentages to events: 10 percent of 50 is 5 no-shows; 14 percent of 50 is 7.
2. A change of two events on a base of fifty sits inside ordinary week-to-week variation for a count that small.
3. The relative jump of 40 percent is arithmetic on that noise; the arithmetic in option C is simply wrong; refusing to say anything until a test runs ignores what the numbers already show.
4. The fair reading is to watch several more weeks before acting.

<a id="q26"></a>

### Q26 of 40. Reason with numbers: base rates: precision from recall and prevalence

A fraud model flags 5 percent of all transactions. It catches 90 percent of the transactions that are actually fraudulent, and fraud is 1 percent of all transactions. Of the flagged transactions, roughly what share are actually fraud?

| Option | Text | Verdict |
|---|---|---|
| A | About 90 percent | 90 percent is recall, the share of fraud caught; it says nothing about the share of flags that are fraud. |
| B | About 5 percent | 5 percent is the flag rate, an input, not the precision. |
| C | About 1 percent | 1 percent is the base rate, an input, not the precision. |
| D | About 18 percent | **Correct.** Of 1,000 transactions, 10 are fraud and the model catches 9 of them, while it flags 50 in total. So 9 of 50 flagged transactions, about 18 percent, are fraud. Catching 90 percent of fraud (recall) is not the same as 90 percent of flags being fraud (precision). |

**Answer.** D.

**Step by step.**

1. Take 1,000 transactions. Fraud is 1 percent: 10 cases. The model catches 90 percent: 9 flagged fraud cases.
2. The model flags 5 percent of everything: 50 flags in total, so 41 of the flags are not fraud.
3. Precision is 9 / 50, about 18 percent: of the flagged transactions, roughly one in five is fraud.
4. 90 percent is recall, the share of fraud caught, and the other numbers are inputs, not the answer.

<a id="q27"></a>

### Q27 of 40. Reason with numbers: mix shift can reverse a total

Overall conversion fell from 5 percent to 4 percent, yet conversion rose in every single city. How can both be true?

| Option | Text | Verdict |
|---|---|---|
| A | They cannot both be true, since the total is just the cities added up; one figure must be wrong | Both can be true; the total is a weighted average, and the weights changed. |
| B | The mix shifted toward cities with lower conversion, so the total fell as each city rose | **Correct.** The overall rate is a weighted average of the city rates. If more customers now come from low-conversion cities, the total can fall while every city improves. This is a mix shift. |
| C | Rounding in the city figures hides small falls that only show up in the total | Rounding cannot reverse the direction of every city at once. |
| D | Seasonality moves the total without moving any single city's own figure | The total is made of the cities; nothing can move it without moving them. |

**Answer.** B.

**Step by step.**

1. The overall rate is a weighted average of the city rates, weighted by how many customers came from each city.
2. If the share of customers from low-converting cities grew, the total can fall while every city's own rate rises.
3. Rounding cannot reverse a direction in every city, and seasonality that moved the total would show in the cities too.
4. The mix shifted; the question to ask is where the traffic went.

<a id="q28"></a>

### Q28 of 40. Estimate: token economics, multi-step estimate

Farhan plans one LLM call per support ticket. Suppose the model bills Rs 40 per million input tokens and Rs 160 per million output tokens, and a call uses about 1,200 input tokens and 200 output tokens. At 1,000 tickets a day for 30 days, the monthly bill is closest to

| Option | Text | Verdict |
|---|---|---|
| A | Rs 1,440 | Rs 1,440 is the input tokens alone; output tokens cost Rs 960 more. |
| B | Rs 6,720 | Rs 6,720 applies the Rs 160 output price to all 42 million tokens. |
| C | Rs 2,400 | **Correct.** Input: 1,000 x 1,200 x 30 = 36 million tokens, Rs 1,440 at Rs 40 per million. Output: 6 million tokens, Rs 960 at Rs 160 per million. Total Rs 2,400 a month. |
| D | Rs 24,000 | Rs 24,000 is a decimal slip: the token counts are in millions and the prices are per million. |

**Answer.** C.

**Step by step.**

1. Input tokens: 1,000 tickets x 1,200 tokens x 30 days = 36 million; at Rs 40 per million that is Rs 1,440.
2. Output tokens: 1,000 x 200 x 30 = 6 million; at Rs 160 per million that is Rs 960.
3. Total Rs 2,400 a month.
4. Rs 1,440 forgets the output; Rs 6,720 applies the output price to every token; Rs 24,000 slips a decimal.

## Section D. Case and scenarios, Q29 to Q34

Case and scenarios, Q29 to Q34. The case table is repeated once below; Q33 and Q34 are the language-model scenarios from [Chapter 4](C2_W00_D02_foundations_04_language_models_STUDENT.md).

<a id="q29"></a>

### Q29 of 40. Case: Kalpa Retail, Q1 against Q2: which branch moved

Meera Raghavan, CEO of Kalpa Retail, has one question for the analytics team: revenue fell from Q1 to Q2, where did it go? Kavya Nair pulled the table below. Use it for Q29 to Q32. Revenue is in Rs lakh.

| Tier | Q1 customers | Q1 orders | Q1 revenue | Q2 customers | Q2 orders | Q2 revenue |
|---|---|---|---|---|---|---|
| Plus | 10,000 | 30,000 | 360 | 10,000 | 27,000 | 324 |
| Basic | 40,000 | 60,000 | 420 | 44,000 | 64,000 | 400 |
| Student | 5,000 | 6,000 | 24 | 8,000 | 9,000 | 36 |
| Total | 55,000 | 96,000 | 804 | 62,000 | 100,000 | 760 |

Which line best explains most of the fall?

| Option | Text | Verdict |
|---|---|---|
| A | Plus customers ordered less often at the same order value; that tier carries most of the fall | **Correct.** Plus revenue fell 36 lakh (orders down 10 percent at an unchanged Rs 1,200 per order), Basic fell 20 lakh, Student rose 12 lakh. Plus alone explains most of the net 44 lakh fall. |
| B | Basic customers paid less per order than in Q1; that tier carries most of the fall | Basic's lower order value cost 20 lakh; Plus cost 36 and carries most of the fall. |
| C | Student growth pulled spending away from the Plus tier, which is why Plus orders fell by a tenth | The table shows no link between Student growth and Plus orders; it is a story, not a finding. |
| D | Fewer customers overall placed orders in Q2, which lowered revenue across every tier | Customers rose from 55,000 to 62,000; fewer customers is contradicted by the table. |

**Answer.** A.

**Step by step.**

1. Read the deltas first: Plus 360 to 324 is a fall of 36 lakh; Basic 420 to 400 is 20; Student 24 to 36 is a rise of 12; net 44 down.
2. Plus carries most of the fall. Inside Plus, customers are flat at 10,000, orders fell 30,000 to 27,000, and revenue per order stayed at Rs 1,200.
3. So Plus customers ordered less often at the same order value.
4. Basic's lower order value is real but smaller; the customer count rose overall; nothing links Student growth to the Plus fall.

<a id="q30"></a>

### Q30 of 40. Case: Kalpa Retail, Q1 against Q2: test a hypothesis against the table

Kavya's first hypothesis is that Plus customers are downgrading to Basic. What does the table say about it?

| Option | Text | Verdict |
|---|---|---|
| A | It supports it, since Basic gained 4,000 customers | Basic gaining customers is consistent with new sign-ups; it does not show where they came from. |
| B | It supports it, since the Basic order value fell | Basic's order value says nothing about Plus customers moving. |
| C | It weakens it, since the Plus customer count did not fall | **Correct.** Plus customers were 10,000 in both quarters. If Plus customers had moved to Basic, the Plus count would have dropped. The table weakens the hypothesis. |
| D | It cannot be judged without customer-level churn data from both quarters | The table already carries the test: the Plus customer count did not fall. |

**Answer.** C.

**Step by step.**

1. If Plus customers moved to Basic, the Plus customer count would fall unless upgrades replaced them exactly.
2. The table shows Plus at 10,000 in both quarters, so the count did not fall.
3. That weakens the hypothesis with evidence already on the page; the Basic rise is consistent with new customers, not with downgrades.
4. Churn data would refine it, but the table already gives a verdict.

<a id="q31"></a>

### Q31 of 40. Case: Kalpa Retail, Q1 against Q2: the fair comparison

A monsoon discount was given to some Basic customers in Q2. Meera asks whether it caused the rise in Basic orders. Which comparison is the fairest one available?

| Option | Text | Verdict |
|---|---|---|
| A | Basic Q2 orders against Basic Q1 orders, since the before-and-after is the change in question | Before and after mixes the discount with season, festivals and trading days. |
| B | Discounted Basic customers against non-discounted Basic customers, same weeks | **Correct.** The fair comparison holds everything else constant: same tier, same weeks, the discount as the only difference. Before-and-after and cross-tier comparisons mix the discount with every other change. |
| C | Basic Q2 orders against Plus Q2 orders, since Plus had no discount | Plus is a different tier with different behaviour; the comparison varies the wrong thing. |
| D | Basic Q2 revenue against the plan line, since the plan assumed no discount | A plan line is a target, not a comparison group. |

**Answer.** B.

**Step by step.**

1. A fair comparison varies only the thing being tested and holds everything else still.
2. Basic Q2 against Basic Q1 varies the discount together with season, festivals and trading days; Basic against Plus varies the tier; revenue against plan compares with a target, not a group.
3. Discounted Basic customers against non-discounted Basic customers over the same weeks isolates the discount.
4. That is the fairest comparison the data allows.

<a id="q32"></a>

### Q32 of 40. Case: Kalpa Retail, Q1 against Q2: like-with-like windows before presenting

Before you put the Plus finding in front of Meera, which check protects the finding most?

| Option | Text | Verdict |
|---|---|---|
| A | Ask for the Plus tier's marketing budget for Q2 and compare it with Q1's | A budget explains a fall; it does not test whether the fall is real. |
| B | Re-add the six revenue figures in a spreadsheet to confirm that the totals match the table exactly | Re-adding the sums checks arithmetic, not the claim. |
| C | Compute the Plus tier's share of total revenue in each quarter and compare | The share of revenue re-describes the same numbers and protects nothing. |
| D | Check that Q1 and Q2 have the same trading days and that no festival sat in one quarter only | **Correct.** A quarter with fewer trading days, or a festival that sat in Q1 only, can create the whole fall on its own. Checking the window protects the finding; the other options describe or re-add the same numbers. |

**Answer.** D.

**Step by step.**

1. A finding about a fall between two quarters rests on the quarters being comparable.
2. If Q1 and Q2 differ in trading days, or a festival sat in one only, the entire fall can be an artefact of the window.
3. Re-adding the sums checks arithmetic, not the claim; the budget explains rather than tests; the revenue share re-describes the same numbers.
4. Check the window first; it costs one calendar lookup.

<a id="q33"></a>

### Q33 of 40. Scenario: LLM intuition: sampling variance and an under-specified prompt

Farhan's team uses an LLM to label each support ticket as refund, delivery or other. The prompt says only 'Label this ticket'. Sending the same ticket twice gives refund once and delivery the second time. Which explanation and first fix fit best?

| Option | Text | Verdict |
|---|---|---|
| A | Sampling above zero temperature varies the reply, and the prompt never names the labels; lower it and list the three labels with an example each | **Correct.** Sampling with a temperature above zero makes replies vary, and a prompt that never lists the allowed labels leaves the model to invent them. Lower the temperature and give the label set with an example each. API calls carry no memory of each other unless the history is sent. |
| B | The model remembers the first call and changed its mind on the second; clear its conversation history before every call so each starts fresh | Calls carry no memory unless the history is sent; the model cannot change its mind between calls. |
| C | The ticket text must contain a typo or odd formatting that confuses the model; clean the data before calling again and re-check | The same text was sent twice; a typo would produce the same wrong answer twice, not two answers. |
| D | The model is too small for a three-way classification; switch to the largest model available and re-run the whole batch | A larger model still samples above zero temperature and still needs the label set. |

**Answer.** A.

**Step by step.**

1. Two things in the setup can produce different labels: sampling above zero temperature, which picks from the scores rather than always the top one, and a prompt that never names the allowed labels, which leaves the model to invent the set.
2. A call carries no memory of an earlier call, so the model cannot have changed its mind; a typo does not explain two different answers to identical text; a larger model still samples.
3. The first fix is the prompt: list the three labels with an example each and ask for the label alone; the second is a lower temperature.
4. Then validate every reply against the allowed set.

<a id="q34"></a>

### Q34 of 40. Scenario: LLM intuition: a small hand-labelled set is the fastest trust check

Kavya's prompt asks a model to rate the sentiment of each customer review from 1 to 5. On 200 reviews the ratings look plausible. Which check tells her fastest whether the ratings can be trusted?

| Option | Text | Verdict |
|---|---|---|
| A | Ask the model to add a confidence score to each rating and keep the high ones | A confidence score is more model output; it cannot check the model. |
| B | Hand-rate a random 30 reviews herself and compare with the model's ratings | **Correct.** Ratings that look plausible are not evidence. Hand-rating a random sample and comparing gives a measured agreement rate within an hour; confidence scores and a second model only add more unverified output. |
| C | Run the prompt through a second model and average the two ratings for each review | Two models agreeing measures agreement, not accuracy. |
| D | Add 'be accurate and careful' to the prompt and re-run the whole batch | Changing the prompt changes the input; it measures nothing. |

**Answer.** B.

**Step by step.**

1. Plausible output is not evidence; the question is how to produce a number that says how often the ratings are right.
2. Hand-rate a random sample of 30, compare with the model's ratings, and compute agreement, overall and per rating.
3. Confidence scores are more model output; a second model agreeing is two opinions, not a measurement; adding words to the prompt changes the input without measuring anything.
4. Thirty items take under an hour and give a rate you can defend.

## Section E. Judgment calls, Q35 to Q40

Judgment calls, Q35 to Q40. Each situation has a best action and a worst action, and the reasoning names both.

<a id="q35"></a>

### Q35 of 40. Best and worst

You sent Anand Iyer, the Finance Controller, the quarterly revenue figure yesterday. This morning you find your query counted returned orders as sales, so the figure is about 4 percent too high, and it is already in a board deck. Mark the best action and the worst action.

| Option | Text | Verdict |
|---|---|---|
| A | Fix the query so next month's figure is right and say nothing about this one, since 4 percent sits inside normal variance | **Worst.** Saying nothing about a known error in a board figure is the one action that destroys trust when it surfaces later, and it always surfaces. |
| B | Ask a peer to re-run your query and send a correction only once they confirm the error is real | Asking a peer to re-run the query delays a correction you already have; the error is known. |
| C | Send Anand the corrected figure now, with the cause and size of the error | **Best.** Sending the correction yourself, now, with the cause and the size, is the only option that protects the board figure and your credibility at once. |
| D | Tell your reporting manager and let them decide whether Finance needs to hear about it | Passing the decision upward delays it and makes someone else responsible for your number. |

**Answer.** Best C, worst A.

**Step by step.**

1. The figure is already in a board deck, so every hour of delay raises the cost of the correction.
2. Best: send Anand the corrected figure now, with the cause and the size, before anyone else finds it.
3. Worst: saying nothing because the error is small treats a known error in a board figure as acceptable; it will surface, and then the question is why you did not say.

<a id="q36"></a>

### Q36 of 40. Best and worst

During an ungraded exercise you got the answer from an AI assistant and submitted it without understanding it. The trainer asks you to explain your approach to the room. Mark the best action and the worst action.

| Option | Text | Verdict |
|---|---|---|
| A | Ask the trainer to come back to you once you have had time to study the answer properly | Asking for time is honest but avoids the question; the room learns nothing and neither do you. |
| B | Say you used an AI assistant, then walk through what you do and do not yet understand | **Best.** Naming the tool and what you do not yet understand is the honest answer and the one that gets you help on the spot. |
| C | Ask the person next to you, who solved it without help, to explain the approach instead | Handing the explanation to a neighbour avoids the question and shows the room what you did not do. |
| D | Present the answer as your own reasoning and improvise wherever the logic is unclear to you | **Worst.** Presenting borrowed reasoning as your own compounds the gap and is found out within minutes of the first question. |

**Answer.** Best B, worst D.

**Step by step.**

1. The question in the room is about your understanding, and the only durable answer is an honest one.
2. Best: say you used an assistant, then walk through what you do and do not yet understand; that is how you get help on the spot.
3. Worst: presenting borrowed reasoning as your own is discovered by the first follow-up question and costs more than the gap it hides.

<a id="q37"></a>

### Q37 of 40. Best and worst

During your group's presentation a group-mate says, in front of the panel, that your chart is misleading. Mark the best action and the worst action.

| Option | Text | Verdict |
|---|---|---|
| A | Say nothing now, since the panel is watching, and fix the chart after the presentation | Staying silent leaves the panel with the doubt and the chart uncorrected. |
| B | Point out that their own section had errors too, so the panel hears both sides | **Worst.** Retaliating in front of the panel damages both of you and answers nothing about the chart. |
| C | Defend the chart, since you checked the numbers twice before the presentation | Defending before hearing the specific point closes the conversation that could fix the chart. |
| D | Ask what specifically misleads and offer to fix it before the presentation moves on | **Best.** Asking what specifically misleads, in front of the panel, turns criticism into a fix and shows the panel how you work. |

**Answer.** Best D, worst B.

**Step by step.**

1. Criticism in front of a panel is uncomfortable and also useful, if you treat it as a fix.
2. Best: ask what specifically misleads and offer to fix it before the presentation moves on.
3. Worst: retaliating with your group-mate's errors damages both of you and answers nothing about the chart.

<a id="q38"></a>

### Q38 of 40. Best and worst

A take-home is due tonight. Your notebook runs, but the answer to the last question is wrong and you know why; the fix needs two more hours. Mark the best action and the worst action.

| Option | Text | Verdict |
|---|---|---|
| A | Submit on time with a note saying which part is wrong, why, and when the fix follows | **Best.** Submitting on time with a note that names the wrong part, the cause and the fix date keeps both the deadline and your credibility. |
| B | Message the TA that you will submit tomorrow with the fix included, since correctness matters more | Missing the deadline is acceptable when necessary, but here a note would have kept both the deadline and the truth. |
| C | Submit as it is and say nothing, since the notebook runs and the deadline is what counts | **Worst.** Knowingly submitting a wrong answer as right is exactly the failure the note would have prevented. |
| D | Submit only the parts that are right and quietly drop the last question from the notebook | Dropping the question hides the gap instead of naming it. |

**Answer.** Best A, worst C.

**Step by step.**

1. Two things matter: the deadline and the truth about the last answer.
2. Best: submit on time with a note naming the wrong part, why it is wrong and when the fix follows; the reader loses nothing.
3. Worst: submitting silently because the notebook runs presents a known wrong answer as right.

<a id="q39"></a>

### Q39 of 40. Best and worst

You have spent 90 minutes stuck on an environment error while the session moves on without you. Mark the best action and the worst action.

| Option | Text | Verdict |
|---|---|---|
| A | Ask the person next to you to do the setup on your machine so you can catch up with the session | Someone else fixing your setup solves today and teaches nothing; you will meet the same error alone. |
| B | Wait until the end of the day and email a screenshot of the error to the TA | Waiting until the end of the day loses the whole session. |
| C | Post the exact error text in the Discussions thread and continue with the parts that need no setup | **Best.** Posting the exact error text is the fastest route to a fix, and working on the parts that need no environment keeps the day productive. |
| D | Keep trying alone, since asking now would show the room you cannot handle the basics | **Worst.** Ninety minutes alone is already too long; asking early is the habit the programme depends on. |

**Answer.** Best C, worst D.

**Step by step.**

1. Ninety minutes alone on an environment error is already the mistake; the session has moved on.
2. Best: post the exact error text where the TAs will see it and keep working on the parts that do not need the environment.
3. Worst: continuing alone to avoid looking weak loses the day and teaches nothing.

<a id="q40"></a>

### Q40 of 40. Best and worst

Anand says your analysis 'cannot be right' because it contradicts his experience, and asks you to change the conclusion before the meeting. Mark the best action and the worst action.

| Option | Text | Verdict |
|---|---|---|
| A | Change the conclusion; he has run Finance for years and knows the business better than the data | **Worst.** Changing a conclusion because of pushback abandons the evidence and makes the analysis worthless to everyone, including him. |
| B | Walk him through the path from raw table to final number and ask which step he doubts | **Best.** Walking through the path from raw table to number lets him point at the step he doubts, which is either a real error or the end of the disagreement. |
| C | Tell him the numbers do not lie and keep the conclusion exactly as it is | Holding the finding is right; closing the conversation with 'the numbers do not lie' loses the chance to find a real error. |
| D | Escalate to Meera at once so she can decide between his experience and your analysis | Escalating skips the conversation that would settle it and turns a data question into a dispute. |

**Answer.** Best B, worst A.

**Step by step.**

1. Pushback from an experienced stakeholder is information, not an instruction.
2. Best: walk him through the path from raw table to final number and ask which step he doubts; either a real error surfaces or the disagreement ends.
3. Worst: changing the conclusion because he pushed abandons the evidence and makes the analysis worthless to everyone, including him.
