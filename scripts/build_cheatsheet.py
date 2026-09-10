"""Render a cheat sheet's markdown into the landscape PDF a learner pins above a desk.

The markdown stays the source of truth, because it is what the verification gate reads and what
renders on GitHub. This turns it into the printed sheet: a title band, an anchor band carrying the
one picture the sheet is built around, the blocks packed into balanced columns, and a foot strip of
the day's vocabulary read from its study notes rather than written again.

Usage:
    python3 scripts/build_cheatsheet.py content/W01/D1/cheatsheets/C2_W01_D01_kernel_records_STUDENT.md
    python3 scripts/build_cheatsheet.py content/W01 --png /tmp/sheets     # every sheet under a folder
    python3 scripts/build_cheatsheet.py <sheet.md> --format png          # raster diagrams instead of svg

Source format: `## Panel {n}: {title}` starts a block and a `**Crux:**` paragraph closes one.
Everything else is the block's body, read as the markdown subset the sheets actually use, which is
paragraphs, bold, inline code, fenced code, mermaid fences, tables and bullet lists. A gap variant
writes its blanks as `__________ [n]` and keeps its answer key after the last panel, and both are
recognised here: the blank prints as a ruled box carrying its number and the key prints as a strip
at the foot that a learner covers while filling the sheet in.

Panel one is the anchor. It spans the full width and it carries the anchor test: cover every other
block and the anchor alone should still recap the sheet. A sheet whose panel one cannot do that has
its panels reordered rather than excused.

Mermaid fences go through mmdc with the programme palette, so a diagram on a slide, in a notebook
and on a sheet are recognisably one drawing. The config sets htmlLabels false at the top level and
not only under flowchart, because mermaid-cli honours only the top-level key and a foreignObject
label is dropped without warning by weasyprint, which prints every node as an empty box.
"""
import argparse
import hashlib
import html
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

# The palette scripts/build_deck.py and scripts/c2kit.py use, so every artifact in the programme
# is recognisably the same drawing.
INK = "#1C1C1A"
MUTED = "#5F6360"
ACCENT = "#2B4A7D"
TINT = "#E4ECF7"
BG = "#F7F7F5"
LINE = "#C9C9C2"
PASS = "#1F6F4A"
FAIL = "#8A3D3D"

CACHE = pathlib.Path(tempfile.gettempdir()) / "c2_sheet_diagrams"

# htmlLabels sits at the top level on purpose. Setting it only under "flowchart" leaves
# mermaid-cli 11 emitting foreignObject labels, which weasyprint drops silently, so every node
# prints as an empty box and the sheet looks finished while carrying no words at all.
MERMAID_CONFIG = """{
  "theme": "base",
  "htmlLabels": false,
  "themeVariables": {
    "background": "#FFFFFF",
    "primaryColor": "#E4ECF7",
    "primaryTextColor": "#1C1C1A",
    "primaryBorderColor": "#2B4A7D",
    "secondaryColor": "#F7F7F5",
    "secondaryTextColor": "#1C1C1A",
    "secondaryBorderColor": "#2B4A7D",
    "tertiaryColor": "#FFFFFF",
    "tertiaryTextColor": "#1C1C1A",
    "tertiaryBorderColor": "#C9C9C2",
    "lineColor": "#2B4A7D",
    "textColor": "#1C1C1A",
    "mainBkg": "#E4ECF7",
    "nodeBorder": "#2B4A7D",
    "clusterBkg": "#F7F7F5",
    "clusterBorder": "#C9C9C2",
    "edgeLabelBackground": "#FFFFFF",
    "fontFamily": "DejaVu Sans, Verdana, sans-serif",
    "fontSize": "16px"
  },
  "flowchart": {"htmlLabels": false, "curve": "linear", "padding": 4,
                "nodeSpacing": 20, "rankSpacing": 18, "useMaxWidth": true},
  "sequence": {"useMaxWidth": true},
  "er": {"useMaxWidth": true, "entityPadding": 4, "minEntityHeight": 10, "minEntityWidth": 70}
}"""

PUPPETEER_CONFIG = '{"args":["--no-sandbox","--disable-setuid-sandbox"]}\n'


# --------------------------------------------------------------------------- mermaid
def _chromium():
    """The browser this session has, wherever it keeps it."""
    roots = [os.environ.get("PLAYWRIGHT_BROWSERS_PATH"), "/opt/pw-browsers",
             str(pathlib.Path.home() / ".cache" / "ms-playwright")]
    for root in [r for r in roots if r]:
        for pattern in ("chromium-*/chrome-linux/chrome", "chromium/chrome-linux/chrome"):
            for path in sorted(pathlib.Path(root).glob(pattern)):
                if path.is_file():
                    return str(path)
    return None


