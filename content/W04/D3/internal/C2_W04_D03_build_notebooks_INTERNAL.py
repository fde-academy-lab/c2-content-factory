"""Assemble and execute the eleven Wednesday notebooks, one per chapter, numbered as its SECTION.

Run from the repository root, after the generator:
    python3 content/W04/D3/internal/C2_W04_D03_build_notebooks_INTERNAL.py

Notebooks 01 to 06 and 09 are the concept chapters, each named by the row's subtopic it teaches and
counted on an invented example in data/ (the canteen's twelve orders, its month, the kirana's
month). Notebooks 07, 08 and 10 are the Instamart case chapters, and 11 is the Kalpa lab. Each
notebook runs cold in its own folder and ships executed. The prose reads its numbers from the facts
file, so a sentence and the output under it cannot disagree. Code stays small: pandas, the standard
library and matplotlib, and a three-line check defined in the notebook itself. A concept notebook's
your-turn cell is empty and comes before any cell that prints its answer, and the check under
it computes the reference and prints it only once the learner's own number exists, compared at
two decimals. The lab notebook finds Kalpa's planted values only in its empty
your-turn cells.
"""
import pathlib
import sys
import textwrap

import yaml

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
sys.path.insert(0, str(REPO / "scripts"))
from nb_make import md, code, empty, build  # noqa: E402

OUT = HERE.parent / "notebooks"
F = {r["id"]: r for rows in yaml.safe_load((HERE / "C2_W04_D03_facts_INTERNAL.yaml")
                                            .read_text(encoding="utf-8")).values() for r in rows}


def s(fid):
    return F[fid]["shown"]


def v(fid):
    return F[fid]["value"]


CHECK = '''def check(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    assert ok, name
'''
PLOT = '''import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 12, "axes.spines.top": False, "axes.spines.right": False})
'''
LABEL = ("Illustrative case: the company is real, the situation and the data are synthetic, "
         "built for this class.")


CANTEEN = '''import pandas as pd
from collections import Counter
from itertools import combinations

lines = pd.read_csv("../data/C2_W04_D03_canteen_order_lines_STUDENT.csv")
listed = lines.groupby("order_id").item.apply(list)      # the items in the order the bill lists them
baskets = listed.apply(set)                               # one set of items per order
n = len(baskets)
print("A hostel canteen's twelve lunch orders, invented for the concept chapters:")
for order_id, held in listed.items():
    print(f"  {order_id}: {', '.join(held)}")


def has(item):
    """True for every order that holds the item."""
    return baskets.apply(lambda b: item in b)


check("twelve orders and 33 order lines", n == 12 and len(lines) == 33)
'''


def concept_head(title, part, topic_line, who, questions):
    """The title cell every concept notebook opens on: the topic, who needs it, the questions."""
    return md(f"""\
    # {title}

    **Week 4, Wednesday, {part}.** The topic, in the curriculum's words: *{topic_line}*.
    {CANTEEN_LABEL}

    **Who needs the answer.** {who}

    **The questions on the way.** {questions}
    """)


CANTEEN_LABEL = ("The examples are invented for this chapter, small enough to count by hand: every "
                 "number below is counted from a table in `data/`, and the code only confirms the count.")


# ================================================================================= notebook 01
def nb01():
    path = OUT / "C2_W04_D03_01_support_by_counting_STUDENT.ipynb"
    cells = [
        concept_head(
            "Support: how often do two items share a basket?",
            "chapter 1 of the concept block",
            "Support, confidence and lift, derived by counting",
            "The canteen manager, who prints two items side by side on the combo board; without a "
            "count, the board goes to whichever pair the manager remembers selling.",
            "What is a basket? How many orders hold both roti and sabzi? Which pair is most "
            "common? What does support leave out?"),
        code(CHECK + PLOT + CANTEEN),
        md("""\
        ## How many of the twelve orders hold roti and sabzi?

        A **basket** is everything one customer pays for in one go: one bill at a kirana, one
        order at the canteen, one cart on an app. Together means in the same basket. Roti is in 4
        orders and sabzi in 4.

        **Predict before you run.** How many orders hold both?

        a) 8, since four roti orders and four sabzi orders make eight.
        b) 5, since five orders hold roti or sabzi.
        c) 3, since three orders hold roti with sabzi.
        d) 4, since every roti order also holds sabzi.
        """),
        code("""\
        roti, sabzi = has("roti"), has("sabzi")
        both = (roti & sabzi).sum()
        print(f"roti in {roti.sum()} orders, sabzi in {sabzi.sum()}")
        print(f"both {both}, roti only {(roti & ~sabzi).sum()}, sabzi only {(sabzi & ~roti).sum()}, "
              f"neither {(~roti & ~sabzi).sum()}")
        print(f"support of roti and sabzi: {both} / {n} = {both / n:.2f}")
        print(f"adding the two counts gives {roti.sum() + sabzi.sum()}, which counts the same orders twice")
        check("the four cells of the 2 by 2 add to twelve",
              both + (roti & ~sabzi).sum() + (sabzi & ~roti).sum() + (~roti & ~sabzi).sum() == n)
        check("support of roti and sabzi is 0.25", both / n == 0.25)
        """),
        md(f"""\
        **What happened.** The answer is c: T09, T10 and T11 hold both, so support is
        3 / 12 = {s('toy_canteen_roti_sabzi_support')}. **The plausible wrong answer** is 8, which
        adds the two counts and never looks inside an order, so T09 to T11 are counted twice. The
        check is the 2 by 2 table below: its four cells, both, roti only, sabzi only and neither,
        must add to twelve. Support is a rate, and its denominator is every basket, as every rate
        since Week 1 Monday named its denominator.
        """),
        code("""\
        grid = [[both, (roti & ~sabzi).sum()], [(sabzi & ~roti).sum(), (~roti & ~sabzi).sum()]]
        fig, ax = plt.subplots(figsize=(5, 4.2))
        ax.imshow([[1, 0.25], [0.25, 0.1]], cmap="Purples", vmin=0, vmax=1.6)
        for i in range(2):
            for j in range(2):
                ax.text(j, i, grid[i][j], ha="center", va="center", fontsize=24, color="#1A0F5C")
        ax.set_xticks([0, 1], ["sabzi", "no sabzi"])
        ax.set_yticks([0, 1], ["roti", "no roti"])
        ax.set_title("Twelve invented orders in a 2 by 2: support = 3 / 12")
        plt.show()
        """),
        md("""\
        ## Which pair is the most common?

        Every order adds one to the tally of every two items it holds. Sorting the two names first
        keeps "dal rice with chaas" and "chaas with dal rice" as one pair; chapter 5 explains why.
        The support of a pair is its count over all twelve orders.
        """),
        code("""\
        pair_count = Counter(p for b in baskets for p in combinations(sorted(b), 2))
        top = pair_count.most_common(6)
        for (a, b), k in top:
            print(f"{a} + {b}: {k} orders, support {k / n:.2f}")
        fig, ax = plt.subplots(figsize=(8, 3.6))
        ax.barh([f"{a} + {b}" for (a, b), _ in top][::-1], [k for _, k in top][::-1],
                color="#EEEAFB", edgecolor="#5B3FD6")
        ax.set_xlabel("orders, of the twelve, holding both")
        ax.set_title("Dal rice and chaas share the most orders")
        plt.show()
        check("dal rice and chaas share 6 orders", pair_count[("chaas", "dal rice")] == 6)
        """),
        md(f"""\
        ## What is one item's own support?

        An item on its own has a support too: its share of all baskets. Chaas is in
        {s('toy_canteen_chaas_orders')} of the twelve orders, a share of
        {s('toy_canteen_chaas_share')}, which is why four of the six most common pairs hold chaas.
        Whether the most common pair is the best one for the combo board is a different question,
        and chapter 4 answers it.
        """),
        code("""\
        single = Counter(x for b in baskets for x in b)
        share = pd.Series(single).sort_values(ascending=False) / n
        print(share.round(2).to_string())
        fig, ax = plt.subplots(figsize=(8, 3.6))
        ax.barh(share.index[::-1], share.values[::-1], color="#EEEAFB", edgecolor="#5B3FD6")
        ax.set_xlim(0, 1)
        ax.set_xlabel("share of the twelve orders holding the item")
        ax.set_title("Chaas sits in three orders of every four")
        plt.show()
        check("chaas sits in 0.75 of the orders", share["chaas"] == 0.75)
        """),
        md("""\
        ### Your turn: what is the support of papad and pickle?

        Papad is in 5 orders and pickle in 2. In the empty cell below, count the orders holding
        both and divide by all orders, the way the roti and sabzi cell did, and store the answer
        as `papad_pickle`. Then run the check under it, which compares your number with the
        reference at two decimals and shows the reference only once your number exists.
        """),
        empty(),
        code("""\
        mine = globals().get("papad_pickle")
        if mine is None:
            print("Store your answer as papad_pickle in the empty cell above, then run this cell again.")
        else:
            reference = (has("papad") & has("pickle")).sum() / n
            print(f"reference: {reference:.2f}; yours: {mine:.2f}")
            print("matches at two decimals" if abs(mine - reference) <= 0.005 else "not yet: count the orders again")
        """),
        md(f"""\
        ## What should you keep from chapter 1?

        - A basket is everything one customer pays for in one go, and together means in the same
          basket.
        - Support of a pair is the baskets holding both over all baskets, so its denominator is
          every basket: roti and sabzi {s('toy_canteen_roti_sabzi_support')}.
        - An item's own support is its share of baskets: chaas {s('toy_canteen_chaas_share')}.
        - The most common pair is a count and nothing more yet. Roti and sabzi and roti and chaas
          both read {s('toy_canteen_roti_chaas_support')}, so support cannot tell them apart;
          notebook 02 adds confidence and notebook 03 adds lift.

        **In the interview.** "What is support?" The share of all baskets that hold both items,
        said with its denominator. Chapter 7 counts it again on twelve of Instamart's carts.
        """),
    ]
    build(path, cells)
    print("wrote", path.relative_to(REPO))


# ================================================================================= notebook 02
def nb02():
    path = OUT / "C2_W04_D03_02_confidence_direction_STUDENT.ipynb"
    cells = [
        concept_head(
            "Confidence: how reliably does one item bring another?",
            "chapter 2 of the concept block",
            "Support, confidence and lift, derived by counting",
            "The canteen manager, who must decide which item the combo card is printed beside: a "
            "card aimed at the wrong buyer reads well and sells nothing.",
            'What does "of those" count? Does direction matter? How far can it swing? What can '
            "confidence not say?"),
        code(CHECK + PLOT + CANTEEN),
        md("""\
        ## Dal rice to papad reads 0.50: what does papad to dal rice read?

        **Confidence** from A to B shrinks the world to the baskets that hold A, then asks how
        many of those also hold B. It is a rate inside a segment, as Week 1 Tuesday's rates were,
        and its denominator is the segment's size. Dal rice is in 6 orders, papad in 5, both in 3.

        **Predict before you run.** What is the confidence from papad to dal rice?

        a) 0.50, since confidence reads the same both ways, like support.
        b) 0.60, since three of papad's five orders hold dal rice.
        c) 0.25, since three of all twelve orders hold both.
        d) 1.00, since every papad order holds dal rice.
        """),
        code("""\
        dal, papad = has("dal rice"), has("papad")
        both = (dal & papad).sum()
        print(f"dal rice in {dal.sum()} orders, papad in {papad.sum()}, both in {both}")
        print(f"dal rice to papad: {both} / {dal.sum()} = {both / dal.sum():.2f}")
        print(f"papad to dal rice: {both} / {papad.sum()} = {both / papad.sum():.2f}")
        check("dal rice to papad reads 0.50", both / dal.sum() == 0.5)
        check("papad to dal rice reads 0.60", both / papad.sum() == 0.6)
        """),
        md(f"""\
        **What happened.** The answer is b. From dal rice the world shrinks to its 6 orders and 3
        hold papad, {s('toy_canteen_dal_papad_conf_ab')}; from papad it shrinks to 5 orders and
        the same 3 hold dal rice, {s('toy_canteen_dal_papad_conf_ba')}. Option c is support,
        which divides by all twelve. **The trap** is reporting one direction's number for the
        other, which aims the combo card at the wrong buyer. The picture shrinks the world twice.
        """),
        code("""\
        ids = list(baskets.index)
        xy = {o: (i % 4, -(i // 4)) for i, o in enumerate(ids)}
        views = [("all twelve orders", set(ids), set()),
                 ("dal rice's orders: 3 of 6 hold papad", set(baskets[dal].index), set(baskets[dal & papad].index)),
                 ("papad's orders: 3 of 5 hold dal rice", set(baskets[papad].index), set(baskets[dal & papad].index))]
        fig, axes = plt.subplots(1, 3, figsize=(12, 3.4))
        for ax, (title, world, hit) in zip(axes, views):
            for o, (x, y) in xy.items():
                inside = o in world
                face = "#5B3FD6" if o in hit else ("#EEEAFB" if inside else "#F7F6FB")
                ax.scatter(x, y, s=520, color=face, edgecolor="#1A0F5C" if inside else "#DDD9EC", zorder=2)
                ax.text(x, y - 0.45, o, ha="center", fontsize=10, color="#1A0F5C" if inside else "#B8B2D6")
            ax.set_title(title, fontsize=12)
            ax.set_xlim(-0.6, 3.6)
            ax.set_ylim(-2.9, 0.6)
            ax.axis("off")
        plt.show()
        """),
        md("""\
        ## How far apart can the two directions sit?

        Every pair has two confidences, one from each side. The cell computes both for the 13
        pairs found in the twelve orders and plots one against the other: a point on the diagonal
        reads the same both ways.
        """),
        code("""\
        single = Counter(x for b in baskets for x in b)
        pair_count = Counter(p for b in baskets for p in combinations(sorted(b), 2))
        table = pd.DataFrame([{"a": a, "b": b, "both": k, "a_to_b": k / single[a], "b_to_a": k / single[b]}
                              for (a, b), k in pair_count.items()])
        print(table[~((table.a == "chaas") & (table.b == "dal rice"))].round(2).to_string(index=False))
        print("(chaas and dal rice is left out: it is the your-turn pair below)")
        fig, ax = plt.subplots(figsize=(6, 5.4))
        ax.plot([0, 1.05], [0, 1.05], color="#6B6690", ls="--", lw=1)
        ax.scatter(table.a_to_b, table.b_to_a, s=70, color="#5B3FD6", edgecolor="#1A0F5C", zorder=3)
        place = {("papad", "pickle"): (-8, 8, "right"), ("chaas", "sabzi"): (-8, -18, "right"),
                 ("roti", "sabzi"): (8, 4, "left"), ("dal rice", "papad"): (8, -14, "left")}
        for r in table.itertuples():
            if (r.a, r.b) in place:
                dx, dy, ha = place[(r.a, r.b)]
                ax.annotate(f"{r.a} + {r.b}", (r.a_to_b, r.b_to_a), xytext=(dx, dy), textcoords="offset points", ha=ha)
        ax.set_ylim(0, 1.15)
        ax.set_xlabel("confidence from the first item")
        ax.set_ylabel("confidence from the second item")
        ax.set_title("Off the diagonal, direction changes the number")
        plt.show()
        pp = table[(table.a == "papad") & (table.b == "pickle")].iloc[0]
        rs = table[(table.a == "roti") & (table.b == "sabzi")].iloc[0]
        check("13 pairs, each counted once", len(table) == 13)
        check("the widest swing: pickle to papad 1.00, papad to pickle 0.40", (pp.b_to_a, pp.a_to_b) == (1.0, 0.4))
        check("roti and sabzi read 0.75 both ways", rs.a_to_b == rs.b_to_a == 0.75)
        """),
        md(f"""\
        ## When do the two directions agree?

        The formula, named last: confidence from A to B is the baskets holding both over the
        baskets holding A. Both directions share the top line and differ only in the bottom one,
        so they agree only when the two items sit in the same number of baskets, as roti and
        sabzi do, 4 each. Sabzi to chaas reads {s('toy_canteen_sabzi_chaas_conf_ab')}, since every
        sabzi order holds chaas; chaas to sabzi reads {s('toy_canteen_sabzi_chaas_conf_ba')}: the
        same four orders, two sentences.
        """),
        code("""\
        ratio_ok = all(abs(r.a_to_b / r.b_to_a - single[r.b] / single[r.a]) < 1e-9 for r in table.itertuples())
        show = [("dal rice", "papad"), ("chaas", "sabzi"), ("roti", "sabzi")]
        fig, ax = plt.subplots(figsize=(8, 3.4))
        for i, (a, b) in enumerate(show):
            r = table[(table.a == a) & (table.b == b)].iloc[0]
            ax.bar(i - 0.18, r.a_to_b, 0.36, color="#5B3FD6", label="from the first" if i == 0 else None)
            ax.bar(i + 0.18, r.b_to_a, 0.36, color="#EEEAFB", edgecolor="#5B3FD6",
                   label="from the second" if i == 0 else None)
        ax.set_xticks(range(len(show)), [f"{a} + {b}" for a, b in show])
        ax.set_ylim(0, 1.15)
        ax.set_ylabel("confidence")
        ax.legend(frameon=False, ncol=2)
        ax.set_title("The same orders, read from each side")
        plt.show()
        check("for every pair, the two directions differ by the ratio of the items' counts", ratio_ok)
        """),
        md("""\
        ### Your turn: what do chaas to dal rice and dal rice to chaas read?

        In the empty cell below, compute both directions for dal rice and chaas with `has()` and
        store them as `chaas_to_dal` and `dal_to_chaas`. Then run the check under it.
        """),
        empty(),
        code("""\
        mine = (globals().get("chaas_to_dal"), globals().get("dal_to_chaas"))
        if None in mine:
            print("Store your answers as chaas_to_dal and dal_to_chaas in the empty cell above, then run this cell again.")
        else:
            both_dc = (has("dal rice") & has("chaas")).sum()
            reference = (both_dc / has("chaas").sum(), both_dc / has("dal rice").sum())
            print(f"reference: chaas to dal rice {reference[0]:.2f}, dal rice to chaas {reference[1]:.2f}")
            ok = all(abs(m - r) <= 0.005 for m, r in zip(mine, reference))
            print("both match at two decimals" if ok else "not yet: which pile is each denominator?")
        """),
        md(f"""\
        ## What should you keep from chapter 2?

        - Confidence from A to B is the baskets holding both over the baskets holding A.
        - It is written with its direction, since its denominator is A's basket count: papad to
          dal rice {s('toy_canteen_dal_papad_conf_ba')}, dal rice to papad
          {s('toy_canteen_dal_papad_conf_ab')}.
        - The two directions agree only when the two items sit in the same number of baskets.
        - Confidence alone never says whether a pair is special, since it ignores how common B is
          anyway: dal rice to chaas reads {s('toy_canteen_dal_chaas_conf_ab')}, and chaas is in
          {s('toy_canteen_chaas_orders')} of the twelve orders. Notebook 03 asks what chance
          alone would give.

        **In the interview.** "What is confidence, and why does the direction matter?" Both over
        A, so A to B and B to A divide by different baskets. Chapter 7 reads bread to milk on
        Instamart's twelve carts.
        """),
    ]
    build(path, cells)
    print("wrote", path.relative_to(REPO))


