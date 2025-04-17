from VIPMUSIC import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🏓🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ "𝘝𝘢𝘯𝘢𝘬𝘬𝘰.. 𝘶𝘯𝘢𝘬𝘦𝘯𝘯𝘢𝘥𝘢 𝘵𝘩𝘶𝘬𝘬𝘢𝘮 𝘪𝘱𝘰𝘷𝘦.𝘈𝘥𝘪𝘯𝘨𝘨 𝘋𝘢𝘮𝘴𝘢𝘬𝘬𝘢𝘯𝘯𝘢.🤣",
          " 𝘕𝘦𝘳𝘢𝘮 𝘢𝘢𝘤𝘩𝘶𝘯𝘢 𝘷𝘢𝘯𝘵𝘩𝘶𝘥𝘳𝘢𝘯𝘶𝘯𝘨𝘢 𝘬𝘢𝘥𝘢𝘺𝘢 𝘴𝘢𝘵𝘵𝘩𝘪𝘵𝘶 𝘬𝘦𝘭𝘢𝘮𝘣𝘪𝘵𝘢𝘯𝘨𝘢𝘭𝘢 𝘪𝘭𝘢𝘺𝘢𝘯𝘶 𝘱𝘢𝘬𝘢𝘯𝘶𝘯𝘢 😒",
          "𝘐𝘱𝘰 𝘦𝘭𝘶𝘯𝘵𝘩𝘶 𝘷𝘢𝘳𝘢 𝘱𝘰𝘳𝘢𝘺𝘢 𝘪𝘭𝘢 𝘶𝘯 𝘮𝘢𝘯𝘥𝘢𝘪𝘭𝘢 𝘮𝘰𝘭𝘢𝘨𝘢 𝘢𝘳𝘢𝘪𝘬𝘢𝘷𝘢👿",
          "𝘛𝘩𝘰𝘰𝘯𝘨𝘪 𝘵𝘩𝘰𝘰𝘯𝘨𝘪𝘺𝘦 𝘱𝘢𝘢𝘵𝘩𝘪 𝘱𝘦𝘳𝘢 𝘷𝘦𝘳𝘢𝘵𝘵𝘪𝘵𝘢. 𝘔𝘦𝘦𝘵𝘩𝘪 𝘱𝘦𝘳𝘢𝘺𝘶𝘮 𝘷𝘦𝘳𝘢𝘵𝘵𝘢 𝘱𝘭𝘢𝘯 𝘱𝘢𝘯𝘥𝘳𝘪𝘺𝘢😤😤",
          "𝘕𝘢𝘯𝘨𝘢 𝘱𝘰𝘷𝘰𝘮 𝘪𝘭𝘢 𝘪𝘯𝘨𝘢𝘺𝘦 𝘱𝘢𝘢𝘪 𝘷𝘪𝘳𝘪𝘤𝘩𝘪 𝘱𝘢𝘥𝘶𝘱𝘰𝘮. 𝘜𝘯𝘨𝘢𝘭𝘶𝘬𝘦𝘯𝘯𝘢🤭🤭",
          "𝘕𝘪𝘵 𝘧𝘶𝘭𝘭𝘢 𝘳𝘰𝘮𝘢𝘯𝘤𝘦 𝘱𝘢𝘯𝘢 𝘵𝘩𝘶𝘬𝘬𝘢𝘮 𝘷𝘢𝘳𝘵𝘩𝘶𝘯𝘶 𝘴𝘰𝘭𝘢 𝘷𝘦𝘯𝘥𝘪𝘺𝘢𝘵𝘩𝘶 🔪",
          "𝘒𝘢𝘥𝘩𝘢𝘭 𝘱𝘢𝘯𝘥𝘳𝘢𝘱𝘰 𝘷𝘢𝘳𝘢𝘵𝘩𝘢 𝘵𝘩𝘶𝘬𝘬𝘢𝘮 𝘪𝘱𝘰 𝘮𝘢𝘵𝘶𝘮 𝘦𝘱𝘥𝘪𝘥𝘢 𝘷𝘢𝘳𝘵𝘩𝘶🥱",
          "𝘒𝘢𝘥𝘩𝘢𝘭 𝘬𝘦𝘦𝘵𝘩𝘢𝘭𝘯𝘶 𝘱𝘢𝘯𝘪𝘵𝘶 𝘵𝘩𝘶𝘬𝘬𝘢𝘮 𝘬𝘦𝘦𝘬𝘢𝘮𝘯𝘶 𝘴𝘰𝘯𝘯𝘢. 𝘈𝘥𝘪𝘤𝘩𝘪 𝘥𝘢𝘮𝘢𝘭 𝘱𝘢𝘯𝘪𝘥𝘶𝘷𝘦𝘯 𝘶𝘯𝘯𝘢 😡",
          "𝘚𝘢𝘳𝘢𝘬𝘢𝘥𝘪𝘬𝘢𝘭𝘢𝘮 𝘵𝘩𝘶𝘯𝘨𝘢𝘵𝘩𝘢 🍻",
          "𝘒𝘢𝘯𝘢𝘷𝘶𝘭𝘢 𝘯𝘢 𝘷𝘢𝘳𝘦𝘯 🤗",
          "𝘛𝘩𝘶𝘯𝘨𝘶𝘳𝘢𝘷𝘢𝘯 𝘵𝘩𝘢𝘭𝘢𝘪𝘭𝘢 𝘧𝘢𝘯 𝘬𝘢𝘭𝘢𝘯𝘥𝘶 𝘷𝘪𝘭𝘶𝘮😝",
          "𝘝𝘪𝘵𝘢𝘵𝘵𝘩𝘢 𝘱𝘢𝘢𝘵𝘩𝘶 𝘱𝘢𝘥𝘶𝘬𝘢𝘵𝘩𝘢 𝘰𝘥𝘶 𝘱𝘶𝘳𝘪𝘯𝘫𝘪 𝘮𝘢𝘯𝘥𝘢𝘪𝘭𝘢 𝘷𝘪𝘭𝘢 𝘱𝘰𝘵𝘩𝘶 😝",
          "𝘶𝘯 𝘒𝘢𝘯𝘢𝘷𝘶𝘭𝘢 𝘬𝘶𝘥𝘢 𝘮𝘢 𝘵𝘩𝘢𝘯 𝘷𝘢𝘳𝘶𝘷𝘦𝘯 🫶🏻",
          "𝘛𝘩𝘢𝘮𝘣𝘪 𝘮𝘢𝘯𝘪 𝘪𝘯𝘯𝘶𝘮 𝘢𝘨𝘢𝘭𝘢. 𝘈𝘵𝘩𝘶𝘬𝘶𝘭𝘭𝘢 𝘦𝘯𝘨𝘢 𝘱𝘰𝘳𝘪𝘯𝘨𝘢🌝",
           ]

