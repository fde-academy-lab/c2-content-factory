/* saturday_docx.js: write a Saturday recap paper and its key as Word files.
 *
 * scripts/build_saturday_paper.py --docx assembles the paper from the tracker's bank and the week's
 * source file, renders every mermaid exhibit to a PNG, and hands this script one JSON spec:
 *
 *     node scripts/saturday_docx.js spec.json paper.docx key.docx
 *
 * The paper follows the requester's baseline diagnostic (content/W00/D2/paper), in its palette of
 * ink, bronze and warm grey, its fonts (Georgia for titles, Arial for text, Consolas for code), its
 * running header and its open question blocks: the number in bronze with a short label beside it,
 * the stem, any code in a beige panel with a bronze rule down its left edge, and the options A to D
 * with a hanging indent. Page one carries what the paper is for, the rules, step one (the rating of
 * each part before any item is read), the paper at a glance and a pacing ribbon. Each part opens on
 * its heading and its situation; each exhibit is printed once, labelled, and kept on the page of
 * the question that reads it; a question never splits across two pages. The answer sheet at the
 * end is the page that is marked: step one's ratings, box grids for every lettered item in three
 * columns, a T and F grid, and one line per written answer, with boxes for the order items.
 *
 * The key is a TRAINER file in the same visual system: the marking steps, the blueprint, what
 * guessing alone would score, the key table, why each answer holds and why each other option fails,
 * the stretch answers, and a marking grid, the answer sheet with every box of the key filled.
 */
"use strict";
const fs = require("fs");
const path = require("path");
let docx;
try { docx = require("docx"); } catch (e) { docx = require("/opt/node22/lib/node_modules/docx"); }
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType,
  BorderStyle, AlignmentType, ImageRun, LevelFormat, Header, Footer, PageNumber, VerticalAlign,
  HeightRule,
} = docx;

// The diagnostic's palette, read from its document.xml.
const INK = "1C1B16", BRONZE = "B37A33", MUTED = "6B675E", RULE = "D5D0C4", BEIGE = "F3F1EA",
      HEADFILL = "F9F8F3", WHITE = "FFFFFF", TINT = "EFE3D0";
const PAGE_W = 11906, PAGE_H = 16838, MARGIN = 1053, CONTENT = 9800;
const BODY = 21, OPTION = 20, SMALL = 18, NOTE = 19, TINY = 15;
const SANS = "Arial", SERIF = "Georgia", MONO = "Consolas";

const [specPath, paperOut, keyOut] = process.argv.slice(2);
const spec = JSON.parse(fs.readFileSync(specPath, "utf8"));

/* ------------------------------------------------------------------ primitives */
function run(text, o) {
  return new TextRun(Object.assign({ text: String(text), font: SANS, size: BODY, color: INK }, o || {}));
}
/* While an exhibit or a set's situation is being built, every paragraph in it keeps with the next,
   so an exhibit never ends a page with the question that reads it on the next one. */
let KEEP = false;
function kept(build) { KEEP = true; try { return build(); } finally { KEEP = false; } }
function p(children, o) {
  if (typeof children === "string") children = [run(children)];
  return new Paragraph(Object.assign({ children: children, keepNext: KEEP,
    spacing: { before: 0, after: 80, line: 276 } }, o || {}));
}
function none() { return { style: BorderStyle.NONE, size: 0, color: WHITE }; }
function line(colour, size) { return { style: BorderStyle.SINGLE, size: size || 4, color: colour || RULE }; }
function box(colour) { const b = line(colour); return { top: b, bottom: b, left: b, right: b }; }
function noBox() { return { top: none(), bottom: none(), left: none(), right: none() }; }
function tableBorders(b) {
  return { top: b, bottom: b, left: b, right: b, insideHorizontal: b, insideVertical: b };
}

function title(text) {
  return new Paragraph({ spacing: { before: 0, after: 60 },
    children: [new TextRun({ text: text, font: SERIF, size: 52, color: BRONZE })] });
}
function subtitle(text) {
  return p([run(text, { color: MUTED, size: BODY })], { spacing: { after: 160 } });
}
function bronzeRule(after) {
  return new Paragraph({ spacing: { before: 0, after: after || 240 }, children: [],
    border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: BRONZE, space: 1 } } });
}
function h2(text, before) {
  return new Paragraph({ keepNext: true, spacing: { before: before === undefined ? 200 : before, after: 80 },
    children: [run(text, { bold: true, size: 22 })] });
}
function partHeading(text) {
  return new Paragraph({ keepNext: true, spacing: { before: 280, after: 120 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: BRONZE, space: 4 } },
    children: [new TextRun({ text: text, font: SERIF, size: 30, color: BRONZE })] });
}
function muted(text, o) {
  return p([run(text, { color: MUTED, size: NOTE })],
           Object.assign({ keepNext: true, spacing: { after: 160, line: 276 } }, o || {}));
}
function spacer(after, keepNext) {
  return new Paragraph({ keepNext: !!keepNext, spacing: { before: 0, after: after || 80 }, children: [] });
}

