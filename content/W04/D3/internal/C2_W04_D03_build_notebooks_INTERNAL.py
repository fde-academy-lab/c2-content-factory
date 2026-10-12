"""Assemble and execute the four Wednesday notebooks.

Run from the repository root, after the generator:
    python3 content/W04/D3/internal/C2_W04_D03_build_notebooks_INTERNAL.py

Each notebook runs cold in its own folder and ships executed. The prose reads its numbers from the
facts file, so a sentence and the output under it cannot disagree. Code stays small: pandas, the
standard library and matplotlib, and a three-line check defined in the notebook itself. The lab
notebook finds Kalpa's planted values only in its empty your-turn cells.
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


# ================================================================================= notebook 01
def nb01():
    path = OUT / "C2_W04_D03_01_receipts_STUDENT.ipynb"
    cells = [
        md(f"""\
        # Which items go together on twelve Instamart carts, and what does "together" mean?

        **Week 4, Wednesday, chapter 1 of 3.** Swiggy Instamart, Pune: the cart page shows a strip
        of three suggested items under the cart. On {s('change_date')} the strip stopped showing a
        curated list and started showing the items most often found in the same cart. Toned milk
        sits in {s('toned_milk_share')} of Pune carts, so it now appears beside nearly everything,
        and the strip's click-through (clicks over times shown) fell from {s('before_strip_ctr')}
        in the three weeks before to {s('after_strip_ctr')} in the three weeks after. The ask, due
        Friday: rank the pairs the strip should show, explain the fall, and put a rupee value on a
        slot. {LABEL}

        **Who needs the answer.** The category manager, who picks what the strip may suggest, and
        the growth lead, who must explain the fall on Friday. A strip filled on the wrong count
        wastes the three most-clicked spaces on the cart page.

        **The questions on the way.** How often do two items turn up in the same cart? How
        reliably does one bring the other? Do they turn up together more than chance would put
        them there? What can twelve carts not tell us?
        """),
        code(CHECK + PLOT + "import pandas as pd\nprint(\"ready: pandas\", pd.__version__)"),
        md(f"""\
        ## Which sentence about ten tea-stall orders is wrong?

        A tea stall keeps ten receipts (invented for this chapter). Chai is on 6 of them, biscuit
        on 4, and both on 3. A pair has three counts worth knowing. **Support** is how often both
        turn up: carts with both, over all carts. **Confidence** from A to B shrinks the world to
        the orders that hold A and asks how many of those also hold B. **Lift** compares what was
        seen with what chance would give: if chai and biscuit ignored each other, 60 percent of
        the 4 biscuit orders, or 2.4, would also hold chai.

        **Predict before you run.** Which sentence is wrong?

        a) Support for the pair is 3 of 10, or 0.30.
        b) Confidence from chai to biscuit is 3 of 6, or 0.50.
        c) Lift is 1.25, and it reads the same from biscuit to chai.
        d) Lift of 1.25 means chai makes a customer buy 25 percent more biscuits.
        """),
        code("""\
        orders, chai, biscuit, both = 10, 6, 4, 3            # invented counts
        support = both / orders
        conf_chai_biscuit = both / chai
        conf_biscuit_chai = both / biscuit
        expected = orders * (chai / orders) * (biscuit / orders)   # if the two ignored each other
        lift = both / expected
        print(f"support {support:.2f}, confidence chai to biscuit {conf_chai_biscuit:.2f}, "
              f"biscuit to chai {conf_biscuit_chai:.2f}")
        print(f"expected together {expected:.1f}, seen {both}, lift {lift:.2f}")
        check("lift reads the same both ways", abs(lift - conf_biscuit_chai / (chai / orders)) < 1e-9)
        check("lift is seen over expected", abs(lift - 1.25) < 1e-9)
        """),
        md(f"""\
        **What happened.** The wrong sentence is d. Lift is a ratio of counts: the pair turns up
        25 percent more often than chance would put it there, and nothing in ten receipts says
        why. Now add a carry bag, which goes into 9 of the 10 orders and into 3 of the 4 biscuit
        orders. Confidence from biscuit to bag is {s('tea_bag_conf')}, which sounds like a bundle,
        yet the bag is in {s('tea_bag')} of {s('tea_orders')} orders anyway, so lift is
        0.75 / 0.90 = {s('tea_bag_lift')}: biscuit orders hold a bag slightly less often than orders
        in general. An item that is everywhere earns high confidence toward everything.
        """),
        code("""\
        bag, biscuit_with_bag = 9, 3                         # invented counts
        conf_biscuit_bag = biscuit_with_bag / biscuit
        lift_bag = conf_biscuit_bag / (bag / orders)
        fig, ax = plt.subplots(figsize=(8, 2.8))
        ax.barh(["confidence, biscuit to bag", "bag's share of all orders"], [conf_biscuit_bag, bag / orders],
                color=["#5B3FD6", "#E4E1F1"], edgecolor="#1A0F5C")
        ax.set_xlim(0, 1)
        ax.set_title(f"High confidence, lift {lift_bag:.2f}: the bag is in nearly every order")
        plt.show()
        check("the popular bag earns lift below one", lift_bag < 1)
        """),
        md("""\
        ## What do twelve real carts from the case hold?

        These are twelve of the 40,000 Pune carts, printed as cards on each table. Each row is a
        cart and each column an item: 1 if the cart holds it. Count by hand first; the code below
        only confirms the count.
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
        {s('twelve_bread_milk_conf')}. That is the trap of this chapter. A hurried analyst reads
        1.00 as "every bread buyer wants milk, so put milk in the bread cart's strip". The check
        is the count the confidence never looked at: milk was already in 8 of 12 carts, so chance
        alone puts it in about 2.67 of the four bread carts, and lift is 4 / 2.67 =
        {s('twelve_bread_milk_lift')}. Four carts are too few to say more; chapter 2 runs the
        same count on 40,000.
        """),
        code("""\
        def three_counts(a, b):
            has_a, has_b = twelve[a] == 1, twelve[b] == 1
            both = (has_a & has_b).sum()
            return both, has_a.sum(), has_b.sum(), both / n, both / has_a.sum(), both * n / (has_a.sum() * has_b.sum())

        for a, b in [("chips", "cold drink"), ("ice cream", "chocolate sauce")]:
            both, na, nb, sup, conf, lift = three_counts(a, b)
            print(f"{a} and {b}: {na} and {nb} carts, both {both}, support {sup:.2f}, "
                  f"confidence {conf:.2f}, lift {lift:.2f}")
        check("chips and cold drink: lift 2.67", round(three_counts("chips", "cold drink")[5], 2) == 2.67)
        check("ice cream and chocolate sauce: one cart, lift 12", three_counts("ice cream", "chocolate sauce")[0] == 1)
        """),
        md("""\
        ## Which pair beat chance on the twelve, and which number should nobody act on?

        Chips and cold drink sit in 3 carts each and together in 2, where chance gives 0.75: lift
        2.67. Ice cream and chocolate sauce share one cart, and one cart makes a lift of 12, a
        number with nothing under it. The picture puts seen beside expected for the three pairs.
        """),
        code("""\
        pairs = [("bread", "toned milk"), ("chips", "cold drink"), ("ice cream", "chocolate sauce")]
        seen = [three_counts(a, b)[0] for a, b in pairs]
        expect = [three_counts(a, b)[1] * three_counts(a, b)[2] / n for a, b in pairs]
        fig, ax = plt.subplots(figsize=(8, 3.6))
        x = range(len(pairs))
        ax.bar([i - 0.18 for i in x], expect, 0.36, color="#E4E1F1", edgecolor="#1A0F5C", label="expected by chance")
        ax.bar([i + 0.18 for i in x], seen, 0.36, color="#5B3FD6", edgecolor="#1A0F5C", label="seen")
        ax.set_xticks(list(x), [f"{a} + {b}" for a, b in pairs])
        ax.set_ylabel("carts of the twelve")
        ax.legend(frameon=False)
        ax.set_title("Lift is seen over expected")
        plt.show()
        check("every pair here was seen more often than chance", all(s > e for s, e in zip(seen, expect)))
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
          Chapter 2 counts all 40,000.

        **In the interview.** "Support, confidence, lift: what does each answer?" The answer names
        three questions: how often, how reliably, and against chance.
        """),
    ]
    build(path, cells)
    print("wrote", path.relative_to(REPO))


# ================================================================================= notebook 02
def nb02():
    path = OUT / "C2_W04_D03_02_pairs_table_STUDENT.ipynb"
    cells = [
        md(f"""\
        # What do support, confidence and lift say across all 40,000 carts?

        **Week 4, Wednesday, chapter 2 of 3.** Swiggy Instamart, Pune. Since {s('change_date')} the
        cart page's three-slot strip shows the items most often found in the same cart, and its
        click-through fell from {s('before_strip_ctr')} to {s('after_strip_ctr')}. {LABEL}
        Chapter 1 counted twelve carts: bread to milk read confidence
        {s('twelve_bread_milk_conf')} and lift {s('twelve_bread_milk_lift')}, chips and cold drink
        lift {s('twelve_chips_cold_lift')}. This notebook runs the same three counts on every cart.

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

        The strip's new rule ranks by exactly this count. Every cart's items, taken two at a time,
        add one to their pair's tally.

        **Predict before you run.** Which pair is found together most often?

        a) chips and cold drink
        b) bread and toned milk
        c) ice cream and chocolate sauce
        d) onions and tomatoes
        """),
        code("""\
        baskets = items.groupby("cart_id").item.apply(set)
        pair_count = Counter(p for basket in baskets for p in combinations(sorted(basket), 2))
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
        single = Counter(x for basket in baskets for x in basket)
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
        md("""\
        **What happened.** The answer is b. Confidence toward milk sits near milk's own share for
        every item, because most carts hold milk whatever else they hold, and lift divides that
        share out. Amazon met the same trap: counting how often buyers of A also bought B would
        have made the bestseller the top recommendation beside everything, and the fix compares
        with what chance predicts, which is lift in spirit (Amazon Science, checked 12 October
        2026).
        """),
        md(f"""\
        ## Why did the strip's click-through fall from {s('before_strip_ctr')} to {s('after_strip_ctr')}?

        `strip_log` counts each day's impressions (times a slot was shown), clicks and adds, by
        slot, by the anchor item a suggestion was ranked from, and by the suggested item. Every
        cart-page view shows all three slots. The strip shows packs, and toned milk comes in more
        than one pack, so one view can show milk in two slots; the log names every pack by its item.

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

        Split the after-change rows by whether the slot suggested toned milk. For each group print
        its share of impressions and its click-through (clicks over impressions), then check that
        the two rates, weighted by their shares, give back the blended rate. Start from
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
        check("milk slots click at 1.2 percent and the rest at 6.4", round(ctr[True], 3) == 0.012 and round(ctr[False], 3) == 0.064)
        check("the two rates rebuild the blend", abs((ctr * weight).sum() - after.clicks.sum() / after.impressions.sum()) < 1e-12)
        """),
        md(f"""\
        **What happened.** The answer is c. After the change milk filled half the slot
        impressions and clicked at {s('milk_slot_ctr_after')}; everything else clicked at
        {s('other_slot_ctr_after')}, a little above the {s('other_slot_ctr_before')} it drew before.
        Half of 1.2 plus half of 6.4 is 3.8. **The plausible wrong answer** is "shoppers changed
        after the monsoon", which would have the team wait or redesign the strip. **The check** is
        the split by suggested item: the fall sits in the milk slots. **The fix** is to rank by
        lift above a support floor, which chapter 3 builds.
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
        popularity?" Lift, because it divides by the partner's base rate; confidence toward milk
        sits near milk's own {s('toned_milk_share')} for every item.
        """),
    ]
    build(path, cells, timeout=300)
    print("wrote", path.relative_to(REPO))


