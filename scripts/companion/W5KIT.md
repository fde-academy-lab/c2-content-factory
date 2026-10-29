# The Week 5 kit: how a day companion is built

INTERNAL. The manual for the five day sessions that build the Week 5 companions. Read
`docs/detailing/W05_briefs/explorers/common.md` first; this file says how the kit carries it out.
The stress page that runs every component is `scripts/companion/demo/w5kit_demo_INTERNAL.html`.
Open it beside this file: every example below is lifted from it.

## 1. What to do first

1. Copy the page template in section 2 into your day's file in `demos/`, keeping its name.
2. Write `4_trainer_only/C2_W05_D0n_explorer_data_INTERNAL.py` so it writes
   `C2_W05_D0n_explorer_data_INTERNAL.json` beside it (section 4).
3. Build each route with its page builder (section 5), one route at a time.
4. After every edit: `python3 scripts/build_companion.py <page>`, then
   `python3 scripts/html_sweep.py <page>`, then
   `python3 scripts/explorer_shots.py <page> <scratch dir> --end`, and look at every picture.

A gap in the kit goes in your report. Never patch `w5kit.js` or `w5kit.css` from a day branch, and
never paste kit code into a page: the build script overwrites the blocks.

## 2. The page template

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Week 5 Monday: should we even build a model?</title>
<style data-w5kit></style>
</head>
<body>
<main data-w5-main>
  <section data-route="story"></section>
  <section data-route="map"></section>
  <section data-route="p1" data-nav="Prediction, rule or query"></section>
  <section data-route="p2" data-nav="Input, target, prediction time"></section>
  <section data-route="case"></section>
  <section data-route="field"></section>
  <section data-route="interview"></section>
  <section data-route="check"></section>
</main>
<script type="application/json" data-w5data="../../4_trainer_only/C2_W05_D01_explorer_data_INTERNAL.json"></script>
<script data-w5kit></script>
<script>
(function () {
  "use strict";
  var D = W5.data, F = W5.fmt;
  W5.app({ week: 5, day: "Monday", question: "Should we even build a model, and what must it beat?" });
  W5.storyPage("story", { ... });
  W5.mapPage("map", { ... });
  W5.howItWorks("p1", { ... });
  /* and so on, one builder per route */
})();
</script>
</body>
</html>
```

- The three blocks stay empty in the source; `build_companion.py` fills them.
- `W5.app` builds the top bar, the nav, the progress rail, the keys and the router. Call it first.
- `data-nav` is the short label the nav prints for a how-it-works page (about 24 characters).
  The kicker on the page itself carries the row's subtopic verbatim.

## 3. The routes

| Route | Builder | Nav label and icon |
|---|---|---|
| `story` | `W5.storyPage` | The story, clapperboard |
| `map` | `W5.mapPage` | The map, waypoints |
| `p1` to `p9` | `W5.howItWorks` | its `data-nav`, numbered |
| `case` | `W5.casePage` | The case, database |
| `field` | `W5.fieldPage` | In the field, building |
| `interview` | `W5.interviewPage` | Interview room, speech bubbles |
| `check` | `W5.checkPage` | Check yourself, checklist |

Sections must appear in that order. `story`, `map`, `p1`, `case`, `field`, `interview` and
`check` are required. The hash names the route (`#p3`), so a trainer guide can link a page.

Keys: left and right arrows step the player last touched on this page, or turn the page when none
was touched; shift with an arrow always turns the page; 1 to 9 (and 0 for the tenth) jump to a
route; P toggles presenter mode, which raises the root type size so every page grows at once.

## 4. The data block

- The page carries `<script type="application/json" data-w5data="PATH"></script>`. `PATH` is
  read relative to the page's own folder.
- `build_companion.py` reads the JSON, compacts it, escapes `</` and writes it into the block.
  `--check` fails when the file changed after the page was built, and a missing or broken file
  fails the build with its reason.
- In the page, `W5.data` is the parsed object and `W5.get("case.split.early_rate")` reads one
  value; a missing key logs a kit error, so a renamed key in the data script cannot pass quietly.
- Keep the JSON to what the page draws: counts, rates, curves sampled at about 100 points, and
  scores rounded to three places. The demo's 8,238 scores travel as integers out of 1,000 and a
  string of 0s and 1s, 37 KB in all.
