---
name: fde-study-notes
description: Build post-session study notes for FDE Academy learners from a delivered session. Use this skill whenever the user asks for study notes, a study guide, session notes, learner notes, revision notes, or a recap for students of any FDE Academy session (Tech, Apply, Consultancy, build or consultant sessions), and whenever a session transcript, recording summary or deck arrives with intent to produce learner material, even when the ask is only "make the notes for yesterday's session". Produces one locked nine-section note as Markdown plus a styled PDF in the programme design system, with live-verified facts and links. Not for pre-session pre-reads, and not for delivery gap analysis, which session-debrief owns.
---

# FDE study notes

Turn one delivered FDE Academy session into a study note a learner absorbs in about 25 minutes, shipped as Markdown plus a styled PDF, with every outside fact verified at build time.

## Inputs and the envelope

| Item | Rule |
|---|---|
| Transcript | Expect one and read it fully, since it is the ground truth for what was covered and how it was explained. |
| Deck, code files or other materials | Use them when supplied, harvest them under the rules below, and never wait for them or assume they exist. |
| Neither supplied | Ask for the session topic and a coverage list, and never reconstruct a session from guesswork. |
| Reader | An FDE Academy learner revising solo after the session, on a laptop or a phone. |
| Budget | About a 25-minute read across 10 to 12 A4 pages, plus a 15 to 20 minute self-challenge; when a draft runs over, cut trivia and history first and keep every concept. |
| Neutrality | No trainer names, no dates, no clock times, no cohort numbers; weekdays and durations only, so one note serves every cohort. |

## Workflow, in order

1. Read references/note-template.md for the locked sections and writing rules, and references/curriculum-map.md for phase placement, the landscape canvas and the skills-unlocked language. Read the concept-packaging skill for the four-beat rhythm and sticky handles before drafting any concept.
2. Mine the transcript. List every concept taught, every term used (these seed the glossary), every example given, and every question learners asked. Learner questions mark the confusion points, so give those concepts the most careful beats and the best visual in the note. When a deck, code files or other materials arrived beside the transcript, mine them in this same pass under the harvesting rules below.
3. Place the session. Name its phase, the landscape territories it claims, and the cumulative territory covered so far. Placement stays at phase level; state a week number only when the user supplies one in the prompt, because the week calendar shifts between cohorts.
4. Draft against the template, section by section. Extend the session on purpose: add analogies with their breaking points stated, parallel company use cases, and history or trivia where it makes a concept stickier. Around a third of the note should be verified material the session never said, because that margin is what separates a study note from a transcript summary.
5. Verify everything external, live. Web-search every company use case, statistic and historical claim before it enters the note; drop whatever fails verification rather than softening it, and mark genuinely contested claims as contested. Fetch every further-reading link to confirm it is alive; confirm each YouTube video exists and matches the topic, and record its creator and duration. A dead or paywalled link gets dropped, never guessed at.
6. Scrub. Run the llm-tic-scrubber scanner on the Markdown and fix every hit, then run the template's own checks by hand: a dash scan, a banned-word scan, and a scan for topic-label headings that should be action titles.
7. Render. Build every diagram as an image file: matplotlib for charts that carry numbers, hand-authored SVG for structures, strips and maps (mermaid-cli has no browser in this container and fails, so do not reach for it). Reference the same images from the Markdown and from an HTML version styled with assets/note-style.css. Install the renderer if missing (pip install weasyprint --break-system-packages) and render the HTML to PDF. Rasterise two or three pages with pdftoppm and look at them, fixing overflow, orphaned headings and broken images before delivering.
8. Deliver with present_files: the PDF first, then a zip holding note.md with its images folder so the Markdown travels with its visuals.

## Harvesting supplied materials, all of them optional

Sessions sometimes arrive with a deck, notebooks, code files or handouts beside the transcript, and sometimes with the transcript alone. Nothing in this section is ever a reason to wait or to ask for materials; when only a transcript arrives, skip the section entirely.

- Harvest by teaching value, never by availability: an asset enters the note only when it changes what the learner understands, and it lands inside the concept it serves rather than in a gallery at the end, because a note that reads as a deck dump has failed.
- Code appears as captioned code panels: trim each snippet to the lines that carry the teaching point (aim under 20 lines, never a whole file), render it as a styled panel in the house code style (the .code-panel classes in assets/note-style.css, highlighted with pygments, which ships in this container) so it reads like a clean screenshot while staying selectable text, and caption it with one sentence saying what to notice in it.
- Diagrams from a deck are redrawn by default: rebuild the useful ones in the house palette so the note stays one visual family, and extract the original as an image only when it is genuinely visual (a product screenshot, a photo, a rendered chart) and survives extraction cleanly; the pptx and pdf skills carry the extraction routes, and LibreOffice in this container can rasterise slides when needed.
- Tables, worked examples and frameworks lifted from materials land inside the relevant concept with every writing rule applied to their text.
- Neutrality survives harvesting: strip trainer names, dates, cohort numbers and logos from anything taken out of the materials.
- Session materials are ground truth for what was taught, so they need no external verification as teaching artefacts, but any world-fact inside them (a price, a benchmark, a company claim) still passes the live verification step before the note repeats it.

## Design system, established from the programme curriculum PDFs

| Role | Value |
|---|---|
| Headings | Poppins Bold and Poppins Medium, shipped in this container under google-fonts. |
| Body | Liberation Sans. |
| Accent pink | #FF4989 |
| Deep magenta | #C2007A |
| Dark navy | #1A1A2E |
| Body grey | #3F3F58 |
| Muted grey | #8A88A4 |
| Grid lines | #E4E2EE |
| Rose fill | #FFF1F6 |

assets/note-style.css encodes all of this. Do not restyle per note, because the point is that every note across the programme reads as one family and sits beside the curriculum PDFs without a seam.

## Quality bar

- A reader who swaps the topic name should find the note breaks everywhere, because the examples, numbers, visuals and challenge are specific to this session; when any section would survive the swap, rewrite that section.
- The note teaches intuition before vocabulary: the problem arrives first, the formal term second, and every formal term lands in the glossary.
- Instructional design lives in the template order: the takeaways act as the advance organiser, the placement maps anchor new material to what the learner already holds, the four beats pair concrete with abstract, the challenge and the interview questions force retrieval, and beyond-the-session drives elaboration. Trust the order rather than rearranging it.
- Nothing is invented: an unverifiable number, name, price or citation gets dropped, and a constructed teaching pair is labelled a worked example.

## Scope boundaries

Session-debrief owns gap analysis of what was delivered against what was planned. Pre-reads and any pre-session material belong to a separate skill. When the user wants slides rebuilt from a session, that is training-deck-builder territory.
