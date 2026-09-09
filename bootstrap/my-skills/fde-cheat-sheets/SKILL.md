---
name: fde-cheat-sheets
description: Build at-a-glance cheat sheets for FDE Academy learners and working FDEs on any GenAI, engineering or consultancy scope, whether a topic (RAG, GraphRAG, agent protocols), a module recap, interview preparation, a first client project, or FDE working behaviours. Use whenever the user asks for a cheat sheet, quick reference, one-pager, crib sheet, ready reckoner, at-a-glance recap or revision sheet, with or without source material, since a sheet can be built from live research alone. Produces one landscape page (two at most) in the programme design system plus a Markdown companion, with every fact live-verified. Not for post-session study notes, which fde-study-notes owns.
---

# FDE cheat sheets

Compress one scope into a landscape page a learner can scan in seconds, pin above a desk, and trust under pressure, because everything on it was verified at build time.

## The envelope

| Item | Rule |
|---|---|
| Reader and moment | A learner mid-build or mid-revision, a candidate the night before an interview, or an FDE in a client room; the sheet is scanned in seconds, so it is judged by what a ten-second look retrieves. |
| Inputs | All optional: a transcript, a deck, code files, links, or nothing at all, in which case the sheet is built from live research. When materials arrive, harvest them under the fde-study-notes harvesting rules. |
| Size | One landscape A4 page by default; a second page only when the scope genuinely needs it, and never a third. Cutting a block beats shrinking the type. |
| Neutrality | No trainer names, dates, clock times or cohort numbers, with one permitted exception: the verification stamp in the title band, because a sheet that gets memorised must declare how fresh its facts are. A phase tag may appear when the fde-study-notes curriculum map is installed to read from; skip the tag silently when it is absent or the scope is phase-free (interview prep, working behaviours). |

## Workflow, in order

1. Read references/sheet-anatomy.md and hold the anatomy while gathering, because knowing the block palette changes what you look for.
2. Name the scope and the reader's moment in one sentence each before collecting anything, since a sheet for the client room keeps different blocks than a sheet for a build session.
3. Gather. Mine whatever was supplied, then research the scope live: current definitions, the variants practitioners actually distinguish, the numbers worth memorising, and the mistakes that appear in real incident write-ups and engineering blogs. A sheet built from stale memory is worse than no sheet.
4. Verify at the strictest bar in the programme, because a cheat sheet gets memorised: every number carries its source and year on the sheet, every claim that fails live verification is dropped, contested claims are either marked contested or left off, and anything invented here (a framework, an acronym, a rule of thumb of ours) is labelled as coined for this programme.
5. Curate down to five to nine blocks. For every candidate block ask what a reader loses if it goes; when the answer is nothing they would miss under pressure, it goes. The sheet is defined by what it leaves out.
6. Compose against the anatomy: title band, one anchor visual, the block grid in the fixed colour code, the foot strip. Author it as HTML on the grid in assets/sheet-style.css, with the anchor drawn as inline SVG or a generated image in the house palette.
7. Scrub. Run the llm-tic-scrubber scanner on all sheet text, then the dash and banned-word scans. The density rules in the anatomy file govern where short clauses are allowed.
8. Render with weasyprint (pip install weasyprint --break-system-packages when missing), rasterise the page with pdftoppm and look at it, fixing overflow, collisions and unreadable type before delivering. A sheet that fails the ten-second scan gets recomposed, never excused.
9. Write the Markdown companion: the same blocks flattened into sections in the same order, images referenced beside it, so the sheet lives in the GitHub repos too.
10. Deliver with present_files: the PDF first, then a zip of the Markdown with its images.

## Design system, established from the programme curriculum PDFs

Poppins Bold and Medium for headings with Liberation Sans body, on the fixed palette: pink #FF4989, magenta #C2007A, dark navy #1A1A2E, body grey #3F3F58, muted #8A88A4, grid #E4E2EE, rose #FFF1F6. assets/sheet-style.css encodes the landscape grid and the block colour code; do not restyle per sheet, because learners should learn the colour code once and read every sheet faster for it.

## Quality bar

- The anchor test: cover every block except the anchor visual, and the anchor alone should still recap the whole concept; when it cannot, the anchor is decoration and gets redrawn.
- The pressure test: pick three questions the reader's moment actually produces ("which retrieval do I reach for", "what number do I quote", "what do I check first") and confirm each is answerable from the sheet inside ten seconds.
- The swap test from the study notes applies with more force: a sheet whose blocks survive a topic-name swap is a template wearing a topic, and gets rebuilt.
- Nothing invented without a label, and nothing memorisable without a source.

## Scope boundaries

fde-study-notes owns post-session study notes; a session can yield both, and they never merge. Pre-reads belong to a separate skill. When the user wants the sheet taught rather than pinned, that is training-deck-builder territory.
