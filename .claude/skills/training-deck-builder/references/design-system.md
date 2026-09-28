# Design system and build pipeline

In this repository one visual system serves every deck, and it is the Programme Head's academic
orientation deck, version 3. Its values live in `scripts/brand.py`, its slide furniture in
`scripts/deck_layout.py`, and `scripts/build_deck.py` turns a markdown source into the .pptx. The
model decks are `content/W01/D1/slides/`. The cheat sheets, the notebook helper and the companion
pages read the same values, so a drawing looks the same everywhere a learner meets it.

## Palette

| Token in `brand.py` | Hex | Used for |
|---|---|---|
| `INK` | `1A0F5C` | Titles, strong text, the dark surface, a table's header band |
| `NIGHT` | `1A1440` | Body text and code cards |
| `VIOLET` | `5B3FD6` | The one accent: eyebrows, icons, the current step |
| `LAVENDER` | `D9A7FF` | Numerals and highlights on the dark surface |
| `MUTED` | `6B6690` | Subtitles and secondary text, never a rule or a verdict |
| `LILAC` | `CFC9EE` | Borders and inactive steps |
| `LINE` | `E4E1F1` | Hairlines and card borders |
| `TINT` | `EEEAFB` | Icon circles and light strips |
| `SURFACE` | `F4F2FA` | Alternate table rows |
| `GREEN` on `GREEN_TINT` | `1F8A5B` on `E8F5EE` | What holds, what is right |
| `ROSE` on `ROSE_TINT` | `D63A6A` on `FCEBF0` | What breaks, what is wrong |

Green and rose carry meaning only. The cover and the chapter openers sit on the dark indigo surface
and every content slide on the light one; both backgrounds are images in `scripts/assets/brand/`.

## Type and geometry

Georgia for titles, Calibri for body text and Consolas for code, as `brand.py` names them. The slide
is 13.333 by 7.5 inches with a 0.58 inch side margin; the header chrome sits at 0.22, the title from
0.74, the subtitle at 1.30, the body from 1.84 to 6.78 and the footer at 6.98. A title runs to at
most 54 characters, which `deck_md_check.py` enforces.

## What a source can ask for

The docstring of `scripts/build_deck.py` is the syntax, and the docstring of `scripts/deck_layout.py`
is the shape each part takes. In short: a cover with the client's words (`Quote:` and `Who:`),
chapter openers (`## SECTION n:`), content slides (`## S3.`), self-study depth slides (`## D10.`),
the three beat strips (`**The client asks.**`, `**Kavya's review.**`, `**In the interview.**`), a
breadcrumb, tables, code windows, a quote with its speaker, and the `cards`, `stats`, `timeline`,
`bar` and `notes` fences.

## Diagrams

Every diagram is a Mermaid fence, rendered through mermaid-cli with the programme's theme (the
`MERMAID_CONFIG` in `scripts/build_cheatsheet.py`). The builder chooses the layout that prints every
label between 9 and 18 points, and a picture beside its words wins over the same picture squeezed
under them when it prints larger. Meaning is carried by four class styles, written into the fence as
the model decks write them:

```
classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
classDef unknown fill:#FFFFFF,stroke:#B8B2D6,color:#6B6690,stroke-dasharray:4 3
classDef bet fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
```

## Build and check

```bash
python3 scripts/build_deck.py content/W01/D1/slides/C2_W01_D01_half1_STUDENT.md
python3 scripts/deck_md_check.py content/W01/D1/slides
python3 scripts/deck_check.py content/W01/D1/slides/C2_W01_D01_half1_STUDENT.pptx --png <scratch>/half1.png
```

`deck_md_check.py` reads the markdown, which is the deck the gate can see; `deck_check.py` measures
every text box of the built file and saves a contact sheet. `verify.py` runs both, and skips a .pptx
older than its markdown, because that file is stale and gets rebuilt.

## Rendering for visual QA

```bash
soffice --headless --convert-to pdf --outdir <scratch> content/W01/D1/slides/C2_W01_D01_half1_STUDENT.pptx
pdftoppm -jpeg -r 80 <scratch>/C2_W01_D01_half1_STUDENT.pdf <scratch>/half1
```

Install the Carlito font first (the `fonts-crosextra-carlito` package), which has Calibri's metrics,
so body text wraps as it will on a trainer's laptop. Georgia falls back to a wider serif in the
container, so a title that fits in the render fits in the room. Look at every slide: text overflow
first, then overlaps, then uneven gaps. Fix in the markdown or in the builder, never in the .pptx.

## Gotchas that have cost real time

- **A .pptx older than its markdown is stale.** Rebuild it rather than editing it; hand edits are
  lost on the next build.
- **Speaker notes go in a `notes` fence**, never in a text box, and a deck that carries one fence
  must carry one on every body slide.
- **Mermaid labels are drawn as SVG text**, never as HTML, because an HTML label is dropped without
  warning by the renderers the pipeline uses and prints as an empty box.
- **Scan the built output as well as the source** for em-dashes and invisible characters; `verify.py`
  runs the style sweep on every file in the pack.
