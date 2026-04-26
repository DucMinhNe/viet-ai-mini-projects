# Viet AI Assistant

This project runs a private Vietnamese AI assistant on the user's machine. It automatically checks the local AI runtime, discovers installed models, selects a sensible default model, and starts a simple terminal chat.

## What It Shows

- Local LLM integration without API keys
- Ollama HTTP API usage
- Automatic model discovery
- Graceful error handling when Ollama is not running
- Vietnamese assistant prompting

## Requirements

This project uses Ollama under the hood. Install it from:

```text
https://ollama.com
```

Start Ollama:

```bash
ollama serve
```

Pull at least one model:

```bash
ollama pull llama3.2
```

Other good local options:

```bash
ollama pull qwen2.5
ollama pull mistral
ollama pull gemma2
```

## Run

```bash
python3 viet-ai-assistant/main.py
```

Ask one question and exit:

```bash
python3 viet-ai-assistant/main.py "Summarize this project in Vietnamese"
```

Use a specific model:

```bash
python3 viet-ai-assistant/main.py --model llama3.2 "Explain local AI in simple English"
```

## How Model Selection Works

The script calls the local Ollama API at:

```text
http://localhost:11434/api/tags
```

It then chooses the first installed model that matches the preferred list:

```text
llama3.2, llama3.1, qwen2.5, qwen2, mistral, gemma2, gemma
```

If none of those are installed, it uses the first available local model.

## Portfolio Note

This project is useful because it demonstrates how to build AI tools that can run privately on a user's laptop. That matters for Vietnamese documents, internal company data, and workflows where sending data to a cloud API may not be acceptable.
