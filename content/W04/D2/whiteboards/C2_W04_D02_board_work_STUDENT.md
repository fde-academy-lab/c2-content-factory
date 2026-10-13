# What goes on the board on Tuesday, and in what order?

*Ramesh's kirana shop, Gulmohar Secondary School and the campus canteen are invented, as every number
about them is. Illustrative case: the company is real, the situation and the data are synthetic,
built for this class.*

Tuesday teaches five topics on invented examples, then uses them on Uber's peak-hour earnings
guarantee in Hyderabad, where gross bookings per peak online hour fell from Rs 314 to Rs 260 at a fare
that held at Rs 165, and the city head has one slide and five minutes at Thursday's review.

**Who needs the answer.** The trainer, who draws these in order, and you, if you missed a drawing or
want to redraw the board from memory before Saturday.

**The questions on the way.** Each heading below asks the question one drawing answers, in the order
the drawings go up, and the last asks what stays on the board at the end.

---

## How do the five topics connect, and where does the case use them?

Goes up first, at S4, and stays up all day. Each topic's box is lit as its chapter closes.

```mermaid
flowchart LR
    K["<b>Already in the room</b><br/>the four-part note;<br/>a rate names its<br/>denominator; Monday's<br/>metric"] -.-> T1
    T1["<b>Chapter 1: The one-slide answer:</b><br/><b>claim, evidence, caveat, action</b>"] --> T2["<b>Chapter 2: What to leave out,</b><br/><b>and the appendix</b>"]
    T2 --> T3["<b>Chapter 3: Defending under challenge:</b><br/><b>restate, answer, concede,</b><br/><b>what would change your mind</b>"]
    T3 --> T4["<b>Chapter 6: The guesstimate:</b><br/><b>clarify, map, calculate, validate</b>"]
    T4 --> T5["<b>Chapter 7: The AI-free</b><br/><b>written business case</b>"]
    T5 --> C["<b>The case</b><br/>Uber, Hyderabad,<br/>chapters 4, 5 and 8 to 10"]
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef kalpa fill:#FFF7E6,stroke:#C98A00,color:#5C3D00
    class T1,T2,T3,T4,T5 lit
    class K known
    class C kalpa
```

---

## The one-slide answer: what do the invented shop's two months say, and what does the slide carry?

Drawn during chapter 1, from Ramesh's shop (invented): 10 hours a day in September, 12 in October.

```mermaid
flowchart LR
    A["<b>Sales a day</b><br/>Rs 11,900 to Rs 12,600:<br/>up 5.9 percent"] --> D["<b>Which unit does</b><br/><b>the decision buy?</b><br/>hours"]
    B["<b>Sales an hour</b><br/>Rs 1,190 to Rs 1,050:<br/>down 11.8 percent"] --> D
    C["<b>Sales a customer</b><br/>Rs 100 in both"] --> D
    D --> S["<b>The slide</b><br/>1 claim, 2 evidence,<br/>3 caveat, 4 action"]
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    class A,B,C known
    class D,S lit
```

---

## What to leave out, and the appendix: where does each element go?

Drawn during chapter 2. The three questions, asked of each of the draft's eight elements.

```mermaid
flowchart LR
    E["<b>an element</b>"] --> Q1{"does the claim<br/>need it?"}
    Q1 -->|"yes"| S["<b>the slide</b>"]
    Q1 -->|"no"| Q2{"will a named<br/>person ask?"}
    Q2 -->|"yes"| P["<b>that person's page</b><br/>headed by their question"]
    Q2 -->|"no"| X["<b>it leaves</b>"]
    V["<b>the caveat</b>"] -->|"always"| S
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    class E,Q1,Q2,P known
    class S lit
    class X,V bad
```

---

## Defending under challenge: what does a full defence of the sports teacher's objection sound like?

Drawn during chapter 3, at Gulmohar Secondary School (invented).

```mermaid
flowchart LR
    R["<b>1. Restate</b><br/>attendance rose because<br/>the exams began"] --> A["<b>2. Answer</b><br/>weeks 3 to 5: 4.7 points<br/>above last year's"]
    A --> C["<b>3. Concede</b><br/>exam weeks run about<br/>8 points higher, both years"]
    C --> M["<b>4. Change my mind</b><br/>the same rise at a school<br/>with the old timetable"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class R,A,C known
    class M lit
```

---

## Which number carries Uber's slide, and what goes behind it?

Drawn during chapters 4 and 5. The slide in its four parts, with one appendix page per role.

```mermaid
flowchart TD
    S["<b>The slide</b><br/>the scheme pays for idle hours:<br/>Rs 314 to Rs 260 per peak online hour"]
    A1["<b>Driver operations asks</b><br/>what happens to the<br/>drivers who accept?"]
    A2["<b>Marketing asks</b><br/>do the 140 new drivers<br/>lose out?"]
    A3["<b>Finance asks</b><br/>how much of the fall<br/>is the season?"]
    S --> A1
    S --> A2
    S --> A3
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    class S lit
    class A1,A2,A3 known
```

---

## The guesstimate: how big is the invented canteen's weekday, and is it sane?

Drawn during chapter 6. Under it, three words stay up all afternoon: unit, period, definition.

```mermaid
flowchart LR
    C["<b>1. Clarify</b><br/>one canteen, one weekday,<br/>cups of tea"] --> M["<b>2. Map</b><br/>students x share who buy<br/>x cups each"]
    M --> L["<b>3. Calculate</b><br/>3,000, then 1,350,<br/>then 2,700 cups"]
    L --> V["<b>4. Validate</b><br/>the till: 2,340,<br/>so revisit the share"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class C,M,L known
    class V lit
```

---

## How many drivers must be online at Uber's evening peak?

Drawn during chapter 8, leaf by leaf, each value said aloud with its range.

```mermaid
flowchart TD
    D["<b>Drivers online at the peak</b><br/>about 5,700; checked:<br/>about 5,000 to 5,700"]
    T["<b>Trips to serve an hour</b><br/>about 8,330"]
    P["<b>Trips per online driver-hour</b><br/>2.4 x (1 - 0.30) = 1.68"]
    B["<b>Buffer</b><br/>1.15"]
    D --> T
    D --> P
    D --> B
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    class D lit
    class T,P,B known
```

---

## The AI-free written business case: what does a page carry, sentence by sentence?

Drawn during chapter 7, on Ramesh's page (invented), and left up for chapter 9's page to the city
head.

```mermaid
flowchart LR
    S1["<b>First</b><br/>the claim, with<br/>what to do and why"] --> S2["<b>Second</b><br/>one number, what it<br/>is divided by"]
    S2 --> S3["<b>Third</b><br/>the caveat"]
    S3 --> S4["<b>Last</b><br/>the action, its cost,<br/>who signs"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class S1,S2,S3 known
    class S4 lit
```

---

## What stays on the board at the end of the day?

The concept map with all five boxes lit, the four steps with unit, period and definition beneath them,
and the day's sentence from S93: the scheme is paying for online hours that carry no trips, Rs 314 to
Rs 260 per peak online hour at a flat Rs 165 fare; part of it may be the monsoon; test paying per
completed peak trip with an acceptance floor; and at the evening peak the city needs about 5,000 to
5,700 drivers online.
