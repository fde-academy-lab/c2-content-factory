# What goes on the board on Monday, and in what order?

*Illustrative case: the company is real, the situation and the data are synthetic, built for this class.*

Uber, Hyderabad, the driver app. From 31 August 2026 an enrolled driver online through a whole peak window
is guaranteed Rs 300 per peak online hour. Six weeks later peak online hours are up 24 percent, completed
peak trips up 3 percent, and trips per peak online hour down from 1.90 to 1.58, with Rs 1.9 crore paid in
top-up. The city head asks, by Friday, whether the scheme works, what it should pay for, and whether
anyone is gaming it.

**Who needs the answer.** The trainer, who draws these in order, and you, if you missed a drawing or want
to redraw the board from memory before Tuesday.

**The questions on the way.** Each heading below asks the question one drawing answers, in the order the drawings go up, and the last asks what stays on the board at the end.

---

## Where does today's ticket sit in the week?

Goes up first, before the ticket is discussed. Monday is lit; the other days stay dashed until they come.

```mermaid
flowchart TD
    C["<b>What does an analyst do with one number?</b><br/>five tickets, five companies, one method a day"]
    M["<b>Mon: is the number measuring what we want?</b><br/>Uber, Hyderabad: online hours against trips<br/>metric design, guardrails, gaming"]
    T["<b>Tue: can it survive one slide?</b><br/>Uber, Hyderabad, one day on<br/>the one-slide answer, the guesstimate"]
    W["<b>Wed: what goes with what?</b><br/>Swiggy Instamart, Pune<br/>support, confidence, lift"]
    H["<b>Thu: who is leaving, at which step?</b><br/>Zomato Gold, Chennai<br/>cohorts, funnels, denominators"]
    F["<b>Fri: how much is coming?</b><br/>Flipkart, Lucknow<br/>baselines, hold-out, cost"]
    S["<b>Sat: does the method travel?</b><br/>other companies, then Kalpa"]
    K1["Kalpa Retail: the auto-reorder window"]
    K3["Kalpa Retail: the Rs 199 charger"]
    K4["Kalpa Retail: the Retail-Plus tier"]
    K5["Kalpa Retail: 24 months and a vendor curve"]
    C --> M
    C --> W
    C --> H
    C --> F
    M -.- T
    M --> K1
    W --> K3
    H --> K4
    F --> K5
    T --> S
    K1 --> S
    K3 --> S
    K4 --> S
    K5 --> S
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef unknown fill:#FFFFFF,stroke:#B8B2D6,color:#6B6690,stroke-dasharray:4 3
    classDef kalpa fill:#FFF7E6,stroke:#C98A00,color:#5C3D00
    class C known
    class M lit
    class T,W,H,F,S unknown
    class K1,K3,K4,K5 kalpa
```

---

## Which four questions must a number answer before anyone is paid for it?

The day's concept board, empty but for its anchor. Each chapter fills one region.

```mermaid
flowchart LR
    Q["<b>What makes a number safe to pay for?</b>"]
    A["<b>Anchor: the canteen token</b><br/>tokens 200 to 400, plates stay 200<br/>(invented numbers)"]
    Q1["<b>What is it for?</b>"]
    Q2["<b>How could it rise while<br/>riders waited longer?</b>"]
    Q3["<b>What stops that?</b>"]
    Q --> A
    Q --> Q1
    Q --> Q2
    Q --> Q3
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef unknown fill:#FFFFFF,stroke:#B8B2D6,color:#6B6690,stroke-dasharray:4 3
    class Q lit
    class A known
    class Q1,Q2,Q3 unknown
```

---

## What happens to a token once servers are paid per token?

The canteen, invented numbers: tokens double from 200 to 400 a day while plates stay at 200.

```mermaid
flowchart LR
    G["<b>What the canteen wants</b><br/>plates served to hungry diners"] --> P["<b>What it pays for</b><br/>tokens printed"]
    P --> C["<b>What a server can do</b><br/>print two tokens per plate"]
    C --> N["<b>What the number says</b><br/>tokens 200 to 400 a day"]
    C --> D["<b>What diners see</b><br/>plates stay at 200"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    class G,P,N known
    class C,D bad
```

