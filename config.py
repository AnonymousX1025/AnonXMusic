import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID","20213849"))
API_HASH = getenv("API_HASH","e97df0eca2a9531c80202c1a7d3f5721")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN","6591274198:AAHpFbUYOpssvwE99p8YevE8LWQdrDSekaA")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://clustercim:cumhuriyet%C3%A7ilikmilliyet%C3%A7ilikhalk%C3%A7%C4%B1l%C4%B1kdevlet%C3%A7iliklaiklikink%C4%B1lap%C3%A7%C4%B1l%C4%B1k@cluster0.lur7fky.mongodb.net")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002130443710))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 5920592740))

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
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 209715200 ))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2147483648))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQDNvmIAd9pQEPhKyvgTndCCtqbbRJ6rD4lU-djlphW-sF-jGcGi7LaDbyU3BAFv3XBJAc6zdu1J3r2iza3pWvt5OT6UekV-n9PWQZw-K_7j0NK9CbDtDNIrgZeJz5lsADrjfpRN5k0rHDgbM2rpi-CJev9i8INgtXtbxSoTyVMhhLpfn7nV6KYlNpeQmat1xrnEZMypn6geVZiUdnS2rCMsSuBirvX_zYuqw9bVbNNlFsConoZaBUAEjz8GTPW9eN7AnrhdJLPobgywUh73Jezc2raAtIcmkMCRqVFtltlYrQ7Vtso9FwPMLe6wZWokMyTrESmNzXgDAKeo4dl0oLjkAJV8ngAAAAEqw11NAA")
STRING2 = getenv("STRING_SESSION2", "BQDNvmIAHCL9Zj1t9L9d5Ca0BC42YVfjFi83x4OEmqeJ3DaonZJ9uBSCgD0IK3jWGstt-_sXpAM8zrhQhPD_Mtt07n7kVXw91oRiTgesaoDKBEHuP64TCn7lexd8bHGg3gVjY9VyMWzAtfGqbtl6bfLAewCAh0DnjLaOM9byAXO-B-bLZ2j5mw_mVc3V2yCLhc1Ny92T23gxvjnaeDNFmKFwBLsu_bjrZF8MhbJADFLj9Xr2eAK_6TgzlHSlrl-3oDEh0ZiZ0aiyu5imHag3G_w1MtakbD9uOtHwwpYbqMamqjO-IwCbl50KpgKxEmoBBhYjOBmw6DxP87cmCwjpLEVO8RLdSgAAAAEqYTC1AA")
STRING3 = getenv("STRING_SESSION3", "AgDNvmIAu7WkkhInY8hC2dCsUPaf0Sh98OvZtccavYKB40NXw2LxUhV_TwD5D6MSJdAJCvQ3BhHoCqXFYq-4oYYJ7IovOJEGijmNuGclzPcx-oZsYHQr4cs7zOCSEy08j78ILqcjzBCz_eHWRRkIF6qD9oaflPrJl7gbFbW5tdnCvFtIG6VnbA5KKRQyKjbhJykimrgQOHr_8ycAFyzhcOVvp1Fk8HbuQt6YKsffztaMEtmld2ulXn_bi6b6mFcaQQkgBv8H3LiXKNkx7MKSuZN9-EAsLZWIWmnixAr4OQllCs6wFRYNLdPOypqcmB7wznRfIAir3E6rQ2kMLKjio-RgjFX1pwAAAAEw2m9tAA")
STRING4 = getenv("STRING_SESSION4", "AgDNvmIAbw55wwy55IKZisPT800EVxgwc3X2FUg1eHH-zisONip8bbCAY2x_JbgQFZumhHbxsAg1vzdPvr_3P6fszY_6IncwBAM0wOpXZMUgAnvqovROrqZLsErVKWfbOkQrmbnCFE9ysPCbczVgGifoLTVPasBTrkRdJOovB40DqmF6EsSfEVS1oAVeAx-UlFSPGsuXweZSPYt9VbpJuRqMk-IJIeQUHmGGndNDv5uBjRDjXYbeoZjYyYtnxDI9u4nG1-MFxJcE8Wk2yTrsts1oHTJWhUrpNwsQDAXW-Z8trzz2Pcs5CoO4kukabHBKjODThEaZxp9rR52gGnWtC3ktVi5KXQAAAAE1ZEE9AA")
STRING5 = getenv("STRING_SESSION5", "BQDNvmIAZEOhE36eqs5X2MCzdiFC8Bz2eP1PRXQVvIex63cJmWjQBTyMgD1zLQ1iG6NodFwCdpfMeLNa5uWJpLzYU5jV6uQoCVxAKDMO-45mJdUQhLC1YJLxnZvkm5bMIJna7TTzThU_anybVymqBu3MnXLsNzEMi9YwjsnhjyMpy9Sr-qb6voFEoKRqaQHwFG-axYHNj0TaHAzXMBfxXNDHHsFG1TunQlT8MeHmjsk1z5fZyuScTYTaN5w736c0XKbpUynRKoKkPJQM4NmFtdES4HSVwhvm3HsgTolCm1Nk-1nEd7jHp__yyms_CDQr21MnuhSbp77ZhP-KNL82_Mf2cDFZJwAAAAEqb5LmAA")


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
