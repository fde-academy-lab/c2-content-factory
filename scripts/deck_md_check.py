"""Review a deck's markdown source, which is the deck that the verification gate can read.

scripts/deck_check.py measures a built .pptx and cannot see one until it is built. The markdown is
the authoritative deck, so this checks the source itself: the numbering build_deck.py reads, the
title guard, the question and answer pairing, diagram coverage, and meta-content on a learner
slide. Run it on the markdown; run deck_check.py on the pptx once it exists.

Usage:
    python3 scripts/deck_md_check.py content/W01/D3/slides/C2_W01_D03_deck_STUDENT.md
    python3 scripts/deck_md_check.py content/W01/D3

What fails a deck:
  1. A `## ` heading that is neither `S12.`, `D3.` nor a SECTION heading, which build_deck.py
     cannot number.
  2. A title over 54 characters once its number is stripped, which wraps into the DEPTH chip.
  3. A question slide with no answer slide immediately after it.
  4. Fewer than one Mermaid diagram per four body slides.
  5. Meta-content on a slide: facilitation, deck self-reference or programme framing.

What is reported without failing: body slides carrying no diagram, no table and no code, and
slides carrying more than one idea.

A question slide is a heading ending in a question mark, a heading beginning `Question`, or a body
holding a line that starts `**Question.**`. Its answer slide's heading, once the number is
stripped, starts with `Answer`.
"""
import pathlib
import re
import sys

SLIDE = re.compile(r"^## (.+)$", re.M)
NUMBERED = re.compile(r"^([SD])(\d+)([a-z]?)\.\s*(.+)$")
STRIP_NUM = re.compile(r"^[SD]\d+[a-z]?\.\s*")
QUESTION_BODY = re.compile(r"^\s*\*\*Question\.?\*\*", re.M)
MAX_TITLE = 54
MIN_DIAGRAM_SHARE = 4  # one diagram per this many body slides

META = [
    (r"\bask the room\b", "facilitation"),
    (r"\btake answers\b", "facilitation"),
    (r"\bshow of hands\b", "facilitation"),
    (r"\bgive (?:this|them) \w+ minutes\b", "facilitation"),
    (r"\bthe room will\b", "facilitation"),
    (r"\bdo not reveal\b", "facilitation"),
    (r"\bcirculate and\b", "facilitation"),
    (r"\bwait for (?:the room|someone)\b", "facilitation"),
    (r"\bthis deck\b", "deck self-reference"),
    (r"\bthe (?:previous|last) slide\b", "deck self-reference"),
    (r"\bas we saw earlier\b", "deck self-reference"),
    (r"\bin the next section\b", "deck self-reference"),
    (r"\blearning objectives?\b", "programme framing"),
    (r"\btoday's agenda\b", "programme framing"),
    (r"\bhow this session runs\b", "programme framing"),
]


def parse(text):
    """[(title, [body lines]), ...], matching how build_deck.py splits the same file."""
    slides, current = [], None
    for line in text.splitlines():
        m = re.match(r"^## (.+)$", line)
        if m:
            if current:
                slides.append(current)
            current = (m.group(1).strip(), [])
        elif current is not None and line.strip() != "---":
            current[1].append(line)
    if current:
        slides.append(current)
    return slides


def blocks(body):
    """Count the content blocks on a slide: prose runs, fences and tables each count once."""
    count, inside, prose = 0, False, False
    for line in body:
        s = line.strip()
        if s.startswith("```"):
            if not inside:
                count += 1
            inside = not inside
            prose = False
            continue
        if inside:
            continue
        if s.startswith("|"):
            if not prose:
                count += 1
            prose = True
            continue
        if s:
            if not prose:
                count += 1
            prose = True
        else:
            prose = False
    return count


