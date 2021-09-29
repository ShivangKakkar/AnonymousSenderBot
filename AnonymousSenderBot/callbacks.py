from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup
from Data import Data


# Callbacks
@Client.on_callback_query()
async def _calls(anonbot, callback_query):
    chat_id = callback_query.from_user.id
    message_id = callback_query.message.message_id
    if callback_query.data.lower() == "home":
        user = await anonbot.get_me()
        mention = user["mention"]
        await anonbot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Data.START.format(callback_query.from_user.mention, mention),
            reply_markup=InlineKeyboardMarkup(Data.buttons),
        )
    if callback_query.data.lower() == "about":
        await anonbot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Data.ABOUT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.home_button),
        )
    if callback_query.data.lower() == "remove":
        caption = ""
        await anonbot.edit_message_caption(
            chat_id=chat_id, message_id=message_id, caption=caption, reply_markup=InlineKeyboardMarkup([Data.add_button])
        )
    if callback_query.data.lower() == "add":
        caption = callback_query.message.reply_to_message.caption
        if caption:
            await anonbot.edit_message_caption(
                chat_id=chat_id, message_id=message_id, caption=caption, reply_markup=InlineKeyboardMarkup([Data.remove_button])
            )
        else:
            await callback_query.answer("The original message has been deleted or their is no previous caption.", show_alert=True)
