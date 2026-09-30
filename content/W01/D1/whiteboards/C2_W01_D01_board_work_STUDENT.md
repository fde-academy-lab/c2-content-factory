# Which drawings go up on Monday's board, and in what order?

Week 1, Monday, Kalpa Retail. Meera Raghavan, Kalpa Retail's CEO, asks whether acquisition is even
the branch of sales that is short before she signs Rs 12 crore for new customers, and the room answers
on 30 orders placed from 1 July to 26 September. Six drawings go up during the retail story, one or
two during each of the six chapters, and one during the second case, and the metric tree drawn in the
story is the same tree the deck, the notebooks and the cheat sheet use all week.

---

## What happens between a supplier and a customer on one Saturday at Kalpa Retail?

Drawing 1 goes up in the story's first part. Each box is a place where the business measures
something, and section 1 of the domain dossier, on what happens at Kalpa Retail in one working day
(`study-notes/C2_W01_D01_domain_retail_STUDENT.md`), has the fuller drawing.

```mermaid
flowchart LR
    SUP["<b>suppliers</b><br/>share of each order filled"] --> DC["<b>distribution centre</b><br/>days of stock held"]
    DC --> ST["<b>store</b><br/>visitors, bills"]
    DC --> LM["<b>last mile</b><br/>the van to the door"]
    APP["<b>the app</b><br/>visitors, orders"] --> LM
    LM -.-> RD["<b>returns desk</b><br/>parcels that come back"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    class SUP,DC,ST,APP,LM,RD known
```

A store's till keeps the bill, while the app keeps every search, cart and order, so the data team
works where customers leave traces, and customers leave far more of them on the app.

---

## Which real companies does Kalpa look like, and which of its units is the room's client today?

Drawing 2 goes up in the story's second part. Kalpa Group is fictional; the real companies are
likenesses, and the dossier's section 2, on which real companies work the way Kalpa Retail does,
names them all.

```mermaid
flowchart TB
    G["<b>Kalpa Group</b><br/>Singapore HQ"] --> R["<b>Retail</b><br/>today"]
    G --> H["<b>Health</b><br/>Build 1"]
    G --> F["<b>Financial Services</b><br/>Week 5"]
    G --> O["<b>Connect, Logistics</b><br/>later"]
    R & H & F & O -.- C["<b>the GCC, Bengaluru</b><br/>you"]
    classDef unit fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef dark fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class R,H,F,O unit
    class G,C dark
```

Reliance runs Jio and Reliance Retail in one group, as Kalpa runs its units, and Kalpa Retail's
stores work like DMart's. The GCC is Kalpa's Global Capability Centre, its own data and AI team in
Bengaluru, and Retail is its client for the first two weeks.

---

## How much of Rs 100 at the checkout does Kalpa keep?

Drawing 3 goes up in the story's third part and stays up all day. Gross merchandise value, GMV, is
everything customers ordered at the prices charged, and net revenue is the smaller figure Finance
reports as earned from the goods. The two differ, and the Rs 20 between them stays open on the board
until chapter 1 answers it from the file. The amounts are illustrative.

```mermaid
flowchart TB
    G["<b>GMV</b><br/>Rs 100 ordered"] -->|"Rs 20 between them:<br/>chapter 1's question"| N["<b>net revenue</b><br/>Rs 80"]
    N -->|"less Rs 60 cost of goods"| M["<b>gross margin</b><br/>Rs 20"]
    M -->|"less Rs 12.50 per-order costs"| C["<b>contribution</b><br/>Rs 7.50"]
    C -->|"less Rs 5 fixed costs"| O["<b>EBITDA</b><br/>Rs 2.50"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef dark fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class G,N,M,C known
    class O dark
```

EBITDA is earnings before interest, tax, depreciation and amortisation, what is left after the goods,
the costs every order brings and the fixed costs of stores, warehouses, technology and head office.
Rs 2.50 of every Rs 100 is a thin slice, and real retailers keep one too: DMart's profit after tax
was 4.8 percent of its FY26 revenue (DMart results release, 2 May 2026).

---

## Who at Kalpa asks the data team for a number?

Drawing 4 goes up in the story's fourth part. Solid lines are reporting lines to the CEO, dotted
arrows are asks that reach the data team, and the dashed box holds functions whose heads the story has not named.

```mermaid
flowchart LR
    CEO["<b>CEO</b><br/>Meera Raghavan"] --> FIN["<b>Finance</b><br/>Anand Iyer"]
    CEO --> MKT["<b>Marketing, Retail-Plus</b><br/>their leads"]
    CEO --> CS["<b>Customer support</b><br/>Farhan Sheikh, Week 8"]
    CEO --> OTH["<b>the other functions</b><br/>buying, pricing,<br/>supply chain, stores"]
    FIN & MKT & CS & OTH -.-> GCC["<b>Kalpa's GCC</b><br/>Kavya Nair and you"]
    CEO -.-> GCC
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef unknown fill:#FFFFFF,stroke:#B8B2D6,color:#6B6690,stroke-dasharray:4 3
    classDef dark fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class FIN,MKT,CS known
    class OTH unknown
    class CEO,GCC dark
```

