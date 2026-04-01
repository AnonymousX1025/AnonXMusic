from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from anony import app
from anony.core.mongo import mongodb

@app.on_message(filters.command(["autoplay"]) & filters.group)
async def autoplay_command(_, message):
    chat_id = message.chat.id
    # Collection based call to avoid Attribute errors
    is_active = await mongodb.autoplay.find_one({"chat_id": chat_id})
    status = is_active.get("autoplay") if is_active else False

    if status:
        text = "✅ **Autoplay is currently ENABLED.**"
        button_text = "Disable Autoplay 🛠️"
        callback_data = "autoplay_disable"
    else:
        text = "❌ **Autoplay is currently DISABLED.**"
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
        await query.answer("Autoplay Enabled! ✅", show_alert=True)
        await query.edit_message_text(
            "🚀 **Autoplay has been ENABLED.**",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Disable 🛠️", callback_data="autoplay_disable")]])
        )
    else:
        await mongodb.autoplay.update_one({"chat_id": chat_id}, {"$set": {"autoplay": False}}, upsert=True)
        await query.answer("Autoplay Disabled! 🛑", show_alert=True)
        await query.edit_message_text(
            "🛑 **Autoplay has been DISABLED.**",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Enable 🚀", callback_data="autoplay_enable")]])
        )
