from pyrogram.types import Message
from pyrogram import filters
from AnonX import app, aiohttpsession as aiosession
from AnonX.utils.errors import capture_err
from asyncio import gather
from io import BytesIO


async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    async with aiosession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


@app.on_message(filters.command("carbon"))
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴄᴀʀʙᴏɴ.")
    if not message.reply_to_message.text:
        return await message.reply_text("ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴄᴀʀʙᴏɴ.")
    m = await message.reply_text("😴 ɢᴇɴᴇʀᴀᴛɪɴɢ ᴄᴀʀʙᴏɴ...")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("ᴜᴩʟᴏᴀᴅɪɴɢ ɢᴇɴᴇʀᴀᴛᴇᴅ ᴄᴀʀʙᴏɴ...")
    await app.send_photo(message.chat.id, carbon)
    await m.delete()
    carbon.close()
