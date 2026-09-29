# Tomorrow: the number reaches the leadership deck

Ten minutes tonight, before Friday's Excel day.

> "Monday's growth review deck needs three things I can open on my laptop without a login: the
> revenue tree by segment for both quarters, the top-fifty protect list with a lookup so I can find
> any member by id, and one number on the front page with its trend. Nothing that needs Python. If a
> director changes an assumption in the room, the sheet must recalculate in front of them."
> Meera Raghavan's chief of staff, Kalpa Retail

## The words you will meet

| Word | What it means tomorrow | What you already know that it is like |
|---|---|---|
| PivotTable | Excel's grouped summary, which a director can slice live | `pivot_table` with `aggfunc="sum"`, dragged by hand |
| Slicer | A button that filters a pivot on one field | a `groupby` key you switch on and off |
| XLOOKUP | Finds a value by key in another range | a `merge` for one row at a time |
| Not-found argument | What XLOOKUP returns when the key is absent | `validate=`: the difference between a loud miss and a quiet wrong answer |
| Front-page number | One figure on a slide, with its denominator, period and comparison | Week 1's rule: every number leaves with its definition |

## One thing to think about

This week the number came from the warehouse, then pandas, and tomorrow it reaches Excel. Which of
the week's steps must never happen in a sheet: joining payments, cleaning duplicates, measuring
recency, choosing the tie rule, or presenting the number? Pick one and have a reason ready.

## The check for tonight

Open the CSV your escalated case wrote to `output/` and confirm it has 340 rows and a spend column
that adds to Rs 19,84,00,000. Bring it tomorrow; the Excel day is built on it.

## The line worth carrying in

The sheet presents the number and lets a director explore it; the warehouse is where the number is
born.
