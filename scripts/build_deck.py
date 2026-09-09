"""Build a .pptx from a markdown slide source.

The markdown is the authoritative deck, because the verification gate can read it and cannot read a
pptx. This turns it into slides without leaking markdown syntax onto them: tables become real
PowerPoint tables, bold markers become bold runs, and backticks disappear.

Usage:
    python3 scripts/build_deck.py content/W01/D3/C2_W01_D03_deck_STUDENT.md \
        --footer "Week 1 Day 3: profile before you touch"

Slide source format: every `## ` heading starts a slide. A heading beginning with SECTION gets the
section-boundary treatment. `---` rules are ignored.
"""
import argparse
import pathlib
import re

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt

INK = RGBColor(0x1C, 0x1C, 0x1A)
MUTED = RGBColor(0x5F, 0x63, 0x60)
ACC = RGBColor(0x2B, 0x4A, 0x7D)
BG = RGBColor(0xF7, 0xF7, 0xF5)
SECBG = RGBColor(0x2B, 0x4A, 0x7D)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

BOLD = re.compile(r"\*\*(.+?)\*\*")


def parse(md):
    slides, cur = [], None
    for line in md.splitlines():
        m = re.match(r"^## (.+)$", line)
        if m:
            if cur:
                slides.append(cur)
            cur = (m.group(1).strip(), [])
        elif cur is not None and line.strip() != "---":
            cur[1].append(line)
    if cur:
        slides.append(cur)
    return slides


def split_blocks(body):
    """Split a slide body into ('text'|'code'|'table', lines) blocks."""
    blocks, buf, mode = [], [], "text"
    for line in body:
        if line.strip().startswith("```"):
            if buf:
                blocks.append((mode, buf)); buf = []
            mode = "code" if mode != "code" else "text"
            continue
        is_row = line.strip().startswith("|") and line.strip().endswith("|")
        want = "code" if mode == "code" else ("table" if is_row else "text")
        if want != mode and mode != "code":
            if buf:
                blocks.append((mode, buf)); buf = []
            mode = want
        buf.append(line)
    if buf:
        blocks.append((mode, buf))
    return [(m, [l for l in b if l.strip() or m == "code"]) for m, b in blocks if any(l.strip() for l in b)]


def clean(text):
    """Strip the markdown that must never reach a slide."""
    return BOLD.sub(r"\1", text).replace("`", "")


def add_runs(para, text, size, colour, mono=False):
    """Write text, turning **bold** into real bold runs rather than printing the asterisks."""
    for i, piece in enumerate(BOLD.split(text.replace("`", ""))):
        if not piece:
            continue
        r = para.add_run()
        r.text = piece
        r.font.size = Pt(size)
        r.font.bold = bool(i % 2)
        r.font.color.rgb = colour
        r.font.name = "Consolas" if mono else "Calibri"


def add_bg(slide, prs, colour):
    s = slide.shapes.add_shape(1, 0, 0, prs.slide_width, prs.slide_height)
    s.fill.solid(); s.fill.fore_color.rgb = colour
    s.line.fill.background(); s.shadow.inherit = False
    slide.shapes._spTree.remove(s._element)
    slide.shapes._spTree.insert(2, s._element)


def add_table(slide, rows, top, width):
    """A markdown table becomes a PowerPoint table, never a wall of pipe characters."""
    grid = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows
            if not re.fullmatch(r"\s*\|[\s:\-|]+\|\s*", r)]
    if not grid:
        return top
    cols = max(len(r) for r in grid)
    grid = [r + [""] * (cols - len(r)) for r in grid]
    height = Inches(min(0.42 * len(grid), 4.2))
    shape = slide.shapes.add_table(len(grid), cols, Inches(0.85), Inches(top), width, height)
    for ri, row in enumerate(grid):
        for ci, cell in enumerate(row):
            tc = shape.table.cell(ri, ci)
            tc.text = ""
            para = tc.text_frame.paragraphs[0]
            add_runs(para, cell, 14 if ri else 13, INK if ri else ACC)
            if ri == 0:
                for r in para.runs:
                    r.font.bold = True
            tc.margin_top = tc.margin_bottom = Pt(2)
    return top + height.inches + 0.2


def build(src, out, footer):
    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
    width = Inches(11.6)
    for title, body in parse(pathlib.Path(src).read_text()):
        section = title.upper().startswith("SECTION")
        s = prs.slides.add_slide(prs.slide_layouts[6])
        add_bg(s, prs, SECBG if section else BG)

        tb = s.shapes.add_textbox(Inches(0.85), Inches(0.7), width, Inches(1.3))
        tb.text_frame.word_wrap = True
        p0 = tb.text_frame.paragraphs[0]
        add_runs(p0, clean(re.sub(r"^S\d+[a-z]?\.\s*", "", title)), 36 if section else 32,
                 WHITE if section else INK)
        for r in p0.runs:
            r.font.bold = True
        if section:
            p0.alignment = PP_ALIGN.CENTER

        top = 2.15
        for mode, lines in split_blocks(body):
            if mode == "table" and not section:
                top = add_table(s, lines, top, width)
                continue
            h = max(0.55, min(4.6, 0.42 * len(lines) + 0.35))
            bb = s.shapes.add_textbox(Inches(0.85), Inches(top), width, Inches(h))
            bb.text_frame.word_wrap = True
            first = True
            for line in lines:
                para = bb.text_frame.paragraphs[0] if first else bb.text_frame.add_paragraph()
                first = False
                mono = mode == "code"
                add_runs(para, line.rstrip(), 17 if mono else 21,
                         WHITE if section else (ACC if mono else INK), mono=mono)
                if section:
                    para.alignment = PP_ALIGN.CENTER
                para.space_after = Pt(4 if mono else 10)
            top += h + 0.15
            if top > 6.6:
                break

        fb = s.shapes.add_textbox(Inches(0.85), Inches(6.9), width, Inches(0.4))
        fr = fb.text_frame.paragraphs[0].add_run()
        fr.text = footer
        fr.font.size = Pt(10); fr.font.color.rgb = MUTED; fr.font.name = "Calibri"
    prs.save(out)
    return len(prs.slides.__iter__.__self__._sldIdLst)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("source")
    ap.add_argument("--footer", default="")
    ap.add_argument("--out")
    a = ap.parse_args()
    src = pathlib.Path(a.source)
    out = pathlib.Path(a.out) if a.out else src.with_suffix(".pptx")
    n = build(src, out, a.footer or src.stem)
    print(f"{out.name}: {n} slides")


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# scripts/build_deck.py content/W01/D3/C2_W01_D03_deck_STUDENT.md --footer "Week 1 Day 3"
#     Writes C2_W01_D03_deck_STUDENT.pptx with 40 slides, no pipe characters and no asterisks
#     anywhere in the slide text, and markdown tables rendered as PowerPoint tables.
# A slide whose body holds a markdown table
#     Becomes a real table with a bold header row, never lines beginning with "|".
# A slide whose title starts with SECTION
#     Gets the dark background, centred text and white type.
