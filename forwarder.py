''' A script to send all messages from one chat to another. '''

import asyncio
import logging

from telethon.tl.patched import MessageService
from telethon.errors.rpcerrorlist import FloodWaitError
from telethon import TelegramClient
from telethon.sessions import StringSession
from settings import API_ID, API_HASH, REPLACEMENTS, forwards, get_forward, update_offset, STRING_SESSION


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

SENT_VIA = f'\n__Sent via__ `{str(__file__)}`'


def intify(string):
    try:
        return int(string)
    except:
        return string

def replace(message):
    for old,new in REPLACEMENTS.items():
        message.text = str(message.text).replace(old,new)
    return message

async def forward_job():
    ''' the function that does the job 😂 '''
    if STRING_SESSION:
        session = StringSession(STRING_SESSION)
    else:
        session = 'forwarder'

    async with TelegramClient(session, API_ID, API_HASH) as client:

        confirm = ''' IMPORTANT 🛑
            Are you sure that your `config.ini` is correct ?

            Take help of @userinfobot for correct chat ids.

            Press [ENTER] to continue:
            '''

        input(confirm)

        error_occured = False
        for forward in forwards:
            from_chat, to_chat, offset = get_forward(forward)

            if not offset:
                offset = 0

            last_id = 0

            async for message in client.iter_messages(intify(from_chat), reverse=True, offset_id=offset):
                if isinstance(message, MessageService):
                    continue
                try:
                    await client.send_message(intify(to_chat), replace(message))
                    last_id = str(message.id)
                    logging.info('forwarding message with id = %s', last_id)
                    update_offset(forward, last_id)
                except FloodWaitError as fwe:
                    print(f'{fwe}')
                    await asyncio.sleep(delay=fwe.seconds)
                except Exception as err:
                    logging.exception(err)
                    error_occured = True
                    break

            logging.info('Completed working with %s', forward)

        await client.send_file('me', 'config.ini', caption='This is your config file for telegram-chat-forward.')

        message = 'Your forward job has completed.' if not error_occured else 'Some errors occured. Please see the output on terminal. Contact Developer.'
        await client.send_message('me', f'''Hi !
        \n**{message}**
        \n**Telegram Chat Forward** is developed by @AahnikDaw.
        \nPlease star 🌟 on [GitHub](https://github.com/aahnik/telegram-chat-forward).
        {SENT_VIA}''', link_preview=False)

if __name__ == "__main__":
    assert forwards
    asyncio.run(forward_job())
