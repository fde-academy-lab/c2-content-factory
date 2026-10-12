# Instamart Pune: the watch list, one zone, and a storm

Week 4, Day 3. Fallback.

Header: WEEK 4  ·  WEDNESDAY  ·  SWIGGY INSTAMART, PUNE  ·  FALLBACK

---

## S1. Four parts fill the 120 minutes
*What runs, for how long, and what does each part answer?*

| Part | Minutes | The question it answers |
|---|---|---|
| The watch-list trial | 35 | What must ice cream and chocolate sauce show before they take a slot? |
| One zone, one time band | 40 | Which pairs change rank when the strip is ranked for one slice of Pune? |
| The storm and the Pop-Tarts | 20 | Why is a sale that jumps before a storm no pair rule? |
| The second transcript | 25 | How do you answer a category manager who is sure the strip needs a redesign? |

```notes
LIVE, 2 minutes, on screen when the IITGN faculty session (tentative) cannot run in its slot. These
120 minutes extend the morning and teach nothing the block owns: no association rules as
probability, no algorithm that finds them. How long a trial must run before its answer can be
trusted is a sample-size question, parked by name for the faculty session (tentative). Transition:
the trial.
```

---

## SECTION 1: When may a thin pair take a slot?
*What must ice cream and chocolate sauce, lift 4.60 on 100 carts, show before they take a slot?*

```notes
LIVE, 35 minutes for the section. Groups design the trial; the TA plays the growth lead.
Transition: the four decisions.
```

---

## S2. A trial in two zones answers four decisions
*Where, for how long, against what, and what stops it?*

```cards
icon: map-pin | eyebrow: Where | title: Two zones alike | body: Two zones with similar carts and similar ice cream sales, one shown the pair and one left as it is. | tone: light
icon: calendar | eyebrow: How long | title: Fixed before it starts | body: The length is chosen before the first day and never stretched to chase a result. | tone: light
icon: target | eyebrow: Against what | title: The slot's own record | body: The pair must beat the click-through that slot drew in the same zones before the trial. | tone: light
icon: octagon-x | eyebrow: What stops it | title: A shock in either zone | body: A stock-out or a campaign in either zone voids the window and the trial restarts. | tone: dark
```

```notes
LIVE, 12 minutes. Each group fills the four cards for its own trial. Press on "fixed before it
starts": a trial watched daily and stopped when it looks good finds a winner by luck. The rule for
how long is the parked sample-size question. Transition: the first data request.
```

---

## S3. The trial's first need is a log split by zone
*Can today's `strip_log` measure a two-zone trial?*

```mermaid
flowchart LR
    L["<b>strip_log</b><br/>date, slot, anchor, suggestion<br/>no zone"] --> R["<b>The request</b><br/>the same log split by zone,<br/>weeks before and during"]
    C["<b>carts</b><br/>has a zone column"] --> R
    R --> T["<b>The trial</b><br/>can now be measured"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class L bad
    class C,R known
    class T lit
```

`strip_log` counts impressions, clicks and adds for the whole city; it has no zone column. A two-zone trial starts with a data request: the same log, split by zone, for the weeks before and during the trial.

```notes
LIVE, 8 minutes. This is a real analyst's moment: the method is ready and the data are not. Ask
the room to write the request in one sentence: which table, which new column, which dates.
Transition: the pass rule.
```

---

## S4. Pass only if the clicks and the rupees both hold
*What rule promotes the pair, and what keeps it on the watch list?*

```mermaid
flowchart LR
    T["<b>Trial zones</b><br/>the pair's slot<br/>click-through"] --> G["<b>Beats the slot's</b><br/>own record by a<br/>margin fixed in advance"]
    R["<b>Rupees</b><br/>adds x margin,<br/>less any discount"] --> G
    G --> P["<b>Promote</b><br/>city-wide"]
    G --> W["<b>Stays on the watch list</b><br/>if either fails"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    class T,R known
    class P lit
    class W bad
```