# ================================================================================= notebook 03
def nb03():
    path = OUT / "C2_W04_D03_03_action_map_STUDENT.ipynb"
    cells = [
        md(f"""\
        # Which pairs should fill the strip, and what is a slot worth in rupees?

        **Week 4, Wednesday, chapter 3 of 3.** Swiggy Instamart, Pune: the strip's click-through
        fell from {s('before_strip_ctr')} to {s('after_strip_ctr')} after it began ranking
        suggestions by how often items share a cart. {LABEL} Chapter 2 found why: milk took half
        the slot impressions and clicked at {s('milk_slot_ctr_after')} against
        {s('other_slot_ctr_after')} for everything else, and lift with milk sits near one for every
        common item. This notebook picks what replaces milk and prices the change.

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

        **Predict before you run.** Which pair should take the first slot?

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
        margin: chips and cold drink {s('chips_cold_lift')}, coriander and green chillies
        {s('coriander_chillies_lift')}, bread and butter {s('bread_butter_lift')}, onions and
        tomatoes {s('onions_tomatoes_lift')}. The next pair reads {s('fifth_pair_lift')}, which is
        chance. The first three fill the strip; the picture places every pair.
        """),
        code("""\
        shown = pairs[pairs.support >= 0.001]
        fig, ax = plt.subplots(figsize=(9, 4.8))
        ax.scatter(shown.support, shown.lift, s=10, alpha=0.4, color="#5B3FD6")
        ax.axvline(floor, color="#6B6690", ls="--"); ax.axhline(1, color="#6B6690", ls="--")
        for _, r in ranked.head(4).iterrows():
            ax.annotate(f"{r.a} + {r.b}", (r.support, r.lift), xytext=(5, 5), textcoords="offset points")
        ax.set_xscale("log"); ax.set_xlabel("support (log scale)"); ax.set_ylabel("lift")
        ax.set_title("Promote above the floor and well above one; watch the strong thin pairs")
        plt.show()
        """),
        md(f"""\
        ## What should the watch list do with a strong pair on few carts?

        Ice cream and chocolate sauce read lift {s('ice_choc_lift')}, the strongest pair between
        0.2 and 1 percent support, but they share {s('ice_choc_carts')} carts in four weeks of
        this sample. A slot shown on every cart page cannot be repaid by a pair that thin, so it
        goes on a **watch list**: tested in two zones before it may take a slot.
        """),
        code("""\
        thin = pairs[(pairs.support >= 0.002) & (pairs.support < floor)].sort_values("lift", ascending=False)
        print(thin.head(4).round(4).to_string(index=False))
        check("ice cream and chocolate sauce lead the thin band", tuple(thin.iloc[0][["a", "b"]]) == ("chocolate sauce", "ice cream"))
        """),
        md(f"""\
        ## What is one slot worth in rupees?

        A slot's margin a day is the cart-page views times its click-through times the share of
        clicks that become an add, times the margin on an added item. Views are
        {s('views_assumed')} a day (the mean in `strip_log` since the change). The add rate
        {s('add_rate_assumed')} is an assumption with a range of {s('add_rate_low')} to
        {s('add_rate_high')} (`strip_log` reads 0.50), and the margin {s('margin_assumed')} an
        assumption with a range of {s('margin_low')} to {s('margin_high')} (a `cart_items` line
        earns {s('margin_per_line_observed')} on average, milk aside).

        **Predict before you run.** What does moving milk's half of the impressions to pairs that
        beat chance recover in a month?

        a) about Rs 50,000
        b) about Rs 2 lakh
        c) about Rs 6 lakh
        d) about Rs 50 lakh
        """),
        code("""\
        views, add_rate, margin = 60_000, 0.5, 9
        def slot_day(ctr):
            return views * ctr * add_rate * margin
        good, milk = slot_day(0.064), slot_day(0.012)
        gap_month = (good - milk) * 30
        recovered = gap_month * 3 * 0.5            # three slots, milk on half the impressions
        low = views * (0.064 - 0.012) * 0.4 * 7 * 30 * 1.5
        high = views * (0.064 - 0.012) * 0.6 * 11 * 30 * 1.5
        print(f"a slot a day: Rs {good:,.0f} with a pair that beats chance, Rs {milk:,.0f} with milk")
        print(f"gap: Rs {good - milk:,.0f} a day, Rs {gap_month / 1e5:.1f} lakh a month per slot")
        print(f"recovered on milk's 1.5 slots' worth: Rs {recovered / 1e5:.1f} lakh a month "
              f"(Rs {low / 1e5:.1f} lakh to Rs {high / 1e5:.1f} lakh across the ranges)")
        fig, ax = plt.subplots(figsize=(7, 3.2))
        ax.bar(["pair that beats chance", "milk"], [good, milk], color=["#1F8A5B", "#D63A6A"])
        ax.set_ylabel("Rs a day, one slot"); ax.set_title("One slot, one day")
        plt.show()
        check("a slot earns Rs 17,280 or Rs 3,240 a day", round(good) == 17_280 and round(milk) == 3_240)
        check("re-ranking recovers Rs 6.3 lakh a month", round(recovered / 1e5, 1) == 6.3)
        """),
        md(f"""\
        **What happened.** The answer is c: {s('recoverable_month')} a month, between
        {s('recoverable_low')} and {s('recoverable_high')} across the two ranges. **The plausible
        wrong answer** books sales as the benefit: 1,920 adds a day at about {s('price_per_add_observed')}
        each reads as {s('gross_sales_day')} a day of "strip revenue", over four times the margin.
        **Why it is wrong.** Growth keeps the margin, never the price; and if the strip ever adds
        a bundle discount, that discount is margin handed back to the customer, the cost line
        Swiggy's own letter describes for Maxxsaver (W4, checked 12 October 2026).
        """),
        code("""\
        after = log[log.date >= "2026-09-07"]
        other = after[after.suggested_item != "toned milk"]
        price = items.drop_duplicates("item").set_index("item").price_rs
        price_per_add = (other.groupby("suggested_item").adds.sum() * price).sum() / other.adds.sum()
        adds = views * 0.064 * add_rate
        print(f"{adds:,.0f} adds a day x Rs {price_per_add:.0f} = Rs {adds * price_per_add:,.0f} of sales; "
              f"the margin is Rs {good:,.0f}")
        check("sales overstate the margin more than four times", adds * price_per_add > 4 * good)
        """),
        md("""\
        ## What can the counts not tell us?

        Six doubts, each with the check that settles it. Co-occurrence is no proof of cause: a
        party shopper buys chips and cold drink together, and promoting chips sells no cold drink
        to anyone else; only a holdout settles that, which the faculty session (tentative) and Week 5 take up.
        Heavy buyers: the top tenth of customers place 38 percent of carts, so lift is recomputed
        with every customer counted once. The stock-out: curd ran out in two zones in week three.
        Time band: morning carts hold milk more often. The strip's own pull: whatever slot 1
        shows draws the most clicks. And per cart against per customer, which the first check
        answers.
        """),
        code("""\
        carts["weight"] = 1 / carts.groupby("customer_id").cart_id.transform("count")
        w = carts.set_index("cart_id").weight
        def lift_per_customer(a, b):
            has_a = baskets.apply(lambda x: a in x); has_b = baskets.apply(lambda x: b in x)
            pa, pb = w[has_a].sum() / w.sum(), w[has_b].sum() / w.sum()
            return w[has_a & has_b].sum() / w.sum() / (pa * pb)
        top_tenth = carts.customer_id.value_counts().head(len(carts.customer_id.unique()) // 10)
        print(f"top tenth of customers: {top_tenth.sum() / n:.0%} of carts")
        per_cart = pairs.set_index(["a", "b"]).lift
        rows = {"chips + cold drink": (per_cart[("chips", "cold drink")], lift_per_customer("chips", "cold drink")),
                "bread + milk": (per_cart[("bread", "toned milk")], lift_per_customer("bread", "toned milk"))}
        for name, (per_cart, per_cust) in rows.items():
            print(f"{name}: lift {per_cart:.2f} per cart, {per_cust:.2f} with each customer counted once")
        fig, ax = plt.subplots(figsize=(7, 2.8))
        ax.barh(list(rows), [r[1] for r in rows.values()], color="#D9A7FF", label="each customer once")
        ax.scatter([r[0] for r in rows.values()], list(rows), color="#1A0F5C", zorder=3, label="every cart")
        ax.axvline(1, color="#6B6690", ls="--"); ax.legend(frameon=False); ax.set_xlabel("lift")
        plt.show()
        check("the top tenth place 38 percent of carts", round(top_tenth.sum() / n, 2) == 0.38)
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
        def lift_in(bs, a, b):
            k = len(bs); na = bs.apply(lambda x: a in x).sum(); nb = bs.apply(lambda x: b in x).sum()
            return bs.apply(lambda x: a in x and b in x).sum() * k / (na * nb)
        print(f"curd's share: {carts.curd.mean():.1%} of all carts, {carts.loc[~hit, 'curd'].mean():.1%} "
              f"with the two zone-weeks set aside")
        print(f"curd and milk lift: {lift_in(baskets, 'curd', 'toned milk'):.2f} and {lift_in(kept, 'curd', 'toned milk'):.2f}")
        check("curd is near zero in the two zones in week three", carts.loc[hit, "curd"].mean() < 0.01)
        by_band = carts.assign(milk=carts.cart_id.isin(items.loc[items.item == "toned milk", "cart_id"])) \\
            .groupby("time_band").milk.mean().sort_values(ascending=False)
        print("share of carts holding milk, by time band:", by_band.round(2).to_dict())
        for band in by_band.index:
            ids = carts.loc[carts.time_band == band, "cart_id"]
            print(f"  {band}: bread and milk lift {lift_in(baskets[ids], 'bread', 'toned milk'):.2f}")
        check("morning carts hold milk most often", by_band.index[0] == "morning")
        """),
        md(f"""\
        ## Does a second route reach the same Rs {s('recoverable_month')[3:]}?

        Read the milk impressions straight from `strip_log` rather than from "half the slots":
        every milk impression moved to a suggestion that beats chance gains the gap in click-through
        times the add rate times the margin.
        """),
        code("""\
        milk_per_day = after[after.suggested_item == "toned milk"].groupby("date").impressions.sum().mean()
        route_two = milk_per_day * (0.064 - 0.012) * add_rate * margin * 30
        print(f"{milk_per_day:,.0f} milk impressions a day -> Rs {route_two / 1e5:.1f} lakh a month")
        check("both routes give Rs 6.3 lakh", round(route_two / 1e5, 1) == round(recovered / 1e5, 1))
        """),
        md(f"""\
        ## What does the growth lead take to Friday?

        - **Which pairs?** Above a floor of {s('support_floor')} of carts: chips and cold drink
          {s('chips_cold_lift')}, coriander and green chillies {s('coriander_chillies_lift')},
          bread and butter {s('bread_butter_lift')}. Milk takes no slot.
        - **The watch list?** Ice cream and chocolate sauce, lift {s('ice_choc_lift')} on
          {s('ice_choc_carts')} carts, tested before it is promoted.
        - **A slot in rupees?** {s('slot_value_other_day')} a day with a pair that beats chance,
          {s('slot_value_milk_day')} with milk; moving milk's half of the impressions recovers
          {s('recoverable_month')} a month.
        - **What the counts cannot say?** Whether the pair causes the purchase; counted per
          customer, chips and cold drink fall to {s('chips_cold_lift_per_customer')} and still beat
          chance; the curd stock-out lowers curd's count and leaves its lift at
          {s('curd_milk_lift_all')}; morning carts hold milk {s('milk_share_morning')} of the time
          and bread with milk still reads about 1.04 in every band.

        **In the interview.** "Turn a basket analysis into a recommendation with a number." Name
        the pairs above a floor, the incremental adds times the margin, the cost line, and the
        assumption that would change the call.
        """),
    ]
    build(path, cells, timeout=600)
    print("wrote", path.relative_to(REPO))


