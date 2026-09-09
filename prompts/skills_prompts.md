# Skills prompts for Claude Code on the web

Run in this order. Each is one task on `c2-content-factory`.

## Prompt E. Import every skill source (run once)

```
Import the skill sources below into .claude/skills/. For every skill folder you create, add a one-line file named SOURCE containing the repository URL and the path it came from, and keep each skill's license file where one exists. Clone with --depth 1 into /tmp.

1. Author's own skills: move every folder under bootstrap/my-skills/ into .claude/skills/ (fourteen folders; their SOURCE files already say author-skill). Remove bootstrap/my-skills afterwards.

2. https://github.com/anthropics/skills : copy skills/pptx, skills/docx, skills/xlsx, skills/pdf and skills/frontend-design, each as its own folder under .claude/skills/. Skip any that already exist.

3. https://github.com/tfriedel/claude-office-skills : copy public/pptx to .claude/skills/pptx-html2pptx and change the name field in its SKILL.md frontmatter to pptx-html2pptx so it does not collide with Anthropic's pptx. Also copy html2pptx-local.cjs, package.json and requirements.txt from that repository's root into .claude/skills/pptx-html2pptx/. Do not import its docx, xlsx or pdf folders; Anthropic's versions supersede them.

4. https://github.com/marcusnelson/presentation-writing-claude-skill : the file powerpoint-keynote-presentation.skill is a zip. Unzip it into .claude/skills/powerpoint-keynote-presentation/ so that SKILL.md sits directly inside that folder.

5. https://github.com/Gabberflast/academic-pptx-skill : the skill lives at the repository root. Copy SKILL.md, content_guidelines.md, slide_patterns.md and LICENSE into .claude/skills/academic-pptx/. Do not copy the PDF.

6. https://github.com/mattpocock/skills : copy every folder that contains a SKILL.md under skills/engineering, skills/productivity and skills/misc into .claude/skills/, one folder per skill, keeping the skill's own folder name. Skip skills/in-progress and skills/personal. If any name collides with a folder already present, keep the existing folder and report the collision.

7. https://github.com/ComposioHQ/awesome-claude-skills : copy only content-research-writer into .claude/skills/. Save the repository README as docs/skills-catalog-composio.md for lookups.

8. https://github.com/abubakarsiddik31/claude-skills-collection : this repository is a catalog with no skill folders. Save its README as docs/skills-catalog-community.md.

9. Append the contents of bootstrap/skill-routing.md to the end of CLAUDE.md, then delete bootstrap/skill-routing.md.

10. Run python3 scripts/skills_index.py and include its full output in your reply. Then report: the number of skills installed, any name collisions, and any source that could not be cloned.

11. Commit on branch import-skills and stop. Do not build any content.
```

After it finishes: open the diff, create the pull request, merge.

## Prompt F. One-time configuration of the engineering skills

```
Run /setup-matt-pocock-skills. When it asks for the issue tracker, choose local files. When it asks for triage labels, accept the defaults. When it asks where to save generated docs, answer docs/. Commit any files it creates on branch setup-skills and stop.
```

## Prompt G. Prove the routing works (read-only)

```
Read CLAUDE.md, then run python3 scripts/skills_index.py. Without building anything, answer: for the task "build the Week 1 Day 2 trainer deck from its deck spine", list the skills you would read, in order, and for each one the specific sections you would take from it and the sections you would ignore. Keep it under 250 words.
```

If the answer names training-deck-builder, pptx, academic-pptx and powerpoint-keynote-presentation with reasons, routing works. If it names only pptx, the routing section did not land and CLAUDE.md needs checking.
