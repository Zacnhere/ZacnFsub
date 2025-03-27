#PremSub

import asyncio
import os
import sys
from datetime import datetime, timedelta
from distutils.util import strtobool
from time import time
import os
from pykeyboard import InlineKeyboard
from pyrogram import filters
from pyrogram.enums import ParseMode
from pyrogram.errors import FloodWait
from pyrogram.types import *

from PremSub import Bot, bot
from PremSub.config import *
from PremSub.modules.btn import *
from PremSub.modules.data import *
from PremSub.modules.func import *


def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "PremSub"])


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 602 * 24),
    ("hour", 602),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append(f'{amount} {unit}{"" if amount == 1 else "s"}')
    return ", ".join(parts)


start_msg = """
👋 <b>Halo</b> {}, Selamat Datang
Perkenalkan saya adalah {} 

Dengan bot ini dapat mempermudah anda dalam membuat bot Force-Sub (File Sharing) dengan mudah tanpa harus menggunakan VPS/HEROKU.
"""

buttons2 = [
    [
        InlineKeyboardButton("🛠️ Create F-Sub 🛠️", callback_data="buat_bot"),
    ],
    [
        InlineKeyboardButton("☎️ Admin ☎️", callback_data="cb_admines"),
        InlineKeyboardButton("💬 Support 💬", url="https://t.me/Cari_Teman_Fwb_Ahh"),
    ],
    [
        InlineKeyboardButton("❗️Information❗️", callback_data="cb_tutor"),
    ],
]


@bot.on_message(filters.command("start") & filters.private & subcribe)
async def start_bot(c, m):
    if c.me.id == BOT_ID:
        await add_user(c.me.id, m.from_user.id)
        await m.reply(
            start_msg.format(m.from_user.mention, c.me.mention),
            reply_markup=InlineKeyboardMarkup(buttons2),
            disable_web_page_preview=True,
        )
        return
    av = await timer_info(c.me.id)
    time = datetime.now().strftime("%d-%m-%Y")
    if av == time:
        print(f"@{c.me.username} Telah habis Mohon Tunggu Sedang Restart Bot")
        await remove_bot(str(c.me.id))
        await del_timer(c.me.id)
        os.popen(f"rm {c.me.id}*")
        await restart()
    kk = await protect_info(c.me.id)
    kon = strtobool(kk)
    await add_user(c.me.id, m.from_user.id)
    for ix in await cek_owner(c.me.id):
        chg = ix["channel"]
    text = m.text
    if len(text) > 7:
        try:
            base64_string = text.split(" ", 1)[1]
        except Exception:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(chg))
                end = int(int(argument[2]) / abs(chg))
            except BaseException:
                return
            if start <= end:
                ids = range(start, end + 1)
            else:
                ids = []
                i = start
                while True:
                    ids.append(i)
                    i -= 1
                    if i < end:
                        break
            temp_msg = await m.reply("__Tunggu Sebentar...__")
            try:
                mes = await get_messages(c, ids)
            except BaseException:
                await m.reply("Telah Terjadi Error 🥺")
                return
            await temp_msg.delete()
            for msg in mes:
                caption = msg.caption.html if msg.caption else ""
                try:
                    await msg.copy(
                        m.chat.id,
                        caption=caption,
                        parse_mode=ParseMode.HTML,
                        protect_content=kon,
                        reply_markup=None,
                    )
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                    await msg.copy(
                        m.chat.id,
                        caption=caption,
                        parse_mode=ParseMode.HTML,
                        protect_content=kon,
                        reply_markup=None,
                    )
                except BaseException:
                    pass
        elif len(argument) == 2:
            try:
                ids = int(int(argument[1]) / abs(chg))
            except BaseException:
                return
            temp_msg = await m.reply("__Tunggu Sebentar...__")
            try:
                mes = await c.get_messages(chg, ids)
            except BaseException:
                await m.reply("Telah Terjadi Error 🥺")
                return
            caption = mes.caption.html if mes.caption else ""
            await temp_msg.delete()
            await mes.copy(
                m.chat.id,
                caption=caption,
                parse_mode=ParseMode.HTML,
                protect_content=kon,
                reply_markup=None,
            )

    else:
        buttons = await button_pas_pertama(c)
        await m.reply(
            f"✋ Hallo {m.from_user.mention} !\n\nSaya dapat menyimpan file pribadi di Channel dan pengguna lain bisa melihat file yang saya buat dengan link khusus.",
            reply_markup=InlineKeyboardMarkup(buttons),
        )


