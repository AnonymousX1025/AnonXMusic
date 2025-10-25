# Copyright (c) 2025 AnonymousX1025
# Licensed under the MIT License.
# This file is part of AnonXMusic


import os
import re
import random
import asyncio
from pathlib import Path
from typing import Optional, Union

import yt_dlp
from py_yt import VideosSearch
from pyrogram import enums, types

from anony.helpers import Track, utils


class YouTube:
    def __init__(self):
        self.base = "https://www.youtube.com/watch?v="
        self.cookies = []
        self.checked = False
        self.regex = r"(https?://)?(www\.|m\.)?(youtube\.com/(watch\?v=|shorts/)|youtu\.be/)([a-zA-Z0-9_-]{11})"

    def get_cookies(self):
        if not self.checked:
            for file in os.listdir("anony/cookies"):
                if file.endswith(".txt"):
                    self.cookies.append(file)
            self.checked = True
        if not self.cookies:
            return None
        return f"anony/cookies/{random.choice(self.cookies)}"

    def valid(self, url: str) -> bool:
        return bool(re.match(self.regex, url))

    def url(self, message_1: types.Message) -> Union[str, None]:
        messages = [message_1]
        if message_1.reply_to_message:
            messages.append(message_1.reply_to_message)

        for message in messages:
            text = message.text or message.caption or ""

            if message.entities:
                for entity in message.entities:
                    if entity.type == enums.MessageEntityType.URL:
                        return text[entity.offset : entity.offset + entity.length]

            if message.caption_entities:
                for entity in message.caption_entities:
                    if entity.type == enums.MessageEntityType.TEXT_LINK:
                        return entity.url

        return None

    async def search(self, query: str, m_id: int, video: bool = False) -> Track | None:
        _search = VideosSearch(query, limit=1)
        results = await _search.next()
        if results and results["result"]:
            data = results["result"][0]
            return Track(
                id=data.get("id"),
                channel_name=data.get("channel", {}).get("name"),
                duration=data.get("duration"),
                duration_sec=utils.to_seconds(data.get("duration")),
                message_id=m_id,
                title=data.get("title")[:25],
                thumbnail=data.get("thumbnails", [{}])[-1].get("url").split("?")[0],
                url=data.get("link"),
                view_count=data.get("viewCount", {}).get("short"),
                video=video,
            )
        return None

    async def download(self, video_id: str, video: bool = False) -> Optional[str]:
        url = self.base + video_id
        ext = "mp4" if video else "m4a"
        filename = f"downloads/{video_id}.{ext}"

        if Path(filename).exists():
            return filename

        base_opts = {
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "quiet": True,
            "noplaylist": True,
            "geo_bypass": True,
            "no_warnings": True,
            "overwrites": False,
            "ignoreerrors": True,
            "nocheckcertificate": True,
            "cookiefile": self.get_cookies(),
        }

        if video:
            ydl_opts = {
                **base_opts,
                "format": "(bestvideo[height<=?720][width<=?1280][ext=mp4])+(bestaudio)",
                "merge_output_format": "mp4",
            }
        else:
            ydl_opts = {
                **base_opts,
                "format": "worst", #"bestaudio[ext=webm][acodec=opus]",  Temporary fix for audio downloads
                "postprocessors": [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "m4a",
                }],
            }

        def _download():
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            return filename

        return await asyncio.to_thread(_download)