# ================================================================================= notebook 03
def nb03():
    path = OUT / "C2_W04_D03_03_chance_and_lift_STUDENT.ipynb"
    cells = [
        concept_head(
            "Chance and lift: do two items meet more often than chance?",
            "chapter 3 of the concept block",
            "Support, confidence and lift, derived by counting",
            "The canteen manager, who wants pairs that sell together more than they would anyway; "
            "a pair that merely meets as often as chance puts nothing extra on the counter.",
            "What would chance give? What is lift? Does lift have a direction? What does lift not "
            "say?"),
        code(CHECK + PLOT + CANTEEN),
        md("""\
        ## If roti and sabzi ignored each other, how many orders would hold both?

        Week 1 Thursday built a chance reference, the number a count would show if nothing were
        going on. Here it takes one multiplication. If roti and sabzi ignored each other, roti's
        orders would hold sabzi at the rate all orders do.

        **Predict before you run.** Roti is in 4 of 12 orders and sabzi in 4. By chance alone, how
        many orders hold both?

        a) 0, since items that ignore each other never meet.
        b) 1.33, a third of roti's 4 orders, if sabzi ignored roti.
        c) 3, since three orders hold both on the cards.
        d) 4, since that is roti's own count.
        """),
        code("""\
        roti, sabzi = has("roti"), has("sabzi")
        chance = n * (roti.sum() / n) * (sabzi.sum() / n)
        seen = (roti & sabzi).sum()
        print(f"chance alone: {n} x {roti.sum()}/{n} x {sabzi.sum()}/{n} = {chance:.2f} orders")
        print(f"seen: {seen} orders, so lift = {seen} / {chance:.2f} = {seen / chance:.2f}")
        check("chance gives roti and sabzi 1.33 orders", round(chance, 2) == 1.33)
        check("lift of roti and sabzi is 2.25", round(seen / chance, 2) == 2.25)
        """),
        md(f"""\
        **What happened.** The answer is b. Chance alone gives
        12 x 4/12 x 4/12 = {s('toy_canteen_roti_sabzi_expected')} orders; three are seen, so
        **lift**, the seen count over the chance count, is 3 / 1.33 =
        {s('toy_canteen_roti_sabzi_lift')}. Two misconceptions fall here: "expected" means what
        chance alone gives, never what anyone hopes to see, and two items that ignore each other
        still share baskets at their own rates. The picture puts seen beside chance for four pairs.
        """),
        code("""\
        four = [("roti", "sabzi"), ("dal rice", "papad"), ("roti", "chaas"), ("papad", "chaas")]
        rows = []
        for a, b in four:
            ha, hb = has(a), has(b)
            rows.append((f"{a} + {b}", (ha & hb).sum(), n * (ha.sum() / n) * (hb.sum() / n)))
        for name, k, e in rows:
            print(f"{name}: seen {k}, chance {e:.2f}, lift {k / e:.2f}")
        fig, ax = plt.subplots(figsize=(9, 3.8))
        x = range(len(rows))
        ax.bar([i - 0.18 for i in x], [e for _, _, e in rows], 0.36, color="#E4E1F1", edgecolor="#1A0F5C", label="chance alone")
        ax.bar([i + 0.18 for i in x], [k for _, k, _ in rows], 0.36, color="#5B3FD6", edgecolor="#1A0F5C", label="seen")
        ax.set_xticks(list(x), [name for name, _, _ in rows])
        ax.set_ylabel("orders of the twelve")
        ax.legend(frameon=False)
        ax.set_title("Above chance, at chance, below chance")
        plt.show()
        check("roti and chaas sit exactly at chance", rows[2][1] == rows[2][2])
        """),
        md(f"""\
        ## Why does lift read the same from both sides?

        The formula, named last: lift = seen / chance = both x all / (A x B) =
        3 x 12 / (4 x 4) = {s('toy_canteen_roti_sabzi_lift')}. Divided through, lift is also
        confidence over the partner's share: from roti, 0.75 / (4/12); from sabzi, the same, which
        is why lift has no direction. The picture draws it as two areas on a unit square: roti's
        band times sabzi's band is the box chance gives, and the seen box is taller.
        """),
        code("""\
        a_share, b_share = roti.mean(), sabzi.mean()
        seen_share = (roti & sabzi).mean()
        from_roti = seen_share / a_share / b_share
        from_sabzi = seen_share / b_share / a_share
        print(f"chance area {a_share * b_share:.2f}, seen area {seen_share:.2f}, lift {seen_share / (a_share * b_share):.2f}")
        print(f"second route: from roti {from_roti:.2f}, from sabzi {from_sabzi:.2f}")
        fig, axes = plt.subplots(1, 2, figsize=(8.5, 4))
        for ax, height, title in [(axes[0], b_share, "chance: roti x sabzi"), (axes[1], seen_share / a_share, "seen")]:
            ax.add_patch(plt.Rectangle((0, 0), 1, 1, color="#F7F6FB"))
            ax.add_patch(plt.Rectangle((0, 0), a_share, height, color="#5B3FD6"))
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.set_aspect("equal")
            ax.set_xlabel("share of orders with roti")
            ax.set_ylabel("share of those with sabzi")
            ax.set_title(f"{title}: {a_share * height:.2f}")
        plt.show()
        check("the second route gives 2.25 from either side", round(from_roti, 2) == round(from_sabzi, 2) == 2.25)
        """),
        md("""\
        ## What does lift say about every pair of the twelve orders?

        Lift below one means together less often than chance, exactly one means chance, and
        above one more often. The cell computes it three ways for all 13 pairs and checks that
        the three agree: seen over chance, confidence from the first over the second's share, and
        confidence from the second over the first's share. Sabzi and chaas are left out of the
        printout, since they are the your-turn pair below.
        """),
        code("""\
        single = Counter(x for b in baskets for x in b)
        pair_count = Counter(p for b in baskets for p in combinations(sorted(b), 2))
        lifts = []
        agree = True
        for (a, b), k in pair_count.items():
            one = k * n / (single[a] * single[b])
            two = (k / single[a]) / (single[b] / n)
            three = (k / single[b]) / (single[a] / n)
            agree = agree and abs(one - two) < 1e-9 and abs(one - three) < 1e-9
            lifts.append((f"{a} + {b}", k, one))
        lifts.sort(key=lambda r: r[2])
        for name, k, lift in lifts[::-1]:
            if name != "chaas + sabzi":
                print(f"{name}: lift {lift:.2f} on {k} order{'s' if k > 1 else ''}")
        fig, ax = plt.subplots(figsize=(8, 5))
        colours = ["#1F8A5B" if l > 1.001 else ("#6B6690" if l > 0.999 else "#D63A6A") for _, _, l in lifts]
        ax.barh([name for name, _, _ in lifts], [l for _, _, l in lifts], color=colours)
        ax.axvline(1, color="#1A0F5C", ls="--")
        ax.set_xlabel("lift")
        ax.set_title("Above one a pull, at one chance, below one apart")
        plt.show()
        check("the three routes to lift agree for every pair", agree)
        """),
        md("""\
        ### Your turn: what do chance and lift give sabzi and chaas?

        Sabzi is in 4 orders, chaas in 9, both in 4. In the empty cell below, compute the count
        chance alone gives the pair and its lift, and store them as `sabzi_chaas_chance` and
        `sabzi_chaas_lift`. Then run the check under it.
        """),
        empty(),
        code("""\
        mine = (globals().get("sabzi_chaas_chance"), globals().get("sabzi_chaas_lift"))
        if None in mine:
            print("Store your answers as sabzi_chaas_chance and sabzi_chaas_lift in the empty cell above, then run this cell again.")
        else:
            ref_chance = n * has("sabzi").mean() * has("chaas").mean()
            ref_lift = (has("sabzi") & has("chaas")).sum() / ref_chance
            print(f"reference: chance {ref_chance:.2f} orders, lift {ref_lift:.2f}")
            ok = abs(mine[0] - ref_chance) <= 0.005 and abs(mine[1] - ref_lift) <= 0.005
            print("both match at two decimals" if ok else "not yet: total x share x share, then seen over chance")
        """),
        md(f"""\
        ## What should you keep from chapter 3?

        - Chance alone gives a pair all baskets times A's share times B's share.
        - Lift is the seen count over the chance count, and it reads the same from both sides.
        - Lift below one means together less often than chance, near one means chance, above one
          a pull: roti and chaas sit exactly at {s('toy_canteen_roti_chaas_lift')}.
        - Lift {s('toy_canteen_roti_sabzi_lift')} never means roti makes anyone buy more sabzi.
          Only a change at the counter, tested fairly, shows cause, which is the subject of this
          week's Monday faculty session on A/B testing (tentative).

        **In the interview.** "Which of the three counts cannot be fooled by popularity?" Lift,
        because it divides by the partner's share; notebook 04 shows the trap it avoids, and
        chapters 7 and 8 read lift on Instamart's carts.
        """),
    ]
    build(path, cells)
    print("wrote", path.relative_to(REPO))


