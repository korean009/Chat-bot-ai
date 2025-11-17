from shizuchat import shizuchat
from pyrogram import filters
from pyrogram.enums import ChatAction
from pyrogram.types import InlineKeyboardMarkup
import asyncio, time,requests
from config import *
from shizuchat.modules.helpers.inline import DEV_OP
from config import OWNER_USERNAME
from BadAPI import api

x=None
@shizuchat.on_cmd(["bard"])
async def bard_chat(bot, message):
    global x
    if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n`/bard write shorts notes on human eyes`")
    else:
        a = message.text.split(' ', 1)[1]
    
    try:
        response =api.gemini(a)
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        x=response["results"]
        
        await message.reply_text(f"{x}\n\n🌸  ᴍᴀᴅᴇ ᴡɪᴛʜ ❣️ ʙʏ [ʙᴀᴅ ᴍᴜɴᴅᴀ](https://t.me/{OWNER_USERNAME}) ||",reply_markup=InlineKeyboardMarkup(DEV_OP),quote=True)  

    except requests.exceptions.RequestException as e:
        pass
        

# Blackbox

from shizuchat import shizuchat
from pyrogram import filters
import asyncio, time,requests
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.enums import ChatAction,ParseMode
from config import *
from BadAPI import api
from config import OWNER_USERNAME
from shizuchat.modules.helpers.inline import DEV_OP

x=None
#blackbox
@shizuchat.on_cmd(["blackbox"])
async def blackbox_chat(bot, message):
    if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n`/blackbox write simple flask app code`")
    else:
        a = message.text.split(' ', 1)[1]
    try:
        response = api.blackbox(a)
        
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        x=response["results"]
        
        await message.reply_text(f"{x}\n\n🌸  ᴍᴀᴅᴇ ᴡɪᴛʜ ❣️ ʙʏ [ʙᴀᴅ ᴍᴜɴᴅᴀ](https://t.me/{OWNER_USERNAME}) ||",reply_markup=InlineKeyboardMarkup(DEV_OP),quote=True,disable_web_page_preview =True,parse_mode=ParseMode.MARKDOWN)  
        
            
    except requests.exceptions.RequestException as e:
        pass
        
