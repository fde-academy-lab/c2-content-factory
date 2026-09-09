# Day 2 solution, E3. The truncated feed

### The answers

1. Line 48 does not exist. The file ends at line 47.
2. The file has 47 lines. `len(open(path).read().splitlines())` gives it in one line.
3. The transfer was cut off part way through a record. Line 47 is the last line in the file and reads `      "signup_date": "2026-08-10"`, sitting inside the nested customer block of an order whose braces were never closed, and the array itself was never closed either.
4. The parser stops where it runs out of input. That is line 48 column 1, one step past the last thing it could read, and line 48 does not exist. The file went wrong wherever the transfer was interrupted, which is the end of line 47. A parser reports where it gave up, never where the mistake was made. Those two positions are the same only in simple cases.
5. Something close to: "The feed we received is truncated at record 5 of what looks like a longer file, so we have 4 complete records out of the batch. Please resend." What you refuse to do is hand-edit the closing brackets to make it parse. That produces a file that loads and quietly holds a fraction of the data, which is the exact failure mode from this morning.

### Where this pattern lives in production

Truncated payloads are ordinary: a connection drops, a disk fills, a job is killed at a timeout. Pipelines that repair them automatically are how partial data reaches dashboards without anybody knowing. The correct behaviour is to fail, record the batch id, and ask again.
