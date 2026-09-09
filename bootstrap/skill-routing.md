
## Skills: finding and using the right ones

Every task starts with skill selection, and it is a step, never an afterthought.

1. Run `python3 scripts/skills_index.py` and read the list. It prints every installed skill with its source and when to use it, and refreshes `docs/skills-catalog.md`.
2. Choose from the routing table below, then read each chosen SKILL.md in full before producing anything. Take the parts that apply to this task and leave the rest; a skill is a toolbox, never a script to run end to end.
3. State in the chat reply which skills were used and which parts, in one line.
4. When two skills disagree, precedence runs: this repository's CLAUDE.md and docs, then day-pack-builder, then the author's own skills (those whose SOURCE file says author-skill), then Matt Pocock's skills, then Anthropic's document skills, then community skills. This repository's writing rules win over any skill's style.
5. Never install a catalog wholesale. `docs/skills-catalog-community.md` and `docs/skills-catalog-composio.md` are lookup lists for importing one specific skill on request.

| Task | Read these skills |
|---|---|
| Any deck | training-deck-builder for structure and the sketchbook visual system; pptx for the build and the render check; pptx-html2pptx when a slide needs HTML-precise layout; academic-pptx for action titles and one exhibit per slide; powerpoint-keynote-presentation for the Workshop scaffold and the anti-AI-tone pass; concept-packaging when a concept lands flat |
| Demo notebook or any script | day-pack-builder for the notebook shape; tdd and diagnosing-bugs for the data generator and for staging deliberate failures; scaffold-exercises for the progression ladder |
| Exercises, take-homes, build-week briefs | scaffold-exercises; mini-project-designer for build weeks; day-pack-builder for the resistance patterns |
| Study notes and cheat sheets | study-notes-builder; fde-study-notes; fde-cheat-sheets; docx and pdf for the files |
| Curriculum rows and week plans | lesson-strategy first, then lesson-architecture, then curriculum-detailing |
| The spine before approval | grilling, or grill-me when the requester is in the session, to close open branches before asking for approval |
| Reference links | research for primary-source verification; every link dated per the hard rules |
| A decision only a person can make | decision-questionnaire or to-questionnaire |
| Parking work for another session | cohort-handoff or handoff |
| A delivered-session transcript | session-debrief |
| Learner concern or a risky announcement | concern-handling |
| Editing CLAUDE.md or any skill | writing-for-agents and writing-great-skills |
| Before committing any written artifact | llm-tic-scrubber, then `python3 scripts/verify.py` |

One-time: run `/setup-matt-pocock-skills` in a session once, choosing local files as the issue tracker and `docs/` for generated docs, so the engineering skills know where to write.
