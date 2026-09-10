"""The shared helper every teaching notebook in this repository imports.

One module, so a diagram, a check and a table look the same in Week 1 and in Week 15, and so no
notebook carries fifty lines of plumbing above its first idea.

Import it with the block documented in every notebook, which walks up from the notebook's own
folder until it finds scripts/c2kit.py:

    import sys, pathlib
    here = pathlib.Path.cwd()
    for parent in [here, *here.parents]:
        if (parent / "scripts" / "c2kit.py").exists():
            sys.path.insert(0, str(parent / "scripts")); break
    import c2kit as kit

What it holds: loaders for the day's data from ../data/, check and check_summary, table, a trace
viewer, and nine diagram builders that render SVG from a code cell so the picture saves into the
notebook and shows on GitHub.

No network, no browser storage, no keys, and no side effects on import.
"""
import csv
import html as _html
import json
import pathlib
import re

from IPython.display import HTML, display

# The palette scripts/build_deck.py uses, so a diagram in a notebook and a diagram on a slide are
# recognisably the same drawing.
INK = "#1C1C1A"
MUTED = "#5F6360"
ACCENT = "#2B4A7D"
TINT = "#E4ECF7"
BG = "#F7F7F5"
LINE = "#C9C9C2"
PASS_COLOUR = "#1F6F4A"
FAIL_COLOUR = "#8A3D3D"
FONT = "system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

_TALLY = {"pass": 0, "fail": 0}


# --------------------------------------------------------------------------- data
def data_dir(start=None):
    """The day's data folder, found from wherever the notebook is running.

    A notebook runs with its own folder as the working directory, so ../data is the normal answer.
    Running from the day folder or the repository root also works, which is what lets the same
    notebook execute under nbconvert and under a learner's Run All.
    """
    here = pathlib.Path(start or pathlib.Path.cwd()).resolve()
    for candidate in [here / "data", here.parent / "data", *[p / "data" for p in here.parents]]:
        if candidate.is_dir() and any(candidate.iterdir()):
            return candidate
    raise FileNotFoundError(
        "No data folder found from " + str(here) + ". A day's data lives in its data/ folder and "
        "is written by data/generate_client_zero.py, never by hand.")


def _resolve(name, start=None):
    path = pathlib.Path(name)
    if path.is_file():
        return path
    found = data_dir(start) / pathlib.Path(name).name
    if not found.is_file():
        raise FileNotFoundError(
            f"{found} is missing. Regenerate it with: python3 data/generate_client_zero.py "
            f"--version <version> --out <day folder>/data --stem <stem>")
    return found


def load_records(name="C2_W01_D01_orders_STUDENT.py", start=None):
    """The day's records from the generated Python literal, as a list of dictionaries."""
    text = _resolve(name, start).read_text(encoding="utf-8")
    scope = {}
    exec(compile(text, str(name), "exec"), scope)  # the file is a generated literal, nothing else
    for key in ("RECORDS", "records", "ORDERS", "orders"):
        if key in scope:
            return scope[key]
    raise ValueError(f"{name} defines no RECORDS list")


def load_csv(name, start=None):
    """A generated CSV as a list of dictionaries, every value left as the text the file holds."""
    with _resolve(name, start).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_json(name, start=None):
    return json.loads(_resolve(name, start).read_text(encoding="utf-8"))


def read_text(name, start=None):
    return _resolve(name, start).read_text(encoding="utf-8")


# --------------------------------------------------------------------------- checks
def check(label, condition, detail=""):
    """Print PASS or FAIL without raising, so one failing check never stops a class.

    Assert on the shape of what happened: a count, a length, a type, a key's presence, a
    reconciliation between two numbers. A check that compares a printed sentence breaks the first
    time the wording improves. It returns nothing, so a CHECK cell ending on a check prints the
    check rather than a bare True.
    """
    ok = bool(condition)
    _TALLY["pass" if ok else "fail"] += 1
    word, colour = ("PASS", PASS_COLOUR) if ok else ("FAIL", FAIL_COLOUR)
    extra = (f'<span style="color:{MUTED}"> &middot; {_html.escape(str(detail))}</span>'
             if detail else "")
    display(HTML(
        f'<div class="c2k-check c2k-{word.lower()}" style="font:14px {FONT};margin:2px 0">'
        f'<span style="display:inline-block;min-width:52px;font-weight:700;color:{colour}">'
        f'{word}</span><span style="color:{INK}">{_html.escape(str(label))}</span>{extra}</div>'))


