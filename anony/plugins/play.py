# Copyright (c) 2025 AnonymousX1025
# Licensed under the MIT License.
# This file is part of AnonXMusic


from pyrogram import filters, types

from anony import anon, app, config, db, lang, queue, tg, yt
from anony.helpers import buttons, utils
from anony.helpers._play import checkUB


@app.on_message(
    filters.command(["play", "playforce", "vplay", "vplayforce"])
    & filters.group
    & ~app.bl_users
)
@lang.language()
@checkUB
async def play_hndlr(
    _,
    m: types.Message,
    force: bool = False,
    video: bool = False,
    url: str = None,
) -> None:
    sent = await m.reply_text(m.lang["play_searching"])

    if len(queue.get_queue(m.chat.id)) >= 20:
        return await sent.edit_text(m.lang["queue_full"])

    media = tg.get_media(m.reply_to_message) if m.reply_to_message else None

    if url:
        file = await yt.search(url, sent.id, video=video)
        if not file:
            return await sent.edit_text(
                m.lang["play_not_found"].format(config.SUPPORT_CHAT)
            )

    elif len(m.command) >= 2:
        query = " ".join(m.command[1:])
        file = await yt.search(query, sent.id, video=video)
        if not file:
            return await sent.edit_text(
                m.lang["play_not_found"].format(config.SUPPORT_CHAT)
            )

    elif media:
        setattr(sent, "lang", m.lang)
        file = await tg.download(m.reply_to_message, sent)

    if file.duration_sec > 3600:
        return await sent.edit_text(m.lang["play_duration_limit"])

    if await db.is_logger():
        await utils.play_log(m, file.title, file.duration)

    file.user = m.from_user.mention
    if force:
        queue.force_add(m.chat.id, file)
    else:
        position = queue.add(m.chat.id, file)

        if await db.get_call(m.chat.id):
            return await sent.edit_text(
                m.lang["play_queued"].format(
                    position,
                    file.url,
                    file.title,
                    file.duration,
                    m.from_user.mention,
                ),
                reply_markup=buttons.play_queued(
                    m.chat.id, file.id, m.lang["play_now"]
                ),
            )

    if not file.file_path:
        try:
            file.file_path = await yt.download(file.id, video=video)
        except:
            await anon.stop(m.chat.id)
            return await sent.edit_text(
                m.lang["error_no_file"].format(config.SUPPORT_CHAT)
            )

    await anon.play_media(chat_id=m.chat.id, message=sent, media=file)
