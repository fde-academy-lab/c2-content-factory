---
name: mini-project-designer
description: "Design weekly integrated mini-projects for applied technical programs (ML/AI, software engineering, data engineering, cybersecurity bootcamps, similar). Use this skill when the user asks to design a weekly project, create a mini-project, build a learner brief, produce faculty notes or a TA playbook or a rubric, generate project specs for a cohort, design a scenario-based assignment, or create a Week N project for students. Also triggers on requests to critique or refine an existing mini-project design, or to run a cross-LLM verification loop on a draft. Produces four audience-split artifacts using a structured 5-pass workflow with optional cross-model critique. Do NOT use for personal or individual developer projects, commercial product design, or non-educational assignments."
---

# Mini-Project Designer

A reusable skill for producing weekly integrated mini-projects in applied technical programs. The skill enforces a specific methodology: scenario-first design, layered difficulty, mandatory LLM-integrated tasks, audience-split artifacts, and optional cross-LLM critique for robustness.

## When to use this skill

Trigger when the user asks for any of:
- A weekly mini-project, integrated project, or capstone-style assignment for a cohort
- A learner brief, faculty notes, TA playbook, or grading rubric for classroom use
- A scenario-based applied assignment (as opposed to a worksheet or quiz)
- Project design for a technical education program (IIT program, bootcamp, PG diploma, certificate course)
- Critique or refinement of an existing mini-project draft
- Cross-LLM verification of a project brief

## When NOT to use this skill

- Personal project ideas for an individual developer
- Commercial product feature design
- Non-educational assignments (e.g., job application take-homes — different evaluation context)
- Quizzes, MCQ sets, or lecture notes (this skill is for integrated projects only)

## Required inputs

Before starting, confirm the user has provided or can provide:

1. **Week Context Pack** (see TEMPLATES.md § 1). If the user has not supplied one, ask for the minimum viable set: week number, topics covered, prior-week dependencies, cohort size, cohort skill-level distribution, time budget (1-week vs 2-week project), allowed tools, and any dataset constraints.
2. **Execution mode preference** — cold-start (5-pass, ~100 min) or steady-state (single-pass + self-critique, ~45 min). If unspecified, default to cold-start for any of: first project of a cohort, new domain/tool being introduced, capstone or milestone release, previous cohort had >30% Tier C failure. Otherwise default to steady-state.
3. **Cross-LLM verification preference** — single-round (Claude → ChatGPT → Claude) or dual-round (adds Gemini). Recommend dual-round for the same high-stakes conditions above.

Do not generate a project without at least the Week Context Pack. If inputs are incomplete, produce a structured question list and wait.

## Non-negotiables (enforced in every output)

1. **One project per week.** No daily-assignment spam. Two lighter practice exercises + one mini-project is the rhythm.
2. **Scenario first, code second.** Every project opens with a named fictional company, concrete role, specific pain point.
3. **Same scenario, layered depth.** Tier C (Base) / Tier B (Stretch) / Tier A (Advanced) / Bonus. Band assignments set expected depth, never access — no lockouts.
4. **Real, messy public data.** Kaggle / UCI / Hugging Face / scraped open sources. No Iris, Titanic, or `sklearn.make_*` toys.
5. **LLM use is integrated, not policed.** Every project contains a pass/fail sub-task where the student uses an LLM, pastes the prompt and response, critiques weaknesses, and shows a corrected version.
6. **Viva within 48 hours.** Project is designed so a 5-minute oral exam can verify comprehension of a sampled student.
7. **Four separate audience-split artifacts.** Never a combined document. See § Four artifacts below.
8. **Bounded "done."** Every tier has one concrete paragraph describing what a complete submission looks like.
9. **Reward thinking, not metrics.** Rubric allocates meaningful points to reflection and explanation, not just model accuracy.
10. **Rubric sums to exactly 100.** Enforce this mechanically.
11. **Tier C completable in ≤4 hours by a weak student. Tier A not completable in <2 hours by a strong student.** Calibrate via dry run.
12. **Portfolio-grade output.** Every project produces a GitHub repo plus a one-page executive memo (framed as interview case study).

## The four artifacts

Every mini-project produces exactly these four files. Never one combined document.

| File | Audience | Must contain |
|------|----------|--------------|
| `learner_brief.md` | Students | Business scenario, dataset, task ladder (C/B/A/Bonus), bounded done per tier, LLM-integrated task, integrity guardrails, reflection questions, rubric summary |
| `faculty_notes.md` | Lead trainer / guest faculty | Expected approach, solution shape, 3 common errors, 5 discussion prompts, 5 viva questions (easy → hard) |
| `ta_playbook.md` | Teaching assistants | Floor-walking checklist, 5 known confusion points with unstick strategies (not solutions), triage rules, 3 Socratic questions |
| `rubric.md` | Grading ops | 100-point breakdown, example submissions for full / partial / zero credit, LLM-task pass/fail gate separate from scored rows |

Plus one optional fifth: `announcement.md` for the weekly LMS broadcast.

## Workflow — cold-start mode (5-pass)

Use when the domain, cohort, or project format is new. ~100 min. Run all passes in the same chat window.

