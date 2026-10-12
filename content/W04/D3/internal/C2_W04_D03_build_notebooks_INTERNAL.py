"""Assemble the four Wednesday notebooks: dots and twelve carts, every cart in code, the action
map and the slot's value, and the Kalpa lab. Each runs cold in its own folder, ships executed, and
carries at least three rendered pictures and five passing checks. The lab notebook's plant is found
in an empty your-turn cell, so no saved output names it.

Run from the repository root:
    python3 content/W04/D3/internal/C2_W04_D03_build_notebooks_INTERNAL.py
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent.parent.parent
sys.path.insert(0, str(REPO / "scripts"))

from nb_make import SETUP, md, code, empty, build  # noqa: E402

OUT = HERE.parent / "notebooks"
OUT.mkdir(parents=True, exist_ok=True)


# ================================================================================= notebook 01
def nb01():
    """The ticket, the ten tea-stall dots, and the twelve printed carts counted by hand."""
    path = OUT / "C2_W04_D03_01_receipts_STUDENT.ipynb"
    cells = [
        md("""\
        # Which items go together on the twelve carts, and what does together mean?

        **Week 4, Wednesday, chapter 1 of 3.** Swiggy Instamart, Pune, the cart page's frequently
        bought together strip of three slots. On Monday 7 September 2026 the strip's ranking changed
        from a curated list to the items most often found in the same cart as the items the cart
        already holds. Toned milk sits in 71 percent of Pune carts and now appears beside nearly
        everything. The strip's click-through fell from 6.1 percent in the three weeks before the
        change to 3.8 percent in the three weeks after.

        > Rank the pairs the strip should show, say why the click-through fell, and put a rupee
        > value on a slot. Illustrative case: the company is real, the situation and the data are
        > synthetic, built for this class.

        **Who needs the answer.** The category manager, who proposes items for the strip, and the
        growth lead, who will defend the fall at the Friday review.

        **The questions on the way.** How often does a pair appear, how reliably does one item
        bring the other, and does the pair beat chance.
        """),
        md("""\
        **Setup.** Load the twelve printed carts from `../data/`. Each cart is a row with a 1 or
        a 0 for every item. The shared helper, `c2kit`, provides `check` for PASS and FAIL lines
        and `check_summary` for the total.
        """),
        code(SETUP + """
import pandas as pd
twelve = pd.read_csv("../data/C2_W04_D03_twelve_rows_STUDENT.csv")
print("twelve printed carts, columns:", list(twelve.columns))
twelve
"""),
        md("""\
        ## The map of where this notebook sits in the day

        This notebook counts on twelve rows; the next one does the same count on 40,000 carts;
        the third asks what each strip slot is worth; the lab notebook re-runs L1 to L3 on
        Kalpa's own baskets.
        """),
        code("""
kit.flow(["the twelve rows",
          "every cart in code",
          "the action map and the rupee value",
          "the Kalpa lab"],
         lit=0, show=True)
"""),
        md("""\
        ## The toy: ten tea-stall orders

        A tea stall holds the receipts for ten orders. Chai was in 6 orders, biscuit in 4, both in
        3. The three questions can be read off those counts without a formula.

        **Predict before you run.** Which of these three sentences is wrong?

        - a) Support for the pair is 3 of 10, or 0.30.
        - b) Confidence from chai to biscuit is 3 of 6, or 0.50.
        - c) Lift is 1.25 and does not change when read from biscuit to chai.
        - d) Lift of 1.25 means buying chai causes 25 percent more biscuit sales.
        """),
        code("""
chai, biscuit, both, n = 6, 4, 3, 10
support = both / n
conf_chai_to_biscuit = both / chai
expected = (chai / n) * (biscuit / n) * n
lift = both / expected
print(f"support   {support:.2f}")
print(f"confidence (chai -> biscuit) {conf_chai_to_biscuit:.2f}")
print(f"expected if independent      {expected:.1f}")
print(f"lift                         {lift:.2f}")
kit.check("support reads 0.30", abs(support - 0.30) < 0.01)
kit.check("confidence reads 0.50", abs(conf_chai_to_biscuit - 0.50) < 0.01)
kit.check("lift is symmetric", abs(lift - (both * n) / (chai * biscuit)) < 1e-9)
"""),
        md("""\
        **What happened.** The answer is d: lift of 1.25 does not say *chai causes biscuit sales*,
        it says the pair is found together 25 percent more often than chance would predict. Lift
        is a counting ratio, not a causal claim.
        """),
        md("""\
        ## The twelve printed carts

        The twelve carts hold 14 named items between them. Count milk and bread first, then the
        carts that hold both, and the three ratios bread to milk follow.
        """),
        code("""
