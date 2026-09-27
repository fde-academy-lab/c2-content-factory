# Trainer day sheet: Week 0, Monday. Arrive and set up

TRAINER ONLY. For the Programme Head, the Academic TA and the Support TA.

Module: <!-- sync:module:W00/D1 -->no module, since Week 0 sits outside the 510 hours<!-- /sync:module:W00/D1 -->. Date: <!-- sync:day-date:W00/D1 -->Mon 28 Sep 2026<!-- /sync:day-date:W00/D1 -->.

## What today is for

Nothing is taught today. By the close, every learner has a working workspace, a self-rating on file
and a picture of how the twenty weeks run. Tomorrow's diagnostic measures what today's self-rating
claims, and the gap between the two is the most useful number of the week, which belongs to the
learner.

**Stop before** any Python, any SQL and any Kalpa story. Week 1 Monday opens on the client's first
question, so today names the client in one line and says nothing more about it.

## The shape of the afternoon

The institute runs the first half of the day: arrival, document verification and its own welcome.
The help desk opens at check-in and stays open all day. The programme's orientation takes the second
half, which the student Week 0 sheet describes as about three hours.

| Block | Duration | Who runs it | What has to happen |
|---|---|---|---|
| Check-in | First half of the day | Support TA, with the ground team | The help desk opens; every learner's name is on the list |
| 1. The welcome | 90 min | Programme Head | The deck: the twenty weeks, the shape of a week, the three seats, this week |
| 2. Setup | 60 min | Academic TA, with the Support TA at the help desk | The walkthrough, end to end, with the checklist ticked at the desk |
| 3. The self-rating | 15 min | Academic TA | The form, filled in alone and collected |

That is 165 minutes, which leaves about fifteen minutes of the three-hour slot for the move between
blocks and the help desk queue.

## Before the room opens

1. On the projector account, create a codespace from GitHub's `codespaces-jupyter` template and let
   it finish installing. The template installs its packages after the editor opens, so a first cell
   run too early can fail on an import; rehearse the wait.
2. Open `notebooks/population.ipynb` and run its first cell. A line chart titled "Population of
   Atlantis" confirms the whole path.
3. In the same codespace's terminal, stage the deliberate failure below and leave the terminal open.
4. Print one self-rating form and one help desk checklist per learner, plus ten spares.
5. Get the LMS address and each learner's login from the ground team. No source in the repository
   carries them, so the walkthrough leaves that slot for the ground team to fill.

## Block 1: the welcome, 90 minutes

The deck carries the facts. Four things decide whether the block lands.

**The journey map before the rules.** The room should be able to say, by the end of the first ten
minutes, that there are four kinds of week and that the rhythm is two teaching weeks, then a build
week, five times. Everything else in the deck hangs on that picture.

**The three seats.** The business owner states a problem in business words; the AI engineer builds
the thing that answers it; the forward deployed engineer makes it work inside the client's own
systems. Say plainly that the seats are this programme's own construction, and that every build week
asks each group to sit all three. A technique is worth learning when some business owner needs its
answer, some engineer has to build it, and someone has to make it run where the client works.

**The deliberate failure: rate yourself out of ten.** Slide D14 asks the room to rate its Python out
of ten and then asks what a seven can do. Take three numbers from the room, then ask each of the three
what their number lets them do. Most will answer with another number or with "quite a lot". That is
the failure the slide exists for: a rating with no task attached tells nobody anything, in an
interview or in a one-to-one. D15 answers it with descriptors, which are the ones on the self-rating
form at the end of the afternoon.

**What the welcome does not say.** No marks, weights, percentages or thresholds: the evaluation
scheme is a proposal awaiting the AOC. No IITGN faculty sessions: they are tentative until IIT
Gandhinagar confirms the faculty and the dates. No placement numbers beyond the student sheet's own
wording. If a learner asks about any of these, the honest answer is that it is being finalised and
will be published when it is fixed.

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

## Block 3: the self-rating, 15 minutes

Hand out `paper/C2_W00_D01_self_rating_STUDENT.md` printed. Each topic has four levels with
descriptors, and the learner circles the one that describes what they can do today, alone. Two rules,
said once: there is no right answer, only an honest one, because tomorrow measures it; and nobody
sees another learner's form. Collect every form before anyone leaves: the self-rating goes onto the
baseline card beside Tuesday's measured result, and the card is agreed in a one-to-one with a TA on
Wednesday or Thursday.

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
3. Every self-rating form, collected, with the target role each learner wrote on it.
4. The setup failures that recurred, so Tuesday morning starts with them fixed.

## Tomorrow

The diagnostic runs on paper with no assistant, and it is taken cold by design, so nothing is
assigned tonight. The only after-class task is setup: anything that failed today goes to the help
desk before the papers begin.
