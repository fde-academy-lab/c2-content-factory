"""Prove every number Thursday's exercises, lab, take-home, Kahoot and extras rest on.

Run from the repository root, with the warehouse loaded (bash .devcontainer/load_warehouse.sh):
    python3 content/W02/D4/internal/C2_W02_D04_key_proofs_INTERNAL.py

Each block recomputes the numbers one file's items quote, from the warehouse, the day's data files
or the invented records the item states, and asserts the key the solution file gives. A number an
item states and nothing here proves is a number nobody checked. The script prints one line per file
and stops on the first assertion that fails.
"""
import pathlib
import sys
from datetime import date

import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
import c2kit as kit  # noqa: E402

DAY = ROOT / "content" / "W02" / "D4"
DATA = DAY / "data"
ENG = kit.engine()

orders = pd.read_sql("SELECT order_id, customer_id, order_date, quarter, channel, amount FROM orders",
                     ENG, parse_dates=["order_date"])
customers = pd.read_sql("SELECT customer_id, segment, city FROM customers", ENG)
feed = pd.read_csv(DATA / "C2_W02_D04_exposure_STUDENT.csv", parse_dates=["exposed_date"])
rfm = (orders.groupby("customer_id")
             .agg(last_order=("order_date", "max"), frequency=("order_id", "count"), spend=("amount", "sum"))
             .reset_index())
table = customers.merge(rfm, on="customer_id", how="left", validate="one_to_one")
table = table.assign(frequency=table["frequency"].fillna(0).astype("int64"), spend=table["spend"].fillna(0))
first = (feed.sort_values("exposed_date").drop_duplicates("customer_id", keep="first")
             [["customer_id", "exposed_date"]])
AS_OF = orders["order_date"].max()


def done(name):
    print(f"PASS  {name}")


# Chapter 1 set: 1c 2b 3d 4a 5c
half = customers.merge(rfm, on="customer_id", how="left", validate="one_to_one")
assert round(half["frequency"].mean(), 2) == 3.32 and round(1000 / 340, 2) == 2.94      # item 2
flipped = rfm.merge(customers, on="customer_id", how="left", validate="one_to_one")
flipped = flipped.assign(frequency=flipped["frequency"].fillna(0).astype("int64"))
assert (len(flipped), int((flipped["frequency"] == 0).sum())) == (301, 0)                  # item 3
lead_routes = {                                     # item 4: the routes the growth team's lead could run
    "a": kit.sql("""SELECT count(*) AS n FROM customers c
                    WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id)""")[0]["n"],
    "b": kit.sql("""SELECT count(*) AS n FROM (SELECT customer_id, count(*) AS k FROM orders
                    GROUP BY customer_id) t WHERE k = 0""")[0]["n"],
    "c": kit.sql("""SELECT count(*) AS n FROM (SELECT c.customer_id, count(*) AS k FROM customers c
                    LEFT JOIN orders o ON o.customer_id = c.customer_id GROUP BY c.customer_id) t
                    WHERE k = 0""")[0]["n"]}
assert lead_routes == {"a": 39, "b": 0, "c": 0} and int((table["frequency"] == 0).sum()) == 39   # key a
order_ids = kit.sql("SELECT customer_id FROM orders")                                     # d: the loop's input
assert len(order_ids) == 1000 and len(set(customers["customer_id"]) - {r["customer_id"] for r in order_ids}) == 39
by_orders = pd.read_sql("""SELECT customer_id, max(order_date) AS last_order, count(*) AS frequency,
                                  sum(amount) AS spend FROM orders GROUP BY customer_id""", ENG)
from_list = pd.read_sql("""SELECT c.customer_id, max(o.order_date) AS last_order,
                                  count(o.order_id) AS frequency, coalesce(sum(o.amount), 0) AS spend
                           FROM customers c LEFT JOIN orders o ON o.customer_id = c.customer_id
                           GROUP BY c.customer_id""", ENG)
