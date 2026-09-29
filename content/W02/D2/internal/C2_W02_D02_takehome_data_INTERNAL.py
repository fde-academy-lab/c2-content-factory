"""Write the Week 2 Tuesday take-home book: content/W02/D2/data/C2_W02_D02_takehome_STUDENT.sql.

INTERNAL. The client-zero generator (data/generate_client_zero.py) has no second v4 sample, so this
seeded builder writes a smaller, invented book of its own: 120 orders over one quarter (Q2, order
dates 2026-07-01 to 2026-09-10), three channels, the payments posted against them and the refunds
raised inside the quarter. It loads into its own schema, `takehome`, so it never touches the
warehouse tables the day's rounds run on.

The book carries five plants of its own. They are named here and in the lead's TRAINER paragraph
for the day sheet, and never in the STUDENT data file or the brief:

  1. Four delivered orders with no payment row, one of them a large Business invoice.
  2. Three small card orders whose first instalment the gateway posted twice (same order, same
     instalment, same amount, same day, new payment id).
  3. One orphan payment against an order id that is not in the book.
  4. One large two-instalment order whose second instalment never arrived (a partial payment).
  5. Two partial refunds dated inside the quarter, stored as negative amounts, as the warehouse
     stores them.

Run: python3 content/W02/D2/internal/C2_W02_D02_takehome_data_INTERNAL.py
Then: psql -v ON_ERROR_STOP=1 -f content/W02/D2/data/C2_W02_D02_takehome_STUDENT.sql
The output is identical on every run, because every draw comes from one seeded generator.
"""
import datetime as dt
import pathlib
import random

SEED = 20261013
N_ORDERS = 120
Q_START = dt.date(2026, 7, 1)
LAST_ORDER = dt.date(2026, 9, 10)
LARGE = 50_000                      # at or above this, an order is settled in two instalments
SPLIT = 0.6                         # the first instalment's share of a two-instalment order

OUT = (pathlib.Path(__file__).resolve().parent.parent / "data" / "C2_W02_D02_takehome_STUDENT.sql")

# The plants, by order id. Chosen by hand so that each sits on a plausible order.
UNPAID = ["TH-0017", "TH-0046", "TH-0071", "TH-0103"]
UNPAID_LARGE = "TH-0071"            # forced to a large Business invoice below
RETRIED = ["TH-0024", "TH-0058", "TH-0089"]
PARTIAL = "TH-0035"                 # forced to a large order; second instalment never arrives
ORPHAN_ORDER_ID = "TH-0131"
REFUNDED = {"TH-0012": (-1_850, "damaged"), "TH-0064": (-2_400, "wrong item")}


def rupees(x):
    return int(round(x / 10.0)) * 10


def build():
    rng = random.Random(SEED)
    span = (LAST_ORDER - Q_START).days
    channels = ["app", "store", "web"]
    methods = ["upi", "netbanking", "wallet", "card"]

    orders = []
    for i in range(1, N_ORDERS + 1):
        oid = f"TH-{i:04d}"
        channel = channels[rng.randrange(3)]
        day = Q_START + dt.timedelta(days=rng.randrange(span + 1))
        if rng.random() < 0.12:
            amount = rupees(rng.uniform(60_000, 2_40_000))
        else:
            amount = rupees(rng.lognormvariate(8.3, 0.7))
            amount = max(420, min(amount, 38_000))
        customer = f"CG-{rng.randrange(1, 71):03d}"
        orders.append({"order_id": oid, "customer_id": customer, "order_date": day,
                       "channel": channel, "amount": amount, "status": "delivered"})

    by_id = {o["order_id"]: o for o in orders}
    # Force the plant shapes onto the chosen orders.
    by_id[UNPAID_LARGE].update(amount=3_86_500, channel="web")
    by_id[PARTIAL].update(amount=1_72_400, channel="store")
    for oid in RETRIED:
        by_id[oid]["amount"] = rupees(rng.uniform(1_200, 5_800))
    for oid in UNPAID:
        if oid != UNPAID_LARGE and by_id[oid]["amount"] >= LARGE:
            by_id[oid]["amount"] = rupees(rng.uniform(900, 9_000))

    payments = []

    def pay(order_id, paid_date, amount, method, instalment):
        payments.append({"order_id": order_id, "paid_date": paid_date, "amount": amount,
                         "method": method, "instalment_no": instalment})

    for o in orders:
        oid = o["order_id"]
        if oid in UNPAID:
            continue
        method = "card" if oid in RETRIED else methods[rng.randrange(4)]
        first_day = o["order_date"] + dt.timedelta(days=rng.randrange(3))
        if o["amount"] >= LARGE:
            first = rupees(o["amount"] * SPLIT)
            pay(oid, first_day, first, method, 1)
            if oid != PARTIAL:
                pay(oid, first_day + dt.timedelta(days=15), o["amount"] - first, method, 2)
        else:
            pay(oid, first_day, o["amount"], method, 1)
            if oid in RETRIED:
                pay(oid, first_day, o["amount"], method, 1)

    pay(ORPHAN_ORDER_ID, dt.date(2026, 8, 21), 4_750, "wallet", 1)

    payments.sort(key=lambda p: (p["paid_date"], p["order_id"], p["instalment_no"]))
    for n, p in enumerate(payments, start=1):
        p["payment_id"] = f"TP-{n:04d}"

    refunds = []
    for n, (oid, (amount, reason)) in enumerate(sorted(REFUNDED.items()), start=1):
        refund_day = by_id[oid]["order_date"] + dt.timedelta(days=9)
        refunds.append({"refund_id": f"TR-{n:03d}", "order_id": oid, "refund_date": refund_day,
                        "amount": amount, "reason": reason})
    return orders, payments, refunds


