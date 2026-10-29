"""Write the demo data block for the kit's stress page, scripts/companion/demo/w5kit_demo_INTERNAL.html.

Everything here is demo data drawn from a seeded generator, so the page shows the same numbers on
every run and on every machine, and no real client, bank or member is in it. A day page never uses
this file: its numbers come from the day's own explorer_data script and the public data.

Usage:
    python3 scripts/companion/demo/make_w5kit_demo_data_INTERNAL.py
    python3 scripts/build_companion.py scripts/companion/demo/w5kit_demo_INTERNAL.html
"""
import json
import math
import pathlib
import random

OUT = pathlib.Path(__file__).resolve().parent / "w5kit_demo_data_INTERNAL.json"


def sigmoid(z):
    return 1 / (1 + math.exp(-z))


def main():
    rng = random.Random(20261029)
    n, pos = 8238, 928
    labels = [1] * pos + [0] * (n - pos)
    rng.shuffle(labels)
    scores = []
    for y in labels:
        z = rng.gauss(-0.75, 1.25) if y else rng.gauss(-2.45, 0.95)
        scores.append(int(round(sigmoid(z) * 1000)))
    called = sum(1 for s in scores if s >= 500)
    found = sum(1 for s, y in zip(scores, labels) if s >= 500 and y)

    # Fifty rows of one invented feature for the five-fold scene: days since the last order, and
    # whether the member came back. Returners sit lower on the axis, with overlap.
    fold_x, fold_y = [], []
    for i in range(50):
        y = 1 if rng.random() < 0.4 else 0
        x = max(1, round(rng.gauss(18 if y else 41, 11)))
        fold_x.append(x)
        fold_y.append(y)

    # Twenty-four invented points for the line page: a curved truth with noise, eight held out.
    line_x, line_y = [], []
    for i in range(24):
        x = round(4 + i * 3.6 + rng.uniform(-1.2, 1.2), 1)
        y = round(5200 - 52 * x + 0.32 * x * x + rng.gauss(0, 420))
        line_x.append(x)
        line_y.append(y)
    held = sorted(rng.sample(range(24), 8))

    data = {
        "label": "Demo data from a seeded generator; no real client, bank or member is in it.",
        "clients": {"n": n, "pos": pos, "score": scores, "y": "".join(str(y) for y in labels)},
        "headline": {"threshold": 0.5, "called": called, "found": found},
        "folds": {"x": fold_x, "y": fold_y},
        "pairs": {"pos": [0.82, 0.71, 0.55, 0.38], "neg": [0.64, 0.49, 0.44, 0.40, 0.33, 0.29, 0.22, 0.18, 0.12, 0.05]},
        "line": {"x": line_x, "y": line_y, "held": held},
    }
    OUT.write_text(json.dumps(data, separators=(",", ":")), encoding="utf-8")
    print(f"wrote {OUT.name}: {n} clients, {pos} buyers, {called} called at 0.5, {found} buyers found")


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# python3 scripts/companion/demo/make_w5kit_demo_data_INTERNAL.py
#     Writes w5kit_demo_data_INTERNAL.json beside this file and prints the counts; a second run
#     writes the same bytes, because the generator is seeded.
