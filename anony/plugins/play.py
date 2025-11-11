# Copyright (c) 2025 AnonymousX1025
# Licensed under the MIT License.
# This file is part of AnonXMusic


from pyrogram import filters, types

from anony import anon, app, config, db, lang, queue, tg, yt
from anony.helpers import buttons, utils
from anony.helpers._play import checkUB


async def playlist_to_queue(
    chat_id: int,
    tracks: list,
    user: str,
    video: bool
) -> str:
    text = "<blockquote expandable>"
    for track in tracks:
        srch = await yt.search(track, 0, video=video)
        if not srch:
            continue
        srch.user = user
        pos = queue.add(chat_id, srch)
        text += f"<b>{pos}.</b> {srch.title}\n"
    text += "</blockquote>"
    return text

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
    mention = m.from_user.mention
    media = tg.get_media(m.reply_to_message) if m.reply_to_message else None
    tracks = None

    if url:
        if "playlist" in url:
            await sent.edit_text(m.lang["playlist_fetch"])
            tracks = await yt.playlist(config.PLAYLIST_LIMIT, url)
            if not tracks:
                return await sent.edit_text(m.lang["playlist_error"])
            file = await yt.search(tracks[0], sent.id, video=video)
            tracks.remove(tracks[0])
        else:
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

    if file.duration_sec > config.DURATION_LIMIT:
        return await sent.edit_text(
            m.lang["play_duration_limit"].format(config.DURATION_LIMIT // 60)
        )

    if await db.is_logger():
        await utils.play_log(m, file.title, file.duration)

    file.user = mention
    if force:
        queue.force_add(m.chat.id, file)
    else:
        position = queue.add(m.chat.id, file)

        if await db.get_call(m.chat.id):
            await sent.edit_text(
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
            if tracks:
                added = await playlist_to_queue(m.chat.id, tracks, mention, video)
                await app.send_message(
                    chat_id=m.chat.id,
                    text=m.lang["playlist_queued"].format(len(tracks)) + added,
                )
            return


    if not file.file_path:
        file.file_path = await yt.download(file.id, video=video)

    await anon.play_media(chat_id=m.chat.id, message=sent, media=file)
    if not tracks:
        return
    added = await playlist_to_queue(m.chat.id, tracks, mention, video)
    await app.send_message(
        chat_id=m.chat.id,
        text=m.lang["playlist_queued"].format(len(tracks)) + added,
    )
