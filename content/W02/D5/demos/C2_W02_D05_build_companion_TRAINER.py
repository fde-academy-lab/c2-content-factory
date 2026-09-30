"""Write Friday's companion page: the director's sheet as a simulator, computed from the two exports.

Run from the repository root, then inline the shared library:
    python3 content/W02/D5/demos/C2_W02_D05_build_companion_TRAINER.py
    python3 scripts/build_companion.py content/W02/D5/demos/C2_W02_D05_last_mile_STUDENT.html

The page carries aggregates, the protect list and the id index the lookup needs, never the raw
rows. Every number is computed here from data/ so a regenerated export is a re-run. The four
experiment cards run on invented records, labelled invented on the page. The page stores nothing
and calls no network.
"""
import json
import pathlib

import pandas as pd

DAY = pathlib.Path("content/W02/D5")
OUT = DAY / "demos" / "C2_W02_D05_last_mile_STUDENT.html"
clean = pd.read_csv(DAY / "data" / "C2_W02_D05_customer_table_STUDENT.csv")
raw = pd.read_csv(DAY / "data" / "C2_W02_D05_raw_export_STUDENT.csv")
raw["quarter"] = pd.to_datetime(raw.order_date).dt.month.map(lambda m: "Q1" if m <= 6 else "Q2")
raw["m"] = pd.to_datetime(raw.order_date).dt.month
once = raw.drop_duplicates("order_id")
SEGMENTS = ["Business", "Retail-Core", "Retail-Plus", "Student"]
CITIES = sorted(clean.city.unique())

data = {"segments": SEGMENTS, "cities": CITIES, "warehouse": {"Q1": 100000000, "Q2": 98400000},
        "monthly": {}, "tree": {}}
for mode, frame in (("once", once), ("row", raw)):
    for seg in SEGMENTS:
        part = frame[frame.segment == seg]
        data["monthly"].setdefault(seg, {})[mode] = [int(part[part.m == m].order_amount.sum()) for m in range(4, 10)]
        for q in ("Q1", "Q2"):
            pq = part[part.quarter == q]
            data["tree"].setdefault(seg, {}).setdefault(q, {})[mode] = {
                "customers": int(pq.customer_id.nunique() if mode == "once" else len(pq)),
                "orders": int(len(pq)), "revenue": int(pq.order_amount.sum())}
plus = clean[clean.segment == "Retail-Plus"].sort_values(["revenue", "customer_id"], ascending=[False, True])
data["protect"] = [[r.customer_id, r.city, int(r.revenue)] for r in plus.head(50).itertuples()]
rank = {cid: i + 1 for i, cid in enumerate(plus.customer_id)}
data["ids"] = [[r.customer_id, r.segment, r.city, int(r.revenue), rank.get(r.customer_id, 0)]
               for r in clean.sort_values("customer_id").itertuples()]

PAGE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The last mile: Week 2, Friday companion</title>
<style data-c2kit></style>
<style>
  .formula{font:15px var(--mono);background:var(--surface);border:1px solid var(--line);border-radius:8px;
           padding:8px 12px;margin-top:10px;color:var(--ink);overflow-x:auto}
  .jumped{font-size:13px;color:var(--muted);margin:10px 8px 2px}
  .note{font-size:13.5px;color:var(--muted)}
  .ok{color:var(--green);font-weight:700}
  .warn{color:var(--rose);font-weight:700}
  select,input[type=text]{font:15px var(--sans);border:1px solid var(--lilac);border-radius:8px;padding:6px 9px;
           color:var(--ink);background:var(--white)}
  .ctl{margin:10px 0}
  .ctl .name{display:block;font:700 10.5px var(--sans);letter-spacing:.2em;text-transform:uppercase;
           color:var(--violet);margin-bottom:6px}
  table.mini{border-collapse:collapse;font-size:14px;width:100%}
  table.mini th{background:var(--ink);color:var(--white);text-align:left;padding:5px 8px}
  table.mini td{padding:4px 8px;border-bottom:1px solid var(--line)}
  table.mini td.num{text-align:right;font-family:var(--mono)}
  tr.hid td{color:var(--soft);text-decoration:line-through}
</style>
</head>
<body>
<header class="hero">
  <span class="kicker">Week 2 &middot; Friday &middot; Companion</span>
  <h1>The last mile</h1>
  <p class="quote">&ldquo;If a director changes an assumption in the room, the sheet must recalculate in front of them.&rdquo;</p>
  <p class="who">Meera's chief of staff, Kalpa Retail, to the data and AI team at Kalpa's Global Capability Centre</p>
  <p class="promise">This page is the director's sheet with its assumptions on switches. Walk the day in six steps,
    then change what a director changes: how orders are counted, which id is looked up and how, which city the list
    is filtered to, and what the card covers. The sheet's numbers come from Friday's two exports; the four experiment
    cards run on invented records, and each says so.</p>
