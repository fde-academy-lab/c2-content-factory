# Which drawings go up on the board, in order, while the room decides whom Marketing protects and whether Q2 is on track?

These are the board drawings for Week 2, Wednesday, in the order they go up. Kalpa Retail's
marketing lead wants the top fifty customers by Q2 revenue in each segment and a flag on anyone
whose monthly spend has fallen two months running, and Meera Raghavan, the CEO, wants revenue to
accumulate week by week against the plan line. The head of Retail-Plus, who owns the paid
membership tier, wants members who spent the same ranked the same, with the count that made the
list. Q2 is July to September 2026, and revenue is booked revenue, every order at its amount
whatever its status: Rs 9,84,00,000 on 462 orders from 227 of Kalpa's 340 members. The segments are
Business, Retail-Core, Retail-Plus and Student. The decks and the notebooks use these same drawings.

---

## What does a window keep that GROUP BY throws away?

Marketing's three asks go up first, in words across the top of the board: a top fifty in each
segment, a flag for spend that fell two months running, and revenue to date against the plan line.
The room tries one GROUP BY for all three and finds that it returns one row per group, so the fork
goes up under the asks, GROUP BY on one branch and a window on the other, and stays up all day.

```mermaid
flowchart LR
    R["<b>rows</b><br/>one per member"] --> G["<b>GROUP BY</b><br/>one row per group"]
    R --> W["<b>a window</b><br/>every row kept,<br/>one column added"]
    G --> A["<b>how much per group</b><br/>4 rows for 4 segments"]
    W --> B["<b>each row beside its neighbours</b><br/>its place, its last month,<br/>the total so far"]
    classDef bet fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    class W,B bet
    class G,A known
```

Beside it goes the shape every window takes, `function() OVER (PARTITION BY ... ORDER BY ...)`: the
partition says whose rows belong together, and the order says which row comes before which.

---

## What does each of Marketing's three asks need the window to add to every row?

Each ask is matched to the column its window adds, which is the day's plan in one drawing.

```mermaid
flowchart LR
    L["<b>the protect list</b>"] --> P["<b>a place</b><br/>inside its segment"]
    F["<b>the falling flag</b>"] --> M["<b>the month before</b><br/>for the same member"]
    T["<b>the plan line</b>"] --> S["<b>the total so far</b><br/>week by week"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bet fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class L,F,T known
    class P,M,S bet
```

---

## How do a named step and a window turn 462 Q2 orders into a ranked list of members?

Chapter 1 draws the build the room chose from four ways to rank. The named step adds up each member's
Q2, 227 rows that carry all 462 orders, and the window numbers them with the customer id settling
equal spend. Under it the room writes the result: 35 Business members, every Business buyer, then 11
Retail-Plus and 4 Retail-Core, and no Student.

```mermaid
flowchart LR
    O["<b>462 Q2 orders</b>"] --> S["<b>q2_spend</b><br/>GROUP BY member<br/>227 rows"]
    S --> N["<b>ranked</b><br/>row_number() OVER<br/>(ORDER BY q2_revenue DESC)"]
    N --> K["<b>WHERE position <= 50</b><br/>in the outer query"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bet fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class S,N known
    class K bet
```

---

## Why did a list of fifty rows name only twenty-eight members, and what does the fix reach?

The quickest list sorted the Q2 orders and kept fifty: 50 rows naming 28 members, all Business. The
check goes up beside it as one line, `count(DISTINCT customer_id)` beside `count(*)`, and then the
fix, which adds up each member's orders before ranking.

```mermaid
flowchart LR
    O["<b>50 orders</b><br/>28 members,<br/>Business only"] --> A["<b>add up each<br/>member's orders</b><br/>227 rows"]
    A --> M["<b>50 members</b><br/>3 segments,<br/>22 more reached"]
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    classDef bet fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class O bad
    class M bet
```

---

## What does PARTITION BY restart, and how many members does each segment's list hold?

