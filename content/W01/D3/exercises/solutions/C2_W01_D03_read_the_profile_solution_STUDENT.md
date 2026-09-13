# Solution: read the profile, decide what you trust

Answers: 1a 2c 3b 4d 5c 6a

---

| Item | Key | Why, and why the rest fail |
|---|---|---|
| **1** | `a` | Export A's defects are visible and countable before anything runs, which means they can be decided on and recorded. Export B looks clean and has no way of showing you what an upstream step already removed. A file with no visible defects is either genuinely clean or has been silently repaired. |
| **2** | `c` | One distinct status across 201 orders means no order was ever returned or cancelled, which does not happen. Something filtered or defaulted on the way out. `b` is the seductive one: delivered is indeed most orders, and "most" is not "all". |
| **3** | `b` | It proves repetition and nothing more. `a` assumes they are duplicates before the identity rule has been applied, `c` assumes a cause, and `d` assumes the repeated rows carry revenue in proportion to their count, which is exactly the arithmetic you have to check. |
| **4** | `d` | It is not an order. `a` is real data, `b` is a formatting difference on a real order, and `c` describes most of the customers in any retail file. Only one of the four was never a transaction. |
| **5** | `c` | The default itself might be defensible. What is lost is the count and the reason, and an auditor cannot ask about rows nobody recorded. The pass still runs and you can no longer say what it did. |
| **6** | `a` | Three rows in 201 is small and that is not the point. A pass that loses three rows without saying so is a pass that will lose thirty on a bigger file, and you will not know then either. |

---

## The one to carry forward

Item 1 is the counter-intuitive one and it is the one interviewers like. The messier file is the
one you can defend, because every defect in it has a count and a decision attached. The tidy file
has an upstream step nobody documented.