</header>

<div class="page">
  <nav class="rail" aria-label="Sections">
    <div class="label">On this page</div>
    <a href="#walk" data-part="walk"><span class="n">01</span>The day in six steps</a>
    <a href="#sheet" data-part="sheet"><span class="n">02</span>The director's sheet</a>
    <a href="#experiments" data-part="experiments"><span class="n">03</span>Four experiments</a>
    <a href="#glossary" data-part="glossary"><span class="n">04</span>Glossary</a>
    <p class="jumped" id="jumped">You are at the top of the page.</p>
  </nav>

  <main>
    <section class="part" id="walk">
      <p class="eyebrow">01 &middot; The guided walk</p>
      <h2>From two exports to a front page</h2>
      <p class="lede">Each step is one decision the day made, drawn from Friday's exports. Press Next.</p>
      <div class="card"><div class="holder" id="walkChart"></div></div>
      <div class="walk" style="margin-top:16px">
        <div class="card narration" aria-live="polite">
          <div class="step" id="walkStep">Step 1 of 6</div>
          <h3 id="walkTitle"></h3>
          <p id="walkText"></p>
          <div class="row">
            <button class="btn primary" id="walkNext" type="button">Next</button>
            <button class="btn" id="walkRestart" type="button">Restart the walk</button>
          </div>
        </div>
      </div>
    </section>

    <section class="part" id="sheet">
      <p class="eyebrow">02 &middot; The simulator</p>
      <h2>The director's sheet</h2>
      <p class="lede">Four assumptions, each a switch. The tree, the lookup, the list's foot and the card recompute
        from the same numbers, and the release line says what may go into Monday's deck.</p>
      <div class="grid2">
        <div class="card">
          <div class="ctl"><span class="name">Count each order</span>
            <div class="row" style="margin-top:0">
              <button class="btn" id="modeOnce" type="button" aria-pressed="true">once per order</button>
              <button class="btn" id="modeRow" type="button" aria-pressed="false">once per payment row</button>
            </div></div>
          <div class="ctl"><span class="name">What the card covers</span>
            <select id="scope" aria-label="What the card covers">
              <option>All segments</option><option>All except Business</option><option>Retail-Plus</option>
              <option>Retail-Core</option><option>Student</option><option>Business</option>
            </select></div>
          <div class="ctl"><span class="name">Member id to look up</span>
            <select id="lookId" aria-label="Member id to look up">
              <option value="C-0152">C-0152</option><option value="C-0194">C-0194</option>
              <option value="C-0195">C-0195</option><option value="C-0999">C-0999</option>
            </select>
            <div class="row" style="margin-top:6px">
              <button class="btn" id="matchExact" type="button" aria-pressed="true">exact match</button>
              <button class="btn" id="matchApprox" type="button" aria-pressed="false">approximate match</button>
            </div></div>
          <div class="ctl"><span class="name">Filter the protect list to a city</span>
            <select id="city" aria-label="Filter the protect list to a city"><option>All cities</option></select>
            <div class="row" style="margin-top:6px">
              <button class="btn" id="footSub" type="button" aria-pressed="true">SUBTOTAL(109) at the foot</button>
              <button class="btn" id="footSum" type="button" aria-pressed="false">SUM at the foot</button>
            </div></div>
          <div class="row"><button class="btn" id="sheetReset" type="button">Back to the honest sheet</button></div>
          <p class="note" id="sheetSays" aria-live="polite">Change a switch and this line says what the change did.</p>
        </div>
        <div class="card">
          <div class="step" style="font:700 11px var(--sans);letter-spacing:.2em;text-transform:uppercase;color:var(--violet)">The card</div>
          <p class="verdict" id="card"></p>
          <div class="holder" id="trend"></div>
          <div class="step" style="font:700 11px var(--sans);letter-spacing:.2em;text-transform:uppercase;color:var(--violet);margin-top:10px">The lookup</div>
          <p id="lookOut"></p>
          <div class="step" style="font:700 11px var(--sans);letter-spacing:.2em;text-transform:uppercase;color:var(--violet);margin-top:10px">The foot of the list</div>
          <p id="footOut"></p>
          <div class="strip" id="releaseStrip"><b class="tag">Release</b><span id="release"></span></div>
        </div>
      </div>
      <div class="grid2" style="margin-top:18px">
        <div class="card"><div class="holder" id="treeChart"></div><p class="note" id="treeNote"></p></div>
        <div class="card"><div class="holder" id="bridgeChart"></div></div>
      </div>
    </section>

    <section class="part" id="experiments">
      <p class="eyebrow">03 &middot; Experiment cards</p>
      <h2>Four experiments, one change each</h2>
      <p class="lede">Read the situation and the hypothesis, decide what you expect, then run. Every record in these
        cards is invented to isolate one mechanism.</p>
      <div class="grid2">
        <article class="card exp" id="expA">
          <div class="part-label">Experiment A &middot; invented rows</div>
          <h3 style="font:400 20px var(--serif);color:var(--ink);margin:0">Remove Duplicates on a payment export</h3>
          <p><b>Situation.</b> Three invented orders of Rs 1,000, Rs 2,000 and Rs 4,000. The second was paid in two
            instalments of Rs 1,200 and Rs 800; the third was posted twice by the gateway. The export has five rows.</p>
          <p><b>Hypothesis.</b> Removing rows that are identical in every column brings the total back to Rs 7,000.</p>
          <p><b>Watch for.</b> How many rows go, and where the total lands.</p>
          <div class="holder" id="expAChart"></div>
          <div class="row">
            <button class="btn" id="expARun" type="button" aria-pressed="false">Remove Duplicates</button>
            <button class="btn" id="expASeq" type="button">Show the sequence</button>
          </div>
          <div class="result" id="expAResult" hidden>
            <p><b>What happened.</b> <span id="expAWhat"></span></p>
            <p><b>Why it matters.</b> An analyst who ran Remove Duplicates believes the export is clean and ships a
              number still inflated by every instalment order.</p>
            <p class="rule">Count each order once by its key; removing identical rows is not the same thing.</p>
          </div>
          <p class="waiting" id="expAWait">What happened appears here after the run.</p>
        </article>

        <article class="card exp" id="expB">
          <div class="part-label">Experiment B &middot; invented ids</div>
          <h3 style="font:400 20px var(--serif);color:var(--ink);margin:0">An approximate match on a missing id</h3>
          <p><b>Situation.</b> Eight invented members, C-0401 to C-0409, sorted by id, with C-0405 missing. The chief
            of staff types C-0405.</p>
          <p><b>Hypothesis.</b> An exact match says the id is not there; an approximate match returns C-0404.</p>
          <p><b>Watch for.</b> Whether either answer carries a warning.</p>
          <div class="formula" id="expBWork">MATCH("C-0405", ids, ?)</div>
          <div class="row">
            <button class="btn" id="expBRun" type="button" aria-pressed="false">Run both lookups</button>
            <button class="btn" id="expBSeq" type="button">Show the sequence</button>
          </div>
          <div class="result" id="expBResult" hidden>
            <p><b>What happened.</b> <span id="expBWhat"></span></p>
            <p><b>Why it matters.</b> The approximate answer looks exactly like a real one, so nobody in the room can
              tell it is somebody else's row.</p>
            <p class="rule">Test every lookup with an id you know is missing before anyone else uses it.</p>
          </div>
          <p class="waiting" id="expBWait">What happened appears here after the run.</p>
        </article>

        <article class="card exp" id="expC">
          <div class="part-label">Experiment C &middot; invented members</div>
          <h3 style="font:400 20px var(--serif);color:var(--ink);margin:0">The foot of a filtered list</h3>
          <p><b>Situation.</b> Eight invented members worth Rs 60,000 together, three of them in Mumbai worth Rs 25,500.
            The list is filtered to Mumbai.</p>
          <p><b>Hypothesis.</b> SUM at the foot still reads Rs 60,000; SUBTOTAL(109) reads Rs 25,500.</p>
          <p><b>Watch for.</b> The struck-through rows, and which foot follows them.</p>
          <div class="holder" id="expCTable"></div>
          <div class="row">
            <button class="btn" id="expCRun" type="button" aria-pressed="false">Filter to Mumbai</button>
            <button class="btn" id="expCSeq" type="button">Show the sequence</button>
          </div>
          <div class="result" id="expCResult" hidden>
            <p><b>What happened.</b> <span id="expCWhat"></span></p>
            <p><b>Why it matters.</b> A store head told Rs 60,000 plans a retention budget for members who are not on
              their list.</p>
            <p class="rule">The foot of a filtered list is SUBTOTAL(109), and a count of visible rows sits beside it.</p>
          </div>
          <p class="waiting" id="expCWait">What happened appears here after the run.</p>
        </article>

        <article class="card exp" id="expD">
          <div class="part-label">Experiment D &middot; invented numbers</div>
          <h3 style="font:400 20px var(--serif);color:var(--ink);margin:0">The base of a change</h3>
          <p><b>Situation.</b> An invented segment fell from Rs 500 in one quarter to Rs 400 in the next.</p>
          <p><b>Hypothesis.</b> Measured on the earlier quarter the fall is 20 percent; divided by the later one it
            reads 25 percent.</p>
          <p><b>Watch for.</b> Which denominator the formula uses.</p>
          <div class="formula" id="expDWork">(400 - 500) / ? = ?</div>
          <div class="row">
            <button class="btn" id="expDRun" type="button" aria-pressed="false">Compute both</button>
            <button class="btn" id="expDSeq" type="button">Show the sequence</button>
          </div>
          <div class="result" id="expDResult" hidden>
            <p><b>What happened.</b> <span id="expDWhat"></span></p>
            <p><b>Why it matters.</b> On Friday's Retail-Plus numbers the same slip turns a 29.4 percent fall into 41.7.</p>
            <p class="rule">A change is measured on the period you are comparing against.</p>
          </div>
          <p class="waiting" id="expDWait">What happened appears here after the run.</p>
        </article>
      </div>
    </section>

    <section class="part" id="glossary">
      <p class="eyebrow">04 &middot; Glossary</p>
      <h2>The day's words, and where each first mattered</h2>
      <div class="card">
        <dl class="gloss">
          <dt>Grain</dt><dd>What one row of a table stands for: a customer, an order or a payment.<span class="where">Half
            one, S7; notebook 1, section 1.</span></dd>
          <dt>PivotTable</dt><dd>Excel's grouped summary of a range; it keeps its own copy of the source and needs a
            refresh when the source changes.<span class="where">Half one, S8; notebook 1, section 1.</span></dd>
          <dt>Control total</dt><dd>A number owned upstream, such as Monday's warehouse revenue, that a sheet must
            reproduce before it is trusted.<span class="where">Half one, S13; notebook 1, section 4.</span></dd>
          <dt>Exact and approximate match</dt><dd>An exact match finds the id or says it is missing; an approximate
            match returns the nearest id below.<span class="where">Half one, S22 to S25; notebook 2, section 3.</span></dd>
          <dt>SUBTOTAL(109)</dt><dd>A sum that leaves out rows a filter or a hide has taken off the screen.<span
            class="where">Half one, S27; notebook 2, section 4.</span></dd>
          <dt>Period, comparison, base</dt><dd>The three things a front-page number carries so it cannot be misread.<span
            class="where">Half one, S30 to S35; notebook 3.</span></dd>
          <dt>Drift</dt><dd>A sheet that no longer ties to its source, usually because a cell was typed over.<span
            class="where">Half two, S8; the second case.</span></dd>
          <dt>Operating rule</dt><dd>The warehouse owns the number, pandas owns the iteration, Excel owns the last
            mile.<span class="where">Half two, S9.</span></dd>
        </dl>
      </div>
      <p class="foot">Week 2, Friday. The workbooks beside this page are the versions to keep: the deck pack holds
        the three deliverables as live formulas, and the decision tool hides one formula defect per tab. Kalpa Retail and
        everyone in it are fictional. The page stores nothing and calls no network.</p>
    </section>
  </main>