/* A cell in the diagnostic's table style: a warm grey rule, light padding, the header row shaded. */
function cell(children, width, o) {
  o = o || {};
  return new TableCell({
    width: { size: width, type: WidthType.DXA }, borders: o.borders || box(RULE),
    shading: o.fill ? { type: ShadingType.CLEAR, color: "auto", fill: o.fill } : undefined,
    margins: o.margins || { top: 40, bottom: 40, left: 100, right: 100 },
    verticalAlign: o.valign || VerticalAlign.CENTER,
    children: children.length ? children : [p("")],
  });
}
function numeric(v) {
  return /^[-+]?(Rs\s)?[\d,]+(\.\d+)?%?$|^[-+]?(Rs\s)?\d+(\.\d+)?\s*(lakh|crore)$/.test(String(v).trim());
}
function grid(head, rows, widths, o) {
  o = o || {};
  const size = o.size || SMALL;
  const headRow = new TableRow({ tableHeader: true, cantSplit: true, children: head.map((h, i) => cell(
    [p([run(h, { bold: true, size: size })], { spacing: { after: 0, line: 240 }, keepNext: !!o.together || KEEP,
      alignment: (o.center || []).includes(i) ? AlignmentType.CENTER : AlignmentType.LEFT })],
    widths[i], { fill: HEADFILL })) });
  const body = rows.map((r, n) => new TableRow({ cantSplit: true, children: r.map((v, i) => {
    const last = o.boldLast && n === rows.length - 1;
    const right = o.numbers && numeric(v) && i > 0;
    const center = (o.center || []).includes(i);
    return cell([p([run(v, { size: size, bold: last || (i === 0 && o.boldFirst) })],
      { spacing: { after: 0, line: 252 }, keepNext: !!o.together && n < rows.length - 1,
        alignment: center ? AlignmentType.CENTER : right ? AlignmentType.RIGHT : AlignmentType.LEFT })], widths[i]);
  }) }));
  return new Table({ width: { size: widths.reduce((a, b) => a + b, 0), type: WidthType.DXA },
    columnWidths: widths, borders: tableBorders(line(RULE)), rows: [headRow].concat(body) });
}
/* One question as the diagnostic prints it: an open block, never boxed, never split across pages. */
function block(children) {
  return new Table({ width: { size: CONTENT, type: WidthType.DXA }, columnWidths: [CONTENT],
    borders: tableBorders(none()),
    rows: [new TableRow({ cantSplit: true, children: [new TableCell({
      width: { size: CONTENT, type: WidthType.DXA }, borders: noBox(),
      margins: { top: 0, bottom: 0, left: 0, right: 0 }, children: children })] })] });
}
function codeLines(lines) {
  return lines.map((l) => new Paragraph({ keepNext: true, keepLines: true,
    spacing: { before: 0, after: 0, line: 240 }, indent: { left: 240 },
    shading: { type: ShadingType.CLEAR, color: "auto", fill: BEIGE },
    border: { left: { style: BorderStyle.SINGLE, size: 12, color: BRONZE, space: 8 } },
    children: [new TextRun({ text: l.length ? l : " ", font: MONO, size: SMALL, color: INK })] }));
}
function image(img) {
  const maxW = 620, scale = Math.min(1, maxW / img.w);
  return new Paragraph({ alignment: AlignmentType.CENTER, keepNext: KEEP, spacing: { before: 80, after: 80 },
    children: [new ImageRun({ type: "png", data: fs.readFileSync(img.path),
      transformation: { width: Math.round(img.w * scale), height: Math.round(img.h * scale) } })] });
}
/* An exhibit table is as wide as its longest cells need, so a two-column table reads as a small
   ledger rather than a banner across the page; it never exceeds the column. */
function exhibitTable(t) {
  const rows = t.rows.map((r) => r.map(String));
  const need = t.head.map((h, i) => Math.max(String(h).length, ...rows.map((r) => (r[i] || "").length)));
  let widths = need.map((c) => Math.max(1100, 120 * c + 260));
  const total = widths.reduce((a, b) => a + b, 0);
  if (total > CONTENT) widths = widths.map((w) => Math.floor(w * CONTENT / total));
  return grid(t.head, rows, widths, { numbers: true });
}
function chrome(label) {
  return {
    headers: { default: new Header({ children: [new Paragraph({
      border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: RULE, space: 4 } },
      spacing: { after: 120 },
      children: [new TextRun({ text: label, font: SANS, size: TINY, color: MUTED })] })] }) },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [
      new TextRun({ text: "Page ", font: SANS, size: TINY, color: MUTED }),
      new TextRun({ children: [PageNumber.CURRENT], font: SANS, size: SMALL, color: INK }),
      new TextRun({ text: " of ", font: SANS, size: TINY, color: MUTED }),
      new TextRun({ children: [PageNumber.TOTAL_PAGES], font: SANS, size: SMALL, color: INK })] })] }) },
  };
}
const numbering = { config: [
  { reference: "steps", levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.START,
      style: { paragraph: { indent: { left: 400, hanging: 300 } } } }] },
  { reference: "bullets", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.START,
      style: { paragraph: { indent: { left: 400, hanging: 300 } } } }] },
] };
function styles() {
  return { default: { document: { run: { font: SANS, size: BODY, color: INK } } } };
}
function page(children, header) {
  return Object.assign({ properties: { page: { size: { width: PAGE_W, height: PAGE_H },
    margin: { top: 900, bottom: 900, left: MARGIN, right: MARGIN, header: 500, footer: 500 } } },
    children: children }, chrome(header));
}