@bot.on_message(filters.command("start") & filters.private)
async def start_bots(c, m):
    if c.me.id == BOT_ID:
        await add_user(c.me.id, m.from_user.id)
        await m.reply(
            start_msg.format(m.from_user.mention, c.me.mention),
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        return
    av = await timer_info(c.me.id)
    time = datetime.now().strftime("%d-%m-%Y")
    if av == time:
        print(f"@{c.me.username} Telah habis Mohon Tunggu Sedang Restart Bot")
        await remove_bot(str(c.me.id))
        await del_timer(c.me.id)
        os.popen(f"rm {c.me.id}*")
        await restart()
    await add_user(c.me.id, m.from_user.id)
    buttons = await force_button(c, m)
    try:
        await m.reply(
            f"✋ Hallo {m.from_user.mention} !\n\nAnda terlebih dahulu harus bergabung ke Channel/Grup untuk melihat File yang saya Bagikan.\n\nJika sudah bergabung silahkan ulangi tekan tombol coba lagi.",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    except Exception as e:
        print(e)

@bot.on_message(
    filters.private
    & ~filters.command(
        [
            "start",
            "clone",
            "users",
            "broadcast",
            "eval",
            "expired",
            "setdb",
            "prem",
            "setexp",#
            "cekakses",
            "addadmin",
            "deladmin",
            "listadmin",
            "help",
            "delprem",
            "info",
            "batch",
            "addseller",
            "delseller",
            "genlink",
            "protect",
            "id",
            "addbutton",
            "delbutton",
            "listbutton",
            "ping",
            "uptime",
            "limitbutton",
            "pyrogram",
        ]
    )
)
async def up_bokep(c, m):
    if c.me.id == BOT_ID:
        return
    cek = await cek_owner(c.me.id)
    adm = await admin_info(c.me.id, m.from_user.id)
    for i in cek:
        owner = i["owner"]
        dbc = i["channel"]
    av = await timer_info(c.me.id)
    time = datetime.now().strftime("%d-%m-%Y")
    if av == time:
        print(f"@{c.me.username} Telah Habis Mohon Tunggu.. Sedang Restart Bot")
        await remove_bot(str(c.me.id))
        os.popen(f"rm {c.me.id}*")
        await restart()
    if not adm and m.from_user.id != owner:
        return
    ppk = await m.reply("Tunggu sebentar...")
    iya = await m.copy(dbc)
    sagne = iya.id * abs(dbc)
    string = f"get-{sagne}"
    base64_string = await encode(string)
    link = f"https://t.me/{c.me.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "Bagikan Tautan", url=f"https://telegram.me/share/url?url={link}"
                )
            ]
        ]
    )

    await ppk.edit(
        f"Link Sharing File Berhasil Di Buat :\n\n{link}",
        reply_markup=reply_markup,
    )
    try:
        await iya.edit_reply_markup(reply_markup)
    except Exception:
        pass


