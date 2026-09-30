"""Build Monday's notebooks: the retail story, six chapters, the escalated case and the second case.

Run from the repository root:
    python3 content/W01/D1/internal/C2_W01_D01_build_notebooks_INTERNAL.py            every notebook
    python3 content/W01/D1/internal/C2_W01_D01_build_notebooks_INTERNAL.py ch3 case   named ones only

Names: story, ch1 to ch6, case (the escalated case twin and solution), second (the second case twin
and solution). Each teaching notebook is executed cold in its own folder by scripts/nb_make.py, so
the saved outputs are the ones a learner sees on GitHub. The TODO twins are written unexecuted and
their solution twins executed. No cell prints a planted record: the discovery of one sits in an
empty your-turn cell, and a mechanism that needs a plant to show runs on invented records labelled
invented.
"""
import pathlib
import re
import sys

sys.path.insert(0, "scripts")
from nb_make import SETUP, build, code, empty, md  # noqa: E402

DAY = pathlib.Path("content/W01/D1")
NB = DAY / "notebooks"
SOL = DAY / "exercises" / "solutions"

LOAD = SETUP + '''
ORDERS = kit.load_records()
'''

CHAPTERS = ["The retail story", "1. Four readings of sales", "2. The tree as metrics",
            "3. The leaves, counted", "4. The typical order", "5. Which branch first",
            "6. The sentence Meera acts on"]


def where(n, levels):
    """The chapter ladder beside this chapter's levels, the map every notebook opens on."""
    steps = ", ".join(repr(s) for s in levels)
    return code(f'''
        kit.side_by_side(
            kit.ladder({CHAPTERS!r}, lit={n}, show=False),
            kit.vflow([{steps}], lit=0, show=False),
        )''')


def twin(path_todo, path_sol, cells, answers):
    """Write the TODO twin unexecuted and the solution executed, from one list of cells.

    A cell's source may hold __TODOn__ placeholders; the solution replaces each with answers[n].
    A markdown cell whose source starts with SOLUTION ONLY is kept in the solution alone, and one
    starting TODO ONLY in the twin alone, with the marker line removed.
    """
    todo, sol = [], []
    for cell in cells:
        src = cell.source
        if src.startswith("SOLUTION ONLY"):
            cell.source = src.split("\n", 1)[1]
            sol.append(cell)
            continue
        if src.startswith("TODO ONLY"):
            cell.source = src.split("\n", 1)[1]
            todo.append(cell)
            continue
        todo.append(cell)
        if "__TODO" in src:
            new = code(re.sub(r"__TODO(\d+)__", lambda m: answers[int(m.group(1))], src))
            sol.append(new)
        else:
            sol.append(cell)
    build(path_todo, [c.copy() for c in todo], execute=False)
    build(path_sol, sol)


# ----------------------------------------------------------------------------------- the story
def story():
    return [
        md("""
        # The retail story, as formulas

        **Week 1, Monday. The story that opens the day: one Saturday at Kalpa Retail, walked from a
        shopping basket to the metrics every later chapter uses.**

        Most of us have shopped in a store and on an app and never seen the business from the other
        side of the till. This notebook takes one scene from the morning's story, a Retail-Plus
        member's basket on a Saturday, and turns it into the metrics a retail data team is asked for,
        each as a formula. Every number in this notebook is **invented**: they are the round
        illustrative numbers of the domain dossier, chosen so the arithmetic is easy, and none of them
        is Kalpa's data or any real company's. Kalpa's own orders arrive in chapter 1.

        The formulas are the ten on the domain card,
        `cheatsheets/C2_W01_D01_retail_domain_card_STUDENT.pdf`, and the long version of each is in
        the dossier, `study-notes/C2_W01_D01_domain_retail_STUDENT.md`, sections 3 and 5.

        > **Kavya's review.** Before I read any number, I read three things beside it: what it is
        > divided by, over which window, and who asked for it. This notebook is where you practise
        > saying all three.
        """),
        md("""
        **Setup.** The first cell finds the shared helper, `c2kit`, by walking up from this folder
        until it reaches `scripts/`. This notebook needs no data file, since its numbers are
        invented and typed in.
        """),
        code(SETUP + 'print("helper loaded; every number below is invented")'),
        where(0, ["1. where Rs 100 of GMV goes", "2. one order's contribution",
                  "3. the app's funnel", "4. the revenue tree for a month",
                  "5. customers over time", "6. what a customer is worth"]),
        md("""
        ## 1. Rs 100 of GMV leaves Rs 2.50 of operating profit

        The member's basket shows Rs 1,800 at the checkout. Gross merchandise value (GMV) is everything
        customers ordered at the price charged; the profit and loss statement walks it down, one
        deduction at a time. On Rs 100 of invented GMV: Rs 4 is cancelled and Rs 6 returned, Rs 10 is
        GST collected for the government, Rs 60 pays for the goods, Rs 12.50 is spent per order on
        delivery, returns, payment fees and marketing, and Rs 5 pays the fixed costs.

        **Predict before you run.** Of Rs 100 ordered, how much is left as operating profit?

        - a) About Rs 25, the gross margin.
        - b) About Rs 10, what a shop keeps after tax.
        - c) Rs 2.50.
        - d) Nothing, since retail runs at a loss.
        """),
        code("""
        gmv = 100.0                               # invented, the dossier's illustrative Rs 100
        steps = [("cancelled and returned", -10), ("GST, collected for the state", -10),
                 ("cost of the goods", -60), ("per-order costs", -12.5), ("fixed costs", -5)]
        left = gmv
        levels = {}
        names = ["kept", "net revenue", "gross margin", "contribution", "operating profit"]
        for (label, change), name in zip(steps, names):
            left += change
            levels[name] = left
        kit.bridge(("GMV, invented", gmv), steps, end_label="operating profit", lit=(3,),
                   fmt=lambda v: f"Rs {v:g}", title="Invented: where Rs 100 of GMV goes")
        kit.table(["line", "Rs left of 100"], [(n, f"{v:g}") for n, v in levels.items()],
                  caption="Invented numbers, the dossier's walk from GMV to operating profit")
        """),
        md("""
        **What happened.** The answer is c. Net revenue is Rs 80, gross margin Rs 20 (25 percent of
        net revenue), contribution Rs 7.50 and operating profit Rs 2.50. A retailer keeps a thin
        slice, which is why a price cut that brings no extra volume can give away the whole profit.
        """),
        code("""
        kit.check("net revenue is Rs 80 of every Rs 100 of GMV", levels["net revenue"] == 80)
        kit.check("gross margin is 25 percent of net revenue",
                  levels["gross margin"] / levels["net revenue"] == 0.25)
        kit.check("operating profit is Rs 2.50", levels["operating profit"] == 2.5)
        """),
        md("""
        ## 2. One order's contribution is Rs 150 of the Rs 1,800 paid

        Contribution is gross margin less the costs that come with each order: picking and delivery,
        the payment fee, the expected cost of returns and the marketing that brought the order. It is
        what the order adds towards the costs that do not change with one more order.

        **Predict before you run.** The member paid Rs 1,800. What does the order contribute?

        - a) Rs 1,800, what the member paid.
        - b) Rs 150.
        - c) Rs 400, the gross margin.
        - d) Rs 1,600, the net revenue.
        """),
        code("""
        basket = {"charged at checkout": 1800, "GST inside the price": -200, "cost of the four items": -1200,
                  "picking, packing and delivery": -120, "payment fee": -20,
                  "expected cost of returns": -50, "marketing that brought the order": -60}  # invented
        net_revenue = basket["charged at checkout"] + basket["GST inside the price"]
        gross_margin = net_revenue + basket["cost of the four items"]
        contribution = gross_margin + sum(v for k, v in basket.items()
                                          if k not in ("charged at checkout", "GST inside the price",
                                                       "cost of the four items"))
        kit.bridge(("charged, invented", 1800), [(k, v) for k, v in basket.items() if v < 0],
                   end_label="contribution", title="Invented: the Saturday basket, walked to contribution")
        print(f"net revenue {kit.rupees(net_revenue)}, gross margin {kit.rupees(gross_margin)} "
              f"({gross_margin / net_revenue:.0%}), contribution {kit.rupees(contribution)} "
              f"({contribution / net_revenue:.1%} of net revenue)")
        """),
        code("""
        kit.check("gross margin percent = (net revenue less COGS) / net revenue = 25 percent",
                  gross_margin / net_revenue == 0.25, f"{gross_margin / net_revenue:.0%}")
        kit.check("contribution on the basket is Rs 150", contribution == 150, kit.rupees(contribution))
        """),
        md("""
        **What happened.** The answer is b. Delivery costs about the same whatever is in the bag, so a
        small basket carries the same trip on far less margin; that is the arithmetic behind a minimum
        order for free delivery.

        ## 3. Conversion depends on what you divide by

        On the invented Saturday the app had 50,000 visitors, 80,000 sessions, 8,000 carts and 2,000
        orders. Conversion is orders over visits in the same window, and "visits" has more than one
        honest reading.

        **Predict before you run.** Which conversion is right: orders over sessions, or orders over
        visitors?

        - a) Over sessions, 2.5 percent, because sessions are what the app counts.
        - b) Over visitors, 4.0 percent, because visitors are people.
        - c) Either, as long as the denominator is named and kept the same across periods.
        - d) Neither, because carts are the real visits.
        """),
        code("""
        funnel = [("visitors", 50000), ("sessions", 80000), ("carts", 8000), ("orders", 2000)]  # invented
        f = dict(funnel)
        rates = [("orders / sessions", f["orders"] / f["sessions"]),
                 ("orders / visitors", f["orders"] / f["visitors"]),
                 ("orders / carts", f["orders"] / f["carts"])]
        kit.columns([n for n, _ in funnel], [("count", [v for _, v in funnel])], width=560,
                    title="Invented: one Saturday on the app")
        kit.table(["conversion", "value"], [(n, f"{r:.1%}") for n, r in rates],
                  caption="Three honest conversions on the same Saturday")
        kit.check("conversion over sessions is 2.5 percent", rates[0][1] == 0.025)
        kit.check("conversion over visitors is 4.0 percent", rates[1][1] == 0.04)
        """),
        md("""
        **What happened.** The answer is c. All three are correct arithmetic; they measure different
        things. An app update that starts new sessions sooner cuts conversion over sessions with no
        change in buyers, which is a denominator that shifted, the first trap on the card.

        ## 4. Revenue is a tree, and the leaks come off it

        For the invented month, 40,000 customers placed 1.25 orders each, of four items, at Rs 450 an
        item, before a 10 percent discount. The tree multiplies them. Returns and cancellations then
        leak out of what the tree produced, and the leaks can grow faster than the revenue.

        **Predict before you run.** Next month revenue rises 10 percent while returns climb from 6 to
        12 percent of it. How much more does Kalpa keep?

        - a) 10 percent more, since revenue rose 10 percent.
        - b) About 3 percent more.
        - c) 4 percent more, 10 less the 6 points of extra returns.
        - d) Less than before.
        """),
        code("""
        month = {"customers": 40000, "orders per customer": 1.25, "items per order": 4,
                 "price per item": 450, "kept after discount": 0.90}                # invented
        revenue = 1.0
        for v in month.values():
            revenue *= v
        kit.driver_tree({"label": "revenue", "note": kit.rupees(revenue), "kind": "known", "children": [
            {"label": "customers", "note": "40,000", "kind": "known"},
            {"label": "orders per customer", "note": "1.25", "kind": "known"},
            {"label": "order value", "note": "4 items x Rs 450, less 10%", "kind": "known"}]},
            title="Invented: one month's revenue tree")
        kept_before = 100 * (1 - 0.06)                                          # invented index
        kept_after = 110 * (1 - 0.12)
        kit.columns(["this month", "next month"], [("revenue, index", [100, 110]), ("kept after returns", [kept_before, kept_after])],
                    fmt=lambda v: f"{v:g}", title="Invented: revenue up 10, kept up about 3")
        print(f"kept: {kept_before:g} then {kept_after:g}, up {kept_after / kept_before - 1:.1%}")
        kit.check("the tree multiplies to Rs 8.1 crore", round(revenue) == 81000000, kit.rupees(revenue))
        kit.check("what Kalpa keeps rises about 3 percent", round(kept_after / kept_before - 1, 2) == 0.03)
        """),
        md("""
        **What happened.** The answer is b: 100 less 6 is 94, and 110 less 13.2 is 96.8, up about 3
        percent. A growth figure has to say which side of the leaks it was measured on, which is the
        question chapter 1 asks of Kalpa's own orders.

        ## 5. Retention divides by the cohort, never by the survivors

        January brought 1,000 new customers (invented). 380 ordered in February, 300 in March and
        260 in April. Retention in month k is the cohort's buyers in month k over the cohort's
        starting size.

        **The plausible wrong answer.** A hurried analyst divides March's 300 by February's 380 and
        reports 79 percent retention.
        """),
        code("""
        cohort = 1000                                                     # invented
        buyers = {"Feb": 380, "Mar": 300, "Apr": 260}
        right = {m: b / cohort for m, b in buyers.items()}
        hurried_march = buyers["Mar"] / buyers["Feb"]
        kit.line(list(buyers), [("retention, over the cohort of 1,000", [round(r * 100) for r in right.values()], "good")],
                 fmt=lambda v: f"{v:g}%", title="Invented: January's cohort, month by month")
        print(f"March retention: {right['Mar']:.0%} over the cohort; {hurried_march:.0%} over the survivors")
        kit.check("March retention over the cohort is 30 percent", right["Mar"] == 0.30)
        kit.check("the survivor division reads 79 percent", round(hurried_march * 100) == 79)
        """),
        md("""
        **Why it is wrong.** 79 percent answers "of February's buyers, how many bought again", a
        different metric. Reported as retention it tells the head of Retail-Plus that the tier holds
        four in five customers when it holds three in ten.

        ## 6. A customer is worth contribution, and the budget pays back from it

        Customer lifetime value, simply: contribution per order, times orders a year, times years as a
        customer. Customer acquisition cost (CAC) is acquisition spend over the new customers it
        brought, and payback is CAC over monthly contribution per customer. On invented numbers:
        Rs 150 of contribution per order, 6 orders a year, 2 years, and Rs 12 crore bringing 80,000
        new customers.

        **Predict before you run.** How many months does one new customer take to pay back their
        acquisition cost?

        - a) One month, since one order of Rs 1,600 covers Rs 1,500.
        - b) 20 months.
        - c) 12 months, one year of orders.
        - d) Never, since contribution is below CAC.
        """),
        code("""
        per_order, per_year, years = 150, 6, 2                            # invented
        clv = per_order * per_year * years
        clv_on_revenue = 1600 * per_year * years
        cac = 12_00_00_000 / 80000
        monthly = per_order * per_year / 12
        payback = cac / monthly
        kit.bars([("CLV on contribution", clv), ("CAC", cac), ("CLV on revenue, the trap", clv_on_revenue)],
                 fmt=kit.rupees, lit=(2,), title="Invented: what one customer is worth, two ways")
        print(f"CLV {kit.rupees(clv)}, CAC {kit.rupees(cac)}, payback {payback:.0f} months")
        kit.check("CLV on contribution is Rs 1,800", clv == 1800)
        kit.check("CAC is Rs 1,500", cac == 1500)
        kit.check("payback is 20 months", payback == 20)
        """),
        md("""
        **What happened.** The answer is b. Rs 75 of contribution a month repays Rs 1,500 in 20 months,
        leaving Rs 300 of the Rs 1,800 lifetime value. Valued on revenue the same customer reads
        Rs 19,200, more than ten times too high, and every acquisition budget sized on it is too
        large. Option a pays the CAC out of revenue, which is the same mistake in one line.

        ### The card's other three formulas

        Inventory days, gross margin, and like-for-like growth each carry a trap the card names. The
        cell computes all three on invented numbers.
        """),
        code("""
        inventory_days = 45_00_000 / 1_00_000                                  # invented
        margin, net, gmv = 400, 1600, 1800                                      # the invented basket
        on_net, on_gmv = margin / net, margin / gmv
        total_growth = (510 + 65) / 500 - 1                                     # invented, Rs crore
        like_for_like = 510 / 500 - 1
        kit.table(["metric", "formula", "invented result", "the trap"],
                  [("inventory days", "stock at cost / COGS per day", f"{inventory_days:.0f} days",
                    "stock at selling price inflates the days"),
                   ("gross margin", "(net revenue less COGS) / net revenue", f"{on_net:.0%}",
                    f"divided by GMV it reads {on_gmv:.0%}, and GST moves it"),
                   ("like-for-like growth", "both-year stores' sales / last year's, less 1",
                    f"{like_for_like:.0%}", f"total growth with 20 new stores reads {total_growth:.0%}")],
                  caption="Invented numbers for the card's last three formulas")
        kit.columns(["gross margin", "growth"], [("the trap", [on_gmv * 100, total_growth * 100]),
                                                 ("the right number", [on_net * 100, like_for_like * 100])],
                    fmt=lambda v: f"{v:.0f}%", title="Invented: the trap against the right number")
        kit.check("margin on net revenue is 25 percent, on GMV 22", (round(on_net, 2), round(on_gmv, 2)) == (0.25, 0.22))
        kit.check("like-for-like growth is 2 percent against 15 total", (round(like_for_like, 2), round(total_growth, 2)) == (0.02, 0.15))
        """),
        md("""
        ### In the interview

        **[S] How does a retailer make money, and why is a marketplace's GMV not its revenue?** "A
        retailer buys goods and sells them at a margin: GMV less cancellations, returns and GST is net
        revenue, less the cost of goods is gross margin, less per-order costs is contribution, less
        fixed costs is operating profit, and real retailers keep a few rupees in a hundred. A
        marketplace does not own the goods, so the GMV it shows is its sellers' sales and its revenue
        is only the fees it charges them."

        **[S] Define average order value, conversion and repeat rate, and say what each is divided
        by.** "Average order value is revenue over orders; conversion is orders over visits, sessions
        or visitors, whichever is named, in the same window; repeat rate is customers with two or more
        orders over customers who ordered. I say the denominator and the window before the number,
        because each metric changes meaning when either moves."

        ## What the story established
        """),
        code("""
        kit.table(["formula", "invented worked number", "who asks"],
                  [("net revenue = GMV less cancellations, returns, GST", "Rs 80 of Rs 100", "the finance controller"),
                   ("contribution = gross margin less per-order costs", "Rs 150 on Rs 1,800", "the finance controller"),
                   ("conversion = orders / visits, same window", "2.5% of sessions", "marketing"),
                   ("revenue = customers x orders per customer x order value", "Rs 8.1 crore; kept up 3% on 10%", "the CEO"),
                   ("retention = cohort buyers in month k / cohort size", "30% in March", "the head of Retail-Plus"),
                   ("payback = CAC / monthly contribution per customer", "20 months", "the CEO, before signing")],
                  caption="The story's formulas; every number invented")
        kit.check_summary()
        print("Next: chapter 1 opens Kalpa's own 30 orders and asks which total is 'sales'.")
        """),
    ]


