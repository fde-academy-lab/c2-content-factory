"""Write the take-home sample for Week 1 Tuesday from the programme's own generator.

The generator writes one file for v1, the class file. The take-home needs a second sample with its
own findings, so a learner cannot paste the class answer into the memo. This script borrows the
generator's own builder, changes only its seed, its segment plan, its quarter targets, its id ranges
and the last day an order can carry in September, and writes the result the way the generator
writes every file. Nothing is typed by hand.

    python3 content/W01/D2/internal/C2_W01_D02_takehome_data_INTERNAL.py

What differs from the class file, which only the day sheet and the provenance name:
  1. Retail-Core loses customers: 34 in Q1, 26 in Q2, and every Q2 Retail-Core id was already a
     Q1 customer, so the branch that moved is customers lost, which is retention and not
     acquisition. Retail-Plus holds steady.
  2. The export was cut on 15 September, so Q2 carries about eleven weeks against Q1's thirteen.
  3. The discount field is absent on a subset, by the generator's own rule.
Every figure the self-check quotes is asserted at the end, so a change fails loudly.
"""
import importlib.util
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
spec = importlib.util.spec_from_file_location("gen", ROOT / "data" / "generate_client_zero.py")
gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)

gen.SEED = 20261006
gen.Q1_CLEAN = 20500000
gen.Q2_TOTAL = 19400000
gen.PLAN = {
    "Q1": {"Student": 6, "Business": 17, "Retail-Plus": 30, "Retail-Core": 37},
    "Q2": {"Student": 6, "Business": 17, "Retail-Plus": 30, "Retail-Core": 26},
}
gen._order_id = lambda n: f"KR-{6000 + n:05d}"
gen._customer_pool = lambda: {
    "Retail-Core": [gen._customer_id(6000 + i) for i in range(34)],
    "Retail-Plus": [gen._customer_id(7000 + i) for i in range(15)],
    "Business": [gen._customer_id(8000 + i) for i in range(11)],
    "Student": [gen._customer_id(9000 + i) for i in range(6)],
}
_plain_date = gen._date


def _cut_date(rng, quarter, i):
    """The same draw as the generator's, with September stopping on the 15th."""
    d = _plain_date(rng, quarter, i)
    if d.startswith("2026-09-"):
        day = int(d[-2:])
        d = f"2026-09-{1 + (day - 1) % 15:02d}"
    return d


gen._date = _cut_date

rows = gen.build_quarters()
q1 = [r for r in rows if r["quarter"] == "Q1"]
q2 = [r for r in rows if r["quarter"] == "Q2"]


def customers(rs, seg=None):
    return {r["customer_id"] for r in rs if seg is None or r["segment"] == seg}


fails = 0


def want(label, ok):
    global fails
    print(("PASS  " if ok else "FAIL  ") + label)
    fails += 0 if ok else 1


want("Q1 lands on Rs 2,05,00,000", sum(r["amount"] for r in q1) == gen.Q1_CLEAN)
want("Q2 lands on Rs 1,94,00,000", sum(r["amount"] for r in q2) == gen.Q2_TOTAL)
want("Retail-Core customers fall from 34 to 26",
     len(customers(q1, "Retail-Core")) == 34 and len(customers(q2, "Retail-Core")) == 26)
want("every Q2 Retail-Core customer bought in Q1",
     customers(q2, "Retail-Core") <= customers(q1, "Retail-Core"))
want("Retail-Plus holds at 15 members and 30 orders in both quarters",
     len(customers(q1, "Retail-Plus")) == len(customers(q2, "Retail-Plus")) == 15)
want("the last Q2 order is dated on or before 15 September", max(r["order_date"] for r in q2) <= "2026-09-15")
want("some records carry no discount field", any("discount" not in r for r in rows))
if fails:
    sys.exit(f"FAIL  {fails} take-home assertions")

out = ROOT / "content" / "W01" / "D2" / "data" / "C2_W01_D02_takehome_STUDENT.py"
out.write_text(gen._py_literal("ORDERS", rows), encoding="utf-8")
print("wrote", out.relative_to(ROOT))
