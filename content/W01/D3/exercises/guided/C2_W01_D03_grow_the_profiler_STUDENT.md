# Day 3, E1. Guided: grow the counter into a profiler

Drop point: the profiler section, first half. About 45 minutes, trainer-led with the room mirroring.

Monday you wrote a counter that said how many orders had a value in a field. Today it grows two more questions.

Step 1. Start from the counter you already have, and get it printing `present` for every field rather than for one.

Step 2. Add `converts`. For each field, how many values become an integer? Most fields will report zero, and that is information rather than a bug. A field where nothing converts is a text field.

Step 3. Add `distinct`. How many different values does the field hold?

Step 4. Print all three per field and read the shape aloud with the room. You are looking for exactly these lines:

```
  field          present  converts  distinct
  order_id            50         0        49
  amount              48        44        46
  discount            11        11         9
```

Step 5. One field has a `distinct` that does not match its row count, and nothing else on the printout explains it. Name that field. Do not solve it. It is the second half of the day.

Then, together, take one missingness decision end to end: pick `discount`, state the choice, and write the one-line reason underneath it.
