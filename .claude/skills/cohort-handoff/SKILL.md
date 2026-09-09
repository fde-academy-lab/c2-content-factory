---
name: cohort-handoff
description: Compact the current chat into a handoff note so a fresh chat in this project, or the ChatGPT or Gemini copy of it, continues the work without re-reading the thread. Use when a chat passes about ten exchanges, when the work moves to another platform, model or owner, when a long build is parked mid-way, or when the user says handoff, hand over, park this, or continue in a new chat. Also use in reverse: when a chat opens with a handoff note, follow the receiving steps at the end.
---

# Cohort handoff

A chat stops being useful after about ten exchanges because the middle of the thread fades. The handoff note is the one-screen document the next chat reads instead of the thread. Write it as a markdown file named `HANDOFF_<cohort>_<topic>_<YYYY-MM-DD>.md`, put it in the outputs folder and present it, so the person can drop it into the next chat on any platform.

## What the note contains, in this order

| Section | What goes in it |
|---|---|
| Header | Cohort, track and level, week or module, who consumes the output, the date, and one line naming what the next chat is for. If the user passed a focus for the next chat, the whole note is tailored to that focus. |
| Goal | The one decision or artefact the work is driving towards, in one sentence. |
| State | What is finished, named by file (the exact file name in outputs or in project knowledge), and what is half done, with the last good stopping point. |
| Decisions and why | Every choice made in the thread, dated, with the reason in one line each, so the next chat does not reopen them. |
| Facts | Two lists: confirmed (with the source file or the person who confirmed) and assumed (still to confirm). An assumed fact never migrates to confirmed inside a handoff. |
| Rejected | Anything the user turned down, with the reason, so it is not proposed again. |
| Read first | The project knowledge files and earlier outputs the next chat should open before doing anything, by name only. |
| Suggested skills | The skills the next chat should invoke, one line each on why. |
| Next steps | The first three actions for the next chat, concrete enough to start without a question. |

## Rules while writing it

- Reference every artefact by file name or link; never paste its content back in. The note is a map of the work, and the map stays under one screen wherever possible.
- Learners appear by roster ID only. Grades, grievances and admissions verdicts stay inside the project and out of the note unless the next chat is the grading chat, in which case the note names the file that holds them.
- Redact credentials, phone numbers, email addresses and anything else that should not sit in a file left open on a screen.
- Full connected sentences, tables where they help, no em-dashes, and the banned-word list from the project instructions applies.
- Mark confidence where the next chat needs it: settled, proposed or unconfirmed, and this programme's own construction where a device is ours.
- Write the note in the platform-neutral form; nothing in it may depend on a tool only one platform has.

## Receiving a handoff

When a chat opens with a handoff note, open the files named under Read first, restate the goal in one line back to the user, confirm the four fixes (cohort, track and level, week, consumer) from the header, and start on step one of Next steps. Reopen a decision only if a Facts line it rested on has since changed.
