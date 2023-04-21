from AshishX.core.bot import AnonXBot
from AshishX.core.dir import dirr
from AshishX.core.git import git
from AshishX.core.userbot import Userbot
from AshishX.misc import dbb, heroku, sudo
from aiohttp import ClientSession

from .logging import LOGGER


dirr()

git()

dbb()

heroku()

sudo()

# Clients
app = AshishXBot()

userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

aiohttpsession = ClientSession()