# ================================================================================= notebook 04
def nb04():
    path = OUT / "C2_W04_D03_04_kalpa_lab_STUDENT.ipynb"
    ids = v("kalpa_twelve_ids")
    cells = [
        md("""\
        # Does the pairs method hold up on Kalpa Retail's baskets?

        **Week 4, Wednesday, the TA-led lab.** Kalpa Retail's merchandising team wants to pair
        every product with the Rs 199 phone charger, "because it is in 80 percent of baskets", to
        give Retail-Plus members a reason to come back. The head of merchandising asks which pairs
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
        the charger's share, the screen protector's confidence and lift toward the charger, and the
        lift of wireless earphones with their case. The cell below confirms your count.
        """),
        code(f"""\
        twelve_ids = "{ids}".split(", ")
        twelve = lines[lines.order_id.isin(twelve_ids)].groupby("order_id").name.apply(set)
        for oid, held in twelve.items():
            print(oid, ", ".join(sorted(held)))
        count = Counter(x for held in twelve for x in held)
        fig, ax = plt.subplots(figsize=(8, 3.8))
        names = sorted(count, key=count.get)
        ax.barh(names, [count[x] for x in names], color="#FFF7E6", edgecolor="#C98A00")
        ax.set_xlabel("baskets, of the twelve"); ax.set_title("Twelve Kalpa baskets, counted")
        plt.show()
        check("twelve baskets", len(twelve) == 12)
        """),
        md("""\
        ### Your turn: how often is the charger in a basket, and what is its lift with each product?

        Build `baskets = lines[lines.order_id.isin(consumer.order_id)].groupby("order_id").name.apply(set)`.
        Print the charger's share of baskets. Then, for every product in at least 2 percent of
        baskets, print its confidence toward the charger and its lift with the charger. Write one
        sentence for merchandising on what the numbers say about "it is in 80 percent of baskets".
        """),
        empty(),
        md("""\
        ### Your turn: which pair beats chance above a 5 percent floor, and which is too thin?

        Count every pair with `Counter` over `combinations(sorted(basket), 2)`, as the Instamart
        notebook did. Keep the pairs in at least 5 percent of baskets and rank them by lift; then
        look below the floor for a pair with a high lift on two or three baskets. For the strongest
        pair above the floor, check which segment its baskets come from by joining `orders`.
        """),
        empty(),
        md("""\
        ## Can the data carry the answer?

        Before a number goes to merchandising, two checks that need no pair counts: how many lines
        a basket holds, and whether every amount reconciles to its lines.
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
        ax.set_xlabel("order amount, Rs"); ax.set_ylabel("sum of its lines, Rs")
        ax.set_title("Every order sits on the line: amount = sum of lines")
        plt.show()
        check("consumer baskets hold one to eight lines", per_basket.between(1, 8).all())
        check("Business orders hold one line each",
              (lines[lines.order_id.isin(orders[orders.segment == "Business"].order_id)]
               .groupby("order_id").size() == 1).all())
        check("the charger lists at Rs 199", products.set_index("name").loc["phone charger 20W", "list_price"] == 199)
        """),
        md("""\
        ## What will merchandising's proposal cost, and what do you bring back?

        The unguided Kalpa exercise prices the charger proposal: a bundle discount on every basket
        that already holds the charger is margin handed back for an add that would have happened
        anyway. Bring back three lines: the charger's share and its lift with the products it would
        be bundled with, the pair you would promote with its support and lift, and the pair you
        would watch, with the number of baskets it rests on.
        """),
    ]
    build(path, cells, timeout=300)
    print("wrote", path.relative_to(REPO))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    nb01()
    nb02()
    nb03()
    nb04()


if __name__ == "__main__":
    main()