/* ------------------------------------------------------------------ page one */
function rulesTable(rows) {
  return grid(["Rule", "Detail"], rows, [1500, CONTENT - 1500]);
}
function glanceTable(g) {
  const fixed = [560, 1800, 1200, 900, 680, 900, 680];
  const shows = CONTENT - fixed.reduce((a, b) => a + b, 0);
  const widths = [fixed[0], fixed[1], fixed[2], shows, fixed[3], fixed[4], fixed[5], fixed[6]];
  return grid(g.head, g.rows, widths, { boldLast: true, center: [0, 4, 5, 6, 7], together: true });
}
/* The pacing ribbon: one band per part, as wide as its minutes, with the minute each part starts. */
function pacingRibbon(pacing) {
  const sum = pacing.reduce((a, x) => a + x.minutes, 0) || 1;
  const widths = pacing.map((x) => Math.max(640, Math.round(CONTENT * x.minutes / sum)));
  const over = widths.reduce((a, b) => a + b, 0) - CONTENT;
  widths[widths.indexOf(Math.max.apply(null, widths))] -= over;
  const band = new TableRow({ cantSplit: true, height: { value: 460, rule: HeightRule.ATLEAST }, children: pacing.map((x, i) => cell(
    [p([run("Part " + x.part, { bold: true, size: SMALL, color: i % 2 ? INK : WHITE })],
       { alignment: AlignmentType.CENTER, spacing: { after: 0, line: 240 } }),
     p([run(x.minutes + " min", { size: TINY, color: i % 2 ? INK : WHITE })],
       { alignment: AlignmentType.CENTER, spacing: { after: 0, line: 240 } })],
    widths[i], { fill: i % 2 ? TINT : BRONZE, borders: box(WHITE), margins: { top: 40, bottom: 40, left: 40, right: 40 } })) });
  const marks = new TableRow({ cantSplit: true, children: pacing.map((x, i) => cell(
    [p([run(String(x.start), { size: TINY, color: MUTED })], { spacing: { after: 0, line: 240 } })],
    widths[i], { borders: noBox(), margins: { top: 20, bottom: 0, left: 40, right: 20 } })) });
  return new Table({ width: { size: CONTENT, type: WidthType.DXA }, columnWidths: widths,
    borders: tableBorders(none()), rows: [band, marks] });
}

/* Step one's scale as four numbered boxes, shaded from light to bronze as the claim grows. */
function scaleStrip(steps) {
  const fills = [HEADFILL, TINT, "E2C9A3", BRONZE];
  const w = Math.floor(CONTENT / steps.length);
  const row = new TableRow({ cantSplit: true, children: steps.map((st, i) => cell([
    new Paragraph({ alignment: AlignmentType.CENTER, keepNext: true, spacing: { before: 0, after: 40 },
      children: [new TextRun({ text: st[0], font: SERIF, size: 36, color: i === 3 ? WHITE : BRONZE })] }),
    p([run(st[1], { size: SMALL, color: i === 3 ? WHITE : INK })],
      { alignment: AlignmentType.CENTER, spacing: { after: 0, line: 252 } })],
    w, { fill: fills[i % fills.length], borders: box(WHITE), valign: VerticalAlign.TOP,
         margins: { top: 80, bottom: 100, left: 120, right: 120 } })) });
  return new Table({ width: { size: w * steps.length, type: WidthType.DXA },
    columnWidths: steps.map(() => w), borders: tableBorders(none()), rows: [row] });
}

