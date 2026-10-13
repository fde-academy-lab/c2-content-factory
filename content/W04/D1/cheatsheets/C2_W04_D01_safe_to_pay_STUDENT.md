# What makes a number safe to pay for?

Monday teaches six topics first, on examples whose numbers are invented, then applies them to a case. Illustrative case: the company is real, the situation and the data are synthetic, built for this class. Uber, Hyderabad: from 31 August 2026 an enrolled driver online through a whole peak window is guaranteed Rs 300 per peak online hour, with a top-up for the gap. Six weeks each side: peak online hours up 24 percent, trips up 3 percent, trips per peak online hour 1.90 to 1.58, offers accepted 0.86 to 0.73, median wait 4.8 to 4.6 minutes, top-up Rs 0 to Rs 1.9 crore. Data: `drivers`, `driver_weeks`, `zone_weeks`. Ask, by Friday: is it working, what should it pay for, is anyone gaming it? Caveats: monsoon's end, 140 new drivers, online means the app is open, three thin outer zones, drivers on two apps.

## Panel 1: Which six topics does Monday teach, and where does the case use them?

```mermaid
flowchart LR
    C1["<b>1 What to measure and why;<br/>the proxy test</b><br/>could it rise while<br/>the goal got worse?"]
    C2["<b>2 North-star and<br/>guardrail metrics</b><br/>one number to chase,<br/>others to guard it"]
    C3["<b>3 Leading against<br/>lagging indicators</b><br/>warns while you can act,<br/>or confirms afterwards"]
    C4["<b>4 Definitions: numerator,<br/>denominator, window,<br/>exclusions</b><br/>four lines make it computable"]
    C5["<b>5 Gaming, and definitions<br/>that resist it</b><br/>a receipt, a system clock,<br/>dated changes"]
    C6["<b>6 The metric<br/>definition artifact</b><br/>seven lines, one page"]
    U["<b>Uber, Hyderabad</b><br/>chapters 7 to 11<br/>apply all six"]
    C1 --> C2
    C2 --> C3
    C3 --> C6
    C1 --> C4
    C4 --> C5
    C5 --> C6
    C6 --> U
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef kalpa fill:#FFF7E6,stroke:#C98A00,color:#5C3D00
    class C1,C2,C3,C4,C5,C6 lit
    class U kalpa
```

**Crux:** Chapters 1 to 3 choose the number, chapters 4 and 5 write it so it cannot be gamed, and chapter 6 puts both on one page: canteen tokens 1.0 to 2.0 a plate, a pass rate 0.60 to 0.90 as licences fell to 0.36, 10.0 an over needed at over 10, five readings of one register, 50 marked against 40 confirmed (all invented).

## Panel 2: What does the finished board say about a number worth paying for?

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

**Crux:** Judge it by completed peak trips per enrolled driver online at peak, guarded by acceptance, the wait and top-up per trip; hours rose 24 percent as trips per hour fell from 1.90 to 1.58.

## Panel 3: What did six drivers do, counted by hand?

| Driver, zone | Hours, week of 10 Aug then 21 Sep | Trips, the same two weeks |
|---|---|---|
| A, Jubilee Hills | 10 then 11 | 21 then 22 |
| B, Banjara Hills | 9 then 10 | 17 then 18 |
| C, Gachibowli | 11 then 12 | 22 then 23 |
| D, Madhapur | 10 then 11 | 19 then 20 |
| E, Shamshabad | 10 then 16 | 18 then 3 |
| F, Rajendranagar | 10 then 14 | 17 then 2 |
| All six | 60 then 74, up 23 percent | 114 then 88, down 23 percent |

E and F keep shorter weeks than the idle tail's average of about 39 peak online hours a driver-week, which chapter 8's full data shows.

**Crux:** 114 / 60 = 1.90 and 88 / 74 = 1.19: add, then divide once. Two of six are in the idle tail against 15 percent of the city, which falls only to 1.58.

## Panel 4: What are the seven lines of a complete definition?

| Line | In plain words | The redesign |
|---|---|---|
| Numerator | What is counted | Peak trips completed, one per paying rider |
| Denominator | Divided by, count printed | Enrolled drivers online one peak hour or more |
| Window | The stretch of time | The calendar week |
| Exclusions | Left out, with why | Cancelled trips, test accounts, off-window trips |
| Does not reward | Behaviour paid nothing | Hours online, declines, a shrinking base |
| Guardrails | Must not get worse | Riders: accepted share over a floor, the wait by zone. Budget: top-up per trip |
| Gaming note | What each guardrail catches | Declines and cancels; lost supply; a runaway top-up |

**Crux:** The first four lines make a number computable; the last three make it hard to game. North star 35.76 to 35.89 trips per online driver-week.

## Panel 5: What is the proxy test?

Could a team hit this number while the thing it stands for got worse?

| Proposed number | How it rises badly | The guardrail |
|---|---|---|
| Peak online hours | Online in empty zones | Hours with no trip: 0.22 to 0.38 |
| Completed trips per driver | Short trips only | Offers accepted, over a floor |
| Enrolled drivers | Sign up, never drive | Share online at peak |

**Crux:** A guardrail is chosen by the gaming it catches; another growth count catches nothing.

## Panel 6: What did hours cost, and what would the redesign save?

Rs 1.9 crore bought 6,700 more trips, about Rs 2,836 each; **Rs 1.159 crore** of it went to weeks accepting under half their offers. Rule: the floor stays only for weeks accepting half, a cancel counted as a decline.

**Crux:** Saving Rs 92.7 lakh if a fifth of the idle top-up is still paid, Rs 58 lakh if half is: an assumption with a range, settled by a test.
