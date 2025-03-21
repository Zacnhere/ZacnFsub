#PremSub

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PremSub import bot
from PremSub.config import *
from PremSub.modules.data import *
from PremSub.modules.func import *


@bot.on_message(filters.private & filters.command("batch"))
async def batch(c, m):
    if c.me.id == BOT_ID:
        return
    cek = await cek_owner(c.me.id)
    adm = await admin_info(c.me.id, m.from_user.id)
    for i in cek:
        owner = i["owner"]
        chg = i["channel"]
    if not adm and m.from_user.id != owner:
        return
    while True:
        try:
            first_message = await c.ask(
                m.from_user.id,
                "<b>sɪʟᴀʜᴋᴀɴ ᴛᴇʀᴜsᴋᴀɴ ᴘᴇsᴀɴ/ғɪʟᴇ ᴘᴇʀᴛᴀᴍᴀ ᴅᴀʀɪ ᴄʜᴀɴɴᴇʟ ᴅᴀᴛᴀʙᴀsᴇ. (ғᴏʀᴡᴀʀᴅ ᴡɪᴛʜ ǫᴏᴜᴛᴇ)</b>\n\n<b>ᴀᴛᴀᴜ ᴋɪʀɪᴍ ʟɪɴᴋ ᴘᴏsᴛɪɴɢᴀɴ ᴅᴀʀɪ ᴄʜᴀɴɴᴇʟ ᴅᴀᴛᴀʙᴀsᴇ</b>",
                filters=(filters.forwarded | (filters.text & ~filters.forwarded)),
                timeout=60,
            )
        except BaseException:
            return
        f_msg_id = await get_message_id(c, first_message)
        if f_msg_id:
            break
        await first_message.reply(
            "❌ <b>ᴇʀʀᴏʀ</b>\n\n<b>ᴘᴏsᴛɪɴɢᴀɴ ʏᴀɴɢ ᴅɪғᴏʀᴡᴀʀᴅ ɪɴɪ ʙᴜᴋᴀɴ ᴅᴀʀɪ ᴄʜᴀɴɴᴇʟ ᴅᴀᴛᴀʙᴀsᴇ sᴀʏᴀ</b>",
            quote=True,
        )
        continue

    while True:
        try:
            second_message = await c.ask(
                m.from_user.id,
                "<b>sɪʟᴀʜᴋᴀɴ ᴛᴇʀᴜsᴋᴀɴ ᴘᴇsᴀɴ/ғɪʟᴇ ᴛᴇʀᴀᴋʜɪʀ ᴅᴀʀɪ ᴄʜᴀɴɴᴇʟ ᴅᴀᴛᴀʙᴀsᴇ. (ғᴏʀᴡᴀʀᴅ ᴡɪᴛʜ ǫᴏᴜᴛᴇ)</b>\n\n<b>ᴀᴛᴀᴜ ᴋɪʀɪᴍ ʟɪɴᴋ ᴘᴏsᴛɪɴɢᴀɴ ᴅᴀʀɪ ᴄʜᴀɴɴᴇʟ ᴅᴀᴛᴀʙᴀsᴇ</b>",
                filters=(filters.forwarded | (filters.text & ~filters.forwarded)),
                timeout=60,
            )
        except BaseException:
            return
        s_msg_id = await get_message_id(c, second_message)
        if s_msg_id:
            break
        await second_message.reply(
            "❌ <b>ᴇʀʀᴏʀ</b>\n\n<b>ᴘᴏsᴛɪɴɢᴀɴ ʏᴀɴɢ ᴅɪғᴏʀᴡᴀʀᴅ ɪɴɪ ʙᴜᴋᴀɴ ᴅᴀʀɪ ᴄʜᴀɴɴᴇʟ ᴅᴀᴛᴀʙᴀsᴇ sᴀʏᴀ</b>",
            quote=True,
        )
        continue

    string = f"get-{f_msg_id * abs(chg)}-{s_msg_id * abs(chg)}"
    base64_string = await encode(string)
    link = f"https://t.me/{c.me.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "ʙᴀɢɪᴋᴀɴ ᴛᴀᴜᴛᴀɴ", url=f"https://telegram.me/share/url?url={link}"
                )
            ]
        ]
    )
    await second_message.reply_text(
        f"<b>ʟɪɴᴋ sʜᴀʀɪɴɢ ғɪʟᴇ ʙᴇʀʜᴀsɪʟ ᴅɪ ʙᴜᴀᴛ:</b>\n\n{link}",
        quote=True,
        reply_markup=reply_markup,
    )


@bot.on_message(filters.private & filters.command("genlink"))
async def link_generator(c, m):
    if c.me.id == BOT_ID:
        return
    cek = await cek_owner(c.me.id)
    adm = await admin_info(c.me.id, m.from_user.id)
    for i in cek:
        owner = i["owner"]
        chg = i["channel"]
    if not adm and m.from_user.id != owner:
        return
    while True:
        try:
            channel_message = await c.ask(
                m.from_user.id,
                "<b>sɪʟᴀʜᴋᴀɴ ᴛᴇʀᴜsᴋᴀɴ ᴘᴇsᴀɴ/ғɪʟᴇ ᴛᴇʀᴀᴋʜɪʀ ᴅᴀʀɪ ᴄʜᴀɴɴᴇʟ ᴅᴀᴛᴀʙᴀsᴇ. (ғᴏʀᴡᴀʀᴅ ᴡɪᴛʜ ǫᴏᴜᴛᴇ)</b>\n\n<b>ᴀᴛᴀᴜ ᴋɪʀɪᴍ ʟɪɴᴋ ᴘᴏsᴛɪɴɢᴀɴ ᴅᴀʀɪ ᴄʜᴀɴɴᴇʟ ᴅᴀᴛᴀʙᴀsᴇ</b>",
                filters=(filters.forwarded | (filters.text & ~filters.forwarded)),
                timeout=60,
            )
        except BaseException:
            return
        msg_id = await get_message_id(c, channel_message)
        if msg_id:
            break
        await channel_message.reply(
            "❌ <b>ᴇʀʀᴏʀ</b>\n\n<b>ᴘᴏsᴛɪɴɢᴀɴ ʏᴀɴɢ ᴅɪғᴏʀᴡᴀʀᴅ ɪɴɪ ʙᴜᴋᴀɴ ᴅᴀʀɪ ᴄʜᴀɴɴᴇʟ ᴅᴀᴛᴀʙᴀsᴇ sᴀʏᴀ</b>",
            quote=True,
        )
        continue

    base64_string = await encode(f"get-{msg_id * abs(chg)}")
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
    await channel_message.reply_text(
        f"<b>File Sharing Berhasil dibuat:</b>\n\n{link}",
        quote=True,
        reply_markup=reply_markup,
    )
