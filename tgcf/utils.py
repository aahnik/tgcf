import os
from tgcf.settings import API_ID,API_HASH,SESSION_STRING,BOT_TOKEN
from telethon import TelegramClient
from telethon.sessions import StringSession
import sys

def get_client():
    if BOT_TOKEN:
        client = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
    elif SESSION_STRING:
        client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
    else:
        print('Neither BOT_TOKEN nor TG_SESSION_STRING found.')
        sys.exit()
    return client


def check_version():
    print('You are not ..')
