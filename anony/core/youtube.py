import os
import re
import yt_dlp
import random
import asyncio
from py_yt import VideosSearch
from anony import logger
from anony.helpers import Track, utils

class YouTube:
    def __init__(self):
        self.base = "https://www.youtube.com/watch?v="
        self.cookie_dir = "anony/cookies"

    def get_cookies(self):
        cookies = []
        if os.path.exists(self.cookie_dir):
            for file in os.listdir(self.cookie_dir):
                if file.endswith(".txt"):
                    cookies.append(f"{self.cookie_dir}/{file}")
        return random.choice(cookies) if cookies else None

    async def search(self, query: str, m_id: int, video: bool = False) -> Track | None:
        try:
            _search = VideosSearch(query, limit=1)
            results = await _search.next()
            if results and results["result"]:
                data = results["result"][0]
                return Track(
                    id=data.get("id"),
                    title=data.get("title")[:25],
                    url=data.get("link"),
                    video=video,
                )
        except Exception:
            return None

    async def get_stream_link(self, video_id: str, video: bool = False) -> str | None:
        url = self.base + video_id
        cookie = self.get_cookies()
        ydl_opts = {
            "quiet": True,
            "format": "bestaudio/best" if not video else "best[height<=720]",
            "cookiefile": cookie,
            "nocheckcertificate": True,
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        }
        def _extract():
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                try:
                    info = ydl.extract_info(url, download=False)
                    return info.get("url")
                except Exception as e:
                    logger.error(f"Stream Error: {e}")
                    return None
        return await asyncio.to_thread(_extract)

    async def get_next_autoplay_video(self, chat_id: int) -> Track | None:
        from anony import queue
        current = queue.get_current(chat_id)
        if not current: return None
        try:
            # Current gaane ke related search
            _search = VideosSearch(f"related to {current.title}", limit=2)
            results = await _search.next()
            if results and results.get("result"):
                # Pehla result aksar wahi gaana hota hai, isliye 2nd wala uthate hain
                data = results["result"][1] if len(results["result"]) > 1 else results["result"][0]
                return Track(
                    id=data.get("id"),
                    title=data.get("title")[:25],
                    url=f"https://www.youtube.com/watch?v={data.get('id')}",
                    user="Autoplay 🚀",
                    video=current.video,
                )
        except Exception as e:
            logger.error(f"Autoplay Search Error: {e}")
            return None
