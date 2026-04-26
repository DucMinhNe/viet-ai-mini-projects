import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

COMMANDS = [
    ["python3", "sentiment-naive-bayes/main.py"],
    ["python3", "semantic-search-demo/main.py", "AI knowledge search"],
    ["python3", "anomaly-detector/main.py"],
    ["python3", "vietnamese-invoice-scanner/main.py"],
    ["python3", "vietnamese-voice-intent/main.py"],
    ["python3", "vietnamese-news-summarizer/main.py"],
]


def main():
    for command in COMMANDS:
        print(f"\n$ {' '.join(command)}", flush=True)
        result = subprocess.run(command, cwd=ROOT, check=False)
        if result.returncode != 0:
            return result.returncode

    print("\nSmoke tests passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
