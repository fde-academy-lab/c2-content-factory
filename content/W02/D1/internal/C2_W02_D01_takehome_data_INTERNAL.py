"""Write the Week 2 Monday take-home's second book: Kalpa Retail East, an invented region, two quarters.

Run from the repository root, with the warehouse's Postgres running:
    python3 content/W02/D1/internal/C2_W02_D01_takehome_data_INTERNAL.py           write, load, check
    python3 content/W02/D1/internal/C2_W02_D01_takehome_data_INTERNAL.py --check   rebuild in memory,
                                                                                   compare, load, check

It writes content/W02/D1/data/C2_W02_D01_takehome_STUDENT.sql. The file creates a schema named
takehome holding two tables, takehome.customers and takehome.orders, so the warehouse's public tables
are never touched, and a learner loads it with
    psql -d kalpa -f content/W02/D1/data/C2_W02_D01_takehome_STUDENT.sql

Why a second book. The standard runs the take-home on data the room has not seen, carrying its own
witnesses, and the shared generator (data/generate_client_zero.py) writes no second Week 2 sample.
Everything here is invented: Kalpa Retail does not report an east region in any other file, and the
brief says the region is invented.

The take-home's own witnesses, one for each of three of the day's traps under new numbers. They are
named only in the trainer's day sheet, never in a learner file.
1. Retail-Plus's orders per customer divide to the same whole number in both quarters, 80 over 34
   and 53 over 26 are both 2, while the numeric ratio falls from 2.35 to 2.04.
2. Twelve Retail-Plus members bought in Q1 and not in Q2, so an average of a CASE with no ELSE
   compares Q1's 34 buyers with Q2's 26 and shows a much smaller fall than the same 38 members do.
3. Every segment's quarters added run past its members: Student's 10 and 11 buyers add to 21 in a
   segment of 14 members, 12 of whom bought in the half-year.

The rows are written in a shuffled order, so a LIMIT without ORDER BY on a fresh load returns five
orders that are not the five smallest ids, and the ordered sample differs from it on the first run.

Every number the self-check prints is asserted at the end, so a change to this script that moves a
number fails here rather than shipping a self-check that no longer matches the file.
"""
import argparse
import datetime
import os
import pathlib
import random
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
OUT = ROOT / "content/W02/D1/data/C2_W02_D01_takehome_STUDENT.sql"
SEED = 20261012

CITIES = ["Kolkata", "Bhubaneswar", "Guwahati"]
QUARTERS = {"Q1": (datetime.date(2026, 4, 1), datetime.date(2026, 6, 30)),
            "Q2": (datetime.date(2026, 7, 1), datetime.date(2026, 9, 30))}
CHANNELS = ["app", "web", "store"]

# Per segment: members, who bought when (both quarters, Q1 only, Q2 only; the rest bought nothing),
# the orders each quarter, and the amount band in rupees.
PLAN = {
    "Business":    dict(members=12, both=7,  q1_only=2,  q2_only=1,  orders=(18, 17), band=(200000, 1200000, 1000)),
    "Retail-Core": dict(members=60, both=30, q1_only=12, q2_only=10, orders=(80, 79), band=(700, 3200, 10)),
    "Retail-Plus": dict(members=40, both=22, q1_only=12, q2_only=4,  orders=(80, 53), band=(1200, 4200, 10)),
    "Student":     dict(members=14, both=9,  q1_only=1,  q2_only=2,  orders=(16, 19), band=(500, 1600, 10)),
}


def spread(total, buyers, rng):
    """Give each buyer at least one order and hand out the rest at random."""
    counts = [1] * buyers
    for _ in range(total - buyers):
        counts[rng.randrange(buyers)] += 1
    return counts


def day_in(quarter, rng):
    start, end = QUARTERS[quarter]
    return start + datetime.timedelta(days=rng.randrange((end - start).days + 1))


