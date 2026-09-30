# Chapter 1 scenario set: is the drop real

Ten minutes, alone, then compare with the person beside you before Kavya's review. Every item has
one right answer. Decide first, then record the letter. Items marked design ask for the best-fit
approach, a sizing, the fact that would switch it, or the second route.

Post one line, 6 letters in item order, no spaces:

```
Post exactly this shape: xxxxxx
```

The ask behind every item:

> "Q2 was Rs 1.9 crore, Q1 was 2.1. Marketing says more customers. Prove it or disprove it." (Meera Raghavan)

The numbers every item refers to, booked orders, the export as it stands:

| Window | Dates | Orders | Revenue |
|---|---|---|---|
| Q1, closed | 1 Apr to 30 Jun | 114 | Rs 2,10,00,000 |
| Q2, closed | 1 Jul to 30 Sep | 86 | Rs 1,87,00,000 |
| Q2 dashboard tile, cut on 15 September | 1 Jul to 15 Sep | 70 | Rs 1,55,59,950 |

```mermaid
flowchart LR
    A["<b>1 Apr</b><br/>Q1 opens"] --> B["<b>1 Jul</b><br/>Q2 opens"]
    B --> C["<b>15 Sep</b><br/>the tile is cut"]
    C --> D["<b>30 Sep</b><br/>Q2 closes"]
```

---

### Q1. Meera asks how far revenue fell between the two closed quarters. Which figure goes in the reply?

a) 12.3 percent, the Rs 23,00,000 gap measured against Q2's total
b) 9.5 percent, from the rounded Rs 1.9 crore against Rs 2.1 crore
c) 11.0 percent, the Rs 23,00,000 gap measured against Q1's total
d) 25.9 percent, the figure on the dashboard tile Marketing quotes

### Q2. Marketing's slide reads "Q2 Rs 1,55,59,950 against Q1 Rs 2,10,00,000: revenue fell 25.9 percent." What makes the slide unfit to act on?

a) The percentage is computed on Q2's total, which overstates the fall
b) It sets about 11 weeks of Q2 against all 13 weeks of the closed Q1
c) It counts booked orders, where Finance would count delivered ones
d) It rounds both totals to the nearest lakh before dividing them

### Q3. (design) On 15 September, with Q2 still open, a colleague turns both sides of Marketing's slide into revenue per week, each side divided by the weeks its dates cover. What does the rate give, and what does it still miss?

a) Minus 12.4 percent, and it still compares Q2's early weeks with the whole of Q1
b) Minus 25.9 percent, since dividing both sides by weeks leaves their ratio alone
c) Minus 11.0 percent, since a rate per week removes every difference in the windows
d) Minus 17.0 percent, the answer that matched weeks of each quarter would give

### Q4. (design) Both quarters have closed. Meera now asks: "Is Q2 always weaker than Q1, because of the monsoon?" Which option answers her, and what does it need?

a) Closed quarters again, since both are complete and compare like with like
b) A rate per day, since it removes the one-day gap between 91 and 92 days
c) The same 11 weeks of each quarter, since it also matches position
d) The same quarter last year, which needs last year's export to run

### Q5. Four moves answer "is the drop real": p) compute the change, q) find the first and last order date of each window, r) state the definition and the window in the sentence to Meera, s) choose closed quarters or matched weeks. Which order is right?

a) s, q, p, r
b) q, s, p, r
c) q, p, s, r
d) q, s, r, p

### Q6. (design) The second route added revenue by the month in `order_date` and reached the same fall as the closed quarters. What does agreement between the two routes prove?

a) That monthly totals are a better headline for Meera than the quarters
b) That no order in the file carries a wrong amount or a missing field
c) That the quarter field and the dates give each quarter the same total
d) That the fall is real and needs no comparison with last year