# ================================================================================= notebook 04
def nb04():
    path = OUT / "C2_W04_D03_04_confidence_trap_lift_near_one_STUDENT.ipynb"
    cells = [
        concept_head(
            "The confidence trap; lift near one: does 1.00 mean a bundle?",
            "chapter 4 of the concept block",
            "The confidence trap; lift near one",
            "The canteen manager, who is told that every dal rice order has chaas and is tempted to "
            "print chaas beside everything; a board full of chaas sells nothing that was not "
            "selling already.",
            "What is a base rate? What is dal rice to chaas worth? Does every item look bundled "
            "with chaas? Which count resists popularity?"),
        code(CHECK + PLOT + CANTEEN),
        md("""\
        ## Dal rice to chaas reads 1.00: what is their lift?

        A **base rate** is how common an item is in all baskets anyway. Chaas is in 9 of the 12
        orders, a base rate of 0.75, so it is in most of dal rice's orders whatever dal rice
        does. Every dal rice order holds chaas.

        **Predict before you run.** What is the lift of dal rice and chaas?

        a) 1.00, the same as the confidence.
        b) 1.33, the confidence over chaas's share.
        c) 2.00, twice as strong as an ordinary pair.
        d) 0.75, chaas's own share of the orders.
        """),
        code("""\
        dal, chaas = has("dal rice"), has("chaas")
        conf = (dal & chaas).sum() / dal.sum()
        chance = n * dal.mean() * chaas.mean()
        lift = (dal & chaas).sum() / chance
        print(f"dal rice to chaas: confidence {conf:.2f}; chaas's base rate {chaas.mean():.2f}")
        print(f"chance alone gives {chance:.1f} of dal rice's {dal.sum()} orders; {(dal & chaas).sum()} are seen; lift {lift:.2f}")
        print(f"second route: {conf:.2f} / {chaas.mean():.2f} = {conf / chaas.mean():.2f}")
        check("dal rice to chaas reads 1.00", conf == 1.0)
        check("their lift is only 1.33", round(lift, 2) == 1.33)
        """),
        md(f"""\
        **What happened.** The answer is b. Chance alone already puts chaas in
        {s('toy_canteen_dal_chaas_expected')} of dal rice's 6 orders, so seeing it in all 6 is
        {s('toy_canteen_dal_chaas_lift')} times chance. **The trap, exactly:** 1.00 read as a
        bundle. The decision it misleads is a combo board filled with chaas beside everything,
        which changes nothing, since chaas was going into nine orders of twelve anyway. **The
        check** is chaas's own share; **the fix** is to read lift. The picture runs the same test
        on every item in four or more orders.
        """),
        code("""\
        common = [x for x in ["dal rice", "papad", "roti", "sabzi"] if has(x).sum() >= 4]
        conf_to = pd.Series({x: (has(x) & chaas).sum() / has(x).sum() for x in common})
        lift_with = conf_to / chaas.mean()
        print(pd.DataFrame({"confidence toward chaas": conf_to, "lift with chaas": lift_with}).round(2).to_string())
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 3.6))
        a1.bar(common, conf_to, color="#5B3FD6")
        a1.axhline(chaas.mean(), color="#D63A6A", ls="--", label="chaas's base rate, 0.75")
        a1.set_ylim(0, 1.4)
        a1.legend(frameon=False, loc="upper right")
        a1.set_title("Confidence toward chaas looks strong")
        a2.bar(common, lift_with, color="#EEEAFB", edgecolor="#5B3FD6")
        a2.axhline(1, color="#1A0F5C", ls="--")
        a2.set_ylim(0, 1.6)
        a2.set_title("Lift with chaas sits near one")
        plt.show()
        check("confidence toward chaas runs 0.60 to 1.00", (conf_to.min(), conf_to.max()) == (0.6, 1.0))
        check("lift with chaas runs 0.80 to 1.33", (round(lift_with.min(), 2), round(lift_with.max(), 2)) == (0.8, 1.33))
        """),
        md("""\
        ## What does popularity do to confidence in general?

        An invented sweep makes the rule visible. A partner that ignores a popular item holds it
        at the item's own share, so its confidence toward the popular item equals that share: as
        the share climbs from 20 to 90 percent, the confidence climbs with it, and lift stays at
        one the whole way.
        """),
        code("""\
        rows = []
        for share in [x / 100 for x in range(20, 91, 5)]:
            partner_baskets = 20                        # an invented partner in 20 baskets
            holding_popular = partner_baskets * share   # it ignores the popular item
            confidence = holding_popular / partner_baskets
            rows.append((share, confidence, confidence / share))
        sweep = pd.DataFrame(rows, columns=["share", "confidence", "lift"])
        print(sweep[sweep.share.isin([0.2, 0.5, 0.9])].round(2).to_string(index=False))
        fig, ax = plt.subplots(figsize=(8, 3.6))
        ax.plot(sweep.share, sweep.confidence, color="#5B3FD6", lw=3, label="confidence toward the popular item")
        ax.plot(sweep.share, sweep.lift, color="#1F8A5B", lw=3, ls="--", label="lift")
        ax.set_xlabel("the popular item's share of baskets")
        ax.set_ylim(0, 1.2)
        ax.legend(frameon=False, loc="lower right")
        ax.set_title("Confidence follows popularity; lift divides it out")
        plt.show()
        check("lift stays at one across the sweep", (sweep.lift - 1).abs().max() < 1e-9)
        """),
        md(f"""\
        ## How close to chance does each chaas pair sit?

        The rule, named last: for a partner that ignores it, confidence toward an item equals
        that item's share, so the most popular item tops the confidence ranking beside almost
        every item, while lift stays at one. Lift with chaas has a ceiling too: a partner cannot
        hold chaas more than every time, so lift stops at one over chaas's share,
        {s('toy_chaas_lift_ceiling')}, where dal rice sits. The picture shows the four chaas pairs
        as counts: the seen orders beside the orders chance alone gives.
        """),
        code("""\
        rows = []
        for x in common:
            k = (has(x) & chaas).sum()
            e = n * has(x).mean() * chaas.mean()
            rows.append((f"{x} + chaas", k, e))
            print(f"{x} + chaas: seen {k}, chance {e:.2f}")
        fig, ax = plt.subplots(figsize=(8, 3.6))
        x = range(len(rows))
        ax.bar([i - 0.18 for i in x], [e for _, _, e in rows], 0.36, color="#E4E1F1", edgecolor="#1A0F5C", label="chance alone")
        ax.bar([i + 0.18 for i in x], [k for _, k, _ in rows], 0.36, color="#5B3FD6", edgecolor="#1A0F5C", label="seen")
        ax.set_xticks(list(x), [name for name, _, _ in rows])
        ax.set_ylabel("orders of the twelve")
        ax.legend(frameon=False)
        ax.set_title("Every chaas pair sits close to chance")
        plt.show()
        check("no chaas pair sits more than 1.5 orders from chance", all(abs(k - e) <= 1.5 for _, k, e in rows))
        """),
        md("""\
        ### Your turn: should a shop bundle a partner with its most popular item?

        An item is in 60 percent of a shop's bills, and a partner reads confidence 0.66 toward
        it. The shop bundles a pair only at a lift of 1.5 or more, the bar chapter 6 uses. In the
        empty cell below, compute the pair's lift and store it as `partner_lift`, then write in a
        comment whether the shop's rule bundles the two. Run the check under it.
        """),
        empty(),
        code("""\
        mine = globals().get("partner_lift")
        if mine is None:
            print("Store your answer as partner_lift in the empty cell above, then run this cell again.")
        else:
            reference = 0.66 / 0.60
            print(f"reference: lift {reference:.2f}; yours: {mine:.2f}")
            print("matches at two decimals" if abs(mine - reference) <= 0.005 else "not yet: confidence over the item's share")
            print("under the 1.5 bar, so the shop's rule does not bundle them" if reference < 1.5 else "over the bar")
        """),
        md(f"""\
        ## What should you keep from chapter 4?

        - A base rate is how common an item is in all baskets anyway: chaas
          {s('toy_canteen_chaas_share')}.
        - Confidence toward an item in most baskets is high from every partner, near its own
          share, so its size says nothing: {s('toy_canteen_chaas_conf_low')} to
          {s('toy_canteen_chaas_conf_high')} toward chaas.
        - Beside one item, confidence ranks the candidates by share times pull, and lift divides
          each candidate's share out: {s('toy_canteen_chaas_lift_low')} to
          {s('toy_canteen_chaas_lift_high')} with chaas.
        - Lift with an item cannot pass one over its share, {s('toy_chaas_lift_ceiling')} for
          chaas, so the item in most baskets stays near one, under the 1.5 bar, because it was
          going into the basket anyway.

        **In the interview.** A weak answer says "confidence, since dal rice to chaas is 1.00". A
        hire-grade answer says "lift, since chaas is in 0.75 of orders anyway, so 1.00 is only
        1.33 times chance". Chapter 8 meets the same trap on milk, in 71 percent of Instamart's
        carts.
        """),
    ]
    build(path, cells)
    print("wrote", path.relative_to(REPO))


# ================================================================================= notebook 05
def nb05():
    path = OUT / "C2_W04_D03_05_basket_analysis_pairs_table_STUDENT.ipynb"
    cells = [
        concept_head(
            "Basket analysis on the order items: how do lines make pairs?",
            "chapter 5 of the concept block",
            "Basket analysis on the order items",
            "Anyone who must count every pair of a real shop: a warehouse stores a bill as order "
            "lines, one row per order and item, which is how Kalpa's `order_items` and Instamart's "
            "`cart_items` are kept.",
            "What is an order line? How does a basket become pairs? How many pairs do twelve "
            "orders hold? Why sort the two names? Which pair tops the table?"),
        code(CHECK + PLOT + textwrap.dedent("""\
        import pandas as pd
        from collections import Counter
        from itertools import combinations, permutations

        lines = pd.read_csv("../data/C2_W04_D03_canteen_order_lines_STUDENT.csv")
        print("The canteen's order lines, invented: one row per order and item")
        print(lines.to_string(index=False))
        check("33 order lines in twelve orders", len(lines) == 33 and lines.order_id.nunique() == 12)
        check("eight items on the menu", lines.item.nunique() == 8)
        """)),
        md("""\
        ## How many pairs do the twelve orders hold?

        Week 2 Thursday grouped order lines by order. Here the group becomes a set of items, so
        each basket counts an item once, and every two items in a basket make a pair.

        **Predict before you run.** The twelve orders hold 33 lines. Counted once per basket, how
        many pairs do they hold?

        a) 33, one pair for every order line.
        b) 30, each order's own pairs, added up.
        c) 60, every pair, its names read both ways round.
        d) 28, every pair the eight menu items could form.
        """),
        code("""\
        baskets = lines.groupby("order_id").item.apply(set)      # one set of items per order
        t01 = sorted(baskets["T01"])
        print("T01 holds", ", ".join(t01), "and so the pairs", list(combinations(t01, 2)))
        pair_count = Counter(p for b in baskets for p in combinations(sorted(b), 2))
        print(f"pairs counted once per order: {sum(pair_count.values())}; distinct pairs: {len(pair_count)}")
        check("33 lines make 30 pairs", sum(pair_count.values()) == 30)
        check("13 distinct pairs", len(pair_count) == 13)
        """),
        md(f"""\
        **What happened.** The answer is b. A basket of three items holds three pairs, four items
        hold six, and k items hold k x (k - 1) / 2: nine three-line orders give
        {s('toy_canteen_pairs_from_three')} and three two-line orders give 3, so
        {s('toy_canteen_pair_lines')}. `combinations` of a sorted basket gives each pair once with
        its names in order (Python's itertools documentation, checked 13 October 2026). **The
        trap, exactly:** counted with its names both ways round, as `permutations` does, every pair
        counts twice and the total reads {s('toy_canteen_pair_lines_both_orders')}; left unsorted, a
        pair that two bills list in opposite orders lands under two keys and its count splits. The
        decision it misleads is a ranking built on doubled or split counts; the check is each
        basket's k x (k - 1) / 2 added up.
        """),
        code("""\
        both_orders = Counter(p for b in baskets for p in permutations(b, 2))
        print(f"every pair counted with its names both ways round: {sum(both_orders.values())} counts")
        split = Counter([*combinations(["dal rice", "chaas"], 2), *combinations(["chaas", "dal rice"], 2)])
        print(f"one pair listed both ways round on two bills, names unsorted: {len(split)} keys of {max(split.values())} each")
        size = baskets.apply(len)
        per_order = size * (size - 1) // 2
        print(f"{(size == 3).sum()} three-line orders give {per_order[size == 3].sum()}; "
              f"{(size == 2).sum()} two-line orders give {per_order[size == 2].sum()}")
        fig, ax = plt.subplots(figsize=(8, 3.2))
        ax.bar(per_order.index, per_order.values, color="#EEEAFB", edgecolor="#5B3FD6")
        ax.set_ylabel("pairs")
        ax.set_yticks([0, 1, 2, 3])
        ax.set_title("Each order adds k x (k - 1) / 2 pairs, 30 in all")
        plt.show()
        check("both name orders double the count", sum(both_orders.values()) == 2 * sum(pair_count.values()))
        check("unsorted names split one pair across two keys", len(split) == 2)
        """),
        md("""\
        ## What does the pairs table hold?

        With the pair counts and each item's own count, every pair gets chapters 1 to 3's three
        numbers: support, confidence both ways, and lift. The table is sorted by count.
        """),
        code("""\
        n = len(baskets)
        single = Counter(x for b in baskets for x in b)
        table = pd.DataFrame([{"pair": f"{a} + {b}", "both": k, "support": k / n,
                               "conf_a_to_b": k / single[a], "conf_b_to_a": k / single[b],
                               "lift": k * n / (single[a] * single[b])}
                              for (a, b), k in pair_count.items()]).set_index("pair")
        print(table.sort_values(["both", "lift"], ascending=False).round(2).to_string())
        by_count = table.sort_values(["both", "lift"], ascending=False).head(4)
        by_lift = table.sort_values(["lift", "both"], ascending=False).head(4)
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 3.4))
        a1.barh(by_count.index[::-1], by_count.both[::-1], color="#EEEAFB", edgecolor="#5B3FD6")
        a1.set_title("By count: orders holding both")
        a2.barh(by_lift.index[::-1], by_lift.lift[::-1], color="#5B3FD6")
        a2.set_title("By lift: seen over chance")
        plt.tight_layout()
        plt.show()
        r = table.loc["roti + sabzi"]
        check("roti and sabzi read back chapters 1 to 3: 3 orders, 0.25, 0.75, 2.25",
              (r.both, r.support, r.conf_a_to_b, r.lift) == (3, 0.25, 0.75, 2.25))
        """),
        md(f"""\
        ## Why do the two rankings disagree?

        By count, dal rice and chaas lead with {s('toy_canteen_dal_chaas_both')} orders at lift
        {s('toy_canteen_dal_chaas_lift')}; by lift, gulab jamun and curd lead at
        {s('toy_canteen_gulab_curd_lift')} on one order. A count rewards the popular item, and a
        lift on one order rewards luck, so the table holds counts and never a ranking: which pair
        to promote is chapter 6's decision. The grid below is the whole table at a glance, the
        orders each pair of items shares.
        """),
        code("""\
        menu = [x for x, _ in single.most_common()]
        grid = pd.DataFrame(0, index=menu, columns=menu)
        for (a, b), k in pair_count.items():
            grid.loc[a, b] = grid.loc[b, a] = k
        fig, ax = plt.subplots(figsize=(6.4, 5.6))
        ax.imshow(grid.values, cmap="Purples")
        for i in range(len(menu)):
            for j in range(len(menu)):
                if grid.iloc[i, j]:
                    ax.text(j, i, grid.iloc[i, j], ha="center", va="center", color="#1A0F5C" if grid.iloc[i, j] < 4 else "white")
        ax.set_xticks(range(len(menu)), menu, rotation=45, ha="right")
        ax.set_yticks(range(len(menu)), menu)
        ax.set_title("Orders each pair of items shares")
        plt.show()
        check("the grid is symmetric and holds every pair count twice", (grid.values == grid.values.T).all()
              and grid.values.sum() == 2 * sum(pair_count.values()))
        """),
        md("""\
        ### Your turn: how many pairs does a four-item order add?

        A thirteenth order arrives with roti, sabzi, chaas and papad. In the empty cell below,
        build its pairs with `combinations(sorted(...), 2)` and store how many there are as
        `t13_pairs`. Then run the check under it.
        """),
        empty(),
        code("""\
        mine = globals().get("t13_pairs")
        if mine is None:
            print("Store your answer as t13_pairs in the empty cell above, then run this cell again.")
        else:
            reference = len(list(combinations(sorted({"roti", "sabzi", "chaas", "papad"}), 2)))
            print(f"reference: {reference} pairs; yours: {mine}")
            print("matches" if mine == reference else "not yet: list the pairs one by one")
        """),
        md(f"""\
        ## What should you keep from chapter 5?

        - Group the order lines by order into a set of items, so each basket counts an item once.
        - Count every two items in a basket with the two names sorted, so each pair has one key.
        - A one-item basket adds no pair, and k items add k x (k - 1) / 2:
          {s('toy_canteen_lines')} lines made {s('toy_canteen_pair_lines')} pairs here.
        - The table holds counts; which pair to promote is the next chapter's decision.

        **In the interview.** "Why sort the pair's names before counting?" So that each pair has
        one key and no count is split or doubled. Chapter 8 runs these lines on 40,000 Instamart
        carts, and the lab on Kalpa's `order_items`.
        """),
    ]
    build(path, cells)
    print("wrote", path.relative_to(REPO))