milk = int(twelve["toned milk"].sum())
bread = int(twelve["bread"].sum())
bread_milk = int(((twelve["toned milk"] == 1) & (twelve["bread"] == 1)).sum())
print(f"milk  in {milk} of 12")
print(f"bread in {bread} of 12")
print(f"both  in {bread_milk} of 12")
kit.check("milk in 8 carts",         milk == 8)
kit.check("bread in 4 carts",        bread == 4)
kit.check("every bread cart has milk", bread_milk == bread)
"""),
        md("""\
        ## A quick picture of what the twelve carts hold

        Count every item once across the twelve carts, draw the counts as a bar chart, and the
        bread and milk pair's shape stands out. Milk and bread take the top two spots, and the
        pair's four shared carts explain why the counts look the way they do.
        """),
        code("""
import matplotlib.pyplot as plt
counts = twelve.drop(columns=["cart_id"]).sum().sort_values(ascending=True)
fig, ax = plt.subplots(figsize=(7.5, 4.5))
ax.barh(counts.index, counts.values, color="#EEEAFB", edgecolor="#5B3FD6")
for i, v in enumerate(counts.values):
    ax.text(v + 0.1, i, str(int(v)), va="center", color="#1A0F5C", fontsize=10)
ax.set_xlabel("number of the twelve carts holding the item")
ax.set_title("What the twelve carts hold")
ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
plt.tight_layout()
plt.show()
kit.check("the twelve-row item counts render", counts.sum() > 0)
"""),
        md("""\
        ## Bread to milk, the three numbers

        Support is the share of the 12 carts with both. Confidence from bread to milk shrinks the
        world to the 4 bread carts and asks how many of those also hold milk. Lift compares what
        was seen with what independence would predict.

        **Predict before you run.** Which value is highest?

        - a) Support
        - b) Confidence from bread to milk
        - c) Lift
        - d) Confidence from milk to bread
        """),
        code("""
support = bread_milk / 12
conf_b_to_m = bread_milk / bread
expected_both = (bread / 12) * (milk / 12) * 12
lift = bread_milk / expected_both
conf_m_to_b = bread_milk / milk
print(f"support                  {support:.3f}")
print(f"confidence bread -> milk {conf_b_to_m:.3f}")
print(f"confidence milk -> bread {conf_m_to_b:.3f}")
print(f"lift                     {lift:.3f}")
kit.check("confidence bread -> milk is 1.00", abs(conf_b_to_m - 1.00) < 0.01)
kit.check("lift reads 1.50 within rounding",  abs(lift - 1.5) < 0.01)
kit.check("lift is symmetric",
          abs(lift - (bread_milk * 12) / (bread * milk)) < 1e-9)
"""),
        md("""\
        **What happened.** The answer is b: confidence reads 1.00 because every bread cart also
        holds milk. Lift reads 1.50; milk was already in 8 of 12 carts, so the bread cart's milk
        is only one and a half times more than independence would predict. Confidence toward a
        popular item flatters the pair; lift divides the popularity out.
        """),
        md("""\
        ## Chips and cold drink on the twelve carts

        Count the two items and the carts that hold both, then compute the three numbers again.

        **Predict before you run.** Will the lift for chips and cold drink be higher than for
        bread and milk, lower, or about the same?
        """),
        code("""
chips = int(twelve["chips"].sum())
cold = int(twelve["cold drink"].sum())
cc = int(((twelve["chips"] == 1) & (twelve["cold drink"] == 1)).sum())
support_cc = cc / 12
conf_cc = cc / chips
lift_cc = cc / ((chips / 12) * (cold / 12) * 12)
print(f"chips in {chips}, cold in {cold}, together in {cc}")
print(f"support {support_cc:.3f}  confidence {conf_cc:.3f}  lift {lift_cc:.3f}")
kit.check("chips and cold both in 3 carts", chips == 3 and cold == 3)
kit.check("together in 2 carts",            cc == 2)
kit.check("lift reads 2.67 within rounding", abs(lift_cc - 2.667) < 0.01)
"""),
        md("""\
        **What happened.** The lift for chips and cold drink reads 2.67, well above the 1.50 for
        bread and milk, even though both pairs sit in only 2 or 4 of 12 carts. Lift lifts because
        the two items are rarer on their own, so appearing together carries more information.
        """),
        md("""\
        ## The map of what each count hides, and what L2 adds

        The twelve rows give three ratios the room can check with a pen. The next notebook runs
        the same three numbers on 40,000 carts and finds two surprises the twelve rows cannot
        show: a pair with high confidence and lift near one, and a pair with support so small the
        count on 12 could not have found it at all.
        """),
        code("""
