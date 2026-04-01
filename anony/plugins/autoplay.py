from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from anony import app
# Import fix: Hum poora module import kar rahe hain taaki crash na ho
from anony.core import mongo 

@app.on_message(filters.command(["autoplay"]) & filters.group)
async def autoplay_command(_, message):
    chat_id = message.chat.id
    # Yahan hum check kar rahe hain ki 'mongodb' hai ya 'MongoDB'
    db = getattr(mongo, "mongodb", getattr(mongo, "MongoDB", None))
    
    if not db:
        return await message.reply_text("Database connection nahi mil raha!")

    is_active = await db.autoplay.find_one({"chat_id": chat_id})
    status = is_active.get("autoplay") if is_active else False

    text = "✅ **Autoplay ENABLE hai.**" if status else "❌ **Autoplay DISABLE hai.**"
    button_text = "Disable 🛠️" if status else "Enable 🚀"
    callback_data = "autoplay_disable" if status else "autoplay_enable"

    key = InlineKeyboardMarkup([[InlineKeyboardButton(button_text, callback_data=callback_data)]])
    await message.reply_text(text, reply_markup=key)

@app.on_callback_query(filters.regex("autoplay_"))
async def autoplay_switch(_, query):
    chat_id = query.message.chat.id
    action = query.data.split("_")[1]
    db = getattr(mongo, "mongodb", getattr(mongo, "MongoDB", None))

    if action == "enable":
        await db.autoplay.update_one({"chat_id": chat_id}, {"$set": {"autoplay": True}}, upsert=True)
        await query.answer("Enabled! ✅")
        await query.edit_message_text("🚀 Autoplay ON ho gaya!", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Disable 🛠️", callback_data="autoplay_disable")]]))
    else:
        await db.autoplay.update_one({"chat_id": chat_id}, {"$set": {"autoplay": False}}, upsert=True)
        await query.answer("Disabled! 🛑")
        await query.edit_message_text("🛑 Autoplay OFF ho gaya!", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Enable 🚀", callback_data="autoplay_enable")]]))
