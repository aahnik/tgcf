import asyncio
import logging

from telethon import TelegramClient
from telethon.errors.rpcerrorlist import FloodWaitError
from telethon.tl.patched import MessageService

from tgcf.config import API_HASH, API_ID, CONFIG, SESSION
from tgcf.plugins import apply_plugins
from tgcf.utils import send_message


async def forward_job():
    """ The function that does the job of forwarding all existing messages in the concerned chats"""

    async with TelegramClient(SESSION, API_ID, API_HASH) as client:

        for forward in CONFIG.forwards:
            last_id = 0
            logging.info(f"Forwarding messages from {forward.source} to {forward.dest}")
            async for message in client.iter_messages(
                forward.source, reverse=True, offset_id=forward.offset
            ):
                if isinstance(message, MessageService):
                    continue
                try:
                    message = apply_plugins(message)
                    if not message:
                        continue

                    for destination in forward.dest:
                        await send_message(client, destination, message)
                    last_id = str(message.id)
                    logging.info(f"forwarding message with id = {last_id}")
                    forward.offset = last_id
                except FloodWaitError as fwe:
                    print(f"Sleeping for {fwe}")
                    await asyncio.sleep(delay=fwe.seconds)
                except Exception as err:
                    logging.exception(err)
                    break
