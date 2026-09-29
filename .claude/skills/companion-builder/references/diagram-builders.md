# The diagram builders, in JavaScript

A companion draws with the JavaScript twins of the notebook helper's builders, so a learner meets
one visual language on the slide, in the notebook and on the page. The library is
`scripts/companion/c2kit.js`, its look is `scripts/companion/c2kit.css`, and the model page that uses
both is `content/W01/D1/demos/C2_W01_D01_revenue_tree_STUDENT.html`.

## How a page gets them

A page opens from disk with no network, so it cannot load a shared script. It carries two empty
marked blocks instead:

```html
<style data-c2kit></style>
<script data-c2kit></script>
```

`python3 scripts/build_companion.py <page>` fills both from the library, and
`python3 scripts/build_companion.py <day folder> --check` reports a page whose copy has fallen behind
it. The page's own script comes after the marked block and draws through `window.C2K`.

## The builders

| Call | Draws | Node shape |
|---|---|---|
| `C2K.flow(steps, lit, opts)` | Steps left to right, one lit | A step is a string; `\n` starts the second line |
| `C2K.vflow(steps, lit, opts)` | The same, top to bottom, with `opts.edges` labelling each arrow | As `flow` |
| `C2K.ladder(items, lit, opts)` | The day's stages numbered, one lit | As `flow` |
| `C2K.tree(node, opts)` | A decision tree, top down | `{label, kind, branches: [[edge label, child], ...]}` |
| `C2K.driverTree(node, opts)` | A total on the left, its drivers on the right | `{label, note, kind, children: [...]}` |
| `C2K.strip(values, opts)` | Every value as a dot on one axis, with `opts.markers` as named lines | `markers: [[label, value, kind], ...]` |
| `C2K.bridge(start, moves, opts)` | A starting total, the moves that change it, and where they land | `start: [label, value]`, `moves: [[label, change], ...]`, `opts.lo` raises the floor |
| `C2K.columns(categories, series, opts)` | Bars grouped by category, light to dark | `series: [[name, values], ...]` |
| `C2K.line(labels, series, opts)` | A trend, with a dashed plan line | `series: [[name, values, kind], ...]`, kind `plan`, `bad` or `good` |
| `C2K.sequence(lanes, messages, opts)` | Messages across named lanes, for a sequence popup | `messages: [[from, to, text], ...]` |
| `C2K.sideBySide(a, b, ...)` | Two or more drawings in one row | Any builder's result |

`C2K.draw(holder, svg)` replaces whatever a holder showed with a new drawing, which is how a walk step
or an experiment run redraws. `C2K.rupees(n)` writes Rs with Indian digit grouping. `opts.kinds`, or
a node's `kind`, sets a box's look by meaning: `plain`, `lit`, `known`, `unknown`, `bad` or `good`,
the same looks the notebook helper and the decks' Mermaid classes use.

A page that needs a builder the library lacks, such as the helper's `stack` or `matrix`, adds it to
`c2kit.js` beside the others and re-runs `build_companion.py`, so the next page has it too. A page
that hand-writes SVG for one diagram breaks the consistency the builders exist to hold.

## The palette

`C2K.colours` holds the values of `scripts/brand.py`, the orientation deck's palette: indigo
`#1A0F5C` for text and the lit node, violet `#5B3FD6` as the one accent, lavender tint `#EEEAFB` for a
plain node, green `#1F8A5B` for what holds and rose `#D63A6A` for what breaks. Muted `#6B6690` is for
captions only.

## Three rules for a builder call

1. **Pass data the page already holds.** A call that re-types the steps as string literals will
   disagree with the logic the first time either changes, and a simulator draws the run it produced.
2. **Light exactly one thing.** Two lit nodes means the diagram is answering two questions and needs
   to be two diagrams.
3. **Label the edges where the mechanism lives.** An arrow with no label says something happens; an
   arrow labelled `times orders per customer` says what.
