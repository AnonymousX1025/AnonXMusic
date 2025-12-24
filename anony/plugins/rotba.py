from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus
from anony import app


@app.on_message(filters.command("رتبتي"))
async def rotba(_: Client, message: Message):
    user_id = message.from_user.id
    member = await app.get_chat_member(message.chat.id, user_id)

    if member.status == ChatMemberStatus.MEMBER:
        await message.reply("⌯ رتبتك هي العضو 🦅.", reply_to_message_id=message.id)

    elif member.status == ChatMemberStatus.ADMINISTRATOR:
        await message.reply("↢ رتبتك هي الادمن 🍪.", reply_to_message_id=message.id)

    elif member.status == ChatMemberStatus.OWNER:
        await message.reply("↢ رتبتك هي المالك 🩷.", reply_to_message_id=message.id)
