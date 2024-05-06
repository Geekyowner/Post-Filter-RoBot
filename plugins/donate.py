from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
@Client.on_message(filters.private & filters.command(["donate"]))
async def donatecm(bot,message):
	text = script.DONATE
	keybord = InlineKeyboardMarkup([
        			[InlineKeyboardButton("🦋 Admin",url = "https://t.me/mrbrutal_141"), 
        			InlineKeyboardButton("🔙 Back",callback_data = "help") ]])
	await message.reply_text(text = text,reply_markup = keybord)
