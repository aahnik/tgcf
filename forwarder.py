''' A script to send all messages from one chat to another '''

import asyncio
import logging

from telethon.tl.patched import MessageService
from telethon.errors.rpcerrorlist import FloodWaitError
from telethon import TelegramClient
from settings import API_ID, API_HASH, forwards, get_forward, update_offset

assert forwards

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def _(string):
    try:
        return int(string)
    except:
        return string


async def forward_job():
    ''' the function that does the job 😂 '''

    async with TelegramClient('forwarder', API_ID, API_HASH) as client:
        confirm = ''' IMPORTANT 🛑
            Are you sure that your `config.ini` is correct ?

            You can run the `get_chat_info.py` script to confirm the `from` and `to`.

            Press [ENTER] to continue:
            '''

        input(confirm)

        for forward in forwards:
            from_chat, to_chat, offset = get_forward(forward)

            if not offset:
                offset = 0

            last_id = 0

            async for message in client.iter_messages(_(from_chat), reverse=True, offset_id=offset):
                if isinstance(message, MessageService):
                    continue
                try:
                    await client.send_message(_(to_chat), message)
                    last_id = str(message.id)
                    logging.info('forwarding message with id = %s', last_id)
                    update_offset(forward, last_id)
                except FloodWaitError as err:
                    print('Run the script again after some time')
                    logging.exception(err)
                    print('Run the script again after some time')
                    quit()
                except Exception as e:
                    logging.exception(e)

                    quit()

            logging.info('Completed working with %s', forward)

if __name__ == "__main__":
    asyncio.run(forward_job())
