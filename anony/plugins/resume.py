# Copyright (c) 2025 AnonymousX1025
# Licensed under the MIT License.
# This file is part of AnonXMusic


from pyrogram import filters, types

from anony import anon, app, db, lang
from anony.helpers import buttons, can_manage_vc


@app.on_message(filters.command(["resume"]) & filters.group & ~app.bl_users)
@lang.language()
@can_manage_vc
async def _resume(_, m: types.Message):
    if not await db.get_call(m.chat.id):
        return await m.reply_text(m.lang["not_playing"])

    if await db.playing(m.chat.id):
        return await m.reply_text(m.lang["play_not_paused"])

    await anon.resume(m.chat.id)
    await m.reply_text(
        text=m.lang["play_resumed"].format(m.from_user.mention),
        reply_markup=buttons.controls(m.chat.id),
    )
