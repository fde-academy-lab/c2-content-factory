"""Write the Week 2 Tuesday case notebooks: two TODO twins, their executed solutions and the trainer key.

    python3 content/W02/D2/internal/C2_W02_D02_build_cases_INTERNAL.py

The escalated case is Anand's page, built alone in five parts; the second case is the data platform
lead's audit of the payments feed, in pairs. Each TODO twin carries lettered choices and a check after
every step, and stops at its first placeholder by design. Each solution fills the letters, runs cold
and prints only the checks, since the lists it builds are what the room is meant to find; the
trainer key runs the same cells with every list and figure printed.
"""
import importlib.util
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from nb_make import SETUP, md, code, empty, build  # noqa: E402

DAY = ROOT / "content" / "W02" / "D2"
spec = importlib.util.spec_from_file_location("chapters", DAY / "internal" / "C2_W02_D02_build_notebooks_INTERNAL.py")
chapters = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chapters)
ASK = chapters.ASK

HELPERS = SETUP + '''from decimal import Decimal

conn = kit.connect()
conn.autocommit = True


def run(query, params=None):
    """Run a query on this notebook's one connection and return its rows as dictionaries."""
    return kit.sql(query, params, conn=conn)


def one(query, params=None):
    row = run(query, params)[0]
    return next(iter(row.values()))


def show(rows, caption="", money=()):
    """Rows as the kit's table; columns named in money print as rupees."""
    if not rows:
        return kit.table(["result"], [["no rows"]], caption)
    heads = list(rows[0])
    body = [[("NULL" if r[h] is None else kit.rupees(r[h]) if h in money else
              (f"{int(r[h]):,}" if isinstance(r[h], Decimal) and r[h] == r[h].to_integral_value() else str(r[h])))
             for h in heads] for r in rows]
    kit.table(heads, body, caption)


def crore(v):
    return f"{v:.2f}"
'''

HOW_E = """**How this notebook works.** Each part has lettered TODOs, each with four options, and a check after
it that tells you whether your pick holds, without showing you the answer. It stops at the first
`__TODO1__` with a NameError until you replace the placeholder with your letter, in quotes; that stop
is intended. The empty cells are yours: they print the lists you are finding. At the end, post the
eight letters in order."""

HOW_S = """**How this notebook works.** Each part has a lettered TODO, a check after it and an empty cell where
you read what you found. It stops at the first `__TODO1__` until you fill it, and that stop is
intended. Post the four letters and your request to the platform lead at the end."""

SOLVED = """**How this solution works.** Every letter is filled in and the notebook runs cold from the top, with
every check passing; under each step, a line says why the other letters fail. The empty cells stay
empty here too, since the lists and figures they print are what the case asks you to find: run them
yourself."""

