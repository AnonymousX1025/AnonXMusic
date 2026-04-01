from pyrogram import filters
from config import BANNED_USERS
from anony import app
from anony.core.call import Anony
from anony.utils.database import is_autoplay_mode, autoplay_on, autoplay_off

@app.on_message(filters.command(["autoplay"]) & ~BANNED_USERS)
async def autoplay_mnt(_, message):
    usage = "Usage:\n\n/autoplay [enable|disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "enable":
        await autoplay_on(message.chat.id)
        await message.reply_text("✅ Autoplay Enabled!")
    elif state == "disable":
        await autoplay_off(message.chat.id)
        await message.reply_text("❌ Autoplay Disabled!")
    else:
        await message.reply_text(usage)