- Every number on the case and field pages comes from this file or from
  `docs/detailing/W05_research/W05_cases.md`; concept pages use invented numbers typed in the page
  and set `data: "invented"`.

## 5. The page builders

Every builder takes the route id and one object. Text fields take full sentences and may carry
`**bold**`; nothing else is read as markup. Every `heading` must be a question.

### The stage API

`howItWorks`, `casePage` steps, `fieldPage` scenes and `storyPage` hand your `stage` (or
`setup`) function one object, `api`:

| Member | What it does |
|---|---|
| `api.el` | The stage element, where pictures go |
| `api.controls` | The controls row under the stage |
| `api.readout` | The readout panel: `api.readout.set(items, sentence)` |
| `api.say(text)` | Writes the line under the controls |
| `api.slider(o)`, `api.toggle(o)`, `api.button(o)` | A control in the controls row |
| `api.chart(o)`, `api.cloud(o)`, `api.dotgrid(o)`, `api.matrix(o)`, `api.player(o)`, `api.svg(o)` | A picture in the stage, in the order called |
| `api.predict` | The page's prediction card, once built |
| `api.data` | The same object as `W5.data` |

Readout items are `{ value, label, sub, tone }`: `value` is the big number, `label` says what it
counts with the count beside any percentage, `sub` is a muted note, and `tone` is `good`, `bad`
or `hero` (full width). Write the readout inside the control's handler, before you start any
animation; the kit's controls already update their own value labels first.

### `W5.howItWorks(id, o)`

```js
W5.howItWorks("p1", {
  kicker: "Prediction, rule or query: when a business question is a modelling problem",   // the row's subtopic, verbatim
  heading: "Prediction, rule or query: which tool answers this ask?",                   // the deck chapter's title and short question
  lede: "One or two sentences on what to watch.",
  data: "invented",                    // "invented" | "real" (then source: "...") | "demo"
  stageTitle: "What the stage shows, as a sentence",
  predict: { q: "...", options: ["...", "...", "..."], answer: 1, why: "..." },
  stage: function (api) { /* draw, add one control, write the readout */ },
  rule: { text: "The rule, named last.", flips: "the condition that flips it." },
  where: { deck: "Chapter 1, Prediction, rule or query", notebook: "C2_W05_D01_ch01_prediction_rule_query_STUDENT.ipynb" }
});
```

The layout is the four parts in order: the kicker and heading; the prediction card, the stage, the
controls row and the readout; the rule card with its "It flips when" line; the footer. On a phone
the column order is prediction, stage, readout, then the rule.

### `W5.storyPage(id, o)`

`o.week` draws the week line (`{ today: 0, days: [{ name: "Monday", q: "..." }, ...] }`).
`o.scenes` is a list of `{ caption }`; `o.setup(api)` builds the picture once; `o.render(i, p,
api)` draws scene `i` at progress `p` (from 0 to 1 while animating, 1 when jumped to). Start a
transition only when `i` changes, as the demo's story does. `o.predict` is the headline's
predict-then-reveal and `o.headline` is `{ title, value, label }`, shown when the prediction is
committed or skipped.

### `W5.mapPage(id, o)`

```js
nodes: [{ id: "rfm", label: "Recency, frequency, cohorts", sub: "Week 2", kind: "earlier", story: "One sentence." },
        { id: "s1", label: "Prediction, rule or query", kind: "today", route: "p1", story: "..." }, ...],
edges: [{ from: "rfm", to: "s1", label: "is a column for" }, ...],   // labels of at most 26 characters
path: ["s1", "s2", "s3"],                                            // today's order
steps: ["**Step 1.** ...", ...],                                     // the storyline, one per path node
intro: "The caption of the whole-map frame."
```

`kind` is `today`, `earlier` or `later`. Today's nodes open their page; the others show their
relations in the panel. The map plays the path as a player, one node per step, and the still
state shows the whole map. On a phone the map turns into a vertical path whose boxes list what
each idea rests on and feeds.

### `W5.casePage(id, o)`

