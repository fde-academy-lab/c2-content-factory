# What goes on the board, in order, from the concept map to the priced strip?

A hostel canteen's twelve lunch orders and a Pune corner shop's month, both invented, carry the five
topics; then Swiggy Instamart, Pune: the cart page's strip of three suggested items, whose
click-through fell from 6.1 to 3.8 percent after it began showing the items most often found in the
same cart. Illustrative case: the company is real, the situation and the data are synthetic, built
for this class.

**Who needs the answer.** Anyone redrawing the day: each drawing below goes up in this order, and the
last one is what the board holds when the day ends.

**The questions on the way.**

- How do the five topics join?
- What do the canteen's twelve orders count to?
- How does confidence shrink the world?
- Which pairs beat chance, drawn as one concept board?
- What does the kirana's combo card earn?
- What do the twelve cards count to?
- Where does lift join the week?
- How do two click-through rates make 3.8 percent?
- Where does each pair sit on the action map?
- What is a slot worth?
- What does the board hold at the close?

## How do the five topics join?

Drawn before the room sits down, on the left of the board, and left up all day; each box gets its
number as its chapter closes.

```mermaid
flowchart TB
    T1["<b>1 · Support, confidence and lift,</b><br/><b>derived by counting</b><br/>chapters 1, 2, 3"] --> T2["<b>2 · The confidence trap;</b><br/><b>lift near one</b><br/>chapter 4"]
    T2 --> T3["<b>3 · Basket analysis on</b><br/><b>the order items</b><br/>chapter 5"]
    T3 --> T4["<b>4 · The support floor</b><br/><b>and the watch list</b><br/>chapter 6"]
    T4 --> T5["<b>5 · Cross-sell and upsell;</b><br/><b>expected value in rupees</b><br/>chapter 9"]
    T5 --> C["<b>The case and the lab</b><br/>chapters 7, 8, 10;<br/>notebook 11"]
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    class T1,T2,T3,T4,T5 lit
    class C known
```

## What do the canteen's twelve orders count to?

Written as the groups call their counts from the canteen cards in chapters 1 to 3, before any formula
is named. The orders are invented.

```mermaid
flowchart LR
    B["<b>roti and sabzi</b><br/>roti 4, sabzi 4, both 3"] --> S["<b>support</b><br/>3 / 12 = 0.25"]
    B --> F["<b>confidence</b><br/>roti to sabzi<br/>3 / 4 = 0.75"]
    E["<b>chance</b><br/>12 x 4/12 x 4/12 = 1.33"] --> L["<b>lift</b><br/>3 / 1.33 = 2.25"]
    B --> L
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class B,S,F,E known
    class L lit
```

## How does confidence shrink the world?

Drawn in chapter 2 on the canteen, and again in chapter 7 on the twelve carts.

```mermaid
flowchart LR
    A["<b>all twelve orders</b>"] --> B["<b>dal rice's orders</b><br/>6 of them"]
    B --> C["<b>with papad too</b><br/>3 of 6 = 0.50"]
    A --> D["<b>papad's orders</b><br/>5 of them"]
    D --> E["<b>with dal rice too</b><br/>3 of 5 = 0.60"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class A,B,D known
    class C,E lit
```

## Which pairs beat chance, drawn as one concept board?

Built through chapters 1 to 6: the example goes up with the cards, each question as its count is
called, the sketches as each picture is drawn, and the two pitfalls last.

```mermaid
flowchart LR
    subgraph A["The example"]
        A1["<b>a hostel canteen</b><br/>roti in 4, sabzi in 4,<br/>both in 3 of 12"]
    end
    subgraph Q["Questions"]
        direction TB
        Q1["<b>how often?</b><br/>support 0.25"] ~~~ Q2["<b>how reliably?</b><br/>confidence 0.75"] ~~~ Q3["<b>against chance?</b><br/>lift 2.25"]
    end
    subgraph S["Sketches"]
        direction TB
        S1["<b>two circles</b><br/>beside the 2 by 2"] ~~~ S2["<b>the world shrinks</b><br/>12 orders, 6 with dal rice"] ~~~ S3["<b>seen against chance</b><br/>3 against 1.33"]
    end
    subgraph P["Pitfalls"]
        direction TB
        P1["<b>the popular partner</b><br/>chaas in 9 of 12"] ~~~ P2["<b>thin support</b><br/>lift 6.0 on one order"]
    end
    A --> Q --> S --> P
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef trap fill:#FFF1F1,stroke:#C0392B,color:#5C1111
    class A1,Q1,Q2,S1,S2,S3 known
    class Q3 lit
    class P1,P2 trap
```

## What does the kirana's combo card earn?

Built left to right in chapter 9, one bar at a time. The month is invented.

```mermaid
flowchart LR
    N["<b>new packs</b><br/>450 tea-only bills<br/>x 4 percent = 18"] --> M["<b>margin</b><br/>18 x Rs 12 = Rs 216"]
    M --> D["<b>handed back</b><br/>Rs 1 on 168 bills<br/>= Rs 168"]
    D --> P["<b>printing</b><br/>Rs 20"]
    P --> V["<b>expected value</b><br/>Rs 28 a month"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class N,M,D,P known
    class V lit
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

## Where does lift join the week?

Added under Wednesday's node at the close of chapter 3, and left up all day.

```mermaid
flowchart LR
    M["<b>Mon</b><br/>trips an online hour"] --> T["<b>Tue</b><br/>one slide"]
    T --> W["<b>Wed</b><br/>lift: beyond chance"]
    W --> H["<b>Thu</b><br/>groups behind one number"]
    H --> F["<b>Fri</b><br/>a forecast against a simple rule"]
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

The wall board, with the pair cards placed in chapter 10. Support runs across with the 1 percent
floor at the middle, and lift runs up; the positions are sketched, and notebook 10's picture draws
them to scale. Chapter 6 drew the same four regions for the canteen.

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
    M --> R["<b>milk taken out, a month</b><br/>about Rs 6.3 lakh, gross"]
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
    R["<b>Rank</b><br/>lift 1.5 up, 1% floor<br/>3.39, 3.00, 2.21, 1.70"] --> W["<b>Watch</b><br/>ice cream and sauce<br/>4.60 on 100 carts"]
    W --> P["<b>Price</b><br/>Rs 17,280 against<br/>Rs 3,240 a day"]
    P --> M["<b>Month</b><br/>milk out: about<br/>Rs 6.3 lakh, gross"]
    M --> D["<b>Doubts</b><br/>per customer 2.56<br/>curd's lift stays 1.01"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    class R,W,P,M,D known
```

> The click-through fell because the strip gave half its slots to milk, which shoppers buy anyway.
> Taking milk out, which ranking by lift above a 1 percent floor and a 1.5 bar does by arithmetic,
> recovers about Rs 6.3 lakh a month before the adds that would have come anyway; a test against a
> count ranking without milk shows whether lift earns more.
