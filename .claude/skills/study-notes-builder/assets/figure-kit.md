# Figure kit

Figures are hand-authored SVG. They are the reason the note reads as designed
rather than generated, and a stock flowchart undoes that in one glance.

## The palette

Set as CSS variables in `notes.css` and repeated inside every SVG, so a
programme rebrand is one line in each place.

| Role | Default | Used for |
|---|---|---|
| ink | `#161616` | All text, all structural lines |
| soft | `#4A4A4A` | Secondary labels |
| muted | `#8A8A8A` | Captions, axis labels, outlined-state text |
| rule | `#E2E2E2` | Hairlines, grid, outlined-state strokes |
| panel | `#F7F7F5` | The one light fill allowed per figure |
| accent | `#1E6B7A` or the programme brand | The one thing the figure is about |

The accent hex is repeated inside every SVG, so a programme rebrand means
changing it in `notes.css` and in each figure. `build_notes.py --brand` only
restyles the document chrome; it does not reach inside the SVG files.

**The one rule: accent is ink, not wallpaper.** It marks the element the figure
exists to point at, and nothing else. A figure with three accent fills has
pointed at nothing. Count them before shipping: one accent element per figure,
two at most.

No gradients, no drop shadows, no rounded-corner card stacks, no icon sets.
Greys carry the hierarchy that colour is often wrongly asked to carry.

## Geometry and type

- Author at 150 viewBox units per display inch. A figure sitting in a 6 inch
  text column is `viewBox="0 0 900 H"`.
- Text at 18 to 22 units for body labels, 26 to 30 for the figure's own
  headings, 15 to 16 for captions inside the figure. Below 14 units nothing is
  readable in print.
- Font family `Poppins, Helvetica, sans-serif` for labels, matching the note.
- Leave 40 units of padding inside the viewBox on every side.
- Arrowheads are drawn as an explicit `path` at the line end. Marker-end on a
  `line` element does not survive several SVG rasterisers.
- Every figure gets a caption below it in the markdown, as an italic paragraph
  starting with `Figure N.` The caption says what the figure shows and what to
  take from it, in two sentences. It never repeats the body text.

## Six recipes

**1. The terrain map.** Two bands of cells. Band A across the top as a row of
labelled rectangles, band B beneath as a narrower row. Three fill states from
`terrain-map.md`. Today's cells carry a 2 unit ink ring. Legend once per
cohort, in the first note only.

**2. The stage funnel.** Two or three stacked bars of decreasing width with
the count at each stage and the unit cost beside it. Use when something cheap
runs over everything and something expensive runs over the survivors.

**3. The comparison strip.** Two columns headed with what the work used to be
and what the work becomes, four to six rows, no borders, hairline between
rows only. This lands harder than a list of new features and it costs less
space.

**4. The decision gate.** Diamonds and boxes, but drawn properly: dead ends in
grey, the path the reader should take in accent, the question written inside
each diamond as a real question. Never a plain box chain with arrows.

**5. The bar with no axes.** Three to six horizontal bars, value printed at the
end of each bar, no gridlines, no y axis, category labels left aligned in ink.
Use a log scale or split the chart when one value is more than twenty times
another, because a linear scale hides the small ones.

**6. The state trace.** A horizontal row of steps with the running thread's
actual values printed under each one, so the reader watches one thing change.
This is the figure that carries the running thread and most notes want one.

## What not to draw

- A diagram that restates a sentence already on the page.
- Three boxes labelled with the three things a bulleted list already said.
- A circular arrow diagram used because the content had no shape of its own.
- Anything where the reader has to read the caption to find out what they are
  looking at.

If a figure cannot be described in one sentence starting with "this shows",
it is decoration and it comes out.
