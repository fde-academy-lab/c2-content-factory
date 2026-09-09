# Retrospective and method · building one training day, 4 to 10 September 2026

This is the honest record of how the PPL Session 2 kit got built, what went wrong at each turn, and the method that survived the corrections. The two prompts beside this file encode that method. Read this once; use the prompts every day.

---

## Part 1 · The arc, turn by turn

| # | What you asked | What I produced | What was wrong, in your words or in mine |
|---|---|---|---|
| 1 | Add two topics to the TOC without adding hours; build a pre-assessment for a mixed QA and DevOps room; flag gaps | Pre-assessment, TOC update, gap list | Adequate. Nothing rejected. |
| 2 | Redistribute the schedule to 3 to 3.5 hours a day; read the Day 1 transcript for what landed; keep hard commitments; a day-by-day playbook | Revised curriculum, playbook | Adequate. You asked me to learn from the transcript: first and last segments held attention, the middle sagged. |
| 3 | Study notes for Day 1 | Notes via the study-notes skill | Fine. |
| 4 | Company context and your own pre-training research; "teaching is an art" | Curriculum refinement | Fine. The research you supplied was the reason the refinement was specific. |
| 5 | Hands-on strategy "like IBS but better": AWS demos, notebooks, HTML artefacts | A strategy with `.py` files | **Wrong file type.** You wanted runnable `.ipynb` with diagrams, summaries and flowcharts, and you told me learners have AWS accounts. I had not asked about the delivery surface. |
| 6 | Two PPT decks, zero to hero, diagrams throughout, do not over- or under-engineer | Two decks on an SVG-rasterising pipeline | **Rejected with a written critique and a redesign brief** you authored: flow not relatable, questions without diagrams, no visual storytelling, not incremental. |
| 7 | Rebuild to the brief | Incident-first rebuild, native shapes | **"Noooo."** Not topic-by-topic. You wanted more slides, each segment as its own progression: why this topic, what it is through an incremental example, the definition and formula, application areas, a worked example step by step, first principles. Copy the Day 1 deck's design exactly. |
| 8 | Half 1 first, copy the design | 45-slide half, on a renderer measured from the Day 1 deck | Accepted for design. Then you re-scoped the whole session. |
| 9 | Re-scope: one agentic loop, built by hand on the Converse API, code beside exploded diagrams; a paper exercise, a fill-the-snippets lab, tools added one at a time, testing and guardrails, a managed agent with its raw trace; check curriculum commitments | Three decks (Loop, By Hand, Making It Hold), a curriculum re-sequencing | Accepted. This is the session that shipped. |
| 10 | Notebooks: one concept per file, progressive, runnable with and without AWS, a mental map before each cell, summary cells, tests, a markdown walkthrough for the console | Seven notebooks, a support module, a walkthrough | Accepted, with one process error: I presented only four of seven files and you read it as a gap. |
| 11 | Guided and unguided exercises | Eight files with trainer framing | **Rejected.** Too many, too verbose in framing, too thin in substance, no critical thinking, and trainer content in files you paste straight into GitHub Discussions. You had already told me the device set weeks earlier and I had it in memory. |
| 12 | Rebuild the exercises | Three exercises of 30 items, a take-home, a separate key | Accepted. A mechanical audit found 26 items where the key was the longest option. |
| 13 | Add hands-on parts; a cheap model with a cost meter; richer notebooks | Nova Lite verified and adopted, notebooks v2 with a cost meter and code-cell diagrams, exercise notebooks with pick-from-options TODOs | Accepted. |
| 14 | Use two references you supplied for AgentCore; update deck, notebooks, exercises; three zips | Done | Accepted. The references made the console segment accurate; before them I had only CLI facts. |
| 15 | The managed demo must be browser-based, framed as the QA sandbox: probe before the build exists | Walkthrough, exercise and deck segment rewritten | Accepted. I had built the CLI path because that is what I had verified, not what you would show. |
| 16 | Excel playbooks and an Apple-styled HTML simulator | Two workbooks, a three-part simulator | Accepted, then extended. |
| 17 | Extend the simulator: pages, animation, simpler Part 1, more models, bold acronym frameworks with applications, mistakes, recipes, tools | Eight pages | Partly accepted. |
| 18 | Trace reader, QA and DevOps playbooks, a build simulator with console steps, popups | Twelve pages | **"Surface level."** The session strip was useless, the meter was unreadable, experiments were vague with important text in grey, R·E·C was loose, "your click" did nothing, nav cluttered, samples looked dead. |
| 19 | Fix all of it, add glossary, cheat sheets, footer, contact, merge mistakes with practices, deepen DevOps | Sixteen pages | **Still broken in places.** Go-to-page did nothing, dropdowns did not appear, stairs did not map to pages, R·E·C had no lineage, the tool designer was a gimmick, no quantitative methods, no contact popup. |
| 20 | Rebuild: unifying model, decision visuals, formulas, sourced frameworks, grouped nav, sidebar, contact modal | Seventeen pages, rebuilt from scratch | Shipped. Every reported bug reproduced in a headless browser before it was fixed. |

## Part 2 · The mistakes, grouped by cause

**I built before I had the envelope.** Turns 5, 11 and 15 all failed for one reason: I did not know, or did not ask, the surface the artifact would land on. Notebooks not scripts because learners run them. No trainer text in exercises because they go into GitHub Discussions verbatim. Browser steps not CLI because that is what a room watches. The fix is a question asked before any build: who consumes this, on what screen, with what in front of them.

