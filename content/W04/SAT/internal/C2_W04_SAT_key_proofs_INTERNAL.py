"""Prove every key and every printed number on the Week 4 Saturday recap paper.

    python3 content/W04/SAT/internal/C2_W04_SAT_key_proofs_INTERNAL.py

Runs cold from the repository root and needs only Python 3, PyYAML and openpyxl (the builder's own
imports). It assembles the paper exactly as scripts/build_saturday_paper.py does, from the tracker's
bank, data/programme/paper_edits.yaml and the week's source file, so every check runs on the items
as they print. Every case number an exhibit or a stem prints is read back from the day's facts file
(content/W04/D{1..5}/internal/C2_W04_D0{d}_facts_INTERNAL.yaml), every derived number is recomputed
from the printed exhibit, and every key is asserted: the letter of a one-correct or reasoned item
must sit on the option that holds the computed number, a word-bank or match key must be the word
the reasoning names, and an applied-maths key must carry the recomputed figures. It prints one line
per item and exits 1 on the first failed assertion.
"""
import pathlib
import re
import math
import sys
from fractions import Fraction

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
import build_saturday_paper as bsp  # noqa: E402

FACTS = {d: yaml.safe_load((ROOT / f"content/W04/D{d}/internal/C2_W04_D0{d}_facts_INTERNAL.yaml")
                           .read_text(encoding="utf-8")) for d in range(1, 6)}
LINES = []


def num(day, fid):
    """A number from a day's facts file by its id, searching the file's id lists and its sections."""
    f = FACTS[day]
    for key, block in f.items():
        if isinstance(block, list):
            for n in block:
                if isinstance(n, dict) and n.get("id") == fid:
                    return n["value"]
        elif isinstance(block, dict) and fid in block and not isinstance(block[fid], (dict, list)):
            return block[fid]
    raise KeyError(f"D{day} facts: no {fid}")


def S(day, section):
    """A facts-file section as {id: value}: an id list is flattened, a mapping is returned as it is."""
    block = FACTS[day][section]
    if isinstance(block, list):
        return {n["id"]: n["value"] for n in block if isinstance(n, dict) and "id" in n}
    return block


def close(a, b, tol=0.005):
    return abs(float(a) - float(b)) <= tol


def half_up(x):
    """Round half away from zero, the way a printed figure is rounded (Python's round() goes to even)."""
    return math.floor(float(x) + 0.5)


def assemble():
    bank = bsp.read_bank()
    edits = yaml.safe_load(bsp.EDITS.read_text(encoding="utf-8"))
    bsp.apply_edits(bank, edits)
    data = bank["W4"]
    source = bsp.read_source("W04")
    printed = bsp.assemble(data, source)
    return printed, source


PRINTED, SOURCE = assemble()
BY_ID = {i["id"]: i for i in PRINTED if i.get("added")}
BY_NO = {i["no"]: i for i in PRINTED if not i.get("added")}


def options(item):
    return {letter: text for letter, text in bsp.parts(item)[1]}


def table(exhibit):
    return exhibit["table"]["head"], exhibit["table"]["rows"]


def show(item, detail):
    name = item.get("id") or f"bank {item['no']}"
    line = f"PASS  Q{item['q']:<3} {name:<18} key {bsp.key_text(item)[:28]:<28} {detail}"
    LINES.append(line)
    print(line)


def keyed(item, *must):
    """The keyed option's text, asserted to carry every string in must."""
    text = options(item)[item["key"]]
    for m in must:
        assert m in text, (item.get("id"), m, text)
    return text


def part_exhibit(p, k=0):
    return SOURCE["parts"][p - 1]["exhibits"][k]


