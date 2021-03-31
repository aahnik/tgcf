from telethon import TelegramClient
import asyncio
import logging

from telethon.tl.patched import MessageService
from telethon.errors.rpcerrorlist import FloodWaitError

from tgcf.config import Config


async def forward_job(client: TelegramClient, config: Config):
    await client.start()
    for forward in config.forwards:
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
    await client.disconnect()
