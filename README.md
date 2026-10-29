# NBA DICE — Telegram Bot Starter

A small Telegram bot that opens a browser-based NBA DICE demo.

## Repository contents

- `bot.py` — Telegram bot with `/start`, `/game`, and `/help`.
- `server.py` — Flask web server and `/health` endpoint.
- `static/index.html` — lightweight playable dice-game demo.
- `requirements.txt` — Python dependencies.
- `Dockerfile` and `Procfile` — deployment helpers.
- `.env.example` — environment variable template.

## Configure

1. Create a bot with Telegram's `@BotFather` and copy its token.
2. Copy `.env.example` to `.env`.
3. Set `TELEGRAM_BOT_TOKEN` to your bot token.
4. Set `WEB_APP_URL` to the public HTTPS URL where this web app is hosted.
5. Install dependencies: `pip install -r requirements.txt`.

Run the web app with `python server.py` and the Telegram bot with `python bot.py` in separate processes. The Telegram Web App button requires a publicly reachable HTTPS URL.

## Important demo limitations

The included frontend is a lightweight demo. Wallet coins and dice rolls are simulated in the browser; they are not persistent and do not sync across users. There is no real payment processing or database-backed multiplayer. Do not use it for real-money play or promise real winnings.

Before production, add persistent storage, server-side game logic, Telegram Web App `initData` signature validation, secure authorization, logging, tests, and a payment flow reviewed for applicable laws. Keep your real bot token in deployment secrets and never commit it to GitHub.
