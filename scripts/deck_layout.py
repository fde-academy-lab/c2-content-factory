"""The visual system every slide in this programme is built from.

build_deck.py reads a markdown slide source and calls into here for the furniture, so a deck looks
the same on Monday as it does on Thursday: the same title band, the same accent rule, the same
breadcrumb across the top of a section, the same tinted bar under a claim, the same table.

Four things a slide can carry, and the shape each one takes:

  A claim          `**The claim.** ...` becomes a tinted bar with its label in the accent colour,
                   because the line that matters should not look like the line before it.
  A breadcrumb     `[a] > [b] > [c]` with one step in bold becomes a row of steps with that one
                   filled, so a room always knows which stop it is at.
  A table          gets the programme's own header band and row rules, never PowerPoint's blue.
  Code             sits on a dark card, so a room can tell at a glance what is typed and what is
                   said.

Geometry is in inches on a 13.333 by 7.5 slide, and every number here is one a person chose rather
than a default: a 0.75in side margin, a title baseline at 0.62, the accent rule at 1.46, the body
running from 1.78 to 6.62, and the footer rule at 6.92.
"""
import re

from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Inches, Pt

INK = RGBColor(0x1C, 0x1C, 0x1A)
MUTED = RGBColor(0x5F, 0x63, 0x60)
ACC = RGBColor(0x2B, 0x4A, 0x7D)
TINT = RGBColor(0xE4, 0xEC, 0xF7)
BG = RGBColor(0xF7, 0xF7, 0xF5)
LINE = RGBColor(0xC9, 0xC9, 0xC2)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
PASS = RGBColor(0x1F, 0x6F, 0x4A)
FAIL = RGBColor(0x8A, 0x3D, 0x3D)

SLIDE_W, SLIDE_H = 13.333, 7.5
MARGIN = 0.75
WIDTH = SLIDE_W - 2 * MARGIN
TITLE_TOP = 0.62
RULE_Y = 1.46
BODY_TOP = 1.78
BODY_BOTTOM = 6.62
FOOTER_Y = 6.92

BOLD = re.compile(r"\*\*(.+?)\*\*")
CALLOUT = re.compile(r"^\*\*([^*]{2,40}?[.:])\*\*\s*(.*)$")
CRUMB = re.compile(r"^`?\s*(\*{0,2}\[[^\]]+\]\*{0,2}(?:\s*>\s*\*{0,2}\[[^\]]+\]\*{0,2}){1,7})\s*`?$")
STEP = re.compile(r"(\*{0,2})\[([^\]]+)\]\1")
NUMBERED = re.compile(r"^\s*(\d{1,2})[.)]\s+(.*)$")
QUOTE = re.compile(r"^>\s?(.*)$")
SLIDE_ID = re.compile(r"^([SD])(\d+)([a-z]?)\.\s*(.*)$")


def clean(text):
    """Strip the markdown that must never reach a slide."""
    return BOLD.sub(r"\1", text).replace("`", "")


# Pixels of advance per character per point of type, taken from the widest font the slide is
# likely to be drawn with rather than the narrowest. A deck is authored where Consolas does not
# exist and is opened where it does, so the renderer substitutes something wider, and an estimate
# built on the narrow font puts the last line of a code card outside the card. DejaVu Sans Mono
# advances 0.602em and DejaVu Sans about 0.52em, which at 96 pixels to the inch is 0.80 and 0.69
# pixels per character per point. Erring wide costs an eighth of an inch of height; erring narrow
# spills the text.
CHAR_W = 0.69
MONO_CHAR_W = 0.80