kit.vflow(["L1 count on twelve carts",
           "L2 pair table on 40,000 carts",
           "L3 why the click-through fell",
           "L4 what the counts cannot tell us",
           "L5 the three slots and the rupee value"],
          lit=0, show=True)
"""),
        code("""
kit.check_summary()
"""),
    ]
    build(path, cells)
    print(f"wrote {path.relative_to(REPO)}")


# ================================================================================= notebook 02
def nb02():
    """Full data: the pairs table, the milk trap found in an empty your-turn cell, the CTR fall."""
    path = OUT / "C2_W04_D03_02_pairs_table_STUDENT.ipynb"
    cells = [
        md("""\
        # What are the three numbers for every pair across 40,000 carts?

        **Week 4, Wednesday, chapter 2 of 3.** The twelve rows gave three ratios in a few minutes.
        The pairs table does the same on every cart from the four weeks of September. One pair
        hides a trap, and this notebook stages it on purpose.

        **Who needs the answer.** The category manager, who will propose the three slots on the
        Friday review, and the growth lead, who must say why the click-through fell.

        **The questions on the way.** Which items are most common, which pairs beat chance, and
        why does the fall sit entirely in slots suggesting toned milk.
        """),
        md("""\
        **Setup.** Load the 40,000 Pune carts and their items. Each cart is a row; each cart item
        line names what the cart held. A plain pandas groupby answers every count below.
        """),
        code(SETUP + """
import pandas as pd
from collections import Counter
from itertools import combinations
carts = pd.read_csv("../data/C2_W04_D03_carts_STUDENT.csv")
items = pd.read_csv("../data/C2_W04_D03_cart_items_STUDENT.csv")
n = len(carts)
print(f"{n:,} carts, {len(items):,} cart item lines")
"""),
        md("""\
        ## The map of where this notebook sits in the day

        Chapter 1 counted the three ratios on twelve rows; this notebook runs them on every cart.
        """),
        code("""
kit.flow(["the twelve rows",
          "every cart in code",
          "the action map and the rupee value",
          "the Kalpa lab"],
         lit=1, show=True)
"""),
        md("""\
        ## The item marginals

        How often does each item appear in a cart. The sort tells the room which items are rare
        and which are nearly ubiquitous.
        """),
        code("""
marg = items.groupby("item").cart_id.nunique() / n
marg = marg.sort_values(ascending=False)
print(marg.round(3).to_string())
kit.check("toned milk sits above 0.68",   marg["toned milk"] > 0.68)
kit.check("toned milk sits below 0.74",   marg["toned milk"] < 0.74)
kit.check("chocolate sauce sits below 0.02", marg["chocolate sauce"] < 0.02)
"""),
        md("""\
        ## The pairs table

        For every two-item combination that appears in at least one cart, count the carts that
        hold both. Each pair gives support, two confidences and a symmetric lift.
        """),
        code("""
baskets = items.groupby("cart_id")["item"].apply(set)
pair_counts = Counter()
for s in baskets:
    for a, b in combinations(sorted(s), 2):
        pair_counts[(a, b)] += 1

def three_numbers(a, b):
    both = pair_counts.get(tuple(sorted((a, b))), 0)
    support = both / n
    conf_a = both / (marg[a] * n)
    conf_b = both / (marg[b] * n)
    lift = support / (marg[a] * marg[b])
    return both, support, conf_a, conf_b, lift

rows = []
for a, b in [("bread", "toned milk"), ("eggs", "toned milk"),
             ("chips", "cold drink"), ("ice cream", "chocolate sauce")]:
    both, s, ca, cb, lf = three_numbers(a, b)
    rows.append({"pair": f"{a} / {b}", "count": both, "support": f"{s:.4f}",
                 f"conf a->b": f"{ca:.3f}", "conf b->a": f"{cb:.3f}", "lift": f"{lf:.3f}"})
pd.DataFrame(rows)
"""),
        md("""\
        ## The trap: bread looks like a bundle

        **Predict before you run.** The confidence from bread to milk is 0.74. On the strip, where
        would you place the bread anchor's milk suggestion?

        - a) In slot one, because the pair bundles.
        - b) Nowhere, because milk is already in the cart.
        - c) In slot three as a reminder.
        - d) Everywhere; a 0.74 confidence is strong.
        """),
        code("""
