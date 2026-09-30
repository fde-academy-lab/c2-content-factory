# Chapter 5 scenario set: Marketing's hypothesis

Ten minutes, alone, then compare with the person beside you before Kavya's review. Every item has
one right answer. Decide first, then record the letter. Items marked design ask for the best-fit
approach, a sizing, the fact that would switch it, or the second route.

Post one line, 6 letters in item order, no spaces:

```
Post exactly this shape: xxxxxx
```

The ask behind every item:

> "A flat count can hide churn replaced by new customers. And Retail-Plus is Rs 65,250 out of a Rs 23 lakh fall." (the marketing lead)

The numbers every item refers to, booked orders, the export as it stands:

| Measure | Value |
|---|---|
| Customer ids in Q1, in Q2 | 69, 69 |
| Customers who placed fewer orders in Q2 | 23 |
| Consumer revenue, Q1 to Q2 | Rs 2,28,820 to Rs 1,58,540 |
| Business revenue fall | Rs 22,29,720 on 3 fewer orders |

```mermaid
flowchart LR
    A["<b>Marketing's claim</b><br/>a flat count hides churn"] --> B["<b>Marketing's ask</b><br/>Rs 12 crore for acquisition"]
```

---

### Q1. (design) Which test answers "a flat count hides churn replaced by new customers" most directly?

a) Count each quarter's customers by segment, since churn hides inside segments
b) Ask Marketing's CRM for new sign-ups by month
c) Count the ids in both quarters, only in Q1 and only in Q2
d) Compare the counts again under a different definition of customer

### Q2. (design) What would make you distrust the id overlap?

a) One person holding two ids, say one from the store and one from the app
b) A member who moved from Retail-Core to Retail-Plus between the quarters
c) A customer whose Q1 order fell on 30 June and Q2 order on 1 July
d) Customers who placed several orders in one quarter and one in the other

### Q3. The overlap comes out 69 in both quarters, 0 only in Q1, 0 only in Q2. What goes back to Marketing?

a) Churn is hidden in the segments, so split them first and run the overlap per segment
b) Nobody was lost and nobody was new, so acquisition has nothing to replace
c) The flat count proves customers are loyal, so no action is needed
d) Marketing is right in spirit, since 23 customers placed fewer orders

### Q4. Last quarter's script prints `summary: {'Retail-Core': -5.3, 'Business': -15.0}` because `pct_change` returns a value only when the change is 30 percent or less. Which fix to the logic keeps every segment in Meera's summary?

a) Raise the threshold to 50 percent, so that fewer of the changes print
b) Print the change as well as returning it, so both appear on the screen
c) Filter with `if ch < 0`, so that a None is compared with zero as well
d) Return the change every time, and put the flag in a column of its own

### Q5. Marketing says Retail-Plus is Rs 65,250 out of a Rs 23 lakh fall, so it does not matter. Using the table, which reply holds?

a) They are right in rupees, so the memo leads with Business and footnotes the tier
b) Retail-Plus is 93 percent of the consumer business's Rs 70,280 fall
c) The tier is 49 percent of the fall, since its orders per member fell 49 percent
d) The tier is 3 percent of the fall, so the reorder complaint can wait a quarter

### Q6. (design) The second route took each customer's first and last order date in the export and counted who first ordered in Q2 or last ordered in Q1: 0 and 0. What does it add, and where does it stop?

a) Nothing new, since it counts the same 69 ids the overlap already counted
b) It proves that no customer has left Kalpa since the business opened
c) It shows which customers slowed, which the overlap cannot see
d) The same 0 and 0 from dates alone; new still means new since 1 April