both = table.merge(from_list, on="customer_id", suffixes=("", "_sql"), validate="one_to_one")
assert (len(by_orders), len(from_list), int((from_list["frequency"] == 0).sum())) == (301, 340, 39)  # item 5
assert (both["frequency"] == both["frequency_sql"]).all() and (both["spend"] == both["spend_sql"].astype(float)).all()
assert orders.groupby("quarter").size().to_dict() == {"Q1": 538, "Q2": 462}                # about 500 a quarter
done("chapter 1 set")

# Chapter 2 set: 1c 2b 3d 4d 5a
small = pd.DataFrame({"customer_id": ["C-8101", "C-8102", "C-8103", "C-8104", "C-8105"],
                      "spend": [4000, 6500, 2500, 9000, 3000]})
diwali = pd.DataFrame({"customer_id": ["C-8101", "C-8102", "C-8102", "C-8104"],
                       "exposed_date": pd.to_datetime(["2026-10-20"] * 4)})
slide = small.merge(diwali, on="customer_id", how="left")
assert slide.loc[slide["exposed_date"].notna(), "spend"].sum() == 26000                    # item 1, key c
assert small.loc[small["customer_id"].isin(diwali["customer_id"]), "spend"].sum() == 19500
assert small["spend"].sum() == 25000 and slide["spend"].sum() == 31500
shapes = [len(table.merge(first, on="customer_id", how=h)) for h in ("inner", "left", "outer", "right")]
assert shapes == [130, 340, 340, 130]                                                      # item 2, key b
assert 12000 + 100 == 12100 and 100 * 5100 == 510000                                       # item 3 sizing
assert feed["campaign_id"].unique().tolist() == ["CMP-MONSOON-26"]                         # item 5: one campaign today
monsoon = "(SELECT customer_id FROM campaign_exposure WHERE campaign_id = 'CMP-MONSOON-26')"
in_monsoon = kit.sql(f"SELECT sum(amount) AS s FROM orders WHERE customer_id IN {monsoon}")[0]["s"]
joined = kit.sql("""SELECT sum(o.amount) AS s FROM orders o JOIN campaign_exposure e
                    ON e.customer_id = o.customer_id WHERE e.campaign_id = 'CMP-MONSOON-26'""")[0]["s"]
plain = table.merge(feed[["customer_id", "exposed_date"]], on="customer_id", how="left")
assert float(in_monsoon) == 878980                                                         # key a
assert float(joined) == plain.loc[plain["exposed_date"].notna(), "spend"].sum() > 878980   # b fans out as a plain merge does
after = orders.merge(first, on="customer_id", validate="many_to_one")
assert after.loc[after["order_date"] >= after["exposed_date"], "amount"].sum() != 878980   # d measures another number
done("chapter 2 set")

# Chapter 3 set: 1b 2d 3c 4a 5b
toy = pd.DataFrame({"member": ["M1", "M1", "M1", "M2"], "month": ["Apr", "Apr", "May", "Apr"],
                    "amount": [1000, 3000, 2000, 4000]})
avg = toy.pivot_table(index="member", columns="month", values="amount")
assert avg["Apr"].sum() == 6000 and toy.loc[toy["month"] == "Apr", "amount"].sum() == 8000  # item 1, key b
assert round(8000 / 3) == 2667
assert 310000 + 290000 == 600000 and round((290000 / 310000 - 1) * 100, 1) == -6.5         # item 2
assert 150 * 13 == 1950 and 150 * 12 - 540 == 1260 and 540 * 3 == 1620                     # item 3, the id counted as a cell
plus = orders.merge(customers, on="customer_id").query("segment == 'Retail-Plus'")
plus = plus.assign(month=plus["order_date"].dt.to_period("M").astype(str))
assert (len(plus), plus["customer_id"].nunique()) == (355, 107)
assert plus.pivot_table(index="month", columns="customer_id", values="amount", aggfunc="sum").shape == (6, 107)
assert int((customers["segment"] == "Retail-Plus").sum()) == 120 and 120 - 107 == 13        # item 4, option d
by_month = kit.sql("""SELECT date_trunc('month', o.order_date)::date AS month, sum(o.amount) AS spend
                      FROM orders o JOIN customers c ON c.customer_id = o.customer_id
                      WHERE c.segment = 'Retail-Plus' GROUP BY 1 ORDER BY 1""")          # item 5, Finance's query
