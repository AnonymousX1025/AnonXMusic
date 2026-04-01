from pyrogram import filters
from anony import app, userbot

# Database simple functions
async def autoplay_on(chat_id: int):
    return await userbot.update_one(
        {"chat_id": chat_id}, {"$set": {"autoplay": True}}, upsert=True
    )

async def autoplay_off(chat_id: int):
    return await userbot.update_one(
        {"chat_id": chat_id}, {"$set": {"autoplay": False}}, upsert=True
    )

@app.on_message(filters.command(["autoplay"]))
async def autoplay_mnt(_, message):
    if len(message.command) < 2:
        return await message.reply_text("Usage:\n\n/autoplay [on|off]\n/autoplay [enable|disable]")
    
    state = message.text.split(None, 1)[1].strip().lower()
    
    if state in ["enable", "on"]:
        await autoplay_on(message.chat.id)
        await message.reply_text("✅ **Autoplay ON ho gaya hai!** Ab queue khatam hote hi naya gaana bajega.")
    elif state in ["disable", "off"]:
        await autoplay_off(message.chat.id)
        await message.reply_text("❌ **Autoplay OFF ho gaya hai.**")
    else:
        await message.reply_text("Bhai sahi se likho: `/autoplay on` ya `/autoplay off`")
