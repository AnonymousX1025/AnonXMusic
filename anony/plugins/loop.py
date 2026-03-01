# Copyright (c) 2025 AnonymousX1025
# Licensed under the MIT License.
# This file is part of AnonXMusic


from pyrogram import filters, types

from anony import app, db, lang
from anony.helpers import can_manage_vc


@app.on_message(filters.command(["loop"]) & filters.group & ~app.bl_users)
@lang.language()
@can_manage_vc
async def _loop(_, m: types.Message):
    if not await db.get_call(m.chat.id):
        return await m.reply_text(m.lang["not_playing"])

    chat_id = m.chat.id
    if len(m.command) < 2:
        if count := await db.get_loop(chat_id):
            return await m.reply_text(m.lang["loop_count"].format(count))
        else:
            return await m.reply_text(m.lang["loop_usage"])

    disable = m.command[1].lower() in ["off", "disable"]
    if not m.command[1].isdigit() and not disable:
        return await m.reply_text(m.lang["loop_usage"])

    loop = int(m.command[1]) if not disable else 0
    if loop < 1: loop = 0
    elif loop > 10: loop = 10

    await db.set_loop(m.chat.id, loop)
    if loop == 0:
        return await m.reply_text(m.lang["loop_off"])
    await m.reply_text(m.lang["loop_set"].format(loop))
