# The claude.ai Project pack

Three things keep the IITGN Cohort 2 Project on claude.ai in step with this repository.

| File | Where it goes | When to redo it |
|---|---|---|
| `PROJECT_INSTRUCTIONS.md` | Everything below its line, pasted into the Project's instructions | When the ground-truth order or the house rules change |
| `knowledge/*.md` | Uploaded into the Project's knowledge, replacing the previous copies | Whenever `python3 scripts/sync_programme.py` reports that a file under `docs/claude-project/knowledge/` changed |
| `MEMORY_UPDATE.md` | Everything below its line, pasted into a new chat inside the Project | After a change large enough that the Project's memory would give an old answer |

The knowledge files are generated: `01_programme_facts.md` is compiled from
`data/programme/facts.yaml` and the workbooks, and the rest are copies of the calendar, the tracker's
exports and the locked docs. Never edit them here; edit the source and sync.

The account's skills sit apart from the Project. Each upload is a ZIP whose single top-level folder
carries the skill's name and holds its `SKILL.md`. It is added under Customize, then Skills, then the
plus button, then "Create skill", then "Upload a skill", with code execution on (checked 27 September
2026). `python3 scripts/package_skills.py` builds those ZIPs from `.claude/skills/`.
