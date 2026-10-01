"""Recount every number Friday's pack quotes, and check that no learner file carries a plant.

    python3 content/W03/D5/internal/C2_W03_D05_numbers_INTERNAL.py

Run it from the repository root. Five checks, each printed PASS or FAIL, then a RESULT line; it
exits 1 on any FAIL.

1. The data pack figures the STUDENT cards quote, recounted from the patient register, the price
   list and the site list in content/W03/D1/data/, and found on each card that quotes them.
2. Each card's arithmetic, computed from the card's own exhibit, and found in the GD prompts file
   (and, for the interview answer, in the day sheet) as those files print it.
3. The day sheet's plant table, against the generator's witness
   (python3 data/generate_kalpa_health.py --witness) and Monday's witness check, which recounts the
   dashboard's test counts from the files.
4. A plant guard over every STUDENT file in the day folder: no planted value and no plant's words.
5. The cold-run script's ten checksums, against the files in the data pack.
"""
import csv
import decimal
import hashlib
import math
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
DAY = HERE.parent
ROOT = HERE.parents[3]
DATA = ROOT / "content" / "W03" / "D1" / "data"
GD = DAY / "gd"
FAILS = []


def report(ok, label, detail=""):
    print(("PASS  " if ok else "FAIL  ") + label + (f" ({detail})" if detail else ""))
    if not ok:
        FAILS.append(label)