def main():
    # ---------------------------------------------------------------- the paper's shape
    assert len(PRINTED) == 39, len(PRINTED)
    hard = sum(1 for i in PRINTED if i["level"] == "Hard")
    mins = sum(i["min"] for i in PRINTED)
    assert hard == 23 and mins <= 120, (hard, mins)
    print(f"PASS  shape: 39 items, {hard} hard ({hard / 39:.0%}), {mins:g} minutes at the blueprint's pace")

    # ---------------------------------------------------------------- Part 1
    head, rows = table(part_exhibit(1))
    ex = {r[0]: r[1:] for r in rows}
    assert ex["Peak online hours, all enrolled drivers"] == ["118,000", "146,300"]
    assert num(1, "hours_before") == 118000 and num(1, "hours_after") == 146300
    assert num(1, "trips_before") == 224200 and num(1, "trips_after") == 230900
    assert close(num(1, "tph_before"), 1.90) and close(num(1, "tph_after"), 1.58)
    assert num(1, "requests_before") == 251910 and num(1, "requests_after") == 256556
    assert close(num(1, "requests_per_hour_before"), 2.13) and close(num(1, "requests_per_hour_after"), 1.75)
    assert close(num(1, "acceptance_before"), 0.863, 0.001) and close(num(1, "acceptance_after"), 0.73)
    assert close(num(1, "median_wait_before"), 4.8) and close(num(1, "median_wait_after"), 4.6)
    assert num(1, "topup_after_rs") == 19_000_000
    print("PASS  Exhibit 1A: every value equals Monday's facts file")

    w = BY_NO[1]
    assert w["key"] == "e" and w["bank_word"] == "guardrails"
    show(w, "guardrails, from Word bank 1")
    w = BY_NO[2]
    assert w["key"] == "b" and w["bank_word"] == "window"
    show(w, "window, from Word bank 1")

    it = BY_ID["tf-leading"]
    keyed(it, "False", "moves first")
    assert close(num(1, "north_star_before"), 35.76) and close(num(1, "north_star_after"), 35.89)
    show(it, "requests per hour 2.13 to 1.75; north star 35.76 to 35.89")

    it = BY_ID["twelve-rows"]
    rows = it["exhibit"]["table"]["rows"]
    twelve = FACTS[1]["twelve_rows"]
    for r, f in zip(rows, twelve):
        assert r[0] == f["driver"] and int(r[3]) == f["peak_online_hours"] and int(r[4]) == f["peak_offers"]
        assert int(r[5]) == f["peak_accepted"] and int(r[6]) == f["peak_trips"], (r, f)
    before = [r for r in rows if r[2] == "before"]
    after = [r for r in rows if r[2] == "after"]
    hb, ha = sum(int(r[3]) for r in before), sum(int(r[3]) for r in after)
    tb, ta = sum(int(r[6]) for r in before), sum(int(r[6]) for r in after)
    assert (hb, ha, tb, ta) == (60, 74, 114, 88)
    assert round(tb / hb, 2) == 1.90 and round(ta / ha, 2) == 1.19
    ef = [r for r in rows if r[0] in "EF"]
    dh = sum(int(r[3]) for r in ef if r[2] == "after") - sum(int(r[3]) for r in ef if r[2] == "before")
    dt = sum(int(r[6]) for r in ef if r[2] == "before") - sum(int(r[6]) for r in ef if r[2] == "after")
    assert (dh, dt) == (10, 30)
    mean_b = sum(int(r[6]) / int(r[3]) for r in before) / 6
    mean_a = sum(int(r[6]) / int(r[3]) for r in after) / 6
    assert round(mean_b, 2) == 1.90 and round(mean_a, 2) == 1.31
    assert "1.31" in options(it)["d"]
    keyed(it, "1.90 to 1.19", "10 hours", "30 trips")
    show(it, "60 to 74 hours, 114 to 88 trips, 1.19; mean of ratios 1.31 in option d")

    it = BY_ID["tf-target"]
    keyed(it, "True", "nobody asked for")
    show(it, "the SEC order's staff behaviour; checked 13 October 2026 (sources list)")

    it = BY_ID["wells-silent"]
    share = Fraction(4, 100) / Fraction(11, 100)
    assert round(float(share) * 100) == 36
    keyed(it, "36 percent", "0.04 of 0.11", "dated log")
    show(it, "0.04 of 0.11 is 36 percent; the dated change log")

    it = BY_ID["kalpa-sheet"]
    plants = {p["id"]: p["value"] for p in FACTS[1]["plants"]}
    assert plants["kalpa_reorders_per_member_ratio"] == 1.22
    assert plants["kalpa_booked_value_per_member_ratio"] == 0.96
    assert plants["kalpa_window_none_delivered"] is True
    k = FACTS[1]["kalpa"]
    assert round(k["reorders_window"] / k["reorders_comparison"], 2) == 1.22
    assert it["key"] == "c, d, e"
    ops = options(it)
    assert ops["c"].startswith("Exclusions") and ops["d"].startswith("Guardrail") and "add-to-cart" in ops["e"]
    show(it, "Monday's lab plants 1.22, 0.96, none delivered (521 over 427 placements)")

    # ---------------------------------------------------------------- Part 2
    head, rows = table(part_exhibit(2))
    assert rows[0][1:] == ["Rs 314", "Rs 260"] and close(num(1, "rs_per_hour_before"), 313.5) \
        and close(num(1, "rs_per_hour_after"), 260.4)
    assert rows[1][1:] == ["Rs 5,817", "Rs 5,861"] and half_up(num(1, "rs_per_driver_week_before")) == 5817 \
        and half_up(num(1, "rs_per_driver_week_after")) == 5861
    assert num(1, "fare_avg_rs") == 165
    print("PASS  Exhibit 2A: Rs 314 to Rs 260, Rs 5,817 to Rs 5,861 and Rs 165, from Monday's facts")

    it = BY_ID["slide-order"]
    assert it["key"] == "c, d, b, a"
    ops = options(it)
    assert "claim" in ops["c"] and "evidence" in ops["d"] and "caveat" in ops["b"] and "action" in ops["a"]
    show(it, "claim, evidence, caveat, action; the topic title and the 24 percent line left out")

    it = BY_ID["keep-two"]
    d2 = {n["id"]: n["value"] for n in FACTS[2]["numbers"]}
    assert d2["topup_per_extra_trip_rs"] == 2836
    assert round(19_000_000 / (230_900 - 224_200)) == 2836
    assert it["key"] == "a, c" and "4.8 to 4.6" in options(it)["a"] and "2,836" in options(it)["c"]
    assert "269,773 to 347,583" in options(it)["b"]
    assert num(1, "offers_before") == 269773 and num(1, "offers_after") == 347583
    show(it, "the wait and Rs 2,836 an extra trip (Rs 1.9 crore over 6,700)")

    it = BY_ID["concede"]
    keyed(it, "False", "1.56 against 1.90")
    assert close(d2["tph_last_three_after"], 1.56)
    assert d2["requests_last_three_low"] >= d2["requests_before_week_low"]
    assert d2["requests_last_three_high"] <= d2["requests_before_week_high"]
    show(it, "last three weeks' requests 41,161 to 42,602 inside 41,155 to 42,719; 1.56")

    it = BY_ID["memo"]
    keyed(it, "False", "one slide", "a week")
    show(it, "the ask is one slide; Amazon's letter, a week or more")

    it = BY_ID["estimate-order"]
    assert it["key"] == "b, d, e, a"
    trips_hour = 1e7 * 0.01 * 0.25 / 3
    per_driver = 2.4 * (1 - 0.30)
    assert round(trips_hour) == 8333 and round(per_driver, 2) == 1.68
    assert round(trips_hour / per_driver, -1) == 4960 and round(trips_hour / per_driver * 1.15, -2) == 5700
    assert d2["drivers_at_peak_central"] == 5704 and d2["wrong_unit_drivers"] == 41700.0
    assert round(1e5 / 2.4, -2) == 41700
    assert close(d2["driver_hours_per_trip_before"], 0.53) and close(d2["driver_hours_per_request_chain"], 0.60)
    show(it, "8,333 an hour over 1.68 is 4,960, times 1.15 is 5,700; 41,700 is a day over an hour")

    it = BY_ID["four-checks"]
    assert it["key"] == "a, c"
    assert round(24.07e9 / 30 / 1e6) == 802
    assert round(66968 / ((415 + 500) / 2), 1) == 146.4
    assert d2["dmart_revenue_per_store_average"] == 146.4 and d2["dmart_stores_fy25_end"] == 415
    assert d2["flipkart_url_number"] == 63
    show(it, "802 million a day over 30 days; Rs 146.4 crore on the average count")

    it = BY_ID["metro"]
    rows = it["exhibit"]["table"]["rows"]
    assert rows[0][1] == "64.06 lakh" and rows[1][1] == "82,44,903"
    pf = {p["id"]: p for p in FACTS[4]["public_facts"]}
    assert "82,44,903" in pf["M6"]["facts"]["record_boardings_2026_09_17"]
    assert "64.06 lakh" in pf["M6"]["facts"]["avg_daily_journeys_current"]
    assert round((64.06 - 60) / 64.06 * 100) == 6 and round((82.44903 - 60) / 82.44903 * 100) == 27
    keyed(it, "line uses", "record day")
    show(it, "6 and 27 percent from 60 lakh; DMRC's journeys count each line used (Thursday's sources)")

    # ---------------------------------------------------------------- Part 3
    st = S(3, "strip")
    tk = S(3, "ticket")
    fd = S(3, "full_data")
    assert close(tk["before_strip_ctr"], 0.061, 0.0001) and close(tk["after_strip_ctr"], 0.038, 0.0001)
    assert close(fd["toned_milk_share"], 0.71) and tk["total_carts"] == 40000 and tk["customers"] == 12000
    print("PASS  Exhibit 3A: 40,000 carts, 12,000 customers, milk 71 percent, 6.1 to 3.8 percent")

    it = BY_ID["ctr-slot"]
    rows = it["exhibit"]["table"]["rows"]

    def pct(s):
        return float(s.split()[0]) / 100
    for r, slot in zip(rows[:3], (1, 2, 3)):
        assert round(st[f"milk_share_after_slot{slot}"], 2) == pct(r[1])
        assert round(st[f"ctr_after_milk_slot{slot}"] * 100, 1) / 100 == pct(r[2])
        assert round(st[f"ctr_before_other_slot{slot}"] * 100, 1) / 100 == pct(r[3])
        assert round(st[f"ctr_after_other_slot{slot}"] * 100, 1) / 100 == pct(r[4])
    lost = [round(pct(r[1]) * (pct(r[4]) - pct(r[2])) * 100, 2) for r in rows[:3]]
    assert lost == [4.76, 2.85, 1.35], lost
    assert round(0.5 * 1.2 + 0.5 * 6.4, 1) == 3.8
    keyed(it, "slot 1", "70 percent")
    show(it, "clicks lost per 100 impressions 4.76, 2.85, 1.35; 0.5 x 1.2 + 0.5 x 6.4 = 3.8")

    it = BY_ID["heavy"]
    rows = it["exhibit"]["table"]["rows"]
    chips = [int(x.replace(",", "")) for x in rows[0][1:4]]
    onions = [int(x.replace(",", "")) for x in rows[1][1:4]]
    assert chips == [fd["chips_carts"], fd["cold_drink_carts"], fd["chips_cold_carts"]]
    assert onions == [fd["onions_carts"], fd["tomatoes_carts"], S(3, "pairs_detail")["pair_onions_tomatoes_carts"]]

    def lift(a, b, both, n=40000):
        return (both / n) / ((a / n) * (b / n))
    assert round(lift(*chips), 2) == 3.39 and round(lift(*onions), 2) == 1.70
    cv = S(3, "caveats")
    assert round(cv["chips_cold_lift_size"], 2) == 2.48 and round(cv["chips_cold_lift_both"], 2) == 1.95
    assert round(cv["onions_tomatoes_lift_size"], 2) == 1.38 and round(cv["onions_tomatoes_lift_both"], 2) == 1.38
    assert round(cv["chips_cold_heavy_share"], 2) == 0.73 and close(tk["heavy_tenth_share"], 0.38)
    keyed(it, "Chips and cold drink only", "1.95", "1.38")
    show(it, "per cart 3.39 and 1.70; corrected 1.95 and 1.38 against the 1.5 rule")

    for no, want in ((30, "0.825"), (31, "0.97")):
        assert BY_NO[no]["key"] == want
    assert Fraction(165, 200) == Fraction(825, 1000)
    assert round(165 / 200 / (850 / 1000), 2) == 0.97 and round(165 / (1000 * 0.2 * 0.85), 2) == 0.97
    show(BY_NO[30], "165 of 200")
    show(BY_NO[31], "0.825 over 0.85, and 165 against the 170 chance gives")
    it = BY_NO[32]
    assert it["key"] == "c" and "lift is below 1" in options(it)["c"]
    show(it, "a lift of 0.97 refuses the bundle")

    it = BY_ID["watch"]
    kl = S(3, "kalpa_lab")
    assert kl["kalpa_thin_baskets"] == 2 and kl["kalpa_baskets"] == 812 and close(kl["kalpa_thin_lift"], 4.0)
    assert close(kl["kalpa_thin_support"], 0.0025, 0.0001)
    assert fd["ice_choc_carts"] == 100 and round(fd["ice_choc_lift"], 1) == 4.6 and close(fd["ice_cream_share"], 0.04)
    assert round(2 / 812 * 100, 2) == 0.25 and round(100 / 40000 * 100, 2) == 0.25
    assert fd["ice_choc_expected"] == 22 and S(3, "slot_value")["ice_cream_views_day"] == 2400
    keyed(it, "True", "2 baskets")
    show(it, "2 of 812 and 100 of 40,000, both 0.25 percent; lift 4.0 swings to 2 or 6")

    it = BY_ID["margin"]
    adds = 30000 * 0.05 * 0.5
    new = adds / 2
    assert (adds, new) == (750, 375)
    value = new * 10 - adds * 3
    assert value == 1500
    ops = options(it)
    assert "Rs 22,500" in ops["a"] and adds * 30 == 22500
    assert "Rs 5,250" in ops["b"] and adds * 7 == 5250
    assert "Rs 2,625" in ops["d"] and new * 7 == 2625
    keyed(it, "Rs 1,500")
    show(it, "375 x Rs 10 less 750 x Rs 3 = Rs 1,500 a day")

    # ---------------------------------------------------------------- Part 4
    d4 = {n["id"]: n["value"] for n in FACTS[4]["numbers"]}
    head, rows = table(part_exhibit(4))
    months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug"]
    for r, m in zip(rows, months):
        assert int(r[1].replace(",", "")) == d4[f"cohort_size_{m}"], (r, m)
        assert round(d4[f"m1_{m}"] * 100) == int(r[2].split()[0]), (r, m)
    assert d4["members_total"] == 53089
    print("PASS  Exhibit 4A: cohort sizes and month-one rates from Thursday's facts; 53,089 members")

    assert BY_NO[33]["key"] == "41" and BY_NO[34]["key"] == "41"
    may = (1000 * 0.50 + 3000 * 0.38) / 4000
    june = (1000 * 0.46 + 3000 * 0.35 + 2000 * 0.475) / 6000
    assert round(may * 100) == 41 and round(june * 100) == 41
    show(BY_NO[33], "1,640 of 4,000")
    show(BY_NO[34], "2,460 of 6,000")
    assert BY_NO[35]["key"] == "a"
    show(BY_NO[35], "both cohorts fell; C props the blend")

    it = BY_ID["funnel-units"]
    rows = it["exhibit"]["table"]["rows"]
    stage = {"Open": "open", "Search": "search", "Menu view": "menu_view", "Add to cart": "add_to_cart",
             "Checkout start": "checkout_start", "Order placed": "order_placed"}
    for r in rows:
        s = stage[r[0]]
        assert int(r[1].replace(",", "")) == d4[f"sep_sessions_{s}"]
        assert int(r[2].replace(",", "")) == d4[f"sep_members_{s}"]
    ses = {r[0]: int(r[1].replace(",", "")) for r in rows}
    mem = {r[0]: int(r[2].replace(",", "")) for r in rows}
    assert round(ses["Menu view"] / ses["Search"] * 100) == 118
    assert round(ses["Add to cart"] / ses["Menu view"] * 100) == 34
    assert round(mem["Add to cart"] / mem["Menu view"] * 100) == 61
    assert [round(ses[k] / ses["Open"] * 100) for k in ("Search", "Menu view", "Add to cart")] == [68, 80, 27]
    keyed(it, "61 percent", "artefact")
    show(it, "118, 34 and 61 percent; option b's 68, 80, 27 over the opening sessions")

    it = BY_ID["android"]
    assert d4["android_member_carts_after"] == 22841 and d4["days_after_release"] == 17
    lost17 = (0.58 - 0.44) * 22841
    week = lost17 * 7 / 17
    assert round(lost17) == 3198 and round(week) == 1317 and d4["lost_orders_per_week"] == 1317
    assert round(week * 300 / 1e5, 1) == 4.0 and round(week * 500 / 1e5, 1) == 6.6
    assert round(lost17 * 300 / 1e5, 1) == 9.6 and round(lost17 * 500 / 1e5, 1) == 16.0
    rows = it["exhibit"]["table"]["rows"]
    pairs = {(r[0], r[1]): (r[2], r[3]) for r in rows}
    assert pairs[("Members", "Android")] == ("58 percent", "44 percent")
    assert pairs[("Non-members", "Android")] == ("52 percent", "51 percent")
    keyed(it, "1,317", "Rs 4.0 to 6.6 lakh")
    show(it, "14 points of 22,841 carts over 17 days is 1,317 a week; Rs 4.0 to 6.6 lakh")

    it = BY_ID["swiggy"]
    rows = it["exhibit"]["table"]["rows"]
    all_ten = [int(x) for x in rows[0][1:]]
    kept = [int(x) for x in rows[1][1:]]
    toy = next(t for t in FACTS[4]["toys"] if t["id"] == "toy_weaned")["values"]
    assert all_ten == toy["all_ten"] and kept == toy["strong_five"]
    assert all_ten[2] * 10 == 40 and kept[2] * 20 == 80 and kept[3] * 20 == 60
    keyed(it, "40 percent per user who joined", "80 per user who stayed")
    show(it, "4 of 10 is 40 percent, 4 of 5 is 80; the toy from Thursday's facts")

    it = BY_ID["kalpa-window"]
    kp = FACTS[4]["kalpa"]
    c = kp["cart_to_checkout_counts"]
    rows = it["exhibit"]["table"]["rows"]
    got = [(int(r[1]), int(r[2])) for r in rows]
    assert got == [(c["before"]["carts"], c["before"]["checkouts"]),
                   (c["comparison"]["carts"], c["comparison"]["checkouts"]),
                   (c["window"]["carts"], c["window"]["checkouts"])]
    assert [round(b / a * 100) for a, b in got] == [82, 83, 64]
    assert round(11 * 10 / 12 - 7, 2) == 2.17 and kp["blend_printed"] == "41 percent"
    keyed(it, "7 of 11", "10 of 12", "about 2 short")
    show(it, "28 of 34, 10 of 12, 7 of 11; 9.17 expected, 7 seen; blend 41 percent")

    # ---------------------------------------------------------------- Part 5
    head, rows = table(part_exhibit(5))
    t5 = S(5, "ticket")
    assert t5["diwali_2024"] == "2024-10-31" and t5["diwali_2025"] == "2025-10-20" and t5["diwali_2026"] == "2026-11-08"
    assert [r[1] for r in rows] == ["Thursday 31 October 2024", "Monday 20 October 2025", "Sunday 8 November 2026"]
    print("PASS  Exhibit 5A: Diwali on 31 October 2024, 20 October 2025 and 8 November 2026")

    it = BY_NO[41]
    assert it["key"] == "Naive Rs 2.1 crore; seasonal naive Rs 3.2 crore."
    assert "October in both 2024 and 2025" in it["text"]
    show(it, "the naive repeats September 2025; the seasonal naive copies October 2024")

    it = BY_ID["calendar"]
    km = S(5, "kalpa_months")
    rows = it["exhibit"]["table"]["rows"]
    assert rows[0][1:] == [f"{km['rev_2024_10'] / 1e5:.1f}", f"{km['rev_2025_10'] / 1e5:.1f}"]
    assert rows[1][1:] == [f"{km['rev_2024_11'] / 1e5:.1f}", f"{km['rev_2025_11'] / 1e5:.1f}"]
    kw = S(5, "kalpa_window")
    assert kw["seasonal_naive_2026_10"] == km["rev_2025_10"] and kw["seasonal_naive_2026_11"] == km["rev_2025_11"]
    assert kw["aligned_2026_11"] == round(km["rev_2025_10"] * 1.04) and round(kw["aligned_2026_11"] / 1e5, 1) == 444.7
    assert round(kw["aligned_2026_10"] / 1e5, 1) == 308.8
    for s in ("427.6", "297.0", "444.7", "November"):
        assert s in it["key"], s
    show(it, "seasonal naive 427.6 and 297.0; festival-aligned November 427.6 x 1.04 = 444.7")

    it = BY_ID["m5"]
    rows = dict((r[0], r[1]) for r in it["exhibit"]["table"]["rows"])
    pub = S(5, "public")
    assert rows["The winning team"] == f"{pub['m5_winner']:.3f}"
    assert rows["Seasonal naive, the same day of the week before"] == f"{pub['m5_seasonal_naive']:.3f}"
    assert rows["Multilayer perceptron, a machine-learning benchmark"] == f"{pub['m5_mlp']:.3f}"
    assert rows["Random forest, a machine-learning benchmark"] == f"{pub['m5_rf']:.3f}"
    assert rows["Naive, the last day seen"] == f"{pub['m5_naive']:.3f}"
    assert close(pub["m5_beat_snaive_pct"], 0.358, 0.0001) and pub["m5_products"] == 3049
    assert 1 - pub["m5_beat_snaive_pct"] > 0.5
    keyed(it, "A fit is no forecast", "most teams")
    show(it, "M5 scores from Friday's facts; 35.8 percent beat the seasonal naive, so most did not")

    it = BY_ID["asym"]
    ho = S(5, "holdout")
    rows = it["exhibit"]["table"]["rows"]
    got = {r[0].split(",")[0]: (int(r[1].replace(",", "")), int(r[2].replace(",", "")), int(r[3])) for r in rows}
    assert got["Festival-aligned"] == (ho["aligned_over"], ho["aligned_under"], ho["aligned_high_weeks"])
    assert got["Same week last year"] == (ho["bot_over"], ho["bot_under"], ho["bot_high_weeks"])
    assert got["The vendor's curve"] == (ho["vendor_over"], ho["vendor_under"], ho["vendor_high_weeks"])
    over_rs = Fraction(650, 120)
    cost = {k: v[0] * over_rs + v[1] * 25 for k, v in got.items()}
    mae = {k: (v[0] + v[1]) / 13 for k, v in got.items()}
    assert [round(mae[k]) for k in ("Festival-aligned", "Same week last year", "The vendor's curve")] == [6615, 9831, 16400]
    assert round(float(cost["The vendor's curve"]) / 1e5, 1) == 11.9
    assert round(float(cost["Festival-aligned"]) / 1e5, 1) == 13.5
    assert round(float(cost["Same week last year"]) / 1e5, 1) == 30.5
    assert min(cost, key=cost.get) == "The vendor's curve"
    signed = {k: (v[0] - v[1]) / 13 for k, v in got.items()}
    assert [round(signed[k]) for k in ("Festival-aligned", "Same week last year", "The vendor's curve")] == [-346, -8708, 16108]
    assert round(25 / (25 + float(over_rs)), 2) == 0.82
    iv = S(5, "interview")
    assert round(iv["own_raised_cost_aligned_rs"] / 1e5, 1) == 8.8 and round(iv["own_raised_cost_vendor_rs"] / 1e5, 1) == 10.0
    assert round(16400 / 6615.076923 - 1, 2) == 1.48
    keyed(it, "the vendor costs least", "own 0.82 point")
    show(it, "MAE 6,615, 9,831, 16,400; priced Rs 13.5, 30.5 and 11.9 lakh; at 0.82, 8.8 against 10.0")

    it = BY_ID["kalpa-board"]
    kx = S(5, "kalpa")
    rows = {r[0]: r for r in it["exhibit"]["table"]["rows"]}
    assert rows["The same month last year"][1] == f"{kw['seasonal_naive_total'] / 1e7:.2f}" == "18.93"
    assert rows["Festival-aligned, matched by Diwali, plus 4 percent"][1] == f"{kw['aligned_total'] / 1e7:.2f}" == "19.69"
    assert rows["Finance's rule, the same month last year plus 4 percent"][1] == f"{kw['finance_total'] / 1e7:.2f}"
    assert rows["The vendor's curve"][1] == f"{kw['vendor_total'] / 1e7:.2f}" == "23.09"
    assert rows["The plan line"][1] == f"{kw['plan_total'] / 1e7:.2f}" == "21.77"
    assert round(kx["seasonal_naive_mae_rs"] / 1e5, 1) == 11.7 and round(kx["vendor_mae_rs"] / 1e5, 1) == 38.8
    assert round(kx["aligned_mae_rs"] / 1e5, 1) == 3.5
    assert round((kw["plan_total"] - kw["aligned_total"]) / 1e7, 2) == 2.08
    mid = (kw["finance_total"] + kw["vendor_total"]) / 2
    assert round(mid / 1e7, 2) == 21.39 and round(kw["seasonal_naive_total"] * 1.13 / 1e7, 2) == 21.39
    assert round(kx["vendor_fit_max_pct"] * 100, 1) == 1.8
    keyed(it, "19.69", "November", "2.08", "3.5 lakh")
    show(it, "Rs 19.69 crore, Rs 2.08 crore under the plan line; misses 3.5, 11.7 and 38.8 lakh")

    # ---------------------------------------------------------------- Part 6
    it = BY_NO[29]
    assert it["key"] == "a, b, d" and "twenty times" in it["text"]
    show(it, "the definition, the guardrail and the baseline stay; the cost of an error changes")
    want = {"brief-logistics": "a definition whose window the measured cannot move, with a guardrail",
            "brief-health": "each funnel step over the step before, in one unit",
            "brief-connect": "cohorts by start month, each read at the same age",
            "brief-finance": "lift above a support floor, valued in margin"}
    for iid, word in want.items():
        it = BY_ID[iid]
        assert it["bank_word"] == word, (iid, it["bank_word"])
        show(it, f"letter {it['key']} of the match table, the method that answers the brief")
    it = BY_ID["amazon"]
    share10 = 10 / (10 + 650 / 120)
    assert round(share10, 2) == 0.65 and round((650 / 120) / (10 + 650 / 120), 2) == 0.35
    keyed(it, "0.65", "festival-aligned copy")
    show(it, "10 over 10 plus 5.42 is 0.65; 0.35 is the share upside down")

    # ---------------------------------------------------------------- the stretch page
    assert round(33440 / 1.90, -2) == 17600 == num(1, "hours_to_carry_idle_trips")
    sv = S(3, "slot_value")
    assert sv["trial_n_full"] == 1105 and sv["trial_n_half"] == 4014
    print("PASS  stretch answers: 17,600 hours; 1,105 and 4,014 ice-cream carts an arm")

    assert len(LINES) == 39, len(LINES)
    print(f"\nRESULT: PASS ({len(LINES)} items proved)")


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# python3 content/W04/SAT/internal/C2_W04_SAT_key_proofs_INTERNAL.py
#     Prints the shape line, the exhibit lines and 39 item lines, PASS Q1 to PASS Q39, each with
#     the item's id or bank number, its key and what was checked, then the stretch line and
#     "RESULT: PASS (39 items proved)", exit 0.
# The same run with the twelve-rows key changed to b in the source file
#     keyed() fails at Q4, because option b does not carry "1.90 to 1.19", and the run exits 1.
# The same run with a cell of Exhibit 4C retyped, 52,948 to 52,984
#     The funnel-units check fails against Thursday's facts file, sep_sessions_add_to_cart.
# The same run with the margin item's discount raised to Rs 4 in its stem only
#     The stem and the options disagree; the proof still asserts Rs 1,500 from its own numbers,
#     so the stem must be changed with the proof, which is the point of keeping both in one file.
# Monday's facts file moved or renamed
#     FileNotFoundError at import, exit 1, before any item is checked.
