"""Build the Week 2 Wednesday notebooks: three round notebooks, the escalated case twin and its solution.

Run from the repository root with the Kalpa warehouse up (PGHOST, PGUSER, PGPASSWORD, PGDATABASE, or
the kit's defaults):

    python3 content/W02/D3/internal/C2_W02_D03_build_notebooks_INTERNAL.py

Every round notebook and the solution are executed cold in their own folder by nb_make.build, so the
saved outputs are the ones a learner's Codespace produces. The TODO twin is written unexecuted, since
it stops at its first placeholder by design. Every query follows the SQL files in content/W02/D3/sql/
and exercises/solutions/C2_W02_D03_protect_list_solution_STUDENT.sql.
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from nb_make import SETUP, build, code, empty, md  # noqa: E402

DAY = ROOT / "content" / "W02" / "D3"
NB = DAY / "notebooks"
SOL = DAY / "exercises" / "solutions"

# ------------------------------------------------------------------ shared cells
HELPERS = r'''
import decimal


def show(rows, money=(), caption="", limit=15):
    """Query rows as the kit's table, with every rupee column in Indian grouping."""
    def cell(h, v):
        if v is None:
            return ""
        return kit.rupees(v) if h in money else str(v)
    headers = list(rows[0])
    body = [[cell(h, r[h]) for h in headers] for r in rows[:limit]]
    if len(rows) > limit:
        body.append(["..."] * len(headers))
    kit.table(headers, body, caption or f"{len(rows)} rows")


def crore(v):
    """A large rupee figure on a chart axis, in crore, so the tick labels stay short."""
    return f"Rs {v / 1e7:.2f} cr"


Q2_PER_MEMBER = """
    SELECT c.segment, o.customer_id, sum(o.amount) AS q2_revenue
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY c.segment, o.customer_id"""

SEGMENTS = ["Business", "Retail-Core", "Retail-Plus", "Student"]

def sql(query):
    """kit.sql with Postgres numerics turned into Python numbers, so charts and arithmetic take them."""
    def num(v):
        if isinstance(v, decimal.Decimal):
            return int(v) if v == v.to_integral_value() else float(v)
        return v
    return [{k: num(v) for k, v in row.items()} for row in kit.sql(query)]


first = sql("SELECT count(*) AS orders, sum(amount) FILTER (WHERE quarter = 'Q2') AS q2 FROM orders")[0]
print(f"The warehouse answered: {first['orders']:,} orders, Q2 booked {kit.rupees(first['q2'])}.")
'''

SETUP_CELL = SETUP + HELPERS

SETUP_MD = r"""
**Setup.** The first lines find `scripts/c2kit.py` by walking up from this folder and import it as
`kit`; the helper opens the Kalpa warehouse with the settings the Codespace exports. `sql` runs a
query through `kit.sql` and hands back rows whose amounts are plain Python numbers, `show` prints a
query's rows as a table with rupees in Indian grouping, and `Q2_PER_MEMBER` is Monday's definition
of Q2 revenue per member, the booked amount of the member's Q2 orders of every status, written once
so every query below starts from the same number.
"""


def map_cell(lit):
    """The day's picture beside the day's ladder, with this round lit."""
    return code(r'''
kit.side_by_side(
    kit.ladder(["Round 1\nwho goes on the protect list",
                "Round 2\nties at the fiftieth place",
                "Round 3\nfalling spend and the plan",
                "The escalated case\none file for Marketing"], lit=%d, show=False),
    kit.flow(["Q2 revenue per member\n227 rows",
              "a window\nPARTITION BY segment, ORDER BY revenue DESC",
              "227 rows kept\neach with its position",
              "filtered in a CTE\nposition at most 50"],
             kinds=["plain", "lit", "known", "known"], show=False),
    kit.flow(["Q2 revenue per member\n227 rows",
              "GROUP BY segment\n4 rows: how much per segment"],
             kinds=["plain", "bad"], show=False),
)
''' % lit)


# ================================================================== Round 1
def round_one():
    cells = [
        md(r"""
# Who goes on the protect list?

**Week 2, Wednesday. Round 1 of 3: SQL window functions.** By the end of this notebook you can
rank members inside their own segment without losing a row, keep the first fifty of each segment
with a named step, and say how much of each segment's revenue the list covers.

> **Marketing asks.** "Retail-Plus frequency is the problem, so we want to protect our best members
> before they drift. Give us the top fifty customers by Q2 revenue in each segment, and flag anyone
> whose monthly spend has fallen for two months running. And Meera wants to see revenue accumulate
> week by week against the plan line, so we know by mid-quarter whether we are on track."

> **Kavya's review, at the end of this round.** "Before you send a list, count it by the group the
> person asked about. A top fifty that hands the Retail-Plus team eleven names answers a question
> nobody asked."

Monday built the suite that reported Q2 booked revenue of Rs 9,84,00,000, and Tuesday joined
payments onto orders and learned to count rows before and after every join. This round starts from
Monday's definition of revenue: Q2 revenue per member is the booked amount of the member's Q2
orders, of every status. The SQL behind every cell is `sql/C2_W02_D03_01_windows_walk_STUDENT.sql`.
"""),
        md(SETUP_MD),
        code(SETUP_CELL),
        map_cell(0),
        # ---------------------------------------------------------- level 1
        md(r"""
## 1. GROUP BY gives one row per member, and one row per segment

Marketing's list is made of members, so the first step collapses 462 Q2 orders into one row per
member, and a second GROUP BY collapses those into one row per segment to show how many members
each segment has to rank at all.

**Predict before you run.** How many rows does the per-member query return? a) 1,000, one per
order in the table; b) 462, one per Q2 order; c) 227, one per member who bought in Q2; d) 340, one
per customer in the table.
"""),
        code(r'''
per_member = sql(Q2_PER_MEMBER + "\n    ORDER BY q2_revenue DESC")
by_segment = sql("""
    SELECT c.segment, count(DISTINCT o.customer_id) AS q2_buyers,
           (SELECT count(*) FROM customers k WHERE k.segment = c.segment) AS customers,
           sum(o.amount) AS q2_revenue
    FROM   orders o
    JOIN   customers c USING (customer_id)
    WHERE  o.quarter = 'Q2'
    GROUP  BY c.segment
    ORDER  BY c.segment""")
print(len(per_member), "rows, one per member who bought in Q2")
show(by_segment, money=("q2_revenue",), caption="One row per segment: how much, and how many members to rank")
kit.columns([r["segment"] for r in by_segment],
            [("customers in the table", [r["customers"] for r in by_segment]),
             ("members who bought in Q2", [r["q2_buyers"] for r in by_segment])],
            title="Two segments have fewer than fifty Q2 buyers to rank at all", lit=(0, 3))
'''),
        code(r'''
kit.bars([(r["segment"], r["q2_revenue"]) for r in by_segment], fmt=kit.rupees, lit=(0,),
         title="Q2 booked revenue by segment: one Business order outweighs a retail member's year")
'''),
        md(r"""
**What happened.** The answer is c. Of 340 customers, 227 bought in Q2, and GROUP BY hands back one
row per member with the member's Q2 total. The segment view shows why a single top fifty will
mislead: Business books Rs 9,75,84,600 of the quarter's Rs 9,84,00,000 from 35 members, while the 96
Retail-Core buyers together book Rs 3,66,250. Business and Student have 35 and 20 Q2 buyers, so a
top fifty in those segments can only ever be everyone who bought.
"""),
        code(r'''
kit.check("one row per Q2 buyer", len(per_member) == 227, f"got {len(per_member)}")
kit.check("the members add back to Monday's Q2 total",
          sum(r["q2_revenue"] for r in per_member) == 98400000,
          kit.rupees(sum(r["q2_revenue"] for r in per_member)))
kit.check("four segments, and their buyers add to 227",
          len(by_segment) == 4 and sum(r["q2_buyers"] for r in by_segment) == 227)
'''),
        # ---------------------------------------------------------- level 2: the trap
        md(r"""
## 2. The trap: one top fifty over the whole table hands Retail-Plus eleven members

**The plausible wrong answer.** A hurried analyst reads "top fifty by Q2 revenue", sorts every
member by revenue and keeps fifty. The query runs, returns exactly fifty rows and looks finished.

**Predict before you run.** How many of those fifty are Retail-Plus members? a) fifty, since they
asked about Retail-Plus; b) about twelve, a quarter of the list for each of four segments; c) a
handful, fewer than a quarter; d) none at all.
"""),
        code(r'''
hurried = sql(f"""
    WITH q2 AS ({Q2_PER_MEMBER}),
    top_fifty AS (SELECT * FROM q2 ORDER BY q2_revenue DESC, customer_id LIMIT 50)
    SELECT segment, count(*) AS members_on_the_list, min(q2_revenue) AS smallest_on_the_list
    FROM   top_fifty
    GROUP  BY segment""")
on_list = {r["segment"]: r["members_on_the_list"] for r in hurried}
smallest = {r["segment"]: r["smallest_on_the_list"] for r in hurried}
show(hurried, money=("smallest_on_the_list",), caption="The whole-table top fifty, counted by segment")
kit.columns(SEGMENTS, [("on the whole-table top fifty", [on_list.get(s, 0) for s in SEGMENTS])],
            title="Fifty rows, and Student has none of them", lit=(2, 3))
'''),
        md(r"""
**What happened.** The answer is c: 11 Retail-Plus members, 4 Retail-Core, 35 Business and no
Student at all.

**Why it is wrong.** Marketing asked for fifty per segment, because each segment team protects its
own members. This list hands the Retail-Plus team 11 names to protect and the Student team none,
because one Business order outweighs a year of a retail member's spend. The number fifty is right
and the list answers a question nobody asked. The check that exposes it costs one GROUP BY: count
the list by the group the stakeholder named.
"""),
        code(r'''
core = [r["q2_revenue"] for r in per_member if r["segment"] == "Retail-Core"]
kit.strip(core, markers=[("whole-table cut", smallest["Retail-Core"], "bad"),
                         ("50th in the segment", sorted(core, reverse=True)[49], "good")],
          title="Retail-Core's 96 buyers: 4 clear the whole-table cut, 50 clear their own segment's")
kit.check("the whole-table list has fifty rows", sum(on_list.values()) == 50)
kit.check("counted by segment it is 35, 4, 11 and 0",
          [on_list.get(s, 0) for s in SEGMENTS] == [35, 4, 11, 0], str(on_list))
kit.check("the smallest Retail-Plus member on it spent Rs 9,600", smallest["Retail-Plus"] == 9600,
          kit.rupees(smallest["Retail-Plus"]))
'''),
        md(r"""
**The fix** is the window in level 3, `PARTITION BY segment`, which restarts the count in each
segment. Level 4 counts what changed: Retail-Plus goes from 11 members to 50, Retail-Core from 4 to
50 and Student from none to all 20 of its Q2 buyers, while Business keeps its 35.
"""),
        # ---------------------------------------------------------- level 3: the window
        md(r"""
## 3. A window keeps every row and restarts the count in each segment

The fix is a window function. `row_number() OVER (PARTITION BY segment ORDER BY q2_revenue DESC,
customer_id)` adds a position to every member: PARTITION BY sets the group the count restarts in,
and ORDER BY inside the window sets who comes first. `customer_id` breaks an exact tie so two runs
give the same numbers; Round 2 is about what that choice means.

**Predict before you run.** How many rows does the window query return? a) 4, one per segment;
b) 50, the list; c) 200, fifty for each of four segments; d) 227, every member with a position.
"""),
        code(r'''