assert len(by_month) == 6 and sum(float(r["spend"]) for r in by_month) == plus["amount"].sum() == 999150
done("chapter 3 set")

# Chapter 4 set: 1b 2a 3d 4b 5c
reach = pd.DataFrame({"customer_id": ["A", "B", "C", "D", "E"],
                      "segment": ["Retail-Core", "Retail-Plus", None, "Retail-Plus", None],
                      "bought": [1, 1, 0, 0, 0]})
out = reach.groupby("segment")["bought"].agg(["size", "sum"])
assert (int(out["size"].sum()), int(out["sum"].sum())) == (3, 2)                           # item 1, key b
assert round(0.96 * 1250) == 1200 and round(1200 / 1480 * 100) == 81 and 1480 - 1250 == 230  # item 3
seg_of_orders = kit.sql("""WITH reached AS (SELECT DISTINCT customer_id FROM campaign_exposure),
     buyers AS (SELECT o.customer_id, min(c.segment) AS segment, count(*) AS orders FROM orders o
                JOIN customers c ON c.customer_id = o.customer_id GROUP BY o.customer_id)
SELECT b.segment, count(*) AS reached, count(b.orders) AS bought
FROM reached r LEFT JOIN buyers b ON b.customer_id = r.customer_id GROUP BY b.segment""")
seg_of_list = kit.sql("""WITH reached AS (SELECT DISTINCT customer_id FROM campaign_exposure),
     buyers AS (SELECT customer_id, count(*) AS orders FROM orders GROUP BY customer_id)
SELECT c.segment, count(*) AS reached, count(b.orders) AS bought
FROM reached r JOIN customers c ON c.customer_id = r.customer_id
LEFT JOIN buyers b ON b.customer_id = r.customer_id GROUP BY c.segment""")
assert {(r["segment"], r["reached"], r["bought"]) for r in seg_of_orders} == {
    ("Retail-Core", 56, 56), ("Retail-Plus", 51, 51), (None, 23, 0)}                       # item 4, option c
assert {(r["segment"], r["reached"], r["bought"]) for r in seg_of_list} == {
    ("Retail-Core", 70, 56), ("Retail-Plus", 60, 51)}                                      # item 4, key b
reached_ids, buyer_ids = set(feed["customer_id"]), set(orders["customer_id"])
assert (len(reached_ids), len(reached_ids & buyer_ids), len(reached_ids - buyer_ids)) == (130, 107, 23)
assert (round(56 / 70 * 100), round(51 / 60 * 100)) == (80, 85)
assert 900 - 40 == 860                                                                     # item 5, invented
done("chapter 4 set")

# Chapter 5 set: 1b 2d 3c 4b 5a
assert 5_000_000 + 200_000 == 5_200_000                                                    # item 1, 52 lakh
fin = pd.read_sql("""SELECT c.segment, o.quarter, sum(o.amount) AS revenue FROM orders o
                     JOIN customers c ON c.customer_id = o.customer_id GROUP BY c.segment, o.quarter""", ENG)
assert (len(fin), len(orders) + len(customers), len(orders)) == (8, 1340, 1000)             # item 3: rows moved
grain = pd.read_sql("""SELECT c.segment, o.quarter, o.channel, c.city, sum(o.amount) AS revenue
                       FROM orders o JOIN customers c ON c.customer_id = o.customer_id
                       GROUP BY 1, 2, 3, 4""", ENG)                                         # item 4, key b
assert (customers["segment"].nunique(), orders["quarter"].nunique(), orders["channel"].nunique(),
        customers["city"].nunique()) == (4, 2, 3, 6) and 4 * 2 * 3 * 6 == 144 and len(grain) == 134
every = orders.merge(customers, on="customer_id", validate="many_to_one")
for cut in (["segment"], ["channel"], ["city"], ["segment", "channel"], ["city", "quarter"]):
    assert grain.groupby(cut)["revenue"].sum().astype(float).round(2).equals(every.groupby(cut)["amount"].sum().round(2))
