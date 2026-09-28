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

What it holds: loaders for the day's data from ../data/, check and check_summary, table and stats,
expect_error for a failure staged on purpose, a trace viewer, and the diagram builders, which render
SVG from a code cell so the picture saves into the notebook and shows on GitHub. The builders are
ladder, flow, vflow, stack, sequence, tree, driver_tree, matrix, decision_ladder, equation, strip,
bars and side_by_side.

The colours come from scripts/brand.py, the same values the decks and the cheat sheets read, so a
tree in a notebook and the tree on the slide are the same drawing in the same violet.

No network, no browser storage, no keys, and no side effects on import.
"""
import csv
import html as _html
import decimal
import linecache
import os
import json
import pathlib
import re

from IPython.display import HTML, display

import brand

# The palette, read from the brand module rather than restated, so it cannot drift from the decks.
INK = brand.INK
NIGHT = brand.NIGHT
MUTED = brand.MUTED
ACCENT = brand.VIOLET
TINT = brand.TINT
BG = brand.SURFACE
LINE = brand.LINE
LILAC = brand.LILAC
WHITE = brand.WHITE
PASS_COLOUR = brand.GREEN
FAIL_COLOUR = brand.ROSE
FONT = "Calibri, Carlito, 'Segoe UI', system-ui, -apple-system, Roboto, sans-serif"
SERIF = "Georgia, 'DejaVu Serif', serif"
MONO = "Consolas, ui-monospace, SFMono-Regular, Menlo, monospace"

# How a box is drawn, by what it means. The deck's mermaid theme uses the same five looks.
KINDS = {
    "plain": (TINT, ACCENT, 1.2, INK, ""),
    "lit": (INK, INK, 1.2, WHITE, ""),
    "known": (TINT, ACCENT, 2.6, INK, ""),
    "unknown": (WHITE, "#B8B2D6", 1.3, MUTED, "5 4"),
    "bad": (brand.ROSE_TINT, brand.ROSE, 1.6, INK, ""),
    "good": (brand.GREEN_TINT, brand.GREEN, 1.6, INK, ""),
}

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
# --------------------------------------------------------------------------- the warehouse
# Week 2 onwards, the day queries a Postgres database rather than reading a file. The connection
# settings come from the environment, so the same notebook runs in a Codespace, on a laptop and in
# a build session without a line changing.
WAREHOUSE = {
    "host": os.environ.get("PGHOST", "localhost"),
    "port": os.environ.get("PGPORT", "5432"),
    "user": os.environ.get("PGUSER", "postgres"),
    "password": os.environ.get("PGPASSWORD", "postgres"),
    "dbname": os.environ.get("PGDATABASE", "kalpa"),
}


def connect():
    """Open a connection to the Kalpa warehouse, and say plainly what to do when there is none."""
    try:
        import psycopg2
    except ImportError:
        raise SystemExit("The psycopg2 driver is missing. Run: pip install psycopg2-binary")
    try:
        return psycopg2.connect(**WAREHOUSE)
    except Exception as e:
        raise SystemExit(
            f"No warehouse answered at {WAREHOUSE['host']}:{WAREHOUSE['port']}. "
            f"Run bash .devcontainer/load_warehouse.sh to build it.\n  {e}")


def engine():
    """A SQLAlchemy engine for the warehouse, which is what pandas.read_sql wants.

    A raw driver connection works and makes pandas warn on every call, and a warning printed
    beside every table in a teaching notebook trains people to ignore warnings.
    """
    try:
        from sqlalchemy import create_engine
    except ImportError:
        raise SystemExit("SQLAlchemy is missing. Run: pip install 'sqlalchemy>=2'")
    w = WAREHOUSE
    return create_engine(
        f"postgresql+psycopg2://{w['user']}:{w['password']}@{w['host']}:{w['port']}/{w['dbname']}")


def sql(query, params=None, conn=None):
    """Run a query and return its rows as a list of dicts, which prints and indexes readably."""
    own = conn is None
    conn = conn or connect()
    try:
        with conn.cursor() as cur:
            cur.execute(query, params)
            if cur.description is None:
                return []
            cols = [d[0] for d in cur.description]
            return [dict(zip(cols, row)) for row in cur.fetchall()]
    finally:
        if own:
            conn.close()


def sql_table(query, caption="", params=None, conn=None, limit=12):
    """Run a query and render its first rows as the kit's table, so a notebook reads as a document."""
    rows = sql(query, params, conn)
    if not rows:
        return table(["result"], [["no rows"]], caption)
    headers = list(rows[0])
    body = [[_cell(r[h]) for h in headers] for r in rows[:limit]]
    if len(rows) > limit:
        body.append(["..." for _ in headers])
    return table(headers, body, caption or f"{len(rows)} rows")


