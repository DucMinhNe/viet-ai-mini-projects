import re
import sys
from pathlib import Path


DEFAULT_PATH = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "vietnamese_documents"
    / "sample_invoice_01.txt"
)


FIELD_PATTERNS = {
    "tax_code": re.compile(r"(?:ma so thue|mst|tax code)\s*[:\-]?\s*([0-9]{10,13})", re.I),
    "invoice_number": re.compile(r"(?:so hoa don|invoice no|invoice number)\s*[:\-]?\s*([A-Z0-9\-]+)", re.I),
    "date": re.compile(r"(?:ngay|date)\s*[:\-]?\s*(\d{1,2}[\/\-]\d{1,2}[\/\-]\d{4})", re.I),
    "total_vnd": re.compile(r"(?:tong cong|total|thanh toan)\s*[:\-]?\s*([0-9\.,]+)\s*(?:vnd|dong)?", re.I),
}


def normalize_text(text):
    replacements = {
        "ã": "a",
        "á": "a",
        "à": "a",
        "ả": "a",
        "ạ": "a",
        "ă": "a",
        "ắ": "a",
        "ằ": "a",
        "ẵ": "a",
        "ẳ": "a",
        "ặ": "a",
        "â": "a",
        "ấ": "a",
        "ầ": "a",
        "ẫ": "a",
        "ẩ": "a",
        "ậ": "a",
        "đ": "d",
        "é": "e",
        "è": "e",
        "ẻ": "e",
        "ẽ": "e",
        "ẹ": "e",
        "ê": "e",
        "ế": "e",
        "ề": "e",
        "ể": "e",
        "ễ": "e",
        "ệ": "e",
        "í": "i",
        "ì": "i",
        "ỉ": "i",
        "ĩ": "i",
        "ị": "i",
        "ó": "o",
        "ò": "o",
        "ỏ": "o",
        "õ": "o",
        "ọ": "o",
        "ô": "o",
        "ố": "o",
        "ồ": "o",
        "ổ": "o",
        "ỗ": "o",
        "ộ": "o",
        "ơ": "o",
        "ớ": "o",
        "ờ": "o",
        "ở": "o",
        "ỡ": "o",
        "ợ": "o",
        "ú": "u",
        "ù": "u",
        "ủ": "u",
        "ũ": "u",
        "ụ": "u",
        "ư": "u",
        "ứ": "u",
        "ừ": "u",
        "ử": "u",
        "ữ": "u",
        "ự": "u",
        "ý": "y",
        "ỳ": "y",
        "ỷ": "y",
        "ỹ": "y",
        "ỵ": "y",
    }
    lowered = text.lower()
    return "".join(replacements.get(char, char) for char in lowered)


def extract_vendor(lines):
    for line in lines:
        cleaned = line.strip()
        if cleaned and not cleaned.lower().startswith(("hoa don", "invoice")):
            return cleaned
    return None


def parse_amount(value):
    digits = re.sub(r"[^0-9]", "", value)
    return int(digits) if digits else None


def extract_fields(text):
    normalized = normalize_text(text)
    lines = [line for line in text.splitlines() if line.strip()]
    fields = {"vendor": extract_vendor(lines)}

    for field, pattern in FIELD_PATTERNS.items():
        match = pattern.search(normalized)
        # Match the labels against the accent-folded text, but read the value
        # back from the original so casing and accents in fields like the
        # invoice number survive. normalize_text maps one char to one char, so
        # the match offsets line up with the source string.
        fields[field] = text[match.start(1):match.end(1)] if match else None

    if fields["total_vnd"]:
        fields["total_vnd"] = parse_amount(fields["total_vnd"])

    found = sum(1 for value in fields.values() if value)
    fields["confidence"] = round(found / len(fields), 2)
    return fields


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PATH
    text = path.read_text(encoding="utf-8")
    fields = extract_fields(text)

    print("Vietnamese Invoice Scanner")
    print(f"Source: {path}")
    for key, value in fields.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