def render_mermaid(code, fmt="svg"):
    """Render one fence to an image and return its path, or None when mmdc is unavailable.

    Renders are cached by content hash and by format, so rebuilding a sheet re-renders only what
    changed and a week of sheets sharing a diagram renders it once.
    """
    body = code.strip() + "\n"
    key = hashlib.sha256((body + fmt + MERMAID_CONFIG).encode()).hexdigest()[:16]
    CACHE.mkdir(parents=True, exist_ok=True)
    out = CACHE / f"{key}.{fmt}"
    if out.exists():
        return out
    if not shutil.which("mmdc"):
        return None
    src = CACHE / f"{key}.mmd"
    src.write_text(body, encoding="utf-8")
    conf = CACHE / f"mermaid_{hashlib.sha256(MERMAID_CONFIG.encode()).hexdigest()[:8]}.json"
    conf.write_text(MERMAID_CONFIG, encoding="utf-8")
    pup = CACHE / "puppeteer.json"
    if not pup.exists():
        pup.write_text(PUPPETEER_CONFIG)
    env = dict(os.environ)
    chrome = _chromium()
    if chrome:
        env.setdefault("PUPPETEER_EXECUTABLE_PATH", chrome)
    cmd = ["mmdc", "-i", str(src), "-o", str(out), "-b", "transparent",
           "-c", str(conf), "-p", str(pup)]
    if fmt == "png":
        cmd += ["-w", "2400"]
    try:
        subprocess.run(cmd, capture_output=True, text=True, env=env, timeout=300)
    except Exception:
        return None
    if not out.exists():
        return None
    if fmt == "svg" and b"foreignObject" in out.read_bytes():
        # An unrendered label is worse than a missing diagram, because it looks finished.
        out.unlink()
        return None
    return out


def svg_size(path):
    """The diagram's own width and height in CSS pixels, from the viewBox mmdc writes."""
    try:
        head = path.read_text(encoding="utf-8", errors="replace")[:800]
    except Exception:
        return (0, 0)
    box = re.search(r'viewBox="[\d.\-]+ [\d.\-]+ ([\d.]+) ([\d.]+)"', head)
    if box:
        return (float(box.group(1)), float(box.group(2)))
    w = re.search(r'\bwidth="([\d.]+)', head)
    h = re.search(r'\bheight="([\d.]+)', head)
    return (float(w.group(1)) if w else 0, float(h.group(1)) if h else 0)


def svg_width(path):
    return svg_size(path)[0]


def label_pt(size, box_pt):
    """How large the diagram's labels print once it is fitted into a box, in points.

    A diagram is scaled to fit both the width and the height it is given, so the smaller of the
    two ratios decides. Mermaid draws its labels at 16px, which is 12pt before any scaling.
    """
    w_px, h_px = size
    if not w_px or not h_px:
        return 99.0
    box_w, box_h = box_pt
    scale = min(box_w / (w_px * 0.75), box_h / (h_px * 0.75), 1.0e9)
    return 12.0 * scale


# Mermaid sets its labels at 16px, so a diagram scaled into a column of C points prints its
# labels at 16C/width_px points, and below about 5.2pt nobody reads them standing at a desk.
# That fixes the widest diagram a column can carry, and it is what picks the column count: a
# sheet of pictures gets two wide columns and a sheet of words gets three narrow ones, so the
# type never shrinks to make a layout work.
PAGE_PT = (297 - 16) * 72 / 25.4     # A4 landscape less the page margins
GAP_PT = 3 * 72 / 25.4               # the column gap
PAD_PT = 5.6 * 72 / 25.4             # a panel's own padding and border
MIN_LABEL_PT = 5.2
MERMAID_LABEL_PX = 16.0


def column_pt(n):
    return (PAGE_PT - (n - 1) * GAP_PT) / n - PAD_PT


def max_width_px(n):
    """The widest diagram column count n can print and still be read."""
    return column_pt(n) * MERMAID_LABEL_PX / MIN_LABEL_PT


def choose_columns(widths, lo=2, hi=4, default=3):
    """The most columns that still print every diagram legibly."""
    if not widths:
        return default
    widest = max(widths)
    for n in range(hi, lo - 1, -1):
        if widest <= max_width_px(n):
            return n
    return lo


MAX_ONE_COLUMN_PX = max_width_px(3)

MM = 72 / 25.4
DIAGRAM_H_CAP_MM = 62       # past this a panel is a poster, not a block on a sheet


def height_for(sizes, box_w_pt, cap_mm=DIAGRAM_H_CAP_MM, floor_mm=26):
    """The height a set of diagrams needs before their labels drop under the readable size.

    The page used to fix this at a constant and quietly shrink whatever did not fit, which is how
    a sheet ends up looking finished while printing its labels at three points. Reading it the
    other way round, the diagrams say how much height they need and the page count follows.
    """
    need = floor_mm
    for w_px, h_px in sizes:
        if not w_px or not h_px:
            continue
        by_width = (box_w_pt / (w_px * 0.75)) * h_px * 0.75 / MM
        by_label = (MIN_LABEL_PT / 12.0) * h_px * 0.75 / MM
        need = max(need, min(by_width, by_label))
    return min(need, cap_mm)


