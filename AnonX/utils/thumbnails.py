import os
import aiohttp
import aiofiles
from StormBeatz.plugins.StormBeatz.thumbnail import generate_thumb

from config import MUSIC_BOT_NAME, YOUTUBE_IMG_URL

async def gen_thumb(videoid):
    return await generate_thumb(videoid,MUSIC_BOT_NAME)
