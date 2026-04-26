# Vietnamese Invoice Scanner

This mini project extracts structured information from Vietnamese invoice or receipt text. It is designed as a lightweight Document AI demo for local business documents.

## What It Extracts

- Vendor name
- Vietnamese tax code
- Invoice number
- Invoice date
- Total amount in VND
- A simple confidence score

## Run

```bash
python3 vietnamese-invoice-scanner/main.py
```

You can also pass a custom text file:

```bash
python3 vietnamese-invoice-scanner/main.py data/vietnamese_documents/sample_invoice_01.txt
```

## PDF Note

The script focuses on the AI-style extraction layer after OCR or PDF text extraction. In production, a PDF pipeline would add tools such as OCR, layout detection, and table extraction before this parser.

## Why It Matters

Many Vietnamese businesses still receive invoices, receipts, and scanned documents in semi-structured formats. A tool like this can be the first step toward automating accounting review, expense tracking, or internal document search.