# ================================================================================= notebook 06
def nb06():
    path = OUT / "C2_W04_D03_06_support_floor_watch_list_STUDENT.ipynb"
    cells = [
        concept_head(
            "The support floor and the watch list: when is a pair too thin?",
            "chapter 6 of the concept block",
            "The support floor and the watch list",
            "The canteen manager, who sees gulab jamun and curd read lift 6.0, the canteen's "
            "strongest pair, and must decide whether one order is enough to print a combo card.",
            "How much can luck move a lift? What is a floor? What does a watch list do? Where does "
            "each pair go?"),
        code(CHECK + PLOT + textwrap.dedent("""\
        import pandas as pd
        from collections import Counter
        from itertools import combinations

        lines = pd.read_csv("../data/C2_W04_D03_canteen_order_lines_STUDENT.csv")
        month = pd.read_csv("../data/C2_W04_D03_canteen_month_STUDENT.csv")
        baskets = lines.groupby("order_id").item.apply(set)
        month_baskets = month.groupby("order_id").item.apply(set)
        print(f"the twelve orders, invented: {len(lines)} lines in {len(baskets)} orders")
        print(f"a month of the canteen, invented so that no item depends on another: "
              f"{len(month_baskets)} orders, {month.item.nunique()} items, {len(month):,} lines")


        def pairs_of(bs):
            \"\"\"Every pair found in the baskets, with the orders holding both, chance, and lift.\"\"\"
            n = len(bs)
            single = Counter(x for b in bs for x in b)
            count = Counter(p for b in bs for p in combinations(sorted(b), 2))
            return pd.DataFrame([{"a": a, "b": b, "both": k, "chance": single[a] * single[b] / n,
                                  "lift": k * n / (single[a] * single[b])} for (a, b), k in count.items()])


        canteen = pairs_of(baskets)
        check("600 orders and 14 items in the month", len(month_baskets) == 600 and month.item.nunique() == 14)
        """)),
        md("""\
        ## In 600 orders of pure chance, how high can a lift go?

        Week 1 Thursday's rule was to distrust any rate built on fewer than thirty observations.
        Gulab jamun and curd read lift 6.0 on one of the twelve orders. The month below was
        invented so that no item depends on another: every item goes into an order on its own
        coin, so nothing pulls any pair together, and since an order must hold at least one item,
        every true lift sits a shade under one.

        **Predict before you run.** On one or two orders, how high can a lift read?

        a) About 1.2, since items that ignore each other stay near one.
        b) About 2, since luck can double a lift and no more.
        c) About 3, since luck can triple it.
        d) Above 6, more than six times chance.
        """),
        code("""\
        m = pairs_of(month_baskets)
        thin, thick = m[m.both <= 2], m[m.both >= 30]
        top = thin.sort_values("lift").iloc[-1]
        one = m[m.both == 1].sort_values("lift").iloc[-1]
        print(f"{len(m)} pairs; {len(thin)} sit on one or two orders")
        print(f"strongest of those: {top.a} + {top.b}, lift {top.lift:.2f} on {top.both} orders, "
              f"where chance gives {top.chance:.2f}")
        print(f"strongest pair on a single order: lift {one.lift:.2f}")
        print(f"{len(thick)} pairs on 30 or more orders read lift {thick.lift.min():.2f} to {thick.lift.max():.2f}")
        check("a thin pair reads lift above 6 in a month of pure chance", top.lift > 6)
        check("every pair on thirty or more orders sits near one", thick.lift.between(0.85, 1.05).all())
        """),
        md(f"""\
        **What happened.** The answer is d. Nothing in this month pulls any item toward another,
        yet gulab jamun and jalebi read lift {s('toy_month_thin_top_lift')} on
        {s('toy_month_thin_top_orders')} orders, where chance gives
        {s('toy_month_thin_top_expected')}. The {s('toy_month_thick_pairs')} pairs on 30 or more
        orders read {s('toy_month_thick_low')} to {s('toy_month_thick_high')}, a shade under one.
        In between, {s('toy_month_mid_over_bar')} pairs on 4 to 7 orders still pass 1.5, up to
        {s('toy_month_mid_top_lift')}, and none on {s('toy_month_bar_safe_orders')} or more orders
        does. A lift on a handful of baskets says more about luck than about the pair. The picture
        reads left to right: wild on the left, flat on the right.
        """),
        code("""\
        mid = m[(m.both > 2) & (m.both < 30)]
        fig, ax = plt.subplots(figsize=(9, 4))
        ax.scatter(mid.both, mid.lift, s=40, color="#6B6690", alpha=0.6, label="3 to 29 orders")
        ax.scatter(thin.both, thin.lift, s=70, color="#D63A6A", edgecolor="#1A0F5C", label="one or two orders")
        ax.scatter(thick.both, thick.lift, s=70, color="#1F8A5B", edgecolor="#1A0F5C", label="30 or more orders")
        ax.axhline(1, color="#1A0F5C", ls="--")
        ax.axvline(30, color="#6B6690", ls=":")
        ax.set_xscale("log")
        ax.set_xticks([1, 2, 5, 10, 30, 100, 200], ["1", "2", "5", "10", "30", "100", "200"])
        ax.minorticks_off()
        ax.set_xlabel("orders holding both (each step right is more orders)")
        ax.set_ylabel("lift")
        ax.legend(frameon=False)
        ax.set_title("600 invented orders, no item depending on another")
        plt.show()
        """),
        md(f"""\
        ## Where does each canteen pair go once a floor is set?

        A **support floor** is the fewest baskets a pair must sit in before anyone acts on its
        lift. It is a decision, stated as a count before the ranking is read, and it belongs where
        luck stops carrying a lift past the bar: {s('toy_month_bar_safe_orders')} orders in the
        month above, Week 1's thirty when no such month is to hand, 1 percent of the carts in the
        case. Twelve orders are too few for any floor, so a floor of 3 here only shows the sort.
        The rule, named last: read a lift only at or above the floor, and promote only at a lift
        of 1.5 or more. That sorts every pair into four regions: promote, watch (strong but thin),
        trap (near one on plenty of baskets) and ignore. Roti and sabzi, 2.25 on three orders,
        lands in promote and would still be trialled first.
        """),
        code("""\
        FLOOR, BAR = 3, 1.5     # orders, lift


        def region(k, lift):
            strong = lift >= BAR
            if k >= FLOOR:
                return "promote" if strong else "trap"
            return "watch" if strong else "ignore"


        canteen["region"] = [region(k, l) for k, l in zip(canteen.both, canteen.lift)]
        print(canteen.sort_values("lift", ascending=False).round(2).to_string(index=False))
        colour = {"promote": "#1F8A5B", "watch": "#C98A00", "trap": "#D63A6A", "ignore": "#B8B2D6"}
        fig, ax = plt.subplots(figsize=(8, 4.4))
        ax.axvline(FLOOR - 0.5, color="#6B6690", ls="--")
        ax.axhline(BAR, color="#6B6690", ls=":")
        ax.axhline(1, color="#1A0F5C", lw=0.8)
        for r in canteen.itertuples():
            ax.scatter(r.both, r.lift, s=90, color=colour[r.region], edgecolor="#1A0F5C", zorder=3)
        place = {("curd", "gulab jamun"): (10, -4, "left"), ("papad", "pickle"): (-8, 10, "right"),
                 ("roti", "sabzi"): (10, -4, "left"), ("pickle", "roti"): (10, 4, "left"),
                 ("chaas", "dal rice"): (-8, 10, "right")}
        for r in canteen.itertuples():
            if (r.a, r.b) in place:
                dx, dy, ha = place[(r.a, r.b)]
                ax.annotate(f"{r.a} + {r.b}", (r.both, r.lift), xytext=(dx, dy), textcoords="offset points", ha=ha)
        ax.set_xlim(0.5, 6.8)
        ax.set_xlabel("orders holding both")
        ax.set_ylabel("lift")
        ax.set_title("Floor 3 orders, bar 1.5: promote, watch, trap, ignore")
        plt.show()
        promote = canteen[canteen.region == "promote"]
        check("only roti and sabzi are promoted", list(zip(promote.a, promote.b)) == [("roti", "sabzi")])
        check("papad and pickle, and gulab jamun and curd, go on the watch list",
              {("papad", "pickle"), ("curd", "gulab jamun")} <= set(zip(canteen[canteen.region == "watch"].a,
                                                                         canteen[canteen.region == "watch"].b)))
        """),
        md(f"""\
        ## What does a watch list do with a strong pair below the floor?

        A pair above the bar and below the floor goes on a **watch list**: the pair, its lift and
        its count, a trial (where, for how long, and against which other half of customers) and a
        pass rule written before the trial starts. A **pass rule** says what the trial must show:
        the half that sees the pair buys it more often than the other half, by a gap fixed in
        advance. Gulab jamun and curd, lift
        {s('toy_canteen_gulab_curd_lift')} on one order, earn a trial and never a printed card. How
        long a trial must run is a sample-size question for the IITGN faculty session (tentative).
        The picture shows why the floor is a decision: lower it and the one-order pairs flood in.
        """),
        code("""\
        floors = range(1, 7)
        promoted = [sum(1 for k, l in zip(canteen.both, canteen.lift) if k >= f and l >= BAR) for f in floors]
        watched = [sum(1 for k, l in zip(canteen.both, canteen.lift) if k < f and l >= BAR) for f in floors]
        fig, ax = plt.subplots(figsize=(8, 3.4))
        ax.plot(list(floors), promoted, marker="o", color="#1F8A5B", lw=2, label="promoted")
        ax.plot(list(floors), watched, marker="o", color="#C98A00", lw=2, label="watched")
        ax.set_xlabel("support floor, orders")
        ax.set_ylabel("pairs")
        ax.legend(frameon=False)
        ax.set_title("A lower floor promotes the lucky pairs")
        plt.show()
        check("a floor of one order would promote gulab jamun and curd; a floor of three does not",
              region(1, 6.0) == "watch" and promoted[0] > promoted[2])
        """),
        md("""\
        ### Your turn: which of the month's pairs clear a floor of 15 orders?

        In the empty cell below, keep the month's pairs (`m`) on at least 15 orders, and store
        how many there are as `floor15_count` and their lowest and highest lift, as a pair of
        numbers, as `floor15_range`. Then run the check under it, and say in a comment whether any
        of them would pass the 1.5 bar.
        """),
        empty(),
        code("""\
        mine = (globals().get("floor15_count"), globals().get("floor15_range"))
        if None in mine:
            print("Store your answers as floor15_count and floor15_range in the empty cell above, then run this cell again.")
        else:
            ref = m[m.both >= 15]
            print(f"reference: {len(ref)} pairs, lift {ref.lift.min():.2f} to {ref.lift.max():.2f}")
            ok = (mine[0] == len(ref) and abs(min(mine[1]) - ref.lift.min()) <= 0.005
                  and abs(max(mine[1]) - ref.lift.max()) <= 0.005)
            print("matches at two decimals" if ok else "not yet: filter on both >= 15 first")
        """),
        md(f"""\
        ## What should you keep from chapter 6?

        - A lift on one or two baskets swings by luck: {s('toy_month_thin_top_lift')} on
          {s('toy_month_thin_top_orders')} orders in a month where every true lift is one.
        - The floor is a count of baskets set where luck stops carrying a lift past the bar,
          before the ranking is read: {s('toy_month_bar_safe_orders')} orders in the month,
          {s('toy_canteen_floor_orders')} on the twelve only to show the sort.
        - A strong pair below the floor goes on a watch list: a trial on a random half of
          customers, its pass rule written first, shows whether the pull is real and whether it
          sells.
        - A pair near one is never promoted: below the floor it is ignored, and above it, where a
          count ranks it first, it is the trap.

        **In the interview.** "A pair has a high lift on very few baskets; act or not?" Watch it:
        test it on a random half of customers with a pass rule set first. Chapter 7 refuses a
        lift of 12 on one Instamart cart, and chapter 10 sets the case's floor at 1 percent of
        carts.
        """),
    ]
    build(path, cells)
    print("wrote", path.relative_to(REPO))


# ================================================================================= notebook 07
def nb07():
    path = OUT / "C2_W04_D03_07_case_three_measures_twelve_carts_STUDENT.ipynb"
    cells = [
        md(f"""\
        # Twelve carts by hand, with support, confidence and lift and the confidence trap: what do twelve carts say?

        **Week 4, Wednesday, chapter 7, the first case chapter.** Swiggy Instamart, Pune: the
        cart page shows a strip of three suggested items under the cart. On {s('change_date')} the
        strip stopped showing a curated list and started showing the items most often found in
        the same cart. Toned milk sits in {s('toned_milk_share')} of Pune carts, so it now appears
        beside nearly everything, and the strip's click-through (clicks over impressions, an
        impression being one showing of one slot) fell from {s('before_strip_ctr')} in the three
        weeks before to {s('after_strip_ctr')} in the three weeks after. The ask, due Friday: rank
        the pairs the strip should show, explain the fall, and put a rupee value on a slot.
        {LABEL}

        **Applies:** Support, confidence and lift, derived by counting (chapters 1 to 3,
        notebooks 01 to 03); The confidence trap; lift near one (chapter 4, notebook 04); The
        support floor and the watch list (chapter 6, notebook 06).

        **Who needs the answer.** The category manager, who decides which products are promoted,
        and the growth lead, who owns the strip's clicks and orders and must explain the fall at
        Friday's review, the weekly meeting where both defend their numbers. A strip filled on the
        wrong count wastes the three most-clicked spaces on the cart page.

        **The questions on the way.** How often do two items turn up in the same cart? How
        reliably does one bring the other? Do they turn up together more than chance would put
        them there? What can twelve carts not tell us?
        """),
        code(CHECK + PLOT + "import pandas as pd\nprint(\"ready: pandas\", pd.__version__)"),
        md("""\
        ## What do twelve carts from the case hold?

        These are twelve of the 40,000 Pune carts, printed as cards on each table. Each row is a
        cart and each column an item: 1 if the cart holds it. Count by hand first, as the canteen's
        orders were counted; the code below only confirms the count.
        """),
        code("""\
        twelve = pd.read_csv("../data/C2_W04_D03_twelve_rows_STUDENT.csv").set_index("cart_id")
        for cart_id, row in twelve.iterrows():
            print(cart_id, ", ".join(row.index[row == 1]))
        held = twelve.sum().sort_values()
        fig, ax = plt.subplots(figsize=(8, 4.2))
        ax.barh(held.index, held.values, color="#EEEAFB", edgecolor="#5B3FD6")
        ax.set_xlabel("carts, of the twelve, holding the item")
        ax.set_title("Milk is in 8 of the 12 carts")
        plt.show()
        check("twelve carts", len(twelve) == 12)
        """),
        md(f"""\
        ## How reliably does bread bring milk on the twelve carts?

        Bread is in {s('twelve_bread')} carts and milk in {s('twelve_milk')}.

        **Predict before you run.** What is the confidence from bread to milk?

        a) 0.33
        b) 0.50
        c) 0.75
        d) 1.00
        """),
        code("""\
        n = len(twelve)
        bread, milk = twelve["bread"] == 1, twelve["toned milk"] == 1
        both = (bread & milk).sum()
        conf = both / bread.sum()
        expected = n * (bread.sum() / n) * (milk.sum() / n)
        lift = both / expected
        print(f"bread {bread.sum()}, milk {milk.sum()}, both {both}")
        print(f"support {both / n:.2f}, confidence bread to milk {conf:.2f}, milk to bread {both / milk.sum():.2f}")
        print(f"expected together {expected:.2f}, seen {both}, lift {lift:.2f}")
        check("every bread cart holds milk", conf == 1.0)
        check("lift is 1.50 on the twelve", round(lift, 2) == 1.50)
        """),
        md(f"""\
        **What happened.** The answer is d: all four bread carts hold milk, so confidence reads
        {s('twelve_bread_milk_conf')}. That is chapter 4's trap, met again: dal rice to chaas read
        1.00 at the canteen. A hurried analyst reads 1.00 as "every bread buyer wants milk, so put
        milk in the bread cart's strip". The check is the count the confidence never looked at:
        milk was already in 8 of 12 carts, so chance alone puts it in about 2.67 of the four bread
        carts, and lift is 4 / 2.67 = {s('twelve_bread_milk_lift')}. Four carts are too few to say
        more, which is chapter 6's floor; chapter 8 runs the same count on 40,000. The 2 by 2 below
        is chapter 1's table, drawn for bread and milk.
        """),
        code("""\
        grid = [[(bread & milk).sum(), (bread & ~milk).sum()], [(milk & ~bread).sum(), (~bread & ~milk).sum()]]
        fig, ax = plt.subplots(figsize=(5, 4.2))
        ax.imshow([[1, 0.25], [0.25, 0.1]], cmap="Purples", vmin=0, vmax=1.6)
        for i in range(2):
            for j in range(2):
                ax.text(j, i, grid[i][j], ha="center", va="center", fontsize=24, color="#1A0F5C")
        ax.set_xticks([0, 1], ["milk", "no milk"])
        ax.set_yticks([0, 1], ["bread", "no bread"])
        ax.set_title("Twelve carts in a 2 by 2: bread and milk")
        plt.show()
        check("the 2 by 2 adds to twelve", sum(map(sum, grid)) == n)
        """),
        code("""\
        rows = []
        for a, b in [("bread", "toned milk"), ("chips", "cold drink"), ("ice cream", "chocolate sauce")]:
            has_a, has_b = twelve[a] == 1, twelve[b] == 1
            both = (has_a & has_b).sum()
            rows.append({"pair": f"{a} + {b}", "carts_a": has_a.sum(), "carts_b": has_b.sum(), "both": both,
                         "expected": has_a.sum() * has_b.sum() / n, "support": both / n,
                         "confidence": both / has_a.sum(), "lift": both * n / (has_a.sum() * has_b.sum())})
        counts = pd.DataFrame(rows).set_index("pair")
        for pair in ["chips + cold drink", "ice cream + chocolate sauce"]:
            r = counts.loc[pair]
            print(f"{pair}: {r.carts_a:.0f} and {r.carts_b:.0f} carts, both {r.both:.0f}, support {r.support:.2f}, "
                  f"confidence {r.confidence:.2f}, lift {r.lift:.2f}")
        check("chips and cold drink: lift 2.67", round(counts.loc["chips + cold drink", "lift"], 2) == 2.67)
        check("ice cream and chocolate sauce: one cart, lift 12", counts.loc["ice cream + chocolate sauce", "both"] == 1)
        """),
        md("""\
        ## Which pair beat chance on the twelve, and which number should nobody act on?

        Chips and cold drink sit in 3 carts each and together in 2, where chance gives 0.75: lift
        2.67. Ice cream and chocolate sauce share one cart, and one cart makes a lift of 12, a
        number with nothing under it, which chapter 6's floor refuses. The loop above writes lift
        as both x n / (A x B), which is seen over expected rearranged: for bread and milk,
        4 / (12 x 4/12 x 8/12) is the same as 4 x 12 / (4 x 8), which is 1.50. The picture puts
        seen beside expected for the three pairs.
        """),
        code("""\
        fig, ax = plt.subplots(figsize=(8, 3.6))
        x = range(len(counts))
        ax.bar([i - 0.18 for i in x], counts.expected, 0.36, color="#E4E1F1", edgecolor="#1A0F5C", label="expected by chance")
        ax.bar([i + 0.18 for i in x], counts.both, 0.36, color="#5B3FD6", edgecolor="#1A0F5C", label="seen")
        ax.set_xticks(list(x), counts.index)
        ax.set_ylabel("carts of the twelve")
        ax.legend(frameon=False)
        ax.set_title("Lift is seen over expected")
        plt.show()
        check("every pair here was seen more often than chance", (counts.both > counts.expected).all())
        """),
        md(f"""\
        ## What did the twelve carts answer?

        - **How often?** Support counts carts with both: bread and milk 4 of 12, chips and cold
          drink 2 of 12.
        - **How reliably?** Confidence shrinks the world to the carts with A: bread to milk 4 of 4,
          {s('twelve_bread_milk_conf')}.
        - **Against chance?** Lift divides seen by expected: bread and milk
          {s('twelve_bread_milk_lift')}, chips and cold drink {s('twelve_chips_cold_lift')}, ice
          cream and chocolate sauce 12 on a single cart.
        - **What can twelve carts not tell us?** Whether 1.50 is a real pull or four lucky carts.
          Chapter 8 counts all 40,000.

        **In the interview.** "Support, confidence, lift: what does each answer?" The answer names
        three questions: how often, how reliably, and against chance.
        """),
    ]
    build(path, cells)
    print("wrote", path.relative_to(REPO))


