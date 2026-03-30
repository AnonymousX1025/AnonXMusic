from pyrogram import filters
from pyrogram.types import Message
from anony import app

# Sabse safe tarika database import karne ka
try:
    from anony.utils.database import is_autoplay_on, autoplay_on, autoplay_off
except:
    try:
        from utils.database import is_autoplay_on, autoplay_on, autoplay_off
    except:
        try:
            from ..utils.database import is_autoplay_on, autoplay_on, autoplay_off
        except:
            is_autoplay_on = None

@app.on_message(filters.command(["autoplay"]) & ~filters.private)
async def autoplay_stat(_, message: Message):
    if is_autoplay_on is None:
        return await message.reply_text("❌ Database structure not found in your repo.")
    
    if len(message.command) != 2:
        return await message.reply_text("Usage:\n/autoplay [on|off]")
    
    state = message.text.split(None, 1)[1].strip().lower()
    
    if state == "on":
        await autoplay_on(message.chat.id)
        await message.reply_text("✅ **Autoplay Enabled!**\nAb gaana khatam hone par bot agla song khud bajayega.")
    elif state == "off":
        await autoplay_off(message.chat.id)
        await message.reply_text("❌ **Autoplay Disabled!**")
    else:
        await message.reply_text("Invalid! Use `/autoplay on` or `/autoplay off`.")
