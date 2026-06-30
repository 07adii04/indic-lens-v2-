# Indic Lens V2

Scan any Indian script, get instant translation — extracted text, translated text, and audio playback, all from a single photo.

🔗 **Live Demo:** https://indic-lens-v2.onrender.com

## What it does

Point it at any image with text — a street sign, a book page, a food label, a handwritten note — and it will:

1. Extract the text using Google Vision API (handles Devanagari, Bengali, Tamil, Telugu, and more)
2. Translate it into your chosen language using Google Translate API
3. Read the translation aloud using browser-based text-to-speech

Built to solve a real problem — millions of people in India encounter text in scripts they can't read every day. This turns a photo into something they can understand and hear.

## Features

- Upload any image containing text
- OCR extraction powered by Google Vision API
- Translation across 6 languages — Hindi, English, Bengali, Telugu, Marathi, Tamil
- Voice playback of translated text (Play / Pause / Stop) using the Web Speech API
- Clean, responsive UI — works on mobile and desktop
- Fully deployed and live

## Tech Stack

- **Backend:** FastAPI, Python 3.12
- **OCR:** Google Cloud Vision API
- **Translation:** Google Cloud Translation API
- **Voice:** Web Speech API (browser-native, no extra cost)
- **Frontend:** HTML, CSS, vanilla JavaScript
- **Deployment:** Render

## Architecture
indic-lens-v2/
├── main.py              # FastAPI app entry point
├── routers/
│   └── ocr.py            # API routes — /health, /extract
├── models/
│   └── schemas.py         # Pydantic request/response models
├── services/
│   └── vision.py          # Google Vision + Translate API integration
├── static/
│   └── index.html          # Frontend UI
└── requirements.txt

## API Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/` | Serves the frontend UI |
| GET | `/api/v1/health` | Health check |
| POST | `/api/v1/extract` | Accepts an image + target language, returns extracted text, translated text, and detected language |

## Run locally

```bash
git clone https://github.com/07adii04/indic-lens-v2-.git
cd indic-lens-v2-
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Add your Google Cloud API key:

```bash
# .env
GOOGLE_VISION_API_KEY=your_key_here
```

Run it:

```bash
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000`

## What I learned building this

This was my first production-style FastAPI project — integrating two external Google Cloud APIs, structuring a backend with proper routers and service layers, handling real-world edge cases (empty OCR results, API permission errors), and connecting a vanilla JS frontend to a Python backend without a framework.

## What's next

- Support for more Indian languages
- Mobile camera capture optimization
- User accounts to save translation history
