# What goes on the board, in order, from the ten dots to the priced strip?

Swiggy Instamart, Pune: the cart page's strip of three suggested items, whose click-through fell from
6.1 to 3.8 percent after it began showing the items most often found in the same cart. Illustrative
case: the company is real, the situation and the data are synthetic, built for this class.

**Who needs the answer.** Anyone redrawing the day: each drawing below goes up in this order, and the
last one is what the board holds when the day ends.

**The questions on the way.**

- What do ten orders look like as counts?
- What do the twelve cards count to?
- How does confidence shrink the world?
- Which pairs beat chance, drawn as one concept board?
- Where does lift join the week?
- How do two click-through rates make 3.8 percent?
- Where does each pair sit on the action map?
- What is a slot worth?
- What does the board hold at the close?

## What do ten tea-stall orders look like as counts?

Drawn before the room sits down, beside the ten dots. The orders are invented.

```mermaid
flowchart LR
    B["<b>both</b><br/>3 orders"] --> S["<b>support</b><br/>3 / 10 = 0.30"]
    C["<b>chai</b><br/>6 orders"] --> F["<b>confidence</b><br/>chai to biscuit<br/>3 / 6 = 0.50"]
    B --> F
    E["<b>chance</b><br/>10 x 0.6 x 0.4 = 2.4"] --> L["<b>lift</b><br/>3 / 2.4 = 1.25"]
    B --> L
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class B,C,E known
    class L lit
```

## What do the twelve cards count to?

Written as each group calls its counts out, before any formula is named.

```mermaid
flowchart LR
    A["<b>bread and milk</b><br/>bread 4, milk 8, both 4<br/>chance 2.67, lift 1.50"] --> B["<b>chips and cold drink</b><br/>3 and 3, both 2<br/>chance 0.75, lift 2.67"]
    B --> C["<b>ice cream and sauce</b><br/>1 and 1, both 1<br/>lift 12 on one cart"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    class A,B,C known
```

## How does confidence shrink the world?

```mermaid
flowchart LR
    A["<b>all twelve carts</b><br/>milk in 8"] --> B["<b>only the bread carts</b><br/>4 of them"]
    B --> C["<b>bread carts with milk</b><br/>4 of 4 = 1.00"]
    A -.-> D["<b>lift asks</b><br/>is 1.00 more than<br/>milk's own 8 of 12?"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef unknown fill:#FFFFFF,stroke:#B8B2D6,color:#6B6690,stroke-dasharray:4 3
    class A,B,C known
    class D unknown
```

## Which pairs beat chance, drawn as one concept board?

Built through chapter 1: the anchor goes up with the dots, each question as its count is called,
the sketches as each picture is drawn, and the two pitfalls last.

```mermaid
flowchart LR
    subgraph A["Anchor"]
        A1["<b>a tea stall</b><br/>chai in 6, biscuit in 4,<br/>both in 3 of 10"]
    end
    subgraph Q["Questions"]
        direction TB
        Q1["<b>how often?</b><br/>support 0.30"] ~~~ Q2["<b>how reliably?</b><br/>confidence 0.50"] ~~~ Q3["<b>against chance?</b><br/>lift 1.25"]
    end
    subgraph S["Sketches"]
        direction TB
        S1["<b>two circles</b><br/>beside the 2 by 2"] ~~~ S2["<b>the world shrinks</b><br/>12 carts, 4 with bread"] ~~~ S3["<b>seen against expected</b><br/>4 against 2.67"]
    end
    subgraph P["Pitfalls"]
        direction TB
        P1["<b>the popular partner</b><br/>milk in 8 of 12"] ~~~ P2["<b>thin support</b><br/>lift 12 on one cart"]
    end
    A --> Q --> S --> P
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef trap fill:#FFF1F1,stroke:#C0392B,color:#5C1111
    class A1,Q1,Q2,S1,S2,S3 known
    class Q3 lit
    class P1,P2 trap
```

## Where does lift join the week?

Added under Wednesday's node at the close of chapter 1, and left up all day.

```mermaid
flowchart LR
    M["<b>Mon</b><br/>trips an online hour"] --> T["<b>Tue</b><br/>one slide"]
    T --> W["<b>Wed</b><br/>lift: beyond chance"]
    W --> H["<b>Thu</b><br/>beyond the blend"]
    H --> F["<b>Fri</b><br/>beyond the baseline"]
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class W lit
```

## How do two click-through rates make 3.8 percent?

```mermaid
flowchart LR
    A["<b>milk slots</b><br/>half the impressions<br/>1.2 percent"] --> C["<b>the strip</b><br/>0.5 x 1.2 + 0.5 x 6.4<br/>= 3.8 percent"]
    B["<b>every other slot</b><br/>half the impressions<br/>6.4 percent"] --> C
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class A,B known
    class C lit
```

## Where does each pair sit on the action map?

The wall board, with the pair cards placed. Support runs across with the 1 percent floor at the
middle, and lift runs up; the positions are sketched, and notebook 03's picture draws them to scale.

```mermaid
quadrantChart
    title Lift against support, 40,000 carts
    x-axis Fewer carts --> More carts
    y-axis Near chance --> Well above chance
    quadrant-1 Promote
    quadrant-2 Watch
    quadrant-3 Ignore
    quadrant-4 Trap
    chips and cold drink: [0.73, 0.79]
    coriander and chillies: [0.68, 0.73]
    bread and butter: [0.72, 0.61]
    onions and tomatoes: [0.79, 0.53]
    bread and milk: [0.86, 0.22]
    eggs and milk: [0.80, 0.10]
    ice cream and sauce: [0.30, 0.95]
    namkeen and poha: [0.32, 0.30]
    butter and tomatoes: [0.54, 0.22]
```

## What is a slot worth?

```mermaid
flowchart LR
    V["<b>views</b><br/>60,000 a day"] --> C["<b>clicks</b><br/>x 6.4 percent<br/>= 3,840"]
    C --> A["<b>adds</b><br/>x 0.5<br/>= 1,920"]
    A --> M["<b>margin</b><br/>x Rs 9<br/>= Rs 17,280 a day"]
    M --> R["<b>re-ranked, a month</b><br/>Rs 6.3 lakh recovered"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class V,C,A known
    class M,R lit
```

## What does the board hold at the close?

The chain below, the week map with lift under Wednesday, the action map with its cards, and the
sentence for Friday written under them all.

```mermaid
flowchart LR
    R["<b>Rank</b><br/>lift above a 1% floor<br/>3.39, 3.00, 2.21"] --> W["<b>Watch</b><br/>ice cream and sauce<br/>4.60 on 100 carts"]
    W --> P["<b>Price</b><br/>Rs 17,280 against<br/>Rs 3,240 a day"]
    P --> M["<b>Month</b><br/>Rs 6.3 lakh recovered"]
    M --> D["<b>Doubts</b><br/>per customer 2.56<br/>curd's lift stays 1.01"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    class R,W,P,M,D known
```

> The click-through fell because the strip gave half its slots to milk, which shoppers buy anyway;
> ranked by lift above a 1 percent floor, the strip shows chips with cold drink, coriander with green
> chillies and bread with butter, and recovers about Rs 6.3 lakh a month.
