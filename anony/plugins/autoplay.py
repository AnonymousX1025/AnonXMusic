from pyrogram import filters
from pyrogram.types import Message
from anony import app
# Direct import from the root's metadata
from ..utils.database import is_autoplay_on, autoplay_on, autoplay_off

@app.on_message(filters.command(["autoplay"]) & ~filters.private)
async def autoplay_stat(_, message: Message):
    if len(message.command) != 2:
        return await message.reply_text("Usage:\n/autoplay [on|off]")
    
    state = message.text.split(None, 1)[1].strip().lower()
    
    if state == "on":
        await autoplay_on(message.chat.id)
        await message.reply_text("✅ **Autoplay Enabled!**\nAb gaana khatam hone par bot khud bajayega.")
    elif state == "off":
        await autoplay_off(message.chat.id)
        await message.reply_text("❌ **Autoplay Disabled!**")
    else:
        await message.reply_text("Invalid! Use `/autoplay on` or `/autoplay off`.")