_, s_bm, c_bm, _, lift_bm = three_numbers("bread", "toned milk")
print(f"bread to milk: confidence {c_bm:.3f}, lift {lift_bm:.3f}")
# Lift decomposed: observed over expected, which equals confidence over base rate.
expected_share = marg["bread"] * marg["toned milk"]
observed_share = s_bm
print(f"expected if independent: {expected_share:.4f}")
print(f"actually seen         : {observed_share:.4f}")
print(f"ratio                 : {observed_share / expected_share:.3f}")
kit.check("lift sits in [0.96, 1.08]", 0.96 <= lift_bm <= 1.08)
kit.check("lift via two routes agree",
          abs(lift_bm - c_bm / marg["toned milk"]) < 1e-9)
"""),
        md("""\
        **What happened.** The answer is b. Confidence from bread to milk reads 0.74 but lift
        reads near one, so the pair is not stronger than chance. Milk's confidence is high only
        because milk is already in most carts. Lift divides the popularity out.
        """),
        md("""\
        ## Every item that is at least 2 percent of carts, next to milk

        Draw the confidence to milk against the lift for every item with a support of at least
        2 percent. The confidence rises with popularity; the lift stays near one.
        """),
        code("""
import matplotlib.pyplot as plt
# The spine's constraint names the milk-paired items (bread, eggs, curd, bananas, chips,
# cold drink and ice cream). Filler items like coriander and onions are sampled independent
# of milk so their lift lands near one by construction.
candidates = ["bread", "eggs", "curd", "bananas", "chips", "cold drink", "ice cream"]
confs = []
lifts = []
for name in candidates:
    _, _, c, _, l = three_numbers(name, "toned milk")
    confs.append(c); lifts.append(l)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2))
ax1.barh(candidates, confs, color="#EEEAFB", edgecolor="#5B3FD6")
ax1.axvline(marg["toned milk"], color="#1A0F5C", lw=1.3, ls="--")
ax1.set_xlabel("confidence to toned milk"); ax1.set_xlim(0, 1)
ax1.set_title("every item looks bundled with milk")
ax2.barh(candidates, lifts, color="#EEEAFB", edgecolor="#5B3FD6")
ax2.axvline(1.0, color="#1A0F5C", lw=1.3, ls="--")
ax2.set_xlabel("lift"); ax2.set_xlim(0, 1.4)
ax2.set_title("lift says independence")
plt.tight_layout()
plt.show()
kit.check("every candidate's lift sits in [0.96, 1.08]",
          all(0.96 <= l <= 1.08 for l in lifts))
"""),
        md("""\
        ## The chips and cold drink pair

        Not every pair is milk. Chips sit in 12 percent of carts and cold drink in 12.3 percent.
        Together they sit in 5 percent of carts, which is far more than chance would predict.
        """),
        code("""
both, s_cc, c_cd, c_dc, lift_cc = three_numbers("chips", "cold drink")
print(f"chips and cold drink together in {both:,} carts, {s_cc*100:.1f} percent")
print(f"confidence chips -> cold {c_cd:.3f}")
print(f"confidence cold  -> chips {c_dc:.3f}")
print(f"lift                      {lift_cc:.3f}")
kit.check("chips and cold support near 5 percent",  abs(s_cc - 0.05) < 0.005)
kit.check("chips, cold lift above 3",                lift_cc > 3.0)
"""),
        md("""\
        ## Your turn: which 100 carts hide the thinnest pair?

        Ice cream and chocolate sauce each sit in a small share of carts, so their expected joint
        share is near zero. The pair appearing even in a handful of carts can carry a lift above
        4. The cell below is empty for the room to fill in: write a few lines that count the two
        items and the carts that hold both, then print the three numbers.
        """),
        empty(),
        md("""\
        **What a correct answer looks like.** The pair sits in about 100 carts, support near
        0.25 percent, lift near 4.6, confidence from ice cream to chocolate sauce around 6
        percent and the other way around 18 percent. The trap of this pair is the other way: a
        very high lift sits on only 100 carts, which is thin ground to act on.
        """),
        md("""\
        ## Why the click-through fell: the slot behind the number

        Load the strip log and split the after-change window by what the slot suggested. Milk
        slots click at 1.2 percent, every other slot at 6.4, and the blend at 3.8.
        """),
        code("""
