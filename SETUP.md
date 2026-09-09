# Browser-only setup and Week 1 build

Everything here runs in a browser. No terminal, no local install.

## Part A. Create the repository (GitHub web, about 10 minutes)

1. Sign in to GitHub and open https://github.com/new. Name it `c2-content-factory`, set it Private, tick "Add a README file" so the repository is not empty, then Create repository.
2. On the repository page, open "Add file", then "Upload files".
3. Unzip the pack on your computer, open the unzipped folder, select everything inside it (CLAUDE.md, README.md, SETUP.md, docs, prompts, scripts, bootstrap), and drag the selection onto the upload area. Drag the contents rather than the outer folder, so the files land at the repository root.
4. Wait for every file to finish uploading. Commit message: `factory v1`. Commit directly to main.
5. Confirm the repository root shows `CLAUDE.md`, `docs/`, `prompts/`, `scripts/` and `bootstrap/`, and that `docs/curriculum/` holds eleven markdown files plus `source.xlsx`.

## Part B. Connect Claude Code on the web (about 5 minutes)

6. Open https://claude.ai/code and sign in with the account the team will share.
7. When prompted, connect GitHub and install the Claude GitHub App, granting it access to `c2-content-factory`.
8. When prompted to create a cloud environment, name it `content-factory` and choose the trusted network access level so sessions can fetch the reference links that the verification step checks. Save it.
9. Back on claude.ai/code, pick `c2-content-factory` as the repository for your first task.

Claude Code on the web is a research preview available on Pro, Max and Team plans, and on Enterprise premium or Chat plus Code seats. Cloud sessions share your account's rate limits, so parallel sessions consume them proportionately.

## Part C. Install the skill into the repository (one task, about 5 minutes)

10. Start a new task on `c2-content-factory` and paste Prompt 1 from `prompts/web_prompts.md`.
11. When the session finishes, open its diff, then create the pull request and merge it on GitHub. From here every session loads the skill automatically.

## Part D. Build Week 1, one day at a time

Week 1 needs five packs. Friday 2 October is Gandhi Jayanti and has no session.

| Task | Day | What it builds |
|---|---|---|
| D1 | Mon 28 Sep | The introduction pack plus the teaching day. Blocked until client zero is locked. |
| D2 | Tue 29 Sep | Functions, errors and files, including the AI-free lab |
| D3 | Wed 30 Sep | Load, clean, profile: the profiled dataset |
| D4 | Thu 01 Oct | Descriptive statistics: the segment summary |
| SAT | Sat 03 Oct | The recap paper, the answer key and the discussion guide |

For each one: start a new task, paste the matching prompt from `prompts/web_prompts.md`, wait for the spine, approve or correct it in the same session, let the passes run, then read the verification report, open the diff, create the pull request, and merge.

Run one session per day pack. Do not ask a session to build two days.

## Part E. Review and tracking

12. Review each pull request on GitHub before merging: read the deck outline, the notebook order and the take-home first, since those carry the teaching.
13. After merging, update the day's row in the Build Tracker tab of the workbook to Reviewed, then Locked once the pull request is merged.
14. When the workbook changes, upload the new `source.xlsx` through the GitHub web uploader and run Prompt 6 so the markdown exports match it again.