def _cell(v):
    if isinstance(v, decimal.Decimal):
        v = int(v) if v == v.to_integral_value() else float(v)
    if isinstance(v, int) and abs(v) >= 10000:
        return f"{v:,}"
    return "" if v is None else str(v)


def rupees(n):
    """Rs with Indian digit grouping, which is how every Kalpa number is read aloud."""
    n = int(n)
    sign, n = ("-", -n) if n < 0 else ("", n)
    s = str(n)
    if len(s) <= 3:
        return f"{sign}Rs {s}"
    head, tail = s[:-3], s[-3:]
    parts = []
    while len(head) > 2:
        parts.insert(0, head[-2:])
        head = head[:-2]
    if head:
        parts.insert(0, head)
    return f"{sign}Rs {','.join(parts)},{tail}"


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
    word, colour, ground = (("PASS", PASS_COLOUR, brand.GREEN_TINT) if ok
                            else ("FAIL", FAIL_COLOUR, brand.ROSE_TINT))
    extra = (f'<span style="color:{MUTED}"> &middot; {_html.escape(str(detail))}</span>'
             if detail else "")
    display(HTML(
        f'<div class="c2k-check c2k-{word.lower()}" style="font:14px {FONT};margin:3px 0;'
        f'padding:4px 10px;background:{ground};border-left:3px solid {colour};border-radius:4px">'
        f'<span style="display:inline-block;min-width:48px;font-weight:700;color:{colour};'
        f'letter-spacing:.06em">{word}</span><span style="color:{INK}">'
        f'{_html.escape(str(label))}</span>{extra}</div>'))


def check_summary():
    """The running totals, printed once at the end of every notebook."""
    passed, failed = _TALLY["pass"], _TALLY["fail"]
    colour = FAIL_COLOUR if failed else PASS_COLOUR
    word = "FAIL" if failed else "PASS"
    display(HTML(
        f'<div class="c2k-check c2k-{word.lower()}" style="font:15px {FONT};margin-top:10px;'
        f'padding:10px 14px;background:{BG};border-left:4px solid {colour};border-radius:4px">'
        f'<b style="color:{colour}">{word}</b> &middot; {passed} checks passed and {failed} failed '
        f'in this notebook.</div>'))


def reset_checks():
    _TALLY["pass"] = _TALLY["fail"] = 0


