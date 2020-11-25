''' A script to send all messages from one chat to another '''

import asyncio
import logging

from telethon.tl.patched import MessageService
from telethon.errors.rpcerrorlist import FloodWaitError
from telethon import TelegramClient
from settings import API_ID, API_HASH, forwards, get_forward, update_offset


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


async def forward_job():
    ''' the function that does the job 😂 '''

    async with TelegramClient('forwarder', API_ID, API_HASH) as client:
        for forward in forwards:
            from_chat, to_chat, offset = get_forward(forward)
            _from, _to = None, None

            async for dialog in client.iter_dialogs():
                if dialog.name == to_chat:
                    _to = dialog
                elif dialog.name == from_chat:
                    _from = dialog
                if (_from and _to):
                    break

            if not (_from and _to):
                logging.warning(
                    'Make sure to have correct `from` and `to` for %s in config.ini', forward)
                continue
            logging.info(
                'Succesfully got the chat of `from` and `to` for %s', forward)
            if not offset:
                offset = 0

            last_id = 0
            async for message in client.iter_messages(from_chat, reverse=True, offset_id=offset):
                if isinstance(message, MessageService):
                    continue
                try:
                    await client.send_message(to_chat, message)
                    last_id = str(message.id)
                    logging.info('forwarding message with id = %s', last_id)
                    update_offset(forward, last_id)
                except FloodWaitError as err:
                    logging.exception(err)
                    quit()
                except Exception as e:
                    logging.exception(e)

            logging.info('Completed working with %s', forward)


asyncio.run(forward_job())