/* ------------------------------------------------------------------ the paper's blocks */
function labelLine(q, level, label, how) {
  const kids = [run("Q" + q, { bold: true, color: BRONZE, size: 22 }),
                run("   " + level, { bold: true, color: MUTED, size: SMALL }),
                run("  ·  " + label, { color: MUTED, size: SMALL })];
  if (how) kids.push(run("  ·  " + how, { italics: true, color: MUTED, size: SMALL }));
  return p(kids, { keepNext: true, spacing: { before: 60, after: 60, line: 276 } });
}
function optionParas(options, lastKeeps) {
  return options.map((o, i) => p([run(o[0] + ".  ", { bold: true, size: OPTION }), run(o[1], { size: OPTION })],
    { keepNext: lastKeeps || i < options.length - 1, keepLines: true,
      spacing: { before: 0, after: 60, line: 264 }, indent: { left: 360, hanging: 360 } }));
}
/* A working box: room for the steps; the answer itself goes on the answer sheet. */
function workingBox(height, label) {
  return new Table({ width: { size: CONTENT, type: WidthType.DXA }, columnWidths: [CONTENT],
    borders: tableBorders(line(RULE)),
    rows: [new TableRow({ cantSplit: true, height: { value: height || 1500, rule: HeightRule.ATLEAST }, children: [
      cell([p([run(label || "Working", { color: MUTED, size: TINY })], { spacing: { after: 0 } })], CONTENT,
           { valign: VerticalAlign.TOP, margins: { top: 60, bottom: 60, left: 120, right: 120 } })] })] });
}
function itemBlock(item, lead) {
  const kids = (lead || []).concat([labelLine(item.q, item.level, item.label, item.how)]);
  item.lines.forEach((l) => kids.push(p([run(l)], { keepNext: true, spacing: { after: 80, line: 276 } })));
  if (item.options.length) kids.push(...optionParas(item.options, item.answer === "order" || item.answer === "working"));
  if (item.answer === "working") {
    kids.push(spacer(60, true));
    kids.push(workingBox(item.room || 1500, "Working. The final answer goes on the answer sheet."));
  } else if (item.answer === "order") {
    kids.push(p([run("Write the letters in order on the answer sheet.", { color: MUTED, size: TINY })], { spacing: { before: 40, after: 0 } }));
  }
  return block(kids);
}
function exhibitParas(b) {
  const out = [p([run(b.label, { bold: true, color: BRONZE, size: NOTE }),
                  run(b.caption ? "   " + b.caption : "", { italics: true, color: MUTED, size: SMALL })],
                 { keepNext: true, spacing: { before: 80, after: 80 } })];
  if (b.image) out.push(image(b.image));
  if (b.table) out.push(exhibitTable(b.table));
  if (b.code && b.code.length) out.push(...codeLines(b.code));
  return out;
}
/* A set's case and an exhibit are never printed on their own: they open the block of the first item
   that reads them, and a block never splits across pages, so the reader never turns a page between
   an exhibit and its question. */
function caseParas(b) {
  return kept(() => {
    const out = [p([run("Set " + b.n + ".  The case", { bold: true, size: 22 })], { keepNext: true, spacing: { before: 120, after: 60 } }),
                 p([run(b.situation)], { keepNext: true, spacing: { after: 100, line: 276 } })];
    if (b.label || b.image || b.table || (b.code && b.code.length)) out.push(...exhibitParas(b));
    out.push(spacer(140, true));
    return out;
  });
}
function leadParas(b) {
  return kept(() => exhibitParas(b).concat([spacer(140, true)]));
}
/* A word bank: its label, its instruction and its lettered words in a shaded grid of three columns,
   bound to the first item that answers from it. */
function bankParas(b) {
  return kept(() => {
    const cols = 3, w = Math.floor(CONTENT / cols), rows = [];
    for (let r = 0; r < Math.ceil(b.options.length / cols); r++) {
      rows.push(new TableRow({ cantSplit: true, children: Array.from({ length: cols }, (_, c) => {
        const o = b.options[r * cols + c];
        return cell(o ? [p([run(o[0] + "   ", { bold: true, color: BRONZE, size: OPTION }), run(o[1], { size: OPTION })],
                         { keepNext: true, spacing: { after: 0, line: 252 } })] : [p("")], w,
                    { fill: BEIGE, borders: box(WHITE), margins: { top: 60, bottom: 60, left: 140, right: 100 } });
      }) }));
    }
    return [p([run(b.label, { bold: true, color: BRONZE, size: NOTE }),
               run("   " + b.instruction, { italics: true, color: MUTED, size: SMALL })],
              { keepNext: true, spacing: { before: 80, after: 80, line: 264 } }),
            new Table({ width: { size: w * cols, type: WidthType.DXA }, columnWidths: Array(cols).fill(w),
                        borders: tableBorders(line(WHITE)), rows: rows }),
            spacer(140, true)];
  });
}
/* A match table: every item of its bank in one block that never splits, the numbered items on the
   left with their levels and the lettered options on the right. */
