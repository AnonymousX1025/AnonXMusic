import asyncio
from pyrogram import Client, filters
from anony import app
import random
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
#BiLaL


iddof = []
@app.on_message(
    command(["قفل الايدي","تعطيل الايدي"])
    & filters.group
)
async def iddlock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [8087077168]:
      if message.chat.id in iddof:
        return await message.reply_text("↢ تم معطل من قبل \n√")
      iddof.append(message.chat.id)
      return await message.reply_text("تم تعطيل الايدي بنجاح 🍫.")
   else:
      return await message.reply_text("↢ متأكد انك ادمن \n√")

@app.on_message(
    command(["فتح الايدي","تفعيل الايدي"])
    & filters.group
)
async def iddopen(client, message):
   get = await app.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [8087077168]:
      if not message.chat.id in iddof:
        return await message.reply_text("↢ الايدي مفعل من قبل √")
      iddof.remove(message.chat.id)
      return await message.reply_text("↢ تم فتح الايدي بنجاح √")
   else:
      return await message.reply_text("↢ متأكد انك ادمن \n√")




@app.on_message(
    command(["ايدي","id","ا"])
    & filters.group
)
async def iddd(client, message):
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"""⌯ 𝐍𝐚𝐦𝐞 :{message.from_user.mention}\n⌯ 𝐔𝐬𝐞𝐫 :@{message.from_user.username}\n⌯ 𝐈𝐝 :`{message.from_user.id}`\n⌯ 𝐁𝐢𝐨 :{usr.bio}\n⌯ 𝐂𝐡𝐚𝐭 : {message.chat.title}\n⌯ 𝐈𝐝 𝐜𝐡𝐚𝐭:`{message.chat.id}`""", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )



iddof = []
@app.on_message(
    command(["قفل جمالي","تعطيل جمالي"])
    & filters.group
)
async def lllock(client, message):
   get = await app.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [8087077168]:
      if message.chat.id in iddof:
        return await message.reply_text("↢ جمالي معطل من قبل√")
      iddof.append(message.chat.id)
      return await message.reply_text("↢  تم تعطيل جمالي بنجاح√")
   else:
      return await message.reply_text("↢ متأكد انك ادمن \n√")

@app.on_message(
    command(["فتح جمالي","تفعيل جمالي"])
    & filters.group
)
async def idljjopen(client, message):
   get = await app.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [8087077168]:
      if not message.chat.id in iddof:
        return await message.reply_text("جمالي مفعل من قبل√")
      iddof.remove(message.chat.id)
      return await message.reply_text("تم فتح جمالي بنجاح √")
   else:
      return await message.reply_text("هذا الامر للأدمن فقط")



@app.on_message(filters.command(['تفعيل التعديل'], prefixes=""))
async def iddlock(client, message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [8087077168]:
        if message.chat.id in italy:
            return await message.reply_text("↢ تم تفعيل التعديل \n√")
        italy.append(message.chat.id)
        return await message.reply_text("تم تفعيل التعديل بنجاح \n√")
    else:
        return await message.reply_text("↢ متأكد انك ادمن \n√")

@app.on_message(filters.command(['تعطيل التعديل'], prefixes=""))
async def iddopen(client, message):
   get = await app.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [8087077168]:
      if not message.chat.id in italy:
        return await message.reply_text("↢ التعديل معطل من قبل \n√")
      italy.remove(message.chat.id)
      return await message.reply_text("تم فتح تعطيل بنجاح \n√")
   else:
      return await message.reply_text("↢ متأكد انك ادمن \n√")



@app.on_message(
    command(["جمالي"])
    & filters.group
)
async def idjjdd(client, message):
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    i = ["0","10", "20","30", "40","50","60", "70","80", "90","100","1000"]
    ik = random.choice(i)
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"↢ هذة هي نسبة جمالك : {ik}%", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )
       
