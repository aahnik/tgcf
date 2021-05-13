"""The module responsible for operating tgcf in live mode."""
import logging

from telethon import events

from tgcf import config, const
from tgcf.bot import BOT_EVENTS
from tgcf.plugins import apply_plugins, plugins
from tgcf.utils import send_message

existing_hashes = []

_stored = {}


class EventUid:
    """The objects of this class uniquely identifies an event."""

    def __init__(self, event):
        self.chat_id = event.chat_id
        try:
            self.msg_id = event.id
        except:  # pylint: disable=bare-except
            self.msg_id = event.deleted_id

    def __str__(self):
        return f"chat={self.chat_id} msg={self.msg_id}"

    def __eq__(self, other):
        return self.chat_id == other.chat_id and self.msg_id == other.msg_id

    def __hash__(self) -> int:
        return hash(self.__str__())


async def new_message_handler(event):
    """Process new incoming messages."""
    chat_id = event.chat_id

    if chat_id not in config.from_to:
        return
    logging.info(f"New message received in {chat_id}")
    message = event.message

    global _stored  # pylint: disable=global-statement,invalid-name

    event_uid = EventUid(event)

    length = len(_stored)
    exceeding = length - const.KEEP_LAST_MANY

    if exceeding > 0:
        for key in _stored:
            del _stored[key]
            break

    to_send_to = config.from_to.get(chat_id)

    if to_send_to:
        if event_uid not in _stored:
            _stored[event_uid] = []

        message = apply_plugins(message)
        if not message:
            return
        for recipient in to_send_to:
            fwded_msg = await send_message(event.client, recipient, message)
            _stored[event_uid].append(fwded_msg)

    existing_hashes.append(hash(message.text))


async def edited_message_handler(event):
    """Handle message edits."""
    message = event.message

    chat_id = event.chat_id

    if chat_id not in config.from_to:
        return

    logging.info(f"Message edited in {chat_id}")

    event_uid = EventUid(event)

    message = apply_plugins(message)

    if not message:
        return

    fwded_msgs = _stored.get(event_uid)

    if fwded_msgs:
        for msg in fwded_msgs:
            if config.CONFIG.live.delete_on_edit == message.text:
                await msg.delete()
                await message.delete()
            else:
                await msg.edit(message.text)
        return

    to_send_to = config.from_to.get(event.chat_id)

    for recipient in to_send_to:
        await send_message(event.client, recipient, message)


async def deleted_message_handler(event):
    """Handle message deletes."""
    chat_id = event.chat_id
    if chat_id not in config.from_to:
        return

    logging.info(f"Message deleted in {chat_id}")

    event_uid = EventUid(event)
    fwded_msgs = _stored.get(event_uid)
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


def start_sync():
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
