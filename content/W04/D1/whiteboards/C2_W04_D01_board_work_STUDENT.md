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

## Which six topics does Monday teach, and how do they join?

Goes up first, before anything else, and stays up all day. The six boxes are the curriculum row's
six topics in its order; each concept chapter lights its own box when it closes, and the case node
fills after the break.

```mermaid
flowchart TD
    E["<b>Weeks 1 to 3</b><br/>numerator and denominator,<br/>like with like, the grain"]
    C1["<b>1. What to measure and why;<br/>the proxy test</b>"]
    C2["<b>2. North-star and<br/>guardrail metrics</b>"]
    C3["<b>3. Leading against<br/>lagging indicators</b>"]
    C4["<b>4. Definitions: numerator,<br/>denominator, window, exclusions</b>"]
    C5["<b>5. Gaming, and definitions<br/>that resist it</b>"]
    C6["<b>6. The metric definition<br/>artifact</b>"]
    U["<b>Applied to: Uber, Hyderabad</b><br/>chapters 7 to 11"]
    E -.-> C1
    E -.-> C4
    C1 --> C2
    C2 --> C3
    C1 --> C4
    C4 --> C5
    C3 --> C6
    C5 --> C6
    C6 --> U
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef unknown fill:#FFFFFF,stroke:#B8B2D6,color:#6B6690,stroke-dasharray:4 3
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    classDef kalpa fill:#FFF7E6,stroke:#C98A00,color:#5C3D00
    class C1,C2,C3,C4,C5,C6 lit
    class E known
    class U kalpa
```

---

## Where does today's ticket sit in the week?

Goes up second, beside the six topics. Monday is lit; the other days stay dashed until they come.

