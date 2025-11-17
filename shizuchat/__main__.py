import sys
import asyncio
import importlib
from flask import Flask
import threading
from pyrogram import idle
from pyrogram.types import BotCommand
from config import OWNER_ID
from shizuchat import LOGGER, shizuchat
from shizuchat.modules import ALL_MODULES


async def anony_boot():
    try:
        await shizuchat.start()
    except Exception as ex:
        LOGGER.error(ex)
        sys.exit(1)

    # Import all modules
    for all_module in ALL_MODULES:
        importlib.import_module("shizuchat.modules." + all_module)
        LOGGER.info(f"Successfully Imported: {all_module}")

    # Set bot commands
    try:
        await shizuchat.set_bot_commands(
            commands=[
                BotCommand("start", "Start the bot"),
                BotCommand("help", "Help menu"),
                BotCommand("ping", "Bot status"),
                BotCommand("shipping", "Couples of the day"),
                BotCommand("rankings", "User message leaderboard"),
            ]
        )
        LOGGER.info("Bot Commands Set Successfully.")
    except Exception as ex:
        LOGGER.error(f"Failed to set bot commands: {ex}")

    LOGGER.info(f"@{shizuchat.username} Started.")

    try:
        await shizuchat.send_message(int(OWNER_ID), f"{shizuchat.mention} has started")
    except Exception:
        LOGGER.info("Start the bot from owner ID first.")

    await idle()


# Flask server for health check
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running"


def run_flask():
    app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    # Start Flask in another thread
    threading.Thread(target=run_flask).start()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(anony_boot())

    LOGGER.info("Stopping shizuchat bot...")
