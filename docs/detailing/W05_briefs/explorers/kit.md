# Week 5 explorers: the kit session

INTERNAL. The kit session runs first and alone. Five day sessions build only with what it ships,
so its API and its quality set the ceiling for the week. Read `common.md` beside this file first.

## What you ship

1. **The kit's two files.** `scripts/companion/w5kit.css` and `scripts/companion/w5kit.js` are new
   files. Leave `c2kit.css` and `c2kit.js` untouched, so the Week 1 to 4 pages do not move.
2. **`scripts/build_companion.py`, extended.**
   - A page carries the blocks `<style data-w5kit></style>`, `<script data-w5kit></script>` and
     `<script type="application/json" data-w5data="<path to the day's JSON>"></script>`. The
     script fills all three.
   - `--check` reports any page whose inlined copy is stale.
   - The c2kit behaviour is unchanged.
3. **`scripts/companion/W5KIT.md`.** The kit's manual for the day sessions:
   - the page template;
   - every component with its options and a minimal example;
   - the data-block protocol;
   - the route names;
   - the rules from `common.md` that the kit enforces.
4. **`scripts/companion/demo/w5kit_demo_INTERNAL.html`.** A stress page that runs every component.
   - Its data is labelled demo data.
   - It includes three stress scenes:
     - 8,238 dots falling into the four boxes of a confusion matrix as a threshold slider moves;
     - a five-fold rotation, with the scaler refitted inside each fold;
     - AUC shown as pairs ranked, one pair at a time.
   - It is not a learner file and lives outside `content/`.
5. **`scripts/html_sweep.py`, with a route walk.**
   - When a page carries the kit's nav, the sweep clicks each route in turn and sweeps the
     controls visible on that route.
   - It reports per route.
   - Before you change it, run it on every Week 1 to 4 day folder that has a `demos/` page and
     save the summary. After your change, every one of those folders must report the same
     result.
6. **`scripts/explorer_shots.py <page> <outdir>`.**
   - It screenshots every route of a kit page at 1366 by 768 and 390 by 844, using Playwright's
     Chromium at `/opt/pw-browsers`.
   - It prints the files it wrote and any console error.

## What the kit holds

| Component | What it does |
|---|---|
| App shell | A top bar with the day and its question, and a nav of the routes with an icon each. A progress rail shows which routes have been visited, with previous and next. Routes live in the hash (`#story`, `#map`, `#p1` and so on). Arrow keys step, number keys jump, and a presenter-mode toggle enlarges the type. Reduced motion is honoured, and scrolling is instant. |
| Page template | Has four parts: (1) a kicker carrying the row's subtopic verbatim; (2) the heading question; (3) the prediction card, then the stage, the controls row and the readout panel; (4) the rule card, named last with its "flips when" line. A footer says "where you met it": the deck chapter and the notebook name. |
| Prediction card | Takes a choice, a number or a direction. It is committed with one button and revealed with the reason. It never disables anything else on the page. |
| Timeline player | Steps through keyframes, each with a caption, using play, pause, step and a scrub bar. Each frame writes its readout. With reduced motion it jumps to the last frame. |
| Charts | Axes, histogram, line, scatter, bars, the 2 by 2 matrix and a dot grid of countable marks, with eased transitions. Each chart writes the numbers it shows into the DOM. A canvas dot cloud handles about 10,000 points with transitions. |
| Concept map | Nodes in three kinds (today, earlier and later), with labelled edges. The day's path animates in order, and clicking a node routes to its page. |
| Story player | Scenes of animated SVG: dots flowing into groups and counters ticking, each scene with its caption. It ends on a predict-then-reveal of the headline number. |
| Interview player | Runs in this order: the question, then a choice of the clarifying question, then ordering the whiteboard steps (by drag, with buttons as a fallback). Next the learner commits the answer. Then the model answer appears while the SVG whiteboard builds step by step. Last come the two follow-ups and the crossed-out wrong answers with their reasons. |
| Six seats | Six cards or a wheel, one seat each, with what that seat does with the idea and the question it asks. |
| Self-check | Items of four types: predict a number, pick, order, and sort into bins (with a click fallback). The score shows as a readout. |
| Icons | A small set drawn for the kit as inline SVG, for example: bank, phone call, coin, ledger, chart, map, tree, forest, shield, clock, magnifier, alarm, the six seats, memo, envelope, lock. No logo of any brand or institution. |

## The look

- **Colours.** The deck's colours, read from `scripts/deck_layout.py`, so slide and page are one
  system.
- **Feel.** Editorial and serious, with generous spacing, a serif for headings as the deck uses and
  the system sans for everything else. Important text is never grey.
- **Motion.** It explains: eased, about 300 to 900 milliseconds a step, with no bounce and no
  decoration.
- **Phone width.** The stage reflows to one column.
- **Craft.** Read `design-taste-frontend` and `dataviz` before you draw, and treat the demo page as
  the proof that the kit looks like a finished product.

## Finish

- **Branch.** `w05-explorer-kit`. Commit in small commits and push.
- **Gate.** Screenshots of every route of the demo page at both widths, looked at by you and fixed
  until they are clean.
- **Proofs in the report.**
  - `html_sweep.py` passes on the demo.
  - The Week 1 to 4 sweep summaries are unchanged.
  - `build_companion.py --check` is clean on Weeks 1 to 4.
  - `verify.py content/W05/D1` still passes on the old page.
- **Report.** Under 400 words: the API in one table, the proofs, and what a day session should
  know first.
- **Time.** You have about two and a half hours.