VC_TAG = [  "𝘝𝘢𝘯𝘢𝘬𝘬𝘰.. 𝘶𝘯𝘢𝘬𝘦𝘯𝘯𝘢𝘥𝘢 𝘵𝘩𝘶𝘬𝘬𝘢𝘮 𝘪𝘱𝘰𝘷𝘦.𝘈𝘥𝘪𝘯𝘨𝘨 𝘋𝘢𝘮𝘴𝘢𝘬𝘬𝘢𝘯𝘯𝘢.🤣",
          " 𝘕𝘦𝘳𝘢𝘮 𝘢𝘢𝘤𝘩𝘶𝘯𝘢 𝘷𝘢𝘯𝘵𝘩𝘶𝘥𝘳𝘢𝘯𝘶𝘯𝘨𝘢 𝘬𝘢𝘥𝘢𝘺𝘢 𝘴𝘢𝘵𝘵𝘩𝘪𝘵𝘶 𝘬𝘦𝘭𝘢𝘮𝘣𝘪𝘵𝘢𝘯𝘨𝘢𝘭𝘢 𝘪𝘭𝘢𝘺𝘢𝘯𝘶 𝘱𝘢𝘬𝘢𝘯𝘶𝘯𝘢 😒",
          "𝘐𝘱𝘰 𝘦𝘭𝘶𝘯𝘵𝘩𝘶 𝘷𝘢𝘳𝘢 𝘱𝘰𝘳𝘢𝘺𝘢 𝘪𝘭𝘢 𝘶𝘯 𝘮𝘢𝘯𝘥𝘢𝘪𝘭𝘢 𝘮𝘰𝘭𝘢𝘨𝘢 𝘢𝘳𝘢𝘪𝘬𝘢𝘷𝘢👿",
          "𝘛𝘩𝘰𝘰𝘯𝘨𝘪 𝘵𝘩𝘰𝘰𝘯𝘨𝘪𝘺𝘦 𝘱𝘢𝘢𝘵𝘩𝘪 𝘱𝘦𝘳𝘢 𝘷𝘦𝘳𝘢𝘵𝘵𝘪𝘵𝘢. 𝘔𝘦𝘦𝘵𝘩𝘪 𝘱𝘦𝘳𝘢𝘺𝘶𝘮 𝘷𝘦𝘳𝘢𝘵𝘵𝘢 𝘱𝘭𝘢𝘯 𝘱𝘢𝘯𝘥𝘳𝘪𝘺𝘢😤😤",
          "𝘕𝘢𝘯𝘨𝘢 𝘱𝘰𝘷𝘰𝘮 𝘪𝘭𝘢 𝘪𝘯𝘨𝘢𝘺𝘦 𝘱𝘢𝘢𝘪 𝘷𝘪𝘳𝘪𝘤𝘩𝘪 𝘱𝘢𝘥𝘶𝘱𝘰𝘮. 𝘜𝘯𝘨𝘢𝘭𝘶𝘬𝘦𝘯𝘯𝘢🤭🤭",
          "𝘕𝘪𝘵 𝘧𝘶𝘭𝘭𝘢 𝘳𝘰𝘮𝘢𝘯𝘤𝘦 𝘱𝘢𝘯𝘢 𝘵𝘩𝘶𝘬𝘬𝘢𝘮 𝘷𝘢𝘳𝘵𝘩𝘶𝘯𝘶 𝘴𝘰𝘭𝘢 𝘷𝘦𝘯𝘥𝘪𝘺𝘢𝘵𝘩𝘶 🔪",
          "𝘒𝘢𝘥𝘩𝘢𝘭 𝘱𝘢𝘯𝘥𝘳𝘢𝘱𝘰 𝘷𝘢𝘳𝘢𝘵𝘩𝘢 𝘵𝘩𝘶𝘬𝘬𝘢𝘮 𝘪𝘱𝘰 𝘮𝘢𝘵𝘶𝘮 𝘦𝘱𝘥𝘪𝘥𝘢 𝘷𝘢𝘳𝘵𝘩𝘶🥱",
          "𝘒𝘢𝘥𝘩𝘢𝘭 𝘬𝘦𝘦𝘵𝘩𝘢𝘭𝘯𝘶 𝘱𝘢𝘯𝘪𝘵𝘶 𝘵𝘩𝘶𝘬𝘬𝘢𝘮 𝘬𝘦𝘦𝘬𝘢𝘮𝘯𝘶 𝘴𝘰𝘯𝘯𝘢. 𝘈𝘥𝘪𝘤𝘩𝘪 𝘥𝘢𝘮𝘢𝘭 𝘱𝘢𝘯𝘪𝘥𝘶𝘷𝘦𝘯 𝘶𝘯𝘯𝘢 😡",
          "𝘚𝘢𝘳𝘢𝘬𝘢𝘥𝘪𝘬𝘢𝘭𝘢𝘮 𝘵𝘩𝘶𝘯𝘨𝘢𝘵𝘩𝘢 🍻",
          "𝘒𝘢𝘯𝘢𝘷𝘶𝘭𝘢 𝘯𝘢 𝘷𝘢𝘳𝘦𝘯 🤗",
          "𝘛𝘩𝘶𝘯𝘨𝘶𝘳𝘢𝘷𝘢𝘯 𝘵𝘩𝘢𝘭𝘢𝘪𝘭𝘢 𝘧𝘢𝘯 𝘬𝘢𝘭𝘢𝘯𝘥𝘶 𝘷𝘪𝘭𝘶𝘮😝",
          "𝘝𝘪𝘵𝘢𝘵𝘵𝘩𝘢 𝘱𝘢𝘢𝘵𝘩𝘶 𝘱𝘢𝘥𝘶𝘬𝘢𝘵𝘩𝘢 𝘰𝘥𝘶 𝘱𝘶𝘳𝘪𝘯𝘫𝘪 𝘮𝘢𝘯𝘥𝘢𝘪𝘭𝘢 𝘷𝘪𝘭𝘢 𝘱𝘰𝘵𝘩𝘶 😝",
          "𝘶𝘯 𝘒𝘢𝘯𝘢𝘷𝘶𝘭𝘢 𝘬𝘶𝘥𝘢 𝘮𝘢 𝘵𝘩𝘢𝘯 𝘷𝘢𝘳𝘶𝘷𝘦𝘯 🫶🏻",
          "𝘛𝘩𝘢𝘮𝘣𝘪 𝘮𝘢𝘯𝘪 𝘪𝘯𝘯𝘶𝘮 𝘢𝘨𝘢𝘭𝘢. 𝘈𝘵𝘩𝘶𝘬𝘶𝘭𝘭𝘢 𝘦𝘯𝘨𝘢 𝘱𝘰𝘳𝘪𝘯𝘨𝘢🌝",
        ]


