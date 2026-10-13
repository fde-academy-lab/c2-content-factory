# What goes on the board on Thursday, and in what order?

*Illustrative case: the company is real, the situation and the data are synthetic, built for this class. The gym and the college are invented.*

Zomato Gold, Chennai. The membership dashboard reads month-two retention flat at 38 percent from June
to September 2026 while every signup cohort falls with age, and since a new Android checkout shipped
on 14 September, members' add-to-cart to order on Android has fallen from 58 to 44 percent. The
membership lead asks, by Friday: is it a cohort problem or an everyone problem, which funnel stage
owns the loss, and what is fixed first?

**Who needs the answer.** The trainer, who draws these in order, and you, if you missed a drawing or
want to redraw the board from memory before Friday.

**The questions on the way.** Each heading below asks the question one drawing answers, in the order the drawings go up, and the last asks what stays on the board at the end.

---

## How do the day's five topics connect?

Goes up first and stays up all day. Each topic's node is lit when its chapter ends; the applied node
is lit as the case begins.

```mermaid
flowchart TB
    E["Weeks 1 and 2"]
    E -->|"W2 Thu · pivot_table,<br/>melt"| T1["1 Cohort construction<br/>SECTION 1"]
    E -->|"W1 Mon · a denominator<br/>for every rate"| T2["2 Funnel stages,<br/>drop-off, denominators<br/>SECTION 4"]
    E -->|"W1 Tue · like<br/>with like"| T3["3 Retention curves:<br/>shape and floor<br/>SECTION 2"]
    E -->|"W1 Thu · Simpson's<br/>reversal"| T4["4 Blended numbers<br/>against cohort truth<br/>SECTION 3"]
    E -->|"W1 Thu · claim,<br/>evidence, caveat, action"| T5["5 The fix-first decision<br/>and its evidence<br/>SECTION 8"]
    T1 --> C["Applied to: Zomato Gold,<br/>Chennai, SECTIONs 5 to 7<br/>and 9; Kalpa's Retail-Plus<br/>tier in the lab"]
    T2 --> C
    T3 --> C
    T4 --> C
    T5 --> C
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef unknown fill:#FFFFFF,stroke:#B8B2D6,color:#6B6690,stroke-dasharray:4 3
    classDef kalpa fill:#FFF7E6,stroke:#C98A00,color:#5C3D00
    class E known
    class T1,T2,T3,T4,T5 unknown
    class C kalpa
```

---

## Cohort construction: what does each batch keep at each age?

Goes up during SECTION 1, counted aloud from the gym's register, one row at a time.

```mermaid
flowchart LR
    R["<b>The register</b><br/>30 joiners, 10 a month"] --> L["<b>One row per member<br/>per month</b>"]
    L --> A["<b>Age</b><br/>month less the joining<br/>month; month zero out"]
    A --> T["<b>The triangle</b><br/>Jan 8, 6, 5, 5, 5<br/>Feb 7, 5, 3, 3<br/>Mar 6, 4, 3"]
    T --> S["<b>Same age</b><br/>age one: 80, 70, 60"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class R,L,A known
    class T,S lit
```

---

## Retention curves: shape and floor: where does each curve stop falling?

Goes up during SECTION 2, beside the triangle, so that each curve is read as a row of it.

```mermaid
flowchart LR
    J["<b>January</b><br/>80, 60, 50, 50, 50"] --> JF["<b>floor 50</b><br/>ages three and four agree"]
    F["<b>February</b><br/>70, 50, 30, 30"] --> FF["<b>floor 30</b><br/>read at 50 after age two:<br/>too early"]
    M["<b>March</b><br/>60, 40, 30"] --> MF["<b>no floor yet</b><br/>still falling"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef unknown fill:#FFFFFF,stroke:#B8B2D6,color:#6B6690,stroke-dasharray:4 3
    class J,F,M,JF,FF known
    class MF unknown
```

---