# ============================================================================== the escalated case
# Each TODO is (number, prompt, {letter: option text}, key, fills-the-slot-with, why the others fail).
E_TODOS = {
    1: ("Which rows give the baseline that booked is reconciled to?",
        {"a": "orders o WHERE o.quarter = 'Q2'",
         "b": "orders o WHERE o.quarter = 'Q2' AND o.status = 'delivered'",
         "c": "orders o JOIN payments p ON p.order_id = o.order_id WHERE o.quarter = 'Q2'",
         "d": "orders o LEFT JOIN payments p ON p.order_id = o.order_id WHERE o.quarter = 'Q2'"},
        "a", "b keeps only delivered orders, which is a different definition from Monday's booked; c "
             "drops every unpaid order and repeats every two-instalment order; d keeps every order "
             "and still repeats the two-instalment ones, so its sum is the fan-out."),
    2: ("What grain should the payments CTE have before it meets the orders?",
        {"a": "every payment row summed per order, as the feed posted it",
         "b": "each instalment once, then summed per order",
         "c": "one row per payment, joined straight to the orders",
         "d": "only the earliest payment row of each order, summed"},
        "b", "a counts a retried instalment twice, so collected carries the repeats; c is no grain at "
             "all and fans out; d drops every second instalment, which is real cash."),
    3: ("Which join keeps every Q2 order on the page?",
        {"a": "JOIN", "b": "RIGHT JOIN", "c": "FULL JOIN", "d": "LEFT JOIN"},
        "d", "a drops the orders nobody paid; b keeps payments and drops unpaid orders; c keeps "
             "every order but adds payment rows with no order, which are not Q2's business."),
    4: ("Which condition keeps only the Q2 orders nothing matched?",
        {"a": "p.order_id IS NULL",
         "b": "p.paid_date NOT BETWEEN '2026-07-01' AND '2026-09-30'",
         "c": "p.amount = 0",
         "d": "o.amount > 0 AND p.amount IS NOT NULL"},
        "a", "b is unknown for a NULL date, so it keeps nothing an unpaid order carries; c looks for a "
             "zero payment, and an unpaid order has no payment row at all; d keeps the paid orders."),
    5: ("Which query lists the payments the gateway posted twice?",
        {"a": "GROUP BY p.order_id HAVING count(*) > 1",
         "b": "GROUP BY p.order_id, p.paid_date HAVING count(*) > 1",
         "c": "GROUP BY p.order_id, p.instalment_no HAVING count(*) > 1",
         "d": "WHERE p.instalment_no = 2, one row for each second instalment paid"},
        "c", "a flags every order paid in two instalments; b flags them too, since Kalpa's two "
             "instalments are paid on the same day; d lists legitimate second instalments."),
    6: ("How much was posted beyond one payment of each repeated instalment?",
        {"a": "sum(p.amount)", "b": "sum(p.amount) - max(p.amount)",
         "c": "max(p.amount)", "d": "(count(*) - 1) * sum(p.amount)"},
        "b", "a is everything posted, including the one payment that should be there; c is one payment; "
             "d multiplies the whole sum, which doubles the surplus of a pair."),
    7: ("Which expression gives each channel's gap with the unpaid orders in it?",
        {"a": "sum(booked - collected)",
         "b": "sum(booked) - sum(coalesce(posted, 0))",
         "c": "sum(booked - coalesce(collected, 0))",
         "d": "sum(coalesce(booked, 0) - collected)"},
        "c", "a and d let an unpaid order's NULL fall out of the sum, so the gap loses exactly the "
             "orders it exists to show; b subtracts posted, which still holds the repeats."),
    8: ("Which check proves that collected holds no payment twice?",
        {"a": "collected is at most booked on every channel",
         "b": "collected plus the surplus posted twice equals posted from payments alone",
         "c": "the gap is not negative on any channel",
         "d": "every channel appears on the page with at least one order and one payment"},
        "b", "a and c pass a report that dropped unpaid orders, and they can pass one with repeats in it; "
             "d says nothing about amounts."),
}


def todo_block(n):
    prompt, options, key, _ = E_TODOS[n]
    lines = [f"# TODO {n}. {prompt}"] + [f"#   {k}) {v}" for k, v in options.items()]
    return "\n".join(lines)