ranked = sql(f"""
    WITH q2 AS ({Q2_PER_MEMBER})
    SELECT segment, customer_id, q2_revenue,
           row_number() OVER (PARTITION BY segment ORDER BY q2_revenue DESC, customer_id) AS position
    FROM   q2
    ORDER  BY segment, position""")
print(len(ranked), "rows kept, each with its position inside its own segment")
show([r for r in ranked if r["position"] <= 3], money=("q2_revenue",),
     caption="The first three of every segment: the count restarts at 1 in each")
top_core = [r for r in ranked if r["segment"] == "Retail-Core"][:10]
kit.bars([(f'{r["position"]}. {r["customer_id"]}', r["q2_revenue"]) for r in top_core],
         fmt=kit.rupees, title="Retail-Core's first ten by Q2 revenue, positioned inside the segment")
'''),
        md(r"""
**What happened.** The answer is d. The window added a column and removed nothing: 227 rows in, 227
rows out, and every segment starts again at 1. GROUP BY answers how much per group; a window keeps
every row and says where each row stands.

The obvious next line keeps the first fifty with `WHERE position <= 50` written straight onto the
window. Postgres refuses it, and the message is worth reading once.
"""),
        code(r'''
with kit.expect_error() as err:
    sql(f"""
        WITH q2 AS ({Q2_PER_MEMBER})
        SELECT segment, customer_id, q2_revenue
        FROM   q2
        WHERE  row_number() OVER (PARTITION BY segment ORDER BY q2_revenue DESC, customer_id) <= 50""")
'''),
        md(r"""
WHERE runs before the window is computed, so there is no position yet to filter on. The fix is a
named step: compute the position in a CTE, then filter the CTE from outside.
"""),
        code(r'''
kept = sql(f"""
    WITH q2 AS ({Q2_PER_MEMBER}),
    ranked AS (
        SELECT segment, customer_id, q2_revenue,
               row_number() OVER (PARTITION BY segment ORDER BY q2_revenue DESC, customer_id) AS position
        FROM   q2
    )
    SELECT segment, count(*) AS members_on_the_list, max(position) AS last_position
    FROM   ranked
    WHERE  position <= 50
    GROUP  BY segment
    ORDER  BY segment""")
show(kept, caption="The position filtered outside the CTE")
kit.check("the window error names WHERE", err.message is not None and "WHERE" in err.message,
          (err.message or "").splitlines()[0])
kit.check("the window kept all 227 rows", len(ranked) == 227)
kit.check("every segment restarts at position 1",
          sorted(r["segment"] for r in ranked if r["position"] == 1) == SEGMENTS)
'''),
        # ---------------------------------------------------------- level 4
        md(r"""
## 4. The per-segment list has 155 rows and covers most of each segment's revenue

The list Marketing asked for is the CTE filtered at position fifty, per segment. The next question
Marketing will ask is how much of each segment's Q2 revenue sits on its list, which is a second
window, `sum(q2_revenue) OVER (PARTITION BY segment)`, a segment total carried on every row.

**Predict before you run.** What share of Retail-Core's Q2 revenue do its top fifty members carry?
a) all of it; b) about three quarters; c) about half, since fifty is about half of 96 buyers;
d) under a third.
"""),
        code(r'''
cover = sql(f"""
    WITH q2 AS ({Q2_PER_MEMBER}),
    ranked AS (
        SELECT q2.*,
               row_number() OVER (PARTITION BY segment ORDER BY q2_revenue DESC, customer_id) AS position,
               sum(q2_revenue) OVER (PARTITION BY segment) AS segment_revenue
        FROM   q2
    )
    SELECT segment,
           count(*) FILTER (WHERE position <= 50) AS on_the_list,
           count(*) AS q2_buyers,
           round(100.0 * sum(q2_revenue) FILTER (WHERE position <= 50) / max(segment_revenue), 1)
               AS share_of_segment_revenue_pct
    FROM   ranked
    GROUP  BY segment
    ORDER  BY segment""")
listed = {r["segment"]: r["on_the_list"] for r in cover}
share = {r["segment"]: float(r["share_of_segment_revenue_pct"]) for r in cover}
show(cover, caption="The protect list per segment, and the share of the segment's Q2 revenue it carries")
kit.columns(SEGMENTS, [("whole-table top fifty", [on_list.get(s, 0) for s in SEGMENTS]),
                       ("fifty per segment", [listed[s] for s in SEGMENTS])],
            title="Retail-Plus goes from 11 members to 50 when the count restarts per segment", lit=(2,))
'''),
        code(r'''
kit.bars([(s, share[s]) for s in SEGMENTS], fmt=lambda v: f"{v:.1f} percent", lit=(1, 2),
         title="Share of each segment's Q2 revenue on its list")
boundary = [r for r in ranked if r["segment"] == "Retail-Core" and r["position"] in (50, 51)]
show(boundary, money=("q2_revenue",), caption="Retail-Core either side of the line")
'''),
        md(r"""
**What happened.** The answer is b: Retail-Core's fifty carry 76.1 percent of the segment's Q2
revenue, and Retail-Plus's fifty carry 85.5 percent. The list has 155 rows, 35 Business, 50
Retail-Core, 50 Retail-Plus and 20 Student, so Retail-Plus went from 11 members on the hurried list
to 50. Business and Student have fewer than fifty Q2 buyers, so their "top fifty" is every member
who bought in Q2 and carries 100 percent of the segment; the list should say so in its header,
or Marketing will read 35 and 20 as a shortfall. In Retail-Core the fiftieth member spent Rs 2,980
and the fifty-first Rs 2,950, thirty rupees apart, which is why Round 2 asks what happens at the
line.
"""),
        code(r'''
kit.check("the per-segment list has 155 rows", sum(listed.values()) == 155, str(listed))
kit.check("35, 50, 50 and 20 per segment", [listed[s] for s in SEGMENTS] == [35, 50, 50, 20])
kit.check("Retail-Plus gained 39 members over the hurried list", listed["Retail-Plus"] - on_list["Retail-Plus"] == 39)
kit.check("Business and Student lists carry all their Q2 revenue",
          share["Business"] == 100.0 and share["Student"] == 100.0)
kit.check("Retail-Core's list carries 76.1 percent", share["Retail-Core"] == 76.1, f"{share['Retail-Core']}")
kit.check("Retail-Core's line sits between Rs 2,980 and Rs 2,950",
          [r["q2_revenue"] for r in boundary] == [2980, 2950])
'''),
        # ---------------------------------------------------------- SUM
        md(r"""
## What this round established

> **Kavya's review.** "Before you send a list, count it by the group the person asked about. A top
> fifty that hands the Retail-Plus team eleven names answers a question nobody asked. And put the
> buyer count beside Business and Student, so nobody reads 35 as a list that fell short."
"""),
        code(r'''
kit.vflow(["one row per member\nGROUP BY, 227 rows",
           "the hurried top fifty\n35, 4, 11 and 0 by segment",
           "a window\nPARTITION BY segment keeps all 227 rows",
           "filtered in a CTE\nposition at most 50, since WHERE cannot see a window",
           "the protect list\n155 rows: 35, 50, 50 and 20"],
          kinds=["known", "bad", "lit", "known", "good"],
          title="Round 1, from one row per member to a list per segment")
kit.table(["Question", "Answer", "Why it matters to Marketing"],
          [("How many members bought in Q2?", "227", "Only buyers can be ranked by Q2 revenue."),
           ("What does one top fifty hand Retail-Plus?", "11 members", "The team would protect a fifth of its list."),
           ("What does fifty per segment hand Retail-Plus?", "50 members", "The list the team asked for."),
           ("How many rows is the protect list?", "155", "Business and Student ship every Q2 buyer."),
           ("What share of Retail-Core revenue is on it?", "76.1 percent", "Fifty members carry three quarters of the segment.")],
          caption="What Round 1 established, with ROW_NUMBER breaking ties by customer_id")
'''),
        md(r"""
### In the interview

**[S] Top-3 per group: GROUP BY or a window, and why?** "A window. GROUP BY collapses each group to
one row, so it can tell me the biggest amount per segment and cannot tell me who the second and third
members are. I compute `row_number()` or `rank()` over `PARTITION BY segment ORDER BY revenue DESC`
in a CTE, which keeps every member with a position inside its own segment, and then filter the CTE
on position at most three. Before I hand it over I count the result by the group column, because a
list of the right length can still hold the wrong mix, and I say which ranking function I used,
since ties decide whether a group returns three rows or four."

**[F] Why can a window function not sit inside WHERE, and what do you do instead?** "Because of the
order a query is evaluated in. FROM and the joins run first, then WHERE, then GROUP BY and HAVING,
and only then are the window functions computed, just before the SELECT list and ORDER BY. At the
moment WHERE runs there is no position to compare with, so Postgres refuses with 'window functions
are not allowed in WHERE'. I compute the window in a CTE or a subquery, which gives the position a
name, and filter it from the outer query. Postgres 16 has no QUALIFY clause, so the CTE is the
portable answer."

**[S] What is the difference between GROUP BY and PARTITION BY?** "GROUP BY changes the grain of
the result: 227 member rows become 4 segment rows, and every column has to be grouped or
aggregated. PARTITION BY lives inside a window and leaves the grain alone: all 227 rows come back,
and the calculation, a rank or a segment total, restarts in each partition. I reach for GROUP BY
when the question is how much per group, and for PARTITION BY when the question is where each row
stands within its group, or what share of its group it carries."
"""),
        md(r"""
### Depth: the same list without a window, and why nobody writes it that way

Before window functions, a per-group top N was written as a correlated subquery: keep a member when
fewer than fifty members of the same segment rank above them. It returns the same 155 rows, it
reads the Q2 table once for every member, and it hides the tie rule inside a comparison, where a
reader has to work out that `>` with `customer_id` as a tiebreaker behaves like ROW_NUMBER. The
window says the rule in its function name. The diagram is the logical order a query is evaluated
in, which is the whole reason the WHERE error exists.
"""),
        code(r'''
correlated = sql(f"""
    WITH q2 AS ({Q2_PER_MEMBER})
    SELECT a.segment, count(*) AS members_on_the_list
    FROM   q2 a
    WHERE  (SELECT count(*) FROM q2 b
            WHERE  b.segment = a.segment
              AND  (b.q2_revenue > a.q2_revenue
                    OR (b.q2_revenue = a.q2_revenue AND b.customer_id < a.customer_id))) < 50
    GROUP  BY a.segment
    ORDER  BY a.segment""")
