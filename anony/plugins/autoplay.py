from pyrogram import filters
from anony import app, db

@app.on_message(filters.command(["autoplay"]))
async def autoplay_mnt(_, message):
    usage = "Usage:\n\n/autoplay [enable|disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "enable":
        await db.autoplay_on(message.chat.id)
        await message.reply_text("✅ Autoplay Enabled! Ab queue khatam hone par gaane khud chalenge.")
    elif state == "disable":
        await db.autoplay_off(message.chat.id)
        await message.reply_text("❌ Autoplay Disabled!")
    else:
        await message.reply_text(usage)
