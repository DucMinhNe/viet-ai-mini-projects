import re
import sys
from collections import Counter
from pathlib import Path


DEFAULT_PATH = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "vietnamese_news"
    / "sample_article_01.txt"
)

STOPWORDS = {
    "va", "la", "cua", "cho", "cac", "mot", "nhung", "voi", "trong", "khi",
    "duoc", "tu", "da", "se", "ve", "tai", "theo", "nay", "vao", "den",
    "co", "khong", "nguoi", "do", "hon", "sau", "truoc", "ra", "len",
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
    return "".join(replacements.get(char, char) for char in text.lower())


def split_sentences(text):
    return [sentence.strip() for sentence in re.split(r"(?<=[.!?])\s+", text) if sentence.strip()]


def tokenize(text):
    return re.findall(r"[a-z0-9]+", normalize(text))


def summarize(text, sentence_count=3):
    sentences = split_sentences(text)
    words = [word for word in tokenize(text) if word not in STOPWORDS and len(word) > 2]
    frequencies = Counter(words)
    scored = []

    for index, sentence in enumerate(sentences):
        tokens = [word for word in tokenize(sentence) if word not in STOPWORDS]
        score = sum(frequencies[word] for word in tokens) / max(len(tokens), 1)
        scored.append((score, index, sentence))

    selected = sorted(scored, reverse=True)[:sentence_count]
    return [sentence for _, _, sentence in sorted(selected, key=lambda item: item[1])]


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
    text = path.read_text(encoding="utf-8")
    summary = summarize(text)

    print("Vietnamese News Summarizer")
    print(f"Source: {path}\n")
    for sentence in summary:
        print(f"- {sentence}")


if __name__ == "__main__":
    main()