show(correlated, caption="The correlated-subquery version, counted by segment")
kit.flow(["FROM and joins", "WHERE", "GROUP BY and HAVING", "window functions", "SELECT, ORDER BY, LIMIT"],
         kinds=["plain", "bad", "plain", "lit", "plain"],
         title="The logical order: WHERE runs before any window exists")
kit.check("the correlated version ships the same 35, 50, 50 and 20",
          [r["members_on_the_list"] for r in correlated] == [listed[s] for s in SEGMENTS])
'''),
        code(r'''
kit.check_summary()
print("Next: Round 2 asks what happens at the fiftieth place when two members spent the same.")
'''),
    ]
    build(NB / "C2_W02_D03_01_windows_STUDENT.ipynb", cells)
    return cells


# ================================================================== Round 2
def round_two():
    cells = [
        md(r"""
# How many make the list when two members tie?

**Week 2, Wednesday. Round 2 of 3: SQL window functions.** By the end of this notebook you can
say what ROW_NUMBER, RANK and DENSE_RANK do with a tie, count the rows each one ships at the line,
and write the tie rule down as a business decision with its count beside it.

> **The head of Retail-Plus asks.** "Ties matter. If two members spent the same, I want them ranked
> the same, and I want to know how many made the top fifty, not forty-nine because of a tie."

> **Kavya's review, at the end of this round.** "The tie rule is a business decision written as a
> function name. Pick RANK, and put how many it shipped in the same line as the list."

Round 1 built the protect list with `row_number()` inside each segment: 155 rows, 35 Business, 50
Retail-Core, 50 Retail-Plus and 20 Student, with `customer_id` quietly deciding any tie. This round
asks what that quiet choice did. The SQL behind every cell is
`sql/C2_W02_D03_02_protect_list_STUDENT.sql`.
"""),
        md(SETUP_MD),
        code(SETUP_CELL),
        map_cell(1),
        # ---------------------------------------------------------- level 1
        md(r"""
## 1. Three functions, one tie: RANK gives 1, 1, 3

Six invented members, A to F, labelled invented because they exist only to show the mechanism on
one screen. A and B spent Rs 7,500 each and lead the list; D and E tie lower down on Rs 5,200.

**Predict before you run.** What does `rank()` give A, B and C? a) 1, 2, 3; b) 1, 1, 2;
c) 1, 1, 3; d) 1, 1, 1.
"""),
        code(r'''
invented = sql("""
    WITH invented (member, spend) AS (
        VALUES ('A', 7500), ('B', 7500), ('C', 6000), ('D', 5200), ('E', 5200), ('F', 4100)
    )
    SELECT member, spend,
           row_number() OVER (ORDER BY spend DESC, member) AS row_number,
           rank()       OVER (ORDER BY spend DESC)         AS rank,
           dense_rank() OVER (ORDER BY spend DESC)         AS dense_rank
    FROM   invented
    ORDER  BY spend DESC, member""")
show(invented, money=("spend",), caption="Six invented members, three functions")
kit.columns([r["member"] for r in invented],
            [("row_number", [r["row_number"] for r in invented]),
             ("rank", [r["rank"] for r in invented]),
             ("dense_rank", [r["dense_rank"] for r in invented])],
            title="Invented members: the three functions part company at every tie")
'''),
        md(r"""
**What happened.** The answer is c. RANK gives tied members the same position and then skips, so
after two members share 1 the next member is 3: the position still says how many members spent
more. DENSE_RANK shares the position without the gap, so C is 2 and F is 4. ROW_NUMBER never shares:
A and B get 1 and 2, and only the tiebreaker inside the window, here the member's letter, decides
which is which.
"""),
        code(r'''
kit.check("ROW_NUMBER numbers 1 to 6 with no repeats", [r["row_number"] for r in invented] == [1, 2, 3, 4, 5, 6])
kit.check("RANK shares and skips: 1, 1, 3, 4, 4, 6", [r["rank"] for r in invented] == [1, 1, 3, 4, 4, 6])
kit.check("DENSE_RANK shares without a gap: 1, 1, 2, 3, 3, 4",
          [r["dense_rank"] for r in invented] == [1, 1, 2, 3, 3, 4])
'''),
        # ---------------------------------------------------------- level 2
        md(r"""
## 2. The tie at the line: each rule ships a different number of rows

Invented again: Marketing wants a top four, and the fourth and fifth members both spent Rs 7,400.
`count(*) OVER (PARTITION BY spend)` carries the size of each member's tie, which gives a fourth
rule, "whole ties only": ship a tied group only if all of it fits.

**Predict before you run.** How many rows does `rank() <= 4` ship? a) 3; b) 4; c) 5; d) 6.
"""),
        code(r'''
line = sql("""
    WITH invented (member, spend) AS (
        VALUES ('A', 9100), ('B', 8800), ('C', 8200), ('D', 7400), ('E', 7400), ('F', 6900)
    ),
    r AS (
        SELECT member, spend,
               row_number() OVER (ORDER BY spend DESC, member) AS rn,
               rank()       OVER (ORDER BY spend DESC)         AS rk,
               dense_rank() OVER (ORDER BY spend DESC)         AS dr,
               count(*)     OVER (PARTITION BY spend)          AS tied_with
        FROM   invented
    )
    SELECT count(*) FILTER (WHERE rn <= 4)                 AS row_number_ships,
           count(*) FILTER (WHERE rk <= 4)                 AS rank_ships,
           count(*) FILTER (WHERE dr <= 4)                 AS dense_rank_ships,
           count(*) FILTER (WHERE rk + tied_with - 1 <= 4) AS whole_ties_only_ships
    FROM   r""")[0]
kit.bars([(k.replace("_ships", "").replace("_", " "), v) for k, v in line.items()], lit=(1,),
         title="Invented top four with a tie at fourth: rows each rule ships")
kit.decision_ladder(["F Rs 6,900", "E Rs 7,400, tied for fourth", "D Rs 7,400, tied for fourth",
                     "C Rs 8,200", "B Rs 8,800", "A Rs 9,100"],
                    cut_at=1, title="Invented: a line drawn after four rows cuts the tied pair in two")
'''),
        md(r"""
**What happened.** The answer is c. RANK ships five, because D and E share fourth place and both
belong on the list. DENSE_RANK also ships five here. ROW_NUMBER ships exactly four and drops E, for
no reason except that E sorts after D. "Whole ties only" ships three, dropping a member who spent
exactly what the fourth did, which is the forty-nine the head of Retail-Plus forbade.
"""),
        code(r'''
kit.check("ROW_NUMBER ships exactly four", line["row_number_ships"] == 4)
kit.check("RANK ships five: the tied pair travels together", line["rank_ships"] == 5)
kit.check("whole ties only ships three", line["whole_ties_only_ships"] == 3)
'''),
        # ---------------------------------------------------------- level 3: the trap
        md(r"""
## 3. The trap: DENSE_RANK sounds like "ties rank the same" and ships 52

**The plausible wrong answer.** An analyst hears "if two members spent the same, rank them the
same", reaches for the function whose name sounds closest, and writes `dense_rank() <= 50`. On the
invented top four it agreed with RANK, so it looks safe. Run it on Retail-Core, where there is no
tie at the fiftieth place at all.

**Predict before you run.** How many Retail-Core members does `dense_rank() <= 50` ship? a) 49;
b) 50; c) 51; d) 52.
"""),
        code(r'''
RULES = f"""
    WITH q2 AS ({Q2_PER_MEMBER}),
    r AS (
        SELECT segment, customer_id, q2_revenue,
               row_number() OVER (PARTITION BY segment ORDER BY q2_revenue DESC, customer_id) AS rn,
               rank()       OVER (PARTITION BY segment ORDER BY q2_revenue DESC)              AS rk,
               dense_rank() OVER (PARTITION BY segment ORDER BY q2_revenue DESC)              AS dr,
               count(*)     OVER (PARTITION BY segment, q2_revenue)                           AS tied_with
        FROM   q2
    )"""
core = sql(RULES + """
    SELECT count(*) FILTER (WHERE rn <= 50)                 AS row_number_ships,
           count(*) FILTER (WHERE rk <= 50)                 AS rank_ships,
           count(*) FILTER (WHERE dr <= 50)                 AS dense_rank_ships,
           count(*) FILTER (WHERE rk + tied_with - 1 <= 50) AS whole_ties_only_ships
    FROM   r
    WHERE  segment = 'Retail-Core'""")[0]
kit.columns(["row_number", "rank", "dense_rank", "whole ties only"],
            [("Retail-Core rows shipped", list(core.values()))],
            title="Retail-Core top fifty: three rules ship 50, DENSE_RANK ships 52", lit=(2,))
'''),
        md(r"""
**What happened.** The answer is d, 52.

**Why it is wrong.** DENSE_RANK closes the gaps a tie leaves, so every tie higher up the list pulls
the members below it one place up. By the fiftieth dense position Retail-Core has run through 52
members, and two members who ranked 51st and 52nd by spend are on a list Marketing will act on. The
report says "top fifty" and ships 52, and nobody at the line tied. The check that exposes it is to
read positions 44 to 54 with all three functions side by side.
"""),
        code(r'''
edge = sql(RULES + """
    SELECT rn, rk, dr, customer_id, q2_revenue
    FROM   r
    WHERE  segment = 'Retail-Core' AND rn BETWEEN 44 AND 54
    ORDER  BY rn""")
show(edge, money=("q2_revenue",), caption="Retail-Core, positions 44 to 54, all three functions")
extra = [r for r in edge if r["dr"] <= 50 and r["rk"] > 50]
kit.bars([(f'{r["rn"]}. {r["customer_id"]}', r["q2_revenue"]) for r in edge], fmt=kit.rupees,
         lit=[i for i, r in enumerate(edge) if r in extra],
         title="Dark bars: on the DENSE_RANK list, ranked 51st and 52nd by spend")
kit.check("DENSE_RANK ships 52 in Retail-Core", core["dense_rank_ships"] == 52)
kit.check("the two extra members rank 51 and 52 by RANK", [r["rk"] for r in extra] == [51, 52],
          ", ".join(r["customer_id"] for r in extra))
kit.check("ROW_NUMBER and RANK agree on 50: no tie sits at the line", core["row_number_ships"] == core["rank_ships"] == 50)
'''),
        md(r"""
**The fix.** RANK inside each segment. In Retail-Core it takes the list from 52 rows back to 50,
removing the two members at 51st and 52nd, Rs 2,950 and Rs 2,910, Rs 5,860 of Q2 revenue that was
never in the top fifty.
"""),
        # ---------------------------------------------------------- level 4: the rule
        md(r"""
## 4. The rule written down: RANK inside each segment, and the count said out loud

RANK does both things the head of Retail-Plus asked for: tied members share a position, and every
member at or above fiftieth ships, so nobody at the line is dropped by a coin toss. The rule costs
one sentence in the report, the number of members shipped per segment and why.

**Predict before you run.** How many Business and Student members does `rank() <= 50` ship?
a) fifty each; b) every Q2 buyer, 35 and 20; c) fewer than their buyers, since ties shrink a list;
d) it cannot be said until the ties are known.
"""),
        code(r'''