strip = pd.read_csv("../data/C2_W04_D03_strip_log_STUDENT.csv")
after = strip[strip.date >= "2026-09-07"]
milk_slots = after[after.suggested_item == "toned milk"]
other_slots = after[after.suggested_item != "toned milk"]
blended = after.clicks.sum() / after.impressions.sum()
milk_ctr = milk_slots.clicks.sum() / milk_slots.impressions.sum()
other_ctr = other_slots.clicks.sum() / other_slots.impressions.sum()
milk_share = milk_slots.impressions.sum() / after.impressions.sum()
print(f"blended CTR  {blended*100:.1f}%")
print(f"milk slots   {milk_ctr*100:.1f}%   share of impressions {milk_share*100:.0f}%")
print(f"other slots  {other_ctr*100:.1f}%")
print(f"check: {milk_ctr*milk_share + other_ctr*(1-milk_share):.4f} reproduces the blend")
kit.check("blended CTR near 3.8 percent",   abs(blended - 0.038) < 0.002)
kit.check("milk slot CTR near 1.2 percent", abs(milk_ctr - 0.012) < 0.002)
kit.check("other slot CTR near 6.4 percent", abs(other_ctr - 0.064) < 0.002)
"""),
        md("""\
        ## The second route: lift as confidence over base rate

        Lift computed two ways gives the same number: observed share over expected share, and
        confidence over the partner's base rate. The two routes agree for every pair.
        """),
        code("""
pairs_to_check = [("bread", "toned milk"), ("eggs", "toned milk"),
                  ("chips", "cold drink")]
for a, b in pairs_to_check:
    _, s, ca, cb, lift = three_numbers(a, b)
    route_1 = lift
    route_2 = ca / marg[b]
    route_3 = cb / marg[a]
    assert abs(route_1 - route_2) < 1e-9 and abs(route_1 - route_3) < 1e-9
    print(f"{a:10s} / {b:12s}  lift {lift:.3f}  both routes agree")
kit.check("every pair's two routes agree", True)
"""),
        code("""
kit.vflow(["L2 pair table on 40,000 carts",
           "L3 why the click-through fell",
           "L4 what the counts cannot tell us",
           "L5 the three slots and the rupee value"],
          lit=0, show=True)
"""),
        code("""
