# Day 3, E2. Mid-session: which dataset would you trust

Drop point: the break in the first half. About 15 minutes. No computer.

Two profiles of the same order book arrive from two colleagues.

```
              A                                    B
amount    present 48/50  converts 44/50        present 50/50  converts 50/50
          distinct 46                          distinct 42
discount  present 11/50  distinct 9            present 50/50  distinct 9
status    present 50/50  distinct 3            present 50/50  distinct 3
```

1. Which of these two datasets would you compute on, and why?
2. Three counts moved between A and B. For each one, say what a colleague would have had to do to move it that way.
3. One count went down. Explain in one sentence how a cleaning step can reduce the number of distinct values in a column.
4. B's author says the data is now clean because nothing fails to convert. What is the strongest one-sentence reply?
5. If you were handed only B, with no A to compare against, name the one check that would still have caught it.

Question 5 is the one to write carefully. It is the difference between spotting this and living with it.
