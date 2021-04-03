import asyncio
import logging

from telethon import TelegramClient
from telethon.tl.patched import MessageService
from telethon.errors.rpcerrorlist import FloodWaitError

from tgcf.config import CONFIG, API_ID, API_HASH, SESSION


async def forward_job():
    ''' The function that does the job of forwarding all existing messages in the concerned chats'''

    async with TelegramClient(SESSION, API_ID, API_HASH) as client:

        for forward in CONFIG.forwards:
            last_id = 0
            print(forward.source)
            print(forward.dest)
            async for message in client.iter_messages(forward.source,
                                                      reverse=True,
                                                      offset_id=forward.offset):
                if isinstance(message, MessageService):
                    continue
                try:
                    for destination in forward.dest:
                        await client.send_message(destination, message)
                    last_id = str(message.id)
                    logging.info('forwarding message with id = %s', last_id)
                    forward.offset = last_id
                except FloodWaitError as fwe:
                    print(f'Sleeping for {fwe}')
                    await asyncio.sleep(delay=fwe.seconds)
                except Exception as err:
                    logging.exception(err)
                    break