rule = sql(RULES + """
    SELECT segment,
           count(*) FILTER (WHERE rk <= 50) AS members_on_the_list,
           max(rk) FILTER (WHERE rk <= 50)  AS last_position,
           count(*)                         AS q2_buyers
    FROM   r
    WHERE  segment <> 'Retail-Plus'
    GROUP  BY segment
    ORDER  BY segment""")
shipped = {r["segment"]: r["members_on_the_list"] for r in rule}
show(rule, caption="RANK within each segment, three segments shown; Retail-Plus is your turn below")
kit.columns([r["segment"] for r in rule],
            [("Q2 buyers", [r["q2_buyers"] for r in rule]),
             ("shipped by RANK", [r["members_on_the_list"] for r in rule])],
            title="RANK ships every buyer where a segment has fewer than fifty")
'''),
        md(r"""
**What happened.** The answer is b. Business and Student ship all 35 and 20 buyers, and Retail-Core
ships 50 with its last position at 50, because no Retail-Core tie sits on the line.

**ROW_NUMBER's coin toss.** Without a tiebreaker, `row_number() OVER (ORDER BY spend DESC)` numbers
tied rows in whatever order the database reads them, so a member can be fiftieth on Monday's run and
fifty-first on Tuesday's with the same spend. Adding `customer_id` to the window's ORDER BY makes the
toss repeatable, and it is still a toss: the member with the smaller id wins, which is no reason a
business would give. The cell below shows it on the invented pair, fed to the database in two
different row orders.
"""),
        code(r'''
def winner(values_sql, tiebreak):
    order = "spend DESC, member" if tiebreak else "spend DESC"
    return sql(f"""
        WITH invented (member, spend) AS (VALUES {values_sql})
        SELECT member FROM (SELECT member, row_number() OVER (ORDER BY {order}) AS rn FROM invented) x
        WHERE rn = 1""")[0]["member"]

orders_in = {"A then B": "('A', 7500), ('B', 7500), ('C', 6000)",
             "B then A": "('B', 7500), ('A', 7500), ('C', 6000)"}
kit.table(["rows fed in", "first place, no tiebreaker", "first place, member as tiebreaker"],
          [(k, winner(v, False), winner(v, True)) for k, v in orders_in.items()],
          caption="Invented: with a tiebreaker the winner never depends on how the rows arrived")
kit.check("with a tiebreaker both feeds give the same first place",
          len({winner(v, True) for v in orders_in.values()}) == 1)
kit.check("RANK ships every Business and Student buyer", shipped["Business"] == 35 and shipped["Student"] == 20)
kit.check("RANK ships 50 in Retail-Core", shipped["Retail-Core"] == 50)
'''),
        md(r'''
**Your turn.** Retail-Plus is the segment whose head asked the question, so run the same count on
it yourself. Type these lines into the empty cell below and run them, then write the one sentence
the report carries: the rule, the count, and why.

```python
rp = sql(RULES + """
    SELECT count(*) FILTER (WHERE rn <= 50)                 AS row_number_ships,
           count(*) FILTER (WHERE rk <= 50)                 AS rank_ships,
           count(*) FILTER (WHERE dr <= 50)                 AS dense_rank_ships,
           count(*) FILTER (WHERE rk + tied_with - 1 <= 50) AS whole_ties_only_ships
    FROM   r WHERE segment = 'Retail-Plus'""")
show(rp)
show(sql(RULES + """
    SELECT rn, rk, dr, customer_id, q2_revenue FROM r
    WHERE  segment = 'Retail-Plus' AND rn BETWEEN 44 AND 54 ORDER BY rn"""), money=("q2_revenue",))
```

The sentence has this shape: "We ranked with RANK inside each segment, so tied members share a
place: the Retail-Plus list carries N members, because ..."
'''),
        empty(),
        # ---------------------------------------------------------- SUM
        md(r"""
## What this round established

> **Kavya's review.** "The tie rule is a business decision written as a function name. Pick RANK,
> and put how many it shipped in the same line as the list. A list that says fifty and ships
> fifty-two will be found by the first person who counts it."
"""),
        code(r'''
kit.vflow(["the ask\nties rank the same, and say how many made it",
           "ROW_NUMBER\nnever shares; a coin toss decides the line",
           "DENSE_RANK\nshares and closes gaps; ships 52 in Retail-Core",
           "RANK\nshares and skips; everyone at the line ships",
           "the report\nthe rule, the count per segment, and why"],
          kinds=["plain", "bad", "bad", "lit", "good"],
          title="Round 2: the tie rule is a function name")
kit.table(["Rule", "What it does with a tie", "Retail-Core ships"],
          [("row_number", "Never shares a position; the tiebreaker decides who is in.", core["row_number_ships"]),
           ("rank", "Shares the position and leaves a gap after it.", core["rank_ships"]),
           ("dense_rank", "Shares the position and closes the gap, so later members move up.", core["dense_rank_ships"]),
           ("whole ties only", "Drops a tied group that does not fit whole.", core["whole_ties_only_ships"])],
          caption="What Round 2 established")
'''),
        md(r"""
### In the interview

**[S] RANK, DENSE_RANK and ROW_NUMBER on a tie.** "Take two members tied on the top spend. ROW_NUMBER
gives them 1 and 2 and the third member 3; which of the pair gets 1 depends on the tiebreaker in the
window's ORDER BY, or on nothing at all if there is none. RANK gives both 1 and the third member 3,
so a position still says how many rows came before it. DENSE_RANK gives both 1 and the third member
2, so there are no gaps and the positions stop counting rows. On the invented list A to F that is
1, 1, 3 for RANK and 1, 1, 2 for DENSE_RANK."

**[D] The business says 'ties rank the same'; which function, and how many rows might the top-N
report ship?** "RANK, filtered at position N or better. It ships at least N rows whenever the group
has N members, and more than N when a tie straddles the line, one extra row for each extra member
of that tie. I would not use DENSE_RANK, because it ships more than N rows even with no tie at the
line: every tie above the line pulls the later members up, which is how Retail-Core's top fifty
became 52. The report then states the count and the reason in one line."

**[F] Your top-fifty list came back with 51 rows. What do you tell the stakeholder, and is it a
bug?** "First I find out whether it is a tie or a mistake: I count members at the last position and
read the rows either side of the line with ROW_NUMBER, RANK and DENSE_RANK side by side. If two
members share fiftieth on exactly the same spend and I ranked with RANK, it is the rule working, and
I tell the stakeholder that the list has 51 members because two tie at fiftieth, with both names.
If the extra row came from DENSE_RANK, or from a join that duplicated a member, it is a bug, and I
fix it before the list goes anywhere."
"""),
        md(r"""
### Depth: the rules a business might ask for, and the one column that serves them all

Every tie rule in this round can be written from two numbers per member, the RANK position and the
size of the member's tie, `count(*) OVER (PARTITION BY segment, q2_revenue)`. A member is in the
RANK list when the position is at most fifty; in the "whole ties only" list when the position plus
the tie size minus one is at most fifty; and at the line exactly when the position is at most fifty
and the position plus the tie size minus one is past it. That last test finds every tie that
straddles a line, in any segment, without reading a single name, which is the first query to run
when a count comes back one above what was asked for.
"""),
        code(r'''
straddle = sql(RULES + """
    SELECT segment, count(*) FILTER (WHERE rk <= 50 AND rk + tied_with - 1 > 50) AS members_in_a_tie_across_the_line
    FROM   r
    WHERE  segment <> 'Retail-Plus'
    GROUP  BY segment
    ORDER  BY segment""")
show(straddle, caption="Ties that straddle the fiftieth place, three segments")
kit.bars([(r["segment"], r["members_in_a_tie_across_the_line"]) for r in straddle],
         title="No tie straddles the line in these three segments")
kit.check("no tie crosses the line in Business, Retail-Core or Student",
          sum(r["members_in_a_tie_across_the_line"] for r in straddle) == 0)
'''),
        code(r'''
kit.check_summary()
print("Next: Round 3 asks whose monthly spend is falling, and whether the quarter is on plan.")
'''),
    ]
    build(NB / "C2_W02_D03_02_ties_STUDENT.ipynb", cells)
    return cells


# ================================================================== Round 3
def round_three():
    cells = [
        md(r"""
# Whose spend is falling, and is the quarter on plan?

**Week 2, Wednesday. Round 3 of 3: SQL window functions.** By the end of this notebook you can
compare each member's month with the member's own previous month, refuse to read a gap as a fall,
and build a running total that closes on the quarter's total and reads against the plan line.

> **Marketing asks.** "Flag anyone whose monthly spend has fallen for two months running. And Meera
> wants to see revenue accumulate week by week against the plan line, so we know by mid-quarter
> whether we are on track."

> **Kavya's review, at the end of this round.** "LAG reads the previous row, so partition by the
> member and check the previous row is last month. A running total is only as true as its order
> and its start: check it closes on the quarter's total."

Round 2 settled the tie rule: RANK inside each segment, with the count said out loud. This round
answers the other two parts of Marketing's ask. The flag means the member spent less in August than
in July, and less again in September than in August. The SQL behind every cell is
`sql/C2_W02_D03_03_falling_spend_STUDENT.sql`.
"""),
        md(SETUP_MD),
        code(SETUP_CELL + r'''
MONTHLY = """
    SELECT customer_id, date_trunc('month', order_date)::date AS month, sum(amount) AS spend
    FROM   orders
    GROUP  BY customer_id, date_trunc('month', order_date)"""
MONTHS = ["2026-04-01", "2026-05-01", "2026-06-01", "2026-07-01", "2026-08-01", "2026-09-01"]
LABELS = ["Apr", "May", "Jun", "Jul", "Aug", "Sep"]
'''),
        map_cell(2),
        # ---------------------------------------------------------- level 1
        md(r"""
## 1. The monthly spend table has a row only for a month with an order

A fall is a comparison between months, so the first step builds one row per member per month,
April to September, from every order of both quarters. C-0010, Retail-Core's biggest Q2 member, is
the worked example, because the member's spend fell in the plain way: July, then August, then
September, each lower.

**Predict before you run.** What does the table hold for a month in which a member placed no order?
a) a row with spend 0; b) a row with spend NULL; c) no row at all; d) a copy of the previous month.
"""),
        code(r'''
monthly = sql(MONTHLY + "\n    ORDER BY customer_id, month")
c0010 = [r for r in monthly if r["customer_id"] == "C-0010"]
show(c0010, money=("spend",), caption="C-0010, one row per month with an order")
by_month = {str(r["month"]): r["spend"] for r in c0010}
kit.line(LABELS, [("C-0010 monthly spend", [by_month.get(m) for m in MONTHS], "bad")], fmt=kit.rupees,
         title="C-0010: July, August and September each lower; May has no row, and the line joins across it")
'''),
        code(r'''
active = sql("""
    SELECT date_trunc('month', order_date)::date AS month, count(DISTINCT customer_id) AS members
    FROM   orders GROUP BY 1 ORDER BY 1""")
kit.columns(LABELS, [("members with an order that month", [r["members"] for r in active])],
            title="Members with a row in each month of the table")
