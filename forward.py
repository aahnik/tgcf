''' A script to send all messages from one chat to another '''

from datetime import datetime
from telethon.tl.types import MessageService
import asyncio
from telethon import TelegramClient
from config import api_id, api_hash, from_chat, to_chat, offset, update_offset
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)


async def job():

    async with TelegramClient('forward_sync', api_id, api_hash) as client:
        _from, _to = None, None

        async for dialog in client.iter_dialogs():
            if dialog.name == to_chat:
                _to = dialog

            elif dialog.name == from_chat:
                _from = dialog

            if (_from and _to):
                break

        if not (_from and _to):
            print('Make sure to have correct from and to in config.ini')

        global offset
        if not offset:
            offset = 0

        last_id = 0
        async for message in client.iter_messages(from_chat, reverse=True, offset_id=offset):
            if isinstance(message, MessageService):
                continue
            try:
                await client.send_message(to_chat, message)
                last_id = message.id
                print(last_id)

            except Exception as err:
                print(err)

        note = f'\n{datetime.now()} : The id of the last message forwarded is : {last_id}\n'
        open('last_id.txt', 'a').write(note)
        update_offset(last_id)


asyncio.run(job())
