# Design system and build pipeline

## Palette

Light editorial. White ground, near-black ink, one warm accent used only
where it means something.

| Token | Hex | Used for |
|---|---|---|
| ground | `FFFFFF` | slide background |
| ink | `0F172A` | headings, primary text, table header fill |
| soft | `334155` | body text inside tables and panels |
| muted | `64748B` | lead lines under titles, captions |
| dim | `94A3B8` | column labels, page numbers, footers |
| rule | `E2E8F0` | hairline borders |
| panel | `F8FAFC` | quiet fills, alternating table rows |
| accent | `B45309` | the one accent: step numbers, key values, active nodes |
| accentSoft | `FEF3C7` | callout bands, highlighted cells, result panels |
| green | `047857` + `ECFDF5` | pass, correct, the right way |
| red | `B91C1C` + `FEF2F2` | fail, wrong, the wrong way |

Green and red carry meaning only. Never use them decoratively.

Dark slides (`ink` ground) bookend the deck: title and closing bridge, plus
section dividers on decks long enough to need them.

## Typography

- Headings: Georgia, 25 to 26pt bold, at `y 0.36`
- Lead line under the heading: Calibri 15.5pt in `muted`, at `y 1.03`
- Body and tables: Calibri, 12 to 14.5pt
- Values inside diagrams: monospace, so `Germany` and `DE` read as data
- Canvas: `LAYOUT_WIDE`, 13.333 x 7.5 inches
- Margins: left and right 0.7, content width 11.933, footer row at `y 6.95`

No accent line under a title. No decorative bars. No edge stripes.

## Slide kinds that carry a deck

Build these as named renderers and reuse them. A deck usually needs eight to
twelve of them.

| Kind | Shape |
|---|---|
| `title` | Dark. Eyebrow, title, deck identifier, the numbered questions the deck answers, one promise line |
| `bigImg` | Title, lead, one full-width diagram vertically centred in the space that remains |
| `definition` | Title, the definition in an accent band, one line after it, a diagram, then a formal-term note in a quiet panel |
| `defTable` | Title, lead, a three or four column table filling to a fixed bottom, an accent footer band at a fixed `y` |
| `quiz` | Three numbered question blocks, each with two or four lettered option chips |
| `check` / `checkAns` | Items with option chips, then an answer table with a per-item reason column and a callback band |
| `steps` | Four columns: step number, what you do, how to do it, the result in an accent panel. Six or seven rows |
| `twoCol` | Two headed columns of one-line panels, tinted green and amber, with a footer band |
| `ladder` | Three or four stacked rows, the last one accented, each with a label, a verdict and an explanation |
| `scenarios` | Two dark-headed columns of facts, then an ask band |
| `takeaways` | A small summary diagram, then numbered rule lines |
| `bridge` | Dark. The questions still open, then one closing line |

## Build pipeline

`pptxgenjs` for the deck, hand-written SVG for every diagram, `sharp` to
rasterise SVG to PNG at `density: 200`, inserted with the
`image/png;base64,` prefix.

Keep the slide content in a data module separate from the renderer. That makes
splicing additions trivial and keeps existing slides provably untouched:

```js
// content_plus.js
const base = require("./content");
const adds = require("./additions");   // [{ when: "before"|"after", anchor: "<exact title>", slide: {...} }]
const out = base.slice();
for (const a of adds) {
  const idx = out.findIndex((s) => s.title === a.anchor);
  if (idx === -1) throw new Error("anchor not found: " + a.anchor);
  out.splice(a.when === "before" ? idx : idx + 1, 0, a.slide);
}
module.exports = out;
```

## Gotchas that have cost real time

- **`addTable` `rowH` applies to the header row too.** A table's height is
  `rowH x (rows + 1)`. Computing `rowH = (bottom - y - headerHeight) / rows`
  overflows every time. Divide by `rows + 1`.
- **Put footer bands at a fixed `y`,** and cap the table's bottom above it.
  Rows grow when text wraps, so a footer positioned relative to the computed
  table end will collide.
- **Set `pres.layout` before adding any slide.** The default is 10 inches
  wide, not 13.3, and off-canvas coordinates are written rather than clamped.
- **Hex colours never carry `#` and never carry alpha.** Both corrupt the
  file.
- **`pptxgenjs` mutates option objects in place.** Build a fresh object for
  every `add*` call.
- **Em-dashes enter as `\u2014` escape sequences in build source.** A
  literal-character scan reports zero while the rendered file still shows
  them. Scan both forms, and scan the rendered output rather than the source.
- **SVG text does not wrap.** Split lines manually and check the widest
  string against the canvas width, or it clips silently.
- **Content near an SVG's bottom edge gets its descenders cut.** Leave at
  least 14px between the last baseline and the canvas height.
- **Speaker notes go in `slide.addNotes()`,** never in a text box.

## Rendering for visual QA

```bash
python3 /mnt/skills/public/pptx/scripts/office/soffice.py --headless --convert-to pdf deck.pptx
rm -f slide-*.jpg
pdftoppm -jpeg -r 120 deck.pdf slide
```

Then build contact sheets and look at every slide. Text overflow first, then
overlaps, then uneven gaps, then margins under 0.5 inches. Fix in the
generator and re-render.
