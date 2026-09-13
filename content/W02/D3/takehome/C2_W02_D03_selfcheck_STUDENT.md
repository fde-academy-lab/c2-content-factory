# Self-check before you hand in Wednesday's take-home

Nine checks.

## The question

1. Read your question aloud. Would somebody in Marketing ask it in those words, or does it
   contain the phrase "window function"? If the tool is in the question, rewrite the question.

2. Does the answer need the original rows back? If one number per group would satisfy the
   stakeholder, you have not found a window question yet.

## The window

3. Can you say in one line what `PARTITION BY` means here, in business terms rather than in SQL
   terms? "Partitioned by segment" is SQL. "Each member is compared only with others in their own
   tier" is business.

4. Same for the window's `ORDER BY`. If it is not obvious why that ordering and not another, the
   question is underspecified.

5. Could two rows tie on your ordering? If yes, which function did you choose and why. If no, say
   how you know, because "probably not" is not knowing.

## The impostor

6. Would a competent colleague write your impostor query and believe it? Read it back as if
   somebody else wrote it. If it looks obviously wrong, it is not doing its job.

7. Run both. Do they actually return different results on the warehouse? Not in principle,
   actually. If they agree, the exercise has not started.

8. Can you point at a specific row where they diverge and say what each query claims about it?
   Write the row down. A difference you cannot point at is a difference you have not found.

## The note

9. Your tie rule needs a business sentence, and the business sentence has to come first. If the
   sentence was reverse-engineered from the function you already chose, it will read that way.
   Write the sentence as the stakeholder would say it, then pick the function that obeys it.
