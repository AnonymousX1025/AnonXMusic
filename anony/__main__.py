# Copyright (c) 2025 AnonymousX1025
# Licensed under the MIT License.
# This file is part of AnonXMusic


import asyncio
import importlib

from pyrogram import idle

from anony import anon, app, db, logger, tasks, userbot
from anony.plugins import all_modules


async def main():
    await db.connect()
    await app.boot()
    await userbot.boot()
    await anon.boot()

    for module in all_modules:
        importlib.import_module(f"anony.plugins.{module}")
    logger.info(f"Loaded {len(all_modules)} modules.")

    sudoers = await db.get_sudoers()
    app.sudoers.update(sudoers)
    app.bl_users.update(await db.get_blacklisted())
    logger.info(f"Loaded {len(app.sudoers)} sudo users.")

    await idle()
    logger.info("Stopping...")
    await app.exit()
    await userbot.exit()
    await db.close()
    for task in tasks:
        task.cancel()
        try:
            await task
        except:
            pass
    logger.info("Stopped.")


if __name__ == "__main__":
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except KeyboardInterrupt:
        pass
