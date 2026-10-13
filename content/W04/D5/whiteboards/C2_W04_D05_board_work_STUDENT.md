# What goes on the board on Friday, and in what order?

*The chai stall is invented, as every number about it is. Illustrative case: the company is real, the
situation and the data are synthetic, built for this class.*

Friday teaches five topics on a chai stall at a hostel gate (invented), then uses them on Flipkart's
Lucknow fulfilment centre, where the planner books packer shifts for the eight festive weeks beginning
12 October to 30 November 2026, between a vendor's plus 22 percent and finance's plus 4.

**Who needs the answer.** The trainer, who draws these in order, and you, if you missed a drawing or
want to redraw the board from memory before Saturday.

**The questions on the way.** Each heading below asks the question one drawing answers, in the order
the drawings go up, and the last asks what stays on the board at the end.

---

## How do the five topics connect, and where does the case use them?

Goes up first and stays up all day. The five topics are lit as each chapter teaches them.

```mermaid
flowchart LR
    E["<b>Earlier weeks</b><br/>like with like;<br/>LAG; beyond chance"] -.-> T1
    T1["<b>Chapter 1: Trend and seasonality,</b><br/><b>read before modelling</b>"] --> T2["<b>Chapter 2: Naive, seasonal naive</b><br/><b>and drift baselines</b>"]
    T2 --> T3["<b>Chapter 3: Holding out; MAE and MAPE</b><br/><b>in the business's units</b>"]
    T3 --> T4["<b>Chapter 4: Beating the baseline;</b><br/><b>the vendor curve tested</b>"]
    T4 --> T5["<b>Chapter 4, second half: the good-enough</b><br/><b>call and the forecast note</b>"]
    T5 --> C["<b>The case</b><br/>Flipkart, Lucknow,<br/>chapters 5 to 7"]
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef kalpa fill:#FFF7E6,stroke:#C98A00,color:#5C3D00
    class T1,T2,T3,T4,T5 lit
    class E known
    class C kalpa
```

---

## Trend and seasonality, read before modelling: what does the invented stall's fortnight say?

Drawn during chapter 1, from the invented stall's first fourteen days.

```mermaid
flowchart LR
    A["<b>Monday 100, Sunday 60</b><br/>up 67 percent?"] --> B["<b>The beat</b><br/>Sunday is 0.6 of a Monday,<br/>every 7 days"]
    B --> C["<b>The trend</b><br/>Monday 110 a year later:<br/>up 10 percent"]
    C --> D["<b>The seasons</b><br/>exams about 1.4,<br/>Diwali week about 0.4"]
    D --> R["<b>The remainder</b><br/>a yearly copy misses by<br/>4.7 cups, typically"]
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    class A known
    class B,C,D,R lit
```

---

## Naive, seasonal naive and drift baselines: what does each rule say for next Sunday?

Drawn during chapter 2. The invented stall's last four days sold 98, 104, 101 and 103, and last
Sunday 61; next Sunday sold 60.

```mermaid
flowchart LR
    H["<b>The past</b><br/>98, 104, 101, 103;<br/>last Sunday 61"] --> N["<b>Naive</b><br/>the last value: 103"]
    H --> D["<b>Drift</b><br/>the four days' line<br/>extended: about 104.7"]
    H --> S["<b>Seasonal naive</b><br/>one season back: 61"]
    N --> A["<b>Sold: 60</b><br/>misses 43, 44.7 and 1"]
    D --> A
    S --> A
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    class H known
    class S lit
```

---

## Holding out; MAE and MAPE in the business's units: how is a rule scored?

Drawn during chapter 3, on the invented stall's fourteen days, the last three hidden.

```mermaid
flowchart LR
    O["<b>Hide the latest</b><br/>days 12 to 14,<br/>origin day 11"] --> F["<b>Forecast</b><br/>naive: 100 each"]
    F --> M["<b>Misses</b><br/>-10, +5 and 0"]
    M --> S["<b>Score</b><br/>MAE 5.0 cups;<br/>MAPE 4.8 percent"]
    S --> L["<b>Lean and price</b><br/>-1.7 cups, low;<br/>Rs 150"]
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class O,F,M,S,L lit
```

---

## Beating the baseline, the good-enough call and the note: when does a forecast earn trust?

Drawn during chapter 4.

```mermaid
flowchart LR
    F["<b>Fit</b><br/>the curve: error 0<br/>on four days"] --> X["<b>Forecast</b><br/>says 168,<br/>day 5 sold 102"]
    X --> B["<b>The baseline race</b><br/>seasonal naive 4.0<br/>against the mean's 12.4"]
    B --> G["<b>Good enough</b><br/>the same cans as a perfect<br/>forecast: better is worth nothing"]
    G --> N["<b>The note</b><br/>number, method,<br/>error bar, what breaks it"]
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    class F,X known
    class B,G,N lit
```

---

## The case: where is Flipkart's peak, and which rule wins on hidden weeks?

Drawn across chapters 5, 6 and 7.

```mermaid
flowchart LR
    P["<b>The peak</b><br/>two weeks before<br/>Diwali's week, both years"] --> C["<b>The calendar copy</b><br/>lands it a week late<br/>in 2025"]
    C --> H["<b>Thirteen hidden weeks</b><br/>festival-aligned 6,615;<br/>house bot 9,831"]
    C --> B25["<b>2025's festival, no growth</b><br/>festival-aligned 10,575;<br/>house bot 58,250"]
    H --> V["<b>The vendor</b><br/>fits within 1.4 percent,<br/>misses by 16,400"]
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class P,C,H,V,B25 lit
```

![The thirteen hidden weeks revealed: the house bot's and the vendor's average miss](C2_W04_D05_holdout_reveal_last_STUDENT.png)

Its animation, `C2_W04_D05_holdout_reveal_STUDENT.gif`, reveals the hidden weeks one at a time, from
`C2_W04_D05_holdout_reveal_first_STUDENT.png` to the still above: the vendor leads in week 1, 3,700
to 12,300, and trails by week 13, 16,400 to 9,831.

---

## What is on the board when the day ends?

The concept map with all five topics lit, and the plan beside it.

```mermaid
flowchart LR
    R["<b>The rule</b><br/>beat the bot on<br/>hidden weeks"] --> PL["<b>The plan</b><br/>19,760 packer shifts;<br/>3,625 in the week<br/>of 19 October"]
    PL --> E["<b>The error bar</b><br/>typically 6,615 a week:<br/>about Rs 35,800 high,<br/>Rs 1.65 lakh low;<br/>3,413 to 3,906 shifts<br/>at the peak"]
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class R,PL,E lit
```
