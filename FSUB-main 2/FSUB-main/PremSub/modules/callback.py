#PremSub

import asyncio
import importlib
import logging
import os
from datetime import datetime, timedelta
from pykeyboard import InlineKeyboard
from pyrogram import filters
from pyrogram.types import *

from PremSub import Bot, bot
from PremSub.config import *
from PremSub.modules import loadModule
from PremSub.modules.btn import *
from PremSub.modules.data import *
from PremSub.modules.func import *
from pyromod import listen

from .start import (
    buttons2,
    cancel,
    restart,
    start_msg
)

lonte = []


logs = logging.getLogger(__name__)




@bot.on_callback_query(filters.regex("cb_admines"))
async def _(_, query: CallbackQuery):
    return await query.edit_message_text(
        """
    <b> Silakan Hubungi Admin Dibawah Jika Anda Membutuhkan Bantuan.</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="Owner", user_id=1325957770),
                ],
                [
                    InlineKeyboardButton(
                        "Kembali", callback_data="back_start"
                    ),
                ],
            ]
        ),
    )

@bot.on_callback_query(filters.regex("cb_kontol"))
async def _(_, query: CallbackQuery):
    return await query.edit_message_text(
        f"""
    <b>Perintah Yang Tersedia\n\n/info - Untuk melihat masa aktif bot anda\n/setdb - Untuk mengatur channel database anda\n/addadmin - Untuk menambahkan admin bot\n/deladmin - Untuk menghapus admin bot\n/listadmin - Untuk menampilkan daftar admin\n/users - Untuk cek pengguna bot\n/broadcast - Untuk kirim pesan broadcast ke pengguna bot\n/batch - Untuk membuat link lebih dari satu file\n/genlink - buat tautan untuk satu posting\n/protect [True or False] - Berguna untuk mengaktifkan privasi konten anda\n/addbutton - Untuk menambahkan force-subs grup/channel\n/delbutton - Untuk menghapus force-subs\n/listbutton - Untuk melihat daftar force-subs</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Tutup", callback_data="mmk"
                    ),
                ]
            ]
        ),
    )

@bot.on_callback_query(filters.regex("mmk"))
async def now(_, cq):
    await cq.message.delete()

@bot.on_callback_query(filters.regex("cb_tutor"))
async def _(_, callback_query: CallbackQuery):
    await callback_query.message.edit(
        text="Berikut adalah video tutorial",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Tutorial", url="https://t.me/RuangZeeb"
                    ),
                    InlineKeyboardButton(
                        "Support", url="https://t.me/ZeebSupport"
                    ),
                ],
                [
                    InlineKeyboardButton("Kembali", callback_data="back_start"),
                ],
            ]
        ),
    )

@bot.on_callback_query(filters.regex("back_start"))
async def back_start_bc(c, callback_query: CallbackQuery):
    await callback_query.message.edit(
        start_msg.format(callback_query.from_user.mention, c.me.mention),
        reply_markup=InlineKeyboardMarkup(buttons2),
    )


