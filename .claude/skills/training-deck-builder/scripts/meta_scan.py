#!/usr/bin/env python3
"""Scan a deck or a slide-content file for meta-content on learner-facing slides.

Usage:
    python3 meta_scan.py deck.pptx
    python3 meta_scan.py content.md
    python3 meta_scan.py content.js

For a .pptx it reads the slide text only and ignores speaker notes, which is
where facilitation guidance belongs. For a text file it scans everything and
you judge which hits sit on a slide.

Exit code is 1 when anything is found, so it can gate a build.
"""
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

NS = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main"}

PATTERNS = [
    ("facilitation", r"\bshow of hands\b"),
    ("facilitation", r"\bask the room\b"),
    ("facilitation", r"\bthe room will\b"),
    ("facilitation", r"\btake the disagreement"),
    ("facilitation", r"\bdo not reveal\b"),
    ("facilitation", r"\bgive this slide\b"),
    ("facilitation", r"\bcirculate\b"),
    ("facilitation", r"\bflip chart\b"),
    ("facilitation", r"\bhold the timer\b"),
    ("facilitation", r"\bcollect answers\b"),
    ("facilitation", r"\btake answers\b"),
    ("deck self-reference", r"\bthis deck\b"),
    ("deck self-reference", r"\bthis slide\b"),
    ("deck self-reference", r"\b(previous|next|earlier|following) slide\b"),
    ("deck self-reference", r"\bdeck [0-9]\b"),
    ("deck self-reference", r"\bas we (saw|discussed|covered)\b"),
    ("deck self-reference", r"\banswered later\b"),
    ("deck self-reference", r"\blater in the (deck|session|module)\b"),
    ("programme framing", r"\bthis (session|module|programme|program|workshop) (is|will|covers)\b"),
    ("programme framing", r"\blearning objectives?\b"),
    ("programme framing", r"\bby the end of (today|this session)\b"),
    ("programme framing", r"\bagenda\b"),
    ("programme framing", r"\bhousekeeping\b"),
    ("programme framing", r"\brecap of (yesterday|day [0-9])\b"),
    ("scaffolding", r"\bthe (snag|instinct|hook)\b"),
    ("scaffolding", r"\bhold on to this\b"),
    ("scaffolding", r"\bbeat [0-9]\b"),
    ("scaffolding", r"\bwarm[- ]up\b"),
    ("rationale", r"\bwe (chose|decided|designed) this\b"),
    ("rationale", r"\bconstruction (built )?for this (course|programme|program)\b"),
    ("rationale", r"\bbecause it is the point of\b"),
    ("audience", r"\byou (learners|participants)\b"),
    ("audience", r"\bthe (learners|participants|trainees) will\b"),
    ("audience", r"\bas a trainer\b"),
]

# Navigation chrome and learner-facing instructions are not meta-content.
ALLOWED = [
    # page identifiers and footers: "Day 2 . Deck 1", "Deck 1 of 2", "Module 3"
    r"^(day\s*\d+\s*[^a-z0-9]{0,4}\s*)?(deck|half|part|session|module|day)\s*\d+(\s*of\s*\d+)?$",
    r"^day\s*\d+\s*,\s*(deck|half|part)\s*\d+(\s*of\s*\d+)?$",
    # the one permitted promise line on a title slide
    r"^by the end of this deck you (can|will be able to)",
    # learner-facing activity instructions
    r"^(in|working in) pairs\b",
]


def slide_text_from_pptx(path):
    out = []
    with zipfile.ZipFile(path) as z:
        names = sorted(
            [n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)],
            key=lambda n: int(re.search(r"(\d+)", n.split("/")[-1]).group(1)),
        )
        for i, n in enumerate(names, 1):
            root = ET.fromstring(z.read(n))
            texts = [t.text or "" for t in root.iter("{%s}t" % NS["a"])]
            for t in texts:
                if t.strip():
                    out.append((i, t.strip()))
    return out


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    path = sys.argv[1]
    if path.lower().endswith(".pptx"):
        items = slide_text_from_pptx(path)
        label = "slide"
    else:
        with open(path, encoding="utf-8") as f:
            items = [(i, line.strip()) for i, line in enumerate(f, 1) if line.strip()]
        label = "line"

    hits = []
    for num, text in items:
        low = text.lower()
        if any(re.search(a, low) for a in ALLOWED):
            continue
        for kind, pat in PATTERNS:
            if re.search(pat, low):
                hits.append((num, kind, text))
                break

    if not hits:
        print("meta_scan: clean, %d text runs checked" % len(items))
        return 0

    print("meta_scan: %d hit(s)\n" % len(hits))
    for num, kind, text in hits:
        snippet = text if len(text) <= 110 else text[:107] + "..."
        print("  %s %-4s [%s] %s" % (label, num, kind, snippet))
    print("\nMove facilitation guidance to speaker notes. Rewrite the rest.")
    print("See references/meta-content.md for the rewrite of each pattern.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
