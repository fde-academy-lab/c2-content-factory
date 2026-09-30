# w00-diagnostic-llm
A golden set without an API key: twenty support tickets labelled by hand and compared with a chat assistant's labels, for the ticket classifier of Chapter 4.

## What it shows
A model's label is a pick from its scores, so one agreement rate can hide the label it hands out too often, and precision and recall per label find that label.

## How to run
Open the repository in a Codespace and run notebook.ipynb top to bottom; it reads labels.csv and prints the agreement overall and per label.

## Result
On the twenty practice tickets the two columns agreed on 16 (80 percent), and refund is the label the model over-predicts.

| label | by hand | by the model | precision | recall |
|---|---|---|---|---|
| refund | 6 | 9 | 0.67 | 1.00 |
| delivery | 9 | 7 | 0.86 | 0.67 |
| other | 5 | 4 | 1.00 | 0.80 |

## What I would do next
Run the same twenty tickets through the Figure 20 prompt, with the label list and an example each, and measure again before any real ticket is counted.