# --------------------------------------------------------------------------------- chapter 1
def ch1():
    return [
        md("""
        # Chapter 1. Four readings of sales

        **Week 1, Monday. Chapter 1 of 6: which total is "sales", and which one goes beside Meera's
        plan?**

        **The need.** Kalpa Retail grew revenue 4 percent last year against a plan of 15, and
        marketing wants Rs 12 crore to acquire customers. Meera Raghavan, the CEO, asks the team:

        > "Before I sign anything, I want to understand our own sales. What is 'sales' made of? Where
        > does revenue come from, by customer type and channel? Is acquisition even the branch that is
        > short?"

        | | |
        |---|---|
        | The metric at stake | Sales, the base every growth percentage is measured from |
        | Who asks | Meera Raghavan, CEO, and behind her Anand Iyer, the finance controller, whose books the number must match |
        | What a wrong number costs | A growth plan measured from demand that never became a sale, and a store baseline inflated by orders nobody kept |
        | A real company with the same question | Reliance Retail reported gross revenue of Rs 90,408 crore and revenue from operations of Rs 79,745 crore for the same quarter to June 2026, with GST recovered as the step between them (Reliance Industries media release, 17 July 2026). Two honest totals for one quarter is normal in retail. |
        | In the dossier (`study-notes/C2_W01_D01_domain_retail_STUDENT.md`) | Section 3, how the business makes money: GMV walked to net revenue, and why two correct totals exist for one quarter |

        The story walked Rs 100 of GMV down to net revenue. This chapter does the same walk on Kalpa's
        own 30 orders, from 1 July to 26 September 2026, and settles which total earns the word
        "sales".

        > **Kavya's review.** Every number you bring me today carries its definition beside it.
        > "Sales is five lakh" is a rumour. "Booked sales on 30 orders, cancellations included" is a
        > number I can take into Meera's room.
        """),
        md("""
        **Setup.** The first cell finds the shared helper, `c2kit`, and loads the 30 orders from
        `../data/` as `ORDERS`, a list of dictionaries, one per order. Run it again after any kernel
        restart.
        """),
        code(LOAD + '''
first_day = min(order["order_date"] for order in ORDERS)
last_day = max(order["order_date"] for order in ORDERS)
print(len(ORDERS), "orders loaded, dated", first_day, "to", last_day)
'''),
        where(1, ["the options, sized", "the build: three sums in one loop",
                  "the trap: cancelled orders as sales", "the second route: sums by status"]),
        md("""
        ## The options

        Four ways a team could answer "what are our sales?", each sized on this file.

        | Option | Rows touched | Time | Error on this file | When it is the right call |
        |---|---|---|---|---|
        | A. Add every amount and send the total | 30 | under a second | counts every cancelled order as a sale | never alone; it is the booked reading, and needs its name |
        | B. Sum by status, report booked, not cancelled and delivered, with the bridge between them | 30, once | under a second | none once the bridge lands | a CEO's first look, when the plan's definition is not yet known |
        | C. Ask Finance for the figure in the books | none | a day or more | none, on Finance's definition | when the number goes to the board and must match the books |
        | D. Tick orders off by hand in a spreadsheet | 30 | about ten minutes | a typo in one of 30 cells | never at 30 rows; impossible at 30 lakh |

        **The best-fit call.** B: one pass gives all three readings, and the bridge names every rupee
        between them, so Meera sees which total she is reading. **What would change it:** if Finance
        has already fixed the definition the 15 percent plan was set on, C decides which of B's
        three totals goes in the note, and B's bridge explains the gap to the others.

        The cell below measures option A's error before any build: it counts the orders whose status
        says they never became a sale.
        """),
        code("""
        statuses = {}
        for order in ORDERS:
            statuses[order["status"]] = statuses.get(order["status"], 0) + 1
        kit.table(["option", "rows touched", "orders it counts that never became a sale"],
                  [("A. add every amount", len(ORDERS), statuses["cancelled"]),
                   ("B. sum by status, with the bridge", len(ORDERS), 0),
                   ("C. Finance's books", 0, "Finance's definition"),
                   ("D. by hand", len(ORDERS), "0, if no typo")],
                  caption="The four options, sized on this file")
        kit.bars([(s, n) for s, n in statuses.items()], lit=(2,),
                 title="The 30 orders by status: what option A would count as sales")
        kit.check("the file holds 30 orders", len(ORDERS) == 30)
        kit.check("some orders never became sales", statuses["cancelled"] > 0, statuses)
        """),
        md("""
        ## 1. The build: one loop keeps three sums

        One Kalpa order is a dictionary of seven named fields. The field that splits the readings of
        sales is `status`: delivered, returned after delivery, or cancelled before it left.

        **Predict before you run.** The loop below adds every amount to a running total. What does it
        print?

        - a) 30 and a total in rupees.
        - b) An error part of the way through the list.
        - c) 0, because the total starts at zero.
        - d) A total smaller than the true one, because returns come off.

        The `with kit.expect_error()` line catches an error so the notebook keeps running.
        """),
        code("""
        with kit.expect_error() as stopped:
            booked = 0
            for order in ORDERS:
                booked += order["amount"]
            print(len(ORDERS), booked)
        """),
        md("""
        **What happened.** The answer is b. The last line reads `TypeError: unsupported operand
        type(s) for +=: 'int' and 'str'`: a whole number on the left, text on the right, and Python
        will not add text to a number. One amount in the file is stored as text. That gets two
        minutes and no more.

        **Your turn.** The loop stopped on a record, and `order` still holds it. Type these two lines
        into the empty cell below and say what is odd about the record:

        ```python
        print(order)
        print(type(order["amount"]))
        ```
        """),
        empty(),
        md("""
        **The fix for today** is `int()`, which turns text that looks like a whole number into a
        number. Why an amount arrived as text, and whether a larger file holds more, is Wednesday's
        question. Now the build proper: one loop, three sums.

        **Predict before you run.** Which rupee reading comes out largest?

        - a) Delivered, because only delivered orders are real.
        - b) Not cancelled, because it keeps returns and deliveries.
        - c) Booked, because it keeps every order.
        - d) All three are equal.
        """),
        code("""
        readings = {"orders": 0, "booked": 0, "not cancelled": 0, "delivered": 0}
        for order in ORDERS:
            amount = int(order["amount"])
            readings["orders"] += 1
            readings["booked"] += amount
            if order["status"] != "cancelled":
                readings["not cancelled"] += amount
            if order["status"] == "delivered":
                readings["delivered"] += amount
        kit.table(["reading of sales", "what it keeps", "value"],
                  [("order count", "every row", readings["orders"]),
                   ("booked", "every order placed", kit.rupees(readings["booked"])),
                   ("not cancelled", "orders that left the shelf, returns included", kit.rupees(readings["not cancelled"])),
                   ("delivered", "orders that reached a customer and stayed", kit.rupees(readings["delivered"]))],
                  caption="Four readings of sales on the same 30 orders")
        kit.bars([(k, readings[k]) for k in ("booked", "not cancelled", "delivered")], fmt=kit.rupees,
                 lit=(0,), title="Three rupee readings of one quarter")
        """),
        code("""
        kit.check("the loop visited all 30 orders", readings["orders"] == 30)
        kit.check("booked sales is Rs 5,44,810", readings["booked"] == 544810, kit.rupees(readings["booked"]))
        kit.check("each narrower reading keeps less",
                  readings["booked"] >= readings["not cancelled"] >= readings["delivered"])
        """),
        md("""
        **What happened.** The answer is c. Booked is Rs 5,44,810, not cancelled Rs 5,35,760 and
        delivered Rs 5,20,790. The order count, 30, is the fourth reading and answers how many times
        somebody decided to buy.

        ## 2. The trap: cancelled orders reported as sales

        **Predict before you run.** Of the 30 orders in the booked total, how many never became a sale?

        - a) None, since every row is an order.
        - b) Nine, the returns and the cancellations.
        - c) Five, the orders that came back.
        - d) Four, the orders cancelled before they left.

        **The plausible wrong answer.** The hurried analyst's line, exactly as it would be sent:
        """),
        code("""
        print("Sales this quarter:", kit.rupees(readings["booked"]), "on", readings["orders"], "orders")
        """),
        md("""
        **Why it is wrong.** A cancelled order never left the shelf and never paid Kalpa a rupee, so it
        is demand that never arrived. Sent as "sales", it overstates the base Meera's 15 percent plan
        is measured from and the channel it sits in. The check counts orders by channel and status
        before adding anything.
        """),
        code("""
        grid = {}
        for order in ORDERS:
            key = (order["channel"], order["status"])
            grid[key] = grid.get(key, 0) + 1
        channels = ["app", "web", "store"]
        kit.columns(channels, [(s, [grid.get((c, s), 0) for c in channels])
                               for s in ["delivered", "returned", "cancelled"]],
                    lit=(2,), title="Orders by channel and status: every cancellation is a store order")
        cancelled_channels = {c for (c, s) in grid if s == "cancelled"}
        kit.check("the statuses split 21 delivered, 5 returned, 4 cancelled",
                  (statuses["delivered"], statuses["returned"], statuses["cancelled"]) == (21, 5, 4))
        kit.check("every cancelled order is a store order", cancelled_channels == {"store"})
        """),
        md("""
        **The fix, and what changed.** The answer is d. Write the definition beside the number and show
        the walk between the readings: taking out the cancellations moves Rs 9,050 and 4 store orders
        out of sales; taking out the returns moves another Rs 14,970 and 5 web orders. Store's 10
        orders overstate its kept orders by 4 in 10.
        """),
        code("""
        kit.bridge(("booked, 30 orders", readings["booked"]),
                   [("cancelled, 4 orders", readings["not cancelled"] - readings["booked"]),
                    ("returned, 5 orders", readings["delivered"] - readings["not cancelled"])],
                   end_label="delivered, 21 orders", lo=500000,
                   title="From booked to delivered (the axis starts at Rs 5,00,000 so the moves show)")
        kit.check("cancelled orders carry Rs 9,050", readings["booked"] - readings["not cancelled"] == 9050)
        kit.check("returned orders carry Rs 14,970", readings["not cancelled"] - readings["delivered"] == 14970)
        """),
        md("""
        ## A second route: sums by status, then combine

        The same three totals come out of a dictionary that adds rupees under each status, after which
        each reading is a sum of statuses. If the two routes disagree, one of them has a bug.
        """),
        code("""
        by_status = {}
        for order in ORDERS:
            by_status[order["status"]] = by_status.get(order["status"], 0) + int(order["amount"])
        second = {"booked": sum(by_status.values()),
                  "not cancelled": by_status["delivered"] + by_status["returned"],
                  "delivered": by_status["delivered"]}
        kit.table(["reading", "one loop, three sums", "sums by status, combined"],
                  [(k, kit.rupees(readings[k]), kit.rupees(second[k])) for k in second],
                  caption="Two routes to the same three totals")
        for k in second:
            kit.check(f"{k}: both routes agree", second[k] == readings[k], kit.rupees(second[k]))
        """),
        md("""
        **When to switch.** The status dictionary is the better route when a fourth status appears
        (a part-refund, say), since it needs no new `if`; the one-loop route is clearer when a reader
        must see each definition written out. At a million rows either becomes one `GROUP BY status`
        in SQL, which Week 2 teaches.

        > **Kavya's review.** You found Rs 9,050 that was never a sale, and you found it by counting
        > before adding. Which definition Meera plans on is her call; your job is to make sure she can
        > see which one she is reading.

        ### In the interview

        **[F] What counts as "sales": booked, net of cancellations, or delivered, and which do you give
        a CEO?** "All three are legitimate and answer different questions: booked is demand, net of
        cancellations is what left the shelf, delivered is what stayed sold. On Kalpa's quarter they
        were Rs 5,44,810, Rs 5,35,760 and Rs 5,20,790. I give the CEO the one her plan was set on, say
        it beside the number, and show the bridge so the gaps are named. Reliance Retail publishes
        gross revenue and revenue from operations for the same quarter for the same reason."

        **[D] How would you decide between summing the file yourself and asking Finance for the
        number?** "By who acts on it. For a first look I sum by status in one pass, which takes a
        second and shows every reading. For anything that reaches the board I reconcile to Finance's
        figure, because a number that disagrees with the books loses the room whatever its logic."

        ### Depth: what a fourth status would do

        A part-refunded order would sit between delivered and returned. The status route absorbs it
        with no new code; the one-loop route needs a new `if` for every reading it touches. That is
        the general rule: when the categories may grow, group by the category.

        ## What this chapter established
        """),
        code("""
        kit.table(["What we now know", "The evidence"],
                  [("Sales has four readings; the definition goes beside the number",
                    "Rs 5,44,810 booked, Rs 5,35,760 not cancelled, Rs 5,20,790 delivered"),
                   ("Cancelled orders are demand that never arrived, all in store", "Rs 9,050 on 4 orders"),
                   ("One amount is text, and int() fixes it for today", "the TypeError, met in two minutes")],
                  caption="Chapter 1: four readings of sales")
        kit.driver_tree({"label": "revenue", "note": "definition named", "kind": "known", "children": [
            {"label": "customers", "note": "chapter 3", "kind": "unknown"},
            {"label": "orders per customer", "note": "chapter 3", "kind": "unknown"},
            {"label": "average order value", "note": "chapter 2", "kind": "lit"}]},
            title="Where the tree stands after chapter 1")
        kit.check_summary()
        print("Next: chapter 2 turns each branch of the tree into a metric with a numerator and a denominator.")
        """),
    ]


