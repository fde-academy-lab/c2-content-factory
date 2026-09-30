# Which extra should you take tonight, the stretch or the recovery?

Both are optional and neither is graded. Pick the one that matches where you are, even if the other
sounds better. The stretch writes the day's mix-and-rate split once, as a function, and the
recovery rebuilds the day's grouping one step at a time.

**Who needs the answer.** You do. Anand Iyer, Kalpa Retail's finance controller, wants the
mix-and-rate split run again next quarter by somebody else, and the rest of the week keeps grouping
orders by key. A split nobody can rerun, or a grouping step that never landed, costs more later than
it does tonight.

**The questions on the way.**

- Can you write the split of revenue per order into mix and rate as one function Anand can trust?
- Can you rebuild the day's grouping one step at a time on the class file?

---

## Stretch. Can you write the split of revenue per order into mix and rate as one function Anand can trust?

This one is for you if you finished the take-home early and the afternoon's mix against rate felt
like arithmetic you did by hand.

### What does Anand ask for after the afternoon?

> "Your split of revenue per order into mix and rate convinced me for one quarter. Next quarter
> somebody else will run it, on a different file, at the end of a long day. Give me the split as
> something that cannot be done differently twice."
>
> Anand Iyer, finance controller, Kalpa Retail

Revenue per order is revenue over orders, taken across every segment together. The mix is each
segment's share of orders, and a segment's rate is its own revenue per order. The split prices the
later period's mix at each segment's earlier rate: what that moves is the mix part, and the rest, the
change inside the segments, is the rate part.

### What must `mix_and_rate` do, step by step?

Write one function, `mix_and_rate(before_rows, after_rows, key)`, that returns a dictionary with
four entries: the overall rate before, the overall rate after, the part of the change explained by
the mix of groups, and the part explained by the rates within groups.

| Step | What it must do |
|---|---|
| 1 | It groups both sets of rows by `key` with your own accumulator and counts the groups in each. |
| 2 | It computes each group's share of orders and its revenue per order, before and after. |
| 3 | It computes what the overall rate would have been with the after mix and the before rates. |
| 4 | It returns the mix part and the rate part, and checks that they add up to the whole change. |
| 5 | It refuses, with a clear message, when a group exists on one side only. |

### Which check on the class file must it pass?

On the class file, with `key="segment"`, it reproduces the afternoon's split of the Rs 33,231 rise
in revenue per order, Rs 1,84,211 in Q1 to Rs 2,17,442 in Q2: Rs 22,902 of mix and Rs 10,330 of
rate, within a rupee.

### What should the function do with a group that exists on one side only?

Step 5 is the hard part. A group that exists on one side only has no before rate or no after rate,
and the split has no honest answer for it. Decide what the function does, write the reason in its docstring, and then
run it on the take-home file, the regional export, with `key="channel"`, and say in one line what the
split tells the regional operations head.

### How do you know the function is done well?

The function prints nothing, returns its answer whenever an honest answer exists, and carries a
docstring from which a colleague could learn what happens to a missing group without opening the
code.

---

## Recovery. Can you rebuild the day's grouping one step at a time on the class file?

This one is for you if the session moved fast and the accumulator did not land. Rebuilding it
tonight costs you nothing tomorrow.

### Which seven steps rebuild the grouping?

Work in a fresh cell in chapter 2's notebook, `notebooks/C2_W01_D02_02_which_branch_STUDENT.ipynb`,
and run after each step. Each order in the class file is a record, a dictionary, that carries its
`quarter`, its `segment` and its `amount` in rupees.

1. Print the first three records on their own, and point at the quarter and the segment in each.
2. Make an empty dictionary, `counts = {}`, and print it. It prints `{}`.
3. Take the first record only. Put its quarter into `counts` with the value 1, and print `counts`.
4. Now write the loop over every record that adds 1 to its quarter's count, creating the entry the
   first time a quarter is seen. Print `counts`. It should say 114 for Q1 and 86 for Q2.
5. Change the key to the pair `(order["quarter"], order["segment"])`. Before you run it, write down
   how many keys you expect. Run it and count them.
6. Wrap steps 4 and 5 in a function, `count_by(rows, field)`, that ends in `return counts`. Call it,
   store the result, and print the stored result. Then change `return` to `print` once, run it
   again, and print the stored result, which now says `None`.
7. On three invented orders of Rs 1,000, Rs 1,200 and Rs 40,000, write the median, the minimum, the
   maximum and the range by hand, then check each with code. The median is the middle value once the
   orders are sorted, and the range is the largest less the smallest.

### What should the recovery leave you believing about grouping and functions?

Grouping is one move: a dictionary, a key, and an update per record. A function is worth writing
when it hands its answer back, and the `None` you saw in step 6 is what every table built on a
printing function is full of.

### What if the three invented orders in step 7 surprised you?

Look at the gap between the mean and the median of those three invented orders, and say in one
sentence which of the two you would put in a note to Meera Raghavan, Kalpa Retail's CEO.