Anand Iyer is the finance controller, Retail-Plus is Kalpa's paid membership tier, and Kavya Nair is
the senior analyst who checks every number before it leaves the team. A wrong dashboard figure can be
corrected before anyone acts on it, and a budget already spent cannot.

---

## What is revenue made of, and what does each branch divide by?

Drawing 5 goes up in the story's fifth part and stays up all day, since the day's case writes its
numbers on it. The dossier's section 5, on which numbers run Kalpa Retail, draws the full tree.

```mermaid
flowchart TB
    S["<b>on the shelf</b><br/>stock and days held"] -.-> R["<b>revenue</b><br/>customers x orders per customer<br/>x average order value"]
    R --> C["<b>customers</b><br/>new and returning"]
    R --> F["<b>orders per customer</b><br/>orders / customers"]
    R --> A["<b>average order value</b><br/>revenue / orders"]
    A --> I["<b>items x price</b><br/>less discounts"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef dark fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class C,F,A,I known
    class R,S dark
```

Nothing sells that is not on the shelf, so the shelf sits above revenue. When Meera's ask is read out,
marketing's Rs 12 crore is written against the customers branch, and each chapter adds one number.

---

## How far should a system act before a person checks it?

Drawing 6 goes up in the story's last part, and the dossier's section 8, on where analytics, ML, NLP
and agents pay for themselves, has the fuller ladder.

```mermaid
flowchart LR
    D["<b>describe</b><br/>what happened<br/>a person reads it"] --> P["<b>predict</b><br/>what will happen<br/>a person decides"]
    P --> R["<b>recommend</b><br/>what to do<br/>a person approves"]
    R --> A["<b>act</b><br/>an agent does it<br/>within limits"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    class D,P,R known
    class A bad
```

The further right a system sits, the more a wrong answer costs, because fewer people see it before it
takes effect. Meera's page on Monday is the left end of this ladder, and she decides on it.

---

## Which of the file's totals is sales, and what does each one count?

Drawing 7 goes up at the start of chapter 1, when the room names what sales could mean, and the
numbers are written in once the loop has counted them.

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

The line written under it is chapter 1's answer: the definition goes beside the number, and
delivered, returned and cancelled add back to booked. The Rs 24,020 between booked and delivered is
the part of drawing 3's gap between GMV and net revenue that this file holds.

---

## Why does booked revenue over delivered orders match nothing?

Drawing 8 goes up in chapter 2, when the mixed average order value of Rs 25,943 is on the screen.

```mermaid
flowchart LR
    F["<b>Finance</b><br/>booked Rs 5,44,810"] --> X["<b>Rs 25,943</b><br/>x 30 = about Rs 7,78,300<br/>lands on nothing"]
    O["<b>dashboard</b><br/>21 delivered orders"] --> X
    B["<b>booked / booked</b><br/>Rs 18,160"] --> OK["<b>x orders lands<br/>on its revenue</b>"]
    D["<b>delivered / delivered</b><br/>Rs 24,800"] --> OK
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    class B,D,OK known
    class F,O,X bad
```

The check written under it: average order value times the orders its revenue was summed over gives
that revenue back, or the fraction mixes two reports.

---

## How many customers stand behind 30 rows?

Drawing 9 goes up in chapter 3, when a colleague's draft of 1.00 orders each is on the screen and the
room is asked who those 30 rows are.

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

The check goes beside it in code: the length of the rows against the length of the set of customer
ids, 30 against 23.

---

## Why does one large order move the mean so much more than the median?

Drawing 10 goes up in chapter 4, after the build's median of Rs 2,205 and before each learner's own
sort. Every amount here is invented, so the mechanism shows on numbers nobody has to trust.

```mermaid
xychart-beta
    title "Six invented orders, sorted, after the sixth is added"
    x-axis ["order 1", "order 2", "order 3", "order 4", "order 5", "order 6"]
    y-axis "Rs" 0 --> 95000
    bar [1900, 2100, 2300, 2400, 2600, 90000]
    line [16883, 16883, 16883, 16883, 16883, 16883]
    line [2350, 2350, 2350, 2350, 2350, 2350]
```

Five invented orders of Rs 1,900, 2,100, 2,300, 2,400 and 2,600 go up first, with a mean of Rs 2,260
and a median of Rs 2,300. An invented Rs 90,000 order is then added as the sixth. The upper line is the
new mean, Rs 16,883, and the lower line the new median, Rs 2,350, the average of the two middle
amounts. The mean jumped by more than Rs 14,000 while the median moved Rs 50, and five of the six bars
sit far below the mean line, which is the picture the room then looks for in its own sort of the 30
real amounts, where only 1 of the 30 sits above the mean of Rs 18,160.