```mermaid
flowchart TD
    C["<b>One number, five tickets</b><br/>four companies, one method a day"]
    M["<b>Mon: Uber, Hyderabad</b><br/>is the number right?"]
    T["<b>Tue: Uber, Hyderabad</b><br/>one slide, one estimate"]
    W["<b>Wed: Instamart, Pune</b><br/>what goes with what?"]
    H["<b>Thu: Zomato Gold, Chennai</b><br/>who leaves, and where?"]
    F["<b>Fri: Flipkart, Lucknow</b><br/>how much is coming?"]
    S["<b>Sat: does it travel?</b>"]
    K1["Kalpa: reorders per member"]
    K3["Kalpa: the Rs 199 charger"]
    K4["Kalpa: Retail-Plus"]
    K5["Kalpa: 24 months"]
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

## What happens to a token once servers are paid per token?

Chapter 1's canteen, invented numbers: tokens double from 200 to 400 a day while plates stay at 200.

```mermaid
flowchart LR
    G["<b>What the canteen wants</b><br/>plates served to hungry diners"] --> P["<b>What it pays servers for</b><br/>tokens handed out"]
    P --> C["<b>What a server can do</b><br/>print two tokens per plate"]
    C --> N["<b>What the number says</b><br/>tokens 200 to 400 a day"]
    C --> D["<b>What diners see</b><br/>plates stay at 200"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    class G,P,N known
    class C,D bad
```

---

## Why did a pass rate rise while licences fell?

Chapter 2's driving school, invented numbers: the hoarding's rate times the share who took the test
gives licences per learner who enrolled.

```mermaid
flowchart LR
    R["<b>The hoarding's rate</b><br/>passed / took the test<br/>0.60 to 0.90"] --> N["<b>The north star</b><br/>licences per learner enrolled<br/>0.60 to 0.36, which is 0.90 x 0.40"]
    T["<b>The guardrail</b><br/>took the test / enrolled<br/>1.00 to 0.40"] --> N
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef unknown fill:#FFFFFF,stroke:#B8B2D6,color:#6B6690,stroke-dasharray:4 3
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    classDef kalpa fill:#FFF7E6,stroke:#C98A00,color:#5C3D00
    class R bad
    class T known
    class N lit
```

---

## When does a chase first look lost?

Chapter 3's chase, invented numbers: the runs an over needed, written after each mark, against the
result.

```mermaid
flowchart LR
    O0["<b>Start</b><br/>160 / 20 = 8.0"] --> O5["<b>After over 5</b><br/>130 / 15 = 8.7"] --> O10["<b>After over 10, 60 for 3</b><br/>100 / 10 = 10.0<br/>the warning: leading"] --> O20["<b>After over 20</b><br/>147, lost by 12<br/>the result: lagging"]
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef unknown fill:#FFFFFF,stroke:#B8B2D6,color:#6B6690,stroke-dasharray:4 3
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    classDef kalpa fill:#FFF7E6,stroke:#C98A00,color:#5C3D00
    class O0,O5 known
    class O10 lit
    class O20 bad
```

---

## Which line moved each reading of one register?

Chapter 4's register, invented numbers: one student's term, five honest readings.

```mermaid
flowchart TD
    R["<b>One register</b><br/>60 days: 10 holidays,<br/>40 present, 8 absent, 2 medical"]
    S["<b>The school's rule</b><br/>40 / 50 = 80.0"]
    D["<b>Denominator</b><br/>calendar days<br/>40 / 60 = 66.7"]
    E1["<b>Exclusions</b><br/>medical out of both<br/>40 / 48 = 83.3"]
    E2["<b>Exclusions</b><br/>medical counted present<br/>42 / 50 = 84.0"]
    W["<b>Window</b><br/>last 20 working days<br/>14 / 20 = 70.0"]
    R --> S
    R --> D
    R --> E1
    R --> E2
    R --> W
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef unknown fill:#FFFFFF,stroke:#B8B2D6,color:#6B6690,stroke-dasharray:4 3
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    classDef kalpa fill:#FFF7E6,stroke:#C98A00,color:#5C3D00
    class R lit
    class S known
    class D,E1,E2,W unknown
```

---

## Which line stops each way of gaming?

Chapter 5's Balaji Kirana, invented numbers: 50 marked done, 40 confirmed by the customer's OTP.

```mermaid
flowchart LR
    G1["<b>The paid person counts</b><br/>the boy presses done"] --> L1["<b>A count the person served confirms</b><br/>the customer's OTP"]
    G2["<b>No receipt is needed</b><br/>done with no OTP"] --> L2["<b>A receipt in the numerator</b>"]
    G3["<b>The person timed starts the clock</b><br/>a typed dispatch time"] --> L3["<b>A clock the system starts</b><br/>the shop's bill"]
    G4["<b>A quiet change</b><br/>attempts start to count"] --> L4["<b>Changes dated on the page</b>"]
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef unknown fill:#FFFFFF,stroke:#B8B2D6,color:#6B6690,stroke-dasharray:4 3
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    classDef kalpa fill:#FFF7E6,stroke:#C98A00,color:#5C3D00
    class G1,G2,G3,G4 bad
    class L1,L2,L3,L4 known
```

---

## What are the seven lines of the page?

Chapter 6's skeleton: lines 1 to 4 make a number computable, lines 5 to 7 make it safe to pay for.
The weak page, "Deliveries, monthly, plus 20 percent", fills only lines 1 and 3.

```mermaid
flowchart LR
    N["<b>1 Numerator</b><br/>with its receipt"] --> D["<b>2 Denominator</b><br/>count printed"] --> W["<b>3 Window</b>"] --> E["<b>4 Exclusions</b><br/>each change dated"]
    E --> R["<b>5 Not rewarded</b>"] --> G["<b>6 Guardrails</b>"] --> M["<b>7 Gaming note</b>"]
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef unknown fill:#FFFFFF,stroke:#B8B2D6,color:#6B6690,stroke-dasharray:4 3
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    classDef kalpa fill:#FFF7E6,stroke:#C98A00,color:#5C3D00
    class N,D,W,E known
    class R,G,M lit
```

---

## Which four questions must a number answer before anyone is paid for it?

The case's board, drawn after the break (S57), empty but for its anchor, chapter 1's canteen.
Each case chapter fills one region.

```mermaid
flowchart LR
    Q["<b>What makes a number safe to pay for?</b>"]
    A["<b>Anchor: the canteen token</b><br/>tokens 200 to 400, plates stay 200<br/>(invented numbers)"]
    Q1["<b>What is it for?</b>"]
    Q2["<b>How could it rise while<br/>riders were served no better?</b>"]
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

## What does the board hold after chapter 7?

The first region filled: what the number is for, and the first pitfall.

```mermaid
flowchart LR
    Q["<b>What makes a number safe to pay for?</b>"]
    A["<b>Anchor: the canteen token</b><br/>tokens doubled, plates did not"]
    Q1["<b>What is it for?</b><br/>riders picked up faster;<br/>hours need no rider"]
    Q2["<b>How could it rise while<br/>riders were served no better?</b>"]
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

Two invented drivers: 40 trips over 50 hours is 0.80, while the average of their rates is 1.25, because Y's 40 slow hours count as one week, the same as X's 10. On the city, the average prints 1.71 against the true 1.58, so it shows a fall of 0.19 where the true fall is 0.32.

```mermaid
flowchart LR
    X["<b>Driver X</b><br/>2.0 trips an hour<br/>10 hours, 20 trips"] --> S["<b>Ratio of sums</b><br/>40 trips / 50 hours<br/>= 0.80"]
    Y["<b>Driver Y</b><br/>0.5 trips an hour<br/>40 hours, 20 trips"] --> S
    X --> M["<b>Average of rates</b><br/>(2.0 + 0.5) / 2 = 1.25"]
    Y --> M
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    class X,Y,S known
    class M bad
```

---

## What does the board hold after chapter 8?

The second region filled: how the number rose while riders were served no better.

```mermaid
flowchart LR
    Q["<b>What makes a number safe to pay for?</b>"]
    Q1["<b>What is it for?</b><br/>riders picked up faster"]
    Q2["<b>How could it rise while<br/>riders were served no better?</b><br/>online but idle, in thin zones:<br/>180 drivers, 15 percent"]
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

Built one region at a time: the north star, then each guardrail with the gaming it catches (two guard riders, the third guards the budget), then the two inputs, drawn dashed because the city team can move them this week. Read it as a seesaw: if the north star rises while a guardrail moves the wrong way, riders or the budget paid for the rise.

```mermaid
flowchart TD
    N["<b>North star</b><br/>completed peak trips per enrolled<br/>driver online at peak, per week"]
    G1["<b>Guardrail 1</b><br/>offers accepted over offers shown,<br/>at or above a floor"]
    G2["<b>Guardrail 2</b><br/>median rider wait at peak"]
    G3["<b>Guardrail 3, the budget</b><br/>top-up per completed trip"]
    L1["<b>Input</b><br/>enrolled drivers online<br/>in the first peak hour"]
    L2["<b>Input</b><br/>rider requests per online<br/>hour, by zone"]
    N --- G1
    N --- G2
    N --- G3
    L1 -.-> N
    L2 -.-> N
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef input fill:#FFFFFF,stroke:#5B3FD6,color:#1A0F5C,stroke-dasharray:4 3
    class N lit
    class G1,G2,G3 known
    class L1,L2 input
```

---

## What makes a number safe to pay for, now that the board is finished?

The finished case board, which is panel two of the cheat sheet.

```mermaid
flowchart LR
    Q["<b>Safe to pay for?</b>"]
    Q1["<b>What is it for?</b><br/>riders picked up faster"]
    Q2["<b>Can it rise badly?</b><br/>idle hours, thin zones"]
    Q3["<b>What stops that?</b><br/>north star and guardrails"]
    S1["<b>The tree</b><br/>north star and inputs"]
    S2["<b>The seesaw</b><br/>star up, guardrail down"]
    S3["<b>The window's start</b><br/>who starts the clock"]
    P1["<b>No usage condition</b><br/>Wells Fargo"]
    P2["<b>Units move numbers</b><br/>Delhi Metro"]
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

The afternoon's first drawing, chapter 10: write, price, defend, score.

```mermaid
flowchart LR
    W["<b>Write, 12 minutes</b><br/>the seven lines, three guardrails<br/>(two for riders), the gaming note"] --> P["<b>Price</b><br/>the saving, with its<br/>assumption stated"]
    P --> D["<b>Defend, about 7 minutes</b><br/>each role attacks once;<br/>a line must answer"]
    D --> S["<b>Score, 1 minute</b><br/>answered, conceded<br/>or lost"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class W,P,D known
    class S lit
```

---

## What structure does a hire-grade answer give the interviewer?

Chapter 11: goal, north star, guardrails, leading input, the test, the order a strong candidate says it aloud.

```mermaid
flowchart LR
    G["<b>Goal</b><br/>riders picked up faster"] --> N["<b>North star</b><br/>numerator, denominator,<br/>window"]
    N --> R["<b>Guardrails</b><br/>what must not<br/>get worse"]
    R --> L["<b>Leading input</b><br/>what moves first"]
    L --> T["<b>The test</b><br/>zones as the unit"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class G lit
    class N,R,L,T known
```

---

## What is on the board when the day ends?

The six topics' map stays up with every box lit, and the finished case board beside it, with three lines written under it:

- Pay for completed peak trips per enrolled driver online at peak, per week.
- Guard it with the share of offers accepted (a floor between 0.46 and 0.78), the median rider wait and the top-up per completed trip.
- Paying for hours sent Rs 1.159 crore, 61 percent of the Rs 1.9 crore top-up, to driver-weeks that accepted fewer than half their offers.