# ================================================================================= notebook 08
def nb08():
    path = OUT / "C2_W04_D03_08_case_pairs_table_confidence_trap_STUDENT.ipynb"
    cells = [
        md(f"""\
        # Basket analysis on 40,000 carts, with lift near one and the floor: what do 40,000 carts say?

        **Week 4, Wednesday, chapter 8, the second case chapter.** Swiggy Instamart, Pune. Since
        {s('change_date')} the cart page's three-slot strip shows the items most often found in
        the same cart, and its click-through fell from {s('before_strip_ctr')} to
        {s('after_strip_ctr')}. {LABEL} Chapter 7 counted twelve carts: bread to milk read
        confidence {s('twelve_bread_milk_conf')} and lift {s('twelve_bread_milk_lift')}, chips and
        cold drink lift {s('twelve_chips_cold_lift')}. This notebook runs the same three counts on
        every cart.

        **Applies:** Support, confidence and lift, derived by counting (chapters 1 to 3,
        notebooks 01 to 03); The confidence trap; lift near one (chapter 4, notebook 04); Basket
        analysis on the order items (chapter 5, notebook 05); The support floor and the watch list
        (chapter 6, notebook 06).

        **Who needs the answer.** The growth lead, who must say on Friday why the click-through
        fell, and the category manager, who will defend milk because it is the top seller.

        **The questions on the way.** How often is each item in a cart? Which pairs sit together
        most often, and is that the ranking the strip should use? What does lift say about milk?
        Why did the click-through fall?
        """),
        code(CHECK + PLOT + textwrap.dedent("""\
        import pandas as pd
        from collections import Counter
        from itertools import combinations

        carts = pd.read_csv("../data/C2_W04_D03_carts_STUDENT.csv")
        items = pd.read_csv("../data/C2_W04_D03_cart_items_STUDENT.csv")
        n = len(carts)
        print(f"{n:,} carts from {carts.customer_id.nunique():,} customers, "
              f"{len(items):,} item lines, {items.item.nunique()} items")
        check("40,000 carts", n == 40_000)
        check("every item line belongs to a cart", items.cart_id.isin(carts.cart_id).all())
        """)),
        md("""\
        ## How often is each item in a cart?

        An item's support on its own is its share of carts. `cart_items` has one row per item in
        a cart, so counting distinct carts per item gives it.
        """),
        code("""\
        share = items.groupby("item").cart_id.nunique().sort_values(ascending=False) / n
        top = share.head(12)
        fig, ax = plt.subplots(figsize=(8, 4.2))
        ax.barh(top.index[::-1], top.values[::-1] * 100, color="#EEEAFB", edgecolor="#5B3FD6")
        ax.set_xlabel("percent of the 40,000 carts")
        ax.set_title(f"Toned milk is in {share['toned milk']:.0%} of carts")
        plt.show()
        print(share.head(12).round(3).to_string())
        check("milk is the most common item", share.index[0] == "toned milk")
        """),
        md("""\
        ## Which pairs sit together most often?

        The strip's new rule ranks by exactly this count. These are notebook 05's lines on the
        canteen, unchanged: every cart's items, taken two at a time, add one to their pair's tally,
        so a cart holding bread, eggs and milk gives three pairs, (bread, eggs), (bread, milk) and
        (eggs, milk), and sorting the items first keeps (bread, milk) and (milk, bread) as one key.

        **Predict before you run.** Which pair is found together most often?

        a) chips and cold drink
        b) bread and toned milk
        c) ice cream and chocolate sauce
        d) onions and tomatoes
        """),
        code("""\
        baskets = items.groupby("cart_id").item.apply(set)          # one set of items per cart
        pair_count = Counter(p for basket in baskets                 # for every cart,
                             for p in combinations(sorted(basket), 2))  # every two of its items
        for (a, b), k in pair_count.most_common(6):
            print(f"{a} + {b}: {k:,} carts")
        check("the most frequent pair holds milk", "toned milk" in pair_count.most_common(1)[0][0])
        """),
        md(f"""\
        **What happened.** The answer is b, bread and milk in {s('bread_milk_carts')} carts, and
        every one of the six most frequent pairs holds milk. **The plausible wrong answer** is "the
        pairs table is the ranking": the most frequent partner of almost any item is milk, so a
        strip ranked by count shows milk beside everything, which is what the strip did from
        7 September. A count rewards the popular item, whatever it is paired with.
        """),
        code("""\
        single = Counter(x for basket in baskets for x in basket)   # carts holding each item
        # lift: carts with both times all carts, over the two items' own counts (seen over expected)
        table = pd.DataFrame([{"a": a, "b": b, "both": k, "support": k / n,
                               "conf_a_to_b": k / single[a], "conf_b_to_a": k / single[b],
                               "lift": k * n / (single[a] * single[b])}
                              for (a, b), k in pair_count.items()])
        featured = [("bread", "toned milk"), ("eggs", "toned milk"), ("chips", "cold drink"),
                    ("chocolate sauce", "ice cream")]
        show = table.set_index(["a", "b"]).loc[featured].round(4)
        print(show.to_string())
        check("chips and cold drink: lift 3.39", round(show.loc[("chips", "cold drink"), "lift"], 2) == 3.39)
        """),
        md(f"""\
        ## What does lift say about bread and milk that confidence does not?

        Bread to milk reads confidence {s('bread_milk_conf_ab')} on 40,000 carts. On the twelve
        carts lift read {s('twelve_bread_milk_lift')}, because all four bread carts happened to hold
        milk; on 40,000 carts it reads {s('bread_milk_lift')}, which says milk sits beside bread
        about as often as it sits in any cart. The picture draws lift as two areas: bread's share
        times milk's share is the overlap chance would give; the overlap seen is barely bigger.
        Chapter 6's lesson on the case: a few carts can make a pull look strong.
        """),
        code("""\
        b, m = single["bread"] / n, single["toned milk"] / n
        seen = pair_count[("bread", "toned milk")] / n
        print(f"bread {b:.2f} x milk {m:.2f} = {b * m:.3f} expected; seen {seen:.3f}; lift {seen / (b * m):.2f}")
        fig, axes = plt.subplots(1, 2, figsize=(9, 4))
        for ax, height, title in [(axes[0], m, "expected: bread x milk"), (axes[1], seen / b, "seen")]:
            ax.add_patch(plt.Rectangle((0, 0), b, 1, color="#EEEAFB"))
            ax.add_patch(plt.Rectangle((0, 0), b, height, color="#5B3FD6"))
            ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_aspect("equal")
            ax.set_xlabel("share of carts with bread"); ax.set_ylabel("share of those with milk")
            ax.set_title(f"{title}: {b * height:.3f}")
        plt.show()
        check("bread to milk: confidence 0.74, lift 1.04", round(seen / b, 2) == 0.74 and round(seen / (b * m), 2) == 1.04)
        """),
        md(f"""\
        ## Does every popular item look bundled with milk?

        **Predict before you run.** For the {s('common_items')} items found in at least 2 percent
        of carts, what does their lift with milk look like?

        a) It rises with the item's popularity.
        b) It sits near one for all of them.
        c) It falls with the item's popularity.
        d) It scatters, each item its own way.
        """),
        code("""\
        common = share[(share >= 0.02) & (share.index != "toned milk")].index
        conf_milk = pd.Series({x: pair_count[tuple(sorted((x, "toned milk")))] / single[x] for x in common})
        lift_milk = conf_milk / share["toned milk"]
        print(f"{len(common)} items: confidence to milk {conf_milk.min():.2f} to {conf_milk.max():.2f}, "
              f"lift {lift_milk.min():.2f} to {lift_milk.max():.2f}")
        fig, ax = plt.subplots(figsize=(8, 3.8))
        ax.scatter(share[common] * 100, lift_milk, color="#5B3FD6")
        ax.axhline(1, color="#6B6690", ls="--")
        ax.set_ylim(0, 2); ax.set_xlabel("percent of carts holding the item"); ax.set_ylabel("lift with milk")
        ax.set_title("Lift with milk sits near one, whatever the item's popularity")
        plt.show()
        check("every common item's lift with milk sits between 0.96 and 1.08", lift_milk.between(0.96, 1.08).all())
        """),
        md(f"""\
        **What happened.** The answer is b. Confidence toward milk sits near milk's own share for
        every item, because most carts hold milk whatever else they hold, and lift divides that
        share out. Milk's own share, how common it is in all carts, is its **base rate**:
        {s('toned_milk_share')}. This is chapter 4's chaas at the scale of a city, ceiling and all:
        no item's lift with milk can pass one over milk's share, {s('milk_lift_ceiling')}. Amazon met the
        same trap: counting how often buyers of A also bought B would have made the bestseller the
        top recommendation beside everything, and the fix scored how much more likely buyers of A
        were to buy B than the average customer, a difference in probabilities where lift takes a
        ratio (Amazon Science, checked 13 October 2026).
        """),
        md(f"""\
        ## Why did the strip's click-through fall from {s('before_strip_ctr')} to {s('after_strip_ctr')}?

        `strip_log` counts each day's impressions (times a slot was shown), clicks and adds (the
        suggestions put in the cart), by slot, by the anchor item (the cart item a suggestion sits
        beside) and by the suggested item. Every cart-page view shows all three slots. Each pack
        size of toned milk is its own suggestion, so milk can fill two slots on one view; the log
        names every pack by its item.

        **Predict before you run.** Which explanation will the log support?

        a) Shoppers' habits changed after the monsoon.
        b) Fewer people opened the cart page in September.
        c) Milk now fills the slots and is rarely clicked.
        d) The strip sits lower on the page than it did.
        """),
        code("""\
        log = pd.read_csv("../data/C2_W04_D03_strip_log_STUDENT.csv", parse_dates=["date"])
        log["after"] = log.date >= "2026-09-07"
        day = log.groupby("date")[["impressions", "clicks"]].sum()
        fig, ax = plt.subplots(figsize=(9, 3.4))
        ax.plot(day.index, day.clicks / day.impressions * 100, marker="o", ms=3, color="#5B3FD6")
        ax.axvline(pd.Timestamp("2026-09-07"), color="#D63A6A", ls="--")
        ax.set_ylabel("click-through, %"); ax.set_title("Daily strip click-through, 17 August to 27 September")
        plt.show()
        window = log.groupby("after")[["impressions", "clicks"]].sum()
        print((window.clicks / window.impressions).round(4).rename({False: "before", True: "after"}).to_string())
        check("6.1 percent before, 3.8 after", [round(x, 3) for x in window.clicks / window.impressions] == [0.061, 0.038])
        """),
        md("""\
        ### Your turn: which slots does the fall sit in?

        A blended rate is a mix of the rates of its parts, each weighted by its share: if half
        the impressions clicked at 2 percent and half at 8, the strip would read 5. Split the
        after-change rows by whether the slot suggested toned milk. For each group print its share
        of impressions and its click-through (clicks over impressions), then check that the two
        rates, weighted by their shares, give back the blended rate. Start from
        `after = log[log.after]` and `after.suggested_item == "toned milk"`.
        """),
        empty(),
        code("""\
        after = log[log.after]
        is_milk = after.suggested_item == "toned milk"
        part = after.groupby(is_milk)[["impressions", "clicks"]].sum()
        ctr = part.clicks / part.impressions
        weight = part.impressions / part.impressions.sum()
        print(f"milk: {weight[True]:.0%} of impressions at {ctr[True]:.1%}; "
              f"everything else: {weight[False]:.0%} at {ctr[False]:.1%}")
        print(f"weighted back together: {(ctr * weight).sum():.1%}")
        before = log[~log.after]
        part_b = before.groupby(before.suggested_item == "toned milk")[["impressions", "clicks"]].sum()
        print(f"before the change: milk {part_b.impressions[True] / part_b.impressions.sum():.0%} of impressions; "
              f"everything else at {part_b.clicks[False] / part_b.impressions[False]:.1%}")
        check("milk slots click at 1.2 percent and the rest at 6.4", round(ctr[True], 3) == 0.012 and round(ctr[False], 3) == 0.064)
        check("before the change the rest clicked at 6.2", round(part_b.clicks[False] / part_b.impressions[False], 3) == 0.062)
        check("the two rates rebuild the blend", abs((ctr * weight).sum() - after.clicks.sum() / after.impressions.sum()) < 1e-12)
        """),
        md(f"""\
        **What happened.** The answer is c. After the change milk filled half the slot
        impressions and clicked at {s('milk_slot_ctr_after')}; everything else clicked at
        {s('other_slot_ctr_after')}, a little above the {s('other_slot_ctr_before')} it drew before.
        Half of 1.2 plus half of 6.4 is 3.8. **The plausible wrong answer** is "shoppers changed
        after the monsoon", which would have the team wait or redesign the strip. **The check** is
        the split by suggested item: the fall sits in the milk slots. **The fix** is to rank by
        lift above a support floor, which chapter 10 builds.
        """),
        code("""\
        # A second route to lift: confidence over the partner's base rate, read in both directions.
        for a, b in [("bread", "toned milk"), ("chips", "cold drink"), ("coriander", "green chillies")]:
            row = table[(table.a == a) & (table.b == b)].iloc[0]
            one = row.conf_a_to_b / (single[b] / n)
            other = row.conf_b_to_a / (single[a] / n)
            print(f"{a} + {b}: {row.lift:.4f} = {one:.4f} = {other:.4f}")
            check(f"{a} and {b}: three routes agree", abs(row.lift - one) < 1e-9 and abs(row.lift - other) < 1e-9)
        """),
        md(f"""\
        ## What did 40,000 carts answer?

        - **How often is each item in a cart?** Milk {s('toned_milk_share')}, bread
          {s('bread_share')}, eggs {s('eggs_share')}.
        - **Which pairs sit together most often?** Pairs with milk, led by bread and milk in
          {s('bread_milk_carts')} carts, which is why a strip ranked by count fills with milk.
        - **What does lift say about milk?** Near one with every common item: bread
          {s('bread_milk_lift')}, eggs {s('eggs_milk_lift')}. Chips and cold drink read
          {s('chips_cold_lift')}.
        - **Why did the click-through fall?** Milk took half the slot impressions at
          {s('milk_slot_ctr_after')}; the rest clicked at {s('other_slot_ctr_after')}.

        **In the interview.** "Support, confidence, lift: which one cannot be fooled by
        popularity?" Lift, because it divides by the partner's base rate, how common it is anyway; confidence toward milk
        sits near milk's own {s('toned_milk_share')} for every item.
        """),
    ]
    build(path, cells, timeout=300)
    print("wrote", path.relative_to(REPO))


