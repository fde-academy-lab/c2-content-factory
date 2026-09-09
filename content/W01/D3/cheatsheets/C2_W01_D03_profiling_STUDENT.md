# Cheat sheet: profiling and cleaning decisions

Week 1, Day 3. Print landscape. Seven panels, one crux line each.

---

## Panel 1: the three counts

```
present     the box has something in it
converts    what is in it is usable
distinct    how many different values
```

`present` minus `converts` is your work list.

**Crux:** distinct is the only count that can fall, so it is the only one that can warn you.

---

## Panel 2: reading a profile

| Shape | What it means |
|---|---|
| distinct 3 or 4 on 50 rows | A category |
| distinct near the row count | An id or a free value |
| distinct below the row count on an id | Something repeats that should not |
| converts 0 on a text field | Correct, not a failure |

**Crux:** you know where the work is before you have touched anything.

---

## Panel 3: missing is a decision

| Choice | Use when | It costs |
|---|---|---|
| Drop | Required field, value exists nowhere else | The rest of that record |
| Stated default | Absence means something you can name | Telling absent from equal-to-the-default |
| Keep and flag | You need the record and the gap must travel | Every downstream reader handles the flag |

**Crux:** a default you did not state is data you invented.

---

## Panel 4: the coercion trap

```
              RAW              COERCED
present       48/50            50/50     rose
converts      44/50            50/50     rose
distinct      46               42        FELL
```

**Crux:** every count improved and the dataset got worse.

---

## Panel 5: duplicates

```
whole-record comparison   finds only exact copies
distinct ids vs row count finds the rest
```

State the rule:

```
two rows are the same order when they share ______
```

**Crux:** an identity rule is something you state, and whoever owns the data decides it.

---

## Panel 6: outliers

```
sorted(amounts)[-5:]     read the tail
```

Converts cleanly and well formed means real until somebody says otherwise.

**Crux:** an outlier is a finding to investigate before it is a row to delete.

---

## Panel 7: what ships

```
profiled dataset    the rows you would compute on
rejects file        what you set aside, with reasons
decisions log       field, finding, choice, reason
```

```
input = profiled + rejected
```

**Crux:** the profiled dataset without its decisions log is an opinion.
