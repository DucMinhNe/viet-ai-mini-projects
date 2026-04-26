# Vietnamese Voice Intent Classifier

This project classifies Vietnamese voice-command transcripts into assistant intents. It simulates the NLP layer that would run after speech-to-text.

## Supported Intents

- `weather_query`
- `calendar_reminder`
- `music_control`
- `smart_home`
- `web_search`
- `unknown`

## Run

```bash
python3 vietnamese-voice-intent/main.py
```

You can pass your own transcript:

```bash
python3 vietnamese-voice-intent/main.py "nhắc tôi gọi khách hàng lúc 3 giờ chiều"
```

## Why It Matters

Voice AI systems usually have two steps: speech-to-text and intent understanding. This project focuses on the intent understanding step for Vietnamese commands, which is useful for assistants, smart-home tools, and customer support automation.
