"""Write Friday's companion page: Monday's sheet as a simulator, one panel per chapter.

Run from the repository root, then inline the shared library:
    python3 content/W02/D5/demos/C2_W02_D05_build_companion_TRAINER.py
    python3 scripts/build_companion.py content/W02/D5/demos/C2_W02_D05_last_mile_STUDENT.html

The guided walk takes one step per chapter, titled with the chapter's question and answered with
its number. Six panels follow, one per chapter, each changing the assumptions that chapter is
about, and a Checks panel reads all of them into one release sentence. Every Kalpa number is
computed here from data/ so a regenerated export is a re-run, and the assertions below stop the
build when a number drifts from the day's fact sheet.

What the page carries, and what it never carries. It holds aggregates, the per-customer ratios a
strip needs, the protect list as rank, city and revenue, and the answers to the four lookups its
dropdown offers. It never holds the customer table's id index, because the room finds the plant by
reconciling and an id list would carry it; the build refuses to write a page that names either id
next to the plant, prints the customer table's grand total, or prints its gap to the warehouse.
The list's source check is left to the learner's own run of chapter 3's your-turn cell, and the
eight experiment cards run on invented records, labelled invented on the page. The page stores
nothing and calls no network.
"""
import json
import pathlib
import re

import pandas as pd

DAY = pathlib.Path("content/W02/D5")
OUT = DAY / "demos" / "C2_W02_D05_last_mile_STUDENT.html"
table = pd.read_csv(DAY / "data" / "C2_W02_D05_customer_table_STUDENT.csv")
raw = pd.read_csv(DAY / "data" / "C2_W02_D05_raw_export_STUDENT.csv", keep_default_na=False)
raw["quarter"] = raw["order_date"].str[5:7].astype(int).map(lambda m: "Q1" if m <= 6 else "Q2")
raw["month"] = raw["order_date"].str[5:7].astype(int)
SEGMENTS = ["Business", "Retail-Core", "Retail-Plus", "Student"]
CITIES = sorted(table["city"].unique())
EARLY_CUT = "2026-09-22"                     # an export pulled a week early, as notebook 05 builds it
WAREHOUSE = {"Q1": {"orders": 538, "revenue": 100_000_000}, "Q2": {"orders": 462, "revenue": 98_400_000}}

# ---------------------------------------------------------------- chapter 1: the customer table
table["rpo"] = table["revenue"] / table["orders"]
ch1 = {}
for seg in SEGMENTS:
    part = table[table["segment"] == seg]
    ch1[seg] = {"customers": int(len(part)), "orders": int(part["orders"].sum()),
                "revenue": int(part["revenue"].sum()),
                "share": round(float(part["revenue"].sum() / table["revenue"].sum() * 100), 2),
                "avg": float(part["rpo"].mean()),
                "ratios": [int(round(v)) for v in part["rpo"]]}

# ---------------------------------------------------------------- chapter 2: the raw export, three counts, two exports
def frames(rows):
    """The export as a pivot would count it: every row, after Remove Duplicates, or once per order."""
    return {"row": rows, "dedup": rows.drop_duplicates(), "once": rows.drop_duplicates("order_id")}


tree, monthly, counts = {}, {}, {}
for exp, rows in (("today", raw), ("early", raw[raw["order_date"] < EARLY_CUT])):
    for mode, frame in frames(rows).items():
        key = f"{exp}:{mode}"
        counts[key] = {"rows": int(len(frame)), "orders": int(frame["order_id"].nunique())}
        tree[key], monthly[key] = {}, {}
        for seg in SEGMENTS:
            part = frame[frame["segment"] == seg]
            monthly[key][seg] = [int(part.loc[part["month"] == m, "order_amount"].sum()) for m in range(4, 10)]
            tree[key][seg] = {}
            for q in ("Q1", "Q2"):
                pq = part[part["quarter"] == q]
                # A pivot on the payment grain counts a customer once per row, as Count of customer_id does.
                tree[key][seg][q] = {"customers": int(pq["customer_id"].nunique() if mode == "once" else len(pq)),
                                     "orders": int(len(pq)), "revenue": int(pq["order_amount"].sum())}

# ---------------------------------------------------------------- chapter 3: the protect list and four lookups
plus = (table[table["segment"] == "Retail-Plus"]
        .sort_values(["revenue", "customer_id"], ascending=[False, True]).reset_index(drop=True))
plus["rank"] = plus.index + 1
protect = plus.head(50)
rank = dict(zip(plus["customer_id"], plus["rank"]))
ids = sorted(table["customer_id"])
by_id = table.set_index("customer_id")


def row_for(cid):
    if cid is None:
        return None
    r = by_id.loc[cid]
    return [cid, r["segment"], r["city"], int(r["revenue"]), int(rank.get(cid, 0))]


lookups = {}
for asked in ("C-0152", "C-0194", "C-0195", "C-0999"):
    below = [i for i in ids if i <= asked]
    lookups[asked] = {"exact": row_for(asked if asked in by_id.index else None),
                      "approx": row_for(below[-1] if below else None),
                      "count": int((table["customer_id"] == asked).sum())}

# ---------------------------------------------------------------- chapter 5: booked against collected
once = raw.drop_duplicates("order_id")
first_row = raw.groupby("order_id").cumcount() == 0
ch5 = {"booked": int(once["order_amount"].sum()),
       "lookup": int(once["paid_amount"].sum()),
       "every": int(raw.drop_duplicates()["paid_amount"].sum()),   # each payment once: a gateway copy is one payment posted twice
       "secondInst": int(raw.loc[~first_row & (raw["paid_amount"] != raw["order_amount"]), "paid_amount"].sum()),
       "unpaid": int(once.loc[once["paid_amount"] == 0, "order_amount"].sum()),
       "twoRow": int((raw.groupby("order_id").size() > 1).sum()),
       "paymentRows": 1428}

# ---------------------------------------------------------------- the day's fact sheet, asserted
t1 = tree["today:once"]
assert ch1["Business"]["revenue"] == 196_599_040 and ch1["Business"]["customers"] == 39
assert round(ch1["Business"]["avg"]) == 1_166_786 and round(ch1["Retail-Plus"]["avg"]) == 2_810
assert round(ch1["Business"]["orders"] * ch1["Business"]["avg"]) == 219_355_841
assert counts["today:row"] == {"rows": 1450, "orders": 1000} and counts["today:dedup"]["rows"] == 1400
assert sum(t1[s][q]["revenue"] for s in SEGMENTS for q in ("Q1", "Q2")) == 198_400_000
for q in ("Q1", "Q2"):
    assert sum(t1[s][q]["revenue"] for s in SEGMENTS) == WAREHOUSE[q]["revenue"]
    assert sum(t1[s][q]["orders"] for s in SEGMENTS) == WAREHOUSE[q]["orders"]
assert sum(tree["today:row"][s][q]["revenue"] for s in SEGMENTS for q in ("Q1", "Q2")) == 394_095_490
assert sum(tree["today:dedup"][s][q]["revenue"] for s in SEGMENTS for q in ("Q1", "Q2")) == 394_057_740
assert (t1["Retail-Plus"]["Q1"]["revenue"], t1["Retail-Plus"]["Q2"]["revenue"]) == (585_770, 413_380)
assert int(protect["revenue"].sum()) == 714_890 and int(plus.loc[49, "revenue"]) == 8_580
assert int(plus.loc[50, "revenue"]) == 8_520 and plus.loc[0, "customer_id"] == "C-0152"
assert lookups["C-0195"]["approx"][0] == "C-0194" and lookups["C-0195"]["approx"][4] == 15
assert lookups["C-0195"]["exact"] is None and lookups["C-0195"]["count"] == 0
mumbai = protect[protect["city"] == "Mumbai"]
assert len(mumbai) == 11 and int(mumbai["revenue"].sum()) == 156_790
assert ch5["lookup"] == 118_381_974 and ch5["every"] == 196_645_070
assert ch5["lookup"] + ch5["secondInst"] == ch5["every"] and ch5["secondInst"] == 78_263_096 and ch5["twoRow"] == 450
assert ch5["booked"] - ch5["every"] == ch5["unpaid"] == 1_754_930
# The figures the experiment cards quote as text, derived from the ones above.
rp1, rp2 = t1["Retail-Plus"]["Q1"]["revenue"], t1["Retail-Plus"]["Q2"]["revenue"]
assert round((rp1 - rp2) / rp2 * 100, 1) == 41.7 and rp1 - rp2 == 172_390 and round((rp1 - rp2) / rp1 * 100, 1) == 29.4
assert round(714_890 / 156_790, 1) == 4.6 and round((219_355_841 - 196_599_040) / 1e7, 2) == 2.28
assert round((ch5["booked"] - ch5["lookup"]) / ch5["booked"] * 100, 1) == 40.3 and ch5["booked"] - ch5["every"] == 1_754_930
assert round(ch5["secondInst"] / 1e7, 2) == 7.83

