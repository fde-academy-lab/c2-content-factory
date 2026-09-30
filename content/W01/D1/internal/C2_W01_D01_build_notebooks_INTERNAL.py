"""Build Monday's notebooks: the retail story, six chapters, the escalated case and the second case.

Run from the repository root:
    python3 content/W01/D1/internal/C2_W01_D01_build_notebooks_INTERNAL.py            every notebook
    python3 content/W01/D1/internal/C2_W01_D01_build_notebooks_INTERNAL.py ch3 case   named ones only

Names: story, ch1 to ch6, case (the escalated case twin and solution), second (the second case twin
and solution). Each teaching notebook is executed cold in its own folder by scripts/nb_make.py, so
the saved outputs are the ones a learner sees on GitHub. The TODO twins are written unexecuted and
their solution twins executed, both from one list of cells.

Every heading is a question and the cells under it answer it, which is the question ladder of
.claude/skills/day-pack-builder/references/the-standard.md. No cell prints a planted record: a
discovery sits in an empty your-turn cell, a mechanism that needs a plant to show runs on invented
records labelled invented, and the consumer view is defined by its business rule, the three consumer
segments Meera's plan concerns, with the count of orders it keeps left to the learner's own cell.
The story notebook states each formula with the question it answers and who asks it, and stages no
Week 1 trap.
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

# The chapter openers' short questions, numbered as the deck numbers its sections. vflow draws them
# as written, where ladder would add a second numeral in front of each.
CHAPTERS = ["0. How does retail earn?", "1. Which total is sales?", "2. What is each branch?",
            "3. Do customers come back?", "4. What is a typical order?", "5. Which branch first?",
            "6. What will Meera sign?"]


def where(n, levels):
    """The day's chapter questions beside this notebook's own, the map every notebook opens on."""
    steps = ", ".join(repr(s) for s in levels)
    return code(f'''
        kit.side_by_side(
            kit.vflow({CHAPTERS!r}, lit={n}, show=False),
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
        # How does a retailer like Kalpa make money, who asks the data team for which number, and how is each number worked out?

        **Week 1, Monday, the story that opens the day (chapter 0 of 6).** Most of the room has shopped
        in a store and on an app without seeing the business from behind the till. One scene from the
        morning's story, a Retail-Plus member's Saturday basket at Kalpa Retail, is enough to work out
        the metrics a retail data team is asked for, each as a formula with a worked number.
        Every number here is **invented**, taken from the round illustrative numbers of the retail
        dossier so the arithmetic stays easy, and none of them is Kalpa's data or a real company's.

        **Who needs the answer.** Everyone who asks the data team for a number needs to know which
        number they are asking for. Meera Raghavan, the CEO, asks for revenue and, before she signs any
        acquisition budget, for how long it takes to pay back. Anand Iyer, the finance controller, asks
        for net revenue and margin. The marketing lead asks for conversion and the cost
        of winning a customer, and the head of Retail-Plus, Kalpa's paid membership tier, asks for
        retention. A number worked out on a definition its reader did not ask for sends them to the
        wrong decision, so each formula below comes with the question it answers and the person who
        asks it.

        **The questions on the way.**

        1. Where does Rs 100 of what customers order go before Kalpa keeps a profit?
        2. What does one Saturday basket add towards the costs that stay fixed?
        3. What share of the app's Saturday sessions end in an order?
        4. How do customers, orders and prices multiply into a month's revenue?
        5. How many of January's new customers order again in each later month?
        6. How many months does a new customer take to pay back what winning them cost?

        The metrics at stake are the ten on the domain card,
        `cheatsheets/C2_W01_D01_retail_domain_card_STUDENT.pdf`, and sections 3 and 5 of the retail
        dossier, `study-notes/C2_W01_D01_domain_retail_STUDENT.md`, carry the long version of each.
        This is the day's first notebook, and chapter 1 then opens Kalpa's own 30 orders.

        > **Kavya's review.** Before I read any number, I read what it is divided by, over which
        > window, and who asked for it. Practise saying all three beside every formula below.
        """),
        md("""
        **Setup.** The first cell finds the shared helper, `c2kit`, by walking up from this folder
        until it reaches `scripts/`. No data file is needed, since every number below is invented and
        typed in.
        """),
        code(SETUP + 'print("helper loaded; every number below is invented")'),
        where(0, ["1. Where does Rs 100 ordered go?", "2. What does one basket add?",
                  "3. What share of sessions order?", "4. How does revenue multiply?",
                  "5. Who orders again after January?", "6. When does a customer pay back?"]),
        md("""
        ## 1. Where does Rs 100 of what customers order go before Kalpa keeps a profit?

        Gross merchandise value (GMV) is the value of everything customers ordered, at the prices
        charged. Net revenue is what the business earns from the goods, and the two are different
        numbers: on Rs 100 of invented GMV, net revenue is Rs 80, and what makes up the Rs 20 between
        them is the question chapter 1 opens on Kalpa's own orders. From net revenue, the profit and
        loss statement (the P&L) steps down one line at a time. Rs 60 pays for the goods, the cost of
        goods sold (COGS), and leaves the gross margin. Rs 12.50 goes on the costs that come with every
        order (picking, delivery, handling returns, the payment fee and the offers that bring a
        customer back) and leaves the contribution. Rs 5 pays the fixed costs of stores, warehouses,
        technology, head office and the budget that wins new customers, and what remains is EBITDA,
        earnings before interest, tax, depreciation and amortisation. The finance controller asks for
        every line, since each one says whether a different part of the business pays its way.

        **Predict before you run.** Of Rs 100 ordered, how much is left as EBITDA?

        - a) About Rs 25, a quarter of what was ordered.
        - b) About Rs 10, a tenth of what was ordered.
        - c) Rs 2.50.
        - d) Nothing, since retail runs at a loss.
        """),
        code("""
        gmv = 100.0                                   # invented, the dossier's illustrative Rs 100
        steps = [("the gap chapter 1 opens", -20), ("cost of the goods", -60),
                 ("per-order costs", -12.5), ("fixed costs", -5)]
        names = ["net revenue", "gross margin", "contribution", "EBITDA"]
        answers = ["what the business earns from the goods", "what the goods earn over their cost",
                   "what each order adds towards the fixed costs",
                   "what is left before interest, tax and depreciation"]
        levels, left = {}, gmv
        for (label, change), name in zip(steps, names):
            left += change
            levels[name] = left
        rs = lambda v: ("-" if v < 0 else "") + f"Rs {abs(v):g}"
        kit.bridge(("GMV, invented", gmv), steps, end_label="EBITDA", lit=(0,), fmt=rs,
                   title="Invented: where Rs 100 of GMV goes, line by line")
        kit.table(["line of the P&L", "Rs left of 100", "what it answers"],
                  [(n, f"{levels[n]:g}", a) for n, a in zip(names, answers)],
                  caption="Invented numbers: the P&L from GMV to EBITDA")
        """),
        md("""
        **What happened.** The answer is c: of Rs 100 ordered, Rs 2.50 is left as EBITDA. Net revenue
        is Rs 80, gross margin Rs 20 (25 percent of net revenue) and contribution Rs 7.50. A retailer
        keeps a thin slice, so a price cut that brings no extra volume can give away the whole profit.
        """),
        code("""
        kit.check("net revenue is Rs 80 of every Rs 100 of GMV", levels["net revenue"] == 80)
        kit.check("gross margin is 25 percent of net revenue",
                  levels["gross margin"] / levels["net revenue"] == 0.25)
        kit.check("EBITDA is Rs 2.50", levels["EBITDA"] == 2.5)
        """),
        md("""
        ## 2. What does one Saturday basket add towards the costs that stay fixed?

        The member's basket shows Rs 1,800 at the checkout, which is its GMV, and Kalpa's net revenue
        on it is Rs 1,600 (invented). Contribution is the gross margin less the costs that come with
        each order: picking and delivery, the payment fee, handling returns averaged over every order,
        and the retention offers that bring a customer back. The cost of winning a new customer stays
        out of it, in the acquisition cost of section 6. The finance controller and the category buyers
        ask for contribution, because it is what one more order adds towards the costs that do not
        change with one more order.

        **Predict before you run.** What does the member's order contribute?

        - a) Rs 1,800, what the member paid.
        - b) Rs 150.
        - c) Rs 400, the gross margin.
        - d) Rs 1,600, the net revenue.
        """),
        code("""
        net_revenue = 1600                                          # invented, the basket's net revenue
        basket = {"cost of the four items": -1200, "picking, packing and delivery": -120,
                  "payment fee": -20, "return handling, averaged": -50,
                  "retention marketing on repeat orders": -60}     # invented
        gross_margin = net_revenue + basket["cost of the four items"]
        contribution = net_revenue + sum(basket.values())
        kit.bridge(("net revenue, invented", net_revenue), list(basket.items()), end_label="contribution",
                   title="Invented: the Saturday basket, from net revenue to contribution")
        print(f"gross margin {kit.rupees(gross_margin)} ({gross_margin / net_revenue:.0%} of net revenue), "
              f"contribution {kit.rupees(contribution)} ({contribution / net_revenue:.1%} of net revenue)")
        """),
        md("""
        **What happened.** The answer is b: the order contributes Rs 150, 9.4 percent of its net
        revenue. Delivery costs about the same whatever is in the bag, so a small basket carries the
        same trip on far less margin, which is the arithmetic behind a minimum order for free delivery.
        """),
        code("""
        kit.check("gross margin percent = (net revenue less COGS) / net revenue = 25 percent",
                  gross_margin / net_revenue == 0.25, f"{gross_margin / net_revenue:.0%}")
        kit.check("contribution on the basket is Rs 150", contribution == 150, kit.rupees(contribution))
        """),
        md("""
        ## 3. What share of the app's Saturday sessions end in an order?

        Conversion is orders over visits, both counted on the same days, and the app counts each visit
        as a session. On the invented Saturday the app had 80,000 sessions, 8,000 of them reached a
        cart and 2,000 became orders. Each step of the funnel is the next stage over the one before, so
        the funnel shows where shoppers stopped. Marketing and the app's product team ask for
        conversion, to see whether a campaign brought buyers or only visits.

        **Predict before you run.** What share of the Saturday's 80,000 sessions ended in an order?

        - a) 25 percent.
        - b) 10 percent.
        - c) 2.5 percent.
        - d) 40 percent.
        """),
        code("""
        funnel = [("sessions", 80000), ("carts", 8000), ("orders", 2000)]           # invented
        f = dict(funnel)
        conversion = f["orders"] / f["sessions"]
        funnel_steps = [("sessions that reached a cart", f["carts"] / f["sessions"]),
                        ("carts that became orders", f["orders"] / f["carts"]),
                        ("sessions that became orders, the conversion", conversion)]
        kit.columns([n for n, _ in funnel], [("count", [v for _, v in funnel])],
                    title="Invented: one Saturday on the app")
        kit.table(["step of the funnel", "rate"], [(n, f"{r:.1%}") for n, r in funnel_steps],
                  caption="Invented: the funnel's two steps and the conversion they make")
        """),
        md("""
        **What happened.** The answer is c: 2,000 orders from 80,000 sessions is a conversion of 2.5
        percent. A tenth of the sessions reached a cart and a quarter of the carts became orders, and
        the two steps multiply to the conversion, so a fall in conversion can be traced to the step
        where shoppers stopped.
        """),
        code("""
        kit.check("conversion is 2.5 percent of sessions", conversion == 0.025)
        kit.check("the funnel's two steps multiply to the conversion",
                  abs(funnel_steps[0][1] * funnel_steps[1][1] - conversion) < 1e-12)
        """),
        md("""
        ## 4. How do customers, orders and prices multiply into a month's revenue?

        The revenue tree splits revenue into branches that multiply: customers, times orders per
        customer, times items per order, times price per item, less discounts. In the invented month,
        40,000 customers placed 1.25 orders each, of four items, at Rs 450 an item, before a 10 percent
        discount. The CEO asks for the tree first, because a revenue number that moves says nothing
        about why until it is split, and each branch has an owner: customers belong to marketing,
        orders per customer to retention and the membership tier, and items and price to
        merchandising.

        **Predict before you run.** Which branch does a Retail-Plus membership, with its free delivery
        and member prices, set out to move?

        - a) Customers.
        - b) Orders per customer.
        - c) Items per order.
        - d) Price per item.
        """),
        code("""
        month = {"customers": 40000, "orders per customer": 1.25, "items per order": 4,
                 "price per item": 450, "kept after the discount": 0.90}              # invented
        revenue = 1.0
        for v in month.values():
            revenue *= v
        order_value = month["items per order"] * month["price per item"] * month["kept after the discount"]
        kit.driver_tree({"label": "revenue", "note": kit.rupees(revenue), "kind": "known", "children": [
            {"label": "customers", "note": "40,000", "kind": "known"},
            {"label": "orders per customer", "note": "1.25", "kind": "lit"},
            {"label": "order value", "note": "4 items x Rs 450, less 10%", "kind": "known"}]},
            title="Invented: one month's revenue tree")
        kit.equation(["revenue\\nRs 8.1 crore", "=", "customers\\n40,000", "x", "orders each\\n1.25", "x",
                      "order value\\n" + kit.rupees(order_value)], title="Invented: the tree as one line")
        print(f"revenue {kit.rupees(revenue)}, which is Rs {revenue / 1e7:.1f} crore")
        """),
        md("""
        **What happened.** The answer is b: a membership sets out to bring members back more often,
        which is the orders-per-customer branch. The month multiplies to Rs 8.1 crore, 40,000 customers
        x 1.25 orders x Rs 1,620 an order, and the same revenue could come from more customers, more
        orders each or larger orders, which is why the CEO's first question is which branch moved.
        """),
        code("""
        kit.check("the tree multiplies to Rs 8.1 crore", round(revenue) == 81000000, kit.rupees(revenue))
        kit.check("customers x orders each x order value gives the same revenue",
                  round(month["customers"] * month["orders per customer"] * order_value) == round(revenue))
        """),
        md("""
        ## 5. How many of January's new customers order again in each later month?

        A cohort is the customers who first bought in the same month. Retention in month k is the number
        of the cohort's customers who ordered in month k, over the cohort's starting size. January
        brought 1,000 new customers (invented), and 380 of them ordered in February, 300 in March and
        260 in April. The head of Retail-Plus and marketing ask for retention, because it shows how fast
        a month's new customers thin out, which is what a retention programme is paid to slow.

        **Predict before you run.** What is the January cohort's retention in March?

        - a) 38 percent.
        - b) 30 percent.
        - c) 26 percent.
        - d) 3 percent.
        """),
        code("""
        cohort = 1000                                                      # invented
        buyers = {"Feb": 380, "Mar": 300, "Apr": 260}
        retention = {m: b / cohort for m, b in buyers.items()}
        kit.line(list(buyers), [("retention, share of the 1,000 who started",
                                 [round(r * 100) for r in retention.values()], "good")],
                 fmt=lambda v: f"{v:g}%", title="Invented: January's cohort, month by month")
        kit.table(["month", "the cohort's buyers", "retention"],
                  [(m, buyers[m], f"{r:.0%}") for m, r in retention.items()],
                  caption="Invented: January's 1,000 new customers")
        """),
        md("""
        **What happened.** The answer is b: 300 of the 1,000 ordered in March, a retention of 30
        percent. The cohort holds 38 percent in February, 30 in March and 26 in April, and the
        flattening between March and April is the part a retention programme sets out to raise.
        """),
        code("""
        kit.check("March retention is 30 percent of the cohort", retention["Mar"] == 0.30)
        kit.check("each month's retention sits at or below the month before",
                  list(retention.values()) == sorted(retention.values(), reverse=True))
        """),
        md("""
        ## 6. How many months does a new customer take to pay back what winning them cost?

        Customer lifetime value (CLV) is contribution per order, times orders a year, times
        years as a customer. Customer acquisition cost (CAC) is acquisition spend over the new customers
        it brought, and payback is CAC over the monthly contribution per customer. On invented numbers:
        Rs 150 of contribution per order (section 2's basket), 6 orders a year, 2 years, and an invented
        campaign of Rs 3 crore that brought 20,000 new customers. The CEO and the finance
        controller ask for the payback before they sign an acquisition budget, since it says how long
        the spend takes to come back.

        **Predict before you run.** How many months does one new customer take to pay back their
        acquisition cost?

        - a) 10 months.
        - b) 20 months.
        - c) 24 months, the whole time a customer stays.
        - d) It never pays back.
        """),
        code("""
        per_order, per_year, years = 150, 6, 2                             # invented
        clv = per_order * per_year * years
        cac = 3_00_00_000 / 20000                                          # invented campaign, Rs 3 crore
        monthly = per_order * per_year / 12
        payback = cac / monthly
        kit.bars([("lifetime value, on contribution", clv), ("acquisition cost", cac)], fmt=kit.rupees,
                 lit=(1,), title="Invented: what one customer is worth, and what winning them costs")
        months = list(range(0, 25, 4))
        kit.line([f"month {m}" for m in months],
                 [("contribution paid back", [monthly * m for m in months], "good"),
                  ("acquisition cost", [cac] * len(months), "plan")],
                 fmt=kit.rupees, title="Invented: one customer's contribution catching up with the CAC")
        print(f"CLV {kit.rupees(clv)}, CAC {kit.rupees(cac)}, payback {payback:.0f} months")
        """),
        md("""
        **What happened.** The answer is b. Rs 75 of contribution a month repays the Rs 1,500 CAC in
        20 of the 24 months a customer stays, so the Rs 1,800 lifetime value clears the acquisition
        cost by Rs 300. The Rs 60 of retention marketing inside section 2's contribution is spent on
        repeat orders, and the cost of winning the customer sits only in the CAC, so the payback counts
        each rupee of marketing once.
        """),
        code("""
        kit.check("CLV on contribution is Rs 1,800", clv == 1800)
        kit.check("CAC is Rs 1,500", cac == 1500)
        kit.check("payback is 20 months", payback == 20)
        kit.check("the CLV clears the CAC by Rs 300", clv - cac == 300)
        """),
        md("""
        ### How are days of inventory, gross margin percent and like-for-like growth worked out?

        The domain card carries three more formulas. Days of inventory is average stock at cost over the
        cost of goods sold per day, and supply chain and the category buyers ask for it, since stock on
        the shelf is cash the business has already paid out. Gross margin percent is net revenue less
        the cost of goods, over net revenue, and the finance controller asks for it. Like-for-like
        growth is the sales of the stores open throughout both periods over the same stores' sales in
        the earlier period, less 1, and the CEO and investors ask for it, since it says whether the
        existing stores sell more. On invented numbers the three come to 45 days, 25 percent and 2
        percent.
        """),
        code("""
        inventory_days = 45_00_000 / 1_00_000      # invented: Rs 45 lakh of stock at cost, Rs 1 lakh of COGS a day
        margin_pct = (1600 - 1200) / 1600          # the invented basket of section 2
        like_for_like = 510 / 500 - 1              # invented: 100 stores, Rs 500 crore to Rs 510 crore
        kit.stats([(f"{inventory_days:.0f} days", "days of inventory", "stock at cost / COGS per day"),
                   (f"{margin_pct:.0%}", "gross margin", "(net revenue less COGS) / net revenue"),
                   (f"{like_for_like:.0%}", "like-for-like growth", "the same stores, both periods")],
                  caption="Invented numbers for the card's last three formulas")
        kit.table(["metric", "formula", "invented result", "who asks"],
                  [("days of inventory", "average stock at cost / COGS per day", f"{inventory_days:.0f} days",
                    "supply chain and the category buyers"),
                   ("gross margin percent", "(net revenue less COGS) / net revenue", f"{margin_pct:.0%}",
                    "the finance controller"),
                   ("like-for-like growth", "same stores' sales / their sales last period, less 1",
                    f"{like_for_like:.0%}", "the CEO, store operations and investors")],
                  caption="The card's last three formulas, with who asks for each")
        kit.check("days of inventory is 45", inventory_days == 45)
        kit.check("gross margin is 25 percent of net revenue", margin_pct == 0.25)
        kit.check("like-for-like growth is 2 percent", round(like_for_like, 2) == 0.02)
        """),
        md("""
        ### How would you answer an interviewer who asks how a retailer makes money?

        **[S] How does a retailer make money, and why is a marketplace's GMV not its revenue?** "A
        retailer buys goods and sells them at a margin. GMV is everything customers ordered at the
        prices charged, net revenue is what the business earns from the goods, and I say which of the
        two a number is. From net revenue, the cost of goods leaves the gross margin, the costs that
        come with each order leave the contribution, and the fixed costs leave EBITDA, which for real
        retailers is a few rupees in a hundred. A marketplace does not own the goods, so the GMV it
        shows is its sellers' sales, and its revenue is the fees it charges them."

        **[S] Define average order value, conversion and repeat rate, and say what each is divided
        by.** "Average order value is revenue over orders. Conversion is orders over sessions, both
        counted on the same days. Repeat rate is customers with two or more orders over customers who
        ordered. I name the denominator and the window with every number I send."
        """),
        md("""
        ## Which formulas does the day use, and who asks for each?

        The day uses six formulas, each asked for by a named person, and chapter 1 starts from the
        first of them on Kalpa's own orders.

        - Where does Rs 100 of what customers order go? Net revenue is Rs 80, gross margin Rs 20,
          contribution Rs 7.50 and EBITDA Rs 2.50, and the Rs 20 between GMV and net revenue is
          chapter 1's question.
        - What does one Saturday basket add? It contributes Rs 150 on Rs 1,600 of net revenue, 9.4
          percent.
        - What share of the Saturday's sessions end in an order? The conversion is 2.5 percent, 2,000
          orders from 80,000 sessions.
        - How do customers, orders and prices multiply? 40,000 customers x 1.25 orders x Rs 1,620 an
          order makes Rs 8.1 crore.
        - How many of January's new customers order again? Retention is 38 percent in February, 30 in
          March and 26 in April.
        - How long does a new customer take to pay back? Payback takes 20 months, on a CAC of Rs 1,500
          and Rs 75 of contribution a month.
        - How are the card's last three formulas worked out? They give 45 days of inventory, a 25
          percent gross margin and 2 percent like-for-like growth.
        """),
        code("""
        kit.table(["formula", "invented worked number", "who asks"],
                  [("GMV and net revenue, two totals that differ", "Rs 100 and Rs 80; chapter 1 opens the gap",
                    "the finance controller"),
                   ("contribution = gross margin less per-order costs", "Rs 150 on Rs 1,600 of net revenue",
                    "the finance controller and the category buyers"),
                   ("conversion = orders / sessions, same days", "2.5 percent", "marketing and the app's product team"),
                   ("revenue = customers x orders per customer x order value", "Rs 8.1 crore", "the CEO"),
                   ("retention in month k = cohort buyers in month k / cohort size", "30 percent in March",
                    "the head of Retail-Plus and marketing"),
                   ("payback = CAC / monthly contribution per customer", "20 months",
                    "the CEO and the finance controller, before signing")],
                  caption="The story's formulas; every number invented")
        kit.check_summary()
        print("Next: chapter 1 opens Kalpa's own 30 orders and asks which total is sales.")
        """),
    ]


