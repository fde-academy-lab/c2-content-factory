/* saturday_docx.js: write a Saturday recap paper and its key as Word files.
 *
 * scripts/build_saturday_paper.py --docx assembles the paper from the tracker's bank and the week's
 * source file, renders every scenario set's exhibit to a PNG, and hands this script one JSON spec:
 *
 *     node scripts/saturday_docx.js spec.json paper.docx key.docx
 *
 * The layout follows the requester's baseline diagnostic: a rules table, the paper at a glance,
 * one bordered card per item, each scenario set's situation and exhibit printed once, and an
 * answer sheet at the end. The key is a TRAINER file: the key table, why each answer holds, why
 * each other option fails, the interview answer in one breath, and the tallies for Monday.
 */
"use strict";
const fs = require("fs");
const path = require("path");
let docx;
try { docx = require("docx"); } catch (e) { docx = require("/opt/node22/lib/node_modules/docx"); }
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType,
  BorderStyle, AlignmentType, ImageRun, PageBreak, LevelFormat, Header, Footer, PageNumber,
} = docx;

const INK = "1A0F5C", VIOLET = "5B3FD6", MUTED = "6B6690", LINE = "CFC9EE", TINT = "EEEAFB", SURFACE = "F4F2FA";
const PAGE_W = 11906, MARGIN = 1050, CONTENT = PAGE_W - 2 * MARGIN;
const BODY = 21, SMALL = 18;

const [specPath, paperOut, keyOut] = process.argv.slice(2);
const spec = JSON.parse(fs.readFileSync(specPath, "utf8"));

function run(text, opts) { return new TextRun(Object.assign({ text: String(text), size: BODY, color: INK }, opts || {})); }
function para(children, opts) {
  if (typeof children === "string") children = [run(children)];
  return new Paragraph(Object.assign({ children: children, spacing: { after: 80 } }, opts || {}));
}
function heading(text, size, before) {
  return new Paragraph({ spacing: { before: before === undefined ? 240 : before, after: 100 },
    children: [new TextRun({ text: text, font: "Georgia", size: size || 30, color: INK })] });
}
function border(colour) {
  const b = { style: BorderStyle.SINGLE, size: 6, color: colour || LINE };
  return { top: b, bottom: b, left: b, right: b };
}
function cell(children, width, opts) {
  opts = opts || {};
  return new TableCell({
    width: { size: width, type: WidthType.DXA }, borders: border(opts.border),
    shading: opts.fill ? { type: ShadingType.CLEAR, color: "auto", fill: opts.fill } : undefined,
    margins: { top: 90, bottom: 90, left: 140, right: 140 },
    children: children.length ? children : [para("")],
  });
}
function grid(head, rows, widths, opts) {
  opts = opts || {};
  const total = widths.reduce((a, b) => a + b, 0);
  const headRow = new TableRow({ tableHeader: true, children: head.map((h, i) => cell(
    [para([run(h, { bold: true, color: "FFFFFF", size: SMALL })])], widths[i], { fill: INK, border: INK })) });
  const body = rows.map((r, n) => new TableRow({ children: r.map((v, i) => cell(
    [para([run(v, { size: opts.size || SMALL, bold: i === 0 && opts.boldFirst })])], widths[i],
    { fill: n % 2 ? SURFACE : undefined })) }));
  return new Table({ width: { size: total, type: WidthType.DXA }, columnWidths: widths, rows: [headRow].concat(body) });
}
function card(children, opts) {
  opts = opts || {};
  return new Table({ width: { size: CONTENT, type: WidthType.DXA }, columnWidths: [CONTENT],
    rows: [new TableRow({ cantSplit: true, children: [cell(children, CONTENT, opts)] })] });
}
function gap(after) { return new Paragraph({ spacing: { after: after || 120 }, children: [] }); }
function image(img) {
  const maxW = 610, scale = Math.min(1, maxW / img.w);
  return new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 60, after: 60 }, children: [
    new ImageRun({ type: "png", data: fs.readFileSync(img.path),
                   transformation: { width: Math.round(img.w * scale), height: Math.round(img.h * scale) } })] });
}
function exhibitTable(t) {
  const n = t.head.length, w = Math.floor((CONTENT - 280) / n);
  return grid(t.head, t.rows, Array(n).fill(w), { size: SMALL });
}
function chrome(label) {
  return {
    headers: { default: new Header({ children: [new Paragraph({ children: [
      new TextRun({ text: label, size: 16, color: MUTED })] })] }) },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [
      new TextRun({ children: ["Page ", PageNumber.CURRENT, " of ", PageNumber.TOTAL_PAGES], size: 16, color: MUTED })] })] }) },
  };
}
const numbering = { config: [
  { reference: "steps", levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.START,
      style: { paragraph: { indent: { left: 400, hanging: 280 } } } }] },
  { reference: "bullets", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.START,
      style: { paragraph: { indent: { left: 400, hanging: 280 } } } }] },
] };
function styles() {
  return { default: { document: { run: { font: "Calibri", size: BODY, color: INK } } } };
}

