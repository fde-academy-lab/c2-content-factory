"""Build Week 2 Wednesday's notebooks: six chapters, the escalated case and the second case.

Run from the repository root, with the warehouse loaded (bash .devcontainer/load_warehouse.sh):
    python3 content/W02/D3/internal/C2_W02_D03_build_notebooks_INTERNAL.py            every notebook
    python3 content/W02/D3/internal/C2_W02_D03_build_notebooks_INTERNAL.py ch3 case   named ones only

Names: ch1 to ch6, case (the escalated case twin and its solution), second (the second case twin
and its solution). Each chapter notebook is executed cold in its own folder by scripts/nb_make.py,
so the saved outputs are the ones a learner sees on GitHub. Every query a chapter runs is a named
block of a .sql file in ../sql/, read at run time, so the notebook and VS Code run the same text.
The TODO twins are written unexecuted and their solution twins executed.

What no saved output may print, because v4 plants it and the room finds it in its own run: any
Retail-Plus count under RANK, DENSE_RANK or whole ties only, the members at or near Retail-Plus's
fiftieth place, the three Retail-Plus members whose spend was planted to fall, any split of the
falling flag by segment, and the bulk order with its member's total. After every build, scan()
reads each written STUDENT notebook for those ids and amounts and stops the build on a hit.
"""
import json
import pathlib
import re
import sys

sys.path.insert(0, "scripts")
from nb_make import SETUP, build, code, empty, md  # noqa: E402,F401

DAY = pathlib.Path("content/W02/D3")
NB = DAY / "notebooks"
SOL = DAY / "exercises" / "solutions"

CHAPTERS = ["Who are the top fifty?", "Top fifty per segment?", "Who makes it at a tie?",
            "Whose spend is falling?", "On track against plan?", "Who does Marketing call?"]

# The planted records and the amounts that would name them, which no learner notebook may print.
FORBIDDEN = ["C-0161", "C-0171", "C-0175", "C-0185", "C-0242", "C-0189", "C-0206",
             "KR-00667", "1,98,57,600", "19857600", "2,08,64,600", "20864600", "3,350", "3350.0",
             "3,480", "3480.0"]

DOSSIER = "content/W01/D1/study-notes/C2_W01_D01_domain_retail_STUDENT.md"

# Each chapter's real company, as checked on the date the provenance records.
COMPANY = {
    1: """**A real company with the same question.** Starbucks Rewards members made 59 percent of the
        money tendered at Starbucks' company-operated US stores in the quarter that ended on 28 June
        2026, and 35.8 million US members were active in the 90 days to that date (Starbucks' card,
        loyalty and mobile dashboard for the third quarter of fiscal 2026, checked 1 October 2026).
        When members carry more than half of the money, a list of which members carry it is the
        first thing a retention offer needs.""",
    2: """**A real company with the same question.** Amazon ranks every product it sells by sales and
        says that the overall rank "doesn't always indicate how well an item is selling in relation
        to similar items", so it also keeps best-seller lists by category and subcategory and shows
        an item's rank within its categories on the product page (Amazon's help page on Best
        Sellers Rank, checked 1 October 2026). India's JEE Advanced does the same with people: each
        category list has its own rank 1, and in 2026 the OBC-NCL rank 1 stood third on the common
        list and the GEN-EWS rank 1 sixth (the JEE Advanced 2026 results release of 1 June 2026,
        checked 1 October 2026).""",
    3: """**A real company with the same question.** American Airlines gives its limited upgrade seats
        to AAdvantage members in a stated order, status tier, then type of upgrade, then Loyalty
        Points earned in the last 12 months, and writes its tiebreaker down in advance: "If the
        upgrade type and 12-month Loyalty Point value are the same, we'll look at the booking code
        then date / time of the request to determine priority" (aa.com, upgrades for status members,
        checked 1 October 2026). That is a hard cap with a stated tiebreaker. Sport shows RANK's
        rule: in the Tokyo 2020 men's high jump final on 1 August 2021, Barshim of Qatar and Tamberi
        of Italy both cleared 2.37 m and shared the gold, and Nedasekau of Belarus, the next
        athlete, was placed third and took the bronze, with no silver awarded (World Athletics
        results, checked 1 October 2026).""",
    4: """**A real company with the same question.** Square, the point-of-sale company, gives its
        sellers a ready-made "Lapsed" group: "customers who were regulars, but haven't visited in
        the last six weeks", where a regular visited three times in the last six months (Square
        Support Center, the page on customer groups and filters, checked 1 October 2026). Each
        customer is judged against their own earlier pattern, which is what Marketing's flag does
        with monthly spend.""",
    5: """**A real company with the same question.** Target's second quarter of 2022 began on 1 May
        2022. On 7 June 2022, about five weeks in, Target said it "now expects its second-quarter
        operating margin rate will be in a range around 2%", down from a range centred on the first
        quarter's 5.3 percent, after markdowns to clear excess inventory (Target's releases of 7
        June and 18 May 2022, checked 1 October 2026). The quarter closed at 1.2 percent (Target's
        release of 17 August 2022). Reading the quarter while it runs is what let Target act before
        it ended.""",
    6: """**A real company with the same question.** Shopify's data team warned merchants that "far
        too often businesses define churn as no purchases after N days", and read a customer's gap
        against that customer's own history: one who bought almost daily and has not been seen in
        months is unlikely to still be active (Cam Davidson-Pilon, "How Shopify Merchants can
        Measure Retention", Shopify Engineering, 14 November 2017, checked 1 October 2026). Hotel
        programmes treated a gap the member did not choose as no reading: Marriott extended elite
        status earned in 2019 until February 2022, and Hilton extended status to 31 March 2022 for
        members set to downgrade in 2020 or 2021 (Marriott's release of 14 April 2020 and Hilton's
        of 27 October 2020, checked 1 October 2026).""",
}

# The setup every notebook runs: the helper, the warehouse, and the named blocks of one .sql file.
WAREHOUSE = SETUP + r'''
import re
from decimal import Decimal
SQL_DIR = kit.data_dir().parent / "sql"

def blocks(stem):
    """Every named block of a .sql file in ../sql/, keyed by the name on its '-- name:' line."""
    text = (SQL_DIR / f"C2_W02_D03_{stem}_STUDENT.sql").read_text(encoding="utf-8")
    parts = re.split(r"^-- name: (\w+)\s*$", text, flags=re.M)
    return {parts[i]: parts[i + 1].strip() for i in range(1, len(parts), 2)}

def num(v):
    """A database number as a Python int or float."""
    if isinstance(v, Decimal):
        return int(v) if v == v.to_integral_value() else float(v)
    return v

def rows(query):
    """Run a query and hand back its rows with every number as a Python number."""
    return [{k: num(v) for k, v in r.items()} for r in kit.sql(query)]

def show(found, caption="", money=(), limit=12):
    """Rows as the kit's table, with the columns named in money set in rupees."""
    if not found:
        kit.table(["result"], [["no rows"]], caption)
        return
    heads = list(found[0])
    def cell(h, v):
        v = num(v)
        if v is None:
            return "NULL"
        if h in money:
            return kit.rupees(v)
        return f"{v:,}" if isinstance(v, int) and abs(v) >= 10000 else str(v)
    body = [[cell(h, r[h]) for h in heads] for r in found[:limit]]
    if len(found) > limit:
        body.append(["..." for _ in heads])
    kit.table(heads, body, caption)

def run(name, caption="", money=(), limit=12, echo=True):
    """Print a named block, run it, show its rows and hand them back."""
    if echo:
        print(Q[name])
    found = rows(Q[name])
    show(found, caption, money, limit)
    return found

def lakh(v):
    """Rupees in lakh, for an axis that has to hold Business and retail members at once."""
    return f"{v / 100000:,.1f} lakh"
'''


def setup(stem, extra=""):
    """The setup cell: the helper, the warehouse, and this chapter's named blocks."""
    return code(WAREHOUSE + f'''
Q = blocks("{stem}")
print(len(Q), "named queries read from", "C2_W02_D03_{stem}_STUDENT.sql;",
      kit.sql("select version()")[0]["version"].split(",")[0])
''' + extra)


def where(n, levels):
    """The day's chapter ladder beside this chapter's steps, the map every notebook opens on."""
    steps = ", ".join(repr(s) for s in levels)
    return code(f'''
        kit.side_by_side(
            kit.ladder({CHAPTERS!r}, lit={n - 1}, show=False),
            kit.vflow([{steps}], lit=0, show=False),
        )''')


def setup_note(stem):
    return md(f"""
        **Setup.** The next cell finds the shared helper, `c2kit`, by walking up from this folder
        until it reaches `scripts/`, connects to the Kalpa warehouse and reads the named queries in
        `../sql/C2_W02_D03_{stem}_STUDENT.sql`. Every query below is a block of that file, so what
        runs here is exactly what runs from VS Code. If no database answers, the error names the
        command that loads the warehouse: `bash .devcontainer/load_warehouse.sh`.
        """)