# --------------------------------------------------------------------------------- chapter 2
def ch2():
    return [
        md("""
        # Chapter 2. The tree as metrics

        **Week 1, Monday. Chapter 2 of 6: which branches make revenue, and can each be measured?**

        **The need.** Meera asked what sales is made of. The answer is a tree: revenue is customers,
        times orders per customer, times average order value, and order value is items per order times
        price per item, less discounts. A branch helps her only when it is a metric, a numerator over a
        denominator on one definition and one window.

        | | |
        |---|---|
        | The metric at stake | Average order value (AOV), revenue over orders, the first branch this file can measure |
        | Who asks | Meera, for the tree; marketing, whose payback case values each new customer by the order they place |
        | What a wrong number costs | A tree built from two definitions multiplies to revenue nobody booked, and a budget is sized on it |
        | A real company with the same question | Reliance reported Jio's quarter as its branches: 533 million subscribers and revenue per user of Rs 215.6 a month (Reliance Industries media release, 17 July 2026). A telecom's tree is customers times revenue per customer, stated the way this chapter states Kalpa's. |
        | In the dossier (`study-notes/C2_W01_D01_domain_retail_STUDENT.md`) | Section 5, the metrics as formulas: the metric tree, and AOV and basket size |

        Chapter 1 settled the readings of sales: Rs 5,44,810 booked on 30 orders, Rs 5,35,760 not
        cancelled on 26, Rs 5,20,790 delivered on 21. This chapter builds the tree on top of them.

        > **Kavya's review.** A branch you cannot divide is a label, not a metric. Give me each branch
        > as a fraction, and tell me which ones this file cannot fill.
        """),
        code(LOAD + '''
for order in ORDERS:
    order["amount"] = int(order["amount"])     # chapter 1's fix, applied once
print(len(ORDERS), "orders loaded, every amount a whole number")
'''),
        where(2, ["the options, sized", "the build: each branch as a fraction",
                  "the trap: two definitions in one fraction", "the second route: the mean of the amounts"]),
        md("""
        ## The options

        Which tree to draw depends on which fields the file holds.

        | Option | Fields it needs | In this file? | What it can tell Meera |
        |---|---|---|---|
        | A. Revenue = orders x AOV | amount, one row per order | yes | the size of orders, and nothing about who buys |
        | B. Revenue = customers x orders per customer x AOV | amount, customer id | yes | who buys, how often, and for how much |
        | C. B, with AOV split into items x price, less discounts | items, list price, discount per order | no | which part of the basket moved |
        | D. A funnel, visits to orders | sessions or footfall | no | where shoppers drop out before buying |

        **The best-fit call.** B, since it is the deepest tree this file fills and it puts
        marketing's branch, customers, beside the two it competes with. **What would change it:**
        order lines with items and prices (the order-items table arrives later in the programme) move
        the call to C; traffic data would add D in front.
        """),
        code("""
        fields = set(ORDERS[0])
        needed = {"A": {"amount"}, "B": {"amount", "customer_id"},
                  "C": {"amount", "customer_id", "items", "price", "discount"},
                  "D": {"sessions", "amount"}}
        kit.table(["option", "fields needed", "missing from this file"],
                  [(k, ", ".join(sorted(v)), ", ".join(sorted(v - fields)) or "none") for k, v in needed.items()],
                  caption="Each tree's fields against the file's " + str(len(fields)))
        fillable = [k for k, v in needed.items() if v <= fields]
        kit.check("options A and B are the ones this file can fill", fillable == ["A", "B"], fillable)
        """),
        md("""
        ## 1. The build: every branch as a fraction

        **Predict before you run.** Booked revenue is split into orders times AOV. What does
        multiplying the two back together give?

        - a) Exactly booked revenue, because the average was made from that total.
        - b) More than booked revenue, because repeat customers count twice.
        - c) Less than booked revenue, because the average rounds down.
        - d) Nothing useful until prices per item are known.
        """),
        code("""
        orders = len(ORDERS)
        revenue = sum(order["amount"] for order in ORDERS)
        aov = revenue / orders
        kit.table(["branch", "numerator", "denominator", "in this file"],
                  [("customers", "distinct customer ids", "none, it is a count", "chapter 3 counts it"),
                   ("orders per customer", "orders", "distinct customers", "chapter 3"),
                   ("average order value", "revenue", "orders", kit.rupees(aov)),
                   ("items per order", "items sold", "orders", "not in this file"),
                   ("price per item", "revenue before discounts", "items sold", "not in this file"),
                   ("discount rate", "rupees discounted", "revenue before discounts", "not in this file")],
                  caption="Every branch as a metric, booked definition, 1 July to 26 September")
        kit.driver_tree({"label": "revenue", "note": kit.rupees(revenue) + " booked", "kind": "known", "children": [
            {"label": "customers", "note": "chapter 3", "kind": "unknown"},
            {"label": "orders per customer", "note": "chapter 3", "kind": "unknown"},
            {"label": "average order value", "note": kit.rupees(aov), "kind": "known", "children": [
                {"label": "items per order", "note": "not in file", "kind": "unknown"},
                {"label": "price per item", "note": "not in file", "kind": "unknown"},
                {"label": "less discounts", "note": "not in file", "kind": "unknown"}]}]},
            title="The revenue tree: what this file can and cannot measure")
        kit.equation(["revenue\\n" + kit.rupees(orders * aov), "=", f"orders\\n{orders}", "x",
                      "average order value\\n" + kit.rupees(aov)], title="The two-branch form, multiplied back")
        """),
        code("""
        kit.check("orders x AOV lands on booked revenue", round(orders * aov) == revenue, kit.rupees(orders * aov))
        kit.check("booked AOV is Rs 18,160", round(aov) == 18160, kit.rupees(aov))
        missing = [b for b in ("items", "price", "discount") if b not in ORDERS[0]]
        kit.check("three branches of six are not in this file", len(missing) == 3, missing)
        """),
        md("""
        **What happened.** The answer is a. That is the tree's strength and its limit: the product
        always lands on revenue, so a wrong leaf never shows in the total and only shows in the split.
        Whether Rs 18,160 describes an order anyone would recognise is chapter 4's question.

        ## 2. The trap: a fraction built from two definitions

        Finance's report carries booked revenue. The operations dashboard counts delivered orders,
        because delivery is what it runs. An analyst in a hurry takes one number from each.

        **Predict before you run.** Booked rupees over delivered orders gives what AOV?

        - a) Rs 18,160, the same as before.
        - b) Rs 24,800, the delivered AOV.
        - c) Rs 25,943.
        - d) Rs 23,687.

        **The plausible wrong answer.**
        """),
        code("""
        delivered_orders = sum(1 for order in ORDERS if order["status"] == "delivered")
        delivered_revenue = sum(order["amount"] for order in ORDERS if order["status"] == "delivered")
        hurried_aov = revenue / delivered_orders
        print("AOV:", kit.rupees(hurried_aov), "(booked revenue / delivered orders)")
        print("The tree then multiplies to:", kit.rupees(orders * hurried_aov), "on", orders, "orders")
        """),
        md("""
        **Why it is wrong.** The answer is c. The numerator counts the 9 cancelled and returned orders'
        rupees while the denominator has dropped those orders, so every order looks Rs 7,783 larger
        than any booked order averages. Multiplied back through the tree it claims Rs 7,78,300 of
        revenue, 43 percent more than anyone booked, and marketing's payback case would value a new
        customer's order on it. The check is the tree's own identity: on one definition, orders times
        AOV must land on that definition's revenue.
        """),
        code("""
        rows = [("booked / booked", revenue, orders), ("delivered / delivered", delivered_revenue, delivered_orders),
                ("booked / delivered, the trap", revenue, delivered_orders)]
        kit.table(["numerator / denominator", "AOV", "orders x AOV", "lands on a real total?"],
                  [(n, kit.rupees(r / o), kit.rupees(o * (r / o)),
                    "yes" if (r, o) in [(revenue, orders), (delivered_revenue, delivered_orders)] else "no")
                   for n, r, o in rows], caption="The identity check on each fraction")
        kit.bars([("booked AOV", round(aov)), ("delivered AOV", round(delivered_revenue / delivered_orders)),
                  ("mixed, the trap", round(hurried_aov))], fmt=kit.rupees, lit=(2,),
                 title="Three AOVs; only the mixed one matches no definition")
        kit.check("the mixed AOV is Rs 25,943", round(hurried_aov) == 25943)
        kit.check("multiplied back on 30 orders, the mix claims revenue nobody booked",
                  round(orders * hurried_aov) != revenue, kit.rupees(orders * hurried_aov))
        """),
        md("""
        **The fix, and what changed.** One definition per fraction: booked AOV is Rs 18,160 on 30
        orders; delivered AOV is Rs 24,800 on 21 orders. The mixed Rs 25,943 goes nowhere. Each
        number goes out with its definition, and the tree multiplies back on each.

        ## A second route: AOV as the mean of the amounts

        Revenue over orders is the mean of the 30 amounts, so a list and a mean must give the same
        number. The two routes agree on every definition, and they are the same number: the mean is
        what the tree calls AOV.
        """),
        code("""
        amounts = [order["amount"] for order in ORDERS]
        mean_route = sum(amounts) / len(amounts)
        import statistics
        library_route = statistics.fmean(amounts)
        kit.table(["route", "booked AOV"],
                  [("revenue / orders", kit.rupees(aov)), ("sum of the list / its length", kit.rupees(mean_route)),
                   ("statistics.fmean(amounts)", kit.rupees(library_route))],
                  caption="Three routes to one AOV")
        kit.check("revenue / orders equals the mean of the amounts", abs(aov - mean_route) < 1e-9)
        kit.check("the library's mean agrees", abs(aov - library_route) < 1e-9)
        """),
        md("""
        **When to switch.** Revenue over orders is the route when the totals already exist in a
        report; the mean of the list is the route when you hold the rows. `statistics.fmean` saves a
        line and nothing else. The bigger switch is the one chapter 4 makes: when the question is
        "what is a typical order", the mean may be the wrong middle altogether.

        > **Kavya's review.** When two reports feed one fraction, ask each report what it counts before
        > you divide. The identity check costs one line and would have caught this before Meera saw it.

        ### In the interview

        **[S] How would you increase sales for an online retailer?** "I would draw the revenue tree
        before suggesting anything: customers, times orders per customer, times average order value,
        with order value split into items, price and discounts. Then I measure each branch on the same
        window and definition and ask which is short against plan, because each costs something
        different to move: acquisition costs marketing, frequency costs retention, basket costs
        merchandising, price risks volume. Initiatives come last, each placed on the branch it moves."

        **[F] A business says "grow revenue 15 percent"; how do you turn that into questions data can
        answer?** "Fifteen percent of which revenue, over which window, against which base. Then I break
        the target down the tree and ask what each branch would have to do alone, in customers, orders
        and rupees per order. Each is a fraction I can compute and each maps to a team that owns it."

        ### Depth: why the denominators cancel

        Customers x (orders / customers) x (revenue / orders) = revenue, because each denominator
        cancels the next numerator. That is also why a branch measured on another definition breaks
        the chain: its denominator no longer matches its neighbour's numerator.

        ## What this chapter established
        """),
        code("""
        kit.table(["What we now know", "The evidence"],
                  [("Each branch is a numerator over a denominator on one definition", "AOV = Rs 5,44,810 / 30 = Rs 18,160"),
                   ("Three branches are not in this file", "items, price and discounts"),
                   ("A fraction from two definitions matches nothing", "Rs 25,943 would claim Rs 7,78,300")],
                  caption="Chapter 2: the tree as metrics")
        kit.driver_tree({"label": "revenue", "note": "Rs 5,44,810 booked", "kind": "known", "children": [
            {"label": "customers", "note": "chapter 3", "kind": "lit"},
            {"label": "orders per customer", "note": "chapter 3", "kind": "lit"},
            {"label": "average order value", "note": "Rs 18,160; typical? chapter 4", "kind": "unknown"}]},
            title="Where the tree stands after chapter 2")
        kit.check_summary()
        print("Next: chapter 3 counts the two customer branches from the rows.")
        """),
    ]


# --------------------------------------------------------------------------------- chapter 3
def ch3():
    return [
        md("""
        # Chapter 3. The leaves, counted

        **Week 1, Monday. Chapter 3 of 6: how many customers, and how often do they buy?**

        **The need.** Marketing's Rs 12 crore buys customers. If the customers Kalpa already has never
        come back, acquisition really is the only branch; if they do come back, frequency is a branch
        Meera can grow without buying anyone new.

        | | |
        |---|---|
        | The metric at stake | Customers, and orders per customer, orders over distinct customers in the window |
        | Who asks | Meera, for the budget; the head of Retail-Plus and the marketing lead, who own the two branches |
        | What a wrong number costs | "Nobody comes back" makes frequency look dead and Rs 12 crore look like the only way to grow |
        | A real company with the same question | Reliance Retail reported 396 million registered customers at 30 June 2026 (Reliance Industries media release, 17 July 2026). A registered customer is a denominator of its own: divide a quarter's orders by it and you get a different, smaller metric than orders per customer who ordered. Which people you count is the whole question. |
        | In the dossier (`study-notes/C2_W01_D01_domain_retail_STUDENT.md`) | Section 5, frequency and repeat rate: the window decides the answer, and every registered customer is a different denominator |

        Chapter 2 built the tree and measured one branch: Rs 5,44,810 over 30 orders is an AOV of
        Rs 18,160. This chapter fills the two customer branches and checks the tree multiplies back.

        > **Kavya's review.** A customer is a person and an order is a row. Count people by their id,
        > and say how you did it.
        """),
        code(LOAD + '''
for order in ORDERS:
    order["amount"] = int(order["amount"])     # chapter 1's fix
revenue = sum(order["amount"] for order in ORDERS)
print(len(ORDERS), "orders,", kit.rupees(revenue), "booked")
'''),
        where(3, ["the options, sized", "the build: a dictionary of orders per customer",
                  "the leaves on delivered orders", "the trap: rows counted as customers",
                  "the second route: the mean of the counts"]),
        md("""
        ## The options

        Four ways to count customers, sized on 30 rows.

        | Option | Passes over the rows | What it answers | Error on this file |
        |---|---|---|---|
        | A. `len(ORDERS)`, the row count | none | how many orders | counts a repeat customer once per order |
        | B. `len(set(ids))`, distinct ids | one | how many customers | none; says nothing about who came back |
        | C. A dictionary of orders per id | one | how many customers, how many orders each, who came back | none |
        | D. Sort the ids and count where they change | a sort and a pass | how many customers | none if done right; easy to miscount by hand |

        **The best-fit call.** C: one pass fills both customer branches and names the repeat buyers,
        which is the number Meera's question turns on. B is the right call when only the count is
        needed. **What would change it:** at millions of rows the same count is one
        `COUNT(DISTINCT customer_id)` in the warehouse, which Week 2 teaches, and a loop in a notebook
        stops being the tool.
        """),
        code("""
        ids = [order["customer_id"] for order in ORDERS]
        options = [("A. rows", len(ORDERS)), ("B. distinct ids", len(set(ids))),
                   ("D. sorted, count changes", 1 + sum(1 for a, b in zip(sorted(ids), sorted(ids)[1:]) if a != b))]
        kit.bars(options, lit=(0,), title="Three of the options, run: how many customers?")
        kit.check("options B and D agree on distinct customers", options[1][1] == options[2][1], options[1][1])
        kit.check("option A counts more customers than there are people", options[0][1] > options[1][1])
        """),
        md("""
        ## 1. The build: a dictionary counts orders per customer

        A set says how many customers there are and forgets the rest. A dictionary keeps a count per
        id: the customer id is the key, the count of that customer's orders is the value.

        **Predict before you run.** Of the 23 customers, how many bought more than once?

        - a) None, because orders per customer is close to 1.
        - b) 7, the difference between 30 orders and 23 customers.
        - c) 16, the customers who are not new.
        - d) 23, because the rate is above 1.
        """),
        code("""
        counts = {}
        for order in ORDERS:
            cid = order["customer_id"]
            counts[cid] = counts.get(cid, 0) + 1
        customers = len(counts)
        per_customer = len(ORDERS) / customers
        once = sum(1 for c in counts.values() if c == 1)
        repeat = customers - once
        print(f"{customers} customers, {per_customer:.2f} orders each; {once} bought once, {repeat} came back")
        kit.columns(["bought once", "bought twice or more"], [("customers", [once, repeat])], lit=(1,),
                    width=520, title="23 customers by how many orders each placed")
        """),
        code("""
        kit.check("orders per customer is 1.30 on distinct customers", round(per_customer, 2) == 1.30)
        kit.check("16 bought once and 7 came back", (once, repeat) == (16, 7))
        kit.check("the counts add back to 30 orders", sum(counts.values()) == 30)
        """),
        md("""
        **What happened.** The answer is b. Here the difference between orders and customers equals
        the repeat buyers because nobody bought three times; a third order would part the two, which is
        why the dictionary is the count to trust. One repeat customer carries Retail-Core on one order
        and Retail-Plus on the other, since the segment is recorded on each order; a count of customers
        per segment has to say which order's segment it used.

        With every branch measured, the tree multiplies back:
        """),
        code("""
        aov = revenue / len(ORDERS)
        rebuilt = customers * per_customer * aov
        kit.driver_tree({"label": "revenue", "note": kit.rupees(revenue) + " booked", "kind": "known", "children": [
            {"label": "customers", "note": f"{customers} distinct ids", "kind": "known"},
            {"label": "orders per customer", "note": f"{per_customer:.2f}; {repeat} came back", "kind": "good"},
            {"label": "average order value", "note": kit.rupees(aov) + "; typical? chapter 4", "kind": "unknown"}]},
            title="The tree with chapter 3's leaves filled in")
        kit.check("customers x orders per customer x AOV = booked revenue", round(rebuilt) == revenue, kit.rupees(rebuilt))
        """),
        md("""
        ## 2. The leaves move when the definition moves

        Chapter 1 gave sales three readings, and every leaf inherits the choice. A customer whose only
        order was cancelled drops out of customers.

        **Predict before you run.** On the delivered definition, what happens to orders per customer?

        - a) It stays at 1.30, since both sides shrink.
        - b) It rises, because the loyal customers remain.
        - c) It cannot be computed without the returns.
        - d) It falls, because orders shrink faster than customers.
        """),
        code("""
        definitions = {"booked": {"delivered", "returned", "cancelled"},
                       "not cancelled": {"delivered", "returned"}, "delivered": {"delivered"}}
        leaves = {}
        for name, keep in definitions.items():
            per = {}
            rupees = 0
            for order in ORDERS:
                if order["status"] in keep:
                    per[order["customer_id"]] = per.get(order["customer_id"], 0) + 1
                    rupees += order["amount"]
            n = sum(per.values())
            leaves[name] = {"orders": n, "customers": len(per), "per": n / len(per),
                            "came back": sum(1 for c in per.values() if c > 1), "revenue": rupees}
        kit.table(["definition", "orders", "customers", "orders per customer", "came back", "revenue"],
                  [(k, v["orders"], v["customers"], f'{v["per"]:.2f}', v["came back"], kit.rupees(v["revenue"]))
                   for k, v in leaves.items()], caption="The leaves under each definition of sales")
        kit.columns(["orders", "customers", "came back"],
                    [(k, [leaves[k]["orders"], leaves[k]["customers"], leaves[k]["came back"]]) for k in leaves],
                    title="Orders fall faster than customers as the definition narrows")
        d = leaves["delivered"]
        kit.check("delivered: 21 orders from 19 customers, 1.11 each",
                  (d["orders"], d["customers"], round(d["per"], 2)) == (21, 19, 1.11))
        kit.check("only 2 customers came back with both orders delivered", d["came back"] == 2)
        """),
        md("""
        **What happened.** The answer is d. Removing 9 cancelled and returned orders removes only 4
        customers, and of the 7 who came back only 2 had both orders delivered. For Meera: customers
        do return, and their second orders are the ones most often cancelled or sent back, so
        frequency is a live branch that leaks.

        """),
        md("""
        ## 3. The trap: every row counted as a customer

        The first draft a colleague sent Meera counted this leaf in one line, from the row count.

        **Predict before you run.** The hurried cell divides orders by the number of rows. What
        orders-per-customer figure does it report?

        - a) 1.30, the figure the tree needs.
        - b) 0.77, because customers outnumber orders.
        - c) 1.00, one order for every customer.
        - d) 23.00, because the division runs the wrong way.

        **The plausible wrong answer.**
        """),
        code("""
        customers_hurried = len(ORDERS)
        per_customer_hurried = len(ORDERS) / customers_hurried
        print("Customers:", customers_hurried)
        print(f"Orders per customer: {per_customer_hurried:.2f}, so nobody comes back")
        kit.equation([f"orders per customer\\n{per_customer_hurried:.2f}", "=", "orders\\n30", "/",
                      "rows, read as customers\\n30"], title="The hurried division: rows stand in for people")
        """),
        md("""
        **Why it is wrong.** The answer is c. The division is correct and its denominator is wrong: a
        row is an order, and one customer can place several. Reported to Meera, "1.00 orders per
        customer, nobody comes back" says frequency is dead and the only way to grow is to buy
        customers, which is marketing's case for Rs 12 crore made by a counting slip. The check compares
        the ids in the list with the distinct ids.
        """),
        code("""
        distinct = set(ids)
        kit.bars([("rows (orders)", len(ids)), ("distinct customer ids", len(distinct))], lit=(1,),
                 title="The same column counted two ways")
        kit.check("the list holds one id per row", len(ids) == 30)
        kit.check("the set holds 23 distinct customers", len(distinct) == 23, len(distinct))
        """),
        md("""
        **The fix, and what changed.** Divide by distinct customers, as the build did: 23, and 30 / 23
        = 1.30 orders each. The draft's 1.00 goes nowhere, 7 customers are no longer invisible, and
        "nobody comes back" is gone from the case for the Rs 12 crore.

        ## A second route: the mean of the counts

        Orders per customer is also the mean of the dictionary's values: each customer's order count,
        averaged over customers. It must equal orders over distinct customers.
        """),
        code("""
        second_route = sum(counts.values()) / len(counts)
        kit.table(["route", "orders per customer"],
                  [("len(ORDERS) / len(set(ids))", f"{len(ORDERS) / len(distinct):.4f}"),
                   ("mean of the per-customer counts", f"{second_route:.4f}")],
                  caption="Two routes to one rate")
        kit.check("the two routes agree", abs(second_route - len(ORDERS) / len(distinct)) < 1e-12)
        kit.check("the dictionary's keys are the set's members", set(counts) == distinct)
        """),
        md("""
        **When to switch.** The ratio route needs only two counts, which is what a report holds; the
        counts route needs the rows and also gives the spread, 16 customers at one and 7 at two, which
        the ratio hides. Use the counts whenever someone will ask "how many came back".

        > **Kavya's review.** The division was fine; the denominator was a guess. Every rate you send upstairs carries the name
        > of its denominator, and a count of people comes from their ids.

        ### In the interview

        **[F] Your extract shows 30 orders and 30 customers; what do you check before saying nobody
        comes back?** "Whether 30 customers means 30 distinct ids or 30 rows. I compare the length of
        the id column with the length of its set; on Kalpa's quarter that is 30 against 23, so seven
        orders came from people who had already bought. I would also check the window, since a
        customer who buys every four months looks one-time in one quarter, and whether one person can
        carry two ids."

        **[SV] A list against a dictionary: when do you reach for each?** "A list when order matters or
        I will walk every item. A dictionary when I look things up or count by a key, such as orders per
        customer id. Real records are both: a list of dictionaries, one per row, which is what a JSON
        array from an API looks like. Checking membership in a list walks every item, while a dictionary
        goes straight to its key."

        **[SV] How do you count distinct customers in Python, and why does a set give the answer a list
        does not?** "`len(set(ids))`, because a set keeps each value once however often it is added,
        while a list keeps every occurrence. When I also need orders per customer, a dictionary keyed by
        id gives both."

        ### Depth: sets answer overlap questions

        `&` keeps the ids two sets share and `|` the ids in either. The cell asks how many customers
        used more than one channel.
        """),
        code("""
        by_channel = {"app": set(), "web": set(), "store": set()}
        for order in ORDERS:
            by_channel[order["channel"]].add(order["customer_id"])
        multi = sum(1 for cid in distinct if sum(cid in s for s in by_channel.values()) > 1)
        kit.table(["question", "set expression", "answer"],
                  [("customers on the app", "len(app)", len(by_channel["app"])),
                   ("customers on both app and web", "len(app & web)", len(by_channel["app"] & by_channel["web"])),
                   ("customers on any channel", "len(app | web | store)", len(by_channel["app"] | by_channel["web"] | by_channel["store"])),
                   ("customers on more than one channel", "counted", multi)],
                  caption="Set questions on the same 30 orders")
        kit.check("the union of the channels is all 23 customers",
                  len(by_channel["app"] | by_channel["web"] | by_channel["store"]) == 23)
        """),
        md("""
        All 7 repeat buyers came back through a different channel from their first. Seven customers
        are too few to call that a pattern; it does say a frequency plan built on one channel would miss
        how these customers return.

        ## What this chapter established
        """),
        code("""
        kit.table(["What we now know", "The evidence"],
                  [("A row is an order; customers are counted by id", "30 rows, 23 customers"),
                   ("Frequency is a live branch", "1.30 orders each; 7 of 23 came back"),
                   ("The tree multiplies back", "23 x 1.30 x Rs 18,160 = Rs 5,44,810"),
                   ("The definition moves every leaf", "delivered: 21 orders, 19 customers, 1.11")],
                  caption="Chapter 3: the leaves, counted")
        kit.check_summary()
        print("Next: chapter 4 asks whether Rs 18,160 describes a typical Kalpa order.")
        """),
    ]


