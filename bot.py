import logging
import os

from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Load local .env values; deployment environment variables still take precedence.
load_dotenv()

logging.basicConfig(format="%(asctime)s %(levelname)s %(name)s: %(message)s", level=os.getenv("LOG_LEVEL", "INFO"))
log = logging.getLogger("nba-dice-bot")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
WEB_APP_URL = os.getenv("WEB_APP_URL", "").strip()


def game_keyboard():
    if not WEB_APP_URL.startswith("https://"):
        return InlineKeyboardMarkup([[InlineKeyboardButton("Setup required", callback_data="setup_required")]])
    return InlineKeyboardMarkup([[InlineKeyboardButton("🎲 Open NBA DICE", web_app=WebAppInfo(url=WEB_APP_URL))]])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    first_name = user.first_name if user else "there"
    await update.effective_message.reply_text(
        f"🏀 Welcome to NBA DICE, {first_name}!\n\n"
        "Open the game below to choose two numbers and roll six dice.\n"
        "This starter connects Telegram to the existing demo web game. Coins, payments, and multiplayer are still demo-only.",
        reply_markup=game_keyboard(),
    )


async def game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.effective_message.reply_text("Tap below to open NBA DICE.", reply_markup=game_keyboard())


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.effective_message.reply_text(
        "Commands:\n/start — Welcome and open the game\n/game — Open NBA DICE\n/help — Show this help\n\n"
        "The web app must be hosted at a public HTTPS URL. Never share your bot token or commit it to GitHub."
    )


def main() -> None:
    if not BOT_TOKEN:
        raise SystemExit("Missing TELEGRAM_BOT_TOKEN. Copy .env.example to .env and set it.")
    if not WEB_APP_URL.startswith("https://"):
        log.warning("WEB_APP_URL is not HTTPS; Telegram Web Apps require a public HTTPS URL.")
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("game", game))
    application.add_handler(CommandHandler("help", help_command))
    log.info("NBA DICE Telegram bot is running (long polling).")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