def build():
    """The customers and orders, as lists of tuples, deterministic from SEED."""
    rng = random.Random(SEED)
    customers, orders = [], []
    cid = 0
    for segment, plan in PLAN.items():
        ids = []
        for _ in range(plan["members"]):
            cid += 1
            joined = datetime.date(2024, 1, 1) + datetime.timedelta(days=rng.randrange(700))
            customers.append((f"E-{cid:04d}", segment, rng.choice(CITIES), joined))
            ids.append(f"E-{cid:04d}")
        both = ids[:plan["both"]]
        q1_only = ids[plan["both"]:plan["both"] + plan["q1_only"]]
        q2_only = ids[plan["both"] + plan["q1_only"]:plan["both"] + plan["q1_only"] + plan["q2_only"]]
        buyers = {"Q1": both + q1_only, "Q2": both + q2_only}
        low, high, step = plan["band"]
        for q, total in zip(("Q1", "Q2"), plan["orders"]):
            for customer, n in zip(buyers[q], spread(total, len(buyers[q]), rng)):
                for _ in range(n):
                    status = rng.choices(["delivered", "returned", "cancelled"], [70, 17, 13])[0]
                    amount = rng.randrange(low // step, high // step + 1) * step
                    orders.append([customer, day_in(q, rng), q, rng.choice(CHANNELS), amount, status])
    orders.sort(key=lambda o: (o[1], o[0]))          # ids follow the date, as an order book's do
    orders = [(f"KE-{i:05d}", *o) for i, o in enumerate(orders, start=1)]
    return customers, orders


def render(customers, orders):
    """The .sql file: a schema of its own, two tables, and the rows in a shuffled order."""
    rng = random.Random(SEED + 1)
    shuffled = orders[:]
    rng.shuffle(shuffled)
    lines = [
        "-- Kalpa Retail East, the Week 2 Monday take-home's second book. INVENTED: a region Kalpa",
        "-- Retail does not report anywhere else, written by content/W02/D1/internal/",
        "-- C2_W02_D01_takehome_data_INTERNAL.py from one seed.",
        "-- Load it once:  psql -d kalpa -f content/W02/D1/data/C2_W02_D01_takehome_STUDENT.sql",
        "-- It creates the schema takehome and leaves the warehouse's own tables as they are.",
        "-- Q1 is April to June 2026 and Q2 is July to September 2026; amounts are in rupees.",
        "",
        "DROP SCHEMA IF EXISTS takehome CASCADE;",
        "CREATE SCHEMA takehome;",
        "",
        "CREATE TABLE takehome.customers (",
        "    customer_id text PRIMARY KEY,",
        "    segment     text NOT NULL,",
        "    city        text NOT NULL,",
        "    joined_date date NOT NULL",
        ");",
        "",
        "CREATE TABLE takehome.orders (",
        "    order_id    text PRIMARY KEY,",
        "    customer_id text NOT NULL REFERENCES takehome.customers (customer_id),",
        "    order_date  date NOT NULL,",
        "    quarter     text NOT NULL,",
        "    channel     text NOT NULL,",
        "    amount      numeric(12, 2) NOT NULL,",
        "    status      text NOT NULL",
        ");",
        "",
        "INSERT INTO takehome.customers (customer_id, segment, city, joined_date) VALUES",
    ]
    lines += [f"    ('{c}', '{s}', '{city}', '{j.isoformat()}')" + ("," if i < len(customers) - 1 else ";")
              for i, (c, s, city, j) in enumerate(customers)]
    lines += ["", "INSERT INTO takehome.orders (order_id, customer_id, order_date, quarter, channel, amount, status) VALUES"]
    lines += [f"    ('{o}', '{c}', '{d.isoformat()}', '{q}', '{ch}', {a}, '{st}')" + ("," if i < len(shuffled) - 1 else ";")
              for i, (o, c, d, q, ch, a, st) in enumerate(shuffled)]
    return "\n".join(lines) + "\n"


def psql(sql=None, file=None):
    env = dict(os.environ, PGPASSWORD=os.environ.get("PGPASSWORD", "postgres"))
    cmd = ["psql", "-h", env.get("PGHOST", "localhost"), "-U", env.get("PGUSER", "postgres"),
           "-d", env.get("PGDATABASE", "kalpa"), "-v", "ON_ERROR_STOP=1", "-At", "-F", "|"]
    cmd += ["-f", str(file)] if file else ["-c", sql]
    done = subprocess.run(cmd, capture_output=True, text=True, env=env)
    if done.returncode:
        sys.exit(f"psql failed: {done.stderr.strip()}")
    return [line.split("|") for line in done.stdout.strip().splitlines() if line]


def check():
    """Load the file and assert every number the brief's self-check prints."""
    psql(file=OUT)
    got = {}
    got["book"] = psql("SELECT quarter, count(*), count(DISTINCT customer_id), sum(amount)::bigint "
                       "FROM takehome.orders GROUP BY quarter ORDER BY quarter")
    got["seg"] = psql("SELECT c.segment, o.quarter, count(*), count(DISTINCT o.customer_id), "
                      "count(*) / count(DISTINCT o.customer_id), "
                      "round(count(*)::numeric / count(DISTINCT o.customer_id), 2), sum(o.amount)::bigint "
                      "FROM takehome.orders o JOIN takehome.customers c USING (customer_id) "
                      "GROUP BY c.segment, o.quarter ORDER BY 1, 2")
    got["spend"] = psql("""WITH m AS (SELECT o.customer_id,
            sum(CASE WHEN o.quarter = 'Q1' THEN o.amount END) AS q1,
            sum(CASE WHEN o.quarter = 'Q2' THEN o.amount END) AS q2
        FROM takehome.orders o JOIN takehome.customers c USING (customer_id)
        WHERE c.segment = 'Retail-Plus' GROUP BY o.customer_id)
        SELECT count(*), count(q1), count(q2), round(avg(q1)), round(avg(q2)),
               round(avg(coalesce(q1, 0))), round(avg(coalesce(q2, 0))) FROM m""")
    got["half"] = psql("SELECT c.segment, count(DISTINCT o.customer_id), "
                       "(SELECT count(*) FROM takehome.customers x WHERE x.segment = c.segment) "
                       "FROM takehome.orders o JOIN takehome.customers c USING (customer_id) "
                       "GROUP BY c.segment ORDER BY 1")
    got["sample"] = psql("SELECT order_id, amount::int FROM takehome.orders WHERE quarter = 'Q2' "
                         "AND channel = 'web' AND status = 'delivered' ORDER BY order_id LIMIT 5")
    got["unordered"] = psql("SELECT order_id FROM takehome.orders WHERE quarter = 'Q2' "
                            "AND channel = 'web' AND status = 'delivered' LIMIT 5")
    got["finger"] = psql("SELECT count(*), sum(amount)::bigint, count(DISTINCT customer_id), max(order_date) "
                         "FROM takehome.orders")
    for name, rows in got.items():
        print(name, rows)

    # The witnesses, stated as properties first, so a reader sees what each number is for.
    rp = {r[1]: r for r in got["seg"] if r[0] == "Retail-Plus"}
    assert rp["Q1"][4] == rp["Q2"][4] == "2", "Retail-Plus's integer ratio should read 2 in both quarters"
    assert float(rp["Q2"][5]) < float(rp["Q1"][5]), "the numeric ratio should fall"
    members, in_q1, in_q2, h1, h2, f1, f2 = (int(x) for x in got["spend"][0])
    assert (members, in_q1, in_q2) == (38, 34, 26)
    hurried, honest = (h2 - h1) / h1, (f2 - f1) / f1
    assert honest < hurried < 0 and honest - hurried < -0.10, "the CASE average should hide most of the fall"
    half = {r[0]: (int(r[1]), int(r[2])) for r in got["half"]}
    q = {(r[0], r[1]): int(r[3]) for r in got["seg"]}
    for s, (counted, members_s) in half.items():
        assert q[(s, "Q1")] + q[(s, "Q2")] > members_s >= counted, s
    assert [r[0] for r in got["unordered"]] != [r[0] for r in got["sample"]], \
        "a fresh load should hand an unordered LIMIT a different five"

    # The self-check's exact numbers.
    expected = {
        "book": EXPECTED_BOOK, "seg": EXPECTED_SEG, "spend": EXPECTED_SPEND,
        "half": EXPECTED_HALF, "sample": EXPECTED_SAMPLE, "finger": EXPECTED_FINGER,
    }
    for name, want in expected.items():
        if want is not None:
            assert got[name] == want, f"{name}: got {got[name]}, want {want}"
    print("every self-check number holds")


# The numbers the self-check prints, as psql returns them. None means not yet pinned.
EXPECTED_BOOK = [["Q1", "194", "95", "10951150"], ["Q2", "168", "85", "11232610"]]
EXPECTED_SEG = [["Business", "Q1", "18", "9", "2", "2.00", "10567000"],
                ["Business", "Q2", "17", "8", "2", "2.13", "10906000"],
                ["Retail-Core", "Q1", "80", "42", "1", "1.90", "150830"],
                ["Retail-Core", "Q2", "79", "40", "1", "1.98", "157970"],
                ["Retail-Plus", "Q1", "80", "34", "2", "2.35", "216940"],
                ["Retail-Plus", "Q2", "53", "26", "2", "2.04", "148080"],
                ["Student", "Q1", "16", "10", "1", "1.60", "16380"],
                ["Student", "Q2", "19", "11", "1", "1.73", "20560"]]
EXPECTED_SPEND = [["38", "34", "26", "6381", "5695", "5709", "3897"]]
EXPECTED_HALF = [["Business", "10", "12"], ["Retail-Core", "52", "60"], ["Retail-Plus", "38", "40"],
                 ["Student", "12", "14"]]
EXPECTED_SAMPLE = [["KE-00198", "906000"], ["KE-00200", "1610"], ["KE-00202", "1080"],
                   ["KE-00205", "1010"], ["KE-00208", "1380"]]
EXPECTED_FINGER = [["362", "22183760", "112", "2026-09-30"]]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="compare with the file on disk instead of writing")
    a = ap.parse_args()
    text = render(*build())
    if a.check:
        if OUT.read_text(encoding="utf-8") != text:
            sys.exit(f"{OUT.name} is stale: rerun this script without --check")
        print(f"{OUT.name} matches a fresh build")
    else:
        OUT.write_text(text, encoding="utf-8")
        print(f"wrote {OUT.relative_to(ROOT)}")
    check()


if __name__ == "__main__":
    main()
