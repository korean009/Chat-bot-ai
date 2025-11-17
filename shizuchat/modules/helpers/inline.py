from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_GRP, UPDATE_CHNL
from shizuchat import OWNER, shizuchat


START_BOT = [
    [
        InlineKeyboardButton(
            text="✦ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ✦",
            url=f"https://t.me/{shizuchat.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="˹ᴅᴇᴠᴇʟᴏᴘᴇʀ˼", user_id=OWNER),
        InlineKeyboardButton(text="˹ꜰᴏʟʟᴏᴡ ᴍᴇ˼", url=f"https://www.instagram.com/ff_noob_hoon?igsh=MTN5d2NnNjZscnh3"),
    ],
    [
        InlineKeyboardButton(text="« ғᴇᴀᴛᴜʀᴇs »", callback_data="HELP"),
    ],
]


DEV_OP = [
    [
        InlineKeyboardButton(text="˹ᴅᴇᴠᴇʟᴏᴘᴇʀ˼", user_id=OWNER),
        InlineKeyboardButton(text="˹ꜰᴏʟʟᴏᴡ ᴍᴇ˼", url=f"https://www.instagram.com/ff_noob_hoon?igsh=MTN5d2NnNjZscnh3"),
    ],
    [
        InlineKeyboardButton(
            text="✦ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ✦",
            url=f"https://t.me/{shizuchat.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="« ʜᴇʟᴘ »", callback_data="HELP"),
    ],
    [
        # InlineKeyboardButton(text="🏔️ sᴏᴜʀᴄᴇ 🏔️", callback_data="SOURCE"),
        InlineKeyboardButton(text="💌 ᴀʙᴏᴜᴛ 💌", callback_data="ABOUT"),
    ],
]

PNG_BTN = [
    [
        InlineKeyboardButton(
            text="✦ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ✦",
            url=f"https://t.me/{shizuchat.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(
            text="⦿ ᴄʟᴏsᴇ ⦿",
            callback_data="CLOSE",
        ),
    ],
]


NEXT = [
    [
        InlineKeyboardButton(text="⦿ ʙᴀᴄᴋ ⦿", callback_data="BACK"),
        InlineKeyboardButton(text="⦿ ɴᴇxᴛ ⦿", callback_data="ADMIN_READ2"),
    ],
]

BACK = [
    [
        InlineKeyboardButton(text="⦿ ʙᴀᴄᴋ ⦿", callback_data="BACK"),
    ],
]


HELP_BTN = [
        [
        InlineKeyboardButton(text="˹ᴅᴇᴠᴇʟᴏᴘᴇʀ˼", callback_data="OWNER"),
    ],
    [
        InlineKeyboardButton(text="🤖 ᴄʜᴀᴛʙᴏᴛ 🤖", callback_data="CHATBOT_CMD"),
    ],
    [
        InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data="CLOSE"),
    ],
]


CLOSE_BTN = [
    [
        InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data="CLOSE"),
    ],
]


CHATBOT_ON = [
    [
        InlineKeyboardButton(text="ᴇɴᴀʙʟᴇ", callback_data="enable_chatbot"),
        InlineKeyboardButton(text="ᴅɪsᴀʙʟᴇ", callback_data="disable_chatbot"),
    ],
]


MUSIC_BACK_BTN = [
    [
        InlineKeyboardButton(text="sᴏᴏɴ", callback_data=f"soom"),
    ],
]

S_BACK = [
    [
        InlineKeyboardButton(text="⦿ ʙᴀᴄᴋ ⦿", callback_data="SBACK"),
        InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data="CLOSE"),
    ],
]


CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="⦿ ʙᴀᴄᴋ ⦿", callback_data="CHATBOT_BACK"),
        InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data="CLOSE"),
    ],
]


HELP_START = [
    [
        InlineKeyboardButton(text="« ʜᴇʟᴘ »", callback_data="HELP"),
        InlineKeyboardButton(text="🚫 ᴄʟᴏsᴇ 🚫", callback_data="CLOSE"),
    ],
]


HELP_BUTN = [
    [
        InlineKeyboardButton(
            text="« ʜᴇʟᴘ »", url=f"https://t.me/{shizuchat.username}?start=help"
        ),
        InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data="CLOSE"),
    ],
]


ABOUT_BTN = [
    [
        InlineKeyboardButton(text="˹ꜰᴏʟʟᴏᴡ ᴍᴇ˼", url=f"https://www.instagram.com/ff_noob_hoon?igsh=MTN5d2NnNjZscnh3"),
        InlineKeyboardButton(text="« ʜᴇʟᴘ »", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="˹ᴅᴇᴠᴇʟᴏᴘᴇʀ˼", user_id=OWNER),
        #   InlineKeyboardButton(text="🏔️ sᴏᴜʀᴄᴇ 🏔️", callback_data="SOURCE"),
    ],
    [
        InlineKeyboardButton(text="⦿ ʙᴀᴄᴋ ⦿", callback_data="BACK"),
    ],
]
