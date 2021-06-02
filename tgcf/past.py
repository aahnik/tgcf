"""The module for running tgcf in past mode.

- past mode can only operate with a user account.
- past mode deals with all existing messages.
"""

import asyncio
import logging
import time

from telethon import TelegramClient
from telethon.errors.rpcerrorlist import FloodWaitError
from telethon.tl.custom.message import Message
from telethon.tl.patched import MessageService

from tgcf import storage as st
from tgcf.config import API_HASH, API_ID, CONFIG, SESSION, write_config
from tgcf.plugins import apply_plugins
from tgcf.utils import send_message


async def forward_job() -> None:
    """Forward all existing messages in the concerned chats."""
    async with TelegramClient(SESSION, API_ID, API_HASH) as client:
        client: TelegramClient
        for forward in CONFIG.forwards:
            last_id = 0
            logging.info(f"Forwarding messages from {forward.source} to {forward.dest}")
            async for message in client.iter_messages(
                forward.source, reverse=True, offset_id=forward.offset
            ):
                message: Message
                event = st.DummyEvent(message.chat_id, message.id)
                event_uid = st.EventUid(event)

                if forward.end and last_id > forward.end:
                    continue
                if isinstance(message, MessageService):
                    continue
                try:
                    tm = await apply_plugins(message)
                    if not tm:
                        continue
                    st.stored[event_uid] = {}

                    if message.is_reply:
                        r_event = st.DummyEvent(
                            message.chat_id, message.reply_to_msg_id
                        )
                        r_event_uid = st.EventUid(r_event)
                    for destination in forward.dest:
                        if message.is_reply and r_event_uid in st.stored:
                            tm.reply_to = st.stored.get(r_event_uid).get(destination)
                        fwded_msg = await send_message(destination, tm)
                        st.stored[event_uid].update({fwded_msg.chat_id: fwded_msg.id})
                    tm.clear()
                    last_id = message.id
                    logging.info(f"forwarding message with id = {last_id}")
                    forward.offset = last_id
                    write_config(CONFIG)
                    time.sleep(CONFIG.past.delay)
                    logging.info(f"slept for {CONFIG.past.delay} seconds")

                except FloodWaitError as fwe:
                    print(f"Sleeping for {fwe}")
                    await asyncio.sleep(delay=fwe.seconds)
                except Exception as err:
                    logging.exception(err)
