import logging

from pydantic import BaseModel  # pylint: disable=no-name-in-module

from tgcf.plugins import TgcfMessage, TgcfPlugin


class TgcfUnique(TgcfPlugin):
    id_ = "unique"

    def __init__(self, data) -> None:
        self.max = 5
        self.messages = []

    def modify(self, tm: TgcfMessage) -> TgcfMessage:
        if self.text_unique(tm):
            logging.info("Message passed unique filter")
            self.include_message(tm)
            return tm

    def text_unique(self, tm: TgcfMessage) -> bool:
        return tm.raw_text not in self.messages

    def include_message(self, tm: TgcfMessage):
        self.messages.insert(0, tm.raw_text)
        if len(self.messages) > self.max:
            self.messages.pop()
            logging.info("Too many messages. Remove 1 oldest")