def escalated(solution=False, key=False):
    fill = {n: (repr(E_TODOS[n][2]) if solution else f"__TODO{n}__") for n in E_TODOS}
    why = {n: f"**Why the other letters fail.** The key is {E_TODOS[n][2]}. {E_TODOS[n][3]}" for n in E_TODOS}
    cells = [
        md(f"""
# The escalated case: which Q2 orders and channels make the gap, and how do you prove the collected figure counts no payment twice?

**Week 2, Tuesday · The escalated case, alone · Kalpa's warehouse, Q2.**

{ASK}

**Who needs the answer.** Anand signs the page and sends it on to the CEO's Monday numbers, the
collections team rings every order on the unpaid list, and the platform lead receives the repeated
postings. A page that drops an order or keeps a repeat fails each of them.

**The questions on the way.**
1. What did Q2 book, by channel, from orders alone?
2. What did Q2 collect at order grain, and does the count close?
3. Which Q2 orders were never paid?
4. Which payments did the gateway post twice?
5. What does the page say, and which check proves it?

**What you already have.** The six chapters built each move on two invented tables and ran it on the
warehouse: payments are brought to one row per order before any join; the LEFT JOIN with orders first
keeps every booked order; an anti-join finds the orders nothing matched; a retry is the same order and
instalment posted twice; and `coalesce(collected, 0)` keeps an unpaid order in the gap. Booked means
every Q2 order at its amount, whatever its status: 462 orders and Rs 9,84,00,000.

{HOW_E if not solution else SOLVED}
"""),
        code(HELPERS + """
print("Connected to", kit.WAREHOUSE["dbname"], "with", one("SELECT count(*) FROM orders WHERE quarter = 'Q2'"), "Q2 orders.")"""),
        code("""kit.vflow(["1. booked, orders alone", "2. collected at order grain\\nrows in = rows out",
           "3. the unpaid list\\ntotal = the gap", "4. the double-paid list\\nsurplus = posted less collected",
           "5. the page, its checks\\nand the sentence to Anand"], kinds=["known", "plain", "plain", "plain", "good"],
          title="Five parts, each checked against the one before")"""),
        md("""
## Part 1. What did Q2 book, by channel, from orders alone?

Every later figure reconciles to this one, so it comes from the orders table with no join. A finance
team already holds this number, so at work you write it down before any query that joins.
"""),
        code(todo_block(1) + f"""
options_1 = {E_TODOS[1][1]!r}
choice_1 = {fill[1]}

baseline = run(f\"\"\"
SELECT o.channel, count(*) AS orders_in, sum(o.amount) AS booked
FROM {{options_1[choice_1]}}
GROUP BY o.channel
ORDER BY o.channel\"\"\")
show(baseline, "Part 1: Q2 orders and booked by channel", money=["booked"])
kit.columns([r["channel"] for r in baseline], [("booked, Rs crore", [float(r["booked"]) / 1e7 for r in baseline])],
            fmt=crore, title="Q2 booked by channel, from orders alone")"""),
        code("""orders_in = sum(r["orders_in"] for r in baseline)
booked = sum(r["booked"] for r in baseline)
kit.check("the baseline holds all 462 Q2 orders", orders_in == 462, f"{orders_in} orders")
kit.check("booked is Monday's Rs 9,84,00,000", booked == 98400000, kit.rupees(booked))
kit.check("three channels, app, store and web", [r["channel"] for r in baseline] == ["app", "store", "web"])"""),
    ]
    if solution:
        cells.append(md(why[1]))
    cells += [
        md("""
## Part 2. What did Q2 collect at order grain, and does the count close?

Payments are brought to one row per order, each instalment counted once, and joined to the Q2 orders.
At work, Anand's analyst reads this reconciliation before any number, so write it before you run the
cell, then fill it in.

- Rows in, from Part 1: ____
- Rows out, from this query: ____
- The difference, and what it is made of: ____
"""),
        code(todo_block(2) + "\n" + todo_block(3) + f"""
options_2 = {{
    "a": "SELECT order_id, sum(amount) AS collected FROM payments GROUP BY order_id",
    "b": "SELECT order_id, sum(amount) AS collected FROM (SELECT order_id, instalment_no, max(amount) AS amount "
         "FROM payments GROUP BY order_id, instalment_no) i GROUP BY order_id",
    "c": "SELECT order_id, amount AS collected FROM payments",
    "d": "SELECT order_id, sum(amount) AS collected FROM payments WHERE payment_id IN "
         "(SELECT min(payment_id) FROM payments GROUP BY order_id) GROUP BY order_id",
}}
options_3 = {E_TODOS[3][1]!r}
choice_2 = {fill[2]}
choice_3 = {fill[3]}

part2 = run(f\"\"\"
WITH collected_per_order AS ({{options_2[choice_2]}})
SELECT o.channel, count(*) AS rows_out, sum(o.amount) AS booked, sum(coalesce(c.collected, 0)) AS collected
FROM orders o
{{options_3[choice_3]}} collected_per_order c ON c.order_id = o.order_id
WHERE o.quarter = 'Q2'
GROUP BY o.channel
ORDER BY o.channel\"\"\")
kit.flow(["payments\\none row per payment", "each instalment once\\nper order", "joined to Q2 orders",
          "rows out against 462"], kinds=["bad", "plain", "plain", "good"], title="Part 2, the method")"""),
        code("""posted_alone = one("SELECT sum(amount) FROM payments WHERE order_id IN (SELECT order_id FROM orders WHERE quarter = 'Q2')")
repeats = one(\"\"\"SELECT coalesce(sum(extra), 0) FROM (SELECT sum(p.amount) - max(p.amount) AS extra
    FROM payments p JOIN orders o ON o.order_id = p.order_id WHERE o.quarter = 'Q2'
    GROUP BY p.order_id, p.instalment_no) r\"\"\")
rows_out = sum(r["rows_out"] for r in part2)
collected = sum(r["collected"] for r in part2)
kit.check("rows out equal rows in", rows_out == orders_in, f"{rows_out} rows out, {orders_in} in")
kit.check("booked after the join equals booked from Part 1", sum(r["booked"] for r in part2) == booked)
kit.check("collected plus the repeated instalments equals what the feed posted against Q2 orders",
          collected + repeats == posted_alone, "equal, figures unprinted")"""),
    ]
    if solution:
        cells.append(md(why[2] + "\n\n" + why[3]))
    cells += [
        md("""
**Your turn.** Read collected by channel. Type these lines in the empty cell below and run them:

```python
show(part2, "Part 2: booked and collected by channel", money=["booked", "collected"])
```
"""),
        _turn(key, 'show(part2, "Part 2: booked and collected by channel", money=["booked", "collected"])'),
        md("""
## Part 3. Which Q2 orders were never paid?

Every Q2 order with no payment at all goes on this list, largest first. The collections team rings
the list at work, and its total must equal the gap, or it is the wrong list.
"""),
        code(todo_block(4) + f"""
options_4 = {E_TODOS[4][1]!r}
choice_4 = {fill[4]}

unpaid = run(f\"\"\"
SELECT o.order_id, o.channel, o.status, o.amount AS booked
FROM orders o
LEFT JOIN payments p ON p.order_id = o.order_id
WHERE o.quarter = 'Q2'
  AND {{options_4[choice_4]}}
ORDER BY o.amount DESC\"\"\")
kit.flow(["LEFT JOIN\\nevery Q2 order", "keep the misses", "the unpaid list\\nits total against the gap"],
         kinds=["plain", "plain", "good"], title="Part 3, the method")"""),
        code("""gap_from_part2 = booked - collected
paid_ids = one("SELECT count(*) FROM payments WHERE order_id = ANY(%s)", ([r["order_id"] for r in unpaid],))
kit.check("the unpaid list's booked total equals booked less collected from Part 2",
          sum(r["booked"] for r in unpaid) == gap_from_part2, "equal, figures unprinted")
kit.check("no order on the list has a payment row", paid_ids == 0)
kit.check("every order on the list is a Q2 order", all(r["order_id"] in {x["order_id"] for x in run(
    "SELECT order_id FROM orders WHERE quarter = 'Q2'")} for r in unpaid))"""),
    ]
    if solution:
        cells.append(md(why[4]))
    cells += [
        md("""
**Your turn.** Show the list, and its count and total by channel:

```python
show(unpaid, "Part 3: Q2 orders never paid", money=["booked"])
for ch in ("app", "store", "web"):
    rows = [r for r in unpaid if r["channel"] == ch]
    print(ch, len(rows), kit.rupees(sum(r["booked"] for r in rows)))
```
"""),
        _turn(key, 'show(unpaid, "Part 3: Q2 orders never paid", money=["booked"])\n'
                   'for ch in ("app", "store", "web"):\n'
                   '    rows = [r for r in unpaid if r["channel"] == ch]\n'
                   '    print(ch, len(rows), kit.rupees(sum(r["booked"] for r in rows)))'),
        md("""
## Part 4. Which payments did the gateway post twice?

The list holds retries only, since a second instalment is real cash and stays off it. At work it
goes to the platform lead and to Finance, who check with the bank whether a customer was charged
twice.
"""),
        code(todo_block(5) + "\n" + todo_block(6) + f"""
options_5 = {{
    "a": "GROUP BY p.order_id, o.channel HAVING count(*) > 1",
    "b": "GROUP BY p.order_id, o.channel, p.paid_date HAVING count(*) > 1",
    "c": "GROUP BY p.order_id, o.channel, p.instalment_no HAVING count(*) > 1",
    "d": "AND p.instalment_no = 2 GROUP BY p.order_id, o.channel, p.payment_id",
}}
options_6 = {E_TODOS[6][1]!r}
choice_5 = {fill[5]}
choice_6 = {fill[6]}

double_paid = run(f\"\"\"
SELECT p.order_id, o.channel, count(*) AS times_posted, {{options_6[choice_6]}} AS posted_twice
FROM payments p
JOIN orders o ON o.order_id = p.order_id
WHERE o.quarter = 'Q2' {{options_5[choice_5]}}\"\"\")
kit.matrix(["instalment 1 only", "instalments 1 and 2", "instalment 1, twice"], ["what it is", "on this list"],
           [["paid once", "no"], ["paid in two parts", "no"], ["a gateway retry", "yes"]], title="Part 4, the rule")"""),
        code("""kit.check("the list's surplus equals posted less collected, both from Part 2's figures",
          sum(r["posted_twice"] for r in double_paid) == posted_alone - collected, "equal, figures unprinted")
kit.check("every row on the list was posted more than once", all(r["times_posted"] > 1 for r in double_paid))"""),
    ]
    if solution:
        cells.append(md(why[5] + "\n\n" + why[6]))
    cells += [
        md("""
**Your turn.** Show the list and its surplus by channel:

```python
show(double_paid, "Part 4: Q2 instalments posted more than once", money=["posted_twice"])
```
"""),
        _turn(key, 'show(double_paid, "Part 4: Q2 instalments posted more than once", money=["posted_twice"])'),
        md("""
## Part 5. What does the page say, and which check proves it?

The page has one line per channel, with orders, booked, collected, the gap, the unpaid count and the
surplus posted twice. A finance controller signs this page at work, and the check under it lets it
leave the team.
"""),
        code(todo_block(7) + "\n" + todo_block(8) + f"""
options_7 = {E_TODOS[7][1]!r}
options_8 = {E_TODOS[8][1]!r}
choice_7 = {fill[7]}
choice_8 = {fill[8]}

page = run(f\"\"\"
WITH per_instalment AS (
    SELECT order_id, instalment_no, max(amount) AS amount FROM payments GROUP BY order_id, instalment_no
),
per_order AS (
    SELECT o.order_id, o.channel, o.amount AS booked,
           (SELECT sum(amount) FROM per_instalment i WHERE i.order_id = o.order_id) AS collected,
           (SELECT sum(amount) FROM payments p WHERE p.order_id = o.order_id)       AS posted
    FROM orders o
    WHERE o.quarter = 'Q2'
)
SELECT channel, count(*) AS orders, sum(booked) AS booked, sum(coalesce(collected, 0)) AS collected,
       {{options_7[choice_7]}} AS gap,
       count(*) FILTER (WHERE collected IS NULL) AS unpaid_orders,
       sum(coalesce(posted, 0) - coalesce(collected, 0)) AS posted_twice
FROM per_order
GROUP BY channel
ORDER BY channel\"\"\")


def run_check(letter, rows, surplus):
    # the four candidate checks, as code, so the choice can be tested on two pages
    if letter == "a":
        return all(r["collected"] <= r["booked"] for r in rows)
    if letter == "b":
        return sum(r["collected"] for r in rows) + surplus == posted_alone
    if letter == "c":
        return all(r["gap"] is not None and r["gap"] >= 0 for r in rows)
    return len(rows) == 3 and all(r["orders"] > 0 for r in rows)


surplus = sum(r["posted_twice"] for r in double_paid)
padded = [dict(r, collected=r["collected"] + r["posted_twice"], gap=(r["gap"] or 0) - r["posted_twice"]) for r in page]
kit.vflow(["the page", "gaps against the unpaid list", "the check you chose", "the sentence to Anand"],
          kinds=["plain", "good", "good", "known"], title="Part 5, what must hold before the page leaves")"""),
        code("""kit.check("the page's orders add to 462 and its booked to Rs 9,84,00,000",
          sum(r["orders"] for r in page) == 462 and sum(r["booked"] for r in page) == booked)
kit.check("the page's gaps add to the unpaid list's total", sum(r["gap"] or 0 for r in page) == sum(r["booked"] for r in unpaid),
          "equal, figures unprinted")
kit.check("the check you chose passes this page and fails a page that counts the repeats as collected",
          run_check(choice_8, page, surplus) and not run_check(choice_8, padded, surplus), "tested on both pages")"""),
    ]
    if solution:
        cells.append(md(why[7] + "\n\n" + why[8]))
    cells += [
        md("""
**Your turn.** Show the page, then write the sentence to Anand under it from your own figures:

```python
show(page, "Q2: booked against collected, by channel", money=["booked", "collected", "gap", "posted_twice"])
```

> "Q2 booked Rs 9,84,00,000 and collected Rs ___, each payment counted once. The gap of Rs ___ is ___
> orders nobody has paid, listed by channel, largest first. Separately, Rs ___ was posted twice by
> gateway retries, and that list goes to the platform lead. Every figure ties back to the orders and
> payments tables, and collected plus the repeats equals what the feed posted."
"""),
        _turn(key, 'show(page, "Q2: booked against collected, by channel", money=["booked", "collected", "gap", "posted_twice"])'),
        md("""
## What do you post?

Post one line: your eight TODO letters in order, no spaces, then your sentence to Anand.

```
Post exactly this shape: xxxxxxxx
```
"""),
        code("kit.check_summary()"),
    ]
    return cells