# ================================================================================= notebook 09
def nb09():
    path = OUT / "C2_W04_D03_09_cross_sell_expected_value_STUDENT.ipynb"
    cells = [
        md(f"""\
        # Cross-sell and upsell reasoning; expected value in rupees: what is a combo worth?

        **Week 4, Wednesday, chapter 9, the last chapter of the concept block.** The topic, in the
        curriculum's words: *Cross-sell and upsell reasoning; expected value in rupees*. Sharma
        Kirana, a corner shop in Pune, is invented for this chapter: every number below is read
        from its month in `data/`, and the code only confirms the arithmetic.

        **Who needs the answer.** The owner of Sharma Kirana, who is weighing a counter card that
        reads "Tea and rusk together, Rs 1 off". Rusk beside tea is **cross-sell**, a second item
        that goes with the first; the bigger tea pack in place of the small one would be
        **upsell**, a dearer version of the same item.

        **The questions on the way.** Cross-sell or upsell? Which bills can the card change? What
        is it worth in a month? What decides the sign?
        """),
        code(CHECK + PLOT + textwrap.dedent("""\
        import pandas as pd

        kirana = pd.read_csv("../data/C2_W04_D03_kirana_month_STUDENT.csv")
        k = kirana.set_index("line").value
        print("Sharma Kirana's month, invented:")
        for line, value, what in kirana.itertuples(index=False):
            print(f"  {line}: {value:g}  ({what})")
        n, tea, rusk, both = (int(k[x]) for x in ["bills", "bills_with_tea", "bills_with_rusk", "bills_with_both"])
        lift = both / (n * (tea / n) * (rusk / n))
        print(f"tea and rusk: support {both / n:.2f}, lift {lift:.2f}, chapter 3's count")
        check("tea and rusk meet a little more often than chance: lift 1.25, under the 1.5 bar", round(lift, 2) == 1.25)
        """)),
        md("""\
        ## What is the tea-and-rusk card worth in a month?

        Tea and rusk meet a little more often than chance on plenty of bills, lift 1.25, under
        chapter 6's 1.5 bar: a weak pull that would earn no slot of its own. A card is the shop's
        cheapest bet on it, and the question is what that bet is worth. The card gives Rs 1 back
        on every bill holding both, and the owner assumes 4 percent of the tea bills without rusk
        will add a pack, somewhere between 2 and 6 percent; the card is assumed to change no
        other bill.

        **Predict before you run.** Which number should the owner weigh against the card?

        a) Rs 5,040, the rusk sold on every bill that will hold both.
        b) Rs 2,016, the rusk margin on every bill that will hold both.
        c) Rs 196, the margin on the new packs less the printing.
        d) Rs 28, the margin on the new packs less every rupee the card costs.
        """),
        code("""\
        price, cost, off, printing = k["rusk_price_rs"], k["rusk_cost_rs"], k["combo_discount_rs"], k["card_printing_rs"]
        margin = price - cost                        # what the shop keeps from a pack
        tea_only = tea - both                        # the only bills the card can change
        new = round(tea_only * k["response_mid"])    # packs added at the assumed 4 percent
        combos = both + new                          # every bill that will hold both, old and new
        value = new * margin - combos * off - printing
        print(f"tea bills without rusk: {tea_only}; new packs at 4 percent: {new}; margin a pack: Rs {margin:g}")
        print(f"Rs {new * margin:g} of new margin, less Rs {combos * off:g} on {combos} combo bills, "
              f"less Rs {printing:g} of printing: Rs {value:g} a month")
        check("the card is worth Rs 28 a month", value == 28)
        check("the discount is paid on 168 bills, the 18 new ones among them", combos == 168 and new == 18)
        """),
        md(f"""\
        **What happened.** The answer is d. The card is assumed to change only the
        {s('toy_kirana_tea_only')} tea bills without rusk, and {s('toy_kirana_packs')} of them add a pack worth
        {s('toy_kirana_margin')} of margin: {s('toy_kirana_incremental_margin')}. The card hands
        {s('toy_kirana_discount')} back on all {s('toy_kirana_combos')} bills that hold both, the
        {s('toy_kirana_both_bills')} that held both anyway among them, and the cards cost
        {s('toy_kirana_printing')}, which leaves {s('toy_kirana_ev')}. **The trap, exactly:**
        {s('toy_kirana_sales_wrong')}, rusk sales on every combo bill, which prints a card as if it
        earned {s('toy_kirana_sales_multiple')} what it does. **The check** is "which bills does
        the card change?"; **the fix** is margin on those bills only, less what the card gives
        away. The bridge below builds the number one bar at a time.
        """),
        code("""\
        wrong = {"rusk sales on every combo bill": combos * price,
                 "rusk margin on every combo bill": combos * margin,
                 "the discount forgotten": new * margin - printing}
        for name, x in wrong.items():
            print(f"{name}: Rs {x:,.0f}")
        print(f"the sales figure is {combos * price / value:.0f} times the gain")
        steps = [("new packs\\nx margin", new * margin), ("Rs 1 back on\\ncombo bills", -combos * off),
                 ("printing", -printing)]
        fig, ax = plt.subplots(figsize=(8, 3.8))
        run = 0
        for i, (label, x) in enumerate(steps):
            ax.bar(i, abs(x), bottom=run if x > 0 else run + x, color="#1F8A5B" if x > 0 else "#D63A6A", edgecolor="#1A0F5C")
            run += x
        ax.bar(len(steps), run, color="#5B3FD6", edgecolor="#1A0F5C")
        ax.set_xticks(range(len(steps) + 1), [s for s, _ in steps] + ["expected\\nvalue"])
        ax.set_ylabel("Rs a month")
        ax.set_title("The card, one bar at a time: Rs 28 a month")
        plt.show()
        check("rusk sales overstate the gain 180 times", combos * price / value == 180)
        """),
        md(f"""\
        ## How does expected value weigh each bill?

        The rule, named last: **expected value** is each outcome times its probability, added up,
        a weighted average (Wikipedia's expected value page, checked 13 October 2026). One tea bill
        without rusk earns {s('toy_kirana_net_new_pack')}, a pack's margin less the rupee its bill
        takes back, with probability {s('toy_kirana_response')}, and nothing on the other
        {s('toy_kirana_no_response')}: {s('toy_kirana_per_bill')} a bill. A second route checks it
        without probabilities: the shop's rusk margin with the card against the same month
        without it.
        """),
        code("""\
        p = k["response_mid"]
        per_bill = p * (margin - off)                     # one tea-only bill; the other 0.96 earn nothing
        route_two = tea_only * per_bill - both * off - printing
        before = rusk * margin
        after = (rusk + new) * margin - combos * off - printing
        print(f"one tea-only bill: {p:.2f} x Rs {margin - off:g}, and nothing on the other {1 - p:.2f}: Rs {per_bill:.2f}")
        print(f"{tea_only} bills: Rs {tea_only * per_bill:.0f}; less Rs {both * off:g} on the bills that held both "
              f"and Rs {printing:g} of printing: Rs {route_two:.0f}")
        print(f"with and without: Rs {after:,.0f} of rusk margin with the card, Rs {before:,.0f} without: Rs {after - before:,.0f}")
        fig, ax = plt.subplots(figsize=(9, 2.8))
        parts = [(both, "#D63A6A", "held both anyway: Rs 1 back each"),
                 (new, "#1F8A5B", "add a pack: Rs 11 each"),
                 (tea_only - new, "#E4E1F1", "unchanged: nothing")]
        left = 0
        for width, colour, label in parts:
            ax.barh(0, width, left=left, color=colour, edgecolor="#1A0F5C", label=label)
            left += width
        ax.set_yticks([])
        ax.set_xlabel("the month's tea bills")
        ax.legend(frameon=False, ncol=3, loc="upper center", bbox_to_anchor=(0.5, -0.45))
        ax.set_title("Which tea bills does the card change?")
        plt.show()
        check("the weighted average and the with-and-without route give Rs 28",
              round(route_two) == value == after - before)
        """),
        md(f"""\
        ## What decides the sign?

        Two numbers the owner sets or guesses move the answer. Every extra rupee off costs
        {s('toy_kirana_discount_back')} a month, since it is paid on every combo bill, so at the
        same 4 percent response the card earns nothing at about {s('toy_kirana_breakeven')} off; a
        bigger discount may draw more buyers, which only a trial of the card would show. And the 4 percent is an assumption:
        at {s('toy_kirana_response_low')} the card loses money, at {s('toy_kirana_response_high')}
        it earns more. An assumed response is said with its range, and the answer travels with it.
        """),
        code("""\
        def card_value(response, off):
            new = round(tea_only * response)
            return new * margin - (both + new) * off - printing


        def rs(x):
            return f"{'-' if x < 0 else ''}Rs {abs(x):,.0f}"


        for response, off_ in [(0.04, 1), (0.04, 2), (0.02, 1), (0.06, 1)]:
            print(f"response {response:.0%}, Rs {off_} off: {rs(card_value(response, off_))}")
        breakeven = (new * margin - printing) / combos
        print(f"at a 4 percent response the card earns nothing at Rs {breakeven:.2f} off")
        offs = [x / 10 for x in range(0, 31)]
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 3.6))
        a1.plot(offs, [card_value(0.04, o) for o in offs], color="#5B3FD6", lw=3)
        a1.axhline(0, color="#1A0F5C")
        a1.set_xlabel("Rs off a combo bill, 4 percent responding")
        a1.set_ylabel("Rs a month")
        a1.set_title("Zero is crossed just past Rs 1")
        rates = [0.02, 0.04, 0.06]
        vals = [card_value(r, 1) for r in rates]
        a2.bar([f"{r:.0%}" for r in rates], vals, color=["#D63A6A" if x < 0 else "#1F8A5B" for x in vals], edgecolor="#1A0F5C")
        a2.axhline(0, color="#1A0F5C")
        a2.set_xlabel("share of tea-only bills adding rusk")
        a2.set_title("The response decides the sign")
        plt.show()
        check("Rs 2 off loses Rs 140", card_value(0.04, 2) == -140)
        check("the sign turns on the response: 2 percent loses, 6 percent earns", card_value(0.02, 1) < 0 < card_value(0.06, 1))
        """),
        md("""\
        ### Your turn: what is a bigger shop's card worth?

        A card reaches 2,000 bills, 5 percent of them add one extra pack at Rs 10 of margin, and
        the cards cost Rs 600. Nothing is handed back on any bill. In the empty cell below,
        compute the card's value for the month and store it as `big_card`. Then run the check
        under it.
        """),
        empty(),
        code("""\
        mine = globals().get("big_card")
        if mine is None:
            print("Store your answer as big_card in the empty cell above, then run this cell again.")
        else:
            reference = round(2000 * 0.05) * 10 - 600
            print(f"reference: Rs {reference:,}; yours: Rs {mine:,.0f}")
            print("matches" if abs(mine - reference) < 0.5 else "not yet: new packs x margin, less the cost")
        """),
        md(f"""\
        ## What should you keep from chapter 9?

        - Cross-sell suggests a second item that goes with the first; upsell suggests a dearer
          version of the same item, and it is priced the same way: the extra margin of the bigger
          pack on the shoppers who switch, less what the switch gives away.
        - A card earns only on the bills it changes, so its gain is margin on the new packs, never
          sales on every combo bill: {s('toy_kirana_ev')}, against {s('toy_kirana_sales_wrong')}.
        - A discount is paid on every bill that takes it, including the bills that would have held
          both anyway.
        - Expected value weighs each outcome by its probability, so an assumed response comes with
          its range, and so does the answer: {s('toy_kirana_ev_low')} at
          {s('toy_kirana_response_low')} and {s('toy_kirana_ev_high')} at
          {s('toy_kirana_response_high')}.

        **In the interview.** "A combo offer lifts the pair's sales; is it worth running?" Margin
        on the purchases the offer creates, less the discount paid on every purchase that takes
        it, including those that would have happened anyway, less the fixed cost, said as a
        range. Chapter 10 prices one of Instamart's strip slots the same
        way, and the lab prices Kalpa's charger bundle.
        """),
    ]
    build(path, cells)
    print("wrote", path.relative_to(REPO))


