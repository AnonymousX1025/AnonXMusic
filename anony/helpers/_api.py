# Written by @AshokShau

import os
import re
import asyncio
import urllib.parse
from dataclasses import dataclass

import aiohttp
import aiofiles

from anony import app


@dataclass
class MusicTrack:
    cdnurl: str
    url: str
    id: str
    key: str = None

    @classmethod
    def from_dict(cls, data: dict) -> "MusicTrack":
        return cls(
            cdnurl=data.get("cdnurl", ""),
            url=data.get("url", ""),
            id=data.get("id", ""),
            key=data.get("key"),
        )


class FallenApi:
    def __init__(
            self, api_url: str, api_key: str,
            retries: int = 3, timeout: int = 10,
        ):
        self.api_url = api_url
        self.api_key = api_key
        self.retries = retries
        self.timeout = aiohttp.ClientTimeout(total=timeout)
        self.session: aiohttp.ClientSession | None = None
        self.headers = {
            "X-API-Key": self.api_key,
            "Accept": "application/json",
        }

    async def get_session(self) -> None:
        if not self.session:
            self.session = aiohttp.ClientSession(timeout=self.timeout)

    async def get_track(self, url: str) -> MusicTrack | None:
        endpoint = f"{self.api_url}/api/track?url={urllib.parse.quote(url)}"

        for _ in range(self.retries):
            try:
                async with self.session.get(endpoint, headers=self.headers) as resp:
                    data = await resp.json(content_type=None)
                    if resp.status == 200 and isinstance(data, dict):
                        return MusicTrack.from_dict(data)
                    else:
                        await asyncio.sleep(4)
                        continue
            except Exception:
                break
        return None

    async def download_cdn(self, cdn_url: str, video_id: str) -> str | None:
        try:
            async with self.session.get(cdn_url) as resp:
                if resp.status != 200:
                    return None

                cd = resp.headers.get("Content-Disposition")
                if cd:
                    match = re.findall(r'filename="?([^";]+)"?', cd)
                    filename = match[0] if match else None
                else:
                    filename = None
                if not filename:
                    filename = os.path.basename(cdn_url.split("?")[0]) or f"{video_id}.mp3"

                save_path = f"downloads/{filename}"
                async with aiofiles.open(save_path, "wb") as f:
                    async for chunk in resp.content.iter_chunked(16 * 1024):
                        if chunk:
                            await f.write(chunk)
                return str(save_path)
        except Exception:
            pass
        return None

    async def download_track(self, video_id: str) -> str | None:
        url = "https://www.youtube.com/watch?v=" + video_id
        track = await self.get_track(url)
        if not track:
            return None

        dl_url = track.cdnurl
        if re.match(r"https?://t\.me/([^/]+)/(\d+)", dl_url):
            try:
                msg = await app.get_messages(message_ids=dl_url)
                file_path = await msg.download()
                return file_path
            except Exception:
                return None

        return await self.download_cdn(dl_url, video_id)
