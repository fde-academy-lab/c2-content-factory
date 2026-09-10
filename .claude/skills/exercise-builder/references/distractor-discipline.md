# Distractor discipline, and the audit that enforces it

Three failures make an item answerable without knowing anything, and all three are common enough that the audit checks every one mechanically.

## The three mechanical failures

### 1. The longest option is the key

Writers make the correct option precise and let the wrong ones stay vague, so length becomes a tell. A room learns this inside two quizzes and stops reading the options.

The fix is to write the wrong options at the same precision as the key. If the key needs a qualifier, give the distractors qualifiers too.

Failing:

```
a) It crashes.
b) It returns None.
c) It silently produces a total that is wrong by exactly the value of the rows whose amount failed to convert, and no line anywhere says so.
d) It logs a warning.
```

Passing:

```
a) It stops on the first bad row and names the value that failed.
b) It returns None, so the caller's next line fails instead.
c) It produces a total short by the rows that failed, with nothing saying so.
d) It writes a warning to the rejects log and continues with the row skipped.
```

### 2. Key positions cluster

Correct answers landing on b and c far more often than a and d is the second-most-used shortcut in any room. Across a file of fifteen items, the four positions should each carry roughly a quarter.

The audit reports the distribution and fails when any position holds less than an eighth or more than half of the keys.

### 3. A format line contains the true answers

The format line exists to show the shape of the reply. When its illustration happens to be the key, the exercise is over before it starts.

```
Post one line: 1a 2c 3b 4d 5a
```

Check that string against the key before shipping. When they collide, change the illustration rather than the key.

## The judgement failures a script cannot catch

**The nonsense option.** An option nobody would ever write eliminates itself and turns a four-way item into a three-way one. Every option is a thing a real person has actually done.

**The near-miss is the best distractor.** The strongest wrong option is right about the concept and wrong about the grain: the right statistic on the wrong denominator, the right check at the wrong point in the pass, the right fix applied to the wrong record. That is the error the room actually makes, so getting it wrong teaches something.

**Two options that are both true.** The fastest way to lose a room. Read every option against the stem and confirm that exactly one survives.

**An option that gives away a later item.** Items inside one file leak into each other more often than anyone expects. Read the file once as a learner working top to bottom.

## Running the audit

```bash
python3 scripts/distractor_audit.py content/W01/D3/exercises/unguided/C2_W01_D03_which_dataset_STUDENT.md
python3 scripts/distractor_audit.py content/W01/D3          # every file under a folder
```

It reads two shapes: a lettered bank whose keys sit in a matching solutions file, and an inline-marked quiz where the correct option carries its own marker on the line. Kahoot packs use the second shape, because Kahoot numbers its answers rather than lettering them, and the pack ships to Kahoot rather than to a learner.

The audit prints one line per file with the key-position distribution and one FAIL line per breach. It is a gate, not advice: a file with a FAIL line has not shipped.
