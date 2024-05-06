@Client.on_message(filters.private & filters.command(["donate"]))
async def donatecm(bot,message):
	text = script.DONATE_TXT
	keybord = InlineKeyboardMarkup([
        			[InlineKeyboardButton("🦋 Admin",url = "https://t.me/mrbrutal_141"), 
        			InlineKeyboardButton("✖️ Close",callback_data = "cancel") ]])
	await message.reply_text(text = text,reply_markup = keybord)
