# The reference visual language (the Cohort 1 bar, extracted 21 Aug 2026)

Extracted directly from `Day1_Half1.pptx` and `Day1_Half2.pptx`, which Akash
named as the standard. The palette is identical to the one already in the
design system. **The difference is entirely in how it is applied.**

## The one rule that fixes 80% of it

**Accent is INK, not wallpaper.**

Measured across the two reference decks (75 slides):

| Use | Count |
|---|---|
| Amber as TEXT | 331 |
| Amber as FILL | 24 |
| Amber TINT (FEF3C7) as fill | 21 |

Amber appears as text roughly fourteen times more often than as a fill.
A rejected build had tinted bands on nearly every slide and coloured table
rows throughout. That is what "obnoxious palette" meant, not the hues.

## Banned in this style

- Bordered tables. The reference has almost no visible cell borders anywhere
- Coloured table row fills. Zero instances across 75 slides
- More than one tinted band per slide, and most slides have none
- Red and green as fills. They appear only as a thin rule plus a small-caps header
- Dark section-divider slides. Navigation is carried by the numbered kicker instead

## The type scale actually used

| Element | Font | Size |
|---|---|---|
| Slide title | Georgia bold | 25 to 28 |
| Title-slide headline | Georgia bold | 36 to 44 |
| Lead line under the title | Calibri italic | 10.5 to 11 |
| Body | Calibri | 9.5 to 12 |
| Dense secondary detail | Calibri | 9 |
| Small-caps kicker and micro-header | Calibri bold, charSpacing 1.5 to 2.6 | 7 to 8 |
| Code, formulas, traces | Consolas | 10 |
| Footer | Calibri | 7.5 |

Four greys carry the hierarchy: 0F172A ink, 334155 soft, 64748B muted,
94A3B8 dim. Typography does the work that colour was doing in the rejected build.

## The eight layout patterns, and when each is right

| Pattern | Shape | Use it for |
|---|---|---|
| **Column block** | N columns, each a small-caps header, a hairline under it, then stacked key/value pairs | Comparing 2 to 4 things across the same attributes. The workhorse |
| **Numbered rows** | Amber numeral, bold label, optional monospace sub-line, description on the right, hairline between | Lists of five where each item needs a sentence |
| **Borderless table** | Small-caps header row, one hairline under it, hairlines between rows, first column in amber | Reference data with three or four columns |
| **Definition quote** | Amber left rule, large Georgia italic | One formal definition, once per deck |
| **Pull quote** | Amber left rule, Calibri italic | The line you want carried out of the room |
| **Tinted band** | Amber tint fill with an amber left edge | The single most important sentence on the slide. Once per slide, at most |
| **Lettered options** | Grey square with an amber letter, text to the right | Quiz questions and sorting activities |
| **Thin bars** | Label, grey track, amber fill, italic note on the right | Proportions and comparisons. No axes, no gridlines |

## Slide skeleton

    kicker      08 · HOW MUCH OF THE WORK        (amber, small caps, letterspaced)
    title       Ninety out of a hundred is worse than none   (Georgia, an assertion)
    lead        one italic grey sentence
    ----------- content, starting around y 1.75
    footer      page number left, deck name right, 7.5pt dim

Numbered kickers (`01 ·`, `02 ·`) replace divider slides entirely and give
navigation on every slide for free.

## Whitespace

Content occupies roughly the top 75% of the slide. Bottom whitespace is
normal in the reference and should not be filled. A slide that reaches the
footer is too dense.
