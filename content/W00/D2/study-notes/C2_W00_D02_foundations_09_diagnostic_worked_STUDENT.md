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
