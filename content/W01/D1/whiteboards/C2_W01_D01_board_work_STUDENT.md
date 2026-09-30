# The board, drawing by drawing

Week 1, Monday, Kalpa Retail. These are the drawings in the order they go up across the day: six
for the retail story, then one or two per chapter and one for the second case. The deck, the
notebooks, the domain card and the cheat sheet carry the same metric tree, so the tree copied from
the board here is the one met everywhere else this week.

---

## Drawings 1 to 6: the retail story

The story's six drawings go up in its six parts, before Meera's ask, and stay up all day. Each is
drawn exactly as the domain dossier draws it,
`study-notes/C2_W01_D01_domain_retail_STUDENT.md`, so the board and the reading match.

| Drawing | Story part | The dossier's section | What it shows |
|---|---|---|---|
| 1 | The Saturday | 1, the value chain | Suppliers to the distribution centre, the store and the app, the last mile, and the returns desk |
| 2 | Kalpa's twins | 2, the group | Kalpa Group, its five units, and the GCC with a dotted line to each |
| 3 | Where Rs 100 goes | 3, the P&L | Rs 100 of GMV walked to Rs 2.50 of operating profit |
| 4 | Who asks | 4, the org chart | The CEO, the functions, and the GCC below with its "asks" line |
| 5 | The metric tree | 5, the metric tree | Revenue, its three branches, the shelf above and the leaks beside |
| 6 | Describe to act | 8, the ladder | Describe, predict, recommend and act, the last in rose |

Drawing 5 is the one the case writes on. Meera's question is read out beside it, marketing's
Rs 12 crore is written against the customers branch, and every chapter adds a number to it:

```mermaid
flowchart TB
    R["<b>revenue</b><br/>4% against a 15% plan"] --> C["<b>customers</b><br/>distinct ids"]
    R --> F["<b>orders per customer</b><br/>orders / customers"]
    R --> A["<b>average order value</b><br/>revenue / orders"]
    A --> I["<b>items, price,<br/>discounts</b><br/>not in today's file"]
    C -.- B["<b>Rs 12 crore</b><br/>marketing's bet"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef unknown fill:#FFFFFF,stroke:#B8B2D6,color:#6B6690,stroke-dasharray:4 3
    classDef bet fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class C,F,A known
    class I unknown
    class B bet
```

---

## Drawing 7: the four readings of "sales", as a funnel

It goes up at the start of chapter 1, when the room names what "sales" could mean, and the numbers are written in once the loop has counted them.

```mermaid
flowchart TB
    O["<b>order count</b><br/>30 orders"] --> B["<b>booked</b><br/>Rs 5,44,810 on 30"]
    B --> N["<b>not cancelled</b><br/>Rs 5,35,760 on 26"]
    N --> D["<b>delivered</b><br/>Rs 5,20,790 on 21"]
    B -.-> X["<b>cancelled</b><br/>4 orders, Rs 9,050<br/>all store"]
    N -.-> Y["<b>returned</b><br/>5 orders, Rs 14,970<br/>all web"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    class O,B,N,D known
    class X,Y bad
```

The rule written under it is chapter 1's crux: the definition goes beside the number, and delivered, returned and cancelled add back to booked.


---

## Drawing 8: one fraction, one definition

It goes up in chapter 2, when the mixed AOV of Rs 25,943 is on the screen.

```mermaid
flowchart LR
    F["<b>Finance</b><br/>booked Rs 5,44,810"] --> X["<b>Rs 25,943</b><br/>x 30 = Rs 7,78,300<br/>lands on nothing"]
    O["<b>dashboard</b><br/>21 delivered orders"] --> X
    B["<b>booked / booked</b><br/>Rs 18,160"] --> OK["<b>x orders lands<br/>on its revenue</b>"]
    D["<b>delivered / delivered</b><br/>Rs 24,800"] --> OK
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    class B,D,OK known
    class F,O,X bad
```

The check written under it: orders times AOV lands on that definition's revenue, or the fraction
mixes two reports.

---

## Drawing 9: rows against customers

It goes up in chapter 3, when the trap's 1.00 is on the screen and the room is asked who those 30 rows are.

```mermaid
flowchart LR
    R["<b>30 rows</b><br/>30 orders"] --> C["<b>23 customers</b><br/>distinct ids"]
    C --> O["<b>16 bought once</b>"]
    C --> T["<b>7 bought twice</b><br/>14 of the rows"]
    R -.-> W["<b>30 / 30 = 1.00</b><br/>rows as people"]
    C --> K["<b>30 / 23 = 1.30</b><br/>orders per customer"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    class C,O,T,K known
    class W bad
```

The check goes beside it in code: the length of the rows against the length of the set of customer ids.


---

## Drawing 10: sorted amounts, with the mean and the median drawn on invented values

It goes up in chapter 4, after the room has seen the mean and the median of the real file and before anyone sorts it. Every amount here is invented, so the mechanism shows on numbers nobody has to trust.