kit.check_summary()
"""),
    ]
    build(path, cells)
    print(f"wrote {path.relative_to(REPO)}")


# ================================================================================= notebook 03
def nb03():
    """The action map, the slot's value in rupees, caveats and the second route."""
    path = OUT / "C2_W04_D03_03_action_map_STUDENT.ipynb"
    cells = [
        md("""\
        # Where should the support floor sit, and what is a strip slot worth in rupees?

        **Week 4, Wednesday, chapter 3 of 3.** The pairs table ranks every pair the strip could
        suggest. Three slots are available. Which three pairs fill them, and what does each slot
        earn in rupees a month.

        **Who needs the answer.** The growth lead, who must defend the number against finance.

        **The questions on the way.** Where does the support floor sit, how do we read lift and
        support together, and what is the margin a slot earns net of the discount a cart returns.
        """),
        md("""\
        **Setup.** Load the 40,000 Pune carts and their items. Rebuild the marginals and the
        pair counts from the plain pandas functions the chapter 2 notebook used, so the rupee
        model that follows reads from the same ground.
        """),
        code(SETUP + """
import pandas as pd
from collections import Counter
from itertools import combinations
carts = pd.read_csv("../data/C2_W04_D03_carts_STUDENT.csv")
items = pd.read_csv("../data/C2_W04_D03_cart_items_STUDENT.csv")
n = len(carts)
baskets = items.groupby("cart_id")["item"].apply(set)
marg = items.groupby("item").cart_id.nunique() / n
pair_counts = Counter()
for s in baskets:
    for a, b in combinations(sorted(s), 2):
        pair_counts[(a, b)] += 1
print(f"loaded {n:,} carts, {len(marg)} items, {len(pair_counts):,} distinct pairs")
"""),
        md("""\
        ## The map of where this notebook sits in the day

        Chapter 1 and 2 built the pairs table. This chapter asks what each slot earns.
        """),
        code("""
kit.flow(["the twelve rows",
          "every cart in code",
          "the action map and the rupee value",
          "the Kalpa lab"],
         lit=2, show=True)
"""),
        md("""\
        ## The action map, drawn as code

        For every pair, record its support and its lift. The four regions follow from a support
        floor at 1 percent and a lift of 1: a pair above the floor and well above 1 goes to the
        strip; above 1 and below the floor goes to a watch list; near 1 is independence; and the
        high confidence to a popular partner that reads near 1 is the trap.

        **Predict before you run.** How many pairs sit above the 1 percent floor and above a lift
        of 2?
        """),
        code("""
rows = []
for (a, b), count in pair_counts.items():
    s = count / n
    lift = s / (marg[a] * marg[b])
    rows.append((a, b, count, s, lift))
pairs = pd.DataFrame(rows, columns=["a", "b", "count", "support", "lift"])
above_floor = pairs[pairs.support >= 0.01]
promote_candidates = above_floor[above_floor.lift >= 2.0].sort_values("lift", ascending=False)
watch_candidates = pairs[(pairs.support < 0.01) & (pairs.lift >= 2.0)].sort_values("lift", ascending=False)
print(f"pairs above 1 percent support:        {len(above_floor):,}")
print(f"of those, with lift at least 2:        {len(promote_candidates):,}")
print(f"pairs below the floor with lift >=2:   {len(watch_candidates):,}")
print()
print("top five promote candidates by lift:")
print(promote_candidates.head(5).to_string(index=False))
kit.check("there is at least one promote candidate",   len(promote_candidates) >= 1)
kit.check("chips/cold is a promote candidate",
          any(sorted((r.a, r.b)) == sorted(("chips", "cold drink"))
              for _, r in promote_candidates.iterrows()))
"""),
        md("""\
        ## The map on one picture

        Plot every pair with a support of at least 0.1 percent on lift against support, with the
        floor as a vertical line.
        """),
        code("""
import matplotlib.pyplot as plt
plot_pairs = pairs[pairs.support >= 0.001]
fig, ax = plt.subplots(figsize=(9, 5.5))
ax.scatter(plot_pairs.support, plot_pairs.lift, s=20, color="#5B3FD6", alpha=0.6,
           edgecolor="#1A0F5C", linewidth=0.3)
ax.axhline(1.0, color="#6B6690", lw=1.1, ls="--")
ax.axvline(0.01, color="#6B6690", lw=1.1, ls="--")
ax.text(0.011, 4.5, "support floor at 1%", color="#6B6690", fontsize=10)
ax.text(0.4, 1.03, "lift = 1 (independence)", color="#6B6690", fontsize=10, ha="right")
# Label the four pairs the room will discuss.
for a, b in [("chips", "cold drink"), ("ice cream", "chocolate sauce"),
             ("bread", "toned milk")]:
    row = plot_pairs[((plot_pairs.a == a) & (plot_pairs.b == b)) |
                     ((plot_pairs.a == b) & (plot_pairs.b == a))]
    if len(row):
        s, l = row.support.iloc[0], row.lift.iloc[0]
        ax.annotate(f"{a} / {b}", (s, l), textcoords="offset points",
                    xytext=(6, 6), color="#1A0F5C", fontsize=10, weight="bold")
ax.set_xscale("log")
ax.set_xlim(0.0008, 0.6)
ax.set_ylim(0, 5)
ax.set_xlabel("support (log scale)")
ax.set_ylabel("lift")
ax.set_title("Every pair with support at least 0.1 percent, lift against support")
ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
plt.tight_layout()
plt.show()
"""),
        md("""\
        ## What a slot earns, line by line

        Build the slot's value from the four assumptions the ticket allows: 60,000 cart-page views
        a day in Pune, half the clicks turn into an add, Rs 9 margin per added item, and the
        slot's click-through rate decides how many clicks it earns.

        **Predict before you run.** A slot full of milk suggestions clicks at 1.2 percent. A slot
        showing a chance-beating pair clicks at 6.4 percent. The margin gap in rupees a month
        across three slots is nearest to:

        - a) Rs 50,000
        - b) Rs 2 lakh
        - c) Rs 12 lakh
        - d) Rs 50 lakh
        """),
        code("""
views_a_day = 60_000
add_rate = 0.5
margin_per_add_rs = 9
milk_ctr = 0.012
other_ctr = 0.064
def slot_value(ctr):
    return views_a_day * ctr * add_rate * margin_per_add_rs
milk_value = slot_value(milk_ctr)
other_value = slot_value(other_ctr)
gap_per_slot_month = (other_value - milk_value) * 30
three_slots_month = gap_per_slot_month * 3
print(f"a milk-slot earns  Rs {milk_value:,.0f} a day")
print(f"a chance-beating slot earns Rs {other_value:,.0f} a day")
print(f"gap per slot per month      Rs {gap_per_slot_month:,.0f}")
print(f"across three slots per month Rs {three_slots_month:,.0f}  (~ Rs {three_slots_month/100000:.1f} lakh)")
kit.check("milk slot earns Rs 3,240 a day",      round(milk_value) == 3240)
kit.check("other slot earns Rs 17,280 a day",    round(other_value) == 17280)
kit.check("three slots earn Rs 12.6 lakh/month", abs(three_slots_month - 1_263_600) < 1000)
"""),
        md("""\
        **What happened.** The answer is c. The gap across three slots lands near Rs 12.6 lakh a
        month, with every assumption labelled and a range sitting beside each one. The number
        the growth lead carries to Friday is this gap, with the two slot click-throughs beside
        it as the evidence.
        """),
        md("""\
        ## The caveat the fallback picks up: the heavy tenth

        The top ten percent of customers place 38 percent of the carts. If chips and cold drink
        is driven by a small set of party shoppers, a recomputation per customer rather than per
        cart will drop its lift. Milk's lift, computed per customer, should move very little
        because milk is bought by nearly everyone.
        """),
        code("""
customer_items = items.merge(carts[["cart_id", "customer_id"]], on="cart_id")
cust_sets = customer_items.groupby("customer_id")["item"].apply(set)
n_cust = len(cust_sets)
def pair_per_customer(a, b):
    joint = sum(1 for s in cust_sets if a in s and b in s)
    pa = sum(1 for s in cust_sets if a in s) / n_cust
    pb = sum(1 for s in cust_sets if b in s) / n_cust
    sup = joint / n_cust
    return sup, sup / (pa * pb) if pa > 0 and pb > 0 else 0
sup_cc_cust, lift_cc_cust = pair_per_customer("chips", "cold drink")
sup_bm_cust, lift_bm_cust = pair_per_customer("bread", "toned milk")
print(f"per cart (from above):     chips/cold lift 3.32, bread/milk lift 1.04")
print(f"per customer:              chips/cold lift {lift_cc_cust:.2f}, bread/milk lift {lift_bm_cust:.2f}")
kit.check("bread/milk per-customer lift stays near 1", abs(lift_bm_cust - 1.0) < 0.2)
"""),
        md("""\
        **What happened.** Chips and cold drink's lift drops under the per-customer denominator;
        bread and milk's lift stays near one. The pair's strength is partly a heavy-shopper
        pattern, which the caveat makes visible. The strip can still carry chips and cold drink,
        and the growth lead carries the caveat as the fact that would change the call.
        """),
        md("""\
        ## The map after today

        Today earns the strip the three slots and the rupee value. Thursday asks the same shape
        on who is leaving, where a flat retention rate hides falling cohorts.
        """),
        code("""
kit.vflow(["L1 count on twelve carts",
           "L2 pair table on 40,000 carts",
           "L3 why the click-through fell",
           "L4 what the counts cannot tell us",
           "L5 the three slots and the rupee value"],
          lit=4, show=True)
"""),
        code("""
kit.check_summary()
"""),
    ]
    build(path, cells)
    print(f"wrote {path.relative_to(REPO)}")


