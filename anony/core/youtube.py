import os
import re
import asyncio
from pathlib import Path
from typing import Union, Optional

from py_yt import Playlist, VideosSearch

from anony import logger
from anony.helpers import Track, utils
from anony.helpers._httpx import HttpxClient
from config import API_URL


class YouTube:
    def __init__(self):
        self.base = "https://www.youtube.com/watch?v="
        self.regex = re.compile(
            r"(https?://)?(www\.|m\.|music\.)?"
            r"(youtube\.com/(watch\?v=|shorts/|playlist\?list=)|youtu\.be/)"
            r"([A-Za-z0-9_-]{11}|PL[A-Za-z0-9_-]+)([&?][^\s]*)?"
        )

    def valid(self, url: str) -> bool:
        return bool(re.match(self.regex, url))

    async def search(self, query: str, m_id: int, video: bool = False) -> Track | None:
        _search = VideosSearch(query, limit=1, with_live=False)
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

    async def playlist(self, limit: int, user: str, url: str, video: bool) -> list[Track | None]:
        tracks = []
        try:
            plist = await Playlist.get(url)
            for data in plist["videos"][:limit]:
                track = Track(
                    id=data.get("id"),
                    channel_name=data.get("channel", {}).get("name", ""),
                    duration=data.get("duration"),
                    duration_sec=utils.to_seconds(data.get("duration")),
                    title=data.get("title")[:25],
                    thumbnail=data.get("thumbnails")[-1].get("url").split("?")[0],
                    url=data.get("link").split("&list=")[0],
                    user=user,
                    view_count="",
                    video=video,
                )
                tracks.append(track)
        except Exception as e:
            logger.warning("Playlist fetch failed: %s", e)
        return tracks

    async def download(self, video_id: str, video: bool = False) -> str | None:
        """
        API Only Download (No yt-dlp, No cookies)
        """

        if not API_URL:
            logger.error("API_URL not set in config.")
            return None

        # Build video URL
        video_url = self.base + video_id
        client = HttpxClient()

        try:
            response = await client.make_request(
                f"{API_URL}/api/track?url={video_url}&video={str(video).lower()}"
            )

            if not response:
                logger.warning("Empty API response.")
                return None

            cdn_url = response.get("cdnurl")
            if not cdn_url:
                logger.warning("cdnurl missing in API response.")
                return None

            # Direct file
            if not cdn_url.startswith("https://t.me/"):
                result = await client.download_file(cdn_url)
                if result.success:
                    return str(result.file_path)
                logger.warning("CDN download failed.")
                return None

            # Telegram CDN
            try:
                from anony import app
                parts = cdn_url.rstrip("/").split("/")
                chat_username = parts[-2]
                message_id = int(parts[-1])

                msg = await app.get_messages(chat_id=chat_username, message_ids=message_id)
                if msg:
                    return await msg.download()
                return None

            except Exception as e:
                logger.warning("Telegram CDN failed: %s", e)
                return None

        except Exception as e:
            logger.warning("API request failed: %s", e)
            return None

        finally:
            await client.close()