`o.data` and `o.source` cover every step. `o.steps` is a list of
`{ chapter, title, applies: [subtopics], text, stageTitle, predict, stage(api), trap }`; each step
is a tab. A trap is `{ wrong, context, misled, check, fix, honest, why }`: the wrong number shown
exactly, what it would have misled, the check that catches it, the fix and the honest number. It
asks "Would you ship it?" before it reveals the check and the fix.

### `W5.fieldPage(id, o)`

`o.scenes` is a list of `{ company, icon, angle, title, situation, source, stageTitle, predict,
stage(api) }`. `source` is one line: the source's name, its link and "checked" with the date,
for example
`"Stripe, A primer on machine learning for fraud protection, https://stripe.com/guides/primer-on-machine-learning-for-fraud-protection, checked 28 October 2026"`.
Keeping the date on the link's line is what lets `verify.py` read it. `o.seats` is
`{ hub, intro, seats: { owner, pm, architect, ml, implementation, qa } }`, each seat
`{ does, asks }`.

### `W5.interviewPage(id, o)`

`o.items` holds four to six situations, each:

```js
{ kind: "technical",                    // technical | techno-functional | scenario | client-facing
  question: "...",
  clarify: { options: ["...", "...", "..."], best: 1, why: "..." },
  steps: ["...", "...", "...", "..."],  // the whiteboard in its right order; the kit shuffles it
  answer: { options: ["...", "...", "..."], best: 0, why: "..." },
  model: "The 30-second answer.",
  board: [{ title: "...", note: "...", icon: "chart" }],   // optional; defaults to the steps
  followups: ["...", "..."],            // exactly two
  wrong: [{ text: "...", why: "..." }] }
```

The model answer opens when the answer is committed or when "Show the model answer" is pressed,
which says so when nothing was committed. The whiteboard then builds one numbered box per step on a
player.

### `W5.checkPage(id, o)`

`o.items` holds six to eight checks: `{ type: "number", q, answer, tolerance, unit, why }`,
`{ type: "pick", q, options, answer, why }`, `{ type: "order", q, items, why }` (items in the
right order) or `{ type: "bins", q, bins, cards: [{ text, bin }], why }`. Any item may carry
`figure: function (el) { ... }` to draw its picture. `o.map` redraws the map with today lit
(same shape as `mapPage`), and `o.tomorrow` is tomorrow's question.

### `W5.route(id, o)`

A head (`kicker`, `heading`, `lede`) and an empty body element to fill, for anything the builders
do not cover.

## 6. The components

