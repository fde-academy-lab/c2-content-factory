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


# Chapter 1 set: 1c 2b 3d 4a 5b
half = customers.merge(rfm, on="customer_id", how="left", validate="one_to_one")
assert round(half["frequency"].mean(), 2) == 3.32 and round(1000 / 340, 2) == 2.94      # item 2
flipped = rfm.merge(customers, on="customer_id", how="left", validate="one_to_one")
flipped = flipped.assign(frequency=flipped["frequency"].fillna(0).astype("int64"))
assert (len(flipped), int((flipped["frequency"] == 0).sum())) == (301, 0)                  # item 3
no_orders = kit.sql("""SELECT count(*) AS n FROM customers c
                       WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id)""")
assert no_orders[0]["n"] == 39 == int((table["frequency"] == 0).sum())                     # item 4
done("chapter 1 set")

# Chapter 2 set: 1c 2b 3d 4a 5c
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
reached_sql = kit.sql("SELECT sum(amount) AS s FROM orders WHERE customer_id IN "
                      "(SELECT customer_id FROM campaign_exposure)")[0]["s"]
assert float(reached_sql) == 878980                                                        # item 5, key c
done("chapter 2 set")

# Chapter 3 set: 1b 2d 3c 4a 5b
toy = pd.DataFrame({"member": ["M1", "M1", "M1", "M2"], "month": ["Apr", "Apr", "May", "Apr"],
                    "amount": [1000, 3000, 2000, 4000]})
avg = toy.pivot_table(index="member", columns="month", values="amount")
assert avg["Apr"].sum() == 6000 and toy.loc[toy["month"] == "Apr", "amount"].sum() == 8000  # item 1, key b
assert round(8000 / 3) == 2667
assert 310000 + 290000 == 600000 and round((290000 / 310000 - 1) * 100, 1) == -6.5         # item 2
assert 150 * 12 == 1800 and 1800 - 540 == 1260                                             # item 3 sizing
plus = orders.merge(customers, on="customer_id").query("segment == 'Retail-Plus'")
plus = plus.assign(month=plus["order_date"].dt.to_period("M").astype(str))
assert (len(plus), plus["customer_id"].nunique()) == (355, 107)
assert plus.pivot_table(index="month", columns="customer_id", values="amount", aggfunc="sum").shape == (6, 107)
done("chapter 3 set")

# Chapter 4 set: 1b 2a 3d 4b 5c
reach = pd.DataFrame({"customer_id": ["A", "B", "C", "D", "E"],
                      "segment": ["Retail-Core", "Retail-Plus", None, "Retail-Plus", None],
                      "bought": [1, 1, 0, 0, 0]})
out = reach.groupby("segment")["bought"].agg(["size", "sum"])
assert (int(out["size"].sum()), int(out["sum"].sum())) == (3, 2)                           # item 1, key b
assert round(0.96 * 1250) == 1200 and round(1200 / 1480 * 100) == 81 and 1480 - 1250 == 230  # item 3
assert [round(x * 100) for x in (610 / 5000, 190 / 800, 610 / 800, 4390 / 5000)] == [12, 24, 76, 88]  # item 5
done("chapter 4 set")

# Chapter 5 set: 1b 2d 3c 4b 5a
assert 5_000_000 + 200_000 == 5_200_000                                                    # item 1, 52 lakh
fin = pd.read_sql("""SELECT c.segment, sum(o.amount) AS revenue FROM orders o
                     JOIN customers c ON c.customer_id = o.customer_id GROUP BY c.segment""", ENG)
by_seg = table.groupby("segment")["spend"].sum()
assert all(float(r.revenue) == by_seg[r.segment] for r in fin.itertuples())                # item 5's check holds
done("chapter 5 set")

# Chapter 6 set: 1b 2c 3d 4a 5a
assert (date(2026, 6, 30) - date(2026, 5, 20)).days == 41                                  # item 1, key b
assert (date(2026, 7, 13) - date(2026, 5, 20)).days == 54
recency = (AS_OF - table["last_order"]).dt.days


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
assert ((166 - 111) * 150, (187 - 111) * 150, 166 * 150, 111 * 150) == (8250, 11400, 24900, 16650)  # item 5
done("chapter 6 set")

# The second case: 1b 2b 3a 4d 5d 6c
rp = orders.merge(customers, on="customer_id").query("segment == 'Retail-Plus'")
ids = {q: list(rp.loc[rp["quarter"] == q, "customer_id"]) for q in ("Q1", "Q2")}
assert {q: len(set(v)) for q, v in ids.items()} == {"Q1": 91, "Q2": 76}
assert len(set(ids["Q1"]) | set(ids["Q2"])) == 107 and len(set(ids["Q1"]) & set(ids["Q2"])) == 60
assert (round(215 / 91, 3), round(140 / 76, 3)) == (2.363, 1.842) and round((1.842 / 2.363 - 1) * 100) == -22
assert (len(rp), len(orders)) == (355, 1000)                                               # rows fetched 355, 2, 1,000
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
