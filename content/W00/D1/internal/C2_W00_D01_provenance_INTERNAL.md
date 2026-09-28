# Provenance: Week 0, Monday

INTERNAL.

## What the pack was built from

The Monday row of `docs/curriculum/W0_Baseline_week.md` (tracker v7, 21 September 2026) for the
content, and the student Week 0 sheet, `docs/journey/Week_0.md` (version 2, 27 September 2026), for
the running order, following the working rule in `data/programme/facts.yaml` for the conflict
between the two. The spine was approved in session on 27 September 2026, with one decision from the
Programme Head: the codespace today is GitHub's `codespaces-jupyter` template, and the course's own
repository follows before teaching needs it.

On 28 September 2026 the requester replaced two parts of the pack with their own material: the
Programme Head's academic orientation deck replaced the pack's welcome deck, and the requester's
diagnostic, whose first page carries the self-rating, replaced the paper self-rating form.

## The orientation deck

`slides/C2_W00_D01_orientation_STUDENT.pptx` is the requester's third version, received on
28 September 2026: 34 slides with speaker notes, committed with one change. Slides 29 to 31 and
their notes named the institute's Director, three committee members, the CDF contact and five
members of the programme team, and the repository copy replaces each name with its role, because the
repository is public; on slide 30 each team card keeps its role label and drops the name line. No
other slide names a person. Measured with `scripts/deck_check.py`, every text box fits.

The deck states the 1,000-mark evaluation scheme, which the requester confirmed as locked on
28 September 2026, and the 90 percent attendance rule; `data/programme/facts.yaml` records both.

## Sources, each checked on 27 September 2026

| Source | What it settled |
|---|---|
| GitHub Docs, creating an account on GitHub | The sign-up page, the verified email, and the Google or Apple sign-up option |
| GitHub Docs, getting started with GitHub Codespaces for machine learning (the row's own resource) | Opening a codespace from the `codespaces-jupyter` template |
| The `github/codespaces-jupyter` template at commit `d841da0` (11 August 2026) | A four-core machine, packages installed from `requirements.txt` after the editor opens (pandas 2.2.2, matplotlib 3.8.4), and `notebooks/population.ipynb`, whose first cell reads `data/atlantis.csv` and draws "Population of Atlantis" |
| GitHub Docs, apply to GitHub Education as a student (the row's own resource) | Who qualifies, the four kinds of enrolment proof, and the academic email rule |
| GitHub Docs, stopping and starting a codespace; setting the idle timeout; deleting a codespace | Closing the tab does not stop a codespace, the default idle timeout is 30 minutes, the stop steps, and the default retention of 30 days |
| GitHub Docs, billing for GitHub Codespaces | 120 core hours a month on the free plan, and a four-core machine using four core hours an hour, which gives the 30 hours the pack states as arithmetic |
| A bare virtual environment, run in session | The exact failure text, `ModuleNotFoundError: No module named 'pandas'` |

## Conflicts, and what the pack did

- **The Monday running order.** The tracker's row runs the welcome, setup and the self-rating. The
  self-rating now sits on the first page of Tuesday's diagnostic, so Monday runs the orientation and
  setup, and the rate-yourself moment from the row closes the orientation as its deliberate failure.
- **The roles map.** The cheat sheet's second panel follows the orientation deck: two primary roles,
  two supported roles, and forward deployed engineering as the way of working.
- **The client.** The deck names Kalpa Group and its first question and goes no further, which keeps
  every Kalpa item for Week 1 Monday.
- **The IITGN faculty sessions.** Left out of the orientation's answers, because every session is
  tentative until IIT Gandhinagar confirms it.

## Not verified, and left for the ground team

- The LMS's name, address and logins, which no source carries; the walkthrough keeps a "to be found"
  slot.
- The exact wording of VS Code's kernel and environment picker in this template, so the walkthrough
  describes what the picker asks for rather than naming a label.
- Whether the institute's student ID or an academic email will exist in time for the GitHub
  Education application; the help desk records learners as pending until it does.

## Own constructions, labelled in the artifacts

The three seats (the row's own statement that they are the course's construction), the rate-yourself
moment staged after the orientation, and each seat's first question.
