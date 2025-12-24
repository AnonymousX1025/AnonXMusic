from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import ChatPrivileges
from anony import app


ANTI_PURGE = []


# ================== Utils ==================
async def is_owner(client, chat_id, user_id):
    member = await client.get_chat_member(chat_id, user_id)
    return member.status == ChatMemberStatus.OWNER


# ================== Anti Purge ==================
@app.on_chat_member_updated()
async def anti_purge(client, upd):
    chat_id = upd.chat.id

    if chat_id not in ANTI_PURGE:
        return

    if upd.new_chat_member.status != ChatMemberStatus.BANNED:
        return

    kicked_user = upd.new_chat_member.user
    by = upd.new_chat_member.restricted_by

    if not by or by.is_self:
        return

    try:
        member = await client.get_chat_member(chat_id, by.id)
        if member.status in [ChatMemberStatus.ADMINISTRATOR]:
            await client.demote_chat_member(chat_id, by.id)
            await client.send_message(
                chat_id,
                f"منع التصفية التلقائي 🛡️\n\n"
                f"↢ الأدمن [{by.first_name}](tg://user?id={by.id}) "
                f"حاول طرد [{kicked_user.first_name}](tg://user?id={kicked_user.id})\n"
                f"↢ تم تنزيله من الإشراف"
            )
    except:
        pass


# ================== Enable / Disable ==================
@app.on_message(filters.command("تفعيل الحماية") & filters.group)
async def enable_anti(client, message):
    if not await is_owner(client, message.chat.id, message.from_user.id):
        return await message.reply("↢ هذا الأمر للمالك فقط")

    if message.chat.id in ANTI_PURGE:
        return await message.reply("↢ الحماية مفعلة بالفعل")

    ANTI_PURGE.append(message.chat.id)
    await message.reply("↢ تم تفعيل حماية التصفية")


@app.on_message(filters.command("تعطيل الحماية") & filters.group)
async def disable_anti(client, message):
    if not await is_owner(client, message.chat.id, message.from_user.id):
        return await message.reply("↢ هذا الأمر للمالك فقط")

    if message.chat.id not in ANTI_PURGE:
        return await message.reply("↢ الحماية معطلة بالفعل")

    ANTI_PURGE.remove(message.chat.id)
    await message.reply("↢ تم تعطيل حماية التصفية")


# ================== Promote ==================
@app.on_message(filters.command("رفع مشرف") & filters.group & filters.reply)
async def promote_admin(client, message):
    if not await is_owner(client, message.chat.id, message.from_user.id):
        return await message.reply("↢ هذا الأمر للمالك فقط")

    user_id = message.reply_to_message.from_user.id

    privileges = ChatPrivileges(
        can_manage_chat=True,
        can_delete_messages=True,
        can_restrict_members=True,
        can_invite_users=True
    )

    await client.promote_chat_member(
        message.chat.id,
        user_id,
        privileges
    )

    await message.reply(f"↢ تم رفع {message.reply_to_message.from_user.first_name} مشرف")