## Blended numbers against cohort truth: what is February's 50 made of?

Goes up during SECTION 3: the dashboard's one number first, then the two cohorts under it.

```mermaid
flowchart LR
    O["<b>Older members, 100</b><br/>50 then 40 percent"] --> B["<b>February's dashboard</b><br/>(40 + 210) / 500<br/>= 50 percent"]
    N["<b>January joiners, 400</b><br/>52.5 percent"] --> B
    B --> W["<b>Wrong</b><br/>(40 + 52.5) / 2 = 46.25,<br/>one vote each"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    class O,N known
    class B lit
    class W bad
```

---

## Funnel stages, drop-off, denominators: which step owns the college's loss?

Goes up during SECTION 4, each step divided aloud by the step before.

```mermaid
flowchart LR
    A["<b>Applied</b><br/>1,000"] -->|"80"| T["<b>Sat the test</b><br/>800"]
    T -->|"50, by design"| S["<b>Shortlisted</b><br/>400"]
    S -->|"75, was 90"| C["<b>Accepted</b><br/>300"]
    C -->|"80"| J["<b>Joined</b><br/>240"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    class A,T,S,J known
    class C bad
```

---

## Which causes could explain the Gold ticket, and what tests each?

Goes up after the break, as SECTION 5 opens the case: the groups' boards, gathered into one.

```mermaid
flowchart LR
    A["<b>1 Tracking</b><br/>did the count change?"] --> B["<b>2 Definition</b><br/>what is counted?"]
    B --> C["<b>3 Cohorts</b><br/>are newer members<br/>weaker?"]
    C --> D["<b>4 Everyone</b><br/>did all change<br/>at once?"]
    D --> E["<b>5 A stage</b><br/>which step lost<br/>members?"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    class A,B,C,D,E known
```

---

## What is Gold's 38 made of, and where is the loss?

Goes up through SECTIONs 6 and 7, under the five causes, one region at a time.

```mermaid
flowchart LR
    Q1["<b>Who entered when?</b><br/>May 3 of 4 · June 2 of 3<br/>sale 0 of 5"] --> Q2["<b>Who is still here?</b><br/>38 = weighted average;<br/>August outside the count"]
    Q2 --> Q3["<b>Where in the funnel?</b><br/>checkout start to order,<br/>72.5 to 55, Android members,<br/>from 14 September"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class Q1,Q2 known
    class Q3 lit
```

---

## What does a fix-first page carry?

Goes up in SECTION 8 on the college and is filled again for Gold in SECTION 9.

```mermaid
flowchart LR
    C["<b>The call</b><br/>one sentence"] --> E["<b>The evidence</b><br/>the step, its past,<br/>the group, the date,<br/>a comparator"]
    E --> K["<b>The cost</b><br/>in the business's unit,<br/>the assumption ranged"]
    K --> O["<b>The objection</b><br/>its true part<br/>conceded"]
    O --> R["<b>What would<br/>change it</b>"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    class C,E,K,O,R known
```

---

## What is on the board when the day ends?

The concept map with all five topics lit, the three regions answered under the five causes, and the
call for Gold in one line: fix the Android checkout's last step first, about 1,133 to 1,317 orders a
week; before another sale, work out whether the sale-week members, at 0.23 orders each in month one
against 0.61 for an organic member, pay back their discount.

```mermaid
flowchart LR
    A["<b>Where are we<br/>losing people?</b>"] --> Q1["<b>Who entered when?</b><br/>fix the signup month"]
    Q1 --> Q2["<b>Who is still here?</b><br/>38 = weighted average"]
    Q2 --> Q3["<b>Where in the funnel?</b><br/>checkout to order,<br/>Android members, 14 Sep"]
    Q3 -.- P["<b>Pitfalls</b><br/>blends, wrong denominators,<br/>stayers read as growth"]
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    class A,Q1,Q2 known
    class Q3 lit
    class P bad
```