class expect_error:
    """Run a block that is meant to fail, show the error Jupyter would print, and carry on.

    A notebook that stages a failure has to keep running for Run All and for the verification
    gate, so the error is caught here and its last line shown exactly as Jupyter prints it, with
    the line that raised it. The name and message stay on the object for the checks that follow:

        with kit.expect_error() as err:
            revenue += order["amount"]
        kit.check("the loop stopped on a type error", err.name == "TypeError")

    A block that runs clean is reported as such, so a fix that removed the failure shows up.
    """

    def __init__(self):
        self.name = None
        self.message = None
        self.line = None

    def __enter__(self):
        return self

    def __exit__(self, kind, exc, tb):
        if exc is None:
            display(HTML(
                f'<div style="font:14px {FONT};padding:6px 12px;background:{brand.GREEN_TINT};'
                f'border-left:3px solid {PASS_COLOUR};border-radius:4px;color:{INK}">'
                f'No error: the block ran clean.</div>'))
            return False
        self.name, self.message = kind.__name__, str(exc)
        while tb is not None and tb.tb_next is not None:
            tb = tb.tb_next
        if tb is not None:
            self.line = linecache.getline(tb.tb_frame.f_code.co_filename, tb.tb_lineno).strip()
        where = (f'<div style="color:{MUTED};font:12px {FONT};margin-top:4px">raised on the line '
                 f'<code style="font:12px {MONO};color:{INK}">{_html.escape(self.line)}</code></div>'
                 if self.line else "")
        display(HTML(
            f'<div style="padding:8px 12px;background:{brand.ROSE_TINT};border-left:3px solid '
            f'{FAIL_COLOUR};border-radius:4px"><div style="font:13.5px {MONO};color:{NIGHT}">'
            f'<b style="color:{FAIL_COLOUR}">{_html.escape(self.name)}</b>: '
            f'{_html.escape(self.message)}</div>{where}</div>'))
        return True


# --------------------------------------------------------------------------- tables and numbers
_NUMERIC = re.compile(r"^-?(Rs\s)?[\d,]+(\.\d+)?%?$")


def table(headers, rows, caption=""):
    """Any result worth reading as a grid, set like the deck's tables: indigo head, banded rows.

    A column whose every cell is a number or an amount in rupees is set flush right, so the digits
    line up the way they do on Finance's sheets.
    """
    rows = [list(r) for r in rows]
    numeric = [bool(rows) and all(_NUMERIC.match(str(r[j]).strip()) for r in rows if j < len(r))
               for j in range(len(headers))]
    head = "".join(
        f'<th style="text-align:{"right" if numeric[j] else "left"};padding:7px 12px;'
        f'background:{INK};color:{WHITE};font-weight:700">{_html.escape(str(h))}</th>'
        for j, h in enumerate(headers))
    body = "".join(
        f'<tr style="background:{BG if i % 2 else WHITE}">' + "".join(
            f'<td style="padding:6px 12px;border-bottom:1px solid {LINE};color:{NIGHT};'
            f'vertical-align:top;text-align:{"right" if j < len(numeric) and numeric[j] else "left"}">'
            f'{_html.escape(str(c))}</td>' for j, c in enumerate(row)) + "</tr>"
        for i, row in enumerate(rows))
    cap = (f'<caption style="text-align:left;caption-side:top;color:{MUTED};font-size:13px;'
           f'padding-bottom:6px">{_html.escape(caption)}</caption>') if caption else ""
    display(HTML(f'<table style="border-collapse:collapse;font:14px {FONT};margin:8px 0;'
                 f'border:1px solid {LINE}">{cap}<thead><tr>{head}</tr></thead>'
                 f'<tbody>{body}</tbody></table>'))


def stats(items, caption=""):
    """Big numbers with a tracked label and a note, the deck's stats row in a notebook.

    items is a list of (value, label, note) tuples; the note may be left empty.
    """
    cells = "".join(
        f'<div style="flex:1;min-width:150px;padding:4px 18px 10px 0;border-bottom:1px solid {LINE}">'
        f'<div style="font:34px {SERIF};color:{ACCENT};line-height:1.15">{_html.escape(str(v))}</div>'
        f'<div style="font:700 11px {FONT};color:{INK};letter-spacing:.16em;text-transform:uppercase;'
        f'margin-top:2px">{_html.escape(str(label))}</div>'
        f'<div style="font:12.5px {FONT};color:{MUTED};margin-top:2px">{_html.escape(str(note))}</div>'
        f'</div>' for v, label, note in items)
    cap = (f'<div style="font:13px {FONT};color:{MUTED};margin-bottom:6px">'
           f'{_html.escape(caption)}</div>') if caption else ""
    display(HTML(f'<div style="margin:8px 0">{cap}<div style="display:flex;gap:18px;'
                 f'flex-wrap:wrap">{cells}</div></div>'))


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
        f'<div style="margin:5px 0;padding:8px 11px;background:{TINT if i % 2 == 0 else WHITE};'
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
    cap = (f'<text x="{width / 2:.0f}" y="{height - 8}" text-anchor="middle" fill="{MUTED}" '
           f'font-family="{FONT}" font-size="12.5">{_html.escape(title)}</text>') if title else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width:.0f}" height="{height:.0f}" '
            f'viewBox="0 0 {width:.0f} {height:.0f}" role="img">'
            f'<rect width="{width:.0f}" height="{height:.0f}" rx="10" fill="{BG}"/>'
            f'{body}{cap}</svg>')


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


