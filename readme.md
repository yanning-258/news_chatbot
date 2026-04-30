# News Chatbot

A personal AI-powered news assistant that fetches headlines, lets you pick what to read, and delivers concise summaries — with a weekly digest built from your reading history.

---

## Roadmap

### Stage 1 — CLI News Chatbot *(current focus)*

A daily terminal tool for staying on top of financial and general news without the noise.

**Flow:**
1. App fetches today's top headlines for your tracked topics (e.g. NVDA, AAPL, macro)
2. You pick which articles to read
3. AI summarises the selected articles in plain English (finance-professor tone)
4. Summary is saved to MongoDB for later
5. At the end of each week, a weekly digest is generated from the saved summaries

**Tech stack:**
- Python (CLI)
- [NewsAPI](https://newsapi.org) — headline fetching
- [DeepSeek](https://deepseek.com) — summarisation via OpenAI-compatible SDK
- MongoDB — document store for daily summaries and weekly digests

**Planned project structure:**
```
news_agent/
├── main.py           # CLI entrypoint — orchestrates the daily flow
├── news.py           # NewsAPI fetching and parsing
├── chat.py           # LLM wrapper (DeepSeek)
├── db.py             # MongoDB read/write (summaries, digests)
├── digest.py         # Weekly digest generation logic
├── .env              # API keys (never committed)
├── .gitignore
├── requirements.txt
└── readme.md
```

**Environment variables (`.env`):**
```
DEEPSEEK_API_KEY=
NEWS_API_KEY=
MONGODB_URI=
```

---

### Stage 2 — Web App *(future)*

Wrap the Stage 1 logic into a web interface and ship it to production.

**Planned features:**
- Topic/ticker management UI
- Daily summary feed (web view of what the CLI produces)
- Weekly digest page
- User authentication (if multi-user)

**Likely stack:**
- Backend: FastAPI (Python, reuses Stage 1 logic)
- Frontend: React or simple server-rendered templates
- Hosting: TBD (Railway / Render / Fly.io)

---

## Getting Started (Stage 1)

```bash
# Clone and set up environment
git clone https://github.com/yanning-258/news_chatbot.git
cd news_chatbot
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Add your API keys
cp .env.example .env
# Edit .env with your keys

# Run
python main.py
```

---

## Status

| Feature | Status |
|---|---|
| Fetch headlines from NewsAPI | Done |
| CLI article picker | In progress |
| AI summarisation | In progress |
| MongoDB persistence | Planned |
| Weekly digest | Planned |
| Web app | Planned |