/* ------------------------------------------------------------------ the paper */
function itemCard(item) {
  const kids = [para([run("Q" + item.q, { bold: true, color: VIOLET, size: 24 }),
                      run("   " + item.type, { color: MUTED, size: SMALL })], { spacing: { after: 60 } })];
  item.lines.forEach((l) => kids.push(para(l)));
  item.options.forEach((o) => kids.push(para([run("(" + o[0] + ")  ", { bold: true, color: VIOLET }), run(o[1])],
                                              { indent: { left: 240 }, spacing: { after: 40 } })));
  if (item.answer === "working") {
    kids.push(para([run("Working", { color: MUTED, size: SMALL })], { spacing: { before: 80, after: 900 } }));
    kids.push(para([run("Answer:  ______________________________", { color: MUTED })]));
  } else if (item.answer === "order") {
    kids.push(para([run("Order:  ______________________________", { color: MUTED })], { spacing: { before: 80 } }));
  } else if (item.answer === "line") {
    kids.push(para([run("Answer:  ______________________________", { color: MUTED })], { spacing: { before: 80 } }));
  }
  return card(kids);
}
function setCard(block) {
  const kids = [para([run("Set " + block.n + ".  Situation", { bold: true, color: VIOLET, size: 22 })])];
  kids.push(para(block.situation));
  if (block.image) kids.push(image(block.image));
  if (block.table) kids.push(exhibitTable(block.table));
  if (block.caption) kids.push(para([run(block.caption, { italics: true, color: MUTED, size: SMALL })],
                                    { alignment: AlignmentType.CENTER }));
  return card(kids, { fill: SURFACE, border: VIOLET });
}
function answerSheet(sheet) {
  const out = [new Paragraph({ children: [new PageBreak()] }), heading("Answer sheet", 30, 0),
    para([run(sheet.note, { color: MUTED, size: SMALL })]),
    grid(["Name", "Marked by", "Items right"], [["", "", "____ of " + sheet.n]], [4200, 3406, 2200]), gap(160)];
  const letters = ["a", "b", "c", "d", "e", "f"];
  const rows = sheet.rows.map((r) => {
    const marks = r.kind === "tf" ? "T      F" : r.kind === "choice"
      ? letters.slice(0, r.count).map((l) => "○ " + l).join("     ") : "______________________________";
    return ["Q" + r.q, marks];
  });
  const half = Math.ceil(rows.length / 2);
  const w = [700, CONTENT / 2 - 760];
  /* A tight cell, so a paper of about sixty items fits its answer sheet on one page. */
  function tight(text, width, bold) {
    return new TableCell({ width: { size: width, type: WidthType.DXA }, borders: border(),
      margins: { top: 30, bottom: 30, left: 110, right: 110 },
      children: [new Paragraph({ spacing: { after: 0 }, children: [run(text, { size: 17, bold: bold, color: bold ? VIOLET : INK })] })] });
  }
  const pairs = [];
  for (let i = 0; i < half; i++) {
    const a = rows[i], b = rows[i + half] || ["", ""];
    pairs.push(new TableRow({ cantSplit: true, children: [
      tight(a[0], w[0], true), tight(a[1], w[1], false), tight(b[0], w[0], true), tight(b[1], w[1], false),
    ] }));
  }
  out.push(new Table({ width: { size: 2 * (w[0] + w[1]), type: WidthType.DXA }, columnWidths: [w[0], w[1], w[0], w[1]], rows: pairs }));
  return out;
}
function paperDoc(p) {
  const kids = [
    new Paragraph({ spacing: { after: 60 }, children: [new TextRun({ text: p.title, font: "Georgia", size: 44, color: INK })] }),
    para([run(p.meta, { color: MUTED })], { spacing: { after: 200 } }),
    heading("What this paper is for", 26, 120), para(p.purpose),
    heading("Rules", 26), grid(["Rule", "Detail"], p.rules, [1800, CONTENT - 1800], { boldFirst: true }),
    heading("The paper at a glance", 26), grid(["Section", "What it asks of you", "Items", "Minutes"], p.glance,
                                               [2600, CONTENT - 2600 - 1500 - 1000, 1500, 1000]),
  ];
  p.sections.forEach((s) => {
    kids.push(new Paragraph({ children: [new PageBreak()] }));
    kids.push(heading(s.letter + ". " + s.title, 30, 0));
    kids.push(para([run(s.intro, { color: MUTED })], { spacing: { after: 160 } }));
    s.blocks.forEach((b) => { kids.push(b.kind === "set" ? setCard(b) : itemCard(b)); kids.push(gap(100)); });
  });
  if (p.stretch && p.stretch.length) {
    kids.push(new Paragraph({ children: [new PageBreak()] }));
    kids.push(heading(p.stretchTitle, 30, 0));
    kids.push(para([run(p.stretchIntro, { color: MUTED })], { spacing: { after: 160 } }));
    p.stretch.forEach((s, i) => {
      const inner = [para([run("Stretch " + (i + 1), { bold: true, color: VIOLET, size: 22 })])];
      s.lines.forEach((l) => inner.push(para(l)));
      inner.push(para([run("", {})], { spacing: { after: 1400 } }));
      kids.push(card(inner)); kids.push(gap(100));
    });
  }
  kids.push(...answerSheet(p.sheet));
  return new Document({ creator: "C2 content factory", title: p.title, styles: styles(), numbering: numbering,
    sections: [Object.assign({ properties: { page: { margin: { top: 900, bottom: 900, left: MARGIN, right: MARGIN } } },
                               children: kids }, chrome(p.header))] });
}