@bot.on_message(filters.command("help"))
async def helper_text(c, m):
    if c.me.id == BOT_ID:
        zeebfly = await cek_seller()
        if m.from_user.id in zeebfly:
            return await m.reply(f"""
<b>Menu Perintah<b>

/prem - Untuk memberi akses bot
/setexp - Untuk mengatur masa aktif
/cekakses - Untuk melihat masa aktif
/limitbutton - Untuk menentukan jumlah button
/delprem - Menghapus anggota premium
""")
    cek = await cek_owner(c.me.id)
    adm = await admin_info(c.me.id, m.from_user.id)
    zeebfly = await cek_seller()
    for i in cek:
        owner = i["owner"]

    if m.from_user.id == owner:
        await c.send_message(
            m.chat.id,
            f"""
<b>Daftar Menu Perintah</b>

/info - Melihat masa aktif bot
/setdb - Merubah Channel database
/addadmin - Menambah admin bot F-Sub
/deladmin - Menghapus admin bot F-Sub
/listadmin - Menampilakn daftar admin
/users - Melihat jumlah pengunjung bot
/broadcast - Kirim pesan siaran ke bot
/batch - Membuat link lebih dari satu file
/genlink - Buat tauatan satu postingan
/protect True/False - Mengatifkan atau menonaktifkan pelindung konten anda
/addbutton - Menambahkan tombol F-Sub 
/delbutton - Menghapus tombol f-Sub
/listbutton - Menampilkan daftar tombol
""")

    elif adm:
        await c.send_message(
            m.chat.id,
            f"""
<b>Daftar Menu Perintah</b>

/info - ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴍᴀsᴀ ᴀᴋᴛɪғ ʙᴏᴛ ᴀɴᴅᴀ
/users - ᴜɴᴛᴜᴋ ᴄᴇᴋ ᴘᴇɴɢᴜɴᴊᴜɴɢ ʙᴏᴛ
/broadcast - ᴜɴᴛᴜᴋ ᴋɪʀɪᴍ ᴘᴇsᴀɴ ʙʀᴏᴀᴅᴄᴀsᴛ ᴋᴇ ᴘᴇɴɢᴜɴᴊᴜɴɢ ʙᴏᴛ
/batch - ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ʟɪɴᴋ ʟᴇʙɪʜ ᴅᴀʀɪ sᴀᴛᴜ ғɪʟᴇ
/genlink - ʙᴜᴀᴛ ᴛᴀᴜᴛᴀɴ ᴜɴᴛᴜᴋ sᴀᴛᴜ ᴘᴏsᴛɪɴɢ
/protect - True ᴜɴᴛᴜᴋ ᴘʀᴏᴛᴇᴄᴛ False ᴜɴᴛᴜᴋ ᴏғғ
""")


@bot.on_message(
    filters.incoming
    & ~filters.command(
        [
            "delprem",
            "eval",
            "setdb",
            "prem",
            "setexp",
            "addadmin",
            "deladmin",
            "listadmin",
            "expired",
            "help",
            "cekakses",
            "batch",
            "addseller",
            "delseller",
            "genlink",
            "protect",
            "id",
            "info",
            "addbutton",
            "delbutton",
            "listbutton",
            "ping",
            "uptime",
            "limitbutton",
            "pyrogram",
            "restart",
        ]
    )
)
async def post_channel(c, m):
    if c.me.id == BOT_ID:
        return
    cek = await cek_owner(c.me.id)
    for i in cek:
        dbc = i["channel"]
    if m.chat.id != dbc:
        return
    converted_id = m.id * abs(dbc)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://t.me/{c.me.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "Bagikan Tautan", url=f"https://telegram.me/share/url?url={link}"
                )
            ]
        ]
    )
    try:
        await m.edit_reply_markup(reply_markup)
    except Exception:
        pass


@bot.on_message(filters.command("delprem") & filters.user(ADMINS))
async def del_users(c, m):
    if c.me.id != BOT_ID:
        return
    if len(m.command) < 2:
        return await m.reply("Balas pesan pengguna atau berikan user_id/username.")
    ids = m.command[1] 
    await remove_bot(str(ids))
    await del_owner(int(ids))
    await del_timer(int(ids))
    await m.reply(f"Hapus data untuk id {ids}")
    os.popen(f"rm {ids}*")


@bot.on_message(filters.command("setdb") & filters.private)
async def ya_setting_bot(c, m):
    if c.me.id == BOT_ID:
        return
    cek = await cek_owner(c.me.id)
    for i in cek:
        owner = i["owner"]
    if m.from_user.id != owner:
        return
    if len(m.command) < 2:
        return await m.reply(
            "Balas pesan pengguna atau berikan user_id/username. channel database\ncontoh : /setdb -100123456789"
        )
    ids = int(m.command[1])
    try:
        await c.export_chat_invite_link(ids)
        await add_owner(int(c.me.id), int(m.from_user.id), ids)
        await m.reply(f"Channel database berhasil di set `{ids}`")
    except:
        return await m.reply(f"Maaf saya bukan admin di `{ids}`")


