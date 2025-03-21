#PremSub

import asyncio

from pyrogram import filters
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked

from PremSub import bot
from PremSub.config import *
from PremSub.modules.data import *

@bot.on_message(filters.command("addseller") & filters.user(ADMINS))
async def add_seller_sub(c, m):
    if c.me.id != BOT_ID:
        return
    if len(m.command) < 2:
        return await m.reply(
            "Balas pesan pengguna atau berikan user_id/username."
        )
    ids = m.command[1]
    iya = await seller_info(int(ids))
    if not iya:
        await add_seller(int(ids))
        await m.reply(f"User {ids} Berhasil di tambahkan ke seller")
    else:
        await m.reply(f"User {ids} Sudah menjadi seller")


@bot.on_message(filters.command("delseller") & filters.user(ADMINS))
async def del_seller_sub(c, m):
    if c.me.id != BOT_ID:
        return
    if len(m.command) < 2:
        return await m.reply(
            "Balas pesan pengguna atau berikan user_id/username."
        )
    ids = m.command[1]
    iya = await seller_info(int(ids))
    if iya:
        await del_seller(int(ids))
        await m.reply(f"{ids} Berhasil di hapus dari seller")
    else:
        await m.reply(f"{ids} Bukan bagian dari seller")