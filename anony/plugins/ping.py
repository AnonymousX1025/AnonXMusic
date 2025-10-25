# Copyright (c) 2025 AnonymousX1025
# Licensed under the MIT License.
# This file is part of AnonXMusic


import time
import psutil

from pyrogram import filters, types
from anony import app, anon, boot, config, lang
from anony.helpers import buttons


@app.on_message(filters.command(["alive", "ping"]) & ~app.bl_users)
@lang.language()
async def _ping(_, m: types.Message):
    start = time.time()
    sent = await m.reply_text(m.lang["pinging"])
    get_time = lambda s: (lambda r: (f"{r[-1]}, " if r[-1][:-4] != "0" else "") + ":".join(reversed(r[:-1])))([f"{v}{u}" for v, u in zip([s%60, (s//60)%60, (s//3600)%24, s//86400], ["s", "m", "h", "days"])])
    uptime = get_time(int(time.time() - boot))
    latency = round((time.time() - start) * 1000, 2)
    await sent.edit_media(
        media=types.InputMediaPhoto(
            media=config.PING_IMG,
            caption=m.lang["ping_pong"].format(
                latency,
                uptime,
                psutil.cpu_percent(interval=0),
                psutil.virtual_memory().percent,
                psutil.disk_usage("/").percent,
                await anon.ping(),
            )
        ),
        reply_markup=buttons.ping_markup(m.lang["support"]),
    )
