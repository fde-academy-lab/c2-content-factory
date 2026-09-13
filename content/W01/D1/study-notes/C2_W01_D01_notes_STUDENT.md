# Day 1: where does our growth come from?

Kalpa Retail, Week 1 Monday. Read this after the session. It carries what was covered, the worked
numbers, the two failures and their fixes, and the questions this day now makes answerable.

---

## The situation, in one paragraph

Kalpa Retail's revenue grew 4 percent last year against a plan of 15. The board wants a growth plan
within a month and marketing has asked for Rs 12 crore to acquire new customers. Meera Raghavan,
the CEO, will not sign it until somebody can tell her what "sales" is made of and whether
acquisition is even the branch that is short. Anand Iyer, who owns the books, added one rule before
any code ran: **no averages, because one business customer can move an average.**

---

## The mental model: revenue is a product, not a total

```
REVENUE = CUSTOMERS × ORDERS PER CUSTOMER × ITEMS PER ORDER × PRICE PER ITEM − DISCOUNTS
```

Five branches. Growth comes from moving one of them, and each costs something different.

| Branch | The metric | Denominator | What it costs to move |
|---|---|---|---|
| Customers | Distinct buyers | The window, matched on both sides | Marketing spend, and it is the slowest |
| Orders per customer | Purchase frequency | Distinct customers, same window | Retention work, a reorder feature, a tier |
| Items per order | Basket size | Orders | Merchandising, bundles |
| Price per item | Realised price | Items | Pricing, and it risks volume |
| Discounts | Discount rate | Gross revenue before discount | Margin, directly |

Marketing's Rs 12 crore is a bet on branch one. Nothing about the tree says that is wrong. It says
somebody should check whether branch one is the branch that moved.

**The sentence to remember:** a rate with no denominator is a rumour.

---

## What the thirty orders said

| Leaf | Value |
|---|---|
| Orders | 30 |
| Revenue | Rs 5,44,810 |
| Customers | 23 |
| Orders per customer | 1.30 |
| Items per order | Not computable, the file has no items |
| Price per item | Not computable, the file has no items |
| Discounts | Not computable, there is no discount field |

Naming what you cannot compute is half the answer. Asking for it is the other half, and it is the
first thing you send back to the business.

### Split by what happened to the order

| Status | Orders | Revenue |
|---|---|---|
| Delivered | 21 | Rs 5,20,790 |
| Returned | 5 | Rs 14,970 |
| Cancelled | 4 | Rs 9,050 |

Four honest readings live inside the word "sales": gross bookings, delivered revenue, net of
returns, and cash collected. Finance recognises delivered. Say which one you used, every time.

---

## The reveal: the average that describes nobody

| | |
|---|---|
| Mean order value | Rs 18,160 |
| Median order value | Rs 2,205 |
| The mean is | 8 times the median |
| Largest single order | Rs 4,80,000 |
| Its share of all revenue | 88 percent |
| Mean with that order removed | Rs 2,235 |

One corporate order carries 88 percent of the revenue. Take it out and the mean lands next door to
the median. That is exactly what Anand meant before any code ran, and it is why a typical order is
described by the median and never by the mean.

**When to use which**

| Use | When | Because |
|---|---|---|
| Median | Describing a typical order | Extremes cannot drag it |
| Mean | Dividing a total that must reconcile | Revenue per customer has to add up to revenue |
| Both | The first pass on any file | The gap between them is itself a finding |

---

## The two failures, and how to read them

### The accumulator that stopped

```
TypeError: unsupported operand type(s) for +=: 'int' and 'str'
```

Four facts in one line: the kind of problem, the operation that failed, what sat on each side, and
where Python gave up. One amount in the file arrived as the text `"4500"` rather than the number
`4500`, and Python will not add a word to a number.

**The fix for today:** `int(order["amount"])`. **The cost of that fix:** it turns a loud problem
into a silent assumption, because nobody has written down that the file holds text where numbers
belong. Wednesday is the day that assumption gets a log entry and a reason.

### The cell that ran out of order

```
NameError: name 'orders' is not defined
```

The notebook on your screen and the state in the kernel can disagree, and the screen is the one
that lies. The recovery is always the same: **Kernel, then Restart Kernel and Run All Cells.** If
it passes, your screen was stale. If it fails, the notebook is wrong.

---

## The three lines everything is made of

```python
total = 0
for order in ORDERS:
    total = total + int(order["amount"])
```

Start at zero, walk the list, add. Count adds one. Sum adds the value. Distinct uses a `set`,
because a set refuses duplicates, which is exactly what "distinct customers" means.

---

## Glossary

| Term | What it means here |
|---|---|
| Revenue tree | Revenue written as a product of branches, each of which a team owns |
| Branch | One factor in that product, expressed as a metric |
| Denominator | What a rate is divided by, and the thing that has to match across periods |
| Accumulator | A variable that starts at zero and is added to inside a loop |
| Record | One row as a dictionary of named fields |
| Median | The middle value once the values are sorted |
| Mean | The total divided by the count |
| Kernel | The process holding everything your cells have created so far |
| Gross bookings | Everything ordered, including what was later cancelled |
| Delivered revenue | What was actually delivered, which is what Finance recognises |

---

## The questions this day now makes answerable

- How would you increase sales for an online retailer?
- Mean or median for order value, and why?
- A business says "grow revenue 15 percent". How do you turn that into questions data can answer?
- When do you reach for a list and when for a dictionary?
- Marketing wants budget for acquisition. What would you check before agreeing it is the right
  branch, and how would you say no?

---

## What tomorrow does with this

Today told you what the branches are. Tomorrow's file has two quarters, and the question becomes
which branch **moved**. The tree stops being a picture and becomes an instrument.

---

## Reading, if you want it

- Hacking the Case Interview, the profitability framework and the revenue tree
  (verified 13 Sep 2026): https://www.hackingthecaseinterview.com/pages/profitability-case-interview
- MConsultingPrep, the profitability framework (verified 13 Sep 2026):
  https://mconsultingprep.com/profitability-case-framework
- Corey Schafer, Dictionaries (verified 03 Sep 2026): https://www.youtube.com/watch?v=daefaLgNkw0
- Khan Academy, mean, median and mode (verified 03 Sep 2026):
  https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/mean-median-basics/v/mean-median-and-mode