The pair is promoted when its slot beats the slot's own record by a margin set before the trial and its adds repay the slot in margin, after any bundle discount. If either fails, it stays on the watch list, which is what a watch list is for.

```notes
LIVE, 15 minutes. Groups present their pass rule in two sentences. The weak rule names only the
click-through; the strong rule names the rupees too. Transition: one zone, one time band.
```

---

## SECTION 2: What changes in one zone at one time?
*Which pairs change rank when the strip is ranked for one zone and one time band?*

```notes
LIVE, 40 minutes for the section, the row's after-class task done in class on notebook 03.
Transition: the code change.
```

---

## S5. The rerun is the same pairs table on fewer carts
*What changes in the code, and what changes in the reading?*

```python
slice_ids = carts.loc[(carts.zone == "Kothrud") & (carts.time_band == "morning"), "cart_id"]
part = baskets[slice_ids]                                  # the same sets, fewer carts
pair_count = Counter(p for b in part for p in combinations(sorted(b), 2))
floor = 0.01 * len(part)                                   # the floor is a share of the slice
```

The code changes in one line: which carts enter. The reading changes more: a slice holds fewer carts, so every pair rests on fewer of them, and a floor written as a share of the slice admits pairs on thinner ground.

```notes
LIVE, 8 minutes. Code along. Morning carts hold milk 80 percent of the time against 66 to 69 in the
other bands, so milk's pairs read slightly differently in the morning. Transition: the slices.
```

---

## S6. Each group takes one slice and reports on it
*Which slice does each group take, and what does it report?*

| Group | Slice | What the group reports |
|---|---|---|
| First and second | Kothrud, morning; Kothrud, evening | The top five pairs above the slice's floor, with support and lift |
| Third and fourth | Baner, morning; Hinjewadi, night | The same, and one pair that moved against the city ranking |
| Fifth and sixth | Hadapsar, week three; Hadapsar, week four | What happened to curd's pairs in the stock-out week |
| Any further group | A zone and band of the group's choice | The top five, and whether the city's three slots still lead |

```notes
LIVE, 25 minutes of group work. The fifth and sixth groups find the stock-out in their own slice: curd's pairs
vanish in week three and return in week four. The common stall is a pair below the slice's floor
that looks exciting; the hint is "how many carts is that lift resting on?". Transition: what the
slices say together.
```

---

## S7. What the slices agree on, and what they do not
*Which findings survive slicing, and which belong to one slice?*

```timeline
label: Survives | title: Milk's lift near one | body: In every band, bread with milk reads about 1.04.
label: Survives | title: The top two pairs | body: Chips with cold drink and coriander with green chillies lead every one of the six slices.
label: One slice only | title: Curd in Hadapsar, week three | body: Curd falls to 0.2 percent of carts, then 28 percent in week four: a stock-out, never a change in taste.
label: Thin ground | title: Hinjewadi at night, 649 carts | body: Three pairs resting on 7 to 10 carts each slip in above bread with butter.
```

```notes
LIVE, 7 minutes. Each group reads one line of its report against this list. Transition: a storm.
```

---

## SECTION 3: Why is a storm's sale no pair rule?
*Why is a sale that jumps before a storm a forecasting question rather than a pair rule?*

```notes
LIVE, 20 minutes for the section. Transition: Walmart's account.
```

---

## S8. Walmart stocked Pop-Tarts before Hurricane Frances
*What did Walmart see, and what did it do with it?*

```mermaid
flowchart LR
    C["<b>Hurricane Charley</b><br/>strawberry Pop-Tart sales<br/>rose about seven times"] --> S["<b>A pattern tied to an event</b><br/>demand jumps before a storm"]
    S --> F["<b>Hurricane Frances</b><br/>is forecast"]
    F --> M["<b>Walmart ships Pop-Tarts</b><br/>to stores in the storm's path"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class C,S,F known
    class M lit
```