def sql(orders, payments, refunds):
    lines = [
        "-- Week 2, Tuesday take-home: a second book, invented for tonight.",
        "-- The Q2 orders of an invented second book, the payments posted against them and the",
        "-- refunds raised inside the quarter. Every number in this file is invented.",
        "-- It loads into its own schema, takehome, and never touches the warehouse tables.",
        "-- Load it once: psql -d kalpa -v ON_ERROR_STOP=1 -f data/C2_W02_D02_takehome_STUDENT.sql",
        "-- Then query takehome.orders, takehome.payments and takehome.refunds.",
        "",
        "SET client_min_messages = warning;",
        "CREATE SCHEMA IF NOT EXISTS takehome;",
        "DROP TABLE IF EXISTS takehome.orders, takehome.payments, takehome.refunds;",
        "",
        "CREATE TABLE takehome.orders (",
        "    order_id     text PRIMARY KEY,",
        "    customer_id  text NOT NULL,",
        "    order_date   date NOT NULL,",
        "    channel      text NOT NULL,",
        "    amount       numeric(12, 2) NOT NULL,",
        "    status       text NOT NULL",
        ");",
        "",
        "CREATE TABLE takehome.payments (",
        "    payment_id     text PRIMARY KEY,",
        "    order_id       text NOT NULL,",
        "    paid_date      date NOT NULL,",
        "    amount         numeric(12, 2) NOT NULL,",
        "    method         text NOT NULL,",
        "    instalment_no  integer NOT NULL",
        ");",
        "",
        "CREATE TABLE takehome.refunds (",
        "    refund_id    text PRIMARY KEY,",
        "    order_id     text NOT NULL,",
        "    refund_date  date NOT NULL,",
        "    amount       numeric(12, 2) NOT NULL,",
        "    reason       text NOT NULL",
        ");",
        "",
        "INSERT INTO takehome.orders (order_id, customer_id, order_date, channel, amount, status) VALUES",
    ]
    rows = [f"    ('{o['order_id']}', '{o['customer_id']}', '{o['order_date']}', '{o['channel']}', "
            f"{o['amount']}, '{o['status']}')" for o in orders]
    lines.append(",\n".join(rows) + ";")
    lines += ["", "INSERT INTO takehome.payments (payment_id, order_id, paid_date, amount, method, "
              "instalment_no) VALUES"]
    rows = [f"    ('{p['payment_id']}', '{p['order_id']}', '{p['paid_date']}', {p['amount']}, "
            f"'{p['method']}', {p['instalment_no']})" for p in payments]
    lines.append(",\n".join(rows) + ";")
    lines += ["", "INSERT INTO takehome.refunds (refund_id, order_id, refund_date, amount, reason) VALUES"]
    rows = [f"    ('{r['refund_id']}', '{r['order_id']}', '{r['refund_date']}', {r['amount']}, "
            f"'{r['reason']}')" for r in refunds]
    lines.append(",\n".join(rows) + ";")
    lines += ["", "SELECT 'takehome loaded' AS status,",
              "       (SELECT count(*) FROM takehome.orders) AS orders,",
              "       (SELECT count(*) FROM takehome.payments) AS payments,",
              "       (SELECT count(*) FROM takehome.refunds) AS refunds;", ""]
    return "\n".join(lines)


if __name__ == "__main__":
    o, p, r = build()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(sql(o, p, r), encoding="utf-8")
    print(f"wrote {OUT} with {len(o)} orders, {len(p)} payments, {len(r)} refunds")
