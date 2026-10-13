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
    assert hard == 13 and mins <= 119, (hard, mins)
    # The levels after the raise of 13 October 2026 and its blind sitting: of the seven items rebuilt with a
    # second idea on their own exhibit, the sitting read Q8, Q10 and Q14 as hard and Q6, Q12, Q31 and Q33 as
    # medium, and it read Q39, hard since the earlier build, as medium too; a label moves only with the read,
    # so those five are Medium. The provenance's levels row carries the rule and the read of each.
    assert sorted(i["q"] for i in PRINTED if i["level"] == "Hard") == [4, 7, 8, 9, 10, 14, 15, 20, 21, 25, 26,
                                                                     30, 32]
    assert [i["q"] for i in PRINTED if i["level"] == "Easy"] == [1, 3, 5, 11, 29, 35, 36, 37, 38]
    print(f"PASS  shape: 39 items, {hard} hard ({hard / 39:.0%}), {mins:g} minutes at the blueprint's pace")

    # ---------------------------------------------------------------- words elsewhere name no answer
    # The second fix pass took out every line the blind second read of 13 October 2026 found naming a
    # key, and the lines this pass found doing the same; none may come back.
    paper = (ROOT / "content/W04/SAT/paper/C2_W04_SAT_recap_paper_STUDENT.md").read_text(encoding="utf-8")
    for leak in ("a check in the right unit", "a baseline that beats the fit", "Ask for the denominator",
                 "so it now appears beside nearly everything", "41 percent", "Puts the spike in",
                 "The redesign pays per completed peak trip", "Allow for heavy buyers", "Move the spike",
                 "states no denominator", "planned toward the costlier side", "Design the test",
                 "raises festival-aligned by", "well above the single weeks", "which it never saw. Diwali",
                 "defend it without retreating", "the cost of an error that changed",
                 "The fall in bookings per hour is the monsoon's end", "Size the silent change",
                 # and the lines the blind check of the same day named
                 "kept beside the definition", "which falls when", "which move before",
                 "which tells the team early", "numerator, denominator and window", "whose window",
                 "valued in margin", "letter of the week's method", "support floor of 1 percent", "above the floor",
                 "carousel", "35.8 percent, beat the seasonal naive", "none was built from", "were scored on",
                 "0.82", "over both costs", "6.25", "9.45", "on each base", "whose other items click least",
                 # and the lines the raise of 13 October 2026 took out: Q39 named Lucknow's held-back weeks
                 # as the latest, which is Q31's half; Stretch 1 gave the other drivers' 1.90, which picks
                 # Q12's check; Exhibit 5D's dates placed the hidden weeks last, which is Q31's half too
                 "held-out latest weeks", "other drivers' 1.90", "beginning 29 June to 21 September",
                 # and the lines the blind sitting of the same day named: Exhibit 5E printed "not a forecast"
                 # against the plan line, which answers Q33's third question, and Exhibit 5D priced the spare
                 # shipment, a step Q32 and Q39 ask for
                 "not a forecast", "Rs 5.42", "planned and not shipped"):
        assert leak not in paper, ("a line names an answer again", leak)
    print("PASS  no part opening, caption, label, spare or stretch line names a timed item's answer")

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
    ops = options(it)
    assert "1.31" in ops["a"] and "1.31" in ops["d"] and "1.19" in ops["c"]
    assert round((1.90 - 1.19) / 1.90 * 100) == 37 and "37 percent" in ops["c"]
    assert round((1.90 - 1.31) / 1.90 * 100) == 31 and "31 percent" in ops["a"]
    assert close(num(1, "tph_after"), 1.58) and "1.58" in ops["d"]
    keyed(it, "1.90 to 1.19", "1.58", "E and F")
    show(it, "60 to 74 hours, 114 to 88 trips, 1.19 against the city's 1.58; 1.31 and 37 percent refused")

    it = BY_ID["tf-target"]
    keyed(it, "True", "nobody asked for")
    show(it, "the SEC order's staff behaviour; checked 13 October 2026 (sources list)")

    it = BY_ID["wells-silent"]
    share = Fraction(4, 100) / Fraction(11, 100)
    assert round(float(share) * 100) == 36
    ex1c = {r[0]: r[1] for r in BY_ID["tf-target"]["exhibit"]["table"]["rows"]}
    # Exhibit 1C's 2013 row carries both causes of the rise in the SEC order's words (paragraph 42).
    assert "0.04 of that year's 0.11 rise" in ex1c["The 2013 change"]
    assert "inactive for at least 365 days" in ex1c["The 2013 change"] and "up to four years" in ex1c["Use"]
    assert it["key"] == "c"
    keyed(it, "dated log", "unused for a year")
    ops = options(it)
    # Both exclusion halves are read off the 2013 row: dropping the remittance accounts takes out the 0.04
    # the stem asks to show, and leaves the inactive rest in.
    assert "dated log" in ops["d"] and "remittance accounts added to the count that year" in ops["d"]
    assert "revenue per household" in ops["a"] and "unused for a year" in ops["a"]
    assert "revenue per household" in ops["b"] and "remittance accounts added to the count that year" in ops["b"]
    assert "Remittance accounts" in ex1c["The 2013 change"] and "closed" not in " ".join(ops.values())
    assert "additions to the ratio's written definition" in it["text"]
    show(it, "the change log shows the 0.04, 36 percent; an exclusion on use keeps the inactive rest out")

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
    # Lines b, d and e name their element without saying what a leading input or a guardrail does,
    # which Q1 and Q3 ask.
    assert "early" not in ops["b"] and "falls" not in ops["d"] and "before" not in ops["e"]
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
    assert it["key"] == "e, b, d, f"
    ops = options(it)
    assert len(ops) == 7 and sorted(ops) == list("abcdefg")
    # The lines carry no slot label, so each slot is a choice the reader makes.
    assert not any(o.lower().startswith(("the claim", "the evidence", "the caveat", "the action")) for o in ops.values())
    assert "Rs 314 to Rs 260" in ops["b"] and "Rs 314 to Rs 260" in ops["g"]
    assert "half the drivers, picked at random" in ops["f"]
    stem = " ".join(bsp.parts(it)[0])
    for slot in ("the claim, written as the title", "the evidence", "the caveat", "the action"):
        assert slot in stem, ("the stem prints the template's four slots", slot)
    fall = 314 - 260
    assert round(fall / 314 * 100) == 17 and "17 percent" in ops["b"]        # measured from where it started
    assert round(fall / 260 * 100) == 21 and "21 percent" in ops["g"]        # the wrong base
    assert round((num(1, "rs_per_hour_before") - num(1, "rs_per_hour_after")) / num(1, "rs_per_hour_before") * 100) == 17
    assert round((num(1, "rs_per_driver_week_after") / num(1, "rs_per_driver_week_before") - 1) * 100, 1) == 0.8
    assert "0.8 percent" in ops["c"]
    show(it, "per-hour claim; Rs 54 of Rs 314 is 17 percent, 21 on the wrong base; the test as the action")

    it = BY_ID["keep-two"]
    d2 = {n["id"]: n["value"] for n in FACTS[2]["numbers"]}
    assert d2["topup_per_extra_trip_rs"] == 2836
    assert round(19_000_000 / (230_900 - 224_200)) == 2836
    assert it["key"] == "a, c" and "4.8 to 4.6" in options(it)["a"] and "2,836" in options(it)["c"]
    assert "251,910 to 256,556" in options(it)["b"]
    assert round(19_000_000 / num(1, "trips_after")) == 82 and "Rs 82" in options(it)["d"]
    show(it, "the wait and Rs 2,836 an extra trip; Rs 82 a completed trip and the requests refused")

    it = BY_ID["concede"]
    assert it["key"] == "c"
    keyed(it, "False", "last three weeks", "1.56")
    ops = options(it)
    assert "1.8 percent over the six weeks" in ops["a"] and "1.8 percent over the six weeks" in ops["d"]
    assert "last three weeks" in ops["b"] and "rains ended inside the window" in ops["d"]
    rows = it["exhibit"]["table"]["rows"]
    weeks = ["2026_07_20", "2026_07_27", "2026_08_03", "2026_08_10", "2026_08_17", "2026_08_24",
             "2026_08_31", "2026_09_07", "2026_09_14", "2026_09_21", "2026_09_28", "2026_10_05"]
    req = [int(r[2].replace(",", "")) for r in rows]
    tph = [float(r[3]) for r in rows]
    for w, r, h, row in zip(weeks, req, tph, rows):
        assert r == num(1, f"requests_{w}") and close(h, num(1, f"tph_{w}")), (w, row)
        assert row[1] == ("before" if w < "2026_08_31" else "after"), (w, row)
    before, after = req[:6], req[6:]
    assert sum(before) == num(1, "requests_before") and sum(after) == num(1, "requests_after")
    assert round((sum(after) / sum(before) - 1) * 100, 1) == 1.8
    assert min(after[:3]) > max(before)                                      # the first three, above every week before
    assert after.index(max(after)) == 1 and all(a > b for a, b in zip(after[1:], after[2:]))  # four falls from 7 September
    assert (min(after[3:]), max(after[3:]), min(before), max(before)) == (41161, 42602, 41155, 42719)
    assert min(before) <= min(after[3:]) and max(after[3:]) <= max(before)   # the last three, inside the old range
    last3 = sum(num(1, f"trips_{w}") for w in weeks[9:]) / sum(num(1, f"hours_{w}") for w in weeks[9:])
    assert close(last3, 1.56) and close(d2["tph_last_three_after"], 1.56)
    show(it, "six-week rise 1.8 percent from the first three weeks; the last three inside the old range at 1.56")

    it = BY_ID["memo"]
    keyed(it, "False", "one slide", "a week")
    show(it, "the ask is one slide; Amazon's letter, a week or more")

    it = BY_ID["estimate-order"]
    assert it["key"] == "b, d, e, a"
    trips_hour = 1e7 * 0.01 * 0.25 / 3
    per_driver = 2.4 * (1 - 0.30)
    assert round(trips_hour) == 8333 and round(per_driver, 2) == 1.68
    assert round(trips_hour / per_driver, -1) == 4960 and round(trips_hour / per_driver * 1.15, -2) == 5700
    assert d2["drivers_at_peak_central"] == 5704
    ops = options(it)

    def rerun(rate):
        """The chain re-run at one of Exhibit 1A's rates, with the same 15 percent buffer."""
        return trips_hour / rate * 1.15
    # Before the launch in trips (the key), before the launch in requests (the wrong unit), and after the
    # launch in trips (the weeks the guarantee filled with idle hours).
    assert round(rerun(num(1, "tph_before")), -2) == 5000 == d2["drivers_at_case_tph"]
    assert "1.90" in ops["a"] and "5,000" in ops["a"]
    assert round(rerun(num(1, "requests_per_hour_before")), -2) == 4500 and "2.13" in ops["c"] and "4,500" in ops["c"]
    assert round(rerun(num(1, "tph_after")), -2) == 6100 and "1.58" in ops["f"] and "6,100" in ops["f"]
    assert num(1, "requests_before") > num(1, "trips_before")
    assert num(1, "median_wait_before") < 5 and round(num(1, "median_wait_before") - num(1, "median_wait_after"), 1) == 0.2
    assert "1.19" not in it["text"], "Q12 prints no six-driver rate, which is Q4's"
    show(it, "chain 5,700; at 1.90 it is 5,000; 2.13 requests gives 4,500 and 1.58 after the launch 6,100")

    it = BY_ID["four-checks"]
    assert it["key"] == "a, c"
    stem = " ".join(bsp.parts(it)[0])
    assert "6.3 million concurrent users in a minute" in stem and "802 million daily" in stem
    assert "63 million" in options(it)["b"] and 2_000_000 / 4 == 500_000 and "5 lakh" in options(it)["d"]
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
    assert rows[2][0] == "How a journey is counted" and "each line" in rows[2][1]
    assert "highest-ever day" in rows[1][2]
    # The 2018 row, from Tuesday's facts: one day's line uses against commuters a day.
    uses, riders = num(2, "dmrc_line_utilisation_2018"), num(2, "dmrc_ridership_2018")
    assert "45,35,932" in rows[3][1] and "27 lakh" in rows[3][1] and (uses, riders) == (4535932, 2700000)
    mix = uses / riders
    assert round(mix, 2) == 1.68
    avg_trips, record_trips = 64.06 / mix, 82.44903 / mix
    assert round(avg_trips) == 38 and round(record_trips) == 49
    assert round((60 / avg_trips - 1) * 100) == 57 and round((60 / record_trips - 1) * 100) == 22
    assert round(64.06 / 60, 2) == 1.07                    # any mix above this puts the average day under 60 lakh
    assert it["key"] == "b"
    keyed(it, "average day", "38 lakh trips", "57 percent high")
    ops = options(it)
    assert "49 lakh" in ops["a"] and "6 percent low" in ops["c"] and "27 percent low" in ops["d"]
    # Raised to the average day, 60 lakh moves 6.8 percent, so option c names the figure it moves to.
    assert round((64.06 / 60 - 1) * 100, 1) == 6.8 and "raised to about 64 lakh" in ops["c"]
    show(it, "45,35,932 over 27 lakh is 1.68 a rider; 64.06 lakh is 38 lakh trips, the chain 57 percent high")

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
    keyed(it, "slot 1", "70 percent", "Neither milk nor other items")
    assert "slot 3" in options(it)["c"] and "Neither milk" in options(it)["c"] and "slot 1" in options(it)["a"]
    # The slot-3 options pick the slot where milk's rate is lowest, which the rows confirm, and lose on
    # clicks lost, share times gap.
    milk = [pct(r[2]) for r in rows[:3]]
    assert milk.index(min(milk)) == 2 and "0.9 percent" in options(it)["c"] and "0.9 percent" in options(it)["d"]
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
    assert "support floor" not in it["text"] and "1.70 per cart" in options(it)["d"]
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
    assert fd["ice_choc_expected"] == 22
    keyed(it, "True", "2 baskets", "no test shows the suggestion sells more")
    assert "0.25 percent" in options(it)["b"] and options(it)["b"].startswith("True")
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
    it = BY_NO[35]
    assert it["key"] == "a"
    without_c = (1000 * 0.46 + 3000 * 0.35) / 4000
    unweighted = (46 + 35) / 2
    assert round(without_c * 100, 1) == 37.8 and unweighted == 40.5
    ops = options(it)
    assert "37.8" in ops["a"] and "40.5" in ops["b"] and "37.8" in ops["c"] and "40.5" in ops["d"]
    assert "41" not in " ".join(ops.values())
    show(it, "both cohorts fell; without C June reads 1,510 of 4,000, 37.8; 40.5 unweighted")

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
    keyed(it, "61 percent", "a step members can skip", "from Open straight to a menu")
    assert "carousel" not in it["exhibit"]["caption"] and "carousel" not in part_exhibit(4)["caption"]
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
    keyed(it, "member path", "1,317", "Rs 4.0 to 6.6 lakh")
    ops = options(it)
    assert "3,198" in ops["a"] and "1,317" in ops["c"] and "August sale cohort" in ops["c"] and "3,198" in ops["d"]
    show(it, "14 points of 22,841 carts over 17 days is 1,317 a week; Rs 4.0 to 6.6 lakh")

    it = BY_ID["swiggy"]
    rows = it["exhibit"]["table"]["rows"]
    all_ten = [int(x) for x in rows[0][1:]]
    kept = [int(x) for x in rows[1][1:]]
    toy = next(t for t in FACTS[4]["toys"] if t["id"] == "toy_weaned")["values"]
    assert all_ten == toy["all_ten"] and kept == toy["strong_five"]
    assert all_ten[2] * 10 == 40 and kept[2] * 20 == 80 and kept[3] * 20 == 60
    keyed(it, "40 percent of the users who joined and 80 percent of those kept", "divides by")
    assert "60 percent" in options(it)["c"] and "divides by" in options(it)["c"]
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
    keyed(it, "7 of 11", "10 of 12", "about 2 checkouts short")
    ops = options(it)
    assert 10 - 7 == 3 and "3 fewer" in ops["a"] and round((10 - 7) / 10 * 100) == 30 and "30 percent" in ops["b"]
    assert round(83 - 64) == 19 and "19-point" in ops["c"]
    show(it, "28 of 34, 10 of 12, 7 of 11; 9.17 expected, 7 seen; the flat blend printed without its number")

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
    assert round(kw["aligned_2026_10"] / 1e5, 1) == 308.8 and round(297.0 * 1.04, 1) == 308.9
    for s in ("427.6", "297.0", "444.7", "308.9", "November"):
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
    assert 1 - pub["m5_beat_snaive_pct"] > 0.5 and round(1972 / 5507, 3) == 0.358
    # The caption no longer names the bar; the key's reason keeps the 35.8 percent with its source.
    m5_why = next(a for a in SOURCE["additions"] if a["id"] == "m5")["why"]
    assert "35.8" not in it["exhibit"]["caption"] and "1,972 of the 5,507 teams, 35.8" in " ".join(m5_why.split())
    assert it["key"] == "a"
    keyed(it, "latest thirteen weeks", "seasonal naive")
    ops = options(it)
    assert "at random" in ops["b"] and "seasonal naive" in ops["b"]
    assert "latest thirteen weeks" in ops["c"] and "seasonal" not in ops["c"]
    assert "at random" in ops["d"] and "seasonal" not in ops["d"]
    # The bar is read off the exhibit: the seasonal naive beat both machine-learning benchmarks, and every
    # other entry beat the naive.
    assert pub["m5_seasonal_naive"] < min(pub["m5_mlp"], pub["m5_rf"])
    assert pub["m5_naive"] > max(pub["m5_winner"], pub["m5_seasonal_naive"], pub["m5_mlp"], pub["m5_rf"])
    # No caption places the hidden weeks last, which would answer the option set's first half.
    assert "29 June" not in BY_ID["asym"]["exhibit"]["caption"]
    show(it, "the latest weeks held back, against the seasonal naive's 0.847, which beat 0.977 and 1.010")

    it = BY_ID["asym"]
    ho = S(5, "holdout")
    rows = it["exhibit"]["table"]["rows"]
    got = {r[0].split(",")[0]: (int(r[1].replace(",", "")), int(r[2].replace(",", "")), int(r[3])) for r in rows}
    assert got["Festival-aligned"] == (ho["aligned_over"], ho["aligned_under"], ho["aligned_high_weeks"])
    assert got["Same week last year"] == (ho["bot_over"], ho["bot_under"], ho["bot_high_weeks"])
    assert got["The vendor's curve"] == (ho["vendor_over"], ho["vendor_under"], ho["vendor_high_weeks"])
    # The caption gives the shift and its size; the cost of one spare shipment is the room's division.
    cap = it["exhibit"]["caption"]
    assert "Rs 650" in cap and "120 shipments" in cap and "Rs 25" in cap and "5.42" not in cap
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
    keyed(it, "6,615, 9,831 and 16,400", "the vendor costs least, about Rs 11.9 lakh", "plan share")
    ops = options(it)
    # Options a and c claim the smallest error also costs least; priced, it does not.
    assert "festival-aligned, with the smallest error, also costs least" in ops["a"]
    assert "festival-aligned, with the smallest error, also costs least" in ops["c"]
    assert min(mae, key=mae.get) == "Festival-aligned" and cost["Festival-aligned"] > cost["The vendor's curve"]
    netted = {k: abs(v[0] - v[1]) / 13 for k, v in got.items()}
    assert [round(netted[k]) for k in ("Festival-aligned", "Same week last year", "The vendor's curve")] == [346, 8708, 16108]
    assert "About 346, 8,708 and 16,108" in ops["b"] and "About 346, 8,708 and 16,108" in ops["c"]
    assert "plan share" in ops["b"] and "0.82" not in " ".join(ops.values())
    show(it, "MAE 6,615, 9,831, 16,400; priced Rs 13.5, 30.5 and 11.9 lakh; at 0.82, 8.8 against 10.0")

    it = BY_ID["kalpa-board"]
    kx = S(5, "kalpa")
    rows = {r[0]: r for r in it["exhibit"]["table"]["rows"]}
    assert rows["The same month last year"][1] == f"{kw['seasonal_naive_total'] / 1e7:.2f}" == "18.93"
    assert rows["Festival-aligned, matched by Diwali, plus 4 percent"][1] == f"{kw['aligned_total'] / 1e7:.2f}" == "19.69"
    assert rows["Finance's rule, the same month last year plus 4 percent"][1] == f"{kw['finance_total'] / 1e7:.2f}"
    assert rows["The vendor's curve"][1] == f"{kw['vendor_total'] / 1e7:.2f}" == "23.09"
    # The plan line is in the stem: a row on Exhibit 5E printed "not a forecast" beside it, which answered
    # Anand's third question for the room.
    assert "The plan line" not in rows
    assert f"Rs {kw['plan_total'] / 1e7:.2f} crore" == "Rs 21.77 crore" and "Rs 21.77 crore" in it["text"]
    assert round(kw["plan_total"] / kw["seasonal_naive_total"] - 1, 2) == 0.15 and "plus 15 percent" in it["text"]
    assert round(kx["seasonal_naive_mae_rs"] / 1e5, 1) == 11.7 and round(kx["vendor_mae_rs"] / 1e5, 1) == 38.8
    assert round(kx["aligned_mae_rs"] / 1e5, 1) == 3.5
    assert round((kw["plan_total"] - kw["aligned_total"]) / 1e7, 2) == 2.08
    mid = (kw["finance_total"] + kw["vendor_total"]) / 2
    assert round(mid / 1e7, 2) == 21.39 and round(kw["seasonal_naive_total"] * 1.13 / 1e7, 2) == 21.39
    assert round(kx["vendor_fit_max_pct"] * 100, 1) == 1.8
    assert it["key"] == "b"
    keyed(it, "19.69", "festival-aligned", "3.5 lakh", "none with a Diwali", "21 lakh", "2.08 crore")
    assert len(it["exhibit"]["table"]["head"]) == 4, "Exhibit 5E prints no spike column"
    assert not "2026-04" <= t5["diwali_2026"][:7] <= "2026-09", "the six unseen months hold no Diwali"
    kex = S(5, "kalpa_exercise")
    bar = kex["bar_six"]
    assert close(bar, 6 * kx["aligned_mae_rs"], 1) and round(bar / 1e5) == 21
    gap = kw["plan_total"] - kw["aligned_total"]
    assert close(gap, kex["gap_to_plan"], 1) and round(gap / 1e7, 2) == 2.08 and round(gap / bar) == 10
    assert round((kw["plan_total"] - mid) / 1e5) == 38 and kw["plan_total"] - mid < 2 * bar
    ops = options(it)
    assert "21.39" in ops["c"] and "21.39" in ops["d"] and "Rs 38 lakh" in ops["c"]
    rng = f"Rs {kw['seasonal_naive_total'] / 1e7:.2f} to {kw['vendor_total'] / 1e7:.2f} crore"
    assert "forecasts' range" in ops["a"] and "forecasts' range" in ops["d"] and rng in ops["a"] and rng in ops["d"]
    # Every option answers all three of Anand's questions and says what the error could not test, so none
    # falls for leaving one out, and the key is not the only option with both of its qualifiers.
    assert all("3.5 lakh a month on six unseen months, none with a Diwali" in o for o in ops.values())
    assert "21 lakh if all six miss one way" in ops["c"] and "not a forecast" not in " ".join(ops.values())
    assert kw["seasonal_naive_total"] < kw["plan_total"] < kw["vendor_total"]
    show(it, "Rs 19.69 crore; 3.5 lakh a month is 21 lakh over six; the Rs 2.08 crore gap is ten times it")

    # ---------------------------------------------------------------- Part 6
    it = BY_NO[29]
    assert it["key"] == "a, b, d" and "twenty times" in it["text"]
    assert options(it)["a"] == "writing the metric's definition down before reading any number"
    show(it, "the definition, the guardrail and the baseline stay; the cost of an error changes")
    want = {"brief-logistics": "a definition the people measured cannot change after the fact",
            "brief-health": "each funnel step over the step before, in one unit",
            "brief-connect": "cohorts by start month, each read at the same age",
            "brief-finance": "lift above a support floor, on enough customers to trust it"}
    for iid, word in want.items():
        it = BY_ID[iid]
        assert it["bank_word"] == word, (iid, it["bank_word"])
        show(it, f"letter {it['key']} of the match table, the method that answers the brief")
    it = BY_ID["amazon"]
    share10 = 10 / (10 + 650 / 120)
    assert round(share10, 2) == 0.65 and round((650 / 120) / (10 + 650 / 120), 2) == 0.35
    keyed(it, "0.65", "festival-aligned copy")
    ops = options(it)
    assert round((650 / 120) / (10 + 650 / 120), 2) == 0.35 and "0.35" in ops["a"] and "0.35" in ops["b"]
    assert "0.82" not in " ".join(ops.values()), "Q39 prints no 0.82, which would read Q32's quantile"
    assert "calendar weeks" in ops["c"] and "0.65" in ops["c"]
    assert "over both costs" not in " ".join(ops.values()), "the share is worked, never printed as a formula"
    assert "latest" not in " ".join(ops.values()), "Q39 names no held-back weeks as the latest, which is Q31's half"
    show(it, "10 over 10 plus 5.42 is 0.65; 0.35, the share upside down, and the calendar copy refused")

    # ---------------------------------------------------------------- the stretch page
    assert round(33440 / 1.90, -2) == 17600 == num(1, "hours_to_carry_idle_trips")
    assert "1.90" not in SOURCE["stretch"][0]["text"], "Stretch 1 gives no rate, which would pick Q12's check"
    sv = S(3, "slot_value")
    assert sv["trial_n_full"] == 1105 and sv["trial_n_half"] == 4014
    # Wednesday's formula, (z for 5 percent two-sided plus z for 80 percent power) squared times the
    # two variances over the squared gap, gives Wednesday's 1,105 and 4,014; Stretch 2 runs it on
    # invented rates, 5 to 8 percent, so it points at no pair on the paper.
    from statistics import NormalDist
    z = NormalDist().inv_cdf(0.975) + NormalDist().inv_cdf(0.8)

    def arm(p1, p2):
        return z * z * (p1 * (1 - p1) + p2 * (1 - p2)) / (p2 - p1) ** 2
    assert round(arm(0.0625, 0.0945)) == 1105 and round(arm(0.0625, 0.0785)) == 4014
    assert round(arm(0.05, 0.08)) == 1056 and round(arm(0.05, 0.065)) == 3777
    assert arm(0.05, 0.065) / arm(0.05, 0.08) > 3
    s2 = SOURCE["stretch"][1]
    assert "5 percent" in s2["text"] and "8 percent" in s2["text"] and "invented" in s2["text"]
    assert "1,056" in s2["answer"] and "3,777" in s2["answer"]
    print("PASS  stretch answers: 17,600 hours; 1,056 and 3,777 carts a half on invented rates")

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
# The same run with the twelve-rows key changed to c in the source file
#     keyed() fails at Q4, because option c does not carry "1.58", and the run exits 1.
# The same run with "41 percent" put back into Exhibit 4F's caption
#     The leak check fails before any item is proved, naming the phrase, and the run exits 1.
# The same run with Q32's option b given back "compare each at its own 0.82 point"
#     The leak check fails on "0.82", since that number would tell a reader the share Q39 asks for.
# The same run with Q13 labelled Hard in the source file
#     The shape check fails: 14 hard items against the 13 the raise and its blind sitting leave.
# The same run with a cell of Exhibit 4C retyped, 52,948 to 52,984
#     The funnel-units check fails against Thursday's facts file, sep_sessions_add_to_cart.
# The same run with the margin item's discount raised to Rs 4 in its stem only
#     The stem and the options disagree; the proof still asserts Rs 1,500 from its own numbers,
#     so the stem must be changed with the proof, which is the point of keeping both in one file.
# Monday's facts file moved or renamed
#     FileNotFoundError at import, exit 1, before any item is checked.