Chapter 2 starts from the plausible wrong answer, chapter 1's numbering split by segment: Business
35, Retail-Core 4, Retail-Plus 11 and Student 0. The check goes up as a rule, each list holds the
smaller of 50 and its segment's buyers, and then the drawing of the fix.

```mermaid
flowchart LR
    W["<b>one window</b><br/>PARTITION BY segment,<br/>ORDER BY Q2 revenue"] --> B["<b>Business</b><br/>1, 2, ... 35"]
    W --> C["<b>Retail-Core</b><br/>1, 2, ... 96"]
    W --> P["<b>Retail-Plus</b><br/>1, 2, ... 76"]
    W --> S["<b>Student</b><br/>1, 2, ... 20"]
    classDef bet fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    class W bet
    class B,C,P,S known
```

Beside it go the counts, 155 members in all: Business 35 and Student 20, every buyer in both, and
Retail-Core and Retail-Plus 50 each.

---

## Why does the place filter wait for the query outside?

This one goes up when someone writes the place into WHERE and Postgres prints "window functions are
not allowed in WHERE". It takes two minutes, and the drawing points back at Monday's run order.

```mermaid
flowchart LR
    F["<b>FROM, WHERE,<br/>GROUP BY</b><br/>rows chosen"] --> S["<b>SELECT</b><br/>the window<br/>computes the place"]
    S --> O["<b>the outer query</b><br/>WHERE position <= 50"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bet fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class F,S known
    class O bet
```

---

## What do ROW_NUMBER, RANK and DENSE_RANK give on one tie?

Chapter 3 works on six invented members, so the mechanism shows on numbers nobody has to trust.
Pairs fill in the three columns on paper before the table is completed on the board.

| Member (invented) | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| Spend, Rs | 7,500 | 7,500 | 6,000 | 5,200 | 5,200 | 4,100 |
| ROW_NUMBER | 1 | 2 | 3 | 4 | 5 | 6 |
| RANK | 1 | 1 | 3 | 4 | 4 | 6 |
| DENSE_RANK | 1 | 1 | 2 | 3 | 3 | 4 |

```mermaid
flowchart LR
    T["<b>two members tie</b><br/>A and B at Rs 7,500<br/>(invented)"] --> RN["<b>ROW_NUMBER</b><br/>1, 2: the tiebreaker<br/>decides"]
    T --> RK["<b>RANK</b><br/>1, 1, then 3"]
    T --> DR["<b>DENSE_RANK</b><br/>1, 1, then 2"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bet fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    class RK bet
    class RN bad
    class DR known
```

---

## How many rows does each rule ship when two members tie at the line?

A second invented list goes up as a chain, a top four with D and E tied at fourth, which is the line,
the last place a top four keeps. Under it the room writes what each rule ships: ROW_NUMBER 4, RANK 5,
DENSE_RANK 5 and whole ties only 3. With nobody tied at the line, ROW_NUMBER, RANK and whole ties
only would each ship exactly four, and DENSE_RANK could still ship more if a tie sat higher up.

```mermaid
flowchart LR
    A["<b>A 9,100</b>"] --> B["<b>B 8,800</b>"] --> C["<b>C 8,200</b>"] --> D["<b>D 7,400</b>"] --> E["<b>E 7,400</b>"] --> F["<b>F 6,900</b>"]
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    class D,E bad
```

---

## Why does DENSE_RANK's fiftieth number land on Retail-Core's 52nd member?

On Kalpa's Retail-Core, 96 Q2 buyers, a hurried analyst picks DENSE_RANK and ships 52 members as the
top fifty, where the other three rules ship 50. Two ties inside the list cost DENSE_RANK one number
each, and RANK, the rule the head of Retail-Plus asked for, ships the same fifty as ROW_NUMBER here,
since nobody ties at Retail-Core's line. The head's own tier is counted by every learner in their
own notebook.

```mermaid
flowchart LR
    T["<b>two ties inside</b><br/>places 31-32, Rs 4,540<br/>places 37-38, Rs 4,120"] --> D["<b>DENSE_RANK</b><br/>two numbers behind<br/>the members"]
    D --> L["<b>its 50</b><br/>place 52, C-0094<br/>Rs 2,910"]
    L -.->|"the fix"| R["<b>RANK</b><br/>50 at place 50, C-0005<br/>Rs 2,980, no tie there"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bet fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    class T known
    class D,L bad
    class R bet
```

