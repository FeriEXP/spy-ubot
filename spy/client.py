from spy.config import config
from pyrogram import Client


if SESSION:
    session = SESSION(str(SESSION))
else:
    session = "spyubot"
try:
bot = Client(
    session=session,
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    plugins={'root': 'spy.plugins'}
)

asst = Client(
  "spy_ubot",
  api_id = config.API_ID,
  api_hash = config.API_HASH,
  bot_token = config.TOKEN,
  plugins={'root': "spy.assistant"}
)
