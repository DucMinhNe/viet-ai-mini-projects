import csv
import math
import re
import sys
from collections import Counter
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "documents.csv"
TOKEN_PATTERN = re.compile(r"[a-z0-9]+")


def tokenize(text):
    return TOKEN_PATTERN.findall(text.lower())


def load_documents(path):
    with path.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def term_frequency(tokens):
    counts = Counter(tokens)
    total = len(tokens) or 1
    return {token: count / total for token, count in counts.items()}


def inverse_document_frequency(documents):
    document_count = len(documents)
    frequencies = Counter()

    for document in documents:
        frequencies.update(set(tokenize(document["content"])))

    return {
        token: math.log((1 + document_count) / (1 + count)) + 1
        for token, count in frequencies.items()
    }


def build_vector(tokens, idf):
    tf = term_frequency(tokens)
    return {token: score * idf.get(token, 0.0) for token, score in tf.items()}


def cosine_similarity(left, right):
    shared_tokens = set(left) & set(right)
    numerator = sum(left[token] * right[token] for token in shared_tokens)
    left_norm = math.sqrt(sum(value * value for value in left.values()))
    right_norm = math.sqrt(sum(value * value for value in right.values()))

    if left_norm == 0 or right_norm == 0:
        return 0.0

    return numerator / (left_norm * right_norm)


def search(query, documents, limit=3):
    idf = inverse_document_frequency(documents)
    query_vector = build_vector(tokenize(query), idf)
    results = []

    for document in documents:
        document_vector = build_vector(tokenize(document["content"]), idf)
        score = cosine_similarity(query_vector, document_vector)
        results.append((score, document))

    return sorted(results, key=lambda item: item[0], reverse=True)[:limit]


def main():
    query = " ".join(sys.argv[1:]) or "machine learning recommendations"
    documents = load_documents(DATA_PATH)
    results = search(query, documents)

    print(f"Query: {query}\n")
    print("Top Results")

    for rank, (score, document) in enumerate(results, start=1):
        print(f"{rank}. {document['title']} | score={score:.3f}")
        print(f"   {document['content']}")


if __name__ == "__main__":
    main()
