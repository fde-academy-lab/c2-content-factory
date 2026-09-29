# The shared helper module

One module per programme, `scripts/c2kit.py`, imported by every notebook in every day pack. It exists
so that a diagram, a check and a table look the same on Monday of Week 1 and on Friday of Week 15,
and so that no notebook carries fifty lines of plumbing above its first idea. Its docstring is the
reference for what it holds; this page says how to use it.

## Where it lives, and the import every notebook carries

A notebook runs with its own folder as the working directory, because that is what `nbclient`,
`jupyter nbconvert --execute` and a learner's Codespace all do. The import walks up from there until
it finds `scripts/c2kit.py`, so it works at any folder depth without counting parents:

```python
import sys, pathlib
here = pathlib.Path.cwd()
for parent in [here, *here.parents]:
    if (parent / "scripts" / "c2kit.py").exists():
        sys.path.insert(0, str(parent / "scripts")); break
import c2kit as kit
```

The markdown cell above it says in one sentence what it does. `scripts/nb_make.py` carries the same
block as `SETUP`, assembles a notebook from cells and executes it in its own folder, and
`python3 scripts/verify.py content/W{ww}/D{d} --execute` proves the cold run.

## What the helper holds

### Loaders

`kit.load_records(name)` reads a generated Python literal from the day's `data/` folder as a list of
dictionaries; `load_csv`, `load_json` and `read_text` read the other forms, and `sql` and
`sql_table` query the Postgres warehouse from the days that have one. The loader is the only place a
file name appears, and a missing file raises with the path it looked for and the command that
regenerates it. No notebook pastes records into a cell.

### Checks

```python
kit.check(label, condition, detail="")
kit.check_summary()
```

`check` prints PASS or FAIL and never raises, because a failing check in front of sixty learners
should show a red line and let the rest of the notebook run. `detail` carries the observed value.
`check_summary` prints the totals, and every notebook's last cell calls it. Checks assert on shape:
a count, a length, a type, the presence of a key, a reconciliation between two numbers.

### A failure staged on purpose

```python
with kit.expect_error() as err:
    revenue += order["amount"]
kit.check("the loop stopped on a type error", err.name == "TypeError", err.message)
```

The block's error is caught and shown the way Jupyter prints its last line, with the line that
raised it, and `err.name`, `err.message` and `err.line` stay available to the checks. A block that
runs clean says so, which is how a fix shows up. The markdown under it quotes the full traceback a
learner sees without the `with` line, as a text fence.

### Tables, numbers and traces

`kit.table(headers, rows, caption)` sets any grid the way the deck sets its tables, with an indigo
head, banded rows and numbers aligned right. `kit.stats(items)` is the deck's row of big numbers.
`kit.rupees(n)` writes Rs with Indian digit grouping. `show_trace` and `show_messages` serve the days
whose topic has a trace or a message exchange.

### Diagram builders

Every builder takes data rather than markup, returns SVG and renders from a code cell as an SVG
image output, so the picture saves into the notebook and shows in every notebook viewer. A node's look comes from its `kind`: `plain`,
`lit` for the current step, `known`, `unknown` with a dashed edge, `bad` in rose and `good` in green.
These are the same looks the decks' Mermaid classes and the companion's builders use.

| Builder | Draws | Used for |
|---|---|---|
| `ladder` | The day's notebooks in order with the current one lit | The opening MAP cell |
| `flow`, `vflow` | Steps left to right, or top to bottom, with one lit | A section MAP, a decision path |
| `stack` | Layers, bottom to top | A concept with layers rather than steps |
| `sequence` | Messages across named lanes | Anything with a caller and a callee |
| `tree` | A decision tree with the taken branch marked | A choice with more than two outcomes |
| `driver_tree` | A total on the left, what multiplies into it on the right | A metric broken into its drivers |
| `equation` | A formula as boxes and operators | A relation worth seeing whole |
| `strip` | Every value as a dot on one axis, with any line named, such as the mean and the median | A distribution, and what one value does to a mean |
| `columns` | Vertical bars grouped by category, one per series, light to dark | Q1 against Q2 by segment, any before and after across groups |
| `line` | Values over an ordered axis, with a dashed plan line | A trend, a running total against plan |
| `bridge` | A starting total, the moves that change it, and where they land | A reconciliation, a decomposition of a change, booked to collected |
| `bars` | Horizontal bars with their values | A comparison of a few totals |
| `matrix` | A two-axis grid with cells filled | A choice with two independent dimensions |
| `decision_ladder` | Options in order with the cut line marked | A choice that is a threshold |
| `side_by_side` | Two or more diagrams composed horizontally | The opening MAP cell, and any before and after |

## The palette

The helper reads its colours from `scripts/brand.py`, the orientation deck's palette, which the
decks and cheat sheets read too, so a tree in a notebook and the tree on the slide are the same
drawing. Indigo `#1A0F5C` carries text and the lit node, violet `#5B3FD6` is the one accent, lavender
tint `#EEEAFB` fills a plain node, green `#1F8A5B` marks a pass and rose `#D63A6A` a failure. A
notebook never restates a colour; it names a kind.

## Three rules for the module itself

1. No network. A notebook that fetches on run fails in a locked-down Codespace and in the gate.
2. No browser storage and no key. Nothing in a teaching notebook needs either.
3. No side effects on import. Importing the helper draws nothing, reads nothing and prints nothing.