def load(name):
    with open(DATA / f"C2_W03_D01_{name}_STUDENT.csv", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def card(n):
    return next(GD.glob(f"C2_W03_D05_gd_card_{n:02d}_*_STUDENT.md")).read_text(encoding="utf-8")


def half_up(x, places):
    """Round as a person does, 65.55 to 65.6, where a float would give 65.5."""
    q = decimal.Decimal(1).scaleb(-places)
    return decimal.Decimal(f"{x:.10f}").quantize(q, rounding=decimal.ROUND_HALF_UP)


def money(x, cents=False):
    return f"${half_up(x, 2):,.2f}" if cents else f"${half_up(x, 0):,.0f}"


def pct(x, places=1):
    return f"{half_up(x * 100, places)} percent"


def one(x):
    return f"{half_up(x, 1)}"


def wilson(k, n, z=1.96):
    p = k / n
    d = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / d
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return centre - half, centre + half


def has(text, needle, label):
    """Find a printed figure, with line breaks and runs of spaces read as one space."""
    flat = " ".join(text.split())
    report(" ".join(needle.split()) in flat, label, f"looked for {needle!r}")


# 1. The data pack figures on the cards ---------------------------------------------------------
patients = load("patients")
catalogue = {r["code"]: r for r in load("test_catalogue")}
sites = load("sites")
n_patients = len(patients)
n_65 = sum(r["age_band"] == "65+" for r in patients)
n_dallas = sum(r["metro"] == "Dallas" for r in patients)
n_dallas_medicaid = sum(r["metro"] == "Dallas" and r["payer_type"] == "Medicaid" for r in patients)
labs = sum(r["kind"] == "laboratory" for r in sites)
centres = sum(r["kind"] == "patient service center" for r in sites)
report(n_patients == 6700, "the register holds 6,700 patients", str(n_patients))
report(n_65 == 1699 and pct(n_65 / n_patients) == "25.4 percent", "1,699 patients aged 65 and over, 25.4 percent")
report(n_dallas == 1250 and n_dallas_medicaid == 180, "Dallas: 1,250 patients, 180 on Medicaid",
       f"{n_dallas}, {n_dallas_medicaid}")
report(pct(n_dallas_medicaid / n_dallas) == "14.4 percent", "Dallas Medicaid share 14.4 percent")
report(catalogue["PNL-WEL"]["list_price_usd"] == "299" and catalogue["PNL-WEL"]["name"] == "Whole-body wellness panel",
       "the Whole-body wellness panel lists at $299")
report(catalogue["PNL-AGE"]["name"] == "Healthy aging panel", "the Healthy aging panel is on the price list")
report(labs == 6 and centres == 12, "six laboratories and twelve patient service centres", f"{labs}, {centres}")
for n in (2, 4):
    has(card(n), "| 6,700 |", f"card {n:02d} quotes the register's 6,700")
    has(card(n), "1,699, which is 25.4 percent", f"card {n:02d} quotes 1,699 aged 65 and over")
has(card(1), "| $299 |", "card 01 quotes the panel's list price")
has(card(4), "Healthy aging panel", "card 04 names the Healthy aging panel")
has(card(8), "| 1,250 |", "card 08 quotes Dallas's 1,250 patients")
has(card(10), "one in seven, 14.4 percent of 1,250", "card 10 quotes Dallas's Medicaid share")
has(card(3), "six, one in each metro", "card 03 quotes the six laboratories")
has(card(7), "twelve patient service centres", "card 07 quotes the twelve centres")

# 2. Each card's arithmetic, as the prompts file prints it ---------------------------------------
prompts = (GD / "C2_W03_D05_gd_prompts_TRAINER.md").read_text(encoding="utf-8")
day_sheet = (DAY / "trainer" / "C2_W03_D05_day_sheet_TRAINER.md").read_text(encoding="utf-8")

# Card 01: price 299 or 249, cost 130, 150 panels a month, 40 percent more at the lower price.
m0, m1 = 299 - 130, 249 - 130
month0, month1 = 150 * m0, 150 * 1.4 * m1
breakeven = month0 / m1
for s in [money(m0), money(m1), money(month0), f"{money(month1)}, which is {money(month0 - month1)} less",
          f"{breakeven:.1f}, so {math.ceil(breakeven)} whole panels", pct(breakeven / 150 - 1),
          money(210 * 249 - 150 * 299), pct((210 * 249) / (150 * 299) - 1)]:
    has(prompts, s, f"card 01: {s}")

# Card 02: 18,000 statements at $1.10; 2,700 to patients 65+, 30 percent refuse, $35, half recovered.
save = 18000 * 1.10
risk = 2700 * 0.30 * 35
lost = risk / 2
wrong = 18000 * 0.254 * 0.30 * 35 / 2
lo, hi = wilson(36, 120)
for s in [money(save), money(risk), money(lost), money(save - lost), pct(save / (2700 * 35 / 2)),
          f"about {lo * 100:.0f} to {hi * 100:.0f} percent", money(wrong), f"{18000 * 0.254:,.0f}"]:
    has(prompts, s, f"card 02: {s}")

# Card 03: six labs' samples a day, a 15 percent rise, 70 a lab on one shift, $32,000 a month.
today = {"New York": 64, "Dallas": 60, "Phoenix": 57, "Chicago": 48, "Philadelphia": 45, "Atlanta": 38}
for lab, n in today.items():
    has(prompts, f"| {lab} | {n} | {one(n * 1.15)} |", f"card 03: {lab} rises to {one(n * 1.15)}")
has(prompts, f"{pct(today['Dallas'] * 1.15 / 70)}, no room", "card 03: Dallas's share of capacity")
total = sum(today.values()) * 1.15
has(prompts, f"{one(total)} samples a day against 420", "card 03: the six labs together")
has(prompts, pct(total / 420), "card 03: the average that hides New York")
has(prompts, f"{money(32000 * 12)} a year at one lab and {money(64000 * 12)} at two", "card 03: the shifts' cost")

# Card 04: 23,000 bookings, 15 percent by phone, one in six may leave, $85 a booking, $65,000 a year.
phone = 23000 * 0.15
leave = phone / 6
lo, hi = wilson(10, 60)
for s in [f"{phone:,.0f}", f"{leave:,.0f}", money(leave * 85), money(65000 - leave * 85),
          pct(65000 / (phone * 85)), pct(1 / 6), f"about {lo * 100:.0f} to {hi * 100:.0f} percent",
          money(phone * 0.254 * 85)]:
    has(prompts, s, f"card 04: {s}")

# Card 05: 12.0 to 8.4 percent at the client lab, 11.5 to 9.9 percent at fourteen labs without it.
beyond = 1 - (8.4 / 12.0) / (9.9 / 11.5)
points = (12.0 - 8.4) - (11.5 - 9.9)
for s in [pct(1 - 8.4 / 12.0), pct(1 - 9.9 / 11.5), pct(beyond), f"{points:.1f} points, {pct(points / 12.0)} of 12.0",
          f"about ${round(300000 * beyond / 0.30, -2):,.0f}", "| 24 percent |"]:
    has(prompts, s, f"card 05: {s}")
has(day_sheet, f"about {beyond * 100:.0f} percent, and the model needed 24", "day sheet's interview answer: card 05's numbers")

# Card 06: routine and batched results at six labs.
mix = {"New York": (8300, .950, 700, .40), "Chicago": (5500, .949, 500, .40), "Dallas": (6800, .952, 700, .42),
       "Philadelphia": (5200, .951, 500, .39), "Atlanta": (4300, .947, 400, .38), "Phoenix": (5300, .962, 1900, .41)}
routine_share = sum(v[0] for v in mix.values()) / sum(v[0] + v[2] for v in mix.values())
card6 = card(6)
for lab, (rn, rs, bn, bs) in mix.items():
    overall = (rn * rs + bn * bs) / (rn + bn)
    standard = routine_share * rs + (1 - routine_share) * bs
    has(card6, f"| {lab} | {rn + bn:,} | {pct(overall)} |", f"card 06: {lab}'s overall rate on the card")
    has(prompts, f"| {lab} | {pct(bn / (rn + bn))} | {pct(overall)} | {pct(rs)} | {pct(standard)} |",
        f"card 06: {lab}'s row in the prompts file")
has(prompts, f"{routine_share * 100:.1f} percent routine", "card 06: the common mix")

# Card 07: $3.2 million at twice Kalpa's prices, plans allow 45 percent; 900 patients at $240;
# 40,000 visitors, 2 percent, $95, 55 percent within reach; costs two thirds.
outreach = 3.2e6 / 2 * 0.45
houston = 900 * 240
online = 40000 * 0.02 * 12 * 95 * 0.55
for s in [money(outreach), money(outreach / 3), f"{1.8e6 / (outreach / 3):.1f} on $1.8 million",
          money(houston), money(houston / 3), f"{2.0e6 / (houston / 3):.1f} on $2.0 million",
          money(online), money(online / 3), f"{0.6e6 / (online / 3):.1f} on $0.6 million"]:
    has(prompts, s, f"card 07: {s}")

# Card 08: 30 percent of Dallas tests, $40 allowed, 12 percent cut, $24 cost, 40 against 15 percent.
mg0, mg1 = 40 - 24, 40 * 0.88 - 24
for s in [f"| {money(mg0)} |", money(mg1, cents=True), f"| {money(30 * mg0)} |", money(42 * mg1, cents=True),
          pct(mg0 / mg1 - 1), "12 percent of all Dallas tests", "50 percent more members' tests",
          money(45 * mg1), pct(15 / 365 * 0.08), pct(1.40 * 0.88 - 1)]:
    has(prompts, s, f"card 08: {s}")

# Card 09: $75,000 of cash, $18,000 a week, $5,500 a working day, 70 claims, 15 working days.
for s in [f"about {75000 / 18000:.1f} weeks", money(5500 * 6), f"{15 * 70:,} claims and {money(15 * 5500)}",
          f"{25000 / 18000:.1f} weeks of net costs", f"{70 * 8 / 60:.1f} staff-hours", f"{1050 * 8 // 60} hours",
          f"{money(70 * 0.40)} a working day"]:
    has(prompts, s, f"card 09: {s}")

# Card 10: $75,000 specialist, $15,000 GCC, $20,000 answering service, $35,000 of payments.
for s in [money(75000 - 15000 - 20000), money(75000 - 20000 - 35000)]:
    has(prompts, s, f"card 10: {s}")

# 3. The day sheet's plant table against the witness --------------------------------------------
w = {}
out = subprocess.run([sys.executable, str(ROOT / "data" / "generate_kalpa_health.py"), "--witness"],
                     capture_output=True, text=True, cwd=ROOT).stdout
for line in out.splitlines():
    if ": " in line and not line.startswith(("PASS", "FAIL")):
        k, v = line.split(": ", 1)
        w[k.strip()] = v.strip()
d1 = subprocess.run([sys.executable, str(ROOT / "content" / "W03" / "D1" / "internal" /
                                       "C2_W03_D01_witness_check_INTERNAL.py")],
                    capture_output=True, text=True, cwd=ROOT).stdout
for m in re.finditer(r"^\s*(?:PASS\s+)?(\w+): ([\d.\-]+)", d1, re.M):
    w.setdefault(m.group(1), m.group(2))
num = lambda k: float(w[k])
plant = [
    ("dashboard_q2_to_q3", pct(num("dashboard_q2_to_q3"))),
    ("dashboard counts", f"{int(num('dashboard_Q2')):,} to {int(num('dashboard_Q3')):,} tests"),
    ("booked_q2_to_q3", pct(num("booked_q2_to_q3"))),
    ("performed_q2_to_q3", pct(num("performed_q2_to_q3"))),
    ("bookings_q2_to_q3", pct(num("bookings_q2_to_q3"))),
    ("employer_tests", f"add {int(num('employer_tests')):,} tests to Q3"),
    ("contract_amount", money(num("contract_amount"))),
    ("contract_share_of_q3", pct(num("contract_share_of_q3"))),
    ("q3_billed", money(num("q3_billed"))),
    ("q3_mean_claim", money(num("q3_mean_claim"), cents=True)),
    ("q3_mean_without_contract", money(num("q3_mean_without_contract"), cents=True)),
    ("q3_median_claim", f"median of {money(num('q3_median_claim'))}"),
    ("text_amounts", f"{int(num('text_amounts'))} billed amounts are text"),
    ("claim_lines_non_employer", f"{int(num('claim_lines_non_employer')):,} claim lines"),
    ("tests_on_claimed_bookings_non_employer", f"{int(num('tests_on_claimed_bookings_non_employer')):,} tests"),
    ("tests_booked_non_employer", f"({int(num('tests_booked_non_employer')):,} counting cancelled"),
    ("switch_apparent_change", f"fall {pct(-num('switch_apparent_change'))} in the old export"),
    ("switch counts", f"({int(num('switch_metros_q2')):,} to {int(num('switch_metros_q3_legacy_only')):,} bookings)"),
    ("switch_real_change", f"{pct(-num('switch_real_change'))} across both systems ({int(num('switch_metros_q2')):,} "
                           f"to {int(num('switch_metros_q3_real')):,})"),
    ("legacy rows", f"{int(num('legacy_rows')):,} rows over {int(num('legacy_distinct_ids')):,} booking ids"),
    ("exact_join", f"{int(num('exact_join_matches'))} of {int(num('remittance_rows')):,} postings, {pct(num('exact_join_share'))}"),
    ("double_posts", f"{int(num('double_posts'))} double posts worth {money(num('double_posted_dollars'), cents=True)}"),
    ("reversals", f"{int(num('reversals'))} reversals"),
    ("claims_without_posting", f"{int(num('claims_without_posting'))} claims with no posting"),
    ("denial_postings", f"{int(num('denial_postings')):,} denial postings"),
    ("denial count", f"{int(num('denial_postings')):,} denial postings"),
    ("denied_billed", money(num("denied_billed"))),
    ("paid_net_of_double_posts", f"{money(num('paid_net_of_double_posts'))} against {money(num('billed_all'))}"),
    ("small site", f"{int(num('small_site_scheduled'))} scheduled and {int(num('small_site_walk_ins'))} walk-in"),
    ("small_site_rate_all_visits", f"On all visits {pct(num('small_site_rate_all_visits'))} against "
                                   f"{pct(num('others_rate_all_visits'))}"),
    ("small_site_rate_scheduled", f"{pct(num('small_site_rate_scheduled'))} ({int(num('small_site_no_shows'))} of "
                                  f"{int(num('small_site_scheduled'))}) against {pct(num('others_rate_scheduled'))}"),
    ("small_site_tail_probability", f"probability {num('small_site_tail_probability'):.2f}"),
    ("campaign_lift_aggregate", f"book {pct(num('campaign_lift_aggregate'))} more overall"),
    ("campaign_metros_prior_change", f"rose {pct(num('campaign_metros_prior_change'))} in the two months"),
]
for label, s in plant:
    has(day_sheet, s, f"day sheet's plant table: {label}")
for metro, key in [("Dallas", "lift_Dallas"), ("Atlanta", "lift_Atlanta"), ("Phoenix", "lift_Phoenix")]:
    has(day_sheet, f"{metro} minus {-num(key) * 100:.1f}", f"day sheet's plant table: {metro}'s gap inside the offer")
ny = float(re.search(r"'New York': ([\d.\-]+)", w["campaign_lift_other_metros"]).group(1))
has(day_sheet, f"New York's plus {ny * 100:.1f} percent", "day sheet's plant table: New York's chance gap")
# The denial rates are recounted from the claims file, since the witness prints them to four places
# and rounding those again can move the last digit: 1,175 of 11,355 is 10.348 percent, which the
# witness prints as 0.1035 and a second rounding turns into 10.4.
claims = [r for r in load("claims") if not r["employer_account"]]
denied = [r for r in claims if r["denial_category"]]
has(day_sheet, f"{len(denied):,} of the {len(claims):,} retail claims denied, {pct(len(denied) / len(claims))}",
    "day sheet's plant table: the retail denial rate")
for payer in ("Medicaid", "commercial", "Medicare"):
    rows = [r for r in claims if r["payer_type"] == payer]
    rate = sum(1 for r in rows if r["denial_category"]) / len(rows)
    has(day_sheet, f"{payer} {one(rate * 100)}", f"day sheet's plant table: {payer}'s denial rate")

# 4. The plant guard over every STUDENT file ------------------------------------------------------
GUARD = [
    r"\$?180,000", r"\b1,200\b", r"\b23\.0 percent", r"\b12\.2 percent", r"\b180 (rows|repeated)",
    r"\b280\b", r"19,204", r"\b105 reversals", r"\b398\b", r"\b1\.9 percent", r"\b10\.4 percent",
    r"\b14\.9\b", r"\b11\.3\b", r"\b8\.8 percent", r"\b18\.8\b", r"\b7\.9 percent", r"\b19\.0 percent",
    r"\b15\.1\b", r"\b0\.21\b", r"(?<![\d.])9\.0 percent", r"(?<![\d.])9 percent", r"\b6\.9 percent", r"\b23\.5\b",
    r"\b5\.1 percent", r"\$210\.50", r"\$179\.75", r"\b14\.6 percent", r"1,231,001", r"2,201,099",
    r"801,314", r"\b36\.4 percent", r"\b18\.5\b", r"\b9\.8\b",
    r"(?i)employer", r"EMP-0", r"(?i)wellness screening", r"KH-ATL-03", r"(?i)walk-in", r"(?i)re-export",
    r"(?i)month first", r"(?i)18 September", r"(?i)new (booking )?system", r"(?i)double[- ]post",
    r"(?i)duplicate (ERA|remittance|posting)", r"CLM-", r"(?i)campaign", r"(?i)at-home", r"(?i)home collection",
    r"(?i)chicago[^.\n]{0,60}philadelphia|philadelphia[^.\n]{0,60}chicago",
]
students = sorted(p for p in DAY.rglob("*_STUDENT.*") if p.suffix in (".md", ".py"))
for p in students:
    # The data pack's own file names are the data dictionary's, so they are no plant.
    text = re.sub(r"C2_W03_D01_\w+_STUDENT\.csv", "", p.read_text(encoding="utf-8"))
    hits = sorted({m.group(0) for g in GUARD for m in re.finditer(g, text)})
    report(not hits, f"plant guard: {p.relative_to(DAY)}", ", ".join(hits) if hits else "no plant value or word")

# 5. The cold-run script's checksums ----------------------------------------------------------------
script = (DAY / "checkpoints" / "C2_W03_D05_cold_run_STUDENT.py").read_text(encoding="utf-8")
pinned = dict(re.findall(r'"(C2_W03_D01_\w+_STUDENT\.csv)": "([0-9a-f]{64})"', script))
report(len(pinned) == 10, "the cold-run script pins ten files", str(len(pinned)))
for name, digest in sorted(pinned.items()):
    real = hashlib.sha256((DATA / name).read_bytes()).hexdigest()
    report(real == digest, f"checksum of {name}")

print(f"\nRESULT: {'FAIL' if FAILS else 'PASS'} ({len(FAILS)} failures)")
sys.exit(1 if FAILS else 0)
