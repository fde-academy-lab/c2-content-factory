/* c2kit.js: the diagram builders and page helpers every companion page inlines.
 *
 * The JavaScript twin of scripts/c2kit.py, so a tree on the slide, in the notebook and on the
 * companion page is one drawing in one violet. Every builder takes data and returns an SVG
 * element; nothing is drawn until a page calls a builder. No storage, no network, no globals
 * beyond window.C2K. scripts/build_companion.py inlines this file into each page.
 */
(function () {
  "use strict";
  var NS = "http://www.w3.org/2000/svg";
  var C = {
    ink: "#1A0F5C", night: "#1A1440", violet: "#5B3FD6", lav: "#D9A7FF", muted: "#6B6690",
    lilac: "#CFC9EE", line: "#E4E1F1", tint: "#EEEAFB", surface: "#F4F2FA", white: "#FFFFFF",
    rose: "#D63A6A", roseTint: "#FCEBF0", green: "#1F8A5B", greenTint: "#E8F5EE"
  };
  var FONT = "Calibri, Carlito, 'Segoe UI', system-ui, sans-serif";
  var SERIF = "Georgia, 'DejaVu Serif', serif";
  var KINDS = {
    plain: [C.tint, C.violet, 1.2, C.ink, ""],
    lit: [C.ink, C.ink, 1.2, C.white, ""],
    known: [C.tint, C.violet, 2.6, C.ink, ""],
    unknown: [C.white, "#B8B2D6", 1.3, C.muted, "5 4"],
    bad: [C.roseTint, C.rose, 1.6, C.ink, ""],
    good: [C.greenTint, C.green, 1.6, C.ink, ""]
  };

  function el(name, attrs, text) {
    var node = document.createElementNS(NS, name);
    Object.keys(attrs || {}).forEach(function (k) { node.setAttribute(k, attrs[k]); });
    if (text !== undefined) node.textContent = text;
    return node;
  }

  function wrap(text, perLine) {
    var words = String(text).split(/\s+/), lines = [], line = "";
    words.forEach(function (w) {
      if (line && (line + " " + w).length > perLine) { lines.push(line); line = w; }
      else { line = line ? line + " " + w : w; }
    });
    if (line) lines.push(line);
    return lines.length ? lines : [""];
  }

  function labelLines(text, w, size) {
    var per = Math.max(8, Math.floor(w / (size * 0.56)));
    var parts = String(text).split("\n"), out = [];
    wrap(parts[0], per).forEach(function (l) { out.push([l, parts.length > 1]); });
    parts.slice(1).forEach(function (p) { wrap(p, per).forEach(function (l) { out.push([l, false]); }); });
    return out;
  }

  function boxHeight(text, w, size) {
    size = size || 13;
    return Math.max(40, labelLines(text, w - 16, size).length * (size + 4) + 16);
  }

  function root(width, height, title) {
    var svg = el("svg", { xmlns: NS, width: width, height: height, viewBox: "0 0 " + width + " " + height,
                          role: "img", "class": "c2k-svg" });
    var defs = el("defs");
    var marker = el("marker", { id: "c2kArrow", viewBox: "0 0 10 10", refX: 9, refY: 5, markerWidth: 6,
                                markerHeight: 6, orient: "auto-start-reverse" });
    marker.appendChild(el("path", { d: "M 0 0 L 10 5 L 0 10 z", fill: C.violet }));
    defs.appendChild(marker);
    svg.appendChild(defs);
    svg.appendChild(el("rect", { width: width, height: height, rx: 10, fill: C.surface }));
    if (title) {
      svg.appendChild(el("text", { x: width / 2, y: height - 8, "text-anchor": "middle", fill: C.muted,
                                   "font-family": FONT, "font-size": 12.5 }, title));
    }
    return svg;
  }

  function box(svg, x, y, w, h, text, kind, size) {
    size = size || 13;
    var k = KINDS[kind] || KINDS.plain;
    var g = el("g", { "class": "c2k-node c2k-" + (kind || "plain") });
    var rect = el("rect", { x: x, y: y, width: w, height: h, rx: 8, fill: k[0], stroke: k[1],
                            "stroke-width": k[2] });
    if (k[4]) rect.setAttribute("stroke-dasharray", k[4]);
    g.appendChild(rect);
    var lines = labelLines(text, w - 16, size);
    var top = y + h / 2 - (lines.length - 1) * (size + 4) / 2 + size * 0.36;
    lines.forEach(function (pair, i) {
      g.appendChild(el("text", { x: x + w / 2, y: top + i * (size + 4), "text-anchor": "middle", fill: k[3],
                                 "font-family": FONT, "font-size": size,
                                 "font-weight": (pair[1] || (kind === "lit" && lines.length === 1)) ? 700 : 400 },
                       pair[0]));
    });
    svg.appendChild(g);
    return g;
  }

  function arrow(svg, x1, y1, x2, y2, label) {
    svg.appendChild(el("line", { x1: x1, y1: y1, x2: x2, y2: y2, stroke: C.violet, "stroke-width": 1.5,
                                 "marker-end": "url(#c2kArrow)" }));
    if (label) {
      svg.appendChild(el("text", { x: (x1 + x2) / 2, y: (y1 + y2) / 2 - 6, "text-anchor": "middle",
                                   fill: C.muted, "font-family": FONT, "font-size": 11.5 }, label));
    }
  }

  function curve(svg, x1, y1, x2, y2) {
    var dx = Math.max(24, (x2 - x1) * 0.5);
    svg.appendChild(el("path", { d: "M " + x1 + " " + y1 + " C " + (x1 + dx) + " " + y1 + ", " + (x2 - dx) + " " +
                                 y2 + ", " + x2 + " " + y2, fill: "none", stroke: C.violet, "stroke-width": 1.5,
                                 "marker-end": "url(#c2kArrow)" }));
  }

  /* Steps left to right, with one lit; kinds sets each step's look by name. */
  function flow(steps, lit, opts) {
    opts = opts || {};
    var w = opts.width || 150, gap = 28;
    var h = Math.max.apply(null, steps.map(function (s) { return boxHeight(s, w); }));
    var svg = root(steps.length * w + (steps.length - 1) * gap + 28, h + 28 + (opts.title ? 22 : 0), opts.title);
    steps.forEach(function (s, i) {
      var x = 14 + i * (w + gap);
      var kind = (opts.kinds && opts.kinds[i]) || (i === lit ? "lit" : "plain");
      box(svg, x, 14, w, h, s, kind);
      if (i) arrow(svg, x - gap, 14 + h / 2, x - 2, 14 + h / 2, opts.edges ? opts.edges[i - 1] : "");
    });
    return svg;
  }

  /* The same, top to bottom; edges labels the arrow into each step after the first. */
  function vflow(steps, lit, opts) {
    opts = opts || {};
    var w = opts.width || 300, gap = opts.edges ? 30 : 22, y = 12, parts = [];
    steps.forEach(function (s) { parts.push(boxHeight(s, w)); });
    var total = parts.reduce(function (a, b) { return a + b; }, 0) + gap * (steps.length - 1) + 28;
    var svg = root(w + 28 + (opts.edges ? 150 : 0), total + (opts.title ? 22 : 0), opts.title);
    steps.forEach(function (s, i) {
      if (i) {
        arrow(svg, 14 + w / 2, y - gap, 14 + w / 2, y - 2);
        if (opts.edges && opts.edges[i - 1]) {
          svg.appendChild(el("text", { x: 14 + w / 2 + 10, y: y - gap / 2 + 4, fill: C.muted, "font-family": FONT,
                                       "font-size": 12 }, opts.edges[i - 1]));
        }
      }
      var kind = (opts.kinds && opts.kinds[i]) || (i === lit ? "lit" : "plain");
      box(svg, 14, y, w, parts[i], s, kind);
      y += parts[i] + gap;
    });
    return svg;
  }

  function ladder(items, lit, opts) {
    return vflow(items.map(function (t, i) { return (i + 1) + ". " + t; }), lit, opts);
  }

  /* A decision tree, top down. node: {label, kind, branches: [[edgeLabel, child], ...]}. */
  function tree(node, opts) {
    opts = opts || {};
    var levels = [];
    (function walk(n, d) {
      if (!levels[d]) levels[d] = [];
      var entry = { n: n, kids: [] };
      levels[d].push(entry);
      (n.branches || []).forEach(function (b) { entry.kids.push([b[0], walk(b[1], d + 1)]); });
      return entry;
    })(node, 0);
    var w = opts.width || 196, gx = 22, gy = 44;
    var lh = levels.map(function (l) {
      return Math.max.apply(null, l.map(function (e) { return boxHeight(e.n.label, w); }));
    });
    var width = Math.max.apply(null, levels.map(function (l) { return l.length; })) * (w + gx) + 28;
    var height = lh.reduce(function (a, b) { return a + b; }, 0) + gy * (levels.length - 1) + 24 + (opts.title ? 22 : 0);
    var svg = root(width, height, opts.title), y = 12;
    levels.forEach(function (level, d) {
      var span = level.length * (w + gx) - gx, x0 = (width - span) / 2;
      level.forEach(function (e, i) {
        e.x = x0 + i * (w + gx); e.y = y; e.h = lh[d];
        box(svg, e.x, e.y, w, e.h, e.n.label, e.n.kind || "plain");
      });
      y += lh[d] + gy;
    });
    levels.forEach(function (level) {
      level.forEach(function (e) {
        e.kids.forEach(function (k) {
          arrow(svg, e.x + w / 2, e.y + e.h, k[1].x + w / 2, k[1].y - 2, k[0]);
        });
      });
    });
    return svg;
  }

  /* A driver tree, left to right: a total on the left, what multiplies into it on the right.
   * node: {label, note, kind, children: [...]}. */
  function driverTree(node, opts) {
    opts = opts || {};
    var w = opts.width || 156, gx = 38, gy = 12, rows = 0, placed = [];
    function text(n) { return n.note ? n.label + "\n" + n.note : n.label; }
    var all = [];
    (function walk(n) { all.push(n); (n.children || []).forEach(walk); })(node);
    var h = Math.max.apply(null, all.map(function (n) { return boxHeight(text(n), w); }));
    (function place(n, d) {
      var y;
      if (!n.children || !n.children.length) { y = rows * (h + gy); rows += 1; }
      else {
        var ys = n.children.map(function (k) { return place(k, d + 1); });
        y = (ys[0] + ys[ys.length - 1]) / 2;
      }
      placed.push([n, d, y]);
      return y;
    })(node, 0);
    var depth = Math.max.apply(null, placed.map(function (p) { return p[1]; }));
    var svg = root((depth + 1) * w + depth * gx + 28, rows * (h + gy) - gy + 24 + (opts.title ? 24 : 0), opts.title);
    var pos = new Map();
    placed.forEach(function (p) { pos.set(p[0], [14 + p[1] * (w + gx), 12 + p[2]]); });
    placed.forEach(function (p) {
      var a = pos.get(p[0]);
      (p[0].children || []).forEach(function (k) {
        var b = pos.get(k);
        curve(svg, a[0] + w, a[1] + h / 2, b[0] - 2, b[1] + h / 2);
      });
    });
    placed.forEach(function (p) {
      var a = pos.get(p[0]);
      var g = box(svg, a[0], a[1], w, h, text(p[0]), p[0].kind || "plain");
      if (p[0].id) g.setAttribute("data-node", p[0].id);
    });
    return svg;
  }

  /* Every value as a dot on one axis, with named marker lines. markers: [[label, value, kind]]. */
  function strip(values, opts) {
    opts = opts || {};
    var fmt = opts.fmt || rupees, width = opts.width || 760;
    var lo = opts.lo === undefined ? 0 : opts.lo;
    var hi = opts.hi === undefined ? niceCeil(Math.max.apply(null, values) * 1.04) : opts.hi;
    var left = 40, right = width - 40, axis = 150, span = (hi - lo) || 1;
    function px(v) { return left + (right - left) * (v - lo) / span; }
    var svg = root(width, axis + 34 + (opts.title ? 22 : 0), opts.title);
    svg.appendChild(el("line", { x1: left, y1: axis, x2: right, y2: axis, stroke: C.muted }));
    for (var i = 0; i < 5; i++) {
      var v = lo + span * i / 4, x = px(v);
      svg.appendChild(el("line", { x1: x, y1: axis, x2: x, y2: axis + 5, stroke: C.muted }));
      svg.appendChild(el("text", { x: x, y: axis + 20, "text-anchor": "middle", fill: C.muted, "font-family": FONT,
                                   "font-size": 12 }, fmt(v)));
    }
    var colour = { bad: C.rose, good: C.green, plain: C.violet };
    var marks = opts.markers || [];
    marks.forEach(function (m, n) {
      var x = px(m[1]), c = colour[m[2]] || C.violet;
      /* Two lines close together would print their labels over each other, so the lower one of a
         close pair reads leftward from its line. */
      var left = n > 0 && Math.abs(x - px(marks[n - 1][1])) < 150 && x <= px(marks[n - 1][1]);
      svg.appendChild(el("line", { x1: x, y1: 34 + 16 * (n % 2), x2: x, y2: axis, stroke: c, "stroke-width": 1.6,
                                   "stroke-dasharray": "5 4", "class": "c2k-marker" }));
      svg.appendChild(el("text", { x: left ? x - 5 : x + 5, y: 30 + 16 * (n % 2), fill: c, "font-family": FONT,
                                   "font-size": 12.5, "font-weight": 700, "text-anchor": left ? "end" : "start" },
                         m[0] + " " + fmt(m[1])));
    });
    var bins = {};
    values.forEach(function (v, i) {
      var x = px(v), key = Math.round(x / 11), level = bins[key] || 0;
      bins[key] = level + 1;
      svg.appendChild(el("circle", { cx: x, cy: axis - 9 - level * 11, r: 5,
                                     fill: (opts.lit || []).indexOf(i) >= 0 ? C.ink : C.violet,
                                     "fill-opacity": 0.8, stroke: C.white, "stroke-width": 1 }));
    });
    return svg;
  }

  /* The next round number at or above x: 1, 2, 2.5 or 5 times a power of ten, so axis ticks read cleanly. */
  function niceCeil(x) {
    if (x <= 0) return 1;
    var p = Math.pow(10, Math.floor(Math.log10(x))), steps = [1, 2, 2.5, 5, 10];
    for (var i = 0; i < steps.length; i++) if (steps[i] * p >= x) return steps[i] * p;
    return 10 * p;
  }

  /* Messages across named lanes, drawn from the run that happened. messages: [[from, to, text]]. */
  function sequence(lanes, messages, opts) {
    opts = opts || {};
    var lw = opts.laneWidth || 180, top = 46, step = 44;
    var width = lanes.length * lw + 28, height = top + Math.max(1, messages.length) * step + 34 + (opts.title ? 16 : 0);
    var svg = root(width, height, opts.title);
    lanes.forEach(function (lane, i) {
      var x = 14 + i * lw;
      box(svg, x + 10, 10, lw - 20, 30, lane, "lit", 12);
      svg.appendChild(el("line", { x1: x + lw / 2, y1: 42, x2: x + lw / 2, y2: height - 28, stroke: C.line }));
    });
    messages.forEach(function (m, n) {
      var y = top + n * step + 20;
      var x1 = 14 + lanes.indexOf(m[0]) * lw + lw / 2, x2 = 14 + lanes.indexOf(m[1]) * lw + lw / 2;
      if (x1 === x2) {
        svg.appendChild(el("text", { x: x1 + 8, y: y + 4, fill: C.night, "font-family": FONT, "font-size": 12 }, m[2]));
      } else {
        arrow(svg, x1, y, x2 + (x2 > x1 ? -4 : 4), y, m[2]);
      }
    });
    return svg;
  }

  function sideBySide() {
    var div = document.createElement("div");
    div.className = "c2k-row";
    Array.prototype.forEach.call(arguments, function (svg) { div.appendChild(svg); });
    return div;
  }

  /* Rs with Indian digit grouping, the way every Kalpa number is read aloud. */
  function rupees(n) {
    var sign = n < 0 ? "-" : "", s = String(Math.round(Math.abs(n)));
    if (s.length <= 3) return sign + "Rs " + s;
    var head = s.slice(0, -3), tail = s.slice(-3), parts = [];
    while (head.length > 2) { parts.unshift(head.slice(-2)); head = head.slice(0, -2); }
    if (head) parts.unshift(head);
    return sign + "Rs " + parts.join(",") + "," + tail;
  }

  /* Put a diagram into a holder, replacing whatever was drawn there before. */
  function draw(holder, svg) {
    var target = typeof holder === "string" ? document.getElementById(holder) : holder;
    target.textContent = "";
    target.appendChild(svg);
    return svg;
  }

  window.C2K = { colours: C, flow: flow, vflow: vflow, ladder: ladder, tree: tree, driverTree: driverTree,
                 strip: strip, sequence: sequence, sideBySide: sideBySide, rupees: rupees, draw: draw };
})();