assert grain["revenue"].astype(float).sum() == 198_400_000
by_seg = table.groupby("segment")["spend"].sum()
fin_seg = fin.groupby("segment")["revenue"].sum()
assert all(float(fin_seg[s]) == by_seg[s] for s in by_seg.index)                           # item 5's check holds
done("chapter 5 set")

# Chapter 6 set: 1b 2c 3d 4a 5b
assert (date(2026, 6, 30) - date(2026, 5, 20)).days == 41                                  # item 1, key b
assert (date(2026, 7, 13) - date(2026, 5, 20)).days == 54 and (date(2026, 7, 13) - date(2026, 6, 30)).days == 13
recency = (AS_OF - table["last_order"]).dt.days
assert AS_OF == pd.Timestamp("2026-09-28") and recency.min() == 0
assert int((pd.Timestamp("2026-10-05") - table["last_order"]).dt.days.min()) == 7           # item 2, key c
assert int((pd.Timestamp("2026-09-21") - table["last_order"]).dt.days.min()) == -7          # item 2, option d
cut = pd.Timestamp("2026-08-31")                                                           # item 3, the auditor's Monday
kept = orders[orders["order_date"] < cut]
aug = (kept.groupby("customer_id")
           .agg(last_order=("order_date", "max"), frequency=("order_id", "count"), spend=("amount", "sum"))
           .reset_index())
aug = customers.merge(aug, on="customer_id", how="left", validate="one_to_one")
aug = aug.assign(frequency=aug["frequency"].fillna(0).astype("int64"), spend=aug["spend"].fillna(0))
aug_as_of = kept["order_date"].max()
aug_rec = (aug_as_of - aug["last_order"]).dt.days
aug_total = float(kit.sql("SELECT sum(amount) AS s FROM orders WHERE order_date < DATE '2026-08-31'")[0]["s"])
assert (len(kept), kept["amount"].sum(), aug_as_of) == (848, 171_959_570, pd.Timestamp("2026-08-28"))
assert aug["customer_id"].is_unique and len(aug) == 340 and aug["spend"].sum() == aug_total   # key d: all four pass
assert aug_rec.min() == 0 and int((aug["frequency"] == 0).sum()) == 47 and int((aug_rec > 60).sum()) == 103
assert int((cut - aug["last_order"]).dt.days.min()) == 3                                    # option b: recency guard fires
assert aug["spend"].sum() != orders["amount"].sum() == 198_400_000                          # option c: spend guard fires
late = orders[orders["order_date"] >= cut]
assert (len(late), late["amount"].sum()) == (152, 26_440_430)                               # option a keeps September
assert int((table["last_order"] >= cut).sum()) == 118 and int((cut - table["last_order"]).dt.days.min()) == -28
shape_ok = table["customer_id"].is_unique and recency.min() == 0                           # item 5: the guards see no age
assert shape_ok and len(table) == 340 and table["spend"].sum() == orders["amount"].sum()
assert 15 > 7 >= 1                                                                         # item 5, invented ages


def fired(t):
    """The guards a copy of the table trips, in the order the item names them."""
    r = (AS_OF - t["last_order"]).dt.days if "rec" not in t else t["rec"]
    return [name for name, ok in (("key", t["customer_id"].is_unique), ("count", len(t) == 340),
                                  ("spend", t["spend"].sum() == orders["amount"].sum()),
                                  ("recency", r.min() == 0)) if not ok]


assert fired(table) == []
assert fired(table[table["frequency"] > 0]) == ["count"]                                   # item 4, copy 1
wall = table.assign(rec=(pd.Timestamp("2026-10-19") - table["last_order"]).dt.days)
assert fired(wall) == ["recency"]                                                          # item 4, copy 2
doubled = table.copy()
doubled.loc[doubled.index[0], "spend"] += 500                                              # one order added again
assert fired(doubled) == ["spend"]                                                         # item 4, copy 3
lists = {d: int(((pd.Timestamp(d) - table["last_order"]).dt.days > 60).sum())
         for d in ("2026-10-15", "2026-10-19", "2026-10-26", "2026-11-02")}