function matchBlock(b, lead) {
  const qw = 900, pw = 3900, gap = 200, lw = 520, ow = CONTENT - qw - pw - gap - lw;
  const n = Math.max(b.rows.length, b.options.length);
  const head = new TableRow({ tableHeader: true, cantSplit: true, children: [
    cell([p([run("Item", { bold: true, size: SMALL })], { spacing: { after: 0 } })], qw + pw, { fill: HEADFILL }),
    cell([p("")], gap, { borders: noBox() }),
    cell([p([run("Match", { bold: true, size: SMALL })], { spacing: { after: 0 } })], lw + ow, { fill: HEADFILL })] });
  const body = Array.from({ length: n }, (_, k) => {
    const r = b.rows[k], o = b.options[k];
    return new TableRow({ cantSplit: true, children: [
      cell(r ? [p([run("Q" + r[0], { bold: true, color: BRONZE, size: SMALL })], { spacing: { after: 0 } }),
                p([run(r[1], { color: MUTED, size: TINY })], { spacing: { after: 0 } })] : [p("")], qw),
      cell(r ? [p([run(r[2], { size: OPTION })], { spacing: { after: 0, line: 252 } })] : [p("")], pw),
      cell([p("")], gap, { borders: noBox() }),
      cell(o ? [p([run(o[0], { bold: true, color: BRONZE, size: OPTION })], { alignment: AlignmentType.CENTER, spacing: { after: 0 } })] : [p("")], lw),
      cell(o ? [p([run(o[1], { size: OPTION })], { spacing: { after: 0, line: 252 } })] : [p("")], ow)] });
  });
  const table = new Table({ width: { size: CONTENT, type: WidthType.DXA }, columnWidths: [qw, pw, gap, lw, ow],
    borders: tableBorders(line(RULE)), rows: [head].concat(body) });
  const labelLine = p([run(b.label, { bold: true, color: BRONZE, size: NOTE }),
                       run("   " + b.instruction, { italics: true, color: MUTED, size: SMALL })],
                      { keepNext: true, spacing: { before: 60, after: 80, line: 264 } });
  return block((lead || []).concat([labelLine, table,
    p([run("Write each letter on the answer sheet.", { color: MUTED, size: TINY })], { spacing: { before: 40, after: 0 } })]));
}

/* ------------------------------------------------------------------ the answer sheet */
function sheetCell(text, width, o) {
  o = o || {};
  return new TableCell({ width: { size: width, type: WidthType.DXA }, borders: box(RULE),
    shading: o.fill ? { type: ShadingType.CLEAR, color: "auto", fill: o.fill } : undefined,
    margins: { top: 20, bottom: 20, left: 60, right: 60 }, verticalAlign: VerticalAlign.CENTER,
    children: [new Paragraph({ alignment: o.left ? AlignmentType.LEFT : AlignmentType.CENTER,
      spacing: { before: 20, after: 20, line: 240 },
      children: [new TextRun({ text: String(text), font: SANS, size: o.size || 16, bold: !!o.bold,
                               color: o.color || INK })] })] });
}
/* One grid of lettered items: Q, then a box per letter. A star marks an item with several keys, and
   a letter the item does not offer is shaded, so a box can only be marked where an option exists. */
