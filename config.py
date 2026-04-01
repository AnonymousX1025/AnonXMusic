from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", 0))
        self.API_HASH = getenv("API_HASH")
        self.BOT_TOKEN = getenv("BOT_TOKEN")
        self.MONGO_URL = getenv("MONGO_URL")
        self.LOGGER_ID = int(getenv("LOGGER_ID", 0))
        self.OWNER_ID = int(getenv("OWNER_ID", 0))

        # Missing attributes fix
        self.SESSION1 = getenv("SESSION1", None)
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)
        self.SESSION4 = getenv("SESSION4", None)
        self.SESSION5 = getenv("SESSION5", None)

        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 20))
        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 60)) * 60
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/+gD6eD6JN3G42OTM9")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/rajfflive")

        self.AUTO_LEAVE = getenv("AUTO_LEAVE", "false").lower() == "true"
        self.AUTO_END = getenv("AUTO_END", "true").lower() == "true"
        self.VIDEO_PLAY = getenv("VIDEO_PLAY", "true").lower() == "true"
        self.THUMB_GEN = getenv("THUMB_GEN", "true").lower() == "true"
        self.LANG_CODE = getenv("LANG_CODE", "en")

        # --- YOUTUBE FORCE BYPASS ---
        self.STREAM_QUALITY = getenv("STREAM_QUALITY", "low") # Low quality usually bypasses blocks
        self.YTDL_OPTS = {
            "format": "bestaudio/best",
            "quiet": True,
            "no_warnings": True,
            "nocheckcertificate": True,
            "geo_bypass": True,
            "source_address": "0.0.0.0",
        }

        # Cookies link (Raw mandatory)
        raw_cookies = getenv("COOKIES_URL", "https://batbin.me/raw/crena")
        self.COOKIES_URL = [url.strip() for url in raw_cookies.split(" ") if url and "batbin.me" in url]

        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://te.legra.ph/file/3e40a408286d4eda24191.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/haagg2.png")
        self.START_IMG = getenv("START_IMG", "https://silabotov.ru/img/5a52040b-83da-47ec-8927-faae141f126e.jpg")

    def check(self):
        for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "SESSION1"]:
            if not getattr(self, var):
                raise SystemExit(f"Missing: {var}")

config = Config()
