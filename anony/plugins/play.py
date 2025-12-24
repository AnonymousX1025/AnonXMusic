from pathlib import Path

from pyrogram import filters, types

from anony import anon, app, config, db, lang, queue, tg, yt
from anony.helpers import buttons, utils
# Removed @checkUB because its wrapper expected m.command (caused TypeError with filters.text)

def playlist_to_queue(chat_id: int, tracks: list) -> str:
    text = "<blockquote expandable>"
    for track in tracks:
        pos = queue.add(chat_id, track)
        text += f"<b>{pos}.</b> {track.title}\n"
    text = text[:1948] + "</blockquote>"
    return text

@app.on_message(filters.text & filters.group & ~app.bl_users)
@lang.language()
async def play_hndlr(_, m: types.Message) -> None:
    text = (m.text or m.caption or "").strip()
    if not text:
        return

    parts = text.split()
    cmd = parts[0].lstrip("/").lower()
    triggers = ["تشغيل", "شغل", "vplay", "vplayforce"]
    if cmd not in triggers:
        return

    force = cmd == "vplayforce" or ("-f" in parts)
    video = cmd in ("vplay", "vplayforce")

    args = [p for p in parts[1:] if p != "-f"]
    url = " ".join(args).strip() if args else None

    sent = await m.reply_text(m.lang["play_searching"])
    file = None
    mention = m.from_user.mention
    media = tg.get_media(m.reply_to_message) if m.reply_to_message else None
    tracks = []

    if url:
        if "playlist" in url:
            await sent.edit_text(m.lang["playlist_fetch"])
            tracks = await yt.playlist(config.PLAYLIST_LIMIT, mention, url, video)
            if not tracks:
                return await sent.edit_text(m.lang["playlist_error"])
            file = tracks[0]
            tracks.remove(file)
            file.message_id = sent.id
        else:
            file = await yt.search(url, sent.id, video=video)
        if not file:
            return await sent.edit_text(m.lang["play_not_found"].format(config.SUPPORT_CHAT))

    elif media:
        setattr(sent, "lang", m.lang)
        file = await tg.download(m.reply_to_message, sent)

    if not file:
        return await sent.edit_text(m.lang["play_usage"])

    if file.duration_sec > config.DURATION_LIMIT:
        return await sent.edit_text(m.lang["play_duration_limit"].format(config.DURATION_LIMIT // 60))

    if await db.is_logger():
        await utils.play_log(m, file.title, file.duration)

    file.user = mention
    if force:
        queue.force_add(m.chat.id, file)
    else:
        position = queue.add(m.chat.id, file)
        if position != 0 or await db.get_call(m.chat.id):
            await sent.edit_text(
                m.lang["play_queued"].format(position, file.url, file.title, file.duration, m.from_user.mention),
                reply_markup=buttons.play_queued(m.chat.id, file.id, m.lang["play_now"]),
            )
            if tracks:
                added = playlist_to_queue(m.chat.id, tracks)
                await app.send_message(chat_id=m.chat.id, text=m.lang["playlist_queued"].format(len(tracks)) + added)
            return

    if not file.file_path:
        fname = f"downloads/{file.id}.{'mp4' if video else 'webm'}"
        if Path(fname).exists():
            file.file_path = fname
        else:
            await sent.edit_text(m.lang["play_downloading"])
            file.file_path = await yt.download(file.id, video=video)

    await anon.play_media(chat_id=m.chat.id, message=sent, media=file)

    if tracks:
        added = playlist_to_queue(m.chat.id, tracks)
        await app.send_message(chat_id=m.chat.id, text=m.lang["playlist_queued"].format(len(tracks)) + added)