'''),
        md(r"""
**What happened.** The answer is c. C-0010 bought in April, June, July, August and September, and
the table has five rows for the member: May has no row at all. That absence is what the rest of the
round turns on. For C-0010 the three Q2 months read Rs 7,840, Rs 4,080 and Rs 1,990, a fall two
months running, and 118 members have a September row that could be compared at all.
"""),
        code(r'''
kit.check("one row per member per month with an order",
          len(monthly) == len({(r["customer_id"], r["month"]) for r in monthly}), f"{len(monthly)} rows")
kit.check("C-0010 has five months and no May row", len(c0010) == 5 and "2026-05-01" not in by_month)
kit.check("C-0010 fell from Rs 7,840 to Rs 4,080 to Rs 1,990",
          [by_month[m] for m in MONTHS[3:]] == [7840, 4080, 1990])
kit.check("118 members have a September order", active[-1]["members"] == 118, str(active[-1]["members"]))
'''),
        # ---------------------------------------------------------- level 2: trap LAG without partition
        md(r"""
## 2. The trap: LAG without PARTITION BY compares a member with someone else

**The plausible wrong answer.** `lag(spend)` reads the previous row, so a hurried analyst sorts the
table by member and month and writes `lag(spend, 1) OVER (ORDER BY customer_id, month)` and
`lag(spend, 2)` beside it, then flags September rows where each month is below the one before.

**Predict before you run.** How many members does this flag? a) 16; b) 20; c) 9; d) 118.
"""),
        code(r'''
hurried = sql(f"""
    WITH monthly AS ({MONTHLY}),
    lagged AS (
        SELECT customer_id, month, spend,
               lag(spend, 1)       OVER (ORDER BY customer_id, month) AS spend_before,
               lag(spend, 2)       OVER (ORDER BY customer_id, month) AS spend_two_before,
               lag(customer_id, 1) OVER (ORDER BY customer_id, month) AS whose_row_before,
               lag(customer_id, 2) OVER (ORDER BY customer_id, month) AS whose_row_two_before
        FROM   monthly
    )
    SELECT (SELECT count(*) FROM lagged
            WHERE month = DATE '2026-09-01'
              AND spend < spend_before AND spend_before < spend_two_before) AS flagged,
           (SELECT count(*) FROM lagged
            WHERE month = DATE '2026-09-01'
              AND spend < spend_before AND spend_before < spend_two_before
              AND whose_row_two_before <> customer_id) AS compared_with_another_member,
           (SELECT count(*) FROM lagged
            WHERE whose_row_before <> customer_id) AS first_months_given_a_previous_value""")[0]
show([hurried], caption="The hurried flag, and two counts that should be zero")
kit.bars([("flagged", hurried["flagged"]),
          ("against another member", hurried["compared_with_another_member"])], lit=(1,),
         title="LAG without PARTITION BY: 20 flagged, 4 of them against someone else's months")
'''),
        md(r"""
**What happened.** The answer is b, 20.

**Why it is wrong.** Without PARTITION BY the window is the whole table in one line, so the row
before a member's first month is the last month of whoever sorts before them. Four of the 20 had
their "fall" computed partly from another member's account, and Marketing would call a member about
a drop in spend that happened to somebody else. The tell is any member's first month carrying a
previous value; in a result of ten thousand rows the check is a count of rows where the row before
belongs to another customer, and it must be zero.
"""),
        code(r'''
fixed = sql(f"""
    WITH monthly AS ({MONTHLY}),
    lagged AS (
        SELECT customer_id, month, spend,
               lag(spend, 1) OVER (PARTITION BY customer_id ORDER BY month) AS spend_before,
               lag(spend, 2) OVER (PARTITION BY customer_id ORDER BY month) AS spend_two_before,
               lag(month, 1) OVER (PARTITION BY customer_id ORDER BY month) AS month_before,
               lag(month, 2) OVER (PARTITION BY customer_id ORDER BY month) AS month_two_before
        FROM   monthly
    )
    SELECT count(*) AS flagged,
           count(*) FILTER (WHERE month_before <> DATE '2026-08-01'
                               OR month_two_before <> DATE '2026-07-01') AS a_gap_read_as_last_month
    FROM   lagged
    WHERE  month = DATE '2026-09-01'
      AND  spend < spend_before AND spend_before < spend_two_before""")[0]
kit.columns(["flagged", "against another member"],
            [("without PARTITION BY", [hurried["flagged"], hurried["compared_with_another_member"]]),
             ("PARTITION BY customer_id", [fixed["flagged"], 0])],
            title="Partitioned by the member, the flag drops from 20 to 16", width=560)
kit.check("the hurried flag counts 20", hurried["flagged"] == 20)
kit.check("4 of them compared with another member's month", hurried["compared_with_another_member"] == 4)
kit.check("first months carried a previous value without the partition",
          hurried["first_months_given_a_previous_value"] > 0,
          f'{hurried["first_months_given_a_previous_value"]} first months')
kit.check("PARTITION BY customer_id flags 16", fixed["flagged"] == 16)
'''),
        md(r"""
**The fix.** `PARTITION BY customer_id` inside every LAG, so each member is compared only with the
member's own months. The flag goes from 20 members to 16, and none of the 16 borrows another
member's spend.
"""),
        # ---------------------------------------------------------- level 3: trap skipped month
        md(r"""
## 3. The trap: a skipped month read as last month

**The plausible wrong answer.** The partitioned flag says 16, and every comparison is now inside one
member's account. A member rings Marketing: "I was on holiday in August." C-0216 bought Rs 6,440 in
May, nothing in June, Rs 4,300 in July, nothing in August and Rs 2,540 in September, and sits on the
list of 16.

**Predict before you run.** For C-0216's September row, what does `lag(month)` call last month?
a) August; b) July; c) nothing, NULL; d) June.
"""),
        code(r'''
c0216 = sql(f"""
    WITH monthly AS ({MONTHLY})
    SELECT customer_id, month, spend,
           lag(month) OVER (PARTITION BY customer_id ORDER BY month) AS the_row_lag_calls_last_month
    FROM   monthly
    WHERE  customer_id = 'C-0216'
    ORDER  BY month""")
show(c0216, money=("spend",), caption="C-0216: the three rows LAG lines up")
seen = {str(r["month"]): r["spend"] for r in c0216}
kit.line(LABELS, [("C-0216 monthly spend", [seen.get(m) for m in MONTHS], "plain")], fmt=kit.rupees,
         title="C-0216 by calendar month: the line joins across June and August, which is what LAG does")
'''),
        md(r"""
**What happened.** The answer is b. LAG reads the previous row, and C-0216 has no August row, so the
row before September is July, and the row before July is May. LAG saw May Rs 6,440, July Rs 4,300 and
September Rs 2,540, three falling readings, and called it two months running.

**Why it is wrong.** The member on holiday is right: two of the "months" in the run are gaps, and a
gap became a fall. Marketing would spend a retention call on a member whose August is simply
missing. The check carries `lag(month)` beside `lag(spend)` and counts the rows where the previous
row is not the previous calendar month.
"""),
        code(r'''
holds = sql(f"""
    WITH monthly AS ({MONTHLY}),
    lagged AS (
        SELECT customer_id, month, spend,
               lag(spend, 1) OVER (PARTITION BY customer_id ORDER BY month) AS spend_before,
               lag(spend, 2) OVER (PARTITION BY customer_id ORDER BY month) AS spend_two_before,
               lag(month, 1) OVER (PARTITION BY customer_id ORDER BY month) AS month_before,
               lag(month, 2) OVER (PARTITION BY customer_id ORDER BY month) AS month_two_before
        FROM   monthly
    )
    SELECT customer_id
    FROM   lagged
    WHERE  month = DATE '2026-09-01'
      AND  month_before     = month - INTERVAL '1 month'
      AND  month_two_before = month - INTERVAL '2 months'
      AND  spend < spend_before AND spend_before < spend_two_before""")
held = {r["customer_id"] for r in holds}
kit.bars([("LAG without PARTITION BY", 20), ("PARTITION BY customer_id", fixed["flagged"]),
          ("August and July required", len(held))], lit=(2,),
         title="The flag, fix by fix")
kit.check("7 of the 16 read a gap as last month", fixed["a_gap_read_as_last_month"] == 7)
kit.check("requiring August and July leaves 9", len(held) == 9, f"{len(held)} members")
kit.check("C-0216, the member on holiday, is not flagged", "C-0216" not in held)
kit.check("C-0010, a plain fall, stays flagged", "C-0010" in held)
'''),
        md(r'''
**The fix.** Require the two previous rows to be August and July, so a month with no order is no
reading and breaks the run. The flag goes from 16 members to 9, and the 7 who dropped out each had a
gap where LAG had found a fall.

**Your turn.** The count is 9; the names are for you to read. Type these lines into the empty cell
below, run them, and say which segments the flagged members sit in:

```python
flagged = sql(f"""
    WITH monthly AS ({MONTHLY}),
    lagged AS (
        SELECT customer_id, month, spend,
               lag(spend, 1) OVER (PARTITION BY customer_id ORDER BY month) AS spend_before,
               lag(spend, 2) OVER (PARTITION BY customer_id ORDER BY month) AS spend_two_before,
               lag(month, 1) OVER (PARTITION BY customer_id ORDER BY month) AS month_before,
               lag(month, 2) OVER (PARTITION BY customer_id ORDER BY month) AS month_two_before
        FROM monthly)
    SELECT c.segment, l.customer_id, l.spend_two_before AS july, l.spend_before AS august, l.spend AS september
    FROM   lagged l JOIN customers c USING (customer_id)
    WHERE  l.month = DATE '2026-09-01'
      AND  l.month_before = l.month - INTERVAL '1 month'
      AND  l.month_two_before = l.month - INTERVAL '2 months'
      AND  l.spend < l.spend_before AND l.spend_before < l.spend_two_before
    ORDER  BY c.segment, l.customer_id""")
show(flagged, money=("july", "august", "september"))
```
'''),
        empty(),
        # ---------------------------------------------------------- level 4: running total
        md(r"""
## 4. A running total needs an unambiguous order and a start that covers the quarter

Meera wants revenue accumulating against the plan line. A running total is `sum(amount) OVER (ORDER
BY ...)`, and its ORDER BY decides what each row's step is. The busiest day of the quarter, 22 July,
carries twelve orders.

**Predict before you run.** With `ORDER BY order_date` alone, what running total does the first of
22 July's twelve orders show? a) the previous day's close plus its own amount; b) the day's closing
figure, the same on all twelve rows; c) NULL, because the order is ambiguous; d) a different figure
on every run.
"""),
        code(r'''
day = sql("""
    WITH running AS (
        SELECT order_date, order_id, amount,
               sum(amount) OVER (ORDER BY order_date)           AS by_date_only,
               sum(amount) OVER (ORDER BY order_date, order_id) AS by_date_then_order
        FROM   orders
        WHERE  quarter = 'Q2'
    )
    SELECT * FROM running WHERE order_date = DATE '2026-07-22' ORDER BY order_id""")
