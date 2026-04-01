# Copyright (c) 2025 AnonymousX1025
# Licensed under the MIT License.
# This file is part of AnonXMusic

from ntgcalls import (ConnectionNotFound, TelegramServerError,
                      RTMPStreamingUnsupported, ConnectionError)
from pyrogram.errors import (ChatSendMediaForbidden, ChatSendPhotosForbidden,
                             MessageIdInvalid)
from pyrogram.types import InputMediaPhoto, Message
from pytgcalls import PyTgCalls, exceptions, types
from pytgcalls.pytgcalls_session import PyTgCallsSession

from anony import (app, config, db, lang, logger,
                   queue, thumb, userbot, yt)
from anony.helpers import Media, Track, buttons


class TgCall(PyTgCalls):
    def __init__(self):
        self.clients = []

    async def pause(self, chat_id: int) -> bool:
        client = await db.get_assistant(chat_id)
        await db.playing(chat_id, paused=True)
        return await client.pause(chat_id)

    async def resume(self, chat_id: int) -> bool:
        client = await db.get_assistant(chat_id)
        await db.playing(chat_id, paused=False)
        return await client.resume(chat_id)

    async def stop(self, chat_id: int) -> None:
        client = await db.get_assistant(chat_id)
        queue.clear(chat_id)
        await db.remove_call(chat_id)
        await db.set_loop(chat_id, 0)
        try:
            await client.leave_call(chat_id, close=False)
        except Exception:
            pass

    async def play_media(
        self,
        chat_id: int,
        message: Message,
        media: Media | Track,
        seek_time: int = 0,
    ) -> None:
        client = await db.get_assistant(chat_id)
        _lang = await lang.get_lang(chat_id)
        
        # Assistant ko join karwane ke liye stream taiyar karna
        stream = types.MediaStream(
            media_path=media.file_path,
            audio_parameters=types.AudioQuality.HIGH,
            video_parameters=types.VideoQuality.HD_720p,
            audio_flags=types.MediaStream.Flags.REQUIRED,
            video_flags=(
                types.MediaStream.Flags.AUTO_DETECT
                if media.video
                else types.MediaStream.Flags.IGNORE
            ),
            ffmpeg_parameters=f"-ss {seek_time}" if seek_time > 1 else None,
        )
        try:
            await client.play(
                chat_id=chat_id,
                stream=stream,
                config=types.GroupCallConfig(auto_start=False),
            )
            if not seek_time:
                await db.add_call(chat_id)
                text = f"🎵 **Now Playing:** [{media.title}]({media.url})\n👤 **By:** {media.user if hasattr(media, 'user') else 'User'}"
                keyboard = buttons.controls(chat_id)
                if message:
                    try:
                        await message.edit_text(text, reply_markup=keyboard, disable_web_page_preview=True)
                    except:
                        pass
        except Exception as e:
            logger.error(f"Play Error: {e}")
            await self.play_next(chat_id)

    async def play_next(self, chat_id: int) -> None:
        # Loop check karo pehle
        if loop := await db.get_loop(chat_id):
            await db.set_loop(chat_id, loop - 1)
            media = queue.get_current(chat_id)
        else:
            # Agla gaana queue se uthao
            media = queue.get_next(chat_id)
        
        # --- AGAR QUEUE KHALI HAI TOH AUTOPLAY TRIGGER KARO ---
        if not media:
            if await db.is_autoplay_mode(chat_id):
                logger.info(f"Autoplay trigger ho raha hai chat: {chat_id}")
                media = await yt.get_next_autoplay_video(chat_id)
                if not media:
                    return await self.stop(chat_id)
            else:
                return await self.stop(chat_id)

        # DIRECT STREAMING: Download ke bina seedha link nikaalo
        stream_url = await yt.get_stream_link(media.id, video=media.video)
        if not stream_url:
            logger.warning(f"Stream link missing for {media.title}, skipping...")
            return await self.play_next(chat_id)

        media.file_path = stream_url
        
        try:
            msg = await app.send_message(chat_id, f"🔄 **Autoplay Next:**\nTrack: **{media.title}**")
            await self.play_media(chat_id, msg, media)
        except Exception as e:
            logger.error(f"Play Next Error: {e}")
            await self.play_next(chat_id)

    async def boot(self) -> None:
        PyTgCallsSession.notice_displayed = True
        for ub in userbot.clients:
            client = PyTgCalls(ub, cache_duration=100)
            await client.start()
            self.clients.append(client)
            
            @client.on_update()
            async def update_handler(_, update: types.Update) -> None:
                if isinstance(update, types.StreamEnded):
                    # Gaana khatam hote hi play_next call hoga
                    await self.play_next(update.chat_id)
                elif isinstance(update, types.ChatUpdate):
                    if update.status in [types.ChatUpdate.Status.KICKED, types.ChatUpdate.Status.LEFT_GROUP, types.ChatUpdate.Status.CLOSED_VOICE_CHAT]:
                        await self.stop(update.chat_id)
        logger.info("Assistant(s) Started with Autoplay support.")
