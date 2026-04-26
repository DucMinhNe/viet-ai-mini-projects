import csv
import math
import random
import re
from collections import Counter, defaultdict
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "reviews.csv"
TOKEN_PATTERN = re.compile(r"[a-z']+")


def tokenize(text):
    return TOKEN_PATTERN.findall(text.lower())


def load_reviews(path):
    with path.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def train_naive_bayes(rows):
    label_counts = Counter(row["label"] for row in rows)
    token_counts = defaultdict(Counter)
    total_tokens = Counter()
    vocabulary = set()

    for row in rows:
        label = row["label"]
        tokens = tokenize(row["text"])
        token_counts[label].update(tokens)
        total_tokens[label] += len(tokens)
        vocabulary.update(tokens)

    return {
        "label_counts": label_counts,
        "token_counts": token_counts,
        "total_tokens": total_tokens,
        "vocabulary": vocabulary,
        "total_examples": len(rows),
    }


def predict(model, text):
    scores = {}
    vocab_size = len(model["vocabulary"])

    for label, label_count in model["label_counts"].items():
        log_probability = math.log(label_count / model["total_examples"])

        for token in tokenize(text):
            word_count = model["token_counts"][label][token]
            denominator = model["total_tokens"][label] + vocab_size
            log_probability += math.log((word_count + 1) / denominator)

        scores[label] = log_probability

    return max(scores, key=scores.get), scores


def evaluate(model, rows):
    true_positive = false_positive = true_negative = false_negative = 0

    for row in rows:
        expected = row["label"]
        predicted, _ = predict(model, row["text"])

        if expected == "positive" and predicted == "positive":
            true_positive += 1
        elif expected == "negative" and predicted == "positive":
            false_positive += 1
        elif expected == "negative" and predicted == "negative":
            true_negative += 1
        elif expected == "positive" and predicted == "negative":
            false_negative += 1

    total = len(rows)
    accuracy = (true_positive + true_negative) / total
    precision = true_positive / max(true_positive + false_positive, 1)
    recall = true_positive / max(true_positive + false_negative, 1)
    f1 = 2 * precision * recall / max(precision + recall, 1e-9)

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }


def main():
    rows = load_reviews(DATA_PATH)
    random.Random(17).shuffle(rows)
    split_index = int(len(rows) * 0.75)
    train_rows = rows[:split_index]
    test_rows = rows[split_index:]

    model = train_naive_bayes(train_rows)
    metrics = evaluate(model, test_rows)

    print("Evaluation")
    for name, value in metrics.items():
        print(f"{name.title()}: {value:.2f}")

    samples = [
        "The setup was simple and the experience felt excellent.",
        "The app crashed twice and support was slow.",
        "Clean design, fast results, and very useful recommendations.",
    ]

    print("\nSample Predictions")
    for text in samples:
        label, _ = predict(model, text)
        print(f"- {label:8} | {text}")


if __name__ == "__main__":
    main()