# --------------------------------------------------------------------------- markdown subset
DIVIDER = re.compile(r"^\s*\|[\s:\-|]+\|\s*$")
GAP = re.compile(r"_{4,}\s*\[(\d+)\]")
ORDERED = re.compile(r"^\s*\d{1,2}[.)]\s+")


def inline(text):
    """Bold, inline code and the gap variant's blanks, with everything else escaped."""
    out, last = [], 0
    for m in re.finditer(r"\*\*(.+?)\*\*|`([^`]+)`|_{4,}\s*\[(\d+)\]|(_{4,})", text):
        out.append(html.escape(text[last:m.start()]))
        if m.group(1) is not None:
            out.append(f"<b>{html.escape(m.group(1))}</b>")
        elif m.group(2) is not None:
            out.append(f"<code>{html.escape(m.group(2))}</code>")
        elif m.group(3) is not None:
            out.append(f'<span class="gap"><i>{m.group(3)}</i></span>')
        else:
            # An unnumbered blank still prints as a rule the width the writer drew it, so a
            # long answer looks long and a one-word answer looks short.
            out.append(f'<span class="gap" style="min-width:{min(len(m.group(4)) * 1.1, 60):.0f}mm">'
                       f'</span>')
        last = m.end()
    out.append(html.escape(text[last:]))
    return "".join(out)


def render_table(rows):
    grid = [[c.strip() for c in r.strip().strip("|").split("|")]
            for r in rows if not DIVIDER.match(r)]
    if not grid:
        return ""
    head = "".join(f"<th>{inline(c)}</th>" for c in grid[0])
    body = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>"
                   for r in grid[1:])
    wide = " class=\"cols3\"" if len(grid[0]) >= 3 else ""
    return f"<table{wide}><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>"


def render_body(lines, fmt, missing):
    """The markdown subset the sheets use, as a list of (kind, html, diagram width) pieces."""
    pieces = []
    buf, mode = [], "text"

    def flush():
        nonlocal buf, mode
        if not buf:
            buf, mode = [], "text"
            return
        if mode == "table":
            pieces.append(("table", render_table(buf), (0, 0)))
        elif mode == "code":
            pieces.append(("code", "<pre>" + html.escape("\n".join(buf).rstrip()) + "</pre>", (0, 0)))
        elif mode == "mermaid":
            img = render_mermaid("\n".join(buf), fmt)
            if img:
                pieces.append(("diagram",
                               f'<figure class="diagram"><img src="{img.as_uri()}"></figure>',
                               svg_size(img) if fmt == "svg" else (0, 0)))
            else:
                missing.append("\n".join(buf).splitlines()[0][:40])
                pieces.append(("code", '<pre class="nodiagram">'
                               + html.escape("\n".join(buf)) + "</pre>", (0, 0)))
        elif mode == "list":
            pieces.append(("list", "<ul>" + "".join(
                f"<li>{inline(l.lstrip('-* ').strip())}</li>" for l in buf) + "</ul>", (0, 0)))
        elif mode == "ordered":
            items = "".join("<li>" + inline(ORDERED.sub("", l)) + "</li>" for l in buf)
            pieces.append(("list", f"<ol>{items}</ol>", (0, 0)))
        elif mode == "quote":
            text = " ".join(l.strip().lstrip("> ").strip() for l in buf if l.strip())
            pieces.append(("quote", f"<blockquote>{inline(text)}</blockquote>", (0, 0)))
        else:
            text = " ".join(l.strip() for l in buf if l.strip())
            if text:
                pieces.append(("text", f"<p>{inline(text)}</p>", (0, 0)))
        buf, mode = [], "text"

    inside_fence = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            if inside_fence:
                flush()
                inside_fence = False
            else:
                flush()
                inside_fence = True
                mode = "mermaid" if stripped[3:].strip().lower() == "mermaid" else "code"
            continue
        if inside_fence:
            buf.append(line.rstrip())
            continue
        if not stripped:
            flush()
            continue
        sub = re.match(r"^#{2,4}\s+(.+?)\s*$", stripped)
        if sub:
            flush()
            pieces.append(("subhead", f"<h3>{inline(sub.group(1))}</h3>", (0, 0)))
            continue
        want = ("table" if stripped.startswith("|") and stripped.endswith("|")
                else "quote" if stripped.startswith(">")
                else "ordered" if ORDERED.match(stripped)
                else "list" if stripped.startswith(("- ", "* "))
                else "text")
        if want != mode:
            flush()
            mode = want
        buf.append(line)
    flush()
    return pieces