function letterGrid(rows, letters, key, qw, lw) {
  qw = qw || 640; lw = lw || 420;
  const head = new TableRow({ tableHeader: true, cantSplit: true, children:
    [sheetCell("", qw, { fill: HEADFILL })].concat(letters.map((l) => sheetCell(l, lw, { fill: HEADFILL, bold: true }))) });
  const body = rows.map((r) => new TableRow({ cantSplit: true, height: { value: 280, rule: HeightRule.ATLEAST }, children:
    [sheetCell("Q" + r.q + (r.multi ? "*" : ""), qw)].concat(letters.map((l, i) => {
      const marked = key && (r.key || []).includes(l);
      return sheetCell(marked ? "X" : "", lw, { fill: i < r.count ? undefined : RULE, bold: true, color: BRONZE });
    })) }));
  return new Table({ width: { size: qw + lw * letters.length, type: WidthType.DXA },
    columnWidths: [qw].concat(letters.map(() => lw)), borders: tableBorders(line(RULE)), rows: [head].concat(body) });
}
function columns(tables, widths) {
  const gapW = 300, cols = [], cells = [];
  tables.forEach((t, i) => {
    if (i) {
      cols.push(gapW);
      cells.push(new TableCell({ width: { size: gapW, type: WidthType.DXA }, borders: noBox(), children: [new Paragraph({ children: [] })] }));
    }
    cols.push(widths[i]);
    cells.push(new TableCell({ width: { size: widths[i], type: WidthType.DXA }, borders: noBox(),
      margins: { top: 0, bottom: 0, left: 0, right: 0 }, verticalAlign: VerticalAlign.TOP,
      children: t ? [t, new Paragraph({ spacing: { after: 0 }, children: [] })] : [new Paragraph({ children: [] })] }));
  });
  return new Table({ width: { size: cols.reduce((a, b) => a + b, 0), type: WidthType.DXA }, columnWidths: cols,
    borders: tableBorders(none()), rows: [new TableRow({ children: cells })] });
}
function splitInto(list, k) {
  const out = [], size = Math.ceil(list.length / k);
  for (let i = 0; i < k; i++) out.push(list.slice(i * size, (i + 1) * size));
  return out;
}
function tfGrid(rows, key, qw, lw) {
  qw = qw || 640; lw = lw || 420;
  const head = new TableRow({ tableHeader: true, cantSplit: true, children:
    [sheetCell("", qw, { fill: HEADFILL }), sheetCell("T", lw, { fill: HEADFILL, bold: true }),
     sheetCell("F", lw, { fill: HEADFILL, bold: true })] });
  const body = rows.map((r) => new TableRow({ cantSplit: true, height: { value: 280, rule: HeightRule.ATLEAST }, children: [
    sheetCell("Q" + r.q, qw),
    sheetCell(key && r.key === "T" ? "X" : "", lw, { bold: true, color: BRONZE }),
    sheetCell(key && r.key === "F" ? "X" : "", lw, { bold: true, color: BRONZE })] }));
  return new Table({ width: { size: qw + 2 * lw, type: WidthType.DXA }, columnWidths: [qw, lw, lw],
    borders: tableBorders(line(RULE)), rows: [head].concat(body) });
}
function orderBoxes(n, width) {
  const bw = Math.floor(width / n);
  return new Table({ width: { size: bw * n, type: WidthType.DXA }, columnWidths: Array(n).fill(bw),
    borders: tableBorders(line(RULE)), rows: [new TableRow({ height: { value: 340, rule: HeightRule.ATLEAST }, children: Array.from({ length: n }, (_, i) =>
      new TableCell({ width: { size: bw, type: WidthType.DXA }, borders: box(RULE), margins: { top: 10, bottom: 10, left: 40, right: 40 },
        verticalAlign: VerticalAlign.TOP, children: [new Paragraph({ spacing: { before: 0, after: 0 }, children: [
          new TextRun({ text: String(i + 1), font: SANS, size: 12, color: MUTED })] })] })) })] });
}
function writtenTable(rows, key, width) {
  const qw = 640, kw = 1250, aw = width - qw - kw;
  const head = new TableRow({ tableHeader: true, cantSplit: true, children:
    [sheetCell("", qw, { fill: HEADFILL }), sheetCell("Answer", kw, { fill: HEADFILL, bold: true }),
     sheetCell(key ? "Key" : "Write it here", aw, { fill: HEADFILL, bold: true, left: true })] });
  const body = rows.map((r) => {
    let answerCell;
    if (r.kind === "order" && !key) {
      answerCell = new TableCell({ width: { size: aw, type: WidthType.DXA }, borders: box(RULE),
        margins: { top: 40, bottom: 40, left: 60, right: 60 },
        children: [orderBoxes(r.steps || 4, aw - 140), new Paragraph({ spacing: { after: 0 }, children: [] })] });
    } else {
      answerCell = sheetCell(key ? r.key : "", aw, { left: true, bold: !!key, color: key ? BRONZE : INK, size: 16 });
    }
    return new TableRow({ cantSplit: true, height: { value: 380, rule: HeightRule.ATLEAST }, children: [
      sheetCell("Q" + r.q, qw), sheetCell(r.kindLabel, kw, { color: MUTED, size: 14 }), answerCell] });
  });
  return new Table({ width: { size: width, type: WidthType.DXA }, columnWidths: [qw, kw, aw],
    borders: tableBorders(line(RULE)), rows: [head].concat(body) });
}
function ratingsGrid(parts, counts) {
  const bw = 620, rw = counts ? 1900 : 0, lw = CONTENT - 4 * bw - rw;
  const widths = [lw, bw, bw, bw, bw].concat(counts ? [rw] : []);
  const head = new TableRow({ tableHeader: true, cantSplit: true, children:
    [sheetCell("Part", lw, { fill: HEADFILL, bold: true, left: true })]
      .concat([1, 2, 3, 4].map((k) => sheetCell(String(k), bw, { fill: HEADFILL, bold: true })))
      .concat(counts ? [sheetCell("Items right (marker)", rw, { fill: HEADFILL, bold: true })] : []) });
  const body = parts.map((t, i) => new TableRow({ cantSplit: true, height: { value: 280, rule: HeightRule.ATLEAST }, children:
    [sheetCell(t, lw, { left: true })].concat([1, 2, 3, 4].map(() => sheetCell("", bw)))
      .concat(counts ? [sheetCell("____ of " + counts[i], rw, { color: MUTED })] : []) }));
  return new Table({ width: { size: CONTENT, type: WidthType.DXA }, columnWidths: widths,
    borders: tableBorders(line(RULE)), rows: [head].concat(body) });
}
/* The answer sheet's grids on one page: the lettered items in three columns with the true or false
   items in a fourth, then the written answers in two columns across the page. */
