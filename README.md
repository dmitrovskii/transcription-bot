# Telegram Transcription Bot


> An asynchronous, Telegram bot designed to instantly transcribe voice messages into text. Powered by the Groq API (using the Whisper model) and built with Aiogram 3, it offers highly accurate speech-to-text conversion with smart language auto-detection, making it a simply tool for processing voice message on the go.

---

## ✨ Features

* 🎙️ **High-Speed Transcription:** Instantly converts voice messages to text using the advanced `whisper-large-v3-turbo` model via Groq API.
* 🌍 **Smart Language Detection:** Supports explicit language selection (English, Ukrainian) via inline keyboards, or an "Auto-detect" mode for mixed speech to prevent AI hallucinations.
* ⚡ **Fully Asynchronous:** Built with `aiogram` and `aiosqlite` for non-blocking database operations and high concurrency.
* 🐳 **Docker Ready:** Fast, reliable, and isolated deployment using Docker and Docker Compose (includes persistent volume for the database).
* ⚙️ **Highly Configurable:** No hardcoded constants. Easily switch AI models and API endpoints using `.env` variables.
* 📝 **Text Summarization:** Integrated LLM support to generate quick summaries from long transcriptions.
---

## 🛠 Tech Stack

* **Language:** Python 3.14
* **Framework:** Aiogram 3.30
* **Database:** SQLite (`aiosqlite`)
* **AI API:** Groq (OpenAI-compatible SDK)
* **DevOps:** Docker & Docker Compose
---

## 📦 Prerequisites

Before you begin, make sure you have installed:
* [Git](https://git-scm.com/)
* [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/)

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `BOT_TOKEN` | Telegram Bot API token obtained from @BotFather | - |
| `GROQ_TOKEN` | API key from Groq Cloud | - |
| `GROQ_BASE_URL` | Endpoint for the OpenAI-compatible client | `https://api.groq.com/openai/v1` |
| `STT_MODEL` | Speech-to-Text model for voice transcription | `whisper-large-v3-turbo` |
| `LLM_MODEL` | Text model for generating summaries | `llama-3.1-8b-instant` |
---

## Quick Start

### 1. Clone the repo
``` bash
git clone https://github.com/dmitrovskii/transcription-bot
cd transcription-bot
```

### Setup environment variables
Copy the example environment file and specify your API tokens:
``` bash
cp .env.example .env
```

### Running via Docker Compose
Build the image and start the container in the background:
``` bash 
docker compose up -d --build 
```
The bot is now running! Open Telegram, find your bot, and send `/start` to begin.

---

### 👨‍💻 Author & License
* **Author:** @dmitrovskii
* **License:** Mit Licenses