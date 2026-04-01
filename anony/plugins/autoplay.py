from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from anony import app
import importlib

@app.on_message(filters.command(["autoplay"]) & filters.group)
async def autoplay_command(_, message):
    chat_id = message.chat.id
    
    try:
        # Dynamic load taaki agar error aaye toh bot crash na ho
        mg = importlib.import_module("anony.core.mongo")
        
        # Tere mongo.py ke 'class MongoDB' ko handle karne ke liye
        if hasattr(mg, "mongodb"):
            db = mg.mongodb.db.autoplay
        elif hasattr(mg, "MongoDB"):
            # Agar class instance nahi hai toh class call karke db nikalega
            db = mg.MongoDB().db.autoplay
        else:
            return await message.reply_text("❌ Database connection object nahi mila!")
            
    except Exception as e:
        return await message.reply_text(f"❌ Database Error: {str(e)}")

    is_active = await db.find_one({"chat_id": chat_id})
    status = is_active.get("autoplay") if is_active else False

    text = "✅ **Autoplay is ENABLED**" if status else "❌ **Autoplay is DISABLED**"
    btn = "Disable 🛠️" if status else "Enable 🚀"
    cb = "autoplay_disable" if status else "autoplay_enable"

    await message.reply_text(text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(btn, callback_data=cb)]]))

@app.on_callback_query(filters.regex("autoplay_"))
async def autoplay_switch(_, query):
    chat_id = query.message.chat.id
    action = query.data.split("_")[1]
    
    # Same logic for callback
    mg = importlib.import_module("anony.core.mongo")
    db = mg.mongodb.db.autoplay if hasattr(mg, "mongodb") else mg.MongoDB().db.autoplay

    if action == "enable":
        await db.update_one({"chat_id": chat_id}, {"$set": {"autoplay": True}}, upsert=True)
        await query.answer("Enabled! ✅")
        await query.edit_message_text("🚀 **Autoplay ON ho gaya!**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Disable 🛠️", callback_data="autoplay_disable")]]))
    else:
        await db.update_one({"chat_id": chat_id}, {"$set": {"autoplay": False}}, upsert=True)
        await query.answer("Disabled! 🛑")
        await query.edit_message_text("🛑 **Autoplay OFF ho gaya!**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Enable 🚀", callback_data="autoplay_enable")]]))