| Component | Call | Options worth knowing |
|---|---|---|
| Prediction card | `W5.predict(el, o)` | `type`: `choice`, `number` or `direction`; `options`; `answer`; `tolerance` and `unit` for a number; `why`; `onReveal(state)`. Commit and "Show me without predicting" are both live from the start; a reveal without a prediction says so. |
| Readout | `W5.readout(el, { title })` | `.set(items, sentence)`, `.say(sentence)` |
| Rule card | `W5.rule(el, { text, flips })` | A missing `flips` is a kit error. |
| Footer | `W5.where(el, { deck, notebook })` | |
| Slider | `W5.slider(el, o)` | `label, min, max, step, value, fmt, onInput(v)`; `.set(v, silent)` |
| Toggle | `W5.toggle(el, o)` | `label, options: [{ value, label }], value, onChange(v)`; a click on the shown option says it is already showing |
| Button | `W5.button(el, o)` | `label, icon, primary, quiet, onClick` |
| Player | `W5.player(el, o)` | `frames: [{ caption, ms }]`, `render(i, p, player)`, `word` ("Step", "Scene", "Pair"), `stepMs`, `holdMs`, `countFrom` (0 when frame 0 is an empty start); `.go(i, animate)`, `.step(d)`, `.end()` |
| Chart | `W5.chart(el, o)` | `height`, `x: { min, max, label, ticks, fmt }` or `x: { band: [labels] }`, `y: {...}`, `legend: [{ label, color, kind: "line" | "dot" | "hollow" }]`, `right` (room for end labels), `numbers: false` to drop the table |
| Chart series | `chart.line(key, pts, o)` and `area`, `scatter`, `bars`, `hist`, `segments`, `squares`, `vline`, `hline`, `band`, `text` | `chart.set(key, data, ms)` animates when the shape matches; `vline` takes `drag(x)` and `snap`; `line` takes `end` for an end label and `dots`; `scatter` takes `hollow` and `style(i)`; `bars` takes `colors` and `fmt`; `hist` takes counts from `W5.bin(values, lo, hi, n)` |
| 2 by 2 matrix | `W5.matrix(el, o)` | `rows, cols, rowTitle, colTitle, names: { tp, fp, fn, tn }, words: { tp: fn(count) }`; `.set(counts)`, `.light("precision" | "recall" | "accuracy" | null)`. Right cells carry a tick and wrong cells a cross, so colour is never alone. |
| Dot grid | `W5.dotgrid(el, o)` | `n, cols, maxSize, gap, states, legend: { key: label }, rowLabels, shape: "square"`; states are `yes, no, hit, miss, amber, teal, empty, hollow, ink`; `.set(states or fn, { stagger })`. The legend prints the count of every state. |
| Dot cloud | `W5.cloud(el, o)` | canvas, about 10,000 dots: `n, height, phoneHeight, palette: { key: colour }, color(i), place(w, h, out)`; `.go(place, { ms, stagger, color })`, `.box(key, x, y, w, h, "right" | "wrong")`, `.label(key, x, y, content, cls, maxWidth)` |
| Placement | `W5.pack.grid(ids, box, out, { pitch, from })`, `W5.pack.columns(ids, values, box, out, { bins, lo, hi })`, `W5.pack.pitch(box, count)` | Fill the cloud's target array; return the dot radius. |
| SVG stage | `W5.svgStage(el, { height, draw(st) })` | Draw against `st.w` and `st.h` in pixels; `.redraw()`. |
| Week line | `W5.weekline(el, { days, today })` | Short names on a phone. |
| Concept map | `W5.conceptMap(el, o)` | as `mapPage`; `player: false` for a still map |
| Order list | `W5.orderList(el, { items, seed })` | drag, or the arrow buttons; `.mark()`, `.order()` |
| Bins | `W5.bins(el, { bins, cards })` | drag, or tap a card and then a bin; `.mark()` |
| Tabs | `W5.tabs(el, labels, onPick, word)` | |
| Six seats | `W5.seats(el, o)` | the wheel, the card, and "Show all six at once" |
| Icons | `W5.icon(name)` | `W5.icons` lists them: the routes, bank, phone, coin, ledger, chart, bars, tree, forest, shield, clock, magnifier, alarm, the six seats, memo, envelope, lock, card, store, cart, truck, heart, home, users, calendar, scale, flag, gauge, target and the player's own |
| Numbers | `W5.fmt` | `int(8238)` gives 8,238; `pct(0.113)` gives 11.3%; `share(174, 928)` gives 174 of 928 (18.8%); `rs(1200)` gives Rs 1,200; `dp(x, d)`; `signed(x, d)` |
| Helpers | `W5.tween(ms, fn, done)`, `W5.reduced()`, `W5.seeded(seed)`, `W5.colors`, `W5.h`, `W5.s` | |

Colours: `violet` for the class the page is about, `rest` for everything else, `amber` and `teal`
as the second and third series, `green` and `rose` only for right and wrong, always beside a tick
or a cross. The three series colours passed the dataviz validator against white on 29 October 2026.

## 7. The rules the kit enforces

| Rule from common.md | How the kit holds it |
|---|---|
| Nothing moves on arrival | No component animates when built; players start on frame 0 and the map shows its whole still state. |
| Reduced motion shows end states | Every tween jumps to its end, and players jump to the last frame on play. |
| Every control writes its readout first | The kit's controls update their labels in the click; builders write readouts in handlers before calling `go` or `set`. Route links act inside the click, not on `hashchange`. |
| No control is disabled | Nothing is ever disabled. A control with nothing to do is hidden (step back on the first frame); a click on the option already showing writes "already showing". |
| A reveal without a prediction says so | The prediction card and the interview both write it. |
| The answer stays hidden until the reveal | A readout, a label or a numbers card that states the prediction's answer shows a question mark until the learner commits or reveals; fill it in `onReveal`. The demo's Stripe scene breaks this (5.07 percent shows beside the question that asks for it) and is not a pattern to copy. |
| Scrolling stays instant | No smooth scrolling anywhere; route changes jump to the top. |
| No storage, no network, no library | The kit uses none; icons are inline path data. |
| A page keeps the skeleton | A missing route, a route out of order, a heading without a question mark, a how-it-works page without its kicker, prediction, rule, flips line or footer, a stage that does not say whether its numbers are invented, real or demo, a field scene without a checked date, a case step that names no subtopic, an interview situation without two follow-ups, and a check page without tomorrow's question each log `w5kit:` as a console error and print a red line at the top of the page. `html_sweep.py` fails on it. |
| Phone at 360 to 390 pixels | Every picture is drawn at the pixel width it gets, with type in rem, so text never shrinks with the stage; the nav becomes a strip and the rail a bar at the foot. |

