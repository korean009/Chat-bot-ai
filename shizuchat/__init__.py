# ============================
# EVENT LOOP FIX (BEFORE UVLOOP)
# ============================
import asyncio

try:
    asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

# Install uvloop AFTER loop creation
import uvloop
uvloop.install()

# ============================
# NORMAL IMPORTS
# ============================
import logging
import time
import pytz
from pymongo import MongoClient
from Abg import patch
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram import Client
from pyrogram.enums import ParseMode
import config

# ============================
# LOGGING
# ============================
logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

logging.getLogger("pyrogram").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

# ============================
# DATABASE
# ============================
mongodb = MongoCli(config.MONGO_URL)
db = mongodb.Anonymous
mongo = MongoClient(config.MONGO_URL)

# ============================
# SCHEDULER
# ============================
TIME_ZONE = pytz.timezone(config.TIME_ZONE)
scheduler = AsyncIOScheduler(timezone=TIME_ZONE)

# ============================
# BOT CLASS
# ============================
class shizuchat(Client):
    def __init__(self):
        super().__init__(
            name="shizuchat",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            lang_code="en",
            parse_mode=ParseMode.DEFAULT,
            in_memory=True,
        )

    async def start(self):
        await super().start()

        self.id = self.me.id
        self.name = f"{self.me.first_name} {self.me.last_name or ''}"
        self.username = self.me.username
        self.mention = self.me.mention

    async def stop(self):
        await super().stop()


shizuchat = shizuchat()