def wrapped_rows(text, width_in, size, mono=False):
    """How many lines this text takes in a box that wide, at that size."""
    per_line = max(12, int(width_in * 96 / (size * (MONO_CHAR_W if mono else CHAR_W))))
    return max(1, -(-len(clean(text)) // per_line))


def text_height(lines, width_in, size, mono=False, gap=0.1):
    """The height a run of lines needs, in inches, counting the ones that wrap."""
    line_in = size / 72 * (1.32 if mono else 1.36)
    rows = sum(wrapped_rows(l, width_in, size, mono) for l in lines)
    return rows * line_in + gap * len(lines) + 0.12


def add_runs(para, text, size, colour, mono=False, bold_all=False):
    """Write text, turning **bold** into real bold runs rather than printing the asterisks."""
    for i, piece in enumerate(BOLD.split(text.replace("`", ""))):
        if not piece:
            continue
        r = para.add_run()
        r.text = piece
        r.font.size = Pt(size)
        r.font.bold = bold_all or bool(i % 2)
        r.font.color.rgb = colour
        r.font.name = "Consolas" if mono else "Calibri"


def _plain(shape):
    shape.line.fill.background()
    shape.shadow.inherit = False
    return shape


def rect(slide, x, y, w, h, fill=None, line=None, line_w=1.0, shape=MSO_SHAPE.RECTANGLE):
    s = slide.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    if fill is None:
        s.fill.background()
    else:
        s.fill.solid()
        s.fill.fore_color.rgb = fill
    if line is None:
        s.line.fill.background()
    else:
        s.line.color.rgb = line
        s.line.width = Pt(line_w)
    s.shadow.inherit = False
    s.text_frame.word_wrap = True
    return s


def textbox(slide, x, y, w, h, anchor=MSO_ANCHOR.TOP):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    # A text frame carries a tenth of an inch of inset on every side by default, which is height
    # the box was never measured for and is why a last line lands outside the card behind it.
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Pt(0)
    return tb


# --------------------------------------------------------------------------- slide furniture
def background(slide, prs, colour):
    s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    s.fill.solid()
    s.fill.fore_color.rgb = colour
    _plain(s)
    slide.shapes._spTree.remove(s._element)
    slide.shapes._spTree.insert(2, s._element)


def pill(slide, x, y, text, fill, ink, w=0.86, h=0.3, size=11):
    s = rect(slide, x, y, w, h, fill, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    s.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = s.text_frame.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = text
    r.font.size = Pt(size)
    r.font.bold = True
    r.font.name = "Calibri"
    r.font.color.rgb = ink
    return s


def title_band(slide, title, section=False, depth=False):
    """The slide's number as a pill, its title, and the rule that separates both from the body."""
    m = SLIDE_ID.match(title)
    label, words = (f"{m.group(1)}{m.group(2)}{m.group(3)}", m.group(4)) if m else (None, title)
    if section:
        tb = textbox(slide, MARGIN, 2.6, WIDTH, 1.6, MSO_ANCHOR.MIDDLE)
        p = tb.text_frame.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        add_runs(p, clean(words), 40, WHITE, bold_all=True)
        return
    if label:
        pill(slide, MARGIN, TITLE_TOP + 0.04, label, ACC if not depth else INK, WHITE)
    if depth:
        pill(slide, SLIDE_W - MARGIN - 1.02, TITLE_TOP + 0.04, "DEPTH", INK, WHITE, w=1.02)
    left = MARGIN + (1.02 if label else 0)
    box_w = WIDTH - (1.02 if label else 0) - (1.2 if depth else 0.2)
    text = clean(words)
    # 30pt Calibri bold runs about 22 characters to the inch of box, so a title that would take a
    # second line steps down instead of growing into the rule underneath it.
    size = 30 if len(text) <= int(box_w * 2.35) else (26 if len(text) <= int(box_w * 2.8) else 23)
    tb = textbox(slide, left, TITLE_TOP - 0.08, box_w, RULE_Y - TITLE_TOP + 0.02,
                 MSO_ANCHOR.MIDDLE)
    p = tb.text_frame.paragraphs[0]
    add_runs(p, text, size, INK, bold_all=True)
    rect(slide, MARGIN, RULE_Y, WIDTH, 0.035, ACC)


def footer_band(slide, footer, number, total, section=False):
    rule = WHITE if section else LINE
    rect(slide, MARGIN, FOOTER_Y, WIDTH, 0.014, rule)
    ink = WHITE if section else MUTED
    tb = textbox(slide, MARGIN, FOOTER_Y + 0.07, WIDTH - 1.2, 0.32)
    r = tb.text_frame.paragraphs[0].add_run()
    r.text = footer
    r.font.size = Pt(10)
    r.font.name = "Calibri"
    r.font.color.rgb = ink
    nb = textbox(slide, SLIDE_W - MARGIN - 1.2, FOOTER_Y + 0.07, 1.2, 0.32)
    np_ = nb.text_frame.paragraphs[0]
    np_.alignment = PP_ALIGN.RIGHT
    nr = np_.add_run()
    nr.text = f"{number} / {total}"
    nr.font.size = Pt(10)
    nr.font.name = "Calibri"
    nr.font.color.rgb = ink


# --------------------------------------------------------------------------- body blocks
def callout(slide, top, label, body, width=WIDTH, dark=False, scale=1.0, x=MARGIN):
    """The line that carries the point, set apart from the line before it."""
    size = round(20 * scale)
    lines = wrapped_rows(label + " " + body, width - 0.6, size)
    h = 0.26 + (size / 72 * 1.42) * lines
    rect(slide, x, top, width, h, INK if dark else TINT)
    rect(slide, x, top, 0.055, h, ACC if not dark else TINT)
    tb = textbox(slide, x + 0.28, top + 0.1, width - 0.5, h - 0.16, MSO_ANCHOR.MIDDLE)
    p = tb.text_frame.paragraphs[0]
    lr = p.add_run()
    lr.text = label + " "
    lr.font.size = Pt(size)
    lr.font.bold = True
    lr.font.name = "Calibri"
    lr.font.color.rgb = TINT if dark else ACC
    if body:
        add_runs(p, body, size, WHITE if dark else INK)
    return top + h + 0.18


def breadcrumb(slide, top, line, section=False):
    """Where the room is in the day, drawn rather than described."""
    steps = [(bool(b), t.strip()) for b, t in STEP.findall(line)]
    if not steps:
        return top
    gap = 0.12
    w = (WIDTH - gap * (len(steps) - 1)) / len(steps)
    h = 0.52
    for i, (here, text) in enumerate(steps):
        x = MARGIN + i * (w + gap)
        if here:
            fill, ink, border = ACC, WHITE, None
        elif section:
            fill, ink, border = None, WHITE, WHITE
        else:
            fill, ink, border = WHITE, MUTED, LINE
        s = rect(slide, x, top, w, h, fill, border, 0.75, MSO_SHAPE.ROUNDED_RECTANGLE)
        s.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = s.text_frame.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        r = p.add_run()
        r.text = text
        r.font.size = Pt(12)
        r.font.bold = here
        r.font.name = "Calibri"
        r.font.color.rgb = ink
    return top + h + 0.22


def code_card(slide, top, lines, width=WIDTH, scale=1.0, x=MARGIN):
    """Typed things sit on a dark card, so a room never confuses them with said things."""
    size = max(11, round(16 * scale))
    rows = sum(wrapped_rows(l, width - 0.6, size, mono=True) for l in lines)
    h = 0.28 + (size / 72 * 1.42) * rows
    rect(slide, x, top, width, h, INK)
    rect(slide, x, top, 0.055, h, ACC)
    tb = textbox(slide, x + 0.26, top + 0.11, width - 0.44, h - 0.2)
    first = True
    for line in lines:
        p = tb.text_frame.paragraphs[0] if first else tb.text_frame.add_paragraph()
        first = False
        add_runs(p, line.rstrip(), size, TINT, mono=True)
        p.space_after = Pt(2)
    return top + h + 0.18


def quote_block(slide, top, lines, width=WIDTH, scale=1.0, x=MARGIN):
    text = " ".join(QUOTE.sub(r"\1", l.strip()) for l in lines if l.strip())
    size = round(19 * scale)
    h = 0.2 + (size / 72 * 1.36) * wrapped_rows(text, width - 0.3, size)
    rect(slide, x, top, 0.045, h, LINE)
    tb = textbox(slide, x + 0.26, top, width - 0.3, h)
    p = tb.text_frame.paragraphs[0]
    add_runs(p, text, size, MUTED)
    for r in p.runs:
        r.font.italic = True
    return top + h + 0.16


def numbered(slide, top, items, width=WIDTH, scale=1.0, x=MARGIN):
    """A counted list gets its numerals in the accent colour and its text on one grid."""
    size = round(19 * scale)
    for n, text in items:
        rows = wrapped_rows(text, width - 0.6, size)
        h = (size / 72 * 1.36) * rows + 0.12
        nb = textbox(slide, x, top, 0.5, h)
        nr = nb.text_frame.paragraphs[0].add_run()
        nr.text = n
        nr.font.size = Pt(size)
        nr.font.bold = True
        nr.font.name = "Calibri"
        nr.font.color.rgb = ACC
        tb = textbox(slide, x + 0.5, top, width - 0.5, h)
        add_runs(tb.text_frame.paragraphs[0], text, size, INK)
        top += h + 0.06
    return top + 0.12


TABLE_STYLE_NONE = "{2D5ABB26-0587-4C30-8999-92F81FD0307C}"


def table(slide, rows, top, width=WIDTH, max_h=None, scale=1.0, x=MARGIN):
    """A markdown table in the programme's own colours, never PowerPoint's blue banding."""
    grid = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows
            if not re.fullmatch(r"\s*\|[\s:\-|]+\|\s*", r)]
    if not grid:
        return top
    cols = max(len(r) for r in grid)
    grid = [r + [""] * (cols - len(r)) for r in grid]
    room = (max_h if max_h is not None else BODY_BOTTOM - top) - 0.1

    # Columns are sized by what they hold. Splitting the width evenly gives a column of counts
    # the same room as a column of sentences, so the sentences wrap four deep and the table grows
    # to twice the height it needs. Each column asks for its longest cell, no column may take
    # more than half the table, and none drops below three quarters of an inch.
    pad = 0.24
    base = max(9, round((15 if cols <= 3 else 13) * scale))
    per_char = base * CHAR_W / 96.0
    want = [max(len(clean(row[ci])) for row in grid) for ci in range(cols)]
    floor_w, ceil_w = 0.85, width * 0.5
    raw = [min(ceil_w, wcell * per_char + pad) for wcell in want]

    # Fit the wants into the width without letting any column fall under its floor. Scaling every
    # column by the same factor and then lifting the short ones back up overshoots the width, and
    # a second scaling pushes them under the floor again, which is how an order id ends up split
    # across two lines. The short columns are pinned and only the rest are scaled.
    col_ws = list(raw)
    for _ in range(cols + 1):
        pinned = [i for i, w in enumerate(col_ws) if w <= floor_w + 1e-9]
        spare = width - floor_w * len(pinned)
        rest = sum(col_ws[i] for i in range(cols) if i not in pinned)
        if rest <= 0 or spare <= 0:
            col_ws = [width / cols] * cols
            break
        col_ws = [floor_w if i in pinned else max(floor_w, col_ws[i] * spare / rest)
                  for i in range(cols)]
        if all(w >= floor_w - 1e-9 for w in col_ws) and abs(sum(col_ws) - width) < 0.01:
            break

    def measure(size):
        """A cell that wraps needs a row two lines tall, so the widest cell sets each row."""
        wrapped = [max(wrapped_rows(c, col_ws[ci] - pad, size) for ci, c in enumerate(row))
                   for row in grid]
        return [max(0.34, (size / 72 * 1.36) * n + 0.14) for n in wrapped]

    # A table is fitted by stepping its type down until the rows it really needs fit the room,
    # never by scaling the row heights. PowerPoint treats a row height as a minimum and grows the
    # row back to hold its text, so a scaled table renders taller than it was told to be and lands
    # on whatever comes after it.
    size, row_hs = base, measure(base)
    while sum(row_hs) > room and size > 9:
        size -= 1
        row_hs = measure(size)
    height = Inches(sum(row_hs))
    shape = slide.shapes.add_table(len(grid), cols, Inches(x), Inches(top), Inches(width),
                                   height)
    tbl = shape.table
    tblPr = tbl._tbl.tblPr
    tblPr.set("firstRow", "0")
    tblPr.set("bandRow", "0")
    for tag in ("a:tableStyleId",):
        node = tblPr.find(qn(tag))
        if node is None:
            node = tblPr.makeelement(qn(tag), {})
            tblPr.append(node)
        node.text = TABLE_STYLE_NONE
    for ci, cw in enumerate(col_ws):
        tbl.columns[ci].width = Inches(cw)
    for ri, row in enumerate(grid):
        tbl.rows[ri].height = Inches(row_hs[ri])
        for ci, cell in enumerate(row):
            tc = tbl.cell(ri, ci)
            tc.text = ""
            tc.fill.solid()
            tc.fill.fore_color.rgb = ACC if ri == 0 else (WHITE if ri % 2 else BG)
            tc.margin_left = tc.margin_right = Pt(8)
            tc.margin_top = tc.margin_bottom = Pt(3)
            tc.vertical_anchor = MSO_ANCHOR.MIDDLE
            para = tc.text_frame.paragraphs[0]
            add_runs(para, cell, size + (0 if ri else 1), WHITE if ri == 0 else INK,
                     bold_all=ri == 0)
    return top + height.inches + 0.28
