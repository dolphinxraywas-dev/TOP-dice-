# NBA DICE Telegram Bot Starter

Starter project for running the NBA DICE demo as a Telegram bot with a web app frontend.

## Files
- `bot.py` — Telegram bot commands (`/start`, `/game`, `/help`).
- `server.py` — Flask server for the web app and `/health` endpoint.
- `static/index.html` — NBA DICE demo interface.
- `requirements.txt` — Python dependencies.
- `Dockerfile` and `Procfile` — deployment helpers.
- `.env.example` — environment variable template.

## Setup
1. Create a Telegram bot with BotFather and copy its token.
2. Copy `.env.example` to `.env` and set `TELEGRAM_BOT_TOKEN`.
3. Set `WEB_APP_URL` to the public HTTPS URL serving the web app.
4. Install dependencies with `pip install -r requirements.txt`.
5. Run the web server with `python server.py` and the bot worker with `python bot.py` in separate processes.

## Important
This is a demo starter, not a production-ready real-money game. The current browser demo uses local state and simulated coins. Before real users, add a backend database, server-side game logic, Telegram Web App `initData` validation, proper authentication, and a compliant payment flow. Never commit real bot tokens or secrets.