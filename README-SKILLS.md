# Skills enrichment pack

Drag the contents of this folder onto the repository root in GitHub's web uploader (setup.sh replaces the old one; scripts, prompts and bootstrap merge into the existing folders). Commit to main. Then:

1. Paste the new setup.sh into the cloud environment's setup script field, replacing the old one.
2. Run prompts/skills_prompts.md Prompt E once. Merge its pull request.
3. Run Prompt F once. Merge.
4. Run Prompt G to confirm routing.

Why the last setup script failed: a variable was set inside a subshell and read outside it under strict mode, which strict mode treats as an error. The new script avoids strict mode, sets the variable plainly, and always exits zero after reporting what it could and could not install. The pip root warning is harmless and is now silenced.

What Prompt E installs, in tiers that match the precedence rule in CLAUDE.md:

| Tier | Skills | Source |
|---|---|---|
| Author's own | training-deck-builder, lesson-strategy, lesson-architecture, curriculum-detailing, concept-packaging, mini-project-designer, study-notes-builder, fde-study-notes, fde-cheat-sheets, session-debrief, concern-handling, cohort-handoff, decision-questionnaire, llm-tic-scrubber | bootstrap/my-skills, exported from the author's Claude environment |
| Matt Pocock | grill-me, grilling, grill-with-docs, research, tdd, diagnosing-bugs, code-review, handoff, teach, to-questionnaire, writing-for-agents, writing-great-skills, scaffold-exercises, setup-matt-pocock-skills and the rest of engineering, productivity and misc | github.com/mattpocock/skills, MIT |
| Anthropic document skills | pptx, docx, xlsx, pdf, frontend-design | github.com/anthropics/skills; the four document skills are source-available for demonstration |
| Presentation specialists | pptx-html2pptx (the HTML-to-slides route), academic-pptx (action titles, exhibit discipline), powerpoint-keynote-presentation (narrative scaffolds incl. Workshop, anti-AI tone) | tfriedel, Gabberflast, marcusnelson |
| Community | content-research-writer, plus two catalogs saved to docs/ for on-demand imports | ComposioHQ, abubakarsiddik31 |

Two of the six repositories you named are catalogs rather than skills: abubakarsiddik31/claude-skills-collection is a README of links, and ComposioHQ/awesome-claude-skills hosts a handful of small skills (invoice organiser, raffle picker, file organiser) that do not apply here. Both are saved as lookup lists, and any entry can be imported later by name.

Context cost: Claude Code loads each skill's description at session start. Roughly forty skills is fine; the catalogs stay as documents rather than installed skills precisely so the list does not balloon.
