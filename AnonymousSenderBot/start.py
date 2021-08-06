from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(anonbot, msg):
    print("/start")
    user = await anonbot.get_me()
    mention = user["mention"]
    await anonbot.send_message(
        msg.chat.id,
        Data.START.format(msg.from_user.mention, mention),
        reply_markup=InlineKeyboardMarkup(Data.buttons),
    )