</div>

<dialog id="seqDialog" aria-labelledby="seqTitle">
  <div class="head"><span id="seqTitle">The sequence</span><button class="close" id="seqClose" type="button">Close</button></div>
  <div class="body"><div class="holder" id="seqBody"></div><p class="note" id="seqNote"></p></div>
</dialog>

<script data-c2kit></script>
<script id="data" type="application/json">__DATA__</script>
<script>
(function () {
  "use strict";
  var K = window.C2K;
  var D = JSON.parse(document.getElementById("data").textContent);
  function $(id) { return document.getElementById(id); }
  var MONTHS = ["Apr", "May", "Jun", "Jul", "Aug", "Sep"];
  function money(n) {
    var a = Math.abs(n);
    if (a >= 1e7) return "Rs " + (n / 1e7).toFixed(2) + " crore";
    if (a >= 1e5) return "Rs " + (n / 1e5).toFixed(2) + " lakh";
    return K.rupees(n);
  }
  function pct(x) { return (Math.round(x * 1000) / 10).toFixed(1); }

  /* ---------------------------------------------------------------- the rail */
  var rail = document.querySelectorAll(".rail a");
  Array.prototype.forEach.call(rail, function (a) {
    a.addEventListener("click", function () {
      Array.prototype.forEach.call(rail, function (b) { b.classList.toggle("on", b === a); });
      $("jumped").textContent = "You jumped to " + a.textContent.replace(/^\d+/, "").trim() + ".";
    });
  });

  /* ---------------------------------------------------------------- sums over the data */
  function segTotal(seg, q, mode) { return D.tree[seg][q][mode].revenue; }
  function scopeSegs(scope) {
    if (scope === "All segments") return D.segments;
    if (scope === "All except Business") return D.segments.filter(function (s) { return s !== "Business"; });
    return [scope];
  }
  function scopeQ(scope, q, mode) {
    return scopeSegs(scope).reduce(function (t, s) { return t + segTotal(s, q, mode); }, 0);
  }
  function scopeMonths(scope, mode) {
    return MONTHS.map(function (_, i) {
      return scopeSegs(scope).reduce(function (t, s) { return t + D.monthly[s][mode][i]; }, 0);
    });
  }

  /* ---------------------------------------------------------------- the walk */
  var consumer = ["Retail-Core", "Retail-Plus", "Student"];
  var WALK = [
    { t: "Two exports, two grains",
      x: "The customer table has one row per customer. The raw export has one row per payment, 1,450 rows for 1,000 orders, and it is the only one that can split the quarters.",
      draw: function () { return K.columns(["rows in the raw export", "distinct orders"], [["count", [1450, 1000]]], { title: "The raw export: more rows than orders" }); } },
    { t: "The hurried pivot",
      x: "Sum of order_amount over every payment row reads Rs 39.41 crore for the half-year, and says Retail-Core grew. The warehouse says Rs 19.84 crore.",
      draw: function () { return K.bridge(["the warehouse", 198400000], [["repeated rows", scopeQ("All segments", "Q1", "row") + scopeQ("All segments", "Q2", "row") - D.warehouse.Q1 - D.warehouse.Q2]], { fmt: money, endLabel: "the hurried pivot", title: "From the warehouse to the hurried pivot" }); } },
    { t: "Count each order once",
      x: "A first-row flag per order brings the tree back to the warehouse to the rupee. Retail-Plus orders per customer fell from 2.36 to 1.84.",
      draw: function () { return K.columns(consumer, [["Q1", consumer.map(function (s) { return D.tree[s].Q1.once.revenue; })], ["Q2", consumer.map(function (s) { return D.tree[s].Q2.once.revenue; })]], { fmt: money, lit: [1], title: "Consumer revenue by quarter, each order once" }); } },
    { t: "A lookup that fails out loud",
      x: "C-0195 has no orders in the two quarters. An approximate match hands back C-0194, rank 15 on the protect list; an exact match says the id is not in the table.",
      draw: function () { return K.flow(["find C-0195", "approximate: C-0194's row", "exact: not in the table"], 2, { title: "Two lookups, one missing id" }); } },
    { t: "The foot of a filtered list",
      x: "Filtered to Mumbai, the protect list shows 11 members worth Rs 1,56,790. SUM at the foot still reads Rs 7,14,890.",
      draw: function () { return K.columns(["the foot"], [["SUM", [714890]], ["SUBTOTAL(109)", [156790]]], { fmt: money, title: "One filtered list, two feet" }); } },
    { t: "The card, with its period, comparison and base",
      x: "Q2, July to September 2026: Rs 9.84 crore, down 1.6 percent on Q1 (Rs 10.00 crore). Take Business out and it is down 17.3 percent; the scope is printed on the card.",
      draw: function () { return K.line(MONTHS, [["all except Business", scopeMonths("All except Business", "once"), "bad"]], { fmt: money, title: "Consumer revenue by month" }); } }
  ];
  var walkAt = 0;
  function showWalk() {
    var w = WALK[walkAt];
    K.draw("walkChart", w.draw());
    $("walkStep").textContent = "Step " + (walkAt + 1) + " of " + WALK.length;
    $("walkTitle").textContent = w.t;
    $("walkText").textContent = w.x;
    $("walkNext").textContent = walkAt === WALK.length - 1 ? "Back to the start" : "Next";
  }
  $("walkNext").addEventListener("click", function () { walkAt = (walkAt + 1) % WALK.length; showWalk(); });
  $("walkRestart").addEventListener("click", function () {
    walkAt = 0; showWalk(); $("walkStep").textContent = "Step 1 of " + WALK.length + ", restarted";
  });
  showWalk();

  /* ---------------------------------------------------------------- the simulator */
  var S = { mode: "once", match: "exact", foot: "sub" };
  D.cities.forEach(function (c) { var o = document.createElement("option"); o.textContent = c; $("city").appendChild(o); });
  function press(on, off) { $(on).setAttribute("aria-pressed", "true"); $(off).setAttribute("aria-pressed", "false"); }

  function lookup(id) {
    var ids = D.ids, i, found = null, below = null;
    for (i = 0; i < ids.length; i++) {
      if (ids[i][0] === id) found = ids[i];
      if (ids[i][0] <= id) below = ids[i];
    }
    return S.match === "exact" ? found : below;
  }

  function render() {
    var scope = $("scope").value;
    var q1 = scopeQ(scope, "Q1", S.mode), q2 = scopeQ(scope, "Q2", S.mode);
    var comp = scopeQ("All segments", "Q2", S.mode);
    var total = scopeQ("All segments", "Q1", S.mode) + comp;
    var ties = Math.abs(total - (D.warehouse.Q1 + D.warehouse.Q2)) < 1;
    var change = (q2 - q1) / q1;
    $("card").textContent = ties
      ? scope + ", Q2, July to September 2026: " + money(q2) + ", " + (change < 0 ? "down " : "up ") + pct(Math.abs(change)) +
        " percent on Q1, April to June 2026 (" + money(q1) + "); " + pct(q2 / comp) + " percent of company revenue in Q2."
      : "Hold the card: its two quarters sum to " + money(total) + " against the warehouse's " + money(D.warehouse.Q1 + D.warehouse.Q2) + ".";
    K.draw("trend", K.line(MONTHS, [[scope, scopeMonths(scope, S.mode), ties ? "plain" : "bad"]], { fmt: money, width: 520, title: "Monthly revenue, " + scope }));

    var id = $("lookId").value, row = lookup(id);
    if (!row) $("lookOut").innerHTML = '<span class="ok">' + id + " is not in the customer table.</span> Say so, and check the export before anyone answers.";
    else if (row[0] !== id) $("lookOut").innerHTML = '<span class="warn">The sheet shows ' + K.rupees(row[3]) + (row[4] && row[4] <= 50 ? ", rank " + row[4] + " on the list" : "") + ".</span> That is " + row[0] + "'s row, returned for " + id + ", with no warning.";
    else $("lookOut").textContent = id + ": " + row[1] + ", " + row[2] + ", " + K.rupees(row[3]) + (row[4] && row[4] <= 50 ? ", rank " + row[4] + " of 50 on the protect list." : ", not on the protect list.");

    var city = $("city").value, visible = D.protect.filter(function (r) { return city === "All cities" || r[1] === city; });
    var sumAll = D.protect.reduce(function (t, r) { return t + r[2]; }, 0);
    var sumVis = visible.reduce(function (t, r) { return t + r[2]; }, 0);
    var shown = S.foot === "sub" ? sumVis : sumAll;
    $("footOut").innerHTML = (S.foot === "sum" && city !== "All cities" ? '<span class="warn">' : '<span class="ok">') + K.rupees(shown) +
      "</span> at the foot, with " + visible.length + " of 50 members on screen" + (city === "All cities" ? "." : ", filtered to " + city + ".");

    var lookBad = row && row[0] !== id, footBad = S.foot === "sum" && city !== "All cities";
    var msg;
    if (!ties) msg = "Do not send anything: the tree counts an order once per payment row, and the card inherits it.";
    else if (lookBad || footBad) msg = "Do not read the list aloud: " + (lookBad ? "the lookup answered with a neighbour" : "the foot adds rows the filter hid") + ".";
    else msg = "The tree and the card tie to the warehouse; the list's lookup and foot answer honestly.";
    $("release").textContent = msg;
    $("releaseStrip").className = "strip " + (ties && !lookBad && !footBad ? "good" : "bad");

    K.draw("treeChart", K.columns(consumer, [["Q1", consumer.map(function (s) { return D.tree[s].Q1[S.mode].orders / D.tree[s].Q1[S.mode].customers; })],
      ["Q2", consumer.map(function (s) { return D.tree[s].Q2[S.mode].orders / D.tree[s].Q2[S.mode].customers; })]],
      { fmt: function (v) { return v.toFixed(2); }, lit: [1], title: "Orders per customer, Q1 against Q2" }));
    $("treeNote").textContent = S.mode === "once"
      ? "Customers counted once each, orders once each: Retail-Plus falls from 2.36 to 1.84."
      : "Counted per payment row, every customer and order is a row, so the rate reads 1.00 and the tree says nothing.";
    K.draw("bridgeChart", K.bridge(["Q1 revenue", scopeQ(scope, "Q1", S.mode)],
      scopeSegs(scope).map(function (s) { return [s, segTotal(s, "Q2", S.mode) - segTotal(s, "Q1", S.mode)]; }),
      { fmt: money, endLabel: "Q2 revenue", title: "Q1 to Q2 by segment, " + scope }));
  }
  function says(text) { $("sheetSays").textContent = text; }
  $("modeOnce").addEventListener("click", function () { S.mode = "once"; press("modeOnce", "modeRow"); render();
    says("Each order counted once: the tree and the card tie to the warehouse's Rs 19.84 crore."); });
  $("modeRow").addEventListener("click", function () { S.mode = "row"; press("modeRow", "modeOnce"); render();
    says("Each payment row counted: the half-year reads Rs 39.41 crore and the release holds everything."); });
  $("matchExact").addEventListener("click", function () { S.match = "exact"; press("matchExact", "matchApprox"); render();
    says("Exact match: a missing id is reported as missing."); });
  $("matchApprox").addEventListener("click", function () { S.match = "approx"; press("matchApprox", "matchExact"); render();
    says("Approximate match: a missing id comes back as its neighbour's row. Try C-0195 or C-0999."); });
  $("footSub").addEventListener("click", function () { S.foot = "sub"; press("footSub", "footSum"); render();
    says("SUBTOTAL(109): the foot adds only the members on screen."); });
  $("footSum").addEventListener("click", function () { S.foot = "sum"; press("footSum", "footSub"); render();
    says("SUM: the foot adds all fifty, whatever the filter hides. Pick a city to see it."); });
  ["scope", "lookId", "city"].forEach(function (k) { $(k).addEventListener("change", function () {
    render(); says("Changed " + $(k).getAttribute("aria-label").toLowerCase() + " to " + $(k).value + "."); }); });
  $("sheetReset").addEventListener("click", function () {
    S = { mode: "once", match: "exact", foot: "sub" };
    press("modeOnce", "modeRow"); press("matchExact", "matchApprox"); press("footSub", "footSum");
    $("scope").value = "All segments"; $("lookId").value = "C-0152"; $("city").value = "All cities";
    render();
    $("release").textContent = "Back to the honest sheet: every switch at its safe setting.";
    says("Every switch is back at its safe setting.");
  });
  render();

  /* ---------------------------------------------------------------- the sequence popup */
  function openSeq(title, lanes, messages, note) {
    $("seqTitle").textContent = title;
    K.draw("seqBody", K.sequence(lanes, messages, { laneWidth: 200 }));
    $("seqNote").textContent = note;
    var d = $("seqDialog");
    if (typeof d.showModal === "function") d.showModal(); else d.setAttribute("open", "");
  }
  $("seqClose").addEventListener("click", function () { $("seqDialog").close(); });
  function reveal(key, text) { $(key + "What").textContent = text; $(key + "Result").hidden = false; $(key + "Wait").hidden = true; }

  /* ---------------------------------------------------------------- experiment A */
  var aDone = false;
  function drawA() {
    K.draw("expAChart", K.columns(["as exported", "after Remove Duplicates", "each order once"], [["total", [13000, aDone ? 9000 : 13000, 7000]]],
      { fmt: K.rupees, lit: [1], title: aDone ? "One row went; the instalment order still counts twice" : "Five rows for three orders worth Rs 7,000" }));
  }
  $("expARun").addEventListener("click", function () {
    aDone = !aDone; this.setAttribute("aria-pressed", String(aDone));
    this.textContent = aDone ? "Put the rows back" : "Remove Duplicates";
    drawA();
    reveal("expA", aDone ? "One row went, the gateway's copy. The instalment order's two rows differ in the amount paid, so both stay, and four rows total Rs 9,000 where the orders are worth Rs 7,000."
      : "Back to the export: five rows, a total of Rs 13,000 for three orders worth Rs 7,000.");
  });
  $("expASeq").addEventListener("click", function () {
    openSeq("Experiment A, as a sequence", ["the export", "Remove Duplicates", "the pivot"], [
      ["the export", "Remove Duplicates", "five rows"], ["Remove Duplicates", "Remove Duplicates", "drop the identical copy"],
      ["Remove Duplicates", "the pivot", "four rows"], ["the pivot", "the pivot", "Rs 9,000, still over"]],
      "Identical rows are one defect; a finer grain is another, and only a key-based count fixes the second.");
  });
  drawA();

  /* ---------------------------------------------------------------- experiment B */
  $("expBRun").addEventListener("click", function () {
    var on = this.getAttribute("aria-pressed") !== "true";
    this.setAttribute("aria-pressed", String(on));
    $("expBWork").textContent = on ? 'MATCH("C-0405", ids, 0) is #N/A; MATCH("C-0405", ids, 1) is C-0404' : 'MATCH("C-0405", ids, ?)';
    reveal("expB", on ? "The exact match returned #N/A, which IFERROR turns into 'not in the table'. The approximate match returned C-0404's row, Rs 8,760, and nothing on the screen said so."
      : "Run it again to see both answers side by side.");
  });
  $("expBSeq").addEventListener("click", function () {
    openSeq("Experiment B, as a sequence", ["chief of staff", "the lookup", "the ids"], [
      ["chief of staff", "the lookup", "find C-0405"], ["the lookup", "the ids", "exact: none"], ["the lookup", "chief of staff", "not in the table"],
      ["the lookup", "the ids", "approximate: largest not above"], ["the lookup", "chief of staff", "C-0404, Rs 8,760"]],
      "Both lookups ran on the same eight ids; only one of them admitted the id was missing.");
  });

  /* ---------------------------------------------------------------- experiment C */
  var MEMBERS = [["C-0501", "Delhi", 11000], ["C-0502", "Mumbai", 9200], ["C-0503", "Pune", 8000], ["C-0504", "Mumbai", 8400],
    ["C-0505", "Delhi", 6000], ["C-0506", "Mumbai", 7900], ["C-0507", "Chennai", 5500], ["C-0508", "Pune", 4000]];
  var cOn = false;
  function drawC() {
    var html = '<table class="mini"><tr><th>Member (invented)</th><th>City</th><th>Revenue</th></tr>';
    MEMBERS.forEach(function (m) { html += '<tr class="' + (cOn && m[1] !== "Mumbai" ? "hid" : "") + '"><td>' + m[0] + "</td><td>" + m[1] + '</td><td class="num">' + K.rupees(m[2]) + "</td></tr>"; });
    var vis = MEMBERS.filter(function (m) { return !cOn || m[1] === "Mumbai"; }).reduce(function (t, m) { return t + m[2]; }, 0);
    html += '<tr><td colspan="2"><b>SUM</b></td><td class="num">' + K.rupees(60000) + '</td></tr><tr><td colspan="2"><b>SUBTOTAL(109)</b></td><td class="num">' + K.rupees(vis) + "</td></tr></table>";
    $("expCTable").innerHTML = html;
  }
  $("expCRun").addEventListener("click", function () {
    cOn = !cOn; this.setAttribute("aria-pressed", String(cOn)); this.textContent = cOn ? "Clear the filter" : "Filter to Mumbai";
    drawC();
    reveal("expC", cOn ? "Five rows went off the screen. SUM still reads Rs 60,000; SUBTOTAL(109) reads Rs 25,500, the three members you can see."
      : "No filter: both feet read Rs 60,000, which is why the defect hides until someone filters.");
  });
  $("expCSeq").addEventListener("click", function () {
    openSeq("Experiment C, as a sequence", ["the filter", "SUM", "SUBTOTAL(109)"], [
      ["the filter", "SUM", "hide five rows"], ["SUM", "SUM", "adds all eight: Rs 60,000"],
      ["the filter", "SUBTOTAL(109)", "hide five rows"], ["SUBTOTAL(109)", "SUBTOTAL(109)", "adds three: Rs 25,500"]],
      "The filter changes what the eye sees; only one of the two formulas follows the eye.");
  });
  drawC();

  /* ---------------------------------------------------------------- experiment D */
  $("expDRun").addEventListener("click", function () {
    var on = this.getAttribute("aria-pressed") !== "true";
    this.setAttribute("aria-pressed", String(on));
    $("expDWork").textContent = on ? "(400 - 500) / 500 = -20.0%;  (400 - 500) / 400 = -25.0%" : "(400 - 500) / ? = ?";
    reveal("expD", on ? "On the earlier quarter the fall is 20 percent; divided by the later quarter it reads 25 percent. The same rupees, two stories."
      : "Run it again to see both bases.");
  });
  $("expDSeq").addEventListener("click", function () {
    openSeq("Experiment D, as a sequence", ["the change", "the right base", "the wrong base"], [
      ["the change", "the change", "400 - 500 = -100"], ["the change", "the right base", "divide by 500"], ["the right base", "the right base", "-20.0%"],
      ["the change", "the wrong base", "divide by 400"], ["the wrong base", "the wrong base", "-25.0%"]],
      "A change answers 'compared with what', and the answer is the earlier period.");
  });
})();
</script>
</body>
</html>
"""

OUT.write_text(PAGE.replace("__DATA__", json.dumps(data, separators=(",", ":"))), encoding="utf-8")
print("wrote", OUT)
