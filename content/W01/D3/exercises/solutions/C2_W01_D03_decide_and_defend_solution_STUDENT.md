# Solution: six calls, each one defended

Answers: 1c 2b 3d 4a 5b 6c

---

| Item | Key | Why, and why the rest fail |
|---|---|---|
| **1** | `c` | Every alternative invents a number. Zero understates revenue and keeps the order count, the segment median is a guess wearing statistics, and keeping it as text moves the problem to whoever sums the column next. Reject it, record it, and if the amount matters ask the source system. |
| **2** | `b` | Status decides which of the four readings of "sales" the row belongs to, so an order without one cannot be counted in any of them. `a` is the dangerous option: defaulting to the most common value makes the split look cleaner and quietly moves revenue between buckets. |
| **3** | `d` | One order id is one order. Keeping both double counts it, rejecting both loses a real order, and averaging the dates produces a date on which nothing happened. Take one, say which, and say why in the log. |
| **4** | `a` | The second header line was never an order. The first one is the header and belongs where it is. `d` is the trap that matters: defaulting its amount to zero makes it a silent extra row in every count. |
| **5** | `b` | It is a real order from a real corporate customer. Rejecting it, capping it or hiding it in a second file are all ways of making the data agree with you. Report it, keep it, and describe the file with a median rather than a mean. |
| **6** | `c` | A bridge with a gap has a step missing, and the step is the finding. `b` is the one that ends careers: adjusting a figure so two systems agree is the difference between reconciling and fabricating. |

---

## The decisions log

A full-credit log is specific, counted, and reads as something an auditor could question.

| Field | Issue | Rows | Decision | Reason |
|---|---|---|---|---|
| `order_id` | Repeated | 14 | Drop the later occurrence | The Q1 migration re-ran a batch, and every field on the pairs is identical |
| `order_id` | Repeated, dates differ | 1 | Keep the later date, drop the earlier | One order recorded twice during the migration window; the later record matches the payment date |
| `status` | Empty | 1 | Reject | An order with no status cannot be placed in any reading of sales |
| `amount` | Text `twelve` | 1 | Reject | Any substitute value would be invented revenue |
| `amount` | Rs 4,80,000 outlier | 1 | Keep, flagged | A real corporate order. Described with the median rather than the mean. |

**What loses credit:** a reason that restates the issue ("it was a duplicate so I removed it"), a
missing row count, or a log that does not mention the order that was kept. The kept row is the one
an auditor asks about, because it is the one that changes the total most.