def check_summary():
    """The running totals, printed once at the end of every notebook."""
    passed, failed = _TALLY["pass"], _TALLY["fail"]
    colour = FAIL_COLOUR if failed else PASS_COLOUR
    word = "FAIL" if failed else "PASS"
    display(HTML(
        f'<div class="c2k-check c2k-{word.lower()}" style="font:14px {FONT};margin-top:10px;'
        f'padding:8px 12px;background:{BG};border-left:3px solid {colour}">'
        f'<b style="color:{colour}">{word}</b> &middot; {passed} checks passed and {failed} failed '
        f'in this notebook.</div>'))


def reset_checks():
    _TALLY["pass"] = _TALLY["fail"] = 0


# --------------------------------------------------------------------------- tables and traces
def table(headers, rows, caption=""):
    """Any result worth reading as a grid, in the deck palette rather than as a print."""
    head = "".join(f'<th style="text-align:left;padding:6px 12px 6px 0;border-bottom:1px solid '
                   f'{ACCENT};color:{ACCENT};font-weight:700">{_html.escape(str(h))}</th>'
                   for h in headers)
    body = "".join(
        "<tr>" + "".join(
            f'<td style="padding:5px 12px 5px 0;border-bottom:1px solid {LINE};color:{INK};'
            f'vertical-align:top">{_html.escape(str(c))}</td>' for c in row) + "</tr>"
        for row in rows)
    cap = (f'<caption style="text-align:left;color:{MUTED};font-size:13px;padding-bottom:6px">'
           f'{_html.escape(caption)}</caption>') if caption else ""
    display(HTML(f'<table style="border-collapse:collapse;font:14px {FONT};margin:6px 0">'
                 f'{cap}<thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'))


def show_trace(steps, title=""):
    """A run's steps in order, each with what it did and what came back."""
    rows = "".join(
        f'<div style="display:flex;gap:10px;padding:5px 0;border-bottom:1px solid {LINE}">'
        f'<span style="color:{ACCENT};font:700 13px {MONO};min-width:26px">{n:02d}</span>'
        f'<span style="color:{INK};font:13px {MONO};min-width:190px">{_html.escape(str(what))}</span>'
        f'<span style="color:{MUTED};font:13px {FONT}">{_html.escape(str(got))}</span></div>'
        for n, (what, got) in enumerate(steps, start=1))
    head = (f'<div style="color:{ACCENT};font:700 13px {FONT};margin-bottom:4px">'
            f'{_html.escape(title)}</div>') if title else ""
    display(HTML(f'<div style="margin:6px 0">{head}{rows}</div>'))


def show_messages(messages, title=""):
    """A message exchange, one card per turn, for any topic that has a caller and a callee."""
    cards = "".join(
        f'<div style="margin:5px 0;padding:8px 11px;background:{TINT if i % 2 == 0 else "#FFFFFF"};'
        f'border:1px solid {LINE};border-radius:7px">'
        f'<div style="color:{ACCENT};font:700 12px {FONT};text-transform:uppercase;'
        f'letter-spacing:.06em">{_html.escape(str(who))}</div>'
        f'<div style="color:{INK};font:14px {FONT};white-space:pre-wrap">{_html.escape(str(said))}'
        f'</div></div>'
        for i, (who, said) in enumerate(messages))
    head = (f'<div style="color:{ACCENT};font:700 13px {FONT};margin-bottom:4px">'
            f'{_html.escape(title)}</div>') if title else ""
    display(HTML(f'<div style="max-width:760px">{head}{cards}</div>'))


# --------------------------------------------------------------------------- diagram builders
def _svg(width, height, body, title=""):
    cap = (f'<text x="{width / 2:.0f}" y="{height - 5}" text-anchor="middle" fill="{MUTED}" '
           f'font-family="{FONT}" font-size="12">{_html.escape(title)}</text>') if title else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width:.0f}" height="{height:.0f}" '
            f'viewBox="0 0 {width:.0f} {height:.0f}" role="img">'
            f'<rect width="{width:.0f}" height="{height:.0f}" fill="{BG}"/>{body}{cap}</svg>')


def _wrap(text, per_line):
    words, lines, line = str(text).split(), [], ""
    for w in words:
        if len(line) + len(w) + 1 > per_line and line:
            lines.append(line)
            line = w
        else:
            line = f"{line} {w}".strip()
    if line:
        lines.append(line)
    return lines or [""]