---

## What does LAG put beside each month?

Chapter 4 draws the flag on three calendar months. Beside it goes C-0040 of Retail-Core, who bought
in all six months: April Rs 7,980, May Rs 3,170, June Rs 1,320, July Rs 4,260, August Rs 4,770 and
September Rs 4,520. LAG shows NULL on April, a flag read at June would fire, and the flag read at
September does not, because August rose above July.

```mermaid
flowchart LR
    J["<b>July</b><br/>spend"] --> A["<b>August</b><br/>lag 1: July"]
    A --> S["<b>September</b><br/>lag 1: August<br/>lag 2: July"]
    S --> F{"<b>September below August,<br/>August below July?</b>"}
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bet fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class J,A,S known
    class F bet
```

---

## Why did LAG flag C-0132 for a fall from a month they never had?

The quick flag sorted the whole table by member and month with no PARTITION BY and flagged 20
members. C-0132 bought only in July and September, so LAG's second step back ran into C-0131's July.
The check goes up beside it, `lag(customer_id)` carried beside `lag(spend)`: four flags read another
member's month. With PARTITION BY customer_id, 16 members are flagged, out of the 118 who ordered in
September.

```mermaid
flowchart LR
    A["<b>C-0131, July</b><br/>Rs 4,700"] --> B["<b>C-0132, July</b><br/>Rs 2,620"]
    B --> C["<b>C-0132, September</b><br/>Rs 1,920"]
    C -.->|"lag 2 reads"| A
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    class A bad
```

---

## What does a running total add to each week's row?

Chapter 5 draws the running total before any query runs: each week keeps its row and carries the
sum of every week up to and including it, so the last row is the quarter.

```mermaid
flowchart LR
    W1["<b>week 1</b><br/>to date = week 1"] --> W2["<b>week 2</b><br/>to date = weeks 1 + 2"]
    W2 --> W3["<b>week 3</b><br/>to date = weeks 1 to 3"]
    W3 --> WK["<b>week 13</b><br/>to date = the quarter"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bet fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class W1,W2,W3 known
    class WK bet
```

---

## Why did a build that starts from the plan's weeks close Rs 15,39,810 short of plan?

The build that started from the plan's 13 weeks closed at Rs 9,68,60,180 against a plan of
Rs 9,83,99,990. The check sets the close beside Monday's Q2 total, Rs 9,84,00,000, and finds it
Rs 15,39,820 short: the 25 orders of 1 to 5 July fall in a week the plan line does not have.

```mermaid
flowchart LR
    Q["<b>Q2 starts</b><br/>Wed 1 July"] --> J["<b>week of 29 June</b><br/>25 orders, Rs 15,39,820<br/>not in the plan line"]
    P["<b>plan starts</b><br/>Mon 6 July"] --> K["<b>13 plan weeks</b><br/>the only weeks the<br/>LEFT JOIN keeps"]
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    class J bad
    class K known
```

The fix goes under it: `greatest()` moves 1 to 5 July onto the first plan Monday, and Q2 closes on
Rs 9,84,00,000 against Rs 9,83,99,990, Rs 10 ahead.

---

## Where did Q2 stand at mid-quarter, and where did the lead come from?

The quarter's lead goes up as a line of five readings, booked to date less plan to date at the end
of each marked week. Beside it the room writes the run rate: six of the seven full weeks from 10
August booked below the weekly plan of Rs 75,69,230.

```mermaid
flowchart LR
    A["<b>6 July week</b><br/>Rs 24,69,050<br/>behind"] --> B["<b>13 July week</b><br/>3.5 times<br/>its plan"]
    B --> C["<b>3 August</b><br/>lead peaks,<br/>Rs 2,16,69,660"]
    C --> D["<b>17 August</b><br/>mid-quarter,<br/>Rs 1,57,51,980 ahead"]
    D --> E["<b>28 September</b><br/>Rs 10 ahead,<br/>on plan"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bet fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    class A bad
    class B,C,E known
    class D bet
```

