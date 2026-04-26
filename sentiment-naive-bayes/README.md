# Sentiment Naive Bayes

This project trains a small Naive Bayes text classifier to predict whether a short product review is positive or negative.

## What It Shows

- Text preprocessing with tokenization
- Bag-of-words classification
- Laplace smoothing for unseen words
- Accuracy, precision, recall, and F1 score
- Human-readable prediction output

## Run

```bash
python3 sentiment-naive-bayes/main.py
```

## Example Output

```text
Evaluation
Accuracy: 1.00
Precision: 1.00
Recall: 1.00
F1: 1.00
```

## Notes

This implementation avoids external dependencies so the core algorithm is easy to inspect. It is not meant to beat production NLP systems, but it demonstrates the fundamentals behind many text classifiers.
