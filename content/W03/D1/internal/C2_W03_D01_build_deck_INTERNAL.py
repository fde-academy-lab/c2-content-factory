"""Build the Build 1 introduction deck without printing its sync markers on the slides.

    python3 content/W03/D1/internal/C2_W03_D01_build_deck_INTERNAL.py

The deck's markdown carries the three Build 1 rubrics inside <!-- sync:rubric:W03/... --> blocks, so
that scripts/sync_programme.py rewrites them whenever data/programme/facts.yaml changes. The shared
builder, scripts/build_deck.py, prints an HTML comment line as slide text, so this script copies the
markdown to a scratch file with every whole-line HTML comment removed, and builds the pptx from that
copy into slides/ with --out. The markdown stays the authoritative deck; only the marker lines differ.
"""
import pathlib
import re
import subprocess
import sys
import tempfile

DAY = pathlib.Path(__file__).resolve().parent.parent
ROOT = DAY.parent.parent.parent
SOURCE = DAY / "slides" / "C2_W03_D01_introduction_STUDENT.md"
OUT = SOURCE.with_suffix(".pptx")
FOOTER = "Week 3 Day 1: Build 1 opens in Kalpa Health"
COMMENT_LINE = re.compile(r"^\s*<!--.*-->\s*$")


def stripped(text):
    """The markdown with every line that is only an HTML comment taken out."""
    return "\n".join(line for line in text.splitlines() if not COMMENT_LINE.match(line)) + "\n"


def main():
    text = SOURCE.read_text(encoding="utf-8")
    clean = stripped(text)
    removed = len(text.splitlines()) - len(clean.splitlines())
    with tempfile.TemporaryDirectory() as tmp:
        copy = pathlib.Path(tmp) / SOURCE.name
        copy.write_text(clean, encoding="utf-8")
        run = subprocess.run([sys.executable, str(ROOT / "scripts" / "build_deck.py"), str(copy),
                              "--footer", FOOTER, "--out", str(OUT)], cwd=ROOT)
    print(f"removed {removed} marker lines; wrote {OUT.relative_to(ROOT)}")
    return run.returncode


if __name__ == "__main__":
    sys.exit(main())

# Test inputs and expected outcomes
# --------------------------------
# python3 content/W03/D1/internal/C2_W03_D01_build_deck_INTERNAL.py
#     Prints the builder's slide count, then "removed 6 marker lines" while the deck carries the
#     three rubric blocks, and writes slides/C2_W03_D01_introduction_STUDENT.pptx; no slide shows
#     "<!--" when the pptx is rendered.
# The same command after a fourth sync block is added to the markdown
#     "removed 8 marker lines", and the new block's rubric text prints on its slide as before.
# stripped("a\n<!-- sync:x -->\nb\n")
#     Returns "a\nb\n": a comment line goes, every other line stays as it was.
