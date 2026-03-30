from pyrogram import filters
from pyrogram.types import Message
from anony import app

# Database functions check
try:
    from anony.utils.database import is_autoplay_on, autoplay_on, autoplay_off
except:
    try:
        from ..utils.database import is_autoplay_on, autoplay_on, autoplay_off
    except:
        # Agar function ke naam alag hain (kuch repos mein set_autoplay hota hai)
        is_autoplay_on = None

@app.on_message(filters.command(["autoplay"]) & ~filters.private)
async def autoplay_stat(_, message: Message):
    if is_autoplay_on is None:
        return await message.reply_text("❌ Aapki repo mein autoplay support missing hai.")
    
    if len(message.command) != 2:
        return await message.reply_text("Usage:\n/autoplay [on|off]")
    
    state = message.text.split(None, 1)[1].strip().lower()
    
    try:
        if state == "on":
            await autoplay_on(message.chat.id)
            await message.reply_text("✅ **Autoplay Enabled!**\nSongs khatam hone par bot khud bajayega.")
        elif state == "off":
            await autoplay_off(message.chat.id)
            await message.reply_text("❌ **Autoplay Disabled!**")
        else:
            await message.reply_text("Invalid! Use `/autoplay on` or `/autoplay off`.")
    except Exception as e:
        await message.reply_text(f"⚠️ Database Error: {e}")

