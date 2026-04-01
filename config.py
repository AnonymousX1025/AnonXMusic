from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        # --- Core Settings ---
        self.API_ID = int(getenv("API_ID", 0))
        self.API_HASH = getenv("API_HASH")
        self.BOT_TOKEN = getenv("BOT_TOKEN")
        self.MONGO_URL = getenv("MONGO_URL")
        self.LOGGER_ID = int(getenv("LOGGER_ID", 0))
        self.OWNER_ID = int(getenv("OWNER_ID", 0))

        # --- Limits ---
        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 60)) * 60
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 20))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))

        # --- Sessions ---
        self.SESSION1 = getenv("SESSION1", None)
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        # --- Support Links ---
        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/+gD6eD6JN3G42OTM9")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/rajfflive")

        # --- Bot Behavior ---
        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", "false").lower() == "true"
        self.AUTO_END: bool = getenv("AUTO_END", "true").lower() == "true"
        self.THUMB_GEN: bool = getenv("THUMB_GEN", "true").lower() == "true"
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", "true").lower() == "true"
        self.LANG_CODE = getenv("LANG_CODE", "en")

        # --- FIX: YouTube Format & Quality Handling ---
        # Isse 'Requested format' wala panga khatam hoga
        self.STREAM_QUALITY = getenv("STREAM_QUALITY", "high") 
        self.YTDL_OPTS = {
            "format": "bestaudio/best",
            "quiet": True,
            "no_warnings": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "cookiesfrombrowser": (), # Isse conflict nahi hoga
        }

        # --- Cookies Handling ---
        raw_cookies = getenv("COOKIES_URL", "")
        self.COOKIES_URL = [
            url.strip() for url in raw_cookies.split(" ")
            if url and "batbin.me" in url
        ]

        # --- Images ---
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://te.legra.ph/file/3e40a408286d4eda24191.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/haagg2.png")
        self.START_IMG = getenv("START_IMG", "https://silabotov.ru/img/5a52040b-83da-47ec-8927-faae141f126e.jpg")

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
