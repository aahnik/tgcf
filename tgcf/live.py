"""The module responsible for operating tgcf in live mode."""

import asyncio
import logging
import os
import sys
from typing import Union

from telethon import TelegramClient, events, functions, types
from telethon.errors.rpcerrorlist import FloodWaitError
from telethon.sessions import StringSession
from telethon.tl.custom.message import Message

from tgcf import config, const
from tgcf import storage as st
from tgcf.bot import get_events
from tgcf.config import CONFIG, get_SESSION
from tgcf.plugins import apply_plugins, load_async_plugins
from tgcf.utils import clean_session_files, send_message

# Retry configuration
MAX_RETRIES = 500
INITIAL_DELAY = 2  # seconds
MAX_DELAY = 60  # seconds


async def new_message_handler(event: Union[Message, events.NewMessage]) -> None:
    """Process new incoming messages."""
    chat_id = event.chat_id

    if chat_id not in config.from_to:
        return
    logging.info(f"New message received in {chat_id}")
    message = event.message

    event_uid = st.EventUid(event)

    length = len(st.stored)
    exceeding = length - const.KEEP_LAST_MANY

    if exceeding > 0:
        for key in st.stored:
            del st.stored[key]
            break

    dest = config.from_to.get(chat_id)

    tm = await apply_plugins(message)
    if not tm:
        return

    if event.is_reply:
        r_event = st.DummyEvent(chat_id, event.reply_to_msg_id)
        r_event_uid = st.EventUid(r_event)

    st.stored[event_uid] = {}
    for d in dest:
        if event.is_reply and r_event_uid in st.stored:
            tm.reply_to = st.stored.get(r_event_uid).get(d)
        try:
            fwded_msg = await send_message(d, tm)
            st.stored[event_uid].update({d: fwded_msg})
        except FloodWaitError as fwe:
            logging.info(f"Sleeping for {fwe} on forward_messages")
            await asyncio.sleep(delay=fwe.seconds)
            # Retry after flood wait
            fwded_msg = await send_message(d, tm)
            st.stored[event_uid].update({d: fwded_msg})
        except Exception as err:
            logging.exception(f"Failed to forward message to {d}: {err}")
    tm.clear()


async def edited_message_handler(event) -> None:
    """Handle message edits."""
    message = event.message

    chat_id = event.chat_id

    if chat_id not in config.from_to:
        return

    logging.info(f"Message edited in {chat_id}")

    event_uid = st.EventUid(event)

    tm = await apply_plugins(message)

    if not tm:
        return

    fwded_msgs = st.stored.get(event_uid)

    if fwded_msgs:
        for _, msg in fwded_msgs.items():
            if config.CONFIG.live.delete_on_edit == message.text:
                await msg.delete()
                await message.delete()
            else:
                await msg.edit(tm.text)
        return

    dest = config.from_to.get(chat_id)

    for d in dest:
        try:
            await send_message(d, tm)
        except FloodWaitError as fwe:
            logging.info(f"Sleeping for {fwe} on forward_messages")
            await asyncio.sleep(delay=fwe.seconds)
            # Retry after flood wait
            await send_message(d, tm)
        except Exception as err:
            logging.exception(f"Failed to forward edited message to {d}: {err}")
    tm.clear()


async def deleted_message_handler(event):
    """Handle message deletes."""
    chat_id = event.chat_id
    if chat_id not in config.from_to:
        return

    logging.info(f"Message deleted in {chat_id}")

    event_uid = st.EventUid(event)
    fwded_msgs = st.stored.get(event_uid)
    if fwded_msgs:
        for _, msg in fwded_msgs.items():
            await msg.delete()
        return


ALL_EVENTS = {
    "new": (new_message_handler, events.NewMessage()),
    "edited": (edited_message_handler, events.MessageEdited()),
    "deleted": (deleted_message_handler, events.MessageDeleted()),
}


async def run_with_retry() -> None:
    retry_count = 0
    current_delay = INITIAL_DELAY

    while retry_count < MAX_RETRIES:
        try:
            await run_client()
            return
        except (ConnectionError, TimeoutError, ValueError, OSError) as e:
            retry_count += 1
            logging.warning(
                f"Connection error (attempt {retry_count}/{MAX_RETRIES}): {e}"
            )
            
            if retry_count >= MAX_RETRIES:
                logging.error(
                    f"Max retries ({MAX_RETRIES}) reached. Exiting."
                )
                break

            logging.info(f"Retrying in {current_delay} seconds...")
            await asyncio.sleep(current_delay)
            
            current_delay = min(current_delay * 2, MAX_DELAY)
            
            clean_session_files()
            logging.info("Session files cleaned, preparing for retry...")
        except Exception as e:
            logging.exception(f"Unexpected error: {e}")
            retry_count += 1
            
            if retry_count >= MAX_RETRIES:
                logging.error(
                    f"Max retries ({MAX_RETRIES}) reached due to unexpected error. Exiting."
                )
                break
            
            logging.info(f"Retrying in {current_delay} seconds...")
            await asyncio.sleep(current_delay)
            current_delay = min(current_delay * 2, MAX_DELAY)
            clean_session_files()


async def run_client() -> None:
    clean_session_files()
    await load_async_plugins()

    SESSION = get_SESSION()
    client = TelegramClient(
        SESSION,
        CONFIG.login.API_ID,
        CONFIG.login.API_HASH,
        sequential_updates=CONFIG.live.sequential_updates,
    )
    if CONFIG.login.user_type == 0:
        if CONFIG.login.BOT_TOKEN == "":
            logging.warning("Bot token not found, but login type is set to bot.")
            sys.exit()
        await client.start(bot_token=CONFIG.login.BOT_TOKEN)
    else:
        await client.start()
    config.is_bot = await client.is_bot()
    logging.info(f"config.is_bot={config.is_bot}")
    command_events = get_events()

    await config.load_admins(client)

    ALL_EVENTS.update(command_events)

    for key, val in ALL_EVENTS.items():
        if config.CONFIG.live.delete_sync is False and key == "deleted":
            continue
        client.add_event_handler(*val)
        logging.info(f"Added event handler for {key}")

    if config.is_bot and const.REGISTER_COMMANDS:
        await client(
            functions.bots.SetBotCommandsRequest(
                scope=types.BotCommandScopeDefault(),
                lang_code="en",
                commands=[
                    types.BotCommand(command=key, description=value)
                    for key, value in const.COMMANDS.items()
                ],
            )
        )
    config.from_to = await config.load_from_to(client, config.CONFIG.forwards)
    await client.run_until_disconnected()


async def start_sync() -> None:
    """Start tgcf live sync."""
    await run_with_retry()
