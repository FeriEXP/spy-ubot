from .client import spy, asst
from pyrogram.errors import AccessTokenInvalid, ApiIdInvalid, ApiIdPublishedFlood
from pytgcalls import PyTgCalls
from pytgcalls import idle as pyidle
from pytgcalls import PyTgCalls



if __name__ == "__main__":
    try:
        asst.start()  # Not using run as wanna print 
        print("•×•Assistant bot Started•×•")
        spy.run() # using run for session client
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your TOKEN is not valid.")

bot = spy
call_py = PyTgCalls(bot)

call_py.start()
print("Vc Client Started")
pyidle()
idle()