# ================================================================================= notebook 10
def nb10():
    path = OUT / "C2_W04_D03_10_case_floor_watchlist_expected_value_STUDENT.ipynb"
    cells = [
        md(f"""\
        # The strip ranked by the support floor and priced by expected value in rupees: what is a slot worth?

        **Week 4, Wednesday, chapter 10, the third case chapter.** Swiggy Instamart, Pune: the
        strip's click-through fell from {s('before_strip_ctr')} to {s('after_strip_ctr')} after it
        began ranking suggestions by how often items share a cart. {LABEL} Chapter 8 found why:
        milk took half the slot impressions and clicked at {s('milk_slot_ctr_after')} against
        {s('other_slot_ctr_after')} for everything else, and lift with milk sits near one for every
        common item. This notebook picks what replaces milk and prices the change.

        **Applies:** The support floor and the watch list (chapter 6, notebook 06); Cross-sell and
        upsell reasoning; expected value in rupees (chapter 9, notebook 09).

        **Who needs the answer.** The growth lead, who takes a ranked list and a rupee figure to
        Friday's review, and the category manager, who will argue for milk.

        **The questions on the way.** Which pairs beat chance by enough, on enough carts? What
        should the watch list do with a strong pair on few carts? What is a slot worth in rupees?
        What can the counts not tell us?
        """),
        code(CHECK + PLOT + textwrap.dedent("""\
        import pandas as pd
        from collections import Counter
        from itertools import combinations

        carts = pd.read_csv("../data/C2_W04_D03_carts_STUDENT.csv", parse_dates=["placed_date"])
        items = pd.read_csv("../data/C2_W04_D03_cart_items_STUDENT.csv")
        log = pd.read_csv("../data/C2_W04_D03_strip_log_STUDENT.csv", parse_dates=["date"])
        n = len(carts)
        baskets = items.groupby("cart_id").item.apply(set)
        single = Counter(x for b in baskets for x in b)
        pairs = pd.DataFrame([{"a": a, "b": b, "both": k, "support": k / n,
                               "lift": k * n / (single[a] * single[b])}
                              for (a, b), k in Counter(p for b in baskets
                                                       for p in combinations(sorted(b), 2)).items()])
        print(f"{len(pairs):,} pairs found in at least one cart")
        check("the pairs table holds every pair once", not pairs.duplicated(["a", "b"]).any())
        """)),
        md(f"""\
        ## Which pairs beat chance by enough, on enough carts?

        A team has four ways to rank what the strip suggests, and each puts a different pair on
        top: by count (bread and milk, {s('bread_milk_carts')} carts, lift
        {s('bread_milk_lift')}); by confidence (milk again, toward which every item reads about
        0.7); by lift alone (ice cream and chocolate sauce, lift {s('ice_choc_lift')} on
        {s('ice_choc_carts')} carts); or by lift above a **support floor**, the fewest carts a pair
        must sit in before it may take a slot. A floor of {s('support_floor')} of carts is
        {s('support_floor_carts')} carts.

        **Predict before you run.** Under a floor of 1 percent of carts and a bar of lift 1.5,
        which pair ranks first?

        a) bread and milk: support 25.2 percent, lift 1.04
        b) chips and cold drink: support 5.0 percent, lift 3.39
        c) ice cream and chocolate sauce: support 0.25 percent, lift 4.60
        d) onions and tomatoes: support 7.5 percent, lift 1.70
        """),
        code("""\
        floor = 0.01
        ranked = pairs[pairs.support >= floor].sort_values("lift", ascending=False)
        print(f"{len(ranked)} pairs at or above the floor; the top five by lift:")
        print(ranked.head(5).round(4).to_string(index=False))
        check("chips and cold drink top the ranking", tuple(ranked.iloc[0][["a", "b"]]) == ("chips", "cold drink"))
        check("four pairs above the floor reach lift 1.5", (ranked.lift >= 1.5).sum() == 4)
        """),
        md(f"""\
        **What happened.** The answer is b. Above the floor, four pairs beat chance by a clear
        gap, lift 1.5 or more: chips and cold drink {s('chips_cold_lift')}, coriander and green chillies
        {s('coriander_chillies_lift')}, bread and butter {s('bread_butter_lift')}, onions and
        tomatoes {s('onions_tomatoes_lift')}. The next pair reads {s('fifth_pair_lift')}, near one.
        A slot sits beside an item already in the cart, so a pair fills a slot only beside its own
        item, cold drink beside chips and butter beside bread; beside an item with no partner over
        the bar, the strip falls back to the curated list it ran before 7 September. No partner of
        milk can reach the bar: milk is in 71 percent of carts, so its lift cannot pass one over
        that share, {s('milk_lift_ceiling')}. The picture places every pair.
        """),
        code("""\
        shown = pairs[pairs.support >= 0.001]
        fig, ax = plt.subplots(figsize=(9, 4.8))
        ax.scatter(shown.support, shown.lift, s=10, alpha=0.4, color="#5B3FD6")
        ax.axvline(floor, color="#6B6690", ls="--"); ax.axhline(1, color="#6B6690", ls="--")
        ax.axhline(1.5, color="#1F8A5B", ls=":")
        top_thin = pairs[(pairs.support >= 0.002) & (pairs.support < floor)].sort_values("lift").iloc[-1]
        for _, r in list(ranked.head(4).iterrows()) + [(None, top_thin)]:
            ax.annotate(f"{r.a} + {r.b}", (r.support, r.lift), xytext=(5, 5), textcoords="offset points")
        ax.set_xscale("log"); ax.set_ylabel("lift")
        ax.set_xticks([0.001, 0.01, 0.1], ["0.1%", "1%", "10%"])
        ax.set_xlabel("support: share of carts holding both (each step right is ten times more carts)")
        ax.set_title("Promote above the floor and well above one; watch the strong thin pairs")
        plt.show()
        """),
        md(f"""\
        ## What should the watch list do with a strong pair on few carts?

        Ice cream and chocolate sauce read lift {s('ice_choc_lift')}, the strongest pair below the
        1 percent floor with enough carts to trial: the search runs between {s('watch_band_low')}
        ({s('watch_band_low_carts')} carts) and the floor, since thousands of pairs on a handful of
        carts read wild lifts by luck, as chapter 6's month showed. The pair is real, {s('ice_choc_carts')} carts where chance gives
        {s('ice_choc_expected')}, but the strip suggests it only beside ice cream, which is in
        {s('ice_cream_share')} of carts: about {s('ice_cream_views_day')} of the strip's
        {s('views_assumed')} cart-page views a day, if views follow carts, and
        {s('ice_choc_carts')} carts cannot say how shoppers will click it there (the next section
        prices it). It goes on a **watch list**: in two zones a random half of shoppers see it
        beside ice cream, and it takes the slot only if their ice-cream carts buy sauce more often
        than the other half's, by a gap set before the trial, with margin per shopper as the
        guardrail, a number that must not fall while the trial runs.
        """),
        code("""\
        thin = pairs[(pairs.support >= 0.002) & (pairs.support < floor)].sort_values("lift", ascending=False)
        print(thin.head(4).round(4).to_string(index=False))
        check("ice cream and chocolate sauce lead the thin band", tuple(thin.iloc[0][["a", "b"]]) == ("chocolate sauce", "ice cream"))
        """),
        md(f"""\
        ## What is one slot worth in rupees?

        Chapter 9 priced Sharma Kirana's card as margin on the purchases it changes, less what it
        hands back; a slot is priced the same way. **Margin** is what Instamart keeps from a sale
        after the item's cost: bread sells for {s('bread_price')} and keeps {s('bread_margin')}. A slot's margin a day is the cart-page
        views times its click-through times the share of clicks that become an add, times the
        margin on an added item. Views are {s('views_assumed')} a day (the mean in `strip_log`
        since the change), each showing all three slots, so {s('impressions_a_day')} impressions
        a day across the strip. The promoted pairs are assumed to click at the
        {s('other_slot_ctr_after')} every suggestion other than milk drew. The add rate
        {s('add_rate_assumed')} is an assumption with a range of {s('add_rate_low')} to
        {s('add_rate_high')} (`strip_log` reads 0.50), and the margin {s('margin_assumed')} an
        assumption with a range of {s('margin_low')} to {s('margin_high')} (a `cart_items` line
        earns {s('margin_per_line_observed')} on average, milk aside). A click is worth
        {s('value_per_click_mid')} at the middle, {s('value_per_click_low')} at the low ends
        (0.4 x Rs 7) and {s('value_per_click_high')} at the high ends (0.6 x Rs 11).

        **Predict before you run.** What does taking milk out recover in a month, its half of the
        impressions given to suggestions that click at {s('other_slot_ctr_after')}?

        a) about Rs 50,000
        b) about Rs 2 lakh
        c) about Rs 6 lakh
        d) about Rs 50 lakh
        """),
        code("""\
        views, add_rate, margin = 60_000, 0.5, 9
        good = views * 0.064 * add_rate * margin     # a slot a day, showing any suggestion but milk
        milk = views * 0.012 * add_rate * margin     # the same slot showing milk
        gap_month = (good - milk) * 30
        recovered = gap_month * 3 * 0.5            # three slots, milk on half the impressions
        low = views * (0.064 - 0.012) * 0.4 * 7 * 30 * 1.5
        high = views * (0.064 - 0.012) * 0.6 * 11 * 30 * 1.5
        print(f"a slot a day: Rs {good:,.0f} with any suggestion but milk, Rs {milk:,.0f} with milk")
        print(f"gap: Rs {good - milk:,.0f} a day, Rs {gap_month / 1e5:.1f} lakh a month per slot")
        print(f"recovered on milk's 1.5 slots' worth: Rs {recovered / 1e5:.1f} lakh a month "
              f"(Rs {low / 1e5:.1f} lakh to Rs {high / 1e5:.1f} lakh across the ranges)")
        fig, ax = plt.subplots(figsize=(7, 3.2))
        ax.bar(["any suggestion but milk", "milk"], [good, milk], color=["#1F8A5B", "#D63A6A"])
        ax.set_ylabel("Rs a day, one slot"); ax.set_title("One slot, one day")
        plt.show()
        check("a slot earns Rs 17,280 or Rs 3,240 a day", round(good) == 17_280 and round(milk) == 3_240)
        check("taking milk out recovers Rs 6.3 lakh a month", round(recovered / 1e5, 1) == 6.3)
        """),
        md(f"""\
        **What happened.** The answer is c: {s('recoverable_month')} a month, between
        {s('recoverable_low')} and {s('recoverable_high')} across the two ranges, before the adds
        that would have come anyway. Every add is priced at the basket's average Rs 9, milk's too.
        Two corrections pull opposite ways: milk earns only {s('milk_margin')} a pouch, which
        raises the gain, and the strip's own adds earned {s('strip_margin_per_add')}, which lowers
        it; with both, {s('recoverable_month_own_margins')}, inside the range. Where does the money
        come from? The cell below splits the strip's clicks by slot and by suggestion.
        """),
        code("""\
        after = log[log.date >= "2026-09-07"]
        other = after[after.suggested_item != "toned milk"]
        lift_of = {(a, b): l for a, b, l in zip(pairs.a, pairs.b, pairs.lift)}
        by_cell = other.groupby(["slot", "anchor_item", "suggested_item"])[["impressions", "clicks"]].sum()
        by_cell["ctr"] = by_cell.clicks / by_cell.impressions
        by_cell["lift"] = [lift_of[tuple(sorted((a, s)))] for _, a, s in by_cell.index]
        for slot, part in by_cell.groupby(level="slot"):
            print(f"slot {slot}: every suggestion other than milk clicked at {part.ctr.min():.1%} to {part.ctr.max():.1%}")
        cc, eb = by_cell.loc[(1, "chips", "cold drink")], by_cell.loc[(1, "eggs", "bread")]
        print(f"slot 1: cold drink beside chips, lift {cc.lift:.2f}, {cc.ctr:.1%}; bread beside eggs, lift {eb.lift:.2f}, {eb.ctr:.1%}")
        fig, ax = plt.subplots(figsize=(8, 3.6))
        for slot, colour in [(1, "#1A0F5C"), (2, "#5B3FD6"), (3, "#B8B2D6")]:
            part = by_cell.loc[slot]
            ax.scatter(part.lift, part.ctr * 100, s=70, color=colour, edgecolor="#1A0F5C", label=f"slot {slot}")
        ax.set_xlabel("the pair's lift")
        ax.set_ylabel("click-through, percent")
        ax.set_ylim(0, 10)
        ax.legend(frameon=False, ncol=3, loc="lower right")
        ax.set_title("Inside a slot, a suggestion's lift does not move its clicks")
        plt.show()
        check("inside each slot, suggestions other than milk click within half a point of each other",
              all(p.ctr.max() - p.ctr.min() < 0.005 for _, p in by_cell.groupby(level="slot")))
        """),
        md(f"""\
        **What the split shows.** Inside each slot, every suggestion other than milk clicked alike,
        whatever its lift: in slot 1, cold drink beside chips (lift {s('chips_cold_lift')}) drew
        {s('chips_cold_slot1_ctr')} and bread beside eggs (lift {s('bread_eggs_lift')})
        {s('eggs_bread_slot1_ctr')}. So the money comes from taking milk out, which ranking by
        lift above the 1.5 bar does by arithmetic. Whether a lift-ranked pair clicks better than
        any other suggestion is not in this log: a test with a count-ranked arm, milk left out,
        against a lift-ranked arm measures it. The watch-list pair, priced at its own margins
        ({s('sauce_margin')} for sauce against {s('milk_margin')} for milk) on about
        {s('ice_cream_views_day')} views a day in place of milk, earns 2,400 x 30 x (0.064 x 0.5 x
        Rs 37.40 less 0.012 x 0.5 x Rs 2), {s('thin_rule_month')} a month, which is why it earns a
        test and never a blind slot. **The plausible wrong answer** books sales as the benefit:
        1,920 adds a day at Rs {v('price_per_add_observed'):.2f} on average reads as
        {s('gross_sales_day_about')} a day of "strip revenue", over four and a half times the
        margin. **Why it is wrong.** The growth lead counts the margin, never the price; and if the strip
        ever adds a bundle discount, that discount is margin handed back to the customer. Swiggy's
        shareholder letter for April to June 2025 describes Maxxsaver, a discount unlocked once a
        basket passes a set size, in just those terms (checked 12 October 2026).
        """),
        code("""\
        price = items.drop_duplicates("item").set_index("item").price_rs
        price_per_add = (other.groupby("suggested_item").adds.sum() * price).sum() / other.adds.sum()
        adds = views * 0.064 * add_rate
        print(f"{adds:,.0f} adds a day x Rs {price_per_add:.2f} = about Rs {round(adds * price_per_add, -2):,.0f} of sales; "
              f"the margin is Rs {good:,.0f}")
        check("sales overstate the margin more than four times", adds * price_per_add > 4 * good)
        """),
        md(f"""\
        ## What can the counts not tell us?

        Six doubts, each with the check that settles it. **Together is no proof of cause.** Lift
        says chips and cold drink are bought together; it does not show that suggesting cold drink
        beside chips makes anyone buy a cold drink they would not have bought. Only a **holdout**
        settles that, a random share of shoppers who see no strip, compared with the rest, the
        subject of this week's Monday faculty session on A/B testing (tentative). **Heavy buyers,
        each placing many carts:** the top tenth of customers place 38 percent of carts, so lift is
        recomputed with every customer counted once, which gives each cart a weight of one over its
        customer's number of carts (a shopper with {s('weight_example_carts')} carts counts each as
        {s('weight_example')}); the next cell. **The stock-out:** curd ran out in two zones in week
        three; the cell after. **Time of day:** morning carts hold milk more often; the same cell.
        **Position in the strip:** whatever slot 1 shows draws the most clicks, as D54's picture
        and the slot split above show. **The strip feeds its own counts:** an add from the strip puts both items in
        one cart, and only the holdout's shoppers, who never see the strip, show the counts without
        it.

        **Predict before you run.** With every customer counted once, where does chips and cold
        drink's lift of {s('chips_cold_lift')} land?

        a) above {s('chips_cold_lift')}, since heavy buyers are loyal to the pair
        b) unchanged, since a weight cannot move a ratio
        c) about 2.5: lower, still well above one
        d) about 1, since the pair was only heavy buyers all along
        """),
        code("""\
        carts["weight"] = 1 / carts.groupby("customer_id").cart_id.transform("count")
        w = carts.set_index("cart_id").weight
        top_tenth = carts.customer_id.value_counts().head(len(carts.customer_id.unique()) // 10)
        print(f"top tenth of customers: {top_tenth.sum() / n:.0%} of carts")
        both_ids = baskets[baskets.apply(lambda x: "chips" in x and "cold drink" in x)].index
        heavy_share = carts.set_index("cart_id").loc[both_ids, "customer_id"].isin(top_tenth.index).mean()
        print(f"...and {heavy_share:.0%} of the carts holding both chips and a cold drink")
        per_cart = pairs.set_index(["a", "b"]).lift
        rows = {}
        for a, b, name in [("chips", "cold drink", "chips + cold drink"), ("bread", "toned milk", "bread + milk")]:
            has_a = baskets.apply(lambda x: a in x); has_b = baskets.apply(lambda x: b in x)
            pa, pb = w[has_a].sum() / w.sum(), w[has_b].sum() / w.sum()
            rows[name] = (per_cart[(a, b)], w[has_a & has_b].sum() / w.sum() / (pa * pb))
        for name, (every_cart, each_once) in rows.items():
            print(f"{name}: lift {every_cart:.2f} per cart, {each_once:.2f} with each customer counted once")
        fig, ax = plt.subplots(figsize=(7, 2.8))
        ax.barh(list(rows), [r[1] for r in rows.values()], color="#D9A7FF", label="each customer once")
        ax.scatter([r[0] for r in rows.values()], list(rows), color="#1A0F5C", zorder=3, label="every cart")
        ax.axvline(1, color="#6B6690", ls="--"); ax.legend(frameon=False); ax.set_xlabel("lift")
        plt.show()
        check("the top tenth place 38 percent of carts", round(top_tenth.sum() / n, 2) == 0.38)
        check("they place 73 percent of the chips and cold drink carts", round(heavy_share, 2) == 0.73)
        check("counted per customer, the party pair shrinks and milk's pair holds",
              rows["chips + cold drink"][1] < 2.7 and abs(rows["bread + milk"][1] - 1.04) < 0.01)
        """),
        code("""\
        carts["curd"] = carts.cart_id.isin(items.loc[items.item == "curd", "cart_id"])
        carts["week"] = (carts.placed_date.dt.day - 1) // 7 + 1
        grid = carts.pivot_table(index="zone", columns="week", values="curd", aggfunc="mean")
        print((grid * 100).round().astype(int).to_string())
        hit = carts.zone.isin(["Hadapsar", "Viman Nagar"]) & (carts.week == 3)
        kept = baskets[carts.loc[~hit, "cart_id"]]
        print(f"curd's share: {carts.curd.mean():.1%} of all carts, {carts.loc[~hit, 'curd'].mean():.1%} "
              f"with the two zone-weeks set aside")
        curd_lift = []
        for bs in (baskets, kept):
            has_curd = bs.apply(lambda x: "curd" in x); has_milk = bs.apply(lambda x: "toned milk" in x)
            curd_lift.append((has_curd & has_milk).sum() * len(bs) / (has_curd.sum() * has_milk.sum()))
        print(f"curd and milk lift: {curd_lift[0]:.2f} and {curd_lift[1]:.2f}")
        check("curd is near zero in the two zones in week three", carts.loc[hit, "curd"].mean() < 0.01)
        by_band = carts.assign(milk=carts.cart_id.isin(items.loc[items.item == "toned milk", "cart_id"])) \\
            .groupby("time_band").milk.mean().sort_values(ascending=False)
        print("share of carts holding milk, by time band:", by_band.round(2).to_dict())
        for band in by_band.index:
            bs = baskets[carts.loc[carts.time_band == band, "cart_id"]]
            has_bread = bs.apply(lambda x: "bread" in x); has_milk = bs.apply(lambda x: "toned milk" in x)
            print(f"  {band}: bread and milk lift "
                  f"{(has_bread & has_milk).sum() * len(bs) / (has_bread.sum() * has_milk.sum()):.2f}")
        check("morning carts hold milk most often", by_band.index[0] == "morning")
        """),
        md(f"""\
        **What happened.** The answer is c: counted once per customer, chips and cold drink fall
        from {s('chips_cold_lift')} to {s('chips_cold_lift_per_customer')} and still beat chance,
        while bread and milk stay at {s('bread_milk_lift_per_customer')}. The plausible wrong number
        is {s('chips_cold_lift')} quoted to finance, which shrinks the first time someone recounts
        it; the growth lead quotes the smaller one. Curd's lift with milk holds at
        {s('curd_milk_lift_kept')} with the stock-out set aside.

        ## Does a second route reach the same Rs {s('recoverable_month')[3:]}?

        Read the milk impressions straight from `strip_log` rather than from "half the slots":
        every milk impression given to any suggestion other than milk gains the gap in
        click-through times the add rate times the margin.
        """),
        code("""\
        milk_per_day = after[after.suggested_item == "toned milk"].groupby("date").impressions.sum().mean()
        route_two = milk_per_day * (0.064 - 0.012) * add_rate * margin * 30
        print(f"{milk_per_day:,.0f} milk impressions a day -> Rs {route_two / 1e5:.1f} lakh a month")
        check("both routes give Rs 6.3 lakh", round(route_two / 1e5, 1) == round(recovered / 1e5, 1))
        """),
        md(f"""\
        ## What does the growth lead take to Friday?

        - **Which pairs?** Above a floor of {s('support_floor')} of carts and the 1.5 bar, each
          beside its own item: chips and cold drink {s('chips_cold_lift')}, coriander and green
          chillies {s('coriander_chillies_lift')}, bread and butter {s('bread_butter_lift')},
          onions and tomatoes {s('onions_tomatoes_lift')}; the curated list elsewhere. No partner
          of milk can pass {s('milk_lift_ceiling')}.
        - **The watch list?** Ice cream and chocolate sauce, lift {s('ice_choc_lift')} on
          {s('ice_choc_carts')} carts, tested before it is promoted.
        - **A slot in rupees?** {s('slot_value_other_day')} a day with any suggestion but milk,
          {s('slot_value_milk_day')} with milk, every add at Rs 9; taking milk out recovers
          {s('recoverable_month')} a month before the adds that would have come anyway, and a test
          shows whether lift beats a count ranking without milk.
        - **What the counts cannot say?** Whether the pair causes the purchase; counted per
          customer, chips and cold drink fall to {s('chips_cold_lift_per_customer')} and still beat
          chance; the curd stock-out lowers curd's count and leaves its lift at
          {s('curd_milk_lift_all')}; morning carts hold milk {s('milk_share_morning')} of the time
          and bread with milk reads {s('bread_milk_lift_morning')} to {s('bread_milk_lift_evening')} in every band.

        **In the interview.** "Turn a basket analysis into a recommendation with a number." Name
        the pairs above a floor, the incremental adds (the adds that would not have happened
        without the strip) times the margin, the cost line (what a promotion gives back, such as a
        discount), and the assumption that would change the call.
        """),
    ]
    build(path, cells, timeout=600)
    print("wrote", path.relative_to(REPO))


