# Vietnamese News Summarizer

This project creates an extractive summary from a Vietnamese article. It scores sentences by important word frequency and returns the highest-scoring sentences in original order.

## Run

```bash
python3 vietnamese-news-summarizer/main.py
```

You can also pass a custom article file:

```bash
python3 vietnamese-news-summarizer/main.py data/vietnamese_news/sample_article_01.txt
```

## What It Shows

- Vietnamese text normalization
- Stopword filtering
- Sentence ranking
- Extractive summarization

## Why It Matters

Vietnamese businesses often need to summarize news, reports, customer feedback, and internal documents. This project demonstrates a transparent NLP baseline before using larger language models.