def twin(path_todo, path_sol, cells, answers):
    """Write the TODO twin unexecuted and the solution executed, from one list of cells.

    A cell's source may hold __TODOn__ placeholders; the solution replaces each with answers[n].
    A cell whose source starts with SOLUTION ONLY is kept in the solution alone, and one starting
    TODO ONLY in the twin alone, with the marker line removed.
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
            filled = re.sub(r"__TODO(\d+)__", lambda m: answers[int(m.group(1))], src)
            sol.append(code(filled) if cell.cell_type == "code" else md(filled))
        else:
            sol.append(cell)
    build(path_todo, [c.copy() for c in todo], execute=False)
    build(path_sol, sol)


def scan(path):
    """Stop the build if a written learner notebook prints a planted record or its amount."""
    text = pathlib.Path(path).read_text(encoding="utf-8")
    hits = [token for token in FORBIDDEN if token in text]
    if hits:
        raise SystemExit(f"{path} names a plant: {', '.join(hits)}")


# ----------------------------------------------------------------------------------- chapter 1
def ch1():
    return [
        md(f"""
        # Which fifty members spent the most in Q2?

        **Week 2, Wednesday. Chapter 1 of 6.** The day climbs one case, Marketing's protect list,
        and this is its first chapter.

        > "Retail-Plus frequency is the problem, so we want to protect our best members before they
        > drift. Give us the top fifty customers by Q2 revenue in each segment, and flag anyone whose
        > monthly spend has fallen for two months running."
        > The marketing lead, Kalpa Retail

        **Who needs the answer.** The marketing lead owns acquisition and campaigns at Kalpa Retail,
        and this quarter's protect budget, a call from the member team and a renewal offer, goes to
        the members this list names. A list built on the wrong unit sends the offer to the wrong
        people: every best member it misses is one nobody called, and every member it repeats is a
        call made twice.

        **The questions on the way.**
        1. Which ways could the team build a ranked list, and what would each cost?
        2. What did each member book in Q2?
        3. Which fifty members spent the most?
        4. What does the quickest list, the fifty biggest orders, give Marketing?
        5. Which segments does the list of fifty members reach?
        6. Does a sort in Python pick the same fifty members?

        **The metric at stake.** Q2 revenue per member: the booked amount of every Q2 order the
        member placed, whatever its status, which is how Monday's suite reached Rs 9,84,00,000 for
        the quarter. Q2 is July to September 2026. A member is one customer on the customers table.
        Kalpa Retail sells to four segments: Business (corporate buyers, whose orders run to
        lakhs), Retail-Core (everyday shoppers), Retail-Plus (the paid membership tier) and Student.
        The retail dossier, `{DOSSIER}`, section 4, has what the head of Retail-Plus watches and
        why a paid tier exists.

        **Where the week left off.** Monday put Week 1's revenue tree on the warehouse, Kalpa's
        Postgres database: Q2 booked Rs 9,84,00,000 on 462 orders from 227 members who bought, and
        Retail-Plus carried the fall, with fewer of its members buying and each ordering less often.
        Tuesday attached payments to orders and kept one rule: a join is only done when its row
        count is explained. Today ranks members on Monday's booked revenue.

        {COMPANY[1]}
        """),
        setup_note("01_top_fifty"),
        setup("01_top_fifty"),
        where(1, ["the options\nfour ways to rank",
                  "one row per member\nwhat each booked",
                  "the fifty\nnumbered in a window",
                  "the quickest list\nthe fifty biggest orders",
                  "who is on it\nsegment by segment",
                  "a second route\na sort in Python"]),
        md("""
        ## The options: which ways could the team build a ranked list, and what would each cost?

        Four ways a team could hand Marketing a ranked list. They differ in what one row of the
        answer is, in what leaves the warehouse, and in how much work the per-segment list Marketing
        actually asked for would take.

        | Option | What one row of the answer is | What leaves the warehouse | Its place on the list | The per-segment list needs |
        |---|---|---|---|---|
        | A. Sort the Q2 order rows and keep fifty | an order | 50 order rows | the row's position on screen | nothing it can do, since an order is not a member |
        | B. Group by member, sort, keep fifty with LIMIT | a member | 50 member rows | the row's position on screen | one query per segment, glued together |
        | C. Group by member, number the members in a window, keep places 1 to 50 | a member, with its place | 50 member rows | a column a later step can count or filter | one more phrase in the same query |
        | D. Export the orders to a spreadsheet and sort by hand | whatever the sort gives | every Q2 order row | typed by hand | four filtered sorts by hand |

        A window function computes a value for each row from related rows and keeps every row,
        where GROUP BY collapses each group to one. `row_number() OVER (ORDER BY q2_revenue DESC)`
        numbers the members from the biggest down.

        **Predict before you run.** For the per-segment list Marketing asked for, how many queries
        does option B need, against option C?

        - a) One each, since both group by member.
        - b) Four for B, one per segment, against one for C.
        - c) Fifty for B, one per place, against one for C.
        - d) None for either, since LIMIT 50 already works per segment.
        """),
        code(r'''
            q2_orders = rows(Q["c1_q2_book"])[0]["orders"]
            segments = rows(Q["c1_segments"])
            per_segment_rows = sum(min(50, s["members_who_bought"]) for s in segments)
            sizing = [("A. sort the orders", 50, "order", "not possible"),
                      ("B. group, sort, LIMIT", 50, "member", f"{len(segments)} queries"),
                      ("C. group, number in a window", 50, "member and place", "1 query"),
                      ("D. export and sort by hand", q2_orders, "order, by hand", f"{len(segments)} sorts by hand")]
            kit.table(["option", "rows that leave the warehouse", "one row is", "per-segment list"],
                      [(o, n, unit, extra) for o, n, unit, extra in sizing],
                      caption=f"Sized on this warehouse: {q2_orders} Q2 orders, {len(segments)} segments, "
                              f"{per_segment_rows} rows in a per-segment list")
            kit.bars([(o, n) for o, n, _, _ in sizing],
                     title="Rows that leave the warehouse for one list of fifty: the export moves every Q2 order",
                     lit=(2,))
            '''),
        md("""
        **What happened.** The answer is b. LIMIT counts rows across the whole result, so option B
        needs one sorted query per segment, four in all, glued together; option C numbers the
        members once and restarts the numbering per segment with one more phrase, which chapter 2
        writes. Option D moves all 462 Q2 order rows out of the warehouse, which the data platform
        lead's rule, "query it, do not export it", rules out, and option A answers in orders.

        **The best-fit call.** Option C. Marketing's real ask is per segment, and the place has to
        be a column that a later step can count and filter, which option B's screen position is
        not. **What would change the call:** if Marketing wanted one overall list to read by eye
        and nothing more, option B is shorter and returns the same fifty members, and the place as
        a column would earn nothing.
        """),
        code(r'''
            kit.check("Q2 holds 462 orders", q2_orders == 462, f"{q2_orders} orders")
            kit.check("four segments bought in Q2", len(segments) == 4, ", ".join(s["segment"] for s in segments))
            kit.check("the export moves more rows than either query", sizing[3][1] > sizing[2][1], f"{sizing[3][1]} against 50")
            '''),
        md("""
        **The day's picture.** GROUP BY keeps one row per group, so it answers how much each group
        booked and keeps nothing below the group. A window keeps every row and adds one column beside
        it, and each of Marketing's three asks needs that column: a member's place, a member's last
        month, and the quarter's total so far.
        """),
        code(r'''
            kit.tree({"label": "rows\none per member", "branches": [
                ("", {"label": "GROUP BY\none row per group", "kind": "known", "branches": [
                    ("", {"label": "how much per group\n4 rows for 4 segments", "kind": "known"})]}),
                ("", {"label": "a window\nevery row kept, one column added", "kind": "lit", "branches": [
                    ("", {"label": "each row beside its neighbours\nits place, its last month, the total so far",
                          "kind": "lit"})]})]},
                title="GROUP BY keeps one row per group; a window keeps every row and adds a column")
            '''),
        md("""
        ## 1. What did each member book in Q2?

        A ranked list of members needs one row per member first. The orders table holds one row per
        order, so the member's Q2 revenue is the sum of their Q2 orders, grouped by member.

        **Predict before you run.** How many rows does one row per member give for Q2?

        - a) 462, one per Q2 order.
        - b) 340, one per member on the customers table.
        - c) 227, one per member who placed a Q2 order.
        - d) 50, the length of Marketing's list.
        """),
        code(r'''
            members = rows(Q["c1_member_spend"])
            print(f"{len(members)} member rows, {sum(m['q2_orders'] for m in members)} orders, "
                  f"{kit.rupees(sum(m['q2_revenue'] for m in members))}")
            run("c1_segments", "Q2 by segment: members who bought, their orders and what they booked",
                money=("q2_revenue",))
            kit.columns([s["segment"] for s in segments],
                        [("Q2 revenue per member who bought, in Rs thousand",
                          [s["q2_revenue"] / s["members_who_bought"] / 1000 for s in segments])],
                        title="A Business member books hundreds of times a retail member's quarter",
                        fmt=lambda v: f"{v:,.1f}")
            '''),
        md("""
        **What happened.** The answer is c: 227 rows, one per member who placed a Q2 order. The
        customers table holds 340 members, and 113 of them bought nothing in Q2, so they have no Q2
        revenue to rank. The 227 rows carry all 462 orders and all Rs 9,84,00,000. A Business
        member booked about Rs 27.9 lakh in the quarter on average, against about Rs 3,800 for a
        Retail-Core member and Rs 5,400 for a Retail-Plus member, and that gap shapes every list
        that ranks the whole book at once.
        """),
        code(r'''
            kit.check("one row per member who bought", len(members) == 227, f"{len(members)} rows")
            kit.check("the member rows carry every Q2 order", sum(m["q2_orders"] for m in members) == 462)
            kit.check("the member rows add back to Q2's Rs 9,84,00,000",
                      sum(m["q2_revenue"] for m in members) == 98400000)
            kit.check("no member appears twice", len({m["customer_id"] for m in members}) == len(members))
            '''),
        md("""
        ## 2. Which fifty members spent the most?

        Option C in full: a named step adds up each member's Q2, a window numbers the members from
        the biggest down, and the outer query keeps places 1 to 50. The customer id after the
        revenue in the window's ORDER BY decides any two members who booked the same, so the
        numbering is the same on every run; chapter 3 asks whether that is fair.

        ```sql
        ranked AS (
            SELECT customer_id, segment, q2_orders, q2_revenue,
                   row_number() OVER (ORDER BY q2_revenue DESC, customer_id) AS position
            FROM   q2_spend
        )
        SELECT ... FROM ranked WHERE position <= 50 ORDER BY position;
        ```

        **Predict before you run.** How many of the four segments will the fifty members come
        from?

        - a) All four, since every segment has big spenders.
        - b) Three.
        - c) Two.
        - d) One, Business.
        """),
        code(r'''
            print(Q["c1_top_fifty"])
            fifty = rows(Q["c1_top_fifty"])
            fifty_b = rows(Q["c1_top_fifty_groupby"])
            by_segment = {}
            for r in fifty:
                by_segment[r["segment"]] = by_segment.get(r["segment"], 0) + 1
            print(f"{len(fifty)} members on the list, places {fifty[0]['position']} to {fifty[-1]['position']}; "
                  f"segments: {by_segment}")
            edge = run("c1_where_business_ends", "Places 33 to 40: where Business ends", money=("q2_revenue",),
                       echo=False)
            kit.bars([(f"{r['position']}. {r['customer_id']} ({r['segment']})", r["q2_revenue"]) for r in edge],
                     title="The last Business members against the first retail ones, Q2 revenue in rupees",
                     fmt=kit.rupees, lit=tuple(i for i, r in enumerate(edge) if r["segment"] != "Business"))
            '''),
        md("""
        **What happened.** The answer is b: three segments. The list holds 35 Business members,
        which is every Business member who bought in Q2, then 11 Retail-Plus and 4 Retail-Core, and
        no Student at all. The last Business member, at place 35, booked Rs 2,25,000; the first
        retail member, at place 36, booked Rs 21,740, about a tenth of it. Ranked across the whole
        book, any Business buyer outranks every retail member.
        """),
        code(r'''
            kit.check("the list holds fifty members", len(fifty) == 50 and len({r["customer_id"] for r in fifty}) == 50)
            kit.check("option B's LIMIT returns the same fifty members",
                      {r["customer_id"] for r in fifty} == {r["customer_id"] for r in fifty_b})
            kit.check("the places run from 1 to 50 with no gap", [r["position"] for r in fifty] == list(range(1, 51)))
            kit.check("every Business buyer is on the list", by_segment.get("Business") == 35, f"{by_segment.get('Business')} of 35")
            '''),
        md("""
        ## 3. What does the quickest list, the fifty biggest orders, give Marketing?

        Under deadline, an analyst reaches for the shortest query that looks like the ask: sort the
        Q2 orders by amount and keep fifty.

        ```sql
        SELECT o.order_id, o.customer_id, c.segment, o.amount
        FROM   orders o JOIN customers c USING (customer_id)
        WHERE  o.quarter = 'Q2'
        ORDER  BY o.amount DESC, o.order_id
        LIMIT  50;
        ```

        **Predict before you run.** How many different members does that list of fifty rows name?

        - a) 50, one per row.
        - b) About 45, since a few members placed two big orders.
        - c) Fewer than 30.
        - d) It cannot be known without reading every row.
        """),
        code(r'''
            hurried = rows(Q["c1_top_orders_check"])[0]
            kit.stats([(hurried["rows_on_the_list"], "rows on the list", "what the report would say it holds"),
                       (hurried["different_members"], "different members", "what Marketing would actually call"),
                       (hurried["segments"], "segment", "Business only")],
                      caption="The plausible wrong answer: the fifty biggest Q2 orders, sent as the top fifty members")
            repeats = rows(Q["c1_top_orders_repeats"])
            kit.bars([(r["customer_id"], r["times_on_the_list"]) for r in repeats],
                     title="Members who take more than one place on the orders list", lit=(0, 1))
            '''),
        md("""
        **The plausible wrong answer.** A list of fifty rows that names only 28 members, every one
        of them Business. Two companies hold five places each, eleven more hold two or three, and
        no Retail-Plus, Retail-Core or Student member appears at all. The answer to the prediction
        is c.

        **Why it is wrong.** One row of the orders table is an order, so a member with five large
        orders takes five places, and a member whose quarter is many smaller orders never shows.
        Marketing would ring 28 companies, two of them five times, and not one member of the tier it
        is worried about.

        **The check that exposes it.** Count the different members on the list and set the count
        beside its rows. A list of members holds as many members as rows; this one holds 28 for 50.

        **The fix, and what it changed.** Add up each member's orders first and rank the members,
        which is section 2's list: 50 rows, 50 members, three segments. The fix reaches 22 more
        members, seven Business members the orders list missed and the 15 retail members it could
        never show.
        """),
        code(r'''
            members_on_member_list = {r["customer_id"] for r in fifty}
            orders_list = rows(Q["c1_top_orders_hurried"])
            members_on_orders_list = {r["customer_id"] for r in orders_list}
            kit.check("the orders list repeats members: fewer members than rows",
                      hurried["different_members"] < hurried["rows_on_the_list"],
                      f"{hurried['different_members']} members for {hurried['rows_on_the_list']} rows")
            kit.check("the member list names one member per row",
                      len(members_on_member_list) == len(fifty) == 50)
            kit.check("every member on the orders list is also on the member list",
                      members_on_orders_list <= members_on_member_list)
            kit.check("the fix reaches 22 more members", len(members_on_member_list - members_on_orders_list) == 22,
                      f"{len(members_on_member_list - members_on_orders_list)} more")
            '''),
        md("""
        ## 4. Which segments does the list of fifty members reach?

        The member list is the right unit. Marketing's ask has one more word in it: "in each
        segment". Count the list by segment, with every segment on the line, including one with
        nobody on the list.

        **Predict before you run.** How many Student members are on the one list of fifty?

        - a) None.
        - b) About five, since Student is about a tenth of the members.
        - c) All twenty Student members who bought.
        - d) Fifty, one list per segment.
        """),
        code(r'''
            reach = run("c1_list_by_segment", "The one list of fifty, counted by segment", echo=False)
            kit.columns([r["segment"] for r in reach],
                        [("on the list of fifty", [r["on_the_list"] for r in reach]),
                         ("members who bought in Q2", [r["members_who_bought"] for r in reach])],
                        title="One list across the book reaches Business in full and Student not at all")
            '''),
        md("""
        **What happened.** The answer is a: no Student member. Business has all 35 of its buyers on
        the list, Retail-Plus 11 of its 76, Retail-Core 4 of its 96 and Student none of its 20. The
        tier Marketing is worried about gets eleven places, because one Business buyer outranks
        every retail member. Marketing asked for fifty in each segment, and that is chapter 2's
        question.
        """),
        code(r'''
            got = {r["segment"]: r["on_the_list"] for r in reach}
            kit.check("the counts add back to fifty", sum(got.values()) == 50, str(got))
            kit.check("the Student line is printed with nobody on it", got.get("Student") == 0)
            kit.check("Retail-Plus holds 11 places of 50", got.get("Retail-Plus") == 11)
            '''),
        md("""
        ## A second route: does a sort in Python pick the same fifty members?

        The second route reaches the list without SQL's GROUP BY or its window: it pulls the 462 Q2
        order rows into Python, adds up each member's rupees in a dictionary, sorts the members by
        revenue and then by id, and keeps fifty. A slip in the window's ORDER BY could not move this
        list, since the two share no code.

        **Predict before you run.** Will Python's fifty match the window's fifty member for member?

        - a) Yes, since both add up the same orders and break a tie by the same id.
        - b) No, since Python sorts text and numbers differently.
        - c) Only the first thirty-five, the Business members.
        - d) Only if the rows arrive sorted from the database.
        """),
        code(r'''
            raw = rows(Q["c1_rows_for_python"])
            spend, segment_of = {}, {}
            for r in raw:
                spend[r["customer_id"]] = spend.get(r["customer_id"], 0) + r["amount"]
                segment_of[r["customer_id"]] = r["segment"]
            py_fifty = sorted(spend, key=lambda cid: (-spend[cid], cid))[:50]
            py_segments = {}
            for cid in py_fifty:
                py_segments[segment_of[cid]] = py_segments.get(segment_of[cid], 0) + 1
            kit.table(["route", "rows read", "members", "Business", "Retail-Plus", "Retail-Core", "Student"],
                      [("SQL window", 462, len(fifty), by_segment.get("Business", 0), by_segment.get("Retail-Plus", 0),
                        by_segment.get("Retail-Core", 0), by_segment.get("Student", 0)),
                       ("Python sort", len(raw), len(py_fifty), py_segments.get("Business", 0),
                        py_segments.get("Retail-Plus", 0), py_segments.get("Retail-Core", 0), py_segments.get("Student", 0))],
                      caption="Two routes, one list")
            '''),
        code(r'''
            kit.check("Python read every Q2 order row", len(raw) == 462)
            kit.check("Python's fifty are the window's fifty", py_fifty == [r["customer_id"] for r in fifty])
            kit.check("Python's segment counts match", py_segments == by_segment)
            '''),
        md("""
        **What happened.** The answer is a. Both routes add up the same 462 orders and break a tie
        by the same id, so they name the same fifty members in the same order, 35 Business, 11
        Retail-Plus and 4 Retail-Core. The Python route moved 462 rows out of the warehouse to reach
        what the query sent back in 50, which is why it is the check and the query is the answer.

        > **Kavya's review.** Say what one row of your list is before you say who is on it. A top
        > fifty of orders and a top fifty of members look alike on screen and send Marketing to
        > different people.

        Kavya Nair is the senior analyst on Kalpa Retail's data team, who checks every number before
        it leaves the team.

        ### In the interview: how is a window different from GROUP BY, and what is one row of your answer?

        **[S] What is the difference between GROUP BY and a window function?** GROUP BY collapses
        each group to one row and can only return what describes the group, such as its sum or its
        count. A window function computes over related rows and keeps every row, so each member
        keeps its own line and gains a column, here its place in the order. A top fifty needs the
        rows kept and numbered, which is a window's job.

        **[F] Marketing asks for the top fifty customers, and your list has fifty rows but only
        twenty-eight names. What happened, and what is your check?** The list ranked order rows, so
        a customer with several big orders took several places. The check is
        `count(DISTINCT customer_id)` beside `count(*)` on the finished list, which must agree on a
        list of customers; the fix is to add up each customer's orders in a named step and rank the
        customers.

        ### Depth: how much of Q2 does the one list of fifty carry?

        Protecting revenue alone would make the overall list look complete, since the fifty members
        on it booked almost all of Q2. The share below is the reason Marketing asked per segment:
        the rupees sit with Business, and the drift Marketing fears sits in Retail-Plus.
        """),
        code(r'''
            carried = sum(r["q2_revenue"] for r in fifty)
            kit.stats([(kit.rupees(carried), "booked by the fifty", "out of Rs 9,84,00,000"),
                       (f"{100 * carried / 98400000:.1f}%", "of Q2", "on 50 of 227 members who bought")],
                      caption="The one list of fifty carries almost all of Q2")
            kit.check("the fifty carry more than 99 percent of Q2", carried / 98400000 > 0.99, f"{100 * carried / 98400000:.2f}%")
            '''),
        md("""
        ## What did this chapter answer?

        1. **Which way, at what cost?** Group by member and number the members in a window, option
           C: fifty member rows leave the warehouse, the place is a column, and the per-segment list
           is one phrase away, where the export would move all 462 Q2 order rows.
        2. **What did each member book?** One row for each of the 227 members who bought, carrying
           all 462 orders and Rs 9,84,00,000.
        3. **Which fifty spent the most?** 35 Business members, every Business buyer, then 11
           Retail-Plus and 4 Retail-Core.
        4. **What does the quickest list give?** Fifty orders naming only 28 members, all Business;
           counting members beside rows catches it, and ranking members fixes it.
        5. **Which segments does the list reach?** Three of four: Retail-Plus holds 11 places and
           Student none.
        6. **Does Python agree?** Yes, member for member, after moving 462 rows to do it.

        Chapter 2 asks the question Marketing actually put: which fifty members lead each segment?
        """),
        code("kit.check_summary()"),
    ]


# ----------------------------------------------------------------------------------- chapter 2
def ch2():
    return [
        md(f"""
        # Which fifty members lead each of the four segments?

        **Week 2, Wednesday. Chapter 2 of 6.** Chapter 1 ranked the whole book; this chapter builds
        the list Marketing asked for, one per segment.

        > "Give us the top fifty customers by Q2 revenue in each segment."
        > The marketing lead, Kalpa Retail

        **Who needs the answer.** The marketing lead spends each segment's protect budget on that
        segment's own members, and the head of Retail-Plus, the owner of Kalpa's paid membership
        tier, wants his best members called before they drift. A list that hands Retail-Plus a few
        places and Student none leaves the tier Marketing is worried about mostly unprotected, and a
        Retail-Plus member who lapses takes the membership fee and every order after it.

        **The questions on the way.**
        1. Which ways could the team build one list per segment, and what would each cost?
        2. Can GROUP BY return each segment's top fifty?
        3. What does numbering the whole book once give each segment?
        4. What does PARTITION BY restart, and how many members does each list hold?
        5. Does one sorted query per segment pick the same members?

        **The metric at stake.** Q2 revenue per member, the booked amount of every Q2 order the
        member placed whatever its status, as Monday's suite counted Rs 9,84,00,000 for Q2 (July to
        September 2026). Kalpa Retail's four segments are Business (corporate buyers, whose orders
        run to lakhs), Retail-Core (everyday shoppers), Retail-Plus (the paid membership tier) and
        Student; the segment lives on the customer. The retail dossier, `{DOSSIER}`, section 4,
        says what the head of Retail-Plus watches.

        **What chapter 1 found.** Ranked across the whole book, the fifty members who spent most in
        Q2 are 35 Business members, which is every Business buyer, then 11 Retail-Plus and 4
        Retail-Core members, and no Student. The 35th member booked Rs 2,25,000 and the 36th, the
        first retail member, Rs 21,740, so a single list is a Business list. Ranking members needs a
        window function, which numbers rows and keeps every one of them, where GROUP BY collapses
        each group to one row.

        {COMPANY[2]}
        """),
        setup_note("02_each_segment"),
        setup("02_each_segment"),
        where(2, ["the options\nfour ways per segment",
                  "GROUP BY\nwhat it can return",
                  "the whole book numbered\nthen split",
                  "PARTITION BY\nthe numbering restarts",
                  "a second route\none query per segment"]),
        md("""
        ## The options: which ways could the team build one list per segment, and what would each cost?

        | Option | How each segment gets its fifty | Queries to keep | What the database works through | A fifth segment needs |
        |---|---|---|---|---|
        | A. One sorted query per segment, glued with UNION ALL | each query keeps its own segment and its own LIMIT 50 | 4 | the Q2 orders once per query | a fifth query |
        | B. A count of who spent more | a member's place is 1 plus the members of the same segment who booked more | 1 | every pair of members inside a segment | nothing |
        | C. A window with PARTITION BY segment | one numbering that starts again at 1 in each segment | 1 | the Q2 orders once, one sort per segment | nothing |
        | D. GROUP BY segment with LIMIT 50 | one row per segment, so no member is left to list | 1 | the Q2 orders once | it cannot list members at all |

        **Predict before you run.** Option B compares every pair of members inside a segment. How
        many comparisons is that on Q2's 227 members?

        - a) 227, one per member.
        - b) About 1,000.
        - c) About 16,600.
        - d) 51,529, every member against every member.
        """),
        code(r'''
            seg = {r["segment"]: r["members_who_bought"] for r in rows(Q["c2_groupby_segment"])}
            q2_orders = rows("SELECT count(*) AS n FROM orders WHERE quarter = 'Q2'")[0]["n"]
            pairs = sum(n * n for n in seg.values())
            sizing = [("A. a query per segment", len(seg), len(seg) * q2_orders),
                      ("B. count who spent more", 1, pairs),
                      ("C. PARTITION BY segment", 1, q2_orders)]
            kit.table(["option", "queries to keep", "rows or pairs worked through"],
                      [(o, qn, f"{w:,}") for o, qn, w in sizing],
                      caption=f"Sized on Q2: {sum(seg.values())} members in {len(seg)} segments, {q2_orders} orders")
            kit.bars([(o, w) for o, _, w in sizing],
                     title="Rows or member pairs each option works through: counting who spent more grows with the square",
                     lit=(2,))
            '''),
        md("""
        **What happened.** The answer is c: 16,617 comparisons, 35 squared plus 96 squared plus 76
        squared plus 20 squared, because option B sets every member against every member of the
        same segment. Option A reads the 462 Q2 orders four times, 1,848 rows, and needs a fifth
        query the day a fifth segment appears. Option C reads them once and sorts each segment once.
        Option D cannot answer at all, which section 1 shows.

        **The best-fit call.** Option C, PARTITION BY segment: one query, one pass, and a new segment
        needs no change. **What would change the call:** a database with no window functions, such
        as a MySQL server older than version 8.0, the first release line to ship them, which leaves
        option A, four sorted queries glued together.
        """),
        code(r'''
            kit.check("four segments bought in Q2", len(seg) == 4)
            kit.check("counting who spent more needs 16,617 member pairs", pairs == 16617, f"{pairs:,}")
            kit.check("the window reads the orders once, a quarter of option A", sizing[2][2] * 4 == sizing[0][2])
            '''),
        md("""
        ## 1. Can GROUP BY return each segment's top fifty?

        The tool every analyst already knows comes first. Two attempts: group by segment, then group
        by segment and member with LIMIT 50.

        **Predict before you run.** How many rows does `GROUP BY c.segment` return?

        - a) 4.
        - b) 155, fifty or every buyer per segment.
        - c) 200, fifty for each of four segments.
        - d) 50.
        """),
        code(r'''
            first = run("c2_groupby_segment", "Attempt 1: GROUP BY segment", money=("q2_revenue",))
            second = run("c2_groupby_limit", "Attempt 2: GROUP BY segment and member, LIMIT 50, counted by segment")
            kit.columns([r["segment"] for r in first],
                        [("members who bought", [r["members_who_bought"] for r in first]),
                         ("rows attempt 2 returned", [next((s["on_the_list"] for s in second if s["segment"] == r["segment"]), 0)
                                                      for r in first])],
                        title="GROUP BY returns one row per group, and LIMIT counts across the whole result")
            '''),
        md("""
        **What happened.** The answer is a. Attempt 1 returns 4 rows, one per segment, because GROUP
        BY answers how much per group and keeps nothing below the group. Attempt 2 returns 50 rows,
        and they are chapter 1's whole-book list again, 35 Business, 11 Retail-Plus and 4
        Retail-Core, because LIMIT counts rows across the whole sorted result and knows nothing of
        segments. GROUP BY can say how much each segment booked; it cannot say who leads each one.
        """),
        code(r'''
            kit.check("GROUP BY segment returns four rows", len(first) == 4)
            kit.check("LIMIT 50 returns fifty rows across the whole book", sum(r["on_the_list"] for r in second) == 50)
            kit.check("LIMIT 50 leaves Student out", "Student" not in {r["segment"] for r in second})
            '''),
        md("""
        ## 2. What does numbering the whole book once give each segment?

        Chapter 1 already numbered every member from the biggest down. The quickest per-segment
        list reuses that numbering: keep each segment's members whose number is 50 or less.

        ```sql
        row_number() OVER (ORDER BY q2_revenue DESC, customer_id) AS position
        ...
        count(*) FILTER (WHERE position <= 50)   -- per segment
        ```

        **Predict before you run.** How many Retail-Plus members does that give Marketing?

        - a) 50, since Retail-Plus has 76 buyers.
        - b) 76, every Retail-Plus buyer.
        - c) 11.
        - d) 0.
        """),
        code(r'''
            split = run("c2_whole_table_split", "The whole book numbered once, then split by segment")
            kit.columns([r["segment"] for r in split],
                        [("on the segment's list", [r["on_the_segment_list"] for r in split]),
                         ("members who bought", [r["members_who_bought"] for r in split])],
                        title="The plausible wrong answer: Retail-Plus gets 11 places and Student none")
            '''),
        md("""
        **The plausible wrong answer.** Business 35, Retail-Core 4, Retail-Plus 11 and Student 0,
        sent as "the top fifty in each segment". The answer to the prediction is c.

        **Why it is wrong.** The number came from one ranking of the whole book, where every
        Business buyer stands above every retail member, so each retail segment only keeps the
        members who also made the whole book's top fifty. Marketing would protect 11 Retail-Plus
        members, the tier it is worried about, and tell the Student team it has nobody worth a
        call.

        **The check that exposes it.** Each segment's list should hold fifty members, or every buyer
        where the segment has fewer than fifty. Set the count beside the smaller of 50 and the
        segment's buyers: Retail-Plus has 76 buyers and gets 11.
        """),
        code(r'''
            short = [r["segment"] for r in split if r["on_the_segment_list"] != min(50, r["members_who_bought"])]
            kit.check("the check flags the segments whose list is short", set(short) == {"Retail-Core", "Retail-Plus", "Student"},
                      ", ".join(short))
            kit.check("only Business looks right, because all its buyers rank above every retail member",
                      [r["segment"] for r in split if r["segment"] not in short] == ["Business"])
            '''),
        md("""
        ## 3. What does PARTITION BY restart, and how many members does each list hold?

        **The fix.** PARTITION BY segment inside the window's brackets starts the numbering again at
        1 in every segment, so each member's place is a place among its own segment.

        ```sql
        row_number() OVER (PARTITION BY segment
                           ORDER BY q2_revenue DESC, customer_id) AS position
        ```

        **Predict before you run.** How many members do the four lists hold together?

        - a) 200, fifty in each segment.
        - b) 155.
        - c) 50.
        - d) 227, every member who bought.
        """),
        code(r'''
            fixed = run("c2_partitioned", "PARTITION BY segment: the numbering restarts in each segment")
            run("c2_first_three", "The first three places in each consumer segment", money=("q2_revenue",), echo=False)
            kit.columns([r["segment"] for r in fixed],
                        [("on the segment's list", [r["on_the_segment_list"] for r in fixed]),
                         ("members who bought", [r["members_who_bought"] for r in fixed])],
                        title="Each segment's list: fifty, or every buyer where a segment has fewer")
            '''),
        md("""
        **What happened.** The answer is b: 155 members, Business 35, Retail-Core 50, Retail-Plus 50
        and Student 20. Fifty is a cap: Business and Student have fewer than fifty Q2 buyers, so
        their lists hold every buyer. The places restart at 1 in each segment, so Retail-Core's
        first member, C-0010 on Rs 13,910, and Retail-Plus's, C-0170 on Rs 21,740, both stand at
        place 1. The fix moves Retail-Plus from 11 places to 50 and Student from none to 20.

        Writing the place straight into WHERE is the first thing most people try, and Postgres
        refuses it. Run the next cell, read the last line of the error, and give it two minutes.
        """),
        code(r'''
            with kit.expect_error() as err:
                kit.sql(Q["c2_where_error"])
            kit.check("the database refuses a window function inside WHERE", err.name is not None, err.name)
            '''),
        md("""
        WHERE decides which rows exist before any window is computed, so the place does not exist
        yet when WHERE runs. The fix is the shape this chapter already uses: compute the place in a
        named step, then filter on it in the query outside. Monday's drawing of the order a query
        runs in shows why: FROM, WHERE and GROUP BY come before SELECT, where the window lives.
        """),
        code(r'''
            got = {r["segment"]: r["on_the_segment_list"] for r in fixed}
            kit.check("the four lists hold 155 members", sum(got.values()) == 155, str(got))
            kit.check("every list holds fifty or every buyer",
                      all(r["on_the_segment_list"] == min(50, r["members_who_bought"]) for r in fixed))
            kit.check("Retail-Plus goes from 11 places to 50", got["Retail-Plus"] == 50)
            '''),
        md("""
        ## A second route: does one sorted query per segment pick the same members?

        Option A, with no window at all: four queries, one per segment, each sorting its own
        members by Q2 revenue and then by id and keeping fifty, glued together with UNION ALL. Each
        piece sits in brackets so that its ORDER BY and LIMIT apply to it alone. A slip in the
        window's PARTITION BY could not move this list, since the two share no window.

        **Predict before you run.** Will the four queries return the window's 155 members?

        - a) Yes, the same 155 members.
        - b) No, 200 rows, fifty from each query.
        - c) No, since UNION ALL sorts the result again.
        - d) Only the Business and Student members.
        """),
        code(r'''
            union = rows(Q["c2_union"])
            window = rows(Q["c2_window_ids"])
            by_route = {}
            for name, found in (("UNION ALL", union), ("window", window)):
                for r in found:
                    by_route.setdefault(r["segment"], {}).setdefault(name, 0)
                    by_route[r["segment"]][name] += 1
            kit.table(["segment", "four queries, UNION ALL", "one window"],
                      [(s, by_route[s].get("UNION ALL", 0), by_route[s].get("window", 0)) for s in sorted(by_route)],
                      caption="Two routes, the same lists")
            kit.check("the four queries return 155 rows", len(union) == 155)
            kit.check("the two routes name the same members in every segment",
                      {(r["segment"], r["customer_id"]) for r in union} == {(r["segment"], r["customer_id"]) for r in window})
            '''),
        md("""
        **What happened.** The answer is a: 155 rows and the same members in every segment. LIMIT
        keeps at most fifty, so the Business and Student queries return all their buyers, 35 and
        20. The four queries do the job on this warehouse and become four places to edit when the
        segments change, which is why they are the check and the window is the answer.

        > **Kavya's review.** Read the ask's last words again before you rank. "In each segment"
        > is a PARTITION BY, and each segment's list holds fifty members or every buyer, whichever
        > is fewer: count it before it leaves the team.

        ### In the interview: GROUP BY or a window for a top N per group, and why not WHERE?

        **[S] Top three per group: GROUP BY or a window, and why?** A window. GROUP BY collapses
        each group to one row, so it can report the group's total but cannot say which rows lead
        it, and LIMIT counts across the whole result. A window with PARTITION BY the group numbers
        the rows inside each group and keeps them all; a named step computes the place and the
        outer query keeps places 1 to 3.

        **[F] Why can a window function not sit inside WHERE, and what do you do instead?** WHERE
        filters rows before the window is computed, so the place does not exist yet when WHERE runs;
        Postgres stops with "window functions are not allowed in WHERE". You compute the place in a
        CTE or a subquery and filter on it outside.

        ### Depth: how much of each segment's Q2 revenue does its list carry?

        A list of fifty in a segment of 96 buyers can still carry most of the segment's rupees,
        because spend concentrates at the top. The share says how much revenue the protect budget
        covers.
        """),
        code(r'''
            carried = run("c2_list_revenue", "Each list's Q2 revenue against its segment's", money=("list_revenue", "segment_revenue"),
                          echo=False)
            kit.bars([(r["segment"], round(100 * r["list_revenue"] / r["segment_revenue"], 1)) for r in carried],
                     title="Share of each segment's Q2 revenue on its list, percent", fmt=lambda v: f"{v:.1f}%")
            kit.check("Business and Student lists carry their whole segment",
                      all(r["list_revenue"] == r["segment_revenue"] for r in carried if r["segment"] in ("Business", "Student")))
            '''),
        md("""
        Retail-Core's fifty carry 76.1 percent of the segment's Q2 revenue and Retail-Plus's fifty
        carry 85.5 percent, so half the buyers hold three quarters or more of the rupees in both.

        ## What did this chapter answer?

        1. **Which way, at what cost?** PARTITION BY segment: one query reading the 462 Q2 orders
           once, where four glued queries read them four times and counting who spent more works
           through 16,617 member pairs.
        2. **Can GROUP BY do it?** No: it returns 4 rows, one per segment, and LIMIT 50 across the
           book returns chapter 1's list again.
        3. **What does the whole book's numbering give each segment?** Business 35, Retail-Core 4,
           Retail-Plus 11 and Student 0; the check is fifty or every buyer per segment.
        4. **What does PARTITION BY restart?** The numbering, at 1 in every segment: 155 members,
           Business 35, Retail-Core 50, Retail-Plus 50 and Student 20.
        5. **Do four sorted queries agree?** Yes, member for member in every segment.

        Each list was cut at fifty by `row_number()`, with the customer id deciding any two members
        who booked the same. Chapter 3 asks the head of Retail-Plus's question: when two members
        spent the same at the line, who makes the list?
        """),
        code("kit.check_summary()"),
    ]


# ----------------------------------------------------------------------------------- chapter 3
def ch3():
    return [
        md(f"""
        # When two members spent the same at the line, how many does a list ship, and which rule did the head of Retail-Plus ask for?

        **Week 2, Wednesday. Chapter 3 of 6.** Chapter 2 built one list per segment; this chapter
        decides what happens when the fiftieth place is shared.

        > "Ties matter. If two members spent the same, I want them ranked the same, and I want to
        > know how many made the top fifty, not forty-nine because of a tie."
        > The head of Retail-Plus, Kalpa Retail

        **Who needs the answer.** The head of Retail-Plus owns Kalpa's paid membership tier and will
        defend the list to his members and to Marketing. A member left off by a coin toss, with the
        same spend as the member kept, has a fair complaint; a list labelled fifty that carries
        fifty-two has spent two calls nobody planned; a list that drops both members of a tie at the
        line is the forty-nine he has already refused.

        **The questions on the way.**
        1. Which rules could cut a list at fifty, and what does each do at a tie?
        2. What do ROW_NUMBER, RANK and DENSE_RANK give on one tie?
        3. How many rows does each rule ship when two members tie at the line?
        4. How many Retail-Core members does each rule ship?
        5. How many does your own segment's list ship under the head's rule?
        6. Does a count with no window agree with RANK?

        **The metric at stake.** The count of members on each segment's list, beside Q2 revenue per
        member, the booked amount of every Q2 order whatever its status (Q2 is July to September
        2026). Two members tie when their Q2 revenue is the same to the rupee.

        **What chapter 2 found.** PARTITION BY segment gives each segment its own list: 155 members,
        Business 35 and Student 20 (every buyer in both), Retail-Core 50 and Retail-Plus 50. Those
        lists were cut by `row_number()`, with the customer id deciding any two members who booked
        the same, which is the rule this chapter questions.

        {COMPANY[3]}
        """),
        setup_note("03_tie_rule"),
        setup("03_tie_rule"),
        where(3, ["the options\nfour rules at the line",
                  "three functions\none tie, invented",
                  "a tie at the line\ninvented top four",
                  "Retail-Core\nfour counts",
                  "your segment\nyour own run",
                  "a second route\na count with no window"]),
        md("""
        ## The options: which rules could cut a list at fifty, and what does each do at a tie?

        | Rule | At a tie on the line | Meets "ranked the same, and say how many"? | What it costs |
        |---|---|---|---|
        | A. ROW_NUMBER with a stated tiebreaker | one tied member in, one out, decided by the tiebreaker | No: two members who spent the same get different places | a member with the same spend is left off, by a rule the business has to defend |
        | B. RANK | both in, and the next place is skipped: 1, 1, 3 | Yes, and the count says so | the list can run past fifty, and the report has to say why |
        | C. DENSE_RANK | both in, and no place is skipped: 1, 1, 2 | Ties share a place, but its numbers count spend figures, not members | the list can run past fifty even with no tie at the line |
        | D. Whole ties only | a tie that straddles the line is left out whole | Ties share a place, but the list runs short | the forty-nine the head of Retail-Plus refused |

        Whole ties only has no function of its own. `count(*) OVER (PARTITION BY q2_revenue)` gives
        each member the number of members who share their figure, and `rank + tied_with - 1` is the
        last place the tie reaches; the rule keeps a tie only when that place is inside the line.

        **Predict before you run.** On an invented top four where the fourth and fifth members spent
        the same, how many rows does RANK ship?

        - a) 4.
        - b) 5.
        - c) 3.
        - d) 6.
        """),
        code(r'''
            line = run("c3_invented_line", "Invented numbers: a top four where the fourth and fifth members tie")[0]
            kit.bars([("A. row_number", line["row_number_ships"]), ("B. rank", line["rank_ships"]),
                      ("C. dense_rank", line["dense_rank_ships"]), ("D. whole ties only", line["whole_ties_only_ships"])],
                     title="Rows each rule ships for an invented top four with a tie at fourth", lit=(1,))
            '''),
        md("""
        **What happened.** The answer is b: RANK ships 5, because the two members tied at fourth
        share fourth place. ROW_NUMBER ships 4 and leaves one of the pair off by its tiebreaker,
        DENSE_RANK ships 5 here, and whole ties only ships 3, dropping both tied members. The members
        are invented: A to F, on Rs 9,100, 8,800, 8,200, 7,400, 7,400 and 6,900.

        **The best-fit call.** RANK, with the count and its reason in the report. It is the only rule
        that both ranks equal spend equally and never drops a member at the line, and the head of
        Retail-Plus asked for the count. **What would change the call:** a hard cap that cannot
        stretch, such as fifty seats at a members' dinner or fifty gift boxes already packed. Then
        ROW_NUMBER with a tiebreaker the business states in advance, such as more Q2 orders first,
        is honest, as long as the report names who was left off and why.
        """),
        code(r'''
            kit.check("RANK ships five for the invented top four", line["rank_ships"] == 5)
            kit.check("ROW_NUMBER always ships exactly the line", line["row_number_ships"] == 4)
            kit.check("whole ties only runs short", line["whole_ties_only_ships"] == 3)
            '''),
        md("""
        ## 1. What do ROW_NUMBER, RANK and DENSE_RANK give on one tie?

        Six invented members, labelled invented: A and B spent Rs 7,500 each, C Rs 6,000, D and E
        Rs 5,200 each and F Rs 4,100.

        **Predict before you run.** What does RANK give the six, in order?

        - a) 1, 2, 3, 4, 5, 6.
        - b) 1, 1, 3, 4, 4, 6.
        - c) 1, 1, 2, 3, 3, 4.
        - d) 1, 1, 1, 2, 2, 3.
        """),
        code(r'''
            six = run("c3_invented_three", "Invented numbers: three functions on six members with two ties", money=("spend",))
            kit.columns([r["member"] for r in six],
                        [("row_number", [r["row_number"] for r in six]), ("rank", [r["rank"] for r in six]),
                         ("dense_rank", [r["dense_rank"] for r in six])],
                        title="Invented: the three functions on the same six members")
            '''),
        md("""
        **What happened.** The answer is b. ROW_NUMBER gives 1 to 6 and puts A ahead of B only
        because the tiebreaker sorts A first. RANK gives A and B the same 1 and skips 2, so C is
        third, as a race reports a shared first place. DENSE_RANK gives 1, 1, 2, 3, 3, 4: it numbers
        the different spend figures, so it never skips, and by F its number, 4, is two below F's
        place among the members, 6.
        """),
        code(r'''
            kit.check("ROW_NUMBER never repeats a number", [r["row_number"] for r in six] == [1, 2, 3, 4, 5, 6])
            kit.check("RANK repeats a tie and skips after it", [r["rank"] for r in six] == [1, 1, 3, 4, 4, 6])
            kit.check("DENSE_RANK repeats a tie and never skips", [r["dense_rank"] for r in six] == [1, 1, 2, 3, 3, 4])
            kit.check("DENSE_RANK falls two behind the member count after two ties",
                      six[-1]["rank"] - six[-1]["dense_rank"] == 2)
            '''),
        md("""
        ## 2. How many Retail-Core members does each rule ship?

        The same four counts on Kalpa: Retail-Core, the everyday shoppers, has 96 Q2 buyers, so its
        top fifty is a real cut. A hurried analyst reads "ties ranked the same" and reaches for
        DENSE_RANK, since its numbers never skip.

        **Predict before you run.** How many Retail-Core members does DENSE_RANK put on a top-fifty
        list?

        - a) 50.
        - b) 49.
        - c) 51.
        - d) 52.
        """),
        code(r'''
            core = run("c3_core_counts", "Retail-Core: the rows each rule ships")[0]
            kit.bars([("row_number", core["row_number_ships"]), ("rank", core["rank_ships"]),
                      ("dense_rank", core["dense_rank_ships"]), ("whole ties only", core["whole_ties_only_ships"])],
                     title="Retail-Core's top fifty under each rule: DENSE_RANK ships 52", lit=(2,))
            '''),
        md("""
        **The plausible wrong answer.** "DENSE_RANK keeps ties together, so Retail-Core's top fifty is
        these 52 members." The answer to the prediction is d.

        **Why it is wrong.** DENSE_RANK numbers spend figures, and two pairs of members higher up the
        list share a figure, so its numbers run two behind the members. Its fiftieth number lands on
        the 52nd member. The 51st and 52nd members tie with nobody at the line, yet Marketing would
        call them as part of a top fifty, and the head of Retail-Plus would sign a list that
        overstates its own cut.

        **The check that exposes it.** Read the members around fiftieth place with all three
        functions side by side, and list the ties inside the first fifty.
        """),
        code(r'''
            near = run("c3_core_line", "Retail-Core around fiftieth place, three functions side by side", money=("q2_revenue",),
                       echo=False)
            ties = run("c3_core_ties", "The ties inside Retail-Core's first fifty", money=("q2_revenue",), echo=False)
            kit.line([str(r["row_number"]) for r in near],
                     [("rank", [r["rank"] for r in near], "lit"), ("dense_rank", [r["dense_rank"] for r in near], "bad"),
                      ("the line at 50", [50 for _ in near], "plan")],
                     title="Places 46 to 54: dense_rank runs two behind rank and reaches 50 at the 52nd member",
                     fmt=lambda v: f"{v:.0f}", lo=40)
            '''),
        md("""
        **What happened.** Two ties sit inside the list, two members on Rs 4,540 at places 31 and 32,
        and two on Rs 4,120 at places 37 and 38. Each tie costs DENSE_RANK one number, so its 50
        falls on C-0094, the 52nd member, on Rs 2,910. Nobody ties at Retail-Core's line: the
        fiftieth member, C-0005, booked Rs 2,980 and the 51st, C-0092, Rs 2,950.

        **The fix, and what it changed.** RANK, the head's rule, ships 50 for Retail-Core, the same
        fifty as ROW_NUMBER, because no tie straddles the line. The fix takes two members, C-0092 and
        C-0094, off a list they never belonged on. When nobody ties at the line, RANK and ROW_NUMBER
        agree, and the head's rule costs nothing.
        """),
        code(r'''
            kit.check("RANK ships 50 for Retail-Core", core["rank_ships"] == 50)
            kit.check("two ties inside the first fifty, two members each", len(ties) == 4 and all(t["tied_with"] == 2 for t in ties))
            kit.check("DENSE_RANK reaches 50 at the 52nd member",
                      [r["row_number"] for r in near if r["dense_rank"] == 50] == [52])
            kit.check("nobody ties at Retail-Core's fiftieth place",
                      [r["q2_revenue"] for r in near if r["row_number"] == 50] != [r["q2_revenue"] for r in near if r["row_number"] == 51])
            '''),
        md("""
        ## 3. How many does your own segment's list ship under the head's rule?

        **Your turn.** The head of Retail-Plus asked about his own tier. Type these lines into the
        empty cell below and run it. The query is block `c3_your_segment` of the chapter's `.sql`
        file, and it counts the rows each rule ships for Retail-Plus:

        ```python
        mine = rows(Q["c3_your_segment"])[0]
        mine
        ```

        Then write, in one sentence a head of a membership tier would read, how many Retail-Plus
        members his list carries under RANK and, if it is not fifty, why. If your four numbers
        differ, read the members around fiftieth place before you write the sentence: copy block
        `c3_core_line` into a cell and change `'Retail-Core'` to `'Retail-Plus'`.
        """),
        empty(),
        md("""
        **Before you move on.** Your sentence names a count and, when the count is not fifty, the
        members at the line and their figure. If your RANK count and your ROW_NUMBER count differ,
        the difference is the reason a report has to carry its count.

        ## A second route: does a count with no window agree with RANK?

        RANK's count can be reached with no window at all: sort the segment's members by Q2 revenue,
        take the fiftieth member's figure with OFFSET 49, and count every member who booked at least
        that much. A member ties with the fiftieth exactly when they booked the same figure, so the
        count includes every tie at the line, as RANK does.

        **Predict before you run.** For Retail-Core, how many members booked at least the fiftieth
        member's Rs 2,980?

        - a) 49.
        - b) 50.
        - c) 51.
        - d) 52.
        """),
        code(r'''
            second = {r["segment"]: r["at_or_above_fiftieth"] for r in rows(Q["c3_second_route"])}
            counts = {r["segment"]: r["rank_ships"] for r in rows(Q["c3_all_counts"])}
            kit.table(["segment", "members at or above the fiftieth's figure", "RANK's count"],
                      [("Retail-Core", second["Retail-Core"], counts["Retail-Core"])],
                      caption="Retail-Core: two routes to the same count")
            kit.check("the count with no window agrees with RANK for Retail-Core", second["Retail-Core"] == counts["Retail-Core"])
            kit.check("the two routes agree for every segment", all(second[s] == counts[s] for s in counts))
            kit.check("Business and Student ship every buyer under either route",
                      (second["Business"], second["Student"]) == (35, 20))
            '''),
        md("""
        **What happened.** The answer is b: 50 members booked Rs 2,980 or more, which is RANK's
        count, and the two routes agree in every segment, including the one you counted yourself. The
        second route uses a sort and a plain comparison, so a slip in a window's PARTITION BY or ORDER
        BY could not move it.

        > **Kavya's review.** A tie rule is a business decision written as a function name. State
        > the rule, the count it ships and the members at the line in the same sentence, before
        > anybody asks why the list holds more or fewer than fifty.

        ### In the interview: what do the three functions do on a tie, and how long is a top-N list?

        **[S] RANK, DENSE_RANK and ROW_NUMBER on a tie.** ROW_NUMBER gives every row its own number
        and breaks a tie by whatever else the ORDER BY names, or arbitrarily if nothing does. RANK
        gives tied rows the same number and skips the numbers they used up, 1, 1, 3. DENSE_RANK gives
        tied rows the same number without a gap, 1, 1, 2, so it numbers distinct values.

        **[D] The business says "ties rank the same": which function, and how many rows might the
        top-N report ship?** RANK. The report can ship more than N rows when a tie straddles the
        line, so it states the count and the tie; it never ships fewer than N when there are N rows
        to rank. DENSE_RANK can ship more than N even with no tie at the line, because ties higher up
        leave its numbers behind the row count, as Retail-Core's 52 shows. ROW_NUMBER always ships N
        and hides the tie.

        **[F] Your top-ten list came back with eleven rows. What do you tell the stakeholder, and is
        it a bug?** It is the tie rule working: two members share tenth place and the rule the
        stakeholder chose keeps both. I say the count and the reason in the same line, name the two
        members, and offer the hard-cap alternative with the tiebreaker it would need.

        ### Depth: which tiebreaker would you defend under a hard cap?

        Under a hard cap the list ships exactly the line, and the tiebreaker decides who is left
        off, so it has to be a business reason. On the invented top four, D and E tie on Rs 7,400. If
        D placed three Q2 orders and E two (invented too), "more orders first" keeps D, a reason the
        head of a tier built on frequency could defend; "lower customer id first" keeps whoever was
        registered earlier and is no reason at all.
        """),
        code(r'''
            invented = [("A", 9100, 4), ("B", 8800, 2), ("C", 8200, 5), ("D", 7400, 3), ("E", 7400, 2), ("F", 6900, 6)]
            capped = sorted(invented, key=lambda m: (-m[1], -m[2], m[0]))[:4]
            kit.table(["member", "spend, Rs", "Q2 orders", "kept under the cap"],
                      [(m, f"{s:,}", n, "yes" if (m, s, n) in capped else "no") for m, s, n in invented],
                      caption="Invented: a hard cap of four, ties broken by more orders, then by name")
            kit.check("the cap ships exactly four", len(capped) == 4)
            kit.check("more orders first keeps D, who placed three", ("D", 7400, 3) in capped and ("E", 7400, 2) not in capped)
            '''),
        md("""
        ## What did this chapter answer?

        1. **Which rule?** RANK, with its count and reason in the report; ROW_NUMBER with a stated
           tiebreaker only under a hard cap.
        2. **What do the three functions give on one tie?** On six invented members, ROW_NUMBER 1 to
           6, RANK 1, 1, 3, 4, 4, 6 and DENSE_RANK 1, 1, 2, 3, 3, 4.
        3. **How many rows at a tie on the line?** On an invented top four, 4 under ROW_NUMBER, 5
           under RANK, 5 under DENSE_RANK and 3 under whole ties only.
        4. **How many Retail-Core members?** 50 under ROW_NUMBER, RANK and whole ties only; 52 under
           DENSE_RANK, whose numbers run two behind after two ties higher up.
        5. **How many in your own segment?** The count your own run gave, with its reason in your
           sentence.
        6. **Does a count with no window agree?** Yes: the members at or above the fiftieth
           member's figure are RANK's count in every segment, 50 for Retail-Core.

        The protect list now has its rule. Chapter 4 turns to Marketing's second ask: whose monthly
        spend fell two months running?
        """),
        code("kit.check_summary()"),
    ]


# ----------------------------------------------------------------------------------- chapter 4
def ch4():
    return [
        md(f"""
        # Whose monthly spend fell two months running?

        **Week 2, Wednesday. Chapter 4 of 6.** Chapters 1 to 3 built the protect list; this chapter
        answers Marketing's second ask, the flag.

        > "... and flag anyone whose monthly spend has fallen for two months running."
        > The marketing lead, Kalpa Retail

        **Who needs the answer.** The marketing lead's member team will ring each flagged member with
        a retention offer before their buying drifts further. A flag that names the wrong member
        costs a call and tells a loyal customer they are slipping; a fall the flag misses is a member
        nobody rang until they had gone.

        **The questions on the way.**
        1. Which ways could the team set each month beside the month before, and what would each cost?
        2. What did each member spend in each month?
        3. What does LAG put beside one member's months?
        4. What does LAG read when the window has no PARTITION BY?
        5. How many members fell two months running once each member's months are kept apart?
        6. Does a walk through each member's months in Python find the same members?

        **The metric at stake.** Monthly spend: a member's booked revenue in one calendar month,
        every order at its amount whatever its status. The book runs from April to September 2026,
        and the flag reads September, the last month: spend in September below the month before, and
        that month below the one before it. The retail dossier, `{DOSSIER}`, section 5, has how
        often a customer orders and why a membership tier watches it.

        **What chapters 1 to 3 found.** Each segment has its own protect list of fifty members, or
        every buyer where a segment has fewer than fifty, cut by RANK so that members who spent the
        same share a place, as the head of Retail-Plus asked. That list says who matters most; this
        chapter asks whose spend is slipping.

        {COMPANY[4]}
        """),
        setup_note("04_falling_spend"),
        setup("04_falling_spend"),
        where(4, ["the options\nfour ways to compare",
                  "monthly spend\none row per member-month",
                  "LAG\none member's months",
                  "no PARTITION BY\nwhat LAG reads",
                  "with PARTITION BY\nthe flag",
                  "a second route\na walk in Python"]),
        md("""
        ## The options: which ways could the team set each month beside the month before, and what would each cost?

        The flag compares three months of one member. Each option has to put a month's spend beside
        the two before it.

        | Option | How it sets a month beside the one before | Statements | What the database works through | What it has to be told |
        |---|---|---|---|---|
        | A. LAG in a window | reads the row before in the order the window names | 1 | every member-month, once | whose rows belong together and in what order |
        | B. A self-join of the monthly table to itself | joins each month to the same member's month one and two before | 1, with two joins | every member-month matched against the table, twice | the month arithmetic |
        | C. A correlated subquery per month | looks up the month before, row by row | 1 | two lookups for every member-month | the lookup's conditions, twice |
        | D. Months as spreadsheet columns, read by eye | reads across each member's row | none | every member times six months, exported | a person to read every row |

        **Predict before you run.** How many member-months, one row per member per month with an
        order, does the book hold from April to September?

        - a) 1,000, one per order.
        - b) 752.
        - c) 301, one per member who bought.
        - d) 6, one per month.
        """),
        code(r'''
            size = rows(Q["c4_monthly_count"])[0]
            sizing = [("A. LAG in a window", size["member_months"]),
                      ("B. self-join, twice", 2 * size["member_months"]),
                      ("C. two lookups per row", 2 * size["member_months"]),
                      ("D. spreadsheet cells", 6 * size["members"])]
            kit.table(["option", "rows, matches or cells worked through"], [(o, f"{n:,}") for o, n in sizing],
                      caption=f"Sized on this book: {size['member_months']} member-months for {size['members']} members")
            kit.bars(sizing, title="What each option works through: the window reads each member-month once", lit=(0,))
            '''),
        md("""
        **What happened.** The answer is b: 752 member-months for 301 members who bought at least
        once. LAG reads them once; the self-join matches them twice and the correlated subquery looks
        up twice per row, 1,504 each; the spreadsheet holds 1,806 cells for someone to read.

        **The best-fit call.** Option A, LAG in a window: one pass, one statement, and `lag(spend, 2)`
        reaches two months back in the same line as `lag(spend, 1)`. **What would change the call:**
        a database with no window functions, such as a MySQL server older than version 8.0, which
        leaves the self-join, option B.
        """),
        code(r'''
            kit.check("752 member-months for 301 members", (size["member_months"], size["members"]) == (752, 301))
            kit.check("118 members ordered in September, the month the flag reads",
                      size["members_with_a_september_order"] == 118)
            kit.check("the window works through the fewest rows", sizing[0][1] == min(n for _, n in sizing))
            '''),
        md("""
        ## 1. What did each member spend in each month?

        The orders table holds one row per order, so monthly spend is grouped by member and by the
        month each order fell in. `date_trunc('month', order_date)` turns every date into the first
        day of its month, so all of a month's orders share one key.

        **Predict before you run.** Roughly how many members placed an order in each month?

        - a) About 120 a month, steady across the six months.
        - b) About 300, nearly every member every month.
        - c) About 30.
        - d) It halves from April to September.
        """),
        code(r'''
            run("c4_monthly", "The first twelve member-months", money=("spend",))
            buyers = rows(Q["c4_buyers_by_month"])
            kit.columns([str(r["month"])[:7] for r in buyers],
                        [("members who placed an order", [r["members_who_bought"] for r in buyers])],
                        title="Members who bought, month by month: between 118 and 141")
            '''),
        md("""
        **What happened.** The answer is a: between 118 and 141 members bought in each month, from
        141 in April to 118 in September. Each member's months sit on separate rows, one row per
        month with an order, which is the shape LAG reads.
        """),
        code(r'''
            kit.check("between 118 and 141 members bought each month",
                      min(r["members_who_bought"] for r in buyers) == 118 and max(r["members_who_bought"] for r in buyers) == 141)
            kit.check("six months on the book", len(buyers) == 6)
            '''),
        md("""
        ## 2. What does LAG put beside one member's months?

        `lag(spend, 1) OVER (PARTITION BY customer_id ORDER BY month)` puts the previous row's spend
        beside each row, counting rows inside the member's own months in month order, and
        `lag(spend, 2)` reads two rows back. C-0040 of Retail-Core bought in all six months.

        **Predict before you run.** What does `lag(spend, 1)` show on C-0040's first month, April?

        - a) 0.
        - b) NULL, since no row comes before it.
        - c) September's spend, the last row.
        - d) April's own spend.
        """),
        code(r'''
            one = run("c4_one_member", "C-0040's six months, with LAG one and two rows back", money=("spend", "spend_1_back", "spend_2_back"))
            kit.line([str(r["month"])[:7] for r in one], [("C-0040's monthly spend", [r["spend"] for r in one], "lit")],
                     title="C-0040: two falls running into June, then a recovery", fmt=kit.rupees)
            '''),
        md("""
        **What happened.** The answer is b: NULL, since April is the first row of C-0040's months,
        and May shows NULL two rows back for the same reason. June carries May's Rs 3,170 and April's
        Rs 7,980 beside its own Rs 1,320: two falls running, so a flag read at June would fire.
        September's Rs 4,520 is below August's Rs 4,770, but August was above July's Rs 4,260, so the
        flag read at September does not fire for C-0040.
        """),
        code(r'''
            kit.check("the first month has nothing before it", one[0]["spend_1_back"] is None and one[0]["spend_2_back"] is None)
            kit.check("June sits beside May and April", (one[2]["spend_1_back"], one[2]["spend_2_back"]) == (3170, 7980))
            kit.check("C-0040's September is not a second fall", not (one[5]["spend"] < one[5]["spend_1_back"] < one[5]["spend_2_back"]))
            '''),
        md("""
        ## 3. What does LAG read when the window has no PARTITION BY?

        The quickest flag sorts the whole table by member and month and lets LAG run down it:

        ```sql
        lag(spend, 1) OVER (ORDER BY customer_id, month) AS spend_1_back,
        lag(spend, 2) OVER (ORDER BY customer_id, month) AS spend_2_back
        ...
        WHERE month = DATE '2026-09-01' AND spend < spend_1_back AND spend_1_back < spend_2_back
        ```

        **Predict before you run.** Against the version with PARTITION BY, does the quick version
        flag more members, fewer, or the same?

        - a) The same, since the sort already keeps each member's months together.
        - b) More.
        - c) Fewer.
        - d) None at all, since LAG needs a partition to run.
        """),
        code(r'''
            hurried = rows(Q["c4_hurried"])[0]["members_flagged"]
            checked = rows(Q["c4_hurried_check"])[0]
            kit.stats([(hurried, "members flagged", "LAG with no PARTITION BY"),
                       (checked["compared_with_another_member"], "of them", "compared with another member's month")],
                      caption="The plausible wrong answer: 20 members flagged")
            crossings = run("c4_crossings", "The four flags that read another member's month",
                            money=("spend", "spend_1_back", "spend_2_back"), echo=False)
            '''),
        md("""
        **The plausible wrong answer.** 20 members flagged as falling two months running. The
        answer to the prediction is b.

        **Why it is wrong.** With no PARTITION BY the window is the whole table, so LAG runs straight
        from one member's last row into the next member's first. A member with fewer than three
        months borrows the months of whoever sorts before them. C-0132 of Retail-Core bought in July
        (Rs 2,620) and September (Rs 1,920), and LAG's second step back read C-0131's July, Rs 4,700,
        so C-0132 would get a call about a fall from a month that belongs to someone else. Four of the
        twenty flags are made this way.

        **The check that exposes it.** Carry `lag(customer_id)` beside `lag(spend)` and count the
        flags where the member LAG read is not the member on the row; it should be zero, and it is
        four.
        """),
        code(r'''
            kit.check("the check finds the four flags that crossed into another member",
                      checked["compared_with_another_member"] == 4 and len(crossings) == 4)
            kit.check("every crossing read the member who sorts just before",
                      all(r["member_2_back"] != r["customer_id"] for r in crossings))
            '''),
        md("""
        ## 4. How many members fell two months running once each member's months are kept apart?

        **The fix.** PARTITION BY customer_id: the window starts again for every member, so LAG
        returns NULL on a member's first row and never reaches into another member's months.

        ```sql
        lag(spend, 1) OVER (PARTITION BY customer_id ORDER BY month) AS spend_1_back
        ```

        **Predict before you run.** How many members does the partitioned flag keep?

        - a) 20, the same members.
        - b) 16.
        - c) 24.
        - d) 4.
        """),
        code(r'''
            fixed = rows(Q["c4_partitioned"])[0]["members_flagged"]
            kit.bridge(("flagged with no PARTITION BY", hurried), [("compared with another member", -checked["compared_with_another_member"])],
                       end_label="flagged with PARTITION BY", title="The fix takes the four borrowed months out of the flag",
                       fmt=lambda v: f"{v:,.0f}")
            '''),
        md("""
        **What happened.** The answer is b: 16 members, out of the 118 who ordered in September,
        spent less in September than in their month before, and less in that month than in the one
        before it. The fix takes four members off the call list who had been accused with somebody
        else's months, 20 less 4.
        """),
        code(r'''
            kit.check("the partitioned flag keeps 16 members", fixed == 16)
            kit.check("the fix removes exactly the four crossings", hurried - fixed == checked["compared_with_another_member"])
            '''),
        md("""
        ## A second route: does a walk through each member's months in Python find the same members?

        The second route uses no window: it pulls the 752 member-months into Python unordered, groups
        them by member in a dictionary, sorts each member's months itself, and flags a member whose
        last month is September and whose last three months each fall. A slip in the window's
        PARTITION BY or ORDER BY could not move this flag, since the two share no code.

        **Predict before you run.** Will the walk flag the same 16 members?

        - a) Yes, the same 16.
        - b) No, 20, since Python reads the rows in the order they arrive.
        - c) No, fewer, since Python drops the NULLs.
        - d) Only the Business members.
        """),
        code(r'''
            raw = rows(Q["c4_rows_for_python"])
            months = {}
            for r in raw:
                months.setdefault(r["customer_id"], []).append((r["month"], r["spend"]))
            walk = set()
            for cid, rows_of in months.items():
                rows_of.sort()
                if len(rows_of) >= 3 and str(rows_of[-1][0]) == "2026-09-01":
                    a, b, c = (s for _, s in rows_of[-3:])
                    if c < b < a:
                        walk.add(cid)
            window = {r["customer_id"] for r in rows(Q["c4_partitioned_ids"])}
            kit.table(["route", "member-months read", "members flagged"],
                      [("LAG, PARTITION BY customer_id", 752, len(window)), ("Python walk", len(raw), len(walk))],
                      caption="Two routes, one flag")
            kit.check("Python read every member-month", len(raw) == 752)
            kit.check("the walk flags the window's members, no more and no fewer", walk == window, f"{len(walk)} members")
            '''),
        md("""
        **What happened.** The answer is a: the walk flags the same 16 members as the partitioned
        LAG, member for member. Both read "the month before" as the member's previous row of months.

        > **Kavya's review.** A window that is not told whose rows belong together will compare
        > anyone with anyone. Carry the id LAG read beside the value it read, and read the rows
        > behind a flag before a call goes out.

        ### In the interview: how do you find a fall two months running, and how do you catch LAG crossing customers?

        **[F] How would you find customers whose spend fell two months in a row?** Build one row per
        customer per month, take `lag(spend, 1)` and `lag(spend, 2)` over a window partitioned by
        the customer and ordered by month, and keep the rows where this month is below the last and
        the last below the one before. The partition is what keeps each customer's history their
        own.

        **[F] LAG returned a value for a customer's very first month. What went wrong, and how do you
        check for it in ten thousand rows?** The window has no PARTITION BY, so LAG crossed from the
        previous customer's last row. Carry `lag(customer_id)` beside the value and count the rows
        where it differs from the row's own customer; the count must be zero.

        ### Depth: which months fell two running anywhere in the six, and what does LEAD read?

        The flag reads September because Marketing acts now. The same window, read at every month,
        shows how common a two-month fall is across the book. `lead()` reads the next row the same
        way LAG reads the previous one; nothing today needs it.
        """),
        code(r'''
            anywhere = rows("""
                WITH monthly AS (
                    SELECT customer_id, date_trunc('month', order_date)::date AS month, sum(amount) AS spend
                    FROM orders GROUP BY customer_id, date_trunc('month', order_date)),
                lagged AS (
                    SELECT customer_id, month, spend,
                           lag(spend, 1) OVER (PARTITION BY customer_id ORDER BY month) AS b1,
                           lag(spend, 2) OVER (PARTITION BY customer_id ORDER BY month) AS b2
                    FROM monthly)
                SELECT to_char(month, 'YYYY-MM') AS month, count(*) AS two_falls_ending_here
                FROM lagged WHERE spend < b1 AND b1 < b2 GROUP BY 1 ORDER BY 1""")
            kit.columns([r["month"] for r in anywhere], [("members whose second fall ends this month",
                         [r["two_falls_ending_here"] for r in anywhere])],
                        title="Two falls running, by the month the second fall lands")
            kit.check("September's count is the flag's 16",
                      [r["two_falls_ending_here"] for r in anywhere if r["month"] == "2026-09"] == [16])
            '''),
        md("""
        ## What did this chapter answer?

        1. **Which way, at what cost?** LAG in a window: one pass over 752 member-months, where a
           self-join or a lookup per row works through 1,504.
        2. **What did each member spend each month?** One row per member per month with an order:
           752 member-months, with 118 to 141 members buying in each month.
        3. **What does LAG put beside a month?** The member's previous row and the one before it;
           C-0040 fell twice running into June and recovered.
        4. **What does LAG read with no PARTITION BY?** Another member's months: 20 flags, four of
           them borrowed, caught by carrying the id LAG read.
        5. **How many fell two months running?** 16 members, with each member's months kept apart.
        6. **Does a Python walk agree?** Yes, the same 16 members.

        Chapter 5 turns to Meera's ask: has Q2 revenue kept pace with the plan line? Chapter 6 comes
        back to these 16 before Marketing rings any of them.
        """),
        code("kit.check_summary()"),
    ]


# ----------------------------------------------------------------------------------- chapter 5
def ch5():
    return [
        md(f"""
        # Has Q2 revenue kept pace with the plan line week by week, and where did it stand at mid-quarter?

        **Week 2, Wednesday. Chapter 5 of 6.** Chapters 1 to 4 looked at members; this chapter
        looks at the quarter, for Meera.

        > "And Meera wants to see revenue accumulate week by week against the plan line, so we know
        > by mid-quarter whether we are on track."
        > The marketing lead, Kalpa Retail, passing on Meera Raghavan's ask

        **Who needs the answer.** Meera Raghavan, CEO of Kalpa Retail, decides at mid-quarter whether
        to change course: hold the plan, push a campaign or move budget. A quarter reported behind
        plan when it is on plan sends Marketing after a gap that is not there, with discounts that
        cost margin; a quarter read as comfortably ahead when one week made the lead hides a run rate
        below plan until the quarter is gone.

        **The questions on the way.**
        1. Which ways could the team accumulate the quarter against plan, and what would each cost?
        2. How much had Q2 booked by the end of each plan week?
        3. Does the running total close on Monday's Q2 total?
        4. Where did Q2 stand at mid-quarter, and how has each week run since?
        5. Can a running total by order say which order took Q2 past Rs 3.5 crore?
        6. Does a plain sum up to each week's end agree?

        **The metric at stake.** Booked revenue to date against plan to date. Booked revenue is
        every order at its amount whatever its status, and Monday's suite put Q2, July to September
        2026, at Rs 9,84,00,000. The plan line is a small table, `plan_line`, with one row per plan
        week: the Monday it starts and the revenue planned for it. To date means every week up to
        and including the one on the row.

        **What chapters 1 to 4 found.** Each segment's protect list is its top fifty by Q2 revenue
        under RANK, and 16 members' spend fell in September and in the month before it. A running
        total is a window too: `sum(x) OVER (ORDER BY week)` keeps every week's row and carries the
        sum of every row up to and including it.

        {COMPANY[5]}
        """),
        setup_note("05_against_plan"),
        setup("05_against_plan"),
        where(5, ["the options\nfour ways to accumulate",
                  "to date\nthe plan's weeks",
                  "the close\nagainst Monday's total",
                  "mid-quarter\nand the run rate",
                  "by order\nwhich order crossed",
                  "a second route\na plain sum"]),
        md("""
        ## The options: which ways could the team accumulate the quarter against plan, and what would each cost?

        | Option | How it accumulates | What the database works through | Statements | When it fits |
        |---|---|---|---|---|
        | A. A running SUM in a window over weekly totals | weekly totals first, then `sum() OVER (ORDER BY week)` for booked and for plan | the Q2 orders once, then 13 weeks | 1 | a to-date figure at every week, in one table |
        | B. A plain SUM up to each week's end | for each plan week, sums every order dated up to its last day | the Q2 orders once per plan week | 1, with a subquery per week | one reading on one date Meera names |
        | C. A self-join of weeks to every earlier week | joins each week to itself and every week before, then GROUP BY | the week pairs | 1 | a database with no window functions |
        | D. A spreadsheet with a cumulative column | exports the orders and copies a formula down | every Q2 order, exported | none | a one-off look nobody reruns |

        **Predict before you run.** How many order rows does option B read to fill all thirteen plan
        weeks?

        - a) 462, the Q2 orders once.
        - b) 13, one per week.
        - c) About 6,000.
        - d) About 91.
        """),
        code(r'''
            plan = rows(Q["c5_plan"])
            span = rows(Q["c5_q2_span"])[0]
            weeks = len(plan)
            sizing = [("A. running SUM in a window", span["orders"]), ("B. plain SUM per week", weeks * span["orders"]),
                      ("C. self-join of weeks", weeks * (weeks + 1) // 2), ("D. spreadsheet export", span["orders"])]
            kit.table(["option", "rows or pairs worked through"], [(o, f"{n:,}") for o, n in sizing],
                      caption=f"Sized on Q2: {span['orders']} orders and {weeks} plan weeks")
            kit.bars(sizing, title="Rows each option works through to fill thirteen weeks", lit=(0,))
            '''),
        md("""
        **What happened.** The answer is c: 6,006 order reads, the 462 Q2 orders once for each of the
        13 plan weeks. The window reads the orders once and accumulates 13 weekly totals; the
        self-join works through 91 week pairs; the spreadsheet exports all 462 orders, which the data
        platform lead's rule, "query it, do not export it", rules out.

        **The best-fit call.** Option A, a running SUM in a window, booked and plan side by side in
        one table. **What would change the call:** a single reading on a day Meera names, such as
        "where were we on 19 August?", which is one plain SUM with the date in WHERE, option B for
        one week.
        """),
        code(r'''
            kit.check("thirteen plan weeks", weeks == 13)
            kit.check("option B reads 6,006 order rows", weeks * span["orders"] == 6006)
            kit.check("the plan adds to Rs 9,83,99,990", sum(p["plan_revenue"] for p in plan) == 98399990)
            '''),
        md("""
        ## 1. How much had Q2 booked by the end of each plan week?

        The plan line holds 13 weeks from Monday 6 July, Rs 75,69,230 each. The quickest build starts
        from the plan's weeks, attaches each week's booked revenue by the Monday its orders fall in,
        `date_trunc('week', order_date)`, and accumulates both sides:

        ```sql
        FROM plan_line p LEFT JOIN weekly w USING (week_start)
        ...
        sum(plan_revenue) OVER (ORDER BY week_start) AS plan_to_date,
        sum(booked)       OVER (ORDER BY week_start) AS booked_to_date
        ```

        **Predict before you run.** Where does booked to date finish against the plan to date of
        Rs 9,83,99,990?

        - a) On plan, within a few rupees.
        - b) About Rs 15 lakh short of plan.
        - c) About Rs 1.6 crore ahead.
        - d) Nine times the plan.
        """),
        code(r'''
            print(Q["c5_plan_first"])
            hurried = rows(Q["c5_plan_first"])
            kit.line([str(r["week_start"])[5:] for r in hurried],
                     [("plan to date", [r["plan_to_date"] / 1e7 for r in hurried], "plan"),
                      ("booked to date, plan-first build", [r["booked_to_date"] / 1e7 for r in hurried], "bad")],
                     title="The plan-first build: booked to date in Rs crore, finishing below plan",
                     fmt=lambda v: f"{v:.2f}")
            last = hurried[-1]
            kit.stats([(kit.rupees(last["booked_to_date"]), "booked to date", "the plan-first build's close"),
                       (kit.rupees(last["plan_to_date"]), "plan to date", "thirteen weeks"),
                       (kit.rupees(last["plan_to_date"] - last["booked_to_date"]), "short of plan", "as the table reports it")],
                      caption="The plausible wrong answer at the close")
            '''),
        md("""
        **The plausible wrong answer.** Q2 closed at Rs 9,68,60,180 against a plan of Rs 9,83,99,990,
        Rs 15,39,810 short. The answer to the prediction, as the table reports it, is b. Sent to
        Meera, that line says the quarter missed plan, and the next quarter opens on a campaign to
        recover Rs 15 lakh.

        ## 2. Does the running total close on Monday's Q2 total?

        **Why it is wrong.** Every rupee of Q2 should be in the last row of a running total.
        Monday's suite put Q2 at Rs 9,84,00,000, and the table's last booked to date is short of it.

        **The check that exposes it.** Set the last booked to date beside the quarter's own total,
        then ask which Mondays Q2's orders fall under.
        """),
        code(r'''
            q2_total = span["q2_revenue"]
            q2_weeks = run("c5_weeks_of_q2", "Q2's orders by the Monday each falls under", money=("booked",), echo=False, limit=4)
            before = rows(Q["c5_before_plan"])[0]
            kit.check("the plan-first close is short of Q2's own total", last["booked_to_date"] < q2_total,
                      f"{kit.rupees(q2_total - last['booked_to_date'])} missing")
            kit.check("Q2's orders fall under 14 Mondays, the plan has 13", len(q2_weeks) == 14 and weeks == 13)
            kit.check("the missing rupees are the orders before the plan's first week",
                      q2_total - last["booked_to_date"] == before["booked"], f"{before['orders']} orders")
            '''),
        md("""
        **What happened.** The close is Rs 15,39,820 short of Q2's own total, and the rupees are not
        lost: Q2 starts on Wednesday 1 July and the plan's first week on Monday 6 July. The 25 orders
        of 1 to 5 July, Rs 15,39,820, fall under Monday 29 June, a week the plan line does not have,
        and a LEFT JOIN that starts from the plan's weeks keeps only the plan's weeks. Tuesday's rule
        holds here too: a join is done only when its rows are explained, and this one dropped 25
        orders without a word.

        **The fix, and what it changed.** The plan's first week carries the Q2 days before it.
        `greatest(date_trunc('week', order_date), first plan Monday)` moves the orders of 1 to 5 July
        onto 6 July, so every Q2 order lands in a plan week.
        """),
        code(r'''
            print(Q["c5_fixed"])
            fixed = rows(Q["c5_fixed"])
            close = fixed[-1]
            kit.bridge(("plan-first close", last["booked_to_date"]), [("orders of 1 to 5 July", before["booked"])],
                       end_label="booked to date, fixed", title="The fix puts the first five days of Q2 back",
                       fmt=kit.rupees, lo=9.5e7)
            kit.check("the fixed close is Monday's Rs 9,84,00,000", close["booked_to_date"] == q2_total == 98400000)
            kit.check("Q2 closes Rs 10 ahead of plan", close["booked_to_date"] - close["plan_to_date"] == 10)
            '''),
        md("""
        **What happened.** Booked to date now closes on Rs 9,84,00,000, Monday's total, against a plan
        of Rs 9,83,99,990: Q2 finished Rs 10 ahead, on plan, where the plan-first build reported it
        Rs 15,39,810 short. The bridge's axis starts at Rs 9.5 crore so the move shows.

        ## 3. Where did Q2 stand at mid-quarter, and how has each week run since?

        Mid-quarter is the end of the seventh of thirteen plan weeks, the week of 17 August.

        **Predict before you run.** At the end of the week of 17 August, where was booked to date
        against plan to date?

        - a) About Rs 15 lakh behind.
        - b) About Rs 1.6 crore ahead.
        - c) Exactly on plan.
        - d) About nine times the plan.
        """),
        code(r'''
            mid = fixed[6]
            kit.line([str(r["week_start"])[5:] for r in fixed],
                     [("plan to date", [r["plan_to_date"] / 1e7 for r in fixed], "plan"),
                      ("booked to date", [r["booked_to_date"] / 1e7 for r in fixed], "lit")],
                     title="Booked to date against plan to date, Rs crore: ahead from mid-July, level at the close",
                     fmt=lambda v: f"{v:.2f}")
            kit.columns([str(r["week_start"])[5:] for r in fixed],
                        [("plan for the week", [r["plan_revenue"] / 1e5 for r in fixed]),
                         ("booked in the week", [r["booked"] / 1e5 for r in fixed])],
                        title="Each week on its own, Rs lakh: one July week far above plan, most weeks since mid-August below",
                        fmt=lambda v: f"{v:,.0f}")
            '''),
        md("""
        **What happened.** The answer is b. At the end of the week of 17 August, booked to date was
        Rs 6,87,36,590 against a plan to date of Rs 5,29,84,610, Rs 1,57,51,980 ahead. The weeks on
        their own tell the rest: the week of 13 July booked Rs 2,66,28,920, three and a half times its
        plan of Rs 75,69,230, and from the week of 10 August six of the seven full weeks booked below
        their plan. The quarter was ahead by the total and behind by the run rate, and it closed level
        because one July week paid for the weeks after it.

        A cumulative figure set beside one week's plan reads Rs 6,87,36,590 against Rs 75,69,230 at
        mid-quarter, about nine times plan, which is option d and is never a comparison: to date goes
        beside to date.
        """),
        code(r'''
            full_since = [r for r in fixed if "2026-08-10" <= str(r["week_start"]) <= "2026-09-21"]
            kit.check("mid-quarter is Rs 1,57,51,980 ahead", mid["booked_to_date"] - mid["plan_to_date"] == 15751980)
            kit.check("six of the seven full weeks from 10 August booked below plan",
                      sum(r["booked"] < r["plan_revenue"] for r in full_since) == 6 and len(full_since) == 7)
            kit.check("the week of 13 July booked Rs 2,66,28,920", fixed[1]["booked"] == 26628920)
            '''),
        md("""
        ## 4. Can a running total by order say which order took Q2 past Rs 3.5 crore?

        At the grain of a week, every row has its own Monday, so the order of the window is never in
        doubt. At the grain of an order it is: 22 July, the busiest day of Q2, holds twelve orders.
        Rows that share the window's ORDER BY value are peers, and the default running sum adds all
        of a row's peers at once.

        **Predict before you run.** With `sum(amount) OVER (ORDER BY order_date)`, what does the first
        order of 22 July show?

        - a) Rs 3,45,16,000, the day before plus its own amount.
        - b) Rs 3,76,90,290, the day's closing total.
        - c) Its own amount.
        - d) NULL.
        """),
        code(r'''
            peers = run("c5_peers", "22 July: a running total by date alone, and by date and order id",
                        money=("amount", "by_date_alone", "by_date_and_id"), echo=False)
            kit.line([r["order_id"][-3:] for r in peers],
                     [("by date alone", [r["by_date_alone"] / 1e7 for r in peers], "bad"),
                      ("by date and order id", [r["by_date_and_id"] / 1e7 for r in peers], "lit")],
                     title="22 July in Rs crore: one flat value for twelve orders, or one step per order",
                     fmt=lambda v: f"{v:.3f}", lo=3.4)
            '''),
        md("""
        **What happened.** The answer is b: by date alone, all twelve orders of 22 July show
        Rs 3,76,90,290, the day's closing total, so no row can say which order crossed Rs 3.5 crore.
        With the order id added to the ORDER BY, every row is its own step, from Rs 3,45,16,000 to
        Rs 3,76,90,290, and the step past Rs 3.5 crore is KR-00580's, Rs 8,55,000. The order id makes
        the running total the same on every run and on every learner's machine; it does not make it
        the true order of the day, since the warehouse records a date and no time. Say which tiebreak
        the figure uses.
        """),
        code(r'''
            kit.check("by date alone, the twelve orders share one value", len({r["by_date_alone"] for r in peers}) == 1 and len(peers) == 12)
            kit.check("by date and id, every order has its own value", len({r["by_date_and_id"] for r in peers}) == 12)
            kit.check("both versions finish the day on the same total", peers[-1]["by_date_alone"] == peers[-1]["by_date_and_id"])
            '''),
        md("""
        ## A second route: does a plain sum up to each week's end agree?

        Option B, with no window: for each plan week, one plain SUM of every Q2 order dated on or
        before the week's last day. It reads the orders 13 times, and it shares no code with the
        window or with the `greatest()` fix.

        **Predict before you run.** Will the thirteen plain sums match the fixed running total week by
        week?

        - a) Yes, all thirteen.
        - b) All but the first week, which the sums miss.
        - c) Only the last week.
        - d) None, since a plain SUM cannot accumulate.
        """),
        code(r'''
            plain = rows(Q["c5_second_route"])
            kit.table(["week starting", "running SUM in a window", "plain SUM to the week's end"],
                      [(str(f["week_start"]), kit.rupees(f["booked_to_date"]), kit.rupees(p["booked_to_date"]))
                       for f, p in zip(fixed, plain)][:5] + [("...", "...", "...")],
                      caption="Two routes, week by week (first five of thirteen)")
            kit.check("the two routes agree in all thirteen weeks",
                      [f["booked_to_date"] for f in fixed] == [p["booked_to_date"] for p in plain])
            '''),
        md("""
        **What happened.** The answer is a: the plain sums equal the window's running total in all
        thirteen weeks, including the first, since the first week's last day, 12 July, already
        includes 1 to 5 July. The plain sums read 6,006 order rows to say what the window said in one
        pass, which is why they are the check.

        > **Kavya's review.** A running total is finished when its last value equals the total you can
        > count without it. Close the loop on Monday's Rs 9,84,00,000 before you say ahead or behind.

        ### In the interview: what makes a running total trustworthy?

        **[F] What makes a running total deterministic, and how would you notice one that was not?**
        An ORDER BY that is unique within the window, such as the date plus the order id. Rows that
        share an ORDER BY value are peers and show the same cumulative figure, which is the tell: a
        flat run of identical values across rows, or a figure that cannot say which row crossed a
        line.

        **[D] Your running total closes below the quarter's total. What do you check first?** Whether
        every row made it in: compare the last cumulative value with the independent total, then look
        for rows outside the join's calendar, such as days before the first plan week or after the
        last. Here 25 orders of 1 to 5 July were missing, Rs 15,39,820.

        **[F] A dashboard says revenue to date is nine times the plan by week seven. What is the likely
        mistake?** A cumulative actual set beside one week's plan. Accumulate the plan too and compare
        to date with to date: at mid-quarter that is Rs 6,87,36,590 against Rs 5,29,84,610.

        ### Depth: how far ahead was Q2 at the end of every plan week?
        """),
        code(r'''
            gap = [(str(r["week_start"])[5:], (r["booked_to_date"] - r["plan_to_date"]) / 1e5) for r in fixed]
            kit.bars(gap, title="Booked to date less plan to date at each plan week's end, Rs lakh",
                     fmt=lambda v: f"{v:,.1f}", lit=(6,))
            kit.check("the lead peaked at the end of the week of 3 August",
                      max(gap, key=lambda g: g[1])[0] == "08-03")
            '''),
        md("""
        The lead was Rs 24.7 lakh behind after the first plan week, jumped ahead in the week of 13
        July, peaked at Rs 2,16,69,660 at the end of the week of 3 August and shrank from there to Rs
        10 at the close.

        ## What did this chapter answer?

        1. **Which way, at what cost?** A running SUM in a window over weekly totals: the Q2 orders
           once, where plain sums per week read them 6,006 times.
        2. **How much had Q2 booked by each week's end?** The plan-first build said the quarter closed
           Rs 15,39,810 short of plan, at Rs 9,68,60,180.
        3. **Does it close on Monday's total?** Not until the plan's first week carries 1 to 5 July:
           then it closes on Rs 9,84,00,000, Rs 10 ahead of plan.
        4. **Where was Q2 at mid-quarter?** Rs 1,57,51,980 ahead, built in one July week, with six of
           the seven full weeks from 10 August below plan.
        5. **Can a running total by order name the order that crossed Rs 3.5 crore?** Only with a
           unique tiebreak: by date alone, twelve orders share one value.
        6. **Does a plain sum agree?** Yes, in all thirteen weeks.

        Chapter 6 brings the members back: Marketing wants to ring the flagged members on the protect
        list, and one of them says he was on holiday.
        """),
        code("kit.check_summary()"),
    ]


# ----------------------------------------------------------------------------------- chapter 6
def ch6():
    return [
        md(f"""
        # Which listed members does Marketing call first, and does each flag hold up when a member says he was on holiday?

        **Week 2, Wednesday. Chapter 6 of 6.** The protect list and the flag meet: Marketing calls
        the flagged members on the list first, and one member has already pushed back.

        > "Before we ring anyone: one of your flagged members, C-0216, rang our help line to say he
        > was travelling in August and has not stopped buying. Is your flag wrong about him, and how
        > many others?"
        > The head of Retail-Plus, Kalpa Retail

        **Who needs the answer.** The marketing lead's member team rings the flagged members on the
        protect list this week, and the head of Retail-Plus answers to his members for every call. A
        call that tells a loyal member his spend is falling when he was away costs his goodwill and
        maybe his renewal, and a call list padded with false alarms spends the team's week on members
        who were never drifting.

        **The questions on the way.**
        1. Which ways could the flag read "last month", and what would each cost?
        2. How many of the flagged members are on the protect list?
        3. What did LAG compare for the member who says he was on holiday?
        4. How many of the sixteen flags step over a month with no order?
        5. Does a join on calendar months find the same members?
        6. Who does Marketing call first?

        **The metric at stake.** Monthly spend, a member's booked revenue in one calendar month, and
        the flag: spend in September below August, and August below July. A month with no order has
        no row in the monthly table.

        **What chapters 1 to 5 found.** Each segment's protect list is its top fifty by Q2 revenue
        under RANK, the head of Retail-Plus's rule, so members who spent the same share a place.
        Chapter 4's flag, LAG over each member's months with PARTITION BY customer_id, found 16
        members whose September was below their month before, and that month below the one before
        it. Q2 itself closed on plan, Rs 9,84,00,000 against Rs 9,83,99,990.

        {COMPANY[6]}
        """),
        setup_note("06_call_first"),
        setup("06_call_first"),
        where(6, ["the options\nfour readings of last month",
                  "the list\nwho is flagged on it",
                  "the member on holiday\nwhat LAG compared",
                  "the gaps\nflags over an empty month",
                  "a second route\na calendar join",
                  "the calls\nwho goes first"]),
        md("""
        ## The options: which ways could the flag read "last month", and what would each cost?

        Marketing's words are "monthly spend has fallen for two months running", which reads as
        calendar months: September below August, August below July.

        | Option | What "last month" is | Rows it reads | What a month with no order does |
        |---|---|---|---|
        | A. LAG over the member's own months, chapter 4's flag | the last month before this one in which the member bought | every member-month | is stepped over, so the months either side are compared |
        | B. LAG with a check that the two rows before September are August and July | the calendar month before | every member-month | breaks the run, so no flag |
        | C. A calendar of every member and every month, with zero where there is no order | the calendar month before | every member times six months | reads as spend of zero, so a quiet month becomes a fall |
        | D. The same calendar, left empty where there is no order | the calendar month before | every member times six months | stays empty, so no flag |

        **Predict before you run.** In how many of the six months does a member who bought place an
        order, on average?

        - a) About 2.5.
        - b) All six.
        - c) About 5.
        - d) About 1.
        """),
        code(r'''
            per = rows(Q["c6_months_per_member"])[0]
            cal = rows(Q["c6_calendar_table"])[0]
            sizing = [("A. LAG over own months", per["member_months"]), ("B. LAG with a calendar check", per["member_months"]),
                      ("C. calendar, zero-filled", cal["calendar_rows"]), ("D. calendar, left empty", cal["calendar_rows"])]
            kit.table(["option", "rows read"], [(o, f"{n:,}") for o, n in sizing],
                      caption=f"{per['members']} members, {per['months_with_an_order_each']} months with an order each, on average")
            kit.bars(sizing, title="Rows each reading works through: a calendar adds every empty month as a row", lit=(1,))
            '''),
        md("""
        **What happened.** The answer is a: 752 member-months for 301 members, 2.5 months with an
        order each out of six. A month with no order is the usual state for a Kalpa member, so a
        zero-filled calendar, option C, reads a quiet month as a fall to zero: it flags 26 members, 17
        of whom simply placed no order in September. Options B and D read calendar months; B works
        through the 752 rows that exist and D through 1,806, every member in every month.

        **The best-fit call.** Option B: LAG with a check that the two rows before September are
        August and July. It reads only the rows that exist and adds two columns. **What would change
        the call:** if Marketing also wants "went quiet" as a signal of its own, a member who bought
        in July and August and nothing in September, the calendar of option D makes those empty months
        rows a query can count.
        """),
        code(r'''
            kit.check("2.5 months with an order per member", float(per["months_with_an_order_each"]) == 2.5)
            kit.check("the calendar holds 1,806 rows, 301 members times six months", cal["calendar_rows"] == 1806 == 301 * 6)
            kit.check("a zero-filled calendar flags 26, of whom 17 placed no September order",
                      (cal["flagged_zero_months"], cal["zero_flags_with_no_september_order"]) == (26, 17))
            '''),
        md("""
        ## 1. How many of the flagged members are on the protect list?

        The protect list is each segment's top fifty under RANK; the flag is chapter 4's partitioned
        LAG. Marketing calls the members who are on both.

        **Predict before you run.** How many of chapter 4's 16 flagged members are on a protect list?

        - a) All 16.
        - b) About half.
        - c) None, since the list is about spend and the flag about falls.
        - d) It cannot be known without the tie rule.
        """),
        code(r'''
            both = rows(Q["c6_on_the_list"])[0]
            kit.stats([(both["members_flagged"], "members flagged", "chapter 4's partitioned LAG"),
                       (both["flagged_on_the_list"], "on a protect list", "each segment's top fifty under RANK")],
                      caption="Who Marketing would ring, before the head of Retail-Plus's message")
            kit.check("every flagged member is on a protect list", both["flagged_on_the_list"] == both["members_flagged"] == 16)
            '''),
        md("""
        **What happened.** The answer is a: all 16 flagged members are on a protect list, since a
        member whose spend can fall twice from a high month is a member who spent a lot. Marketing's
        call sheet would read 16 names.

        ## 2. What did LAG compare for the member who says he was on holiday?

        C-0216 of Retail-Plus stands at place 23 on his segment's list. Carry the month LAG read
        beside the spend it read.

        **Predict before you run.** Which month did LAG treat as "last month" for C-0216's September?

        - a) August.
        - b) July.
        - c) June.
        - d) None, since his August is empty.
        """),
        code(r'''
            his = run("c6_holiday_member", "C-0216: each month with the months LAG read",
                      money=("spend", "spend_1_back", "spend_2_back"), echo=False)
            labels = ["2026-04", "2026-05", "2026-06", "2026-07", "2026-08", "2026-09"]
            spent = {str(r["month"])[:7]: r["spend"] for r in his}
            kit.line(labels, [("C-0216's monthly spend", [spent.get(m) for m in labels], "lit")],
                     title="C-0216 bought in May, July and September: no June, no August", fmt=kit.rupees)
            '''),
        md("""
        **What happened.** The answer is b. C-0216 bought in May (Rs 6,440), July (Rs 4,300) and
        September (Rs 2,540). LAG reads the previous row, and with no order in August there is no
        August row, so it compared September with July and July with May, four months apart. Chapter
        4's flag called that two months of falls; C-0216 says August was a holiday, and his rows agree
        that August is simply empty.
        """),
        code(r'''
            sep = his[-1]
            kit.check("LAG read July as last month for September", str(sep["month_1_back"]) == "2026-07-01")
            kit.check("and May as the month before that", str(sep["month_2_back"]) == "2026-05-01")
            kit.check("C-0216 has no August row", "2026-08" not in spent)
            '''),
        md("""
        ## 3. How many of the sixteen flags step over a month with no order?

        **The plausible wrong answer.** Ship chapter 4's flag as it stands: sixteen calls, each member
        told that their spend has fallen two months running. Answered for C-0216, the hurried reply is
        that he did spend less each time he ordered.

        **Why it is wrong.** Marketing asked about calendar months, and LAG counts rows. Wherever a
        member skipped a month, LAG steps over the gap and compares months that are further apart, so
        a holiday reads as a fall and the call accuses a loyal member.

        **The check that exposes it.** Count the flags whose two rows before September are not August
        and July.
        """),
        code(r'''
            gaps = rows(Q["c6_gap_check"])[0]
            kept = rows(Q["c6_calendar_flag"])[0]["members_flagged"]
            kit.bridge(("chapter 4's flag", gaps["members_flagged"]),
                       [("compared across a month with no order", -gaps["across_a_month_with_no_order"])],
                       end_label="flag with the calendar check", title="Seven of the sixteen flags step over an empty month",
                       fmt=lambda v: f"{v:,.0f}")
            kit.check("seven flags step over a month with no order", gaps["across_a_month_with_no_order"] == 7)
            kit.check("the calendar check keeps nine", kept == 9 == gaps["members_flagged"] - gaps["across_a_month_with_no_order"])
            '''),
        md("""
        **What happened.** Seven of the sixteen flags compare September with a month before the one
        before it, because the member placed no order in July or August. C-0216 is one of the seven.

        **The fix, and what it changed.** Option B: the flag holds only when the two rows before
        September are August and July.

        ```sql
        AND month_1_back = DATE '2026-08-01'
        AND month_2_back = DATE '2026-07-01'
        ```

        Nine members keep the flag. Seven calls are not made, C-0216's among them, and every call that
        goes out describes three consecutive months that each fell.

        ## A second route: does a join on calendar months find the same members?

        A self-join with no window: each member's September row joined to the same member's August row
        and July row by date, keeping the members whose spend fell at each step. A missing month has no
        row to join to, so a gap breaks the run here too, by construction.

        **Predict before you run.** How many members does the calendar join keep?

        - a) 9, the same members.
        - b) 16.
        - c) 7.
        - d) 26.
        """),
        code(r'''
            joined = {r["customer_id"] for r in rows(Q["c6_second_route"])}
            checked = {r["customer_id"] for r in rows(Q["c6_calendar_ids"])}
            kit.table(["route", "members flagged"], [("LAG with the calendar check", len(checked)),
                                                    ("join on calendar months", len(joined))],
                      caption="Two routes, one flag")
            kit.check("the join keeps the same members as the checked LAG", joined == checked, f"{len(joined)} members")
            '''),
        md("""
        **What happened.** The answer is a: the join keeps the same nine members as the checked LAG,
        member for member. The two share no window and agree because both read calendar months.

        ## 4. Who does Marketing call first?

        All nine flagged members are on a protect list, since the list is wider than the flag. One of
        them shows what a fall that holds up looks like: C-0010 of Retail-Core, first on his segment's
        list.
        """),
        code(r'''
            his = run("c6_genuine_fall", "C-0010, the top of Retail-Core's list, in each Q2 month", money=("spend",), echo=False)
            kit.columns([str(r["month"])[:7] for r in his], [("C-0010's monthly spend, Rs", [r["spend"] for r in his])],
                        title="A fall that holds up: July, August and September each lower", fmt=kit.rupees)
            calls = rows(Q["c6_call_list"])
            kit.check("nine members to call, all on a protect list", len(calls) == 9)
            kit.check("every call describes three consecutive months, each lower",
                      all(r["september"] < r["august"] < r["july"] for r in calls))
            '''),
        md("""
        **Your turn.** Type these lines into the empty cell below and run it. The block is
        `c6_call_list` of the chapter's `.sql` file: the nine members with their segment, their place
        on the list and their three months.

        ```python
        calls = run("c6_call_list", "Marketing's first calls", money=("july", "august", "september"))
        ```

        Read the nine before you write the line to Marketing: which segments they come from, how high
        on each list they stand, and how far each one's spend fell.
        """),
        empty(),
        md("""
        **What happened.** C-0010 spent Rs 7,840 in July, Rs 4,080 in August and Rs 1,990 in
        September, three consecutive months, each lower. Marketing's first calls are the nine members
        the checked flag keeps, every one of them on a protect list; the member on holiday is not
        among them, and the call script describes months the member can check on his own statement.

        > **Kavya's review.** A month with no order is no reading. Write that into the flag's
        > definition, and read the rows behind a flag before a call goes out.

        ### In the interview: how does your flag treat a month with no orders?

        **[D] A member says he was on holiday in August and should not be flagged. How does your
        definition treat a month with no orders, and why not fill it with zero?** A month with no
        order is no reading, so it breaks the run and he is not flagged; the check is that the rows
        LAG reads are the calendar months before. Filling the empty month with zero would read a quiet
        month as a fall to zero, and Kalpa's members buy in about 2.5 of six months, so zeros would
        flag 26 members here, 17 of them only for a quiet September.

        **[D] Marketing also wants members who went quiet. How would you build that flag?** With a
        calendar of every member and every month, left empty where there is no order, so a quiet month
        becomes a row the query can see: bought in July and August, nothing in September. It is a
        second flag with its own name, never mixed into the falling-spend flag.

        ### Depth: what would a zero-filled calendar have flagged?

        Option C turns every quiet September into a fall to zero. The counts below come from the same
        calendar, read both ways.
        """),
        code(r'''
            kit.columns(["left empty", "zero-filled"],
                        [("members flagged", [cal["flagged_empty_months"], cal["flagged_zero_months"]]),
                         ("of them with no September order", [0, cal["zero_flags_with_no_september_order"]])],
                        title="One calendar, two readings of an empty month")
            kit.check("the calendar left empty agrees with the checked LAG", cal["flagged_empty_months"] == 9)
            '''),
        md("""
        Left empty, the calendar flags the same nine. Zero-filled, it flags 26, and 17 of them had no
        September order at all, which is a different question, who went quiet, answered by accident.

        ## What did this chapter answer?

        1. **Which reading of "last month"?** The calendar month before, checked on LAG's own rows:
           752 rows, where a calendar reads 1,806 and a zero-filled one flags 26.
        2. **How many flagged members are on the list?** All 16 of chapter 4's flag.
        3. **What did LAG compare for C-0216?** September with July and July with May, stepping over
           an empty June and August.
        4. **How many flags step over an empty month?** 7 of 16; the calendar check keeps 9.
        5. **Does a calendar join agree?** Yes, the same nine members.
        6. **Who does Marketing call first?** The nine checked flags, all on a protect list, C-0010 of
           Retail-Core among them and the member on holiday not.

        **The day's answer, to Marketing and the head of Retail-Plus.** Each segment's protect list is
        its top fifty by Q2 revenue under RANK, so members who spent the same share a place: Business
        and Student list every Q2 buyer, 35 and 20, Retail-Core lists 50, and Retail-Plus lists the
        count your own run gave, with the reason in the same line if it is not fifty. Call the nine
        members whose spend fell in August and again in September first; a month with no order is no
        reading, so the member on holiday is not one of them. Q2 closed on plan, Rs 9,84,00,000 against
        Rs 9,83,99,990, and the Rs 1.58 crore lead at mid-quarter came from one week in July, so the
        weekly run rate has sat below plan since 10 August.
        """),
        code("kit.check_summary()"),
    ]


# ----------------------------------------------------------------------------------- the escalated case
CASE_SETUP = WAREHOUSE + r'''
Q = {}
print("connected:", kit.sql("select version()")[0]["version"].split(",")[0])

Q2_SPEND = """
    SELECT c.segment, o.customer_id, count(*) AS q2_orders, sum(o.amount) AS q2_revenue
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY c.segment, o.customer_id"""

MONTHLY = """
    SELECT customer_id, date_trunc('month', order_date)::date AS month, sum(amount) AS spend
    FROM   orders
    GROUP  BY customer_id, date_trunc('month', order_date)"""
'''


def case():
    """The escalated case: Marketing's Monday pack, the whole day's pass on its own."""
    cells = [
        md("""
        # What does Marketing get on Monday: each segment's list with its count, the members to ring first, the share of revenue the lists carry, and Q2 against plan?

        **Week 2, Wednesday. The escalated case, alone, in five parts.** Parts 1 and 2 run in the
        afternoon session; parts 3 to 5 run in the practice lab.

        > "We start calling on Monday. Send me each segment's protect list under the head of
        > Retail-Plus's rule, with its count; the members we ring first; how much of each segment's Q2
        > revenue the lists cover; and one line Meera can take into the leadership meeting on whether
        > Q2 is on track."
        > The marketing lead, Kalpa Retail

        **The situation.** Kalpa Retail sells to four segments: Business (corporate buyers, whose
        orders run to lakhs), Retail-Core (everyday shoppers), Retail-Plus (the paid membership tier)
        and Student. The head of Retail-Plus has asked that members who spent the same be ranked the
        same and that every list say how many made it. Marketing wants to ring members whose monthly
        spend fell two months running, in calendar months, and one member has already said his
        "fall" was a holiday. Meera Raghavan, Kalpa Retail's CEO, wants to know whether Q2 is on track
        against the plan line, by the total and week by week. This notebook builds all of it, part by
        part, with nothing taken from elsewhere.

        **The data.** Kalpa's Postgres warehouse: `orders` (1,000 rows: order_id, customer_id,
        order_date, quarter, channel, amount, status), `customers` (340 rows, one per member, with the
        segment) and `plan_line` (one row per plan week: week_start, the Monday it starts, and
        plan_revenue). Q2 is July to September 2026. Q2 revenue is booked revenue, every order at its
        amount whatever its status, Rs 9,84,00,000 for the quarter. Monthly spend is a member's booked
        revenue in one calendar month.
        """),
        md("""
        TODO ONLY
        **How to answer.** Each part holds two `TODO` markers. Each marker is a choice, lettered a to
        d, written as comments above a placeholder whose name starts with `__TODO` and ends in the
        marker's number. Replace the placeholder with the letter in quotes, for example `"a"`, and run
        the cell; the check cell after it tells you whether your part behaves. Running a cell before
        you fill its marker stops with a `NameError`, which is expected. Post your ten letters in
        order when you finish, then answer the brief's five design items.
        """),
        md("""
        SOLUTION ONLY
        **This is the solution.** Every marker is filled with its key and the notebook runs clean from
        the top. The reasons for each key, and the brief's five design items, are in
        `exercises/solutions/C2_W02_D03_escalated_case_solution_STUDENT.md`. Where a part's answer
        for Retail-Plus is the count your own run gave, this notebook checks it without printing it.
        """),
        code(CASE_SETUP),
        code(r'''
            kit.side_by_side(
                kit.ladder(["Each segment's list and its count", "The members to ring first", "The share each list carries",
                            "Q2 against plan, total and run rate", "The line to Marketing and Meera"], lit=0, show=False),
                kit.flow(["rank inside each segment", "flag three calendar months", "share of the segment", "to date against plan"],
                         lit=0, show=False),
            )
            '''),
        md("""
        ## Part 1. Which members make each segment's list under the head of Retail-Plus's rule, and how many in each?

        Where this is used at work: every ranked list a business acts on states its rule and its
        count, and the count is the first line a manager checks.
        """),
        code(r'''
            # TODO 1. Which function gives members who spent the same the same place, and skips the places they use up?
            #   a) row_number()
            #   b) dense_rank()
            #   c) rank()
            #   d) count(*), which counts the members up to and including each one's figure
            FUNCTION = {"a": "row_number()", "b": "dense_rank()", "c": "rank()", "d": "count(*)"}[__TODO1__]

            # TODO 2. Which ORDER BY inside the window lets two members who spent the same tie?
            #   a) ORDER BY q2_revenue DESC, customer_id
            #   b) ORDER BY q2_revenue DESC
            #   c) ORDER BY q2_revenue
            #   d) ORDER BY customer_id
            ORDER = {"a": "ORDER BY q2_revenue DESC, customer_id", "b": "ORDER BY q2_revenue DESC",
                     "c": "ORDER BY q2_revenue", "d": "ORDER BY customer_id"}[__TODO2__]
            PLACE = f"{FUNCTION} OVER (PARTITION BY segment {ORDER})"
            list_sql = f"""WITH q2 AS ({Q2_SPEND}),
            placed AS (SELECT segment, customer_id, q2_orders, q2_revenue, {PLACE} AS place FROM q2)
            SELECT segment, customer_id, q2_orders, q2_revenue, place FROM placed WHERE place <= 50"""
            protect = rows(list_sql)
            counts = {}
            for r in protect:
                counts[r["segment"]] = counts.get(r["segment"], 0) + 1
            buyers = {r["segment"]: r["n"] for r in rows(f"SELECT segment, count(*) AS n FROM ({Q2_SPEND}) q2 GROUP BY 1")}
            print("Lists built for:", ", ".join(sorted(counts)))
            '''),
        code(r'''
            TODO ONLY
            kit.table(["segment", "members on the list", "members who bought"],
                      [(s, counts.get(s, 0), buyers[s]) for s in sorted(buyers)], caption="Your lists, one per segment")
            '''),
        code(r'''
            SOLUTION ONLY
            kit.table(["segment", "members on the list", "members who bought"],
                      [(s, counts.get(s, 0), buyers[s]) for s in sorted(buyers) if s != "Retail-Plus"],
                      caption="The lists for Business, Retail-Core and Student; Retail-Plus's count is the one your run printed")
            '''),
        code(r'''
            fiftieth = {r["segment"]: r["q2_revenue"] for r in rows(f"""SELECT segment, q2_revenue FROM (
                SELECT segment, q2_revenue, row_number() OVER (PARTITION BY segment ORDER BY q2_revenue DESC) AS n
                FROM ({Q2_SPEND}) q2) x WHERE n = 50""")}
            at_or_above = {s: sum(1 for r in rows(f"SELECT segment, q2_revenue FROM ({Q2_SPEND}) q2")
                                  if r["segment"] == s and r["q2_revenue"] >= fiftieth.get(s, 0)) for s in buyers}
            print("Segments with a fiftieth member to measure the line against:", ", ".join(sorted(fiftieth)))
            '''),
        code(r'''
            last_kept = {}
            for r in protect:
                last_kept[r["segment"]] = min(last_kept.get(r["segment"], 10 ** 12), r["q2_revenue"])
            everyone = rows(f"SELECT segment, customer_id, q2_revenue FROM ({Q2_SPEND}) q2")
            listed = {r["customer_id"] for r in protect}
            kit.check("every segment has a list", set(counts) == set(buyers), ", ".join(sorted(counts)))
            kit.check("each list holds fifty, or every buyer where a segment has fewer",
                      all(counts.get(s, 0) >= min(50, buyers[s]) for s in buyers))
            kit.check("nobody who spent at least the last listed member's figure is left off",
                      all(r["customer_id"] in listed for r in everyone if r["segment"] in last_kept
                          and r["q2_revenue"] >= last_kept[r["segment"]]))
            kit.check("no list runs past the members at or above its fiftieth member's figure",
                      all(counts.get(s, 0) <= at_or_above[s] for s in buyers))
            kit.check("members who spent the same share a place",
                      all(len({p["place"] for p in protect if p["segment"] == s and p["q2_revenue"] == v}) == 1
                          for s, v in {(p["segment"], p["q2_revenue"]) for p in protect}))
            '''),
        md("""
        ## Part 2. Which listed members does Marketing ring first?

        Where this is used at work: a retention call goes to a customer whose own history shows the
        drift, and the definition of the drift is written down before the first call.
        """),
        code(r'''
            # TODO 3. Which window keeps each member's months to themselves?
            #   a) OVER (PARTITION BY segment ORDER BY month)
            #   b) OVER (PARTITION BY customer_id ORDER BY month)
            #   c) OVER (ORDER BY customer_id, month), since the sort keeps a member's months together
            #   d) OVER (PARTITION BY month ORDER BY customer_id)
            WINDOW = {"a": "OVER (PARTITION BY segment ORDER BY month)",
                      "b": "OVER (PARTITION BY customer_id ORDER BY month)",
                      "c": "OVER (ORDER BY customer_id, month)",
                      "d": "OVER (PARTITION BY month ORDER BY customer_id)"}[__TODO3__]

            # TODO 4. Which condition keeps a flag only for three calendar months in a row?
            #   a) month_1_back = DATE '2026-08-01' AND month_2_back = DATE '2026-07-01'
            #   b) spend_1_back IS NOT NULL AND spend_2_back IS NOT NULL
            #   c) coalesce(spend_1_back, 0) > spend AND coalesce(spend_2_back, 0) > spend_1_back
            #   d) month_1_back < month AND month_2_back < month_1_back
            CALENDAR = {"a": "month_1_back = DATE '2026-08-01' AND month_2_back = DATE '2026-07-01'",
                        "b": "spend_1_back IS NOT NULL AND spend_2_back IS NOT NULL",
                        "c": "coalesce(spend_1_back, 0) > spend AND coalesce(spend_2_back, 0) > spend_1_back",
                        "d": "month_1_back < month AND month_2_back < month_1_back"}[__TODO4__]

            seg_of = {r["customer_id"]: r["segment"] for r in rows("SELECT customer_id, segment FROM customers")}
            flag_sql = f"""WITH monthly AS ({MONTHLY}),
            lagged AS (
                SELECT customer_id, month, spend,
                       lag(spend, 1) {WINDOW} AS spend_1_back, lag(spend, 2) {WINDOW} AS spend_2_back,
                       lag(month, 1) {WINDOW} AS month_1_back, lag(month, 2) {WINDOW} AS month_2_back,
                       lag(customer_id, 1) {WINDOW} AS member_1_back, lag(customer_id, 2) {WINDOW} AS member_2_back
                FROM monthly)
            SELECT customer_id, spend_2_back AS earlier, spend_1_back AS before, spend AS september,
                   month_1_back, month_2_back, member_1_back, member_2_back
            FROM lagged
            WHERE month = DATE '2026-09-01' AND spend < spend_1_back AND spend_1_back < spend_2_back AND {CALENDAR}"""
            flagged = rows(flag_sql)
            to_ring = [r for r in flagged if r["customer_id"] in listed]
            kit.stats([(len(flagged), "members flagged", "three calendar months, each lower"),
                       (len(to_ring), "on a protect list", "Marketing's first calls")],
                      caption="The members Marketing rings first")
            '''),
        code(r'''
            TODO ONLY
            show(sorted(to_ring, key=lambda r: (seg_of[r["customer_id"]], r["customer_id"])), "Your first calls",
                 money=("earlier", "before", "september"))
            '''),
        code(r'''
            crossed = rows(f"""SELECT count(*) AS n FROM (SELECT customer_id, lag(customer_id) {WINDOW} AS prev
                                                     FROM ({MONTHLY}) m) x WHERE prev <> customer_id""")[0]["n"]
            kit.check("your window never reads past the start of a member's own months", crossed == 0, f"{crossed} rows cross")
            kit.check("the flag finds members to ring", len(to_ring) > 0)
            kit.check("no flag compares a member with another member's month",
                      all(r["member_1_back"] == r["customer_id"] == r["member_2_back"] for r in flagged))
            kit.check("every flag reads July and August before September",
                      all(str(r["month_2_back"]) == "2026-07-01" and str(r["month_1_back"]) == "2026-08-01" for r in flagged))
            kit.check("every flagged member's three months each fall", all(r["september"] < r["before"] < r["earlier"] for r in flagged))
            kit.check("the member on holiday, C-0216, is not rung", "C-0216" not in {r["customer_id"] for r in to_ring})
            '''),
        md("""
        ## Part 3. How much of each segment's Q2 revenue does its list carry?

        Where this is used at work: a protect budget is judged by the revenue it covers, so every list
        carries its share of the whole it was cut from.
        """),
        code(r'''
            # TODO 5. Which expression puts the segment's whole Q2 revenue beside every member's row?
            #   a) sum(q2_revenue) OVER (PARTITION BY segment)
            #   b) sum(q2_revenue) OVER (PARTITION BY segment ORDER BY q2_revenue DESC)
            #   c) sum(q2_revenue) OVER ()
            #   d) sum(q2_revenue) OVER (ORDER BY segment)
            TOTAL = {"a": "sum(q2_revenue) OVER (PARTITION BY segment)",
                     "b": "sum(q2_revenue) OVER (PARTITION BY segment ORDER BY q2_revenue DESC)",
                     "c": "sum(q2_revenue) OVER ()",
                     "d": "sum(q2_revenue) OVER (ORDER BY segment)"}[__TODO5__]

            # TODO 6. Which share answers "how much of each segment's revenue does its list cover"?
            #   a) the list's revenue over the book's Q2 revenue, Rs 9,84,00,000
            #   b) the list's members over the segment's members who bought
            #   c) the list's revenue over the segment's revenue
            #   d) the last listed member's revenue over the first's
            SHARE = __TODO6__

            share_sql = f"""WITH q2 AS ({Q2_SPEND})
            SELECT segment, customer_id, q2_revenue,
                   rank() OVER (PARTITION BY segment ORDER BY q2_revenue DESC) AS place,
                   {TOTAL} AS segment_total
            FROM q2"""
            members = rows(share_sql)
            book = sum(m["q2_revenue"] for m in members)
            parts = []
            for seg in sorted({m["segment"] for m in members}):
                mine = [m for m in members if m["segment"] == seg]
                kept = [m for m in mine if m["place"] <= 50]
                parts.append({"segment": seg, "list_revenue": sum(m["q2_revenue"] for m in kept), "listed": len(kept),
                              "bought": len(mine), "segment_total": mine[0]["segment_total"]})
            def share_of(r):
                return {"a": r["list_revenue"] / book, "b": r["listed"] / r["bought"],
                        "c": r["list_revenue"] / r["segment_total"], "d": None}[SHARE]
            shares = [(r["segment"], share_of(r)) for r in parts]
            print("Shares computed for:", ", ".join(s for s, v in shares if v is not None))
            '''),
        code(r'''
            TODO ONLY
            kit.bars([(s, round(100 * v, 1)) for s, v in shares if v is not None],
                     title="The share of each segment's Q2 revenue its list carries, percent", fmt=lambda v: f"{v:.1f}%")
            '''),
        code(r'''
            SOLUTION ONLY
            kit.bars([(s, round(100 * v, 1)) for s, v in shares if v is not None and s != "Retail-Plus"],
                     title="The share each list carries: Business, Retail-Core and Student; Retail-Plus's is your run's",
                     fmt=lambda v: f"{v:.1f}%")
            '''),
        code(r'''
            seg_rev = {r["segment"]: r["q2_revenue"] for r in rows(f"SELECT segment, sum(q2_revenue) AS q2_revenue FROM ({Q2_SPEND}) q2 GROUP BY 1")}
            kit.check("every row carries its segment's whole Q2 revenue", all(m["segment_total"] == seg_rev[m["segment"]] for m in members))
            kit.check("every share is a fraction of its own segment", all(v is not None and 0 < v <= 1 for _, v in shares))
            core = next(r for r in parts if r["segment"] == "Retail-Core")
            kit.check("each share counts rupees, so Retail-Core's is above its share of members",
                      dict(shares).get("Retail-Core") is not None and dict(shares)["Retail-Core"] > core["listed"] / core["bought"])
            '''),
        md("""
        ## Part 4. Is Q2 on track by the total and by the run rate?

        Where this is used at work: a quarter is read twice, by the total so far and by how each week
        is running, and the two can disagree.
        """),
        code(r'''
            # TODO 7. Which expression gives every Q2 order a plan week, including 1 to 5 July?
            #   a) date_trunc('week', order_date)::date
            #   b) greatest(date_trunc('week', order_date)::date, (SELECT min(week_start) FROM plan_line))
            #   c) date_trunc('month', order_date)::date
            #   d) (order_date - 5)
            WEEK = {"a": "date_trunc('week', order_date)::date",
                    "b": "greatest(date_trunc('week', order_date)::date, (SELECT min(week_start) FROM plan_line))",
                    "c": "date_trunc('month', order_date)::date",
                    "d": "(order_date - 5)"}[__TODO7__]

            plan_sql = f"""WITH weekly AS (
                SELECT {WEEK} AS week_start, sum(amount) AS booked FROM orders WHERE quarter = 'Q2' GROUP BY 1),
            joined AS (SELECT p.week_start, p.plan_revenue, coalesce(w.booked, 0) AS booked
                       FROM plan_line p LEFT JOIN weekly w USING (week_start))
            SELECT week_start, plan_revenue, booked,
                   sum(plan_revenue) OVER (ORDER BY week_start) AS plan_to_date,
                   sum(booked) OVER (ORDER BY week_start) AS booked_to_date
            FROM joined ORDER BY week_start"""
            weeks = rows(plan_sql)
            kit.line([str(w["week_start"])[5:] for w in weeks],
                     [("plan to date", [w["plan_to_date"] / 1e7 for w in weeks], "plan"),
                      ("booked to date", [w["booked_to_date"] / 1e7 for w in weeks], "lit")],
                     title="Q2 to date against plan to date, Rs crore", fmt=lambda v: f"{v:.2f}")
            kit.columns([str(w["week_start"])[5:] for w in weeks],
                        [("plan for the week", [w["plan_revenue"] / 1e5 for w in weeks]),
                         ("booked in the week", [w["booked"] / 1e5 for w in weeks])],
                        title="Each plan week on its own, Rs lakh", fmt=lambda v: f"{v:,.0f}")

            # TODO 8. Which comparison counts the weeks that ran below plan, each week on its own?
            #   a) booked_to_date < plan_to_date
            #   b) booked < plan_revenue
            #   c) booked_to_date < plan_revenue
            #   d) sum(booked) < sum(plan_revenue) over the seven weeks
            RUN_RATE = __TODO8__
            since = [w for w in weeks if "2026-08-10" <= str(w["week_start"]) <= "2026-09-21"]
            below = {"a": sum(w["booked_to_date"] < w["plan_to_date"] for w in since),
                     "b": sum(w["booked"] < w["plan_revenue"] for w in since),
                     "c": sum(w["booked_to_date"] < w["plan_revenue"] for w in since),
                     "d": int(sum(w["booked"] for w in since) < sum(w["plan_revenue"] for w in since))}[RUN_RATE]
            print(f"Close: {kit.rupees(weeks[-1]['booked_to_date'])} against {kit.rupees(weeks[-1]['plan_to_date'])}; "
                  f"mid-quarter: {kit.rupees(weeks[6]['booked_to_date'] - weeks[6]['plan_to_date'])} ahead; "
                  f"full weeks from 10 August below plan: {below} of {len(since)}")
            '''),
        code(r'''
            q2_total = rows("SELECT sum(amount) AS t FROM orders WHERE quarter = 'Q2'")[0]["t"]
            kit.check("the running total closes on Q2's own total", weeks[-1]["booked_to_date"] == q2_total)
            kit.check("every plan week carries a to-date that never falls", all(b["booked_to_date"] >= a["booked_to_date"]
                                                                               for a, b in zip(weeks, weeks[1:])))
            kit.check("the run-rate count reads the seven full weeks from 10 August, one week at a time",
                      below == sum(w["booked"] < w["plan_revenue"] for w in since) and len(since) == 7)
            '''),
        md("""
        ## Part 5. What goes to Marketing and Meera?

        Where this is used at work: the line a stakeholder carries into a meeting is the only part of
        the analysis most people will read, so each number in it has to hold on its own.
        """),
        code(r'''
            # TODO 9. Which line goes to Meera for the leadership meeting?
            #   a) "Q2 closed Rs 15,39,810 short of plan, so the next quarter should open on a recovery campaign."
            #   b) "Q2 closed on plan and was Rs 1.58 crore ahead at mid-quarter, so the quarter needs no action at all."
            #   c) "Q2 closed on plan, Rs 10 ahead; the mid-quarter lead came from one July week, and six of seven weeks since 10 August ran below."
            #   d) "Q2 revenue to date stood at about nine times the weekly plan by mid-quarter, well ahead of every target."
            MEERA = __TODO9__

            # TODO 10. Which line goes to Marketing with the lists?
            #   a) "Every segment's list holds exactly fifty members, cut by a stated tiebreaker, so each list is the same size."
            #   b) "Each list holds fifty, or every buyer where a segment has fewer, and a list above fifty names the members tied at its line."
            #   c) "The lists hold 155 members in all, fifty per segment where possible, ranked by Q2 revenue across the whole book."
            #   d) "Each list ranks members with DENSE_RANK, so members who spent the same share a place and no number is skipped."
            MARKETING = __TODO10__
            print("To Meera:", MEERA, "| To Marketing:", MARKETING)
            '''),
        code(r'''
            kit.check("both lines are chosen", MEERA in "abcd" and MARKETING in "abcd")
            kit.check("the run rate the lines rest on reads each week on its own", RUN_RATE in "abcd")
            kit.check_summary()
            '''),
    ]
    answers = {1: '"c"', 2: '"b"', 3: '"b"', 4: '"a"', 5: '"a"', 6: '"c"', 7: '"b"', 8: '"b"', 9: '"c"', 10: '"b"'}
    return cells, answers


# ----------------------------------------------------------------------------------- the second case
def second():
    """The second case: Retail-Core ranked by how often members ordered, in pairs, in the take-home."""
    cells = [
        md("""
        # Should Retail-Core's protect list rank members by how often they ordered in Q2, instead of by how much they spent?

        **Week 2, Wednesday. The second case, in pairs or alone, in the take-home.**

        > "Frequency is what fell in Retail-Plus. Before it spreads, I want Retail-Core's top fifty
        > ranked by how often members ordered in Q2. Same rule as the head of Retail-Plus: ties ranked
        > the same, and tell me how many made it."
        > The marketing lead, Kalpa Retail

        **The situation.** Retail-Core is Kalpa Retail's everyday shoppers, 96 of whom ordered in Q2
        (July to September 2026). Ranked by Q2 revenue, booked revenue of every order whatever its
        status, Retail-Core's top fifty under RANK holds 50 members, because no two members share the
        fiftieth figure. Frequency is how many orders a member placed in the quarter. Under RANK,
        members who spent, or ordered, the same share a place, and the list says how many made it.

        **The data.** Kalpa's Postgres warehouse: `orders` (1,000 rows: order_id, customer_id,
        order_date, quarter, channel, amount, status) and `customers` (340 rows, one per member, with
        the segment).
        """),
        md("""
        TODO ONLY
        **How to answer.** Seven `TODO` markers, each a choice lettered a to d. Replace each
        placeholder with the letter in quotes, for example `"a"`, and run the cell; the check cell
        after it tells you whether your step behaves. Post your seven letters in order, then answer
        the brief's three design items together.
        """),
        md("""
        SOLUTION ONLY
        **This is the solution.** Every marker is filled with its key; the reasons and the brief's
        design items are in `exercises/solutions/C2_W02_D03_second_case_solution_STUDENT.md`.
        """),
        code(CASE_SETUP),
        code(r'''
            kit.flow(["orders per member", "rank by orders", "a second key", "the two lists compared", "the line"], lit=1)
            '''),
        md("""
        ## Step 1. How many Q2 orders did each Retail-Core member place, and where do the ties fall?

        Where this is used at work: a frequency metric is a count, and counts tie far more often than
        rupee amounts do.
        """),
        code(r'''
            # TODO 1. Which expression counts a member's Q2 orders?
            #   a) count(*), one per order row the member placed
            #   b) count(DISTINCT o.customer_id)
            #   c) sum(o.amount)
            #   d) count(DISTINCT date_trunc('month', o.order_date))
            ORDERS = {"a": "count(*)", "b": "count(DISTINCT o.customer_id)", "c": "sum(o.amount)",
                      "d": "count(DISTINCT date_trunc('month', o.order_date))"}[__TODO1__]
            core = rows(f"""SELECT o.customer_id, {ORDERS} AS q2_orders, sum(o.amount) AS q2_revenue
                            FROM orders o JOIN customers c USING (customer_id)
                            WHERE o.quarter = 'Q2' AND c.segment = 'Retail-Core'
                            GROUP BY o.customer_id""")
            spread = {}
            for r in core:
                spread[r["q2_orders"]] = spread.get(r["q2_orders"], 0) + 1
            kit.columns([str(k) for k in sorted(spread, reverse=True)], [("members", [spread[k] for k in sorted(spread, reverse=True)])],
                        title="Retail-Core members by their number of Q2 orders")
            '''),
        code(r'''
            kit.check("96 Retail-Core members ordered in Q2", len(core) == 96)
            kit.check("the order counts add back to the segment's Q2 orders",
                      sum(r["q2_orders"] for r in core) == rows("SELECT count(*) AS n FROM orders o JOIN customers c USING (customer_id) "
                                                                "WHERE o.quarter = 'Q2' AND c.segment = 'Retail-Core'")[0]["n"])
            '''),
        md("""
        ## Step 2. How many members does each rule ship when the list is ranked by orders alone?

        Where this is used at work: a tie rule chosen for rupee amounts has to be read again when the
        metric becomes a count.
        """),
        code(r'''
            # TODO 2. Which window gives members with the same number of orders the same place, and skips the places they use up?
            #   a) row_number() OVER (ORDER BY q2_orders DESC, customer_id)
            #   b) rank() OVER (ORDER BY q2_orders DESC)
            #   c) dense_rank() OVER (ORDER BY q2_orders DESC)
            #   d) rank() OVER (ORDER BY q2_revenue DESC)
            RULE = {"a": "row_number() OVER (ORDER BY q2_orders DESC, customer_id)", "b": "rank() OVER (ORDER BY q2_orders DESC)",
                    "c": "dense_rank() OVER (ORDER BY q2_orders DESC)", "d": "rank() OVER (ORDER BY q2_revenue DESC)"}[__TODO2__]
            base = f"""SELECT o.customer_id, count(*) AS q2_orders, sum(o.amount) AS q2_revenue
                       FROM orders o JOIN customers c USING (customer_id)
                       WHERE o.quarter = 'Q2' AND c.segment = 'Retail-Core' GROUP BY o.customer_id"""
            ranked = rows(f"SELECT customer_id, q2_orders, q2_revenue, {RULE} AS place FROM ({base}) b")
            chosen = sum(1 for r in ranked if r["place"] <= 50)
            all_rules = rows(f"""SELECT count(*) FILTER (WHERE rn <= 50) AS row_number_ships, count(*) FILTER (WHERE rk <= 50) AS rank_ships,
                                        count(*) FILTER (WHERE dr <= 50) AS dense_rank_ships
                                 FROM (SELECT row_number() OVER (ORDER BY q2_orders DESC, customer_id) AS rn,
                                              rank() OVER (ORDER BY q2_orders DESC) AS rk,
                                              dense_rank() OVER (ORDER BY q2_orders DESC) AS dr FROM ({base}) b) x""")[0]
            kit.bars([("row_number", all_rules["row_number_ships"]), ("rank", all_rules["rank_ships"]),
                      ("dense_rank", all_rules["dense_rank_ships"]), ("your rule", chosen)],
                     title="Rows each rule ships when Retail-Core is ranked by Q2 orders alone", lit=(3,))
            '''),
        code(r'''
            same_orders_same_place = all(len({r["place"] for r in ranked if r["q2_orders"] == n}) == 1 for n in spread)
            kit.check("members with the same number of orders share a place under your rule", same_orders_same_place)
            kit.check("your rule ships what the head of Retail-Plus's rule ships on these counts", chosen == all_rules["rank_ships"])
            kit.check("your rule ranks by orders, so the member with most orders is first",
                      min(ranked, key=lambda r: r["place"])["q2_orders"] == max(spread))
            '''),
        md("""
        ## Step 3. Why does that rule ship the number it ships?

        Where this is used at work: a stakeholder who asked for fifty and receives more wants the
        reason in one sentence.
        """),
        code(r'''
            # TODO 3. Why does RANK on orders alone ship 51 members?
            #   a) 24 members placed three or more orders, and the 27 members with two orders all share 25th place.
            #   b) RANK skips a number after every tie, and those skipped numbers count as extra members on the list.
            #   c) One member placed eight orders, so RANK counts that member several times on the list.
            #   d) The 45 members with one order share a place, and RANK adds one of them to make the list even.
            WHY = __TODO3__
            print("your reason:", WHY)
            '''),
        code(r'''
            SOLUTION ONLY
            three_or_more = sum(v for k, v in spread.items() if k >= 3)
            two = spread.get(2, 0)
            print(f"members with three or more orders: {three_or_more}; members with two: {two}")
            kit.check("the members with three or more orders and the members with two add to RANK's count",
                      three_or_more + two == all_rules["rank_ships"])
            '''),
        md("""
        ## Step 4. Which second key breaks the crowd of ties, and how many members does the list ship then?

        Where this is used at work: a ranking on a count almost always needs a second key, and the
        second key is a business choice with a reason.
        """),
        code(r'''
            # TODO 4. Which ORDER BY ranks by orders first, then lets revenue separate members with the same orders?
            #   a) ORDER BY q2_orders DESC, customer_id
            #   b) ORDER BY q2_orders DESC, q2_revenue DESC
            #   c) ORDER BY q2_revenue DESC, q2_orders DESC
            #   d) ORDER BY q2_orders DESC
            ORDER = {"a": "q2_orders DESC, customer_id", "b": "q2_orders DESC, q2_revenue DESC",
                     "c": "q2_revenue DESC, q2_orders DESC", "d": "q2_orders DESC"}[__TODO4__]
            freq_list = rows(f"""SELECT customer_id, q2_orders, q2_revenue FROM (
                                    SELECT customer_id, q2_orders, q2_revenue, rank() OVER (ORDER BY {ORDER}) AS place
                                    FROM ({base}) b) x WHERE place <= 50""")
            rev_list = rows(f"""SELECT customer_id, q2_orders, q2_revenue FROM (
                                   SELECT customer_id, q2_orders, q2_revenue, rank() OVER (ORDER BY q2_revenue DESC) AS place
                                   FROM ({base}) b) x WHERE place <= 50""")
            kit.stats([(len(freq_list), "on the frequency list", "RANK on your ORDER BY"),
                       (len(rev_list), "on the revenue list", "RANK on Q2 revenue")], caption="Two lists, one rule")
            '''),
        code(r'''
            kit.check("the frequency list puts orders first", max(r["q2_orders"] for r in freq_list) == max(spread)
                      and min(r["q2_orders"] for r in freq_list) >= 2)
            kit.check("the second key leaves no crowd at the line", len(freq_list) <= 50)
            two_kept = [r["q2_revenue"] for r in freq_list if r["q2_orders"] == 2]
            two_left = [r["q2_revenue"] for r in core if r["q2_orders"] == 2 and r["customer_id"] not in {f["customer_id"] for f in freq_list}]
            kit.check("among members with two orders, the list keeps the ones who spent more",
                      not two_left or not two_kept or min(two_kept) >= max(two_left))
            '''),
        md("""
        ## Step 5. How many members do the two lists share, and how far apart are they in rupees?

        Where this is used at work: before a team argues over two definitions, it measures how much
        the answer actually changes.
        """),
        code(r'''
            # TODO 5. Which query counts the members who are on both lists?
            #   a) An INNER JOIN of the two lists on customer_id, counting the rows it returns
            #   b) A LEFT JOIN from the revenue list to the frequency list, counting all the rows it returns
            #   c) UNION ALL of the two lists, counting the rows
            #   d) The two list counts subtracted, 50 less 50
            BOTH = __TODO5__
            f_ids, r_ids = {r["customer_id"] for r in freq_list}, {r["customer_id"] for r in rev_list}
            shared = {"a": len(f_ids & r_ids), "b": len(r_ids), "c": len(freq_list) + len(rev_list),
                      "d": len(freq_list) - len(rev_list)}[BOTH]
            only_freq = sorted(f_ids - r_ids)
            only_rev = sorted(r_ids - f_ids)
            kit.bars([("by orders, then revenue", sum(r["q2_revenue"] for r in freq_list)),
                      ("by revenue", sum(r["q2_revenue"] for r in rev_list))],
                     title="Q2 revenue each Retail-Core list carries", fmt=kit.rupees)
            kit.table(["list", "members", "Q2 revenue carried", "only on this list"],
                      [("by orders, then revenue", len(freq_list), kit.rupees(sum(r["q2_revenue"] for r in freq_list)), ", ".join(only_freq)),
                       ("by revenue", len(rev_list), kit.rupees(sum(r["q2_revenue"] for r in rev_list)), ", ".join(only_rev))],
                      caption=f"Members on both lists, by your query: {shared}")
            '''),
        code(r'''
            kit.check("your count of shared members is the overlap of the two lists", shared == len(f_ids & r_ids))
            kit.check("each list has members the other lacks", bool(only_freq) and bool(only_rev))
            '''),
        md("""
        ## Step 6. What do you tell the marketing lead?

        Where this is used at work: a definition argument ends when someone says what changes, by how
        much, and which choice they recommend.
        """),
        code(r'''
            # TODO 6. How far apart are the two lists in the Q2 revenue they carry?
            #   a) Rs 40
            #   b) Rs 2,950
            #   c) About Rs 1.2 lakh
            #   d) Nothing, since both lists hold fifty members
            GAP = __TODO6__

            # TODO 7. Which line goes to the marketing lead?
            #   a) "Rank Retail-Core by orders alone under RANK: 51 members ship, which honours the tie rule and protects frequency."
            #   b) "Rank by orders with Q2 revenue as the second key: fifty ship, 49 are on the revenue list too, and the lists differ by Rs 40."
            #   c) "Rank Retail-Core with DENSE_RANK on orders, so that every member who ordered the same shares a place on the list."
            #   d) "Keep the revenue list, since ranking by orders would drop the members whose quarters carry the most revenue."
            LINE = __TODO7__
            print("gap:", GAP, "| line:", LINE)
            '''),
        code(r'''
            carried_gap = abs(sum(r["q2_revenue"] for r in freq_list) - sum(r["q2_revenue"] for r in rev_list))
            kit.check("the gap you chose is the gap the two lists carry", {"a": 40, "b": 2950, "c": 120000, "d": 0}.get(GAP) == carried_gap)
            kit.check("the line is chosen", LINE in "abcd")
            kit.check_summary()
            '''),
    ]
    answers = {1: '"a"', 2: '"b"', 3: '"a"', 4: '"b"', 5: '"a"', 6: '"a"', 7: '"b"'}
    return cells, answers


# ---- END OF CHAPTERS ----


BUILDERS = {
    "ch1": lambda: (NB / "C2_W02_D03_01_top_fifty_STUDENT.ipynb", ch1()),
    "ch2": lambda: (NB / "C2_W02_D03_02_each_segment_STUDENT.ipynb", ch2()),
    "ch3": lambda: (NB / "C2_W02_D03_03_tie_rule_STUDENT.ipynb", ch3()),
    "ch4": lambda: (NB / "C2_W02_D03_04_falling_spend_STUDENT.ipynb", ch4()),
    "ch5": lambda: (NB / "C2_W02_D03_05_against_plan_STUDENT.ipynb", ch5()),
    "ch6": lambda: (NB / "C2_W02_D03_06_call_first_STUDENT.ipynb", ch6()),
}

TWINS = {
    "case": (NB / "C2_W02_D03_ex1_escalated_case_STUDENT.ipynb", SOL / "C2_W02_D03_ex1_escalated_case_solution_STUDENT.ipynb", case),
    "second": (NB / "C2_W02_D03_ex2_second_case_STUDENT.ipynb", SOL / "C2_W02_D03_ex2_second_case_solution_STUDENT.ipynb", second),
}


def main(names):
    for name in names:
        if name in TWINS:
            todo, sol, maker = TWINS[name]
            cells, answers = maker()
            print("building", todo, "and", sol)
            twin(todo, sol, cells, answers)
            scan(todo)
            scan(sol)
            continue
        path, cells = BUILDERS[name]()
        print("building", path)
        build(path, cells)
        scan(path)


if __name__ == "__main__":
    main(sys.argv[1:] or list(BUILDERS) + list(TWINS))
