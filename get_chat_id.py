import asyncio
from settings import API_ID, API_HASH
from telethon import TelegramClient


async def get_chat_id():
    async with TelegramClient('forwarder', API_ID, API_HASH) as client:
        ref = input('Enter link/phone/username to get chat id: ')
        try:
            entity = await client.get_entity(ref)
            print(entity.title)
            print(entity.id)
        except ValueError:
            print('Could not get')


asyncio.run(get_chat_id())