/* ------------------------------------------------------------------ the key */
function keyDoc(k) {
  const kids = [
    new Paragraph({ spacing: { after: 60 }, children: [new TextRun({ text: k.title, font: "Georgia", size: 40, color: INK })] }),
    para([run(k.meta, { color: MUTED })], { spacing: { after: 160 } }),
    heading("Marking", 26, 120),
  ];
  k.marking.forEach((m) => kids.push(new Paragraph({ numbering: { reference: "steps", level: 0 }, spacing: { after: 60 }, children: [run(m)] })));
  kids.push(heading("The key", 26));
  kids.push(grid(["Q", "Key", "Type", "Level", "Tag", "Day", "Source"], k.rows,
                 [600, 1500, 2300, 1100, 900, 900, CONTENT - 600 - 1500 - 2300 - 1100 - 900 - 900]));
  if (k.reasons.length) {
    kids.push(new Paragraph({ children: [new PageBreak()] }));
    kids.push(heading("Why each answer holds", 30, 0));
    k.reasons.forEach((r) => {
      const inner = [para([run("Q" + r.q, { bold: true, color: VIOLET, size: 24 }), run("   key " + r.key, { bold: true }),
                           run("   " + r.meta, { color: MUTED, size: SMALL })])];
      if (r.why) inner.push(para([run("Why it holds.  ", { bold: true }), run(r.why)]));
      r.wrong.forEach((w) => inner.push(new Paragraph({ numbering: { reference: "bullets", level: 0 }, spacing: { after: 40 },
        children: [run("(" + w[0] + ")  ", { bold: true, color: VIOLET }), run(w[1])] })));
      if (r.answer) inner.push(para([run("In the interview.  ", { bold: true }), run(r.answer)], { spacing: { before: 60 } }));
      if (r.anchor) inner.push(para([run("Anchor: " + r.anchor, { color: MUTED, size: SMALL })]));
      kids.push(card(inner)); kids.push(gap(90));
    });
  }
  kids.push(heading("For the tally", 26));
  k.tally.forEach((t) => kids.push(new Paragraph({ numbering: { reference: "bullets", level: 0 }, spacing: { after: 40 }, children: [run(t)] })));
  if (k.additions.length) {
    kids.push(heading("New items waiting for the tracker", 26));
    kids.push(para(k.additionsNote));
    k.additions.forEach((a) => kids.push(new Paragraph({ numbering: { reference: "bullets", level: 0 }, spacing: { after: 40 }, children: [run(a)] })));
  }
  if (k.stretch.length) {
    kids.push(heading("The stretch page", 26));
    k.stretch.forEach((s, i) => kids.push(para([run("Stretch " + (i + 1) + ".  ", { bold: true, color: VIOLET }), run(s)])));
  }
  return new Document({ creator: "C2 content factory", title: k.title, styles: styles(), numbering: numbering,
    sections: [Object.assign({ properties: { page: { margin: { top: 900, bottom: 900, left: MARGIN, right: MARGIN } } },
                               children: kids }, chrome(k.header))] });
}

(async () => {
  fs.mkdirSync(path.dirname(paperOut), { recursive: true });
  fs.mkdirSync(path.dirname(keyOut), { recursive: true });
  fs.writeFileSync(paperOut, await Packer.toBuffer(paperDoc(spec.paper)));
  fs.writeFileSync(keyOut, await Packer.toBuffer(keyDoc(spec.key)));
  console.log("wrote " + paperOut + "\nwrote " + keyOut);
})();