---

## What do two 10 percent lifts make on the consumer segments' Rs 64,810?

Drawing 11 goes up in chapter 5, when marketing's 20 percent is on the screen. The consumer view keeps
the orders whose segment is Retail-Core, Retail-Plus or Student, the three segments Meera's growth
plan concerns, and they booked Rs 64,810, so the 15 percent plan is about Rs 9,722 more.

```mermaid
flowchart LR
    B["<b>consumer view</b><br/>Rs 64,810 booked"] --> C["<b>customers x 1.10</b><br/>Rs 71,291"]
    C --> F["<b>frequency x 1.10</b><br/>Rs 78,420, +21%"]
    B -.-> W["<b>added: +20%</b><br/>Rs 77,772"]
    B --> D["<b>15% off, orders x 1.10</b><br/>0.85 x 1.10 = 0.935, a 6.5% fall"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    class C,F known
    class W,D bad
```

The line written under it: lifts multiply along the tree, so two 10 percent lifts make 21 percent, and
a discount can lift orders while revenue falls.

---

## How many of the 16 one-time buyers are too recent to judge?

Drawing 12 goes up in chapter 6, when "70 percent of customers are lost" is on the screen and the room
is asked how long customers usually take to come back.

```mermaid
flowchart LR
    W["<b>88-day window</b><br/>1 July to 26 September"] --> B["<b>7 came back</b><br/>median gap 45 days"]
    W --> H["<b>7 bought once</b><br/>and had 45 days"]
    W --> R["<b>9 bought once</b><br/>under 45 days<br/>before the end<br/>too recent to judge"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef unknown fill:#FFFFFF,stroke:#B8B2D6,color:#6B6690,stroke-dasharray:4 3
    class B,H known
    class R unknown
```

The line written under it: a one-time buyer is not a lost customer until they have had time to come
back.

---

## Where does store's 91.6 percent come from, and what does each channel keep?

Drawing 13 goes up in the second case, when a pair reports that store brings 91.6 percent of booked
revenue and the room is asked whose revenue that share is.

```mermaid
flowchart LR
    S0["<b>store, all orders</b><br/>91.6% of booked"] -.-> S["<b>store, consumer view</b><br/>Rs 18,920, 29.2%"]
    S --> SD["<b>delivered Rs 9,870</b><br/>Rs 9,050 cancelled"]
    W["<b>web, consumer view</b><br/>Rs 27,290, 42.1%"] --> WD["<b>delivered Rs 12,320</b><br/>Rs 14,970 returned"]
    A["<b>app, consumer view</b><br/>Rs 18,600, 28.7%"] --> AD["<b>delivered Rs 18,600</b><br/>all of it"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    class S,W,A,AD known
    class S0,SD,WD bad
```

The consumer view keeps the three consumer segments Meera's plan concerns, Rs 64,810 booked. Once the
view keeps them, store's share falls from 91.6 to 29.2 percent, so store's headline share came from
outside those segments. The two leaks, web returns and store cancellations, go beside the tree as
findings for the note to Meera, and the branch stays where the tree put it.

---

## What is on the board when the day ends?

```mermaid
flowchart LR
    R["<b>revenue</b><br/>Rs 5,44,810 booked<br/>1 July to 26 September"] --> C["<b>customers</b><br/>23, Rs 12 crore waits"]
    R --> F["<b>orders per customer</b><br/>1.30, 7 back, 9 too recent<br/>open this first"]
    R --> A["<b>typical order</b><br/>median Rs 2,205"]
    A --> I["<b>items, price, discounts</b><br/>not in this file"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef unknown fill:#FFFFFF,stroke:#B8B2D6,color:#6B6690,stroke-dasharray:4 3
    classDef bet fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class C,A known
    class I unknown
    class F bet
```

1. The metric tree carries the day's numbers, 23 customers, 1.30 orders each and a typical order of
   Rs 2,205, with frequency marked as the branch to open first, and the Rs 100 journey stays beside it.
2. Marketing's Rs 12 crore stays written against the customers branch, marked as waiting for
   Tuesday's two quarters.
3. The four readings of sales and the one-definition fraction sit in one corner.
4. The window's edge, 7 back, 7 past the usual gap and 9 too recent, sits under the frequency branch.
5. The two leaks from the channel split, web returns and store cancellations, sit beside the tree.
6. The six lines to carry run down the side, and the sentence that went to Meera sits under the tree:
   "On the 30 booked orders from 1 July to 26 September, 23 customers placed 1.30 orders each at a
   typical order of Rs 2,205; 7 came back, 7 are past the usual gap without a second order, and 9
   bought too recently to judge, so I would open frequency before acquisition, and since one quarter
   cannot show which branch moved, hold the Rs 12 crore until Tuesday's two quarters."
