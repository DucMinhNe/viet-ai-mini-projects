# AI Mini Tools for Vietnamese Workflows

This repository is a portfolio-style collection of small AI and data projects built with Python. The projects focus on practical use cases that are easy to understand, easy to run, and relevant to real workflows in Vietnam: document scanning, Vietnamese text processing, voice-command understanding, local AI assistants, search, classification, and anomaly detection.

The goal is not to hide complexity behind large frameworks. Most demos are intentionally implemented with the Python standard library so the core logic is visible: how text becomes tokens, how documents are scored, how fields are extracted, how commands become intents, and how local AI can run privately on a user's machine.

## Highlights

- Vietnamese-focused NLP examples for invoices, news, and voice commands.
- A private local AI assistant that uses an installed local model through Ollama.
- Lightweight algorithms that are readable enough for interview discussion.
- Sample datasets included, so every offline demo can be run immediately.
- A smoke test runner to verify the project quickly after cloning.

## Project Overview

| Project | What it does | Skills demonstrated |
| --- | --- | --- |
| [Viet AI Assistant](./viet-ai-assistant) | Runs a private Vietnamese AI assistant on the user's machine using a local model runtime. | Local LLM integration, model discovery, chat UX, privacy-first AI |
| [Vietnamese Invoice Scanner](./vietnamese-invoice-scanner) | Extracts vendor, tax code, invoice number, date, and total amount from Vietnamese invoice text. | Document AI, regex extraction, data normalization, confidence scoring |
| [Vietnamese Voice Intent](./vietnamese-voice-intent) | Classifies Vietnamese voice-command transcripts into assistant actions such as weather, reminders, music, smart home, and web search. | Intent classification, keyword scoring, assistant routing |
| [Vietnamese News Summarizer](./vietnamese-news-summarizer) | Produces short extractive summaries from Vietnamese news-style articles. | Sentence scoring, stopword filtering, extractive summarization |
| [Semantic Search Demo](./semantic-search-demo) | Ranks short documents against a query using TF-IDF and cosine similarity. | Search ranking, document vectors, similarity scoring |
| [Sentiment Naive Bayes](./sentiment-naive-bayes) | Predicts whether short product reviews are positive or negative. | Text classification, bag-of-words, Laplace smoothing, evaluation metrics |
| [Anomaly Detector](./anomaly-detector) | Detects unusual spikes and drops in time-series traffic data. | Rolling baselines, z-scores, threshold-based alerting |

## Why These Projects Matter

Many AI demos are built around generic English examples. This repository is different: several projects are designed around Vietnamese business and user workflows.

For example, a Vietnamese company might want to:

- extract fields from local invoices and receipts
- classify customer voice commands or support requests
- summarize Vietnamese business news or internal notes
- search internal documents without relying only on exact keywords
- run private AI locally when data should not leave the machine
- monitor product metrics and detect unusual activity

These are small demos, but they map to real product directions.

## Repository Structure

```text
.
├── anomaly-detector/
├── semantic-search-demo/
├── sentiment-naive-bayes/
├── viet-ai-assistant/
├── vietnamese-invoice-scanner/
├── vietnamese-news-summarizer/
├── vietnamese-voice-intent/
├── data/
└── scripts/
```

## Quick Start

Most projects use only the Python standard library.

```bash
python3 sentiment-naive-bayes/main.py
python3 semantic-search-demo/main.py "AI knowledge search"
python3 anomaly-detector/main.py
python3 vietnamese-invoice-scanner/main.py
python3 vietnamese-voice-intent/main.py
python3 vietnamese-news-summarizer/main.py
```

Run all offline demos:

```bash
python3 scripts/run_smoke_tests.py
```

## Local AI Assistant

The [Viet AI Assistant](./viet-ai-assistant) project uses Ollama under the hood. It automatically checks local models and selects a sensible default model if one is installed.

Install Ollama:

```text
https://ollama.com
```

Start the local runtime:

```bash
ollama serve
```

Pull a model:

```bash
ollama pull llama3.2
```

Run the assistant:

```bash
python3 viet-ai-assistant/main.py
```

Ask one question:

```bash
python3 viet-ai-assistant/main.py "Explain how local AI can help a Vietnamese accounting team"
```

## Example Outputs

Vietnamese invoice extraction:

```text
vendor: CONG TY TNHH CONG NGHE SAO VIET
tax_code: 0312345678
invoice_number: hd-2026-0042
date: 15/04/2026
total_vnd: 13750000
confidence: 1.0
```

Vietnamese voice intent classification:

```text
intent=calendar_reminder confidence=1.00 | nhac toi goi khach hang luc 3 gio chieu
intent=smart_home        confidence=0.50 | tat dieu hoa luc 10 gio toi
intent=web_search        confidence=0.50 | tra cuu diem tin cong nghe viet nam
```

Semantic search:

```text
Query: AI knowledge search

1. AI Knowledge Search | score=0.309
2. Personalized Learning | score=0.161
3. Customer Churn Prediction | score=0.000
```

## Technical Notes

The projects are intentionally compact. Instead of relying on a full machine learning stack, they show the mechanics behind common AI workflows:

- Naive Bayes shows how probabilistic text classification works.
- TF-IDF search shows how documents can be converted into comparable vectors.
- The invoice scanner shows how OCR/PDF text can be turned into structured records.
- The voice intent classifier shows how assistant commands can be routed.
- The summarizer shows a transparent baseline for extractive NLP.
- The local assistant shows how to connect a Python app to a local LLM runtime.

This makes the repository useful for learning, portfolio review, and interview discussion.

## Future Improvements

- Add a web interface with Streamlit or Gradio.
- Add OCR support for real PDF and image invoices.
- Add speech-to-text integration before the voice intent classifier.
- Add unit tests and GitHub Actions.
- Compare standard-library baselines with scikit-learn models.
- Add embeddings and vector database support for search.
- Add charts for anomaly detection and model evaluation.

## Suggested GitHub Description

```text
Python AI mini tools for Vietnamese NLP, document scanning, local AI assistants, semantic search, and anomaly detection.
``` 