data = {"segments": SEGMENTS, "cities": CITIES, "warehouse": WAREHOUSE, "ch1": ch1, "tree": tree,
        "monthly": monthly, "counts": counts, "lookups": lookups, "ch5": ch5,
        "plus": [int(v) for v in plus["revenue"]],
        "protect": [[int(r["rank"]), r["city"], int(r["revenue"])] for _, r in protect.iterrows()]}

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
  .note{font-size:13.5px;color:var(--muted)}
  .jumped{font-size:13px;color:var(--muted);margin:10px 8px 2px}
  .stats{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:4px 0 8px}
  .stat{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:10px 12px}
  .stat .k{font:700 10.5px var(--sans);letter-spacing:.18em;text-transform:uppercase;color:var(--violet)}
  .stat .v{font:20px/1.2 var(--serif);color:var(--ink);margin-top:2px}
  .stat .d{font-size:13px;color:var(--night)}
  .group{margin:12px 0 4px}
  .group:first-child{margin-top:0}
  .group .q{font-weight:700;color:var(--ink);margin:0 0 4px}
  .group .row{margin-top:4px}
  .said{margin:14px 0 0;font-size:14.5px;color:var(--ink)}
  .verdict.bad{color:var(--rose)}
  .verdict.good{color:var(--green)}
  .line{margin:8px 0 0;color:var(--ink)}
  .line b{color:var(--ink)}
  .ok{color:var(--green);font-weight:700}
  .warn{color:var(--rose);font-weight:700}
  .stack{display:grid;gap:16px;margin-top:16px}
  h3.card-title{font:400 20px/1.3 var(--serif);color:var(--ink);margin:0 0 8px}
  h3.exp-title{font:400 20px/1.3 var(--serif);color:var(--ink);margin:0}
  select{font:15px var(--sans);border:1px solid var(--lilac);border-radius:8px;padding:6px 9px;color:var(--ink);
         background:var(--white);max-width:100%}
  input.yellow{background:#FFF4C2;border-color:#E3C766;max-width:200px}
  .listbox{max-height:300px;overflow-y:auto;border:1px solid var(--line);border-radius:8px}
  .listbox table.t{margin:0}
  tr.hid td{color:var(--soft);text-decoration:line-through}
  td.pass{color:var(--green);font-weight:700}
  table.t td .note{font-weight:400}
  td.hold{color:var(--rose);font-weight:700}
  td.wait{color:var(--violet);font-weight:700}
</style>
</head>
<body>
<header class="hero">
  <span class="kicker">Week 2 &middot; Friday &middot; Companion</span>
  <h1>What can a director open on Monday without a login, change in the room, and still trust?</h1>
  <p class="quote">"Monday's growth review deck needs three things I can open on my laptop without a login: the revenue
    tree by segment for both quarters, the top-fifty protect list with a lookup so I can find any member by id, and one
    number on the front page with its trend. Nothing that needs Python. If a director changes an assumption in the
    room, the sheet must recalculate in front of them."</p>
  <p class="who">Meera's chief of staff, Kalpa Retail, to the data and AI team at Kalpa's Global Capability Centre.
    Kavya Nair, senior analyst, adds: "Everything you built this week has to survive a room that only has Excel."</p>
  <p class="promise">This page is Monday's sheet with its assumptions on switches. The walk climbs the day's six
    chapters, one question each, and every Kalpa number on the page comes from Friday's two exports and the Kalpa
    warehouse. The panels after the walk let you change one assumption at a time, the way a director or a hurried
    analyst would, and watch the tree, the list, the card and the release move. The eight experiment cards run on
    invented records, and each card says so.</p>
</header>

<div class="page">
  <nav class="rail" aria-label="Sections">
    <div class="label">On this page</div>
    <a href="#walk" data-part="walk"><span class="n">01</span>The walk</a>
    <a href="#ch1" data-part="ch1"><span class="n">02</span>Which segment carries it?</a>
    <a href="#ch2" data-part="ch2"><span class="n">03</span>Where did Q2 fall?</a>
    <a href="#ch3" data-part="ch3"><span class="n">04</span>Find any member by id?</a>
    <a href="#ch4" data-part="ch4"><span class="n">05</span>Read right in two minutes?</a>
    <a href="#ch5" data-part="ch5"><span class="n">06</span>What must Excel never do?</a>
    <a href="#ch6" data-part="ch6"><span class="n">07</span>Can a director break it?</a>
    <a href="#checks" data-part="checks"><span class="n">08</span>The Checks tab</a>
    <a href="#experiments" data-part="experiments"><span class="n">09</span>Eight experiments</a>
    <a href="#decision" data-part="decision"><span class="n">10</span>The decision</a>
    <a href="#glossary" data-part="glossary"><span class="n">11</span>Glossary</a>
    <p class="jumped" id="jumped">You are at the top of the page.</p>
  </nav>

  <main>
    <section class="part" id="walk">
      <p class="eyebrow">01 &middot; The guided walk</p>
      <h2>Which six questions take the ask to a file a director can trust, and what number answers each?</h2>
      <p class="lede">Each step is one chapter of the day: its question as the chapter asks it, and its answer with the
        number that settles it. The picture redraws from Friday's exports at every step, and the meter counts the
        chapters climbed.</p>
      <div class="card"><div class="holder" id="walkDraw"></div></div>
      <div class="walk" style="margin-top:16px">
        <div class="card narration" aria-live="polite">
          <div class="step" id="walkStep">Chapter 1 of 6</div>
          <h3 id="walkTitle"></h3>
          <p id="walkText"></p>
          <div class="meter">
            <div class="bar"><div class="fill" id="walkFill"></div></div>
            <div class="legend"><span>chapter 1</span><span id="walkRungs"></span><span>chapter 6</span></div>
          </div>
          <div class="row">
            <button class="btn primary" id="walkNext" type="button">Next</button>
            <button class="btn" id="walkRestart" type="button">Restart the walk</button>
            <button class="btn" id="walkMeter" type="button">What the meter counts</button>
          </div>
        </div>
      </div>
    </section>

    <section class="part" id="ch1">
      <p class="eyebrow">02 &middot; Chapter 1 &middot; The customer table, April to September 2026</p>
      <h2>Which leaf separates the segments, and does the tree multiply back to its revenue?</h2>
      <p class="lede">The chief of staff puts the tree by segment on page two of Monday's deck, and the directors decide
        from it which segment the growth plan talks about. One row of the customer table is one customer who ordered in
        the two quarters, 300 rows for 300 ids, so a Sum adds each customer once. Pick a segment and a way to compute
        revenue per order, and watch whether the three leaves still multiply back to the segment's revenue.</p>
      <div class="grid2">
        <div class="card">
          <div class="group"><p class="q">Which segment's tree is drawn?</p>
            <select id="seg" aria-label="Which segment's tree is drawn"></select></div>
          <div class="group"><p class="q">How is revenue per order computed?</p>
            <div class="row">
              <button class="btn" id="leafSums" type="button" aria-pressed="true">Revenue over orders, a ratio of the sums</button>
              <button class="btn" id="leafAvg" type="button" aria-pressed="false">The average of each customer's own ratio</button>
            </div></div>
          <p class="said" id="c1Said">The tree opens on Business, with revenue per order as the segment's revenue over its
            orders. Change one assumption to see what moves.</p>
          <div class="holder" id="c1Tree" style="margin-top:12px"></div>
        </div>
        <div class="card">
          <div class="stats">
            <div class="stat"><div class="k">Customers</div><div class="v" id="c1Cust"></div><div class="d" id="c1CustD"></div></div>
            <div class="stat"><div class="k">Orders per customer</div><div class="v" id="c1Opc"></div><div class="d" id="c1OpcD"></div></div>
            <div class="stat"><div class="k">Revenue per order</div><div class="v" id="c1Rpo"></div><div class="d" id="c1RpoD"></div></div>
            <div class="stat"><div class="k">Share of revenue</div><div class="v" id="c1Share"></div><div class="d" id="c1ShareD"></div></div>
          </div>
          <div class="formula" id="c1Identity"></div>
          <p class="verdict line" id="c1Verdict"></p>
        </div>
      </div>
      <div class="card" style="margin-top:16px"><div class="holder" id="c1Strip"></div></div>
      <div class="card" style="margin-top:16px">
        <h3 class="card-title">Which way should a director get the tree: a PivotTable, a formula grid, pasted numbers or a live dashboard?</h3>
        <div class="group"><p class="q">What will the directors do with the tree in the room?</p>
          <div class="row">
            <button class="btn" id="wayRe" type="button" aria-pressed="true">Re-slice it by another column</button>
            <button class="btn" id="wayIf" type="button" aria-pressed="false">Change an assumption that must recalculate at once</button>
            <button class="btn" id="wayRead" type="button" aria-pressed="false">Only read it</button>
            <button class="btn" id="wayLogin" type="button" aria-pressed="false">Log in to the warehouse</button>
          </div></div>
        <div class="holder" id="c1Way" style="margin-top:10px"></div>
        <p class="line" id="c1WaySays"></p>
        <p class="said" id="c1WaySaid">This choice opens on directors who re-slice the tree in the room. Pick what
          Monday's directors will do with it.</p>
      </div>
    </section>

    <section class="part" id="ch2">
      <p class="eyebrow">03 &middot; Chapter 2 &middot; The raw export, Q1 against Q2</p>
      <h2>Does the tree for both quarters tie to the warehouse once each order counts once, and where did Q2 fall?</h2>
      <p class="lede">Of Friday's two exports, only the raw one carries order dates, so only it can split the quarters,
        and it holds one row per payment with the order's amount repeated on each. Monday's warehouse queries put Q1, April to June 2026, at
        Rs 10,00,00,000 on 538 orders and Q2, July to September 2026, at Rs 9,84,00,000 on 462 orders, and every number
        on the deck has to tie to those. Change how the pivot counts an order and watch the tie, the bridge and the
        leaves.</p>
      <div class="grid2">
        <div class="card">
          <div class="group"><p class="q">How does the pivot count an order paid in two instalments?</p>
            <div class="row">
              <button class="btn" id="modeRow" type="button" aria-pressed="false">Once per payment row, as the export arrived</button>
              <button class="btn" id="modeDedup" type="button" aria-pressed="false">After Remove Duplicates on every column</button>
              <button class="btn" id="modeOnce" type="button" aria-pressed="true">Once per order, by its first row</button>
            </div></div>
          <p class="said" id="c2Said">The pivot opens counting each order once, by the first row of each order id. Change
            the count to see what the export does to the quarters.</p>
          <div class="group"><p class="q">How many rows will the export carry when it grows?</p>
            <div class="slider"><label for="rows">Rows in the export <b id="rowsV"></b></label>
              <input type="range" id="rows" min="1450" max="145000" step="1450" value="1450"></div>
            <p class="line" id="c2Scale"></p></div>
        </div>
        <div class="card">
          <div class="stats">
            <div class="stat"><div class="k">Q1, April to June</div><div class="v" id="c2Q1"></div><div class="d" id="c2Q1D"></div></div>
            <div class="stat"><div class="k">Q2, July to September</div><div class="v" id="c2Q2"></div><div class="d" id="c2Q2D"></div></div>
            <div class="stat"><div class="k">Q2 against Q1</div><div class="v" id="c2Chg"></div><div class="d" id="c2ChgD"></div></div>
            <div class="stat"><div class="k">Rows against orders</div><div class="v" id="c2Rows"></div><div class="d" id="c2RowsD"></div></div>
          </div>
          <div class="strip" id="c2Tie"><b class="tag">Does the tree tie to the warehouse?</b><span id="c2TieText"></span></div>
        </div>
      </div>
      <div class="card" style="margin-top:16px"><div class="holder" id="c2Bridge"></div></div>
      <div class="card" style="margin-top:16px">
        <h3 class="card-title">Which segment and which leaf moved from Q1 to Q2?</h3>
        <div class="holder" id="c2Table"></div><p class="note" id="c2TableNote"></p></div>
    </section>

    <section class="part" id="ch3">
      <p class="eyebrow">04 &middot; Chapter 3 &middot; The customer table, Retail-Plus</p>
      <h2>Which fifty members make the protect list, and does the lookup answer for the member the chief of staff typed?</h2>
      <p class="lede">The head of Retail-Plus sends the fifty members on the list a retention offer, and the chief of
        staff reads a member's line aloud when a director names one. The list is the 106 Retail-Plus members sorted by
        revenue across the two quarters, with the top fifty kept. Pick an id and a match type, and read the id the
        sheet returned beside the id you asked for.</p>
      <div class="grid2">
        <div class="card">
          <div class="group"><p class="q">Which member id does the chief of staff type?</p>
            <select id="lookId" aria-label="Which member id the chief of staff types">
              <option value="C-0152">C-0152, at the top of the list</option>
              <option value="C-0194">C-0194, a member on the list</option>
              <option value="C-0195">C-0195, a member with no orders and so no row</option>
              <option value="C-0999">C-0999, an id past the end of the table</option>
            </select></div>
          <div class="group"><p class="q">Which match type does the lookup use?</p>
            <div class="row">
              <button class="btn" id="matchExact" type="button" aria-pressed="true">Exact, with a not-found path</button>
              <button class="btn" id="matchApprox" type="button" aria-pressed="false">Approximate, the fourth argument left out</button>
            </div></div>
          <div class="formula" id="c3Formula"></div>
          <p class="said" id="c3Said">The lookup opens on C-0152 with an exact match. Try an id the table does not hold.</p>
        </div>
        <div class="card">
          <p class="verdict line" id="c3Answer"></p>
          <p class="line" id="c3Check"></p>
          <p class="line" id="c3Second"></p>
          <div class="stats" style="margin-top:12px">
            <div class="stat"><div class="k">On the list</div><div class="v">50 of 106</div><div class="d">Retail-Plus members, top fifty by revenue</div></div>
            <div class="stat"><div class="k">The cut-off</div><div class="v" id="c3Cut"></div><div class="d" id="c3CutD"></div></div>
          </div>
        </div>
      </div>
      <div class="card" style="margin-top:16px"><div class="holder" id="c3Strip"></div></div>
    </section>

    <section class="part" id="ch4">
      <p class="eyebrow">05 &middot; Chapter 4 &middot; The front-page card, from the raw export</p>
      <h2>What does the front-page card say, and how will a director read it in two minutes?</h2>
      <p class="lede">Meera and the directors read the front page first and may read nothing else, and the chief of staff
        presents it and answers for it. Pick the card's form, its scope and the quarter its change is divided by, then
        read the card the way a director would. The card reads the count chosen in chapter 2's panel, so a tree that does
        not tie holds the card too.</p>
      <div class="grid2">
        <div class="card">
          <div class="group"><p class="q">Which form does the card take?</p>
            <div class="row">
              <button class="btn" id="formA" type="button" aria-pressed="false">a) The total</button>
              <button class="btn" id="formB" type="button" aria-pressed="false">b) The quarter</button>
              <button class="btn" id="formC" type="button" aria-pressed="false">c) The quarter against the last</button>
              <button class="btn" id="formD" type="button" aria-pressed="true">d) c, with its sentence and its trend</button>
            </div></div>
          <div class="group"><p class="q">Which segments does the card cover?</p>
            <select id="scope" aria-label="Which segments the card covers">
              <option>All segments</option><option>All except Business</option><option>Retail-Plus</option>
              <option>Retail-Core</option><option>Student</option><option>Business</option>
            </select></div>
          <div class="group"><p class="q">Which quarter is the change divided by?</p>
            <div class="row">
              <button class="btn" id="baseQ1" type="button" aria-pressed="true">Q1, the earlier quarter</button>
              <button class="btn" id="baseQ2" type="button" aria-pressed="false">Q2, by mistake</button>
            </div></div>
          <p class="said" id="c4Said">The card opens in form d for all segments, with its change measured on Q1.</p>
        </div>
        <div class="card">
          <p class="verdict line" id="c4Card"></p>
          <p class="line" id="c4Sentence"></p>
          <p class="line" id="c4Reads"></p>
          <p class="line" id="c4Check"></p>
        </div>
      </div>
      <div class="card" style="margin-top:16px"><div class="holder" id="c4Trend"></div></div>
    </section>

    <section class="part" id="ch5">
      <p class="eyebrow">06 &middot; Chapter 5 &middot; The operating rule</p>
      <h2>Where does each of the week's steps belong, and what happens when a lookup does the join?</h2>
      <p class="lede">Kavya signs the team's operating rule, and Anand Iyer, the finance controller, has an analyst who
        audits every number Finance relies on. Booked against collected, Tuesday's report for Anand, is the test case,
        because it needs a join of one order to several payments. Change how collected is computed and which export the
        workbook holds, then place each of the week's steps.</p>
      <div class="grid2">
        <div class="card">
          <div class="group"><p class="q">How is collected computed for each order?</p>
            <div class="row">
              <button class="btn" id="colLookup" type="button" aria-pressed="false">A lookup fetches the order's paid amount</button>
              <button class="btn" id="colSum" type="button" aria-pressed="true">Every payment for the order is added once</button>
            </div></div>
          <div class="group"><p class="q">Which export does the workbook hold?</p>
            <div class="row">
              <button class="btn" id="expToday" type="button" aria-pressed="true">Today's export</button>
              <button class="btn" id="expEarly" type="button" aria-pressed="false">An export pulled a week early</button>
            </div></div>
          <div class="group"><p class="q">Which of the week's steps do you place?</p>
            <select id="step" aria-label="Which of the week's steps you place"></select></div>
          <p class="said" id="c5Said">Collected opens with every payment added once, on today's export.</p>
        </div>
        <div class="card">
          <div class="stats">
            <div class="stat"><div class="k">Booked</div><div class="v" id="c5Booked"></div><div class="d">the orders' value, each order once</div></div>
            <div class="stat"><div class="k">Collected</div><div class="v" id="c5Coll"></div><div class="d" id="c5CollD"></div></div>
            <div class="stat"><div class="k">Short of booked</div><div class="v" id="c5Short"></div><div class="d" id="c5ShortD"></div></div>
            <div class="stat"><div class="k">Two-row orders</div><div class="v" id="c5Two"></div><div class="d">orders with two payment rows</div></div>
          </div>
          <div class="strip" id="c5Drift"><b class="tag">Does the drift check pass on this export?</b><span id="c5DriftText"></span></div>
        </div>
      </div>
      <div class="grid2" style="margin-top:16px">
        <div class="card"><div class="holder" id="c5Rule"></div><p class="line" id="c5RuleSays"></p></div>
        <div class="card"><div class="holder" id="c5Bridge"></div></div>
      </div>
    </section>

    <section class="part" id="ch6">
      <p class="eyebrow">07 &middot; Chapter 6 &middot; The director-proof workbook</p>
      <h2>What can a director change in the room, and what does the sheet show when they do?</h2>
      <p class="lede">The chief of staff hands the laptop across the table mid-meeting. The directors filter, sort, type
        and ask what-ifs, and the head of Retail-Plus sizes each city's retention budget from the protect list. Filter
        the list, change the foot, try a voucher, or type a figure over a computed cell, and watch the foot, the cost and
        the Checks panel below.</p>
      <div class="grid2">
        <div class="card">
          <div class="group"><p class="q">Which city does a director filter the protect list to?</p>
            <select id="city" aria-label="Which city a director filters the protect list to"><option>All cities</option></select></div>
          <div class="group"><p class="q">What formula sits at the foot of the list?</p>
            <div class="row">
              <button class="btn" id="footSub" type="button" aria-pressed="true">SUBTOTAL(109), with SUBTOTAL(103) beside it</button>
              <button class="btn" id="footSum" type="button" aria-pressed="false">SUM</button>
            </div></div>
          <div class="group"><p class="q">What voucher does a director try for each member on screen, in rupees?</p>
            <input type="number" class="yellow" id="voucher" min="0" step="50" value="500" aria-label="Voucher per member, in rupees"></div>
          <div class="group"><p class="q">Does a director type a figure over the card's Q2 revenue, in rupees?</p>
            <div class="row">
              <input type="number" id="typed" min="0" step="1" placeholder="nothing typed" aria-label="A figure typed over the card's Q2 revenue" style="max-width:200px">
              <button class="btn" id="typedClear" type="button">Clear the typed figure</button>
            </div></div>
          <p class="said" id="c6Said">The list opens unfiltered, with SUBTOTAL(109) at its foot and a Rs 500 voucher in
            the yellow input.</p>
          <h3 class="card-title" style="margin-top:16px">Which rows of the protect list are on screen?</h3>
          <div class="listbox" id="c6List"></div>
          <p class="note">Each row is a member's rank, city and revenue across the two quarters; the member ids sit in the
            deck pack's Protect tab.</p>
        </div>
        <div class="card">
          <p class="verdict line" id="c6Foot"></p>
          <p class="line" id="c6Check"></p>
          <p class="line" id="c6Second"></p>
          <p class="line" id="c6Cost"></p>
          <div class="holder" id="c6Feet" style="margin-top:10px"></div>
        </div>
      </div>
    </section>

    <section class="part" id="checks">
      <p class="eyebrow">08 &middot; The Checks tab</p>
      <h2>Which of the five checks pass on your settings, and what does the release ship?</h2>
      <p class="lede">Each check compares a number on the sheet with one that comes from somewhere else, and the release
        reads the checks and nothing else. The list's source check compares the customer table with the warehouse; this
        page leaves that comparison to your own run of chapter 3's your-turn cell, so tell it what your run found.</p>
      <div class="grid2">
        <div class="card"><div class="holder" id="checksTable"></div></div>
        <div class="card">
          <div class="group"><p class="q">What did your run of chapter 3's your-turn cell find?</p>
            <div class="row">
              <button class="btn" id="srcUnrun" type="button" aria-pressed="true">I have not run it yet</button>
              <button class="btn" id="srcTies" type="button" aria-pressed="false">The customer table ties</button>
              <button class="btn" id="srcShort" type="button" aria-pressed="false">The customer table falls short</button>
            </div></div>
          <div class="strip" id="releaseStrip"><b class="tag">What does the release ship?</b><span id="release"></span></div>
          <p class="line" id="releaseWhy"></p>
          <div class="row"><button class="btn" id="reset" type="button">Back to the honest sheet</button></div>
          <p class="said" id="checksSaid">Every panel opens at its honest setting, so the checks this page runs all pass.</p>
        </div>
      </div>
    </section>

    <section class="part" id="experiments">
      <p class="eyebrow">09 &middot; Experiment cards</p>
      <h2>What does each of the day's traps do to a number, one change at a time?</h2>
      <p class="lede">Each card is one of the day's traps: a plausible wrong number and the decision it would mislead.
        Card A is the toggle the trainer already runs, and cards B to H follow the chapters from 1 to 6. Every record in
        these cards is invented to isolate one mechanism, and each card's label says so. Read the situation and the
        hypothesis, decide what you expect, then run.</p>
      <div class="grid2">
        <article class="card exp">
          <div class="part-label">Experiment A &middot; chapter 2 &middot; invented rows</div>
          <h3 class="exp-title">Does Remove Duplicates bring a payment export back to one row per order?</h3>
          <p><b>Situation.</b> Three invented orders worth Rs 7,000 together sit on five rows of a payment export: an order
            of Rs 1,000 on one row, an order of Rs 2,000 paid in two instalments of Rs 1,200 and Rs 800, and an order of
            Rs 4,000 the gateway posted twice. Every row carries its order's amount, so a pivot's Sum reads Rs 13,000.</p>
          <p><b>Hypothesis.</b> Removing the rows that are identical in every column brings the total back to the orders'
            Rs 7,000.</p>
          <p><b>Watch for.</b> How many rows go, and where the middle bar lands against the orders' Rs 7,000.</p>
          <div class="holder" id="expADraw"></div>
          <div class="row">
            <button class="btn" id="expARun" type="button" aria-pressed="false">Remove Duplicates</button>
            <button class="btn" id="expASeq" type="button">Show the sequence</button>
          </div>
          <div class="result" id="expAResult" hidden>
            <p><b>What happened.</b> <span id="expAWhat"></span></p>
            <p><b>Why it matters.</b> An analyst who ran Remove Duplicates believes the export is clean and ships a total
              still inflated by every instalment order. On Friday's export it moved the two quarters only from
              Rs 39,40,95,490 to Rs 39,40,57,740, against the warehouse's Rs 19,84,00,000.</p>
            <p class="rule">Count each order once by its key; removing identical rows leaves every instalment in.</p>
          </div>
          <p class="waiting" id="expAWait">What happened appears here after the run.</p>
        </article>

        <article class="card exp">
          <div class="part-label">Experiment B &middot; chapter 1 &middot; invented buyers</div>
          <h3 class="exp-title">Does an average of each buyer's revenue per order give the tree's leaf?</h3>
          <p><b>Situation.</b> Three invented corporate buyers spent Rs 30,00,000 on 12 orders. One placed a single order
            of Rs 6,00,000, one placed 3 orders worth Rs 9,00,000, and one placed 8 orders worth Rs 15,00,000. The tree
            needs revenue per order.</p>
          <p><b>Hypothesis.</b> Averaging the three buyers' own revenue per order gives a leaf that is too high, because
            the buyer with one large order counts as much as the buyer with eight, so the tree no longer multiplies back
            to Rs 30,00,000.</p>
          <p><b>Watch for.</b> The outlined bar in the bridge: rupees the averaged leaf adds that the buyers never spent.</p>
          <div class="holder" id="expBDraw"></div>
          <div class="row">
            <button class="btn" id="expBRun" type="button" aria-pressed="false">Average each buyer's ratio</button>
            <button class="btn" id="expBSeq" type="button">Show the sequence</button>
          </div>
          <div class="result" id="expBResult" hidden>
            <p><b>What happened.</b> <span id="expBWhat"></span></p>
            <p><b>Why it matters.</b> On Friday's customer table the same averaging reads Business at Rs 11,66,786 an order
              against Rs 10,45,740 from revenue over orders, and the tree comes back Rs 2.28 crore above what Business
              sold.</p>
            <p class="rule">Make every leaf a ratio of the sums, and multiply the tree back before it goes on a page.</p>
          </div>
          <p class="waiting" id="expBWait">What happened appears here after the run.</p>
        </article>

        <article class="card exp">
          <div class="part-label">Experiment C &middot; chapter 3 &middot; invented ids</div>
          <h3 class="exp-title">What does each lookup return for an id the table does not hold?</h3>
          <p><b>Situation.</b> Eight invented members, C-0401 to C-0409, sit sorted by id with C-0405 missing. The chief of
            staff types C-0405.</p>
          <p><b>Hypothesis.</b> An exact match reports the id as missing, and an approximate match returns C-0404's row
            with nothing on the screen to say it belongs to somebody else.</p>
          <p><b>Watch for.</b> Which id each lookup returned, and whether either answer carries a warning.</p>
          <div class="formula" id="expCWork">MATCH("C-0405", ids, ?)</div>
          <div class="row">
            <button class="btn" id="expCRun" type="button" aria-pressed="false">Run both lookups</button>
            <button class="btn" id="expCSeq" type="button">Show the sequence</button>
          </div>
          <div class="result" id="expCResult" hidden>
            <p><b>What happened.</b> <span id="expCWhat"></span></p>
            <p><b>Why it matters.</b> On Friday's customer table the same default hands C-0195, a member with no row, the
              revenue of C-0194, Rs 16,740 at rank 15 on the protect list, and a retention offer goes to someone who placed
              no order between April and September.</p>
            <p class="rule">Test every lookup with an id you know is missing, and print the id returned beside the id asked.</p>
          </div>
          <p class="waiting" id="expCWait">What happened appears here after the run.</p>
        </article>

        <article class="card exp">
          <div class="part-label">Experiment D &middot; chapter 4 &middot; invented numbers</div>
          <h3 class="exp-title">Which quarter should a change be divided by?</h3>
          <p><b>Situation.</b> An invented segment fell from Rs 500 in one quarter to Rs 400 in the next, and the front
            page has room for one percentage.</p>
          <p><b>Hypothesis.</b> Measured on the earlier quarter the fall is 20 percent; divided by the later quarter by
            mistake it reads 25 percent.</p>
          <p><b>Watch for.</b> Which denominator each formula uses, and how far apart the two percentages land.</p>
          <div class="formula" id="expDWork">(400 - 500) / ? = ?</div>
          <div class="row">
            <button class="btn" id="expDRun" type="button" aria-pressed="false">Compute both</button>
            <button class="btn" id="expDSeq" type="button">Show the sequence</button>
          </div>
          <div class="result" id="expDResult" hidden>
            <p><b>What happened.</b> <span id="expDWhat"></span></p>
            <p><b>Why it matters.</b> On Friday's numbers the same slip turns Retail-Plus's fall of 29.4 percent into
              41.7 percent, on a fall of Rs 1.72 lakh that is 0.4 percent of company revenue.</p>
            <p class="rule">Measure a change on the period you compare against, and print its rupee base beside it.</p>
          </div>
          <p class="waiting" id="expDWait">What happened appears here after the run.</p>
        </article>

        <article class="card exp">
          <div class="part-label">Experiment E &middot; chapter 5 &middot; invented orders</div>
          <h3 class="exp-title">Does a lookup add up all of an order's payments?</h3>
          <p><b>Situation.</b> Three invented orders are booked at Rs 10,000, Rs 20,000 and Rs 6,000. The Rs 10,000 order
            was paid in one payment, the Rs 20,000 order in two instalments of Rs 12,000 and Rs 8,000, and the Rs 6,000
            order is unpaid, so the payments sit on four rows.</p>
          <p><b>Hypothesis.</b> A lookup on the order id fetches one payment per order, so it reports Rs 8,000 less
            collected than the customers paid.</p>
          <p><b>Watch for.</b> The outstanding bar, and whether it shrinks to the one unpaid order.</p>
          <div class="holder" id="expEDraw"></div>
          <div class="row">
            <button class="btn" id="expERun" type="button" aria-pressed="false">Add every payment instead</button>
            <button class="btn" id="expESeq" type="button">Show the sequence</button>
          </div>
          <div class="result" id="expEResult" hidden>
            <p><b>What happened.</b> <span id="expEWhat"></span></p>
            <p><b>Why it matters.</b> On Friday's export the lookup reports Rs 11,83,81,974 collected and Rs 8.00 crore
              outstanding, 40.3 percent of booked; adding every payment once leaves Rs 17,54,930 short, 0.9 percent,
              exactly the orders nobody has paid for, and Anand's team would have chased Rs 7.83 crore that customers
              had already paid.</p>
            <p class="rule">Where one order meets several payments, add them; the join lives in the warehouse, and a SUMIFS
              in the sheet only checks it.</p>
          </div>
          <p class="waiting" id="expEWait">What happened appears here after the run.</p>
        </article>

        <article class="card exp">
          <div class="part-label">Experiment F &middot; chapter 6 &middot; invented members</div>
          <h3 class="exp-title">What does the foot of a filtered list add?</h3>
          <p><b>Situation.</b> Eight invented members spent Rs 60,000 together, three of them in Mumbai worth Rs 25,500.
            A director filters the list to Mumbai.</p>
          <p><b>Hypothesis.</b> SUM at the foot still reads Rs 60,000, and SUBTOTAL(109) reads the Rs 25,500 the director
            can see.</p>
          <p><b>Watch for.</b> The struck-through rows, and which foot follows them.</p>
          <div class="holder" id="expFTable"></div>
          <div class="row">
            <button class="btn" id="expFRun" type="button" aria-pressed="false">Filter to Mumbai</button>
            <button class="btn" id="expFSeq" type="button">Show the sequence</button>
          </div>
          <div class="result" id="expFResult" hidden>
            <p><b>What happened.</b> <span id="expFWhat"></span></p>
            <p><b>Why it matters.</b> On Friday's protect list, filtered to Mumbai, SUM reads Rs 7,14,890 while the eleven
              members on screen spent Rs 1,56,790, so a city budget sized on the foot is 4.6 times too big.</p>
            <p class="rule">Write the foot of a list a director will filter as SUBTOTAL(109), with SUBTOTAL(103) beside it
              counting the rows on screen.</p>
          </div>
          <p class="waiting" id="expFWait">What happened appears here after the run.</p>
        </article>

        <article class="card exp">
          <div class="part-label">Experiment G &middot; chapter 6 &middot; invented records</div>
          <h3 class="exp-title">What does the release hold when a list's source falls short of its control total?</h3>
          <p><b>Situation.</b> An invented list is built from five invented records worth Rs 11,000 together, and the system
            that owns them gives a control total of Rs 12,200. The checks on the tree, the lookup and the foot all pass.</p>
          <p><b>Hypothesis.</b> Four of the five checks pass, and the release still holds the list while the rest ships,
            because the failing check stands behind the list.</p>
          <p><b>Watch for.</b> The source line, and which part the release sentence names.</p>
          <div class="holder" id="expGTable"></div>
          <div class="row">
            <button class="btn" id="expGRun" type="button" aria-pressed="false">Run the five checks</button>
            <button class="btn" id="expGSeq" type="button">Show the sequence</button>
          </div>
          <div class="result" id="expGResult" hidden>
            <p><b>What happened.</b> <span id="expGWhat"></span></p>
            <p><b>Why it matters.</b> A list built on a short source can leave out a member the head of Retail-Plus would
              have protected, and a release that counted passing checks would have shipped it.</p>
            <p class="rule">Hold a part when a check behind it fails, name the check, and ship what ties.</p>
          </div>
          <p class="waiting" id="expGWait">What happened appears here after the run.</p>
        </article>

        <article class="card exp">
          <div class="part-label">Experiment H &middot; chapter 6 &middot; an invented sheet</div>
          <h3 class="exp-title">What does ISFORMULA see when a director types over a formula?</h3>
          <p><b>Situation.</b> An invented two-cell sheet holds Q1 at Rs 500 and Q2 at Rs 400, each a formula that reads
            the export, and a card says down 20.0 percent. A director types Rs 450 over Q2 so the card looks better.</p>
          <p><b>Hypothesis.</b> The card moves to the typed figure with no error anywhere, and only ISFORMULA notices that
            Q2 has stopped being a formula.</p>
          <p><b>Watch for.</b> The ISFORMULA column, and what the release does with one FALSE.</p>
          <div class="holder" id="expHTable"></div>
          <div class="row">
            <button class="btn" id="expHRun" type="button" aria-pressed="false">Type Rs 450 over Q2</button>
            <button class="btn" id="expHSeq" type="button">Show the sequence</button>
          </div>
          <div class="result" id="expHResult" hidden>
            <p><b>What happened.</b> <span id="expHWhat"></span></p>
            <p><b>Why it matters.</b> A typed figure has no source, the next refresh wipes it without a trace, and nobody
              can say which other numbers it moved, so the release cannot vouch for any of them.</p>
            <p class="rule">Every cell outside the yellow inputs holds a formula, and ISFORMULA on the Checks tab proves it.</p>
          </div>
          <p class="waiting" id="expHWait">What happened appears here after the run.</p>
        </article>
      </div>
    </section>

    <section class="part" id="decision">
      <p class="eyebrow">10 &middot; The decision card</p>
      <h2>Which file should the chief of staff take into Monday's meeting?</h2>
      <p class="lede">Pick the way you would hand the workbook to a room of directors and read Kavya's review of it. The
        tree lights the branch you picked.</p>
      <div class="card"><div class="holder" id="decTree"></div></div>
      <div class="card" style="margin-top:16px">
        <div class="row" style="margin-top:0">
          <button class="btn" id="decProtect" type="button" aria-pressed="false">Protect every cell</button>
          <button class="btn" id="decPdf" type="button" aria-pressed="false">Send a PDF</button>
          <button class="btn" id="decYellow" type="button" aria-pressed="false">Yellow inputs, formulas and a Checks tab</button>
          <button class="btn" id="decCopy" type="button" aria-pressed="false">A copy for each director</button>
        </div>
        <div class="strip" id="decWhy"><b class="tag">Kavya's review</b><span id="decWhyText">Pick an answer above to see
          Kavya's review of it, the review the file gets before it reaches the chief of staff.</span></div>
        <div class="strip good"><b class="tag">Kavya's review of the file that goes</b>"Give the room a sheet it can
          change and cannot break silently: inputs in yellow, every other cell a formula, SUBTOTAL at every foot, and a
          Checks tab whose release holds whatever does not tie. A director who filters, sorts or asks a what-if should see
          a number move, and never a number lie."</div>
      </div>
    </section>

    <section class="part" id="glossary">
      <p class="eyebrow">11 &middot; Glossary</p>
      <h2>Which words does the day use, and where did each first matter?</h2>
      <div class="card">
        <dl class="gloss">
          <dt>Revenue</dt><dd>Revenue is booked order value in rupees: every order at the price charged, whatever became
            of it.<span class="where">Chapter 1, the metric at stake.</span></dd>
          <dt>Revenue tree</dt><dd>The tree splits revenue into three leaves that multiply back to it: customers, times
            orders per customer, times revenue per order.<span class="where">Chapter 1.</span></dd>
          <dt>Segment</dt><dd>Kalpa's segments are Retail-Core, the everyday shoppers; Retail-Plus, the paid membership
            tier; Business, the corporate buyers invoiced in large amounts; and Student.<span class="where">Chapter 1.</span></dd>
          <dt>Grain</dt><dd>The grain is what one row of a table stands for: a customer in the customer table, a payment in
            the raw export, an order in the warehouse.<span class="where">Chapter 1, question 1; chapter 2, the trap.</span></dd>
          <dt>Ratio of sums</dt><dd>A leaf is the pivot's Sum of one field over its Sum of another, so the tree multiplies
            back; an average of each customer's own ratio gives every customer one vote, and the tree stops multiplying
            back.<span class="where">Chapter 1, the trap and its fix.</span></dd>
          <dt>PivotTable</dt><dd>A PivotTable summarises a table by the fields dragged into it and recalculates when someone
            presses Refresh; a SUMIFS formula recalculates the moment an input changes.<span class="where">Chapter 1, the
            options.</span></dd>
          <dt>Quarter</dt><dd>Kalpa's Q1 is April to June 2026 and Q2 is July to September 2026; in Excel the column is
            =IF(MONTH(date)&lt;=6,"Q1","Q2").<span class="where">Chapter 2, question 1.</span></dd>
          <dt>First-row flag</dt><dd>=IF(COUNTIF($A$2:A2,A2)=1,1,0) puts 1 on the first row of each order id, so a sum over
            the flagged rows counts each order once.<span class="where">Chapter 2, the fix.</span></dd>
          <dt>Remove Duplicates</dt><dd>Excel's Remove Duplicates deletes rows that are identical in every ticked column, so
            two instalments of one order, which differ in the amount paid, both stay.<span class="where">Chapter 2, the
            trap.</span></dd>
          <dt>Control total</dt><dd>A control total is a number someone upstream owns, such as the warehouse's
            Rs 10,00,00,000 for Q1, and a sheet ties when it reproduces it to the rupee.<span class="where">Chapter 2, the
            second route; chapter 6, the Checks tab.</span></dd>
          <dt>Warehouse</dt><dd>The warehouse is Kalpa's Postgres database, one row per order, which Monday's queries read
            and every number on the deck ties back to.<span class="where">Chapter 2.</span></dd>
          <dt>Protect list and cut-off</dt><dd>The protect list is the fifty Retail-Plus members with the highest revenue
            across the two quarters, and its cut-off is the fiftieth member's revenue, Rs 8,580.<span class="where">Chapter
            3, question 1.</span></dd>
          <dt>Exact and approximate match</dt><dd>An exact match finds the id or says it is missing; an approximate match,
            VLOOKUP's default when its fourth argument is left out, returns the largest id not above the one asked
            for.<span class="where">Chapter 3, the trap.</span></dd>
          <dt>XLOOKUP, or IFERROR with INDEX and MATCH</dt><dd>XLOOKUP is exact by default and takes a not-found message as
            its fourth argument in Excel 2021, 2024 and Microsoft 365; IFERROR around INDEX and MATCH does the same in Excel
            2016, Excel 2019 and LibreOffice.<span class="where">Chapter 3, the options.</span></dd>
          <dt>Period, comparison and base</dt><dd>A front-page number carries the months it covers, what it is compared
            with, and the base its change is divided by, which is the earlier period.<span class="where">Chapter 4.</span></dd>
          <dt>Scope and share</dt><dd>The scope is the segments a card covers, printed on the card, and the share is the
            scope's revenue over the company's in the same quarter.<span class="where">Chapter 4, the trend and the
            base.</span></dd>
          <dt>Percentage points</dt><dd>A change in a rate is quoted in points: the consumer segments' share of revenue
            fell from 0.99 percent in Q1 to 0.83 percent in Q2, 0.16 points, which is a 16 percent fall in the
            share.<span class="where">Chapter 4, depth.</span></dd>
          <dt>Booked and collected</dt><dd>Booked is the value of the orders; collected is the money received against them,
            which needs every payment of every order added once.<span class="where">Chapter 5.</span></dd>
          <dt>Join</dt><dd>A join matches each order with its payments; where one order meets several payments, a lookup
            takes the first and a sum takes them all.<span class="where">Chapter 5, the trap.</span></dd>
          <dt>Operating rule</dt><dd>The warehouse owns the number and every join, dedupe and rank Finance relies on; pandas
            owns the analyst's iteration until Finance relies on it; the workbook owns the last mile on an export that
            ties, and nobody types over the source.<span class="where">Chapter 5.</span></dd>
          <dt>Drift check</dt><dd>Every time the workbook recalculates, its Checks tab compares the sheet's orders and
            booked revenue per quarter with the warehouse's control totals, which travel on a small tab beside each
            export, and a mismatch holds the deck until someone knows why.<span class="where">Chapter
            5, question 6.</span></dd>
          <dt>Yellow input</dt><dd>A yellow cell holds an assumption a director may change, and every other cell holds a
            formula that reads it.<span class="where">Chapter 6.</span></dd>
          <dt>SUBTOTAL(109) and SUBTOTAL(103)</dt><dd>SUBTOTAL(109) adds only the rows on screen and SUBTOTAL(103) counts
            them; both leave out rows a filter or a hand has hidden.<span class="where">Chapter 6, the fix.</span></dd>
          <dt>ISFORMULA</dt><dd>ISFORMULA returns TRUE for a cell that holds a formula, so the Checks tab can find a figure
            typed over one.<span class="where">Chapter 6, the Checks tab.</span></dd>
          <dt>Checks tab and release</dt><dd>The Checks tab holds five PASS or HOLD lines, each comparing the sheet with
            something outside it, and one release sentence that holds the part behind any failing check.<span
            class="where">Chapter 6.</span></dd>
        </dl>
      </div>
      <p class="foot">Week 2, Friday. Two workbooks sit beside this page in demos/: the deck pack,
        C2_W02_D05_deck_pack_STUDENT.xlsx, holds the three deliverables and the Checks tab as live formulas over the two
        exports, and the decision tool, C2_W02_D05_decision_tool_STUDENT.xlsx, hides one formula defect on each of its six
        chapter tabs. The Kalpa figures on this page are computed from Friday's two exports; the records on the
        experiment cards are invented. Kalpa Retail and everyone in it are fictional. The page stores nothing and calls no
        network.</p>
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
  var K = window.C2K, R = K.rupees;
  var D = JSON.parse(document.getElementById("data").textContent);
  function $(id) { return document.getElementById(id); }
  var MONTHS = ["Apr", "May", "Jun", "Jul", "Aug", "Sep"];
  var CONSUMER = ["Retail-Core", "Retail-Plus", "Student"];
  function money(n) {
    var a = Math.abs(n), s = n < 0 ? "-" : "";
    if (a >= 1e7) return s + "Rs " + (a / 1e7).toFixed(2) + " crore";
    if (a >= 1e5) return s + "Rs " + (a / 1e5).toFixed(2) + " lakh";
    return R(n);
  }
  function pct(x, d) { var p = Math.pow(10, d === undefined ? 1 : d); return (Math.round(x * p) / p).toFixed(d === undefined ? 1 : d); }
  function count(n) { return Math.round(n).toLocaleString("en-US"); }
  function share(x) { return x < 0.1 ? x.toFixed(2) : pct(x); }
  function pctOf(x) { return Math.abs(x) > 100 ? "more than 10,000" : pct(Math.abs(x) * 100); }
  function scopeWords(scope) {
    return scope === "All segments" ? "all segments" : scope === "All except Business" ? "all segments except Business" : scope;
  }
  function sum(a) { return a.reduce(function (t, x) { return t + x; }, 0); }
  function press(group, on) { group.forEach(function (id) { $(id).setAttribute("aria-pressed", String(id === on)); }); }
  function esc(s) { return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;"); }

  /* ---------------------------------------------------------------- the state every panel reads */
  var HONEST = { seg: "Business", leaf: "sums", way: "re", mode: "once", rows: 1450, id: "C-0152", match: "exact",
                 form: "d", scope: "All segments", base: "Q1", collect: "every", exp: "today", step: 0,
                 city: "All cities", foot: "sub", voucher: 500, typed: null, source: "unrun" };
  var S = JSON.parse(JSON.stringify(HONEST));

  /* ---------------------------------------------------------------- the rail */
  var rail = document.querySelectorAll(".rail a");
  Array.prototype.forEach.call(rail, function (a) {
    a.addEventListener("click", function () {
      Array.prototype.forEach.call(rail, function (b) { b.classList.toggle("on", b === a); });
      $("jumped").textContent = "You are reading section " + a.querySelector(".n").textContent + ": " +
        a.textContent.replace(/^\d+/, "").trim();
    });
  });
  if ("IntersectionObserver" in window) {
    var seen = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        Array.prototype.forEach.call(rail, function (b) { b.classList.toggle("on", b.dataset.part === e.target.id); });
      });
    }, { rootMargin: "-20% 0px -70% 0px" });
    Array.prototype.forEach.call(document.querySelectorAll("section.part"), function (s) { seen.observe(s); });
  }

  /* ---------------------------------------------------------------- the popup */
  function openPop(title, svg, note) {
    $("seqTitle").textContent = title;
    K.draw("seqBody", svg);
    $("seqNote").textContent = note;
    var d = $("seqDialog");
    if (typeof d.showModal === "function") d.showModal(); else d.setAttribute("open", "");
  }
  function openSeq(title, lanes, messages, note) { openPop(title, K.sequence(lanes, messages, { laneWidth: 200 }), note); }
  $("seqClose").addEventListener("click", function () { $("seqDialog").close(); });

  /* ---------------------------------------------------------------- sums over the exports */
  function key() { return S.exp + ":" + S.mode; }
  function T(seg, q, k) { return D.tree[k || key()][seg][q]; }
  function scopeSegs(scope) {
    if (scope === "All segments") return D.segments;
    if (scope === "All except Business") return D.segments.filter(function (s) { return s !== "Business"; });
    return [scope];
  }
  function scopeQ(scope, q, field, k) {
    return scopeSegs(scope).reduce(function (t, s) { return t + T(s, q, k)[field]; }, 0);
  }
  function scopeMonths(scope, k) {
    return MONTHS.map(function (_, i) {
      return scopeSegs(scope).reduce(function (t, s) { return t + D.monthly[k || key()][s][i]; }, 0);
    });
  }
  function floorOf(start, moves) {
    var run = start, low = start, high = start;
    moves.forEach(function (m) { run += m[1]; low = Math.min(low, run); high = Math.max(high, run); });
    var unit = Math.pow(10, Math.floor(Math.log10(Math.max(1, high - low))));
    return Math.max(0, Math.floor((low - unit * 0.2) / unit) * unit);
  }
  function niceTop(max) {
    var raw = max * 1.04 / 4, p = Math.pow(10, Math.floor(Math.log10(raw))), steps = [1, 1.2, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10];
    for (var i = 0; i < steps.length; i++) if (steps[i] * p >= raw) return 4 * steps[i] * p;
    return 40 * p;
  }
  function treeTies() {
    return ["Q1", "Q2"].every(function (q) {
      return scopeQ("All segments", q, "revenue") === D.warehouse[q].revenue &&
             scopeQ("All segments", q, "orders") === D.warehouse[q].orders;
    });
  }

  /* ---------------------------------------------------------------- the walk */
  var PILLS = ["Which segment carries it?", "Where did Q2 fall?", "Find any member by id?", "Read right in two minutes?",
               "What must Excel never do?", "Can a director break it?"];
  var C1 = D.ch1, P = C1["Retail-Plus"], CORE = C1["Retail-Core"], B = C1.Business;
  function leafOf(x) { return { opc: x.orders / x.customers, rpo: x.revenue / x.orders, rpc: x.revenue / x.customers }; }
  var LP = leafOf(P), LC = leafOf(CORE);
  var ONCE = "today:once";
  var Q1 = D.warehouse.Q1.revenue, Q2 = D.warehouse.Q2.revenue;
  var SEG_MOVES = D.segments.map(function (s) { return [s, T(s, "Q2", ONCE).revenue - T(s, "Q1", ONCE).revenue]; });
  var COMPANY = scopeMonths("All segments", ONCE);
  var PROTECT_SUM = sum(D.protect.map(function (r) { return r[2]; }));
  var MUMBAI = D.protect.filter(function (r) { return r[1] === "Mumbai"; });
  var MUMBAI_SUM = sum(MUMBAI.map(function (r) { return r[2]; }));
  var C5 = D.ch5;
  var WALK = [
    { t: "Which segment carries Kalpa's revenue, and which leaf of the tree separates the segments?",
      x: "Business carries " + pct(B.share) + " percent of the half-year's revenue in the customer table: " + B.customers +
         " corporate buyers, " + R(B.revenue) + ". Between the two consumer tiers the basket does the separating: a Retail-Plus order is worth " +
         R(LP.rpo) + " against Retail-Core's " + R(LC.rpo) + ", " + pct((LP.rpo / LC.rpo - 1) * 100) +
         " percent more, while orders per customer differ by " + pct((LP.opc / LC.opc - 1) * 100, 0) + " percent (" + LP.opc.toFixed(2) +
         " against " + LC.opc.toFixed(2) + "). Each leaf is a ratio of the pivot's own sums, so the tree multiplies back to its revenue.",
      d: function () {
        return K.driverTree({ label: "revenue per customer", note: "Retail-Plus " + R(LP.rpc) + " against Retail-Core " + R(LC.rpc) + ", " + pct((LP.rpc / LC.rpc - 1) * 100, 0) + "% more", kind: "plain",
          children: [{ label: "orders per customer", note: LP.opc.toFixed(2) + " against " + LC.opc.toFixed(2) + ", " + pct((LP.opc / LC.opc - 1) * 100, 0) + "% more" },
                     { label: "revenue per order", note: R(LP.rpo) + " against " + R(LC.rpo) + ", " + pct((LP.rpo / LC.rpo - 1) * 100) + "% more", kind: "lit" }] },
          { width: 250, title: "Retail-Plus against Retail-Core, April to September: the basket separates the tiers" });
      } },
    { t: "How much did revenue fall from Q1 to Q2, and in which segment and which leaf?",
      x: "Counted once per order, revenue fell " + R(Q1 - Q2) + ", " + pct((Q1 - Q2) / Q1 * 100) + " percent, from " + money(Q1) + " in Q1 to " +
         money(Q2) + " in Q2, and the export ties to the warehouse to the rupee. In rupees Business carries " + R(-SEG_MOVES[0][1]) +
         " of the fall; the steepest fall is Retail-Plus, down " + pct(-SEG_MOVES[2][1] / T("Retail-Plus", "Q1", ONCE).revenue * 100) +
         " percent, because orders per customer fell from " + (T("Retail-Plus", "Q1", ONCE).orders / T("Retail-Plus", "Q1", ONCE).customers).toFixed(2) +
         " to " + (T("Retail-Plus", "Q2", ONCE).orders / T("Retail-Plus", "Q2", ONCE).customers).toFixed(2) +
         " while the basket grew. A pivot on every payment row would have read " +
         R(scopeQ("All segments", "Q1", "revenue", "today:row") + scopeQ("All segments", "Q2", "revenue", "today:row")) + " for the two quarters.",
      d: function () {
        return K.bridge(["Q1, April to June", Q1], SEG_MOVES, { fmt: money, lo: 98000000, lit: [2], endLabel: "Q2, July to September",
          title: "Q1 to Q2 by segment, each order counted once; Retail-Plus outlined" });
      } },
    { t: "Which fifty Retail-Plus members go on the protect list, and when the chief of staff types an id, does the sheet answer for that member?",
      x: "Fifty of the " + D.plus.length + " Retail-Plus members make the list, from C-0152 at " + R(D.plus[0]) + " down to a cut-off of " + R(D.plus[49]) +
         "; the fifty-first spent " + R(D.plus[50]) + ", so no tie crosses the line, and the fifty spent " + R(PROTECT_SUM) +
         " together. When the chief of staff types C-0195, a member with no orders and so no row, VLOOKUP with its fourth argument left out returns C-0194's " +
         R(D.lookups["C-0195"].approx[3]) + " at rank " + D.lookups["C-0195"].approx[4] + "; an exact match with a not-found path says \"not in the table\".",
      d: function () {
        return K.strip(D.plus, { fmt: R, width: 760, hi: 30000, lit: D.plus.slice(0, 50).map(function (_, i) { return i; }),
          markers: [["cut-off, rank 50", D.plus[49], "good"], ["what C-0195 gets back, rank 15", D.lookups["C-0195"].approx[3], "bad"]],
          title: "The 106 Retail-Plus members by revenue; the fifty on the list are dark" });
      } },
    { t: "What must sit beside the front-page number so a director reads it right in two minutes?",
      x: "The card reads: \"All segments, Q2, July to September 2026: " + money(Q2) + ", down " + pct((Q1 - Q2) / Q1 * 100) + " percent on Q1, April to June 2026 (" +
         money(Q1) + "); 100.0 percent of company revenue in Q2.\" A bare \"Revenue " + money(Q1 + Q2) + "\" is two quarters added, and a director who remembers Q1 reads it as up " +
         pct(Q2 / Q1 * 100) + " percent. \"Retail-Plus down 29.4 percent\" needs its base beside it: a fall of " +
         money(-SEG_MOVES[2][1]) + " on " + money(T("Retail-Plus", "Q1", ONCE).revenue) + ", 0.4 percent of company revenue.",
      d: function () {
        return K.line(MONTHS, [["company revenue, each order once", COMPANY, "plain"]], { fmt: money, width: 760,
          title: "The trend beside the number: company revenue by month, April to September 2026" });
      } },
    { t: "Which of the week's steps belong in the workbook, which must never be done there, and how do the two stay in step?",
      x: "Tuesday's booked against collected must never be done in the sheet: a lookup that fetches each order's paid amount takes the first payment of the " +
         C5.twoRow + " two-row orders and reports " + R(C5.lookup) + " collected, " + money(C5.booked - C5.lookup) + " outstanding. Adding every payment once gives " +
         R(C5.every) + ", " + R(C5.booked - C5.every) + " short, " + pct((C5.booked - C5.every) / C5.booked * 100) +
         " percent, exactly the orders nobody has paid for. The warehouse owns every join, dedupe and rank, pandas the analyst's iteration and the workbook the last mile, with a drift check live on the Checks tab.",
      d: function () {
        return K.bridge(["collected, by lookup", C5.lookup], [["second instalments of 400 orders", C5.secondInst]],
          { fmt: money, endLabel: "collected, every payment once", lit: [0], title: "What the lookup left out of collected" });
      } },
    { t: "When a director takes the workbook in the room, what can they break, and which checks catch it before anyone reads a wrong number?",
      x: "Filtered to Mumbai, a foot written as SUM still reads " + R(PROTECT_SUM) + " while the " + MUMBAI.length + " members on screen spent " + R(MUMBAI_SUM) +
         ", so a budget sized on it is " + pct(PROTECT_SUM / MUMBAI_SUM) + " times too big. SUBTOTAL(109) follows the filter and SUBTOTAL(103) beside it counts " +
         MUMBAI.length + " of 50; a director's Rs 500 voucher goes in a yellow input and costs " + R(500 * MUMBAI.length) +
         " for Mumbai. The Checks tab runs five checks, and its release holds whatever a failing check stands behind.",
      d: function () {
        return K.columns(["filtered to Mumbai"], [["SUM at the foot", [PROTECT_SUM]], ["SUBTOTAL(109) at the foot", [MUMBAI_SUM]]],
          { fmt: R, width: 520, title: "The protect list filtered to Mumbai: one list, two feet" });
      } }
  ];
  var walkAt = 0;
  function showWalk(extra) {
    var w = WALK[walkAt];
    K.draw("walkDraw", w.d());
    $("walkStep").textContent = "Chapter " + (walkAt + 1) + " of 6" + (extra || "");
    $("walkTitle").textContent = w.t;
    $("walkText").textContent = w.x;
    $("walkFill").style.width = (100 * (walkAt + 1) / 6) + "%";
    $("walkRungs").textContent = (walkAt + 1) + " of 6 chapters climbed";
    $("walkNext").textContent = walkAt === WALK.length - 1 ? "Back to chapter 1" : "Next";
  }
  $("walkNext").addEventListener("click", function () { walkAt = (walkAt + 1) % WALK.length; showWalk(); });
  $("walkRestart").addEventListener("click", function () { walkAt = 0; showWalk(", restarted"); });
  $("walkMeter").addEventListener("click", function () {
    openPop("What the meter counts", K.ladder(PILLS, walkAt, { width: 420 }),
      "The meter counts the day's six chapters, each a harder question on the same two exports, and the lit rung is chapter " +
      (walkAt + 1) + ", the one the walk is on.");
  });
  showWalk();

  /* ---------------------------------------------------------------- chapter 1 */
  D.segments.forEach(function (s) { var o = document.createElement("option"); o.textContent = s; $("seg").appendChild(o); });
  var WAYS = {
    re: ["Hand them a PivotTable with each leaf beside it as a ratio of the pivot's sums. On this table that is 1 pivot and 8 leaf formulas, a director can re-slice by any of the 6 columns in seconds, and it recalculates when someone presses Refresh.", 0],
    if: ["Hand them a SUMIFS grid. It takes 12 formulas reading 3,600 cells and a city split adds 72 more, and every formula recalculates the moment a director's input changes, where a PivotTable waits for Refresh.", 1],
    read: ["Paste the tied values. That takes 0 formulas, and it holds only while nobody asks a new question in the room.", 2],
    login: ["A live dashboard on the warehouse answers anything, and every director needs a login, which the chief of staff's brief rules out.", 3]
  };
  function ch1() {
    var x = C1[S.seg], L = leafOf(x), avg = S.leaf === "avg", rpo = avg ? x.avg : L.rpo;
    var back = x.orders * rpo, off = back - x.revenue, ties = Math.abs(off) < 1;
    $("c1Cust").textContent = String(x.customers);
    $("c1CustD").textContent = x.orders + " orders between them";
    $("c1Opc").textContent = L.opc.toFixed(2);
    $("c1OpcD").textContent = x.orders + " orders over " + x.customers + " customers";
    $("c1Rpo").textContent = R(rpo);
    $("c1RpoD").textContent = avg ? "the average of " + x.customers + " customers' own ratios" : money(x.revenue) + " over " + x.orders + " orders";
    $("c1Share").textContent = share(x.share) + "%";
    $("c1ShareD").textContent = money(x.revenue) + ", its share of the table's revenue";
    $("c1Identity").textContent = avg
      ? x.customers + " customers × (" + x.orders + " / " + x.customers + ") orders each × " + R(rpo) + " an order comes to " + money(back)
      : x.customers + " customers × (" + x.orders + " / " + x.customers + ") orders each × (" + R(x.revenue) + " / " + x.orders + ") an order = " + R(back);
    var v = $("c1Verdict");
    v.className = "verdict line " + (ties ? "good" : "bad");
    v.textContent = ties
      ? "The leaves multiply back to " + S.seg + "'s " + R(x.revenue) + " to the rupee, so the tree can go on page two."
      : "The leaves multiply back to " + money(back) + ", " + money(Math.abs(off)) + (off > 0 ? " more" : " less") + " than " + S.seg +
        " sold: the averaged leaf gives every customer one vote, whatever they bought. Multiply back before the tree goes on a page.";
    K.draw("c1Tree", K.driverTree({ label: S.seg + " revenue", note: R(x.revenue), kind: "plain", children: [
      { label: "customers", note: String(x.customers) },
      { label: "orders per customer", note: L.opc.toFixed(2) },
      { label: "revenue per order", note: R(rpo) + (avg ? ", averaged" : ""), kind: ties ? "good" : "bad" }] },
      { width: 200, title: "The tree for " + S.seg + ": three leaves that multiply to its revenue" }));
    var lo = Math.min.apply(null, x.ratios), hi = Math.max.apply(null, x.ratios);
    K.draw("c1Strip", K.strip(x.ratios, { fmt: money, width: 880, hi: niceTop(hi),
      markers: [["revenue over orders", L.rpo, "good"], ["averaged", x.avg, avg ? "bad" : "plain"]],
      title: "Each " + S.seg + " customer's revenue per order, " + money(lo) + " to " + money(hi) }));
  }
  function ch1Way() {
    var w = WAYS[S.way], k = function (i) { return i === w[1] ? "good" : "plain"; };
    K.draw("c1Way", K.tree({ label: "What will a director do with the tree?", kind: "lit", branches: [
      ["", { label: "a) PivotTable\nto re-slice: 1 pivot and 8 leaf formulas, recalculating on Refresh", kind: k(0) }],
      ["", { label: "b) SUMIFS grid\nfor a what-if: 12 formulas over 3,600 cells, recalculating at once", kind: k(1) }],
      ["", { label: "c) Pasted values\nto read only: 0 formulas, slicing nothing", kind: k(2) }],
      ["", { label: "d) Live dashboard\nanswers anything, with a login for every director", kind: k(3) }]] },
      { width: 200, title: "Four ways to hand over the tree, sized on the 300-row customer table" }));
    $("c1WaySays").textContent = w[0];
  }
  var C1SAY = {
    leafSums: ["leaf", "sums", "Revenue per order is now the segment's revenue over its orders, a ratio of the pivot's own sums."],
    leafAvg: ["leaf", "avg", "Revenue per order is now the average of each customer's own revenue over orders, which a pivot's Average gives."]
  };
  Object.keys(C1SAY).forEach(function (id) {
    $(id).addEventListener("click", function () {
      S.leaf = C1SAY[id][1]; press(["leafSums", "leafAvg"], id); $("c1Said").textContent = C1SAY[id][2]; ch1();
    });
  });
  $("seg").addEventListener("change", function () {
    S.seg = this.value; $("c1Said").textContent = "The tree now draws " + S.seg + ", " + C1[S.seg].customers + " customers in the customer table."; ch1();
  });
  var WAYIDS = { wayRe: "re", wayIf: "if", wayRead: "read", wayLogin: "login" };
  var WAYSAY = { re: "The directors will re-slice the tree by city or channel in the room.",
                 if: "A director will change an assumption, and the tree has to recalculate in front of the room.",
                 read: "The directors will only read the tree and ask nothing new of it.",
                 login: "Every director will log in to the warehouse, which the brief rules out on Monday." };
  Object.keys(WAYIDS).forEach(function (id) {
    $(id).addEventListener("click", function () {
      S.way = WAYIDS[id]; press(Object.keys(WAYIDS), id); $("c1WaySaid").textContent = WAYSAY[S.way]; ch1Way();
    });
  });

  /* ---------------------------------------------------------------- chapter 2 */
  var MODE_NAME = { row: "once per payment row", dedup: "after Remove Duplicates", once: "once per order" };
  function ch2() {
    var k = key(), c = D.counts[k];
    var q1 = scopeQ("All segments", "Q1", "revenue"), q2 = scopeQ("All segments", "Q2", "revenue");
    var o1 = scopeQ("All segments", "Q1", "orders"), o2 = scopeQ("All segments", "Q2", "orders");
    var ties = treeTies();
    $("c2Q1").textContent = money(q1);
    $("c2Q1D").textContent = R(q1) + " on " + count(o1) + (S.mode === "once" ? " orders" : " rows");
    $("c2Q2").textContent = money(q2);
    $("c2Q2D").textContent = R(q2) + " on " + count(o2) + (S.mode === "once" ? " orders" : " rows");
    $("c2Chg").textContent = (q2 < q1 ? "down " : "up ") + pct(Math.abs(q2 - q1) / q1 * 100) + "%";
    $("c2ChgD").textContent = "measured on Q1, " + MODE_NAME[S.mode];
    $("c2Rows").textContent = count(c.rows) + " / " + count(c.orders);
    $("c2RowsD").textContent = "rows counted against distinct order ids";
    var strip = $("c2Tie");
    strip.className = "strip " + (ties ? "good" : "bad");
    var wq = D.warehouse;
    $("c2TieText").textContent = ties
      ? "Yes. Q1 " + R(q1) + " on " + o1 + " orders and Q2 " + R(q2) + " on " + o2 + " orders match the warehouse to the rupee and to the order."
      : (S.exp === "early" && S.mode === "once"
        ? "No. Q2 reads " + R(q2) + " on " + o2 + " orders against the warehouse's " + R(wq.Q2.revenue) + " on " + wq.Q2.orders +
          ": every row is real, and the export was pulled before the last week of September arrived."
        : "No. The two quarters add " + R(q1 + q2) + " on " + count(c.rows) + " rows against the warehouse's " + R(wq.Q1.revenue + wq.Q2.revenue) +
          " on " + count(wq.Q1.orders + wq.Q2.orders) + " orders. Rows against distinct order ids, " + count(c.rows) + " against " + count(c.orders) +
          ", say some orders are counted more than once.");
    var moves2 = D.segments.map(function (s) { return [s, T(s, "Q2").revenue - T(s, "Q1").revenue]; });
    K.draw("c2Bridge", K.bridge(["Q1", q1], moves2,
      { fmt: money, lo: floorOf(q1, moves2), lit: [2], endLabel: "Q2", width: 880,
        title: "Q1 to Q2 by segment, counted " + MODE_NAME[S.mode] + (S.exp === "early" ? ", on the early export" : "") }));
    var html = '<table class="t"><tr><th>Segment</th><th class="num">Customers Q1 to Q2</th><th class="num">Orders each</th><th class="num">Revenue per order</th><th class="num">Change</th></tr>';
    D.segments.forEach(function (s) {
      var a = T(s, "Q1"), b = T(s, "Q2");
      html += "<tr><td>" + s + '</td><td class="num">' + a.customers + " to " + b.customers + '</td><td class="num">' +
        (a.orders / a.customers).toFixed(2) + " to " + (b.orders / b.customers).toFixed(2) + '</td><td class="num">' +
        R(a.revenue / a.orders) + " to " + R(b.revenue / b.orders) + '</td><td class="num">' +
        (b.revenue < a.revenue ? "-" : "+") + pct(Math.abs(b.revenue - a.revenue) / a.revenue * 100) + "%</td></tr>";
    });
    $("c2Table").innerHTML = html + "</table>";
    $("c2TableNote").textContent = S.mode === "once"
      ? "Each order counted once: Retail-Plus fell because its members ordered less often, while its basket grew."
      : "Counted " + MODE_NAME[S.mode] + ", a pivot's Count of customer_id counts rows, so every customer is a row, orders each read 1.00 and the tree says nothing about frequency.";
  }
  function ch2Scale() {
    var n = Number($("rows").value);
    $("rowsV").textContent = count(n);
    var running = n * (n + 1) / 2;
    $("c2Scale").textContent = "A running COUNTIF compares each row with every row above it, so " + count(n) + " rows make " +
      count(running) + " comparisons" + (running >= 1e9 ? ", about " + pct(running / 1e9) + " billion" : "") +
      ". Sorting by order id and comparing each row with the one above makes " + count(n - 1) +
      ", and an export at the order grain from the warehouse makes the flag unnecessary.";
  }
  var MODEIDS = { modeRow: "row", modeDedup: "dedup", modeOnce: "once" };
  var MODESAY = {
    row: "The pivot now adds every payment row, so an order paid in two instalments, or posted twice by the gateway, counts twice.",
    dedup: "The pivot now runs on the export after Remove Duplicates, which took out only the 50 rows identical in every column.",
    once: "The pivot now counts each order once, by the first row of its order id."
  };
  Object.keys(MODEIDS).forEach(function (id) {
    $(id).addEventListener("click", function () {
      S.mode = MODEIDS[id]; press(Object.keys(MODEIDS), id); $("c2Said").textContent = MODESAY[S.mode]; everything();
    });
  });
  $("rows").addEventListener("input", ch2Scale);

  /* ---------------------------------------------------------------- chapter 3 */
  function lookupRow(id, match) { var l = D.lookups[id]; return match === "exact" ? l.exact : l.approx; }
  function ch3() {
    var id = S.id, row = lookupRow(id, S.match), l = D.lookups[id];
    $("c3Formula").textContent = S.match === "exact"
      ? '=IFERROR(INDEX(E:E, MATCH("' + id + '", A:A, 0)), "not in the table")'
      : '=VLOOKUP("' + id + '", A2:F301, 5)';
    var ans = $("c3Answer"), wrong = row && row[0] !== id;
    ans.className = "verdict line " + (wrong ? "bad" : "good");
    if (!row) ans.textContent = id + " is not in the table. Say so, and check the export before anyone answers.";
    else if (wrong) ans.textContent = "The sheet shows " + R(row[3]) + (row[4] && row[4] <= 50 ? ", rank " + row[4] + " on the protect list" : ", a " + row[1] + " customer in " + row[2]) +
      ". That is " + row[0] + "'s row, returned for " + id + ", and nothing on the screen is red.";
    else ans.textContent = id + ": " + row[1] + ", " + row[2] + ", " + R(row[3]) + (row[4] && row[4] <= 50 ? ", rank " + row[4] + " of 50 on the protect list." : ", not on the protect list.");
    $("c3Check").innerHTML = "<b>The check.</b> Asked " + id + ", returned " + (row ? row[0] : "\"not in the table\"") + ": " +
      (wrong ? '<span class="warn">a different member, so the lookup is wrong.</span>'
             : (row ? '<span class="ok">the lookup answers for the id asked.</span>' : '<span class="ok">the lookup says so when an id is missing.</span>'));
    var agree = l.count === 0 ? !row : !!row && row[0] === id;
    $("c3Second").innerHTML = "<b>A second route.</b> =COUNTIF(A:A, \"" + id + "\") finds " + l.count + (l.count === 1 ? " row" : " rows") +
      (l.count === 1 ? " and =SUMIFS(E:E, A:A, \"" + id + "\") adds " + R(l.exact[3]) : "") + ", which " +
      (agree ? '<span class="ok">agrees with the lookup.</span>' : '<span class="warn">disagrees with the lookup, so one of the two is wrong.</span>');
    $("c3Cut").textContent = R(D.plus[49]);
    $("c3CutD").textContent = "the fiftieth member's revenue; the fifty-first spent " + R(D.plus[50]) + ", and the fifty spent " + R(PROTECT_SUM) + " together";
    var cuts = [["cut-off, rank 50", D.plus[49], "good"]];
    if (row && row[4] && row[4] <= 106 && row[1] === "Retail-Plus") cuts.push([(wrong ? "returned for " + id : id) + ", rank " + row[4], row[3], wrong ? "bad" : "plain"]);
    K.draw("c3Strip", K.strip(D.plus, { fmt: R, width: 880, hi: 30000, lit: D.plus.slice(0, 50).map(function (_, i) { return i; }), markers: cuts,
      title: "The 106 Retail-Plus members by revenue across the two quarters; the fifty on the protect list are dark" }));
  }
  $("lookId").addEventListener("change", function () {
    S.id = this.value; $("c3Said").textContent = "The chief of staff now types " + S.id + "."; ch3(); checks();
  });
  var MATCHIDS = { matchExact: "exact", matchApprox: "approx" };
  Object.keys(MATCHIDS).forEach(function (id) {
    $(id).addEventListener("click", function () {
      S.match = MATCHIDS[id]; press(Object.keys(MATCHIDS), id);
      $("c3Said").textContent = S.match === "exact" ? "The lookup now matches exactly and says when an id is missing."
        : "The lookup now matches approximately: a missing id comes back as the row just below it. Try C-0195 or C-0999.";
      ch3(); checks();
    });
  });

  /* ---------------------------------------------------------------- chapter 4 */
  function cardNumbers() {
    var q1 = scopeQ(S.scope, "Q1", "revenue"), q2 = scopeQ(S.scope, "Q2", "revenue");
    if (S.typed !== null) q2 = S.typed;
    var comp = scopeQ("All segments", "Q2", "revenue") - (S.typed !== null ? scopeQ(S.scope, "Q2", "revenue") - S.typed : 0);
    return { q1: q1, q2: q2, comp: comp, change: (q2 - q1) / (S.base === "Q1" ? q1 : q2) };
  }
  function ch4() {
    var n = cardNumbers(), ties = treeTies(), card = $("c4Card");
    var dir = n.change < 0 ? "down " : "up ";
    var full = S.scope + ", Q2, July to September 2026: " + money(n.q2) + ", " + dir + pctOf(n.change) + " percent on Q1, April to June 2026 (" + money(n.q1) + ")";
    var text;
    if (!ties) text = "Hold the card: it reads a tree that does not tie to the warehouse, counted " + MODE_NAME[S.mode] + (S.exp === "early" ? " on the early export" : "") + ".";
    else if (S.form === "a") text = "Revenue " + money(n.q1 + n.q2);
    else if (S.form === "b") text = "Q2 revenue " + money(n.q2);
    else if (S.form === "c") text = full + ".";
    else text = full + "; " + share(n.q2 / n.comp * 100) + " percent of company revenue in Q2.";
    card.className = "verdict line " + (!ties || S.form === "a" || S.base === "Q2" ? "bad" : "good");
    card.textContent = text;
    var segs = scopeSegs(S.scope);
    var sentence = "";
    if (ties && S.form === "d") {
      if (segs.length > 1) {
        var moves = segs.map(function (s) { var a = T(s, "Q1").revenue, b = T(s, "Q2").revenue; return [s, b - a, (b - a) / a]; });
        var worstRs = moves.slice().sort(function (a, b) { return a[1] - b[1]; })[0];
        var worstPct = moves.slice().sort(function (a, b) { return a[2] - b[2]; })[0];
        var risers = moves.filter(function (m) { return m[1] > 0; }).map(function (m) { return m[0]; });
        var net = n.q1 - scopeQ(S.scope, "Q2", "revenue");
        if (net <= 0 || worstRs[1] >= 0) sentence = "Where the change sits: " + scopeWords(S.scope) + " rose by " + money(-net) + " from Q1 to Q2.";
        else sentence = "Where the change sits: in rupees the largest fall is " + worstRs[0] + "'s " + money(-worstRs[1]) +
          (-worstRs[1] <= net ? ", out of a net fall of " + money(net) : ", more than the net fall of " + money(net) + " because " + risers.join(" and ") + " rose") +
          ", and the steepest fall is " + worstPct[0] + ", down " + pct(-worstPct[2] * 100) + " percent.";
      } else {
        var a = T(segs[0], "Q1"), b = T(segs[0], "Q2");
        sentence = "Where the change sits: customers who ordered went from " + a.customers + " to " + b.customers + ", orders each from " +
          (a.orders / a.customers).toFixed(2) + " to " + (b.orders / b.customers).toFixed(2) + ", and the basket from " + R(a.revenue / a.orders) + " to " + R(b.revenue / b.orders) + ".";
      }
    }
    $("c4Sentence").textContent = sentence;
    var reads;
    if (!ties) reads = "A director reads nothing on this card until the tree ties, because the card inherits whatever the tree counted.";
    else if (S.form === "a") reads = "A director who remembers Q1's " + money(n.q1) + " reads " + money(n.q1 + n.q2) + " as up " + pct(((n.q1 + n.q2) / n.q1 - 1) * 100) +
      " percent in a quarter, when it is two quarters added; the card needs its period and its comparison.";
    else if (S.form === "b") reads = "A director has to bring Q1's figure from memory to know whether " + money(n.q2) + " is good news, so the comparison belongs on the card.";
    else if (S.form === "c") reads = "Nothing is left to memory, and the director's next question, where the change sits, is still open.";
    else reads = "Nothing is left to memory: the card carries its period, its comparison and its base, the sentence says where the change sits, and the trend shows the six months.";
    $("c4Reads").textContent = reads;
    var right = (n.q2 - n.q1) / n.q1;
    $("c4Check").innerHTML = "<b>The check.</b> " + (S.base === "Q1"
      ? '<span class="ok">The change is measured on Q1, the earlier quarter.</span>'
      : '<span class="warn">The change is divided by Q2, the later quarter: it reads ' + pctOf(n.change) + " percent where it moved " + pctOf(right) + " percent.</span>");
    if (S.form === "d" && ties) {
      K.draw("c4Trend", K.line(MONTHS, [[S.scope, scopeMonths(S.scope), S.typed !== null ? "bad" : "plain"]], { fmt: money, width: 860,
        title: "The trend beside the number: " + S.scope + ", revenue by month, April to September 2026" }));
    } else {
      $("c4Trend").innerHTML = '<p class="note">' + (ties ? "The trend sits beside the card in form d; forms a to c leave it off." : "The trend is held with the card until the tree ties.") + "</p>";
    }
  }
  var FORMIDS = { formA: "a", formB: "b", formC: "c", formD: "d" };
  var FORMSAY = { a: "The card now shows the half-year's total in big type.", b: "The card now shows Q2 alone.",
                  c: "The card now shows Q2 against Q1 with both periods named.", d: "The card now shows Q2 against Q1 with its base, its sentence and its trend." };
  Object.keys(FORMIDS).forEach(function (id) {
    $(id).addEventListener("click", function () { S.form = FORMIDS[id]; press(Object.keys(FORMIDS), id); $("c4Said").textContent = FORMSAY[S.form]; ch4(); });
  });
  $("scope").addEventListener("change", function () { S.scope = this.value; $("c4Said").textContent = "The card now covers " + scopeWords(S.scope) + "."; ch4(); });
  var BASEIDS = { baseQ1: "Q1", baseQ2: "Q2" };
  Object.keys(BASEIDS).forEach(function (id) {
    $(id).addEventListener("click", function () {
      S.base = BASEIDS[id]; press(Object.keys(BASEIDS), id);
      $("c4Said").textContent = S.base === "Q1" ? "The change is now divided by Q1, the quarter it is compared against." : "The change is now divided by Q2, the later quarter, as a hurried formula does.";
      ch4();
    });
  });

  /* ---------------------------------------------------------------- chapter 5 */
  var STEPS = [
    ["Monday's tree by segment and quarter", 0, "Finance audits it, and a GROUP BY anyone can rerun computes it."],
    ["Friday's count of each order once, the first-row flag", 0, "A grain fix is cleaning, so the export should arrive at the order grain and the first-row flag becomes a check."],
    ["Tuesday's booked against collected", 0, "It joins one order to several payments, which a lookup gets wrong and a query gets right."],
    ["Wednesday's top fifty with a tie rule", 0, "Finance and Marketing both rely on the rank, so it lives where it can be rerun and audited."],
    ["Thursday's customer table", 1, "It is the analyst's weekly iteration, and it stays in pandas until Finance relies on it."],
    ["Friday's pivot, lookup and card", 2, "Presenting, slicing and looking up on an export that ties is the workbook's last mile."],
    ["A director's what-if in the room", 2, "An assumption goes in a labelled yellow input, and the actual keeps its formula."]
  ];
  STEPS.forEach(function (s, i) { var o = document.createElement("option"); o.value = String(i); o.textContent = s[0]; $("step").appendChild(o); });
  function ch5() {
    var coll = S.collect === "every" ? C5.every : C5.lookup, short = C5.booked - coll;
    $("c5Booked").textContent = money(C5.booked);
    $("c5Coll").textContent = money(coll);
    $("c5CollD").textContent = S.collect === "every" ? R(C5.every) + ", every payment added once" : R(C5.lookup) + ", one payment per order";
    $("c5Short").textContent = money(short);
    $("c5ShortD").textContent = R(short) + ", " + pct(short / C5.booked * 100) + " percent of booked";
    $("c5Two").textContent = String(C5.twoRow);
    var moves5 = [[S.collect === "every" ? "orders nobody has paid for" : "outstanding, says the lookup", -short]];
    K.draw("c5Bridge", K.bridge(["booked", C5.booked], moves5, { fmt: money, lo: floorOf(C5.booked, moves5), lit: S.collect === "every" ? [] : [0],
      endLabel: S.collect === "every" ? "collected, every payment once" : "collected, by lookup",
      title: S.collect === "every" ? "Booked against collected, every payment added once" : "Booked against collected, one payment per order by lookup" }));
    var k = S.exp + ":once", w = D.warehouse, t2 = scopeQ("All segments", "Q2", "revenue", k), o2 = scopeQ("All segments", "Q2", "orders", k);
    var t1 = scopeQ("All segments", "Q1", "revenue", k), o1 = scopeQ("All segments", "Q1", "orders", k);
    var ok = t1 === w.Q1.revenue && o1 === w.Q1.orders && t2 === w.Q2.revenue && o2 === w.Q2.orders;
    $("c5Drift").className = "strip " + (ok ? "good" : "bad");
    $("c5DriftText").textContent = ok
      ? "Yes. The export's quarters, counted once, match the warehouse: Q1 " + R(t1) + " on " + o1 + " orders and Q2 " + R(t2) + " on " + o2 + " orders, so the deck ships."
      : "No. Q2 reads " + R(t2) + " on " + o2 + " orders against the warehouse's " + R(w.Q2.revenue) + " on " + w.Q2.orders +
        ". Every row in the early export is real, and the check holds the deck until someone pulls a fresh export.";
    var st = STEPS[S.step], kinds = ["plain", "plain", "plain"];
    kinds[st[1]] = "lit";
    K.draw("c5Rule", K.vflow(["the warehouse\nevery join, dedupe and rank Finance relies on", "pandas\nthe analyst's iteration until Finance relies on it",
      "the workbook\npresenting, slicing, looking up and what-ifs"], st[1],
      { width: 300, kinds: kinds, edges: ["queried and exported", "an export that ties"], title: "Where it lives: " + st[0] }));
    $("c5RuleSays").textContent = st[0] + " lives in " + ["the warehouse", "pandas", "the workbook"][st[1]] + ". " + st[2];
  }
  var COLIDS = { colLookup: "lookup", colSum: "every" };
  Object.keys(COLIDS).forEach(function (id) {
    $(id).addEventListener("click", function () {
      S.collect = COLIDS[id]; press(Object.keys(COLIDS), id);
      $("c5Said").textContent = S.collect === "every" ? "Collected now adds every payment of each order once, as SUMIFS over the export's distinct rows or the warehouse's join does."
        : "Collected now comes from a lookup that stops at the first payment row of each order.";
      ch5();
    });
  });
  var EXPIDS = { expToday: "today", expEarly: "early" };
  Object.keys(EXPIDS).forEach(function (id) {
    $(id).addEventListener("click", function () {
      S.exp = EXPIDS[id]; press(Object.keys(EXPIDS), id);
      $("c5Said").textContent = S.exp === "today" ? "The workbook now holds today's export." : "The workbook now holds an export pulled a week early, before the last week of September arrived.";
      everything();
    });
  });
  $("step").addEventListener("change", function () { S.step = Number(this.value); $("c5Said").textContent = "You are placing: " + STEPS[S.step][0] + "."; ch5(); });

  /* ---------------------------------------------------------------- chapter 6 */
  D.cities.forEach(function (c) { var o = document.createElement("option"); o.textContent = c; $("city").appendChild(o); });
  function visibleRows() { return D.protect.filter(function (r) { return S.city === "All cities" || r[1] === S.city; }); }
  function ch6() {
    var vis = visibleRows(), visSum = sum(vis.map(function (r) { return r[2]; }));
    var foot = S.foot === "sub" ? visSum : PROTECT_SUM, adds = S.foot === "sub" ? vis.length : 50;
    var follows = adds === vis.length;
    var f = $("c6Foot");
    f.className = "verdict line " + (follows ? "good" : "bad");
    f.textContent = (S.foot === "sub" ? "=SUBTOTAL(109, E2:E51)" : "=SUM(E2:E51)") + " reads " + R(foot) + " with " + vis.length + " of 50 members on screen" +
      (S.city === "All cities" ? "." : ", filtered to " + S.city + ".");
    $("c6Check").innerHTML = "<b>The check.</b> Rows on screen, by =SUBTOTAL(103, A2:A51): " + vis.length + "; rows the foot adds: " + adds + ". " +
      (follows ? '<span class="ok">The foot follows the filter.</span>' : '<span class="warn">The foot adds ' + (adds - vis.length) + " rows nobody can see; a budget sized on it is " + pct(foot / visSum) + " times too big.</span>");
    $("c6Second").innerHTML = "<b>A second route.</b> " + (S.city === "All cities" ? "=SUM over the whole list" : '=SUMIFS(E2:E51, C2:C51, "' + S.city + '")') + " ignores the filter and gives " +
      R(visSum) + ", which " + (foot === visSum ? '<span class="ok">agrees with the foot.</span>' : '<span class="warn">disagrees with the foot.</span>');
    var v = isFinite(S.voucher) && S.voucher >= 0 ? S.voucher : 0;
    $("c6Cost").innerHTML = "<b>The what-if.</b> =B1*SUBTOTAL(103, A2:A51), with the voucher in yellow B1: " + R(v) + " × " + vis.length + " = <b>" + R(v * vis.length) +
      "</b> for the members on screen" + (vis.length < 50 ? ", where the whole list would cost " + R(v * 50) : "") +
      ". The list's figures never change, because the assumption sits beside them.";
    K.draw("c6Feet", K.columns(["the foot, " + (S.foot === "sub" ? "SUBTOTAL(109)" : "SUM"), "what the rows on screen spent"], [[S.city, [foot, visSum]]],
      { fmt: R, lit: follows ? [] : [0], width: 420, title: "The foot against the rows on screen, " + S.city }));
    var html = '<table class="t"><tr><th class="num">Rank</th><th>City</th><th class="num">Revenue</th></tr>';
    D.protect.forEach(function (r) {
      var shown = S.city === "All cities" || r[1] === S.city;
      html += '<tr class="' + (shown ? "" : "hid") + '"><td class="num">' + r[0] + "</td><td>" + r[1] + '</td><td class="num">' + R(r[2]) + "</td></tr>";
    });
    html += '<tr><td colspan="2"><b>' + (S.foot === "sub" ? "SUBTOTAL(109)" : "SUM") + '</b></td><td class="num"><b>' + R(foot) + "</b></td></tr></table>";
    $("c6List").innerHTML = html;
  }
  $("city").addEventListener("change", function () {
    S.city = this.value;
    $("c6Said").textContent = S.city === "All cities" ? "A director cleared the filter, so all fifty members are on screen." : "A director filtered the list to " + S.city + ".";
    ch6(); checks();
  });
  var FOOTIDS = { footSub: "sub", footSum: "sum" };
  Object.keys(FOOTIDS).forEach(function (id) {
    $(id).addEventListener("click", function () {
      S.foot = FOOTIDS[id]; press(Object.keys(FOOTIDS), id);
      $("c6Said").textContent = S.foot === "sub" ? "The foot is now SUBTOTAL(109), which adds only the rows on screen." : "The foot is now SUM, which adds all fifty rows whatever the filter hides. Pick a city to see it.";
      ch6(); checks();
    });
  });
  $("voucher").addEventListener("input", function () {
    S.voucher = Number(this.value); $("c6Said").textContent = "A director typed a voucher of " + R(S.voucher || 0) + " into the yellow input."; ch6();
  });
  $("typed").addEventListener("input", function () {
    S.typed = this.value === "" ? null : Number(this.value);
    $("c6Said").textContent = S.typed === null ? "Nothing is typed over the card's Q2 revenue." : "A director typed " + R(S.typed) + " over the card's Q2 revenue, a cell that held a formula.";
    ch4(); checks();
  });
  $("typedClear").addEventListener("click", function () {
    var had = S.typed !== null;
    S.typed = null; $("typed").value = "";
    $("c6Said").textContent = had ? "The typed figure is cleared, and the card's Q2 revenue reads its formula again." : "There was no typed figure to clear; Q2 already reads its formula.";
    ch4(); checks();
  });

  /* ---------------------------------------------------------------- the Checks tab */
  function checks() {
    var ties = treeTies();
    var c195 = lookupRow("C-0195", S.match), honest = !c195;
    var vis = visibleRows(), adds = S.foot === "sub" ? vis.length : 50, follows = adds === vis.length;
    var typed = S.typed !== null;
    var rows = [
      ["The tree ties", "The tree's two quarters against the warehouse's", ties ? "pass" : "hold",
       ties ? "Q1 and Q2 match the warehouse to the rupee." : "The quarters do not match the warehouse."],
      ["The list's source ties", "The customer table's orders and revenue against the warehouse's",
       S.source === "unrun" ? "wait" : (S.source === "ties" ? "pass" : "hold"),
       S.source === "unrun" ? "Not run on this page; your run decides it." : (S.source === "ties" ? "Your run says it ties." : "Your run says it falls short.")],
      ["The lookup is honest", "The lookup's answer for C-0195, an id known to be missing", honest ? "pass" : "hold",
       honest ? "It says not in the table." : "It returned " + c195[0] + "'s row."],
      ["The foot follows the filter", "SUBTOTAL(103) against the rows the foot adds", follows ? "pass" : "hold",
       vis.length + " on screen, " + adds + " added."],
      ["No typed-over formula", "ISFORMULA on every cell outside the yellow inputs", typed ? "hold" : "pass",
       typed ? "The card's Q2 revenue holds a typed figure." : "Every computed cell holds a formula."]
    ];
    var html = '<table class="t"><tr><th>Check</th><th>It compares</th><th>Result</th></tr>';
    rows.forEach(function (r) {
      html += "<tr><td><b>" + r[0] + "</b></td><td>" + r[1] + '</td><td class="' + r[2] + '">' + { pass: "PASS", hold: "HOLD", wait: "YOURS TO RUN" }[r[2]] + "<br><span class=\"note\">" + esc(r[3]) + "</span></td></tr>";
    });
    $("checksTable").innerHTML = html + "</table>";
    var listHeld = rows[1][2] === "hold" || !honest || !follows;
    var text, kind;
    if (typed) { text = "Hold the whole workbook until the typed figure is traced and its formula is back."; kind = "bad"; }
    else if (!ties && listHeld) { text = "Hold everything: the tree and the front page do not tie, and the protect list fails a check behind it."; kind = "bad"; }
    else if (!ties) { text = "Hold the tree and the front page; ship the protect list" + (rows[1][2] === "wait" ? " once its source check passes." : "."); kind = "bad"; }
    else if (listHeld) { text = "Hold the protect list; ship the rest."; kind = "bad"; }
    else if (rows[1][2] === "wait") { text = "The tree and the front page can ship; the protect list ships once its source check passes."; kind = ""; }
    else { text = "Ship everything: the tree, the protect list and the front page."; kind = "good"; }
    $("release").textContent = text;
    $("releaseStrip").className = "strip" + (kind ? " " + kind : "");
    var why = rows.filter(function (r) { return r[2] === "hold"; }).map(function (r) { return r[0].charAt(0).toLowerCase() + r[0].slice(1); });
    $("releaseWhy").textContent = why.length ? "The checks that read HOLD: \"" + why.join("\", \"") + "\"." : "No check this page runs reads HOLD.";
  }
  var SRCIDS = { srcUnrun: "unrun", srcTies: "ties", srcShort: "short" };
  var SRCSAY = { unrun: "You have not told the page what your run found, so the source line waits for you.",
                 ties: "You told the page your run ties, so the source line reads PASS.",
                 short: "You told the page your run falls short, so the source line reads HOLD." };
  Object.keys(SRCIDS).forEach(function (id) {
    $(id).addEventListener("click", function () { S.source = SRCIDS[id]; press(Object.keys(SRCIDS), id); $("checksSaid").textContent = SRCSAY[S.source]; checks(); });
  });
  $("reset").addEventListener("click", function () {
    S = JSON.parse(JSON.stringify(HONEST));
    $("seg").value = S.seg; $("lookId").value = S.id; $("scope").value = S.scope; $("city").value = S.city; $("step").value = "0";
    $("rows").value = "1450"; $("voucher").value = "500"; $("typed").value = "";
    press(["leafSums", "leafAvg"], "leafSums"); press(Object.keys(WAYIDS), "wayRe"); press(Object.keys(MODEIDS), "modeOnce");
    press(Object.keys(MATCHIDS), "matchExact"); press(Object.keys(FORMIDS), "formD"); press(Object.keys(BASEIDS), "baseQ1");
    press(Object.keys(COLIDS), "colSum"); press(Object.keys(EXPIDS), "expToday"); press(Object.keys(FOOTIDS), "footSub");
    press(Object.keys(SRCIDS), "srcUnrun");
    everything();
    $("checksSaid").textContent = "Every panel is back at its honest setting: each order counted once, an exact lookup, SUBTOTAL(109) at the foot and nothing typed over, with the source line waiting for your run.";
  });

  function everything() { ch1(); ch1Way(); ch2(); ch2Scale(); ch3(); ch4(); ch5(); ch6(); checks(); }
  everything();

  /* ---------------------------------------------------------------- the experiments */
  function reveal(k, text) { $(k + "What").textContent = text; $(k + "Result").hidden = false; $(k + "Wait").hidden = true; }
  function toggle(btn, on, onText, offText) { btn.setAttribute("aria-pressed", String(on)); btn.textContent = on ? offText : onText; }

  var aOn = false;
  function drawA() {
    K.draw("expADraw", K.columns(["as exported", "after Remove Duplicates", "each order once"], [["total, invented rows", [13000, aOn ? 9000 : 13000, 7000]]],
      { fmt: R, lit: [1], width: 440, title: aOn ? "One row went; the instalment order still counts twice" : "Five invented rows for three orders worth Rs 7,000" }));
  }
  $("expARun").addEventListener("click", function () {
    aOn = !aOn; toggle(this, aOn, "Remove Duplicates", "Put the rows back"); drawA();
    reveal("expA", aOn ? "One row went, the gateway's copy. The instalment order's two rows differ in the amount paid, so both stay, and four rows total Rs 9,000 where the orders are worth Rs 7,000."
      : "Back to the export: five rows and a total of Rs 13,000 for three orders worth Rs 7,000.");
  });
  $("expASeq").addEventListener("click", function () {
    openSeq("Experiment A, as a sequence", ["the export", "Remove Duplicates", "the pivot"], [
      ["the export", "Remove Duplicates", "five invented rows"], ["Remove Duplicates", "Remove Duplicates", "drop the identical copy"],
      ["Remove Duplicates", "the pivot", "four rows"], ["the pivot", "the export", "Rs 9,000 against orders worth Rs 7,000"]],
      "Identical rows are one defect and a finer grain is another, and only a count by the order key fixes the second.");
  });
  drawA();

  var bOn = false;
  function drawB() {
    K.draw("expBDraw", K.bridge(["what the buyers spent", 3000000], bOn ? [["the averaged leaf adds", 1350000]] : [],
      { fmt: money, lo: 0, lit: [0], width: 440, endLabel: bOn ? "rebuilt, averaged leaf" : "rebuilt, revenue over orders",
        title: bOn ? "The tree rebuilt with the averaged leaf" : "The tree rebuilt with revenue over orders, Rs 2,50,000" }));
  }
  $("expBRun").addEventListener("click", function () {
    bOn = !bOn; toggle(this, bOn, "Average each buyer's ratio", "Use revenue over orders again"); drawB();
    reveal("expB", bOn ? "The three buyers' own ratios are Rs 6,00,000, Rs 3,00,000 and Rs 1,87,500, and their average is Rs 3,62,500 against Rs 2,50,000 from revenue over orders, 45.0 percent high. Times 12 orders the tree rebuilds Rs 43,50,000, Rs 13,50,000 more than the buyers spent."
      : "With revenue over orders, Rs 30,00,000 over 12 orders is Rs 2,50,000 an order, and 3 buyers × 4 orders each × Rs 2,50,000 multiplies back to Rs 30,00,000.");
  });
  $("expBSeq").addEventListener("click", function () {
    openSeq("Experiment B, as a sequence", ["the buyers", "the leaf", "the tree"], [
      ["the buyers", "the leaf", "ratios 6,00,000; 3,00,000; 1,87,500"], ["the leaf", "the leaf", "average: Rs 3,62,500"],
      ["the leaf", "the tree", "12 orders × Rs 3,62,500"], ["the tree", "the buyers", "Rs 43,50,000 against the Rs 30,00,000 spent"],
      ["the buyers", "the leaf", "sum over sum: 30,00,000 / 12"], ["the leaf", "the tree", "Rs 2,50,000 multiplies back"]],
      "The average gives each buyer one vote, while revenue over orders gives each order one vote, which is what the tree's leaf claims.");
  });
  drawB();

  $("expCRun").addEventListener("click", function () {
    var on = this.getAttribute("aria-pressed") !== "true";
    this.setAttribute("aria-pressed", String(on));
    this.textContent = on ? "Clear both lookups" : "Run both lookups";
    $("expCWork").textContent = on ? 'MATCH("C-0405", ids, 0) is #N/A; MATCH("C-0405", ids, 1) lands on C-0404' : 'MATCH("C-0405", ids, ?)';
    reveal("expC", on ? "The exact match returned #N/A, which IFERROR turns into \"not in the table\". The approximate match returned C-0404's row, Rs 8,760, and nothing on the screen said so."
      : "Both lookups are cleared; run them again to see the two answers side by side.");
  });
  $("expCSeq").addEventListener("click", function () {
    openSeq("Experiment C, as a sequence", ["chief of staff", "the lookup", "the ids"], [
      ["chief of staff", "the lookup", "find C-0405"], ["the lookup", "the ids", "exact: no such id"], ["the lookup", "chief of staff", "not in the table"],
      ["the lookup", "the ids", "approximate: largest not above"], ["the lookup", "chief of staff", "C-0404, Rs 8,760"]],
      "Both lookups ran on the same eight invented ids, and only one of them admitted that the id was missing.");
  });

  $("expDRun").addEventListener("click", function () {
    var on = this.getAttribute("aria-pressed") !== "true";
    this.setAttribute("aria-pressed", String(on));
    this.textContent = on ? "Clear both" : "Compute both";
    $("expDWork").textContent = on ? "(400 - 500) / 500 = -20.0%;  (400 - 500) / 400 = -25.0%" : "(400 - 500) / ? = ?";
    reveal("expD", on ? "Measured on the earlier quarter the fall is 20 percent; divided by the later quarter it reads 25 percent. The same Rs 100 fall tells two stories."
      : "Both are cleared; compute them again to see the two bases.");
  });
  $("expDSeq").addEventListener("click", function () {
    openSeq("Experiment D, as a sequence", ["the change", "the right base", "the wrong base"], [
      ["the change", "the change", "400 - 500 = -100"], ["the change", "the right base", "divide by 500"], ["the right base", "the right base", "-20.0%"],
      ["the change", "the wrong base", "divide by 400"], ["the wrong base", "the wrong base", "-25.0%"]],
      "A change answers the question \"compared with what\", and the answer is the earlier period.");
  });

  var eOn = false;
  function drawE() {
    var series = [["a lookup per order", [36000, 22000, 14000]]];
    if (eOn) series.push(["every payment added", [36000, 30000, 6000]]);
    K.draw("expEDraw", K.columns(["booked", "collected", "outstanding"], series, { fmt: R, lit: [2], width: 440,
      title: eOn ? "Three invented orders, two ways to join the payments" : "Three invented orders, joined by a lookup" }));
  }
  $("expERun").addEventListener("click", function () {
    eOn = !eOn; toggle(this, eOn, "Add every payment instead", "Back to the lookup alone"); drawE();
    reveal("expE", eOn ? "The lookup took the first payment of each order and reported Rs 22,000 collected and Rs 14,000 outstanding. Adding every payment gives Rs 30,000 collected and Rs 6,000 outstanding, which is the one unpaid order; the Rs 8,000 second instalment had been paid all along."
      : "The lookup alone reports Rs 22,000 collected and Rs 14,000 outstanding on Rs 36,000 booked.");
  });
  $("expESeq").addEventListener("click", function () {
    openSeq("Experiment E, as a sequence", ["the orders", "the payments", "the report"], [
      ["the orders", "the payments", "lookup on the order id"], ["the payments", "the report", "first row only: Rs 22,000"],
      ["the orders", "the payments", "SUMIFS on the order id"], ["the payments", "the report", "every row: Rs 30,000"],
      ["the report", "the orders", "outstanding: the unpaid Rs 6,000"]],
      "A lookup stops at the first match, so a second payment never reaches the report; a sum keeps going to the last row.");
  });
  drawE();

  var MEMBERS = [["C-0501", "Delhi", 11000], ["C-0502", "Mumbai", 9200], ["C-0503", "Pune", 8000], ["C-0504", "Mumbai", 8400],
    ["C-0505", "Delhi", 6000], ["C-0506", "Mumbai", 7900], ["C-0507", "Chennai", 5500], ["C-0508", "Pune", 4000]];
  var fOn = false;
  function drawF() {
    var html = '<table class="t"><tr><th>Member (invented)</th><th>City</th><th class="num">Revenue</th></tr>';
    MEMBERS.forEach(function (m) { html += '<tr class="' + (fOn && m[1] !== "Mumbai" ? "hid" : "") + '"><td>' + m[0] + "</td><td>" + m[1] + '</td><td class="num">' + R(m[2]) + "</td></tr>"; });
    var vis = MEMBERS.filter(function (m) { return !fOn || m[1] === "Mumbai"; }).reduce(function (t, m) { return t + m[2]; }, 0);
    html += '<tr><td colspan="2"><b>SUM</b></td><td class="num">' + R(60000) + '</td></tr><tr><td colspan="2"><b>SUBTOTAL(109)</b></td><td class="num">' + R(vis) + "</td></tr></table>";
    $("expFTable").innerHTML = html;
  }
  $("expFRun").addEventListener("click", function () {
    fOn = !fOn; toggle(this, fOn, "Filter to Mumbai", "Clear the filter"); drawF();
    reveal("expF", fOn ? "Five rows went off the screen. SUM still reads Rs 60,000, and SUBTOTAL(109) reads Rs 25,500, the three members you can see."
      : "No filter: both feet read Rs 60,000, which is why the defect hides until somebody filters.");
  });
  $("expFSeq").addEventListener("click", function () {
    openSeq("Experiment F, as a sequence", ["the filter", "SUM", "SUBTOTAL(109)"], [
      ["the filter", "SUM", "hide five rows"], ["SUM", "SUM", "adds all eight: Rs 60,000"],
      ["the filter", "SUBTOTAL(109)", "hide five rows"], ["SUBTOTAL(109)", "SUBTOTAL(109)", "adds 3: Rs 25,500"]],
      "The filter changes which rows are on screen, and only SUBTOTAL(109) adds just those rows.");
  });
  drawF();

  var INVENTED = [["X-01", 3000], ["X-02", 2500], ["X-03", 2200], ["X-04", 1800], ["X-05", 1500]];
  var gOn = false;
  function drawG() {
    var src = sum(INVENTED.map(function (r) { return r[1]; }));
    var lines = [["The tree ties", "pass"], ["The list's source ties", "hold"], ["The lookup is honest", "pass"], ["The foot follows the filter", "pass"], ["No typed-over formula", "pass"]];
    var html = '<table class="t"><tr><th>Check, on invented records</th><th>Result</th></tr>';
    lines.forEach(function (l) {
      html += "<tr><td>" + l[0] + (l[0] === "The list's source ties" ? " (" + R(src) + " against " + R(12200) + ")" : "") + '</td><td class="' + (gOn ? l[1] : "") + '">' + (gOn ? l[1].toUpperCase() : "not run") + "</td></tr>";
    });
    $("expGTable").innerHTML = html + "</table>";
  }
  $("expGRun").addEventListener("click", function () {
    gOn = !gOn; toggle(this, gOn, "Run the five checks", "Clear the checks"); drawG();
    reveal("expG", gOn ? "The tree, lookup, foot and typed-over lines read PASS, the source line reads HOLD at Rs 1,200 short of Rs 12,200, and the release says: \"Hold the protect list; ship the rest.\" One failing check holds the part it stands behind and nothing else."
      : "The checks are cleared and the release has nothing to read yet.");
  });
  $("expGSeq").addEventListener("click", function () {
    openSeq("Experiment G, as a sequence", ["the checks", "the release", "Monday's deck"], [
      ["the checks", "the checks", "four PASS, source HOLD"], ["the checks", "the release", "which part stands behind it?"],
      ["the release", "the release", "the protect list"], ["the release", "Monday's deck", "ship the tree and the card"],
      ["the release", "Monday's deck", "hold the list until the source ties"]],
      "The release reads which check failed, so a list on a short source waits while everything that ties ships.");
  });
  drawG();

  var hOn = false;
  function drawH() {
    var q2 = hOn ? 450 : 400;
    var html = '<table class="t"><tr><th>Cell, invented</th><th>Holds</th><th class="num">Value</th><th>ISFORMULA</th></tr>' +
      '<tr><td>Q1</td><td>a formula</td><td class="num">Rs 500</td><td class="pass">TRUE</td></tr>' +
      '<tr><td>Q2</td><td>' + (hOn ? "a typed figure" : "a formula") + '</td><td class="num">' + R(q2) + '</td><td class="' + (hOn ? "hold" : "pass") + '">' + (hOn ? "FALSE" : "TRUE") + "</td></tr>" +
      '<tr><td colspan="4">The card: down ' + pct((500 - q2) / 500 * 100) + " percent on Q1</td></tr></table>";
    $("expHTable").innerHTML = html;
  }
  $("expHRun").addEventListener("click", function () {
    hOn = !hOn; toggle(this, hOn, "Type Rs 450 over Q2", "Put the formula back"); drawH();
    reveal("expH", hOn ? "The card now reads down 10.0 percent instead of 20.0 percent and nothing on the sheet is red. ISFORMULA on Q2 returns FALSE, so the typed-over check reads HOLD and the release holds the whole workbook until someone traces the figure."
      : "The formula is back in Q2, ISFORMULA reads TRUE in both cells, and the card says down 20.0 percent again.");
  });
  $("expHSeq").addEventListener("click", function () {
    openSeq("Experiment H, as a sequence", ["the director", "the sheet", "the Checks tab"], [
      ["the director", "the sheet", "type Rs 450 over Q2"], ["the sheet", "the sheet", "card: down 10.0 percent, no error"],
      ["the Checks tab", "the sheet", "ISFORMULA on every computed cell"], ["the sheet", "the Checks tab", "Q2: FALSE"],
      ["the Checks tab", "the director", "hold the whole workbook"]],
      "Nothing on the sheet itself turns red when a formula is typed over, so the check has to ask every computed cell.");
  });
  drawH();

  /* ---------------------------------------------------------------- the decision */
  var DEC = {
    decProtect: ["protect", "bad", "Locking every cell keeps the formulas safe, and Excel can still let a director filter and sort, but no what-if can be asked, so the chief of staff's condition fails. A locked sheet still shows a SUM under a filter, and it cannot tell anyone that the export under it is short."],
    decPdf: ["pdf", "bad", "Nothing in a PDF can go wrong and nothing recalculates, so a director who changes an assumption sees nothing move. A PDF is the right answer for a board pack nobody is meant to change, which Monday's review is not."],
    decYellow: ["yellow", "good", "This is the one I would send. A director can filter, sort and change any yellow input, every other cell is a formula, the foot is SUBTOTAL(109), and the Checks tab turns a wrong number red and holds the part behind it before anyone reads it."],
    decCopy: ["copy", "bad", "A copy for each director lets everyone do anything, and by the end of the meeting the copies disagree, with no way to tell which is right and no check that ties any of them to the warehouse."]
  };
  function drawDec(pick) {
    function k(which, good) { return pick === which ? (good ? "good" : "bad") : "plain"; }
    K.draw("decTree", K.tree({ label: "How does the workbook go into the room?", kind: pick ? "plain" : "lit", branches: [
      ["", { label: "a) Protect every cell\nno what-if can be asked", kind: k("protect", false) }],
      ["", { label: "b) Send a PDF\nnothing recalculates", kind: k("pdf", false) }],
      ["", { label: "c) Yellow inputs and a Checks tab\na wrong number turns red", kind: k("yellow", true) }],
      ["", { label: "d) A copy for each director\ncopies disagree", kind: k("copy", false) }]] },
      { width: 200, title: "Four ways to hand Monday's workbook to the room" }));
  }
  Object.keys(DEC).forEach(function (id) {
    $(id).addEventListener("click", function () {
      press(Object.keys(DEC), id); drawDec(DEC[id][0]);
      $("decWhy").className = "strip " + DEC[id][1]; $("decWhyText").textContent = DEC[id][2];
    });
  });
  drawDec(null);
})();
</script>
</body>
</html>
"""

html = PAGE.replace("__DATA__", json.dumps(data, separators=(",", ":")))
# The plant stays the room's to find: no id beside it, no grand total of the customer table, no gap.
for forbidden in (r"C-0169", r"C-0170", r"19,83,78,260", r"\b198378260\b", r"\b21,740\b", r"\b21740\b"):
    assert not re.search(forbidden, html), f"the page would print {forbidden}"
OUT.write_text(html, encoding="utf-8")
print("wrote", OUT)
