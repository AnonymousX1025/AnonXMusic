# Copyright (c) 2025 AnonymousX1025
# Licensed under the MIT License.
# This file is part of AnonXMusic


from py_yt import VideosSearch
from pyrogram import types

from anony import app
from anony.helpers import buttons


@app.on_inline_query(~app.bl_users)
async def inline_query_handler(_, query: types.InlineQuery):
    text = query.query.strip().lower()
    if not text:
        return

    try:
        search = VideosSearch(text, limit=15)
        results = (await search.next()).get("result", [])

        answers = []
        for video in results:
            title = video.get("title", "Unknown Title").title()
            duration = video.get("duration", "N/A")
            views = video.get("viewCount", {}).get("short", "N/A")
            thumbnail = video.get("thumbnails", [{}])[0].get("url", "").split("?")[0]
            channel = video.get("channel", {}).get("name", "Unknown Channel")
            channellink = video.get("channel", {}).get("link", "https://youtube.com")
            link = video.get("link", "https://youtube.com")
            published = video.get("publishedTime", "N/A")

            description = f"{views} | {duration} | {channel} | {published}"
            caption = (
                f"<b>Title:</b> <a href='{link}'>{title[:250]}</a>\n\n"
                f"<b>Duration:</b> {duration}\n"
                f"<b>Views:</b> <code>{views}</code>\n"
                f"<b>Channel:</b> <a href='{channellink}'>{channel}</a>\n"
                f"<b>Published:</b> {published}\n\n"
                f"<u><i>Fetched by {app.name}</i></u>"
            )

            answers.append(
                types.InlineQueryResultPhoto(
                    photo_url=thumbnail,
                    title=title,
                    description=description,
                    caption=caption,
                    reply_markup=buttons.yt_key(link),
                )
            )

        if answers:
            await app.answer_inline_query(query.id, results=answers, cache_time=5)
    except:
        pass