---

## What did six drivers' hours and trips do, counted by hand?

Hours 60 then 74, trips 114 then 88: 1.90 then 1.19 trips per hour. Two of the six, E and F, sit in the idle tail, a third of the sample against 15 percent of the city.

```mermaid
flowchart LR
    B["<b>Before: six drivers</b><br/>60 hours, 114 trips"] -->|"114 / 60"| RB["<b>1.90</b><br/>trips per hour"]
    A["<b>After: the same six</b><br/>74 hours, 88 trips"] -->|"88 / 74"| RA["<b>1.19</b><br/>trips per hour"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class B,A known
    class RB,RA lit
```

---

## What does the board hold after chapter 1?

The first region filled: what the number is for, and the first pitfall.

```mermaid
flowchart LR
    Q["<b>What makes a number safe to pay for?</b>"]
    A["<b>Anchor: the canteen token</b><br/>tokens doubled, plates did not"]
    Q1["<b>What is it for?</b><br/>riders picked up faster;<br/>hours need no rider"]
    Q2["<b>How could it rise while<br/>riders waited longer?</b>"]
    Q3["<b>What stops that?</b>"]
    P1["<b>Pitfall: no usage condition</b><br/>Wells Fargo's unused accounts"]
    Q --> A
    Q --> Q1
    Q --> Q2
    Q --> Q3
    Q1 --> P1
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef unknown fill:#FFFFFF,stroke:#B8B2D6,color:#6B6690,stroke-dasharray:4 3
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    class Q lit
    class A,Q1 known
    class Q2,Q3 unknown
    class P1 bad
```

---

## Why does an average of each driver-week's rate mislead?

Two invented drivers: 21 trips over 11 hours is 1.91, while the average of their rates is 1.5. On the city, the average prints 1.71 against the true 1.58.

```mermaid
flowchart LR
    X["<b>Driver X</b><br/>2.0 trips an hour, 10 hours<br/>20 trips"] --> S["<b>Ratio of sums</b><br/>21 trips / 11 hours = 1.91"]
    Y["<b>Driver Y</b><br/>1.0 trip an hour, 1 hour<br/>1 trip"] --> S
    X --> M["<b>Average of rates</b><br/>(2.0 + 1.0) / 2 = 1.5"]
    Y --> M
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    class X,Y,S known
    class M bad
```

---

## What does the board hold after chapter 2?

The second region filled: how the number rose while riders were served no faster.

```mermaid
flowchart LR
    Q["<b>What makes a number safe to pay for?</b>"]
    Q1["<b>What is it for?</b><br/>riders picked up faster"]
    Q2["<b>How could it rise while<br/>riders waited longer?</b><br/>online but idle, in thin zones:<br/>180 drivers, 15 percent"]
    Q3["<b>What stops that?</b>"]
    P1["<b>Pitfall: no usage condition</b><br/>Wells Fargo"]
    P2["<b>Pitfall: the unit moves the number</b><br/>Delhi Metro; offers and requests"]
    Q --> Q1
    Q --> Q2
    Q --> Q3
    Q1 --> P1
    Q2 --> P2
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef unknown fill:#FFFFFF,stroke:#B8B2D6,color:#6B6690,stroke-dasharray:4 3
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    class Q lit
    class Q1,Q2 known
    class Q3 unknown
    class P1,P2 bad
```

---

## What decision would the celebrated number have sent?

The wrong memo, the check that catches it and the fix, side by side.

```mermaid
flowchart LR
    N["<b>The number</b><br/>peak online hours up 24 percent"] --> D["<b>The memo</b><br/>supply target met;<br/>extend to two more cities"]
    D --> C["<b>What it would buy</b><br/>the same top-up,<br/>paid in three cities"]
    K["<b>The check</b><br/>trips per hour 1.90 to 1.58;<br/>waits 4.8 to 4.6 minutes"] -.-> D
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    class N,D,C bad
    class K known
```

