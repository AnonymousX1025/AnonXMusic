# Copyright (c) 2025 AnonymousX1025
# Licensed under the MIT License.
# This file is part of AnonXMusic


import os
import shutil

from pyrogram import filters, types

from anony import anon, app, db, lang


@app.on_message(filters.command(["restart"]) & app.sudoers)
@lang.language()
async def _restart(_, m: types.Message):
    sent = await m.reply_text(m.lang["restarting"])

    for chat_id in list(db.active_calls.keys()):
        try:
            await app.send_message(
                chat_id=chat_id,
                text=m.lang["restarted"]
            )
            await anon.stop(chat_id)
        except:
            pass

    for directory in ["downloads", "cache"]:
        try:
            shutil.rmtree(directory)
        except:
            pass

    await sent.edit_text(m.lang["restarted"])
    os.system(f"kill -9 {os.getpid()} && bash start")
