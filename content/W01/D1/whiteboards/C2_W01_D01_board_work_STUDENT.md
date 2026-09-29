# The board, drawing by drawing

Week 1, Monday, Kalpa Retail. These are the drawings in the order they go up across the day. The deck, the notebooks and the cheat sheet carry the same revenue tree, so the tree copied from the board here is the one met everywhere else this week.

---

## Drawing 1: the revenue tree, with marketing's bet placed

It goes up in the first 20 minutes, straight after Meera's ask is read out and before any notebook opens.

```mermaid
flowchart LR
    R["<b>revenue</b><br/>4% against a 15% plan"] --> C["<b>customers</b><br/>distinct ids in the window"]
    R --> F["<b>orders per customer</b><br/>orders / distinct customers"]
    R --> A["<b>average order value</b><br/>revenue / orders"]
    A --> I["<b>items per order</b><br/>items / orders"]
    A --> P["<b>price per item</b><br/>revenue / items"]
    A --> D["<b>discounts</b><br/>rupees given back"]
    C -.- B["<b>Rs 12 crore</b><br/>marketing's bet"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef unknown fill:#FFFFFF,stroke:#B8B2D6,color:#6B6690,stroke-dasharray:4 3
    classDef bet fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class C,F,A known
    class I,P,D unknown
    class B bet
```

Each branch is written as a numerator over a denominator, and the bill for moving it goes beside it: customers cost marketing, frequency costs retention, basket costs merchandising, price risks volume, and discounts trade margin for quantity. The dashed branches need fields today's file does not carry.

---

## Drawing 2: the four readings of "sales", as a funnel

It goes up at the start of round 1, when the room names what "sales" could mean, and the numbers are written in once the loop has counted them.

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

The rule written under it is round 1's crux: the definition goes beside the number, and delivered, returned and cancelled add back to booked.

---

## Drawing 3: rows against customers

It goes up in round 2, when the trap's 1.00 is on the screen and the room is asked who those 30 rows are.

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

## Drawing 4: sorted amounts, with the mean and the median drawn on invented values

It goes up in round 3, after the room has seen the mean and the median of the real file and before anyone sorts it. The five amounts are invented, so the mechanism shows on numbers nobody has to trust.

```mermaid
xychart-beta
    title "Five invented orders, sorted, after the last is replaced"
    x-axis ["order 1", "order 2", "order 3", "order 4", "order 5"]
    y-axis "Rs" 0 --> 95000
    bar [1900, 2100, 2200, 2400, 90000]
    line [19720, 19720, 19720, 19720, 19720]
    line [2200, 2200, 2200, 2200, 2200]
```

The upper line is the mean, Rs 19,720, and the lower line is the median, Rs 2,200. Before the last amount was replaced, the five orders ran from Rs 1,900 to Rs 2,600 with a mean of Rs 2,240 and the same median. Four of the five bars sit far below the mean line, which is the picture the room then looks for in its own sort of the 30 real amounts.

---

## Drawing 5: the lifts multiplying

It goes up in the afternoon debrief, after the escalated case, when the room's "20 percent" answers are read out.

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

## Drawing 6: the channel split, booked against delivered

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
    R --> F["<b>orders per customer</b><br/>1.30, 16 of 23 bought once<br/>open this first"]
    R --> A["<b>typical order</b><br/>median Rs 2,205"]
    A --> I["<b>basket, price, discounts</b><br/>not in this file"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef unknown fill:#FFFFFF,stroke:#B8B2D6,color:#6B6690,stroke-dasharray:4 3
    classDef bet fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class C,A known
    class I unknown
    class F bet
```

1. The revenue tree carries the day's numbers: 23 customers, 1.30 orders each, and a typical order of Rs 2,205, with the branch to open first marked.
2. Marketing's Rs 12 crore stays written against the customers branch, marked as waiting for Tuesday's two quarters.
3. The funnel of the four readings stays in one corner with the definition rule under it.
4. The two leaks from the channel split, web returns and store cancellations, sit beside the tree.
5. The five crux lines run down the side, and the sentence that went to Meera sits under the tree: "On the 30 orders from 1 July to 26 September, 23 customers placed 1.30 orders each at a typical order of Rs 2,205, and 16 of them bought only once, so I would open frequency before acquisition; this one window cannot show which branch moved, so hold the Rs 12 crore until Tuesday's two quarters."