def _turn(key, src):
    """An empty your-turn cell in the STUDENT twins; filled in the trainer key."""
    return code(src) if key else empty()


# ================================================================================ the second case
S_TODOS = {
    1: ("Which join accounts for every payment row the feed holds?",
        {"a": "orders o LEFT JOIN payments p ON p.order_id = o.order_id",
         "b": "orders o JOIN payments p ON p.order_id = o.order_id",
         "c": "payments p LEFT JOIN orders o ON o.order_id = p.order_id",
         "d": "payments p JOIN orders o ON o.order_id = p.order_id AND o.quarter IN ('Q1', 'Q2')"},
        "c", "a starts from orders, so a payment with no order never appears and an unpaid order adds a "
             "row the feed does not hold; b and d keep only payments that match an order."),
    2: ("Which condition keeps only the payments that match no order?",
        {"a": "p.order_id IS NULL",
         "b": "o.order_id IS NULL",
         "c": "o.quarter NOT IN ('Q1', 'Q2')",
         "d": "p.amount > 0 AND o.amount IS NULL AND o.quarter = 'Q2'"},
        "b", "a tests the payment's own order id, which the table never leaves empty; c is unknown for a "
             "NULL quarter, so it keeps nothing; d adds a Q2 test that no unmatched row can pass."),
    3: ("Which rows should the retry list cover for the platform lead?",
        {"a": "Q2 orders only, the quarter Anand asked about",
         "b": "Q1 orders only, since Q2 is already on Anand's page",
         "c": "payments made from 1 July only, whatever order they pay",
         "d": "both quarters, all the feed holds"},
        "d", "a and b split one fault across two reports and leave the platform lead half of it; c cuts "
             "by payment date, which is not how the feed files a retry."),
    4: ("Which dates tell the gateway team when the retries happened?",
        {"a": "the first and last paid_date on the retry list",
         "b": "the first and last day of the quarters the orders belong to",
         "c": "the first and last paid_date of every payment in the feed",
         "d": "the paid_date of the first retry, since the rest repeat it"},
        "a", "b and c describe the quarters and the feed, so the window they give starts and ends on days "
             "with no retry; d assumes every retry happened on one day, which the list does not show."),
}