assert lists == {"2026-10-15": 154, "2026-10-19": 166, "2026-10-26": 180, "2026-11-02": 187}
assert int((recency > 60).sum()) == 111
done("chapter 6 set")

# The second case: 1b 2b 3a 4d 5d 6c
rp = orders.merge(customers, on="customer_id").query("segment == 'Retail-Plus'")
ids = {q: list(rp.loc[rp["quarter"] == q, "customer_id"]) for q in ("Q1", "Q2")}
assert {q: len(set(v)) for q, v in ids.items()} == {"Q1": 91, "Q2": 76}
assert len(set(ids["Q1"]) | set(ids["Q2"])) == 107 and len(set(ids["Q1"]) & set(ids["Q2"])) == 60
assert (round(215 / 91, 3), round(140 / 76, 3)) == (2.363, 1.842) and round((1.842 / 2.363 - 1) * 100) == -22
assert (len(rp), len(orders)) == (355, 1000)                                               # rows fetched 355, 2, 1,000
assert kit.sql("SELECT count(*) AS n FROM customers WHERE segment = 'Retail Plus'")[0]["n"] == 0  # 3b matches no row
once = rp.drop_duplicates("customer_id").groupby("quarter").size()
assert int(once.sum()) == 107 and once.to_dict() != {"Q1": 91, "Q2": 76}                   # 4c counts each member once
done("second case")

# The practice lab: 1c 2a 3d 4b 5a 6c 7b 8d 9a, then problems 3 and 4
assert customers.groupby("city").size().shape[0] == 6
assert orders.groupby(["customer_id", "quarter"]).size().shape[0] == 471
assert orders.pivot_table(index="channel", columns="quarter", values="amount", aggfunc="sum").shape == (3, 2)
assert orders.groupby("customer_id").agg(first=("order_date", "min"), last=("order_date", "max")).shape == (301, 2)
assert int((recency > 45).sum()) == 144
ch = orders.pivot_table(index="customer_id", columns="channel", values="order_id", aggfunc="count", fill_value=0)
ct = customers.merge(ch.reset_index(), on="customer_id", how="left", validate="one_to_one")
cols = ["app", "store", "web"]
ct[cols] = ct[cols].fillna(0).astype("int64")
ordered = ct[ct[cols].sum(axis=1) > 0]
ties = ordered[cols].eq(ordered[cols].max(axis=1), axis=0).sum(axis=1) > 1
assert (len(ct), int(ct[cols].values.sum()), len(ordered), int(ties.sum())) == (340, 1000, 301, 98)
assert ct.loc[ct[cols].sum(axis=1) == 0, cols].idxmax(axis=1).eq("app").all()               # 39 empty rows read app
assert ordered[cols].idxmax(axis=1).value_counts().to_dict() == {"app": 149, "store": 92, "web": 60}
q = orders.pivot_table(index="customer_id", columns="quarter", values="amount", aggfunc="sum", fill_value=0)
m = customers[customers["segment"] == "Retail-Plus"].merge(q.reset_index(), on="customer_id", how="left",
                                                           validate="one_to_one")
m[["Q1", "Q2"]] = m[["Q1", "Q2"]].fillna(0)
m = m.merge(first, on="customer_id", how="left", validate="one_to_one").assign(reached=lambda d: d["exposed_date"].notna())
less = m["Q2"] < m["Q1"]
assert (len(m), m["Q1"].sum() + m["Q2"].sum(), int(m["reached"].sum())) == (120, 999150, 60)
assert (int((less & m["reached"]).sum()), int((less & ~m["reached"]).sum())) == (33, 34)
q1_buyers = m["Q1"] > 0                                                                    # problem 4's base
assert (int((q1_buyers & m["reached"]).sum()), int((q1_buyers & ~m["reached"]).sum())) == (44, 47)
assert (round(33 / 44 * 100, 1), round(34 / 47 * 100, 1)) == (75.0, 72.3)
assert int((less & ~q1_buyers).sum()) == 0                                                 # only a Q1 buyer can spend less
rp_rec = (AS_OF - m.merge(rfm, on="customer_id", how="left")["last_order"]).dt.days
assert rp_rec.min() == 0 and int((rp_rec > 60).sum()) == 47
done("practice lab")

