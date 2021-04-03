from telethon import events, TelegramClient
from tgcf.config import CONFIG, API_HASH, API_ID, SESSION


from_to = {}

KEEP_LAST_MANY = 10000

existing_hashes = []

_stored = {}


for forward in CONFIG.forwards:
    from_to[forward.source] = forward.dest


class EventUid:
    def __init__(self, event):
        self.chat_id = event.chat_id
        try:
            self.msg_id = event.id
        except:
            self.msg_id = event.deleted_id

    def __str__(self):
        return f'chat={self.chat_id} msg={self.msg_id}'

    def __eq__(self, other):
        return self.chat_id == other.chat_id and self.msg_id == other.msg_id

    def __hash__(self) -> int:
        return hash(self.__str__())


async def new_message_handler(event):
    chat_id = event.chat_id

    if chat_id not in from_to:
        return

    message = event.message

    global _stored

    event_uid = EventUid(event)

    length = len(_stored)
    exceeding = length - KEEP_LAST_MANY

    if exceeding > 0:
        for key in _stored:
            del _stored[key]
            break

    to_send_to = from_to.get(chat_id)

    if to_send_to:
        if event_uid not in _stored:
            _stored[event_uid] = []

        for recipient in to_send_to:
            fwded_msg = await event.client.send_message(recipient, message)
            _stored[event_uid].append(fwded_msg)

    existing_hashes.append(hash(message.text))


async def edited_message_handler(event):
    message = event.message

    chat_id = event.chat_id
    if chat_id in from_to:

        event_uid = EventUid(event)

        fwded_msgs = _stored.get(event_uid)
        if fwded_msgs:
            for msg in fwded_msgs:
                await msg.edit(message.text)
            return
        else:
            to_send_to = from_to.get(event.chat_id)
            for recipient in to_send_to:
                await event.client.send_message(recipient, message)


async def deleted_message_handler(event):
    chat_id = event.chat_id
    if chat_id in from_to:
        event_uid = EventUid(event)
        fwded_msgs = _stored.get(event_uid)
        if fwded_msgs:
            for msg in fwded_msgs:
                await msg.delete()
            return


ALL_EVENTS = {
    'new': (new_message_handler, events.NewMessage()),
    'edited': (edited_message_handler, events.MessageEdited()),
    'deleted': (deleted_message_handler, events.MessageDeleted())
}


def start_sync():
    client = TelegramClient(SESSION, API_ID, API_HASH)
    for key, val in ALL_EVENTS.items():
        print(f'Adding event {key}')
        client.add_event_handler(*val)
    client.start()
    client.run_until_disconnected()
