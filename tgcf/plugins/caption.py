import logging

from tgcf.plugins import TgcfMessage, TgcfPlugin


class TgcfCaption(TgcfPlugin):
    id_ = "caption"

    def __init__(self, data) -> None:
        self.caption = data
        logging.info(self.caption)

    def modify(self, tm: TgcfMessage) -> TgcfMessage:
        tm.text = f"{self.caption.header}{tm.text}{self.caption.footer}"
        return tm
