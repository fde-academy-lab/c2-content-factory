# Provenance: Week 0, Monday

INTERNAL.

## What the pack was built from

The Monday row of `docs/curriculum/W0_Baseline_week.md` (tracker v7, 21 September 2026) for the
content, and the student Week 0 sheet, `docs/journey/Week_0.md` (version 2, 27 September 2026), for
the running order and for anything learners have already been told, following the working rule in
`data/programme/facts.yaml` for the conflict between the two. The spine was approved in session on
27 September 2026, with one decision from the Programme Head: the codespace today is GitHub's
`codespaces-jupyter` template, and the course's own repository follows before teaching needs it.

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

- **The Monday running order.** The tracker's row and the student sheet agree on the blocks (the
  welcome, setup, the self-rating) and the pack follows both. The week's other days follow the
  student sheet: Tuesday's paper as about two hours, the introductions on Wednesday, and Saturday's
  session with a working forward deployed engineer.
- **The client.** The student sheet promises "your client" in Monday's orientation, while the
  tracker keeps every Kalpa item for Week 1 Monday. The deck names the client in one line and says
  nothing more, as agreed in session.
- **Placement.** The deck uses the student sheet's own wording and states no numbers.
- **The IITGN faculty sessions.** Left out of the welcome, as agreed in session, because every
  session is tentative until IIT Gandhinagar confirms it.
- **Holidays.** The deck lists the six gazetted holidays from the locked calendar, including
  Christmas Day and Republic Day, which the student sheet does not list yet; the restricted holidays,
  which are still open, are not mentioned.

## Not verified, and left for the ground team

- The LMS's name, address and logins, which no source carries; the walkthrough keeps a "to be found"
  slot.
- The exact wording of VS Code's kernel and environment picker in this template, so the walkthrough
  describes what the picker asks for rather than naming a label.
- Whether the institute's student ID or an academic email will exist in time for the GitHub
  Education application; the help desk records learners as pending until it does.

## Own constructions, labelled in the artifacts

The three seats (the row's own statement that they are the course's construction), the A to D
self-rating scale and its topic descriptors, and each seat's first question.

## Open for the next packs

The template has no Postgres, and Thursday's SQL brush-up runs queries from VS Code against Postgres,
so the course's own repository, or another workspace with a database, has to exist before Thursday
1 October. Tuesday's pack also has to reconcile the student sheet's paper of about two hours with the
tracker's four papers of 60, 45, 30 and 30 minutes plus a 40-minute one-pager.
