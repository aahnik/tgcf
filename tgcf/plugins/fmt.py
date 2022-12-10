import logging
from enum import Enum
from typing import Any, Dict

from pydantic import BaseModel  # pylint: disable=no-name-in-module

from tgcf.plugin_models import STYLE_CODES, Format, Style
from tgcf.plugins import TgcfMessage, TgcfPlugin


class TgcfFmt(TgcfPlugin):
    id_ = "fmt"

    def __init__(self, data) -> None:
        self.format = data
        logging.info(self.format)

    def modify(self, tm: TgcfMessage) -> TgcfMessage:
        if self.format.style is Style.PRESERVE:
            return tm
        msg_text: str = tm.raw_text
        if not msg_text:
            return tm
        style = STYLE_CODES.get(self.format.style)
        tm.text = f"{style}{msg_text}{style}"
        return tm
