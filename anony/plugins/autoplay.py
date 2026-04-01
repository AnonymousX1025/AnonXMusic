from pyrogram import filters
from anony import app, userbot

# Database Functions (Isi file mein add kar diye)
async def is_autoplay_mode(chat_id: int) -> bool:
    user = await userbot.find_one({"chat_id": chat_id})
    if not user:
        return False
    return user.get("autoplay", False)

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
    if len(message.command) != 2:
        return await message.reply_text("Usage:\n\n/autoplay [enable|disable]")
    
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "enable":
        await autoplay_on(message.chat.id)
        await message.reply_text("✅ Autoplay Enabled! Ab queue khatam hone par gaane apne aap chalenge.")
    elif state == "disable":
        await autoplay_off(message.chat.id)
        await message.reply_text("❌ Autoplay Disabled!")
    else:
        await message.reply_text("Usage:\n\n/autoplay [enable|disable]")
