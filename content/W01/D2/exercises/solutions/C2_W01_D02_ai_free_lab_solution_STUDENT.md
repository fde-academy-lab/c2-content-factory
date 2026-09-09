# Day 2 solution, E4. The AI-free lab

### What you should have seen

```
input 24, clean 21, rejected 3
{'order_id': 'KR5303', 'reason': "invalid literal for int() with base 10: 'nine hundred'"}
{'order_id': 'KR5307', 'reason': "invalid literal for int() with base 10: ''"}
{'order_id': 'KR5312', 'reason': "invalid literal for int() with base 10: '1,240'"}
```

Total of the 21 clean amounts: `34515`.

Reconciliation: 24 in, 21 plus 3 out. If your two output files hold fewer than 24 rows between them, records vanished inside your loop, and finding where is more valuable than the totals.

### The defect that behaves differently

`1,240` is the one. The other two are unusable: `nine hundred` is a word and the empty string holds nothing at all. `1,240` is a real number wearing a thousands separator, so it is recoverable, and that makes it a decision rather than a rejection.

You have three defensible answers and one indefensible one.

| Choice | Defence |
|---|---|
| Reject it, note the format in the reason | Safe. The supplier learns their export is wrong. You lose 1,240 from today's total. |
| Strip the comma and convert | Recovers the value. You have now decided that commas are decoration, which is wrong in locales where the comma is the decimal point. |
| Reject it today, ask the supplier, repair tomorrow with a written rule | The one a reviewer will not argue with. |
| Strip every non-digit character from every amount | The indefensible one. It converts `1,240` and also converts `4500 refund` into `4500`. |

If you stripped the comma, you were right that the value is recoverable and you skipped the step where you write down the rule. Write it down now.

### Why your first attempt may have missed it

If you tested only for an empty string, `1,240` sailed past the check and failed later at `int()`. That is the argument for attempting the conversion and catching the failure rather than trying to predict every wrong shape in advance. You cannot list all the ways a value can be wrong. You can catch the one thing that goes wrong when you use it.

### Where this pattern lives in production

Thousands separators, currency prefixes, trailing spaces and locale decimal points are the four most common reasons a numeric column arrives as text. Every mature ingestion codebase has a normaliser for each, and a comment explaining which locale it assumes.
