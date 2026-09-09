#!/usr/bin/env python3
"""Run every mechanical check a training deck must pass before it ships.

Usage:
    python3 qa_deck.py deck.pptx [--render]

Checks, in order:
  1. Schema validation, via the public pptx skill validator when present
  2. Em-dashes and en-dashes in the rendered slide text
  3. Banned filler words
  4. Meta-content on learner-facing slides (speaker notes are exempt)
  5. Slide count against speaker-note count
  6. Edge bleed, when --render is passed and LibreOffice is available

Exit code is 1 if any check fails.
"""
import os
import re
import subprocess
import sys
import zipfile
import xml.etree.ElementTree as ET

A = "http://schemas.openxmlformats.org/drawingml/2006/main"
BANNED = [
    "Additionally", "Moreover", "However", "Hence", "Thus", "Nonetheless",
    "Furthermore", "Accordingly", "Indeed", "Dynamic",
]
VALIDATOR = "/mnt/skills/public/pptx/scripts/office/validate.py"
SOFFICE = "/mnt/skills/public/pptx/scripts/office/soffice.py"


def parts(path, pattern):
    with zipfile.ZipFile(path) as z:
        names = [n for n in z.namelist() if re.match(pattern, n)]
        names.sort(key=lambda n: int(re.search(r"(\d+)", n.split("/")[-1]).group(1)))
        return [(n, z.read(n)) for n in names]


def texts(xml_bytes):
    root = ET.fromstring(xml_bytes)
    return [t.text or "" for t in root.iter("{%s}t" % A)]


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    deck = sys.argv[1]
    render = "--render" in sys.argv
    failures = []

    slides = parts(deck, r"ppt/slides/slide\d+\.xml$")
    notes = parts(deck, r"ppt/notesSlides/notesSlide\d+\.xml$")
    slide_text = []
    for i, (_, b) in enumerate(slides, 1):
        for t in texts(b):
            if t.strip():
                slide_text.append((i, t.strip()))

    print("deck: %s" % os.path.basename(deck))
    print("slides: %d   notes pages: %d" % (len(slides), len(notes)))
    if len(notes) < len(slides):
        print("  WARN %d slide(s) have no speaker notes" % (len(slides) - len(notes)))

    # 1. schema
    if os.path.exists(VALIDATOR):
        r = subprocess.run([sys.executable, VALIDATOR, deck], capture_output=True, text=True)
        ok = "PASSED" in (r.stdout + r.stderr)
        print("schema: %s" % ("PASS" if ok else "FAIL"))
        if not ok:
            failures.append("schema")
            print(r.stdout.strip()[-1500:])
    else:
        print("schema: skipped, validator not present")

    # 2. dashes
    bad = [(n, t) for n, t in slide_text if "\u2014" in t or "\u2013" in t]
    print("dashes: %s" % ("PASS" if not bad else "FAIL, %d" % len(bad)))
    for n, t in bad[:10]:
        print("   slide %s: %s" % (n, t[:100]))
    if bad:
        failures.append("dashes")

    # 3. banned words
    rx = re.compile(r"\b(%s)\b" % "|".join(BANNED), re.I)
    bad = [(n, t) for n, t in slide_text if rx.search(t)]
    print("banned words: %s" % ("PASS" if not bad else "FAIL, %d" % len(bad)))
    for n, t in bad[:10]:
        print("   slide %s: %s" % (n, t[:100]))
    if bad:
        failures.append("banned words")

    # 4. meta-content
    here = os.path.dirname(os.path.abspath(__file__))
    scanner = os.path.join(here, "meta_scan.py")
    if os.path.exists(scanner):
        r = subprocess.run([sys.executable, scanner, deck], capture_output=True, text=True)
        clean = r.returncode == 0
        print("meta-content: %s" % ("PASS" if clean else "FAIL"))
        if not clean:
            failures.append("meta-content")
            print(r.stdout.strip())
    else:
        print("meta-content: skipped, meta_scan.py not found")

    # 5. edge bleed
    if render:
        try:
            from PIL import Image
            import numpy as np
        except ImportError:
            print("edge bleed: skipped, Pillow or numpy not available")
        else:
            base = os.path.splitext(deck)[0]
            subprocess.run([sys.executable, SOFFICE, "--headless", "--convert-to", "pdf", deck],
                           capture_output=True)
            subprocess.run(["pdftoppm", "-jpeg", "-r", "100", base + ".pdf", "qa-slide"],
                           capture_output=True)
            imgs = sorted(f for f in os.listdir(".") if f.startswith("qa-slide") and f.endswith(".jpg"))
            flagged = []
            for f in imgs:
                a = np.asarray(Image.open(f).convert("L"))
                h, w = a.shape
                m = 20
                edges = [a[:m, :], a[-m:, :], a[:, :m], a[:, -m:]]
                dark = sum(int((e < 200).sum()) for e in edges)
                if 0 < dark < h * w * 0.02:
                    flagged.append(f)
            print("edge bleed: %s" % ("PASS" if not flagged else "CHECK %s" % ", ".join(flagged)))
            print("  rendered %d image(s) as qa-slide-*.jpg. Look at every one." % len(imgs))

    print()
    if failures:
        print("FAILED: %s" % ", ".join(failures))
        return 1
    print("All mechanical checks passed. Now look at every rendered slide.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
