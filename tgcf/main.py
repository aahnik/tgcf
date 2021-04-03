from telethon import TelegramClient
from telethon.sessions import StringSession
import asyncio
from tgcf.past import forward_job





def start_past():
    asyncio.run(forward_job())



def start_live():
    print('live')