function answerGrids(sheet, key) {
  const out = [];
  const letters = sheet.letterColumns;
  const lw = 420, qw = 640;
  const letterW = qw + lw * letters.length, tfW = qw + 2 * lw;
  if (sheet.letters.length || sheet.tf.length) {
    out.push(h2(key ? "Lettered items, and true or false" :
      "Lettered items: one box, or every correct box for a starred item. True or false: one box", 120));
    const chunks = splitInto(sheet.letters, 3).filter((c) => c.length);
    const tables = chunks.map((c) => letterGrid(c, letters, key, qw, lw));
    const widths = chunks.map(() => letterW);
    if (sheet.tf.length) { tables.push(tfGrid(sheet.tf, key, qw, lw)); widths.push(tfW); }
    out.push(columns(tables, widths));
    if (sheet.letters.some((r) => r.multi)) {
      out.push(p([run("* Mark every correct box. A shaded box is a letter the item does not offer.", { color: MUTED, size: TINY })],
                 { spacing: { before: 40, after: 60 } }));
    }
  }
  if (sheet.written.length) {
    out.push(h2(key ? "The written answers" : "Letters, words, numbers and orders: one answer per space", 140));
    const halves = splitInto(sheet.written, 2).filter((c) => c.length);
    const w = Math.floor((CONTENT - 300 * (halves.length - 1)) / halves.length);
    out.push(columns(halves.map((h) => writtenTable(h, key, w)), halves.map(() => w)));
  }
  return out;
}
function answerSheet(sheet) {
  const out = [new Paragraph({ pageBreakBefore: true, spacing: { before: 0, after: 60 },
      children: [new TextRun({ text: sheet.title, font: SERIF, size: 40, color: BRONZE })] }),
    p([run(sheet.note, { color: MUTED, size: NOTE })], { spacing: { after: 120, line: 276 } }),
    bronzeRule(160),
    grid(["Name", "Seat", "Marked by", "Items right"], [["", "", "", "____ of " + sheet.n]],
         [3900, 1300, 2700, CONTENT - 3900 - 1300 - 2700])];
  out.push(h2("Step one: rate each part before you read any item", 200));
  out.push(ratingsGrid(sheet.parts, sheet.partItems));
  out.push(p([run(sheet.scale, { color: MUTED, size: TINY })], { spacing: { before: 60, after: 60 } }));
  out.push(...answerGrids(sheet, false));
  return out;
}

/* ------------------------------------------------------------------ the paper */
function paperDoc(s) {
  const kids = [
    title(s.title), subtitle(s.subtitle), bronzeRule(),
    h2("What this paper is for", 0), p([run(s.purpose)], { spacing: { after: 120, line: 276 } }),
    h2("Rules"), rulesTable(s.rules),
    h2("Step one, before Part 1"), p([run(s.stepOne.intro)], { keepNext: true, spacing: { after: 100, line: 276 } }),
    scaleStrip(s.stepOne.steps),
    muted(s.stepOne.areas, { keepNext: false, spacing: { before: 60, after: 80 } }),
    h2("The paper at a glance"), glanceTable(s.glance),
    h2("Pacing"), muted(s.pacingNote, { spacing: { after: 80 } }), pacingRibbon(s.pacing),
  ];
  s.sections.forEach((sec) => {
    kids.push(partHeading(sec.heading));
    kids.push(muted(sec.intro));
    if (sec.situation) kids.push(p([run(sec.situation)], { keepNext: true, spacing: { after: 140, line: 276 } }));
    let lead = [], first = true;
    sec.blocks.forEach((b) => {
      if (b.kind === "set") lead = lead.concat(caseParas(b));
      else if (b.kind === "exhibit") lead = lead.concat(leadParas(b));
      else if (b.kind === "bank") lead = lead.concat(bankParas(b));
      else {
        if (!first) kids.push(spacer(120));
        kids.push(b.kind === "match" ? matchBlock(b, lead) : itemBlock(b, lead)); lead = []; first = false;
      }
    });
    kids.push(...lead);
  });
  if (s.stretch && s.stretch.items.length) {
    kids.push(new Paragraph({ pageBreakBefore: true, spacing: { before: 0, after: 120 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: BRONZE, space: 4 } },
      children: [new TextRun({ text: s.stretch.title, font: SERIF, size: 30, color: BRONZE })] }));
    kids.push(muted(s.stretch.intro));
    s.stretch.items.forEach((it, i) => {
      const inner = [p([run("Stretch " + it.n, { bold: true, color: BRONZE, size: 22 }),
                        run(it.short ? "   Recall  ·  one line" : "   Written  ·  the answer you would say aloud",
                            { color: MUTED, size: SMALL })],
                       { keepNext: true, spacing: { before: 60, after: 60 } })];
      it.lines.forEach((l) => inner.push(p([run(l)], { keepNext: true, spacing: { after: 80, line: 276 } })));
      if (it.options && it.options.length) inner.push(...optionParas(it.options, true));
      inner.push(it.short ? p([run("Answer:  ", { color: MUTED }), run("_".repeat(40), { color: MUTED })], { spacing: { before: 60 } })
                          : workingBox(1700, "Your answer"));
      if (i) kids.push(spacer(140));
      kids.push(block(inner));
    });
  }
  kids.push(...answerSheet(s.sheet));
  return new Document({ creator: "C2 content factory", title: s.title, styles: styles(), numbering: numbering,
    sections: [page(kids, s.header)] });
}

