from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from anony import app
from anony.core.mongo import mongodb # Wapas small 'm' use kar rahe hain connection ke liye

@app.on_message(filters.command(["autoplay"]) & filters.group)
async def autoplay_command(_, message):
    chat_id = message.chat.id
    # FIX: mongodb.autoplay collection ko call kar rahe hain
    is_active = await mongodb.autoplay.find_one({"chat_id": chat_id})
    status = is_active.get("autoplay") if is_active else False

    if status:
        text = "✅ **Autoplay abhi ENABLE hai.**\n\nKya aap ise band karna chahte hain?"
        button_text = "Disable Autoplay 🛠️"
        callback_data = "autoplay_disable"
    else:
        text = "❌ **Autoplay abhi DISABLE hai.**\n\nKya aap ise shuru karna chahte hain?"
        button_text = "Enable Autoplay 🚀"
        callback_data = "autoplay_enable"

    key = InlineKeyboardMarkup(
        [[InlineKeyboardButton(text=button_text, callback_data=callback_data)]]
    )
    await message.reply_text(text, reply_markup=key)

@app.on_callback_query(filters.regex("autoplay_"))
async def autoplay_switch(_, query):
    chat_id = query.message.chat.id
    action = query.data.split("_")[1]

    if action == "enable":
        await mongodb.autoplay.update_one({"chat_id": chat_id}, {"$set": {"autoplay": True}}, upsert=True)
        await query.answer("Autoplay Shuru! ✅", show_alert=True)
        await query.edit_message_text(
            "🚀 **Autoplay ENABLE kar diya gaya hai.**",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Disable 🛠️", callback_data="autoplay_disable")]])
        )
    else:
        await mongodb.autoplay.update_one({"chat_id": chat_id}, {"$set": {"autoplay": False}}, upsert=True)
        await query.answer("Autoplay Band! 🛑", show_alert=True)
        await query.edit_message_text(
            "🛑 **Autoplay DISABLE kar diya gaya hai.**",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Enable 🚀", callback_data="autoplay_enable")]])
        )
