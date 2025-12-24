from pyrogram import filters, types
from pyrogram.enums import ChatMemberStatus

from anony import app
from anony.helpers import admin_check

# تخزين المكتومين (ذاكرة مؤقتة)
muted = {}


def is_admin(member: types.ChatMember) -> bool:
    return member.status in (
        ChatMemberStatus.ADMINISTRATOR,
        ChatMemberStatus.OWNER,
    )


@app.on_message(filters.command("كتم") & filters.group & filters.reply)
async def mute_user(_, message: types.Message):
    chat_id = message.chat.id
    from_user = message.from_user
    target = message.reply_to_message.from_user

    member = await app.get_chat_member(chat_id, from_user.id)
    target_member = await app.get_chat_member(chat_id, target.id)

    if not is_admin(member):
        return await message.reply("↢ يجب أن تكون مشرفًا لاستخدام هذا الأمر.")

    if is_admin(target_member):
        return await message.reply("↢ لا يمكنك كتم مشرف أو مالك.")

    muted.setdefault(chat_id, [])

    if target.id in muted[chat_id]:
        return await message.reply("↢ هذا المستخدم مكتوم بالفعل.")

    muted[chat_id].append(target.id)

    await message.reply(
        f"↢ تم كتم المستخدم {target.first_name} بواسطة {from_user.first_name}"
    )


@app.on_message(filters.command("الغاء الكتم") & filters.group & filters.reply)
async def unmute_user(_, message: types.Message):
    chat_id = message.chat.id
    from_user = message.from_user
    target = message.reply_to_message.from_user

    member = await app.get_chat_member(chat_id, from_user.id)

    if not is_admin(member):
        return await message.reply("↢ يجب أن تكون مشرفًا لاستخدام هذا الأمر.")

    if chat_id not in muted or target.id not in muted[chat_id]:
        return await message.reply("↢ هذا المستخدم غير مكتوم.")

    muted[chat_id].remove(target.id)

    await message.reply(
        f"↢ تم إلغاء كتم المستخدم {target.first_name} بواسطة {from_user.first_name}"
    )


@app.on_message(filters.command("المكتومين") & filters.group)
async def muted_list(_, message: types.Message):
    chat_id = message.chat.id
    member = await app.get_chat_member(chat_id, message.from_user.id)

    if not is_admin(member):
        return await message.reply("↢ يجب أن تكون مشرفًا لاستخدام هذا الأمر.")

    if chat_id not in muted or not muted[chat_id]:
        return await message.reply("↢ لا يوجد أي مكتومين.")

    text = "↢ قائمة المكتومين:\n\n"
    for user_id in muted[chat_id]:
        text += f"↢ [مستخدم](tg://user?id={user_id})\n"

    await message.reply(text)


@app.on_message(filters.command("مسح المكتومين") & filters.group)
async def clear_muted(_, message: types.Message):
    chat_id = message.chat.id
    member = await app.get_chat_member(chat_id, message.from_user.id)

    if not is_admin(member):
        return await message.reply("↢ يجب أن تكون مشرفًا لاستخدام هذا الأمر.")

    muted.pop(chat_id, None)

    await message.reply("↢ تم مسح جميع المكتومين بنجاح.")


@app.on_message(filters.group & filters.text, group=999)
async def delete_muted_messages(_, message: types.Message):
    chat_id = message.chat.id

    if chat_id not in muted:
        return

    if message.from_user and message.from_user.id in muted[chat_id]:
        try:
            await message.delete()
        except:
            pass