# --------------------------------------------------------------------------------- chapter 1
def ch1():
    return [
        md("""
        # Which of the file's totals should Meera call sales, and what does each one count?

        **Week 1, Monday, chapter 1 of 6.** Kalpa Retail grew revenue 4 percent last year against a
        plan of 15, and marketing wants Rs 12 crore to acquire customers. Meera Raghavan, the CEO, asks
        the team:

        > "Before I sign anything, I want to understand our own sales. What is 'sales' made of? Where
        > does revenue come from, by customer type and channel? Is acquisition even the branch that is
        > short?"

        **Who needs the answer.** Meera needs one number called sales to measure the 15 percent plan
        from before she decides on the Rs 12 crore, and Anand Iyer, the finance controller, needs that
        number to match his books. A total that counts demand which never became a sale puts the plan's
        base too high, and a channel's baseline built on orders nobody kept looks larger than it is.

        **The questions on the way.**

        1. Which way of answering fits a file of 30 orders?
        2. Which reading of sales comes out largest?
        3. What goes wrong if all 30 orders are sent as sales?
        4. Do sums by status reach the same three totals?
        5. Which total goes at the top of the revenue tree for the chapters that follow?

        The metric at stake is sales, the base every growth percentage is measured from. Each order
        carries a status, delivered, returned after delivery, or cancelled before it left, and the file
        supports four readings of sales: the count of orders, the rupees booked on every order, the
        rupees not cancelled and the rupees delivered. Reliance Retail faces the same question in public:
        it reported gross revenue of Rs 90,408 crore and revenue from operations of Rs 79,745 crore for
        the same quarter to June 2026, with the goods and services tax (GST) it recovered as the step
        between them (Reliance Industries media release, 17 July 2026), so two honest totals for one
        quarter are normal in retail. Section 3 of the retail dossier,
        `study-notes/C2_W01_D01_domain_retail_STUDENT.md`, has the long version.

        The story notebook named gross merchandise value (GMV) and net revenue and said they differ: on
        its invented Rs 100 of GMV, net revenue was Rs 80, and the Rs 20 between them was left for this
        chapter. This chapter opens Kalpa's own 30 orders, placed from 1 July to 26 September 2026, and
        settles which total earns the word sales. Chapter 2 then splits that total into the branches of
        a revenue tree, customers times orders per customer times order value, with the total at the
        top.

        > **Kavya's review.** Every number you bring me today carries its definition beside it. "Sales
        > is five lakh" is a rumour; "booked sales on 30 orders, cancellations included" is a number I
        > can take into Meera's room.
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
        where(1, ["Which way fits 30 orders?", "1. Which reading is largest?",
                  "2. What if all 30 are sales?", "Do sums by status agree?",
                  "Which total tops the tree?"]),
        md("""
        ## Which way of answering fits a file of 30 orders?

        A team could answer "what are our sales?" in four ways, sized here on this file.

        | Option | Rows touched | Time | Error on this file | When it is the right call |
        |---|---|---|---|---|
        | A. Add every amount and send the total | 30 | under a second | It counts every cancelled order as a sale. | It is right only with its name, booked, written beside it. |
        | B. Sum by status and report booked, not cancelled and delivered, with the bridge between them | 30, once | under a second | It has none once the bridge lands. | It fits a CEO's first look, before the plan's definition is known. |
        | C. Ask Finance for the figure in the books | none | a day or more | It has none on Finance's own definition. | It fits when the number goes to the board and must match the books. |
        | D. Tick orders off by hand in a spreadsheet | 30 | about ten minutes | Any one of the 30 cells can carry a typo. | It never fits: it is slow at 30 rows and impossible at 30 lakh. |

        Option A's error is sized first, by counting the orders whose status says they never became a
        sale.
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
        **The best-fit call.** B, because one pass gives all three rupee readings and the bridge names
        every rupee between them, so Meera sees which total she is reading; the sizing shows option A
        would count 4 orders that never became a sale. **What would change it:** if Finance has already
        fixed the definition the 15 percent plan was set on, C decides which of B's three totals goes in
        the note, and B's bridge explains the gap to the others.
        """),
        md("""
        ## 1. Which reading of sales comes out largest?

        One Kalpa order is a dictionary of seven named fields, and the field that splits the readings
        of sales is `status`. The first loop adds every amount to a running total, the way anyone would
        first write it. The `with kit.expect_error()` line catches an error, if one comes, so the
        notebook keeps running.
        """),
        code("""
        with kit.expect_error() as stopped:
            booked = 0
            for order in ORDERS:
                booked += order["amount"]
            print(len(ORDERS), booked)
        """),
        md("""
        The loop stopped, and its last line reads `TypeError: unsupported operand type(s) for +=:
        'int' and 'str'`: a whole number on the left, text on the right, and Python will not add text
        to a number. One amount in the file is stored as text, and the error gets two minutes and no
        more.

        **Your turn.** The loop stopped on a record, and `order` still holds it. Type these two lines
        into the empty cell below and say what is odd about the record:

        ```python
        print(order)
        print(type(order["amount"]))
        ```
        """),
        empty(),
        md("""
        The fix for today is `int()`, which turns text that looks like a whole number into a number.
        Why an amount arrived as text, and whether a larger file holds more, is Wednesday's question.
        The build proper keeps three sums in one loop.

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
        **What happened.** The answer is c: booked is the largest reading, at Rs 5,44,810, against
        Rs 5,35,760 not cancelled and Rs 5,20,790 delivered. The order count, 30, is the fourth reading
        and answers how many times somebody decided to buy. Each narrower reading keeps less, so a
        total sent without its name could be any of the three.
        """),
        md("""
        ## 2. What goes wrong if all 30 orders are sent as sales?

        **Predict before you run.** Of the 30 orders in the booked total, how many never left the
        shelf?

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
        is demand that never arrived. Sent as sales, it puts the base of Meera's 15 percent plan too
        high and inflates the channel it sits in. The check counts orders by channel and status before
        adding anything.
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
        **What happened.** The answer is d: 4 of the 30 orders were cancelled before they left, all of
        them store orders, and sent as sales the Rs 5,44,810 carries their Rs 9,050. The fix writes the
        definition beside the number and shows the walk between the readings: taking out the
        cancellations moves Rs 9,050 and 4 store orders out of sales, and taking out the returns moves
        another Rs 14,970 and 5 web orders. Store's 10 orders overstate its kept orders by 4 in 10.
        """),
        md("""
        ## Do sums by status reach the same three totals?

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
        **What happened.** They do: both routes give Rs 5,44,810 booked, Rs 5,35,760 not cancelled and
        Rs 5,20,790 delivered, to the rupee.
        """),
        md("""
        **When to switch.** The status dictionary is the better route when a fourth status appears, a
        part-refund say, since it needs no new `if`; the one-loop route is clearer when a reader must
        see each definition written out. At a million rows either becomes one `GROUP BY status` in SQL,
        which Week 2 teaches.

        > **Kavya's review.** You found Rs 9,050 that was never a sale, and you found it by counting
        > before adding. Which definition Meera plans on is her call; your job is to make sure she can
        > see which one she is reading.
        """),
        md("""
        ### How would you answer an interviewer who asks which total counts as sales?

        **[F] What counts as "sales": booked, net of cancellations, or delivered, and which do you give
        a CEO?** "All three are legitimate and answer different questions: booked is demand, net of
        cancellations is what left the shelf, and delivered is what stayed sold. On Kalpa's quarter they
        were Rs 5,44,810, Rs 5,35,760 and Rs 5,20,790. I give the CEO the one her plan was set on, say
        it beside the number, and show the bridge so the gaps are named. Reliance Retail publishes gross
        revenue and revenue from operations for the same quarter for the same reason."

        **[D] How would you decide between summing the file yourself and asking Finance for the
        number?** "It depends on who acts on it. For a first look I sum by status in one pass, which
        takes a second and shows every reading. For anything that reaches the board I reconcile to Finance's figure,
        because a number that disagrees with the books loses the room whatever its logic."
        """),
        md("""
        ### What would a part-refund status do to each route?

        A part-refunded order would sit between delivered and returned. The status route absorbs it with
        no new code, and the one-loop route needs a new `if` for every reading it touches, so when the
        categories may grow, group by the category.
        """),
        md("""
        ## Which total goes at the top of the revenue tree for the chapters that follow?

        Booked sales, Rs 5,44,810 on 30 orders, goes at the top of the tree for chapters 2 to 6, named
        as booked, with Rs 5,35,760 not cancelled and Rs 5,20,790 delivered beside it and the bridge
        between them. The escalated case this afternoon rebuilds the answer on delivered orders, the
        reading Anand's books keep.

        - Which way fits a file of 30 orders? Option B fits: one pass sums by status, and the bridge
          names every rupee between the readings.
        - Which reading comes out largest? Booked comes out largest, at Rs 5,44,810.
        - What goes wrong if all 30 are sent as sales? The total carries 4 cancelled store orders, whose
          Rs 9,050 never left the shelf.
        - Do sums by status reach the same totals? They do, all three, to the rupee.
        - Which total should Meera call sales? She should call sales the total her plan was set on, with
          its name beside it, since booked, not cancelled and delivered each count something different.
        """),
        code("""
        kit.table(["What we now know", "The evidence"],
                  [("Sales has four readings, and the definition goes beside the number",
                    "Rs 5,44,810 booked, Rs 5,35,760 not cancelled, Rs 5,20,790 delivered"),
                   ("Cancelled orders are demand that never arrived, all in store", "Rs 9,050 on 4 orders"),
                   ("One amount is text, and int() fixes it for today", "the TypeError, met in two minutes")],
                  caption="Chapter 1: which total is sales")
        kit.driver_tree({"label": "revenue", "note": "Rs 5,44,810 booked, named", "kind": "known", "children": [
            {"label": "customers", "note": "chapter 3", "kind": "unknown"},
            {"label": "orders per customer", "note": "chapter 3", "kind": "unknown"},
            {"label": "average order value", "note": "chapter 2", "kind": "lit"}]},
            title="Where the tree stands after chapter 1")
        kit.check_summary()
        print("Next: chapter 2 turns each branch of the tree into a fraction on one definition.")
        """),
    ]


# --------------------------------------------------------------------------------- chapter 2
def ch2():
    return [
        md("""
        # How does sales split into customers, orders per customer and order value, each a fraction on one definition?

        **Week 1, Monday, chapter 2 of 6.** Meera asked what sales is made of, and the answer is a tree:
        revenue is customers, times orders per customer, times average order value, and order value is
        items per order times price per item, less discounts.

        **Who needs the answer.** Meera needs the tree to see which branch of sales is short, and the
        marketing lead's payback case values every new customer by the order they will place, so it
        leans on the order-value branch. A branch helps them only when it is a metric, a numerator over
        a denominator on one definition and one window. A branch built from two definitions multiplies
        back to revenue nobody booked, and a budget sized on it is too large.

        **The questions on the way.**

        1. Which revenue tree can this file fill?
        2. What is Kalpa's average order value on booked orders?
        3. What goes wrong when booked rupees are divided by delivered orders?
        4. Does the mean of the 30 amounts give the same average order value?
        5. Which branches does the file still lack?

        The metric at stake is average order value (AOV), revenue over orders, the first branch this
        file can measure. Reliance reported Jio's quarter as its branches, 533 million subscribers and
        revenue per user of Rs 215.6 a month (Reliance Industries media release, 17 July 2026): a
        telecom's tree is customers times revenue per customer, stated the same way as Kalpa's.
        Section 5 of the retail dossier, `study-notes/C2_W01_D01_domain_retail_STUDENT.md`, covers the
        metric tree, AOV and basket size.

        Chapter 1 settled the readings of sales on the 30 orders: Rs 5,44,810 booked, Rs 5,35,760 not
        cancelled on 26 orders and Rs 5,20,790 delivered on 21, each with its name beside it. This
        chapter splits the booked total into the tree's branches.

        > **Kavya's review.** Give me each branch as a numerator over a denominator, and tell me which
        > ones this file cannot fill, because nobody can plan on those yet.
        """),
        md("""
        **Setup.** The first cell finds the shared helper, loads the 30 orders from `../data/`, and
        turns every amount into a whole number with `int()`, the fix chapter 1 found for an amount
        stored as text.
        """),
        code(LOAD + '''
for order in ORDERS:
    order["amount"] = int(order["amount"])     # chapter 1's fix for an amount stored as text
print(len(ORDERS), "orders loaded, every amount a whole number")
'''),
        where(2, ["Which tree can this file fill?", "1. What is the booked AOV?",
                  "2. What if two definitions mix?", "Does the mean agree?",
                  "Which branches are missing?"]),
        md("""
        ## Which revenue tree can this file fill?

        Which tree to draw depends on which fields the file holds.

        | Option | Fields it needs | In this file? | What it can tell Meera |
        |---|---|---|---|
        | A. Revenue = orders x AOV | amount, one row per order | yes | It tells her the size of orders and nothing about who buys. |
        | B. Revenue = customers x orders per customer x AOV | amount, customer id | yes | It tells her who buys, how often, and for how much. |
        | C. B, with AOV split into items x price, less discounts | items, list price, discount per order | no | It would tell her which part of the basket moved. |
        | D. A funnel, visits to orders | sessions or footfall | no | It would tell her where shoppers drop out before buying. |

        Each option is sized on this file by setting the fields it needs against the fields the file
        holds.
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
        **The best-fit call.** B, since it is the deepest tree this file fills and it puts marketing's
        branch, customers, beside the two it competes with; C and D each need fields the file does not
        hold. **What would change it:** order lines with items and prices (the order-items table
        arrives later in the programme) move the call to C, and traffic data would add D in front.
        """),
        md("""
        ## 1. What is Kalpa's average order value on booked orders?

        Average order value is booked revenue over the orders it was summed from. The tree multiplies
        the branches back together, and the product has to land on the revenue it started from.

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
        kit.equation(["revenue\\n" + kit.rupees(round(orders * aov)), "=", f"orders\\n{orders}", "x",
                      "average order value\\nRs 5,44,810 / 30, about " + kit.rupees(aov)],
                     title="The two-branch form, multiplied back on the unrounded AOV")
        """),
        code("""
        kit.check("orders x AOV lands on booked revenue", round(orders * aov) == revenue, kit.rupees(orders * aov))
        kit.check("booked AOV is Rs 18,160", round(aov) == 18160, kit.rupees(aov))
        missing = [b for b in ("items", "price", "discount") if b not in ORDERS[0]]
        kit.check("three branches of six are not in this file", len(missing) == 3, missing)
        """),
        md("""
        **What happened.** The answer is a. Kalpa's booked AOV is Rs 5,44,810 over 30 orders, about
        Rs 18,160, and 30 times the unrounded AOV, 30 x (Rs 5,44,810 / 30), lands back on the booked
        total. Because the product always lands on revenue, a wrong leaf can hide in the split while
        the total looks right. Whether Rs 18,160 describes an order anyone would recognise is chapter
        4's question.
        """),
        md("""
        ## 2. What goes wrong when booked rupees are divided by delivered orders?

        Finance's report carries booked revenue, and the operations dashboard counts delivered orders,
        because delivery is what operations runs. An analyst in a hurry takes one number from each.

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
        **Why it is wrong.** The numerator counts the rupees of the 9 cancelled and returned orders while
        the denominator has dropped those orders, so every order looks Rs 7,783 larger than a booked
        order averages. Multiplied back through the tree on the 30 orders the rupees came from, it
        claims Rs 7,78,300 of revenue, 43 percent more than anyone booked, and marketing's payback case
        would value a new customer's order on it. The check is the tree's own identity: AOV times the
        orders the revenue was summed over must give that revenue back. Multiplying by the 21 delivered
        orders would only hand back the numerator, so the check uses the 30 the booked rupees came from.
        """),
        code("""
        # each fraction, and the orders its revenue was summed over
        rows = [("booked / booked", revenue, orders, orders),
                ("delivered / delivered", delivered_revenue, delivered_orders, delivered_orders),
                ("booked / delivered, the trap", revenue, delivered_orders, orders)]
        kit.table(["numerator / denominator", "AOV, rounded", "unrounded AOV x the orders the revenue covers",
                   "lands on that revenue?"],
                  [(n, kit.rupees(round(r / o)), kit.rupees(round(base * r / o)),
                    "yes" if round(base * r / o) == r else "no, " + kit.rupees(round(base * r / o - r)) + " over")
                   for n, r, o, base in rows], caption="The identity check: AOV times the orders the revenue was summed over")
        kit.bars([("booked AOV", round(aov)), ("delivered AOV", round(delivered_revenue / delivered_orders)),
                  ("mixed, the trap", round(hurried_aov))], fmt=kit.rupees, lit=(2,),
                 title="Three AOVs; only the mixed one matches no definition")
        kit.check("the mixed AOV is Rs 25,943", round(hurried_aov) == 25943)
        kit.check("multiplied back on 30 orders, the mix claims revenue nobody booked",
                  round(orders * hurried_aov) != revenue, kit.rupees(orders * hurried_aov))
        """),
        md("""
        **What happened.** The answer is c: booked rupees over delivered orders gives Rs 25,943, which
        matches no definition and multiplies back to Rs 7,78,300, 30 x (Rs 5,44,810 / 21). The fix is one
        definition per
        fraction: booked AOV is Rs 18,160 on 30 orders and delivered AOV is Rs 24,800 on 21 orders, each
        goes out with its definition, the tree multiplies back on each, and the mixed Rs 25,943 is
        dropped.
        """),
        md("""
        ## Does the mean of the 30 amounts give the same average order value?

        Revenue over orders is the mean of the 30 amounts, so the list's own mean must give the same
        number. `statistics.fmean` is the standard library's mean of a list of numbers.
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
        **What happened.** It does: revenue over orders, the list's sum over its length and
        `statistics.fmean` all give Rs 18,160.
        """),
        md("""
        **When to switch.** Revenue over orders is the route when the totals already exist in a report,
        and the mean of the list is the route when you hold the rows; `statistics.fmean` does the same
        sum in one line. Chapter 4 makes a bigger switch: when the question is what a typical order
        looks like, the mean may be the wrong middle altogether.

        > **Kavya's review.** When two reports feed one fraction, ask each report what it counts before
        > you divide. The identity check costs one line and would have caught this before Meera saw it.
        """),
        md("""
        ### How would you answer an interviewer who asks how to grow an online retailer's sales?

        **[S] How would you increase sales for an online retailer?** "I would draw the revenue tree
        before suggesting anything: customers, times orders per customer, times average order value,
        with order value split into items, price and discounts. Then I measure each branch on the same
        window and definition and ask which is short against plan, because each costs something
        different to move: acquisition costs marketing, frequency costs retention, basket costs
        merchandising, and price risks volume. Initiatives come last, each placed on the branch it
        moves."

        **[F] A business says "grow revenue 15 percent"; how do you turn that into questions data can
        answer?** "I ask fifteen percent of which revenue, over which window and against which base.
        Then I break the target down the tree and ask what each branch would have to do alone, in customers, orders
        and rupees per order. Each is a fraction I can compute and each maps to a team that owns it."
        """),
        md("""
        ### Why do the denominators cancel when the branches multiply?

        Customers x (orders / customers) x (revenue / orders) = revenue, because each denominator
        cancels the next numerator. A branch measured on another definition breaks the chain for the
        same reason: its denominator no longer matches its neighbour's numerator.
        """),
        md("""
        ## Which branches does the file still lack?

        Three of the tree's six branches are missing: items per order, price per item and discounts
        need order lines with items and prices, which arrive later in the programme. The two customer
        branches can be counted from the customer ids, which is chapter 3's work.

        - Which tree can this file fill? Option B fills: revenue is customers x orders per customer x
          AOV.
        - What is the booked AOV? It is Rs 18,160, Rs 5,44,810 over 30 orders.
        - What goes wrong when booked rupees meet delivered orders? A mixed AOV of Rs 25,943 claims
          Rs 7,78,300 of revenue that nobody booked.
        - Does the mean of the amounts agree? It does, at Rs 18,160 by every route.
        - How does sales split? It splits into customers, orders per customer and order value, each a
          fraction on one definition, with three of order value's branches still missing from the file.
        """),
        code("""
        kit.table(["What we now know", "The evidence"],
                  [("Each branch is a numerator over a denominator on one definition", "AOV = Rs 5,44,810 / 30, about Rs 18,160"),
                   ("Three branches are not in this file", "items, price and discounts"),
                   ("A fraction from two definitions matches nothing", "Rs 25,943 would claim Rs 7,78,300")],
                  caption="Chapter 2: what each branch is")
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
        # How many customers does Kalpa have, and how many came back for a second order?

        **Week 1, Monday, chapter 3 of 6.** Marketing's Rs 12 crore buys customers, and Meera wants to
        know how many Kalpa already has and whether they come back.

        **Who needs the answer.** Meera needs the customer count before she funds acquisition: if
        Kalpa's customers never come back, acquisition is the only branch left, and if they do,
        frequency, orders per customer, is a branch she can grow without buying anyone new. The
        marketing lead and the head of Retail-Plus own those two branches. A count that reads "nobody
        comes back" makes frequency look dead and hands the Rs 12 crore to acquisition on a counting
        slip.

        **The questions on the way.**

        1. How do we count customers when a row is an order?
        2. How many customers came back for a second order?
        3. What goes wrong if every row is counted as a customer?
        4. Does the mean of the per-customer counts give the same rate?
        5. Which count goes on the tree's customer branch, and on which definition?

        The metric at stake is customers, and orders per customer: orders over distinct customers in
        the window. Reliance Retail reported 396 million registered customers at 30 June 2026 (Reliance
        Industries media release, 17 July 2026), and a registered customer is a denominator of its own:
        a quarter's orders divided by it give a different, smaller metric from orders per customer who
        ordered. Section 5 of the retail dossier, `study-notes/C2_W01_D01_domain_retail_STUDENT.md`,
        covers frequency and repeat rate.

        Chapter 2 measured the first branch on booked orders, the reading chapter 1 put at the top of the
        tree: booked revenue of Rs 5,44,810 over 30 orders is an average order value (AOV) of about
        Rs 18,160. This chapter fills the two customer branches and checks that the tree multiplies back.

        > **Kavya's review.** One person can leave several rows, so count people by their id and say in
        > the note how you counted them.
        """),
        md("""
        **Setup.** The first cell finds the shared helper, loads the 30 orders from `../data/`, applies
        chapter 1's `int()` fix to every amount, and sums booked revenue.
        """),
        code(LOAD + '''
for order in ORDERS:
    order["amount"] = int(order["amount"])     # chapter 1's fix for an amount stored as text
revenue = sum(order["amount"] for order in ORDERS)
print(len(ORDERS), "orders,", kit.rupees(revenue), "booked")
'''),
        where(3, ["How do we count customers?", "1. How many came back?",
                  "2. What if rows are customers?", "Does the mean of counts agree?",
                  "Which count goes on the branch?"]),
        md("""
        ## How do we count customers when a row is an order?

        A row in the file is one order, and one customer can place several, so there are four ways to
        count customers, sized here on the 30 rows.

        | Option | Passes over the rows | What it answers | Error on this file |
        |---|---|---|---|
        | A. `len(ORDERS)`, the row count | none | how many orders | It counts a repeat customer once per order. |
        | B. `len(set(ids))`, distinct ids | one | how many customers | It has none, though it says nothing about who came back. |
        | C. A dictionary of orders per id | one | how many customers, how many orders each, who came back | It has none. |
        | D. Sort the ids and count where they change | a sort and a pass | how many customers | It has none if done right, and it is easy to miscount by hand. |
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
        **The best-fit call.** C: one pass fills both customer branches and names the repeat buyers,
        which is the number Meera's question turns on, and B and D agree with it on 23 customers where
        A reads 30. B is the right call when only the count is needed. **What would change it:** at
        millions of rows the same count is one `COUNT(DISTINCT customer_id)` in the warehouse, which
        Week 2 teaches, and a loop in a notebook stops being the tool.
        """),
        md("""
        ## 1. How many customers came back for a second order?

        A set says how many customers there are and forgets the rest. A dictionary keeps a count per
        id: the customer id is the key, and the count of that customer's orders is the value.

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
        **What happened.** The answer is b: 7 of the 23 customers came back for a second order, 16
        bought once, and 30 orders over 23 customers is 1.30 orders each. The difference between orders
        and customers equals the repeat buyers here because nobody bought three times; a third order
        would part the two, which is why the dictionary is the count to trust. One repeat customer is
        recorded as Retail-Core on one order and Retail-Plus on the other, since the segment is recorded
        on each order, so a count of customers per segment has to say which order's segment it used.
        With every branch measured, the tree multiplies back on the unrounded values: 23 x (30 / 23) x
        (Rs 5,44,810 / 30) = Rs 5,44,810. Rounded to 1.30 and Rs 18,160 first, the same product reads
        about Rs 5,42,984, so the check multiplies the values as computed, before any rounding.
        """),
        code("""
        aov = revenue / len(ORDERS)
        rebuilt = customers * per_customer * aov
        kit.driver_tree({"label": "revenue", "note": kit.rupees(revenue) + " booked", "kind": "known", "children": [
            {"label": "customers", "note": f"{customers} distinct ids", "kind": "known"},
            {"label": "orders per customer", "note": f"{per_customer:.2f}; {repeat} came back", "kind": "good"},
            {"label": "average order value", "note": "about " + kit.rupees(aov) + "; typical? chapter 4", "kind": "unknown"}]},
            title="The tree with chapter 3's leaves filled in")
        kit.check("customers x orders per customer x AOV, unrounded, gives booked revenue", round(rebuilt) == revenue,
                  kit.rupees(round(rebuilt)))
        """),
        md("""
        ## 2. What goes wrong if every row is counted as a customer?

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
        **Why it is wrong.** The division is correct and its denominator is wrong: a row is an order,
        and one customer can place several. Reported to Meera, "1.00 orders per customer, nobody comes
        back" says frequency is dead and the only way to grow is to buy customers, which is marketing's
        case for Rs 12 crore made by a counting slip. The check compares the ids in the list with the
        distinct ids.
        """),
        code("""
        distinct = set(ids)
        kit.bars([("rows (orders)", len(ids)), ("distinct customer ids", len(distinct))], lit=(1,),
                 title="The same column counted two ways")
        kit.check("the list holds one id per row", len(ids) == 30)
        kit.check("the set holds 23 distinct customers", len(distinct) == 23, len(distinct))
        """),
        md("""
        **What happened.** The answer is c: counting rows as customers reports 30 customers at 1.00
        orders each and says nobody comes back. The fix divides by distinct customers, as the build did:
        30 / 23 = 1.30 orders each, the 7 who came back are visible again, and "nobody comes back" drops
        out of the case for the Rs 12 crore.
        """),
        md("""
        ## Does the mean of the per-customer counts give the same rate?

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
        **What happened.** It does: both routes give 1.3043 orders per customer, 1.30 to two places.
        """),
        md("""
        **When to switch.** The ratio route needs only two counts, which is what a report holds; the
        counts route needs the rows and also gives the spread, 16 customers at one order and 7 at two,
        which the ratio hides. Use the counts whenever someone will ask how many came back.

        > **Kavya's review.** Your first 30 was a count of rows, divided as if it were people. Every
        > rate you send upstairs carries the name of its denominator, and a count of people comes from
        > their ids.
        """),
        md("""
        ### How would you answer an interviewer who asks how you count customers?

        **[F] Your extract shows 30 orders and 30 customers; what do you check before saying nobody
        comes back?** "I check whether 30 customers means 30 distinct ids or 30 rows. I compare the
        length of the id column with the length of its set; on Kalpa's quarter that is 30 against 23, so seven
        orders came from people who had already bought. I would also check the window, since a customer
        who buys every four months looks one-time in one quarter, and whether one person can carry two
        ids."

        **[SV] A list against a dictionary: when do you reach for each?** "A list when order matters or
        I will walk every item. A dictionary when I look things up or count by a key, such as orders per
        customer id. Real records are both: a list of dictionaries, one per row, which is what a JSON
        array from an API looks like. Checking membership in a list walks every item, while a dictionary
        goes straight to its key."

        **[SV] How do you count distinct customers in Python, and why does a set give the answer a list
        does not?** "`len(set(ids))`, because a set keeps each value once however often it is added,
        while a list keeps every occurrence. When I also need orders per customer, a dictionary keyed by
        id gives both."
        """),
        md("""
        ### Which channel did the 7 repeat buyers come back through?

        A set answers overlap questions: `&` keeps the ids two sets share and `|` the ids in either. A
        frequency plan has to reach customers where they come back, so the question is which channels
        the repeat buyers used. All 7 came back through a different channel from their first order, so a
        frequency plan built on one channel would have missed every one of these returns.
        """),
        code("""
        by_channel = {"app": set(), "web": set(), "store": set()}
        for order in ORDERS:
            by_channel[order["channel"]].add(order["customer_id"])
        multi = sum(1 for cid in counts if sum(cid in s for s in by_channel.values()) > 1)
        kit.table(["question", "set expression", "answer"],
                  [("customers on the app", "len(app)", len(by_channel["app"])),
                   ("customers on both app and web", "len(app & web)", len(by_channel["app"] & by_channel["web"])),
                   ("customers on any channel", "len(app | web | store)",
                    len(by_channel["app"] | by_channel["web"] | by_channel["store"])),
                   ("customers on more than one channel", "counted", multi)],
                  caption="Set questions on the same 30 orders")
        kit.columns(["one channel", "two channels"], [("customers", [len(counts) - multi, multi])], lit=(1,),
                    width=520, title="Customers by the number of channels they bought through")
        kit.check("the union of the channels is all 23 customers",
                  len(by_channel["app"] | by_channel["web"] | by_channel["store"]) == 23)
        kit.check("every repeat buyer used a second channel", multi == repeat == 7, multi)
        """),
        md("""
        ### When does orders less customers stop counting the repeat buyers?

        On Kalpa's file, 30 orders less 23 customers is 7, and 7 customers came back, because nobody
        bought three times. On three **invented** customers with 3, 1 and 1 orders, orders less
        customers is 2 while only 1 customer came back: the dictionary counts people, and the
        subtraction counts extra orders.
        """),
        code("""
        invented = {"X-1": 3, "X-2": 1, "X-3": 1}          # invented customers, for the mechanism only
        extra_orders = sum(invented.values()) - len(invented)
        came_back = sum(1 for n in invented.values() if n > 1)
        kit.bars([("orders less customers", extra_orders), ("customers who came back", came_back)], lit=(1,),
                 title="Invented: a third order parts the two counts")
        kit.check("on the invented three the two counts differ", extra_orders != came_back)
        """),
        md("""
        ## Which count goes on the tree's customer branch, and on which definition?

        The customer branch takes 23 customers, the distinct customer ids behind the 30 booked orders
        placed from 1 July to 26 September, and the frequency branch takes 1.30 orders per customer on
        the same booked orders. Each number goes out with that definition beside it, since a count of
        customers depends on which orders it is taken from. Frequency is a live branch: 7 of the 23 came
        back for a second order, so Meera can grow it without buying anyone new.

        - How do we count customers when a row is an order? We count distinct ids, with a dictionary
          that also counts each customer's orders.
        - How many came back? 7 of the 23 came back, and 16 bought once.
        - What goes wrong if every row is a customer? The draft reports 30 customers at 1.00 orders
          each and says nobody comes back.
        - Does the mean of the counts agree? It does, at 1.30 by both routes.
        - Which count goes on the customer branch? The branch takes 23 customers and 1.30 orders each,
          on booked orders, written with that definition.
        - Which channel did the repeat buyers come back through? All 7 came back through a different
          channel from their first order.
        - When does orders less customers stop counting repeat buyers? It stops as soon as anyone
          places a third order, as the invented three show: 2 extra orders from 1 customer who came
          back.
        """),
        code("""
        leaf = (f"customers: {customers} distinct customer ids behind the {len(ORDERS)} booked orders placed "
                f"from 1 July to 26 September; orders per customer: {per_customer:.2f}, on the same booked orders")
        print(leaf)
        kit.table(["What we now know", "The evidence"],
                  [("A row is an order, and customers are counted by id", "30 rows, 23 customers"),
                   ("Frequency is a live branch", "1.30 orders each; 7 of 23 came back"),
                   ("The tree multiplies back on unrounded values", "23 x (30 / 23) x (Rs 5,44,810 / 30) = Rs 5,44,810"),
                   ("The customer branch carries its definition", "23 customers, 1.30 orders each, on booked orders")],
                  caption="Chapter 3: do customers come back")
        kit.check_summary()
        print("Next: chapter 4 asks whether Rs 18,160 describes a typical Kalpa order.")
        """),
    ]


# --------------------------------------------------------------------------------- chapter 4
def ch4():
    return [
        md("""
        # What does a typical Kalpa order look like, stated so that one large order cannot move it?

        **Week 1, Monday, chapter 4 of 6.** Marketing's case for Rs 12 crore values every new customer
        by the order they will place. Meera wants to know what that order is worth, and Anand has said
        how he will read the answer:

        > Meera: "What does a typical order look like?"
        > Anand: "No averages. One business customer can move an average."

        **Who needs the answer.** Meera and the marketing lead need a typical order to price what a new
        customer brings in the acquisition payback, and Anand will reject any answer that one order can
        move. A first order valued several times too high makes Rs 12 crore look cheap and the payback
        look short.

        **The questions on the way.**

        1. Which middle survives one large order?
        2. What is the median Kalpa order?
        3. Where does a trimmed mean of Kalpa's 30 orders land?
        4. What goes wrong when the mean is sold as the typical order?
        5. Does Python's own median function give the same middle?
        6. What goes into the payback case?

        The metric at stake is the typical order, the value per order that an acquisition payback is
        priced on. Blinkit reported a net average order value of Rs 518 for the quarter to June 2026
        (MediaNama on Eternal's results, 24 July 2026). A reported AOV is a mean, the right number for
        totals across millions of orders, and the wrong one to describe one shopper's basket when a few
        very large orders sit in the same file. Section 5 of the retail dossier,
        `study-notes/C2_W01_D01_domain_retail_STUDENT.md`, covers average order value and basket size.

        Chapter 3 filled the customer branches: 23 customers placed 1.30 orders each, 7 came back, and
        the tree multiplies back through chapter 2's AOV of about Rs 18,160, booked revenue over orders. This
        chapter asks whether Rs 18,160 describes an order anybody at Kalpa would recognise.

        > **Kavya's review.** When you tell Meera what a typical order is worth, tell her which middle
        > you used and why. If one order can move your number, your number is describing that order.
        """),
        md("""
        **Setup.** The first cell finds the shared helper, loads the 30 orders from `../data/`, turns
        each amount into a whole number with chapter 1's `int()` fix, and takes the mean, which is
        chapter 2's AOV.
        """),
        code(LOAD + '''
amounts = [int(order["amount"]) for order in ORDERS]
mean = sum(amounts) / len(amounts)
print(len(amounts), "amounts; the mean, chapter 2's AOV, is", kit.rupees(mean))
'''),
        where(4, ["Which middle survives?", "1. What is the median?",
                  "2. Where does a trimmed mean land?", "3. What if the mean is typical?",
                  "Does Python's median agree?", "What goes into the payback?"]),
        md("""
        ## Which middle survives one large order?

        A team could report four middles. The sizing says how far each moves when one **invented**
        Rs 90,000 order joins five invented orders of Rs 1,900 to Rs 2,600, which is the test Anand set.

        | Option | Work on this file | How far one large order moves it | When it is the right call |
        |---|---|---|---|
        | A. The mean, total over count | one sum | It moves by every rupee of the large order. | It is right when totals and forecasts must multiply back. |
        | B. The median, the middle of the sorted amounts | a sort of 30 | It moves by one place in the sort. | It is right when the question is what a typical order looks like. |
        | C. A trimmed mean, dropping the smallest and the largest order | a sort and a sum | It moves little, if the rule trims enough. | It is right when there is a stated rule for how many to drop. |
        | D. A mean per customer type | a grouping | It does not move within a type. | It is right when the types are known and each gets its own plan. |
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
        **The best-fit call.** B, the median, survives: it moves Rs 50 when the invented Rs 90,000
        order joins, where the mean moves more than Rs 14,000. Report it as the typical order, with A
        beside it for totals and the gap between the two stated. **What would change it:**
        if marketing prices the payback per customer type, D answers better; that grouping is the
        afternoon's second case.
        """),
        md("""
        ## 1. What is the median Kalpa order?

        The median has half the orders below it and half above. With 30 orders there are two middle
        values, the 15th and 16th in size order, and the median is halfway between them.

        **Predict before you run.** What is the median order?

        - a) About Rs 2,200.
        - b) Rs 18,160.
        - c) Rs 9,080, half the mean.
        - d) Rs 2,300, the 16th order in size order.
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
        **What happened.** The answer is a: the median Kalpa order is Rs 2,205, halfway between the 15th
        and 16th orders, Rs 2,110 and Rs 2,300. The mean of Rs 18,160 sits about eight times above it.
        """),
        md("""
        ## 2. Where does a trimmed mean of Kalpa's 30 orders land?

        Option C in the table, run on the file: drop the smallest and the largest order and average the
        other 28. It needs a rule for how many to drop, and it is the middle a spreadsheet user reaches
        for first.

        **Predict before you run.** Where does the trimmed mean of the 30 land?

        - a) Near the mean of Rs 18,160.
        - b) Halfway between the mean and the median.
        - c) Within about Rs 100 of the median.
        - d) Below every order in the file.
        """),
        code("""
        trimmed_kalpa = trimmed(amounts)
        definitions = {"booked": {"delivered", "returned", "cancelled"}, "not cancelled": {"delivered", "returned"}}
        middles = {}
        for name, keep in definitions.items():
            kept = [int(o["amount"]) for o in ORDERS if o["status"] in keep]
            middles[name] = {"orders": len(kept), "mean": sum(kept) / len(kept), "median": middle(kept)}
        kit.bars([("mean", round(mean)), ("trimmed mean, 28 of 30", round(trimmed_kalpa)), ("median", round(median))],
                 fmt=kit.rupees, lit=(2,), title="Three middles of Kalpa's 30 orders")
        kit.check("the trimmed mean lands within Rs 100 of the median", abs(trimmed_kalpa - median) < 100,
                  kit.rupees(round(trimmed_kalpa)))
        kit.check("the trimmed mean sits more than Rs 15,000 below the mean", mean - trimmed_kalpa > 15000)
        """),
        md("""
        **What happened.** The answer is c: the trimmed mean lands at Rs 2,300, beside the median of
        Rs 2,205. The rule of one order at each end happened to fit this file, and a file with more very
        large orders than the rule trims would leave the trimmed mean far above the median, which is why
        the median, which needs no rule, stays the call.
        """),
        md("""
        ## 3. What goes wrong when the mean is sold as the typical order?

        Marketing's slide values each new customer's first order at the average order value.

        **Predict before you run.** How many of the 30 orders are larger than the mean of Rs 18,160?

        - a) About 15, half of them, since the mean is the middle.
        - b) One of them.
        - c) Most of them, since the mean sits low.
        - d) None of them.

        **The plausible wrong answer.** The number as it appears on marketing's slide:
        """),
        code("""
        print("A typical Kalpa order:", kit.rupees(mean))
        print("What each new customer's first order is worth, per the model:", kit.rupees(mean))
        """),
        md("""
        **Why it is wrong.** A typical order is one that most orders look like. If nearly every order
        sits below the mean, something at the top is pulling the total, and the mean with it. Priced at
        Rs 18,160, a new customer's order looks about eight times the size of the orders Kalpa usually
        takes, and Rs 12 crore looks cheap. The check counts the orders above the mean and draws every
        amount.
        """),
        code("""
        import math
        above = sum(1 for a in amounts if a > mean)
        print(f"only {above} of the {len(amounts)} orders sits above the mean of {kit.rupees(mean)}")
        kit.strip([math.log10(a) for a in amounts], markers=[("mean", math.log10(mean), "bad")],
                  lo=2, hi=6, fmt=lambda v: kit.rupees(round(10 ** v)),
                  title="The 30 amounts on a scale where each step is ten times the one before")
        kit.check("only 1 of the 30 orders sits above the mean", above == 1)
        kit.check("the mean sits between the two largest orders", ranked[-2] < mean < ranked[-1])
        """),
        md("""
        **What happened.** The answer is b: only 1 of the 30 orders sits above the mean of Rs 18,160,
        and the dots pile up below Rs 5,000 while the mean stands far to the right. Sold as typical,
        Rs 18,160 values a new customer's order about eight times higher than the median order of
        Rs 2,205.

        **Your turn.** Which order sits above the mean? Type these lines into the empty cell and run
        them, then say in one sentence what kind of order the largest one must be:

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
        The fix is to report the median, Rs 2,205, as the typical order, with the mean beside it for
        totals, since mean times count still gives revenue. A payback that credits each new customer's
        order with Rs 18,160 overstates a typical order about eightfold, so it is built on the mean
        contribution of the customers the spend targets, and chapter 5 sizes the plan on the customer
        segments Meera's plan concerns.
        """),
        md("""
        ## Does Python's own median function give the same middle?

        The standard library's `statistics.median` has the rule built in, including the even-count
        case. It must agree with the hand-written middle on every definition.
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
        **What happened.** It does: the hand-written middle and `statistics.median` agree at Rs 2,205 on
        booked orders and Rs 2,100 on not-cancelled orders.
        """),
        md("""
        **When to switch.** Write the middle by hand once, so you know what the library does with an
        even count; after that `statistics.median` is the route, and in Week 2 it becomes
        `PERCENTILE_CONT(0.5)` in SQL and `.median()` in pandas. The choice left is between middles,
        since the mean comes back whenever a total has to reconcile.

        > **Kavya's review.** Anand said "no averages" and you now know why. Put the median in the
        > sentence, say the mean is eight times higher, and give the count of orders above it.
        """),
        md("""
        ### How would you answer an interviewer who asks for a typical order value?

        **[S] Mean or median for order value, and why?** "I use the median when a few large orders can
        pull the mean, which in retail is almost always, since occasional large buyers sit in the same
        file as households. I report both with the count of orders above the mean, because the gap is itself
        a finding: on Kalpa's quarter the mean was Rs 18,160, the median Rs 2,205, and only 1 of the 30
        orders sat above the mean. The mean keeps its job for totals, since mean times count gives
        revenue."

        **[S] The mean order is Rs 18,160 and the median Rs 2,205; what do you tell the business about
        its orders?** "I tell them that a typical order is about Rs 2,205 and that very large orders
        lift the mean to eight times that. I would sort the orders, look at the largest, and ask which customers they
        come from, since a plan or a payback is built on the mean of the segments it targets, with the
        median quoted as the typical order."

        **[D] Which middle would you put in a payback model, and what would make you change it?** "A
        payback is a total over a customer's life, so it needs a mean, and the mean has to come from the
        customers the spend targets: their mean contribution per customer over the repeat window. The
        median is what I quote as the typical order beside it. I would change the segments, and so the
        mean, if the spend targeted business buyers."
        """),
        md("""
        ### How far does one order have to grow before the mean stops describing the file?

        One **invented** order grows from Rs 2,600 to Rs 90,000 beside the same five invented orders.
        The median never passes Rs 2,500, while the mean follows the growing order all the way.
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
        ## What goes into the payback case?

        The median, Rs 2,205, goes in as the typical order, the payback itself is priced on the mean
        contribution of the customers the spend targets, and the booked mean of Rs 18,160 stays beside
        the median for totals.

        - Which middle survives one large order? The median survives, moving Rs 50 where the mean moves
          more than Rs 14,000 on the invented six.
        - What is the median order? It is Rs 2,205, halfway between Rs 2,110 and Rs 2,300.
        - Where does a trimmed mean land? It lands at Rs 2,300, near the median, because its rule
          happened to fit this file.
        - What goes wrong when the mean is sold as typical? Rs 18,160 is eight times the median, and
          only 1 of the 30 orders sits above it.
        - Does Python's median agree? It does, on booked and on not-cancelled orders.
        """),
        code("""
        kit.table(["What we now know", "The evidence"],
                  [("The mean is total over count, and it sits far above most orders",
                    "Rs 18,160, with only 1 of the 30 orders above it"),
                   ("The median is the typical order", "Rs 2,205, about one eighth of the mean"),
                   ("A trimmed mean lands near the median on this file", "Rs 2,300 against Rs 2,205"),
                   ("A payback on Rs 18,160 overstates a typical order eightfold",
                    "the payback uses the targeted customers' mean")],
                  caption="Chapter 4: what is a typical order")
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
        # Which branch should Meera open first to reach the 15 percent plan, and why not the others?

        **Week 1, Monday, chapter 5 of 6.** Meera has a tree with every branch measured, and marketing
        has proposed moving one branch, customers, for Rs 12 crore. Before she signs, she wants to know
        which branch to open first, and why not the others.

        **Who needs the answer.** Meera decides where the money goes. The marketing lead owns
        acquisition, and the head of Retail-Plus owns the members most likely to come back. The
        Rs 12 crore placed on a branch that was never short, or a plan sized by adding lifts that
        multiply, spends the budget on the wrong lever.

        **The questions on the way.**

        1. Which orders is the 15 percent plan sized on, and how many rupees short are they?
        2. What would each branch have to do alone to reach the plan?
        3. Which branch has evidence behind it?
        4. What goes wrong when two 10 percent lifts are called 20 percent?
        5. Does adding the lift piece by piece land on the same total?
        6. What would switch the call from frequency to acquisition?

        The metric at stake is revenue growth against the 15 percent plan, and what each branch alone
        would have to do to reach it. Retailers pay to move frequency directly: Flipkart launched
        Flipkart Black at Rs 1,499 a year in 2025, evolving it from its VIP programme (Flipkart Stories,
        12 September 2025), and Amazon offers Prime in India from Rs 399 to Rs 1,499 a year (About
        Amazon India). A membership is a bet on the frequency branch, placed by companies that could have
        spent the same money on acquisition. Sections 2 and 5 of the retail dossier,
        `study-notes/C2_W01_D01_domain_retail_STUDENT.md`, cover Retail-Plus, the paid tier, and the
        acquisition payback.

        Chapter 4 settled the typical order: the median is Rs 2,205, and the booked mean of Rs 18,160
        sits about eight times above it, so a plan is priced on the customers it targets, with the
        median quoted as the typical order. The tree reads 23 customers, 1.30 orders each, 16 of them
        bought once, and Rs 5,44,810 booked on 30 orders.

        > **Kavya's review.** Pick the branch the evidence points at and the one that costs least to
        > test. Then say what would make you pick another.
        """),
        md("""
        **Setup.** The first cell finds the shared helper, loads the 30 orders from `../data/`, applies
        chapter 1's `int()` fix, and rebuilds the booked tree: customers by id, orders per customer and
        average order value (AOV).
        """),
        code(LOAD + '''
for order in ORDERS:
    order["amount"] = int(order["amount"])     # chapter 1's fix for an amount stored as text
revenue = sum(o["amount"] for o in ORDERS)
counts = {}
for order in ORDERS:
    counts[order["customer_id"]] = counts.get(order["customer_id"], 0) + 1
customers, orders = len(counts), len(ORDERS)
per_customer, aov = orders / customers, revenue / orders
once = sum(1 for c in counts.values() if c == 1)
print(f"booked: {kit.rupees(revenue)} from {customers} customers, {per_customer:.2f} orders each, about {kit.rupees(round(aov))} an order")
'''),
        where(5, ["Which orders is the plan on?", "What would each branch do alone?",
                  "1. Which branch has evidence?", "2. What if lifts are added?",
                  "Does the lift, piece by piece, agree?", "What would switch the call?"]),
        md("""
        ## Which orders is the 15 percent plan sized on, and how many rupees short are they?

        Meera's growth plan concerns Kalpa's three consumer segments, Retail-Core, Retail-Plus and
        Student, since those are the customers a retention offer or an acquisition campaign reaches.
        The consumer view keeps the orders whose segment is one of those three, and the plan is sized on
        it: 15 percent more than the consumer view booked in the quarter.

        **Predict before you run.** How many more rupees does the plan ask of the consumer view?

        - a) About Rs 81,700, 15 percent of all booked sales.
        - b) About Rs 9,700.
        - c) About Rs 64,800.
        - d) About Rs 1,500.
        """),
        code("""
        CONSUMER = ("Retail-Core", "Retail-Plus", "Student")          # the segments Meera's plan concerns
        consumer = [o for o in ORDERS if o["segment"] in CONSUMER]
        c_rev = sum(o["amount"] for o in consumer)
        plan = c_rev * 1.15
        kit.bridge(("consumer view, booked", c_rev), [("the plan's 15 percent", round(plan - c_rev))],
                   end_label="the plan", lo=50000,
                   title="The 15 percent plan on the consumer view (the axis starts at Rs 50,000)")
        print(f"consumer view booked {kit.rupees(c_rev)}; the plan {kit.rupees(int(plan + 0.5))}, "
              f"{kit.rupees(round(plan - c_rev))} more")
        kit.check("the consumer view keeps only the three consumer segments",
                  {o["segment"] for o in consumer} == set(CONSUMER))
        kit.check("the consumer view booked Rs 64,810", c_rev == 64810, kit.rupees(c_rev))
        kit.check("the plan asks Rs 9,722 more of it", round(plan - c_rev) == 9722)
        """),
        md("""
        **What happened.** The answer is b: the consumer view booked Rs 64,810 in the quarter, so the
        plan is about Rs 74,532, Rs 9,722 more.

        **Your turn.** How many orders does the consumer view keep? Type this line into the empty cell
        below and run it:

        ```python
        print(len(consumer), "orders in the consumer view, of", len(ORDERS))
        ```
        """),
        empty(),
        md("""
        ## What would each branch have to do alone to reach the plan?

        Any one branch could carry the plan alone, and each asks something different of different
        people, set out below with each branch's ask sized in rupees and percentages.

        | Option | The branch moved alone | Who has to act | Evidence in this file |
        |---|---|---|---|
        | A. Acquisition | customers | People Kalpa has never met have to start buying. | There is none, since one window cannot show customers falling. |
        | B. Frequency | orders per customer | Customers already on file have to buy again. | Some customers already came back in the quarter. |
        | C. Order value | rupees per order | Every shopper has to spend more on every basket. | Items and prices are not in this file. |
        | D. Price | price per item | Every shopper has to pay more, and nobody may leave. | There is none, and nothing may sell above its printed maximum retail price. |

        **Predict before you run.** Once each branch is sized, which one does the evidence in this file
        favour?

        - a) Customers: 15 percent more customers who buy like today's.
        - b) Frequency: 15 percent more orders from today's customers.
        - c) Order value: Rs 335 more on every order.
        - d) Price: every price 15 percent higher, with nobody leaving.
        """),
        code("""
        c_counts = {}
        for o in consumer:
            c_counts[o["customer_id"]] = c_counts.get(o["customer_id"], 0) + 1
        c_cust, c_orders = len(c_counts), len(consumer)
        c_once = sum(1 for c in c_counts.values() if c == 1)
        c_per, c_aov = c_orders / c_cust, c_rev / c_orders
        need = {"customers": c_cust * 1.15, "orders": c_orders * 1.15, "aov": c_aov * 1.15}
        returning = (need["orders"] - c_orders) / c_once       # share of one-time buyers who must return once
        in_ten = ["none", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
        kit.table(["option: the branch moved alone", "the plan needs", "in rupees and percentages", "evidence in this file"],
                  [("A. acquisition, customers", "15 percent more customers",
                    f"{kit.rupees(round(plan - c_rev))} of orders from people Kalpa has never met",
                    "none: one window cannot show customers falling"),
                   ("B. frequency, orders per customer", "15 percent more orders from the same customers",
                    f"about {in_ten[round(returning * 10)]} in ten of the one-time buyers returning once",
                    f"{c_cust - c_once} customers already came back"),
                   ("C. order value", f"{kit.rupees(round(c_aov))} to {kit.rupees(round(need['aov']))}",
                    f"{kit.rupees(round(need['aov'] - c_aov))} more on every order", "items and prices are not in this file"),
                   ("D. price", "15 percent higher prices", "every price up, with nobody leaving",
                    "none, and nothing may sell above its printed maximum retail price")],
                  caption=f"The 15 percent plan on the consumer view: {kit.rupees(c_rev)} to {kit.rupees(int(plan + 0.5))}")
        kit.driver_tree({"label": "the plan", "note": f"{kit.rupees(c_rev)} to {kit.rupees(int(plan + 0.5))}",
                         "kind": "known", "children": [
            {"label": "customers", "note": "15 percent more, new people", "kind": "unknown"},
            {"label": "orders per customer", "note": f"15 percent more; {c_cust - c_once} already came back", "kind": "lit"},
            {"label": "order value", "note": f"{kit.rupees(round(c_aov))} to {kit.rupees(round(need['aov']))}", "kind": "unknown"}]},
            title="What the plan asks of each branch alone, on the consumer view")
        """),
        code("""
        kit.check("customers alone reach the plan through the tree", abs(need["customers"] * c_per * c_aov - plan) < 1)
        kit.check("orders alone reach the plan through the tree", abs(need["orders"] * c_aov - plan) < 1)
        kit.check("order value alone reaches the plan through the tree", abs(c_orders * need["aov"] - plan) < 1)
        """),
        md("""
        **What happened.** The answer is b. Every branch alone has to rise 15 percent, so what separates
        them is who is asked and what the file shows. Acquisition has to find 15 percent more customers
        Kalpa has never met. Frequency asks about three in ten of the consumer one-time buyers to come
        back once, at the consumer view's mean order of Rs 2,235, and 7 customers already did. Order
        value needs Rs 335 more on every order and price needs every price 15 percent higher with nobody
        leaving, and the file holds neither the items nor the prices that would show how.
        """),
        md("""
        **The best-fit call.** B, frequency first: the customers exist, the file shows some of them
        return, and a retention test costs a reminder or an offer to people already on the list, where
        acquisition pays marketing to find new ones. **What would change it:** a second quarter showing
        customers falling while frequency held, or a retained order costing more than a new customer;
        the last section says which.
        """),
        md("""
        ## 1. Which branch has evidence behind it?

        The file's evidence for a branch is customers already doing what the branch asks. For frequency
        that is customers who bought more than once in the quarter; for acquisition it would be
        customers falling from one quarter to the next, which one quarter cannot show.

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
        kit.check("every customer either bought once or came back", once + (customers - once) == 23)
        """),
        md("""
        **What happened.** The answer is c: 16 of the 23 customers bought once and 7 came back, so
        frequency is the branch with evidence behind it, and each of the 16 is one order away from
        moving it.
        """),
        md("""
        ## 2. What goes wrong when two 10 percent lifts are called 20 percent?

        The marketing lead answers the frequency case with a bigger plan: "Fund acquisition and a
        retention programme together. A 10 percent lift in customers and a 10 percent lift in orders per
        customer make 20 percent growth, well over the 15 percent plan." The rupees below stay on the
        consumer view, the base the plan is sized on.

        **Predict before you run.** What do the two lifts really make?

        - a) 20 percent, as the slide says.
        - b) 21 percent.
        - c) 10 percent, since the lifts overlap.
        - d) 11 percent.

        **The plausible wrong answer.**
        """),
        code("""
        added = c_rev * (1 + 0.10 + 0.10)                     # the consumer view, as the plan is sized
        print(f"Consumer revenue after both lifts: {kit.rupees(round(added))}, growth 20 percent")
        """),
        md("""
        **Why it is wrong.** The branches multiply, so the lifts multiply: the second lift applies to a
        customer base that is already 10 percent larger. Adding them drops the lift on the lift, and at
        bigger or more numerous lifts the gap grows until a budget sized by addition misses its target.
        The check recomputes revenue leaf by leaf through the tree.
        """),
        code("""
        through_tree = (c_cust * 1.10) * (c_per * 1.10) * c_aov
        print(f"through the tree: {kit.rupees(round(through_tree))}, growth {through_tree / c_rev - 1:.0%}; "
              f"the slide's figure {kit.rupees(round(added))}, short by {kit.rupees(round(through_tree - added))}")
        lifts = [0.10, 0.20, 0.30]
        kit.columns([f"two {int(l * 100)}% lifts" for l in lifts],
                    [("added, the slide", [2 * l * 100 for l in lifts]),
                     ("multiplied, the tree", [((1 + l) ** 2 - 1) * 100 for l in lifts])],
                    fmt=lambda v: f"{v:.0f}%", title="Added against multiplied: the gap grows with the lift")
        kit.check("through the tree, two 10 percent lifts make 21 percent", round(through_tree / c_rev - 1, 2) == 0.21)
        kit.check("the added figure is Rs 77,772", round(added) == 77772)
        kit.check("the tree's figure is Rs 78,420", round(through_tree) == 78420)
        """),
        md("""
        **What happened.** The answer is b: the two lifts make 21 percent, Rs 78,420, which is Rs 648
        above the slide's Rs 77,772. At 10 percent the gap is small; two 30 percent lifts make 69
        percent where the slide would say 60. The same rule prices a discount: 15 percent off with 10
        percent more orders is 0.85 x 1.10 = 0.935, a 6.5 percent fall that addition would call a 5
        percent fall.
        """),
        md("""
        ## Does adding the lift piece by piece land on the same total?

        Revenue after both lifts is the base, plus the customer lift, plus the frequency lift, plus the
        lift on the lift, which is 1 percent of the base. A bridge built from those four parts must land
        where the multiplication did.
        """),
        code("""
        parts = [("customers +10 percent", c_rev * 0.10), ("orders per customer +10 percent", c_rev * 0.10),
                 ("the lift on the lift, 0.10 x 0.10", c_rev * 0.01)]
        kit.bridge(("consumer view, this quarter", c_rev), [(n, round(v)) for n, v in parts],
                   end_label="after both lifts", lit=(2,), lo=60000,
                   title="The two lifts as parts (the axis starts at Rs 60,000)")
        kit.check("the parts land on the multiplied total", abs(c_rev + sum(v for _, v in parts) - through_tree) < 1e-6)
        """),
        md("""
        **What happened.** It does: Rs 64,810, plus Rs 6,481 for customers, plus Rs 6,481 for
        frequency, plus Rs 648 for the lift on the lift, lands on Rs 78,420, where the multiplication
        did.
        """),
        md("""
        **When to switch.** Multiply the factors when you need the total; build the parts when someone
        asks where the extra came from, since the bridge shows the lift on the lift as its own bar. The
        parts route is the one to bring to marketing.

        > **Kavya's review.** Recompute through the tree anything someone adds up. Then tell Meera the
        > branch the evidence points at, frequency, and that the lifts multiply whichever she funds.
        """),
        md("""
        ### How would you answer an interviewer who asks which branch to fund first?

        **[D] Marketing wants budget for acquisition; what would you check before agreeing it is the
        right branch, and how would you say no?** "I would count customers by id and see how many came
        back, price what a new customer brings on the mean order of the segments the plan targets, and
        ask for the quarter before this one to see whether customers fell. On Kalpa's quarter
        16 of 23 bought once and 7 came back, and the consumer view's mean order is Rs 2,235 against a
        booked mean of Rs 18,160. The no is a no for now, with a date: frequency is the cheaper branch
        to test, and if Tuesday's two quarters show customers fell, acquisition goes first."

        **[F] A 10 percent lift in customers and a 10 percent lift in frequency make 20 percent growth;
        what is the right number, and when does it matter?** "The right number is 21 percent, because
        branches multiply: 1.10 x 1.10 = 1.21. It matters when the lifts are large or many: two 30 percent lifts make 69
        percent where addition says 60, and a target sized by addition is missed by the difference."

        **[D] Which of four branches would you open first for a retailer, and what would make you
        switch?** "I open the one the evidence says is short and that costs least to test. Here that is
        frequency: the customers exist and a third already came back. I would switch to acquisition if a
        second window showed customers falling with frequency steady, or if retaining an order cost more
        than acquiring a customer."
        """),
        md("""
        ### How far does a 15 percent discount have to lift orders to break even?

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
        ## What would switch the call from frequency to acquisition?

        Two facts would move the call to acquisition: Tuesday's second quarter showing customers falling
        while frequency held, or a retained order costing more than a new customer. Until one of them
        arrives, Meera opens frequency first.

        - Which orders is the plan sized on? It is sized on the consumer view, which booked Rs 64,810,
          so the plan is about Rs 74,532, Rs 9,722 more.
        - What would each branch have to do alone? Each would have to rise 15 percent: 15 percent more
          customers, 15 percent more orders from the same customers, Rs 335 more per order, or prices 15
          percent higher.
        - Which branch has evidence behind it? Frequency has it, since 16 of 23 customers bought once
          and 7 came back.
        - What goes wrong when two lifts are added? The slide's Rs 77,772 (20 percent) falls Rs 648
          short of the tree's Rs 78,420 (21 percent).
        - Does the lift, piece by piece, land on the same total? It does, on Rs 78,420.
        """),
        code("""
        kit.table(["What we now know", "The evidence"],
                  [("The plan asks the same 15 percent of any one branch", "Rs 9,722 more on the consumer view"),
                   ("Frequency is the branch to open first", f"{once} of {customers} bought once; 7 came back"),
                   ("Lifts multiply", "two 10 percent lifts make 21 percent, Rs 78,420")],
                  caption="Chapter 5: which branch first")
        kit.check_summary()
        print("Next: chapter 6 writes the sentence Meera can act on, and its caveat.")
        """),
    ]


# --------------------------------------------------------------------------------- chapter 6
def ch6():
    return [
        md("""
        # What one sentence can Meera sign, with its evidence, its branch, its caveat and its ask?

        **Week 1, Monday, chapter 6 of 6.** Meera will not read the day's notebooks. She needs the answer,
        the evidence and the limit of the evidence in the time it takes to read one sentence, and
        marketing will read the same sentence looking for the weakest number in it.

        **Who needs the answer.** Meera signs the sentence, Kavya reviews it first, and the marketing
        lead reads it for the number to attack. A sentence that says "70 percent of customers are lost"
        either panics the room or hands marketing an easy rebuttal, and the team loses the trust the
        week depends on.

        **The questions on the way.**

        1. Which form carries the decision in the time Meera has?
        2. What does the first draft of the sentence say?
        3. How many of the 16 one-time buyers are really lost?
        4. Does counting forward from each order find the same buyers too recent to judge?
        5. What does the sentence Meera signs say?

        The metric at stake is the repeat picture: who came back, who has not, and who has not had time
        to. Klarna reported that its AI assistant handled two-thirds of customer-service chats in its
        first month (Klarna, 27 February 2024); fifteen months later its chief executive said the focus
        on cost had lowered quality (Fortune, 9 May 2025). Meera's sentence carries a caveat so that
        one window's number is not taken as the verdict. Section 5 of the retail dossier,
        `study-notes/C2_W01_D01_domain_retail_STUDENT.md`, covers retention and cohorts, and its section
        8 tells Klarna's case in full.

        Chapter 5 chose frequency first: 16 of 23 customers bought once and 7 came back, and two 10
        percent lifts make 21 percent where the slide said 20. This chapter turns that into the sentence
        and tests the one number in it most likely to be misread.

        > **Kavya's review.** One sentence, four parts in this order: the evidence with its window, the
        > branch, what the window cannot show, and what happens to the Rs 12 crore.
        """),
        md("""
        **Setup.** The first cell finds the shared helper, loads the 30 orders from `../data/`, applies
        chapter 1's `int()` fix, and groups each customer's order dates.
        """),
        code(LOAD + '''
from datetime import date
for order in ORDERS:
    order["amount"] = int(order["amount"])     # chapter 1's fix for an amount stored as text
start = date.fromisoformat(min(o["order_date"] for o in ORDERS))
end = date.fromisoformat(max(o["order_date"] for o in ORDERS))
by_customer = {}
for order in ORDERS:
    by_customer.setdefault(order["customer_id"], []).append(date.fromisoformat(order["order_date"]))
customers = len(by_customer)
once_ids = [cid for cid, days in by_customer.items() if len(days) == 1]
print(f"{len(ORDERS)} orders from {start} to {end}, {(end - start).days + 1} days; {customers} customers, {len(once_ids)} bought once")
'''),
        where(6, ["Which form carries it?", "1. What does the draft say?",
                  "2. How many are really lost?", "Does counting forward agree?",
                  "What does Meera sign?"]),
        md("""
        ## Which form carries the decision in the time Meera has?

        There are four ways to hand Meera the answer, sized in the reader's time and in what can go
        wrong.

        | Option | Her reading time | The decision it carries | How it gets misread |
        |---|---|---|---|
        | A. One number: "orders per customer, 1.30" | two seconds | It carries none, and she has to supply it. | She reads it as good or bad news with no benchmark. |
        | B. The tree as a table of every leaf | a minute or more | It carries none, and she draws the conclusion. | She picks the number that suits the room. |
        | C. One sentence: evidence, branch, caveat, the ask | about twenty seconds | It carries the call: open frequency and hold the budget until Tuesday. | It is misread only if a number in it is, which the trap below tests. |
        | D. A dashboard refreshed every week | weeks to build | It carries whatever she looks at. | A chart with no denominator misleads her. |
        """),
        code("""
        reading = [("A. one number", 2), ("C. one sentence", 20), ("B. the tree as a table", 60)]
        kit.bars(reading, fmt=lambda v: f"{v} s", lit=(1,),
                 title="Seconds Meera spends reading each option (D is weeks to build before she reads it)")
        kit.check("the sentence is the one option that carries a decision inside half a minute",
                  [n for n, t in reading if t <= 30 and n.startswith("C")] == ["C. one sentence"])
        """),
        md("""
        **The best-fit call.** C: one sentence, read in about twenty seconds, is the only option that
        carries a decision and its limit together. **What would change it:** when the question becomes
        weekly, as it does when Meera's chief of staff asks for the leadership deck in Week 2, D earns
        its build cost, with C as its headline.
        """),
        md("""
        ## 1. What does the first draft of the sentence say?

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
        **What happened.** The answer is b: the draft puts the evidence first, then the branch and the
        limit, and ends on the Rs 12 crore, the ask Meera acts on. It reads 23 customers at 1.30 orders
        each, a typical order of Rs 2,205, and 16 who bought only once, and that 16 is the number
        marketing will reach for.
        """),
        md("""
        ## 2. How many of the 16 one-time buyers are really lost?

        A colleague tightens the draft for the slide, and the 16 becomes a percentage.

        **Predict before you run.** 16 of the 23 customers bought only once in the quarter. How many of
        them can you say are lost?

        - a) All 16, about 70 percent of the customers.
        - b) None, since every one of them might still return.
        - c) Only those past the usual gap between orders.
        - d) Seven, the same as those who came back.

        **The plausible wrong answer.**
        """),
        code("""
        lost_share = len(once_ids) / customers
        print(f"{len(once_ids)} of {customers} customers never came back: {lost_share:.0%} of customers are lost")
        """),
        md("""
        **Why it is wrong.** A customer who bought on 19 September had seven days to come back before the
        extract ends. The file shows who bought once inside the window, and whether they are lost
        depends on orders placed after it closes, which the file cannot show. Sent to Meera, 70 percent
        churn makes retention look like an emergency on a number marketing can knock down with one
        question: how long do our customers usually take to come back? The check asks that question of
        the 7 who did.
        """),
        code("""
        gaps = sorted((max(d) - min(d)).days for d in by_customer.values() if len(d) > 1)
        typical_gap = gaps[len(gaps) // 2]
        too_recent = [cid for cid in once_ids if (end - by_customer[cid][0]).days < typical_gap]
        had_time = len(once_ids) - len(too_recent)
        kit.strip(gaps, markers=[("median gap", typical_gap, "bad")], lo=0, hi=90, fmt=lambda v: f"{v:g} days",
                  title="Days between a returning customer's first and second order")
        kit.bars([("came back", came_back), ("once, past the usual gap", had_time),
                  ("once, too recent to judge", len(too_recent))], lit=(2,),
                 title="The 23 customers, with the window's edge taken into account")
        kit.check("the median gap between two orders is 45 days", typical_gap == 45, gaps)
        kit.check("9 of the 16 one-time buyers bought fewer than 45 days before the end", len(too_recent) == 9)
        kit.check("7 came back, 7 past the usual gap, 9 are too recent",
                  (came_back, had_time, len(too_recent)) == (7, 7, 9))
        """),
        md("""
        **What happened.** The answer is c: at most 7 of the 16 can be called lost, the ones past the
        usual gap. The 7 who came back took a median of 45 days, and 9 of the 16 one-time buyers ordered
        fewer than 45 days before the window ends, so they have not had a typical customer's time to
        return. The file supports 7 came back, 7 past the usual gap without a second order, and 9 too
        recent to judge, so "70 percent lost" becomes at most 7 of 23. The window also cuts the gap
        short: a customer who took 100 days to
        return could not show up in 88, so 45 days is a floor, and more of the 16 may still be on their
        way back. The sentence replaces the 16 with the split.
        """),
        md("""
        ## Does counting forward from each order find the same buyers too recent to judge?

        The same split comes from the other direction: give each one-time buyer a due date, their order
        date plus the typical gap, and count those whose due date falls after the window ends. The count
        must match the recency route.
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
        **What happened.** It does: counting forward 45 days from each order finds the same 9 buyers
        whose due date falls after 26 September.
        """),
        md("""
        **When to switch.** Recency is the route when you report today's state; due dates are the route
        when you plan follow-ups, since a due date is the day a reminder would go out. Both need the
        gap, and a second quarter would show which of the 9 came back and would see returns slower than
        88 days, so the caveat would shrink.

        > **Kavya's review.** This is a sentence I would take into the room. It says what we know, what
        > we would do, and what we would need before spending Rs 12 crore, and every number in it is one
        > we can defend.
        """),
        md("""
        ### How would you answer an interviewer who asks what one quarter says about lost customers?

        **[D] You have one quarter of orders and 70 percent of customers bought once; what do you tell
        the CEO?** "I tell the CEO that 70 percent bought once in this window, which is a fact, and
        that it is no churn rate. Customers who came back took a median of 45 days, and 9 of the 16 one-time buyers bought
        fewer than 45 days before the extract ends, so they have not had time. I would say 7 came back,
        7 are past the usual gap and 9 are too recent, and add that a one-quarter window only sees short
        gaps, so 45 days is a floor. Then I ask for the prior quarter before calling anyone lost."

        **[F] How do you write a recommendation a stakeholder can act on?** "One sentence in four parts:
        the evidence with its window and definition, the recommendation, what the evidence cannot show,
        and the decision it asks for. Every number comes from the analysis without retyping, and none
        can be recomputed into a different story by the person who disagrees."

        **[D] When would you replace this sentence with a dashboard?** "When the question recurs on a
        schedule and the definitions are settled, so the build cost is paid back every week. Until then
        a sentence with its caveat is faster and harder to misread."
        """),
        md("""
        ### Where else does the window's edge cut a metric short?

        Any count of who has not done something yet is cut short at the end of the window: returns that
        arrive after the window closes, renewals not yet due, orders still in transit when the extract is
        taken. The fix is always
        to measure how long the thing usually takes and hold back judgement on everyone who has not had
        that long.
        """),
        md("""
        ## What does the sentence Meera signs say?

        "On the 30 booked orders from 1 July to 26 September, 23 customers placed 1.30 orders each at a
        typical order of Rs 2,205; 7 came back, 7 are past the usual gap without a second order, and 9
        bought too recently to judge, so I would open frequency before acquisition, and since one
        quarter cannot show which branch moved, hold the Rs 12 crore until Tuesday's two quarters." The
        cell below builds it from the variables, so no number in it can drift from the work.

        - Which form carries the decision? One sentence in four parts carries it, read in about twenty
          seconds.
        - What does the first draft say? It gives the evidence, the branch, the caveat and the ask, with
          16 of 23 who bought once as its weakest number.
        - How many of the 16 are really lost? At most 7 are, the ones past the median gap of 45 days,
          and 9 are too recent to judge.
        - Does counting forward agree? It finds the same 9 customers.
        - What can Meera sign? She can sign the sentence above, with its evidence, its branch, its
          caveat and its ask.
        """),
        code("""
        sentence = (f"On the {len(ORDERS)} booked orders from 1 July to 26 September, {customers} customers placed "
                    f"{per_customer:.2f} orders each at a typical order of {kit.rupees(median)}; {came_back} came back, "
                    f"{had_time} are past the usual gap without a second order, and {len(too_recent)} bought too recently "
                    f"to judge, so I would open frequency before acquisition, and since one quarter cannot show which "
                    f"branch moved, hold the Rs 12 crore until Tuesday's two quarters.")
        print(sentence)
        print(len(sentence.split()), "words")
        kit.check("the sentence splits the one-time buyers", str(len(too_recent)) in sentence and str(had_time) in sentence)
        kit.check("the sentence names what one quarter cannot show", "cannot show" in sentence)
        kit.check("the sentence calls nobody lost", "lost" not in sentence)
        kit.table(["What we now know", "The evidence"],
                  [("One-time buyers are not lost customers", "median repeat gap 45 days; 9 of 16 too recent"),
                   ("The sentence has four parts in a fixed order", f"{len(sentence.split())} words, every number from a variable"),
                   ("The Rs 12 crore waits for a second quarter", "a second quarter would show which branch moved")],
                  caption="Chapter 6: what Meera signs")
        kit.check_summary()
        print("Next: the escalated case asks the same question on the delivered definition, alone.")
        """),
    ]


# ------------------------------------------------------------------------ the escalated case
CASE_ANSWERS = {1: 'order["status"] == "delivered"', 2: "len(set(delivered_ids))",
                3: "len(delivered) / delivered_customers", 4: "amounts[n // 2]",
                5: "amount > mean_order", 6: "len(kept) * 1.15", 7: "0.85 * 1.10",
                8: "days_since < typical_gap", 9: '"frequency"'}
CASE_KEY = "cbdcaabbc"


def case():
    return [
        md("""
        # Does the answer survive on the orders that stayed delivered?

        **Week 1, Monday, afternoon: the escalated case, alone, 35 minutes.** The six chapters answered
        Meera on booked orders. Anand Iyer, the finance controller, has read the draft and pushes back:

        > "Booked includes orders we cancelled and orders that came back. Do it again on what was
        > delivered and stayed delivered, and tell me whether your answer survives."

        **Who needs the answer.** Anand reads the note at the board and checks it against his books,
        which keep what stayed delivered, and Meera signs the recommendation. An answer that holds only
        on booked orders falls apart the first time Anand recomputes it, and the frequency
        recommendation falls with it.

        **The questions on the way.**

        1. How many customers stand behind the delivered orders, and how often did each buy?
        2. What does a typical delivered order look like?
        3. How much more must delivered consumer revenue bring, and what would a discount do to it?
        4. Which branch does Meera open first on delivered orders, once the window's edge is allowed for?
        5. What one sentence does Meera sign on delivered orders?

        The metrics at stake are the chapters' own, rebuilt on the delivered definition: orders per
        customer, the typical order, the plan in rupees and the repeat picture. On the same 30 orders,
        placed from 1 July to 26 September 2026, the chapters found 23 customers at 1.30 orders each, a
        typical (median) order of Rs 2,205, a plan of Rs 9,722 more on the orders of the three consumer
        segments, and, of the 16 one-time buyers, 9 too recent to judge against the median repeat gap of
        45 days, so frequency came first and the Rs 12 crore waits for Tuesday's two quarters. This case
        climbs the same questions on delivered orders, alone.

        > **Kavya's review.** Rebuild it on delivered orders and say what moved and what held. If the
        > branch changes on Anand's definition, Meera needs to know before Thursday.
        """),
        md("""
        TODO ONLY
        Each part carries `TODO` markers. Above each `__TODOn__` placeholder is a lettered choice;
        replace the placeholder with the option you pick, run the cell, then run the check under it.
        Run from the top: the notebook stops at the first placeholder with a `NameError` naming it,
        which is intended.
        """),
        md("""
        SOLUTION ONLY
        Every placeholder is filled with the right option, and the notebook was executed from a fresh
        kernel. Under each part sits why the other options fail. The nine TODO picks, in order, are
        `cbdcaabbc`.
        """),
        md("""
        **Setup.** The first cell finds the shared helper, loads the 30 orders from `../data/`, and
        turns every amount into a whole number with `int()`, the fix chapter 1 found for an amount
        stored as text. `BOOKED` holds what the chapters found on booked orders, so the last table can
        say what moved and what held.
        """),
        code(LOAD + '''
from datetime import date, timedelta
for order in ORDERS:
    order["amount"] = int(order["amount"])     # chapter 1's fix for an amount stored as text
end = date.fromisoformat(max(o["order_date"] for o in ORDERS))
BOOKED = {"orders per customer": 1.30, "typical order": 2205, "too recent": "9 of 16",
          "branch": "frequency"}              # what chapters 3 to 6 found on the 30 booked orders
print(len(ORDERS), "orders loaded; the extract ends on", end)
'''),
        code("""
        kit.side_by_side(
            kit.ladder(["The chapters: is acquisition short?", "The escalated case: does it survive?",
                        "The second case: does channel change it?"], lit=1, show=False),
            kit.vflow(["1. Who stands behind delivered orders?", "2. What is a typical delivered order?",
                       "3. What must delivered revenue bring?", "4. Which branch, at the window's edge?",
                       "5. What does Meera sign?"], show=False),
        )
        """),
        md("""
        ## Part 1. How many customers stand behind the delivered orders, and how often did each buy?

        A finance controller's definition changes every leaf of the tree, and at work the analyst
        recounts the leaves on it before defending a recommendation.

        **Write down:** delivered orders, delivered customers and delivered orders per customer.
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
                   ("orders per customer", f"{BOOKED['orders per customer']:.2f}", f"{delivered_per_customer:.2f}"),
                   ("revenue", "Rs 5,44,810", kit.rupees(delivered_revenue))],
                  caption="The same file on two definitions")
        kit.columns(["orders", "customers"], [("booked", [30, 23]), ("delivered", [len(delivered), delivered_customers])],
                    title="The definition moves every leaf")
        """),
        code("""
        kit.check("21 orders were delivered", len(delivered) == 21, len(delivered))
        kit.check("delivered customers are fewer than delivered orders", delivered_customers < len(delivered))
        kit.check("orders per customer times customers gives back the delivered orders",
                  round(delivered_per_customer * delivered_customers) == len(delivered))
        """),
        md("""
        SOLUTION ONLY
        **Why not the others.** TODO 1: a keeps returns, which did not stay sold; b keeps them on
        purpose, a different definition; d keeps everything. TODO 2: a counts rows; c counts booked
        customers, mixing two definitions in one leaf; d counts orders. TODO 3: a is upside down; b puts
        booked orders over delivered customers; c divides by the booked customer count.

        **What happened.** 19 customers stand behind the 21 delivered orders, 1.11 orders each, with
        Rs 5,20,790 delivered.
        """),
        md("""
        ## Part 2. What does a typical delivered order look like?

        A payback or a pricing case at work quotes a typical order, and it has to be the one the
        definition in use leaves.

        **Write down:** the delivered mean, the delivered median, and the orders above the mean.
        """),
        code("""
        amounts = sorted(o["amount"] for o in delivered)
        n = len(amounts)
        mean_order = sum(amounts) / n
        # TODO 4. Which expression is the median of the sorted list?
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
        kit.stats([(kit.rupees(round(mean_order)), "delivered mean", "every delivered amount / the delivered orders"),
                   (kit.rupees(median_order), "delivered median", "the middle of the sorted list"),
                   (f"{above} of {n}", "above the mean", "the rest sit below")])
        kit.strip(amounts, markers=[("mean", round(mean_order), "bad"), ("median", median_order, "good")],
                  title="The delivered amounts, with both middles")
        """),
        code("""
        kit.check("the median has as many delivered amounts above it as below it",
                  sum(a > median_order for a in amounts) == sum(a < median_order for a in amounts))
        kit.check("the delivered mean sits more than ten times above the median", mean_order > 10 * median_order)
        kit.check("at most one delivered order in ten sits above the mean", above <= n / 10)
        """),
        md("""
        SOLUTION ONLY
        **Why not the others.** TODO 4: a is the even-count rule, which here averages the 10th and 11th;
        b is one place past the middle; d is the mean. TODO 5: b counts orders above the median, about
        half by construction; c counts everything; d counts the other side.

        **What happened.** The typical delivered order is the median, Rs 2,060; the mean is Rs 24,800,
        with 1 of the 21 orders above it. The mean rose Rs 6,640 from the booked Rs 18,160 and the
        median fell Rs 145, so the typical order held.
        """),
        md("""
        ## Part 3. How much more must delivered consumer revenue bring, and what would a discount do to it?

        At work, every growth plan and every promotion is sized in rupees before anyone funds it. As in
        chapter 5, the plan is sized on the consumer view, the orders in the three consumer segments
        Meera's plan concerns (Retail-Core, Retail-Plus and Student), here kept to the delivered orders.

        **Write down:** the plan on delivered consumer revenue, what frequency alone asks of the same
        customers, and what a 15 percent discount that lifts orders 10 percent does to delivered
        consumer revenue.
        """),
        code("""
        CONSUMER = ("Retail-Core", "Retail-Plus", "Student")        # the segments Meera's plan concerns
        kept = [o for o in delivered if o["segment"] in CONSUMER]    # the delivered consumer view
        kept_revenue = sum(o["amount"] for o in kept)
        kept_customers = len({o["customer_id"] for o in kept})
        plan = kept_revenue * 1.15
        # TODO 6. If only frequency moves, how many delivered consumer orders must the same customers place?
        #   a) len(kept) * 1.15
        #   b) len(kept) + 15
        #   c) len(kept) + 0.15
        #   d) len(set(o["customer_id"] for o in kept)) * 1.15
        needed_orders = __TODO6__
        # TODO 7. A 15 percent discount lifts orders 10 percent. What multiplies delivered revenue?
        #   a) 1 - 0.15 + 0.10
        #   b) 0.85 * 1.10
        #   c) 1.15 * 1.10
        #   d) (1 - 0.15) * (1 - 0.10)
        discount_factor = __TODO7__
        after_discount = kept_revenue * discount_factor
        kit.table(["question", "answer"],
                  [("the plan on delivered consumer revenue",
                    f"{kit.rupees(kept_revenue)} to {kit.rupees(int(plan + 0.5))}, {kit.rupees(int(plan + 0.5) - kept_revenue)} more"),
                   ("orders per customer the plan needs from frequency alone",
                    f"{len(kept) / kept_customers:.2f} to {needed_orders / kept_customers:.2f}, "
                    f"{needed_orders / len(kept) - 1:+.0%} orders from the same customers"),
                   ("delivered consumer revenue after the discount",
                    f"{kit.rupees(round(after_discount))}, {discount_factor - 1:+.1%}")],
                  caption="The plan and the discount on the delivered consumer view")
        kit.bridge(("delivered consumer", kept_revenue),
                   [("price 15 percent lower", -round(kept_revenue * 0.15)),
                    ("orders +10 percent at the lower price", round(kept_revenue * 0.85 * 0.10))],
                   end_label="after the discount", lit=(0,), lo=20000,
                   title="The discount through the tree (the axis starts at Rs 20,000)")
        """),
        code("""
        kit.check("frequency alone reaches the plan", abs(needed_orders * (kept_revenue / len(kept)) - plan) < 1)
        kit.check("the discount lowers delivered consumer revenue", after_discount < kept_revenue)
        kit.check("the discount lands where the bridge's two moves land",
                  abs(after_discount - (kept_revenue - kept_revenue * 0.15 + kept_revenue * 0.85 * 0.10)) < 1)
        """),
        md("""
        SOLUTION ONLY
        **Why not the others.** TODO 6: d is the customers answer; b adds 15 orders, a 75 percent lift;
        c adds 0.15 of an order. TODO 7: a adds the two moves and reads a 5 percent fall where the tree
        gives 6.5; c raises the price; d cuts orders instead of lifting them.

        **What happened.** On the delivered consumer view, Rs 40,790, the plan is Rs 46,909, Rs 6,119
        more. Frequency alone needs 15 percent more delivered orders from the same customers, orders per
        customer from 1.11 to 1.28, and the discount takes the same Rs 40,790 to Rs 38,139, a 6.5
        percent fall.
        """),
        md("""
        ## Part 4. Which branch does Meera open first on delivered orders, once the window's edge is allowed for?

        At work, a retention team calls a customer lapsed only after the usual gap between orders has
        passed. Count the one-time buyers on delivered orders, then hold back the ones too recent to
        judge, using chapter 6's median repeat gap of 45 days, measured on the 7 customers who came back
        on booked orders.

        **Write down:** delivered customers who bought once, how many of them are too recent, and the
        branch.
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
        kit.bars([("kept two orders", delivered_customers - len(once)), ("once, past the gap", len(once) - too_recent),
                  ("once, too recent", too_recent)], lit=(2,), title="Delivered customers, with the window's edge")
        print("open first:", first_branch)
        """),
        code("""
        kit.check("every delivered customer is counted once", len(firsts) == delivered_customers)
        kit.check("the due-date route finds the same too-recent count",
                  too_recent == sum(1 for cid in once if firsts[cid][0] + timedelta(days=typical_gap) > end))
        kit.check("the one-time buyers outnumber the customers who kept two orders",
                  len(once) > delivered_customers - len(once))
        """),
        md("""
        SOLUTION ONLY
        **Why not the others.** TODO 8: a flags the ones who had time; c catches only a same-day order;
        d compares the gap with itself. TODO 9: a is marketing's branch, which one window cannot show
        falling; b and d rest on fields this file lacks, items and prices, and d also leans on a mean
        that sits far above the typical order.

        **What happened.** 17 of the 19 delivered customers kept one order, 7 of them too recent to
        judge, and only 2 kept two orders, so frequency stays first. The delivered view adds a leak: of
        the 7 customers who came back, 4 lost that second order to a cancellation or a return.
        """),
        md("""
        ## Part 5. What one sentence does Meera sign on delivered orders?

        At work, an analysis ends as a sentence a stakeholder can sign. Write one sentence in chapter
        6's four parts, on delivered orders: the evidence with its window and definition, the branch,
        what one quarter cannot show, and what happens to the Rs 12 crore. Say what held from the booked
        answer, and post it as text.
        """),
        md("""
        SOLUTION ONLY
        One sentence that holds: "On the 21 delivered orders from 1 July to 26 September, 19 customers
        kept 1.11 orders each at a typical Rs 2,060, and 17 kept only one, 7 of them too recent to
        judge, so frequency is still the branch to open first, with returns and cancellations on repeat
        orders as the leak to fix; one quarter cannot show which branch moved, so hold the Rs 12 crore
        until Tuesday's two quarters."
        """),
        code("""
        kit.table(["part", "booked (the chapters)", "delivered (this case)", "held?"],
                  [("orders per customer", f"{BOOKED['orders per customer']:.2f}", f"{delivered_per_customer:.2f}",
                    "held" if abs(delivered_per_customer - BOOKED["orders per customer"]) < 0.05 else "moved"),
                   ("typical order", kit.rupees(BOOKED["typical order"]), kit.rupees(median_order),
                    "held" if abs(median_order - BOOKED["typical order"]) < 200 else "moved"),
                   ("one-time buyers too recent to judge", BOOKED["too recent"], f"{too_recent} of {len(once)}",
                    "held" if too_recent > 0 else "moved"),
                   ("branch", BOOKED["branch"], first_branch, "held" if first_branch == BOOKED["branch"] else "moved")],
                  caption="What moved and what held")
        """),
        md("""
        TODO ONLY
        ## What do you post when every part has run?

        Post the two lines the brief asks for (six letters, then three numbers), your sentence to Meera,
        and the nine TODO picks from this notebook in order as one more line. Every check should print
        PASS before you post.
        """),
        md("""
        SOLUTION ONLY
        ## Did Meera's answer survive on the orders that stayed delivered?

        It did. Frequency stays the branch to open first, orders per customer fell from 1.30 to 1.11,
        and the typical order held at Rs 2,060 against Rs 2,205.

        - How many customers stand behind the delivered orders? 19 customers placed the 21 delivered
          orders, 1.11 each, and 2 of them kept two.
        - What does a typical delivered order look like? The median is Rs 2,060, and the mean is
          Rs 24,800 with 1 of the 21 orders above it.
        - How much more must delivered consumer revenue bring? It must bring Rs 6,119 more, from
          Rs 40,790 to Rs 46,909; frequency alone needs 15 percent more orders from the same customers,
          and a 15 percent discount that lifts orders 10 percent takes revenue to Rs 38,139, a 6.5
          percent fall.
        - Which branch comes first, once the window's edge is allowed for? Frequency does: 17 of 19
          kept one order, and 7 of those are too recent to judge.
        - What does Meera sign? She signs the sentence above, with returns and cancellations on repeat
          orders named as the leak to fix.
        """),
        code("""
        kit.check_summary()
        print("Next: the second case asks whether the channel view changes the branch.")
        """),
    ]


# ------------------------------------------------------------------------ the second case
SECOND_ANSWERS = {1: 'channel_revenue[ch] = channel_revenue.get(ch, 0) + order["amount"]',
                  2: 'channel_revenue["store"] / booked_revenue',
                  3: 'status_count[ch][st] = status_count[ch].get(st, 0) + 1',
                  4: 'order["segment"] in CONSUMER',
                  5: 'consumer_status_rev["web"].get("returned", 0)',
                  6: "consumer_revenue",
                  7: '"frequency first, two leaks named"'}
SECOND_KEY = "cbdabca"


def second():
    return [
        md("""
        # Where does revenue come from, by customer type and channel, and does it change the branch?

        **Week 1, Monday, afternoon: the second case, in pairs, 25 minutes.** Meera asked two things at
        the start of the day, and the chapters answered the second, which branch of sales is short.
        This case answers the first on the same 30 orders, placed from 1 July to 26 September 2026, and
        tests whether the channel view changes the recommendation.

        > Meera Raghavan, CEO of Kalpa Retail: "Where does revenue come from, by customer type and
        > channel? Is acquisition even the branch that is short?"
        >
        > Anand Iyer, the finance controller: "No averages. One business customer can move an average."

        **Who needs the answer.** Meera will open the channel slide before she reads the sentence, and
        the store team says they carry the business. A share read without the orders behind it can turn
        the growth plan store-led, and the Rs 12 crore would follow the share.

        **The questions on the way.**

        1. What share of booked revenue does each channel bring?
        2. How many orders stand behind each channel's share, and what are they like?
        3. Which orders does Meera's growth plan concern, and what share of them does each channel hold?
        4. Where does consumer revenue leak between booked and delivered, channel by channel?
        5. How much consumer revenue does each customer type bring?
        6. Does the channel view change the branch Meera opens first?

        The metric at stake is share of revenue: a channel's or a customer type's rupees over the total
        they are part of. Booked revenue counts every order placed, cancellations and returns included,
        and delivered counts what reached a customer and stayed. The chapters found frequency the branch
        to open first, since on the 30 booked orders 16 of 23 customers bought once and 7 came back, and
        the escalated case rebuilt that answer on delivered orders.

        > **Kavya's review.** Meera will open the channel slide before she reads your sentence, and the
        > first thing on it will be store at nine rupees in ten. Decide whether that number changes your
        > answer before she asks, and count the orders behind every share you show her.
        """),
        md("""
        TODO ONLY
        Each step carries a `TODO` marker. Above each `__TODOn__` placeholder is a lettered choice;
        replace the placeholder with the option you pick, run the cell, then run the check under it.
        Run from the top: the notebook stops at the first placeholder with a `NameError` naming it,
        which is intended.
        """),
        md("""
        SOLUTION ONLY
        Every placeholder is filled with the right option, and the notebook was executed from a fresh
        kernel. Under each step sits the reason the other three options fail, and step 1 stages the
        plausible wrong answer with its exact number. The seven TODO picks, in order, are `cbdabca`.
        """),
        md("""
        **Setup.** The first cell finds the shared helper, loads the 30 orders from `../data/`, turns
        every amount into a whole number with `int()`, the fix chapter 1 found for an amount stored as
        text, and sums booked revenue for the shares below.
        """),
        code(LOAD + '''
import statistics
for order in ORDERS:
    order["amount"] = int(order["amount"])     # chapter 1's fix for an amount stored as text
booked_revenue = 0
for order in ORDERS:
    booked_revenue += order["amount"]
channels = ["app", "web", "store"]
print(len(ORDERS), "orders loaded, every amount a whole number; booked revenue", kit.rupees(booked_revenue))
'''),
        code("""
        kit.side_by_side(
            kit.ladder(["The chapters: is acquisition short?", "The escalated case: does it survive?",
                        "The second case: does channel change it?"], lit=2, show=False),
            kit.vflow(["1. What share does each channel bring?", "2. What orders stand behind it?",
                       "3. Which orders does the plan concern?", "4. Where does revenue leak?",
                       "5. What does each customer type bring?", "6. Does the branch change?"], show=False),
        )
        """),
        md("""
        ## Step 1. What share of booked revenue does each channel bring?

        A channel mix review opens most retail operating meetings, and a share is the first number on
        its slide. Add each order's amount to its channel's total, then work out store's share of booked
        revenue.

        **Write down:** each channel's share of booked revenue, and store's in particular.
        """),
        code("""
        channel_revenue = {}
        channel_orders = {}
        for order in ORDERS:
            ch = order["channel"]
            # TODO 1. Which line adds this order's amount to its channel's total?
            #   a) channel_revenue[ch] = order["amount"]
            #   b) channel_revenue[ch] = channel_revenue.get(ch, 0) + 1
            #   c) channel_revenue[ch] = channel_revenue.get(ch, 0) + order["amount"]
            #   d) channel_revenue[ch] = channel_revenue.get(ch, order["amount"]) + order["amount"]
            __TODO1__
            channel_orders[ch] = channel_orders.get(ch, 0) + 1

        # TODO 2. Which expression is store's share of booked revenue?
        #   a) channel_revenue["store"] / len(ORDERS)
        #   b) channel_revenue["store"] / booked_revenue
        #   c) channel_orders["store"] / len(ORDERS)
        #   d) channel_revenue["store"] / channel_revenue["app"]
        store_share = __TODO2__

        total = sum(channel_revenue.values())
        kit.table(["Channel", "Orders", "Share of booked revenue"],
                  [(ch, channel_orders[ch], f"{channel_revenue[ch] / total * 100:.1f}%") for ch in channels],
                  caption="Share of booked revenue by channel, all 30 orders")
        kit.bars([(ch, round(channel_revenue[ch] / total * 1000) / 10) for ch in channels],
                 fmt=lambda v: f"{v:.1f}%", lit=(2,), title="Share of booked revenue by channel, percent")
        """),
        code("""
        kit.check("the channels reconcile to booked revenue", sum(channel_revenue.values()) == booked_revenue)
        kit.check("each channel carries the same number of orders", len(set(channel_orders.values())) == 1,
                  str(channel_orders))
        kit.check("store's share of rupees sits above its share of orders and below one",
                  channel_orders["store"] / len(ORDERS) < store_share < 1, f"{store_share * 100:.1f} percent")
        """),
        md("""
        SOLUTION ONLY
        **Why not the others.** In TODO 1, option a overwrites the total with the latest order; b counts
        orders instead of adding rupees; d starts each channel at its first amount and then adds it
        again, so every channel's first order counts twice. In TODO 2, option a spreads store's rupees
        over all 30 orders; c is store's share of orders, one third; d compares store with app, a ratio
        with no whole behind it.

        **The plausible wrong answer.** "Store brings 91.6 percent of revenue, so the growth plan should
        be store-led."

        **Why it is wrong.** Every channel has 10 orders, yet store's share is nine rupees in ten, so
        store's rupees per order sit far above the other channels'. A share is a total, and a total is a
        count times a mean, so a share can mislead the way a mean can; Anand has already said one
        business customer can move an average. The check is to count the orders behind each share and
        set each channel's mean order beside its median, which step 2 does.
        """),
        md("""
        ## Step 2. How many orders stand behind each channel's share, and what are they like?

        Sales operations teams count the orders behind a share before anyone plans around it, and they
        set a channel's average order beside its typical one. Count each channel's orders by status, then
        set each channel's mean order beside its median.

        **Write down:** each channel's delivered, returned and cancelled counts, and each channel's mean
        and median order.
        """),
        code("""
        status_count = {"app": {}, "web": {}, "store": {}}
        for order in ORDERS:
            ch = order["channel"]
            st = order["status"]
            # TODO 3. Which line counts this order under its channel and its status?
            #   a) status_count[ch] = status_count.get(ch, 0) + 1
            #   b) status_count[st][ch] = status_count[st].get(ch, 0) + 1
            #   c) status_count[ch][st] = status_count[ch].get(st, 0) + order["amount"]
            #   d) status_count[ch][st] = status_count[ch].get(st, 0) + 1
            __TODO3__

        channel_mean = {ch: channel_revenue[ch] / channel_orders[ch] for ch in channels}
        channel_median = {ch: statistics.median([o["amount"] for o in ORDERS if o["channel"] == ch])
                          for ch in channels}
        statuses = ["delivered", "returned", "cancelled"]
        kit.table(["Channel", "Delivered", "Returned", "Cancelled", "Mean order", "Median order"],
                  [(ch, *[status_count[ch].get(st, 0) for st in statuses], kit.rupees(round(channel_mean[ch])),
                    kit.rupees(round(channel_median[ch]))) for ch in channels],
                  caption="The orders behind each channel's share")
        kit.columns(channels, [(st, [status_count[ch].get(st, 0) for ch in channels]) for st in statuses],
                    title="Each channel's 10 orders by status", fmt=lambda v: f"{v:.0f}")
        """),
        code("""
        kit.check("the status counts add back to 30 orders",
                  sum(sum(c.values()) for c in status_count.values()) == len(ORDERS))
        kit.check("every returned order came through one channel",
                  sum(1 for ch in channels if status_count[ch].get("returned", 0) > 0) == 1)
        kit.check("store's mean order is more than ten times its median",
                  channel_mean["store"] > 10 * channel_median["store"],
                  f"{kit.rupees(round(channel_mean['store']))} against {kit.rupees(round(channel_median['store']))}")
        """),
        md("""
        SOLUTION ONLY
        **Why not the others.** Option a counts orders per channel and loses the status; b indexes the
        dictionary by status first, and `status_count["delivered"]` does not exist, so it raises a
        `KeyError`; c adds rupees where the step asks for counts.

        **What happened.** App's 10 orders were all delivered, web delivered 5 and saw 5 returned, and
        store delivered 6 and had 4 cancelled. Every channel has 10 orders, yet store's mean order is
        Rs 49,892 against a median of Rs 2,430, while app's and web's means sit close to their medians:
        store's typical order looks like the other channels' orders, and its total is lifted by orders
        unlike its typical one. Step 3 keeps the orders Meera's plan concerns.
        """),
        md("""
        ## Step 3. Which orders does Meera's growth plan concern, and what share of them does each channel hold?

        An analyst scopes a number to the customers a decision concerns before comparing channels.
        Meera's growth plan concerns Kalpa's three consumer segments, Retail-Core, Retail-Plus and
        Student, since those are the customers a retention offer or an acquisition campaign reaches. The
        consumer view keeps the orders whose segment is one of those three; recompute the channel view on
        it.

        **Write down:** consumer booked revenue, and each channel's consumer revenue and share.
        """),
        code("""
        CONSUMER = ("Retail-Core", "Retail-Plus", "Student")     # the segments Meera's plan concerns
        # TODO 4. Which condition keeps the orders in the three consumer segments Meera's plan concerns?
        #   a) order["segment"] in CONSUMER
        #   b) order["segment"] == "Retail-Core"
        #   c) order["channel"] != "store"
        #   d) order["status"] != "cancelled"
        consumer = []
        for order in ORDERS:
            if __TODO4__:
                consumer.append(order)

        consumer_revenue = 0
        consumer_channel_rev = {"app": 0, "web": 0, "store": 0}
        for order in consumer:
            consumer_revenue += order["amount"]
            consumer_channel_rev[order["channel"]] += order["amount"]

        kit.table(["Channel", "Consumer revenue", "Share of consumer revenue"],
                  [(ch, kit.rupees(consumer_channel_rev[ch]),
                    f"{consumer_channel_rev[ch] / consumer_revenue * 100:.1f}%") for ch in channels],
                  caption=f"The consumer view: {kit.rupees(consumer_revenue)} booked")
        kit.columns(channels, [("share of all booked revenue", [channel_revenue[ch] / booked_revenue * 100 for ch in channels]),
                               ("share of consumer revenue", [consumer_channel_rev[ch] / consumer_revenue * 100 for ch in channels])],
                    title="Each channel's share before and after the consumer view, in percent", fmt=lambda v: f"{v:.1f}")
        """),
        code("""
        kit.check("the consumer view keeps every order of the three consumer segments and no other",
                  {o["segment"] for o in consumer} <= set(CONSUMER)
                  and all(sum(o["segment"] == s for o in consumer) == sum(o["segment"] == s for o in ORDERS)
                          for s in CONSUMER))
        kit.check("the consumer channels reconcile to consumer revenue",
                  sum(consumer_channel_rev.values()) == consumer_revenue, kit.rupees(consumer_revenue))
        kit.check("on the consumer view store no longer leads",
                  consumer_channel_rev["store"] < max(consumer_channel_rev.values()))
        """),
        md("""
        SOLUTION ONLY
        **Why not the others.** Option b keeps one consumer segment and drops the other two; c drops
        every store order, the consumer ones with it; d applies a status definition, which answers a
        different question and keeps orders outside the three segments.

        **What happened.** The consumer view booked Rs 64,810. Web leads it with Rs 27,290 (42.1
        percent), store has Rs 18,920 (29.2 percent) and app Rs 18,600 (28.7 percent). Once the view
        keeps the three consumer segments Meera's plan concerns, store's share falls from 91.6 to 29.2
        percent, so store's headline share came from outside those segments.
        """),
        md("""
        ## Step 4. Where does consumer revenue leak between booked and delivered, channel by channel?

        A returns rate and a cancellation rate by channel are standard lines in an e-commerce operating
        review. Booked is what customers asked for and delivered is what stayed sold, so split each
        channel's consumer revenue by status and find where it leaks.

        **Write down:** web's returned revenue, store's cancelled revenue, and consumer delivered revenue.
        """),
        code("""
        consumer_status_rev = {"app": {}, "web": {}, "store": {}}
        for order in consumer:
            ch = order["channel"]
            st = order["status"]
            consumer_status_rev[ch][st] = consumer_status_rev[ch].get(st, 0) + order["amount"]

        # TODO 5. Which number is web's leak, the booked revenue that came back?
        #   a) consumer_status_rev["web"].get("delivered", 0)
        #   b) consumer_status_rev["web"].get("returned", 0)
        #   c) consumer_status_rev["store"].get("returned", 0)
        #   d) consumer_channel_rev["web"] - consumer_status_rev["web"].get("returned", 0)
        web_leak = __TODO5__
        store_leak = consumer_status_rev["store"].get("cancelled", 0)
        consumer_delivered = 0
        for ch in channels:
            consumer_delivered += consumer_status_rev[ch].get("delivered", 0)

        kit.table(["Channel", "Delivered", "Returned", "Cancelled"],
                  [(ch, *[kit.rupees(consumer_status_rev[ch].get(st, 0)) for st in statuses]) for ch in channels],
                  caption="Consumer revenue by channel and status")
        kit.columns(channels, [("booked", [consumer_channel_rev[ch] for ch in channels]),
                               ("delivered", [consumer_status_rev[ch].get("delivered", 0) for ch in channels])],
                    title="Consumer revenue by channel, booked against delivered", fmt=kit.rupees)
        kit.bridge(("consumer booked", consumer_revenue),
                   [("web returns", -web_leak), ("store cancellations", -store_leak)],
                   end_label="consumer delivered", lit=(0, 1),
                   title="Where consumer revenue leaks between booked and delivered")
        """),
        code("""
        kit.check("booked less the two leaks lands on delivered",
                  consumer_revenue - web_leak - store_leak == consumer_delivered, kit.rupees(consumer_delivered))
        kit.check("app delivered every rupee it booked",
                  consumer_status_rev["app"].get("delivered", 0) == consumer_channel_rev["app"])
        kit.check("web lost more than a third of its booked revenue to returns",
                  web_leak > consumer_channel_rev["web"] / 3, kit.rupees(web_leak))
        """),
        md("""
        SOLUTION ONLY
        **Why not the others.** Option a is what web kept; c looks for returns in store, which has none;
        d is web's booked revenue less its returns, which is again what web kept.

        **What happened.** Web booked Rs 27,290, and Rs 14,970 of it, 54.9 percent, came back as
        returns, leaving Rs 12,320 delivered. Store's consumer orders booked Rs 18,920, and its
        cancellations took Rs 9,050, 47.8 percent, leaving Rs 9,870 delivered. App booked Rs 18,600 and
        delivered all of it. Consumer delivered revenue is Rs 40,790.
        """),
        md("""
        ## Step 5. How much consumer revenue does each customer type bring?

        Segment reporting is how the head of a membership tier sees what the tier earns. Meera asked
        about customer type, and the segment is recorded on each order, so this step stays at revenue by
        segment: one repeat customer appears once as Retail-Core and once as Retail-Plus, and a count of
        customers per segment would count that customer twice.

        **Write down:** each consumer segment's revenue, its share of consumer revenue and its revenue
        per order.
        """),
        code("""
        segment_rev, segment_delivered, segment_orders = {}, {}, {}
        for order in consumer:
            seg = order["segment"]
            segment_rev[seg] = segment_rev.get(seg, 0) + order["amount"]
            segment_orders[seg] = segment_orders.get(seg, 0) + 1
            if order["status"] == "delivered":
                segment_delivered[seg] = segment_delivered.get(seg, 0) + order["amount"]

        # TODO 6. Which total is the denominator for a segment's share of consumer revenue?
        #   a) booked_revenue
        #   b) len(consumer)
        #   c) consumer_revenue
        #   d) segment_rev["Retail-Core"]
        denominator = __TODO6__

        segments = list(CONSUMER)
        kit.table(["Customer type", "Booked revenue", "Share of consumer revenue", "Revenue per order", "Delivered revenue"],
                  [(seg, kit.rupees(segment_rev[seg]), f"{segment_rev[seg] / denominator * 100:.1f}%",
                    kit.rupees(round(segment_rev[seg] / segment_orders[seg])), kit.rupees(segment_delivered.get(seg, 0)))
                   for seg in segments],
                  caption="Consumer revenue by customer type, recorded on each order")
        kit.columns(segments, [("booked", [segment_rev[seg] for seg in segments]),
                               ("delivered", [segment_delivered.get(seg, 0) for seg in segments])],
                    title="Consumer revenue by customer type, booked against delivered", fmt=kit.rupees)
        """),
        code("""
        kit.check("the three consumer segments reconcile to consumer revenue",
                  sum(segment_rev.values()) == consumer_revenue, kit.rupees(sum(segment_rev.values())))
        kit.check("the shares of consumer revenue add to one",
                  abs(sum(segment_rev[s] / denominator for s in segments) - 1) < 1e-9)
        kit.check("each customer type delivered no more than it booked",
                  all(segment_delivered.get(s, 0) <= segment_rev[s] for s in segments))
        """),
        md("""
        SOLUTION ONLY
        **Why not the others.** Option a divides by all booked revenue, which includes orders outside
        the three consumer segments, so the three shares add to about 12 percent; b divides rupees by a
        count of orders, which gives rupees per order; d indexes every segment to Retail-Core, so
        Retail-Core reads 100 percent.

        **What happened.** Retail-Core booked Rs 32,650 (50.4 percent of consumer revenue), Retail-Plus
        Rs 27,320 (42.2 percent) and Student Rs 4,840 (7.5 percent). Retail-Plus, the paid tier, brings
        the most per order, Rs 2,732, and Rs 9,160 of its booked revenue, a third, came back as returns,
        which is a question for the head of Retail-Plus on Tuesday.
        """),
        md("""
        ## Step 6. Does the channel view change the branch Meera opens first?

        A recommendation is tested against each new cut of the data before it reaches the board. The
        chapters and the escalated case said open frequency first; weigh that against what the channel
        view found.
        """),
        code("""
        # TODO 7. What does the channel view do to the recommendation?
        #   a) "frequency first, two leaks named"
        #   b) "store-led, since store brings 91.6 percent"
        #   c) "web-led"
        #   d) "acquisition first"
        verdict = __TODO7__
        print("the recommendation:", verdict)
        kit.flow([f"store: {store_share * 100:.1f} percent of all booked rupees",
                  f"store's mean order: {channel_mean['store'] / channel_median['store']:.0f} times its median",
                  f"consumer view: store {consumer_channel_rev['store'] / consumer_revenue * 100:.1f} percent",
                  "web returns, store cancellations", "the recommendation: " + verdict],
                 kinds=["bad", "unknown", "known", "known", "lit"],
                 title="From store's headline share to the recommendation")
        """),
        code("""
        kit.check("no channel holds half of consumer revenue", max(consumer_channel_rev.values()) < consumer_revenue / 2)
        kit.check("both leaks carry rupees", web_leak > 0 and store_leak > 0,
                  f"web returns {kit.rupees(web_leak)}, store cancellations {kit.rupees(store_leak)}")
        """),
        md("""
        SOLUTION ONLY
        **Why not the others.** Option b is the plausible wrong answer of step 1, a share that the
        consumer view takes from 91.6 to 29.2 percent; c reads web's booked lead and ignores that more
        than half of web's booked rupees came back; d moves to the branch the file gave no reason to
        open first.

        **What happened.** The branch recommendation stands: open frequency first. The channel view adds
        two leaks for the note, web returns of Rs 14,970 and store cancellations of Rs 9,050, and app is
        the clean channel, with all of its Rs 18,600 delivered.

        > **Kavya's review.** Good: you counted the orders behind the share before you believed it. The
        > channel slide now carries two leaks with their numbers, and your sentence to Meera does not
        > change.
        """),
        md("""
        TODO ONLY
        ### What will an interviewer ask about channel shares, and how do you answer?

        Answer each aloud in the drill, with this notebook's numbers, then compare with the solution.

        - **[D] One channel carries nine rupees in ten of revenue; does that change where the growth
          plan invests?**
        - **[F] A business says "grow revenue 15 percent"; how do you turn that into questions data can
          answer?**
        """),
        md("""
        SOLUTION ONLY
        ### What will an interviewer ask about channel shares, and how do you answer?

        **[D] One channel carries nine rupees in ten of revenue; does that change where the growth plan
        invests?** First I count the orders behind the share. At Kalpa, store's 91.6 percent of booked
        revenue came from a third of the orders, and once the view keeps the three consumer segments
        Meera's plan concerns, store's share falls to 29.2 percent, Rs 18,920 of Rs 64,810, so store's
        headline share came from outside those segments. The plan still invests on the branch the tree
        points to, frequency, and the channel view adds the leaks to fix: web returns and store
        cancellations.

        **[F] A business says "grow revenue 15 percent"; how do you turn that into questions data can
        answer?** I turn it into counts and ratios. Which revenue, booked, net of cancellations or
        delivered? Over which two windows? Which branch is short: customers, orders per customer or
        revenue per order? What does 15 percent need from one branch alone, which on Kalpa's consumer
        view is 15 percent more customers who buy like today's, or 15 percent more orders from the same
        customers (about three in ten of the consumer one-time buyers returning once), or Rs 335 more
        per order? And which customer types and channels carry the revenue, and where does it leak before
        delivery?
        """),
        code("""
        kit.table(["Step", "What it established"], [
            ("1. by channel", f"store carries {store_share * 100:.1f} percent of booked revenue from a third of the orders"),
            ("2. the orders behind it", f"store's mean order is {kit.rupees(round(channel_mean['store']))} against a median "
                                        f"of {kit.rupees(round(channel_median['store']))}"),
            ("3. the consumer view", f"store holds {kit.rupees(consumer_channel_rev['store'])} of "
                                     f"{kit.rupees(consumer_revenue)}, "
                                     f"{consumer_channel_rev['store'] / consumer_revenue * 100:.1f} percent"),
            ("4. by status", f"web returned {kit.rupees(web_leak)}; store cancelled {kit.rupees(store_leak)}; "
                             f"app delivered all {kit.rupees(consumer_channel_rev['app'])}"),
            ("5. by customer type", f"Retail-Core {kit.rupees(segment_rev['Retail-Core'])}, Retail-Plus "
                                    f"{kit.rupees(segment_rev['Retail-Plus'])}, Student {kit.rupees(segment_rev['Student'])}"),
            ("6. the recommendation", verdict)], caption="What the second case established")
        kit.bars([(ch, consumer_status_rev[ch].get("delivered", 0)) for ch in channels], fmt=kit.rupees,
                 title="What stayed sold: consumer delivered revenue by channel")
        """),
        md("""
        TODO ONLY
        ## What does the pair post when every step has run?

        One post per pair: the brief's line of six letters, then this notebook's seven TODO picks in
        order as a second line, then one sentence answering Meera's channel question. Every check should
        print PASS before you post.
        """),
        md("""
        SOLUTION ONLY
        ## Where does Kalpa's revenue come from, and does the branch hold?

        Store brings 91.6 percent of booked revenue, and once the view keeps the three consumer segments
        Meera's plan concerns, store's share falls to 29.2 percent, so store's headline share came from
        outside those segments; frequency stays the branch to open first, with two leaks named.

        - What share of booked revenue does each channel bring? Store brings 91.6 percent of it from a
          third of the orders.
        - How many orders stand behind each share? Every channel has 10, and store's mean order is
          Rs 49,892 against a median of Rs 2,430.
        - Which orders does the plan concern, and what does each channel hold of them? The three
          consumer segments booked Rs 64,810, of which web holds Rs 27,290 (42.1 percent), store
          Rs 18,920 (29.2 percent) and app Rs 18,600 (28.7 percent).
        - Where does consumer revenue leak? Web returned Rs 14,970 and store cancelled Rs 9,050, so
          Rs 40,790 stayed delivered.
        - What does each customer type bring? Retail-Core brings Rs 32,650 (50.4 percent), Retail-Plus
          Rs 27,320 (42.2 percent) and Student Rs 4,840 (7.5 percent).
        - Does the channel view change the branch? It does not: frequency stays first, with web returns
          and store cancellations named in the note.
        """),
        code("""
        kit.check_summary()
        print("Next: Tuesday puts the quarter before this one beside it, to see which branch moved.")
        """),
    ]


def split_md(cells):
    """One markdown cell per heading, and the call, each result and each trap beat in their own cell."""
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
        twin(NB / "C2_W01_D01_ex2_second_case_STUDENT.ipynb",
             SOL / "C2_W01_D01_ex2_second_case_solution_STUDENT.ipynb", second(), SECOND_ANSWERS)
        print("built the second case twin and solution")


if __name__ == "__main__":
    main(sys.argv[1:])
