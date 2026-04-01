from pyrogram.types import InputMediaPhoto
from pytgcalls import PyTgCalls, exceptions, types
from pytgcalls.pytgcalls_session import PyTgCallsSession
from anony import app, db, lang, logger, queue, userbot, yt
from anony.helpers import buttons
import asyncio

# Ek acchi Music related image link
IMG = "https://telegra.ph/file/af55d7879948408f65792.jpg"

class TgCall(PyTgCalls):
    def __init__(self):
        self.clients = []

    async def stop(self, chat_id: int) -> None:
        client = await db.get_assistant(chat_id)
        queue.clear(chat_id)
        await db.remove_call(chat_id)
        try:
            await client.leave_call(chat_id)
        except:
            pass

    async def play_media(self, chat_id: int, media, message=None):
        client = await db.get_assistant(chat_id)
        
        stream = types.MediaStream(
            media_path=media.file_path,
            audio_parameters=types.AudioQuality.HIGH,
            video_parameters=types.VideoQuality.HD_720p,
            video_flags=types.MediaStream.Flags.AUTO_DETECT if media.video else types.MediaStream.Flags.IGNORE,
        )
        try:
            await client.play(chat_id, stream)
            await db.add_call(chat_id)
            if message:
                # Premium Bold UI with Progress Bar & Credits
                text = (
                    f"✨ **ɴᴏᴡ ᴘʟᴀʏɪɴɢ ᴏɴ ᴠᴏɪᴄᴇᴄʜᴀᴛ** ✨\n\n"
                    f"🎵 **ᴛɪᴛʟᴇ:** `{media.title}`\n"
                    f"👤 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:** {media.user}\n\n"
                    f"⏳ **ᴅᴜʀᴀᴛɪᴏɴ:** `Streaming Live`\n"
                    f"───────────────\n"
                    f"▶️ 🔘──────────────── 05:00\n\n"
                    f"🛡️ **ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ:** @aavyabots"
                )
                try:
                    await message.edit_media(
                        media=InputMediaPhoto(media=IMG, caption=text),
                        reply_markup=buttons.controls(chat_id)
                    )
                except:
                    try:
                        await message.edit_text(text, reply_markup=buttons.controls(chat_id))
                    except:
                        pass
        except Exception as e:
            logger.error(f"Play Error: {e}")
            await self.play_next(chat_id)

    async def play_next(self, chat_id: int):
        media = queue.get_next(chat_id)
        
        # Autoplay Logic
        if not media:
            if await db.is_autoplay_mode(chat_id):
                logger.info(f"Autoplay Triggered for {chat_id}")
                media = await yt.get_next_autoplay_video(chat_id)
                if not media:
                    return await self.stop(chat_id)
            else:
                return await self.stop(chat_id)

        # Get Direct Stream Link
        link = await yt.get_stream_link(media.id, video=media.video)
        if not link:
            # Agar link fail ho toh agla gaana dhoondo, VC leave mat karo
            return await self.play_next(chat_id)

        media.file_path = link
        
        try:
            msg = await app.send_message(chat_id, "🔄 **ꜰᴇᴛᴄʜɪɴɢ ɴᴇxᴛ ᴛʀᴀᴄᴋ ꜰʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ...**")
            await self.play_media(chat_id, msg, media)
        except Exception as e:
            logger.error(f"Play Next Error: {e}")
            await self.play_next(chat_id)

    async def boot(self) -> None:
        PyTgCallsSession.notice_displayed = True
        for ub in userbot.clients:
            client = PyTgCalls(ub)
            await client.start()
            self.clients.append(client)
            
            @client.on_update()
            async def update_handler(_, update):
                if isinstance(update, types.StreamEnded):
                    await self.play_next(update.chat_id)
                elif isinstance(update, types.ChatUpdate):
                    if update.status in [types.ChatUpdate.Status.KICKED, types.ChatUpdate.Status.LEFT_GROUP, types.ChatUpdate.Status.CLOSED_VOICE_CHAT]:
                        await self.stop(update.chat_id)
        logger.info("Bot started with @aavyabots Credits!")