# --------------------------------------------------------------------------------- chapter 4
def ch4():
    return [
        md("""
        # Chapter 4. The typical order

        **Week 1, Monday. Chapter 4 of 6: what does a typical Kalpa order look like, and which
        "typical" is honest?**

        **The need.** Marketing's case for Rs 12 crore values every new customer by the order they
        will place. Meera wants to know what that order is worth, and Anand has said how he will read
        the answer:

        > Meera: "What does a typical order look like?"
        > Anand: "No averages. One business customer can move an average."

        | | |
        |---|---|
        | The metric at stake | The typical order, the value per order that an acquisition payback is priced on |
        | Who asks | Meera and the marketing lead for the payback; Anand Iyer, who has already warned against averages |
        | What a wrong number costs | A first order valued eight times too high makes Rs 12 crore look cheap and the payback look short |
        | A real company with the same question | Blinkit reported a net average order value of Rs 518 for the quarter to June 2026 (MediaNama on Eternal's results, 24 July 2026). A reported AOV is a mean, the right number for totals across millions of orders; it is the wrong one to describe one shopper's basket when a few very large orders sit in the same file. |
        | In the dossier (`study-notes/C2_W01_D01_domain_retail_STUDENT.md`) | Section 5, average order value and basket size: the trap of an average across segments |

        Chapter 3 filled the customer branches: 23 customers, 1.30 orders each, 7 came back, and the
        tree multiplies back through an AOV of Rs 18,160. This chapter asks whether Rs 18,160
        describes an order anybody at Kalpa would recognise.

        > **Kavya's review.** When you tell Meera what a typical order is worth, tell her which middle
        > you used and why. If one order can move your number, it describes that order and not the
        > business.
        """),
        code(LOAD + '''
amounts = [int(order["amount"]) for order in ORDERS]
mean = sum(amounts) / len(amounts)
print(len(amounts), "amounts; the mean, chapter 2's AOV, is", kit.rupees(mean))
'''),
        where(4, ["the options, sized", "the build: sort, and take the middle",
                  "the median under each definition", "the trap: the mean sold as typical",
                  "the second route: statistics.median"]),
        md("""
        ## The options

        Four middles a team could report. The sizing column says how far each moves when one
        **invented** Rs 90,000 order joins five invented orders of Rs 1,900 to Rs 2,600, which is the
        test Anand set.

        | Option | Work on this file | Moves with one large order | Right call when |
        |---|---|---|---|
        | A. The mean, total over count | one sum | by every rupee of the large order | totals and forecasts must multiply back |
        | B. The median, the middle of the sorted amounts | a sort of 30 | by one place in the sort | the question is "what does a typical order look like" |
        | C. A trimmed mean, dropping the top and bottom order | a sort and a sum | little, if the rule trims enough | there is a stated rule for how many to drop |
        | D. A mean per customer type | a grouping | none within a type | the types are known and each gets its own plan |

        **The best-fit call.** B for the typical order, with A reported beside it for the total, since
        the gap between them is itself a finding. **What would change it:** if marketing prices the
        payback per customer type, D answers better; that grouping is the afternoon's second case.
        """),
        code("""
        invented = [1900, 2100, 2300, 2400, 2600]                  # invented orders, for the sizing only
        plus = sorted(invented + [90000])                          # one invented large order added
        def middle(xs):
            xs = sorted(xs); n = len(xs)
            return xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2
        def trimmed(xs):
            xs = sorted(xs)[1:-1]; return sum(xs) / len(xs)
        moves = [("A. mean", sum(plus) / 6 - sum(invented) / 5),
                 ("B. median", middle(plus) - middle(invented)),
                 ("C. trimmed mean", trimmed(plus) - trimmed(invented))]
        kit.bars([(n, round(m)) for n, m in moves], fmt=kit.rupees, lit=(0,),
                 title="Invented: how far each middle moves when one Rs 90,000 order joins five")
        kit.check("the invented median moves Rs 50", round(moves[1][1]) == 50)
        kit.check("the invented mean moves by more than Rs 14,000", moves[0][1] > 14000)
        """),
        md("""
        ## 1. The build: sort, and take the middle

        The median has half the orders below it and half above. With 30 orders there are two middle
        values, the 15th and 16th in size order, and the median is halfway between them.

        **Predict before you run.** What is the median order?

        - a) About Rs 2,200.
        - b) Rs 18,160.
        - c) Rs 9,080, half the mean.
        - d) Rs 4,80,000 / 30.
        """),
        code("""
        ranked = sorted(amounts)
        median = (ranked[14] + ranked[15]) / 2
        print("the two middle orders:", kit.rupees(ranked[14]), "and", kit.rupees(ranked[15]))
        print("median:", kit.rupees(median), "| mean:", kit.rupees(mean), f"| the mean is {mean / median:.1f} times the median")
        kit.bars([("mean, chapter 2's AOV", round(mean)), ("median, the middle order", round(median))],
                 fmt=kit.rupees, lit=(1,), title="Two middles of the same 30 orders")
        kit.check("the median is Rs 2,205", median == 2205)
        kit.check("the mean is about eight times the median", 8 <= mean / median <= 8.5, f"{mean / median:.2f}")
        """),
        md("""
        **What happened.** The answer is a: Rs 2,205, about one eighth of the mean. Two middles that far
        apart are a finding in themselves; the trap below is what happens when the wrong one is sent.

        ## 2. The median holds under every definition

        **Predict before you run.** On delivered orders only, the mean rises. What does the median do?

        - a) It rises by the same amount.
        - b) It doubles.
        - c) It becomes equal to the mean.
        - d) It moves by less than Rs 200.
        """),
        code("""
        definitions = {"booked": {"delivered", "returned", "cancelled"},
                       "not cancelled": {"delivered", "returned"}, "delivered": {"delivered"}}
        middles = {}
        for name, keep in definitions.items():
            kept = [int(o["amount"]) for o in ORDERS if o["status"] in keep]
            middles[name] = {"orders": len(kept), "mean": sum(kept) / len(kept), "median": middle(kept)}
        kit.table(["definition", "orders", "mean", "median"],
                  [(k, v["orders"], kit.rupees(round(v["mean"])), kit.rupees(v["median"])) for k, v in middles.items()],
                  caption="Both middles under each definition of sales")
        kit.columns(list(middles), [("mean", [round(v["mean"]) for v in middles.values()]),
                                    ("median", [v["median"] for v in middles.values()])],
                    fmt=kit.rupees, title="The mean swings with the definition; the median barely moves")
        spread = max(v["median"] for v in middles.values()) - min(v["median"] for v in middles.values())
        kit.check("the medians stay within Rs 200 of each other", spread < 200, kit.rupees(spread))
        kit.check("delivered median is Rs 2,060", middles["delivered"]["median"] == 2060)
        """),
        md("""
        **What happened.** The answer is d: Rs 2,205 booked, Rs 2,100 not cancelled, Rs 2,060
        delivered. The mean runs from Rs 18,160 to Rs 24,800 over the same three, because removing
        ordinary orders leaves the same large order carrying a bigger share of a smaller count.

        ## 3. The trap: the mean sold as the typical order

        Marketing's slide values each new customer's first order at the average order value.

        **Predict before you run.** How many of the 30 orders are larger than the mean of Rs 18,160?

        - a) About 15, half of them, since the mean is the middle.
        - b) One of them.
        - c) 29 of them, since the mean sits low.
        - d) None of them.

        **The plausible wrong answer.** The number as it appears on marketing's slide:
        """),
        code("""
        print("A typical Kalpa order:", kit.rupees(mean))
        print("What each new customer's first order is worth, per the model:", kit.rupees(mean))
        """),
        md("""
        **Why it is wrong.** A typical order is one most orders look like. If nearly every order sits
        below the mean, one order at the top is pulling the total, and the mean with it. Valued at
        Rs 18,160, a new customer looks about eight times more valuable than the orders Kalpa takes,
        and Rs 12 crore looks cheap. The check counts the orders on each side and draws every amount.
        """),
        code("""
        import math
        above = sum(1 for a in amounts if a > mean)
        print(above, "order above the mean,", len(amounts) - above, "below it")
        kit.strip([math.log10(a) for a in amounts], markers=[("mean", math.log10(mean), "bad")],
                  lo=2, hi=6, fmt=lambda v: kit.rupees(round(10 ** v)),
                  title="The 30 amounts on a scale where each step is ten times the one before")
        kit.check("exactly one order sits above the mean", above == 1)
        kit.check("29 of 30 orders sit below the mean", len(amounts) - above == 29)
        """),
        md("""
        **What happened.** The answer is b. The dots pile up below Rs 5,000 while the mean stands far to
        the right. The mean is correct arithmetic and a poor description of a Kalpa order.

        **Your turn.** Find what sits at the top of the sort. Type these lines into the empty cell and
        run it, then say in one sentence what kind of order the largest one must be:

        ```python
        print("largest three:", ranked[-3:])
        for order in ORDERS:
            if int(order["amount"]) == ranked[-1]:
                print(order)
        ```
        """),
        empty(),
        md("""
        The mechanism on a handful of **invented** numbers, which are not Kalpa orders: five invented
        orders between Rs 1,900 and Rs 2,600, then one invented Rs 90,000 order added.
        """),
        code("""
        kit.table(["invented records", "mean", "median"],
                  [("five invented orders", kit.rupees(sum(invented) / 5), kit.rupees(middle(invented))),
                   ("plus one invented Rs 90,000 order", kit.rupees(round(sum(plus) / 6)), kit.rupees(middle(plus)))],
                  caption="Invented numbers: what one large order does to each middle")
        kit.strip(plus, markers=[("median", middle(plus), "good"), ("mean", round(sum(plus) / 6), "bad")],
                  title="The six invented amounts, both middles marked")
        """),
        md("""
        **The fix, and what changed.** Report the build's median, Rs 2,205, as the typical order, with
        the mean beside it for totals and the top order on its own line. The first order in the payback
        falls from Rs 18,160 to Rs 2,205, about one eighth, so the Rs 12 crore has to earn back its cost
        over roughly eight times as many orders as the slide suggested.

        ## A second route: `statistics.median`

        The standard library has the rule built in, including the even-count case. It must agree with
        the hand-written middle on every definition.
        """),
        code("""
        import statistics
        rows = []
        for name, keep in definitions.items():
            kept = [int(o["amount"]) for o in ORDERS if o["status"] in keep]
            rows.append((name, kit.rupees(middles[name]["median"]), kit.rupees(statistics.median(kept))))
            kit.check(f"{name}: hand-written and library medians agree", statistics.median(kept) == middles[name]["median"])
        kit.table(["definition", "sort and take the middle", "statistics.median"], rows,
                  caption="Two routes to the median")
        """),
        md("""
        **When to switch.** Write the middle by hand once, so you know what the library does with an
        even count; after that `statistics.median` is the route, and in Week 2 it becomes
        `PERCENTILE_CONT(0.5)` in SQL and `.median()` in pandas. The switch that matters is between
        middles: the mean comes back whenever a total has to reconcile.

        > **Kavya's review.** Anand said "no averages" and you now know why. Put the median in the sentence, say the mean
        > is eight times higher, and say one order does it.

        ### In the interview

        **[S] Mean or median for order value, and why?** "The median when a few large orders can pull
        the mean, which in retail is almost always, since bulk buyers sit in the same file as
        households. I report both with the count of orders above the mean, because the gap is itself a
        finding: on Kalpa's quarter the mean was Rs 18,160, the median Rs 2,205, and 29 of 30 orders
        sat below the mean. The mean keeps its job for totals, since mean times count gives revenue."

        **[S] The mean order is Rs 18,160 and the median Rs 2,205; what do you tell the business about
        its orders?** "That a typical order is about Rs 2,205 and one or a few very large orders lift
        the mean to eight times that. I would sort, name what sits at the top, and ask whether it is a
        different kind of customer that needs its own line in the plan. Anything priced per order, an
        acquisition payback or a delivery cost, is priced on the median."

        **[D] Which middle would you put in a payback model, and what would make you change it?** "The
        median of the first orders of new customers, since that is the order the spend buys. I would
        switch to a mean per customer type if the plan targets types separately, because within a type
        the large orders no longer mix with the small."

        ### Depth: how far one order has to go

        The cell grows one **invented** order from Rs 2,600 to Rs 90,000 beside the same five invented
        orders.
        """),
        code("""
        sizes = [2600, 10000, 30000, 60000, 90000]                 # the invented large order, growing
        means = [round(sum(invented + [s]) / 6) for s in sizes]
        medians = [round(middle(invented + [s])) for s in sizes]
        kit.line([kit.rupees(s) for s in sizes], [("mean of six invented orders", means, "bad"),
                                                  ("median of six invented orders", medians, "good")],
                 fmt=kit.rupees, title="Invented: one order grows, and only the mean follows it")
        kit.check("the invented median never passes Rs 2,500", max(medians) <= 2500)
        """),
        md("""
        ## What this chapter established
        """),
        code("""
        kit.table(["What we now know", "The evidence"],
                  [("The mean is total over count, and one order drags it", "Rs 18,160, 29 of 30 orders below"),
                   ("The median is the typical order", "Rs 2,205, about one eighth of the mean"),
                   ("The median holds when the definition changes", "Rs 2,205 booked, Rs 2,060 delivered"),
                   ("A first order is worth about Rs 2,205 to the payback", "8.2 typical orders match one mean order")],
                  caption="Chapter 4: the typical order")
        kit.driver_tree({"label": "revenue", "note": "Rs 5,44,810 booked", "kind": "known", "children": [
            {"label": "customers", "note": "23, by id", "kind": "known"},
            {"label": "orders per customer", "note": "1.30; 16 of 23 bought once", "kind": "good"},
            {"label": "average order value", "note": "typical Rs 2,205, the median", "kind": "known"}]},
            title="The tree after the morning: every branch measured and named")
        kit.check_summary()
        print("Next: chapter 5 asks which branch Meera opens first.")
        """),
    ]


