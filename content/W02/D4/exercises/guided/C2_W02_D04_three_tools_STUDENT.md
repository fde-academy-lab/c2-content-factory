# Guided: one node, three tools

Built together, with all three versions on screen at the same time rather than in sequence. The
comparison is the content.

## The node

Revenue per segment. You have answered it twice already, so nothing here is about getting the
number.

## Step 1: the Week 1 version, from memory

Write the plain Python accumulator without looking it up. A dictionary, a loop, `.get` with a
default.

Count the lines. Count how many of them are about your question and how many are about
bookkeeping.

## Step 2: the Monday version

Write the SQL. Notice that the join to `customers` is needed because segment lives on the
customer, and that nothing in the query is about bookkeeping at all.

## Step 3: today's version

```python
orders.groupby("segment")["amount"].sum()
```

One line. Run all three and confirm the numbers agree to the rupee. If any disagree, stop and find
out why before moving on, because the rest of the day assumes they do.

## Step 4: the question that is not about length

Which is shortest is obvious and mostly irrelevant. Answer these three instead, out loud, for this
node:

```
Who owns this number?
For how long?
Who has to be able to read it?
```

For revenue per segment on Anand's Monday report, the answers pick SQL and nothing else comes
close. Say why in one sentence.

## Step 5: change the question and watch the answer change

Now the node is "revenue per segment, for a model I am prototyping this afternoon, which I will
throw away on Friday".

Same three questions. A different tool wins. Say which and why.

## Step 6: the one you would refuse

Somebody proposes that Finance's Monday number be produced by a notebook that an analyst runs.

Write the refusal in one sentence, and make the sentence about audit rather than about pandas.

## Before moving on

Everybody writes their three answers to step 4 down. They are the first three sentences of
tonight's tool note.