# --------------------------------------------------------------------------- the sheet
PANEL = re.compile(r"^##\s+Panel\s+(\d+)\s*:\s*(.+?)\s*$", re.M)
# The crux runs to the end of its paragraph. Matching one physical line leaves the wrapped
# remainder in the body, where it prints as an orphan fragment above the crux box.
CRUX = re.compile(r"^\*\*Crux:\*\*[ \t]*(.+?)(?=\n[ \t]*\n|\Z)", re.M | re.S)
ANSWER_KEY = re.compile(r"^#{2,3}\s*(?:The\s+)?answers?\b.*$", re.I | re.M)


def _para(text):
    return re.sub(r"\s+", " ", text).strip()


def parse_sheet(path):
    text = path.read_text(encoding="utf-8")
    title = re.search(r"^#\s+(.+?)\s*$", text, re.M)
    title = title.group(1).strip() if title else path.stem
    head_end = PANEL.search(text)
    head = text[:head_end.start()] if head_end else text
    promise, block = "", []
    for line in head.splitlines()[1:]:
        if line.startswith("#") or line.startswith("---"):
            continue
        if line.strip():
            block.append(line.strip())
        elif block:
            break
    promise = _para(" ".join(block))

    panels, marks = [], list(PANEL.finditer(text))
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        body = text[m.end():end]
        key_here = ANSWER_KEY.search(body)
        if key_here:
            body = body[:key_here.start()]
        crux = CRUX.search(body)
        body = CRUX.sub("", body)
        body = re.sub(r"^\s*---\s*$", "", body, flags=re.M)
        panels.append({"n": m.group(1), "title": m.group(2),
                       "crux": _para(crux.group(1)) if crux else "",
                       "lines": body.splitlines()})

    key = []
    key_at = ANSWER_KEY.search(text)
    if key_at:
        for line in text[key_at.end():].splitlines():
            item = re.match(r"^\s*(\d{1,3})[.)]\s+(.+?)\s*$", line)
            if item:
                key.append((item.group(1), item.group(2)))
    return title, promise, panels, key


def glossary_for(path, limit=8, width=76):
    """The day's vocabulary, read from its study notes rather than written again.

    The foot strip has to carry real terms a learner already met, so it reads the glossary table
    the study notes already carry. A day with no glossary yet simply gets no foot strip.
    """
    stem = re.match(r"^(C2_W\d{2}_(?:D\d{2}|SAT))_", path.name)
    if not stem:
        return []
    notes = list((path.parent.parent / "study-notes").glob(f"{stem.group(1)}_*.md"))
    if not notes:
        return []
    text = notes[0].read_text(encoding="utf-8", errors="replace")
    block = re.search(r"^\|\s*Term\s*\|.*?\n(?:\|.*\n)+", text, re.M)
    if not block:
        return []
    terms = []
    for row in block.group(0).splitlines()[2:]:
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        if len(cells) >= 2 and cells[0]:
            meaning = _para(cells[1])
            if len(meaning) > width:
                # Cut at a word so the strip reads as a sentence that stopped, never as a word
                # sliced down the middle.
                meaning = meaning[:width].rsplit(" ", 1)[0].rstrip(" ,;") + "..."
            terms.append((cells[0], meaning))
    return terms[:limit]