**I built before I had the sources.** The deck's managed-agent segment was thin until you supplied two links. The model ladder was two entries until I verified twelve. The R·E·C framework was a label until I found the API design, the OpenTelemetry span kinds and τ-bench underneath it. Research is the first move, not a repair.

**I shipped breadth where you wanted depth.** Eight exercises instead of three. Twelve thin pages instead of six deep ones. "One change each" as a heading instead of a situation, a hypothesis and a rule per card. Your test is always the same: what happens when a learner uses it. A thinner artifact that makes them think beats a wider one that reads well.

**I trusted the wrong evidence about my own output.** Playwright said the dropdown was "visible" while CSS overflow clipped it. I presented four files and let the listing imply seven did not exist. A sample preloaded in a textarea made the button look dead. The rule that came out of it: verify what the user will see, not what the DOM reports, and never let a presentation imply an absence.

**I applied rules after the rejection instead of before the build.** The selection-only device set, the vary-the-shape rule and the distractor discipline were all in memory before turn 11. Memory is a set of constraints to trade off before the first line is written, not a checklist to reconcile afterwards.

**Styling was never the problem.** No rejection in twenty turns was about colour or type. Every one was about structure, flow, depth or fit. When you did mention fonts and glass, it was after the substance was right.

## Part 3 · What you look for, as I now understand it

1. **Research first, then convert.** Find the one written and one video source, the product docs, the prices, the model ids. Verify each. Then turn what exists into something a learner can do, which is the half of the job a librarian does not do.
2. **One world, carried through everything.** A fictional but realistic scenario with a proper name, a business line, entities, a relationship picture, and features planted so that each teaching point has one thing in the data only that point explains. Northlight for PPL; client zero for the Academy; the bank records spiral for Gandhinagar.
3. **Segments as questions, each a full concept unit.** Pain in money or minutes, ground it, first-principles strip, clearest example, derived framework, steps, worked example, the central case, the gotcha, the crux plus a transfer question. Multiple slides per segment. More slides carrying one idea each.
4. **The day is a loop across surfaces.** Deck to establish a concept. Companion HTML to make it move on the projector. Back to the deck for the deep dive. Notebook to make them do it. Exercise to make them think. Excel to hand them a tool they keep. Cheat sheet to make it stick. Transcript into study notes so a learner a month later can recover it.
5. **Every artifact is handed over as it is.** No trainer voice in learner files, no design rationale in any file, no meta-content on a slide. Rationale, arithmetic and assumptions go in the chat reply.
6. **Substance is measured mechanically.** Notebooks execute with every check passing. Excel recalculates in LibreOffice with verdicts asserted and design decisions flipped. HTML is swept in a headless browser with element-at-point checks. Exercises pass a distractor audit. Decks pass the validator, the meta scan, the tic scan and the em-dash scan. A pixel-level look happens whenever the tool allows.
7. **Frameworks are welcome when they are load-bearing.** Named, every letter defined, situations listed, steps numbered, lineage cited, shown without and with, and honest about where they stop. Marked as constructions when they are.
8. **Numbers wherever a decision hides.** Cost of a run, a lap budget, when escalation pays, the failure rate a person is cheaper than, what an evaluation can resolve. A rule that cannot be computed is an opinion.
9. **Simplicity is a structure.** Not fewer words or fewer diagrams. One idea per slide, one concept per notebook, one change per experiment, one job per tool.

## Part 4 · The method that survived · the eight moves of a day build

Named so a team can say them. Each move produces a named artifact. No move starts until the one before it has its artifact.

| Move | Question it answers | Artifact it produces |
|---|---|---|
| **1 LOCK** | What already exists that is good, and what is true today? | A source lock: one written reference, one video, the product docs, verified prices and ids, each with the date checked |
| **2 FRAME** | Who consumes this, on what surface, in how many minutes, knowing what? | The delivery envelope: audience objects they already know, room and remote mix, surfaces (projector, VS Code, Colab, console, GitHub Discussions), minutes per block, hard commitments from the TOC, what the room does not know |
| **3 GROUND** | What is the one world every example lives in? | The world artifact: name, business line, entities, relationship picture, the incident, the fixtures, the witness matrix (teaching point × data feature) |
| **4 SPINE** | What are the segments, in what order, and which artifact carries each? | The spine: segments as questions, a concept unit per major topic, the deck split by block, the artifact map, the minute arithmetic, the cut list |
| **5 BUILD** | Build each artifact to its spec | Decks, companion HTML, notebooks, exercises, Excel tools, cheat sheets, walkthroughs, trainer playbook |
| **6 PROVE** | Does it run, does it compute, does it render, is it fair? | The verification report: executions, recalcs, browser sweeps, audits, plus the fit review (what happens when it is used) |
| **7 RUN** | In what order, with what live path? | The run sheet: the loop across surfaces with minutes, the live path through the deck, the demo script, the probe list |
| **8 SETTLE** | What did the room do with it, and what carries to tomorrow? | Study notes from the transcript, the debrief with delivery-reality numbers, the continuity block for the next day, the memory update |

The prompts that follow apply these eight moves to Gandhinagar Cohort 2, and install them as skills in the Claude Code project.
