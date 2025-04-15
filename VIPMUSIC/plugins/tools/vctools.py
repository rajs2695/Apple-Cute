from pyrogram import Client, filters
from pyrogram.types import Message
from VIPMUSIC import app
from config import OWNER_ID
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# vc on
@app.on_message(filters.video_chat_started)
async def brah(_, msg):
    await msg.reply("**𝑉𝑎𝑛𝑡ℎ𝑢 𝐾𝑎𝑑ℎ𝑎𝑙 𝑃𝑎𝑛𝑛𝑢𝑛𝑔𝑎 𝑉𝑐 𝐿𝑎 𝐷𝑜𝑙𝑖 & 𝐷𝑜𝑙𝑎𝑛𝑠 🫶🏻🫴🏻🤍**")

# vc off
@app.on_message(filters.video_chat_ended)
async def brah2(_, msg):
    await msg.reply("**🤧💫 𝑉𝑐 𝐸𝑣𝑎𝑛𝑑𝑎 𝐸𝑛𝑑 𝑃𝑎𝑛𝑛𝑢𝑛𝑎𝑡ℎ𝑢 🥹🤌🏻**")

# invite members on vc
@app.on_message(filters.video_chat_members_invited)
async def brah3(app: app, message: Message):
    text = f"*💕 {message.from_user.mention}\n\n**𝑉𝑐 𝑉𝑎 𝑃𝑎𝑛𝑔𝑢𝑢𝑢 🫀🫂💙**\n\n**💕 **"
    x = 0
    for user in message.video_chat_members_invited.users:
        try:
            text += f"[{user.first_name}](tg://user?id={user.id}) "
            x += 1
        except Exception:
            pass

    try:
        invite_link = await app.export_chat_invite_link(message.chat.id)
        add_link = f"https://t.me/{app.username}?startgroup=true"
        reply_text = f"{text} 🤭🤭"

        await message.reply(reply_text, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text= "🐣 𝑉𝑐 𝐿𝑎 𝐽𝑜𝑖𝑛 𝐴𝑔𝑢𝑑𝑎 🦋", url=add_link)],
        ]))
    except Exception as e:
        print(f"Error: {e}")


####

@app.on_message(filters.command("math", prefixes="/"))
def calculate_math(client, message):   
    expression = message.text.split("/math ", 1)[1]
    try:        
        result = eval(expression)
        response = f"ᴛʜᴇ ʀᴇsᴜʟᴛ ɪs : {result}"
    except:
        response = "ɪɴᴠᴀʟɪᴅ ᴇxᴘʀᴇssɪᴏɴ"
    message.reply(response)


@app.on_message(filters.command(["spg"], ["/", "!", "."]))
async def search(event):
    msg = await event.respond("Searching...")
    async with aiohttp.ClientSession() as session:
        start = 1
        async with session.get(f"https://content-customsearch.googleapis.com/customsearch/v1?cx=ec8db9e1f9e41e65e&q={event.text.split()[1]}&key=AIzaSyAa8yy0GdcGPHdtD083HiGGx_S0vMPScDM&start={start}", headers={"x-referer": "https://explorer.apis.google.com"}) as r:
            response = await r.json()
            result = ""
            
            if not response.get("items"):
                return await msg.edit("No results found!")
            for item in response["items"]:
                title = item["title"]
                link = item["link"]
                if "/s" in item["link"]:
                    link = item["link"].replace("/s", "")
                elif re.search(r'\/\d', item["link"]):
                    link = re.sub(r'\/\d', "", item["link"])
                if "?" in link:
                    link = link.split("?")[0]
                if link in result:
                    # remove duplicates
                    continue
                result += f"{title}\n{link}\n\n"
            prev_and_next_btns = [Button.inline("▶️Next▶️", data=f"next {start+10} {event.text.split()[1]}")]
            await msg.edit(result, link_preview=False, buttons=prev_and_next_btns)
            await session.close()
