# Copyright (c) 2025 AnonymousX1025
# Licensed under the MIT License.
# This file is part of AnonXMusic


import asyncio

from pyrogram import enums, errors, types

from anony import app, config, db, yt


def checkUB(play):
    async def wrapper(_, m: types.Message):
        if not m.from_user:
            return await m.reply_text(m.lang["play_user_invalid"])

        if m.chat.type != enums.ChatType.SUPERGROUP:
            await m.reply_text(m.lang["play_chat_invalid"])
            return await app.leave_chat(m.chat.id)

        if not m.reply_to_message and (
            len(m.command) < 2 or (len(m.command) == 2 and m.command[1] == "-f")
        ):
            return await m.reply_text(m.lang["play_usage"])

        force = m.command[0].endswith("force") or (
            len(m.command) > 1 and "-f" in m.command[1]
        )
        video = m.command[0][0] == "v" and config.VIDEO_PLAY
        url = yt.url(m)
        if url and not yt.valid(url):
            return await m.reply_text(m.lang["play_unsupported"])

        play_mode = await db.get_play_mode(m.chat.id)
        if play_mode or force:
            adminlist = await db.get_admins(m.chat.id)
            if (
                m.from_user.id not in adminlist
                and not await db.is_auth(m.chat.id, m.from_user.id)
                and not m.from_user.id in app.sudoers
            ):
                return await m.reply_text(m.lang["play_admin"])

        if m.chat.id not in db.active_calls:
            client = await db.get_client(m.chat.id)
            try:
                member = await app.get_chat_member(m.chat.id, client.id)
                if member.status in [
                    enums.ChatMemberStatus.BANNED,
                    enums.ChatMemberStatus.RESTRICTED,
                ]:
                    try:
                        await app.unban_chat_member(
                            chat_id=m.chat.id, user_id=client.id
                        )
                    except:
                        return await m.reply_text(
                            m.lang["play_banned"].format(
                                app.name,
                                client.id,
                                client.mention,
                                f"@{client.username}" if client.username else None,
                            )
                        )
            except errors.ChatAdminRequired:
                return await m.reply_text(m.lang["admin_required"])
            except errors.UserNotParticipant:
                if m.chat.username:
                    invite_link = m.chat.username
                    try:
                        await client.resolve_peer(invite_link)
                    except:
                        pass
                else:
                    try:
                        invite_link = (await app.get_chat(m.chat.id)).invite_link
                        if not invite_link:
                            invite_link = await app.export_chat_invite_link(m.chat.id)
                    except errors.ChatAdminRequired:
                        return await m.reply_text(m.lang["admin_required"])
                    except Exception as ex:
                        return await m.reply_text(
                            m.lang["play_invite_error"].format(type(ex).__name__)
                        )

                umm = await m.reply_text(m.lang["play_invite"].format(app.name))
                await asyncio.sleep(2)
                try:
                    await client.join_chat(invite_link)
                except errors.UserAlreadyParticipant:
                    pass
                except errors.InviteRequestSent:
                    try:
                        await client.approve_chat_join_request(m.chat.id, client.id)
                    except Exception as ex:
                        return await umm.edit_text(
                            m.lang["play_invite_error"].format(type(ex).__name__)
                        )
                except Exception as ex:
                    return await umm.edit_text(
                        m.lang["play_invite_error"].format(type(ex).__name__)
                    )

                await umm.delete()
                await client.resolve_peer(m.chat.id)

        try:
            await m.delete()
        except:
            pass

        return await play(_, m, force, video, url)

    return wrapper