# ================================================================================= notebook 11
def nb11():
    path = OUT / "C2_W04_D03_11_kalpa_basket_analysis_order_items_STUDENT.ipynb"
    ids = v("kalpa_twelve_ids")
    cells = [
        md("""\
        # Does the pairs method hold up on Kalpa Retail's baskets?

        **Week 4, Wednesday, the TA-led lab, after chapter 10.** **Applies:** Basket analysis on
        the order items (chapter 5, notebook 05); The confidence trap; lift near one (chapter 4,
        notebook 04); The support floor and the watch list (chapter 6, notebook 06); Cross-sell and
        upsell reasoning; expected value in rupees (chapter 9, notebook 09).

        Kalpa Retail's merchandising team, which decides
        which products are bundled and promoted, wants to pair every product with the Rs 199 phone
        charger, "because it is in 80 percent of baskets", to give Retail-Plus members (Kalpa's
        paid membership tier) a reason to come back. The head of merchandising asks which pairs
        to promote and what each promotion is worth in rupees before any money is spent. The data
        are Kalpa's own: the warehouse's 1,000 orders from April to September 2026, now with their
        order lines (`order_items`: order, product, quantity, unit price) and the product list.

        **Who needs the answer.** The head of merchandising, whose bundle budget goes wherever the
        lab's numbers point.

        **The questions on the way.** What does a basket mean in Kalpa's data? What do twelve
        baskets say when counted by hand? How often is the charger in a basket, and what is its
        lift with each product? Which pair beats chance above a 5 percent floor, and which strong
        pair is too thin to promote?
        """),
        code(CHECK + PLOT + textwrap.dedent("""\
        import pandas as pd
        from collections import Counter
        from itertools import combinations

        orders = pd.read_csv("../data/C2_W04_D03_kalpa_orders_STUDENT.csv")
        lines = pd.read_csv("../data/C2_W04_D03_kalpa_order_items_STUDENT.csv")
        products = pd.read_csv("../data/C2_W04_D03_kalpa_products_STUDENT.csv")
        lines = lines.merge(products[["product_id", "name"]], on="product_id")
        line_total = (lines.quantity * lines.unit_price).groupby(lines.order_id).sum()
        check("every order's lines add up to its amount",
              (line_total.reindex(orders.order_id).values == orders.amount.values).all())
        consumer = orders[orders.segment != "Business"]
        print(f"{len(orders):,} orders: {len(consumer)} consumer baskets, "
              f"{(orders.segment == 'Business').sum()} Business orders of one product in bulk")
        """)),
        md("""\
        ## What does a basket mean here, and what do twelve baskets say?

        A basket is one consumer order with its lines; a Business order holds one product bought
        in bulk, so it is left out. The TA hands out twelve baskets on paper. Count by hand first:
        the charger's share, the screen protector's confidence toward the charger and its lift
        with the charger, and the lift of the pen set with the phone grip. The cell below prints
        those numbers to check your count.
        """),
        code("""\
        twelve_ids = "IDS".split(", ")
        twelve = lines[lines.order_id.isin(twelve_ids)].groupby("order_id").name.apply(set)
        for oid, held in twelve.items():
            print(oid, ", ".join(sorted(held)))
        charger = twelve.apply(lambda x: "phone charger 20W" in x)
        protector = twelve.apply(lambda x: "screen protector" in x)
        pens = twelve.apply(lambda x: "pen set" in x)
        grip = twelve.apply(lambda x: "phone grip" in x)
        conf_sp = (protector & charger).sum() / protector.sum()
        lift_sp = (protector & charger).sum() * 12 / (protector.sum() * charger.sum())
        lift_pg = (pens & grip).sum() * 12 / (pens.sum() * grip.sum())
        print(f"charger in {charger.mean():.2f} of the twelve; screen protector to charger: "
              f"confidence {conf_sp:.2f}, lift {lift_sp:.2f}; pen set with phone grip: lift {lift_pg:.2f}")
        count = Counter(x for held in twelve for x in held)
        fig, ax = plt.subplots(figsize=(8, 3.8))
        names = sorted(count, key=count.get)
        ax.barh(names, [count[x] for x in names], color="#FFF7E6", edgecolor="#C98A00")
        ax.set_xlabel("baskets, of the twelve"); ax.set_title("Twelve Kalpa baskets, counted")
        plt.show()
        check("twelve baskets", len(twelve) == 12)
        """.replace("IDS", ids)),
        md("""\
        ### Your turn: how often is the charger in a basket, and what is its lift with each product?

        Build `baskets = lines[lines.order_id.isin(consumer.order_id)].groupby("order_id").name.apply(set)`.
        Print the charger's share of baskets. Then, for every product in at least 2 percent of
        baskets, print its confidence toward the charger and its lift with the charger. Write one
        sentence for merchandising on what the numbers say about "it is in 80 percent of baskets".
        Checks you can run yourself: your baskets number 812, every share sits between 0 and 1,
        and a pair's lift reads the same from both sides.
        """),
        empty(),
        md(f"""\
        ### Your turn: which pair beats chance above a 5 percent floor, and which is too thin?

        Count every pair with `Counter` over `combinations(sorted(basket), 2)`, as notebook 05 did
        on the canteen and notebook 08 on Instamart's carts. With 812 baskets, a floor of 1 percent would be
        {s('kalpa_one_pct_baskets')} baskets, too thin to trust, so the lab sets its floor at
        5 percent, {s('kalpa_floor_baskets')} baskets: still thin, so a pair earns a promotion
        there only with a lift far above the 1.5 bar. Keep the pairs at or above it and rank them
        by lift; then look below the floor for a pair with a high lift on two or three baskets.
        For the strongest pair above the floor, find which segment its baskets come from:
        `orders.set_index("order_id").loc[ids, "segment"].value_counts()` counts the segments of a
        list of basket ids. Kalpa's consumer segments are Retail-Core, Retail-Plus and Student, and
        a pair whose baskets come mostly from one segment is a pair to promote to that segment.
        """),
        empty(),
        md("""\
        ## Can the data carry the answer?

        Before a number goes to merchandising, two checks that need no pair counts: how many lines
        a basket holds, and whether every amount reconciles to its lines. A basket of one line
        holds no pair, so the first picture says how many baskets the pairs table can use. An
        order lists at most eight products, and a bigger order buys more units of each, so the
        larger orders all sit at eight lines.
        """),
        code("""\
        per_basket = lines[lines.order_id.isin(consumer.order_id)].groupby("order_id").size()
        fig, ax = plt.subplots(figsize=(7, 3.2))
        ax.hist(per_basket, bins=range(1, 10), color="#EEEAFB", edgecolor="#5B3FD6", align="left")
        ax.set_xlabel("lines in a consumer basket"); ax.set_title("Baskets hold one to eight lines")
        plt.show()
        fig, ax = plt.subplots(figsize=(7, 3.6))
        ax.scatter(orders.amount, line_total.reindex(orders.order_id), s=8, color="#5B3FD6")
        ax.set_xscale("log"); ax.set_yscale("log")
        rupees = [1e3, 1e4, 1e5, 1e6, 1e7]
        names = ["Rs 1,000", "Rs 10,000", "Rs 1 lakh", "Rs 10 lakh", "Rs 1 crore"]
        ax.set_xticks(rupees, names); ax.set_yticks(rupees, names)
        ax.set_xlabel("order amount"); ax.set_ylabel("sum of its lines")
        ax.set_title("Every order sits on the line: amount = sum of lines")
        plt.show()
        check("consumer baskets hold one to eight lines", per_basket.between(1, 8).all())
        check("Business orders hold one line each",
              (lines[lines.order_id.isin(orders[orders.segment == "Business"].order_id)]
               .groupby("order_id").size() == 1).all())
        check("the charger lists at Rs 199", products.set_index("name").loc["phone charger 20W", "list_price"] == 199)
        """),
        md(f"""\
        ## What will merchandising's proposal cost, and what do you bring back?

        The unguided Kalpa exercise prices the charger proposal as chapter 9 priced the kirana's
        card. The charger lists at
        {s('kalpa_charger_list_price')} and costs Kalpa {s('kalpa_charger_cost')}, so the proposed
        {s('kalpa_bundle_discount')} off leaves {s('kalpa_margin_bundled')} of margin on every
        bundled charger, and every basket that already holds the charger hands that discount back
        for an add that would have happened anyway. Bring back three lines: the charger's share and
        its lift with the products it would be bundled with, the pair you would promote with its
        support and lift, and the pair you would watch, with the number of baskets it rests on.
        """),
    ]
    build(path, cells, timeout=300)
    print("wrote", path.relative_to(REPO))


OLD = ["C2_W04_D03_01_receipts_STUDENT.ipynb", "C2_W04_D03_02_pairs_table_STUDENT.ipynb",
       "C2_W04_D03_03_action_map_STUDENT.ipynb", "C2_W04_D03_04_kalpa_lab_STUDENT.ipynb"]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name in OLD:                       # the four notebooks of the case-first pack
        (OUT / name).unlink(missing_ok=True)
    for make in (nb01, nb02, nb03, nb04, nb05, nb06, nb07, nb08, nb09, nb10, nb11):
        make()


if __name__ == "__main__":
    main()
