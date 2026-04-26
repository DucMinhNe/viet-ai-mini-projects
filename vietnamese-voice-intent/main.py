import csv
import re
import sys
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "vietnamese_voice" / "commands.csv"

INTENT_KEYWORDS = {
    "weather_query": ["thoi tiet", "mua", "nang", "nhiet do", "du bao"],
    "calendar_reminder": ["nhac toi", "lich", "cuoc hop", "goi", "luc", "hen"],
    "music_control": ["mo nhac", "phat bai", "dung nhac", "tang am luong", "giam am luong"],
    "smart_home": ["bat den", "tat den", "may lanh", "dieu hoa", "cua", "quat"],
    "web_search": ["tim", "tra cuu", "google", "kiem tra", "search"],
}


def normalize(text):
    replacements = {
        "á": "a", "à": "a", "ả": "a", "ã": "a", "ạ": "a",
        "ă": "a", "ắ": "a", "ằ": "a", "ẳ": "a", "ẵ": "a", "ặ": "a",
        "â": "a", "ấ": "a", "ầ": "a", "ẩ": "a", "ẫ": "a", "ậ": "a",
        "đ": "d",
        "é": "e", "è": "e", "ẻ": "e", "ẽ": "e", "ẹ": "e",
        "ê": "e", "ế": "e", "ề": "e", "ể": "e", "ễ": "e", "ệ": "e",
        "í": "i", "ì": "i", "ỉ": "i", "ĩ": "i", "ị": "i",
        "ó": "o", "ò": "o", "ỏ": "o", "õ": "o", "ọ": "o",
        "ô": "o", "ố": "o", "ồ": "o", "ổ": "o", "ỗ": "o", "ộ": "o",
        "ơ": "o", "ớ": "o", "ờ": "o", "ở": "o", "ỡ": "o", "ợ": "o",
        "ú": "u", "ù": "u", "ủ": "u", "ũ": "u", "ụ": "u",
        "ư": "u", "ứ": "u", "ừ": "u", "ử": "u", "ữ": "u", "ự": "u",
        "ý": "y", "ỳ": "y", "ỷ": "y", "ỹ": "y", "ỵ": "y",
    }
    lowered = text.lower()
    ascii_text = "".join(replacements.get(char, char) for char in lowered)
    return re.sub(r"\s+", " ", ascii_text).strip()


def classify(text):
    normalized = normalize(text)
    scores = {}

    for intent, keywords in INTENT_KEYWORDS.items():
        score = sum(len(keyword.split()) for keyword in keywords if keyword in normalized)
        if score:
            scores[intent] = score

    if not scores:
        return "unknown", 0.0

    intent = max(scores, key=scores.get)
    confidence = min(scores[intent] / 4, 1.0)
    return intent, round(confidence, 2)


def load_samples(path):
    with path.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def main():
    samples = [{"transcript": " ".join(sys.argv[1:]), "expected_intent": ""}]
    if len(sys.argv) == 1:
        samples = load_samples(DATA_PATH)

    print("Vietnamese Voice Intent Classifier")
    correct = 0
    for sample in samples:
        transcript = sample["transcript"]
        intent, confidence = classify(transcript)
        expected = sample.get("expected_intent", "")
        correct += int(expected == intent) if expected else 0
        label = f" expected={expected:17}" if expected else ""
        print(f"- intent={intent:17}{label} confidence={confidence:.2f} | {transcript}")

    if samples and samples[0].get("expected_intent"):
        print(f"\nAccuracy: {correct / len(samples):.2f}")


if __name__ == "__main__":
    main()