# The Kahoot: Q2's shape, two keys and two measures
k2 = (orders.merge(customers, on="customer_id")
            .groupby(["segment", "quarter"]).agg(n=("order_id", "count"), spend=("amount", "sum")))
assert k2.shape == (8, 2)
done("kahoot")

# The take-home's self-check, on the staging snapshot
to = pd.read_csv(DATA / "C2_W02_D04_takehome_orders_STUDENT.csv", parse_dates=["order_date"])
tc = pd.read_csv(DATA / "C2_W02_D04_takehome_customers_STUDENT.csv")
tx = pd.read_csv(DATA / "C2_W02_D04_takehome_exposure_STUDENT.csv", parse_dates=["exposed_date"])
tr = to.groupby("customer_id").agg(last_order=("order_date", "max"), frequency=("order_id", "count"),
                                   spend=("amount", "sum")).reset_index()
tt = tc.merge(tr, on="customer_id", how="left", validate="one_to_one")
tt = tt.assign(frequency=tt["frequency"].fillna(0).astype("int64"), spend=tt["spend"].fillna(0))
tf = tx.sort_values("exposed_date").drop_duplicates("customer_id", keep="first")
tt = tt.merge(tf[["customer_id", "exposed_date"]], on="customer_id", how="left", validate="one_to_one")
t_rec = (to["order_date"].max() - tt["last_order"]).dt.days
assert (len(tr), len(tt), tt["spend"].sum(), to["order_date"].max()) == (309, 340, 198_400_000, pd.Timestamp("2026-09-28"))
assert (t_rec.min(), int((tt["frequency"] == 0).sum())) == (0, 31)
assert (int(tt["exposed_date"].notna().sum()), int((tt["exposed_date"].notna() & (tt["frequency"] > 0)).sum())) == (153, 142)
assert [int((t_rec > d).sum()) for d in (45, 60, 90)] == [150, 123, 77]
assert [int(((pd.Timestamp(d) - tt["last_order"]).dt.days > 60).sum()) for d in ("2026-10-15", "2026-10-19")] == [153, 162]
trp = to.merge(tc, on="customer_id").query("segment == 'Retail-Plus'")
assert [round(len(trp[trp["quarter"] == q]) / trp.loc[trp["quarter"] == q, "customer_id"].nunique(), 3)
        for q in ("Q1", "Q2")] == [2.194, 1.867]
done("take-home self-check")

# The stretch extra: the channel switch on the warehouse
def main_channel(qq):
    p = orders[orders["quarter"] == qq].pivot_table(index="customer_id", columns="channel", values="order_id",
                                                     aggfunc="count", fill_value=0)
    tie = p.eq(p.max(axis=1), axis=0).sum(axis=1) > 1
    return p.idxmax(axis=1).where(~tie, "mixed")


both = pd.concat([main_channel("Q1").rename("q1"), main_channel("Q2").rename("q2")], axis=1, join="inner")
clear = both[(both["q1"] != "mixed") & (both["q2"] != "mixed")]
assert (len(both), len(both) - len(clear), len(clear), int((clear["q1"] != clear["q2"]).sum())) == (170, 77, 93, 67)
done("tiered extras")

print("every proof holds")

# Test inputs and expected outcomes
# --------------------------------
# python3 content/W02/D4/internal/C2_W02_D04_key_proofs_INTERNAL.py
#     Prints PASS for each of the eleven blocks, then "every proof holds".
# Running it with the warehouse down
#     Stops at kit.engine() with the helper's message naming load_warehouse.sh.
# Running it after an item's number is edited without the data changing
#     Stops on that block's assertion, naming the line whose number no longer holds.