---

## How do a north star, its guardrails and its inputs fit together?

Built one region at a time: the north star, then each guardrail with the gaming it catches, then the two inputs. Read it as a seesaw: if the north star rises and a guardrail drops, the rise was bought.

```mermaid
flowchart TD
    N["<b>North star</b><br/>completed peak trips per enrolled<br/>driver online at peak, per week"]
    G1["<b>Guardrail 1</b><br/>offers accepted over offers shown,<br/>at or above a floor"]
    G2["<b>Guardrail 2</b><br/>median rider wait at peak"]
    G3["<b>Guardrail 3</b><br/>top-up per completed trip"]
    L1["<b>Input</b><br/>enrolled drivers online<br/>in the first peak hour"]
    L2["<b>Input</b><br/>rider requests per online<br/>hour, by zone"]
    N --- G1
    N --- G2
    N --- G3
    L1 -.-> N
    L2 -.-> N
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef kalpa fill:#FFF7E6,stroke:#C98A00,color:#5C3D00
    class N lit
    class G1,G2,G3 known
    class L1,L2 kalpa
```

---

## What makes a number safe to pay for, now that the board is finished?

The finished board, which is panel one of the cheat sheet.

```mermaid
flowchart LR
    Q["<b>Safe to pay for?</b>"]
    Q1["<b>What is it for?</b><br/>riders picked up faster"]
    Q2["<b>How could it rise badly?</b><br/>online but idle, thin zones"]
    Q3["<b>What stops that?</b><br/>north star and guardrails"]
    S1["<b>The tree</b>"]
    S2["<b>The seesaw</b>"]
    S3["<b>The window's start</b>"]
    P1["<b>No usage condition</b><br/>Wells Fargo"]
    P2["<b>The unit moves it</b><br/>Delhi Metro"]
    P3["<b>The measured set the start</b><br/>VA"]
    Q --> Q1
    Q --> Q2
    Q --> Q3
    Q3 --> S1
    Q3 --> S2
    Q3 --> S3
    Q1 --> P1
    Q2 --> P2
    S3 --> P3
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    class Q lit
    class Q1,Q2,Q3,S1,S2,S3 known
    class P1,P2,P3 bad
```

---

## How does round 3 of the war game run?

The afternoon's first drawing: write, price, defend, score.

```mermaid
flowchart LR
    W["<b>Write, 14 minutes</b><br/>the seven lines, two guardrails<br/>or more, the gaming note"] --> P["<b>Price</b><br/>the saving, with its<br/>assumption stated"]
    P --> D["<b>Defend, 10 minutes</b><br/>each role attacks once;<br/>a line must answer"]
    D --> S["<b>Score, 3 minutes</b><br/>answered, conceded<br/>or lost"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class W,P,D known
    class S lit
```

---

## What structure does a hire-grade answer give the interviewer?

Goal, north star, guardrails, leading input, the test: the order a strong candidate says it aloud.

```mermaid
flowchart LR
    G["<b>Goal</b><br/>riders picked up faster"] --> N["<b>North star</b><br/>numerator, denominator,<br/>window"]
    N --> R["<b>Guardrails</b><br/>what must not<br/>get worse"]
    R --> L["<b>Leading input</b><br/>what moves first"]
    L --> T["<b>The test</b><br/>how cause is settled"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class G lit
    class N,R,L,T known
```

---

## What is on the board when the day ends?

The finished concept board from the morning stays up all afternoon, with three lines written under it:

- Pay for completed peak trips per enrolled driver online at peak, per week.
- Guard it with the share of offers accepted (a floor between 0.46 and 0.78), the median rider wait and the top-up per completed trip.
- Paying for hours sent Rs 1.159 crore, 61 percent of the Rs 1.9 crore top-up, to driver-weeks that accepted fewer than half their offers.
