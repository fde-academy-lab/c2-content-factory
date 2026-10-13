# What should you bring to Thursday, when a retention number stays flat?

Week 4, read on Wednesday evening: about 10 minutes of reading and two checks to run, so that
Thursday can start on its ticket from the first minute.

---

## What does Thursday's ticket say?

> **Zomato Gold, Chennai, the membership and the app's order flow.** The membership dashboard reports
> month-two retention for Chennai as flat at 38 percent for the reporting months June, July, August
> and September 2026: the share of members two or more months past their signup month who ordered in
> the month. Each signup month's own group of members keeps fewer members as it ages, and each new
> month keeps fewer in its first month than the one before: January 2026, 58 percent; July, 49;
> August, 31. The August group, grown by a sale week, is 13,000 members, 2.6 times the 5,000 a month
> of January to July. On Monday 14 September 2026 a new checkout flow shipped on Android, and since
> then members' add-to-cart to order rate on Android fell from 58 to 44 percent. The data covers the
> 53,089 members who joined from January to September.
> The ask, due Friday: is it a problem of one signup month or of everyone, which step of the order
> flow owns the loss, and what should be fixed first?
>
> Illustrative case: the company is real, the situation and the data are synthetic, built for this
> class.

```mermaid
flowchart LR
    D["<b>The dashboard</b><br/>38 percent, flat<br/>June to September"] --> Q{"<b>Which reading?</b>"}
    Q --> A["<b>One signup month</b><br/>August, 31 percent"]
    Q --> B["<b>Everyone</b><br/>58, then 49"]
    Q --> C["<b>One step of the flow</b><br/>Android, 58 to 44"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef unknown fill:#FFFFFF,stroke:#B8B2D6,color:#6B6690,stroke-dasharray:4 3
    class D known
    class A,B,C unknown
```

On Thursday you answer the membership lead, who wants one cause and one fix with the evidence.

---

## Which five topics will Thursday teach, in the curriculum's words?

Thursday's curriculum row names these five topics, in this order. Read the list once tonight and
notice which words you already half know; nothing here is taught yet.

1. Cohort construction
2. Funnel stages, drop-off, denominators
3. Retention curves: shape and floor
4. Blended numbers against cohort truth
5. The fix-first decision and its evidence

---

## Which words will Thursday use that you may not know yet?

Write what you think each one means tonight, from memory, in the right-hand column. Thursday's first
minutes assume you have tried, and a word you leave blank is the one to listen for in the room.

| Term | When Thursday uses it | What you think it means tonight |
|---|---|---|
| Cohort | The members who signed up in the same month are followed together. | |
| Retention | The ticket's flat number is a share of members still ordering. | |
| Blended | The dashboard's 38 percent mixes members of every signup month old enough to be counted. | |
| Funnel | The order flow runs from opening the app to an order placed, step by step. | |
| Month-one rate and month-two retention | The ticket sets each signup month's month-one rate beside the dashboard's month-two number; they are different measures. | |
| Add-to-cart to order rate | The step of the order flow the Android release touched. | |

---

## Which one question should you think about tonight?

Today the strip's click-through fell while every part of it held, because milk's share of the slots
grew. Thursday's number does the opposite: it holds while each signup month keeps fewer members than
the month before.

How could a number made of shrinking groups stay flat? Bring your answer as one sentence, since you
will be asked for it.

---

## What should you check in your Codespace tonight?

Nothing needs installing, and each check takes under five minutes.

1. Run Restart and Run All on Wednesday's eleven notebooks, 01 to 11. Each ends on its checks
   passing, and if one does not, post its last error line in the cohort channel before the session.
2. Save your take-home notebook with its outputs showing, since a notebook that ran but was not saved
   looks empty to everyone else.

---

## Which line is worth carrying into Thursday?

> Wednesday's 3.8 percent fell while its parts held; Thursday's 38 percent holds while its parts fall.