def _lines(text, w, size):
    """A label as (text, bold) lines: the first line of a two-part label is its bold title."""
    per = max(8, int(w / (size * 0.56)))
    parts = str(text).split("\n")
    out = [(l, True) for l in _wrap(parts[0], per)] if len(parts) > 1 else \
          [(l, False) for l in _wrap(parts[0], per)]
    for extra in parts[1:]:
        out += [(l, False) for l in _wrap(extra, per)]
    return out


def _box_height(text, w, size=13, pad=16):
    return max(40, len(_lines(text, w - 16, size)) * (size + 4) + pad)


def _box(x, y, w, h, text, lit=False, size=13, radius=8, kind=None):
    """A labelled box. kind picks the look: plain, lit, known, unknown, bad or good."""
    kind = kind or ("lit" if lit else "plain")
    fill, stroke, width, ink, dash = KINDS.get(kind, KINDS["plain"])
    lines = _lines(text, w - 16, size)
    top = y + h / 2 - (len(lines) - 1) * (size + 4) / 2 + size * 0.36
    label = "".join(
        f'<text x="{x + w / 2:.0f}" y="{top + i * (size + 4):.1f}" text-anchor="middle" '
        f'fill="{ink}" font-family="{FONT}" font-size="{size}" '
        f'font-weight="{700 if bold or kind == "lit" and len(lines) == 1 else 400}">'
        f'{_html.escape(l)}</text>' for i, (l, bold) in enumerate(lines))
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" rx="{radius}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{width}"{dash_attr}/>{label}')


def _arrow(x1, y1, x2, y2, label=""):
    mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
    cap = (f'<text x="{mid_x:.0f}" y="{mid_y - 6:.0f}" text-anchor="middle" fill="{MUTED}" '
           f'font-family="{FONT}" font-size="11.5">{_html.escape(label)}</text>') if label else ""
    return (f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{ACCENT}" '
            f'stroke-width="1.5" marker-end="url(#c2kArrow)"/>{cap}')


def _curve(x1, y1, x2, y2):
    dx = max(24, (x2 - x1) * 0.5)
    return (f'<path d="M {x1:.0f} {y1:.0f} C {x1 + dx:.0f} {y1:.0f}, {x2 - dx:.0f} {y2:.0f}, '
            f'{x2:.0f} {y2:.0f}" fill="none" stroke="{ACCENT}" stroke-width="1.5" '
            f'marker-end="url(#c2kArrow)"/>')


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
    w, gap = 230, 12
    heights = [_box_height(f"{i + 1}. {item}", w) for i, item in enumerate(items)]
    body, y = [_DEFS], 12
    for i, (item, h) in enumerate(zip(items, heights)):
        if i:
            body.append(_arrow(14 + w / 2, y - gap, 14 + w / 2, y))
        body.append(_box(14, y, w, h, f"{i + 1}. {item}", kind="lit" if i == lit else "plain"))
        y += h + gap
    return _emit(_svg(w + 28, y + (24 if title else 6), "".join(body), title), show)