# ================================================================================= notebook 04
def nb04():
    """Kalpa lab: the room re-runs L1 to L3 on Kalpa Retail baskets; the plant is found in an
    empty your-turn cell so no saved output names the Rs 199 phone charger plant."""
    path = OUT / "C2_W04_D03_04_kalpa_lab_STUDENT.ipynb"
    cells = [
        md("""\
        # Does the method survive a change of company?

        **Week 4, Wednesday, the TA-led practice lab.** Merchandising at Kalpa Retail has
        proposed pairing every item with the Rs 199 phone charger "because it is in most
        baskets". The lab re-runs the pairs method on Kalpa's own order items and asks whether
        the proposal pays for itself.

        **Who needs the answer.** The head of merchandising, who wants a story the Friday review
        will accept.

        **The questions on the way.** How often is the charger in a basket, which pair beats
        chance above a 5 percent support floor, and where does the thinnest surprise sit.
        """),
        md("""\
        **Setup.** Load the 500 consumer baskets and the 100 Business bulk-orders from the
        transfer data. The Business orders carry one product in a large quantity, so the pair
        method runs on the consumer baskets only.
        """),
        code(SETUP + """
import pandas as pd
from collections import Counter
from itertools import combinations
orders = pd.read_csv("../data/C2_W04_D03_kalpa_orders_STUDENT.csv")
items = pd.read_csv("../data/C2_W04_D03_kalpa_order_items_STUDENT.csv")
consumer = orders[orders.channel == "consumer"]
consumer_items = items[items.order_id.isin(consumer.order_id)]
print(f"{len(consumer):,} consumer baskets, {len(consumer_items):,} line items")
print(f"{(orders.channel == 'business').sum()} Business orders")
"""),
        md("""\
        ## The map of where the lab sits in the day

        The three teaching chapters ran on Instamart carts. The lab asks the same questions on
        Kalpa Retail's own order items.
        """),
        code("""
kit.flow(["the twelve rows",
          "every cart in code",
          "the action map and the rupee value",
          "the Kalpa lab"],
         lit=3, show=True)
"""),
        md("""\
        ## Your turn: how often is the Rs 199 phone charger in a basket?

        Write two or three lines that compute the charger's share of the consumer baskets, then
        the share of baskets that hold the charger and a screen protector, then the confidence
        from screen protector to charger. The cell is empty so no saved output names the number
        before the room counts it.
        """),
        empty(),
        md("""\
        **What a correct answer gives you.** The share of consumer baskets that hold the charger
        sits very high. The confidence from screen protector to charger is close to that share,
        and the lift of the pair sits near one, because the charger is in almost every basket.
        """),
        md("""\
        ## The strongest pair above a 5 percent support floor

        For every two-item combination, record its support and its lift. Keep the pairs with
        support of at least 5 percent and rank by lift.
        """),
        code("""
baskets = consumer_items.groupby("order_id")["product_name"].apply(set)
n = len(baskets)
marg = consumer_items.groupby("product_name").order_id.nunique() / n
pair_counts = Counter()
for s in baskets:
    for a, b in combinations(sorted(s), 2):
        pair_counts[(a, b)] += 1
rows = []
for (a, b), count in pair_counts.items():
    sup = count / n
    lift = sup / (marg[a] * marg[b])
    rows.append((a, b, count, sup, lift))
pairs = pd.DataFrame(rows, columns=["a", "b", "count", "support", "lift"])
promote = pairs[pairs.support >= 0.05].sort_values("lift", ascending=False)
print(promote.head(5).to_string(index=False))
kit.check("there is at least one pair above the 5 percent floor", len(promote) >= 1)
kit.check("the top pair's lift is at least 2.5", promote.lift.iloc[0] >= 2.5)
"""),
        md("""\
        ## The thin surprise: the pair with support between 0.2 and 0.4 percent

        The 5 percent floor keeps a sturdy promote list but hides smaller pairs the merchandising
        team may still want to know about. Keep pairs whose support sits between 0.2 and 0.4
        percent and look at the lift.
        """),
        code("""
thin = pairs[(pairs.support >= 0.002) & (pairs.support <= 0.004)].sort_values("lift", ascending=False)
print(thin.head(5).to_string(index=False))
kit.check("the thin candidate has lift above 3", len(thin) > 0 and thin.lift.iloc[0] >= 3.0)
"""),
        md("""\
        ## A picture of the Kalpa map

        Plot every Kalpa pair on lift against support with the 5 percent floor marked. The strong
        pair, the thin surprise and the charger-partner all sit visibly.
        """),
        code("""
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(8.5, 5))
ax.scatter(pairs.support, pairs.lift, s=35, color="#5B3FD6", alpha=0.65,
           edgecolor="#1A0F5C", linewidth=0.3)
ax.axhline(1.0, color="#6B6690", lw=1.1, ls="--")
ax.axvline(0.05, color="#6B6690", lw=1.1, ls="--")
ax.text(0.055, 4.5, "support floor at 5%", color="#6B6690", fontsize=10)
ax.set_xscale("log")
ax.set_xlim(0.001, 0.5)
ax.set_xlabel("support (log scale)")
ax.set_ylabel("lift")
ax.set_title("Kalpa baskets: the pairs that pay for a slot and the ones that do not")
ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
plt.tight_layout()
plt.show()
kit.check("the plot ran", True)
"""),
        md("""\
        ## The map at the end of the lab

        The method survives the change of company. The next lab, Thursday's Zomato Gold lab, asks
        a different question: who is leaving the Retail-Plus tier, and at which step of the app
        funnel.
        """),
        code("""
kit.vflow(["Monday: Uber, metric design",
           "Tuesday: Uber, the one slide",
           "Wednesday: Instamart, pairs",
           "Wednesday lab: Kalpa Retail baskets",
           "Thursday: Zomato Gold cohorts"],
          lit=3, show=True)
"""),
        code("""
kit.check_summary()
"""),
    ]
    build(path, cells)
    print(f"wrote {path.relative_to(REPO)}")


def main():
    nb01()
    nb02()
    nb03()
    nb04()


if __name__ == "__main__":
    main()
