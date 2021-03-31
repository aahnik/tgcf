from telethon import TelegramClient
from telethon.sessions import StringSession
import asyncio
from tgcf.past import forward_job
from tgcf.config import read_config

config = read_config()



def start_past(client):
    asyncio.run(forward_job(client, config))


def start_live(client):
    pass

def start_tgcf(mode):
    pass