```mermaid
xychart-beta
    title "Six invented orders, sorted, after the sixth is added"
    x-axis ["order 1", "order 2", "order 3", "order 4", "order 5", "order 6"]
    y-axis "Rs" 0 --> 95000
    bar [1900, 2100, 2300, 2400, 2600, 90000]
    line [16883, 16883, 16883, 16883, 16883, 16883]
    line [2350, 2350, 2350, 2350, 2350, 2350]
```

Five invented orders of Rs 1,900, 2,100, 2,300, 2,400 and 2,600 go up first, with a mean of Rs 2,260 and a median of Rs 2,300. An invented Rs 90,000 order is then added as the sixth. The upper line is the new mean, Rs 16,883, and the lower line is the new median, Rs 2,350, the average of the two middle amounts. The mean jumped by more than Rs 14,000 and the median moved by Rs 50, and five of the six bars sit far below the mean line, which is the picture the room then looks for in its own sort of the 30 real amounts.


---

## Drawing 11: the lifts multiplying

It goes up in chapter 5, when marketing's "20 percent" is on the screen.

```mermaid
flowchart LR
    B["<b>today</b><br/>Rs 5,44,810"] --> C["<b>customers x 1.10</b><br/>Rs 5,99,291"]
    C --> F["<b>frequency x 1.10</b><br/>Rs 6,59,220, +21%"]
    B -.-> W["<b>added: +20%</b><br/>Rs 6,53,772"]
    B --> D["<b>15% off, quantity x 1.10</b><br/>0.85 x 1.10 = 0.935, a 6.5% fall"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    class C,F known
    class W,D bad
```

The line written under it: lifts multiply along the tree, so two 10 percent lifts make 21 percent, and a discount can lift quantity while revenue falls.


---

## Drawing 12: the window's edge

It goes up in chapter 6, when "70 percent of customers are lost" is on the screen and the room is
asked how long customers usually take to come back.

```mermaid
flowchart LR
    W["<b>88-day window</b><br/>1 July to 26 September"] --> B["<b>7 came back</b><br/>median gap 45 days"]
    W --> H["<b>7 bought once</b><br/>and had 45 days"]
    W --> R["<b>9 bought once</b><br/>in the last 45 days<br/>too recent to judge"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef unknown fill:#FFFFFF,stroke:#B8B2D6,color:#6B6690,stroke-dasharray:4 3
    class B,H known
    class R unknown
```

The line written under it: a one-time buyer is not a lost customer until they have had time to come
back.

---

## Drawing 13: the channel split, booked against delivered

It goes up in the second case, when a pair reports that store brings 91.6 percent of booked revenue and the room is asked how many orders stand behind that share.

```mermaid
flowchart LR
    S0["<b>store, all orders</b><br/>91.6% of booked<br/>resting on one order"] -.-> S["<b>store, consumer</b><br/>booked Rs 18,920 on 9"]
    S --> SD["<b>delivered Rs 9,870</b><br/>4 of 9 cancelled"]
    W["<b>web, consumer</b><br/>booked Rs 27,290 on 10"] --> WD["<b>delivered Rs 12,320</b><br/>5 of 10 returned"]
    A["<b>app, consumer</b><br/>booked Rs 18,600 on 10"] --> AD["<b>delivered Rs 18,600</b><br/>10 of 10"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    class S,W,A,AD known
    class S0,SD,WD bad
```

Consumer orders are the 29 outside the Business segment, Rs 64,810 booked. The two leaks, web returns and store cancellations, are written beside the tree as findings for the note to Meera, and the branch recommendation stays where the tree put it.


---

## What is on the board when the day ends

```mermaid
flowchart LR
    R["<b>revenue</b><br/>Rs 5,44,810 booked<br/>1 July to 26 September"] --> C["<b>customers</b><br/>23, Rs 12 crore waits"]
    R --> F["<b>orders per customer</b><br/>1.30, 7 back, 9 too recent<br/>open this first"]
    R --> A["<b>typical order</b><br/>median Rs 2,205"]
    A --> I["<b>basket, price, discounts</b><br/>not in this file"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef unknown fill:#FFFFFF,stroke:#B8B2D6,color:#6B6690,stroke-dasharray:4 3
    classDef bet fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class C,A known
    class I unknown
    class F bet
```

1. The story's six drawings stay up, and the metric tree carries the day's numbers: 23 customers,
   1.30 orders each, and a typical order of Rs 2,205, with the branch to open first marked.
2. Marketing's Rs 12 crore stays written against the customers branch, marked as waiting for
   Tuesday's two quarters.
3. The funnel of the four readings and the one-definition fraction sit in one corner.
4. The window's edge, 7 back, 7 had time, 9 too recent, sits under the frequency branch.
5. The two leaks from the channel split, web returns and store cancellations, sit beside the tree.
6. The six crux lines run down the side, and the sentence that went to Meera sits under the tree:
   "On the 30 booked orders from 1 July to 26 September, 23 customers placed 1.30 orders each at a
   typical order of Rs 2,205; 7 came back, 7 have had time and not returned, and 9 bought too
   recently to judge, so I would open frequency before acquisition, and since one quarter cannot
   show which branch moved, hold the Rs 12 crore until Tuesday's two quarters."
