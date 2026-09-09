# Day 1 solution, E2. Predicting the output

### The idea being tested

A value carries its type with it, and the type decides what every operator and every method does next. You cannot read a type off the shape of a number on screen, so you ask.

### The answers

Cell 1 prints:

```
<class 'str'>
<class 'int'>
```

Cell 2 prints:

```
3755
```

Cell 3 prints:

```
True
False
```

| Cell | Why it printed that |
|---|---|
| Cell 1 | The quotes are the entire difference between the two lines, and each quote is one character wide. `'4500'` is text that happens to be made of digits, and `4500` is a number. |
| Cell 2 | Two of the three records are delivered, so the condition held twice, and 2395 plus 1360 is 3755. The returned record added nothing because the condition refused it. |
| Cell 3 | The same two values are compared twice with the same operator and the two lines disagree, because the first pair are text and the second pair are numbers. Two pieces of text are compared one character at a time, and the character 9 comes after the character 2, so the text comparison answers True. Two numbers are compared by size, so the number comparison answers False. |

The follow-on question. A person who sees only the printed True and the printed False has no way of telling which line was handed text, so neither output can be trusted on its own. The thing they have to look at is the type of the values that went into each comparison, which is what `type()` settles in one second.

### The part worth arguing about

Read cell 3 next to the `TypeError` you met earlier in the day. There Python was handed one piece of text and one number, it could make no honest comparison between them, and it stopped and told you so. Here it is handed two pieces of text, the comparison is one it can make, and it makes it and hands you an answer about the characters it was given. The refusal you met earlier and the answer you just got are the same rule running twice, which is that the type of a value decides what the operator does with it.

### Where this pattern lives in production

A column of amounts that arrived as text sorts and compares like text everywhere it travels, and the answer it produces looks exactly like the answer a column of numbers would have produced. Teams meet this on the day a report ranks an order of 900 above an order of 2000 and somebody senior asks how. Asking a column what type it holds before you compare anything inside it is the cheap habit that prevents the expensive conversation.
