from telethon import client
from tgcf.utils import get_client

client = get_client()

def syncer():
    client.start()
    client.run_until_disconnected()
    