from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from anony import app
# Tere code ke mutabik mongodb object ko import kar rahe hain
from anony.core.mongo import mongodb

@app.on_message(filters.command(["autoplay"]) & filters.group)
async def autoplay_command(_, message):
    chat_id = message.chat.id
    
    # Tere MongoDB class mein 'self.db' use ho raha hai, isliye hum 'mongodb.db' call karenge
    # Yeh 'autoplay' collection ko access karega
    db = mongodb.db.autoplay 

    # Status check karo
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
    
    db = mongodb.db.autoplay

    if action == "enable":
        await db.update_one({"chat_id": chat_id}, {"$set": {"autoplay": True}}, upsert=True)
        await query.answer("Autoplay ON! ✅", show_alert=True)
        await query.edit_message_text(
            "🚀 **Autoplay ON ho gaya!**", 
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Disable 🛠️", callback_data="autoplay_disable")]])
        )
    else:
        await db.update_one({"chat_id": chat_id}, {"$set": {"autoplay": False}}, upsert=True)
        await query.answer("Autoplay OFF! 🛑", show_alert=True)
        await query.edit_message_text(
            "🛑 **Autoplay OFF ho gaya!**", 
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Enable 🚀", callback_data="autoplay_enable")]])
        )