def flow(steps, lit=None, title="", show=True, kinds=None):
    """Steps left to right, with one lit. kinds, when given, sets each step's look by name."""
    w, gap = 164, 30
    h = max(_box_height(s, w) for s in steps)
    width = len(steps) * w + (len(steps) - 1) * gap + 28
    body = [_DEFS]
    for i, step in enumerate(steps):
        x = 14 + i * (w + gap)
        kind = (kinds[i] if kinds else None) or ("lit" if i == lit else "plain")
        body.append(_box(x, 14, w, h, step, kind=kind))
        if i:
            body.append(_arrow(x - gap, 14 + h / 2, x - 2, 14 + h / 2))
    return _emit(_svg(width, h + 28 + (22 if title else 0), "".join(body), title), show)


def vflow(steps, lit=None, title="", show=True, kinds=None, edges=None):
    """The same, top to bottom, for a decision path or a longer sequence.

    edges, when given, labels the arrow into each step after the first.
    """
    w, gap = 320, 30 if edges else 22
    body, y = [_DEFS], 12
    for i, step in enumerate(steps):
        h = _box_height(step, w)
        if i:
            label = edges[i - 1] if edges and i - 1 < len(edges) else ""
            body.append(_arrow(14 + w / 2, y - gap, 14 + w / 2, y - 2))
            if label:
                body.append(f'<text x="{14 + w / 2 + 10:.0f}" y="{y - gap / 2 + 4:.0f}" '
                            f'fill="{MUTED}" font-family="{FONT}" font-size="12">'
                            f'{_html.escape(label)}</text>')
        kind = (kinds[i] if kinds else None) or ("lit" if i == lit else "plain")
        body.append(_box(14, y, w, h, step, kind=kind))
        y += h + gap
    return _emit(_svg(w + 28 + (150 if edges else 0), y - gap + 16 + (22 if title else 0),
                      "".join(body), title), show)


def stack(layers, lit=None, title="", show=True):
    """Layers bottom to top, for a concept with layers rather than steps."""
    w, h, gap = 320, 44, 8
    body = []
    for i, layer in enumerate(layers):
        y = 12 + (len(layers) - 1 - i) * (h + gap)
        body.append(_box(14, y, w, h, layer, kind="lit" if i == lit else "plain"))
    return _emit(_svg(w + 28, len(layers) * (h + gap) + 30, "".join(body), title), show)


def sequence(lanes, messages, title="", show=True):
    """Messages across named lanes, drawn from the run that actually happened."""
    lane_w, top, step = 190, 46, 44
    width = len(lanes) * lane_w + 28
    height = top + max(1, len(messages)) * step + 34
    body = [_DEFS]
    for i, lane in enumerate(lanes):
        x = 14 + i * lane_w
        body.append(_box(x + 10, 10, lane_w - 20, 30, lane, kind="lit", size=12, radius=5))
        body.append(f'<line x1="{x + lane_w / 2:.0f}" y1="42" x2="{x + lane_w / 2:.0f}" '
                    f'y2="{height - 28}" stroke="{LINE}" stroke-width="1"/>')
    for n, (src, dst, text) in enumerate(messages):
        y = top + n * step + 20
        x1 = 14 + lanes.index(src) * lane_w + lane_w / 2
        x2 = 14 + lanes.index(dst) * lane_w + lane_w / 2
        body.append(_arrow(x1, y, x2, y, text))
    return _emit(_svg(width, height, "".join(body), title), show)


