import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("27175096"))
API_HASH = getenv("22930f3501fc1c277e707d385c772547")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("5474502814:AAH261L7TCCNh48gBcYiI4mMnPxBiAGRt3M")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://noobarpita:arpita9711@cluster0.6tcho7h.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 700))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002103073049))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6878751957))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/AnonymousX1025/AnonXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", "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"
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/CWH_Official")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/voidxsupportchat")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "8e84d6ccd3094428908d5d2045d16790")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "14785b6abaab46f18ffe6dbc24bef229")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "=BQE9sBUAFJlZ02B0ffeiS_Tnw1lMPuDJdIuwZ2232BV6YxGrQlJpX1Vtsl7P0AU-1MLGCh5OyH3-AVW7eioG0lGSxR4x5bhBK0YqSGUXGnDkcbCR0asqjc8mSpba44QWghRt_87mLqhgwaSs1gDvh7Kh1lkfUwgvi90s0nK5QVtfBB0GREczHMMLna9GXBxMfnlvjp4n59qHFGXBjgbxkQWmvO80efOzvRtOyiYzrZoA5-cT4TWpmYZNS7UYua9BOFSnhtHtwOJnoa1cWCbr3vajHHA4xI66w1jHlHOVBMJ3iknbg8n3FzLWqDRKU2ZX-ohHmKGnZWIyjxMB1jD_fiMBBlsWaQAAAAGTQ4j6AA")
STRING2 = getenv("STRING_SESSION2", "BQE9sBUAkTD5HzwPgWzJ1LFtewKZ6ACI-YdMXebBk_fma6W6KiPcbl9tu_5Xp19gOmIVWUTtgwKKnwacsM5kKtv1937v5rfQWUJ6HUymrL3_8SR5GLT2K2qEYLSbVgNclkZT2FFASOhut_4rhGvqlbIkXdR9I_WPyu0AHRfZWPWIrpXBQ5CPLEltZCxc6qhk-K6S9adbvRGDt5uVB2bgYqnoNpP_DbhgwNuS_DGwUangWicUWlYR2Mw0jliuybwp486rZ37RIlvkoiPfLmhGiQtxYDq61RZPSave8v3VuY4e7AbAkM7SLaXuu2jQFGfq5Vku8E7CRrd6ubxZZtTCevnwcxiSHQAAAAGRxMZZAA")
STRING3 = getenv("STRING_SESSION3", "BQE9sBUAfTqkBXK66k3g40H60tP8gMjcqYGjwj5xaNoUkjhgJpvDkOeEHgOvCZipcrglVlSbZBGVjRv1Iaih07AnLUg8P78DfOPwld2VcN6d3LDyhfaCkU0oLQhImNWA5OxBbhZ98L3BoLQibTGJ0mRDkvg0XXPhfigslBtCeAKh6zkmja2Pg20zqeaL-w1xc3NPCCCR2QGPi7-4vTGPpTMzH5zII7xA8h2TtZ1bupiOS6LZ9OUYQWaC_3iwAp0nuqEB0RoUuvbHB-foyyMj9b45sipdH5LhOxreLCG3AZ0Y4CYg0uIqA_ZjMfRWvz0Z-Gl6pUQU6VkVtzPYO3W8qI0L57z7CgAAAAGbURsWAA")
STRING4 = getenv("STRING_SESSION4", "BQE9sBUARdkh_LlN7UwOtOuZRVkcyftKSCwe2AV1LhXbrM4NOiwcHjYgC580zl-pi8vbG3JdqI03XtxlT1-JnzoEzmuj9strfyKs8b_vuv5jP70cBEwBL4OyYA_6DZLonG-bcqStpXMRrXFqYvsqBd4G8bvFu8BGGhDOPbmOKlVjMl-T4JnG6KNtXu_xkgPx_WSRiuWAPF2KM9_uzgul-uKAxIp-wC22NMHEjupD-1b_RBKwU6pUZk_XqTtymWiXC0fyhmn1ANFaK0cHd-KqTJtCtbA38ZTqbx0KQLvjHaA22g7YfithLTyFUQxtDvip_h8E3PLGijBxzVz9J9kIZoer26SIRAAAAAF9x7rQAA")
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/25efe6aa029c6baea73ea.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/b8a0c1a00db3e57522b53.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