@app.on_message(filters.command(["gntag" ], prefixes=["/"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs. ")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ʙᴏᴛ ᴛᴀɢɢɪɴɢ...")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ғᴏᴛ ᴛᴀɢɢɪɴɢ...")
    else:
        return await message.reply("/tagall ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ʙᴏᴛ ᴛᴀɢɢɪɴɢ...")
    if chat_id in spam_chats:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt, reply_markup=InlineKeyboardMarkup([
                     [InlineKeyboardButton( text="💕 𝐒𖾓𖽖𖽷𖾓 🦋", url=f"https://t.me/{app.username}?start=help")]
                ]))
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@app.on_message(filters.command(["gmtag"], prefixes=["/"]))
async def mention_allvc(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs. ")
    if chat_id in spam_chats:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            txt = f"{usrtxt} {random.choice(VC_TAG)}"
            await client.send_message(chat_id, txt, reply_markup=InlineKeyboardMarkup([
                     [InlineKeyboardButton( text="💕 𝐒𖾓𖽖𖽷𖾓 🦋", url=f"https://t.me/{app.username}?start=help")]
                ]))
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass



@app.on_message(filters.command(["cancel", "cancel"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("๏ ᴄᴜʀʀᴇɴᴛʟʏ ɪ'ᴍ ɴᴏᴛ ᴛᴀɢɢɪɴɢ ʙᴀʙʏ.")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("๏ 🦋Stopped Mention.....🫠 ๏")
