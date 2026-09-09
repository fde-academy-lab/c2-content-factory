---
name: decision-questionnaire
description: Turn a fact or decision the assistant cannot settle alone into a short markdown questionnaire for the one person who can answer it, to be filled in async or in a meeting. Use it whenever an artefact is blocked on an item in the project's unsettled list (an institute partner, a certificate name, a consulting weekday, a clock time, a cut-off, a rubric weight, a brochure commitment, a week map), whenever a rule forbids answering from memory, whenever more than two clarifying questions would otherwise be asked in chat, or when the user says ask Akash, ask RG, ask Sumit, confirm with, get sign-off, needs a decision, or send a questionnaire.
---

# Decision questionnaire

The project forbids filling a gap with a plausible value, and it lists facts that must be confirmed before use. Each of those is a decision that belongs to one person. This skill turns the blocker into a form that person can answer in two minutes, instead of a chat that stalls or a value invented in silence.

The pattern follows the mattpocock/skills to-questionnaire: interview about the send (who answers, what is needed back, by when), never about the subject, then produce the form.

## Before writing, settle the send

Answer these from the conversation and the project files; ask only what cannot be inferred, as choices.

| Question | Where the answer usually is |
|---|---|
| Who answers | The role split in the project instructions (roadmap and expectations to Akash, academic and session matters to Sumit, trainers to Ayush, delivery logistics to the programme manager, admissions and quality to RG). |
| What it blocks | The artefact, session or answer that cannot proceed, named. |
| Needed by | The content lock (forty-eight hours before the session), the trainer lead time (one week), or the learner-facing date. |
| The default if unanswered | What the assistant will assume, marked proposed, so work continues at the owner's risk rather than stopping. |

## Produce one file

Name it `questionnaire_<topic>_<YYYY-MM-DD>.md`, save it to the outputs folder and present it. Fill `references/questionnaire_template.md`.

| Part | What goes in it |
|---|---|
| Header | For whom, from whom, needed by, what it unblocks, in four lines. |
| Questions | At most seven. Each is one line, answerable by ticking an option or writing one line. Each carries the options with what each implies, the current record (file, section and date), the default if unanswered, and a blank answer cell. |
| Where the answer lands | The numbered file and section that will be updated, and the line in the unsettled list that will be removed. |

## Rules

- Never pre-answer from memory. The current record cell quotes only what a dated file says, with the file name.
- Options carry consequences: "Thursday (the calendar workbook then needs the Wednesday column cleared)". A question without consequences gets guessed.
- Order questions by what they unblock soonest.
- One questionnaire per owner. Two owners means two files.
- If the user asks to send it, create a draft in the connected email tool addressed to the owner with the file attached; never send.
- When the answer comes back, update the named file, bump its version line, remove the item from the unsettled list, and say so in one line.

## When not to use it

A question the project files already answer is looked up, never sent. A preference question with no fact at stake ("which of these two titles") is asked in chat as two choices.