/* ------------------------------------------------------------------ the key */
function keyDoc(k) {
  const kids = [title(k.title), subtitle(k.meta), bronzeRule(), h2("Marking", 0)];
  k.marking.forEach((m) => kids.push(new Paragraph({ numbering: { reference: "steps", level: 0 },
    spacing: { after: 60, line: 276 }, children: [run(m)] })));
  if (k.blueprint && k.blueprint.rows.length) { kids.push(h2("The blueprint")); kids.push(glanceTable(k.blueprint)); }
  if (k.guessing) { kids.push(h2("What guessing alone would score")); kids.push(p([run(k.guessing)], { spacing: { after: 80, line: 276 } })); }
  if (k.itemReading) { kids.push(h2("Reading the items after marking")); kids.push(p([run(k.itemReading)], { spacing: { after: 80, line: 276 } })); }
  kids.push(h2("The key"));
  kids.push(grid(["Q", "Key", "Type", "Part", "Level", "Tag", "Day", "Source"], k.rows,
                 [560, 1900, 2100, 600, 900, 700, 700, CONTENT - 560 - 1900 - 2100 - 600 - 900 - 700 - 700],
                 { center: [0, 3, 5, 6] }));
  if (k.reasons.length) {
    kids.push(new Paragraph({ pageBreakBefore: true, spacing: { before: 0, after: 120 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: BRONZE, space: 4 } },
      children: [new TextRun({ text: "Why each answer holds", font: SERIF, size: 30, color: BRONZE })] }));
    k.reasons.forEach((r) => {
      const inner = [p([run("Q" + r.q, { bold: true, color: BRONZE, size: 22 }), run("   Key " + r.key, { bold: true }),
                        run("   " + r.meta, { color: MUTED, size: SMALL })], { keepNext: true, spacing: { before: 60, after: 60 } })];
      if (r.why) inner.push(p([run("Why it holds.  ", { bold: true }), run(r.why)], { keepNext: true, spacing: { after: 60, line: 276 } }));
      r.wrong.forEach((w) => inner.push(p([run(w[0] + ".  ", { bold: true, size: OPTION }), run(w[1], { size: OPTION })],
        { keepNext: true, spacing: { after: 40, line: 264 }, indent: { left: 360, hanging: 360 } })));
      if (r.answer) inner.push(p([run("In the interview.  ", { bold: true }), run(r.answer)],
                                 { keepNext: !!r.anchor, spacing: { before: 60, after: 40, line: 276 } }));
      if (r.anchor) inner.push(p([run("Anchor: " + r.anchor, { color: MUTED, size: SMALL })], { spacing: { after: 0 } }));
      kids.push(block(inner)); kids.push(spacer(160));
    });
  }
  kids.push(h2("For the tally"));
  k.tally.forEach((t) => kids.push(new Paragraph({ numbering: { reference: "bullets", level: 0 }, spacing: { after: 40 }, children: [run(t)] })));
  if (k.additions.length) {
    kids.push(h2("New items waiting for the tracker"));
    kids.push(p([run(k.additionsNote)]));
    k.additions.forEach((a) => kids.push(new Paragraph({ numbering: { reference: "bullets", level: 0 }, spacing: { after: 40 }, children: [run(a)] })));
  }
  if (k.folded && k.folded.length) {
    kids.push(h2("Bank items folded into deeper items"));
    kids.push(p([run(k.foldedNote)]));
    k.folded.forEach((a) => kids.push(new Paragraph({ numbering: { reference: "bullets", level: 0 }, spacing: { after: 40 }, children: [run(a)] })));
  }
  if (k.stretch.length) {
    kids.push(h2("The stretch page"));
    k.stretch.forEach((s, i) => kids.push(p([run("Stretch " + (i + 1) + ".  ", { bold: true, color: BRONZE }), run(s)], { spacing: { after: 80, line: 276 } })));
  }
  if (k.grid) {
    kids.push(new Paragraph({ pageBreakBefore: true, spacing: { before: 0, after: 60 },
      children: [new TextRun({ text: "Marking grid", font: SERIF, size: 40, color: BRONZE })] }));
    kids.push(p([run(k.grid.note, { color: MUTED, size: NOTE })], { spacing: { after: 120, line: 276 } }));
    kids.push(bronzeRule(160));
    kids.push(...answerGrids(k.grid, true));
  }
  return new Document({ creator: "C2 content factory", title: k.title, styles: styles(), numbering: numbering,
    sections: [page(kids, k.header)] });
}

(async () => {
  fs.mkdirSync(path.dirname(paperOut), { recursive: true });
  fs.mkdirSync(path.dirname(keyOut), { recursive: true });
  fs.writeFileSync(paperOut, await Packer.toBuffer(paperDoc(spec.paper)));
  fs.writeFileSync(keyOut, await Packer.toBuffer(keyDoc(spec.key)));
  console.log("wrote " + paperOut + "\nwrote " + keyOut);
})();