---

## What does "the month before" mean for a member who skipped a month?

Chapter 6 opens on the head of Retail-Plus's message: a flagged member, C-0216, says they were
travelling in August and have not stopped buying. Two readings of "the month before" go up side by
side.

```mermaid
flowchart LR
    S["<b>September</b><br/>an order"] -->|"the calendar's<br/>month before"| A["<b>August</b><br/>no order:<br/>no reading"]
    S -->|"LAG's<br/>row before"| J["<b>July</b><br/>an order:<br/>compared"]
    classDef unknown fill:#FFFFFF,stroke:#B8B2D6,color:#6B6690,stroke-dasharray:4 3
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    class A unknown
    class J bad
    class S known
```

---

## What did LAG compare for C-0216, the member on holiday?

C-0216 of Retail-Plus, place 23 on that segment's list, bought in May, July and September, with no
order in June or August. With no August row, LAG compared September with July and July with May.

```mermaid
flowchart LR
    M["<b>May</b><br/>Rs 6,440"] --> J["<b>July</b><br/>Rs 4,300"] --> S["<b>September</b><br/>Rs 2,540"]
    S -.->|"lag 1"| J
    S -.->|"lag 2"| M
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    class J,M bad
```

---

## How many of the sixteen flags survive the calendar check?

All 16 flagged members are on a protect list, so the call sheet would read 16 names. The check
carries `lag(month)` beside `lag(spend)`, and 7 of the 16 flags step over an empty month. Under the
drawing goes a fall that holds up: C-0010 of Retail-Core, first on that segment's list, spent
Rs 7,840 in July, Rs 4,080 in August and Rs 1,990 in September.

```mermaid
flowchart LR
    F["<b>16 flags</b><br/>LAG over own months"] -->|"rows before September<br/>not August and July"| G["<b>7 step over<br/>an empty month</b>"]
    F --> K["<b>9 read three<br/>calendar months</b>"]
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    classDef bet fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class G bad
    class K bet
```

---

## What does Marketing hear when the day ends?

The day's answer goes up as one chain, in the order Marketing reads it.

```mermaid
flowchart LR
    L["<b>the lists</b><br/>top fifty per segment<br/>under RANK, counts said"] --> C["<b>the calls</b><br/>nine members,<br/>three months lower"]
    C --> Q["<b>Q2</b><br/>closed Rs 10 ahead,<br/>on plan"]
    Q --> R["<b>the run rate</b><br/>6 of 7 full weeks<br/>from 10 August below plan"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bet fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class L,C,Q known
    class R bet
```

---

## What is on the board when the day ends?

The fork is still up at the top, with the three asks above it and each ask matched to its column.
Under it run the chapters in order: the named step and the window with 35, 11 and 4 written
beside them; the fifty orders that named 28 members, with the count check; PARTITION BY restarting
in four segments, 155 members; the place filter waiting for the outer query; the invented six with
their three columns and the invented top four with 4, 5, 5 and 3; Retail-Core's DENSE_RANK running
two behind to 52; LAG reading the month before, and C-0132 reading C-0131's July; the running total,
the missing week of 29 June, and the lead's five readings; and C-0216's empty August beside the 16
flags that became 9. The chain to Marketing runs across the bottom, and beside it the six lines the
cheat sheet prints:

1. Say what one row of the list is before you rank it: fifty orders named only 28 members.
2. "In each segment" is a PARTITION BY: fifty, or every buyer, in each segment.
3. RANK keeps a tie at the line and says the count; DENSE_RANK can run past the line with no tie at it.
4. Tell the window whose rows belong together, or LAG reads another member's month.
5. A running total is done when its last value equals the quarter's total.
6. A month with no order is no reading: check that LAG read the calendar months before.

Tomorrow's question goes in the corner, left open: the growth team wants one table with one row per
customer, refreshed every Monday, built in pandas.
