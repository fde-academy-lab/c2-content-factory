# Day 2, E4. Unguided: the AI-free lab

Drop point: the second half, after files. About 40 minutes, working alone. Solution released at the close of the session.

This lab is AI-free. No assistant, no autocomplete suggestions accepted, no searching for a finished answer. You have your own notebook from today and the Python documentation. That is the whole toolkit, and the point is to find out what you can do without help.

The file `../data/C2_W01_D02_lab_STUDENT.csv` is one you have not seen. It has the same five fields and defects you have not met.

Produce three things:

1. `output/clean.csv`, holding every record whose amount converted, with the amount stored as a number.
2. `output/rejects.csv`, holding every record that did not, with its id and the reason.
3. A reopened count: read both output files back and print one line reconciling them against the input.

Rules that make this the real job rather than an exercise:

- Use the functions you carved this morning. If you find yourself writing a fresh loop, stop and go back for the function.
- Every rejection carries the interpreter's own reason, never wording you invented.
- Reopen both files at the end. Writing a file is not finishing.

When you are done, write down two numbers before you look at anything: how many records went in, and how many are in the two output files together. If those do not match, you have found the most valuable thing in this lab.

One defect in this file behaves differently from the two you met this morning. When you find it, write one line about why it slipped past your first attempt.
