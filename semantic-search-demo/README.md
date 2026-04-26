# Semantic Search Demo

This project builds a lightweight document search engine using TF-IDF and cosine similarity. It ranks short AI-related documents against a user query.

## What It Shows

- Text normalization and tokenization
- Term frequency and inverse document frequency
- Vector similarity scoring
- Ranked search results with explainable scores

## Run

```bash
python3 semantic-search-demo/main.py "recommendation systems"
```

If no query is provided, the demo uses a default query.

## Why It Matters

Semantic search is a core idea behind many modern knowledge-base and retrieval systems. This simple version is not a neural embedding model, but it makes the ranking pipeline easy to understand before moving to vector databases or transformer embeddings.