CSS = f"""
@page {{ size: A4 landscape; margin: 7mm 8mm 6mm 8mm; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: "DejaVu Sans", Verdana, sans-serif; font-size: 7pt;
        line-height: 1.3; color: {INK}; background: #FFFFFF; }}

.band {{ display: flex; align-items: flex-end; gap: 8mm; border-bottom: 1.6pt solid {ACCENT};
         padding-bottom: 1.8mm; margin-bottom: 2.6mm; }}
.band .kicker {{ font-size: 6.4pt; letter-spacing: 1pt; text-transform: uppercase;
                 color: {MUTED}; margin: 0 0 0.6mm; }}
.band h1 {{ font-size: 14pt; margin: 0; color: {ACCENT}; letter-spacing: -0.2pt;
            line-height: 1.05; }}
.band .promise {{ font-size: 7pt; color: {MUTED}; margin: 1mm 0 0; max-width: 205mm; }}
.band .stamp {{ margin-left: auto; text-align: right; font-size: 6pt; color: {MUTED};
                line-height: 1.6; white-space: nowrap; }}
.band .stamp b {{ color: {ACCENT}; font-size: 6.4pt; }}

.wrap {{ columns: 3; column-gap: 3mm; }}
.panel {{ border: 0.6pt solid {LINE}; border-radius: 1.4mm; padding: 1.8mm 2.2mm 1.6mm;
          background: #FFFFFF; break-inside: avoid; margin: 0 0 2.6mm; }}
.panel h2, .anchor h2 {{ font-size: 7.8pt; margin: 0 0 1.4mm; color: {ACCENT};
                          font-weight: bold; line-height: 1.2; }}
.anchor h2 {{ font-size: 9pt; margin-bottom: 1.8mm; }}
.panel h2 .n, .anchor h2 .n {{ display: inline-block; min-width: 4.2mm; height: 4.2mm;
                line-height: 4.2mm; text-align: center; border-radius: 50%; background: {ACCENT};
                color: #FFFFFF; font-size: 6pt; margin-right: 1.2mm; }}
.anchor h2 .n {{ min-width: 5mm; height: 5mm; line-height: 5mm; font-size: 6.6pt; }}
.panel p, .anchor p {{ margin: 0 0 1.2mm; }}
.panel > *:last-child, .anchor > *:last-child {{ margin-bottom: 0; }}
.panel ul, .anchor ul, .panel ol, .anchor ol {{ margin: 0 0 1.2mm; padding-left: 3.6mm; }}
.panel li, .anchor li {{ margin-bottom: 0.4mm; }}
.panel h3, .anchor h3 {{ font-size: 6.8pt; margin: 1.6mm 0 1mm; color: {INK};
                         text-transform: uppercase; letter-spacing: 0.4pt; }}
blockquote {{ margin: 0 0 1.2mm; padding: 1mm 1.6mm; border-left: 1.4pt solid {LINE};
              background: {BG}; color: {INK}; font-style: italic; }}

.anchor {{ column-span: all; border: 1pt solid {ACCENT}; background: {BG};
           border-radius: 1.4mm; padding: 2.2mm 2.6mm 2mm; margin: 0 0 3mm; }}
.anchor h2 .n {{ background: {INK}; }}
.anchor .split {{ display: flex; gap: 5mm; align-items: flex-start; }}
.anchor .art {{ flex: 0 0 46%; }}
.anchor .art .diagram img {{ max-height: __ANCHOR_H__mm; }}
.anchor .solo {{ text-align: center; }}
.anchor .solo .diagram {{ margin-bottom: 0; }}
.anchor .solo .diagram img {{ max-height: __ANCHOR_H__mm; max-width: 66%; }}
.anchor .said {{ flex: 1 1 auto; min-width: 0; }}
.anchor .spread {{ columns: 2; column-gap: 5mm; }}

code {{ font-family: "DejaVu Sans Mono", monospace; font-size: 6.4pt; color: {ACCENT}; }}
pre {{ font-family: "DejaVu Sans Mono", monospace; font-size: 6.1pt; line-height: 1.3;
       background: {BG}; border-left: 1.4pt solid {ACCENT}; margin: 0 0 1.4mm;
       padding: 1.2mm 1.8mm; white-space: pre-wrap; color: {INK}; }}
.anchor pre {{ background: #FFFFFF; }}
pre.nodiagram {{ border-left-color: {FAIL}; color: {MUTED}; }}

table {{ border-collapse: collapse; width: 100%; margin: 0 0 1.4mm; font-size: 6.6pt; }}
th {{ text-align: left; color: {ACCENT}; border-bottom: 0.8pt solid {ACCENT};
      padding: 0.5mm 1.4mm 0.5mm 0; font-weight: bold; }}
td {{ border-bottom: 0.4pt solid {LINE}; padding: 0.6mm 1.4mm 0.6mm 0; vertical-align: top; }}
tr:last-child td {{ border-bottom: none; }}
td:last-child, th:last-child {{ padding-right: 0; }}

.diagram {{ margin: 0 0 1.4mm; text-align: center; }}
.diagram img {{ max-width: 100%; max-height: __PANEL_H__mm; }}
.panel.wide {{ column-span: all; }}
.panel.wide .split {{ display: flex; gap: 5mm; align-items: flex-start; }}
.panel.wide .split .art {{ flex: 1 1 62%; min-width: 0; }}
.panel.wide .split .said {{ flex: 1 1 38%; min-width: 0; }}
.panel.wide .diagram img {{ max-height: __WIDE_H__mm; }}

.gap {{ display: inline-block; min-width: 15mm; border-bottom: 0.8pt solid {ACCENT};
        margin-bottom: -0.4mm; }}
.gap i {{ font-style: normal; font-size: 5.4pt; color: {ACCENT}; vertical-align: super; }}

.crux {{ margin: 1.4mm 0 0; padding: 1.1mm 1.8mm; background: {TINT}; border-radius: 0.8mm;
         font-size: 6.9pt; }}
.anchor .crux {{ background: {TINT}; }}
.crux b {{ color: {ACCENT}; }}

.foot {{ border-top: 1.2pt solid {ACCENT}; padding-top: 1.6mm; margin-top: 0.4mm;
         column-span: all; break-inside: avoid; }}
.foot h3 {{ font-size: 6.4pt; margin: 0 0 1mm; color: {ACCENT}; text-transform: uppercase;
            letter-spacing: 0.6pt; }}
.foot .terms {{ columns: 5; column-gap: 4.5mm; font-size: 6pt; }}
.foot .terms div {{ break-inside: avoid; margin-bottom: 0.7mm; }}
.foot .terms b {{ color: {INK}; }}
.foot .terms span {{ color: {MUTED}; }}

.key {{ margin-top: 2mm; border: 0.6pt dashed {MUTED}; border-radius: 1.4mm;
        padding: 1.6mm 2mm; background: {BG}; }}
.key h3 {{ font-size: 6.4pt; margin: 0 0 1mm; color: {MUTED}; text-transform: uppercase;
           letter-spacing: 0.6pt; }}
.key .items {{ columns: 6; column-gap: 4mm; font-size: 5.8pt; line-height: 1.35; }}
.key .items div {{ break-inside: avoid; margin-bottom: 0.4mm; }}
.key .items b {{ color: {ACCENT}; }}
.key code {{ font-size: 5.6pt; }}
.note {{ margin-top: 1.6mm; font-size: 6pt; color: {FAIL}; }}
"""


