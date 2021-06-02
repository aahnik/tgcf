from typing import Dict

from telethon.tl.custom.message import Message


class EventUid:
    """The objects of this class uniquely identifies a message with its chat id and message id."""

    def __init__(self, event) -> None:
        self.chat_id = event.chat_id
        try:
            self.msg_id = event.id
        except:  # pylint: disable=bare-except
            self.msg_id = event.deleted_id

    def __str__(self) -> str:
        return f"chat={self.chat_id} msg={self.msg_id}"

    def __eq__(self, other) -> bool:
        return self.chat_id == other.chat_id and self.msg_id == other.msg_id

    def __hash__(self) -> int:
        return hash(self.__str__())


class DummyEvent:
    def __init__(self, chat_id, msg_id):
        self.chat_id = chat_id
        self.id = msg_id


stored: Dict[EventUid, Dict[int, Message]] = {}