# --------------------------------------------------------------------------------- chapter 5
def ch5():
    return [
        md("""
        # Chapter 5. Which branch Meera opens first

        **Week 1, Monday. Chapter 5 of 6: is acquisition even the short branch, and which branch
        does the 15 percent plan ask least of?**

        **The need.** Meera has a tree with every branch measured. Marketing has proposed moving one
        branch, customers, for Rs 12 crore. Before she signs she wants to know which branch to open
        first, and why not the others.

        | | |
        |---|---|
        | The metric at stake | Revenue growth against the 15 percent plan, and what each branch alone would have to do to reach it |
        | Who asks | Meera; the marketing lead, who owns acquisition; the head of Retail-Plus, who owns the members most likely to come back |
        | What a wrong number costs | Rs 12 crore placed on the branch that was fine, and a plan sized by adding lifts that multiply |
        | A real company with the same question | Retailers pay to move frequency directly: Flipkart launched Flipkart Black at Rs 1,499 a year in 2025, evolving it from its VIP programme (Flipkart Stories, 12 September 2025), and Amazon offers Prime in India from Rs 399 to Rs 1,499 a year (About Amazon India). A membership is a bet on the frequency branch, placed by companies that could have spent the same money on acquisition. |
        | In the dossier (`study-notes/C2_W01_D01_domain_retail_STUDENT.md`) | Section 2, Retail-Plus, the paid tier, and section 5, customer acquisition cost and payback |

        Chapter 4 settled the typical order at Rs 2,205, the median. The tree now reads 23 customers,
        1.30 orders each, 16 of them bought once, and Rs 5,44,810 booked on 30 orders.

        > **Kavya's review.** Pick the branch the evidence points at and the one that costs least to
        > test. Then say what would make you pick another.
        """),
        code(LOAD + '''
for order in ORDERS:
    order["amount"] = int(order["amount"])
revenue = sum(o["amount"] for o in ORDERS)
counts = {}
for order in ORDERS:
    counts[order["customer_id"]] = counts.get(order["customer_id"], 0) + 1
customers, orders = len(counts), len(ORDERS)
per_customer, aov = orders / customers, revenue / orders
once = sum(1 for c in counts.values() if c == 1)
print(f"{customers} customers x {per_customer:.2f} orders x {kit.rupees(aov)} = {kit.rupees(customers * per_customer * aov)}")
'''),
        where(5, ["the options, sized: the plan from one branch", "the build: the branch on the tree",
                  "the trap: two 10 percent lifts called 20", "the second route: the lift, part by part"]),
        md("""
        ## The options

        The plan is 15 percent on booked revenue: Rs 81,722 more on this extract. Each branch could
        carry it alone, and each asks something different. The sizing cell computes what.

        **Predict before you run.** Which branch asks for the fewest new actions from customers?

        - a) Customers: about 3.45 more customers who buy like today's.
        - b) Price: every price up 15 percent with nobody leaving.
        - c) Order value: Rs 2,724 more on every order.
        - d) Frequency: about 4.5 more orders from the 23 customers already on file.
        """),
        code("""
        plan = revenue * 1.15
        need = {"customers": customers * 1.15, "orders": orders * 1.15, "aov": aov * 1.15}
        kit.table(["option: the branch moved alone", "this quarter", "the plan needs", "in plain words", "evidence in this file"],
                  [("A. acquisition, customers", customers, f"{need['customers']:.2f}",
                    f"{need['customers'] - customers:.2f} more customers who buy like today's", "none: one window cannot show customers falling"),
                   ("B. frequency, orders per customer", f"{per_customer:.2f}", f"{need['orders'] / customers:.2f}",
                    f"{need['orders'] - orders:.1f} more orders from the same {customers}, about 5 of the {once} one-time buyers returning once",
                    "7 of 23 already came back"),
                   ("C. order value", kit.rupees(aov), kit.rupees(need["aov"]),
                    f"{kit.rupees(need['aov'] - aov)} more per order, on an average one order drags", "items and prices are not in this file"),
                   ("D. price", "today's prices", "15 percent higher", "every price up with nobody leaving", "none; and nothing sells above MRP")],
                  caption=f"The 15 percent plan is {kit.rupees(plan)} of booked revenue")
        kit.columns(["customers", "orders"], [("this quarter", [customers, orders]),
                                              ("the plan, one branch alone", [need["customers"], need["orders"]])],
                    fmt=lambda v: f"{v:.2f}", title="What the plan needs from customers alone, or orders alone")
        kit.check("customers alone reach the plan through the tree",
                  abs(need["customers"] * per_customer * aov - plan) < 1)
        kit.check("orders alone reach the plan through the tree", abs(need["orders"] * aov - plan) < 1)
        """),
        md("""
        **What happened.** Both a and d are small asks in customers' actions; the difference is who
        is asked. Acquisition has to find 3.45 people Kalpa has never met; frequency asks 5 of the 16
        who already bought once to come back once, and 7 others already did. Price and order value
        rest on fields this file does not hold, or on an average one order drags.

        **The best-fit call.** B, frequency first: the customers exist, the file shows some of them
        return, and a retention test costs a reminder or an offer to people already on the list,
        where acquisition pays marketing to find new ones. **What would change it:** Tuesday's second
        quarter showing customers falling while frequency held, or a cost per retained order above the
        cost of acquiring a customer; either moves the call to A.

        ## 1. The build: the branch on the tree

        **Predict before you run.** How many of the 23 customers bought exactly once?

        - a) 7.
        - b) 23.
        - c) 16.
        - d) 0.
        """),
        code("""
        kit.driver_tree({"label": "booked revenue", "note": kit.rupees(revenue), "kind": "known", "children": [
            {"label": "customers", "note": f"{customers}; marketing's Rs 12 crore", "kind": "known"},
            {"label": "orders per customer", "note": f"{per_customer:.2f}; {once} of {customers} bought once", "kind": "lit"},
            {"label": "order value", "note": "median Rs 2,205", "kind": "known", "children": [
                {"label": "items per order", "note": "not in file", "kind": "unknown"},
                {"label": "price per item", "note": "not in file", "kind": "unknown"}]}]},
            title="Kalpa's tree, 1 July to 26 September: the branch to open first, lit")
        kit.bars([("bought once", once), ("came back", customers - once)], lit=(0,),
                 title="Customers by orders placed this quarter")
        kit.check("16 of 23 customers bought once", once == 16)
        kit.check("every customer is either once or came back", once + (customers - once) == 23)
        """),
        md("""
        **What happened.** The answer is c. Sixteen customers are one order away from moving the
        frequency branch, which is the branch Meera opens first.

        ## 2. The trap: two 10 percent lifts called 20 percent

        The marketing lead answers the frequency case with a bigger plan: "Fund acquisition and a
        retention programme together. A 10 percent lift in customers and a 10 percent lift in orders
        per customer make 20 percent growth, well over the 15 percent plan."

        **Predict before you run.** What do the two lifts really make?

        - a) 20 percent, as the slide says.
        - b) 21 percent.
        - c) 10 percent, since the lifts overlap.
        - d) 11 percent.

        **The plausible wrong answer.**
        """),
        code("""
        added = revenue * (1 + 0.10 + 0.10)
        print(f"Revenue after both lifts: {kit.rupees(added)}, growth 20 percent")
        """),
        md("""
        **Why it is wrong.** The branches multiply, so the lifts multiply: the second lift applies to a
        customer base that is already 10 percent larger. Adding them drops the lift on the lift, and at
        bigger or more numerous lifts the gap grows until a budget sized by addition misses its target.
        The check recomputes revenue leaf by leaf through the tree.
        """),
        code("""
        through_tree = (customers * 1.10) * (per_customer * 1.10) * aov
        print(f"through the tree: {kit.rupees(through_tree)}, growth {through_tree / revenue - 1:.0%}; "
              f"the slide's figure {kit.rupees(added)}, short by {kit.rupees(through_tree - added)}")
        lifts = [0.10, 0.20, 0.30]
        kit.columns([f"two {int(l * 100)}% lifts" for l in lifts],
                    [("added, the slide", [2 * l * 100 for l in lifts]),
                     ("multiplied, the tree", [((1 + l) ** 2 - 1) * 100 for l in lifts])],
                    fmt=lambda v: f"{v:.0f}%", title="Added against multiplied: the gap grows with the lift")
        kit.check("through the tree, two 10 percent lifts make 21 percent", round(through_tree / revenue - 1, 2) == 0.21)
        kit.check("the added figure is Rs 6,53,772", round(added) == 653772)
        kit.check("the tree's figure is Rs 6,59,220", round(through_tree) == 659220)
        """),
        md("""
        **The fix, and what changed.** The answer is b: Rs 6,59,220, 21 percent, Rs 5,448 above the
        slide. At 10 percent the gap is small; two 30 percent lifts make 69 percent where the slide
        would say 60. The same rule prices a discount: 15 percent off with 10 percent more orders is
        0.85 x 1.10 = 0.935, a 6.5 percent fall that addition would call a 5 percent fall.

        ## A second route: the lift, part by part

        Revenue after both lifts is the base, plus the customer lift, plus the frequency lift, plus the
        lift on the lift, 1 percent of the base. A bridge built from those four parts must land where
        the multiplication did.
        """),
        code("""
        parts = [("customers +10 percent", revenue * 0.10), ("orders per customer +10 percent", revenue * 0.10),
                 ("the lift on the lift, 0.10 x 0.10", revenue * 0.01)]
        kit.bridge(("booked, this quarter", revenue), [(n, round(v)) for n, v in parts],
                   end_label="after both lifts", lit=(2,), lo=500000,
                   title="The two lifts as parts (the axis starts at Rs 5,00,000)")
        kit.check("the parts land on the multiplied total", abs(revenue + sum(v for _, v in parts) - through_tree) < 1e-6)
        """),
        md("""
        **When to switch.** Multiply the factors when you need the total; build the parts when someone
        asks where the extra came from, since the bridge shows the lift on the lift as its own bar. The
        parts route is the one that wins the argument with the slide.

        > **Kavya's review.** Recompute through the tree anything someone adds up. Then tell Meera the
        > branch the evidence points at, frequency, and that the lifts multiply whichever she funds.

        ### In the interview

        **[D] Marketing wants budget for acquisition; what would you check before agreeing it is the
        right branch, and how would you say no?** "I would count customers by id and see how many came
        back, value a first order at the median rather than the mean, and ask for the quarter before
        this one to see whether customers actually fell. On Kalpa's quarter 16 of 23 bought once and 7
        came back, and the typical order is Rs 2,205 against a Rs 18,160 mean. The no is a no for now
        with a date: frequency is the cheaper branch to test, and if Tuesday's two quarters show
        customers fell, acquisition goes first."

        **[F] A 10 percent lift in customers and a 10 percent lift in frequency make 20 percent growth;
        what is the right number, and when does it matter?** "21 percent, because branches multiply:
        1.10 x 1.10 = 1.21. It matters when the lifts are large or many; two 30 percent lifts make 69,
        not 60, and a target sized by addition is missed by the difference."

        **[D] Which of four branches would you open first for a retailer, and what would make you
        switch?** "The one the evidence says is short and that costs least to test. Here frequency: the
        customers exist and a third already came back. I would switch to acquisition if a second window
        showed customers falling with frequency steady, or if retaining an order cost more than
        acquiring a customer."

        ### Depth: how far a discount has to lift orders to break even

        A 15 percent discount needs orders up 1 / 0.85 less one, about 17.6 percent, just to hold
        revenue, and more to hold margin.
        """),
        code("""
        lift_axis = [0, 5, 10, 15, 20, 25]
        kit.line([f"+{l}%" for l in lift_axis],
                 [("revenue before the discount", [100] * 6, "plan"),
                  ("revenue after 15 percent off", [round(85 * (1 + l / 100), 1) for l in lift_axis], "bad")],
                 fmt=lambda v: f"{v:g}", lo=80, title="Revenue index against the lift in orders, 15 percent discount")
        kit.check("the break-even lift is about 17.6 percent", round((1 / 0.85 - 1) * 100, 1) == 17.6)
        """),
        md("""
        ## What this chapter established
        """),
        code("""
        kit.table(["What we now know", "The evidence"],
                  [("The plan asks little of either customer branch", "3.45 more customers, or 4.5 more orders"),
                   ("Frequency is the branch to open first", f"{once} of {customers} bought once; 7 came back"),
                   ("Lifts multiply", "two 10 percent lifts make 21 percent, Rs 6,59,220")],
                  caption="Chapter 5: which branch first")
        kit.check_summary()
        print("Next: chapter 6 writes the sentence Meera can act on, and its caveat.")
        """),
    ]


# --------------------------------------------------------------------------------- chapter 6
def ch6():
    return [
        md("""
        # Chapter 6. The sentence Meera acts on

        **Week 1, Monday. Chapter 6 of 6: one sentence Meera can sign against, and what one quarter
        cannot tell her.**

        **The need.** Meera will not read five notebooks. She needs the answer, the evidence, and the
        limit of the evidence, in the time it takes to read one sentence, and marketing will read the
        same sentence looking for the weakest number in it.

        | | |
        |---|---|
        | The metric at stake | The repeat picture: who came back, who has not, and who has not had time to |
        | Who asks | Meera, who signs; Kavya, who reviews it first; the marketing lead, who will attack it |
        | What a wrong number costs | A sentence that says "70 percent of customers are lost" either panics the room or hands marketing an easy rebuttal, and the team loses the trust the week depends on |
        | A real company with the same question | Klarna reported that its AI assistant handled two-thirds of customer-service chats in its first month (Klarna, 27 February 2024); fifteen months later its chief executive said the focus on cost had lowered quality (Fortune, 9 May 2025). A first window's number read as the verdict is the risk this chapter's caveat guards against. |
        | In the dossier (`study-notes/C2_W01_D01_domain_retail_STUDENT.md`) | Section 5, retention and cohorts, and the returns rate's late window; section 8 tells Klarna's case in full |

        Chapter 5 chose frequency first: 16 of 23 customers bought once and 7 came back, and the
        lifts multiply. This chapter turns that into the sentence, and stress-tests the one number in
        it most likely to be misread.

        > **Kavya's review.** One sentence, four parts in this order: the evidence with its window, the
        > branch, what the window cannot show, and what happens to the Rs 12 crore.
        """),
        code(LOAD + '''
from datetime import date
for order in ORDERS:
    order["amount"] = int(order["amount"])
start = date.fromisoformat(min(o["order_date"] for o in ORDERS))
end = date.fromisoformat(max(o["order_date"] for o in ORDERS))
by_customer = {}
for order in ORDERS:
    by_customer.setdefault(order["customer_id"], []).append(date.fromisoformat(order["order_date"]))
customers = len(by_customer)
once_ids = [cid for cid, days in by_customer.items() if len(days) == 1]
print(f"{len(ORDERS)} orders from {start} to {end}, {(end - start).days + 1} days; {customers} customers, {len(once_ids)} bought once")
'''),
        where(6, ["the options, sized: four ways to answer Meera", "the build: the first draft",
                  "the trap: one-time buyers read as lost", "the second route: due dates"]),
        md("""
        ## The options

        Four ways to hand Meera the answer, sized in the reader's time and in what can go wrong.

        | Option | Her reading time | The decision it carries | How it gets misread |
        |---|---|---|---|
        | A. One number: "orders per customer, 1.30" | two seconds | none; she has to supply it | as good or bad news with no benchmark |
        | B. The tree as a table of every leaf | a minute or more | none; she draws the conclusion | she picks the number that suits the room |
        | C. One sentence: evidence, branch, caveat, the ask | about twenty seconds | open frequency, hold the budget until Tuesday | only if a number in it is misread, which the trap below tests |
        | D. A dashboard refreshed every week | weeks to build | whatever she looks at | a chart with no denominator |

        **The best-fit call.** C: it is the only option that carries a decision and its limit together.
        **What would change it:** when the question becomes weekly, as it does when Meera's chief of
        staff asks for the leadership deck in Week 2, D earns its build cost, with C as its headline.
        """),
        code("""
        reading = [("A. one number", 2), ("C. one sentence", 20), ("B. the tree as a table", 60)]
        kit.bars(reading, fmt=lambda v: f"{v} s", lit=(1,),
                 title="Seconds Meera spends reading each option (D is weeks to build before she reads it)")
        kit.check("the sentence is the one option that carries a decision inside half a minute",
                  [n for n, t in reading if t <= 30 and n.startswith("C")] == ["C. one sentence"])
        """),
        md("""
        ## 1. The build: the first draft of the sentence

        Every number in the sentence comes from a variable, so the sentence cannot drift from the work.
        The draft carries the evidence the chapters produced, in the four parts.

        **Predict before you run.** Which part does the sentence put last?

        - a) The evidence.
        - b) What happens to the Rs 12 crore.
        - c) The branch.
        - d) The caveat.
        """),
        code("""
        amounts = sorted(o["amount"] for o in ORDERS)
        median = (amounts[14] + amounts[15]) / 2
        per_customer = len(ORDERS) / customers
        came_back = customers - len(once_ids)
        draft = (f"On the {len(ORDERS)} booked orders from 1 July to 26 September, {customers} customers placed "
                 f"{per_customer:.2f} orders each at a typical order of {kit.rupees(median)}, and {len(once_ids)} of "
                 f"them bought only once, so I would open frequency before acquisition, and since one quarter cannot "
                 f"show which branch moved, hold the Rs 12 crore until Tuesday's two quarters.")
        print(draft)
        kit.flow(["the evidence, with its window", "the branch: frequency", "the caveat: one quarter",
                  "the ask: hold the budget"], kinds=["known", "lit", "unknown", "good"],
                 title="The sentence's four parts, in order")
        kit.check("the draft carries the customers, the rate and the typical order",
                  str(customers) in draft and f"{per_customer:.2f}" in draft and kit.rupees(median) in draft)
        kit.check("the draft ends on the budget", draft.rstrip(".").endswith("two quarters"))
        """),
        md("""
        **What happened.** The answer is b. The order is the review's order: evidence first so Meera can
        weigh it, the branch, the limit, and the ask she acts on. One number in the draft, the 16 who
        bought once, is the one marketing will reach for.

        ## 2. The trap: one-time buyers read as lost customers

        A colleague tightens the draft for the slide, and the 16 becomes a percentage.

        **Predict before you run.** 16 of the 23 customers bought only once in the quarter. What share
        of Kalpa's customers can you say are lost?

        - a) About 70 percent, 16 of 23.
        - b) 30 percent, the ones who came back.
        - c) None can be called lost from this file alone, and some are too recent to judge.
        - d) 100 percent of the one-time buyers.

        **The plausible wrong answer.**
        """),
        code("""
        lost_share = len(once_ids) / customers
        print(f"{len(once_ids)} of {customers} customers never came back: {lost_share:.0%} of customers are lost")
        """),
        md("""
        **Why it is wrong.** A customer who bought on 20 September had six days to come back before the
        extract ends. "Bought once in this window" is a fact; "lost" is a claim about the future the
        window cannot see. Sent to Meera, 70 percent churn makes retention look like an emergency on a
        number marketing can knock down in one question: "how long do our customers usually take to
        come back?" The check asks that question of the 7 who did.
        """),
        code("""
        gaps = sorted((max(d) - min(d)).days for d in by_customer.values() if len(d) > 1)
        typical_gap = gaps[len(gaps) // 2]
        too_recent = [cid for cid in once_ids if (end - by_customer[cid][0]).days < typical_gap]
        had_time = len(once_ids) - len(too_recent)
        kit.strip(gaps, markers=[("median gap", typical_gap, "bad")], lo=0, hi=90, fmt=lambda v: f"{v:g} days",
                  title="Days between a returning customer's first and second order")
        kit.bars([("came back", came_back), ("once, and had time", had_time),
                  ("once, too recent to judge", len(too_recent))], lit=(2,),
                 title="The 23 customers, with the window's edge taken into account")
        kit.check("the median gap between two orders is 45 days", typical_gap == 45, gaps)
        kit.check("9 of the 16 one-time buyers bought within the last 45 days", len(too_recent) == 9)
        kit.check("7 came back, 7 had time and did not, 9 are too recent",
                  (came_back, had_time, len(too_recent)) == (7, 7, 9))
        """),
        md("""
        **The fix, and what changed.** The answer is c. The seven who came back took a median of 45 days
        to do it, and 9 of the 16 one-time buyers placed their order inside the last 45 days of the
        window, so they have not had a typical customer's time to return. What the file supports is
        7 came back, 7 had time and have not, and 9 are too recent to judge: the "70 percent lost"
        becomes at most 7 of 23, and even that rests on a gap measured from 7 customers. The sentence
        replaces the 16 with the split.
        """),
        code("""
        sentence = (f"On the {len(ORDERS)} booked orders from 1 July to 26 September, {customers} customers placed "
                    f"{per_customer:.2f} orders each at a typical order of {kit.rupees(median)}; {came_back} came back, "
                    f"{had_time} have had time and not returned, and {len(too_recent)} bought too recently to judge, "
                    f"so I would open frequency before acquisition, and since one quarter cannot show which branch "
                    f"moved, hold the Rs 12 crore until Tuesday's two quarters.")
        print(sentence)
        print(len(sentence.split()), "words")
        kit.check("the sentence splits the one-time buyers", str(len(too_recent)) in sentence and str(had_time) in sentence)
        kit.check("the sentence names what one quarter cannot show", "cannot show" in sentence)
        kit.check("the sentence says nobody is lost", "lost" not in sentence)
        """),
        md("""
        ## A second route: due dates

        The same split comes from the other direction: give each one-time buyer a due date, their
        order date plus the typical gap, and count those whose due date falls after the window ends.
        The count must match the recency route.
        """),
        code("""
        from datetime import timedelta
        due_after_end = [cid for cid in once_ids if by_customer[cid][0] + timedelta(days=typical_gap) > end]
        kit.table(["route", "one-time buyers too recent to judge"],
                  [("days since the order, under the typical gap", len(too_recent)),
                   ("due date after the window ends", len(due_after_end))],
                  caption="Two routes to the same caveat")
        kit.check("both routes find the same customers", set(due_after_end) == set(too_recent))
        """),
        md("""
        **When to switch.** Recency is the route when you report today's state; due dates are the route
        when you plan follow-ups, since a due date is the day a reminder would go out. Both need the
        gap; with more quarters the gap would come from hundreds of customers instead of 7, and the
        caveat would shrink.

        > **Kavya's review.** This is a sentence I would take into the room. It says what we know, what we would do, and
        > what we would need before spending Rs 12 crore, and every number in it is one we can defend.

        ### In the interview

        **[D] You have one quarter of orders and 70 percent of customers bought once; what do you tell
        the CEO?** "That 70 percent bought once in this window, which is a fact, and that it is not a
        churn rate. Customers who came back took a median of 45 days, and 9 of the 16 one-time buyers
        bought within the last 45 days, so they have not had time. I would say 7 came back, 7 had time
        and did not, 9 are too recent, and ask for the prior quarter before calling anyone lost."

        **[F] How do you write a recommendation a stakeholder can act on?** "One sentence in four
        parts: the evidence with its window and definition, the recommendation, what the evidence
        cannot show, and the decision it asks for. Every number comes from the analysis, not retyped,
        and none can be recomputed into a different story by the person who disagrees."

        **[D] When would you replace this sentence with a dashboard?** "When the question recurs on a
        schedule and the definitions are settled, so the build cost is paid back every week. Until
        then a sentence with its caveat is faster and harder to misread."

        ### Depth: the window's edge in every metric

        Any count of "who has not done X yet" is cut short at the end of the window: returns that
        arrive late, renewals not yet due, a cohort one month old. The dossier's returns-rate trap is
        the same edge. The fix is always the same: measure how long X usually takes, and hold back
        judgement on everyone who has not had that long.

        ## What this chapter established
        """),
        code("""
        kit.table(["What we now know", "The evidence"],
                  [("One-time buyers are not lost customers", "median repeat gap 45 days; 9 of 16 too recent"),
                   ("The sentence has four parts in a fixed order", f"{len(sentence.split())} words, every number from a variable"),
                   ("The Rs 12 crore waits for a second quarter", "one window shows shape, two show movement")],
                  caption="Chapter 6: the sentence Meera acts on")
        kit.check_summary()
        print("Next: the escalated case asks the same question on the delivered definition, alone.")
        """),
    ]