@bot.on_callback_query(filters.regex("buat_bot"))
async def _(c, callback_query: CallbackQuery):
    if c.me.id != BOT_ID:
        return
    user_id = callback_query.from_user.id
    zeebfly = await cek_seller()
    if user_id not in MEMBER and user_id not in zeebfly:
        for X in zeebfly:
            await c.resolve_peer(X)
        buttons = InlineKeyboard(row_width=3)
        keyboard: List[InlineKeyboardButton] = []
        for i in range(len(zeebfly)):
            list_admin = f"👮🏼 Admin {i}"
            id_admin = zeebfly[i]
            keyboard.append(
                InlineKeyboardButton(
                    list_admin,
                    user_id=id_admin,
                )
            )
        but = [InlineKeyboardButton("Kembali", callback_data="back_start")]
        buttons.add(*keyboard + but)
        await callback_query.message.edit(
            "Untuk mengakses fitur premium ini, Anda perlu melakukan pembelian..\n\nBeli sekarang untuk bisa membuat fsub premium!",
            reply_markup=buttons,
        )
        return
    await callback_query.message.delete()
    api_ids = int(18932594)
    api_hash = "7eb4a970fcec2af7c83aba882d686810"
    bot_token = await c.ask(
        user_id,
        "Silahkan Masukan Bot token Anda",
        filters=filters.text,
    )
    if await cancel(callback_query, bot_token.text):
        return
    name_id = bot_token.text.split(":")[0]
    mang = Bot(
        name=str(name_id),
        api_id=api_ids,
        api_hash=api_hash,
        bot_token=bot_token.text,
    )
    try:
        mang.in_memory = False
        await mang.start()

        await c.send_message(
            user_id,
            f"Bot Ditemukan:\nNama : {mang.me.mention}\nID : {mang.me.id}\nUsername : @{mang.me.username}",
        )
    except Exception as e:
        return await c.send_message(user_id, f"ERROR:\n{e}")
    channel_id = await c.ask(
        user_id,
        "Masukan ID Channel Untuk Database, Pastikan Bot sudah menjadi admin di Channel Database\nContoh -100xxxx",
        filters=filters.text,
    )
    if await cancel(callback_query, channel_id.text):
        return
    try:
        await mang.export_chat_invite_link(int(channel_id.text))
        await channel_id.reply(f"Channel Database Ditemukan `{channel_id.text}`", quote=True)
    except Exception:
        channel_id = await c.ask(user_id,
            f"Pastikan @{mang.me.username} adalah admin di Channel Database tersebut.\n\n Channel Database : `{channel_id.text}`\n\nMohon Masukkan Ulang !",
            filters=filters.text,
        )

    sub_id = await c.ask(
        user_id,
        "Silakan Masukkan ID Channel Atau Grup Sebagai Force Subscribe !\n\nDan Pastikan Bot Anda Adalah Admin Di Grup/Channel Tersebut.",
    )
    if await cancel(callback_query, sub_id.text):
        return
    try:
        if int(sub_id.text) != 0:
            await mang.export_chat_invite_link(int(sub_id.text))
            await sub_id.reply(f"Force-Subs terdeteksi `{sub_id.text}`", quote=True)
    except Exception:
        sub_id = await c.ask(user_id,
            f"Pastikan @{mang.me.username} adalah admin di Channel atau Group tersebut.\n\n Channel atau Group Saat Ini: `{sub_id.text}`\n\nMohon Masukkan Ulang !",
            filters=filters.text,
        )
    admin_id = await c.ask(
        user_id,
        "Silakan Masukan ID Admin Untuk Bot Anda !",
        filters=filters.text,
    )
    if await cancel(callback_query, admin_id.text):
        return
    try:
        admin_ids = int(admin_id.text)
    except ValueError:
        admin_id = await c.ask(user_id,
            "Bukan ID Pengguna Yang Valid, ID Pengguna Haruslah Berupa Integer",
            filters=filters.text,
        )
    owner_id = await c.ask(
        user_id,
        "Silakan Masukan ID Owner Untuk Bot Anda !",
        filters=filters.text,
    )
    if await cancel(callback_query, owner_id.text):
        return
    try:
        owner_ids = int(owner_id.text)
    except ValueError:
        owner_id = await c.ask(user_id,
            "Bukan ID Pengguna Yang Valid, ID Pengguna Haruslah Berupa Integer",
            filters=filters.text,
        )
    await c.send_message(user_id, "Sukses Di Deploy . Silakan Tunggu Sebentar...")
    await add_bot(str(mang.me.id), api_ids, api_hash, bot_token.text)
    await add_owner(mang.me.id, owner_ids, int(channel_id.text))
    await add_admin(mang.me.id, admin_ids)
    await add_sub(
        mang.me.id,
        int(sub_id.text),
    )
    time = (datetime.now() + timedelta(30)).strftime("%d-%m-%Y")
    await add_timer(mang.me.id, time)
    anu = await c.send_message(
        LOG_GRP,
        f"Nama : {mang.me.first_name}\nUsername : @{mang.me.username}\nId: {mang.me.id}\nMasa Aktif : {time}\n\nPembuat: {callback_query.from_user.mention}\nId Pengguna: {callback_query.from_user.id}",
    )

    await c.pin_chat_message(LOG_GRP, anu.id)
    sinting = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "Aktif Anjeng", callback_data=f"telah_aktif {callback_query.from_user.id} {mang.me.username}"
                )
            ]
        ]
    )
    await c.send_message(LOG_GRP, f"Pesan untuk deployer @{mang.me.username}", reply_markup=sinting
    )
    os.popen(f"rm {name_id}*")
    for mod in loadModule():
            importlib.reload(importlib.import_module(f"PremSub.modules.{mod}"))
    await c.send_message(user_id, "Bot Fsub Anda Sudah Aktif Dan Bisa Langsung Digunakan !\n\nKetik /help Di Bot Anda Untuk Melihat Perintah Yang Tersedia .\n\nTerima Kasih ...")


@bot.on_callback_query(filters.regex("bck_cb"))
async def _(c, query: CallbackQuery):
    buttons = await button_pas_pertama(c)
    await query.message.edit(
            f"<b>ʜᴇʟʟᴏ</b> {query.from_user.mention}\n\n<b>sᴀʏᴀ ᴅᴀᴘᴀᴛ ᴍᴇɴʏɪᴍᴘᴀɴ ғɪʟᴇ ᴘʀɪʙᴀᴅɪ ᴅɪ ᴄʜᴀɴɴᴇʟ ᴛᴇʀᴛᴇɴᴛᴜ ᴅᴀɴ ᴘᴇɴɢɢᴜɴᴀ ʟᴀɪɴ ᴅᴀᴘᴀᴛ ᴍᴇɴɢᴀᴋsᴇsɴʏᴀ ᴅᴀʀɪ ʟɪɴᴋ ᴋʜᴜsᴜs.</b>",
            reply_markup=InlineKeyboardMarkup(buttons),
    )


@bot.on_callback_query(filters.regex("telah_aktif"))
async def _(client, callback_query: CallbackQuery):
    user_ids = int(callback_query.data.split()[1])
    bot_user = callback_query.data.split()[2]
    await client.send_message(user_ids, f"✅ <b>ʙᴏᴛ ᴋᴀᴍᴜ ᴛᴇʟᴀʜ ᴀᴋᴛɪғ sɪʟᴀʜᴋᴀɴ sᴛᴀʀᴛ ʙᴏᴛ</b> @{bot_user}")
    await callback_query.message.edit("Pesan telah di kirim")


@bot.on_callback_query(filters.regex("tutup"))
async def cb_tutup(c, query: CallbackQuery):
    try:
        await query.answer()
        await query.message.delete()
    except BaseException as e:
        logs.info(e)
