import random
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus
from anony import app


# ================== Storage ==================
ID_DISABLED = []
BEAUTY_DISABLED = []
EDIT_ENABLED = []


# ================== Utils ==================
async def is_admin(client: Client, message: Message) -> bool:
    member = await client.get_chat_member(message.chat.id, message.from_user.id)
    return member.status in (
        ChatMemberStatus.ADMINISTRATOR,
        ChatMemberStatus.OWNER
    )


# ================== ID Lock ==================
@app.on_message(filters.command(["قفل الايدي", "تعطيل الايدي"]) & filters.group)
async def id_lock(client: Client, message: Message):
    if not await is_admin(client, message):
        return await message.reply("↢ هذا الأمر للأدمن فقط")

    if message.chat.id in ID_DISABLED:
        return await message.reply("↢ الايدي معطل بالفعل")

    ID_DISABLED.append(message.chat.id)
    await message.reply("تم تعطيل الايدي بنجاح")


@app.on_message(filters.command(["فتح الايدي", "تفعيل الايدي"]) & filters.group)
async def id_unlock(client: Client, message: Message):
    if not await is_admin(client, message):
        return await message.reply("↢ هذا الأمر للأدمن فقط")

    if message.chat.id not in ID_DISABLED:
        return await message.reply("↢ الايدي مفعل بالفعل")

    ID_DISABLED.remove(message.chat.id)
    await message.reply("تم تفعيل الايدي بنجاح")


# ================== ID Command ==================
@app.on_message(filters.command(["ايدي", "id", "ا"]) & filters.group)
async def show_id(client: Client, message: Message):
    if message.chat.id in ID_DISABLED:
        return

    user = message.from_user
    photo = None

    if user.photo:
        photo = await client.download_media(user.photo.big_file_id)

    text = (
        f"⌯ الاسم : {user.mention}\n"
        f"⌯ اليوزر : @{user.username}\n"
        f"⌯ الايدي : `{user.id}`\n"
        f"⌯ القروب : {message.chat.title}\n"
        f"⌯ ايدي القروب : `{message.chat.id}`"
    )

    btn = InlineKeyboardMarkup(
        [[InlineKeyboardButton(user.first_name, url=f"https://t.me/{user.username}")]]
    )

    if photo:
        await message.reply_photo(photo, caption=text, reply_markup=btn)
    else:
        await message.reply(text, reply_markup=btn)


# ================== Beauty Lock ==================
@app.on_message(filters.command(["قفل جمالي", "تعطيل جمالي"]) & filters.group)
async def beauty_lock(client: Client, message: Message):
    if not await is_admin(client, message):
        return await message.reply("↢ هذا الأمر للأدمن فقط")

    if message.chat.id in BEAUTY_DISABLED:
        return await message.reply("↢ جمالي معطل بالفعل")

    BEAUTY_DISABLED.append(message.chat.id)
    await message.reply("تم تعطيل جمالي بنجاح")


@app.on_message(filters.command(["فتح جمالي", "تفعيل جمالي"]) & filters.group)
async def beauty_unlock(client: Client, message: Message):
    if not await is_admin(client, message):
        return await message.reply("↢ هذا الأمر للأدمن فقط")

    if message.chat.id not in BEAUTY_DISABLED:
        return await message.reply("↢ جمالي مفعل بالفعل")

    BEAUTY_DISABLED.remove(message.chat.id)
    await message.reply("تم تفعيل جمالي بنجاح")


# ================== Beauty ==================
@app.on_message(filters.command("جمالي") & filters.group)
async def beauty(client: Client, message: Message):
    if message.chat.id in BEAUTY_DISABLED:
        return

    percent = random.choice([10,20,30,40,50,60,70,80,90,100])
    await message.reply(f"↢ نسبة جمالك هي {percent}%")


# ================== Edit Toggle ==================
@app.on_message(filters.command("تفعيل التعديل") & filters.group)
async def enable_edit(client: Client, message: Message):
    if not await is_admin(client, message):
        return await message.reply("↢ هذا الأمر للأدمن فقط")

    if message.chat.id in EDIT_ENABLED:
        return await message.reply("↢ التعديل مفعل بالفعل")

    EDIT_ENABLED.append(message.chat.id)
    await message.reply("تم تفعيل التعديل بنجاح")


@app.on_message(filters.command("تعطيل التعديل") & filters.group)
async def disable_edit(client: Client, message: Message):
    if not await is_admin(client, message):
        return await message.reply("↢ هذا الأمر للأدمن فقط")

    if message.chat.id not in EDIT_ENABLED:
        return await message.reply("↢ التعديل معطل بالفعل")

    EDIT_ENABLED.remove(message.chat.id)
    await message.reply("تم تعطيل التعديل بنجاح")