# ------------------------------------------------------------------------ the escalated case
CASE_ANSWERS = {1: 'order["status"] == "delivered"', 2: "len(set(delivered_ids))",
                3: "len(delivered) / delivered_customers", 4: "amounts[n // 2]",
                5: "amount > mean_order", 6: "len(delivered) * 1.15", 7: "0.85 * 1.10",
                8: "days_since < typical_gap", 9: '"frequency"'}
CASE_KEY = "cbdcaabbc"


def case():
    return [
        md("""
        # The escalated case: Meera's question on what stayed sold

        **Week 1, Monday, afternoon. Alone, 35 minutes.** The six chapters answered Meera on booked
        orders. Anand Iyer has read the draft and pushes back: "Booked includes orders we cancelled and
        orders that came back. Do it again on what was delivered and stayed delivered, and tell me
        whether your answer survives." Same 30 orders, 1 July to 26 September 2026.

        > **Kavya's review.** A recommendation that only holds on one definition is a coincidence.
        > Rebuild it on delivered orders, say what moved and what held, and keep the caveat honest.
        """),
        md("""
        TODO ONLY
        Each step carries `TODO` markers. Above each `__TODOn__` placeholder is a lettered choice;
        replace the placeholder with the option you pick, run the cell, then run the check under it.
        Run from the top: the notebook stops at the first placeholder with a `NameError` naming it,
        which is intended.

        **What to post:** the nine letters in order as one string, the numbers each part's heading
        asks for, and your sentence to Meera.
        """),
        md("""
        SOLUTION ONLY
        Every placeholder is filled with the right option, and the notebook was executed from a fresh
        kernel. Under each part sits why the other options fail.

        **The answer string:** `cbdcaabbc`.
        """),
        code(LOAD + '''
from datetime import date
for order in ORDERS:
    order["amount"] = int(order["amount"])     # chapter 1's fix
end = date.fromisoformat(max(o["order_date"] for o in ORDERS))
print(len(ORDERS), "orders loaded; the extract ends on", end)
'''),
        code("""
        kit.side_by_side(
            kit.ladder(["The six chapters, booked", "The escalated case, delivered", "The second case, by channel"],
                       lit=1, show=False),
            kit.vflow(["1. the delivered leaves", "2. the typical delivered order", "3. the plan and the discount",
                       "4. the branch, with the window's edge", "5. the sentence to Meera"], show=False),
        )
        """),
        md("""
        ## Part 1. The leaves on what stayed delivered

        **Post:** delivered orders, delivered customers and delivered orders per customer.
        """),
        code("""
        # TODO 1. Which condition keeps the orders that reached a customer and stayed there?
        #   a) order["status"] != "cancelled"
        #   b) order["status"] in ("delivered", "returned")
        #   c) order["status"] == "delivered"
        #   d) order["amount"] > 0
        delivered, delivered_ids, delivered_revenue = [], [], 0
        for order in ORDERS:
            if __TODO1__:
                delivered.append(order)
                delivered_ids.append(order["customer_id"])
                delivered_revenue += order["amount"]

        # TODO 2. Which expression counts the distinct customers behind the delivered orders?
        #   a) len(delivered_ids)
        #   b) len(set(delivered_ids))
        #   c) len(set(o["customer_id"] for o in ORDERS))
        #   d) len(delivered)
        delivered_customers = __TODO2__

        # TODO 3. Which expression is orders per customer on the delivered definition?
        #   a) delivered_customers / len(delivered)
        #   b) len(ORDERS) / delivered_customers
        #   c) len(delivered) / 23
        #   d) len(delivered) / delivered_customers
        delivered_per_customer = __TODO3__
        kit.table(["leaf", "booked (the chapters)", "delivered"],
                  [("orders", 30, len(delivered)), ("customers", 23, delivered_customers),
                   ("orders per customer", "1.30", f"{delivered_per_customer:.2f}"),
                   ("revenue", "Rs 5,44,810", kit.rupees(delivered_revenue))],
                  caption="The same file on two definitions")
        kit.columns(["orders", "customers"], [("booked", [30, 23]), ("delivered", [len(delivered), delivered_customers])],
                    title="The definition moves every leaf")
        """),
        code("""
        kit.check("21 orders were delivered", len(delivered) == 21, len(delivered))
        kit.check("delivered customers are fewer than delivered orders", delivered_customers < len(delivered))
        kit.check("delivered orders per customer sits above one", delivered_per_customer > 1)
        """),
        md("""
        SOLUTION ONLY
        **Why not the others.** TODO 1: a keeps returns, which did not stay sold; b keeps them on
        purpose, a different definition; d keeps everything. TODO 2: a counts rows; c counts booked
        customers, mixing two definitions in one leaf; d counts orders. TODO 3: a is upside down; b
        puts booked orders over delivered customers; c divides by the booked customer count.
        **The numbers.** 21 orders, 19 customers, 1.11 each, Rs 5,20,790.
        """),
        md("""
        ## Part 2. The typical delivered order

        21 is an odd count, so the median is one value, not the average of two.

        **Post:** the delivered mean, the delivered median, and the orders above the mean.
        """),
        code("""
        amounts = sorted(o["amount"] for o in delivered)
        n = len(amounts)
        mean_order = sum(amounts) / n
        # TODO 4. n is 21, an odd count. Which expression is the median?
        #   a) (amounts[n // 2 - 1] + amounts[n // 2]) / 2
        #   b) amounts[n // 2 + 1]
        #   c) amounts[n // 2]
        #   d) sum(amounts) / n
        median_order = __TODO4__
        # TODO 5. Which test counts an order as sitting above the mean?
        #   a) amount > mean_order
        #   b) amount > median_order
        #   c) amount >= 0
        #   d) amount < mean_order
        above = 0
        for amount in amounts:
            if __TODO5__:
                above += 1
        kit.stats([(kit.rupees(round(mean_order)), "delivered mean", "every delivered amount / 21"),
                   (kit.rupees(median_order), "delivered median", "the 11th of 21 in size order"),
                   (f"{above} of {n}", "above the mean", "the rest sit below")])
        kit.strip(amounts, markers=[("mean", mean_order, "bad"), ("median", median_order, "good")],
                  title="The 21 delivered amounts, with both middles")
        """),
        code("""
        kit.check("the median is one of the delivered amounts", median_order in amounts)
        kit.check("the delivered mean sits more than ten times above the median", mean_order > 10 * median_order)
        kit.check("almost every delivered order sits below the mean", n - above >= 20)
        """),
        md("""
        SOLUTION ONLY
        **Why not the others.** TODO 4: a is the even-count rule, which here averages the 10th and 11th;
        b is one place past the middle; d is the mean. TODO 5: b counts orders above the median, about
        half by construction; c counts everything; d counts the other side.
        **The numbers.** Mean Rs 24,800, median Rs 2,060, 1 of 21 above the mean. The mean rose by
        Rs 6,640 from the booked Rs 18,160 and the median fell Rs 145, so the typical order held.
        """),
        md("""
        ## Part 3. The plan, and the discount marketing will propose

        **Post:** the delivered orders the plan needs from frequency alone, and what a 15 percent
        discount that lifts orders 10 percent does to delivered revenue.
        """),
        code("""
        plan = delivered_revenue * 1.15
        # TODO 6. If only frequency moves, how many delivered orders must the same customers place?
        #   a) len(delivered) * 1.15
        #   b) len(delivered) + 15
        #   c) len(delivered) + 0.15
        #   d) delivered_customers * 1.15
        needed_orders = __TODO6__
        # TODO 7. A 15 percent discount lifts orders 10 percent. What multiplies delivered revenue?
        #   a) 1 - 0.15 + 0.10
        #   b) 0.85 * 1.10
        #   c) 1.15 * 1.10
        #   d) (1 - 0.15) * (1 - 0.10)
        discount_factor = __TODO7__
        after_discount = delivered_revenue * discount_factor
        kit.table(["question", "answer"],
                  [("the plan on delivered revenue", kit.rupees(plan)),
                   ("delivered orders the plan needs from frequency alone", f"{needed_orders:.2f}, {needed_orders - len(delivered):.2f} more"),
                   ("delivered revenue after the discount", f"{kit.rupees(after_discount)}, {discount_factor - 1:+.1%}")],
                  caption="The plan and the discount on what stayed delivered")
        kit.bridge(("delivered, this quarter", delivered_revenue),
                   [("price 15 percent lower", -round(delivered_revenue * 0.15)),
                    ("orders +10 percent at the lower price", round(delivered_revenue * 0.85 * 0.10))],
                   end_label="after the discount", lit=(0,), lo=350000,
                   title="The discount through the tree (the axis starts at Rs 3,50,000)")
        """),
        code("""
        kit.check("frequency alone reaches the plan", abs(needed_orders * (delivered_revenue / len(delivered)) - plan) < 1)
        kit.check("the discount lowers delivered revenue", after_discount < delivered_revenue)
        """),
        md("""
        SOLUTION ONLY
        **Why not the others.** TODO 6: d is the customer answer; b adds 15 orders, a 71 percent lift;
        c adds 0.15 of an order. TODO 7: a adds the moves and calls a fall a rise; c raises the price; d
        cuts orders instead of lifting them.
        **The numbers.** The plan is Rs 5,98,909; frequency alone needs 24.15 delivered orders, 3.15
        more; the discount takes delivered revenue to Rs 4,86,939, a 6.5 percent fall.
        """),
        md("""
        ## Part 4. The branch, with the window's edge

        Count the one-time buyers on delivered orders, then hold back the ones too recent to judge,
        using chapter 6's typical gap of 45 days.

        **Post:** delivered customers who bought once, how many of them are too recent, and the branch.
        """),
        code("""
        firsts = {}
        for order in delivered:
            firsts.setdefault(order["customer_id"], []).append(date.fromisoformat(order["order_date"]))
        once = [cid for cid, days in firsts.items() if len(days) == 1]
        typical_gap = 45                                   # chapter 6, from the booked repeat buyers
        # TODO 8. Which test flags a one-time buyer as too recent to judge?
        #   a) days_since > typical_gap
        #   b) days_since < typical_gap
        #   c) days_since == 0
        #   d) typical_gap < 45
        too_recent = 0
        for cid in once:
            days_since = (end - firsts[cid][0]).days
            if __TODO8__:
                too_recent += 1
        # TODO 9. On delivered orders, which branch does Meera open first?
        #   a) "customers"
        #   b) "price"
        #   c) "frequency"
        #   d) "order value"
        first_branch = __TODO9__
        kit.bars([("kept two orders", delivered_customers - len(once)), ("once, had time", len(once) - too_recent),
                  ("once, too recent", too_recent)], lit=(2,), title="Delivered customers, with the window's edge")
        print("open first:", first_branch)
        """),
        code("""
        kit.check("every delivered customer is counted once", len(firsts) == delivered_customers)
        kit.check("some one-time buyers are too recent to judge", 0 < too_recent < len(once))
        kit.check("the branch is the one the one-time buyers point to", first_branch == "frequency")
        """),
        md("""
        SOLUTION ONLY
        **Why not the others.** TODO 8: a flags the ones who had time; c catches only a same-day order;
        d compares the gap with itself. TODO 9: a is marketing's branch, which one window cannot show
        falling; b and d rest on fields this file lacks and on a mean one order drags.
        **The numbers.** 17 of 19 delivered customers kept one order, 7 of them too recent to judge;
        only 2 kept two orders. Frequency stays first, and the delivered view adds a leak: customers
        come back, and their second orders are the ones cancelled or returned.
        """),
        md("""
        ## Part 5. The sentence to Meera

        Write one sentence in chapter 6's four parts, on delivered orders, and say what held from the
        booked answer. Post it as text.
        """),
        md("""
        SOLUTION ONLY
        One sentence that holds: "On the 21 delivered orders from 1 July to 26 September, 19 customers
        kept 1.11 orders each at a typical Rs 2,060, and 17 kept only one, 7 of them too recent to
        judge, so frequency is still the branch to open first, with the second order's returns and
        cancellations as the leak to fix; one quarter cannot show which branch moved, so hold the
        Rs 12 crore until Tuesday's two quarters."
        """),
        code("""
        kit.table(["part", "booked (the chapters)", "delivered (this case)", "held?"],
                  [("orders per customer", "1.30", f"{delivered_per_customer:.2f}", "fell"),
                   ("typical order", "Rs 2,205", kit.rupees(median_order), "held"),
                   ("one-time buyers", "16 of 23, 9 too recent", f"{len(once)} of {delivered_customers}, {too_recent} too recent", "held"),
                   ("branch", "frequency", first_branch, "held")],
                  caption="What moved and what held")
        kit.check_summary()
        """),
    ]