def build_html(path, fmt, verified, cap_mm=DIAGRAM_H_CAP_MM, tight=False):
    title, promise, panels, answers = parse_sheet(path)
    missing = []
    kicker, _, rest = title.partition(":")
    heading = rest.strip() or title
    kicker = kicker.strip() if rest else "Cheat sheet"

    # Two passes: the first measures every diagram so the column count can be chosen from the
    # widest one, the second lays the panels out inside that choice.
    body_sizes, anchor_sizes = [], []
    for i, p in enumerate(panels):
        sizes = [z for kind, _, z in render_body(p["lines"], fmt, []) if kind == "diagram"]
        (anchor_sizes if i == 0 else body_sizes).extend(sizes)
    columns = choose_columns([w for w, _ in body_sizes])
    panel_h = height_for(body_sizes, column_pt(columns), cap_mm)
    wide_h = height_for(body_sizes, (PAGE_PT - PAD_PT) * 0.62, cap_mm)
    anchor_h = height_for(anchor_sizes, (PAGE_PT - PAD_PT) * 0.66, cap_mm)
    css = (CSS.replace("__PANEL_H__", f"{panel_h:.0f}")
              .replace("__WIDE_H__", f"{max(wide_h, panel_h):.0f}")
              .replace("__ANCHOR_H__", f"{anchor_h:.0f}"))
    if tight:
        # A sheet that spills only its last strip is not a sheet that needs a second page. The
        # leading closes by a hair and the vocabulary strip carries its six most useful terms.
        css = (css.replace("line-height: 1.3;", "line-height: 1.22;")
                  .replace("margin: 0 0 2.6mm;", "margin: 0 0 2mm;")
                  .replace("padding: 1.8mm 2.2mm 1.6mm;", "padding: 1.5mm 2mm 1.3mm;"))
    PANEL_H_PT = panel_h * MM
    WIDE_H_PT = max(wide_h, panel_h) * MM
    ANCHOR_SOLO_H_PT = ANCHOR_ART_H_PT = anchor_h * MM

    blocks, n_diagrams, wide, cramped = [], 0, [], []
    for i, p in enumerate(panels):
        pieces = render_body(p["lines"], fmt, missing)
        n_diagrams += sum(1 for kind, *_ in pieces if kind == "diagram")
        crux = (f'<div class="crux"><b>Crux.</b> {inline(p["crux"])}</div>' if p["crux"] else "")
        head = f'<h2><span class="n">{p["n"]}</span>{inline(p["title"])}</h2>'
        if i == 0:
            art = "".join(h for kind, h, _ in pieces if kind == "diagram")
            said = "".join(h for kind, h, _ in pieces if kind != "diagram")
            box = ((PAGE_PT - PAD_PT) * (0.46 if said else 0.66),
                   ANCHOR_ART_H_PT if said else ANCHOR_SOLO_H_PT)
            for kind, _, size in pieces:
                if kind == "diagram" and label_pt(size, box) < MIN_LABEL_PT:
                    cramped.append((p["n"], size, label_pt(size, box)))
            if art and said:
                inner = (f'<div class="split"><div class="art">{art}</div>'
                         f'<div class="said">{said}{crux}</div></div>')
            elif art:
                # Nothing to set beside the picture, so the picture takes the whole band and
                # the crux runs under it rather than leaving half the width empty.
                inner = f'<div class="solo">{art}</div>{crux}'
            else:
                inner = f'<div class="spread">{said}</div>{crux}'
            blocks.append(f'<section class="anchor">{head}{inner}</section>')
        else:
            widest = max([z[0] for kind, _, z in pieces if kind == "diagram"], default=0)
            goes_wide = widest > max_width_px(columns)
            box = ((PAGE_PT - PAD_PT) * 0.62 if goes_wide else column_pt(columns),
                   WIDE_H_PT if goes_wide else PANEL_H_PT)
            for kind, _, size in pieces:
                if kind == "diagram" and label_pt(size, box) < MIN_LABEL_PT:
                    cramped.append((p["n"], size, label_pt(size, box)))
            if goes_wide:
                wide.append(p["n"])
                art = "".join(h for kind, h, _ in pieces if kind == "diagram")
                said = "".join(h for kind, h, _ in pieces if kind != "diagram")
                blocks.append(f'<section class="panel wide">{head}<div class="split">'
                              f'<div class="art">{art}</div>'
                              f'<div class="said">{said}{crux}</div></div></section>')
            else:
                blocks.append(f'<section class="panel">{head}'
                              f'{"".join(h for _, h, _ in pieces)}{crux}</section>')

    terms = glossary_for(path, limit=6 if tight else 8)
    foot = ""
    if terms:
        cells = "".join(f"<div><b>{inline(t)}</b> <span>{inline(m)}</span></div>"
                        for t, m in terms)
        foot = (f'<div class="foot"><h3>The words on this sheet</h3>'
                f'<div class="terms">{cells}</div></div>')

    key = ""
    if answers:
        items = "".join(f"<div><b>{n}</b> {inline(a)}</div>" for n, a in answers)
        key = (f'<div class="key"><h3>Answers, covered until the panels are full</h3>'
               f'<div class="items">{items}</div></div>')

    note = ""
    if missing:
        note = (f'<p class="note">{len(missing)} diagram(s) did not render and their source is '
                f'printed instead.</p>')

    stamp = (f'<div class="stamp"><b>{html.escape(path.stem)}</b><br>Verified {verified}<br>'
             f'{len(panels)} panels, {n_diagrams} diagrams</div>')
    page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>{html.escape(title)}</title>
