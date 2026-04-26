# AI Mini Projects Portfolio

This repository contains a set of small, practical AI and data science projects built with plain Python. Each project is designed to be easy to read, easy to run, and useful as a portfolio signal for recruiters or technical reviewers.

## Projects

| Project | What it demonstrates | Key ideas |
| --- | --- | --- |
| [Sentiment Naive Bayes](./sentiment-naive-bayes) | A text classifier that predicts whether short product reviews are positive or negative. | Tokenization, bag-of-words features, Laplace smoothing, evaluation metrics |
| [Semantic Search Demo](./semantic-search-demo) | A small search engine that ranks documents by meaning-related keyword overlap. | TF-IDF, cosine similarity, document ranking |
| [Anomaly Detector](./anomaly-detector) | A simple detector for unusual values in time-series data. | Rolling baseline, z-score, threshold-based alerts |
| [Vietnamese Invoice Scanner](./vietnamese-invoice-scanner) | Extracts structured fields from Vietnamese invoice or receipt text. | Document AI, regex extraction, confidence scoring |
| [Vietnamese Voice Intent](./vietnamese-voice-intent) | Classifies Vietnamese voice-command transcripts into practical intents. | Keyword features, intent classification, assistant routing |
| [Vietnamese News Summarizer](./vietnamese-news-summarizer) | Creates short extractive summaries from Vietnamese news articles. | Sentence scoring, Vietnamese stopwords, extractive NLP |
| [Viet AI Assistant](./viet-ai-assistant) | Runs a private Vietnamese AI assistant on the user's machine. | Local LLMs, model discovery, chat UX, privacy-first AI |

## Quick Start

These projects use only the Python standard library.

```bash
python3 sentiment-naive-bayes/main.py
python3 semantic-search-demo/main.py "machine learning search"
python3 anomaly-detector/main.py
python3 vietnamese-invoice-scanner/main.py
python3 vietnamese-voice-intent/main.py
python3 vietnamese-news-summarizer/main.py
python3 viet-ai-assistant/main.py
```

## Why This Repository Exists

The goal is to show practical AI foundations without hiding everything behind large frameworks. The code is intentionally compact and readable, so someone reviewing the repository can quickly understand:

- how the data is represented
- how the model or scoring logic works
- how predictions are evaluated
- how results are explained in the terminal

## Suggested GitHub Description

> A small AI portfolio repository with practical Python demos for sentiment classification, semantic search, and anomaly detection.

## Future Improvements

- Add unit tests for each project.
- Add charts for model performance and anomaly detection.
- Add a Streamlit or Gradio interface for interactive demos.
- Replace the simple algorithms with scikit-learn or transformer-based models for comparison.
