# The shared helper module

One module per programme, imported by every notebook in every day pack. It exists so that a diagram, a check and a table look the same on Monday of Week 1 and on Friday of Week 15, and so that no notebook carries fifty lines of plumbing above its first idea.

## Where it lives, and the test that decides

A notebook runs with its own folder as the working directory, because that is what `jupyter nbconvert --execute` does and what a learner gets in a Codespace. Two placements satisfy that:

1. `scripts/c2kit.py`, reached by a relative `sys.path` insert documented at the top of every notebook.
2. A copy inside the day's `notebooks/`, named to the stem rule.

Pick one and prove it: `python3 scripts/verify.py content/W{ww}/D{d} --execute` has to pass. A helper that imports in your terminal and fails under nbconvert is not installed.

The documented import line looks like this, and the markdown cell above it says in one sentence what it does and why the path is relative:

```python
import sys, pathlib
sys.path.insert(0, str(pathlib.Path.cwd().parents[2] / "scripts"))
import c2kit
```

Count the `parents` index against the real depth of the notebook folder rather than copying it, and let the cold run confirm it.

## What the helper holds

### Loaders

One loader per dataset the day reads, each pointed at `../data/` and each returning plain Python objects: a list of dictionaries for records, a list of rows for a table. The loader is the only place a path string appears, so moving a data file breaks one line rather than twenty cells.

A loader never invents data. When the file is missing it raises with the path it looked for and the command that regenerates it.

### Checks

```python
c2kit.check(label, condition, detail="")
c2kit.check_summary()
```

`check` prints PASS or FAIL as HTML and returns the boolean. It never raises, because a failing check in front of sixty learners should show a red line and let the rest of the notebook run. `detail` carries the observed value, so a failure says what it saw rather than only that it failed.

`check_summary` prints the counts and returns them. Every notebook's final cell calls it.

Checks assert on shape. A count, a length, a type, the presence of a key, a reconciliation between two numbers. Never on a printed sentence, because the sentence will improve and the check will fail for no reason.

### Tables

```python
c2kit.table(headers, rows, caption="")
```

Renders an HTML table in the deck palette. Any result worth reading as a grid goes through it rather than through `print`, so a SUM cell and a profile printout look like the same programme.

### Traces

`show_trace` and a message viewer, built only for the days whose topic has a trace or a message sequence. A day with neither does not get an empty stub.

### Diagram builders

Every builder returns SVG and renders from a code cell, so the picture survives GitHub, Colab and a Codespace with no extension installed. Nine builders:

| Builder | Draws | Used for |
|---|---|---|
| `ladder` | The day's notebooks in order with the current one lit | The opening MAP cell of every notebook |
| `flow` | Steps left to right with one highlighted | A section MAP where the concept is a pipeline |
| `vflow` | The same top to bottom | A decision path or a long sequence |
| `stack` | Layers, bottom to top | A concept with layers rather than steps |
| `sequence` | Messages across named lanes | Anything with a caller and a callee |
| `tree` | A decision tree with the taken branch marked | A choice with more than two outcomes |
| `matrix` | A two-axis grid with cells filled | A choice with two independent dimensions |
| `decision_ladder` | Options in escalating order with the cut line marked | A choice that is really a threshold |
| `side_by_side` | Two diagrams composed horizontally | The opening MAP cell, and any before-and-after |

All nine take data, not markup. The caller passes a list of steps or a list of rows and the builder decides geometry, which is what keeps every diagram in the programme consistent and lets a later notebook draw a diagram of a run it just produced.

## The palette

The same values `scripts/build_deck.py` uses, so a diagram in a notebook and a diagram on a slide are recognisably the same drawing.

```
ink      #1C1C1A     text and strokes
muted    #5F6360     captions and secondary labels
accent   #2B4A7D     the one accent, used to mean something
tint     #E4ECF7     the lit node, the highlighted step
bg       #F7F7F5     the drawing ground
pass     #1F6F4A     a passing check
fail     #8A3D3D     a failing check
```

Important text is never grey. Muted is for captions only.

## Three rules for the module itself

1. No network. A notebook that fetches on run fails in a locked-down Codespace and fails in the verification gate.
2. No browser storage and no key. Nothing in a teaching notebook should need either.
3. No side effects on import. Importing the helper draws nothing, reads nothing and prints nothing. Every action is an explicit call from a cell the learner can see.