@bot.on_message(filters.command("prem"))
async def member_prem(c, m):
    if c.me.id != BOT_ID:
        return
    if len(m.command) < 2:
        return await m.reply(
            "Balas pesan pengguna atau berikan user_id/username.\ncontoh : /akses 607067484"
        )
    iya = await seller_info(m.from_user.id)
    if not iya and m.from_user.id not in ADMINS:
        return
    ids = m.command[1]
    prem = await haku_info(int(ids))
    if not prem:
        await add_haku(int(ids))
        await m.reply(f"{ids} Berhasil di tambahkan ke member premium")
    else:
        await m.reply(f"Maaf {ids} Sudah menjadi member premium")


@bot.on_message(filters.command("setexp"))
async def add_aktif_bot(c, m):
    if len(m.command) < 3:
        return await m.reply(
            "Balas pesan pengguna atau berikan user_id/username., 1 sama dengan 1 hari\ncontoh : /setexp 607067484 30"
        )
    iya = await seller_info(m.from_user.id)
    if not iya and m.from_user.id not in ADMINS:
        return
    ids = m.command[1]
    h = int(m.command[2])
    time = (datetime.now() + timedelta(h)).strftime("%d-%m-%Y")
    await add_timer(int(ids), time)
    await m.reply(f"User ID : {ids}\nTime : {time}")


@bot.on_message(filters.command("cekakses"))
async def cek_member_prem(c, m):
    iya = await seller_info(m.from_user.id)
    if not iya and m.from_user.id not in ADMINS:
        return
    anu = await cek_prem()
    msg = "Daftar member premium\n\n"
    ang = 0
    for ex in anu:
        try:
            afa = f"`{ex['nama']}` » {ex['aktif']}"
            ang += 1
        except Exception:
            continue
        msg += f"{ang} › {afa}\n"
    await m.reply(msg)


async def cancel(callback_query, text):
    if text.startswith("/"):
        await bot.send_message(
            callback_query.from_user.id,
            "Proses di batalkan, silahkan coba lagi",
        )
        return True
    else:
        return False


async def canceled(m):
    if (
        "/cancel" in m.text
        or "/cancel" not in m.text
        and "/clone" in m.text
        or "/cancel" not in m.text
        and "/clone" not in m.text
        and m.text.startswith("/")
    ):
        await m.reply("Proses di batalkan silahkan gunakan /setting", quote=True)
        return True
    else:
        return False


@bot.on_message(filters.command("ping"))
async def ping_pong(c, m):
    start = time()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    m_reply = await m.reply("Pinging...")
    delta_ping = time() - start
    await m_reply.edit(
        "PONG!!🏓 \n"
        f"• Pinger - `{delta_ping * 1000:.3f}ms`\n"
        f"• Uptime - `{uptime}`\n"
    )


@bot.on_message(filters.command("uptime"))
async def get_uptime(client, m: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m.reply_text(
        "🤖 Bot Status:\n"
        f"• Uptime: `{uptime}`\n"
        f"• Start Time: `{START_TIME_ISO}`"
    )


@bot.on_message(filters.command("limitbutton"))
async def add_max_bot(c, m):
    if len(m.command) < 3:
        return await m.reply(
            "Gunakan Format /limitbutton 20731464 2"
        )
    iya = await seller_info(m.from_user.id)
    if not iya and m.from_user.id not in ADMINS:
        return
    ids = m.command[1]
    h = int(m.command[2])
    await add_max(int(ids), h)
    await m.reply(f"BOT_ID : {ids}\nButtons : {h}")




@bot.on_message(filters.command("user") & filters.user(KITA))
async def user(client, message):
    user_id = message.from_user.id
    count = 0
    user = ""
    for X in bot._bot:
        try:
            count += 1
            user += f"""
❏ F-Sub KE {count}
 ├ AKUN: {X.me.username}
 ╰ ID: <code>{X.me.id}</code>
"""
        except:
            pass
    if len(str(user)) > 4096:
        with BytesIO(str.encode(str(user))) as out_file:
            out_file.name = "bot.txt"
            await message.reply_document(
                document=out_file,
            )
    else:
        await message.reply(f"<b>{user}</b>")

@bot.on_message(filters.command("restart") & filters.user(5589099893))
async def resttt(client, message):
    await message.reply("berhasil merestart")
    await restart()
