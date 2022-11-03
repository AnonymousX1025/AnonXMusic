from datetime import datetime

from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from AnonX import app
from config import OWNER_ID, START_IMG_URL, SUPPORT_HEHE


def content(msg: Message) -> [None, str]:
    text_to_return = msg.text

    if msg.text is None:
        return None
    if " " in text_to_return:
        try:
            return msg.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


@app.on_message(filters.command("bug") & ~filters.private)
async def bug(_, msg: Message):
    if msg.chat.username:
        chat_username = (f"@{msg.chat.username}/`{msg.chat.id}`")
    else:
        chat_username = (f"ᴩʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴩ/`{msg.chat.id}`")

    bugs = content(msg)
    user_id = msg.from_user.id
    mention = "["+msg.from_user.first_name+"](tg://user?id="+str(msg.from_user.id)+")"
    datetimes_fmt = "%d-%m-%Y"
    datetimes = datetime.utcnow().strftime(datetimes_fmt)
    
    bug_report = f"""
**#ʙᴜɢ ʀᴇᴩᴏʀᴛ**

**ʀᴇᴩᴏʀᴛᴇᴅ ʙʏ :** `{mention}`
**ᴜsᴇʀ ɪᴅ :** `{user_id}`
**ᴄʜᴀᴛ :** {chat_username}

**ʙᴜɢ :** {bugs}

**ᴇᴠᴇɴᴛ sᴛᴀᴍᴩ :** {datetimes}"""

    if user_id == OWNER_ID:
        if bugs:
            await msg.reply_text(
                "<b>» ᴀʀᴇ ʏᴏᴜ ᴄᴏᴍᴇᴅʏ ᴍᴇ 🤣, ʏᴏᴜ'ʀᴇ ᴛʜᴇ ᴏᴡɴᴇʀ ᴏғ ᴛʜᴇ ʙᴏᴛ.</b>",
            )
            return
        else:
            await msg.reply_text(
                "ᴄʜᴜᴍᴛɪʏᴀ ᴏᴡɴᴇʀ!"
            )
    elif user_id != OWNER_ID:
        if bugs:
            await msg.reply_text(
                f"<b>ʙᴜɢ ʀᴇᴩᴏʀᴛ : {bugs}</b>\n\n"
                "<b>» ʙᴜɢ sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇᴩᴏʀᴛᴇᴅ ᴀᴛ sᴜᴩᴩᴏʀᴛ ᴄʜᴀᴛ !</b>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "• ᴄʟᴏsᴇ •", callback_data=f"close")
                        ]
                    ]
                )
            )
            await app.send_photo(
                SUPPORT_HEHE,
                photo=config.START_IMG_URL,
                caption=bug_report,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "• ᴠɪᴇᴡ ʙᴜɢ •", url=msg.link)
                        ]
                    ]
                )
            )
        else:
            await msg.reply_text(
                f"<b>» ɴᴏ ʙᴜɢ ᴛᴏ ʀᴇᴩᴏʀᴛ !</b>",
            )