## 8. Proving a page

- `python3 scripts/build_companion.py <page>`; `--check` on the day folder before you push.
- `python3 scripts/html_sweep.py <page>` walks the shell, then every route and every tab in it,
  and prints one line per route. Every control must change the page; a panel that appears after a
  click is swept on the next pass.
- `python3 scripts/explorer_shots.py <page> <scratch dir> --end` writes each route at 1366 and 390
  wide, and with `--end` each route again after every reveal and every player's last frame. Look at
  every picture for overflow, clipping, overlap and type under about 12 pixels. `--presenter`
  shoots the same routes with presenter mode on, and `--route p3 --width 390` shoots one picture.

## 9. Decisions the kit session made, 29 October 2026

| Decision | Why |
|---|---|
| Icons are Lucide path data inlined in the kit. | The deck draws Lucide icons, so slide and page share one family; the brief asks for inline SVG with no library, and Lucide's ISC licence allows it. |
| One light theme, no dark mode. | The page sits beside the light deck on the same projector; a second theme doubles the canvas and chart colour work for no teaching gain. |
| Headings in Georgia, everything else in the system sans, sizes in rem. | The deck's serif for headings, as the brief asks, and one root size that presenter mode raises. |
| Pictures render at their real pixel width, not a fixed viewBox. | A 640-unit chart shown 350 pixels wide prints 7-pixel labels; drawing at the real width keeps type at its CSS size on a phone. |
| Route changes happen inside the click, with pushState. | `hashchange` fires after the click returns, so the sweep saw nav links as dead and a learner on a slow phone saw a lag. |
| Field sources are one string with the link and "checked" date. | `verify.py` looks for the checked date on the same line as the link, and one string keeps them together. |
| The interview whiteboard is a numbered grid of boxes built on a player. | Boxes that wrap in a free flow lost their order on a projector; numbers keep it at any width. |
| Histograms of two groups of very different sizes are drawn as shares of their own group in the demo. | Drawn as counts, 928 buyers vanish under 7,310 others; the axis says "share of its own group". |
| The order list moves its elements instead of rebuilding them. | The sweep tracks controls by identity, and a rebuilt list looked like a fresh set of controls on every pass. |
| A click on the current route rewrites the rail's line and scrolls to the top. | Every control must change the page, including the nav link of the page already open. |

## Changes after the Monday and Tuesday builds (29 October 2026)

| Change | What a day page gets |
|---|---|
| The rule card waits for the prediction | On a how-it-works page the rule card holds its text behind one line and a "Show the rule now" button until the page's prediction is committed or revealed, so a rule never states the answer first. Nothing is locked: the button opens it at once, and `W5.debug.endState()` releases it with the reveal. |
| `toggle.set(value)` | Switches a toggle from another control exactly as a click on that option would, with its readout and `onChange`. |
| `chart.setY([lo, hi])` | Changes a chart's y range after it is built and lays it out again. |
| Captions carry no step number | The player prints "Step 3" or "Scene 3" beside the caption, so a caption that opens with its own "Step 3:" has it removed; the interview board's default captions no longer number themselves. |
| The dot grid speaks of dots | The kit's code no longer uses the word that tripped `verify.py`'s marks-language warning on every page. |
| `html_sweep.py` fails on load errors | A console error raised while the page loads, such as a chart laid out inside a hidden tab, now fails the sweep instead of only being counted. |
| `explorer_shots.py --tabs` | Also shoots every tab after a route's first (case chapters, field companies, interview situations), with `_end` pictures under `--end`. |
