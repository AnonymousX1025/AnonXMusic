from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from anony import app
from anony.core.mongo import mongodb

@app.on_message(filters.command(["autoplay"]) & filters.group)
async def autoplay_command(_, message):
    chat_id = message.chat.id
    # Database se current status check karo
    is_active = await mongodb.find_one({"chat_id": chat_id})
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

# Buttons handle karne ke liye callback function
@app.on_callback_query(filters.regex(paper="autoplay_"))
async def autoplay_switch(_, query):
    chat_id = query.message.chat.id
    action = query.data.split("_")[1]

    if action == "enable":
        await mongodb.update_one({"chat_id": chat_id}, {"$set": {"autoplay": True}}, upsert=True)
        await query.answer("Autoplay Shuru Ho Gaya! ✅", show_alert=True)
        await query.edit_message_text(
            "🚀 **Autoplay ENABLE kar diya gaya hai.**\n\nAb agla gaana apne aap bajega.",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Disable 🛠️", callback_data="autoplay_disable")]])
        )
    else:
        await mongodb.update_one({"chat_id": chat_id}, {"$set": {"autoplay": False}}, upsert=True)
        await query.answer("Autoplay Band Kar Diya! 🛑", show_alert=True)
        await query.edit_message_text(
            "🛑 **Autoplay DISABLE kar diya gaya hai.**",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Enable 🚀", callback_data="autoplay_enable")]])
        )