def second_case(solution=False, key=False):
    fill = {n: (repr(S_TODOS[n][2]) if solution else f"__TODO{n}__") for n in S_TODOS}
    why = {n: f"**Why the other letters fail.** The key is {S_TODOS[n][2]}. {S_TODOS[n][3]}" for n in S_TODOS}

    def block(n):
        prompt, options, _, _ = S_TODOS[n]
        return "\n".join([f"# TODO {n}. {prompt}"] + [f"#   {k}) {v}" for k, v in options.items()])

    cells = [
        md(f"""
# The second case: which payment rows in the feed should not be there, and what should the platform lead fix first?

**Week 2, Tuesday · The second case, in pairs · Kalpa's warehouse, both quarters.**

> **The client asks.** "Before I repair the payments feed, tell me which rows in it should not be
> there: payments with no order behind them, and payments the gateway posted twice. Both quarters,
> with the dates, the methods and the rupees at stake, and tell me what to fix first."
>
> The data platform lead, Kalpa Retail

**Who needs the answer.** The platform lead owns the warehouse and the feed that fills it, and
Finance must know whether any customer was charged twice. A feed fix aimed at the wrong
integration costs weeks and leaves the fault in place; a repeat deleted from the warehouse removes
the evidence Finance needs.

**The questions on the way.**
1. Is every payment row in the feed accounted for?
2. Which payments match no order?
3. Which instalments were posted more than once, in either quarter?
4. Is there a pattern the gateway team can act on?

**What you already have.** Anand's question started from the orders, because it was about every
booked order; this one starts from the payments, because it is about every row the feed holds, which
is the fact chapter 1 said would change the join. A retry is the same order and instalment posted
twice, and chapter 4 found the orders side of it for Q2. The warehouse's `payments` table holds 1,428
rows across both quarters.

{HOW_S if not solution else SOLVED}
"""),
        code(HELPERS + """
print("payments holds", one("SELECT count(*) FROM payments"), "rows.")"""),
        code("""kit.vflow(["1. every row accounted for\\npayments first", "2. payments with no order",
           "3. instalments posted twice\\nboth quarters", "4. the pattern\\nand the request"],
          kinds=["known", "plain", "plain", "good"], title="The platform lead's audit, in four parts")"""),
        md("""
## Part 1. Is every payment row in the feed accounted for?

Each payment row belongs to a Q1 order, a Q2 order or no order at all, and the three counts must add
to the table. At work, this is the first query any audit of a feed runs: before explaining any row,
prove that none was lost.
"""),
        code(block(1) + f"""
options_1 = {S_TODOS[1][1]!r}
choice_1 = {fill[1]}

homes = run(f\"\"\"
SELECT coalesce(o.quarter, 'no order') AS home, count(p.payment_id) AS payment_rows
FROM {{options_1[choice_1]}}
GROUP BY coalesce(o.quarter, 'no order')
ORDER BY home\"\"\")
kit.flow(["payments\\nevery row kept", "LEFT JOIN orders", "Q1, Q2 or no order"],
         kinds=["known", "plain", "good"], title="Part 1: start from the table whose every row must survive")"""),
        code("""total_rows = one("SELECT count(*) FROM payments")
kit.check("the homes add to every row in the payments table", sum(r["payment_rows"] for r in homes) == total_rows,
          f"{total_rows:,} rows")
kit.check("every home is a quarter or no order", {r["home"] for r in homes} <= {"Q1", "Q2", "no order"})"""),
    ]
    if solution:
        cells.append(md(why[1]))
    cells += [
        md("""
**Your turn.** Show the three homes and their counts:

```python
show(homes, "Part 1: where each payment row belongs")
```
"""),
        _turn(key, 'show(homes, "Part 1: where each payment row belongs")'),
        md("""
## Part 2. Which payments match no order?

The suspense list holds the payments whose order id is not in the orders table, with their ids,
dates, methods and amounts. At work these are held in a suspense account until someone finds the order, or
learns that the payment was never Kalpa's.
"""),
        code(block(2) + f"""
options_2 = {S_TODOS[2][1]!r}
choice_2 = {fill[2]}

orphans = run(f\"\"\"
SELECT p.payment_id, p.order_id AS paid_for, p.paid_date, p.method, p.amount
FROM payments p
LEFT JOIN orders o ON o.order_id = p.order_id
WHERE {{options_2[choice_2]}}
ORDER BY p.payment_id\"\"\")
kit.flow(["payments LEFT JOIN orders", "keep the rows with no order", "the suspense list"],
         kinds=["plain", "plain", "good"], title="Part 2: the anti-join, from the payments side")"""),
        code("""no_order = next((r["payment_rows"] for r in homes if r["home"] == "no order"), 0)
in_orders = one("SELECT count(*) FROM orders WHERE order_id = ANY(%s)", ([r["paid_for"] for r in orphans],))
kit.check("the list holds exactly the rows Part 1 found on no order", len(orphans) == no_order, "count unprinted")
kit.check("none of the listed order ids exists in the orders table", in_orders == 0)"""),
    ]
    if solution:
        cells.append(md(why[2]))
    cells += [
        md("""
**Your turn.** Show the list and its total, and look at the dates and methods together:

```python
show(orphans, "Part 2: payments that match no order", money=["amount"])
print(len(orphans), "payments,", kit.rupees(sum(r["amount"] for r in orphans)))
```
"""),
        _turn(key, 'show(orphans, "Part 2: payments that match no order", money=["amount"])\n'
                   'print(len(orphans), "payments,", kit.rupees(sum(r["amount"] for r in orphans)))'),
        md("""
## Part 3. Which instalments were posted more than once, in either quarter?

Every order and instalment the feed posted more than once goes on the retry list, with the order's
quarter beside it. At work the platform lead fixes the whole feed, which spans both quarters, so this list covers
everything the feed holds.
"""),
        code(block(3) + f"""
options_3 = {{
    "a": "WHERE o.quarter = 'Q2'",
    "b": "WHERE o.quarter = 'Q1'",
    "c": "WHERE p.paid_date >= '2026-07-01'",
    "d": "",
}}
choice_3 = {fill[3]}

retries = run(f\"\"\"
SELECT p.order_id, o.quarter, p.instalment_no, min(p.method) AS method, min(p.paid_date) AS paid_date,
       count(*) AS times_posted, sum(p.amount) - max(p.amount) AS posted_twice
FROM payments p
JOIN orders o ON o.order_id = p.order_id
{{options_3[choice_3]}}
GROUP BY p.order_id, o.quarter, p.instalment_no
HAVING count(*) > 1
ORDER BY o.quarter, p.order_id\"\"\")
kit.matrix(["Q1 orders", "Q2 orders"], ["on Anand's Q2 page", "on this audit"],
           [["no", "yes"], ["yes, as posted twice", "yes"]], title="Part 3: the feed's fault spans both quarters")"""),
        code("""posted_matched = one("SELECT sum(p.amount) FROM payments p JOIN orders o ON o.order_id = p.order_id")
collected_matched = one(\"\"\"SELECT sum(amount) FROM (SELECT p.order_id, p.instalment_no, max(p.amount) AS amount
    FROM payments p JOIN orders o ON o.order_id = p.order_id GROUP BY p.order_id, p.instalment_no) i\"\"\")
kit.check("the list's surplus equals posted less collected across the whole matched feed",
          sum(r["posted_twice"] for r in retries) == posted_matched - collected_matched, "equal, figures unprinted")
kit.check("every row on the list was posted more than once", all(r["times_posted"] > 1 for r in retries))"""),
    ]
    if solution:
        cells.append(md(why[3]))
    cells += [
        md("""
**Your turn.** Show the list, and its count and surplus by quarter:

```python
show(retries, "Part 3: instalments posted more than once", money=["posted_twice"])
for q in ("Q1", "Q2"):
    rows = [r for r in retries if r["quarter"] == q]
    print(q, len(rows), kit.rupees(sum(r["posted_twice"] for r in rows)))
```
"""),
        _turn(key, 'show(retries, "Part 3: instalments posted more than once", money=["posted_twice"])\n'
                   'for q in ("Q1", "Q2"):\n'
                   '    rows = [r for r in retries if r["quarter"] == q]\n'
                   '    print(q, len(rows), kit.rupees(sum(r["posted_twice"] for r in rows)))'),
        md("""
## Part 4. Is there a pattern the gateway team can act on?

The gateway team fixes one integration at a time, so the list has to say which one. At work, a fix
request that names the integration, the instalment and the date range gets scheduled; one that says
"the feed double-posts" does not.
"""),
        code(block(4) + f"""
from datetime import date
retry_dates = [r["paid_date"] for r in retries]
options_4 = {{
    "a": (min(retry_dates), max(retry_dates)),
    "b": (date(2026, 4, 1), date(2026, 9, 30)),
    "c": (one("SELECT min(paid_date) FROM payments"), one("SELECT max(paid_date) FROM payments")),
    "d": (min(retry_dates), min(retry_dates)),
}}
choice_4 = {fill[4]}
window = options_4[choice_4]

pattern = run(\"\"\"
SELECT method, count(*) AS instalments, sum(extra) AS posted_twice
FROM (SELECT p.order_id, p.instalment_no, min(p.method) AS method, sum(p.amount) - max(p.amount) AS extra
      FROM payments p JOIN orders o ON o.order_id = p.order_id
      GROUP BY p.order_id, p.instalment_no HAVING count(*) > 1) r
GROUP BY method
ORDER BY method\"\"\")
kit.vflow(["the retry list", "its dates and its methods", "the integration to fix", "the request"],
          kinds=["plain", "plain", "good", "known"], title="Part 4: from a list to a request")"""),
        code("""kit.check("every retry falls inside the window, and the window starts and ends on a retry",
          all(window[0] <= d <= window[1] for d in retry_dates) and window[0] in retry_dates and window[1] in retry_dates,
          "window unprinted")
kit.check("the method breakdown adds back to the whole retry list", sum(r["instalments"] for r in pattern) == len(retries)
          and sum(r["posted_twice"] for r in pattern) == sum(r["posted_twice"] for r in retries), "equal, figures unprinted")"""),
    ]
    if solution:
        cells.append(md(why[4]))
    cells += [
        md("""
**Your turn.** Show the window and the retries by payment method, then write your request to the
platform lead under it:

```python
print("from", window[0], "to", window[1])
show(pattern, "Part 4: the retries by payment method", money=["posted_twice"])
```

> "The feed holds ___ payments that match no order, Rs ___, all on ___ by ___: please hold them in
> suspense and trace them. It also holds ___ instalments posted twice, Rs ___ across both quarters,
> every one of them ___ instalment ___: please fix that integration so a retry cannot post twice,
> and keep the raw rows until Finance has checked with the bank whether any customer was charged
> twice."
"""),
        _turn(key, 'print("from", window[0], "to", window[1])\n'
                   'show(pattern, "Part 4: the retries by payment method", money=["posted_twice"])'),
        md("""
## What do you post?

Post one line: your four TODO letters in order, no spaces, then your request to the platform lead.

```
Post exactly this shape: xxxx
```
"""),
        code("kit.check_summary()"),
    ]
    return cells


def main():
    nb, sol, tr = DAY / "notebooks", DAY / "exercises" / "solutions", DAY / "trainer"
    build(nb / "C2_W02_D02_ex1_escalated_case_STUDENT.ipynb", escalated(), execute=False)
    build(sol / "C2_W02_D02_ex1_escalated_case_solution_STUDENT.ipynb", escalated(solution=True))
    build(nb / "C2_W02_D02_ex2_second_case_STUDENT.ipynb", second_case(), execute=False)
    build(sol / "C2_W02_D02_ex2_second_case_solution_STUDENT.ipynb", second_case(solution=True))
    key_cells = [md("""
# Trainer key: both cases, with every list and figure printed

**TRAINER ONLY.** This file holds the two case notebooks with every letter filled and every your-turn
cell run, so the trainer sees what the room is meant to find. Never share it with a learner.
""")] + escalated(solution=True, key=True) + second_case(solution=True, key=True)[1:]
    build(tr / "C2_W02_D02_case_key_TRAINER.ipynb", key_cells, timeout=300)
    print("cases written")


if __name__ == "__main__":
    main()
