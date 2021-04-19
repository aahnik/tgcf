import asyncio
import logging

from telethon import TelegramClient
from telethon.tl.patched import MessageService
from telethon.errors.rpcerrorlist import FloodWaitError

from tgcf.config import CONFIG, API_ID, API_HASH, SESSION
from tgcf.utils import send_message
from tgcf.plugins import extended


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
                    modified_message = extended(message)
                    if not modified_message:
                        continue

                    for destination in forward.dest:
                        await send_message(client, destination, modified_message)
                    last_id = str(message.id)
                    logging.info(f"forwarding message with id = {last_id}")
                    forward.offset = last_id
                except FloodWaitError as fwe:
                    print(f"Sleeping for {fwe}")
                    await asyncio.sleep(delay=fwe.seconds)
                except Exception as err:
                    logging.exception(err)
                    break
