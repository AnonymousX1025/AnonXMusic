# Copyright (c) 2025 AnonymousX1025
# Licensed under the MIT License.
# This file is part of AnonXMusic


from pyrogram import filters, types

from anony import app, db, lang


@app.on_message(filters.command(["blacklist", "unblacklist", "whitelist"]) & app.sudoers)
@lang.language()
async def _blacklist(_, m: types.Message):
    if len(m.command) < 2:
        return await m.reply_text(m.lang["bl_usage"].format(m.command[0]))

    try:
        chat_id = m.command[1]
        if not str(chat_id).startswith("@"):
            chat_id = int(chat_id)
        else:
            chat_id = (await app.get_chat(chat_id)).id
    except:
        return await m.reply_text(m.lang["bl_invalid"])

    if m.command[0] == "blacklist":
        if chat_id in db.blacklisted or chat_id in app.bl_users:
            return await m.reply_text(m.lang["bl_already"])
        if not str(chat_id).startswith("-100"):
            app.bl_users.add(chat_id)
        await db.add_blacklist(chat_id)
        await m.reply_text(m.lang["bl_added"])
    else:
        if chat_id not in db.blacklisted and chat_id not in app.bl_users:
            return await m.reply_text(m.lang["bl_not"])
        if not str(chat_id).startswith("-100"):
            app.bl_users.discard(chat_id)
        await db.del_blacklist(chat_id)
        await m.reply_text(m.lang["bl_removed"])