Walmart's analysts had seen strawberry Pop-Tart sales rise about seven times before Hurricane Charley, so when Hurricane Frances was forecast the chain shipped extra Pop-Tarts to the stores in its path (OpenStax, checked 12 October 2026). The decision moved stock ahead of the storm; a wrong forecast would have left it on the wrong shelves.

```notes
LIVE, 10 minutes. Read the account. Ask: "is strawberry Pop-Tarts with a storm a pair, like chips
with cold drink?" Transition: the answer.
```

---

## S9. A pair holds weekly; a storm's sale needs a forecast
*Where does each kind of pattern belong this week?*

```timeline
label: A pair rule, today | title: Chips with cold drink | body: Found together in about 5 percent of carts, week after week.
label: An event, Friday | title: Pop-Tarts before a storm | body: Sales jump around a known future event, which a forecast with the event in it captures.
label: Friday's method | title: Line up the event | body: Compare each week with the same distance from the event, never the same calendar week.
label: What stays | title: Two events are two points | body: A pattern seen twice is thin ground, as a pair on 100 carts is.
```

```notes
LIVE, 10 minutes. Friday's ticket at Flipkart's Lucknow fulfilment centre takes this up with
Diwali as the event. Transition: the second transcript.
```

---

## SECTION 4: How do you answer a redesign?
*How do you answer a category manager who is sure the strip needs a new layout?*

```notes
LIVE, 25 minutes for the section: the dispute transcript read in pairs, then scored.
Transition: the three sentences.
```

---

## S10. Three sentences that sound right
*What does the category manager say, and which parts hold?*

> The click-through fell because shoppers buy differently after the monsoon. The strip needs a redesign; our team has mocked up a two-row layout that sits higher on the page. We can run it next week.

The first sentence names a cause the log can test. The second proposes a fix for a problem nobody has shown. The third is a test, which is the part worth keeping.

```notes
LIVE, 5 minutes. Pairs list what is partly right and what is unproven before the next slide.
Transition: the four moves.
```

---

## S11. The four moves, answered from the log
*How does the growth lead answer without dismissing the manager?*

```cards
icon: ear | eyebrow: Restate | title: Habits may have shifted | body: The monsoon ended inside the window, so a change in habits is possible. | tone: light
icon: chart-column | eyebrow: Answer | title: The fall sits in milk's slots | body: Milk slots clicked 1.2 percent; every other slot 6.4, up from 6.2 before the change. | tone: light
icon: handshake | eyebrow: Concede | title: Position matters | body: Slot 1 draws 8.2 percent against 5.4 for slot 3, so a layout is worth testing on its own. | tone: light
icon: refresh-cw | eyebrow: What would change it | title: If other slots fell too | body: Had the non-milk slots fallen with milk's, the habits story would lead. | tone: dark
```

```notes
LIVE, 10 minutes. Score each pair's answer on the four moves, 0 to 2 each. Transition: the one
chart to hand the manager.
```

---

## S12. The chart that settles the dispute
*Which picture answers "shoppers changed"?*

![Click-through by slot position: before the change, milk after, everything else after](../whiteboards/C2_W04_D03_ctr_by_slot_STUDENT.png)

In every slot, suggestions other than milk clicked as well after the change as before; milk clicked low in all three. Shoppers who had changed their habits would have stopped clicking everything. A new layout is worth a test of its own; it is not what fell.

```notes
LIVE, 7 minutes. The sentence to carry: "a redesign is worth testing; the ranking is what fell".
Transition: the close.
```

---

## S13. What the fallback leaves the room with
*What does the room keep from the four parts?*

```timeline
label: The trial | title: Four decisions before day one | body: Where, how long, against what, and what voids it.
label: The slices | title: Thin ground moves | body: The city's three slots survive; curd's dip belongs to one zone and week.
label: The storm | title: An event needs a forecast | body: Friday's question, with Diwali as the event.
label: The dispute | title: Four moves, one chart | body: The log settles what fell; a layout earns its own test.
```

```notes
LIVE, 1 minute. Say only that the faculty session (tentative) did not run today. Tomorrow's
pre-read ships tonight.
```
