from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from anony import app
import importlib

@app.on_message(filters.command(["autoplay"]) & filters.group)
async def autoplay_command(_, message):
    chat_id = message.chat.id
    
    try:
        # Dynamic import taaki crash na ho
        mongo_module = importlib.import_module("anony.core.mongo")
        # Check if 'mongodb' or 'MongoDB' exists
        db_connection = getattr(mongo_module, "mongodb", getattr(mongo_module, "MongoDB", None))
        
        # Collection ko dictionary style mein call karna (AttributeError fix)
        db = db_connection["autoplay"]
    except Exception:
        return await message.reply_text("❌ Database connection error!")

    # Database se status check karo
    is_active = await db.find_one({"chat_id": chat_id})
    status = is_active.get("autoplay") if is_active else False

    text = "✅ **Autoplay ENABLE hai.**" if status else "❌ **Autoplay DISABLE hai.**"
    btn_text = "Disable 🛠️" if status else "Enable 🚀"
    cb_data = "autoplay_disable" if status else "autoplay_enable"

    await message.reply_text(
        text, 
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(btn_text, callback_data=cb_data)]])
    )

@app.on_callback_query(filters.regex("autoplay_"))
async def autoplay_switch(_, query):
    chat_id = query.message.chat.id
    action = query.data.split("_")[1]
    
    mongo_module = importlib.import_module("anony.core.mongo")
    db_connection = getattr(mongo_module, "mongodb", getattr(mongo_module, "MongoDB", None))
    db = db_connection["autoplay"]

    if action == "enable":
        await db.update_one({"chat_id": chat_id}, {"$set": {"autoplay": True}}, upsert=True)
        await query.answer("Autoplay Shuru! ✅", show_alert=True)
        await query.edit_message_text(
            "🚀 **Autoplay ENABLE ho gaya hai.**", 
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Disable 🛠️", callback_data="autoplay_disable")]])
        )
    else:
        await db.update_one({"chat_id": chat_id}, {"$set": {"autoplay": False}}, upsert=True)
        await query.answer("Autoplay Band! 🛑", show_alert=True)
        await query.edit_message_text(
            "🛑 **Autoplay DISABLE ho gaya hai.**", 
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Enable 🚀", callback_data="autoplay_enable")]])
        )
