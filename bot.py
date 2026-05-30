from pyrogram import Client
from config import *

bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

assistant = Client(
    "assistant",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION
)

from pyrogram import idle
#assistant.start()
bot.start()

print("Bot Started")
print("Assistant Started")

bot.idle()

bot.stop()
assistant.()