def _box(x, y, w, h, text, lit=False, size=12, radius=7):
    fill = TINT if lit else "#FFFFFF"
    stroke = ACCENT
    weight = 700 if lit else 400
    lines = _wrap(text, max(8, int(w / (size * 0.55))))
    top = y + h / 2 - (len(lines) - 1) * (size + 3) / 2 + size * 0.35
    label = "".join(
        f'<text x="{x + w / 2:.0f}" y="{top + i * (size + 3):.0f}" text-anchor="middle" '
        f'fill="{INK}" font-family="{FONT}" font-size="{size}" font-weight="{weight}">'
        f'{_html.escape(l)}</text>' for i, l in enumerate(lines))
    return (f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" rx="{radius}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{2 if lit else 1}"/>{label}')


def _arrow(x1, y1, x2, y2, label=""):
    mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
    cap = (f'<text x="{mid_x:.0f}" y="{mid_y - 6:.0f}" text-anchor="middle" fill="{MUTED}" '
           f'font-family="{FONT}" font-size="11">{_html.escape(label)}</text>') if label else ""
    return (f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{ACCENT}" '
            f'stroke-width="1.4" marker-end="url(#c2kArrow)"/>{cap}')


_DEFS = (f'<defs><marker id="c2kArrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
         f'markerHeight="6" orient="auto-start-reverse">'
         f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{ACCENT}"/></marker></defs>')


def _emit(svg, show=True):
    """Draw the diagram, or hand back its SVG when a composer is going to place it."""
    if show:
        display(HTML(svg))
        return None
    return svg


def ladder(items, lit=None, title="", show=True):
    """The day's notebooks or stages in order, with the current one lit."""
    w, h, gap = 200, 44, 12
    height = len(items) * (h + gap) + 34
    body = [_DEFS]
    for i, item in enumerate(items):
        y = i * (h + gap) + 10
        body.append(_box(14, y, w, h, f"{i + 1}. {item}", lit=(i == lit)))
        if i:
            body.append(_arrow(14 + w / 2, y - gap, 14 + w / 2, y))
    return _emit(_svg(w + 28, height, "".join(body), title), show)


def flow(steps, lit=None, title="", show=True):
    """Steps left to right, with one highlighted."""
    w, h, gap = 168, 58, 30
    width = len(steps) * w + (len(steps) - 1) * gap + 28
    body = [_DEFS]
    for i, step in enumerate(steps):
        x = 14 + i * (w + gap)
        body.append(_box(x, 12, w, h, step, lit=(i == lit)))
        if i:
            body.append(_arrow(x - gap, 12 + h / 2, x, 12 + h / 2))
    return _emit(_svg(width, h + 46, "".join(body), title), show)


def vflow(steps, lit=None, title="", show=True):
    """The same, top to bottom, for a decision path or a longer sequence."""
    w, h, gap = 300, 46, 22
    body = [_DEFS]
    for i, step in enumerate(steps):
        y = 12 + i * (h + gap)
        body.append(_box(14, y, w, h, step, lit=(i == lit)))
        if i:
            body.append(_arrow(14 + w / 2, y - gap, 14 + w / 2, y))
    return _emit(_svg(w + 28, len(steps) * (h + gap) + 30, "".join(body), title), show)


def stack(layers, lit=None, title="", show=True):
    """Layers bottom to top, for a concept with layers rather than steps."""
    w, h, gap = 320, 44, 8
    body = []
    for i, layer in enumerate(layers):
        y = 12 + (len(layers) - 1 - i) * (h + gap)
        body.append(_box(14, y, w, h, layer, lit=(i == lit)))
    return _emit(_svg(w + 28, len(layers) * (h + gap) + 30, "".join(body), title), show)


def sequence(lanes, messages, title="", show=True):
    """Messages across named lanes, drawn from the run that actually happened."""
    lane_w, top, step = 190, 46, 44
    width = len(lanes) * lane_w + 28
    height = top + max(1, len(messages)) * step + 34
    body = [_DEFS]
    for i, lane in enumerate(lanes):
        x = 14 + i * lane_w
        body.append(_box(x + 10, 10, lane_w - 20, 30, lane, lit=True, size=12, radius=5))
        body.append(f'<line x1="{x + lane_w / 2:.0f}" y1="42" x2="{x + lane_w / 2:.0f}" '
                    f'y2="{height - 28}" stroke="{LINE}" stroke-width="1"/>')
    for n, (src, dst, text) in enumerate(messages):
        y = top + n * step + 20
        x1 = 14 + lanes.index(src) * lane_w + lane_w / 2
        x2 = 14 + lanes.index(dst) * lane_w + lane_w / 2
        body.append(_arrow(x1, y, x2, y, text))
    return _emit(_svg(width, height, "".join(body), title), show)


def tree(node, taken=(), title="", show=True):
    """A decision tree from nested dicts, with the branch actually taken marked.

    node is {"label": ..., "branches": [(edge_label, child_node), ...]}, and taken is the list of
    edge labels the run followed.
    """
    levels = []

    def walk(n, depth, path):
        while len(levels) <= depth:
            levels.append([])
        entry = {"label": n["label"], "path": path, "children": []}
        levels[depth].append(entry)
        for edge, child in n.get("branches", []):
            entry["children"].append((edge, walk(child, depth + 1, path + [edge])))
        return entry

    walk(node, 0, [])
    w, h, gap_x, gap_y = 190, 50, 22, 40
    width = max(len(l) for l in levels) * (w + gap_x) + 28
    height = len(levels) * (h + gap_y) + 30
    body, coords = [_DEFS], {}
    for d, level in enumerate(levels):
        span = len(level) * (w + gap_x) - gap_x
        x0 = (width - span) / 2
        for i, entry in enumerate(level):
            x, y = x0 + i * (w + gap_x), 12 + d * (h + gap_y)
            on = list(taken)[:len(entry["path"])] == entry["path"]
            coords[id(entry)] = (x + w / 2, y, x + w / 2, y + h)
            body.append(_box(x, y, w, h, entry["label"], lit=on))
    for level in levels:
        for entry in level:
            _, _, bx, by = coords[id(entry)]
            for edge, child in entry["children"]:
                cx, cy, _, _ = coords[id(child)]
                body.append(_arrow(bx, by, cx, cy, edge))
    return _emit(_svg(width, height, "".join(body), title), show)


def matrix(row_labels, col_labels, cells, title="", show=True):
    """A two-axis grid, for a choice with two independent dimensions."""
    cw, ch, lw = 190, 58, 150
    width = lw + len(col_labels) * cw + 28
    height = 40 + len(row_labels) * ch + 30
    body = []
    for j, col in enumerate(col_labels):
        body.append(f'<text x="{14 + lw + j * cw + cw / 2:.0f}" y="28" text-anchor="middle" '
                    f'fill="{ACCENT}" font-family="{FONT}" font-size="12" font-weight="700">'
                    f'{_html.escape(str(col))}</text>')
    for i, row in enumerate(row_labels):
        y = 40 + i * ch
        body.append(f'<text x="14" y="{y + ch / 2 + 4:.0f}" fill="{ACCENT}" font-family="{FONT}" '
                    f'font-size="12" font-weight="700">{_html.escape(str(row))}</text>')
        for j in range(len(col_labels)):
            value = cells[i][j] if i < len(cells) and j < len(cells[i]) else ""
            body.append(_box(14 + lw + j * cw + 4, y + 4, cw - 8, ch - 8, value, size=12, radius=5))
    return _emit(_svg(width, height, "".join(body), title), show)


def decision_ladder(options, cut_at=None, title="", show=True):
    """Options in escalating order with the cut line marked, for a choice that is a threshold."""
    w, h, gap = 340, 44, 10
    height = len(options) * (h + gap) + 30
    body = []
    for i, option in enumerate(options):
        y = 12 + (len(options) - 1 - i) * (h + gap)
        body.append(_box(14, y, w, h, option, lit=(i == cut_at)))
        if cut_at is not None and i == cut_at:
            body.append(f'<line x1="10" y1="{y - gap / 2:.0f}" x2="{w + 22}" '
                        f'y2="{y - gap / 2:.0f}" stroke="{FAIL_COLOUR}" stroke-width="1.5" '
                        f'stroke-dasharray="5 4"/>'
                        f'<text x="{w + 24}" y="{y - gap / 2 + 4:.0f}" fill="{FAIL_COLOUR}" '
                        f'font-family="{FONT}" font-size="11">stop here</text>')
    return _emit(_svg(w + 120, height, "".join(body), title), show)


def side_by_side(*svgs, gap=26, show=True):
    """Two or more diagrams composed horizontally, which is the opening MAP cell's shape."""
    parts = []
    for svg in svgs:
        m = re.search(r'width="(\d+)" height="(\d+)"', svg)
        parts.append((svg, int(m.group(1)), int(m.group(2))) if m else (svg, 0, 0))
    body = f'<div style="display:flex;gap:{gap}px;align-items:flex-start;flex-wrap:wrap">' + \
           "".join(f"<div>{svg}</div>" for svg, _, _ in parts) + "</div>"
    if show:
        display(HTML(body))
        return None
    return body


# Test inputs and expected outcomes
# --------------------------------
# kit.check("44 rows survive", len(clean) == 44, f"got {len(clean)}")
#     Prints a green PASS line with the detail beside it and adds one to the tally.
# kit.check("44 rows survive", len(clean) == 43)
#     Prints a red FAIL line and does not raise, so the rest of the notebook runs.
# kit.check_summary()
#     Prints "12 checks passed and 0 failed in this notebook".
# kit.flow(["read", "profile", "decide"], lit=1)
#     Renders three boxes left to right with the middle one tinted and bold, as saved SVG.
# kit.side_by_side(kit.ladder(["a", "b"], lit=0, show=False), kit.flow(["x"], show=False))
#     Renders both diagrams in one row. Pass show=False to a builder to compose rather than draw.
# kit.load_records() from a notebooks/ folder whose ../data holds the generated orders file
#     Returns the 30 dictionaries. With the file missing it raises, naming the generator command.