<style>{css}</style></head><body>
<div class="band"><div><p class="kicker">{html.escape(kicker)}</p>
<h1>{html.escape(heading)}</h1>
<p class="promise">{inline(promise)}</p></div>{stamp}</div>
<div class="wrap" style="columns: {columns}">{''.join(blocks)}{foot}</div>
{key}{note}
</body></html>
"""
    return page, missing, len(panels), n_diagrams, wide, columns, cramped


def last_page_fill(pdf_path):
    """How much of the last page carries ink, as a fraction of its height.

    A sheet that spills one block onto a second page is worse than a denser first page, and
    nothing in the layout knows that. Rasterising the last page at a low resolution and finding
    the lowest row with ink on it answers the question directly.
    """
    try:
        from PIL import Image
    except ImportError:
        return 1.0
    out = pathlib.Path(tempfile.mkdtemp(prefix="c2_fill_")) / "p"
    r = subprocess.run(["pdftoppm", "-jpeg", "-r", "36", "-l", "9999", str(pdf_path), str(out)],
                       capture_output=True)
    pages = sorted(out.parent.glob("p-*.jpg"))
    if r.returncode != 0 or not pages:
        return 1.0
    im = Image.open(pages[-1]).convert("L")
    w, h = im.size
    px = im.load()
    for y in range(h - 1, -1, -1):
        if any(px[x, y] < 245 for x in range(0, w, 3)):
            return (y + 1) / h
    return 0.0


def build(path, fmt, verified, png_dir=None, max_pages=1):
    out_pdf = path.with_suffix(".pdf")
    CACHE.mkdir(parents=True, exist_ok=True)
    try:
        from weasyprint import HTML
    except ImportError:
        print(f"INFO  {path.name}: weasyprint is not installed, so nothing was rendered. "
              f"Install it with pip install weasyprint.")
        return 1

    # Larger diagrams read better and cost height, so the caps are tried from generous down and
    # the first layout that lands inside the page budget with a full last page wins. Anything
    # that would print a label too small to read is never a candidate.
    def score(c):
        """Readable first, then compact, then a full last page, then the larger diagrams."""
        return (not c["cramped"], -min(c["pages"], 9),
                1.0 if c["pages"] == 1 else round(c["fill"], 2),
                0 if c["tight"] else 1, c["cap"])

    best = None
    plans = [(c, False) for c in (DIAGRAM_H_CAP_MM, 54, 48, 44, 40, 36)]
    plans += [(c, True) for c in (DIAGRAM_H_CAP_MM, 48, 40, 36)]
    for cap, tight in plans:
        page, missing, n_panels, n_diagrams, wide, columns, cramped = build_html(
            path, fmt, verified, cap, tight)
        doc = HTML(string=page, base_url=str(path.parent)).render()
        doc.write_pdf(str(out_pdf))
        pages, fill = len(doc.pages), last_page_fill(out_pdf)
        cand = dict(page=page, missing=missing, n_panels=n_panels, n_diagrams=n_diagrams,
                    wide=wide, columns=columns, cramped=cramped, pages=pages, fill=fill,
                    cap=cap, tight=tight)
        if best is None or score(cand) > score(best):
            best = cand
        if not n_diagrams:
            break
        if not cramped and pages <= max_pages and (pages == 1 or fill >= 0.45):
            break
    page, missing, n_panels = best["page"], best["missing"], best["n_panels"]
    n_diagrams, wide, columns = best["n_diagrams"], best["wide"], best["columns"]
    cramped, pages = best["cramped"], best["pages"]
    (CACHE / (path.stem + ".html")).write_text(page, encoding="utf-8")
    HTML(string=page, base_url=str(path.parent)).render().write_pdf(str(out_pdf))
    fails = 0
    if pages > max_pages:
        print(f"FAIL  {out_pdf.name}: {pages} pages against {max_pages} allowed. Cut a block or "
              f"move it to the day's study notes rather than shrinking the type.")
        fails += 1
    if missing:
        print(f"FAIL  {out_pdf.name}: {len(missing)} diagrams did not render ({', '.join(missing)})")
        fails += 1
    for n, (w_px, h_px), pt in cramped:
        print(f"FAIL  {out_pdf.name} panel {n}: its diagram is {w_px:.0f} by {h_px:.0f} and prints "
              f"its labels at {pt:.1f}pt, under the {MIN_LABEL_PT}pt a person reads standing up. "
              f"Reshape it shorter or narrower rather than letting the page shrink it.")
    fails += len(cramped)
    if n_diagrams == 0:
        print(f"FAIL  {out_pdf.name}: no diagram anywhere, so the sheet has no anchor to redraw "
              f"from memory.")
        fails += 1
    widened = f", panels {', '.join(wide)} widened" if wide else ""
    fill = f", last page {best['fill'] * 100:.0f}% full" if pages > 1 else ""
    print(f"      {out_pdf.name}: {n_panels} panels, {n_diagrams} diagrams, {columns} columns, "
          f"{pages} page(s), {out_pdf.stat().st_size // 1024} KB{widened}{fill}")
    if png_dir:
        pathlib.Path(png_dir).mkdir(parents=True, exist_ok=True)
        subprocess.run(["pdftoppm", "-jpeg", "-r", "110", str(out_pdf),
                        str(pathlib.Path(png_dir) / path.stem)], capture_output=True)
    return fails


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("targets", nargs="+", help="a cheat sheet .md, or a folder to walk")
    ap.add_argument("--format", default="svg", choices=("svg", "png"),
                    help="how mermaid fences are rendered into the sheet")
    ap.add_argument("--verified", default=None,
                    help="the verification date printed in the title band, as 03 Sep 2026")
    ap.add_argument("--png", default=None, help="also rasterise each sheet into this folder")
    ap.add_argument("--max-pages", type=int, default=2,
                    help="pages a sheet may take before it fails. Two is the default, because a "
                         "sheet of diagrams prints double sided rather than shrinking its labels")
    a = ap.parse_args()

    verified = a.verified or __import__("datetime").date.today().strftime("%d %b %Y")
    sheets = []
    for t in a.targets:
        p = pathlib.Path(t)
        if p.is_dir():
            sheets += sorted(q for q in p.rglob("*.md") if q.parent.name == "cheatsheets")
        else:
            sheets.append(p)
    if not sheets:
        print("INFO  no cheat sheets found")
        sys.exit(0)

    if not shutil.which("mmdc"):
        print("INFO  mermaid-cli is not installed, so any diagram falls back to its source. "
              "Install it with npm install -g @mermaid-js/mermaid-cli")

    fails = sum(build(s, a.format, verified, a.png, a.max_pages) for s in sheets)
    print(f"      {len(sheets)} sheets built")
    print("RESULT:", "FAIL" if fails else "PASS", f"({fails} failures)")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# scripts/build_cheatsheet.py content/W01/D1/cheatsheets/C2_W01_D01_kernel_records_STUDENT.md
#     Writes the .pdf beside the .md, reports panels, diagrams, page count and size, and exits 0
#     when the sheet fits one landscape page with every diagram rendered.
# scripts/build_cheatsheet.py content/W01 --png /tmp/sheets
#     Builds every sheet under the week and rasterises each one so a person can look at it.
# scripts/build_cheatsheet.py <a sheet with no mermaid fence>
#     FAIL saying the sheet has no anchor to redraw from memory, and exit 1.
# scripts/build_cheatsheet.py <sheet.md> in a session with no mermaid-cli
#     One INFO line, then a FAIL per sheet whose diagrams fell back to their source, and exit 1.
# scripts/build_cheatsheet.py <a sheet with twelve panels>
#     FAIL naming the page count, because a sheet is defined by what it leaves out.
