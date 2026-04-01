from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from anony import app
import importlib

@app.on_message(filters.command(["autoplay"]) & filters.group)
async def autoplay_command(_, message):
    chat_id = message.chat.id
    
    # DATABASE AUTO-DETECT (Tujhe kuch change nahi karna padega)
    try:
        mongo_module = importlib.import_module("anony.core.mongo")
        # Ye line 'mongodb' aur 'MongoDB' dono ko check karegi
        db = getattr(mongo_module, "mongodb", getattr(mongo_module, "MongoDB", None))
    except Exception:
        return await message.reply_text("❌ Database file 'anony/core/mongo.py' nahi mili!")

    if not db:
        return await message.reply_text("❌ Database connection object nahi mila!")

    # Check status from MongoDB collection 'autoplay'
    is_active = await db.autoplay.find_one({"chat_id": chat_id})
    status = is_active.get("autoplay") if is_active else False

    text = "✅ **Autoplay ENABLE hai.**" if status else "❌ **Autoplay DISABLE hai.**"
    btn_text = "Disable 🛠️" if status else "Enable 🚀"
    cb_data = "autoplay_disable" if status else "autoplay_enable"

    await message.reply_text(text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(btn_text, callback_data=cb_data)]]))

@app.on_callback_query(filters.regex("autoplay_"))
async def autoplay_switch(_, query):
    chat_id = query.message.chat.id
    action = query.data.split("_")[1]
    
    mongo_module = importlib.import_module("anony.core.mongo")
    db = getattr(mongo_module, "mongodb", getattr(mongo_module, "MongoDB", None))

    if action == "enable":
        await db.autoplay.update_one({"chat_id": chat_id}, {"$set": {"autoplay": True}}, upsert=True)
        await query.answer("Enabled! ✅")
        await query.edit_message_text("🚀 **Autoplay ON ho gaya!**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Disable 🛠️", callback_data="autoplay_disable")]]))
    else:
        await db.autoplay.update_one({"chat_id": chat_id}, {"$set": {"autoplay": False}}, upsert=True)
        await query.answer("Disabled! 🛑")
        await query.edit_message_text("🛑 **Autoplay OFF ho gaya!**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Enable 🚀", callback_data="autoplay_enable")]]))
