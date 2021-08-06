import random
from pyrogram import Client, filters


STICKERS = ["CAACAgUAAxkBAAEGPnNgPcbx75_XWKMwgMtZIJlvpUa9gAACsQIAAkzoiVdQPozmP6_Gjx4E", "CAACAgUAAxkBAAEGPnVgPccf4H7Yj7GAoVY9NuoNH9CslAACEQIAApuT8FXBRjVF95zJJR4E"]


# Help Message
@Client.on_message(filters.private & filters.command(["help"]))
async def _help(_, msg):
	STICKER = random.choice(STICKERS)
	await msg.reply_sticker(STICKER)
