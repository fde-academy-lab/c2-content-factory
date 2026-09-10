# The diagram builders, ported to JavaScript

The companion draws with the same nine builders the notebook helper uses, so a learner meets one visual language across the slide, the notebook and the page. The Python versions live in `scripts/c2kit.py`; these are their JavaScript twins, and they take the same arguments in the same order.

## The nine

| Builder | Signature | Draws |
|---|---|---|
| `ladder` | `ladder(items, lit)` | The day's notebooks or stages in order, with one lit |
| `flow` | `flow(steps, lit)` | Steps left to right, with one highlighted |
| `vflow` | `vflow(steps, lit)` | The same, top to bottom |
| `stack` | `stack(layers, lit)` | Layers bottom to top |
| `sequence` | `sequence(lanes, messages)` | Messages across named lanes |
| `tree` | `tree(node, takenPath)` | A decision tree with the taken branch marked |
| `matrix` | `matrix(rowLabels, colLabels, cells)` | A two-axis grid with cells filled |
| `decisionLadder` | `decisionLadder(options, cutAt)` | Options in escalating order with the cut line marked |
| `sideBySide` | `sideBySide(a, b)` | Two diagrams composed horizontally |

Every one returns an SVG element, takes data rather than markup, and reads its colours from the palette below. A companion that hand-writes SVG for one diagram has broken the consistency the builders exist to hold.

## The palette

Identical to `scripts/build_deck.py` and the notebook helper.

```
--ink      #1C1C1A     text and strokes
--muted    #5F6360     captions and units
--accent   #2B4A7D     the one accent, used to mean something
--tint     #E4ECF7     the lit node, the highlighted step
--bg       #F7F7F5     the drawing ground
--pass     #1F6F4A     a passing state
--fail     #8A3D3D     a failing state
```

A dark-scheme block may re-map these under `prefers-color-scheme: dark`, and the mapping keeps the same meanings: accent stays the one accent, tint stays the lit state.

## Why the simulator needs them

A simulator produces a run that nobody wrote in advance, so its diagram cannot be hand-authored. `sequence(lanes, messages)` takes the messages the run actually produced and draws them, which is the whole reason the builders take data. Any page that generates a run draws that run rather than showing a fixed picture of a typical one.

## Three rules for a builder call

1. **Pass data the page already holds.** A builder call that re-types the steps as string literals will disagree with the logic the first time either changes.
2. **Light exactly one thing.** Two lit nodes means the diagram is answering two questions and needs to be two diagrams.
3. **Label the edges where the mechanism lives.** An arrow with no label says something happens. An arrow labelled `converts, or rejects with a reason` says what.