def tree(node, taken=(), title="", show=True):
    """A decision tree from nested dicts, top down, with the branch actually taken marked.

    node is {"label": ..., "branches": [(edge_label, child_node), ...]}, and taken is the list of
    edge labels the run followed. A node may carry "kind" to set its look.
    """
    levels = []

    def walk(n, depth, path):
        while len(levels) <= depth:
            levels.append([])
        entry = {"label": n["label"], "path": path, "children": [], "kind": n.get("kind")}
        levels[depth].append(entry)
        for edge, child in n.get("branches", []):
            entry["children"].append((edge, walk(child, depth + 1, path + [edge])))
        return entry

    walk(node, 0, [])
    w, gap_x, gap_y = 196, 22, 44
    level_h = [max(_box_height(e["label"], w) for e in level) for level in levels]
    width = max(len(l) for l in levels) * (w + gap_x) + 28
    height = sum(level_h) + gap_y * (len(levels) - 1) + 24 + (22 if title else 0)
    body, coords, y = [_DEFS], {}, 12
    for d, level in enumerate(levels):
        span = len(level) * (w + gap_x) - gap_x
        x0 = (width - span) / 2
        for i, entry in enumerate(level):
            x = x0 + i * (w + gap_x)
            on = bool(taken) and list(taken)[:len(entry["path"])] == entry["path"]
            coords[id(entry)] = (x + w / 2, y, x + w / 2, y + level_h[d])
            body.append(_box(x, y, w, level_h[d], entry["label"],
                             kind=entry["kind"] or ("lit" if on else "plain")))
        y += level_h[d] + gap_y
    for level in levels:
        for entry in level:
            _, _, bx, by = coords[id(entry)]
            for edge, child in entry["children"]:
                cx, cy, _, _ = coords[id(child)]
                body.append(_arrow(bx, by, cx, cy - 2, edge))
    return _emit(_svg(width, height, "".join(body), title), show)


def driver_tree(node, title="", show=True, width_per=156):
    """A driver tree left to right: a total on the left, what multiplies into it on the right.

    node is {"label": ..., "note": ..., "kind": ..., "children": [node, ...]}. The label prints
    bold and the note under it; kind is plain, lit, known, unknown, bad or good. This is the day's
    picture from the deck, drawn in the same shapes so the two are recognisably one drawing.
    """
    w, gap_x, gap_y = width_per, 38, 12
    rows, placed = [], []

    def text(n):
        return f'{n["label"]}\n{n["note"]}' if n.get("note") else n["label"]

    h = max(_box_height(text(n), w) for n in _nodes(node))

    def place(n, depth):
        kids = n.get("children", [])
        if not kids:
            y = len(rows) * (h + gap_y)
            rows.append(n)
        else:
            ys = [place(k, depth + 1) for k in kids]
            y = (ys[0] + ys[-1]) / 2
        placed.append((n, depth, y))
        return y

    place(node, 0)
    depth = max(d for _, d, _ in placed)
    width = (depth + 1) * w + depth * gap_x + 28
    height = len(rows) * (h + gap_y) - gap_y + 24 + (24 if title else 0)
    pos = {id(n): (14 + d * (w + gap_x), 12 + y) for n, d, y in placed}
    body = [_DEFS]
    for n, d, y in placed:
        x0, y0 = pos[id(n)]
        for k in n.get("children", []):
            x1, y1 = pos[id(k)]
            body.append(_curve(x0 + w, y0 + h / 2, x1 - 2, y1 + h / 2))
    for n, d, y in placed:
        x0, y0 = pos[id(n)]
        body.append(_box(x0, y0, w, h, text(n), kind=n.get("kind", "plain")))
    return _emit(_svg(width, height, "".join(body), title), show)


def _nodes(node):
    yield node
    for k in node.get("children", []):
        yield from _nodes(k)


def equation(parts, title="", show=True):
    """A formula as boxes and operators, read left to right, for a relation worth seeing whole.

    parts alternates terms and operators: ["revenue", "=", "customers", "x", ...]. A term may be
    "label\\nnote"; an operator is any part of three characters or fewer.
    """
    w, gap = 132, 12
    terms = [p for p in parts if len(p) > 3]
    h = max(_box_height(t, w, 12.5) for t in terms)
    x, body = 14, []
    for p in parts:
        if len(p) <= 3:
            body.append(f'<text x="{x + 11:.0f}" y="{12 + h / 2 + 8:.0f}" text-anchor="middle" '
                        f'fill="{ACCENT}" font-family="{SERIF}" font-size="24">'
                        f'{_html.escape(p)}</text>')
            x += 22 + gap
        else:
            body.append(_box(x, 12, w, h, p, size=12.5, kind="lit" if x == 14 else "plain"))
            x += w + gap
    return _emit(_svg(x + 2, h + 30 + (20 if title else 0), "".join(body), title), show)


