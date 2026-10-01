"""Run scripts/distractor_audit.py on the question slides of this Saturday's decks.

    python3 content/W03/SAT/internal/C2_W03_SAT_deck_options_audit_INTERNAL.py

The audit reads option sets only in exercise folders, and a build week's Saturday has none, so a deck's
question slides would otherwise go unaudited. This copies each deck in slides/ into a scratch folder,
reads the key of every question slide from the answer slide after it ("Answer: b, ..."), writes those
keys beside the copy as an Answers line, and runs the audit on the copy. The deck itself is unchanged,
and the keys come from the deck, so a key moved on a slide moves here too.
"""
import pathlib
import re
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SLIDES = HERE.parent / "slides"
AUDIT = ROOT / "scripts" / "distractor_audit.py"
HEADING = re.compile(r"^## (?:[SD]\d+[a-z]?\.\s*)?(.+)$", re.M)


def keys(text):
    """The key of each question slide, in order, read from the answer slide that follows it."""
    titles = HEADING.findall(text)
    found = []
    for i, title in enumerate(titles[:-1]):
        if title.lower().startswith("question"):
            m = re.match(r"answer:\s*([a-f])\b", titles[i + 1], re.I)
            if not m:
                raise SystemExit(f"FAIL  the question slide '{title}' has no 'Answer: x' slide after it")
            found.append(m.group(1).lower())
    return found


def main():
    worst = 0
    for deck in sorted(SLIDES.glob("*_STUDENT.md")):
        answers = keys(deck.read_text(encoding="utf-8"))
        if not answers:
            print(f"INFO  {deck.name}: no question slides, so nothing to audit")
            continue
        scratch = pathlib.Path(tempfile.mkdtemp(prefix="c2_deck_audit_"))
        copy = scratch / deck.name
        copy.write_text(deck.read_text(encoding="utf-8"), encoding="utf-8")
        key_file = scratch / deck.name.replace("_STUDENT.md", "_solution_STUDENT.md")
        key_file.write_text("Answers: " + " ".join(f"{n}{k}" for n, k in enumerate(answers, 1)) + "\n",
                            encoding="utf-8")
        print(f"      {deck.name}: keys read from its answer slides, {' '.join(answers)}")
        done = subprocess.run([sys.executable, str(AUDIT), str(copy)], capture_output=True, text=True)
        print(done.stdout.rstrip())
        worst = max(worst, done.returncode)
    sys.exit(worst)


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes.
# 1. As shipped: the presentation format deck's four question slides are keyed b, a, d and c from
#    their answer slides, and the audit prints "RESULT: PASS (0 failures)"; a deck with no question
#    slide prints INFO and is skipped. Exit code 0.
# 2. A question slide whose next slide does not begin "Answer:": "FAIL" naming the slide, exit 1.
# 3. A key that is the lone longest option: the audit's own FAIL line naming the item, exit 1.
