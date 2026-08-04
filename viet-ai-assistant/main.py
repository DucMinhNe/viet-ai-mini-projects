import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path


OLLAMA_URL = "http://localhost:11434"
PROMPT_PATH = Path(__file__).resolve().parents[1] / "data" / "ollama_prompts" / "system_prompt.txt"
PREFERRED_MODELS = ["llama3.2", "llama3.1", "qwen2.5", "qwen2", "mistral", "gemma2", "gemma"]


class OllamaError(RuntimeError):
    pass


def request_json(path, payload=None):
    url = f"{OLLAMA_URL}{path}"
    data = None
    method = "GET"
    headers = {"Content-Type": "application/json"}

    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        method = "POST"

    request = urllib.request.Request(url, data=data, headers=headers, method=method)

    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError as error:
        raise OllamaError(
            "Cannot connect to Ollama. Start it with `ollama serve`, then run this script again."
        ) from error
    except json.JSONDecodeError as error:
        raise OllamaError("Ollama returned an invalid JSON response.") from error


def list_models():
    response = request_json("/api/tags")
    return [model["name"] for model in response.get("models", [])]


def choose_model(models, requested_model=None):
    if requested_model:
        if requested_model in models:
            return requested_model
        for model in models:
            if model.startswith(requested_model + ":"):
                return model
        raise OllamaError(f"Requested model `{requested_model}` is not installed locally.")

    for preferred in PREFERRED_MODELS:
        for model in models:
            if model.startswith(preferred):
                return model

    if models:
        return models[0]

    raise OllamaError("No Ollama models found. Install one with `ollama pull llama3.2`.")


def chat(model, messages):
    payload = {
        "model": model,
        "messages": messages,
        "stream": False,
        "options": {
            "temperature": 0.4,
            "num_predict": 500,
        },
    }
    response = request_json("/api/chat", payload)
    return response.get("message", {}).get("content", "").strip()


def load_system_prompt():
    return PROMPT_PATH.read_text(encoding="utf-8").strip()


def run_single_prompt(model, prompt):
    messages = [
        {"role": "system", "content": load_system_prompt()},
        {"role": "user", "content": prompt},
    ]
    print(chat(model, messages))


def run_interactive_chat(model):
    messages = [{"role": "system", "content": load_system_prompt()}]

    print("Viet AI Assistant")
    print(f"Model: {model}")
    print("Type `exit` to quit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            break
        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})
        answer = chat(model, messages)
        messages.append({"role": "assistant", "content": answer})
        print(f"AI: {answer}\n")


def parse_args():
    parser = argparse.ArgumentParser(description="Run a private Vietnamese AI assistant on your machine.")
    parser.add_argument("prompt", nargs="*", help="Optional one-shot prompt. If omitted, chat mode starts.")
    parser.add_argument("--model", help="Use a specific installed Ollama model.")
    parser.add_argument("--list-models", action="store_true", help="List installed Ollama models and exit.")
    return parser.parse_args()


def main():
    args = parse_args()

    try:
        models = list_models()

        if args.list_models:
            print("Installed Ollama models")
            for model in models:
                print(f"- {model}")
            return

        model = choose_model(models, args.model)
        prompt = " ".join(args.prompt).strip()

        if prompt:
            run_single_prompt(model, prompt)
        else:
            run_interactive_chat(model)
    except OllamaError as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