# ------------------------------------------------------------------------ the second case
# Carried from the 29 September pack, relabelled to the chapter grid.
def second_todo():
    return [
        md('# The second case: where revenue comes from\n\n**Week 1, Monday, afternoon. The second case, in pairs, 25 minutes.** The six chapters and the escalated case said\nfrequency first. This notebook answers the other half of Meera\'s question on the same 30 orders,\n1 July to 26 September 2026, and tests whether the channel view changes that recommendation.\n\nMeera Raghavan, CEO of Kalpa Retail: "Where does revenue come from, by customer type and channel? Is\nacquisition even the branch that is short?" Anand Iyer, the finance controller: "No averages. One\nbusiness customer can move an average."\n\n> **Kavya\'s review.** "Meera will open the channel slide before she reads your sentence, and the first\n> thing on it will be store at nine rupees in ten. Decide whether that number changes your answer\n> before she asks, and count the orders behind every share you show her."\n\nEach step carries a `TODO` marker. Above each `__TODOn__` placeholder is a lettered choice; replace the placeholder with the option you pick, run the cell, then run the check under it. Run from the top: the notebook stops at the first placeholder with a `NameError` naming it, which is intended.\n\n**What to post, one post per pair:** the seven letters in order as one string, the numbers the step headings ask for, and your answer to Meera\'s channel question.'),
        md('The setup cell reaches the shared helper and loads the 30 orders, converting the amount stored as\ntext with `int()` as chapter 1 did.'),
        code('import sys, pathlib\nhere = pathlib.Path.cwd()\nfor parent in [here, *here.parents]:\n    if (parent / "scripts" / "c2kit.py").exists():\n        sys.path.insert(0, str(parent / "scripts")); break\nimport c2kit as kit\n\nORDERS = kit.load_records()\nfor order in ORDERS:\n    order["amount"] = int(order["amount"])\nprint(len(ORDERS), "orders loaded, every amount now a whole number")\nbooked_revenue = 0\nfor order in ORDERS:\n    booked_revenue += order["amount"]\nprint("booked revenue summed for the shares below")'),
        code('kit.side_by_side(\n    kit.ladder(["The six chapters, booked", "The escalated case, delivered", "The second case, by channel"],\n               lit=2, show=False),\n    kit.vflow(["1. revenue by channel", "2. the orders behind each share",\n               "3. consumer orders only", "4. each channel by status",\n               "5. revenue by customer type", "6. does the recommendation change"], show=False),\n)'),
        md("## Step 1. Revenue by channel\n\nAdd each order's amount to its channel's total, then work out store's share of booked revenue.\n\n**Post:** each channel's share of booked revenue, and store's in particular."),
        code('channel_revenue = {}\nchannel_orders = {}\nfor order in ORDERS:\n    ch = order["channel"]\n    # TODO 1. Which line adds this order\'s amount to its channel\'s total?\n    #   a) channel_revenue[ch] = order["amount"]\n    #   b) channel_revenue[ch] = channel_revenue.get(ch, 0) + 1\n    #   c) channel_revenue[ch] = channel_revenue.get(ch, 0) + order["amount"]\n    #   d) channel_revenue[ch] = channel_revenue.get(ch, order["amount"]) + order["amount"]\n    __TODO1__\n    channel_orders[ch] = channel_orders.get(ch, 0) + 1\n\n# TODO 2. Which expression is store\'s share of booked revenue?\n#   a) channel_revenue["store"] / len(ORDERS)\n#   b) channel_revenue["store"] / booked_revenue\n#   c) channel_orders["store"] / len(ORDERS)\n#   d) channel_revenue["store"] / channel_revenue["app"]\nstore_share = __TODO2__\n\nchannels = ["app", "web", "store"]\nkit.table(["Channel", "Orders", "Share of booked revenue"],\n          [(ch, channel_orders[ch], f"{channel_revenue[ch] / booked_revenue * 100:.1f}%")\n           for ch in channels],\n          caption="Share of booked revenue by channel, all 30 orders")\nkit.bars([(ch, round(channel_revenue[ch] / booked_revenue * 1000) / 10) for ch in channels],\n         fmt=lambda v: f"{v:.1f}%", lit=(2,), title="Share of booked revenue by channel, percent")'),
        code('kit.check("the channels reconcile to booked revenue", sum(channel_revenue.values()) == booked_revenue)\nkit.check("each channel carries the same number of orders",\n          len(set(channel_orders.values())) == 1, str(channel_orders))\nkit.check("store\'s share is a fraction of booked revenue", 0 < store_share < 1,\n          f"{store_share * 100:.1f} percent")'),
        md("## Step 2. The orders behind each share\n\nCount each channel's orders by status, and count the orders in each channel that sit above the booked\nmean of Rs 18,160.\n\n**Post:** each channel's delivered, returned and cancelled counts, and the orders above the mean."),
        code('status_count = {"app": {}, "web": {}, "store": {}}\nfor order in ORDERS:\n    ch = order["channel"]\n    st = order["status"]\n    # TODO 3. Which line counts this order under its channel and its status?\n    #   a) status_count[ch] = status_count.get(ch, 0) + 1\n    #   b) status_count[st][ch] = status_count[st].get(ch, 0) + 1\n    #   c) status_count[ch][st] = status_count[ch].get(st, 0) + order["amount"]\n    #   d) status_count[ch][st] = status_count[ch].get(st, 0) + 1\n    __TODO3__\n\nmean_order = booked_revenue / len(ORDERS)\nabove_mean = {"app": 0, "web": 0, "store": 0}\nfor order in ORDERS:\n    if order["amount"] > mean_order:\n        above_mean[order["channel"]] += 1\n\nstatuses = ["delivered", "returned", "cancelled"]\nkit.table(["Channel", "Delivered", "Returned", "Cancelled", "Orders above the mean"],\n          [(ch, *[status_count[ch].get(st, 0) for st in statuses], above_mean[ch]) for ch in channels],\n          caption="Orders, not rupees, behind each channel\'s share")\nkit.columns(channels, [(st, [status_count[ch].get(st, 0) for ch in channels]) for st in statuses],\n            title="Each channel\'s 10 orders by status", fmt=lambda v: f"{v:.0f}")'),
        code('kit.check("the status counts add back to 30 orders",\n          sum(sum(c.values()) for c in status_count.values()) == len(ORDERS))\nkit.check("store\'s share rests on a single order above the mean", above_mean["store"] == 1,\n          f"{above_mean[\'store\']} order")\nkit.check("every returned order came through one channel",\n          sum(1 for ch in channels if status_count[ch].get("returned", 0) > 0) == 1)'),
        md("## Step 3. The fix: consumer orders only\n\nMeera's growth plan is about the customers who buy again and again, so recompute the channel view on\nthe consumer orders, the 29 outside the Business segment.\n\n**Post:** consumer booked revenue, and each channel's consumer revenue and share."),
        code('# TODO 4. Which condition keeps the consumer orders, the 29 outside the Business segment?\n#   a) order["segment"] != "Business"\n#   b) order["segment"] == "Retail-Core"\n#   c) order["channel"] != "store"\n#   d) order["status"] != "cancelled"\nconsumer = []\nfor order in ORDERS:\n    if __TODO4__:\n        consumer.append(order)\n\nconsumer_revenue = 0\nconsumer_channel_rev = {"app": 0, "web": 0, "store": 0}\nconsumer_channel_orders = {"app": 0, "web": 0, "store": 0}\nfor order in consumer:\n    consumer_revenue += order["amount"]\n    consumer_channel_rev[order["channel"]] += order["amount"]\n    consumer_channel_orders[order["channel"]] += 1\n\nkit.table(["Channel", "Consumer orders", "Consumer revenue", "Share of consumer"],\n          [(ch, consumer_channel_orders[ch], kit.rupees(consumer_channel_rev[ch]),\n            f"{consumer_channel_rev[ch] / consumer_revenue * 100:.1f}%") for ch in channels],\n          caption=f"{len(consumer)} consumer orders, {kit.rupees(consumer_revenue)} booked")\nkit.columns(channels, [("share of all booked revenue",\n                        [channel_revenue[ch] / booked_revenue * 100 for ch in channels]),\n                       ("share of consumer revenue",\n                        [consumer_channel_rev[ch] / consumer_revenue * 100 for ch in channels])],\n            title="Store\'s share before and after the fix, in percent", fmt=lambda v: f"{v:.1f}")'),
        code('kit.check("29 consumer orders remain", len(consumer) == 29, f"got {len(consumer)}")\nkit.check("the consumer channels reconcile to consumer revenue",\n          sum(consumer_channel_rev.values()) == consumer_revenue, kit.rupees(consumer_revenue))\nkit.check("on consumer orders store no longer leads",\n          consumer_channel_rev["store"] < max(consumer_channel_rev.values()))'),
        md("## Step 4. Each channel by status, in rupees\n\nBooked is what customers asked for; delivered is what stayed sold. Split each channel's consumer\nrevenue by status and find where it leaks.\n\n**Post:** web's returned revenue, store's cancelled revenue, and consumer delivered revenue."),
        code('consumer_status_rev = {"app": {}, "web": {}, "store": {}}\nfor order in consumer:\n    ch = order["channel"]\n    st = order["status"]\n    consumer_status_rev[ch][st] = consumer_status_rev[ch].get(st, 0) + order["amount"]\n\n# TODO 5. Which number is web\'s leak, the booked revenue that came back?\n#   a) consumer_status_rev["web"].get("delivered", 0)\n#   b) consumer_status_rev["web"].get("returned", 0)\n#   c) consumer_status_rev["store"].get("returned", 0)\n#   d) consumer_channel_rev["web"] - consumer_status_rev["web"].get("returned", 0)\nweb_leak = __TODO5__\nstore_leak = consumer_status_rev["store"].get("cancelled", 0)\nconsumer_delivered = 0\nfor ch in channels:\n    consumer_delivered += consumer_status_rev[ch].get("delivered", 0)\n\nkit.table(["Channel", "Delivered", "Returned", "Cancelled"],\n          [(ch, *[kit.rupees(consumer_status_rev[ch].get(st, 0)) for st in statuses])\n           for ch in channels], caption="Consumer revenue by channel and status")\nkit.columns(channels, [("booked", [consumer_channel_rev[ch] for ch in channels]),\n                       ("delivered", [consumer_status_rev[ch].get("delivered", 0) for ch in channels])],\n            title="Consumer revenue by channel, booked against delivered", fmt=kit.rupees)\nkit.bridge(("consumer booked", consumer_revenue),\n           [("web returns", -web_leak), ("store cancellations", -store_leak)],\n           end_label="consumer delivered", lit=(0, 1),\n           title="Where consumer revenue leaks between booked and delivered")'),
        code('kit.check("booked less the two leaks lands on delivered",\n          consumer_revenue - web_leak - store_leak == consumer_delivered, kit.rupees(consumer_delivered))\nkit.check("app delivered every rupee it booked",\n          consumer_status_rev["app"].get("delivered", 0) == consumer_channel_rev["app"])\nkit.check("web lost more than a third of its booked revenue to returns",\n          web_leak > consumer_channel_rev["web"] / 3, kit.rupees(web_leak))'),
        md("## Step 5. Revenue by customer type\n\nMeera also asked about customer type. Segment is recorded on each order, so this step stays at\norders and revenue by segment: one repeat customer appears once as Retail-Core and once as Retail-Plus,\nand a count of customers per segment would count that customer twice. The Business segment is one\norder, so its row carries the count and the rupee view stays on the three consumer segments.\n\n**Post:** each consumer segment's orders, revenue and share of consumer revenue."),
        code('segment_orders = {}\nfor order in ORDERS:\n    segment_orders[order["segment"]] = segment_orders.get(order["segment"], 0) + 1\n\nsegment_rev = {}\nsegment_delivered = {}\nfor order in consumer:\n    seg = order["segment"]\n    segment_rev[seg] = segment_rev.get(seg, 0) + order["amount"]\n    if order["status"] == "delivered":\n        segment_delivered[seg] = segment_delivered.get(seg, 0) + order["amount"]\n\n# TODO 6. Which total is the denominator for a segment\'s share of consumer revenue?\n#   a) booked_revenue\n#   b) len(consumer)\n#   c) consumer_revenue\n#   d) segment_rev["Retail-Core"]\ndenominator = __TODO6__\n\nsegments = ["Retail-Core", "Retail-Plus", "Student"]\nrows = [(seg, segment_orders[seg], kit.rupees(segment_rev[seg]),\n         f"{segment_rev[seg] / denominator * 100:.1f}%",\n         kit.rupees(round(segment_rev[seg] / segment_orders[seg]))) for seg in segments]\nrows.append(("Business", segment_orders["Business"], "outside the consumer view",\n             "outside the consumer view", "outside the consumer view"))\nkit.table(["Customer type", "Orders", "Booked revenue", "Share of consumer", "Revenue per order"],\n          rows, caption="Revenue by customer type, recorded on each order")\nkit.columns(segments, [("booked", [segment_rev[seg] for seg in segments]),\n                       ("delivered", [segment_delivered[seg] for seg in segments])],\n            title="Consumer revenue by customer type, booked against delivered", fmt=kit.rupees)'),
        code('kit.check("the four segments account for all 30 orders", sum(segment_orders.values()) == len(ORDERS))\nkit.check("the consumer segments reconcile to consumer revenue",\n          sum(segment_rev.values()) == consumer_revenue, kit.rupees(sum(segment_rev.values())))\nkit.check("the shares of consumer revenue add to one",\n          abs(sum(segment_rev[s] / denominator for s in segments) - 1) < 1e-9)'),
        md('## Step 6. Does one channel change the recommendation?\n\nThe escalated case said open frequency first. Weigh that against what the channel view found.'),
        code('# TODO 7. What does the channel view do to the recommendation?\n#   a) "frequency first, two leaks named"\n#   b) "store-led, since store brings 91.6 percent"\n#   c) "web-led"\n#   d) "acquisition first"\nverdict = __TODO7__\nprint("the recommendation:", verdict)\nkit.flow(["store 91.6 percent of booked", "one order behind it", "consumer view: store 29.2 percent",\n          "web returns, store cancellations", "frequency first stands"],\n         kinds=["bad", "unknown", "known", "known", "lit"],\n         title="From the trap to the recommendation")'),
        code('kit.check("the recommendation keeps the branch and names the leaks", verdict.startswith("frequency"),\n          verdict)'),
        md("### In the interview\n\nAnswer each aloud in the drill, with this notebook's numbers, then compare with the solution.\n\n- **[D]** One channel carries nine rupees in ten of revenue; does that change where the growth plan\n  invests?\n- **[F]** A business says 'grow revenue 15 percent'; how do you turn that into questions data can\n  answer?"),
        md('## What the second case established\n\nSix steps, and the recommendation survives the channel view with two leaks added to the note.'),
        code('kit.table(["Step", "What it established"], [\n    ("1. by channel", f"store carries {store_share * 100:.1f} percent of booked revenue"),\n    ("2. orders behind it", f"{above_mean[\'store\']} store order sits above the mean; "\n                            f"store cancelled {status_count[\'store\'].get(\'cancelled\', 0)}"),\n    ("3. consumer only", f"store holds {kit.rupees(consumer_channel_rev[\'store\'])} of "\n                         f"{kit.rupees(consumer_revenue)}"),\n    ("4. by status", f"web returned {kit.rupees(web_leak)}; store cancelled {kit.rupees(store_leak)}; "\n                     f"app delivered {status_count[\'app\'].get(\'delivered\', 0)} of 10"),\n    ("5. by customer type", f"Retail-Core {kit.rupees(segment_rev[\'Retail-Core\'])}, Retail-Plus "\n                            f"{kit.rupees(segment_rev[\'Retail-Plus\'])}, Student "\n                            f"{kit.rupees(segment_rev[\'Student\'])}"),\n    ("6. the recommendation", verdict),\n])\nkit.bars([(ch, consumer_status_rev[ch].get("delivered", 0)) for ch in channels], fmt=kit.rupees,\n         title="What stayed sold: consumer delivered revenue by channel")'),
        code('kit.check_summary()\nprint("Next: Tuesday puts the quarter before this one beside it, to see which branch moved.")'),
    ]


