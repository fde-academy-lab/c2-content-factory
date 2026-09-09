# Day 2 unguided exercise: trace three calls on paper

Drop point: the break in the first half. About 15 minutes. No computer. Write your answers down before anyone runs anything.

```
def a(record):
    record["amount"] = int(record["amount"])

def b(record):
    return int(record["amount"])

def c(record):
    amount = int(record["amount"])
    print(amount)
```

For each line below, write what the named variable holds afterwards.

1. `rec = {"amount": "4500"}` then `x = a(rec)`. What is in `x`?
2. What is in `rec` after that same call?
3. `y = b({"amount": "4500"})`. What is in `y`?
4. `z = c({"amount": "4500"})`. What appears on screen, and what is in `z`?
5. One of these three functions is the one you would put in a pipeline. Which, and why?

Then, without running it: `x["amount"]` on the result of question 1 raises something. Name the exception and the exact message.