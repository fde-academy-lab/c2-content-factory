# Day 2 solution: trace three calls on paper

Read the explanation before the answer. The answer alone is worth very little in an interview.

### The idea being tested

A function hands back exactly one thing: whatever follows `return`. When there is no `return`, it hands back `None`, and `None` is a real value that travels quietly until something tries to use it.

### The answers

| Question | Answer |
|---|---|
| 1. What is in `x`? | `None`. `a` has no `return`. |
| 2. What is in `rec`? | `{'amount': 4500}`. The function changed the dictionary you passed in. |
| 3. What is in `y`? | `4500`, an `int`. |
| 4. `z`, and what appears? | `4500` appears on screen. `z` holds `None`. |
| 5. Which belongs in a pipeline? | `b`. It returns a value and changes nothing you did not ask it to change. |

`x["amount"]` raises:

```
TypeError: 'NoneType' object is not subscriptable
```

### The part worth arguing about

`a` is the dangerous one, and it is dangerous precisely because it appears to work. It changed `rec` in place, so the value really is converted, and a learner who checks `rec` afterwards concludes the function is fine. Then somebody writes `x = a(rec)` and the `None` travels three functions before it lands.

Changing something in place and returning nothing is a legitimate choice in some code. Doing it by accident is not.

### Where this pattern lives in production

Function returns `None` on a path nobody tested, the `None` is stored, and it surfaces hours later as a `NoneType` error in a component that did nothing wrong. Reading the traceback bottom-up gets you to the crash. Finding which function forgot to return is the actual work.