show(day, money=("amount", "by_date_only", "by_date_then_order"), caption="22 July, twelve orders")
kit.line([r["order_id"][-3:] for r in day],
         [("ORDER BY order_date", [r["by_date_only"] for r in day], "bad"),
          ("ORDER BY order_date, order_id", [r["by_date_then_order"] for r in day], "good")],
         fmt=crore, lo=34000000, title="22 July: same-date rows are peers unless order_id breaks the tie")
'''),
        md(r"""
**What happened.** The answer is b. With a date alone, the twelve orders of 22 July are peers, and
Postgres gives every peer the running total at the end of the peer group, Rs 3,76,90,290, the day's
closing figure. With `order_id` as a tiebreaker each row is one step, from Rs 3,45,16,000 after the
first order of the day to Rs 3,76,90,290 after the last, and the same steps on every run.
"""),
        code(r'''
kit.check("22 July carries twelve Q2 orders", len(day) == 12)
kit.check("by date alone, all twelve show one figure", len({r["by_date_only"] for r in day}) == 1)
kit.check("with order_id, twelve distinct steps", len({r["by_date_then_order"] for r in day}) == 12)
kit.check("the steps run from Rs 3,45,16,000 to Rs 3,76,90,290",
          day[0]["by_date_then_order"] == 34516000 and day[-1]["by_date_then_order"] == 37690290)
'''),
        md(r"""
Now against the plan. `plan_line` has thirteen weeks starting Monday 6 July, Rs 75,69,230 each. Both
sides accumulate, and the actual is read at each plan week's last day, `week_start + 6`, so orders
placed before the plan's first week still count.

**Predict before you run.** At mid-quarter, the end of the seventh plan week, where did Q2 stand?
a) behind plan; b) on plan within a lakh; c) ahead by about Rs 1.58 crore; d) at nine times the plan.
"""),
        code(r'''
plan = sql("""
    WITH daily AS (
        SELECT order_date, sum(amount) AS booked FROM orders WHERE quarter = 'Q2' GROUP BY order_date
    ),
    to_date AS (
        SELECT order_date, sum(booked) OVER (ORDER BY order_date) AS booked_to_date FROM daily
    ),
    plan AS (
        SELECT week_start, week_start + 6 AS week_end, plan_revenue,
               sum(plan_revenue) OVER (ORDER BY week_start) AS plan_to_date
        FROM   plan_line
    )
    SELECT p.week_start, p.plan_revenue, p.plan_to_date,
           (SELECT max(t.booked_to_date) FROM to_date t WHERE t.order_date <= p.week_end) AS booked_to_date
    FROM   plan p
    ORDER  BY p.week_start""")
for r in plan:
    r["ahead_of_plan"] = r["booked_to_date"] - r["plan_to_date"]
weeks = [r["week_start"].strftime("%d %b").lstrip("0") for r in plan]
kit.line(weeks, [("plan to date", [r["plan_to_date"] for r in plan], "plan"),
                 ("booked to date", [r["booked_to_date"] for r in plan], "good")],
         fmt=crore, title="Q2 booked to date against plan to date, read at each plan week's last day")
show([{k: r[k] for k in ("week_start", "plan_to_date", "booked_to_date", "ahead_of_plan")} for r in plan],
     money=("plan_to_date", "booked_to_date", "ahead_of_plan"), caption="The thirteen plan weeks")
'''),
        code(r'''
weekly = [plan[0]["booked_to_date"]] + [plan[i]["booked_to_date"] - plan[i - 1]["booked_to_date"]
                                        for i in range(1, len(plan))]
kit.bars([("1 Jul to 12 Jul" if i == 0 else f"week of {w}", v) for i, (w, v) in enumerate(zip(weeks, weekly))],
         fmt=kit.rupees,
         lit=[i for i, v in enumerate(weekly) if v < plan[i]["plan_revenue"]], width=820,
         title="Booked in each plan week; dark bars fell below the weekly plan of Rs 75,69,230")
'''),
        md(r"""
**What happened.** The answer is c. At the end of the seventh plan week, the week of 17 August, Q2
had booked Rs 6,87,36,590 against a plan to date of Rs 5,29,84,610, ahead by Rs 1,57,51,980. Almost
all of that lead came from the week of 13 July, which booked Rs 2.66 crore on its own. From the week
of 10 August, six of the seven full weeks booked below the weekly plan, and the lead shrank from a
peak of Rs 2,16,69,660 to Rs 10 at the close: Rs 9,84,00,000 against Rs 9,83,99,990. On track by the
total, off track by the run rate. Option d is what a dashboard shows when it sets the running actual
beside one week's plan instead of the plan to date.
"""),
        code(r'''
ahead = [r["ahead_of_plan"] for r in plan]
kit.check("thirteen plan weeks", len(plan) == 13)
kit.check("booked to date closes on Monday's Q2 total", plan[-1]["booked_to_date"] == 98400000,
          kit.rupees(plan[-1]["booked_to_date"]))
kit.check("the plan closes at Rs 9,83,99,990", plan[-1]["plan_to_date"] == 98399990)
kit.check("ahead by Rs 1,57,51,980 at mid-quarter", ahead[6] == 15751980, kit.rupees(ahead[6]))
kit.check("the lead peaked at Rs 2,16,69,660", max(ahead) == 21669660)
kit.check("six of the seven full weeks from 10 August booked below plan",
          sum(1 for i in range(5, 12) if weekly[i] < plan[i]["plan_revenue"]) == 6)
'''),
        # ---------------------------------------------------------- SUM
        md(r"""
## What this round established

> **Kavya's review.** "LAG reads the previous row, so partition by the member and check the previous
> row is last month. A running total is only as true as its order and its start: check it closes on
> the quarter's total before anybody reads the chart."
"""),
        code(r'''
kit.vflow(["LAG without PARTITION BY\n20 flagged, 4 against another member",
           "PARTITION BY customer_id\n16 flagged, 7 across a gap",
           "previous rows must be August and July\n9 flagged",
           "running total, date then order_id\none step per order",
           "read at each plan week's last day\ncloses on Rs 9,84,00,000"],
          kinds=["bad", "bad", "good", "known", "good"],
          title="Round 3: the flag, fix by fix, then the plan line")
kit.table(["Question", "Answer", "What it means for Marketing and Meera"],
          [("Flagged by the hurried LAG?", "20", "Four calls about someone else's fall."),
           ("Flagged with the member partition?", "16", "Seven of them read a holiday as a fall."),
           ("Flagged with consecutive months?", "9", "The list Marketing can defend."),
           ("Ahead of plan at mid-quarter?", kit.rupees(ahead[6]), "Almost all of it from one July week."),
           ("Where did Q2 close?", kit.rupees(plan[-1]["booked_to_date"]), "Rs 10 ahead of the plan line.")],
          caption="What Round 3 established")
'''),
        md(r"""
### In the interview

**[F] How would you find customers whose spend fell two months in a row?** "I build one row per
customer per month, then use `lag(spend, 1)` and `lag(spend, 2)` over `PARTITION BY customer_id ORDER
BY month`, and keep the latest month where spend is below the month before and that is below the
month before it. I also carry `lag(month)` beside `lag(spend)` and require the previous rows to be the
previous two calendar months, because LAG reads the previous row, and a customer with no order in
August has July as the previous row. Without that condition a gap becomes a fall."

**[F] LAG returned a value for a customer's very first month. What went wrong, and how do you check
for it in a result of ten thousand rows?** "The window is missing PARTITION BY customer_id, so the
previous row belongs to whoever sorts before that customer. I check it with a count, never by eye: I
carry `lag(customer_id)` beside the value and count rows where it differs from the current customer.
With the partition in place that count is zero, and so is the count of first months with a non-null
previous value."

**[D] A member says he was on holiday in August and should not be flagged. How does your definition
treat a month with no orders, and why not fill it with zero?** "My definition treats a month with no
order as no reading, so it breaks the run and the member is not flagged: a fall needs three readings a
calendar month apart. Filling the gap with zero would turn every holiday into a fall to zero and flag
anyone who skipped September, which is a different question, lapsed members, and deserves its own
list with its own name."

**[F] What makes a running total deterministic, and how would you notice one that was not?** "An
ORDER BY in the window that gives every row a unique place, which usually means adding a key like
order_id after the date. With the date alone, rows on the same date are peers and all show the day's
closing figure. I notice it when several rows share one running value, or when a row-level running
total differs between two runs, and I check that the last value equals the plain sum."

**[F] A dashboard says revenue to date is nine times the plan by week seven. What is the likely
mistake?** "It is comparing a running total with one week's plan. Booked to date at week seven was
Rs 6,87,36,590 and a single week's plan is Rs 75,69,230, which is about nine times. Both sides have to
accumulate: the plan to date at week seven was Rs 5,29,84,610, so the business was ahead by
Rs 1,57,51,980, a long way from nine times."
"""),
        md(r"""
### Depth: why zero-filling a gap is no fix

The tempting repair for the holiday member is to give every member a row for every month, with 0 where
there was no order, and let LAG run over a complete calendar. It makes the gaps disappear from view
and changes the question. A member who bought in July and August and was away in September now reads
as a fall to zero, and so does every member who simply stopped at the end of August. The invented
member below, labelled invented, spent Rs 5,000 in July and Rs 3,000 in August and placed no order in
September; zero-filled, the member is flagged. On Kalpa's months the zero-filled flag counts 26
members, and every one of the 17 it adds to the nine placed no September order at all.
"""),
        code(r'''
kit.line(["Jul", "Aug", "Sep"],
         [("invented member, zero-filled", [5000, 3000, 0], "bad"),
          ("invented member, as recorded", [5000, 3000, None], "plain")],
         fmt=kit.rupees, title="Invented: zero-filling turns a month away into a fall to nothing")
zero = sql(f"""
    WITH months AS (
        SELECT generate_series(DATE '2026-04-01', DATE '2026-09-01', INTERVAL '1 month')::date AS month
    ),
    members AS (SELECT DISTINCT customer_id FROM orders),
    monthly AS ({MONTHLY}),
    filled AS (
        SELECT m.customer_id, mo.month, coalesce(x.spend, 0) AS spend
        FROM   members m CROSS JOIN months mo
        LEFT   JOIN monthly x ON x.customer_id = m.customer_id AND x.month = mo.month
    ),
    lagged AS (
        SELECT customer_id, month, spend,
               lag(spend, 1) OVER (PARTITION BY customer_id ORDER BY month) AS spend_before,
               lag(spend, 2) OVER (PARTITION BY customer_id ORDER BY month) AS spend_two_before
        FROM   filled
    )
    SELECT count(*) AS flagged, count(*) FILTER (WHERE spend = 0) AS no_september_order
    FROM   lagged
    WHERE  month = DATE '2026-09-01' AND spend < spend_before AND spend_before < spend_two_before""")[0]
show([zero], caption="The zero-filled flag on Kalpa's months")
kit.check("zero-filling flags more members than the consecutive-month rule", zero["flagged"] > len(held),
          f'{zero["flagged"]} against {len(held)}')