def check_deck(path):
    text = path.read_text(encoding="utf-8", errors="replace")
    slides = parse(text)
    if not slides:
        print(f"FAIL  {path.name}: no '## ' slide headings, so build_deck.py would produce nothing")
        return 1, ""

    fails, body_slides, diagrams, text_only, crowded = 0, 0, 0, [], []
    titles = [t for t, _ in slides]

    for n, (title, body) in enumerate(slides, start=1):
        section = title.upper().startswith("SECTION")
        joined = "\n".join(body)

        if not section and not NUMBERED.match(title):
            print(f"FAIL  {path.name} slide {n}: heading '{title[:44]}' carries no S or D number, "
                  f"so the deck loses its numbering and its DEPTH marks")
            fails += 1

        bare = STRIP_NUM.sub("", title)
        if not section and len(bare) > MAX_TITLE:
            print(f"FAIL  {path.name} slide {n}: title is {len(bare)} characters against a "
                  f"{MAX_TITLE} limit, so it wraps into the chip. '{bare[:60]}'")
            fails += 1

        for pattern, kind in META:
            hit = re.search(pattern, joined, re.I)
            if hit:
                print(f"FAIL  {path.name} slide {n}: {kind} on a learner slide, "
                      f"'{hit.group(0)}'. It belongs in the trainer day sheet.")
                fails += 1

        is_question = (bare.rstrip().endswith("?") or QUESTION_BODY.search(joined)
                       or re.match(r"^Question\b", bare, re.I))
        if is_question:
            nxt = STRIP_NUM.sub("", titles[n]) if n < len(titles) else ""
            if not nxt.lower().startswith("answer"):
                print(f"FAIL  {path.name} slide {n}: '{bare[:44]}' asks a question and the next "
                      f"slide is '{nxt[:44] or 'the end of the deck'}'. Every question slide is "
                      f"followed by its answer slide.")
                fails += 1

        if section:
            continue
        body_slides += 1
        has_diagram = "```mermaid" in joined
        has_table = any(l.strip().startswith("|") for l in body)
        has_code = "```" in joined and not has_diagram
        diagrams += 1 if has_diagram else 0
        if not (has_diagram or has_table or has_code):
            text_only.append(n)
        if blocks(body) > 3 or joined.count("\n### ") > 1:
            crowded.append(n)

    wanted = -(-body_slides // MIN_DIAGRAM_SHARE)
    if diagrams < wanted:
        print(f"FAIL  {path.name}: {diagrams} Mermaid diagrams across {body_slides} body slides, "
              f"and {wanted} are required at one per {MIN_DIAGRAM_SHARE}. A concept slide and its "
              f"applied slide each carry a diagram.")
        fails += 1

    depth = sum(1 for t in titles if t.startswith("D") and NUMBERED.match(t))
    sections = sum(1 for t in titles if t.upper().startswith("SECTION"))
    report = (f"      {path.name}: {len(slides)} slides, {sections} section boundaries, {depth} "
              f"DEPTH, {diagrams} diagrams, {len(text_only)} text-only, {len(crowded)} carrying "
              f"more than one idea")
    if text_only:
        print(f"      {path.name}: text-only slides at {', '.join(str(n) for n in text_only[:14])}"
              f"{' and more' if len(text_only) > 14 else ''}")
    if crowded:
        print(f"      {path.name}: more than one idea on slides "
              f"{', '.join(str(n) for n in crowded[:14])}"
              f"{' and more' if len(crowded) > 14 else ''}")
    return fails, report


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print("FAIL  deck_md_check.py needs a slide source or a folder to look in")
        sys.exit(1)

    paths = []
    for a in args:
        t = pathlib.Path(a)
        paths += sorted(p for p in t.rglob("*.md") if p.parent.name == "slides") if t.is_dir() \
            else [t]
    if not paths:
        print("INFO  no slide markdown found, so deck_md_check has nothing to read")
        sys.exit(0)

    fails, reports = 0, []
    for path in paths:
        f, report = check_deck(path)
        fails += f
        if report:
            reports.append(report)
    for report in reports:
        print(report)
    print("RESULT:", "FAIL" if fails else "PASS", f"({fails} failures)")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# scripts/deck_md_check.py content/W01/D3/slides/C2_W01_D03_deck_STUDENT.md
#     Reports slide count, section boundaries, DEPTH slides, diagrams, text-only slides and slides
#     carrying more than one idea. Exit 0 when the numbering, titles, pairing, diagram share and
#     meta scans all pass.
# A deck with a slide titled "S14. Reading a traceback bottom up, and what the last line actually
# tells you about where to look"
#     One FAIL line giving the character count against the 54 limit, and exit 1.
# A deck whose slide S22 ends in a question mark and whose S23 is titled "The whale"
#     One FAIL line naming both slides, and exit 1.
# A deck of 40 body slides carrying 6 Mermaid fences
#     One FAIL line saying 10 are required, and exit 1.
# A slide reading "Ask the room which one they would keep"
#     One FAIL line marking it as facilitation, and exit 1.
