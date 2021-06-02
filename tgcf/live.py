"""The module responsible for operating tgcf in live mode."""

import logging
from typing import Union

from telethon import events
from telethon.tl.custom.message import Message

from tgcf import config, const
from tgcf import storage as st
from tgcf.bot import BOT_EVENTS
from tgcf.plugins import apply_plugins, plugins
from tgcf.utils import send_message


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

    to_send_to = config.from_to.get(chat_id)

    if to_send_to:

        tm = await apply_plugins(message)
        if not tm:
            return

        if event.is_reply:
            r_event = st.DummyEvent(chat_id, event.reply_to_msg_id)
            r_event_uid = st.EventUid(r_event)

        st.stored[event_uid] = {}
        for recipient in to_send_to:
            if event.is_reply and r_event_uid in st.stored:
                tm.reply_to = st.stored.get(r_event_uid).get(recipient)
            fwded_msg = await send_message(recipient, tm)
            st.stored[event_uid].update({recipient: fwded_msg})
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

    to_send_to = config.from_to.get(event.chat_id)

    for recipient in to_send_to:
        await send_message(recipient, tm)
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
        for msg in fwded_msgs:
            await msg.delete()
        return


ALL_EVENTS = {
    "new": (new_message_handler, events.NewMessage()),
    "edited": (edited_message_handler, events.MessageEdited()),
    "deleted": (deleted_message_handler, events.MessageDeleted()),
}

ALL_EVENTS.update(BOT_EVENTS)

for _, plugin in plugins.items():
    try:
        event_handlers = getattr(plugin, "event_handlers")
        if event_handlers:
            ALL_EVENTS.update(event_handlers)
    except AttributeError:
        pass


def start_sync() -> None:
    """Start tgcf live sync."""
    # pylint: disable=import-outside-toplevel
    from telethon.sync import TelegramClient, functions, types

    client = TelegramClient(config.SESSION, config.API_ID, config.API_HASH)
    client.start(bot_token=config.BOT_TOKEN)
    is_bot = client.is_bot()

    for key, val in ALL_EVENTS.items():
        if key.startswith("bot"):
            if not is_bot:
                continue
        if config.CONFIG.live.delete_sync is False and key == "deleted":
            continue
        client.add_event_handler(*val)
        logging.info(f"Added event handler for {key}")

    if is_bot and const.REGISTER_COMMANDS:
        client(
            functions.bots.SetBotCommandsRequest(
                commands=[
                    types.BotCommand(command=key, description=value)
                    for key, value in const.COMMANDS.items()
                ]
            )
        )

    client.run_until_disconnected()