kit.check("every member zero-filling adds bought nothing in September",
          zero["no_september_order"] == zero["flagged"] - len(held) == 17)
'''),
        code(r'''
kit.check_summary()
print("Next: the escalated case puts the list, the flag and the plan line into one file for Marketing.")
'''),
    ]
    build(NB / "C2_W02_D03_03_falling_STUDENT.ipynb", cells)
    return cells


# ================================================================== the escalated case
TIE_OPTIONS = r'''
# TODO 1. Which window ranks members the way the head of Retail-Plus asked?
TIE_RULES = {
    "a": "row_number() OVER (PARTITION BY segment ORDER BY q2_revenue DESC, customer_id)",
    "b": "dense_rank() OVER (PARTITION BY segment ORDER BY q2_revenue DESC)",
    "c": "rank() OVER (PARTITION BY segment ORDER BY q2_revenue DESC)",
    "d": "rank() OVER (ORDER BY q2_revenue DESC)",
}
'''

FLAG_OPTIONS = r'''
# TODO 2. For a September row, what must the row two back be for the run to count?
TWO_BACK = {
    "a": "DATE '2026-07-01'",
    "b": "DATE '2026-06-01'",
    "c": "coalesce(month_two_before, month)",
    "d": "DATE '2026-08-01'",
}
'''

READ_OPTIONS = r'''
# TODO 3. On which day is the booked-to-date read for each plan week?
READ_ON = {
    "a": "p.week_start",
    "b": "p.week_start + 7",
    "c": "date_trunc('month', p.week_start)::date",
    "d": "p.week_start + 6",
}
'''

CLOSE_OPTIONS = r'''
# TODO 4. What must the last booked-to-date equal before anyone reads the chart?
MUST_EQUAL = {
    "a": "plan_to_date_at_the_close",
    "b": "q2_booked_total",
    "c": "hurried_close",
    "d": "thirteen_weeks_of_the_weekly_plan",
}
'''

SENTENCE_OPTIONS = r'''
# TODO 5. Which line about the plan goes to Meera?
PLAN_LINES = {
    "a": ("Q2 closed Rs 15,39,810 short of plan, Rs 9,68,60,180 against Rs 9,83,99,990, because the lead of "
          "Rs 1.58 crore that Q2 held at mid-quarter did not survive the quieter weeks of August and September."),
    "b": ("By the end of the seventh plan week Q2 had booked Rs 6,87,36,590 against a weekly plan of "
          "Rs 75,69,230, about nine times the plan, so the quarter was never in doubt and closed at Rs 9,84,00,000."),
    "c": ("Q2 closed on plan, Rs 9,84,00,000 against Rs 9,83,99,990, and the Rs 1.58 crore lead at mid-quarter "
          "came from one week in July, so the weekly run rate has been below plan since 10 August."),
    "d": ("Q2 closed on plan, Rs 9,84,00,000 against Rs 9,83,99,990, and it stayed ahead of the plan line in "
          "every one of the thirteen plan weeks, so the weekly run rate needs no attention from Marketing."),
}
'''

WHY = {
    1: "a) ROW_NUMBER breaks a tie at the line by customer_id, a coin toss the head of Retail-Plus ruled out. "
       "b) DENSE_RANK closes the gaps after every tie, so a segment ships more than fifty with no tie at the "
       "line, 52 in Retail-Core. d) RANK without PARTITION BY ranks the whole table, the Round 1 trap, and "
       "hands Retail-Plus 11 members.",
    2: "b) June two back means July is missing, the gap Round 3 refused to read as a fall. c) matches "
       "whatever month sits two rows back, so a member with no July order is read as falling from June. d) "
       "August is already the row one back, so no September row has August two back and nobody is flagged.",
    3: "a) week_start reads the actual on the Monday the week opens, before the week's orders are in. b) "
       "week_start + 7 is the next week's Monday, so every reading takes one day of the next week. c) the "
       "month's first day reads most weeks against a date weeks earlier.",
    4: "a) the plan to date is the target, and a total that equals it only says the chart was built from "
       "the plan. c) the hurried close is the number under test. d) thirteen weekly plans is the plan "
       "again, Rs 9,83,99,990.",
    5: "a) quotes the hurried plan-first join's close, Rs 15,39,820 short of the true total. b) sets a "
       "running total beside one week's plan. d) is contradicted by the first plan week, which closed "
       "Rs 24,69,050 behind, and it hides a run rate below plan in six of the seven full weeks from 10 August.",
}
ANSWERS = {1: '"c"', 2: '"a"', 3: '"d"', 4: '"b"', 5: '"c"'}


def case_cells(solved):
    """The escalated case, as the TODO twin (solved=False) or the executed solution (solved=True)."""
    def pick(n):
        return ANSWERS[n] if solved else f"__TODO{n}__"

    def why(n):
        return [md(f"**Why the other letters fail.** {WHY[n]}")] if solved else []

    title = "# The escalated case: one file for Marketing" + (", solved" if solved else "")
    intro = (r"""
This is the solved notebook, released after the case: every placeholder is filled with the letter
that holds, and a line under each part says why the other three letters fail. The answer string is
**c a d b c**.
""" if solved else r"""
Each part has one placeholder, `__TODO1__` to `__TODO5__`, and each answer is a letter from the
options written above it, typed in quotes, for example `"a"`. Run All stops at `__TODO1__` with a
NameError naming the placeholder; that is the notebook asking for your first letter, and it is no
bug. Each part ends with checks that tell you whether your letter holds. Post the five letters in
order when you are done.
""")
    cells = [
        md(title + r"""

**Week 2, Wednesday. The escalated case, 45 minutes, unguided.** The five parts match
`sql/C2_W02_D03_04_marketing_case_STUDENT.sql` and the brief in
`exercises/unguided/C2_W02_D03_marketing_case_STUDENT.md`.

> **Marketing asks.** "We act on this list on Monday. One file: the top fifty members by Q2 revenue
> in every segment, ranked the way the head of Retail-Plus asked, a column that says whether each
> one's spend fell in August and again in September, and the running total against the plan so
> Meera can see where the quarter stood at mid-quarter and where it closed. Tell us the tie rule and
> the number of members it ships."

> **Kavya's review of the case.** "Every number you send has a check under it. The list says its tie
> rule and its count, the flag says what a month without an order means, and the running total
> closes on the quarter's total before anybody reads the chart."

The morning's three rounds established the pieces: a window partitioned by segment keeps every
member with a position (Round 1), RANK is the tie rule and the report says how many it ships
(Round 2), and a fall needs the previous two rows to be the previous two calendar months, while a
running total needs an unambiguous order and a start that covers the quarter (Round 3).
""" + intro),
        md(SETUP_MD),
        code(SETUP_CELL),
        map_cell(3),
        # ---------------------------------------------------------- Part 1
        md(r"""
## Part 1. The protect list: fifty per segment, ties ranked the same

The list is Q2 revenue per member ranked inside each segment and filtered at position fifty in a
CTE. The only decision is the window, and it is a business decision.
"""),
        code(TIE_OPTIONS + f"""position_sql = TIE_RULES[{pick(1)}]
""" + r'''
protect = sql(f"""
    WITH q2 AS ({Q2_PER_MEMBER}),
    ranked AS (SELECT segment, customer_id, q2_revenue, {position_sql} AS position FROM q2)
    SELECT segment, customer_id, q2_revenue, position FROM ranked
    WHERE  position <= 50
    ORDER  BY segment, position, customer_id""")
buyers = {r["segment"]: r["n"] for r in sql(f"WITH q2 AS ({Q2_PER_MEMBER}) SELECT segment, count(*) AS n FROM q2 GROUP BY segment")}
counts = {s: sum(1 for r in protect if r["segment"] == s) for s in SEGMENTS}
kit.columns(SEGMENTS, [("Q2 buyers", [buyers[s] for s in SEGMENTS]),
                       ("on the protect list", [counts.get(s, 0) for s in SEGMENTS])],
            title="The protect list by segment")


def at_last_position(segment):
    """How many listed members of a segment share its last position."""
    last = max(r["position"] for r in protect if r["segment"] == segment)
    return sum(1 for r in protect if r["segment"] == segment and r["position"] == last)


show([{"segment": s, "q2_buyers": buyers[s], "on_the_list": counts[s],
       "last_position": max((r["position"] for r in protect if r["segment"] == s), default=0),
       "members_at_the_last_position": at_last_position(s) if counts[s] else 0} for s in SEGMENTS],
     caption="The protect list by segment, with the position each list stops at")
'''),
        code(r'''
tied_apart = sum(1 for a in protect for b in protect
                 if a["segment"] == b["segment"] and a["q2_revenue"] == b["q2_revenue"]
                 and a["position"] != b["position"])
kit.check("every segment is ranked separately", set(counts) == set(SEGMENTS) and all(counts[s] > 0 for s in SEGMENTS))
kit.check("Business and Student ship every Q2 buyer", counts["Business"] == 35 and counts["Student"] == 20)
kit.check("Retail-Core ships exactly 50", counts["Retail-Core"] == 50)
kit.check("members who spent the same share a position", tied_apart == 0, f"{tied_apart} tied pairs split")
kit.check("no segment ships fewer than fifty or all its buyers",
          all(counts[s] >= min(50, buyers[s]) for s in SEGMENTS))
'''),
        *why(1),
        # ---------------------------------------------------------- Part 2
        md(r"""
## Part 2. The falling-spend flag on the list

The flag is LAG over each member's months, partitioned by the member. A month with no order is no
reading, so the run counts only when the row one back is August and the row two back is the month
you choose below.
"""),
        code(FLAG_OPTIONS + f"""two_back_sql = TWO_BACK[{pick(2)}]
""" + r'''
falling = sql(f"""
    WITH monthly AS (
        SELECT customer_id, date_trunc('month', order_date)::date AS month, sum(amount) AS spend
        FROM   orders
        GROUP  BY customer_id, date_trunc('month', order_date)
    ),
    lagged AS (
        SELECT customer_id, month, spend,
               lag(spend, 1) OVER (PARTITION BY customer_id ORDER BY month) AS spend_before,
               lag(spend, 2) OVER (PARTITION BY customer_id ORDER BY month) AS spend_two_before,
               lag(month, 1) OVER (PARTITION BY customer_id ORDER BY month) AS month_before,
               lag(month, 2) OVER (PARTITION BY customer_id ORDER BY month) AS month_two_before
        FROM   monthly
    )
    SELECT customer_id, spend_two_before AS july, spend_before AS august, spend AS september
    FROM   lagged
    WHERE  month = DATE '2026-09-01'
      AND  month_before = DATE '2026-08-01'
      AND  month_two_before = {two_back_sql}
      AND  spend < spend_before AND spend_before < spend_two_before""")
fell = {r["customer_id"]: r for r in falling}
for r in protect:
    r["falling"] = r["customer_id"] in fell
on_list_flagged = [r for r in protect if r["falling"]]
kit.bars([(s, sum(1 for r in on_list_flagged if r["segment"] == s)) for s in SEGMENTS],
         title="Members on the protect list whose spend fell in August and again in September")
