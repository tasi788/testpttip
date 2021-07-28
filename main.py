import os
from PyPtt import PTT

ptt_bot = PTT.API()

ptt_bot.login(
    os.getenv('acc'),
    os.getenv('passwd'),
    kick_other_login=True)