def _nice_ceil(x):
    """The next round number at or above x, 1, 2, 2.5 or 5 times a power of ten, for clean ticks."""
    if x <= 0:
        return 1
    import math
    p = 10 ** math.floor(math.log10(x))
    for step in (1, 2, 2.5, 5, 10):
        if step * p >= x:
            return step * p
    return 10 * p


def strip(values, markers=(), title="", show=True, lo=0, hi=None, fmt=None, width=820,
          lit=()):
    """Every value as a dot on one axis, with the mean, the median or any line you name.

    markers is a list of (label, value, kind) where kind is "bad" or "good" or "plain". Dots that
    would overlap stack upward, so thirty values that sit close together show as a pile. lit is
    a list of indexes whose dots are drawn dark.
    """
    fmt = fmt or rupees
    hi = hi if hi is not None else _nice_ceil(max(values) * 1.04)
    left, right, axis_y = 40, width - 40, 150
    span = (hi - lo) or 1

    def px(v):
        return left + (right - left) * (v - lo) / span

    body, bins = [], {}
    body.append(f'<line x1="{left}" y1="{axis_y}" x2="{right}" y2="{axis_y}" stroke="{MUTED}" '
                f'stroke-width="1"/>')
    for i in range(5):
        v = lo + span * i / 4
        x = px(v)
        body.append(f'<line x1="{x:.0f}" y1="{axis_y}" x2="{x:.0f}" y2="{axis_y + 5}" '
                    f'stroke="{MUTED}"/><text x="{x:.0f}" y="{axis_y + 20}" text-anchor="middle" '
                    f'fill="{MUTED}" font-family="{FONT}" font-size="12">'
                    f'{_html.escape(fmt(v))}</text>')
    colours = {"bad": FAIL_COLOUR, "good": PASS_COLOUR, "plain": ACCENT}
    markers = list(markers)
    for n, (label, v, kind) in enumerate(markers):
        x = px(v)
        c = colours.get(kind, ACCENT)
        # Two lines close together would print their labels over each other, so the lower one of a
        # close pair reads leftward from its line.
        prev = px(markers[n - 1][1]) if n else None
        left = n > 0 and abs(x - prev) < 150 and x <= prev
        body.append(f'<line x1="{x:.0f}" y1="{34 + 16 * (n % 2)}" x2="{x:.0f}" y2="{axis_y}" '
                    f'stroke="{c}" stroke-width="1.6" stroke-dasharray="5 4"/>'
                    f'<text x="{x - 5 if left else x + 5:.0f}" y="{30 + 16 * (n % 2)}" fill="{c}" '
                    f'text-anchor="{"end" if left else "start"}" '
                    f'font-family="{FONT}" font-size="12.5" font-weight="700">'
                    f'{_html.escape(label)} {_html.escape(fmt(v))}</text>')
    for i, v in enumerate(values):
        x = px(v)
        key = round(x / 11)
        level = bins.get(key, 0)
        bins[key] = level + 1
        y = axis_y - 9 - level * 11
        fill = INK if i in lit else ACCENT
        body.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{fill}" fill-opacity="0.8" '
                    f'stroke="{WHITE}" stroke-width="1"/>')
    return _emit(_svg(width, axis_y + 34 + (22 if title else 0), "".join(body), title), show)