show([{"segment": r["segment"], "position": r["position"], "customer_id": r["customer_id"],
       "july": fell[r["customer_id"]]["july"], "august": fell[r["customer_id"]]["august"],
       "september": fell[r["customer_id"]]["september"]} for r in on_list_flagged],
     money=("july", "august", "september"), caption="The flag, read on the protect list")
'''),
        code(r'''
kit.check("every flagged member fell two calendar months running",
          all(r["july"] > r["august"] > r["september"] for r in falling))
kit.check("C-0010, Retail-Core's plain fall, is flagged", "C-0010" in fell)
kit.check("C-0216, the member on holiday in August, is not flagged", "C-0216" not in fell)
kit.check("the flag counts 9 members, and all 9 are on the list",
          len(falling) == 9 and len(on_list_flagged) == 9, f"{len(falling)} flagged, {len(on_list_flagged)} on the list")
'''),
        *why(2),
        # ---------------------------------------------------------- Part 3
        md(r"""
## Part 3. Revenue against plan, both sides accumulating

Both sides accumulate: the booked total runs by day, the plan runs by week, and the actual is read
once per plan week. Orders placed before the plan's first week must still count.
"""),
        code(READ_OPTIONS + f"""read_sql = READ_ON[{pick(3)}]
""" + r'''
plan = sql(f"""
    WITH daily AS (
        SELECT order_date, sum(amount) AS booked FROM orders WHERE quarter = 'Q2' GROUP BY order_date
    ),
    to_date AS (
        SELECT order_date, sum(booked) OVER (ORDER BY order_date) AS booked_to_date FROM daily
    ),
    p AS (
        SELECT week_start, plan_revenue, sum(plan_revenue) OVER (ORDER BY week_start) AS plan_to_date
        FROM   plan_line
    )
    SELECT p.week_start, p.plan_to_date,
           (SELECT max(t.booked_to_date) FROM to_date t WHERE t.order_date <= {read_sql}) AS booked_to_date
    FROM   p
    ORDER  BY p.week_start""")
weeks = [r["week_start"].strftime("%d %b").lstrip("0") for r in plan]
kit.line(weeks, [("plan to date", [r["plan_to_date"] for r in plan], "plan"),
                 ("booked to date", [r["booked_to_date"] for r in plan], "good")],
         fmt=crore, title="Q2 booked to date against plan to date, by plan week")
'''),
        code(r'''
ahead = [r["booked_to_date"] - r["plan_to_date"] for r in plan]
kit.check("thirteen plan weeks, each with a reading", len(plan) == 13 and all(r["booked_to_date"] for r in plan))
kit.check("the first week's reading includes the orders of 1 to 5 July",
          plan[0]["booked_to_date"] == 5100180, kit.rupees(plan[0]["booked_to_date"]))
kit.check("ahead by Rs 1,57,51,980 at the end of the seventh plan week", ahead[6] == 15751980,
          kit.rupees(ahead[6]))
'''),
        *why(3),
        # ---------------------------------------------------------- Part 4
        md(r"""
## Part 4. The check: does the close equal Monday's Q2 total?

**The plausible wrong answer.** A hurried version starts from the plan and joins weekly revenue onto
it on `date_trunc('week', order_date)`. It looks complete, thirteen weeks and thirteen numbers, and
it closes short of the quarter. The check decides which number the close must equal.
"""),
        code(r'''
hurried = sql("""
    WITH weekly AS (
        SELECT date_trunc('week', order_date)::date AS week_start, sum(amount) AS booked
        FROM   orders WHERE quarter = 'Q2' GROUP BY 1
    )
    SELECT p.week_start,
           sum(w.booked)       OVER (ORDER BY p.week_start) AS booked_to_date,
           sum(p.plan_revenue) OVER (ORDER BY p.week_start) AS plan_to_date
    FROM   plan_line p
    LEFT   JOIN weekly w ON w.week_start = p.week_start
    ORDER  BY p.week_start""")
show([{"week_start": h["week_start"], "hurried_to_date": h["booked_to_date"],
       "read_at_week_end": t["booked_to_date"], "short_by": t["booked_to_date"] - h["booked_to_date"]}
      for h, t in zip(hurried, plan)],
     money=("hurried_to_date", "read_at_week_end", "short_by"),
     caption="The plan-first join beside the reading at each week's last day")
before = sql("""
    SELECT count(*) AS orders, sum(amount) AS booked FROM orders
    WHERE  quarter = 'Q2' AND order_date < (SELECT min(week_start) FROM plan_line)""")[0]
candidates = {
    "plan_to_date_at_the_close": plan[-1]["plan_to_date"],
    "q2_booked_total": sql("SELECT sum(amount) AS t FROM orders WHERE quarter = 'Q2'")[0]["t"],
    "hurried_close": hurried[-1]["booked_to_date"],
    "thirteen_weeks_of_the_weekly_plan": 13 * sql("SELECT min(plan_revenue) AS w FROM plan_line")[0]["w"],
}
''' + CLOSE_OPTIONS + f"""target = candidates[MUST_EQUAL[{pick(4)}]]
""" + r'''
hurried_close, true_close = hurried[-1]["booked_to_date"], plan[-1]["booked_to_date"]
kit.bridge(("hurried close", hurried_close),
           [(f'{before["orders"]} orders of 1 to 5 July', before["booked"])],
           end_label="true close", lo=95000000, fmt=lambda v: f"Rs {v / 1e7:.3f} cr",
           title="The plan-first join drops the week of 29 June; the axis starts at Rs 9.50 crore")
'''),
        code(r'''
kit.check("the close equals the number it must equal", true_close == target, kit.rupees(target))
kit.check("the close is Monday's Q2 total, Rs 9,84,00,000", target == 98400000)
kit.check("the hurried join closes Rs 15,39,820 short", target - hurried_close == 1539820,
          kit.rupees(target - hurried_close))
kit.check("the hurried join runs short by the same amount every week",
          len({t["booked_to_date"] - h["booked_to_date"] for h, t in zip(hurried, plan)}) == 1)
kit.check("the missing rupees are the 25 orders before the plan's first week",
          before["orders"] == 25 and hurried_close + before["booked"] == true_close)
'''),
        *why(4),
        # ---------------------------------------------------------- Part 5
        md(r"""
## Part 5. The sentence Marketing and Meera read

Three sentences: the tie rule and how many members it ships per segment, how many listed members
carry the flag and what the flag means for a member who says he was on holiday, and where Q2 stood
against plan at mid-quarter and at the close. The first two are built from the parts above; choose
the third.
"""),
        code(SENTENCE_OPTIONS + f"""plan_line_text = PLAN_LINES[{pick(5)}]
""" + r'''
WORDS = ["no", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
         "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
everyone = [s for s in SEGMENTS if counts[s] == buyers[s]]
ranked_to_fifty = [s for s in SEGMENTS if s not in everyone]
over = [s for s in ranked_to_fifty if counts[s] > 50]
tie_line = ("We ranked with RANK inside each segment, so tied members share a place and nobody at the line "
            "is dropped by a coin toss: the list carries "
            + " and ".join(f"{counts[s]} {s}" for s in everyone) + " members, which is every Q2 buyer there, "
            + " and ".join(f"{counts[s]} {s}" for s in ranked_to_fifty)
            + "".join(f", because {WORDS[at_last_position(s)]} {s} members tie at fiftieth" for s in over) + ".")
flag_line = (f"{WORDS[len(on_list_flagged)].capitalize()} listed members spent less in August than July and "
             "less again in September; a member with no August order is not flagged, because a month "
             "without an order is no reading.")
message = " ".join([tie_line, flag_line, plan_line_text])
per_segment = ", ".join(f"{counts[s]} {s}" for s in SEGMENTS)
kit.show_messages([("To Marketing and Meera", message)])
kit.stats([(str(sum(counts.values())), "members on the list", per_segment),
           (str(len(on_list_flagged)), "flagged", "fell in August and again in September"),
           (kit.rupees(true_close - plan[-1]["plan_to_date"]), "ahead at the close", "against the plan to date")])
'''),
        code(r'''
kit.check("the plan line quotes the true close and the plan to date",
          kit.rupees(true_close) in plan_line_text and kit.rupees(plan[-1]["plan_to_date"]) in plan_line_text)
kit.check("the plan line quotes the mid-quarter lead", f"Rs {ahead[6] / 1e7:.2f} crore" in plan_line_text)
kit.check("the plan line names the week the run rate turned", "10 August" in plan_line_text)
kit.check("the message says why a segment ships more than fifty",
          all(f"{s} members tie at fiftieth" in message for s in over))
kit.check("the message carries the flag count it computed",
          f"{WORDS[len(on_list_flagged)].capitalize()} listed members" in message)
'''),
        *why(5),
        code(r'''
kit.vflow(["Part 1\nRANK inside each segment, count said out loud",
           "Part 2\nLAG partitioned by member, consecutive months only",
           "Part 3\nboth sides accumulate, read at each week's last day",
           "Part 4\nthe close equals Monday's Q2 total",
           "Part 5\nthree sentences for Marketing and Meera"],
          kinds=["known", "known", "known", "good", "lit"],
          title="The escalated case, part by part")
kit.check_summary()
''' + ('print("The letters are c, a, d, b and c. Thursday re-expresses the ranks with pandas groupby.")'
       if solved else 'print("Post your five letters in order. Thursday re-expresses the ranks with pandas groupby.")')),
    ]
    return cells


def the_case():
    build(NB / "C2_W02_D03_hands_on_STUDENT.ipynb", case_cells(False), execute=False)
    build(SOL / "C2_W02_D03_hands_on_solution_STUDENT.ipynb", case_cells(True))


if __name__ == "__main__":
    for fn in (round_one, round_two, round_three, the_case):
        fn()
        print("built", fn.__name__)

# Test inputs and expected outcomes
# --------------------------------
# python3 content/W02/D3/internal/C2_W02_D03_build_notebooks_INTERNAL.py with the warehouse up
#     Prints "built round_one" to "built the_case" and writes five notebooks: three round notebooks
#     and the solution executed with every check passing, and the TODO twin written unexecuted.
# The same command with no warehouse listening
#     Stops in round_one's setup cell: nbclient raises CellExecutionError carrying the kit's message
#     "No warehouse answered at localhost:5432", and nothing after it is rewritten.
# python3 scripts/nb_check.py content/W02/D3/notebooks
#     Reports the twin as a TODO twin with at least three diagram calls and five check calls, and
#     every round notebook with at least eight diagrams and eight passing checks, none failing.
# Running the TODO twin with "c" typed for __TODO1__ and the other placeholders left in place
#     Part 1's checks pass and the run stops at __TODO2__ with NameError: name '__TODO2__' is not defined.
# Running the TODO twin with "a" for __TODO1__ (ROW_NUMBER)
#     "members who spent the same share a position" fails in the segment where a tie sits at the line,
#     and Retail-Core still shows 50.
# Running the TODO twin with "c" typed for __TODO4__ (the hurried close)
#     "the close equals the number it must equal" fails, showing Rs 9,68,60,180.
