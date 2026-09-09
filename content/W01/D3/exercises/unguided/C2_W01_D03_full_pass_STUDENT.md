# Day 3, E4. Unguided: the full pass

Drop point: the last block. About 40 minutes, alone, no hints. Solution released at the close.

Take the order book from zero to something you would put your name on.

Produce three things:

1. `output/profiled_orders.csv`, the orders you would compute on.
2. `output/rejects.csv`, everything you set aside, each with the reason the interpreter gave.
3. `output/decisions_log.csv`, one line per decision, with the field, what you found, what you chose and why.

Rules that make this the real job rather than an exercise:

- Profile before you change anything, and keep the profile.
- Call `clean_record` and `clean_records` from yesterday. If you are writing a fresh conversion loop, stop and go back for the function.
- Every decision goes in the log, including the ones where you chose to change nothing.
- Reconcile at the end: input equals profiled plus rejected. Print it even when it holds.

Two things in this file need a decision rather than a cleaning step. One is a row, one is a value. Your log should show both, and neither should be deleted.

Before you look at anything, write down two numbers: how many orders you profiled, and how many you rejected. If they do not sum to 50, you have found the most valuable thing in this exercise.
