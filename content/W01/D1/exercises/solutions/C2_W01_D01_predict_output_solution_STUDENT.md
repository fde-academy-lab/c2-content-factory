# Solution: predict before you run

Answers: 1b 2a 3c 4c 5a 6b

---

| Item | Key | Why, and why the rest fail |
|---|---|---|
| **1** | `b` | `*` on text repeats it, so `"4500" * 2` is `"45004500"`. It is not arithmetic because the value is text, which is the same fact that broke the running total in the demo. |
| **2** | `a` | `sum` gives 8490 and `len` gives 4, so the mean is 2122.5. Option b is the median of the sorted list, which is a different statistic and is the one you would report to a stakeholder. |
| **3** | `c` | A notebook runs cells in the order you run them, not the order they appear. Cell 2 ran when `orders` did not exist yet, so the name lookup failed. Nothing about the file is wrong; the kernel simply had not been told. |
| **4** | `c` | A dictionary raises rather than guessing. Python never invents a default, because a silent zero would make a missing discount look like a discount of nothing. Tomorrow you meet `.get()` and the reason it needs a stated default. |
| **5** | `a` | A set holds each value once, so two distinct ids remain. That is exactly why counting distinct customers uses a set rather than a counter. |
| **6** | `b` | The accumulator survives each pass because `total` is reassigned rather than recreated. Option a describes what would happen with `total = n`, which is the most common first bug. |

---

## The one to carry forward

Item 3 is the only one that is about the tool rather than the data, and it is the one that costs a
learner the most time in week one. When a notebook disagrees with what you believe, restart the
kernel and run all cells. If it passes, your screen was stale. If it fails, the notebook is wrong.