def bars(rows, title="", show=True, fmt=None, lit=(), width=720):
    """Horizontal bars, one per (label, value), with the value printed at the end of each bar."""
    fmt = fmt or (lambda v: f"{v:,}")
    label_w, bar_h, gap = 190, 26, 10
    top = max(v for _, v in rows) or 1
    room = width - label_w - 130
    body = []
    for i, (label, v) in enumerate(rows):
        y = 12 + i * (bar_h + gap)
        w = max(2, room * v / top)
        fill = INK if i in lit else ACCENT
        body.append(f'<text x="{label_w - 10}" y="{y + bar_h / 2 + 5:.0f}" text-anchor="end" '
                    f'fill="{INK}" font-family="{FONT}" font-size="13">{_html.escape(str(label))}'
                    f'</text><rect x="{label_w}" y="{y}" width="{w:.0f}" height="{bar_h}" rx="5" '
                    f'fill="{fill}" fill-opacity="0.85"/><text x="{label_w + w + 8:.0f}" '
                    f'y="{y + bar_h / 2 + 5:.0f}" fill="{INK}" font-family="{FONT}" font-size="13" '
                    f'font-weight="700">{_html.escape(fmt(v))}</text>')
    height = len(rows) * (bar_h + gap) + 14 + (22 if title else 0)
    return _emit(_svg(width, height, "".join(body), title), show)


def matrix(row_labels, col_labels, cells, title="", show=True):
    """A two-axis grid, for a choice with two independent dimensions."""
    cw, ch, lw = 190, 58, 150
    width = lw + len(col_labels) * cw + 28
    height = 40 + len(row_labels) * ch + 30
    body = []
    for j, col in enumerate(col_labels):
        body.append(f'<text x="{14 + lw + j * cw + cw / 2:.0f}" y="28" text-anchor="middle" '
                    f'fill="{ACCENT}" font-family="{FONT}" font-size="12.5" font-weight="700">'
                    f'{_html.escape(str(col))}</text>')
    for i, row in enumerate(row_labels):
        y = 40 + i * ch
        body.append(f'<text x="14" y="{y + ch / 2 + 4:.0f}" fill="{ACCENT}" font-family="{FONT}" '
                    f'font-size="12.5" font-weight="700">{_html.escape(str(row))}</text>')
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
        body.append(_box(14, y, w, h, option, kind="lit" if i == cut_at else "plain"))
        if cut_at is not None and i == cut_at:
            body.append(f'<line x1="10" y1="{y - gap / 2:.0f}" x2="{w + 22}" '
                        f'y2="{y - gap / 2:.0f}" stroke="{FAIL_COLOUR}" stroke-width="1.5" '
                        f'stroke-dasharray="5 4"/>'
                        f'<text x="{w + 24}" y="{y - gap / 2 + 4:.0f}" fill="{FAIL_COLOUR}" '
                        f'font-family="{FONT}" font-size="11.5">stop here</text>')
    return _emit(_svg(w + 120, height, "".join(body), title), show)


def side_by_side(*svgs, gap=26, show=True):
    """Two or more diagrams composed horizontally, which is the opening MAP cell's shape."""
    body = (f'<div style="display:flex;gap:{gap}px;align-items:flex-start;flex-wrap:wrap">'
            + "".join(f"<div>{svg}</div>" for svg in svgs) + "</div>")
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
# with kit.expect_error() as err: int("1,20,000")
#     Shows "ValueError: invalid literal for int() with base 10: '1,20,000'" with the line that
#     raised it; err.name is "ValueError" and the next cell runs.
# kit.flow(["read", "profile", "decide"], lit=1)
#     Renders three boxes left to right with the middle one dark, as saved SVG.
# kit.driver_tree({"label": "revenue", "children": [{"label": "customers"}, {"label": "spend"}]})
#     Renders the total on the left and its two drivers on the right, joined by curves.
# kit.strip([400, 2100, 2300, 90000], markers=[("mean", 23700, "bad"), ("median", 2200, "good")])
#     Renders four dots on one axis with a rose mean line and a green median line.
# kit.side_by_side(kit.ladder(["a", "b"], lit=0, show=False), kit.flow(["x"], show=False))
#     Renders both diagrams in one row. Pass show=False to a builder to compose rather than draw.
# kit.load_records() from a notebooks/ folder whose ../data holds the generated orders file
#     Returns the 30 dictionaries. With the file missing it raises, naming the generator command.