def second_sol():
    return [
        md('# The second case: where revenue comes from, solution\n\n**Week 1, Monday, afternoon. The second case, in pairs, 25 minutes.** The six chapters and the escalated case said\nfrequency first. This notebook answers the other half of Meera\'s question on the same 30 orders,\n1 July to 26 September 2026, and tests whether the channel view changes that recommendation.\n\nMeera Raghavan, CEO of Kalpa Retail: "Where does revenue come from, by customer type and channel? Is\nacquisition even the branch that is short?" Anand Iyer, the finance controller: "No averages. One\nbusiness customer can move an average."\n\n> **Kavya\'s review.** "Meera will open the channel slide before she reads your sentence, and the first\n> thing on it will be store at nine rupees in ten. Decide whether that number changes your answer\n> before she asks, and count the orders behind every share you show her."\n\nEvery placeholder is filled with the right option, and the notebook was executed from a fresh kernel. Under each step sits the reason the other three options fail, and step 1 stages the plausible wrong answer with its exact number.\n\n**The answer string:** `cbdabca`.'),
        md('The setup cell reaches the shared helper and loads the 30 orders, converting the amount stored as\ntext with `int()` as chapter 1 did.'),
        code('import sys, pathlib\nhere = pathlib.Path.cwd()\nfor parent in [here, *here.parents]:\n    if (parent / "scripts" / "c2kit.py").exists():\n        sys.path.insert(0, str(parent / "scripts")); break\nimport c2kit as kit\n\nORDERS = kit.load_records()\nfor order in ORDERS:\n    order["amount"] = int(order["amount"])\nprint(len(ORDERS), "orders loaded, every amount now a whole number")\nbooked_revenue = 0\nfor order in ORDERS:\n    booked_revenue += order["amount"]\nprint("booked revenue summed for the shares below")'),
        code('kit.side_by_side(\n    kit.ladder(["The six chapters, booked", "The escalated case, delivered", "The second case, by channel"],\n               lit=2, show=False),\n    kit.vflow(["1. revenue by channel", "2. the orders behind each share",\n               "3. consumer orders only", "4. each channel by status",\n               "5. revenue by customer type", "6. does the recommendation change"], show=False),\n)'),
        md("## Step 1. Revenue by channel\n\nAdd each order's amount to its channel's total, then work out store's share of booked revenue.\n\n**Post:** each channel's share of booked revenue, and store's in particular."),
        code('channel_revenue = {}\nchannel_orders = {}\nfor order in ORDERS:\n    ch = order["channel"]\n    # TODO 1. Which line adds this order\'s amount to its channel\'s total?\n    #   a) channel_revenue[ch] = order["amount"]\n    #   b) channel_revenue[ch] = channel_revenue.get(ch, 0) + 1\n    #   c) channel_revenue[ch] = channel_revenue.get(ch, 0) + order["amount"]\n    #   d) channel_revenue[ch] = channel_revenue.get(ch, order["amount"]) + order["amount"]\n    channel_revenue[ch] = channel_revenue.get(ch, 0) + order["amount"]\n    channel_orders[ch] = channel_orders.get(ch, 0) + 1\n\n# TODO 2. Which expression is store\'s share of booked revenue?\n#   a) channel_revenue["store"] / len(ORDERS)\n#   b) channel_revenue["store"] / booked_revenue\n#   c) channel_orders["store"] / len(ORDERS)\n#   d) channel_revenue["store"] / channel_revenue["app"]\nstore_share = channel_revenue["store"] / booked_revenue\n\nchannels = ["app", "web", "store"]\nkit.table(["Channel", "Orders", "Share of booked revenue"],\n          [(ch, channel_orders[ch], f"{channel_revenue[ch] / booked_revenue * 100:.1f}%")\n           for ch in channels],\n          caption="Share of booked revenue by channel, all 30 orders")\nkit.bars([(ch, round(channel_revenue[ch] / booked_revenue * 1000) / 10) for ch in channels],\n         fmt=lambda v: f"{v:.1f}%", lit=(2,), title="Share of booked revenue by channel, percent")'),
        code('kit.check("the channels reconcile to booked revenue", sum(channel_revenue.values()) == booked_revenue)\nkit.check("each channel carries the same number of orders",\n          len(set(channel_orders.values())) == 1, str(channel_orders))\nkit.check("store\'s share is a fraction of booked revenue", 0 < store_share < 1,\n          f"{store_share * 100:.1f} percent")'),
        md('**Why not the others.** In TODO 1, option a overwrites the total with the latest order; b counts\norders instead of adding rupees; d starts each channel at its first amount and then adds it again, so\nevery channel\'s first order counts twice. In TODO 2, option a is revenue per order in the store; c is\nstore\'s share of orders, one third; d compares store with app, a ratio with no whole behind it.\n\n**The plausible wrong answer.** "Store brings 91.6 percent of revenue, so the growth plan should be\nstore-led."\n\n**Why it is wrong.** Every channel has 10 orders, yet store\'s share is nine rupees in ten. A share\nthat large from a third of the orders means a few orders carry it, and Anand has already said one\nbusiness customer can move an average; a share is an average in disguise.\n\n**The check that catches it.** Count the orders behind each share and split them by status, which is\nstep 2.'),
        md("## Step 2. The orders behind each share\n\nCount each channel's orders by status, and count the orders in each channel that sit above the booked\nmean of Rs 18,160.\n\n**Post:** each channel's delivered, returned and cancelled counts, and the orders above the mean."),
        code('status_count = {"app": {}, "web": {}, "store": {}}\nfor order in ORDERS:\n    ch = order["channel"]\n    st = order["status"]\n    # TODO 3. Which line counts this order under its channel and its status?\n    #   a) status_count[ch] = status_count.get(ch, 0) + 1\n    #   b) status_count[st][ch] = status_count[st].get(ch, 0) + 1\n    #   c) status_count[ch][st] = status_count[ch].get(st, 0) + order["amount"]\n    #   d) status_count[ch][st] = status_count[ch].get(st, 0) + 1\n    status_count[ch][st] = status_count[ch].get(st, 0) + 1\n\nmean_order = booked_revenue / len(ORDERS)\nabove_mean = {"app": 0, "web": 0, "store": 0}\nfor order in ORDERS:\n    if order["amount"] > mean_order:\n        above_mean[order["channel"]] += 1\n\nstatuses = ["delivered", "returned", "cancelled"]\nkit.table(["Channel", "Delivered", "Returned", "Cancelled", "Orders above the mean"],\n          [(ch, *[status_count[ch].get(st, 0) for st in statuses], above_mean[ch]) for ch in channels],\n          caption="Orders, not rupees, behind each channel\'s share")\nkit.columns(channels, [(st, [status_count[ch].get(st, 0) for ch in channels]) for st in statuses],\n            title="Each channel\'s 10 orders by status", fmt=lambda v: f"{v:.0f}")'),
        code('kit.check("the status counts add back to 30 orders",\n          sum(sum(c.values()) for c in status_count.values()) == len(ORDERS))\nkit.check("store\'s share rests on a single order above the mean", above_mean["store"] == 1,\n          f"{above_mean[\'store\']} order")\nkit.check("every returned order came through one channel",\n          sum(1 for ch in channels if status_count[ch].get("returned", 0) > 0) == 1)'),
        md('**Why not the others.** Option a counts orders per channel and loses the status; b indexes the\ndictionary by status first, and `status_count["delivered"]` does not exist, so it raises a\n`KeyError`; c adds rupees where the step asks for counts.\n\n**What it shows.** App\'s 10 orders were all delivered. Web delivered 5 and saw 5 returned. Store\ndelivered 6 and had 4 cancelled, and exactly one store order sits above the booked mean: the order\nyour chapter 4 sort put at the top, which belongs to the one Business customer. Store\'s nine rupees in\nten is one order\'s share.'),
        md("## Step 3. The fix: consumer orders only\n\nMeera's growth plan is about the customers who buy again and again, so recompute the channel view on\nthe consumer orders, the 29 outside the Business segment.\n\n**Post:** consumer booked revenue, and each channel's consumer revenue and share."),
        code('# TODO 4. Which condition keeps the consumer orders, the 29 outside the Business segment?\n#   a) order["segment"] != "Business"\n#   b) order["segment"] == "Retail-Core"\n#   c) order["channel"] != "store"\n#   d) order["status"] != "cancelled"\nconsumer = []\nfor order in ORDERS:\n    if order["segment"] != "Business":\n        consumer.append(order)\n\nconsumer_revenue = 0\nconsumer_channel_rev = {"app": 0, "web": 0, "store": 0}\nconsumer_channel_orders = {"app": 0, "web": 0, "store": 0}\nfor order in consumer:\n    consumer_revenue += order["amount"]\n    consumer_channel_rev[order["channel"]] += order["amount"]\n    consumer_channel_orders[order["channel"]] += 1\n\nkit.table(["Channel", "Consumer orders", "Consumer revenue", "Share of consumer"],\n          [(ch, consumer_channel_orders[ch], kit.rupees(consumer_channel_rev[ch]),\n            f"{consumer_channel_rev[ch] / consumer_revenue * 100:.1f}%") for ch in channels],\n          caption=f"{len(consumer)} consumer orders, {kit.rupees(consumer_revenue)} booked")\nkit.columns(channels, [("share of all booked revenue",\n                        [channel_revenue[ch] / booked_revenue * 100 for ch in channels]),\n                       ("share of consumer revenue",\n                        [consumer_channel_rev[ch] / consumer_revenue * 100 for ch in channels])],\n            title="Store\'s share before and after the fix, in percent", fmt=lambda v: f"{v:.1f}")'),
        code('kit.check("29 consumer orders remain", len(consumer) == 29, f"got {len(consumer)}")\nkit.check("the consumer channels reconcile to consumer revenue",\n          sum(consumer_channel_rev.values()) == consumer_revenue, kit.rupees(consumer_revenue))\nkit.check("on consumer orders store no longer leads",\n          consumer_channel_rev["store"] < max(consumer_channel_rev.values()))'),
        md('**Why not the others.** Option b keeps one consumer segment and drops the other two; c drops every\nstore order, including the nine consumer ones; d applies a status definition, which answers a\ndifferent question and still keeps the Business order.\n\n**The fix, and what changed.** On the 29 consumer orders, Rs 64,810 booked, web leads with Rs 27,290\n(42.1 percent), store has Rs 18,920 (29.2 percent) and app Rs 18,600 (28.7 percent). The channel that\nlooked like nine rupees in ten is under a third of consumer revenue.'),
        md("## Step 4. Each channel by status, in rupees\n\nBooked is what customers asked for; delivered is what stayed sold. Split each channel's consumer\nrevenue by status and find where it leaks.\n\n**Post:** web's returned revenue, store's cancelled revenue, and consumer delivered revenue."),
        code('consumer_status_rev = {"app": {}, "web": {}, "store": {}}\nfor order in consumer:\n    ch = order["channel"]\n    st = order["status"]\n    consumer_status_rev[ch][st] = consumer_status_rev[ch].get(st, 0) + order["amount"]\n\n# TODO 5. Which number is web\'s leak, the booked revenue that came back?\n#   a) consumer_status_rev["web"].get("delivered", 0)\n#   b) consumer_status_rev["web"].get("returned", 0)\n#   c) consumer_status_rev["store"].get("returned", 0)\n#   d) consumer_channel_rev["web"] - consumer_status_rev["web"].get("returned", 0)\nweb_leak = consumer_status_rev["web"].get("returned", 0)\nstore_leak = consumer_status_rev["store"].get("cancelled", 0)\nconsumer_delivered = 0\nfor ch in channels:\n    consumer_delivered += consumer_status_rev[ch].get("delivered", 0)\n\nkit.table(["Channel", "Delivered", "Returned", "Cancelled"],\n          [(ch, *[kit.rupees(consumer_status_rev[ch].get(st, 0)) for st in statuses])\n           for ch in channels], caption="Consumer revenue by channel and status")\nkit.columns(channels, [("booked", [consumer_channel_rev[ch] for ch in channels]),\n                       ("delivered", [consumer_status_rev[ch].get("delivered", 0) for ch in channels])],\n            title="Consumer revenue by channel, booked against delivered", fmt=kit.rupees)\nkit.bridge(("consumer booked", consumer_revenue),\n           [("web returns", -web_leak), ("store cancellations", -store_leak)],\n           end_label="consumer delivered", lit=(0, 1),\n           title="Where consumer revenue leaks between booked and delivered")'),
        code('kit.check("booked less the two leaks lands on delivered",\n          consumer_revenue - web_leak - store_leak == consumer_delivered, kit.rupees(consumer_delivered))\nkit.check("app delivered every rupee it booked",\n          consumer_status_rev["app"].get("delivered", 0) == consumer_channel_rev["app"])\nkit.check("web lost more than a third of its booked revenue to returns",\n          web_leak > consumer_channel_rev["web"] / 3, kit.rupees(web_leak))'),
        md("**Why not the others.** Option a is what web kept; c looks for returns in store, which has none; d is\nweb's booked revenue less its returns, which is again what web kept.\n\n**What it shows.** Web booked Rs 27,290 and half its orders came back, Rs 14,970 returned, leaving\nRs 12,320 delivered. Store's consumer orders booked Rs 18,920, and 4 of its 9 were cancelled for\nRs 9,050, leaving Rs 9,870 delivered. App booked Rs 18,600 and delivered all of it, 10 of 10. Consumer\ndelivered revenue is Rs 40,790."),
        md("## Step 5. Revenue by customer type\n\nMeera also asked about customer type. Segment is recorded on each order, so this step stays at\norders and revenue by segment: one repeat customer appears once as Retail-Core and once as Retail-Plus,\nand a count of customers per segment would count that customer twice. The Business segment is one\norder, so its row carries the count and the rupee view stays on the three consumer segments.\n\n**Post:** each consumer segment's orders, revenue and share of consumer revenue."),
        code('segment_orders = {}\nfor order in ORDERS:\n    segment_orders[order["segment"]] = segment_orders.get(order["segment"], 0) + 1\n\nsegment_rev = {}\nsegment_delivered = {}\nfor order in consumer:\n    seg = order["segment"]\n    segment_rev[seg] = segment_rev.get(seg, 0) + order["amount"]\n    if order["status"] == "delivered":\n        segment_delivered[seg] = segment_delivered.get(seg, 0) + order["amount"]\n\n# TODO 6. Which total is the denominator for a segment\'s share of consumer revenue?\n#   a) booked_revenue\n#   b) len(consumer)\n#   c) consumer_revenue\n#   d) segment_rev["Retail-Core"]\ndenominator = consumer_revenue\n\nsegments = ["Retail-Core", "Retail-Plus", "Student"]\nrows = [(seg, segment_orders[seg], kit.rupees(segment_rev[seg]),\n         f"{segment_rev[seg] / denominator * 100:.1f}%",\n         kit.rupees(round(segment_rev[seg] / segment_orders[seg]))) for seg in segments]\nrows.append(("Business", segment_orders["Business"], "outside the consumer view",\n             "outside the consumer view", "outside the consumer view"))\nkit.table(["Customer type", "Orders", "Booked revenue", "Share of consumer", "Revenue per order"],\n          rows, caption="Revenue by customer type, recorded on each order")\nkit.columns(segments, [("booked", [segment_rev[seg] for seg in segments]),\n                       ("delivered", [segment_delivered[seg] for seg in segments])],\n            title="Consumer revenue by customer type, booked against delivered", fmt=kit.rupees)'),
        code('kit.check("the four segments account for all 30 orders", sum(segment_orders.values()) == len(ORDERS))\nkit.check("the consumer segments reconcile to consumer revenue",\n          sum(segment_rev.values()) == consumer_revenue, kit.rupees(sum(segment_rev.values())))\nkit.check("the shares of consumer revenue add to one",\n          abs(sum(segment_rev[s] / denominator for s in segments) - 1) < 1e-9)'),
        md('**Why not the others.** Option a divides by a total that includes the Business order, so the three\nconsumer shares add to about 12 percent; b divides rupees by orders, which is revenue per order; d\nindexes every segment to Retail-Core, so Retail-Core reads 100 percent.\n\n**What it shows.** Retail-Core placed 14 orders for Rs 32,650 (50.4 percent of consumer revenue),\nRetail-Plus 10 for Rs 27,320 (42.2 percent) and Student 5 for Rs 4,840 (7.5 percent); Business is\n1 order. Retail-Plus, the paid tier, has the highest revenue per order at Rs 2,732, and 3 of its 10\norders came back, which is a question for the head of Retail-Plus on Tuesday.'),
        md('## Step 6. Does one channel change the recommendation?\n\nThe escalated case said open frequency first. Weigh that against what the channel view found.'),
        code('# TODO 7. What does the channel view do to the recommendation?\n#   a) "frequency first, two leaks named"\n#   b) "store-led, since store brings 91.6 percent"\n#   c) "web-led"\n#   d) "acquisition first"\nverdict = "frequency first, two leaks named"\nprint("the recommendation:", verdict)\nkit.flow(["store 91.6 percent of booked", "one order behind it", "consumer view: store 29.2 percent",\n          "web returns, store cancellations", "frequency first stands"],\n         kinds=["bad", "unknown", "known", "known", "lit"],\n         title="From the trap to the recommendation")'),
        code('kit.check("the recommendation keeps the branch and names the leaks", verdict.startswith("frequency"),\n          verdict)'),
        md('**Why not the others.** Option b is the trap, a share that one order carries; c reads web\'s booked\nlead and ignores that half its orders came back; d moves to the branch the file gave no reason to\nopen first.\n\n**The conclusion.** The branch recommendation stands: open frequency first. The channel view adds two\nleaks for the note: web returns, 5 of 10 orders and Rs 14,970, and store cancellations, 4 orders and\nRs 9,050. App is the clean channel, 10 of 10 delivered.\n\n> **Kavya\'s review.** "Good: you counted the orders behind the share before you believed it. The\n> channel slide now carries two leaks with their numbers, and your sentence to Meera does not change."'),
        md("### In the interview\n\n**[D] One channel carries nine rupees in ten of revenue; does that change where the growth plan\ninvests?** Not before I count the orders behind the share. At Kalpa, store's 91.6 percent rests on one\nBusiness order; on the 29 consumer orders store holds Rs 18,920 of Rs 64,810, 29.2 percent, and 4 of\nits 9 consumer orders were cancelled. So the plan still invests on the branch the tree points to,\nfrequency, and the channel view adds the leaks to fix: web returns and store cancellations.\n\n**[F] A business says 'grow revenue 15 percent'; how do you turn that into questions data can\nanswer?** I turn it into counts and ratios. Which revenue, booked, net of cancellations or delivered?\nOver which two windows? Which branch is short: customers, orders per customer or revenue per order?\nWhat does 15 percent need from one branch alone, which on Kalpa's quarter is about 3.45 more customers,\nor 4.5 more orders from the same 23 customers, or Rs 2,724 more per order? And which customer types\nand channels carry the revenue, and where does it leak before delivery?"),
        md('## What the second case established\n\nSix steps, and the recommendation survives the channel view with two leaks added to the note.'),
        code('kit.table(["Step", "What it established"], [\n    ("1. by channel", f"store carries {store_share * 100:.1f} percent of booked revenue"),\n    ("2. orders behind it", f"{above_mean[\'store\']} store order sits above the mean; "\n                            f"store cancelled {status_count[\'store\'].get(\'cancelled\', 0)}"),\n    ("3. consumer only", f"store holds {kit.rupees(consumer_channel_rev[\'store\'])} of "\n                         f"{kit.rupees(consumer_revenue)}"),\n    ("4. by status", f"web returned {kit.rupees(web_leak)}; store cancelled {kit.rupees(store_leak)}; "\n                     f"app delivered {status_count[\'app\'].get(\'delivered\', 0)} of 10"),\n    ("5. by customer type", f"Retail-Core {kit.rupees(segment_rev[\'Retail-Core\'])}, Retail-Plus "\n                            f"{kit.rupees(segment_rev[\'Retail-Plus\'])}, Student "\n                            f"{kit.rupees(segment_rev[\'Student\'])}"),\n    ("6. the recommendation", verdict),\n])\nkit.bars([(ch, consumer_status_rev[ch].get("delivered", 0)) for ch in channels], fmt=kit.rupees,\n         title="What stayed sold: consumer delivered revenue by channel")'),
        code('kit.check_summary()\nprint("Next: Tuesday puts the quarter before this one beside it, to see which branch moved.")'),
    ]


def split_md(cells):
    """One markdown cell per heading, and the options, the call and the result each in their own cell."""
    out = []
    for cell in cells:
        if cell.cell_type != "markdown":
            out.append(cell)
            continue
        parts, current = [], []
        for line in cell.source.split("\n"):
            starts = line.startswith(("## ", "### ", "**The best-fit call.**", "**What happened.**",
                                      "**Why it is wrong.**", "**When to switch.**", "**The plausible wrong answer.**"))
            if starts and any(l.strip() for l in current):
                parts.append("\n".join(current).strip("\n"))
                current = []
            current.append(line)
        parts.append("\n".join(current).strip("\n"))
        out += [md(p) for p in parts if p.strip()]
    return out


TEACHING = {
    "story": ("C2_W01_D01_00_retail_story_STUDENT.ipynb", story),
    "ch1": ("C2_W01_D01_01_four_readings_of_sales_STUDENT.ipynb", ch1),
    "ch2": ("C2_W01_D01_02_the_tree_as_metrics_STUDENT.ipynb", ch2),
    "ch3": ("C2_W01_D01_03_the_leaves_counted_STUDENT.ipynb", ch3),
    "ch4": ("C2_W01_D01_04_the_typical_order_STUDENT.ipynb", ch4),
    "ch5": ("C2_W01_D01_05_which_branch_first_STUDENT.ipynb", ch5),
    "ch6": ("C2_W01_D01_06_the_sentence_STUDENT.ipynb", ch6),
}


def main(names):
    for name, (fname, cells) in TEACHING.items():
        if not names or name in names:
            nb = build(NB / fname, split_md(cells()))
            print(f"built {fname}: {len(nb.cells)} cells")
    if not names or "case" in names:
        twin(NB / "C2_W01_D01_ex1_escalated_case_STUDENT.ipynb",
             SOL / "C2_W01_D01_ex1_escalated_case_solution_STUDENT.ipynb", case(), CASE_ANSWERS)
        print("built the escalated case twin and solution")
    if not names or "second" in names:
        build(NB / "C2_W01_D01_ex2_second_case_STUDENT.ipynb", second_todo(), execute=False)
        build(SOL / "C2_W01_D01_ex2_second_case_solution_STUDENT.ipynb", second_sol())
        print("built the second case twin and solution")


if __name__ == "__main__":
    main(sys.argv[1:])