1. **Priming** — paste PROMPTS.md §2.1 along with the Week Context Pack. Sets non-negotiables.
2. **Pass 1 — Three candidates.** Get three distinct project concepts with scenarios, datasets, and fit rationale. Pick one.
3. **Pass 2 — Architecture.** Produce problem statement, learner outcomes, stage breakdown, depth ladder, rubric skeleton.
4. **Pass 3 — Dataset audit.** Verify the dataset is real, messy enough, not already solved, and scenario is authentic.
5. **Pass 4 — Four artifacts.** Generate learner_brief, faculty_notes, ta_playbook, rubric as separate labeled blocks.
6. **Pass 5 — Self-critique + rewrite.** Attack the draft against seven failure modes; rewrite the weakest artifact end-to-end.

Exact prompts in PROMPTS.md §2.

## Workflow — steady-state mode

Use when a library of 2–3 past projects exists. ~45 min.

1. Priming + all required context in one block.
2. Produce all 4 artifacts in one pass.
3. Run self-critique pass.

## Cross-LLM robustness loop (optional but recommended)

Every LLM has blind spots. Claude's self-critique cannot catch Claude's house-style failure modes. Running output past a different model surfaces what was invisible.

### Single-round (recommended standard, +25 min)

1. Claude produces v1 via cold-start or steady-state workflow.
2. **Open a fresh ChatGPT chat.** Paste PROMPTS.md §3.1 with the Week Context Pack and all 4 artifacts.
3. ChatGPT returns a structured critique (showstoppers, risks, calibration checks, blind spots, verdict).
4. **Return to Claude's original chat.** Paste PROMPTS.md §3.2 with ChatGPT's critique.
5. Claude produces v2 + changelog.

### Dual-round (recommended high-stakes, +45 min)

Continue from single-round:

6. **Open a fresh Gemini chat.** Paste PROMPTS.md §3.3 with Week Context Pack, v2 artifacts, and ChatGPT's critique.
7. Gemini returns a second critique focused on technical accuracy and what the first reviewer missed.
8. **Return to Claude.** Paste PROMPTS.md §3.4 with Gemini's critique.
9. Claude produces v3 + final changelog.

### Hard rules for cross-LLM loop

- Critic LLM diagnoses, never rewrites. Rewriting injects critic's style biases and defeats the purpose.
- Run each critique in a fresh chat. Never in the author's chat — context contamination defeats independent review.
- If any verdict is "rebuild," restart from Pass 2. Refinement cannot save a fundamentally wrong premise.
- Human review (trainer + TA cold read) still happens after the cross-LLM loop. LLM critique pre-filters, humans verify.

## Difficulty model — same bar, different plates

| Tier | Expected depth | Assigned to |
|------|----------------|-------------|
| Tier C (Base) | Baseline model + one metric + one business observation | Bottom ~30% by rolling performance |
| Tier B (Stretch) | C + tuning + compare two approaches + error analysis | Middle ~40% |
| Tier A (Advanced) | B + production angle (deployment, explainability, failure modes) + improvement | Top ~30% |
| Bonus | Open-ended, creative or research-style extension | Anyone who finished their expected tier |

Rubric allocates points by tier (C=40, B=30, A=20, Bonus=10). A Tier A student submitting only Tier C work scores like Tier C.

## Adaptive spot-checks (use when uncertainty is high)

Three ad-hoc checks available any time (full prompts in PROMPTS.md §4):

- **Ambiguity sweep:** ask a second LLM to read the learner brief "as a weak student" and list every ambiguous sentence.
- **Dataset re-verification:** ask a different LLM than the one that proposed the dataset to verify the link, size, and claimed properties.
- **Effort calibration:** ask a third LLM to estimate Tier C and Tier A effort independently and compare to targets.

## Quality gate — before releasing

Run CHECKLIST.md before publishing to LMS. Every item must pass. If not peer-reviewed by release minus 1 day noon, the project does not ship — repeat last week's structure instead.

## Output format rules

- Always produce the four artifacts as separate code-fenced markdown blocks with clear file markers: `=== learner_brief.md ===` etc.
- No em-dashes anywhere in output.
- Tight, direct language. No fluff. No "In conclusion" or "Accordingly."
- Use tables for structured data.
- Code blocks for commands, paths, data schemas.
- Inline no citations of sources (this is not research output).

## Supporting files

| File | Purpose |
|------|---------|
| `PROMPTS.md` | Every copy-paste prompt used in the workflow, organized by stage |
| `TEMPLATES.md` | Blank templates for Week Context Pack and the 4 artifacts |
| `CHECKLIST.md` | Quality gate + cross-LLM verification checklist |

Load these files when needed. Do not paraphrase their contents into the SKILL.md — they are the canonical sources.

## Anti-patterns to reject

If the user or earlier context pushes toward any of these, do not comply:

- One combined document instead of four split artifacts
- Strict tier gating (locking students out of higher tiers)
- Toy datasets like Iris/Titanic
- Rubric that sums to 97 or 103 — must be exactly 100
- Creativity required in Tier C (ambiguity paralyzes weak students)
- Leaderboard-centric framing by default (competition platforms are optional wrappers only)
- Using the same LLM for author + critic + second critic
- Skipping human review because "the AI loop already caught everything"

## Escalation: when to tell the user to stop

If the user requests something that would corrupt the methodology (e.g., "skip the LLM-integrated task because we don't want students using AI"), push back once with the rationale. If they insist, produce what they asked for but flag at the end what was compromised and why it matters.
