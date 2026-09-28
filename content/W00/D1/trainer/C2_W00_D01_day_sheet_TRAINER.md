# Trainer day sheet: Week 0, Monday. Arrive and set up

TRAINER ONLY. For the Programme Head, the Academic TA and the Support TA.

Module: <!-- sync:module:W00/D1 -->no module, since Week 0 sits outside the 510 hours<!-- /sync:module:W00/D1 -->. Date: <!-- sync:day-date:W00/D1 -->Mon 28 Sep 2026<!-- /sync:day-date:W00/D1 -->.

## What today is for

Nothing is taught today. By the close, every learner has a working workspace and a picture of how
the twenty weeks run. The self-rating that used to close the afternoon now opens Tuesday's
diagnostic: its first page asks each learner to rate five areas from 1 to 4 before any question is
seen, so the claim and the measurement sit in one sitting.

**Stop before** any Python, any SQL and any Kalpa story beyond the orientation deck's own lines.
Week 1 Monday opens on the client's first question, and the deck names the client and that question
without going further.

## The shape of the afternoon

The institute runs the first half of the day: arrival, document verification and its own welcome.
The help desk opens at check-in and stays open all day. The programme's orientation takes the second
half.

| Block | Duration | Who runs it | What has to happen |
|---|---|---|---|
| Check-in | First half of the day | Support TA, with the ground team | The help desk opens; every learner's name is on the list |
| 1. The orientation | 90 min | Programme Head | The academic orientation deck, then the rate-yourself moment below |
| 2. Setup | 60 min | Academic TA, with the Support TA at the help desk | The walkthrough, end to end, with the checklist ticked at the desk |

## Before the room opens

1. On the projector account, create a codespace from GitHub's `codespaces-jupyter` template and let
   it finish installing. The template installs its packages after the editor opens, so a first cell
   run too early can fail on an import; rehearse the wait.
2. Open `notebooks/population.ipynb` and run its first cell. A line chart titled "Population of
   Atlantis" confirms the whole path.
3. In the same codespace's terminal, stage the deliberate failure below and leave the terminal open.
4. Print one help desk checklist per learner, plus ten spares.
5. Get the LMS address and each learner's login from the ground team. No source in the repository
   carries them, so the walkthrough leaves that slot for the ground team to fill.

## Block 1: the orientation, 90 minutes

Present `slides/C2_W00_D01_orientation_STUDENT.pptx`, the Programme Head's academic orientation.
Its speaker notes carry the talk track, slide by slide, with the number of clicks each slide needs.
The repository copy replaces every staff and faculty name with a role, as a public repository must;
the names are said aloud in the room and shared with learners separately, as slide 31 says.

**The deliberate failure: rate yourself out of ten.** After the last slide and before setup, ask the
room to rate its Python out of ten, take three numbers, and ask each of the three what their number
lets them do. Most answer with another number or with "quite a lot", which is the failure: a rating
with no task attached tells nobody anything. Tomorrow's diagnostic asks for the same rating on a
scale where each point is a task, from "I have not used this" to "I can find and fix mistakes in
someone else's version".

**What the orientation settles.** The evaluation scheme is locked, so the deck's marks, weights and
build-week split can be answered directly. The IITGN faculty sessions stay out of the answers: every
one is tentative until IIT Gandhinagar confirms the faculty and the date.

## Block 2: setup, 60 minutes

Run it from `whiteboards/C2_W00_D01_setup_walkthrough_STUDENT.md` on the projector, one step at a
time, with the room following on its own laptops. The help desk takes anything that does not work
within two minutes, so the room keeps moving.

**The deliberate failure: the wrong environment.** After the population cell has run, switch to the
terminal staged before the session and run:

```
python3 -m venv /tmp/bare
/tmp/bare/bin/python -c "import pandas"
```

The room sees the last line of the traceback:

```
ModuleNotFoundError: No module named 'pandas'
```

The same import worked a minute earlier in the notebook. The difference is the environment: the
codespace installed its packages into one Python, and this command asked a bare one. Say it in one
sentence and move on: when VS Code asks which environment to run a notebook in, pick the Python
environment the codespace set up, and if a cell says a module is missing, bring it to the help desk
rather than installing things at random. Week 1 Monday teaches what a kernel is; today stops at the
choice.

### What goes wrong, and the fix

| Symptom | Likely cause | Fix at the help desk |
|---|---|---|
| The verification email from GitHub does not arrive | It went to spam, or the address was mistyped | Check spam, resend it from the sign-up page, or start again with another address |
| The codespace takes minutes to open, or the first cell fails on an import | The template is still installing its packages | Wait until the terminal has finished, then run the cell again |
| The notebook asks which kernel or environment to use | It has not been chosen yet | Choose the Python environment the codespace set up |
| `ModuleNotFoundError` on a cell | Another environment was chosen | Switch to the codespace's Python environment, then run the cell again |
| The learner closed the tab and assumes the codespace stopped | Closing the tab does not stop it | Stop it from github.com/codespaces; it also stops after 30 minutes idle |
| GitHub Education asks for an academic email or a document the learner does not have yet | The application wants proof of current enrolment | Note the learner as pending and restart the application once the institute's ID or enrolment letter is issued |
| The LMS login fails | Credentials not issued, or a typo | Take it to the ground team the same day |

### The help desk checklist

Five ticks per learner, recorded on the desk's sheet: GitHub account created and email verified; the
codespace open; the population cell run with its chart showing; the LMS login working; the GitHub
Education application submitted, or pending with its reason noted.

## The interview angle, with the answers

The two questions are staples. The room meets them today as questions; the answers below are for
the team, so a one-to-one can hold a learner to them.

**[S] Rate yourself in Python out of ten, and tell me what you would expect a seven to be able to
do.** A strong answer gives a number and then the tasks behind it: "A five. I can read a file into
records, loop over them and total a field, write a function that returns a value, and read a
traceback to the failing line. A seven would also organise a small script into functions others can
reuse and work in pandas without looking up every method; that is what I am working on." The number
matters less than the tasks, and a candidate who names the next level shows they know where they
stand.

**[S] Tell me about yourself in one minute, with one thing you have built.** About twenty seconds on
who you are, thirty on one thing you built (what it did, why you built it, one thing that broke and
what you changed), and ten on the role you are here to become. Wednesday's introductions are the
four-minute version of the same answer.

## What to record today

1. The help desk sheet: five ticks per learner, and the reason for every missing tick.
2. Who is pending on GitHub Education, and what they are waiting for.
3. The setup failures that recurred, so Tuesday starts with them fixed, since the diagnostic runs
   in each learner's browser.

## Tomorrow

The diagnostic runs for about 90 minutes on the Google Form, with a paper copy for anyone whose
laptop fails, and with no second tab, no notes and no AI assistant. It is taken cold by design, so
nothing is assigned tonight. The only after-class task is setup: a laptop that cannot open a browser
page tomorrow goes to the help desk before the diagnostic starts.
